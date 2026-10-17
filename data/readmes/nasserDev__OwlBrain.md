# 🦉 OwlBrain

### Multi-LLM Debate Platform — Five AI Agents. Three Providers. One Verdict.

> **OwlBrain pits five specialised AI agents against each other in structured, multi-round debates about any business case you throw at them.** Each agent can run on a different LLM — Claude argues against GPT argues against Gemini — and an independent judge scores consensus after every round. When the dust settles, a synthesizer produces a final verdict backed by the full transcript.
>
> No opinions. No single-model bias. Just structured adversarial reasoning that converges on the strongest answer.

[![Live Demo](https://img.shields.io/badge/Live-Demo-D4762C?style=for-the-badge)](https://owlbrain.ai) [![Deploy on Railway](https://img.shields.io/badge/Deploy-Railway-000?style=for-the-badge&logo=railway)](https://railway.com/deploy/owlbrain) [![License: BSL 1.1](https://img.shields.io/badge/License-BSL_1.1-orange?style=for-the-badge)](LICENSE)

---

![OwlBrain — Structured multi-agent debate](docs/assets/hero.png)

---

## The Problem

You ask ChatGPT a question — you get one model's opinion. You ask Claude — you get another. You ask Gemini — you get a third. **None of them challenge each other. None of them evolve their reasoning. None of them tell you where they disagree.**

OwlBrain fixes that.

---

## The Panel

Five agents with distinct roles, each assignable to any LLM:

| | Agent | Role | What It Does |
|:--|:------|:-----|:-------------|
| 🎯 | **The Strategist** | Strategy Lead | Builds the core recommendation and execution plan |
| 📊 | **The Analyst** | Quant Expert | Stress-tests claims with data, numbers, and evidence |
| ⚠️ | **Risk Officer** | Risk & Mitigation | Identifies failure modes, legal exposure, and downside scenarios |
| 🚀 | **The Innovator** | Creative Lead | Proposes unconventional approaches and reframes the problem |
| 😈 | **Devil's Advocate** | Challenger | Attacks the strongest position — specifically to find its weaknesses |

Each agent has a distinct persona, configurable model, and independent memory. They reference each other's arguments, track stance shifts, and call out sycophantic agreement.

---

## How It Works

```
You submit a business case
        │
        ▼
┌─────────────────────────────────────────────┐
│              ROUND 1 → ROUND N              │
│                                             │
│  🎯 Strategist ──► 📊 Analyst ──► ⚠️ Risk  │
│        │               │             │      │
│        ▼               ▼             ▼      │
│  🚀 Innovator ──────► 😈 Devil's Advocate   │
│                                             │
│         ┌──────────────────────┐            │
│         │   Consensus Judge    │            │
│         │  scores 5 dimensions │            │
│         │  detects sycophancy  │            │
│         └──────────┬───────────┘            │
│                    │                        │
│         threshold met? ──► yes ──► STOP     │
│              no ──► compress memory ──► ↑   │
└─────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────────────────────────────┐
│              FINAL VERDICT                  │
│  Synthesizer produces a structured report   │
│  backed by the full debate transcript       │
└─────────────────────────────────────────────┘
```

![A completed debate with consensus scoring](docs/assets/debate.png)

**Consensus is scored across five dimensions:**

| Dimension | What the Judge Evaluates |
|:----------|:------------------------|
| Core Recommendation | Is there a clear, unified recommendation? |
| Reasoning | Is the reasoning well-supported and logically sound? |
| Execution Plan | Are there concrete, actionable steps? |
| Risk Assessment | Have risks been identified and addressed? |
| Stability | Have positions converged or are agents still shifting? |

---

## Features

🔀 **Multi-LLM Orchestration** — Assign different models to different agents. Run Claude as your strategist, GPT as your analyst, and Gemini as your devil's advocate in the same debate.

🧠 **18 Models Across 3 Providers** — Claude Opus 4.6, Sonnet 4.6, Haiku 4.5 · GPT-5.4, GPT-5, o4-mini, o3, GPT-4o · Gemini 3.1 Pro, 3 Flash, 2.5 Pro, 2.5 Flash — and more. Adding a new model is one catalog entry.

⚖️ **Consensus Scoring** — An independent judge evaluates the panel after each round. Scores range 0–100 with per-dimension breakdowns and written rationale.

🔍 **Sycophancy Detection** — The judge flags when agents agree too readily without substantive reasoning. Shallow consensus gets called out, not rewarded.

🔄 **Two Debate Modes** — *Sequential*: agents see previous responses and build on them. *Independent*: agents argue in isolation to eliminate anchoring bias.

📡 **Real-Time Streaming** — Watch the debate unfold live via Server-Sent Events. Responses stream as they're generated.

🧾 **Memory & Stance Tracking** — Tracks every agent's position across rounds, detects stance shifts, compresses history, and feeds structured memory bundles into later rounds.

🌐 **Web Search** — Any agent can ground arguments in real-time web data. Supported across Anthropic, OpenAI, and Google.

🎛️ **Full Control Room** — Configure every parameter: models, temperature, reasoning effort, thinking budgets, web search, frequency penalties, word limits, system prompts, and presets.

📝 **Synthesis & Verdict** — A dedicated synthesizer produces a structured final report that references the full transcript, acknowledges dissent, and delivers an actionable recommendation.

💾 **SQLite Persistence** — Every debate is saved with full round data, scores, event logs, config snapshots, and token usage. Browse or replay any past debate.

🔒 **Demo Mode** — Host a public demo with built-in rate limiting, token caps, model locking, and showcase debates. One env var activates everything.

---

## Supported Models

**Anthropic**

| Model | Tier | Web Search | Structured Output |
|:------|:-----|:----------:|:-----------------:|
| Claude Opus 4.6 | Flagship | ✅ | ✅ |
| Claude Sonnet 4.6 | Balanced | ✅ | ✅ |
| Claude Sonnet 4.5 | Balanced | ✅ | ✅ |
| Claude Haiku 4.5 | Fast | ✅ | ✅ |

**OpenAI**

| Model | Tier | Reasoning | Web Search | Structured Output |
|:------|:-----|:---------:|:----------:|:-----------------:|
| GPT-5.4 | Flagship | ✅ | ✅ | — |
| GPT-5.4 Pro | Flagship | ✅ | ✅ | — |
| GPT-5 | Reasoning | ✅ | ✅ | — |
| GPT-5 Mini | Budget | ✅ | ✅ | — |
| o4-mini | Reasoning | ✅ | ✅ | — |
| o3 | Reasoning | ✅ | ✅ | — |
| GPT-4.1 | Chat | — | ✅ | ✅ |
| GPT-4o | Chat | — | ✅ | ✅ |

**Google**

| Model | Tier | Thinking | Web Search | Structured Output |
|:------|:-----|:--------:|:----------:|:-----------------:|
| Gemini 3.1 Pro | Flagship | ✅ | ✅ | ✅ |
| Gemini 3 Flash | Fast | ✅ | ✅ | ✅ |
| Gemini 3.1 Flash-Lite | Budget | ✅ | ✅ | — |
| Gemini 2.5 Pro | Balanced | ✅ | ✅ | ✅ |
| Gemini 2.5 Flash | Balanced | ✅ | ✅ | ✅ |
| Gemini 2.5 Flash-Lite | Budget | ✅ | ✅ | ✅ |

> 💡 Adding a new model? One entry in `server/modelCatalog.ts`. That's it.

---

## Quick Start

**Prerequisites:** [Node.js 20+](https://nodejs.org/) and at least one API key from [Anthropic](https://console.anthropic.com/), [OpenAI](https://platform.openai.com/), or [Google AI](https://aistudio.google.com/).

```bash
git clone https://github.com/nasserDev/OwlBrain.git
cd owlbrain
npm install
cp .env.example .env    # Add your API keys
npm run dev             # Open http://localhost:5000
```

That's it. Five agents, ready to argue.

---

## Deploy to Railway

```bash
npm install -g @railway/cli
railway login
railway init
railway up
```

Set your API keys in the Railway dashboard. The app builds and deploys automatically.

---

## Configuration

Everything is configurable from the **Control Room** in the UI. For environment-level defaults:

```env
# Provider API Keys (set at least one)
ANTHROPIC_API_KEY=your-key
OPENAI_API_KEY=your-key
GEMINI_API_KEY=your-key

# Server
PORT=5000
ADMIN_API_KEY=your-admin-password

# Demo Mode (for public deployments)
DEMO_MODE=false
DEMO_DAILY_TOKEN_CAP=5000000
DEMO_MAX_DEBATES_PER_IP_PER_DAY=3
DEMO_MAX_ROUNDS=3
```

See [`.env.example`](.env.example) for every option.

---

## Architecture

```
owlbrain/
├── client/src/
│   ├── pages/           DebatePage · AdminPage · ShowcasePage
│   ├── components/      AuthGate · DemoBanner · UI library
│   ├── context/         DemoStatusContext
│   └── lib/             Query client · debate state · utilities
│
├── server/
│   ├── orchestrator.ts  Debate execution engine
│   ├── llmRouter.ts     Multi-provider LLM routing
│   ├── consensus.ts     Consensus judge & 5-dimension scoring
│   ├── synthesizer.ts   Final verdict generation
│   ├── memory.ts        Stance tracking & round compression
│   ├── promptBuilder.ts Prompt construction per round & mode
│   ├── configStore.ts   SQLite persistence layer
│   ├── modelCatalog.ts  Supported model registry
│   ├── demoConfig.ts    Demo mode restrictions
│   ├── demoGuards.ts    Rate limiting & budget protection
│   └── routes.ts        API endpoints & SSE streaming
│
├── shared/              Shared types & validation schemas
├── .env.example         Environment template
├── railway.toml         Railway deployment config
└── nixpacks.toml        Build environment config
```

**Tech Stack**

| Layer | Technology |
|:------|:-----------|
| Frontend | React 18 · TanStack Query · Tailwind CSS · shadcn/ui |
| Backend | Node.js 20 · Express 5 · TypeScript |
| Database | SQLite via better-sqlite3 |
| LLM SDKs | @anthropic-ai/sdk · openai · @google/genai |
| Build | Vite · esbuild · tsx |
| Streaming | Server-Sent Events |

---

## Demo Mode

Hosting OwlBrain for the public? One environment variable protects your budget:

```env
DEMO_MODE=true
```

**What activates:**

| Protection | Default |
|:-----------|:--------|
| Per-IP debate limit | 3 per day |
| System-wide daily token cap | 5M tokens |
| Per-debate token cap | 150K tokens |
| Model selection | Locked to cheapest viable combo |
| Thinking / reasoning tokens | Disabled |
| Admin panel | Read-only (operator password for changes) |
| Showcase debates | Pre-seeded as instant fallback |
| Capacity messaging | Graceful redirect to showcase |

Every restriction is configurable. Every guard is server-enforced. The same code runs in demo and full mode — the flag just activates the restriction profile.

---

## Contributing

Contributions are welcome. Open an issue first to discuss what you'd like to change.

```bash
npm run dev       # Dev server with hot reload
npm run check     # TypeScript type checking
npm test          # Run test suite
npm run build     # Production build
npm start         # Start production server
```

---

## License

OwlBrain is source-available under the **Business Source License 1.1**.

**Free for** personal use, research, education, evaluation, and non-commercial projects.

**Commercial use** requires a separate license. [Contact me](mailto:nasserdevx@outlook.com) for details.

The license converts to **Apache 2.0** on the change date specified in the [LICENSE](LICENSE) file.

---

## Acknowledgements

Built with the same models that power the debates: [Claude](https://claude.ai), [GPT](https://platform.openai.com), and [Gemini](https://ai.google.dev).

---

*Built by [nasserDev](https://github.com/nasserDev)*
