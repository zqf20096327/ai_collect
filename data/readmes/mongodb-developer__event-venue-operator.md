# Event Venue Operator

Agentic event-venue operator demo built on MongoDB Atlas. Showcases three-layer memory (long-term, short-term, shared), hybrid retrieval with Voyage AI multimodal embeddings, optional Langfuse traces, and persona-segmented agent decisions during a rain delay scenario at a Premier Tennis Tournament.

**Live demo:** [event-venue-operator.vercel.app](https://event-venue-operator.vercel.app/)

## What this is

A demo seed for practitioners exploring agentic patterns on MongoDB. Shows how to model agent memory, retrieve patterns from past events, and segment actions by persona type — all backed by a single Atlas cluster.

The narrative: an AI operator agent monitors a tennis tournament on Day 6. Rain is incoming. The agent reads live venue state, retrieves patterns from past events via vector search, plans persona-specific actions (guide a first-time visitor to an open court; reserve covered dining for a premier visitor), and writes the outcome back to long-term memory.

The visible UI is intentionally deterministic for demo reliability. The backend proof points are real: Atlas setup, seeded memory, Voyage embeddings, hybrid search, Atlas Vector Search, visual-document RAG, optional Langfuse observability, and a runnable LangGraph agent path.

## What this isn't

A production agentic platform. Patterns are demonstrated; production hardening (CI, production observability, error recovery, live operator approvals) is intentionally outside this tutorial scope.

## Three ways to interact

### 1. Stage demo (deterministic UI)

```bash
uv run python -m event_venue_operator.server
```

Open http://127.0.0.1:8000. Walk through the three-tab narrative, then use the fourth tab for live backend validation:

- **Tab 1 — Venue Ops** (2:15pm): Live dashboard with courts, hospitality, KPIs. Weather indicator shows rain 90m out.
- **Tab 2 — Scenario (rain)**: Click-by-click agent walkthrough. Five steps: READ short-term, READ long-term (vector search), PLAN, ACT (agent items appear on visitor view), WRITE (memory flash). Toggle between Mikiko (first-timer, blue) and Nina (premier, purple).
- **Tab 3 — Final Outcomes** (10:00pm): End-of-day summary. Revenue, retention, reputation lift. Memory patterns written for future events.
- **Tab 4 — Live Backend**: Runs live retrieval calls against Atlas and emits optional Langfuse traces when configured.

UI values are hardcoded for predictable stage presentation. Use the API endpoints and scripts below to exercise the live backend.

### 2. Live agent (real LangGraph execution)

```bash
uv run python scripts/run_poc.py
```

Runs the full LangGraph chain end-to-end:

1. **perceive** — reads from Atlas (guest memories + fleet patterns via vector search)
2. **plan** — calls Claude Sonnet 4.6 to generate an itinerary
3. **hitl_gate** — preserves the approval insertion point and auto-approves in V1
4. **act** — executes tools (update_itinerary, book_reservation)
5. **reflect** — writes new inferences back to memory store

Agent decisions are non-deterministic and depend on retrieved memories, but the seeded scenario now follows the same Mikiko/Nina tennis rain-delay story as the stage UI.

When Langfuse keys are configured, this script emits a run-level `langgraph.run_agent` observation so the live agent path can be validated outside the UI.

### 3. API exploration

The FastAPI server exposes endpoints for direct interaction with the memory store:

- `GET /api/search?q=...&namespace=guests` — Atlas Vector Search over memories
- `GET /api/hybrid-search?q=...&namespace=guests` — vector + lexical hybrid retrieval over memories
- `POST /api/unified-search` — cross-namespace search with profile-fact join
- `POST /api/vision-rag/query` — vector search + Claude Vision reads operational documents
- `GET /api/debug/embed?text=...` — inspect Voyage embeddings directly
- `GET /api/observability/status` — confirm whether Langfuse tracing is configured

## Setup

### Prerequisites

- Python 3.12+
- MongoDB Atlas cluster with Atlas Vector Search enabled
- Anthropic API key
- Voyage AI API key

### Install

```bash
git clone https://github.com/mikikob-mongodb/event-venue-operator.git
cd event-venue-operator
uv sync
```

### Configure

```bash
cp .env.example .env
# Edit .env: MONGODB_URI, ANTHROPIC_API_KEY, VOYAGE_API_KEY
# Optional: LANGFUSE_PUBLIC_KEY, LANGFUSE_SECRET_KEY, LANGFUSE_HOST
```

### Initialize Atlas

```bash
uv run python scripts/setup_atlas.py
# Wait ~60s for vector index to build
```

### Seed data

```bash
uv run python scripts/seed_data.py
uv run python scripts/seed_visual_docs.py
```

### Run

```bash
# Stage demo
uv run python -m event_venue_operator.server

# Live agent
uv run python scripts/run_poc.py
```

### Verify

With the server running in one terminal, run:

```bash
uv run python scripts/smoke_test.py
```

The smoke test checks MongoDB health, Atlas Vector Search, hybrid search, visual-document indexing, Vision RAG, Langfuse wiring, and collection stats.

## Architecture

- **Frontend**: Vanilla HTML/JS at `static/index.html` (three-tab story flow plus Live Backend validation tab)
- **Backend**: FastAPI at `src/event_venue_operator/server.py`
- **Agent**: LangGraph chain at `src/event_venue_operator/graph.py` (perceive -> plan -> hitl_gate -> act -> reflect)
- **Data**: MongoDB Atlas (memory_store, guests, visits, venue_status, weather_events, venues, reservations, agent_actions)
- **Embeddings**: Voyage AI `voyage-multimodal-3.5` (1024d, cross-modal text+image)
- **LLM**: Claude Sonnet 4.6 (plan node), Claude Sonnet 4.5 (vision RAG)
- **Observability**: optional Langfuse tracing for retrieval endpoints and the live LangGraph run when `LANGFUSE_PUBLIC_KEY` and `LANGFUSE_SECRET_KEY` are configured

## Memory layers

| Layer | Storage | Retrieved via |
|---|---|---|
| Long-term | `memory_store` collection with Voyage embeddings | Atlas Vector Search and hybrid retrieval |
| Short-term | `venue_status`, `weather_events` collections | Direct document lookup |
| Shared | `agent_actions` collection | Agent and subagent coordination log |

## Personas

- **Mikiko First-Timer** (blue, `#60a5fa`) — first visit, match-focused, exploring the grounds
- **Nina Premier** (purple, `#a78bfa`) — premier access, hospitality history, covered seating preference

## Repository layout

```
event-venue-operator/
├── src/event_venue_operator/   # Package: server, agent, db, config, seed
├── scripts/                    # Setup, seeding, POC runner, visual doc generation
├── static/                     # Stage demo HTML + visual documents
└── docs/                       # Architecture notes and feature inventory
```

## Scope boundaries

- The stage UI is guided/static by design; API endpoints and scripts exercise the live backend proof points.
- Change stream listeners exist as an extension path, but the V1 tutorial does not wire them into the UI.
- `hitl_gate` is included in the graph shape as a placeholder for production approvals, but V1 auto-approves actions.
- CI, eval harnesses, production error handling, and deployment hardening are out of scope for this tutorial repo.

## Further reading

- [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) — design decisions
- [docs/LANGGRAPH.md](docs/LANGGRAPH.md) — live agent walkthrough
- [docs/OBSERVABILITY.md](docs/OBSERVABILITY.md) — optional Langfuse setup and validation
- [docs/VERCEL.md](docs/VERCEL.md) — hosted preview deployment plan
- [docs/features.md](docs/features.md) — current feature inventory

## License

MIT License. See LICENSE file for details.
