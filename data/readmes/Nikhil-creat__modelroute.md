# ModelRoute: Smaller Models. Bigger Impact.
AI Project #5 by Nikhil Chary Sriramoju ([GitHub](https://github.com/Nikhil-creat) · [LinkedIn](https://in.linkedin.com/in/nikhil-chary-sriramoju-95041b38a))

A working LLM routing system. A trained classifier predicts whether a support request needs a large model; easy requests go to a small, cheap model and hard ones to a larger one. Answers are grounded with RAG, near-duplicates are cached, PII and prompt injection are guarded, weak answers escalate, and every request is logged so cost, latency and fallback rate are measured, not guessed.

## Quick start (about 2 minutes, no API keys needed)
```bash
pip install -r requirements.txt -r requirements-dev.txt
python -m modelroute.train          # trains the router, writes EVALUATION.md
python -m unittest discover -s tests -v
LLM_MODE=mock uvicorn modelroute.app:app --port 8000   # open http://localhost:8000
```
Open `http://localhost:8000` for the site wired to the live API, or `/docs` for the OpenAPI page. For real answers, copy `.env.example` to `.env`, add free Groq and Gemini keys and drop `LLM_MODE=mock`. Without keys the responses are labelled `provider: mock` (extractive answers from the knowledge base).

## How a request flows
`guard` (injection block, PII redaction) → `semantic cache` → `RAG` (TF-IDF over `kb/`) → `router` (p(small is enough) vs per-mode threshold) → `LLM` (Groq 8B or Gemini, with failover and circuit breaker) → `judge` (weak answer escalates to the large model) → `human review queue` for uncertain cases → `SQLite log`. Each response includes a `trace` of these steps.

## API
| Endpoint | Purpose |
|---|---|
| `POST /route` | `{text, mode: fast|cost|quality, visual_complexity?}` returns answer, model, provider, cost, trace |
| `GET /stats` | Real request count, cost saving vs always-large, latency, fallback and cache rates |
| `GET /review`, `POST /feedback` | Human-in-the-loop queue and ratings |
| `GET /health`, `GET /config` | Status, modes and prices |

Optional auth: set `API_KEYS=a,b` and send `x-api-key`. Rate limit: `RATE_LIMIT` per minute.

## Evaluation
`python -m modelroute.train` trains on templates and tests on unseen templates; results land in [EVALUATION.md](EVALUATION.md). `python -m modelroute.eval` pushes the held-out set through the full pipeline. Prices are assumptions, override with `PRICE_SMALL` / `PRICE_LARGE`. **The bundled dataset is synthetic.** Put your own labelled tickets in `data/tickets.jsonl` (`{"text","label"}`, 0 = small is enough, 1 = needs large) and retrain.

## Layout
| Path | Role |
|---|---|
| `modelroute/` | Core package: data, train, router, rag, cache, guard, llm, pipeline, store, app, eval, mcp_server |
| `kb/` | Support policy knowledge base used for RAG |
| `tests/` | Unit and API tests (also run in CI) |
| `docs/` | The website (GitHub Pages) and the UI served by the API |
| `vision/` | Optional PyTorch CNN screenshot classifier (`python train_cnn.py`) |
| `trainer/` | Optional LoRA fine-tune for the router (`train_lora.py data/tickets.jsonl`) |

## Status
Tested in this repo: guard, dataset, router, RAG, cache, pipeline, logging and stats (`make test`). API tests run in CI where FastAPI is installed. The vision CNN and LoRA trainer are optional modules that need PyTorch and have their own scripts. Limitations: TF-IDF retrieval, not a vector DB; the cache is in-memory; in-memory rate limiting suits a single process.

Deployment: see [DEPLOY.md](DEPLOY.md). Design notes: [ARCHITECTURE.md](ARCHITECTURE.md).
