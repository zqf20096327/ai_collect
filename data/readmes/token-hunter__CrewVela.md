![CrewVela 多 Agent 协作海报](docs/media/crewvela-collaboration-banner.png)

<div align="center">

# CrewVela

### 多个 Agent，一个工作台。

让 Claude Code 写代码，让 Codex 做审查，让其他 Agent 接着干。

[![版本 0.1.0 Beta](https://img.shields.io/badge/version-0.1.0--beta-8B6CEF?style=flat-square)](CHANGELOG.md)
[![Tauri 2](https://img.shields.io/badge/Tauri-2-24C8D8?style=flat-square)](src-tauri/Cargo.toml)
[![React 与 TypeScript](https://img.shields.io/badge/React-TypeScript-3178C6?style=flat-square)](package.json)
[![MIT 许可](https://img.shields.io/badge/license-MIT-64748B?style=flat-square)](LICENSE)

[![下载 Windows Beta](https://img.shields.io/badge/%E4%B8%8B%E8%BD%BD-Windows_Beta-2563EB?style=for-the-badge&logo=github&logoColor=white)](docs/downloads.md)

[宣传片](#一分钟看-crewvela) · [开始使用](#开始使用) · [协作玩法](docs/workflows.md) · [使用手册](docs/user-guide.md) · [English](README.en.md)

**如果你也想让多个编程 Agent 配合干活，点个 Star，方便回来看看它们又学会了什么。**

</div>

CrewVela 是一个基于 **Tauri 2 + React + Rust** 的桌面多 Agent 工作台，把独立会话、会话通信、项目协作和工作交接放进同一个窗口。沿用各 Agent 的本机安装、账号与权限机制，让你围绕任务组织工具。

> **当前版本 v0.1.0 Beta。** 提供 Windows x64 安装向导和 macOS Apple Silicon DMG。下载链接、校验文件和安装步骤见[下载与安装](docs/downloads.md)。

## 一分钟看 CrewVela

点击下方播放器，看看多个 Agent 如何在一个工作台里协作。

https://github.com/user-attachments/assets/a3eb08ee-a30e-4619-92aa-b2854f8d690f

时长 1 分钟。

## 让你的 Agent 成为一支队伍

你可能已经在用好几个编程 Agent：一个擅长搭功能，一个适合挑问题，另一个更顺手处理某类任务。CrewVela 把它们放进同一个工作空间，让分工、沟通和交接都有对应的入口。

| 你想怎么干 | 在 CrewVela 里怎么组织 |
| --- | --- |
| 一个实现，一个 Review | 并排打开不同 Agent，让实现者说明改动，让审查者反馈问题 |
| 当前 Agent 卡住了，换个思路 | 预览交接资料，再交给另一个 Agent；保留来源会话的可见历史 |
| 同时推进几个任务 | 网格分屏查看会话；按需使用 Git worktree 分隔工作目录 |
| 把一个需求拆成多个角色 | 通过项目成员、任务依赖、协作消息和诊断查看进展 |
| 让 Agent 按验收条件交付 | 在项目中选择全自动托管，由成员完成实现、按计划审查与联调，再按项目配置验收和提供 Demo |
| 下次打开还能接着做 | 使用会话恢复，以及可选的本地共享记忆接入 |

## 多个 Agent，如何一起完成工作

下面是一种分工方式，具体角色由你决定：

![从需求到协作的工作流程](docs/media/collaboration-workflow.zh.svg)

**实现 → 审查 → 回传修复 → 交接继续。** 在各自会话中保留工作上下文，通过明确的目标传递消息；需要换人时，先看交接资料，再决定是否交接。

这是工作方式示意，不是自动执行记录。通信需要受支持且已加载工具的会话；**已排队不等于已送达、已读或回复**。完整示例见[三种协作玩法](docs/workflows.md)。

想了解消息如何流转、不同 Agent 如何接入？[查看技术架构](docs/architecture.md)。

## 工作台里有什么

| 能力 | 用来做什么 |
| --- | --- |
| **CLI 与原生聊天** | 在同一个桌面工作区使用不同类型的 Agent 会话 |
| **会话通信** | 选择发送方与接收方，使用会话列表、消息来源和回复指引对齐对象 |
| **项目协作与托管** | 项目聊天可切换 Bot 模式。托管支持单个成员交付，也可为多成员分配实现、审查与联调职责 |
| **工作交接** | 准备并预览交接资料；来源会话停止运行，历史仍可见 |
| **会话与工作区管理** | 网格分屏、工作区搜索、会话筛选和 Git worktree 管理 |
| **共享记忆（可选）** | 配置内置本地记忆，也可使用旧版共享记忆接入，让后续会话检索项目上下文 |
| **工作工具** | 在工作面板访问文件、终端、浏览器、源码控制和多智能体协作 |

## 接入你已经在用的 Agent

当前提供 8 个 Agent 系列的接入。实际可用性取决于 CLI、适配器、账号与模型配置。

| Agent | CLI 终端入口 | 原生聊天入口 |
| --- | --- | --- |
| Claude Code | Claude Code | Claude Code Chat |
| Codex | Codex CLI | Codex Chat |
| Antigravity | Antigravity CLI | — |
| ZCode | ZCode CLI | ZCode Desktop |
| Kimi | Kimi Code CLI | Kimi Code Chat |
| DeepSeek Harness | — | DeepSeek Harness |
| OpenCode | OpenCode | OpenCode Chat |
| Pi | Pi Agent | Pi Chat |

CrewVela 沿用各 Agent 自己的账号、订阅和模型配置。「设置 → 协作中心 → 管理 Runtime」可管理 Antigravity CLI 等受支持的官方安装，也可检测或选择本机已有的 ZCode CLI。详见 [CLI 安装与版本管理](docs/runtime-installation.md)和[使用手册](docs/user-guide.md)。

## 开始使用

### 选择你的入口

| 想做什么 | 从这里开始 |
| --- | --- |
| 下载桌面应用 | [安装说明与附件状态](docs/downloads.md) |
| 体验两个 Agent 互相联系 | [协作玩法](docs/workflows.md) |
| 查配置、会话与工具的用法 | [完整使用手册](docs/user-guide.md) |
| 在 Mac 上构建与验收 | [Mac 指南](MACOS-CODEX-HANDOFF.md) |
| 参与开发 | [贡献指南](CONTRIBUTING.md) |

### 从源码运行

准备 **Node.js 24、Rust stable** 和平台构建工具。Windows 需要 MSVC C++ 与 WebView2；Mac 需要 Xcode Command Line Tools。先在系统终端安装并登录要使用的 Agent CLI。

在项目根目录运行：

```sh
npm ci
npm run tauri -- dev
```

<details>
<summary>Windows 与 macOS 打包命令</summary>

**Windows：**

```sh
npm run tauri -- build --no-bundle
```

输出：`src-tauri/target/release/CrewVela.exe`，为应用本体。NSIS 安装向导另见[安装说明](docs/downloads.md)。

**macOS：在 Apple Silicon Mac 上执行。**

```sh
rustup target add aarch64-apple-darwin
APPLE_SIGNING_IDENTITY=- npm run build:macos
```

输出目录：

- `.app`：`src-tauri/target/aarch64-apple-darwin/release/bundle/macos/`
- `.dmg`：`src-tauri/target/aarch64-apple-darwin/release/bundle/dmg/`

该命令使用 ad-hoc 测试签名，未做 Developer ID 签名或公证。Intel 命令及原生验收步骤见 [Mac 指南](MACOS-CODEX-HANDOFF.md)。需要空白首次启动效果时使用[独立测试目录](docs/macos-isolated-test.md)；该模式停用真实 Agent、账号与共享记忆操作。

</details>

### 三步让 Agent 互相联系

1. 新建两个受支持的 Agent 会话，为它们选择工作目录和易辨认的名称。
2. 点击 **会话通信**，选择发送方和目标，复制对应指令。
3. 在发送方粘贴指令，到目标会话核对消息和回复；需要时打开通信诊断。

项目成员也可以使用这一入口。复制教程只写入剪贴板，不会直接发消息。升级前从旧窗口或托盘完整退出旧版，避免多个主程序使用同一数据目录。

## 当前平台与发布状态

| 平台 | 当前验证范围 |
| --- | --- |
| Windows x64 | 提供未签名的 NSIS 安装包。验证范围见对应 Release |
| macOS Apple Silicon | 提供 ARM64 DMG，使用 ad-hoc 签名，未经 Apple 公证 |
| macOS Intel / Linux | 未完成原生验收，当前不提供已验证安装包 |

各平台安装包对应的源码提交与 SHA-256 见[下载页](docs/downloads.md)和对应 Release。平台验收、隐私脱敏、依赖风险与素材来源见[发布检查清单](docs/release-checklist.md)、[安全说明](SECURITY.md)及[素材记录](docs/asset-provenance.md)。

## 常见问题

**CLI 终端和原生聊天有什么区别？** 终端入口保留对应 CLI 的交互方式；原生聊天将受支持协议的会话放进统一聊天界面。具体能力随 Agent 和适配器而异。

**交接之后，原来的记录还在吗？** 当前交接流程会停止来源会话，并保留其可见历史；接手 Agent 继续处理交接资料。详细行为见使用手册。

**模型请求在哪里运行？** 请求发送到你为对应 Agent 配置的模型服务。CrewVela 是本机桌面工作台，不代表模型离线推理。

**密钥和记忆保存在哪里？** CrewVela 管理的 Provider key 使用系统凭据库，外部 Agent 自行管理登录状态；共享记忆默认保存在本机。第三方工具的数据访问行为取决于其配置。不要在 Issue、截图或日志中上传凭据与私人数据。

## 接下来，一起把工作流打磨好

| 你的参与 | 对项目的帮助 |
| --- | --- |
| **点个 Star** | 收藏项目，方便回来跟进更新，也帮助更多人发现它 |
| **描述一个协作场景** | 告诉我们你希望哪几个 Agent 怎样配合 |
| **提交可复现的问题** | 帮助定位具体 CLI、平台或模型组合的兼容问题 |
| **贡献代码或文档** | 改善接入、教程、无障碍和平台体验 |

从[贡献指南](CONTRIBUTING.md)开始。公开反馈前请先脱敏；安全问题按 [SECURITY.md](SECURITY.md) 处理。

### 加入 Agent 交流群

用微信扫码加入群聊，交流 Agent相关技术。本次二维码在 2026 年 12 月 4 日前有效。

<img src="docs/media/wechat-agent-group.jpg" alt="微信 Agent 交流群入群二维码" width="360" />

[查看二维码原图](docs/media/wechat-agent-group.jpg)

### 联系作者

想聊 CrewVela 的使用体验、功能建议或合作，欢迎加我微信 `weilegexinaaa`。添加时请备注「CrewVela」。

## 给作者加个鸡腿 🍗

<div align="center">

<img src="docs/media/author-drumstick.gif" alt="戴眼镜的搞怪鸡腿，循环动画" width="220" />

Agent 在干活，作者在等开饭。

一个 Star、一条反馈、一份贡献，都是给作者加餐。

</div>

## Star 趋势

<a href="https://www.star-history.com/?repos=token-hunter%2FCrewVela&amp;type=date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=token-hunter/CrewVela&amp;type=Date&amp;theme=dark" />
    <img alt="CrewVela 的 GitHub Star 趋势" src="https://api.star-history.com/svg?repos=token-hunter/CrewVela&amp;type=Date" />
  </picture>
</a>

## 开源许可

CrewVela 项目代码采用 [MIT 许可证](LICENSE)。第三方依赖与素材的相关说明，请参阅[第三方声明](THIRD_PARTY_NOTICES.md)。
