# 🤖 BugTrace-Agent

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green?style=for-the-badge&logo=fastapi)
![Google Cloud](https://img.shields.io/badge/Google_Cloud-Run-orange?style=for-the-badge&logo=google-cloud)
![Gemini](https://img.shields.io/badge/Gemini-AI-purple?style=for-the-badge&logo=google)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**An autonomous, serverless AI agent that identifies, fixes, and tests software bugs using Google Gemini Pro and FastAPI**

[Demo](#-demo) • [Features](#-features) • [Quick Start](#-quick-start) • [Documentation](#-documentation) • [Author](#-author)

</div>

> [!NOTE]
> **📢 Repository Restoration & Migration Notice:**  
> My original GitHub account (`@ayushcmd`) was suspended, so I have re-uploaded and restored this complete codebase to my new account: [**@ayushcmdx**](https://github.com/ayushcmdx).
> 
> 🏆 **Achievement & Background:**  
> This project was developed during my 1st year at **IIT Patna** (BS in Computer Science & Data Analytics), where it won **3rd Place** at the **Hack-N-Tech 24-Hour Hackathon**!

---

## 🎯 Overview

**BugTrace-Agent** is an AI-powered debugging agent that automates the entire bug fixing workflow. Instead of developers manually tracing errors through codebases, this system:

1. **Ingests** bug reports via REST API
2. **Searches** the codebase using RAG (Retrieval-Augmented Generation)
3. **Writes** the fix using Google Gemini Pro
4. **Tests** the solution with automated testing
5. **Waits** for human approval before merging (HITL pattern)

### 🏗️ Architecture Highlights

- **Backend**: FastAPI (Python) with comprehensive error handling
- **AI Engine**: Google Gemini Pro via Vertex AI
- **Deployment**: Google Cloud Run (serverless, auto-scaling)
- **Key Patterns**: 
  - Retrieval-Augmented Generation (RAG)
  - Human-in-the-Loop (HITL) for safety
  - Multi-agent workflow orchestration

---

## 📸 Demo

> **Note**: Add your demo screenshot/GIF here for maximum impact!

```bash
# Example API Usage
curl -X POST https://your-service.run.app/start_run \
  -H "Content-Type: application/json" \
  -d '{
    "issue_id": "BUG-123",
    "description": "Login function always returns true regardless of credentials"
  }'
```

**Response:**
```json
{
  "success": true,
  "issue_id": "BUG-123",
  "message": "Agent finished coding. Tests passed. Awaiting HITL approval."
}
```

---

## ✨ Features

### 🔍 **Autonomous Bug Detection**
- RAG-powered codebase search to locate relevant files
- Context-aware analysis using vector embeddings
- Smart file retrieval based on issue description

### 🛠️ **Self-Correcting AI Agent**
- Writes fixes using Google Gemini Pro
- Runs automated tests on generated code
- Self-corrects if tests fail (iterative refinement)

### 🔒 **Human-in-the-Loop Safety**
- **Critical safeguard**: No code merges without approval
- Manual review gate via `/approve` endpoint
- Maintains full audit trail of all changes

### ☁️ **Production-Ready Infrastructure**
- Serverless deployment on Google Cloud Run
- Environment-based configuration (no hardcoded secrets)
- Structured logging for observability
- Comprehensive error handling

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Cloud account with Vertex AI enabled
- Git

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ayushcmdx/BugTrace-Agent.git
cd BugTrace-Agent
```

### 2️⃣ Set Up Environment

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your GCP project ID
nano .env
```

Your `.env` should contain:
```bash
GCP_PROJECT_ID=your-project-id-here
GCP_LOCATION=us-central1
PORT=8080
LOG_LEVEL=INFO
```

### 4️⃣ Run Locally

```bash
# Option 1: Using the provided script (recommended)
python run_local.py

# Option 2: Direct execution
python main.py
```

Visit: **http://localhost:8080**

---

## 📡 API Endpoints

### Health Check
```bash
GET /
```

**Response:**
```json
{
  "status": "online",
  "service": "Bug Hunter AI Agent",
  "version": "1.0.0"
}
```

### Start Bug Hunt (Phase 1 & 2)
```bash
POST /start_run
Content-Type: application/json

{
  "issue_id": "BUG-123",
  "description": "Description of the bug"
}
```

**What it does:**
1. Receives the bug report
2. Searches codebase using RAG
3. Generates fix using Gemini
4. Runs automated tests
5. Returns status (awaiting approval)

### Approve Fix (Phase 3 - HITL)
```bash
POST /approve/{issue_id}
```

**What it does:**
1. Validates the issue is ready
2. Simulates merge to repository
3. Returns confirmation

---

## 🏗️ Project Structure

```
BugTrace-Agent/
├── app/
│   ├── config.py           # Centralized configuration & multi-provider settings
│   ├── main.py             # FastAPI REST API endpoints & lifecycle
│   ├── engine/
│   │   ├── agent.py        # Core AI Agent loop (Gemini API, Vertex AI & Sandbox)
│   │   └── memory.py       # Session history & state management
│   └── tools/
│       ├── rag.py          # Semantic & keyword codebase file retrieval
│       └── runner.py       # Automated pytest verification runner
├── sample_target/          # Real target codebase for agent to detect and fix
│   ├── auth.py             # Buggy authentication target
│   └── test_auth.py        # Automated test suite verifying auth
├── tests/                  # Automated API integration tests
│   └── test_api.py         # Pytest suite for FastAPI endpoints
├── .env.example            # Environment template (Gemini API / Vertex / Demo)
├── requirements.txt        # Python dependencies
├── run_local.py            # Local development launcher
├── Procfile                # Cloud Run deployment config
└── README.md               # Documentation
```

---

## 🔧 Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Backend API** | FastAPI | High-performance REST API |
| **AI Model** | Google Gemini Pro | Bug analysis & code generation |
| **AI Platform** | Vertex AI | Model hosting & orchestration |
| **Deployment** | Google Cloud Run | Serverless container platform |
| **Language** | Python 3.8+ | Core implementation |
| **Testing** | pytest | Automated test execution |
| **Config** | python-dotenv | Environment management |

---

## 🌐 Cloud Deployment

### Deploy to Google Cloud Run

```bash
# 1. Authenticate with GCP
gcloud auth login

# 2. Set your project
gcloud config set project YOUR_PROJECT_ID

# 3. Deploy the service
gcloud run deploy bug-hunter-agent \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GCP_PROJECT_ID=YOUR_PROJECT_ID \
  --set-env-vars GCP_LOCATION=us-central1

# 4. Get the service URL
gcloud run services describe bug-hunter-agent \
  --region us-central1 \
  --format 'value(status.url)'
```

### Environment Variables in Cloud Run

Set these in the Cloud Run console or via CLI:
- `GCP_PROJECT_ID`: Your Google Cloud project ID
- `GCP_LOCATION`: Vertex AI region (default: us-central1)

---

## 🧪 Testing

```bash
# Run automated tests
pytest

# Test the API locally
curl http://localhost:8080

# Test bug report submission
curl -X POST http://localhost:8080/start_run \
  -H "Content-Type: application/json" \
  -d '{
    "issue_id": "TEST-001",
    "description": "Sample bug for testing"
  }'

# Test approval workflow
curl -X POST http://localhost:8080/approve/TEST-001
```

---

## 🛡️ Security Best Practices

This project implements several security measures:

✅ **No Hardcoded Credentials** - All secrets via environment variables  
✅ **Input Validation** - Comprehensive request validation with Pydantic  
✅ **Error Handling** - Graceful degradation, no sensitive data in errors  
✅ **HITL Pattern** - Mandatory human approval before code changes  
✅ **Structured Logging** - Full audit trail of all operations  

### Important Security Notes

- ⚠️ **Never commit `.env` files** - Contains sensitive credentials
- ⚠️ **Rotate credentials regularly** - GCP service account keys
- ⚠️ **Enable authentication** - For production deployments
- ⚠️ **Monitor logs** - Watch for suspicious activity

See [SECURITY_SETUP.md](SECURITY_SETUP.md) for detailed security configuration.

---

## 📚 Documentation

- **[ACTION_PLAN.md](ACTION_PLAN.md)** - Step-by-step setup guide
- **[SECURITY_SETUP.md](SECURITY_SETUP.md)** - Security & deployment docs
- **[BEFORE_AFTER.md](BEFORE_AFTER.md)** - Code improvements comparison

---

## 🎯 How It Works

### Phase 1: RAG-Based Search
```python
# Agent receives bug report
bug_report = "Login function always returns true"

# Searches codebase using vector embeddings
relevant_files = retrieve_relevant_files(bug_report)
# Returns: {"file": "auth.py", "content": "..."}
```

### Phase 2: AI-Powered Fix
```python
# Gemini analyzes the code
# Generates a fix
# Runs automated tests
# Iterates if tests fail
```

### Phase 3: Human Approval (HITL)
```python
# Agent pauses and waits
# Human reviews the fix
# Approval via POST /approve/{issue_id}
# Only then does merge proceed
```

---

## 🚧 Roadmap

Future enhancements planned:

- [ ] **Real RAG Implementation** - Integrate Vertex AI Vector Search
- [ ] **Multi-Repository Support** - Connect to GitHub/GitLab APIs
- [ ] **WebSocket Updates** - Real-time progress notifications
- [ ] **Authentication** - API key / OAuth integration
- [ ] **Metrics Dashboard** - Success rate, response time tracking
- [ ] **CI/CD Pipeline** - Automated testing & deployment
- [ ] **Database Integration** - Persistent state storage (Redis/PostgreSQL)

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

Please ensure:
- Code follows PEP 8 style guide
- All tests pass
- New features include tests
- Documentation is updated

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Ayush Raj**

- 🎓 **Education**: Indian Institute of Technology (IIT) Patna — BS in Computer Science & Data Analytics
- 🏆 **Achievement**: 3rd Place Winner, *Hack-N-Tech* 24-Hour Hackathon (1st Year Project)
- 🐙 **GitHub**: [@ayushcmdx](https://github.com/ayushcmdx) *(formerly [@ayushcmd](https://github.com/ayushcmd))*

---

## 🙏 Acknowledgments

- **Google Gemini** - Powerful AI model for code generation
- **Vertex AI** - Scalable AI platform
- **FastAPI** - Modern, fast Python web framework
- **The AI/ML Community** - For inspiration and best practices

---

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/ayushcmdx/BugTrace-Agent?style=social)
![GitHub forks](https://img.shields.io/github/forks/ayushcmdx/BugTrace-Agent?style=social)
![GitHub issues](https://img.shields.io/github/issues/ayushcmdx/BugTrace-Agent)
![GitHub last commit](https://img.shields.io/github/last-commit/ayushcmdx/BugTrace-Agent)

---

<div align="center">

**If you found this project helpful, please consider giving it a ⭐!**

Made with ❤️ by Ayush Raj (IIT Patna)

</div>
