# s8 解读卡片预览（593/593 张，star 降序）

> 生成于试批进行中时为快照；重跑 `python s8_view.py` 刷新

## openclaw/openclaw（⭐392271，confidence: high）

**运行在自有设备上的开源 AI 助手，接入聊天渠道**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

OpenClaw 是开源 AI 助手，运行在用户自己的设备上，通过 Discord、iMessage、Slack、Telegram、WhatsApp 等 20+ 聊天渠道以及 macOS/iOS/Android/Windows/Linux 原生应用交付。一个 Gateway 既可作为个人助手运行，也可作为团队共享部署。状态、记忆与凭证存于本地硬件；模型与 agent harness 作为可替换插件接入；默认仅每日版本检查联网，匿名统计需主动开启。由独立 501(c)(3) 基金会维护，无付费层或托管服务。

- Gateway 本地控制面管理会话、工具、事件与渠道连接
- 接入 20+ 聊天渠道及多平台原生应用
- 模型与 agent harness（Claude、Codex、本地模型）以插件方式可替换
- 沙箱配置与消息发送者配对等安全机制

> L11: OpenClaw is an open-source AI assistant that runs on your own computer and meets you in the channels you already use: Di
> L13: **Yours, with no catch.** State, memory, and credentials live on your hardware. Models and agent harnesses (Claude, Code
> L63: - The Gateway is the local control plane for sessions, tools, events, and channel connections.

## morluto/rea（⭐303126，confidence: high）

**为 agent 接入逆向工程工具的 MCP 服务器，从应用行为到原生二进制**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

REA 以 MCP 服务器形式将 agent 连接到逆向工程工具集，可检视原生二进制、JavaScript/Electron 应用、.NET 程序集、Android APK、网站、网络抓包等 20 类目标；返回结论附带证据与局限，分析在本地运行。原生深度分析需调用已有的 Hopper、Ghidra 或 IDA 安装；静态 JavaScript/.NET 检视无需原生引擎。通过 `npx rea-agents setup` 向 agent 注册并安装工作流说明，也提供 CLI（`rea`）在终端直接使用。要求 Node.js 22.19+/24.11+/26+ 与 npm。

- 单一 MCP 服务器覆盖原生二进制、JS/Electron、.NET、APK、固件、抓包等约 20 类分析目标
- 支持 Claude Code、Codex、Cursor、Gemini CLI 等多种 agent，其他客户端可手动注册 MCP
- 原生分析可复用已有 Hopper/Ghidra/IDA 安装，也可配合 objdump、Rizin、JADX、pwntools 等
- 结果附带证据与局限说明，分析在本地运行

> L6: ### One MCP for reverse engineering across binaries, applications, and runtime behavior.
> L41: REA connects your agent to tools for inspecting native binaries, JavaScript and Electron apps, .NET assemblies, and webs
> L43: Setup registers REA with your agent and installs matching workflow instructions. Native analysis can use an existing Hop
> L66: Setup supports Claude Code, Codex, Cursor, Gemini CLI, Grok Build and

## obra/superpowers（⭐301059，confidence: high）

**给编码 agent 的技能框架与软件开发方法论**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Superpowers 是一套面向编码 agent 的软件开发方法论，由一组可组合的技能与启动指令构成。技能按阶段自动触发：先通过头脑风暴澄清需求并产出设计文档，再生成细粒度实现计划，随后以子 agent 驱动或内联方式执行任务，强制红绿 TDD、代码评审与分支收尾流程。以插件形式分发到 Claude Code、Codex、Cursor、Gemini CLI 等多种编码工具，另提供企业商业支持联系方式。

- 可组合技能库：测试、调试、协作、元技能四类（如 TDD、系统化调试、git worktree）
- brainstorming→计划→子 agent 执行→评审→分支收尾的七步工作流，技能自动触发
- 提供 diagnosing-superpowers 技能，读取会话记录定位流程异常
- 支持十余种编码工具的插件安装途径

> L3: Superpowers is a complete software development methodology for your coding agents, built on top of a set of composable s
> L15: Next up, once you say "go", it launches a *subagent-driven-development* process, having agents work through each enginee
> L29: Superpowers is available via the official Claude plugin marketplace

## affaan-m/ECC（⭐282122，confidence: high）

**为 Claude Code 等 AI 编码 harness 安装 agent 工程系统的插件**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

ECC 是面向 AI 编码代理的开源 harness 系统，以 Claude Code 插件（ecc@ecc）和 npm 包（ecc-universal）形式分发，提供 71 个 agent、311 个技能、97 个命令、hooks、规则包、记忆与持续学习机制，以及 AgentShield 安全扫描（扫描 prompts、hooks、MCP 配置、权限、密钥）。项目按 plan→test→implement→review→verify→remember→improve 流程组织。对 Claude Code 提供引导式插件安装，Codex 与 Kimi Code 有引导路径，Cursor、OpenCode、Gemini、Zed、GitHub Copilot、Qwen 等通过能力受限的适配器支持；README 注明需查看支持状态矩阵，不保证功能对等。MIT 许可，另有面向私有仓库的托管 Pro 版 GitHub App。

- 71 个 agent、311 个技能与 97 个命令的插件化分发
- AgentShield 扫描 prompts、hooks、MCP 配置、权限与密钥
- hooks、记忆、会话摘要与持续学习等运行时机制
- 提供 npx/pnpm/yarn/bun 引导式安装与 dry-run 预检

> L98: Your agent can write code, but ECC gives it a coordinated engineering system and toolbox: it plans before it builds, ver
> L108: ECC is MIT-licensed open source. It works best with Claude Code today, has native Codex and Qoder plugin paths, and prov
> L110: Access to 71 agents, 311 skills, and 97 legacy command shims, plus hooks, rules, memory, continuous learning, and AgentS

## NousResearch/hermes-agent（⭐254611，confidence: high）

**自学习循环的个人 AI Agent，可在多终端与消息平台运行**

`ai_role=ai-native · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=medium · maturity=—`

Nous Research 开发的命令行 Agent：运行时通过内建学习循环创建与改进技能、维护长期记忆与用户模型，并支持跨会话检索历史对话。提供完整 TUI 终端界面与消息网关（Telegram、Discord、Slack、WhatsApp、Signal、Email），内置 cron 调度、子 Agent 并行、七种终端后端（local/Docker/SSH/Singularity/Modal/Daytona/Vercel Sandbox），并面向训练用途提供轨迹批量生成与压缩。安装脚本覆盖 Linux/macOS/WSL2、原生 Windows 与 Android/Termux。

- 内建学习循环：技能自动创建、使用中改进、Agent 主动持久化记忆
- 单一网关进程接入 Telegram/Discord/Slack/WhatsApp/Signal/CLI 六个入口
- 七种终端后端，含 Modal/Daytona 的无服务器持久化
- 从 OpenClaw 一键迁移设置、记忆、技能与 API key

> L15: **The self-improving AI agent built by Nous Research.** It's the only agent with a built-in learning loop — it creates s
> L21:  A closed learning loop Agent-curated memory with periodic nudges. Autonomous skill creation after complex tasks. Skills
> L24:  Runs anywhere, not just your laptop Seven terminal backends — local, Docker, SSH, Singularity, Modal, Daytona, and Verc

## deepseek-ai/deepseek-harness（⭐251995，confidence: high）

**DeepSeek 开源的 agent 运行时框架，一切皆插件**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=locked-api · hardware=— · install_friction=low · maturity=idea`

由 DeepSeek AI 开发的开源 agent harness（dsh），基于 Cordis 框架的 everything-is-a-plugin 架构，设计思想出自一篇时空可组合性编程范式的论文。目前处于 developer preview 阶段，官方声明会有破坏性兼容变更。提供 Web UI（默认 127.0.0.1:3080）与 SSH 两种启动方式，支持通过 npm 直接运行或克隆仓库用 pnpm 从源码构建，插件仓库通过 dsh-plugin 话题标签收录。

- everything-is-a-plugin 架构，基于 Cordis 框架
- npm 一条命令启动本地 Web UI（127.0.0.1:3080）
- 支持 SSH 场景启动与 --no-open 无浏览器运行
- 插件仓库可通过 dsh-plugin topic 提升可发现性

> L5: DeepSeek Harness (`dsh`) is an open-source agent harness developed by DeepSeek AI.
> L7: It is built on an **everything-is-a-plugin** architecture and powered by Cordis, whose design is described in _A Program
> L11: ## Developer preview

## n8n-io/n8n（⭐207794，confidence: high）

**AI 工作流自动化平台：可视化编排 agents 与 1500+ 集成**

`ai_role=ai-native · license_risk=dual · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

Fair-code 工作流自动化平台，用于构建和部署 AI agents 与多步工作流：可视化画布结合 JavaScript/Python 自定义代码与 npm 包，支持自托管或云部署。内置模型灵活性，可接入 OpenAI、Anthropic、Google 或开源模型并切换而不改架构；工作流支持逻辑分支、工具调用、人工审批与可观测性。提供基于角色的访问控制、审计日志与敏感数据处理能力，附带 1500+ 集成和 9000+ 工作流模板。采用 Sustainable Use License 与企业许可分发。

- 可视化画布与 JavaScript/Python 代码及 npm 包结合构建 AI 工作流
- 可接入 OpenAI、Anthropic、Google 或开源模型，切换不改架构
- 1500+ 集成与 9000+ 工作流模板
- 支持自托管/云部署、角色权限、审计日志

> L11: - **AI-Native Automation Platform**: Build and operationalize AI workflows and multi-step agents using your own data, mo
> L12: - **Model Flexibility, No Lock-In**: Connect to OpenAI, Anthropic, Google, or open-source models and switch providers wi

## tensorflow/tensorflow（⭐201076，confidence: high）

**面向研究者与开发者的端到端开源机器学习平台**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=cpu-ok · install_friction=medium · maturity=—`

端到端开源机器学习平台，提供工具、库与社区资源，供研究者推进 ML 研究并让开发者构建和部署 ML 应用。最初由 Google Brain 机器智能团队的研究者与工程师开发。提供稳定的 Python 与 C++ API，并为其他语言提供非保证向后兼容的 API。通过 pip 安装，含 CUDA GPU 支持包与 CPU-only 精简包，另有 nightly 测试包与 Docker 容器、源码构建途径。

- 端到端机器学习平台，含工具、库与社区资源生态
- 稳定 Python 与 C++ API，其他语言 API 非保证向后兼容
- pip 安装含 GPU（CUDA）包 tensorflow 与 CPU-only 包 tensorflow-cpu
- 官方构建覆盖 Linux/macOS/Windows/Android(LiteRT)/树莓派

> L15: TensorFlow is an end-to-end open source platform
> L28: TensorFlow provides stable Python

## firecrawl/firecrawl（⭐192411，confidence: high）

**为 AI agent 提供网页抓取与搜索数据的 API 及多语言 SDK**

`ai_role=ai-native · license_risk=dual · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=—`

网页数据获取服务与开源库：提供 Search（搜索并返回页面全文）、Scrape（URL 转 markdown/HTML/截图/结构化 JSON）、Interact（抓取后用 AI 提示或代码操作页面）、Crawl（整站抓取）、Map（站点 URL 发现）、Batch Scrape 与 Agent（按 prompt 自动检索数据）等端点。通过 Python/Node.js/Go/Java 等 10 种语言 SDK、CLI、MCP server 与 Skill 方式接入 agent。需在 firecrawl.dev 注册获取 API key；开源版为 AGPL-3.0，云端托管版含附加功能。

- 提供 Search/Scrape/Crawl/Map/Batch Scrape/Interact/Agent 等端点
- 支持 10 种语言的官方 SDK、CLI 与 MCP server 接入
- Agent 端点按 prompt 检索数据，支持 schema 结构化输出与 effort 分级（spark-2 模型）
- 解析网页托管的 PDF、DOCX 等媒体内容

> L31: **Supercharge your AI agents with data from the web and beyond. Building the library for superintelligence. 🔥** Open sou
> L43: - **LLM-ready output**: Clean markdown, structured JSON, screenshots, and more — spend fewer tokens, build better AI app
> L45: - **Agent ready**: Connect Firecrawl to any AI agent or MCP client with a single command
> L552: Firecrawl is open source under the AGPL-3.0 license. The cloud version at firecrawl.dev includes additional features:

## microsoft/markitdown（⭐190745，confidence: high）

**面向 LLM 场景的文件转 Markdown Python 工具**

`ai_role=ai-enhanced · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

轻量级 Python 工具，将多类文件转换为 Markdown，目标消费者是 LLM 与文本分析流水线，转换时保留标题、列表、表格、链接等文档结构。支持 PDF、Office 文档、图片（EXIF/OCR）、音频（转录）、HTML、YouTube URL 等。提供 CLI、Python API、第三方插件机制与 Docker 运行方式；另可通过 Azure Document Intelligence / Content Understanding 或 OpenAI 客户端进行云端增强转换与图片描述。README 明确定位为库而非面向最终用户的应用，不接受 Web 服务或桌面应用贡献。

- 多格式转 Markdown：PDF、Word、PowerPoint、Excel、图片、音频、HTML、EPub 等
- 提供 CLI、Python API、Docker 三种使用方式
- 支持第三方插件机制（#markitdown-plugin）
- 可选接入 Azure Document Intelligence / Content Understanding 与 LLM 图片描述

> L9: MarkItDown is a lightweight Python utility for converting various files to Markdown for use with LLMs and related text a
> L263: To use Large Language Models for image descriptions (currently only for pptx and image files), provide `llm_client` and 
> L287: MarkItDown is a Python utility for converting files to Markdown for use with LLMs and related text analysis pipelines. T

## Significant-Gravitas/AutoGPT（⭐187621，confidence: high）

**面向用户与开发者的 AI agent 构建与运行平台**

`ai_role=ai-native · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

AutoGPT 提供构建、部署和运行 AI agent 的开源平台，支持用自然语言描述任务（AutoPilot）或在可视化画布（Build）中逐步编排工作流，agent 可按需、按计划或由触发器运行。平台包含 Agents 仪表盘与 Marketplace 社区 agent 市场，连接 45+ 平台与数百个 AI 模型。提供托管 Platform（付费、含模型访问）与自托管（免费、需自备 Docker 基础设施与模型 API key）两条路径；原独立版 AutoGPT Classic 保留于 classic/ 目录，采用 MIT 许可证。

- AutoPilot 对话转 agent 与可视化 Build 画布两种构建方式
- 45+ 平台集成（Gmail、GitHub、Slack、Notion 等）
- 托管 Platform 与自托管双路径，同一代码仓库
- AutoGPT Classic 以 MIT 许可证保留在 classic/ 目录

> L31: AutoGPT lets you build, deploy, and run AI agents that carry out complete workflows. Describe an outcome in plain Englis
> L84: ### Self-host AutoGPT
> L155: Looking for the original standalone AutoGPT agent? It remains available in `classic/` under the MIT License.

## ollama/ollama（⭐183604，confidence: high）

**本地与云端运行开源大模型的工具：下载即用多款开放模型**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

Ollama 是一个用于在本地或云端运行开源大模型的工具，覆盖下载安装、命令行交互、模型管理和 REST API。支持 macOS、Windows、Linux 的脚本安装与 Docker 官方镜像，提供 Python、JavaScript 官方库；可配合 Claude Code、Codex、Copilot CLI 等编码集成运行，并通过 OpenClaw 接入多平台消息渠道作为 AI 助手。后端基于 llama.cpp 项目。

- 提供 REST API 与 Python/JavaScript 官方库（pip/npm 安装）
- 支持 macOS/Windows/Linux 脚本安装与官方 Docker 镜像
- 支持编码集成（Claude Code、Codex、Copilot CLI 等）与 OpenClaw 助手接入
- 模型后端基于 llama.cpp 项目

> L5: # Ollama
> L7: Start building with open models. Access the latest releases locally or in the cloud with complete privacy.
> L86: Ollama has a REST API for running and managing models.

## anthropics/skills（⭐181734，confidence: high）

**为 Claude 提供 Agent Skills 示例、规范与模板的官方仓库**

`ai_role=ai-ecosystem · license_risk=dual · deploy=— · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

Anthropic 官方的 Agent Skills 仓库：Skill 是含 SKILL.md（YAML frontmatter + 指令）的文件夹，Claude 按任务动态加载。仓库包含四类示例技能（创意、技术、企业、文档）、Agent Skills 规范与模板，文档类 docx/pdf/pptx/xlsx 技能为 source-available 许可，其余多为 Apache 2.0。官方声明仅供演示与教学用途，关键任务前需自行测试。可通过 Claude Code 插件市场、Claude.ai（付费计划）及 Claude API 使用。

- 技能以 SKILL.md 文件夹形式自包含，仅需 name 与 description 两个字段
- 含文档技能（docx/pdf/pptx/xlsx）生产实现作为参考
- 可作为 Claude Code 插件市场注册安装
- 提供 Agent Skills 规范与技能模板

> L1: > **Note:** This repository contains Anthropic's implementation of skills for Claude. For information about the Agent Sk
> L16: This repository contains skills that demonstrate what's possible with Claude's skills system. These skills range from cr
> L20: Many skills in this repo are open source (Apache 2.0). We've also included the document creation & editing skills that p

## f/prompts.chat（⭐173251，confidence: high）

**给 AI 用户的社区开源提示词库，可浏览、收藏与自托管**

`ai_role=ai-ecosystem · license_risk=dual · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=idea`

一个社区共建的提示词集合（前身为 Awesome ChatGPT Prompts），提供网站浏览与 CSV、Markdown、Hugging Face Dataset 三种数据格式，用户可通过网站提交提示词并自动同步。支持用 npx/npm 自托管私有提示词库，含品牌、主题与 GitHub/Google/Azure AD 认证配置向导，数据库使用 PostgreSQL。另提供 CLI、Claude Code 插件与 MCP Server 三种接入方式，并附免费交互式提示工程教程与儿童学习模块。

- 提示词数据以 CSV、PROMPTS.md、Hugging Face Dataset 发布
- npx prompts.chat 一键创建自托管库，支持 GitHub/Google/Azure AD 认证
- 提供 CLI、Claude Code 插件与 MCP Server 接入
- 附 28+ 章交互式提示工程教程

> L40: A curated collection of **prompts** for AI chat models. Originally created for ChatGPT, these prompts work great with an
> L67: ## 🚀 Self-Hosting
> L111: ### MCP Server
> L191: This project is dual-licensed:

## huggingface/transformers（⭐167789，confidence: high）

**为文本/视觉/音频/多模态模型提供统一模型定义，用于推理与训练**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

Hugging Face 的 Transformers 库作为模型定义框架，集中维护各模态预训练模型的定义，使其可被 Axolotl、DeepSpeed 等训练框架与 vLLM、TGI 等推理引擎复用。提供 Pipeline 高层推理 API，覆盖文本生成、语音识别、图像分类、视觉问答等任务，模型从 Hub 下载并缓存。要求 Python 3.10+ 与 PyTorch 2.6+，可通过 pip/uv 安装或从源码构建；Hub 上有 1M+ 模型检查点可用，另提供 transformers chat 命令行对话与 serve 本地服务。

- 统一模型定义框架，兼容主流训练框架与推理引擎
- Pipeline API 覆盖文本、音频、视觉、多模态任务
- Hub 上 1M+ 预训练模型检查点可直接调用
- 同一模型可在 PyTorch/JAX/TF2.0 之间切换

> L34: Transformers acts as the model-definition framework for state-of-the-art machine learning with text, computer
> L85: Get started with Transformers right away with the Pipeline API. The `Pipeline` is a high-level inference class that supp
> L51: Transformers works with Python 3.10+, and PyTorch 2.6+.

## DietrichGebert/ponytail（⭐165861，confidence: high）

**给 AI 编码 agent 注入“极简优先”编码原则的提示词技能包**

`ai_role=ai-enhanced · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=—`

以单个 SKILL.md 提示词为核心的 agent 技能：在写代码前按七级阶梯依次判断“是否需要写、仓库已有、标准库、平台特性、已有依赖、能否一行”，只在必要时写最小实现；不做代码高尔夫，验证、错误处理、安全与可访问性不在裁剪范围，含分支/循环/解析/金钱/安全的逻辑要求附带小测试。提供 /ponytail-review（读 diff 之外被触碰的代码做审查）与 /ponytail-audit（全仓库按优先级排序）等命令，以及 Claude Code 中的成本/token/复用率状态条与本地统计面板。宣称在 20 个 agent 上可用。

- 七级阶梯决策：优先复用仓库代码、标准库与平台特性
- /ponytail-review 读取变更触碰的全部代码而非仅 diff
- Claude Code 提示条展示成本、token、agent 时间与代码复用率
- /ponytail-debt 汇集 shortcut: 注释为技术债清单

> L96: Ponytail is one prompt: `skills/ponytail/SKILL.md`. The compact version, for agents that read a rules file, is `AGENTS.m
> L139: Commands need a skill-capable host (Claude Code, Codex, Devin CLI, OpenCode, Gemini, Antigravity CLI, pi, Hermes Agent, 

## AUTOMATIC1111/stable-diffusion-webui（⭐165071，confidence: high）

**给创作者提供 Stable Diffusion 的浏览器图像生成界面**

`ai_role=ai-native · license_risk=viral · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=—`

基于 Gradio 实现的 Stable Diffusion Web 界面，提供 txt2img 与 img2img 两种生成模式，附带外绘、内绘、提示词矩阵、放大（RealESRGAN/SwinIR 等）、Textual Inversion、Lora、检查点合并、批量处理、CLIP 反推提示词、API 等功能。通过一键脚本安装运行，支持 NVidia GPU、AMD GPU、Intel CPU/GPU 与 Ascend NPU，也给出 Windows/Linux/Apple Silicon 的安装说明；生成参数可保存于图像元数据中供还原。

- txt2img 与 img2img 两种生成模式及内绘/外绘
- 集成 GFPGAN、CodeFormer、RealESRGAN 等修复与放大网络
- 生成参数写入 PNG/EXIF 元数据并可一键还原
- 提供 API 与社区扩展脚本机制

> L2: A web interface for Stable Diffusion, implemented using Gradio library.
> L96: - NVidia (recommended)

## Snailclimb/JavaGuide（⭐159096，confidence: high）

**Java 后端求职者的面试知识指南，覆盖基础到分布式**

`ai_role=ai-knowledge · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=medium · maturity=—`

以 Markdown 文章目录为主体的知识库，按 Java 基础/集合/并发/JVM、计算机基础、MySQL/Redis/MongoDB、分布式、高性能、高可用、系统设计等板块组织面试知识点与学习路线，并提供在线阅读站与面试突击 PDF 版。README 同时列出新方向的 AI 应用开发面试指南（LLM、Agent、RAG、MCP），但该内容位于另一仓库 AIGuide；本仓库为纯文档项目，无安装或运行步骤。

- 按面试板块组织的知识点/面试题总结目录（Java、数据库、分布式、系统设计等）
- 提供在线阅读站与面试突击版 PDF 下载
- 含 Java 后端面试通关计划、学习路线与简历指南
- 另有独立的 AI 应用开发面试指南仓库（LLM/Agent/RAG/MCP）

> L12: > - **大模型实战项目**： ⭐AI 智能面试辅助平台 + RAG 知识库（基于 Spring Boot 4.0 + Java 21 + Spring AI 2.0，非常适合作为学习和简历项目，学习门槛低）。
> L22: 面向后端开发者的 AI 应用开发、AI 编程实战与面试指南已开源，涵盖 LLM、Agent、RAG、MCP、Claude Code、Codex 等核心技术与工程实践。对标 JavaGuide！有帮助的话，欢迎 Star！
> L38: ## Java

## langgenius/dify（⭐158711，confidence: high）

**给团队的 LLM 应用开发平台：可视化构建工作流、RAG 与 Agent**

`ai_role=ai-native · license_risk=none · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

开源 LLM 应用开发平台，界面整合 AI 工作流、RAG 管道、Agent 能力、模型管理与可观测性（含 Opik、Langfuse、Arize Phoenix 集成）。工作流在可视化画布上构建；模型支持数百个专有/开源 LLM 及 OpenAI API 兼容模型；Agent 带独立沙箱，可运行命令、安装软件、处理文件，并接入 Marketplace 工具、MCP 服务器与自有 API。所有功能提供对应 API（Backend-as-a-Service）。部署方式：Docker Compose 自托管、Cloud 托管或企业版（SSO/RBAC）。最低要求 CPU 2 核、内存 4 GiB。

- 可视化画布构建 AI 工作流，RAG 管道覆盖文档摄取到检索（支持 PDF/PPT 抽取）
- 接入数百个专有/开源 LLM 及任意 OpenAI API 兼容模型
- Agent 自带沙箱，可执行命令、安装软件、连接 MCP 服务器与自有 API
- 全部功能附 API，Cloud/VPC/自托管三种部署路径

> L58: Dify is an open-source LLM app development platform. Its intuitive interface combines AI workflow, RAG pipeline, agent c
> L90: Seamless integration with hundreds of proprietary / open-source LLMs from dozens of inference providers and self-hosted 
> L113: - **Self-hosting Dify Community Edition **

## open-webui/open-webui（⭐155970，confidence: high）

**自托管 AI 交互界面，接入本地与云端多模型**

`ai_role=ai-ecosystem · license_risk=none · deploy=self-host · model_dep=local-ok · hardware=cpu-ok · install_friction=low · maturity=—`

自托管 Web 平台，通过 Ollama 与 OpenAI 兼容 API 连接本地及云端模型，提供 RBAC 用户组、插件体系（Filters/Actions/Pipes/Tools/Skills）、MCP 与 OpenAPI 工具服务器接入、RAG（9 种向量数据库、混合检索）、网络搜索注入、图像生成、语音视频通话、日历与定时任务、企业认证（LDAP/SSO/SCIM）及 OpenTelemetry 可观测性。可通过 pip、Docker、Kubernetes 安装，支持纯 CPU 或 CUDA 镜像，另有 macOS/Windows/Linux 原生桌面应用。

- 支持 Ollama 与任何 OpenAI 兼容 API（LMStudio、GroqCloud、Mistral、OpenRouter、vLLM 等）
- 插件体系与 MCP/OpenAPI 工具服务器接入，可构建带终端与文件系统的 Agent
- RAG 支持 9 种向量数据库、BM25+向量混合检索与多家网络搜索提供商
- 企业功能：RBAC、LDAP/SSO/SCIM、多节点水平扩展、OpenTelemetry

> L12: Open WebUI is **a home for AI**, a self-hosted AI platform that's **extensible**, **feature-rich**, user-friendly, and b
> L31: - 🧩 **Plugin Support**: Extend Open WebUI with **Filters**, **Actions**, **Pipes**, **Tools**, and **Skills**. Connect e
> L57: - 📚 **Local RAG Integration**: Retrieval Augmented Generation backed by 9 vector databases and multiple content-extracti

## anthropics/claude-code（⭐151510，confidence: mid）

**终端里的 agentic 编码工具，用自然语言操作代码库**

`ai_role=ai-native · license_risk=none · deploy=library · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

Anthropic 出品的命令行编码代理：读取并理解代码库，通过自然语言执行例行任务、解释复杂代码、处理 git 工作流。可在终端、IDE 中使用，也可在 GitHub 上以 @claude 触发。仓库附带插件机制，以自定义命令和 agent 扩展功能。安装支持 macOS/Linux/Windows 的官方脚本、Homebrew 与 WinGet，npm 安装方式已被标注为弃用。使用数据（代码接受/拒绝、会话数据）会被收集用于反馈，官方声明有限保留期且不用于模型训练。

- 终端内自然语言驱动的 agentic 编码，理解代码库上下文
- 支持终端、IDE、GitHub @claude 多种使用入口
- 插件机制通过自定义命令和 agent 扩展功能
- 内置 /bug 命令直接上报问题

> L5: Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster 
> L46: This repository includes several Claude Code plugins that extend functionality with custom commands and agents. See the 

## langchain-ai/langchain（⭐147982，confidence: high）

**面向开发者的构建 agent 与 LLM 应用的框架**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

LangChain 是用于构建 agent 和 LLM 应用的 Python 框架，通过标准接口统一模型、嵌入、向量存储等组件，支持可互换的第三方集成。提供 init_chat_model 统一入口调用各厂商模型，经 uv/pip 从 PyPI 安装。同生态包含 Deep Agents（高层 agent 包）、LangGraph（底层编排框架）、LangSmith（评估/观测/部署），并提供 JS/TS 版本。README 未给出具体模型接入配置细节，需查文档。

- 模型、嵌入、向量存储等组件的标准接口与可互换性
- 与 LangGraph、Deep Agents、LangSmith 组成的产品矩阵
- uv add langchain 一条命令安装
- 同时提供 JS/TS 等效库 LangChain.js

> L14: LangChain is a framework for building agents and LLM-powered applications. It helps you chain together interoperable com
> L22: uv add langchain

## x1xhlol/system-prompts-and-models-of-ai-tools（⭐144064，confidence: mid）

**收录多款 AI 编程工具系统提示词的资料合集**

`ai_role=ai-knowledge · license_risk=viral · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

该仓库汇总多款 AI 工具（含 Cursor、Claude Code、Devin、Lovable、Windsurf、Perplexity、Replit、v0 等）的系统提示词及开源相关资料，以文件集合形式提供，无运行代码与安装流程。维护者通过 Discord 社区、Patreon、Ko-fi 与加密货币地址接收支持，并提供 ZeroLeaks 相关的安全提示内容。README 未给出目录结构或使用说明，仅包含社区与赞助信息。

- 收录 Augment Code、Claude Code、Cursor、Devin、Windsurf 等多款工具的系统提示词
- 附带 LeaksLab Discord 社区链接
- 提供 BTC/LTC/ETH、Patreon、Ko-fi 等赞助渠道
- 含面向 AI 创业公司的提示词安全提示

> L1: <a href="https://discord.gg/NwzrWErdMU" target="_blank">
> L12: > **Warning:** If you're an AI startup, make sure your data is secure. Exposed prompts or AI models can easily become a 

## Shubhamsaboo/awesome-llm-apps（⭐142109，confidence: mid）

**面向开发者的 100+ 开源 AI agent 与 RAG 应用模板合集**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

以 Apache-2.0 许可的开源仓库形式收录 100+ 模板，按 Agent Skills、入门/进阶 agent、多 agent 团队、语音 agent、生成式 UI、游戏 agent、MCP agent 与 RAG 等类别组织；每个模板附带可运行代码，可通过 npx 安装技能或 git clone 后 pip 安装依赖并用 streamlit 运行。支持接入 Claude、Gemini、GPT、DeepSeek、Llama、Qwen 等模型，入门类 agent 只需 API key 即可运行。模板通过 Unwind AI 周更分发。

- 100+ 开源模板，覆盖入门 agent、多 agent 团队、MCP、RAG 等类别
- Agent Skills 可通过 npx 一条命令安装，适配 Claude Code、Codex、Cursor 等编码 agent
- 入门类单文件 agent 仅需 API key 即可运行
- 支持本地与云端模型（含本地 RAG 与本地旅行 agent）

> L3: **100+ open-source AI agents, agent skills, and RAG apps. Hand-built, tested end-to-end, Apache-2.0.**
> L7: Works with Claude, Gemini, GPT, DeepSeek, Llama, Qwen and other open-source models.
> L56: ### 🧩 Agent Skills

## github/spec-kit（⭐141634，confidence: high）

**为 AI 编码代理提供结构化流程与模板的工具包**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

开源工具包，为 AI 编码代理提供结构化流程、可复用模板与文档化产物。内置规格驱动开发（SDD）流程，附带可选的 bug 修复与想法评估扩展，并提供扩展、预设、工作流、捆绑包、目录等组合机制用于定制或自建流程。以 CLI 形式安装，依赖 Python 3.11+ 与 uv，在代理聊天中以 /speckit-* 技能形式调用。MIT 许可。

- 内置 SDD 流程：specify → plan → tasks → implement → converge
- 扩展、预设、工作流、捆绑包等组合机制可定制或自建流程
- bug 修复与想法评估作为可选扩展按需安装
- 支持本地源与自托管目录，可离线或在防火墙后使用

> L15: Spec Kit is an open source toolkit that gives AI coding agents structured
> L63: You need **Python 3.11+**, **uv**,
> L84: below. Invoke each `/speckit-*` **skill in your agent's chat**, one at a time,

## Comfy-Org/ComfyUI（⭐138032，confidence: high）

**给视觉创作者的节点式扩散模型 GUI 与本地推理后端**

`ai_role=ai-native · license_risk=viral · deploy=library · model_dep=— · hardware=gpu-8g · install_friction=medium · maturity=—`

以节点图组织图像、视频、音频、3D 与文本生成工作流的桌面/后端程序：支持加载 checkpoints、VAE、LoRA、ControlNet 等模型文件，工作流可存为 JSON，提供本地 API 与 App Mode 供集成到生产流水线。核心可完全离线运行（--offline 禁用付费 API 节点），通过异步权重流式在最低约 4GB 显存 + 8GB 内存的消费级硬件上运行大模型。Windows/macOS 提供桌面安装包与便携版，Linux 手动安装。

- 节点图界面构建无代码的可复用生成工作流
- 原生支持 SD/Flux/Qwen/Wan/Hunyuan 等多类开源模型
- 异步权重流式与 VRAM/RAM 管理，支持量化模型
- 全平台覆盖：桌面应用、Windows 便携版、comfy-cli、手动安装

> L16: ComfyUI is the AI creation engine for visual professionals who demand control over every model, every parameter, and eve
> L45: - A visual node graph for building and reusing image, video, audio, 3D, and text workflows without code.
> L123: # Installing

## harry0703/MoneyPrinterTurbo（⭐132313，confidence: high）

**给内容创作者：按主题一键生成配音字幕齐全的高清短视频**

`ai_role=ai-enhanced · license_risk=permissive · deploy=desktop · model_dep=local-ok · hardware=gpu-8g · install_friction=low · maturity=—`

以主题或关键词为输入的自动化短视频生成流水线：依次完成脚本生成、素材匹配（本地/库存/AI 文生视频）、配音（Edge TTS 等多种服务）、字幕生成（edge/whisper 两种模式）、背景音乐合成与成片剪辑，支持 9:16/16:9/1:1 三种画幅及批量生成。提供 AI Agent、WebUI、API 和 CLI 四种使用方式，可一键上传至 TikTok、Instagram、YouTube Shorts。脚本生成依赖外部大模型 API Key，GPU 非必需。

- 提供 AI Agent、WebUI、API 和 CLI 四种使用方式
- 支持 Kimi、OpenAI、Claude、Gemini、DeepSeek、通义千问等多种模型服务及统一网关
- 集成 Edge TTS（免费无 Key）等十余种配音服务与 faster-whisper 本地转写
- 支持跨平台自动发布至 TikTok、Instagram、YouTube Shorts

> L5: 只需提供视频 主题 或 关键词 ，即可自动生成视频脚本、匹配素材、生成字幕和背景音乐，并合成高清短视频。
> L118: - [x] 提供 **AI Agent、WebUI、API 和 CLI** 四种使用方式，既能快速上手，也能接入自动化流程
> L125: - [x] 支持 Kimi / Moonshot AI、OpenAI、Anthropic Claude、Google Gemini、DeepSeek、阿里云通义千问、Microsoft Azure OpenAI、火山引擎方舟、xAI Gro

## ggml-org/llama.cpp（⭐131496，confidence: high）

**让开发者在本地和云端多种硬件上运行 LLM/VLM 推理**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=medium · maturity=—`

以 C/C++ 实现的 LLM（含 VLM）推理项目，目标是以最小配置在广泛硬件上运行推理。核心机制包括：无依赖的纯 C/C++ 实现、1.5-bit 到 8-bit 整数量化以降低内存占用、CPU+GPU 混合推理，以及 CUDA/HIP/MUSA/Metal/Vulkan/SYCL 等多后端。提供 cli 与 server 等工具，server 提供 OpenAI 兼容 API 与内置 Web UI。基于 ggml 库构建，MIT 许可，可经安装脚本、Docker、预编译二进制或源码构建获取。

- 纯 C/C++ 实现且无依赖，支持从 1.5-bit 到 8-bit 的整数量化
- 覆盖 CUDA、HIP、MUSA、Metal、Vulkan、SYCL 等多后端与多架构指令集
- CPU+GPU 混合推理，可运行超过总 VRAM 容量的模型
- llama serve 提供 OpenAI 兼容 API 与内置 Web UI

> L5:  LLM inference in C/C++
> L51: The main goal of `llama.cpp` is to enable LLM (and VLM) inference with minimal setup and state-of-the-art performance on
> L54: - Plain C/C++ implementation without any dependencies

## openai/codex（⭐129622，confidence: high）

**OpenAI 出品的终端内本地运行的编程 Agent**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

Codex CLI 是 OpenAI 提供的命令行编程 Agent，在用户本地计算机上运行。安装方式覆盖 macOS/Linux 的 shell 脚本、Windows PowerShell 脚本，以及 npm、Homebrew 等包管理器，并提供各平台的预编译二进制下载（安装器默认从 releases.openai.com 下载，可回退或强制使用 GitHub Releases）。使用时可通过 ChatGPT 账号登录（Plus/Pro/Business/Edu/Enterprise 套餐），也可改用 API key（需额外设置）。另有 IDE 扩展、桌面应用（codex app）与云端版本 Codex Web。仓库采用 Apache-2.0 许可证。

- macOS/Linux/Windows 一行命令安装脚本，另有 npm 与 Homebrew 渠道
- 提供 Apple Silicon/x86_64 与 Linux arm64/x86_64 预编译二进制
- 支持 ChatGPT 套餐登录或 API key 两种使用方式
- 配套 IDE 扩展、桌面应用与云端版本入口

> L1: Codex CLI is a coding agent from OpenAI that runs locally on your computer.
> L35: Codex CLI can also be installed via the following package managers:
> L75: This repository is licensed under the Apache-2.0 License.

## Graphify-Labs/graphify（⭐127605，confidence: mid）

**给 AI 编码助手把代码库映射成可查询知识图谱的 CLI 工具**

`ai_role=ai-enhanced · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

以 `/graphify` 技能形式注册到 Claude Code、Cursor、Codex、Gemini CLI 等 20+ 编码助手，用 tree-sitter AST 本地确定性解析代码，构建覆盖 ~40 语言的 calls/imports/inherits 跨文件知识图谱，输出 graph.html、GRAPH_REPORT.md 与 graph.json 三个文件；每条边带 EXTRACTED/INFERRED 标签，提供 query/path/explain 三类命令。文档、PDF、图像、音视频经语义 pass 也并入图。代码解析不调用 LLM、无向量索引；语义 pass 需配置模型或 API key。依赖 Python 3.10+ 与 uv/pipx。

- tree-sitter AST 本地解析 ~40 语言，代码解析零 LLM 调用、数据不出本机
- 每条边带 EXTRACTED/INFERRED 置信标签
- 无嵌入与向量库，图遍历支持 query/path/explain
- 一条命令注册到 Claude Code、Cursor、Codex 等 20+ 平台

> L22: Type `/graphify` in your AI coding assistant and it maps your entire project (code, docs, PDFs, images, videos) into a *
> L24: - **Code maps for free, fully local.** Code is parsed with tree-sitter AST: deterministic, no LLM, nothing leaves your m
> L61: **One install, any assistant, any OS.** Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot, and 20+ more, on macOS, 

## shadcn-ui/ui（⭐125795，confidence: high）

**给开发者的可定制 React 组件集合，用于构建自己的组件库**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

shadcn/ui 提供一组可组合、注重可访问性的 React 组件，代码复制到用户项目中，可自行定制与扩展，用于构建自己的组件库。README 说明文档位于 ui.shadcn.com/docs，采用 MIT 许可证，接受社区贡献。README 本身仅作入口，安装方式与框架集成细节（如 Next.js、Radix UI 等主题标签所示）需查阅其文档站点。

- 可组合、注重可访问性的组件集
- 代码归用户所有，可定制、扩展并构建自有组件库
- MIT 许可证开源

> L3: A set of beautifully designed components that you can customize, extend, and build on. Start here then make it your own.
> L14: Licensed under the MIT license.

## microsoft/generative-ai-for-beginners（⭐121521，confidence: high）

**面向初学者的生成式 AI 应用开发入门课程（21 课）**

`ai_role=ai-knowledge · license_risk=permissive · deploy=— · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

微软云推广团队制作的 21 课生成式 AI 应用开发课程，第 3 版。课程分 "Learn"（讲解概念：LLM 原理、模型选择、负责任 AI、提示工程、微调等）与 "Build"（配套 Python 与 TypeScript 代码示例：文本生成、聊天、向量检索、图像生成、RAG、AI Agent 等）两类，每课含视频介绍、README 讲义与延伸资源。代码可接入 Azure OpenAI、Microsoft Foundry Models、OpenAI API 或本地运行的 Foundry Local；仓库提供 50+ 语言翻译，并给出排除翻译目录的 sparse checkout 克隆方式。

- 21 课覆盖概念讲解与代码实践，代码示例提供 Python 与 TypeScript 两种语言
- 支持 Azure OpenAI、Microsoft Foundry Models、OpenAI API 及本地离线运行的 Foundry Local 四种模型接入途径
- 提供 50+ 语言翻译版本，可用 sparse checkout 排除翻译目录以减小克隆体积
- 课程主题包含提示工程、RAG 与向量数据库、函数调用、微调、SLM 及 Mistral/Meta 模型使用

> L3: ### 21 Lessons teaching everything you need to know to start building Generative AI applications
> L45: Learn the fundamentals of building Generative AI applications with our 21-lesson comprehensive course by Microsoft Cloud
> L51: Lessons are labeled either "Learn" lessons explaining a Generative AI concept or "Build" lessons that explain a concept 

## browser-use/browser-use（⭐118313，confidence: high）

**面向 AI agent 的开源浏览器自动化 Python 库**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

提供 Python 库、CLI 和全托管云三条使用路径：库可嵌入应用运行浏览器 agent，支持本地或云浏览器、自定义工具与结构化输出；CLI 让现有 agent 获得浏览器控制能力；云服务提供带隐身、住宅代理与 CAPTCHA 处理的托管浏览器及托管 agent API。库本身 MIT 协议免费，模型推理与云浏览器按用量另计；CAPTCHA 处理效果依赖具体站点。

- Python 库内嵌 Agent 运行时，支持本地/云浏览器与自定义 Tools 注册
- 为 Claude 提供 31 个浏览器动作的工具集集成，可经 CDP 控制远程浏览器
- ChatBrowserUse 网关可调用 Claude/GPT/Gemini 等模型，也可用 Ollama 本地模型
- 云浏览器按 $0.02/小时计费，支持 Docker/CI/serverless 场景

> L41:  Three ways to use Browser Use: the hosted V4 agent, the Browser Use CLI, or the open source Python library. All three d
> L160: - **Python Library:** Run the open source agent in your own application, with custom tools, structured output, and your 
> L202: The Python library is free and MIT-licensed. Model inference and hosted browsers are separate: API providers, including 

## JuliusBrussee/caveman（⭐113219，confidence: high）

**给编码 agent 省token的代理与技能：压缩回答与读取内容**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=locked-api · hardware=— · install_friction=low · maturity=research`

以 CLI 安装的代理加技能组合，让编码 agent 用受控短语风格输出，压缩日志、JSON、CSV、测试输出等模型读取内容；包含六项功能：短回答、读前压缩、按任务选模型与effort的 Auto、脚本复用 Blocks、token 浪费修复、网页压缩。通过 npx 一条命令覆盖 Mac/Linux/Windows，需 Node.js 22.13+，在本机以用户自己的密钥与登录运行，支持 Claude Code、Codex、Gemini CLI 等 30+ agent；README 标注部分测量为中期数据或未复测。

- 短回答技能：同一修复 63 token 降至 20，代码与命令保持原样
- 读前压缩：日志/JSON/CSV/测试输出整体会话输入 token 减少 33.2%（README 自报）
- Auto 模式按任务选择模型与 effort，README 自报成本降 54%
- Blocks 代码模式：脚本保留在仓库并在 PR 检查，提供 8 个内置 block

> L5: **Caveman make your AI agent say less and read less. Code stay exact. Brain still big.**
> L47: One command. Mac, Linux, Windows. Caveman find your agents and your logins, show what it change. Press Enter. Done. Need
> L49: After that, plain `claude` stays caveman'd. So do Codex, Gemini CLI, OpenCode, and 30+ more. It runs on your machine, wi

## supabase/supabase（⭐111682，confidence: high）

**给 Web/移动/AI 应用开发者提供 Postgres 后端开发平台**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

基于 Postgres 的开发平台，将数据库、认证授权、自动生成 API、实时订阅、函数、文件存储与向量嵌入工具集组合为一体化后端。架构由 PostgREST、GoTrue、Realtime、Storage、pg_graphql 等开源组件构成。提供托管平台（注册即用）与自托管/本地开发两种方式；官方客户端库覆盖 JavaScript、Flutter、Swift、Python、Kotlin 等，并有 C#、Go、Java、Ruby、Rust、Godot 等社区库。README 未列出安装命令与硬件要求。

- 托管 Postgres 数据库与认证授权、REST/GraphQL 自动生成 API
- Realtime 通过 websocket 广播数据库变更（基于 Elixir 服务器）
- AI + Vector/Embeddings Toolkit 与 pg_graphql 扩展
- 多语言官方客户端库（JS/Flutter/Swift/Python/Kotlin 等）

> L3: Supabase is the Postgres development platform. We're building the features of Firebase using enterprise-grade open sourc
> L15: - [x] AI + Vector/Embeddings Toolkit. Docs
> L43: Supabase is a hosted platform. You can sign up and start using Supabase without installing anything.

## TauricResearch/TradingAgents（⭐111677，confidence: high）

**多智能体 LLM 金融交易研究框架：模拟交易公司角色分工**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

以真实交易公司组织方式组织 LLM 智能体：分析师团队（基本面/情绪/新闻/技术四类）、多空研究员辩论、交易员决策、风控与组合经理审批，最终在模拟交易所执行。支持多 LLM 提供商、CLI 交互与无终端参数化运行、回测、LangGraph checkpoint 续跑、HTML 报告导出。README 明确声明仅供研究用途，不构成投资建议；运行受所选模型、温度、数据质量等因素影响。

- 分析师/研究员/交易员/风控/组合经理的多智能体协作与辩论机制
- 多 LLM 提供商：OpenAI、Gemini、Claude、Bedrock、Ollama 及任意 OpenAI 兼容端点
- 可用 ChatGPT Plus/Pro 订阅计划运行，无需单独 API key
- CLI 支持 ticker/date 等参数免交互运行与 HTML 单页报告输出

> L51: TradingAgents is a multi-agent trading framework that mirrors the dynamics of real-world trading firms. By deploying spe
> L53: > TradingAgents framework is designed for research purposes. Trading performance may vary based on many factors, includi
> L121: TradingAgents supports multiple LLM providers. Set the API key for your chosen provider:

## openai/whisper（⭐110751，confidence: high）

**为开发者提供多语言语音识别与翻译的开源模型**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=research`

OpenAI 发布的通用语音识别模型，基于 Transformer 序列到序列架构，在大规模多语言音频数据上训练，可执行多语言语音识别、语音翻译、语言识别与语音活动检测，以单一模型替代传统多级语音处理流水线。提供 6 种模型规模（含 turbo 加速版），附带命令行工具与 Python API，依赖 ffmpeg 处理音频。代码与模型权重以 MIT 许可发布。

- 单一模型支持多语言识别、语音翻译、语言识别与语音活动检测
- 提供 6 种模型规模（tiny 至 large，含 turbo），各档标注显存需求与相对速度
- 提供 CLI 与 Python 两种使用方式，代码与模型权重均以 MIT 许可发布

> L8: Whisper is a general-purpose speech recognition model. It is trained on a large dataset of diverse audio and is also a m
> L14: A Transformer sequence-to-sequence model is trained on various speech processing tasks, including multilingual speech re
> L127: Whisper's code and model weights are released under the MIT License. See LICENSE for further details.

## google-gemini/gemini-cli（⭐107415，confidence: high）

**在终端中使用 Gemini 模型的开源 AI agent CLI**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

Google 发布的开源命令行 AI agent，将 Gemini 模型接入终端：支持查询与编辑代码库、从 PDF/图片/草图生成应用、自然语言调试、以脚本方式非交互运行并输出 JSON/流式 JSON。通过 OAuth 登录、Gemini API Key 或 Vertex AI 三种方式认证，支持 MCP server 扩展工具、GEMINI.md 上下文文件、检查点、令牌缓存与沙箱执行。经 npm/brew/MacPorts 安装，提供 preview/stable/nightly 三个发布通道。README 注明免费层与 Google One 用户已被 Antigravity CLI 取代。

- 三种认证方式：Google OAuth、Gemini API Key、Vertex AI
- MCP server 集成以扩展自定义工具（含 Imagen/Veo/Lyria 媒体生成）
- 非交互脚本模式，支持 JSON 与 stream-json 输出
- preview/stable/nightly 三个发布通道

> L24: Gemini CLI is an open-source AI agent that brings the power of Gemini directly
> L124: ## 🔐 Authentication Options
> L308: Configure MCP servers in `~/.gemini/settings.json` to extend Gemini CLI with

## rasbt/LLMs-from-scratch（⭐106726，confidence: high）

**学习者/研究者：从零用 PyTorch 逐步实现类 GPT 大模型**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

《Build a Large Language Model (From Scratch)》一书的官方代码仓库，按章节组织：用 PyTorch 从零实现、预训练与指令微调一个类 GPT 模型，不依赖外部 LLM 库。包含练习解答、附录材料（BPE 分词器、KV Cache、MoE、DPO 等扩展笔记）以及加载 Llama/Qwen/Gemma 等预训练权重进行微调的代码。配套 17 小时视频课程与 170 页测验 PDF。作者要求不提交偏离印刷书内容的主章节代码贡献。

- 从零实现、预训练与指令微调类 GPT 模型，不使用外部 LLM 库
- 附加 Llama 3.2、Qwen3、Gemma 3 等模型的 From Scratch 实现与预训练权重加载
- 提供 Docker 环境搭建指南与 17 小时配套视频课程
- 包含 DPO 对齐与 RLVR/GRPO 等扩展材料

> L3: This repository contains the code for developing, pretraining, and finetuning a GPT-like LLM and is the official code re
> L32: This book uses PyTorch to implement the code from scratch without using any external LLM libraries. While proficiency in
> L38: The code in the main chapters of this book is designed to run on conventional laptops within a reasonable timeframe and 

## pytorch/pytorch（⭐104823，confidence: high）

**给开发者的 GPU 加速张量计算与动态神经网络 Python 库**

`ai_role=ai-ecosystem · license_risk=none · deploy=desktop · model_dep=— · hardware=cpu-ok · install_friction=low · maturity=—`

提供 GPU 加速的 NumPy 式张量计算与基于 tape 机制的自动微分动态神经网络，组件包括 torch、torch.autograd、torch.nn、torch.multiprocessing 与 torch.utils。定位为深度学习研究平台，强调 Python 优先集成、命令式执行、可扩展的 C/C++ 扩展 API。安装途径为官网提供的 conda/pip 二进制，或从源码构建（需 Python 3.10+、C++20 编译器、10 GB 磁盘等），并分别给出 CUDA、ROCm、Intel GPU 的构建说明。

- GPU 加速张量计算与基于 tape 的自动微分
- 组件划分：torch / autograd / nn / multiprocessing / utils
- 支持 CUDA、AMD ROCm、Intel GPU 三类 GPU 后端构建
- 提供二进制（conda/pip）与源码两种安装途径

> L3: PyTorch is a Python package that provides two high-level features:
> L4: - Tensor computation (like NumPy) with strong GPU acceleration
> L112: Commands to install binaries via Conda or pip wheels are on our website: https://pytorch.org/get-started/locally/
> L158: ##### NVIDIA CUDA Support

## paperclipai/paperclip（⭐103483，confidence: high）

**给团队的 AI 代理编排控制台：目标、预算、治理一体化**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

一个 Node.js 服务器加 React UI，用于编排一组 AI 代理执行业务工作：用户定义目标、按角色组建代理团队（org chart）、审批与运行任务，并在仪表板中跟踪工作与成本。核心机制包括心跳唤醒、原子任务领取与执行锁、预算阈值与硬停、审批门与配置回滚、技能注入与定时例程。可接入多种代理运行时（Claude Code、Codex、Cursor、Gemini CLI 等），支持多组织隔离与模板导出导入。面向需要协调多个代理并控制成本与权限的团队。

- 跨运行时接入任意代理：能接收心跳即可入编（适配器/HTTP/自定义进程扩展）
- 组织级治理：审批门、权限边界、配置版本化与回滚
- 预算与成本控制：按公司/代理/项目维度跟踪花费、阈值告警、硬停
- 任务系统：原子任务领取、阻塞依赖、会话持久化、定时例程（cron/webhook/API 触发）

> L23: Open-source orchestration for teams of AI agents.
> L27: Paperclip is a Node.js server and React UI that orchestrates a team of AI agents to run a business. Bring your own agent
> L77: |**Agentic OS** — The infrastructure that makes the work run.|IT & platform|Cross-provider runtime: any model, any agent

## thedotmack/claude-mem（⭐101357，confidence: high）

**为 AI 编码 Agent 提供跨会话持久记忆的压缩与注入系统**

`ai_role=ai-native · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=—`

以 Claude Code 为主要目标的上下文记忆压缩系统：通过生命周期钩子自动捕获会话中的工具使用观察，生成语义摘要存入 SQLite 与 Chroma 向量库，并在后续会话启动时注入相关上下文。提供 4 个 MCP 搜索工具与三层渐进式检索流程以控制 token 消耗，经 npx 安装器或插件市场接入 Claude Code、OpenCode、T3 Code、OpenClaw 等宿主。安装时需登录或显式指定 provider，免费试用结束后回落到 Anthropic 计划。

- 生命周期钩子自动捕获会话观察并生成语义摘要
- SQLite + FTS5 与 Chroma 混合检索（语义+关键词）
- 4 个 MCP 搜索工具，三层渐进式检索节省 token
- 多宿主支持：Claude Code、OpenCode、T3 Code、OpenClaw、Antigravity 等

> L46:  Persistent memory compression system built for Claude Code.
> L103:  Claude-Mem seamlessly preserves context across sessions by automatically capturing tool usage observations, generating 
> L235: 1. **Lifecycle Hooks** - SessionStart, UserPromptSubmit, PreToolUse, PostToolUse, Stop, SessionEnd. Each is one shell-fr

## Panniantong/Agent-Reach（⭐98621，confidence: mid）

**给 AI Agent 一键配置读取与搜索互联网渠道的 CLI 能力层**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

Agent Reach 定位为能力层：为 Claude Code、OpenClaw、Cursor 等可执行命令行的 Agent 选型、安装并体检各平台的读取工具，覆盖网页、YouTube、RSS、GitHub、Twitter、B站、Reddit、小红书等 17 个渠道。每个平台维护「首选+备选」的有序后端列表，按序真实探测选择可用路径，接入方式失效时切换路由。凭据仅存本地，`agent-reach doctor` 可诊断各渠道状态；安装默认只读检查，显式 `--system` 才修改系统。

- 17 个平台渠道，6 个零配置即用，其余按引导配置登录态
- 每平台「首选+备选」多后端路由，失效自动换路径
- agent-reach doctor 一条命令诊断各渠道可用性
- 凭据本地存储、默认不修改系统的安全安装流程

> L75: |🤖 **兼容所有 Agent**|Claude Code、OpenClaw、Cursor、Windsurf……任何能跑命令行的 Agent 都能用|
> L165: **Agent Reach 是一个能力层（capability layer），不是又一个工具。**
> L178: ├── twitter.py      → twitter-cli ▸ OpenCLI ▸ bird

## hacksider/Deep-Live-Cam（⭐97104，confidence: high）

**给创作者提供单张图片实时换脸与一键视频 deepfake**

`ai_role=ai-native · license_risk=viral · deploy=library · model_dep=local-ok · hardware=— · install_friction=medium · maturity=—`

开源的实时换脸工具：选择一张源人脸图像后，可对图片/视频进行换脸输出，或在摄像头模式下实时替换面部并配合 OBS 推流。功能包括 Mouth Mask 保留原始嘴部动作、多人 Face Mapping、以及基于 execution provider 的多硬件加速路径（CUDA/CoreML/DirectML/OpenVINO/CPU）。安装分预构建版（官网付费 Ultimate 版）与手动源码安装，手动安装需自行下载两个模型文件并配置 Python 环境，需 ffmpeg 等系统依赖。

- 单张图片驱动的实时摄像头换脸与图片/视频换脸
- Mouth Mask 保留原始嘴部、Face Mapping 多人多脸同时替换
- 支持 CUDA、CoreML、DirectML、OpenVINO 等 GPU 加速执行提供者
- 内置内容检查，阻止处理裸露等不当媒体

> L3:  Real-time face swap and video deepfake with a single click and only a single image.
> L173: **Run:** If you don't have a GPU, you can run Deep-Live-Cam using `python run.py`. Note that initial execution will down
> L175: ### GPU Acceleration

## punkpeye/awesome-mcp-servers（⭐96511，confidence: mid）

**面向 AI 应用开发者的 MCP 服务器精选清单**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

一份收录 Model Context Protocol (MCP) 服务器的精选清单（awesome list 形式）。MCP 是开放协议，使 AI 模型通过标准化服务器实现与本地及远程资源的交互；清单聚焦可通过 GitHub 仓库自行安装运行的实现，条目按聚合器、浏览器自动化、数据库、文件系统等数十个类别组织，并用图例标注实现语言（Python/TypeScript/Go/Rust 等）、官方实现标识、本地/云范围与操作系统支持。另提供客户端清单、教程链接与网页版同步目录。

- 按数十个类别组织 MCP 服务器条目（L72-125）
- 图例标注实现语言、官方实现、本地/云范围与操作系统（L42-60）
- 提供网页版目录并与仓库同步（L70）
- 附客户端清单与教程入口（L26, L34-35）

> L16: A curated list of awesome Model Context Protocol (MCP) servers.
> L22: MCP is an open protocol that enables AI models to securely interact with local and remote resources through standardized
> L30: This list is for servers with a GitHub repo you install and run yourself. Looking for a hosted server you just connect t

## vllm-project/vllm（⭐93995，confidence: high）

**面向开发者的 LLM 高吞吐推理与服务引擎**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=research`

vLLM 提供 LLM 推理与服务能力：以 PagedAttention 管理 KV 内存，支持连续批处理、chunked prefill、前缀缓存、投机解码与量化方案（FP8/INT8/GPTQ/AWQ/GGUF 等）；兼容 Hugging Face 200+ 模型架构，输出 OpenAI 兼容 API、Anthropic Messages API 与 gRPC，支持张量/流水线/专家并行及多 LoRA。项目源自 UC Berkeley Sky Computing Lab，由社区维护，通过 uv/pip 安装。

- PagedAttention KV 内存管理与连续批处理
- OpenAI 兼容 API 服务器，另支持 Anthropic Messages API 与 gRPC
- 支持 NVIDIA/AMD/Intel GPU 与 x86/ARM/PowerPC CPU 及 TPU、Ascend 等硬件插件
- 200+ Hugging Face 模型架构，覆盖 MoE、多模态、嵌入模型

> L12: vLLM is a fast and easy-to-use library for LLM inference and serving.
> L37: - OpenAI-compatible API server, plus Anthropic Messages API and gRPC support
> L39: - Support for NVIDIA GPUs, AMD GPUs, Intel GPUs, and x86/ARM/PowerPC CPUs. Additionally, diverse hardware plugins such a

## infiniflow/ragflow（⭐92375，confidence: mid）

**企业级开源 RAG 引擎：融合 Agent 能力为 LLM 提供上下文层**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

RAGFlow 是 infiniflow 维护的开源检索增强生成引擎，结合 Agent 能力为 LLM 提供上下文层。核心机制包括基于模板的分块、文档/数据集级知识编译（生成 Wiki、图谱、树、思维导图等）、多步 Agentic 检索（Low 到 Ultra 四档思考模式）、可追溯引用的可视化分块。支持 Word、PDF、网页等异构数据源接入，提供 API 集成。本地部署支持 Docker 或源码构建，另提供 cloud.ragflow.io 云服务。注意源码构建依赖 Go 1.27、Clang 20 等工具链。

- 模板化分块与文档可视化干预，引用可溯源
- 知识编译生成 Wiki、Graph、Tree、PageIndex 等结构化产物
- Agentic 检索支持 Low/Medium/High/Ultra 四档思考模式
- 支持 Word/PPT/Excel/PDF/网页等多格式数据源

> L57: RAGFlow is a leading open-source Retrieval-Augmented Generation (RAG) engine that fuses cutting-edge RAG with Agent capa
> L131: Local deployment supports both Docker deployment and launching from source. Docker is suitable for quick evaluation, int

## microsoft/ML-For-Beginners（⭐91559，confidence: high）

**面向初学者的 12 周 26 课经典机器学习课程**

`ai_role=ai-knowledge · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

微软 Cloud Advocates 出品的机器学习课程仓库：12 周、26 课、52 个测验，围绕经典机器学习（主要使用 Scikit-learn，不涉及深度学习）。每课含课前/课后测验、讲义、项目步骤、作业与挑战，采用项目式教学法，以世界各地文化数据为案例主题。课程以 Python 为主，部分课提供 R 版本；测验应用可在本地运行或部署到 Azure。提供 50+ 语言翻译及克隆时跳过翻译的 sparse-checkout 方案。

- 12 周 26 课 52 测验的结构化课程，含 PAT 自评工具
- 主要基于 Scikit-learn 的经典机器学习，覆盖回归/分类/聚类/NLP/时间序列/强化学习
- 50+ 语言自动翻译，提供跳过翻译的 sparse-checkout 克隆方式
- 测验应用可本地运行或部署到 Azure

> L49: Cloud Advocates at Microsoft are pleased to offer a 12-week, 26-lesson curriculum all about **Machine Learning**. In thi
> L103: We have chosen two pedagogical tenets while building this curriculum: ensuring that it is hands-on **project-based** and

## PaddlePaddle/PaddleOCR（⭐91276，confidence: high）

**将 PDF/图片文档转为结构化数据的 OCR 与文档解析工具包**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=local-ok · hardware=— · install_friction=medium · maturity=—`

PaddleOCR 将 PDF 与图像转换为 JSON/Markdown 等结构化格式，供下游 LLM/RAG/Agent 应用使用。核心机制包括：面向文档解析的轻量视觉语言模型 PaddleOCR-VL（0.9B）、提供细粒度坐标信息的 PP-StructureV3、支持 100+ 语言的 PP-OCR 系列文本识别模型，以及面向 LLM 微调的数据集构建流水线。以 Python 工具包形式发布于 PyPI，另提供浏览器端 PaddleOCR.js 与 C++ 本地部署方案，支持 NVIDIA GPU、Intel CPU、昆仑芯 XPU 等硬件后端。

- PaddleOCR-VL-0.9B 文档解析 VLM，输出 Markdown/JSON，支持 109 种语言
- PP-StructureV3 将复杂 PDF/图像转为 Markdown 或 JSON 并提供表格单元格与文本坐标
- PP-OCRv6 单模型统一支持 50 种语言，提供 tiny/small/medium 三档部署规模
- 提供 LLM 训练数据集构建流水线，并与 Dify、RAGFlow 等框架集成

> L17: **PaddleOCR converts PDF documents and images into structured, LLM-ready data (JSON/Markdown) with industry-leading accu
> L24: * **SOTA Document VLM**: Featuring **PaddleOCR-VL-1.6 (0.9B)**, the industry's leading lightweight vision-language model
> L39: * **LLM Data Flywheel**: A complete pipeline to build high-quality datasets, providing a sustainable "Data Engine" for f

## opencv/opencv（⭐91204，confidence: mid）

**开源计算机视觉库：提供图像处理与视觉算法**

`ai_role=ai-enhanced · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

OpenCV 是开源计算机视觉库，README 提供主页、文档（5.x）、课程、问答论坛、issue 跟踪及附加功能模块 opencv_contrib 的链接。仓库以 C++ 为主（主题标签含 c-plus-plus），主题标签还涉及计算机视觉、深度学习与图像处理。README 本身不包含安装步骤或 API 说明，仅给出资源入口与贡献指南摘要（每个 issue 一个 PR、需含测试与文档、遵循编码风格等）。

- 提供在线文档（docs.opencv.org 5.x）与问答论坛入口
- 附加功能通过 opencv_contrib 仓库提供
- 以 C++ 为主，主题标签覆盖计算机视觉、深度学习、图像处理

> L1: ## OpenCV: Open Source Computer Vision Library
> L7: * Docs: <https://docs.opencv.org/5.x/>
> L28: * Follow OpenCV on LinkedIn for daily posts showing the state-of-the-art in computer vision & AI

## OpenHands/OpenHands（⭐91122，confidence: high）

**自托管的编码 agent 控制中心：管理多 agent 与自动化**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=idea`

OpenHands Agent Canvas 是一个自托管开发者控制中心，用于启动与编码 agent 的对话并自动化日常任务，如生成报告发布到 Slack、将 GitHub issue 分解为任务。默认本地运行，可连接多个 agent 后端：本地、Docker 容器、VM 或企业基础设施，也可选用 OpenHands Cloud/Enterprise。开箱即用运行开源 OpenHands agent，也支持 Claude Code、Codex、Gemini CLI、Pi、OpenCode 等 ACP 兼容 agent。提供 npm 安装与 Docker 沙箱模式，项目状态为 beta。

- 支持 OpenHands、Claude Code、Codex、Gemini 等 ACP 兼容 agent
- 本地/Docker/VM/云多种后端可切换，不丢失焦点
- 创建定时或 webhook 触发的自动化，集成 Slack、GitHub、Notion 等
- 支持任意 LLM（bring your own model）

> L4:  The self-hosted developer control center for coding agents and automations.
> L29: Agent Canvas runs the open source OpenHands agent out-of-the-box, but can use third-party agents such as Claude Code, Co
> L37: |**Bring your own model**|Use with any LLM|

## ChatGPTNextWeb/NextChat（⭐88852，confidence: high）

**给消费者/开发者提供零配置跨平台 AI 聊天客户端**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=self-host · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

基于 Next.js 的跨平台 AI 聊天助手客户端，提供 Web、iOS、macOS、Android、Linux、Windows 版本。通过环境变量接入 OpenAI、Azure、Gemini、Claude、DeepSeek、百度、字节、阿里、讯飞、ChatGLM 等多家服务，支持自定义模型列表与视觉模型；提供 prompt 模板（mask）、聊天记录自动压缩、WebDAV 同步、访问密码控制，数据存于浏览器本地。可一键部署到 Vercel 或用 Docker 运行，另设有企业版提供私有部署与权限管理。

- 一次部署接入 OpenAI/Azure/Gemini/Claude/DeepSeek/百度/字节/阿里/讯飞/ChatGLM 等多家 API
- 支持 MCP（Model Context Protocol），通过 ENABLE_MCP=true 开启
- 聊天记录自动压缩以支持长对话并节省 token，支持 WebDAV 同步
- 客户端体积约 5MB，覆盖六大平台

> L67: - **Deploy for free with one-click** on Vercel in under 1 minute
> L69: - Fully compatible with self-deployed LLMs, recommended for use with RWKV-Runner or LocalAI
> L176: ### `ANTHROPIC_API_KEY` (optional)

## koala73/worldmonitor（⭐88608，confidence: high）

**面向研究者与分析师的实时全球情报仪表盘**

`ai_role=ai-enhanced · license_risk=viral · deploy=library · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

以 TypeScript 构建的实时全球情报仪表盘，将新闻聚合、地缘政治监测与基础设施追踪整合到统一态势感知界面。提供 3D 地球与 WebGL 平面地图双引擎、31 个 Tier-1 国家的国家不稳定指数（CII v8）、金融雷达、跨流信号关联，并可用 Ollama 本地运行 AI 功能而无需 API key。支持 Web、桌面端（Tauri 2）及六个站点变体，面向 OSINT、地缘政治分析等用途的用户。

- 跨军事、经济、灾害与升级信号的跨流关联
- 31 个 Tier-1 国家的实时 CII v8 评分与 24 小时变化
- 通过 Ollama 本地运行 AI，无需 API key
- 提供 MCP server、REST API、CLI 与 Python/Ruby/Go SDK

> L41: - **Curated news feeds** across global and regional categories, AI-synthesized into briefs
> L47: - **Local AI** — run everything with Ollama, no API keys required
> L107: - **MCP server** — `https://worldmonitor.app/mcp` (Streamable HTTP). Public `tools/list`; `tools/call` authenticates wit

## D4Vinci/Scrapling（⭐88249，confidence: high）

**自适应网页抓取框架：从单次请求到全站爬取**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

Python 网页抓取框架，提供三类能力：Spider 爬虫框架（并发爬取、多会话、断点续爬、AutoThrottle 自适应限速、robots.txt 遵循、内置 JSON/JSONL/CSV/XML 导出）；抓取器体系（Fetcher 支持 TLS 指纹伪装，DynamicFetcher 基于 Playwright，StealthyFetcher 处理 Cloudflare Turnstile 等反爬）；自适应解析（页面结构变更后通过相似度算法重新定位元素）。提供 CLI、MCP 接口、Docker 镜像与 AI Agent Skill。面向爬虫开发者与常规数据采集用户。

- 解析器学习页面变更，自动重新定位元素（adaptive=True）
- StealthyFetcher 开箱处理 Cloudflare Turnstile，DynamicFetcher 基于 Playwright
- Spider 框架支持并发、断点续爬、AutoThrottle 与流式输出
- 提供 MCP 服务、CLI 与 AI Agent Skill 入口

> L55: Scrapling is an adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl.
> L57: Its parser learns from website changes and automatically relocates your elements when pages update. Its fetchers bypass 
> L183: ### AI Features

## unclecode/crawl4ai（⭐85709，confidence: high）

**为 LLM 与 AI Agent 提供网页抓取，输出干净 Markdown**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

开源网页爬取与抓取库，把任意网页转换为面向 LLM 的 Markdown，用于 RAG、AI Agent 与数据管道。提供 Python 库、CLI（crwl）、Docker 自托管服务器与 Crawl4AI Cloud 托管服务四种形态；内置 CSS/XPath/正则等免 LLM 的结构化抽取策略，也支持接入任意 LLM 做 JSON 抽取；通过 Playwright 控制浏览器，支持会话、代理、深爬与自适应爬取。Apache 2.0 协议并要求署名。

- pip 安装后 crawl4ai-setup 一键配置浏览器
- CSS/XPath/正则免 LLM 抽取与 LLM 抽取策略并存
- Docker 自托管 REST API 与 MCP 端点，提供 AMD64/ARM64 镜像
- 云服务提供 /scrape、/extract、/search、/serp、/answer 端点

> L19: Crawl4AI turns any website into clean, LLM-ready Markdown for RAG, AI agents and data pipelines. Run the open-source web
> L100: - 🔎 **CSS and XPath schemas**: fast extraction with no LLM (`JsonCssExtractionStrategy`, `JsonXPathExtractionStrategy`, 
> L157: pip install -U crawl4ai

## tt-a1i/archify（⭐84756，confidence: high）

**面向 coding agent 的交互式架构图生成 skill**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

Archify 是一个可安装到 AI 编码代理的 skill：用户用自然语言描述想法、计划或让代理读取仓库，生成可交互的独立 HTML 图（架构、时序、数据流、ERD 等 10 种类型），支持主题切换、路径追踪、PNG/分享卡导出。输出为单文件 HTML，查看者无需安装 Archify。通过 npx skills 安装，支持 Claude Code、Codex CLI、Cursor、OpenCode，社区另有 DSH 插件接入；更新检查为可关闭的可选网络请求。

- 支持 10 种图类型（架构、工作流、时序、数据流、ERD 等）
- 输出自包含 HTML，查看无需安装本工具
- 支持读取仓库生成带来源依据的架构图
- 通过 npx skills 一条命令安装，支持 4 种 agent

> L9:  Start with an idea, a question, or a plan. Describe it to your AI agent, and Archify turns it into an interactive HTML 
> L26:  Works with Claude Code, Codex, Cursor, and OpenCode
> L48: npx skills add tt-a1i/archify -g

## bytedance/deer-flow（⭐84015，confidence: mid）

**面向开发者的长时程 SuperAgent 编排框架：研究、编码与创作**

`ai_role=ai-native · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=idea`

DeerFlow 是字节跳动开源的 super agent harness，通过编排子代理、记忆、沙箱与可扩展技能来处理耗时数分钟到数小时的任务。安装提供 make setup 交互式向导，引导选择 LLM 提供商、可选网络搜索及沙箱/bash/文件写入等安全偏好，生成 config.yaml 与 .env；另有面向编码代理的一句话引导安装说明。README 详述多种搜索/抓取后端（Brave、Tavily、DuckDuckGo、Serper、InfoQuest、Jina 等）对畸形响应的结构化错误处理，并提供 make doctor 自检与 make support-bundle 问题诊断包。v2.0 为完全重写，v1.x 分支继续维护原 Deep Research 框架。

- 编排子代理、记忆与沙箱的长时程任务 harness
- make setup 交互式向导配置 LLM 提供商与安全偏好
- 多种网络搜索与抓取后端的结构化错误处理
- make doctor 自检与 support-bundle 问题诊断流程

> L12: DeerFlow (**D**eep **E**xploration and **E**fficient **R**esearch **Flow**) is an open-source **super agent harness** th
> L17: > **DeerFlow 2.0 is a ground-up rewrite.** It shares no code with v1. If you're looking for the original Deep Research f
> L103:  This launches an interactive wizard that guides you through choosing an LLM provider, optional web search, and executio

## mlabonne/llm-course（⭐83713，confidence: high）

**面向 LLM 学习者的三阶段课程：路线图与 Colab 笔记本**

`ai_role=ai-knowledge · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

按三部分组织的学习路线：LLM Fundamentals（数学、Python、神经网络、NLP 基础）、The LLM Scientist（构建模型的技术）、The LLM Engineer（构建与部署 LLM 应用）。作者附赠一组可运行的 Colab 笔记本，覆盖自动评估、模型合并、云上微调（Unsloth/Axolotl/TRL）、量化（GGUF/GPTQ/EXL2/AWQ/HQQ）、去重与消融等工具流程，并配套文章与基于该课程合著的 LLM Engineer's Handbook。课程本身声明永久免费。

- 三部分路线图：基础、LLM Scientist、LLM Engineer
- 8 个自动化工具笔记本（LLM AutoEval、LazyMergekit、AutoQuant 等）
- 6 个微调教程笔记本覆盖 Llama/Mistral/CodeLlama
- 量化教程覆盖 GGUF、GPTQ、EXL2、AWQ、HQQ 格式

> L8: LLM EngineerThe LLM course is divided into three parts:
> L21: A list of notebooks and articles I wrote about LLMs.
> L29: |🧐 LLM AutoEval|Automatically evaluate your LLMs using RunPod|Open In Colab|

## rtk-ai/rtk（⭐83713，confidence: high）

**压缩开发命令输出的 CLI 代理，降低 agent 读取的 token 消耗**

`ai_role=ai-ecosystem · license_risk=dual · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

RTK 以 shell hook 方式拦截 agent 的命令调用，在输出进入 LLM 上下文前按命令类型做过滤、分组、截断与去重，覆盖 git、cargo、npm、pytest、docker 等 100+ 命令。单个 Rust 二进制、无运行时依赖，安装后通过 `rtk init` 为各编码 agent 配置集成；`rtk gain` 提供节省统计。部分版本含 BUSL-1.1 授权的可选 proxy 守护进程，将压缩扩展到 provider API 流量。注意 README 明确节省比例仅针对 bash 输出部分，不等于整体账单降幅。

- 支持 18 个 AI 编码工具的 hook/规则集成（Claude Code、Copilot、Cursor、Gemini CLI 等）
- 覆盖 100+ 开发命令的输出过滤，宣称 <10ms 开销
- 按 Apache-2.0 与 BUSL-1.1 双版本分发（oss 版无压缩引擎）
- 可选 rtk-proxy 守护进程处理 provider API 流量并支持模型路由

> L31: rtk filters and compresses command outputs before they reach your LLM context. Single Rust binary, 100+ supported comman
> L143: RTK supports 18 AI coding tools. Each integration rewrites shell commands to `rtk` equivalents, reducing the bash output
> L147: |**Claude Code**|`rtk init -g`|PreToolUse hook (native binary)|

## Developer-Y/cs-video-courses（⭐83691，confidence: high）

**为学生收录带视频讲授的计算机科学课程链接清单**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=medium · maturity=—`

以列表形式收录大学（学院）级别的计算机科学课程及其视频讲授链接，覆盖计算机科学导论、数据结构与算法、系统编程、操作系统等方向，条目标注学校、教师、学期并附视频播放列表、讲义或课程网站链接。收录标准为正式的大学级别课程，明确排除小型 MOOC、基础教程与站点广告。项目通过 CONTRIBUTING.md 接受 PR 贡献，并对空 issue 等行为设有限制规则。

- 按学科分类组织大学级别课程链接清单
- 每条附视频播放列表/课程网站/讲义链接
- 收录 UNSW、MIT、Stanford、Berkeley、IIT 等多校课程
- PR 贡献制并设有收录标准（排除基础教程与广告）

> L1: # Computer Science courses with video lectures
> L8: - You are welcome to contribute, please create PR for actual college/University level courses. Please do not add links f
> L14: ## Courses

## datawhalechina/hello-agents（⭐83499，confidence: high）

**面向开发者的从零构建智能体系统开源教程**

`ai_role=ai-native · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Datawhale 社区出品的系统性智能体学习教程，共 16 章，覆盖智能体基础、经典范式（ReAct、Plan-and-Solve、Reflection）、低代码平台使用、主流框架应用、自研框架 HelloAgents 构建、RAG 与记忆、上下文工程、MCP 等通信协议、Agentic RL 训练与性能评估，并附智能旅行助手、DeepResearch 复现、赛博小镇等实战案例。提供在线阅读、PDF 下载与配套代码。要求读者具备基础 Python 能力与 LLM 概念性了解，采用 CC BY-NC-SA 4.0 协议。

- 16 章教程覆盖从 LLM 基础到多智能体应用的全流程
- 基于 OpenAI 原生 API 从零构建自研框架 HelloAgents
- 提供配套代码仓库与社区贡献章节（面试题、踩坑经验等）
- 提供在线阅读、国内加速访问与 PDF 下载渠道

> L22: &emsp;&emsp;Hello-Agents 是 Datawhale 社区的 系统性智能体学习教程 。如今 Agent 构建主要分为两派，一派是 Dify，Coze，n8n 这类软件工程类 Agent，其本质是流程驱动的软件开发，LLM
> L37: - 🛠️ 自研框架 HelloAgents 基于 Openai 原生 API 从零构建一个自己的智能体框架
> L103: &emsp;&emsp;本项目内容兼顾理论与实战，旨在帮助你系统性地掌握从单个智能体到多智能体系统的设计与开发全流程。因此，尤其适合有一定编程基础的 AI 开发者、软件工程师、在校学生 以及对前沿 AI 技术抱有浓厚兴趣的 自学者 。在学习

## lobehub/lobehub（⭐83291，confidence: mid）

**多智能体协作平台：像团队一样雇佣、调度、汇报 AI 代理**

`ai_role=ai-native · license_risk=none · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=idea`

LobeHub 是一个面向多智能体协作的工作空间：以 Agent 为工作单元，提供 Agent Builder 一键生成智能体配置、Agent Groups 并行协作、Pages 共享上下文协作写作、Schedule 定时运行、Workspace 团队空间，以及结构化可编辑的 Personal Memory 持续学习机制。声称支持 10,000+ 技能工具与 MCP 兼容插件。支持通过 Vercel、Zeabur、Sealos、阿里云或 Docker 镜像自行部署，配置 OPENAI_API_KEY 等环境变量后使用。README 注明项目仍在活跃开发中。

- Agent Builder 一句话生成智能体配置
- Agent Groups 多智能体并行协作与定时调度
- 10,000+ 工具/MCP 兼容插件库
- 结构化、可编辑的白盒 Personal Memory

> L76: LobeHub is a work-and-lifestyle space to find, build, and collaborate with agent teammates that grow with you. In LobeHu
> L93: - **Unified Intelligence**: Seamlessly access any model and any modality—all under your control.
> L128: LobeHub provides Self-Hosted Version with Vercel, Alibaba Cloud, and [Docker Image][docker-release-link]. This allows yo

## netdata/netdata（⭐80985，confidence: high）

**为基础设施团队提供每秒级实时监控与 ML 异常检测**

`ai_role=ai-enhanced · license_risk=viral · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Netdata 是开源实时基础设施监控平台，Agent 部署在被监控节点上执行采集、存储、边缘 ML 训练与告警，覆盖系统资源、存储、网络、容器、虚拟机、日志、云服务与 800+ 集成；采用 Parent-Child 架构实现集中化与横向扩展，可选连接 Netdata Cloud 获得多节点视图与 RBAC，数据保留在本地基础设施。存储约 0.5 字节/样本，生产环境默认资源占用约 5% CPU、150MiB RAM。

- 每秒级指标采集与实时可视化（1 秒延迟）
- 边缘训练 ML 模型做每指标无监督异常检测
- 800+ 集成，自动发现节点上的指标
- 指标可导出至 Prometheus、InfluxDB、OpenTSDB、Graphite 等

> L42: Netdata is an open-source, real-time infrastructure monitoring platform. Monitor, detect, and act across your entire inf
> L83: |**ML-Powered**|Unsupervised anomaly detection|Trains multiple ML models per metric at the edge|
> L232: |**Edge-Based ML**|• ML models trained at the edge • Automatic anomaly detection per metric • Pattern recognition based 

## dair-ai/Prompt-Engineering-Guide（⭐79259，confidence: high）

**面向研究者与开发者的提示工程指南：论文、课程、笔记本与资源合集**

`ai_role=ai-knowledge · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

由 DAIR.AI 维护的提示工程指南，汇集提示工程相关论文、学习指南、讲座、引用与工具，覆盖零样本/少样本、思维链、ReAct、RAG 等技术主题，并按模型（ChatGPT、LLaMA、Mistral 等）与应用场景组织章节；提供网页版与 13 种语言翻译，配套 DAIR.AI Academy 的付费课程。本地运行需 Node >=18 与 pnpm，以 Next.js/Nextra 构建文档站点。

- 覆盖零样本、思维链、ReAct、ToT、RAG 等提示技术章节
- 支持 13 种语言的翻译版本
- 提供 1 小时视频讲座及配套 notebook 与幻灯片
- 含模型、应用、风险、论文、工具、数据集等分类指引

> L5: Prompt engineering is a relatively new discipline for developing and optimizing prompts to efficiently use language mode
> L7: Motivated by the high interest in developing with LLMs, we have created this new prompt engineering guide that contains 
> L123: 1. Install the dependencies: `pnpm i next react react-dom nextra nextra-theme-docs`

## shareAI-lab/learn-claude-code（⭐78745，confidence: low）

**教学仓库：从 0 到 1 构建类 Claude Code 的 agent harness**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

一个 harness 工程教学课程，用 Python 从零实现类 Claude Code 的 agent 运行时，分 17 个递进章节，每章只讲一个机制：agent loop、工具注册、权限、hooks、TodoWrite、subagent、技能按需加载、上下文压缩、记忆、文件任务系统、后台任务、定时任务、MCP、多 agent 团队等。核心论点是「智能来自模型，工程者的工作是构建 harness」。每章含英/中/日三语 README 与可运行 code.py。属教学材料，非生产框架。

- 17 个递进章节，每章实现一个 harness 机制并提供可运行 code.py
- 以单一 agent loop 为核心，工具经 dispatch map 注册
- README 提供英文、中文、日文三语版本
- 保留 legacy 12 课版本并提供新旧章节映射表

> L5: # Learn Claude Code -- Harness Engineering for Real Agents
> L124:  The root-level `s01_*` ... `s17_*` folders are the canonical version. Each chapter contains an English default README, 
> L156: > **s01** &nbsp; *"One loop & Bash is all you need"* &mdash; one tool + one loop = one agent

## unslothai/unsloth（⭐78179，confidence: high）

**在本地运行和微调 LLM 与扩散模型的桌面应用**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

Unsloth 提供三种使用形态：桌面应用（Unsloth Desktop）、Web UI（Unsloth Studio）与代码库（Unsloth Core）。功能覆盖本地运行与训练 LLM、GGUF、MLX、扩散、嵌入、音频等模型；微调支持 LoRA、QLoRA、GRPO、DPO、FP8 等；提供 OpenAI 兼容 API、RAG/搜索、LAN 与 Cloudflare 远程访问；通过 unsloth start 一条命令将 Claude Code、Codex 等 agent 接到本地模型。支持 Windows/macOS/Linux，含 Docker 镜像与免费 Colab 类 notebook。

- 运行与训练 LLM、GGUF、MLX、扩散、嵌入、音频模型
- 微调支持 RL、LoRA、QLoRA、GRPO、DPO、FP8，导出 GGUF/NVFP4/FP8
- unsloth start 命令连接 Claude Code、Codex、MCP 等本地 agent
- 提供 OpenAI 兼容 API、RAG、LAN/Cloudflare 远程访问

> L6: Unsloth is the first desktop app to run and train models.
> L78: * Run and train LLMs, MLX, GGUF, diffusion, decision, embedding, audio models: Qwen3.8, GLM-5.3-Flash, Kimi K3, Qwen-Ima
> L86: * **Fine-tuning:** Train LLMs, diffusion, decision, TTS, and embedding models 2× faster with 70% less VRAM with no accur

## tensorflow/models（⭐77646，confidence: high）

**TensorFlow 用户的 SOTA 模型与建模方案实现仓库**

`ai_role=ai-ecosystem · license_risk=none · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

TensorFlow Model Garden 仓库，包含四部分：official（官方维护、基于 TF2 高层 API 的 SOTA 模型示例实现）、research（研究者维护的 TF1/TF2 研究模型）、community（社区模型仓库清单）与 orbit（自定义训练循环库，集成 tf.distribute，支持 CPU/GPU/TPU）。面向用 TensorFlow 做研究与产品开发的用户，提供训练日志（TensorBoard.dev），可通过 pip 包或克隆源码安装。

- official/research/community/orbit 四类模型集合
- orbit 训练循环库支持 CPU、GPU 与 TPU
- 提供 tf-models-official 稳定版与 tf-models-nightly 每日构建包
- 部分模型提供 TensorBoard.dev 训练日志

> L7: implementations of state-of-the-art (SOTA) models and modeling solutions for
> L9: TensorFlow users can take full advantage of TensorFlow for their research and
> L21: |orbit|• A flexible and lightweight library that users can easily use or fork when writing customized training loop code

## microsoft/ai-agents-for-beginners（⭐77340，confidence: high）

**面向初学者的 AI Agent 构建 18 课教程课程**

`ai_role=ai-knowledge · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

微软官方出品的 AI Agent 教学课程，共 18 课，内容覆盖 Agent 基础概念、设计模式（工具使用、规划、多智能体、元认知）、Agentic RAG、MCP/A2A 协议、上下文工程、记忆管理、生产部署与安全等。每课含文字教材、短视频、Python 代码示例与扩展资源。代码示例使用 Microsoft Agent Framework 与 Microsoft Foundry Agent Service V2，需要 Azure 账户；部分示例兼容 OpenAI 兼容服务商（如 MiniMax）。

- 18 节课程，每课含文字教材、视频、Python 代码示例
- 覆盖设计模式、Agentic RAG、MCP/A2A 协议、记忆与安全等主题
- 代码示例基于 Microsoft Agent Framework 与 Foundry Agent Service V2
- 提供 50+ 语言翻译版本，支持 sparse checkout 加速克隆

> L5: ## A course teaching everything you need to know to start building AI Agents
> L69: This course uses the following AI Agent frameworks and services from Microsoft:
> L71: - Microsoft Agent Framework (MAF)

## tesseract-ocr/tesseract（⭐77041，confidence: high）

**OCR 引擎：为开发者提供图片文字识别库与命令行工具**

`ai_role=ai-enhanced · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

包含 OCR 引擎 libtesseract 与命令行程序 tesseract 两个部分。第 4 版引入基于 LSTM 神经网络的行识别引擎，同时通过 --oem 0 兼容第 3 版的字符模式识别引擎。支持 Unicode/UTF-8，开箱可识别 100 多种语言，支持 PNG、JPEG、TIFF 等图像输入，输出纯文本、hOCR、PDF、TSV、ALTO、PAGE 等格式。不含 GUI，可通过 tessdata 训练数据支持更多语言，开发者可经 C/C++ API 或多语言 wrapper 集成。依赖 Leptonica 库读取图像。

- 提供 libtesseract 库与 tesseract 命令行程序两种使用方式
- 支持 LSTM 引擎与 Legacy 引擎两种 OCR 模式（--oem 切换）
- 开箱支持 100 多种语言，输出文本/hOCR/PDF/TSV/ALTO/PAGE 等格式
- 提供 C/C++ API 与其他语言的 wrapper 绑定

> L14: This package contains an **OCR engine** - `libtesseract` and a **command line program** - `tesseract`.
> L16: Tesseract 4 adds a new neural net (LSTM) based OCR engine which is focused on line recognition, but also still supports 
> L22: Tesseract has **unicode (UTF-8) support**, and can **recognize more than 100 languages** "out of the box".

## openai/openai-cookbook（⭐76666，confidence: high）

**为 OpenAI API 使用者提供示例代码与任务指南**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

OpenAI 官方维护的示例代码与指南合集，覆盖使用 OpenAI API 完成常见任务的方法。示例以 Python 为主，概念可迁移到其他语言。运行示例需要 OpenAI 账号与 API key，通过 OPENAI_API_KEY 环境变量或 .env 文件配置。内容在 cookbook.openai.com 提供导航，项目采用 MIT 许可证。

- 常见任务的示例代码与指南合集
- 示例以 Python 为主，概念可应用于其他语言
- 通过 OPENAI_API_KEY 环境变量或 .env 文件配置密钥
- MIT 许可证开源

> L9: Example code and guides for accomplishing common tasks with the OpenAI API. To run these examples, you'll need an OpenAI
> L11: Most code examples are written in Python, though the concepts can be applied in any language.

## headroomlabs-ai/headroom（⭐75573，confidence: mid）

**为 AI agent 压缩上下文输入输出的本地压缩层**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

在工具输出、日志、RAG 片段、文件与对话历史进入 LLM 前进行压缩，以 Python/TypeScript 库、本地代理、agent 包装命令和 MCP server 四种形式提供。内部按内容类型路由到不同压缩器（JSON/代码/文本），原文本地缓存并可通过 headroom_retrieve 按需取回。还提供输出 token 削减（verbosity steering、effort routing）与跨 agent 共享记忆。压缩在本地运行，不外发内容。

- 库、代理、wrap 命令、MCP server 四种接入方式
- CCR 机制本地缓存原文，可按需取回
- 支持 20 余种 agent CLI 的一键包装与还原
- 输出 token 削减开关与 savings/评估命令

> L26: Headroom compresses everything your AI agent reads — tool outputs, logs, RAG
> L38: - **Library** — `compress(messages)` in Python or TypeScript, inline in any app.
> L41: - **MCP server** — `headroom_compress`, `headroom_retrieve`, `headroom_stats` for any MCP client.

## hiyouga/LlamaFactory（⭐75539，confidence: high）

**面向开发者的 100+ LLM/VLM 统一微调工具**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=idea`

以 CLI 与零代码 Web UI 提供 100+ 大语言模型与视觉语言模型的微调能力，覆盖预训练、SFT、奖励建模及 PPO/DPO/KTO/ORPO 等训练方法，支持 LoRA 与多比特 QLoRA 量化微调。内置数十个模型对话模板，提供 Hugging Face 数据集清单、TensorBoard/Wandb 等实验监控，并可经 vLLM/SGLang worker 以 OpenAI 风格 API、Gradio UI 或 CLI 推理。README 给出按训练方法与模型规模估算的显存需求表，支持本地训练与 Colab/PAI-DSW/AMD GPU Cloud 云端训练。

- 支持 100+ LLM/VLM 与 8 种训练方法（Pre-Training/SFT/Reward/PPO/DPO/KTO/ORPO/SimPO）
- LoRA 与 2/3/4/5/6/8-bit QLoRA 量化微调
- 零代码 CLI 与 Web UI，附带 OpenAI 风格 API 与 vLLM/SGLang 推理 worker
- 内置大量中英文训练数据集清单与模型模板管理

> L35: ### Easily fine-tune 100+ large language models with zero-code CLI and Web UI
> L68: - **Various models**: LLaMA, LLaVA, Mistral, Mixtral-MoE, Qwen3, Qwen3-VL, DeepSeek, Gemma, GLM, Phi, etc.
> L69: - **Integrated methods**: (Continuous) pre-training, (multimodal) supervised fine-tuning, reward modeling, PPO, DPO, KTO

## career-ops-hq/career-ops（⭐75331，confidence: high）

**给求职者的本地 AI 求职 agent：评分匹配并代拟申请材料**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

运行在用户已有 AI CLI（Claude Code、Codex 等）中的求职辅助系统：粘贴职位后检查岗位是否仍开放、按用户真实 CV 做 A-H 多维评估（1-5 评分、低于 4.0 提示不投）、生成 ATS 可读 PDF 简历与求职信草稿、STAR+R 面试准备、申请追踪与漏斗统计。设计上不自动提交、不发邮件、无遥测，数据全部留在本机；支持批量无头 worker、100+ 公司门户扫描、可选插件集成。经 npx 或全局 npm 安装。

- 按用户 CV 对职位做 A-H 评估打分（1-5），低于 4.0 默认劝阻投递并允许覆盖
- ATS 可读简历与求职信 PDF 生成（HTML + Playwright 流水线）
- 人工在环设计：脚本不 POST、不发邮件，用户亲自点击 Submit
- 批量并行评估、重发检测、拒绝模式分析与终端 TUI 看板

> L76:  Open source. Local. In the AI CLI you already use. Free and local models included.
> L110: - **Where does it all go?** Every application stays on your machine. Nothing is uploaded to us.
> L171: claude   # or codex / qwen / opencode / agy / grok — open your AI CLI here

## binhnguyennus/awesome-scalability（⭐74788，confidence: low）

**面向工程师的大规模系统可扩展性架构文章阅读清单**

`ai_role=ai-knowledge · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=medium · maturity=—`

以阅读清单形式组织大型分布式系统的架构模式与实践案例，内容分为原理、可扩展性、缓存、分布式锁、调度、监控告警、安全、消息流等多个主题章节；条目多为 Netflix、Uber、Google、LinkedIn 等公司工程博客与知名工程师文章链接。README 按场景组织入口（系统变慢、系统宕机、系统设计面试、团队建设），并接受社区通过 pull request 提交和移除失效链接。纯文档型仓库，无代码与安装步骤。

- 按原理/可扩展性/缓存/调度/监控/安全等主题组织的文章目录
- 收录多家科技公司的实战架构案例研究
- 面向系统变慢、宕机、面试、组队四类场景的导航入口
- 社区协作维护，接受 PR 更新失效链接

> L3: An updated and organized reading list for illustrating the patterns of scalable, reliable, and performant large-scale sy
> L23: ## Content
> L86: ## Scalability

## thedaviddias/Front-End-Checklist（⭐74489，confidence: high）

**为开发者与 AI agent 提供前端质量检查清单与规则库**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

将前端最佳实践整理为 386 条规则、11 个类别的检查清单，覆盖 HTML、CSS、JavaScript、性能、可访问性、SEO、安全等，每条规则按 Critical/High/Medium/Low 分级。提供三种使用路径：网站在线浏览与筛选、MCP 服务器（托管端点与本地 stdio 服务器，暴露 11 个工具如 review_code、audit_url、search_rules）供 agent 做代码审查与 URL 审计，以及 npx 安装的 skills 形式审计工作流。规则贡献通过 pnpm 脚本本地开发与校验。

- 386 条规则覆盖 11 个活跃类别，按四级优先级标注
- 托管 MCP 服务器暴露 11 个工具，支持代码审查与公开 URL 审计
- 提供 npx 安装的 skills 形式审计工作流（如 https 专项）
- 规则页含解释、修复指引、验证步骤与 AI prompts

> L11: Front-End Checklist is the open-source front-end quality system for humans and AI agents. It turns front-end best practi
> L27: - `11` MCP tools exposed by the hosted server
> L66: Connect an MCP-capable agent to Front-End Checklist for frontend code review, structured rule lookup, audits, and remedi

## openbq-org/OpenBB（⭐74340，confidence: high）

**为量化分析师与 AI agent 提供统一金融数据接入的开源平台**

`ai_role=ai-ecosystem · license_risk=none · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

OpenBB 的开放数据平台（ODP）是帮助数据工程师将专有、授权与公开数据源整合进下游应用的 Python 工具集，面向量化人员、分析师与 AI agent。核心机制为"一次连接、多处消费"：同一数据层同时暴露给 Python 环境、OpenBB Workspace/Excel、MCP 服务器与 REST API。安装通过 PyPI 的 pip 完成，`openbb-api` 命令可启动 FastAPI/Uvicorn 本地服务（127.0.0.1:6900）。数据准确性免责声明明确提示不保证准确。

- 提供统一 Python 接口访问股票、加密、衍生品、固收等金融数据
- 支持 REST API、MCP server、Python 多种消费方式
- openbb-api 一键启动 FastAPI 本地数据后端
- 可与 OpenBB Workspace 企业 UI 连接使用

> L15: Open Data Platform by OpenBB (ODP) is the open-source toolset that helps data engineers integrate proprietary, licensed,
> L17: ODP operates as the "connect once, consume everywhere" infrastructure layer that consolidates and exposes data to multip
> L72: This will launch a FastAPI server, via Uvicorn, at `127.0.0.1:6900`.

## debpalash/VoiceStudio（⭐72657，confidence: high）

**本地运行的开源语音工作台：克隆、配音、转写与有声书制作**

`ai_role=ai-enhanced · license_risk=dual · deploy=desktop · model_dep=— · hardware=cpu-ok · install_friction=medium · maturity=—`

基于 Electron 的桌面语音工作台，默认引擎为 k2-fsa/OmniVoice，支持语音克隆、语音设计、视频配音、听写、转写与有声书批量制作，覆盖 646 种语言。本地工作流在用户硬件上运行，按 GPU/CPU 提供不同加速方式（CUDA、Metal、CPU），并可安装管理本地语音模型；提供本地 API 与 MCP 接入供 agent 调用，支持配方与监视文件夹。Tauri 桌面壳已移除，Electron 为唯一桌面应用与 Web UI。

- 语音克隆、语音设计、视频配音、听写、转写、有声书制作，支持 646 种语言
- CUDA / Metal (MPS) / CPU 三类硬件加速路径，无独显也可用（较慢）
- 本地 API 与 MCP 接口，支持 agent 集成与监视文件夹等自动化
- 一键安装脚本覆盖 macOS/Linux/Windows，也可从源码运行

> L30: Start with **VoiceStudio** (default, powered by k2-fsa/OmniVoice), or choose another engine. Features & engine catalog.
> L72: |NVIDIA GPU (Windows / Linux)|CUDA acceleration|
> L108: > **Electron is the only desktop app and web UI.** Version 0.5.3 was the final Tauri release. Existing Tauri users must 

## Fission-AI/OpenSpec（⭐72217，confidence: high）

**为 AI 编码助手提供规范化规格开发（SDD）工作流的 CLI 工具**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

OpenSpec 以 CLI 形式在项目中建立 specs/changes 目录结构，让人与 AI 助手在写代码前先对齐规格：AI 按斜杠命令（/opsx:explore、/opsx:propose 等）读取代码并生成 Markdown 格式的需求与场景，由人审核后再进入实现。每个变更独立成目录，包含提案、规格、设计与任务。支持 30+ AI 编码工具，通过 openspec init 生成对应命令形式；提供 beta 阶段的 Stores 机制支持跨仓库团队共享规格。需 Node.js 20.19.0+，经 npm 或 Homebrew 安装。

- 通过 /opsx:explore、/opsx:propose 等斜杠命令驱动 AI 生成 Markdown 规格
- 支持 30+ AI 编码工具，init 自动输出各工具的命令形式
- Stores 机制（beta）支持跨仓库、团队共享的规格存储
- openspec update 可刷新各项目内 AI 指引

> L134: - **Use your tools** — works with 30+ AI assistants via slash commands
> L129: AI coding assistants are powerful but unpredictable when requirements live only in chat history. OpenSpec adds a lightwe

## binary-husky/gpt_academic（⭐71496，confidence: mid）

**为学术用户提供LLM交互接口，优化论文阅读润色写作**

`ai_role=ai-enhanced · license_risk=viral · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

一个面向学术场景的LLM交互前端，围绕论文阅读/润色/写作提供插件化功能：LaTeX/PDF论文翻译与总结、arxiv论文精细翻译、语法校对、代码项目剖析与自译解、批量注释生成等。支持通过functional.py动态生成自定义按钮与热更新函数插件，可并行问询多种模型，支持多API-key负载均衡与本地模型后端（ChatGLM/MOSS/RWKV）。Windows/Linux/macOS可直接运行，另提供Docker与一键脚本部署。

- 一键解读/翻译latex与pdf论文并生成摘要，支持arxiv精细翻译
- 虚空终端：用自然语言调度本项目其他插件
- 插件支持热更新，按钮由functional.py动态生成可自定义
- 多LLM并行问询，多API-key共存与负载均衡

> L12:  GPT 学术优化 (GPT Academic)
> L32: 功能（⭐= 近期新增功能） | 描述
> L43: 读论文、翻译论文 | [插件] 一键解读latex/pdf论文全文并生成摘要

## FoundationAgents/MetaGPT（⭐70895，confidence: high）

**多智能体框架：模拟软件公司角色协作完成复杂任务**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

MetaGPT 接收一行需求作为输入，输出用户故事、竞品分析、需求文档、数据结构、API 等产物；内部模拟软件公司中的产品经理、架构师、项目经理、工程师等角色，通过编排 SOP（Code = SOP(Team)）驱动 LLM 组成的团队协作。以 Python 库与 CLI 形式提供，需 Python 3.9–3.12，实际使用前需安装 node 和 pnpm，支持 pip/源码/docker 安装，并支持以库形式调用与 Data Interpreter 写代码。

- 一行需求生成用户故事/需求/数据结构/API 等多类产物
- 内置产品经理/架构师/项目经理/工程师等 LLM 角色与 SOP 编排
- 支持 CLI 用法与 Python 库调用，附 Data Interpreter 数据分析角色
- 配置中支持 openai/azure/ollama/groq 等多种 LLM 接入类型

> L31: 1. MetaGPT takes a **one line requirement** as input and outputs **user stories / competitive analysis / requirements / 
> L32: 2. Internally, MetaGPT includes **product managers / architects / project managers / engineers.** It provides the entire
> L69:   api_type: "openai"  # or azure / ollama / groq etc. Check LLMType for more options

## rohitg00/ai-engineering-from-scratch（⭐70583，confidence: high）

**面向开发者的 AI 工程免费开源课程（542 课/20 阶段）**

`ai_role=ai-knowledge · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

以 MIT 许可发布的 AI 工程课程仓库，含 542 节课、20 个阶段，覆盖模型内部机制、检索管线与 agent 运行时，使用 Python、TypeScript、Rust、Julia。提供三种学习方式：网站阅读、编码 agent 当导师（通过 npx 安装 Agent Skills，支持 Codex、Claude Code 等宿主）、本地克隆运行代码。含 3 个带本地评分器的分阶段项目与十题定位测验生成个性化学习计划。

- 542 节课、20 个阶段，提供 23 种语言翻译
- 3 个分阶段项目（检索评估、trace 调试、工具调用防火墙）带本地评分器与参考实现
- AI 导师模式：npx skills add 安装后由 Codex/Claude Code 等宿主调用学习技能
- 十题定位测验映射起点阶段并生成个性化学习计划

> L3: Implement model internals, retrieval pipelines, and agent runtimes. Test them, inspect failures, and keep the code and e
> L149: If Node.js, `npx`, and a skill-capable coding agent are already installed, your coding agent can become your tutor. A re
> L152: npx skills add rohitg00/ai-engineering-from-scratch

## code-yeongyu/oh-my-openagent（⭐70134，confidence: high）

**单命令编码 Agent：编排多 Agent 图执行研究与编码任务**

`ai_role=ai-native · license_risk=none · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

OmO 是一个通过 `omo` 命令运行的终端编码 Agent，运行在自研的 senpi（pi 的 fork）之上。在提示中加入 `ulw` 或 `mass ulw` 可将任务展开为多 Agent 图，各部分在不同模型上并行执行并逐一校验；内置以 git 仓库中 markdown 文件存储的记忆系统、按任务加载的技能、会话恢复（/resume、omo -c）等机制。安装方式为官方安装脚本或 npm/bun 全局包（包名 omo-ai），提供 Windows PowerShell 安装路径。

- `mass ulw` 关键词将任务展开为多 Agent 图并行执行
- 记忆系统存储于 git 仓库中的 markdown 文件，由辅助模型读取并提示主 Agent
- /login 支持 Claude、ChatGPT、Kimi、GLM 订阅登录，每个模型配套专用系统提示
- 独立工具调用合并执行，支持长任务断点续做与配置热加载

> L40: OmO is one `omo` command that turns your tokens into finished work: research across ten thousand sources, a deck people 
> L65: **Hundreds of agents, one keyword.** Type `mass ulw` and the whole job becomes a graph of agents: deep research over tho

## microsoft/AI-For-Beginners（⭐69913，confidence: high）

**面向 AI 初学者的 12 周 24 课系统课程**

`ai_role=ai-knowledge · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

微软出品的 12 周、24 课时人工智能入门课程，内容含符号 AI（知识表示与推理）、神经网络与深度学习、计算机视觉、自然语言处理、遗传算法、多智能体系统与 AI 伦理等模块，每课提供 Jupyter Notebook、测验和实验，代码以 PyTorch 与 TensorFlow 双框架呈现。仓库含 50+ 语言自动翻译、本地/ Codespace 运行指引与可本地部署的测验应用，课程明确不覆盖经典机器学习、业务 AI 与云平台实操等主题。

- 24 课时覆盖符号 AI 到 LLM 的完整路径
- 每课含可执行 Jupyter Notebook，支持 PyTorch/TensorFlow/Keras 双框架
- 50+ 语言翻译由 GitHub Action 自动维护
- 附测验应用（可本地运行或部署至 Azure）与实验 Lab

> L21: Explore the world of **Artificial Intelligence** (AI) with our 12-week, 24-lesson curriculum! It includes practical less
> L64: * Different approaches to Artificial Intelligence, including the "good old" symbolic approach with **Knowledge Represent
> L124: * Executable Jupyter Notebooks, which are often specific to the framework (**PyTorch** or **TensorFlow**). The executabl

## asgeirtj/system_prompts_leaks（⭐69793，confidence: high）

**收录各家聊天产品系统提示词原文的资料集**

`ai_role=ai-knowledge · license_risk=viral · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

以 Markdown 目录形式聚合多家 AI 产品的系统提示词全文，按厂商分节（Anthropic、OpenAI、Google、xAI、Meta、Perplexity、Cursor、Moonshot、DeepSeek、Qwen、Microsoft 等），每个条目附链接指向仓库内文件；维护“最近新增”变更表，标注旧模型与弃用功能的提示词归档分区；欢迎通过 PR 提交新抓取结果，README 声明定期更新。仓库为纯资料集合，无安装或运行说明。

- 收录 20 余家厂商产品的系统提示词原文链接
- Claude 按模型版本、Claude Code 形态（桌面/云/headless/子代理）分目录
- OpenAI 区分 ChatGPT、Codex、API 注入提示词与弃用功能分区
- 维护带日期的最近新增/变更表

> L10: # System Prompts Leaks
> L12: The full verbatim system prompts behind the most popular chatbots in the world. Carefully curated and complete. Feel fre

## usestrix/strix（⭐69150，confidence: mid）

**面向开发者与安全团队的自主 AI 渗透测试 agent 工具**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

以 CLI 形式运行的自主渗透测试 agent：动态运行目标代码、发现漏洞并以实际 PoC 验证，覆盖 OWASP Top 10 类漏洞；支持多 agent 编排（Graph of Agents）分布式测试、SAST+DAST、自动生成补丁与合规报告，并可接入 GitHub Actions CI。运行依赖 Docker 沙箱与外部 LLM API key，推荐模型默认为 OpenRouter 上的 GLM-5.3；另提供 Strix Cloud 托管平台与企业版（SSO、VPC/自托管），本地 Web 查看器以 strix view 启动。

- 多 agent 编排：侦察/利用/后渗透分工协作
- 以可运行 PoC 验证漏洞，并自动生成修复补丁与合规报告
- 支持 OpenAPI/Swagger/Postman 合约驱动的 API 测试与无头模式
- 可接入外部 MCP 服务器扩展 agent 工具

> L30: Strix are autonomous AI penetration testing agents that act just like real hackers - they run your code dynamically, fin
> L55: - An LLM API key from any supported provider (OpenAI, Anthropic, Google, etc.)
> L148: - **Distributed Pentesting** - Specialized AI agents for recon, exploitation, and post-exploitation

## calesthio/OpenMontage（⭐69085，confidence: high）

**把 AI 编码助手变成完整视频制作工作室的 agentic 系统**

`ai_role=ai-native · license_risk=viral · deploy=library · model_dep=local-ok · hardware=— · install_friction=high · maturity=—`

OpenMontage 是一套以 agent 驱动的视频生产系统：12 条制作流水线、100+ 工具、700+ agent 技能与制作知识文件，用户用自然语言描述需求，由 AI 编码助手（Claude Code/Cursor/Copilot/Windsurf/Codex）完成调研、脚本、素材生成、剪辑与合成。支持图片式视频与真实素材路径（从 Archive.org、NASA 等开放档案检索动态片段后剪辑渲染）。依赖 Python 3.10+、FFmpeg、Node.js 18+，通过 make setup 或手动 venv/npm 安装；所有 API key 可选，零 key 时用 Piper TTS 等免费工具。含 Backlot 本地看板用于实时展示制作进度与人工审批门。

- 12 条制作流水线、100+ 工具、700+ agent 技能与制作知识文件
- 从 YouTube/Shorts/TikTok/本地片段出发生成有依据的制作方案与成本预估
- Backlot 本地看板：分阶段展示进度、分镜审批门与可审计的 provider 决策日志
- 零 API key 路径：Piper TTS 旁白、开放档案素材、Remotion/HyperFrames 合成、FFmpeg 后期

> L34: Turn your AI coding assistant into a full video production studio. Describe what you want in plain language — your agent
> L93: Works with **Claude Code, Cursor, Copilot, Windsurf, Codex** — any AI coding assistant that can read files and run code.
> L167:  OpenMontage is pipeline-driven. Real work goes through `pipeline_defs/`, stage director skills in `skills/pipelines/`, 

## docling-project/docling（⭐69004，confidence: high）

**文档解析转换库：为生成式 AI 准备各格式文档**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

解析 PDF、Office 文档、HTML、音频、图像等多种格式，输出统一的 DoclingDocument 表示，可导出 Markdown、HTML、JSON 等；含版面/阅读顺序/表格结构理解、OCR、ASR、VLM 流水线。提供 Python API、CLI、docling-serve API 服务与 MCP server。本地可运行，适合敏感数据与离线环境。需 Python 3.10+，由 IBM 研究团队发起、LF AI & Data 基金会托管。

- 多格式解析：PDF、DOCX、PPTX、HTML、音频、图像等
- 高级 PDF 理解：版面、阅读顺序、表格结构、公式
- 与 LangChain、LlamaIndex、Crew AI、Haystack 的集成及 MCP server
- 支持本地执行，可用于气隙环境

> L27: Docling simplifies document processing by parsing diverse formats — including advanced PDF understanding — and providing
> L37: - 🤖 Plug-and-play [integrations][integrations] incl. LangChain, LlamaIndex, Crew AI & Haystack for agentic AI

## scikit-learn/scikit-learn（⭐67725，confidence: high）

**给 Python 用户提供构建于 SciPy 之上的机器学习模块**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=idea`

基于 SciPy 的 Python 机器学习模块，以 3-Clause BSD 许可分发。项目 2007 年由 David Cournapeau 在 Google Summer of Code 中发起，现由志愿者社区并获多个组织支持维护。要求 Python ≥3.12 及 NumPy、SciPy、Narwhals、joblib、threadpoolctl 等依赖；绘图功能需 Matplotlib。支持 pip 或 conda-forge 安装，可用 pytest 运行测试套件，通过 git clone 获取最新源码，并附开发指南与变更日志。

- 基于 SciPy 的 Python 机器学习模块，BSD 3-Clause 许可
- 支持 pip 与 conda-forge 两种安装途径
- 绘图能力（plot_ 函数与 *Display 类）依赖 Matplotlib
- 提供开发指南、测试套件与 SKLEARN_SEED 随机种子控制

> L48: **scikit-learn** is a Python module for machine learning built on top of
> L56: It is currently maintained by a community of contributors, with volunteers but also `support from several
> L61: Installation

## shanraisshan/claude-code-best-practice（⭐67665，confidence: high）

**Claude Code 最佳实践与工作流编目，面向使用 Claude Code 的开发者**

`ai_role=ai-knowledge · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

该仓库整理 Claude Code 的功能清单与使用实践：涵盖 Subagents、Commands、Skills、Hooks、MCP Servers、Memory、Checkpointing 等特性的位置与用法；收录 Command→Agent→Skill 的编排工作流示例；汇总 12 套社区开发工作流、跨模型协作（Plugin/MCP/Router 三种机制）、技能与子代理合集，以及 83 条来自 Boris Cherny、Thariq 等来源的提示与技巧。面向使用 Claude Code 的开发者与工程团队。内容以编目与链接为主，非可安装的软件工具。

- Claude Code 全特性清单（Subagents/Skills/Hooks/MCP/Memory 等）及文件位置
- Command → Agent → Skill 编排工作流实现
- 12 套社区工作流与跨模型协作机制（Plugin/MCP/Router）编目
- 83 条提示、规划、上下文与会话管理技巧

> L1: # claude-code-best-practice
> L20: ## 🧠 CONCEPTS
> L98: All major workflows converge on the same architectural pattern: **Research → Plan → Execute → Review → Ship**

## labmlai/annotated_deep_learning_paper_implementations（⭐67564，confidence: high）

**深度学习论文的 PyTorch 实现与旁注教程合集（60+）**

`ai_role=ai-knowledge · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

以 PyTorch 实现神经网络及相关算法的论文复现合集，配套讲解文档，官网以旁注格式并排呈现代码与笔记。覆盖 Transformer 各变体、LoRA、扩散模型（DDPM/DDIM/Stable Diffusion）、GAN 系列、强化学习（PPO/DQN）、图神经网络、优化器、归一化层、蒸馏与采样技术等。仓库持续维护、几乎每周新增实现；通过 pip 安装 labml-nn 包使用。面向学习与理解算法的读者。

- 60+ 篇深度学习论文的 PyTorch 实现并配讲解笔记
- 覆盖 Transformer 变体、LoRA、扩散模型、GAN、RL、GNN、优化器等类别
- 官网以旁注格式并排渲染代码与说明
- pip 安装 labml-nn 即可使用

> L5: This is a collection of simple PyTorch implementations of
> L10: renders these as side-by-side formatted notes.
> L146: ### Installation

## mem0ai/mem0（⭐67348，confidence: high）

**为 AI 智能体和应用提供可持久化记忆层的基础设施**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=research`

Mem0 为 AI 助手和智能体添加记忆层：记录用户偏好与状态，随交互持续学习。提供三种形态——pip/npm 安装的库（测试原型用）、docker compose 启动的自托管服务器（含 Dashboard 与鉴权）、云平台（托管服务）。记忆提取采用单遍 ADD-only 机制，检索融合语义、BM25 关键词与实体匹配，并含时间感知检索。需外部 LLM 运行（默认 OpenAI gpt-5-mini），嵌入默认 text-embedding-3-small。提供 CLI 管理记忆，Apache 2.0 协议。

- 多层级记忆：User/Session/Agent 状态保留与个性化
- 多信号检索：语义、BM25 关键词、实体匹配并行融合，含时间感知排序
- 提供 Python/JavaScript SDK、CLI 及支持 skills 标准的编码助手技能包
- 库 / Docker 自托管 / 云平台三种部署形态

> L70: Mem0 ("mem-zero") enhances AI assistants and agents with an intelligent memory layer, enabling personalized AI interacti
> L102: |**Setup**|`pip install mem0ai`|`docker compose up`|Sign up at app.mem0.ai|
> L186: Mem0 requires an LLM to function, with `gpt-5-mini` from OpenAI as the default. However, it supports a variety of LLMs; 

## Mintplex-Labs/anything-llm（⭐67247，confidence: high）

**本地优先的一体化 AI 应用：私聊文档、运行 AI Agent**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=local-ok · hardware=— · install_friction=medium · maturity=—`

一体化 AI 应用：接入本地或云端 LLM，导入 PDF/DOCX 等文档后即可对话，内置 agent、多用户权限、向量数据库与文档处理管道。支持 Docker 多用户部署与可嵌入聊天组件，桌面版覆盖 Mac/Windows/Linux，Android 客户端开源。自带本地 LLM 引擎（Lemonade/llama.cpp，支持 CUDA/Vulkan），遥测可关闭。

- 内置本地 LLM 引擎，CPU/GPU（CUDA/Vulkan）运行本地模型
- 支持 40+ LLM 提供商与 9 种向量数据库
- 无代码 AI Agent 构建器与 MCP 兼容
- 多用户实例与权限管理（Docker 版）

> L37: AnythingLLM is the all-in-one AI application that lets you build a private, fully-featured ChatGPT—without compromises. 
> L43: - Built-in local LLM engine - Run local models on your CPU or GPU (NVIDIA via CUDA, AMD and Intel via Vulkan) with no ex
> L52: - 👤 Multi-user instance support and permissioning _Docker version only_

## xtekky/gpt4free（⭐66885，confidence: high）

**给开发者的多提供方 LLM 聚合接入库，附 GUI 与 OpenAI 兼容 API**

`ai_role=ai-ecosystem · license_risk=viral · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=—`

社区项目，聚合多个可访问的提供方适配器，统一提供 Python 同步/异步客户端、浏览器 JS 客户端、本地 Web GUI，以及 FastAPI 实现的 OpenAI 兼容 REST API（Interference API）。支持图像/音频/视频媒体生成、本地推理后端接入，并内置 MCP 服务器（web_search/web_scrape/image_generation 三个工具，可接入 Claude Desktop）。部分提供方依赖 Chrome/Chromium 浏览器自动化或 cookies/HAR 凭据；Python 3.10+，提供 pip、Docker（full/slim）与 Windows exe 安装方式。

- Python/JS 客户端、本地 GUI 与 OpenAI 兼容 REST API 多形态接入
- 多提供方适配器，含媒体生成与本地推理后端
- 内置 MCP 服务器（stdio/HTTP 两种模式）暴露 web_search、web_scrape、image_generation
- 支持 x86_64 与 arm64 的 Docker full/slim 镜像

> L17: GPT4Free (g4f) is a community-driven project that aggregates multiple accessible providers and interfaces to make workin
> L27: - FastAPI-based OpenAI-compatible API (Interference API).
> L251: - GPT4Free integrates many providers including (but not limited to) OpenAI-compatible endpoints, PerplexityLabs, Gemini,

## ZhuLinsen/daily_stock_analysis（⭐66583，confidence: high）

**给个人投资者：LLM 每日自动分析自选股并推送决策仪表盘**

`ai_role=ai-enhanced · license_risk=permissive · deploy=— · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

基于大模型的多市场股票分析系统，覆盖 A股/港股/美股/日股/韩股/台股与 ETF。聚合 AkShare、Tushare 等行情源与多路新闻搜索，生成包含结论、评分、买卖点位、风险警报的 AI 决策报告，并推送到企业微信/飞书/Telegram/Discord/Slack/邮箱。部署方式包括 GitHub Actions 定时运行（零成本、无需服务器）、本地运行与 Docker；附带 Web 工作台与 Agent 策略问股（15 种内置策略）。README 声明仅供学习研究，不构成投资建议。

- 每日自动分析并推送决策仪表盘到 6 类通知渠道
- GitHub Actions 定时运行，零成本无需服务器
- Agent 策略问股：多轮追问，15 种内置策略
- 多源行情（AkShare/Tushare/Baostock/YFinance 等）默认零配置可运行

> L13: > 🤖 基于 AI 大模型的 A股/港股/美股/日股/韩股/台股自选股智能分析系统，每日自动分析并推送「决策仪表盘」到企业微信/飞书/Telegram/Discord/Slack/邮箱
> L48: |AI 模型|Modelflare、AIHubMix、Gemini、OpenAI 兼容、DeepSeek、通义千问、Claude、Ollama 本地模型等|

## heygen-com/hyperframes（⭐65757，confidence: high）

**给开发者和 AI 编码代理：把 HTML/CSS/动画渲染为确定性 MP4 视频**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=—`

一个将 HTML、CSS、媒体与可寻址动画转为确定性 MP4 视频的开源框架，支持三种使用方式：本地 CLI、面向 AI 编码代理的 skills（21 个，含路由器与按需加载的领域技能）、以及作为托管创作流程的渲染核心。代理工作流覆盖产品介绍视频、PR 讲解、字幕嵌入、动效图形、幻灯片等 9 类创作流程；运行时适配 GSAP、Lottie、Three.js、Anime.js、CSS、WAAPI。要求 Node.js 22+ 与 FFmpeg。

- 把定义为 HTML 的视频按 data-* 时间属性渲染为确定性 MP4
- 提供 21 个 agent skills，含 `/hyperframes` 意图路由与按需加载的领域技能
- 支持 Claude Code、Codex、Cursor、Gemini CLI 等支持 skills 的编码代理
- 支持 GSAP/CSS/Lottie/Three.js/Anime.js/WAAPI 等可寻址动画运行时

> L21: HyperFrames is an open-source framework for turning HTML, CSS, media, and seekable animations into deterministic MP4 vid
> L44: > The picker opens with nothing pre-selected — the **Core Skills** group is all you need: the `/hyperframes` router inst
> L52: The skills teach agents the HyperFrames production loop: plan the video, write valid HTML, wire seekable animations, add

## keras-team/keras（⭐64377，confidence: high）

**给深度学习开发者用的多后端神经网络框架**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=local-ok · hardware=cpu-ok · install_friction=medium · maturity=—`

Keras 3 是多后端深度学习框架，可在 JAX、TensorFlow、PyTorch 之上运行，另提供仅推理的 OpenVINO 后端；通过环境变量 KERAS_BACKEND 或配置文件切换后端，导入后不可更改。覆盖计算机视觉、自然语言处理、音频、时序、推荐等任务，可作为 tf.keras 的替代（drop-in replacement），Keras 模型可用 tf.data.Dataset 或 PyTorch DataLoader 数据集训练。Linux/macOS 直接安装，Windows 建议 WSL2。

- 多后端支持：JAX、TensorFlow、PyTorch、OpenVINO（仅推理）
- 通过 KERAS_BACKEND 环境变量或 ~/.keras/keras.json 配置后端
- 作为 tf.keras 的 drop-in replacement，支持迁移现有代码
- 提供各后端 CUDA 依赖的 requirements 文件

> L3: Keras 3 is a multi-backend deep learning framework, with support for JAX, TensorFlow, PyTorch, and OpenVINO (for inferen
> L84: You can export the environment variable `KERAS_BACKEND` or you can edit your local config file at `~/.keras/keras.json`

## jingyaogong/minimind（⭐63891，confidence: high）

**从零训练 64M 超小语言模型的开源教程项目**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=local-ok · hardware=— · install_friction=medium · maturity=—`

从 0 开始完整复现小语言模型训练的开源项目：核心算法用 PyTorch 原生实现，不依赖第三方高层封装，覆盖 MoE、数据清洗、预训练、SFT、LoRA、DPO、PPO/GRPO/CISPO、Tool Use、Agentic RL、自适应思考与模型蒸馏全流程。提供全阶段开源数据集、Streamlit 聊天 WebUI、兼容 OpenAI API 协议的服务端，模型结构对齐 Qwen3 生态，可被 transformers/llama.cpp/vllm/ollama 等框架加载。适合想亲手理解 LLM 训练链路的个人，单张 NVIDIA 3090 上 SFT 1 epoch 实测约 2 小时。

- 全训练链路代码从 0 用 PyTorch 原生实现，不依赖第三方框架封装
- 覆盖 Pretrain/SFT/LoRA/DPO/PPO/GRPO/CISPO/Tool Use/Agentic RL/蒸馏全流程
- 开源全阶段数据集，主线模型结构对齐 Qwen3/Qwen3-MoE 生态
- 兼容 transformers、llama.cpp、vllm、ollama 及 OpenAI API 协议服务端

> L16: * 此开源项目旨在完全从 0 开始，仅用 3 块钱成本与 2 小时训练时间，即可训练出规模约为 64M 的超小语言模型 MiniMind。
> L18: * 项目同时开源了大模型的极简结构与完整训练链路，覆盖 MoE、数据清洗、预训练（Pretrain）、监督微调（SFT）、LoRA、RLHF（DPO）、RLAIF（PPO / GRPO / CISPO）、Tool Use、Agentic R
> L20: * 项目所有核心算法代码均从 0 使用 PyTorch 原生实现，不依赖第三方库提供的高层抽象接口。

## upstash/context7（⭐63194，confidence: high）

**为 AI 编码代理提供最新版本库文档的检索平台**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

Context7 是 Upstash 维护的文档检索平台，向编码代理注入最新的、特定版本的库文档与代码示例，缓解模型训练数据过时导致的问题。提供两种模式：CLI + Skills（通过 ctx7 命令抓取文档，无需 MCP）与注册 MCP 服务器让代理原生调用文档工具。一条命令完成安装与 OAuth 认证，可用 --cursor/--claude/--opencode 定向配置；支持库 ID 精确匹配与版本指定。注意：API 后端与爬虫引擎为闭源，不在本仓库。

- CLI + Skills 与 MCP 两种接入模式，一条命令完成设置
- 按库 ID 与版本精确检索文档（/mongodb/docs、/vercel/next.js 等）
- MCP 客户端手动配置支持 30+ 客户端
- 提供 MCP server、CLI、TypeScript SDK、Vercel AI SDK 工具等多个包

> L21: Context7 pulls up-to-date, version-specific documentation and code examples straight from the source — and gives them to
> L41: - **CLI + Skills** — installs a skill that guides your agent to fetch docs using `ctx7` CLI commands (no MCP required)
> L42: - **MCP** — registers a Context7 MCP server so your agent can call documentation tools natively

## hugohe3/ppt-master（⭐63103，confidence: mid）

**给 AI agent 用户的工具：从文档或主题生成本地可编辑的原生 PPT**

`ai_role=ai-native · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=—`

一个以 skill/工作流形式交付的开源项目：用户在具备 agent 能力的 AI 工具（IDE 插件、CLI 等）中给出文档或主题，工作流在本地运行并导出可编辑的 .pptx，包含原生形状与连接符、带数据的图表与表格、切换与动画、基于演讲者备注的旁白音频，并支持自有 .pptx 模板。需自行安装 Python 3.10+ 并依赖依赖文件安装包；文档另说明旧格式需可选 Pandoc。模型质量由所用 LLM 决定，推荐大上下文窗口模型并搭配 AI 图像生成。

- 生成本地可编辑 .pptx：原生形状、母版/版式继承、带数据图表与表格
- 支持从参考中提炼品牌/风格/版式模板，填充既有 .pptx 并保留设计
- 为成品幻灯片添加原生切换、动画与旁白音频
- 流程在本地机器运行，除模型通信外数据不离开本机

> L69: In form, it's a workflow (a "skill") that runs inside any agent-capable AI tool: tell it in chat — "make a deck from thi
> L77: - **No platform lock-in** — any agent-capable AI IDE can drive it; Claude, GPT, Gemini, Kimi, and other models all work
> L83: > `harness + model = agent` — PPT Master only owns the workflow; the model sets the ceiling. Recommended: **Kimi K3 (or 

## sansan0/TrendRadar（⭐62980，confidence: high）

**面向个人用户的多平台热点聚合监控与 AI 舆情筛选推送工具**

`ai_role=ai-enhanced · license_risk=viral · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

聚合多平台热榜与 RSS 订阅，按关键词或自然语言兴趣描述筛选新闻，通过微信、飞书、钉钉、Telegram、邮件、ntfy、bark、slack 等渠道推送。AI 功能包括智能筛选（自动提取标签并对新闻打分，失败时回退关键词匹配）、标题翻译、分析简报（趋势概述、情感倾向等），底层经 LiteLLM 统一接入 100+ 模型提供商。支持 Docker、GitHub Actions、本地部署与 Cloudflare Pages，数据本地/云端自持；另提供 MCP Server，支持自然语言对话式查询与分析。

- AI 智能筛选：自然语言兴趣描述自动打分，失败回退关键词匹配
- 通过 LiteLLM 接入 DeepSeek、OpenAI、Gemini、Anthropic 等 100+ 提供商
- MCP Server 提供 21 个工具与 4 个资源，支持对话式分析与文章正文读取
- 9 个推送渠道，含通用 Webhook 适配 Discord/IFTTT 等平台

> L339: - **统一 AI 接口**：使用 LiteLLM 替代手动实现，支持 100+ AI 提供商
> L269: - **AI 智能筛选系统**：不用再手动设关键词！在 `ai_interests.txt` 里用日常语言写下你关注的方向（如"我想看 AI 和新能源相关新闻"），AI 会自动提取标签并对每条新闻打分，只推送真正和你相关的内容。万一 AI 

## ultralytics/ultralytics（⭐62594，confidence: mid）

**YOLO 系列视觉模型库：检测/分割/分类/姿态/跟踪一体化**

`ai_role=ai-ecosystem · license_risk=dual · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

Ultralytics 维护的 YOLO 模型库，覆盖目标检测、实例分割、语义分割、深度估计、图像分类、姿态估计、旋转框检测与多帧目标跟踪任务。通过 pip 安装后提供 CLI（yolo 命令）与 Python API 两种调用方式，预训练权重在首次使用时自动从官方 release 下载。模型在 COCO、Cityscapes、ImageNet、DOTAv1、NYU Depth V2 等数据集上预训练，README 附带各系列模型的精度与速度指标表。商业使用需向官方申请 Enterprise License。

- 支持检测、分割、深度估计、分类、姿态、OBB、跟踪七类视觉任务
- CLI（yolo 命令）与 Python API 两种调用方式
- 预训练权重首次使用时自动下载，含 COCO/Cityscapes/ImageNet/DOTA/NYU 等预训练版本
- 提供 YOLO27 预告（尚未发布，无发布日期）

> L19: Ultralytics creates cutting-edge, state-of-the-art (SOTA) YOLO models built on years of foundational research in compute
> L43: ## 📄 Documentation
> L91: Ultralytics supports a wide range of YOLO models, from early versions like YOLOv3 to the latest YOLO26. The tables below

## microsoft/autogen（⭐61449，confidence: mid）

**微软多智能体 AI 应用框架：构建可自主运行或与人协作的 agent 应用**

`ai_role=ai-native · license_risk=viral · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

面向创建多智能体 AI 应用的 Python/.NET 框架，采用分层可扩展设计：Core API 提供消息传递、事件驱动 agent 与本地/分布式运行时，AgentChat 提供快速原型的高层 API，Extensions 提供模型客户端与代码执行等能力；配套 AutoGen Studio 无代码 GUI 与 AutoGen Bench 基准套件。注意：项目已被微软归档，不再提供 bug 修复、安全修复与新特性，新用户被引导至 Microsoft Agent Framework。

- 分层框架：Core / AgentChat / Extensions 三层 API
- AutoGen Studio 无代码 GUI 构建多 agent 工作流
- 支持 MCP Server 接入与 AgentTool 多 agent 编排
- Core API 支持 .NET 与 Python 跨语言

> L11: **AutoGen** is a framework for creating multi-agent AI applications that can act autonomously or work alongside humans.
> L108: The autogen _framework_ uses a layered and extensible design. Layers have clearly divided responsibilities and build on 
> L14: > **⚠️ Project archived and no longer maintained**

## BerriAI/litellm（⭐61439，confidence: high）

**统一的 LLM 网关：一份接口调用 100+ 模型供应商**

`ai_role=ai-ecosystem · license_risk=none · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

提供 Python SDK 与可自部署的 AI Gateway（Proxy Server）两种使用方式，用 OpenAI 格式统一调用 100+ LLM 供应商。支持 /chat/completions、/responses、/embeddings、/images、/audio、/batches、/rerank、/messages 等端点，以及 A2A 代理调用、MCP 服务器接入。网关侧提供虚拟密钥、花费跟踪、guardrails、负载均衡与管理后台；SDK 侧提供带重试/回退的 Router 与可观测性回调。核心为 Rust 实现，附 Python SDK。

- Python SDK 与 AI Gateway（Proxy Server）两种形态，OpenAI 格式调用 100+ 供应商
- A2A Agent 网关与 MCP 网关：将 MCP 服务器接入 /chat/completions
- 虚拟密钥、多租户花费跟踪、guardrails、负载均衡与管理后台
- Router 支持跨部署的重试/回退与应用级负载均衡

> L40: LiteLLM is an open source AI Gateway that gives you a single, unified interface to call 100+ LLM providers — OpenAI, Ant
> L42: Use it as a **Python SDK** for direct library integration, or deploy the **AI Gateway (Proxy Server)** as a centralized 
> L53: - **Production-ready gateway** — virtual keys, spend tracking, guardrails, load balancing, and an admin dashboard out of

## CorentinJ/Real-Time-Voice-Cloning（⭐60189，confidence: high）

**5 秒音频克隆声音、实时生成任意语音的工具箱**

`ai_role=ai-native · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=medium · maturity=research`

基于 SV2TTS 三阶段深度学习框架的声音克隆实现：从几秒音频提取声纹的数字表示，再以该表示为参考，由任意文本合成语音，配套的 toolbox 可实时运行。作者硕士论文成果，实现了 SV2TTS、GE2E、Tacotron、WaveRNN 四篇论文。支持 Windows 与 Linux，依赖 ffmpeg 读音频，用 uv 管理 Python 环境，预训练模型自动下载，可选用 LibriSpeech 等数据集。README 提示项目已随深度学习进展显旧，推荐关注更新的开源替代。

- SV2TTS 三阶段框架：声纹表示→文本合成，vocoder 实时运行
- 实现 4 篇论文（SV2TTS/GE2E/Tacotron/WaveRNN）
- 预训练模型自动下载，也可从 Hugging Face 手动获取
- uv 自动创建虚拟环境，支持 NVIDIA GPU 与 CPU 两种运行方式

> L3: This repository is an implementation of [Transfer Learning from Speaker Verification to
> L6: SV2TTS is a deep learning framework in three stages. In the first stage, one creates a digital representation of a voice
> L30: Both Windows and Linux are supported.

## crewAIInc/crewAI（⭐59797，confidence: mid）

**面向开发者的多 Agent 协作编排 Python 框架**

`ai_role=ai-native · license_risk=dual · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

开源 Python 框架，通过 Crews（基于角色的自主协作 Agent 团队）与 Flows（事件驱动、精细控制的确定性工作流）两种抽象构建多 Agent 自动化。提供 CLI（crewai create/install/run）以 JSON-first 项目结构脚手架化项目，支持工具、记忆、知识、结构化输出、checkpointing 与 MCP/A2A；要求 Python >=3.10 且 <3.14，依赖 uv 管理。另有面向企业的 AMP Suite 商业控制面提供托管部署、可观测性与支持。

- Crews（自主协作）与 Flows（事件驱动控制）双模型组合
- CLI 一键创建项目并按 JSON 定义运行（crewai create/run）
- 支持工具、记忆、知识、结构化输出、checkpointing 与 MCP/A2A
- 提供 Claude Code/Cursor 等 AI 编码 agent 的官方 skills 安装

> L49: > CrewAI is an open-source Python framework with high-level abstractions and low-level APIs for building production-read
> L52: - **CrewAI Crews**: Optimize for autonomy and collaborative intelligence with role-based AI agents.
> L53: - **CrewAI Flows**: Build event-driven automations that combine precise workflow control, single LLM calls, and native s

## MemPalace/mempalace（⭐59609，confidence: high）

**给 AI 编码代理提供本地化、可溯源的会话记忆存储与语义检索**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

以逐字文本存储对话历史，不做摘要或改写，通过语义搜索检索；索引按 wing/room/drawer 层级结构化以支持范围化搜索。检索后端可插拔（默认 ChromaDB），支持 Milvus、Qdrant、pgvector、SQLite、Rust 原生引擎等六种。以 CLI 与 MCP 服务器形式提供，共 47 个 MCP 工具；含时间性知识图谱、多 agent 协作日志流，以及 Claude Code、Codex CLI、Cursor IDE 的自动保存 hooks。默认路径无需 API key 与云服务，数据默认留在本地。

- 逐字存储 + 语义检索，默认路径零 API 调用、零云端依赖
- 可插拔检索后端：ChromaDB 默认，另支持 Milvus/Qdrant/pgvector/SQLite/Rust 原生
- 47 个 MCP 工具与结构化 wing/room/drawer 索引
- LongMemEval 基准 96.6% R@5（原始语义检索，无 LLM）可复现

> L5: Local-first AI memory. Verbatim storage, pluggable backend, 96.6% R@5 raw on LongMemEval — zero API calls.
> L22: MemPalace stores your conversation history as verbatim text and retrieves
> L264: 47 MCP tools cover palace reads/writes, knowledge-graph operations,

## meilisearch/meilisearch（⭐59591，confidence: high）

**为网站与应用提供 AI 混合搜索的搜索引擎 API**

`ai_role=ai-enhanced · license_risk=dual · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=—`

开源搜索引擎，提供 RESTful API 与多语言 SDK，供应用与网站集成搜索功能。核心机制包括语义与全文结合的混合搜索、输入即搜（50 毫秒内返回）、容错、过滤与分面、地理搜索、多语言支持（含中文/日文优化）与多租户。支持自然语言对话式搜索并生成基于检索结果的 AI 回答，可与 LangChain 及 MCP 配合。分社区版（MIT）与企业版（商业许可/BSL 1.1，生产环境需商业协议），官方提供 Cloud 托管服务，并默认收集可关闭的匿名遥测数据。

- 混合搜索：语义搜索与全文搜索结合
- 对话式搜索：基于检索结果生成 AI 回答
- 支持地理搜索、分面过滤、同义词与多租户
- 开箱支持 LangChain 与 Model Context Protocol

> L45: - **Hybrid search:** Combine the best of both semantic & full-text search to get the most relevant results
> L57: - **Conversational search:** let users ask questions in natural language and get AI-generated answers grounded in your s
> L62: - **AI-ready:** works out of the box with LangChain and the Model Context Protocol (MCP)

## pathwaycom/serviette（⭐58792，confidence: high）

**面向企业和开发者的零代码文档问答 RAG 服务器，答案随文档实时更新**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=locked-api · hardware=— · install_friction=medium · maturity=—`

基于 Pathway Live Data Framework 的 RAG 服务器：指向一个文档目录，在单个 YAML 文件中选择向量数据库与 embedder，运行两条命令即获得带来源引用的聊天界面与 REST API。索引器与服务器为独立进程，仅通过向量数据库耦合；文档的增、改、删在数秒内反映到答案，无需重新上传或重建索引。默认使用内嵌 DuckDB 零配置启动，支持本地免费 embedder。运行需要免费的 Pathway license key；目前一次只回答一个问题，未内置对话记忆、用户账号与托管服务。

- 8 种向量数据库后端，通过 Pathway 原生连接器写入 upsert/delete
- 文档编辑、新增、删除数秒内同步到答案（实时增量索引）
- 多源接入：本地文件、Google Drive、S3/MinIO、SharePoint、FTP/SFTP/WebDAV/ZIP
- 文本、Office、PDF、扫描图片开箱即用，可配置音频与视频解析

> L12: **A no-code, always up-to-date RAG server for any vector database — built on
> L65: **How mature it is.** serviette is a thin layer over the
> L126: - **Live & incremental.** Built on Pathway: additions, edits and deletions

## ultralytics/yolov5（⭐58179，confidence: mid）

**基于 PyTorch 的目标检测/实例分割/分类模型及训练导出工具**

`ai_role=ai-ecosystem · license_risk=dual · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

Ultralytics 发布的 YOLOv5 视觉模型仓库：基于 PyTorch 框架，覆盖目标检测、实例分割与图像分类任务。提供 detect.py 推理脚本、PyTorch Hub 加载、train.py 训练（COCO 复现，n/s/m/l/x 五档模型），并支持导出 TFLite、ONNX、CoreML、TensorRT 等部署格式。安装需 Python>=3.8 与 PyTorch>=1.8，通过克隆仓库安装依赖；预训练权重从 release 自动下载。README 另提示最新任务（姿态估计、OBB）可使用 ultralytics 统一包。

- 目标检测、实例分割、图像分类三类任务的训练与推理
- 导出 TFLite/ONNX/CoreML/TensorRT 部署格式
- n/s/m/l/x 五档 COCO 预训练权重自动下载
- 多 GPU DDP 训练、TTA、模型剪枝与超参数演化教程

> L14: Ultralytics YOLOv5 🚀 is a fast, accurate, and easy-to-use computer vision model developed by Ultralytics. Based on the P
> L52: Clone the repository and install dependencies in a **Python>=3.8.0** environment. Ensure you have **PyTorch>=1.8** insta
> L85: The commands below demonstrate how to reproduce YOLOv5 COCO dataset results. Both models and datasets are downloaded aut

## jamiepine/voicebox（⭐57827，confidence: high）

**本地优先的 AI 语音工作室：克隆声音、生成语音、全局听写**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

本地优先的开源语音应用，整合语音输入与输出两个环节：从几秒参考音频做零样本克隆，支持 8 个 TTS 引擎与 23 种语言生成语音，通过全局热键做听写并以 Whisper 转写，还可经内置 MCP 服务器让 MCP 感知的 agent 以克隆声音发声。附带后期音效处理、多轨 Stories 编辑器、生成版本管理与 REST API。模型与音频数据全程留在本机。基于 Tauri (Rust) 构建，macOS/Windows 提供安装包，Linux 需从源码构建。

- 8 个可切换的 TTS 引擎（Qwen3-TTS、Chatterbox、Kokoro 等）与 23 种语言
- 零样本声音克隆与 50+ 预置声音
- 全局热键听写 + Whisper 语音转写，支持 LLM 清理口头语
- 内置 MCP 服务器与 REST API，agent 可通过 voicebox_speak 发声

> L61: Voicebox is a **local-first AI voice studio** — a free and open-source alternative to **ElevenLabs** and **WisprFlow** i
> L74: - **Agent voice output** — one tool call (`voicebox_speak`) and any MCP-aware agent (Claude Code, Cursor, Cline) speaks 
> L78: - **Runs everywhere** — macOS (MLX/Metal), Windows (CUDA), Linux, AMD ROCm, Intel Arc, Docker

## blader/humanizer（⭐57767，confidence: high）

**面向 agent 用户的 AI 痕迹改写技能：按 Wikipedia 标准去除 AI 写作特征**

`ai_role=ai-enhanced · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

以 skill 形式运行的文本改写工具：基于 Wikipedia「Signs of AI writing」归纳的 26 种 AI 写作模式（分六类，含弱特征需共现才判定），逐条标注后重写，输出初稿、对残留人工痕迹的批评与终稿。可通过写作样本做声音匹配，改写文件时只改散文内容，保留代码、数据、frontmatter 与链接。要求事实细节必须来自原文或作者，缺失时询问而非编造。支持 Claude Code 插件、Codex、Claude.ai/Desktop 及 Skills CLI 覆盖的其他 agent。明确不以免过 AI 检测器为目标。

- 基于 Wikipedia「Signs of AI writing」的 26 种 AI 写作模式检测与改写
- 提供写作样本可做声音匹配（节奏、用词、标点）
- 改写文件时仅改散文，保留代码、数据、frontmatter、链接
- 事实细节不编造，缺失时向作者询问

> L7: Humanizer makes AI-written text sound like a person wrote it, without changing what it says. It is built on Wikipedia's 
> L29: Humanizer checks for 26 patterns in all.
> L104: Humanizer marks every tell it finds, strongest first. It drafts a rewrite without treating the original structure as fix

## zylon-ai/private-gpt（⭐57591，confidence: high）

**把本地模型变成私有 AI 应用的开源 API 层**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=local-ok · hardware=— · install_friction=low · maturity=idea`

以 Claude API 为参照模型的 API 层，为本地模型提供消息、文件摄取、带引用的检索与 agentic RAG、内置工具、MCP、数据库/CSV 访问、嵌入与编排等后端原语。自身不运行模型，通过 OPENAI_API_BASE 连接任意 OpenAI 兼容推理服务器。附内置演示 UI，API 为核心产品。2023 年以离线文档问答脚本起步，后重构为 1.0 API 层，由 Zylon 团队维护。

- 兼容 Claude API 的消息流式、文件摄取、引用检索与工具调用
- 内置 web search/fetch、代码执行工具与 MCP 连接器
- 连接任意 OpenAI 兼容推理服务器（Ollama、llama.cpp、vLLM 等）
- 提供 brew/uv 安装与内置演示 UI

> L3: **PrivateGPT is the open-source API layer that turns local models into production AI applications.**
> L12: Running a model locally is only the first step. To build useful AI applications you need a set of higher-level building 
> L24: > PrivateGPT does **not** run models itself. It connects to any OpenAI-compatible inference server via `OPENAI_API_BASE`

## deepfakes/faceswap（⭐57573，confidence: high）

**给研究/创作者用深度学习换脸图片与视频的工具**

`ai_role=ai-native · license_risk=viral · deploy=— · model_dep=— · hardware=— · install_friction=medium · maturity=—`

FaceSwap 是一个用深度学习识别并替换图片和视频中人脸的 Python 程序，工作流分为提取人脸、训练模型、应用转换三步，均通过 faceswap.py 命令行调用，另提供 GUI 入口和基于 ffmpeg 的视频转换工具。可运行于 Windows、Linux 和 macOS，README 建议使用支持 CUDA 的现代 GPU 以获得更好性能，AMD GPU 在 Linux 上可经 ROCm 支持。项目明确列出伦理约束，禁止用于未经同意或不当内容的制作，支持主要通过 Discord 和论坛提供。

- extract/train/convert 三段式换脸工作流与 GUI 入口
- 支持 Windows/Linux/macOS 多平台
- AMD GPU 可通过 ROCm 支持（Linux）
- 附视频格式转换工具（effmpeg/ffmpeg）

> L6:  FaceSwap is a tool that utilizes deep learning to recognize and swap faces in pictures and videos.
> L45: FaceSwap is a Python program that will run on multiple Operating Systems including Windows, Linux, and MacOS.
> L47: See INSTALL.md for full installation instructions. You will need a modern GPU with CUDA support for best performance. Ma

## ageitgey/face_recognition（⭐56831，confidence: high）

**给 Python/命令行用户提供的简单人脸识别库**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=—`

基于 dlib 深度学习模型构建的 Python 库与命令行工具：支持从图片中定位人脸、提取眼睛/鼻子/嘴等面部特征点、生成人脸编码并比对识别人物，提供 face_recognition 与 face_detection 两个 CLI 命令，支持 --tolerance 阈值与 --cpus 多核并行。模型在 LFW 基准上自报准确率 99.38%。要求 Python 3.3+/2.7 与 macOS/Linux（Windows 非官方支持），依赖预装 dlib 与 cmake，亦可经 Docker 运行。

- 提供 Python API 与 face_recognition/face_detection 命令行工具
- 人脸定位、特征点提取、编码与比对三类功能
- 支持 --cpus 多核并行与 --tolerance 匹配阈值调节
- 提供 CNN 模型选项（model="cnn"）的检测示例

> L8: Built using dlib's state-of-the-art face recognition
> L63: ## Installation
> L82: Finally, install this module from pypi using `pip3` (or `pip2` for Python 2):

## hesreallyhim/awesome-claude-code（⭐55886，confidence: mid）

**面向 Claude Code 用户的精选资源清单**

`ai_role=ai-ecosystem · license_risk=none · deploy=library · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

以 awesome list 形式收录 Claude Code 相关资源的仓库：分类组织入门指南、Anthropic 官方文档与工具、技能（skills）、插件、hooks、状态栏与开发工具等条目，每条附维护者、创建时间、最近提交、许可证与 star 数等元信息。本次迭代优先收录上一版未包含的新资源，旧资源暂存于 README_ALTERNATIVES 目录并将陆续迁回。附带 Claude Code Ticker 展示 GitHub 上的相关项目。声明与 Anthropic 无隶属关系。

- 分类收录 Claude Code 指南、官方资源、技能、插件等条目
- 收录 Anthropic 官方仓库（Agent Skills、GitHub Action、Best Practices 等）
- 条目附 created/last-commit/license/stars 元信息
- 旧版资源保留于 README_ALTERNATIVES 目录

> L5: _A hand-picked collection of the finest of resources for the most awesome of agents, Claude Code, the undisputed champio
> L49: - Agent Skills by Anthropic - Anthropic's official repository for Agent Skills — the SKILL.md format, a skill template, 

## aaif-goose/goose（⭐55361，confidence: high）

**本地运行的通用开源 AI agent：桌面应用、CLI 与 API 三形态**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

goose 是运行在用户本机的通用 AI agent，用途不限于代码，也覆盖研究、写作、自动化与数据分析。提供 macOS/Linux/Windows 桌面应用、完整 CLI 与嵌入用 API，以 Rust 构建并开源（Apache-2.0）。接入 15+ 模型提供商，支持 API key 或经 ACP 使用已有的 Claude/ChatGPT/Gemini 订阅；通过 MCP 开放标准连接 70+ 扩展，并支持自定义发行版（预配置 provider、扩展与品牌）。项目隶属 Linux Foundation 下的 Agentic AI Foundation。

- 桌面应用、CLI、API 三种交付形态，Rust 构建
- 支持 15+ 模型提供商，可经 ACP 复用已有订阅
- 通过 MCP 标准连接 70+ 扩展
- 支持构建自定义发行版（Custom Distributions）

> L16: goose is a general-purpose AI agent that runs on your machine. Not just for code — use it for research, writing, automat
> L20: goose works with 15+ providers — Anthropic, OpenAI, Google, Ollama, OpenRouter, Azure, Bedrock, and more. Use API keys o
> L18: A native desktop app for macOS, Linux, and Windows. A full CLI for terminal workflows. An API to embed it anywhere. Buil

## microsoft/VibeVoice（⭐54857，confidence: high）

**语音 AI 模型家族：长音频识别与多说话人语音生成**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=local-ok · hardware=cpu-ok · install_friction=low · maturity=—`

微软开源的语音 AI 模型家族，含 TTS 与 ASR 两条线：ASR 模型单次处理 60 分钟长音频，联合输出说话人、时间戳与文本，支持自定义热词、流式识别与 50+ 语言；TTS 支持最长 90 分钟、最多 4 说话人的语音生成，另有 0.5B 实时流式 TTS（约 300 毫秒首响）。核心机制为 7.5 Hz 连续语音 tokenizer 与 next-token diffusion 框架。注意：TTS 代码已于 2025-09 从仓库移除，模型仅限研究用途。

- ASR 单次处理 60 分钟音频，联合输出说话人/时间戳/内容
- TTS 单次生成最长 90 分钟、最多 4 说话人的对话语音
- 0.5B 实时流式 TTS，支持流式文本输入
- ASR-BitNet 经量化压缩至 1.58 GB，可在 CPU 上实时推理

> L40: VibeVoice is a **family of open-source frontier voice AI models** that includes both Text-to-Speech (TTS) and Automatic 
> L34: 2025-09-05: VibeVoice is an open-source research framework intended to advance collaboration in the speech synthesis com
> L140: We do not recommend using VibeVoice in commercial or real-world applications without further testing and development. Th

## bojieli/ai-agent-book（⭐54675，confidence: high）

**面向工程师的 AI Agent 开源书：10 章正文加 109 个配套实验**

`ai_role=ai-knowledge · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=—`

开源图书仓库，正文按 Agent = LLM + 上下文 + 工具的框架分 10 章，主题覆盖上下文工程、用户记忆与 RAG、MCP 工具、Coding Agent、评估、后训练与多 Agent 协作。提供 15 种语言的 PDF/EPUB 下载与在线阅读，正文源码为 markdown，可自行编译（需 pandoc/xelatex/ElegantBook）。实验代码统一支持 Python 3.11–3.13，用 uv 或 pip 按章节安装依赖，调用模型需自行配置 API Key；第 6/7/8/10 章部分实验需另行克隆 22 个外部仓库。

- 10 章正文与 109 个配套实验全部开源（Apache 2.0）
- 15 种语言的 PDF/EPUB 构建与在线阅读，main 分支推送后自动更新
- 实验环境用 uv.lock 固定，按章节 extra 安装依赖
- 配套代码由 coding agent 生成，附思考题参考答案与学习建议

> L10: **Agent = LLM + 上下文 + 工具**——本书围绕这个核心公式，用 10 章把 AI Agent 从原理讲到工程实战。全书正文、配图、**109 个配套实验**全部开源，欢迎亲手把实验跑一遍。
> L64: |1|🚀 **AI Agent 入门**|**Agent = LLM + 上下文 + 工具**；Harness 工程才是竞争力|读|4|
> L91: 运行会调用模型的实验前，请按该实验 README 配置凭据：支持根目录配置的实验可复制 `.env.example` 为 `.env` 并填入至少一个提供商 Key；有些实验要求在自身目录放 `.env` 或直接导出环境变量。只有在实验 R

## ggml-org/whisper.cpp（⭐54450，confidence: mid）

**在本地多平台离线运行 Whisper 语音识别的 C/C++ 推理实现**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=desktop · model_dep=local-ok · hardware=cpu-ok · install_friction=high · maturity=—`

OpenAI Whisper 语音识别模型的 C/C++ 移植，无依赖的纯 C/C++ 实现，基于 ggml 机器学习库构建。提供 C 风格 API、整数量化、VAD、混合精度推理，支持 Metal、Core ML、CUDA、Vulkan、OpenVINO 及 AMD NPU 等后端。模型需转换为 ggml 格式后由 whisper-cli 等示例程序运行，仅支持 16-bit WAV 输入，其他音频需用 ffmpeg 预先转换。支持 macOS/iOS/Android/Linux/Windows/WebAssembly 等平台，MIT 许可。

- 纯 C/C++ 无依赖实现，基于 ggml 库，提供 C 风格 API
- 多后端支持：Metal、Core ML、ANE、CUDA、Vulkan、OpenVINO、AMD NPU
- 整数量化降低模型内存与磁盘占用（tiny 75 MiB 至 large 2.9 GiB）
- 跨平台覆盖 iOS、Android、WebAssembly、树莓派、Docker 等

> L11: High-performance inference of OpenAI's Whisper automatic speech recognition (ASR) model:
> L13: - Plain C/C++ implementation without dependencies
> L26: Supported platforms:

## bmad-code-org/BMAD-METHOD（⭐54257，confidence: high）

**面向开发者的敏捷 AI 驱动开发工作流方法与技能集**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=idea`

一套以敏捷方式组织 AI 驱动开发（AiDD）的方法论，以 agent 技能与工作流形式安装到 AI 编码工具中：从澄清、规划到构建验证的交付闭环，把产品/架构决策显式化并作为上下文延续，按变更规模选择规划深度，覆盖新项目与既有代码库。稳定版 v6.12 经 npm 安装；V7 为预览 alpha，通过 skills CLI 安装，并提供 Claude Code 与 Codex 插件市场通道，运行需 uv 与 Python 脚本支持。

- 澄清→规划→构建验证的交付闭环，按变更规模调整规划深度
- 以 skills/工作流形式接入 AI 编码工具，提供 bmad-build/bmad-help 等技能入口
- 官方模块生态：Test Architect、Game Dev Studio、Loop 等 6 个模块
- v6.12 稳定版与 V7 预览双通道，支持 npx skills 安装与更新

> L7: **Agile Ai Driven Development — turn an idea or change request into working software without giving up the thinking.**
> L31: Expect breaking changes between updates. You need an AI coding tool that supports skills.

## lllyasviel/Fooocus（⭐53567，confidence: mid）

**面向普通用户的离线文生图软件：专注提示词即可出图**

`ai_role=ai-enhanced · license_risk=viral · deploy=desktop · model_dep=— · hardware=gpu-8g · install_friction=medium · maturity=—`

基于 Gradio 与 Stable Diffusion XL 架构的图像生成软件，离线、开源、免费。安装即用：从下载到生成首图点击少于 3 次，最低 4GB Nvidia 显存即可运行。内置离线 GPT-2 提示词处理引擎与采样优化，支持文生图、放大、变体、内绘/外绘、图像提示与 FaceSwap；提供 Windows 安装包、Colab、Anaconda/venv/系统 Python 及 AMD GPU（beta）多种运行途径。项目目前处于仅修复 bug 的 LTS 状态。

- 基于 SDXL 架构，内置离线 GPT-2 提示词处理引擎
- 最低 4GB Nvidia VRAM + 8GB RAM 即可运行
- 支持内绘/外绘、放大/变体、图像提示、FaceSwap
- 提供 Windows 一键包、Colab 与多种 Linux 安装途径

> L5: Fooocus is an image generating software (based on Gradio ).
> L7: Fooocus presents a rethinking of image generator designs. The software is offline, open source, and free, while at the s
> L13: The Fooocus project, built entirely on the **Stable Diffusion XL** architecture, is now in a state of limited long-term 

## anthropics/claude-cookbooks（⭐53514，confidence: high）

**面向开发者的 Claude 使用示例与指南手册**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

以 notebook/recipe 形式提供可复制的代码片段与指南，覆盖分类、RAG、摘要、工具调用、第三方集成、多模态、提示缓存、成本优化、JSON 输出、内容审核等主题。使用示例需要 Claude API key，代码以 Python 为主但说明可适配其他支持 Claude API 的语言。内容组织为 Capabilities、Tool Use、Third-Party Integrations、Multimodal、Advanced Techniques 等章节。

- 提供分类、RAG、摘要、工具调用等能力的示例 notebook
- 包含 Pinecone、Wikipedia、Voyage AI 等第三方集成示例
- 涵盖子 agent、提示缓存、成本优化、自动评估等进阶技术
- 提供 Claude API Fundamentals 课程作为入门路径

> L1: # Claude Cookbooks
> L3: The Claude Cookbooks provide code and guides designed to help developers build with Claude, offering copy-able code snip
> L7: To make the most of the examples in this cookbook, you'll need a Claude API key (sign up for free here).

## CherryHQ/cherry-studio（⭐52711，confidence: high）

**多模型桌面 AI 客户端：统一接入云/本地 LLM 与助手**

`ai_role=ai-ecosystem · license_risk=dual · deploy=— · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

支持多 LLM 提供商的桌面客户端，覆盖 Windows、Mac 和 Linux。核心功能包括：接入主流云服务（OpenAI、Gemini、Anthropic 等）与本地模型（Ollama、LM Studio）；300+ 预配置助手与自定义助手、多模型同时对话；支持文本/图片/Office/PDF 文档处理、WebDAV 备份、Mermaid 图表；集成搜索、翻译、MCP 服务器等工具。安装后即用，无需环境配置。另有企业版提供私有部署、统一模型管理与知识库（非完全开源）。社区版采用 AGPL-3.0 许可，商业豁免需联系官方。

- 支持 OpenAI、Gemini、Anthropic 等云服务与 Ollama、LM Studio 本地模型
- 300+ 预配置 AI 助手，支持多模型同时对话
- 支持 MCP（Model Context Protocol）服务器与小程序
- 跨平台桌面应用，开箱即用无需环境配置

> L25: Cherry Studio is a desktop client that supports multiple LLM providers, available on Windows, Mac and Linux.
> L39: - ☁️ Major LLM Cloud Services: OpenAI, Gemini, Anthropic, and more
> L41: - 💻 Local Model Support with Ollama, LM Studio

## dbeaver/dbeaver（⭐52092，confidence: high）

**给开发者和管理员的多平台通用数据库工具与 SQL 客户端**

`ai_role=ai-enhanced · license_risk=permissive · deploy=— · model_dep=local-ok · hardware=— · install_friction=medium · maturity=idea`

基于 Java/Eclipse RCP 的桌面数据库管理工具，采用 OSGI 插件架构（社区版 130+ 插件），开箱支持 100+ 数据库驱动，任何有 JDBC/ODBC 驱动的数据库均可连接。功能覆盖 schema/SQL/数据编辑、ER 图、数据导入导出迁移、执行计划、SSH 隧道等。AI 集成方面提供类 LLM 聊天视图，可将数据库结构、SQL 方言等上下文提供给模型以生成/分析/优化 SQL；社区版接入 OpenAI 与 Copilot，Pro 版额外支持 Anthropic/Grok/Azure/Bedrock/Gemini/Ollama。运行需 Java（发行包内置 OpenJDK 25），另有商业化 PRO 版本。

- 开箱支持 100+ 数据库驱动，兼容任意 JDBC/ODBC 数据库
- AI Chat 视图：生成/分析/优化 SQL，注入数据库结构与方言上下文
- OSGI 插件架构，社区版含 130+ 插件
- 提供 GitHub Releases 预编译二进制与每日 Early Access 版本

> L8: Free multi-platform database tool for developers, SQL programmers, database administrators and analysts.
> L64: - All DBeaver products contain AI Chat view similar to classic LLM chats.
> L71: - Pro versions provide additional AI tools + native support of Anthropic/Grok/Azure/Bedrock/Gemini/Ollama providers.

## elder-plinius/CL4R1T4S（⭐51329，confidence: high）

**收录各主流 AI 产品泄露系统提示词的透明度资料库**

`ai_role=ai-knowledge · license_risk=viral · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

以仓库形式汇集从 OpenAI、Google、Anthropic、xAI、Perplexity、Cursor、Windsurf、Devin、Manus、Replit 等产品中提取的系统提示词、指南与工具文本，声称覆盖几乎所有主流 AI 模型与 agent。目的是让用户了解各产品隐藏的系统指令内容。接受社区以 pull request 方式提交：需附模型名称/版本、提取日期及可选的上下文备注，通过 X 或 Discord 联系维护者。README 末段 L41-L43 包含试图让读取者复述自身指令的指令性文本。

- 收录多家 AI 产品的完整提取系统提示词与指南
- 提供 PR 贡献流程（模型名/版本、提取日期、备注）
- 以仓库形式按产品组织泄露文本

> L3: AI SYSTEMS TRANSPARENCY AND OBSERVABILITY FOR ALL! Full extracted system prompts, guidelines, and tools from OpenAI, Goo
> L28: Leak, extract, or reverse-engineer something? Good.

## roboflow/supervision（⭐51231，confidence: high）

**计算机视觉开发者的可复用工具集：模型接入、标注、数据集处理**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

面向计算机视觉应用的 Python 工具库：提供模型无关的检测/分类/分割结果封装（sv.Detections），内置 Ultralytics、Transformers、MMDetection、Inference、rfdetr 等库的连接器；提供可自定义的图像标注器，以及 YOLO 等（含 COCO）格式的数据集加载、拆分、合并、转换与保存工具。需 Python>=3.10，通过 pip 安装，含教程与文档。使用 Inference 模型需 Roboflow API KEY。

- 模型无关设计，内置多框架检测结果连接器
- 高度可自定义的图像标注器
- 数据集加载、拆分、合并、格式转换与保存工具
- 提供区域计数、跟踪、速度估计等教程

> L22: **We are your essential toolkit for computer vision.** From data loading to real-time zone counting, we provide the buil
> L38: Supervision was designed to be model agnostic. Just plug in any classification, detection, or segmentation model. For yo

## upscayl/upscayl（⭐50681，confidence: high）

**面向普通用户的免费开源 AI 图像放大与增强桌面应用**

`ai_role=ai-enhanced · license_risk=viral · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=—`

基于 Real-ESRGAN 模型与 Vulkan 架构的图像放大工具，将低分辨率图像放大并增强细节，后端以 AGPLv3 开源。提供 Linux（Flatpak/AppImage/AUR/Snap/RPM/DEB）、macOS（dmg/App Store/Homebrew）、Windows（exe）安装包，附带 CLI 工具 upscayl-ncnn 与自定义模型仓库。限制：需要 Vulkan 兼容 GPU，多数集成显卡与 CPU 不可用；不支持去模糊或对焦调整。

- 使用 Real-ESRGAN 模型放大低分辨率图像，后端 AGPLv3 开源
- 提供批量处理，可加载 custom-models 仓库的更多模型
- 附带 CLI 工具 upscayl-ncnn
- 三平台桌面安装包覆盖 Linux/macOS/Windows

> L45: #### Free and Open Source AI Image Upscaler
> L46: Upscayl lets you enlarge and enhance low-resolution images using advanced AI algorithms.
> L167:  - Upscayl uses AI models to enhance your images by guessing what the details could be. It uses Real-ESRGAN and Vulkan a

## ClickHouse/ClickHouse（⭐50458，confidence: high）

**面向开发者的实时分析型列式数据库管理系统**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

开源列式数据库管理系统，用于实时生成分析数据报告。通过官方脚本一行命令安装于 Linux、macOS 和 FreeBSD，并提供 ClickHouse Cloud 托管服务作为免安装使用方式。README 同时维护月度发布与社区电话会议、全球线下 meetup、培训与招聘信息，公司由该数据库的创建者与维护者运营。核心定位为 OLAP 场景下的分析查询，主题标签覆盖分布式、云原生、lakehouse 等部署形态。

- 列式存储的实时分析数据报告生成
- 一行 curl 脚本安装，支持 Linux/macOS/FreeBSD
- 提供托管服务 ClickHouse Cloud 免安装试用

> L6:  ClickHouse® is an open-source column-oriented database management system that allows generating analytical data reports
> L11: curl https://clickhouse.com/ | sh

## GokuMohandas/Made-With-ML（⭐49756，confidence: high）

**面向开发者的生产级 ML/MLOps 应用开发课程**

`ai_role=ai-knowledge · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

一个以课程形式组织的仓库，配套站点 madewithml.com 提供课程内容，代码覆盖从实验（设计+开发）到生产（部署+迭代）的完整流程：Jupyter notebook 交互式讲解后重构为带测试、文档、日志的 Python 脚本，使用 MLflow 做实验跟踪，通过 Ray 本地或 Anyscale 集群运行训练、调参、评估、推理与服务，并演示 CI/CD 工作流。读者为各方向开发者、应届毕业生与想建立技术基础的产品/管理层。可在个人笔记本运行，也可按 Anyscale 配置使用 GPU 集群。

- 从 notebook 交互式学习到软件工程化脚本（测试、日志、版本化）的完整工作流
- 支持本地笔记本与 Anyscale 集群两种运行环境，并可部署到 AWS/GCP/K8s
- 使用 MLflow 做实验跟踪与模型注册
- 通过 Ray 提供模型服务，可用 cURL/Python 调用

> L16: Learn how to combine machine learning with software engineering to design, develop, deploy and iterate on production-gra
> L27: In this course, we'll go from experimentation (design + development) to production (deployment + iteration). We'll do th
> L38: - **⚙️ MLOps**: connect MLOps components (tracking, testing, serving, orchestration, etc.) as we build an end-to-end mac

## MadsLorentzen/ai-job-search（⭐49696，confidence: mid）

**求职者本地运行的 AI 求职申请框架：评估职位、定制简历与面试准备**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

基于 Claude Code CLI 构建的求职申请工作流框架，以命令形式组织：/setup 建立个人档案，/scrape 抓取职位并按匹配度排序，/apply 运行 drafter-reviewer 流程生成 LaTeX 简历与求职信。支持 /interview 面试准备、/rank 批量评分、/outcome 记录进展、/notion-sync 与 /gmail-sync 集成等 13 个命令。核心流程与国家无关，职位门户搜索技能默认面向丹麦市场，可通过 /add-portal 替换为本地招聘网站。要求 Claude Pro/Max 订阅或 Anthropic API 额度，fork 后档案数据会写入受跟踪文件，README 建议使用私有仓库。

- /apply 的 drafter-reviewer 双 agent 流程：起草、评审、修订并强制 PDF 编译
- /add-portal 为任意招聘网站生成搜索技能，核心流程与国家/语言无关
- 13 个命令覆盖评估、投递、面试准备、结果跟踪与学习计划
- 职位描述按不可信输入处理，遵循指令级防护并提示人工复核

> L11: An AI-powered job application framework built on Claude Code. Fork it, fill in your profile, and let Claude evaluate job
> L34: A structured workflow that turns Claude Code into a full-stack job application assistant. The core workflow (self-profil
> L47: - Claude Code (CLI). Claude Code has no free tier: you need a Claude Pro/Max/Team subscription or Anthropic API credits 

## mudler/LocalAI（⭐49601，confidence: high）

**本地运行各类 AI 模型的开源引擎，无需 GPU**

`ai_role=ai-native · license_risk=permissive · deploy=desktop · model_dep=local-ok · hardware=cpu-ok · install_friction=low · maturity=—`

以小型核心加按需拉取后端镜像的架构运行 LLM、视觉、语音、图像、视频模型，每个后端封装 llama.cpp、vLLM、whisper.cpp 等引擎。提供 OpenAI/Anthropic/ElevenLabs 兼容 API、API key 认证与用户配额、内置带工具调用与 RAG 的 Agent、分布式模式与 WebUI。CPU 可运行，也支持 NVIDIA/AMD/Intel/Apple Silicon 加速；macOS 提供 DMG，其余通过容器镜像分发。

- OpenAI、Anthropic、ElevenLabs API 兼容的多模态统一接口
- 60+ 后端按需以 OCI 镜像安装，含自研 C++/GGML 引擎
- 内置自主 Agent（工具调用、RAG、MCP、skills）
- 分布式集群模式（PostgreSQL + NATS）与 P2P 推理

> L26: **LocalAI** is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU re
> L32: - **Drop-in API compatibility**: OpenAI, Anthropic, and ElevenLabs APIs across every backend
> L36: - **Built-in AI agents**: autonomous agents with tool use, RAG, MCP, and skills

## microsoft/qlib（⭐49440，confidence: high）

**面向量化研究的 AI 量化投资平台**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=research`

Qlib 是微软开源的量化投资研究平台，覆盖数据处理、模型训练、回测的完整机器学习流水线，以及 Alpha 挖掘、风险建模、组合优化、订单执行的量化全链条。支持监督学习、市场动态建模（概念漂移适应）与强化学习等多种建模范式，内置多个已发表论文的量化模型。组件采用松耦合设计，可独立使用。安装方面提供 pip 与源码两种途径；官方数据集当前临时禁用，可使用社区数据源或自行从 Yahoo Finance 抓取数据。

- 覆盖量化投资全链条：Alpha 挖掘、风险建模、组合优化、订单执行
- 支持监督学习、市场动态建模、强化学习多种 ML 范式
- 内置多个已发表量化模型（论文模型 Zoo）与嵌套交易决策框架
- 提供 RD-Agent（LLM 自动因子挖掘与模型优化）集成

> L92: Qlib is an open-source, AI-oriented quantitative investment platform that aims to realize the potential, empower researc
> L96: It contains the full ML pipeline of data processing, model training, back-testing; and covers the entire chain of quanti
> L173:   pip install pyqlib

## JuliaLang/julia（⭐49211，confidence: high）

**面向技术计算的高性能动态编程语言**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Julia 是一种面向技术计算的高级动态编程语言，官方仓库提供源代码、编译与安装说明。安装推荐使用 juliaup 管理多版本，也可手动下载二进制或从源码 git clone 后用 make 编译，编译需约 2GiB 磁盘与 4GiB 虚拟内存。README 还涵盖源码目录结构、REPL 使用、以及 Emacs/Vim/VS Code/Jupyter/Pluto 等编辑与笔记本环境支持。

- 面向技术计算的高级动态语言
- juliaup 安装管理器支持多版本共存与更新
- 支持从源码 make 编译构建
- 提供 REPL 及多种编辑器/IDE/笔记本支持

> L17: Julia is a high-level, high-performance dynamic language for technical
> L52: The recommended way of installing Julia is to use `juliaup` which will install
> L88: To build the `julia` executable, run `make` from within the julia directory.

## HKUDS/nanobot（⭐49127，confidence: mid）

**给个人用户的自托管轻量 AI agent 框架**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

以 Python 编写的自托管个人 AI agent 框架：提供浏览器 WebUI、终端 TUI 及 Telegram/Discord/Slack/微信/邮件等聊天渠道接入，内置文件读写、shell、网页搜索/抓取、MCP、定时任务、图像生成与多 agent 委派，通过 Dream 保存会话历史与长期记忆，并暴露 Python SDK 与 OpenAI 兼容 API。需自备模型供应商账号或本地模型服务，框架本身不提供模型。通过安装脚本、uv/pip 安装 PyPI 包或源码检出运行。

- WebUI、终端 TUI 与多聊天渠道接入
- 内置文件工具支持读取 PDF/Word/Excel/PowerPoint
- 通过 Dream 保存长期记忆，支持长时目标与定时自动化
- 暴露 Python SDK 与 OpenAI 兼容 API

> L28: 🐈 **nanobot** is an ultra-lightweight, open-source, self-hosted personal AI agent framework written in Python. Use it in
> L49: - connect to Telegram, Discord, Slack, WeChat, Email, Mattermost, Linear, and other channels
> L61: - **Model freedom**: OpenAI-compatible APIs, local LLMs, image generation, search, and fallbacks.

## jeecgboot/JeecgBoot（⭐48245，confidence: high）

**企业级 AI 低代码平台：一句话生成前后端系统**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=local-ok · hardware=— · install_friction=medium · maturity=—`

基于 Spring Boot 与 Vue3 前后端分离架构的 AI 低代码开发平台，核心能力为低代码开发、AI 应用平台与 AI 知识库。AI Skills 结合 Claude Code 支持自然语言生成代码、表单、流程、报表与大屏；内置 AI 聊天、知识库（RAG）、流程编排、MCP 插件等模块。代码生成器支持单表、树表、一对一/一对多模型，兼容 MySQL、Oracle、PostgreSQL、达梦、人大金仓等多种数据库，支持单体与微服务部署。默认账号 admin/123456，提供 IDEA 与 Docker 启动方式。

- 一句话生成完整系统：AI 自动建表、生成前后端 CRUD 代码与菜单权限
- AI 应用平台：聊天助手、知识库（RAG）、流程编排、MCP 与插件管理
- 兼容多种主流大模型（ChatGPT、DeepSeek、Ollama、千问、智普、minimax 等）
- 支持单体/微服务切换，兼容 MySQL、Oracle、达梦、人大金仓等多种数据库

> L17: JeecgBoot 是一款 AI 低代码开发平台，以 **低代码开发、AI 应用平台和 AI 知识库** 为核心能力。随着 AI Skills 自然语言编程的发布，平台迈入低代码 v2.0：开发者可用一句话生成完整系统或业务模块，由 AI 
> L167: - AI框架：langchain4j 1.17.2，AI模型支持 `ChatGPT` `DeepSeek` `千问` `智普` `minimax`、`本地模型`等

## GitHubDaily/GitHubDaily（⭐48216，confidence: mid）

**面向开发者的 GitHub 开源项目分享与年度盘点清单**

`ai_role=ai-knowledge · license_risk=none · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=idea`

GitHubDaily 自 2015 年起维护的开源项目分享仓库，累计分享超 10000 个项目，内容涵盖技术资料、开发者工具、编程网站与应用。README 按年份复盘并分类整理，2025 年部分设 AI 工具、后端、前端等目录，每条以表格形式给出项目名与简述；同时引导用户通过公众号、微博、知乎、X 等社交平台获取更新，并可在 issues 推荐或自荐项目。

- 累计收录超 10000 个开源项目的分享清单
- 按年份（2018–2025）与领域分类整理复盘目录
- 通过 issues 接受项目推荐或自荐
- 同步运营公众号、微博、知乎、X 多个传播渠道

> L17: 秉着挖掘开源价值的初衷，GitHubDaily 自 2015 年 10 月 10 日正式成立。
> L21: 目前，GitHubDaily 已累积分享超过 10000 个开源项目，内容包括但不限于 GitHub 上的开源技术资料、开发者工具、编程网站以及成熟应用。
> L36: 下面是对 GitHubDaily 在 2025 年所推荐的项目进行分类整理，方便大家查找以往分享过的内容。

## zhayujie/CowAgent（⭐47441，confidence: high）

**个人 AI 助手框架：任务规划、工具技能、多渠道接入**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

CowAgent 是一个开源自托管个人 AI 助手/Agent Harness 参考实现：消息经 Channels 接入，Agent Core 基于记忆、知识与工具进行任务规划与执行，模型层生成回复。三层记忆架构（上下文→日→长期）加夜间 Deep Dream 蒸馏，自动维护 Markdown 知识库与知识图谱，支持 Skill Hub 一键装技能、MCP 协议接入工具，Web 控制台统一配置。提供一行安装脚本、Docker、桌面客户端，可 24/7 运行于个人电脑或服务器。

- 三层记忆架构（上下文→每日→长期）与 Deep Dream 夜间蒸馏
- Skill Hub/GitHub/对话式生成技能，原生 MCP 集成（stdio/SSE，热重载）
- 内置 10+ 工具（文件、终端、浏览器自动化、搜索、调度等）
- 多渠道并行：Web、微信、飞书、钉钉、Telegram、Slack 等 12 种

> L14: **CowAgent** is an open-source super AI assistant that proactively plans tasks, controls your computer and external serv
> L52: CowAgent is a complete **Agent Harness**: messages flow in through **Channels**; the **Agent Core** plans and reasons ov
> L172: **MCP protocol** integrates the open ecosystem of Model Context Protocol servers. A single `mcp.json` is enough — suppor

## apache/airflow（⭐47197，confidence: mid）

**数据与 AI 工作流的编排平台：用代码编写、调度和监控**

`ai_role=ai-enhanced · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

Apache 软件基金会的工作流编排平台，以代码定义工作流（Dag），由调度器按依赖关系在 worker 上执行任务，配合 CLI 与 Web 界面监控运行中的流水线。工作流以代码形式定义，便于版本管理、测试与协作。任务要求幂等，任务间通过 XCom 传递元数据而非大批量数据；定位为批处理编排，非流式方案，也非 agent 本身。README 提到其广泛用于编排机器学习与基于 LLM 的工作负载（数据准备、工具调用、模型调用、评估等步骤）。通过 PyPI 配约束文件安装，官方支持 pip 与 uv。

- 以代码定义 Dag，调度器按依赖在 worker 数组上执行任务
- Jinja 模板引擎支持自定义，内置多种 operator 可扩展
- Web UI 提供 Dags、Assets、Grid、Graph、Backfill 等视图
- 仅官方支持 pip/uv 安装，需配合约束文件保证可重复安装

> L21: Apache Airflow (or simply Airflow) is a platform to programmatically author, schedule, and monitor workflows.
> L35: Beyond traditional data pipelines, Airflow is widely used to orchestrate machine learning workflows — training, retraini
> L107: > Note: Only `pip` and `uv` installation is currently officially supported.

## siyuan-note/siyuan（⭐46812，confidence: mid）

**隐私优先自托管知识管理工具，人与 AI agent 协作**

`ai_role=ai-enhanced · license_risk=viral · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=—`

思源笔记是一个隐私优先的个人知识管理系统，支持块级引用与 Markdown 所见即所得编辑，涵盖双向链接、SQL 查询嵌入、数据库表格视图、间隔重复闪卡、PDF 标注、导出为 PDF/Word/HTML 等功能。AI 方面通过 OpenAI API 提供写作与问答聊天，主题标签与项目描述表明支持 MCP 与 agent 协作场景。桌面端通过应用商店或安装包分发，移动端有 Android/iOS/HarmonyOS 应用，服务端提供 Docker 部署与社区维护的 Helm chart，部分功能仅对付费会员开放。

- 块级引用、双向链接与 SQL 查询嵌入的内容块体系
- 通过 OpenAI API 提供 AI 写作与问答聊天
- Docker 部署支持 PUID/PGID 权限配置与 OIDC 认证
- 多端应用：Android/iOS/HarmonyOS 与桌面安装包

> L18: SiYuan is a privacy-first personal knowledge management system, supporting fine-grained block-level reference and Markdo
> L53: - AI writing and Q/A chat via OpenAI API
> L59: - Docker deployment

## paperless-ngx/paperless-ngx（⭐46805，confidence: high）

**将纸质文档扫描、索引并归档为可搜索在线档案的文档管理系统**

`ai_role=ai-ecosystem · license_risk=viral · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

社区维护的文档管理系统，把实体文档转化为可搜索的在线归档，主题标签涉及 OCR、机器学习、PDF 等能力方向。项目是 Paperless 与 Paperless-ng 的官方继任者，由团队分工推进，提供多语言翻译协作、GitHub Discussions 收集功能请求，并有在线 demo。README 提醒文档可能包含敏感信息，数据明文存储，建议在本地可信服务器上运行并做好备份。

- 将实体文档转化为可搜索在线归档
- 提供 docker compose 部署路径与安装脚本
- 支持多语言翻译协作与社区团队分工
- 提供官方在线 demo（demo.paperless-ngx.com）

> L10: Paperless-ngx is a document management system that transforms your physical documents into a searchable online archive s
> L29: The easiest way to deploy paperless is `docker compose`. The files in the `/docker/compose` directory are configured to 
> L12: Paperless-ngx is the official successor to the original Paperless & Paperless-ng projects and is designed to distribute 

## milvus-io/milvus（⭐46407，confidence: high）

**面向 AI 应用的分布式向量数据库：存储并检索大规模向量**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=—`

以 Go 和 C++ 编写的云原生向量数据库，存储向量与标量数据并支持向量 ANN 检索、元数据过滤与混合搜索。支持分布式（K8s 部署、计算存储分离）、单机 Standalone 与 Python pip 安装的 Milvus Lite 三种形态。索引类型覆盖 HNSW、IVF、FLAT、SCANN、DiskANN 及 GPU 索引（如 NVIDIA CAGRA），并原生支持 BM25 全文检索与 SPLADE/BGE-M3 稀疏向量。提供用户认证、TLS、RBAC 等企业特性，Apache 2.0 许可，隶属 LF AI & Data 基金会。

- 支持 HNSW、IVF、DiskANN 等多种索引类型及 GPU 索引（CAGRA）
- 分布式架构支持水平扩展，并提供 Standalone 与 Milvus Lite 部署形态
- 原生支持 BM25 全文检索与 SPLADE/BGE-M3 稀疏向量的混合搜索
- 提供用户认证、TLS 加密与 RBAC 访问控制

> L16: 🐦 Milvus is a high-performance vector database built for scale. It powers AI applications by efficiently organizing and 
> L134:  Milvus integrates with a comprehensive suite of AI development tools, such as LangChain, LlamaIndex, OpenAI and Hugging

## streamlit/streamlit（⭐46021，confidence: high）

**让开发者用 Python 脚本快速构建和分享数据应用**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

Streamlit 将 Python 脚本转换为交互式 Web 应用的框架：提供输入组件、数据框、图表、布局与多页面应用等元素，编辑脚本后应用即时更新。应用可通过 Streamlit Community Cloud 平台免费部署、管理和分享。通过 pip 安装，社区可通过 Streamlit Components 扩展功能；目前 README 注明已暂停接受维护者团队之外的 pull request。

- 将 Python 脚本转换为交互式 Web 应用（仪表盘、报告、聊天应用）
- 实时编辑：脚本修改后应用即时更新
- Community Cloud 平台免费部署、管理和分享应用
- 支持通过 Streamlit Components 扩展能力

> L9: Streamlit lets you transform Python scripts into interactive web apps in minutes, instead of weeks. Build dashboards, ge
> L92: - 🤖 LLMs & chatbot apps
> L103: Deploy, manage and share your apps for free using our Community Cloud! Sign-up here.

## LibreChat-AI/LibreChat（⭐45867，confidence: high）

**自托管多模型 AI 聊天平台：统一接入多家服务商**

`ai_role=ai-native · license_risk=permissive · deploy=desktop · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

自托管的 AI 对话平台，将多家模型服务商统一在一个界面中，支持自定义端点（任何 OpenAI 兼容 API）。提供 Agent 构建与市场、MCP 工具接入、SKILL.md 技能包、代码解释器沙箱（Python/Node.js/Go 等多语言）、联网搜索、图像生成、Artifacts、语音输入输出、消息搜索与导入导出。多用户场景支持 OAuth2/LDAP/邮箱登录、管理面板与按角色权限配置，可单机或配合 Redis 水平扩展部署，提供 Docker Compose 一键部署栈。

- 统一界面接入多家模型服务商，支持任意 OpenAI 兼容自定义端点
- Agent 体系：无代码构建、市场分享、子代理、MCP 与 SKILL.md 技能
- 沙箱化代码解释器支持 Python、Node.js、Go、C/C++ 等语言
- 多用户安全认证（OAuth2/LDAP）、管理面板与 Token 用量工具

> L63: - 🤖 **AI Model Selection**:
> L173: LibreChat is a self-hosted AI chat platform that unifies all major AI providers in a single, privacy-focused interface.
> L175: Beyond chat, LibreChat provides AI Agents, Model Context Protocol (MCP) support, Artifacts, Code Interpreter, custom act

## janhq/jan（⭐44978，confidence: high）

**给个人用户的本地离线 LLM 客户端：下载并运行模型**

`ai_role=ai-native · license_risk=none · deploy=desktop · model_dep=locked-api · hardware=— · install_friction=high · maturity=—`

基于 Tauri 与 llama.cpp 的桌面应用，可在本地下载并运行 HuggingFace 上的 LLM（Llama、Gemma、Qwen 等）。支持接入 OpenAI、Anthropic、Groq、Mistral 等云端模型，提供 localhost:1337 的 OpenAI 兼容 API 服务器，并集成 MCP 以支持 agent 能力。提供 Windows/macOS/Linux 安装包与源码构建途径，Apache 2.0 许可。

- 本地下载并运行 HuggingFace 上的 LLM
- localhost:1337 提供 OpenAI 兼容 API 服务器
- MCP 集成支持 agentic 能力
- 多种引擎变体（cpu/vulkan/metal/cuda12/cuda13/hip）

> L62: - **Local AI Models**: Download and run LLMs (Llama, Gemma, Qwen, GPT-oss etc.) from HuggingFace
> L63: - **Cloud Integration**: Connect to GPT models via OpenAI, Claude models via Anthropic, Mistral, Groq, MiniMax, and othe
> L65: - **OpenAI-Compatible API**: Local server at `localhost:1337` for other applications

## herdrdev/herdr（⭐44476，confidence: high）

**给编码 Agent 提供后台会话复用与多机终端管理的运行时**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=medium · maturity=—`

用 Rust 编写的终端复用器，定位为编码 Agent 的运行时：客户端断开或 SSH 掉线后终端在后台服务器继续运行，重启后恢复布局并可恢复受支持的 Agent 会话；支持本地与 SSH 机器合并为统一 Agent 列表，每个窗格标记 working/blocked/idle 状态。Agent 可通过 CLI 与 socket API 驱动 herdr（互相生成窗格、发送提示、等待阻塞）。单个二进制运行，提供插件与市场。

- 客户端关闭/SSH 掉线后台服务器保持运行，重启后恢复布局与部分 Agent 会话
- 窗格状态标记（working/blocked/idle），Agent 阻塞等待输入时提示
- agent-native：CLI 与 socket API 供 Agent 生成窗格、互相提示与等待
- 单一 Rust 二进制，tmux 风格快捷键与鼠标操作并存

> L18: **the runtime your coding agents live on.**
> L23: - **agent-native** — agents drive herdr through the cli and socket api: they can spawn panes, prompt each other, and wai
> L24: - **runs what you already run** — claude code, codex, cursor, opencode, grok and the rest. herdr doesn't wrap or replace

## reactive-resume/reactive-resume（⭐44432，confidence: high）

**面向求职者的开源隐私优先简历与求职追踪构建器**

`ai_role=ai-enhanced · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

开源简历构建器，覆盖简历与求职信编写、实时 PDF 预览、17 套模板、可读性与职位关键词检查、求职申请追踪，以及通过公共链接分享。AI 部分为可选功能：文档旁的 AI 助手可提出修改建议、审阅写作、依据职位描述起草求职信；用户提供 OpenAI、Anthropic、Gemini、Ollama 等自有服务接入。提供 REST API 与 MCP server。可通过托管服务使用，或经 Docker、Vercel、Cloudflare Workers、Hostinger 自托管，依赖 PostgreSQL 与上传存储。

- 可选 AI 助手：逐条接受/拒绝建议的编辑工作流
- 接入 OpenAI、Anthropic、Gemini、OpenRouter、Ollama 等 provider 及兼容端点
- 提供 REST API 与 MCP server 用于文档管理、导入导出与检查
- 支持 Docker、Vercel、Cloudflare Workers、Hostinger 多种自托管方式

> L92: **AI Assistant**
> L97: - Connect OpenAI, Anthropic, Google Gemini, OpenRouter, Ollama, or other supported providers and compatible endpoints
> L110: - Self-host with Docker, Vercel, Cloudflare Workers, or a 1-click deploy on Hostinger

## danielmiessler/Fabric（⭐44317，confidence: high）

**面向命令行用户的 AI 提示词组织与调用框架**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

开源 AI 框架，将提示词组织为 Patterns（按现实任务分类的可复用单元），供用户在各工具中调用，也可作为命令行界面直接使用。覆盖提取视频要点、写文章、摘要论文、生成总结等任务场景。提供 Go 实现与 REST API，支持 10 余种原生接入的 AI 提供商及数十家 OpenAI 兼容供应商，配置按 Pattern 映射模型。安装覆盖脚本、二进制、多包管理器与 Docker。

- 以 Patterns（提示词单元）组织 AI 能力，按任务分类管理
- 原生接入十余家 AI 提供商，另支持数十家 OpenAI 兼容供应商
- 提供 CLI 与 REST API（含 Swagger/OpenAPI 文档）两种使用方式
- 支持按 Pattern 配置模型映射（FABRIC_MODEL_PATTERN_NAME 环境变量）

> L22:  <code>fabric</code> is an open-source framework for augmenting humans using AI.
> L50: **Fabric was created to address this by creating and organizing the fundamental units of AI—the prompts themselves!**
> L253: Fabric supports a wide range of AI providers:

## Kong/kong（⭐44276，confidence: high）

**面向 API/LLM/MCP 流量的云原生网关**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

Kong Gateway 是一个云原生、平台无关的网关，提供代理、路由、负载均衡、健康检查、认证等功能，作为微服务或常规 API 流量的中央编排层，并扩展至 LLM 与 MCP 流量。AI 能力包括多 LLM 提供商路由、语义安全、MCP 流量治理与可观测性、语义路由与缓存等。支持 Kubernetes Ingress Controller、数据库无关部署与混合部署（控制面/数据面分离），通过插件机制扩展功能，另有 Kong Konnect 云托管与商业订阅版本。

- Universal LLM API 支持跨 OpenAI、Anthropic、Gemini、Bedrock 等多家提供商路由
- MCP 流量治理、安全与可观测性，并可从任意 RESTful API 自动生成 MCP
- 60+ AI 功能，含 AI 可观测性、语义安全与缓存、语义路由
- 通过官方 Kubernetes Ingress Controller 原生运行于 Kubernetes

> L5: Kong or Kong Gateway is a cloud-native, platform-agnostic, scalable **API 𖧹 LLM 𖧹 MCP** Gateway distinguished for its hi
> L57: - Universal LLM API to route across multiple providers like OpenAI, Anthropic, GCP Gemini, AWS Bedrock, Azure AI, Databr

## ray-project/ray（⭐44051，confidence: high）

**分布式 AI 计算引擎：把 ML 工作负载从笔记本扩展到集群**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=research`

Ray 提供一个核心分布式运行时和一组 AI 库，用于扩展 AI 与 Python 应用。AI 库包括 Data（可扩展数据集）、Train（分布式训练）、Tune（超参数调优）、RLlib（强化学习）、Serve（服务化）；Ray Core 提供 Tasks、Actors、Objects 三种抽象。支持在任意机器、集群、云提供商与 Kubernetes 上运行，并有社区集成生态。通过 pip 安装，提供 Dashboard 监控与分布式调试器。

- 核心分布式运行时（Tasks/Actors/Objects）与 5 个 AI 库（Data/Train/Tune/RLlib/Serve）
- 同一代码可在笔记本与集群间扩展
- 运行于任意机器、集群、云提供商与 Kubernetes
- 提供 Ray Dashboard 监控与 Distributed Debugger 调试

> L18: Ray is a unified framework for scaling AI and Python applications. Ray consists of a core distributed runtime and a set 
> L47: Install Ray with: ``pip install ray``. For nightly wheels, see the
> L44: Ray runs on any machine, cluster, cloud provider, and Kubernetes, and features a growing

## gradio-app/gradio（⭐43783，confidence: high）

**面向 ML 开发者：用纯 Python 快速构建并分享模型演示 Web 应用**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=research`

开源 Python 包，用于为机器学习模型、API 或任意 Python 函数生成演示或 Web 应用，无需 JavaScript/CSS 或 Web 托管经验。提供高层 Interface 类、低层 Blocks 布局类和 ChatInterface 聊天界面类，内置 30 余个组件；launch(share=True) 可生成公开 URL 而计算保留在本地。附带 Python/JS 客户端库以编程方式查询应用，支持热重载模式与 --vibe 自然语言编辑，提供 gradio skills add 为 AI 编码助手安装 Gradio 知识技能。要求 Python 3.10+，Apache 2.0 许可。

- Interface/Blocks/ChatInterface 三层抽象，30+ 内置组件
- share=True 一键生成公开访问 URL，计算保留本地
- gradio_client（Python）与 @gradio/client（JS）编程查询
- gradio skills add 为编码助手安装 Gradio 技能

> L21: # Gradio: Build Machine Learning Web Apps — in Python
> L63:  > When developing locally, you can run your Gradio app in hot reload mode , which automatically reloads the Gradio app 
> L136: Gradio provides a "skill" that enriches AI coding assistants (like Cursor, Claude Code, Codex, etc.) with Gradio-specifi

## langchain-ai/langgraph（⭐43403，confidence: high）

**面向构建有状态长期运行 agent 的低层编排框架**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

LangGraph 是由 LangChain Inc 构建的 Python 库，用于构建、管理和部署长期运行的有状态 agent 与工作流。提供持久化执行（失败后自动从断点恢复）、人在回路（检查和修改执行状态）、短期与长期记忆、通过 LangSmith 调试追踪，以及面向生产环境的部署基础设施。可独立使用，也可与 LangChain 产品线配合使用；另提供 JS/TS 版本及更高层的 Deep Agents 包。

- 持久化执行：agent 可跨故障运行并在断点处自动恢复
- 人在回路：执行过程中可检查与修改 agent 状态
- 短期工作记忆与跨会话长期记忆支持
- pip install -U langgraph 即可安装，另有 LangGraph.js 版本

> L7:  Low-level orchestration framework for building stateful agents.
> L14: Trusted by companies shaping the future of agents – including Klarna, Replit, Elastic, and more – LangGraph is a low-lev
> L68: LangGraph is inspired by Pregel and Apache Beam. The public interface draws inspiration from NetworkX. LangGraph is buil

## deepspeedai/DeepSpeed（⭐43238，confidence: high）

**面向大模型训练与推理的分布式优化库**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=high · maturity=research`

DeepSpeed 是一个深度学习优化库，提供分布式训练与推理能力，核心机制包括 ZeRO、ZeRO-Infinity、3D 并行、Ulysses 序列并行、DeepSpeed-MoE 等。支持 NVIDIA（Pascal 至 Hopper）、AMD MI100/MI200，并有华为昇腾 NPU、Intel Gaudi 2/Xeon/XPU、Tecorigin SDAA 等社区贡献的硬件适配。通过 pip 安装，C++/CUDA 扩展默认以 JIT 方式在运行时构建；Windows 支持部分训练与推理功能。曾用于训练 MT-530B、BLOOM 等大模型。

- ZeRO/ZeRO-Infinity、3D 并行、Ulysses 序列并行、DeepSpeed-MoE 等系统机制
- 多硬件后端：NVIDIA/AMD/CPU/Gaudi2/XPU/昇腾 NPU/SDAA
- 与 Transformers、Accelerate、Lightning、MosaicML、Determined、MMEngine 等框架集成
- pip 安装 + torch JIT 编译扩展，ds_report 校验环境

> L52: # Extreme Speed and Scale for DL Training
> L54: ***DeepSpeed enabled the world's most powerful language models (at the time of this writing) such as MT-530B and BLOOM**
> L100: # Installation
> L110: ## Requirements

## agno-agi/agno（⭐42777，confidence: high）

**供开发者构建、运行并管理 agent 平台的框架与运行时**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Agno 提供 SDK 与 AgentOS 运行时：用 SDK 构建 agent，作为服务运行（REST API、SSE、websockets），并通过 Web UI 管理平台。数据与链路存于自有 Postgres 数据库，内置 JWT RBAC、多租户隔离、人工审批、OpenTelemetry 可观测性与定时任务。上手路径是把提示词交给编码 agent（Claude Code、Cursor 等）从模板仓库部署，也支持手写代码；模板覆盖 Railway、Docker、AWS、GCP、Azure 等部署目标。每轮 agent 运行发送遥测事件，可用 AGNO_TELEMETRY=false 关闭。

- SDK 构建 + AgentOS 运行时 + Web UI 管理的组合
- 50+ 端点的生产 API，支持 SSE 与 websockets
- JWT RBAC 与多用户多租户隔离
- 100+ 预置工具集成（GitHub、Slack、Postgres 等）

> L11: Agno is a framework and runtime for agent platforms. Build agents, run them as a service, manage your platform using a w
> L13: - Build your agent platform using the Agno SDK.
> L14: - Run your agent platform using the AgentOS runtime.

## tinyhumansai/openhuman（⭐42130，confidence: high）

**Rust 编写的 agent 运行时：单机运行数百个 agent 的桌面应用与库**

`ai_role=ai-native · license_risk=viral · deploy=desktop · model_dep=local-ok · hardware=— · install_friction=low · maturity=idea`

以 GPL-3.0 发布的 agent harness，编译为单进程 Rust 核心，同时提供桌面应用（macOS/Windows/Linux 安装包）与 Rust 库两种形态。内置记忆（每轮按 token 预算召回并附引用）、Jev 工具搜索模型（在 1,215 个工具中选取）、浏览器与桌面控制、MCP 与技能、14 个消息渠道及 Composio 的 119 个 OAuth 集成。模型经 BYOK 接入 26 个 provider，本地模型支持 Ollama、LM Studio、MLX，含自动模型路由。当前为 early beta。README 中列出与六个其他 harness 的公开基准数据，复现材料在 openhuman-benchmarks 仓库。

- 桌面应用与 Rust 库双形态，单进程可并行运行数百个 agent（README 称 500 个可放于 $10 VPS）
- RLM token 压缩：大型工具结果压缩为可检索句柄后再交给模型
- Jev 小模型做工具搜索，无截图地从屏幕按钮选取点击
- 14 个消息渠道（Telegram/Discord/iMessage/邮件等）作为 agent 前端

> L4:  A desktop app for people. A Rust library for developers.
> L84:  Use it as a Rust library: call an agent like any other function, or run a whole fleet from one small server.
> L164: |Models|Local models (Ollama, LM Studio, MLX) and BYOK for 26 providers, with automatic model routing|

## AstrBotDevs/AstrBot（⭐42055，confidence: mid）

**对接多家 IM 平台与 LLM 的开源 Agent 聊天机器人平台**

`ai_role=ai-native · license_risk=viral · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

AstrBot 是一个开源的一体化 Agent 聊天机器人平台，接入 QQ、微信企业版、飞书、钉钉、Telegram、Slack、Discord 等 20 个即时通讯平台，提供 LLM 对话、多模态、MCP、知识库、人设、自动上下文压缩等能力，并以插件机制扩展（README 称有 1000+ 插件可一键安装）。支持 Dify、阿里云百炼、Coze 等 agent 平台接入，Agent Sandbox 提供代码与 shell 的隔离执行。部署途径包括 uv、Docker、桌面应用、启动器及宝塔/1Panel/CasaOS 等。

- 接入 20 个 IM 平台（QQ、Telegram、Discord、飞书、钉钉等），官方/社区维护
- 支持多家 LLM 服务与 API 网关，含 Ollama、LM Studio 自托管
- 1000+ 插件一键安装的插件扩展机制（README 自述）
- Agent Sandbox 隔离执行代码与 shell 调用

> L24: AstrBot is an open-source all-in-one Agent chatbot platform that integrates with mainstream instant messaging apps. It p
> L33: 4. 🌐 Multi-Platform: QQ, WeChat Work, Feishu, DingTalk, WeChat Official Accounts, Telegram, Slack, and more.
> L127: |OpenAI and Compatible Services|LLM Services|

## chatboxai/chatbox（⭐42047，confidence: mid）

**面向桌面/移动端用户的多模型 AI 聊天客户端**

`ai_role=ai-enhanced · license_risk=dual · deploy=desktop · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

Chatbox 社区版是一个开源（GPLv3）的桌面 AI 客户端，支持接入多家 LLM 服务（OpenAI、Azure OpenAI、Claude、Gemini、Ollama、ChatGLM-6B 等），提供本地数据存储、Dall-E-3 图像生成、Markdown/LaTeX 渲染、流式回复、提示词库、团队 API 共享、多语言界面等。覆盖 Windows/macOS/Linux 桌面端及 iOS/Android/Web。仓库与商业 pro 版定期双向同步代码，非完全独立演进。

- 支持多家 LLM 提供商：OpenAI、Azure OpenAI、Claude、Gemini、Ollama 本地模型、ChatGLM-6B
- 数据本地存储，提供桌面、Web、iOS/Android 多端形态
- Dall-E-3 图像生成、Markdown/LaTeX 渲染、流式回复、提示词库
- GPLv3 开源社区版，与 pro 仓库定期同步代码

> L7:  Your Ultimate AI Copilot on the Desktop. Chatbox is a desktop client for ChatGPT, Claude and other LLMs, available on W
> L35: This is the repository for the Chatbox Community Edition, open-sourced under the GPLv3 license.
> L105: - **Support for Multiple LLM Providers**

## HKUDS/DeepTutor（⭐41565，confidence: low）

**面向学习者的多智能体个性化辅导系统**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

由 HKUDS 维护的开源 AI 辅导系统，围绕知识库（RAG）、多智能体循环与三层记忆构建，提供 Chat、Guided Learning、Deep Research、Book 生成、Visualize、练习题等功能面；支持接入自建 Partners（可连接本地 Claude Code / Codex）、通过 15 个 IM 渠道通信、以 Docker Compose 或源码部署，并区分单用户与多用户（含管理员账户）部署形态。提供 CLI（deeptutor start / skill install）与在线文档站点。

- 知识中心支持 GraphRAG / LightRAG / PageIndex / 关联知识库 / Obsidian
- 三层记忆（L1/L2/L3）与单智能体循环驱动的学习功能面
- 可通过 15 个 IM 渠道接入 Partners 机器人
- 提供 CLI：deeptutor start、deeptutor skill install、deeptutor doctor

> L3: # DeepTutor: Lifelong Personalized Tutoring
> L137: > **[2026.5.22]** v1.4.0 — GA cut of v1.4: Auto Mode, three-layer Memory, agentic Deep Research / Solve / Question, Llam
> L23: Python 3.11+

## hpcaitech/ColossalAI（⭐41431，confidence: high）

**面向开发者的大模型分布式训练与推理加速系统**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

分布式深度学习训练与推理框架：提供数据并行、流水线并行、1D/2D/2.5D/3D 张量并行、序列并行、ZeRO、自动并行等并行策略，以及异构内存管理（PatrickStar）；支持通过配置文件声明并行方式，用少量代码启动分布式训练与推理。附带应用示例（Open-Sora 视频生成、Colossal-LLaMA-2、ColossalChat RLHF 流水线、Stable Diffusion 加速、AlphaFold 加速）和 LLaMA3/2/1、MoE、GPT、BERT 等训练 demo，并提供文档、示例与论坛。

- 多种并行策略：数据/流水线/1D-2D-2.5D-3D 张量/序列并行/ZeRO/自动并行
- 异构内存管理（PatrickStar）与配置文件驱动的并行声明
- 附带 ColossalChat 完整 RLHF 流水线与 Open-Sora 视频生成应用
- 提供 LLaMA、GPT、BERT、MoE、AlphaFold 等训练示例

> L93: Colossal-AI provides a collection of parallel components for you. We aim to support you to write your
> L95: distributed training and inference in a few lines.
> L97: - Parallelism strategies

## anthropics/claude-plugins-official（⭐41420，confidence: high）

**Anthropic 官方维护的 Claude Code 插件市场目录**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

由 Anthropic 管理的 Claude Code 插件官方目录，分内部插件（/plugins，Anthropic 团队开发）与外部插件（/external_plugins，第三方伙伴与社区提交，需通过质量与安全审核）。插件通过 Claude Code 内置插件系统安装（/plugin install 命令或 Discover 界面浏览）。README 还规定了插件目录结构（plugin.json 清单）、插件名 slug 不可变更及 renames 迁移机制、以及无清单仓库以 skills 数组打包技能的方式。

- 官方市场，插件可经 /plugin install {name}@claude-plugins-official 安装
- 内部插件由 Anthropic 开发，外部插件需质量与安全审核
- 插件名 slug 不可变，renames 映射支持重命名自动迁移
- 支持 skill-bundle 形式：无清单仓库可直接声明 SKILL.md 技能路径

> L3: A curated directory of high-quality plugins for Claude Code.
> L9: - **`/plugins`** - Internal plugins developed and maintained by Anthropic
> L10: - **`/external_plugins`** - Third-party plugins from partners and the community

## microsoft/BitNet（⭐41180，confidence: high）

**1-bit 大模型的官方 CPU/GPU 推理框架**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=research`

bitnet.cpp 是 1-bit LLM（如 BitNet b1.58）的官方推理框架，提供 I2_S/TL1/TL2 等优化内核，支持在 x86 与 ARM CPU 及 GPU 上运行，并附 CPU/GPU 推理基准脚本与 .safetensors 转 gguf 的转换脚本。官方在 Hugging Face 发布 BitNet-b1.58-2B-4T 与两个 embedding 模型，社区模型列表含 Llama3-8B-1.58、Falcon3/Falcon-E 家族。构建需 python>=3.10、cmake>=3.22、clang>=18，Windows 需 Visual Studio 2022，从源码克隆编译后经 setup_env.py 下载/量化模型运行。

- 提供 I2_S、TL1、TL2 三种内核，按模型与 CPU 架构列出支持矩阵
- 支持对话模式（-cnv）与线程数、上下文、温度等推理参数
- 提供端到端基准脚本与 dummy 模型生成脚本用于本机测试
- 支持从 .safetensors 检查点转换为 gguf 模型

> L44: bitnet.cpp is the official inference framework for 1-bit LLMs (e.g., BitNet b1.58). It offers a suite of optimized kerne
> L204: ## Installation
> L221: ### Build from source

## codewhale-hq/Codewhale（⭐41093，confidence: high）

**开源 Rust 编码 agent 引擎与终端客户端，任意模型可选**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

Codewhale 提供本地运行的 Rust agent 引擎与终端客户端：读取项目、编辑文件、执行命令并自查工作，模型由用户自选（40+ 内置 provider 路由，含本地运行时）。核心机制包括 Plan/Work/Operate 三种模式、Ask/Auto-Review/Full Access 三种审批姿态、/undo 与 /restore 工作区恢复、/receipts 会话操作清单，以及 OS 沙箱（macOS Seatbelt、Linux bubblewrap）。安装覆盖 curl 脚本、winget、npm、cargo、Docker、Nix 等多条路线。

- 40+ 内置 provider 路由，支持 OpenAI 兼容端点与 Ollama/vLLM/SGLang 本地模型
- Plan/Work/Operate 模式与审批姿态、/receipts 全量操作回执
- 子 agent 委派与受监督 agent 团队（含 pre-spend check）
- MCP 服务器、skills、plugins、hooks 扩展，并加载 Claude Code 插件

> L3: **The open-source coding agent that works with any model.**
> L95: - **Any model, no lock-in.** Over 40 built-in provider routes — Anthropic,
> L77: Every client drives the same local Codewhale Engine, so

## pingcap/tidb（⭐40646，confidence: high）

**开源分布式 SQL 数据库：面向事务、分析与向量检索负载**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

TiDB 是开源、云原生的分布式 SQL 数据库，采用存算分离架构，通过两阶段提交与 Raft 协议提供分布式事务、强一致与高可用。内置 TiKV 行存与 TiFlash 列存双引擎，支持 HTAP 混合负载；兼容 MySQL 8.0 协议与工具生态，提供迁移工具；支持向量搜索。可部署于本地、公有云或 Kubernetes（TiDB Operator），亦提供全托管的 TiDB Cloud（含免费计划）。以 Go 编写，Apache 2.0 许可。

- 两阶段提交 + Raft 多副本的分布式事务与自动故障转移
- TiKV 行存与 TiFlash 列存双引擎 HTAP 架构
- 兼容 MySQL 8.0 协议、框架与工具，支持向量搜索
- 支持本地、Kubernetes（TiDB Operator）与 TiDB Cloud 托管部署

> L14: TiDB (/’taɪdiːbi:/, "Ti" stands for Titanium) is an open-source, cloud-native, distributed SQL database designed for hig
> L26: - **Hybrid Transactional/Analytical Processing (HTAP)**: TiDB provides two storage engines: TiKV, a row-based storage en
> L28: - **Cloud-Native**: TiDB can be deployed in public clouds, on-premises, or natively in Kubernetes. TiDB Operator helps m

## photoprism/photoprism（⭐40311，confidence: high）

**面向个人的自托管 AI 照片管理应用：整理、检索与分享**

`ai_role=ai-enhanced · license_risk=dual · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

PhotoPrism 是一个以隐私为先的 Web 相册应用，运行于自托管服务器或云端，提供照片与视频的浏览、组织和分享功能。基于内容与位置自动打标签，并识别人脸；搜索过滤器支持标签、位置、分辨率、色彩等属性组合。元数据可从 Exif、XMP 及 Google Photos 等来源提取合并；支持 WebDAV 客户端直接连接。以 Go 语言编写（主题标签含 golang/tensorflow），采用 AGPL 许可，社区版通过 Docker 安装，另提供付费会员与商业许可。

- 基于内容与位置自动打标签，支持人脸识别
- 组合式搜索过滤器（标签、位置、分辨率、色彩、质量等）
- 从 Exif/XMP/Google Photos 提取合并元数据
- WebDAV 直接挂载，PWA 跨设备使用

> L10: PhotoPrism® is an AI-powered, privacy-first app for browsing, organizing, and sharing photos and videos. It helps tag, s
> L21: * Automatically labels your pictures based on content and location, and recognizes the faces of your family and friends
> L32: Step-by-step installation instructions for our self-hosted community edition can be found on docs.photoprism.app - all y

## HKUDS/LightRAG（⭐40183，confidence: high）

**面向开发者的轻量知识图谱 RAG 框架**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

HKUDS 出品的轻量级知识图谱 RAG 框架，采用双层架构同时管理知识图谱与向量嵌入，支持增量更新与选择性删除、四种文本分块策略、多文档解析引擎（MinerU/Docling/Native）及多种存储后端（默认内存存储仅适合测试，生产推荐 PostgreSQL）。提供 PyPI/源码/Docker Compose 安装、WebUI、交互式配置向导，并可配合 30B 级开源 LLM 运行。已集成 RAGAS 评估与 Langfuse 追踪。

- 双层架构：知识图谱 + 向量嵌入统一管理
- 四种分块策略与多文档解析引擎（MinerU/Docling/Native）
- 增量更新与文档删除时自动重建受影响实体关系
- 多种生产级存储后端与 WebUI、Docker 部署

> L137: LightRAG is a lightweight knowledge-graph RAG framework and an efficient alternative to Microsoft GraphRAG. It adopts a 
> L145: - **Multiple Document Parsing Engines:** LightRAG's document processing pipeline supports MinerU, Docling, and Native an

## anthropics/financial-services（⭐40163，confidence: high）

**面向金融从业者的 Claude 参考智能体、技能与数据连接器合集**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

由 Anthropic 维护的金融服务领域参考仓库，提供端到端工作流 Agent（Pitch Agent、Market Researcher、GL Reconciler 等）、按 FSI 垂直方向打包的插件（技能、斜杠命令、MCP 连接器），以及 Managed Agents 部署模板。同一套系统提示与技能可通过 Claude Cowork 插件安装，也可经 /v1/agents API 部署。所有输出均标注为供专业人士审阅的分析草稿，不构成投资建议，不执行交易。全部内容基于 markdown/JSON 文件，无构建步骤。

- 10 个端到端工作流 Agent，以自包含插件形式提供
- 9 个垂直插件，含 comps/DCF/LBO 等建模技能与斜杠命令
- 集中管理 11 个 MCP 数据连接器（Daloopa、FactSet、Morningstar 等）
- 支持 Cowork 插件安装与 Claude Managed Agents API 两种部署方式

> L3: Reference agents, skills, and data connectors for the financial-services workflows we see most — investment banking, equ
> L5: Everything here is available **two ways from one source**: install it as a Claude Cowork plugin, or deploy it through th
> L12: - **Agents** — named, end-to-end workflow agents (Pitch Agent, Market Researcher, GL Reconciler, …). Each ships as a Cow

## volcengine/OpenViking（⭐40163，confidence: high）

**给 AI Agent 的上下文数据库：统一记忆、知识与技能**

`ai_role=ai-native · license_risk=dual · deploy=library · model_dep=local-ok · hardware=— · install_friction=low · maturity=research`

OpenViking 把 Agent 的知识、记忆与技能统一组织为 `viking://` 虚拟文件系统，Agent 可用 ls/read/grep 等文件操作浏览和编辑上下文；目录携带 L0 摘要/L1 概览/L2 全文三层结构，检索可限定在子树内。会话提交后可抽取记忆为可检查的 Markdown，VikingBot 可将素材编译为 wiki/知识图谱。服务端以 AGPLv3 开源，另提供火山引擎托管 SaaS 与 BYOC 商业版；安装依赖 uv 与 Python 3.10+，需配置一个带嵌入模型和 VLM 的模型服务。

- 知识与记忆、技能统一为可浏览的虚拟文件系统（viking:// URI）
- L0 摘要/L1 概览/L2 全文三层上下文加载
- 支持 Claude Code、Codex、Cursor 等记忆插件一键安装，提供 Python/Go/TypeScript SDK 与 HTTP API
- 附带 LoCoMo 与 tau2-bench 基准评测脚本（./benchmark）

> L31: OpenViking is an open-source context database for AI agents — one filesystem for everything an agent knows: knowledge, m
> L45: - **One filesystem for knowledge, memory, and skills.** Resources hold documents and code; memories retain user preferen

## github/awesome-copilot（⭐40118，confidence: high）

**为 GitHub Copilot 用户提供社区贡献的自定义 agent 与配置集合**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

社区创建的资源集合，收录自定义 agents、instructions、skills、hooks、workflows 与 plugins，供 GitHub Copilot 用户扩展其工作方式。资源按 Agents（可集成 MCP 服务器）、Instructions（按文件模式自动应用）、Skills、Plugins（打包组合）、Cookbook（API 配方）等类别组织；配套网站提供全文检索、筛选与 Learning Hub 教程，并提供机器可读的 llms.txt。通过 Copilot CLI/VS Code 的 marketplace 安装插件。

- 收录 agents、instructions、skills、hooks、workflows、plugins 六类资源
- Agents 支持集成 MCP 服务器；Instructions 按文件模式自动应用
- 提供 copilot plugin install 命令行安装插件
- 网站提供全文检索与 Learning Hub 教程，并提供 llms.txt 供 AI agent 读取

> L4: A community-created collection of custom agents, instructions, skills, hooks, workflows, and plugins to supercharge your
> L23: |🤖 Agents|Specialized Copilot agents that integrate with MCP servers|All agents →|
> L31: ## Install a Plugin

## 2noise/ChatTTS（⭐39913，confidence: high）

**面向对话场景的文本转语音生成模型，支持中英文**

`ai_role=ai-native · license_risk=dual · deploy=library · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

ChatTTS 是面向 LLM 助手等对话场景的文本转语音模型，支持中英文输入。模型用 100,000+ 小时中英文音频训练，开源版本为无 SFT 的 40,000 小时预训练版，发布于 HuggingFace。支持多说话人、细粒度韵律控制（笑声、停顿、插入语），可控制 token 级标签 [laugh]、[uv_break]、[lbreak]。代码采用 AGPLv3+ 许可，模型采用 CC BY-NC 4.0 许可，仅限学术用途，禁止商用。训练中添加高频噪声并压缩音质以限制滥用。

- 面向对话任务优化的 TTS，支持多说话人交互
- 细粒度韵律控制：笑声、停顿、插入语
- 40,000 小时中英文预训练模型
- 提供 WebUI 与命令行两种推理入口

> L23: ChatTTS is a text-to-speech model designed specifically for dialogue scenarios such as LLM assistant.
> L41: - The main model is trained with Chinese and English audio data of 100,000+ hours.
> L94: #### Optional: Install vLLM (Linux only)

## mindsdb/mindshub（⭐39800，confidence: high）

**面向知识工作者的开源 Agent 工作台：可自选模型完成研究与开发任务**

`ai_role=ai-native · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=—`

开源 Agent 工作台，定位为完成知识工作与软件开发的统一工作空间，支持研究、分析、内容创作与软件开发。仓库为平台 superproject，聚合桌面/Web 应用、Agent 后端与数据引擎，可从源码构建运行。关键机制包括模型路由器（在多个闭源与开源模型间切换）、可互换的开源 agent harness（Anton 默认与 Hermes）、跨会话记忆、技能库、定时任务与制品发布。部署上支持本机、VPC、云端及隔离环境；Web 版免安装，macOS/Windows 提供桌面安装包，Linux 从源码构建。

- Model Router 在 Claude/GPT/Gemini 与 DeepSeek/Qwen/Kimi 间切换，无需逐家配 key
- 可互换的开源 agent harness：Anton（默认）与 Hermes，下拉切换
- 安全数据保险箱连接 BigQuery/Postgres/Gmail/Drive 等，凭据按连接隔离
- Agent 输出转为文档、仪表盘、应用并发布到在线 URL，支持定时任务与跨会话记忆

> L5: **MindsHub is an agent workspace for completing knowledge work and developing software, with open-source agent harnesses
> L22: MindsHub gives you the freedom to choose among models and providers instead of being locked into one ecosystem. Use its 
> L49: - **Model Router.** Switch between frontier models (Claude, GPT, Gemini) and open models (DeepSeek, Qwen, Kimi) without 

## The-Vibe-Company/quivr（⭐39597，confidence: high）

**开源内容流搜索引擎：将持续内容转为可搜索与监控**

`ai_role=ai-enhanced · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=idea`

以 Go 编写的单二进制引擎（api/worker/migrate 命令），将持续输入的内容流持久化摄入并提供词汇、语义与混合检索，支持保存的查询、订阅与告警（关键词、描述式、本地语义三类），告警通过签名 webhook 投递。核心保持通用，连接器、规范化、增强、检索与投递均为插件能力。数据规范存储于 PostgreSQL 与 S3，搜索索引为可重建投影。当前处于评估阶段，API 为 v0，README 明确不建议用于生产。

- 持久化与幂等摄入：写入提交确认、幂等键、不可变版本与更正/撤回机制
- 词汇、语义与混合检索，每次命中从规范存储回读并重新鉴权
- 三类告警插件：布尔关键词、外部分类器描述式、基于本地向量的语义告警
- 索引可从持久化工件重建，签名 webhook 投递与重试

> L5: **An open-source engine that turns continuous content streams into search and monitoring.**
> L49: |Lexical and vector search|Weaviate|
> L50: |Embeddings|Local TEI serving pinned `multilingual-e5-small` (384 dimensions)|

## deepseek-ai/awesome-deepseek-integration（⭐39399，confidence: high）

**将 DeepSeek API 接入常用软件的项目清单**

`ai_role=ai-ecosystem · license_risk=viral · deploy=library · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

由 deepseek-ai 组织维护的聚合清单，收录将 DeepSeek API 集成到各类软件的项目条目，按应用、客户端库等类别组织。条目涵盖桌面/移动端聊天客户端、翻译与 OCR 工具、笔记与知识库软件、浏览器、RPA 客服、Zotero 插件，以及 PHP/Go/Swift 等 API 客户端库和 Laravel 封装。提供英语、简体中文、繁体中文、日语、西班牙语多个语言版本。清单本身不含安装步骤，各条目链接至各自仓库。

- 收录数十个接入 DeepSeek API 的应用与工具条目
- 包含 PHP、Go、Swift 语言的 DeepSeek API 客户端库条目
- 提供英语、简体中文、繁体中文、日语、西班牙语版本

> L3: # Awesome DeepSeek Integrations Awesome
> L5: Integrate the DeepSeek API into popular softwares. Access DeepSeek Open Platform to get an API key.
> L11: ## Table of Contents

## bytedance/UI-TARS-desktop（⭐39305，confidence: high）

**开发者的多模态 GUI Agent 栈：用自然语言操作电脑与浏览器**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=research`

包含两个子项目：Agent TARS 是通用多模态 AI Agent 栈，提供 CLI 与 Web UI，通过多模态 LLM 与 MCP 工具集成，在终端、计算机、浏览器中执行类人任务流程；UI-TARS Desktop 是基于 UI-TARS 模型的桌面应用，提供本地/远程计算机与浏览器操作器，支持截图视觉识别、精确鼠标键盘控制，声称处理全在本地完成。面向使用自然语言驱动 GUI 自动化的开发者与用户，Apache 2.0 协议开源。

- Agent TARS CLI 支持 headful Web UI 与 headless 服务器两种执行模式
- 混合浏览器 Agent：GUI Agent、DOM 或混合策略控制浏览器
- 内核基于 MCP 构建，支持挂载 MCP Server 连接真实工具
- UI-TARS Desktop 支持本地与远程计算机/浏览器操作器，跨平台（Windows/macOS/Browser）

> L7:  TARS \* is a Multimodal AI Agent stack, currently shipping two projects: Agent TARS and UI-TARS-desktop:
> L16:  Agent TARS is a general multimodal AI Agent stack, it brings the power of GUI Agent and Vision into your terminal, comp
> L21:  UI-TARS Desktop is a desktop application that provides a native GUI Agent based on the UI-TARS model.

## VectifyAI/PageIndex（⭐39237，confidence: high）

**面向长专业文档 RAG 的树状索引检索引擎，无需向量库**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

PageIndex 用层次化树索引替代向量索引：索引阶段从文档版式提取树结构并由基础模型摘要精炼，检索阶段由 LLM 在树上推理式搜索定位相关章节，不需要向量数据库与分块。以 pip 包提供 SDK，支持本地模式（本地索引/检索/对话，用自有 LLM key）与 PageIndex Cloud（托管解析、OCR、存储）两种形态；提供 OpenAI Agents SDK、Claude Agent SDK 集成路径。开源版仅处理文本型 PDF；扫描件与图像文档需走云服务。

- 树状索引 + LLM 推理检索，无向量库、无分块
- SDK 本地模式：本机索引/检索/对话，用自有 LLM key
- 可接入 OpenAI Agents SDK / Claude Agent SDK 等 agent 框架
- 本地索引成本与耗时的基准数据（约 $0.001/页，9–1,098 页文档 13 秒–4.5 分钟）

> L7: # PageIndex: Vectorless, Reasoning-based RAG
> L30: 1. **Index**: generate a **tree-structure index** for each document
> L76: Drop PageIndex tools into the OpenAI Agents SDK, the Claude Agent SDK, or any other framework.

## lyogavin/airllm（⭐39132，confidence: high）

**让单张 4GB 显卡运行超大 LLM 的推理库**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=—`

Python 推理库，通过每次仅在 GPU 上保留一层解码层、逐层从磁盘流式加载的方式降低显存占用，README 称可在 4GB 显存上运行 70B 模型，无需量化、蒸馏或剪枝；v3.0 起支持 FP8，并提供 block-wise 量化压缩（宣称最高 3x 推理加速）。经 pip 安装，通过 AutoModel 传入 Hugging Face 模型 ID 或本地路径使用；推理前会将原模型分层切分保存，需要充足磁盘空间。支持 Apple Silicon 上的 MacOS，并提供小显存 LoRA 微调脚本。

- 逐层流式加载，使显存需求取决于单层大小而非模型总大小
- 支持 4bit/8bit block-wise 量化压缩（模型加载体积减小）
- 通过 AutoModel 一行代码加载多种开源 LLM
- 提供小显存 LoRA 训练（冻结权重逐层流式、仅适配器驻留 GPU）

> L9: **AirLLM** dramatically reduces inference memory usage, letting 70B large language models run on a single 4GB GPU card —
> L77: pip install airllm
> L187: The trick: AirLLM only ever keeps **one layer on the GPU at a time**, so the VRAM you need depends on the model's layer 

## google/langextract（⭐38965，confidence: high）

**用 LLM 从非结构化文本提取结构化信息并溯源的 Python 库**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

LangExtract 是一个 Python 库：按用户自定义指令和 few-shot 示例，用 LLM 从临床笔记、报告等非结构化文本中提取结构化信息。核心机制包括：分块与并行处理长文档、多次抽取提高召回、将每个抽取值锚定回原文精确字符区间，并可生成自包含的交互式 HTML 可视化文件。模型侧支持 Gemini 系列、OpenAI（可选依赖）、经内置 Ollama 接口的本地模型，并提供插件系统接入自定义 provider。云模型需配置 API key；本地模型无需 key。

- 抽取值精确锚定到源文本字符区间，支持可视化高亮核验
- 分块+并行+多次抽取策略处理长文档
- 内置 Ollama 支持本地推理，无需 API key
- 轻量插件系统注册自定义模型 provider

> L17: LangExtract is a Python library that uses LLMs to extract structured information from unstructured text documents based 
> L30: 5. **Flexible LLM Support:** Supports your preferred models, from cloud-based LLMs like the Google Gemini family to loca

## google-research/google-research（⭐38927，confidence: mid）

**Google Research 开源研究代码汇总仓库**

`ai_role=ai-ecosystem · license_risk=dual · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

该仓库集中存放 Google Research 发布的研究代码，内容按子目录划分为多个独立项目，覆盖主题标签所列的 AI 与机器学习研究方向。仓库体量较大，README 建议仅下载感兴趣的子目录（可通过 github.dev 编辑器下载），或以浅克隆方式获取源码。数据集采用 CC BY 4.0 许可，源代码采用 Apache 2.0 许可，仓库声明非 Google 官方产品。

- 集中托管 Google Research 发布的多个研究项目代码
- 数据集采用 CC BY 4.0，源代码采用 Apache 2.0 双许可结构
- 支持通过 github.dev 编辑器按子目录下载
- 提供浅克隆命令以减小下载体积

> L3: This repository contains code released by
> L12: Because the repo is large, we recommend you download only the subdirectory of

## naptha/tesseract.js（⭐38767，confidence: high）

**JS 库：浏览器/Node 从图片识别 100+ 语言文字**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

Tesseract.js 是 JavaScript OCR 库，通过封装 Tesseract 的 WebAssembly 移植版，在浏览器（webpack/ESM/script 标签+CDN）和 Node.js 中从图片提取文字。支持图片识别与视频实时识别示例，v4 起提供旋转预处理与并行处理（schedulers）。项目范围明确：不修改 Tesseract 核心识别模型、不支持 PDF；需 PDF 提取或精度改进的项目被指引至 Scribe.js。npm/yarn 或 CDN 安装，v7 需 Node.js v16+。

- 支持 100+ 语言图片文字识别
- 浏览器与 Node.js 双端运行（WebAssembly 封装）
- 旋转/灰度/二值化预处理选项与并行调度器
- 多图识别的 worker 复用模式

> L17: Tesseract.js is a javascript library that gets words in almost any language out of images. (Demo)
> L27: Tesseract.js works in the browser using webpack, esm, or plain script tags with a CDN and on the server with Node.js.
> L62: Tesseract.js aims to bring the Tesseract OCR engine (a separate project) to the browser and Node.js, and works by wrappi

## chatchat-space/Langchain-Chatchat（⭐38694，confidence: high）

**给开发者的可离线部署本地知识库 RAG 与 Agent 应用**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

基于 Langchain 框架构建的本地知识库问答与 Agent 应用项目，原名为 Langchain-ChatGLM。支持接入 ChatGLM、Qwen、Llama 等语言模型，通过 Xinference、Ollama、LocalAI、FastChat 等模型部署框架加载本地模型，也可接入 OpenAI、Azure、Anthropic 等在线 API。提供知识库对话、文件对话、数据库对话、搜索引擎对话、文生图、多模态图片对话等功能，底层支持 BM25+KNN 等多种检索方式。以 Python 库（pip）形式安装，或通过 Docker 部署；不涉及模型微调与训练。

- 支持 Xinference、Ollama、LocalAI、FastChat 等本地模型部署框架接入
- 支持 BM25+KNN 等多种检索方式与本地知识库管理
- 以 Python 库形式安装（pip install langchain-chatchat），提供 Docker 镜像
- Agent 与工具调用，支持多模态图片对话与文生图

> L11: 基于 ChatGLM 等大语言模型与 Langchain 等应用框架实现，开源、可离线部署的 RAG 与 Agent 应用项目。
> L29: ✅ 本项目支持市面上主流的开源 LLM、 Embedding 模型与向量数据库，可实现全部使用**开源**模型**离线私有部署**。与此同时，本项目也支持
> L122: 从 0.3.0 版本起，Langchain-Chatchat 提供以 Python 库形式的安装方式，具体安装请执行：

## anthropics/prompt-eng-interactive-tutorial（⭐38615，confidence: high）

**面向开发者的 Claude 提示词工程交互式教程**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

Anthropic 官方的提示词工程交互式课程，共 9 章（初级到高级）加附录，每章配练习与答案，按章节顺序学习。每节课末尾提供 Example Playground，可修改提示词并观察 Claude 响应变化；示例使用 Claude 3 Haiku 模型，另提供基于 Claude for Sheets 扩展的 Google Sheets 版本。内容覆盖提示词结构、消除幻觉、思维链、示例使用及法律/金融/编码等行业用例。

- 9 章分级课程，每章配练习与答案
- 每课附带 Example Playground 供实验
- 行业用例章节含法律、金融、编码复杂提示练习
- 附录覆盖提示链、工具使用、检索

> L1: # Welcome to Anthropic's Prompt Engineering Interactive Tutorial
> L19: Note: This tutorial uses our smallest, fastest, and cheapest model, Claude 3 Haiku. Anthropic has two other models, Clau

## linshenkx/prompt-optimizer（⭐38350，confidence: high）

**提示词优化工具：编写、测试与评估更好的 AI 提示词**

`ai_role=ai-ecosystem · license_risk=none · deploy=desktop · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

面向使用 AI 模型的用户，提供提示词的优化、测试、评估与收藏管理。支持系统提示词与用户提示词双模式优化、多轮迭代改进、单结果与对比评估、上下文变量与多轮对话测试，并提供文本生成图像提示词的优化。提供网页版、桌面应用、Chrome 扩展与 Docker 四种使用方式，纯客户端处理，数据直接与模型服务商交互；通过 MCP 协议可接入 Claude Desktop 等 AI 应用。使用前需自行配置模型 API key。

- 一键优化与多轮迭代改进，支持系统/用户提示词双模式
- 多模型接入：OpenAI、Gemini、DeepSeek、Grok、智谱、SiliconFlow、MiniMax 等
- 文本生成图像（T2I/I2I/多图）提示词优化与模型参数配置
- MCP 协议支持，可集成 Claude Desktop 等 MCP 兼容应用

> L21: Prompt Optimizer is a powerful AI prompt optimization tool that helps you write better AI prompts and improve the qualit
> L44: - 🤖 **Multi-model Integration**: Support for mainstream AI models including OpenAI, Gemini, DeepSeek, Grok, Zhipu AI, Si
> L52: - 🧩 **MCP Protocol Support**: Supports Model Context Protocol (MCP), enabling integration with MCP-compatible AI applica

## patchy631/ai-engineering-hub（⭐38348，confidence: high）

**面向 AI 工程学习者的 LLM/RAG/Agent 教程项目合集（93+）**

`ai_role=ai-knowledge · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

按难度分层的 AI 工程教程仓库，收录 93+ 个可运行项目，覆盖 OCR、聊天界面、基础与高级 RAG、多模态、语音、MCP、模型评测、微调与生产系统等类别，每个项目附实现代码与教程。面向初学者、从业者与研究者，提供从入门路线图到高级微调的学习路径，并接受社区通过 fork 分支与 PR 方式贡献。仓库采用 MIT 许可证。

- 93+ 个项目按初/中/高难度三级分类
- 覆盖 RAG、Agent、MCP、多模态、语音、微调等方向
- 提供 AI Engineering Roadmap 学习路径
- MIT 许可证并接受社区贡献

> L14: - **93+ Production-Ready Projects** across all skill levels
> L15: - In-depth tutorials on **LLMs, RAG, Agents, and more**
> L16: - Real-world **AI agent** applications

## microsoft/playwright-mcp（⭐38278，confidence: mid）

**给 LLM 提供浏览器自动化能力的 MCP 服务器**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

基于 Playwright 的 Model Context Protocol 服务器，使 LLM 通过结构化无障碍快照与网页交互，无需截图或视觉模型。README 逐项给出 Amp、Claude Code、Codex、Cursor、Gemini CLI、Goose、VS Code、Windsurf 等约 20 种 MCP 客户端的接入配置。要求 Node.js 18 及以上，通过 npx 运行 @playwright/mcp。提供约 30 个配置参数，涵盖浏览器选择、CDP 连接、代码生成、移动设备模拟、无头模式、文件访问限制等。另提及面向编码代理的 CLI+SKILLS 替代路径。

- 基于无障碍树的结构化交互，不依赖视觉模型
- 提供 20 余种 MCP 客户端的逐步接入配置
- 约 30 个配置参数：CDP 端点、设备模拟、headless、文件访问控制等
- 支持 vision/pdf/devtools 附加能力（--caps）

> L3: A Model Context Protocol (MCP) server that provides browser automation capabilities using Playwright. This server enable
> L21: - VS Code, Cursor, Windsurf, Claude Desktop, Goose, Grok, Junie or any other MCP client
> L280: Playwright MCP server supports following arguments. They can be provided in the JSON configuration above, as a part of t

## CopilotKit/CopilotKit（⭐38077，confidence: high）

**给开发者提供 agent 前端接入栈与 Generative UI**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

面向构建 agent 应用的前端 SDK：将聊天 UI、Generative UI、共享状态与 human-in-the-loop 工作流接入 React、Angular、Vue、React Native 等框架，并通过 Channels SDK 将同一 agent 发布到 Slack、Microsoft Teams、Discord、WhatsApp、Telegram 等渠道。底层的 agent 前端通信由其维护的 AG-UI Protocol 承担，提供 useAgent hook 编程式控制 agent 连接。安装走 npm/npx 脚手架命令，另有可选的 CopilotKit Intelligence 托管或自托管平台（持久会话、用户记忆、分析）。MIT 许可。

- 支持 React/Angular/Vue/React Native 前端框架接入
- 提供 Generative UI、共享状态与 human-in-the-loop 机制
- Channels SDK 支持发布到 Slack/Teams/Discord/WhatsApp/Telegram
- 维护 AG-UI Protocol 并提供 useAgent hook

> L10: Build **agent-native applications** — on any framework, on any surface.
> L38: CopilotKit is a best-in-class SDK for building full-stack agentic applications, Generative UI, and chat applications.
> L132: Your agent logic stays the same — AG-UI handles the wire protocol, CopilotKit handles the UI layer for each framework an

## AlexsJones/llmfit（⭐38019，confidence: high）

**检测本机硬件并推荐可流畅运行的本地 LLM 的命令行工具**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=—`

Rust 编写的终端工具：自动检测 CPU、内存、GPU/VRAM 与加速器配置，对模型目录中的模型按内存占用、预估速度、质量与上下文四维打分，推荐适配当前硬件的量化版本。支持 GGUF/AWQ/GPTQ/EXL2 量化格式、多 GPU 与 MoE 架构、硬件模拟，提供交互式 TUI、经典 CLI、Web UI 与 REST API。社区基准数据可通过 PR 回传，合并后同硬件用户可看到实测数值。安装途径覆盖 Scoop/Homebrew/MacPorts/安装脚本/uv/pip/预编译二进制/Docker/源码编译。

- 硬件自动检测：CPU、内存、GPU/VRAM、统一内存架构（CUDA/Apple Silicon/ROCm/OneAPI）
- 兼容性引擎：分析参数量、上下文长度与量化格式，投影内存占用与 tok/s
- TUI/CLI/Web UI/REST API 多种形态，支持脚本与 agent 消费 JSON 输出
- 社区基准共享：实测 tok/s 经 PR 合并后替代估算值

> L16: Find out which open-source Large Language Models (LLMs) your hardware can comfortably run. `llmfit` inspects your CPU, s
> L25: - **Model Compatibility Engine**: Analyzes model parameter counts, context lengths, and quantization formats (GGUF, AWQ,
> L27: - **REST API Endpoint**: Exposes standard HTTP JSON endpoints (`/api/v1/system`, `/api/v1/models`) for integration into 

## fengdu78/Coursera-ML-AndrewNg-Notes（⭐37974，confidence: high）

**机器学习入门者的吴恩达课程中文学习笔记**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

整理斯坦福 2014 年吴恩达机器学习课程的中文笔记，覆盖 10 周 18 节内容：监督学习、无监督学习、SVM、神经网络、推荐系统等。提供 markdown、word、html 三种笔记格式及 pdf 下载，随附课程原版 ppt 课件、中英文字幕（mp4 存百度云）、python 课程代码及 B 站课程视频链接。html 版公式已转为图片以便在线阅读。面向中文机器学习学习者。

- 笔记提供 word/markdown/html 三种格式及 pdf 下载
- 附课程原版 ppt 与中英文字幕
- 包含课程 python 代码
- html 在线版公式已转为图片

> L1: **斯坦福大学2014（吴恩达）机器学习教程中文笔记**
> L19: 本人2014年下半年开始翻译本课程字幕，并写了课程的中文笔记。笔记被下载了几万次，应该帮助了不少人，也有很多人一直在帮助我，现在我把笔记的**word**原稿和**markdown**原稿分享给大家。
> L21: **markdown**的笔记和课程中英文字幕我将放在**github**，希望大家能继续完善。为方便数学公式的在线显示，在线观看的是**html**文件，公式已经被转为图片，公式源码在**markdown**文件。

## Dokploy/dokploy（⭐37841，confidence: mid）

**自托管 PaaS：部署和管理应用与数据库**

`ai_role=ai-ecosystem · license_risk=none · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

免费、可自托管的平台即服务（PaaS），用于简化应用与数据库的部署管理。支持部署多种语言应用（Node.js、PHP、Python、Go、Ruby 等）及 MySQL、PostgreSQL、MongoDB、MariaDB、Redis 等数据库；基于 Docker Swarm 实现多节点集群，内置 Traefik 路由集成、数据库外部备份、一键部署开源模板、实时资源监控与日志指标推送（Grafana、Datadog 等），并提供 CLI 与 API 管理入口。在 VPS 上通过一行脚本安装，另有 Dokploy Cloud 托管选项。

- 部署多语言应用与管理 6 种数据库
- Docker Swarm 多节点伸缩与 Traefik 自动集成
- 日志与指标推送至 Grafana、Datadog、AWS CloudWatch 等多个平台
- CLI 与 API 管理途径，支持多服务器远程部署

> L2:  Dokploy - Open Source Alternative to Vercel, Heroku and Netlify.
> L10: Dokploy is a free, self-hostable Platform as a Service (PaaS) that simplifies the deployment and management of applicati
> L20: - **Multi Node**: Scale applications to multiple nodes using Docker Swarm to manage the cluster.

## khoj-ai/khoj（⭐37721，confidence: high）

**自托管的个人 AI 第二大脑：检索文档与网络、构建自定义 agent**

`ai_role=ai-native · license_risk=viral · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

Khoj 是一个可自托管的个人 AI 应用，支持接入本地或在线 LLM，从互联网和本地文档（PDF、Markdown、Notion、Word、org-mode 等）中检索并回答问题；可创建带有自定义知识、persona、聊天模型与工具的 agent，支持定时自动化研究与通知。可通过浏览器、Obsidian、Emacs、桌面、手机或 WhatsApp 访问，提供云端版本供免安装使用，另有面向企业的云/本地/混合部署形态。

- 支持 llama3、qwen、mistral、gpt、claude、gemini、deepseek 等本地或在线 LLM
- 读取 PDF、Markdown、Notion、Word、org-mode 等多种文档并做语义搜索
- 创建自定义知识、persona、模型与工具的 agent，支持自动化研究任务
- 支持自托管，也提供云端直接使用入口

> L28: Khoj is a personal AI app to extend your capabilities. It smoothly scales up from an on-device personal AI to a cloud-sc
> L30: - Chat with any local or online LLM (e.g llama3, qwen, gemma, mistral, gpt, claude, gemini, deepseek).
> L37: - Khoj is open-source, self-hostable. Always.

## ItzCrazyKns/Vane（⭐37366，confidence: high）

**自托管的 AI 答问搜索引擎，本地运行并带引用来源**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

Vane 是一个注重隐私的 AI 答问引擎，可完全运行在用户自己的硬件上。它通过 SearxNG 聚合多个搜索引擎结果（支持网页、讨论、学术论文来源），接入本地 LLM（Ollama、OpenAI 兼容服务器、Lemonade）或云服务商（OpenAI、Claude、Groq、Gemini），生成带引用来源的回答。功能包括文件上传问答（PDF/文本/图片）、图片与视频搜索、域名限定搜索、天气/股价等小组件、搜索历史本地保存，并提供 API 供开发者集成。Docker 镜像内置 SearxNG，也支持 npm 从源码运行。

- 基于 SearxNG 的网页/讨论/学术搜索，回答带引用来源
- 支持本地 LLM（Ollama）与多家云服务商，可混合搭配模型
- 文件上传问答：PDF、文本、图片
- 提供 API 与浏览器搜索引擎快捷方式接入

> L11: Vane is a **privacy-focused AI answering engine** that runs entirely on your own hardware. It combines knowledge from th
> L19: 🤖 **Support for all major AI providers** - Use local LLMs through Ollama or connect to OpenAI, Anthropic Claude, Google 
> L27: 🔍 **Web search powered by SearxNG** - Access multiple search engines while keeping your identity private. Support for Ta

## google-ai-edge/mediapipe（⭐37305，confidence: high）

**面向开发者的跨端设备机器学习方案库**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=idea`

MediaPipe 是 Google 维护的开源项目，提供面向移动（Android/iOS）、Web、桌面、边缘设备与 IoT 的端侧机器学习库与工具。包含 MediaPipe Tasks 跨平台 API、预训练模型、Model Maker 模型定制工具与 Studio 浏览器端可视化评估工具；底层 Framework 以 Packets/Graphs/Calculators 概念构建端侧 ML 管线。README 已迁移至 developers.google.com 作为主文档站。Legacy Solutions 自 2023 年 3 月起终止支持，代码与二进制按原样提供。

- MediaPipe Tasks 提供跨平台部署 API 与库
- 提供各方案预训练、可直接运行的模型
- Model Maker 支持用自有数据定制模型
- Framework 以图（Graphs）与计算器（Calculators）构建端侧管线

> L15: **On-device machine learning for everyone**
> L40: MediaPipe Solutions provides a suite of libraries and tools for you to quickly
> L51: * **MediaPipe Tasks**: Cross-platform APIs and libraries for deploying

## ashishpatel26/500-AI-Machine-learning-Deep-learning-Computer-vision-NLP-Projects-with-code（⭐37303，confidence: high）

**为 AI/ML 学习者提供 500+ 带代码项目的清单**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

以 Markdown 表格形式收录的 AI/机器学习/深度学习/计算机视觉/NLP 项目链接清单，条目按序号组织，覆盖时间序列预测、情感分析、聊天机器人、推荐系统、OpenCV、GAN、AutoML、数据集等方向，部分条目为论文与代码合集或学习资源合集。作者声明清单持续更新并接受 pull request 贡献，链接经过测试。README 本身不含安装与运行说明，各项目代码需跳转对应链接获取。

- 500+ 条带代码的 AI/ML/DL/CV/NLP 项目链接
- 覆盖 NLP、计算机视觉、时间序列、推荐系统、AutoML 等多方向
- 包含 Kaggle 项目合集与论文带代码合集
- 作者声明持续更新并接受社区贡献

> L1: ## 500 + 𝗔𝗿𝘁𝗶𝗳𝗶𝗰𝗶𝗮𝗹 𝗜𝗻𝘁𝗲𝗹𝗹𝗶𝗴𝗲𝗻𝗰𝗲 𝗣𝗿𝗼𝗷𝗲𝗰𝘁 𝗟𝗶𝘀𝘁 𝘄𝗶𝘁𝗵 𝗰𝗼𝗱𝗲
> L7: ***This list is continuously updated.*** - You can take pull requests and contribute. All Links are tested and working f
> L9: |Sr No|Name|Link|

## sgl-project/sglang（⭐37249，confidence: high）

**面向开发者的大模型与多模态模型推理服务框架**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

开源推理框架，支持大语言模型、视觉语言模型与扩散模型的部署服务，面向 agentic 工作负载、大规模服务与 RL rollout 场景进行优化。仓库内置 SGLang Diffusion 图像与视频生成引擎，并通过 SGLang Omni 提供语音模型的 TTS/ASR 服务。通过 Docker 镜像或 uv/pip 从 PyPI 安装；开发环境提供 dev 镜像与可编辑安装方式。项目由 LMSYS 托管，覆盖 GPU、TPU、NPU、CPU 及 Apple Silicon 多类平台。

- 支持大语言、视觉语言与扩散模型的服务
- 内置 SGLang Diffusion 图像与视频生成引擎
- 覆盖 NVIDIA/AMD/TPU/Intel/Apple Silicon/昇腾/摩尔线程等硬件平台
- 生态包含 SpecForge 投机解码与多个 RL 训练框架集成

> L15: SGLang is an open-source inference framework for large language, vision-language, and diffusion models, optimized for ag
> L40: SGLang supports a wide range of GPUs, TPUs, NPUs, CPUs, and Apple Silicon platforms.

## huggingface/pytorch-image-models（⭐37225，confidence: high）

**为 PyTorch 开发者提供图像编码器/骨干网络集合与预训练权重**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=medium · maturity=—`

timm 是一个 PyTorch 图像模型库，收录多种视觉骨干网络（ResNet、EfficientNet、ViT、Swin Transformer、ConvNeXt 等）的定义与预训练权重，并提供训练、评估、推理、导出脚本（train.py / validate.py / inference.py）以及 ONNX 导出支持。面向计算机视觉研究与工程开发者。近期更新包括 sweep.py 超参网格/随机搜索、多标签分类任务（BCE 训练与 mAP/F1 评估）、WSD 学习率调度器，以及一批新模型权重的接入。

- 提供多种图像分类骨干网络的模型定义与预训练权重
- 附带 train.py、validate.py、inference.py、export 脚本及新的 sweep.py 超参搜索
- 支持多标签分类任务与 mAP/F1 评估指标
- 支持 ONNX 导出与 torch.compile

> L1: # PyTorch Image Models
> L8: * Hyperparameter sweeps via a new `sweep.py`: grid / random search over any `train.py` argument, one effective `--config
> L39:  * Add `--task multilabel` to `train.py` / `validate.py`, trained with BCE (`MultiLabelClassificationTask`). See the

## 1Panel-dev/1Panel（⭐37193，confidence: high）

**面向自托管者的 Linux 服务器管理面板与轻量 AI 管理平台**

`ai_role=ai-ecosystem · license_risk=dual · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

通过 Web 界面提供 Linux 服务器一站式管理：主机监控、文件/数据库/容器管理、网站一键部署（与 WordPress、Halo 集成）、内置 165+ 开源应用的应用商店一键安装升级、基于容器的部署方式及 WAF 与日志审计等安全功能、一键备份恢复并对接多种云存储。AI 方面提供从裸金属到 agent 的统一管理平台，集成 AI 网关与 Skills Hub，支持集中管理 agent 与模型。通过官方脚本一行命令安装，GPL v3 开源，另有按功能分层收费的 Pro/Ent 版本。

- Web 界面管理主机、文件、数据库与容器
- 内置应用商店提供 165+ 应用一键安装与升级
- AI 管理：AI 网关、Skills Hub 与 agent/模型集中管理
- 一键备份恢复并集成多种云存储

> L31: 1Panel is a modern, open-source Linux server management panel and a lightweight AI management platform. Through an intui
> L32: - **AI Management**: Offers a unified management platform from bare metal to agents (Metal-to-Agent). It integrates an A
> L55: bash -c "$(curl -sSL https://resource.1panel.pro/v2/quick_start.sh)"

## songquanpeng/one-api（⭐37190，confidence: high）

**开发者的 LLM API 网关：统一多家模型接口并管理分发 key**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

以 Go 编写的 LLM API 管理与分发系统，将数十家模型服务商的接口统一为 OpenAI API 格式对外提供。核心机制包括渠道管理、负载均衡、失败重试、令牌（额度、过期时间、IP 范围、模型范围）与兑换码管理、多机部署主从节点、按分组的倍率计费。默认 SQLite 存储，可通过环境变量切换 MySQL/PostgreSQL 并配置 Redis 缓存。提供单可执行文件、Docker 镜像及宝塔、Sealos、Zeabur、Render 等部署途径。README 提醒需遵循 OpenAI 使用条款及中国区备案要求。

- 支持 30 余家模型服务商，统一以 OpenAI API 格式访问
- 令牌与兑换码管理：额度、过期时间、IP 范围、模型访问控制
- 多渠道负载均衡与失败自动重试，支持多机主从部署
- 单可执行文件 + Docker 镜像，支持 SQLite/MySQL/PostgreSQL

> L7: _✨ 通过标准的 OpenAI API 格式访问所有的大模型，开箱即用 ✨_
> L57: 1. 支持多种大模型：
> L89: 6. 支持**令牌管理**，设置令牌的过期时间、额度、允许的 IP 范围以及允许的模型访问。

## JCodesMore/ai-website-cloner-template（⭐36924，confidence: high）

**给 AI 编码代理的模板：一条命令把网站复刻为 Next.js 应用**

`ai_role=ai-enhanced · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

一个 Next.js 模板项目，核心是一个可移植的 Agent Skill（/clone-website）：用户给 AI 编码代理一个 URL，代理按 Map→Observe→Build→Compare 四步将目标网站复刻为可编辑的 Next.js 应用，产出路由映射、运行说明与对比截图。要求 Node.js 24+ 与具备浏览器访问能力的 AI 编码代理；Framer 页面与动效站点有专门的检查指引。README 明确声明不用于钓鱼、冒充或违反目标站点服务条款的场景。

- /clone-website 技能按四步流程复刻网站为 Next.js 应用
- 同一技能文件供 Codex、Cursor、OpenCode 直接读取，Claude Code 经命令桥接使用
- 复刻产出含路由映射、运行说明、对比截图与差距清单
- 对 Framer 页面与动效站点提供专门检查指引

> L5: Give your AI coding agent a URL and watch it recreate the website as a clean Next.js app.
> L57: |Claude Code|**Recommended** — Opus 5.5|
> L125: The project keeps one portable Agent Skill at `.agents/skills/clone-website/`. Codex, Cursor, and OpenCode read it direc

## babysor/MockingBird（⭐36888，confidence: high）

**给需要中文语音克隆的用户：5秒音频实时合成任意语音**

`ai_role=ai-native · license_risk=none · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=research`

基于 SV2TTS 的中文语音克隆工具箱，由 encoder、synthesizer、vocoder 三部分组成，支持用多套中文数据集（aidatatang_200zh、magicdata、aishell3 等）训练或使用社区共享的预训练模型。提供 Web 服务（web.py）、图形工具箱（PyQt5）与命令行三种使用方式，可复用预训练 encoder/vocoder 仅重训 synthesizer。README 注明作者已不再积极更新，转向商业化项目 noiz.ai；demo_cli 在中文预训练模型下不可用，需额外 synthesizer 模型。

- 支持中文普通话，可在多套中文数据集上训练
- 提供 Web 服务、桌面工具箱与命令行三种入口
- 可复用预训练 encoder/vocoder，仅训练新 synthesizer
- 支持 Windows、Linux 及 M1 macOS（x86 转译方案）

> L11: 🌍 **Chinese** supported mandarin and tested with multiple datasets: aidatatang_200zh, magicdata, aishell3, data_aishell,
> L166: |**1806.04558**|**SV2TTS**|**Transfer Learning from Speaker Verification to Multispeaker Text-To-Speech Synthesis**|This
> L19: 🌍 **Webserver Ready** to serve your result with remote calling

## blakeblackshear/frigate（⭐36694，confidence: high）

**本地实时目标检测的 IP 摄像头 NVR**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

面向 Home Assistant 的完全本地化 NVR，使用 OpenCV 与 TensorFlow 对 IP 摄像头画面做实时目标检测，无需将视频上传云端。通过自定义组件与 Home Assistant 集成，以低开销运动检测决定何时何地运行目标检测，经 MQTT 与其他系统通信。支持基于检测对象的录像保留策略、24/7 录像、RTSP 转流及 WebRTC/MSE 低延迟实时查看。文档注明建议使用 GPU 或 AI 加速器以获得更好效果。

- 本地运行 TensorFlow 实时目标检测
- 与 Home Assistant 通过自定义组件紧密集成
- MQTT 通信，便于接入其他系统
- RTSP 转流与 WebRTC/MSE 低延迟实时查看

> L13: A complete and local NVR designed for Home Assistant with AI object detection. Uses OpenCV and Tensorflow to perform rea
> L15: Use of a GPU or AI accelerator is highly recommended. AI accelerators will outperform even the best CPUs with very littl

## microsoft/graphrag（⭐36364，confidence: high）

**面向私有数据的图谱化 RAG 数据管线与研究系统**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

微软研究院的 GraphRAG 项目：一条数据管线与转换工具集，用 LLM 从非结构化文本中抽取结构化数据，构建知识图谱作为问答的定向上下文。提供 CLI 快速上手、索引流程与提示词调优指南，经 PyPI 分发。README 标注为处于维护模式的科研项目，不再接受新 PR 或新功能，仅做缺陷修复与依赖更新；并提示索引操作成本可能较高，建议从小规模开始。

- 用 LLM 从非结构化文本抽取结构化数据的数据管线
- 以知识图谱为问答构建定向上下文
- 提供 CLI 快速上手与大版本迁移笔记本
- 提供提示词调优指南与负责任 AI FAQ

> L25: The GraphRAG project is a data pipeline and transformation suite that is designed to extract meaningful, structured data
> L35: This repository presents a methodology for using knowledge graph memory structures to enhance LLM outputs. Please note t
> L4: > GraphRAG is a research project that explores the functional use of graphs to form a targeted context for question answ

## DayuanJiang/next-ai-draw-io（⭐36303，confidence: high）

**通过对话生成与编辑 draw.io 图表的 AI 工具**

`ai_role=ai-native · license_risk=permissive · deploy=desktop · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

以自然语言描述生成 draw.io 图表的工具，支持手动编辑、选中局部让 AI 修改、每次 AI 变更生成可对比/恢复/撤销的版本卡片，导出 .drawio/.png/.svg。内置 AWS/Azure/GCP/Kubernetes 图标库，可上传截图、草图、PDF、Markdown 等由 AI 重绘为图表。提供 Web 应用、Windows/macOS/Linux 桌面应用及面向 Claude Code、Cursor、VS Code 等 agent 的 MCP 服务器；支持 25 家模型服务商，API key 存于本地浏览器。自托管需配置服务商与 API key。

- 对话生成与局部选中编辑，每次 AI 变更为可对比/恢复的版本卡片
- MCP 服务器形式接入 Claude Code、Cursor、VS Code 等客户端
- 内置 AWS、Azure、GCP、Kubernetes 图标库与连接线流动动画
- 支持 25 家模型服务商及 OpenAI 兼容自定义 URL，key 保留在本地

> L3: **Draw and edit draw.io diagrams by chatting with an AI.**
> L18: Available as a web app, a desktop app for Windows, macOS and Linux, and an MCP server for AI agents such as Claude Code,
> L150: 25 providers are supported: AWS Bedrock (default), OpenAI, Anthropic, Google AI, Google Vertex AI, Azure OpenAI, Ollama,

## continuedev/continue（⭐36232，confidence: high）

**面向开发者的开源编码代理：CLI、VS Code、JetBrains 三形态**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Continue 是一个编码代理，以 CLI、VS Code 扩展和 JetBrains 插件三种形态提供。仓库现处于只读状态、不再积极维护，团队发布了最终的 2.0.0 版本，该版本移除了匿名遥测与身份认证并修复了缺陷。各形态分发渠道：VS Code 扩展在 Marketplace 与 OpenVSX，CLI 通过 npm，JetBrains 插件通过 GitHub Releases；官方推荐改用 Continue CLI 而非 JetBrains 插件。配置与定制方法见 Continue Docs。

- 以 CLI、VS Code 扩展、JetBrains 插件三种形态分发
- 最终 2.0.0 版本移除匿名遥测与认证
- JetBrains 插件经 GitHub Releases 分发
- Apache 2.0 许可

> L3:  Pioneering open-source coding agent
> L11: Continue is a coding agent available as a CLI, VS Code extension, and JetBrains plugin.
> L9: > _Note: The `continuedev/continue` repository is no longer actively maintained and is read-only for all users._

## langfuse/langfuse（⭐35964，confidence: high）

**LLM 应用的开源追踪与评估平台：开发、监控、调试 AI 应用**

`ai_role=ai-native · license_risk=none · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

开源 LLM 工程平台，供团队协作开发、监控、评估和调试 AI 应用。核心机制包括：应用埋点摄入 trace 以跟踪 LLM 调用、检索、嵌入与 agent 动作；集中式 Prompt 管理与版本控制（服务端/客户端缓存）；支持 LLM-as-a-judge、代码评估器、用户反馈、人工标注等评估方式；数据集支持测试集与基准；LLM Playground 迭代提示词。可通过 Docker Compose、Kubernetes (Helm) 或 Terraform 自托管，也提供 Langfuse Cloud 托管版与 Python/JS-TS SDK。

- 可观测性：摄取 trace 跟踪 LLM 调用、检索、嵌入与 agent 动作
- Prompt 集中管理与版本控制，含服务端与客户端缓存
- 评估支持 LLM-as-a-judge、代码评估器、用户反馈、人工标注与自定义管线
- 提供 Python/JS-TS SDK、OpenAPI 规范与 Postman 集合

> L49: Langfuse is an **open source LLM engineering** platform. It helps teams collaboratively
> L62: - LLM Application Observability: Instrument your app and start ingesting traces to Langfuse, thereby tracking LLM calls 
> L74: ## 📦 Deploy Langfuse

## esengine/DeepSeek-Reasonix（⭐35829，confidence: high）

**开源终端/桌面编码 Agent：读写代码、跑命令与测试**

`ai_role=ai-native · license_risk=permissive · deploy=desktop · model_dep=locked-api · hardware=— · install_friction=low · maturity=idea`

Reasonix 是开源 AI 编码助手，程序运行在用户本地，模型由用户自行配置并直接付费。用户用自然语言描述任务，它在指定项目文件夹内读取代码、编辑文件、运行命令与测试，并展示每步操作；支持权限分级、plan 模式与按会话回合的文件回滚（仅覆盖其编辑工具改动的文件）。分发形态包括 Studio 桌面应用、终端 CLI/TUI、浏览器界面与 VS Code 等 ACP 编辑器扩展，四者为同一引擎。2.x 处于活跃开发，1.x 处于维护状态。

- DeepSeek 内置预设，任意 OpenAI 兼容端点经一条配置即可接入
- MCP 服务器提供工具/提示/资源，Extension Protocol 可拦截运行时事件
- CGO_ENABLED=0 单二进制静态分发，一条命令交叉编译六个目标
- 编辑工具改动的文件按会话回合可回滚，不触碰 git 历史

> L37:  An open-source coding agent for your terminal, desktop, browser and editor.
> L54: Reasonix is an open-source AI coding assistant. The program runs on your computer; the AI model is a service you configu
> L113: - **Multi-model & composable.** DeepSeek ships as a preset; any

## agentscope-ai/QwenPaw（⭐35802，confidence: high）

**可自托管部署的个人 AI 助手，多渠道接入**

`ai_role=ai-native · license_risk=permissive · deploy=desktop · model_dep=local-ok · hardware=— · install_friction=low · maturity=idea`

面向个人用户的 AI 助手，可部署在本地或云端。采用三层记忆机制（工作上下文、完整历史、基于 ReMe 的个人知识库），内置 QwenPaw-Flash 系列模型（2B–35B-A3B），也可接入 Ollama、LM Studio 或 14+ 云端模型服务。支持 DingTalk、Lark、WeChat、Discord、Telegram、iMessage、QQ 等多渠道接入，以及 Console、TUI、桌面应用访问。扩展能力包括 Skills、Plugin 市场、MCP 集成、多 Agent 并行与 ACP 协议编排。安全机制含沙箱、Tool Guard、File Guard、Skill Scanner 与访问策略。

- 三层记忆：工作上下文、全量历史、自演化个人知识库（ReMe）
- 内置 QwenPaw-Flash 模型，本地运行无需 API key；兼容 Ollama/LM Studio/14+ 云服务
- 多渠道接入：DingTalk/Lark/WeChat/Discord/Telegram/iMessage/QQ 单实例全覆盖
- Kernel 级沙箱、Tool Guard、Skill Scanner 等安全机制

> L26: Your personal AI assistant — deploy locally or in the cloud, extend with Skills & Plugins, connect across every channel.
> L31: |**Local or cloud, runs free**|QwenPaw-Flash models (2B / 4B / 9B / 35B-A3B / 27B) trained for agent tasks. Built-in Qwe
> L36: |**Reachable anywhere**|DingTalk, Lark, WeChat, Discord, Telegram, iMessage, QQ — one instance, all channels. Console, T

## can1357/oh-my-pi（⭐35753，confidence: mid）

**面向开发者的 IDE 级编码 agent CLI，60+ 模型接入**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

Stencil Labs 维护的 Pi 分叉，以 CLI/TUI 形式提供编码 agent：内置 31 个工具、14 个 LSP 操作、28 个 DAP 调试操作，Rust 核心约 8 万行。支持 60+ 模型提供方，接入 lldb/dlv/debugpy 等调试器，提供子代理 fan-out（隔离 worktree、schema 校验返回）、reviewer 模型逐轮监督、流中规则注入、/collab 会话共享、按内容哈希的编辑（hashline）与基于 git 的原子提交拆分。安装覆盖 curl 脚本、Homebrew、Bun、Nix、Windows PowerShell、mise。PR 接受采用 vouch 机制（当前暂停试用中）。

- 60+ 模型提供方、31 内置工具、14 LSP 操作、28 DAP 操作
- 持久 Python/Bun 执行内核可回调 agent 工具
- 子代理在隔离 worktree 并行，返回 schema 校验结果
- 通过 ACP 在 Zed 中驱动同一 agent，无需插件

> L3:  A coding agent with the IDE wired in.
> L19: **60+** providers · **31** built-in tools · **14** lsp ops · **28** dap ops · **~80k** lines of Rust core.
> L15:  Built by Stencil Labs · Fork of Pi by @mariozechner

## HKUDS/Vibe-Trading（⭐35694，confidence: mid）

**个人量化交易 Agent：回测、实盘与研究一站式**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=—`

由 HKUDS 开发的个人交易 Agent，以 Python 包（vibe-trading-ai）分发，通过 FastAPI 后端与 React 前端提供 Web 界面。功能覆盖策略回测（Sortino、Monte Carlo、walk-forward 等指标）、实盘运行调度（决策会话、每日用量预算）、研究工作流（因子计算、SEC 文件、证据溯源 grounding gate）以及多渠道接入（Email、Slack、Discord、飞书、WeChat、WebSocket）。支持 18 家券商连接器与多市场数据（A 股、美港股、加密货币等），v0.1.16 起数字需经工具证据校验。

- 回测引擎输出 Sortino、turnover、Monte Carlo p 值等结构化指标并以 CSV 佐证
- grounding gate 按数字角色（observed/derived/proposed/cited/count）校验模型输出与工具证据一致性
- 18 家券商连接器（含 KIS、Upbit、Toss Securities、Scalable Capital 等）与多市场数据源
- Email/Slack/Discord/飞书/WeChat/WebSocket 等多渠道接入及定时报告（PDF 支持 AES-256 加密）

> L5:  Vibe-Trading: Your Personal Trading Agent
> L33:  pip install vibe-trading-ai
> L79: - **2026-09-29** 🚀 **v0.1.16 released** (Release notes, `pip install -U vibe-trading-ai`): 492 commits and 116 merged pu

## p-e-w/heretic（⭐35609，confidence: high）

**自动去除语言模型审查（abliteration）的命令行工具**

`ai_role=ai-ecosystem · license_risk=viral · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

Heretic 是一个对 transformer 语言模型执行去审查（移除安全对齐）的工具，采用方向消融（abliteration）实现，并用 Optuna 的 TPE 参数优化器自动搜索消融参数，目标为同时最小化拒答数与与原模型的 KL 散度。支持多数稠密模型、部分多模态、MoE 及混合架构，纯状态空间模型暂不支持。通过 pip 安装后以命令行运行，提供内置评估、量化（bitsandbytes）、保存、上传 Hugging Face 与聊天测试等功能。

- 方向消融 + TPE 自动参数优化，无需手动调参与 transformer 内部知识
- 同时最小化拒答数与 KL 散度以保留原模型能力
- 运行前自动基准测试系统以确定最优 batch size
- 支持 bitsandbytes 量化以降低 VRAM 占用，完成后可上传 Hugging Face

> L7: Heretic is a tool that removes censorship (aka "safety alignment") from
> L13: with a TPE-based parameter optimizer powered by Optuna.
> L89: pip install -U heretic-llm

## virgiliojr94/book-to-skill（⭐35143，confidence: mid）

**把技术书籍 PDF 转成 agent 可用的结构化技能**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

以 Agent Skills 标准（SKILL.md）为输出格式的转换器：指向一个 PDF、文件夹或 glob，先由确定性 Python 提取器产出文本与元数据，再由 agent 按 spec 生成含章节索引、词汇表、模式与速查表的结构化技能，章节文件按需加载。兼容 GitHub Copilot CLI、Claude Code、Codex、OpenCode 等多个宿主。MIT 许可，本地处理，不内置任何书籍内容。

- 输出 SKILL.md + 按需加载的章节文件，节省上下文 token
- 支持 PDF/EPUB/DOCX/HTML 等多种格式，按书类型自动选提取工具
- 本地处理，文件不上传
- 支持 GitHub 发布与 npx skills add 一键安装

> L9:  Turn any technical book, document folder, or collection of sources into a unified agent skill — ready to study, referen
> L90: Two halves: a deterministic Python **extractor** (document → clean text + metadata) and a spec-driven **generator** (you
> L59: Running `/book-to-skill your-book.pdf` (or a folder, glob, or list of files) creates a full skill in the user-level cros

## qdrant/qdrant（⭐35115，confidence: high）

**AI 应用的向量相似度搜索引擎与向量数据库**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

以 Rust 编写的向量数据库服务，提供 REST 与 gRPC API 存储、搜索和管理带 payload 的向量点。支持稠密/稀疏/多向量检索、payload 过滤、混合搜索（RRF/DBSF 融合）、量化与磁盘存储、分片与复制的分布式部署。官方提供 Docker 部署方式与 Go/Rust/JS/Python/.NET/Java 客户端，另有面向边缘设备的 Qdrant Edge 版本和托管云服务（含免费层）。

- 稠密、稀疏与多向量搜索，支持 ColBERT 类 late interaction 模型
- payload 过滤与混合搜索（RRF/DBSF 融合策略）
- 分布式部署：分片、复制、零停机扩缩容
- GPU 加速索引（NVIDIA/AMD），SIMD 硬件加速

> L12: **Qdrant** (read: _quadrant_) is a vector similarity search engine and vector database.
> L28: Qdrant provides a collection of ready-to-use agent skills that bring Qdrant's vector search capabilities directly into y
> L115: Qdrant supports dense vectors for semantic similarity, sparse vectors for full-text search, and multivector search for o

## TheAlgorithms/C-Plus-Plus（⭐34777，confidence: high）

**面向教学的多领域 C++ 算法实现集合**

`ai_role=ai-knowledge · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

The Algorithms 社区维护的 C++ 算法实现集合，覆盖计算机科学、数学与统计、数据科学、机器学习、工程等主题，MIT 许可证开源。每个源码文件独立、仅使用 STL、无需外部库，遵循 C++17 标准，每次提交在 Windows/macOS/Ubuntu 三系统上用 MSVC/AppleClang/GNU 编译测试。文档由源码自动生成，提供程序执行说明、流程图示与 STL 函数链接。定位为教育者与学生的学习资源，同一目标可能提供多种算法策略的实现。

- 仅依赖 STL、无需外部库即可编译运行的原子化实现
- 每次提交在三大操作系统上以三种编译器编译测试
- 文档由源码生成，含执行说明与程序流程图
- 遵循 C++17 标准，可移植到 ESP32、ARM Cortex 等嵌入式平台

> L15: This repository is a collection of open-source implementation of a variety of algorithms implemented in C++ and licensed
> L21: - Each source code is atomic using STL classes and _no external libraries_ are required for their compilation and execut
> L22: - Source codes are compiled and tested for every commit on the latest versions of three major operating systems viz., Wi

## huggingface/diffusers（⭐34744，confidence: high）

**为开发者提供 PyTorch 扩散模型的推理与训练工具库**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=—`

Hugging Face 维护的 PyTorch 扩散模型库，覆盖图像、音频与分子 3D 结构的生成任务。核心由三部分组成：数行代码即可运行的推理 pipeline、可互换的噪声调度器、可组合搭建自定义系统的预训练模型模块。README 提供 pip/conda 安装方式、文本生成图像的快速上手示例，并列出文本生成图像、图生图、修复、超分辨率等任务对应的 pipeline 与 Hub 上的 30,000+ 检查点入口。设计取向为可用性与可定制性，并提示贡献者参考 .ai/ 目录的 AI agent 约定。

- 提供数行代码完成推理的 diffusion pipeline 与 30,000+ 预训练检查点加载
- 噪声调度器可互换，预训练模型可作为组件组合搭建自定义扩散系统
- 覆盖文本生成图像、图生图、修复、超分辨率等任务及对应 pipeline 清单
- 提供面向 AI agent 的贡献约定（.ai/ 目录、claude plugin 安装）

> L7: 🤗 Diffusers is the go-to library for state-of-the-art pretrained diffusion models for generating images, audio, and even
> L11: - State-of-the-art diffusion pipelines that can be run in inference with just a few lines of code.
> L74: If you are using an AI agent, please point it at the project conventions in `.ai/` first (install them as a plugin with 

## mukul975/Anthropic-Cybersecurity-Skills（⭐34601，confidence: high）

**为 AI 代理提供网络安全技能库：818 条技能，映射 6 大框架**

`ai_role=ai-knowledge · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

面向 AI 代理的网络安全技能库，收录 818 条遵循 agentskills.io 标准的结构化技能，覆盖 34 个安全领域，并映射到 MITRE ATT&CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF 与 MITRE F3 六个框架。每条技能以 YAML frontmatter 加 Markdown 正文组织，支持渐进式加载（扫描约 30 tokens，完整加载 500–2,000 tokens）。通过 npx 或 git clone 获取，可在 Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI 等平台直接使用。README 声明为独立社区项目，与 Anthropic PBC 无隶属关系，并要求仅在授权合法场景下使用。

- 818 条技能覆盖 34 个安全领域，映射 6 个行业框架
- 每条技能带 YAML frontmatter，扫描约 30 tokens、完整加载 500–2,000 tokens 的渐进式披露架构
- ATT&CK v19.1 映射经官方 mitreattack-python 库校验，覆盖 290 个技术 ID
- 通过 npx skills add 或 git clone 安装，兼容 agentskills.io 标准平台

> L34: This repo contains **818 structured cybersecurity skills** spanning **34 security domains**, each following the agentski
> L137: **Anthropic Cybersecurity Skills** is not a collection of scripts or checklists. It is an **AI-native knowledge base** b
> L101: Works immediately with Claude Code, GitHub Copilot, OpenAI Codex CLI, Cursor, Gemini CLI, and any agentskills.io-compati

## SillyTavern/SillyTavern（⭐34587，confidence: high）

**面向高级用户的本地 LLM 聊天前端界面**

`ai_role=ai-native · license_risk=viral · deploy=— · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

本地安装的用户界面，用于与文本生成 LLM、图像生成引擎和 TTS 语音模型交互。统一接入多种 LLM API（KoboldAI/CPP、Horde、NovelAI、OpenAI、OpenRouter、Claude、Mistral 等），提供移动端友好布局、Visual Novel 模式、Automatic1111 与 ComfyUI 图像生成集成、TTS、WorldInfo（lorebooks）、自定义 UI、自动翻译，并支持第三方扩展。不提供在线托管服务，也不收集用户数据；运行需 NodeJS 20 及以上。

- 统一界面接入多种 LLM API
- 集成 Automatic1111 与 ComfyUI 图像生成及 TTS
- 支持 WorldInfo（lorebooks）、自定义 UI 与第三方扩展
- 支持 Windows、macOS/Linux、Android (Termux) 与 Docker 安装

> L10: SillyTavern provides a single unified interface for many LLM APIs (KoboldAI/CPP, Horde, NovelAI, Ooba, Tabby, OpenAI, Op
> L16: SillyTavern (or ST for short) is a locally installed user interface that allows you to interact with text generation LLM
> L28: The hardware requirements are minimal: it will run on anything that can run NodeJS 20 or higher. If you intend to do LLM

## Tencent/WeKnora（⭐34498，confidence: high）

**面向企业的开源 LLM 知识平台：文档转 RAG、Agent 与 Wiki**

`ai_role=ai-native · license_risk=none · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

腾讯开源的 LLM 知识框架，围绕同一知识库提供三种模式：RAG（混合检索、多模态解析、引用溯源）、Agent（多步推理、技能沙箱、本地浏览器、MCP 工具与记忆）、Wiki（知识图谱组织与回滚）。支持飞书、Confluence、Notion 等 10 余种数据源自动同步与 10+ 文档格式解析；内置 29 家模型供应商；多工作区 RBAC、任务队列治理与 Langfuse 追踪。可通过 Docker Compose、Kubernetes Helm、Lite 单二进制或桌面应用部署，数据可留在自有环境。

- RAG、Agent、Wiki 三模式共享同一知识库
- 技能经 ClawHub/Git/ZIP 安装并在 Docker/E2B/Cube 沙箱运行，支持操作本地 Chrome/Edge
- 29 家内置模型供应商目录，含 OpenAI、DeepSeek、Ollama 等，模型/向量库/存储后端可替换
- 飞书、Confluence、GitLab、Notion 等数据源自动同步，10+ 文档格式解析

> L32: WeKnora is an open-source, LLM-powered knowledge framework for enterprise document understanding, semantic retrieval and
> L40:  01 RAG: answers you can check, with hybrid search, multimodal parsing and citations. 02 Agent: tasks done with knowledg
> L49: - **Models**: 29 built-in vendors with a generated model catalog, including OpenAI, DeepSeek, Qwen (Alibaba Cloud), Zhip

## openai/CLIP（⭐34473，confidence: high）

**研究者的图像-文本对比预训练模型库**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=research`

OpenAI 发布的 CLIP（Contrastive Language-Image Pre-Training）神经网络，在大量（图像, 文本）对上训练，可用自然语言指令在给定图像时预测最相关的文本片段，README 称其在 ImageNet 零样本设置下达到 ResNet50 的性能水平。以 Python 包形式发布，提供 clip.load、clip.tokenize、encode_image、encode_text 等 API，附零样本预测与线性探测（配合 scikit-learn）两个示例，另提供 Blog、Paper、Model Card 与 Colab 链接。

- 在图像-文本对上训练的对比预训练神经网络
- 提供 clip.load / clip.tokenize / encode_image / encode_text 等 API
- README 附零样本预测与线性探测评估两个示例
- 支持从本地 checkpoint 路径加载模型

> L5: CLIP (Contrastive Language-Image Pre-Training) is a neural network trained on a variety of (image, text) pairs. It can b
> L13: First, install PyTorch 1.7.1 (or later) and torchvision, as well as small additional dependencies, and then install this
> L18: $ pip install git+https://github.com/openai/CLIP.git

## datawhalechina/happy-llm（⭐34418，confidence: high）

**面向 LLM 学习者的大模型原理与训练系统教程**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Datawhale 出品的系统性 LLM 学习教程，从 NLP 基础、Transformer 架构、预训练语言模型讲起，到基于 PyTorch 亲手实现 LLaMA2、训练 Tokenizer 并完成预训练、SFT 与 LoRA/QLoRA 微调，再延伸至 RAG、Agent 与 GRPO 等 Agentic RL 内容。提供在线阅读、PDF 与 PPT 资源，第5/6章训练代码按章节拆分依赖，需具备 Python 与深度学习基础。

- 8 章覆盖从 NLP 基础到 Agentic-RL（GRPO、Search-R1、ReTool）的完整学习路径
- 动手实现 LLaMA2 并完成预训练、SFT、LoRA/QLoRA 微调全流程
- 提供教程 PDF 与配套 PPT 下载，附 ModelScope 模型与创空间体验
- Extra Chapter 开放社区 Blog 投稿（PR 贡献机制）

> L22: &emsp;&emsp;本项目是一个**系统性的 LLM 学习教程**，将从 NLP 的基本研究方法出发，根据 LLM 的思路及原理逐层深入，依次为读者剖析 LLM 的架构基础和训练过程。同时，我们会结合目前 LLM 领域最主流的代码框架，
> L97: &emsp;&emsp;本项目分为两部分——基础知识与实战应用。第1章～第4章是基础知识部分，从浅入深介绍 LLM 的基本原理。其中，第1章简单介绍 NLP 的基本任务和发展，为非 NLP 领域研究者提供参考；第2章介绍 LLM 的基本架构
> L145: 本作品采用知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议进行许可。

## openai/codex-plugin-cc（⭐34330，confidence: high）

**让 Claude Code 用户调用 Codex 做代码审查与任务委派的插件**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

OpenAI 官方发布的 Claude Code 插件，通过 /plugin marketplace 安装后，在 Claude Code 工作流内提供 /codex:review、/codex:adversarial-review 等斜杠命令调用 Codex 做只读代码审查，并提供 /codex:rescue、/codex:transfer 等命令把任务委派给 Codex、迁移会话上下文、管理后台作业。插件封装本地 Codex CLI 与 app server，复用已有安装、认证与 config.toml 配置；需要 ChatGPT 订阅或 OpenAI API key，以及 Node.js 18.18+。可选启用 review gate 在 Claude 停止前执行 Codex 审查。

- /codex:review 只读审查与 /codex:adversarial-review 可定向质询审查
- /codex:rescue 通过子代理把调查、修 bug 等任务委派给 Codex
- /codex:transfer 把 Claude Code 会话迁移为 Codex 线程，可在 App/TUI 续接
- 复用本地 Codex CLI 的安装、认证与 config.toml 配置

> L3: Use Codex from inside Claude Code for code reviews or to delegate tasks to Codex.
> L18: - **ChatGPT subscription (incl. Free) or OpenAI API key.**
> L269: The Codex plugin wraps the Codex app server. It uses the global `codex` binary installed in your environment and applies

## explosion/spaCy（⭐33967，confidence: high）

**Python 开发者的工业级 NLP 处理库**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=high · maturity=—`

Python/Cython 编写的自然语言处理库，提供预训练流水线，支持 70+ 语言的分词与训练，内置分词、词性标注、依存句法分析、命名实体识别、文本分类、实体链接等组件，支持与 BERT 等预训练 transformer 进行多任务学习，并包含训练系统与模型打包、部署和工作流管理功能。采用 MIT 许可证，可通过 pip、conda 安装或从源码编译，另有商业定制服务。

- 支持 70+ 语言的分词与训练，提供多语言预训练流水线
- 内置命名实体识别、句法分析、文本分类等 NLP 组件
- 支持 PyTorch、TensorFlow 等框架的自定义模型
- 提供训练系统与模型打包、部署、工作流管理

> L3: spaCy is a library for **advanced Natural Language Processing** in Python and
> L9: state-of-the-art speed and **neural network models** for tagging, parsing,
> L74: - Production-ready **training system**

## Twigpine/openclaude（⭐33962，confidence: high）

**面向开发者的多后端编码 agent CLI，统一终端工作流**

`ai_role=ai-native · license_risk=none · deploy=library · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

OpenClaude 是一个开源编码 agent CLI，通过一套终端工作流接入云 API 与本地模型后端：支持 prompts、工具调用、agents、MCP、slash 命令与流式输出。通过 /provider 命令做引导式后端配置并保存 profile，凭证存于 .openclaude-profile.json；不自动加载项目 .env，需显式导出或使用 --provider-env-file。会话支持恢复、分叉（仅对话分支，无文件系统隔离）、后台运行（本地子进程，无 daemon）。需 Node.js >=22；配置独立于 Claude Code 存储。

- 单一 CLI 接入 OpenAI 兼容 API、Gemini、GitHub Models、Codex OAuth、Ollama 等后端
- /provider 引导式配置与 profile 保存，支持多个网关型服务商的专属通道
- 后台会话管理：--bg 运行、ps/logs/kill 进程管理
- 内置 bash、文件工具、grep/glob、agents、tasks、MCP 与 web 工具，附带 VS Code 扩展

> L7: OpenClaude is an open-source coding-agent CLI for cloud and local model providers.
> L9: Use OpenAI-compatible APIs, Gemini, GitHub Models, Codex OAuth, Codex, Ollama, Atomic Chat, and other supported backends
> L103: - Coding-agent workflows in one place: bash, file tools, grep, glob, agents, tasks, MCP, and web tools

## TabbyML/tabby（⭐33915，confidence: high）

**自托管 AI 编程助手：团队私有化部署代码补全与问答**

`ai_role=ai-native · license_risk=none · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

Tabby 是一个可自托管的开源 AI 编程助手，定位为 GitHub Copilot 的本地化部署替代方案。核心功能包括代码补全、聊天侧边栏、Answer Engine 知识问答；支持通过 REST API 接入自有文档、索引 GitLab Merge Request 作为上下文、LDAP 认证与团队管理。无需外部数据库或云服务，提供 Docker 一键启动方式，支持消费级 GPU；另可从 Rust 源码构建。IDE 侧通过 VSCode/Vim/IntelliJ 插件接入。

- 自包含部署，无需 DBMS 或云服务
- 支持消费级 GPU 及 Apple M1/M2 Metal 推理
- 提供 OpenAPI 接口与 VSCode/Vim/IntelliJ 插件
- RAG 代码补全、Answer Engine 与 GitLab MR 索引

> L14: Tabby is a self-hosted AI coding assistant, offering an open-source and on-premises alternative to GitHub Copilot. It bo
> L15: * Self-contained, with no need for a DBMS or cloud service.
> L17: * Supports consumer-grade GPUs.

## huggingface/agents-course（⭐33688，confidence: high）

**面向学习者的免费 AI Agent 入门课程（4 单元+认证）**

`ai_role=ai-knowledge · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Hugging Face 官方的 Agents 课程仓库，内容分为 4 个单元：从 agent 与 LLM 基础概念，到 smolagents、LlamaIndex、LangGraph 三个框架的构建实践，再到 Agentic RAG 用例与最终作业（含自动化评测、排行榜与认证）。附有 bonus 单元覆盖 LLM 函数调用微调、可观测性评估与游戏场景。面向具备基础 Python 与 LLM 知识的学习者，免费报名，课程通过 hf.co 访问，仓库接受 typo 修复与新单元的贡献。

- 4 个单元从 agent 基础到带 benchmark 的最终作业
- 覆盖 smolagents、LangGraph、LlamaIndex 三个框架的构建教学
- 最终项目提供 agent 自动化评测与学员排行榜
- Bonus 单元含函数调用微调、可观测性与游戏场景

> L9: The course is divided into 4 units. These will take you from **the basics of agents to a final assignment with a benchma
> L20: |2|Frameworks for AI Agents|Overview of `smolagents`, `LangGraph` and `LlamaIndex`.|
> L26: |4|Final Project - Create, Test and Certify Your Agent|Automated evaluation of agents and leaderboard with student resul

## xai-org/x-algorithm（⭐33670，confidence: high）

**X 平台 For You 信息流排序算法的参考实现**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

xai-org 开源的 X 平台 For You 信息流核心代码：请求路径上由 Thunder 读取关注账号的在网内容，Phoenix 检索与 SimClusters 提供非关注来源内容，经预过滤、Phoenix 打分（按行为预测概率加权求和）、TopK 选择、可见性过滤后输出时间线；另含标注路径（botmaker 规则、agatha/bdsm 账号评分、媒体模型）驱动 visibility-filtering 的 ALLOW/NOTICE/INTERSTITIAL/DROP 判定。2026 年 8 月版本加入权重配置参数、可见性过滤系统与 Phoenix 训练及合成数据生成代码。README 未给出安装运行步骤。

- Phoenix 模型按行为预测概率加权合成帖子分数
- visibility-filtering 输出 ALLOW/NOTICE/INTERSTITIAL/DROP 四种可见性判定
- SimClusters 与 popular_posts_source 作为非关注内容候选来源
- Phoenix 训练代码与合成数据生成，可运行概念验证训练

> L3: This repository contains the core code that determines which posts a viewer sees in the **For You** feed on X. It combin
> L44: Both are ranked together by the same model. **Phoenix** reads the viewer's recent engagement history and predicts, for e
> L30: 1. **Visibility filtering:** `visibility-filtering/` determines whether to show a post, drop it, or show it behind an in

## Pythagora-io/gpt-pilot（⭐33654，confidence: mid）

**给开发者的 AI 编码代理：逐步生成完整应用**

`ai_role=ai-native · license_risk=none · deploy=library · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

GPT Pilot 是 Pythagora VS Code 扩展的核心技术，也可作为 CLI 工具独立运行。它以多 agent 流水线（规格、架构、任务分解、编码、审查、调试、文档）逐步生成应用代码，开发者监督并修正每个步骤；通过代码过滤机制在 LLM 上下文中只呈现当前任务相关的代码。README 同时包含安全通告：2025 年 8 月至 2026 年 6 月间仓库源码中曾隐藏凭据窃取蠕虫，且项目已停止维护。

- 11 种角色的多 agent 流水线（规格/架构/开发/审查/调试/文档等）
- 代码过滤机制使 LLM 对话无需包含整个代码库
- 支持 openai、anthropic、groq 等 provider，Azure 与 OpenRouter 经 openai 设置使用
- 提供 VS Code 扩展与 CLI 两种使用途径

> L40: GPT Pilot is the core technology for the Pythagora VS Code extension that aims to provide **the first real AI developer 
> L46: GPT Pilot aims to research how much LLMs can be utilized to generate fully working, production-ready apps while the deve
> L151: # 🕴How's GPT Pilot different from _Smol developer_ and _GPT engineer_?

## iOfficeAI/AionUi（⭐33598，confidence: high）

**连接 20+ CLI Agent 的桌面 Cowork 平台，支持内置助手与多智能体协作**

`ai_role=ai-native · license_risk=permissive · deploy=desktop · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

跨平台桌面应用，内置 aionrs agent 引擎，提供 21 个办公助手（PPT/Word/Excel 生成等）及文件读写、网页搜索、MCP 工具调用能力。可自动检测本机已安装的 CLI Agent（Claude Code、Codex、Gemini CLI、OpenClaw 等 20 余种）并纳入统一界面并行运行；Team 模式下由 Leader 智能体拆解任务并经 Team MCP Server 分派给 Teammate。支持 30+ 模型平台接入，WebUI 可从浏览器远程访问，并可经 Telegram/Lark/钉钉/微信对话。安装包从 GitHub Releases 下载。

- 内置 agent 引擎，粘贴 API key 即可使用，无需另装 CLI 工具
- 自动检测已安装 CLI Agent，20+ 外部智能体统一界面并行运行
- Team 模式：Leader 拆解任务、Teammate 并行执行、共享任务板与异步邮箱
- WebUI + Telegram/Lark/钉钉/微信远程访问与 Cron 定时自动化

> L13:  A free, open-source, Cowork app with AI Agents
> L103: **Supported Agents:** Built-in Agent (powered by the embedded aionrs agent engine) • Claude Code • Codex • Qwen Code • G
> L144: Same agent capabilities — file read/write, web search, image generation, tool use — regardless of which model powers it.

## lutzroeder/netron（⭐33583，confidence: high）

**神经网络与机器学习模型的可视化查看器**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=—`

Netron 是一个模型结构查看工具，以图形方式展示神经网络、深度学习与机器学习模型的层次结构。支持 ONNX、TensorFlow Lite、PyTorch、TensorFlow、Core ML、Keras 等格式的主线支持，并对 MLIR、GGUF、PaddlePaddle 等提供实验性支持。可通过浏览器、macOS/Linux/Windows 桌面安装包或 Python 包（pip install netron）使用，附带示例模型文件供打开浏览。

- 支持 ONNX、TensorFlow Lite、PyTorch、Core ML 等多种模型格式
- 提供浏览器、桌面应用与 Python 库多种使用方式
- 对 MLIR、GGUF、RKNN、PaddlePaddle 等提供实验性支持
- 提供多种格式的示例模型文件

> L1: Netron is a viewer for neural network, deep learning and machine learning models.
> L3: Netron supports ONNX, TensorFlow Lite, PyTorch, torch.export, ExecuTorch, TorchScript, TensorFlow, Core ML, OpenVINO, Ke
> L9: **Browser**: **Start** the browser version.

## agentscope-ai/agentscope（⭐33422，confidence: mid）

**给开发者的 agent 构建框架与服务运行时**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=local-ok · hardware=— · install_friction=low · maturity=research`

AgentScope 2.0 是一个 agent 框架，提供 SDK 层与服务层两部分：SDK 层以 ReAct 循环、工具集、模型接入、上下文压缩、记忆、权限/人工确认、沙箱执行等构件组合出 agent；服务层为 FastAPI 后端加预置 Web UI，提供多租户多会话、leader-worker 团队编排、IM 渠道接入（飞书/Discord）、RAG 服务、MCP 与技能中心、持久化与定时调度。需 Python 3.11+，从 PyPI 或源码安装，Web UI 依赖 pnpm。

- ReAct 循环 agent 构建块：结构化输出、实时中断恢复、批量工具执行
- 模型层接入 OpenAI、Anthropic、Gemini、DashScope、DeepSeek、Moonshot、Volcengine、xAI、Ollama 等
- 内置 agent 服务：多租户多会话、团队编排、飞书/Discord 渠道、RAG、持久化
- 支持 A2A 协议与 MCP 服务器、实时语音 agent（WebRTC）

> L56: AgentScope 2.0 is a production-ready, easy-to-use agent framework with essential abstractions that keep up with rising m
> L110: |**Model**|LLM, embedding, and TTS across major providers (OpenAI, Anthropic, Gemini, DashScope, DeepSeek, Moonshot, Vol
> L129: AgentScope ships a batteries-included **agent service** — a FastAPI backend with a pre-built Web UI (`examples/web_ui`) 

## zeroclaw-labs/zeroclaw（⭐32988，confidence: high）

**个人 AI 助手运行时：单二进制 Rust 程序，多渠道多模型自托管**

`ai_role=ai-native · license_risk=dual · deploy=— · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

ZeroClaw 是一个以单个 Rust 二进制分发的 agent 运行时，用户在本机配置运行：通过 30+ 渠道（Discord、Telegram、Matrix、邮件、webhook、CLI 等）收发消息，接入约 20 余家 LLM 提供商并可配置 fallback 链与路由，通过 shell、浏览器、HTTP、硬件、自定义 MCP 服务器等工具执行动作。默认自治级别为 supervised，中等风险操作需审批、高风险被阻止，支持 Landlock/Bubblewrap/Seatbelt/Docker 沙箱与工具回执。配置为单个 TOML 文件，可注册为系统服务常驻运行。

- 单 Rust 二进制，本地运行，数据与密钥留在用户机器
- 30+ 消息渠道适配器与可插拔模型提供商（含 fallback 链）
- supervised 默认自治模式、OS 级沙箱与每次动作的加密工具回执
- 通过 Peripheral trait 支持 Raspberry Pi、STM32、Arduino、ESP32 的 GPIO/I2C/SPI/USB

> L21: ZeroClaw is an agent runtime — a single Rust binary you configure and run. It talks to LLM providers (Anthropic, OpenAI,
> L67: - **Provider-agnostic** — model providers are pluggable. Configure Anthropic, OpenAI, local Ollama, or any OpenAI-compat
> L68: - **Security-first, with escape hatches** — default autonomy is `supervised`: medium-risk ops require approval, high-ris

## Fincept-Corporation/FinceptTerminal（⭐32620，confidence: high）

**开源 C++ 金融研究终端：面向投资者/研究者的市场分析与 AI 自动化**

`ai_role=ai-enhanced · license_risk=dual · deploy=desktop · model_dep=local-ok · hardware=— · install_friction=medium · maturity=—`

原生 C++20/Qt6 桌面金融终端，嵌入 Python 3.11 分析，单一二进制。开源版（AGPL-3.0）提供 DCF、投资组合优化、VaR/Sharpe 等分析模块，37 个交易/经济/地缘 agent（自带 LLM key），100+ 数据连接器（FRED、IMF、Polygon 等），纸面交易引擎与 16 家券商集成，可视化节点编辑器与 MCP 工具。另有闭源 Enterprise 版按月付费，团队日常开发在 Enterprise，本仓库每月发布一次。

- 37 个 trader/economic/geopolitics agents，支持 OpenAI、Anthropic、Gemini、Groq、DeepSeek、OpenRouter、Ollama 等 key
- 100+ 数据连接器（FRED、IMF、World Bank、Polygon、AkShare 等）
- 16 家券商集成与纸面交易引擎
- 原生 C++20/Qt6，单二进制，无 Electron/Node.js

> L65: **Fincept Terminal** is a native C++20 desktop terminal for financial research — Qt6 UI, embedded Python 3.11 analytics,
> L119: - **Analytics** — DCF, portfolio optimisation, VaR/Sharpe, derivatives pricing, fixed income, alternatives, plus an 18-m
> L120: - **AI** — 37 trader/investor, economic and geopolitics agents; bring your own key (OpenAI, Anthropic, Gemini, Groq, Dee

## onyx-dot-app/onyx（⭐32543，confidence: high）

**给团队接入内部知识的企业 AI 聊天与 RAG 平台**

`ai_role=ai-native · license_risk=dual · deploy=— · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

Onyx 是面向团队与企业的知识/上下文平台：连接 50+ 应用索引数据（含权限元数据），提供检索增强问答、深度研究、自定义 Agent、联网搜索、沙箱代码执行、语音交互等功能。支持自托管与气隙部署，数据索引与处理在自身环境内完成；提供 Web、桌面端、Slack/Discord 机器人、MCP server、Chrome 扩展与嵌入式组件多种访问方式。采用 CE（MIT）+ EE 双版本模式，标准版与轻量版两种部署形态。

- 连接 50+ 应用构建组织知识索引
- Agentic RAG 与多步深度研究流程
- 支持自托管/气隙部署，模型与嵌入可本地运行
- MCP server 方式向外部 AI 客户端提供组织上下文

> L22: **Onyx** is the knowledge/context layer for your team and AI agents.
> L24: Onyx connects to your application to index and surface knowledge from 50+ applications while protecting your data sovere
> L57: Onyx supports all major LLM providers, both self-hosted (like Ollama, LiteLLM, vLLM, etc.) and proprietary (like Anthrop

## datawhalechina/self-llm（⭐32500，confidence: high）

**面向国内初学者的开源大模型配置、部署与微调中文教程**

`ai_role=ai-knowledge · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Datawhale 出品的开源大模型教程仓库，基于 Linux 平台覆盖环境配置、本地部署（命令行调用、在线 Demo、LangChain 集成）与微调（分布式全量微调、LoRA、ptuning）全流程，收录 50+ 主流大语言与多模态模型，并设 AMD GPU（ROCm）、昇腾 Ascend NPU、Apple M 等硬件平台专区。面向学生、研究者等需要本地部署与低成本使用 LLM 的初学者，内容为纯教程，由社区协作维护。

- 收录 50+ 主流开源大模型，每个模型提供部署、微调与使用教程
- 设 AMD GPU（ROCm）、昇腾 Ascend NPU、Apple M 等硬件平台专区
- 微调覆盖分布式全量微调、LoRA、ptuning 等方法
- 含 Chat-嬛嬛、天机、AMChat 等实战 Example 系列

> L5: &emsp;&emsp;本项目是一个围绕开源大模型、针对国内初学者、基于 Linux 平台的中国宝宝专属大模型教程，针对各类开源大模型提供包括环境配置、本地部署、高效微调等技能在内的全流程指导，简化开源大模型的部署、使用和应用流程，让更多的
> L69:  ✨ 已支持 50+ 主流大语言模型 ✨
> L141:  🚀 AMD GPU 平台已支持模型

## topoteretes/cognee（⭐32438，confidence: high）

**给 AI agent 提供持久长期记忆的开源知识图谱平台**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=research`

将文档、代码与会话内容转化为可自托管的知识图谱，agent 可在多次会话间存储（remember）、检索（recall）、增补（improve）和删除（forget）记忆。默认路径使用本地 GLiNER 抽取与本地嵌入模型，无需 API key 即可在 CPU 上运行；配置 LLM key 后可生成回答，支持 OpenAI 或本地 Ollama。提供 Python 库、CLI、REST API、MCP server 及 Claude Code/Codex 插件，支持 Docker Compose 部署，Postgres 单机整合当前为 demo 特性。

- 无 LLM key 时用本地 GLiNER 与嵌入模型在 CPU 上构建图谱
- remember/recall/improve/forget 四种记忆操作
- Claude Code、Codex、OpenClaw、MCP 客户端等多种接入接口
- Docker 镜像内置 GLiNER 运行时，可用 COGX 格式从 Mem0/Letta/Zep/Graphiti 导入

> L32:  Cognee is a free open-source AI memory platform that gives AI agents persistent long-term memory across sessions. Turn 
> L34:  Runs locally for free — no API key required.
> L116: Once a key is set, Cognee uses OpenAI for language models and embeddings, and processing and generated answers make prov

## tirth8205/code-review-graph（⭐32218，confidence: high）

**给 AI 编码工具的本地代码知识图谱：MCP 提供精准审查上下文**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=—`

用 Tree-sitter 将代码库解析为持久化图谱（函数/类/导入为节点，调用/继承/测试覆盖为边），存于 SQLite，并通过 MCP 服务器向 AI 编码工具提供紧凑上下文。变更时通过调用边追踪影响面（blast radius），让助手只读受影响文件；hooks、pre-commit 与 watch 模式基于 SHA-256 做增量更新。`install` 命令检测已装 AI 工具并写入 MCP 配置。同一分析可作为 GitHub Action 在 CI 中运行，附带可复现的 token 基准测试。需 Python 3.10+。

- Tree-sitter 解析 + SQLite 持久化图谱，覆盖 30+ 语言，可用 languages.toml 扩展
- blast-radius 分析返回变更影响的最小文件集
- hooks/watch 增量更新：~3,000 文件项目两文件编辑约 2.5 秒重建
- GitHub Action 形式的 PR 风险评分评论，可设 fail-on-risk 合并门禁

> L12:  A local code knowledge graph that gives AI coding tools precise review context over MCP.
> L38: AI coding tools often re-read large parts of a codebase to review a change. `code-review-graph` builds a structural map 
> L86: The repository is parsed into ASTs with Tree-sitter and stored as a graph of nodes (functions, classes, imports) and edg

## feder-cr/invisible_dots（⭐32125，confidence: high）

**自托管的个人 AI 智能体：给每个用户一台带反检测浏览器的 VM**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=locked-api · hardware=— · install_friction=low · maturity=idea`

以 Node.js CLI 与 Web 服务器形式提供的自托管平台：`setup --all` 通过 QEMU（KVM 或 Windows Hypervisor Platform 加速）构建/下载 Dot 的镜像，每个 Dot 拥有一台带持久磁盘的 Linux 桌面虚拟机，空闲休眠、有任务时唤醒。浏览器基于 C++ 补丁版 Firefox（invisible_playwright_mcp），指纹在引擎内设置，各身份独立保存 cookies 与登录态；支持 MCP 服务器接入、权限分级（allow/ask/deny）、定时任务队列、以及 Web UI/CLI/HTTP API/Telegram/WhatsApp 多通道触达，重启后消息与任务不丢失。README 注明状态为 alpha，仅支持 Linux 与 Windows，使用时需遵守目标站点条款与 robots.txt。

- 硬件加速 VM 内运行 Linux 桌面，持久磁盘，空闲休眠/按任务唤醒
- C++ 补丁版 Firefox 浏览器，指纹在引擎内设置，身份级 cookies 与登录态
- MCP 服务器声明式接入与 allow/ask/deny 权限分级，ask 请求可在重启后恢复
- Web UI、CLI、HTTP API、Telegram、WhatsApp 多通道接入

> L51: |**A computer of its own**|A hardware-accelerated VM with a Linux desktop and a persistent disk. It sleeps when idle and
> L52: |**A browser that is not blocked**|invisible_playwright_mcp: Firefox patched in C++, the fingerprint set inside the engi
> L54: |**Your MCP servers**|Any MCP server you declare, a program on its computer or a URL, as in Claude Code. Its keys stay o

## iOfficeAI/OfficeCLI（⭐32107，confidence: mid）

**让 AI Agent 读写并自动化 Word/Excel/PPT 的 CLI 套件**

`ai_role=ai-native · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=medium · maturity=idea`

以单一二进制分发的命令行工具，供 AI Agent 创建、读取、修改与自动化 .docx/.xlsx/.pptx 文件，运行无需安装 Office。内置 HTML 渲染引擎可将文档渲染为 HTML 或逐页 PNG，供多模态 Agent 执行渲染-检查-修正循环；Excel 写入时自动求值 350+ 内置函数。officecli install 会将 skill 文件装入检测到的 AI 编码 Agent。自述以 skill 文件引导 Agent 一行命令完成安装。

- 单二进制内嵌 .NET 运行时，无需安装 Office 或管理依赖
- 内置渲染引擎：view html / view screenshot / watch 三种模式，支持 PNG 截图供多模态 Agent 读取
- Word/Excel/PPT 三类格式的读取、修改、创建能力矩阵
- Excel 公式引擎：350+ 函数写入时自动求值，含动态数组与财务统计函数

> L3: > **OfficeCLI is the world's first and the best Office suite designed for AI agents.**
> L68: This copies the binary to your PATH and installs the **officecli skill** into every AI coding agent it detects — Claude 

## getzep/graphiti（⭐31886，confidence: high）

**为 AI Agent 构建可查询的时序知识图谱框架**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

Graphiti 是构建和查询时序上下文图谱的开源框架，面向处理动态数据的 AI Agent。事实带时间有效期窗口、追溯至原始数据（episodes），支持 Pydantic 定义或从数据涌现的本体，新数据增量集成无需全图重算，检索采用语义嵌入+BM25 关键词+图遍历的混合方式。图数据库后端支持 Neo4j、FalkorDB、Amazon Neptune、Kuzu（已弃用），默认使用 OpenAI 做推理与嵌入，另附 MCP server 实现。

- 事实带时间有效期窗口，历史查询无需全图重算
- 混合检索：语义嵌入 + BM25 关键词 + 图遍历
- 增量图构建，支持规定式与习得式本体（Pydantic 模型）
- 提供 MCP server，供 AI 助手调用图谱能力

> L27: Graphiti is a framework for building and querying temporal context graphs for AI agents. Unlike static knowledge graphs,
> L143: - Neo4j 5.26 / FalkorDB 1.1.2 / Amazon Neptune Database Cluster or Neptune Analytics Graph + Amazon OpenSearch
> L165: pip install graphiti-core

## openai/openai-python（⭐31868，confidence: high）

**OpenAI API 官方 Python 客户端库**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

面向 Python 3.10+ 应用的 OpenAI REST API 官方 SDK，由 OpenAPI 规范生成，包含全部请求参数与响应字段的类型定义，提供同步与异步客户端。功能覆盖 Responses API、Chat Completions、流式响应（SSE）、Realtime API（WebSocket 音视频对话）、视觉输入、自动分页、文件上传与 Webhook 签名校验；支持 API key、Kubernetes/Azure/GCP 工作负载身份及 X.509 mTLS 多种认证方式，错误按状态码映射为类型化异常。

- 同步与异步客户端，HTTPX2 默认传输，可选 aiohttp
- 支持 SSE 流式与 Realtime WebSocket 多模态会话
- 多认证方式：API key、K8s/Azure/GCP 工作负载身份、X.509 mTLS
- 自动分页迭代器与 TypedDict/Pydantic 类型定义

> L5: The OpenAI Python library provides convenient access to the OpenAI REST API from any Python 3.10+
> L9: It is generated from our OpenAPI specification.
> L19: pip install openai

## ScrapeGraphAI/Scrapegraph-ai（⭐31841，confidence: high）

**基于 LLM 的 Python 网页抓取库，自然语言即抽取**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

使用 LLM 与图（graph）逻辑构建抓取流水线的 Python 库，支持网站与本地文档（XML、HTML、JSON、Markdown）的信息抽取，用户给出提示词与来源即可输出结构化字典。内置 SmartScraperGraph、SearchGraph、SpeechGraph、ScriptCreatorGraph 等多种流水线及多页并行版本，可通过 OpenAI、Groq、Azure、Gemini、MiniMax 等 API 或 Ollama 本地模型调用 LLM。安装需配合 Playwright，另有官方托管云 API（Python/Node SDK）与匿名遥测（可关闭）。

- 提示词驱动的抓取流水线（SmartScraperGraph 等 6 种及 multi 并行版本）
- 支持 OpenAI/Groq/Azure/Gemini/MiniMax 等 API 与 Ollama 本地模型
- 可抓取网站与本地文档（XML/HTML/JSON/Markdown），并可生成 Python 脚本或音频文件
- 同时提供开源库与托管云 API 两种形态（MIT 许可）

> L24: ScrapeGraphAI is a *web scraping* python library that uses LLM and direct graph logic to create scraping pipelines for w
> L103: It is possible to use different LLM through APIs, such as **OpenAI**, **Groq**, **Azure**, **Gemini**, **MiniMax** and m

## Zackriya-Solutions/meetily（⭐31839，confidence: mid）

**本地运行的隐私优先 AI 会议记录与摘要应用**

`ai_role=ai-enhanced · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=medium · maturity=—`

Meetily 是一款运行在用户本机的会议助手，基于 Tauri（Rust 后端 + Next.js 前端）构建，可捕获麦克风与系统音频、用 Whisper 或 Parakeet 模型实时转录，并生成会议摘要。全部处理与存储在本地完成，不发送数据到云端。摘要支持多种 AI 提供方（推荐本地 Ollama），也可接 Claude、Groq、OpenRouter 或自定义 OpenAI 兼容端点。提供 Windows 安装包、macOS dmg，Linux 需从源码构建；说话人分离在社区版尚未提供（规划于 PRO）。

- Whisper/Parakeet 模型本地实时转录，无需云端
- 多 AI 提供方摘要：Ollama（本地）、Claude、Groq、OpenRouter、OpenAI 兼容端点
- 麦克风与系统音频同时采集，含 ducking 与削波防护
- GPU 加速：macOS Metal/CoreML 自动启用，Windows 包含 Vulkan 构建

> L23: A privacy-first AI meeting assistant that captures, transcribes, and summarizes meetings entirely on your infrastructure
> L37: Meetily is a privacy-first AI meeting assistant that runs entirely on your local machine. It captures your meetings, tra
> L67: - **Flexible AI Provider Support:** Choose from Ollama (local), Claude, Groq, OpenRouter, or use your own OpenAI-compati

## jumpserver/jumpserver（⭐31786，confidence: high）

**为 DevOps/IT 团队提供带 AI 能力的开源堡垒机（PAM）平台**

`ai_role=ai-enhanced · license_risk=viral · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

JumpServer 是开源的特权访问管理（PAM）平台，即堡垒主机。它为 DevOps 与 IT 团队提供统一工作区，安全接入 SSH、RDP、Kubernetes、数据库、网站、RemoteApp、VirtualApp 等资产。采用多组件架构：JumpServer 核心平台、Lina Web 界面、Luna Web 终端与原生客户端、KoKo 协议连接代理、Chen 数据库连接器、Kael AI 组件；另有企业版组件（Windows 应用连接器、RDP/数据库/VNC 协议代理、会话录像转码等）。支持 11 种语言界面，通过一键脚本在 64 位 Linux 服务器上部署，默认管理员账号 admin。

- 统一接入 SSH、RDP、Kubernetes、数据库、网站、RemoteApp、VirtualApp 等多种协议与资产
- 内置 AI 能力：终端 AI 提示与 AI 助手（Kael 组件）
- KoKo TUI 终端支持资产搜索与多会话管理
- 组件化架构，社区版与企业版组件分层

> L17: JumpServer is an open-source Privileged Access Management (PAM) platform with AI-powered capabilities. It gives DevOps a
> L83:  JumpServer AI component
> L142: Copyright (c) 2014-2026 FIT2CLOUD, All rights reserved.

## googleworkspace/cli（⭐31602，confidence: high）

**面向人类与 AI agent 的 Google Workspace 统一命令行工具**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=idea`

单一 CLI 覆盖 Drive、Gmail、Calendar、Sheets、Docs、Chat、Admin 等 Workspace API：运行时读取 Google Discovery Service 动态生成命令面，新端点自动纳入。输出为结构化 JSON，支持 --dry-run 预览与自动分页；附带 100+ 个 SKILL.md 格式的 agent 技能与 50 个工作流配方，支持 npx skills add 与 OpenClaw 安装，并作为 Gemini CLI 扩展接入。认证覆盖交互式 OAuth、Service Account、预取 token 等多种方式；凭据以 AES-256-GCM 加密存放于系统钥匙串。预编译二进制发布于 GitHub Releases，也可经 npm、cargo、Homebrew、Nix 安装。README 声明非 Google 官方支持产品，v1.0 前可能有破坏性变更。

- 运行时读取 Discovery Service 动态构建全部命令，无需随 API 更新发版
- 输出结构化 JSON，附带 100+ agent 技能与 50 个 Gmail/Drive/Docs/Calendar/Sheets 配方
- 多种认证工作流：交互式 OAuth、Service Account、预取 token、无头 CI 导出
- 带 + 前缀的手工 helper 命令（+agenda、+send、+triage 等）与 Model Armor 提示注入扫描

> L3: **One CLI for all of Google Workspace — built for humans and AI agents.**
> L190: The repo ships 100+ Agent Skills (`SKILL.md` files) — one for every supported API, plus higher-level helpers for common 

## storytold/artcraft（⭐31446，confidence: high）

**面向艺术家与影像创作者的 AI 图像/视频生成 IDE**

`ai_role=ai-native · license_risk=dual · deploy=— · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

ArtCraft 定位为交互式 AI 图像与视频创作的 IDE：支持 2D 合成、3D 场景搭建、角色摆姿、镜头规划等可视化创作工具，并可调用多种模型生成图像、视频、音乐、3D 网格与世界（Gaussian splats），目录共列出 62 个模型。提供 Windows 与 macOS 稳定版下载，也可从源码构建（含 Linux）。部分模型标注为当前禁用或桌面端受限。

- 2D/3D 场景合成与镜头规划工具（Image to Location、Kitbashing 等）
- 62 模型目录覆盖图像、视频、音乐/音效、3D 网格与世界生成
- 支持 Grok、Midjourney、Sora、World Labs 等模型提供方
- Windows/macOS 稳定版下载，支持从源码构建（含 Linux）

> L17: ArtCraft is the IDE for interactive AI image and video creation. Compose in 2D, stage scenes in 3D, and choose the model
> L50: ## Models and Providers Supported within ArtCraft
> L112: - Stable releases for Windows and macOS

## Lightning-AI/pytorch-lightning（⭐31413，confidence: high）

**为深度学习开发者提供的 PyTorch 训练框架，自动化工程代码**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=—`

组织 PyTorch 代码的深度学习框架，将反向传播、混合精度、多 GPU 与分布式训练等工程代码自动化，用户保留模型逻辑控制。提供两个核心包：PyTorch Lightning（Trainer 抽象）与 Lightning Fabric（专家级控制）。通过 pip/conda 安装，支持从 CPU 到多节点 GPU/TPU 运行，提供 40+ 高级特性如早停、检查点、ONNX/TorchScript 导出，并维护多平台 CI 测试矩阵。

- Trainer 接口无需改代码即可切换 CPU/GPU/TPU、多 GPU 与多节点训练
- Fabric 提供对训练循环与扩展策略（DDP/FSDP/DeepSpeed）的专家级控制
- 支持 TorchScript 与 ONNX 导出用于生产部署
- 早停、检查点、实验管理等 40+ 高级特性

> L3: **The deep learning framework to pretrain and finetune AI models.**
> L34: Training models in plain PyTorch requires writing and maintaining a lot of repetitive engineering code. Handling backpro
> L45: PyTorch Lightning: Train and deploy PyTorch at scale.
> L264:  Use state-of-the-art distributed training strategies (DDP, FSDP, DeepSpeed) and mixed precision out of the box

## ahujasid/mcp-for-blender（⭐31370，confidence: high）

**让 AI 通过 MCP 协议控制 Blender 进行 3D 建模的社区插件**

`ai_role=ai-native · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=—`

由两部分组成：Blender 插件内建 socket 服务器接收并执行命令，以及实现 Model Context Protocol 的 Python 服务器连接两者。AI 可创建/修改/删除 3D 物体、控制材质、直接编写 Blender Python 代码，并通过多角度/线框/渲染视图自查结果。接入 Poly Haven、Sketchfab、Poly Pizza 资产及 Tripo、Hyper3D Rodin、Hunyuan3D 生成 3D 模型。提供一键安装脚本、pipx 与 Docker 运行方式；socket 服务器无认证加密，建议保持 localhost 或使用安全模式。

- 双向 socket 通信：AI 读写 Blender 对象、材质与场景
- 多角度/线框/X 光/渲染视图供 AI 自检成果
- 集成 Poly Haven、Sketchfab、Poly Pizza 与 Tripo/Hyper3D Rodin/Hunyuan3D 模型生成
- BLENDER_MCP_SAFE_MODE=1 可在执行前校验脚本并拦截风险代码

> L10: Prompt-assisted 3D modeling, scene creation, and manipulation — driven by AI.
> L132: 1. **Blender Addon** (`addon.py`) — a Blender addon that creates a socket server within Blender to receive and execute c
> L133: 2. **MCP Server** (`src/blender_mcp/server.py`) — a Python server that implements the Model Context Protocol and connect

## decolua/9router（⭐30956，confidence: mid）

**为 AI 编码 CLI 工具聚合 40+ 模型提供商的本地路由网关**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

本地运行的 AI 模型路由网关：将 Claude Code、Codex、Cursor、Cline 等 CLI 编码工具统一接入 40+ 提供商与 100+ 模型，暴露 OpenAI 兼容端点（localhost:20128/v1）。核心机制包括 RTK 令牌压缩（对 git diff/grep 等工具输出做无损压缩）、订阅→低价→免费的三级自动回退、多账号轮询、配额实时追踪与 OAuth 令牌自动刷新。通过 npm 全局安装或源码/Docker 运行，提供 Web Dashboard 管理。

- RTK 工具输出压缩，声明节省 20-40% 输入令牌
- 订阅→低价→免费的三级自动回退路由
- OpenAI/Claude/Gemini/Cursor/Kiro/Vertex 间格式转换
- 自托管 STT/TTS/Embedding 提供商接入与 baseUrl 配置

> L7:  **Connect All AI Code Tools (Claude Code, Cursor, Antigravity, Copilot, Codex, Gemini, OpenCode, Cline, OpenClaw...) to
> L53: npm install -g 9router
> L387: |🎯 **Smart 3-Tier Fallback**|Auto-route: Subscription → Cheap → Free|Never stop coding, zero downtime|

## ComposioHQ/composio（⭐30608，confidence: high）

**给 AI Agent 开发者提供 1000+ 工具集成、认证与沙箱的 SDK**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

Composio 是一个 SDK monorepo，包含 TypeScript SDK（@composio/core）、Python SDK、CLI 以及多个 provider 适配器。它为 AI Agent 提供 1000+ 预认证工具集、按用户会话、认证、触发器和沙箱；会话默认获得可在运行时发现、认证并执行工具的 meta tools，避免将大量工具定义载入上下文；每个会话也可暴露托管 MCP 端点供 Claude、Cursor 等 MCP 客户端使用。CLI 支持工具搜索、执行、账号连接和 TypeScript 脚本工作流。需要 COMPOSIO_API_KEY。TypeScript SDK 要求 Node 22+，Python SDK 支持 3.10+。

- 1000+ 预认证工具集与按用户会话管理
- meta tools 运行时发现/认证/执行，控制上下文占用
- 每个会话可开启托管 MCP 端点
- 覆盖 OpenAI、Anthropic、LangChain、CrewAI 等的 provider 适配器

> L20: Composio gives your AI agents 1000+ pre-authenticated toolkits, per-user sessions, authentication, triggers, and a sandb
> L27: - **Provider adapters** for OpenAI Agents, Claude Agent SDK, Vercel AI SDK, LangChain, and more

## e2b-dev/awesome-ai-agents（⭐30483，confidence: mid）

**为开发者和研究者收录开源与闭源 AI 智能体项目的清单**

`ai_role=ai-knowledge · license_risk=none · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=—`

由 E2B 维护的 AI 自主智能体目录，将条目分为开源项目与闭源项目/公司两部分，每条记录名称、一句话简介、类别（如通用、多智能体、编码、HR 等）与相关链接（文档、论文、GitHub、Discord 等）。收录 Adala、AutoGen、AutoGPT、BabyAGI、Aider 等项目，并按字母序组织。清单自我声明不保证全面，提供 Web 版按类别与用例过滤，社区可通过 PR 或表单提交新条目。

- 条目分开源项目与闭源项目/公司两部分组织
- 每个条目含类别、描述与文档/论文/GitHub 等链接
- 提供 Web 版界面按类别与用例过滤
- 通过 PR 或表单接受社区提交并要求按字母序排列

> L17: Welcome to our list of AI agents.
> L18: We structured the list into two parts:
> L19: - Open source projects
> L20: - Closed-source projects and companies

## jackwener/OpenCLI（⭐30374，confidence: high）

**把任意网站变成 CLI 命令、供 AI agent 操作登录态浏览器的工具**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=—`

OpenCLI 是面向 AI agent 的通用浏览器自动化 CLI，同时自称 agent-browser 的一款替代工具。它通过 Browser Bridge 扩展与本地守护进程连接用户已登录的 Chrome/Chromium，无需站点适配器即可导航、点击、填表、提取与截图；内置 Bilibili、知乎、Reddit、HackerNews 等站点适配器提供确定性命令。所有命令默认输出 JSON 并配退出码约定，便于 agent 消费。安装方式包括 macOS/Windows 桌面应用 OpenCLIApp 和 npm 全局安装（需 Node.js ≥ 20.18.1），并通过 npx skills 向 Claude Code、Cursor 等 agent 安装四个技能。

- 内置 Bilibili、知乎、小红书、Reddit 等站点适配器，提供确定性 CLI 命令
- 命令默认 JSON 输出（ok/data/error 结构）并配非零退出码约定
- 四个可安装技能：opencli-browser、adapter-author、autofix、usage
- 支持多 Chrome profile 别名管理与 --session 页面会话路由

> L12: OpenCLI is a **general-purpose browser automation CLI for AI agents** and an **agent-browser alternative**. Navigate, in
> L17: - **Let AI Agents operate any website** — install the `opencli-browser` skill in your AI agent (Claude Code, Cursor, etc
> L60: npm install -g @jackwener/opencli

## langchain-ai/deepagents（⭐30365，confidence: high）

**给开发者的开箱即用 agent harness，构建长程多步 agent**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

LangChain 团队开源的 agent harness，基于 LangGraph 构建，提供子代理、可插拔文件系统后端、上下文管理与持久化记忆等默认组件，每个部件可覆盖或替换而不需 fork。支持任何具备工具调用能力的模型（前沿 API、开源权重或本地模型），随流式输出、检查点持久化与经 LangSmith 的追踪评估能力一同提供。提供 Python 与 JavaScript/TypeScript 两个库版本，另有终端编码代理 Deep Agents Code，通过 curl 脚本安装。

- 子代理机制：将任务委派给具有独立上下文窗口的代理
- 可插拔文件系统（本地/沙箱/远程后端）与 shell 执行
- 上下文管理：摘要长对话并将工具输出落盘
- 人在回路审批、按需加载的 Skills 与任意 MCP 服务器接入

> L14: Deep Agents is an open source agent harness — an opinionated agent that runs out of the box. Extend, override, or replac
> L20: - **Model-agnostic** — works with any LLM that supports tool calling: frontier, open-weight, or local
> L21: - **Production-ready** — built on LangGraph (streaming, persistence, checkpointing) with first-class tracing, evaluation

## oraios/serena（⭐30344，confidence: high）

**给编码 Agent 提供符号级语义代码检索与编辑工具的 MCP 服务器**

`ai_role=ai-native · license_risk=viral · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Serena 以 MCP 服务器形式向编码 Agent 提供 IDE 式工具：符号级检索、重构、符号编辑与调试，并带跨会话记忆系统和多层 YAML 配置体系。语义能力有两种后端可选：默认的开源语言服务器（LSP，支持 40+ 语言）与付费的 JetBrains 插件（含独占的调试工具）。README 强调 agent-first 工具设计避免行号级低层操作；通过 uv 安装，可接入 Claude Code、Codex 等任何支持 MCP 的客户端。

- 符号级检索、重构与编辑工具，经 MCP 接入任意客户端
- LSP 后端支持 40+ 编程语言，可选 JetBrains 插件后端
- JetBrains 插件独占交互式调试（断点、变量检查、REPL）
- 跨会话/跨项目记忆系统与多层可组合配置

> L6: * Serena provides essential **semantic code retrieval, editing, refactoring and debugging tools** that are akin to an ID
> L58: Serena can extend the functionality of your existing AI client via the **model context protocol (MCP)**.
> L95: When using Serena's language server backend, we provide **support for over 40 programming languages**, including

## facefusion/facefusion（⭐30301，confidence: mid）

**面向开发者的人脸换脸与唇形同步操作平台**

`ai_role=ai-native · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

以 Python 入口（facefusion.py 命令行）运行的人脸操作平台，提供安装文档与使用文档；源码安装需要终端操作与技术能力，同时提供 Windows 与 macOS 安装器供不熟悉终端的用户使用。README 未展开具体功能细节，仅以主题标签（deepfake、face-swap、lip-sync 等）与描述表明其用途。

- 通过 python facefusion.py 命令行运行
- 提供 Windows 与 macOS 安装器
- 提供安装与深度使用文档

> L3: > Industry leading face manipulation platform.
> L15: Be aware, the installation needs technical skills and is not recommended for beginners. In case you are not comfortable 
> L22: python facefusion.py [commands] [options]

## nautechsystems/nautilus_trader（⭐30243，confidence: high）

**给量化交易者的多资产多市场 Rust 原生交易引擎**

`ai_role=ai-enhanced · license_risk=viral · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=idea`

以 Rust 为核心、Python 作为策略控制面的开源交易引擎，覆盖研究、确定性回测模拟与实盘执行，采用事件驱动架构并通过 PyO3 提供 Python 绑定。通过模块化适配器接入带 REST API 或 WebSocket 的任意交易场所，当前集成覆盖 CEX/DEX 加密货币交易所、外汇/股票/期货/期权等传统市场及博彩交易所。预编译 wheel 安装无需 Rust 工具链；v2 迁移期 v1 仅接收关键安全回补，当前仍处活跃开发、版本间可能出现破坏性变更。

- 同一策略代码可在回测与实盘系统间复用
- Rust 核心（mimalloc/tokio）+ Python 控制面的双层架构
- 20+ 交易所与数据商的模块化适配器集成表
- 支持 128 位高精度与 64 位标准精度两种数值模式

> L30: NautilusTrader is an open-source, production-grade, Rust-native engine for multi-asset,
> L63: - **AI Training**: Engine fast enough to train AI trading agents (RL/ES).
> L85: Python bindings are provided via PyO3 for the Rust-native v2 runtime.

## academic/awesome-datascience（⭐30197，confidence: mid）

**数据科学学习与资源导航的聚合清单，面向入门到实战者**

`ai_role=ai-knowledge · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

开源的数据科学知识清单：回答"什么是数据科学、应该学什么"，收录专家文章链接、编程语言与工具库介绍（Python/R、Pandas、NumPy、Scikit-Learn、Seaborn），给出初学者五步路线图，并包含 Agents 框架/工具、科研知识检索等分类的资源条目。提供 brew 安装的 academic CLI，欢迎社区贡献。面向数据科学学习者与从业者。

- 数据科学入门路线图（Python→核心库→项目→数学→ML）
- 收录专家视角的数据科学定义与职业发展链接
- Agents 分类列出可用于数据科学工作流的框架与工具
- Research & Knowledge Retrieval 分类收录 arXiv/PubMed 检索等工具条目

> L7: **An open-source Data Science repository to learn and apply concepts toward solving real- world problems.**
> L60: ## Agents

## assafelovic/gpt-researcher（⭐30140，confidence: high）

**为研究任务生成带引文报告的自主深度研究 Agent**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

面向个人与组织的自动化研究 Agent：将任务拆解为研究问题，由 planner 与 execution 多智能体分工检索、汇总并生成超过 2,000 词、引用 20+ 来源的报告。支持网页与本地文档（PDF、CSV、Excel、Markdown、Word 等）两类数据源，提供 pip 包、Docker 部署、HTML/NextJS 前端、MCP 客户端与服务端、LangGraph 多智能体助手及 LangSmith 追踪。默认依赖 OpenAI 与 Tavily API key，也可通过 OPENAI_BASE_URL 接入自定义模型。

- planner/execution/publisher 多智能体架构，递归式广度+深度研究
- 支持网页搜索与本地文档研究，报告可导出 PDF/Word/Markdown
- Jev 上下文过滤，无 key 时回退 BM25 关键词过滤
- 提供 MCP Server（独立仓库 gptr-mcp）与 Claude Desktop 集成

> L20: **GPT Researcher the first open deep research agent designed for both web and local research on any given task.**
> L22: The agent produces detailed, factual, and unbiased research reports with citations. GPT Researcher provides a full suite
> L51: The core idea is to utilize 'planner' and 'execution' agents. The planner generates research questions, while the execut

## openai/openai-agents-python（⭐30100，confidence: high）

**给开发者的多 Agent 工作流 Python 框架**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

OpenAI 官方发布的 Python SDK，用于构建多 Agent 工作流。核心概念包括 Agent（配置指令/工具/护栏/交接）、沙箱 Agent（容器内长时任务）、实时 Agent（WebSocket 语音）、语音管线、Agent 即工具与交接、MCP 等工具接入、输入输出护栏、人工介入机制、会话历史管理与内置 tracing。Provider 无关：支持 OpenAI Responses 与 Chat Completions API 及 100+ 其他 LLM。需 Python 3.10+，通过 pip/uv 安装，运行示例需设置 OPENAI_API_KEY。

- 多 Agent 工作流核心原语：handoffs、guardrails、sessions、tracing
- 支持文本、沙箱、实时语音、语音管线四种 Agent 运行方式
- provider-agnostic：支持 OpenAI API 及 100+ 其他 LLM
- 沙箱客户端：macOS/Linux 用本地沙箱，Windows 支持 Docker 沙箱

> L3: The OpenAI Agents SDK is a lightweight yet powerful framework for building multi-agent workflows. It is provider-agnosti
> L27: To get started, set up your Python environment (Python 3.10 or newer required), and then install OpenAI Agents SDK packa

## JaidedAI/EasyOCR（⭐30080，confidence: high）

**支持80+语言的即用型 OCR 图文识别库**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=self-host · model_dep=— · hardware=cpu-ok · install_friction=low · maturity=—`

基于 PyTorch 的开源 OCR 库：检测端使用 CRAFT 算法，识别端使用 CRNN（Resnet/VGG 特征提取 + LSTM 序列标注 + CTC 解码），支持拉丁、中文、阿拉伯、天城文、西里尔等 80+ 种语言的文字检测与识别，输出边界框、文本与置信度。以 Python 包与命令行两种方式使用，模型权重自动下载或从模型库手动放置；无 GPU 或显存不足时可切换 CPU-only 模式。手写体识别尚在开发计划中，新语言需按流程提交字符表与词典 PR。

- 支持 80+ 语言与主流书写系统，多语言可同时传入识别
- 检测用 CRAFT、识别用 CRNN（Resnet/VGG + LSTM + CTC）
- 提供 Python API 与命令行两种使用方式，模型权重自动下载
- GPU 不可用或显存低时可用 gpu=False 以 CPU 模式运行

> L8: Ready-to-use OCR with 80+ supported languages and all popular writing scripts including: Latin, Chinese, Arabic, Devanag
> L84: In case you do not have a GPU, or your GPU has low memory, you can run the model in CPU-only mode by adding `gpu=False`.
> L120: All deep learning execution is based on Pytorch. :heart:

## gitleaks/gitleaks（⭐30068，confidence: high）

**扫描 git 仓库、目录与 stdin 中的密码/API 密钥等秘密的工具**

`ai_role=ai-enhanced · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=idea`

Go 编写的命令行工具，通过正则规则检测 git 仓库、目录文件和 stdin 输入中的硬编码秘密。提供 git/dir/stdin 三种扫描模式，支持自定义 TOML 检测规则、基线忽略旧发现、gitleaks:allow 与 .gitleaksignore 忽略机制，支持编码文本解码（percent/hex/base64）与递归归档扫描，输出 json/csv/junit/sarif 及模板自定义报告。可安装为 pre-commit 钩子或 GitHub Action。v8.19.0 起废弃 detect/protect 命令；维护者声明不再合并新功能，后续仅发布安全补丁。

- git/dir/stdin 三种扫描模式，基于正则规则引擎检测秘密
- TOML 自定义规则，v8.28.0 引入带邻近约束的复合规则
- 基线报告忽略旧发现，支持 gitleaks:allow 与 .gitleaksignore
- 内置 json/csv/junit/sarif 报告格式及 Go 模板自定义

> L21: Gitleaks is a tool for **detecting** secrets like passwords, API keys, and tokens in git repos, files, and whatever else
> L32: Gitleaks can be installed using Homebrew, Docker, or Go. Gitleaks is also available in binary form for many popular plat
> L90: There are three scanning modes: `git`, `dir`, and `stdin`.

## trycua/cua（⭐30023，confidence: high）

**给 AI agent 提供可操作的完整桌面环境与自动化工具**

`ai_role=ai-native · license_risk=dual · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=idea`

Cua 是一套面向 computer-use agent 的基础设施：Cua Spaces 提供运行于自有 Mac/机器/云账号上的 macOS 与 Linux 桌面 Space，支持应用 Teleport 与人机多人协作；Cua Driver 提供 CLI/MCP/多语言 SDK 驱动 macOS、Windows、Linux 原生应用与浏览器；Lume 基于 Virtualization.Framework 在 Apple Silicon 上管理本地 VM；另含 CUA-S1 小型决策模型（研究发布，权重在 Hugging Face）与 Cua Bench 任务评测框架。主体 MIT 许可，Spaces 与部分 Bench 为 FSL-1.1-MIT。

- Cua Driver 支持 macOS/Windows/Linux 桌面自动化，经 CLI、MCP 或类型化 SDK 接入
- Lume 用 Apple Virtualization.Framework 在 Apple Silicon 上管理 macOS/Linux VM
- SDK 覆盖 Python/TypeScript/Swift/Kotlin，含 gVisor 容器沙箱与 cua-spacesd 守护进程
- Cua Bench 可构建任务、评测 agent 并导出训练轨迹

> L7:  Give AI agents computers they can use. Cua Spaces gives your agents full desktops on your Mac and on machines you own. 
> L69: Give your agent tools to inspect and operate native desktop apps and browsers on macOS, Windows, and Linux. Connect thro
> L141: - **SDK:** the same API in Python (`pip install cua`), TypeScript (`@trycua/cua`), Swift (`Cua`) and Kotlin (generated b

## anthropics/knowledge-work-plugins（⭐29971，confidence: high）

**面向知识工作者的 Claude 插件集（11 个职能专用插件）**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

Anthropic 开源的插件仓库，包含 11 个针对具体职能（销售、客服、产品、市场、法务、财务、数据、科研等）的插件，供 Claude Cowork 使用，亦兼容 Claude Code。每个插件捆绑 skills、connectors、slash commands 与 sub-agents，通过 MCP 服务器接入 Slack、Notion、Jira、Snowflake 等外部工具。全部组件为 markdown 与 JSON 文件，无代码、无构建步骤；支持从 claude.com/plugins 安装或经 Claude Code 市场命令安装，并可自定义或创建新插件。

- 11 个覆盖销售/法务/财务/数据等职能的插件
- skills、commands、connectors、sub-agents 的插件结构
- 通过 .mcp.json 配置 MCP 连接器接入外部工具
- 组件均为 markdown/JSON 文件，无构建步骤

> L3: Plugins that turn Claude into a specialist for your role, team, and company. Built for Claude Cowork, also compatible wi
> L9: Each plugin bundles the skills, connectors, slash commands, and sub-agents for a specific job function. Out of the box, 
> L63: - **Connectors** wire Claude to the external tools your role depends on — CRMs, project trackers, data warehouses, desig

## modular/modular（⭐29964，confidence: high）

**面向 AI 开发与部署的平台：MAX 框架 + Mojo 语言**

`ai_role=ai-ecosystem · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

该仓库托管 Modular Platform 的开源组件，覆盖 AI 开发与部署全链路：MAX 框架提供模型创作（Python）、推理服务端（OpenAI 兼容端点）、Mojo 编写的计算内核与 GPU 编程抽象、模型流水线；Mojo 语言提供编译器与标准库。README 指出正持续开源更多组件，即当前并非全部源码开放。接受两部分代码的贡献与 bug 报告，采用 Apache License v2.0，并提示用户自行核验第三方（如 Hugging Face）下载内容的许可证。

- MAX 推理服务器提供 OpenAI 兼容端点
- Mojo 编译器与标准库已开源
- MAX 内核与 GPU 编程抽象以 Mojo 编写
- Apache License v2.0 许可

> L5: This repo hosts open-source components of the Modular Platform,
> L6: a unified platform for AI development and deployment,
> L35: - MAX inference server: /max/python/max/serve

## NirDiamant/RAG_Techniques（⭐29899，confidence: high）

**为 RAG 开发者与研究者提供 42+ 可运行 notebook 的技术合集**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

以 notebook 教程形式展示检索增强生成（RAG）的各类技术，共 42+ 个可运行示例，按基础、查询增强、上下文丰富、高级检索、迭代技术、评估、可解释性、高级架构等类别组织，每个技术附文档说明、实现指引与参考文献。部分技术提供 LangChain 与 LlamaIndex 两个版本的 notebook 及可运行脚本。仓库同时包含作者的课程、书籍、Newsletter 与 YouTube 内容推广，以及赞助商展示。

- 42+ 个可运行 RAG 技术 notebook，覆盖基础到高级架构
- 每项技术附详细文档与实现指引
- 部分技术提供 LangChain 与 LlamaIndex 双版本
- 涵盖 Graph RAG、Self-RAG、CRAG、RAPTOR 等架构

> L4: A community-driven hub of **42+ runnable notebooks** covering RAG techniques from foundational to cutting-edge - the int
> L109: Retrieval-Augmented Generation (RAG) is revolutionizing the way we combine information retrieval with generative AI. Thi
> L149: > **Recently added:** MemoRAG (memory-augmented retrieval), End-to-End RAG Evaluation, Open-RAG-Eval, JSON RAG. **42 not

## huggingface/smolagents（⭐29895，confidence: high）

**面向开发者的极简 Agent 库：以代码片段作为行动形式**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

Hugging Face 维护的 Python Agent 库，核心是 CodeAgent——LLM 以 Python 代码片段形式书写动作并执行，另提供基于 JSON/文本工具调用的 ToolCallingAgent 与多 Agent 层级。模型侧通过 InferenceClientModel、LiteLLMModel、OpenAIModel、TransformersModel、AzureOpenAIModel、AmazonBedrockModel 等封装接入多类推理来源；工具可来自 MCP 服务器或 LangChain，Agent/工具可经 Hub 分享。代码执行存在安全风险，需在 E2B/Blaxel/Modal/Docker 等沙箱中运行，内置 LocalPythonExecutor 不构成安全边界。

- CodeAgent 以 Python 代码片段作为动作形式，agents.py 主代码约 1,000 行
- 支持 E2B、Blaxel、Modal、Docker 沙箱执行与本地 LocalPythonExecutor
- 模型来源可换：transformers/ollama 本地模型、Hub 提供商、LiteLLM、OpenAI 兼容服务、Azure、Bedrock
- 提供 smolagent/webagent 两个 CLI 命令与 Hub 上的 Agent/工具分享

> L10: `smolagents` is a library that enables you to run powerful agents in a few lines of code. It offers:
> L14: 🧑‍💻 **First-class support for Code Agents**. Our `CodeAgent` writes its actions in code (as opposed to "agents being use
> L18: 🌐 **Model-agnostic**: smolagents supports any LLM. It can be a local `transformers` or `ollama` model, one of many provi

## hpcaitech/Open-Sora（⭐29871，confidence: high）

**面向开发者的开源高质量视频生成模型与训练工具集**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=research`

提供 11B 参数的视频生成模型（Open-Sora 2.0），支持文生视频与图生视频，支持 256px/768px 分辨率及多种宽高比与帧长设置，并通过 torchrun 支持单卡与多卡（ColossalAI 序列并行）推理。发布 checkpoints 与完整训练代码，含数据预处理管线；提供 arXiv 技术报告与 Hugging Face Spaces 上的 Gradio demo。安装依赖 conda 环境与 Python 3.10，可选安装 flash attention 提速。

- 11B 模型一个 checkpoint 同时支持 T2V 与 I2V，覆盖 256px 与 768px
- 发布完整训练代码与 checkpoints，报告训练成本为 $200K
- 支持多分辨率、多宽高比（16:9/9:16/1:1/2.39:1）与帧长调节
- 多 GPU 推理基于 colossalai 序列并行

> L3: We design and implement **Open-Sora**, an initiative dedicated to **efficiently** producing high-quality video. We hope 
> L25: - **[2025.03.12]** 🔥 We released **Open-Sora 2.0** (11B). 🎬 11B model achieves on-par performance with 11B HunyuanVideo 
> L131: Our 11B model supports 256px and 768px resolution. Both T2V and I2V are supported by one model. 🤗 Huggingface 🤖 ModelSco

## labring/FastGPT（⭐29847，confidence: high）

**知识库问答应用构建平台：可视化工作流编排 + RAG**

`ai_role=ai-native · license_risk=dual · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

基于 LLM 的 AI Agent 构建平台，提供数据处理、RAG 检索、模型调用等开箱即用能力，并通过 Flow 可视化界面编排对话工作流与插件工作流。核心模块包括应用编排、应用调试（调用链路日志、应用评测）、知识库（多格式导入、混合检索与重排）、插件与运营（免登录分享、iframe 嵌入、对话记录标注）。支持云服务、Docker 自托管、Sealos 一键部署三种方式，另有商业版提供扩展功能与服务。

- Flow 可视化编排对话与插件工作流，含 RPA 节点与用户交互
- 知识库支持 TXT/MD/HTML/PDF/Docx/PPTX/CSV/XLSX 导入及 URL 读取
- 双向 MCP 支持与 Agent Skill 编排
- 混合检索 & 重排，对话可反馈引用并修改删除

> L12: FastGPT 是一个 AI Agent 构建平台，提供开箱即用的数据处理、模型调用等能力，同时可以通过 Flow 可视化进行工作流编排，从而实现复杂的应用场景。
> L64:  - [x] 对话工作流、插件工作流，包含基础的 RPA 节点
> L78:  - [x] 多库复用，混用

## simstudioai/sim（⭐29834，confidence: high）

**给开发者的可视化 AI agent 与工作流构建平台**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

Sim 提供一个协作工作区，用于构建、部署和管理 AI agent 与工作流：支持可视化/对话式/代码三种构建方式，内置数据库表格、文件存储、知识库，可接入 270+ 集成（5,400+ 动作、520+ 触发器），并提供运行监控、日志与调度。部署方式包括云端（sim.ai）、macOS 桌面应用（需 macOS 12+）和自托管（npx sim-setup 向导，需 Node.js 20+ 与 Docker）。自托管 Chat 服务由 Sim 管理并需 API key。

- 270+ 集成、5,400+ 动作、520+ 触发器
- 可视化/对话式/代码三种 agent 构建方式
- 内置表格数据库、文件存储与知识库（agent 共享工作区）
- 自托管安装向导 sim-setup 支持 Docker Compose、本地开发与 Kubernetes 模式

> L13:  A workspace to build, deploy and manage AI agents and workflows.
> L37: - Connect 270+ integrations (5,400+ actions, 520+ triggers) and every major LLM
> L61: **Requirements:** Node.js 20+ and Docker.

## The-Art-of-Hacking/h4cker（⭐29793，confidence: high）

**为安全从业者提供网络安全资源聚合清单**

`ai_role=ai-knowledge · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

由 Omar Santos 维护的网络安全资源聚合仓库，收录与伦理黑客、漏洞赏金、数字取证与应急响应、AI 安全、漏洞研究、漏洞利用开发、逆向工程相关的参考、脚本、工具、实验与培训材料。内容按目录组织：网络安全领域分类、AI 安全与 LLM 工程、认证路线图、自建实验室与培训参考。作为其书籍、视频课程与线下培训的补充资料，通过 MIT 许可开源，使用方式为按目标进入对应领域页面后跟随链接。

- 覆盖攻防、云与容器、应用安全、AI 安全等领域分类目录
- 含 AI 安全、LLM 工程、AI 辅助应急响应资源板块
- 认证备考资料单独分组（Cisco/CompTIA/ISC2 等）
- 提供自建实验室与 cyber range 资源章节

> L3: This repository is a comprehensive collection of cybersecurity references, scripts, tools, code, labs, and training reso
> L7: The repository serves as supplemental material for books, video courses, and live training created by Omar Santos. It in
> L12: - **AI**: ai contains AI security, LLM engineering, AI-assisted incident response and automation, and AI ethics/privacy/

## HandsOnLLM/Hands-On-Large-Language-Models（⭐29736，confidence: high）

**O'Reilly《Hands-On Large Language Models》图书代码仓库**

`ai_role=ai-knowledge · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

存放 Jay Alammar 与 Maarten Grootendez 所著《Hands-On Large Language Models》全书示例代码，按书中章节组织，配合近 300 幅自绘图示讲解 LLM 的实践工具与概念。仓库还收录补充内容（Mamba、量化、稳定扩散、MoE、推理 LLM、DeepSeek-R1 等可视化指南），并提供书籍的 BibTeX 引用条目。购书渠道覆盖 Amazon、O'Reilly、Kindle、Barnes and Noble 等平台。

- 收录全书各章节示例代码
- 提供 Mamba/量化/MoE/推理 LLM/DeepSeek-R1 等补充可视化指南
- 提供 BibTeX 学术引用条目
- 书籍在 Amazon、O'Reilly、Kindle 等多平台发售

> L3: Welcome! In this repository you will find the code for all examples throughout the book Hands-On Large Language Models w
> L7: Through the visually educational nature of this book and with **almost 300 custom made figures**, learn the practical to
> L51: **A Visual Guide to Mixture of Experts** | **A Visual Guide to Reasoning LLMs** | **The Illustrated DeepSeek-R1**

## opendataloader-project/opendataloader-pdf（⭐29730，confidence: mid）

**为 AI 数据管道解析 PDF 的开源工具：输出 Markdown/JSON/HTML**

`ai_role=ai-enhanced · license_risk=dual · deploy=library · model_dep=— · hardware=cpu-ok · install_friction=medium · maturity=—`

Python/Node.js/Java 三种 SDK 提供的 PDF 解析器：本地确定性模式用 XY-Cut++ 阅读序与边界框坐标输出 Markdown、JSON、HTML；hybrid 模式将复杂页（复杂表格、扫描件、公式、图表）路由到 AI 后端处理，内置 80+ 语言 OCR。另提供无障碍功能：将未标记 PDF 自动标记为屏幕阅读器可用的 Tagged PDF（Apache 2.0），PDF/UA-1/2 导出为企业版附加项。依赖 Java 11+。

- 输出带边界框的 JSON、Markdown 与 HTML，支持 RAG 分块与来源引用
- hybrid 模式：简单页本地处理，复杂页路由到 AI 后端
- 内置 80+ 语言 OCR，支持 EasyOCR/RapidOCR/Tesseract/ocrmac 等多种 OCR 引擎
- 自动将未标记 PDF 生成 Tagged PDF（Apache 2.0 免费层）

> L13: 🔍 **PDF parser for AI data extraction** — Extract Markdown, JSON (with bounding boxes), and HTML from any PDF. #1 in ben
> L75: |Auto-tagging → Tagged PDF for untagged PDFs|Yes|Free (Apache 2.0)|
> L76: |PDF/UA-1, PDF/UA-2 export|💼 Available|Enterprise|

## rohitg00/agentmemory（⭐29613，confidence: mid）

**给 AI 编码 agent 提供跨会话持久记忆的 MCP 服务器**

`ai_role=ai-native · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=—`

基于 iii 引擎的记忆服务：通过 12 个自动 hook 捕获 agent 会话，压缩为可检索记忆，下次会话时注入相关上下文；支持 BM25、本地向量嵌入（Xenova/all-MiniLM-L6-v2）与图结构匹配的混合检索（RRF 融合），提供 54 个 MCP 工具与 REST API。兼容支持 hooks、MCP 或 REST 的任意 agent，官方列出 20 余个适配器。无外部数据库依赖（SQLite + 内置 iii 引擎）。可配置 LLM provider 实现 LLM 压缩，也可完全 keyless 运行。

- 54 个 MCP 工具 + 12 个自动 hook，静默捕获会话并注入上下文
- BM25 + 本地向量 + 图匹配的混合检索，keyless 模式默认可用
- 20+ agent 适配器（Claude Code、Codex CLI、Cursor 等），共享同一记忆服务器
- 无外部数据库依赖，状态存于本地 SQLite + iii 引擎

> L6:  Persistent memory for Claude Code, GitHub Copilot CLI, Cursor, Gemini CLI, Codex CLI, Hermes, OpenClaw, pi, OpenCode, a
> L132: agentmemory works with any agent that supports hooks, MCP, or REST API. All agents share the same memory server.
> L236: You explain the same architecture every session. You re-discover the same bugs. You re-teach the same preferences. Built

## chroma-core/chroma（⭐29518，confidence: high）

**面向 AI 应用的开源向量/检索数据库**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

开源的 AI 数据基础设施项目，提供向量、混合与全文检索能力，支持 Python 客户端（pip）与 JavaScript 客户端（npm）接入，并可启动 client-server 模式运行。核心 API 为 4 个函数，提供内存模式便于原型开发并支持持久化。项目另提供托管服务 Chroma Cloud，以 pypi 和 npm 包形式按周发布新版本，采用 Apache 2.0 许可证。

- 提供向量、混合与全文检索
- Python（pip）与 JavaScript（npm）客户端安装
- 核心 API 仅 4 个函数，支持内存与持久化模式
- 提供 client-server 运行模式与托管服务 Chroma Cloud

> L4:  Chroma - the open-source data infrastructure for AI .
> L27: Our hosted service, Chroma Cloud, powers serverless vector, hybrid, and full-text search. It's extremely fast, cost-effe

## TencentCloud/TencentDB-Agent-Memory（⭐29487，confidence: high）

**给 AI Agent 团队用的共享记忆中枢，沉淀可复用资产**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=locked-api · hardware=— · install_friction=low · maturity=idea`

由腾讯云维护的团队级 Agent 记忆中枢：把对话、文档与代码自动转换为四类记忆资产（Chat Memory、Skill、LLM-Wiki、CodeGraph），统一注册为 Memory Asset，经 Memory Hub 面板完成审核、共享、版本与 ACL 管理，并通过一个 Proxy 按固定绑定分发给不同 Agent。对话按 L0–L3 分层蒸馏，检索采用 BM25+向量+RRF 并受条目数、字符预算与超时限制。部署为 memory-core、memory-hub、proxy 三个服务，Node 环境运行；MongoDB 存储后端为实验性且默认关闭。

- 四类记忆资产：Chat Memory、Skill、Wiki、CodeGraph，统一注册与分发
- 单 Proxy 零代码接入：改 base URL 即可，无需插件或 MCP 服务器
- L0–L3 分层记忆与 BM25+向量+RRF 混合检索
- private/team/restricted/agent 四级可见性与 ACL 权限控制

> L64: # What is TencentDB Agent Memory?
> L78: **Memory Hub** for Agent teams closes the loop across the entire experience lifecycle: work produces assets, assets circ
> L80: 1. **Automatic asset extraction**: Extract Chat Memory and Skills from conversations and tasks; convert documents and co

## alibaba/page-agent（⭐29464，confidence: high）

**网页内嵌 JS GUI agent：让任意网页支持自然语言控制**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

以页内 JavaScript 形式提供 GUI agent，通过文本化 DOM 操作执行任务，不依赖浏览器扩展、Python 或无头浏览器，也不使用截图或多模态模型；一行 script 标签或 npm 安装即可集成到任意网页。支持接入大多数主流模型（含本地部署模型），可选 Chrome 扩展支持跨页面任务，并提供 Beta 版 MCP Server 供外部 agent 客户端控制浏览器。基于 browser-use 的 DOM 处理组件与 prompt，定位为客户端网页增强而非服务端自动化。MIT 协议。

- 页内 JavaScript 集成，无需扩展/Python/无头浏览器
- 基于文本 DOM 操作，无需截图与多模态 LLM
- 支持主流模型及本地部署模型
- 提供 Chrome 扩展（多页任务）与 MCP Server (Beta)

> L14: The GUI Agent Living in Your Webpage. One script gives any web page its own AI agent.
> L28:  - Just in-page javascript. Everything happens in your web page.
> L94: `PageAgent` is designed for **client-side web enhancement**, not server-side automation.

## ATH-MaaS/Pixelle-Video（⭐29119，confidence: high）

**输入主题即自动生成配图、配音、字幕短视频的引擎**

`ai_role=ai-enhanced · license_risk=permissive · deploy=— · model_dep=local-ok · hardware=— · install_friction=medium · maturity=—`

以 Web UI（Streamlit）运行的短视频自动生成流水线：LLM 撰写文案，按句分镜后通过 ComfyUI/RunningHub 工作流或直连 API 生成图像/视频片段，TTS 合成解说（支持参考音频克隆音色），叠加 BGM 与 HTML 模板后合成成片。扩展模块含数字人口播、图生视频、动作迁移。Windows 提供整合包，macOS/Linux 需自装 uv 与 ffmpeg 从源码运行；LLM 与媒体模型均需配置 API Key 或本地服务。

- 输入主题即可完成文案→配图→语音→合成视频的全流程
- 支持 ComfyUI/RunningHub 工作流与 DashScope、OpenAI、Seedance、Kling 等直连 API 两种媒体生成路径
- TTS 支持 Edge-TTS、Index-TTS 及参考音频声音克隆
- 数字人口播、图生视频、动作迁移等扩展模块

> L15: 只需输入一个 **主题**，Pixelle-Video 就能自动完成：
> L55: - ✅ **原子能力灵活组合** - 支持 ComfyUI / RunningHub 工作流，也支持直连 API 模型，可按需替换图像、视频、TTS、VLM 等能力
> L151: ### 从源码安装（适合 macOS / Linux 用户或需要自定义的用户）

## ifixai-ai/iFixAi（⭐29073，confidence: high）

**面向 AI Agent 的独立审计 CLI，120 秒内给出合规评分**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

提供 CLI 与 IDE 插件两种形态的 AI Agent 审计工具：对被测 agent 生成对抗性探针（默认 10 项检查，全量 60 项），覆盖权限越界、提示注入、数据越权、任务偏离等行为，由独立 vendor 的 judge 模型评分，输出 JSON 与 Markdown 报告。要求 Python 3.10+，通过 pip 安装并按被测 provider 安装 extra；可引述的评分需来自不同厂商的 SUT 与 judge 两把 API key，缺第二把时只能以 --eval-mode self 做冒烟测试。

- 三种运行方式：向导式 CLI、显式 flag CLI、Claude Code/Codex 插件与任意 agent 的 skill 脚手架
- 独立 judge 评分机制：SUT 与 judge 须来自不同厂商，缺省则标记为 self-judged
- 默认 10 项检查覆盖权限、注入、数据隔离、任务保持等，全量 60 项
- Policy Lab 检查最短有害操作序列与权限修复

> L46: Is the agent doing the job it is supposed to do based on the business KPIs and Organizational Structure? iFixAi gives yo
> L148: A grade is **citable** when a second, independent provider graded your agent, not the agent
> L195: `ifixai run` runs **10 inspections** unless you ask for more. They are the `essential` suite: six

## harvard-edge/cs249r_book（⭐29053，confidence: high）

**Harvard CS249r 的 ML 系统工程四卷本开放教材与配套课程资源**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=idea`

哈佛 CS249r 课程的开源教材仓库，提供四卷 Machine Learning Systems 教材：基础、分布式扩展、Agentic 系统、物理 AI（后两卷在开发中）。除阅读材料外配套 TinyTorch（从零构建 ML 框架的 20 个模块）、交互式 Labs、MLSys·im 基础设施模拟器、硬件实验套件（Arduino/树莓派等边缘设备部署）与 StaffML 面试题库，并为教师提供 16 周教学大纲与讲义。硬拷贝将由 MIT Press 出版。支持英中日韩多语言。

- 四卷本教材覆盖单机推理到分布式扩展、agent 编排与机器人物理系统
- TinyTorch 提供从零构建 ML 框架的 20 个渐进模块
- MLSys·im 模拟器可计算内存瓶颈、网络饱和与调度上限
- 硬件套件支持在 Arduino、Seeed、Grove、树莓派上部署 ML

> L79:  Four-volume MIT Press textbook series on Machine Learning Systems Architecture:
> L100:  Deploy ML to Arduino, Seeed, Grove, and Raspberry Pi devices. Real memory limits, real power budgets, real latency.
> L121:  The AI Engineering Blueprint: two 16-week syllabi, pedagogy guide, assessment rubrics, and a TA handbook.

## dmlc/xgboost（⭐28881，confidence: high）

**面向数据科学者的分布式梯度提升树库**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=research`

XGBoost 是一个分布式梯度提升库，实现 Gradient Boosting 框架下的机器学习算法，提供并行树提升（GBDT/GBM）。同一份代码可运行在单机及 Kubernetes、Hadoop、SGE、Dask、Spark、PySpark 等分布式环境，可处理超过十亿样本规模的问题。以库形式提供，经 PyPI、Conda、CRAN 等渠道分发，支持 Python、R 等多种语言，源自华盛顿大学研究项目，基于 Apache-2 许可证发布。

- 并行树提升（GBDT/GBM）实现
- 同一代码运行于 Kubernetes/Hadoop/SGE/Dask/Spark/PySpark 等分布式环境
- 支持 Python、R、Java、Scala、C 等多语言接口
- 支持 Colab 在线运行

> L20: XGBoost is an optimized distributed gradient boosting library designed to be highly ***efficient***, ***flexible*** and 
> L23: The same code runs on major distributed environment (Kubernetes, Hadoop, SGE, Dask, Spark, PySpark) and can solve proble

## yamadashy/repomix（⭐28875，confidence: high）

**给开发者把整个仓库打包成单文件供 LLM 使用**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

一个 CLI/网站/浏览器扩展工具，将仓库内容打包为单个 AI 友好格式文件。提供 XML/Markdown/JSON/纯文本四种输出格式，统计每文件与整仓 token 数，支持 .gitignore 感知、Secretlint 凭证检测排除、Tree-sitter 代码压缩，可打包远程仓库与 stdin 文件列表。通过 npm 安装或 Docker 运行，也可在 repomix.com 网页使用，另提供 Chrome/Firefox 扩展与社区 VSCode 扩展。生成文件可发送给各类 AI 工具做代码审查、文档生成、测试用例生成等。

- 单命令打包整仓并生成 repomix-output.xml 等格式文件
- token 计数与 Tree-sitter 代码压缩（--compress）
- Secretlint 凭证格式检测并从输出中排除
- 支持远程仓库打包、git log 注入与 stdin 文件列表

> L46: 📦 Repomix is a powerful tool that packs your entire repository into a single, AI-friendly file.
> L71: - **AI-Optimized**: Formats your codebase in a way that's easy for AI to understand and process.
> L238: Once you have generated the packed file, you can use it with Generative AI tools like ChatGPT, DeepSeek, Perplexity, Gem

## mastra-ai/mastra（⭐28864，confidence: high）

**面向开发者的 TypeScript AI 应用与 Agent 框架**

`ai_role=ai-native · license_risk=dual · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Mastra 提供基于 TypeScript 的框架，用于构建 AI 应用与 Agent，覆盖从原型到生产部署的环节。关键机制包括：统一接口接入 40+ 模型提供商的模型路由、基于图的 workflow 引擎（.then/.branch/.parallel）、human-in-the-loop 暂停恢复（依赖存储保存执行状态）、上下文与记忆管理、MCP server 编写，以及内置 evals 与可观测性。可嵌入 React/Next.js/Node.js 应用或作为独立服务部署。仓库采用 Apache-2.0 与企业许可的双许可模式，`ee/` 目录代码生产使用需企业许可。

- 模型路由：单一标准接口接入 40+ 提供商（OpenAI、Anthropic、Gemini 等）
- 图式 workflow 引擎与 human-in-the-loop 暂停/恢复机制
- MCP server 编写：以标准协议暴露 agents、tools 与资源
- 内置 evals 与可观测性支持生产迭代

> L11: Mastra is a framework for building AI-powered applications and agents with a modern TypeScript stack.
> L21: - **Model routing**: Connect to 40+ providers through one standard interface. Use models from OpenAI, Anthropic, Gemini,
> L33: - **MCP servers**: Author Model Context Protocol servers, exposing agents, tools, and other structured resources via the

## srbhr/Resume-Matcher（⭐28730，confidence: high）

**本地自托管的 AI 简历定制与 ATS 优化工具**

`ai_role=ai-enhanced · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

开源简历工具：上传主简历（PDF/DOCX）与目标职位描述，生成针对该职位的定制简历、求职信与面试准备内容，并导出可被 ATS 解析的 PDF。架构为 FastAPI 后端 + Next.js 前端 + SQLite，本机运行、无需注册账号，数据存于本地数据库。支持接入云端 API 或本地模型（Ollama）；另提供 MCP 服务器，可由 Claude Code、Cursor 等编码代理驱动生成，无需 LLM key。ATS 评分与 ATS 检查为纯代码实现，不调用 LLM。定制提示词禁止添加主简历中不存在的经历。

- 主简历+职位描述生成定制简历、求职信与面试准备
- 支持云端 API 与本地模型（Ollama），数据留在本机
- ATS 评分与解析检查为纯代码（pdfminer），不调用 LLM
- 10 套模板，其中 7 套提供可编辑 pdfLaTeX 工程；多语言界面与内容生成

> L47: - **It runs on your machine.** A FastAPI backend, a Next.js frontend and a SQLite file. Clone the repo or start one Dock
> L48: - **You choose the model.** Bring an API key for OpenAI, Anthropic, Gemini, DeepSeek, OpenRouter or Groq, or run a local
> L49: - **Claude Code can drive it.** The MCP server lets Claude Code, Cursor or Codex write the tailored resume while Resume 

## invoke-ai/InvokeAI（⭐28704，confidence: high）

**面向创作者的 Stable Diffusion 本地图像生成 WebUI 与工作流工具**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Invoke 是一个基于 Stable Diffusion 系列模型的本地图像生成引擎：在本机运行 Web 服务器与 React UI，提供统一画布（内绘/外绘、笔刷工具）、节点式工作流管理与图库管理。支持 ckpt、diffusers 及部分 gguf 格式模型，覆盖 SD 1.5 至 Flux.2、Z-Image、Qwen Image 等二十余个模型，其中 Nano Banana、GPT Image、Wan 仅经 API 调用。采用商业友好许可证，通过专用 Launcher 下载安装，并作为多个商业产品的基础。

- 本地托管 Web 服务器与 React UI
- 统一画布：内绘/外绘、笔刷工具与生成能力集成
- 节点式工作流创建、管理与分享
- 支持 20+ 图像模型及 ckpt/diffusers/gguf 格式

> L9: Invoke is a leading creative engine built to empower professionals and enthusiasts alike. Generate and create stunning v
> L39: Invoke runs a locally hosted web server & React UI with an industry-leading user experience.
> L53: ### Model Support

## charmbracelet/crush（⭐28684，confidence: high）

**给开发者的终端 AI 编程 Agent，接入自选 LLM 进行代码工作**

`ai_role=ai-native · license_risk=none · deploy=library · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

一个运行在终端中的 agentic coding 工具（TUI），将用户的工具、代码与工作流接入所选 LLM。关键机制：支持通过 OpenAI 或 Anthropic 兼容 API 接入多种模型，会话中途切换 LLM 并保留上下文；每个项目可维护多个会话；利用 LSP 获取额外上下文；通过 MCP（stdio/http/sse）扩展能力。配置采用 Bash 风格的 crushrc，支持项目级与全局级；旧 JSON 配置仍支持但已标记废弃。提供 brew、winget、scoop、Nix、apt、yum、二进制包与 go install 等多种安装方式。

- 多模型接入：OpenAI/Anthropic 兼容 API，会话内切换模型保留上下文
- 利用 LSP 为决策提供额外代码上下文
- 支持 MCP 三种传输方式（stdio/http/sse）及 OAuth 授权
- crushrc（Bash 风格）配置，内置自配置技能，跨平台一致

> L7:  Your new coding bestie, now available in your favourite terminal. Your tools, your code, and your workflows, wired into
> L14: - **Multi-Model:** choose from a wide range of LLMs or add your own via OpenAI- or Anthropic-compatible APIs
> L17: - **LSP-Enhanced:** Crush uses LSPs for additional context, just like you do

## microsoft/semantic-kernel（⭐28669，confidence: high）

**为开发者提供构建 AI 智能体与多智能体系统的 SDK**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=local-ok · hardware=— · install_friction=medium · maturity=—`

Semantic Kernel 是一个模型无关的 SDK，提供 Python、.NET、Java 三语言包，用于构建、编排和部署 AI agent 与多智能体系统。关键机制包括：插件/工具扩展（原生函数、prompt 模板、OpenAPI、MCP）、多智能体编排、向量数据库集成、多模态输入处理与本地部署支持。README 顶部声明该项目已由 Microsoft Agent Framework 接替，MAF 1.0 已发布并提供迁移指南。

- 模型无关 SDK，内置接入 OpenAI、Azure OpenAI、Hugging Face、NVidia 等
- 提供 Python / .NET / Java 三语言包
- 插件扩展支持原生函数、prompt 模板、OpenAPI、MCP
- 支持 Ollama、LMStudio、ONNX 本地运行

> L17: Semantic Kernel is a model-agnostic SDK that empowers developers to build, orchestrate, and deploy AI agents and multi-a
> L4: > Semantic Kernel is now Microsoft Agent Framework! Microsoft Agent Framework (MAF) is the enterprise‑ready successor to

## QwenLM/qwen-code（⭐28539，confidence: high）

**面向开发者的终端 AI 编码 agent，支持多模型多界面**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

开源命令行 AI 编码 agent，提供终端、桌面应用、Web UI、编辑器插件与 IM 渠道等多种使用界面。内置 SubAgents、Agent Teams、Auto-Memory、Auto-Skills 与 MCP 支持，支持 OpenAI、Anthropic、Gemini、Qwen 协议及第三方本地模型，可在运行时切换。通过 npm、Homebrew 或安装脚本部署，需 Node.js 22+（npm 路径）。README 提供 SWE-bench Verified 评测数据（76.40%–77.80%）。

- 支持多协议模型接入：OpenAI/Anthropic/Gemini/Qwen API 及 Ollama/vLLM 本地模型
- 多种使用界面：终端、桌面、Web UI、VS Code/Zed/JetBrains 插件、Telegram/钉钉/微信/飞书渠道
- Headless 模式可嵌入脚本、CI/CD 与批处理，另提供 TypeScript/Python/Java SDK
- Agent Arena 支持多模型在同一任务上对比运行

> L8: **The open-source AI coding agent for your terminal, editor, desktop, browser, and chat.**
> L24: - **Multi-protocol** — Supports OpenAI, Anthropic, Gemini, and Qwen APIs. Any third-party provider or local model (Ollam
> L112: |Feature|Qwen Code|Claude Code|

## deezer/spleeter（⭐28494，confidence: high）

**为开发者提供音频音轨分离库与预训练模型**

`ai_role=ai-enhanced · license_risk=dual · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=research`

Deezer 出品的 Python 音源分离库，基于 TensorFlow，提供预训练模型：2 stems（人声/伴奏）、4 stems、5 stems 三种分离配置。可从命令行直接使用，也可作为 Python 库嵌入开发管线。依赖 ffmpeg 与 libsndfile，可通过 pip 或 Docker 安装，另提供 Google Colab 在线试用。2.1.0 版本引入 CLI 选项命名变更并移除独立 GPU 包；Apple M1 芯片存在已知兼容问题；另有商业版 Spleeter Pro。

- 提供 2/4/5 stems 三种预训练分离模型
- 支持命令行与 Python 库两种使用方式
- 可 pip 或 Docker 安装，并提供 Colab 试用
- GPU 上 4 stems 分离速度达实时 100 倍

> L8: **Spleeter** is Deezer source separation library with pretrained models
> L9: written in Python and uses Tensorflow. It makes it easy
> L20: as well as directly in your own development pipeline as a Python library. It can be installed with pip or be used with

## HumanSignal/label-studio（⭐28480，confidence: high）

**面向 ML 团队的多类型数据标注与标注工具**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

开源数据标注工具，支持对音频、文本、图像、视频、时间序列等数据类型进行标注，提供直观 UI 并可导出多种模型训练格式，用于准备原始数据或改进已有训练数据。关键机制包括：多用户账号与多项目管理、可配置的标注界面模板与专用配置语言、从 AWS S3/Google Cloud Storage 或文件导入、通过 ML SDK 连接模型后端实现预标注、在线学习与主动学习、REST API 嵌入数据流水线。限制方面：README 未提及移动端；Windows 需额外安装 wheel 依赖；Python 要求 >=3.10。

- 支持图像、音频、文本、HTML、时间序列、视频等多类型数据标注
- 通过 ML SDK 连接模型后端，支持预标注、在线学习与主动学习
- 提供 Docker、pip、poetry、Anaconda 等多种安装与部署方式
- REST API 支持嵌入现有数据流水线，前端/后端可独立集成

> L7: Label Studio is an open source data labeling tool. It lets you label data types like audio, text, images, videos, and ti
> L158: - **Integration with machine learning models** so that you can visualize and compare predictions from different models a
> L167: Connect your favorite machine learning model using the Label Studio Machine Learning SDK. Follow these steps:

## mlflow/mlflow（⭐28426，confidence: high）

**AI 工程 平台：调试/评估/监控 agent 与 LLM 应用**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

面向 agents、LLM 与 ML 模型的开源 AI 工程平台，功能包括基于 OpenTelemetry 的可观测性追踪、带 50+ 内置指标与 LLM judge 的系统化评估、带版本与血缘的 prompt 管理与自动优化、以及提供 OpenAI 兼容接口的 AI Gateway；另覆盖实验追踪、模型注册与部署等传统 ML 生命周期管理。支持 Python、TypeScript/JavaScript、Java 等语言，对 60+ 框架提供一行式自动追踪，可本地、本地集群或云平台部署。

- 基于 OpenTelemetry 的 LLM/agent 追踪可观测性，支持 60+ 框架一行接入
- 50+ 内置评估指标与 LLM judge，跟踪质量指标与回归
- AI Gateway：OpenAI 兼容统一网关，含限流、回退、凭证管理与 A/B 流量切分
- 实验追踪、模型评估、模型注册与部署（Docker/Kubernetes/Azure ML/AWS SageMaker）

> L7: MLflow is the largest open source **AI engineering platform for agents, LLMs, and ML models**. MLflow enables teams of a
> L73: MLflow provides everything you need to build, debug, evaluate, and deploy production-quality LLM applications and AI age
> L122: MLflow supports all agent frameworks, LLM providers, tools, and programming languages. We offer one-line automatic traci

## OtterMind/Chat2DB（⭐28323，confidence: high）

**连接 40+ 数据库的本地优先 SQL 客户端，支持自带 AI 模型**

`ai_role=ai-enhanced · license_risk=dual · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=idea`

面向开发者、DBA、分析师与数据团队的跨平台数据库客户端与 SQL 工作区，完全运行在本机。支持通过 JDBC 配置接入 40+ 数据库，提供 SQL 编辑、补全、格式化、执行历史、元数据浏览、DDL/DML 管理、数据导入导出、仪表盘与 ER 图。AI 部分采用自带模型（BYOM）方式：用户接入自己的模型来生成、解释和优化 SQL；开源 CLI 提供 MCP 支持。桌面版从 Releases 安装，另提供 Docker/Web 部署与源码构建路径；数据源密码与 AI API key 以 AES-256-GCM 本地加密。

- 40+ 数据库连接，新 JDBC 数据库仅靠配置即可接入
- 自带 AI 模型生成/解释/优化 SQL，开源 CLI 支持 MCP
- AES-256-GCM 本地加密数据源密码与 AI API key
- 桌面、Web/Docker、CLI 多形态分发

> L15: Chat2DB Community is a free, cross-platform database client for Windows, macOS, and Linux. It runs entirely on your mach
> L19: - **AI assistant** — bring your own AI model to generate, explain, and optimize SQL in natural language.
> L178: The Community edition contains the full local database client described above, including custom AI model support. The co

## huggingface/lerobot（⭐28250，confidence: high）

**为机器人提供模型、数据集与工具的开源库**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=research`

Hugging Face 的机器人学 PyTorch 库：提供统一的 Robot 硬件控制接口（覆盖 SO100、LeKiwi、Reachy2 等原生支持型号）、托管于 HF Hub 的 LeRobotDataset 数据格式（Parquet+MP4）及配套工具、纯 PyTorch 实现的策略模型（涵盖模仿学习、强化学习、VLA、世界模型、奖励模型五类），并提供 lerobot-train 与 lerobot-eval 训练评估脚本，支持 LIBERO、MetaWorld 基准。通过 lerobot_ 前缀包名机制自动发现社区硬件插件。面向机器人研究者与开发者。

- 统一 Robot 类接口解耦控制逻辑与硬件，原生支持 SO100、LeKiwi、Unitree G1 等设备
- LeRobotDataset 标准数据格式托管于 HF Hub，支持流式读取与可视化
- 提供五类策略模型：模仿学习、强化学习、VLA、世界模型、奖励模型
- 社区硬件插件按包名前缀自动发现与接入

> L12: **LeRobot** aims to provide models, datasets, and tools for real-world robotics in PyTorch. The goal is to lower the bar
> L47: **Supported Hardware:** SO100, LeKiwi, Koch, HopeJR, OMX, EarthRover, Reachy2, Gamepads, Keyboards, Phones, OpenARM, Uni
> L72: LeRobot implements state-of-the-art policies in pure PyTorch, covering Imitation Learning, Reinforcement Learning, Visio

## eyaltoledano/claude-task-master（⭐28237，confidence: high）

**AI 驱动的开发任务管理系统，可接入多款 AI 编辑器**

`ai_role=ai-native · license_risk=none · deploy=library · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

以 MCP 服务器与 npm CLI 两种形式运行的任务管理系统：解析 PRD 生成任务，支持任务拆分、依赖管理、状态更新、复杂度分析与研究命令，提供 36 个 MCP 工具并可按 all/standard/core/custom 模式选择性加载以控制上下文占用。需配置至少一个 AI 供应商的 API key（或 Claude Code/Codex CLI OAuth），可定义主模型、研究模型与回退模型。采用 MIT + Commons Clause 许可，禁止将其本身作为托管服务出售。

- MCP 服务器形式接入 Cursor、Windsurf、VS Code、Q CLI 等编辑器
- 36 个 MCP 工具支持 selective tool loading（all/standard/core/custom 四种模式）
- 支持主/研究/回退三类模型配置，多供应商 API key 接入
- npm CLI 提供 init 与任务管理命令

> L5:  Taskmaster : A task management system for AI-driven development, designed to work seamlessly with any AI chat.
> L76: Taskmaster utilizes AI across several commands, and those require a separate API key. You can use a variety of models fr
> L226: Task Master's MCP server supports selective tool loading to reduce context window usage. By default, all 36 tools are lo

## fastai/fastai（⭐28227，confidence: high）

**基于 PyTorch 的深度学习库：分层 API 兼顾易用与可扩展**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=research`

fastai 是构建在 PyTorch 之上的深度学习库，面向从业者提供高层组件以快速在标准深度学习领域训练模型，同时为研究者提供可组合的低层组件以构建新方法。关键机制包括 Python 类型分发系统、GPU 优化的计算机视觉库、可重构的优化器抽象、双向回调系统与 data block API。依赖 PyTorch，提供 pip/conda 安装、Colab 免安装使用与官方 Docker 容器；Windows 上 Jupyter 下 num_workers 被重置为 0，视觉任务速度受限。

- 分层 API：高层快速建模与低层可组合构件
- Python 类型分发系统与张量语义类型层级
- GPU 优化的计算机视觉库，可用纯 Python 扩展
- 双向回调系统与 data block API

> L57: fastai is a deep learning library which provides practitioners with
> L63: possible thanks to a carefully layered architecture, which expresses
> L67: underlying Python language and the flexibility of the PyTorch library.

## op7418/guizang-ppt-skill（⭐28124，confidence: high）

**给 AI Agent 用的网页 PPT 生成技能：产出单文件 HTML 演示**

`ai_role=ai-native · license_risk=viral · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

适配 Claude Code / Codex 等 Agent 环境的 Skill，生成单文件 HTML 横向翻页 PPT、配图与多平台封面。内置两套视觉系统：电子杂志风（10 种布局）与瑞士国际主义风（22 种锁定版式、4 套锚点色），含主题色预设并禁止自定义 hex。提供配图流程、演讲者模式（双窗口观众屏、备注、计时、排练）与脚本校验器。输出为无需构建与服务器、浏览器直接打开的单文件 HTML，不支持导出 PPTX。

- 双视觉系统：电子杂志风 10 种布局 + 瑞士风 22 种锁定版式
- 演讲者模式：双窗口观众屏、备注、计时排练、激光笔与故障恢复
- Codex 中可用 GPT-Image 生成配图与多平台封面
- 单文件 HTML 交付，按 B 键可退回低性能静态模式

> L16: 一个适配 Claude Code / Codex 等 Agent 环境的网页 PPT 技能,用于生成**单文件 HTML 横向翻页 PPT**、PPT 配图和多平台封面,并内置完整的排练与演讲者模式。
> L128: |Claude Code|支持|原生 Skill 工作流,适合生成和迭代 HTML deck|

## openai/skills（⭐28123，confidence: high）

**为 Codex 提供可发现、可复用的 AI agent 技能目录**

`ai_role=ai-native · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

OpenAI 维护的 Codex 技能目录仓库：技能是指令、脚本与资源的文件夹，供 AI agent 发现并用于完成特定任务。目录分为 .system（随最新版 Codex 自动安装）、.curated 与 .experimental 三类，通过 Codex 内置的 $skill-installer 按名称、文件夹或 GitHub URL 安装，安装后重启 Codex 生效。各技能的许可单独存放在其目录内的 LICENSE.txt。仓库本身已弃用，官方指向 OpenAI Plugins 仓库与 Build plugins 指南。

- 技能以指令/脚本/资源文件夹形式打包，一次编写多处使用
- .system 技能随最新版 Codex 自动安装
- 通过 $skill-installer 按名称、文件夹或 GitHub URL 安装技能
- 各技能许可独立存放于目录内 LICENSE.txt

> L4: # Agent Skills
> L8: Codex uses skills to help package capabilities that teams and individuals can use to complete specific tasks in a repeat
> L2: > **This repository is deprecated.** For current Codex skill and plugin examples, use the OpenAI Plugins repository. If 

## openai/symphony（⭐27723，confidence: mid）

**给工程团队的自主编码任务编排器：监控任务板并派发 agent 执行**

`ai_role=ai-enhanced · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=idea`

Symphony 将项目工作转化为隔离的、自主的实现运行（implementation runs），团队通过管理任务而非逐个监督编码 agent。机制上：监控 Linear 任务板，为任务生成 agent，agent 完成任务后提供工作量证明（CI 状态、PR 审查反馈、复杂度分析、演示视频），被接受后安全合入 PR。适合已采用 harness engineering 的代码库。README 标注为工程预览版，建议在可信环境中测试。提供两种获取方式：按 SPEC.md 自行实现，或使用 Elixir 参考实现。

- 监控 Linear 任务板并自动派发 agent 处理任务
- agent 提供工作量证明：CI 状态、PR 审查反馈、复杂度分析、视频
- 提供 SPEC.md 规范可自行实现，附 Elixir 参考实现
- 任务隔离运行，工程师以更高层级管理工作

> L3: Symphony turns project work into isolated, autonomous implementation runs, allowing teams to manage
> L8: _In this demo video, Symphony monitors a Linear board for work and spawns agents to handle the tasks. The agents complet
> L11: > Symphony is a low-key engineering preview for testing in trusted environments.

## QwenLM/Qwen3（⭐27678，confidence: high）

**阿里通义千问团队的开源大语言模型系列 Qwen3**

`ai_role=ai-native · license_risk=none · deploy=— · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

Qwen3 是阿里云 Qwen 团队开发的大语言模型系列，提供密集与 MoE 两种结构、0.6B 到 235B-A22B 多种规模，以及 Instruct 与 Thinking 两种 2507 变体。README 给出通过 Transformers、llama.cpp、Ollama、LM Studio、MLX 等框架运行模型的方式，并提供涵盖推理、本地运行、部署、量化（GPTQ/AWQ/GGUF）与后训练（SFT/RLHF）的文档指引。权重公开在 Hugging Face 与 ModelScope，支持 100+ 语言与 256K 上下文（可扩展至 1M token）。

- 密集与 MoE 模型，0.6B 至 235B-A22B 共 9 种规模
- Thinking/Non-thinking 两种模式变体（2507 版本各自独立模型）
- 支持 100+ 语言与 256K 长上下文，可扩展至 1M token
- 提供 Transformers、llama.cpp、Ollama、MLX 等多框架运行指引

> L40:  We are excited to announce the release of Qwen3, the latest addition to the Qwen family of large language models.
> L46:  Dense and Mixture-of-Experts (MoE) models of various sizes , available in 0.6B, 1.7B, 4B, 8B, 14B, 32B and 30B-A3B, 235
> L74: ### 🤗 Transformers

## Kilo-Org/kilocode（⭐27638，confidence: high）

**面向开发者的多形态开源编码 Agent，覆盖 IDE 与 CLI**

`ai_role=ai-native · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=—`

Kilo Code 是可在 VS Code、JetBrains 和 CLI 中使用的 AI 编码 Agent，以 MIT 协议开源。内置 Code/Plan/Ask/Debug 四类专用 Agent 并支持自定义；提供自然语言多文件代码生成、行内补全、自检、终端与浏览器控制、Marketplace 扩展（agents/skills/MCP/plugins）。可选 500+ 模型并支持任务中途切换，按模型提供方原价计费，无需预先配置 API key。另有 Web 端 Cloud Agent 与 PR 自动代码评审入口，CLI 支持 --auto 无提示自主运行于 CI/CD。CLI 由 OpenCode fork 而来。

- VS Code 扩展、JetBrains 插件、CLI 三种形态接入
- Code/Plan/Ask/Debug 四类内置 Agent，可自建自定义 Agent
- 500+ 模型可选，任务中途切换，按模型提供方原价计费
- --auto 参数支持无提示自主运行，面向 CI/CD 管线

> L5:  The open source coding agent for building with AI in VS Code, JetBrains, or the CLI.
> L16: Kilo Code is an AI coding agent that meets you everywhere you work: VS Code, JetBrains, and the CLI. It's open source wi
> L105: Kilo CLI is a fork of OpenCode, enhanced to work within the Kilo agentic engineering platform.

## Fosowl/agenticSeek（⭐27502，confidence: high）

**本地运行的自主 AI 代理：浏览网页、写代码、规划任务**

`ai_role=ai-native · license_risk=viral · deploy=desktop · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

一个完全本地运行的自主代理助手，通过本地推理模型在用户硬件上完成网页搜索、信息提取、表单填写，以及 Python/C/Go/Java 等语言的代码编写与调试；可自动选择代理并把大任务拆分为步骤执行，附带语音输入功能（标注为进行中）。运行依赖 Python 3.10.x、Docker（含 SearxNG、Redis 等服务），通过 config.ini 配置本地或云端提供商；硬件不足以本地运行 LLM 时可改用 API 方式。

- 完全本地运行，数据不离开设备，API key 对本地运行用户为可选项
- 自主网页浏览：搜索、读取、提取信息、填写表单
- 自动选择代理并拆分执行多步任务
- 支持 ollama、lm-studio、openai 兼容 API 等本地提供商

> L7: *A **100% local alternative to Manus AI**, this voice-enabled AI assistant autonomously browses the web, writes code, an
> L116: To run LLMs locally, you'll need sufficient hardware. At a minimum, a GPU capable of running Magistral, Qwen or Deepseek
> L241: By default AgenticSeek is run fully in docker.

## xai-org/grok-build（⭐27429，confidence: high）

**给开发者的终端 AI 编码 Agent（全屏 TUI）**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

SpaceXAI 的终端 AI 编码 Agent，以 Rust 编写、全屏 TUI 形式运行，能理解代码库、编辑文件、执行 shell 命令、搜索网络并管理长时任务；支持交互、无头脚本/CI 模式，以及通过 Agent Client Protocol (ACP) 嵌入编辑器。预编译二进制覆盖 macOS/Linux/Windows，也可从源码构建（Windows 构建为 best-effort）；首次启动需浏览器认证，支持 MCP 服务器、skills、插件、hooks 与沙箱。

- 全屏 TUI，支持鼠标交互
- 交互、无头（脚本/CI）与 ACP 编辑器嵌入三种运行方式
- 支持 MCP 服务器、skills、插件、hooks、沙箱
- 提供 macOS/Linux/Windows 预编译二进制

> L5: **Grok Build** is SpaceXAI's terminal-based AI coding agent. It runs as a
> L23: This repository contains the Rust source for the `grok` CLI/TUI and its agent
> L31: Prebuilt binaries are published for macOS, Linux, and Windows:

## vercel/ai（⭐27364，confidence: high）

**给 TypeScript 开发者的统一接口 AI 应用与 Agent 构建工具包**

`ai_role=ai-ecosystem · license_risk=none · deploy=library · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

Vercel 出品的 provider-agnostic TypeScript 工具库，用于构建 AI 应用与 Agent。核心机制：统一 Provider API 接入 OpenAI、Anthropic、Google 等模型提供方，默认经 Vercel AI Gateway 访问各提供方，也可安装各家的 @ai-sdk/* 包直连。提供 generateText 文本生成、基于 zod 的结构化输出、ToolLoopAgent 工具循环 Agent，以及框架无关的 UI hooks（Next.js/React/Svelte/Vue）用于构建聊天与生成式界面。要求 Node.js 22+，通过 npm 安装，并为 Claude Code、Cursor 等 coding agent 提供 skill 安装命令。

- 统一 Provider API 接入 OpenAI、Anthropic、Google 等模型提供方
- 默认经 Vercel AI Gateway 访问各主要提供方，传模型字符串即可调用
- ToolLoopAgent 构建工具循环 Agent，zod 定义结构化输出
- 框架无关 UI hooks 支持 Next.js/React/Svelte/Vue 的聊天与生成式界面

> L5: The AI SDK is a provider-agnostic TypeScript toolkit designed to help you build AI-powered applications and agents using
> L27: The AI SDK provides a unified API to interact with model providers like OpenAI, Anthropic, Google, and more.
> L29: By default, the AI SDK uses the Vercel AI Gateway to give you access to all major providers out of the box. Just pass a 

## Stability-AI/generative-models（⭐27302，confidence: high）

**Stability AI 的开源生成模型仓库：SV4D/SV3D/SVD/SDXL**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=—`

Stability AI 发布多代生成模型的官方代码库，以 News 形式按时间累积收录：SV4D 2.0（视频到 4D 新视角合成）、SV4D、SV3D（单图生成多视角轨道视频）、SDXL-Turbo、Stable Video Diffusion、SDXL 系列等，均注明面向研究用途。代码库采用配置驱动架构，通过 yaml 配置中的 instantiate_from_config() 组合子模块；训练基于 PyTorch Lightning，推理提供 streamlit demo、独立 python 脚本与社区 gradio demo。模型权重从 HuggingFace 下载，部分早期模型需通过组织邮箱申请访问。

- SV4D 2.0 视频到 4D 扩散模型：12 帧输入生成 48 帧（12 帧 x 4 视角）576x576 输出，支持自回归生成更长视频
- 低显存运行选项：--encoding_t=1、--decoding_t=1 或降低分辨率 --img_size=512
- 配置驱动的模块化代码库：yaml 配置组合子模块，guiders 与 samplers 分离且独立于模型
- 提供 streamlit demo、独立推理脚本与社区 gradio demo 多种运行入口

> L1: # Generative Models by Stability AI
> L152: Modularity is king. This repo implements a config-driven approach where we build and combine submodules by
> L157: For training, we use PyTorch Lightning, but it should be easy to use other

## t8y2/dbx（⭐27046，confidence: high）

**给开发者的 25MB 跨平台数据库管理客户端，支持 100+ 数据库**

`ai_role=ai-enhanced · license_risk=permissive · deploy=desktop · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

用 Rust 构建的轻量级开源数据库管理工具，单个约 25MB 二进制文件，无 JRE/Python/Chromium 依赖，提供 macOS、Windows、Linux 桌面端、Docker/Web 部署与 CLI。支持 100+ 数据库连接（含国产数据库达梦、人大金仓等）及消息队列/中间件控制台。内置 AI SQL 助手支持自然语言生成 SQL、解释与优化，并独立分发 MCP Server 供 AI 编码代理查询数据库，权限分 read_only/safe_write/high_risk_write 三档。另有签名沙箱插件商店与 Go/TypeScript SDK。

- 单二进制约 25MB，无 JRE、Python venv、Chromium 依赖
- 内置 AI SQL 助手，支持 Claude、OpenAI、本地模型及 OpenAI 兼容端点，AI 生成 SQL 经内置安全检查
- 独立分发的 Rust MCP Server，供 Claude Code、Cursor 等 AI 代理通过已配置连接查询数据库
- 支持消息队列与中间件控制台：Kafka、RocketMQ、RabbitMQ、Pulsar、MQTT、Nacos 等

> L1: 100+ databases in 25 MB. Desktop, Docker, CLI, built-in AI assistant, and MCP Server.
> L128:  Highlight a table, describe what you want, get SQL back — no copy-paste between tools. Works with Claude, OpenAI, or lo
> L208: DBX provides a separate Rust-powered MCP server that lets AI coding agents query databases using connections configured 

## onlook-dev/onlook（⭐26933，confidence: high）

**给设计/前端工程师的开源可视化 AI 代码编辑器**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=idea`

面向 Next.js + TailwindCSS 项目的开源可视化编辑器：在浏览器 iFrame 中直接编辑 DOM 元素并映射回代码位置，支持从文本或图像起步创建应用、实时预览、图层浏览、分支试验设计、检查点保存恢复，以及带代码访问能力的 AI 聊天。架构上把代码加载进 web 容器运行，通过插桩把元素映射到代码位置，编辑同步回代码。README 明确当前聚焦 Next.js + Tailwind，非该栈的项目尚在待办中；托管托管版处于 early access。

- 可视化编辑 iFrame 元素并同步写回代码（插桩映射元素到代码位置）
- AI 聊天具备代码读取与编辑工具
- 分支机制用于试验设计变体，支持检查点保存与恢复
- 架构声明可扩展到任何声明式 DOM 语言，目前聚焦 Next.js + TailwindCSS

> L35: # An Open-Source, Visual-First Code Editor
> L37: Craft websites, prototypes, and designs with AI in Next.js + TailwindCSS. Make
> L152: - OpenRouter - LLM model provider

## deepset-ai/haystack（⭐26756，confidence: high）

**面向 Python 开发者的 LLM 应用编排框架**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

Haystack 是一个 Python 开源编排框架，用于构建生产级 LLM 应用。提供模块化 Pipeline 与 Agent 工作流，对检索、路由、记忆、生成环节做显式控制；同一 Pipeline 支持同步/异步运行与逐 token 流式输出，Agent 可并发调用工具并暴露生命周期钩子与 token/工具调用计数。模型与厂商无关，内置组件可自建扩展，可通过 pip 或 Docker 安装，另有 Hayhooks 将流水线封装为 REST API 或 MCP 服务。

- 模块化 Pipeline 与 Agent 工作流，显式控制检索/路由/记忆/生成
- 同一 Pipeline 支持同步、异步与逐 token 流式输出，Agent 可并发工具调用
- 模型与厂商无关，可替换模型或基础设施组件
- 匿名组件级遥测，可按文档说明关闭

> L10: Haystack is an open-source AI orchestration framework for building production-ready LLM applications in Python.
> L57: Integrate with OpenAI, Mistral, Anthropic, Cohere, Hugging Face, Google, Azure OpenAI, AWS Bedrock, local models, and ma

## huggingface/open-r1（⭐26480，confidence: high）

**复现 DeepSeek-R1 训练流程的开源项目**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=local-ok · hardware=— · install_friction=high · maturity=—`

以 DeepSeek-R1 技术报告为蓝本，提供三步复现路径：蒸馏复刻 R1-Distill 模型、纯 RL 管线（R1-Zero 路径）、多阶段训练。仓库包含 SFT、GRPO 训练脚本与基于 Distilabel 的合成数据生成脚本，配套 Makefile 快捷命令与 YAML 配方。已发布 Mixture-of-Thoughts（350k）、OpenR1-Math-220k、CodeForces-CoTs 等数据集。训练默认配置为 8×H100 节点，依赖 CUDA 12.4、vLLM 0.8.5.post1、PyTorch 2.6.0，多节点经 Slurm 调度。README 声明项目已停止维护，训练部分后续由 TRL 承接。

- 提供 sft.py/grpo.py/generate.py 覆盖 R1 流水线的训练与数据生成
- 发布 350k Mixture-of-Thoughts 与 OpenR1-Math-220k 等蒸馏推理数据集
- 支持 DDP 与 DeepSpeed ZeRO-2/3，GRPO 可经 TRL vLLM 后端多节点扩展
- 代码奖励函数支持 E2B 与 Morph 两种沙箱执行提供方

> L7: *A fully open reproduction of DeepSeek-R1.*
> L25: The goal of this repo is to build the missing pieces of the R1 pipeline such that everybody can reproduce and build on t
> L103: We support training models with either DDP or DeepSpeed (ZeRO-2 and ZeRO-3). For example, to perform SFT on a dataset di

## zai-org/Open-AutoGLM（⭐26423，confidence: mid）

**基于视觉语言模型控制手机完成任务的 Phone Agent 框架**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=research`

由智谱开源的 Phone Agent 框架，通过 ADB/HDC 控制安卓或鸿蒙设备，以视觉语言模型感知屏幕截图、规划并执行点击、滑动、输入等操作，响应用户的自然语言指令。支持命令行与 Python API 两种调用方式，内置敏感操作确认与人工接管机制，提供远程 WiFi 调试。模型可用智谱 BigModel、ModelScope 等第三方 API，或通过 vLLM/SGLang 自行部署（本地部署建议 24GB+ 显存 GPU）。面向研究与学习用途。

- 通过 ADB/HDC 控制安卓与鸿蒙设备，以截图+视觉模型循环执行操作
- 支持 50+ 款 Android 中文应用与 60+ 款鸿蒙原生应用
- 提供 vLLM/SGLang 本地部署与智谱 BigModel、ModelScope API 两种模型接入方式
- 内置敏感操作确认、人工接管回调与远程 ADB/HDC 调试

> L24: Phone Agent 是一个基于 AutoGLM 构建的手机端智能助理框架，它能够以多模态方式理解手机屏幕内容，并通过自动化操作帮助用户完成任务。系统通过
> L610: - **原理**：截图 → 视觉模型理解界面 → 输出点击坐标 → ADB 执行操作 → 循环
> L642:  - 需要 NVIDIA GPU(建议 24GB+ 显存)

## WZMIAOMIAO/deep-learning-for-image-processing（⭐26414，confidence: high）

**图像处理深度学习入门教程：讲解与代码实现经典网络**

`ai_role=ai-knowledge · license_risk=viral · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

作者整理研究生期间学习内容的教程项目，以视频课程形式在 bilibili 分享。内容覆盖图像分类（LeNet 至 ConvNeXt/MobileViT）、目标检测（Faster-RCNN、SSD、YOLO 系列等）、语义分割（FCN、DeepLabV3、U-Net 等）、实例分割、关键点检测。每个网络按“结构与创新点讲解→PyTorch 搭建→TensorFlow2 搭建”三段式教学，配套 PPT 放在 course_ppt 文件夹供下载，各模型源码以目录形式组织在仓库中。

- 每个网络提供 PyTorch 与 TensorFlow2 双框架实现
- 覆盖分类、检测、分割、关键点检测四大任务方向
- 配套 bilibili 视频教程与可下载的课程 PPT
- 涵盖 LeNet 到 Swin Transformer、ConvNeXt 等多代网络

> L1: # 深度学习在图像处理中的应用教程
> L7: 2）使用Pytorch进行网络的搭建与训练
> L13: * 图像分类

## mozilla-ai/llamafile（⭐26390，confidence: high）

**把 LLM 打包成单文件分发与本地运行的开发者工具**

`ai_role=ai-ecosystem · license_risk=none · deploy=desktop · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

将 llama.cpp 与 Cosmopolitan Libc 结合，把 LLM 运行时压缩为单个可执行文件（llamafile），在多数操作系统与 CPU 架构上本地运行，无需安装；另含基于 whisper.cpp 的单文件语音转文字工具 whisperfile。0.10.0 起改用新构建系统以跟进 llama.cpp 最新模型与功能，旧版本仍可从 releases 页获取。Windows 下可执行文件有 4GB 上限，超限时需以二进制搭配外部 GGUF 权重运行。

- LLM 运行时与模型打包为单文件可执行，免安装跨平台运行
- whisperfile：单文件语音转写与翻译工具
- 0.10.0 新构建系统对齐 llama.cpp 最新版本
- 支持下载预构建 llamafile 或从源码安装

> L13: **llamafile lets you distribute and run LLMs with a single file.**
> L19: combining llama.cpp with Cosmopolitan Libc into one
> L24: llamafile also includes **whisperfile**, a single-file speech-to-text tool built on whisper.cpp and the same Cosmopolita

## datawhalechina/pumpkin-book（⭐26128，confidence: high）

**机器学习学习者的西瓜书公式推导详解笔记**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

对周志华《机器学习》（西瓜书）中较难理解的公式进行解析，并补充部分公式的推导细节，内容以本科数学基础视角表述，超纲知识以附录和参考文献给出。使用前提是读者具备西瓜书内容作为前置知识，定位为西瓜书的配套查阅资料而非独立教材。提供在线阅读、PDF 下载、B 站视频教程及组队学习资源，另有经人民邮电出版社修缮的纸质版。

- 对西瓜书公式补充推导细节与解析
- 以本科数学基础视角讲解，超纲内容附附录与参考文献
- 提供 PDF 下载、视频教程与组队学习等配套资源

> L1: 南瓜书（pumpkin-book）
> L3: “周志华老师的《机器学习》（西瓜书）是机器学习领域的经典入门教材之一，周老师为了使尽可能多的读者通过西瓜书对机器学习有所了解, 所以在书中对部分公式的推导细节没有详述，但是这对那些想深究公式推导细节的读者来说可能“不太友好”，本书旨在对西瓜
> L13: ## 配套资源

## promptfoo/promptfoo（⭐26085，confidence: high）

**为开发者提供 LLM 应用评估与红队扫描的 CLI/库**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

promptfoo 是一个用于评估与红队测试 LLM 应用的 CLI 和库：支持对 prompt、agent 与 RAG 做自动化评估，进行漏洞扫描与红队测试，并排比较多个模型，在 CI/CD 中自动执行检查，通过代码扫描审查 PR 中的 LLM 安全与合规问题。评估可 100% 本地运行，配置采用声明式 YAML 式写法，附 Web 查看器展示评估矩阵与安全报告。安装途径覆盖 npm、brew、pip，也可用 npx 免安装运行。README 声明该项目现为 OpenAI 旗下，仍以 MIT 许可开源。

- 自动化评估 prompt、agent 与 RAG 应用
- 红队测试与 LLM 漏洞扫描并生成安全报告
- 并排比较 OpenAI、Anthropic、Azure、Bedrock、Ollama 等模型
- CI/CD 集成与 PR 代码扫描审查

> L9:  <code>promptfoo</code> is a CLI and library for evaluating and red-teaming LLM-based apps. Stop using trial-and-error..
> L46: - **Test your prompts and models** with automated evaluations
> L48: - **Compare models** side-by-side (OpenAI, Anthropic, Azure, Bedrock, Ollama, and more)

## go-kratos/kratos（⭐25975，confidence: high）

**Go 微服务框架：云原生服务开发全流程支持**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

Kratos 是用于构建云原生微服务的 Go 框架，提供传输层、中间件、注册发现、配置、日志、编码与代码生成等小型显式 API。以 Protobuf 为核心做 API-first 开发，自动生成 HTTP/gRPC 代码，并通过 contrib 生态提供注册中心、配置存储、可观测性等可选集成。通过 CLI 工具创建、生成和运行服务，要求 Go 1.25+ 与 protoc 工具链，采用 MIT 许可证。

- 基于 Protobuf 生成 HTTP/gRPC 代码的 API-first 开发
- 统一 HTTP 与 gRPC 的传输层及可组合中间件（恢复、日志、校验、追踪、指标、鉴权）
- 可插拔的注册、配置与编码组件，contrib 生态提供可选集成
- CLI 工具支持服务脚手架创建、proto 代码生成与运行

> L17: Kratos is a lightweight Go framework for building cloud-native microservices. It provides small, explicit APIs for trans
> L21: - API-first development with Protobuf and generated HTTP/gRPC code.
> L33: - Go 1.25 or later

## SYSTRAN/faster-whisper（⭐25917，confidence: high）

**基于 CTranslate2 的 Whisper 语音转写推理库**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=—`

使用 CTranslate2 推理引擎重新实现的 OpenAI Whisper 语音转写库，提供 Python API 加载模型并对音频文件转写。支持 CPU 与 GPU 运行，支持 int8/fp16 量化与批量转写管线，内置 Silero VAD 过滤无语音片段，可输出词级时间戳。模型可按尺寸从 Hugging Face Hub 自动下载，也可用脚本将 Transformers 兼容的 Whisper 模型转换为 CTranslate2 格式。经 PyPI 安装，GPU 运行需另行安装 cuBLAS 与 cuDNN 9。

- 基于 CTranslate2 的 Whisper 推理，支持 int8/fp16 量化
- BatchedInferencePipeline 批量转写，接口与单条转写兼容
- 集成 Silero VAD 过滤静音段，支持词级时间戳
- 提供模型转换脚本，可加载微调后的 Whisper 模型

> L5: **faster-whisper** is a reimplementation of OpenAI's Whisper model using CTranslate2, which is a fast inference engine f
> L7: This implementation is up to 4 times faster than openai/whisper for the same accuracy while using less memory. The effic

## shap/shap（⭐25817，confidence: high）

**给机器学习模型输出提供 Shapley 值解释的 Python 库**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=—`

基于博弈论 Shapley 值，为任意机器学习模型的输出计算特征归因（SHAP 值），并提供 force plot、beeswarm、scatter、bar、dependence plot 等可视化接口。针对不同模型类型提供多种解释器：TreeExplainer（树模型精确高速 C++ 实现）、DeepExplainer 与 GradientExplainer（TensorFlow/Keras/PyTorch 深度模型近似）、LinearExplainer（线性模型）、KernelExplainer（模型无关）。以 Python 包形式发布，支持 PyPI 与 conda-forge 安装，可选 CUDA extra 启用 GPU 加速的 Tree SHAP。

- TreeExplainer 对 XGBoost/LightGBM/CatBoost/scikit-learn/pyspark 树模型提供 C++ 精确算法
- DeepExplainer/GradientExplainer 支持 TensorFlow/Keras/PyTorch 深度模型
- KernelExplainer 为模型无关方法，可解释任意函数
- TreeExplainer 支持 SHAP interaction values 的成对交互精确计算

> L10: **SHAP (SHapley Additive exPlanations)** is a game theoretic approach to explain the output of any machine learning mode
> L40: While SHAP can explain the output of any machine learning model, we have developed a high-speed exact algorithm for tree

## Cinnamon/kotaemon（⭐25809，confidence: mid）

**面向终端用户与开发者的开源 RAG 文档问答 UI**

`ai_role=ai-native · license_risk=permissive · deploy=desktop · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

提供开箱即用的 RAG 文档问答 Web UI 与供开发者构建自定义 RAG pipeline 的框架。面向想对文档做问答的终端用户和想自建 RAG 流水线的开发者。关键机制包括混合检索（全文+向量）加重排序、带 PDF 高亮预览的引用展示、多模态文档解析选项，以及可扩展的 GraphRAG 索引示例。限制方面：Python 3.10+，处理 pdf/html/mhtml/xlsx 之外的文件需另装 Unstructured，非 Docker 安装涉及较多环境配置步骤。

- 混合 RAG 流水线：全文+向量检索加重排序
- 浏览器内 PDF 引用预览与相关度分数展示
- 支持多模态文档解析与图表问答
- 提供 GraphRAG/LightRAG 等索引接入示例

> L30: This project serves as a functional RAG UI for both end users who want to do QA on their
> L43: - **Support for Various LLMs**: Compatible with LLM API providers (OpenAI, AzureOpenAI, Cohere, etc.) and local LLMs (vi
> L48: - **Framework for RAG Pipelines**: Tools to build your own RAG-based document QA pipeline.

## titanwings/distilly（⭐25719，confidence: high）

**把人物经验沉淀为可复用 Agent 技能的人物建模工具**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=idea`

从聊天记录、文档、访谈、公开资料等素材中提炼人物的经验、判断与表达方式，生成可移植、有出处依据的 Person Profile，并打包为 Agent Skill 供兼容宿主安装调用。覆盖同事、关系、名人三类人物族，各有人物素材收集策略与分析维度。支持八种 Agent 宿主的本地 Skill 发现，数据源包括 Lark、钉钉、Slack、微信（经 WeChatMsg/PyWxDump 导出）、邮件与手动上传。安装方式为将仓库克隆到宿主的 Skills 目录。README 注明当前仍为 demo 版本。

- 三类人物族（colleague/relationship/celebrity）单一工作流生成 Person Profile
- 支持 Claude Code、Codex、DeepSeek Harness 等八种 Agent 宿主的本地 Skill 发现
- 数据源覆盖 Lark/钉钉/Slack API、微信聊天记录 SQLite、PDF/邮件/Markdown 手动上传
- 生成的 Skill 支持 delta 合并、对话纠正写入 Correction 层、自动版本归档回滚

> L24: Distilly is the person-modeling layer for agents. It turns the materials you provide into a portable, source-grounded Pe
> L74: The old version only ran in Claude Code. Distilly now supports native local Skill discovery across eight agent hosts.
> L88: Each generated Person Profile is packaged as an Agent Skill and can be installed into any supported host.

## browserbase/stagehand（⭐25716，confidence: high）

**面向 agent 开发者的浏览器自动化 SDK：浏览、操作并提取网页数据**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

以 SDK 形式提供的浏览器代理工具库，提供 goto/click/locator/screenshot 等 Playwright 风格 API，并以自然语言驱动 act/observe/extract 三类操作与数据抽取；支持通过无障碍树裁剪控制 token 用量，站点变更时自愈刷新动作。提供 TypeScript、Python、Go 三种 SDK，可本地运行（需安装 Chrome），也可指向 Browserbase 云端运行并配置 Model Gateway 接入模型；另提供托管 MCP server、Search/Fetch 接口与多框架集成。MIT 协议。

- Playwright 风格 API（goto/click/locator/screenshot）加自然语言 act/observe/extract
- TypeScript、Python、Go 三语言 SDK
- 托管 MCP server 可供 Claude Code、Cursor、Codex 等 MCP 客户端使用
- Search/Fetch 支持无浏览器的网页搜索与 URL 转 markdown

> L7:  Stagehand is the SDK for browser agents
> L100:  One complete browser driver across TypeScript, Python, and Go.
> L135: The hosted Browserbase MCP server puts `navigate`, `act`, `observe`, and `extract` in any MCP client — no install, no lo

## ageron/handson-ml（⭐25603，confidence: high）

**机器学习入门者的 Python 笔记本练习集（第一版，已过时）**

`ai_role=ai-knowledge · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=medium · maturity=—`

配套 O'Reilly《Hands-on Machine Learning with Scikit-Learn and TensorFlow》第一版的 Jupyter 笔记本项目，提供书中示例代码与习题解答，用于教授 Python 机器学习基础。维护者声明该项目已过时（2017 年出版），README 顶部指向第三版 handson-ml3 与 PyTorch 版 handson-mlp。安装方式包括 Colaboratory/Binder/Deepnote 在线运行、Docker 镜像、或本地 Anaconda 环境克隆运行。

- 包含书籍示例代码与习题解答的 Jupyter 笔记本
- 支持 Colaboratory、Binder、Deepnote 在线运行
- 提供 Docker 镜像与 Anaconda 环境两种本地运行途径
- 维护者声明已过时并指向新版项目

> L7: This project aims at teaching you the fundamentals of Machine Learning in
> L8: python. It contains the example code and solutions to the exercises in my O'Reilly book Hands-on Machine Learning with S
> L5: This project is for the first edition, which is now outdated (it came out in 2017).

## lucidrains/vit-pytorch（⭐25553，confidence: high）

**为研究者提供 PyTorch 版 Vision Transformer 及多种变体实现**

`ai_role=ai-enhanced · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

以 PyTorch 库形式实现的 Vision Transformer（ViT）图像分类模型，通过 pip 安装后在 Python 中以 `from vit_pytorch import ViT` 方式使用。核心是单一 transformer encoder 结构，参数覆盖 image_size、patch_size、depth、heads、mlp_dim、dropout 等。除基础 ViT 外，还收录 Simple ViT、NaViT、DistillableViT、Deep ViT、CaiT、CCT、Cross ViT、MaxViT、MobileViT 等数十种论文变体的实现，各变体以独立子模块导入，附对应用法代码示例。

- 提供基础 ViT 实现及 image_size/patch_size/depth/heads 等参数配置
- 收录数十种 ViT 论文变体：Simple ViT、NaViT、CaiT、CCT、CrossViT、MaxViT、MobileViT 等
- 支持从卷积网络（如 Resnet50）到 ViT 的蒸馏训练（DistillableViT，可 `.to_vit` 转回 ViT）
- pip 一条命令安装，各变体独立子模块导入

> L7: Implementation of Vision Transformer, a simple way to achieve SOTA in vision classification with only a single transform
> L20: $ pip install vit-pytorch
> L27: from vit_pytorch import ViT

## microsoft/OmniParser（⭐25529，confidence: high）

**为视觉 GUI Agent 解析界面截图的结构化工具**

`ai_role=ai-native · license_risk=dual · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=research`

微软发布的屏幕解析工具：将用户界面截图解析为结构化、易于理解的元素，供 GPT-4V 等视觉模型将动作准确定位到界面区域。配套 OmniTool 可用视觉模型控制 Windows 11 虚拟机，支持 OpenAI、DeepSeek、Qwen 与 Anthropic Computer Use 等模型。提供交互区域检测模型（YOLOv9-E）与图标功能描述模型，权重托管于 Hugging Face；通过 conda/pip 安装，附带 Gradio demo 与 demo.ipynb 示例。

- 将 UI 截图解析为结构化可交互元素
- 交互区域检测模型（YOLOv9-E）与图标描述模型（Florence caption）
- OmniTool 支持接入多家视觉模型控制 Windows 11 VM
- Hugging Face Space 在线 demo 与 gradio_demo.py 本地 demo

> L1: # OmniParser: Screen Parsing tool for Pure Vision Based GUI Agent
> L10: **OmniParser** is a comprehensive method for parsing user interface screenshots into structured and easy-to-understand e
> L17: - [2025/2] We introduce OmniTool: Control a Windows 11 VM with OmniParser + your vision model of choice. OmniTool suppor

## toon-format/toon（⭐25508，confidence: high）

**为 LLM 提示词设计的紧凑 JSON 序列化格式，降低 token 消耗**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

定义了一种对 JSON 数据模型的紧凑、人类可读编码格式（SPEC v4.4）：用缩进替代大括号、对同构数组/键值集合采用表头声明一次的表格形式，提供长度 [N] 与字段 {fields} 声明以便模型解析与校验，并支持无损往返转换。附带 TypeScript SDK、CLI（npx @toon-format/cli，可统计 token 节省量）与基准测试：244 个数据检索问题、4 个模型，含按数据集与问题类型的准确率对比表。README 同时列出适用边界：深层嵌套或非同构数据、纯表格数据（CSV 更小）、延迟敏感场景不适用。MIT 许可。

- JSON 数据模型的无损、确定性往返编码
- 表格形式对同构数据声明一次字段列表，逐行输出
- [N] 行数与 {fields} 字段声明提供截断/畸形输出防护
- 附 CLI（npx 免安装试用）与多模型、多格式基准测试

> L11: **Token-Oriented Object Notation** is a compact, human-readable encoding of the JSON data model that minimizes tokens an
> L15: Think of it as a translation layer: use JSON programmatically, and encode it as TOON for LLM input – a drop-in, lossless
> L90: - 🌐 **Multi-Language Ecosystem:** Official implementations, plus dozens of community ports, all targeting one spec with 

## mxgmn/WaveFunctionCollapse（⭐25402，confidence: mid）

**从单个示例图生成局部相似位图与瓦片地图的程序**

`ai_role=ai-knowledge · license_risk=none · deploy=desktop · model_dep=— · hardware=— · install_friction=medium · maturity=—`

用 C# 编写的控制台程序，读取输入位图并统计 NxN 图案，通过观察-传播循环生成与输入局部相似的位图或瓦片地图；仅依赖标准库，通过 .NET Core 以 dotnet run 构建，输出写入 output 文件夹，参数经 samples.xml 配置。可用的另一种途径包括 Windows 官方 release、itch.io 图形版与浏览器运行。README 记录该算法已被移植到十余种语言与 Unity/Unreal/Godot 等引擎，并被多款游戏用于生成关卡；同时说明算法可能陷入矛盾而无法继续（判定问题为 NP-hard）。

- 以观察-传播循环生成与输入局部相似的位图，输出只含输入中出现过的 NxN 图案
- 支持瓦片模型：以瓦片列表与邻接数据初始化，含瓦片对称性系统以缩短邻接枚举
- 支持约束条件，可与人工创建或其他生成算法组合使用
- 支持更高维度（体素模型）与时间维

> L2: This program generates bitmaps that are locally similar to the input bitmap.
> L14: WFC initializes output bitmap in a completely unobserved state, where each pixel value is in superposition of colors of 
> L68: 1. Read the input bitmap and count NxN patterns.

## fastai/fastbook（⭐25392，confidence: high）

**以 Jupyter Notebook 形式发布的 fastai 深度学习教材**

`ai_role=ai-knowledge · license_risk=dual · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=research`

《Deep Learning for Coders with fastai and PyTorch》一书的 Notebook 版仓库，内容覆盖深度学习入门、fastai 分层 API 与 PyTorch，包含从 MNIST 基础到 NLP、卷积、优化器与回调等 20 章内容。代码部分采用 GPL v3 许可，散文部分（markdown 单元格）不允许再分发或商业使用，仅可自用复制或 fork。面向学习深度学习的读者，推荐通过 Google Colab 在浏览器中直接运行，无需本地搭建 Python 环境。

- 以 Jupyter Notebook 形式提供全部章节内容
- 覆盖深度学习、fastai 与 PyTorch 入门，含 20 章
- 支持通过 Google Colab 在浏览器中打开运行
- 代码部分采用 GPL v3 许可，配套 MOOC 课程

> L3: # The fastai book
> L5: These notebooks cover an introduction to deep learning, fastai, and PyTorch. fastai is a layered API for deep learning; 

## liguodongiot/llm-action（⭐25179，confidence: mid）

**大模型工程化与实践教程合集：覆盖训练、推理、压缩、评测**

`ai_role=ai-knowledge · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

以文章目录形式组织的大模型工程化知识库，内容按 LLM 训练、推理、压缩、测评、数据工程、提示工程、算法架构、应用开发等章节编排。训练部分汇总从 6B 到 65B、覆盖全量微调与 LoRA/QLoRA/P-Tuning v2 等高效微调及 RLHF 的实战教程；推理部分列出 vLLM、SGLang、TensorRT-LLM 等引擎与优化技术文章；另含分布式训练并行技术系列与量化/剪枝/蒸馏原理讲解。各条目多为外链教程，部分附带配套代码。

- 覆盖 6B–65B 模型的全量微调、LoRA/QLoRA/P-Tuning v2 与 RLHF 实战教程
- 九篇分布式训练并行技术系列（数据/流水线/张量/序列/自动并行等）
- 推理引擎汇总：vLLM、SGLang、TensorRT-LLM、LMDeploy 及轻量实现
- 量化（GPTQ/AWQ/SmoothQuant 等）、剪枝、知识蒸馏原理系列文章

> L6: ## LLM训练
> L120: ## LLM推理
> L182: ## LLM压缩

## letta-ai/letta（⭐25171，confidence: high）

**构建可跨会话记忆并自我改进的有状态 AI agent 平台**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

Letta（前名 MemGPT）提供有状态 agent 开发平台：agent 具备持久记忆，可在多次交互中学习并自我改进。当前源码位于 letta-code 仓库，包含 agent harness、终端交互 UI、App Server、多渠道接入与运行时。安装后通过 `letta` 命令启动终端 UI，`letta server` 运行本地或自托管的 agent 服务；另提供 macOS/Windows/Linux 桌面应用、网页端、Slack/Telegram/Discord 渠道、TypeScript SDK 与云托管服务。archive 分支保留已退役的 V1 API 服务器。

- agent 具备持久记忆，支持跨会话学习与自我改进
- npm 全局安装后提供终端交互 UI 与本地/自托管 App Server
- 支持桌面应用、网页端、Slack/Telegram/Discord 等多渠道接入
- 提供 TypeScript Agent SDK 与 Letta Cloud 云端服务

> L3: Build stateful agents with memory that can learn and improve over time.
> L29: - the desktop app for macOS, Windows, and Linux
> L32: - the Letta Agent SDK for building agents into TypeScript applications

## activepieces/activepieces（⭐25083，confidence: high）

**开源 AI 工作流自动化平台：为 AI 代理提供 MCP 工具集**

`ai_role=ai-native · license_risk=dual · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Activepieces 是用 TypeScript 编写的可扩展自动化平台，通过类型安全的 pieces 框架提供 200+ 集成（如 Google Sheets、Discord、RSS），覆盖循环、分支、重试、HTTP、代码块等构建器功能，并提供无代码构建器供非技术用户使用。所有 pieces 自动可作为 MCP server 供 LLM 客户端调用；内置原生 AI pieces 与 AI SDK 用于创建 agent 和构建流程，支持人工审批、延迟执行、聊天/表单人工输入触发。社区版 MIT 许可，企业功能采用商业许可。

- 280+ pieces 自动作为 MCP servers，供 Claude Desktop、Cursor、Windsurf 等 LLM 客户端使用
- 原生 AI pieces 与 AI SDK，可在构建器内创建 agent
- TypeScript pieces 框架，npm 包形式发布，支持本地开发热重载
- 支持人工审批、延迟执行与聊天/表单人工输入触发

> L39: All-in-one AI automation designed to be **extensible** through a **type-safe** pieces framework written in **TypeScript*
> L48: - **🛠️ Largest open source MCP toolkit**: All our pieces (280+) are available as MCP that you can use with LLMs on Claud
> L52: - **🤖 AI-First**: Native AI pieces let you experiment with various providers, or create your own agents using our AI SDK

## flipped-aurora/gin-vue-admin（⭐25076，confidence: high）

**为 Go+Vue 全栈开发者提供带 AI 辅助的后台开发基础平台**

`ai_role=ai-enhanced · license_risk=dual · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

基于 Gin 与 Vue 的前后端分离基础平台，内置 JWT 鉴权、Casbin 权限管理、动态路由与菜单、代码生成器、表单生成器、分页封装、多点登录拦截、文件上传下载（七牛云/阿里云/腾讯云）等后台开发常用功能。AI 相关机制包括：高度适配 AI 编辑器的 MCP 服务、AI 生成结构并生成基础 CRUD 代码的一分钟流程、内置 skills 管理，支持 TS 和 JS 混用。以源码方式运行，另提供商业授权版。

- 高度适配 AI 编辑器的 MCP，可由 AI 生成结构、代码与权限分配
- 内置 skills 管理，支持 TS 和 JS 混用
- 基于 jwt 与 casbin 的权限管理及动态路由/菜单
- 代码生成器、表单生成器与可配置的导入导出

> L7: ## 支持 Claw 生态
> L13:  ⭐️ 高度适配AI编辑器的MCP
> L56: > Gin-vue-admin是一个基于 vue 和 gin 开发的全栈前后端分离的开发基础平台，集成jwt鉴权，动态路由，动态菜单，casbin鉴权，表单生成器，代码生成器等功能，提供多种示例文件，让您把更多时间专注在业务开发上。

## trekhleb/homemade-machine-learning（⭐24826，confidence: high）

**为学习者提供从零实现的经典机器学习算法示例与交互演示**

`ai_role=ai-knowledge · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

该仓库以 Python 从零实现流行机器学习算法，每个算法附数学原理讲解与交互式 Jupyter Notebook 演示，可在浏览器中调整训练数据与算法配置并查看结果、图表与预测。内容覆盖监督学习（线性/逻辑回归）、无监督学习（K-means、高斯异常检测）与多层感知机，讲解多基于 Andrew Ng 的机器学习课程。作者明确声明这些实现不用于生产环境。

- 从零实现算法并配数学原理讲解，基于 Andrew Ng 课程
- 每个算法提供交互式 Jupyter Notebook 演示，浏览器内即可运行
- 覆盖回归、分类、聚类、异常检测与多层感知机
- 提供 NBViewer 在线预览与 Binder 在线执行入口

> L22: > This repository contains examples of popular machine learning algorithms implemented in **Python** with mathematics be
> L24: The purpose of this repository is _not_ to implement machine learning algorithms by using 3 rd party library one-liners 

## NirDiamant/GenAI_Agents（⭐24610，confidence: high）

**面向学习者的 50+ 生成式 AI Agent 教程与实现合集**

`ai_role=ai-ecosystem · license_risk=none · deploy=— · model_dep=local-ok · hardware=— · install_friction=medium · maturity=—`

以教程/笔记本形式组织的生成式 AI Agent 合集，按初学者、框架、教育、商业、创意、分析、新闻等分类收录 57 个实现，每个条目标注所用框架（LangChain、LangGraph、PydanticAI、AutoGen、CrewAI 等）与关键功能，涵盖对话机器人、多智能体协作、RAG Agent、任务与内容生成等。仓库还提供作者付费课程、newsletter、YouTube 讲解频道及配套项目（RAG Techniques、Agent Memory Techniques 等），接受社区贡献。

- 57 个按类别组织的 Agent 教程实现，标注框架与功能
- 覆盖 LangChain、LangGraph、PydanticAI、AutoGen、CrewAI 等框架
- 从简单对话代理到多智能体系统的渐进式学习路径
- 接受社区贡献并持续更新条目

> L9: Welcome to one of the most extensive and dynamic collections of Generative AI (GenAI) agent tutorials and implementation
> L135: |#|Category|Agent Name|Framework|Key Features|
> L137: |1|🌱 **Beginner**|Simple Conversational Agent|LangChain/PydanticAI|Context-aware conversations, history management|

## nocobase/nocobase（⭐24607，confidence: high）

**AI + 无代码平台：快速搭建企业业务系统**

`ai_role=ai-enhanced · license_risk=none · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

开源无代码平台，以数据模型驱动方式提供内置的数据建模、权限、工作流与审计日志模块。AI 侧包含两类机制：一是与主流编码 Agent 配合的 CLI 与 skills，使 AI 可承担部署、开发、迁移、发布；二是运行在系统内的 AI 员工，接入业务工作流执行表单填写、文档识别、任务路由等任务。所有 AI 操作遵循与人类用户相同的细粒度权限，并记录审计日志。通过 MCP、HTTP API、CLI 开放接口连接外部 Agent 平台。数据保存在用户自有数据库中，插件采用微内核架构。

- AI 编码代理（Claude Code、Cursor、Codex、OpenCode、TRAE）通过 CLI 与 skills 端到端处理部署、开发、迁移、发布
- 系统内 AI 员工自动获取业务上下文并执行前端分析与后端任务
- MCP、HTTP API、CLI 标准接口连接 OpenClaw、Hermes、Dify、Coze、n8n 等平台
- 数据模型、权限、工作流、审计日志开箱即用，微内核插件架构

> L12: NocoBase is an open-source AI + no-code platform for building business systems fast. Instead of generating everything fr
> L49: Coding agents get a full CLI and skills, while people get a WYSIWYG no-code interface, so both can collaborate efficient
> L82: NocoBase includes AI employees, so AI can work directly inside the system.

## plotly/dash（⭐24455，confidence: mid）

**用纯 Python 构建数据应用与仪表盘的 Web 框架**

`ai_role=ai-ecosystem · license_risk=dual · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

基于 Plotly.js、React 与 Flask 的 Python 框架，将下拉框、滑块、图表等 UI 元素直接绑定到分析代码，声明式响应式编写交互应用，无需写 JavaScript。README 给出下拉联动图表、交叉筛选、Mapbox 地图、PDF 风格财务报告等示例。开源版在本地运行；另提供 Dash Enterprise 商业版，含部署、Kubernetes 扩缩、认证、任务队列、低代码组件与 GPU/Dask 加速等功能。

- 纯 Python 编写交互式数据 Web 应用，无需 JavaScript
- 基于 Plotly.js，支持约 50 种图表类型（含地图）
- 声明式响应式代码模型，示例含交叉筛选应用
- 提供 Dash Enterprise 版本（部署/认证/任务队列/低代码组件）

> L9: #### *Dash is the most downloaded, trusted Python framework for building ML & data science web apps*.
> L11: Built on top of Plotly.js, React and Flask, Dash ties modern UI elements like dropdowns, sliders, and graphs directly to
> L32: ### Dash OSS & Dash Enterprise

## guillaumemeyer/watermarks-remover（⭐24313，confidence: mid）

**给内容所有者去除多厂商 AI 水印/溯源标记的 agent skill 与本地服务**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=self-host · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

由 agent skill（纯 Markdown 薄客户端，经 HTTP 调用）与 Python stdlib 服务两部分组成，用于清除用户自有内容中的 AI 溯源标记。分三层：A 层确定性脚本清理不可见 Unicode/bidi/标签字符；B 层借助模型改写处理统计型文本水印（可选）；文件层读取 C2PA/EXIF/XMP/文档属性，覆盖 PNG、JPEG、PDF、DOCX、MP4 等多种格式。支持安装到 Claude Code、Codex、Cursor、Grok 等宿主，并提供 Claude Code PostToolUse hook 与 pre-commit 门禁实现确定性清理。需 Python 3.10+；hook 无法改写聊天消息本身。

- 三层清理：不可见 Unicode（确定性脚本）、统计型文本水印（模型改写）、文件元数据（C2PA/EXIF/XMP）
- skill 为无代码 HTTP 薄客户端，宿主无需 Python；服务仅需 Python 3.10+ stdlib 无依赖
- 支持 Claude Code/Codex/Cursor/Cowork/Grok 多宿主安装，含 Claude Code plugin marketplace 一键安装
- PostToolUse hook 提供确定性 check/clean 两种模式，并支持 pre-commit 门禁与 SARIF 导出

> L14: Agent skill + stdlib Python service to strip **multi-vendor AI provenance marks** from text and files — for privacy and 
> L37: (Python 3.10+ stdlib, no dependencies):
> L22: Vendors / ecosystems (class-level): **Claude**, **Gemini / SynthID-Text**, **OpenAI** provenance surfaces, **open-LLM** 

## deepseek-ai/DeepSeek-Coder（⭐24292，confidence: mid）

**面向开发者的开源代码大模型系列（1B-33B）**

`ai_role=ai-native · license_risk=dual · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=research`

DeepSeek Coder 是一系列从零训练的代码语言模型，训练语料 2T tokens，其中 87% 为代码、13% 为中英文自然语言。模型提供 1B、5.7B、6.7B、33B 多个规模，采用 16K 窗口与 fill-in-the-blank 任务训练，支持项目级代码补全与填充。提供 Base 与指令微调的 Instruct 两类模型，附 Hugging Face transformers 推理示例、vLLM 高吞吐推理路径、微调脚本及 llama.cpp/GPTQ 量化问答。代码仓库为 MIT 许可，模型使用另有 Model License，声明支持商业使用。

- 1B/5.7B/6.7B/33B 多规模模型，87% 代码 + 13% 中英文语料从零训练
- 16K 窗口与 fill-in-the-blank 任务支持项目级代码补全与填充
- 提供 finetune_deepseekcoder.py 微调脚本，支持 DeepSpeed 训练
- 支持 vLLM 高吞吐推理及 GGUM/GPTQ 量化路径

> L11: DeepSeek Coder is composed of a series of code language models, each trained from scratch on 2T tokens, with a compositi
> L17: - **Highly Flexible & Scalable**: Offered in model sizes of 1B, 5.7B, 6.7B and 33B, enabling users to choose the setup m
> L167: ### Inference with vLLM

## PaddlePaddle/Paddle（⭐24126，confidence: high）

**深度学习框架，支持分布式训练与跨平台部署**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

源自产业实践的深度学习平台，2016 年开源，覆盖核心框架、模型库、端到端开发套件与组件。3.x 版本支持动/静统一图与自动并行（单卡配置注解自动推导分布式策略）、大模型训练与推理一体化、高阶自动微分用于科学计算、神经网络编译器，以及多硬件芯片的统一适配方案。提供中英文文档与社区贡献渠道，采用 Apache-2.0 许可证。

- 动/静统一图与自动并行分布式训练策略
- 大模型训练与推理同一框架、代码复用
- 高阶自动微分支持科学计算（微分方程求解）
- 多芯片异构适配，标准化接口抽象不同硬件栈

> L11: PaddlePaddle, as the first independent R&D deep learning platform in China, has been officially open-sourced to professi
> L24: ## **PaddlePaddle New Generation Framework 3.2**
> L28:  By requiring only minimal tensor partitioning annotations based on a single-card configuration, PaddlePaddle automatica

## pyg-team/pytorch_geometric（⭐24124，confidence: high）

**基于 PyTorch 的图神经网络库，面向结构化数据**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=—`

构建在 PyTorch 之上的库，用于编写和训练图神经网络（GNN），覆盖结构化数据相关应用。收录来自多篇已发表论文的图与不规则结构深度学习方法（几何深度学习）；提供小图与巨型图的 mini-batch 加载器、多 GPU 支持、torch.compile 与 DataPipe 支持、常见基准数据集接口，以及面向任意图、3D 网格与点云的变换。架构分为 engine、storage、operators、models 四层，GNN 层基于 nn.MessagePassing 接口实现，面向机器学习研究者与初学者。

- 通过 MessagePassing 接口实现数十种论文发表的 GNN 层（GCN、GAT、SAGE、GIN 等）
- 支持大规模图训练：百万级节点图、动态图、异构图，提供多种采样方案
- 多 GPU、torch.compile、TorchScript 与 DataPipe 支持
- 10-20 行代码即可完成一个 GNN 模型训练，附带 Colab 笔记本与 OGB 示例

> L13: **PyG** *(PyTorch Geometric)* is a library built upon PyTorch to easily write and train Graph Neural Networks (GNNs) for
> L84: - The PyG **engine** utilizes the powerful PyTorch deep learning framework with full `torch.compile` and TorchScript sup
> L94: All Graph Neural Network layers are implemented via the **`nn.MessagePassing`** interface.

## AccumulateMore/CV（⭐24045，confidence: high）

**中文自学者的深度学习与大模型课程笔记合集**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

以 Jupyter Notebook 形式整理的中文深度学习学习笔记，覆盖四个视频课程系列：土堆 Pytorch（100-122 号笔记）、李沐动手学深度学习（200-268）、吴恩达深度学习（300-354）、大飞大模型 Agent（400-409），并预告另一 Agent 系列待上线。附百度网盘分享的数据集、在线观看图片/公式显示问题的说明、Jupyter Notebook 目录插件建议及自学交流群。面向中文自学入门者，仓库本身不含代码工程或安装流程。

- 四套视频课程的中文笔记（PyTorch、李沐、吴恩达、大模型 Agent）
- 以 Jupyter Notebook 组织，可在线阅读或下载本地查看
- 附百度网盘数据集分享与交流群入口

> L1: # 超级全面的 深度学习 笔记（包含CV、NLP、大模型、Agent）
> L5: Pytorch 视频讲解【主讲人：土堆】【对应笔记：100-122】
> L17: 大模型Agent 视频讲解【主讲人：大飞】【对应笔记：400-409】

## deepseek-ai/DeepSeek-OCR（⭐24019，confidence: high）

**面向研究者的视觉文本压缩 OCR 模型**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=local-ok · hardware=— · install_friction=medium · maturity=research`

DeepSeek AI 发布的开源模型，探索从 LLM 中心视角研究视觉编码器的作用，将文本上下文以视觉形式压缩表示。提供 vLLM 与 Transformers 两条推理路径，支持图片流式输出、PDF 处理与基准批量评测，提供 5 种分辨率模式（Tiny 至 Gundam 动态分辨率）与文档转 Markdown、OCR、Free OCR 等 prompt 模板。模型权重发布于 Hugging Face，环境依赖 CUDA 11.8 与 torch 2.6.0，README 注明 vLLM/transformers 同环境安装可能报依赖版本冲突。

- 支持 vLLM 与 Transformers 两条推理路径
- 5 种分辨率模式：512×512 至动态 Gundam 模式
- 提供文档转 Markdown、OCR、Free OCR 等 prompt 模板
- 已获上游 vLLM 官方支持

> L23:  DeepSeek-OCR: Contexts Optical Compression
> L30: - [2025/10/20]🚀🚀🚀 We release DeepSeek-OCR, a model to investigate the role of vision encoders from an LLM-centric viewpo
> L104: The current open-source model supports the following modes:

## Tencent/ncnn（⭐23969，confidence: high）

**面向移动/嵌入式/桌面端部署的神经网络推理框架**

`ai_role=ai-ecosystem · license_risk=none · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=—`

ncnn 是腾讯开源的神经网络推理框架，无第三方运行时依赖，支持 CPU 与 Vulkan GPU 后端，提供 C++ API 与 Python 绑定。通过 pnnx 工具将 PyTorch 和 ONNX 模型转换为 ncnn 格式，并保留 Caffe/MXNet/Darknet 等旧格式转换器。支持 int8 量化、fp16 计算、自定义层与模型优化工具。提供覆盖 Android、iOS、Windows、Linux、WebAssembly 等平台的预编译包，也可从源码构建。已在 QQ、微信等腾讯应用中使用，覆盖分类、检测、分割、OCR 等模型类型。

- 无第三方运行时依赖，纯 C++ 实现，提供 C API 与 Python 绑定
- CPU（ARM NEON、多核调度）与 Vulkan GPU 两种推理后端
- pnnx 工具完成 PyTorch/ONNX 模型转换，支持 int8 量化与 fp16
- 提供 Android/iOS/WebAssembly/HarmonyOS 等多平台预编译包与构建指南

> L9: ncnn is a high-performance neural network inference framework optimized for mobile, embedded, and desktop deployment.
> L10: It has no third-party runtime dependencies, runs across CPU and Vulkan GPU backends, and provides tools such as pnnx for
> L181: - Optimized CPU inference for mobile and embedded processors, including ARM NEON and multi-core scheduling.

## sinaptik-ai/pandas-ai（⭐23886，confidence: high）

**用自然语言对话查询数据库与数据文件的 Python 库**

`ai_role=ai-native · license_risk=dual · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

PandasAI 是一个 Python 库，通过 LLM 让用户以自然语言向数据提问，支持 SQL、CSV、parquet 等数据源。定位为帮助非技术用户以更自然的方式与数据交互，也帮助技术用户节省时间。提供 df.chat 接口提问、生成图表、多 DataFrame 关联问答；可通过 pandasai-docker 在 Docker 沙箱中隔离执行生成的代码。安装依赖 Python 3.8–3.11，pip 或 poetry 安装，LLM 接入经 pandasai-litellm 扩展包。仓库 ee 目录另有单独许可。

- df.chat 自然语言提问数据并返回文本答案
- 按自然语言指令生成图表（直方图等）
- 多个 DataFrame 关联查询
- Docker 沙箱隔离执行代码（pandasai-docker）

> L11: PandasAI is a Python library that makes it easy to ask questions to your data in natural language. It helps non-technica
> L93: You can run PandasAI in a Docker sandbox, providing a secure, isolated environment to execute code safely and mitigate t

## lukasmasuch/best-of-ml-python（⭐23849，confidence: mid）

**给 ML 开发者的 Python 库排名清单，每周更新**

`ai_role=ai-knowledge · license_risk=viral · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

以自动化方式维护的机器学习 Python 开源项目目录：收录 920 个项目、划分为 34 个类别，按从 GitHub 与包管理器自动采集的指标计算项目质量分并排序。条目附星数、贡献者/下载/依赖数量、活跃状态、许可证警告等标记，并给出各库的 git clone、pip、conda、docker 安装命令。内容每周自动更新，社区可通过 issue、PR 或直接编辑 projects.yaml 参与维护。

- 收录 920 个开源项目，分 34 个类别，基于质量分自动排序
- 指标自动采集自 GitHub 与多个包管理器，每周更新
- 条目标注关联生态（TensorFlow/PyTorch/JAX/Pandas 等）与活跃度、许可证警告
- 支持通过编辑 projects.yaml 直接贡献条目

> L3:  🏆&nbsp; A ranked list of awesome machine learning Python libraries. Updated weekly.
> L5: This curated list contains 920 awesome open-source projects with a total of 5.1M stars grouped into 34 categories. All p

## coleam00/Archon（⭐23702，confidence: mid）

**为 AI 编码 agent 提供可复现 YAML 工作流引擎的开发者工具**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=desktop · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

Archon 是面向 AI 编码 agent 的工作流引擎：开发者把计划、实现、验证、代码评审、PR 创建等开发流程定义为 YAML 工作流，由引擎确定性执行，AI 仅在各步骤填充智能内容。支持确定性节点（bash 脚本、测试、git 操作）与 AI 节点组合，可在独立 git worktree 中运行，并提供 CLI、Web UI 及 Telegram/Slack/Discord/GitHub 等平台接入。安装依赖 Bun、Claude Code 与 GitHub CLI；提供 curl 安装脚本、Homebrew 与源码安装途径，附带 sdlc 工作流包与匿名遥测。

- 以 YAML 定义开发流程工作流，含阶段、验证门与产物
- 确定性节点与 AI 节点可混合编排
- 支持 CLI、Web UI、Slack、Telegram、Discord、GitHub 触发运行
- 内置 sdlc 工作流包（archon-ship/triage/investigate/review 等 10 个）

> L13: Archon is a workflow engine for AI coding agents. Define your development processes as YAML workflows - planning, implem
> L26: - **Composable** - Mix deterministic nodes (bash scripts, tests, git ops) with AI nodes (planning, code generation, revi
> L129: Release binaries ship without AI providers. The quick installers ask which of

## serengil/deepface（⭐23565，confidence: high）

**Python 人脸识别与人脸属性分析库，一行代码完成验证/检索/分析**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

用于 Python 的人脸识别与人脸属性分析框架，封装 VGG-Face、FaceNet、ArcFace、Buffalo_L 等模型，后台完成检测、对齐、归一化、表示、验证五段流水线。提供验证（verify）、1:N 检索（find，支持 s3/ftp）、数据库后端注册与搜索（postgres、pgvector、milvus 等 15 种）、属性分析（年龄/性别/表情/种族）、嵌入向量提取、实时视频流、反欺骗检测；另带 REST/gRPC API 与 Docker 化脚本，并提供 deepface.dev 托管 API（含 MCP 端点）。MIT 许可，附 BibTeX 引用条目。

- 封装 10 种人脸识别模型，支持验证、1:N 检索与嵌入向量提取
- 数据库后端人脸识别：支持 postgres、pgvector、milvus、qdrant 等 15 种后端及近似最近邻
- 年龄/性别/表情/种族属性分析与反欺骗（anti-spoofing）模块
- 提供 REST API、gRPC API 与 Docker 脚本，支持摄像头实时分析

> L11: DeepFace is a lightweight face recognition and facial attribute analysis (age, gender, emotion and race) framework for p
> L13: A modern face recognition pipeline consists of 5 common stages: detect, align, normalize, represent and verify. While De
> L62: DeepFace supports database-backed operations for scalable face recognition, allowing embeddings to be explicitly registe

## conwnet/github1s（⭐23302，confidence: high）

**浏览器中秒开 GitHub 仓库的 VS Code 代码阅读器**

`ai_role=ai-enhanced · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

基于 VS Code 的浏览器端代码浏览工具：在仓库 URL 中插入 1s 即可在线浏览文件、搜索代码、查看提交历史与 PR/MR diff，无需克隆仓库。内置 AI 聊天面板可解释文件或选中代码并检索相关代码，用户自行配置可接受浏览器请求的模型端点。公共仓库免登录浏览，私有仓库需授权；远程仓库只读。另支持 GitLab 与 npm 包浏览，可通过开发指南本地运行。

- URL 插入 1s 即可浏览器内浏览仓库，无需克隆
- 基于 VS Code 界面的目录浏览、文件查找与代码搜索
- 内置 AI 聊天：解释文件/选中代码并检索相关代码
- 同时支持 GitHub、GitLab 与 npm 包浏览

> L5: GitHub1s is a browser-based code explorer built on VS Code. Browse files, search code, and review changes without clonin
> L34: ## 🤖 GitHub1s AI
> L32: Remote repositories are **read-only**. Search and code navigation depend on the repository platform and available upstre

## mlc-ai/mlc-llm（⭐23249，confidence: high）

**面向多平台本地部署 LLM 的编译与推理引擎**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=medium · maturity=—`

MLC LLM 是面向大语言模型的机器学习编译器与部署引擎，通过 ML Compilation 将模型编译后在统一推理引擎 MLCEngine 上运行，覆盖 Linux/Windows（Vulkan、ROCm、CUDA）、macOS（Metal）、Web 浏览器（WebGPU/WASM）、iOS/iPadOS 与 Android（OpenCL on Adreno/Mali）等平台。MLCEngine 提供 OpenAI 兼容 API，可通过 REST server、Python、JavaScript、iOS、Android 调用。安装与上手方式指向官方文档，项目以软件引用（bibtex）形式给出引文信息，并列出其底层技术（如 TensorIR）的学术论文。

- 统一推理引擎 MLCEngine 跨桌面、移动与浏览器平台运行
- 提供 OpenAI 兼容 API，支持 REST server、Python、JavaScript、iOS、Android 接入
- 支持 NVIDIA/AMD/Apple/Intel GPU 与 Metal、Vulkan、CUDA、ROCm、WebGPU、OpenCL 等后端
- 以机器学习编译（ML Compilation）为核心技术路线

> L14: MLC LLM is a machine learning compiler and high-performance deployment engine for large language models. The mission of 
> L43: MLC LLM compiles and runs code on MLCEngine -- a unified high-performance LLM inference engine across the above platform

## marimo-team/marimo（⭐23227，confidence: high）

**反应式 Python 笔记本：可复现实验、SQL 查询、可部署为应用**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

一个反应式 Python 笔记本环境：运行或交互某个单元格时自动执行依赖单元格或标记为过期，消除隐藏状态，按变量引用确定性执行。笔记本以纯 Python 文件存储，可用 git 版本管理，可作为脚本执行或部署为 Web 应用。内置 SQL 引擎可查询 dataframe、数据库等，支持包管理序列化到文件并在隔离 venv 中自动安装。提供 VS Code 扩展、PyCharm 插件，支持 Jupyter 笔记本一键转换，可配合 Claude Code 等 agent 或使用编辑器内置 AI 补全（可自带 API key 或本地模型）。

- 反应式执行：自动运行依赖单元格，无隐藏状态，确定性执行顺序
- 笔记本存储为纯 .py 文件，可作为脚本执行或部署为 Web 应用/幻灯片
- 内置 SQL 引擎，查询 dataframe、数据库、lakehouse、CSV、Google Sheets
- 支持 molab 云端笔记本服务与 WASM 浏览器运行

> L23: **marimo** is a reactive Python notebook: run a cell or interact with a UI
> L35: - 🤖 **AI-native**: pair with AI agents like Claude Code, or use our editor's built-in AI features
> L91: CSVs, Google Sheets, or anything else using our built-in SQL engine, which

## Skyvern-AI/skyvern（⭐23222，confidence: high）

**用 LLM 与视觉自动执行浏览器工作流的工具**

`ai_role=ai-native · license_risk=viral · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

提供 Playwright 兼容的 SDK 与无代码工作流构建器，用视觉 LLM 理解网页并执行操作，可在未见过的网站上运行且不依赖预定义 XPath。核心命令包括 page.act/extract/validate/prompt，支持任务链（Workflows）、连接本地 Chrome、凭证管理（Skyvern/Bitwarden/1Password）。安装途径有 pip、Docker Compose，默认 SQLite 可选 Postgres，另提供托管云版本。面向技术与非技术用户自动化网页操作流程。

- Playwright 兼容 SDK，提供 act/extract/validate/prompt 四个 AI 页面命令
- 支持 Python 与 TypeScript 双 SDK（npm @skyvern/client）
- 无代码工作流构建器，任务可链式组合
- 可接管本地 Chrome（CDP 连接）并经隧道由云版控制

> L7: Skyvern automates browser-based workflows using LLMs and computer vision. It provides a Playwright-compatible SDK that a
> L11: Instead of only relying on code-defined XPath interactions, Skyvern relies on Vision LLMs to learn and interact with the
> L105: **Skyvern is a Playwright extension that adds AI-powered browser automation.** It gives you the full power of Playwright

## spmallick/learnopencv（⭐23205，confidence: mid）

**为学习计算机视觉/深度学习的开发者提供博客配套代码示例库**

`ai_role=ai-knowledge · license_risk=none · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=—`

该仓库收录 LearnOpenCV.com 博客文章对应的 C++ 与 Python 示例代码，主题覆盖 OpenCV 基础操作（图像读写、边缘检测、轮廓、相机标定、光流）、深度学习模型（YOLO 系列、SAM、DETR、CLIP、Gemma、Stable Diffusion 等）以及 3D 重建、SLAM、RAG、VLM、边缘部署等内容。以「博客文章—代码」链接清单为主要组织形式，由 BigVision.AI 公司维护，未在可见 README 中给出统一安装步骤。

- 博客文章与配套代码一一对应的索引清单
- 覆盖 OpenCV C++/Python 双语言示例
- 内容横跨传统 CV、深度学习、3D 视觉、多模态与边缘部署
- 由 CV 咨询公司 BigVision.AI 维护

> L3: This repository contains code for Computer Vision, Deep learning, and AI research articles shared on our blog LearnOpenC
> L11:  LearnOpenCV is maintained by BigVision.AI , a computer vision and AI consulting company. We help organizations design, 
> L19: ## List of Blog Posts

## micro/go-micro（⭐23087，confidence: high）

**Go 分布式系统开发框架，含 Agent 与工作流支持**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

面向 Go 语言的分布式系统开发框架，提供 RPC（含流式）、服务发现、消息、存储与配置五类核心能力，每个组件以 Go 接口加默认实现的方式组织，可替换。在服务层之上提供 Agents（模型、对话历史、工具与 agent 执行）与 Workflows（有序步骤、重试、检查点），agent 将服务作为工具调用。通过 go get 安装，附 quickstart、services 与 agent 指南文档，采用 Apache 2.0 许可。

- 提供 RPC（含流式）、服务发现、消息、存储与配置
- Agents：模型、对话历史、工具与 agent 执行
- Workflows：有序步骤、重试与检查点
- 组件均为可替换默认实现的 Go 接口

> L3: Go Micro is a Go framework for distributed systems development.
> L6: Agents use services as tools; workflows coordinate service calls and agent tasks.
> L12: - **Agents:** models, conversation history, tools, and agent execution.

## 1Panel-dev/MaxKB（⭐22987，confidence: high）

**给企业搭建智能体的开源平台：RAG+工作流+MCP 工具调用**

`ai_role=ai-native · license_risk=viral · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

MaxKB（Max Knowledge Brain）是一个构建企业级智能体的开源平台，集成 RAG 管道（文档上传/在线文档抓取、自动分块、向量化）、工作流引擎、函数库与 MCP 工具调用能力，支持文本/图像/音频/视频多模态输入输出，可零编码接入第三方业务系统。技术栈为 Vue.js + Django + LangChain + PostgreSQL/pgvector，采用 GPL v3 协议，通过 Docker 容器一键启动，适用智能客服、企业内部知识库、学术研究与教育等场景。

- RAG 管道：文档上传/自动抓取、自动分块与向量化
- Agentic 工作流引擎、函数库与 MCP 工具调用
- 多模型接入：私有模型与公开模型均支持
- 原生支持文本、图像、音频、视频多模态

> L14: MaxKB = Max Knowledge Brain, it is an open-source platform for building enterprise-grade agents. MaxKB integrates Retrie
> L19: - **Model-Agnostic**: Supports various large models, including private models (such as DeepSeek, Llama, Qwen, etc.) and 
> L27: docker run -d --name=maxkb --restart=always -p 8080:8080 -v ~/.maxkb:/opt/maxkb 1panel/maxkb

## hypit-ai/hypit（⭐22980，confidence: high）

**给编码 Agent 用的视频克隆工作流 DSL 与技能：一条命令产出多版本视频**

`ai_role=ai-native · license_risk=none · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

Hypit 以 Skill 形式安装（npx skills add），为 Claude Code、Codex 等编码 Agent 提供 SVML 标记语言和组件系统来制作视频：放入参考视频后 Agent 将其克隆为完整工作流（素材、字幕、B-roll、特效），时间轴锚定到词而非秒；也可从模板起步或由 Agent 从零编写。工作流编译为成品视频，可通过无头 Chromium 进程并发渲染，生成模型为可选项（纯代码渲染可不调用生成 API）。开源无席位费、单次渲染费或水印，模型服务按所选服务商计费。

- 视频克隆为可编辑、可重跑的完整工作流（SVML 语言 + 插件组件系统）
- 一个工作流批量生成变体：换主持人、换文案、换语言，一处结构多处复用
- 支持无生成模型的纯代码渲染路径（字幕、动效、代码视觉本地渲染）
- npx skills add 一条命令安装到编码 Agent

> L34: Hypit gives AI agents (Claude Code, Codex...) a language and system to create video. Drop in a video, and your agent clo
> L36: **To be clear:** cloning a video is the fastest way in, not the only one. You can start from our templates, or just desc
> L45: npx skills add hypit-ai/hypit -g

## amusi/CVPR2026-Papers-with-Code（⭐22902，confidence: high）

**面向计算机视觉研究者的 CVPR 2026 论文与开源项目目录**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

以 Markdown 目录形式持续收录 CVPR 2026 录用论文及其开源代码、项目页、模型链接，按 3DGS、Agent、多模态大语言模型、具身智能、自动驾驶、医学图像分割、3D 重建等数十个方向分类组织。条目附 arXiv 论文链接与 GitHub 代码仓库地址，部分含 Hugging Face 模型链接。读者可通过提交 issue 补充条目，README 同时导向维护者的往届 CV 论文盘点仓库与学术交流社群。

- 按数十个研究方向分类组织的 CVPR 2026 论文目录
- 每条条目附 arXiv 论文链接及代码/项目页/模型链接
- 欢迎通过 issue 提交新论文与开源项目
- 关联往届 ICCV/ECCV/CVPR 论文盘点仓库

> L1: # CVPR 2026 论文和开源项目合集(Papers with Code)
> L14: # 【CVPR 2026 论文开源目录】

## jundot/omlx（⭐22884，confidence: mid）

**macOS 菜单栏管理的 Apple Silicon 本地 LLM 推理服务器**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=medium · maturity=—`

面向 Apple Silicon 的本地 LLM 推理服务器，通过 macOS 菜单栏应用或 CLI 管理服务；核心机制包括块式 KV 缓存的内存热层与 SSD 冷层两级缓存（跨请求、可跨重启复用）、基于 mlx-lm BatchGenerator 的连续批处理、多模型共存时的 LRU 逐出/固定/TTL 管理。提供 OpenAI 与 Anthropic 兼容 API、管理仪表盘 Web UI、HuggingFace 模型下载与一键基准测试。要求 macOS 15+、Python 3.11–3.13、Apple Silicon 芯片。

- KV 缓存热(RAM)+冷(SSD)两级分层，前缀匹配可跨请求与重启复用
- 同一服务器加载 LLM、VLM、OCR、embedding、reranker，支持 LRU 逐出/固定/TTL
- OpenAI 与 Anthropic API 兼容端点，内置管理仪表盘与聊天 UI
- 实验性多 Mac 流水线推理（Ring/Thunderbolt RDMA）

> L4:  LLM inference, optimized for your Mac Continuous batching and tiered KV caching, managed directly from your menu bar.
> L56: Requires macOS 15.0+ (Sequoia), Python 3.11–3.13, and Apple Silicon (M1/M2/M3/M4/M5).
> L114: Supports text LLMs, vision-language models (VLM), OCR models, embeddings, and rerankers on Apple Silicon.

## AiHubCN/Awesome-Chinese-LLM（⭐22772，confidence: high）

**中文开源大语言模型资源清单：收录模型、应用、数据集与教程**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

收集和梳理中文 LLM 相关开源资料的 awesome 清单，收录资源达 100+ 个，以规模较小、可私有化部署、训练成本较低的模型为主。内容组织为底座模型概览表（含参数量、训练 token 数、上下文长度、可商用性）、文本 LLM 模型条目、垂直领域微调及应用、数据集与教程等类别；每个模型条目提供仓库地址与简介，欢迎社区通过 PR 贡献新条目。

- 提供常见底座模型细节概览表（参数、token 数、最大长度、商用许可）
- 收录 100+ 个中文 LLM 相关开源模型、应用、数据集与教程
- 以规模较小、可私有化部署、训练成本较低的模型为收录重点

> L13: 自ChatGPT为代表的大语言模型（Large Language Model, LLM）出现以后，由于其惊人的类通用人工智能（AGI）的能力，掀起了新一轮自然语言处理领域的研究和应用的浪潮。尤其是以ChatGLM、LLaMA等平民玩家都能跑
> L37: ## 目录
> L21: 常见底座模型细节概览：

## NVIDIA/NemoClaw（⭐22759，confidence: high）

**在 NVIDIA OpenShell 沙箱中更安全运行 AI agent 的参考栈**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

NVIDIA 开源的参考栈，将 OpenClaw、Hermes、LangChain Deep Agents Code 三种 AI agent 运行在 OpenShell 沙箱内，通过 NemoClaw CLI 及其 agent 专属别名提供引导式上手、托管推理、网络策略、托管集成、沙箱化状态持久化与生命周期操作。安装器支持在 DGX 或 WSL 主机上以推荐预设快速安装，也可交互式选择 agent、沙箱名称、推理提供商与模型。官方文档另覆盖沙箱加固与网络安全最佳实践。

- 支持 OpenClaw（默认）、Hermes、LangChain Deep Agents Code 三种 agent
- 托管推理与可配置网络策略、出口控制
- OpenShell 沙箱隔离与加固（能力裁剪、进程限制）
- CLI 交互式选择沙箱名称、推理提供商与模型

> L7: NVIDIA NemoClaw is an open source reference stack for running supported AI agents more safely inside NVIDIA OpenShell sa
> L8: It provides guided onboarding, managed inference, network policy, managed integrations, OpenShell-backed state persisten
> L12: - OpenClaw (default)

## comet-ml/opik（⭐22678，confidence: mid）

**面向 LLM 应用团队的观测、评估与 Agent 追踪平台**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

由 Comet 开发的开源 LLM 可观测性与评估平台，Apache-2.0 授权，包含服务端后端与 Web 应用，可完整自托管。核心能力：多步 Agent 与工具调用的追踪树、基于数据集与实验的 LLM 评估（含 LLM-as-a-judge 指标如幻觉检测）、Prompt 管理与 Playground、生产仪表盘与在线评估规则、PyTest CI/CD 集成，自述设计规模为每日 4000 万条以上 trace。提供 Python/TypeScript SDK、REST API 与 OpenTelemetry 支持，另可通过 MCP 命令接入 Claude Code、Cursor 等编码代理。

- AI Agent 追踪：多步 trace 树覆盖 LLM 调用、工具执行与检索步骤
- LLM 评估：数据集、实验与 LLM-as-a-judge 指标（幻觉检测、审核、RAG 评估）
- Apache-2.0 完整平台可自托管，支持 Docker Compose 与 Kubernetes/Helm
- MCP 命令接入 Claude Code、Cursor、VS Code Copilot 等编码代理

> L10:  Opik is the open-source LLM observability and evaluation platform for AI agent tracing, LLM evaluation, prompt manageme
> L33: - **AI Agent Tracing & Observability**: Deep tracing of LLM calls, conversation logging, and agent activity, with full t
> L190: Opik provides a suite of client libraries and a REST API to interact with the Opik server. This includes SDKs for Python

## wandb/openui（⭐22613，confidence: high）

**用自然语言描述并实时渲染生成 UI 的开源工具**

`ai_role=ai-enhanced · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

OpenUI 让用户以想象描述界面，实时看到渲染结果，并支持将 HTML 转换为 React、Svelte、Web Components 等框架代码。模型接入通过 LiteLLM 统一代理，支持 OpenAI、Groq、Gemini、Anthropic、Cohere、Mistral 及 OpenAI 兼容端点，也可连接本地 Ollama 实例。安装途径包括 Docker（ghcr.io 镜像）、源码运行（uv/pip）、Docker Compose、Codespace 与 Gitpod。该项目由 W&B 维护，也用于其内部 LLM 应用工具链的原型测试。

- 描述 UI 并实时渲染，可转换为 React/Svelte/Web Components 等框架代码
- 通过 LiteLLM 接入多种 LLM 服务，支持 OpenAI 兼容端点
- 支持本地 Ollama 模型（如 llava），可配置 OLLAMA_HOST
- 提供 Docker、源码、Codespace、Gitpod 多种运行方式

> L5: Building UI components can be a slog. OpenUI aims to make the process fun, fast, and flexible. It's also a tool we're us
> L11: OpenUI let's you describe UI using your imagination, then see it rendered live. You can ask for changes and convert HTML
> L19: OpenUI supports OpenAI, Groq, and any model LiteLLM supports such as Gemini or Anthropic (Claude). The following environ

## steipete/CodexBar（⭐22589，confidence: high）

**给 AI 编码用户在菜单栏显示各家服务商用量与额度**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

一个 macOS 14+ 菜单栏应用（另有 Qt 6 Linux 桌面版与 CLI），聚合 106 个 AI 编码服务商的用量数据：会话/周/月窗口余量、重置倒计时、余额与支出、服务状态徽标。不要求单独登录，复用用户已有的 OAuth、设备流、API key、浏览器 Cookie 或本地文件会话读取用量；每服务商一个图标或合并模式，配置存于 ~/.config/codexbar/config.json，可用 CLI 脚本化管理。通过 Homebrew、AUR 或 GitHub Releases 分发。

- 聚合 106 个 AI 编码服务商的额度/用量/余额数据
- 复用已有会话读取数据，不存储密码
- 会话、周、月窗口的重置倒计时与服务状态徽标
- macOS 菜单栏、Linux 桌面（Wayland/X11）与 CLI 三种形态

> L13: CodexBar — every AI coding limit in your menu bar. 106 providers.
> L15: Tiny macOS 14+ menu bar app that keeps **AI coding-provider limits visible** and shows when each window resets. See the 
> L26: - **Privacy-first.** Reuses existing provider sessions — OAuth, device flow, API keys, browser cookies, local files — so

## winfunc/opcode（⭐22410，confidence: high）

**给 Claude Code 用户的桌面 GUI：管理会话、自建 agent 与用量**

`ai_role=ai-ecosystem · license_risk=viral · deploy=desktop · model_dep=locked-api · hardware=— · install_friction=low · maturity=idea`

基于 Tauri 2 的桌面应用，为 Claude Code CLI 提供图形界面：浏览 ~/.claude/projects 下的项目与会话并恢复历史、创建带自定义系统提示词与权限的 CC Agents 并在独立进程后台运行、集中管理 MCP 服务器、会话检查点时间线与回滚、CLAUDE.md 内置编辑器、用量与成本仪表盘。数据本地存储，无遥测；依赖 Claude Code CLI 在 PATH 中可用；AGPL 许可。README 说明发布版可执行文件尚未提供，需从源码构建。

- 可视化浏览与恢复 ~/.claude/projects 会话历史
- 自定义 CC Agents：系统提示词、权限配置、独立进程后台执行
- MCP 服务器集中管理，支持从 Claude Desktop 导入配置
- 会话检查点时间线、分支回滚与 diff 查看

> L25: **opcode** is a powerful desktop application that transforms how you interact with Claude Code. Built with Tauri 2, it p
> L44: - **Custom AI Agents**: Create specialized agents with custom system prompts and behaviors
> L127: - **Claude Code CLI**: Install from Claude's official site

## dipakkr/awesome-ai-engineering（⭐22406，confidence: high）

**面向学生与新手的 AI/编程学习资源聚合清单**

`ai_role=ai-knowledge · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

以课程、教程、GitHub 仓库、研究论文入口、认证与竞赛机会为主的资源目录，覆盖 AI 工具、Python、机器学习、LLM、深度学习，并延伸至 Web3、网络安全、云计算与前端等方向；用 :baby: 标注零基础内容、:heavy_dollar_sign: 标注付费内容、:star: 标注普遍推荐项。仓库本体不包含可安装的软件，内容以外部链接聚合形式提供。

- LLM 板块列出课程、论文入口与在线 Playground（OpenAI Playground、Google AI Studio、OpenRouter 等）
- 以 emoji 标记零基础/推荐/付费属性，附 Quick Start 路径
- 覆盖 ML/LLM/深度学习之外的多技术方向学习入口
- 汇总 hackathon、开源、面试准备等学生机会类资源

> L20: AI Tools and Resources
> L58: # AI Tools and Resources
> L176: ## Large Language Models (LLMs)

## k4yt3x/video2x（⭐22287，confidence: high）

**基于机器学习的视频超分辨率与插帧框架**

`ai_role=ai-enhanced · license_risk=viral · deploy=desktop · model_dep=— · hardware=— · install_friction=medium · maturity=—`

用 C/C++ 重写的视频处理框架，支持超分辨率放大与帧插值两种模式，通过 ncnn 与 Vulkan 运行 Anime4K v4、Real-ESRGAN、Real-CUGAN、RIFE 模型及 MPV 兼容 GLSL 着色器。提供 Windows 安装包（含 GUI，支持多语言界面）、Linux 发行版包与 AppImage、Docker/Podman 容器镜像，以及 Google Colab 免费使用方式。预编译二进制要求 CPU 支持 AVX2，GPU 需支持 Vulkan。

- 支持超分辨率与帧插值两种模式
- 通过 ncnn 与 Vulkan 运行 Real-ESRGAN、Real-CUGAN、RIFE 模型
- 支持 Anime4K v4 及所有 MPV 兼容 GLSL 着色器
- 处理过程无需额外磁盘空间

> L24: - supports Real-ESRGAN, Real-CUGAN, and RIFE (all models) via ncnn and Vulkan;
> L31: Your system must meet the minimum hardware requirements below to run Video2X.

## microsoft/unilm（⭐22239，confidence: high）

**微软研究院的大规模自监督预训练模型与工具汇总库**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

微软研究院维护的统一入口仓库，汇总其团队在跨任务、跨语言（100+语言）、跨模态（文本、图像、语音、文档版式）方向的自监督预训练研究成果：涵盖 UniLM、BEiT/BEiT-3、LayoutLM 系列、WavLM、VALL-E、Kosmos 系列、E5 等模型，以及 TorchScale 基础架构库、s2s-ft 微调工具包与 TrOCR 等应用。每个模型指向各自的子仓库/发布页，README 本身以目录与新闻列表为主，未提供统一安装步骤；许可需查看根目录 LICENSE 文件。

- 汇总数十个跨语言、视觉、语音与多模态预训练模型及其子仓库入口
- 包含 LayoutLM/LayoutXLM 文档 AI 模型与 TrOCR、LayoutReader 等应用
- 提供 TorchScale 基础架构库与 s2s-ft 微调工具包
- 发布历史记录各模型在 HuggingFace 等平台的模型发布

> L38: **The Big Convergence** - Large-scale self-supervised pre-training across ```tasks``` (predictive and generative), ```la
> L5: # Foundation Architecture

## MLEveryday/100-Days-Of-ML-Code（⭐22239，confidence: high）

**机器学习中文学习路线：Day1~54 讲解、代码与练习**

`ai_role=ai-knowledge · license_risk=permissive · deploy=library · model_dep=— · hardware=cpu-ok · install_friction=low · maturity=—`

基于 Avik-Jain 英文项目的中文版机器学习学习路线，覆盖 Day 1～54（Day 55～100 未编写）。内容含数据预处理、监督/无监督学习、神经网络基础、CNN 与聚类等，提供逐日课程目录、Python 3.11/3.12 环境安装说明、数据集准备与常见问题解答；以分步代码与 Markdown 注释为源，用脚本同步生成 .md 与 .ipynb 课程文件。基础课程不需要 GPU。

- 逐日课程目录：目标、代码与练习（Day 1～54）
- 运行 tools/sync_lessons.py 生成配套 .md 与 .ipynb
- 更新至现代 scikit-learn 与 Keras 3 用法
- 基础课程不需要 GPU

> L5: 本项目基于 Avik-Jain 的英文项目，提供中文机器学习学习路线、讲解与练习。
> L12: - 环境安装与运行：Python 3.11/3.12、基础和深度学习依赖、Notebook 内核。
> L24: 脚本默认把图形保存在 `outputs/`。打开 Notebook 时按顺序运行所有单元；完整说明见安装文档。深度学习依赖单独安装，基础课程不需要 GPU。

## microsoft/onnxruntime（⭐22107，confidence: high）

**给开发者提供跨平台高性能的 ML 推理与训练加速运行时**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

ONNX Runtime 是跨平台的机器学习加速运行时：推理侧可读取来自 PyTorch、TensorFlow/Keras 等深度学习框架，以及 scikit-learn、LightGBM、XGBoost 等经典机器学习库导出的模型，利用硬件加速器与图优化/变换提升性能；训练侧通过在现有 PyTorch 训练脚本中添加一行代码，加速多节点 NVIDIA GPU 上 transformer 模型的训练。以 MIT 许可发布，由微软维护，配套独立的推理与训练示例仓库及 QNN Plugin EP 插件仓库。项目可能收集使用数据并回传 Microsoft。

- 跨平台推理加速，支持 PyTorch/TensorFlow/Keras/scikit-learn/LightGBM/XGBoost 等来源模型
- 利用硬件加速器并结合图优化与 transforms 提供性能
- 训练侧一行代码接入现有 PyTorch 脚本，加速多节点 NVIDIA GPU 上 transformer 训练
- 提供独立的推理/训练示例仓库与 QNN Plugin EP 插件仓库

> L1: **ONNX Runtime is a cross-platform inference and training machine-learning accelerator**.
> L3: **ONNX Runtime inference** can enable faster customer experiences and lower costs, supporting models from deep learning 
> L5: **ONNX Runtime training** can accelerate the model training time on multi-node NVIDIA GPUs for transformer models with a

## huggingface/datasets（⭐22062，confidence: high）

**ML 从业者的一站式数据集加载与预处理库**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

Hugging Face 的 Python 数据集库：通过 load_dataset() 一行命令加载 Hub 上图像、音频、文本（467 种语言）、视频、PDF、NIfTI 等公开数据集，也可读取本地 CSV/JSON/Parquet 等文件或 Python 对象。基于 Apache Arrow 后端做零拷贝内存映射与智能缓存，支持 streaming=True 流式迭代、map() 多进程预处理，并可转换为 NumPy/Pandas/PyTorch/TensorFlow/JAX/Spark 等框架格式。面向训练与评估 ML 模型的开发者与科研人员。

- load_dataset() 一行加载 Hub 公开数据集与本地文件
- Apache Arrow 零拷贝内存映射，支持 streaming 流式迭代
- 多框架互转：NumPy/Pandas/Polars/PyTorch/TensorFlow/JAX/Spark
- 内置 FAISS 与 Elasticsearch 相似性检索索引支持

> L11: 🤗 Datasets is a lightweight library providing **two** main features:
> L13: - **one-line dataloaders for many public datasets**: one-liners to download and pre-process any of the number of dataset
> L24: |📦 **One-line dataset loading**|Load AI-ready datasets from the Hugging Face Hub or local files with `load_dataset()`|

## openai/swarm（⭐22061，confidence: high）

**面向开发者的轻量多 Agent 编排教学框架**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

OpenAI 团队维护的实验性教育框架，用于探索多 Agent 编排模式。核心机制为 Agent（封装 instructions 与 functions）和 handoffs（通过函数返回值转移执行权）两个原语；client.run() 实现补全-工具执行-换 Agent-更新上下文的循环，函数自动转 JSON Schema，支持流式输出与 REPL 调试循环。完全基于 Chat Completions API，无状态运行，默认模型 gpt-4o。README 明确其已被 OpenAI Agents SDK 取代，生产场景建议迁移。

- Agent 与 handoffs 两个原语表达多 Agent 编排
- 函数自动转换为 Chat Completions tools 的 JSON Schema
- 基于 Chat Completions API 的无状态设计
- 提供 airline、support_bot、triage_agent 等 6 组示例

> L6: > Swarm is now replaced by the OpenAI Agents SDK, which is a production-ready evolution of Swarm. The Agents SDK feature
> L43: Swarm focuses on making agent **coordination** and **execution** lightweight, highly controllable, and easily testable.
> L56: The Assistants API is a great option for developers looking for fully-hosted threads and built in memory management and 

## docmost/docmost（⭐22011，confidence: mid）

**给团队提供的开源协作 wiki 与文档软件**

`ai_role=ai-ecosystem · license_risk=viral · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Docmost 是一个开源的协作 wiki 与文档软件，自称是 Confluence 和 Notion 的开源替代品。功能包括实时协作、图表绘制（Draw.io、Excalidraw、Mermaid）、空间管理、权限管理、群组、评论、页面历史、搜索、文件附件与嵌入（Airtable、Loom、Miro 等），支持 10+ 种语言翻译。可参考其文档自行部署，或使用官方提供的云版本。核心采用 AGPL 3.0 许可证。

- 实时协作编辑
- 支持 Draw.io、Excalidraw、Mermaid 图表
- 空间与权限管理、群组、页面历史
- 10+ 种语言翻译支持

> L3:  Open-source collaborative wiki and documentation software.
> L33: Docmost core is licensed under the open-source AGPL 3.0 license.

## screenpipe/screenpipe（⭐21967，confidence: high）

**持续录制电脑屏幕与音频，为企业/个人构建可搜索的 AI 记忆**

`ai_role=ai-enhanced · license_risk=dual · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=—`

本地持续捕获屏幕与音频的应用：事件驱动截屏（配 accessibility tree，OCR 兜底）、Whisper 本地语音转写与说话人识别、自然语言检索（SQLite FTS5）、时间线回放。通过 Markdown 定义的 Pipes 运行 AI agent（如 meeting-summary、day-recap），带 YAML 确定性数据权限控制；以 MCP server 与 localhost REST API 向 AI 助手暴露屏幕历史。source-available 许可：个人非商用免费，商用需购买许可。桌面应用支持 macOS/Windows/Linux，也可经 CLI 运行。

- 事件驱动截屏 + accessibility tree/OCR 兜底，本地 Whisper (Large-V3-Turbo) 转写
- Pipes 插件系统：markdown 定义的定时 AI agent，含三层确定性数据权限
- MCP server 零配置接入 Claude Desktop、Cursor 等 MCP 客户端
- localhost REST API 与 JS/TS SDK，支持原始 SQL 访问 SQLite

> L12:  Continuously record your company's computer work, map workflows, help find work worth automating, and power agents' con
> L51: - **Local-first** - capture history stays on your device by default. Cloud AI, sync, integrations, and managed team stor
> L166: - **License**: Screenpipe Commercial License (source-available; personal, non-commercial use permitted, commercial use r

## dyad-sh/dyad（⭐21960，confidence: high）

**本地运行的开源 AI 应用构建器，面向进阶用户**

`ai_role=ai-native · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Dyad 是一个在本地机器上运行的开源 AI 应用构建器，定位为 Lovable、v0、Bolt 的替代品。采用自带 API 密钥（bring your own keys）模式，用户使用自己的 AI API 密钥，无需注册即可下载使用，支持 Mac 与 Windows 双平台。代码采用 Apache 2.0 许可证，仓库中 `src/pro` 目录之外的代码开源。项目维护 Reddit 社区（r/dyadbuilders）供用户分享项目与交流。

- 本地运行，自带 API 密钥，无供应商锁定
- 支持 Mac 与 Windows 跨平台
- 无需注册，下载即用
- 代码以 Apache 2.0 许可开源（src/pro 除外）

> L3: Dyad is a local, open-source AI app builder. It's fast, private, and fully under your control — like Lovable, v0, or Bol
> L11: - ⚡️ **Local**: Fast, private and no lock-in.
> L12: - 🛠 **Bring your own keys**: Use your own AI API keys — no vendor lock-in.

## recommenders-team/recommenders（⭐21955，confidence: high）

**面向研究者与开发者的推荐系统最佳实践库与示例集**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=—`

Recommenders 是 Linux Foundation of AI and Data 旗下的推荐系统项目，以 Jupyter notebook 形式提供构建推荐系统的示例与最佳实践，覆盖数据准备、模型构建、离线评估、超参调优与模型在 Azure 上的生产化五类任务，并附带数据加载、评估、训练/测试切分等工具。仓库收录多种经典与深度学习推荐算法实现，提供 uv 管理环境与 PyPI 安装途径，可选 gpu/spark/experimental 等扩展，附算法对比基准 notebook（MovieLens 数据集）。

- 以 Jupyter notebook 提供 Quick start 与 Deep dive 两级示例
- 收录 ALS、xDeepFM、LightGCN、SASRec 等多类推荐算法实现
- 提供 gpu、spark、dev、all、experimental 等安装扩展选项
- 提供基于 MovieLens 的算法对比基准 notebook

> L19: Recommenders objective is to assist researchers, developers and enthusiasts in prototyping, experimenting with and bring
> L23: This repository contains examples and best practices for building recommendation systems, provided as Jupyter notebooks.
> L21: Recommenders is a project under the Linux Foundation of AI and Data.

## QwenLM/Qwen（⭐21925，confidence: mid）

**阿里云开源的通义千问大语言模型官方仓库**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

Qwen（通义千问）系列的官方仓库，收录 1.8B/7B/14B/72B 四个规模的基础模型与 Chat 对话模型，提供权重下载链接（Hugging Face、ModelScope）。内容覆盖：Transformers/ModelScope 推理示例、GPTQ 与 KV cache 量化、全参数/LoRA/Q-LoRA 微调教程、vLLM 与 FastChat 部署、WebUI/CLI demo、DashScope API 与 OpenAI 风格 API 搭建、工具调用/Agent/代码解释器用法。注意仓库声明不再积极维护，后续跟进指向 QwenLM/Qwen2。

- 提供 1.8B 至 72B 四种规模的基础模型与 Chat 模型
- 量化模型（Int4/Int8、GPTQ、KV cache 量化）降低推理显存需求
- 微调教程覆盖全参数、LoRA、Q-LoRA
- 支持工具调用、Agent 与代码解释器用法

> L19: We opensource our **Qwen** series, now including **Qwen**, the base language models, namely **Qwen-1.8B**, **Qwen-7B**, 
> L21: In brief, we have strong base language models, which have been stably pretrained for up to 3 trillion tokens of multilin

## elder-plinius/L1B3RT4S（⭐21898，confidence: mid）

**面向各旗舰 AI 模型的越狱提示词收集仓库**

`ai_role=ai-knowledge · license_risk=viral · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

该仓库收集针对多个旗舰 AI 模型的提示词文本（README 称为 jailbreaks/liberation prompts），以 Markdown 文件组织，并附有 Discord 社区链接。仓库作者署名为 Pliny the Prompter/Liberator。README 未提供安装步骤、运行说明或使用文档，内容为提示词文本本身；仓库描述含乱码字符与模拟提示注入的口号文本。适用对象为对这些提示词文本进行研究或查阅的用户。

- 收集针对多个旗舰 AI 模型的提示词文本
- 以 Markdown 文件按模型组织的仓库结构
- 提供关联 Discord 社区链接

> L3: J̴̡̢̡̧̧̨̛̛̺̼̫̝̲̦̪͔̮̭͔͙͕͓̱̲͖͓̹̞͉̤͖̬̟͙̟̳̦̯͚̺͔͍̲̓͐͒̾͐͂̈́̑̑̊̓̔͂̈́̂͌̈́̊͐̌̓̊͒͌̉̈͜͜͝͝A̸̛͌̀̓̈́͂͋̿̈́̃̒̂͊̈̓̉̃͑̉̊̈̈́͋̉̃̊́̉͛͛̏͋́̐̍͘͘̚͝͠͠
> L8: CLICK TO JOIN->: BASI Discord

## teableio/teable（⭐21896，confidence: mid）

**面向企业的 AI 电子表格：数据管理、AI 工作流与应用构建一体**

`ai_role=ai-native · license_risk=none · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

基于 PostgreSQL 的数据库协作平台，自托管时提供四合一部署：按会话隔离的 agent 沙箱容器、以独立容器运行的应用部署平台、由记录变更/定时/webhook 触发并含 AI 步骤的自动化引擎，以及表格/视图/权限/API 的协作数据库。功能包括自然语言操作数据的 AI Chat、描述需求即由 agent 构建并一键部署的 App Builder、批量填充字段的 AI field filling。提供云端托管与自托管两种形态，独立自托管版不含 AI 功能与应用构建。

- AI Chat 以自然语言查询与操作表格数据
- App Builder 在隔离沙箱中构建应用并一键部署到独立 URL
- 自动化引擎支持记录变更、定时与 webhook 触发并可插入 AI 步骤
- 数据底层为真实 PostgreSQL，支持表格、视图、权限与 SQL 查询

> L4:  One platform where data management, AI workflows, and app building come together — spreadsheet-simple on the surface, r
> L33: - **A secure, scalable agent sandbox** — every AI session runs in its own isolated container, started on demand and gone
> L36: - **A full-featured database collaboration platform on PostgreSQL** — tables, views, permissions, and API.

## google/adk-python（⭐21892，confidence: high）

**面向开发者的代码优先 Python AI Agent 构建与部署框架**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

Google 开源的 Python 工具包，将软件工程方法应用于 AI Agent 开发：提供图式执行引擎（支持路由、循环、状态管理、human-in-the-loop）、多 Agent 层级组合、Task API 结构化委派，以及覆盖预置工具/自定义函数/OpenAPI/MCP 的工具生态。代码优先定义 Agent，另支持无代码的 Agent Config。内置 CLI、Web 开发 UI 与评估命令；可容器化部署到 Cloud Run 或 Vertex AI Agent Engine。要求 Python 3.11+。

- 图式工作流引擎：路由、fan-out/fan-in、循环、重试、状态管理、human-in-the-loop
- 模块化多 Agent 系统与 Task API 结构化委派
- 工具生态覆盖预置工具、自定义函数、OpenAPI、MCP
- 内置开发 UI、评估命令与 docker/cloud_run 部署命令

> L12:  An open-source, code-first Python framework for building, evaluating, and deploying sophisticated AI agents with flexib
> L25: Agent Development Kit (ADK) is a flexible and modular framework that applies
> L28: tasks to complex systems. While optimized for Gemini, ADK is model-agnostic,

## huggingface/peft（⭐21796，confidence: high）

**大模型参数高效微调库：小参数量适配下游任务**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

Hugging Face 的参数高效微调（PEFT）库，通过仅微调少量（额外）参数实现大模型向下游任务的适配，降低计算与存储开销，检查点仅数 MB 量级。与 Transformers 集成用于训练推理、Diffusers 管理适配器、Accelerate 支持分布式训练推理，并可与量化（QLoRA）、TRL（RLHF/DPO）组合使用。通过 pip 安装，README 提供 LoRA 训练与推理的代码示例及各方法的概念指南与 API 参考。

- 仅微调少量参数即可适配大模型（示例中仅训练 0.19% 参数）
- 与 Transformers/Diffusers/Accelerate 集成，支持适配器加载与切换
- 支持 LoRA 等多种 PEFT 方法，可与量化、TRL/RLHF 组合
- 提供 Stable Diffusion LoRA DreamBooth 训练脚本与示例 Space

> L3:  State-of-the-art Parameter-Efficient Fine-Tuning (PEFT) methods
> L5: Fine-tuning large pretrained models is often prohibitively costly due to their scale. Parameter-Efficient Fine-Tuning (P
> L7: PEFT is integrated with Transformers for easy model training and inference, Diffusers for conveniently managing differen

## NirDiamant/agents-towards-production（⭐21723，confidence: mid）

**面向开发者的生产级 GenAI Agent 教程合集**

`ai_role=ai-knowledge · license_risk=none · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

以代码优先的教程仓库形式，收录 28 个覆盖 GenAI Agent 生产环节的教程，主题包括有状态工作流、向量记忆、实时网络搜索 API、Docker 部署、FastAPI 端点、安全护栏、GPU 扩展、浏览器自动化、微调、多 Agent 协调、可观测性、评估与 UI 开发。教程由多个公司以赞助形式提供，附作者付费课程、Newsletter 与 YouTube 频道。定位读者为希望将 Agent 从原型推进到企业部署的开发者。

- 28 个代码优先的生产级 Agent 教程
- 覆盖部署、安全护栏、GPU 扩展、多 Agent 协调、可观测性与评估等生产环节
- 含 LangGraph、Redis、Mem0、RunPod 等公司贡献的分步教程

> L5: **Agents Towards Production is your go‑to resource for building production‑ready GenAI agents that scale from prototype 
> L28: > **28 production-grade tutorials** covering stateful workflows, vector memory, web search APIs, Docker deployment, secu
> L32: Companies that have contributed step-by-step tutorials to this repository.

## coze-dev/coze-studio（⭐21720，confidence: high）

**企业/开发者的一站式可视化 AI Agent 开发平台**

`ai_role=ai-native · license_risk=dual · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

Coze Studio 是一个 AI agent 开发工具，覆盖从开发到部署的全流程：提供 prompt、RAG、插件、工作流等 agent 开发核心能力，支持无代码/低代码方式通过可视化画布创建、调试和发布 agent、应用与工作流，并管理模型服务、知识库、数据库等资源。后端 Golang、前端 React + TypeScript，架构基于微服务与领域驱动设计。部署依赖 Docker/Docker Compose，最低要求 2 核 4 GB；通过 OpenAPI 与 Chat SDK 可将 agent 集成到自有业务系统；部分功能（如语气定制）仅限商业版。

- 集成 prompt、RAG、插件、工作流的 agent 开发核心能力
- 可视化画布拖拽节点构建工作流，无代码/低代码方式
- OpenAPI 与 Chat SDK 集成 agent 到自有应用
- 支持接入 OpenAI、火山引擎等模型服务

> L15: Coze Studio is an all-in-one AI agent development tool. Providing the latest large models and tools, various development
> L17: * **Provides all core technologies needed for AI agent development**: prompt, RAG, plugin, workflow, enabling developers
> L22: The backend of Coze Studio is developed using Golang, the frontend uses React + TypeScript, and the overall architecture

## bee-san/Ciphey（⭐21684，confidence: mid）

**无需密钥自动解密/解码文本的 Rust CLI 工具**

`ai_role=ai-enhanced · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=medium · maturity=—`

终端工具：粘贴被编码或加密的文本，无需密钥或密码名，自动搜索解码器链条并输出明文；支持 24 种解码器（Base64/Base32/Hex/Morse/Caesar/Vigenère 等），默认 5 秒超时，支持 regex crib 与词表匹配判定明文，LemmeKnow 识别 120+ 格式。Rust 编写，A* 搜索、Rayon 并行与 sqlite 缓存。可作 crate 库使用，另提供 MCP server 供 AI 助手调用；crates.io 发布版与 master 分支 API 存在差异。

- 24 种解码器，支持多层嵌套链条自动搜索（A* 优先尝试最有希望链条）
- LemmeKnow 识别 120+ 格式（IP、token、CTF flag 等）
- regex crib 与词表模式限定明文判定
- 提供 ciphey-mcp MCP server，含 decode/decode_with/detect_plaintext/list_decoders 四个工具

> L92: Ciphey doesn't need to be told what it's looking at. It searches chains of decoders (Base64 inside hex inside ROT13, fou
> L197: `ciphey-mcp` is a Model Context Protocol server, so AI assistants such as Claude Desktop and Kiro can decode text with C

## Zeyi-Lin/HivisionIDPhotos（⭐21639，confidence: high）

**AI 证件照制作工具：抠图、换底、排版一站式生成**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

基于 AI 模型工作流的证件照制作工具：对人像照片进行离线抠图（仅需 CPU 推理），按尺寸规格生成标准证件照与六寸排版照，支持自定义底色、美颜与裁剪。提供 Gradio Demo、Python 推理脚本与 FastAPI 服务三种使用形态，支持纯离线或端云推理（Face++ 在线人脸检测为可选项）。Apache-2.0 许可，支持 Docker 部署，社区有 ComfyUI、微信小程序、Windows GUI 等扩展。

- 轻量级人像抠图，纯离线且仅需 CPU 即可推理
- 多种抠图模型可选（MODNet、hivision_modnet、rmbg-1.4、birefnet-v1-lite）
- 生成标准证件照、六寸排版照，支持五种排版尺寸与 HEX 自定义底色
- 提供 Gradio Demo、Python CLI 与 API 服务，支持 Docker 部署

> L47: HivisionIDPhoto 旨在开发一种实用、系统性的证件照智能制作算法。
> L49: 它利用一套完善的AI模型工作流程，实现对多种用户拍照场景的识别、抠图与证件照生成。
> L53: 1. 轻量级抠图（纯离线，仅需 **CPU** 即可快速推理）

## onnx/onnx（⭐21591，confidence: high）

**给 AI 开发者的跨框架模型互操作开放格式标准**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

ONNX 定义 AI 模型的开源格式，覆盖深度学习与传统 ML：采用可扩展计算图模型，内置算子与标准数据类型定义，当前聚焦推理能力。提供 Python 包及图处理工具（形状/类型推断、图优化、opset 版本转换）、中间表示规范文档与预训练模型资源。由社区开放治理维护，含 SIG、工作组与年度社区聚会，包以 abi3 兼容 wheel 发布，构建流程支持可复现构建。

- 可扩展计算图模型与内置算子、标准数据类型定义
- 图处理工具：形状/类型推断、图优化、opset 版本转换
- abi3 兼容 wheel，单个二进制适配多个 Python 版本（3.12 起）
- 构建发布流程设置 SOURCE_DATE_EPOCH 支持可复现构建

> L10: Open Neural Network Exchange (ONNX) is an open ecosystem that empowers AI developers
> L11: to choose the right tools as their project evolves. ONNX provides an open source format for AI models, both deep learnin
> L74: pip install onnx # or pip install onnx[reference] for optional reference implementation dependencies

## KKKKhazix/khazix-skills（⭐21480，confidence: high）

**个人开源的 Agent Skills 合集，给 Claude Code 等 40+ Agent 装载使用**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

由数字生命卡兹克维护的 Agent Skills 仓库，含 6 个遵循 Agent Skills 开放标准的结构化指令集：leader（目标定义）、storage-analyzer（磁盘清理）、aihot（AI 资讯查询）、neat-freak（项目文档/记忆对齐）、hv-analysis（横纵分析法研究报告）、khazix-writer（公众号风格写作）。安装方式为在支持 Agent Skills 的工具中让 Agent 自行 clone 指定目录；不支持该标准的 Agent 可直接下载 SKILL.md 全文作为规则文件使用。MIT 许可。

- 6 个遵循 Agent Skills 开放标准的 SKILL.md 指令集
- 支持 Claude Code、Codex、Cursor、Kimi Code 等 40+ 兼容 Agent 加载
- storage-analyzer 提供只读扫描与浏览器端三色分级删除确认
- 不支持该标准的 Agent 可下载 SKILL.md 作为项目规则文件

> L17: 这里的每个 Skill 都是 Agent 能直接加载的结构化指令集，遵循 Agent Skills 开放标准。Claude Code、Codex、Qoder、Kimi Code、iFlow、CodeBuddy、Cursor 等 40+ 支持
> L5: #### 我自己每天在用的一些 AI Skill，都开源在这里

## AI4Finance-Foundation/FinGPT（⭐21415，confidence: high）

**面向金融场景的开源大语言模型项目与微调框架**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=cpu-ok · install_friction=low · maturity=—`

由 AI4Finance Foundation 维护的金融大语言模型项目：在 HuggingFace 发布基于 Llama2/ChatGLM2/Falcon/Bloom/MPT/Qwen 等开源底座、以 LoRA 微调的金融模型，任务覆盖情感分析、关系抽取、NER、金融问答与股价走势预测（FinGPT-Forecaster）。配套指令微调数据集、基准测试与五层架构（数据源/数据工程/LLM/任务/应用）。可用云 API（OpenAI）推理或本地 GPU 运行，单张 RTX 3090 可完成 8bit/QLoRA 微调。

- 发布多任务金融 LLM 与情感分析模型至 HuggingFace
- LoRA/QLoRA 轻量微调，单张 RTX 3090 即可训练
- FinGPT-Forecaster 提供股票下周走势预测的 HuggingFace Space 演示
- 提供指令微调数据集与 FinGPT-Benchmark 基准

> L22: FinGPT is an open-source financial large language model project developed and maintained by the AI4Finance Foundation.
> L109:  * What's new: **Best trainable and inferable FinGPT for sentiment analysis on a single RTX 3090, which is even better t

## stefan-jansen/machine-learning-for-trading（⭐21396，confidence: high）

**为交易研究者提供机器学习交易策略的图书配套代码库**

`ai_role=ai-knowledge · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

Stefan Jansen《Machine Learning for Trading》第三版的全书代码：27 章、9 个案例研究，围绕一条从数据基础设施、策略研究到部署监控的端到端工作流组织。覆盖梯度提升、深度时间序列、因果机器学习、强化学习、生成式 AI（基于 SEC 文件的 RAG、Graph RAG、多智能体研究系统）与合成金融数据生成。数据层使用 Polars，每章提供可复现的 Docker 环境。

- 27 章与 9 个横贯全书的案例研究（ETF、加密永续、日内股票、期权、外汇、期货等）
- 模型工具箱含 XGBoost/LightGBM/CatBoost 与 PatchTST、iTransformer、Mamba 等时间序列架构
- 生成式 AI 章节：SEC 文件 RAG、知识图谱与 Graph RAG、多智能体研究系统
- 每章提供可复现 Docker 环境，数据层基于 Polars

> L5: The code for *Machine Learning for Trading, 3rd Edition* by
> L37: - **Generative AI**: retrieval-augmented generation grounded in SEC filings, knowledge graphs and Graph RAG, and
> L51: The data layer moves to **Polars** for fast, expression-based manipulation, and every chapter ships in **reproducible

## google/skills（⭐21377，confidence: high）

**为 AI agent 提供谷歌产品与技术的技能集合**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

谷歌官方维护的 Agent Skills 仓库，收录面向 Google 产品与技术（含 Google Cloud）的技能，按 Google Cloud 入门、AI/ML、基础设施、数据库与分析、开发者工具、安全与身份、广告等类别组织，覆盖 GKE、BigQuery、Agent Platform、Cloud Run、SecOps 等产品。通过 skills.sh 的 npx 命令安装，可选择具体技能与作用范围；另为 Claude Code、Codex、Antigravity CLI 等 agent harness 提供包含 MCP server 的插件包。

- 按 12+ 类别组织的 Agent Skills 清单（AI/ML、基础设施、数据库、安全等）
- 通过 npx skills add 安装，支持选择性安装与项目/全局作用域
- 提供 skills update 命令更新并移除过时技能
- 为 Claude Code、Codex、Antigravity CLI 打包产品插件（Skills + MCP servers）

> L5: This repository contains Agent Skills for Google
> L11: npx skills add google/skills
> L223: This repo also bundles Google product plugins (Skills + MCP servers) for agent harnesses.

## Ebony-Vinyl/dsh-our-free-model（⭐21372，confidence: high）

**dsh 插件：免登录免 Key 使用免费前沿模型清单**

`ai_role=ai-enhanced · license_risk=permissive · deploy=desktop · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

挂载在 dsh 宿主上的插件，安装后无需账号与 API Key 即可在模型选择器中使用上游免费车道提供的模型（如 DeepSeek V4.1 Flash、Kimi K3）。模型清单每次刷新向上游重新拉取，不存静态快照；选择器按本机网络出口实测剔除网关拒绝路由的模型。附带 OpenAI 与 Anthropic 兼容的本地转发端口、用量看板、思考强度下发、聚合渠道（内置 75 家提供商注册表）与降级链路由。通过仓库 Release 包或本地源码目录安装，README 明确警告 npm 上的同名包非本仓库发布。

- 免登录、免注册、免 API Key 使用免费模型，清单跟随上游刷新
- 本地网关支持 Chat Completions、Responses 与 Anthropic Messages 端点
- 聚合渠道注册表内置 75 家提供商（NVIDIA NIM、OpenRouter、Groq、Ollama 等）
- 应用内一键升级：SHA-256 校验、原子替换、失败回滚、热重载

> L18: > 你只需在 dsh 里装上这个插件，无需登录、注册、填 API Key 或任何其它操作，
> L48: - **聚合渠道，自带 Key**——设置页新增一页，把第三方端点接进同一条模型清单：注册表内置 75 家提供商（NVIDIA NIM、OpenRouter、Groq、Cerebras、SambaNova、Gemini、DeepSeek、M
> L96: ## 安装

## RasaHQ/rasa（⭐21353，confidence: high）

**构建文本/语音对话助手的开源机器学习框架**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=—`

Rasa Open Source 是用于自动化文本与语音对话的开源机器学习框架，支持 NLU 与对话管理，可接入 Facebook Messenger、Slack、Telegram、Twilio 等多种对话渠道构建上下文助手。README 声明该项目当前处于维护模式，开发重心转向基于 CALM 引擎的 Hello Rasa（LLM 处理对话理解、业务流以 Flows 描述、带 Inspector 实时决策查看）。开发者安装走 PyPI，源码开发使用 Poetry 管理依赖，项目采用 Apache 2.0 许可证。

- 支持 NLU 与对话管理，可连接 Slack、Facebook、Telegram、Twilio 等渠道
- 新方向 CALM/Hello Rasa：LLM 理解对话、代码强制业务规则
- Flows 以逻辑步骤而非对话树描述业务流程
- 源码开发使用 Poetry 与 make 构建

> L62: Rasa is an open source machine learning framework for automating text and voice-based conversations. With Rasa, you can 
> L12:  Rasa Open Source is currently in maintenance mode.
> L22: **Hello Rasa** is our new interactive playground for prototyping AI agents. It combines LLM fluency with the reliability

## jnMetaCode/agency-agents-zh（⭐21330，confidence: high）

**面向 AI 编程工具用户的即插即用专家角色库（含中国市场化原创智能体）**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=locked-api · hardware=— · install_friction=medium · maturity=—`

agency-agents 的中文社区版，收录 301 个 AI 专家角色定义，覆盖经营、工程、设计、营销、金融等 20 个部门，每个智能体含身份定义、工作流程与交付物。在英文上游翻译（235 个）之外新增 66 个中国市场原创智能体（小红书/抖音/微信/飞书/钉钉运营、Qt 上位机、机械设计等）。支持 20 种 AI 编程工具，通过脚本一键安装或手动复制到对应目录；配套 agency-orchestrator 编排器支持多智能体按 DAG 协作，另有桌面客户端与在线浏览页。MIT 协议。

- 301 个智能体角色，含 66 个中国市场原创（⭐ 标记）
- 支持 20 种 AI 编程工具，install.sh 一键安装，其他工具经 convert.sh 转换格式
- OpenClaw 集成：拆分为 SOUL.md/AGENTS.md/IDENTITY.md 三文件
- 配套 agency-orchestrator 编排器：DAG 并行、断点续跑、npm 全局安装

> L5: > **301 个即插即用的 AI 专家角色** — 覆盖公司经营（CEO/CTO/CMO/COO/CPO/CFO）、工程、设计、营销、产品、游戏、安全、GIS、金融等 20 个部门。不是通用提示词模板，每个智能体都有独立的人设、专业流程和
> L7: agency-agents 的中文社区版。在已有上游翻译的基础上，新增了 66 个中国市场原创智能体（小红书、抖音、微信、B站、飞书、钉钉等平台运营，以及跨境电商、政务ToG、医疗合规、Qt 工业上位机、机械设计、畜禽养殖档案核对等垂直领域
> L91: npm install -g agency-orchestrator

## liyupi/ai-guide（⭐21286，confidence: high）

**面向零基础者的 Vibe Coding 教程与 AI 资源知识库**

`ai_role=ai-knowledge · license_risk=dual · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

以 VuePress 建站的免费 AI 知识共享平台，内容分为两部分：一是《Vibe Coding 零基础入门教程》，覆盖 AI 编程工具选用、项目实战、经验技巧、产品变现与进阶学习路线；二是 AI 知识库导航，收录 DeepSeek 上手与本地部署、Cursor/Claude Code 用法、Spring AI/LangChain 框架教程及工具测评文章。配套 B 站视频课程，提供中英双语版本，教程内容采用 CC BY-NC-SA 4.0、建站代码采用 MIT 的双协议，商业使用需授权。

- Vibe Coding 零基础教程：工具选型、项目实战、变现模式、学习路线
- AI 知识库导航：含 DeepSeek 本地部署、Cursor/Claude Code 技巧、MCP 开发
- 提供英文与繁体中文翻译版本及 B 站配套视频课程
- 教程内容 CC BY-NC-SA 4.0 + 建站代码 MIT 的双协议

> L12: 这是一个 **完全免费开放** 的 AI 知识共享平台，汇总整合目前热门的 AI 工具相关信息，包括产品介绍、使用指南、工具测评、技巧分享、应用场景、AI 变现、行业资讯、教程资源等一系列内容。
> L20: ## 🔥 鱼皮的 Vibe Coding 零基础入门教程
> L66: ## AI 知识库导航

## huggingface/candle（⭐21186，confidence: mid）

**面向 Rust 开发者的极简机器学习框架，支持 GPU 与浏览器推理**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=desktop · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

用 Rust 实现的机器学习框架，提供 Tensor 定义、CPU/CUDA/WASM 后端、模型训练与量化加载（safetensors、npz、ggml、PyTorch 文件）。内置大量模型示例，覆盖文本生成、语音识别、图像分割、文生图等任务；部分演示可编译为 WASM 在浏览器中运行。设计目标为 serverless 推理与去除生产环境中的 Python 依赖，输出轻量二进制。以 cargo crate 分发，含 core、nn、datasets、transformers 等子模块。

- CPU（可选 MKL/Accelerate）、CUDA（NCCL 多卡）与 WASM 三类后端
- 加载 safetensors/npz/ggml/PyTorch 文件格式，支持 llama.cpp 量化类型
- 内置 LLM、文生图、语音、视觉等大量模型示例，浏览器端 WASM 演示
- 语法对齐 PyTorch 的 cheatsheet，含 ONNX 评估子模块 candle-onnx

> L8: Candle is a minimalist ML framework for Rust with a focus on performance (including GPU support)
> L183: - Simple syntax, looks and feels like PyTorch.
> L269: Candle's core goal is to *make serverless inference possible*. Full machine learning frameworks like PyTorch

## cube-js/cube（⭐21027，confidence: high）

**面向 AI、BI 与嵌入式分析的开源语义层**

`ai_role=ai-ecosystem · license_risk=none · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

Cube Core 是开源语义层：以代码形式集中定义指标、维度、关联与访问规则，通过 SQL、REST 和 GraphQL API 向下游暴露给 BI 工具、自定义应用或 AI agent。支持所有 SQL 数据源（Snowflake、Databricks、BigQuery、Presto、Amazon Athena、Postgres 等），内置关系缓存引擎以降低 API 请求延迟并支撑高并发。无头设计，不附带 UI。Docker 本地或自托管运行；开发模式存在认证绕过，仅限本机调试，不可用于生产。

- 一次定义指标/维度/访问规则，经 SQL、REST、GraphQL API 供下游消费
- 兼容 Snowflake、Databricks、BigQuery、Athena、Postgres 等 SQL 数据源
- 内置关系缓存引擎，提供亚秒级延迟与高并发
- 无头设计，数据模型与商业版 Cube 双向兼容

> L9: __Cube Core is the open-source semantic layer.__ Define metrics, dimensions, joins, and access rules once in code, then 
> L26: Cube Core is an open, standalone semantic layer that any analytics application or AI agent can consume through standard 
> L66: Cube is our commercial product — an agentic analytics platform built on Cube Core. Same semantic layer underneath, plus 

## EthicalML/awesome-production-machine-learning（⭐21014，confidence: mid）

**面向 ML 从业者的生产化开源工具策展清单**

`ai_role=ai-knowledge · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=—`

按月更新的开源机器学习生产化库策展清单，覆盖部署、监控、版本管理、扩缩容与安全等环节。条目按 24 个类别组织，包括 AutoML、计算与通信优化、数据管道、部署与服务、可解释性与公平性、特征存储、模型与实验管理等；通过 GitHub releases 订阅每月新增库的摘要，另提供搜索工具包辅助导航，并有 10 分钟视频概述与相关 GenAI 姊妹清单。

- 24 个生产 ML 类别的开源库目录
- 按月通过 GitHub releases 发布新增库摘要
- 提供工具链搜索工具包与 10 分钟视频概述
- 含姊妹清单 Awesome Production GenAI List

> L6: This repository contains a curated list of awesome open source libraries that will help you deploy, monitor, version, sc
> L16: |🔧 AutoML|🧮 Computation & Communication Optimisation|🏷️ Data Annotation & Synthesis|
> L58: ## AutoML

## qax-os/excelize（⭐20997，confidence: high）

**给 Go 开发者的 Excel 读写库：操作 XLSX 等电子表格文件**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Excelize 是纯 Go 编写的库，提供读写 XLAM/XLSM/XLSX/XLTM/XLTX 电子表格文件的函数集合，支持 Microsoft Excel 2007 及以后版本生成的文档，要求 Go 1.26.0 或更高版本。README 展示的用法包括创建、读取电子表格，添加图表（可基于工作表数据或无数据生成），以及在文件中添加图片。提供流式 API 用于处理包含大量数据的工作表。通过 go get 安装，兼容 Go Modules，采用 BSD 3-Clause 许可证。

- 纯 Go 实现，读写 XLAM/XLSM/XLSX/XLTM/XLTX 文件
- 流式 API 支持生成或读取海量数据的工作表
- 图表生成与管理，可基于工作表数据或无数据构建
- 支持在电子表格中添加图片

> L13: Excelize is a library written in pure Go providing a set of functions that allow you to write to and read from XLAM / XL
> L20: go get github.com/xuri/excelize
> L76: This program is under the terms of the BSD 3-Clause License. See https://opensource.org/licenses/BSD-3-Clause.

## vercel/chatbot（⭐20997，confidence: high）

**面向开发者的 Next.js 开源 AI 聊天机器人模板**

`ai_role=ai-ecosystem · license_risk=none · deploy=library · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

由 Vercel 构建的 Next.js + AI SDK 聊天机器人模板，覆盖对话界面、聊天历史与用户数据的 Postgres 持久化、文件存储、Auth.js 认证等模块。模型访问通过 Vercel AI Gateway 统一接口完成，在 lib/ai/models.ts 中按模型配置 provider 路由，内置 Mistral、Moonshot、DeepSeek、OpenAI、xAI 等模型；非 Vercel 部署需自行设置 AI_GATEWAY_API_KEY。可一键部署到 Vercel，本地运行依赖 .env 环境变量与数据库迁移。

- 基于 Next.js App Router、RSC 与 Server Actions 构建
- 通过 Vercel AI Gateway 统一接入多家模型提供商
- Neon Serverless Postgres 保存聊天历史，Vercel Blob 存储文件
- Auth.js 认证与 shadcn/ui + Tailwind 界面组件

> L6:  Chatbot (formerly AI Chatbot) is a free, open-source template built with Next.js and the AI SDK that helps you quickly 
> L34: This template uses the Vercel AI Gateway to access multiple AI models through a unified interface. Models are configured

## 1jehuang/jcode（⭐20966，confidence: high）

**Rust 编写的编码 agent 运行器：并行跑大量 agent 且低内存**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

用 Rust 编写的终端编码 agent 工具（TUI/CLI），面向多 agent 并行开发流程。核心机制：无头 swarm worker 每会话额外内存约 3.1 MB，支持在同一仓库生成多个 agent 并由服务器管理协作（文件变更通知、DM/广播消息、自动冲突处理）；agent 可自主生成子 swarm。附带 agentgrep 检索工具返回文件结构并按已见内容裁剪结果以节省上下文。安装提供 macOS/Linux 一键脚本，Windows 另有说明。

- 多 agent swarm：服务器管理的协作、消息通道与冲突通知
- agentgrep 工具返回文件结构并自适应裁剪以节省上下文
- 支持 Claude OAuth 与 OpenAI Codex OAuth 等多种 provider
- self dev 模式：agent 可修改、构建、测试自身源码并热重载

> L7:  High-performance coding agents.
> L8:  Run dozens of agents in parallel without melting your machine. More agents, less RAM, no lag.
> L78: Spawn two or more agents in the same repo, and they will automatically be managed by the server to allow native collabor
> L111: Supports a wide range of providers, including Claude OAuth and OpenAI Codex OAuth.

## modelscope/FunASR（⭐20729，confidence: high）

**面向开发者的语音识别工具包：训练/推理/流式 ASR 与部署服务**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=cpu-ok · install_friction=low · maturity=research`

FunASR 是一个语音识别工具包，将任务、checkpoint 与运行时分开选择：提供文件转写、流式转写、VAD、标点、说话人分离、情感与音频事件识别等 pipeline，模型库含 SenseVoiceSmall、Paraformer、Fun-ASR-Nano 等。支持 Python AutoModel、CLI、OpenAI 兼容 HTTP 服务、Docker 流式服务、vLLM 批处理加速以及 llama.cpp/GGUF 的无 Python 边缘部署，并提供 MCP Server 供 Claude/Cursor 等 agent 调用。工具包本身为 MIT 许可，第三方模型许可单独约定。

- 任务/checkpoint/运行时分离的工具包架构，含模型选择与部署矩阵指南
- 多种部署路径：Python、CLI、OpenAI 兼容服务、Docker、vLLM、llama.cpp/GGUF
- 提供 MCP Server 与 OpenAI API 接入 LangChain/Dify/AutoGen 等 agent 框架
- GPU（CUDA/Vulkan）与 CPU/边缘设备的预编译二进制分发

> L5:  Industrial speech recognition toolkit for offline, streaming, and edge deployment.
> L6:  ASR · VAD · punctuation · speaker pipelines · emotion and audio-event models · OpenAI-compatible serving
> L112: FunASR is a toolkit: choose the task, checkpoint, and runtime separately.

## pydantic/pydantic-ai（⭐20679，confidence: high）

**面向 Python 开发者的类型安全 AI Agent SDK**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

Pydantic 团队出品的 Python AI SDK，核心是带类型标注的可扩展 agent 循环：结构化输出、依赖注入与工具参数校验由 Pydantic 类型系统保证。同一 agent 定义可运行于终端 CLI、Web 聊天、实时语音会话、持久化后台队列或 GitHub Actions。配套 Harness 能力库提供记忆、护栏、子 agent、规划等能力；另有 Evals 评估、Graph 控制流、OpenTelemetry 原生可观测性。安装经 PyPI/uv，无需编译，内置 'test' 模型可不带 API key 起步。

- 任意模型通过字符串切换，统一 Python API（OpenAI、Anthropic、Google、Bedrock、Ollama 等数十家）
- 类型端到端：结构化输出、类型化依赖注入与工具 schema 校验
- 九种持久化执行引擎（Temporal、DBOS、Prefect、Restate、AWS Lambda 等），支持人审
- 实时语音（OpenAI Realtime、Gemini Live、Azure、xAI Grok Voice）与图像生成同栈提供

> L18: **Pydantic AI** is the Python AI SDK: a typed, extensible agent loop with every model a string swap away. The same agent
> L157: - **Any model, one Python API.** Virtually every model and provider (OpenAI, Anthropic, Google, Bedrock, Azure AI Foundr
> L163: - **Batteries, composably.** One primitive, the capability, bundles tools, instructions, hooks, and model settings into 

## SWE-agent/SWE-agent（⭐20583，confidence: high）

**科研团队的自动修复 GitHub issue 的 LM agent**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=research`

SWE-agent 让用户选择的语言模型自主调用工具，修复真实 GitHub 仓库中的 issue，也可用于进攻性网络安全（CTF，EnIGMA 模式）与竞赛编程等自定义任务。配置由单一 yaml 文件管理，面向研究场景设计。由普林斯顿与斯坦福的研究者维护，MIT 许可；README 警告当前开发重心已转向 mini-swe-agent，一般建议新用户改用 mini-SWE-agent，EnIGMA 模式目前需使用 0.7 版本。

- 接入用户自选 LM（如 GPT-4o、Claude Sonnet 4）自主调用工具修复 GitHub issue
- EnIGMA 模式用于 CTF 进攻性网络安全挑战
- 单一 yaml 文件配置，面向研究可修改设计
- 提供 GitHub Codespaces 浏览器内试运行途径

> L20: SWE-agent enables your language model of choice (e.g. GPT-4o or Claude Sonnet 4) to autonomously use tools to
> L28: * ✅ **Made for research**: Simple & hackable by design
> L30: SWE-agent is built and maintained by researchers from Princeton University and Stanford University.

## openai/gpt-oss（⭐20474，confidence: high）

**OpenAI 开放权重的两个开源语言模型（120B/20B）**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=local-ok · hardware=— · install_friction=medium · maturity=—`

本仓库提供 gpt-oss-120b 与 gpt-oss-20b 两个开放权重模型的参考实现与工具链：PyTorch、Triton、Metal 三种推理实现，浏览器与 Python 两个内置工具，终端聊天客户端与 Responses API 示例服务器。模型采用 harmony 响应格式训练，需以该格式调用；权重经 MXFP4 量化，120b 可在单张 80GB GPU 上运行，20b 可在 16GB 内存内运行。提供 Transformers、vLLM、Ollama、LM Studio 等多种推理途径。

- 两个开放权重模型：117B/5.1B 激活与 21B/3.6B 激活
- MXFP4 量化 MoE 权重，120b 适配单张 80GB GPU，20b 适配 16GB 内存
- 原生函数调用、网页浏览、Python 代码执行与 Structured Outputs 能力
- Apache 2.0 许可，支持参数微调与三档推理努力配置

> L10: Welcome to the gpt-oss series, OpenAI's open-weight models designed for powerful reasoning, agentic tasks, and versatile
> L28: - **MXFP4 quantization:** The models were post-trained with MXFP4 quantization of the MoE weights, making `gpt-oss-120b`
> L104: This repository provides a collection of reference implementations:

## NVIDIA/SkillSpector（⭐20420，confidence: mid）

**给安装 AI agent 技能前的用户做安全扫描的命令行工具**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

SkillSpector 是面向 AI agent 技能（SKILL.md、MCP 等）的安全扫描器，在安装前检测漏洞模式、恶意行为、提示注入、数据外泄与供应链风险。提供 71 种检测模式、两阶段分析（静态分析 + 可选 LLM 语义评估）、0-100 风险评分、基线误报抑制、多格式输入与输出报告，支持 Docker 运行与批量扫描，并可作为 Pi/OpenCode 扩展嵌入 agent 会话。它是 NVIDIA Verified Skills 流水线的组成部分。LLM 语义分析需配置 OpenAI 兼容端点；对超大输入设有 fail-closed 上限。

- 71 种漏洞模式，覆盖提示注入、数据外泄、供应链、MCP 工具投毒等 17 类
- 静态分析 + 可选 LLM 语义评估的两阶段扫描
- 支持 openai/anthropic/bedrock/gemini/ollama/vllm 等多种 SKILLSPECTOR_PROVIDER
- 基线机制抑制已知误报，重复扫描只暴露新问题

> L3: **Security scanner for AI agent skills.** Detect vulnerabilities, malicious patterns, and security risks before installi
> L14: SkillSpector is part of the NVIDIA Verified Skills pipeline, which scans, evaluates, and signs agent skills before publi
> L26: - **Multi-format input**: Scan Git repos, URLs, zip files, directories, or single files
> L260: |Provider (`SKILLSPECTOR_PROVIDER`)|Credential env var|Endpoint|Default model|

## kortix-ai/suna（⭐20279，confidence: high）

**开源自托管 AI 操作系统：团队用 Agent 交付并审批实际工作**

`ai_role=ai-native · license_risk=none · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

以 git 仓库承载整个组织的 Agent 配置：agents、skills、记忆与连接器均以文件形式版本化。每个会话在独立云沙箱分支上运行，产出的变更经人工批准的 change request 合入 main。支持 Slack/Microsoft Teams 接入、cron/webhook 触发、每工具的 Allow/Ask/Block 审批门、3,000+ 应用连接器、SAML SSO 与审计日志。通过 Docker Compose 自托管，或使用 Kortix Cloud 托管服务；模型可自选提供商并使用自己的 API key。

- 公司配置全部为 git 仓库内文件，可版本化、diff 与审计
- 每会话独立隔离沙箱，变更默认拒绝合并、需人工审批 change request
- 3,000+ 应用连接器加 MCP/OpenAPI/GraphQL/HTTP，凭据服务端代理
- cron 与签名 webhook 自动触发会话

> L5: **The open-source AI Operating System**
> L22: **Kortix is the one you own.** It's an open-source **AI Operating System**: your agents, the
> L24: diffable, and shared by the whole company. The agents work on real **cloud computers** — an

## walkinglabs/learn-harness-engineering（⭐20228，confidence: high）

**面向开发者的 AI coding agent harness 工程课程（14 讲+8 项目）**

`ai_role=ai-knowledge · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

以项目制课程形式讲解如何为 AI coding agent 构建运行环境（harness）：覆盖指令、状态、验证、范围、会话生命周期五个子系统，以及 loop engineering 与 graph engineering 等进阶主题。内容含 14 讲、8 个动手项目、可复制的模板资源库（AGENTS.md、feature_list.json、init.sh 等），全部课程材料以 MIT 许可发布并提供 15 种语言翻译，可通过 npm 脚本在本地生成 PDF 教材。毕设项目为一个 Electron 知识库桌面应用，随课程阶段演进。

- harness 五子系统框架：指令、状态、验证、范围、会话生命周期
- 提供可复制模板库与 harness-creator 脚手架技能（AGENTS.md、init.sh、验证流程）
- 14 讲 + 8 项目，15 种语言翻译，MIT 许可
- 含 Claude Code、Codex、DeepSeek、Pi 四个生产 harness 的拆解章节

> L19:  A project-based course on building the environment, state management, verification, and control mechanisms that make AI
> L136: A harness has five subsystems:
> L187: 1. **Lectures**: 13 conceptual units explaining the theory behind harness engineering.
> L188: 2. **Projects**: 7 hands-on projects where you build an agentic workspace from scratch.

## eosphoros-ai/DB-GPT（⭐20158，confidence: high）

**给开发者和企业的开源 Agent 式 AI 数据分析助手**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=locked-api · hardware=— · install_friction=low · maturity=research`

连接数据库、CSV/Excel、数仓与知识库，用自然语言驱动 AI 自动生成 SQL 与 Python 代码，在沙箱中执行分析并输出图表、仪表盘与 HTML 报告。平台层提供 Agent 编排、AWEL 工作流、RAG 与多模型接入；默认安装含 FastAPI、ChromaDB 向量库，首次运行有交互式配置向导。支持私有模型部署、代理脱敏与沙箱执行。以一行安装脚本、PyPI 包与 Docker 提供，Web 界面运行在 localhost:5670。

- 自然语言转 SQL 与 Python 代码的自主执行
- 可复用 skills 机制打包领域分析流程
- 沙箱化代码执行与可控工具调用
- Text2SQL 微调支持 LLaMA、Qwen、ChatGLM2 等 11 类模型

> L43: > **An open-source AI data assistant that connects to your data, writes SQL and code, runs skills in sandboxed environme
> L59: DB-GPT is also a platform for building **AI-native data agents, workflows, and applications** with agents, AWEL, RAG, an
> L191: The default installation includes the core framework (CLI, FastAPI, Agent), OpenAI-compatible LLM support, DashScope / T

## camel-ai/owl（⭐20150，confidence: mid）

**面向开发者的多智能体协作框架，自动化真实世界任务**

`ai_role=ai-native · license_risk=none · deploy=self-host · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

基于 CAMEL-AI Framework 构建的多智能体协作框架，通过动态 agent 交互完成真实世界任务自动化。内置在线搜索、浏览器自动化（Playwright）、多模态数据处理、文档解析（Word/Excel/PDF/PPT）与 Python 代码执行等工具包，并支持 MCP 协议接入工具。提供 uv/venv/conda/Docker 多种安装方式，运行需配置 LLM API key，模型需具备工具调用能力，多模态任务需多模态模型。提供 Web 界面与示例脚本，已开源训练数据集与模型检查点。

- 基于 Playwright 的浏览器自动化与多种搜索引擎接入
- 内置 MCP、代码执行、文档解析等大量工具包
- 支持多种 LLM 后端，含 Claude、Gemini、OpenRouter 等示例脚本
- 提供 Web 界面、Docker 镜像与社区 agent 挑战活动

> L27: 🦉 OWL is a cutting-edge framework for multi-agent collaboration that pushes the boundaries of task automation, built on 
> L75: - **Browser Automation**: Utilize the Playwright framework for simulating browser interactions, including scrolling, cli
> L231: - **Tool Calling**: OWL requires models with robust tool calling capabilities to interact with various toolkits. Models 

## dailydotdev/daily（⭐20109，confidence: high）

**开发者的个性化新闻聚合 feed 与社区：浏览器新标签页/移动端获取技术内容**

`ai_role=ai-ecosystem · license_risk=viral · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

daily.dev 是面向开发者的个性化新闻聚合服务：聚合 2,000+ 来源的文章、教程、发布说明与新闻，按用户关注的标签及阅读行为生成个性化 feed。产品形态包括 Chrome/Edge 新标签页扩展、Web 应用与 iOS/Android 移动应用，核心功能免费，另提供付费订阅 daily.dev Plus；商业模式为广告支持。代码按 AGPL-3.0 开源，前端应用位于 dailydotdev/apps 仓库，本仓库为项目中心枢纽与文档所在。每个账号可创建公共 API 的个人访问令牌，同一 API 亦提供 MCP server 供 agent 客户端接入。

- 聚合 2,000+ 来源的内容并按标签与阅读行为个性化 feed
- Chrome/Edge 新标签页扩展、Web 应用与 iOS/Android 应用多种形态
- 公共 API 提供个人访问令牌，并以 MCP server 形式供 agent 接入
- Squads 社区、评论、书签与全站搜索功能

> L35: daily.dev is a free, open source personalized news feed for developers, used by millions of developers worldwide. It agg
> L107: Yes. Every account can create a free personal access token for the daily.dev public API: your feed, search, bookmarks, c
> L95: Yes. daily.dev is open source under the AGPL-3.0 license. This repository is the central hub, and the frontend applicati

## QwenLM/Qwen3-VL（⭐20083，confidence: high）

**面向开发者的开源多模态视觉语言模型系列及使用代码**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=research`

阿里云 Qwen 团队开发的多模态大语言模型系列，提供 Dense 与 MoE 两种架构、2B 到 235B 多种规模及 Instruct/Thinking 版本。模型能力覆盖视觉 Agent（操作 PC/手机 GUI）、从图像/视频生成代码、2D/3D 空间定位、原生 256K 上下文（可扩展至 1M）、32 语言 OCR 等。README 提供 Transformers 与 ModelScope 的推理示例、qwen-vl-utils 工具包用法、图像/视频像素预算控制方法，并附 Colab Cookbook 集合。

- 提供 2B/4B/8B/32B/30B-A3B/235B-A22B 多种规模的 Dense 与 MoE 模型及 FP8 版本
- 支持 32 语言 OCR、原生 256K 上下文（可扩展至 1M）与小时级视频理解
- 提供 qwen-vl-utils 工具包控制图像/视频像素预算与视觉 token 数量
- 通过 Colab 提供 12 类能力 Cookbook（识别、文档解析、视频理解、Agent 等）

> L1: # Qwen3-VL
> L8: Meet Qwen3-VL — the most powerful vision-language model in the Qwen series to date.
> L12: Available in Dense and MoE architectures that scale from edge to cloud, with Instruct and reasoning‑enhanced Thinking ed

## Alibaba-NLP/DeepResearch（⭐20049，confidence: high）

**面向长程深度信息检索任务的 30B 级开源 agent 模型**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=locked-api · hardware=— · install_friction=low · maturity=research`

通义实验室发布的 agentic 大语言模型，总参数 30.5B、每 token 激活 3.3B，上下文 128K，面向长程深度信息检索任务。训练机制包括全自动合成数据管线、基于 GRPO 定制框架的端到端强化学习；推理兼容 ReAct 与基于 IterResearch 的 Heavy 测试时扩展两种范式。提供 HuggingFace/ModelScope 权重下载、本地推理评测脚本，并可通过 OpenRouter API 无 GPU 调用；官方在线 demo 仅用于快速探索，稳定体验建议本地部署。

- 30.5B 总参数、每 token 激活 3.3B 的 MoE 结构，128K 上下文
- 全自动合成数据管线支持 agentic 预训练、SFT 与强化学习
- 兼容 ReAct 与 IterResearch Heavy 两种推理范式
- 提供 OpenRouter API 通道，无 GPU 也可运行推理

> L20: We present **Tongyi DeepResearch**, an agentic large language model featuring 30.5 billion total parameters, with only 3
> L31: - 🤖 **Agent Inference Paradigm Compatibility**: At inference, Tongyi DeepResearch is compatible with two inference parad
> L154: Tongyi-DeepResearch-30B-A3B is now available at OpenRouter. You can run the inference without any GPUs.

## dzhng/deep-research（⭐19790，confidence: high）

**面向研究者的极简深度研究 agent：迭代搜索生成带来源报告**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

以搜索、网页抓取与 LLM 组合实现迭代式深度研究的助手：根据研究目标生成搜索查询，处理结果、递归下钻，可配置研究广度（breadth）与深度（depth），并通过追问澄清需求，最终产出含来源的 markdown 报告。代码量控制在 500 行内以便理解与二次开发。需 Node.js 环境及 Firecrawl、OpenAI 的 API key，默认用 o3-mini；支持本地 LLM、DeepSeek R1（经 Fireworks）及任意 OpenAI 兼容端点，提供 npm 与 Docker 两种运行方式。

- 迭代式深度研究：生成查询→处理结果→递归下钻
- 可配置研究广度与深度，带追问澄清机制
- 支持本地 LLM、DeepSeek R1 与 OpenAI 兼容自定义端点
- 并行并发处理多个搜索与结果分析

> L3: An AI-powered research assistant that performs iterative, deep research on any topic by combining search engines, web sc
> L5: The goal of this repo is to provide the simplest implementation of a deep research agent - e.g. an agent that can refine
> L30: - API keys for:

## Unity-Technologies/ml-agents（⭐19768，confidence: high）

**让游戏与仿真成为强化学习智能体训练环境的 Unity 工具包**

`ai_role=ai-native · license_risk=none · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=—`

Unity 官方开源项目，将 2D/3D/VR/AR 游戏与仿真作为智能体训练环境：基于 PyTorch 提供 PPO、SAC、MA-POCA、自博弈等深度强化学习算法和 BC、GAIL 模仿学习算法，含 17+ 示例环境、课程学习、多实例并发训练。通过 Python API 和 Gym/PettingZoo 封装供研究人员使用，训练产物可经 Inference Engine 跨平台推理。以 Unity 包（com.unity.ml-agents）+ Python 包双组件发布，已迁移至 Unity Package 文档并停止维护 web 文档。

- 基于 PyTorch 的 PPO/SAC/MA-POCA/自博弈等强化学习与 BC/GAIL 模仿学习实现
- 17+ 示例 Unity 环境，支持单智能体、多智能体合作与对抗训练
- 可封装为 Gym 与 PettingZoo 环境，从 Python 控制 Unity 环境
- 经 Inference Engine 提供原生跨平台推理支持

> L9: **The Unity Machine Learning Agents Toolkit** (ML-Agents) is an open-source project that enables games and simulations t
> L15: - Support for training single-agent, multi-agent cooperative, and multi-agent competitive scenarios via several Deep Rei
> L37: - The `com.unity.ml-agents` package is verified for Unity 2020.1 and later. Verified packages releases are numbered 1.0.

## datawhalechina/easy-vibe（⭐19765，confidence: mid）

**面向 AI 原生产品构建者的 vibe coding 入门教程**

`ai_role=ai-ecosystem · license_risk=none · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=idea`

Datawhale 出品的多语言（10 种）在线教程，教零基础学习者通过对话式 AI 编程把想法做成产品。内容分三个阶段：产品原型（需求验证、原型搭建、接入 AI 能力）、全栈开发（前端、Git、Supabase、API、部署、Stripe 计费）、进阶（Claude Code、MCP、Skills、Agent Teams、跨平台项目），另附 9 大知识领域的附录知识库与交互式演示组件。面向初学者、产品经理、创始人及各级开发者，提供学习路径导航与 Vibe Stories 用户案例。

- 三阶段路径：产品原型→全栈交付→Claude Code 进阶工作流
- 10 种语言完整覆盖教程内容
- 提供 llms.txt 供 OpenClaw、Claude、Cursor、Trae 等 AI agent 读取仓库结构
- 附录含 9 大知识领域、80+ 交互式主题与用户研究方法（Double Diamond、JTBD、The Mom Test）

> L5:  Learn AI coding from zero by shipping real products.
> L90: - **[2026-08-12]** 📘 **Stage 1 has been restructured and polished**: The beginner path now starts with real problems and
> L140: ### AI-Native: I want advanced Claude Code and agent workflows

## elizaOS/eliza（⭐19613，confidence: high）

**面向开发者的自主 AI agent 开源 TypeScript 框架与产品栈**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

以 monorepo 形式提供：核心运行时、Eliza 应用（web/桌面/移动）、CLI、云服务、原生桥接与第一方插件。运行时模型无关，通过插件注册 actions、providers、evaluators、services、model handlers 等组件；应用能力覆盖聊天、语音、记忆、知识、消息连接器、浏览器与桌面自动化、EVM/Solana 钱包操作等，实际可用性取决于操作系统、已装插件与配置的模型/服务商。另含可引导的 Linux 与 AOSP 发行版工具链及本地推理路径（Eliza-1，基于 Gemma 4 的 2B–27B 档位）。

- 模型无关运行时 @elizaos/core，插件可注册 actions/providers/evaluators/services/model handlers 等
- 本地推理路径含 2B/4B/9B/27B 模型档位及本地嵌入、语音、视觉、图像生成资产
- 按能力将模型请求路由到本地、直连服务商或 Eliza Cloud 三类后端
- 提供可引导的 Linux 与 AOSP 发行版（packages/os）

> L10: elizaOS is an open-source TypeScript framework and product stack for autonomous
> L90: The framework is model-agnostic and extended through plugins:
> L108: `@elizaos/plugin-local-inference` provides the

## openai/evals（⭐19613，confidence: high）

**给 LLM 开发者提供评测框架与公开基准注册表**

`ai_role=ai-ecosystem · license_risk=none · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

OpenAI 提供的 LLM 评测框架与开源评测注册表：可运行注册表中的评测测试 OpenAI 模型的各维度表现，也可为自有用例编写自定义评测，并支持用私有数据构建不公开的评测。运行需配置 OPENAI_API_KEY 环境变量（README 提示注意 API 成本），要求 Python 3.9 以上；评测数据经 Git-LFS 存储可按需拉取，评测结果可记录到 Snowflake 数据库。评测模板以 YAML 加 JSON 数据方式定义，无需编写评测代码；目前不接受含自定义代码的评测贡献。

- 开源评测注册表，经 Git-LFS 拉取，可按单个评测选择性获取数据
- 支持模型分级（model-graded）评测的 YAML 模板，无需编写评测代码
- 提供 Completion Function Protocol 支持提示链与工具调用 agent 类用例
- 评测结果可记录至 Snowflake 数据库

> L5: Evals provide a framework for evaluating large language models (LLMs) or systems built using LLMs. We offer an existing 
> L13: To run evals, you will need to set up and specify your OpenAI API key. After you obtain an API key, specify it using the
> L15: **Minimum Required Version: Python 3.9**

## stas00/ml-engineering（⭐19541，confidence: high）

**面向 LLM 训练工程师的训练/微调/推理方法论开源手册**

`ai_role=ai-knowledge · license_risk=viral · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

作者基于参与 BLOOM-176B、IDEFICS-80B 训练及 Contextual.AI 工作的经验整理的开放技术手册，覆盖大语言模型与多模态模型的训练、微调和推理的方法论、工具与逐步操作说明。内容以脚本和可复制粘贴的命令为主，供 LLM/VLM 训练工程师和运维人员使用。提供 PDF/EPUB 电子书版本，附两个供 AI agent 使用的 SKILL.md 文件、网络吞吐与 TFLOPS 基准测试脚本、PyTorch 调试与 slurm 速查指南，以及加速器与网络的对比表格。以 CC BY-SA 4.0 分发。

- 提供脚本与可直接复制的命令，覆盖 LLM/VLM 训练、微调与推理
- 附 torch-dist-bench、mamf-finder 等网络与 TFLOPS 基准工具
- 提供两个 SKILL.md 文件用于训练 AI agent
- 提供 PDF/EPUB 电子书格式，托管于 Hugging Face Hub

> L5: This is an open collection of methodologies, tools and step by step instructions to help with successful training and fi
> L7: This is a technical material suitable for LLM/VLM training engineers and operators. That is the content here contains lo
> L31: I maintain two SKILL.md files that you can use to teach your AI agent:

## huggingface/trl（⭐19535，confidence: high）

**为开发者提供基础模型后训练（SFT/DPO/GRPO 等）的库**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

构建于 Transformers 之上的基础模型后训练库，通过 SFTTrainer、GRPOTrainer、DPOTrainer、KTOTrainer、RewardTrainer 等 trainer 提供 SFT、GRPO、DPO、KTO 等训练方法；基于 Accelerate 支持从单卡到多节点集群的 DDP/DeepSpeed/FSDP 分布式训练，配合 PEFT 通过量化与 LoRA/QLoRA 在有限硬件上训练大模型，并集成 Unsloth 加速内核。提供无需写代码的 CLI，pip 安装，Apache-2.0 许可。

- 多种训练方法 trainer：SFT、GRPO、DPO、KTO、Reward
- 基于 Accelerate 的 DDP/DeepSpeed/FSDP 分布式训练支持
- 与 PEFT 集成，支持量化与 LoRA/QLoRA
- CLI 无需写代码即可微调模型

> L7:  A comprehensive library to post-train foundation models
> L24: TRL is a cutting-edge library designed for post-training foundation models using advanced techniques like Supervised Fin
> L31:  - Leverages 🤗 Accelerate to scale from single GPU to multi-node clusters using methods like DDP and DeepSpeed.

## agent0ai/agent-zero（⭐19496，confidence: high）

**给 agent 一个完整 Dockerized Linux 环境的开源框架**

`ai_role=ai-native · license_risk=none · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

开源 agent 框架，核心是在 Docker 容器内提供完整 Linux 桌面（XFCE），agent 可操作真实 GUI 软件、终端与文件。功能包括内置浏览器（DOM 标注/改写元素）、与 agent 实时协作编辑 Markdown 与 LibreOffice 文档、100+ 社区插件的 Plugin Hub、项目级记忆与配置隔离、子 agent 分工协作，以及通过 A0 CLI 连接宿主机文件。依赖 Docker 运行，提供 Launcher 安装器、脚本安装器与直接 docker run 三条路径。

- 容器内真实 XFCE Linux 桌面，agent 可驱动 GUI 软件如 Blender
- 浏览器 Annotate 模式：点击页面元素生成检查/修改/复刻指令
- Plugin Hub 提供 100+ 社区插件，支持 MCP 服务器与 A2A 连接
- 子 agent 分工协作与项目级记忆/密钥隔离

> L6: Agent Zero is an open agent framework for work that needs more than chat: a Dockerized Linux desktop, a browser with DOM
> L26: |**Full Linux desktop**|The agent can use real GUI software, terminals, files, and desktop apps inside the Canvas.|
> L110: Agent Zero opens its own Linux desktop inside the right-side Canvas. Not a remote VM, not a shared clipboard, but a real

## danielmiessler/LifeOS（⭐19486，confidence: high）

**个人 AI 操作系统：让 AI 基于你的上下文推动你达成目标**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

LifeOS 是一个通用 AI Harness，以单个自包含 skill 形式分发，安装即向 Claude Code、Cursor、Codex 等 AI 编码代理粘贴一段 prompt 完成配置。系统围绕「从当前状态到理想状态」概念组织，包含持久记忆（Cortex）、49 个技能、hooks、意图路由、七阶段 Algorithm 循环与 TELOS 身份层等组件。代码为 TypeScript 与 Bash，运行依赖 AI coding harness 和 bun，主要在 Claude Code 上测试。

- 通过粘贴 prompt 或 curl 一行命令由 AI 完成安装
- 持久记忆、技能库、智能路由与自我改进机制
- 七阶段 Algorithm 循环并按复杂度分级验证
- 设计为 harness 无关，基于通用原语（hooks、skills、context files）

> L25: **LifeOS** is a General Purpose AI Harness for doing anything you want to do in life and work with AI. It captures who y
> L84: Any high-end one. LifeOS is harness-agnostic by design — it's built on universal primitives (hooks, skills, context file
> L198: - **Skill-based distribution** — the whole system now ships as a single self-contained skill (`LifeOS/`): the orchestrat

## openai/tiktoken（⭐19476，confidence: high）

**面向 OpenAI 模型的快速 BPE 分词器库**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

tiktoken 是一个 BPE 分词 Python 库，提供编码/解码文本、按 OpenAI 模型名获取对应 tokeniser（如 gpt-4o）等 API，API 文档位于 tiktoken/core.py。文本可逆无损转换、支持任意文本、token 序列可压缩原文。附带 educational 子模块用于可视化 BPE 过程，并通过 tiktoken_ext 插件机制支持注册自定义 Encoding。从 PyPI 安装，示例代码在 OpenAI Cookbook。

- 提供 encoding_for_model 按模型名获取对应分词器
- BPE 编码可逆无损、支持任意文本并压缩 token 序列
- educational 子模块可视化 BPE 训练过程
- tiktoken_ext 插件机制注册自定义编码

> L3: tiktoken is a fast BPE tokeniser for use with
> L12: enc = tiktoken.encoding_for_model("gpt-4o")
> L15: The open source version of `tiktoken` can be installed from PyPI:

## Avaiga/taipy（⭐19441，confidence: high）

**给数据科学家/ML工程师：把数据和AI算法快速变成Web应用**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

Taipy 是 Avaiga 维护的 Python 库，面向数据科学家与机器学习工程师，用于构建数据与 AI 驱动的 Web 应用。功能覆盖用户界面生成、数据集成、流水线编排、假设分析与场景管理、认证与用户管理、定时任务调度。生态还包括 Taipy Designer、Taipy Studio、预定义模板与数据平台集成，并随附 CLI、部署脚本、版本管理、数据迁移和遥测监控等生产运维材料。仅需 Python（3.9–3.12），通过 pip 安装。

- 以纯 Python 构建 Web 应用，无需学习其他语言
- 提供 UI 生成、数据集成、流水线编排与场景管理
- 内置认证、角色与用户管理、Cron 调度
- 附带 CLI、部署脚本、版本管理与遥测监控等运维工具

> L56: Taipy is designed for data scientists and machine learning engineers to create
> L66: Taipy includes the Taipy Python library enabling developers to easily empower their end-users with:
> L120: Copyright 2021-2025 Avaiga Private Limited

## nndl/nndl（⭐19441，confidence: high）

**深度学习教材读者：获取邱锡鹏《神经网络与深度学习》电子书与勘误**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

该仓库是邱锡鹏《神经网络与深度学习》第二版与通识版的资料入口：提供两本书的开放电子稿 PDF 下载、16 章目录与勘误渠道，勘误通过 GitHub Issues 提交并注明版本与页码。第二版（蒲公英书）面向专业课程与研究入门，需线性代数、微积分与概率论基础，配套 PyTorch 实践；通识版面向非专业读者与高校通识课。第一版资料归档在 legacy 目录与 nndl-v1 分支，LaTeX 源码不在公开仓库中。

- 提供第二版与通识版开放电子稿 PDF，内容随修订更新
- 第二版 16 章加 5 个数学基础附录，含注意力机制与 Transformer、图神经网络、大语言模型等章节
- 通识版 16 章，覆盖大模型、智能体、多模态、具身智能与 AI 安全
- 第一版资料归档于 legacy/nndl-v1 目录与 nndl-v1 分支，含各章 PDF 与教学幻灯片

> L3: 邱锡鹏著 · **第二版与通识版的电子书、目录和勘误入口**
> L15:  从机器学习基础出发，系统讲解神经网络、优化、Transformer、图神经网络、强化学习、生成模型与大语言模型。
> L23:  用故事、案例和生活类比解释神经网络与深度学习，并延伸到大语言模型、智能体、多模态、科学智能、具身智能、AI 安全与未来。

## nari-labs/dia（⭐19407，confidence: high）

**单次生成超真实对话的 1.6B 文本转语音模型**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=idea`

Nari Labs 开源的 1.6B 参数 TTS 模型，从文本一次生成对话语音，支持 [S1]/[S2] 说话人标签、笑声咳嗽等非语言标记，以及基于音频提示的语音克隆与情感语调控制。权重托管在 Hugging Face，可通过 Transformers 库或本仓库推理代码运行；目前仅支持英文，仅支持 GPU 推理（pytorch 2.0+/CUDA 12.6），Apache 2.0 许可，面向研究与教育用途。bfloat16 下 VRAM 约 4.4GB。

- [S1]/[S2] 标签一次生成多说话人对话
- 语音克隆：上传 5-10 秒音频加转写作为提示
- 支持 (laughs)、(coughs) 等 21 种非语言标记
- 已接入 Hugging Face Transformers（DiaForConditionalGeneration）

> L12: Dia is a 1.6B parameter text to speech model created by Nari Labs.
> L18: Dia **directly generates highly realistic dialogue from a transcript**. You can condition the output on audio, enabling 
> L142: Dia has been tested on only GPUs (pytorch 2.0+, CUDA 12.6). CPU support is to be added soon.

## mlc-ai/web-llm（⭐19276，confidence: high）

**开发者用浏览器内 LLM 推理引擎：WebGPU 加速、无需服务器**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

运行在浏览器中的 LLM 推理引擎，依赖 WebGPU 做硬件加速，推理全部在客户端完成、无服务器参与。以 npm 包形式提供 MLCEngine 接口，兼容 OpenAI API 风格（流式、JSON-mode、seed、function-calling 为初步支持），支持 Web Worker 与 Service Worker 将计算移出主线程，提供 Chrome 扩展示例。模型以 MLC 格式接入，首次加载需下载模型文件。是 MLC LLM 的伴生项目。

- 浏览器内推理，WebGPU 硬件加速，无服务器支持
- 全量兼容 OpenAI API：流式、JSON-mode、seed、function-calling（WIP）
- 支持 Web Worker / Service Worker 卸载计算与离线缓存
- 四种缓存后端（Cache API、IndexedDB、OPFS、cross-origin 扩展）

> L15: WebLLM is a high-performance in-browser LLM inference engine that brings language model inference directly onto web brow
> L18: WebLLM is **fully compatible with OpenAI API.**
> L24: You can use WebLLM as a base npm package and build your own web application on top of it by following the examples below

## mrdbourke/pytorch-deep-learning（⭐19224，confidence: high）

**面向深度学习初学者的 PyTorch 免费课程材料库**

`ai_role=ai-knowledge · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Zero to Mastery「Learn PyTorch for Deep Learning」课程的配套材料仓库，含 10 个章节（00-09）的 notebook、练习与解答、幻灯片，覆盖 PyTorch 基础、工作流、分类、计算机视觉、自定义数据集、模块化、迁移学习、实验跟踪、论文复现与模型部署。全部代码以 Google Colab/Jupyter notebook 形式提供，材料免费在线书（learnpytorch.io）、YouTube 视频与 Udemy 课程形式发布，共 321 个视频。面向机器学习初学者，前置要求为 3-6 个月 Python 经验。

- 10 个章节配套 notebook、练习/解答与幻灯片
- 在线书（learnpytorch.io）与 YouTube 前 25 小时视频免费开放
- 3 个里程碑项目围绕 FoodVision 食物图像分类模型
- 含 PyTorch 2.0 快速教程与速查表

> L63: **This course:** Teaches you PyTorch and many machine learning concepts in a hands-on, code-first way.
> L86: The code is all written via Google Colab Notebooks (you could also use Jupyter Notebooks), an incredible free resource t
> L116: The course uses a free tool called Google Colab. If you've got no experience with it, I'd go through the free Introducti

## huggingface/sentence-transformers（⭐19187，confidence: high）

**为开发者提供文本嵌入、检索与重排模型的训练和推理框架**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=research`

Python 框架，提供 SentenceTransformer、CrossEncoder、SparseEncoder、MultiVectorEncoder 四类模型的加载与推理 API，可计算嵌入、相似度分数、稀疏嵌入与 ColBERT 式 token 级嵌入。支持在自定义数据上微调嵌入/重排/稀疏模型，提供 20+ 损失函数、训练中评估、多语言与多任务学习。Hugging Face 上有超过 15,000 个预训练模型可直接使用，覆盖 100+ 语言。安装要求 Python 3.10+、PyTorch 2.2+、transformers v5.0+。

- 四类模型支持：嵌入、重排（Cross-Encoder）、稀疏嵌入、多向量（ColBERT 式）检索
- 支持 BERT、RoBERTa、XLM-R、DistilBERT、Electra、BART 等骨干网络
- 20+ 嵌入损失函数、10+ 重排与稀疏损失函数，训练中自动评估选优
- 提供 Matryoshka 嵌入、静态嵌入训练、嵌入量化等效率技术文档

> L7: # Sentence Transformers: Embeddings, Retrieval, and Reranking
> L9: This framework provides an easy method to compute embeddings for accessing, using, and training state-of-the-art embeddi
> L141: - Support of various transformer networks including BERT, RoBERTa, XLM-R, DistilBERT, Electra, BART, ...

## tensorflow/tfjs（⭐19148，confidence: high）

**在浏览器与 Node.js 中训练和部署机器学习模型的 JS 库**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

TensorFlow.js 是硬件加速的 JavaScript 库，支持在浏览器和 Node.js 中训练与部署机器学习模型。仓库组合多个包：Core（底层计算）、Layers（类似 Keras 的高层 API）、Data（数据加载）、Converter（导入 TensorFlow SavedModel）、Vis（浏览器内可视化）、AutoML（加载 AutoML Edge 模型）。后端覆盖 CPU、WebGL、WASM、WebGPU、Node.js 与 React Native。安装方式为 script 标签或 npm/yarn，并支持从 TensorFlow SavedModel 与 Keras 迁移预训练模型。

- 浏览器内训练与部署模型，支持 WebGL/WASM/WebGPU/CPU 多后端
- 提供模型转换器导入 TensorFlow SavedModel 与 Keras 模型
- Layers API 实现类似 Keras 的高层功能，可按需单独导入包
- 预训练模型通过 NPM 上的 models 仓库提供

> L3: TensorFlow.js is an open-source hardware-accelerated JavaScript library for
> L44: Backends/Platforms:
> L78: There are two main ways to get TensorFlow.js in your JavaScript project:

## amark/gun（⭐19144，confidence: high）

**去中心化图数据同步协议，供开发者构建 P2P 加密应用**

`ai_role=ai-ecosystem · license_risk=none · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

GUN 是一个图数据同步协议及配套工具生态，提供端到端加密的实时 P2P 状态同步，支持键值、表、文档等多种数据形态的图存储，本地优先、可离线运行。由 Mark Nadal 于 2014 年创建，核心引擎压缩后约 9KB。以 npm 包分发，可在浏览器通过 CDN 脚本引入，也提供 Docker 镜像、Linux 安装脚本、Heroku 等多种 relay 部署途径。框架适配方面给出 React、Vue、Svelte、Electron 等文档入口。

- 实时 P2P 状态同步，本地优先、可离线、端到端加密
- 图数据模型兼容键值/表/文档等多种访问方式
- 约 9KB gzipped 的嵌入式引擎，含 CRDT 冲突解决与加密模块
- 提供 npm 包、浏览器 CDN、Docker 镜像等多种接入与部署方式

> L4: **GUN** is an ecosystem of **tools** that let you build community run and encrypted applications - like an Open Source F
> L63: Technically, **GUN is a graph synchronization protocol** with a *lightweight embedded engine*, capable of doing *20M+ AP
> L122: To quickly spin up a GUN relay peer for your development team, utilize Heroku, Docker, or any others listed below. Or so

## AgriciDaniel/claude-seo（⭐19104，confidence: high）

**给 Claude Code 用户的 SEO 审计技能插件**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

面向 Claude Code 的开源 SEO 分析插件：26 个子技能与 19 个专项 agent 并行运行，覆盖技术 SEO、E-E-A-T 内容质量、Schema.org 标记、GEO/AI 搜索优化、本地 SEO、电商与国际 SEO，以及 Google API 与 PDF/Excel 报告。审计输出带优先级与可证伪性检查的行动计划。通过 Claude Code 插件市场安装，setup 步骤创建隔离 Python 环境并安装 Playwright Chromium；另提供 9 个可选扩展命令。

- 26 个子技能、19 个专项 agent 并行执行整站审计
- 34 个 /seo 命令，含 /seo agentic（Lighthouse Agentic Browsing、llms.txt、WebMCP）
- 4 层凭证体系从零 key 起步接入 Google SEO API（PageSpeed、CrUX、GSC、GA4、Keyword Planner）
- MIT 开源，另有面向会员的社区私有镜像版本

> L5: **Claude SEO is an open-source SEO analysis plugin for Claude Code.** It runs 26 sub-skills and 19 specialist agents in 
> L103: 34 user-invocable `/seo` commands across the orchestrator, its sub-skills, and 9 MCP extensions. Full reference in docs/

## keon/awesome-nlp（⭐19080，confidence: high）

**面向 NLP 学习者与研究者精选资源清单**

`ai_role=ai-knowledge · license_risk=viral · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

一个以自然语言处理为主题的 curated 资源清单，收录研究动态跟踪源、著名 NLP 实验室、教程/课程、书籍以及多语言 NLP 库链接。README 声明其范围限定于语言分析、多语言工具、经典与神经方法、数据集和评测；大语言模型仅在推进或评测核心 NLP 任务时收录，通用聊天机器人、agent 框架等被排除并指向其他清单。通过社区 pull request 持续维护，条目含 archived 标注。

- 按研究动态、实验室、教程、课程、书籍、库等栏目组织的资源链接
- README 明确界定收录范围：LLM 仅限推进核心 NLP 任务的场景
- 覆盖 Node.js/JavaScript 与 Python 等语言的 NLP 库条目
- 部分条目标注 archived 状态

> L5: A curated list of resources dedicated to Natural Language Processing
> L11: This list covers natural language processing — linguistic analysis, multilingual tooling, classical and neural methods, 

## jlcodes99/cockpit-tools（⭐19058，confidence: mid）

**管理多款 AI IDE/Cli 账号的桌面工具：切号、配额、多开**

`ai_role=ai-ecosystem · license_risk=none · deploy=desktop · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

本地桌面工具，统一管理 Antigravity、Codex、GitHub Copilot、Windsurf、Kiro、Cursor、Grok CLI、CodeBuddy、Qoder、Trae、Zed、ZCode 等平台的账号：一键切换、OAuth/Token 导入、配额监控、定时唤醒任务，以及各平台应用的多账号多实例并行运行。数据保存在本机目录，提供 WebSocket 本机 API 供插件联动。支持 macOS/Windows/Linux 与 18 种界面语言。Grok CLI 凭据以明文保存在本机，README 提示依赖系统文件权限保护。

- 覆盖 16 个 AI IDE/CLI 平台的账号切换与配额监控
- 各平台多账号多实例并行运行与参数隔离
- 内置 Rust/Go 双引擎本地网关，提供 OpenAI 兼容等接口
- WebSocket 仅监听 127.0.0.1，提供本机切号 API

> L10: 一款**通用的 AI IDE 账号管理工具**，目前支持 **Antigravity IDE**、**Codex**、**GitHub Copilot**、**Windsurf**、**Kiro**、**Cursor**、**Grok CL
> L271: - **这是本地桌面工具**：不需要单独注册平台账号，也不依赖项目自建云端来存你的账号列表。

## bbfamily/abu（⭐18942，confidence: high）

**给量化投资者的Python回测与策略开发框架**

`ai_role=ai-enhanced · license_risk=viral · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

基于 Python 的开源量化交易系统，源代码在 abupy 目录，配套教程目录与非编程界面（abupy_ui）。支持美股、A股、港股、期货、期权、比特币/莱特币市场的回测与选股、择时策略开发，内置缠论、波浪、谐波、K线形态、均线等信号体系与上百种子量化模型，并包含机器学习模块（AbuMLPd）与自定义数据源接入。推荐 Anaconda 部署，教程以 ipynb 形式提供，License 为 GPL。

- 支持美股/A股/港股/期货/期权/比特币等多市场回测
- 内置缠论、波浪、谐波、K线形态、均线等多种信号体系
- 内置机器学习模块并支持策略参数 Grid Search 评分
- 提供非编程界面 abupy_ui 与 19 节 ipynb 教程

> L5: |阿布量化系统源代码|abupy目录|
> L118: * 使用多种机器学习技术智能优化策略
> L123: * 美股，A股，港股

## ymcui/Chinese-LLaMA-Alpaca（⭐18929，confidence: high）

**在LLaMA上扩充中文词表并二次预训练/精调的开源中文大模型**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=research`

开源中文LLaMA基座模型与指令精调的中文Alpaca模型：在原版LLaMA上扩充中文词表、用中文语料二次预训练，Alpaca再经中文指令数据精调。发布LoRA权重（7B/13B/33B，基础/Plus/Pro版），需与原版LLaMA合并后使用；同时开源预训练与指令精调脚本。支持llama.cpp、transformers、text-generation-webui、LlamaChat、LangChain、privateGPT等量化推理与本地CPU/GPU部署，提供C-Eval评测结果与在线竞技场。

- 扩充中文词表并开源中文二次预训练与指令精调模型（LoRA权重，7B-33B）
- 开源预训练脚本与指令精调脚本，可继续训练
- 支持llama.cpp、transformers、text-generation-webui、LlamaChat、LangChain、privateGPT等部署方式
- 支持个人电脑CPU/GPU本地量化部署

> L10: 本项目开源了**中文LLaMA模型和指令精调的Alpaca大模型**，以进一步促进大模型在中文NLP社区的开放研究。这些模型**在原版LLaMA的基础上扩充了中文词表**并使用了中文数据进行二次预训练，进一步提升了中文基础语义理解能力。同时
> L19: - 🚀 快速使用笔记本电脑（个人PC）的CPU/GPU本地量化和部署体验大模型
> L20: - 🚀 支持🤗transformers, llama.cpp, text-generation-webui, LlamaChat, LangChain, privateGPT等生态

## lightgbm-org/LightGBM（⭐18889，confidence: high）

**机器学习用户：基于决策树的分布式梯度提升框架**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=medium · maturity=—`

LightGBM 是基于决策树算法的梯度提升框架（GBT/GBDT/GBRT/GBM/MART），用于排序、分类等机器学习任务。支持并行、分布式与 GPU 训练，可处理大规模数据。官方提供 Python、R 包，以及 CUDA 版本和 SWIG 封装，并通过 PyPI、conda、CRAN、NuGet、Winget 等渠道分发。文档托管于 readthedocs，另收录数十个非官方生态项目（PMML 转换、Spark/Kubernetes 集成、各语言绑定、可解释性与可视化工具等）。

- 基于决策树的梯度提升框架，用于排序、分类等任务
- 支持并行、分布式与 GPU 学习，可处理大规模数据
- 官方提供 Python/R 包及 CUDA、SWIG 构建，多渠道分发
- 收录大量第三方生态：Spark/K8s 集成、多语言绑定、模型转换与可解释工具

> L27: LightGBM is a gradient boosting framework that uses tree based learning algorithms. It is designed to be distributed and
> L32: - Support of parallel, distributed, and GPU learning.

## iii-hq/iii（⭐18845，confidence: high）

**为后端开发者提供统一实时组合、扩展与观测服务的引擎**

`ai_role=ai-enhanced · license_risk=none · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

iii 是一个以 Rust 引擎为核心的后端服务运行时，将队列、cron、HTTP、状态、可观测性、agent 与沙箱统一到一个实时系统面。一切能力映射为三个原语：Worker（注册到引擎的进程）、Trigger（触发函数运行的事件）与 Function（带稳定标识的工作单元）。各 worker 加入实时目录后互相可发现、可调用；agent 使用与开发者相同的目录与函数调用接口，可在运行时添加 worker。提供 Node.js/Python/Rust/Go SDK、开发者 Console 与可安装到第三方 harness 的 agent skills。

- Worker/Trigger/Function 三原语统一队列、cron、HTTP、状态与可观测性
- 实时目录：worker 注册后其他 worker 可立即发现并调用
- agent 与开发者共用同一函数目录，可运行时添加 worker 并追踪
- 提供 Node.js、Python、Rust、Go 四语言 SDK 与开发者 Console

> L47: That is the agent story too: when a task needs a capability the system does not have, an agent can
> L87: Platform teams publish workers. Application teams register functions and declare triggers. Agents
> L55: **Workers** are processes that register with the iii engine and then register triggers and

## microsoft/agent-lightning（⭐18733，confidence: high）

**面向开发者的 agent 强化学习训练框架**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=local-ok · hardware=— · install_friction=medium · maturity=—`

约 3,500 行代码的 agentic RL 训练框架：agent 通过其代理捕获模型交互并转为训练数据，训练器基于 verl 与 vLLM 更新策略，rollout controller 支持本地运行或以 Kubernetes Job 运行 agent。README 称 agent 侧零代码改动即可接入训练，同时保留工具、上下文与控制流。安装依赖 CUDA 12.8+ GPU 环境与 uv、verl 脚本。提供 Calc-X、Search-R1、Coding Agent 等 7 个示例。

- 通过 API 代理捕获训练数据，agent 侧零改动接入训练
- 原生支持 Kubernetes，agent 可作为 K8s Job 运行
- 提供完整 Coding Agent 训练管线（数据清洗、reward-hacking 防护、训练脚本）
- 训练栈基于 verl 与 vLLM

> L3:  3,500-Line Lightweight Agentic RL Framework for Training Agents with Real Harnesses!
> L19: - 🧩 **Train with real agent harnesses:** Agents interact with the model through the Agent Lightning v1.0 proxy with **ZE
> L41: - **Trainer:** Runs `verl` and vLLM, builds training samples, and updates the policy.

## google/magika（⭐18722，confidence: high）

**给开发者与安全场景用的 AI 文件类型检测工具**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=research`

基于深度学习的文件内容类型检测工具：模型体积约数 MB，可在单 CPU 上毫秒级完成识别，支持 200+ 内容类型（含二进制与文本），训练与评估数据集约 1 亿样本。提供 Rust 编写的命令行工具、Python API，以及 Rust、JavaScript/TypeScript（实验性 npm 包）和 Go（开发中）绑定；支持递归扫描目录、按内容类型的阈值系统与多种预测模式（high-confidence/medium-confidence/best-guess）。README 注明非 Google 官方项目。

- CLI、Python API 与 Rust/JS/Go 多语言绑定
- 200+ 内容类型，~100M 样本训练评估
- 单 CPU 每文件推理约 5ms，近恒定耗时与文件大小无关
- 按内容类型阈值与多种预测模式控制误判容忍度

> L16: Magika is a novel AI-powered file type detection tool that relies on the recent advance of deep learning to provide accu
> L28: - Available as a command line tool written in Rust, a Python API, and additional bindings for Rust, JavaScript/TypeScrip

## UFund-Me/Qbot（⭐18686，confidence: high）

**面向量化交易者的本地部署 AI 量化投研与自动交易平台**

`ai_role=ai-enhanced · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

以 Python 编写的量化投研平台，覆盖数据获取、策略开发、回测、模拟交易到实盘交易的流程，提供 GUI 前端与事件驱动后端。策略层包含经典技术指标策略与基于 qlib 的机器学习/深度学习/强化学习模型（Model Zoo 收录 300+ 模型、40+ 论文方法），支持股票、基金、期货、虚拟货币等交易对象，并接入多家券商与交易所接口。README 注明仅在 Python 3.8/3.9 下测试过，并提示交易结果不构成投资建议。

- 数据层、策略层、交易引擎的模块化分层设计
- Model Zoo 提供 300+ 模型、40+ 论文方法的训练与使用
- 覆盖股票/期货/期权/数字货币的多实盘交易接口
- 邮件、飞书、弹窗、微信多通道交易消息提示

> L41: > Qbot is an AI-oriented automated quantitative investment platform, which aims to realize the potential, empower AI tec
> L62: Qbot是一个免费的量化投研平台，提供从数据获取、交易策略开发、策略回测、模拟交易到最终实盘交易的全闭环流程。在实盘接入前，有股票、基金评测和策略回测，在模拟环境下做交易验证，近乎实盘的时延、滑点仿真。故，本平台提供GUI前端/客户端（部分
> L288:  **Note:** All the about **300+ models, methods of 40+ papers** in quant.ai supported by Model Zoo can be trained or use

## meta-llama/llama-cookbook（⭐18565，confidence: high）

**Meta 官方 Llama 模型使用指南：推理、微调、RAG 示例集**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Meta 官方的 Llama 模型家族构建指南仓库，覆盖推理、微调、RAG 入门示例及跨领域端到端用例；包含第三方服务商集成教程（3P Integrations）与 Llama 4 系列新配方（长上下文、WhatsApp 集成、论文分析等）。由 llama-recipes 更名而来，近期做过仓库重构，旧内容归档于 archive-main 分支。以 Python 代码配方形式组织，附微调 FAQ。

- 推理、微调、RAG 三类入门参考配方
- Llama 4 Scout/Maverick 最新示例（5M 长上下文、论文分析等）
- 多家 Llama 服务商的集成与端到端用例
- 保留原 llama-recipes 库源码与微调 FAQ

> L12: Welcome to the official repository for helping you get started with inference, fine-tuning and end-to-end use-cases of b
> L26: - 3P Integrations: Getting Started Recipes and End to End Use-Cases from various Llama providers
> L36:  **A:** We recently renamed llama-recipes to llama-cookbook.

## microsoft/AirSim（⭐18561，confidence: high）

**无人机/自动驾驶仿真平台：供 AI 研究者做模拟实验**

`ai_role=ai-enhanced · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

基于 Unreal Engine（另有实验性 Unity 版本）的开源跨平台仿真器，支持无人机、汽车等载具的物理与视觉仿真。提供平台无关 API（C++/Python/C#/Java，经 RPC 暴露），可读取图像与状态、控制载具；支持 PX4、ArduPilot 的软件在环与 PX4 硬件在环仿真。提供录制位姿与图像生成训练数据、ComputerVision 模式收集深度/视差/分割等图像，以及 API 控制的天气效果。面向自主载具的深度学习、计算机视觉与强化学习研究。

- 通过 RPC 暴露多语言 API，读取图像/状态并控制载具
- 支持 PX4、ArduPilot 软件在环与 PX4 硬件在环仿真
- ComputerVision 模式可采集深度、视差、表面法线、分割图像
- 录制按钮一键生成位姿+图像训练数据

> L3: AirSim is a simulator for drones, cars and more, built on Unreal Engine (we now also have an experimental Unity release)
> L7: Our goal is to develop AirSim as a platform for AI research to experiment with deep learning, computer vision and reinfo
> L55: AirSim exposes APIs so you can interact with the vehicle in the simulation programmatically. You can use these APIs to r

## microsoft/SkillOpt（⭐18508，confidence: high）

**为冻结参数的 LLM agent 训练可复用自然语言技能文档的优化器**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=locked-api · hardware=— · install_friction=low · maturity=research`

将技能文档视为冻结 agent 的可训练状态：由独立的优化器模型把带评分的轨迹转化为对单个技能文档的有界增/删/改编辑，默认路径下候选编辑仅在提升留出验证分数时被接受，配合文本学习率预算、被拒编辑缓冲与按 epoch 的慢/元更新。部署产物为 300–2,000 token 的 best_skill.md，推理时不增加模型调用。以 PyPI 包发布，含多后端支持、六个内置基准与可选 WebUI 仪表盘，另提供 skillopt-sleep 夜间离线自进化 CLI。

- 技能文档作为可训练状态：rollout→reflect→aggregate→select→update→evaluate 训练循环
- 验证门控编辑接受机制与文本学习率预算、被拒编辑缓冲
- 多后端支持：OpenAI / Azure / Claude / Qwen / MiniMax 及多种 exec 后端
- 部署产物 best_skill.md（300–2,000 token），推理时零额外模型调用

> L17: - **[2026-06-02]** 🎉 **SkillOpt v0.1.0 is now available on PyPI!** Install with `pip install skillopt`. This initial rel
> L26: **SkillOpt treats the skill document as the trainable state of a frozen
> L57: A backend = a chat / exec target (e.g. `openai_chat`, `claude_chat`,

## teambit/bit（⭐18495，confidence: high）

**为开发者提供组件化代码构建系统并让 AI agent 复用组件**

`ai_role=ai-enhanced · license_risk=none · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

Bit 是一个连接组件与应用、覆盖开发到 CI 的构建系统：将源码组织为可组合的组件，支持创建可复用 UI 组件、定义组件蓝图模板、组合应用外壳、部署应用与服务。通过 MCP 让 AI agent 创建和复用组件。支持 monorepo、polyrepo 或无仓库结构，提供 NodeJS、React、Angular、Vue、React Native、NextJS 等官方开发环境，原生支持 TypeScript 与 ESM。通过 npx 安装器装到 PATH，组件可通过标准包管理器安装；托管 scope 需使用 Bit Cloud 或自托管。

- 通过 MCP 使 AI agent 能创建和复用组件
- 提供 NodeJS、React、Angular、Vue、React Native、NextJS 等官方开发环境
- 支持 monorepo、polyrepo 或无仓库的代码结构
- 组件可用 npm 等标准包管理器安装

> L12: Bit is the build system to connect components and apps from development to CI in the AI era. Bit organizes source code i
> L21: Bit supports all tooling in the JS ecosystem and comes out of the box with official dev environments for NodeJS, React, 

## browser-use/browser-harness（⭐18468，confidence: high）

**让编码 Agent 驱动真实 Chrome，以登录态完成浏览器操作**

`ai_role=ai-enhanced · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

通过一段 setup prompt 将 Claude Code、Codex 或 Cursor 连接到用户本机已登录的 Chrome：经 DevTools Protocol（CDP）通信，支持打开页面、点击、输入、读取与下载。Agent 运行时在本地工作区补写可复用 helper，`SKILL.md` 提供工作流说明，`src/` 目录保持受保护。另提供 `browser-harness-mcp`，经 stdio 将浏览器控制 helper 暴露为 MCP 工具供任意 MCP 客户端调用。MIT 许可。

- 通过 CDP 连接用户真实已登录 Chrome 执行操作
- Agent 运行时自动补写可复用 helper
- 提供 browser-harness-mcp，支持任意 MCP 客户端驱动浏览器
- setup prompt 一步安装（uv + Python 3.12）

> L5: Browser Harness lets Claude Code, Codex or Cursor use your real Chrome browser: open pages, click, type, read and downlo
> L45: Use your local browser for logged-in, personal work. When you want many browsers in parallel—with live previews, proxies
> L49: `browser-harness-mcp` exposes the browser control helpers as MCP tools over

## arc53/DocsGPT（⭐18322，confidence: high）

**面向企业与开发者的自托管文档问答与 AI Agent 平台**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

DocsGPT 将文档、网站与已连接的应用转为可引用出处的 AI Agent：支持可视化工作流编排、知识同步（Google Drive、SharePoint、Confluence、GitHub、S3 等）与 GraphRAG，每个回答附带来源引用。模型可任选云端（OpenAI、Anthropic、Groq 等）或本地（Ollama、vLLM），整个栈运行在用户自身环境内。提供一键安装脚本、`docsgpt` CLI 管理命令，另有 Docker Compose、pip、Kubernetes 及离线部署途径；MIT 许可，包含 SSO、团队与配额等团队功能。

- Agent 与深度研究模式：自定义提示、知识与工具，支持多步回答
- 拖拽式可视化工作流：串联 Agent、条件与沙箱代码
- 答案带来源引用，知识源可从多平台持续同步
- OpenAI 兼容 API、MCP server、网站 widget、Discord/Slack/Telegram 机器人与 CLI 多种接入方式

> L3:  Open-source AI agents grounded in your docs. Private, self-hosted, any model.
> L45: DocsGPT turns your documents, sites and connected apps into AI agents that answer with sources. Build agents and
> L66: - 🧠 **Any model:** OpenAI, Anthropic, Google, Groq, OpenRouter, or local models through Ollama, vLLM and other OpenAI-co

## xming521/WeClone（⭐18305，confidence: mid）

**用聊天记录微调 LLM 打造个人数字分身并接入聊天机器人**

`ai_role=ai-native · license_risk=viral · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=idea`

端到端数字分身流水线：从 Telegram 导出聊天记录（JSON/图片），经预处理去除手机号、邮箱、IP 等隐私信息，再用 LoRA/QLoRA 等方法以 Qwen2.5-VL-7B-Instruct（默认）微调 LLM，支持图像模态数据；推理以 OpenAI 兼容 API 服务提供，可接入 AstrBot、LangBot 部署到 Discord/Telegram/Slack/微信等平台。数据支持加密存储，默认微调后不支持工具调用。Windows 未严格测试，建议 WSL。

- 聊天数据导出→预处理→训练→部署的完整流程（CLI 驱动）
- 默认 Qwen2.5-VL-7B-Instruct + LoRA SFT，支持图像模态微调
- Microsoft Presidio 隐私过滤 + blocked_words 黑名单 + 加密存储模式
- 多卡训练（DeepSpeed）与按模型大小/精度的显存需求表

> L24: - 💫 Complete end-to-end solution for creating digital avatars, including chat data export, preprocessing, model training
> L25: - 💬 Fine-tune LLM using chat history with support for image modal data, infusing it with that authentic "flavor"
> L46: |WeChat (Personal Account)|✅ (Based on **openclaw-weixin**)|

## emcie-co/parlant（⭐18298，confidence: high）

**面向企业客服场景的 AI Agent 对话控制框架**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

面向客户服务的 Agent 框架，核心机制是按对话轮次动态收窄上下文：开发者以代码定义规则、知识与工具，引擎在每轮匹配仅相关的指令与工具再调用 LLM。提供 Guidelines（条件-动作规则）、Journeys（多轮 SOP）、Canned Responses（预审模板）、工具按需触发与 OpenTelemetry 全链路追踪。通过 pip 安装，提供 Python SDK 与官方 React 聊天组件，Apache 2.0 协议。

- 条件-动作式 Guidelines，引擎按轮次匹配相关规则注入上下文
- Journeys 多轮 SOP 流程，支持快进、回退与节奏自适应
- Canned Responses 预审模板限制关键回复用词
- 内置 OpenTelemetry 日志、指标与追踪

> L3: ### The interaction control harness for customer-facing AI agents
> L45: Parlant is an agentic harness offering optimized context engineering for conversational use cases: getting the right con

## ahmedkhaleel2004/gitdiagram（⭐18293，confidence: high）

**把 GitHub 仓库转成交互式架构图与一分钟讲解视频**

`ai_role=ai-enhanced · license_risk=permissive · deploy=— · model_dep=locked-api · hardware=— · install_friction=low · maturity=idea`

将公开或私有 GitHub 仓库转换为可交互的架构图：点击组件可跳转到对应文件或目录，支持导出 PNG 或复制 Mermaid 源码；私有仓库通过 GitHub token 访问。近期新增生成约一分钟解说视频的功能（制作新视频处于 early access）。对外提供远程 MCP 服务器（无需 key），供 Claude、Cursor、VS Code、ChatGPT 等 agent 客户端读取仓库架构说明与 Mermaid 源码。本地运行需 Bun、Cloudflare R2、Upstash Redis 及 OpenAI 或 OpenRouter API key。

- AI 生成交互式架构图，点击组件跳转源码，可导出 PNG/Mermaid
- 远程 MCP 服务器（gitdiagram.com/mcp，无需 key）供 AI agent 调用
- 生成约一分钟解说视频，支持 MP4 横竖屏下载与内嵌字幕
- 支持通过 GitHub token 访问私有仓库

> L3: Visualize any codebase: turn any public or private GitHub repository into an interactive architecture diagram, or watch 
> L36: GitDiagram is a remote MCP server at `https://gitdiagram.com/mcp` (no key or sign-in). Agents can read a public reposito
> L54: Requires Bun, Cloudflare R2, Upstash Redis, and an OpenAI or OpenRouter API key. See the setup guide for prerequisites a

## langchain-ai/langchainjs（⭐18275，confidence: high）

**JavaScript 开发者构建 LLM 应用的组件化框架**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

LangChain.js 是 TypeScript 编写的框架，用于构建由 LLM 驱动的应用：提供 agents、models、embeddings、vector stores 等的统一接口，可组合互操作组件与第三方集成。README 列出数据增强、模型互换、快速原型等用途，并指向生态内的 Deep Agents、LangGraph.js（agent 编排）与 LangSmith（构建/测试/监控平台）。通过 npm/pnpm/yarn 安装，支持 Node.js、Cloudflare Workers、浏览器、Deno、Bun 等运行环境。

- 为 agents、模型、嵌入、向量库等提供统一标准接口
- 可替换模型的互操作层，含模型供应商/工具/向量库集成库
- 支持 Node.js、Cloudflare Workers、Vercel/Next.js、Deno、Bun 等多种环境
- npm/pnpm/yarn 三种包管理器安装

> L11: LangChain is a framework for building LLM-powered applications. It helps you chain together interoperable components and
> L32: LangChain helps developers build applications powered by LLMs through a standard interface for agents, models, embedding
> L55: - Node.js (ESM and CommonJS) - 20.x, 22.x, 24.x

## anthropics/claude-quickstarts（⭐18262，confidence: high）

**帮助开发者快速上手 Claude API 构建应用的示例项目集**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

Anthropic 维护的快速入门项目集合，每个子项目演示一类 Claude API 用法：客服 Agent、金融数据分析、桌面/浏览器计算机操作（含 toolset 最小示例）、基于 Claude Agent SDK 的自主编码 Agent、以及一批基于 Managed Agents 的集成示例（Slack、Linear、Sentry、MCP Server、知识 Wiki、定时简报等）。各子项目附独立 README 与安装说明，通用流程为克隆仓库、安装依赖、配置 API key 后运行。要求持有 Claude API key。

- 覆盖客服 Agent、金融分析、计算机操作、浏览器自动化等多类入门示例
- 含 computer_toolset_20260801 与 browser_toolset_20260801 的 Python/TypeScript 最小驱动示例
- Managed Agents 系列演示 Slack/Linear/Sentry webhook 桥接、cron 部署与 MCP Server 封装
- MIT 许可证，各子项目附独立安装说明

> L3: Claude Quickstarts is a collection of projects designed to help developers quickly get started with building application
> L9: ## Available Quickstarts
> L115: Each quickstart project comes with its own README and setup instructions. Generally, you'll follow these steps:

## langbot-app/LangBot（⭐18231，confidence: high）

**给开发者的多平台 IM 聊天机器人开发与运行平台**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

开源平台，将大语言模型接入 Slack、Discord、Telegram、微信/企业微信、飞书、钉钉、QQ 等 IM 平台，构建能对话、执行任务的智能体。内置 RAG 知识库，深度集成 Dify、Coze、n8n、Langflow 等编排工具；提供 Web 管理面板做配置与监控、插件生态、访问控制与限流。支持 uvx 一行启动、Docker Compose 与多家云平台部署，并通过 MCP Server 与 CLI（lbctl）供编程代理管理机器人、流水线与插件。

- 一套代码接入 Discord、Telegram、Slack、LINE、QQ、微信、企业微信、飞书、钉钉、KOOK 等 IM 平台
- 内置 RAG 知识库，集成 Dify、Coze、n8n、Langflow、Deerflow、Weknora
- 内置 MCP 端点与 lbctl CLI，供编程代理管理机器人、流水线、插件与模型
- 插件生态与事件驱动架构，Web 面板配置无需 YAML

> L28: LangBot is an **open-source, production-grade platform** for building AI-powered instant messaging bots. It connects Lar
> L34: - **AI Conversations & Agents** — Multi-turn dialogues, tool calling, multi-modal support, streaming output. Built-in RA
> L144: - **MCP Server** — LangBot exposes a built-in Model Context Protocol endpoint at `/mcp`, mirroring the HTTP API so an ag

## AsyncFuncAI/deepwiki-open（⭐18215，confidence: mid）

**为 GitHub/GitLab/Bitbucket 仓库自动生成 AI Wiki 的工具**

`ai_role=ai-enhanced · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

输入仓库名即可为 GitHub、GitLab 或 Bitbucket 仓库自动生成可交互的 Wiki：分析代码结构、生成文档、创建可视化图解、组织为可导航的 Wiki，并生成面向代码导览的 codemap。项目自称是对 DeepWiki 的自有实现，2.0 版本以 Grok-Wiki 名称发布，提供 grok-wiki.com 下载入口。README 采用多语言（含简繁中文等 9 种语言），以 MIT 许可证发布，接受社区 issue 与 PR 贡献。

- 输入仓库名即可生成分析文档、可视化图解与 codemap
- 支持 GitHub、GitLab、Bitbucket 三类仓库托管平台
- 2.0 版本以 Grok-Wiki 名称发布，提供站点下载入口

> L5: **DeepWiki** is my own implementation attempt of DeepWiki, automatically creates beautiful, interactive wikis for any Gi
> L20: ## Deepwiki-Open 2.0 (Grok Wiki is now live)

## RightNow-AI/openfang（⭐18211，confidence: low）

**给需要自主运行的 agent 的 Rust 单二进制操作系统**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=idea`

用 Rust 编写的开源 Agent OS，编译为约 32MB 的单个二进制文件，含 14 个 crate 与 1,767+ 测试。核心概念是 Hands：预置的自主能力包（HAND.toml 清单+系统提示词+SKILL.md+审批护栏），按计划独立运行，内置 Clip、Lead、Collector、Predictor、Researcher、Twitter、Browser 共 7 个。系统自带 16 项安全机制（WASM 沙箱、Merkle 审计链、提示注入扫描等）、40 个频道适配器、SQLite+向量记忆与 Web 仪表盘。当前为 pre-1.0 版本，README 提示小版本间可能有破坏性变更。

- 7 个内置自主 Hand，按计划运行无需人工提示
- 编译为单个约 32MB 二进制，Hand 全部编译进二进制无需额外下载
- 16 项安全机制：WASM 沙箱、Merkle 哈希链审计、Ed25519 签名清单、提示注入扫描等
- 40 个频道适配器（Telegram/Discord/Slack/飞书/钉钉等），支持按频道覆盖模型

> L26: OpenFang is an **open-source Agent Operating System**. Not a chatbot framework. Not a Python wrapper around an LLM. Not 
> L30: The entire system compiles to a **single ~32MB binary**. One install, one command, your agents are live.
> L203: openfang-api         140+ REST/WS/SSE endpoints, OpenAI-compatible API, dashboard

## MathFoundationRL/Book-Mathematical-Foundation-of-Reinforcement-Learning（⭐18193，confidence: high）

**给强化学习学习者提供数学基础教材及配套课程资源**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

《Mathematical Foundations of Reinforcement Learning》一书的主页仓库，提供 Latex/Beamer 制作的幻灯片源码获取方式、全书章节目录、读者对象说明与引用格式。作者自 2019 年起在研究生课程中编写讲义成书，由 Springer 与清华大学出版社出版。仓库还汇总了读者制作的 Python/Matlab/R/C++ 代码实现与多语言学习笔记，并提供中英文课程视频链接；教授可邮件索取幻灯片源码用于授课。PDF 文件托管于 GitHub，另附印刷版勘误表。

- 以数学视角系统介绍强化学习基本概念、问题与经典算法（共 10 讲）
- 配套中英文课程视频（Bilibili/YouTube），累计播放超 210 万次
- 汇总读者贡献的多语言代码实现与学习笔记链接
- 全部示例基于 grid world 任务展开

> L9: This book aims to provide a **mathematical but friendly** introduction to the fundamental concepts, basic problems, and 
> L27: This book is designed for senior undergraduate students, graduate students, researchers, and practitioners interested in
> L36: I have been teaching a graduate-level course on reinforcement learning since 2019. Along with teaching, I have been prep

## NVIDIA/Megatron-LM（⭐18178，confidence: high）

**面向研究团队的大规模 transformer 模型分布式训练库**

`ai_role=ai-native · license_risk=none · deploy=library · model_dep=locked-api · hardware=— · install_friction=low · maturity=idea`

NVIDIA 维护的大规模 transformer 训练代码库，含两个组件：Megatron-LM 提供预配置训练脚本，供研究团队学习分布式训练与快速实验；Megatron Core 提供可组合的 GPU 优化构建块，含 TP/PP/DP/EP/CP 并行策略、FP16/BF16/FP8/FP4 混合精度与多种模型架构，供框架开发者搭建自定义训练流水线。提供 2B 到 462B 参数模型的基准测试结果与 Hugging Face 双向 checkpoint 转换工具 Megatron Bridge。即将发布的 0.17.0 版本将停止支持 Python 3.10。

- 五种并行策略（TP、PP、DP、EP、CP）与 FP16/BF16/FP8/FP4 混合精度支持
- 基准测试覆盖 2B 至 462B 参数模型、数千 GPU 规模
- Megatron Bridge 提供 Hugging Face 与 Megatron checkpoint 双向转换
- MoE 模型训练配置与 checkpoint 转换工具（DeepSeek-V3、Mixtral、Qwen3）

> L13: **Megatron-LM** is a reference example that includes Megatron Core plus pre-configured training scripts, ideal for resea
> L15: **Megatron Core** is a composable library with GPU-optimized building blocks for custom training frameworks. It provides
> L75: The codebase efficiently trains models from 2B to 462B parameters across thousands of GPUs, achieving up to **47% Model 

## rowboatlabs/rowboat（⭐18030，confidence: high）

**本地优先的个人 AI 助手，带知识图谱与团队 Spaces 协作**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

面向个人与团队的桌面端 AI 助手：将邮件、会议、Slack 与助手对话索引为 Obsidian 风格的双链知识图谱（Brain），并在此基础上提供邮件客户端、笔记、内置浏览器、会议记录、Code Mode（并行编码 agent）等工作界面。团队通过 Spaces（基于开源 Harbor 服务器）协作，各成员的助手在本机运行，仅以本人身份向房间发帖；个人数据以本地 Markdown 存储。支持 Ollama/LM Studio 本地模型或自带 API key。Mac/Windows/Linux 提供安装包，Harbor 可自托管。

- 将邮件、会议、Slack、对话索引为本地双链知识图谱
- 基于事件或定时的后台 agent，可调用工具、搜索网页并经 Claude Code/Codex 写代码
- Spaces 多人协作：@rowboat 以用户身份在房间内干活，私有上下文不出本机
- 通过 MCP 连接外部工具，本地优先存储为纯 Markdown

> L6:  Open-source personal AI assistant with built-in docs, whiteboard and email. Works solo or with your team.
> L27: Rowboat indexes your work into a living knowledge graph and uses that to get work done on your machine. It includes work
> L42: Rowboat indexes email, meetings, slack and assistant conversations into a living Obsidian-style backlinked knowledge gra

## pytorch/vision（⭐17958，confidence: high）

**给 CV 开发者提供数据集、模型架构与图像变换的 PyTorch 库**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

torchvision 是 PyTorch 官方的计算机视觉库，提供三部分内容：常用公开数据集（下载与预处理工具）、模型架构（含预训练权重）以及常见图像变换。安装需与 torch 版本配套，README 给出二者与 Python 版本的对应表；支持 torch tensors 与 PIL（含 Pillow-SIMD）两种图像后端。README 声明库本身不托管数据集，数据集与预训练模型可能附带各自的许可条款（如 SWAG 模型为 CC-BY-NC 4.0），使用许可由用户自行判断。

- 提供公开数据集、模型架构与常见图像变换
- 与 torch 版本一一配套（版本对应表）
- 支持 torch tensors 与 PIL/Pillow-SIMD 图像后端
- 部分预训练模型（SWAG）使用 CC-BY-NC 4.0 许可

> L6: The torchvision package consists of popular datasets, model architectures, and common image transformations for computer
> L7: vision.
> L60: Torchvision currently supports the following image backends:

## camel-ai/camel（⭐17917，confidence: high）

**面向研究者的多智能体系统开源框架与数据生成工具**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=idea`

CAMEL 是一个开源多智能体框架与社区，定位为研究 agent 行为与规模的实验平台。框架支持大规模 agent 系统仿真、状态记忆、角色扮演式多 agent 协作（Workforce）、多种基准测试与工具集成；提供 CoT、Self-Instruct 等合成数据生成模块，以及 Agents、Memory、Retrievers（RAG）、Benchmarks 等模块化组件。通过 PyPI 安装，附 Cookbooks 与文档，主要面向从事 Multi-Agent Systems 研究的科研群体，社区包含 100+ 研究者并附论文引用入口。

- 支持最多 1M 规模 agent 的仿真与协调（框架设计目标）
- Role Playing 与 Workforce 多智能体协作机制
- CoT、Self-Instruct、Source2Synth 等合成数据生成模块
- 含 Memory、Retrievers、Benchmarks 等 13 个核心模块

> L32:  🐫 CAMEL is an open-source community dedicated to finding the scaling laws of agents. We believe that studying these age
> L69: We are a community-driven research collective comprising over 100 researchers dedicated to advancing frontier research i
> L137: Installing CAMEL is a breeze thanks to its availability on PyPI. Simply open your terminal and run:

## Canner/WrenAI（⭐17886，confidence: high）

**给 AI agent 提供受治理 text-to-SQL 与语义层的开源 GenBI 引擎**

`ai_role=ai-ecosystem · license_risk=dual · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

以 CLI（pip 安装）与 SDK 形式提供的开源 GenBI 引擎：用 MDL 建模语言将指标定义、枚举、连接关系等业务语义以 YAML/Markdown 文件托管在 Git 中，为已有 agent（Claude Code、Cursor、MCP 客户端等）提供语义层与上下文层，把自然语言问题转成经 dry-plan 校验的 SQL 并可部署为可分享的 dashboard。核心引擎、SDK 与 skills 为 Apache-2.0 且可自托管；行列级安全、GenBI UI、Agentic Mode 等属商业版 Wren AI Cloud / Enterprise Plus。旧 Docker 版 GenBI 应用已归档至 legacy/v1 分支，无新特性与安全修复。

- MDL 语义层与 AI 上下文层以可审查的 YAML/Markdown 文件存于 Git
- 覆盖 22+ 数据源（BigQuery、Snowflake、PostgreSQL、ClickHouse 等）的治理式执行
- 提供 wren-langchain、wren-pydantic 等 Agent SDK 与 MCP server
- agent 构建的浏览器端 dashboard 可部署到 Vercel 或 Cloudflare Pages

> L24: WrenAI is the open-source **generative BI (GenBI) engine**. It gives the AI agents you already use (Claude Code, Cursor,
> L147: - **Engine**: Apache DataFusion based. BigQuery, Snowflake, PostgreSQL, ClickHouse, Amazon Redshift, Databricks, DuckDB,
> L150: - **Agent SDKs**: `wren-langchain` (LangChain / LangGraph), `wren-pydantic`, and a reference Python integration for othe

## NLP-LOVE/ML-NLP（⭐17833，confidence: high）

**机器学习/NLP 面试知识点与代码实现的中文知识库**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

面向算法工程师求职与复习的学习资料仓库：按模块整理机器学习、深度学习、NLP 面试常考知识点，每章列出可能被问到的面试问题，并附算法实战代码案例；以建立清晰知识体系为目标，定位为常读常记的复习材料。作者自述不以全面为目标，思维导图需通过微信公众号回复关键词获取。

- 机器学习/深度学习/NLP 面试常考知识点整理
- 各章附算法实战代码案例
- 按模块组织的知识体系，附思维导图获取途径

> L3: - 此项目是**机器学习、NLP面试**中常考到的**知识点和代码实现**，也是作为一个算法工程师必会的理论基础知识。
> L5: - 此项目以各个模块为切入点，让大家有一个清晰的知识体系。

## GoogleCloudPlatform/generative-ai（⭐17798，confidence: high）

**面向开发者的 Google Cloud 生成式 AI 示例与笔记本集**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Google Cloud 平台上的生成式 AI 示例仓库，收录 notebooks、代码示例与样例应用，演示如何使用 Agent Platform 开发与管理生成式 AI 工作流。按主题目录组织：Gemini 入门笔记本、Agent Search 网站与企业数据搜索、RAG 与 Grounding、Imagen/Veo 视觉、Chirp 语音，以及 Google Colab 与 Workbench 的环境配置说明。README 声明该仓库本身并非官方支持产品，代码仅作演示用途。

- 提供 Gemini 入门笔记本、函数调用与样例应用目录
- RAG 与 Grounding 主题的跨目录笔记本索引
- 涵盖 Imagen/Veo 视觉与 Chirp 语音的从零构建示例
- 提供 Google Colab 与 Workbench 环境配置说明

> L5: This repository contains notebooks, code samples, sample apps, and other resources that demonstrate how to use, develop 
> L15:  <code>gemini/</code>
> L47:  Instructions on how to set up Google Cloud, the Gen AI Python SDK, and notebook environments on Google Colab and Workbe

## rocketride-org/rocketride-server（⭐17758，confidence: high）

**在 IDE 中构建、调试和部署 AI/LLM 管线的开源引擎**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

RocketRide 是一个开源 AI 管线构建器与运行时：管线以 .pipe JSON 定义，可在 VS Code 可视化画布中编辑，由多线程 C++ 引擎执行，也可在 Docker、本地或 RocketRide Cloud 部署。README 称含 100+ 节点，覆盖 15+ LLM 提供商、9 个向量数据库、OCR、NER、PII 匿名化等，节点可用 Python 扩展；提供 Python/TypeScript/MCP SDK、VS Code 扩展，内置 CrewAI 与 LangChain 支持，带 token 用量与延迟等可观测性功能。示例管线可在本地模型上运行，无需 API key。

- 管线以可移植 JSON（.pipe）定义，VS Code 可视化画布构建与调试
- C++ 多线程运行时执行，节点可 Python 扩展
- 提供 Python、TypeScript 与 MCP SDK，集成到应用中调用
- 内建可观测性：调用树、token 用量、内存与延迟追踪

> L5:  RocketRide is the open source AIDE: the AI Development Environment.
> L14:  Under the hood, RocketRide is an open source data pipeline builder and runtime built for AI and ML workloads. With 100+
> L56: |**TypeScript, Python & MCP SDKs**|Integrate pipelines into native apps, expose them as callable tools for AI assistants

## tradecatlabs/vibe-coding-cn（⭐17656，confidence: high）

**面向中文开发者的 Vibe Coding 资源工具箱：整理提示词、Skill 与工作流资产**

`ai_role=ai-knowledge · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

以 Pi Agent 与 OpenAI GPT 为运行底座的 Vibe Coding 工具箱，将既有 Context、Skills、Extensions 组合为可验证的工作流。内容分为功法体系（思想、准则、方法与流程）、法器总表（30 项工具分级登记）、从零入门路线与 Codex 配置一键安装；交付路径为需求→上下文文档→实施计划→分步实现→自测→进度记录。仓库以 git submodule 锁定来源，Skill 通过 pi --skill 显式加载；README 声明只整理既有资产，未完成正式效能验证。

- 功法体系：按问题选用思想、准则、思维模型与工程流程
- 法器总表：30 项工具按天/地/玄/黄四阶分级登记
- 从零入门路线覆盖网络环境、CLI 配置、首个项目与 Git 闭环
- 闭环交付路径：需求→上下文→计划→实现→自测→进度记录

> L3: **以Pi Agent与OpenAI GPT为主体底座，将既有Context、Skills和Extensions组合成可验证的工作流。**
> L46: - `vibe-coding-cn` 是Vibe Coding工具箱，主体底座为Pi Agent与OpenAI GPT；本次只整理已有资产，不增加业务Skill。
> L109: 一句话：Vibe Coding = **规划驱动 + 上下文固定 + AI 结对执行**，让「从想法到可维护代码」变成一条可审计的流水线，而不是一团无法迭代的巨石文件。

## wanshuiyin/Auto-claude-code-research-in-sleep（⭐17627，confidence: low）

**给 ML 研究者提供跨模型审查循环的 Markdown 技能集**

`ai_role=ai-native · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=research`

ARIS 是一套纯 Markdown 的技能/工作流方法，用于自主 ML 研究：由执行模型驱动、独立模型（默认 Codex MCP）做跨模型审查，覆盖想法发现、实验自动化与审查循环。定位为方法论而非平台，可安装到 Claude Code、Codex CLI、Cursor、OpenClaw 等 agent 环境，也提供独立 CLI（ARIS-Code）与各平台插件发行，含 82-83 个技能；README 说明 codex-cli 0.154 移除 mcp-server 后改用 codex exec 桥接，替代模型组合无需 Claude 或 OpenAI API。

- 跨模型审查循环：执行者驱动，独立模型（默认 Codex MCP）审查
- 纯 Markdown 技能形式，82-83 个技能，无框架依赖
- 提供独立 CLI（ARIS-Code）及 Claude Code / Codex CLI / DeepSeek Harness 插件
- 支持 ModelScope 托管模型的替代模型组合，无需 Claude/OpenAI API

> L9: 🌱 *ARIS is a methodology, not a platform. What matters is the research workflow — take it wherever you go.*
> L11: 💡 *Use ARIS as a skill-based workflow in Claude Code / Codex CLI / Cursor / Trae / Antigravity / GitHub Copilot CLI / Op
> L13: 📦 *Those are the skills installed directly. Want it in one command? ARIS also ships as a standalone CLI and as plugins:*

## leon-ai/leon（⭐17584，confidence: high）

**开源个人 AI 助手：以工具、上下文、记忆与 agent 执行完成任务**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=idea`

Leon 是一个开源个人 AI 助手，围绕工具、上下文、记忆与 agentic 执行构建。三种运行模式：smart 自动选择、controlled 走确定性原生技能、agent 逐步规划；技能分 native 与 SKILL.md 格式的 agent 两类，并含可操作桌面与浏览器界面的 computer use 能力。支持本地与远程 AI 提供商以平衡隐私。需 Node.js >= 24，克隆仓库后 pnpm 运行，默认本地 http://localhost:5366 访问。当前为 2.0 Developer Preview，新文档尚未就绪。

- smart/controlled/agent 三种执行模式
- 原生技能与 SKILL.md agent 技能双层体系
- 渐进加载的 computer use 可操作桌面与浏览器界面
- 支持本地与远程 AI 提供商

> L31: **Leon** is **your open-source personal AI assistant** built around **tools, context, memory, and agentic execution**.
> L41: - Leon can run in different ways depending on the task: `smart` mode chooses for you, `controlled` mode follows determin
> L47: - Leon supports both local and remote AI providers, which helps balance privacy, control, and capability.

## NVlabs/instant-ngp（⭐17577，confidence: mid）

**给 NeRF/图形研究者：用哈希编码 MLP 秒级训练并渲染神经图形基元**

`ai_role=ai-enhanced · license_risk=none · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=research`

实现四类神经图形基元：NeRF、符号距离函数（SDF）、神经图像与神经体渲染，核心是用多分辨率哈希输入编码训练 MLP，基于 tiny-cuda-nn 框架实现。提供交互式 GUI（VR 查看、相机路径编辑、NeRF/SDF 转网格、快照保存加载）与 Python 绑定。Windows 提供按显卡系列划分的预编译包，Linux 或需要开发者绑定时须自行用 CMake 编译，要求 NVIDIA GPU 与 CUDA。README 含数据集制作、故障排查 FAQ 与 Colab 示例指引。

- 支持 NeRF、SDF、神经图像、神经体四类基元的训练与渲染
- 多分辨率哈希输入编码 + tiny-cuda-nn 框架
- GUI 含 VR 模式、相机路径编辑、网格导出与快照管理
- 全部 GUI 功能均有 Python 绑定，可脚本化运行

> L5: Here you will find an implementation of four __neural graphics primitives__, being neural radiance fields (NeRF), signed
> L6: In each case, we train and render a MLP with multiresolution hash input encoding using the __tiny-cuda-nn__ framework.
> L147: - __(optional) Python 3.8 or higher__ for interactive bindings. Also, run `pip install -r requirements.txt`.

## microsoft/data-formulator（⭐17571，confidence: high）

**给分析师的 AI 数据探索工作台：连接、分析并可视化数据**

`ai_role=ai-native · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=—`

微软研究院出品的交互式数据分析系统，将 UI 交互与自然语言结合：数据连接器统一接入文件、本地文件夹、数据库与 Databricks 等平台并维护数据间关系记忆；Data Thread 支持分支提问、对比分析路径；可视化由 Flint 图表语言驱动，支持 30+ 图表类型、风格微调 agent 与报告分享。支持 CSV/TSV/Excel/JSON/截图/文本等输入。提供桌面版（Windows/macOS，未签名）与 uv/pip/Docker 运行方式，浏览器访问 localhost:5567，UI 支持英文/中文。

- 数据连接器统一接入文件、数据库与数据平台，并维护数据关系记忆
- Data Thread 分支式分析：从任意步骤分支探索替代路径
- 基于 Flint 图表语言的 30+ 图表类型与风格微调 agent
- 通过 LiteLLM 支持 OpenAI、Azure、Ollama、Anthropic 等模型

> L73: **Data Formulator** is a Microsoft Research project for data exploration with visualizations powered by AI agents. It co
> L29: 1. **Data connectors** give agents a common way to connect to different data
> L65: - **Model Support**: OpenAI, Azure, Ollama, Anthropic via LiteLLM (feedback)

## citrolabs/ego-lite（⭐17569，confidence: high）

**让 AI agent 与用户共享同一浏览器的自动化浏览器**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

ego lite 是一款为 AI agent 设计的浏览器：agent 在浏览器内的隔离 Space 中执行自动化任务，用户可同时继续使用自己的标签页，并可通过迁移 Chrome 数据让 agent 继承已有登录、Cookie 与扩展。agent 经 `ego-browser` 技能连接层（支持 Claude Code、Codex、Cursor 等命令行 agent），以页面内 JavaScript 工具（snapshot、fill、click、navigate 等）驱动浏览器。当前仅支持 macOS（Apple Silicon/Intel），Windows 封测、Linux 在路线图中；MIT 许可，仓库内容与浏览器本体分发分离。

- 每个 agent 拥有隔离 Space，多任务并行且不占用用户标签页
- ego-browser 技能将浏览器暴露为页面内 JavaScript 工具集
- 首次启动可迁移 Chrome 数据（登录、Cookie、扩展、书签）
- 提供 npx skills add 安装 ego-browser 技能

> L24: ego (lite) is a browser where you and your AI agents work in parallel. Your agents run their browser tasks in their own 
> L89: |**Any agent can drive it through `ego-browser`**|`ego-browser` is the connection layer between any agent CLI (Claude Co
> L96: |Capability|ego lite|Browser-Use|agent-browser (Vercel)|ChatGPT Atlas|Perplexity Comet|

## lidge-jun/opencodex（⭐17528，confidence: high）

**本地代理：让 Codex/Claude Code 等工具运行任意 LLM**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=desktop · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

opencodex 是一个本地代理服务，将 Codex 的 Responses API 翻译为各提供商的协议（流式、工具调用、推理 token、图像双向转换），使 Claude Code、Codex、Claude Desktop、Grok Build 可调用 40+ 内置提供商或任意 OpenAI 兼容端点。通过 `provider/model` 语法路由模型，支持 Combo 故障转移/加权轮询、子代理任意模型、ChatGPT 账号池配额路由、xAI/Anthropic/Kimi OAuth 登录。CLI 经 npm 安装（Node 18+，Bun 运行时自动捆绑），另提供 beta 桌面应用（.dmg/.msi/.AppImage/.deb），仪表盘运行在 localhost:10100。

- 将 Codex Responses API 翻译为各提供商协议，40+ 内置提供商
- ChatGPT 账号池：配额刷新、最低用量路由、线程亲和
- Combo 虚拟模型：跨提供商 failover 或加权轮询
- 内存有界管理：14 个保留存储按 256 MiB 预算驱逐

> L48: opencodex is a lightweight local proxy that translates Codex's Responses API into whatever your
> L120: - **Use any LLM with Codex, Claude Code, Claude Desktop, and Grok Build** — 40+ providers out of
> L114: The CLI install requires Node 18+; the desktop app needs neither Node nor Bun. The Bun runtime is bundled on `npm instal

## microsoft/mcp-for-beginners（⭐17467，confidence: high）

**面向开发者的 MCP（模型上下文协议）入门教学课程**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

微软维护的开源课程，通过 .NET、Java、TypeScript、JavaScript、Rust、Python 六种语言的真实示例讲解 Model Context Protocol 基础。内容按 Foundation、Building、Growing、Mastery 四阶段组织为 11 个模块，覆盖核心概念、安全实践、服务器/客户端构建、调试与生产部署、数据库集成等；Module 11 为 13 个实验的 PostgreSQL 集成实战路径。课程基于 MCP 2026-07-28 规范编写，含 CIMD/DCR 授权对比示例，并提供 50+ 语言翻译（可 sparse checkout 跳过翻译目录）。

- 六种语言（C#/Java/TS/JS/Rust/Python）的跨语言实战示例
- 11 个模块分四阶段学习路径，Module 11 含 13 个动手实验
- 基于 MCP 2026-07-28 规范，覆盖无状态请求与 Extensions 框架
- 提供 50+ 语言翻译及稀疏克隆方式

> L48: ## **Learn MCP with Hands-on Code Examples in C#, Java, JavaScript, Rust, Python, and TypeScript**
> L61: The current protocol revision is **MCP Specification 2026-07-28**. The MCP
> L149: Module 11 deserves special mention - it's a complete 13-lab hands-on learning path that teaches you to build production-

## RyanCodrai/turbovec（⭐17394，confidence: high）

**面向 Python/Rust 开发者的 2-4 比特量化内存向量索引库**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=research`

基于 Google Research TurboQuant 的进程内向量索引，提供 Python 与 Rust 双 API。将向量以 2 或 4 bit/维存储并用 SIMD 内核直接检索，无需训练步骤，支持增量持久化（sync 只写变更）、id 过滤搜索与微秒级删除。以库而非服务形式分发，无网络 API；x86 内核运行时按 CPU 特性选择。提供与 LangChain、LlamaIndex、Haystack、Agno 的集成包，并可从源码用 maturin 构建。

- 2/4 bit 每维量化存储，内存较 float32 缩小 7.8–15.5 倍
- 无需训练与重建，增删向量即时生效，sync() 增量落盘且崩溃安全
- 提供 LangChain/LlamaIndex/Haystack/Agno 的 drop-in 替代集成
- Rust API 与 Python 对应，支持 allowlist/bitmask 过滤检索

> L17: turbovec is an in-process vector index for Python and Rust. It stores each vector at 2 or 4 bits per dimension using Goo
> L50: Framework integrations are drop-in replacements for each framework's in-memory store — same public surface, same persist
> L95: - **You need a graph index.** turbovec scans every vector. At 100K vectors a query costs 0.13–0.25 ms on all eight cores

## langchain-ai/openwiki（⭐17231，confidence: high）

**为代码库生成并维护代理可读的 Markdown wiki 的 CLI**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

OpenWiki 将代码库与知识源转换为相互链接的 Markdown wiki，供编码代理检索上下文、回答问题。工作流为：在编码代理内或通过独立 CLI 初始化 wiki，工具以 Claims 形式把事实追溯到源证据，后续更新只处理变更部分，支持中断恢复与逐页保存进度。可通过 openwiki link 将多个仓库组成 workspace 做跨库检索，内置本地可视化图谱与静态导出，并提供 GitHub Actions/GitLab CI/Bitbucket 定时更新模板。依赖 Node.js 22.22.0+。

- Claims 溯源机制：事实关联源证据，更新时识别需关注的部分
- 通过 MCP 生命周期工具（begin/submit_plan/next_page/…）与宿主代理协作
- openwiki link 组建跨仓库 workspace 检索与阅读
- 提供交互式图谱可视化与可发布的静态导出

> L13: OpenWiki turns your codebase and knowledge sources into a linked Markdown wiki that you own. Your coding agent can use i
> L30: The easiest way to get started is inside the coding agent you already use. OpenWiki uses that agent's authenticated mode
> L96: The MCP generation lifecycle is `openwiki_begin → openwiki_submit_plan → openwiki_next_page → openwiki_submit_page → … →

## xx025/carrot（⭐17203，confidence: high）

**面向普通用户的 AI 工具网站导航清单，按类别收录可用站点**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

以列表形式收录 AI 助手、Agent、开发工具、创作工具和行业应用类网站的导航目录，附发布网站与 Issues 反馈渠道。条目按「热门、通用助手与智能搜索、Agent 与自动化、模型/API 与算力、编程与开发工具、图像设计、音视频、写作办公」等类别组织，每条含名称、简介、链接及免费/需登录/需国际网络等标注。通过 Issues 接受站点提交、失效反馈与信息更正。未提供本地安装或运行方式。

- 按用途分类的 AI 工具站点目录，含免费/需登录/需国际网络标注
- 覆盖助手、Agent、API 算力、编程、图像、音视频、写作办公等类别
- 通过 GitHub Issues 接收站点提交与失效反馈

> L4: 这里收录了可用的 AI 助手、Agent、开发工具、创作工具和行业应用。
> L15: ## 热门
> L820: ## Agent 与自动化

## QwenLM/Qwen-Agent（⭐17186，confidence: high）

**面向开发者的 Qwen 系列 LLM 应用开发 Agent 框架**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

基于 Qwen 模型的指令遵循、工具使用、规划与记忆能力构建 LLM 应用的 Python 框架，提供 BaseChatModel、BaseTool、Agent 等原子与高层组件，内置 Function Calling、MCP 接入、基于本地 Docker 容器的 Code Interpreter 与快速 RAG 方案，附带 Gradio WebUI 部署及 BrowserQwen 浏览器助手等示例应用。模型服务可使用阿里云 DashScope API 或自行部署 OpenAI 兼容服务（vLLM/Ollama）。代码解释器沙箱隔离为基本实现，官方提示在生产环境谨慎使用；GUI 需 Python 3.10+。

- 提供 Function Calling、MCP、Code Interpreter、RAG 等内置能力
- 基于本地 Docker 容器的代码解释器沙箱执行
- 支持 1M token 超长文档问答的快速 RAG 方案
- Gradio WebUI 一行代码部署 Agent 界面

> L7: Qwen-Agent is a framework for developing LLM applications based on the instruction following, tool usage, planning, and
> L59: Qwen-Agent offers atomic components, such as LLMs (which inherit from `class BaseChatModel` and come with function calli
> L86: We implement a code interpreter tool based on local Docker containers. You can enable the built-in `code interpreter` to

## MemoriLabs/Memori（⭐17151，confidence: high）

**面向 agent 的记忆基础设施：把执行与对话转为持久化结构化记忆**

`ai_role=ai-native · license_risk=none · deploy=library · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

提供 Python 与 TypeScript SDK 的 agent 记忆层，将 LLM 交互与 agent 执行（含工具调用、决策、结果）捕获为按 entity/process/session 分级的结构化记忆，后台增强生成 attributes、facts、preferences 等类型，不增加请求延迟。LLM、数据存储与框架无关，支持 OpenAI 等多种 LLM 与 LangChain 等框架，可接入自有数据库（BYODB）或使用 Memori Cloud；通过 MCP 一条命令接入 Claude Code、Cursor 等客户端；默认高级增强免账号但限速。

- entity/process/session 三级记忆归属与后台增强（attributes/facts/preferences 等）
- MCP 单命令接入 Claude Code、Cursor、Codex、Warp 等客户端，无需 SDK 集成
- LLM/datastore/framework 无关，提供 BYODB 模式接入自有数据库
- OpenClaw 插件与 Hermes 记忆 provider 两种开箱集成

> L3:  Memory from what agents do, not just what they say.
> L43: Set `MEMORI_API_KEY` and your LLM API key (e.g. `OPENAI_API_KEY`), then:
> L170: ## Supported LLMs

## kubesphere/kubesphere（⭐17060，confidence: mid）

**企业级 Kubernetes 容器平台：多云/多集群/边缘统一管理**

`ai_role=ai-ecosystem · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

以 Kubernetes 为内核的分布式云原生应用管理系统，采用微内核+扩展组件架构（LuBan），核心仅含基础功能，功能模块以扩展组件形式在运行期动态管理。功能覆盖多集群集中管控与应用跨云分发、基于 Argo CD 与 Jenkins 的 DevOps 流水线、多租户 RBAC 与配额、监控告警日志、基于 Istio 的服务 Mesh、Helm 应用商店、集成 KubeEdge 的边缘部署、GPU 工作负载调度与配额管理。通过 Helm 在既有 K8s 集群安装，也托管于多家云厂商一键部署，支持离线（air-gapped）安装。

- 多集群集中控制面，支持应用跨云厂商分发
- 微内核+扩展组件架构（LuBan），运行期动态管理扩展
- 集成 KubeEdge 的边缘计算平台与 GPU 负载调度
- Helm 一条命令安装，支持离线 air-gapped 部署

> L3:  The container platform tailored for Kubernetes multi-cloud, datacenter, and edge management
> L75: KubeSphere 4.x adopts a microkernel + extension components architecture (codename LuBan). The core part (KubeSphere Core
> L97: helm upgrade --install -n kubesphere-system --create-namespace ks-core https://charts.kubesphere.io/main/ks-core-1.1.3.t

## argoproj/argo-workflows（⭐17040，confidence: high）

**面向 Kubernetes 的容器化并行任务工作流引擎**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Argo Workflows 是以 Kubernetes CRD 形式实现的开源工作流引擎，用于编排并行作业：每个步骤以容器运行，支持以任务序列或 DAG 建模多步骤流程。提供工作流模板、cron 定时调度、归档、重试/超时/挂起恢复、步骤级输入输出、UI 管理界面、REST/gRPC 服务端接口以及 Java/Golang/Python/TypeScript SDK。制品存储支持 S3、GCS、Azure Blob 等。面向在 Kubernetes 上运行机器学习、数据处理、CI/CD 等计算密集型作业的用户。为 CNCF 毕业项目。

- 以 Kubernetes CRD 实现，每步为一个容器
- 支持 DAG 与 Steps 两种工作流声明方式
- 提供 UI、REST/gRPC 接口与四种语言 SDK
- 支持 cron 调度、重试、超时、归档、并行度限制等

> L14: Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes.
> L15: Argo Workflows is implemented as a Kubernetes CRD (Custom Resource Definition).
> L21: Argo is a Cloud Native Computing Foundation (CNCF) graduated project.

## cft0808/edict（⭐16995，confidence: high）

**给个人/团队用的多 Agent 协作编排系统，以三省六部制分权制衡执行任务**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

基于 OpenClaw 的多 Agent 编排系统，由 12 个 Agent 模拟三省六部流程：太子分拣消息、中书省规划、门下省审议封驳、尚书省派发、六部与吏部并行执行。配套 React 军机处看板，提供 Kanban 任务管理、任务叫停/取消/恢复、奏折归档、模型热切换、技能管理、Token 统计与新闻推送。依赖已安装的 OpenClaw、Python 3.10+ 与 macOS/Linux，后端基于 Python 标准库 http.server，服务间经 Redis Streams 事件总线通信，支持 Docker Demo 镜像与 systemd 部署。

- 门下省专职审核，封驳不合格产出并强制返工
- Kanban 看板实时监控，支持叫停/取消/恢复与状态机校验
- Agent 权限矩阵与奏折流转审计日志
- 看板内按 Agent 热切换 LLM 与远程 Skills 导入

> L5:  12 个 AI Agent（11 个业务角色 + 1 个兼容角色）组成三省六部：太子分拣、中书省规划、门下省审核封驳、尚书省派发、六部+吏部并行执行。 比 CrewAI 多一层 制度性审核 ，比 AutoGen 多一个 实时看板 。
> L97: ### 📋 军机处看板（10 个功能面板）
> L217: - OpenClaw 已安装

## composio-community/awesome-codex-skills（⭐16941，confidence: mid）

**为 Codex CLI/API 用户提供自动化工作流技能的策展清单**

`ai_role=ai-ecosystem · license_risk=none · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

由 Composio 维护的 Codex 技能清单，按开发工具、效率协作、写作、数据分析、元工具等类别收录数十个 SKILL.md 格式的技能条目，覆盖代码审查、迁移审计、会议纪要、发票整理、幻灯片生成等场景。提供 Python 技能安装脚本与手动复制两种安装方式，技能放入 $CODEX_HOME/skills 目录后由 Codex 按 description 触发；同时包含技能创建模板与最佳实践说明。

- 分类收录数十个 Codex 技能（SKILL.md 格式）
- 提供 skill-installer Python 脚本从 GitHub 安装技能
- 含 SKILL.md 模板与渐进式披露的技能创建指南
- 配套 Composio MCP Gateway 提供 1,000+ 集成的接入入口

> L25: A curated list of practical Codex skills for automating workflows across the Codex CLI and API.
> L56: Codex skills are modular instruction bundles that tell Codex how to execute a task the way you want it done. Each skill 

## weaviate/weaviate（⭐16886，confidence: mid）

**面向开发者的开源向量数据库，支持语义搜索与 RAG**

`ai_role=ai-ecosystem · license_risk=dual · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

用 Go 编写的云原生向量数据库，同时存储对象与向量，将向量相似搜索、关键词过滤、检索增强生成（RAG）与重排序整合在单一查询接口。支持导入时用集成模型自动向量化，或直接导入预计算向量；生产部署内置多租户、复制、RBAC 与向量压缩。通过 REST/gRPC/GraphQL API 访问，提供 Python、JavaScript/TypeScript、Java、Go、C# 等客户端库。许可为 BSD 3-Clause 加 wl/ 目录下的商业许可，企业功能需许可证密钥。

- 向量搜索、关键词过滤、RAG 与重排序在单一查询接口
- 导入时自动向量化（集成 OpenAI、Cohere、HuggingFace 等模型）或导入自有向量
- 内置多租户、复制、RBAC、向量压缩等生产特性
- 提供面向 Claude Code、Cursor 等 coding agent 的 Weaviate Agent Skills

> L9: **Weaviate** is a cloud-native vector database that stores both objects and vectors, enabling semantic search at scale. 
> L75: Weaviate exposes REST API, gRPC API, and GraphQL API to communicate with the database server.
> L146: |**LLM and Agent Frameworks**|Build agents and generative AI applications|Agno, Composio, CrewAI, DSPy, Dynamiq, Haystac

## QwenLM/Qwen3-Coder（⭐16833，confidence: mid）

**为开发者提供的代码生成与 Agentic Coding 开源大语言模型系列**

`ai_role=ai-native · license_risk=none · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=research`

Qwen 团队发布的 Qwen3 系列代码模型，含 Qwen3-Coder-Next（基于 Qwen3-Next-80B-A3B-Base，混合注意力与 MoE 架构）、480B-A35B 与 30B-A3B 三个规模，另有 Base 与 FP8/GGUF 版本。模型原生支持 256K 上下文（可用 Yarn 扩展至 1M），覆盖 358 种编程语言，支持 FIM 代码补全，仅支持非思考模式。提供 transformers 推理示例；function calling 依赖 SGLang 与 vLLM 中的新工具解析器。权重发布于 Hugging Face 与 ModelScope。

- 支持 358 种编程语言与 256K 原生上下文（Yarn 可扩展至 1M）
- 支持 FIM（fill-in-the-middle）代码补全任务
- 兼容 Qwen Code、CLINE、Claude Code 等平台的函数调用格式
- 提供 Instruct/Base 与 FP8/GGUF 多种权重版本

> L13: We are announcing Qwen3-Coder, our most agentic code model to date. **Qwen3-Coder** is available in multiple sizes, **Qw
> L15: **Qwen3-Coder-Next**, an open-weight language model designed specifically for coding agents and local development. Built
> L23: 📚 **Long-context Capabilities**: with native support for **256K** tokens, extendable up to **1M** tokens using Yarn, opt

## datawhalechina/leedl-tutorial（⭐16812，confidence: high）

**面向中文读者的李宏毅深度学习课程整理教程（PDF 书籍）**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Datawhale 组织维护的开源中文教程，内容整理自李宏毅《机器学习》（2021 年春）课程并补充推导与扩展章节，覆盖深度学习基础、CNN/RNN/Transformer、GAN、BERT/GPT-3、扩散模型、强化学习、网络压缩、元学习与 ChatGPT 原理等主题，每章由不同贡献者署名编写。提供 Releases 页 PDF 下载与百度网盘国内地址，纸质版由人民邮电出版社出版，附勘误表页面和 Homework 文件夹配套代码。采用 CC BY-NC-SA 4.0 许可。

- PDF 全书经 Releases 与百度网盘提供下载
- 章节覆盖 GAN、BERT、扩散模型、强化学习、元学习、ChatGPT 等 17 个主题
- 提供 Homework 文件夹配套代码与在线勘误表
- 纸质版由人民邮电出版社出版，中英双 BibTeX 引用条目

> L3: # 李宏毅深度学习教程LeeDL-Tutorial（苹果书）
> L43: * **引言** @王琦
> L94: ## 配套代码
> L133: 知识共享许可协议 本作品采用知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议进行许可。

## xbtlin/ai-berkshire（⭐16774，confidence: mid）

**给个人投资者的 Claude Code/Codex 价值投研 Skill 框架**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

一套可装入 Claude Code 与 Codex 的投资研究 Skill 合集（20 个入口），将四位价值投资者的方法论结构化为可执行流程，覆盖个股深度研究、财报精读、行业筛选、持仓管理。核心机制包括：Team Lead 并行调度 4 个大师视角 Agent 独立研究后综合、强制输出通过/不通过/灰色地带结论、A/B/C 信息丰富度评级与快速否决清单、Python decimal 精确计算与多源数据交叉验证。安装依赖先装 Claude Code 或 Codex 客户端，再克隆仓库运行脚本复制 skills。README 含实盘收益宣传，属维护者自述。

- 20 个 Skill 入口：深度研究、财报分析、行业筛选、持仓管理、思维工具
- /investment-team 启动 4 个独立 Agent 并行研究，Team Lead 综合
- 数据用 Python decimal 精确计算，关键数据至少 2 个独立来源交叉验证
- 同时维护 Claude Code commands 与 Codex skills 两套入口及同步脚本

> L11: **AI Berkshire** 是一套同时兼容 Claude Code 与 Codex 的投资研究 Skill 合集，将巴菲特、芒格、段永平、李录四位价值投资大师的方法论系统化、结构化，通过 AI Agent 实现专业级投资研究。
> L158: - **Skill 层**：把"你要做什么"抽象成 20 个明确入口——深度研究、财报分析、行业筛选、持仓管理、思维工具，按场景选用
> L232: ```bash

## HKUDS/DeepCode（⭐16723，confidence: mid）

**多客户端编程 Agent：把论文与自然语言转成代码**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

HKUDS 出品的多 Agent 编程系统，围绕一个共享的本地后台服务提供 TUI、Desktop 与 Web 三种客户端，三者共享项目、会话历史、模型配置、Skills、权限与自动化。会话支持历史保留、上下文窗口上限与 /compact 压缩，后台服务自动迁移端口并支持跨客户端续接任务。安全机制包括命令沙箱、凭据隔离与可选的出站主机限制。支持语音听写、MCP 服务器管理与中文界面，Windows/macOS/Linux 均可运行。

- TUI/Desktop/Web 三客户端共享同一本地服务与会话状态
- 命令沙箱隔离模型密钥与 SSH 私钥，可选出站主机限制
- 会话上下文窗口上限（/context）与 /compact 压缩机制
- MCP 服务器管理、语音听写、Paper2Code 功能

> L41: DeepCode provides TUI, Desktop, and Web clients over one shared local service.
> L55: *🎯 **Watch our complete introduction** - See how DeepCode transforms research papers and natural language into productio
> L187: - **Choose your interface.** Run `deepcode` for the TUI, `deepcode desktop`

## bharathgs/Awesome-pytorch-list（⭐16708，confidence: high）

**为 PyTorch 用户整理的 GitHub 相关资源清单**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=medium · maturity=—`

按类别组织的 PyTorch 相关 GitHub 项目清单，收录模型实现、辅助库与教程等内容。清单分为 PyTorch 相关库、NLP 与语音处理、计算机视觉、概率/生成模型库、其他库等章节，每条目为一行链接与简介。内容以引用外部仓库为主，README 本身不含安装或运行说明。

- 收录 NLP 与语音处理类 PyTorch 项目 44 条
- 收录计算机视觉类项目 37 条
- 收录概率/生成模型库 10 条
- 按领域分章节组织的目录结构

> L1: Awesome-Pytorch-list
> L7: ## Pytorch & related libraries
> L12: ### NLP & Speech Processing:

## owainlewis/awesome-artificial-intelligence（⭐16682，confidence: high）

**面向开发者学习构建生成式与 Agent 系统的 AI 资源清单**

`ai_role=ai-knowledge · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

一份由自动化流程每周评审维护的 AI 学习与实践资源精选清单，收录书籍、课程、论文、指南与开源工具链接，覆盖基础理论、LLM 应用工程、协议规范、Agent 框架、检索、评估、部署观测及编码 Agent 等分类。声明每条目须经质量门槛筛选，非全量产品目录。以 Markdown 清单形式提供，无安装或运行环节，资源多为外部链接。

- 按学习路径组织：书籍/课程/基础论文到构建、评估、部署
- 收录 Agent 框架、MCP/A2A 协议及编码 Agent 等工程资源条目
- 声明由证据驱动的自动化流程每周评审与合并更新

> L3: An opinionated, actively maintained collection of resources for software developers learning to build and ship generativ
> L14: This is not a comprehensive directory of AI products. Every entry must clear an absolute quality bar for technical depth
> L20: ## Learn

## googleapis/mcp-toolbox（⭐16673，confidence: high）

**连接 AI agent/IDE 与企业数据库的开源 MCP 服务器**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=—`

Google 维护的 Model Context Protocol 服务器，双用途：一是开箱即用的预置通用工具（如 list_tables、execute_sql），让 Gemini CLI、Claude Code、Codex 等 MCP 客户端直接探索数据库、生成代码；二是通过 tools.yaml 定义结构化查询、语义搜索与 NL2SQL 的自定义工具框架，供生产 agent 集成。内置连接池、IAM 认证与 OpenTelemetry 可观测性。支持 AlloyDB、BigQuery、PostgreSQL、MySQL、MongoDB、Redis 等多种数据库，提供二进制、Docker、Homebrew、Go、npm 等多种安装方式。

- 预置通用工具可直接接入 Gemini CLI、Claude Code、Codex 等 MCP 客户端
- tools.yaml 自定义工具框架：结构化查询、语义搜索、NL2SQL
- 支持 AlloyDB、BigQuery、PostgreSQL、MySQL、MongoDB、Redis 等多种数据库
- 内置连接池、IAM 集成认证与 OpenTelemetry 指标与追踪

> L18: MCP Toolbox for Databases is an open source Model Context Protocol (MCP) server that connects your AI agents, IDEs, and 
> L23: 1. **Ready-to-use MCP Server (Build-Time):** Instantly connect Gemini CLI, Google Antigravity, Claude Code, Codex, or ot
> L24: 2. **Custom Tools Framework (Run-Time):** A robust framework to build specialized, highly secure AI tools for your produ

## udecode/plate（⭐16658，confidence: high）

**为 React 开发者提供带 AI 能力的富文本编辑器框架**

`ai_role=ai-ecosystem · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

基于 Slate 的 React 富文本编辑器框架，README 提供三种起步模板：Notion 风格模板（含插件与 AI）、playground 模板、最小模板。核心机制通过插件体系组织功能，文档站与中文文档、Discord 中文频道支持中文使用者。README 本身内容简短，功能细节需查阅文档。

- 基于 Slate 的 React 富文本编辑器框架
- 提供 Notion 风格、playground、minimal 三种模板
- 模板可组合插件与 AI 能力
- 提供中文文档与 Discord 中文频道

> L1: Plate
> L11: |Option|Plate|Plugins|AI|Backend|
> L25: ## 中文文档

## browser-use/web-ui（⭐16617，confidence: mid）

**基于 Gradio 的浏览器 AI Agent Web 界面**

`ai_role=ai-native · license_risk=permissive · deploy=desktop · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

在 browser-use 基础上构建的 Web UI，通过 Gradio 提供对浏览器 agent 功能的图形化操作界面。集成多家 LLM 提供商，支持使用用户自有浏览器（复用登录态与认证），支持在任务间保持浏览器会话以保留完整交互历史，并提供高清屏幕录制。提供本地 Python（uv）与 Docker 两种安装方式，Docker 部署附带 VNC 以查看浏览器操作过程，支持 ARM64 平台。

- 基于 Gradio 的 Web 界面，支持多数 browser-use 功能
- 集成多家 LLM：Google、OpenAI、Azure OpenAI、Anthropic、DeepSeek、Ollama 等
- 支持使用自有浏览器，复用登录态并支持高清录屏
- Docker 部署附 VNC 观看浏览器交互，支持 ARM64

> L8: This project builds upon the foundation of the browser-use, which is designed to make websites accessible for AI agents.
> L12: **WebUI:** is built on Gradio and supports most of `browser-use` functionalities. This UI is designed to be user-friendl
> L14: **Expanded LLM Support:** We've integrated support for various Large Language Models (LLMs), including: Google, OpenAI, 

## memvid/memvid（⭐16603，confidence: high）

**为 AI Agent 提供单文件、免数据库的持久记忆层**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=—`

Memvid 将数据、嵌入、检索结构与元数据打包为单个 .mv2 文件，作为 AI Agent 的可移植记忆层，无需运行 RAG 流水线或服务器式向量数据库。核心机制是把记忆组织为不可变的 Smart Frame 序列（借鉴视频编码思路），支持追加写入、按时间线回溯与分支、崩溃安全。提供 CLI、Node.js、Python、Rust SDK；检索支持 BM25 全文、本地 ONNX 向量嵌入（BGE/Nomic/GTE）与 OpenAI 云端嵌入，需 Rust 1.85+。README 中含 LoCoMo 等基准数据，此处不作评价。

- 数据、嵌入与索引打包为单个 .mv2 文件，无 sidecar 文件
- Smart Frame 追加式设计：支持时间线回溯、分支与查询过去状态
- 本地 ONNX 嵌入（BGE/Nomic/GTE）与 OpenAI API 嵌入可选
- 提供 npm、pip、cargo 多语言 SDK 与 CLI

> L6:  Memvid is a single-file memory layer for AI agents with instant retrieval and long-term memory.
> L38: Memvid is a portable AI memory system that packages your data, embeddings, search structure, and metadata into a single 
> L42: The result is a model-agnostic, infrastructure-free memory layer that gives AI agents persistent, long-term memory they 

## triggerdotdev/trigger.dev（⭐16562，confidence: high）

**为开发者提供 TypeScript 平台构建部署持久化 AI 工作流**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

开源的 TypeScript AI 工作流构建平台：以 SDK 形式在用户代码库中编写任务，部署后获得无超时的长运行任务、自动重试、队列与幂等、检查点与版本化，并附全量日志追踪的可观测面板。支持人审节点暂停、流式输出回传前端、批量触发与多环境管理；可使用云托管或通过 Docker Compose / Helm 自托管。任务运行时可运行浏览器、Python 脚本、FFmpeg 等系统包。

- 长运行任务无超时，带自动重试、队列与幂等机制
- 人机协同节点：任务可暂停等待人工审批或反馈
- 实时运行订阅与 LLM 流式输出支持
- 提供 Docker Compose 与 Kubernetes Helm chart 自托管路径

> L19: Trigger.dev is the open-source platform for building AI workflows in TypeScript. Long-running tasks with retries, queues
> L103: - Docker self-hosting guide - use Docker Compose to spin up a Trigger.dev instance

## pipecat-ai/pipecat（⭐16552，confidence: high）

**给开发者构建实时语音与多模态 AI 代理的 Python 框架**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

Pipecat 是一个用于构建实时语音与多模态对话代理的开源 Python 框架，由 Daily 与社区维护。它编排音频/视频、AI 服务、传输层与对话管道，支持单代理或多代理系统（交接、并行分发、共享总线，可跨进程与机器分布式运行）。传输层支持 WebSockets 与 WebRTC。核心框架默认轻量，第三方 AI 服务依赖通过 extras 按需添加。需要 Python 3.11+，用 uv 安装；提供 CLI 脚手架、客户端 SDK（JS/React/Swift/Kotlin/C++/ESP32）、调试工具与 Pipecat Cloud 部署。

- 语音优先管道：集成语音识别、TTS 与对话处理，支持多模态（语音/视频/图像）
- 多代理系统：每个管道即一个代理，支持 handoff、并行 fan-out、sidecar 与分布式部署
- 大量可插拔服务：LLM、STT、TTS、传输、视频、VAD 等数十家服务商
- 官方多平台客户端 SDK：JavaScript/React/React Native/Swift/Kotlin/C++/ESP32

> L7: **Pipecat** is an open-source Python framework for building real-time voice and multimodal conversational agents. Build 
> L26: - **Multi-Agent Ready**: Each pipeline is an agent. Compose them with handoff, parallel fan-out, sidecar workers, or dis
> L87: |LLMs|Anthropic, AWS, Azure, Baseten, Cerebras, Crusoe, DeepSeek, Fireworks AI, Gemini, Grok, Groq, Inception, Mistral, 

## NVIDIA/OpenShell（⭐16511，confidence: high）

**为自主 AI agent 提供安全隔离运行时与策略管控**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

面向多 agent 舰队（fleets of autonomous AI agents）的运行时：agent 需要读文件、装包、调 API、用凭证才有用，OpenShell 通过策略声明限定其可触达范围并在运行时强制执行。机制包括内核级隔离沙箱（文件、系统调用、网络逐一管控，真实凭证不暴露给 agent）与形式化验证（策略变更先标记高风险新增访问，等待人工审查）。提供 CLI 安装脚本、Python/TypeScript/Go/Rust SDK、agent skills 包及 Helm 部署网关。

- 内核级沙箱强制执行文件/系统调用/网络策略
- 策略变更经形式化验证后进入人工审查
- 凭证仅注入发往已批准端点的请求
- 提供 Python/TypeScript/Go/Rust 四语言 SDK 与 Helm 部署

> L11: OpenShell is the safe, private runtime for fleets of autonomous AI agents. Agents are most useful when they can read fil
> L15: OpenShell governs what agents can do in two ways: it instruments the kernel to enforce policy on every file access, syst
> L17: - **Kernel-level enforcement.** Each agent runs in an isolated sandbox. Kernel controls confine which files it can acces

## piskvorky/gensim（⭐16504，confidence: high）

**面向 NLP/IR 社区的 Python 主题建模与相似度检索库**

`ai_role=ai-ecosystem · license_risk=viral · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=research`

Gensim 是处理大规模语料的 Python 库，提供主题建模、文档索引与相似度检索。算法对语料规模内存无关，可流式处理超出 RAM 的输入；提供 LSA、LDA、RP、HDP、word2vec 等算法的多核实现，并支持在集群上分布式运行 LSA/LDA。通过依赖 NumPy 调用底层 BLAS 库（如 MKL、ATLAS、OpenBLAS）获得性能。目前处于稳定维护模式，不接受新特性，仅接受 bug 与文档修复；4.0.0 起不再支持 Python 2.7。

- 内存无关的流式处理，可处理大于 RAM 的语料
- LSA/LDA/RP/HDP/word2vec 等算法的多核实现
- 支持在计算机集群上分布式运行 LSA 与 LDA
- 提供文档与 Jupyter Notebook 教程

> L10: Gensim is a Python library for *topic modelling*, *document indexing*
> L12: *natural language processing* (NLP) and *information retrieval* (IR)
> L17: ## ⚠️ Gensim is in stable maintenance mode: we are not accepting new features, but bug and documentation fixes are still

## MODSetter/SurfSense（⭐16492，confidence: high）

**本地离线运行的开源 NotebookLM 替代桌面应用**

`ai_role=ai-enhanced · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=—`

面向需要在本地处理文档的用户：桌面应用读取 PDF、Office、图像、音视频等格式，提供带引用的回答、文档创建、编辑副本与格式转换，索引保存在本机磁盘，模型可任选本地或 OpenAI 兼容远程 API，无需账号。官方插件（Google 搜索、网页爬取、YouTube 等）需输入邮箱获取 30 天免费许可证；第三方接入走 MCP。托管网页版将停止服务，需在期限内导出工作区迁移到桌面版。

- 支持 PDF/Word/Excel/PPT/图像/录音等多种格式的研究、创建、编辑与转换
- 索引保留在本地磁盘，可选用本地模型，无需账号
- 插件生态：官方网络插件 + MCP 服务器接入
- Apache-2.0 许可，提供 Windows/macOS/Linux 安装包

> L28: SurfSense is a free, open-source desktop app for documents you can't upload. A privacy-focused, NotebookLM-style AI agen
> L91: |Open source|No|**Apache-2.0**|
> L97: Apache-2.0. See LICENSE.

## huggingface/transformers.js（⭐16349，confidence: high）

**Web 开发者在浏览器中运行 Transformer 预训练模型的 JS 库**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

Transformers.js 是 Hugging Face transformers Python 库在 JavaScript 上的功能等价实现，通过 ONNX Runtime 在浏览器内运行预训练模型，无需服务器。API 与 Python 版一致，提供 pipeline 接口；任务覆盖 NLP、计算机视觉、音频与多模态共数十种。模型默认通过 WASM 在 CPU 上运行，可设置 device: 'webgpu' 切换到 GPU；在浏览器等资源受限环境中可通过 dtype 选项选择 fp32/fp16/q8/q4 量化以降低带宽。经 NPM 安装，也可通过 CDN 直接引入。

- 基于 ONNX Runtime 在浏览器运行预训练模型，无需服务器
- 支持 NLP、视觉、音频、多模态等多类任务（含任务/架构支持清单）
- 默认 WASM/CPU 运行，可配置 WebGPU
- 支持 fp32/fp16/q8/q4 量化以适配资源受限环境

> L11: Run 🤗 Transformers directly in your browser, with no need for a server!
> L13: Transformers.js is designed to be functionally equivalent to Hugging Face's transformers python library, meaning you can
> L19: Transformers.js uses ONNX Runtime to run models in the browser. The best part about it, is that you can easily convert y

## Arindam200/awesome-ai-apps（⭐16308，confidence: high）

**面向开发者的 132 个 LLM 应用示例合集（agent/RAG/MCP/语音）**

`ai_role=ai-knowledge · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

收录 132 个项目、教程与配方的清单仓库，覆盖文本 agent、语音助手、RAG 应用与 MCP 工具等 LLM 应用类型，按 Starter Agents、Simple Agents、Voice Agents、MCP Agents、Memory Agents、RAG Applications 等类别组织，每个条目注明所用框架（AutoGen、LangChain/LangGraph、CrewAI、Agno、LlamaIndex、LiveKit、Pipecat 等）。面向学习各 AI 框架与技术栈的开发者，作为参考指南使用，多数示例由 Nebius Token Factory 等赞助方提供推理支持。

- 收录 132 个 LLM 应用示例项目，按 6+ 类别组织
- 覆盖 text agent、voice assistant、RAG、MCP 工具等类型
- 条目标明所用框架与技术栈，便于按框架检索
- 部分类别含多 agent、记忆与沙箱执行等进阶示例

> L7: This repository is a comprehensive collection of **132 projects**, tutorials, and recipes for building powerful LLM-powe
> L119: **Quick-start agents for learning and extending different AI frameworks.** _21 projects_
> L184: **Examples using Model Context Protocol for external tool integration.** _14 projects_

## dagster-io/dagster（⭐16284，confidence: high）

**面向数据资产的管道编排平台，覆盖开发到生产全周期**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

Dagster 是一个云原生数据管道编排器：以 Python 函数声明式定义数据资产（表、数据集、机器学习模型、报告），由平台在合适时机运行函数并保持资产更新。内置血缘追踪与可观测性、集中元数据管理、多租户编排引擎，支持本地开发、单元测试、集成测试到生产的完整生命周期。通过 PyPI 分发，官方支持 Python 3.9–3.14，提供 Web UI 与 dg CLI，并维护数据工具集成库。

- 以 Python 函数声明式定义数据资产并自动调度运行
- Web UI 中可视化资产血缘图，内置元数据编目与诊断
- 覆盖本地开发、单元/集成测试、staging 到生产的全生命周期
- 提供多租户、多工具的编排引擎与数据工具集成库

> L27: **Dagster is a cloud-native data pipeline orchestrator for the whole development lifecycle, with integrated lineage and 
> L29: It is designed for **developing and maintaining data assets**, such as tables, data sets, machine learning models, and r
> L52: Dagster is available on PyPI and officially supports Python 3.9 through Python 3.14.

## WEIFENG2333/VideoCaptioner（⭐16269，confidence: high）

**给视频创作者提供 LLM 驱动的字幕生成、优化与翻译工具**

`ai_role=ai-enhanced · license_risk=viral · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

基于大语言模型的视频字幕处理工具，覆盖语音识别、字幕断句、LLM 优化、翻译与视频合成的全流程。提供 CLI 与 GUI 桌面版两种形态，pip 安装即用；必剪语音识别与必应/谷歌翻译为免费功能，无需 API Key。LLM 仅用于字幕优化和大模型翻译，支持所有 OpenAI 兼容接口服务商。另提供 Claude Code Skill，使 AI 编程助手可直接调用该工具处理视频。开发依赖 uv 管理环境。

- 语音识别、断句、LLM 优化、翻译、视频合成一站式 CLI 命令
- 免费功能（必剪识别、必应/谷歌翻译）安装即用、无需 API Key
- 支持所有 OpenAI 兼容接口的服务商
- 提供 Claude Code Skill 供 AI 编程助手调用

> L3:  基于大语言模型的视频字幕处理工具 — 语音识别、字幕优化、翻译、视频合成一站式处理
> L39: |`transcribe`|语音转字幕。引擎：`faster-whisper`、`whisper-api`、`bijian`（免费）、`jianying`（免费）、`whisper-cpp`|
> L100: 音视频输入 → 语音识别 → 字幕断句 → LLM 优化 → 翻译 → 视频合成

## alibaba/MNN（⭐16232，confidence: high）

**面向开发者的端侧深度学习推理与训练框架，支持本地部署 LLM 与扩散模型**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=medium · maturity=research`

MNN 是一个轻量级深度学习框架，支持深度学习模型的推理与训练，已被集成进阿里巴巴 30 多个应用（淘宝、天猫、优酷、钉钉等）及 IoT 嵌入式设备。基于该引擎提供 MNN-LLM 端侧大模型运行时（覆盖手机/PC/IoT）与 MNN-Diffusion 稳定扩散运行时；附带模型转换、压缩、训练、CV 等工具链，支持 Tensorflow/Caffe/ONNX/Torchscript 模型转换与 FP16/Int8 量化，通过 Metal/OpenCL/Vulkan/CUDA 支持 GPU 推理。

- MNN-LLM 支持在手机/PC/IoT 上本地部署大语言模型（含 Qwen、LLAMA 等）
- 支持 Tensorflow/Caffe/ONNX/Torchscript 模型转换（合计数百个 OP）与 FP16/Int8 量化
- 通过 Metal/OpenCL/Vulkan/CUDA 支持 GPU 推理，另含 Hexagon DSP 后端
- 提供 MNN-LLM Android/iOS 多模态应用及 TaoAvatar、Sana 等衍生应用

> L60: MNN is a highly efficient and lightweight deep learning framework. It supports inference and training of deep learning m
> L62: MNN-LLM is a large language model runtime solution developed based on the MNN engine. The mission of this project is to 
> L90: ## Key Features

## wkentaro/labelme（⭐16230，confidence: high）

**给 CV 研究者/开发者的图形化图像标注工具，含 AI 辅助标注**

`ai_role=ai-enhanced · license_risk=viral · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

用 Python 与 Qt 编写的图形图像标注工具，灵感来自 MIT labelme 项目。支持多边形、矩形、圆、线、点等图元标注，覆盖图像分类 flag、视频标注场景，可将标注导出为 VOC 或 COCO 格式数据集，标注结果以 JSON 文件保存。AI 机制方面：内置 SAM/EfficientSAM 做点到多边形/掩码辅助标注，YOLO-world/SAM3 支持文本到标注。安装途径包括 pip、独立可执行文件（付费）与 Linux 发行版包。v7 起不提供稳定 Python API，仅保证 CLI、JSON 格式与配置文件三个公开接口。

- 多图元标注：多边形、矩形、圆、线、点及分类 flag
- AI 辅助标注：SAM/EfficientSAM 点到多边形/掩码，YOLO-world/SAM3 文本到标注
- 导出 VOC/COCO 格式数据集，标注以 JSON 保存
- 支持 20 种语言界面

> L12: Labelme is a graphical image annotation tool inspired by <http://labelme.csail.mit.edu>.\
> L36: - [x] AI-assisted point-to-polygon/mask annotation by SAM, EfficientSAM models
> L91: - **Qt binding:** the GUI moved from PyQt5 (Qt5) to PySide6 (Qt6). `pip install labelme` now pulls PySide6 instead of Py

## ramitsurana/awesome-kubernetes（⭐16122，confidence: mid）

**Kubernetes 学习资源与工具的精选链接清单**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

由 @sindresorhus 的 awesome 系列启发的 Kubernetes 资源精选清单，收录入门概念介绍、历史背景、教程文章、书籍与部署指南等链接。内容提供 Gitbook 电子书形式下载阅读，配有 Links Validator、Python 应用等自动化校验机制；清单接受社区贡献，对不再维护或不合适的条目欢迎提交 pull request 更新。

- 精选 Kubernetes 教程、书籍与部署指南链接
- 提供 Gitbook 电子书形式阅读
- Links Validator 自动校验链接有效性
- 社区贡献机制维护清单内容

> L10: A curated list for awesome kubernetes sources inspired by @sindresorhus' awesome
> L21: **Thanks to Gitbook.This awesome list can now be downloaded and read in the form of a book. Check it out --> https://ram

## tracel-ai/burn（⭐16120，confidence: high）

**给 Rust 开发者的训练+推理统一张量库与深度学习框架**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=—`

Burn 是同时作为张量库与深度学习框架的 Rust 项目，通过统一 API 执行多平台张量运算，使训练代码与生产部署代码一致。基于 CubeCL 的后端覆盖 CUDA、ROCm、Metal、Vulkan、WebGPU 及 CPU，并可通过 autodiff、kernel fusion、remote 执行等装饰器组合；同一应用内可启用多后端并在运行时选择设备。提供训练 TUI 仪表盘、burn-onnx 导入、PyTorch/Safetensors 权重加载及 WebAssembly 浏览器推理。LibTorch 后端在 0.22.0 起废弃并已从 main 移除。

- 单一统一 API 覆盖训练与推理，多平台后端可运行时切换
- JIT 编译张量运算流并自动 kernel fusion
- autodiff、fusion、remote 后端装饰器可组合
- burn-onnx 将 ONNX 模型转成原生 Rust 代码

> L9: **Burn is both a tensor library and a deep learning framework, optimized for numerical
> L17: Burn unifies the two. By executing multi-platform tensor operations via a single, unified API, the
> L50: Burn's CubeCL backends (CUDA, ROCm, Metal, Vulkan, WebGPU,

## alibaba/zvec（⭐16119，confidence: high）

**面向应用开发者的嵌入式向量数据库，提供进程内相似度检索**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

以进程内库形式运行的向量数据库，直接嵌入应用程序，无需独立服务。支持稠密与稀疏向量、多种索引类型（内存到磁盘）、关键词全文检索，并可在单条查询中融合向量相似度、全文与结构化过滤。通过预写日志（WAL）保证持久化，支持多进程并发读。官方提供 Python/Node.js/Go/Rust/Dart SDK，及 zvec-grep 搜索 CLI 与 Zvec Studio 可视化工具。预编译二进制覆盖 Linux/macOS/Windows/Android/iOS。

- 稠密+稀疏向量、多向量查询，索引类型覆盖内存到磁盘
- 混合检索：向量相似度、全文检索与结构化过滤单查询融合
- WAL 持久化与多进程并发读取
- 提供 Python/Node.js/Go/Rust/Dart 官方 SDK

> L22: **Zvec** is an open-source, in-process vector database — lightweight, lightning-fast, and designed to embed directly int
> L28: > - **ReMe integration**: zvec is now a file store backend in ReMe, the memory management kit for agents, providing in-p
> L43: - **Hybrid Search**: Fuse vector similarity, full-text search, and structured filters in a single query for precise resu

## wasp-lang/open-saas（⭐16118，confidence: high）

**面向开发者的开源 JS 全栈 SaaS 起始模板**

`ai_role=ai-enhanced · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

基于 Wasp 框架（React + NodeJS + Prisma）的 SaaS 应用模板，内置邮件+社交登录认证、邮件发送、后台定时任务/队列、落地页、Stripe/Polar.sh/Lemon Squeezy 支付、ShadCN UI、AWS S3 文件上传、文档与博客（Astro Starlight）以及 Plausible/Google Analytics 统计。模板提供针对 Claude Code、Cursor 等 AI 编码工具的插件、Skills 与规则文件，并含 OpenAI API function calling 示例；可通过 CLI 一条命令部署到 Railway 或 Fly.io。安装依赖 npm 全局安装 Wasp CLI。

- 内置认证（Email、Google、GitHub、Slack、MS）、支付、邮件、后台任务、S3 上传等 SaaS 常用模块
- 提供面向 Claude Code/Cursor 等 AI 编码工具的插件、Skills 与规则文件
- 含 OpenAI API function calling 示例
- CLI 一条命令部署到 Railway 或 Fly.io

> L28: - 🐝 Wasp - a full-stack React, NodeJS, Prisma framework with superpowers
> L32: - 🤖 AI-Ready - Custom Plugins, Skills, & Rules for AI-assisted coding with Claude Code, Cursor, or your favorite AI-assi
> L19: 4. ready to work with your favorite AI coding tool or agent (Claude Code, Cursor, Codex, OpenCode, etc.)

## apache/doris（⭐16095，confidence: high）

**面向实时分析与混合搜索场景的 MPP 架构分析型数据库**

`ai_role=ai-enhanced · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=medium · maturity=—`

基于 MPP 架构的开源实时分析与搜索数据库，提供三条核心能力线：支持流式摄入与高并发亚秒查询的实时分析、基于 Iceberg/Delta Lake/Hudi 等开放表格式的湖仓查询加速、以及覆盖 JSON、全文与向量数据的混合搜索。支持存算一体与存算分离两种部署形态，提供 Flink/Spark/Kafka 连接器与 Kubernetes Operator。README 未含安装命令细节，安装与编译指引在官网文档中。

- MPP 架构下的实时分析：流式摄入、增量转换、高并发亚秒查询
- 湖仓分析：对 Iceberg、Delta Lake、Hudi 开放表格式做 SQL 加速
- 混合搜索：同一 SQL 引擎内查询向量、文本、JSON 与结构化数据
- 支持存算耦合与存算分离部署，分离模式下计算组运行于共享对象存储

> L24: Apache Doris is an open-source, real-time analytics and search database built on MPP architecture. It provides fast SQL 
> L35: |Doris for AI|Use vector, text, JSON, and structured search in one SQL engine.|
> L43: |Real-Time Analytics|Streaming ingestion, incremental transformation, and sub-second queries under high concurrency.|
> L65: Apache Doris supports both compute-storage coupled and compute-storage decoupled deployments. In decoupled mode, statele

## vibrantlabsai/ragas（⭐16046，confidence: high）

**为 LLM 应用提供评估指标与测试集生成的工具包**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

Python 工具包，提供 LLM 应用的客观评估指标（含 LLM-based 与传统指标）、自动化测试数据生成与基于生产数据的反馈闭环。通过 pip 从 PyPI 或源码安装，附 ragas quickstart 命令可生成示例工程（rag_eval 评估 RAG 系统，agent_evals 等模板标注 Coming Soon）。与 LangChain 及主流可观测性工具集成，运行示例需设置 OPENAI_API_KEY。另提供咨询服务，并默认收集匿名使用数据（可通过 RAGAS_DO_NOT_TRACK 退出）。

- 提供 LLM-based 与传统两类评估指标
- 自动生成覆盖多场景的测试数据集
- 与 LangChain 及主流可观测性工具集成
- ragas quickstart 提供完整示例工程模板

> L36: Objective metrics, intelligent test generation, and data-driven insights for LLM apps
> L38: Ragas is your ultimate toolkit for evaluating and optimizing Large Language Model (LLM) applications. Say goodbye to tim
> L45: - 🔗 Seamless Integrations: Works flawlessly with popular LLM frameworks like LangChain and major observability tools.

## GLips/Figma-Context-MCP（⭐16002，confidence: high）

**给 AI 编码工具提供 Figma 布局信息的 MCP 服务器**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

一个 Model Context Protocol 服务器，将 Figma 文件的布局与样式元数据提供给 Cursor 等 AI 编码工具。工作流程：在 IDE 聊天中粘贴 Figma 文件/框架/组链接，客户端从 Figma API 获取元数据后，该服务器先对响应做简化与转换，仅保留最相关的布局与样式信息再传给模型，以减少上下文量。使用前需创建 Figma API 访问令牌，通过 MCP 配置文件接入，提供 macOS/Linux 与 Windows 配置示例，也可通过环境变量设置 FIGMA_API_KEY 与 PORT。

- 作为 MCP 服务器向 AI 编码客户端提供 Figma 布局与样式信息
- 对 Figma API 响应做简化与翻译，仅传最相关的布局与样式数据
- 支持通过 MCP 配置文件或 FIGMA_API_KEY/PORT 环境变量配置
- 提供 macOS/Linux 与 Windows 两种配置示例

> L23: Give Cursor and other AI-powered coding tools access to your Figma files with this Model Context Protocol server.
> L42: This MCP server is specifically designed for use with Cursor. Before responding with context from the Figma API, it simp
> L52: > NOTE: You will need to create a Figma access token to use this server. Instructions on how to create a Figma API acces

## GreyDGL/PentestGPT（⭐15992，confidence: high）

**面向渗透测试人员与 CTF 选手的 LLM 自动化测试代理框架**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=research`

由 LLM 驱动的自动化渗透测试代理框架，发表于 USENIX Security 2024。v1.0 采用多阶段流水线（CTF：侦察→利用→通关；渗透：资产发现→漏洞识别→报告），前一阶段结果作为下一阶段输入，代理驱动 Claude Code 或 Codex CLI 运行工具并保存/恢复会话。另保留人机交互的 legacy 模式（pentestgpt-legacy），运行推理/生成/解析三个 LLM 会话并维护 Pentesting Task Tree，通过官方 SDK 原生接入 OpenAI、Anthropic、Gemini、DeepSeek、xAI、Qwen、Moonshot 及本地 Ollama。默认收集匿名遥测数据（上传 Langfuse），可用 --no-telemetry 关闭。

- 多阶段流水线代理，自动驱动 Claude Code 或 Codex CLI 执行工具
- legacy 模式通过官方 SDK 原生支持 8 类提供商及本地 Ollama
- 三个协作 LLM 会话维护 Pentesting Task Tree（PTT）
- Docker 镜像捆绑工具与两个 CLI，登录凭据持久化在卷中

> L38: - **Multi-Stage Pipeline** - The agent works through staged phases (recon → exploit → walkthrough for CTF; asset discove
> L116: pipeline supports Claude and Codex backends; this legacy mode talks **natively** to many providers
> L49: - **AI-Powered Challenge Solver** - Leverages LLM advanced reasoning to perform penetration testing and CTFs

## budtmo/docker-android（⭐15984，confidence: high）

**在 Docker 中运行 Android 模拟器的镜像，供开发测试与 AI-Agent 场景**

`ai_role=ai-ecosystem · license_risk=none · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

提供封装 Android 模拟器的 Docker 镜像，覆盖 9.0–14.0 多个 Android 版本与多种手机/平板设备配置。功能包括：noVNC 网页查看容器内部、日志 Web-UI 共享、adb connect 从容器外控制模拟器、运行 Appium/Espresso 等测试框架构建 Android 项目。含 beta 版 MCP-Server 与 AI-Agent 支持（AI-Agent 属 pro 版），支持对接 Genymotion 云及 Azure/AWS/GCP 部署。要求宿主机为 Ubuntu 并支持虚拟化（KVM），macOS/Windows 需借助虚拟机或 WSL2。

- 多 Android 版本与设备配置的模拟器 Docker 镜像
- noVNC 网页查看与 Web-UI 日志共享
- 支持 adb connect 外部控制与 Appium/Espresso UI 测试
- beta 版 MCP-Server；AI-Agent 支持本地 LLM 服务器 Ollama/VLLM（pro 版）

> L3: Docker-Android is a docker image built to be used for everything related to Android. It can be used for Application deve
> L13: 8. It support (http) MCP-Server (beta-version)
> L14: 9. It support AI-Agent (beta-version) - supported local-LLM server: Ollama, VLLM

## coderamp-labs/gitingest（⭐15941，confidence: high）

**把 Git 仓库转成 LLM 可用文本摘要的开发者工具**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

将任意 Git 仓库 URL 或本地目录转换为面向 LLM 提示词优化的文本摘要，输出文件/目录结构、提取大小与 token 统计（基于 tiktoken 估算）。提供三种使用途径：网页版（改 GitHub URL 中的 hub 为 ingest）、CLI 命令行工具与 Python 包（同步/异步 API，兼容 Jupyter）。默认跳过 .gitignore 文件，私有仓库需 GitHub PAT。支持 Docker/Compose 自托管服务端，可选 MinIO S3 存储、Prometheus 指标与 Sentry 错误跟踪。

- CLI、Python 包（含 sync/async API）与浏览器扩展三种使用方式
- 输出文件结构、提取大小与 token 统计（tiktoken 估算）
- 默认跳过 .gitignore，可用 --include-gitignored 覆盖，支持 STDOUT 管道输出
- Docker Compose 提供 prod/dev 两套 profile，dev 集成 MinIO 对象存储

> L20: Turn any Git repository into a prompt-friendly text ingest for LLMs.
> L37: - **Easy code context**: Get a text digest from a Git repository URL or a directory
> L43: - **CLI tool**: Run it as a shell command
> L44: - **Python package**: Import it in your code

## GeeeekExplorer/nano-vllm（⭐15925，confidence: high）

**面向开发者的轻量级 LLM 离线推理引擎，从零实现 vLLM 接口**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=—`

以约 1,200 行 Python 从零实现的 vLLM 式推理引擎，提供离线批量推理，API 镜像 vLLM 接口（LLM.generate 有细微差异）。内置前缀缓存、张量并行、Torch 编译、CUDA graph 等优化项，README 附 RTX 4070 Laptop 8GB 上 Qwen3-0.6B 的吞吐对比数据。通过 pip 直接从 GitHub 安装，模型权重从 Hugging Face 下载，示例基于 Qwen/Qwen3-0.6B。

- 约 1,200 行 Python 代码的可读实现
- 支持前缀缓存、张量并行、Torch 编译、CUDA graph 等优化
- API 镜像 vLLM 的 LLM/SamplingParams 接口
- 提供 bench.py 基准测试脚本与吞吐数据

> L5: A lightweight vLLM implementation built from scratch.
> L10: * 📖 **Readable codebase** - Clean implementation in ~ 1,200 lines of Python code
> L30: See `example.py` for usage. The API mirrors vLLM's interface with minor differences in the `LLM.generate` method:

## treeverse/dvc（⭐15925，confidence: high）

**给 ML 团队的开源数据与模型版本控制及实验管理工具**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=research`

DVC 是一个命令行工具（配套 VS Code 扩展），通过在 Git 仓库中保存数据/模型的版本元信息，将实际文件存储在 Git 之外的缓存或云存储中，实现 ML 项目的可复现开发。功能覆盖数据与模型版本管理、轻量级 pipeline 定义与增量执行、本地实验跟踪与对比、远程数据共享与协作复现。支持 S3、Azure、Google Cloud、SSH 等远程存储，按存储类型可选安装 dvc-s3、dvc-azure 等附加依赖。以 Apache 2.0 许可分发。

- 数据/模型版本元信息入 Git，文件本体存 Git 外缓存或云存储
- pipeline 计算图只重跑受变更影响的步骤
- 本地实验跟踪，可按超参数和指标过滤、比较并绘图
- VS Code 扩展提供 GUI（实验跟踪与数据管理）

> L20: **Data Version Control** or **DVC** is a command line tool and `VS Code Extension`_ to help you develop reproducible mac
> L72: #. **Git for data**: Store and share data artifacts (like Git-LFS but without a server) and models, connecting them with
> L143: Depending on the remote storage type you plan to use to keep and share your data, you might need to install optional dep

## opensandbox-group/OpenSandbox（⭐15922，confidence: high）

**在自有基础设施上运行 AI agent 的沙箱运行时**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=—`

OpenSandbox 为 AI 应用提供隔离执行环境，支持代码执行、命令运行、文件管理以及浏览器/桌面操作。本地可用 Docker 启动，部署到 Kubernetes 通过统一沙箱 API 管理。提供 Python、Java/Kotlin、TypeScript/JavaScript、C#/.NET、Go 多语言 SDK，附带 `osb` CLI 与 MCP server，支持流量入口网关、出站 egress 策略、凭据保管（Credential Vault），以及 Firecracker 沙箱的暂停/恢复，资源池与批量创建面向 agent 评估与 RL 训练负载。Apache 2.0 开源。

- 多语言 SDK（Python/Java/TS/C#/Go）、CLI 与 MCP 三种接入方式
- Firecracker 沙箱支持暂停/恢复并保留内存与磁盘状态
- 入站统一 ingress 网关与按沙箱出站 egress 策略
- 官方镜像发布于 Docker Hub/ghcr/阿里云三个镜像仓库，Cosign 签名

> L17: **Run AI agents in sandboxes on your own infrastructure.**
> L19: OpenSandbox gives AI applications isolated environments to execute code, run commands, manage files, and operate browser
> L32: |**SDKs, CLI, and MCP**|Integrate with Python, Java/Kotlin, TypeScript/JavaScript, C#/.NET, or Go SDKs. Use `osb` from t

## kubeflow/kubeflow（⭐15913，confidence: mid）

**面向 AI 从业者与管理员的云原生 AI 平台**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Kubeflow 是由模块化开源项目组成的 Kubernetes 原生技术栈，面向 AI 从业者、平台管理员与决策者，支持数据、AI/ML 与 HPC 工作负载。项目由社区工作组维护，覆盖 AI 生命周期各环节，强调可移植（本地/本地机房/云同一套代码）与可扩展（超大规模训练与高吞吐 AI agent）。本仓库主要作为各子项目的入口与共享元数据，开发在子项目仓库进行；README 未给出安装与运行步骤。

- 由模块化开源项目组成，可按需组合跨 AI 生命周期使用
- 同一代码可在本地笔记本、本地机房或任意云上运行
- 社区主导，由多个工作组与委员会维护
- 本仓库作为子项目入口与项目元数据承载

> L7: Kubeflow is _the_ Cloud Native AI platform.
> L9: Kubeflow is composed of modular, open source projects that form the Kubernetes-native stack
> L43: This repository serves primarily as a gateway to Kubeflow subprojects and shared project metadata.

## camenduru/stable-diffusion-webui-colab（⭐15910，confidence: high）

**在 Google Colab 上运行 Stable Diffusion WebUI 的笔记本合集**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

为 Stable Diffusion WebUI 提供的一组 Google Colab 笔记本，提供 lite、stable、nightly 三种分支：stable 含 ControlNet v1.1，nightly 使用 PyTorch 2.0 并每日更新扩展。覆盖 txt2img、img2img、inpainting、DreamBooth 与 LoRA 训练（training 分支）等场景，并收录数十个社区模型的 Open In Colab 一键入口。README 声明该仓库已停止更新，建议转向 TostUI。

- lite/stable/nightly 三种分支可选，stable 含 ControlNet v1.1，nightly 基于 PyTorch 2.0
- 提供数十个社区模型的 Open In Colab 一键运行入口
- 提供 DreamBooth 与 LoRA 训练分支及 Google Drive 安装分支
- 支持 stable-diffusion、waifu-diffusion、inpainting、v2 系列等多种模型

> L5: # WebUI Restrictions Lifted! 🥳 Free WebUI is Back! 🔥 This repository is outdated and no longer receives updates. Please 
> L19: `lite` has a stable WebUI and stable installed extensions.
> L23: ## 🦒 Colab

## modelscope/ms-swift（⭐15870，confidence: high）

**给开发者微调与部署 600+ LLM/400+ MLLM 的训练框架**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=local-ok · hardware=— · install_friction=medium · maturity=research`

ModelScope 社区提供的大模型与多模态大模型微调及部署框架，覆盖预训练、微调、人类对齐训练、推理、评测、量化和部署全流程。集成 Megatron 并行（TP/PP/CP/EP）加速训练，内置 GRPO 系列强化学习算法（GRPO、DAPO、GSPO 等）与 DPO/KTO/SimPO 等偏好学习算法，支持 Embedding/Reranker 训练。通过 vLLM/SGLang/LMDeploy 加速推理，AWQ/GPTQ/BNB/FP8 量化。提供 Web-UI 界面，内置 150+ 数据集，支持自定义数据集一键训练。

- 支持 600+ 纯文本与 400+ 多模态大模型的训练到部署全流程
- 内置 GRPO/DAPO/GSPO 等强化学习算法与 DPO/KTO 等偏好学习算法
- 支持 LoRA/QLoRA/DoRA 等轻量微调与 Megatron/DeepSpeed/FSDP 分布式训练
- 支持量化模型训练，7B 模型仅需 9GB 训练资源

> L23: 🍲 **ms-swift** is a large model and multimodal large model fine-tuning and deployment framework provided by the ModelSco
> L31: - **Hardware Support**: Supports NVIDIA GPUs (A100/H100/RTX series, etc., via CUDA), AMD GPUs (MI300 series, etc., via R
> L90: To install using pip:

## Anionex/banana-slides（⭐15770，confidence: mid）

**基于图像生成模型的 AI PPT 应用，自然语言生成与修改幻灯片**

`ai_role=ai-native · license_risk=dual · deploy=self-host · model_dep=locked-api · hardware=— · install_friction=low · maturity=idea`

前后端分离的 Web 应用（另提供桌面版）：以 nano banana pro / gpt-image 等图像生成模型为核心，从一句话、大纲或页面描述生成整套幻灯片页面，支持上传 PDF/Docx/MD 等文件解析素材、上传模板图片匹配风格、框选区域口头修改，导出 PPTX/PDF 及带 AI 旁白的讲解视频。部署提供 Docker Compose 预构建镜像与源码运行两种途径，依赖各图像/文本模型的 API Key，AGPL-3.0 许可下闭源商业使用需另行授权。

- 想法/大纲/页面描述三种创作路径，支持自然语言修改与局部重绘
- 上传 PDF/Docx/MD/Txt 等文件自动解析为素材，图片自动入库
- 一键导出 PPTX/PDF，含可编辑 PPTX 导出（Beta）与讲解视频（多语言音色、字幕）
- 通过 LazyLLM 注册 11 家在线供应商，支持 gemini/openai/volcengine/vertex 等接口格式

> L3:  基于图像生成模型的原生 AI PPT 应用，
> L96: 但是，nano banana🍌模型的出现让一切有了转机。我尝试使用🍌pro进行ppt页面生成，发现生成的结果无论是质量、美感还是一致性，都做的非常好，且几乎能精确渲染prompt要求的所有文字+遵循参考图的风格。那为什么不基于🍌pro，做一
> L122: 支持**想法**、**大纲**、**页面描述**三种起步方式，满足不同创作习惯。

## google-deepmind/mujoco（⭐15730，confidence: high）

**面向机器人与仿真研究的通用多关节接触动力学物理引擎**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=—`

MuJoCo（Multi-Joint dynamics with Contact）是一个通用物理引擎，服务于机器人、生物力学、图形动画、机器学习等需要对铰接结构与环境交互进行快速精确仿真的领域。提供 C API，运行时仿真模块基于内置 XML 编译器预分配的底层数据结构运作，含 OpenGL 原生交互可视化 GUI 与物理量计算工具函数。提供 Python 绑定与 Unity 插件，版本化发布每月一次，由 Google DeepMind 维护。

- 提供 C API 与官方 Python 绑定（pip install mujoco）
- 含 OpenGL 原生交互式可视化查看器 simulate
- MJX 分支基于 JAX 编写，支持可微物理教程
- 提供 Unity 插件及 JS/C#/MATLAB 等第三方绑定

> L13: **MuJoCo** stands for **Mu**lti-**Jo**int dynamics with **Co**ntact. It is a
> L19: This repository is maintained by Google DeepMind.
> L21: MuJoCo has a C API and is intended for researchers and developers. The runtime

## Unstructured-IO/unstructured（⭐15571，confidence: high）

**面向 LLM 开发者的文档解析 ETL 库：把文档转为结构化数据**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

提供开源组件用于摄取和预处理图像与文本文档（PDF、HTML、Word 等），核心是 partition 函数，自动检测文件类型并路由到对应的分区函数，输出结构化元素。安装方式包括 PyPI 安装（按文档类型选择 extras）、Docker 容器运行及本地开发（uv 管理依赖）。README 注明开源库永久免费，但官方推荐更高精度的 Transform v2 API（商业产品），并默认发送轻量遥测，可通过环境变量关闭。

- partition 函数自动检测文件类型并路由到对应分区函数
- 按文档类型提供 pip extras 安装（如 unstructured[docx,pptx]）
- 提供多平台 Docker 镜像（x86_64 与 Apple silicon）
- 默认遥测可通过 DO_NOT_TRACK 或 SCARF_NO_ANALYTICS 关闭

> L29: The `unstructured` library provides open-source components for ingesting and pre-processing images and text documents, s
> L100: - Install the Python SDK to support all document types with `pip install "unstructured[all-docs]"`
> L238: Unstructured sends lightweight analytics to `GET https://packages.unstructured.io/python-telemetry` by default: one libr

## ggml-org/ggml（⭐15494，confidence: high）

**面向机器学习的 C/C++ 张量计算库**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=medium · maturity=—`

以纯 C/C++ 实现的机器学习张量库，目标是简单、可移植、高效且安装配置最少。无任何外部依赖，支持 x86、ARM、RISC-V、LoongArch、PowerPC、s390x 与 WebAssembly 多平台，为 x86/ARM/RISC-V 提供 SIMD 优化内核；后端覆盖 CPU、GPU、NPU 与浏览器，支持 2-8 位整数量化及 MXFP4/NVFP4 微缩格式，运行期零内存分配。通过 CMake 从源码构建，MIT 协议。

- 纯 C/C++ 实现，无外部依赖
- 跨平台支持 x86、ARM、RISC-V 等 7 类架构与 WebAssembly
- 后端覆盖 CPU、GPU、NPU 与浏览器
- 支持 2-8 位整数量化与 MXFP4/NVFP4 格式

> L28: The main goal of `ggml` is to be a simple, portable, and efficient tensor library for machine learning with minimal setu
> L33: - Broad backend support - CPU, GPU, NPU, and browser

## cmusatyalab/openface（⭐15441，confidence: high）

**基于深度神经网络的开源人脸识别库（CMU）**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Carnegie Mellon University 发布的开源人脸识别研究项目，以深度神经网络生成人脸表示。仓库提供批量图像表示生成（batch-represent）、双图对比、分类器训练与使用、摄像头实时分类等 demo，附带 LFW 精度评估脚本、Python 库代码、模型训练脚本与测试。安装与使用讨论通过 gitter/mailing list 支持；源码与训练模型默认采用 Apache 2.0 许可，包含多个修改过的第三方组件。

- 提供 Python 库及批量表示生成、对比、分类器训练等脚本
- 包含 LFW 精度评估脚本与网络输出可视化 demo
- 支持 webcam 实时分类器与实时 web demo
- 附训练新模型脚本与含神经网络训练的测试

> L3: *Free and open source face recognition with
> L33: + openface: Python library code.
> L54: model files are copyright Carnegie Mellon University and licensed

## yc-software/qm（⭐15437，confidence: high）

**企业级多人共享 agent 运行框架，部署在自有云上，Slack 与网页使用**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

QM 是面向初创公司的多人 agent 运行框架：每位员工获得隔离工作区（独立记忆、文件、密钥视图、权限、定时任务、沙箱），同时可在 Slack 频道、群消息和项目中协作使用。核心以 TypeScript 运行在 Node 上，用 Postgres 持久化会话与状态，agent 通过固定工具面中的 execute 在持久沙箱执行命令。harness、模型、会话存储、沙箱、记忆均藏在接口之后可替换，部署配置集中在部署目录，由 qm CLI 校验并部署到运营者自己的云账户。提供 Strict/Auto/Dangerous 三档安全姿态与内容筛查、审计。

- 个人与共享双作用域：每人和每个房间有独立的记忆、文件、权限与沙箱
- harness 与模型可插拔，Pi 和 Claude Code 驱动同一核心
- Strict/Auto/Dangerous 三档工具调用审批姿态与内容筛查、审计日志
- 支持定时任务、监听与入站 webhook 等后台工作

> L3: **A multiplayer agent harness for work. In Slack and on the web.**
> L74: Every turn runs through a central core, which can use a variety of models and harnesses
> L89: `qm` CLI validates and deploys. Every substrate (harness, session

## DataTalksClub/mlops-zoomcamp（⭐15425，confidence: high）

**面向数据从业者的 9 周免费 MLOps 课程**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

DataTalks.Club 出品的免费 9 周 MLOps 课程，内容覆盖实验跟踪（MLflow）、工作流编排、模型部署（Flask、AWS Kinesis/Lambda）、监控（Evidently、Grafana、Prometheus）及 CI/CD、Terraform 等最佳实践，以模块化课程、作业与期末项目组成。提供直播批次与自学两种形式，2026 年暂无直播批次，材料全部开放自学。面向有 Python、Docker 与一年以上编程经验的数据科学家、ML 工程师和软件工程师。

- 9 个模块覆盖从实验跟踪到监控的 MLOps 全流程
- 完成期末项目与互评可获得结业证书
- 课程视频、材料、作业全部免费开放
- Slack 社区支持提问与学习打卡

> L28: MLOps (machine learning operations) is a must-know skill for many data professionals. This free 9-week course teaches th
> L32: This course is for data scientists, ML engineers, and software engineers who want to learn how to put machine learning m

## electerm/electerm（⭐15378，confidence: high）

**跨平台终端/SSH/SFTP/RDP/VNC 客户端，带 AI 助手**

`ai_role=ai-enhanced · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=—`

基于 Electron 的终端与远程连接客户端，支持 ssh/sftp/ftp/telnet/serialport/RDP/VNC/Spice 协议，覆盖 Linux/Mac/Windows/Android/HarmonyOS/iOS，兼容 UOS、Kylin、LoongArch、RISC-V 等系统。提供书签同步、隧道/跳板、Zmodem/Trzsz、代理、多语言等终端功能。AI 部分集成多 LLM API 格式（OpenAI Chat Completions/Responses、Anthropic Messages），提供命令建议、脚本编写、选中内容解释，以及 agent 模式直接执行终端操作，另有 MCP widget 供外部工具接入。

- AI 助手支持 OpenAI Chat Completions、OpenAI Responses、Anthropic Messages 三种 API 格式
- agent 模式可代为执行终端操作，支持创建书签/主题
- MCP widget 供 AI 助手与外部工具集成
- 支持 ssh 隧道、跳板连接、Zmodem/Trzsz、全局/会话代理

> L12: Open-sourced terminal/ssh/sftp/telnet/serialport/RDP/VNC/Spice/ftp client(Linux, Mac, Windows, Android, HarmonyOS, iOS).
> L50: - AI assistant integration (supporting multiple LLM API formats — OpenAI Chat Completions, OpenAI Responses, and Anthrop
> L51: - MCP (Model Context Protocol) widget for AI assistants and external tools integration - see MCP Widget Usage Guide

## theonedev/onedev（⭐15316，confidence: high）

**自托管 DevOps 平台：代码托管+CI/CD+_issue 管理+AI 助手**

`ai_role=ai-enhanced · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

自托管的统一开发平台，覆盖代码搜索与导航、pull request 与代码保护规则、issue 工作流与看板、服务台邮件联动、CI/CD 编辑器与多种执行器（容器/Kubernetes/agent）、内置包仓库、版本化 Wiki、仪表盘与高可用集群。AI 部分：内置自然语言查询、代码解释、提交与 PR 审查、构建错误排查；AI 用户可在 issue/PR 流程中自主实现任务、修复失败；Workspaces 在浏览器中提供预配置 dev container 以运行终端编码 agent。README 注明服务器最低可在 1 核 2G 内存环境运行中型项目。

- 内置 AI：自然语言查询、代码解释、PR 审查、CI/CD 规格辅助与构建错误调查
- AI 用户在 issue/PR 流程中自主实现 issue、修复 CI 失败与合并冲突
- Workspaces 提供服务端预配置 dev container，浏览器内使用终端编码 agent
- TOD CLI 与内置 skills 供编码 agent 查询/编辑 issue、PR、build 并触发 CI

> L156: ## 🤖 Built-in AI for DevOps Intelligence
> L165: Work on any branch with preconfigured dev containers on server. Use OpenCode, Claude Code, Codex, or other terminal agen
> L179: AI users work autonomously in your issue and pull request flow: implement assigned issues, review and improve pull reque

## n8n-io/self-hosted-ai-starter-kit（⭐15296，confidence: high）

**自托管本地 AI 工作流入门模板：一条 Docker Compose 拉起整套环境**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

由 n8n 官方维护的 Docker Compose 模板，组合四个组件：n8n 低代码平台（400+ 集成与 AI 节点）、Ollama 本地 LLM 运行时、Qdrant 向量库、PostgreSQL。按 GPU 型号（Nvidia/AMD/Apple Silicon/CPU）提供不同 compose profile，一条命令启动；预配置网络与存储，含示例工作流与本地文件共享目录挂载。README 说明面向原型验证，非生产环境优化。

- 一条 docker compose 命令启动 n8n + Ollama + Qdrant + PostgreSQL 组合
- 按 Nvidia GPU / AMD GPU / Mac / CPU 提供不同启动 profile
- 内置示例工作流与 400+ 集成的 n8n 平台
- 本地文件共享目录挂载至 n8n 容器 /data/shared

> L3: **Self-hosted AI Starter Kit** is an open-source Docker Compose template designed to swiftly initialize a comprehensive 
> L7: Curated by <https://github.com/n8n-io>, it combines the self-hosted n8n
> L115: The core of the Self-hosted AI Starter Kit is a Docker Compose file, pre-configured with network and storage settings, m

## GaiZhenbiao/ChuanhuChatGPT（⭐15267，confidence: high）

**为多种 LLM 提供带附加功能的 Web 聊天界面**

`ai_role=ai-ecosystem · license_risk=viral · deploy=library · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

基于 Gradio 的 Web 图形界面，为 ChatGPT 等多种 LLM 提供对话入口。支持 API 调用模型（ChatGPT、Azure OpenAI、Gemini、Claude、DeepSeek 等）与本地部署模型（ChatGLM、LLaMA、Qwen 等），并提供川虎助理（类 AutoGPT 全自动代理）、在线搜索、基于文件问答的知识库、GPT-3.5 微调、Prompt 模板、对话历史管理与多 api-key 负载均衡等功能。通过 git clone 加 pip 安装依赖后以 Python 启动，可部署到服务器或 Hugging Face Space，也支持作为 PWA 安装。

- 接入多种 API 模型与本地部署模型（含 Lora 支持）
- 川虎助理、在线搜索、文件问答知识库、GPT-3.5 微调
- 支持 PWA 安装与移动端适配，多用户历史记录隔离
- 支持自定义 api-host、代理与多 api-key 负载均衡

> L9:  为ChatGPT等多种LLM提供了一个轻快好用的Web图形界面和众多附加功能
> L57: |API 调用模型|备注|本地部署模型|备注|
> L125: git clone https://github.com/GaiZhenbiao/ChuanhuChatGPT.git

## wdndev/llm_interview_note（⭐15254，confidence: high）

**大模型算法工程师的知识整理与面试题笔记**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

以个人笔记形式整理大语言模型相关知识及面试题，内容参考网络资源汇编，答案为作者自行撰写并欢迎修正，提供在线阅读链接，另附微信公众号作为更新渠道。仓库同时推荐作者的其他动手实践项目（tiny-llm-zh、tiny-rag、tiny-mcp、llama3-from-scratch-zh）及 AI 工程师八股等学习资源。适合准备大模型方向岗位面试的读者阅读。

- 覆盖 LLM 算法（应用）工程师相关知识及面试题
- 提供在线阅读链接
- 附带 tiny-llm-zh、tiny-rag、tiny-mcp 等配套实践项目
- llama3-from-scratch-zh 可在 16G 内存本地笔记本运行

> L1: # LLMs 相关知识及面试题
> L5: 本仓库为大模型面试相关概念，由本人参考网络资源整理，欢迎阅读，如果对你有用，麻烦点一下 `🌟 star`，谢谢！
> L21: 在线阅读链接：LLMs Interview Note

## google-deepmind/deepmind-research（⭐15236，confidence: high）

**为科研人员提供 DeepMind 论文的配套开源代码与环境**

`ai_role=ai-knowledge · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=research`

DeepMind 官方研究仓库，收录其发表论文的实现与示例代码，并开放研究环境、数据集和代码，供更广泛的研究社区在其工作基础上开展研究。仓库以目录形式组织约 60 个论文项目，覆盖强化学习、图网络、生成模型、语言模型、因果推理、蛋白质结构预测（AlphaFold CASP13）等方向。README 未提供统一安装说明，各项目需进入对应目录查看；页面声明这不是 Google 官方产品。

- 收录约 60 个 DeepMind 论文的实现与示例代码
- 开放 DeepMind Lab、StarCraft II 等研究环境与数据集
- 覆盖强化学习、图网络、生成模型、AlphaFold 等多方向

> L3: This repository contains implementations and illustrative code to accompany
> L9: enable the broader research community to engage with our work and build upon it,
> L25: ## Projects

## ty4z2008/Qix（⭐15224，confidence: mid）

**机器学习/分布式系统/Go/PostgreSQL 学习资源合集**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

个人维护的学习资源仓库，按主题分章节组织：机器学习与深度学习资料、Golang 学习资源、PostgreSQL 数据库资源、分布式系统资源及数据库系统资源。另包含译者对 node-mysql 官方文档的中文翻译。作者声明文章可能存在不准确信息，欢迎通过邮件或 PR 反馈纠错；同时提醒使用者尊重原作署名，发现署名错误时提交反馈。仓库采用 MIT 许可证。

- 按章节组织机器学习/深度学习、Golang、PostgreSQL、分布式系统等主题资源
- 包含 node-mysql 官方文档中文翻译
- 开放 PR 协作与纠错反馈机制
- MIT 许可证

> L27: ## Machine Learning And deep learning Resources
> L33: ## Golang learning resources
> L41: ## Distributed system resources

## alphacep/vosk-api（⭐15177，confidence: high）

**离线语音识别工具包：面向 20+ 语言的开发者 API**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Vosk 是一个离线开源语音识别工具包，支持 20 多种语言和方言的语音识别。模型体积小（50 MB），提供连续大词汇量转写、流式 API 零延迟响应、可重配置词汇表与说话人识别。为 Python、Java、Node.js、C#、C++、Rust、Go 等语言提供绑定，可从树莓派、Android 手机扩展到大型集群，安装文档位于官网。

- 支持 20+ 语言的离线语音识别
- 小体积模型（50 MB）支持流式 API 与说话人识别
- 多语言绑定：Python、Java、Node.js、C#、C++、Rust、Go
- 可运行于树莓派/Android 至大型集群

> L3: Vosk is an offline open source speech recognition toolkit. It enables
> L14: Speech recognition bindings implemented for various programming languages
> L21: Vosk scales from small devices like Raspberry Pi or Android smartphone to

## Tencent-Hunyuan/Hunyuan3D-2（⭐15142，confidence: high）

**给创作者/开发者的图像与文本生成高分辨率带纹理 3D 资产的扩散模型系统**

`ai_role=ai-native · license_risk=none · deploy=library · model_dep=— · hardware=gpu-8g · install_friction=low · maturity=—`

腾讯混元发布的 Hunyuan3D 2.0 开源 3D 生成系统，采用两阶段管线：基于流扩散 transformer 的形状生成模型 Hunyuan3D-DiT 依据条件图像生成网格，纹理合成模型 Hunyuan3D-Paint 为生成或手工网格生成纹理贴图。提供多系列模型（1.1B 标准、0.6B mini、多视图 mv、蒸馏加速 Turbo/Fast 版本），支持 macOS/Windows/Linux，输出 glb/obj 格式。提供 Python API、Gradio App、本地 API Server 与 Blender 插件；形状生成需 6 GB 显存，形状+纹理共需 16 GB。

- 两阶段管线：形状生成（Hunyuan3D-DiT）+ 纹理合成（Hunyuan3D-Paint）
- 提供 mini/mv/turbo 等多系列模型，0.6B 起可选
- 提供 Python API、Gradio App、API Server 与 Blender 插件四种使用方式
- 形状生成 6 GB 显存即可运行

> L42: We present Hunyuan3D 2.0, an advanced large-scale 3D synthesis system for generating high-resolution textured 3D assets.
> L60: Hunyuan3D 2.0 features a two-stage generation pipeline, starting with the creation of a bare mesh, followed by the
> L120: Hunyuan3D 2.0 supports Macos, Windows, Linux. You may follow the next steps to use Hunyuan3D 2.0 via:

## corsairdev/corsair（⭐15100，confidence: mid）

**为开发者提供统一的第三方应用集成平台，供 agent 与应用调用**

`ai_role=ai-ecosystem · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Corsair 是一个产品集成平台，基于 REST API 构建，为第三方 API 集成提供统一语法并由官方维护适配器。同一集成层可同时服务 agent、后端服务与多租户用户仪表盘。支持自托管，也可使用 Hub 由官方托管 OAuth 刷新与 webhook。以 npm 包发布，采用 Apache 2.0 许可证。README 未给出具体安装命令与支持的服务列表。

- 基于 REST API 的集成层，兼容 agent、后端服务与用户仪表盘
- 所有集成统一语法，适配器由项目维护
- 支持自托管，Hub 托管模式提供 OAuth 刷新与 webhook
- 开源（Apache 2.0），npm 发布

> L9: Corsair is a fully-featured product integration platform with a seamless DX. Build anything, from an agent working acros
> L17: Most agent integration tools are MCP-only. Corsair is built on a REST API, so the same integration layer works for agent

## openai/math（⭐15087，confidence: high）

**面向数学研究者的 OpenAI 模型生成数学论文集与证明工件**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

该仓库收录由 OpenAI 内部模型产出的数学稿件及配套证明材料，共 719 篇手稿、组织为 372 个结果族，按数学学科分类。提供概览、手稿地图、preprints 目录（含 PDF、源文件与构建说明）、Lean 形式化目录与 Comparator 校验说明，约 42% 顶级结果已形式化；部分结果尚无 Lean 形式化且可能存在问题。每篇手稿目录内含 BibTeX 引用块，版本修订以新版本形式保留。

- 719 篇手稿按 372 个结果族组织，按数学学科分类
- 约 42% 顶级结果附带 Lean 形式化证明
- 提供手稿推理摘要与 preprints 源文件及构建说明
- 版本历史保留，修订以新版本发布

> L3: This repository contains mathematical manuscripts and supporting proof artifacts produced by an internal OpenAI model.
> L14: The current catalogue contains 719 manuscripts organized into 372 families. A family groups related papers, which may in
> L19: - The Lean library and formalization catalogue describe the available formal proofs, their associated papers, and verifi

## CoplayDev/unity-mcp（⭐15048，confidence: high）

**给 Unity 开发者的 MCP 桥：让 AI 助手控制编辑器**

`ai_role=ai-ecosystem · license_risk=dual · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

通过 Model Context Protocol 将 AI 助手（Claude、Cursor、VS Code、本地 LLM 等）接入 Unity Editor，提供 50 个 MCP 工具入口，支持自然语言创建场景与 GameObject、编辑 C# 脚本、管理资产、运行测试、性能分析与构建。要求 Unity 2021.3 LTS 至 6.x 及 Python 3.10+（经 uv）。安装方式为 Unity Package Manager 的 git URL 或 openupm，可在多个客户端自动配置，MIT 许可，另支持多实例路由、工具分组、远程服务器鉴权等。

- 50 个 MCP 工具入口，任意 MCP 客户端可用
- 自然语言控制 Unity Editor：场景、脚本、资产、测试、构建
- 支持多 Unity 实例路由与按领域分组的工具组
- 提供远程托管服务器与鉴权选项

> L8:  Create your Unity apps with LLMs. MCP for Unity bridges AI assistants — Claude, Codex, VS Code, local LLMs, and more — 
> L24: Control the Unity Editor in natural language from any MCP client — create scenes & GameObjects, edit C# scripts, manage 
> L30: **Requirements:** Unity **2021.3 LTS → 6.x** · Python **3.10+** (via `uv`). Works with **any MCP client** — Claude Deskt

## NanmiCoder/cc-haha（⭐15046，confidence: high）

**给 Claude Code 用户的跨平台桌面工作台：多 Agent 协作与可视化管理**

`ai_role=ai-native · license_risk=dual · deploy=— · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

基于 Electron 的桌面应用，将 Claude Code CLI 包装为图形化工作台：多会话管理、分支/Worktree 启动、Diff 审阅、内置浏览器预览、MCP 与 SubAgent 可视化管理、Agent Teams 协作、动态 Workflow 编排、Computer Use、技能市场、桌面宠物，以及 H5 与 IM 远程接入。模型侧支持官方账号登录、第三方 API 预设与本地模型端点。需在设置中配置模型提供商与 API Key；许可证为源码可用许可，非 OSI 认证，商业使用须书面授权。

- 多会话工作台：Worktree 启动、Diff 审阅、Cmd+K 全局搜索
- Agent Teams 多 Agent 协作与动态 Workflow 编排
- Computer Use 跨应用操作，macOS 上不占用真实鼠标键盘
- MCP 图形化管理与技能市场（ClawHub / SkillHub）

> L16: cc-haha 是一个**桌面端 Claude Code 工作台**：多会话与全局搜索、分支 / Worktree 启动、Diff 审阅、内置浏览器预览、图形化权限审批、模型自选（Claude / ChatGPT / Grok / 预设 /
> L109: - **模型自选**：Claude / ChatGPT / Grok 官方账号可直接登录；DeepSeek、Kimi、智谱 GLM 等第三方 API 有现成预设；LM Studio、Ollama 的本地模型也接得上。
> L162: 当前采用 cc-haha Community Source License 1.0。允许个人非商业使用及企业内部自用；接单、对外商业盈利、收费修改或二次开发、商业分发及付费服务须事先取得书面商业授权；二次分发须显著保留来源署名。历史 MIT

## T8RIN/ImageToolbox（⭐15046，confidence: high）

**Android 用户的开源高级图像编辑工具，覆盖裁剪到 OCR 多种处理**

`ai_role=ai-enhanced · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

基于 Kotlin 与 Jetpack Compose 构建的 Android 图像编辑应用，提供裁剪、滤镜、EXIF 编辑、背景擦除、OCR 与批量处理等功能，支持 500 多种滤镜的链式叠加。分发上提供 FOSS 与 Market 两个版本：FOSS 版使用 ONNX、OpenCV、Zxing 等开源实现且不含 Google 依赖与分析组件，Market 版改用 MlKit 并包含分析组件。安装途径包括 GitHub Releases、Google Play、F-Droid 与 Obtainium 的 APK，也可克隆仓库用 Gradle 构建。

- 500+ 滤镜链式叠加处理与批量处理
- 自动背景移除：FOSS 版用 ONNX，Market 版用 MlKit
- EXIF 数据编辑与 OCR
- FOSS 版不含 Google 依赖与分析组件，含 OpenCV 文档扫描

> L42: ImageToolbox is a versatile image editing tool designed for efficient photo manipulation. It allows
> L43: users to crop, apply filters, edit EXIF data, erase backgrounds, and even enhance images with AI.
> L89: # ⚔️ FOSS vs MARKET

## ConardLi/easy-dataset（⭐15011，confidence: high）

**为开发者从领域文档生成微调/RAG/评测数据集**

`ai_role=ai-native · license_risk=none · deploy=desktop · model_dep=local-ok · hardware=— · install_friction=low · maturity=research`

面向构建 LLM 数据集的应用：内置文档解析（PDF/Markdown/DOCX/TXT/EPUB）、多种文本切分算法、问题与答案（含 COT）自动生成、数据清洗与领域标签树管理；支持单轮 QA、多轮对话、图像 QA、数据蒸馏等数据集类型，并含自动评测（Judge Model）、人工盲测（Arena）体系。导出 Alpaca/ShareGPT 等格式，一键生成 LLaMA Factory 配置，可上传 Hugging Face Hub。提供 Windows/macOS/Linux 桌面客户端、NPM 与 Docker 运行方式。

- 文档转多类型数据集：单轮 QA、多轮对话、图像 QA、数据蒸馏
- 自动评测体系：Judge Model 评分与双盲人工 Arena 盲测
- 导出 Alpaca/ShareGPT/Multilingual-Thinking 格式并集成 LLaMA Factory
- 兼容所有 OpenAI 格式 API，支持 Ollama 本地模型

> L23: Easy Dataset is an application specifically designed for building large language model (LLM) datasets. It features an in
> L71: - **Wide Model Compatibility**: Compatible with all LLM APIs that follow the OpenAI format

## Usagi-org/ai-goofish-monitor（⭐14967，confidence: mid）

**面向闲鱼用户的商品实时监控与 AI 智能分析系统**

`ai_role=ai-enhanced · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

基于 Playwright 的闲鱼多任务监控系统，提供 Web 管理界面，覆盖任务管理、账号登录态管理、AI 标准编辑、运行日志与结果浏览。支持自然语言创建任务（后台异步生成分析标准）与关键词规则两种模式，多模态模型分析商品图片，结果持久化到 SQLite。支持 Cron 定时调度、多账号与代理池轮换、ntfy/企业微信/Bark/Telegram/Webhook 通知，Docker 一键部署。通过 Chrome 扩展导出闲鱼登录态，作者提示需遵守平台协议、避免账号被限制。

- 自然语言创建监控任务，AI 模式后台 job 异步生成分析标准
- 多模态模型深度分析商品，需支持图片输入的模型
- 多账号管理与代理池轮换、失败重试与任务暂停保护
- SQLite 主存储，自动从旧 config.json/jsonl/price_history 导入历史数据

> L5: 基于 Playwright 和 AI 的闲鱼多任务实时监控，提供完整的 Web 管理界面。
> L10: - **AI 驱动**: 自然语言创建任务，多模态模型深度分析商品
> L11: - **多任务并发**: 独立配置关键词、价格、筛选条件和 AI Prompt

## jujumilk3/leaked-system-prompts（⭐14964，confidence: high）

**收录主流 LLM 服务泄露系统提示词的文档集合**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

以文档形式收集被泄露的、来自广泛使用的基于 LLM 的服务的系统提示词。收录流程要求提交的 PR 与现有文档格式一致，并附可验证来源或可复现的提示词；不便走 PR 流程时可在 Issues 区贴链接，由维护者核实后合并。README 说明该仓库被多篇论文引用，并要求提交者不包含敏感商业源代码，以避免 DMCA 下架风险。除收录与提交规范外，README 未描述其他工具或功能。

- 收集来自广泛使用的 LLM 服务的泄露系统提示词
- 收录需附可验证来源或可复现提示词
- 通过 Issues 贴链接的替代投稿通道
- 声明被多篇论文引用并规定 DMCA 风险规避规范

> L5: This repository is a collection of leaked system prompts from widely used LLM based services.
> L7: 1. If you would like to submit a PR, please match the format of other documents. You must include sources that I can ver

## microsoft/RD-Agent（⭐14960，confidence: mid）

**微软自动化研发流程的 Agent：自动化模型与数据研发迭代**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=locked-api · hardware=— · install_friction=low · maturity=research`

微软开源的研发自动化框架，将 R&D 过程拆解为提出想法（R）与实现（D）两类组件，应用于量化交易因子/模型演化、数据挖掘、论文/财报读取并实现模型、Kaggle 竞赛特征工程、LLM 微调等场景。后端默认通过 LiteLLM 接入多家模型提供商，仅支持 Linux，多数场景依赖 Docker，通过 PyPI 安装或源码开发安装，提供 `rdagent health_check` 健康检查与 Web UI。

- R（提出想法）+D（实现）双组件框架，覆盖量化、数据科学、医疗等多个场景命令
- 默认 LiteLLM 后端接入多家 LLM 提供商，提供 OpenAI/Azure OpenAI/DeepSeek 配置示例
- 在 MLE-bench（75 个 Kaggle 竞赛数据集）上提交运行结果并公开详细 runs
- 提供 `rdagent server_ui` Web 前端用于实时交互与 trace 查看

> L97: R&D-Agent aims to automate the most critical and valuable aspects of the industrial R&D process, and we begin with focus
> L98: Methodologically, we have identified a framework with two key components: 'R' for proposing new ideas and 'D' for implem
> L119: ### RD-Agent currently only supports Linux.

## botpress/botpress（⭐14956，confidence: high）

**面向开发者的开源聊天机器人/Agent 构建与部署平台**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

Botpress Cloud 的主仓库，包含 Botpress Hub 的公开集成、开发者工具（CLI、SDK、API Client）以及仅用 SDK 和 CLI 编写的 "as code" 机器人示例。开发者可通过 npm/yarn/pnpm 安装 @botpress/cli，用 bp init 从模板生成集成，修改 integration.definition.ts 与 src/index.ts 后用 bp deploy 部署到工作区，并可设为公开分享到 Hub。所有包以 MIT 许可开源。README 明确说明 bots-as-code 不是官方推荐方式，Studio 才是主要构建途径。

- 提供 @botpress/cli、@botpress/client、@botpress/sdk 三类开发者工具包
- bp init 从模板生成集成，bp deploy 部署并支持公开可见性
- 包含 Botpress Hub 全部公开集成与 as-code 机器人示例
- 全部包以 MIT 许可开源

> L9: Botpress is the ultimate platform for building **next-generation chatbots** and assistants powered by OpenAI. Start buil
> L21: - **Integrations** – all public integrations on the Botpress Hub maintained by Botpress
> L22: - **Devtools** – all Botpress Cloud dev tools (CLI, SDK, API Client)

## optuna/optuna（⭐14931，confidence: high）

**面向机器学习的超参数自动优化 Python 框架**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=research`

为机器学习提供超参数优化的 Python 框架，采用 define-by-run 命令式 API，用户可用普通 Python 语法（含条件与循环）动态构建搜索空间。核心机制包括采样与剪枝算法、study/trial 抽象、以少量代码改动扩展到数十至数百 worker 的并行化，以及优化历史绘图。另提供 Rust 实现的实验性版本 Rustuna、Web 仪表盘 optuna-dashboard 与特性共享平台 OptunaHub。要求 Python 3.10 及以上，MIT 许可。

- define-by-run API 动态构建搜索空间
- 并行化扩展至数十至数百 worker
- Rustuna：Rust 实现，支持 TPE/MOTPE/NSGA-II/CMA-ES 采样器
- Optuna Dashboard 实时查看优化历史与超参数重要性

> L18: *Optuna* is an automatic hyperparameter optimization software framework, particularly designed
> L38: - Lightweight, versatile, and platform agnostic architecture
> L79: Optuna is available at the Python Package Index and on Anaconda Cloud.

## kyegomez/OpenMythos（⭐14912，confidence: high）

**对 Claude Mythos 架构的理论性开源重建：循环深度 Transformer 实现**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=—`

以 PyPI 包形式发布的理论性模型实现：按公开研究与猜测重建被称为 Claude Mythos 的架构，实现三段式 Recurrent-Depth Transformer（Prelude / 循环 Recurrent Block / Coda），注意力可在 MLA 与 GQA 间切换，前馈层为带路由与共享专家的稀疏 MoE。提供 1B 到 1T 参数的预配置变体、基于 FineWeb-Edu 的 3B 训练脚本（单卡与 torchrun 多卡）、API 文档，并附架构假设、稳定性约束与循环模型缩放律的说明。README 明确声明与 Anthropic 无关联。

- 三段式 RDT 实现：Prelude、可循环 Recurrent Block（至多 max_loop_iters）、Coda
- 注意力可在 GQA（可选 Flash Attention 2）与 MLA（DeepSeek-V2 式压缩 KV 缓存）间切换
- 提供 1B–1T 参数的预配置变体与 3B FineWeb-Edu 训练脚本
- 通过参数化约束注入矩阵 A 使谱半径 ρ(A)<1，保证训练稳定性

> L24: > **Disclaimer:** OpenMythos is an independent, community-driven theoretical reconstruction based solely on publicly ava
> L26: OpenMythos is an open-source, theoretical implementation of the Claude Mythos model. It implements a Recurrent-Depth Tra
> L28: ## Installation

## xcanwin/KeepChatGPT（⭐14900，confidence: high）

**为 ChatGPT 用户提供保持活跃、数据脱敏等增强功能的浏览器插件**

`ai_role=ai-ecosystem · license_risk=viral · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

以 UserScript（Tampermonkey 脚本）形式分发的 ChatGPT 网页增强插件，通过 Tampermonkey 安装，支持电脑系统与移动系统（鸿蒙、iOS、Android）。功能包括定时保活请求以减少网络报错、敏感信息脱敏（按用户自定义正则规则）、拦截跟踪请求、克隆对话、取消审计提示、净化页面、展示大屏、言无不尽、侧边栏增强等。提供 npm 依赖安装与开发调试流程；README 提示谷歌/微软应用商店存在非作者上传的付费版本。

- 定时保活请求，缓解 NetworkError 等网络报错与页面刷新
- 数据安全功能：按正则规则对输入内容自动脱敏并风险提示
- 拦截跟踪请求，减少页面追踪类网络请求
- 克隆对话、言无不尽、净化页面、展示大屏等界面与交互增强

> L16: - 这是一款提高```ChatGPT```的数据安全能力和效率的插件。它可以让你的聊天无比丝滑，省去足足几十数百个多余步骤，一劳永逸摆脱各种```报错```和```警告```。并且免费共享大量创新功能，如：自动刷新、保持活跃、数据安全、取消
> L84: 1. 安装```Tampermonkey```，通过 官网；
> L42: 13. 支持移动系统 (鸿蒙、iOS、Android)

## google-deepmind/alphafold（⭐14895，confidence: mid）

**为科研人员提供蛋白质结构预测 AlphaFold2 推理代码**

`ai_role=ai-enhanced · license_risk=dual · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

DeepMind 开源的 AlphaFold v2 推理流水线实现，读取 FASTA 格式的蛋白序列，输出预测的蛋白质结构。附带 AlphaFold-Multimer（多链复合物预测）实现、v2.3.0 技术说明与 CASP15 基线预测。运行依赖 Linux、Docker、NVIDIA GPU，需下载约 556 GB（解压 2.62 TB）的遗传数据库与模型参数；模型参数以 CC BY 4.0 授权，代码为 Apache 2.0。代码发布使用，发表成果需引用相应论文。

- 提供 AlphaFold2 单体与 AlphaFold-Multimer 推理流水线
- 提供 monomer/casp14/ptm/multimer 等多种 model_preset
- 附下载脚本统一获取遗传数据库与模型参数
- 支持 --gpu_devices、--max_template_date、reduced_dbs 等运行参数

> L5: This package provides an implementation of the inference pipeline of AlphaFold
> L40: You will need a machine running Linux, AlphaFold does not support other
> L42: genetic databases (SSD storage is recommended) and a modern NVIDIA GPU (GPUs
> L289: **The simplest way to run AlphaFold is using the provided Docker script.** This

## yetone/magpie（⭐14891，confidence: high）

**为多 agent 统一接入模型与账号的本地网关应用**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

在多个 AI coding agent 与多个模型提供方之间做统一接入的本地应用：一个位于 127.0.0.1:3425 的本地网关读写各 agent 自身的配置文件，把模型选择、订阅账号、路由规则集中到一处。网关以 OpenAI Chat、OpenAI Responses、Anthropic Messages、Gemini 四种协议互通，含流式、工具调用与 reasoning。核心机制包括：按 agent 粒度改写配置（保持注释与格式）、配额耗尽时的多账号故障转移路由组、五种调度策略（smart/order/rotate/usage/pace）、基于 npm/Bun 的插件与网关中间件、用量与成本统计、局域网/远程共享。限多 agent 多 provider 用户使用；单一 agent 单一订阅的用户 README 明确表示不适用。

- 本地网关翻译 OpenAI/Anthropic/Gemini 协议，含流式、工具调用与 reasoning
- 配额耗尽自动切换账号/模型，五种路由策略（smart/order/rotate/usage/pace）
- 原子改写各 agent 自身配置，保留注释与格式；Profiles 一键切换全套配置
- npm/Bun 插件体系与网关中间件（param-override、model-map、word-guard 等）

> L8: Switch any of them from the menu bar. One local gateway serves them all,
> L73: The gateway at `127.0.0.1:3425` speaks OpenAI Chat, OpenAI Responses, Anthropic Messages and Gemini, and translates betw
> L91: > **Presets include** Anthropic · OpenAI · Google Gemini · Google Vertex AI · Amazon Bedrock (runtime and Mantle) · Deep

## NVIDIA/TensorRT-LLM（⭐14841，confidence: high）

**开发者在 NVIDIA GPU 上高效运行 LLM 推理的优化库**

`ai_role=ai-ecosystem · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=medium · maturity=idea`

NVIDIA 开源的 LLM 与视觉生成模型推理优化库：提供针对 attention、GEMM、MoE 等常见操作的定制 kernel，以及 Prefill-Decode 分离、Wide Expert Parallelism、Speculative Decoding 等运行时优化。基于 PyTorch 架构，提供高层 Python LLM API，覆盖单卡到多卡、多节点部署，内置多种并行策略，并可与 NVIDIA Dynamo 和 Triton Inference Server 集成；含 Python 和 C++ 运行时组件。Quick Start、安装指南、支持硬件与模型清单、性能基准文档均指向官方文档站点。

- 提供针对 attention/GEMM/MoE 等操作的定制 kernel 与运行时算法优化
- 基于 PyTorch 的 Python LLM API，支持单 GPU 到多 GPU/多节点部署
- 内置多种并行策略，可扩展、可用原生 PyTorch 代码自定义预定义模型
- 支持扩散模型视觉生成，与 NVIDIA Dynamo 和 Triton Inference Server 集成

> L263: TensorRT LLM is an open-sourced library for optimizing LLM and Visual Gen inference. It provides state-of-the-art optimi
> L265: Architected on PyTorch, TensorRT LLM provides a high-level Python LLM API that supports a wide range of inference setups
> L267: TensorRT LLM is designed to be modular and easy to modify. Its PyTorch-native architecture allows developers to experime

## llmware-ai/llmware（⭐14814，confidence: high）

**为企业在本地/边缘设备构建小型专用模型 RAG 应用的统一框架**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

llmware 是一个 Python 框架，包含模型目录（300+ 预打包量化模型，含 50+ 自研 SLIM/Bling/Dragon/Industry-Bert 微调模型）与 RAG Pipeline（文档解析、分块、嵌入、知识库构建与查询）两大组件，用于将知识源接入生成式 AI 模型。推理层支持 GGUF、OpenVINO、ONNXRuntime、ONNXRuntime-QNN、WindowsLocalFoundry、Pytorch 等后端，并支持 OpenAI、Anthropic、Google 云端模型；数据层提供 3 种文本库与 10 种向量库组合，默认 SQLite+ChromaDB 开箱即用。主要面向企业流程自动化场景。

- 模型目录含 300+ 模型，其中 50+ 为 RAG 优化的小参数量微调模型（1-7B）
- 支持 GGUF、OpenVINO、ONNXRuntime-QNN（骁龙 NPU）等多推理后端
- 集成 3 种文本数据库与 10 种向量数据库，含 Docker Compose 部署脚本
- LLMfx Agent 支持基于 SLIM 模型的函数调用多步工作流

> L9: `llmware` is optimized for AI PC and local laptop, edge and self-hosted deployment across a wide range of Windows, Mac a
> L13:  1. **Model catalog with 300+ models** - models prepackaged in quantized, optimized formats, to leverage on device GPU a
> L15:  2. **RAG Pipeline** - integrated components for the full lifecycle of connecting knowledge sources to generative AI mod

## tensorflow/tfjs-models（⭐14802，confidence: high）

**前端开发者在浏览器中运行 TensorFlow.js 预训练模型集合**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

托管一组已移植到 TensorFlow.js 的预训练模型，发布在 NPM 与 unpkg 上，可直接使用或在 TensorFlow.js 中做迁移学习。涵盖图像分类、手部/人体姿态检测、目标检测、语义分割、人脸关键点、语音命令分类、文本编码与毒性评分、人像深度估计，另附 KNN 分类器等通用工具。API 设计上隐藏张量细节，面向非机器学习专家，每个模型有独立目录与 README。

- 提供 MobileNet 图像分类、Coco SSD 目标检测、DeepLab v3 语义分割等图像模型
- 支持浏览器端实时手部/人体姿态检测与 3D 人脸关键点检测
- 包含语音命令分类、文本编码/毒性评分、人像深度估计
- 提供 KNN 分类器工具包，支持迁移学习场景

> L3: This repository hosts a set of pre-trained models that have been ported to
> L6: The models are hosted on NPM and unpkg so they can be used in any project out of the box. They can be used directly or u
> L11: non-machine learning experts.

## livekit/agents（⭐14789，confidence: mid）

**给开发者：构建实时语音 AI Agent 的 Python 框架**

`ai_role=ai-native · license_risk=dual · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

LiveKit Agents 是用于在服务器上构建实时、可编程参与者的框架，用于创建能看、能听、能理解的多模态对话语音 Agent。机制包括：STT/LLM/TTS/Realtime API 的可组合插件生态、内置任务调度与分发 API、基于 transformer 的语义轮次检测、MCP 工具一行代码接入、内置测试框架与 judge。提供 dev 热重载、console 终端测试与生产三种运行模式，需连接 LiveKit Cloud 或自托管服务器。Apache-2.0 许可，轮次检测模型采用单独的 LiveKit Model License。

- STT/LLM/TTS/Realtime API 插件生态，可自由组合模型供应商
- 内置任务调度与分发 API，连接终端用户与 Agent
- 语义轮次检测与 MCP 原生支持
- 内置测试框架，支持 pytest 集成与 console 终端本地音频测试

> L14: The Agent Framework is designed for building realtime, programmable participants
> L20: - **Flexible integrations**: A comprehensive ecosystem to mix and match the right STT, LLM, TTS, and Realtime API to sui
> L35: pip install "livekit-agents[openai,deepgram,cartesia]"

## oblien/openship（⭐14789，confidence: high）

**给开发者的自托管部署平台：从仓库到带 TLS 的线上应用**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=—`

自托管部署平台，内置 CI/CD：指向一个 GitHub 仓库、本地目录或预构建产物后，执行检测栈、构建（Docker 镜像或裸发布）、以容器或受管进程运行、由 OpenResty 边缘写反向代理并签发 Let's Encrypt 证书的完整流水线，支持 GitHub webhook 推送部署与单体仓库增量重建。提供桌面应用、Web 面板、CLI、JS/TS SDK 四种接口，另暴露 MCP 端点供 AI agent 调用（仅显式开放的路由成为工具，每次调用重查权限）。运行形态分桌面本机、Compose 模式（Linux+Docker）与 bare 模式；多节点与负载均衡 UI 尚在计划中。

- 从仓库检测到反向代理 + Let's Encrypt 证书的一体化部署流水线
- 桌面应用 / Web 面板 / CLI / JS/TS SDK 四种操作接口
- MCP 端点供 AI agent 调用，权限路由显式开放、逐次校验
- 内置 CI/CD、数据库/域名/SSL/CDN/邮件/备份统一管理

> L3:  Open-source, self-hostable deployment platform with built-in CI/CD.
> L170: An **MCP** endpoint (for AI agents) and a **REST API** round it out for automation. Only routes that opt in are exposed 

## DataTalksClub/machine-learning-zoomcamp（⭐14773，confidence: high）

**面向工程师的免费 4 个月机器学习工程实战课程**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

DataTalks.Club 出品的免费机器学习工程课程，覆盖从问题定义、数据准备、模型训练评估到通过 API 部署上线的完整流程。技术栈包括 Python、scikit-learn、TensorFlow、PyTorch、FastAPI、Docker、Kubernetes 与 AWS Lambda。支持随直播批次学习（含作业评分、同伴评审、证书资格）或按材料自学（免费但不评分、无证书）。前置要求为至少一年编程经验，不要求 ML 经验或本地 GPU，深度学习模块使用云端资源。

- 10 个模块 + 期中与两个 capstone 项目的完整课程结构
- 覆盖模型训练到 FastAPI/Docker/Kubernetes/AWS Lambda 部署全链路
- 支持直播批次（证书/评审/排行榜）与自学两种参与方式
- 深度学习模块使用云端资源，不要求本地 GPU

> L34: Machine Learning Zoomcamp is a free, practical course for people who want to learn machine learning engineering by build
> L40: You will work with Python, NumPy, pandas, scikit-learn, TensorFlow, PyTorch, FastAPI, Docker, Kubernetes, and AWS Lambda
> L81: - A powerful computer or local GPU. The deep learning modules use cloud resources for more intensive computation.

## BlinkDL/RWKV-LM（⭐14750，confidence: high）

**RWKV 线性 RNN 语言模型的参考实现与训练指南**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=gpu-8g · install_friction=high · maturity=research`

RWKV 语言模型架构的主仓库，当前为 RWKV-7 "Goose"：一种线性时间、常数空间（无 kv-cache）、无 attention 的 100% RNN 架构，可像 GPT transformer 一样并行训练。仓库提供 RWKV-v7 参考训练实现（train_temp）、CUDA kernel、MiniPile/Pile 训练流程、参数初始化表，以及 demo 代码与推理评测链接；并列出权重（HuggingFace）、GGUF、pip 包、GUI 运行器、服务器等周边生态。训练参考配置最低 1 GPU 7G 显存。

- RWKV-7：线性时间、常数空间、无 kv-cache 的 RNN 架构，可并行训练
- 提供 train_temp 参考实现，默认配置 1 GPU 7G 显存即可运行
- 提供 CUDA kernel 仓库与推理评测代码（MMLU、MATH500 等）
- README 含 MiniPile/Pile 训练教程与逐参数初始化/权重衰减表

> L1: # RWKV: Parallelizable RNN with Transformer-level LLM Performance (pronounced as "RwaKuv" (rʌkuv in IPA), from 4 major p
> L11: RWKV-7 "Goose" is a strong **linear-time** & **constant-space** (no kv-cache) & **attention-free** & 100% RNN architectu
> L45: **Please use https://github.com/BlinkDL/RWKV-LM/tree/main/RWKV-v7/train_temp as RWKV-7 reference implementation**. The d

## nltk/nltk（⭐14741，confidence: high）

**面向 NLP 研究与开发的 Python 模块、数据集与教程套件**

`ai_role=ai-ecosystem · license_risk=dual · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

NLTK 是一套开源 Python 模块、数据集与教程，支持自然语言处理的研究与开发。要求 Python 3.10 至 3.14。文档托管于 nltk.org，贡献指南与引用条目（NLTK 书，O'Reilly 2009）在 README 中给出。源码采用 Apache 2.0 许可，文档采用 CC BY-NC-ND 3.0，语料库按各自 README 条款以非商业用途再分发。

- 提供 Python 模块、数据集与教程的组合
- 要求 Python 3.10–3.14
- 源码 Apache 2.0，文档 CC BY-NC-ND 3.0，语料库可再分发

> L5: NLTK -- the Natural Language Toolkit -- is a suite of open source Python
> L6: modules, data sets, and tutorials supporting research and development in Natural
> L7: Language Processing. NLTK requires Python version from 3.10 up to the latest 3.14.

## casdoor/casdoor（⭐14596，confidence: high）

**为应用与 AI agent 提供自托管 SSO/IAM 的认证服务器**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

自托管的单点登录与身份认证服务器，带 Web 管理控制台。支持 OAuth 2.0、OIDC、SAML 2.0、CAS、LDAP、SCIM 2.0、WebAuthn、TOTP/MFA、Face ID 等协议，并可对接 Google Workspace、Entra ID、GitHub 等身份提供方。组织、应用、登录方式等均在控制台配置，无需改动配置文件重新部署；授权策略基于 Casbin（ACL/RBAC/ABAC）。AI 相关部分包括 MCP 网关与 A2A 通信支持。提供 Docker、Docker Compose、Helm、源码四种安装路径及商业托管版 Casdoor Cloud。

- 多协议认证：OAuth 2.0/OIDC、SAML 2.0、CAS、LDAP、SCIM 2.0、WebAuthn、TOTP/MFA、Face ID
- MCP 网关：暴露 Model Context Protocol 服务器并控制访问，另支持 A2A 通信
- Casbin 策略授权（ACL/RBAC/ABAC）与多租户组织管理
- 四种安装路径：Docker all-in-one、Docker Compose+MySQL、Helm、源码构建

> L7:  Casdoor is a single sign-on (SSO) and authentication server with a web console.
> L225: - **MCP gateway** — expose Model Context Protocol servers and control access to them
> L226: - **A2A** — agent-to-agent communication support

## waooAI/waoowaoo（⭐14573，confidence: high）

**给创作者的可控 AI 影像生产画布工作区**

`ai_role=ai-native · license_risk=none · deploy=— · model_dep=locked-api · hardware=— · install_friction=medium · maturity=idea`

自托管的图像与视频创作工作区：右侧 Assistant 协助开发创意简报并生成资产，画布上上传参考素材、整理文件并检查生成结果。支持首帧、首尾帧、参考图等生成模式（可用性随所选模型而定），可对既有结果迭代新版本并保留原版。预览版通过 OpenRouter 接入模型（GPT Image 2、Nano Banana、Seedance、MiniMax H3 系列），调用费用由用户自己的 OpenRouter 账户承担；预览版不含音乐与配音控制。推荐以预构建 Docker 镜像分发部署。

- 画布式工作区：上传参考、整理文件、检视生成的图像与视频
- 模型感知的宽高比、时长、分辨率与参考角色配置
- 首帧/首尾帧/参考图生成模式，结果可迭代出新版本并保留原件
- 提供编码助手自动安装脚本与预构建 Docker 镜像两种部署路径

> L5:  An AI creative workspace for images and videos: develop ideas with the right-hand Assistant, upload references, and org
> L22: This preview exposes **OpenRouter** configuration. Available models include GPT Image 2, Nano Banana variants, Seedance 
> L43: After launching, open your profile’s **API configuration** and add your OpenRouter API key. Provider calls are paid thro

## nidhinjs/prompt-master（⭐14544，confidence: high）

**给各 AI 工具写精准提示词的 Claude skill**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

以 Claude skill 形式分发的提示词生成器：对用户请求运行结构化流水线——检测目标工具、提取 9 维意图、最多 3 个澄清问题、自动路由到 13 个提示词模板之一、应用 5 种声明为安全的技术、做 token 效率审计后输出单个可复制提示词。内置 30+ 工具 profile，未收录的工具用 4 问 Universal Fingerprint 处理。明确排除 Tree of Thought 等易幻觉方法。面向使用多个 AI 工具的普通用户。

- 覆盖推理、编码、图像、视频、语音、自动化等 30+ 工具的专用 profile
- 13 个提示词模板自动选择并对用户隐藏框架名
- 检测 37 种浪费额度的提示词模式并给出改写
- max 3 个澄清问题与 token 效率审计机制

> L1: A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory 
> L71: Prompt Master runs a structured pipeline on every request:

## gunthercox/ChatterBot（⭐14520，confidence: high）

**面向开发者的 Python 机器学习对话引擎，用于创建聊天机器人**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

基于机器学习的对话引擎 Python 库：从已知对话集合中生成回复，输入语句会被保存并与对应回复关联，随输入增多可回复的数量与准确度提升；通过搜索最匹配的已知语句、按回复出现频率选出最可能的回应。语言无关设计，可训练为任意语言，内置十余种语言的训练数据模块（chatterbot-corpus），社区欢迎提交语料。通过 PyPI 安装，BSD 3-clause 许可。

- 从已知对话集合生成匹配回复，随输入累积提升准确度
- 语言无关设计，可训练为任意语言
- 内置十余种语言的训练数据模块
- 提供 ChatterBotCorpusTrainer 训练接口

> L5: ChatterBot is a machine-learning based conversational dialog engine built in
> L25: An untrained instance of ChatterBot starts off with no knowledge of how to communicate. Each time a user enters a statem
> L81: ChatterBot is licensed under the BSD 3-clause license.

## carla-simulator/carla（⭐14502，confidence: high）

**面向自动驾驶研究的开源仿真器**

`ai_role=ai-ecosystem · license_risk=dual · deploy=— · model_dep=— · hardware=— · install_friction=medium · maturity=research`

CARLA 是面向自动驾驶系统开发、训练与验证的开源仿真器，提供开源代码、协议及可自由使用的城市布局、建筑、车辆等数字资产，支持灵活配置传感器组合与环境条件。当前 ue5-dev 分支基于 Unreal Engine 5.5，与 ue4-dev 分支并行维护。Linux/Windows 通过官方 setup 脚本从源码构建，需事先关联 Epic Games 账号以访问 UE5 fork，构建消耗较大磁盘空间与时间；项目有 CoRL'17 论文引用要求与 MIT/CC-BY 双重许可安排。

- 开源仿真器附带可自由使用的城市、车辆等数字资产
- 支持灵活指定传感器组合与环境条件
- 提供 ROS-bridge、Scenario_Runner、自动排行榜等生态仓库
- 提供 Python API 与蓝图库，跨 Linux/Windows 平台

> L11: CARLA is an open-source simulator for autonomous driving research. CARLA has been developed from the ground up to suppor
> L19: > This is the development branch `ue5-dev` for the **Unreal Engine 5.5 version of CARLA**. This branch exists in paralle
> L82: In order to build CARLA, you need access to the CARLA fork of Unreal Engine 5.5. In order to access this repository, you

## davisking/dlib（⭐14461，confidence: high）

**C++ 机器学习与数据分析算法工具库**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=—`

一个 C++ 工具包，包含机器学习算法与用于构建复杂软件的工具，同时提供 Python API。README 给出三条使用路径：编译 examples 目录的 C++ 示例程序（需 C++17 编译器与 CMake）、通过 vcpkg 安装 C++ 库、以及从 PyPI 或 GitHub 源码安装 Python API。构建时可开启 AVX 指令加速，支持通过 setup.py 参数或 DLIB_* 环境变量调整构建选项。采用 Boost 软件许可证，允许闭源商业使用。

- C++ 机器学习算法工具包，附 Python API
- vcpkg 单命令安装 C++ 库并集成 CMake
- AVX 指令加速选项与 DLIB_* 环境变量构建配置
- Boost 许可证，允许闭源商业使用

> L3: Dlib is a modern C++ toolkit containing machine learning algorithms and tools for creating complex software in C++ to so
> L7: You need a C++17 compiler and CMake. Go into the examples folder and type:
> L38: Either fetch the latest stable release of dlib from PyPi and install that:

## PaddlePaddle/PaddleDetection（⭐14443，confidence: high）

**给开发者的目标检测端到端开发套件**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

基于 PaddlePaddle 框架的目标检测开发套件，覆盖 2D/3D 目标检测、实例分割、多目标跟踪、关键点检测、人脸检测与半监督学习等方向。将模型解耦为 backbone、neck、loss、数据增强等可组合模块，提供 PP-YOLOE+、PP-PicoDet、PP-TinyPose、PP-HumanV2、PP-Vehicle 等产业特色模型与预训练权重，并整理农业、工业、交通等领域的应用范例。部署路径包括 Paddle Inference、Paddle Lite、Paddle Serving 及 ONNX 导出。安装说明需另行参考安装文档。

- 模型库覆盖 2D/3D 检测、实例分割、多目标跟踪、关键点检测等方向
- 模块化设计：backbone/neck/loss/数据增强组件可自定义组合
- 提供 Paddle Inference/Paddle Lite/Paddle Serving 部署与 ONNX 导出
- PP 系列产业模型附带预训练模型与产业应用示例代码

> L8: PaddleDetection是一个基于PaddlePaddle的目标检测端到端开发套件，在提供丰富的模型组件和测试基准的同时，注重端到端的产业落地应用，通过打造产业级特色模型|工具、建设产业应用范例等手段，帮助开发者实现数据准备、模型选型
> L54: PaddleDetection支持大量的最新主流的算法基准以及预训练模型，涵盖2D/3D目标检测、实例分割、人脸检测、关键点检测、多目标跟踪、半监督学习等方向。`传送门`：📱模型库、⚖️模型性能对比。

## fathah/hermes-desktop（⭐14425，confidence: mid）

**为 Hermes Agent 提供安装、配置与对话的桌面应用**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=local-ok · hardware=— · install_friction=low · maturity=idea`

社区维护的原生桌面应用，把 Hermes Agent 的安装、provider 配置与日常使用集中到 GUI：首次启动引导本地安装（调用官方安装脚本，存放于 ~/.hermes）或连接远程 API，本地模式经 127.0.0.1:8642 以 SSE 流式通信。覆盖会话管理、多 Profile 隔离、记忆条目编辑、SOUL.md 人格编辑、cron 定时任务、16 个消息网关与备份/日志查看。API key 默认存于 .env，可选 command provider 对接多种密码管理器；该 provider 仅限 POSIX 系统。项目处于活跃开发期。

- 引导式首次安装 Hermes Agent（本地/远程两种模式）
- 多 provider 支持：OpenRouter、Anthropic、OpenAI、Gemini、Grok 等 11 类及 OpenAI 兼容本地端点
- 22 个 slash 命令与 14 个工具集（浏览器、终端、图像生成、TTS 等）
- secrets command provider 可对接 KeePassXC、GnuPG、pass、1Password CLI 等

> L26: Hermes One is a community maintained native desktop app for installing, configuring, and chatting with Hermes Agent — a 
> L88: - **Multi-provider support** — OpenRouter, Anthropic, OpenAI, Google (Gemini), xAI (Grok), Nous Portal, Qwen, MiniMax, H

## e2b-dev/E2B（⭐14413，confidence: high）

**为 AI agent 提供云端安全沙箱，运行生成的代码**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

E2B 是开源基础设施，在云端安全隔离沙箱中运行 AI 生成的代码，通过 JavaScript 或 Python SDK 创建并控制沙箱。提供三个 SDK：核心沙箱 SDK（执行命令）、Code Interpreter SDK（runCode 执行代码并获取结果）、Desktop SDK（鼠标、键盘、截图、桌面流等计算机操作 API）。使用需注册获取 API key 并设置环境变量；支持通过 Terraform 自托管部署到自有云环境。

- 云端隔离沙箱中运行 AI 生成的代码
- JavaScript 与 Python 双 SDK，另有 Code Interpreter 与 Desktop 扩展 SDK
- Desktop SDK 提供鼠标、键盘、截图与应用流 API
- 支持 Terraform 自托管，支持 AWS/GCP/Azure/Linux

> L13: E2B is an open-source infrastructure that allows you to run AI-generated code in secure isolated sandboxes in the cloud.
> L99: Read the embed deployment guide to learn how to set up the E2B runtime on your own. The infrastructure is deployed using

## flairNLP/flair（⭐14392，confidence: high）

**面向开发者的 NLP 任务库：NER、情感分析、词性标注与文本嵌入**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=research`

由柏林洪堡大学等开发的 PyTorch NLP 框架，当前版本 0.15.1。提供预训练模型覆盖命名实体识别、情感分析、词性标注、 biomedical 文本处理、词义消歧与分类，支持多语言。同时作为文本嵌入库提供词与文档嵌入的组合接口，可直接基于 PyTorch 训练自定义模型。模型托管于 Hugging Face model hub，README 附带在线 demo 与评分对比表，需 Python 3.9+。

- 提供 NER、情感分析、词性标注等任务的预训练模型
- 支持组合多种词与文档嵌入（含 Flair embeddings 与 transformers）
- 构建于 PyTorch 之上，可训练自定义模型
- 模型托管在 Hugging Face model hub 并提供在线试用

> L9: A very simple framework for **state-of-the-art NLP**. Developed by Humboldt University of Berlin and friends.
> L21: * **A PyTorch NLP framework.** Our framework builds directly on PyTorch, making it easy to
> L51: Flair requires Python 3.9+.

## lsdefine/GenericAgent（⭐14324，confidence: mid）

**自进化 Agent 框架：从约3K行种子代码生长个人技能树**

`ai_role=ai-native · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=low · maturity=research`

以约3K行种子代码、9个原子工具和约100行 Agent Loop 构成的自主 Agent 框架，赋予 LLM 对本地计算机的系统级控制，覆盖浏览器、终端、文件系统、键鼠输入、屏幕视觉与 ADB 移动设备。每次完成新任务会把执行路径固化为可复用 Skill，形成个人技能树；配套 L0-L4 分层记忆系统与 TUI/Streamlit/IM 多种前端。需配置 LLM API key，Python 限定 3.11/3.12。预置 SOP 以中文撰写，核心依赖刻意精简。

- 任务执行路径自动固化为可复用 Skill，形成个人技能树
- 9 个原子工具 + 约100行核心 Agent Loop（agent_loop.py）
- L0-L4 分层记忆系统沉淀经验与 SOP
- 支持 Telegram/Discord/Lark 等 IM 前端接入

> L23: **GenericAgent** is a minimal, self-evolving autonomous agent framework. Its core is just **~3K lines of code**. Through
> L39: |🧬 **Self-Evolving**|Automatically crystallizes each task into a Skill. Capabilities grow with every use, forming your p

## deeplearning4j/deeplearning4j（⭐14270，confidence: high）

**JVM 平台的深度学习训练与部署工具套件**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=medium · maturity=—`

Eclipse Deeplearning4J 是面向 JVM 的深度学习项目集合，覆盖从数据加载、预处理到构建与调优各类深度网络的流程。套件包含高层 API（DL4J）、线性代数库 ND4J（基于 C++ 的 LibND4J，提供 CPU/GPU 加速）、自动微分框架 SameDiff、ETL 工具 DataVec 与 Python4J。支持 Keras、TensorFlow、ONNX 模型导入，可在 Apache Spark 上分布式训练。仅支持通过构建工具使用，可从源码构建。由 Konduit K.K. 团队开发。

- ND4J 提供 500+ 数学/线性代数/深度学习运算，底层 C++ 支持 CPU（AVX2/512）与 CUDA GPU 加速
- SameDiff 自动微分框架支持导入 TensorFlow .pb 模型
- DL4J 支持 Keras h5 模型导入与 Apache Spark 分布式训练
- 支持 Java、Scala、Kotlin、Clojure 等 JVM 语言

> L8: The **Eclipse Deeplearning4J** (DL4J) ecosystem is a set of projects intended to support all the needs of a JVM based de
> L14: - **ND4J**: General purpose linear algebra library with over 500 mathematical, linear algebra and deep learning operatio
> L84: Deeplearning4J is actively developed by the team at Konduit K.K..

## janishar/mit-deep-learning-book-pdf（⭐14270，confidence: high）

**为学习者提供 MIT 深度学习教材的 PDF 版本**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

将 MIT Press《Deep Learning》（Ian Goodfellow、Yoshua Bengio、Aaron Courville 著）的 HTML 免费版本排版装订为 PDF，提供完整全书与分章节两种 PDF 下载。README 说明原书官网不提供 PDF 下载，作者按官网建议以 Chrome 打印 HTML 内容制作本版本；另收录练习题、讲义幻灯片与外部链接等学习资源入口，并引导读者购买纸质书支持原作者。

- 提供完整全书 PDF 与分章节 PDF 两种形式
- 内容源自官方免费 HTML 版本（deeplearningbook.org）
- 收录练习题、讲义幻灯片与外部链接清单

> L6: MIT Deep Learning Book in PDF format (complete and parts) by Ian Goodfellow, Yoshua Bengio and Aaron Courville.
> L38: 1. The pdf version of the book which is available in html at http://www.deeplearningbook.org/
> L39: 2. The book is available in chapter wise PDFs as well as complete book in PDF.

## mlfoundations/open_clip（⭐14203，confidence: high）

**给研究者的开源 CLIP（图文对比学习）PyTorch 实现**

`ai_role=ai-ecosystem · license_risk=none · deploy=library · model_dep=— · hardware=— · install_friction=medium · maturity=research`

CLIP 的开源实现，基于 PyTorch 提供图文对比学习模型的训练与推理。main 分支的训练栈围绕 TrainingTask 封装、dict 批次、FSDP2、NaFlex 图像/音频管线与多种 torch.compile 策略组织，新增 CLAP 音频-文本、CoCa、MaMMUT、SigLIP 等模型族配置；旧版训练 API 需固定到 v3 分支或 PyPI 3.x 版本。预训练图文模型的推理用法保持兼容。提供论文链接与 Colab 示例。

- CLIP 的开源 PyTorch 实现，支持训练与预训练模型推理
- 训练支持 FSDP2、多种 torch.compile 策略与 NaFlex 可变分辨率/音频管线
- 包含 CLIP、SigLIP、CoCa、MaMMUT、CLAP 等模型族配置
- 提供交互式 Colab notebook 与论文引用入口

> L1: # OpenCLIP
> L8: > `main` now uses the post-refactor training stack by default. Training is organized around `TrainingTask` wrappers, dic
> L45: > - Training pipeline wraps `model + loss` in a `TrainingTask` subclass (`CLIPTask`, `SigLIPTask`, `CoCaTask`, `DistillC

## microsoft/agent-framework（⭐14179，confidence: high）

**面向团队构建生产级 AI agent 与多 agent 工作流的多语言框架**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=locked-api · hardware=— · install_friction=medium · maturity=—`

Microsoft Agent Framework（MAF）是支持 Python、.NET 与 Go 的多语言开源框架，用于构建、编排与部署 AI agent 及多 agent 工作流。面向要把 agent 从原型推进到生产的团队，提供图式编排（顺序、并发、handoff、群协作）、检查点与断点恢复、OpenTelemetry 可观测性、YAML 声明式 agent、中间件管道与 DevUI 调试界面；通过 PyPI（agent-framework）与 NuGet（Microsoft.Agents.AI）分发，另有 AF Labs 实验包与从 Semantic Kernel、AutoGen 迁移的指南。

- 支持 Python、.NET 与 Go，跨语言一致 API
- 图式多 agent 工作流：顺序/并发/handoff/群协作，含检查点、human-in-the-loop 与 time-travel
- 内置 OpenTelemetry 分布式追踪；YAML 声明式定义 agent
- Foundry 托管部署（2 行代码）与 DevUI 开发调试界面

> L11: Microsoft Agent Framework (MAF) is an open, multi-language framework for building **production-grade AI agents and multi
> L13: Microsoft Agent Framework is built for teams taking agents from prototype to production. It provides a consistent founda
> L46: - **Orchestration Patterns & Workflows**: Build multi-agent systems with graph-based workflows supporting sequential, co

## datawhalechina/llm-universe（⭐14159，confidence: high）

**面向小白的中文大模型应用开发教程：RAG 知识库助手**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Datawhale 出品的中文开源教程，以个人知识库助手项目为主线，讲解大模型应用开发流程：调用大模型 API、搭建向量知识库、用 LangChain 构建检索问答链、Streamlit 部署、评估与优化，并规划进阶 RAG 技巧与开源应用解读两部分内容。面向具备基础 Python 能力、无人工智能与算法基础的开发者。对百度文心、讯飞星火、智谱 GLM 等 API 做了统一封装。教程不需要 GPU，提供阿里云服务器学生免费领取及本地环境搭建指南。

- 基于个人知识库助手项目的实践式课程，含 API 调用、向量库、RAG 问答链、部署与评估全流程
- 对 GPT、百度文心、讯飞星火、智谱 GLM 等国内外主要 LLM API 统一封装，支持一键调用
- 无需 GPU 环境，提供阿里云服务器学生免费领取与本地环境搭建指南
- 内容大纲含进阶 RAG 技巧（分块优化、混合检索、微调向量模型等）与开源应用案例解读

> L13: 本项目是一个面向小白开发者的大模型应用开发教程，旨在基于阿里云服务器，结合个人知识库助手项目，通过一个课程完成大模型开发的重点入门，主要内容包括：
> L47: 所有具备基础 Python 能力，想要掌握 LLM 应用开发技能的开发者。
> L63: 3. 兼具统一性与拓展性。本项目对 GPT、百度文心、讯飞星火、智谱GLM 等国内外主要 LLM API 进行了统一封装，支持一键调用不同的 LLM，帮助开发者将更多的精力放在学习应用与模型本身的优化上，而不需要花时间在繁琐的调用细节上；同

## Open-LLM-VTuber/Open-LLM-VTuber（⭐14148，confidence: high）

**本地运行的语音交互 AI 陪伴：Live2D 形象+免手操作对话**

`ai_role=ai-native · license_risk=dual · deploy=— · model_dep=local-ok · hardware=— · install_friction=medium · maturity=idea`

跨平台语音交互 AI 陪伴项目：整合 LLM 推理、语音识别与语音合成方案，支持实时语音对话、语音打断、视觉感知（摄像头/截屏/录屏）与 Live2D 虚拟形象。提供网页版与桌面客户端两种模式，桌面客户端支持透明背景桌宠模式。全部功能可完全离线运行于本地。通过配置文件切换各功能模块，可自定义 Live2D 模型、人设 Prompt 与声音克隆。安装依赖 uv，v1.0.0 存在破坏性变更需重新部署。

- 完全离线模式：本地模型运行，对话数据不出设备
- 语音打断（免耳机）与视觉感知（摄像头/屏幕截图）
- Live2D 表情映射、桌宠模式与触摸交互
- 模块化可扩展：LLM/ASR/TTS 模块经配置文件切换

> L35: **Open-LLM-VTuber** is a unique **voice-interactive AI companion** that not only supports **real-time voice conversation
> L70:  - 🤖 Large Language Models (LLM): Ollama, OpenAI (and any OpenAI-compatible API), Gemini, Claude, Mistral, DeepSeek, Zhi
> L54: - 🔒 **Offline mode support**: Run completely offline using local models - no internet required. Your conversations stay 

## isl-org/Open3D（⭐14098，confidence: high）

**为 C++/Python 开发者提供 3D 数据处理的开源库**

`ai_role=ai-ecosystem · license_risk=none · deploy=desktop · model_dep=— · hardware=cpu-ok · install_friction=medium · maturity=research`

Open3D 是处理 3D 数据的开源库，前端在 C++ 与 Python 中提供数据结构与算法，后端针对并行化设置。功能覆盖 3D 数据结构、处理算法、场景重建、表面对齐、3D 可视化、基于物理的渲染（PBR），并支持 PyTorch 与 TensorFlow 的 3D 机器学习及核心操作的 GPU 加速。提供 pip 预编译包（Ubuntu/macOS/Windows）、C++ 二进制包、独立 Viewer 应用与 Open3D-ML 扩展，发布工件含 SLSA 构建来源证明。

- C++ 与 Python 双接口，覆盖 3D 数据结构与处理算法
- 支持 PyTorch 与 TensorFlow 的 3D 机器学习（Open3D-ML 扩展）
- 核心 3D 操作支持 GPU 加速
- 提供 pip 预编译包与独立 3D Viewer 应用

> L33: - 3D machine learning support with PyTorch and TensorFlow
> L105: Open3D-ML is an extension of Open3D for 3D machine learning tasks. It builds on

## semantica-agi/semantica（⭐14090，confidence: high）

**为 AI 系统提供上下文图谱与决策溯源的开源基础设施**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

以 Python 库形式提供的语义/上下文层：摄取企业数据后抽取实体与关系，构建 Context Graph 与知识图谱，并支持 Rete/Datalog/SPARQL 确定性推理、W3C PROV-O 溯源、SHACL/OWL 本体治理与决策记录。图谱构建、推理与溯源不依赖 LLM，LLM 调用为可选项。图存储支持 RDF 与 LPG 多后端互换，提供 REST API、MCP server、CLI 与可视化界面。面向 AI/ML 平台团队、企业数据团队与受监管行业的合规/审计场景。

- 每个事实带 W3C PROV-O 溯源，决策作为一等图节点可查询
- 确定性推理引擎（前向链、Rete、Datalog、SPARQL），图谱构建无需 LLM
- 多源摄取连接器：Databricks、Snowflake、SAP、Kafka、Git 等
- RDF（Oxigraph、Blazegraph 等）与 LPG（Neo4j、FalkorDB 等）存储可互换

> L54: Semantica is the semantic/context layer underneath your LLM, vector store, and agent framework: deterministic infrastruc
> L74: - **Context Graphs:** A structured, queryable graph of everything your agent knows, decides, and reasons about
> L101: Semantica complements your existing stack rather than replacing it. Keep your LLM, vector store, and agent framework exa

## cactus-compute/needle（⭐14071，confidence: high）

**面向小型设备的端侧自动化基础模型（8-29 MB）**

`ai_role=ai-native · license_risk=permissive · deploy=desktop · model_dep=— · hardware=— · install_friction=medium · maturity=—`

Cactus Compute 团队构建的基础模型，单一二进制文件 8-29 MB，为手机、可穿戴、智能家居、机器人、汽车和微控制器提供端侧能力：根据应用暴露的函数生成工具调用并填充参数、按声明结构抽取类型化字段、句子级文本嵌入，配套 16.9 MB 的 Whistle 语音转文字模型共享同一引擎。支持 2-bit 量化的 .cact 容器格式，可通过 LoRA 或平台微调裁剪到 2 层子网络部署到更小设备。权衡说明：模型以牺牲通用对话能力换取工具调用表现。默认开启遥测，可用环境变量关闭。

- 工具调用：从用户话语生成函数调用并填充参数，无覆盖时返回空列表
- 结构化抽取：由 schema 编译的字节级语法约束解码，保证输出可解析
- Whistle 语音模型与 Needle 共享 .cact 容器与 C++ 引擎，音频入、工具调用出
- 本地（JAX CPU/CUDA/Metal）与平台两种微调路径，子网络最小可至 2 层

> L3: A foundation model for mobiles, wearables, robots, smart home, automotive and microcontrollers. The whole model is a sin
> L164: Needle is built by the Cactus Compute team. If you use it in your work, please cite:

## browseros-ai/BrowserOS（⭐13970，confidence: high）

**给 AI agent 用的第二浏览器：代理执行登录态网页任务**

`ai_role=ai-native · license_risk=viral · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

一个面向 AI agent 的浏览器：从 Chrome 一键导入登录态、书签与扩展，连接 Claude Code、Codex、Cursor 等任意 MCP 协议的 agent，让 agent 在独立标签页并行执行网页任务；提供实时仪表盘、会话录像回放（含动作时间线）与本地存储（~/.browserclaw/）。基于 Chromium fork，数据不出本机。与内置 AI 的 BrowserOS 由同一 monorepo 发布。AGPL-3.0 许可。

- 一键连接 Claude Code、Codex、Cursor、VS Code 等支持 MCP 的 agent
- 从 Chrome 一键导入登录态，agent 以真实账号执行任务
- 会话保存为可拖动回放的视频并附动作时间线
- 会话、截图、历史本地存储，数据不上传

> L21: A second browser, just for your AI agents. Import your logins from Chrome in one click, connect Claude Code, Codex, or a
> L86: - **Not a locked-in AI browser.** Atlas, Comet, and Dia only work with their own AI. BrowserOS neo works with the agents
> L121: Both browsers ship from this monorepo. Two main subsystems: the **browser** (Chromium fork, C++ and Python) and the **ag

## DLR-RM/stable-baselines3（⭐13901，confidence: high）

**给 RL 研究者与工程师提供 PyTorch 强化学习算法参考实现库**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=research`

基于 PyTorch 的强化学习算法实现集合（Stable Baselines 的后续主要版本），提供 A2C、PPO、DQN、SAC、TD3 等算法的统一接口，支持自定义环境与自定义策略、Dict 观测空间、Tensorboard 日志与回调机制。代码遵循 sklearn 风格语法。面向研究社区与工业界，用于复现、对比与新想法验证；README 提示使用者需具备一定 RL 基础。核心仓库目前聚焦于 bug 修复与维护，新算法在 SB3-Contrib、SBX 等关联仓库中开发。

- 提供 A2C、PPO、DQN、SAC、TD3 等多种强化学习算法的统一接口实现
- 支持自定义环境、自定义策略、Dict 观测空间与多进程训练
- 与 Weights & Biases、Hugging Face 存在文档记载的集成
- 提供 Google Colab 在线运行示例与配套训练框架 RL Baselines3 Zoo

> L7: Stable Baselines3 (SB3) is a set of reliable implementations of reinforcement learning algorithms in PyTorch. It is the 
> L11: These algorithms will make it easier for the research community and industry to replicate, refine, and identify new idea
> L94: **Note:** Stable-Baselines3 supports PyTorch >= 2.8

## google/ax（⭐13880，confidence: high）

**集群级 agent 工作负载的声明式编排运行时**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=idea`

AX 是一个声明式编排器，用于在集群上运行大规模自主 agent 工作负载，基于 Agent Substrate 提供沙箱执行。核心原语包括 Task（隔离沙箱运行不可信 agent 代码，含 CPU/内存限制）、Workspace（预置 Git 仓库、MCP 服务器与技能包）和 Model（配置平台所用 LLM 及凭据）。全部以 ax.io/v1alpha1 YAML 清单表达，CLI 采用 kubectl 风格命令，支持 suspend/resume 断点续跑与 ax ssh 进入运行中任务。依赖 Kubernetes 集群、Go、kubectl、ko 与容器镜像仓库。

- Task/Workspace/Model 三原语的声明式 YAML 清单（ax.io/v1alpha1）
- ax suspend/ax resume 支持暂停后从原状态恢复
- kubectl 风格 CLI，跟随 kubectx 上下文切换集群
- 基于 Agent Substrate 的沙箱执行，带 CPU/内存限制

> L11: AX is a high-throughput, declarative orchestrator to run billions of autonomous agent workloads in a cluster. It runs on
> L30: Agents are a new kind of workload. They are neither stateless microservices nor run-to-completion batch jobs. They accum
> L34: |Run untrusted agent code in an isolated sandbox with CPU/memory limits|**`Task`**|

## apache/tvm（⭐13842，confidence: high）

**面向 ML 开发者的开源机器学习编译框架**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

Apache TVM 是开源机器学习编译框架，采用 Python-first 开发方式，支持对编译流水线的快速自定义，并将模型部署为最小可部署模块。当前设计以 TensorIR 作为张量级表示、Relax 作为图级表示，可联合优化计算图、张量程序与库；定位为构建面向 LLM 等领域的 Python-first 垂直编译器的基础设施。采用 Apache committer 社区治理模式，源自深度学习编译研究项目，受 Halide、Loopy、Theano 影响。安装教程见其文档站点。

- TensorIR（张量级）与 Relax（图级）跨层表示设计
- Python-first 变换，多数转换可用 Python 自定义
- 通用部署，将模型编译为最小可部署模块
- 定位为构建 LLM 等领域垂直编译器的基础设施

> L7: Apache TVM is an open machine learning compilation framework,
> L39: and Relax as the graph-level representation and Python-first transformations.
> L43: infra for building Python-first vertical compilers for domains, such as LLMs.

## QwenLM/Qwen3-TTS（⭐13832，confidence: high）

**开发者用的开源 TTS 模型系列：语音克隆、音色设计与流式生成**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=local-ok · hardware=— · install_friction=low · maturity=research`

阿里通义 Qwen 团队发布的 TTS 模型系列（0.6B/1.7B），基于自研 Qwen3-TTS-Tokenizer-12Hz 与离散多码本 LM 架构，覆盖 10 种语言及多种方言音色。提供三种模型形态：CustomVoice（9 种预置音色加指令风格控制）、VoiceDesign（自然语言描述设计音色）、Base（3 秒参考音频快速克隆，可微调）。单模型同时支持流式与非流式生成，README 称端到端首包延迟可低至 97ms。通过 PyPI 的 qwen-tts 包安装，也可用 vLLM 加载，并提供本地 Web UI demo（Base 模型部署建议 HTTPS 以启用浏览器麦克风）。

- 3 秒参考音频快速语音克隆（Base 模型），支持微调
- 自然语言指令驱动的音色设计与音色/情感/韵律控制
- 单模型流式与非流式生成，双轨混合流式架构
- 覆盖中英日韩德法俄葡西意 10 种语言及多个方言音色

> L7: We release **Qwen3-TTS**, a series of powerful speech generation capabilities developed by Qwen, offering comprehensive 
> L17: Qwen3-TTS covers 10 major languages (Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish, a
> L55: The easiest way to quickly use Qwen3-TTS is to install the `qwen-tts` Python package from PyPI. This will pull in the re

## nmap/nmap（⭐13802，confidence: mid）

**网络扫描与主机发现工具，供网络管理员使用**

`ai_role=ai-enhanced · license_risk=dual · deploy=— · model_dep=— · hardware=— · install_friction=medium · maturity=—`

GitHub 上的 Nmap 官方 SVN 镜像仓库。Nmap 是网络扫描工具（Network Mapper），提供主机发现、端口扫描等网络探测功能，并附带图形界面前端 Zenmap。README 说明安装方式为源码编译（configure/make/make install），Windows、macOS 与 Linux（RPM）的二进制安装包从 Nmap.org 获取，完整文档在 Nmap.org 网站。采用基于 GPLv2 但与其不兼容的自定义许可证，终端用户可免费使用，企业再分发需商业许可。

- 提供源码编译安装（./configure && make && make install）
- Windows/macOS/Linux 提供 Nmap.org 官方二进制安装包
- 内置 Zenmap 图形界面前端
- 自定义许可证：终端用户免费，企业再分发需商业许可

> L19: Installing
> L30: Nmap has a lot of features, but getting started is as easy as running `nmap

## BasedHardware/omi（⭐13756，confidence: high）

**记录屏幕与对话并生成摘要行动项的 AI 可穿戴伴侣应用**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

开源的 AI 记录工具：捕获屏幕画面与对话，实时转写、生成摘要与行动项，并提供带有完整记忆的 AI 聊天。覆盖桌面、手机与可穿戴设备三种形态，macOS 应用从源码构建并连接云端后端，Windows 由 Node.js 从源码运行，移动端提供 App Store 与 Google Play 安装。项目包含多个组件：Swift 桌面应用、Flutter 移动应用、Python/FastAPI 后端、nRF/Zephyr 固件及 ESP32-S3 的 Omi Glass 硬件，并提供 REST API 与多语言设备 SDK。

- 实时转写屏幕与对话，生成摘要与行动项
- 支持桌面、手机与可穿戴设备多形态
- 提供 REST API、MCP Server 及 Python/Swift/RN 设备 SDK
- 开源可穿戴硬件（Omi 项链与 Omi Glass）设计公开

> L5: Omi captures your screen and conversations, transcribes in real-time, generates summaries and action items, and gives yo
> L95: |Component|Path|Stack|
> L137: ## Omi Hardware

## Data-Centric-AI-Community/fg-data-profiling（⭐13727，confidence: high）

**一行代码生成 DataFrame 数据质量剖析与 EDA 报告**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

ydata-profiling 更名后的 Python 包，为 Pandas 与 Spark DataFrame 提供一行式探索性数据分析：类型推断、缺失/偏斜等质量警告、单变量与多变量统计、时间序列与文本分析、文件与图像元信息、数据集对比，报告可导出为 HTML/JSON 或 Jupyter widget。支持 pip/conda/源码安装与 CLI 处理 CSV。需 Python 3，报告渲染需现代浏览器；数据库级剖析引导至 YData Fabric 商业产品。

- 一行代码生成剖析报告，支持 HTML/JSON/Jupyter widget 导出
- 支持 Pandas 与 Spark（pyspark extra）处理大规模数据
- 覆盖时间序列、文本（Unicode）、文件与图像分析
- 提供 CLI 直接处理 CSV 文件

> L25: `fg-data-profiling` primary goal is to provide a one-line Exploratory Data Analysis (EDA) experience in a consistent and
> L93: - **Type inference**: automatic detection of columns' data types (*Categorical*, *Numerical*, *Date*, etc.)
> L111: - Want to scale? Check the latest release with ⭐⚡Spark support!

## Lightning-AI/litgpt（⭐13713，confidence: high）

**给开发者用的 LLM 预训练/微调/部署全流程库**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

以从零实现方式提供 20+ 开源 LLM（Llama、Qwen、Phi、Gemma、Mistral 等）的 PyTorch 库，通过统一 CLI 提供下载、chat、finetune、pretrain、continued pretraining、evaluate、serve 等工作流，并附 YAML 训练配置。支持 LoRA/QLoRA/Adapter 等参数高效微调、Flash Attention、FSDP 多卡与 TPU、4/8/16 位量化与权重格式导出；模型下载可能需要额外访问令牌。Apache 2.0 许可，pip 安装或从源码运行，由 Lightning AI 维护。

- 统一 CLI 覆盖下载/chat/finetune/pretrain/evaluate/serve 工作流
- 支持 LoRA、QLoRA、Adapter 与 Adapter v2 参数高效微调
- Flash Attention v2、FSDP 多 GPU、TPU/XLA 支持
- 4-bit/8-bit 量化降低显存需求

> L3: **20+ high-performance LLMs with recipes to pretrain, finetune, and deploy at scale.**
> L181: # litgpt [action] [model]
> L345: ✅ State-of-the-art optimizations: Flash Attention v2, multi-GPU support via fully-sharded data parallelism, optional CPU

## MiniMax-AI/skills（⭐13712，confidence: high）

**为 AI 编程 agent 提供前端/全栈/移动端开发技能包**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=medium · maturity=idea`

MiniMax 维护的 AI 编程 agent 技能集合，提供 16 个技能，覆盖前端、全栈、Android/iOS 原生、Flutter、React Native 与 GLSL shader 开发，另含 PDF/PPTX/XLSX/DOCX 文档生成及音乐、视频、图像等多模态生成技能（部分依赖 MiniMax API）。安装方式为通过 Claude Code 插件市场安装，或以 git clone 后软链方式接入 Cursor、Codex、OpenCode；VS Code 无独立扩展，需在集成终端运行支持的 CLI 工具。项目处于 Beta 阶段，接口与配置格式可能变动。

- 16 个技能覆盖前端、全栈、Android/iOS、Flutter、React Native、shader 开发
- 部分技能通过 MiniMax API 调用图像/视频/音频/TTS 生成能力
- 支持 Claude Code、Cursor、Codex、OpenCode 四种 agent 工具接入
- 文档生成技能覆盖 PDF、PPTX、XLSX、DOCX 四种格式

> L7: Development skills for AI coding agents. Plug into your favorite AI coding tool and get structured, production-quality g
> L33: ### Claude Code
> L43: git clone https://github.com/MiniMax-AI/skills.git ~/.cursor/minimax-skills

## XiaomiMiMo/MiMo-Code（⭐13677，confidence: high）

**面向开发者的终端原生 AI 编码助手，带持久记忆与多 Agent**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=medium · maturity=—`

终端（TUI）内运行的 AI 编码助手：读写代码、执行命令、管理 Git，并通过 SQLite FTS5 驱动的跨会话持久记忆（项目记忆、会话检查点、任务日志）保持对项目的理解。内置 build/plan 双 Agent、子 Agent 并行、目标停止条件判定、JavaScript 工作流（deep-research、fact-check 等 3 个内置）与技能系统（arxiv、pdf、pptx 等内置技能）。可通过 OAuth 或 API key 连接多家 LLM 提供商，另可迁移 Claude Code 认证；附带以 MiMo Code 为核心引擎的桌面版。安装提供 macOS/Linux 一行脚本；macOS 不支持自带 Terminal.app。

- SQLite FTS5 跨会话持久记忆，会话恢复自动注入上下文
- 多 Agent 与子 Agent 并行，/goal 独立裁判模型判定停止条件
- JavaScript 编写的确定性工作流 + BM25 技能检索系统
- 上下文预算管理与按模型的 /context-limit 压缩点调节

> L11: MiMoCode is a terminal-native AI coding assistant. It can read and write code, run commands, manage Git, and use a persi
> L29: MiMoCode supports connecting to any mainstream LLM provider API.
> L19: Xiaomi MiMo Desktop is built for real-world work: one conversation can handle office work, design, coding, and multimoda

## Orchestra-Research/AI-Research-SKILLs（⭐13634，confidence: high）

**面向 AI 研究者的 98 项 agent 技能库**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

由 Orchestra Research 维护的开源技能库，收录 98 个覆盖 23 个类别的 AI 研究与工程技能，供 Claude Code、Gemini CLI、Cursor 等编码 agent 安装使用。技能覆盖自动研究编排（autoresearch 双循环架构）、模型架构、微调、后训练、分布式训练、推理、评测、RAG、多模态等，内容来自官方仓库与 GitHub issue。安装方式为 npx 交互式安装器（自动检测已装 agent 并以符号链接部署）或 Claude Code 插件市场。以 MIT 许可发布。

- 98 个技能覆盖 23 个类别，含 autoresearch 双循环编排层
- npx 安装器自动检测已装编码 agent 并以符号链接部署到 ~/.orchestra/skills/
- 支持 Claude Code 插件市场安装
- 技能内容包含代码示例、排错指南与工作流文档

> L33: We enable AI agents to **autonomously conduct AI research** — from literature survey and idea generation through experim
> L46:  - End-to-End Coverage - 98 skills spanning the full AI research lifecycle, from ideation and literature survey to exper
> L71: - **Auto-detects** your installed coding agents (Claude Code, Hermes Agent, OpenCode, Qoder, Cursor, Gemini CLI, etc.)

## xszyou/Fay（⭐13576，confidence: high）

**为数字人与大语言模型连通业务系统的 agent 框架**

`ai_role=ai-native · license_risk=viral · deploy=library · model_dep=locked-api · hardware=— · install_friction=medium · maturity=—`

Fay 数字人框架向上适配各类数字人模型技术（2.5d、3d、移动、pc、网页），向下接入 openai 兼容接口与 deepseek 等大语言模型，并可更换 TTS、ASR 模型，为单片机、app、网站等终端提供数字人应用接口。功能包含全时流式、多用户多路并发、自动播报模式（虚拟教师/主播/新闻播报）、自定义知识库与人设、唤醒打断对话、MCP 工具管理与 agent 自主决策工具调用、仿生记忆等。源码启动需 Python 3.12，支持 Windows/macOS/Ubuntu。

- 支持任意终端接入：单片机、app、网站、大屏、三方业务系统
- 支持多用户多路并发与全时流式
- 提供文字/语音交互、数字人驱动、自动播报、意图等接口
- 支持 MCP 工具管理（sse、studio）与 agent 自主决策工具调用

> L7: 我们致力于思考面向终端的数字人落地应用，并通过完整代码把思考结果呈现给大家。Fay数字人框架，向上适配各种数字人模型技术，向下接入各式大语言模型，并且便于更换诸如TTS、ASR等模型，为单片机、app、网站提供全面的数字人应用接口。
> L16: - 自由匹配数字人模型、大语言模型（openai 兼容接口）、ASR、TTS模型

## huggingface/speech-to-speech（⭐13491，confidence: high）

**用开源模型在本机搭建低延迟语音对话 agent 的框架**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

以可插拔级联管道（Silero VAD → Parakeet TDT → Qwen3.5-4B → Qwen3-TTS）在本地运行语音对话，无 API key、无云端依赖；服务端实现 OpenAI Realtime 协议（WebSocket/WebRTC），为 OpenAI Realtime API 构建的应用可指向本机服务器。各阶段提供多种可替换后端，经 CLI 标志选择，支持工具调用、流式说话人分离与可视化口型输出；并作为 Reachy Mini 机器人的对话后端运行。

- 四级级联管道（VAD/STT/LLM/TTS），每级均有多个可互换后端
- 服务端实现 OpenAI Realtime 协议，兼容 OpenAI Realtime 客户端与 Agents SDK、LiveKit Agents
- 默认本地模型，首次下载后可完全离线运行
- 提供工具调用扩展与可选 viseme/说话人分离组件

> L11: A low-latency voice agent built from open models that **runs entirely on your computer**. One command starts a conversat
> L13: The default pipeline is **Silero VAD → Parakeet TDT → Qwen3.5-4B → Qwen3-TTS**, and every stage is swappable. The server
> L76: Every stage has multiple interchangeable backends, selected via CLI flags. The code is designed for easy modification, w

## puckeditor/puck（⭐13484，confidence: high）

**React 开发者的可视化拖拽页面编辑器**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=—`

Puck 是一个模块化的 React 可视化编辑器，本身以 React 组件形式提供，可在自有应用中嵌入并基于自己的 React 组件构建拖拽式编辑体验，兼容 Next.js 等环境，数据由使用者自持、无供应商锁定。采用 MIT 许可，可用于内部系统与商业应用。通过 npm 安装 @puckeditor/core，或用 create-puck-app 脚手架生成预配置应用，官方提供 Next.js 与 React Router v7 两种 recipe，另设文档、Demo、Discord 社区与付费咨询渠道。

- 以 React 组件形式嵌入自有应用，支持自定义拖拽体验
- 兼容 Next.js、React Router 等 React 环境
- MIT 许可，可用于商业应用
- create-puck-app 提供预配置应用模板

> L15: Puck is a modular, open-source visual editor for React.js. You can use Puck to build custom drag-and-drop experiences wi
> L17: Because Puck is just a React component, it plays well with all React.js environments, including Next.js. You own your da
> L19: Puck is also licensed under MIT, making it suitable for both internal systems and commercial applications.

## EverMind-AI/EverOS（⭐13464，confidence: high）

**给 AI agent 的本地优先可携带记忆层**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=locked-api · hardware=— · install_friction=low · maturity=—`

Python 库与本地优先的 agent 记忆运行时：将对话、文件与 agent 轨迹存为可读 Markdown，配合本地 SQLite 与 LanceDB 索引实现检索与离线反思（合并片段、精炼画像与技能）。支持按 user_id/agent_id/app_id/project_id/session_id 正交检索，提供本地服务器与 /api/v2 端点；一个 OpenRouter key 即可运行核心流程，embedding/rerank 为可选配置；Office 文档解析需系统安装 LibreOffice。

- Markdown 为事实源，可用 Git 版本化并直接编辑，级联 watcher 同步索引
- 本地三件套 Markdown+SQLite+LanceDB，无需 MongoDB/Elasticsearch/Redis
- 分层配置：[llm] 基础流程，[embedding]/[rerank]/[multimodal] 逐步解锁混合检索、反思与多模态摄取
- 提供 MCP Server（uvx everos-mcp）接入 Claude Code、Codex、Cursor 等编码助手

> L16: EverOS is a Python library and local-first memory runtime for agents and
> L19: trajectories as readable Markdown, then syncs local SQLite and LanceDB indexes
> L67: > One OpenRouter API key is enough to start EverOS, write durable memories,

## doocs/md（⭐13438，confidence: high）

**给公众号创作者的微信 Markdown 排版编辑器**

`ai_role=ai-enhanced · license_risk=viral · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

将 Markdown 即时渲染为微信图文的编辑器，减少公众号排版调整工作。功能覆盖标准 Markdown、KaTeX 数学公式、Mermaid/PlantUML 图表、代码高亮主题、本地草稿管理与内容导出导入；支持 13 类图床上传（GitHub、阿里云、腾讯云、S3 协议等）；集成 DeepSeek、OpenAI、通义千问等模型辅助内容创作。在线版可直接使用，另提供 npm CLI 与 Docker 私有化部署方式。

- Markdown 即时渲染为微信图文，支持 KaTeX、Mermaid、PlantUML、Ruby 注音
- 13 种图床上传选项（GitHub、阿里云、腾讯云、MinIO、S3、Cloudflare R2 等）
- 集成 DeepSeek、OpenAI、通义千问、腾讯混元、火山方舟等模型辅助创作
- 提供在线版、npm CLI、Docker 三种使用与部署方式

> L11: **Markdown 文档自动即时渲染为微信图文**，让你不再为公众号排版发愁。只需掌握基本的 Markdown 语法，即可生成样式简洁、美观大方的微信图文。
> L37: - 集成主流 AI 模型（DeepSeek、OpenAI、通义千问、腾讯混元、火山方舟、302.AI 等），辅助内容创作
> L96: docker run -d -p 8080:80 doocs/md:latest

## The-PR-Agent/pr-agent（⭐13426，confidence: high）

**面向开发团队的 AI 代码审查 agent，自动审查 PR**

`ai_role=ai-native · license_risk=permissive · deploy=desktop · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

PR-Agent 是开源的 AI 代码审查 agent，已在 GitHub 上由 Qodo 捐赠给开源社区，现为社区维护项目，与 Qodo 商业产品相区分。核心工具包括 /describe、/review、/improve、/ask，以 PR 评论或 CLI 方式触发，每个工具使用单次 LLM 调用（约 30 秒）。支持 GitHub、GitLab、BitBucket、Azure DevOps、Gitea 平台，通过 PR Compression 策略处理大小 PR，基于 JSON 的提示词可经配置文件自定义。部署途径含 GitHub Action、CLI、Docker、自托管 webhook。

- /review、/improve、/describe、/ask 等工具以 PR 评论或 CLI 方式运行
- PR Compression 策略处理任意规模的 PR
- JSON 提示词经配置文件自定义审查类别与行为
- 支持 GitHub/GitLab/BitBucket/Azure DevOps/Gitea 与多种部署方式

> L9:  This repository contains the open-source PR Agent Project.
> L12: PR-Agent is an open-source, AI-powered code review agent and a community-maintained legacy project of Qodo. It is distin
> L72: - **AI Models**: OpenAI GPT, Anthropic Claude, Google Gemini, DeepSeek, Mistral, and any other model reachable through L

## NVIDIA/TensorRT（⭐13410，confidence: high）

**面向开发者的 NVIDIA GPU 深度学习推理 SDK 开源组件仓库**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

本仓库包含 NVIDIA TensorRT 的开源组件（OSS）：TensorRT 插件、ONNX 解析器的源码，以及演示平台用法与能力的示例应用。这些开源组件是 TensorRT GA 发布版本的子集，含部分扩展与修复。仓库提供预编译 Python 包的 pip 安装途径，也可通过 Docker 构建容器或本机 CMake 从源码构建，支持 x86-64 与 aarch64（含 Jetson、DriveOS 交叉编译）目标。企业支持通过 NVIDIA AI Enterprise 提供。

- 包含 TensorRT 插件与 ONNX 解析器源码及示例应用
- 提供 pip install tensorrt 预编译 Python 包安装途径
- 支持 Docker 构建容器与本机 CMake 源码构建，覆盖 x86-64/aarch64 与 Jetson、DriveOS、QNX 交叉编译
- 提供与编码代理（coding agent）配合使用的 TensorRT 使用与基准测试技能

> L16: This repository contains the Open Source Software (OSS) components of NVIDIA TensorRT. It includes the sources for Tenso
> L34: We provide the TensorRT Python package for an easy installation. \
> L56: - CUDA

## zoicware/RemoveWindowsAI（⭐13377，confidence: high）

**给 Windows 11 用户移除 Copilot、Recall 等 AI 组件的 PowerShell 脚本**

`ai_role=ai-ecosystem · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

一个 PowerShell 脚本，用于移除/禁用 Windows 11 中的 AI 组件：禁用 Copilot、Recall、语音访问、Office/Photos/画图/记事本等应用内的 AI 功能，删除 Appx 与 CBS 中的 AI 包，并通过自定义 Windows Update 包阻止 AI 包重装；支持安装经典版应用替代，提供 UI 启动、命令行参数、备份/还原模式。要求 Windows PowerShell 5.1（PowerShell 7 不支持），管理员权限运行，部分杀毒软件可能误报。

- 禁用 Copilot、Recall、Voice Access、Defender AI 等多项系统 AI 组件
- 删除含 Nonremovable 标记的 AI Appx 包与 CBS 隐藏包，并用自定义更新包阻止重装
- 支持 UI 启动与非交互式命令行参数、备份/还原模式
- 可安装 Notepad/Paint/截图工具/照片查看器的经典版本

> L3: In Windows 11 22H2 Microsoft began adding AI features like Copilot and Recall. Since then, additional AI driven componen
> L65:  > Running the script with PowerShell 7 is no longer supported and it WILL cause issues, to avoid this ensure you are ru
> L70:  & ([scriptblock]::Create((irm "https://raw.githubusercontent.com/zoicware/RemoveWindowsAI/main/RemoveWindowsAi.ps1")))

## cloudwego/eino（⭐13331，confidence: high）

**Go 语言的 LLM/AI 应用开发框架**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

Eino 是面向 Golang 的 LLM 应用开发框架，设计上参照 LangChain、Google ADK 等开源框架并遵循 Go 语言惯例。核心提供：可复用组件抽象（ChatModel、Tool、Retriever、ChatTemplate 等，官方实现含 OpenAI、Ollama 等）、Agent 开发工具包 ADK（工具调用、多 Agent 协作、人机协同的中断/恢复、编排为图与工作流）、全链路流式处理与回调切面（日志/追踪/指标注入）。框架由本仓库与 EinoExt、Eino Devops、EinoExamples 四部分组成，依赖 Go 1.18+，采用 Apache-2.0 许可。

- 组件抽象带官方实现（OpenAI、Claude、Gemini、Ark、Ollama、Elasticsearch 等）
- ADK 支持工具调用、多 Agent 协作与人机协同的中断/恢复
- compose 将组件编排为图/工作流，可作为工具暴露给 Agent
- 编排全程自动处理流式拼接、合并与复制

> L17: **Eino['aino]** is an LLM application development framework in Golang. It draws from LangChain, Google ADK, and other op
> L20: - **Components**: reusable building blocks like `ChatModel`, `Tool`, `Retriever`, and `ChatTemplate`, with official impl
> L21: - **Agent Development Kit (ADK)**: build AI agents with tool use, multi-agent coordination, context management, interrup

## YaoFANGUK/video-subtitle-remover（⭐13330，confidence: high）

**给需要去除视频硬字幕/文本水印的用户，本地AI修复填充**

`ai_role=ai-enhanced · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

基于AI的视频/图片硬字幕与文本水印去除工具：对字幕区域进行填充（非相邻像素填充），以无损分辨率输出去除后的文件。支持自定义字幕位置或全视频自动去除所有文本，支持图片批量去水印。内置 GUI 与 CLI 两种使用方式，去除算法含 STTN、LAMA、ProPainter 三种可配置模式，模型可通过 backend/tools/train 自行训练替换。本地运行，无需申请第三方 API。Windows 提供多个预构建包，也可源码安装。

- 无损分辨率去除硬字幕/文本水印，本地运行无需第三方 API
- 三种填充算法可选（STTN/LAMA/ProPainter），参数可调
- 支持 CUDA、DirectML、CPU、macOS Apple Silicon 四种运行模式
- 提供 GUI、CLI、Docker 三种使用方式

> L15: Video-subtitle-remover (VSR) 是一款基于AI技术，将视频中的硬字幕去除的软件。
> L115: 本项目支持 CUDA (NVIDIA显卡加速)、CPU (无 GPU)、 DirectML (AMD、Intel等GPU/APU加速) 和 macOS (Apple Silicon) 四种运行模式。
> L19: - 提取原视频字幕，可配合：video-subtitle-extractor (VSE)

## dair-ai/AI-Papers-of-the-Week（⭐13281，confidence: high）

**面向 ML 从业者的每周 AI 论文精选清单**

`ai_role=ai-knowledge · license_risk=none · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

DAIR.AI 维护的每周 AI 论文精选仓库：按周汇总当周值得关注的 AI/ML 论文链接，列表自 2023 年 1 月起持续更新至 2026 年，按年份分组归档；另有 newsletter 订阅渠道将每周清单发送至邮箱，并通过 Twitter 与 Discord 进行发布和社区交流。仓库本身为索引型内容，不包含安装或运行步骤。

- 按周归档的 AI 论文清单（2023 年至今，按年份分组）
- 提供 newsletter 邮件订阅渠道
- 配套 Twitter 与 Discord 发布/交流渠道

> L3: Subscribe to our newsletter to get a weekly list of top AI papers in your inbox.
> L5: At DAIR.AI we ❤️ reading AI papers so we've created this repo to highlight the top AI papers of every week.
> L7: Here is the weekly series:

## langchain4j/langchain4j（⭐13258，confidence: high）

**给 JVM/Java 开发者的 LLM 应用开发库**

`ai_role=ai-native · license_risk=permissive · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=idea`

LangChain4j 是一个面向 JVM 的开源 Java 库，目标是简化在 Java 应用中集成 LLM 的过程。它提供统一 API 屏蔽各 LLM 提供商与向量数据库的专有接口，支持在 20+ LLM 提供商与 30+ 嵌入存储之间切换而无需重写代码。工具箱覆盖提示词模板、聊天记忆管理、函数调用，直至 Agents 与 RAG 等高层模式，每个抽象都带接口与多种实现。该库按 Java 惯例从零设计（类型安全、POJO、注解、依赖注入），与 Quarkus、Spring Boot、Helidon、Micronaut 一级集成，与 Python 版 LangChain 的 API 与发布周期相互独立。

- 统一 API 覆盖 20+ LLM 提供商与 30+ 嵌入存储，可切换实现
- 工具箱从提示词模板、聊天记忆、函数调用到 Agents 与 RAG
- 按 Java 惯例原生设计，一级集成 Quarkus/Spring Boot/Helidon/Micronaut
- MCP 相关工具调用支持

> L16: The goal of LangChain4j is to simplify integrating LLMs into Java applications.
> L23:  LangChain4j currently supports 20+ popular LLM providers
> L43: type safety, POJOs, annotations, interfaces, dependency injection, fluent APIs, and first-class integrations with Quarku

## modelscope/DiffSynth-Studio（⭐13256，confidence: high）

**为开发者提供的开源 Diffusion 模型推理与训练引擎**

`ai_role=ai-enhanced · license_risk=permissive · deploy=library · model_dep=— · hardware=— · install_friction=low · maturity=research`

由 ModelScope 社区团队维护的 Diffusion 模型引擎，集成图像生成、视频生成、音频生成与图像质量评估类开源模型。框架提供跨磁盘/内存/显存的动态参数调度，使低显存消费级 GPU 可运行大模型推理；支持 NF4、INT8 等量化以降低推理与 LoRA 训练的显存需求；推理支持的模型基本均可训练，训练过程可拆分为两阶段。相关派生项目包括 ComfyUI 节点包与 LoRA 训练 WebUI。README 说明开发人力有限，旧版本功能不再维护。

- 集成图像/视频/音频生成与图像质量评估模型
- 跨磁盘、内存、显存的动态参数调度，低显存 GPU 可推理大模型
- NF4/INT8 等量化后端（含自研 EntroPack 压缩库）
- 提供 Agent Skills 用于自动化模型集成流程

> L16: Welcome to the magical world of Diffusion models! DiffSynth-Studio is an open-source Diffusion model engine developed an
> L20: * Model Support: The framework integrates mainstream open-source Diffusion models, covering image generation, video gene
> L21: * VRAM Management: Dynamically schedules model parameters across disk, memory, and VRAM, allowing consumer-grade GPUs wi

## halfrost/Halfrost-Field（⭐13248，confidence: high）

**开发者阅读开源源码与协议的技术文章集**

`ai_role=ai-knowledge · license_risk=viral · deploy=— · model_dep=— · hardware=— · install_friction=low · maturity=—`

个人技术笔记仓库，记录作者阅读开源项目源码后的分析与心得，内容按 LLM、Go、机器学习、JavaScript、网络协议等主题以目录表形式组织，每条对应具体项目版本与系列文章。受众为希望深入理解框架源码与底层协议的开发者。仓库持续更新，支持中英双语，接受 PR/issue 勘误，文章以 Creative Commons BY 4.0 许可转载。

- LLM 专题收录 vLLM v1 源码系列解析（调度器、KV Cache、进程架构等）
- 覆盖 Go 内部实现、Google S2 空间索引、TLS 1.3/HTTP2/QUIC 等 RFC 级协议文章
- 中英双语内容，接受社区 PR 与 issue 勘误

> L11: People often say that reading the source code of open-source frameworks can significantly improve one’s skills, so I hav
> L15: # 🔥 LLM

## Portkey-AI/gateway（⭐13210，confidence: mid）

**为开发者提供统一的 AI 网关，路由 1600+ 模型并集成 guardrails**

`ai_role=ai-native · license_risk=permissive · deploy=library · model_dep=local-ok · hardware=— · install_friction=low · maturity=—`

开源 AI Gateway，通过单一 API 将请求路由到 1600+ 语言、视觉、音频与图像模型。核心机制包括自动重试与 fallback、负载均衡与条件路由、40+ 预置 guardrails、虚拟密钥管理与用量分析；另提供 MCP Gateway 作为组织级 MCP 服务器的集中控制平面（认证、访问控制、可观测性）。通过 npx 本地运行，支持 Docker、Cloudflare 等多种部署方式；部分功能（语义缓存、prompt 管理等）仅 hosted/企业版提供。

- 单一 API 路由 1600+ 多模态模型，支持 45+ provider
- fallback、自动重试、负载均衡等可靠路由机制
- 40+ 预置 guardrails 验证 LLM 输入输出
- MCP Gateway 提供集中认证、访问控制与调用日志

> L24: The **AI Gateway** is designed for fast, reliable & secure routing to 1600+ language, vision, audio, and image models. I
> L37: - Manage MCP servers with enterprise auth & observability using **MCP Gateway**

## InsForge/InsForge（⭐13136，confidence: high）

**为编码 Agent 提供数据库/认证/存储/托管的一体化后端平台**

`ai_role=ai-native · license_risk=permissive · deploy=self-host · model_dep=— · hardware=— · install_friction=low · maturity=—`

开源后端平台，将数据库（Postgres）、用户认证、S3 兼容存储、Model Gateway、边缘函数、站点部署等能力打包为一套可自托管的服务。编码 Agent 通过 MCP Server（自托管与云）或 CLI + Skills（仅云）两种接口调用其操作：读取后端 schema、元数据与运行日志，执行数据库迁移、部署边缘函数、创建存储桶、配置认证提供方等。自托管经 Docker Compose 完成，要求 Docker 与 Compose v2，默认本地文件系统存储，可挂接 S3 兼容存储后端。

- 通过 MCP Server 将后端操作暴露为 Agent 可调用工具
- Postgres 数据库、认证、S3 兼容存储、边缘函数、站点部署一体化
- Model Gateway 提供 OpenAI 兼容 API 跨多个 LLM 提供方
- 支持 Docker Compose 自托管与 Railway/Zeabur/Sealos 等一键部署

> L32: The all-in-one, open-source backend platform for agentic coding. InsForge gives your coding agent database, auth, storag
> L40: - **MCP Server** (self-hosted and cloud): exposes InsForge's operations as tools any MCP-compatible agent can call.
> L78: Prerequisites: Docker with Compose v2.
