<div align="center">
  <img src="./docs/assets/icon-180.png" width="76" height="76" alt="dsh-lark-bridge" />
  <h1>dsh-lark-bridge</h1>
  <p><strong>把 Claude Code / Codex / TRAE / DeepSeek Harness 接进飞书群：<br/>零公网暴露 · 懂分寸不刷屏 · 会记事与夜间复盘 · 能主动委派跟进</strong></p>
  <p>
    <a href="https://github.com/harryzhz/dsh-lark-bridge/releases/latest"><img src="https://img.shields.io/github/v/release/harryzhz/dsh-lark-bridge?style=flat-square&color=0ea5e9" alt="Latest Release" /></a>
    <a href="./LICENSE"><img src="https://img.shields.io/github/license/harryzhz/dsh-lark-bridge?style=flat-square&color=10b981" alt="License: MIT" /></a>
    <a href="https://github.com/harryzhz/dsh-lark-bridge/stargazers"><img src="https://img.shields.io/github/stars/harryzhz/dsh-lark-bridge?style=flat-square&color=f59e0b" alt="GitHub Stars" /></a>
    <img src="https://img.shields.io/badge/Platform-macOS%20%7C%20Windows%20%7C%20Linux-64748b?style=flat-square" alt="Platform" />
  </p>
  <p>
    <strong>简体中文</strong> · <a href="./README_EN.md">English</a>
  </p>
  <p>
    <a href="#产品亮点">产品亮点</a> ·
    <a href="#产品演示">产品演示</a> ·
    <a href="#一键安装3-分钟跑起来">3 分钟安装</a> ·
    <a href="#典型场景">典型场景</a> ·
    <a href="./docs/README.md">文档导航</a>
  </p>
</div>

