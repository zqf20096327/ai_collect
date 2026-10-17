<div align="center">

# IRIS-X

**Intelligent Robotics & Infrastructure Sentinel**

Autonomous cyber-physical command console: 3D digital twin · agentic AI swarm · RAG · CNN vision · personal AI assistant · zero-trust by design

**Designed & developed by [NIKHIL CHARY SRIRAMOJU](https://github.com/Nikhil-creat)**
[GitHub](https://github.com/Nikhil-creat) · [LinkedIn](https://in.linkedin.com/in/nikhil-chary-sriramoju-95041b38a)

`Three.js` `Agentic AI` `RAG` `CNN / PyTorch` `Groq` `Gemini` `FastAPI` `Redis Streams` `Docker` `Prometheus` `Grafana` `Kubernetes` `Istio` `PWA`

**Live demo:** `https://nikhil-creat.github.io/iris-x/`

</div>

---

## What it does

| Capability | Details |
|---|---|
| **3D digital twin** | Robotic arm, three server racks and an uplink gateway rendered in WebGL with bloom, floating live labels, a sweeping floor pulse, touch orbit and pinch zoom. Joints, heat and stress follow telemetry in real time. |
| **Agentic swarm** | Robotics, SecOps and Forecaster agents work in parallel, grounded by RAG and the CNN. An Orchestrator decides and applies mitigation; the twin shows the recovery. Always completes, even with no AI key. |
| **Personal assistant** | Tool-using agent on the free Groq tier (Gemini fallback). Keeps notes and tasks, does maths, reads facility status, runs incidents. Voice in and out. Works offline with slash commands. |
| **RAG** | BM25 retrieval over operations runbooks grounds every agent, the copilot and the assistant. |
| **CNN vision** | Classifies a 12×12 thermal map: nominal, hotspot, distributed overheating, sensor fault. Browser demo uses fixed kernels; the backend trains a PyTorch CNN. |
| **Insights** | Live security posture score with explained factors, predictive time-to-limit per rack, 30-second telemetry charts. |
| **Incident reports** | One tap exports a Markdown post-incident report: timeline, decision, peaks, AI usage, runbooks. |
| **Dual AI layer** | Groq (Llama 3.3 70B) and Gemini Flash. Automatic failover on 429 and errors, cooldowns, optional dual-model consensus. |
| **Command palette** | `Ctrl/Cmd + K` for every action. |
| **Installable PWA** | Works offline after the first visit; add to your phone's home screen. |
| **Backend (optional)** | FastAPI + WebSocket, Redis Streams telemetry, agentic state graph, PyTorch CNN, Prometheus metrics, Grafana dashboard. |
| **Infra** | Docker Compose, Kubernetes manifests (non-root, read-only, network policy), Istio strict mTLS, SecOps audit, CI. |

## Quick start

### A. GitHub Pages, no backend

Everything runs in the browser. See **Deploy** below, then open the site, tap **AI settings** and paste a free Groq key.

### B. Full stack

```bash
docker compose up --build
```

| Service | URL |
|---|---|
| Console | http://localhost:8080 |
| Agent engine API / metrics | http://localhost:8000 (`/health`, `/metrics`) |
| Prometheus | http://localhost:9090 |
| Grafana (dashboard "IRIS-X Operations") | http://localhost:3000 (user `admin`, password from `GRAFANA_PASSWORD`, see `.env.example`) |

In the console: **AI settings → Live backend → `http://localhost:8000` → Connect**. Telemetry then flows generator → Redis → agent engine → WebSocket, and the swarm runs server-side with keys held in memory for that session only.

The first build downloads CPU PyTorch (~200 MB). For a small image set `INSTALL_TORCH: "0"` in `docker-compose.yml`; a heuristic classifier is used instead.

Static preview without Docker: `npm run serve` (or `cd docs && python3 -m http.server 8080`). Opening `index.html` by double click will not load runbooks because browsers block `fetch` on `file://`.

## Free API keys

* Groq: https://console.groq.com/keys
* Gemini: https://aistudio.google.com/apikey

Keys stay in your browser (toggle "Remember keys" off for session-only). Nothing in this repo contains a key; `npm run audit` verifies that.

## Deploy to GitHub Pages

1. Create an empty **public** repo named `iris-x` on github.com (no README or .gitignore).
2. In the unzipped folder:

```bash
git init
git add .
git commit -m "IRIS-X v2.0"
git branch -M main
git remote add origin https://github.com/Nikhil-creat/iris-x.git
git push -u origin main
```

   Use a personal access token as the password (GitHub → Settings → Developer settings → Tokens, scope `repo`), or run `gh auth login` first.
3. Repo **Settings → Pages → Build and deployment → Source: Deploy from a branch → `main` / `/docs` → Save**.
4. After 1–2 minutes: `https://nikhil-creat.github.io/iris-x/`.

No git? Repo → **Add file → Upload files**, drag in the *contents* of the unzipped folder (keep `docs/`), commit.
To update later: `git add . && git commit -m "update" && git push`.

## Using it

* **Swarm**: press *Overheat / Breach / Overload* (or leave auto-incidents on) and watch the agents work. *Export incident report* downloads Markdown.
* **Assistant**: try "Summarize the facility status", "Add a task: review runbooks tomorrow", "What is 15% of 2,480?", "Start a breach incident". Without a key: `/note`, `/task`, `/tasks`, `/done <id>`, `/time`, `/status`.
* **Insights**: posture gauge, per-rack ETA to 90 °C and live charts.
* **Vision**: simulate a cooling failure or sensor fault and watch the CNN reclassify.
* **Voice**: Mic button and "Read replies aloud" appear in browsers that support the Web Speech API. In Chrome, speech recognition streams audio to the browser vendor's service.
* Tap **IRIS-X** in the header for the About card.

## Testing

```bash
npm test                                   # 15 Node tests: RAG, CNN, telemetry, swarm, assistant, insights, reports
cd services/agent-engine && python -m unittest discover -s tests -v
npm run audit                              # secret scan + manifest checks
```

GitHub Actions (`.github/workflows/ci.yml`) runs all of these plus Docker builds on every push.

## Limits to know

* GitHub Pages is static, so the FastAPI backend cannot run there. The Pages site is the full browser simulator; host the backend yourself and connect with the Live backend field.
* From an https site, Chrome and Firefox allow `ws://localhost`; Safari blocks it. Use `http://localhost:8080` for the full stack.
* The in-browser CNN uses fixed kernels and hand-set weights. The trained model is `services/agent-engine/app/cnn.py`.
* Enclave attestation is simulated; Istio and confidential-container settings need a real cluster.
* Model ids change over time. If a model errors, type another id in the model field.

## Project layout

```
docs/                    GitHub Pages site: index.html, css/, js/, data/knowledge.json, PWA assets
services/agent-engine/   FastAPI, AgenticLoop.py, RAG, PyTorch CNN, LLM router, tests
services/telemetry-generator/
infra/                   k8s, istio, prometheus, grafana, secops audit
frontend/                Next.js reference components (aiClient.ts, DigitalTwinCanvas.tsx, SettingsDrawer.tsx)
tests/                   Node test suite
docker-compose.yml  ARCHITECTURE.md  SECURITY.md  LICENSE
```

## Roadmap

Persistent vector memory (Qdrant), LangGraph graph runtime, real device telemetry via MQTT, multi-site fleet view, WebGPU renderer.

---

<div align="center">

© 2026 **Nikhil Chary Sriramoju** · MIT License · Designed & developed with care.

</div>
