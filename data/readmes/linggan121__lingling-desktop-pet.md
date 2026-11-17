# 灵灵 · 桌面 AI 助理桌宠

> 一只住在桌面角落的小宠物，也是一个能帮你干活的助理。
> **把文件拖到她身上，回一个数字，就帮你转好格式。**

<p align="center">
  <img src="docs/screenshots/icon.png" width="120" alt="灵灵">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-7c3ddb" alt="License">
  <img src="https://img.shields.io/badge/python-3.9%2B-7c3ddb" alt="Python">
  <img src="https://img.shields.io/badge/platform-Windows-7c3ddb" alt="Platform">
  <a href="https://github.com/linggan121/lingling-desktop-pet/releases/latest"><img src="https://img.shields.io/badge/下载-Windows%20exe-2ea44f" alt="Download"></a>
</p>

<p align="center">
  <img src="docs/screenshots/hero.png" width="320" alt="桌宠">
  <img src="docs/screenshots/chat-demo.png" width="230" alt="聊天">
</p>

---

## 现在能做什么

- **文件助理（核心）**
  把文件（或文件夹）拖到灵灵身上，她会列出来并给编号选项：

  **选项会按文件内容来给**，不是固定的：

  ```
  拖一份带表格的 Word：
  1. 提取文字
  2. 转成 Markdown
  3. 导出里面的表格（CSV）

  拖一张图片：
  1. 转成 webp
  2. 转成 jpg（质量 80）
  3. 转成 png
  4. 长边缩到 1080
  5. 转成 PDF
  ```

  - 回 **数字** → 直接执行
  - 直接说 **「转成 heic」「质量 60」「盯着这个文件夹」** → 复述确认后执行
  - **全部走内置引擎**，不用装任何东西：图片 30+ 格式、HEIC、图片→PDF、PDF 拆图/提字、
    Word/Excel/PPT 提文字、文档转 Markdown、表格导 CSV、提取文档图片、zip 打包解压、
    视频→mp4/mp3/gif
  - **盯着文件夹**：内置监听，新文件自动转到 `converted/`（说「停止监听」就停）
  - 不会的事直接说不会，不瞎答应
- **文件位置可点**：聊天里出现的文件都是青绿色小胶囊，点一下在资源管理器里打开并选中
- **记得聊天**：对话、拖进来的文件、转好的文件都存在本地，关掉窗口再打开还在，编号也还能接着回
- **能翻历史**：聊天窗支持鼠标滚轮、PageUp/PageDown、Home/End，右侧有滚动条；往上翻时新消息不会把你拽回底部
- **桌面住客**：无边框、不占任务栏、置顶、可拖动、位置记忆、贴边吸附、托盘、单实例
- **会聊天**：接任意 OpenAI 兼容服务（DeepSeek / 豆包 / 硅基流动 / Kimi / 智谱 / 通义 / OpenRouter / 本地 Ollama），流式逐字回复；没配 Key 时只说自己内置的台词；**也可以一键切到本机 Ollama，完全离线**
- **记得你**：每聊 8 轮提炼一次「关于你的事」，存成本地事实卡
- **看屏幕**：右键「看看我在干什么」，截图让视觉模型点评；窗口标题命中密码 / 银行 / 支付等词时连截图都不截
- **有脾气**：回复里带 `<mood:开心>` 这类情绪标记会自动切动作，标记本身不显示

<p align="center">
  <img src="docs/screenshots/settings.png" width="420" alt="设置">
</p>

---

## 快速开始

### 方式一：直接用 exe

