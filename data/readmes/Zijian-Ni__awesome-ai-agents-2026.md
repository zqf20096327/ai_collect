<div align="center">

# 🤖 Awesome AI Agents 2026

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FZijian-Ni%2Fawesome-ai-agents-2026&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)](https://github.com/Zijian-Ni/awesome-ai-agents-2026)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-October%208%2C%202026-blue.svg)](#)
[![Resources](https://img.shields.io/badge/Resources-940%2B-orange.svg)](#)
[![Categories](https://img.shields.io/badge/Categories-25-purple.svg)](#)
[![Audited](https://img.shields.io/badge/Spam_Audited-2026--10--08-success.svg)](#️-status-legend)
[![Chinese](https://img.shields.io/badge/Lang-中文-red.svg)](README.zh-CN.md)
[![Japanese](https://img.shields.io/badge/Lang-日本語-purple.svg)](README.ja.md)

**A curated list of AI models, agent frameworks, tools, protocols, and resources for 2026 — the year agents went mainstream and AI became infrastructure.**

*Covering foundation models, multimodal AI, agent protocols (MCP/A2A), coding agents, computer use, generative AI, and more.*

### 🏷️ Status Legend

Entries may carry one or more status tags so readers can judge maturity at a glance:

- 🆕 **New** — Added in the last 60 days, still settling.
- 📦 **Archived** — Repository archived by its owner; preserved for historical reference, no further updates expected.
- 💤 **Stale** — No commits in 6+ months; project may still work but is no longer actively maintained.
- ⚠️ **Unverified** — Recent submission with limited independent traction (low stars / no third-party adoption / sole-maintainer / submitted to many awesome lists in parallel). Listed for completeness, **not endorsed** — vet before using.
- 🇨🇳 **Chinese ecosystem** — Project from a mainland-China team or primarily targeting the Chinese market.
- 🔥 **Hot** — GitHub stars grew >20% in the last 30 days; community momentum.
- ⚡ **Updated** — Received a notable release or major feature in the last 14 days.
- 🧪 **Experimental** — Promising but not production-ready; use for R&D only.
- 💰 **Freemium** — Core functionality free; paid tiers for scale/advanced features.
- 🔐 **Audited** — Has undergone independent security audit or formal verification.
- 🇨🇳 **China-first** — Optimized for Chinese language, regulation, or infra stack.

[Foundation Models](#-foundation-models-2026) · [Multimodal AI](#-multimodal--generative-ai) · [Protocols](#-agent-protocols--standards) · [Frameworks](#️-agent-frameworks) · [IDEs & Builders](#️-agent-ides--visual-builders) · [Memory](#-agent-memory) · [Tools](#-tool--api-integration) · [Sandboxing](#-agent-sandboxing--compute-isolation) · [Security](#️-agent-security) · [RAG](#-rag--knowledge) · [Coding](#-coding-agents) · [Physical AI](#-physical-ai--embodied-agents) · [Simulation](#-agent-simulation--world-models) · [Benchmarks](#-benchmarks--leaderboards) · [Computer Use](#️-computer-use--desktop-agents) · [Browser & Web](#-browser--web-agents) · [Voice](#️-voice--multimodal-agents) · [Personal](#-personal-ai-agents) · [Mobile](#-mobile-agents) · [Enterprise](#-enterprise-agent-platforms) · [Evaluation](#-agent-evaluation--observability) · [Research Tools](#-ai-research-tools) · [Learning](#-learning-resources) · [Chinese Ecosystem](#-chinese-ai-ecosystem) · [Compare](#-compare--side-by-side-tables) · [Notable 2026](#-notable-agent-projects-of-2026) · [Timeline](#-2026-ai-timeline)

</div>

---

## 🚀 Start Here


> **New to AI agents?** Follow this path:
> 1. 📖 **Understand** — what an agent actually is vs. a chatbot
> 2. 🗺️ **Find your scenario** → [Scenario Guide](#️-scenario-guide--what-should-i-use-for)
> 3. 🧩 **Adapt a starting setup** → [Stack Recipes](#-stack-recipes--curated-tool-combinations)
> 4. 🔍 **Pick the right tool** → [Compare Tables](#-compare--side-by-side-tables)
> 5. ⚠️ **Avoid common mistakes** → [Anti-Picks](#️-anti-picks--what-not-to-use-for)
>
> **Already building?** Jump to:
> - 🆕 [Latest additions (October 2026)](#-2026-ai-timeline) • 🛡️ [Security](#️-agent-security) • 💰 [Cost comparison](#-foundation-models--api-cost--context)

---

## Quick Navigation

*Counts cover catalogue appearances, including historical/contextual entries; they are not a count of unique products. This is a curated selection with official catalogue links for further model discovery.*

| Category | Description | Count |
|----------|-------------|-------|
| [🧠 Foundation Models](#-foundation-models-2026) | Latest LLMs from OpenAI, Anthropic, Google, Meta, and 22+ providers | 245+ |
| [🎨 Multimodal & Generative AI](#-multimodal--generative-ai) | Image, video, audio, and music generation | 60+ |
| [🔗 Agent Protocols](#-agent-protocols--standards) | MCP, A2A, and interoperability standards | 20+ |
| [🏗️ Agent Frameworks](#️-agent-frameworks) | Libraries for building autonomous AI agents | 55+ |
| [🛠️ Agent IDEs & Visual Builders](#️-agent-ides--visual-builders) | Visual / low-code environments for designing agent flows | 10+ |
| [🧠 Agent Memory](#-agent-memory) | Persistent memory and context management | 25+ |
| [🔌 Tool & API Integration](#-tool--api-integration) | Connecting agents to external services | 25+ |
| [💱 Agent Economy & Marketplaces](#-agent-economy--marketplaces) | Where agents pay, get paid, and discover services | 10+ |
| [🧪 Sandboxing & Compute Isolation](#-agent-sandboxing--compute-isolation) | Secure runtimes for agent-generated code | 10+ |
| [🛡️ Agent Security](#️-agent-security) | Prompt injection defense and guardrails | 40+ |
| [🔍 RAG & Knowledge](#-rag--knowledge) | Retrieval-augmented generation systems | 20+ |
| [💻 Coding Agents](#-coding-agents) | AI-powered software engineering | 55+ |
| [🤖 Physical AI](#-physical-ai--embodied-agents) | Humanoid robots, embodied AI, industrial automation | 45+ |
| [🎮 Simulation & World Models](#-agent-simulation--world-models) | Sim environments for training and stress-testing agents | 10+ |
| [📊 Benchmarks](#-benchmarks--leaderboards) | Leaderboards tracking frontier capability | 25+ |
| [🖥️ Computer Use](#️-computer-use--desktop-agents) | Desktop automation and OS-level control | 10+ |
| [🌐 Browser & Web Agents](#-browser--web-agents) | Agents that drive real browsers | 20+ |
| [🗣️ Voice & Multimodal Agents](#️-voice--multimodal-agents) | Voice-enabled conversational AI | 25+ |
| [📱 Personal AI Agents](#-personal-ai-agents) | Productivity and daily life assistants | 20+ |
| [📱 Mobile Agents](#-mobile-agents) | Phone-control agents (Android / iOS) | 10+ |
| [🏢 Enterprise Platforms](#-enterprise-agent-platforms) | Enterprise-grade agent deployment | 30+ |
| [📊 Evaluation & Observability](#-agent-evaluation--observability) | Testing, monitoring, and benchmarking | 30+ |
| [🔬 AI Research Tools](#-ai-research-tools) | Tools for AI/ML research and experimentation | 15+ |
| [📚 Learning Resources](#-learning-resources) | Papers, courses, and tutorials | 25+ |
| [🇨🇳 Chinese AI Ecosystem](#-chinese-ai-ecosystem) | Major projects from China-based teams | 25+ |
| [📝 Compare](#-compare--side-by-side-tables) | Side-by-side comparison tables | — |
| [🗺️ Scenario Guide](#️-scenario-guide--what-should-i-use-for) | Curated scenario-to-tool mappings | 58 |
| [📋 Stack Recipes](#-stack-recipes--curated-tool-combinations) | Curated multi-tool combinations | 8 |
| [⚠️ Anti-Picks](#️-anti-picks--what-not-to-use-for) | What NOT to use and why | 17 |

---

## Contents

- [🧠 Foundation Models 2026](#-foundation-models-2026)
- [🎨 Multimodal & Generative AI](#-multimodal--generative-ai)
- [🔗 Agent Protocols & Standards](#-agent-protocols--standards)
- [🏗️ Agent Frameworks](#️-agent-frameworks)
- [🛠️ Agent IDEs & Visual Builders](#️-agent-ides--visual-builders)
- [🧠 Agent Memory](#-agent-memory)
- [🔌 Tool & API Integration](#-tool--api-integration)
- [💱 Agent Economy & Marketplaces](#-agent-economy--marketplaces)
- [🧪 Agent Sandboxing & Compute Isolation](#-agent-sandboxing--compute-isolation)
- [🛡️ Agent Security](#️-agent-security)
- [🔍 RAG & Knowledge](#-rag--knowledge)
- [💻 Coding Agents](#-coding-agents)
- [🤖 Physical AI & Embodied Agents](#-physical-ai--embodied-agents)
- [🎮 Agent Simulation & World Models](#-agent-simulation--world-models)
- [📊 Benchmarks & Leaderboards](#-benchmarks--leaderboards)
- [🖥️ Computer Use & Desktop Agents](#️-computer-use--desktop-agents)
- [🌐 Browser & Web Agents](#-browser--web-agents)
- [🗣️ Voice & Multimodal Agents](#️-voice--multimodal-agents)
- [📱 Personal AI Agents](#-personal-ai-agents)
- [📱 Mobile Agents](#-mobile-agents)
- [🏢 Enterprise Agent Platforms](#-enterprise-agent-platforms)
- [📊 Agent Evaluation & Observability](#-agent-evaluation--observability)
- [🔬 AI Research Tools](#-ai-research-tools)
- [📚 Learning Resources](#-learning-resources)
- [🇨🇳 Chinese AI Ecosystem](#-chinese-ai-ecosystem)
- [📝 Compare — Side-by-Side Tables](#-compare--side-by-side-tables)
- [🗺️ Scenario Guide — What Should I Use For…](#️-scenario-guide--what-should-i-use-for)
- [📋 Stack Recipes — Curated Tool Combinations](#-stack-recipes--curated-tool-combinations)
- [⚠️ Anti-Picks — What NOT to Use For…](#️-anti-picks--what-not-to-use-for)
- [🌟 Notable Agent Projects of 2026](#-notable-agent-projects-of-2026)
- [📅 2026 AI Timeline](#-2026-ai-timeline)

---

## 🧠 Foundation Models 2026

*Selected current and historical foundation models, organized by provider. Model cards, API availability and weight licenses can differ; dated entries preserve release history.*

### OpenAI
- [GPT-6.1 Sol](https://openai.com/index/introducing-gpt-6-1-sol/) - 🆕 **September 29, 2026 (DevDay)**. Upgrade to GPT-6 Sol for agentic coding, computer use and professional work; API model `gpt-6.1-sol` ($2/$10 per million input/output tokens, 1.05M context, 128K output) and ChatGPT Work/Codex on paid plans. OpenAI positions it near GPT-6 Astra at one-fifth of Astra's token prices; the benchmark comparisons are vendor-reported.
- [GPT-6 Sol / GPT-6 Luna](https://openai.com/index/introducing-gpt-6-sol-and-luna/) - 🆕 **September 22, 2026**. Mid and efficiency tiers of GPT-6; API IDs `gpt-6-sol` ($2/$10) and `gpt-6-luna` ($0.10/$0.50 per million input/output tokens), half the earlier GPT-5.6 Sol/Luna rates. They launched in ChatGPT Work and Codex first; [from October 7–8](https://help.openai.com/en/articles/6825453-chatgpt-release-notes) Chat uses Sol on paid plans and Luna on Free/Go.
- [OpenAI Agents API](https://openai.com/index/introducing-the-agents-api/) - 🆕 **September 10, 2026 (public beta)**. Hosted agent runtime built on the open-source Codex harness: one API call sets the task, model, tools and environment (OpenAI-hosted, self-managed or partner sandboxes such as E2B, Daytona, Modal and Vercel), with subagents, MCP tools and automatic context compaction. Computer use was added at DevDay; there is no separate fee beyond tokens and tools.
- [OpenAI DevDay 2026 — Dots, ChatGPT Space, Ultrafast](https://openai.com/index/devday-2026-recap/) - 🆕 **September 29, 2026**. Dots are always-on agents with connected apps and a cloud computer, rolling out to eligible Pro and Business Premium users (Enterprise/Edu beta, off by default; Pro excludes the EEA, Switzerland and the UK at launch). OpenAI also announced ChatGPT Space and Pages, a limited-preview Decisions API, plugin extensions, MCP events for plugin automations (based on a proposed spec), Sign in with ChatGPT and a Pro 500 plan with GPT-6 Astra Ultrafast.
- [GPT-Live-1 / GPT-Live-1 mini](https://openai.com/index/introducing-gpt-live/) - 🆕 **July 8, 2026**. OpenAI's full-duplex conversational voice model replacing Advanced Voice Mode. **ChatGPT-only — not exposed as an API model**; for programmatic realtime voice use `gpt-realtime-2.1`, and for streaming transcription `gpt-live-transcribe` ($0.017/min). Listens and speaks simultaneously, handles interruptions, delegates complex queries to GPT-5.5 in the background while keeping the conversation flowing. **GPT-Live-1** is default for paid users (Go/Plus/Pro); **GPT-Live-1 mini** is default for free users. Includes real-time live translation. Available on iOS, Android, and web.
- [GPT-6 Astra / Astra Pro](https://openai.com/index/gpt-6-astra/) - 🆕 **September 3, 2026**. Introduced for demanding reasoning, coding and computer use; [limited organizational rollout, not yet generally available](https://help.openai.com/en/articles/6825453-chatgpt-release-notes), so verify account access separately from the published API model card. The [API model page](https://developers.openai.com/api/docs/models/gpt-6-astra) now lists rate limits for paid usage tiers (not Free), and an Astra Ultrafast tier arrived on **September 29** for Pro 500 and Enterprise.
- [GPT-5.6 Sol](https://openai.com/blog/gpt-5-6) - GPT-5.6-family model for reasoning, coding and tool-based work. Standard API input/output pricing is $4/$20 per million tokens at this review; consult the [pricing table](https://developers.openai.com/api/docs/pricing) for long-context tiers, caching and service-tier differences.
- [GPT-5.6 Terra](https://openai.com/blog/gpt-5-6) - 🆕 **July 9, 2026**. Mid-tier model in the GPT-5.6 family offering GPT-5.5-parity performance at approximately 2× lower cost. Designed for cost-efficient production workloads.
- [GPT-5.6 Luna](https://openai.com/blog/gpt-5-6) - 🆕 **July 9, 2026**. The fastest and most cost-efficient tier of GPT-5.6 — optimised for high-volume, speed-critical tasks.
- [ChatGPT Work](https://openai.com/index/chatgpt-for-your-most-ambitious-work/) - 🆕 **July 9, 2026**. OpenAI's agent that turns a goal into finished work — acts across connected apps and files, stays on a project for hours, creates slides/sheets/docs/web apps, runs scheduled tasks, and uses desktop computer-use with a built-in browser. Powered by GPT-5.6. Rolling out on web/mobile starting with Pro, Enterprise, and Edu (Plus/Business next); the desktop app is available globally on Mac and Windows for all plans, including Free.
- [Sites for ChatGPT](https://openai.com/academy/chatgpt-sites/) - 🆕 **June 2026**. A Codex-powered ChatGPT feature that transforms plans and analyses into interactive, sharable websites and lightweight apps. In public beta as of the July 9, 2026 GPT-5.6 / ChatGPT Work launch.
- [Codex Business Plugins](https://venturebeat.com/orchestration/openais-codex-update-lets-agents-build-interactive-enterprise-workspaces-via-sites-and-role-specific-plugins) - 🆕 **June 2026**. Enterprise enhancements bringing sales, data analytics, and creative production plugins directly to Codex.
- [GPT-Rosalind](https://openai.com/index/introducing-new-capabilities-to-gpt-rosalind/) - **June 3, 2026**. Major update to OpenAI's life-sciences frontier model — stronger drug discovery, genomics, quantitative biology, and wet-lab troubleshooting (≈31% fewer tokens than GPT-5.5 on long-horizon genomics analyses). Research preview opened to eligible organizations worldwide; Novo Nordisk joins earlier partners Amgen, Moderna, the Allen Institute, and Thermo Fisher.

- [GPT-5.5](https://openai.com/index/gpt-5-5-system-card/) - Released **April 23, 2026** (codename "Spud"). OpenAI's new frontier model for agentic tasks: coding, online research, data analysis, autonomous tool navigation. Significant gains in reasoning, consistency, and long-horizon task handling. Available on ChatGPT Plus / Pro / Business / Enterprise.
- [GPT-5.5 Pro](https://openai.com/index/gpt-5-5-system-card/) - April 23, 2026. Parallel test-time compute variant for higher-accuracy cognitive tasks. Pro / Business / Enterprise tiers.
- [GPT-5.5 Instant](https://openai.com/index/gpt-5-5-instant/) - **May 5, 2026**. New ChatGPT default model. Efficiency-first upgrade with ~50% lower hallucination rate on high-stakes prompts; available on free tier.
- [GPT-5.5-Cyber](https://openai.com/index/trusted-access-for-cyber/) - **April 30, 2026**. Cybersecurity-specialized variant of GPT-5.5, rolled out via OpenAI's Trusted Access for Cyber (TAC) program to vetted defenders, government, critical infrastructure operators, and security vendors. Not available to the general public.
- [OpenAI Daybreak](https://thehackernews.com/2026/05/openai-launches-daybreak-for-ai-powered.html) - **May 12, 2026**. Cyber-defense platform bundling GPT-5.5 + GPT-5.5-Cyber + Trusted-Access-for-Cyber for AI-powered vulnerability detection and patch validation; preview access extended to EU governments and security vendors.
- [GPT-5.6-Cyber](https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows) - 🆕 **August 10, 2026**. OpenAI's cybersecurity-specialized model built on GPT-5.6 Sol, made available through the **Daybreak Red** vetted program for authorized vulnerability research and exploit validation. Capable of identifying zero-day vulnerabilities and developing exploit chains; access limited to cleared security professionals. Daybreak also expanded to AWS Bedrock on August 11.
- [GPT-Realtime-2](https://openai.com/) - **May 8, 2026**. GPT-5-class reasoning brought to the Realtime API, 128K context, parallel tool calls with audio feedback, adjustable reasoning effort.
- [GPT-Realtime-Translate](https://openai.com/) - **May 8, 2026**. Live speech-to-speech translation across 70+ input languages and 13 output languages.
- [GPT-Realtime-Whisper](https://openai.com/) - **May 8, 2026**. Streaming low-latency speech-to-text companion to GPT-Realtime-2.
- [OpenAI Deployment Company (DeployCo)](https://openai.com/index/openai-launches-the-deployment-company/) - **May 11, 2026**. New OpenAI-majority-owned services entity for enterprise AI rollout. Backed by **$4B+** from TPG / Advent / Bain Capital / Brookfield / Goldman Sachs / SoftBank and consulting partners Bain & Company, Capgemini, McKinsey. Built around Forward Deployed Engineers; absorbs the Tomoro AI consulting acquisition (~150 engineers).
- [Codex on Mobile](https://9to5mac.com/2026/05/14/openai-brings-codex-control-to-chatgpt-for-iphone-and-android/) - **May 14, 2026**. ChatGPT iOS/Android can now remote-control the Codex desktop app — review outputs, approve actions, switch models, and kick off new tasks from the phone while the live session runs on Mac (Windows next). Rolling out as preview to Free, Plus and Go users.
- [OpenAI ↔ Malta partnership](https://openai.com/index/malta-chatgpt-plus-partnership/) - **May 16, 2026**. First country-wide deal: every Maltese citizen / resident aged 14+ gets a free 1-year ChatGPT Plus subscription after completing a 2-hour AI literacy course built by the University of Malta. Part of the "OpenAI for Countries" initiative; phased rollout starting May 2026.
- [OpenAI ↔ Dell Codex partnership](https://openai.com/news/company-announcements/) - **May 18, 2026**. Brings Codex to hybrid and on-premises enterprise environments via Dell Technologies infrastructure — first major Codex distribution channel outside the public cloud, targeted at regulated industries needing data-residency control.
- [ChatGPT Safety Updates — sensitive-conversation tracking](https://www.edtechinnovationhub.com/news/openai-updates-chatgpt-safety-systems-to-track-risk-across-sensitive-conversations) - **May 18, 2026**. ChatGPT's safety systems updated to detect and track subtle escalation cues across long sessions for acute risks (suicide / self-harm / harm to others), with cross-session state retention.
- [OpenAI Guaranteed Capacity (Compute Annual Pass)](https://openai.com/news/company-announcements/) - **May 19, 2026**. Long-term compute reservation product for enterprise AI products / agents / workflows. 1, 2, or 3-year terms; longer terms unlock larger discounts. OpenAI's structural response to the Anthropic "Priority Tier" model.
- [OpenAI ↔ Google SynthID + C2PA content provenance](https://openai.com/index/advancing-content-provenance/) - **May 19, 2026**. OpenAI partners with Google to add durable cross-platform **SynthID watermarking** to ChatGPT/Sora images, joins C2PA, and previews a public **"is-this-image-from-OpenAI"** verifier. First major frontier-lab interop on watermarking.
- [GPT-5.4](https://openai.com/) - Released March 2026. Frontier model with 1M-token context, advanced coding, computer use, tool search. BenchLM 94, SWE-bench Verified 77.2%, OSWorld 75% (beats human).
- [GPT-5.4 Pro](https://openai.com/) - Higher-accuracy variant of GPT-5.4. BenchLM 92.
- [GPT-5.3](https://openai.com/) - Early 2026. Includes GPT-5.3 Instant (conversations) and GPT-5.3-Codex (coding).
- [GPT-5.2](https://openai.com/) - Released Dec 2025. State-of-the-art reasoning, long-context understanding, and vision.
- [GPT-5](https://openai.com/index/introducing-gpt-5/) - **August 2025**. Earlier GPT generation with standard, mini and nano API variants; retained as release history.
- [GPT-4o](https://openai.com/index/hello-gpt-4o/) - Omni model with native text, vision, and audio. Retired from ChatGPT Feb 2026 but still available via API.
- [GPT-4.5](https://developers.openai.com/api/docs/deprecations) - 📦 Historical research preview; the `gpt-4.5-preview` API was retired on **July 14, 2025**.
- [o3 / o4-mini](https://openai.com/index/introducing-o3-and-o4-mini/) - Reasoning models with chain-of-thought for complex problem solving. Released April 2025. o3 leaves ChatGPT on Aug 26, 2026; the `o3-2025-04-16` and `o3-pro-2025-06-10` **API snapshots are removed on Dec 11, 2026**, with `gpt-5.6-sol` named as the replacement ([deprecations](https://developers.openai.com/api/docs/deprecations.md)).
- [Codex CLI](https://github.com/openai/codex) - Open-source terminal-based coding agent powered by OpenAI models. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fopenai%2Fcodex&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [OpenAI Jalapeño](https://openai.com/index/jalapeno-first-results) - 🆕 ⚡ **August 25, 2026**. First public results for OpenAI's custom inference chip: higher throughput and lower latency for modern models. RSS: "industry-leading speed and efficiency in AI inference."
- [ChatGPT for Teens](https://openai.com/index/chatgpt-for-teens) - 🆕 **August 18, 2026**. Age-appropriate ChatGPT experience with stronger built-in protections, healthy-use features, and extra parent controls.
- [Zero Data Retention for frontier models](https://openai.com/index/offering-zero-data-retention-for-frontier-models) - 🆕 **August 19, 2026**. OpenAI reaffirms ZDR for eligible API customers and previews Private Safety Processing so advanced safety checks can run without retaining customer data.

### Anthropic

- [Claude Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5) - 🆕 **October 7, 2026**. Small Claude tier (`claude-haiku-5-5`) with 1M context, 128K output and the effort parameter; $0.10/$0.50 per million input/output tokens for prompts up to 100K and $0.50/$2.50 above. Migration note: `budget_tokens` returns a 400 and adaptive thinking is on by default ([release notes](https://platform.claude.com/docs/en/release-notes/overview)).
- [Claude Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5) - 🆕 **September 28, 2026**. `claude-sonnet-5-5` at $2/$10 per million input/output tokens with 1M context; Anthropic reports over 30% faster output and up to 30% lower cost per task than Sonnet 5. Forced tool use (`tool_choice` `any`/`tool`) returns a 400, so test migrations from Sonnet 5.
- [Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5) - 🆕 **September 22, 2026**. `claude-opus-5-5` at $4/$20 per million input/output tokens with 1M context and 128K output; Anthropic says it costs about 40% less than Opus 5 on typical workloads and approaches Fable 5.1 on most work, while GPT-6 Astra leads some of its published comparisons. Thinking cannot be disabled; Fast mode is a research preview.
- [Claude — Cowork in any conversation](https://support.claude.com/en/articles/12138966-release-notes) - 🆕 **September 16, 2026**. Cowork tasks, projects, connectors and skills become available from any conversation (gradual rollout on Pro/Max), and designs, decks and docs can be created on every plan, including Free; on Enterprise these are off until an owner enables them.
- [Claude Haiku 4.5](https://platform.claude.com/docs/en/models/overview) - Low-latency Claude tier with a 200K context window and 64K maximum output; superseded as the small tier by Haiku 5.5 on October 7, 2026.
- [Claude Fable 5.1 / Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1) - 🆕 **September 1, 2026**. Fable 5.1 is generally available (`claude-fable-5-1`); Mythos 5.1 uses the same model with different safeguards and remains limited to approved US organizations.
- [Claude text watermarking + content credentials](https://www.anthropic.com/news/claude-text-watermark) - 🆕 **August 14, 2026**. Anthropic adds invisible **SynthID-Text-based watermarking** (Google DeepMind's method) to future Claude models globally at launch, plus C2PA content credentials on generated images/files (.png/.jpg/.svg); models released before August 2, 2026 get it "over the coming months", and a detection API is coming. Implemented to comply with the EU AI Act after Anthropic signed the EU transparency Code of Practice in July. Anthropic says watermarked text is indistinguishable to readers.
- [Claude Opus 5](https://www.anthropic.com/news/claude-opus-5) - 🆕 **July 24, 2026**. Anthropic's fifth-generation flagship — nears Fable 5 performance at a significantly lower price ($5/$25 per million input/output tokens). 1M-token context window, 128K output tokens. Now the default model on Claude Max. API: `claude-opus-5`. Available on Anthropic API, Amazon Bedrock, and Google Cloud Vertex AI.
- [Claude Fable 5 (Global Reinstatement)](https://www.anthropic.com/news/redeploying-fable-5) - 🆕 **July 1, 2026**. After US Commerce Department export controls were lifted on June 30, Anthropic reinstated global access to Fable 5 across Claude.ai, the Claude Platform, Claude Code, and Claude Cowork. A new safety classifier blocking the Amazon-discovered jailbreak was deployed (blocks the reported behavior in >99% of cases). Pro/Max/Team and select Enterprise plans got Fable 5 included for up to 50% of weekly usage through July 7, then via usage credits; cloud re-enablement on AWS, Google Cloud, and Microsoft Foundry to follow. Mythos 5 remains restricted to vetted US entities.
- [Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5) - **June 30, 2026**. The most agentic Sonnet yet — planning, browser/terminal tool use, and autonomous operation at a level that recently required Opus-class models. Performance approaches Opus 4.8 on agentic search (BrowseComp) and computer use (OSWorld-Verified) at higher effort settings, with a much wider cost-performance range than Sonnet 4.6. Now the default model for Claude.ai Free/Pro; also on Max/Team/Enterprise, Claude Code, and the API as `claude-sonnet-5`. **August 10, 2026 update**: the introductory $2/$10 per million input/output pricing was made **permanent** — the previously scheduled increase to $3/$15 on September 1 will not occur. Anthropic reports a lower rate of undesirable behaviors than Sonnet 4.6.
- [Claude Fable 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) - **June 9, 2026**. Anthropic's first publicly available **Mythos-class** model — a capability tier above Opus. Surpasses Opus 4.8 across software engineering, knowledge work, vision, and scientific research benchmarks. Ships with built-in safeguards (sensitive cyber/bio queries may be rerouted to Opus 4.8). $10 / $50 per million in/out tokens. Available via Anthropic API, Amazon Bedrock, and Google Cloud Vertex AI. **⚠️ Access suspended June 12, 2026** — a US government export-control directive ordered Anthropic to disable Fable 5 and Mythos 5 for all customers pending security review. **✅ Export controls lifted June 30, 2026; access restored July 1** with a new cybersecurity classifier — see entry above ([statement](https://www.anthropic.com/news/redeploying-fable-5)). **August 7, 2026**: [biology-safeguard false positives reduced](https://www.anthropic.com/news) so Fable 5 falls back to a weaker model less often on biology-related queries.
- [Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) - **June 9, 2026**. The same underlying Mythos-class model as Fable 5 with fewer restrictions, deployed only to vetted partners (cybersecurity firms, infrastructure providers) through **Project Glasswing** in collaboration with the US government. Successor to the April Claude Mythos Preview. **⚠️ Suspended June 12, 2026** alongside Fable 5 under a US export-control directive. **✅ Partially reinstated June 26, 2026** — US Commerce Secretary Lutnick restored access to 100+ approved US companies and federal agencies; broader reinstatement ongoing ([statement](https://www.anthropic.com/news/fable-mythos-access)).
- [Claude Opus 4.8](https://www.anthropic.com/claude/opus) - **May 28, 2026**. Major Opus refresh: codebase-scale migrations, sharper agentic judgment, **dynamic workflows** research preview with hundreds of parallel sub-agents in a single session, manual **effort-control** panel, **3× cheaper Fast mode** at the same $5 / $25 per million in/out. Available on Anthropic native + Amazon Bedrock + AWS Claude Platform + Google Cloud + Microsoft Foundry. Teases an upcoming **Mythos-class** model series for limited orgs.
- [Claude Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7) - Released April 16, 2026. Advanced software engineering (SWE-bench Verified 87.6%), enhanced vision, proactive code verification. Supports `/think xhigh` reasoning effort. 1M-token context.
- [Claude Opus 4.6](https://www.anthropic.com/) - Released Feb 2026. 1M-token context, 14.5-hour task horizon. Leads Arena chat leaderboard.
- [Claude Sonnet 4.6](https://www.anthropic.com/news/claude-sonnet-4-6) - Released Feb 2026. Frontier coding and agentic performance, 1M token context window.
- [Claude Mythos Preview](https://www.anthropic.com/) - April 2026 gated research preview. BenchLM 99 (top of leaderboard), SWE-bench Verified 93.9%. Limited to Project Glasswing partners.
- [Claude Opus 4](https://www.anthropic.com/news/claude-4) - Released May 2025. Advanced reasoning and complex task execution.
- [Claude Sonnet 4](https://www.anthropic.com/news/claude-4) - Released May 2025. Balanced performance and cost for a wide range of tasks.
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) - Agentic coding tool operating directly in your terminal. Model options follow the current Claude lineup (Opus 5.5, Sonnet 5.5, Haiku 5.5, Fable 5.1); earlier Opus 4.7 `/think xhigh` guidance is historical. **July 2026**: desktop app gains a **built-in browser** enabling live website interaction (scraping, debugging, live-page inspection); Fable 5 model available since July 1.
- [Claude Security](https://www.anthropic.com/) - **May 1, 2026**. Public beta. Enterprise security tool powered by Opus 4.7 — scans entire codebases for vulnerabilities and generates targeted patches with confidence rating, severity, reproduction steps, and recommended fixes. Available to Enterprise customers via [claude.ai/security](https://claude.ai/security).
- [Claude Finance Agents](https://www.anthropic.com/news/finance-agents) - **May 5, 2026**. Ten Opus-4.7-powered specialised agents for pitchbook authoring, KYC, month-end close, deal screening, etc. Deployable as Claude Cowork plugins, Claude Code skills, or Managed-Agents cookbooks.
- [Claude Finance JV](https://www.anthropic.com/) - **May 4, 2026**. $1.5B Claude deployment joint venture with Goldman Sachs and Blackstone embedding Anthropic engineers in mid-market Wall Street firms.
- [Claude Managed Agents updates](https://claude.com/blog/new-in-claude-managed-agents) - **May 19, 2026**. Managed Agents update documents multi-agent coordination, rubric-based outcomes and dreaming in research preview; availability differs by feature.
- [Anthropic ↔ SpaceX Colossus 1](https://www.siliconrepublic.com/business/anthropic-joins-forces-with-spacex-for-colossus-capacity) - **May 6, 2026**. Anthropic takes all available capacity at SpaceX's Colossus 1 Memphis datacenter (>220K NVIDIA H100/H200/GB200 GPUs, 300+ MW) for Claude Opus inference. Doubles Claude Code 5-hour rate limits on Pro/Max/Team/Enterprise; also lifts peak-hour limits.
- [Anthropic ↔ AMD (up to 2 GW of Instinct MI450)](https://ir.amd.com/news-events/press-releases/detail/1292/amd-and-anthropic-announce-strategic-partnership-to-deploy-up-to-2-gigawatts-of-amd-instinct-mi450-series-gpus) - 🆕 **July 22, 2026**. Anthropic will deploy **up to 2 gigawatts** of AMD Instinct MI450 Series (MI455X) GPUs in AMD Helios rack-scale systems with EPYC "Venice" CPUs, Pensando networking and ROCm; the first gigawatt begins in H1 2027. AMD has committed a strategic equity investment of **up to $5 billion** in Anthropic, plus a multi-year engineering collaboration. Builds on Anthropic's existing MI355X usage — a deliberate hardware-diversification move alongside its TPU, Trainium and SpaceX Colossus capacity.
- [Anthropic's position on open-weights models](https://www.anthropic.com/news/position-open-weights-models) - 🆕 **July 27, 2026**. Dario Amodei responds to reports that US officials are weighing a ban on Chinese open-weights models: "Anthropic has never advocated for a ban on open-weights models." He calls non-dangerous open weights "a public good" and instead backs chip export controls plus a smuggling crackdown, deterrence of industrial-scale distillation, and **mandatory pre-release safety testing for all sufficiently capable models, open and closed**. Useful primary source for anyone tracking the 2026 open-vs-closed policy fight.
- [Claude for Legal](https://github.com/anthropics/claude-for-legal) - 🆕 **May 12, 2026**. New legal stack on top of Claude Cowork: **20+ MCP connectors** (iManage, NetDocuments, DocuSign, Ironclad, LexisNexis, Westlaw, Harvey, Everlaw, Relativity, CourtListener…) + **12 practice-area plugins** (commercial, employment, privacy, product, corporate, AI governance, litigation associate, law-student bar-exam). Microsoft Word / Outlook / Excel / PowerPoint orchestration built in.
- [Claude for Small Business](https://www.anthropic.com/news/claude-for-small-business) - **May 13, 2026**. Small-business toggle inside Claude Cowork — 15 pre-built agentic workflows across finance / ops / sales / marketing / HR / customer service, native connectors for QuickBooks, PayPal, HubSpot, Canva, DocuSign, Google Workspace, Microsoft 365. Bundled with a free PayPal-backed "AI Fluency for Small Business" course and a 10-city US workshop tour kicking off in Chicago.
- [Anthropic ↔ Gates Foundation $200M](https://www.anthropic.com/news/gates-foundation-partnership) - **May 14, 2026**. 4-year, $200M partnership pairing grants + Claude usage credits + Anthropic engineers on global-health, life-sciences, education, and agriculture programs. All tools produced under the program will be freely available; first focus areas include vaccine R&D for polio / HPV / preeclampsia and agriculture-specific Claude extensions.
- [Anthropic ↔ PwC strategic alliance expansion](https://www.pwc.com/us/en/about-us/newsroom/press-releases/anthropic-pwc-expand-alliance-agentic-enterprise.html) - **May 14, 2026**. PwC commits to global rollout of Claude Code + Claude Cowork, certifies 30,000 PwC professionals, and stands up a joint "Agentic Enterprise" Center of Excellence — focused on agentic build, AI-native deals, and finance / supply-chain / HR reinvention.
- [Anthropic ↔ Financial Stability Board briefing (Claude Mythos)](https://www.theguardian.com/technology/2026/may/18/anthropic-ai-claude-mythos-cyber-financial-stability-board-fsb) - **May 18, 2026**. Anthropic briefs the global FSB on Claude Mythos cyber-flaw discovery capabilities — first time a frontier lab briefs a G20-level financial-stability regulator on a frontier model's offensive-security implications.
- [Code with Claude 2026 sessions on YouTube](https://www.infoq.com/news/2026/05/code-with-claude/) - **May 18, 2026 (sessions published)**. Full developer-conference recordings (May 6 event) go public: Claude Code roadmap, Claude Developer Platform updates, Managed Agents dreaming + multi-agent orchestration, and partner deployments.
- [Widening the conversation on frontier AI](https://www.anthropic.com/news/widening-conversation-ai) - **May 19, 2026**. Anthropic publishes its framework for engaging diverse traditions (religious, philosophical, indigenous) in frontier-AI safety dialogue. Companion to ongoing public-engagement work.
- [Bristol Myers Squibb ↔ Anthropic Claude Enterprise](https://news.bms.com/news/corporate-financial/2026/Bristol-Myers-Squibb-Announces-Strategic-Agreement-with-Anthropic-to-Position-Claude-Enterprise-as-the-Shared-Intelligence-Platform-Across-Its-Global-Operations/default.aspx) - **May 20, 2026**. BMS adopts Claude Enterprise as its shared intelligence platform for 30,000+ employees globally, embedding agentic Claude into drug-discovery / development / delivery workflows. First top-5 pharma enterprise-wide Claude deployment.

### Google DeepMind
- [Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) - 🆕 **September 30, 2026 (limited access)**. Google DeepMind's new frontier model with a 1M-token output limit; initially available only to trusted cyber defenders through the [Fairwind Program](https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/), with paid API customers and Google AI Ultra subscribers next but no date given. Announced introductory API pricing is $2/$10 per million input/output tokens, then $4/$20.
- [Gemini 3.8 Live / Live Extended Thinking](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/) - 🆕 **September 15, 2026**. Speech-to-speech Live API models (`gemini-3.8-live`, `gemini-3.8-live-extended-thinking`), also used in Search Live, Gemini Live and Google Workspace.
- [Gemini 3.8 Flash TTS / Flash-Lite TTS](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/) - 🆕 **September 22, 2026**. Generally available text-to-speech models with a Voices endpoint, voice design and consent-verified voice replication; Flash-Lite TTS replaces `gemini-3.1-flash-tts-preview`.
- [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash) - 🆕 **September 2026**. Stable `gemini-3.8-flash` supports text, image, audio, video and PDF input, 1,048,576 input tokens, 65,536 output tokens and function calling.
- [Gemini 3.7 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) - 🆕 **August 13, 2026**. Google's new "most intelligent workhorse model" for coding and agents, shipped just three weeks after 3.6 Flash — and before the still-missing 3.5 Pro. FrontierCode 1.1 43.6% (vs 34.4% for 3.6 Flash), DeepSWE v1.1 65.3% (vs 49.0%). Introductory pricing **$0.75/$3.75 per million in/out through Dec 31, 2026** (then $1.50/$7.50). Available in AI Studio, Android Studio, Antigravity, and the Gemini Enterprise Agent Platform; powers Gemini Spark for AI Pro/Ultra subscribers.
- [Gemini 3.6 Flash](https://github.com/google-gemini/cookbook) - 🆕 **July 21, 2026**. Google's Flash tier — stronger on complex agentic and multimodal tasks **while using fewer tokens, at a lower price point than 3.5 Flash**. API id `gemini-3.6-flash`. Documented in the official Gemini API cookbook alongside thinking-mode guides. Superseded as the top Flash tier by 3.7 Flash on August 13, 2026.
- [Gemini 3.5 Flash-Lite](https://github.com/google-gemini/cookbook) - 🆕 **July 21, 2026**. The fastest, lowest-cost model in the 3.5 family; outperforms prior Flash-Lite generations for high-throughput execution. API id `gemini-3.5-flash-lite`. Now the cheapest Gemini tier, superseding 3.1 Flash-Lite for new builds.
- [Gemini 3.1 Pro (preview)](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-pro-preview) - Preview reasoning model with multimodal input and 1M context; availability and limits are endpoint-specific.
- [Gemini 3.5 Pro (announcement)](https://ai.google.dev/gemini-api/docs/models) - ⚠️ No Gemini 3.5 Pro endpoint appears in the current public Gemini API catalog checked **2026-09-08**; do not assume an announced model is available or infer its price/context.
- [Gemma 4 12B](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/) - **June 2026**. Novel multimodal open model with a **unified, encoder-free architecture** processing text, images, and audio in a single pass. Runs locally on 16 GB VRAM.
- [DiffusionGemma](https://www.marktechpost.com/2026/06/10/google-ai-releases-diffusiongemma-a-26b-moe-open-model-using-text-diffusion-for-up-to-4x-faster-generation/) - **June 2026**. 26B MoE open model using **text-diffusion** for up to **4× faster generation** than autoregressive models.

- [Gemini 3.5 Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - **May 19, 2026 — Google I/O 2026**. Default model powering the Gemini app and Google Search AI Mode. Marketed as **~4× faster** than other frontier models in output tokens/sec while outperforming Gemini 3.1 Pro on key benchmarks. Gemini 3.5 Pro was slated for June 2026 but has been delayed (see above).
- [Gemini Omni / Omni Flash](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - **May 19, 2026 — Google I/O 2026**. New Google DeepMind multimodal **world-model** family aimed at AGI. Omni Flash, the first shipped variant, can take any input modality and generate any output (starting with video; image and text generation following). Direct lineage to Gemini Robotics / Genie line of work.
- [Gemini 3.1 Pro](https://deepmind.google/technologies/gemini/) - Released Feb 2026. BenchLM 94, GPQA Diamond 94.3% (world-record), ARC AGI2 77.1%. `$2/1M tokens` flagship.
- [Gemini 3.1 Flash Live](https://deepmind.google/technologies/gemini/) - April 2026. Real-time multimodal streaming for voice assistants and interactive agents. Low latency, long context.
- [Gemini 3.1 Flash-Lite (GA)](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-lite-is-now-generally-available) - **May 8, 2026**. Generally available on Gemini API / AI Studio / Vertex AI. Fastest and most cost-efficient model in the Gemini 3 family — built for low-latency code completion, real-time UX, and agentic developer tools; matches Gemini 2.5 Flash quality at significantly lower cost.
- [Gemini Omni Flash — voice-controlled video editing rollout](https://www.techtimes.com/articles/317309/20260528/google-gemini-omni-flash-brings-voice-controlled-ai-video-editing-future-conversational-ai.htm) - **May 28, 2026**. Omni Flash starts rolling out to consumers via the Gemini app, **Google Flow**, and **YouTube Shorts** as the editing engine — conversational cinematic zooms / background swaps / weather edits driven by text, voice, image, or audio prompts; no traditional NLE required.
- [Gemini Spark (24/7 personal AI agent)](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - **May 19, 2026 — Google I/O 2026**. Cloud-resident personal AI agent that runs **24/7** on user intent, integrates Gmail / Chat first, then ~30+ third-party tools via MCP (Adobe / Dropbox / Uber). Available to Google AI Ultra subscribers in the US within the I/O week.
- [Google AI Ultra ($100/month tier)](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/) - **May 19, 2026 — Google I/O 2026**. New top consumer subscription targeted at developers / creators / power users. Gates Gemini Spark, highest Gemini 3.5 quotas, and the upcoming Gemini 3.5 Pro.
- [Gemini 3.1 Flash / Flash Lite](https://deepmind.google/technologies/gemini/) - Fast, cost-efficient models for high-throughput applications.
- [Gemma 4 family](https://huggingface.co/google/gemma-4-31B-it) - Open-weight multimodal family with E2B, E4B, 12B, 26B A4B and 31B variants under Apache-2.0; this is Gemma, not a released open Gemini 4 family.
- [Gemini 2.5 Pro / Flash](https://deepmind.google/technologies/gemini/) - GA June 2025. Thinking model with 1M context.
- [Gemma 4 31B](https://github.com/google-deepmind/gemma) - April 2026. GPQA Diamond 84.3%. Strong open-weight alternative for on-device reasoning. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fgoogle-deepmind%2Fgemma&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Gemma 3](https://github.com/google-deepmind/gemma) - Previous open model family for on-device and research use.
- [Gemini Robotics ER 2](https://ai.google.dev/gemini-api/docs/robotics-overview) - 🆕 Current embodied-reasoning preview for spatial understanding and robotics tool orchestration, with a separate streaming preview; replaces the retired ER 1.6 endpoint.

### Meta

- [Muse Spark 1.3](https://research.meta.ai/blog/introducing-muse-spark-1-3) - 🆕 **September 2, 2026**. Agentic and coding update available in Muse Code and Meta Model API, including max reasoning; Spark open weights remain on the roadmap.
- [Muse Image](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) - 🆕 **July 7, 2026**. Meta Superintelligence Labs' most advanced image generation model to date — an "agentic" image model that performs intermediate reasoning steps (web search, code execution, self-refinement) before producing high-quality visuals. Integrated into the Meta AI app, Instagram Stories (US), and WhatsApp in limited countries (Facebook coming soon). Note: a controversial feature allowing images from other users' public Instagram profiles was added then removed on July 10 after feedback.
- [Muse Spark 1.1](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/) - 🆕 **July 9, 2026**. Multimodal reasoning model designed for agentic tasks from Meta Superintelligence Labs — available through a new public preview of the Meta Model API. Marks a strategic shift toward proprietary revenue-focused models alongside Meta's open-source Llama line.
- [Muse Video](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) - 🆕 **July 7, 2026 (preview)**. Video generation model from Meta Superintelligence Labs, built on the same foundational technology as Muse Image; ranks #3 on Arena for text-to-video. Previewed alongside the Muse Image launch — "coming soon to creators and Meta AI."
- [Muse Spark 1.2 + Muse Code (beta)](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2) - 🆕 **August 5, 2026**. **Muse Code** is MSL's terminal coding agent (async background agents, replay-exact local event log, `/plan` / `/grill` / `/goal` skills), powered by the new **Muse Spark 1.2** — trained on whole-repository generation and long-horizon coding. Spark 1.2 is also available in the Meta Model API with expanded global access.
- [Muse Glimmer 30B](https://huggingface.co/meta-models/Muse-Glimmer-30B) - 🆕 **August 10, 2026**. Open-weight, 30B-parameter multimodal model from Meta Superintelligence Labs, Apache 2.0 license. Designed for **always-on local agent workflows** and optimized to run on a single consumer GPU or Apple Silicon. 131K-token context window, 100+ language training, DFlash acceleration. Distilled from Muse Spark; tuned for coding, evaluation, and agentic tasks. Available on Hugging Face with llama.cpp / MLX / ExecuTorch integrations.
- **Llama 5** — ❌ **Does not exist. Removed from this list on 2026-07-30 after verification.** A "Llama 5, 600B+, April 8 2026" entry circulated widely in AI-news aggregators and LLM search summaries, and was previously listed here. It does not hold up: the `meta-llama` Hugging Face organisation contains **no Llama-5 weights of any kind** (newest Llama-family upload is Llama-4-Maverick, May 2025), and Wikipedia's Llama article states "the latest version is Llama 4, released in April 2025" and that **Muse Spark replaced the Llama line in April 2026**. Treat any "Llama 5" claim as unverified until Meta publishes weights or a newsroom post. See [Muse Spark](#meta) above for what actually shipped.
- [Muse Spark](https://ai.meta.com/blog/introducing-muse-spark-msl/) - **April 9, 2026**. First model from Meta Superintelligence Labs (MSL). Natively multimodal reasoning model powering Meta AI app, smart glasses, and features across Facebook / Instagram / WhatsApp / Messenger.
- [Llama 4 Scout](https://llama.meta.com/) - 109B total params (17B active), MoE with 16 experts, 10M token context window, multimodal. Runs on single H100.
- [Llama 4 Maverick](https://llama.meta.com/) - 400B total params (17B active), 128 experts, 1M context. Outperforms GPT-4o on multimodal benchmarks.
- [Llama 4 Behemoth](https://llama.meta.com/) - 2T parameters (288B active). In training — Meta's frontier model rivaling top closed-source models.
- [Llama 3.3 70B](https://llama.meta.com/) - Strong instruction following and reasoning, open-weight under Llama Community License.

### Sakana AI

- [Sakana Namazu](https://console.sakana.ai/models) - Japanese-specialized LLM exposed as `sakana-namazu-v1.0`; the `sakana-namazu` alias follows the current release.
- [Sakana RL Conductor](https://venturebeat.com/orchestration/how-sakana-trained-a-7b-model-to-orchestrate-gpt-5-claude-sonnet-4-and-gemini-2-5-pro) - **Paper April 27, 2026; Fugu beta late-April / early-May 2026**. 7B RL-trained orchestrator (built on Qwen2.5-7B) that routes subtasks between GPT-5, Claude Sonnet 4, Gemini 2.5 Pro, etc. SOTA on LiveCodeBench (83.9%) and GPQA-Diamond (87.5%) at ~1.8K tokens/query — roughly 6× cheaper than other multi-agent ensembles.
- [Sakana Fugu / Fugu Ultra](https://console.sakana.ai/models) - Model orchestration API with `fugu`, `fugu-ultra-v1.1` and pay-as-you-go `fugu-cyber-v1.0`, supporting OpenAI-compatible Responses and Anthropic-compatible Messages.

### Zyphra

- [ZAYA1-8B](https://www.zyphra.com/models/zaya1-8b) - **May 6, 2026**. Small MoE reasoning model with Apache-2.0 weights, trained using AMD MI300X infrastructure.
- [ZAYA1-8B-Diffusion-Preview](https://www.zyphra.com/post/zaya1-8b-diffusion-preview) - **May 14, 2026**. First MoE diffusion language model converted from an autoregressive LLM and the first diffusion LM trained on AMD GPUs. Generates 16 tokens per step, achieving up to **7.7× inference speedup** vs the autoregressive base. Built with Zyphra's TiDAR recipe + CCA attention.

### Thinking Machines Lab

- [Inkling](https://thinkingmachines.ai/inkling/) - **July 15, 2026**. Apache-2.0 MoE model with 975B total / 41B active parameters and native text, image and audio input; model context reaches 1M, while Tinker exposes smaller limits.
- [Inkling-Small](https://thinkingmachines.ai/inkling/) - 🆕 **July 30, 2026 (weights released)**. Compact variant of Inkling — 276B total / 12B active, same native multimodal architecture (text/image/audio), 1M-token context, Apache 2.0. Scores **31.6% on HLE text benchmark** — slightly outperforming the larger 975B Inkling (29.7%) on that metric, validating the efficiency-first design. Available via Thinking Machines API and Hugging Face.

### Mistral AI

- [Mistral Large 4](https://mistral.ai/news/mistral-large-4) - 🆕 **October 6, 2026 (public preview)**. Natively multimodal MoE (about 1T total / 52B active parameters) combining instruct and reasoning modes, available in Mistral Studio's preview API at $1.36/$4.18 per million input/output tokens; Mistral says open weights follow at the end of October, and the licence has not yet been published.
- [Voxtral Mini Transcribe Realtime](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602) - Apache-2.0 open-weight model for streaming speech recognition, distinct from the Voxtral TTS generation model.
- [Shieldstral 1.0](https://docs.mistral.ai/models/shieldstral-1-0) - 🆕 **August 4, 2026**. Apache-2.0 text/image moderation model in public preview; classifies policy questions, prompt-response pairs and refusals.
- [Mistral OCR 4.1](https://docs.mistral.ai/models/ocr-4-1) - Document OCR service returning paragraph bounding boxes, structural block labels and confidence scores.
- [Mistral Large 3](https://mistral.ai/news/mistral-3) - 675B total / 41B active parameters, MoE, 256K context. Flagship open-weight multimodal model. Released Dec 2025.
- [Mistral Medium 3.1](https://docs.mistral.ai/models) - 📦 Legacy 2025 release now listed among deprecated/retired models; Mistral Medium 3.5 is the current Medium entry.
- [Mistral Small 4](https://mistral.ai/news/mistral-small-4) - Released March 2026. 119B total / 6B active. Hybrid model combining reasoning, multimodal, and coding strengths.
- [Magistral 1.2](https://docs.mistral.ai/models) - 📦 Historical Medium/Small reasoning variants from September 2025, now in Mistral's deprecated/retired catalog.
- [Devstral 2](https://docs.mistral.ai/models/devstral-2-25-12) - Historical agentic coding model with a December 2025 model card; check lifecycle status before deployment.
- [Codestral 2508](https://docs.mistral.ai/models/codestral-25-08) - Code-completion model in the current Mistral catalog; use the versioned model card instead of the original 2024 22B specifications.
- [Pixtral Large](https://mistral.ai/) - 124B multimodal model with 1B vision encoder, 128K context, processes 30+ high-res images.
- [Ministral 3B/8B/14B](https://mistral.ai/) - Compact models optimized for edge deployment and efficiency.
- [Mistral Forge](https://mistral.ai/) - March 2026 platform for training custom LLMs on proprietary data.
- [Mistral Medium 3.5](https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04) - **April 28, 2026**. Dense 128B open-weight model, 256K context, Modified MIT license. Unifies instruction-following, reasoning, and coding.
- [Leanstral 1.5](https://mistral.ai/news/leanstral-1-5/) - 🆕 **July 2, 2026**. Formal-verification model for proof engineering in Lean 4 — 119B total / 6B active parameters, Apache 2.0, weights on Hugging Face plus a free API endpoint. Scores 100% on miniF2F, solves 587/672 PutnamBench problems, and discovered 5 previously unreported bugs across 57 real-world repositories.
- [Robostral Navigate](https://mistral.ai/news/robostral-navigate/) - 🆕 **July 8, 2026**. Mistral's first robotics model — an 8B embodied-navigation model that steers wheeled, legged, and flying robots through offices, homes, and outdoor spaces from natural-language instructions using only a single RGB camera (76.6% success rate on unseen validation). Trained fully in-house on ~400K simulated trajectories.
- [Voxtral TTS](https://docs.mistral.ai/models/voxtral-tts-26-03) - Open-weight speech generation with voice cloning and multilingual support; weights use CC-BY-NC-4.0, so commercial deployment needs separate permission.

### DeepSeek

- [DeepSeek-V4.1-Flash](https://api-docs.deepseek.com/news/news260910) - 🆕 **September 10, 2026**. API model `deepseek-flash`: MoE with a 552B-parameter backbone, 8B active parameters for prefill and 16B for decode, native image input, 1M context and [MIT-licensed weights](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash). Peak/off-peak cache-miss input is $0.30/$0.15 and output $1.20/$0.60 per million tokens; the retired V4-Flash names route to it. The announcement also scheduled temporary `deepseek-v4-pro` routing, but the current pricing page still maps that name to V4-Pro-0813 — verify before migrating.
- [DeepSeek-V4-Pro-0813 (GA)](https://api-docs.deepseek.com/news/news260813) - **August 13, 2026**. Production checkpoint behind `deepseek-v4-pro`, with configurable reasoning effort and Responses API support; peak/off-peak pricing has applied since August 16.
- [DeepSeek-V4-Pro](https://api-docs.deepseek.com/news/news260424) - **April 24, 2026 (preview); production launch mid-July 2026**. 1.6T total / 49B active MoE, 1M-token context. MIT license. Leadership in agent capabilities, world knowledge, reasoning; tops open-source benchmarks. 384K max output, 500-request concurrency. `deepseek-v4-pro` / `deepseek-v4-flash` are the production API models (V4-Pro serves the 0813 checkpoint since August 13 — see above; tiered peak/off-peak pricing from August 16, 2026).
- [DeepSeek-V4-Flash](https://api-docs.deepseek.com/news/news260424) - 📦 API model retired on September 10, 2026; its names now route to V4.1-Flash. April 24, 2026. 284B total / 13B active MoE, 1M context. MIT. Cost-efficient tier — from August 16, 2026: peak **$0.014 cache-hit / $0.44 cache-miss input, $1.32 output**, off-peak **$0.007 / $0.22 / $0.66** per 1M tokens; 384K max output, 2,500-request concurrency ([pricing](https://api-docs.deepseek.com/quick_start/pricing)).
- [DeepSeek-V4-Flash-0731](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731) - 🆕 **July 31, 2026**. Updated Flash checkpoint with enhanced agentic capabilities — same 284B/13B-active MoE architecture, same pricing/API model ID, but outperforms V4-Pro (Preview) on agent task benchmarks. Open weights on Hugging Face under MIT license. Drop-in replacement for `deepseek-v4-flash` API users.
- [DeepSeek-V4-Flash-Vision-Exp](https://api-docs.deepseek.com/news/news260821) - 🆕 **August 21, 2026**. Experimental multimodal API model (`deepseek-v4-flash-vision-exp`) that matches V4-Flash on text/agents/reasoning while jumping multimodal-agent benchmarks to near Opus-4.8. Images billed at V4-Flash rates (up to 384 tokens each); Chat Completions / Messages / Responses; base64, URL, or Files API. **Files API** launched the same day (free upload, reuse by `file_id`). DeepSeek Harness 0.1.1 shipped with day-one support.
- [DeepSeek Agent Harness team](https://www.scmp.com/tech/big-tech/article/3354113/deepseek-recruits-former-jane-street-engineer-catch-ai-agents-revenue-race) - **May 19, 2026**. DeepSeek hires a former Jane Street engineer to lead a new "AI harness" team building the deterministic scaffolding that turns DeepSeek V4 into autonomous, revenue-generating agents — first major signal DeepSeek is moving past raw-model R&D into agentic productisation.
- [DeepSeek-V3.2](https://www.deepseek.com/) - Released Dec 2025. Advanced MoE architecture with 671B total parameters. V3.2 Speciale variant for enhanced reasoning. ⚠️ API model IDs deepseek-chat / deepseek-reasoner (V3.2-era) deprecated effective July 24, 2026 — superseded by V4-Flash modes.
- DeepSeek-R2 - 🧪 **Unreleased/rumored.** No official announcement, model card, or API ID exists as of mid-July 2026; reasoning is served via V4's Thinking mode.
- [DeepSeek-R1](https://www.deepseek.com/) - Reasoning-focused model with chain-of-thought capabilities. Released Jan 2025.
- [DeepSeek-Coder-V2](https://github.com/deepseek-ai/DeepSeek-Coder-V2) - Code generation model competitive with GPT-4 on coding benchmarks. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fdeepseek-ai%2FDeepSeek-Coder-V2&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Alibaba (Qwen)

- [Qwen3.8-Flash-Next](https://huggingface.co/Qwen/Qwen3.8-Flash-Next) - 🆕 **August 2026**. Experimental multimodal MoE with 125B parameters / 6B active plus 51B n-gram tables and 4B MTP; native 262K context, extensible to 1M, under Qwen Community License 1.0.
- [Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B) - 🆕 **August 14, 2026**. Open-weight 27B multimodal (text/image/video input) distillation of Qwen3.8-Max, released on Hugging Face under **Apache 2.0** — sized for ~24 GB-VRAM consumer GPUs (RTX 4090-class). The promised open-weight companion to the Qwen3.8-Max launch, shipped on schedule.
- [Qwen3.8-Max / Qwen3.8-2.4T-A95B](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) - **August 2026**. Multimodal flagship with an official downloadable checkpoint; full-model weights use a custom Qwen license, while the separate Qwen3.8-27B checkpoint uses Apache-2.0.
- [Qwen3.7-Max](https://www.scmp.com/tech/big-tech/article/3354212/alibaba-unveils-new-qwen-model-custom-chips-bid-become-chinas-ai-factory) - **May 20, 2026 — Alibaba Cloud Summit Hangzhou**. New Qwen flagship purpose-built as the foundation for AI agents: agentic coding, complex reasoning, and **long-horizon multi-step missions** with sustained decision-making. Released alongside a full-stack AI infrastructure upgrade and new T-Head **Zhenwu M890** AI accelerator chip. Worldwide developer/enterprise availability rolling.
- [Qwen3.7-Max-Preview / Qwen3.7-Plus-Preview](https://www.scmp.com/tech/tech-trends/article/3354087/alibaba-teases-new-qwen-previews-highest-ranking-chinese-ai-models-arena) - **May 18, 2026**. Preview ladder before the Hangzhou unveil. Ranked the highest of any Chinese model on LM Arena in both text and vision; sustained 1M-context evaluations.
- [Qwen3.6-27B](https://qwen.ai/blog?id=qwen3.6-27b) - **April 22, 2026**. Dense 27B multimodal. Open-sourced. Focus: agentic coding + thinking-context preservation.
- [Qwen3.6-Max-Preview](https://qwen.ai/) - **April 18, 2026**. Proprietary frontier preview. High coding/reasoning performance, 1M context window. Top-tier among Chinese models on coding benchmarks.
- [Qwen3.6-35B-A3B](https://qwen.ai/blog?id=qwen3.6-35b-a3b) - **April 15, 2026**. MoE, 35B total / 3B active. Apache 2.0. Stability and real-world utility improvements.
- [Qwen3.6-Plus](https://qwen.ai/) - **April 2, 2026**. Proprietary flagship. High value-per-token general model. Strong long-context, tool-calling, agentic behavior.
- [HappyHorse 1.1](https://technode.com/2026/06/23/alibaba-unveils-happyhorse-1-1-video-generation-model-launches-global-ai-filmmaking-competition/) - 🆕 **June 23, 2026**. Alibaba's video-generation model (T2V/I2V/S2V, up to 15s 1080p with synced audio, strong multi-shot character consistency). HappyHorse 1.0 entered limited beta April 28, 2026 after launching anonymously and topping video leaderboards.
- [Qwen3.5 Max Pro](https://qwen.ai/) - April 2026. High-performance flagship. Enhanced coding and math reasoning, long context.
- [Qwen3.5 Omni Plus](https://qwen.ai/) - April 2026. Proprietary full-modal foundation model unifying text and image input.
- [Qwen3-Max-Thinking](https://qwen.ai/) - Alibaba's strongest thinking model. 1T+ parameters, enhanced agentic capabilities.
- [Qwen3.5-Omni](https://qwen.ai/) - March 2026. Fully omni-modal: language, vision, sound, motion. Speech recognition in 113 languages, 256K context.
- [Qwen3-Coder-Next](https://qwen.ai/) - Feb 2026. Open-weight coding agent model, MoE 80B total / 3B active.
- [Qwen3 235B-A22B](https://qwen.ai/) - MoE with dual-mode reasoning. Strong math, code, and commonsense reasoning.
- [Qwen2.5 Coder 32B](https://github.com/QwenLM/Qwen3-Coder) - Top open-source coding model. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FQwenLM%2FQwen3-Coder&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### xAI / SpaceXAI (Grok)

- [Grok 4.7](https://docs.x.ai/docs/release-notes) - 🆕 **September 21, 2026**. `grok-4.7` on the xAI API for coding, agentic tasks and knowledge work: 500K context, text and image input, reasoning effort low–xhigh; $2/$0.50/$6 per million input/cached/output tokens below 200K prompt tokens and $4/$1/$12 above. Grok 4.7 Fast (2× rates) is offered only in Cursor and Grok Build.
- [Grok 4.6](https://x.ai/news/grok-4-6) - **August 12, 2026**. Coding and agentic model offered through the API, Cursor and Grok Build, starting at $2 input / $6 output per million tokens; Fast costs twice as much.
- [Grok Bot](https://docs.x.ai/docs/release-notes) - 🆕 **August 11, 2026 (early beta)**. Durable AI teammates that work on a **persistent cloud computer**, with messaging, approvals, connectors, and routines — xAI's entry into always-on autonomous agents. Available via SuperGrok Heavy, Cursor Ultra, and Cursor Teams Premium.
- [Grok 4.5](https://x.ai/) - 🆕 **July 8, 2026**. Optimised for coding and agentic tasks through joint training with Cursor using real developer interaction data. Features a 500K-token context window, function calling, structured outputs, web/X search, code execution, document search, and context compaction. Priced at $2/$6 per million in/out tokens. EU API-console availability arrived July 17, 2026. Superseded as flagship by Grok 4.6 on August 12, 2026.
- [Grok 4.3 GA](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-grok-4-3-on-microsoft-foundry-latest-generation-agentic-capabilities/4517096) - **May 2026**. Grok 4.3 reached general availability on Microsoft Foundry and OCI Generative AI; xAI's flagship for agentic workloads with improved tool-calling and long-horizon reasoning.
- [Grok 4.3 Beta](https://x.ai/) - April 2026. Latest iteration with improved reasoning and coding benchmarks. See [`2026.4` benchmark snapshot](https://benchlm.ai/).
- [Grok 4.20](https://x.ai/) - Feb 2026. Multi-agent system (4 standard + 16 specialized agents in Heavy mode), 2M token context.
- [Grok 4 / 4 Heavy](https://x.ai/) - Released July 2025. xAI's frontier model of the Grok 4 generation.
- [Grok 3 / 3 Mini](https://x.ai/) - Feb 2025. First reasoning models with "Think Mode".

### Microsoft (MAI)

- [MAI-Transcribe-2-Streaming](https://microsoft.ai/news/our-first-streaming-transcription-model/) - 🆕 **October 1, 2026**. Microsoft's first streaming speech-recognition model: 60 languages with continuous language detection and first partial transcripts in about 100 ms; offered in Microsoft Foundry, MAI Playground, Vercel and Azure Voice Live at an introductory $0.54 per audio hour through year-end.
- [MAI-Transcribe-2](https://microsoft.ai/news/mai-transcribe-2-is-the-fastest-most-accurate-and-cheapest-speech-recognition-model-in-the-world/) - 🆕 **September 3, 2026**. Speech recognition with diarization, word timestamps, vocabulary biasing and 60-language support; promotional pricing is $0.10/audio-hour through year-end.
- [Microsoft MAI-Code-1-Flash](https://microsoft.ai/news/introducingmai-code-1-flash/) - **Build 2026 (June 2, 2026)**. Microsoft's first major in-house foundation model built entirely without OpenAI technology. 5B-parameter coding model with adaptive thinking, rolling out in GitHub Copilot. Outperforms Claude Haiku 4.5 across four core coding benchmarks (16-point lead on SWE-Bench Pro: 51.2% vs 35.2%); solves harder tasks with up to 60% fewer tokens on SWE-Bench Verified.
- [Microsoft MAI-Thinking-1](https://microsoft.ai/news/microsoft-build-2026-mai-keynote-transcript/) - **Build 2026 (June 2, 2026)**. Microsoft's first in-house reasoning model, trained from scratch without OpenAI data. Companion to MAI-Code-1-Flash; signals Microsoft's foundation-model independence push.
- [MAI-Code-1.1-Flash](https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/) - 🆕 **August 11, 2026**. Production Copilot workhorse vs the June 1.0 baseline: higher-quality code, **25% greater token efficiency**, **a quarter of the cost**; +22% Terminal-Bench 2.1, +15% on .NET tasks.
- [MAI-Image-2.6](https://microsoft.ai/news/mai-image-2-6-launches-at-no-2-on-arena-ahead-of-google-meta-and-xai/) - 🆕 **August 10, 2026** (Arena editing update **August 18**). Microsoft's image model launched at Arena T2I #2; by Aug 18 it was Arena **image-editing #3**, ahead of Nano Banana and Muse Image (+79 Elo vs 2.5). MAI Playground + Microsoft Foundry private preview. **September 4, 2026**: [MAI-Image-2.6-Flash](https://microsoft.ai/news/pushing-the-quality-cost-frontier-with-mai-image-2-6/) was added and both models entered public preview in Microsoft Foundry.
- [MAI-Cyber-1-Flash](https://microsoft.ai/news/introducing-mai-cyber-1-flash-inside-mdash/) - 🆕 **August 13, 2026**. Cyber model inside MDASH; Microsoft says world-class performance at **50% of the cost** of leading models.

### Microsoft (Phi)

- [Phi-4-reasoning-vision-15B](https://huggingface.co/microsoft/Phi-4-reasoning-vision-15B) - MIT-licensed 15B vision-language model combining image understanding with reasoning; consult the official checkpoint for deployment requirements.
- [Phi-4](https://azure.microsoft.com/en-us/products/phi) - 14B parameter SLM with reasoning rivaling much larger models. Open-source under MIT License.
- [Phi-4-mini](https://azure.microsoft.com/en-us/products/phi) - 3.8B parameter dense model. 128K context. Excels in reasoning, math, coding, and function-calling.
- [Phi-4-multimodal](https://azure.microsoft.com/en-us/products/phi) - 5.6B parameter. First multimodal Phi model — integrates speech, vision, and text in unified architecture.

### Cohere

- [Command A+](https://docs.cohere.com/docs/command-a-plus) - **May 2026**. `command-a-plus-05-2026` unifies image input, reasoning, tool use and translation, with 128K input context and 64K output.
- [Command A](https://docs.cohere.com/v2/changelog/command-a) - Released March 13, 2025. 111B open-weights model, 256K context. Agentic, multilingual, and coding focused.
- [Command R+](https://cohere.com/) - Enterprise RAG model, 128K context, multilingual (10 languages), grounded generation with citations.
- [Command R](https://cohere.com/) - Cost-efficient model for retrieval-augmented generation and enterprise workloads.

### Baidu (ERNIE / 文心)

- [ERNIE 5.1](https://ernie.baidu.com/blog/posts/ernie-5.1-0508-release/) - **May 9, 2026 official post**. ERNIE model update using asynchronous reinforcement learning and agentic post-training for writing, reasoning and tool-driven work.
- [ERNIE 5.0](https://ernie.baidu.com/) - Released November 13, 2025 (Baidu World). 2.4T-parameter omni-modal MoE (activates <3% per query).
- [ERNIE 4.5](https://yiyan.baidu.com/) - Multimodal predecessor released 2025. Strong reasoning and Chinese language capabilities.

### Zhipu AI / Z.ai (GLM)

- [GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash) - 🆕 MIT-licensed multimodal MoE with 320B total / 18B active parameters, hybrid sparse/linear attention and configurable reasoning effort.
- [GLM-5.3](https://huggingface.co/zai-org/GLM-5.3) - 🆕 Official coding/reasoning weights are now downloadable; they use the custom GLM-5.3 License, not GLM-5.2's MIT license, and support vLLM/SGLang deployment.
- [GLM-5.2](https://z.ai/blog/glm-5.2) - **June 13, 2026**. Coding-first 744B-MoE flagship with a **1M-token context window** (~5× GLM-5.1) and up to 131K output tokens. Live across all GLM Coding Plan tiers; MIT open weights + standalone API rolling out the launch week. Works out of the box with Claude Code, Cline, OpenCode, Roo Code, Goose, and OpenClaw. (No benchmark numbers published at launch.)
- [GLM-5.1](https://z.ai/blog/glm-5.1) - **April 8, 2026**. 744B MoE / 40B active, 200K context. MIT license. Tops SWE-Bench Pro.
- [ZCode](https://www.scmp.com/tech/tech-trends/article/3359170/zhipu-ai-releases-harness-glm-52-model-chinese-firm-takes-aim-anthropic) - 🆕 🇨🇳 **July 2, 2026**. Zhipu's agent harness for GLM-5.2 — turns the model into an autonomous coding agent, squarely targeting Claude Code; launch promos include +50% quota for Coding Plan subscribers and 5M free tokens for new users.
- [GLM-5 Reasoning](https://z.ai/) - April 2026. BenchLM 85 — **top open-source score**. SWE-Bench Pro surpasses GPT-5.4 and Claude Opus 4.6.
- [GLM-5V-Turbo](https://z.ai/) - April 2026. Native multimodal agent — vision, video clips, text inputs. Cost-performance balanced.
- [GLM-5](https://z.ai/) - Released Feb 2026. 744B parameters, advanced agentic intelligence. MIT license.
- [GLM-4.7](https://z.ai/) - Released late 2025. Matches Claude Opus 4 on SWE-Bench.

### MiniMax

- [MiniMax M3](https://huggingface.co/MiniMaxAI/MiniMax-M3) - Open-weight multimodal model for coding and agentic work with MiniMax Sparse Attention and 1M context; weights use the MiniMax Community License.
- [MiniMax-M2.7 (Open Weights)](https://www.minimax.io/) - April 2026. 230B-class open-weight flagship. Top-tier performance on coding and Agent tasks.
- [MiniMax M2.7 (release history)](https://huggingface.co/MiniMaxAI/MiniMax-M2.7) - Earlier MiniMax agentic/coding model with downloadable weights and its own license; the hosted launch description does not mean its weights remain proprietary-only.
- [MiniMax M2.5](https://www.codemotion.com/magazine/ai-ml/minimax-m2-5-low-costs-high-performance/) - 🇨🇳 **February 2026**. 230B-parameter cost-efficient flagship for "real-world productivity".
- [MiniMax H3](https://huggingface.co/MiniMaxAI/MiniMax-H3) - 🆕 🇨🇳 **July 2026** (HF created July 28). Open-weight omni-modal generator: understands text/image/video/audio and produces **video with native stereo audio** up to 2K / 15s. 33B dense Omni Transformer; `minimax-h3-community-license-agreement`. Current MiniMax video flagship (supersedes Hailuo 2.3). 4.4M+ HF downloads.
- [Hailuo 2.3 / 2.3 Fast](https://www.minimax.io/news/minimax-hailuo-23) - 🇨🇳 **October 2025**. Predecessor video model — SOTA physics, character micro-expressions, strong stylization; Hailuo 02 (2025) remains as the I2V-focused variant. Superseded as flagship by MiniMax H3 (July 2026).
- [MiniMax Music 3.0](https://huggingface.co/MiniMaxAI/MiniMax-Music3) - 🆕 🇨🇳 **August 13, 2026**. Open-weight music model for complete songs up to **five minutes** (8B Global LLM + 0.6B Local LLM, 32 kHz 16-bit stereo WAV). Current MiniMax music flagship.
- [MiniMax Music 2.6](https://aimlapi.com/blog/the-ultimate-guide-to-minimax-models-2026-m2-7-music-2-6-hailuo-video-advanced-tts) - 🇨🇳 **April 10, 2026**. Cover-generation predecessor; superseded as flagship by Music 3.0.
- [MiniMax-M1-80k](https://www.minimax.io/) - Open-weight hybrid-attention reasoning model. 456B parameters, 1M token context.
- [Hailuo AI (Video)](https://hailuoai.video/) - Text/image-to-video generation with AI avatars, voiceovers, and character consistency.
- [Kilo Code Integration](https://www.minimax.io/) - MiniMax models are heavily featured in Kilo Code (open-source AI coding extension at kilo.ai).

### Moonshot AI (Kimi)

- [Kimi K3](https://huggingface.co/moonshotai/Kimi-K3) - Open-weight multimodal MoE with 2.8T total / 104B active parameters and 1M context; the custom Kimi K3 License includes additional terms for large model-service businesses.
- [Kimi K2.7 Code](https://kimi.ai/) - **June 12, 2026**. Coding-first successor to K2.6 — 1T MoE / 32B active (384 experts), 256K context, Modified MIT, on Hugging Face + Kimi API. Targets long-horizon agentic coding with ~30% lower reasoning-token use; Moonshot reports +21.8% over K2.6 on its Kimi Code Bench v2 (vendor benchmarks). $0.95 / $4.00 per million in/out tokens.
- [Kimi K2.6](https://kimi.ai/) - **April 20-21, 2026**. 1T MoE / 32B active, 256K context. Enhanced coding, long multi-step execution, **agent swarm up to 1,000 collaborating agents**. Supports `thinking.keep="all"` persistent reasoning. Default in OpenClaw v2026.4.20+.
- [Kimi K2.5](https://kimi.ai/) - Jan-Feb 2026. 1T total / 32B active MoE. Native multimodal, Agent Swarm (up to 100 parallel sub-agents). Open-source. ⚠️ Support ended May 25, 2026; no longer available to newly registered users, with **full platform sunset on August 31, 2026** — migrate to K2.6.
- [Kimi Code](https://kimi.ai/) - Premium coding tier powered by K2.5/K2.6, terminal-based developer workflows.

### ByteDance (Doubao / 豆包)

- [Seed 2.1](https://seed.bytedance.com/en/seed2_1) - 🆕 Current Seed model for general agent tasks and end-to-end coding, with official evaluations and product access links.
- [Doubao 2.0](https://www.taipeitimes.com/News/biz/archives/2026/02/16/2003852382) - 🇨🇳 **February 2026**. Agent-era upgrade focused on real-world task execution; powers ByteDance's consumer AI apps.
- [Seedance 2.0](https://economictimes.indiatimes.com/us/news/seedance-2-0-goes-live-as-bytedances-ai-videos-ignite-china-market-rally/articleshow/128150649.cms) - 🇨🇳 **February 2026**. Multi-modal cinematic video generation, 2K resolution, ~30% faster than Seedance 1.5.
- [Doubao-Seed-2.0 Pro](https://seed.bytedance.com/en/seed2) - Seed 2.0 Pro is the reasoning and agentic-work tier of ByteDance's Seed 2.0 family; use the regional ModelArk catalog for endpoint availability and pricing.
- [Doubao-Seed-2.0 Lite](https://seed.bytedance.com/) - General production workloads. Balanced performance and efficiency.
- [Doubao-Seed-2.0 Code](https://seed.bytedance.com/) - Software development — code generation, debugging, and review.
- [BAGEL](https://github.com/bytedance-seed/BAGEL) - Open-source multimodal model for text, image, and video understanding and generation.

### Amazon (Nova)

- [Nova 2 Omni](https://docs.aws.amazon.com/nova/) - Multimodal understanding and generation member documented in the Amazon Nova 2 lineup.
- [Nova 2 Pro](https://docs.aws.amazon.com/nova/) - Reasoning member of the Nova 2 family; consult the Amazon Nova 2 guide for access, regional availability and supported modalities.
- [Nova 2 Lite](https://aws.amazon.com/nova/) - **December 2, 2025**. Fast, cost-effective reasoning with 1M-token context. Adjustable "thinking effort" controls.
- [Nova 2 Sonic](https://aws.amazon.com/nova/) - **December 2, 2025**. Speech-to-speech model for real-time conversational AI. Multilingual.
- [Nova Act](https://aws.amazon.com/nova/) - **December 2, 2025**. Browser-based AI agent service for web task automation, re-launched powered by Nova 2 Lite.
- [Nova Forge](https://aws.amazon.com/nova/) - **December 2, 2025**. "Open training" service for building custom Nova model variants with proprietary data.

### NVIDIA (Nemotron)
- [Nemotron 3.5 Lightning](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Lightning-30B-A3B-BF16) - Open-weight 30B / 3B-active model for efficient agentic workloads, with official BF16 and NVFP4 checkpoints; follow the NVIDIA license attached to each artifact.
- [Nemotron 3.5 ASR](https://developer.nvidia.com/nemotron) - **June 6, 2026**. NVIDIA's 600M-parameter cache-aware streaming speech recognition model — real-time transcription across 40 language-locales.
- [Nemotron 3 Ultra (550B)](https://research.nvidia.com/labs/nemotron/Nemotron-3-Ultra/) - 🆕 **June 4, 2026**. Open-weight 550B-total / 55B-active hybrid Mamba-Transformer MoE for long-running agents. Frontier-level reasoning among US open models, optimized for Blackwell.
- [Nemotron-Labs-TwoTower](https://huggingface.co/nvidia/Nemotron-Labs-TwoTower-30B-A3B-Base-BF16) - 🆕 🧪 **July 1, 2026**. Open-weight diffusion language model from NVIDIA Research, adapted from a frozen Nemotron-3-Nano-30B-A3B backbone — one tower holds context, the other writes tokens in parallel for ~2.4× throughput without retraining.
- [Nemotron 3 Super](https://developer.nvidia.com/nemotron) - Released March 11, 2026 (GTC). 120B total / 12B active. 1M context. 5x higher throughput vs predecessor.
- [Nemotron 3 Nano](https://developer.nvidia.com/nemotron) - **December 15, 2025**. Cost-efficient hybrid Transformer-Mamba MoE. Optimized for targeted agentic tasks.
- [Nemotron 3 Nano Omni](https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents/) - **April 28, 2026**. 30B-A3B hybrid MoE (Mamba + Transformer). Natively multimodal: text, image, audio, video, charts, and documents in one model. 9x higher throughput than comparable open omni models. Topped 6 leaderboards (MMlongbench-Doc, OCRBenchV2, WorldSense, DailyOmni, VoiceBench). Open weights on Hugging Face, OpenRouter, Amazon SageMaker JumpStart.

### Tencent (Hunyuan)

- [Hunyuan Hy3](https://huggingface.co/tencent/Hy3) - Apache-2.0 open-weight MoE for reasoning and tool use, with an official checkpoint and deployment guidance.
- [Hunyuan Hy3 Preview](https://hy.tencent.com/hy3-preview) - 🇨🇳 **April 2026**. Preview that preceded the official Hy3: fast-slow thinking fusion architecture, 40% improved inference efficiency, vLLM and SGLang support. Open-sourced on GitHub, Hugging Face, ModelScope, GitCode. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2FTencent-Hunyuan%2FHy3-preview&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)

### Apple

- [Apple Foundation Models 3 / ADM 3 Cloud](https://machinelearning.apple.com/research/introducing-third-generation-of-apple-foundation-models) - **June 8, 2026**. Five-model family: on-device AFM 3 Core/Core Advanced, server AFM 3 Cloud/Cloud Pro, and ADM 3 Cloud for image generation on Private Cloud Compute.
- [OpenELM](https://machinelearning.apple.com/research/openelm) - Open-source efficient language models (270M–3B). Designed for on-device processing on Apple silicon.

### Samsung

- [Samsung Gauss2](https://news.samsung.com/sg/samsung-electronics-hosts-samsung-developer-conference-korea-2024-unveils-its-improved-gen-ai-model) - Samsung's officially documented proprietary multimodal family has Compact, Balanced and Supreme variants for internal productivity; a public Gauss 2.3 API/model card was not verified in this refresh.

### StepFun

- [Step 3.7 Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash) - Apache-2.0 open-weight vision-language MoE for agentic coding and search, with official deployment instructions.
- [Step 3.5 Flash](https://github.com/stepfun-ai/Step-3.5-Flash) - 🇨🇳 **February 2026**. Open-weight 196B MoE (11B active) reasoning + agent model; punches above its weight against larger rivals.

### Baichuan

- [Baichuan-M4 (research)](https://arxiv.org/abs/2606.08982) - **June 8, 2026**. Research report on a medical agent system for continuous care, combining a reasoning model, persistent patient memory, evidence retrieval and multimodal clinical tools; public API/weight availability is not established by the paper.
- [Baichuan-M3-235B](https://huggingface.co/baichuan-inc/Baichuan-M3-235B) - Official 235B medical-domain model with downloadable Apache-2.0 weights.
- [Baichuan-M3 Plus](https://github.com/baichuan-inc/baichuan-mcp-servers/blob/main/packages/baixiaoying-mcp-server/README_EN.md) - Medical-domain model with an application-based access program for eligible institutions; availability and use restrictions are defined by Baichuan.

### Inflection AI

- [Inflection 2.5 / Pi](https://inflection.ai/labs) - Historical Inflection generation; the lab remains active in personal-intelligence research and Pi products, so it should not be treated as an abandoned project.

### 01.AI

- [Yi-Lightning](https://www.01.ai/) - **October 2024**. Historical 100B MoE release; 01.AI's current product focus includes enterprise platforms such as TrueNorth, released in July 2026.

### Chinese Academy of Sciences

- [ScienceOne 100 / 磐石100](https://english.cas.cn/newsroom/cas-in-media/202604/t20260429_1158251.shtml) - **April 2026**. CAS scientific AI system built around ScienceOne and discipline-specific models, with research tools for scientific workflows.

---

## 🎨 Multimodal & Generative AI

*Tools and models for generating and editing images, videos, audio, and music.*

### Image Generation

- [Nano Banana 2 Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite-image) - Google's efficient image generation/editing variant, exposed as `gemini-3.1-flash-lite-image` in the Gemini API.
- [Grok Imagine Image 2.0](https://x.ai/news/grok-imagine-image-2) - 🆕 **August 7, 2026**. SpaceXAI's image generation/editing model — magic-wand editing, segmentation, background removal, multi-reference editing (up to 5 images), and smart resize; ranked **#2 worldwide on Arena in both text-to-image and image editing** at launch. Available on grok.com/imagine, iOS/Android, and the API as `grok-imagine-image-2.0`.
- [Meta Muse Image](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) - 🆕 **July 7, 2026**. Meta's most advanced image generation model from MSL — agentic design that performs web search, code execution, and self-refinement before producing images. Rolled out in Instagram Stories (US) and WhatsApp in limited countries (Facebook coming soon). Also accessible in the Meta AI app and on meta.ai.
- [Midjourney V8.1 / V8.2 Edit (alpha)](https://updates.midjourney.com/alpha-changelog-9-2-26/) - **September 3, 2026 update**. V8.2 Edit is available on the alpha site with instruction-based edits and up to four reference images; the main generation model remains V8.1.
- [FLUX.2 Pro / Flex / Dev / Klein](https://bfl.ai/blog/flux-2) - 🆕 **November 25, 2025**. Black Forest Labs' next-generation family. SOTA image quality, multi-reference consistency (up to 10 images), dramatically improved text rendering; open-weight 32B Dev variant.
- [Recraft V4 / V4.1](https://www.recraft.ai/blog/introducing-recraft-v4-design-taste-meets-image-generation) - 🆕 **February 17, 2026** (V4.1 **May 14, 2026**). Ground-up rebuild; major prompt-accuracy improvements; editable SVG vector output. V4.1 adds better photorealism, 3D/gradients, and Vector/Utility variants.
- [Stable Diffusion 3.5](https://huggingface.co/stabilityai/stable-diffusion-3.5-large) - Open-weight image generation under the Stability AI Community License, with separate commercial terms where applicable; not Apache-2.0.
- [Ideogram 4.0](https://ideogram.ai/models/4.0/) - Image generation and editing with multilingual typography and layout control; public quantized weights use the [Ideogram Non-Commercial Model Agreement](https://ideogram.ai/licensing/), with separate commercial licenses.
- [P-Image-Ideogram](https://ideogram.ai/tools/p-image-ideogram/) - Pruna and Ideogram image-model family offering multiple quality, latency and cost tradeoffs.
- [Ideogram 3.0](https://ideogram.ai/) - Excels at text rendering in images; March 2025 release with style references and in-platform canvas editor.
- [ChatGPT Images 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/) - 🆕 **April 21, 2026**. State-of-the-art image generation with improved text rendering, multilingual support, advanced visual reasoning, and multi-turn editing for iterative refinement.
- [gpt-image-2](https://developers.openai.com/api/docs/models/gpt-image-2) - 🆕 **April 21, 2026**. OpenAI's latest image generation/editing API model with flexible image sizes and high-fidelity inputs. **August 20, 2026**: transparent-background **preview** (`background=transparent`, `png`/`webp` only) on `gpt-image-2` and `gpt-image-2-2026-04-21` in the Images API and Responses image tool ([changelog](https://developers.openai.com/api/docs/changelog.md)).
- [MAI-Image-2.6](https://microsoft.ai/news/mai-image-2-6-launches-at-no-2-on-arena-ahead-of-google-meta-and-xai/) - 🆕 **August 10, 2026** (editing leaderboard **August 18**). Microsoft's in-house image model — Arena T2I #2 at launch, Arena image-editing #3 by Aug 18. See Foundation → Microsoft (MAI).
- [DALL·E 3](https://developers.openai.com/api/docs/deprecations) - 📦 Historical text-to-image model; the `dall-e-3` API was retired on **May 12, 2026** and the documented replacement is the GPT Image family.
- [Gemini 3 Pro Image (Nano Banana Pro)](https://deepmind.google/models/gemini-image/pro/) - Google's native image generation within Gemini.
- [Nano Banana 2.1](https://ai.google.dev/gemini-api/docs/changelog) - 🆕 **October 6, 2026**. Generally available update to Nano Banana 2 (`gemini-nano-banana-2.1`) for image generation and conversational editing; `gemini-3.1-flash-image` is deprecated with no shutdown date announced yet.
- [Nano Banana 2 (Gemini 3.1 Flash Image)](https://blog.google/innovation-and-ai/technology/ai/nano-banana-2/) - 🆕 **February 26, 2026**. Nano Banana Pro-level quality and world knowledge at Flash speed; up to 5-character consistency, 512px–4K output, text rendering/translation in images.
- [Kling Image 3.0 / 3.0 Omni](https://ir.kuaishou.com/news-releases/news-release-details/kling-ai-launches-30-model-ushering-era-where-everyone-can-be/) - 🇨🇳 🆕 **February 5, 2026**. Kuaishou's native 2K/4K image generation, launched alongside Video 3.0 in the Kling 3.0 suite.
- [Flux](https://github.com/black-forest-labs/flux) - 💤 **Stale** (last update 2025-07). Black Forest Labs' original open-source repo — superseded by Flux 2 family. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fblack-forest-labs%2Fflux&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Seedream 5.0 Pro](https://seed.bytedance.com/en/blog/beyond-generation-it-understands-design-introducing-seedream-5-0-pro) - **July 8, 2026**. ByteDance's image creation model for layouts, text rendering and multimodal design; Seedream is the image family, while Seedance is the video family.
- [Qwen-Image-3.0](https://qwenlm.github.io/) - 🆕 🇨🇳 **July 20, 2026**. Alibaba's third-generation image generation model, unveiled at the World AI Conference. Significant improvements in photorealism, text rendering, and multi-subject consistency. Available via Alibaba Cloud Bailian and Qwen Cloud.
- [FLUX 3](https://bfl.ai/blog/flux-3) - 🆕 **July 23, 2026 (Early Access)**. Black Forest Labs' pivot from a still-image family to a unified multimodal foundation model that jointly learns from images, video and audio in one architecture. Generates video **up to 20 seconds with native synchronized audio** (text-to-video, image-to-video, video-to-video, keyframe-to-video, multilingual dialogue, agentic multi-shot chaining). In BFL's own early evaluations FLUX 3 was preferred over Runway Gen-4.5 in 77% of comparisons, Luma Ray 3.2 in 93%, Kling v3 Pro in 60%, and Seedance 2.0 / Gemini Omni Flash in 52% — vendor-reported and explicitly preliminary. World understanding also extends to **action prediction** for robotics. FLUX 3 Image early access still pending as of mid-August 2026.
- [Reve](https://reve.com/) - 🆕 "Layout-first" image model — it plans a structured, editable layout before rendering pixels, so individual elements can be moved, resized or recolored and re-rendered without regenerating the whole frame. Native 4K, sketch/annotation input, and direct object editing.

### Video Generation

- [Runway Aleph 2.0](https://docs.dev.runwayml.com/guides/models/) - Runway video-editing model exposed as `aleph2`, with video/text/image input and professional output formats.
- [Meta Muse Video](https://ai.meta.com/blog/introducing-muse-image-muse-video-msl/) - 🆕 **July 7, 2026 (preview)**. Video generation model from Meta Superintelligence Labs built on the same architecture as Muse Image; ranks #3 on Arena for text-to-video. Previewed at the Muse Image launch; broader rollout anticipated across Meta apps.
- [Runway Agent](https://runwayml.com/news/introducing-runway-agent) - 🆕 **May 13, 2026**. Conversational agent that takes a written brief and ships a complete **multi-shot finished video**: storyboard → generation → cut → voiceover, with a timeline editor for final adjustments; first credible end-to-end "prompt-to-rough-cut" production agent.
- [Veo 3.1](https://ai.google.dev/gemini-api/docs/veo) - Video-with-audio generation, frame control and extension; Gemini API preview supports 4/6/8-second clips, with 1080p/4K restricted to 8 seconds.
- [Runway Gen-4.5](https://runwayml.com/research/introducing-runway-gen-4.5) - 🆕 **December 2025**. Runway's flagship video model, #1 on the Artificial Analysis text-to-video benchmark at launch. Platform also exposes third-party models incl. Kling 3.0 and Sora 2 Pro (added February 20, 2026).
- [Kling VIDEO 3.0](https://app.klingai.com/) - 🇨🇳 🆕 **February 4-7, 2026**. Kuaishou's new generation; realistic human motion, lip-sync, narrative production with audio sync.
- [Sora 2 (via Runway)](https://runwayml.com/changelog) - OpenAI's Sora app shut down April 26, 2026 (API until September 24, 2026), but Sora 2 Pro has been available inside Runway since **February 20, 2026**.
- [Seedance 2.5](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) - 🇨🇳 🆕 **July 31, 2026 (official release)**. ByteDance's next-gen video model (announced June 23 at the Volcano Engine 2026 conference): native 30-second one-shot generation with multi-round extensions, flexible referencing (up to **30 images + 10 video clips + 10 audio clips** in a single pass), and improved character/product consistency. Rolling out on Jimeng AI and Doubao Pro in China; API via BytePlus ModelArk pre-release — no official global rate card yet.
- [Seedance 2.0](https://seed.bytedance.com/) - 🇨🇳 **February 2026**. ByteDance multi-modal cinematic video generation, 2K resolution (upgraded to 4K output June 23, 2026), ~30% faster than 1.5.
- [MiniMax H3](https://huggingface.co/MiniMaxAI/MiniMax-H3) - 🆕 🇨🇳 **July 2026**. Open-weight omni video+audio generator (2K / 15s, native stereo). Current MiniMax video flagship — see Foundation → MiniMax.
- [MiniMax-H3-Fun-Controlnet-Union](https://huggingface.co/alibaba-pai/MiniMax-H3-Fun-Controlnet-Union) - 🆕 🇨🇳 **August 24, 2026**. Alibaba PAI ControlNet-Union for H3: one checkpoint conditions on Canny / Depth / HED / MLSD / Pose and supports video inpainting (`minimax-h3-community-license-agreement`).
- [Hailuo 2.3](https://www.minimax.io/news/minimax-hailuo-23) - 🇨🇳 **October 28, 2025**. Predecessor MiniMax video model: SOTA physics, character micro-expressions, strong stylization (anime/ink-wash/game CG); Hailuo 2.3 Fast variant at Hailuo 02 pricing. Superseded as flagship by MiniMax H3.
- [Pika 2.5](https://pika.art/) - Creative video generation with scene and effects control.
- [LTX Studio](https://ltx.studio/) - AI-powered cinematic video creation platform.
- [HappyHorse 1.1](https://technode.com/2026/06/23/alibaba-unveils-happyhorse-1-1-video-generation-model-launches-global-ai-filmmaking-competition/) - 🇨🇳 🆕 **June 23, 2026**. Alibaba's video model (revealed April 10, 2026 as "HappyHorse-1.0" after topping benchmarks anonymously; rose to #2 globally). 1.1 upgrades motion dynamics, subject consistency, prompt adherence, and audio generation. Available via the HappyHorse site, Alibaba Cloud Bailian, and Qwen Cloud.
- [Sora 2 API (deprecated)](https://developers.openai.com/api/docs/deprecations) - 📦 Deprecated API with shutdown scheduled for **September 24, 2026**; retained for migration tracking, not recommended for new integrations.
- [Gemini Omni Flash 1.1](https://ai.google.dev/gemini-api/docs/omni) - Google's current default video-generation recommendation, supporting multi-turn editing through `gemini-omni-1.1-flash`; uploaded-video editing and extensions have regional restrictions.
- [Wan 3.0](https://www.alibabacloud.com/en/blog/wan-3-0-next-gen-video-generation-model-public-beta-launched) - 🆕 🇨🇳 **August 6, 2026 (public beta)**. Alibaba Tongyi Lab's next-gen video generation model — generates up to 30-second native single-shot video. Uniquely accepts documents (PDF/Word/PPT) and web pages as input alongside text, images, and audio. Intelligent duration recommendation based on prompt. Available for testing on Alibaba Cloud Model Studio and QwenCloud; full API and open weights not yet confirmed. Companion to the Qwen3.8-Max launch.
- [LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) - 🆕 **August 12, 2026**. Lightricks' open-weight video-audio world model with native multishot generation (multiple connected scenes in one pass with consistent character identity, environment, and voice across cuts), diffusion fidelity rendering, a new video decoder (sharper faces, fewer artifacts), custom Gemma 4 12B text encoder, and a prompt enhancer. Supports text-to-video, image-to-video, video-to-video, audio-to-video, and text-to-audio-video. Self-hostable, no per-generation billing. Available on Hugging Face; commercial license (full terms in LICENSE).
- [Decart Lucy 2.5](https://decart.ai/) - 🆕 **July 2026**. Real-time video/world transformation model behind Decart's "Live AI" push — continuous infinite video with physically-aware effects, billed as ~100× more efficient than persistent-compute approaches. Positioned for live streams, interactive world models and robotics/AV simulation.

### Audio & Music

- [MAI-Transcribe-2](https://microsoft.ai/news/mai-transcribe-2-is-the-fastest-most-accurate-and-cheapest-speech-recognition-model-in-the-world/) - 🆕 **September 3, 2026**. Microsoft speech-to-text model with speaker labels, word timestamps and configurable verbatim/clean transcripts.
- [Muse Voice Transcribe](https://research.meta.ai/blog/introducing-muse-voice-transcribe) - 🆕 **September 1, 2026**. Meta's real-time audio perception model for streaming ASR, diarization and speech endpoint detection.
- [Lyria 3.5](https://ai.google.dev/gemini-api/docs/models/lyria-3.5) - Google's current full-song music-generation model, documented as `lyria-3.5`; Lyria RealTime remains a separate interactive music model.
- [Qwen3-TTS](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice) - Apache-2.0 multilingual TTS family with separate Base, CustomVoice and VoiceDesign checkpoints and streaming generation.
- [Qwen3-ASR](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) - Apache-2.0 speech-recognition family with 0.6B/1.7B variants, streaming and offline inference, and 30 languages plus 22 Chinese dialects.
- [ElevenLabs Eleven v3 + ElevenAgents](https://elevenlabs.io/agents) - 🆕 2026 "audio layer of the internet" — 70+ language TTS with emotional Audio Tags, plus the AIUC-1-certified ElevenAgents voice-agent platform with multimodal messages, conversation topic discovery, and pre-tool speech controls. **July 2026 update**: Music Finetunes API (programmatic custom model management), per-agent sentiment analysis, nested agent transfers, RAG knowledge-base queries, auto-translated transcripts, faster generation with improved tonal consistency for long audio.
- [Eleven Music + Scribe v2 Realtime](https://elevenlabs.io/) - ElevenLabs' music generation and live transcription stack.
- [Cartesia Sonic 3 / 3.5](https://cartesia.ai/blog/introducing-line-for-voice-agents) - **2026**. State-space-model TTS hitting ~40-90ms time-to-first-audio (Sonic 3.5 GA May 2026); powers the **Line** voice-agent platform (Line agents run on Sonic 3.5 TTS + Ink-2 STT by default since May 2026).
- [Deepgram Nova-3 + Aura-2 + Flux Multilingual](https://deepgram.com/learn/best-voice-ai-agents-2026-buyers-guide) - **April 2026**. Speech-to-text in 45+ languages, sub-200ms TTS, conversational STT with mid-call language switching across 10 languages.
- [MiniMax Music 3.0](https://huggingface.co/MiniMaxAI/MiniMax-Music3) - 🆕 🇨🇳 **August 13, 2026**. Open-weight complete-song generator (up to 5 minutes, 32 kHz stereo). Current MiniMax music flagship — see Foundation → MiniMax.
- [MiniMax Music 2.6](https://aimlapi.com/blog/the-ultimate-guide-to-minimax-models-2026-m2-7-music-2-6-hailuo-video-advanced-tts) - 🇨🇳 **April 10, 2026** (global beta). Cover-generation predecessor; superseded by Music 3.0.
- [Voxtral TTS](https://docs.mistral.ai/models/voxtral-tts-26-03) - Mistral's multilingual speech-generation model; open weights are CC-BY-NC-4.0, distinct from Apache-2.0 Voxtral transcription weights.
- [Suno v5.5 + Studio 2.0](https://suno.com/blog/v5-5) - 🆕 **March 26, 2026** (Studio 2.0 **August 13, 2026**). AI music generation with high-quality vocals; v5.5 adds Voices (sing with your own verified voice), Custom Models trained on your uploads, and My Taste personalization. **Studio 2.0** (Aug 13) is a completely redesigned browser-based DAW with MIDI support, audio effects, and built-in synths; Voices expanded to iOS/Android free plans Aug 7. V6 rumored but unannounced.
- [Udio](https://www.udio.com/) - Text-to-music generation with professional audio quality.
- [OpenAI Audio Models](https://openai.com/) - Native audio understanding and generation within GPT-4o and GPT-Realtime-2 (**May 7, 2026**, with GPT-Realtime-Translate and GPT-Realtime-Whisper); gpt-realtime-2.1 and 2.1-mini released **July 6, 2026** with improved alphanumeric recognition, noise handling, and interruption behavior.
- [Stable Audio 3.0](https://stability.ai/stable-audio) - Audio-generation family with Large, Medium, Small and Small SFX variants; Medium and Small have open weights, with deployment rights governed by the applicable Stability license.
- [Bark](https://github.com/suno-ai/bark) - 💤 **Stale** (no commits since 2024-08). Open-source text-to-audio model supporting speech, music, and sound effects. ![GitHub stars](https://img.shields.io/badge/dynamic/json?label=Stars&query=%24.stargazers_count&url=https%3A%2F%2Fapi.github.com%2Frepos%2Fsuno-ai%2Fbark&color=yellow&logo=github&logoColor=white&style=flat&cacheSeconds=300)
- [Hume TADA](https://github.com/HumeAI/tada) - Speech-language models using 1:1 text/acoustic alignment, with TADA