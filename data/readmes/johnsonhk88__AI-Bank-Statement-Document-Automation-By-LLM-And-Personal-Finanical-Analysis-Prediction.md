# AI Bank Statement Automation with LLM & Personal Financial Analysis

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)](https://www.python.org)
[![CrewAI](https://img.shields.io/badge/CrewAI-Agents-green?style=for-the-badge)](https://github.com/crewAIInc/crewAI)
[![Deep Agents](https://img.shields.io/badge/Deep%20Agents-LangChain-blue?style=for-the-badge)](https://docs.langchain.com/oss/python/deepagents/overview)
[![LiteLLM](https://img.shields.io/badge/LiteLLM-Local%20%2B%20Cloud-orange?style=for-the-badge)](https://github.com/BerriAI/litellm)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

> Upload bank-statement PDFs, extract a **Postgres ledger**, and ask questions with a **shared pipeline**. Choose **Pipeline**, **CrewAI**, or **Deep Agents**. Local LLMs via LiteLLM (vLLM, SGLang, Strata, LM Studio, Ollama).

**Scripts:** [docs/guides/getting-started.md](docs/guides/getting-started.md) · **Manual (no scripts):** [docs/guides/manual-setup.md](docs/guides/manual-setup.md) · **Terms:** [CONTEXT.md](CONTEXT.md)

---

## Quick start

**With scripts**

```bash
./scripts/setup.sh          # infra/.env + JWT
./scripts/up.sh             # Postgres, Redis, Qdrant, RustFS, API :8000, worker
./scripts/preflight.sh      # health + login + sample upload
./scripts/dev-frontend.sh   # http://localhost:5173
```

**Manual** (same stack, no `./scripts`)

```bash
cp infra/.env.example infra/.env   # then edit JWT_SECRET, ADMIN_EMAIL, ADMIN_PASSWORD
cd infra && docker compose up -d --build
curl -s http://localhost:8000/api/health
cd ../frontend && npm install && npm run dev
```

Full commands, ports, overlays, and pitfalls: [docs/guides/manual-setup.md](docs/guides/manual-setup.md).

| Script | Purpose |
|--------|---------|
| `./scripts/setup.sh` | Write `infra/.env`, generate `JWT_SECRET` |
| `./scripts/up.sh` | Compose up (`--gpu`, `--ocr`, `--prod`) |
| `./scripts/preflight.sh` | Health, login, sample PDF |
| `./scripts/dev-frontend.sh` | Vite on `:5173` |
| `./scripts/logs.sh` | Follow `backend` + `worker` (or pass service names) |
| `./scripts/test.sh` | Backend pytest + frontend vitest |
| `./scripts/down.sh` | Stop (`--volumes` wipes data) |

On **New analysis** pick **Pipeline** (default), **CrewAI**, or **Deep Agents**. PDFs go to **RustFS**; statements and transactions go to **Postgres**.

---

## How it fits together

| Store | Holds |
|-------|--------|
| **RustFS** `:9000` (console `:9001`) | PDF bytes (`documents/{sha256}.pdf`) |
| **Postgres 16** | Upload registry, `statements`, `transactions`, analysis history |
| **Qdrant** | Redacted chunks for RAG — not the ledger |
| **Redis** | Celery queue |

Pipeline stages (shared by every harness): extract → optional OCR → redact PII → parse → verify → categorize → store → report.

---

## Key features

- **Deterministic pipeline** — PyMuPDF extract, PII redaction, heuristic parse + LLM fallback, balance check
- **Selectable agents** — Pipeline, CrewAI, Deep Agents (Hermes still disabled)
- **Object storage** — S3-compatible RustFS locally; same client for AWS/R2 later
- **SQL ledger** — dashboard totals from `transactions`, not JSONB blobs
- **Local LLM first** — vLLM, SGLang, Strata, LM Studio, Ollama via LiteLLM; live `/v1/models`
- **Optional YOLO + OCR** — `./scripts/up.sh --ocr` when PDF text is sparse
- **GPU optional** — `./scripts/up.sh --gpu` (CPU torch is the default image)
- **History dashboard** — quarterly / annual totals from Postgres
- **MCP stdio** — Claude Desktop / Cursor over the BankAI API
- **Domain skills** — edit `skills/` only, then `python scripts/sync_skills.py --apply`

---

## Ports

| Port | Service |
|------|---------|
| `5173` | Vite UI (dev) |
| `80` | Nginx UI (prod profile) |
| `8000` | FastAPI (`/api/*`) |
| `5432` | PostgreSQL |
| `6379` | Redis |
| `6333` | Qdrant |
| `9000` | MinIO S3 API |
| `9001` | MinIO console (login = `S3_ACCESS_KEY` / `S3_SECRET_KEY`) |
| `3001` | Grafana (optional monitoring stack) |

BankAI FastAPI **owns :8000**. If you run vLLM, bind it to **:8001**.

---

## Object storage

```bash
docker compose -f infra/monitoring/docker-compose.yml up -d
# Grafana http://localhost:3001  (admin/admin)  dashboard /d/bankai-local-llm
```

- [docs/guides/local-llm-and-monitoring.md](docs/guides/local-llm-and-monitoring.md)
- [docs/guides/mcp.md](docs/guides/mcp.md)

Prefer **9B+** models and **16K+** context (32K better). Prefer Markdown reports over strict JSON on small local models.

---

## Tech stack

| Component | Technology |
|-----------|------------|
| **API** | FastAPI, SQLAlchemy 2.0 (async), Alembic, Pydantic v2 |
| **Pipeline** | PyMuPDF, PII redact, heuristic + instructor parse |
| **Object store** | RustFS (S3 API) |
| **LLM** | LiteLLM (vLLM, SGLang, Strata, LM Studio, Ollama, OpenAI, …) |
| **Agents** | Pipeline adapter · CrewAI · Deep Agents |
| **Vector DB** | Qdrant |
| **Queue** | Celery + Redis |
| **Database** | PostgreSQL 16 |
| **Frontend** | React 18, TypeScript 5, Vite 5, TailwindCSS 3 |
| **GPU (optional)** | NVIDIA Container Toolkit, PyTorch cu128 |

---

## Project structure

```text
├── backend/                 # FastAPI + Celery (HTTP under /api/*)
│   ├── app/pipeline/        # Canonical extract → report stages
│   ├── app/agents/          # pipeline, crewai, deep-agents, hermes stub
│   └── alembic/
├── frontend/                # React SPA
├── infra/                   # Compose, Dockerfiles, k8s stub, monitoring
├── skills/                  # Canonical SKILL.md packages
├── scripts/                 # setup, up, down, logs, test, preflight
├── agents/                  # Experimental harness copies (not the API)
├── notebooks/               # CrewAI / YOLO experiments
├── data/samples/
├── docs/guides/             # Run books
├── docs/specs/              # Historical design snapshots
├── docs/adr/
└── CONTEXT.md
```

**Skills:** edit `skills/` only, then `python scripts/sync_skills.py --apply`.

---

## GPU (optional)

Default `./scripts/up.sh` is **CPU**. For CUDA torch and NVIDIA devices:

```bash
./scripts/up.sh --gpu
cd infra && docker compose exec backend python -c \
  "import torch; print(torch.cuda.is_available(), torch.cuda.get_device_name(0) if torch.cuda.is_available() else '')"
```

Needs [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html) on the host. Verify with:

```bash
docker run --rm --gpus all nvidia/cuda:12.2.1-base-ubuntu22.04 nvidia-smi
```

---

## HTTP smoke tests and pytest

After `./scripts/up.sh`, use [docs/guides/full-stack-app-guide.md](docs/guides/full-stack-app-guide.md) for curl walkthroughs and test layout.

```bash
./scripts/test.sh
```

---

## Experiments (notebooks / `agents/`)

Production analysis is the FastAPI app. These trees are **offline experiments**:

| Harness | Path | How to run |
|---------|------|------------|
| CrewAI notebook | `notebooks/ai_agent_skills_dev.ipynb` | project venv + Jupyter |
| Deep Agents CLI | `agents/deep-agents/` | `run_e2e.py --mode pipeline` (no LLM) |
| Hermes | `agents/hermes/` | Hermes CLI + Docker sandbox |

Guide: [docs/guides/multi-harness-agents-guide.md](docs/guides/multi-harness-agents-guide.md)

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
jupyter notebook notebooks/ai_agent_skills_dev.ipynb
```

---

## Developer notes

- Containers set `PYTHONPATH=/app/backend:/app/skills`.
- Admin login uses **plain** `ADMIN_PASSWORD` in `infra/.env` (hashed in the container). Do not paste bcrypt into Compose.
- Image pins `bcrypt<4.1` (passlib 1.7.4).
- Qdrant healthcheck reads `/proc/net/tcp` (no curl in that image).
- Historical v1 specs: [docs/specs/](docs/specs/) — current ops are getting-started.
- Decisions: [docs/adr/0001-minio-s3-for-statement-documents.md](docs/adr/0001-minio-s3-for-statement-documents.md), [docs/adr/0002-postgres-ledger.md](docs/adr/0002-postgres-ledger.md), [docs/adr/0003-rustfs-for-local-object-storage.md](docs/adr/0003-rustfs-for-local-object-storage.md)

---

## Roadmap

- Wire Hermes into the live API
- Kubernetes as a separate base project
- Stronger PII (names/addresses)
- Multi-document workspaces / forecasting on the SQL ledger

---

## License

Apache License 2.0
