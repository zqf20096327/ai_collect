# IM CLI Bridge

### 用任意 IM 远程操控 AI 编程工具 -- 随时随地 Vibe Coding

**6 大 IM 平台 | 6 大 CLI 工具 | 完全免费开源**

[![GitHub stars](https://img.shields.io/github/stars/tmwgsicp/im-cli-bridge?style=for-the-badge&logo=github)](https://github.com/tmwgsicp/im-cli-bridge/stargazers)
[![License](https://img.shields.io/badge/License-AGPL%203.0-blue?style=for-the-badge)](LICENSE)
[![Node.js](https://img.shields.io/badge/Node.js-22+-339933?style=for-the-badge&logo=node.js&logoColor=white)](https://nodejs.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=for-the-badge)](https://github.com/tmwgsicp/im-cli-bridge)

[English](README.en.md) | 中文

---

## 这是什么?

这是一个 **IM-CLI 桥接器**，连接任意即时通讯平台和各种 AI 编程工具，让你在手机上远程操控电脑/服务器上的 CLI。

### 核心架构

```
IM 平台 (微信/Telegram/Discord/飞书/Slack/企业微信)
    |  桥接器 (本项目)
Claude Code / Codex / Cursor / Gemini / Kiro CLI (服务器/电脑)
```

**本质**:
- 这是一个桥接器 -- 连接 IM 和 CLI 工具的中间层
- CLI 跑在服务器 -- Claude、Cursor 等工具在你的服务器/电脑上运行
- IM 发指令 -- 在手机上发消息，远程操控 CLI
- 实时交互 -- 指令发送，结果返回，就像本地操作一样

**不是什么**:
- 不是 AI 本身 -- AI 能力来自 Claude、Codex 等官方 CLI 工具
- 不是 API 封装 -- 直接调用官方 CLI，保持原生体验
- 不是网页版 -- 运行在你自己的服务器，完全私有化

---

## 支持的 IM 平台

| 平台 | 消息接收方式 | 需要公网 IP | 状态 |
|------|------------|-----------|------|
| **微信 (WeChat)** | 本地轮询 (iLink Bot API) | 否 | 稳定 |
| **Telegram** | Long Polling | 否 | 稳定 |
| **Discord** | WebSocket Gateway | 否 | 稳定 |
| **飞书 (Feishu/Lark)** | WebSocket 长连接 / Webhook | 仅 Webhook 模式 | 稳定 |
| **Slack** | Socket Mode WebSocket | 否 | 稳定 |
| **企业微信 (WeCom)** | WebSocket 长连接 / Webhook | 仅 Webhook 模式 | 稳定 |

> 所有平台默认使用不需要公网 IP 的连接方式。飞书和企业微信可通过环境变量切换到 Webhook 模式。

## 支持的 CLI 工具

| CLI 工具 | 状态 | 说明 |
|---------|------|------|
| **Claude Code** | 稳定 | Anthropic 官方，推理能力强 |
| **OpenAI Codex** | 稳定 | GPT-5.3，每个 ChatGPT 计划都包含 |
| **Cursor CLI** | 稳定 | 独立 CLI 工具，无需 IDE |
| **Gemini CLI** | 稳定 | Google 官方，免费额度大 |
| **Kiro CLI** | 稳定 | AWS 官方，Claude 模型 (Win 需 WSL) |
| **Qwen Code** | 稳定 | 通义千问，国产模型 |

---

## 快速开始

### 1. 准备环境

- **Node.js 22+** ([下载](https://nodejs.org/))
- **一个 AI CLI** (Claude/Codex/Cursor/Gemini/Kiro 任选其一，需提前安装并登录)

### 2. 部署桥接器

```bash
# 克隆项目
git clone https://github.com/tmwgsicp/im-cli-bridge.git
cd im-cli-bridge

# 安装依赖
npm install

# 复制并编辑配置
cp .env.example .env
```

### 3. 配置 IM 平台

编辑 `.env`，设置你要使用的 IM 平台：

```bash
# 选择平台: weixin, telegram, discord, feishu, slack, wecom
PLATFORM=telegram

# 选择 CLI: claude, codex, cursor, gemini, kiro, qwen
CLI_TYPE=claude
```

然后填入对应平台的凭证 (详见 [平台创建指南](PLATFORM_SETUP_GUIDE.md) 和 [.env.example](.env.example)):

#### Telegram

```bash
TELEGRAM_BOT_TOKEN=123456:ABC-DEF...    # 从 @BotFather 获取
```

#### Discord

```bash
DISCORD_BOT_TOKEN=your_bot_token        # Discord Developer Portal
# 需要启用 MESSAGE CONTENT INTENT
```

#### 飞书

```bash
FEISHU_APP_ID=cli_xxxxx                 # 飞书开放平台
FEISHU_APP_SECRET=xxxxx
FEISHU_MODE=ws                          # ws (无需公网IP) | webhook
```

#### Slack

```bash
SLACK_BOT_TOKEN=xoxb-xxx                # Slack API
SLACK_APP_TOKEN=xapp-xxx                # 需启用 Socket Mode
```

#### 企业微信

```bash
WECOM_CORP_ID=ww_xxxxx                  # 企业微信管理后台
WECOM_CORP_SECRET=xxxxx
WECOM_AGENT_ID=1000002
WECOM_MODE=ws                           # ws (无需公网IP) | webhook
```

#### 微信

无需额外配置，启动后扫码登录。

### 4. 启动

```bash
node src/index.mjs
```

微信平台首次启动需要扫码登录，其他平台通过 Token 自动连接。

> **媒体能力自动安装**: 启动时自动将媒体发送规则 (语音/图片/文件) 安装到所有 CLI 的 rules 目录 (`~/.claude/rules/im-media.md` 等)。无需手动操作，rules 在所有模式下生效（含 -p headless 模式）。如需手动安装: `node scripts/install-rules.mjs`

### 5. (可选) 扩展功能

```bash
# 图片生成 + 语音合成 (共用一个 API Key)
MINIMAX_API_KEY=sk-xxx

# CLI 工作目录
CLAUDE_WORKDIR=/path/to/your/project
```

---

## 使用示例

### 远程写代码

```
你 (手机): 帮我写个 Python 爬虫，爬取豆瓣电影 Top250

Claude Code (服务器):
已保存到 douban_spider.py
```

### 随时切换 CLI

```
你: /cli cursor
切换到 Cursor

你: /cli claude
切换到 Claude
```

### 定时任务

```
你: 每天早上8点提醒我看日报

桥接器: [Scheduled Task Created]
ID: #task_abc1
Type: Reminder
Cron: 0 8 * * *

你: 每周一上午10点分析上周代码提交

桥接器: [Scheduled Task Created]
ID: #task_def2
Type: AI
CLI: CLAUDE
```

### 异步长任务

```
你: 分析整个项目的代码质量，给出改进建议

桥接器: [Task Accepted] Running in background
Type: 代码分析
Estimated: 5-10 min

(你可以继续其他操作，完成后自动通知)
```

---

## 常用命令

在 IM 中发送:

```
/help              # 查看所有命令
/cli               # 查看/切换 CLI 工具
/status            # 查看当前状态
/model             # 查看/切换模型
/reset             # 重新开始对话
/sessions          # 查看所有对话
/context           # 查看/注入上下文摘要
/task              # 查看异步任务
/schedule list     # 查看定时任务
/persona list      # 查看可用人设
/persona set coder # 切换人设
```

---

## 核心功能

### 多平台支持

一套代码支持 6 个 IM 平台。通过 `PLATFORM` 环境变量切换，零代码改动。

### 多 CLI 热切换

运行时通过 `/cli <name>` 切换 CLI 工具，每个用户独立会话。

### 跨 CLI 上下文管理

切换 CLI 时自动总结历史对话并持久化。按需注入,不浪费 tokens:

```
/context          # 查看上下文摘要
/context inject   # 注入摘要到下一条消息
/context refresh  # 重新生成摘要
/context clear    # 清除摘要
```

### 异步任务

自动检测长任务 (代码分析、重构等)，在后台执行，完成后推送结果。

### 定时任务

支持自然语言创建定时任务:
- **提醒任务**: "每天8点提醒我站会"
- **AI 任务**: "每周一分析上周代码提交"
- **一次性任务**: "30秒后提醒我休息"

### Session Guard

检测 Token 失效，自动暂停 1 小时避免触发风控，到期自动恢复。

### 人设/伴侣系统

内置 4 种人设 (coder / companion / mentor / supervisor)，支持自定义。通过 CLI rules 机制注入，所有模式（含 -p headless）都生效。

```
/persona list              # 查看可用人设
/persona set companion     # 激活伴侣模式
/persona off               # 关闭人设
/persona create id|name|prompt  # 创建自定义人设
```

### Markdown 渲染

代码块、加粗、链接等格式在各平台正确渲染:
- Telegram: Markdown 模式
- 飞书: Interactive Card
- Slack: mrkdwn 格式
- Discord: 原生 Markdown
- 企业微信: Markdown 消息类型

### 危险操作确认

桥接层自动检测 AI 提出的高危操作 (rm -rf, DROP TABLE, format 等)，拦截并要求用户确认后才执行。

### 多模态

- 图片识别 -- 发截图，CLI 分析调试
- 文件处理 -- 发代码/日志，CLI 分析
- 文件发送 -- CLI 可通过 `发送文件: 路径` 格式发送本地文件到 IM
- 语音合成 -- CLI 可语音回复 (需配置 MiniMax)
- 图片生成 -- CLI 可生成图片 (需配置 MiniMax)

### 多实例隔离

通过 `INSTANCE_ID` 环境变量支持同一台机器运行多个实例，数据完全隔离:

---

## 生产部署 (PM2)

### 安装 PM2

```bash
npm install -g pm2
```

### 单平台部署

```bash
# 1. 配置 .env (填入平台 token)
cp .env.example .env

# 2. 启动
pm2 start src/index.mjs --name im-bridge --node-args="--no-deprecation"

# 3. 常用命令
pm2 logs im-bridge       # 查看日志
pm2 restart im-bridge    # 重启
pm2 stop im-bridge       # 停止

# 4. 开机自启
pm2 startup
pm2 save
```

### 多平台同时部署 (一台机器跑多个平台)

每个平台启动一个独立进程，用不同的 `--platform` 和 `--name`:

```bash
# 先在 .env 里填好各平台的 token，然后:

# 启动 Telegram
pm2 start src/index.mjs --name im-telegram --node-args="--no-deprecation" -- --platform=telegram

# 启动飞书
pm2 start src/index.mjs --name im-feishu --node-args="--no-deprecation" -- --platform=feishu

# 启动 Slack
pm2 start src/index.mjs --name im-slack --node-args="--no-deprecation" -- --platform=slack

# 启动微信
pm2 start src/index.mjs --name im-weixin --node-args="--no-deprecation" -- --platform=weixin

# 查看所有实例状态
pm2 status
```

### 同平台多 Bot 部署

同一个平台跑多个 bot (比如两个 Telegram bot):

```bash
# Bot 1
TELEGRAM_BOT_TOKEN=token_1 pm2 start src/index.mjs \
  --name im-tg-bot1 --node-args="--no-deprecation" \
  -- --platform=telegram --instance=tg-bot1

# Bot 2
TELEGRAM_BOT_TOKEN=token_2 pm2 start src/index.mjs \
  --name im-tg-bot2 --node-args="--no-deprecation" \
  -- --platform=telegram --instance=tg-bot2
```

> 关键: 不同 bot 用不同的 `--instance` 隔离数据，不同的环境变量传入 token。

### 声明式部署 (ecosystem.config.cjs)

也可以编辑 `ecosystem.config.cjs`，取消注释需要的平台，然后一键启动:

```bash
pm2 start ecosystem.config.cjs    # 启动所有配置的平台
pm2 status                        # 查看状态
```

---

## 项目结构

```
src/
  index.mjs              # 主入口
  config.mjs             # 配置中心
  platforms/             # IM 平台适配器
    base-platform.mjs    # 平台抽象基类
    index.mjs            # 平台工厂
    weixin/              # 微信
    telegram/            # Telegram
    discord/             # Discord
    feishu/              # 飞书
    slack/               # Slack
    wecom/               # 企业微信
  core/                  # 核心逻辑
    commands.mjs         # 命令处理
    cli-manager.mjs      # CLI 管理 (懒加载)
    message-queue.mjs    # 消息队列
    types.mjs            # 统一消息类型
  cli/                   # CLI 适配器
    claude.mjs
    codex.mjs
    cursor.mjs
    gemini.mjs
    kiro.mjs
    qwen.mjs
  utils/                 # 工具模块
    task-scheduler.mjs   # 定时任务调度
    task-parser.mjs      # 自然语言任务解析
    task-detector.mjs    # 长任务检测
    async-task-manager.mjs # 异步任务管理
    session-guard.mjs    # Session 保护
    logger.mjs
```

---

## 常见问题

### 1. 支持哪些系统?
- Windows 10/11/Server 2016+
- Linux (Ubuntu 18.04+, Debian 10+)
- macOS 10.15+ (Intel/Apple Silicon)

### 2. 需要公网 IP 吗?
默认不需要。所有平台默认使用不需要公网 IP 的连接方式。飞书和企业微信的 Webhook 模式需要公网 IP，但它们默认使用 WebSocket 模式。

### 3. 安全吗?
- 代码全开源，可自行审查
- 运行在你自己的服务器
- 各平台使用官方 API

### 4. 微信会封号吗?
使用官方 iLink Bot API，协议合规。内置 Session Guard 自动防风控。

### 5. 可以同时接多个平台吗?
可以。每个平台启动一个实例，通过 `INSTANCE_ID` 隔离数据。

---

## 后续计划

### v1.3.1 (当前)
- 6 IM + 6 CLI 全平台验证
- 人设/伴侣系统
- Markdown 渲染 (Telegram/飞书/Slack/Discord/WeCom)
- 危险操作确认
- 媒体 Rules 自动安装 (取代 Skills，-p 模式兼容)
- 飞书 64-bit varint 修复、事件去重
- 跨 CLI 上下文管理 (/context 按需查看/注入历史摘要)

### v1.4 (2026 Q3)
- Streaming 流式预览 (stream-json 模式)
- 多 Agent 协作 (多 CLI 并行处理)
- Web 管理面板

---

## 各平台双向收发能力

> 与同类项目的核心区别: im-cli-bridge 不仅能接收用户消息，**还能主动向用户发送文件、图片、语音、视频**。CLI 生成的代码文件、截图、语音回复都能直接推送到 IM。

### 接收能力 (用户 -> Bot)

| 类型 | 微信 | Telegram | Discord | 飞书 | Slack | 企业微信 |
|------|------|----------|---------|------|-------|----------|
| 文字 | O | O | O | O | O | O |
| 图片 | O | O | O | O | O | O |
| 语音 | O (ASR) | O (OGG) | O | O | O | O (ASR) |
| 视频 | O | O | O | O | O | O |
| 文件 | O | O | O | O | O | O |

### 发送能力 (Bot -> 用户)

| 类型 | 微信 | Telegram | Discord | 飞书 | Slack | 企业微信 |
|------|------|----------|---------|------|-------|----------|
| 文字 | O | O | O | O | O | O |
| Markdown | - | O | O | O (Card) | O (mrkdwn) | O |
| 图片 | O | O | O | O | O | O |
| 语音 | O* | O (OGG) | O* | O* | O* | O (AMR) |
| 视频 | O | O | O* | O* | O* | O |
| 文件 | O | O | O | O | O | O |
| TTS 合成 | O | O | O | O | O | O |
| 图片生成 | O | O | O | O | O | O |
| Typing | O | O | O | O** | O** | - |

> O = 原生支持, O* = 以文件附件形式发送, O** = 模拟提示 ("Thinking..."), - = 平台不支持

### 典型场景

- **发截图给 Bot** -> CLI 识别并分析代码/报错 (全平台)
- **Bot 发送生成的代码文件** -> 直接在 IM 里下载 (全平台)
- **Bot 语音回复** -> 配合 TTS 实现语音交互 (全平台)
- **Bot 发送图片** -> AI 生成的图表/图片直接推送 (全平台)

> 各平台 Bot 创建和配置的详细步骤请参考 [平台创建指南](PLATFORM_SETUP_GUIDE.md)。

## 核心特性

- **6 IM x 6 CLI** -- 任意组合，一套代码
- **CLI 热切换** -- `/cli codex` 一句话切换，会话独立保留，上下文按需同步
- **人设/伴侣** -- 4 种内置人设 + 自定义创建，跨 CLI 生效
- **异步长任务** -- 自动检测，后台执行，完成推送，不阻塞日常对话
- **定时任务** -- 自然语言 + AI 智能解析，支持中文数字
- **危险操作确认** -- 桥接层拦截 rm -rf / DROP TABLE 等高危操作
- **Session Guard** -- 自动检测 Token 失效，暂停防风控，到期恢复
- **消息队列** -- 每用户独立串行，不丢消息不打断
- **多实例隔离** -- PM2 多实例，数据完全隔离
- **图片生成 + TTS** -- MiniMax 内置，CLI 直接输出到 IM

---

## 开源协议

本项目采用 **AGPL 3.0** 协议开源，**所有功能代码完整公开，私有化部署完全免费**。

| 使用场景 | 是否允许 |
|---------|---------|
| 个人学习和研究 | 允许，免费使用 |
| 企业内部使用 | 允许，免费使用 |
| 私有化部署 | 允许，免费使用 |
| 修改后对外提供网络服务 | 需开源修改后的代码 |

详见 [LICENSE](LICENSE) 文件。

### 免责声明

- 本项目仅供学习和研究使用
- 使用各 IM 平台 API 需遵守其官方服务条款
- 使用各 CLI 工具需遵守其官方许可协议
- 开发者不对使用本项目产生的任何后果负责

---

## 参与贡献

欢迎参与:

- **提交 Issue** -- 报告 Bug、提出功能建议
- **Pull Request** -- 欢迎提交 PR
- **Fork 项目** -- 自由修改和定制
- **Star 支持** -- 给项目点 Star，让更多人看到

---

## 联系方式

<table>
  <tr>
    <td align="center">
      <img src="assets/qrcode/wechat.jpg" width="200"><br>
      <b>个人微信</b><br>
      <em>技术交流 / 商务合作</em>
    </td>
    <td align="center">
      <img src="assets/qrcode/sponsor.jpg" width="200"><br>
      <b>赞赏支持</b><br>
      <em>开源不易，感谢支持</em>
    </td>
  </tr>
</table>

---

<div align="center">

**如果这个项目对你有帮助，请点一个 Star，让更多人发现它**

[![Star History Chart](https://api.star-history.com/svg?repos=tmwgsicp/im-cli-bridge&type=Date)](https://star-history.com/#tmwgsicp/im-cli-bridge&Date)

Made by [tmwgsicp](https://github.com/tmwgsicp)

</div>
