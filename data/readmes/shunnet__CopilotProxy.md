<h1 align="center">
  <img width="120" height="120" src="https://api.snet.cn/pic/nuget.png" alt="Snet Logo"/><br/>
  📦 CopilotProxy
</h1>

<p align="center">
  <b>🛠️ 多模型 AI 代理 — 将 GitHub Copilot 连接到 DeepSeek & 小米 MiMo</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/.NET-10.0%2B-purple.svg" alt=".NET 10"/>
  <img src="https://img.shields.io/badge/license-MIT-green" alt="MIT"/>
  <img src="https://img.shields.io/badge/platform-Windows-success" alt="Windows"/>
  <a href="https://github.com/shunnet/CopilotProxy/releases/latest"><img src="https://img.shields.io/github/v/release/shunnet/CopilotProxy" alt="Latest Release"/></a>
  <a href="https://github.com/shunnet/CopilotProxy/actions/workflows/release.yml"><img src="https://github.com/shunnet/CopilotProxy/actions/workflows/release.yml/badge.svg?branch=main" alt="Build and validation"/></a>
  <img src="https://img.shields.io/github/stars/shunnet/CopilotProxy?style=social" alt="GitHub Stars"/>
</p>

<p align="center">
  <a href="https://snet.cn"><b>🌐 官方网站</b></a> ·
  <a href="https://www.nuget.org/profiles/shun"><b>📚 NuGet</b></a> ·
  <a href="https://github.com/shunnet"><b>💻 GitHub</b></a> ·
  <a href="https://github.com/shunnet/CopilotProxy/releases/latest"><b>📥 下载</b></a>
</p>

## 📖 项目介绍

CopilotProxy 是一个 **Windows WPF 管理工具与本地 Ollama / OpenAI Chat Completions 兼容代理**，在 GitHub Copilot Chat / Agent 与 DeepSeek、小米 MiMo 之间转换协议。WPF 提供配置、构建、启停和日志界面，Node.js / Bun 服务负责实际转发。

模型从账号可见的供应商官方目录自动发现，**不维护固定型号白名单，不设置默认模型或隐藏回退**。每次生成请求必须显式提供目录返回的完整 `model`。IDE 仍需按下文添加自定义端点，供应商权限、额度和模型能力决定实际可用范围。

## ✨ 功能亮点

<table>
<tr><td>🔌 <b>官方模型发现</b></td><td>DeepSeek / MiMo 官方目录、缓存刷新、认证失效处理；新型号无需修改允许列表</td></tr>
<tr><td>🖥️ <b>WPF 桌面管理</b></td><td>可视化设置、构建、启动/停止/重启、实时日志；保留单实例、托盘和中英文界面</td></tr>
<tr><td>🔄 <b>双协议入口</b></td><td>Ollama NDJSON 与 OpenAI JSON/SSE 共用模型、消息、队列和上游传输管线</td></tr>
<tr><td>🧠 <b>推理与工具</b></td><td>尊重显式控制及上游默认，保留原生工具 ID、参数和完整推理历史</td></tr>
<tr><td>🖼️ <b>视觉输入</b></td><td>向支持图片的模型转发 Ollama images / OpenAI image_url，能力以实际元数据为准</td></tr>
<tr><td>⚡ <b>有界并发</b></td><td>队列上限、总截止时间、取消与下游背压清理；溢出明确失败</td></tr>
<tr><td>📦 <b>无损默认</b></td><td>off 默认不压缩；lite 仅整理工具描述空白，不截断工具结果或改写历史</td></tr>
<tr><td>🛡️ <b>配置与进程保护</b></td><td>仅停止自有进程树，构建保留运行配置，发布按清单排除个人密钥与缓存</td></tr>
<tr><td>📊 <b>可验证交付</b></td><td>JS / C# 回归、VS 构建、三种运行时包、发布排除检查和本地 HTTP 压测</td></tr>
<tr><td>🔍 <b>版本与分发</b></td><td>项目版本统一注入桌面、代理及分发清单，GitHub Actions 验证后生成版本 Release</td></tr>
</table>

## 📋 系统要求

