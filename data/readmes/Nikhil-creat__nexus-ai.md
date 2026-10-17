# NEXUS-AI — Agentic Routing Intelligence Platform

NEXUS-AI extends the original NEXUS 3D routing lab into a full backend
platform that layers **agentic AI**, **RAG**, and a **CNN-based topology
classifier** on top of the classical graph algorithms, all containerized
with **Docker**.

```
┌─────────────────────────────────────────────────────────────────────┐
│                          nexus-net (docker network)                  │
│                                                                       │
│   ┌───────────────┐        ┌───────────────────────────────────┐    │
│   │   frontend      │◄────►│              backend                │    │
│   │  (nginx, static │ HTTP  │            (FastAPI)                │    │
│   │   3D visualizer)│       │                                     │    │
│   └───────────────┘        │  ┌───────────┐  ┌────────────────┐   │    │
│                             │  │  graph.py  │  │   agent.py     │   │    │
│                             │  │ Dijkstra/  │  │ tool-calling   │   │    │
│                             │  │ BFS / A*   │  │ orchestrator   │   │    │
│                             │  └─────┬─────┘  └───┬───────┬────┘   │    │
│                             │        │            │       │        │    │
│                             │  ┌─────▼─────┐ ┌────▼───┐ ┌─▼──────┐ │    │
│                             │  │  rag.py    │ │cnn.py  │ │Anthropic│ │   │
│                             │  │ TF-IDF     │ │topology│ │ API     │ │   │
│                             │  │ retrieval  │ │classfr │ │(optional│ │   │
│                             │  └────────────┘ └────────┘ └────────┘ │    │
│                             └───────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────┘
```
## Designed and Developed by 
# **NIKHIL CHARY SRIRAMOJU**
BTech CSE (Final Year)

