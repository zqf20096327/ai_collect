# 🧠🖼️📄 Multimodal RAG Demo (Qwen3-VL)

Try the future of RAG - **multimodal RAG** - that effortlessly brings **PDFs, images, and text** together in one index: **ingest → retrieve → rerank → (optionally) answer with sources**.  

![Multimodal RAG UI](assets/screenshot.png)

---

## ✨ Why multimodal RAG?
Traditional RAG is great when everything is plain text. Real documents aren’t.

PDFs often contain:
- 📊 charts and tables
- 🧾 scanned pages / images of text
- 🧩 figures with crucial labels
- 🧠 context split across captions + visuals

**Multimodal RAG** lets you retrieve from *both*:
- 📝 plain text (searchable chunks)
- 🖼️ rendered page images / standalone images (visual understanding)

That means you can ask questions like:
- “Which page contains the table with latency numbers?”
- “Where is the screenshot that shows the error dialog?”
…and get results that actually reflect the *document as it exists*, not just what text extraction managed to capture.

You can even **search** the index using example images, not just with text queries!

---

## 🚀 Why Qwen3-VL for this demo?
This demo uses Apache-2.0 Qwen3-VL models designed specifically for **vision-language embedding and reranking**:

- 🧲 **Qwen3-VL Embedding**: turns *text + images* into vectors in the same semantic space  
  → You can retrieve “the right page image” even if the answer isn’t explicitly in extracted text.

- 🏁 **Qwen3-VL Reranker** (optional): reorders the initial candidates with a stronger cross-encoder  
  → Better top results, fewer “almost relevant” hits.

---

## 🧰 What you get
- 📥 Ingest **PDFs** (page images + extracted text), **images**, and **text files**
- 🧲 Multimodal embeddings with **Qwen3-VL**
- 🏁 Multimodal reranker support (**toggleable**) for improved ordering
- 📝🖼️ Text or image queries (or both)
- ✍️ Optional **answer generation** with source context:
  - fully local via `transformers`, or
  - via an **OpenAI-compatible API** (local or remote)
- 💾 Disk-backed index for quick restarts
- 🌐 Web UI at `/` for ingest + query

---

## 🖥️ Quick starts
Open the UI after launch: `http://localhost:8000/`

### 0) Retrieval only (no answer generation) 🔎
```bash
uv run qwen3vl_multimodal_rag_server.py
```
### 1) Fully local (built-in generation via transformers) 🏠
```bash
uv run qwen3vl_multimodal_rag_server.py --enable-generator
```
### 2) Local LLM via LM Studio or any other OpenAI-compatible API 🔌
```bash
uv run qwen3vl_multimodal_rag_server.py \
  --enable-generator \
  --generator-backend openai \
  --generator-remote-endpoint http://localhost:1234/v1
```
Tip: set OPENAI_API_KEY in a .env file. Many local servers accept any value.

### 3) Remote OpenAI answer generation ☁️
```bash
uv run qwen3vl_multimodal_rag_server.py \
  --enable-generator \
  --generator-backend openai \
  --generator-remote-model gpt-5-mini \
  --generator-remote-reasoning-effort minimal
```
Create a .env with OPENAI_API_KEY=... before starting.

# Typical workflow

1. 📥 Drop a few PDFs / images  
2. ❓ Ask a question  
3. 🔎 See retrieved sources (text chunks + page images)  
4. ✍️ Turn on generation when you want an answer with citations  

---

## Parameters

All available CLI parameters (defaults shown):

| Flag | Default | Description |
|---|---:|---|
| `--host` | `0.0.0.0` | Bind address for the server. |
| `--port` | `8000` | Port for the server. |
| `--log-level` | `info` | Logging level (`debug`, `info`, `warning`, `error`). |
| `--data-dir` | `./qwen3vl_rag_data` | Storage directory for the index, originals, and derived assets. |
| `--device` | `auto` | Device selection (`auto`, `cuda`, `mps`, `cpu`). |
| `--embedder-model` | `Qwen/Qwen3-VL-Embedding-2B` | Embedding model name. |
| `--embedder-quant` | `off` | Embedder quantization (`off`, `8bit`, `4bit`). |
| `--reranker-model` | `Qwen/Qwen3-VL-Reranker-2B` | Reranker model name. |
| `--reranker-quant` | `off` | Reranker quantization (`off`, `8bit`, `4bit`). |
| `--disable-reranker` | `false` | Disable reranking. |
| `--generator-model` | `Qwen/Qwen3-VL-2B-Instruct` | Local generator model name. |
| `--generator-quant` | `off` | Generator quantization (`off`, `8bit`, `4bit`). |
| `--enable-generator` | `false` | Enable answer generation. |
| `--generator-backend` | `transformers` | Generator backend (`transformers`, `openai`). |
| `--generator-remote-endpoint` | `None` | Base URL for OpenAI-compatible APIs. |
| `--generator-remote-model` | `None` | Model name for OpenAI-compatible APIs. |
| `--generator-remote-reasoning-effort` | `medium` | Reasoning effort for remote generator (`none`, `minimal`, `low`, `medium`, `high`, `xhigh`). |
| `--text-chunk-size` | `1200` | Text chunk size during ingestion. |
| `--text-chunk-overlap` | `200` | Overlap between text chunks. |
| `--pdf-dpi` | `75` | DPI for rendering PDF pages (also used to downscale images). |
| `--pdf-max-pages` | `0` | If `>0`, only ingest the first `N` pages of a PDF. |

---

## Notes

- `.env` is loaded automatically at startup (for `OPENAI_API_KEY` or other env vars).
- Retrieval defaults: `top_k=4`, `rerank_k=4` (can be overridden per query in the API).
- The UI exposes `/ingest` and `/query` and shows metadata from `/health`.

