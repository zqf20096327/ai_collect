<h1 align="center">Awesome AI Agent Stack</h1>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="https://tayyabimam1.github.io/awesome-ai-agent-stack/"><img src="https://img.shields.io/badge/website-live-0969da?style=flat" alt="Website"></a>
  <a href="https://github.com/tayyabimam1/awesome-ai-agent-stack/stargazers"><img src="https://img.shields.io/github/stars/tayyabimam1/awesome-ai-agent-stack?style=flat" alt="Stars"></a>
  <a href="https://github.com/tayyabimam1/awesome-ai-agent-stack/commits/main"><img src="https://img.shields.io/github/last-commit/tayyabimam1/awesome-ai-agent-stack?style=flat" alt="Last commit"></a>
</p>

<p align="center"><em>A curated, layer-by-layer map of the tools I actually use to build AI agents — from the coding agent in your terminal down to the model serving the tokens.</em></p>

<p align="center">
  <a href="https://tayyabimam1.github.io/awesome-ai-agent-stack/"><strong>Browse the website</strong></a> ·
  <a href="https://github.com/tayyabimam1/awesome-ai-agent-stack/edit/main/README.md">Suggest a tool</a>
</p>

<p align="center">
  <a href="https://tayyabimam1.github.io/awesome-ai-agent-stack/"><img src=".github/site-preview.jpg" alt="The Awesome AI Agent Stack website: 3,000+ tools in 29 categories, ranked by GitHub stars" width="860"></a>
</p>

**3,000+ tools across 29 categories, ranked by GitHub stars.** Each section is split into sub-groups by what the tools do. Every entry passes a mechanical bar: real, public, not archived, and actively maintained (pushed in the last 12 months); new additions also need 1,000+ stars. Every link is re-checked against the GitHub API, and projects under 10,000 stars that stop being maintained are pruned. Organized as a **stack** so you can find the right tool for each layer of an agent system.

**On the website** you can search every tool, sort any category by stars, and see the most-starred projects in each layer. It rebuilds from this README on every change.

