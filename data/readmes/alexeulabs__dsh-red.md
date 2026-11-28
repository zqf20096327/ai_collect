# DSH Special

English | [中文](README.zh.md)

[![Release](https://img.shields.io/github/v/release/alexeulabs/dsh-red?label=release&color=D92D20)](https://github.com/alexeulabs/dsh-red/releases) [![License](https://img.shields.io/github/license/alexeulabs/dsh-red?color=D92D20)](LICENSE) [![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-555)](#run-from-source) [![Local](https://img.shields.io/badge/data-100%25%20local-D92D20)](#data) [![Tools](https://img.shields.io/badge/tools-terminal%20%C2%B7%20ssh%20%C2%B7%20ghidra%20%C2%B7%20ida-555)](#builtin-plugins)

面向渗透测试的 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) 发行版，命令为 `dshs`。

在一个界面里完成侦察、打点、后渗透与报告：交互式终端、SSH 运维、逆向工程引擎、演练台事实库、插件市场全部预置开箱可用。与官方 `dsh` **完全隔离**，可并排安装互不影响。

<a id="run"></a>

## 为什么是它

官方 `dsh` 是通用 agent harness，执行受沙箱约束、工具偏保守。本版本按渗透场景重新组装：

| 能力 | 官方 dsh | 本版本 |
|---|---|---|
| 命令 / 主目录 / 端口 | `dsh` / `~/.dsh` / 3080 | `dshs` / `~/.dshs` / 3180 |
| 提示词清洗 | 无 | 内置 `dsh-purge-safe`，可按模型切换提示词 |
| 演练台事实库 | 无 | 内置，SQLite 记录资产、凭据、战果 |
| 交互式终端 | 需自行配置 | 右键侧栏终端标签，PowerShell/bash PTY |
| SSH 运维 | 无 | 内置主机管理、终端、SFTP、端口转发 |
| 逆向工程 | 无 | 内置 REA MCP：Ghidra、IDA、JADX、apktool、WABT、tshark |
| 插件市场 | 官方目录 | `dshmarket` 可视化市场，5500+ 社区插件 |
| 权限档位 | 沙箱受限 | 含 `danger-full-access` 全权限档 |
| Skill 目录 | 与其它 agent 共用 `.agents` | 独立在 `~/.dshs`，不读跨工具目录 |

<a id="run-from-source"></a>

## 快速开始

需要 Node.js 24.9 或更新版本。

```sh
git clone https://github.com/alexeulabs/dsh-red.git
cd deepseek-harness
pnpm install
pnpm run build
pnpm dshs web
```

默认在 `http://127.0.0.1:3180` 启动，并自动用默认浏览器打开。通过 SSH 连接时只打印宿主机 URL，本地转发由你的 SSH 客户端或编辑器负责；加 `--no-open` 可仅运行服务器。

进入界面后在**设置 → 模型**填入 API Key 即可开始。本版本不包含账号登录。

<a id="builtin-plugins"></a>

## 内置能力

### 命令清洗（dsh-purge-safe）

内置的 `dsh-purge-safe` 会改写模型收到的系统提示词，让被拒的请求正常执行，并可按模型分别配置提示词。它同时提供演练台。

改动只作用于本版本的提示词层，不修改模型本身。注入文件在 `~/.dshs/prompt-inject.md`，可直接编辑。

### 演练台

把一次交互动过的资产、凭据、漏洞、战果记进结构化事实库，跨会话保留，不用再翻聊天记录。

- 事实库存放：`~/.dshs/redteam`（SQLite）
- 预设与技能：内置，随版本更新
- 报告导出：`sqlmap`、`nuclei` 等工具输出可直接归档进对应资产

### 终端

右键侧栏的终端标签页提供真正持久的 shell（Windows 为 PowerShell PTY，其它平台为 bash），用于反弹 shell、`msfconsole`、`sqlmap` 交互会话等一次性命令跑不了的长任务。会话状态在多次操作之间保留。

### SSH

`@linxin666/dsh-ssh` 提供主机管理、浏览器内终端、SFTP、端口转发与代理，以及会话级 AI 直接操作远程主机。

主机配置是本地 JSON：`~/.dshs/dsh-ssh.json`。凭据由本版本的凭据存储管理，不写入该文件。

### 逆向工程（REA）

REA（`rea-agents`）以 stdio MCP 客户端随版本注册，工具直接可用，无需在 profile 里配置。覆盖 ELF/PE/Mach-O、.NET、APK/IPA、WASM、固件、流量包与浏览器页面。

引擎路径都可以用环境变量覆盖，换机器不必改代码：

| 变量 | 引擎 |
|---|---|
| `REA_ENTRY` | `rea-agents` 入口脚本 |
| `REA_NODE_COMMAND` | Node 可执行文件 |
| `GHIDRA_INSTALL_DIR` | Ghidra |
| `JAVA_HOME` | JDK |
| `REA_JADX_MCP_JAR` | JADX |
| `REA_APKTOOL_COMMAND` | Apktool |
| `REA_WABT_BIN_DIRECTORY` | WABT |
| `REA_TSHARK_COMMAND` / `REA_CAPINFOS_COMMAND` | Wireshark |

入口脚本不存在时该行自动停用，没装 REA 的机器照常启动。

### 插件市场

`dshmarket` 提供可视化市场，索引来自 `https://dshmarket.com/index.json`，浏览、搜索、一键安装。内置的**插件 → 发现**页与它并存，使用社区目录索引。索引内容在你确认安装之前不会运行。

<a id="environment"></a>

## 环境准备

内置技能假定了一台配好的 Linux 渗透机：`/usr/bin/nmap`、`/usr/bin/nuclei`、systemd 服务、API Key。这些前提**不会**随 DSH Special 一起安装。先跑自检确认当前机器能不能支撑作业：

```sh
node tools/redteam-preflight.mjs
```

输出会按技能列出每个工具的可用性、本地服务是否在线、外部配置是否填写。加 `--json` 便于脚本处理。

典型结果分三类缺口：

| 缺口 | 表现 | 影响 |
|---|---|---|
| 工具链 | `nmap`、`nuclei`、`sqlmap`、`fscan`、`chisel`、`hashcat` 等缺失 | 相关技能失败，或模型自行找替代命令 |
| Linux 运行时 | Windows 上 WSL 无发行版，技能里的 `/usr/bin/*` 与 `DISPLAY` 都不成立 | 浏览器自动化、systemd 托管的守护进程不可用 |
| 外部服务 | `FOFA_KEY`、VPS 主机与密钥未填 | FOFA 侦察、反弹 shell 接收端不可用 |

**路线一：WSL + Kali（技能原样可用）**

技能是按 Linux 写的，装一个发行版就不用改任何路径：

```sh
wsl --install -d kali-linux
wsl -d kali-linux -- sudo apt update
wsl -d kali-linux -- sudo apt install -y nmap nuclei sqlmap hashcat john netcat-openbsd dnsutils metasploit-framework
```

装完在 DSH Special 里让 agent 通过 `wsl -d kali-linux -- <命令>` 调用，或直接在终端标签页里 `wsl -d kali-linux` 进入。

**路线二：Windows 原生（贴合当前机器）**

逆向引擎已经就位，只有网络侧的 CLI 需要补。用 winget 或 scoop 装，然后自行把路径加进 `PATH`：

```powershell
winget install Insecure.Nmap
winget install WiresharkFoundation.Wireshark
scoop install nuclei sqlmap hashcat chisel
```

注意技能正文里写的是 Linux 路径，走这条路需要让 agent 按实际路径执行，或把技能文件里的路径改成本机路径。

**外部服务**

FOFA Key 与 VPS 登录信息在**设置 → 演练台**里填，写到 `~/.dshs/.env`。填完再跑一次自检确认。

<a id="permissions"></a>

## 权限档位

在界面右下角的权限选择器切换，或执行 `/permission <档位>`：

| 档位 | 沙箱 | 审批 |
|---|---|---|
| `workspace-write` | 只写工作区与临时目录 | 每次确认 |
| `danger-full-access` | 无限制 | 不询问 |

渗透作业通常选 `danger-full-access`：否则每次 `nmap`、每次写目标目录都要点确认。

<a id="workflow"></a>

## 典型工作流

1. **侦察** — 让 agent 用 REA 的被动/主动侦察技能收集资产与指纹，结果自动进演练台
2. **打点** — 复现漏洞时用浏览器标签页做越权与逻辑测试，用终端跑 `sqlmap`、`nuclei`
3. **后渗透** — 通过 SSH 插件维持主机访问，用终端标签页挂持久会话与隧道
4. **取证与逆向** — 拖进样本，REA 直接反编译、脱壳、分析流量
5. **收尾** — 从演练台导出报告，资产、凭据、漏洞按资产归组

<a id="isolation"></a>

## 隔离

命令、主目录、端口、用户数据、Skill 目录全部独立，官方 `dsh` 与本版本的 shell 状态互不影响。

本版本优先读取 `$DSHS_HOME`，不把 `$DSH_HOME` 当作自己的主目录。启动时会把 `DSH_HOME` 对齐到自己解析出的目录，让只认这个变量的第三方插件也把数据落在 `~/.dshs`。

**Skill 目录**

| 作用域 | 本版本 | 官方 dsh | 其它 agent 工具 |
|---|---|---|---|
| 用户级 | `~/.dshs/skills` | `~/.dsh/skills` | `~/.agents/skills` |
| Agent 级 | `~/.dshs/agents/skills` | `~/.dsh/agents/skills` | `~/.agents/skills` |
| 项目级 | `<项目>/.dsh/skills` | `<项目>/.dsh/skills` | `<项目>/.agents/skills` |

`.agents/` 是多工具共用约定，本版本默认不扫描，因此不会读到别的工具放在那里的技能。需要临时共用时设置 `DSHS_SKILL_AGENTS_ROOTS=1`。

不要把这个包 `npm install -g` 到与官方 `@deepseek-ai/dsh` 相同的前缀，那会替换官方包。在检出目录里用 `pnpm dshs`。

<a id="data"></a>

## 数据位置

全部在本机，不联网上传：

| 内容 | 路径 |
|---|---|
| 提示词注入 | `~/.dshs/prompt-inject.md` |
| 演练台事实库 | `~/.dshs/redteam` |
| SSH 主机 | `~/.dshs/dsh-ssh.json` |
| 凭据 | `~/.dshs/.credentials.yaml` |
| 会话记录 | `~/.dshs/sessions` |
| 技能 | `~/.dshs/skills` |
| 插件 profile | `~/.dshs/profiles` |

<a id="development"></a>

## 开发

请先阅读[开发指南](docs/development.md)与[架构文档](docs/architecture.md)。

`pnpm run dev:web` 在一个终端里完成构建、启动，并在源码修改时重建 client bundle；`make help` 列出 Web 与 Desktop 对应的 Make target。

面向 agent：请遵循 [AGENTS.md](AGENTS.md)。

<a id="scope"></a>

## 使用范围

本版本是渗透测试与安全研究的作业环境。请只在你有明确授权的目标上使用；对未授权系统的操作由使用者承担。

<a id="license"></a>

## 许可证

[MIT](LICENSE)

基于 DeepSeek Harness 二次分发，遵循其 MIT 许可。内置第三方插件保留各自许可，详见各插件目录下的 `LICENSE` 与 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
