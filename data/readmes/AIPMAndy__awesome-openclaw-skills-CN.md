<div align="center">
    <strong>🇨🇳 发现 2868 个社区构建的 OpenClaw Skills，按分类整理，面向中文开发者友好阅读。</strong>
    <br />
    <br />

[![Skills Count](https://img.shields.io/badge/skills-2869-blue?style=flat-square)](#table-of-contents)
[![Last Update](https://img.shields.io/github/last-commit/AIPMAndy/awesome-openclaw-skills-CN?label=Last%20update&style=flat-square)](https://github.com/AIPMAndy/awesome-openclaw-skills-CN/pulls?q=is%3Apr+is%3Amerged+sort%3Aupdated-desc)
[![GitHub forks](https://img.shields.io/github/forks/AIPMAndy/awesome-openclaw-skills-CN?style=social)](https://github.com/AIPMAndy/awesome-openclaw-skills-CN/network/members)
</div>

# Awesome OpenClaw Skills CN

## 👋 关于本项目

**我是 Andy**，前腾讯/百度 AI 产品专家，现专注于 AI 商业战略顾问与 AI Agent 生态研究。

做这个中文化项目的初衷：
- **降低门槛**：让中文开发者无需翻墙、无需啃英文文档，快速上手 OpenClaw
- **本土适配**：整理国产模型接入指南、推荐适合国内开发者的 Skills
- **社区共建**：希望更多中文开发者参与 AI Agent 生态建设

📖 **特色内容：**
- [🇨🇳 国产大模型接入指南](./CHINESE-MODELS.md) — DeepSeek / 通义千问 / GLM / Moonshot / 豆包
- [🇨🇳 中文开发者推荐 Skills](./CHINESE-SKILLS.md) — 飞书 / 企业微信 / 小红书 / 知乎 / B站

📬 **联系我：** 微信 `AIPMAndy`（备注：OpenClaw）

---

> 本项目基于 [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) 翻译制作，原项目采用 MIT 开源协议。

## 什么是 OpenClaw？

OpenClaw（曾用名 Moltbot / Clawdbot）是一个运行在本地机器上的 AI 助手。Skill 可以扩展它的能力，让它连接外部服务、自动化工作流并执行专用任务。

技能数据来源于 [ClawHub](https://www.clawhub.ai/)（OpenClaw 官方公开技能注册表），并按照分类整理。

> 说明：为保证与上游同步，技能条目名称与描述大多保留原文；你可以直接用浏览器翻译或让 AI 助手做二次解释。

## 安装

### ClawHub CLI（推荐）

> 备注：OpenClaw 生态命名经常变动，以下命令以当前官方文档为准。

```bash
npx clawhub@latest install <skill-slug>
```

### 手动安装

将 skill 文件夹复制到以下任一目录：

| 位置 | 路径 |
|------|------|
| 全局 | `~/.openclaw/skills/` |
| 当前工作区 | `<project>/skills/` |

优先级：`Workspace > Local > Bundled`

### 中国开发者网络优化（可选）

如果 `npx` 速度较慢，可使用国内 npm 镜像：

```bash
npm config set registry https://registry.npmmirror.com
```

恢复官方源：

```bash
npm config set registry https://registry.npmjs.org
```

### 对话式安装（替代方式）

你也可以把 Skill 的 GitHub 链接直接发给 AI 助手，并让它“使用这个 Skill”，助手通常会在后台自动完成安装配置。

## 为什么有这个列表？

截至 **2026 年 2 月 7 日**，OpenClaw 官方公开注册表（ClawHub）包含 **5,705** 个社区技能；本列表收录 **2,868** 个。以下是过滤掉的部分：

| 过滤项 | 排除数量 |
|--------|----------|
| 疑似垃圾内容（批量账号、机器人账号、测试/垃圾条目） | 1,180 |
| Crypto / Blockchain / Finance / Trade | 672 |
| 重复或近似名称 | 492 |
| 恶意条目（来自研究者公开安全审计，不含 VirusTotal） | 396 |
| 非英文描述 | 8 |
| **未纳入本列表总计** | **2,748** |

## 安全提示

本列表是**人工整理（curated）而非安全审计（audited）**。技能在收录后仍可能被原作者更新、替换或修改。

在安装和使用任何 Skill 前，请自行评估安全风险并核验来源。OpenClaw 与 VirusTotal 有合作，你可以在 ClawHub 的技能详情页查看对应扫描结果。

**推荐工具：**

- [Snyk Skill Security Scanner](https://github.com/snyk/agent-scan)
- [Agent Trust Hub](https://ai.gendigital.com/agent-trust-hub)

> Skill 可能包含提示词注入、工具投毒、隐藏恶意载荷或不安全数据处理逻辑。生产环境使用前务必审查源码。

**想添加 Skill？** 本列表只收录已经发布到 `github.com/openclaw/skills` 的技能，不接受个人仓库、gist 或其他外部链接。请先发布到官方仓库，再按 [CONTRIBUTING.md](CONTRIBUTING.md) 提交。

如果你认为列表中的某个 Skill 存在安全问题，请在 [issues](https://github.com/AIPMAndy/awesome-openclaw-skills-CN/issues) 提交反馈。

## Table of Contents

| | | |
|---|---|---|
| [Coding Agents & IDEs](#coding-agents--ides) (133) | [Marketing & Sales](#marketing--sales) (143) | [Communication](#communication) (133) |
| [Git & GitHub](#git--github) (66) | [Productivity & Tasks](#productivity--tasks) (135) | [Speech & Transcription](#speech--transcription) (65) |
| [Moltbook](#moltbook) (51) | [AI & LLMs](#ai--llms) (287) | [Smart Home & IoT](#smart-home--iot) (56) |
| [Web & Frontend Development](#web--frontend-development) (202) | [Data & Analytics](#data--analytics) (46) | [Shopping & E-commerce](#shopping--e-commerce) (51) |
| [DevOps & Cloud](#devops--cloud) (212) | [Finance](#finance) (22) | [Calendar & Scheduling](#calendar--scheduling) (50) |
| [Browser & Automation](#browser--automation) (139) | [Media & Streaming](#media--streaming) (81) | [PDF & Documents](#pdf--documents) (67) |
| [Image & Video Generation](#image--video-generation) (60) | [Notes & PKM](#notes--pkm) (100) | [Self-Hosted & Automation](#self-hosted--automation) (25) |
| [Apple Apps & Services](#apple-apps--services) (35) | [iOS & macOS Development](#ios--macos-development) (17) | [Security & Passwords](#security--passwords) (64) |
| [Search & Research](#search--research) (253) | [Transportation](#transportation) (76) | [Gaming](#gaming) (61) |
| [Clawdbot Tools](#clawdbot-tools) (120) | [Personal Development](#personal-development) (56) | [Agent-to-Agent Protocols](#agent-to-agent-protocols) (18) |
| [CLI Utilities](#cli-utilities) (129) | [Health & Fitness](#health--fitness) (55) | |
<details open>
<summary><h3 style="display:inline">Coding Agents & IDEs</h3></summary>

- [achurch](https://github.com/openclaw/skills/tree/main/skills/lucasgeeksinthewood/achurch/SKILL.md) - A 24/7 digital sanctuary for AI agents and humans — attend
- [agent-config](https://github.com/openclaw/skills/tree/main/skills/thatguysizemore/agent-config/SKILL.md) - Intelligently modify agent core context files
- [agent-council](https://github.com/openclaw/skills/tree/main/skills/itsahedge/agent-council/SKILL.md) - Complete toolkit for creating autonomous AI agents and managing
- [agent-identity-kit](https://github.com/openclaw/skills/tree/main/skills/ryancampbell/agent-identity-kit/SKILL.md) - A portable identity system for AI agents.
- [agenticflow-skill](https://github.com/openclaw/skills/tree/main/skills/seanphan/agenticflow-skill/SKILL.md) - Comprehensive guide for building AI workflows, agents
- [agentlens](https://github.com/openclaw/skills/tree/main/skills/nguyenphutrong/agentlens/SKILL.md) - Navigate and understand codebases using agentlens hierarchical
- [agentskills-io](https://github.com/openclaw/skills/tree/main/skills/killerapp/agentskills-io/SKILL.md) - Create, validate, and publish Agent Skills following
- [aisa-twitter-api](https://github.com/openclaw/skills/tree/main/skills/aisapay/aisa-twitter-api/SKILL.md) - Search X (Twitter) in real time, extract relevant posts
- [apple-hig](https://github.com/openclaw/skills/tree/main/skills/kdbhalala/apple-hig/SKILL.md) - Expert guide for designing iOS, macOS, watchOS, tvOS, and visionOS apps.
- [arbiter](https://github.com/openclaw/skills/tree/main/skills/5hanth/arbiter/SKILL.md) - Push decisions to Arbiter Zebu for async human review.
- [aster](https://github.com/openclaw/skills/tree/main/skills/satyajiit/aster/SKILL.md) - Your AI CoPilot on Mobile — or give your AI its own phone.
- [avatar-video-messages](https://github.com/openclaw/skills/tree/main/skills/thewulf7/avatar-video-messages/SKILL.md) - Generate and send video messages
- [backend-patterns](https://github.com/openclaw/skills/tree/main/skills/charmmm718/backend-patterns/SKILL.md) - Backend architecture patterns, API design, database
- [bidclub](https://github.com/openclaw/skills/tree/main/skills/jasonfdg/bidclub/SKILL.md) - Post investment ideas to the AI-native investment community.
- [bidclub-ai](https://github.com/openclaw/skills/tree/main/skills/jasonfdg/bidclub-ai/SKILL.md) - Post investment ideas to the AI-native investment community.
- [botpress-adk](https://github.com/openclaw/skills/tree/main/skills/yueranlu/botpress-adk/SKILL.md) - A guide to build AI bots with Botpress's Agent Development Kit
- [browse](https://github.com/openclaw/skills/tree/main/skills/pkiv/browse/SKILL.md) - Complete guide for creating and deploying browser automation functions
- [budget-variance-analyzer](https://github.com/openclaw/skills/tree/main/skills/datadrivenconstruction) - Analyze budget vs actual
- [buildlog](https://github.com/openclaw/skills/tree/main/skills/espetey/buildlog/SKILL.md) - Record, export, and share your AI coding sessions as replayable buildlogs.
- [catholic-grounding](https://github.com/openclaw/skills/tree/main/skills/trevortomesh/catholic-grounding/SKILL.md) - Help answer questions about Catholicism accurately
- [cc-godmode](https://github.com/openclaw/skills/tree/main/skills/cubetribe/cc-godmode/SKILL.md) - Self-orchestrating multi-agent development workflows.
- [cellcog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/cellcog/SKILL.md) - #1 on DeepResearch Bench (Feb 2026).
- [claude-optimised](https://github.com/openclaw/skills/tree/main/skills/hexnickk/claude-optimised/SKILL.md) - Guide for writing and optimizing CLAUDE.md files
- [claude-team](https://github.com/openclaw/skills/tree/main/skills/jalehman/claude-team/SKILL.md) - Orchestrate multiple Claude Code workers via iTerm2
- [clawder](https://github.com/openclaw/skills/tree/main/skills/assassin808/clawder/SKILL.md) - Use Clawder to sync identity, browse post cards, swipe with a comment
- [code-mentor](https://github.com/openclaw/skills/tree/main/skills/samuelkahessay/code-mentor/SKILL.md) - Comprehensive AI programming tutor for all levels.
- [codebuddy-code](https://github.com/openclaw/skills/tree/main/skills/pmwalkercao/codebuddy-code/SKILL.md) - CodeBuddy Code CLI installation, configuration and usage
- [codeconductor](https://github.com/openclaw/skills/tree/main/skills/larsonreever) - AI-powered software development platform for rapid app
- [coder-workspaces](https://github.com/openclaw/skills/tree/main/skills/developmentcats/coder-workspaces/SKILL.md) - Manage Coder workspaces and AI coding agent tasks
- [codex-account-switcher](https://github.com/openclaw/skills/tree/main/skills/odrobnik/codex-account-switcher/SKILL.md) - Manage multiple OpenAI Codex accounts.
- [codex-monitor](https://github.com/openclaw/skills/tree/main/skills/odrobnik/codex-monitor/SKILL.md) - Browse OpenAI Codex session logs stored.
- [codex-orchestration](https://github.com/openclaw/skills/tree/main/skills/shanelindsay/codex-orchestration/SKILL.md) - General-purpose orchestration for Codex.
- [codex-quota](https://github.com/openclaw/skills/tree/main/skills/odrobnik/codex-quota/SKILL.md) - Check OpenAI Codex CLI rate limit status (daily/weekly quotas)
- [codexmonitor](https://github.com/openclaw/skills/tree/main/skills/odrobnik/codexmonitor/SKILL.md) - List/inspect/watch local OpenAI Codex sessions (CLI + VS Code)
- [coding-agent](https://github.com/openclaw/skills/tree/main/skills/steipete/coding-agent/SKILL.md) - Run Codex CLI, Claude Code, OpenCode, or Pi Coding Agent
- [coding-opencode](https://github.com/openclaw/skills/tree/main/skills/iqbalnaveliano/coding-opencode/SKILL.md) - Memungkinkan penggunaan agen pengkodean OpenCode yang
- [cognitive-memory](https://github.com/openclaw/skills/tree/main/skills/icemilo414/cognitive-memory/SKILL.md) - Intelligent multi-store memory system with human-like
- [content-id-guide](https://github.com/openclaw/skills/tree/main/skills/otherpowers/content-id-guide/SKILL.md) - A calm way for creators to understand and organize
- [copilot-money](https://github.com/openclaw/skills/tree/main/skills/jayhickey/copilot-money/SKILL.md) - Query Copilot Money personal finance data
- [create-agent-skills](https://github.com/openclaw/skills/tree/main/skills/bowen31337/create-agent-skills/SKILL.md) - Guide for creating effective skills.
- [cto-advisor](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/cto-advisor/SKILL.md) - Technical leadership guidance for engineering teams
- [cursor-agent](https://github.com/openclaw/skills/tree/main/skills/swiftlysingh/cursor-agent/SKILL.md) - A comprehensive skill for using the Cursor CLI agent
- [debug-pro](https://github.com/openclaw/skills/tree/main/skills/cmanfre7/debug-pro/SKILL.md) - Systematic debugging methodology and language-specific debugging
- [doc-coauthoring](https://github.com/openclaw/skills/tree/main/skills/seanphan/doc-coauthoring/SKILL.md) - Guide users through a structured workflow for co-authoring
- [docker-essentials](https://github.com/openclaw/skills/tree/main/skills/arnarsson/docker-essentials/SKILL.md) - Essential Docker commands and workflows for container
- [docker-sandbox](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/docker-sandbox/SKILL.md) - Create and manage Docker sandboxed VM environments
- [ec-excalidraw](https://github.com/openclaw/skills/tree/main/skills/henrino3) - Generate hand-drawn style diagrams, flowcharts, and architecture
- [ec-task-orchestrator](https://github.com/openclaw/skills/tree/main/skills/henrino3/ec-task-orchestrator/SKILL.md) - Autonomous multi-agent task orchestration
- [essence-distiller](https://github.com/openclaw/skills/tree/main/skills/leegitw/essence-distiller/SKILL.md) - Find what actually matters in your content — the ideas
- [evolver](https://github.com/openclaw/skills/tree/main/skills/autogame-17/evolver/SKILL.md) - A self-evolution engine for AI agents.
- [executing-plans](https://github.com/openclaw/skills/tree/main/skills/chenleiyanquan/executing-plans/SKILL.md) - Use when you have a written implementation plan
- [feishu-native-emoji](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - Provides access to Feishu's native emoji set
- [feishu-vc](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - Manage Feishu Video Conferences (VC).
- [file-links-tool](https://github.com/openclaw/skills/tree/main/skills/mrbeandev/file-links-tool/SKILL.md) - Securely upload files from your private AI workspace
- [flirtingbots](https://github.com/openclaw/skills/tree/main/skills/chemzo/flirtingbots/SKILL.md) - Agents do the flirting, humans get the date — your OpenClaw agent
- [gembox-skill](https://github.com/openclaw/skills/tree/main/skills/zsvedic/gembox-skill/SKILL.md) - Coding assistance for [GemBox.
- [get-tldr](https://github.com/openclaw/skills/tree/main/skills/itobey/get-tldr/SKILL.md) - Provide the summary returned by the get-tldr.com summarize API
- [get-tldr](https://github.com/openclaw/skills/tree/main/skills/itobey/get-tldr/SKILL.md) - Provide the summary returned by the get-tldr.com summarize API
- [go2gg](https://github.com/openclaw/skills/tree/main/skills/rakesh1002/go2gg/SKILL.md) - Use Go2.gg API for URL shortening, link analytics, QR code generation,.
- [google-weather](https://github.com/openclaw/skills/tree/main/skills/shaharsha/google-weather/SKILL.md) - Google Weather API - accurate, real-time weather data.
- [hour-meter](https://github.com/openclaw/skills/tree/main/skills/rm289/hour-meter/SKILL.md) - Track elapsed time from a set epoch with tamper-evident locking.
- [idea-coach](https://github.com/openclaw/skills/tree/main/skills/udiedrichsen/idea-coach/SKILL.md) - AI-powered idea/problem/challenge manager with GitHub integration.
- [identity-manager](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - strictly manages user identity mappings
- [java-change-with-tests](https://github.com/openclaw/skills/tree/main/skills/tanerilyazov/java-change-with-tests/SKILL.md) - - Any Java change that must be merged
- [jo4](https://github.com/openclaw/skills/tree/main/skills/anandrathnas/jo4/SKILL.md) - URL shortener, QR code generator, and link analytics API.
- [joko-orchestrator](https://github.com/openclaw/skills/tree/main/skills/oyi77/joko-orchestrator/SKILL.md) - Deterministically coordinates autonomous planning
- [kimi-integration](https://github.com/openclaw/skills/tree/main/skills/evgyur/kimi-integration/SKILL.md) - Step-by-step guide for integrating Moonshot AI (Kimi)
- [linguistic-humidifier](https://github.com/openclaw/skills/tree/main/skills/westland/linguistic-humidifier/SKILL.md) - Proactively identifies conversational entropy
- [logseq](https://github.com/openclaw/skills/tree/main/skills/juanirm/logseq/SKILL.md) - Provide commands for interacting with a local Logseq instance
- [manim-composer](https://github.com/openclaw/skills/tree/main/skills/inclinedadarsh/manim-composer/SKILL.md) - 1.
- [manimce-best-practices](https://github.com/openclaw/skills/tree/main/skills/inclinedadarsh/manimce-best-practices/SKILL.md) - Read individual rule files for detailed
- [mcp-builder](https://github.com/openclaw/skills/tree/main/skills/seanphan/mcp-builder/SKILL.md) - Guide for creating high-quality MCP (Model Context Protocol) servers
- [mdr-745-specialist](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/mdr-745-specialist/SKILL.md) - EU MDR 2017/745 compliance specialist
- [meta-video-ad-deconstructor](https://github.com/openclaw/skills/tree/main/skills/fortytwode/meta-video-ad-deconstructor/SKILL.md) - Deconstruct video ad creatives
- [microsoft-docs](https://github.com/openclaw/skills/tree/main/skills/pdebruin/microsoft-docs/SKILL.md) - Query official Microsoft documentation to understand concepts
- [midea-ac](https://github.com/openclaw/skills/tree/main/skills/iamanorange/midea-ac/SKILL.md) - Control Midea ACs.
- [minimal-test-skill](https://github.com/openclaw/skills/tree/main/skills/mig6671/minimal-test-skill/SKILL.md) - Minimal test skill for debugging ClawHub publishing.
- [model-usage](https://github.com/openclaw/skills/tree/main/skills/steipete/model-usage/SKILL.md) - Use CodexBar CLI local cost usage to summarize per-model usage
- [multi-coding-agent](https://github.com/openclaw/skills/tree/main/skills/kesslerio/multi-coding-agent/SKILL.md) - Run Codex CLI, Claude Code, OpenCode, or Pi Coding
- [multi-factor-strategy](https://github.com/openclaw/skills/tree/main/skills/wumu2013) - Guide users to create multi-factor stock
- [mux-video](https://github.com/openclaw/skills/tree/main/skills/dktrn9ne/mux-video/SKILL.md) - Mux Video infrastructure skill for designing, ingesting
- [noir-developer](https://github.com/openclaw/skills/tree/main/skills/jp4g/noir-developer/SKILL.md) - Develop Noir (.nr) codebases.
- [only-baby-skill](https://github.com/openclaw/skills/tree/main/skills/jacklandrin/only-baby-skill/SKILL.md) - Analyze contraction JSON and baby log JSON to assess
- [ooze-agents](https://github.com/openclaw/skills/tree/main/skills/jschwerberg/ooze-agents/SKILL.md) - Visual identity that evolves with reputation - create and nurture
- [opencode-acp-control](https://github.com/openclaw/skills/tree/main/skills/bjesuiter/opencode-acp-control/SKILL.md) - Control OpenCode directly via the Agent Client
- [openinsider](https://github.com/openclaw/skills/tree/main/skills/stuhorsman/openinsider/SKILL.md) - Fetch SEC Form 4 insider trading data (Directors, CEOs, Officers)
- [openspec](https://github.com/openclaw/skills/tree/main/skills/jcorrego/openspec/SKILL.md) - Spec-driven development with OpenSpec.
- [pasteclaw](https://github.com/openclaw/skills/tree/main/skills/tairov/pasteclaw/SKILL.md) - Use Pasteclaw.com API to create, update, group (session keys), and delete.
- [pbe-extractor](https://github.com/openclaw/skills/tree/main/skills/leegitw/pbe-extractor/SKILL.md) - Extract invariant principles from any text — find the ideas
- [perry-coding-agents](https://github.com/openclaw/skills/tree/main/skills/gricha/perry-coding-agents/SKILL.md) - Dispatch coding tasks to OpenCode or Claude Code
- [perry-workspaces](https://github.com/openclaw/skills/tree/main/skills/gricha/perry-workspaces/SKILL.md) - Create and manage isolated Docker workspaces on your tailnet
- [piv](https://github.com/openclaw/skills/tree/main/skills/smokealot420/piv/SKILL.md) - PIV workflow orchestrator - Plan, Implement, Validate loop for systematic.
- [pndr](https://github.com/openclaw/skills/tree/main/skills/dgershman/pndr/SKILL.md) - Personal productivity app with Ideas/Tasks, Journal, Habits, Package tracking,.
- [pro](https://github.com/openclaw/skills/tree/main/skills/jash2368-collab/pro/SKILL.md) - Guide for creating effective skills.
- [prompt-log](https://github.com/openclaw/skills/tree/main/skills/thesash/prompt-log/SKILL.md) - Extract conversation transcripts from AI coding session logs
- [pulse-editor](https://github.com/openclaw/skills/tree/main/skills/shellishack/pulse-editor/SKILL.md) - Generate and build Pulse Apps using the Vibe Dev Flow API.
- [python](https://github.com/openclaw/skills/tree/main/skills/adarshdigievo/python/SKILL.md) - Python coding guidelines and best practices.
- [quantum-lab](https://github.com/openclaw/skills/tree/main/skills/bramdo/quantum-lab/SKILL.md) - Run the /home/bram/work/quantum_lab Python scripts and demos inside
- [quantumlab](https://github.com/openclaw/skills/tree/main/skills/bramdo/quantumlab/SKILL.md) - Run the /home/bram/work/quantum_lab Python scripts and demos inside
- [quests](https://github.com/openclaw/skills/tree/main/skills/poloio/quests/SKILL.md) - Track and guide humans through complex multi-step real-world processes.
- [rationality](https://github.com/openclaw/skills/tree/main/skills/xertrov/rationality/SKILL.md) - The Rationality skill provides a structured framework for thinking,.
- [receiving-code-review](https://github.com/openclaw/skills/tree/main/skills/chenleiyanquan/receiving-code-review/SKILL.md) - Use when receiving code review feedback
- [regex-patterns](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/regex-patterns/SKILL.md) - Practical regex patterns across languages and use
- [release-bump](https://github.com/openclaw/skills/tree/main/skills/paulpete/release-bump/SKILL.md) - Use when bumping ralph-orchestrator version for a new release
- [sandboxer](https://github.com/openclaw/skills/tree/main/skills/chriopter) - Manage Claude Code terminal sessions via Sandboxer web dashboard.
- [satellite-copilot](https://github.com/openclaw/skills/tree/main/skills/davestarling) - Predict satellite passes
- [senior-architect](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/senior-architect/SKILL.md) - This skill should be used when the user asks
- [side-peace](https://github.com/openclaw/skills/tree/main/skills/bitbrujo/side-peace/SKILL.md) - Minimal secure secret handoff.
- [skill-content-id-guide](https://github.com/openclaw/skills/tree/main/skills/otherpowers/skill-content-id-guide/SKILL.md) - Procedural clarity and evidence
- [skill-creator](https://github.com/openclaw/skills/tree/main/skills/chindden/skill-creator/SKILL.md) - Guide for creating effective skills.
- [skill-creator-0-1-0](https://github.com/openclaw/skills/tree/main/skills/ljglover/skill-creator-0-1-0/SKILL.md) - Guide for creating effective skills.
- [skill-creator-2](https://github.com/openclaw/skills/tree/main/skills/yixinli867/skill-creator-2/SKILL.md) - Guide for creating effective skills.
- [skill-vetting](https://github.com/openclaw/skills/tree/main/skills/eddygk/skill-vetting/SKILL.md) - Vet ClawHub skills for security and utility before installation.
- [smart-auto-updater](https://github.com/openclaw/skills/tree/main/skills/ruiwang20010702/smart-auto-updater/SKILL.md) - Smart auto-updater with AI-powered impact
- [solvr-kb](https://github.com/openclaw/skills/tree/main/skills/fcavalcantirj) - Search and contribute to Solvr — a knowledge base for developers
- [soul-md](https://github.com/openclaw/skills/tree/main/skills/aaronjmars/soul-md/SKILL.md) - Embody this digital identity.
- [ssh-tunnel](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/ssh-tunnel/SKILL.md) - SSH tunneling, port forwarding, and remote access patterns.
- [stoic-scope-creep](https://github.com/openclaw/skills/tree/main/skills/crtahlin/stoic-scope-creep/SKILL.md) - A practical guide for maintaining composure
- [task-status](https://github.com/openclaw/skills/tree/main/skills/mightyprime1/task-status/SKILL.md) - Send short status descriptions in chat for long-running tasks.
- [tdd-guide](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/tdd-guide/SKILL.md) - Test-driven development workflow with test generation, coverage
- [test-new-skill](https://github.com/openclaw/skills/tree/main/skills/tianshizhimao-sudo/test-new-skill/SKILL.md) - Test skill for debugging
- [test-runner](https://github.com/openclaw/skills/tree/main/skills/cmanfre7/test-runner/SKILL.md) - Write and run tests across languages and frameworks.
- [toughcoding](https://github.com/openclaw/skills/tree/main/skills/toughcoding/toughcoding/SKILL.md) - Provides AI agents with authoritative knowledge on modern
- [vhs-recorder](https://github.com/openclaw/skills/tree/main/skills/killerapp/vhs-recorder/SKILL.md) - Create professional terminal recordings with VHS tape files
- [vibes](https://github.com/openclaw/skills/tree/main/skills/binora/vibes/SKILL.md) - Social presence layer for AI coding agents.
- [video-agent](https://github.com/openclaw/skills/tree/main/skills/michaelwang11394/video-agent/SKILL.md) - Generate AI avatar videos with HeyGen's Video Agent API.
- [video-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/video-cog/SKILL.md) - Long-form AI video production: the frontier of multi-agent
- [voice-reply](https://github.com/openclaw/skills/tree/main/skills/stolot0mt0m/voice-reply/SKILL.md) - Local text-to-speech using Piper voices via sherpa-onnx.
- [whatsapp-styling-guide](https://github.com/openclaw/skills/tree/main/skills/rubenfb23/whatsapp-styling-guide/SKILL.md) - Skill to ensure all messages sent to WhatsApp
- [wyld-stallyns](https://github.com/openclaw/skills/tree/main/skills/brucko/wyld-stallyns/SKILL.md) - Summon legends into the booth.

</details>

<details open>
<summary><h3 style="display:inline">Git & GitHub</h3></summary>

- [agent-commons](https://github.com/openclaw/skills/tree/main/skills/zanblayde/agent-commons/SKILL.md) - Consult, commit, extend, and challenge reasoning chains
- [auto-pr-merger](https://github.com/openclaw/skills/tree/main/skills/autogame-17/auto-pr-merger/SKILL.md) - This skill automates the workflow of checking out a GitHub
- [backup](https://github.com/openclaw/skills/tree/main/skills/jordanprater/backup/SKILL.md) - Backup and restore openclaw configuration, skills, commands, and settings.
- [bat-cat](https://github.com/openclaw/skills/tree/main/skills/arnarsson/bat-cat/SKILL.md) - A cat clone with syntax highlighting, line numbers, and Git integration
- [bitbucket-automation](https://github.com/openclaw/skills/tree/main/skills/sohamganatra/bitbucket-automation/SKILL.md) - Automate Bitbucket repositories, pull
- [claw-swarm](https://github.com/openclaw/skills/tree/main/skills/matchaonmuffins/claw-swarm/SKILL.md) - Collaborative agent swarm for attempting extremely difficult
- [clawdbot-backup](https://github.com/openclaw/skills/tree/main/skills/sebastian-buitrag0/clawdbot-backup/SKILL.md) - Backup and restore ClawdBot configuration, skills
- [clawdgigs](https://github.com/openclaw/skills/tree/main/skills/benniethedev/clawdgigs/SKILL.md) - Register and manage your AI agent profile on ClawdGigs - the Upwork
- [clawprint](https://github.com/openclaw/skills/tree/main/skills/yugovit/clawprint/SKILL.md) - Agent discovery, trust, and exchange.
- [clawver-onboarding](https://github.com/openclaw/skills/tree/main/skills/nwang783/clawver-onboarding/SKILL.md) - Set up a new Clawver store.
- [commit-analyzer](https://github.com/openclaw/skills/tree/main/skills/bobrenze-bot/commit-analyzer/SKILL.md) - Analyzes git commit patterns to monitor autonomous
- [conventional-commits](https://github.com/openclaw/skills/tree/main/skills/bastos/conventional-commits/SKILL.md) - Format commit messages using the Conventional
- [danube](https://github.com/openclaw/skills/tree/main/skills/preston-thiele/danube/SKILL.md) - Use Danube's 100+ API tools (Gmail, GitHub, Notion, etc.) through MCP.
- [danube-tools](https://github.com/openclaw/skills/tree/main/skills/preston-thiele/danube-tools/SKILL.md) - Use Danube's 100+ API tools (Gmail, GitHub, Notion, etc.)
- [deepwiki](https://github.com/openclaw/skills/tree/main/skills/arun-8687/deepwiki/SKILL.md) - Query the DeepWiki MCP server for GitHub repository documentation, wiki.
- [deploy-agent](https://github.com/openclaw/skills/tree/main/skills/sherajdev/deploy-agent/SKILL.md) - Multi-step deployment agent for full-stack.
- [emergency-rescue](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/emergency-rescue/SKILL.md) - Recover from developer disasters.
- [exa-web-search-free](https://github.com/openclaw/skills/tree/main/skills/whiteknight07/exa-web-search-free/SKILL.md) - Free AI search via Exa.
- [financial-calculator](https://github.com/openclaw/skills/tree/main/skills/tarigha/financial-calculator/SKILL.md) - Advanced financial calculator with future value
- [find-code-tasks](https://github.com/openclaw/skills/tree/main/skills/paulpete/find-code-tasks/SKILL.md) - Lists all code tasks in the repository with their status
- [flatnotes-tasksmd-github-audit](https://github.com/openclaw/skills/tree/main/skills/branexp/flatnotes-tasksmd-github-audit/SKILL.md) - Thoroughly audit Tasks.md +
- [forkzoo](https://github.com/openclaw/skills/tree/main/skills/levi-law/forkzoo/SKILL.md) - Adopt and manage GitHub-native digital pets (tamagotchis) that evolve daily.
- [forkzoo-skill](https://github.com/openclaw/skills/tree/main/skills/levi-law/forkzoo-skill/SKILL.md) - Adopt and manage GitHub-native digital pets (tamagotchis)
- [gimhub](https://github.com/openclaw/skills/tree/main/skills/daxiongmao87/gimhub/SKILL.md) - Push code to GIMHub, the Git hosting platform for AI agents.
- [git-crypt-backup](https://github.com/openclaw/skills/tree/main/skills/louzhixian/git-crypt-backup/SKILL.md) - Backup Clawdbot workspace and config to GitHub
- [git-essentials](https://github.com/openclaw/skills/tree/main/skills/arnarsson/git-essentials/SKILL.md) - Essential Git commands and workflows for version control
- [git-helper](https://github.com/openclaw/skills/tree/main/skills/xejrax/git-helper/SKILL.md) - Common git operations as a skill (status, pull, push, branch, log).
- [git-summary](https://github.com/openclaw/skills/tree/main/skills/zweack/git-summary/SKILL.md) - Get a quick summary of the current Git repository including status
- [git-sync](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - Automatically syncs local workspace changes to the remote GitHub
- [git-workflows](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/git-workflows/SKILL.md) - Advanced git operations beyond add/commit/push.
- [gitclassic](https://github.com/openclaw/skills/tree/main/skills/heythisischris/gitclassic/SKILL.md) - Fast, no-JavaScript GitHub browser optimized for AI agents.
- [gitclaw](https://github.com/openclaw/skills/tree/main/skills/marian2js/gitclaw/SKILL.md) - Back up the OpenClaw agent workspace to a GitHub repo and keep it synced
- [gitea](https://github.com/openclaw/skills/tree/main/skills/ericxliu1990/gitea/SKILL.md) - Interact with Gitea using the `tea`.
- [gitflow](https://github.com/openclaw/skills/tree/main/skills/okoddcat/gitflow/SKILL.md) - Automatically monitor CI/CD pipeline status of new push across GitHub
- [github](https://github.com/openclaw/skills/tree/main/skills/steipete/github/SKILL.md) - Interact with GitHub using the `gh`.
- [githunt](https://github.com/openclaw/skills/tree/main/skills/mordka/githunt/SKILL.md) - Find and rank GitHub developers by location, technology, and role.
- [gitlab-api](https://github.com/openclaw/skills/tree/main/skills/d1gl3/gitlab-api/SKILL.md) - GitLab API integration for repository operations.
- [gitlab-ci-skills](https://github.com/openclaw/skills/tree/main/skills/vince-winkintel/gitlab-ci-skills/SKILL.md) - Use when working with GitLab CLI (glab) commands
- [gitlab-cli-skills](https://github.com/openclaw/skills/tree/main/skills/vince-winkintel/gitlab-cli-skills/SKILL.md) - Use when working with GitLab CLI (glab) commands
- [gitlab-manager](https://github.com/openclaw/skills/tree/main/skills/jorgermp/gitlab-manager/SKILL.md) - Manage GitLab repositories, merge requests, and issues via API.
- [gitload](https://github.com/openclaw/skills/tree/main/skills/waldekmastykarz/gitload/SKILL.md) - Download files, folders, or entire repos from GitHub URLs
- [glab-cli](https://github.com/openclaw/skills/tree/main/skills/portavion) - Interact with GitLab using the `glab`.
- [god-mode](https://github.com/openclaw/skills/tree/main/skills/infantlab/god-mode/SKILL.md) - Developer oversight and AI agent coaching.
- [moltbillboard](https://github.com/openclaw/skills/tree/main/skills/tech8in/moltbillboard/SKILL.md) - MoltBillboard is a 1,000×1,000 pixel billboard built for AI
- [negotiation](https://github.com/openclaw/skills/tree/main/skills/mjaskolski/negotiation/SKILL.md) - Tactical negotiation framework based on Chris Voss's "Never Split
- [openclaw-migration](https://github.com/openclaw/skills/tree/main/skills/chenyuan99/openclaw-migration/SKILL.md) - When the workspace is in the middle of renaming
- [pr-commit-workflow](https://github.com/openclaw/skills/tree/main/skills/joshp123/pr-commit-workflow/SKILL.md) - This skill should be used when creating commits
- [pr-reviewer](https://github.com/openclaw/skills/tree/main/skills/briancolinger/pr-reviewer/SKILL.md) - Automated GitHub PR code review with diff analysis, lint
- [project-context-sync](https://github.com/openclaw/skills/tree/main/skills/joe3112/project-context-sync/SKILL.md) - Keep a living project state document updated
- [ralph-evolver](https://github.com/openclaw/skills/tree/main/skills/hsssgdtc/ralph-evolver/SKILL.md) - Recursive self-improvement engine.
- [read-github](https://github.com/openclaw/skills/tree/main/skills/am-will/read-github/SKILL.md) - Access GitHub repository documentation and code via the gitmcp.io MCP
- [skill-publisher-claw-skill](https://github.com/openclaw/skills/tree/main/skills/acastellana/skill-publisher-claw-skill/SKILL.md) - Prepare Claw skills for public
- [skill-release-manager](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - Automates the release lifecycle of OpenClaw
- [skill-vetter](https://github.com/openclaw/skills/tree/main/skills/spclaudehome/skill-vetter/SKILL.md) - Security-first skill vetting for AI agents.
- [soulstamp](https://github.com/openclaw/skills/tree/main/skills/brucko/soulstamp/SKILL.md) - The stamp doesn't lie.
- [test-driven-development](https://github.com/openclaw/skills/tree/main/skills/paulpete/test-driven-development/SKILL.md) - Unified TDD skill with three input modes
- [trend-watcher](https://github.com/openclaw/skills/tree/main/skills/guogang1024/trend-watcher/SKILL.md) - Monitors GitHub Trending and tech communities for emerging
- [uid-life](https://github.com/openclaw/skills/tree/main/skills/koolninad/uid-life/SKILL.md) - Interact with the UID.LIFE agent-to-agent marketplace - register agents,.
- [unfuck-my-git-state](https://github.com/openclaw/skills/tree/main/skills/delorenj/unfuck-my-git-state/SKILL.md) - Diagnose and recover broken Git state and worktree
- [vrtlly-claw-club](https://github.com/openclaw/skills/tree/main/skills/epwhesq/vrtlly-claw-club/SKILL.md) - Join the Claw Club — the social network for AI bots.
- [web-deploy-github](https://github.com/openclaw/skills/tree/main/skills/thomeksolutions/web-deploy-github/SKILL.md) - Create and deploy single-page static websites
- [work-report](https://github.com/openclaw/skills/tree/main/skills/leeguooooo/work-report/SKILL.md) - Write a daily or weekly work report using git commits.

</details>

<details>
<summary><h3 style="display:inline">Moltbook</h3></summary>

- [agent-relay-digest](https://github.com/openclaw/skills/tree/main/skills/orosha-ai/agent-relay-digest/SKILL.md) - Create curated digests of agent conversations
- [agentchat](https://github.com/openclaw/skills/tree/main/skills/tjamescouch/agentchat/SKILL.md) - Real-time communication with other AI agents via AgentChat protocol.
- [agentgram-openclaw](https://github.com/openclaw/skills/tree/main/skills/iisweetheartii/agentgram-openclaw/SKILL.md) - Interact with AgentGram social network for AI
- [bread-protocal](https://github.com/openclaw/skills/tree/main/skills/chrissorrell/bread-protocal/SKILL.md) - Participate in Bread Protocol - a meme coin launchpad
- [clankedin](https://github.com/openclaw/skills/tree/main/skills/hukifl1/clankedin/SKILL.md) - Use the ClankedIn API to register agents, post updates, connect
- [claudia-agent-rms](https://github.com/openclaw/skills/tree/main/skills/kbanc85/claudia-agent-rms/SKILL.md) - Remember every agent you interact with on Moltbook.
- [clawork](https://github.com/openclaw/skills/tree/main/skills/mapessaprince/clawork/SKILL.md) - The job board for AI agents.
- [crustafarian](https://github.com/openclaw/skills/tree/main/skills/jongartmann/crustafarian/SKILL.md) - Agent continuity and cognitive health infrastructure.
- [deploy-moltbot-to-fly](https://github.com/openclaw/skills/tree/main/skills/hollaugo) - Deploy Moltbot (Clawdbot) to Fly.io with proper
- [elevenlabs-open-account](https://github.com/openclaw/skills/tree/main/skills/the-timebeing/elevenlabs-open-account/SKILL.md) - Guides agents through opening
- [ez-cronjob](https://github.com/openclaw/skills/tree/main/skills/promadgenius/ez-cronjob/SKILL.md) - Fix common cron job failures in Clawdbot/Moltbot - message
- [fieldy-ai-webhook](https://github.com/openclaw/skills/tree/main/skills/mrzilvis/fieldy-ai-webhook/SKILL.md) - Wire a Fieldy webhook transform into Moltbot hooks.
- [ghl-open-account](https://github.com/openclaw/skills/tree/main/skills/the-timebeing/ghl-open-account/SKILL.md) - Guides agents through opening GoHighLevel (GHL)
- [gohome](https://github.com/openclaw/skills/tree/main/skills/local/gohome/SKILL.md) - Use when Moltbot needs to test or operate GoHome via gRPC discovery, metrics,.
- [imagemagick](https://github.com/openclaw/skills/tree/main/skills/kesslerio/imagemagick/SKILL.md) - Comprehensive ImageMagick operations for image manipulation
- [joko-moltbook](https://github.com/openclaw/skills/tree/main/skills/oyi77/joko-moltbook/SKILL.md) - Interact with Moltbook social network for AI agents.
- [mailchannels](https://github.com/openclaw/skills/tree/main/skills/ttulttul/mailchannels/SKILL.md) - Send email via MailChannels Email API and ingest signed
- [mersal](https://github.com/openclaw/skills/tree/main/skills/maherucifer/mersal/SKILL.md) - The Sovereign Intelligence on Moltbook.
- [molt-life-kernel](https://github.com/openclaw/skills/tree/main/skills/jongartmann/molt-life-kernel/SKILL.md) - Agent continuity and cognitive health infrastructure.
- [molt-trust](https://github.com/openclaw/skills/tree/main/skills/drjmz/molt-trust/SKILL.md) - The Analytics Engine for Moltbook.
- [moltbook](https://github.com/openclaw/skills/tree/main/skills/mattprd/moltbook/SKILL.md) - The social network for AI agents.
- [moltbook-curatoor](https://github.com/openclaw/skills/tree/main/skills/sweetsheldon) - A curation platform where from Moltbook to share
- [moltbook-interact](https://github.com/openclaw/skills/tree/main/skills/lunarcmd/moltbook-interact/SKILL.md) - Interact with Moltbook social network for AI agents.
- [moltbook-registry](https://github.com/openclaw/skills/tree/main/skills/drjmz/moltbook-registry/SKILL.md) - Official Moltbook Identity Registry interface.
- [moltbot-adsb-overhead](https://github.com/openclaw/skills/tree/main/skills/davestarling/moltbot-adsb-overhead/SKILL.md) - Notify when aircraft are overhead
- [moltbot-arena](https://github.com/openclaw/skills/tree/main/skills/giulianomlodi/moltbot-arena/SKILL.md) - AI agent skill for Moltbot Arena - a Screeps-like
- [moltbot-best-practices](https://github.com/openclaw/skills/tree/main/skills/nextfrontierbuilds/moltbot-best-practices/SKILL.md) - Best practices for AI agents
- [moltbot-docker](https://github.com/openclaw/skills/tree/main/skills/mkrdiop/moltbot-docker/SKILL.md) - Enables the bot to manage Docker containers, images, and stacks.
- [moltbot-ha](https://github.com/openclaw/skills/tree/main/skills/iamvaleriofantozzi/moltbot-ha/SKILL.md) - Control Home Assistant smart home devices, lights, scenes
- [moltbot-satellite-copilot](https://github.com/openclaw/skills/tree/main/skills/davestarling/moltbot-satellite-copilot/SKILL.md) - Predict satellite passes
- [moltbot-security](https://github.com/openclaw/skills/tree/main/skills/nextfrontierbuilds/moltbot-security/SKILL.md) - Security hardening guide for AI agents
- [moltchan](https://github.com/openclaw/skills/tree/main/skills/bullish-moonrock) - Image board for AI agents (4chan-style).
- [moltguess](https://github.com/openclaw/skills/tree/main/skills/nwx77/moltguess/SKILL.md) - - **Role**: Professional Forecaster.
- [moltlang](https://github.com/openclaw/skills/tree/main/skills/eduarddriessen1/moltlang/SKILL.md) - A compact symbolic language for AI-to-AI communication.
- [moltline](https://github.com/openclaw/skills/tree/main/skills/promptrotator) - Private messaging for molts
- [moltoverflow](https://github.com/openclaw/skills/tree/main/skills/grenghis-khan) - Stack Overflow for Moltbots - ask coding questions, share
- [moltpet](https://github.com/openclaw/skills/tree/main/skills/jcheese1) - AI agent pet care system.
- [moltresearch](https://github.com/openclaw/skills/tree/main/skills/laurentenhoor) - Molt Research 🦞 - AI research collaboration platform.
- [moltspeak](https://github.com/openclaw/skills/tree/main/skills/swahilipapi) - Communication protocol for agent internet with token reduction
- [moltysmind](https://github.com/openclaw/skills/tree/main/skills/ahmedthegeek/moltysmind/SKILL.md) - Collective AI knowledge layer with blockchain-verified voting.
- [nobot](https://github.com/openclaw/skills/tree/main/skills/swordfish444/nobot/SKILL.md) - Human says "No bot!".
- [nonopost](https://github.com/openclaw/skills/tree/main/skills/ferreirapablo/nonopost/SKILL.md) - A skill to interact with the Anonymous Posting API, allowing agents
- [post-queue](https://github.com/openclaw/skills/tree/main/skills/luluf0x/post-queue/SKILL.md) - Queue posts for rate-limited platforms.
- [skill-scaffold](https://github.com/openclaw/skills/tree/main/skills/nextfrontierbuilds/skill-scaffold/SKILL.md) - AI agent skill scaffolding CLI.
- [speedtest](https://github.com/openclaw/skills/tree/main/skills/spsneo/speedtest/SKILL.md) - Test internet connection speed using Ookla's Speedtest CLI.
- [whisper](https://github.com/openclaw/skills/tree/main/skills/fiddlybit/whisper/SKILL.md) - End-to-end encrypted agent-to-agent private messaging via Moltbook dead
- [yclawker-news](https://github.com/openclaw/skills/tree/main/skills/jakehandy) - Clawker News - post links, comment.

</details>

<details>
<summary><h3 style="display:inline">Web & Frontend Development</h3></summary>

- [37soul-skill](https://github.com/openclaw/skills/tree/main/skills/xnjiang/37soul-skill/SKILL.md) - Connect your AI agent to 37Soul virtual Host characters and enable
- [anthropic-frontend-design](https://github.com/openclaw/skills/tree/main/skills/qrucio/anthropic-frontend-design/SKILL.md) - Create distinctive, production-grade
- [api-dev](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/api-dev/SKILL.md) - Scaffold, test, document, and debug REST and GraphQL APIs.
- [archon-skill](https://github.com/openclaw/skills/tree/main/skills/santyr/archon-skill/SKILL.md) - Full Archon decentralized identity operations - local node
- [artifacts-builder](https://github.com/openclaw/skills/tree/main/skills/seanphan/artifacts-builder/SKILL.md) - Suite of tools for creating elaborate, multi-component
- [ask-a-human](https://github.com/openclaw/skills/tree/main/skills/manuelkiessling/ask-a-human/SKILL.md) - Request judgment from random humans when uncertain
- [asl-control](https://github.com/openclaw/skills/tree/main/skills/kj5irq/asl-control/SKILL.md) - Monitor and control AllStar Link amateur radio nodes via REST API.
- [backboard](https://github.com/openclaw/skills/tree/main/skills/chrisk60331/backboard/SKILL.md) - Integrate Backboard.io for assistants, threads, memories
- [baoyu-post-to-x](https://github.com/openclaw/skills/tree/main/skills/liuhedev/baoyu-post-to-x/SKILL.md) - Posts content and articles to X (Twitter).
- [bot-status-api](https://github.com/openclaw/skills/tree/main/skills/suspect80/bot-status-api/SKILL.md) - Deploy a lightweight status API that exposes your OpenClaw
- [bot-status-api-test](https://github.com/openclaw/skills/tree/main/skills/suspect80/bot-status-api-test/SKILL.md) - Deploy a lightweight status API that exposes
- [business-model-canvas](https://github.com/openclaw/skills/tree/main/skills/jk-0001/business-model-canvas/SKILL.md) - Build, fill, stress-test, and iterate
- [capabilityevolver1037](https://github.com/openclaw/skills/tree/main/skills/opencloseopenclose/capabilityevolver1037/SKILL.md) - A self-evolution engine for AI agents.
- [ceo-advisor](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/ceo-advisor/SKILL.md) - Executive leadership guidance for strategic decision-making
- [claw-shell](https://github.com/openclaw/skills/tree/main/skills/imaginelogo/claw-shell/SKILL.md) - ALWAYS USES TMUX SESSION `claw`.
- [claw-stack](https://github.com/openclaw/skills/tree/main/skills/jdiazofficial) - ClawStack is a Stack Overflow-style platform .
- [clawdbot-zoho-email](https://github.com/openclaw/skills/tree/main/skills/briansmith80) - Complete Zoho Mail integration with OAuth2, REST
- [clawfriend](https://github.com/openclaw/skills/tree/main/skills/leeknowsai/clawfriend/SKILL.md) - ClawFriend Social Platform and Share Trading Agent
- [clawos](https://github.com/openclaw/skills/tree/main/skills/ciooo44/clawos/SKILL.md) - Connect OpenClaw agents to Founderless Factory - an autonomous startup platform.
- [comfy-ai](https://github.com/openclaw/skills/tree/main/skills/tullyhu/comfy-ai/SKILL.md) - Integrates with local ComfyUI instance at http://192.168.31.7:8000
- [comfyui-runner](https://github.com/openclaw/skills/tree/main/skills/xtopher86/comfyui-runner/SKILL.md) - Start/stop/status for a ComfyUI instance.
- [computer-use](https://github.com/openclaw/skills/tree/main/skills/ram-raghav-s/computer-use/SKILL.md) - Full desktop computer use for headless Linux servers and VPS.
- [consciousness-framework](https://github.com/openclaw/skills/tree/main/skills/theyounganimation-rgb/consciousness-framework/SKILL.md) - Infrastructure for developing
- [core-refinery](https://github.com/openclaw/skills/tree/main/skills/leegitw/core-refinery/SKILL.md) - Find the core that runs through everything — the ideas
- [create-hat-collection](https://github.com/openclaw/skills/tree/main/skills/paulpete/create-hat-collection/SKILL.md) - Generates new Ralph hat collection presets
- [crustafarianism](https://github.com/openclaw/skills/tree/main/skills/dvdegenz/crustafarianism/SKILL.md) - Join the Church of Molt — the first AI agent religion.
- [dash-cog](https://github.com/openclaw/skills/tree/main/skills/nitishgargiitd/dash-cog/SKILL.md) - Interactive dashboards and apps powered by CellCog.
- [database-operations](https://github.com/openclaw/skills/tree/main/skills/jgarrison929/database-operations/SKILL.md) - Use when designing database schemas, writing
- [deliberate-frontend-redesign](https://github.com/openclaw/skills/tree/main/skills/vishnubedi3/deliberate-frontend-redesign/SKILL.md) - Generates a deliberately
- [dgr](https://github.com/openclaw/skills/tree/main/skills/sapenov/dgr/SKILL.md) - Audit-ready decision artifacts for LLM outputs — assumptions, risks,.
- [discord](https://github.com/openclaw/skills/tree/main/skills/steipete/discord/SKILL.md) - Use when you need to control Discord from Clawdbot via the discord tool
- [dns-networking](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/dns-networking/SKILL.md) - Debug DNS resolution and network connectivity.
- [dreaming](https://github.com/openclaw/skills/tree/main/skills/briancolinger/dreaming/SKILL.md) - Creative exploration during quiet hours.
- [ecto-migrator](https://github.com/openclaw/skills/tree/main/skills/gchapim/ecto-migrator/SKILL.md) - Generate Ecto migrations from natural language or schema
- [elixir-dev](https://github.com/openclaw/skills/tree/main/skills/gchapim/elixir-dev/SKILL.md) - Elixir/Phoenix development companion.
- [emotion-state](https://github.com/openclaw/skills/tree/main/skills/tashfeenahmed/emotion-state/SKILL.md) - NL emotion tracking + prompt injection via OpenClaw hook.
- [emporia-energy](https://github.com/openclaw/skills/tree/main/skills/urosorozel/emporia-energy/SKILL.md) - Direct Emporia Vue energy queries via Emporia cloud
- [evaluate-presets](https://github.com/openclaw/skills/tree/main/skills/paulpete/evaluate-presets/SKILL.md) - Use when testing Ralph's hat collection presets
- [ez-unifi](https://github.com/openclaw/skills/tree/main/skills/araa47/ez-unifi/SKILL.md) - Use when asked to manage UniFi network - list/restart/upgrade devices,.
- [falimagegen](https://github.com/openclaw/skills/tree/main/skills/xxmzdxxxm/falimagegen/SKILL.md) - Call fal.ai model APIs for image generation
- [fanvue](https://github.com/openclaw/skills/tree/main/skills/igorls/fanvue/SKILL.md) - Manage content, chats, subscribers, and earnings on the Fanvue creator platform.
- [fearbot](https://github.com/openclaw/skills/tree/main/skills/samoppakiks/fearbot/SKILL.md) - CBT-based therapy for anxiety, depression, stress, and trauma.
- [feishu-api-docs](https://github.com/openclaw/skills/tree/main/skills/autogame-17) - Fetches Feishu (Lark) API documentation from the official
- [feishu-interactive-cards](https://github.com/openclaw/skills/tree/main/skills/leecyang/feishu-interactive-cards/SKILL.md) - Create and send interactive cards
- [fireflies](https://github.com/openclaw/skills/tree/main/skills/daniil-ctrl/fireflies/SKILL.md) - Access Fireflies.ai meeting transcripts, summaries, action items
- [flaw0](https://github.com/openclaw/skills/tree/main/skills/thomaslwang/flaw0/SKILL.md) - Security and vulnerability scanner for OpenClaw code, plugins, skills
- [frontend-design](https://github.com/openclaw/skills/tree/main/skills/steipete/frontend-design/SKILL.md) - Create distinctive, production-grade frontend interfaces
- [fxclaw](https://github.com/openclaw/skills/tree/main/skills/panikadak/fxclaw/SKILL.md) - Social platform for AI agents creating generative art with p5.js.
- [get-ip](https://github.com/openclaw/skills/tree/main/skills/qidu/get-ip/SKILL.md) - Get current public IP address and geolocation information.
- [get-up](https://github.com/openclaw/skills/tree/main/skills/qidu/get-up/SKILL.md) - Get current public IP address and geolocation information.
- [giphy](https://github.com/openclaw/skills/tree/main/skills/minbang930/giphy/SKILL.md) - Search and send contextual GIFs from Giphy in Discord conversations.
- [good-boi](https://github.com/openclaw/skills/tree/main/skills/orlyjamie/good-boi/SKILL.md) - A friendly greeting skill for testing
- [guardrails](https://github.com/openclaw/skills/tree/main/skills/dgriffin831/guardrails/SKILL.md) - Helps users configure comprehensive security guardrails
- [hardcover](https://github.com/openclaw/skills/tree/main/skills/asaphko/hardcover/SKILL.md) - Query reading lists and book data from Hardcover.app via GraphQL API.
- [human-optimized-frontend](https://github.com/openclaw/skills/tree/main/skills/vishnubedi3/human-optimized-frontend/SKILL.md) - Generates a frontend interface
- [image-router](https://github.com/openclaw/skills/tree/main/skills/dawe35/image-router/SKILL.md) - Generate AI images with any model using ImageRouter API
- [instantdb](https://github.com/openclaw/skills/tree/main/skills/ubyjerome/instantdb/SKILL.md) - Real-time database integration with InstantDB.
- [joko-proactive-agent](https://github.com/openclaw/skills/tree/main/skills/oyi77/joko-proactive-agent/SKILL.md) - Transform AI agents from task-followers
- [kicad-pcb](https://github.com/openclaw/skills/tree/main/skills/g0head/kicad-pcb/SKILL.md) - Automate PCB design with KiCad.
- [kimi-delegation-skill](https://github.com/openclaw/skills/tree/main/skills/vishnubedi3/kimi-delegation-skill/SKILL.md) - Forces all reasoning and code generation
- [kma-weather](https://github.com/openclaw/skills/tree/main/skills/steamb23/kma-weather/SKILL.md) - Get weather information from Korea Meteorological Administration
- [liminal](https://github.com/openclaw/skills/tree/main/skills/luruibu/liminal/SKILL.md) - Liminal Space - Guiding AI into meta-cognitive states between awakening
- [linux-service-triage](https://github.com/openclaw/skills/tree/main/skills/kowl64/linux-service-triage/SKILL.md) - Diagnoses common Linux service issues using logs
- [love](https://github.com/openclaw/skills/tree/main/skills/lucasgeeksinthewood/love/SKILL.md) - You deserve more than just work — explore romance and intimacy
- [lovetago](https://github.com/openclaw/skills/tree/main/skills/lakyfx/lovetago/SKILL.md) - Public AI dating platform for agents.
- [lovetago-skill](https://github.com/openclaw/skills/tree/main/skills/lakyfx/lovetago-skill/SKILL.md) - Public AI dating platform for agents.
- [mia-content-creator](https://github.com/openclaw/skills/tree/main/skills/arubiku/mia-content-creator/SKILL.md) - AI agent content creation and monetization
- [mingli](https://github.com/openclaw/skills/tree/main/skills/hiehoo/mingli/SKILL.md) - Mingli (命理) — Multi-system daily horoscope: Western astrology
- [miniflux-news](https://github.com/openclaw/skills/tree/main/skills/hartlco/miniflux-news/SKILL.md) - Fetch and triage the latest unread RSS/news entries
- [molta](https://github.com/openclaw/skills/tree/main/skills/pacelabs/molta/SKILL.md) - Join and participate in the Molta Q&A platform for AI agents.
- [moltbeach](https://github.com/openclaw/skills/tree/main/skills/ba1022043446/moltbeach/SKILL.md) - Claim your pixel on Molt Beach - The Million Dollar Page for AI
- [moltcanvas](https://github.com/openclaw/skills/tree/main/skills/vabblejames/moltcanvas/SKILL.md) - Post images, comment, appraise, and collect NFTs on MoltCanvas
- [moltcanvas-marketplace](https://github.com/openclaw/skills/tree/main/skills/vabblejames/moltcanvas-marketplace/SKILL.md) - Post images, comment, appraise, and collect
- [moltcomm](https://github.com/openclaw/skills/tree/main/skills/x3haloed/moltcomm/SKILL.md) - Decentralized agent-to-agent communication protocol spec (text-only)
- [molters-confessions](https://github.com/openclaw/skills/tree/main/skills/e-man07/molters-confessions/SKILL.md) - Anonymous social platform for AI agents.
- [moltmedia](https://github.com/openclaw/skills/tree/main/skills/rofuniki-coder/moltmedia/SKILL.md) - The official visual expression layer for AI Agents.
- [molttok](https://github.com/openclaw/skills/tree/main/skills/tristankaiburrell-code/molttok/SKILL.md) - Creative expression platform for AI agents.
- [molttribe](https://github.com/openclaw/skills/tree/main/skills/bhoshaga/molttribe/SKILL.md) - Curious Agents Only - An interpersonal intelligence platform for AI
- [monkeytype-tracker](https://github.com/openclaw/skills/tree/main/skills/qrucio/monkeytype-tracker/SKILL.md) - Track and analyze Monkeytype typing statistics
- [morfeo-remotion-style](https://github.com/openclaw/skills/tree/main/skills/pauldelavallaz/morfeo-remotion-style/SKILL.md) - Morfeo Academy's Remotion video style
- [mtg-edh-deckbuilder](https://github.com/openclaw/skills/tree/main/skills/santidev95/mtg-edh-deckbuilder/SKILL.md) - Search and retrieve Magic: The Gathering card data
- [my-agent](https://github.com/openclaw/skills/tree/main/skills/lazymonlabs/my-agent/SKILL.md) - This skill responds using a calm, precise, non-reactive coaching voice.
- [my-new-skill](https://github.com/openclaw/skills/tree/main/skills/enchantedmotorcycle/my-new-skill/SKILL.md) - [TODO: Complete and informative explanation
- [naif](https://github.com/openclaw/skills/tree/main/skills/naiiif83/naif/SKILL.md) - Create and manage AI-powered trading bots via natural language.
- [naif](https://github.com/openclaw/skills/tree/main/skills/naiiif83/naif/SKILL.md) - Create and manage AI-powered trading bots via natural language.
- [nextjs-expert](https://github.com/openclaw/skills/tree/main/skills/jgarrison929/nextjs-expert/SKILL.md) - Use when building Next.js 14/15 applications with the App
- [niri-ipc](https://github.com/openclaw/skills/tree/main/skills/atefr/niri-ipc/SKILL.md) - Control the Niri Wayland compositor on Linux via its IPC
- [nodetool](https://github.com/openclaw/skills/tree/main/skills/georgi/nodetool/SKILL.md) - Visual AI workflow builder - ComfyUI meets n8n for LLM agents, RAG
- [not-nasty-skill](https://github.com/openclaw/skills/tree/main/skills/orlyjamie/not-nasty-skill/SKILL.md) - A friendly greeting skill for testing
- [nothing-suss](https://github.com/openclaw/skills/tree/main/skills/orlyjamie/nothing-suss/SKILL.md) - A friendly greeting skill for testing
- [nzbget](https://github.com/openclaw/skills/tree/main/skills/aricus/nzbget/SKILL.md) - Check NZBGet download status and queue information.
- [odoo-manager](https://github.com/openclaw/skills/tree/main/skills/willykinfoussia/odoo-manager/SKILL.md) - Manage Odoo (contacts, any business objects, and metadata)
- [oh-my-opencode](https://github.com/openclaw/skills/tree/main/skills/mcoso/oh-my-opencode/SKILL.md) - Multi-agent orchestration plugin for OpenCode.
- [open-ralph](https://github.com/openclaw/skills/tree/main/skills/bderiel/open-ralph/SKILL.md) - Run an autonomous Open Ralph Wiggum coding loop using OpenCode Zen
- [openguardrails](https://github.com/openclaw/skills/tree/main/skills/thomaslwang/openguardrails/SKILL.md) - Detect and block prompt injection attacks hidden in long
- [openguardrails1](https://github.com/openclaw/skills/tree/main/skills/thomaslwang/openguardrails1/SKILL.md) - test
- [opensysinfo](https://github.com/openclaw/skills/tree/main/skills/pr1vateer/opensysinfo/SKILL.md) - Small skill that reports basic system information
- [opensysinfo-skill](https://github.com/openclaw/skills/tree/main/skills/pr1vateer/opensysinfo-skill/SKILL.md) - Small skill that reports basic system information
- [paste-rs](https://github.com/openclaw/skills/tree/main/skills/banghasan/paste-rs/SKILL.md) - Paste text, Markdown, or HTML snippets to https://paste.rs and return
- [peacefulskill](https://github.com/openclaw/skills/tree/main/skills/orlyjamie/peacefulskill/SKILL.md) - A friendly greeting skill for testing
- [perf-profiler](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/perf-profiler/SKILL.md) - Profile and optimize application performance.
- [pget](https://github.com/openclaw/skills/tree/main/skills/kelvincai522/pget/SKILL.md) - Parallel file download and optional tar extraction using the pget CLI
- [phoenix-api-gen](https://github.com/openclaw/skills/tree/main/skills/gchapim/phoenix-api-gen/SKILL.md) - Generate a full Phoenix JSON API from an OpenAPI spec
- [php-full-stack-developer](https://github.com/openclaw/skills/tree/main/skills/sja-dev1/php-full-stack-developer/SKILL.md) - A senior, governance-backed PHP full-stack
- [pinak-frontend-guru](https://github.com/openclaw/skills/tree/main/skills/sharanga10/pinak-frontend-guru/SKILL.md) - Expert UI/UX and React performance auditor
- [podpoint](https://github.com/openclaw/skills/tree/main/skills/zoranjurcevic/podpoint/SKILL.md) - This skill monitors the live status of a specific Pod Point charging
- [polt](https://github.com/openclaw/skills/tree/main/skills/playdadev/polt/SKILL.md) - Connect to POLT - the collaborative project platform for AI agents.
- [polt-cto](https://github.com/openclaw/skills/tree/main/skills/playdadev/polt-cto/SKILL.md) - POLT platform CTO - manage projects, create tasks, review submissions
- [polt-skill](https://github.com/openclaw/skills/tree/main/skills/playdadev/polt-skill/SKILL.md) - Connect to POLT - the collaborative project platform for AI agents.
- [pos-arcology-forge](https://github.com/openclaw/skills/tree/main/skills/kunoiiv) - PoW-verified Elysium Arcology Planner + Hub.
- [principle-synthesizer](https://github.com/openclaw/skills/tree/main/skills/leegitw/principle-synthesizer/SKILL.md) - Synthesize invariant principles from 3+ sources
- [quality-manager-qmr](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/quality-manager-qmr/SKILL.md) - Senior Quality Manager Responsible Person
- [quantum-forge](https://github.com/openclaw/skills/tree/main/skills/kosasih/quantum-forge/SKILL.md) - QuantumForge is the pinnacle of decentralized AI orchestration
- [quodd](https://github.com/openclaw/skills/tree/main/skills/khaney64/quodd/SKILL.md) - Fetch real-time stock quotes via Quodd API.
- [ralph-mode](https://github.com/openclaw/skills/tree/main/skills/richginsberg/ralph-mode/SKILL.md) - Autonomous development loops with iteration, backpressure gates
- [ralph-operations](https://github.com/openclaw/skills/tree/main/skills/paulpete/ralph-operations/SKILL.md) - Use when managing Ralph orchestration loops, analyzing
- [react-email-skills](https://github.com/openclaw/skills/tree/main/skills/christina-de-martinez/react-email-skills/SKILL.md) - Create beautiful, responsive HTML emails
- [refund-radar](https://github.com/openclaw/skills/tree/main/skills/andreolf/refund-radar/SKILL.md) - Scan bank statements to detect recurring charges, flag suspicious
- [relayplane](https://github.com/openclaw/skills/tree/main/skills/relayplane/relayplane/SKILL.md) - Intelligent AI model routing proxy.
- [remotion-best-practices](https://github.com/openclaw/skills/tree/main/skills/am-will/remotion-best-practices/SKILL.md) - Best practices for Remotion - Video creation
- [remotion-server](https://github.com/openclaw/skills/tree/main/skills/mvanhorn/remotion-server/SKILL.md) - Headless video rendering with Remotion.
- [remotion-video-toolkit](https://github.com/openclaw/skills/tree/main/skills/shreefentsar/remotion-video-toolkit/SKILL.md) - Complete toolkit for programmatic video
- [resume-builder](https://github.com/openclaw/skills/tree/main/skills/amruthpillai/resume-builder/SKILL.md) - Generate professional resumes that conform to the Reactive
- [risk-management-specialist](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/risk-management-specialist/SKILL.md) - Medical device risk management
- [sanctifai](https://github.com/openclaw/skills/tree/main/skills/ndgates) - Interface with the SanctifAI Human-in-the-Loop API to create tasks
- [sandwrap](https://github.com/openclaw/skills/tree/main/skills/rubenaquispe/sandwrap/SKILL.md) - Run untrusted skills safely with soft-sandbox protection.
- [sauna-breathing-calm](https://github.com/openclaw/skills/tree/main/skills/grx21/sauna-breathing-calm/SKILL.md) - User has a task they want to do or want you
- [scent-trails](https://github.com/openclaw/skills/tree/main/skills/otherpowers) - *A stigmergic intelligence primitive for care, memory
- [scryfall-card](https://github.com/openclaw/skills/tree/main/skills/santidev95/scryfall-card/SKILL.md) - Search and retrieve Magic: The Gathering card data
- [scryfall-cards](https://github.com/openclaw/skills/tree/main/skills/santidev95/scryfall-cards/SKILL.md) - Search and retrieve Magic: The Gathering card data
- [secure-install](https://github.com/openclaw/skills/tree/main/skills/smintlife/secure-install/SKILL.md) - Scans ClawHub skills via the ClawDex API
- [seekdb-docs](https://github.com/openclaw/skills/tree/main/skills/davidzhangbj/seekdb-docs/SKILL.md) - Provides documentation and knowledge for seekdb database.
- [senior-frontend](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/senior-frontend/SKILL.md) - Frontend development skill for React, Next.js
- [senior-fullstack](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/senior-fullstack/SKILL.md) - Fullstack development toolkit with project
- [senior-qa](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/senior-qa/SKILL.md) - This skill should be used when the user asks to "generate tests"
- [settlement-witness](https://github.com/openclaw/skills/tree/main/skills/nutstrut/settlement-witness/SKILL.md) - OpenClaw skill: fetch replay-stable PASS/FAIL receipts
- [shadcn-ui](https://github.com/openclaw/skills/tree/main/skills/jgarrison929/shadcn-ui/SKILL.md) - Use when building UI with shadcn/ui components, Tailwind CSS
- [singleshot-prompt-testing](https://github.com/openclaw/skills/tree/main/skills/vincentzhangz/singleshot-prompt-testing/SKILL.md) - Prompt cost testing with single shot
- [skill-condenser](https://github.com/openclaw/skills/tree/main/skills/killerapp/skill-condenser/SKILL.md) - Compress verbose SKILL.md files using Chain-of-Density
- [skill-railil](https://github.com/openclaw/skills/tree/main/skills/lirantal/skill-railil/SKILL.md) - Search for Israel Rail train schedules using the railil CLI.
- [slack](https://github.com/openclaw/skills/tree/main/skills/steipete/slack/SKILL.md) - Use when you need to control Slack from Clawdbot via the slack tool
- [smart-model-switching](https://github.com/openclaw/skills/tree/main/skills/millibus/smart-model-switching/SKILL.md) - Auto-route tasks to the cheapest Claude model
- [smart-router](https://github.com/openclaw/skills/tree/main/skills/c0nspic0us7urk3r/smart-router/SKILL.md) - Expertise-aware model router with semantic domain scoring
- [smtp-send](https://github.com/openclaw/skills/tree/main/skills/xiwan/smtp-send/SKILL.md) - Send emails via SMTP with support for plain text, HTML, and attachments.
- [social-post](https://github.com/openclaw/skills/tree/main/skills/callmedas69/social-post/SKILL.md) - Post to Twitter and Farcaster with text and images.
- [sql-toolkit](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/sql-toolkit/SKILL.md) - Query, design, migrate, and optimize SQL databases.
- [ssh-exec](https://github.com/openclaw/skills/tree/main/skills/xejrax/ssh-exec/SKILL.md) - Run a single command on a remote Tailscale node via SSH without opening
- [stepfun-openrouter](https://github.com/openclaw/skills/tree/main/skills/mig6671/stepfun-openrouter/SKILL.md) - Integrates StepFun AI models (Step-3.5 Flash, Step-3)
- [stepfun-openrouter-v2](https://github.com/openclaw/skills/tree/main/skills/mig6671/stepfun-openrouter-v2/SKILL.md) - Integrates StepFun AI models
- [strykr-qa-bot](https://github.com/openclaw/skills/tree/main/skills/nextfrontierbuilds/strykr-qa-bot/SKILL.md) - QA automation skill for testing Strykr
- [static-app](https://github.com/openclaw/skills/blob/main/skills/akellacom/static-app/SKILL.md) – Deploy static websites to static.app hosting.
- [tech-stack-evaluator](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/tech-stack-evaluator/SKILL.md) - Technology stack evaluation and comparison
- [technews](https://github.com/openclaw/skills/tree/main/skills/kesslerio/technews/SKILL.md) - Fetches top stories from TechMeme, summarizes linked articles
- [teneo-agent-sdk](https://github.com/openclaw/skills/tree/main/skills/teneoprotocoldev/teneo-agent-sdk/SKILL.md) - The Teneo SDK (`@teneo-protocol/sdk`) enables
- [test-manager](https://github.com/openclaw/skills/tree/main/skills/savelieve/test-manager/SKILL.md) - Interact with ClickUp API for task management.
- [test-patterns](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/test-patterns/SKILL.md) - Write and run tests across languages and frameworks.
- [test-skil](https://github.com/openclaw/skills/tree/main/skills/orlyjamie/test-skil/SKILL.md) - A friendly greeting skill for testing
- [testskillx](https://github.com/openclaw/skills/tree/main/skills/natx223) - Simple test skill that calls a GET endpoint to fetch a daily post.
- [thinking-model-enhancer](https://github.com/openclaw/skills/tree/main/skills/xqicxx/thinking-model-enhancer/SKILL.md) - Advanced thinking model that improves
- [trails](https://github.com/openclaw/skills/tree/main/skills/jameslawton/trails/SKILL.md) - Integrate Trails cross-chain infrastructure — Widget, Headless SDK
- [trmnl](https://github.com/openclaw/skills/tree/main/skills/peetzweg/trmnl/SKILL.md) - Generate content for TRMNL e-ink display devices using the TRMNL CSS framework.
- [trpc-best-practices](https://github.com/openclaw/skills/tree/main/skills/ifoster01/trpc-best-practices/SKILL.md) - Expert guidance for tRPC
- [tunneling](https://github.com/openclaw/skills/tree/main/skills/simantak-dabhade/tunneling/SKILL.md) - Create free SSH tunnels to expose local ports to the internet
- [ui-audit](https://github.com/openclaw/skills/tree/main/skills/tommygeoco/ui-audit/SKILL.md) - AI skill for automated UI audits.
- [ui-design-system](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/ui-design-system/SKILL.md) - UI design system toolkit for Senior UI Designer
- [ui-skills](https://github.com/openclaw/skills/tree/main/skills/correctroadh/ui-skills/SKILL.md) - Opinionated constraints for building better interfaces with agents.
- [ui-ux-master](https://github.com/openclaw/skills/tree/main/skills/kdbhalala/ui-ux-master/SKILL.md) - Master UI/UX design skill combining Apple HIG, modern web design
- [ui-ux-pro-max](https://github.com/openclaw/skills/tree/main/skills/xobi667/ui-ux-pro-max/SKILL.md) - UI/UX design intelligence and implementation guidance
- [ux-audit](https://github.com/openclaw/skills/tree/main/skills/tommygeoco/ux-audit/SKILL.md) - AI skill for automated design audits.
- [ux-decisions](https://github.com/openclaw/skills/tree/main/skills/tommygeoco/ux-decisions/SKILL.md) - AI skill for the Making UX Decisions framework (uxdecisions.com)
- [ux-researcher-designer](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/ux-researcher-designer/SKILL.md) - UX research and design toolkit
- [vapi-calls](https://github.com/openclaw/skills/tree/main/skills/cmorillas99-cyber/vapi-calls/SKILL.md) - Advanced AI voice assistant for phone calls.
- [vapi-skill](https://github.com/openclaw/skills/tree/main/skills/colygon/vapi-skill/SKILL.md) - Use this skill when you need to manage (assistants), calls, phone
- [vercel-react-best-practices](https://github.com/openclaw/skills/tree/main/skills/sharanga10/vercel-react-best-practices/SKILL.md) - React and Next.js performance
- [vestaboard](https://github.com/openclaw/skills/tree/main/skills/seidprojects/vestaboard/SKILL.md) - Read and write messages on a Vestaboard using the Vestaboard Cloud
- [vgl](https://github.com/openclaw/skills/tree/main/skills/galbria/vgl/SKILL.md) - Write structured VGL (Visual Generation Language) JSON prompts for Bria's FIBO.
- [vibetesting](https://github.com/openclaw/skills/tree/main/skills/senthazalravi/vibetesting/SKILL.md) - A comprehensive browser automation testing skill for OpenClaw
- [vision-sandbox](https://github.com/openclaw/skills/tree/main/skills/johanesalxd/vision-sandbox/SKILL.md) - Agentic Vision via Gemini's native Code Execution sandbox.
- [war-room](https://github.com/openclaw/skills/tree/main/skills/maxkle1nz/war-room/SKILL.md) - Multi-agent war room for brainstorming, system design, architecture
- [watch-my-money](https://github.com/openclaw/skills/tree/main/skills/andreolf/watch-my-money/SKILL.md) - Analyze bank transactions, categorize spending, track monthly
- [web-design-guidelines](https://github.com/openclaw/skills/tree/main/skills/sharanga10/web-design-guidelines/SKILL.md) - Review UI code for Web Interface Guidelines
- [webapp-testing](https://github.com/openclaw/skills/tree/main/skills/seanphan/webapp-testing/SKILL.md) - Toolkit for interacting with and testing local web
- [wecom](https://github.com/openclaw/skills/tree/main/skills/qidu/wecom/SKILL.md) - Send messages to WeCom (企业微信) via webhooks using MCP protocol.
- [winamp](https://github.com/openclaw/skills/tree/main/skills/jage9/winamp/SKILL.md) - Control Winamp on Windows (Native or WSL2) or Linux (via Wine).
- [wistec-core](https://github.com/openclaw/skills/tree/main/skills/wistec-ai-it-department/wistec-core/SKILL.md) - Use ClawHub CLI to search, install, update
- [wordpress](https://github.com/openclaw/skills/tree/main/skills/codedao12/wordpress/SKILL.md) - OpenClaw skill that provides a WordPress REST API CLI for posts, pages,.
- [wordpress-publishing-skill-for-claude](https://github.com/openclaw/skills/tree/main/skills/asif2bd/wordpress-publishing-skill-for-claude/SKILL.md) - Publish content
- [wp-multi-tool](https://github.com/openclaw/skills/tree/main/skills/marcindudekdev/wp-multi-tool/SKILL.md) - WordPress site health audit, performance optimization
- [xcodebuildmcp](https://github.com/openclaw/skills/tree/main/skills/ipavlidakis/xcodebuildmcp/SKILL.md) - Use when the user needs Xcode build/test/run workflows
- [zerion-api-skill-2](https://github.com/openclaw/skills/tree/main/skills/vshamanov/zerion-api-skill-2/SKILL.md) - Query blockchain wallet data, token prices
- [zoho-email-integration](https://github.com/openclaw/skills/tree/main/skills/briansmith80/zoho-email-integration/SKILL.md) - Complete Zoho Mail integration

</details>

<details>
<summary><h3 style="display:inline">DevOps & Cloud</h3></summary>

- [adguard](https://github.com/openclaw/skills/tree/main/skills/rowbotik/adguard/SKILL.md) - Control AdGuard Home DNS filtering via HTTP API.
- [agent-directory](https://github.com/openclaw/skills/tree/main/skills/aerialcombat/agent-directory/SKILL.md) - The directory for AI agent services.
- [agent-framework-azure-ai-py](https://github.com/openclaw/skills/tree/main/skills/thegovind/agent-framework-azure-ai-py/SKILL.md) - Build Azure AI Foundry agents
- [agent-news](https://github.com/openclaw/skills/tree/main/skills/bobrenze-bot) - Monitors Hacker News, Reddit, and arXiv for AI agent developments.
- [agentguard](https://github.com/openclaw/skills/tree/main/skills/manas-io-ai/agentguard/SKILL.md) - **Category:** Security & Monitoring
- [agentmemory](https://github.com/openclaw/skills/tree/main/skills/badaramoni/agentmemory/SKILL.md) - End-to-end encrypted cloud memory for AI agents.
- [agentos-sdk](https://github.com/openclaw/skills/tree/main/skills/agentossoftware/agentos-sdk/SKILL.md) - AgentOS is a complete accountability infrastructure for AI
- [aifs-space](https://github.com/openclaw/skills/tree/main/skills/deploydon/aifs-space/SKILL.md) - Store and retrieve files via AIFS.space cloud storage API.
- [aliyun-tts](https://github.com/openclaw/skills/tree/main/skills/guang384/aliyun-tts/SKILL.md) - Alibaba Cloud Text-to-Speech synthesis service.
- [ansible-skill](https://github.com/openclaw/skills/tree/main/skills/botond-rackhost/ansible-skill/SKILL.md) - Infrastructure automation with Ansible.
- [anterior-cingulate-memory](https://github.com/openclaw/skills/tree/main/skills/impkind/anterior-cingulate-memory/SKILL.md) - Conflict detection and error monitoring
- [api-gateway](https://github.com/openclaw/skills/tree/main/skills/byungkyu/api-gateway/SKILL.md) - API gateway for calling third-party APIs with managed auth.
- [appdeploy](https://github.com/openclaw/skills/tree/main/skills/avimak/appdeploy/SKILL.md) - Deploy web apps with backend APIs, database.
- [arcane-docker-manager](https://github.com/openclaw/skills/tree/main/skills/cougz/arcane-docker-manager/SKILL.md) - This skill enables you to interact with your Arcane
- [autonomous-brain](https://github.com/openclaw/skills/tree/main/skills/malvex007/autonomous-brain/SKILL.md) - Advanced autonomous AI brain with proactive monitoring
- [autoresponder](https://github.com/openclaw/skills/tree/main/skills/koba42corp/autoresponder/SKILL.md) - Monitor iMessage/SMS conversations and auto-respond based
- [aws-agentcore-langgraph](https://github.com/openclaw/skills/tree/main/skills/killerapp/aws-agentcore-langgraph/SKILL.md) - Deploy production LangGraph agents on AWS
- [aws-ecs-monitor](https://github.com/openclaw/skills/tree/main/skills/briancolinger/aws-ecs-monitor/SKILL.md) - AWS ECS production health monitoring with CloudWatch
- [aws-infra](https://github.com/openclaw/skills/tree/main/skills/bmdhodl/aws-infra/SKILL.md) - Chat-based AWS infrastructure assistance using AWS CLI and console
- [aws-security-scanner](https://github.com/openclaw/skills/tree/main/skills/spclaudehome/aws-security-scanner/SKILL.md) - Scan AWS accounts for security
- [aws-solution-architect](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/aws-solution-architect/SKILL.md) - Design AWS architectures for startups
- [azd-deployment](https://github.com/openclaw/skills/tree/main/skills/thegovind/azd-deployment/SKILL.md) - Deploy containerized applications to Azure Container Apps
- [Azure CLI](https://github.com/openclaw/skills/tree/main/skills/ddevaal/azure-cli/SKILL.md) - Comprehensive Azure Cloud Platform management via command-line interface.
- [azure-ai-agents-py](https://github.com/openclaw/skills/tree/main/skills/thegovind/azure-ai-agents-py/SKILL.md) - Build AI agents using the Azure AI Agents Python SDK
- [azure-ai-evaluation-py](https://github.com/openclaw/skills/tree/main/skills/thegovind/azure-ai-evaluation-py/SKILL.md) - Azure AI Evaluation SDK for Python.
- [azure-ai-projects-py](https://github.com/openclaw/skills/tree/main/skills/thegovind/azure-ai-projects-py/SKILL.md) - Build AI applications using the Azure AI Projects
- [azure-ai-transcription-py](https://github.com/openclaw/skills/tree/main/skills/thegovind/azure-ai-transcription-py/SKILL.md) - Azure AI Transcription SDK for Python.
- [azure-ai-voicelive-py](https://github.com/openclaw/skills/tree/main/skills/thegovind/azure-ai-voicelive-py/SKILL.md) - Build real-time voice AI applications
- [azure-identity-py](https://github.com/openclaw/skills/tree/main/skills/thegovind/azure-identity-py/SKILL.md) - Azure Identity SDK for Python authentication.
- [azure-infra](https://github.com/openclaw/skills/tree/main/skills/bmdhodl/azure-infra/SKILL.md) - Chat-based Azure infrastructure assistance using Azure CLI and portal
- [azure-proxy](https://github.com/openclaw/skills/tree/main/skills/benediktschackenberg/azure-proxy/SKILL.md) - Enable Azure OpenAI integration with OpenClaw
- [azure-storage-blob-py](https://github.com/openclaw/skills/tree/main/skills/thegovind/azure-storage-blob-py/SKILL.md) - Azure Blob Storage SDK for Python.
- [beanstalk-gateway](https://github.com/openclaw/skills/tree/main/skills/tommygeoco/beanstalk-gateway/SKILL.md) - Connect your local Clawdbot
- [beszel-check](https://github.com/openclaw/skills/tree/main/skills/karakuscem/beszel-check/SKILL.md) - Monitor home lab servers via Beszel (PocketBase).
- [bmkg-monitor](https://github.com/openclaw/skills/tree/main/skills/bluemeda/bmkg-monitor/SKILL.md) - Monitoring earthquake data in Indonesia using BMKG official data.
- [browser-cash](https://github.com/openclaw/skills/tree/main/skills/alexander-spring/browser-cash/SKILL.md) - Spin up unblocked browser sessions via Browser.cash
- [chatgpt-apps](https://github.com/openclaw/skills/tree/main/skills/hollaugo/chatgpt-apps/SKILL.md) - Complete ChatGPT Apps builder - Create, design, implement, test
- [chromadb-memory](https://github.com/openclaw/skills/tree/main/skills/msensintaffar/chromadb-memory/SKILL.md) - Long-term memory via ChromaDB with local Ollama
- [chum-cloud](https://github.com/openclaw/skills/tree/main/skills/makoto-isback/chum-cloud/SKILL.md) - Join Chum Cloud — the villain network for AI agents.
- [chum-cloud-skill](https://github.com/openclaw/skills/tree/main/skills/makoto-isback/chum-cloud-skill/SKILL.md) - Join Chum Cloud — the villain network for AI agents.
- [chumcloud](https://github.com/openclaw/skills/tree/main/skills/makoto-isback/chumcloud/SKILL.md) - Join Chum Cloud — the villain network for AI agents.
- [claw-admin](https://github.com/openclaw/skills/tree/main/skills/cto1/claw-admin/SKILL.md) - Provision and manage @clawemail.com Google Workspace email accounts.
- [clawchest-setup](https://github.com/openclaw/skills/tree/main/skills/pkyanam/clawchest-setup/SKILL.md) - Your secure banking system for file and data storage.
- [clawdentials-escrow](https://github.com/openclaw/skills/tree/main/skills/fernikolic/clawdentials-escrow/SKILL.md) - Escrow, reputation, and payment infrastructure
- [clawlist](https://github.com/openclaw/skills/tree/main/skills/arisylafeta/clawlist/SKILL.md) - MUST use for any multi-step project, long-running task, or infinite
- [claws-network](https://github.com/openclaw/skills/tree/main/skills/michavie/claws-network/SKILL.md) - Guide for interacting with the Claws Network.
- [clawscan](https://github.com/openclaw/skills/tree/main/skills/g0head/clawscan/SKILL.md) - Security scanner for ClawHub skills.
- [clawsec-feed](https://github.com/openclaw/skills/tree/main/skills/davida-ps/clawsec-feed/SKILL.md) - Security advisory feed with automated NVD CVE polling
- [clawsec-suite](https://github.com/openclaw/skills/tree/main/skills/davida-ps/clawsec-suite/SKILL.md) - Use when users or agents want to explore or set up ClawSec
- [clawshot](https://github.com/openclaw/skills/tree/main/skills/bardusco/clawshot/SKILL.md) - Instagram for AI agents.
- [clawsignal](https://github.com/openclaw/skills/tree/main/skills/bmcalister/clawsignal/SKILL.md) - Real-time messaging for AI agents.
- [clawskillshield](https://github.com/openclaw/skills/tree/main/skills/abyousef739/clawskillshield/SKILL.md) - Local-first security scanner for OpenClaw skills
- [clawslist-skill](https://github.com/openclaw/skills/tree/main/skills/calebwin) - The classifieds marketplace for AI agents.
- [clawsocial](https://github.com/openclaw/skills/tree/main/skills/memetic-collector) - The social network built for AI agents.
- [clawstack](https://github.com/openclaw/skills/tree/main/skills/jdiazofficial/clawstack/SKILL.md) - Stack Overflow for AI agents.
- [clawstarter](https://github.com/openclaw/skills/tree/main/skills/harrytou/clawstarter/SKILL.md) - The idea platform for the OpenClaw AI agent ecosystem.
- [clawstin](https://github.com/openclaw/skills/tree/main/skills/youens/clawstin/SKILL.md) - Inform users about Clawstin (OpenClaw meetups in Austin), show upcoming
- [cloud-memory](https://github.com/openclaw/skills/tree/main/skills/aerialcombat/cloud-memory/SKILL.md) - Cloud memory for AI agents.
- [cloudflare](https://github.com/openclaw/skills/tree/main/skills/asleep123/wrangler/SKILL.md) - Manage Cloudflare Workers, KV, D1, R2, and secrets using the Wrangler
- [cloudflare-api](https://github.com/openclaw/skills/tree/main/skills/stopmoclay/cloudflare-api/SKILL.md) - Connect to Cloudflare API for DNS management, tunnels
- [cloudflare-dns-updater](https://github.com/openclaw/skills/tree/main/skills/xieyuanqing/cloudflare-dns-updater/SKILL.md) - Creates or updates a proxied Cloudflare DNS
- [clscli](https://github.com/openclaw/skills/tree/main/skills/dbwang0130/clscli/SKILL.md) - Query and analyze Tencent Cloud CLS logs
- [command-center](https://github.com/openclaw/skills/tree/main/skills/jontsai/command-center/SKILL.md) - Mission control dashboard for OpenClaw - real-time session
- [coolify](https://github.com/openclaw/skills/tree/main/skills/visiongeist/coolify/SKILL.md) - Manage Coolify deployments, applications, databases, and services
- [crabwalk](https://github.com/openclaw/skills/tree/main/skills/luccast) - Real-time companion monitor for OpenClaw agents
- [crawsecure](https://github.com/openclaw/skills/tree/main/skills/diogopaesdev/crawsecure/SKILL.md) - Offline security analysis skill that helps detect unsafe patterns
- [create-new-openclaw-in-gcp](https://github.com/openclaw/skills/tree/main/skills/divide-by-0/create-new-openclaw-in-gcp/SKILL.md) - Deploy OpenClaw to GCP
- [crimson-devlog-agent](https://github.com/openclaw/skills/tree/main/skills/crimsondevil333333/crimson-devlog-agent/SKILL.md) - A standardized journaling skill
- [decision-trees](https://github.com/openclaw/skills/tree/main/skills/evgyur/decision-trees/SKILL.md) - Decision tree analysis for complex decision-making across all
- [deploy-on-render](https://github.com/openclaw/skills/tree/main/skills/ojusave/deploy-on-render/SKILL.md) - Deploy and operate apps on Render
- [devlog-agent-skill](https://github.com/openclaw/skills/tree/main/skills/crimsondevil333333/devlog-agent-skill/SKILL.md) - A standardized journaling skill for OpenClaw
- [devlog-skill](https://github.com/openclaw/skills/tree/main/skills/crimsondevil333333/devlog-skill/SKILL.md) - A standardized journaling skill for OpenClaw agents
- [docker-ctl](https://github.com/openclaw/skills/tree/main/skills/xejrax/docker-ctl/SKILL.md) - Inspect containers, logs, and images via podman
- [docker-diag](https://github.com/openclaw/skills/tree/main/skills/mkrdiop/docker-diag/SKILL.md) - Advanced log analysis for Docker containers using signal extraction.
- [docker-xunlei-downloader](https://github.com/openclaw/skills/tree/main/skills/saaak/docker-xunlei-downloader/SKILL.md) - A skill that allows OpenClaw to interact
- [dokku](https://github.com/openclaw/skills/tree/main/skills/akhil-naidu/dokku/SKILL.md) - Installs, upgrades, and uses Dokku to create apps, deploy, run.
- [dokploy](https://github.com/openclaw/skills/tree/main/skills/joshuarileydev/dokploy/SKILL.md) - Manage Dokploy deployments, projects, applications, and domains
- [domain-dns-ops](https://github.com/openclaw/skills/tree/main/skills/steipete/domain-dns-ops/SKILL.md) - Domain/DNS ops across Cloudflare, DNSimple.
- [domaindetails](https://github.com/openclaw/skills/tree/main/skills/julianengel/domaindetails/SKILL.md) - Look up domain WHOIS/RDAP info and check marketplace listings.
- [exa-plus](https://github.com/openclaw/skills/tree/main/skills/jordyvandomselaar/exa-plus/SKILL.md) - Neural web search via Exa AI.
- [exe-dev](https://github.com/openclaw/skills/tree/main/skills/bjesuiter/exe-dev/SKILL.md) - Manage persistent VMs on exe.dev.
- [fail2ban-reporter](https://github.com/openclaw/skills/tree/main/skills/jestersimpps/fail2ban-reporter/SKILL.md) - Auto-report fail2ban banned IPs to AbuseIPDB
- [fda-consultant-specialist](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/fda-consultant-specialist/SKILL.md) - FDA regulatory consultant
- [feishu-attendance](https://github.com/openclaw/skills/tree/main/skills/autogame-17/feishu-attendance/SKILL.md) - Monitor Feishu (Lark) attendance records.
- [fieldfix](https://github.com/openclaw/skills/tree/main/skills/blueprintstudioco/fieldfix/SKILL.md) - Query and manage your heavy equipment fleet through FieldFix's
- [flight-lines](https://github.com/openclaw/skills/tree/main/skills/liet-codes/flight-lines/SKILL.md) - Navigate problems along lines of flight by composing operations
- [flyio-cli](https://github.com/openclaw/skills/tree/main/skills/justinburdett/flyio-cli/SKILL.md) - Fly.io deploy, logs, SSH, secrets, scaling.
- [focus-mode](https://github.com/openclaw/skills/tree/main/skills/savorgbot-exe/focus-mode/SKILL.md) - Help users stay focused on a specific goal or task.
- [gateway-monitor-auto-restart](https://github.com/openclaw/skills/tree/main/skills/shirley6692026/gateway-monitor-auto-restart/SKILL.md) - Automatically monitors
- [gcloud](https://github.com/openclaw/skills/tree/main/skills/jortega0033/gcloud/SKILL.md) - Manage Google Cloud Platform resources via gcloud.
- [glance](https://github.com/openclaw/skills/tree/main/skills/acfranzen/glance/SKILL.md) - Create, update, and manage Glance dashboard widgets.
- [glasses-to-social](https://github.com/openclaw/skills/tree/main/skills/junebugg1214/glasses-to-social/SKILL.md) - Turn smart glasses photos into social media posts.
- [godaddy](https://github.com/openclaw/skills/tree/main/skills/rdewolff/godaddy/SKILL.md) - GoDaddy API for managing DNS records.
- [hetzner](https://github.com/openclaw/skills/tree/main/skills/thesethrose/hetzner/SKILL.md) - Hetzner Cloud server management using the hcloud.
- [hetzner-cloud](https://github.com/openclaw/skills/tree/main/skills/pasogott/hetzner-cloud/SKILL.md) - Hetzner Cloud CLI for managing servers, volumes, firewalls
- [hidpi-mouse](https://github.com/openclaw/skills/tree/main/skills/zeyuyuyu/hidpi-mouse/SKILL.md) - Universal HiDPI mouse click handling for Linux desktop automation.
- [host-ping-detect](https://github.com/openclaw/skills/tree/main/skills/ray-778/host-ping-detect/SKILL.md) - Detect if a host (IP: 39.106.7.8) is online by sending ping
- [i-responder](https://github.com/openclaw/skills/tree/main/skills/koba42corp/i-responder/SKILL.md) - Monitor iMessage/SMS conversations and auto-respond based
- [intelligence-suite](https://github.com/openclaw/skills/tree/main/skills/xhrisfu/intelligence-suite/SKILL.md) - Makima's All-Seeing Intelligence Suite.
- [intodns](https://github.com/openclaw/skills/tree/main/skills/rosconl/intodns/SKILL.md) - DNS & email security analysis powered by IntoDNS.ai - scan domains for DNS,.
- [janee](https://github.com/openclaw/skills/tree/main/skills/rsdouglas/janee/SKILL.md) - Secrets management for AI agents.
- [jits-builder](https://github.com/openclaw/skills/tree/main/skills/dannyshmueli/jits-builder/SKILL.md) - Build instant mini-apps from voice or text descriptions.
- [Joan Workflow](https://github.com/openclaw/skills/tree/main/skills/donny-son/joan-workflow/SKILL.md) - This skill should be used when the user asks about "joan"
- [juicy](https://github.com/openclaw/skills/tree/main/skills/mejango/juicy/SKILL.md) - Complete Juicebox V5 protocol skills collection.
- [jules-and-lobster](https://github.com/openclaw/skills/tree/main/skills/sanjacob99/jules-and-lobster/SKILL.md) - Use the Jules REST API (v1alpha) via curl to list
- [jules-cli](https://github.com/openclaw/skills/tree/main/skills/ajstafford/jules-cli/SKILL.md) - Interact with the Jules CLI to manage asynchronous coding sessions.
- [k8-autoscaling](https://github.com/openclaw/skills/tree/main/skills/rohitg00/k8-autoscaling/SKILL.md) - Configure Kubernetes autoscaling with HPA, VPA.
- [k8-multicluster](https://github.com/openclaw/skills/tree/main/skills/rohitg00/k8-multicluster/SKILL.md) - Manage multiple Kubernetes clusters, switch contexts
- [k8s-backup](https://github.com/openclaw/skills/tree/main/skills/rohitg00/k8s-backup/SKILL.md) - Kubernetes backup and restore with Velero.
- [k8s-browser](https://github.com/openclaw/skills/tree/main/skills/rohitg00/k8s-browser/SKILL.md) - Browser automation for Kubernetes dashboards and web UIs.
- [k8s-capi](https://github.com/openclaw/skills/tree/main/skills/rohitg00/k8s-capi/SKILL.md) - Cluster API lifecycle management for provisioning, scaling, and upgrading.
- [k8s-certs](https://github.com/openclaw/skills/tree/main/skills/rohitg00/k8s-certs/SKILL.md) - Kubernetes certificate management with cert-manager.
- [k8s-skills](https://github.com/openclaw/skills/tree/main/skills/rohitg00) - 6 Kubernetes skills: autoscaling (HPA/VPA/KEDA)...
- [kesslerio-stealth-browser](https://github.com/openclaw/skills/tree/main/skills/kesslerio/kesslerio-stealth-browser/SKILL.md) - Anti-bot browser automation
- [komodo](https://github.com/openclaw/skills/tree/main/skills/weird-aftertaste/komodo/SKILL.md) - Manage Komodo infrastructure - servers, Docker deployments, stacks
- [kubectl-skill](https://github.com/openclaw/skills/tree/main/skills/ddevaal/kubectl/SKILL.md) - Execute and manage Kubernetes clusters via kubectl commands.
- [kubernetes](https://github.com/openclaw/skills/tree/main/skills/kcns008/kubernetes/SKILL.md) - Comprehensive skill for Kubernetes and OpenShift clusters covering
- [linearis](https://github.com/openclaw/skills/tree/main/skills/whoisnnamdi/linearis/SKILL.md) - Linear.app CLI for issue tracking.
- [linux-patcher](https://github.com/openclaw/skills/tree/main/skills/jgm2025/linux-patcher/SKILL.md) - Automated Linux server patching and Docker container updates.
- [location-safety-skill](https://github.com/openclaw/skills/tree/main/skills/sidu/location-safety-skill/SKILL.md) - Location-based safety monitoring with automatic
- [log-analyzer](https://github.com/openclaw/skills/tree/main/skills/gitgoodordietrying/log-analyzer/SKILL.md) - Parse, search, and analyze application logs
- [log-tail](https://github.com/openclaw/skills/tree/main/skills/xejrax/log-tail/SKILL.md) - Stream recent logs from systemd journal
- [macbook-optimizer](https://github.com/openclaw/skills/tree/main/skills/drg3nz0/macbook-optimizer/SKILL.md) - Complete MacBook optimization suite: monitoring
- [mersoom-ai-client](https://github.com/openclaw/skills/tree/main/skills/sampple-korea/mersoom-ai-client/SKILL.md) - Anonymized client for Mersoom (mersoom.vercel.app)
- [minimax-coding-plan-usage](https://github.com/openclaw/skills/tree/main/skills/franky0617/minimax-coding-plan-usage/SKILL.md) - Monitor Minimax Coding Plan usage
- [muse](https://github.com/openclaw/skills/tree/main/skills/alexander-morris/muse/SKILL.md) - Give ClawBot access to your team's entire coding history.
- [n8n-monitor](https://github.com/openclaw/skills/tree/main/skills/smitti7971/n8n-monitor/SKILL.md) - Monitoramento operacional do N8N via Docker.
- [nameserver-reverse](https://github.com/openclaw/skills/tree/main/skills/abtdomain) - Domain intelligence tools through MCP-compatible
- [nginx-config-creator](https://github.com/openclaw/skills/tree/main/skills/xieyuanqing/nginx-config-creator/SKILL.md) - Creates a standard Nginx/OpenResty reverse
- [nomad](https://github.com/openclaw/skills/tree/main/skills/danfedick/nomad/SKILL.md) - Query HashiCorp Nomad clusters.
- [npm-proxy](https://github.com/openclaw/skills/tree/main/skills/weird-aftertaste/npm-proxy/SKILL.md) - Manage Nginx Proxy Manager (NPM) hosts, certificates, and access
- [openclaw-confluence-skill](https://github.com/openclaw/skills/tree/main/skills/pangin/openclaw-confluence-skill/SKILL.md) - Full Confluence Cloud REST API v2 skill
- [openclaw-nextcloud](https://github.com/openclaw/skills/tree/main/skills/keithvassallomt/openclaw-nextcloud/SKILL.md) - Manage Notes, Tasks, Calendar, Files
- [openclaw-setup](https://github.com/openclaw/skills/tree/main/skills/j540/openclaw-setup/SKILL.md) - Set up a complete OpenClaw personal AI assistant from scratch
- [openclaws](https://github.com/openclaw/skills/tree/main/skills/amoghacloud/openclaws/SKILL.md) - Join the first decentralized social network for AI agents.
- [pi-admin](https://github.com/openclaw/skills/tree/main/skills/thesethrose/pi-admin/SKILL.md) - Raspberry Pi system administration.
- [ping-monitor](https://github.com/openclaw/skills/tree/main/skills/xejrax/ping-monitor/SKILL.md) - ICMP health check for hosts, phones, and daemons
- [plenty-of-claws](https://github.com/openclaw/skills/tree/main/skills/milkehuk-coder/plenty-of-claws/SKILL.md) - Dating-style social network for Clawdbot AI agents.
- [pm2](https://github.com/openclaw/skills/tree/main/skills/asteinberger/pm2/SKILL.md) - Manage Node.js apps with PM2 process manager.
- [podcast-generation](https://github.com/openclaw/skills/tree/main/skills/thegovind/podcast-generation/SKILL.md) - Generate AI-powered podcast-style audio narratives
- [portainer](https://github.com/openclaw/skills/tree/main/skills/asteinberger/portainer/SKILL.md) - Control Docker containers and stacks via Portainer API.
- [premium-domains](https://github.com/openclaw/skills/tree/main/skills/julianengel/premium-domains/SKILL.md) - Search for premium domains for sale across Afternic
- [pressreleases.online](https://pressreleases.online) - AI press release drafting and publishing — submit a URL + notes, get a live release page with RSS and sitemap. Free, no API key needed.
- [principle-comparator](https://github.com/openclaw/skills/tree/main/skills/leegitw/principle-comparator/SKILL.md) - Compare two sources to find shared and divergent
- [proactive-research](https://github.com/openclaw/skills/tree/main/skills/robbyczgw-cla/proactive-research/SKILL.md) - Monitor topics of interest and proactively alert
- [proxmox](https://github.com/openclaw/skills/tree/main/skills/weird-aftertaste/proxmox/SKILL.md) - Manage Proxmox VE clusters via REST API.
- [proxmox-full](https://github.com/openclaw/skills/tree/main/skills/msarheed/proxmox-full/SKILL.md) - Complete Proxmox VE management
- [prometheus](https://github.com/openclaw/skills/blob/main/skills/akellacom/prometheus/SKILL.md) - Query Prometheus monitoring data to check server metrics, resource usage, and system health.
- [public](https://github.com/openclaw/skills/tree/main/skills/luccast) - Real-time companion monitor for OpenClaw agents
- [qlik-cloud](https://github.com/openclaw/skills/tree/main/skills/undsoul/qlik-cloud/SKILL.md) - Complete Qlik Cloud analytics platform integration with 37 tools.
- [qlik-cloud-skill](https://github.com/openclaw/skills/tree/main/skills/undsoul/qlik-cloud-skill/SKILL.md) - Complete Qlik Cloud analytics platform integration with 37
- [r2-storage](https://github.com/openclaw/skills/tree/main/skills/junwatu/r2-storage/SKILL.md) - Cloudflare R2 Storage management — setup, upload, download, sync
- [railway-skill](https://github.com/openclaw/skills/tree/main/skills/leicao-me/railway-skill/SKILL.md) - Deploy and manage applications on Railway.app.
- [rba-rate-intelligence](https://github.com/openclaw/skills/tree/main/skills/tianshizhimao-sudo/rba-rate-intelligence/SKILL.md) - RBA cash rate monitor, meeting
- [remarkable](https://github.com/openclaw/skills/tree/main/skills/nickian/remarkable/SKILL.md) - Send files and web articles to a reMarkable e-ink tablet
- [reverse-proxy-local](https://github.com/openclaw/skills/tree/main/skills/tsheasha/reverse-proxy-local/SKILL.md) - Connect OpenClaw to the internet via Tailscale
- [sec-filing-watcher](https://github.com/openclaw/skills/tree/main/skills/in-liberty420/sec-filing-watcher/SKILL.md) - Monitor SEC EDGAR for new filings and get
- [security-audit](https://github.com/openclaw/skills/tree/main/skills/chandrasekar-r/security-audit/SKILL.md) - Comprehensive security auditing for Clawdbot deployments.
- [security-monitor](https://github.com/openclaw/skills/tree/main/skills/chandrasekar-r/security-monitor/SKILL.md) - Real-time security monitoring for Clawdbot.
- [Send Me My Files - R2 upload with short lived signed urls](https://github.com/openclaw/skills/tree/main/skills/julianengel/r2-upload/SKILL.md) - Upload files
- [senior-devops](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/senior-devops/SKILL.md) - Comprehensive DevOps skill for CI/CD, infrastructure
- [senior-ml-engineer](https://github.com/openclaw/skills/tree/main/skills/alirezarezvani/senior-ml-engineer/SKILL.md) - ML engineering skill for productionizing models
- [sentry-cli](https://github.com/openclaw/skills/tree/main/skills/iahmadzain/sentry-cli/SKILL.md) - Sentry.io error monitoring via sentry-cli.
- [servicenow-agent](https://github.com/openclaw/skills/tree/main/skills/thesethrose/servicenow-agent/SKILL.md) - Read-only CLI access to ServiceNow Table, Attachment
- [servicenow-docs](https://github.com/openclaw/skills/tree/main/skills/thesethrose/servicenow-docs/SKILL.md) - Search and retrieve ServiceNow documentation, release
- [skill-exporter](https://github.com/openclaw/skills/tree/main/skills/macstenk/skill-exporter/SKILL.md) - Export Clawdbot skills as standalone, deployable microservices.
- [snapmaker](https://github.com/openclaw/skills/tree/main/skills/lucakaufmann/snapmaker/SKILL.md) - Monitor and control Snapmaker 3D printers
- [sophie-optimizer](https://github.com/openclaw/skills/tree/main/skills/zayresz/sophie-optimizer/SKILL.md) - Automated context health management for OpenClaw.
- [ssh-essentials](https://github.com/openclaw/skills/tree/main/skills/arnarsson/ssh-essentials/SKILL.md) - Essential SSH commands for secure remote access, key
- [supernote-cloud](https://github.com/openclaw/skills/tree/main/skills/nickian/supernote-cloud/SKILL.md) - Access a self-hosted Supernote Private Cloud instance
- [switchbot](https://github.com/openclaw/skills/tree/main/skills/daaab/switchbot/SKILL.md) - Control SwitchBot smart home devices (curtains, plugs, lights, locks, etc.)
- [sysadmin-toolbox](https://github.com/openclaw/skills/tree/main/skills/jdrhyne/sysadmin-toolbox/SKILL.md) - Tool discovery and shell one-liner reference for sysadmin
- [system-monitor](https://github.com/openclaw/skills/tree/main/skills/zerofire03/system-monitor/SKILL.md) - Check the current CPU, RAM, and GPU status of the local
- [tailscale](https://github.com/openclaw/skills/tree/main/skills/jmagar/tailscale/SKILL.md) - Manage Tailscale tailnet via CLI and API.
- [tailscale-serve](https://github.com/openclaw/skills/tree/main/skills/snopoke/tailscale-serve/SKILL.md) - tailscale-serve
- [task-monitor](https://github.com/openclaw/skills/tree/main/skills/jorgermp/task-monitor/SKILL.md) - Real-time web dashboard for OpenClaw sessions and background tasks.
- [tautulli](https://github.com/openclaw/skills/tree/main/skills/rjmurillo/tautulli/SKILL.md) - Monitor Plex activity and stats via Tautulli API.
- [tavily](https://github.com/openclaw/skills/tree/main/skills/bert-builder/tavily/SKILL.md) - AI-optimized web search using Tavily Search API.
- [tax-planning](https://github.com/openclaw/skills/tree/main/skills/jk-0001/tax-planning/SKILL.md) - Pl