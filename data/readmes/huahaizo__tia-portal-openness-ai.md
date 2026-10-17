# 🚀 TIA Openness Control

![TIA Portal](https://img.shields.io/badge/TIA%20Portal-V15--V21-0f766e)
![Openness](https://img.shields.io/badge/Siemens-Openness-2563eb)
![AI Ready](https://img.shields.io/badge/AI-Ready-7c3aed)
![Windows](https://img.shields.io/badge/Platform-Windows-475569)

通过 Siemens **TIA Portal Openness**，让 AI 帮你自动化操作博途项目。

你可以用中文描述需求，例如“打开项目并列出所有设备”“导出 PLC 块”“把这段 SCL 导入项目并编译”。AI 会先生成可审查的动作计划，再通过 C# 控制器调用 `Siemens.Engineering` 官方 API 执行。

```text
你的需求 -> AI 动作计划 -> JSON/YAML 指令 -> C# Openness 控制器 -> TIA Portal 项目
```

## 📌 目录

- [✅ 当前状态](#-当前状态)
- [✨ 可以做什么](#-可以做什么)
- [🧰 使用前准备](#-使用前准备)
- [📦 安装 skill](#-安装-skill)
- [🔐 首次使用配置](#-首次使用配置)
- [🧭 支持版本](#-支持版本)
- [🚀 快速开始](#-快速开始)
- [🧪 建议的使用方式](#-建议的使用方式)
- [🛠 常见报错](#-常见报错)
- [⚠️ 安全提醒](#️-安全提醒)
- [📖 常见术语](#-常见术语)

## ✅ 当前状态

当前版本已经过实际 Openness 调用验证，可以用于生成控制器并执行 TIA Portal 自动化任务。

脚手架已处理常见的 `Siemens.Engineering.dll` 加载问题：程序会先注册程序集解析器，再加载 `Siemens.Engineering.dll`，最后才进入真正的 Openness 逻辑。

## ✨ 可以做什么

| 你想做的事 | 对应自动化动作 |
| --- | --- |
| 打开博途项目并列出设备 | `OpenProject` + `ListDevices` |
| 导出 PLC 块 | `ExportBlocks` |
| 导入 AI 生成的 SCL 源文件 | `ImportSources` |
| 编译 PLC 并返回诊断信息 | `CompilePlc` |
| 归档项目 | `ArchiveProject` |
| 生成 Openness 控制器骨架 | `new-openness-controller.ps1` |

## 🧰 使用前准备

请确认本机满足这些条件：

- Windows 系统
- 已安装 TIA Portal V15 到 V21 中的任一版本
- 当前 Windows 用户已加入 `Siemens TIA Openness` 用户组
- 已启用 TIA Portal Openness
- 要操作的项目已经备份
- 本机可以访问对应版本的 `Siemens.Engineering.dll`

## 📦 安装 skill

把整个 `tia-openness-control` 文件夹复制到你的 AI 工具或 Agent 支持的 skills 目录中。这个文件夹必须包含 `SKILL.md`。

不同 AI 工具的 skills 目录位置不同，请以你正在使用的工具文档为准。只要最终能让 AI 读取到 `SKILL.md`、`references/` 和 `scripts/`，就可以使用。

最终结构应类似：

```text
tia-openness-control/
├─ SKILL.md
├─ README.md
├─ agents/openai.yaml
├─ references/openness-patterns.md
└─ scripts/new-openness-controller.ps1
```

## 🔐 首次使用配置

第一次使用 Openness 前，需要把当前 Windows 用户加入 `Siemens TIA Openness` 用户组。这个操作需要管理员权限。

用管理员身份打开 PowerShell，然后执行：

```powershell
net localgroup "Siemens TIA Openness" "$env:USERNAME" /add
```

如果要添加指定用户：

```powershell
net localgroup "Siemens TIA Openness" "用户名" /add
```

添加后请注销并重新登录 Windows，必要时重启电脑。否则 TIA Portal 可能仍然识别不到新的 Openness 权限。

也可以通过图形界面操作：

```text
计算机管理 -> 本地用户和组 -> 组 -> Siemens TIA Openness -> 添加用户
```

## 🧭 支持版本

支持这些 TIA Portal 版本：

```text
V15, V15_1 / V15.1, V16, V17, V18, V19, V20, V21
```

脚本会自动扫描本机安装的 Openness API，并默认选择最高可用版本：

```text
C:\Program Files\Siemens\Automation\Portal V*\PublicAPI\V*\Siemens.Engineering.dll
```

## 🚀 快速开始

如果当前目录就是 `tia-openness-control`，运行下面的命令，自动检测当前安装的 TIA Portal 版本，并生成 C# 控制器：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\new-openness-controller.ps1 -OutputPath . -ProjectName TiaOpennessController
```

如果你在它的上一级目录运行，使用：

```powershell
powershell -ExecutionPolicy Bypass -File .\tia-openness-control\scripts\new-openness-controller.ps1 -OutputPath . -ProjectName TiaOpennessController
```

如果要指定 TIA Portal 版本：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\new-openness-controller.ps1 -OutputPath . -ProjectName TiaOpennessController -TiaVersion V17
```

生成后构建控制器：

```powershell
dotnet build .\TiaOpennessController
```

## 🧪 建议的使用方式

先让 AI 做只读或 dry-run 操作，例如：

```text
请使用 tia-openness-control，自动检测本机 TIA Portal 版本，打开 D:\Projects\Line1.ap20，并列出所有设备。先不要写入项目。
```

确认结果正确后，再让 AI 生成写入动作，例如导入源文件、编译、保存或归档。

## 🛠 常见报错

如果运行控制器时看到类似错误：

```text
System.IO.FileNotFoundException: 未能加载文件或程序集“Siemens.Engineering, Version=16.0.0.0...”
在 TiaOpennessController.Program.Main(String[] args)
```

通常不是 DLL 不存在，而是程序在 `Main` 里太早引用了 `Siemens.Engineering` 类型，导致程序集解析器还没注册就开始加载 DLL。

处理方式：

- 优先使用本 skill 的 `new-openness-controller.ps1` 重新生成控制器骨架
- 不要让 AI 在 `Main` 里直接写 `TiaPortal`、`TiaPortalMode`、`Project`、`Device`
- `Main` 只负责注册 `AssemblyResolve` 和加载 `Siemens.Engineering.dll`
- 真正的 Openness 代码放到单独的 runner 方法或类里，并延迟调用

如果 AI 说“运行成功”，但你没有看到项目变化，请让它提供：

- 实际执行的命令
- stdout / stderr
- 退出码
- 项目完整路径
- 保存后重新打开项目并读取到的设备或块列表

不要只相信“退出码为 0”或“文件时间变了”。添加 PLC、块、变量表之后，必须通过 Openness 再读回项目内容确认。

## ⚠️ 安全提醒

以下操作必须人工确认后再执行：

- 下载到 PLC 或 HMI
- 进入在线模式
- 删除设备、块、变量表或库
- 修改安全相关对象或受保护对象
- 修改生产项目的硬件地址、网络参数或通信设置
- 未备份项目时执行写入

推荐优先操作离线项目。AI 生成的 PLC 内容最好先保存为源文件，再由 Openness 导入并编译。

## 📄 免责声明

本项目是独立的 AI skill 和 Openness 自动化脚手架，不包含 Siemens TIA Portal、`Siemens.Engineering.dll`、Siemens 专有库、官方文档或任何 Siemens 授权软件。

使用者需要自行安装并授权 Siemens TIA Portal，并遵守 Siemens 的许可条款、安全要求和官方文档。本项目与 Siemens 无隶属关系，未获得 Siemens 认可、赞助、背书或支持。

完整说明见 [DISCLAIMER.md](./DISCLAIMER.md)。

## 📖 常见术语

| 中文 | 英文 / API |
| --- | --- |
| 博途 | TIA Portal |
| 官方自动化接口 | Openness |
| 公共 API 路径 | `PublicAPI` |
| 核心 DLL | `Siemens.Engineering.dll` |
| 带界面启动 | `TiaPortalMode.WithUserInterface` |
| 无界面启动 | `TiaPortalMode.WithoutUserInterface` |
| 只读 / 试运行 | dry-run |
