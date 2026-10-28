# Ollama RAG + Reranker (CLI)

A command-line experiment for comparing retrieval with and without reranking on a small text corpus. It uses:

- **Ollama** for embeddings and chat generation
- **HNSWVectorDB** for vector search
- **FlagEmbedding** for reranking (selectable in the CLI)

![RAG Flow](assets/cli.png)

## Quick Start

Requires Python 3.11+, uv, and a running Ollama server. Run from the repository root:

```bash
git clone https://github.com/00200200/ollama-rag-reranker.git
cd ollama-rag-reranker

# Install dependencies
uv sync

# Download the models configured in src/rag/ (once)
ollama pull hf.co/CompendiumLabs/bge-base-en-v1.5-gguf:Q4_K_M
ollama pull hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF:Q4_K_M

# Run interactive CLI
uv run python main.py
```

The CLI indexes `data/cat-facts.txt` at each startup. It also loads the
`BAAI/bge-reranker-base` model on import, even in `none` mode; the first load may
download model weights. Selecting `none` skips reranking, not model loading.

## How it Works

- `src/rag/embedding.py`: Embeds text with Ollama.
- `src/db/db_handler.py`: HNSW index for `TextDoc`, search + convenience helpers.
- `src/rag/rerank.py`: Reranker (`BAAI/bge-reranker-base`) to rescore candidates.
- `src/rag/llm.py`: Generates the final answer from context using an Ollama chat model.

## Project Structure

```
ollama-rag-reranker/
├── assets/                  # README images (screenshots)
├── data/
│   └── cat-facts.txt        # Sample corpus
├── main.py                  # Interactive CLI
└── src/
    ├── data/dataio.py
    ├── db/db_handler.py
    └── rag/
        ├── embedding.py
        ├── llm.py
        └── rerank.py
```

## Interactive CLI

The CLI lets you change the number of context passages and compare `none`,
`rerank`, and `both` modes. The following is an abbreviated example of the output
in `both` mode, not a measured comparison of answer quality:

```
$ uv run python main.py
========================================
       RAG MENU | k=6 | mode=both
========================================
  1) Ask question
  2) Change k
  3) Change mode [none|rerank|both]
  4) Exit
╚══════════════════════════════════════════════╝
Select: 1
Question: How much time does a cat sleep?

--- NO-RERANK ANSWER ---
... generated answer ...
├────────────────────────────┤
[1] Cats sleep 16 to 18 hours per day.
...
└────────────────────────────┘

--- RERANK ANSWER ---
... generated answer ...
├────────────────────────────┤
[1] Cats sleep 16 to 18 hours per day.
...
└────────────────────────────┘
```

## Configuration

Change default models in:

- `src/rag/embedding.py`: `emb_model`
- `src/rag/llm.py`: `model`, `system_prompt`

## Screenshots

![RAG Flow](assets/answer.png)
