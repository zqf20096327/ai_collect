# ⚡ Local AI Engineering Studio

A 100% private, offline, and free local AI engineering workbench with dual UI frontends (**Gradio** & **Streamlit**), powered by **Ollama**, **DuckDB**, and local tokenizers (**Google GenAI / SentencePiece**).

Zero cloud dependencies, zero telemetry, and no external API keys required.

---

## 🌟 Modules & Features

1. **🤖 Local Model Inference**
   - Connects to local [Ollama](https://ollama.com) models (`qwen2.5-coder`, `llama3.2`, `mistral`, etc.).
   - Streams completions in real time with live TPS (tokens/second) throughput and latency tracking.
   - Automatically logs telemetry into an embedded DuckDB database.

2. **📚 Document Search & Indexing (Local RAG)**
   - Chunk and index private notes, specifications, or documents directly into a local embedded **DuckDB** instance.
   - Run offline keyword and full-text retrieval queries with zero cloud exposure.

3. **🔍 Codebase Token Auditor**
   - Recursively scans local directories across configurable file extensions (`.py`, `.md`, `.toml`, `.json`, `.sql`, etc.).
   - Computes exact token footprints with offline tokenizers.
   - Generates interactive Plotly Treemap charts showing token distribution before sending code to LLM context windows.

4. **⚖️ Prompt Comparison & Eval**
   - Side-by-side prompt engineering workspace.
   - Live token counting and differential calculation between prompt variants.
   - Concurrently test variants on local models to validate JSON adherence and outputs.

5. **📊 DuckDB Analytics & SQL Console**
   - Stores prompt logs, token usage, latencies, and speed metrics in `local_analytics.duckdb`.
   - Ad-hoc interactive SQL console to query execution history and model performance aggregates.

6. **🧹 Hardware & VRAM Management**
   - Instant VRAM flush via Ollama's `keep_alive: 0` endpoint and local Python garbage collection.

---

## 🚀 Quick Start

### 1. Prerequisites
- **Python 3.10+** (or modern toolchains like `uv`)
- **[Ollama](https://ollama.com)** running locally:
  ```bash
  ollama serve
  ollama pull qwen2.5-coder:latest   # or your preferred model
  ```

### 2. Setup Environment & Dependencies
```bash
# Clone or navigate to the repository
cd ~/Projects/streamlit-dashboard

# Install dependencies using uv or pip
uv pip install -r requirements.txt
# OR: pip install -r requirements.txt
```

---

## 🖥️ Running the Application

You can run either the **Gradio** app or the classic **Streamlit** dashboard:

### Option A: Gradio Interface (Recommended)
```bash
python app_gradio.py
```
Open **[http://127.0.0.1:7860](http://127.0.0.1:7860)** in your browser.

### Option B: Streamlit Dashboard
```bash
streamlit run dashboard.py
```
Open **[http://localhost:8501](http://localhost:8501)** in your browser.

---

## 📂 Project Structure

```text
├── app_gradio.py          # Refined Gradio web application (side-by-side)
├── dashboard.py           # Streamlit dashboard implementation
├── local_analytics.duckdb # Embedded DuckDB database for logs & RAG chunks
├── local_usage.csv        # Local exported metrics
├── enterprise/            # Enterprise modules and utilities
├── desktop-wrappers/      # Desktop packaging scripts
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

---

## 🔒 Privacy & Local-First Guarantees
- All prompts, outputs, documents, and analytics are persisted exclusively to local files (`local_analytics.duckdb`).
- Token counting is executed strictly in-process with local tokenizer binaries.
- No network requests are made outside of `localhost` / `127.0.0.1`.
