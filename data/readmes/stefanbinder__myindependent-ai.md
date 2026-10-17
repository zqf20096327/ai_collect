# My Independent AI 🤖

A fully local, privacy-first personal AI assistant. Ask questions about your own data — emails, documents, chats — without anything leaving your machine.

**Stack:** Ollama · Qdrant · Streamlit · Python (uv monorepo)

---

## Quickstart

**Prerequisites:** [Docker](https://docs.docker.com/get-docker/) & [Docker Compose](https://docs.docker.com/compose/install/)

```bash
git clone https://github.com/your-username/myindependent-ai.git
cd myindependent-ai
docker compose up
```

Open [http://localhost:8501](http://localhost:8501) — that's it.

> **First run:** `docker compose up` automatically pulls `llama3.2` (~2 GB) and `nomic-embed-text` (~300 MB) via the `ollama-init` service. Subsequent starts are instant.

---

## What's Running

| Service   | URL                    | Purpose                |
| --------- | ---------------------- | ---------------------- |
| Dashboard | http://localhost:8501  | Streamlit chat UI      |
| Ollama    | http://localhost:11434 | Local LLM + embeddings |
| Qdrant    | http://localhost:6333  | Local vector database  |

---

## Getting Data In

The dashboard searches whatever is in your Qdrant `personal_data` collection. To populate it, run one of the importers:

```bash
# Gmail (requires OAuth credentials)
uv run python -m importers.orchestrator --importer gmail

# WhatsApp exports
uv run python -m importers.orchestrator --importer whatsapp

# Files from Synology NAS
uv run python -m importers.orchestrator --importer synology-nas
```

See [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md) for adding new importers or setting up your dev environment.

---

## Local Development (without Docker)

```bash
# Install all dependencies
uv sync --all-packages --group dev

# Run the dashboard
uv run streamlit run apps/admin-dashboard/app.py

# Run tests
uv run pytest
```

You'll need Ollama and Qdrant running separately:

```bash
ollama serve                  # terminal 1
docker run -p 6333:6333 qdrant/qdrant   # terminal 2
```

---

## Configuration

Copy `.env.example` to `.env` and adjust if needed:

```bash
cp .env.example .env
```

Key variables:

| Variable          | Default               | Description               |
| ----------------- | --------------------- | ------------------------- |
| `OLLAMA_BASE_URL` | `http://ollama:11434` | Ollama API URL            |
| `QDRANT_URL`      | `http://qdrant:6333`  | Qdrant URL                |
| `MAPPING_DB_PATH` | `/data/mapping.db`    | PII mapping database path |

---

## Project Structure

```
.
├── apps/
│   ├── admin-dashboard/    # Streamlit chat UI
│   ├── importers/          # Data ingestion (Gmail, WhatsApp, etc.)
│   └── orchestrator/       # Ingestion pipeline runner
├── libs/
│   ├── embedding/          # Ollama embedding wrapper
│   ├── vector-storage/     # Qdrant client wrapper
│   └── privacy-core/       # PII scrubbing (Presidio + SQLite)
├── infrastructure/         # Terraform for GCP deployment
├── scripts/                # Operational helpers
├── docker-compose.yml      # Local stack (Ollama + Qdrant + Dashboard)
└── pyproject.toml          # uv workspace root
```

---

## Architecture

See [`docs/architecture.md`](docs/architecture.md) for the full system design. For GCP/cloud deployment, see `infrastructure/`.

## Upcoming Architectural Milestones

See [Technical Roadmap](docs/how-my-independent-ai-works/technical-roadmap.md) for our technical roadmap.