> 基于 [DeepSeek Harness (DSH)](https://github.com/deepseek-ai/deepseek-harness)（Desktop & Web）构建，受 [dsh-superagent](https://github.com/deepseek-ai/dsh-superagent-prototype) 与 [botmux](https://github.com/deepcoldy/botmux) 启发。默认使用 DSH 原生预设与模型；一键安装脚本已配套 [dsh-external-agents](https://github.com/harryzhz/dsh-external-agents)，开箱接入 **Claude Code、Codex、Antigravity、TRAE CLI** 等外部 Coding Agent，MIT 协议开源。

---

## 产品亮点

1. **零公网暴露，扫码 3 分钟跑起来**
   基于飞书官方 WebSocket 长连接，无需云服务器、公网域名或内网穿透。一行命令装齐环境，控制台扫码自动创建飞书应用、配齐权限并拉起长连接，拉进群自动启用并打招呼。
2. **多引擎无侵入，一个群一套配置**
   默认直接使用 DSH 原生预设与模型；搭配 [dsh-external-agents](https://github.com/harryzhz/dsh-external-agents) 开箱支持 **Claude Code / Codex / Antigravity / TRAE CLI**。研发群、告警群、发布群可各自绑定代码仓库、运行时、模型与并发上限，支持 AI 一键生成定制角色和监听规则。
3. **懂分寸、不刷屏的智能分流与主动监听**
   轻量前置**智能分流** + **逐成员/应用主动监听开关**：同事日常沟通彻底静默；线上告警卡片一到秒开话题查本地代码库，按「止损 → 根因 → 后续行动」回复。支持**飞书原生思考过程气泡**与卡片底部一键跳回 DSH 接管同一会话，话题内追问免 `@`。
4. **越用越懂团队的跨运行时长期记忆 + Auto-Dream**
   不依赖单一 Agent 的私有文件，统一沉淀在 SQLite + FTS5 混合检索引擎与 Obsidian 风格**关系图谱**中，按全局 / 工作区 / 群聊三级隔离防串味。每晚 **Auto-Dream** 自动低优先级复盘增量对话、对照最新代码验真并双时态纠偏过时规则。
5. **说到做到的主动提醒、委派跟进与隔离修补**
   静默识别群内 `A @ B` 的明确指派与承诺，到期先核查群历史/MR/CI 真实状态——**已闭环静默归档，未闭环才精准 `@负责人 cc 发起人`**，夜间免打扰自动顺延至白天。开启主动代码优化后，可在 `.worktrees/` 隔离分支改代码、跑单测并提审 PR/MR，绝不污染主工作分支。
6. **生产级驾驶舱可观测 + 免重启热更新**
   内置**驾驶舱（概览 / 洞察 / 监控）**看清消息吞吐、Token 结构与缓存命中率、分流减负漏斗、P50/P95 延迟与 SQLite WAL 健康度；Web 版支持从 GitHub Release **一键原地免重启热更新**，不打断在途长任务。

---

## 产品演示

<div align="center">
  <a href="https://drive.google.com/file/d/1pjdbF6pjJ9ZZGqx8MDeb8X0NV1D_XMmo/view?usp=drive_link">
    <img src="./docs/assets/demo-cover-v5.png" alt="点击观看 dsh-lark-bridge v5 产品实景演示视频" />
  </a>
  <p>
    ▶️ <a href="https://drive.google.com/file/d/1pjdbF6pjJ9ZZGqx8MDeb8X0NV1D_XMmo/view?usp=drive_link"><strong>点击在线观看完整产品演示视频（v5 · 1080p · 2 分 33 秒）</strong></a>
  </p>
  <p><sub>涵盖：扫码一键建智能体 · 群内 <code>@</code> 排障与 DSH 接管 · 告警群免 <code>@</code> 主动值守 · 定时巡检图文卡片 · <code>A @ B</code> 委派跟进与夜间盘点 · 长期记忆关系图谱 · 驾驶舱可观测视图</sub></p>
</div>

<table>
  <tr>
    <td width="50%">
      <img src="./docs/assets/feishu-alert-triage.png" alt="告警群免 @ 主动值守" />
      <p align="center"><sub><strong>零打扰主动监听</strong>：同事闲聊静默跳过，P1 告警秒开话题给止损与根因</sub></p>
    </td>
    <td width="50%">
      <img src="./docs/assets/feishu-reminder-nudge.png" alt="Auto-Dream 夜间盘点与精准催办" />
      <p align="center"><sub><strong>委派跟进与夜间盘点</strong>：核查真实进展，未闭环承诺白天精准 <code>@负责人 cc 发起人</code></sub></p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <img src="./docs/assets/memory-graph.png" alt="长期记忆关系图谱" />
      <p align="center"><sub><strong>记忆库 · 关系图谱</strong>：跨运行时团队记忆成网，支持演进生长回放</sub></p>
    </td>
    <td width="50%">
      <img src="./docs/assets/cockpit-overview.png" alt="驾驶舱概览" />
      <p align="center"><sub><strong>驾驶舱 · 概览 / 洞察 / 监控</strong>：一屏掌握吞吐、Token 缓存、分流减负与 SLA</sub></p>
    </td>
  </tr>
</table>

---

## 一键安装（3 分钟跑起来）

支持 macOS / Windows / Linux，一行命令自动检测环境并装好 **DSH + `dsh-lark-bridge` + `dsh-external-agents`**（已装兼容版本直接复用，不改已有凭据与配置）：

#### macOS / Linux

```bash
# 交互模式：自动选择 Desktop App / 独立 Web 服务 / 两版都装（Linux 自动选 Web）
curl -fsSL https://raw.githubusercontent.com/harryzhz/dsh-lark-bridge/main/scripts/install.sh | bash

# 直接指定模式（非交互可追加 -y）
curl -fsSL https://raw.githubusercontent.com/harryzhz/dsh-lark-bridge/main/scripts/install.sh | bash -s -- --mode app
curl -fsSL https://raw.githubusercontent.com/harryzhz/dsh-lark-bridge/main/scripts/install.sh | bash -s -- --mode web
```

#### Windows (PowerShell)

```powershell
# 交互模式
irm https://raw.githubusercontent.com/harryzhz/dsh-lark-bridge/main/scripts/install.ps1 | iex

# 直接指定模式（app / web / both）
$env:DSH_INSTALL_MODE = 'app'; irm https://raw.githubusercontent.com/harryzhz/dsh-lark-bridge/main/scripts/install.ps1 | iex
```

### 扫码接入只需 3 步

1. **打开控制台**：Desktop 版启用插件后点击左侧 **飞书桥接**；独立 Web 版运行 `dsh web`（或 `dsh --profile web --no-open --port 3880` 后台常驻）。
2. **扫码一键建机器人**：点右上角 **飞书认证** 扫码登录开放平台 → **智能体 → 新增智能体**，填名字、本地工作目录与运行时（DSH / Claude Code / Codex / TRAE），扫码自动创建应用、配齐权限并拉起长连接（也支持接入已有应用）。
3. **拉进群直接用**：在飞书里把智能体拉进群，自动启用并打招呼（或到 **群聊** 页精细配置角色设定、分流与主动监听规则）。

<details>
<summary>展开查看：安装模式对比、脚本可选参数、手动安装（界面 / <code>dsh plugin</code> CLI）与免重启热更新</summary>

#### 前置要求与安装模式

- 前置环境：`DeepSeek Harness >= 0.2.2-rc.5`（Desktop App 内置运行时无需预装 Node；独立 Web 版需 `Node.js >= 22.13.0`）。

| 安装模式 | 适用场景 | 支持平台 | 安装内容 |
| --- | --- | --- | --- |
| **Desktop App 版**（`--mode app`） | 个人桌面日常使用，开箱即用 | macOS / Windows | 自动安装官方 Desktop 客户端并激活双插件 |
| **Web 版**（`--mode web`） | 局域网 / 服务器后台常驻、免重启热更新 | macOS / Linux / Windows | 自动准备 Node 22 + pnpm + `@deepseek-ai/dsh`（免 sudo），向 `web` profile 安装双插件并默认绑定局域网 IPv4 |
| **两版都装**（`--mode both`） | 同时使用桌面端与独立 Web 服务 | macOS / Windows | 依次完成两套环境安装与激活 |

#### 一键脚本常用可选参数

| 参数（`install.sh` / `install.ps1`） | 环境变量 | 说明 |
| --- | --- | --- |
| `--mode <auto\|web\|app\|both>` / `-Mode` | `DSH_INSTALL_MODE` | 指定安装模式（`install.sh` 亦支持 `--web` / `--app` / `--both`） |
| `--web-host <auto\|loopback\|IP>` / `-WebHost` | `DSH_WEB_HOST` | Web 版默认监听地址：默认 `auto`（自动绑定局域网 IPv4，离线回退 `127.0.0.1`） |
| `--without-external-agents` / `-WithoutExternalAgents` | `DSH_WITHOUT_EXTERNAL_AGENTS=1` | 仅安装 `dsh-lark-bridge`，不安装 `dsh-external-agents` |
| `--upgrade-dsh` / `-UpgradeDsh` | `DSH_UPGRADE=1` | 即使已存在兼容版 DSH，也升级到最新版 |
| `--force` / `-Force` | `DSH_FORCE=1` | 强制重新安装目标版本插件 |
| `--github-proxy <url>` / `-GithubProxy` | `GITHUB_PROXY` | 为 GitHub Release 下载添加镜像前缀 |
| `--dry-run` / `-DryRun` | `DSH_DRY_RUN=1` | 仅检测环境并打印安装计划，不做实际修改 |
| `-y, --yes` / `-Yes` | `DSH_YES=1` | 非交互模式，自动确认全部提示 |

#### 手动安装（DSH 界面 / CLI）

- **界面安装**：侧边栏 **插件 → 添加插件**，填入 Release `.tgz` 地址安装并启用：
  - `https://github.com/harryzhz/dsh-lark-bridge/releases/latest/download/dsh-lark-bridge.tgz`
  - `https://github.com/harryzhz/dsh-external-agents/releases/latest/download/dsh-external-agents.tgz`（可选）
- **CLI 安装（Web Profile）**：
  ```bash
  dsh plugin --profile web add \
    https://github.com/harryzhz/dsh-external-agents/releases/latest/download/dsh-external-agents.tgz \
    https://github.com/harryzhz/dsh-lark-bridge/releases/latest/download/dsh-lark-bridge.tgz
  ```
- **日常升级（免重启热更新）**：点击控制台右上角版本徽标或执行 `lark-bridge plugin update` 原地热更新；仅升级 DSH 本体确需重启时先执行 `lark-bridge lifecycle drain --wait` 排空在途回合。

</details>

---

## 典型场景

| 场景 | 推荐配置 | 实际效果 |
| --- | --- | --- |
| **研发群驻群搭档** | 群绑定服务仓库；开启话题内回复、按话题复用与原生思考气泡 | `@Bot` 查提交、定位根因、改代码跑单测并收进话题；同话题免 `@` 追问，点卡片一键回 DSH 接管。 |
| **告警群自动值班** | 「主动监听」选 **告警排查** 模板（或 AI 一键生成），仅监听告警应用 | 同事日常沟通零打扰；P0/P1 告警卡片一到秒开话题给止损、根因与核查命令。 |
| **群内委派防遗漏** | 开启 **主动创建提醒 + 委派事项跟进 + 夜间免打扰** | 同事间 `A @ B` 认领的任务自动静默跟进；到期查真实进展，已闭环静默归档，未闭环精准 `@` 提醒。 |
| **团队知识越用越准** | 开启 **Dreaming 与长期记忆**，在 **记忆库** 置顶核心规范 | 群内一句话「记住…」即刻生效；每晚 Auto-Dream 复盘验真并纠偏过时经验，新老会话风格一致。 |
| **每日巡检静默播报** | 「自动化 → 定时任务」绑定目标群，推送时机选 **有内容或异常时** | 一切正常零消息打扰；发现阻塞 MR 或指标异常自动发图文卡片并精准 `@` 处理人。 |
| **负责人繁忙期代答** | 「权限与代答」添加目标负责人并开启话题续跟 | 群内 `@负责人` 问代码或接口细节时，智能体先查证作答并承接追问，高风险决策留给本人确认。 |

---

## 文档导航与开发

完整架构设计、路由机制、记忆系统、CLI 手册与开发规范见 **[docs/README.md](./docs/README.md)**（[系统架构](./docs/architecture/overview.md) · [会话与路由](./docs/architecture/session-management.md) · [长期记忆与 Auto-Dream](./docs/architecture/memory-and-dreaming.md) · [安全策略](./SECURITY.md)）。

```bash
pnpm install
pnpm build && pnpm typecheck && pnpm test && pnpm run check:privacy
```

## License

[MIT](./LICENSE)
