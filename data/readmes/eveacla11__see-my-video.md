# 怎么让 AI 真的"看见"你发的视频

**一份踩坑记录：把视频喂给 AI，以及在自建服务器上传视频会遇到的两个隐形陷阱。**

AI（Claude 这类）能读文字、能看图片，但**打不开视频文件**。
给它一个 mp4，它只能看着文件名干瞪眼。

这篇讲怎么解决，以及三个你一定会撞上的坑。

---

## 这个仓库里有什么

| 文件 | 是什么 |
|---|---|
| `extract_frames.py` | 能直接跑的抽帧脚本，输出帧图片 + 一段可以贴给 AI 的清单 |
| `api_snippet.py` | 抽帧后直接喂给 Claude API（自己接前端的话看这个） |
| `server_snippet.py` | 切片上传 + 轻量播放版（FastAPI 示例，抄走改个目录就能用） |
| `upload_snippet.js` | 前端切片上传，带进度和重试 |

```bash
python extract_frames.py 视频.mp4
```

---

## 核心思路：一句话

视频拆开看，本质就是一串画面。
用 [ffmpeg](https://ffmpeg.org/) 把视频抽成几张关键帧图片，AI 一张张看过去，就等于看了这段视频。

思路不新鲜——GitHub 上有个两千星的项目
[claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video)
走的同一条路，做得比这里完整得多（去重、说话人分离、可视化查看器）。
**想要开箱即用的成熟工具，去用它。**

这篇的价值在别处：如果你是**自己给 AI 搭一双眼睛**——服务架在家里、手机远程访问——
那么下面的坑二和坑三，是那类本地工具不会遇到、而你一定会撞上的。

---

## 坑一：帧怎么抽才聪明

最笨的办法是掐秒表均匀取，比如 17 秒的视频取 8 张。

问题是拍猫这种"趴半天不动、突然暴起扑玩具"的视频，
名场面可能正好卡在两帧之间漏掉。

**解法：让 ffmpeg 按画面变化抽帧**，顺便把每帧在原视频里的时间点也拿出来。

```bash
ffmpeg -i 视频.mp4 \
  -vf "select='eq(n,0)+gt(scene,0.25)',showinfo,scale=-2:720" \
  -vsync vfr -frames:v 12 帧_%02d.jpg
```

- `gt(scene,0.25)` — 画面变化超过阈值就抓一帧，静止画面不浪费配额
- `eq(n,0)` — 强制保留第一帧（否则开头可能一张都没有）
- `-vsync vfr` — 防止 ffmpeg 自作主张补帧
- `showinfo` — 每帧的时间戳会打进 stderr，形如 `pts_time:4.000`，正则抓出来即可

有了时间戳，AI 就能说出"**第 12 秒**猫回头看了你一眼"，
而不是含糊的"中间有一帧"。

**别忘了兜底**：一镜到底的静态视频切不出场景，得回退均匀取样。

```python
if len(frames) < 3:
    # 场景法没切出东西，退回均匀取样
    fps = n / duration
    subprocess.run([ffmpeg, "-y", "-i", src,
                    "-vf", f"fps={fps},scale=-2:720",
                    "-frames:v", str(n), out_pattern])
```

抽完帧，把路径列表连同时间戳一起写进给 AI 的提示词里，让它逐张读就行：

```
- video.mov（这是一段视频，17秒。已按画面变化抽出 5 帧关键画面）:
  - frames/f_01.jpg（第 0.0 秒）
  - frames/f_02.jpg（第 3.2 秒）
  ...
```

---

## 坑二：上传"进度 100% 之后失败"

**症状极具迷惑性**：进度条稳稳爬到 100%，然后报上传失败。
看起来像服务器坏了，其实不是。

如果你的服务架在家里、靠 Cloudflare 隧道（或类似反代）暴露到公网——
**大文件的单个请求会撞上约 100 秒的等待上限**：

浏览器把文件交给 Cloudflare 边缘节点很快（所以进度条直冲 100%），
但边缘节点往你家里灌是慢的，没灌完就直接判超时。

**解法：切片上传。** 把文件剁成 4MB 一块串行发，每块几秒落地，永远碰不到那堵墙。

前端：

```js
const CHUNK = 4 * 1024 * 1024;
const uploadId = crypto.randomUUID().replace(/-/g, "");
const total = Math.ceil(file.size / CHUNK);

for (let i = 0; i < total; i++) {
  const form = new FormData();
  form.append("chunk", file.slice(i * CHUNK, (i + 1) * CHUNK));
  form.append("upload_id", uploadId);
  form.append("index", i);
  form.append("total", total);
  form.append("filename", file.name);

  // 每块失败重试 2 次，网络抖一下不至于前功尽弃
  const data = await postWithRetry("/api/upload/chunk", form);
  onProgress(Math.round(((i + 1) / total) * 100));
  if (data.path) finalPath = data.path;   // 最后一块的响应带正式路径
}
```

服务端（FastAPI 示例）：

```python
@app.post("/api/upload/chunk")
async def upload_chunk(chunk: UploadFile = File(...), upload_id: str = Form(...),
                       index: int = Form(...), total: int = Form(...),
                       filename: str = Form("")):
    uid = re.sub(r"[^a-f0-9]", "", upload_id.lower())[:32]   # 只认十六进制，防路径穿越
    if not uid:
        return {"ok": False, "error": "bad upload_id"}

    tmp = UPLOAD_DIR / f"part_{uid}.tmp"
    with tmp.open("ab" if index > 0 else "wb") as f:      # 第一块新建，之后追加
        while piece := await chunk.read(1024 * 1024):
            f.write(piece)

    if index + 1 < total:
        return {"ok": True, "received": index + 1, "total": total}

    name = f"{uuid.uuid4().hex}{Path(filename).suffix}"     # 最后一块到齐，改名转正
    tmp.rename(UPLOAD_DIR / name)
    return {"ok": True, "filename": filename, "path": f"/uploads/{name}"}
```

顺带两件小事：

- 单请求上传也别用 `await file.read()` 一口吞——手机视频动辄上百 MB，会把内存吃穿。用循环分块写盘。
- 用 `XMLHttpRequest` 而不是 `fetch` 做单请求上传，因为它有 `upload.onprogress`，能给用户看到真实进度。

---

## 坑三：传上去了，但播放永远卡在第一帧

又一个不报错的坑。视频出现在页面里，第一帧好好显示着，点播放——没反应。

**病因是码率。** 手机拍的 1080p 视频码率动辄 20+ Mbps，
播放它需要每秒供二十多兆的带宽，家用隧道供不起。
播放器不报错，就是干等着，看起来像坏了。

（上传能成功是因为切片在慢慢爬；播放要的是实时供流，两回事。）

**解法：存档归存档，播放归播放。** 上传成功后自动转一份低码率播放版：

```bash
ffmpeg -i 原片.mov -vf scale=-2:720 \
  -c:v libx264 -preset veryfast -crf 26 \
  -movflags +faststart \
  -c:a aac -b:a 96k 播放版.mp4
```

- `crf 26` — 画质够看，体积暴降。实测 21.8MB → 0.6MB，小了 35 倍
- `+faststart` — 把元数据挪到文件头，浏览器不用下完整个文件就能起播（**这个参数很关键**）
- 原片原封不动留着，页面里播小的

在消息数据结构里给附件加个 `play` 字段，前端优先播它、没有才回退原片：

```js
video.src = attachment.play || attachment.path;
```

**另外检查一下你的静态文件服务支不支持 Range 请求**（断点续传）。
不支持的话 iOS 上的视频永远播不了。FastAPI 的 `StaticFiles`、
nginx、Caddy 默认都支持，返回 206 就对了：

```bash
curl -s -o /dev/null -w "%{http_code}\n" -H "Range: bytes=0-1" http://你的地址/uploads/xxx.mp4
# 206 = 支持，200 = 不支持，得换文件服务方案
```

---

## 如果你是 API + 自己的前端

上面的做法是把帧路径列进提示词，让带工具的 AI（Claude Code 那类）自己去读。
如果你直接调 API，链路更短：**帧转 base64 直接塞进 messages**，模型立刻就看见。

```python
content = [{"type": "text", "text": "这是一段 7 秒的视频，抽了 3 帧关键画面……"}]
for path, sec in frames:
    content.append({"type": "text", "text": f"第 {sec:.1f} 秒："})
    content.append({
        "type": "image",
        "source": {"type": "base64", "media_type": "image/jpeg",
                   "data": base64.standard_b64encode(Path(path).read_bytes()).decode()},
    })
content.append({"type": "text", "text": "这段视频里发生了什么？"})
```

每帧前面单独放一行时间点，模型才能引用"第 3.7 秒那帧"。完整可运行版本见 `api_snippet.py`。

**但要算钱。** 图片按尺寸吃 token，约等于 `宽 × 高 / 750`：

| 分辨率 | 每帧 token | 8 帧合计 |
|---|---|---|
| 720p (1280×720) | ≈ 1230 | ≈ 9800 |
| 480p (854×480) | ≈ 550 | ≈ 4400 |

抽帧数和分辨率是仅有的两个旋钮，按钱包拧。

**还有个隐性成本：API 是无状态的**，多轮对话要把历史整个重发。
聊到第十轮时，前面九条视频的帧全躺在上下文里，账单滚雪球。
实用做法：老视频的帧过几轮就撤掉，历史里只留模型当时给出的文字描述。

---

## 还能更进一步：声音

上面全是画面。视频 = 画面 + 声音，声音这条路也是通的：

用 **本地 Whisper**（开源语音识别，[faster-whisper](https://github.com/SYSTRAN/faster-whisper) 更快）
把音轨转成带时间戳的文字，和关键帧一起喂给 AI——
它就既看得见画面，又"听"得到内容。

```bash
ffmpeg -i 视频.mp4 -vn -ar 16000 -ac 1 音轨.wav
# 然后把 wav 交给 whisper，拿到带时间戳的转写
```

本项目的作者暂时没做这一步（画面的优先级更高），但方案是现成的，
想要完整体验的可以自己接上，或者直接用文章开头提到的 claude-real-video。

---

## 一句话总结

> AI 看不了视频，那就把视频翻译成 AI 看得懂的语言：
> 画面拆成带时间戳的图，声音转成文字。剩下的，它自己会看。

---

## 关于这篇

这些代码来自一个自建的 AI 伴侣项目，是 2026 年 8 月 7 日一天之内
从"能不能发视频"到"能看、能传、能播"撞出来的记录。
三段话的教训，是一整天的重启换来的。

**独立实现声明**：抽帧喂给 AI、切片上传、转轻量播放版这三件事是独立摸索的结果；
其中「按场景变化抽帧」和「每帧标注时间戳」两个点子，
参考自 [claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) 的项目介绍。
本仓库不含任何他人代码。

MIT License．拿去用，不用署名。
