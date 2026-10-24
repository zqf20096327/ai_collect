# BastionMesh AI v3

**Live site (GitHub Pages):** `docs/index.html` · Consensus Lab, in-browser CRAG Copilot, architecture, API and author profile.

Autonomous multi-agent mesh: PyTorch CNN vision → LangGraph agents (with HITL) → Corrective Agentic RAG over Qdrant with MCP fallback tools → Raft-inspired weighted consensus on Redis Streams → Postgres audit ledger. Telemetry via OpenTelemetry, Prometheus and a WebSocket stream.

## Run
```bash
cp .env.example .env          # set API_TOKEN and CONSENSUS_SECRET
docker compose -f docker/docker-compose.yml up --build
```
First build downloads ResNet-50 / bge-small / MiniLM weights into the image (needs internet, ~1.5 GB). API on :8000, Prometheus on :9090.

## Layout
```
src/config.py, telemetry.py        settings, OTel tracing, Prometheus metrics, trace-context propagation
src/vision/                        ResNet-50 spatial extractor, async micro-batching worker, schemas
src/rag/                           Qdrant hybrid store (dense + BM25 sparse + RRF), cross-encoder, CRAG engine
src/mcp/                           MCP tool server (stdio) + async gateway client
src/agents/                        LangGraph state, nodes (4 agents), voters, graph, runner
src/consensus/                     models, pure tally math, Postgres ledger, Redis Streams engine
src/api/                           FastAPI app, routes, WebSocket telemetry hub
docker/                            Dockerfile (multi-stage), docker-compose.yml, prometheus.yml
data/                              sample manuals + firewall policy (indexed on first start)
tests/                             quorum math, chunking, sparse encoder
```

## How the CNN decides (no labelled data needed)
Frames pass through ResNet-50; a fixed-seed 2048→512 projection gives per-location embeddings. A streaming baseline (Welford) of *normal* embeddings is learned online: the first `VISION_BASELINE_WARMUP` (32) frames are labelled `baseline_learning`. After that, a per-cell Mahalanobis anomaly map yields the confidence score and bounding boxes. Register labelled exemplars with `POST /api/v1/vision/prototype` to get class names (nearest prototype by cosine); otherwise anomalies are `anomalous_unclassified`. Feed it only normal footage during warm-up.

## Quick test
```bash
H='X-API-Key: change-me-api-token'
# 1) warm up the baseline with 32+ normal frames
for i in $(seq 40); do curl -s -H "$H" -F file=@normal.jpg localhost:8000/api/v1/vision/ingest >/dev/null; done
# 2) send an anomalous frame with logs
curl -s -H "$H" -F file=@anomaly.jpg -F 'logs=ERROR upstream timeout on gateway-7
CRITICAL connection refused 10.0.3.4' localhost:8000/api/v1/vision/ingest
# 3) CRAG
curl -s -H "$H" -H 'content-type: application/json' -d '{"query":"Can an agent isolate a network segment automatically?"}' localhost:8000/api/v1/rag/query
# 4) live stream
websocat "ws://localhost:8000/ws/v1/telemetry?token=change-me-api-token"
```
CRITICAL proposals pause at the graph's `hitl_gate`; approve with
`POST /api/v1/consensus/proposal/{id}/hitl-approve {"approve":true,"actor":"alice"}`.

## Consensus semantics
- Per-agent HMAC-SHA256 signed votes (`scripts/derive_agent_key.py`), one vote per agent (atomic `HSETNX`), replay-safe.
- Pass = weighted `AGREE/(AGREE+DISAGREE) > 0.66` **and** ≥50% weighted participation. Weight = agent weight × vote confidence (compliance-agent weighs 1.5×).
- Non-responders go to the `bastionmesh:dlq` stream. Timeout policy is fail-safe: insufficient participation → `EXPIRED`; CRITICAL proposals never pass with missing voters.
- Set `EXTERNAL_VOTERS=compliance-agent` to have an agent vote over the HTTP API instead of in-process.
- Approved actions are appended to the `bastionmesh:actions` stream for downstream executors.

## Notes
- `web_search` MCP fallback needs `SEARXNG_URL`; without it CRAG falls back to on-disk `document_search` only.
- Without `LLM_BASE_URL` CRAG answers are extractive (top refined sentences); with it, any OpenAI-compatible server is used.
- Run tests: `pip install -r requirements.txt && pytest`.

## Highlights
- Hash-chained (SHA-256) audit ledger + `GET /api/v1/audit/verify`
- `GET /api/v1/ai/explain/{proposal_id}` — plain-English decision explanation (LLM optional)
- `docs/` static site + `.github/workflows/pages.yml` (auto-deploy on push to `main`)

## Publish the site on GitHub Pages
1. Create an empty repo `bastionmesh-ai` on GitHub.
2. `git init && git add . && git commit -m "BastionMesh AI v2" && git branch -M main`
3. `git remote add origin https://github.com/<user>/bastionmesh-ai.git && git push -u origin main`
4. Repo → Settings → Pages → Source: **GitHub Actions**. The workflow publishes `docs/` at `https://<user>.github.io/bastionmesh-ai/`.

## Dev shortcuts
`make up` · `make smoke` (end-to-end test: warms the CNN baseline, sends an anomaly, prints agent trace, explanation and audit-chain check) · `make test` · `make down`

## Termux one-shot
`bash scripts/push_to_github.sh <your-github-username>`
