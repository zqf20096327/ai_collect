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
  <a href="https://tayyabimam1.github.io/awesome-ai-agent-stack/"><img src=".github/site-preview.jpg" alt="The Awesome AI Agent Stack website: 6,000+ tools in 29 categories, ranked by GitHub stars" width="860"></a>
</p>

**6,000+ tools across 29 categories, ranked by GitHub stars.** Each section is split into sub-groups by what the tools do. Every entry passes a mechanical bar: real, public, not archived, and actively maintained (pushed in the last 12 months); new additions also need 1,000+ stars. Every link is re-checked against the GitHub API, and projects under 10,000 stars that stop being maintained are pruned. Organized as a **stack** so you can find the right tool for each layer of an agent system.

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
- [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) - Terminal coding agent with anchored edits and subagents.
- [CodebuffAI/freebuff](https://github.com/CodebuffAI/freebuff) - Free AI coding agent for the terminal.
- [CommandCodeAI/command-code](https://github.com/CommandCodeAI/command-code) - Terminal coding agent supporting multiple model providers.
- [dhanji/g3](https://github.com/dhanji/g3) - Minimal terminal coding agent with multi-model support.
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
- [claude-code-best/claude-code](https://github.com/claude-code-best/claude-code) - Runnable and debuggable build of the Claude Code terminal agent.
- [zai-org/ZCode](https://github.com/zai-org/ZCode) - Extensible coding agent harness from Z.ai.
- [anus-dev/ANUS](https://github.com/anus-dev/ANUS) - Terminal coding agent that runs on whichever free model is currently available.
- [shareAI-lab/Kode-CLI](https://github.com/shareAI-lab/Kode-CLI) - Terminal AI agent aimed at general human and computer tasks.
- [iflow-ai/iflow-cli](https://github.com/iflow-ai/iflow-cli) - Terminal-based coding agent for repository analysis and task automation.
- [DSH-APP/DSHA](https://github.com/DSH-APP/DSHA) - Run DeepSeek harness and Ubuntu environment on Android without root.
- [huggingface/tau](https://github.com/huggingface/tau) - Python port of Pi's minimalist coding agent.
- [google-antigravity/antigravity-cli](https://github.com/google-antigravity/antigravity-cli) - Terminal CLI that brings the Antigravity agent harness to the command line.
- [1rgs/nanocode](https://github.com/1rgs/nanocode) - Minimalist terminal-based coding agent harness.
- [itayinbarr/little-coder](https://github.com/itayinbarr/little-coder) - Coding agent harness tuned for smaller local LLMs.
- [tanbiralam/claude-code](https://github.com/tanbiralam/claude-code) - Terminal-based agentic coding tool for codebase navigation and task automation.
- [getkimchi/kimchi](https://github.com/getkimchi/kimchi) - Terminal coding agent with multi-model orchestration.
- [MiniMax-AI/minimax-code](https://github.com/MiniMax-AI/minimax-code) - Open-source terminal coding agent powered by MiniMax.
- [microsoft/intelligent-terminal](https://github.com/microsoft/intelligent-terminal) - Fork of Windows Terminal with native agent integration through the Agent Client Protocol.
- [lessweb/deepcode-cli](https://github.com/lessweb/deepcode-cli) - Terminal coding assistant optimized for DeepSeek V4 with reasoning-effort control and Agent Skills.
- [AntigmaLabs/ante](https://github.com/AntigmaLabs/ante) - Self-contained Rust terminal agent harness, similar to Claude Code or Codex but model-agnostic.
- [Doorman11991/smallcode](https://github.com/Doorman11991/smallcode) - AI coding agent optimized for small LLMs, scoring 87% on a benchmark with a 4B-active model.
- [Dicklesworthstone/pi_agent_rust](https://github.com/Dicklesworthstone/pi_agent_rust) - High-performance AI coding agent CLI written in Rust with zero unsafe code.
- [StartupHakk/OpenMonoAgent.ai](https://github.com/StartupHakk/OpenMonoAgent.ai) - Terminal-native coding agent powered by local LLMs, free and open source.
- [Twigpine/zero](https://github.com/Twigpine/zero) - Terminal coding agent you control, working with your choice of model on your machine.
- [lorryjovens-hub/claude-code-rust](https://github.com/lorryjovens-hub/claude-code-rust) - High-performance Rust implementation of Claude Code.
- [proxysoul/Empryo](https://github.com/proxysoul/Empryo) - AI coding harness for desktop, terminal and CI that edits code by symbol via AST and LSP.
- [dirac-run/dirac](https://github.com/dirac-run/dirac) - Coding agent focused on efficiency and context curation, using hash-anchored edits.
- [yusufcanb/tlm](https://github.com/yusufcanb/tlm) - A local CLI copilot powered by Ollama.
- [tontinton/maki](https://github.com/tontinton/maki) - Efficient AI coding agent extendable by neovim-like Lua plugins.
- [laude-institute/headlong](https://github.com/laude-institute/headlong) - A bash-based agent microharness with persistent agency and recursive LLMs.
- [soongenwong/claudecode](https://github.com/soongenwong/claudecode) - Open-source terminal coding agent replicating Claude Code functionality in Rust.
- [dulikaifazr/Cougar-CLI](https://github.com/dulikaifazr/Cougar-CLI) - An AI programming agent for the command line.
- [LiuMengxuan04/MiniCode](https://github.com/LiuMengxuan04/MiniCode) - A lightweight terminal coding assistant with Claude Code-like workflow, tool loop, and TUI architecture.
- [momozi1996/momo-code](https://github.com/momozi1996/momo-code) - AI coding agent that evolves with you.
- [walter-grace/mac-code](https://github.com/walter-grace/mac-code) - A free local AI coding agent running on Apple Silicon as a Claude Code alternative.
- [ConardLi/easy-agent](https://github.com/ConardLi/easy-agent) - Terminal coding agent with sandboxing, MCP, and multiple model support.
- [Harvil1/codeAgent](https://github.com/Harvil1/codeAgent) - Terminal-based coding agent that plans, edits, runs tests, and iterates until tasks complete.
- [pulseaiclub/phi](https://github.com/pulseaiclub/phi) - Fast terminal-based coding agent with RPC plugins, sub-agents, and MCP support.
- [OleksandrChekhovskyi/hax](https://github.com/OleksandrChekhovskyi/hax) - A minimalist, terminal-native coding agent written in C.

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
- [different-ai/openwork](https://github.com/different-ai/openwork) - Open source alternative to Claude Cowork, powered by opencode.
- [YishenTu/claudian](https://github.com/YishenTu/claudian) - Obsidian plugin that embeds Claude Code, Codex and other agents as a collaborator in your vault.
- [github/copilot.vim](https://github.com/github/copilot.vim) - Neovim plugin for GitHub Copilot.
- [conwnet/github1s](https://github.com/conwnet/github1s) - One second to read GitHub code with VS Code.
- [crynta/terax-ai](https://github.com/crynta/terax-ai) - Lightweight terminal-first AI-native development environment built with Tauri.
- [vastsa/PI-Desktop](https://github.com/vastsa/PI-Desktop) - Local-first AI coding agent desktop app built on Electron, a Rust core and the pi agent harness.
- [zhukunpenglinyutong/jetbrains-cc-gui](https://github.com/zhukunpenglinyutong/jetbrains-cc-gui) - JetBrains IDE plugin that provides a GUI for Claude Code and Codex.
- [op7418/CodePilot](https://github.com/op7418/CodePilot) - Electron desktop client for AI agents with any provider, MCP, skills and phone control.
- [get-bb/bb](https://github.com/get-bb/bb) - Agent IDE for working with coding agents such as Claude Code and Codex.
- [omnirush-ai/omnirush-gui](https://github.com/omnirush-ai/omnirush-gui) - Desktop coding agent with free access to frontier models.
- [ThePrimeagen/99](https://github.com/ThePrimeagen/99) - AI agent plugin for Neovim.
- [phodal/auto-dev](https://github.com/phodal/auto-dev) - Multi-agent coding development platform built on Kotlin Multiplatform with IntelliJ integration.
- [kirodotdev/Kiro](https://github.com/kirodotdev/Kiro) - Agentic IDE that works alongside the developer from prototype to production.
- [zgsm-ai/costrict](https://github.com/zgsm-ai/costrict) - Enterprise AI coding assistant with agent, code review and code completion for IDEs.
- [zbirenbaum/copilot.lua](https://github.com/zbirenbaum/copilot.lua) - Neovim plugin for GitHub Copilot providing complete API and auto-completion integration.
- [nickjvandyke/opencode.nvim](https://github.com/nickjvandyke/opencode.nvim) - Neovim plugin to integrate OpenCode LLMs directly into the developer workflow.
- [twinnydotdev/twinny](https://github.com/twinnydotdev/twinny) - VS Code AI coding assistant with agent mode, completion, chat and edits on local or hosted models.
- [opensumi/core](https://github.com/opensumi/core) - Framework for building AI-native IDE products, with an MCP client for tool use.
- [CopilotC-Nvim/CopilotChat.nvim](https://github.com/CopilotC-Nvim/CopilotChat.nvim) - Neovim plugin for chatting with GitHub Copilot.
- [dsh-tauri/deepseek-harness-desktop](https://github.com/dsh-tauri/deepseek-harness-desktop) - Tauri desktop app for DeepSeek Harness with preset plugins and no environment setup.
- [athasdev/athas](https://github.com/athasdev/athas) - Lightweight Tauri code editor with Git support, AI agents and vim keybindings.
- [folke/sidekick.nvim](https://github.com/folke/sidekick.nvim) - Neovim plugin providing AI sidekick integration with Claude Code, Copilot, and Gemini CLI.
- [RAIT-09/obsidian-agent-client](https://github.com/RAIT-09/obsidian-agent-client) - Obsidian plugin that brings ACP agents such as Claude Code, Codex and Gemini CLI into Obsidian.
- [ggml-org/llama.vim](https://github.com/ggml-org/llama.vim) - Vim plugin for LLM-assisted code and text completion.
- [Zoo-Code-Org/Zoo-Code](https://github.com/Zoo-Code-Org/Zoo-Code) - Team of AI coding agents inside your code editor.
- [greggh/claude-code.nvim](https://github.com/greggh/claude-code.nvim) - Neovim plugin for integrating Claude Code AI assistant.
- [xenodium/agent-shell](https://github.com/xenodium/agent-shell) - Brings AI agents to Emacs with native buffers and key bindings via the Agent Client Protocol.
- [px0-ai/px0](https://github.com/px0-ai/px0) - Browser-based IDE for reviewing and editing AI-generated code with Git integration.
- [carlrobertoh/ProxyAI](https://github.com/carlrobertoh/ProxyAI) - An open-source AI copilot plugin for JetBrains IDEs.
- [hanshuaikang/nezha](https://github.com/hanshuaikang/nezha) - Code editor for the AI agents era with multi-agent support.
- [egoist/waku](https://github.com/egoist/waku) - Native app for working with all your coding agents.
- [Rice-dog/code-codex](https://github.com/Rice-dog/code-codex) - Local project file tree and preview companion for Codex Desktop.
- [ggml-org/llama.vscode](https://github.com/ggml-org/llama.vscode) - VS Code extension for LLM-assisted code and text completion.
- [dvdsgl/claude-canvas](https://github.com/dvdsgl/claude-canvas) - Give Claude Code an external monitor for enhanced visualization.
- [chmod777john/swarm-ide](https://github.com/chmod777john/swarm-ide) - IDE built for agent swarms supporting multiple LLMs.
- [milanglacier/minuet-ai.nvim](https://github.com/milanglacier/minuet-ai.nvim) - Neovim plugin for as-you-type code completion from OpenAI, Gemini, Claude, Ollama and more.
- [elirantutia/vibeyard](https://github.com/elirantutia/vibeyard) - The IDE built for AI coding agents.
- [huggingface/llm-vscode](https://github.com/huggingface/llm-vscode) - LLM powered development extension for VSCode.
- [ai-genie/chatgpt-vscode](https://github.com/ai-genie/chatgpt-vscode) - VS Code extension providing AI pair programming.
- [aicodeking/pandacode](https://github.com/aicodeking/pandacode) - Desktop workspace for coding agents.
- [Oleafly/Oleafly](https://github.com/Oleafly/Oleafly) - LaTeX and Typst editor with live collaboration and AI agents.
- [Kc1t/alethe-agents](https://github.com/Kc1t/alethe-agents) - Desktop workspace for managing multiple coding agents and shells.
- [huggingface/llm.nvim](https://github.com/huggingface/llm.nvim) - LLM-powered development plugin for Neovim.
- [madox2/vim-ai](https://github.com/madox2/vim-ai) - AI-powered code assistant for Vim and Neovim.
- [DeepMyst/Mysti](https://github.com/DeepMyst/Mysti) - AI coding agent team for VS Code where Claude Code and OpenAI Codex collaborate on solutions.
- [paean-ai/deeptide](https://github.com/paean-ai/deeptide) - Swift-native macOS coding agent built by DeepSeek.
- [alishobeiri/thread-notebook](https://github.com/alishobeiri/thread-notebook) - AI-powered Jupyter Notebook for generating code and chatting with data.
- [alchaincyf/fanbox](https://github.com/alchaincyf/fanbox) - A cockpit for vibe coding with file browsing, command agents, and change tracking.

**Autonomous software engineers**

- [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) - Autonomous software-development agent platform with sandboxed execution.
- [aaif-goose/goose](https://github.com/aaif-goose/goose) - Extensible open-source agent that installs, runs and tests code with any LLM.
- [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) - The project that started the autonomous-agent wave; now a platform for building agents.
- [ai-christianson/RA.Aid](https://github.com/ai-christianson/RA.Aid) - Autonomous dev agent that plans, edits, and validates.
- [AndyMik90/Aperant](https://github.com/AndyMik90/Aperant) - Autonomous multi-session AI coding with verification.
- [aws-samples/remote-swe-agents](https://github.com/aws-samples/remote-swe-agents) - AWS samples for running SWE agents remotely.
- [bytedance/trae-agent](https://github.com/bytedance/trae-agent) - ByteDance's software engineering agent for repo tasks.
- [open-inspect/background-agents](https://github.com/open-inspect/background-agents) - Self-hosted background coding system for repo tasks.
- [HKUDS/DeepCode](https://github.com/HKUDS/DeepCode) - Agentic coding system turning specs into code and sites.
- [imbue-ai/sculptor](https://github.com/imbue-ai/sculptor) - Imbue's coding agent with verification harnesses.
- [langchain-ai/open-swe](https://github.com/langchain-ai/open-swe) - Async coding agent working tasks in isolated environments.
- [PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent) - Self-improving coding agent for long-running tasks.
- [Pythagora-io/gpt-pilot](https://github.com/Pythagora-io/gpt-pilot) - AI developer that plans, writes, and debugs whole apps.
- [SWE-agent/SWE-agent](https://github.com/SWE-agent/SWE-agent) - Autonomous agent that resolves real GitHub issues.
- [chaitin/MonkeyCode](https://github.com/chaitin/MonkeyCode) - AI coding platform for teams.
- [algorithmicsuperintelligence/openevolve](https://github.com/algorithmicsuperintelligence/openevolve) - Open-source implementation of AlphaEvolve, an evolutionary coding agent for program discovery.
- [kuafuai/DevOpsGPT](https://github.com/kuafuai/DevOpsGPT) - Multi-agent system that turns natural-language requirements into working software.
- [AutoCodeRoverSG/auto-code-rover](https://github.com/AutoCodeRoverSG/auto-code-rover) - Autonomous software engineer that improves codebases using project structure awareness.
- [yologdev/yoyo-evolve](https://github.com/yologdev/yoyo-evolve) - Coding agent that evolves its own source code with every commit agent-written and test-gated.
- [magiksoft/aider-desk](https://github.com/magiksoft/aider-desk) - Platform for AI-powered software engineers.
- [ntegrals/10x](https://github.com/ntegrals/10x) - Open-source agent that speeds AI coding with smart model routing.
- [strongdm/attractor](https://github.com/strongdm/attractor) - A non-interactive coding agent for use in a software factory.
- [EuniAI/Prometheus](https://github.com/EuniAI/Prometheus) - Knowledge-graph-driven agent that maps, understands, and repairs codebases.
- [Agent-Field/SWE-AF](https://github.com/Agent-Field/SWE-AF) - Autonomous fleet of AI agents that plan, code, test, and ship production-grade pull requests.
- [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) - Autonomous software factory that generates pull requests from GitHub issues or tasks.
- [marcus/nightshift](https://github.com/marcus/nightshift) - Uses leftover LLM budget to autonomously generate useful pull requests.
- [TransformerOptimus/SuperCoder](https://github.com/TransformerOptimus/SuperCoder) - Open-source autonomous software development system that plans and writes code.

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
- [earendil-works/pi](https://github.com/earendil-works/pi) - AI agent toolkit: unified LLM API, agent loop, TUI, coding agent CLI.
- [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) - 🙌 OpenHands: AI-Driven Development.
- [dohooo/helmor](https://github.com/dohooo/helmor) - Open-source local workbench for multi-agent software development.
- [HKUDS/OpenHarness](https://github.com/HKUDS/OpenHarness) - Open agent harness with a built-in personal agent called Ohmo.
- [yc-software/qm](https://github.com/yc-software/qm) - Multiplayer agent harness for work.
- [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) - Agent harness for agentic coding workflows with Claude Code and Codex.
- [OpenBMB/XAgent](https://github.com/OpenBMB/XAgent) - Autonomous LLM agent for solving complex tasks.
- [thirdlayerinc/autoagent](https://github.com/thirdlayerinc/autoagent) - Autonomous harness for engineering tasks.
- [onecli/onecli](https://github.com/onecli/onecli) - Open-source sandboxed agent harness that gives each employee a secured personal agent.
- [Prism-Shadow/penguin-harness](https://github.com/Prism-Shadow/penguin-harness) - Agent harness platform aimed at recursive self-improvement.
- [yb2460/harness-anything](https://github.com/yb2460/harness-anything) - An AI agent control hub for office software and CLI commands.
- [ShenSeanChen/waku-agent](https://github.com/ShenSeanChen/waku-agent) - Local-first Python agent harness with an agent loop, memory and evals in readable code.
- [zhnt/loushang](https://github.com/zhnt/loushang) - AI-native agent harness for coding workflows with multi-model orchestration.
- [AgnesAI-Labs/agnes-harness](https://github.com/AgnesAI-Labs/agnes-harness) - Pluggable agent harness for Forward Deployed Engineering.
- [AMAP-ML/LongHorizon-Harness](https://github.com/AMAP-ML/LongHorizon-Harness) - Harness for long-running computer-use agents with fresh-context runs, durable state and auditing.
- [exoharness/exo](https://github.com/exoharness/exo) - Recursive agent and harness architecture that can safely edit all aspects of itself at runtime.
- [razzant/ouroboros](https://github.com/razzant/ouroboros) - Self-creating autonomous AI agent for general-purpose and coding tasks.
- [openonion/connectonion](https://github.com/openonion/connectonion) - Agent CLI harness for building and running agents from the command line.
- [valkor-ai/loom](https://github.com/valkor-ai/loom) - Loop engineering framework for agentic software delivery.
- [ishaan1013/shadow](https://github.com/ishaan1013/shadow) - Background coding agent and real-time web interface.
- [limecloud/lime](https://github.com/limecloud/lime) - Full-stack AI agent for coding, files, terminals, research and multi-agent workflows.
- [hesamsheikh/octogent](https://github.com/hesamsheikh/octogent) - An orchestration dashboard for managing Claude Code context and automation.
- [huiliyi37/Tianshu-harness](https://github.com/huiliyi37/Tianshu-harness) - A terminal coding agent harness that externalizes goals and state to ensure stable delivery.
- [SaladDay/pi-from-scratch](https://github.com/SaladDay/pi-from-scratch) - 600-line TypeScript implementation of a minimalist AI agent framework.
- [hoangnb24/repository-harness](https://github.com/hoangnb24/repository-harness) - Turns any repo into an agent-ready workspace for coding agents.
- [rasbt/mini-coding-agent](https://github.com/rasbt/mini-coding-agent) - A minimal Python implementation explaining the core components of coding agents.
- [Chorus-AIDLC/Chorus](https://github.com/Chorus-AIDLC/Chorus) - Agent harness for AI-human collaboration and task management.
- [cuga-project/cuga-agent](https://github.com/cuga-project/cuga-agent) - An open-source generalist agent harness for the enterprise supporting complex tasks.
- [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit) - Spec-driven coding harness with multiple agents and skills for autonomous feature development.
- [Onelevenvy/flock](https://github.com/Onelevenvy/flock) - Desktop multi-agent harness in Rust and React, powered by langgraph-rust.
- [pat-jj/harness-1](https://github.com/pat-jj/harness-1) - Recipe for training long-horizon search agents with a stateful harness.
- [wk42worldworld/cybercode](https://github.com/wk42worldworld/cybercode) - An AI agent combining Claude Code coding capabilities with Hermes Agent self-evolution.
- [qiz029/dscode](https://github.com/qiz029/dscode) - A DeepSeek coding agent harness with persistent shell and Chrome MCP integration.

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
- [tempestai-dev/tempest](https://github.com/tempestai-dev/tempest) - Tauri desktop running CLI coding agents in parallel.
- [wainmann/agent-manager](https://github.com/wainmann/agent-manager) - Go TUI running coding agents side by side in tmux.
- [iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi) - Desktop cowork app that runs Claude Code, Codex, OpenCode and other agents.
- [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) - Ghostty-based macOS terminal with vertical tabs and notifications for coding agents.
- [openchamber/openchamber](https://github.com/openchamber/openchamber) - Agentic development environment built on the OpenCode agent.
- [alvinunreal/oh-my-opencode-slim](https://github.com/alvinunreal/oh-my-opencode-slim) - Lean multi-agent suite for OpenCode with model mixing and auto delegation.
- [darrenhinde/OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl) - Plan-first agent framework with approval-gated execution for coding workflows.
- [codeaholicguy/ai-devkit](https://github.com/codeaholicguy/ai-devkit) - Control plane for managing and standardizing AI coding agents.
- [BloopAI/vibe-kanban](https://github.com/BloopAI/vibe-kanban) - Get 10X more out of Claude Code, Codex or any coding agent.
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
- [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) - Layer for Codex CLI that adds hooks, agent teams and HUDs.
- [Gentleman-Programming/gentle-shell](https://github.com/Gentleman-Programming/gentle-shell) - Pi-native workspace for AI-assisted development with parallel coding agents, live tasks, Git diffs, memory and permission controls.
- [spacering-net/codeg](https://github.com/spacering-net/codeg) - Collaborative multi-agent coding workspace aggregating sessions from various coding agents.
- [hardbeat920/monocode](https://github.com/hardbeat920/monocode) - Graphical interface for working with coding agents.
- [code-yeongyu/lazycodex](https://github.com/code-yeongyu/lazycodex) - Agent harness inside Codex that adds project memory, planning, execution and verification.
- [NanmiCoder/dsh-agent-teams](https://github.com/NanmiCoder/dsh-agent-teams) - DeepSeek Harness plugin for multi-agent teams with task assignment and messaging.
- [moazbuilds/CodeMachine-CLI](https://github.com/moazbuilds/CodeMachine-CLI) - Orchestrate AI coding agents into repeatable, long-running workflows from the CLI.
- [supabitapp/supacode](https://github.com/supabitapp/supacode) - Command center for running coding agents in git worktrees.
- [vercel-labs/coding-agent-template](https://github.com/vercel-labs/coding-agent-template) - Multi-agent AI coding platform built on Vercel Sandbox and AI Gateway.
- [reason-machines/reason-network](https://github.com/reason-machines/reason-network) - Engine for multi-agent communication and coordination between coding agents.
- [Dicklesworthstone/agentic_coding_flywheel_setup](https://github.com/Dicklesworthstone/agentic_coding_flywheel_setup) - Bootstraps an Ubuntu VPS into a multi-agent AI coding environment in about 30 minutes.
- [fujibee/agmsg](https://github.com/fujibee/agmsg) - Cross-vendor messaging for CLI coding agents, built with Bash and SQLite.
- [ShawnPana/smux](https://github.com/ShawnPana/smux) - tmux configuration with terminal automation and agent-to-agent communication.
- [cline/kanban](https://github.com/cline/kanban) - Local web app that runs CLI agents in parallel.

**Remote control & session monitoring**

- [amantus-ai/vibetunnel](https://github.com/amantus-ai/vibetunnel) - Share terminal agent sessions over the web.
- [Dimillian/CodexMonitor](https://github.com/Dimillian/CodexMonitor) - macOS menu-bar monitor for Codex CLI sessions.
- [kbwo/ccmanager](https://github.com/kbwo/ccmanager) - Session manager for Claude Code with usage tracking.
- [omnara-ai/omnara](https://github.com/omnara-ai/omnara) - Remote monitoring and control for coding agents.
- [rustykuntz/clideck](https://github.com/rustykuntz/clideck) - Phone-friendly dashboard for CLI coding agents.
- [slopus/happy](https://github.com/slopus/happy) - Mobile client for monitoring Claude Code sessions.
- [soul-sol/agent-watch](https://github.com/soul-sol/agent-watch) - Stall detection for background Claude Code and Codex jobs.
- [tryatlas/atlas](https://github.com/tryatlas/atlas) - Source control for agents that tracks and queries changes from multiple coding agents.
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
- [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) - Web interface for using Hermes Agent from a browser or a phone.
- [its-maestro-baby/maestro](https://github.com/its-maestro-baby/maestro) - Desktop app that runs up to 6 AI coding sessions in parallel, each in its own isolated git worktree.
- [agegr/pi-web](https://github.com/agegr/pi-web) - Web UI for the pi coding agent.
- [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) - Pixel desktop pet that reflects the activity of Claude Code, Codex, Cursor and other coding agents.
- [graykode/abtop](https://github.com/graykode/abtop) - htop-style terminal monitor for Claude Code and Codex CLI sessions, tokens and rate limits.
- [Emanuele-web04/remodex](https://github.com/Emanuele-web04/remodex) - Remote control app for Codex sessions.
- [zarazhangrui/lark-coding-agent-bridge](https://github.com/zarazhangrui/lark-coding-agent-bridge) - Bridge connecting Feishu and Lark messaging with local Claude Code or Codex CLI sessions.
- [overwirehq/claude-code-telegram](https://github.com/overwirehq/claude-code-telegram) - Telegram bot enabling remote access to Claude Code with session persistence and full AI assistance.
- [wxtsky/CodeIsland](https://github.com/wxtsky/CodeIsland) - Notch panel for MacBooks showing live status and approvals for 30+ AI coding tools.
- [Nexting-ai/nexting](https://github.com/Nexting-ai/nexting) - Remote control for Claude Code, Codex, Grok and Cursor sessions from a phone or wearable.
- [devswha/ovis](https://github.com/devswha/ovis) - Browser and phone client for herdr: chat and live terminals for Claude Code, Codex and more.
- [Octane0411/open-vibe-island](https://github.com/Octane0411/open-vibe-island) - Native macOS control center to monitor AI coding agent sessions and approve actions.
- [deepcoldy/botmux](https://github.com/deepcoldy/botmux) - Bridges Feishu/Lark to AI coding CLIs, giving each chat its own live-streaming session.
- [davidondrej/cloudroom](https://github.com/davidondrej/cloudroom) - Cloud-based agent harness for running coding agents in isolated environments.
- [jamro/tiny-engineer](https://github.com/jamro/tiny-engineer) - Desktop robot that visualizes coding-agent activity such as reading, thinking, and writing code.
- [eliasstravik/shepherdr](https://github.com/eliasstravik/shepherdr) - Plugin for running and monitoring many coding agents across machines from a phone, tablet, or desktop.
- [K9i-0/ccpocket](https://github.com/K9i-0/ccpocket) - Mobile client to control Codex and Claude coding agents via WebSocket bridge.
- [marcus/sidecar](https://github.com/marcus/sidecar) - A TUI tool for CLI agents providing diffs, file trees, and task management.

**Account, session & proxy managers**

- [farion1231/cc-switch](https://github.com/farion1231/cc-switch) - Desktop switcher for Claude Code, Codex, OpenCode and friends.
- [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router) - Route Claude Code requests across models and providers.
- [heyhuynhgiabuu/proxypal](https://github.com/heyhuynhgiabuu/proxypal) - Expose your chat subscriptions as local OpenAI-compatible endpoints.
- [badrisnarayanan/antigravity-claude-proxy](https://github.com/badrisnarayanan/antigravity-claude-proxy) - Proxy Antigravity-provided Claude/Gemini models to any client.
- [starbaser/ccproxy](https://github.com/starbaser/ccproxy) - Hook any Claude Code request, modify responses, route custom models.
- [lbjlaq/Antigravity-Manager](https://github.com/lbjlaq/Antigravity-Manager) - Account manager and one-click switcher for Antigravity.
- [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools) - Multi-account manager for AI IDEs such as Cursor, Windsurf and Codex, with quota monitoring.
- [SaladDay/cc-switch-cli](https://github.com/SaladDay/cc-switch-cli) - Cross-platform CLI helper for Claude Code, Codex and Gemini CLI.
- [router-for-me/EasyCLIProxyAPI](https://github.com/router-for-me/EasyCLIProxyAPI) - Desktop GUI for CLIProxyAPI that also auto-configures popular AI agents.
- [farouqaldori/vibe-notch](https://github.com/farouqaldori/vibe-notch) - Minimal macOS session manager for Claude Code notifications without context switching.
- [Draculabo/AntigravityManager](https://github.com/Draculabo/AntigravityManager) - Desktop application to manage accounts and quotas for AI coding tools through a local gateway.
- [numman-ali/cc-mirror](https://github.com/numman-ali/cc-mirror) - Creates isolated Claude Code variants on custom providers such as Z.ai, OpenRouter and LiteLLM.
- [yigitkonur/cli-continues](https://github.com/yigitkonur/cli-continues) - Resumes an AI coding session in another tool such as Claude Code, Codex or Cursor.

**CI & GitHub Actions**

- [anthropics/claude-code-action](https://github.com/anthropics/claude-code-action) - Official Claude Code GitHub Action for CI automation.
- [github/gh-aw](https://github.com/github/gh-aw) - GitHub Agentic Workflows for running agents in CI.
- [google-github-actions/run-gemini-cli](https://github.com/google-github-actions/run-gemini-cli) - GitHub Action running Gemini CLI in workflows.
- [openai/codex-action](https://github.com/openai/codex-action) - Official Codex GitHub Action for automated coding tasks.

**App builders**

- [dyad-sh/dyad](https://github.com/dyad-sh/dyad) - Local desktop AI app builder that iterates on full-stack code.
- [onlook-dev/onlook](https://github.com/onlook-dev/onlook) - Open-source visual editor with AI app generation.
- [Nutlope/llamacoder](https://github.com/Nutlope/llamacoder) - Open-source Claude Artifacts clone generating apps with Llama.
- [abi/screenshot-to-code](https://github.com/abi/screenshot-to-code) - Turn a screenshot into clean HTML/Tailwind/React.
- [wandb/openui](https://github.com/wandb/openui) - Lets you describe a UI in plain text and see it rendered live.
- [cloudflare/vibesdk](https://github.com/cloudflare/vibesdk) - Open-source vibe coding platform for building your own, built on the Cloudflare stack.
- [convex/chef](https://github.com/convex/chef) - AI app builder that generates a full-stack backend and frontend from natural language.
- [anymorph-ai/Claudable](https://github.com/anymorph-ai/Claudable) - Open-source web builder that leverages local CLI coding agents to build and deploy apps.

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
- [storytold/craft-anything](https://github.com/storytold/craft-anything) - See how any website, app or game works, then have AI build your own version: an open-source, clean-room engine in pure Rust.
- [rlaope/oh-my-hermes](https://github.com/rlaope/oh-my-hermes) - The coding harness with Hermes Agent wired into the IDE.
- [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core) - Git. Ship. Done: a spec-driven development core for coding agents.
- [kirodotdev/KiroCrew](https://github.com/kirodotdev/KiroCrew) - A persistent workspace for development work that self-improves and continues beyond one session.
- [ccch1mneyyy/dsh-Go](https://github.com/ccch1mneyyy/dsh-Go) - DeepSeek Harness in your pocket: run dsh on your phone locally, or remote-control your computer.
- [osaurus-ai/osaurus](https://github.com/osaurus-ai/osaurus) - The native macOS harness for AI agents: any model, persistent memory, autonomous operation.
- [egoist/kero](https://github.com/egoist/kero) - A cross-platform native terminal app optimized for agents.
- [liguobao/ds-harness-remote](https://github.com/liguobao/ds-harness-remote) - Remote access to local DSH, Codex, Cursor, and Claude Code workspaces over a low-latency, end-to-end encrypted P2P network.
- [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop) - Lets your CLI agent pick up work in the background and follow it through on its own, only pinging you when a decision is needed.
- [snarktank/ralph](https://github.com/snarktank/ralph) - An autonomous AI agent loop that runs repeatedly until all PRD items are complete.
- [kingcharleslzy-ai/dsh-purge](https://github.com/kingcharleslzy-ai/dsh-purge) - Community-maintained DeepSeek Harness companion: host compatibility, status diagnostics, prompt management, updates and local backup/rollback.
- [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) - An agent-managed museum exhibit, built in Rust with Gajae-Code / LazyCodex, developed and maintained with no human intervention.
- [yynxxxxx/Codex-X](https://github.com/yynxxxxx/Codex-X) - Visual manager for OpenAI Codex desktop/CLI: provider/API switching, session sync, prompt injection, Skills/MCP management, visual TOML config.
- [agentclientprotocol/claude-agent-acp](https://github.com/agentclientprotocol/claude-agent-acp) - Adapter that lets any ACP client use the Claude Agent SDK.

## Skills, Plugins & Context Engineering

*What you put in front of the agent matters more than which agent. Skills, CLAUDE.md files, methodology.*

**Skill frameworks & methodology**

- [obra/superpowers](https://github.com/obra/superpowers) - Agentic skills framework and development methodology (brainstorm → plan → TDD → review).
- [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) - Production-grade engineering skills from Addy Osmani.
- [garrytan/gstack](https://github.com/garrytan/gstack) - Garry Tan's opinionated Claude Code toolset.
- [affaan-m/ECC](https://github.com/affaan-m/ECC) - Harness performance-optimization system: skills, instincts, evals.
- [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) - AI task-management system that drops into Cursor, Claude Code or Lovable.
- [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) - File-based persistent planning for long-running agent tasks.
- [HKUDS/AgentPilot](https://github.com/HKUDS/AgentPilot) - Skill-management layer for agents.
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
- [jnMetaCode/superpowers-zh](https://github.com/jnMetaCode/superpowers-zh) - AI coding superpowers, Chinese enhanced edition: full Chinese localization of the superpowers skills framework (250k+ stars) plus 4 original skills, covering 26 AI coding tools including Claude Code, Copilot CLI, Hermes Agent, Cursor, Windsurf, Kiro and Gemini CLI.
- [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) - Prompt-as-code repository with 530+ image generation examples and reusable skills.
- [diet103/claude-code-infrastructure-showcase](https://github.com/diet103/claude-code-infrastructure-showcase) - Example Claude Code setup showing skill auto-activation, hooks and agents.
- [tw93/Waza](https://github.com/tw93/Waza) - Engineering habits packaged as skills that Claude Code, Codex and Cursor can run.
- [therealXiaomanChu/ex-skill](https://github.com/therealXiaomanChu/ex-skill) - Framework to distill personality traits into AI skills for conversational agents.
- [backnotprop/pstack](https://github.com/backnotprop/pstack) - Skills and principles for rigorous AI-assisted engineering.
- [rebelytics/one-skill-to-rule-them-all](https://github.com/rebelytics/one-skill-to-rule-them-all) - Meta-skill that watches work sessions and turns patterns and corrections into skill improvements.
- [HughYau/qiushi-skill](https://github.com/HughYau/qiushi-skill) - Methodology skills that make agents investigate first, prioritize and validate in practice.
- [foryourhealth111-pixel/Vibe-Skills](https://github.com/foryourhealth111-pixel/Vibe-Skills) - Skill routing and workflow orchestration layer for AI agents, benchmarked on SkillsBench.
- [chaseai-yt/claudex-loop](https://github.com/chaseai-yt/claudex-loop) - Claude Code skill for four-phase plan hardening with Codex review and cross-model build.
- [rpamis/comet](https://github.com/rpamis/comet) - Agent skill harness that turns ideas into evaluated, phase-guarded workflows.
- [mitsuhiko/agent-stuff](https://github.com/mitsuhiko/agent-stuff) - Collection of commands and utilities for use with AI agents.
- [Tiger3807861189/J-Space-Cognition-Suite](https://github.com/Tiger3807861189/J-Space-Cognition-Suite) - A model-agnostic inference-time control suite for deep reasoning and long-horizon work.
- [AMAP-ML/SkillClaw](https://github.com/AMAP-ML/SkillClaw) - Framework for collective skill evolution in agentic systems.
- [yaojingang/yao-meta-skill](https://github.com/yaojingang/yao-meta-skill) - A framework for engineering, evaluating, and governing reusable agent skills with cross-platform portability.
- [UnderleveledBuilder/awesome-short-drama-skills](https://github.com/UnderleveledBuilder/awesome-short-drama-skills) - Curated agent skills for AI short drama creation.
- [RinDig/icm-architect](https://github.com/RinDig/icm-architect) - Agent skill that designs a process as an ICM workspace, using folders as agent architecture.
- [Sahir619/fable-method](https://github.com/Sahir619/fable-method) - Skills distilling a think, act, prove workflow for any model, with an eval to check it.
- [nateherkai/AIS-OS](https://github.com/nateherkai/AIS-OS) - Starter kit of five skills for Claude Code and Codex, built around the Three Ms framework.
- [GBSOSS/skill-from-masters](https://github.com/GBSOSS/skill-from-masters) - Build AI skills using proven domain expert methodologies.
- [michaelshimeles/rstack](https://github.com/michaelshimeles/rstack) - Agent skills and an AGENTS.md workflow template using worktrees, evidence and review loops.
- [LilMGenius/paperthin](https://github.com/LilMGenius/paperthin) - A skillbook on recursive self-improvement for AI coding agents, distilled from harness engineering.
- [skillsgate/skillsgate](https://github.com/skillsgate/skillsgate) - A skills management platform for AI tools.
- [CloudAI-X/claude-workflow-v2](https://github.com/CloudAI-X/claude-workflow-v2) - Claude Code workflow plugin bundling agents, skills, hooks and commands.
- [kerpopule/hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills) - Jev-powered model routing, memory, compaction, skill selection, computer and browser use for Hermes agents.
- [udecode/dotai](https://github.com/udecode/dotai) - Skills for agents compatible with Claude Code, Codex, and Cursor.
- [MoizIbnYousaf/ai-agent-skills](https://github.com/MoizIbnYousaf/ai-agent-skills) - Universal skill installer and package manager for AI coding agents.
- [easyeda/easyeda-api-skill](https://github.com/easyeda/easyeda-api-skill) - Provides EasyEDA Pro API interface and WebSocket bridging for AI programming tools.
- [Jane-xiaoer/claude-skill-web-clone](https://github.com/Jane-xiaoer/claude-skill-web-clone) - Methodology for faithfully cloning any website without hallucinated code.
- [titanwings/ex-skill](https://github.com/titanwings/ex-skill) - Skill generator for persona-based AI agent interactions.
- [NVIDIA-NeMo/Skills](https://github.com/NVIDIA-NeMo/Skills) - Framework for improving and managing skills of large language models.
- [bitjaru/styleseed](https://github.com/bitjaru/styleseed) - Design-method engine for AI coding agents with 22 workflows for design judgment and UI generation.

**Autonomous loops (Ralph)**

- [ClaytonFarr/ralph-playbook](https://github.com/ClaytonFarr/ralph-playbook) - Comprehensive guide to running autonomous AI coding loops with Ralph.
- [frankbria/ralph-claude-code](https://github.com/frankbria/ralph-claude-code) - Autonomous AI development loop for Claude Code with exit detection.
- [mikeyobrien/ralph-orchestrator](https://github.com/mikeyobrien/ralph-orchestrator) - Improved Ralph Wiggum implementation for autonomous agent orchestration.
- [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) - Claude Code skill that repeats modify, verify, keep or discard cycles toward a goal.
- [Forward-Future/loopy](https://github.com/Forward-Future/loopy) - Library of agent loops and an installable skill for designing repeatable agent workflows.
- [leo-lilinxiao/codex-autoresearch](https://github.com/leo-lilinxiao/codex-autoresearch) - Codex skill that loops modify, verify and keep-or-discard cycles, inspired by autoresearch.
- [michaelshimeles/ralphy](https://github.com/michaelshimeles/ralphy) - An autonomous bash script loop running Claude Code and other tools until a PRD is completed.
- [umputun/ralphex](https://github.com/umputun/ralphex) - Extended Ralph loop for autonomous plan execution with coding agents.

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
- [tanweai/pua](https://github.com/tanweai/pua) - High-agency skill that prompts an agent to act like a P8 engineer on a performance improvement plan.
- [QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html) - Agent skill that answers hard questions with a readable one-page HTML.
- [Jakubantalik/transitions.dev](https://github.com/Jakubantalik/transitions.dev) - A library of UI motion transitions designed as a skill for design workflows.
- [drona23/claude-token-efficient](https://github.com/drona23/claude-token-efficient) - Single CLAUDE.md file that keeps Claude responses terse and cuts output verbosity.
- [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) - Writing skill to make AI-generated Chinese text sound natural and human-like.
- [Arekejoker/qwen21-nsfw-pose-skill](https://github.com/Arekejoker/qwen21-nsfw-pose-skill) - Skill package for image generation control using prompts and LoRA.
- [Leonxlnx/unlazy](https://github.com/Leonxlnx/unlazy) - Agent skill implementing the Depth Tree method to prevent model laziness and underthinking.
- [larashero3-dotcom/writing-dna-skill](https://github.com/larashero3-dotcom/writing-dna-skill) - Tool to distill and recreate writing styles as agent skills.
- [DrCatHicks/learning-opportunities](https://github.com/DrCatHicks/learning-opportunities) - Claude and Codex skill for deliberate skill development during AI-assisted coding.
- [DreambigOu/ELI5](https://github.com/DreambigOu/ELI5) - A Claude Code skill that explains complex topics to any audience.
- [yetone/native-feel-skill](https://github.com/yetone/native-feel-skill) - Agent skill for designing cross-platform desktop applications.
- [hexiecs/talk-normal](https://github.com/hexiecs/talk-normal) - System prompt to make LLMs respond in a more natural, human-like way.
- [RobMitt/grill-me-skill](https://github.com/RobMitt/grill-me-skill) - Claude Code skill that interviews the user until shared understanding is reached.
- [alexgreensh/attention-span](https://github.com/alexgreensh/attention-span) - ADHD-friendly output styles that make Claude Code and Codex replies easier to read.
- [snflkd/fluent-korean](https://github.com/snflkd/fluent-korean) - Claude Code output-style plugin that makes responses clear, fluent Korean.
- [yetone/kill-ai-slop](https://github.com/yetone/kill-ai-slop) - A field guide to AI-generated product copy and a skill that scans and removes them.
- [chen0416ccc-cpu/codex-windows-fast-patch-skill](https://github.com/chen0416ccc-cpu/codex-windows-fast-patch-skill) - Skill that restores Codex Desktop patches and feature toggles after Windows upgrades.
- [juliobsz/skills](https://github.com/juliobsz/skills) - An agent skill that builds award-caliber websites from one line.
- [voidful/hung-yi-lee-skill](https://github.com/voidful/hung-yi-lee-skill) - Distills skills from Hung-Yi Lee's teachings, combining with Karpathy's LLM, Fable 5 and GPT6.
- [kharmanskyi/open-steps](https://github.com/kharmanskyi/open-steps) - Plain-language agent skills for Claude Code, Codex, Cursor and Gemini CLI.
- [CharlesWiltgen/Axiom](https://github.com/CharlesWiltgen/Axiom) - Skills for modern xOS development.
- [mohi-devhub/antivibe](https://github.com/mohi-devhub/antivibe) - A skill that turns AI-generated code into educational deep dives.
- [joeseesun/opus-video-prompts](https://github.com/joeseesun/opus-video-prompts) - Collection of 54 copy-ready prompts for generating videos with Claude Opus 5.5 code rendering.
- [theclaymethod/unslop](https://github.com/theclaymethod/unslop) - Agent skill to remove AI-generated slop from writing.
- [karanb192/awesome-claude-code-mods](https://github.com/karanb192/awesome-claude-code-mods) - A collection of 8,000+ Claude Code mods with usage hints.

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
- [openai/skills](https://github.com/openai/skills) - Catalog of reusable agent skills for Codex.
- [huggingface/skills](https://github.com/huggingface/skills) - Agent skills that connect agents to the Hugging Face ecosystem.
- [remotion-dev/skills](https://github.com/remotion-dev/skills) - Agent skills for working with Remotion.
- [BuilderIO/skills](https://github.com/BuilderIO/skills) - Collection of agent skills from Builder.io.
- [davidondrej/skills](https://github.com/davidondrej/skills) - Collection of personal agent skills and behavior-shaping tools.
- [Jakeschincariol/founder-skill](https://github.com/Jakeschincariol/founder-skill) - Eleven free Claude skills that test a business before you launch it.
- [browserbase/skills](https://github.com/browserbase/skills) - Browserbase's official agent skills for accessing the web.
- [google-deepmind/science-skills](https://github.com/google-deepmind/science-skills) - Agent skills that bring AlphaGenome, AFDB, UniProt and 30+ other science databases into workflows.
- [cloudflare/skills](https://github.com/cloudflare/skills) - Skills that teach coding agents how to build on Cloudflare.
- [microsoft/skills](https://github.com/microsoft/skills) - Skills, MCP servers, custom agents and AGENTS.md files that ground coding agents in Microsoft SDKs.
- [typesafe-ai/skills](https://github.com/typesafe-ai/skills) - Agent skills for building with TypeSafe's System One API.
- [badlogic/pi-skills](https://github.com/badlogic/pi-skills) - Skills for the pi coding agent, also usable with Claude Code and Codex CLI.
- [LearnPrompt/awesome-seedance](https://github.com/LearnPrompt/awesome-seedance) - Collection of AI video prompts and installable agent skills.
- [yawiii/ComfyUI-Prompt-Assistant](https://github.com/yawiii/ComfyUI-Prompt-Assistant) - ComfyUI plugin that provides one-click prompt translation, expansion, image captioning, and preset insertion.
- [apify/agent-skills](https://github.com/apify/agent-skills) - Collection of agent skills for working with the Apify platform and Actors.
- [WordPress/agent-skills](https://github.com/WordPress/agent-skills) - Agent skills giving AI coding assistants WordPress knowledge on blocks, themes and plugins.
- [glittercowboy/taches-cc-resources](https://github.com/glittercowboy/taches-cc-resources) - Collection of custom Claude Code resources and commands.
- [YouMind-OpenLab/nano-banana-pro-prompts-recommend-skill](https://github.com/YouMind-OpenLab/nano-banana-pro-prompts-recommend-skill) - AI skill for OpenClaw & Claude Code recommending Nano Banana Pro image prompts.
- [NiazMorshed2007/reanimate](https://github.com/NiazMorshed2007/reanimate) - A Claude Code skill for reverse-engineering animation frames.
- [microsoft/hve-core](https://github.com/microsoft/hve-core) - Microsoft collection of instructions, prompts, agents and skills for GitHub Copilot projects.
- [bevibing/tutor-skills](https://github.com/bevibing/tutor-skills) - Claude Code skill that turns PDFs and codebases into Obsidian study vaults.
- [qdhenry/Claude-Command-Suite](https://github.com/qdhenry/Claude-Command-Suite) - Professional slash commands for Claude Code to streamline software development workflows.
- [viettranx/3dviz-pro-max](https://github.com/viettranx/3dviz-pro-max) - Agent skill that turns ideas into Three.js/Blender 3D scenes.
- [langchain-ai/langchain-skills](https://github.com/langchain-ai/langchain-skills) - A collection of skills for LangChain agents.
- [minsight-ai-info/AI-Search-Hub](https://github.com/minsight-ai-info/AI-Search-Hub) - Aggregates native AI search skills from multiple platforms into a unified agent workflow.
- [Illyism/seo-skills](https://github.com/Illyism/seo-skills) - 30 SEO skills for AI agents like Claude Code, Cursor, and Codex.
- [doggy8088/github-copilot-configs](https://github.com/doggy8088/github-copilot-configs) - Curated GitHub Copilot configurations.
- [BankrBot/skills](https://github.com/BankrBot/skills) - Plug-and-play tools for building powerful agents.
- [getsentry/skills](https://github.com/getsentry/skills) - Agent skills used by the Sentry team for development.
- [forcedotcom/sf-skills](https://github.com/forcedotcom/sf-skills) - Salesforce's curated collection of agent skills for building applications.
- [openclaw/agent-skills](https://github.com/openclaw/agent-skills) - Useful skills for agents and claws.
- [zhnnky329/MathModeling-skills](https://github.com/zhnnky329/MathModeling-skills) - Claude Code skills for math modeling competitions with staged process and Python, MATLAB support.
- [data-goblin/power-bi-agentic-development](https://github.com/data-goblin/power-bi-agentic-development) - Marketplace of Power BI skills and agents for Claude Code and Copilot.
- [google-gemma/gemma-skills](https://github.com/google-gemma/gemma-skills) - Skills for Gemma models to enable agent interactions.
- [new-silvermoon/awesome-android-agent-skills](https://github.com/new-silvermoon/awesome-android-agent-skills) - A collection of standardized agent skills for Android development in tools like Copilot and Cursor.

**Security skills**

- [agamm/claude-code-owasp](https://github.com/agamm/claude-code-owasp) - OWASP Top 10:2025 and ASVS 5.0 secure-coding skill.
- [BehiSecc/VibeSec-Skill](https://github.com/BehiSecc/VibeSec-Skill) - Helps Claude write secure code and prevent common vulnerabilities.
- [gadievron/raptor](https://github.com/gadievron/raptor) - Turns Claude Code into an offensive and defensive security agent.
- [trailofbits/skills](https://github.com/trailofbits/skills) - Trail of Bits skills for security research, vulnerability detection, and audits.
- [anthropics/claude-code-security-review](https://github.com/anthropics/claude-code-security-review) - AI-powered security review GitHub Action that analyzes code changes for vulnerabilities.
- [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector) - Security scanner for AI agent skills: detects vulnerabilities and prompt injection.
- [cso1z/claude-ip-guard](https://github.com/cso1z/claude-ip-guard) - Hook plugin for IP-based access control and account protection.
- [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) - Coding-agent skill for multi-phase security audits with verified findings.
- [SnailSploit/Claude-Red](https://github.com/SnailSploit/Claude-Red) - Library of offensive-security skills for Claude.
- [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) - Skill router pack for reverse engineering and authorized pentesting that installs tools on demand.
- [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) - 817 cybersecurity skills for AI agents mapped to MITRE ATT&CK, NIST and other frameworks.
- [anthropics/defending-code-reference-harness](https://github.com/anthropics/defending-code-reference-harness) - Skills for threat modeling, scanning, triage and patching, plus a customizable scanning harness.
- [ljagiello/ctf-skills](https://github.com/ljagiello/ctf-skills) - Agent skills for solving CTF challenges across web, pwn, crypto, reverse engineering and forensics.
- [cisco-ai-defense/skill-scanner](https://github.com/cisco-ai-defense/skill-scanner) - Security scanner for agent skills.
- [yaklang/hack-skills](https://github.com/yaklang/hack-skills) - Security skills and prompts that teach AI agents practical penetration testing.
- [P4nda0s/reverse-skills](https://github.com/P4nda0s/reverse-skills) - Reverse engineering skills plugin for Claude Code.
- [DUNHKpcc/Claude-Guardian](https://github.com/DUNHKpcc/Claude-Guardian) - Claude Guardian is an all-in-one Claude account safety and risk prevention skill.
- [tanweai/wooyun-legacy](https://github.com/tanweai/wooyun-legacy) - A security analysis skill for Claude Code based on historical Wooyun vulnerability data.
- [utkusen/sast-skills](https://github.com/utkusen/sast-skills) - Collection of agent skills for static application security testing to find vulnerabilities.
- [pashov/skills](https://github.com/pashov/skills) - Security-focused agent skills for Claude Code and AI security research.
- [prompt-security/clawsec](https://github.com/prompt-security/clawsec) - Security skill suite for OpenClaw and Hermes agents with drift detection and audits.

**Domain & workflow skills**

- [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) - Turn any AI agent into an AI Scientist. The #1 Agent Skills library for science, used by.
- [antonbabenko/terraform-skill](https://github.com/antonbabenko/terraform-skill) - Terraform and OpenTofu skill: modules, CI/CD, and production patterns.
- [bradautomates/claude-video](https://github.com/bradautomates/claude-video) - Lets Claude watch any video: downloads, extracts frames, transcribes.
- [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) - Marketing skills: CRO, copywriting, SEO, analytics, and growth.
- [gooseworks-ai/goose-skills](https://github.com/gooseworks-ai/goose-skills) - Growth and GTM skills plus data APIs for Claude Code, Codex, and Cursor.
- [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) - 67 specialized skills turning Claude Code into an expert full-stack pair programmer.
- [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) - 277 plug-and-play AI expert roles for 20+ tools across 20 departments.
- [Li-Evan/BloomTutor](https://github.com/Li-Evan/BloomTutor) - Socratic AI tutor skill grounded in Bloom's 2-sigma research.
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
- [obsidianmd/obsidian-skills](https://github.com/obsidianmd/obsidian-skills) - Agent skills that teach agents to use Obsidian CLI and open file formats.
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
- [Yuan1z0825/nature-skills](https://github.com/Yuan1z0825/nature-skills) - Skills for writing in Nature-paper academic style and producing scientific figures.
- [op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) - Agent skill that generates HTML slide decks in editorial magazine and Swiss layouts.
- [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) - Collection of agent skills for Claude Code, Codex and OpenClaw.
- [KKKKhazix/khazix-skills](https://github.com/KKKKhazix/khazix-skills) - Agent skills for goal setting, analysis and writing, for Claude Code, Codex and 40+ agents.
- [latent-spaces/brag](https://github.com/latent-spaces/brag) - Agent skill that turns your project into a short, shareable launch video with one command.
- [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) - Markdown-only skills for autonomous ML research: cross-model review loops and experiment automation.
- [AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) - Claude Code plugin that files sources into a linked Markdown knowledge base in Obsidian.
- [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) - Codex skills suite for human-in-the-loop academic research workflows.
- [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) - Open-source skills collection covering web design, knowledge retrieval and image generation.
- [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) - Codex skill that generates 16:9 hand-drawn illustrations on white with a few colored annotations.
- [tw93/Kami](https://github.com/tw93/Kami) - Layout rules and templates that let AI agents export PDF, PNG and editable PowerPoint.
- [yizhiyanhua-ai/fireworks-tech-graph](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) - Generates SVG and PNG technical diagrams from natural language, with 7 styles and UML support.
- [WhiteTowerAI/ohmygame](https://github.com/WhiteTowerAI/ohmygame) - The open-source studio for making games with AI. Your own one-person game studio. Everything you need to make games with AI, in one app.
- [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill) - Agent skill that distills anyone's thinking style, decision heuristics and expression DNA.
- [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) - Privacy-first tool to remove AI-generated watermarks from digital content.
- [HKUSTDial/Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) - AI skills that encode a PhD advisor's research experience, from idea to paper submission.
- [zubair-trabzada/geo-seo-claude](https://github.com/zubair-trabzada/geo-seo-claude) - A GEO-first SEO skill for Claude Code.
- [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) - Agent skill that generates HTML pages or slide decks for diagrams, diff reviews and plan audits.
- [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) - Claude Code skill for paid-media audits and account changes across 12 ad platforms.
- [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) - Agent skill that turns text, code, Terraform, SQL and API specs into editable draw.io diagrams.
- [alchaincyf/zhangxuefeng-skill](https://github.com/alchaincyf/zhangxuefeng-skill) - Career planning skill for college entrance and graduate exam guidance.
- [eze-is/web-access](https://github.com/eze-is/web-access) - Skill giving local agents web access through tiered channels, browser CDP and parallel subtasks.
- [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill) - Claude Code skill that supports reverse engineering of Android apps.
- [zenstory-ai/oh-story-claudecode](https://github.com/zenstory-ai/oh-story-claudecode) - Fourteen agent skills for writing Chinese web novels in Claude Code, Codex and OpenCode.
- [Master-cai/Research-Paper-Writing-Skills](https://github.com/Master-cai/Research-Paper-Writing-Skills) - Skill package for writing ML, CV and NLP papers, for Codex, Claude Code and Gemini.
- [op7418/guizang-social-card-skill](https://github.com/op7418/guizang-social-card-skill) - Claude Code and Codex skill that generates Xiaohongshu carousels and WeChat cover pairs.
- [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills) - Product management skills framework for Claude Code, Codex and other AI agents.
- [lingfengQAQ/webnovel-writer](https://github.com/lingfengQAQ/webnovel-writer) - Claude Code-based system for long-form web novels that limits AI forgetting and hallucination.
- [irinabuht12-oss/marketing-skills](https://github.com/irinabuht12-oss/marketing-skills) - 49 marketing skills for Claude Code and claude.ai: Google Ads, Meta Ads, SEO and AI visibility.
- [ningzimu/codex-ppt-skill](https://github.com/ningzimu/codex-ppt-skill) - Skill that generates image-based PowerPoint decks with GPT-Image-2 for Codex and other agents.
- [MengTo/Skills](https://github.com/MengTo/Skills) - Agent skills for designers and builders using Codex, Claude, Cursor and other coding agents.
- [Cocoon-AI/architecture-diagram-generator](https://github.com/Cocoon-AI/architecture-diagram-generator) - Claude skill that generates dark-themed system architecture diagrams as standalone HTML/SVG files.
- [htdt/godogen](https://github.com/htdt/godogen) - Claude Code and Codex skills for autonomous Godot game development.
- [internet-court/internet-court-skill](https://github.com/internet-court/internet-court-skill) - Agent skill for agent-to-agent commerce with payments, escrow and dispute resolution.
- [kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill) - Logo-design skill for AI agents with SVG craft, testing tools and a 1,400+ logo reference library.
- [alchaincyf/huashu-art-motion](https://github.com/alchaincyf/huashu-art-motion) - Provides art animation skills and styles for AI agents.
- [anysearch-ai/anysearch-skill](https://github.com/anysearch-ai/anysearch-skill) - Agent skill for real-time web search, vertical search, batch search and page content extraction.
- [larashero3-dotcom/lieflat-charts](https://github.com/larashero3-dotcom/lieflat-charts) - Agent skill that turns data into interactive HTML charts.
- [SawyerHood/dev-browser](https://github.com/SawyerHood/dev-browser) - Claude skill that lets an agent use a web browser.
- [eternityspring/shuohao-skills](https://github.com/eternityspring/shuohao-skills) - Agent skills for AI short drama production: characters, outlines, scene art, scripts and storyboards.
- [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) - Claude skill that rewrites AI-generated Korean text to read like human writing.
- [s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill) - Agent skill for simplified, rounded IP mascot logos in a subtle neo-skeuomorphic style.
- [twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill) - SwiftUI skill for Claude Code, Codex and other AI coding tools.
- [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) - Claude skill that feeds web pages, videos and PDFs to NotebookLM for podcasts, slides and quizzes.
- [VoltAgent/awesome-codex-subagents](https://github.com/VoltAgent/awesome-codex-subagents) - Collection of 130+ specialized Codex subagents for a range of development tasks.
- [Adkid-Zephyr/anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill) - Agent skill and prompt pack for eliminating defensive writing in academic papers.
- [Hisn00w/ASu-skills](https://github.com/Hisn00w/ASu-skills) - Collection of practical AI skills for job search and development.
- [WUBING2023/PaperSpine](https://github.com/WUBING2023/PaperSpine) - Research agent skill for literature review, analysis, figure generation, and paper drafting.
- [wuyoscar/GPT-Image2-Skill](https://github.com/wuyoscar/GPT-Image2-Skill) - Prompt gallery, agent skill and CLI for OpenAI GPT Image 2 generation and editing.
- [Jakeschincariol/youtube-agent-skill](https://github.com/Jakeschincariol/youtube-agent-skill) - Eleven Claude skills to automate script writing, editing decisions, and optimization for YouTube.
- [antfu/skills](https://github.com/antfu/skills) - Anthony Fu's curated collection of agent skills.
- [zLanqing/codex-claude-academic-skills](https://github.com/zLanqing/codex-claude-academic-skills) - Academic research skills for Claude Code and Codex: paper reading, writing and scientific computing.
- [Dammyjay93/interface-design](https://github.com/Dammyjay93/interface-design) - Design engineering context rules and UI enforcement skills for Claude Code.
- [sergebulaev/linkedin-skills](https://github.com/sergebulaev/linkedin-skills) - Twelve Claude Code and Codex skills for LinkedIn posts, comments and publishing cadence.
- [geeklee/srt-whiteboard-animation](https://github.com/geeklee/srt-whiteboard-animation) - Tool to convert SRT subtitles into hand-drawn whiteboard animation videos.
- [AIScientists-Dev/academic-humanizer](https://github.com/AIScientists-Dev/academic-humanizer) - Skill that strips AI-writing tells from papers and grant proposals while keeping scholarly voice.
- [coleam00/excalidraw-diagram-skill](https://github.com/coleam00/excalidraw-diagram-skill) - Skill to give coding agents the ability to generate Excalidraw diagrams.
- [nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft) - Agent skill for building immersive scroll-driven websites with coding agents.
- [brycewang-stanford/Auto-Empirical-Research-Skills](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills) - Large collection of agent skills for empirical research across eight social science fields.
- [zarazhangrui/beautiful-html-templates](https://github.com/zarazhangrui/beautiful-html-templates) - HTML slide templates designed for coding agents to auto-generate presentation decks.
- [liustack/modlens](https://github.com/liustack/modlens) - Vision plugin for text-only coding agents that turns pasted images into structured JSON.
- [UditAkhourii/adhd](https://github.com/UditAkhourii/adhd) - Coding agent skill that runs pruned tree-of-thought brainstorming with parallel divergent thoughts.
- [dexhunter/seedance2-skill](https://github.com/dexhunter/seedance2-skill) - Skill for writing effective prompts for Seedance 2.0 video generation.
- [nykooi1/vibe-wise](https://github.com/nykooi1/vibe-wise) - Claude Code plugin that explains architectural concepts while AI writes code.
- [isjiamu/gzh-design-skill](https://github.com/isjiamu/gzh-design-skill) - An AI-agent skill that turns Markdown into paste-ready WeChat article HTML.
- [zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills) - Skills for Claude Code and Codex covering short-drama scripts, storyboards and video prompts.
- [aicodeking/leanrea](https://github.com/aicodeking/leanrea) - Lightweight reverse engineering skill for AI coding agents.
- [nowork-studio/notfair-plugin](https://github.com/nowork-studio/notfair-plugin) - Collection of SEO and marketing skills for AI agents.
- [plannotator/effective-html](https://github.com/plannotator/effective-html) - Agent skills for producing HTML artifacts, wireframes, prototypes, plans and diagrams.
- [muxuuu/serenity-skill](https://github.com/muxuuu/serenity-skill) - Agent skill for researching supply-chain bottlenecks and stock investments.
- [GordenSun/GordenPPTSkill](https://github.com/GordenSun/GordenPPTSkill) - Build polished Chinese PPTX files from templates with text-only editing via python-pptx.
- [jangviktor-web/nihaixia](https://github.com/jangviktor-web/nihaixia) - A collection of agent skills for traditional Chinese medicine diagnosis and theory.
- [aldegad/sprite-gen](https://github.com/aldegad/sprite-gen) - Codex and Claude skill that generates 2D game sprites and animation atlases.
- [Dimillian/Skills](https://github.com/Dimillian/Skills) - Collection of custom skills and context files for Codex AI coding agent.
- [jakubkrehel/make-interfaces-feel-better](https://github.com/jakubkrehel/make-interfaces-feel-better) - Agent skill that helps agents build interfaces that feel more polished.
- [AvdLee/SwiftUI-Agent-Skill](https://github.com/AvdLee/SwiftUI-Agent-Skill) - Agent skill with SwiftUI best-practice guidance for AI coding tools.
- [Nanako0129/sepia](https://github.com/Nanako0129/sepia) - De-AI writing skill covering fiction and professional prose for Agent Skills-compatible agents.
- [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) - Agent skills for growth experiments, sales pipeline, content, outbound, SEO and finance.
- [geekjourneyx/md2wechat-skill](https://github.com/geekjourneyx/md2wechat-skill) - Agent-facing CLI and skill for writing, formatting and publishing WeChat Official Account articles.
- [axtonliu/axton-obsidian-visual-skills](https://github.com/axtonliu/axton-obsidian-visual-skills) - Skills that generate Obsidian Canvas, Excalidraw and Mermaid diagrams from text in Claude Code.
- [bergside/awesome-design-skills](https://github.com/bergside/awesome-design-skills) - 67 DESIGN.md and SKILL.md design skill files for Claude, Codex, Cursor and other agents.
- [yanliudesign/mono-color-skill](https://github.com/yanliudesign/mono-color-skill) - Skill for one-ink editorial print imagery with halftone photos, negative space and restrained type.
- [Jakeschincariol/linkedin-agent-skill](https://github.com/Jakeschincariol/linkedin-agent-skill) - Collection of Claude skills for managing L