- GitHub: [Nikhil-creat](https://github.com/Nikhil-creat)
- LinkedIn: [nikhil-chary-sriramoju](https://in.linkedin.com/in/nikhil-chary-sriramoju-95041b38a)
- Email: sriramojunikhil66@gmail.com
- Instagram: [@nikhil__sriramoju](https://www.instagram.com/nikhil__sriramoju)
- Facebook: [Profile](https://www.facebook.com/profile.php?id=100079201124141)


## What each layer actually does

| Layer | File | Real behavior |
|---|---|---|
| **Graph engine** | `backend/app/graph.py` | Generates the 49-node synthetic mesh (ported 1:1 from the frontend), runs Dijkstra, BFS, and A* with real cost/hop accounting and failure-aware routing. |
| **RAG** | `backend/app/rag.py` | TF-IDF vector store built from the markdown docs in `knowledge_base/`. No external embedding API required, so it runs fully offline inside the container. Returns the top-k passages relevant to whatever the agent needs to explain (why Dijkstra vs A*, what "congested" means, etc). |
| **CNN** | `backend/app/cnn.py` | A small PyTorch CNN (`TopologyNet`) trained on synthetically generated "topology heatmaps" (grid encodings of node load / edge saturation) to classify a network snapshot into `healthy`, `congested`, `partitioned`, or `failure_risk`. Includes the synthetic dataset generator and training loop (`train.py`) plus inference used at request time. |
| **Agent** | `backend/app/agent.py` | A tool-calling loop (`AgentSession`) that decides, per user question, which of `route`, `classify_topology`, `retrieve_docs` to invoke, in what order, then composes a final answer. Uses the Anthropic API for the reasoning/composition step if `ANTHROPIC_API_KEY` is set; otherwise falls back to a deterministic rule-based composer so the whole system runs with zero external API calls. |
| **API** | `backend/app/main.py` | FastAPI service exposing `/graph`, `/route`, `/classify`, `/agent/ask`, `/health`. |
| **Docker** | `docker-compose.yml`, `backend/Dockerfile` | Two services: `backend` (Python 3.11-slim + CPU torch) and `frontend` (nginx serving the existing `nexus.html` visualizer), joined on a private bridge network. |

## Why this combination

- **RAG** gives the agent grounded, citable explanations instead of
  free-associating about routing theory — every explanation the agent
  gives is backed by a retrieved passage from `knowledge_base/`.
- **CNN** adds a second, independent signal (visual/statistical
  topology health) that a pure graph-search algorithm can't produce —
  Dijkstra tells you the cheapest path *exists*, the CNN tells you
  whether the network *as a whole* looks strained.
- **Agentic orchestration** is what ties them together: the agent
  decides *when* it needs a route, *when* it needs a topology
  classification, and *when* it needs to look something up, rather
  than a hardcoded pipeline always running all three.
- **Docker** makes the three independently-versioned pieces (graph
  engine, ML models, static frontend) deployable as one unit without
  dependency collisions (torch vs the frontend's node-free static
  serving).

## Running it

```bash
docker compose up --build
```

- Frontend: http://localhost:8080
- Backend API: http://localhost:8000/docs (FastAPI's auto Swagger UI)

Set `ANTHROPIC_API_KEY` in a `.env` file at the project root to let the
agent use Claude for answer composition; without it, the agent still
fully functions using its rule-based composer.

## Training the CNN from scratch

The container ships with a small pre-training script since no real
network telemetry dataset is bundled:

```bash
docker compose exec backend python -m app.cnn train
```

This generates 4,000 synthetic topology snapshots across the four
classes, trains `TopologyNet` for 8 epochs, and writes weights to
`app/models/topology_net.pt`. The inference path in `agent.py` loads
these weights at startup if present, and otherwise falls back to a
heuristic classifier so `/classify` never hard-fails.

## Performance & reliability features

| Feature | File | What it does |
|---|---|---|
| **Redis-backed response caching** | `backend/app/cache.py` | `/route` and `/classify` results are cached by a hash of their inputs (algo, src, dst, failed-node set / graph state). Falls back to an in-process store automatically if Redis isn't reachable, so the service never hard-fails on a cache miss-of-infrastructure. |
| **Rate limiting** | `backend/app/main.py` (slowapi) | Per-IP limits on every mutating/expensive endpoint (`/agent/ask` 15/min, `/route` 60/min, `/graph/generate` 10/min) to protect the CNN/agent paths from being overwhelmed. |
| **Retry with exponential backoff** | `backend/app/agent.py` (tenacity) | Anthropic API calls retry up to 3 times with exponential backoff before being treated as a real failure — absorbs transient rate limits/timeouts. |
| **Circuit breaker** | `backend/app/agent.py` | After 3 consecutive LLM failures, the agent stops calling Anthropic for 30s and transparently serves the rule-based planner instead, then automatically half-opens and retries — prevents a struggling upstream API from slowing down every request. |
| **Structured request logging** | `backend/app/main.py` (loguru) | Every request gets a short request ID, logged with method/path/status/latency; unhandled exceptions are caught centrally and still return a valid JSON error with that ID for tracing. |
| **Liveness & readiness probes** | `GET /health`, `GET /ready` | `/health` reports the process is alive; `/ready` additionally checks the graph is loaded, which cache backend is active, and whether trained CNN weights are present — the shape expected by container orchestrators (Kubernetes, ECS, Fly.io). |
| **Resource limits** | `docker-compose.yml` | Backend container is capped at 1.5 CPU / 1GB RAM so a runaway request can't starve the host. |
| **Automated tests + CI** | `backend/tests/test_graph.py`, `.github/workflows/ci.yml` | Unit tests assert full graph connectivity, that Dijkstra's cost is never worse than BFS's, that A* matches Dijkstra's optimal cost while exploring no more nodes, and that failed nodes are actually routed around. CI runs these plus a Docker build + container health smoke test on every push/PR. |
| **Model versioning hook** | `GET /model/info` | Reports which CNN classes are loaded and whether trained weights vs. the heuristic fallback are active, so a deployment can be verified without guessing. |

## API quick reference

```
POST /graph/generate                → new random 49-node topology
POST /route          {algo, src, dst, failed[]}   → path/cost/steps (+ cache_hit flag)
POST /classify                                     → CNN topology verdict (+ cache_hit flag)
POST /agent/ask       {question}                   → agent's full answer + tool trace
GET  /health                                       → liveness
GET  /ready                                        → readiness (graph/cache/model checks)
GET  /model/info                                   → CNN class list + weights/cache status
```

---

## Deploying it: GitHub + GitHub Pages

GitHub Pages only serves **static files** — it cannot run the FastAPI
backend, the CNN, or Redis. So the deployment splits in two:

- **Frontend (`frontend/nexus.html` + `config.js`)** → GitHub Pages (free, static).
- **Backend (`backend/`, `docker-compose.yml`)** → any container host that
  runs Docker (Render, Railway, Fly.io, a VM, etc). This part is what
  actually executes the routing engine, CNN, RAG, and agent.

### 1. Push the project to GitHub

From the unzipped `nexus-ai/` folder:

```bash
cd nexus-ai
git init
git add .
git commit -m "Initial commit: NEXUS-AI routing lab with agentic RAG + CNN backend"
git branch -M main
git remote add origin https://github.com/<your-username>/nexus-ai.git
git push -u origin main
```

(Create the empty `nexus-ai` repository on GitHub first, via the "New
repository" button — don't initialize it with a README there, since
you already have one.)

### 2. Enable GitHub Pages via the included workflow

The repo already contains `.github/workflows/pages.yml`, which
publishes `frontend/nexus.html` and `frontend/config.js` to Pages
automatically on every push to `main`.

1. On GitHub, go to **Settings → Pages**.
2. Under **Build and deployment → Source**, choose **GitHub Actions**
   (not "Deploy from a branch").
3. Push to `main` (or re-run the "Deploy Frontend to GitHub Pages"
   workflow from the **Actions** tab manually).
4. After it finishes, your site is live at:
   `https://<your-username>.github.io/nexus-ai/`

### 3. Deploy the backend somewhere that runs Docker

Pick one (all have free/low-cost tiers as of writing — check current
pricing yourself):

- **Render**: New → Web Service → point at your GitHub repo → set
  **Root Directory** to `backend`, it auto-detects the `Dockerfile`.
  Add `ANTHROPIC_API_KEY` as an environment variable if you want the
  LLM-driven agent; add a Render Redis instance and set `REDIS_URL` to
  enable caching (optional — it degrades gracefully without one).
- **Railway**: New Project → Deploy from GitHub repo → set the service
  root to `backend` → Railway builds the Dockerfile automatically. Add
  a Redis plugin from their marketplace and it injects `REDIS_URL` for
  you.
- **Fly.io**: `fly launch` from inside `backend/`, then `fly deploy`.
  Add Upstash Redis via `fly redis create` if you want caching.

Whichever you choose, note the public URL it gives you (e.g.
`https://nexus-backend.onrender.com`).

### 4. Point the deployed frontend at your backend

Edit `frontend/config.js`:

```js
window.NEXUS_BACKEND_URL = "https://nexus-backend.onrender.com";
```

Commit and push — the Pages workflow redeploys automatically since it
triggers on changes under `frontend/`. The agent panel on your GitHub
Pages site will now call your live backend.

### 5. (Optional) Custom domain for Pages

**Settings → Pages → Custom domain**, enter your domain, and add the
CNAME record your DNS provider requires. GitHub issues an HTTPS
certificate for it automatically after verification.

### Notes

- CORS is already open (`allow_origins=["*"]`) on the backend so the
  Pages-hosted frontend can call it cross-origin without extra setup.
  Tighten this to your Pages URL specifically before treating this as
  production-hardened.
- The 3D visualizer itself (topology, Dijkstra/BFS/A* animation) works
  entirely client-side and needs no backend — only the "04 / AGENT"
  panel (RAG + CNN + agentic reasoning) requires the backend to be
  reachable.

---
