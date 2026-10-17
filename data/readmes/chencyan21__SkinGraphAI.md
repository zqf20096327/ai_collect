# SkinGraph AI

SkinGraph AI is a small, end-to-end demonstration of a safe dermoscopy workflow. It connects image gating, structured SkinVL-style findings, evidence-aware explanation, persistent LangGraph human review, and final output guardrails without requiring model weights, a dedicated dataset, Qdrant, Ollama, or network access.

> **SIMULATED / DEMO**: The default image router, SkinVL findings, and RAG evidence backends are deterministic simulations. Their output is not a clinical diagnosis, medical advice, or a claim about the real SkinVL model's performance.

## Supported Scope

- Dermoscopy image analysis with structured findings
- General skin and dermoscopy knowledge questions
- Optional web search for time-sensitive skin-domain questions
- Human approve, edit, or reject review for every supported image analysis

Ordinary skin photographs, pathology slides, chest X-rays, MRI scans, and unrelated medical questions are outside the active product scope. Historical implementations remain in the repository for reference but are not part of the SkinVL runtime path.

## Demo Workflow

```text
image + question
  -> dermoscopy gate
  -> mock SkinVL raw JSON
  -> parse / repair / schema validation / normalization
  -> image-question consistency check
  -> retrieval_bundle + multimodal_context
  -> demo RAG explanation
  -> LangGraph interrupt
  -> approve / edit / reject
  -> output guardrails
  -> final response
```

Unsupported images stop after the image gate. They do not call SkinVL or RAG. Invalid SkinVL output produces a safe failure draft and still enters human review. An `uncertain` result remains uncertain throughout the response.

## Demo Scenarios

Set `SKINVL_DEMO_SCENARIO` to one of:

| Scenario | Expected behavior |
| --- | --- |
| `supported_high_risk` | Supported dermoscopy image with high-risk simulated findings |
| `supported_benign` | Supported dermoscopy image with benign-leaning simulated findings |
| `supported_uncertain` | Supported image whose uncertainty is preserved downstream |
| `unsupported_image` | Rejected by the image gate without SkinVL or RAG |
| `skinvl_error` | Safe SkinVL failure draft followed by human review |

The default is `supported_high_risk`.

## Quick Start

Requirements:

- Python 3.13 or newer
- `uv`

Create the local environment and start FastAPI with the mounted Chainlit UI:

```bash
cp .env.example .env
uv sync
uv run uvicorn app:app --host 0.0.0.0 --port 8000
```

Open `http://localhost:8000`. The Chainlit UI is mounted at `/chainlit/`.

Default demo mode works without Ollama, Qdrant, Hugging Face downloads, Tavily, or a dedicated dataset. Placeholder Chainlit reviewer credentials disable login; replace them in `.env` to enable reviewer authentication and login-backed history.

### Optional Backends

The default installation is intentionally limited to the offline demo. Install only the integrations you need:

```bash
uv sync --extra rag       # Docling, Ollama/Qdrant RAG, reranking
uv sync --extra skinvl    # Transformers, PyTorch, real SkinVL adapter
uv sync --extra web       # Tavily web search
uv sync --all-extras      # All optional and legacy integrations
```

Installing an extra does not enable it automatically. Configure the corresponding values in `.env` and set `SKINVL_DEMO_MODE=false` when using real runtime backends.

You can also start the application directly with the configured host and port:

```bash
uv run python app.py
```

In the Chainlit page, send a text question or attach a PNG/JPG/JPEG dermoscopy image. Supported image requests pause for an approve, edit, or reject decision before the final response is returned. The same workflow is available through the HTTP endpoints documented below.

### Docker

The repository includes a Dockerfile for a containerized deployment:

```bash
docker build -t skinvl-demo .
docker run --rm -p 8000:8000 --env-file .env skinvl-demo
```

The container serves the API and Chainlit UI at `http://localhost:8000`.

## Configuration

The main demo settings are:

```dotenv
SKINVL_DEMO_MODE=true
SKINVL_DEMO_SCENARIO=supported_high_risk
WEB_SEARCH_ENABLED=false
UPLOAD_RETENTION_MINUTES=60
```

`UPLOAD_RETENTION_MINUTES` keeps uploaded originals available while a LangGraph review is interrupted. A background cleanup removes expired backend uploads after the retention window.

Real model, vector database, and web search variables remain in `.env.example` as optional integration points. The demo does not download or validate the real `zwq803/SkinVL-MM` model.

## API

The existing endpoints remain available:

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/health` | Demo mode, scenario, backend types, and retention metadata |
| `POST` | `/chat` | Skin-domain text questions and product conversation |
| `POST` | `/upload` | Dermoscopy image plus optional question |
| `POST` | `/validate` | Resume the same LangGraph thread with approve/edit/reject |

Image and review responses expose optional structured fields including `simulation`, `backend_metadata`, `image_routing`, `image_findings`, `retrieval_bundle`, `sources`, and `review_state`.

Preserve the `session_id` cookie between `/upload` and `/validate` so the review resumes the interrupted thread:

```bash
curl -c cookies.txt \
  -F "image=@sample_images/skin_lesion_images/ISIC_0020879.jpg" \
  -F "text=What dermoscopic features are visible?" \
  http://localhost:8000/upload

curl -b cookies.txt \
  -F "validation_result=approve" \
  http://localhost:8000/validate
```

Use `validation_result=edit` with `edited_response`, or `validation_result=reject` with `comments`, for the other review paths.

## Tests

The contract and workflow suite is designed to run offline:

```bash
uv run --no-sync python -m unittest discover -s tests -v
```

Coverage focuses on the SkinVL schema, fixed three-item differentials, supported and unsupported image paths, mismatch handling, simulated backend failures, human review resumption, API response contracts, and upload retention.

## Project Status

This repository is an educational engineering demonstration. It intentionally does not include training, fine-tuning, data labeling, a formal benchmark, clinical accuracy claims, confidence calibration, or production-grade medical validation.

The current workflow, RAG pipeline, and SkinVL field contract are documented in [`docs/`](docs/).

## Repository Layout

| Path | Description |
| --- | --- |
| `app.py` | FastAPI API and Chainlit mount |
| `chainlit_app.py` | Chainlit chat and human-review UI |
| `agents/agent_decision_multi_agent.py` | LangGraph workflow entry point |
| `agents/image_analysis_agent/` | Image routing and SkinVL backends |
| `agents/rag_agent/` | Retrieval, reranking, and response generation |
| `data/raw_extras/` | Optional source documents for the RAG pipeline |
| `tests/` | Offline contract and workflow tests |

## Optional RAG Ingestion

The checked-in demo uses the deterministic RAG backend. To rebuild a local knowledge base for the runtime RAG path, inspect the ingestion options first and run:

```bash
uv sync --extra rag
uv run python ingest_rag_data.py --help
```

Runtime RAG requires the configured embedding model and Qdrant/Ollama services. Generated indexes and parsed document exports are intentionally ignored by Git and must be rebuilt locally.

## Data and Privacy

Do not upload identifiable patient data. Uploaded images are stored locally for the configured review-retention window and then removed by the background cleanup task. Historical papers, sample images, model weights, and media in this repository may have licensing terms separate from the project source-code license; verify their provenance before redistribution.

## License

See [`LICENSE`](LICENSE).
