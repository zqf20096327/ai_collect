# Awesome AI Agents [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> The comprehensive, up-to-date directory of the **AI agent ecosystem** — frameworks and SDKs for building agents, hosted agent platforms, autonomous coding agents, computer-use/GUI agents, multi-agent orchestration, and the infrastructure underneath it all: protocols, evals, memory, observability, marketplaces, security, and sandboxes.

This list tracks every notable product in the space as of **September 2026**. A machine-readable copy lives in [`data/agents.json`](data/agents.json).

> **Scope:** This is the *broad ecosystem* list — the starting point for anything agent-related. It covers single-agent frameworks and SDKs, hosted agent development platforms, autonomous coding agents, and computer-use/GUI agents, alongside the supporting layers (protocols, evals, memory, observability, marketplaces, security, sandboxes). Its Multi-Agent Orchestration section overlaps with two sibling lists: when you want *depth on coordination itself* rather than ecosystem breadth, open [awesome-AI-agent-orchestration](https://github.com/awesome-llms-labs/awesome-AI-agent-orchestration) (the coordination mechanisms: graphs, handoffs, protocols, memory, durable execution) or [awesome-multi-agents-workflow](https://github.com/awesome-llms-labs/awesome-multi-agents-workflow) (multi-agent teams as working systems: crews, supervisor teams, SaaS/cloud platforms, workflow infrastructure).


**Status tags:** `(beta)` = public beta/preview · `(legacy)` = superseded but still around · `(archived)` = repo archived · `(deprecated)` = vendor-retired · `(sunsetting)` = being wound down — avoid for new work · `(maintenance)` = maintenance mode only — avoid for greenfield · `acquired by X` = product continues under new owner

## Contents

- [Agent Frameworks & SDKs](#agent-frameworks--sdks)
- [Agent Development Platforms](#agent-development-platforms)
- [Autonomous Coding Agents](#autonomous-coding-agents)
- [Computer-Use / GUI Agents](#computer-use--gui-agents)
- [Multi-Agent Orchestration](#multi-agent-orchestration)
- [Communication Protocols](#communication-protocols)
- [Evals & Benchmarks](#evals--benchmarks)
- [Agent Memory](#agent-memory)
- [Agent Observability](#agent-observability)
- [Agent Marketplaces](#agent-marketplaces)
- [Agent Security & Guardrails](#agent-security--guardrails)
- [Agent Sandboxes & Tool Platforms](#agent-sandboxes--tool-platforms)
- [Guides](#guides)
- [Status Changes](#status-changes)
- [Related Lists](#related-lists)
- [Contributing](#contributing)
- [License](#license)

---

## Agent Frameworks & SDKs

Libraries and SDKs for building agents — single-agent loops, tool use, and multi-agent coordination.

- [LangChain](https://github.com/langchain-ai/langchain) `OSS` — Foundational LLM app framework: chains, prompts, tools, retrievers.
- [LangGraph](https://langchain-ai.github.io/langgraph/) `OSS` — Graph-based, stateful agent orchestration with checkpointing; supports supervisor, swarm, and hierarchical multi-agent patterns.
- [LlamaIndex](https://developers.llamaindex.ai/) `OSS` — Data framework for RAG-centric agentic systems; event-driven Workflows.
- [Haystack](https://github.com/deepset-ai/haystack) `OSS` — Production NLP pipeline framework from deepset for enterprise document-processing agents.
- [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/overview/) `OSS` — Microsoft's enterprise AI orchestrator (C#, Python, Java).
- [Microsoft Agent Framework](https://aka.ms/agentframework) `OSS` — Converged AutoGen + Semantic Kernel agent stack (Python + .NET).
- [AutoGen](https://github.com/microsoft/autogen) `OSS` `(legacy)` — Microsoft's conversational multi-agent framework; pioneered multi-agent group chat — continued by the community as AG2.
- [AG2](https://docs.ag2.ai/latest/) `OSS` — Community continuation of AutoGen by its original creators; open governance with MCP and A2A support.
- [CrewAI](https://docs.crewai.com) `OSS` — Role-based multi-agent framework; agents, tasks, and crews map to real teams.
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python) `OSS` — Lightweight, handoff-centric agent framework from OpenAI with tracing and guardrails.
- [Google ADK](https://google.github.io/adk-docs/) `OSS` — Google's multi-agent framework with A2A built in; hierarchical agent systems pair with Vertex AI.
- [Amazon Strands Agents](https://github.com/strands-agents/sdk-python) `OSS` — AWS-native composable agent framework.
- [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk) — Anthropic's SDK for building Claude-powered agents; MCP-native with extended thinking (Python and TypeScript SDKs).
- [smolagents](https://github.com/huggingface/smolagents) `OSS` — Hugging Face's minimal, code-first agent library.
- [Pydantic-AI](https://github.com/pydantic/pydantic-ai) `OSS` — Type-safe agent framework from the Pydantic team with validated structured outputs.
- [Agno](https://www.agno.com/) `OSS` — High-performance agent framework with multimodal support; Teams primitive and AgentOS runtime.
- [Mastra](https://github.com/mastra-ai/mastra) `OSS` — TypeScript-first agent framework with built-in memory, evals, RAG, and MCP.
- [Vercel AI SDK](https://github.com/vercel/ai) `OSS` — Streaming-first agent SDK for web apps and agent UIs.
- [MetaGPT](https://github.com/geekan/MetaGPT) `OSS` — Multi-agent software-company simulation with SOPs and typed artifact pub/sub between roles.
- [CAMEL-AI](https://www.camel-ai.org) `OSS` — Communicative-agent framework for role-play and multi-agent research.
- [DSPy](https://dspy.ai/) `OSS` — Declarative programming of LM pipelines with automatic prompt optimization (Stanford NLP).
- [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) `OSS` — The 2023 autonomous-agent pioneer; general-purpose agents that plan and execute tasks.

## Agent Development Platforms

Hosted platforms for building, running, and managing agents — low-code to fully managed runtimes.

- [Vertex AI Agent Builder](https://docs.cloud.google.com/agent-builder/overview) — Google Cloud's managed agent development platform; framework-agnostic runtime with RAG Engine and Google Search grounding.
- [ChatGPT Agent](https://openai.com/index/introducing-chatgpt-agent/) — OpenAI's agentic product for browser automation and long multi-step tasks; absorbed Operator in July 2025.
- [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) `(beta)` — Anthropic's hosted agent execution environment; stateful sessions with sandboxing, no own infra needed.
- [Amazon Bedrock Agents / AgentCore](https://aws.amazon.com/bedrock/agents/) — AWS managed agent service; framework-agnostic, multi-model, with Bedrock Guardrails.
- [Azure AI Foundry](https://ai.azure.com/) — Full-stack AI platform with managed agent runtime for Microsoft-centric shops.
- [Microsoft Copilot Studio](https://copilotstudio.microsoft.com/) — Low-code agent builder for Microsoft 365, Dynamics, and Power Platform.
- [Salesforce Agentforce](https://www.salesforce.com/agentforce/) — CRM-native autonomous agents on live Salesforce data; Atlas Reasoning Engine.
- [Relevance AI](https://relevanceai.com/docs/get-started/introduction) — No-code multi-agent "workforce" builder with a visual canvas; strong in sales/GTM workflows.
- [Lindy](https://www.lindy.ai/) — Template-first no-code AI employees for email, CRM, and calendar; "Agent Swarms" for parallel tasks.
- [Voiceflow](https://www.voiceflow.com) — Omnichannel chat and voice agent design platform; one agent runs across web, app, WhatsApp, SMS, and voice.
- [Botpress](https://botpress.com/) — Long-standing hosted agent creation and deployment platform.
- [Dify](https://github.com/langgenius/dify) `OSS` — Open-source LLMOps platform with visual agent builder and broad plugin marketplace.
- [n8n](https://n8n.io/) `OSS` — Workflow automation with native AI-agent nodes and MCP support; self-hostable.
- [Activepieces](https://github.com/activepieces/activepieces) `OSS` — Open-source AI workflow automation; MCP-server-first automation for agents.
- [Agno AgentOS](https://www.agno.com/) — Hosted and self-hosted agent operating system behind the Agno framework.
- [LiveKit Agents](https://github.com/livekit/agents) `OSS` — Real-time voice agent framework on WebRTC; open source with plugin architecture and MCP support.
- [Zapier Agents](https://zapier.com/agents) — Custom AI teammates inside Zapier automations, grounded in company knowledge.
- [Flowise](https://github.com/FlowiseAI/Flowise) `OSS` `(sunsetting)` — Visual LangChain/LlamaIndex agent builder; sunsetting — do not build on it.

## Autonomous Coding Agents

Agents that write, edit, test, and ship code — terminal CLIs, IDE extensions, and cloud engineers.

- [Claude Code](https://github.com/anthropics/claude-code) — Anthropic's terminal-first agentic coding tool: subagents, hooks, plan mode, MCP.
- [Codex CLI](https://github.com/openai/codex) `OSS` — OpenAI's open-source terminal coding agent; headless `codex exec` and MCP server mode.
- [Cursor](https://cursor.com/) — AI-native IDE with background agents; the IDE agent to beat.
- [GitHub Copilot](https://github.com/features/copilot) — Agent mode and completion across VS Code and JetBrains; BYOK for enterprise.
- [Windsurf](https://windsurf.com/) — Agentic IDE with "Cascade" flow and worktrees.
- [Aider](https://github.com/Aider-AI/aider) `OSS` — Open-source CLI pair-programmer with strong git integration; BYO LLM.
- [Cline](https://github.com/cline/cline) `OSS` — Open-source autonomous coding agent for VS Code; transparent consumption, headless SDK.
- [Continue](https://github.com/continuedev/continue) `OSS` — Open-source, model-agnostic IDE extension agent; Mission Control UI and cloud agents.
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) `OSS` — Google's open-source terminal agent with LSP integration.
- [Devin](https://devin.ai/) — Cognition's autonomous cloud software engineer; CLI and API.
- [Google Jules](https://jules.google) — Asynchronous autonomous coding agent; GitHub-integrated, runs in cloud sandboxes.
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) `OSS` — Open-source "developer control center"; SDK, CLI, GUI, and Agent Canvas.
- [SWE-agent](https://github.com/SWE-agent/SWE-agent) `OSS` — Research-grade automated GitHub-issue solver (Princeton); the academic reference coding agent.
- [opencode](https://github.com/sst/opencode) `OSS` — Open-source terminal AI coding agent (TUI) with plugin support and headless JSON mode.
- [Goose](https://github.com/block/goose) `OSS` — Block's extensible local agent; recipes, MCP-native, Agent Client Protocol support.
- [Roo Code](https://github.com/RooCodeInc/Roo-Code) `OSS` — Autonomous agent extension in the Cline lineage; multi-mode with cloud agents.
- [Kilo Code](https://github.com/Kilo-Org/kilocode) `OSS` — Agentic coding extension for VS Code and JetBrains; multi-mode context and Memory Bank.
- [Crush](https://github.com/charmbracelet/crush) `OSS` — Charmbracelet's TUI coding agent (Go) with multi-model configs.
- [Amp](https://ampcode.com) — Subagent-based coding agent with issue integration; spun off from Sourcegraph as independent Amp Inc. (Dec 2025).
- [OpenClaw](https://github.com/openclaw/openclaw) `OSS` — Self-hosted, always-on assistant harness; chat-reachable and proactive, orchestrates CLI agents.

## Computer-Use / GUI Agents

Agents that operate computers the way humans do — clicking, typing, and seeing screens.

- [Anthropic Computer Use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) `(beta)` — Screenshot→coordinate→action API tool loop; Docker Linux reference environment.
- [Claude in Chrome](https://code.claude.com/docs/en/chrome) — Browser extension that drives the user's installed Chrome.
- [OpenAI CUA](https://openai.com/index/computer-using-agent/) — Computer-Using Agent model via the Responses API `computer` tool; originally powered Operator.
- [ChatGPT Agent](https://openai.com/index/introducing-chatgpt-agent/) — OpenAI's agentic product for browser automation and long multi-step tasks; absorbed Operator in July 2025.
- [OpenAI Operator](https://openai.com/index/introducing-operator/) `(deprecated)` — Standalone browser-automation product (Jan 2025); merged into ChatGPT Agent on July 17, 2025.
- [Browser Use](https://github.com/browser-use/browser-use) `OSS` — Widely-used open-source browser-agent library (Playwright); CLI 2.0 uses the Chrome DevTools Protocol.
- [Skyvern](https://github.com/Skyvern-AI/skyvern) `OSS` — Enterprise browser-RPA replacement; planner-agent-validator architecture.
- [Agent S3 (Simular)](https://www.simular.ai/articles/agent-s3) `OSS` — Full-desktop (macOS/Linux/Windows) and Android GUI agent.
- [OmniParser v2](https://www.microsoft.com/en-us/research/articles/omniparser-v2-turning-any-llm-into-a-computer-use-agent/) `OSS` — Microsoft's vision GUI-grounding module that turns any LLM into a GUI agent; pairs with OmniTool.
- [AIHawk](https://github.com/feder-cr/AIHawk) `OSS` — Job-application automation agent; Firefox-based community project.
- [OSWorld](https://github.com/xlang-ai/OSWorld) `OSS` — Real-computer OS task benchmark/environment across Ubuntu, Windows, and macOS; the standard computer-use benchmark.
- [AndroidWorld](https://github.com/google-research/android_world) `OSS` — Real Android phone-control benchmark from Google Research.

## Multi-Agent Orchestration

Frameworks whose primary abstraction is multi-agent coordination. (Single-agent frameworks with multi-agent modes — LangGraph, AG2, Google ADK, CrewAI, MetaGPT — also appear above.)

- [OpenAI Swarm](https://github.com/openai/swarm) `OSS` `(archived)` — Lightweight educational multi-agent handoff pattern; archived reference implementation — superseded by the OpenAI Agents SDK.
- [DeerFlow](https://github.com/bytedance/deer-flow) `OSS` — ByteDance's long-horizon "SuperAgent" harness with sub-agents and sandboxes.
- [OpenAgents](https://github.com/openagents-org/openagents) `OSS` — Protocol-based multi-agent communication and orchestration platform.
- [ChatDev](https://github.com/OpenBMB/ChatDev) `OSS` — Communicative "virtual software company"; classic chat-chain pipeline.
- [AgentScope](https://github.com/agentscope-ai/agentscope) `OSS` — Alibaba's production-ready multi-agent framework with visual drag-and-drop tooling.
- [Agency Swarm](https://github.com/VRSEN/agency-swarm) `OSS` — Swarms of agents with distinct roles; type-safe tools with auto-validation.
- [Kitaru](https://github.com/zenml-io/kitaru) `OSS` — ZenML's durable execution framework: checkpoints, replay, and stateful flows for long-running agent systems.

---

## Communication Protocols

The standards that let agents talk to tools, to each other, and to frontends.

- [MCP (Model Context Protocol)](https://modelcontextprotocol.io) `OSS` — Standard for connecting agents to tools, data, prompts, and resources; donated to the Linux Foundation (Agentic AI Foundation) in December 2025.
- [A2A (Agent2Agent)](https://a2a-protocol.org) `OSS` — Open protocol for discovery, delegation, and artifacts between opaque agents; Linux Foundation, v1.0.0 spec.
- [ACP (Agent Client Protocol)](https://zed.dev/acp) `OSS` — Connect any editor to any coding agent (Zed); unrelated to IBM's ACP/A2A despite the acronym.
- [AG-UI](https://github.com/ag-ui-protocol/ag-ui) `OSS` — Stream agent state, events, and human interaction into frontends; created by CopilotKit.
- [ANP (Agent Network Protocol)](https://agent-network-protocol.com/) `OSS` — Decentralized agent identity, discovery, and encrypted collaboration (`did:wba`); W3C community group.
- [AP2 (Agent Payments Protocol)](https://ap2-protocol.org) — Scoped, revocable payment authorization for agentic commerce; Google/Stripe-backed mandate protocol.
- [AGENTS.md](https://github.com/agentsmd/agents.md) `OSS` — Portable repo-guidance convention for coding agents; read by OpenCode, Crush, Cline, Cursor, and others.

## Evals & Benchmarks

How the field measures agents — task success, tool-call accuracy, and real-computer benchmarks.

- [AgentBench](https://github.com/THUDM/AgentBench) — Eight-environment holistic agent evaluation (ICLR 2024).
- [GAIA](https://huggingface.co/spaces/gaia-benchmark/leaderboard) — Real-world questions requiring web search, tool use, and reasoning; difficulty tiers.
- [τ-bench](https://github.com/sierra-research/tau-bench) — Customer-support agent eval with realistic tools and a user simulator (Sierra).
- [SWE-bench](https://github.com/swe-bench/SWE-bench) — Resolve real GitHub issues across Python repos; the code-agent gold standard, with a cleaned Verified subset.
- [WebArena](https://github.com/web-arena-x/webarena) — Realistic web tasks across e-commerce, GitLab, and social sites; VisualWebArena adds visual reasoning.
- [OSWorld](https://github.com/xlang-ai/OSWorld) — Real-computer OS task benchmark/environment; the standard computer-use benchmark.
- [BFCL](https://gorilla.cs.berkeley.edu/leaderboard.html) — Berkeley Function Calling Leaderboard; AST-matched tool-call accuracy at scale.
- [ToolBench](https://github.com/OpenBMB/ToolBench) — Tool use across thousands of real APIs (ToolLLM).
- [ClawBench](https://arxiv.org/abs/2604.08523) — Everyday online tasks for AI agents; a 2026 consumer-task benchmark.

## Agent Memory

How agents remember — short-term context, long-term knowledge, and self-editing memory.

- [mem0](https://mem0.ai/) `OSS` — Self-improving memory layer for agents and assistants.
- [Zep](https://www.getzep.com/) — Managed memory on a temporal knowledge graph; community edition deprecated — enterprise continues on the Graphiti engine.
- [Graphiti](https://github.com/getzep/graphiti) `OSS` — Real-time bi-temporal knowledge-graph engine (powers Zep); hybrid semantic + keyword + graph retrieval.
- [Letta](https://github.com/letta-ai/letta-code) `OSS` — Stateful agent platform (ex-MemGPT): self-editing memory blocks; Git-backed context.
- [Cognee](https://www.cognee.ai/) `OSS` — Open-source memory engine; self-hosted knowledge graph via an ECL pipeline.

## Agent Observability

Tracing, debugging, and evaluating agents in development and production.

- [LangSmith](https://www.langchain.com/langsmith) — Tracing, evals, and prompt management for LangChain/LangGraph.
- [Langfuse](https://langfuse.com/) `OSS` — Open-source LLM/agent tracing, evals, and prompt management. 🔀 **Acquired by ClickHouse (Jan 2026).**
- [Arize Phoenix](https://docs.arize.com/phoenix) `OSS` — OTel-native tracing with RAG/agent evaluation; commercial Arize AX on top.
- [Helicone](https://www.helicone.ai/) `(maintenance)` — Proxy-based LLM observability; in maintenance mode since March 2026 — avoid for greenfield.

## Agent Marketplaces

Where agents and agent capabilities get discovered, bought, and distributed.

- [AWS Marketplace — AI Agents & Tools](https://aws.amazon.com/bedrock/agentcore/) — Buy and deploy agents; Bedrock AgentCore-deployable with PAYG, contracts, and private offers.
- [Salesforce AgentExchange](https://www.salesforce.com/agentforce/agentexchange/?bc=OTH) — Partner agent marketplace for the Salesforce ecosystem.
- [Microsoft Copilot Agent Store](https://www.microsoft.com/en-us/microsoft-cloud/blog/2025/09/25/empower-your-workforce-with-agents-in-microsoft-365-copilot/) — Enterprise procurement for Copilot agents inside Microsoft 365.
- [Anthropic Agent Skills](https://agentskills.io) — Open SKILL.md capability-pack spec and ecosystem.

## Agent Security & Guardrails

Keeping agents safe: prompt-injection defense, AI firewalls, model scanning, and programmable guardrails.

- [Lakera Guard](https://www.lakera.ai/lakera-guard) — Real-time prompt-injection and data-leak protection. 🔀 **Acquired by Check Point (Sept 2025).**
- [Robust Intelligence](https://robustintelligence.com) — AI firewall and automated red teaming. 🔀 **Acquired by Cisco.**
- [Protect AI](https://protectai.com) — Model scanning and ML supply-chain security. 🔀 **Acquired by Palo Alto Networks.**
- [NVIDIA NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) `OSS` — Programmable, open-source guardrails toolkit (Colang).

## Agent Sandboxes & Tool Platforms

Isolated execution for agent code, plus the tool-calling platforms that let agents act in the world.

- [E2B](https://e2b.dev) `OSS` — Cloud sandboxes for agent-generated code; desktop (computer-use) sandboxes.
- [Arcade](https://www.arcade.dev) `OSS` — Tool-calling platform with per-user authorization; agents act as the user, not a bot.
- [Composio](https://composio.dev) `OSS` — Managed auth and app integrations as agent tools; skips OAuth plumbing for Gmail, Slack, Jira.
- [Firecracker](https://github.com/firecracker-microvm/firecracker) `OSS` — AWS microVMs; the isolation tech underneath most multi-tenant agent execution platforms.

---

## Guides

- [Choosing an agent framework](docs/choosing-an-agent-framework.md) — how to pick between LangGraph, CrewAI, ADK, the OpenAI Agents SDK, and the rest.
- [Agent protocols](docs/agent-protocols.md) — MCP vs A2A vs ACP vs AG-UI vs ANP vs AP2, and when each matters.
- [Evaluation and observability](docs/evaluation-and-observability.md) — benchmarks, tracing, and what to measure before production.
- [Status changes](docs/status-changes.md) — acquisitions, shutdowns, deprecations, and maintenance-mode entries.
- [Glossary](docs/glossary.md) — the terms this ecosystem can't stop inventing.

## Status Changes

Notable recent churn — see [docs/status-changes.md](docs/status-changes.md) for details:

- OpenAI Operator merged into ChatGPT Agent (Jul 2025); OpenAI Swarm archived (superseded by the OpenAI Agents SDK).
- AutoGen is legacy — the community continues it as AG2; Flowise is sunsetting.
- MCP donated to the Linux Foundation (Dec 2025); IBM's ACP merged into A2A (Aug 2025).
- Langfuse acquired by ClickHouse (Jan 2026); Helicone in maintenance mode (Mar 2026); Zep Community Edition deprecated.
- Lakera Guard → Check Point; Robust Intelligence → Cisco; Protect AI → Palo Alto Networks.

## Related Lists

- [awesome-ai-sandboxes](https://github.com/dakotac1994/awesome-ai-sandboxes) — the deep dive on AI sandboxes and coding-agent sandboxes (this list's [Agent Sandboxes](#agent-sandboxes--tool-platforms) section is the short version).
- [awesome-microVM](https://github.com/dakotac1994/awesome-microVM) — the microVM ecosystem underneath most agent sandboxes.
- [awesome-jev](https://github.com/dakotac1994/awesome-jev) — TypeSafe Jev / System One: fast, typed AI decisions with calibrated confidence.

## Contributing

Contributions welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) first — entries need a verified official URL, a one-line description, and no marketing metrics.

## License

[![MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

This repository is released under the [MIT License](LICENSE). Copyright (c) 2026 dakotac1994.

