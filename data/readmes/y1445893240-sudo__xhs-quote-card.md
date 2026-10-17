# 小红书金句图文起号

> 🎯 **一句话说明**：把一段「带中文字幕的名人访谈/演讲视频」，自动变成一套**可以直接发小红书**的金句图文包（卡片图 + 标题 + 正文 + 话题标签）。
>
> 你不用会剪辑、不用会设计、不用会写文案——**给 AI 一个视频，它帮你把发布物料全部做好**。

---

## 📌 这个 Agent 是干什么的？

很多做小红书的朋友都有这样的痛点：

> 看到一个很好的访谈视频（比如莫言、董宇辉、马云的访谈），里面有一句句特别打动人的话，
> 想做成「金句卡片」发小红书吸引粉丝，但——
> - ❌ 不会剪辑，不知道从哪句开始截
> - ❌ 不会设计，做出来的图丑
> - ❌ 不会写文案，不知道配什么标题和话题
> - ❌ 找代做又贵又慢

**「小红书金句图文起号」就是来解决这个问题的。** 你只需要提供一个视频，它全自动完成：

```
视频 ──▶ 1. 自动抽帧（把视频拆成一张张画面）
         2. OCR 识别字幕（把每句话从画面上抠出来）
         3. 智能挑金句（按"是否打动人心"自动评分排序）
         4. 生成 3:4 竖版金句卡片（小红书标准尺寸，自动排版美化）
         5. 配好发布文案（标题 + 正文 + 话题标签）
         输出 ──▶ 一套可以直接发布的小红书图文包
```

**产出物**（都在一个输出文件夹里）：
- 🖼️ `card_1.png ~ card_N.png` — 每句金句一张竖版卡片（1080×1440，小红书图集标准尺寸）
- 📝 `小红书文案.txt` — 配好的标题 + 正文 + 话题标签，复制就能发
- 📄 `quotes.json` — 全部金句及评分，方便你自己再挑

**适合谁用**：
- 想做「名人语录」「金句分享」「观点输出」类账号的新手博主
- 需要批量出图的运营人员
- 任何想把视频内容转成图文的人

---

## ✨ 核心特性

- **纯本地运行**：不依赖任何云端 key、不需要挂代理、**你的视频不会上传到任何服务器**（隐私安全）
- **一键出稿**：一条命令跑完全流程，产出可直接发布的小红书图文包
- **规则引擎挑金句**：按「长度 + 情感浓度 + 句式 + 口语过滤」自动评分排序，不依赖 LLM，零成本
- **3:4 竖版卡片**：1080×1440，小红书/抖音图集标准尺寸，6 套深色高级配色（暖金/深紫/深绿/酒红/深海蓝）
- **自动兜底**：底部字幕识别不到时自动改用整帧 OCR 重试
- **全中文注释**：脚本结构清晰，词库/规则/文案模板都可自由扩展

---

## 🚀 使用指南（小白版）

有两种使用方式，**推荐方式一**（最简单，适合完全不懂编程的人）。

### 方式一：装进 WorkBuddy 使用（推荐，零命令行）

