# 🔍 RAG-Based Policy Agent  
### Enterprise-Grade Policy Intelligence Platform Powered by Retrieval-Augmented Generation (RAG)

Transform fragmented regulatory PDFs into a **searchable, intelligent, context-grounded policy assistant** using semantic embeddings, FAISS retrieval, and Google Gemini reasoning.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Flask-API-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/FAISS-Retrieval-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Gemini-LLM-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/RAG-Framework-black?style=for-the-badge">
</p>

---

# 📘 Overview

**RAG-Based Policy Agent** is a production-ready platform that converts PDF-based policies, compliance rules, and regulatory frameworks into a **real-time policy intelligence engine**.

It enables policy teams to instantly search, retrieve, and reason over internal documents — with **grounded, traceable, and compliant answers** powered by RAG.

Designed for:

- 🛡 Compliance & Audit  
- ⚖ Legal & Governance  
- 🏢 Corporate Policy Teams  
- 🔍 Internal Risk & Regulatory Operations  

---

# 🧠 Why This Product Matters

Organizations face challenges with:

- Thousands of pages of policy documents  
- Manual search through static PDFs  
- Slow compliance decision-making  
- Risk of misinterpretation or oversight  

**This platform provides:**

✓ Real-time policy intelligence  
✓ Explainable, context-grounded LLM answers  
✓ High-precision document extraction  
✓ Enterprise-level consistency & reliability  

---

# 🗂 Project Structure

```
srujanrana07-rag-based-policy-agent/
│
├── README.md                 
├── LICENSE
│
├── app.py                    # Flask REST API server
├── main.py                   # Core RAG workflow runner
├── deploy.sh                 # Deployment script
│
├── document_loader.py        # PDF/table loader & preprocessing
├── vectorizer.py             # Sentence Transformer embeddings
├── retriever.py              # FAISS vector store operations
├── gpt_client.py             # Gemini LLM wrapper
├── submitter.py              # Batch inference + evaluation
│
├── answers_output.json       # Output results
├── questions.json            # Test questions dataset
├── temp.json                 # Intermediate processing store
│
├── requirements.txt
└── log.txt
```

---

# 🏗 System Architecture

<p align="center">
  <img width="3054" height="518" alt="diagram" src="https://github.com/user-attachments/assets/305712c6-880c-4bcc-b168-1a34437c8876" />
  <img width="2688" height="2728" alt="diagram - Copy" src="https://github.com/user-attachments/assets/f1e711dc-7b56-4543-80cc-4e3427295b36" />
</p>

---

# 🚀 Key Features

### 1️⃣ Intelligent PDF Ingestion
- High-fidelity extraction via GhostScript  
- Accurate table detection through Camelot-py  
- Clean preprocessing for long-form policies  

### 2️⃣ Embedding & Vectorization
- Sentence Transformer embeddings  
- Chunking + semantic scoring  
- Stored and indexed for fast retrieval  

### 3️⃣ FAISS-Powered Semantic Search
- Millisecond-level semantic retrieval  
- Top-k contextual selection  
- Deterministic policies for safe RAG  

### 4️⃣ Context-Grounded LLM Reasoning
- Gemini LLM integrated through `gpt_client.py`  
- Strict grounding in FAISS-retrieved context  
- No hallucinations → verified policy answers  

### 5️⃣ Modular, Production-Ready REST API
- Upload documents  
- Extract structured content  
- Ask policy questions  
- Plug into dashboards, portals, BI tools  

---

# ⚙ Installation

### Clone Repository
```bash
git clone https://github.com/srujanrana07/rag-based-policy-agent
cd rag-based-policy-agent
```

### Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
# Windows: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Configure Environment
Create a `.env`:
```
GEMINI_API_KEY=your_api_key
```

---

# ▶ Usage

### Start API Server
```bash
python app.py
```

### Run End-to-End RAG Pipeline
```bash
python main.py
```

### Run Batch Q&A Evaluation
```bash
python submitter.py
```

---

# 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| **POST** | `/upload` | Upload a policy PDF |
| **GET** | `/extract` | Extract text + tables |
| **POST** | `/query` | Ask a question using RAG |

---

# 🔐 Security & Reliability

- Sanitized PDF ingestion  
- Deterministic FAISS retrieval  
- Strictly grounded LLM answers  
- Full logging in `log.txt`  
- Cloud-ready and container-friendly  

---

# 🐳 Deployment

### Docker
```bash
docker build -t rag-policy-agent .
docker run -p 5000:5000 rag-policy-agent
```

### Linux (Auto Setup)
```bash
./deploy.sh
```

Supports deployment on:

- AWS (ECS, EC2, Lambda)  
- GCP (Cloud Run)  
- Azure App Service  
- Railway / Render  

---

# 🤝 Contributing
Pull requests and improvements are welcome.

---

# 📄 License
MIT License — free for personal and commercial use.