| 用途 | 要求 |
|---|---|
| Windows x64 Node 包 / 源码 | Node 24；源码最低 Node 22，按 lockfile 安装依赖 |
| Windows x86 Node 包 | Node 22，实测 22.23.3 / ia32 在 x64 Windows WOW64 下运行；Node 24 不提供 Windows x86 包 |
| Windows x64 Bun 包 / 源码 | Bun，实测 1.4.3，原生 HTTP 与独立编译 |
| WPF 开发 | Windows、.NET 10 SDK、Visual Studio 2026 的 .NET 桌面开发工作负载 |
| 上游 | 至少一个有效 DeepSeek / MiMo Key；权限和额度决定可见及可调用模型 |

Node 22 维护期于 **2027-04-30** 结束，x86 部署需在此之前重新评估支持范围。[Node 发布计划](https://github.com/nodejs/Release/blob/main/schedule.json)。启动器采用 V8 按架构选择的默认堆限制；需要调优时使用适合目标架构的 `NODE_OPTIONS`。

## 🚀 快速开始

可先从 [GitHub Releases](https://github.com/shunnet/CopilotProxy/releases/latest) 下载对应架构的完整桌面包。Windows x64 可选 Node 或 Bun 包；Windows x86 选择 Node 包。WPF 需要 .NET 10 Desktop Runtime；源码构建另需下方 SDK 和开发环境。

### 1️⃣ 配置 API Key

首次复制 `src/script/.env.example` 为 `.env` 并填入 Key；已有文件请直接编辑。也可在 WPF 设置页保存，或设置 `SNET_ENV_PATH` 指向外部配置。进程环境优先于文件，显式配置路径不存在时启动失败。不要提交个人配置。

### 2️⃣ 构建 & 启动

下载包解压后打开 WPF 程序，保存设置并点击 **启动**；源码方式可先构建再启动，或使用以下 Node 入口：

```powershell
Set-Location src/script
npm.cmd ci
Copy-Item .env.example .env   # 仅首次创建
notepad .env
npm.cmd run node             # Node 前台
# 或 .\start.cmd             # Windows 自动选择运行时
# 或 npm.cmd start           # Bun
```

默认地址 `http://127.0.0.1:11434`。端口占用时明确失败，不换端口、不终止占用者。管理接口只接受可信本机连接，修改操作另校验 Origin/Host；该服务未提供公网鉴权。

### 3️⃣ 添加到 Visual Studio

使用 **18.10+ 的新 Agent (Preview)**。打开 Chat → 模型选择器 → **Add a model / Manage Models** → 连接 **Ollama 自定义端点**，服务地址为 `http://127.0.0.1:11434`，选择目录返回的完整 ID，再进入 Agent (Preview)。OpenAI 自定义端点也可连接 Chat Completions：基地址为 `http://127.0.0.1:11434/v1`，实际请求路径 `/v1/chat/completions`。字段名称以当前界面为准，不把 VS Code JSON 配置粘贴进 Visual Studio。

微软说明 18.10 的 BYOK 替换旧 Ask/Agent 体验，既有 Ollama 模型可能需重新添加。依据：[当前 VS 指南](https://learn.microsoft.com/en-us/visualstudio/ide/copilot-select-add-models?view=visualstudio)、[2026-09-29 更新说明](https://devblogs.microsoft.com/visualstudio/visual-studio-september-update-power-your-workflow-with-your-model/)。本机 VS Professional 18.11.0 构建通过；实际 IDE GUI 未执行，不承诺所有内联补全或其他 IDE 功能。

### 4️⃣ 添加到 VS Code

模型选择器 → **Manage Language Models**（命令 `Chat: Manage Language Models`）→ **Add Models → Custom Endpoint**，选择 **Chat Completions**。当前文档已弃用内置 Ollama 提供程序及旧 `github.copilot.chat.customOAIModels`；原生 Ollama 方式请按官方 Ollama 扩展的当前说明设置 `http://127.0.0.1:11434`。

Custom Endpoint 的 `chatLanguageModels.json` 可使用自动发现：

```json
[
  {
    "name": "CopilotProxy",
    "vendor": "customendpoint",
    "apiType": "chat-completions",
    "url": "http://127.0.0.1:11434/v1"
  }
]
```

供应商 Key 只配置在代理端；如客户端强制要求 Key，可填无权限的本地占位文本，代理不使用该字段选择供应商凭据。手动配置时从 `/v1/models` 复制 ID，完整 URL 用 `http://127.0.0.1:11434/v1/chat/completions`，工具/视觉/上下文以实际元数据为准。Responses 和 Messages 未实现。

当前 Agent Host 的 BYOK 可能需要实验设置 `chat.agentHost.byokModels.enabled`，组织策略也影响可用性。依据：[VS Code 当前模型配置](https://code.visualstudio.com/docs/agent-customization/language-models)。实际 VS Code GUI 未验收；官方 Copilot SDK 1.0.23 / runtime 1.0.100 的真实客户端本地协议测试已通过，包括多轮工具、推理和空 ID 增量。

## 🤖 支持模型

- 启动及五分钟 TTL 过期后访问供应商官方 `/models`。ID 为 `ds/<官方ID>` / `mimo/<官方ID>`；`:latest` 只是兼容别名。认证失败或凭据/端点变更立即失效，暂时故障最多使用同凭据/端点一小时内成功目录并标记 `stale`。
- API 元数据优先。仅对确切型号的缺失字段使用注明来源的官方能力补充；未知能力/上下文保持未知，未来新型号不会因此被过滤。专用语音模型不列为通用聊天模型。验收账号快照不是固定型号表。

| 供应商 | 模型 ID | 选择方式 |
|---|---|---|
| 🔮 DeepSeek | `ds/<官方ID>` | 从 `/api/tags` 或 `/v1/models` 获取 |
| 🎯 小米 MiMo | `mimo/<官方ID>` | 从 `/api/tags` 或 `/v1/models` 获取 |

💡 型号以官方 API 当前返回为准；`/api/show` 提供实际已知上下文和能力，未知字段不伪造。

## ⚙️ 配置参数

完整模板见 [`.env.example`](src/script/.env.example)。按启动快照加载，保存新配置后重启；WPF 保留未知有效配置键。

| 变量 | 默认值 | 含义 |
|---|---|---|
| `SERVER_HOST` / `SERVER_PORT` | `127.0.0.1` / `11434` | 监听地址 |
| `DEEPSEEK_API_KEY` / `MIMO_API_KEY` | 空 | 各供应商凭据 |
| `DEEPSEEK_BASE_URL` / `MIMO_BASE_URL` | 见模板 | 目录与生成共用地址 |
| `CONCURRENCY_STANDARD` / `CONCURRENCY_THINKING` | `15` / `5` | 按实际思考状态分队列 |
| `MAX_QUEUE_SIZE` / `QUEUE_TIMEOUT_MS` | `100` / `30000` | 每队列等待上限；容量 0 禁止等待 |
| `REQUEST_TIMEOUT_MS` / `THINKING_TIMEOUT_MS` | 各 `300000` | 排队、请求与读取共用总截止时间 |
| `MAX_REQUEST_BODY_BYTES` / `MAX_UPSTREAM_RESPONSE_BYTES` | 各 `67108864` | 读取字节限制，非 token 上限 |
| `RETRY_MAX` / `RETRY_BASE_DELAY_MS` | `6` / `100` | 明确 429/502/503/504 有限重试；不重播不确定网络 POST 或已输出的流 |
| `MODEL_TTL_MS` / `MODEL_STALE_TTL_MS` | `300000` / `3600000` | 新鲜期 / 陈旧结果期限 |
| `DEFAULT_TEMPERATURE` | 空 | 上游默认；非空范围 0..2 |
| `COMPRESSION_LEVEL` / `SNET_LANGUAGE` | `off` / `zh` | off 或 lite；zh 或 en |

推理恢复缓存默认 5,000 条 / 16 MiB / 24 小时，条目与 UTF-8 字节双重约束，到期按访问清理。默认日志只记录元数据，不打印正文或密钥。

## 🌐 API 端点

| 方法与路径 | 行为 |
|---|---|
| `GET /api/tags`、`/api/list`、`/api/models`、`/v1/models` | 动态目录、真实已知能力、陈旧状态 |
| `POST /api/show` | 能力、已知上下文、声明的思考选项 |
| `POST /api/chat`、`/api/generate` | 默认 NDJSON；`stream:false` 单 JSON，保留 thinking、换行、结束原因和用量 |
| `POST /v1/chat/completions` | JSON/SSE、原生工具与推理，参数只输出新增片段 |
| `POST /v1/completions` | 字符串 prompt 的 JSON/SSE；不支持 suffix、echo、best_of、多 choice，明确拒绝 |
| `GET /api/ps` | 当前活跃请求模型，不伪称本地驻留模型 |
| `GET /health`、`/api/version`、`/version` | 健康、版本与目录状态 |
| `GET /api/stats`、`POST /api/refresh`、`/api/diagnostics` | 本机统计、刷新、本地诊断，诊断不发推理请求 |
| `GET/POST /api/language`、`POST /api/session/stop`、`GET /stop` | 语言、本机会话取消、优雅关闭 |
| `POST /api/pull`、`/api/push`、`/api/copy`、`/api/create`、`/api/embed`、`/api/embeddings`；`DELETE /api/delete` | 未实现的本地操作明确 501 |

缺少 model / 无效 JSON 为 400，未知模型 404，超大输入 413，队列溢出 503。上游认证、额度、限流保留失败状态；流开始后的错误不伪造成功结束。没有 `/v1/responses`。

## ⌨️ WPF 界面操作

| 按钮 | 操作 |
|---|---|
| 🏗️ 构建 | 构建运行时分发包，保留已有配置和失败前的有效产物 |
| ⚙️ 设置 | 编辑实际运行入口旁的配置；保留未知配置键，运行中保存后重启服务以应用配置 |
| ▶️ 启动 | 启动所选入口；端口冲突明确失败，不终止其他程序 |
| ⏹️ 停止 | 取消并等待本窗口启动的进程树退出 |
| 🔄 重启 | 停止自有进程后重新启动 |
| 🔧 重建 | 停止后安全构建，不先删除整个 .dist |
| 🔍 检查更新 | 查询 GitHub 最新 Release 并比对版本 |
| 🧹 清空 | 清除界面日志显示 |

## 🏗️ 技术架构

```text
┌──────────────────────────────────────────┐
│ WPF 管理工具 (.NET 10 / Visual Studio)    │
│ 配置 · 构建 · 自有进程控制 · 日志 · 语言   │
└────────────────────┬─────────────────────┘
                     │ Node / Bun 源入口或托管 service.exe
                     ▼
┌──────────────────────────────────────────┐
│ 本地 HTTP 入口 (Hono / Node / Bun)        │
│ Ollama API            OpenAI Chat API    │
├──────────────────────────────────────────┤
│ 官方模型目录 · 能力元数据 · 消息规范化      │
│ 有界队列 · 总截止时间 · 取消 · 推理缓存    │
│ 统一上游传输 → JSON / SSE / NDJSON 编码   │
└────────────────────┬─────────────────────┘
                     ▼
             DeepSeek / Xiaomi MiMo
```

## 📁 项目结构

```text
CopilotProxy/
├── .github/
│   ├── workflows/release.yml          # 验证、三种分发包、版本标签发布
│   └── scripts/Publish-Release.ps1    # 标签一致性与已有 Release 保护
├── docs/validation/                  # 验收记录、原始问题映射与边界
├── image/                            # 历史界面截图
├── src/
│   ├── Snet.CopilotProxy.csproj      # WPF 项目与唯一版本来源
│   ├── App.xaml.cs / MainWindowModel.cs
│   ├── handler/
│   │   ├── DesktopRuntimeController.cs # 构建、设置与启动配置的一致入口
│   │   ├── CmdHandle.cs / OwnedProxyProcess.cs
│   │   └── EnvHandle.cs / SingleInstanceHandle.cs
│   └── script/
│       ├── .env.example              # 无个人密钥的配置模板
│       ├── start.cmd / build*.cmd    # 源码启动与构建入口
│       ├── Build.ps1 / Package.ps1   # 暂存、回滚、清单导出
│       ├── Launcher.cs               # 共享托管进程 / SCM 包装程序
│       ├── src/
│       │   ├── server.js / app.js    # 运行时启动与 HTTP 路由
│       │   ├── config.js / model-registry.js
│       │   ├── capability-profiles.js # API 缺失字段的有来源能力补充
│       │   ├── message-pipeline.js / provider-transport.js
│       │   ├── protocol.js / sse-parser.js / concurrency.js
│       │   └── reasoning-cache.js / reasoning-replay.js
│       └── test/                     # JS 回归与独立本地负载脚本
└── tests/
    ├── Snet.CopilotProxy.Tests/       # 引用生产项目的桌面回归
    └── scripts/                      # 构建、启动、发布与密钥排除检查
```

## 🔧 高级特性

### 🧠 推理、工具与多模态

- 无显式推理控制时尊重上游默认，不按名称强制 LOW/MAX。原生 `think`、OpenAI `reasoning_effort` / `reasoning.effort` 和供应商 `thinking` 按声明能力映射；冲突/不支持值明确失败。MiMo 二元思考不伪造多档 effort。显式输出 cap 不增加，MiMo 使用同值 `max_completion_tokens`。
- 完整回传原生 `thinking` / `reasoning_content`，包括无工具历史助手轮次。仅在显式 `x-session-id`、精确历史、供应商、端点和凭据范围内恢复缺失推理；信息不足则明确失败，不按工作区猜测。内存缓存重启丢失。
- 仅转发原生声明工具调用，不从 Markdown、计划或推理文字制造动作。参数、ID、schema、大工具结果保持完整，非法交换明确拒绝。默认 `COMPRESSION_LEVEL=off` 无损；`lite` 仅压缩函数描述空白，其余旧模式拒绝。
- 原生 `messages[].images` 与 OpenAI `image_url` 输入传给视觉模型；不提供生成图片、音频合成或 embedding。`/api/show` 的 `general.architecture=copilotproxy` 是公开网关兼容命名空间，`copilotproxy.context_length` 供 Copilot 读取真实已知上下文，不是底层神经网络架构；未知上下文省略，IDE 回退由 IDE 决定。
- “会话保活”仅指有界本地状态与空闲清理，不自动发送付费 ping，不保证供应商 KV Cache 持续存在。

### ⚙️ 桌面配置一致性

WPF 设置与启动共用实际入口旁的 `.env`（优先 `.dist/service.exe`，否则源目录 `start.cmd`）。Build/Rebuild 逐字节保留已有 `.dist/.env`；首次桌面构建仅在配置不存在时从源文件复制，源文件也不存在则使用默认值。设置保存保留未知键，只修改所选运行入口的配置。`REQUEST_LOG=false` 在重启后关闭请求/完成元数据日志，错误仍可见。

## 🛠️ 构建独立包

| 脚本 | 说明 |
|---|---|
| `build.cmd` | 自动选择 Bun / Node.js |
| `build-bun.cmd` | 构建 Windows x64 原生 Bun 程序与托管入口 |
| `build-node.cmd` | 构建当前 Node 架构的可移植运行时包 |
| `Package.ps1` | 校验当前 distribution.json 的文件与哈希，导出干净包 |

在 `src/script` 中运行构建脚本。从源码构建的默认运行时取决于本机；下载包的架构与运行时由文件名标明。

`src/script/build.cmd` 选择 Bun 优先、Node 备用；`build-node.cmd` / `build-bun.cmd` 明确选择。Node 包携带当前构建架构的 Node；Bun 包为 x64 编译程序。失败返回非零，保留既有产物和本地配置。

两种包均由托管 `service.exe` 管理子进程和 SCM 入口。裸 JS 服务管理命令委托经过清单验证的相邻托管入口，没有该入口时明确失败。真实 SCM 安装/启动/停止尚未验收，隔离命令替身测试不能代替实际 Windows 服务验收。

本地 `.dist/.env` 会保留；`.dist` 是工作目录，不能直接归档。使用 `Package.ps1 -Destination <新的目录>` 按当前 `distribution.json` 的文件与哈希导出干净包，排除个人配置、缓存和旧运行时。WPF publish 只复制明确的源码/生产依赖，不复制源码 `.env`。发布要求新标签与项目版本一致，保留既有标签及 release。GitHub Actions 对 main / PR 执行验证与打包；推送与项目版本完全匹配的新版本标签后，才创建 Release。

## 🧪 开发与验收

仓库根目录执行，PowerShell 请逐条检查退出码，依赖安装结束后再构建：

```powershell
npm.cmd --prefix src/script ci
dotnet build Snet.CopilotProxy.sln -m:1 -p:UseSharedCompilation=false
npm.cmd --prefix src/script test
dotnet test tests/Snet.CopilotProxy.Tests/Snet.CopilotProxy.Tests.csproj -m:1 -p:UseSharedCompilation=false
```

Visual Studio 打开 `Snet.CopilotProxy.sln`，以 WPF 项目为启动项目构建/调试；Debug 输出包含脚本路径。VS MSBuild Debug/Release 已实际通过，WPF 交互仍需手动验收。VS Code 可用集成终端执行上述命令，用 Node 调试器启动 `src/script/src/server.js`，工作目录设为 `src/script`。

### 🔍 故障排查与本地压测

先查 `/health`、`/v1/models`，再用返回的完整 ID 生成。目录为空时检查供应商 Key、地址、权限和目录错误/陈旧状态，不补固定默认型号。`length` 表示达到调用者输出 cap，增加预算需由调用者决定。供应商约束仍适用，例如 DeepSeek thinking 不支持 required/named tool_choice。

```powershell
npm.cmd --silent --prefix src/script run bench > local-load.json
```

压测完全本地，不读取个人 `.env`。独立代理进程执行 1,000 请求/50 客户端、100 个 262,144 字符工具历史、队列饱和/取消和三轮 RSS 趋势，JSON 记录 TTFB、p50/p95、吞吐、RSS、队列与缓存。普通 `npm test` 仅选择 `*.test.js`，不会隐式压测。

截至 2026-10-20：156 个 JS 测试、25 个 C# 测试与 VS Debug/Release 构建通过；真实账号 7 个聊天模型基础 JSON/SSE 14/14、5 个视觉模型两路径合计 10/10、7 个模型推理工具三轮对话通过。初始失败、截断、探针修正及具体运行时边界保留在[验证记录](docs/validation/2026-10-20-modernization.md)。这些结果不代表 GUI、实际 SCM、原生 32 位 Windows、无限时长内存稳定性或未来型号已经验收。

📋 [完整验证记录与 38 项问题修复映射](docs/validation/2026-10-20-modernization.md)。各提交的远程构建结果请查看 [GitHub Actions](https://github.com/shunnet/CopilotProxy/actions/workflows/release.yml)。

## 📸 界面截图

> 💡 以下保留原项目截图，展示桌面与 IDE 的使用布局。模型列表、配置项和 IDE 菜单可能来自旧版，请以本文说明及当前界面为准。

<p align="center">
  <img src="image/1.png" alt="主界面（历史截图）" width="45%"/>
  <img src="image/2.png" alt="设置（历史截图）" width="45%"/>
</p>
<p align="center">
  <img src="image/3.png" alt="构建（历史截图）" width="45%"/>
  <img src="image/4.png" alt="启动服务（历史截图）" width="45%"/>
</p>
<p align="center">
  <img src="image/5.png" alt="VS Code 配置（历史截图）" width="45%"/>
  <img src="image/6.png" alt="模型列表（历史截图）" width="45%"/>
</p>
<p align="center">
  <img src="image/7.png" alt="Copilot Chat（历史截图）" width="45%"/>
  <img src="image/8.png" alt="终端输出（历史截图）" width="45%"/>
</p>
<p align="center">
  <img src="image/9.png" alt="完整工作流（历史截图）" width="80%"/>
</p>

## 📈 Star History

<a href="https://www.star-history.com/?repos=shunnet%2FCopilotProxy&type=date&legend=bottom-right">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=shunnet/CopilotProxy&type=date&theme=dark&legend=bottom-right"/>
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=shunnet/CopilotProxy&type=date&legend=bottom-right"/>
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=shunnet/CopilotProxy&type=date&legend=bottom-right"/>
 </picture>
</a>

<p align="center">
  <sub>Made with ❤️ by <a href="https://snet.cn">Snet.cn</a> · MIT License</sub>
</p>
