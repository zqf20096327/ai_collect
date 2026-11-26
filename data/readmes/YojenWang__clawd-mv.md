# clawd-mv

**给一首歌做手绘动画 MV —— 把这件事变成 AI 能直接执行的流程。**

作者：绘梨衣 Yojen · MIT 许可

[![MIT](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![p5.js](https://img.shields.io/badge/p5.js-p5.brush-ED225D?style=flat-square)

---

## 介绍

不是"AI 一键生成 MV"。

是一个**技能包**：一份 292 行的 `SKILL.md` + 一个无头渲染器。你把 `SKILL.md` 给一个会写代码的模型，它就会照着这份流程，把一首歌切成 40–60 个镜头、逐句配画面、每个镜头内部都设计好动作节拍，最后渲染成 MP4。

基于 [ClaudeAnimationBase](https://github.com/JohnHeibel/ClaudeAnimationBase)（p5.js + p5.brush + Clawd 小螃蟹）。
## 使用方法

**方式一：放进 AI 的技能目录**

```bash
git clone https://github.com/YojenWang/clawd-mv ~/.dsh/skills/clawd-mv
```

然后直接对 AI 说「给这首歌做一支手绘 MV」，它会自动读取这份流程。

**方式二：手动喂给模型**

把 `SKILL.md` 整个贴进对话，让它照着执行。



## 为什么要做成"流程"而不是"提示词"

直接跟 AI 说"给这首歌做个 MV"，你会得到：

- 一个镜头铺一整个段落 → **画面单调无聊**
- 每个镜头是一张静止的画，靠推近来假装有变化 → **像 PPT**
- 画面和歌词没关系，一整段氛围镜头糊过去 → **不知道在讲什么**

`SKILL.md` 里的每一条规则，都是为了堵住这些具体的失败。而且大部分规则不是凭空写的，是用户真的骂过之后才写下来的。

比如这条：

> 用户原话："要每一个镜头内也有变化，像动画片一样。"

于是就有了「四层运动」的硬性要求 —— 角色表演、次要动作、环境生命、摄影机，**缺一层就算"死镜头"**。

再比如：

> 用户原话："每个分镜的剧情都要单独写，不然和 PPT 有什么区别？"

于是每个镜头必须填三行：**想要**（这一镜里他想干什么）、**阻碍**（什么挡住了）、**结果**（镜头结束时状态变了）。

## 内容

`SKILL.md` 十章，292 行：

| 章节 | 内容 |
|---|---|
| 0. 四条铁律 | 先故事后代码、镜头要密、画面咬住歌词、每个镜头内部要有变化 |
| 1. 立项：故事板先行 | Logline / 世界 / 母题 / 情绪弧 / 分镜表；**镜头密度表**（前奏 20-30s 至少 5-7 镜） |
| 2. 音乐与逐句时间轴 | 怎么把歌词和节拍对到时间码上 |
| 3. 工程搭建 | 项目骨架 |
| 4. 镜头：一镜一函数 | 用覆盖率剪出密度 |
| 5. 渲染：先测速，再决定画质 | 不同画质档位的耗时 |
| 6. 自检 | 不能只看代码，必须逐帧看 |
| 7. 交付 | 输出规格 |
| 8. 故障速查 | 踩过的坑 |
| 9. 时间预算 | 按 4070 实测的数据 |

## 渲染器

`scripts/render.py` —— 基于 Edge headless + CDP 的无头渲染，288 行，支持：

```bash
# 抽单帧检查构图
python render.py --stills=1.2,3.4 --out=out/stills

# 接触表：一次看多帧
python render.py --sheet=0.5,1,1.5 --cols=4 --w=480 --out=out/check/a.jpg

# 帧条：逐帧检查某个镜头有没有动
python render.py --strip=2.0:2.5 --cols=6 --w=320 --out=out/check/strip.jpg

# 局部裁剪（看脸的表情）
python render.py --sheet=2.1 --crop=760,300,400,400 --w=600 --out=out/check/face.jpg

# 渲帧序列
python render.py --frames --range=0:8 --workers=2 --fps=24 --out=out/frames

# 编码成 MP4
python render.py --encode --fps=24 --audio=assets/song.mp3 --out=out/video.mp4
```

依赖：`pip install websocket-client`，Edge 浏览器（Windows 默认路径，可改 `render.py` 顶部的 `EDGE` 常量）。



## 已知限制

- **渲染器是 Windows + Edge 专用的。** `EDGE` 路径写死在 `render.py` 顶部，macOS / Linux 需要自己改。
- **没有内置示例项目。** 仓库里只有流程和渲染器，`studio.html` 得自己搭（或者让 AI 照着 SKILL.md 搭）。
- **它不生成音乐，也不分析音频。** 时间轴要你自己（或 AI）对。

## 许可

MIT。署名 **绘梨衣 Yojen** 即可自由使用与修改。

---

**用着有问题？** 提 [Issue](https://github.com/YojenWang/clawd-mv/issues) 或发邮件 yojenwang@163.com。
