# AskDocs AI: AI-Powered PDF Q&A Bot

**AskDocs AI** is an AI-powered chatbot that leverages **Hybrid RAG (Retrieval-Augmented Generation)** to answer your questions based on the content of uploaded PDFs. It combines semantic vector search with traditional keyword-based search for superior accuracy.

<img src="./images/landing_page.png" alt="Landing Page">
<img src="./images/chat_interface.png" alt="Chat Interface">

## Key Features

- **Hybrid Search**: Combines **ChromaDB** (semantic) and **BM25** (keyword) retrieval.
- **LLM Powered**: High-performance LLM via Groq Cloud.
- **Async Processing**: PDF ingestion and indexing are offloaded to background threads.
- **Multimodal Support**: Optimized for PDF extraction and processing.

## Tech Stack

- **Backend:** FastAPI, LangChain (Classic), ChromaDB, Groq Cloud
- **Frontend:** Streamlit
- **Search Engines:** BM25 (Keyword), Vector (Cosine Similarity)
- **Embeddings:** HuggingFace (Sentence Transformers)
- **Containerization:** Docker & Docker Compose

## Configuration

Control the behavior of the Hybrid Search by adjusting weights in your `.env` file or `server/config.py`:

| Variable | Description | Default |
|----------|-------------|---------|
| `HYBRID_SEARCH_BM25_WEIGHT` | Weight for keyword search (0.0 to 1.0) | `0.5` |
| `HYBRID_SEARCH_CHROMA_WEIGHT` | Weight for semantic search (0.0 to 1.0) | `0.5` |
| `GROQ_API_KEY` | Your Groq Cloud API Key | *Required* |

## Optimization Features

- **Split Dependencies**: Client and Server have separate requirement files to minimize image sizes.
- **CPU-Only Optimization**: Server image is optimized for CPU-only environments, reducing size from ~12.8GB to ~2.3GB.
- **Persistent Memory**: Uses Docker volumes to persist the ChromaDB vector store and uploaded files.

## Setup Instruction

### 1. Set up environment variables
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_api_key_here
```

### 2. Run with Docker (Recommended)
```sh
docker-compose up -d --build
```
- **Streamlit UI**: [http://localhost:8501](http://localhost:8501)
- **FastAPI Docs**: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### Alternative: Local Setup

1. **Create and activate a virtual environment**
   ```sh
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   ```

2. **Install dependencies**
   ```sh
   pip install -r requirements.client.txt
   pip install -r requirements.server.txt
   ```

3. **Run the services**
   ```sh
   # Backend
   python server/main.py
   
   # Frontend
   streamlit run client/main.py
   ```

## Testing & Verification

To verify that the Hybrid Search mechanism and LLM integration are working correctly:

```sh
python server/tests/test_hybrid_search.py
```
This script validates:
1. Vectorstore connectivity.
2. BM25 index reconstruction.
3. Ensemble Retriever initialization.

