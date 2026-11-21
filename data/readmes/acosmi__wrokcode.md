> **相关仓库**：[wrokBot](https://github.com/acosmi/OpenMyBot) · [RSIAgent](https://github.com/acosmi/RSIAgent)
>
> **新仓库说明**：本仓库是 **wrok Code** 的新名称发版仓。旧名称仓库 [`acosmi/crabcode`](https://github.com/acosmi/crabcode) 保留用于兼容；当前已复制 `v1.1.32` 全量发布资产（31 件，字节与旧仓一致）。在发版链路正式接入本仓前，两仓后续版本可能不同步。

<div align="center">

# wrok Code · 一个人的 AI 工作台

**从一份需求，到页面、文档和海报 · Code × Work 双模式**<br>
**From a brief to pages, documents and posters — a one-person AI workspace**

[![Latest Release](https://img.shields.io/github/v/release/acosmi/wrokCode?display_name=tag&label=latest)](https://github.com/acosmi/wrokCode/releases/latest)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-blue)](#最新版本)
[![Status](https://img.shields.io/badge/status-active-success)](https://github.com/acosmi/wrokCode/releases)
[![Issues](https://img.shields.io/github/issues/acosmi/wrokCode?label=issues)](https://github.com/acosmi/wrokCode/issues)

[简体中文](#简体中文) · [English](#english)

</div>

---

## 最新版本

**v1.1.32** · 2026-11-13 · [Release Notes](https://github.com/acosmi/wrokCode/releases/tag/v1.1.32)

| 平台 | 形态 | 安装包 |
|---|---|---|
| macOS Apple Silicon | TUI | `crabcode-1.1.32-darwin-arm64.tar.gz` |
| macOS Intel | TUI | `crabcode-1.1.32-darwin-x64.tar.gz` |
| Linux arm64 | TUI | `crabcode-1.1.32-linux-arm64.tar.gz` |
| Linux x64 | TUI | `crabcode-1.1.32-linux-x64.tar.gz` |
| Windows x64 | TUI | `crabcode-1.1.32-win-x64.zip` |
| Windows x64 | GUI | `crabcode-1.1.32-win-x64-setup.exe` |
| macOS Apple Silicon | GUI | `crabcode-1.1.32-darwin-arm64-gui.dmg` |
| macOS Intel | GUI | `crabcode-1.1.32-darwin-x64-gui.dmg` |

所有包都在 [Releases](https://github.com/acosmi/wrokCode/releases/latest) 提供，并附 SHA-256 校验文件；macOS / Linux GUI 也可从官网下载页获取。

## 关于 wrok Code

做一项工作，经常要整理资料、写代码、做设计，还要记住前面讨论过什么。**wrok Code** 把这些环节接进同一个助手，让一个助手能跟着项目继续往下做。

- **工作**：整理资料、提炼重点，让知识带着出处，让结果可以继续使用。
- **编程**：从需求开始开发页面、编写代码；复杂任务交给多个子智能体分工推进。
- **设计**：内置 104 个设计模板，支持导出图片、PDF 和视频，把想法做成可以交付的作品。
- **记忆**：记住项目背景和你的偏好；记忆可以检查、修改，下次不用从头解释。
- **操作**：经你授权，操作浏览器与电脑；关键动作先确认，你可以随时接管或停止。

模型可以按任务选择，技能、插件和 MCP 工具按需接入。

> wrok Code 已发布；**wrokBot** 与 **RSIAgent** 即将发布。接下来，我们希望把任务协作与经过验证的经验积累连接起来，走向「**可递归自我进化的 AI 同事**」。

## 新用户福利

> 注册即享 **免费一个月 Basic 基础版会员**，赠送 **6000 万 Credits**，畅用 DeepSeek、Qwen3.7、MiniMax-M3、GLM-5.2 等国内主流模型。

- 注册：<https://acosmi.com/zh>
- 注册后在 wrok Code 中执行 `/login` 即可激活会员与额度。
- 老用户邀请新用户可额外获得奖励。

## 两种使用形态

| 形态 | 说明 | 获取 |
|---|---|---|
| 桌面 GUI 版 | 图形界面桌面应用，开箱即用，适合偏好可视化操作的用户。 | 官网下载页 <https://acosmi.com/zh/downloads>；Windows 也可从本仓 [Releases](https://github.com/acosmi/wrokCode/releases/latest) 下载 |
| 命令行 TUI 版 | 终端原生全屏体验，贴近工程目录，适合 CLI、远程和自动化场景。 | 本仓 [Releases](https://github.com/acosmi/wrokCode/releases/latest)，见下方安装说明 |

> 本仓 Releases 提供全平台 TUI 包、Windows GUI 安装器和 macOS GUI 安装包；macOS / Linux GUI 也可从官网下载页获取。

---

## 简体中文

### 简介

**wrok Code（原 CrabCode）** 是一款运行在终端和桌面上的 AI 工作台，把模型调用、代码检索、文件编辑、Shell 执行、MCP 工具、设计导出和 GitHub 工作流收进同一套体验。你无需离开当前工程目录，就能完成代码理解、排错、重构、测试生成、资料整理与日常自动化。

这个公开仓库用于发布稳定安装包和面向用户的说明。当前最新版本为 **v1.1.32**，发布于 **2026-11-13**。如需图形界面桌面版（GUI），请前往官方下载页：<https://acosmi.com/zh/downloads>。

### 核心能力

- **终端原生 TUI**：全屏交互、流式输出、历史会话、主题和中英文界面。
- **模型动态路由**：可用模型、能力和价格由 Acosmi SDK 动态下发；在客户端内使用 `/model` 查看和切换。
- **工程级工具**：读取、写入、精确编辑、全文检索、Glob 匹配、沙盒化 Shell、Notebook 读写。
- **设计交付**：内置 104 个设计模板，支持导出图片、PDF 和视频。
- **记忆与工作流**：跨会话记忆、Hooks、Skills、Plan Mode、权限管理、Git / GitHub 协作。
- **MCP 与自动化**：支持配置和调用 Model Context Protocol 服务器；`wrok cron` 使用独立 Rust 调度守护进程，支持 macOS、Linux 和 Windows。
- **电脑操作**：经授权操作浏览器与电脑，关键动作先确认，可随时接管或停止。

### 安装

**macOS / Linux** — 一条命令完成安装（自动识别平台、SHA256 fail-closed 校验、自动配置 PATH）：

```bash
curl -fsSL https://updates.acosmi.com/crabcode/install.sh | sh
```

**Windows** — 在 **PowerShell** 中执行（不要粘贴进 CMD；正确提示符以 `PS ` 开头）：

```powershell
irm https://updates.acosmi.com/crabcode/install.ps1 | iex
```

说明：

- 安装源为国内镜像（`updates.acosmi.com`），镜像不可达时自动回退 GitHub Releases；校验文件与产物**同源**，SHA256 校验 fail-closed（校验不过绝不落地）。
- 海外用户也可以直接使用 GitHub 源，效果等价：

```bash
curl -fsSL https://github.com/acosmi/wrokCode/releases/latest/download/install.sh | sh
```

- 当前安装脚本与更新器仍指向旧仓 `acosmi/crabcode` 与国内镜像；本仓已复制同版 v1.1.32 资产，安装结果一致。发版链路正式接入本仓前，两仓后续版本可能不同步。
- Windows 运行交互式 TUI 请使用 **Windows Terminal** 或新版 PowerShell 窗口，并从普通用户目录启动（例如 `C:\Users\you>`）。老式 CMD（尤其管理员窗口的 `C:\Windows\System32>`）可能出现界面不刷新或黑屏；若必须使用旧 CMD，先执行 `chcp 65001` 并关闭 legacy console 模式。
- 手动安装（高级）：从 [Releases](https://github.com/acosmi/wrokCode/releases/latest) 下载对应平台压缩包，解压后把目录加入 PATH 即可。注意安装目录需**整体保留**：不要只拷单个文件、也不要跨目录 symlink（程序依赖同目录下的运行时文件）。

#### 更新

已安装用户一条命令更新到最新版（只替换程序文件，不动配置、登录状态、历史与记忆数据）：

```bash
wrok update
```

`crabcode update` 与 TUI 内的 `/update` 仍然可用。也可以重跑上面的安装命令（等价覆盖安装）。

#### Windows 图形界面（GUI）版

不想用命令行的 Windows 用户，可以直接下载图形界面安装包，无需配置 PATH：

1. 打开 [最新 Release](https://github.com/acosmi/wrokCode/releases/latest)，在 Assets 中下载 `crabcode-1.1.32-win-x64-setup.exe`。
2. 双击运行安装向导，按提示完成；安装后从开始菜单启动 wrok Code 桌面版。

直接下载链接：<https://github.com/acosmi/wrokCode/releases/download/v1.1.32/crabcode-1.1.32-win-x64-setup.exe>

> macOS / Linux 的图形界面版请前往官网下载页：<https://acosmi.com/zh/downloads>，或从本仓 Release 下载对应 `.dmg`。

### 校验文件完整性

在已下载发布包的目录中执行：

```bash
curl -fsSL -O https://github.com/acosmi/wrokCode/releases/download/v1.1.32/checksums-sha256.txt
shasum -a 256 -c checksums-sha256.txt
```

Linux 也可以使用：

```bash
sha256sum -c checksums-sha256.txt
```

Windows 可下载 Windows 专用校验文件后对比：

```powershell
Invoke-WebRequest `
  -Uri "https://github.com/acosmi/wrokCode/releases/download/v1.1.32/checksums-sha256.txt" `
  -OutFile checksums-sha256.txt

$Expected = (Select-String -Path checksums-sha256.txt -Pattern "crabcode-1.1.32-win-x64.zip").Line.Split()[0].ToLower()
$Actual = (Get-FileHash crabcode-1.1.32-win-x64.zip -Algorithm SHA256).Hash.ToLower()
if ($Expected -ne $Actual) {
  throw "SHA256 mismatch: expected $Expected, got $Actual"
}
"SHA256 OK: $Actual"
```

### 快速上手

```bash
wrok                   # 进入交互式 TUI（crabcode 命令保留兼容）
wrok -p "解释当前目录的代码结构"
wrok --help
wrok --version
```

第一次使用请在 TUI 中执行 `/login` 完成账号认证。

常用命令：

| 命令 | 用途 |
|---|---|
| `/login` | 登录或切换账号 |
| `/model` | 查看和切换可用模型 |
| `/clear` | 清空当前会话上下文 |
| `/history` | 查看历史会话 |
| `/permissions` | 查看或修改工具权限 |
| `/help` | 打开帮助 |

常用快捷键：

| 操作 | 按键 |
|---|---|
| 切换思考档位 | `Tab` |
| 中断当前任务 | `Esc` |
| 翻阅历史 | `↑` / `↓` |
| 滚动屏幕 | `PgUp` / `PgDn` 或鼠标滚轮 |
| 退出 | 连续按两次 `Ctrl+C` |

### 数据与隐私

- 用户配置、认证状态、历史和本地记忆默认保存在 `~/.crabcode/`（技术目录名保持不变）。
- 工具执行默认受权限控制；文件和 Shell 操作需要按目录授权。
- 模型请求经由 Acosmi 网关转发到上游模型服务；具体可用模型和额度以账号状态为准。

### 故障排查：老 CPU 报「非法指令 / Illegal instruction」

wrok Code 内置的 Bun 运行时默认要求 **AVX2** 指令集（Intel 第 4 代 Haswell，2013 年及以后）。更老的 x64 CPU（如第 1/2/3 代 i5）缺少 AVX2，启动时会崩溃并报 `Illegal instruction`、`非法指令` 或 `CPU lacks AVX support`。

解决办法：改用 Bun 官方的 **baseline 构建**（只需 SSE4.2，支持更老的 x64 CPU；性能略低但可正常运行）。

1. 下载对应平台的 baseline 包（版本号 `1.3.11` 为当前内置 Bun 版本，如不一致请换成对应版本）：

   - Linux：`bun-linux-x64-baseline.zip`
   - macOS：`bun-darwin-x64-baseline.zip`
   - Windows：`bun-windows-x64-baseline.zip`

   下载地址：<https://github.com/oven-sh/bun/releases/tag/bun-v1.3.11>

2. 解压得到 `bun`（Windows 为 `bun.exe`），放到一个固定路径。

3. 设置环境变量 `CRABCODE_BUN_BIN` 指向它，然后**重启 wrok Code**（GUI 需整个退出重开）：

   macOS / Linux（写入 `~/.zshrc` 或 `~/.bashrc`，然后 `source` 或重开终端）：

   ```bash
   export CRABCODE_BUN_BIN="$HOME/path/to/bun"
   ```

   Windows（PowerShell，设用户级变量后重开终端）：

   ```powershell
   [Environment]::SetEnvironmentVariable("CRABCODE_BUN_BIN", "C:\path\to\bun.exe", "User")
   ```

> 说明：baseline 构建仍需 **SSE4.2**（约 2008 年后的 CPU）。更早的处理器 Bun 不支持，无法运行。

### 反馈与支持

- Bug / 建议：<https://github.com/acosmi/wrokCode/issues>
- 最新发布：<https://github.com/acosmi/wrokCode/releases/latest>
- 官方网站：<https://acosmi.com>
- 账号和词元问题：登录账户后台，或在 wrok Code 中执行 `/help`。

---

## English

### Overview

**wrok Code** (formerly CrabCode) is an AI workspace for the terminal and desktop. It brings model access, code search, file editing, shell execution, MCP tools, design export, and GitHub workflows into one experience — from a brief to pages, documents, and posters.

This public repository hosts stable release packages and user-facing documentation. The latest release is **v1.1.32**, published on **2026-11-13**. For the graphical desktop app, use the official downloads page: <https://acosmi.com/zh/downloads>.

### Current Release

| Platform | Edition | Asset |
|---|---|---|
| macOS Apple Silicon | TUI | `crabcode-1.1.32-darwin-arm64.tar.gz` |
| macOS Intel | TUI | `crabcode-1.1.32-darwin-x64.tar.gz` |
| Linux arm64 | TUI | `crabcode-1.1.32-linux-arm64.tar.gz` |
| Linux x64 | TUI | `crabcode-1.1.32-linux-x64.tar.gz` |
| Windows x64 | TUI | `crabcode-1.1.32-win-x64.zip` |
| Windows x64 | GUI | `crabcode-1.1.32-win-x64-setup.exe` |
| macOS Apple Silicon | GUI | `crabcode-1.1.32-darwin-arm64-gui.dmg` |
| macOS Intel | GUI | `crabcode-1.1.32-darwin-x64-gui.dmg` |

All packages are available on the [latest release](https://github.com/acosmi/wrokCode/releases/latest) page with SHA-256 checksum files.

### Core Features

- **Work**: organize materials, extract highlights, keep sources, and reuse results.
- **Code**: build pages and write code from a brief; complex tasks are split across subagents.
- **Design**: 104 built-in templates; export images, PDF, and video.
- **Memory**: remember project context and preferences; inspect and edit memory at any time.
- **Control**: operate the browser and computer with your authorization; confirm key actions and take over or stop at any time.
- **Models, skills, plugins, and MCP**: choose models per task and attach tools as needed.

### Installation

**macOS / Linux** — one command (auto-detects platform, fail-closed SHA256 verification, sets up PATH automatically):

```bash
curl -fsSL https://updates.acosmi.com/crabcode/install.sh | sh
```

**Windows** — run in **PowerShell** (not CMD; the prompt should start with `PS `):

```powershell
irm https://updates.acosmi.com/crabcode/install.ps1 | iex
```

Notes:

- The default source is our distribution mirror (`updates.acosmi.com`) with automatic fallback to GitHub Releases. Checksums are fetched from the **same source** as the artifact and verification is fail-closed.
- You can also install straight from GitHub — fully equivalent:

```bash
curl -fsSL https://github.com/acosmi/wrokCode/releases/latest/download/install.sh | sh
```

- The install scripts and updater currently still point at the legacy `acosmi/crabcode` repository and the China mirror. This repository carries the same v1.1.32 bytes, so the installed result is identical. Until the release pipeline is switched over, subsequent versions may differ between the two repositories.
- On Windows, run the interactive TUI from **Windows Terminal** or a modern PowerShell window started in a regular user directory (e.g. `C:\Users\you>`). Legacy CMD windows (especially elevated `C:\Windows\System32>`) may show a frozen or black screen; if you must use legacy CMD, run `chcp 65001` first and disable legacy console mode.
- Manual install (advanced): download the platform archive from [Releases](https://github.com/acosmi/wrokCode/releases/latest), extract it, and add the directory to PATH. Keep the directory **intact** — do not copy out a single file or symlink across directories (the app relies on runtime files in the same directory).

#### Update

Already installed? One command updates to the latest version (replaces program files only — your config, login state, history and memory data are untouched):

```bash
wrok update
```

`crabcode update` and `/update` inside the TUI remain available. You can also re-run the install one-liner above.

#### Windows GUI Edition

Windows users who prefer a graphical app can download the installer directly — no command line or PATH setup needed:

1. Open the [latest release](https://github.com/acosmi/wrokCode/releases/latest) and download `crabcode-1.1.32-win-x64-setup.exe` from Assets.
2. Double-click the installer and follow the wizard; launch wrok Code from the Start menu afterwards.

Direct download: <https://github.com/acosmi/wrokCode/releases/download/v1.1.32/crabcode-1.1.32-win-x64-setup.exe>

> For the macOS / Linux GUI, use the official downloads page: <https://acosmi.com/zh/downloads>, or download the `.dmg` from this repository's release.

### Verify File Integrity

Run this in the directory where you downloaded the release packages:

```bash
curl -fsSL -O https://github.com/acosmi/wrokCode/releases/download/v1.1.32/checksums-sha256.txt
shasum -a 256 -c checksums-sha256.txt
```

On Linux you can also use:

```bash
sha256sum -c checksums-sha256.txt
```

For Windows:

```powershell
Invoke-WebRequest `
  -Uri "https://github.com/acosmi/wrokCode/releases/download/v1.1.32/checksums-sha256.txt" `
  -OutFile checksums-sha256.txt

$Expected = (Select-String -Path checksums-sha256.txt -Pattern "crabcode-1.1.32-win-x64.zip").Line.Split()[0].ToLower()
$Actual = (Get-FileHash crabcode-1.1.32-win-x64.zip -Algorithm SHA256).Hash.ToLower()
if ($Expected -ne $Actual) {
  throw "SHA256 mismatch: expected $Expected, got $Actual"
}
"SHA256 OK: $Actual"
```

### Quick Start

```bash
wrok                   # Interactive TUI (the crabcode command remains available)
wrok -p "Explain this repository"
wrok --help
wrok --version
```

On first use, run `/login` inside the TUI to authenticate your account.

Common slash commands:

| Command | Purpose |
|---|---|
| `/login` | Sign in or switch account |
| `/model` | Inspect and switch available models |
| `/clear` | Clear current session context |
| `/history` | View past sessions |
| `/permissions` | View or change tool permissions |
| `/help` | Open help |

Common shortcuts:

| Action | Key |
|---|---|
| Cycle thinking level | `Tab` |
| Interrupt current task | `Esc` |
| History up/down | `↑` / `↓` |
| Scroll screen | `PgUp` / `PgDn` or mouse wheel |
| Quit | `Ctrl+C` twice |

### Data & Privacy

- User configuration, auth state, history, and local memory are stored under `~/.crabcode/` by default (the technical directory name is unchanged).
- Tool execution is permission-gated by default; file and Shell access are authorized per directory.
- Model requests are routed through the Acosmi gateway to upstream model services; available models and quota depend on account status.

### Troubleshooting: "Illegal instruction" on older CPUs

wrok Code's bundled Bun runtime requires **AVX2** by default (Intel Haswell / 4th-gen, 2013 and later). Older x64 CPUs without AVX2 (such as 1st/2nd/3rd-gen i5) crash on startup with `Illegal instruction` or `CPU lacks AVX support`.

Fix: switch to Bun's official **baseline build** (needs only SSE4.2; slightly slower but runs on older x64 CPUs).

1. Download the baseline package for your platform (version `1.3.11` is the currently bundled Bun; change it if yours differs):

   - Linux: `bun-linux-x64-baseline.zip`
   - macOS: `bun-darwin-x64-baseline.zip`
   - Windows: `bun-windows-x64-baseline.zip`

   From: <https://github.com/oven-sh/bun/releases/tag/bun-v1.3.11>

2. Extract `bun` (`bun.exe` on Windows) to a fixed path.

3. Set the `CRABCODE_BUN_BIN` environment variable to point at it, then **restart wrok Code** (fully quit and reopen the GUI):

   macOS / Linux (add to `~/.zshrc` or `~/.bashrc`, then `source` it or reopen the terminal):

   ```bash
   export CRABCODE_BUN_BIN="$HOME/path/to/bun"
   ```

   Windows (PowerShell; set a user-level variable, then reopen the terminal):

   ```powershell
   [Environment]::SetEnvironmentVariable("CRABCODE_BUN_BIN", "C:\path\to\bun.exe", "User")
   ```

> Note: the baseline build still requires **SSE4.2** (CPUs from ~2008 onward). Bun does not support older processors.

### Feedback & Support

- Bugs / suggestions: <https://github.com/acosmi/wrokCode/issues>
- Latest release: <https://github.com/acosmi/wrokCode/releases/latest>
- Official site: <https://acosmi.com>
- Account and token issues: use your account dashboard, or run `/help` inside wrok Code.

---

<div align="center">

**wrok Code · Crafted by Acosmi · 2026**

</div>
