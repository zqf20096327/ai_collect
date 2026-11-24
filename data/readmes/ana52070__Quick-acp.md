# Quick-acp

[Codeg 配置教程](docs/Codeg配置教程.md) · [T3 Code 配置教程](docs/T3Code配置教程.md) · [能力对标](docs/能力对标.md) · [0.1.8更新说明](docs/0.1.8更新说明.md) · [0.1.8重装复验](docs/0.1.8重装复验.md) · [0.1.7更新说明](docs/0.1.7更新说明.md) · [0.1.6更新说明](docs/0.1.6更新说明.md) · [打包与CI发布](docs/打包与CI发布指南.md) · [贡献指南](CONTRIBUTING.md) · [安全策略](SECURITY.md)

[![CI](https://github.com/ana52070/Quick-acp/actions/workflows/ci.yml/badge.svg)](https://github.com/ana52070/Quick-acp/actions/workflows/ci.yml)
[![npm version](https://img.shields.io/badge/npm-0.1.8-blue.svg)](https://www.npmjs.com/package/quick-acp)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Node](https://img.shields.io/badge/Node-%3E%3D22-blue.svg)](package.json)
[![Community](https://img.shields.io/badge/Community-LINUX%20DO-orange?logo=linux)](https://linux.do/)

Quick-acp 是一个将 **AWS Quick (Quickwork)** 的 Claude 配额与推理能力，桥接到任何标准 **ACP (Agent Client Protocol)** 编辑器（如 **[codeg](https://github.com/xintaofei/codeg)**、**[T3 Code](https://t3.codes)**、**[Zed](https://zed.dev)** 等）的本地执行代理。同时为上游 Quick 补充了客户端所需的本地 Shell 执行、文件读写及多模态图片交互能力。

```
codeg / T3 Code / Zed ──ACP (JSON-RPC over stdio)──▶ quick-acp ──Quick bidi (WSS)──▶ Quick 网关
                                                        │
                                                        ├── 本机执行 Shell 与文件操作 (高危命令黑名单过滤，无沙箱)
                                                        ├── 会话级 MCP 挂载 (stdio / Streamable HTTP / SSE)
                                                        └── 本地会话持久化与状态恢复 (~/.quick-acp/sessions)
```

**无需安装 Quick 官方桌面客户端**，通过系统已有凭据或独立的浏览器 OIDC 登录即可直连网关。

> ⚠️ **quick-acp 会以你的用户权限在本机执行命令、读写文件，它不是沙箱。** 使用前请务必阅读 [安全策略](SECURITY.md) 中的安全边界说明。若需收紧，设置 `QUICK_ACP_ALLOW_SHELL=0` 关闭命令执行，或 `QUICK_ACP_PERMISSION_MODE=ask` 逐次确认敏感操作。

---

## 核心特性与验证状态

| 能力 | 当前实现 | 已有验证证据 |
|---|---|---|
| ACP、本机读写与Shell | 标准stdio协议、本地文件工具、命令执行与工具卡片 | 0.1.8正式包复验：超额明确未完成（max_turn_requests）；额度内10次本机调用、7项测试、三文件自主回读通过 |
| 嵌套代码块与多调用 | 平衡JSON解析、流过滤、顺序工具调度 | 离线回归；Codeg写入含代码块README并回读通过 |
| 图片与嵌入上下文 | 首轮图片转发、嵌入文本提取 | 代码与回归覆盖；本轮Codeg未做图片专项测试 |
| 会话列表、恢复与分叉 | 本地持久化、原thread续接、会话级全量历史分支 | 离线ACP集成通过；Codeg交互入口未做专项复验 |
| MCP | 官方SDK stdio/Streamable HTTP/SSE客户端 | 本地协议fixture覆盖工具调用、取消和关闭；外部服务及Codeg界面未专项复验 |
| 计划、命令与技能 | plan_update、/help /mode /plan /clear、SKILL.md与skill_read | 离线状态机与ACP集成通过 |
| 权限与提问 | auto/ask、敏感操作审批、单选按钮 | 离线拒绝无副作用与ACP双向请求通过；不支持多选或自由文本表单 |
| 未保存缓冲区与用量 | 客户端fs委托；_meta与自定义用量扩展 | 离线集成通过；用量UI取决于客户端支持 |
| 重试、取消和并发保护 | 分类退避、副作用/正文守卫、同会话互斥 | 离线回归覆盖；未做真实服务故障注入 |
| 模型选择 | Fast/Balanced/Smart档位；不接受任意modelId | 当前网关接入未提供已验证的任意选模接口 |

Windows已实测。CI工作流配置Windows与Ubuntu，尚无本轮远端CI运行结果；macOS未配置该矩阵，也未本地实测。文件工具允许绝对路径，Shell按本机进程权限执行，命令黑名单不构成系统沙箱。

**版本演进与稳定性**：0.1.6加入默认本机路由保护；0.1.7修复心跳误杀与套接字异常误报认证；0.1.8修复工具额度耗尽误报完成，返回max_turn_requests并显示未完成进度。0.1.8正式发布包的干净重装复验已通过：超额任务（Codeg会话828）正确返回max_turn_requests并标为未完成，额度内任务（会话827）10次调用完成项目、7项测试与三文件自主回读。

---

## 安装与快速开始

### 方式一：npx 免安装直接使用（首选推荐）

无需克隆代码或本地编译，确保环境 **Node.js ≥ 22** 即可开箱即用：

```bash
# 运行环境自检（只读，先跑这个）
npx -y quick-acp doctor

# 登录 AWS Quick（已登录官方桌面端时可跳过）
npx -y quick-acp-login --start-url https://<你的SSO入口>.awsapps.com/start

# 启动代理（通常由 ACP 客户端拉起，手工运行会阻塞等待 stdin）
npx -y quick-acp@0.1.8
```

> **注意**：`quick-acp` 没有 `--version` / `--help` 参数，带上这些参数它会忽略并直接启动 ACP 服务、阻塞等待 stdin，看起来像卡住。要确认版本请用 `npm ls -g quick-acp` 或 `npm view quick-acp version`。

### 方式二：本地源码编译运行（次选，二次开发）

```bash
git clone https://github.com/ana52070/Quick-acp.git
cd Quick-acp
npm install
npm run build
npm test              # 全套离线测试（build + probe + smoke + 19项回归 + 9项路由 + 11步集成 + 5项根因 + 10项工具预算）
```

---

## 登录与鉴权

Quick-acp 支持两种鉴权方式：

1. **自动读取系统凭据（推荐日常使用）**：
   若本机已运行并登录过 Quick 官方桌面端，Quick-acp 会自动从 Windows 凭据管理器或 macOS Keychain 中读取刷新令牌并自动重组。
2. **免桌面端浏览器单点登录**：
   ```bash
   npx -y quick-acp-login --start-url https://<your-sso-portal>.awsapps.com/start
   ```
   启动本地单点登录并在浏览器中完成认证，刷新凭据保存在本地 `~/.quick-acp/login.json`（权限 0600），后续直连 AWS OIDC 刷新。

运行自检诊断命令检查凭据有效性：
```bash
npx -y quick-acp doctor
```

---

## 编辑器配置指南

支持任何标准 ACP 客户端。下面给出 Codeg、T3 Code、Zed 三种已验证或已知可用形态的配置，并为每种客户端附一段**可直接粘给 AI 助手执行的配置提示词**。

### 环境变量速查

配置里出现的环境变量都在这里，按需增减。带「默认」的项不写也是这个值。

| 变量 | 默认 | 作用 |
| --- | --- | --- |
| `QUICK_ACP_ALLOW_SHELL` | `1` | 设为 `0` 关闭本机命令执行，只保留文件读写。**安全相关**，见 [SECURITY.md](SECURITY.md) |
| `QUICK_ACP_PERMISSION_MODE` | `auto` | 设为 `ask` 时，敏感操作（删除、覆盖、发布等）逐次请求确认 |
| `QUICK_ACP_MAX_TOOL_ROUNDS` | `12` | 单回合工具调用上限，失败调用同样计数。超出时返回 `max_turn_requests` |
| `QUICK_ACP_WORKSPACE` | 进程工作目录 | 工作区根目录。ACP 客户端通常通过 `session/new.cwd` 传入，一般不用设 |
| `QUICK_ACP_SESSIONS_DIR` | `~/.quick-acp/sessions` | 本地会话持久化目录 |
| `QUICK_ACP_TURN_TIMEOUT_MS` | `180000` | 单轮上游等待上限（毫秒） |
| `QUICK_ACP_HEADLESS` | 未设置 | 设为 `1` 时禁用 `ask_user_question`，适合无人值守场景 |
| `QUICK_ACP_DEBUG` | 未设置 | 设为 `1` 输出调试日志到 `stderr` |
| `QUICK_ACP_QUICKWORK_HOME` | `~/.quickwork` | Quick 桌面端数据目录，用于自动读取凭据 |

### Codeg 配置

**推荐用 npx 分发**，版本固定，不用管路径。在 **Settings → Agents → Add custom agent** 中填：

```json
{
  "npx": {
    "package": "quick-acp@0.1.8",
    "args": []
  }
}
```

若你的 Codeg 版本要求 command/args 形式：

```json
{
  "command": "npx",
  "args": ["-y", "quick-acp@0.1.8"],
  "env": {
    "QUICK_ACP_ALLOW_SHELL": "1",
    "QUICK_ACP_PERMISSION_MODE": "auto",
    "QUICK_ACP_MAX_TOOL_ROUNDS": "12"
  }
}
```

本地源码构建的备选方案：

```json
{
  "command": "node",
  "args": ["D:/projects/quick-acp/dist/main.js"],
  "env": { "QUICK_ACP_ALLOW_SHELL": "1" }
}
```

**交给 AI 助手执行的提示词：**

````text
请帮我在 Codeg 里配置 quick-acp 这个 ACP 智能体。

背景：quick-acp 已发布到 npm，包名 quick-acp，当前版本 0.1.8，是一个把 AWS Quick
的 Claude 额度桥接成标准 ACP agent 的本地代理。

请按以下步骤操作，每一步做完告诉我结果，遇到问题停下来说明，不要猜测：
1. 先确认 Node.js 版本：运行 node -v，必须 ≥ 22。
2. 确认 quick-acp 能跑：运行
   npx -y quick-acp@0.1.8 doctor
   这个命令只读，会打印平台、Quick 数据目录、凭据可读性和 outpost 状态。
   注意：不要用 --version 或 --help 验证——quick-acp 没有这两个参数，它会直接启动
   ACP 服务并阻塞等待 stdin，看起来像卡住。
3. 在 Codeg 打开 Settings → Agents → Add custom agent，按 npx 分发方式填写：
   package 填 quick-acp@0.1.8，args 留空。
4. 如果 Codeg 这一版只支持 command/args 形式，改填：
   command = npx，args = ["-y", "quick-acp@0.1.8"]，
   env 增加 QUICK_ACP_ALLOW_SHELL=1。
5. 保存后新建一个 Quick 会话，发送一句普通提示（例如「列出当前目录下有哪些文件」），
   确认三件事：能连上、工具调用真的执行了、回复里的文件名与实际一致。
   如果提示需要登录，先运行 npx -y quick-acp-login --start-url <你的 SSO 入口>。
6. 把最终填写的配置原样贴给我。

注意：
- 不要修改我的账户设置、系统环境变量或全局 npm 配置。
- 不要把任何 token 或凭据写进配置文件。
- 如果 Codeg 版本与我说的入口名称不一致，以你实际看到的界面为准，并告诉我差异。
````

### T3 Code 配置

**T3 Code 在 Windows 上无法通过界面接入 quick-acp，必须手写配置文件。** 完整的排查过程、逐字段说明与 7 类常见卡点见 [T3 Code 配置教程](docs/T3Code配置教程.md)。这里给出可直接用的配置。

前置：把仓库里的 [`scripts/t3-acp-compat.mjs`](scripts/t3-acp-compat.mjs) 放到一个固定路径。

配置文件位置：`%USERPROFILE%\.t3\userdata\settings.json`（macOS/Linux 为 `~/.t3/userdata/settings.json`）

```json
{
  "providerInstances": {
    "quick-acp": {
      "driver": "acpRegistry",
      "displayName": "Quick ACP",
      "enabled": true,
      "config": {
        "source": "local",
        "commandPath": "E:\\Nodejs\\node.exe",
        "commandArgs": [
          "D:\\path\\to\\quick-acp\\scripts\\t3-acp-compat.mjs"
        ]
      }
    }
  }
}
```

三条硬性要求，少一条就不工作：

1. `commandPath` 必须是**原生 `node.exe` 的绝对路径**。T3 在 Windows 上以 `shell: false` 启动，硬拒 `.cmd`/`.bat`，而 npm 全局装的 `quick-acp` 恰好只有 `.cmd` shim。
2. `commandArgs` 指向**兼容脚本**，不要指向 `main.js`。T3 会注入 40 个自带的 MCP 工具，quick-acp 会把它们的完整 JSON Schema 拼进上游提示词，帧涨到 100366 字节，顶爆网关 64 KB 上限。
3. 文件必须是**无 BOM 的 UTF-8**，且改完**重启 T3**（T3 的配置缓存 TTL 是 infinity，没有文件监听）。

**交给 AI 助手执行的提示词：**

````text
请帮我在 T3 Code 里配置 quick-acp 这个 ACP 智能体，我的系统是 Windows。

背景（很重要，别跳过）：quick-acp 不在 ACP 官方 Registry 里，所以 T3 界面里的
ACP Registry 搜不到它；界面上的 Enter manually 只能填 Registry ID，也用不了；
Local ACP command 只有一个 Executable 输入框，而 T3 在 Windows 上会拒绝 .cmd/.bat
并提示 "Local ACP commands launch without a shell"。所以只能改配置文件，不要浪费时间
在界面上试。

请按以下步骤操作，每步做完报告结果，任一步失败就停下说明原因，不要硬凑：

1. 确认 T3 Code 已安装并至少启动过一次，检查这个文件所在目录是否存在：
   %USERPROFILE%\.t3\userdata\
   如果不存在，请先启动一次 T3 Code 再退出。

2. 确认 Node.js 可执行文件的绝对路径：运行 where node，取第一行结果。

3. 确认 quick-acp 已全局安装并能运行：
   npm ls -g quick-acp --depth 0
   node <第2步的路径> <npm 全局目录>\node_modules\quick-acp\dist\main.js --help
   记下 main.js 的绝对路径。

4. 在 <quick-acp 仓库目录>\scripts\t3-acp-compat.mjs 放一个兼容脚本。如果仓库里没有
   这个文件，从 https://github.com/ana52070/Quick-acp 获取。这个脚本的作用是：转发
   ACP stdio 消息，同时清空 session/new 里的 mcpServers——否则 T3 注入的 40 个 MCP
   工具会让发给上游的提示词超过 64 KB，报 FrameTooLarge。

5. 备份并写入 %USERPROFILE%\.t3\userdata\settings.json（注意：必须是 UTF-8 无 BOM，
   不要用 PowerShell 的 Out-File 默认编码），内容为：
   {
     "providerInstances": {
       "quick-acp": {
         "driver": "acpRegistry",
         "displayName": "Quick ACP",
         "enabled": true,
         "config": {
           "source": "local",
           "commandPath": "<第2步的 node.exe 绝对路径>",
           "commandArgs": ["<第4步的兼容脚本绝对路径>"]
         }
       }
     }
   }
   JSON 里的 Windows 路径反斜杠要转义成双反斜杠。

6. 完全退出并重启 T3 Code（手改配置必须重启才生效，没有文件监听）。

7. 用 T3 自带 CLI 验证，注意 --provider 和 --model 必须一起给：
   & $env:USERPROFILE\.t3\bin\t3.cmd thread start --provider quick-acp --model default --wait --json "." "请列出当前工作区根目录下的所有一级子目录"
   期望看到 status 为 completed，且 reply 里的目录名与实际一致。

8. 如果报 FrameTooLarge，说明兼容脚本没生效，检查 commandArgs 是否指向兼容脚本而不是
   main.js。如果报 Local ACP commands launch without a shell，说明 commandPath 填成了
   .cmd 或 .bat。

9. 把最终写入的配置原样贴给我（把绝对路径保留，不要贴任何 token）。

注意：
- 不要修改我的账户设置、系统环境变量或全局 npm 配置。
- 不要改 quick-acp 的版本。
- 不要提交或推送任何 git 变更。
````

### Zed 配置

在 Zed 的 `settings.json` 中：

```json
{
  "agent_servers": {
    "Quick ACP": {
      "type": "custom",
      "command": "npx",
      "args": ["-y", "quick-acp@0.1.8"],
      "env": {
        "QUICK_ACP_ALLOW_SHELL": "1"
      }
    }
  }
}
```

> Zed 的接入未经本项目实测，配置依据 ACP 标准形态给出。若遇到问题，欢迎按 [客户端接入问题模板](.github/ISSUE_TEMPLATE/client_compat.md) 反馈。

### 其他 ACP 客户端

任何支持「自定义 stdio ACP agent」的客户端都可以用同一组参数：命令 `npx`，参数 `["-y", "quick-acp@0.1.8"]`。需要时可加[环境变量速查](#环境变量速查)中的项。

---

## 实测协议特性与运行说明

经真实网关流量与契约实测验证的关键协议特征：

1. **鉴权参数位置**：网关 WebSocket 握手必须在 URL 查询参数中提供 `?token=<jwt>`；使用 HTTP `Authorization: Bearer` 头会被网关拒绝（返回 401）。
2. **必填 surfaceType**：握手参数必须包含 `?surfaceType=QUICK_WORK_DESKTOP_WINDOWS`。
3. **真实连接路径**：网关双向流端点为 `/streaming/quickwork-chat-bidirectional-stream`。
4. **空闲保活机制**：网关在空闲超过 95 秒无帧时会主动断开，Quick-acp 内部设置 45 秒定时发送 ping 帧维持心跳；在持续业务数据流交互时，业务入站帧能够正常维持保活，避免旧看门狗仅依靠控制 pong 造成的误杀。
5. **多轮消息完成时机**：服务端推送的 `turn_usage` 早于真实的对话流收尾；必须以 `message_complete` 事件作为当前轮次结束的判定基准，确保后续工具结果不会被上一轮未关闭的会话吞并。
6. **标准协议字段与自定义扩展划分**：
   - **标准 ACP 规范字段**：会话生命周期严格适配标准 ACP 规范，声明 `protocolVersion: 1` 与 `agentCapabilities.loadSession: true`，会话通知完全使用标准类型（正文、思考流、工具调用卡片、`plan` 计划卡片与 `available_commands_update` 斜杠命令列表）；
   - **非标准自定义扩展**：单轮 Token 消耗指标通过 `PromptResponse._meta.usage` 以及非标准扩展通知 `session/usage` 推送；会话列表与分叉通过 `session/list` 与 `session/fork` 扩展提供。
7. **工具调用额度与截断规范 (0.1.8)**：默认单回合允许调用工具 12 次（失败调用亦计入额度），达到上限且任务未完成时返回 `stopReason: 'max_turn_requests'` 而非 `end_turn`，并输出中文进度与下一步操作提示；支持通过 `QUICK_ACP_MAX_TOOL_ROUNDS` 调整额度。
8. **会话恢复与历史连续性**：`loadSession` 会在本地持久化历史记录的基础上恢复原上游线程；在续接或分叉 (`session/fork`) 后的首个提问中，会自动将父历史摘要注入给模型，确保模型在上游会话跨会话恢复时保持记忆连续。
9. **生命周期与 MCP 隔离**：单轮对话取消 (`session/cancel`) 仅中断当前轮次推理与本地工具，**绝不关闭 MCP 服务**；仅在会话彻底销毁时清理 stdio 进程树或发送 HTTP DELETE 请求。
10. **用户提问能力边界**：`ask_user_question` 底层映射为 ACP `requestPermission` 单选按钮，**仅支持单选按钮，不支持多选框或自由文本表单**。

---

## 开发与测试

- **全套离线测试**：`npm test`
  - 自动化运行 `build`、`probe`、`smoke`、`test:regression`（19 项核心回归、9 项路由专项、5 项根因专项）、`test:integration`（11 步）与 `test:budget`（8 项预算专项 + 2 项边界回归）。
  - 纯离线运行，无需用户凭据或外网连接，适用于本地快速校验与 CI 流程。
- **离线协议集成测试**：`node scripts/acp-offline-integration.mjs`
  - 启动真实 `dist/main.js` 子进程并通过 stdio 进行完整 ACP JSON-RPC 交互，内建 Mock Upstream Gateway，验证全流程协议闭环。
- **在线端到端验收**：`npm run test:live`
  - 通过本地 `dist/main.js` 启动真实 ACP stdio 会话，由在线 Quick Claude 模型自主读取代码、生成报告、执行测试并回读。
  - 需有效登录凭据、网络、Python 3.10及以上和 pygame。先运行 `python -m pip install -r examples/snake/requirements.txt`。
- **打包校验**：`npm pack --dry-run`
  - 验证发布包清单文件与 package.json / lockfile 保持一致。

---

## 贡献

欢迎提交 issue 与 PR。开始前请阅读：

- [贡献指南](CONTRIBUTING.md) —— 开发环境、测试要求、发布流程
- [行为准则](CODE_OF_CONDUCT.md)
- [安全策略](SECURITY.md) —— 安全问题请走私密渠道，不要开公开 issue

适合首次参与的方向：补 Zed 等未实测客户端的接入记录、补 MCP 外部服务联调用例、补 macOS 实机验证。

---

## 免责声明

- 本项目为**非官方**第三方工具，与亚马逊 AWS、AWS Quick (Quickwork) 官方无任何关联、未获其背书或授权。
- 你的对话内容会经由本项目提供的凭据发往 AWS Quick 服务，受其条款与隐私政策约束。本仓库不对上游服务的行为作任何保证。
- 使用本项目可能与你所在组织或 AWS Quick 的服务条款存在冲突（例如以非官方客户端访问额度）。**使用前请自行确认合规性，风险自负。**
- 本项目按「现状」提供，不附带任何明示或暗示的担保。因使用本项目造成的任何直接或间接损失，作者与贡献者不承担责任。
- 模型生成的命令与文件改动由模型判断产生，请自行复核后再执行不可逆操作。

---

## 致谢

特别鸣谢 **[LINUX DO](https://linux.do/)** 社区及其热心佬友们的支持与启发！

*Special thanks to the **[LINUX DO](https://linux.do/)** community for inspiration and support!*

同作者的其他项目：

- **[LocalTimeTzClock](https://github.com/ana52070/LocalTimeTzClock)** —— 为 Windows 11 原生任务栏时钟显示任意自定义时区，保持系统全局时区与时间戳不受影响。发布包仅 38 KB，Explorer 内常驻 36 KB。

---

## 许可证

本项目采用 [MIT 许可证](LICENSE)。

Copyright (c) 2026 quick-acp contributors

第三方依赖的许可证与署名见 [NOTICE](NOTICE)。
