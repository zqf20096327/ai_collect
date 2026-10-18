# Academic Deep Search & QA

A local research assistant: you give it a topic, it searches [Semantic Scholar](https://www.semanticscholar.org/product/api), filters papers, builds a [RAPTOR](https://arxiv.org/abs/2401.18059) summary tree, and answers questions from that corpus. Chat, summarization, and embeddings all go through a **llama.cpp `llama-server`** over its OpenAI-compatible `/v1` API.

The algorithms live in an installable Python package, `academic_deepsearch`. Streamlit is only the UI.

## What it does

1. **Paper discovery** — Semantic Scholar bulk search (or a built-in mock corpus in debug mode).
2. **Filtering** — publisher / journal match, drop papers with no abstract, then an LLM yes/no relevance check.
3. **RAPTOR indexing** — cluster chunks, summarize clusters, repeat until one root; retrieve from the full tree via FAISS.
4. **Conversational QA** — answers are grounded in retrieved nodes only.
5. **Exports** — academic-style PDF report, pipeline Mermaid diagram, and a bibliography of kept and discarded papers.

## Tech stack

- **Library:** `academic_deepsearch` (LangGraph pipeline, RAPTOR, filters, reports)
- **Search:** Semantic Scholar API
- **Models:** llama.cpp `llama-server` (`/v1/chat/completions`, `/v1/embeddings`, `/v1/models`, `/health`)
- **UI:** Streamlit
- **Glue:** LangChain + `langchain-openai` pointed at the local server

## Requirements

- Python 3.11 or 3.12
- A running [`llama-server`](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md)
  - Chat GGUF on one port (default `8080`)
  - Embeddings need pooling enabled (`--embeddings`), often on a **second** server (default `8081`)
- Optional: Semantic Scholar access for live search (debug mode does not need it)

## Install

```bash
git clone https://github.com/iblameandrew/local-deepsearch-academic.git
cd local-deepsearch-academic

python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate

pip install -e ".[app]"
```

For tests and lint: `pip install -e ".[dev]"`.

`requirements.txt` pins the same runtime stack if you prefer a flat install.

## Run llama.cpp

Two processes are the usual setup, because one `llama-server` is typically either a chat model or an embedding model:

```bash
llama-server -m /path/to/chat.gguf --host 127.0.0.1 --port 8080
llama-server -m /path/to/embed.gguf --host 127.0.0.1 --port 8081 --embeddings
```

Environment variables (also used by Docker):

| Variable | Default | Purpose |
|---|---|---|
| `LLAMA_CPP_BASE_URL` | `http://127.0.0.1:8080/v1` | Chat, relevance, summaries, report rewrite |
| `LLAMA_CPP_EMBED_BASE_URL` | same as chat URL | Embeddings |
| `LLAMA_CPP_API_KEY` | `sk-no-key` | Dummy key for the OpenAI client; set this if you started the server with `--api-key` |

The sidebar talks to `GET /health` and `GET /v1/models`. If the server is down you can still type a model id by hand.

## Run the app

```bash
streamlit run app.py
```

Configure the topic, publishers, and llama.cpp URLs in the sidebar, then start the pipeline. Enable **Debug Mode** to run search against the built-in mock papers (the LLM still comes from llama.cpp).

## Use the library

```python
from academic_deepsearch import (
    ResearchConfig,
    ResearchPipeline,
    MockSearcher,
)

config = ResearchConfig(
    query="indoor air quality monitoring using machine learning",
    publishers=["IEEE", "ACM", "Springer", "Elsevier", "Arxiv", "Scholar"],
    max_results=100,
    llm_base_url="http://127.0.0.1:8080/v1",
    embed_base_url="http://127.0.0.1:8081/v1",
    chat_model="local",
    embedding_model="local",
)

# Offline / tests: inject search + model fakes.
# Live: omit searcher/llm/embeddings and the pipeline will call Semantic Scholar
# and llama.cpp using the URLs above.
result = ResearchPipeline(config, searcher=MockSearcher()).run()
docs = result.retrieve("What clustering method is used?")
```

Lower-level helpers (`filter_by_publisher`, `filter_by_relevance`, `RAPTORIndex`, PDF/Mermaid/report builders) are exported from `academic_deepsearch`.

The package does **not** import Streamlit. Pass a `ProgressReporter` if you want logs; tests use `NullReporter`.

## Docker

```bash
# App container; llama-server stays on the host
docker compose up app --build

# Offline test image (no llama.cpp, no Semantic Scholar)
docker compose run --rm test
```

The app container defaults `LLAMA_CPP_BASE_URL` to `http://host.docker.internal:8080/v1`.

Optional compose profile `llm` starts `ghcr.io/ggml-org/llama.cpp:server` and expects `./models/chat.gguf` and `./models/embed.gguf`. It is not used in CI.

```bash
docker compose --profile llm up
```

## Tests and CI

```bash
pytest
pytest --cov --cov-report=term-missing
ruff check academic_deepsearch tests app.py
```

The default suite is offline. Tests marked `@pytest.mark.live` (network / llama.cpp) are excluded unless you pass `-m live`.

GitHub Actions (`.github/workflows/ci.yml`) runs Ruff, pytest on Python 3.11 and 3.12, and builds both the `test` and `runtime` Docker stages.

## Who this is for

- **Students and academics** — literature review starting point, theme extraction, structured Q&A export.
- **Engineers** — get up to speed on a method from the primary papers.
- **Anyone** who wants a local, inspectable RAG loop over real abstracts.

## Contributing

Issues and pull requests are welcome: [iblameandrew/local-deepsearch-academic](https://github.com/iblameandrew/local-deepsearch-academic).