到 **[Releases](https://github.com/linggan121/lingling-desktop-pet/releases/latest)** 下载安装包，双击即可。
首次启动约 5–8 秒（自带转换引擎，体积比以前大），之后很快。

运行数据在：

```
%LOCALAPPDATA%\灵灵\
├── settings.json   位置、模型配置
├── chat_log.json   聊天记录（含文件链接）
├── history.json    给模型看的对话历史
├── memory.json     关于你的事实卡
├── lines.json      台词库（可改）
├── persona.json    人设（可改）
└── _frames.pkl     切帧缓存（可删）
```

想变成绿色便携版：在 exe 同目录建一个 `data` 文件夹，程序会优先用它。

### 方式二：源码运行

```bash
pip install -r requirements.txt
pythonw 灵灵.pyw              # 启动
python  灵灵.pyw --selftest   # 自检
python  灵灵.pyw --settings   # 启动并打开设置
```

需要 Python 3.9+（tkinter 是标准库自带的）。

### 文件转换需要什么？

**什么都不用装。** 转换引擎已经内置在灵灵里（Pillow / PyMuPDF / pillow-heif / py7zr 等）。
只有**视频/音频**转换第一次用时会自动下载 FFmpeg（约 80 MB，存到 `%LOCALAPPDATA%\灵灵\ffmpeg.exe`），
之后再转就不用联网了。

---

## 文件技能怎么用

**拖**：把文件或文件夹拖到她身上 → 聊天窗自动打开 → 回数字或直接下指令。

**不想拖**：右键 →「技能 → 选文件转换…」。

支持的说法：

| 你说 | 她做 |
|---|---|
| `1` / `2` / `3` | 执行对应编号选项 |
| `转成 webp`、`换成 png`、`导出 pdf` | 转换格式 |
| `转成 jpg，质量 80` | 带质量参数 |
| `解压` | 解压 zip / 7z 到旁边 |
| `你支持哪些格式` | 列出 270 种格式 |
| `盯着这个文件夹，转成 jpg` | 后台监听，新文件自动转 |
| `提取文字` | PDF / Word / PPT → txt |
| `转成 mp4`、`提取音频 mp3`、`转成 gif` | 视频/音频转换（首次会下 FFmpeg）|
| `停止监听` | 结束监听 |

做不到的（合并、拆分、重命名、整理、OCR、翻译…）她会直接说明，不会假装能做。

---

## 接大模型

右键灵灵 →「设置…」，选服务商 → 填 Key →「测试连接」→ 成功会自动保存。

| 服务商 | 接口地址 | 备注 |
|---|---|---|
| DeepSeek | `https://api.deepseek.com` | Key 是 `sk-` 开头 |
| 豆包（火山方舟） | `https://ark.cn-beijing.volces.com/api/v3` | 模型填 **Model ID**（如 `doubao-seed-2-1-turbo-260628`） |
| 硅基流动 / Kimi / 智谱 / 通义 / OpenAI / OpenRouter | 内置预设 | 选好自动填地址和模型 |
| 本地 Ollama | `http://127.0.0.1:11434/v1` | 不用 Key、不出网 |

- **不知道 Key 是哪家的**：粘进去点「自动匹配服务商」，会并行试常见服务商
- **视觉模型**（看屏幕用）单独一栏，留空就用对话模型
- 豆包默认关掉「深度思考」（开着首字要 20 秒），想开在 `settings.json` 的 `llm` 里加 `"thinking": "enabled"`

---

---

## 本地模型（完全离线）

不想用云端、或者要断网用，可以接本机的 [Ollama](https://ollama.com)：

1. 装 Ollama，命令行拉一个模型（4 GB 显存推荐 3B）：
   `ash
   ollama pull qwen2.5:3b
   `
2. 右键灵灵 →「设置…」→ 点左下「**本地模型**」→ 从列表里选一个 → 自动填好地址/模型并测试连通 → 保存

之后聊天推理全部在本机完成：

- 聊天内容、记忆、文件都不出本机
- 断网也能聊、也能转文件
- 不花 token 钱

> 设置里还有一个「本地模型优化」开关：本地小模型回复更短（120 tokens）、温度更低（0.75），不容易跑题。
> 旁边的「生成上下文配置」会写一份 Modelfile（
um_ctx 4096），按提示执行
> ollama create qwen2.5-lingling -f Modelfile.lingling 就能把上下文从默认 2048 放大到 4096。

视觉模型（看屏幕）也可以填本地多模态模型（如 qwen2.5vl:3b），这样连截图分析都不出网。

## 交互一览

| 操作 | 反应 |
|---|---|
| 单击 | 摸头：压扁弹回 + 冒心心 + 说一句话 |
| 双击 | 打开聊天窗口 |
| 拖动 | 跟着鼠标跑，松手记住位置 |
| **拖文件到她身上** | 聊天窗打开并列出文件 + 编号选项 |
| 右键 | 聊天 / 看屏幕 / 逗一下 / 心情 / 投喂 / 换动作 / 换装 / 技能 / 窗口搬回来 / 设置 / 回到右下角 / 退出 |
| 托盘 | 显示隐藏、设置、叫回屏幕、退出 |

---

## 项目结构

```
.
├── 灵灵.pyw              入口
├── ling/
│   ├── pet.py            窗口、交互、聊天、技能接线
│   ├── dnd.py            拖放接收（Win32 WM_DROPFILES）
│   ├── convert_engine.py 内置转换引擎（图片/PDF/Office/压缩包/媒体）
│   ├── intent.py         自然语言指令 → 意图（部分场景在用）
│   ├── llm.py            OpenAI 兼容 / Ollama / 多模态
│   ├── vision.py         看屏幕：截屏、隐私过滤
│   ├── frames.py         切帧 + 缓存
│   ├── anim.py           帧动画
│   ├── bubble.py         气泡
│   ├── mood.py           情绪解析
│   ├── persona.py        人设 + 时间上下文
│   ├── memory.py         事实卡
│   ├── config.py         设置读写
│   ├── settings_ui.py    设置窗口
│   ├── tray.py           托盘
│   └── paths.py          路径 + 原子写
├── tests/                61 个单元测试（不弹窗、不联网）
├── assets/               精灵图、图标
├── data/                 默认台词与人设
└── docs/screenshots/     截图
```

跑测试：

```bash
python -m unittest discover -s tests -v
```

---

## 打包

```bash
pyinstaller --onefile --windowed --name 灵灵 --icon assets/app.ico ^
  --add-data "assets;assets" ^
  --add-data "data/lines.json;data" ^
  --add-data "data/persona.json;data" ^
  灵灵.pyw
```

---

## 隐私

- 不联网也能用；只有填了 Key 并发消息 / 看屏幕时才会请求你配置的接口
- Key 只存在本机 `settings.json`，没有遥测
- 看屏幕前检查前台窗口标题，命中隐私词直接放弃，截图不落盘
- 聊天记录、记忆都在本地，可随时删除；文件只在你自己电脑上被转换，不上传

---

## 已知限制

- 视频/音频转换需要 FFmpeg：首次使用自动下载（约 80 MB 压缩包 / 160 MB 可执行文件），之后离线可用
- Office 文档目前只做「提取文字 / 转 CSV」，不做 docx→pdf（那需要 LibreOffice）
- 拖拽只在 Windows 上验证过
- 素材一帧约 112×198 像素，放大偏软；tkinter 的透明是色键方案，边缘是硬边
- 文档只做「提取文字 / Markdown / 表格 CSV / 提图片」，不做 docx→pdf（需要 LibreOffice）

---

## 素材版权

- **代码**采用 [MIT](LICENSE)，可自由使用、修改、商用
- **角色立绘与图标**不是本项目原创，来自 [Petdex](https://petdex.dev/zh) 的用户投稿宠物包，**不在 MIT 授权范围内**

> Petdex 官方 FAQ：*Pets are user-submitted fan art. Petdex does not claim rights to any underlying IP.*
> *Every pet on Petdex is free to install and use. Pets keep credit to their original authors.*

商用前请换成自己有权利的素材——替换 `assets/spritesheet.webp` + `frames.json` 即可，代码不用改。
详见 [assets/NOTICE.md](assets/NOTICE.md)。

## License

代码：[MIT](LICENSE)（素材除外）
