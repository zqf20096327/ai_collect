<div align="center">

# 🔬 Research Co-Scientist

**Ask a research question. Eight AI agents find the papers, read them, argue about them,
and hand you an answer where every claim is traceable to a real arXiv passage.**

![Python](https://img.shields.io/badge/python-3.14-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-gateway-009688?logo=fastapi&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-16-000000?logo=nextdotjs&logoColor=white)
![Agno](https://img.shields.io/badge/agents-Agno-7C3AED)
![Ollama](https://img.shields.io/badge/LLM-Ollama%20(local)-white?logo=ollama&logoColor=black)
![ChromaDB](https://img.shields.io/badge/vectors-ChromaDB-FF6F61)
![Playwright](https://img.shields.io/badge/e2e-Playwright-2EAD33?logo=playwright&logoColor=white)

<img src="docs/system-design-animated.svg" alt="Animated system design: requirements, high-level architecture, critic-based multi-agent workflow with bounded revision loop, platform and data layer, external services, data model, design patterns, end-to-end sequence and evaluation metrics." width="100%"/>

</div>

---

## Why this exists

General-purpose chatbots answer research questions fluently and cite papers that don't exist.
Research Co-Scientist is built the other way round:

- **Evidence first.** Answers are synthesised only from passages actually retrieved from arXiv,
  including the **full text** of the most relevant papers, not just abstracts.
- **A critic in the loop.** A separate agent attacks the hypothesis. If key claims are unsupported,
  the system goes back for more evidence, at most once, and that cap is enforced in code.
- **Citations are verified, not trusted.** A deterministic verifier strips any evidence id the
  model invented and rebuilds the citation list from real metadata. Fabricated citations cannot ship.
- **Both sides of the evidence.** Every passage is labelled as *supporting* or *contradicting*
  the hypothesis, and the balance is shown.
- **Private by default.** All models run locally through Ollama. Your questions never leave your
  machine; only search keywords go to arXiv or OpenAlex.

## Screenshots

| Live: agents working, activity streaming | Result: verified answer, evidence graph, stance balance |
|---|---|
| ![Live pipeline and activity log](docs/ui-live.png) | ![Recommendation with evidence graph](docs/ui-result.png) |

## How it works

<img src="docs/architecture-animated.svg" alt="Runtime flow: the Next.js UI calls the FastAPI gateway, which queues work for a worker pool running eight agents over arXiv, ChromaDB and local Ollama models; events stream back to the browser over SSE." width="100%"/>

```
question ─► Planner ─► arXiv ─► Ranker ─► Reader ─► Synthesis ─► Critic ─┬─► Final ─► Verifier ─► answer
                         ▲                                                 │
                         └──────── needs more evidence (≤ 1 revision) ─────┘
```

| Agent | What it does | Implemented as |
|---|---|---|
| 🧭 **Planner** | Turns the question into 2–4 keyword searches | Agno agent → `SearchPlan` schema |
| 📚 **arXiv** | Fetches candidate papers, cached for 24 h, rate-limited to the arXiv ToS | Code: arXiv API → OpenAlex fallback → stale cache |
| 🧲 **Ranker** | Splits abstracts into passages, embeds them, keeps the top-k (max 2 per paper) | Code: `nomic-embed-text` + ChromaDB |
| 📖 **Reader** | Reads the PDFs of the top 3 papers within a 20 s budget and adds their best passages | Code: `pypdf` + batched embeddings |
| 💡 **Synthesis** | Proposes one testable hypothesis and tags supporting and contradicting evidence | Agno agent → `Hypothesis` schema |
| 🔍 **Critic** | Flags unsupported claims, contradictions, methodology issues and missing evidence | Agno agent → `Critique` schema |
| 📝 **Final** | Writes the recommendation, keeping evidence-backed points apart from inference | Agno agent → `Recommendation` schema |
| 🛡️ **Verifier** | Drops unknown evidence ids and requires ≥ 2 distinct papers | Code: `workflow.verify()` |

**Design rule: the LLM decides content, code decides control flow.** The loop, the revision cap,
the rate limits, the time budgets and the citation gate are plain Python. That keeps the
system bounded, testable and auditable even on a 4B-parameter local model.

## Features

- ⚡ **Live activity stream.** Server-Sent Events push every agent action to the browser within
  about 200 ms, with automatic fallback to polling.
- 🕸️ **Interactive evidence graph.** Hypothesis → claims → passages → papers, with flowing
  edges. Hover a node to trace its links.
- 🔎 **Evidence hover cards.** Hover any `E3` chip to see the passage, section
  (abstract or full text), match score and stance.
- ⚖️ **Support vs. contradiction balance** for every hypothesis.
- 🧯 **Resilient retrieval.** The arXiv circuit breaker, OpenAlex fallback, stale-cache fallback,
  per-request timeouts and a time-budgeted PDF reader mean one slow source never blows the
  latency budget.
- 🧪 **Deterministic fake mode** (`CS_FAKE_LLM=1`) for tests and demos with no GPU or network.

## Quick start

### Prerequisites

| Tool | Version | Notes |
|---|---|---|
| [uv](https://docs.astral.sh/uv/) | ≥ 0.13 | Python 3.14 is installed automatically |
| [Node.js](https://nodejs.org/) | ≥ 20 | for the Next.js UI |
| [Ollama](https://ollama.com/) | latest | runs the models locally (GPU recommended, 6 GB is enough) |

```bash
ollama pull nomic-embed-text
ollama pull <chat-model>        # any instruction-tuned model, e.g. a 4B Qwen
```

Then set `CS_LLM_MODEL=<chat-model>`. The default, `qwen3.5-4b-16k`, is a local alias of a Qwen 3.5 4B
model with a 16k context window. Small models work because every agent returns a strict schema.

### Run

```bash
# 1. backend  →  http://localhost:8000  (OpenAPI docs at /docs)
uv sync
uv run co-scientist serve

# 2. frontend →  http://localhost:3000
cd web
npm install
npm run dev
```

Check the setup: `curl http://localhost:8000/health` → `{"ok": true, "missing_models": []}`.

**No GPU?** Start the backend with `CS_FAKE_LLM=1 uv run co-scientist serve` for a canned
end-to-end demo (PowerShell: `$env:CS_FAKE_LLM="1"; uv run co-scientist serve`).

### Command line

```bash
uv run co-scientist ask "Does retrieval-augmented generation reduce hallucination in LLMs?"
```

Progress goes to stderr; the final session JSON goes to stdout.

## Configuration

All settings are environment variables with the `CS_` prefix (or a `.env` file).

| Variable | Default | Purpose |
|---|---|---|
| `CS_LLM_MODEL` | `qwen3.5-4b-16k` | Ollama model for all four LLM agents |
| `CS_EMBED_MODEL` | `nomic-embed-text` | Ollama embedding model |
| `CS_EMBED_DIM` | `768` | Expected embedding size (checked on every call) |
| `CS_MAX_REVISIONS` | `1` | Critic-driven re-retrieval rounds |
| `CS_PAPERS_PER_QUERY` | `10` | Papers fetched per search |
| `CS_TOP_K_EVIDENCE` | `8` | Abstract passages kept per retrieval round |
| `CS_FULLTEXT_PAPERS` | `3` | Top papers whose PDF is read (`0` disables full text) |
| `CS_FULLTEXT_BUDGET_S` | `20` | Hard time ceiling for PDF reading per round |
| `CS_WORKERS` | `2` | Concurrent research sessions (GPU-bound) |
| `CS_API_KEY` | *(empty)* | When set, required as `X-API-Key` (or `?key=` for SSE) |
| `CS_CORS_ORIGINS` | `http://localhost:3000,http://127.0.0.1:3000` | Allowed browser origins |
| `CS_DATA_DIR` | `./data` | Chroma index, search cache, PDF text cache |
| `CS_FAKE_LLM` | `0` | Canned, deterministic run with no Ollama or network |

Frontend: `NEXT_PUBLIC_API_URL` (default `http://localhost:8000`) and `NEXT_PUBLIC_API_KEY`.

## API

| Method | Path | Description |
|---|---|---|
| `POST` | `/sessions` | `{"question": "..."}` (10–1000 chars) → `{session_id, status, position}` |
| `GET` | `/sessions/{id}` | Full session snapshot: status, events, evidence, hypothesis, critiques, recommendation |
| `GET` | `/sessions/{id}/stream` | **SSE**: one snapshot per change until a terminal status |
| `GET` | `/health` | Ollama reachable and required models present |

Session status: `queued → retrieving → synthesizing → critiquing → (retrieving) → finalizing →`
`done` \| `insufficient_evidence` \| `failed`.

## Performance budget

| Metric | Target | Measured |
|---|---|---|
| API responses (`POST`, `GET`, `/health`) | < 2 s | 5–40 ms |
| First agent event visible in the UI | < 2 s | < 50 ms (SSE) |
| End-to-end research session, p95 | < 3 min | 109–156 s per live run on an RTX 3060 Laptop (6 GB), 4B model, including one critic revision |

The first two rows are enforced by tests (see below). The PDF reader's 20 s budget and the
arXiv circuit breaker keep slow external sources from pushing a session past the end-to-end target.

## Testing

```bash
# API latency contract: every response and the first SSE event < 2 s
CS_FAKE_LLM=1 uv run python tests/test_latency.py

# Browser end-to-end (starts its own isolated stack on ports 8001 / 3001)
cd web && npx playwright install chromium && npx playwright test
```

The Playwright suite covers the full flow: agent activity is visible within 2 s, all eight
agents finish, the verifier strips a hallucinated citation (`E99`), the stance balance and
evidence graph render, hover cards show passages, and input validation works.

## Project structure

```
co-scientist/
├── src/co_scientist/
│   ├── agents.py        # Agno agents (planner, synthesis, critic, final) + robust JSON parsing
│   ├── workflow.py      # state machine, revision loop, citation verifier, activity events
│   ├── retrieval.py     # arXiv/OpenAlex search, circuit breaker, Chroma ranking, PDF reader
│   ├── api.py           # FastAPI gateway: auth, validation, worker pool, SSE
│   ├── schemas.py       # Pydantic contracts shared by agents, API and UI
│   ├── config.py        # CS_* settings
│   └── __init__.py      # `co-scientist serve | ask` CLI
├── web/
│   ├── app/page.tsx         # pipeline, activity log, results
│   ├── app/EvidenceGraph.tsx
│   ├── lib/api.ts           # typed client + SSE stream
│   └── e2e/flow.spec.ts     # Playwright tests
├── tests/test_latency.py
├── docs/                    # animated architecture diagram, screenshots
├── architecture.md          # system design and implementation plan
└── enterprise-architecture.md  # target state: tenancy, security, LLMOps, scale-out roadmap
```

## Documentation

- **[architecture.md](architecture.md)**: component design, data model, sequence diagrams,
  technology choices and the review of the original design.
- **[enterprise-architecture.md](enterprise-architecture.md)**: target state for organisation-wide
  rollout: multi-tenancy, SSO/RBAC, model gateway, evaluation gates, Kubernetes deployment,
  observability, ADRs and a phased migration roadmap.

## Troubleshooting

| Symptom | Cause and fix |
|---|---|
| Log shows `arXiv rate-limited, used fallback` | arXiv returned 429. The circuit breaker switches to OpenAlex for 2 minutes. Normal behaviour; nothing to do. |
| Sessions stuck in `retrieving` or very slow | Another process is using the GPU. On Windows, stopping a terminal can leave orphan `python.exe` processes holding Ollama; end them in Task Manager. |
| LLM steps take minutes each | Your model is "thinking". Use a model or tag with thinking disabled; the app already sends `think: false`. |
| `/health` lists `missing_models` | `ollama pull` the listed model, or point `CS_LLM_MODEL` / `CS_EMBED_MODEL` at one you have. |
| UI shows "Lost connection" | Backend not running on `NEXT_PUBLIC_API_URL`, or CORS: add the UI origin to `CS_CORS_ORIGINS`. |

## Limitations

- Sessions are held in memory (capped at 200), so a backend restart clears them. Phase 1 of the
  enterprise roadmap moves them to Postgres.
- Single-process rate limiter. Running multiple backend processes needs a shared limiter (e.g. Redis).
- Answers are only as good as the retrieved evidence. Treat confidence scores as guidance, not truth.

## Acknowledgements

[arXiv](https://arxiv.org) (thank you for open access to scholarly papers) ·
[OpenAlex](https://openalex.org) · [Agno](https://github.com/agno-agi/agno) ·
[Ollama](https://ollama.com) · [ChromaDB](https://www.trychroma.com) ·
[FastAPI](https://fastapi.tiangolo.com) · [Next.js](https://nextjs.org)
