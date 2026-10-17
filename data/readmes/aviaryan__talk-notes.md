# 🗣️📚 Talk Notes

A conversational AI assistant that lets you chat with your Obsidian notes using RAG (Retrieval-Augmented Generation). Ask questions about your notes and get intelligent, context-aware responses.

## 🎬 DEMO

https://github.com/user-attachments/assets/3fd7e668-60bb-4cbc-b691-4d65e5337a41


## ✨ Features

- **Semantic Search**: Find relevant notes based on meaning, not just keywords
- **Recency-Aware Retrieval**: Prioritizes recently modified notes for more relevant results
- **Local Embeddings**: Uses BGE embeddings via HuggingFace (runs entirely on your machine)
- **Fast Vector Search**: Powered by FAISS for efficient similarity search
- **Conversational Interface**: Chat naturally with your notes through a web UI
- **Privacy-Focused**: Your notes are processed locally; only queries go to the LLM
- **Flexible LLM Options**: Use Google Gemini or run completely locally with Ollama


## ✅ Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager
- [Ollama](https://ollama.ai/) for local LLM **OR** Google API key (for Gemini LLM)

## 🛠️ Installation

1. **Clone the repository**

   ```sh
   git clone https://github.com/aviaryan/talk-notes.git
   cd talk-notes
   ```

2. **Install dependencies**

   ```sh
   uv sync
   ```

3. **Configure environment variables**

   Create a `.env` file in the project root (refer to [.env.example](.env.example) for reference)):

   ```sh
   # Required
   MARKDOWN_FOLDER_PATH=/path/to/your/obsidian/vault

   # For local AI queries with Ollama
   USE_LOCAL_MODEL=true
   OLLAMA_MODEL=ministral-3:8b

   # Optional
   VECTOR_STORE_PATH=vectorstore.faiss
   BGE_EMBEDDING_MODEL=BAAI/bge-small-en
   ```

## 🚀 Usage

### 1. Ingest Your Notes

First, process your Obsidian vault to create the vector store:

```sh
uv run python app/ingest.py
# OR
make ingest
```

This will:
- Load all Markdown files from your vault
- Split them into chunks
- Generate embeddings using BGE
- Save the vector store locally

### 2. Start the Chat Interface

Launch the LangGraph development server:

```sh
uv run langgraph dev --allow-blocking
```

Then open [Agent Chat](https://agentchat.vercel.app/) in your browser to start chatting with your notes.

You can also use the convenience script that runs langgraph and opens Agent Chat for you.

```sh
./scripts/start_chat.sh
# OR
make chat
```


## ⚙️ Configuration

| Environment Variable | Description | Default |
|---------------------|-------------|---------|
| `MARKDOWN_FOLDER_PATH` | Path to your Obsidian vault | Required |
| `GOOGLE_API_KEY` | Google API key for Gemini | Optional (unless using gemini model) |
| `GOOGLE_MODEL` | Google Gemini model to use | `gemini-3-flash-preview` |
| `USE_LOCAL_MODEL` | Use Ollama instead of Google Gemini | `false` |
| `OLLAMA_MODEL` | Ollama model to use when `USE_LOCAL_MODEL=true` | - |
| `VECTOR_STORE_PATH` | Path to save/load the vector store | `vectorstore.faiss` |
| `BGE_EMBEDDING_MODEL` | HuggingFace BGE model for embeddings | `BAAI/bge-small-en` |
| `LANGSMITH_API_KEY` | LangSmith API key for tracing (optional) | - |

### 🧠 Embedding Models

You can use different BGE models based on your needs:

- `BAAI/bge-small-en` - Fast, lower memory (default)
- `BAAI/bge-base-en` - Balanced performance
- `BAAI/bge-large-en` - Best quality, higher resource usage

### 🧩 Local LLM with Ollama

For fully local operation (no API keys needed), you can use Ollama:

1. Install [Ollama](https://ollama.ai/)
2. Pull a model: `ollama pull ministral-3:8b`
3. Set variables in `.env` file:
   ```sh
   USE_LOCAL_MODEL=true
   OLLAMA_MODEL=ministral-3:8b
   ```

Popular Ollama models for this use case:
- `ministral-3:8b` - Good balance of quality and speed
- `ministral-3:14b` - Better than the above but slower
- `gemma3:12b` - `ministal-3:8b` outperforms this in my experience, not recommended


## 🧭 How It Works

1. **Ingestion**: Markdown files are loaded with metadata (including modification time), split into chunks, and embedded using BGE models.

2. **Retrieval**: When you ask a question, the system performs a semantic search with recency scoring:
   - Fetches semantically similar chunks
   - Applies a recency boost to recently modified notes
   - Returns the most relevant context

3. **Generation**: The retrieved context is injected into the prompt, and the LLM (Gemini or Ollama) generates a response based on your notes.

## 👩‍💻 Development

Format code with Ruff:

```sh
uv run ruff format
```

