<div align="center">

<img src=".github/assets/logo.png" alt="LOOM Logo" width="120" />

# GenUI-LoomAgent

**AI decides what to show, not just what to say.**

An open-source Generative UI Agent framework — the AI doesn't just return text, it autonomously decides which UI components to render.

Plug in any REST API via YAML config. No backend code changes needed.

[![AG-UI Compatible](https://img.shields.io/badge/AG--UI-Compatible-00C896?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyTDIgN2wxMCA1IDEwLTV6TTIgMTdsIDEwIDUgMTAtNS01LTIuNUwxMiAxN2wtNSAyLjV6Ii8+PC9zdmc+)](https://ag-ui.com)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Next.js](https://img.shields.io/badge/Next.js-15-000000?style=flat-square&logo=next.js)](https://nextjs.org)

**[English](README.md)** · [中文](README.zh-CN.md)

<img src=".github/assets/demo.gif" alt="GenUI-LoomAgent Demo" width="700" />

[Quick Start](#-quick-start) · [Architecture](#-architecture) · [AG-UI Protocol](#-ag-ui-protocol) · [Add Services](#-add-services) · [Contributing](CONTRIBUTING.md)

</div>

---

## What is LOOM?

LOOM is a **Generative UI (GenUI) Agent** framework. Traditional AI apps return plain text. LOOM's AI backend generates text responses **and** autonomously decides which UI components to render — data lists, comparison tables, charts, weather cards, trip cards, and more — all orchestrated by the AI in real time.

```
User: "What's the weather like in Beijing tomorrow?"

Traditional AI  →  A paragraph describing the weather
LOOM AI         →  Short summary + WeatherCard (temp/humidity/wind) + Graph (7-day trend)

User: "Find me a train from Beijing to Shanghai"

Traditional AI  →  A paragraph listing trains
LOOM AI         →  Brief summary + TripCard (train/time/price) + DataList (available options)
```

### Core Features

| Feature | Description |
|---------|-------------|
| **GenUI Dynamic Rendering** | AI returns `{ name, props }` instructions, frontend dynamically renders registered components |
| **Declarative Service Integration** | Add any REST API via YAML config — 5 lines to connect a new data source |
| **Multi-Intent Parallel Processing** | Single message with multiple needs → automatic task decomposition and parallel execution |
| **Emotional Memory System** | Time-aware context + behavioral signals + user memory extraction — AI remembers your preferences |
| **Narrative Flow** | Not just "text + card" stitching, but story-driven information delivery with mood and rhythm |
| **Streaming SSE** | Real-time streaming responses with interrupt and retry support |
| **AG-UI Protocol** | Compatible with [AG-UI](https://ag-ui.com) standard protocol, works with CopilotKit and other AG-UI clients |
| **Mobile Ready** | Capacitor for iOS packaging, mobile-first UI design |

### Tech Stack

| Layer | Technologies |
|-------|-------------|
| Frontend | Next.js 15 · React 19 · TypeScript · Tailwind CSS v4 |
| Backend | Python · FastAPI · LangGraph |
| LLM Gateway | [LiteLLM](https://github.com/BerriAI/litellm) — unified interface for **any** LLM provider |
| Protocol | [AG-UI](https://ag-ui.com) (Agent-User Interaction Protocol) |
| Database | MongoDB |
| Mobile | Capacitor (iOS) |
| Testing | Vitest · React Testing Library · Pytest |

### Supported LLM Providers

Powered by [LiteLLM](https://github.com/BerriAI/litellm), LOOM works with **any** LLM provider out of the box. Just set `LLM_MODEL` and `LLM_API_KEY` in your `.env`:

| Provider | Example `LLM_MODEL` | Notes |
|----------|---------------------|-------|
| [OpenRouter](https://openrouter.ai/) | `openrouter/google/gemini-2.5-pro` | Access 200+ models through one API key |
| OpenAI | `openai/gpt-4o` | |
| Anthropic | `anthropic/claude-sonnet-4-20250514` | |
| Google | `gemini/gemini-2.5-pro` | |
| DashScope (Qwen) | `dashscope/qwen3.5-plus` | Recommended for Chinese users |
| DeepSeek | `deepseek/deepseek-chat` | |
| Any OpenAI-compatible | Set `LLM_BASE_URL` | Works with any provider that supports the OpenAI API format |

You can also set `LLM_FAST_MODEL` separately for lightweight tasks (intent recognition, memory extraction) to reduce cost.

### Search Services

LOOM supports web search via YAML-configured REST APIs:

| Service | Best For | Env Var |
|---------|----------|---------|
| [Zhipu AI Web Search](https://open.bigmodel.cn/) | **Chinese content** — better results for Chinese queries | `ZHIPU_API_KEY` |
| [Tavily](https://tavily.com/) | **International content** — deep search with extracted content | `TAVILY_API_KEY` |

Both can be enabled simultaneously — the AI will choose the most appropriate one based on the query language and context.

---

## 🚀 Quick Start

### Option A: Docker (Recommended)

```bash
git clone https://github.com/qingkongzhiqian/GenUI-LoomAgent.git
cd GenUI-LoomAgent

cp backend/.env.example backend/.env
# Edit backend/.env — fill in your LLM API key

docker compose up
```

Open http://localhost:3000 — frontend, backend, and MongoDB are all running.

### Option B: Manual Setup

#### Prerequisites

- Node.js 20+
- Python 3.10+
- MongoDB (local or cloud)

#### 1. Frontend

```bash
cd frontend
npm install
cp example.env.local .env.local
npm run dev
```

Open http://localhost:3000

#### 2. Backend

```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Edit .env — fill in your LLM API key (DashScope or OpenAI)

python run.py
```

Backend runs at http://localhost:8000

### Configuration

**Frontend** (`frontend/.env.local`):

| Variable | Description |
|----------|-------------|
| `BACKEND_URL` | Backend address for SSR proxy |
| `NEXT_PUBLIC_BACKEND_URL` | Client-side direct URL (for Capacitor) |

**Backend** (`backend/.env`):

| Variable | Description |
|----------|-------------|
| `LLM_MODEL` | Model identifier (e.g. `openrouter/google/gemini-2.5-pro`, `dashscope/qwen3.5-plus`) |
| `LLM_API_KEY` | API key for your LLM provider |
| `LLM_BASE_URL` | Custom endpoint (optional, for OpenAI-compatible providers) |
| `LLM_FAST_MODEL` | Lightweight model for fast tasks (optional, defaults to `LLM_MODEL`) |
| `MONGODB_URI` | MongoDB connection string |
| `JWT_SECRET` | JWT signing key |
| `TAVILY_API_KEY` | Tavily search API key (optional) |
| `ZHIPU_API_KEY` | Zhipu AI search API key (optional) |

Generate a JWT secret: `python -c "import secrets; print(secrets.token_urlsafe(32))"`

### Deploy

**Frontend → Vercel** (one click):

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/qingkongzhiqian/GenUI-LoomAgent&env=BACKEND_URL&envDescription=Your%20backend%20API%20URL)

Set `BACKEND_URL` to your backend's public URL. Set **Root Directory** to `frontend`.

**Backend → Any Python host** (Railway, Render, fly.io, etc.):

```bash
cd backend
pip install -r requirements.txt
python run.py
```

---



### LangGraph Nodes

| Node | Responsibility |
|------|---------------|
| **Initializer** | Loads chat history, user memory, environmental context, and emotional context in parallel |
| **Planner** | Intent recognition and task decomposition — splits complex requests into dependency-ordered execution plans |
| **Executor** | Runs plan steps — independent steps execute in parallel, dependent steps wait for prerequisites |
| **Evaluator** | Conditional routing — if steps remain, loop back to Executor; otherwise proceed to Synthesizer (max 5 iterations) |
| **Synthesizer** | Generates final text response + GenUI component instructions; emits AG-UI events |

### Data Flow

```
User Input
  → Initializer (load history, memory, emotional context)
  → Planner (intent recognition + task decomposition)
  → Executor (parallel sub-task execution)
    ├─ Chat intent → mark as complete
    └─ Service intent → REST API call via adapter
  → Evaluator (check completion, loop or proceed)
  → Synthesizer (refine results → generate text + components)
  → AG-UI Event Stream → Frontend
    ├─ TEXT_MESSAGE_CHUNK  (streaming text)
    ├─ TOOL_CALL_START / ARGS / END / RESULT  (service calls)
    ├─ CUSTOM genui:components  ({ name, props })
    ├─ CUSTOM genui:narrative  (mood, opener, insight, next_actions)
    └─ CUSTOM genui:sources  (reference links)
  → Component Registry → Dynamic UI Rendering
```

### GenUI Components

The AI can dynamically render any of these registered components:

| Component | Use Case |
|-----------|----------|
| **DataList** | Lists, bullet points, resource collections |
| **DetailPanel** | Knowledge cards, entity details |
| **DataTable** | Comparisons, rankings, parameter tables |
| **Graph** | Bar / Line / Pie charts |
| **TripCard** | Travel and transportation info |
| **WeatherCard** | Weather forecasts |
| **MetricCard** | KPIs and numeric indicators |
| **StepCard** | Step-by-step processes |
| **QuoteCard** | Quotes, definitions, facts |
| **POIList** | Points of interest |
| **LinkPreview** | URL previews |
| **ClarifyCard** | Clarification questions |

---

## 🔌 AG-UI Protocol

GenUI-LoomAgent is compatible with [AG-UI (Agent-User Interaction Protocol)](https://ag-ui.com) — an open standard that defines how AI agents interact with frontend applications in real time.

### Why AG-UI?

AG-UI complements MCP and A2A to form a complete Agent protocol stack:

| Protocol | Role |
|----------|------|
| **MCP** | Gives agents access to tools |
| **A2A** | Agent-to-agent communication |
| **AG-UI** | Agent-to-user interface (this project) |

### Event Stream

The backend sends standard AG-UI events via SSE:

```
RUN_STARTED → STEP_STARTED → ACTIVITY_SNAPSHOT (execution plan)
→ TOOL_CALL_START → TOOL_CALL_ARGS → TOOL_CALL_END → TOOL_CALL_RESULT
→ TEXT_MESSAGE_CHUNK → CUSTOM("genui:components")
→ CUSTOM("genui:narrative") → RUN_FINISHED
```

### GenUI Extension Events

On top of AG-UI standard events, this project uses `CUSTOM` events for GenUI-specific capabilities:

| Event Name | Purpose |
|------------|---------|
| `genui:components` | AI-generated UI component list (`[{ name, props }]`) |
| `genui:narrative` | Narrative flow data (mood, insight, suggested actions) |
| `genui:clarify` | Clarification questions when user intent is ambiguous |
| `genui:sources` | Reference links and data sources |

### Third-Party Integration

Any AG-UI compatible frontend client (e.g. [CopilotKit](https://copilotkit.ai/), `@ag-ui/client`) can connect directly to the backend:

```typescript
import { HttpAgent } from "@ag-ui/client";

const agent = new HttpAgent({
  url: "http://localhost:8000/api/chat/stream",
});

const result = await agent.runAgent({
  messages: [{ id: "1", role: "user", content: "What's the weather in Beijing?" }],
});
```

---

## 🔧 Add Services

Services are configured declaratively in `backend/services.yaml` — no backend code changes required.

### REST API Example

```yaml
services:
  - id: "my-search"
    type: "rest"
    name: "My Search API"
    description: "Search products from my backend"
    endpoint: "https://api.example.com/search"
    method: "POST"
    headers:
      Authorization: "Bearer ${MY_API_KEY}"
    parameters_schema:
      type: "object"
      properties:
        query:
          type: "string"
          description: "Search keyword"
      required: ["query"]
    ui_hint:
      component: "ProductList"
      formatter: "format_products"
```

### Configuration Fields

| Field | Description |
|-------|-------------|
| `id` | Unique service identifier |
| `description` | The AI reads this to decide when to invoke the service — be specific |
| `parameters_schema` | JSON Schema format — the AI extracts parameters from user input based on this |
| `requires_env` | Optional — service only enabled when all listed env vars exist |
| `payload_defaults` | Optional — default fields included in every request |
| `timeout` | Optional — request timeout in seconds |

See `services.example.yaml` for more examples.

---

## 📁 Project Structure

```
GenUI-LoomAgent/
├── frontend/                       # Next.js frontend
│   └── src/
│       ├── app/chat/               # Chat page
│       ├── components/
│       │   ├── custom-chat/        # Component registry & renderer
│       │   ├── charts/             # Chart components (Recharts)
│       │   └── primitives/         # GenUI components (DataList, TripCard, etc.)
│       ├── hooks/                  # useCustomChat and other hooks
│       ├── contexts/               # Auth, language contexts
│       ├── i18n/                   # Internationalization (zh/en)
│       ├── lib/                    # API client, utilities
│       └── types/                  # Shared TypeScript types
│
├── backend/                        # FastAPI + LangGraph backend
│   └── app/
│       ├── agent/
│       │   ├── nodes/              # LangGraph nodes (initializer → planner → executor → evaluator → synthesizer)
│       │   ├── services/           # Service registry, REST adapter
│       │   ├── memory/             # User memory extraction & storage
│       │   ├── emotional/          # Emotional context builder
│       │   └── prompts/            # LLM prompt templates
│       ├── auth/                   # JWT authentication
│       ├── crud/                   # MongoDB operations
│       └── models/                 # Data models
│
├── .github/                        # CI/CD, issue templates, assets
├── docker-compose.yml              # One-command full-stack startup
├── CONTRIBUTING.md
├── CHANGELOG.md
└── LICENSE                         # Apache 2.0
```

---

## 📜 Available Scripts

```bash
# Frontend (from frontend/)
npm run dev              # Dev server
npm run build            # Production build
npm run start            # Production server
npm run lint             # ESLint
npm run typecheck        # TypeScript type check
npm test                 # Vitest
npm run analyze          # Bundle size analysis

# Backend (from backend/)
python run.py            # Start server
```

---

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:

- Adding new GenUI components
- Adding new REST API services
- Improving the Agent workflow

---

## 📄 License

[Apache 2.0](LICENSE)
