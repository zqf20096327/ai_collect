# 🏦 JPMC Intelligence - RAG-Powered Financial Query Assistant

A cutting-edge **Retrieval-Augmented Generation (RAG)** system for answering questions about JPMorgan Chase financial documents with precise, source-grounded responses.

## 🎯 Features

- **Hybrid Search**: Dense (semantic) + Sparse (keyword) retrieval with RRF ranking
- **Cross-Encoder Reranking**: BGE-Reranker for precision matching
- **Multi-Turn Conversations**: History-aware with context preservation
- **Document Analysis**: Browse chunks, analyze distribution by type and year
- **Source Citations**: Every answer includes source document references
- **API-Agnostic**: Works with any LLM via OpenRouter
- **Fully Containerized**: Docker & Docker Compose ready

## 🚀 Quick Start

### Prerequisites
- Python 3.10+ or Docker
- OpenRouter API key
- Hugging Face token
- JPMorgan Chase PDF documents

### Option 1: Local Setup

```bash
# Clone repository
git clone https://github.com/yourusername/jpmc-intelligence.git
cd jpmc-intelligence

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cat > .env << EOF
OPENROUTER_API_KEY=your_api_key
HF_TOKEN=your_hf_token
EOF

# Add your documents
# Place PDF files in JPMorgan_Chase_documents/ folder

# Run the app
streamlit run app.py
```

### Option 2: Docker (Recommended)

```bash
# Start with Docker Compose
docker-compose up -d

# Access at http://localhost:8502
```

See [DOCKER_QUICKSTART.md](DOCKER_QUICKSTART.md) for more options.

## 📊 Architecture

### RAG Pipeline
```
User Query
    ↓
Query Contextualization (resolves pronouns, references)
    ↓
Query Expansion (generates semantic variants)
    ↓
Hybrid Retrieval
  ├─ Dense: BGE embeddings (semantic meaning)
  └─ Sparse: BM25 (exact keywords)
    ↓
Reciprocal Rank Fusion (merges results)
    ↓
Cross-Encoder Reranking (precision refinement)
    ↓
LLM Answer Generation (with full context)
    ↓
Answer + Source Citations
```

### Components

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Embedding | BGE-Base-EN-V1.5 | Dense vector representations |
| Reranker | BGE-Reranker-Base | Cross-encoder precision scoring |
| Vector Store | ChromaDB | Persistent embedding storage |
| Search | BM25 + Dense + RRF | Multi-method retrieval |
| LLM | Qwen2.5-72B (OpenRouter) | Answer generation |
| UI | Streamlit | Interactive web interface |

## 📁 Project Structure

```
jpmc-intelligence/
├── app.py                          # Streamlit UI
├── query_engine.py                 # RAG query engine
├── retriever.py                    # Hybrid search
├── vectorstore.py                  # ChromaDB wrapper
├── chunk.py                        # Document chunking
├── ingest.py                       # PDF ingestion
├── config.py                       # Configuration
├── requirements.txt                # Dependencies
├── Dockerfile                      # Container config
├── docker-compose.yml              # Docker stack
├── DOCKER_SETUP.md                 # Docker guide
├── .gitignore                      # Git exclusions
└── JPMorgan_Chase_documents/       # PDF storage
```

## 🔧 Configuration

Edit `config.py` to customize:

```python
# Models
LLM_MODEL = "qwen/qwen-2.5-72b-instruct"
EMBED_MODEL = "BAAI/bge-base-en-v1.5"
RERANKER_MODEL = "BAAI/bge-reranker-base"

# Retrieval
QUERY_EXPANSION_N = 3          # Number of query variants
TOP_K_DENSE = 10               # Dense search results
TOP_K_SPARSE = 10              # BM25 results
TOP_K_RERANK = 5               # Final reranked results

# LLM
MAX_NEW_TOKENS = 1024
TEMPERATURE = 0.1
MAX_CHAT_HISTORY = 5           # Conversation turns
```

## 📝 Usage

### Chat Interface
1. Open http://localhost:8502
2. Select **Chat** tab (default)
3. Ask questions about JPMorgan Chase documents
4. View source citations with **Show source citations** toggle

### Document Library
1. Click **Document Library** in sidebar
2. View document statistics and distribution
3. Filter by type, year, and search text
4. Browse individual chunks