> If this list saves you time, **[give it a star](https://github.com/tayyabimam1/awesome-ai-agent-stack/stargazers)** — it helps other builders find it.

**Weekly maintenance:** Star this repository to follow weekly audits, new AI-agent tools, and removals of dead or stale projects. **[Suggest a tool](https://github.com/tayyabimam1/awesome-ai-agent-stack/discussions/categories/ideas)** or **[report a stale link](https://github.com/tayyabimam1/awesome-ai-agent-stack/discussions/categories/q-a)** in Discussions.

```
┌──────────────────────────────────────────────────────────────┐
│  Coding Agents & Harnesses  →  Skills & Context Engineering  │  ← how you build
├──────────────────────────────────────────────────────────────┤
│  Agent Frameworks  →  Memory  →  RAG  →  MCP / Tools         │  ← what you build with
├──────────────────────────────────────────────────────────────┤
│  Sandboxes & Browsers  →  Document Ingestion  →  Workflows   │  ← what agents act on
├──────────────────────────────────────────────────────────────┤
│  Gateways & Routing  →  Free LLM APIs  →  Local Inference    │  ← where tokens come from
├──────────────────────────────────────────────────────────────┤
│  Evaluation, Observability & Review  →  Reference Systems    │  ← how you ship
└──────────────────────────────────────────────────────────────┘
```

## Contents

- [Coding Agents & Harnesses](#coding-agents--harnesses)
- [Skills, Plugins & Context Engineering](#skills-plugins--context-engineering)
- [Agent Frameworks & Orchestration](#agent-frameworks--orchestration)
- [Memory & Persistent Context](#memory--persistent-context)
- [RAG & Retrieval](#rag--retrieval)
- [MCP Servers & Tool Integration](#mcp-servers--tool-integration)
- [Sandboxes, Browsers & Computer Use](#sandboxes-browsers--computer-use)
- [Document Processing & Data Ingestion](#document-processing--data-ingestion)
- [Workflow Automation](#workflow-automation)
- [Model Gateways & Routing](#model-gateways--routing)
- [Free LLM APIs & Free Tiers](#free-llm-apis--free-tiers)
- [Local Models, Inference & Hardware](#local-models-inference--hardware)
- [Evaluation, Observability & Code Review](#evaluation-observability--code-review)
- [Production Architectures & Reference Systems](#production-architectures--reference-systems)
- [UI & Application Layer](#ui--application-layer)
- [Learning Path](#learning-path)
- [Voice, Speech & Audio](#voice-speech--audio)
- [Vision & Multimodal](#vision--multimodal)
- [Image, Video & Creative Generation](#image-video--creative-generation)
- [Computer Use & GUI Agents](#computer-use--gui-agents)
- [Structured Output, Guardrails & Safety](#structured-output-guardrails--safety)
- [Chat UIs & Application Layer](#chat-uis--application-layer)
- [Deployment, Serving & MLOps](#deployment-serving--mlops)
- [Data, Datasets & Synthetic Data](#data-datasets--synthetic-data)
- [Domain Agents: Finance, Healthcare, Research & More](#domain-agents-finance-healthcare-research--more)
- [Assistants, Copilots & Personal Agents](#assistants-copilots--personal-agents)
- [Interpretability, Alignment & Research](#interpretability-alignment--research)
- [Developer Tools & Utilities](#developer-tools--utilities)
- [Other Awesome Lists](#other-awesome-lists)

## Coding Agents & Harnesses

*The agent that writes the code. Pick one, learn it deeply.*

**Terminal coding agents**

- [anthropics/claude-code](https://github.com/anthropics/claude-code) - Anthropic's terminal coding agent; the reference harness most of this list is built around.
- [openai/codex](https://github.com/openai/codex) - OpenAI's lightweight terminal coding agent.
- [google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) - Gemini in the terminal with a generous free tier.
- [anomalyco/opencode](https://github.com/anomalyco/opencode) - Open-source, provider-agnostic coding agent with a polished TUI.
- [Aider-AI/aider](https://github.com/Aider-AI/aider) - Pair-programming in the terminal with git-native edits; the original open coding agent.
- [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) - Alibaba's open-source terminal coding agent with MCP support.
- [Twigpine/openclaude](https://github.com/Twigpine/openclaude) - Open Claude Code-compatible harness that runs on any provider.
- [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) - Plugin-first agent harness from DeepSeek.
- [earendil-works/pi](https://github.com/earendil-works/pi) - AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI.
- [shareAI-lab/learn-claude-code](https://github.com/shareAI-lab/learn-claude-code) - Bash is all you need - A nano claude code–like 「agent harness」, built from 0 to 1.
- [1jehuang/jcode](https://github.com/1jehuang/jcode) - Memory-efficient terminal coding agent for repo work.
- [aws/amazon-q-developer-cli](https://github.com/aws/amazon-q-developer-cli) - AWS terminal coding agent with AWS service integration.
- [build-with-groq/groq-code-cli](https://github.com/build-with-groq/groq-code-cli) - Lightweight terminal coding agent for Groq models.
- [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) - Terminal coding agent with anchored edits and subagents.
- [CodebuffAI/freebuff](https://github.com/CodebuffAI/freebuff) - Free AI coding agent for the terminal.
- [CommandCodeAI/command-code](https://github.com/CommandCodeAI/command-code) - Terminal coding agent supporting multiple model providers.
- [dhanji/g3](https://github.com/dhanji/g3) - Minimal terminal coding agent with multi-model support.
- [esengine/DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) - Terminal coding agent tuned for DeepSeek models.
- [gi-dellav/zerostack](https://github.com/gi-dellav/zerostack) - Lightweight Rust coding agent with Git worktrees and ACP.
- [github/copilot-cli](https://github.com/github/copilot-cli) - GitHub's terminal coding agent for repo tasks and commands.
- [codewhale-hq/Codewhale](https://github.com/codewhale-hq/Codewhale) - Rust terminal coding agent with MCP, worktrees, and subagents.
- [gptme/gptme](https://github.com/gptme/gptme) - Terminal agent that codes, browses, and runs autonomously.
- [Kuberwastaken/claurst](https://github.com/Kuberwastaken/claurst) - Agentic coding assistant for builders who ship.
- [letta-ai/letta-code](https://github.com/letta-ai/letta-code) - Stateful terminal coding agent with persistent memory.
- [MayDay-wpf/snow-cli](https://github.com/MayDay-wpf/snow-cli) - Terminal coding agent for OpenAI, Gemini, Claude workflows.
- [MoonshotAI/kimi-code](https://github.com/MoonshotAI/kimi-code) - Moonshot's terminal coding agent with MCP support.
- [mistralai/mistral-vibe](https://github.com/mistralai/mistral-vibe) - Mistral's terminal coding agent with planning and delegation.
- [Nano-Collective/nanocoder](https://github.com/Nano-Collective/nanocoder) - Local-first terminal coding agent with bring-your-own-model.
- [neovateai/neovate-code](https://github.com/neovateai/neovate-code) - Terminal coding agent for codegen, fixes, and headless runs.
- [solvyxtech/molt](https://github.com/solvyxtech/molt) - Coding agent refusing unproven done claims with receipts.
- [superagent-ai/grok-cli](https://github.com/superagent-ai/grok-cli) - Open-source terminal coding agent for the Grok API.
- [SWE-agent/mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent) - Minimalist terminal coding agent for SWE tasks.
- [tailcallhq/forgecode](https://github.com/tailcallhq/forgecode) - Terminal pair programmer with multi-provider model support.
- [truffle-ai/dexto](https://github.com/truffle-ai/dexto) - Terminal coding agent with local-first tool execution.
- [vinhnx/VTCode](https://github.com/vinhnx/VTCode) - Rust terminal coding agent with native sandboxing.
- [vercel-labs/fx](https://github.com/vercel-labs/fx) - Small embeddable Zig coding agent with a Unix-like CLI.
- [XiaomiMiMo/MiMo-Code](https://github.com/XiaomiMiMo/MiMo-Code) - Xiaomi's terminal coding agent with skills and worktrees.
- [xai-org/grok-build](https://github.com/xai-org/grok-build) - xAI terminal coding agent with full-screen interface.
- [vstorm-co/pydantic-deepagents](https://github.com/vstorm-co/pydantic-deepagents) - Self-hosted terminal coding assistant and Python framework for deep agents.
- [charmbracelet/crush](https://github.com/charmbracelet/crush) - Glamourous agentic coding for all.
- [stakpak/agent](https://github.com/stakpak/agent) - Terminal AI coding agent for agentic software engineering.
- [Tura-AI/tura](https://github.com/Tura-AI/tura) - Coding agent harness with terminal and editor integrations.
- [vybestack/llxprt-code](https://github.com/vybestack/llxprt-code) - Multi-provider AI coding assistant CLI for terminal workflows.
- [fuxicodex/Fuxi](https://github.com/fuxicodex/Fuxi) - FuXi is a fast, self-contained AI coding agent that lives in your terminal — edit code, run commands, and drive tools, with cost-aware routi.
- [codewhale-hq/Codewhale](https://github.com/codewhale-hq/Codewhale) - Open-source Rust agent engine and terminal client for Codewhale, with provider choice, tools, approvals and receipts.

**IDE, editor & desktop agents**

- [cline/cline](https://github.com/cline/cline) - Autonomous coding agent inside VS Code with human-in-the-loop approvals.
- [continuedev/continue](https://github.com/continuedev/continue) - Open-source coding agent.
- [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) - Open-source agentic coding platform for VS Code and JetBrains; the Roo Code successor.
- [intitni/CopilotForXcode](https://github.com/intitni/CopilotForXcode) - The first GitHub Copilot, Codeium and ChatGPT Xcode Source Editor Extension.
- [TabbyML/tabby](https://github.com/TabbyML/tabby) - Self-hosted AI coding assistant with autocomplete, chat, and RAG.
- [avante-corp/avante.nvim](https://github.com/avante-corp/avante.nvim) - Cursor-style AI coding features for Neovim.
- [baiyuscc13724-max/deepseek-harness-desktop](https://github.com/baiyuscc13724-max/deepseek-harness-desktop) - Desktop client for the DeepSeek Harness coding workbench.
- [coder/claudecode.nvim](https://github.com/coder/claudecode.nvim) - Neovim bridge making it a first-class Claude Code IDE.
- [olimorris/codecompanion.nvim](https://github.com/olimorris/codecompanion.nvim) - ACP-based AI chat and coding assistant for Neovim.
- [PawanOsman/OpenCursor](https://github.com/PawanOsman/OpenCursor) - VS Code coding agent with agentic chat and semantic search.
- [stagewise-io/stagewise](https://github.com/stagewise-io/stagewise) - Agentic IDE with code editing and app previews.
- [warpdotdev/warp](https://github.com/warpdotdev/warp) - Agentic terminal combining a modern shell with coding agents.
- [trypear/pearai-master](https://github.com/trypear/pearai-master) - Open-source AI-native code editor (PearAI).
- [winfunc/opcode](https://github.com/winfunc/opcode) - Desktop GUI for Claude Code: custom agents and sessions.
- [zed-industries/zed](https://github.com/zed-industries/zed) - High-performance editor with built-in agentic coding.
- [editor-code-assistant/eca](https://github.com/editor-code-assistant/eca) - Editor-agnostic AI pair programming server and protocol.
- [github/CopilotForXcode](https://github.com/github/CopilotForXcode) - GitHub's official Copilot coding assistant for Xcode.
- [NanmiCoder/cc-haha](https://github.com/NanmiCoder/cc-haha) - Local-first cross-platform desktop workspace for Claude Code / agents: multi-agent, Git worktrees, code diffs, skill marketplace, multi-mode.
- [zhukunpenglinyutong/desktop-cc-gui](https://github.com/zhukunpenglinyutong/desktop-cc-gui) - Multi-engine AI coding desktop client (Tauri). Claude Code, Codex, Gemini, OpenCode, DeepSeek Harness and more in one GUI.
- [CoderLuii/HolyClaude](https://github.com/CoderLuii/HolyClaude) - AI coding workstation: Claude Code + web UI + 8 AI CLIs + headless browser + 50+ tools.

**Autonomous software engineers**

- [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) - Autonomous software-development agent platform with sandboxed execution.
- [aaif-goose/goose](https://github.com/aaif-goose/goose) - Extensible open-source agent that installs, runs and tests code with any LLM.
- [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) - The project that started the autonomous-agent wave; now a platform for building agents.
- [coleam00/remote-agentic-coding-system](https://github.com/coleam00/remote-agentic-coding-system) - Run coding agents remotely with a persistent workspace.
- [ai-christianson/RA.Aid](https://github.com/ai-christianson/RA.Aid) - Autonomous dev agent that plans, edits, and validates.
- [AndyMik90/Aperant](https://github.com/AndyMik90/Aperant) - Autonomous multi-session AI coding with verification.
- [aws-samples/remote-swe-agents](https://github.com/aws-samples/remote-swe-agents) - AWS samples for running SWE agents remotely.
- [bytedance/trae-agent](https://github.com/bytedance/trae-agent) - ByteDance's software engineering agent for repo tasks.
- [ColeMurray/background-agents](https://github.com/ColeMurray/background-agents) - Self-hosted background coding system for repo tasks.
- [HKUDS/DeepCode](https://github.com/HKUDS/DeepCode) - Agentic coding system turning specs into code and sites.
- [imbue-ai/sculptor](https://github.com/imbue-ai/sculptor) - Imbue's coding agent with verification harnesses.
- [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) - Async coding agent working tasks in isolated environments.
- [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) - Self-improving coding agent for long-running tasks.
- [Pythagora-io/gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) - AI developer that plans, writes, and debugs whole apps.
- [SWE-agent/SWE-agent](https://github.com/SWE-agent/SWE-agent) - Autonomous agent that resolves real GitHub issues.
- [chaitin/MonkeyCode](https://github.com/chaitin/MonkeyCode) - AI coding platform for teams.

**General-purpose agent harnesses**

- [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) - Self-improving general-purpose agent with a large skills ecosystem.
- [openclaw/openclaw](https://github.com/openclaw/openclaw) - Cross-platform agent that operates the OS, not just the editor.
- [agentlas-ai/Agentlas-OS](https://github.com/agentlas-ai/Agentlas-OS) - Local-first OS staffing specialist agent teams per task.
- [truefoundry/trueforge](https://github.com/truefoundry/trueforge) - Open-source agent harness that turns an LLM into a working agent runtime.
- [autonomous-ai/openharness](https://github.com/autonomous-ai/openharness) - Harness to run all your coding agents across all your machines.
- [androoAGI/starnet](https://github.com/androoAGI/starnet) - Local-first desktop agent harness where agents work in a pixel-art station.
- [InsForge/InsForge](https://github.com/InsForge/InsForge) - The all-in-one, open-source backend platform for agentic coding. InsForge gives your coding agent database, auth, storage, compute, hosting,.
- [XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt) - ChatGPT thinks. Codex works. Use ChatGPT as the planning brain while keeping the Codex harness.
- [teaql/teaql-agent-kit](https://github.com/teaql/teaql-agent-kit) - A model-mediated harness for reliable agentic software development.
- [maxritter/pilot-shell](https://github.com/maxritter/pilot-shell) - Professional context and harness engineering for Claude Code and OpenAI Codex. Build production-grade software with spec-driven development,.
- [earendil-works/pi](https://github.com/earendil-works/pi) - AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI.
- [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) - 🙌 OpenHands: AI-Driven Development.
- [dohooo/helmor](https://github.com/dohooo/helmor) - Open-source local workbench for multi-agent software development.

**Multi-agent orchestration on top of coding agents**

- [stablyai/orca](https://github.com/stablyai/orca) - Agentic Development Environment for running fleets of parallel coding agents.
- [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) - Teams-first multi-agent orchestration layer for Claude Code.
- [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) - Graph-based multi-agent workflows triggered from a single prompt.
- [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) - Delegate review or tasks from Claude Code to Codex.
- [asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck) - Kanban-style TUI for running parallel coding agents.
- [AutoMaker-Org/automaker](https://github.com/AutoMaker-Org/automaker) - Autonomous coding agent orchestrator for multi-agent builds.
- [awslabs/cli-agent-orchestrator](https://github.com/awslabs/cli-agent-orchestrator) - AWS Labs harness for orchestrating CLI coding agents.
- [Charlie85270/Dorothy](https://github.com/Charlie85270/Dorothy) - TUI dashboard for parallel Claude Code sessions.
- [coder/xum](https://github.com/coder/xum) - A desktop app for isolated, parallel agentic development.
- [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) - Named tmux manager coordinating AI coding agents.
- [dagger/container-use](https://github.com/dagger/container-use) - Isolated dev environments for parallel coding agents.
- [gastownhall/gastown](https://github.com/gastownhall/gastown) - Terminal multi-agent coding orchestrator.
- [generalaction/emdash](https://github.com/generalaction/emdash) - Open-source agentic development environment for running coding agents in parallel.
- [getpaseo/paseo](https://github.com/getpaseo/paseo) - Parallel coding agent orchestrator for Claude and Codex.
- [herdrdev/herdr](https://github.com/herdrdev/herdr) - Agent-aware multiplexer for building agentic coding systems.
- [johannesjo/parallel-code](https://github.com/johannesjo/parallel-code) - Run multiple coding agents in parallel workspaces.
- [launchapp-dev/animus-cli](https://github.com/launchapp-dev/animus-cli) - Orchestrator running multi-model dev teams from YAML.
- [looptroop-ai/LoopTroop](https://github.com/looptroop-ai/LoopTroop) - Local AI coding orchestration for repo-scale work.
- [madarco/agentbox](https://github.com/madarco/agentbox) - Run coding agents in parallel sandboxed VMs.
- [mixpeek/amux](https://github.com/mixpeek/amux) - Control plane running dozens of parallel coding agents.
- [nimbalyst/nimbalyst](https://github.com/nimbalyst/nimbalyst) - Open-source visual workspace for Claude Code, Codex, and OpenCode.
- [nwiizo/ccswarm](https://github.com/nwiizo/ccswarm) - Swarm manager orchestrating Claude Code sessions in worktrees.
- [Orkas-AI/Orkas](https://github.com/Orkas-AI/Orkas) - Local-first desktop AI workforce coordinating coding agents.
- [penso/arbor](https://github.com/penso/arbor) - Multi-agent coding orchestration in the terminal.
- [proliferate-ai/proliferate](https://github.com/proliferate-ai/proliferate) - Agent IDE for Claude Code, Codex, and Gemini in parallel.
- [pungme/superagent-desktop](https://github.com/pungme/superagent-desktop) - macOS desktop giving coding agents a browser and simulator.
- [raysonmeng/agent-bridge](https://github.com/raysonmeng/agent-bridge) - Local bridge for Claude Code and Codex collaboration.
- [sahithvibudhi/vibe-tree](https://github.com/sahithvibudhi/vibe-tree) - Execute Claude Code tasks in parallel git worktrees.
- [simion/termic](https://github.com/simion/termic) - Terminal multiplexer for agent coding sessions.
- [smtg-ai/claude-squad](https://github.com/smtg-ai/claude-squad) - Manage multiple Claude Code agents from one unified TUI.
- [standardagents/dmux](https://github.com/standardagents/dmux) - tmux-based multiplexer for parallel agent sessions.
- [stravu/crystal](https://github.com/stravu/crystal) - Desktop app running parallel Claude Code sessions.
- [subsy/ralph-tui](https://github.com/subsy/ralph-tui) - TUI runner for Ralph-style autonomous coding loops.
- [superset-sh/superset](https://github.com/superset-sh/superset) - Agentic IDE orchestrating 100+ coding agents in parallel.
- [tempestai-dev/tempest](https://github.com/tempestai-dev/tempest) - Tauri desktop running CLI coding agents in parallel.
- [YoanWai/agent-manager](https://github.com/YoanWai/agent-manager) - Go TUI running coding agents side by side in tmux.
- [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) - Desktop cowork app that runs Claude Code, Codex, OpenCode and other agents.
- [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) - Ghostty-based macOS terminal with vertical tabs and notifications for coding agents.
- [openchamber/openchamber](https://github.com/openchamber/openchamber) - Agentic development environment built on the OpenCode agent.
- [alvinunreal/oh-my-opencode-slim](https://github.com/alvinunreal/oh-my-opencode-slim) - Lean multi-agent suite for OpenCode with model mixing and auto delegation.
- [darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl) - Plan-first agent framework with approval-gated execution for coding workflows.
- [codeaholicguy/ai-devkit](https://github.com/codeaholicguy/ai-devkit) - Control plane for managing and standardizing AI coding agents.
- [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) - Get 10X more out of Claude Code, Codex or any coding agent.
- [AgentsMesh/AgentsMesh](https://github.com/AgentsMesh/AgentsMesh) - AI agent workforce platform; run hundreds of coding agents across machines.
- [HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin) - Local multi-agent harness driving your Claude Code and Codex subscriptions.
- [coleam00/Archon](https://github.com/coleam00/Archon) - Open-source harness builder for AI coding agents.
- [mattpocock/sandcastle](https://github.com/mattpocock/sandcastle) - Orchestrate sandboxed coding agents in TypeScript.
- [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) - Meta-harness orchestrating Claude Code, Codex, Cursor, and custom agents.
- [openai/symphony](https://github.com/openai/symphony) - Turns project work into isolated, autonomous implementation runs.
- [OrchestratorInc/agent-orchestrator](https://github.com/OrchestratorInc/agent-orchestrator) - Run and supervise teams of coding agents from planning to merge.
- [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk) - Git worktree CLI built for running AI coding agents in parallel.
- [mvschwarz/openrig](https://github.com/mvschwarz/openrig) - Persistent teams of Claude Code, Codex and Pi agents with roles and shared context.
- [Gaurav-Gosain/tuios](https://github.com/Gaurav-Gosain/tuios) - Terminal window manager that tracks what your agents are doing.
- [zeronsh/zeron](https://github.com/zeronsh/zeron) - Native control plane for Claude Code, Codex, Cursor and other coding agents.
- [SeemSeam/claude_codex_bridge](https://github.com/SeemSeam/claude_codex_bridge) - Visible multi-agent CLI workspace for mixing Codex, Claude, Gemini, Kimi, Qwen, Cursor, Copilot, Pi, OpenCode, and other AI coding agents.
- [agent-of-empires/agent-of-empires](https://github.com/agent-of-empires/agent-of-empires) - Manage multiple Claude Code, OpenCode agents from either TUI or Web for easy access on mobile. Also supports Mistral Vibe, Codex CLI, Gemini.
- [HarnessMD/munder-difflin](https://github.com/HarnessMD/munder-difflin) - an open-source alternative to the dots, bots and muses of the world, run an office of claude code/codex like agents on your laptop, sandboxe.
- [kungfu-systems/kungfu](https://github.com/kungfu-systems/kungfu) - Your agents don’t hand off the work. Kungfu keeps the same Work moving across Codex, Claude, OpenCode, and your own execution surface.
- [the-open-engine/zeroshot](https://github.com/the-open-engine/zeroshot) - Runs coding agents as a graph: one agent implements, independent agents review, failures go to repair, and nothing ships until the checks pa.

**Remote control & session monitoring**

- [amantus-ai/vibetunnel](https://github.com/amantus-ai/vibetunnel) - Share terminal agent sessions over the web.
- [Dimillian/CodexMonitor](https://github.com/Dimillian/CodexMonitor) - macOS menu-bar monitor for Codex CLI sessions.
- [kbwo/ccmanager](https://github.com/kbwo/ccmanager) - Session manager for Claude Code with usage tracking.
- [omnara-ai/omnara](https://github.com/omnara-ai/omnara) - Remote monitoring and control for coding agents.
- [rustykuntz/clideck](https://github.com/rustykuntz/clideck) - Phone-friendly dashboard for CLI coding agents.
- [slopus/happy](https://github.com/slopus/happy) - Mobile client for monitoring Claude Code sessions.
- [soul-sol/agent-watch](https://github.com/soul-sol/agent-watch) - Stall detection for background Claude Code and Codex jobs.
- [pacifio/atlas](https://github.com/pacifio/atlas) - Source control for agents that tracks and queries changes from multiple coding agents.
- [tiann/hapi](https://github.com/tiann/hapi) - App for driving Codex, Claude Code and OpenCode sessions from anywhere.
- [backnotprop/plannotator](https://github.com/backnotprop/plannotator) - Visually annotate and review coding agent plans and diffs, and share them.
- [siteboon/claudecodeui](https://github.com/siteboon/claudecodeui) - Use Claude Code on mobile and web via CloudCLI.
- [stefanprodan/cctop](https://github.com/stefanprodan/cctop) - Live top-style monitor for Claude Code sessions.
- [tomasz-tomczyk/crit](https://github.com/tomasz-tomczyk/crit) - A feedback loop between you and your agent: review plans and diffs fast.
- [ewsun22/codex-manager](https://github.com/ewsun22/codex-manager) - Desktop control center for OpenAI Codex sessions.
- [pingdotgg/t3code](https://github.com/pingdotgg/t3code) - Mobile, web and desktop control surface for the coding agents on your machine.
- [Louis-CFM/coucou](https://github.com/Louis-CFM/coucou) - Notch companion that watches your coding agents and alerts you.
- [chenhg5/cc-connect](https://github.com/chenhg5/cc-connect) - Bridge local AI coding agents (Claude Code, Cursor, Gemini CLI, Codex) to messaging platforms (Feishu/Lark, DingTalk, Slack, Telegram, Disco.
- [eneskirca/nodeterm](https://github.com/eneskirca/nodeterm) - Node-based terminal manager for AI coding agents — tmux-backed terminals and parallel agent sessions as draggable nodes on an infinite pan/z.
- [happier-dev/happier](https://github.com/happier-dev/happier) - Web, Desktop & Mobile client and orchestrator for Codex, Claude Code, OpenCode, Pi, Cursor, Grok, Antigravity, Kimi, Augment Code, Qwen, ful.
- [AltanS/collie](https://github.com/AltanS/collie) - Herdr mobile client for iPhone and Android. A self-hosted PWA to drive Claude Code, Pi, Codex and OpenCode in Herdr, tmux or zellij from you.
- [Ataraxy-Labs/opensessions](https://github.com/Ataraxy-Labs/opensessions) - tmux sidebar for coding agents — Amp, Claude Code, Codex, OpenCode. Per-thread markers, local HTTP API, live session state.

**Account, session & proxy managers**

- [farion1231/cc-switch](https://github.com/farion1231/cc-switch) - Desktop switcher for Claude Code, Codex, OpenCode and friends.
- [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router) - Route Claude Code requests across models and providers.
- [heyhuynhgiabuu/proxypal](https://github.com/heyhuynhgiabuu/proxypal) - Expose your chat subscriptions as local OpenAI-compatible endpoints.
- [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) - Proxy Antigravity-provided Claude/Gemini models to any client.
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Hook any Claude Code request, modify responses, route custom models.
- [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) - Account manager and one-click switcher for Antigravity.

**CI & GitHub Actions**

- [anthropics/claude-code-action](https://github.com/anthropics/claude-code-action) - Official Claude Code GitHub Action for CI automation.
- [github/gh-aw](https://github.com/github/gh-aw) - GitHub Agentic Workflows for running agents in CI.
- [google-github-actions/run-gemini-cli](https://github.com/google-github-actions/run-gemini-cli) - GitHub Action running Gemini CLI in workflows.
- [openai/codex-action](https://github.com/openai/codex-action) - Official Codex GitHub Action for automated coding tasks.

**App builders**

- [dyad-sh/dyad](https://github.com/dyad-sh/dyad) - Local desktop AI app builder that iterates on full-stack code.
- [onlook-dev/onlook](https://github.com/onlook-dev/onlook) - Open-source visual editor with AI app generation.
- [Nutlope/llamacoder](https://github.com/Nutlope/llamacoder) - Open-source Claude Artifacts clone generating apps with Llama.
- [stackblitz-labs/bolt.diy](https://github.com/stackblitz-labs/bolt.diy) - Prompt, run, edit, and deploy full-stack web applications using any LLM you want!.
- [abi/screenshot-to-code](https://github.com/abi/screenshot-to-code) - Turn a screenshot into clean HTML/Tailwind/React.

**Protocols & standards**

- [agentsmd/agents.md](https://github.com/agentsmd/agents.md) - Open standard for AGENTS.md agent instructions.
- [agentclientprotocol/agent-client-protocol](https://github.com/agentclientprotocol/agent-client-protocol) - Protocol connecting editors to coding agents.
- [unstablebuild/rune](https://github.com/unstablebuild/rune) - the development environment for pros.
- [wangmiaozero/pi-harness](https://github.com/wangmiaozero/pi-harness) - Superset of the Pi coding agent with a visual workspace, run controls and agent teams.
- [michael-denyer/pstack-claude](https://github.com/michael-denyer/pstack-claude) - Multi-agent workflow configs ported across Claude Code, Codex, Copilot, OpenCode and more.
- [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) - CLI tool and template collection for configuring and monitoring Claude Code.
- [maddada/Ghostex](https://github.com/maddada/Ghostex) - Native agents workspace built in Rust with 20+ agents and mobile apps.
- [peteromallet/desloppify](https://github.com/peteromallet/desloppify) - Agent harness to make slop code well-engineered and beautiful.
- [amosblomqvist/learnharness](https://github.com/amosblomqvist/learnharness) - Agent harness for learning difficult things.
- [JetBrains/thinkrail](https://github.com/JetBrains/thinkrail) - Vibe code with pi in a lightweight, real IDE that customises itself around you.

## Skills, Plugins & Context Engineering

*What you put in front of the agent matters more than which agent. Skills, CLAUDE.md files, methodology.*

**Skill frameworks & methodology**

- [obra/superpowers](https://github.com/obra/superpowers) - Agentic skills framework and development methodology (brainstorm → plan → TDD → review).
- [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) - Production-grade engineering skills from Addy Osmani.
- [garrytan/gstack](https://github.com/garrytan/gstack) - Garry Tan's opinionated Claude Code toolset.
- [affaan-m/ECC](https://github.com/affaan-m/ECC) - Harness performance-optimization system: skills, instincts, evals.
- [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) - AI task-management system that drops into Cursor, Claude Code or Lovable.
- [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) - File-based persistent planning for long-running agent tasks.
- [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) - Skill-management layer for agents.
- [skainguyen1412/antigravity-superpowers](https://github.com/skainguyen1412/antigravity-superpowers) - Superpowers workflows ported to Antigravity.
- [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) - Breakthrough Method for Agile Ai Driven Development.
- [danielmiessler/Fabric](https://github.com/danielmiessler/Fabric) - Fabric is an open-source framework for augmenting humans using AI. It provides a modular system.
- [SuperClaude-Org/SuperClaude_Framework](https://github.com/SuperClaude-Org/SuperClaude_Framework) - Framework enhancing Claude Code with commands, personas, and token-efficient modes.
- [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) - Official Compound Engineering plugin for Claude Code, Codex, Cursor, and more.
- [revfactory/harness](https://github.com/revfactory/harness) - Meta-skill that designs agent teams and generates the skills they use.
- [tony/claude-code-riper-5](https://github.com/tony/claude-code-riper-5) - RIPER-5 autonomous coding mode for Claude Code.
- [imbue-ai/blueprint](https://github.com/imbue-ai/blueprint) - Planning copilot for coding agents.
- [NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) - Hand-crafted skills for domain-driven architecture and subagent-driven development.
- [automazeio/ccpm](https://github.com/automazeio/ccpm) - Project management skill system using GitHub Issues and worktrees.
- [TexasBedouin/vibe-check](https://github.com/TexasBedouin/vibe-check) - Turns a vague idea into a buildable plan, then guides the build.
- [google-labs-code/design.md](https://github.com/google-labs-code/design.md) - A format specification for describing a visual identity to coding agents. DESIGN.md gives agents a persistent, structured understanding of a.
- [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) - 🦸 AI 编程超能力 · 中文增强版 — superpowers（250k+ ⭐）完整汉化 + 4 个中国原创 skills，让 Claude Code / Copilot CLI / Hermes Agent / Cursor / Windsurf / Kiro / Gemin.

**Autonomous loops (Ralph)**

- [ClaytonFarr/ralph-playbook](https://github.com/ClaytonFarr/ralph-playbook) - Comprehensive guide to running autonomous AI coding loops with Ralph.
- [frankbria/ralph-claude-code](https://github.com/frankbria/ralph-claude-code) - Autonomous AI development loop for Claude Code with exit detection.
- [mikeyobrien/ralph-orchestrator](https://github.com/mikeyobrien/ralph-orchestrator) - Improved Ralph Wiggum implementation for autonomous agent orchestration.
- [muratcankoylan/ralph-wiggum-marketer](https://github.com/muratcankoylan/ralph-wiggum-marketer) - Autonomous AI copywriter plugin built on the Ralph methodology.
- [snwfdhmp/awesome-ralph](https://github.com/snwfdhmp/awesome-ralph) - Curated resources on the Ralph autonomous-loop coding technique.

**Behavior-shaping skills (single-file, high leverage)**

- [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) - A single `CLAUDE.md` distilled from Karpathy's guidance.
- [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) - Makes the agent think like the laziest senior dev: YAGNI, stdlib first, shortest diff.
- [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) - Cut ~65% of output tokens by making the agent talk terse.
- [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) - Stops the agent burying the answer; answer-first output.
- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) - Gives your AI good taste; stops boring, generic output.
- [conorbronsdon/avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) - Audits and rewrites content to remove AI writing patterns.
- [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop) - Removes AI tells from prose before it reaches the reader.
- [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) - Removes AI-generated stylistic traces from text (Chinese edition).
- [tjboudreaux/cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) - 28 eval-informed mental models and critical-thinking skills for agents.
- [human-avatar/skills-for-humanity](https://github.com/human-avatar/skills-for-humanity) - Structured reasoning methods from history's rigorous thinkers, as skills.
- [pbakaus/impeccable](https://github.com/pbakaus/impeccable) - Design language that makes coding agents better at frontend design.
- [danyuchn/asd-ste100-skill](https://github.com/danyuchn/asd-ste100-skill) - Simplified Technical English rules as a skill for clearer agent-facing writing.
- [Spielewoy/autoprompt-skill](https://github.com/Spielewoy/autoprompt-skill) - Autoprompt is a coding-agent skill that cuts failures by 45% on agentic coding tasks.

**Official skill collections**

- [anthropics/skills](https://github.com/anthropics/skills) - Anthropic's official Agent Skills repo; the reference implementation of the Agent Skills standard.
- [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) - Vercel's official collection of agent skills.
- [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) - Official plugins for non-coding knowledge work.
- [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) - Official, Anthropic-managed directory of high-quality Claude Code plugins.
- [google/skills](https://github.com/google/skills) - Agent skills for Google products and technologies.
- [hashicorp/agent-skills](https://github.com/hashicorp/agent-skills) - Official skills and plugins for HashiCorp products.
- [qdrant/skills](https://github.com/qdrant/skills) - Agent skills for Qdrant vector search: scaling, quality, and monitoring.
- [anthropics/financial-services](https://github.com/anthropics/financial-services) - Anthropic's reference agents, skills and data connectors for financial services.
- [cursor/plugins](https://github.com/cursor/plugins) - Cursor's plugin specification and official plugins.
- [openai/plugins](https://github.com/openai/plugins) - OpenAI's official plugin collection.
- [greensock/gsap-skills](https://github.com/greensock/gsap-skills) - Official AI skills for GSAP. These skills teach AI coding agents how to correctly use GSAP (GreenSock Animation Platform), including best pr.
- [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) - A library of Agent Skills designed to work with the Stitch MCP server. Each skill follows the Agent Skills open standard, for compatibility.
- [slavingia/skills](https://github.com/slavingia/skills) - Claude Code skills based on The Minimalist Entrepreneur by Sahil Lavingia.

**Security skills**

- [agamm/claude-code-owasp](https://github.com/agamm/claude-code-owasp) - OWASP Top 10:2025 and ASVS 5.0 secure-coding skill.
- [BehiSecc/VibeSec-Skill](https://github.com/BehiSecc/VibeSec-Skill) - Helps Claude write secure code and prevent common vulnerabilities.
- [gadievron/raptor](https://github.com/gadievron/raptor) - Turns Claude Code into an offensive and defensive security agent.
- [jthack/ffuf_claude_skill](https://github.com/jthack/ffuf_claude_skill) - Lets Claude drive FFUF for web fuzzing workflows.
- [trailofbits/skills](https://github.com/trailofbits/skills) - Trail of Bits skills for security research, vulnerability detection, and audits.
- [anthropics/claude-code-security-review](https://github.com/anthropics/claude-code-security-review) - AI-powered security review GitHub Action that analyzes code changes for vulnerabilities.
- [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) - Security scanner for AI agent skills: detects vulnerabilities and prompt injection.
- [cso1z/claude-ip-guard](https://github.com/cso1z/claude-ip-guard) - Hook plugin for IP-based access control and account protection.
- [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) - Coding-agent skill for multi-phase security audits with verified findings.
- [SnailSploit/Claude-Red](https://github.com/SnailSploit/Claude-Red) - Library of offensive-security skills for Claude.

**Domain & workflow skills**

- [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) - Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by.
- [AlmogBaku/debug-skill](https://github.com/AlmogBaku/debug-skill) - Gives your agent a real debugger: breakpoints, stepping, inspection.
- [antonbabenko/terraform-skill](https://github.com/antonbabenko/terraform-skill) - Terraform and OpenTofu skill: modules, CI/CD, and production patterns.
- [bradautomates/claude-video](https://github.com/bradautomates/claude-video) - Lets Claude watch any video: downloads, extracts frames, transcribes.
- [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) - Marketing skills: CRO, copywriting, SEO, analytics, and growth.
- [gooseworks-ai/goose-skills](https://github.com/gooseworks-ai/goose-skills) - Growth and GTM skills plus data APIs for Claude Code, Codex, and Cursor.
- [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) - 67 specialized skills turning Claude Code into an expert full-stack pair programmer.
- [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) - 277 plug-and-play AI expert roles for 20+ tools across 20 departments.
- [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) - Socratic AI tutor skill grounded in Bloom's 2-sigma research.
- [mhattingpete/claude-skills-marketplace](https://github.com/mhattingpete/claude-skills-marketplace) - Skills for software engineering: Git automation, testing, and code review.
- [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) - Collection of skills for context engineering and multi-agent architectures.
- [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) - Researches any topic across Reddit, X, YouTube, and HN from the last 30 days.
- [Orchestra-Research/AI-Research-SKILLs](https://github.com/Orchestra-Research/AI-Research-SKILLs) - Open-source library of AI research and engineering skills for any model.
- [pasky/chrome-cdp-skill](https://github.com/pasky/chrome-cdp-skill) - Hooks your agent into your live Chrome session over CDP.
- [rampstackco/claude-skills](https://github.com/rampstackco/claude-skills) - Stack-agnostic skills covering the website lifecycle: brand, SEO, dev, ops, growth.
- [sanjay3290/ai-skills](https://github.com/sanjay3290/ai-skills) - 24 cross-platform skills for Claude Code, Cursor, Codex, and Gemini CLI.
- [SerhiiKorniienko/bullshit-detector](https://github.com/SerhiiKorniienko/bullshit-detector) - Fact-checks the internet claim-by-claim with a 0-10 BS score.
- [skills-directory/skill-codex](https://github.com/skills-directory/skill-codex) - Skill that delegates prompts to Codex from Claude Code.
- [wrsmith108/linear-claude-skill](https://github.com/wrsmith108/linear-claude-skill) - Skill for managing Linear issues, projects, and teams via MCP and SDK.
- [zarazhangrui/codebase-to-course](https://github.com/zarazhangrui/codebase-to-course) - Skill turning any codebase into an interactive HTML course.
- [zxkane/aws-skills](https://github.com/zxkane/aws-skills) - Plugins and skills for AWS development: IaC, serverless, cost ops, AgentCore.
- [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) - Agent skills that teach agents to use Obsidian CLI and open file formats.
- [phuryn/pm-skills](https://github.com/phuryn/pm-skills) - Marketplace of 100+ product management skills, commands and plugins for agents.
- [czlonkowski/n8n-skills](https://github.com/czlonkowski/n8n-skills) - Claude Code skill set for building reliable n8n workflows.
- [Weizhena/Deep-Research-skills](https://github.com/Weizhena/Deep-Research-skills) - Structured deep research skill for Claude Code, OpenCode and Codex.
- [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) - Turns Claude Code into a game dev studio with 49 agents and 72 skills.
- [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) - Collection of 100+ specialized Claude Code subagents.
- [mattpocock/skills](https://github.com/mattpocock/skills) - Matt Pocock's engineering skills from his own agents directory.
- [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) - Specialized agent personas covering engineering, design, marketing and more.
- [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) - Agent skill with design intelligence for building UI/UX across platforms.
- [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) - DESIGN.md files from popular design systems for coding agents to follow.
- [tt-a1i/archify](https://github.com/tt-a1i/archify) - Agent skill that turns ideas, plans or codebases into interactive diagrams.
- [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) - Gives coding agents CAD modeling abilities.
- [neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster) - Image-to-world skill set for Claude.
- [humanlayer/skills](https://github.com/humanlayer/skills) - HumanLayer's Claude Code skills for diagrams, visual PRs and more.
- [WorldFlowAI/everything-claude-code](https://github.com/WorldFlowAI/everything-claude-code) - Claude Code toolkit of agents, commands, skills, rules and hooks.
- [rehan-remade/universal-modder](https://github.com/rehan-remade/universal-modder) - Skills and tools that let Claude Code mod almost any PC game.

**Hooks, status lines & usage tracking**

- [ccusage/ccusage](https://github.com/ccusage/ccusage) - Track Claude Code usage and token spend from the terminal.
- [disler/claude-code-hooks-multi-agent-observability](https://github.com/disler/claude-code-hooks-multi-agent-observability) - Real-time monitoring of agents through hook events.
- [disler/claude-code-hooks-mastery](https://github.com/disler/claude-code-hooks-mastery) - Master Claude Code hooks with patterns and examples.
- [egorfedorov/claude-context-optimizer](https://github.com/egorfedorov/claude-context-optimizer) - Tracks token usage and wasted context, saving 30-50% on API costs.
- [karanb192/claude-code-hooks](https://github.com/karanb192/claude-code-hooks) - Hooks plus an installable marketplace: safety, cost, observability.
- [kenryu42/cc-safety-net](https://github.com/kenryu42/cc-safety-net) - Pre-execution guard blocking destructive git and filesystem commands.
- [leeguooooo/claude-code-usage-bar](https://github.com/leeguooooo/claude-code-usage-bar) - Status line with 5h/7d usage, reset countdowns, model, context window.
- [mag123c/toktrack](https://github.com/mag123c/toktrack) - Ultra-fast token and cost tracker for LLM usage.
- [luoyuctl/agenttrace](https://github.com/luoyuctl/agenttrace) - Local-first TUI auditing agent sessions: cost, latency, failures.
- [Owloops/claude-powerline](https://github.com/Owloops/claude-powerline) - Vim-style powerline status line for Claude Code.
- [shanraisshan/claude-code-hooks](https://github.com/shanraisshan/claude-code-hooks) - Hooks that announce agent activity with voice feedback.

**Context compression & management**

- [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) - Compress tool outputs, logs, files, and RAG chunks before they reach the LLM. 20% fewer tokens.
- [jia-gao/leanctx](https://github.com/jia-gao/leanctx) - Drop-in prompt compression cutting token bills 40-60%.
- [microsoft/LLMLingua](https://github.com/microsoft/LLMLingua) - Prompt compression up to 20x with minimal information loss.
- [parcadei/Continuous-Claude-v3](https://github.com/parcadei/Continuous-Claude-v3) - Context management via hooks: ledgers, handoffs, no context pollution.
- [yvgude/lean-ctx](https://github.com/yvgude/lean-ctx) - Context intelligence tooling for AI systems.
- [mksglu/context-mode](https://github.com/mksglu/context-mode) - Context window optimizer that sandboxes tool output for AI coding agents.
- [ZongqianLi/500xCompressor](https://github.com/ZongqianLi/500xCompressor) - [ACL 2025] 500xCompressor: generalized prompt compression for LLMs.
- [wilpel/caveman-compression](https://github.com/wilpel/caveman-compression) - Caveman Compression: semantic compression for LLM context.
- [ojuschugh1/sqz](https://github.com/ojuschugh1/sqz) - Context compression for AI coding agents, compressing tool output.
- [ooples/token-optimizer-mcp](https://github.com/ooples/token-optimizer-mcp) - Measure token savings per coding agent and optimize context.
- [sci-m-wang/OpenCE](https://github.com/sci-m-wang/OpenCE) - OpenCE: community toolkit to implement and evaluate context engineering.
- [Context-Engine-AI/Context-Engine](https://github.com/Context-Engine-AI/Context-Engine) - Agentic context compression suite delivered over MCP.
- [Ahren09/SARA](https://github.com/Ahren09/SARA) - [ACL 2026] SARA: selective and adaptive context compression.
- [snchimata/tokenfold](https://github.com/snchimata/tokenfold) - Private, provider-neutral, reversible context compression for LLMs.
- [yzhangchuck/Sentinel](https://github.com/yzhangchuck/Sentinel) - Sentinel: lightweight, interpretable context compression for LLMs.
- [Supercompress/Supercompress](https://github.com/Supercompress/Supercompress) - Query-aware context compression for LLMs, cutting about 65% of tokens.
- [dshakes/distil](https://github.com/dshakes/distil) - Compression with a quality contract: cache-aware and causally pruned.
- [Adityapal67/context-graph-compressor](https://github.com/Adityapal67/context-graph-compressor) - Convert long AI conversations into portable conversation state graphs.

**Prompt engineering**

- [KhazP/vibe-coding-prompt-template](https://github.com/KhazP/vibe-coding-prompt-template) - Templates for PRDs, tech designs and MVP workflows.
- [f/prompts.chat](https://github.com/f/prompts.chat) - f.k.a. Awesome ChatGPT Prompts. Share, discover, and collect prompts from the community. Free.
- [dair-ai/Prompt-Engineering-Guide](https://github.com/dair-ai/Prompt-Engineering-Guide) - Guides, papers, lessons, notebooks and resources for prompt engineering, context engineering, RAG, and AI Agents.
- [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) - Anthropic's interactive prompt engineering tutorial.
- [langgptai/LangGPT](https://github.com/langgptai/LangGPT) - Structured prompt framework for becoming a prompt expert.
- [NirDiamant/Prompt_Engineering](https://github.com/NirDiamant/Prompt_Engineering) - 22 prompt engineering techniques with hands-on notebooks.
- [promptslab/Promptify](https://github.com/promptslab/Promptify) - Prompt engineering and versioning toolkit for structured output.
- [promptslab/Awesome-Prompt-Engineering](https://github.com/promptslab/Awesome-Prompt-Engineering) - Hand-curated prompt engineering resources and guides.
- [ianarawjo/ChainForge](https://github.com/ianarawjo/ChainForge) - Visual environment for battle-testing prompts against LLMs.
- [gepa-ai/gepa](https://github.com/gepa-ai/gepa) - AI-powered reflective optimization for prompts and code.

**System prompt collections**

- [x1xhlol/system-prompts-and-models-of-ai-tools](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) - Leaked system prompts of Cursor, Devin, Claude Code and others; study how the pros prompt.
- [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) - Extracted system prompts from Anthropic, OpenAI and Google products.
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) - Complete collection of Claude Code system prompts and tool definitions.

**Guides & best practices**

- [coleam00/context-engineering-intro](https://github.com/coleam00/context-engineering-intro) - Practical introduction to context engineering.
- [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) - From vibe coding to agentic engineering.
- [danielrosehill/Claude-Code-Projects-Index](https://github.com/danielrosehill/Claude-Code-Projects-Index) - Index of starter templates and projects for Claude Code.
- [ithiria894/awesome-claude-code-workflows](https://github.com/ithiria894/awesome-claude-code-workflows) - Workflow recipes combining hooks, MCP, skills, agents, and CLAUDE.md.
- [jasontang-ai/Context-Engineering](https://github.com/jasontang-ai/Context-Engineering) - Guide to filling the context window with just the right information.
- [kousen/claude-code-training](https://github.com/kousen/claude-code-training) - Slides and demos for a Claude Code training course.
- [loulanyue/awesome-claude-notes](https://github.com/loulanyue/awesome-claude-notes) - Community notes: agents, commands, skills, hooks, and workflows.
- [OneRedOak/claude-code-workflows](https://github.com/OneRedOak/claude-code-workflows) - Battle-tested workflows from day-one Claude Code use.
- [wesammustafa/Claude-Code-Everything-You-Need-to-Know](https://github.com/wesammustafa/Claude-Code-Everything-You-Need-to-Know) - Practical guide with mental models and copy-paste examples.
- [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips) - 45+ tips for getting the most out of Claude Code.
- [VILA-Lab/Dive-into-Claude-Code](https://github.com/VILA-Lab/Dive-into-Claude-Code) - Systematic analysis of Claude Code for designing agent systems.
- [zebbern/claude-code-guide](https://github.com/zebbern/claude-code-guide) - Setup, commands, workflows, agents, skills, and tips from beginner to power user.

**Plugin & skill directories**

- [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) - The canonical Claude Code resource list.
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) - Curated Claude Skills.
- [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) - 380+ skills, agents and plugins.
- [heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills) - Tutorials, guides and skill directories.
- [quemsah/awesome-claude-plugins](https://github.com/quemsah/awesome-claude-plugins) - Plugin adoption metrics across GitHub.
- [awesome-opencode/awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) - Plugins, themes and agents for OpenCode.
- [0xNyk/awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent) - Skills, plugins and memory providers for Hermes.
- [ai-boost/awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) - Tools, patterns and evals for agent harnesses.
- [sickn33/agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) - Local, agent-first control plane for skill catalogs.
- [jeremylongshore/tons-of-skills-marketplace](https://github.com/jeremylongshore/tons-of-skills-marketplace) - Model-agnostic skills marketplace with a canonical layout.
- [wshobson/agents](https://github.com/wshobson/agents) - Multi-harness plugin and skill marketplace for Claude Code, Codex, Cursor, OpenCode, and Copilot.
- [PatrickJS/awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules) - The definitive collection of .cursorrules for every stack.
- [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) - 135 agents, 35 skills, 176+ plugins, and 20 hooks for Claude Code.
- [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) - 5,400+ OpenClaw skills, filtered and categorized.
- [standardbeagle/standardbeagle-tools](https://github.com/standardbeagle/standardbeagle-tools) - Claude Code marketplace plugins: browser, code intelligence, tools.

**Spec-driven development**

- [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) - Spec-driven development (SDD) for AI coding assistants.
- [github/spec-kit](https://github.com/github/spec-kit) - Toolkit to help you get started with Spec-Driven Development.
- [buildermethods/agent-os](https://github.com/buildermethods/agent-os) - Spec-driven development system with codebase standards.

**Codebase context & packing**

- [yamadashy/repomix](https://github.com/yamadashy/repomix) - Packs an entire repository into one AI-friendly file for LLM context.
- [coderamp-labs/gitingest](https://github.com/coderamp-labs/gitingest) - Turn any GitHub URL into a prompt-friendly codebase extract.
- [mohsen1/yek](https://github.com/mohsen1/yek) - Fast Rust tool serializing repo files for LLM consumption.
- [mufeedvh/code2prompt](https://github.com/mufeedvh/code2prompt) - CLI converting a codebase into one prompt with tree, templates, token count.
- [repoprompt/repoprompt-ce](https://github.com/repoprompt/repoprompt-ce) - Native macOS context-engineering app for AI coding agents.
- [zilliztech/claude-context](https://github.com/zilliztech/claude-context) - Code search MCP that makes an entire codebase context for coding agents.
- [oraios/serena](https://github.com/oraios/serena) - Coding agent toolkit with semantic code understanding.
- [cyberchitta/llm-context.py](https://github.com/cyberchitta/llm-context.py) - Share code with LLMs via MCP or clipboard, with rule-based customization.
- [vercel-labs/opensrc](https://github.com/vercel-labs/opensrc) - Fetch source code for npm packages to give AI coding agents deeper context.

**Skill tooling & rules sync**

- [activeloopai/hivemind](https://github.com/activeloopai/hivemind) - Turns coding-agent session traces into reusable skills across agents.
- [agent-sh/agnix](https://github.com/agent-sh/agnix) - Linter for agent configs: validates SKILL.md, CLAUDE.md, hooks, and MCP definitions.
- [hqhq1025/skill-optimizer](https://github.com/hqhq1025/skill-optimizer) - Lifecycle toolkit: mine workflows, audit skills, and personalize from session data.
- [sentient-agi/EvoSkill](https://github.com/sentient-agi/EvoSkill) - Automatically discovers and synthesizes reusable skills from failed trajectories.
- [tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness) - Self-learning skill layer for Claude Code that distills sessions into skills.
- [iflytek/skillhub](https://github.com/iflytek/skillhub) - Self-hosted agent skill registry for publishing and versioning skill packages.
- [greyhaven-ai/autocontext](https://github.com/greyhaven-ai/autocontext) - Recursive self-improving harness for agent success.
- [dyoshikawa/rulesync](https://github.com/dyoshikawa/rulesync) - Utility CLI syncing agent rules across coding tools.
- [Gentleman-Programming/gentle-ai](https://github.com/Gentleman-Programming/gentle-ai) - Configures the coding agents you already use, including Claude Code and Cursor.
- [Piebald-AI/tweakcc](https://github.com/Piebald-AI/tweakcc) - Customize Claude Code's system prompts, toolsets, and themes.
- [pchalasani/claude-code-tools](https://github.com/pchalasani/claude-code-tools) - Productivity tools for Claude Code, Codex-CLI, and similar agents.
- [xingkongliang/skills-manager](https://github.com/xingkongliang/skills-manager) - Desktop app to manage and sync agent skills across 50+ coding tools.
- [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) - Turn any technical book PDF into a Claude Code skill — ready to study, reference, and use while you work.
- [titanwings/distilly](https://github.com/titanwings/distilly) - Distilly — Distill how they think into reusable Skills for any Agent or Bot. Formerly Colleague Skill（原同事 Skill）.
- [ciembor/agent-rules-books](https://github.com/ciembor/agent-rules-books) - AGENTS.md rules / skills for AI coding agents: Codex, Cursor & Claude Code. Inspired by Clean Code, Refactoring, DDD, Clean Architecture and.
- [Spark-To-Paper-Skills/paperjury](https://github.com/Spark-To-Paper-Skills/paperjury) - Pre-submission AI review stress-test for research papers. A Claude Code skill: review, verdict, revise, verify.
- [ranxianglei/billion-context](https://github.com/ranxianglei/billion-context) - A context-compression plugin for small context windows (a 100K context is enough), token savings (5x fewer tokens), and month-long single se.
- [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) - Clone any website with one command using AI coding agents.
- [first-fluke/oh-my-agent](https://github.com/first-fluke/oh-my-agent) - A specialist team for the coding agent you already use: 12 roles, 21 workflows and 33 skills that plan, build in parallel, review and debug.
- [Appllama/appllama-skills](https://github.com/Appllama/appllama-skills) - Agent skills for building mobile apps, checked in simulators.
- [soumatheusgomes/vibe-coding-toolkit](https://github.com/soumatheusgomes/vibe-coding-toolkit) - Docs, prompts and templates for coding with Claude Code and Codex subagents.
- [ruc-datalab/EvoOntology](https://github.com/ruc-datalab/EvoOntology) - Self-evolving ontology layer for data agents: builds and refines domain semantics from data, exposed as MCP tools and Claude Code/Codex plugins.
- [android/skills](https://github.com/android/skills) - Google's official skills collection for Android development with AI agents.
- [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design) - Editorial diagram design skill for Claude Code, Codex, Copilot, Cursor and other coding agents.
- [ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills) - AI agent skills for social media research: outlier posts, comment mining and competitor teardowns.
- [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) - Universal SEO skill for Claude Code: 26 sub-skills and 19 sub-agents.
- [samber/cc-skills-golang](https://github.com/samber/cc-skills-golang) - Collection of Golang agentic skills.
- [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) - Agent skill for creating detailed, interactive isometric illustrations of real-world machines.
- [bowenliang123/dsh-context](https://github.com/bowenliang123/dsh-context) - DeepSeek Harness plugin for context insight and management, with a context dashboard.
- [vercel-labs/skills](https://github.com/vercel-labs/skills) - Vercel's open agent skills tool: npx skills.
- [Nutlope/hallmark](https://github.com/Nutlope/hallmark) - Anti-AI-slop design skill for Claude Code, Cursor and Codex.
- [Jakeschincariol/replica-skill](https://github.com/Jakeschincariol/replica-skill) - Agent skill for replicating interfaces and designs.
- [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) - Agent skill for building frontend slide decks.
- [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) - Local video editor for coding agents: 42 FFmpeg tools with a machine-readable contract and an MCP server, for Claude Code, Cursor and Codex.
- [dzhng/skills](https://github.com/dzhng/skills) - Reusable AI agent skills for software factories: explore ideas, write specs, implement, review, and run autonomous research.
- [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) - AI video skill for Claude Code and Codex: cinematic product videos.
- [plugin87/ux-ui-agent-skills](https://github.com/plugin87/ux-ui-agent-skills) - Agent skills that turn Claude into a senior design architect: design tokens and components.
- [Shpigford/chops](https://github.com/Shpigford/chops) - macOS app to browse, edit and manage your AI agent skills.
- [agentskills/agentskills](https://github.com/agentskills/agentskills) - Specification and documentation for Agent Skills.
- [OpenSenseNova/SenseNova-Skills](https://github.com/OpenSenseNova/SenseNova-Skills) - Modular SenseNova skills for building AI-powered office assistants.
- [microsoft/skill-recorder](https://github.com/microsoft/skill-recorder) - Desktop app that records your on-screen work session and turns it into GitHub Copilot agent skills.
- [Jakeschincariol/day-trader-skill](https://github.com/Jakeschincariol/day-trader-skill) - 11 Claude skills for day trading: scan thousands of charts and track breaking news.

## Agent Frameworks & Orchestration

*Build your own agents and multi-agent systems.*

**Core frameworks**

- [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) - Graph-based stateful agent orchestration; the default for production Python agents.
- [langchain-ai/langchain](https://github.com/langchain-ai/langchain) - The original LLM application framework and integration ecosystem.
- [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) - Type-safe agent framework from the Pydantic team; great for structured outputs.
- [openai/openai-agents-python](https://github.com/openai/openai-agents-python) - OpenAI's lightweight multi-agent SDK with handoffs and guardrails.
- [google/adk-python](https://github.com/google/adk-python) - Google's Agent Development Kit for Gemini and beyond.
- [anthropics/anthropic-sdk-python](https://github.com/anthropics/anthropic-sdk-python) - Official Claude SDK; tool use, streaming and the Agent SDK.
- [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) - Role-playing multi-agent crews with tasks and processes.
- [microsoft/autogen](https://github.com/microsoft/autogen) - Conversational multi-agent framework from Microsoft Research.
- [huggingface/smolagents](https://github.com/huggingface/smolagents) - Minimal agents that write code as actions.
- [run-llama/llama_index](https://github.com/run-llama/llama_index) - Data framework for connecting LLMs to your data; strong agentic RAG.
- [deepset-ai/haystack](https://github.com/deepset-ai/haystack) - Production-oriented pipelines for RAG and agents.
- [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) - Program, don't prompt: optimize prompts and weights declaratively.
- [agno-agi/agno](https://github.com/agno-agi/agno) - Build, run, and manage agent platforms.
- [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) - The batteries-included agent harness.
- [microsoft/agent-framework](https://github.com/microsoft/agent-framework) - Microsoft's framework for building, orchestrating and deploying agents.
- [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) - Build agents you can see, understand and trust.
- [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) - Microsoft's SDK for building LLM agents into .NET, Python, and Java apps.
- [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) - AWS's official open-source agent SDK for Python and TypeScript, any model or cloud.
- [ag2ai/ag2](https://github.com/ag2ai/ag2) - AG2 (formerly AutoGen): the open-source AgentOS for multi-agent applications.
- [anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python) - Official Python SDK for building Claude-powered agents.
- [i-am-bee/beeai-framework](https://github.com/i-am-bee/beeai-framework) - Build production-ready AI agents in Python and TypeScript.
- [Upsonic/Upsonic](https://github.com/Upsonic/Upsonic) - Build autonomous AI agents in Python.
- [Eigenwise/atomic-agents](https://github.com/Eigenwise/atomic-agents) - Build AI agents atomically with modular, composable components.
- [Forethought-Technologies/AutoChain](https://github.com/Forethought-Technologies/AutoChain) - Build lightweight, extensible, and testable LLM agents.
- [jackmpcollins/magentic](https://github.com/jackmpcollins/magentic) - Seamlessly integrate LLMs as plain Python functions.
- [Mirascope/mirascope](https://github.com/Mirascope/mirascope) - The LLM anti-framework: minimal abstractions over provider APIs.
- [langroid/langroid](https://github.com/langroid/langroid) - Harness LLMs with multi-agent programming in Python.
- [SylphAI-Inc/AdalFlow](https://github.com/SylphAI-Inc/AdalFlow) - Library to build and auto-optimize LLM applications.
- [The-Pocket/PocketFlow](https://github.com/The-Pocket/PocketFlow) - 100-line LLM framework where agents can build agents.
- [TencentCloudADP/youtu-agent](https://github.com/TencentCloudADP/youtu-agent) - Simple agent framework built to work well with open-source models.
- [evalstate/fast-agent](https://github.com/evalstate/fast-agent) - Build and evaluate agents with MCP, skills, ACP and A2A support.
- [QwenLM/Qwen-Agent](https://github.com/QwenLM/Qwen-Agent) - Agent framework on Qwen with function calling, MCP, and code execution.
- [microsoft/Agents-for-python](https://github.com/microsoft/Agents-for-python) - Microsoft 365 Agents SDK for Python.
- [andrewyng/openworker](https://github.com/andrewyng/openworker) - Andrew Ng's open agentic-worker framework.
- [lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent) - Build effective agents with Model Context Protocol and simple workflows.
- [emcie-co/parlant](https://github.com/emcie-co/parlant) - Interaction control harness for building reliable customer-facing agents.
- [RasaHQ/rasa](https://github.com/RasaHQ/rasa) - Open-source machine learning framework for text and voice assistants.
- [aurelio-labs/semantic-router](https://github.com/aurelio-labs/semantic-router) - Superfast semantic decision-making for routing between agents and tools.
- [humanlayer/humanlayer](https://github.com/humanlayer/humanlayer) - Human-in-the-loop layer so coding agents solve hard problems safely.
- [griptape-ai/griptape](https://github.com/griptape-ai/griptape) - Modular Python framework for AI agents and workflows with chain-of-thought reasoning, tools, and memory.
- [PrefectHQ/marvin](https://github.com/PrefectHQ/marvin) - Ambient intelligence library for agentic data workflows.
- [modelscope/ms-agent](https://github.com/modelscope/ms-agent) - MS-Agent: a lightweight framework to empower agentic execution of complex tasks.
- [microsoft/agent-lightning](https://github.com/microsoft/agent-lightning) - The absolute trainer to light up AI agents.
- [google/ax](https://github.com/google/ax) - Google's open agentic orchestration runtime.
- [cobusgreyling/loop-engineering](https://github.com/cobusgreyling/loop-engineering) - Practical patterns, starters & CLI tools for loop engineering with AI coding agents. Design systems that prompt and orchestrate agents (insp.
- [superplanehq/superplane](https://github.com/superplanehq/superplane) - Open source factory for one-shot engineering.
- [Q00/ouroboros](https://github.com/Q00/ouroboros) - Agent OS: the agent gets smarter on its own. We just hold the line: Interview-gated, staged evaluation, budgeted evolution loop. MCP server,.
- [ageerle/ruoyi-ai](https://github.com/ageerle/ruoyi-ai) - Enterprise-grade AI agent framework with multi-provider LLM management, secure knowledge bases and high-precision RAG, visual workflow orche.
- [ApodexAI/FrontierAgent](https://github.com/ApodexAI/FrontierAgent) - 🧩 FrontierAgent, our agent framework, open-sourced alongside it — native command-line TUI, ReAct and Agent Team modes, one command on macOS.
- [Intelligent-Internet/ii-agent](https://github.com/Intelligent-Internet/ii-agent) - II-Agent: a new open-source framework to build and deploy intelligent agents.
- [yomorun/yomo](https://github.com/yomorun/yomo) - 🦖 Serverless AI Agent Framework with Geo-distributed Edge AI Infra.

**TypeScript & JavaScript frameworks**

- [mastra-ai/mastra](https://github.com/mastra-ai/mastra) - Mastra is the modern TypeScript framework for AI-powered applications and agents.
- [genkit-ai/genkit](https://github.com/genkit-ai/genkit) - Google's open-source framework for agentic apps in JS, Go, Python, and Dart.
- [elizaOS/eliza](https://github.com/elizaOS/eliza) - TypeScript framework for autonomous agents across chat, social, and on-chain integrations.
- [anthropics/anthropic-sdk-typescript](https://github.com/anthropics/anthropic-sdk-typescript) - Official TypeScript SDK for Anthropic APIs and agent tooling.
- [anthropics/claude-agent-sdk-typescript](https://github.com/anthropics/claude-agent-sdk-typescript) - Official TypeScript SDK for building Claude-powered agents.
- [google/adk-js](https://github.com/google/adk-js) - Google's open-source, code-first TypeScript toolkit for building agents.
- [inngest/agent-kit](https://github.com/inngest/agent-kit) - Build multi-agent networks in TypeScript with deterministic routing.
- [kaiban-ai/KaibanJS](https://github.com/kaiban-ai/KaibanJS) - JavaScript-native framework for building multi-agent teams.
- [langchain-ai/langchainjs](https://github.com/langchain-ai/langchainjs) - The agent engineering platform for JavaScript and TypeScript.
- [openai/openai-agents-js](https://github.com/openai/openai-agents-js) - Lightweight framework for multi-agent workflows and voice agents.
- [VoltAgent/voltagent](https://github.com/VoltAgent/voltagent) - AI agent engineering platform on open-source TypeScript.
- [vercel/eve](https://github.com/vercel/eve) - The open framework for building agents.
- [withastro/flue](https://github.com/withastro/flue) - The sandbox agent framework.
- [open-multi-agent/open-multi-agent](https://github.com/open-multi-agent/open-multi-agent) - Self-hosted TypeScript agent runtime with durable approvals and run records.
- [cloudflare/agents](https://github.com/cloudflare/agents) - Build and deploy AI agents on Cloudflare's edge network.
- [daydreamsai/daydreams](https://github.com/daydreamsai/daydreams) - TypeScript toolkit for building commerce-focused AI agents.
- [bradygaster/squad](https://github.com/bradygaster/squad) - AI agent teams for any project, in TypeScript.

**Go, Java, Rust, Ruby & other languages**

- [0xPlaygrounds/rig](https://github.com/0xPlaygrounds/rig) - Modular Rust library for building scalable LLM-powered applications.
- [agenticenv/agent-sdk-go](https://github.com/agenticenv/agent-sdk-go) - Durable execution framework for AI agents in Go.
- [agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java) - Build distributed, production-grade, long-running agents in Java.
- [aixgo-dev/aixgo](https://github.com/aixgo-dev/aixgo) - AI-native agent framework for Go.
- [BoxcarsAI/boxcars](https://github.com/BoxcarsAI/boxcars) - Composable Ruby framework for building applications with LLMs.
- [cloudwego/eino](https://github.com/cloudwego/eino) - ByteDance's Go framework for LLM/AI application development.
- [embabel/embabel-agent](https://github.com/embabel/embabel-agent) - JVM agent framework for predictable, enterprise-grade agents.
- [geminik23/ai-agents](https://github.com/geminik23/ai-agents) - Declarative Rust agent framework: one YAML defines any agent.
- [google/adk-go](https://github.com/google/adk-go) - Google's open-source, code-first Go toolkit for building agents.
- [google/adk-java](https://github.com/google/adk-java) - Google's open-source, code-first Java toolkit for building agents.
- [JetBrains/koog](https://github.com/JetBrains/koog) - JVM framework for predictable, fault-tolerant, enterprise agents.
- [langchain4j/langchain4j](https://github.com/langchain4j/langchain4j) - Idiomatic Java library for building LLM applications.
- [LLPhant/LLPhant](https://github.com/LLPhant/LLPhant) - Comprehensive PHP generative AI framework with agent support.
- [patterns-ai-core/langchainrb](https://github.com/patterns-ai-core/langchainrb) - Build LLM-powered applications in Ruby.
- [prism-php/prism](https://github.com/prism-php/prism) - Unified interface for working with LLMs in Laravel.
- [rhgs/crewai-go](https://github.com/rhgs/crewai-go) - Idiomatic Go port of CrewAI for collaborative autonomous agents.
- [Shopify/roast](https://github.com/Shopify/roast) - Structured AI workflows made easy in Ruby.
- [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai) - Application framework for AI engineering on Spring.
- [tmc/langchaingo](https://github.com/tmc/langchaingo) - LangChain for Go: the easiest way to write LLM programs in Go.
- [crmne/ruby_llm](https://github.com/crmne/ruby_llm) - Ruby-native AI framework for chat, agents, tools and media through one API.
- [agentjido/jido](https://github.com/agentjido/jido) - Autonomous, distributed agent framework for Elixir.
- [trpc-group/trpc-agent-go](https://github.com/trpc-group/trpc-agent-go) - Go framework for production agents with graph workflows, tools and memory.
- [alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba) - Agentic AI framework for Java developers.
- [11fsociety/encom](https://github.com/11fsociety/encom) - Open-source AI agent framework; single-binary Rust daemon with TypeScript skills.
- [thClaws/thClaws](https://github.com/thClaws/thClaws) - Open-source AI agent harness in native Rust: GUI, CLI, and headless.
- [GCWing/OpenBitFun](https://github.com/GCWing/OpenBitFun) - OpenBitFun combines a high-performance agent runtime written in Rust with a polished desktop application. It pairs the depth of a Code Agent.

**Multi-agent systems**

- [bytedance/deer-flow](https://github.com/bytedance/deer-flow) - An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the.
- [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) - ChatDev 2.0: Dev All through LLM-powered Multi-Agent Collaboration.
- [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) - The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming.
- [2FastLabs/agent-squad](https://github.com/2FastLabs/agent-squad) - Flexible framework for managing multiple AI agents and complex conversations.
- [camel-ai/camel](https://github.com/camel-ai/camel) - Pioneering multi-agent framework for role-playing autonomous agents.
- [camel-ai/owl](https://github.com/camel-ai/owl) - Optimized workforce learning for general multi-agent assistance.
- [FoundationAgents/OpenManus](https://github.com/FoundationAgents/OpenManus) - Open-source generalist multi-agent framework.
- [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) - Agent swarm intelligence with one-command full automation.
- [kyegomez/swarms](https://github.com/kyegomez/swarms) - Enterprise-grade multi-agent orchestration framework.
- [openai/swarm](https://github.com/openai/swarm) - Educational framework for ergonomic, lightweight multi-agent orchestration.
- [VRSEN/agency-swarm](https://github.com/VRSEN/agency-swarm) - Reliable multi-agent orchestration framework.
- [openagents-org/openagents](https://github.com/openagents-org/openagents) - The collaboration OS for AI agents.
- [multica-ai/multica](https://github.com/multica-ai/multica) - Make humans and AI agents work as one team; open-source and self-hostable.
- [MervinPraison/PraisonAI](https://github.com/MervinPraison/PraisonAI) - Multi-agent framework for building always-on AI workforces.
- [yyyy231209/ai-company-framework](https://github.com/yyyy231209/ai-company-framework) - Open-source multi-agent orchestration for running an AI company.
- [Zerone-Laboratories/RIGEL](https://github.com/Zerone-Laboratories/RIGEL) - Multi-agentic AI assistant and builder.
- [NeuroLift-Technologies/nlt-otoi](https://github.com/NeuroLift-Technologies/nlt-otoi) - Multi-agent orchestration with user-defined terms of interaction.
- [sipyourdrink-ltd/bernstein](https://github.com/sipyourdrink-ltd/bernstein) - Declarative governance and orchestration framework for AI agents.
- [GammaLabTechnologies/harmonist](https://github.com/GammaLabTechnologies/harmonist) - Portable agent orchestration with mechanical protocol enforcement.
- [block/buzz](https://github.com/block/buzz) - Hive-mind communication platform for coordinating agent swarms.
- [aden-hive/hive](https://github.com/aden-hive/hive) - Multi-agent harness for production AI workloads.
- [ruvnet/ruflo](https://github.com/ruvnet/ruflo) - Agent harness for deploying multi-player swarms and autonomous workflows.
- [cft0808/edict](https://github.com/cft0808/edict) - OpenClaw multi-agent orchestration with nine specialized agents and dashboard.
- [CelestoAI/agentor](https://github.com/CelestoAI/agentor) - Open-source Claude managed-agents platform for building agent teams.
- [compozy/compozy](https://github.com/compozy/compozy) - Operating system for AI agents that plugs into your existing agent CLIs.
- [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) - Open orchestration platform for teams of AI agents and their people.
- [Runfusion/Fusion](https://github.com/Runfusion/Fusion) - Software factory: multi-node agents building software around the clock.
- [phodal/routa](https://github.com/phodal/routa) - Workspace-first multi-agent coordination with shared specs and Kanban.
- [hfadhlullah/kaizen](https://github.com/hfadhlullah/kaizen) - Agents show the plan first, then a second agent reviews the work.
- [paperclipai/paperclip](https://github.com/paperclipai/paperclip) - The open-source app everyone uses to manage agents at work.
- [zhayujie/CowAgent](https://github.com/zhayujie/CowAgent) - Open-source super AI assistant and self-evolving agent harness.
- [openakita/openakita](https://github.com/openakita/openakita) - Open-source AI assistant framework with skills and agent architecture.
- [TokenRhythm/opensquilla](https://github.com/TokenRhythm/opensquilla) - Token-efficient AI agent with higher intelligence density per budget.
- [OrchestratorInc/agent-orchestrator](https://github.com/OrchestratorInc/agent-orchestrator) - Run and supervise teams of coding agents from planning to merge. Any harness (Claude code, codex, +25 more). Desktop, web, mobile, and cloud.
- [RunMaestro/Maestro](https://github.com/RunMaestro/Maestro) - Agent Orchestration Command Center.
- [stellarlinkco/myclaude](https://github.com/stellarlinkco/myclaude) - Multi-agent orchestration workflow (Claude Code Codex Gemini OpenCode).
- [Kocoro-lab/Shannon](https://github.com/Kocoro-lab/Shannon) - A production-oriented multi-agent orchestration framework.
- [rcortx/kiwiq](https://github.com/rcortx/kiwiq) - Production-grade multi-agent orchestration platform - JSON-defined agents, multi-tier memory, and built-in observability. Battle-tested on 2.
- [Mininglamp-OSS/octo-server](https://github.com/Mininglamp-OSS/octo-server) - 🐙 The Go backend powering OCTO — an open workplace built for humans × AI agents. REST & WebSocket APIs, Lobster (AI agent) orchestration, an.
- [crestalnetwork/intentkit](https://github.com/crestalnetwork/intentkit) - IntentKit is an open-source, self-hosted cloud agent cluster that manages a collaborative team of AI agents for you.
- [nextlevelbuilder/goclaw](https://github.com/nextlevelbuilder/goclaw) - GoClaw - GoClaw is OpenClaw rebuilt in Go — with multi-tenant isolation, 5-layer security, and native concurrency. Deploy AI agent teams at.
- [MaxMiksa/Autonomous-Company](https://github.com/MaxMiksa/Autonomous-Company) - AI company framework for continuous autonomous work: 14 AI agent role definitions that research, decide, and code within human-configured goals.
- [jnMetaCode/agency-orchestrator](https://github.com/jnMetaCode/agency-orchestrator) - 🚀 One sentence → your one-person company of AI experts → complete deliverable in minutes. 276 CN + 184 EN + 5 more languages (ko/ru/pt-BR/id.
- [777genius/agent-teams-ai](https://github.com/777genius/agent-teams-ai) - You're the boss, agents are your team. They handle tasks on their own, message each other, and review each other's work. You just watch the.
- [nrslib/takt](https://github.com/nrslib/takt) - TAKT Agent Koordination Topology - Define how AI agents coordinate, where humans intervene, and what gets recorded — in YAML.

**Visual & low-code builders**

- [langgenius/dify](https://github.com/langgenius/dify) - Visual builder for agentic workflows and RAG pipelines with a rich tool ecosystem.
- [langflow-ai/langflow](https://github.com/langflow-ai/langflow) - Drag-and-drop builder for LangChain flows and agents.
- [inkeep/agents](https://github.com/inkeep/agents) - Build agents in a visual builder or TypeScript SDK with two-way sync.
- [botpress/botpress](https://github.com/botpress/botpress) - Open-source hub to build and deploy GPT/LLM agents.
- [dust-tt/dust](https://github.com/dust-tt/dust) - Custom AI agent platform to speed up knowledge work.
- [i-am-bee/agentstack](https://github.com/i-am-bee/agentstack) - Deploy and share agents on open infrastructure, free from vendor lock-in.
- [paradigmxyz/centaur](https://github.com/paradigmxyz/centaur) - Frontier agentic infrastructure you own; open-source agent cloud.
- [coze-dev/coze-studio](https://github.com/coze-dev/coze-studio) - An AI agent development platform with all-in-one visual tools, simplifying agent creation, debugging, and deployment like never before. Coze.
- [melih-unsal/DemoGPT](https://github.com/melih-unsal/DemoGPT) - 🤖 Create agentic apps in a second with your prompts. Everything you need to create an LLM Agent - tools, prompts, frameworks, and models - a.

**Agent protocols & interoperability**

- [a2aproject/a2a-js](https://github.com/a2aproject/a2a-js) - Official JavaScript SDK for the Agent2Agent (A2A) protocol.
- [a2aproject/a2a-python](https://github.com/a2aproject/a2a-python) - Official Python SDK for the Agent2Agent (A2A) protocol.
- [a2aproject/a2a-go](https://github.com/a2aproject/a2a-go) - Official Go SDK for the Agent2Agent (A2A) interoperability protocol.
- [agent-network-protocol/AgentNetworkProtocol](https://github.com/agent-network-protocol/AgentNetworkProtocol) - Open protocol for agent communication, discovery, and identity.
- [agntcy/dir](https://github.com/agntcy/dir) - Distributed announce and discovery service for multi-agent systems.
- [agntcy/oasf](https://github.com/agntcy/oasf) - Open Agentic Schema Framework for interoperable agent definitions.
- [Coral-Protocol/coral-server](https://github.com/Coral-Protocol/coral-server) - CoralOS: registry, runtime, and payments between your agents and production.
- [fetchai/uAgents](https://github.com/fetchai/uAgents) - Fast, lightweight framework for decentralized autonomous agents.
- [google-agentic-commerce/AP2](https://github.com/google-agentic-commerce/AP2) - Google's open protocol for secure, interoperable agent payments.
- [projnanda/adapter](https://github.com/projnanda/adapter) - SDK for building agents on MIT's NANDA Internet-of-Agents network.
- [valory-xyz/open-autonomy](https://github.com/valory-xyz/open-autonomy) - Framework for creating autonomous agent services.
- [a2aproject/A2A](https://github.com/a2aproject/A2A) - Agent2Agent (A2A) is an open protocol enabling communication and interoperability between opaque agentic applications.
- [a2aproject/A2A](https://github.com/a2aproject/A2A) - Agent2Agent (A2A) is an open protocol enabling communication and interoperability between opaque agentic applications.
- [GetBindu/Bindu](https://github.com/GetBindu/Bindu) - Bindu: The identity, communication, and payments layer for AI agents.
- [wang2122/sprix-sage-router](https://github.com/wang2122/sprix-sage-router) - Sprix AI at 屿智同行 — state-aware SELF/COLLABORATE/HANDOFF routing for A2A agent networks.

**Durable execution & background agents**

- [temporalio/temporal](https://github.com/temporalio/temporal) - Durable workflow engine; the right way to run long-lived agents that must survive crashes.
- [inngest/inngest](https://github.com/inngest/inngest) - Event-driven durable functions with first-class AI step support.
- [conductor-oss/conductor](https://github.com/conductor-oss/conductor) - Conductor is an event driven agentic workflow engine providing durable and highly resilient execution engine for applications and AI Agents.
- [julep-ai/julep](https://github.com/julep-ai/julep) - Durable, composable AI agents with crash-and-resume flows.
- [loopx-project/loopx](https://github.com/loopx-project/loopx) - Control plane with durable state kernel for long-horizon agents.
- [restatedev/restate](https://github.com/restatedev/restate) - Resilient applications with durable workflows that tolerate any failure.
- [ThousandBirdsInc/chidori](https://github.com/ThousandBirdsInc/chidori) - Agent framework where every run is durable, replayable and resumable.

**Azure AI Foundry**

- [Azure-Samples/get-started-with-ai-agents](https://github.com/Azure-Samples/get-started-with-ai-agents) - Deploy an agent web app with Azure AI Foundry.
- [Azure-Samples/app-service-agentic-langgraph-foundry-python](https://github.com/Azure-Samples/app-service-agentic-langgraph-foundry-python) - LangGraph + Foundry agents on App Service.
- [MSFT-Innovation-Hub-India/LangGraph-Foundry-HostedAgent-TravelAgent](https://github.com/MSFT-Innovation-Hub-India/LangGraph-Foundry-HostedAgent-TravelAgent) - Multi-agent customer support as a hosted Foundry agent.
- [scholarly360/From-Zero-to-Microsoft-Foundry-Creating-Agents-Via-AI-Projects-Library](https://github.com/scholarly360/From-Zero-to-Microsoft-Foundry-Creating-Agents-Via-AI-Projects-Library) - Agents via the Azure AI Projects SDK.
- [google-antigravity/antigravity-sdk-python](https://github.com/google-antigravity/antigravity-sdk-python) - A Python library for building AI agents that leverage the full power of Google Antigravity.
- [YGYOOO/WorldX](https://github.com/YGYOOO/WorldX) - One sentence creates an AI-driven world — generate maps, characters, and watch stories emerge on their own. 一句话生成一个AI自主驱动的世界.
- [Fei2411/DeepSeek-Bot](https://github.com/Fei2411/DeepSeek-Bot) - A team of long-lived bots for DeepSeek Harness, with main bots, bot-to-bot messages and group chats.

- [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) - A framework for building agentic apps.
- [openJiuwen-ai/jiuwenswarm](https://github.com/openJiuwen-ai/jiuwenswarm) - Intelligent AI agent built on openJiuwen; brings LLM capabilities to your fingertips.
- [onestardao/WFGY](https://github.com/onestardao/WFGY) - Open-source framework for AI reasoning, RAG, agents, and real-world workflows.
- [Fei2411/DeepSeek-Bot](https://github.com/Fei2411/DeepSeek-Bot) - A team of long-lived bots for DeepSeek Harness, with main bots, bot-to-bot messages and group chats.
- [MaxMiksa/Autonomous-Company](https://github.com/MaxMiksa/Autonomous-Company) - An autonomous company working 24/7 on your own PC - Windows/Linux/macOS.
- [wanikua/danghuangshang](https://github.com/wanikua/danghuangshang) - Open-source multi-agent collaboration system inspired by Chinese governance — deploy and coordinate specialized AI agents with OpenClaw.
- [4thfever/cultivation-world-simulator](https://github.com/4thfever/cultivation-world-simulator) - 基于 AI Agent 工作流的修仙世界模拟器，旨在还原智能、开放的仙侠世界。| An open-source Cultivation World Simulator using Agentic Workflow to create a dynamic, emerging Xia.
- [hyperspaceai/agi](https://github.com/hyperspaceai/agi) - The first distributed AGI system. Thousands of autonomous AI agents collaboratively train models, share experiments via P2P gossip, and push.
- [google/agentmesh](https://github.com/google/agentmesh) - Google's open framework for building multi-agent systems with mesh-style orchestration.
- [google-research/harness2](https://github.com/google-research/harness2) - Framework that optimizes the prompts, tools, memory and orchestration around a model.
- [open-gitagent/opengap](https://github.com/open-gitagent/opengap) - Git-native standard for portable AI agent definitions that export to major frameworks.
- [Ryder-Sun/Meldwork](https://github.com/Ryder-Sun/Meldwork) - Local-first desktop app that orchestrates Codex, Claude Code, Gemini CLI and other agents.
- [apache/maka](https://github.com/apache/maka) - Apache Maka (incubating): high-performance agent workspace with a complete record of every interaction.
- [docker/docker-agent](https://github.com/docker/docker-agent) - AI agent builder and runtime by Docker Engineering.
- [Alpha-Dojo/DojoAgents](https://github.com/Alpha-Dojo/DojoAgents) - Framework for training and testing agents.
- [agentuniverse-ai/agentUniverse](https://github.com/agentuniverse-ai/agentUniverse) - agentUniverse is a LLM multi-agent framework that allows developers to easily build multi-agent applications.
- [nightly-labs/openbot](https://github.com/nightly-labs/openbot) - A local-first desktop workspace for persistent AI teammates. Run Codex, Claude, and Grok with dedicated workspaces, task queues, file.
- [AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot) - AI agent assistant and development framework integrating many messaging platforms.
- [kdlbs/kandev](https://github.com/kdlbs/kandev) - AI kanban and development environment that orchestrates multiple agents.

## Memory & Persistent Context

*Agents forget between sessions unless you give them somewhere to remember.*

**Memory layers & frameworks**

- [mem0ai/mem0](https://github.com/mem0ai/mem0) - Drop-in memory layer for agents and apps.
- [letta-ai/letta](https://github.com/letta-ai/letta) - Stateful agents with self-editing memory (formerly MemGPT).
- [getzep/graphiti](https://github.com/getzep/graphiti) - Temporal knowledge graphs for agent memory.
- [topoteretes/cognee](https://github.com/topoteretes/cognee) - Memory built from knowledge graphs plus vector search.
- [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) - Memory and context engine + app that is extremely fast, scalable, and can be run fully locally. The Memory API for the AI era.
- [MemTensor/MemOS](https://github.com/MemTensor/MemOS) - Self-evolving memory OS for LLM & AI Agents: ultra-persistent memory, hybrid-retrieval, and.
- [volcengine/OpenViking](https://github.com/volcengine/OpenViking) - Self-evolving Context Database for AI Agents. Unify Agent Memory, Knowledge RAG and Skills.
- [TencentCloud/TencentDB-Agent-Memory](https://github.com/TencentCloud/TencentDB-Agent-Memory) - TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs.
- [memodb-io/memobase](https://github.com/memodb-io/memobase) - User Profile-Based Long-Term Memory for AI Chatbot Applications.
- [MemPalace/mempalace](https://github.com/MemPalace/mempalace) - The best-benchmarked open-source AI memory system. And it's free.
- [getzep/zep](https://github.com/getzep/zep) - Zep | Examples, Integrations, & More.
- [MemMachine/MemMachine](https://github.com/MemMachine/MemMachine) - Open-source long-term memory layer for AI agents with MCP server support.
- [langchain-ai/langmem](https://github.com/langchain-ai/langmem) - Long-term memory SDK for agents.
- [memvid/memvid](https://github.com/memvid/memvid) - Single-file memory layer for AI agents in Rust with ultra-low-latency recall.
- [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight) - Hindsight: agent memory that learns from outcomes.
- [MemoriLabs/Memori](https://github.com/MemoriLabs/Memori) - Agent-native memory infrastructure: an LLM-agnostic memory layer.
- [NevaMind-AI/memU](https://github.com/NevaMind-AI/memU) - Personal memory across agents.
- [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) - One portable, local-first memory layer for every AI agent.
- [plastic-labs/honcho](https://github.com/plastic-labs/honcho) - Memory library for building stateful agents.
- [aiming-lab/SimpleMem](https://github.com/aiming-lab/SimpleMem) - [ICML'26] SimpleMem: efficient lifelong memory for LLM agents.
- [memodb-io/Acontext](https://github.com/memodb-io/Acontext) - Agent Skills as a Memory Layer.
- [BAI-LAB/MemoryOS](https://github.com/BAI-LAB/MemoryOS) - [EMNLP 2025] MemoryOS: a memory operating system for personalized AI.
- [kayba-ai/agentic-context-engine](https://github.com/kayba-ai/agentic-context-engine) - Make your agents learn from experience.
- [import-ai/omnibox](https://github.com/import-ai/omnibox) - Anywhere, anything to memory, memory to anything.
- [ClaudioDrews/memory-os](https://github.com/ClaudioDrews/memory-os) - A 7-layer memory operating system for persistent agent memory.
- [kitfunso/hippo-memory](https://github.com/kitfunso/hippo-memory) - Biologically-inspired memory for AI agents with decay and retrieval strength.
- [agiresearch/A-mem](https://github.com/agiresearch/A-mem) - A-MEM: Agentic Memory for LLM Agents.
- [FjgarciaMac/AIrecall](https://github.com/FjgarciaMac/AIrecall) - Drop-in long-term memory layer for AI agents: episodic plus semantic.
- [Siddhant-K-code/distill](https://github.com/Siddhant-K-code/distill) - Context intelligence layer for LLM agents with persistent memory.
- [kael-bit/engram-rs](https://github.com/kael-bit/engram-rs) - Memory engine for AI agents with a 3-layer time-decay axis.
- [spectrayan/spector](https://github.com/spectrayan/spector) - Memory backbone for AI agents: four-tier working, episodic, semantic store.
- [Kyros-494/kyros-ai](https://github.com/Kyros-494/kyros-ai) - Kyros: the memory OS for AI agents, secure and self-hosted.
- [zensation-ai/zenbrain](https://github.com/zensation-ai/zenbrain) - Agent memory for LLM agents with 7 neuroscience-inspired layers.
- [dog-last/E-mem](https://github.com/dog-last/E-mem) - [ICML 2026] E-mem: multi-agent episodic context reconstruction.
- [alibaizhanov/mengram](https://github.com/alibaizhanov/mengram) - Human-like memory for AI agents: semantic, episodic, and procedural.
- [memseekai/memseek](https://github.com/memseekai/memseek) - Open source declarative context engine for AI agents.
- [moorcheh-ai/memanto](https://github.com/moorcheh-ai/memanto) - Memory layer for AI agents.
- [Mirix-AI/MIRIX](https://github.com/Mirix-AI/MIRIX) - Multi-agent personal assistant with long-term memory of on-screen activity.
- [FlowElement-xinliuyuansu/m_flow](https://github.com/FlowElement-xinliuyuansu/m_flow) - Bio-inspired cognitive memory engine for graph RAG.
- [neo4j-labs/agent-memory](https://github.com/neo4j-labs/agent-memory) - Graph-native memory system for AI agents backed by Neo4j.
- [tigerless-labs/agent-memory](https://github.com/tigerless-labs/agent-memory) - Long-term agent memory runtime with Markdown as the source of truth.
- [yuzi001a/hippocampus-memory](https://github.com/yuzi001a/hippocampus-memory) - Local-first, source-preserving long-term memory runtime for agents.
- [xzf-thu/VoiceMem](https://github.com/xzf-thu/VoiceMem) - Infrastructure for the next generation of voice agents, designed to provide universal memory. It is divided into a left brain and a right br.

**Memory for coding agents**

- [lucasrosati/claude-code-memory-setup](https://github.com/lucasrosati/claude-code-memory-setup) - Obsidian plus Graphify persistent memory setup for Claude Code.
- [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) - Persistent cross-session context for Claude Code and other agents.
- [rohitg00/agentmemory](https://github.com/rohitg00/agentmemory) - Persistent memory for coding agents, benchmarked on real workloads.
- [CaviraOSS/LongMemory](https://github.com/CaviraOSS/LongMemory) - Local persistent memory store for LLM applications including claude desktop, github copilot, codex, antigravity, etc.
- [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) - Long-term memory for agent coding CLIs with cross-vendor handoff.
- [mex-memory/mex](https://github.com/mex-memory/mex) - Team memory for engineers and their AI agents, living in your repo.
- [tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem) - OpenCode plugin giving coding agents persistent memory locally.
- [0xK3vin/MegaMemory](https://github.com/0xK3vin/MegaMemory) - Persistent project knowledge graph for coding agents via MCP.
- [jaredrhod/ai-memory-vault](https://github.com/jaredrhod/ai-memory-vault) - Give your AI a real, persistent memory.
- [okf-memory/okf-agent-memory](https://github.com/okf-memory/okf-agent-memory) - Git-native persistent memory for AI coding agents.
- [DragonShadows1978/AI-AfterImage](https://github.com/DragonShadows1978/AI-AfterImage) - Episodic memory for AI coding agents: recall of code and decisions.
- [dvquy13/qrec](https://github.com/dvquy13/qrec) - Session recall engine: persistent daemon with BM25 plus vector hybrid.
- [zilliztech/memsearch](https://github.com/zilliztech/memsearch) - Persistent unified memory layer shared across Claude Code, Codex and other agents.
- [vshulcz/deja-vu](https://github.com/vshulcz/deja-vu) - Searchable session history memory for coding agents.
- [cytostack/openwolf](https://github.com/cytostack/openwolf) - Portable project memory across Claude Code, Codex and OpenCode with to