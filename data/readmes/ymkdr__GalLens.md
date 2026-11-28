# GalLens

Windows 上的 Galgame 屏幕实时汉化工具：截取游戏画面 → 本地 OCR 识别日文 → 调用大模型流式翻译 → 在游戏上叠一层中文字幕。

**不注入进程、不读写游戏内存、不修改游戏文件**，只处理屏幕像素。

![界面](docs/screenshot.png)

![效果](docs/demo.png)

## 特性

- **纯外部程序**：只截图和叠窗口，不碰游戏本体，不会被反作弊或杀软误伤
- **本地 OCR**：用 Windows 自带的 OCR 引擎，20~30 ms 一帧，不联网
- **流式翻译**：首字 0.4 秒左右，边译边显示
- **图像兜底**：OCR 认不准时自动改让模型看图；也支持手动触发（竖排、艺术字、本身就是图片的场合）
- **按游戏记忆**：每个游戏的台词区域和术语表分别保存
- **字幕可调**：字体、字号、颜色、描边、背景不透明度，可自由拖动
- **托盘常驻**：点 X 收进托盘，翻译不中断
- 单文件 exe，约 25 MB

## 工作原理

```
PrintWindow(PW_RENDERFULLCONTENT)        ~14 ms
        ↓  裁出用户框选的台词区域
像素指纹比对（没变就跳过）
        ↓
Windows.Media.Ocr (ja)                   ~20 ms
        ↓  去掉 OCR 硬插的空格、合并断行
稳定判定（连续 2 帧一致才算一句）
        ↓
译文缓存命中 → 直接显示
        ↓  未命中
OpenAI 兼容流式接口                      首 token 300~500 ms
        ↓
透明置顶字幕层（点击穿透，按住 Alt 可拖动）
```

## 环境要求