### Suggested Questions
- "What was JPMC's net revenue in 2023?"
- "Explain JPMorgan's AML policy and key controls."
- "What are JPMC's revenue sources and business segments?"
- "What does the proxy say about executive compensation?"

## 🔑 API Setup

### OpenRouter
1. Get API key from [openrouter.ai](https://openrouter.ai)
2. Add to `.env`: `OPENROUTER_API_KEY=sk-or-...`

### Hugging Face
1. Get token from [huggingface.co](https://huggingface.co/settings/tokens)
2. Add to `.env`: `HF_TOKEN=hf_...`

## 🐳 Docker Deployment

### Quickstart
```bash
docker-compose up -d
```

### Full Guide
See [DOCKER_SETUP.md](DOCKER_SETUP.md)

### Production Deployment
```bash
# Build image
docker build -t jpmc-intelligence:v1.0 .

# Push to registry
docker tag jpmc-intelligence:v1.0 registry.example.com/jpmc-intelligence:v1.0
docker push registry.example.com/jpmc-intelligence:v1.0

# Deploy with resource limits
docker run -d \
  -p 8502:8502 \
  --env-file .env \
  -v data:/app/data \
  -m 4G \
  --cpus 2 \
  jpmc-intelligence:v1.0
```

## 📊 Document Processing

### Supported Formats
- PDF (.pdf)

### Automatic Classification
Documents are classified as:
- `annual_report` - Annual financial reports
- `financial_statement` - Consolidated statements
- `policy` - Compliance and policy documents
- `proxy` - Proxy filings

### Chunking Strategy
Documents are split with overlap for context preservation:
- Annual Reports: 1200 tokens, 200 overlap
- Financial Statements: 1000 tokens, 150 overlap
- Policies: 600 tokens, 100 overlap
- Proxy: 800 tokens, 120 overlap

## 🧪 Testing

### Unit Tests
```bash
python -m pytest tests/
```

### Integration Tests
```bash
python -m pytest tests/ -v
```

### Manual Testing
1. Start app: `streamlit run app.py`
2. Test suggested questions
3. Check source citations
4. Browse Document Library
5. Verify API connectivity

## 🐛 Troubleshooting

### API Key Issues
```bash
# Test OpenRouter connection
curl -H "Authorization: Bearer YOUR_KEY" \
  https://openrouter.ai/api/v1/models
```

### Model Download Failures
```bash
# Pre-download models
python -c "from sentence_transformers import SentenceTransformer; \
  SentenceTransformer('BAAI/bge-base-en-v1.5')"
```

### Memory Issues
- Reduce `TOP_K_*` values in config.py
- Use lighter embedding model
- Increase Docker memory limit

### Docker Issues
```bash
# Check logs
docker-compose logs -f

# Rebuild image
docker-compose build --no-cache
```

## 📈 Performance

| Operation | Time | Notes |
|-----------|------|-------|
| Query Processing | 2-5s | Includes retrieval + generation |
| Document Ingestion | 5-10min | For ~300 pages |
| First Startup | 2-5min | Model downloads |
| Subsequent Startup | <30s | Cached models |

## 🔒 Security

- ✅ API keys stored in `.env` (not in repo)
- ✅ No data persisted in memory after response
- ✅ Source documents not exposed to users
- ✅ Rate limiting on LLM API calls
- ✅ Input sanitization for queries

## 📜 License

This project is provided as-is. Adjust licensing as needed.

## 🤝 Contributing

Contributions welcome! Please:
1. Fork repository
2. Create feature branch: `git checkout -b feature/description`
3. Commit changes: `git commit -m "description"`
4. Push to branch: `git push origin feature/description`
5. Open Pull Request

## 📧 Support

For issues, questions, or suggestions:
- Open GitHub Issues
- Check documentation in DOCKER_SETUP.md
- Review logs: `docker-compose logs -f`

## 🎓 Learn More

- [RAG Explained](https://docs.llamaindex.ai/en/stable/getting_started/concepts.html)
- [ChromaDB Docs](https://docs.trychroma.com/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [OpenRouter API](https://openrouter.ai/docs)
- [BGE Models](https://huggingface.co/BAAI/bge-base-en-v1.5)

---

**Built with ❤️ | Powered by RAG + Hybrid Search + LLMs**

Made for JPMorgan Chase document analysis.
