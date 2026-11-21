# 📜 Doc_Query_Genie

🚀 **Ask questions about your PDFs with a local LLM.** Retrieval-Augmented Generation (RAG) with Llama 3, LangChain, Ollama and ChromaDB, served by a Flask API with a built-in web UI.

![PDF_Searcher](https://github.com/user-attachments/assets/053688a0-63e7-4005-a258-69bc4200913a)

## 🔍 About

Upload a PDF, then ask questions about it. Doc_Query_Genie finds the most relevant passages and has a local LLM answer from them, citing each passage by number with its file name and page. Everything runs on your machine: no API keys, and no documents leave your computer.

### ✨ Features

- **PDF Q&A with citations.** Answers cite passages as `[1]`, `[2]`, and each source comes with its file name, page number and text.
- **Per-document search.** Ask about one specific PDF or across all of them.
- **Follow-up questions.** Pass the conversation history and questions like "what did she do next?" work.
- **Streaming.** Answers arrive token by token.
- **Duplicate detection.** Uploading the same file twice doesn't index it twice.
- **General chat.** Talk to the model directly, with no documents involved.
- **Web UI** at `/`, plus a JSON API.

## 🚀 Getting started

### 1. Install Ollama and pull the model

Install [Ollama](https://ollama.com), then:

```sh
ollama pull llama3.2:3b
ollama serve            # if it isn't already running
```

The default `llama3.2:3b` (~2 GB) runs well on an 8 GB machine. With 16 GB or more you can use a larger model for better answers, e.g. `ollama pull llama3.1:8b` and `OLLAMA_MODEL=llama3.1:8b`.

### 2. Install and run

Requires Python 3.10+.

```sh
git clone https://github.com/OmJavia/Doc_Query_Genie.git
cd Doc_Query_Genie
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open **http://127.0.0.1:8080** for the web UI. The first start downloads the embedding model (~70 MB).

> Answer speed depends on your hardware. On a machine without a strong GPU, Ollama can take a minute or more to read the retrieved passages. Use `"stream": true` (the UI does) to see text as soon as it's generated.

### Run with Docker

Ollama keeps running on the host. The container reaches it via `host.docker.internal`.

```sh
docker build -t doc-query-genie .
docker run -p 8080:8080 -v dqg-data:/data doc-query-genie
```

On Linux, add `--add-host=host.docker.internal:host-gateway`.

## ⚙️ Configuration

Everything is set through environment variables:

| Variable | Default | Meaning |
|---|---|---|
| `OLLAMA_BASE_URL` | `http://localhost:11434` | Where Ollama is running |
| `OLLAMA_MODEL` | `llama3.2:3b` | Any chat model you've pulled |
| `OLLAMA_NUM_CTX` | `4096` | Context window in tokens. Bigger uses more RAM |
| `OLLAMA_KEEP_ALIVE` | `5m` | How long the model stays loaded after a request. `0` frees RAM immediately |
| `LLM_TEMPERATURE` | `0.1` | Lower = more factual |
| `DATA_DIR` | `data` | Uploaded PDFs (`uploads/`) and vector store (`chroma/`) |
| `EMBEDDING_MODEL` | `BAAI/bge-small-en-v1.5` | FastEmbed model |
| `EMBEDDING_BATCH_SIZE` | `8` | Chunks embedded at once while indexing. Higher uses much more RAM |
| `CHUNK_SIZE` / `CHUNK_OVERLAP` | `1000` / `150` | Characters per chunk |
| `TOP_K` / `FETCH_K` | `4` / `20` | Passages sent to the LLM / candidates considered (MMR) |
| `MAX_HISTORY_MESSAGES` | `10` | Conversation messages kept per request |
| `MAX_UPLOAD_MB` | `25` | Upload size limit |
| `HOST` / `PORT` | `127.0.0.1` / `8080` | Use `HOST=0.0.0.0` to allow other machines |
| `DEBUG` | `false` | Flask debug mode. Never enable on a network-reachable host |

### Running on an 8 GB machine

Most of the memory goes to the LLM inside Ollama, not to this app. The app itself uses about 350 MB, peaking around 750 MB while indexing a PDF. To keep things responsive:

- Stick with a 3B model (the default) or smaller. `qwen2.5:1.5b` and `llama3.2:1b` (~1 GB) are lighter still, at some cost in answer quality.
- Set `OLLAMA_KEEP_ALIVE=0` if you want Ollama to release the model's memory right after each answer. The next question then takes a few extra seconds to load it.
- Tell Ollama itself to stay lean. These are settings for the Ollama server, not this app. On macOS, run the following and then restart Ollama:
  ```sh
  launchctl setenv OLLAMA_MAX_LOADED_MODELS 1   # never keep two models in memory
  launchctl setenv OLLAMA_NUM_PARALLEL 1        # one request at a time (each parallel slot reserves its own memory)
  launchctl setenv OLLAMA_FLASH_ATTENTION 1
  launchctl setenv OLLAMA_KV_CACHE_TYPE q8_0    # halves the context memory, negligible quality loss
  ```
- Close other heavy apps (browsers especially) while asking questions.

## 📡 API

### Upload a PDF: `POST /documents` (or `/pdf`)

```sh
curl -F file=@pdf/alice.pdf http://127.0.0.1:8080/documents
```
```json
{"status": "indexed", "doc_id": "31ffbb580c5c2d8a", "filename": "alice.pdf", "pages": 80, "chunks": 214, "uploaded_at": "..."}
```
Returns `201` when newly indexed, or `200` with `"status": "already_indexed"` for a file that's already there.

### Ask about documents: `POST /ask_pdf`

```sh
curl -X POST http://127.0.0.1:8080/ask_pdf -H 'Content-Type: application/json' \
  -d '{"query": "What does Alice see as she falls?", "doc_id": "31ffbb580c5c2d8a"}'
```
```json
{
  "answer": "She sees cupboards and book-shelves, and maps and pictures hung upon pegs [1].",
  "sources": [{"id": 1, "doc_id": "31ffbb580c5c2d8a", "filename": "alice.pdf", "page": 2, "content": "..."}]
}
```

Body fields:
- `query` (required)
- `doc_id` (optional; omit to search all documents)
- `history` (optional; `[{"role": "user"|"assistant", "content": "..."}]` for follow-ups)
- `stream` (optional, default `false`)

### General chat: `POST /ai`

Same body as above, without `doc_id`. Returns `{"answer": "...", "sources": []}`.

### Streaming

With `"stream": true`, the response is [NDJSON](https://github.com/ndjson/ndjson-spec), one event per line:

```
{"type": "sources", "sources": [...]}
{"type": "token", "content": "She"}
{"type": "token", "content": " sees"}
{"type": "done"}
```
If generation fails midway, the last line is `{"type": "error", "error": "..."}`.

### Other endpoints

| | |
|---|---|
| `GET /documents` | List indexed documents |
| `DELETE /documents/<doc_id>` | Remove a document and its index |
| `GET /health` | Whether Ollama is reachable and the model is pulled |

Errors are always JSON, `{"error": "..."}`, with a meaningful status: `400` for bad input, `404` for an unknown document, `413` for a file that's too large, `503` when Ollama isn't running.

## 🧪 Development

```sh
pip install -r requirements-dev.txt
pytest
```

The tests use a fake LLM and fake embeddings, so they don't need Ollama.

Project layout:

```
app.py                       # entry point: python app.py
doc_query_genie/
  config.py                  # settings from environment variables
  rag.py                     # ingestion, retrieval, prompting
  web.py                     # Flask routes, validation, errors, streaming
  static/index.html          # web UI
tests/
```

## 🤝 Contributing

Issues and pull requests are welcome.

---
🌟 **If you find this project helpful, please consider giving it a star!**