[WorkBuddy](https://www.workbuddy.cn) 是腾讯出品的 AI 办公平台（电脑桌面客户端）。装好后，你**直接打字说话**就能让 AI 干活，不用记任何命令。

**第一步：把本项目装成 WorkBuddy 的「技能」**

打开你的电脑文件管理器，找到 WorkBuddy 的技能目录：

- **Windows**：`C:\Users\你的用户名\.workbuddy\skills\`
  （例如 `C:\Users\Administrator\.workbuddy\skills\`）
- **macOS**：`/Users/你的用户名/.workbuddy/skills/`

> 💡 如果看不到 `.workbuddy` 文件夹，是因为它被隐藏了：
> - Windows：文件管理器 → 查看 → 勾选「隐藏的项目」
> - macOS：访达 → 按 `Cmd + Shift + .`（点号）显示隐藏文件

**第二步：把整个项目文件夹复制进去**

把本仓库整个文件夹复制到上面的 `skills\` 目录里，最终效果应该是：

```
C:\Users\Administrator\.workbuddy\skills\
└── xhs-quote-card\            ← 整个项目文件夹
    ├── SKILL.md               ← 技能定义文件（WorkBuddy 靠它识别）
    ├── run.py
    ├── scripts\
    └── ...
```

**第三步：安装依赖（一次性）**

打开终端（Windows 按 `Win + R`，输入 `cmd` 回车），执行：

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple rapidocr_onnxruntime opencv-python-headless pillow
```

> 如果提示 `pip 不是内部或外部命令`，说明没装 Python。先到 [python.org](https://www.python.org/downloads/) 下载安装 Python 3.10+（安装时记得勾选 **Add python.exe to PATH**），再重试。

**第四步：重启 WorkBuddy，直接对话使用**

重启 WorkBuddy（让新技能生效），然后新建对话，直接对 AI 说：

```
帮我用「小红书金句图文起号」把 D:\视频\莫言访谈.mp4 做成金句卡片
```

AI 会自动调用这个技能，跑完流程后把卡片图 + 文案直接发给你。**就这么简单。**

---

### 方式二：命令行使用（适合懂一点电脑的人）

**安装依赖**（需要 Python 3.10+）：

```bash
# 建议用独立虚拟环境
python -m venv .venv
# Windows:
.venv/Scripts/pip install -i https://pypi.tuna.tsinghua.edu.cn/simple \
    rapidocr_onnxruntime opencv-python-headless pillow
# macOS / Linux:
.venv/bin/pip install -i https://pypi.tuna.tsinghua.edu.cn/simple \
    rapidocr_onnxruntime opencv-python-headless pillow
```

> `rapidocr_onnxruntime` 首次运行会自动下载 OCR 模型（约 15MB，来自官方源）。

**一键全流程**：

```bash
python run.py "访谈视频.mp4" --author "莫言" --title "他这段话治好了我的焦虑" --out-dir output
```

**输出目录**：

```
output/
├── quotes.json          # 评分排序的金句列表
├── card_1.png ...       # 每句一张 3:4 竖版金句卡片
└── 小红书文案.txt        # 配好的标题+正文+话题标签
```

### 分步使用（调试 / 复用中间结果）

```bash
# 1. 抽帧（默认每1秒一帧）
python scripts/extract_frames.py 视频.mp4 --out frames --interval 1.0

# 2. OCR 底部字幕（字幕不在底部时加 --ocr-full）
python scripts/ocr_subs.py frames --out subs.json --subtitle-ratio 0.32

# 3. 选金句（评分排序取前N）
python scripts/pick_quotes.py subs.json --top 6 --out quotes.json

# 4. 生成卡片（可手动指定金句）
python scripts/make_card.py "金句文本" --out card.png --author 人名 --title 大标题
```

---

## ⚙️ 参数一览

| 参数 | 说明 | 默认 |
|---|---|---|
| `--interval` | 抽帧间隔（秒），字幕滚动快可调 0.5 | 1.0 |
| `--author` | 金句作者/人物署名 | - |
| `--title` | 卡片顶部大标题 | - |
| `--top` | 最多生成卡片数 | 6 |
| `--ocr-full` | 对整帧 OCR（字幕不在底部时） | false |
| `--palette` | 配色 0-4（暖金/深紫/深绿/酒红/深海蓝） | 随机 |
| `--skip-card` | 只出金句不出卡片 | false |
| `--frames-dir` | 复用已有帧目录 | - |

---

## 🧩 工作原理

```
视频 ──抽帧──▶ 帧图片 ──OCR(底部32%)──▶ 字幕文本(带时间戳)
                                              │
                    去重合并相邻相似帧 ◀────────┘
                          │
                    清洗 + 规则评分
                          │
              ┌───────────┼────────────┐
              ▼           ▼            ▼
        3:4竖版卡片   金句列表json    小红书文案
```

**金句评分规则**（`scripts/pick_quotes.py`）：
- 长度适中 (12-45 字) `+2`
- 感叹/疑问结尾 `+2`，句号结尾 `+1`
- 命中情感词库（人生/选择/坚持/勇气...）`+2/词`
- 含转折/排比句式 `+2`，引用式 `+1`
- 口语填充开头（其实/就是/然后...）`-1`

---

## 🛠 定制指南

| 想改什么 | 改哪里 |
|---|---|
| 情感词库 / 评分规则 | `scripts/pick_quotes.py` |
| 卡片配色 / 排版 / 水印 | `scripts/make_card.py` |
| 小红书文案模板 | `run.py` 的 `build_copywriting()` |
| 字幕裁剪比例 | `scripts/ocr_subs.py` 的 `--subtitle-ratio` |

---

## 🐛 常见问题

**Q: 识别不到字幕？**
A: 先加 `--ocr-full` 对整帧识别；还不行说明视频没有硬字幕（AI 配音+软字幕），先用 ffmpeg 烧录字幕再跑：
```bash
ffmpeg -i input.mp4 -vf "subtitles=sub.srt" -c:a copy output.mp4
```

**Q: 能在 WorkBuddy 里用吗？**
A: 可以，而且这是推荐的用法。按上面「方式一」把整个文件夹复制到 `~/.workbuddy/skills/` 目录，重启 WorkBuddy 后直接对话说"帮我用小红书金句图文起号做…"即可，AI 会自动帮你完成。

**Q: 金句不准？**
A: 规则引擎是启发式的，最优解是让 AI/人工从 `quotes.json` 里再筛一遍，然后用 `make_card.py` 手动生成指定金句的卡片。

**Q: 需要联网或 API Key 吗？**
A: 不需要。所有处理都在本机完成，唯一一次联网是首次运行自动下载 OCR 模型（约 15MB）。

**Q: 对视频有什么要求？**
A: 视频里要有**烧录进去的硬字幕**（画面里直接能看到字），AI 配音但没有字幕的不行（可先烧录字幕）。名人访谈/演讲/口播视频效果最好。

---

## 📄 License

MIT

---

**Made for 内容创作者 · 不占用云额度 · 视频不出本机**