| 项 | 要求 |
|---|---|
| 系统 | Windows 10 2004+ / Windows 11（x64） |
| 运行时 | [.NET 10 Desktop Runtime](https://dotnet.microsoft.com/download/dotnet/10.0) |
| OCR | 系统需装**日语 OCR 语言包** |
| 网络 | 仅调用模型接口时需要 |

### 安装日语 OCR

设置 → 时间和语言 → 语言和区域 → 添加语言 → **日本語** → 可选语言功能里勾选**光学字符识别**。

## 快速开始

```powershell
git clone https://github.com/ymkdr/GalLens.git
cd GalLens
dotnet build GalLens.slnx -c Release

# 发布单文件 exe（必须用脚本，见下方说明）
build.cmd
```

然后双击生成的 `GalLens.exe`。

> **为什么用 build.cmd**：Windows 默认禁止直接运行 .ps1；且不能把发布输出直接写到项目根目录（会生成损坏的 exe）。脚本会发到临时目录再复制出来。

## 使用

1. 游戏设置为**窗口化**或**无边框窗口**（独占全屏截不到图）
2. 选游戏窗口 → 框选台词区域
3. 填接口地址 / API Key / 模型 → 开始翻译

| 快捷键 | 作用 |
|---|---|
| `Alt + T` | 开始 / 停止 |
| `Alt + R` | 重新框选台词区域 |
| `Alt + M` | 锁定拖动模式 |
| `Ctrl + Alt + R` | 重译当前句（绕过缓存） |
| `Ctrl + Alt + V` | 用图像翻译当前画面 |
| `Alt + H` | 字幕历史 |
| 按住 `Alt` 悬停字幕 | 出现「历史 / 重译 / 图像」三个按钮 |
| 按住 `Alt` 拖动字幕 | 直接挪字幕位置 |

详细说明见 [使用说明.md](使用说明.md)，程序内也有「帮助」。

## 模型支持

任何兼容 **OpenAI Chat Completions** 规范（`/chat/completions` + `stream: true`）的服务都能接入：

- 云端：DeepSeek、通义千问、Kimi、智谱、OpenAI，以及其它兼容该规范的服务商
- 本地：Ollama、LM Studio、vLLM 等自建推理服务

接口地址、模型名以**服务商文档为准**，程序只是把它们原样放进请求。换服务商时地址和模型要一起换。

图像兜底额外要求模型支持图像输入；纯文本模型请把「OCR 不可靠时改用图像识别」取消勾选。

## 目录结构

```
GalLens/
├── src/GalLens/          # 应用本体（WPF，17 个文件约 2400 行）
│   ├── ScreenCapture.cs  # 窗口截图（PrintWindow + BitBlt 兜底）
│   ├── OcrService.cs     # Windows OCR 封装
│   ├── TextUtil.cs       # OCR 结果清洗与质量判定
│   ├── Translator.cs     # OpenAI 兼容流式客户端（文本 / 图像）
│   ├── Pipeline.cs       # 主循环：指纹 → 稳定判定 → 翻译 → 兜底
│   ├── OverlayWindow.cs  # 透明字幕层
│   ├── TrayIcon.cs       # 系统托盘
│   └── ...
├── tests/                # 四个自测工程
├── docs/                 # 截图
├── build.ps1 / build.cmd # 发布脚本
└── 使用说明.md
```

## 自测

```powershell
dotnet run --project tests/Probe     -c Release   # 截图 + OCR 精度与耗时
dotnet run --project tests/TransTest -c Release   # 本地假服务器，验证流式与图像请求
dotnet run --project tests/E2E       -c Release   # 全链路：假游戏窗口 → 字幕
```

## 隐私

- 程序的网络请求**只发往你自己填写的接口地址**，没有遥测、没有统计。
- 截图和识别出的文字仅在翻译请求中发送。
- API Key 用 Windows DPAPI 加密后存放在 `%APPDATA%\GalLens\settings.json`，不写进程序目录，更不会进仓库。
- 卸载：删除程序目录 + `%APPDATA%\GalLens`。

## 免责声明

本项目仅用于**个人学习、技术研究与无障碍辅助**，不提供任何游戏内容。

- 不包含、不内置、不分发任何游戏资源、文本、图像或字体。
- **不破解、不解包、不绕过任何 DRM 或技术保护措施**，仅读取用户屏幕上已显示的内容。
- 使用本工具需要你**自行合法拥有**所运行的游戏；请遵守游戏最终用户许可协议。
- 翻译内容由第三方大模型生成，其准确性、合法性由模型服务方与使用者自行负责；使用 API 产生的费用由使用者承担。
- 本工具与任何游戏发行商、模型服务商均无关联，相关商标归其各自所有者。
- 软件按 MIT 协议「按原样」提供，作者不对使用后果承担任何责任。

## 图标

图标由 **Ma Shan Zheng（马善政毛笔楷书）** 渲染「汉」字生成，脚本见 `src/GalLens/assets/make_icon.py`。

- 字体采用 **SIL Open Font License 1.1**，允许把字形用于 logo、图标等输出物
- **字体文件不随仓库分发**（仓库里只有渲染出的 PNG/ICO）。重新生成图标需自行下载字体，并设置环境变量 `GALLENS_ICON_FONT` 指向 ttf
- 字体主页：https://fonts.google.com/specimen/Ma+Shan+Zheng
- 不使用任何第三方美术素材或书法作品扫描件

## 许可证

[MIT](LICENSE) © 2026 ymkdr

---

## English

**GalLens** is a Windows screen translator for Japanese visual novels. It captures the game window, runs OCR locally with the built-in Windows engine, translates with any OpenAI-compatible LLM, and renders the result as a click-through subtitle overlay.

It never injects into the game, never reads or writes its memory, and never modifies game files — it only reads what is already on screen.

- Requirements: Windows 10 2004+, .NET 10 Desktop Runtime, Japanese OCR language pack
- Build: `dotnet build GalLens.slnx -c Release`, then `build.cmd`
- Supports any OpenAI-compatible `/chat/completions` endpoint with streaming
- Optional vision fallback for vertical text, stylized fonts, or text baked into images

Provided for personal use and accessibility research. No game assets included. No DRM circumvention. You must own a legal copy of any game you translate.

Licensed under MIT.
