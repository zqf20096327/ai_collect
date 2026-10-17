# SecureAI Enterprise — Intelligent Cyber Security, AI/ML DLP & Threat Deception Platform

[![Python Version](https://img.shields.io/badge/python-3.10%20%7C%203.11-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-ML%20Engine-F7931E.svg?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Tests](https://img.shields.io/badge/pytest-Passing-brightgreen.svg?logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![Security](https://img.shields.io/badge/Zero--Trust-AES--256%20%2B%20Honeytokens-purple.svg)](https://en.wikipedia.org/wiki/Zero_trust_security_model)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

**SecureAI Enterprise** is a production-grade, AI/ML-driven Data Loss Prevention (DLP), Ransomware Threat Detection, and Honeytrap Deception platform engineered for enterprise backup, disaster recovery, and SIEM security operations.

Built with **Zero-Trust Cybersecurity** principles and modern **AI/ML Tech Stacks**, SecureAI continuously inspects, tokenizes, isolates, encrypts, and audits critical corporate data against modern adversary threat vectors.

---

## 🌟 Key Pillars & AI/ML Architecture

### 1. Multi-Layer AI/ML DLP (Data Loss Prevention) Engine
* **Algorithmic Validation**: Luhn Algorithm verification for payment cards, combined with high-precision Regex tokenizers for:
  - **India PII**: Aadhaar (`\d{4}\s\d{4}\s\d{4}`), PAN Card (`[A-Z]{5}[0-9]{4}[A-Z]`), Passport.
  - **Financial Data**: Credit Cards (Luhn validated), Bank Account numbers, IFSC Codes, CVV numbers.
  - **Cloud Secrets & Credentials**: AWS Access Keys (`AKIA...`), JWT Tokens, Private RSA/SSH Keys (`-----BEGIN RSA PRIVATE KEY-----`), Passwords & Database Connection Strings.
  - **Global PII**: US Social Security Numbers (SSN), Email Addresses, International Phone Numbers.
* **Context Classifier**: TF-IDF N-Gram Vectorizer + Scikit-Learn Logistic Regression (`data/models/context_model.joblib`) predicting whether surrounding textual context is financial, credential, confidential, or benign.
* **Semantic Embeddings**: Cosine similarity embedding analysis via `SentenceTransformers` (`all-MiniLM-L6-v2`) for semantic intent matching.

### 2. Shannon Entropy & Ransomware ML Classifier
* **Shannon Entropy Engine**: Calculates byte entropy $H = -\sum_{i=1}^{n} p_i \log_2 p_i$ per file (0.0 to 8.0 bits/byte). Files with entropy $> 7.5$ are flagged for potential ransomware payload or unauthorized pre-encryption.
* **Random Forest ML Classifier**: 100-estimator Random Forest (`data/models/ransomware_model.joblib`) trained on 5 structural features:
  $$\vec{X} = [\text{Entropy}, \text{Byte Variance}, \text{Non-ASCII Ratio}, \text{Compression Ratio}, \text{Extension Risk Flag}]$$
* **Automated Batch Isolation**: Batches containing ransomware extension anomalies (`.locked`, `.crypto`, `.wcry`, `.blackmatter`) or high anomaly ratios are automatically diverted into `data/quarantine/` instead of corrupting clean backups.

### 3. Honeytrap & Deception Cyber Engine 🐝
* **Decoy Asset Seeding**: Automatically injects decoy files (`_HONEYTRAP_DO_NOT_OPEN_PASSWORDS.env`, `_DECOY_EXECUTIVE_SALARY.csv`) embedded with unique canary tripwire tokens (`<HONEYTOKEN_CANARY_v1:...>`).
* **Real-Time Forensic Tripwire**: Unauthorized reading, restoring, or tampering with decoy assets instantly generates a **CRITICAL Forensic Incident Alert** logged to telemetry.

### 4. Enterprise Glassmorphism Dashboard & SIEM Exporter
* **Real-time Glassmorphism SPA**: Built with HTML5, CSS3 Variables, Vanilla JS, and Chart.js. Features dynamic Security Health Score gauge (0–100), interactive Drag-and-Drop file threat inspector, Backup Catalog, and Honeypot Console.
* **SIEM Telemetry Exporter**: Streams security events in standard JSON and **CEF (Common Event Format)** for direct ingestion into Splunk, Elastic, and IBM QRadar.

---

## 🛡️ Threat Model & Defensive Matrix

| Attack Vector / Threat | Adversary Objective | SecureAI Defensive Countermeasure |
| :--- | :--- | :--- |
| **Data Exfiltration / Insider Leak** | Steal PII, bank details, passwords, or AWS keys from backups | **Multi-Layer DLP + Token Redaction + AES-256 Fernet Encryption** auto-encrypts sensitive tokens and high-risk files. |
| **Ransomware Encryption Attack** | Encrypt corporate files (`.locked`, `.crypto`) and pollute backup stores | **Shannon Entropy Engine + Random Forest ML Classifier** detects high-entropy anomalies and auto-quarantines infected batches into `data/quarantine/`. |
| **Adversary Reconnaissance** | Enumerate backup directory looking for administrator credentials | **Honeytrap Deception System** seeds canary decoys; opening or restoring canary files triggers instant CRITICAL SIEM tripwire alerts. |
| **Tampering with Backup Integrity** | Inject rogue payloads into restored datasets | **Cryptographic Decryption Validation & Signature Checks** ensure only authorized keys can decrypt and restore clean backups. |

---

## 📊 Model Evaluation & Benchmarks

Both AI/ML models are evaluated using stratified 80/20 train/test splits, with performance metrics serialized to `data/models/training_report.json`:

```
============================================================
[PIPELINE] 1. Training DLP Context Intelligence Model...
============================================================
[METRICS] DLP Context Classifier (TF-IDF + Logistic Regression):
  - Accuracy : 100.00%
  - Precision: 100.00%
  - Recall   : 100.00%
  - F1-Score : 100.00%

============================================================
[PIPELINE] 2. Training Ransomware Threat Detection Classifier...
============================================================
[METRICS] Ransomware Classifier (Random Forest, n_estimators=100):
  - Accuracy : 100.00%
  - Precision: 100.00%
  - Recall   : 100.00%
  - F1-Score : 100.00%
```

---

## 🏗️ System Architecture

```
                                  ┌───────────────────────────────┐
                                  │      SecureAI Dashboard       │
                                  │ (HTML5 / Glassmorphism / SPA) │
                                  └──────────────┬────────────────┘
                                                 │
                                                 ▼
                                  ┌───────────────────────────────┐
                                  │    FastAPI Application Server │
                                  │ (Pydantic Schemas / Logging)  │
                                  └──────────────┬────────────────┘
                                                 │
                   ┌──────────────────────────────┼──────────────────────────────┐
                   ▼                              ▼                              ▼
     ┌───────────────────────────┐  ┌───────────────────────────┐  ┌───────────────────────────┐
     │     AI/ML DLP Engine      │  │    Ransomware Detector    │  │ Deception & Honeypot Sys  │
     │  - Regex & Luhn Check     │  │  - Shannon Entropy calc   │  │  - Canary File Seeding    │
     │  - TF-IDF + Logistic Reg  │  │  - Random Forest ML Model │  │  - Real-time Tripwire Log │
     │  - AES-256 / Fernet Enc   │  │  - Auto-Quarantine Engine │  │  - SIEM Log Stream (CEF)  │
     └───────────────────────────┘  └───────────────────────────┘  └───────────────────────────┘
```

---

## 📁 Repository Structure

```
SecureAI-Backup/
├── app/
│   ├── main.py                  # FastAPI server entry point, middleware & logging
│   ├── config.py                # Centralized configuration & environment settings
│   ├── schemas.py               # Pydantic v2 validation models & request/response types
│   ├── requirements.txt         # Production dependencies
│   ├── routes/
│   │   ├── __init__.py          # Routes package initializer
│   │   └── backup_routes.py     # Backup, restore, upload scan, analytics API routes
│   └── utils/
│       ├── __init__.py          # Utils package initializer
│       ├── analytics.py         # Security Health Score algorithm & SIEM exporter
│       ├── crypto_utils.py      # AES-256 Fernet string & whole-file encryption
│       ├── dlp.py               # Multi-layer DLP detection engine & TF-IDF model loader
│       ├── honeypot.py          # Canary trap generator & intrusion alert logger
│       └── ransomware_detector.py # Entropy calculator & Random Forest ML model
├── data/
│   ├── backups/                 # Encrypted backup archives & metadata.json
│   ├── models/                  # Serialized ML models (.joblib) & training_report.json
│   ├── quarantine/              # Quarantined ransomware batches
│   └── honeypot_logs.json       # Audit trail of intrusion events
├── templates/
│   ├── index.html               # Enterprise Dynamic Glassmorphism Dashboard
│   ├── backup.html              # Legacy backup UI
│   └── scan.html                # Legacy scan UI
├── testing_folder/              # Test suite with DLP, ransomware, & canary files
├── tests/                       # Automated Pytest Suite
│   ├── __init__.py
│   ├── conftest.py              # Shared fixtures & test client
│   ├── test_dlp.py              # DLP regex, Luhn, context score tests
│   ├── test_ransomware.py       # Shannon entropy & ransomware detection tests
│   ├── test_honeypot.py         # Honeytoken & canary trap tests
│   └── test_api.py              # FastAPI endpoint integration tests
├── Dockerfile                   # Production multi-stage Docker build
├── Makefile                     # Developer automation commands
├── .env.example                 # Environment variables configuration template
├── train_model.py               # AI/ML Training Pipeline script
└── README.md                    # Project documentation
```

---

## ⚡ Quick Start Guide

### 1. Prerequisites & Installation

```bash
# Clone the repository
git clone https://github.com/your-username/SecureAI-Backup.git
cd SecureAI-Backup

# Create virtual environment & install dependencies
python -m venv app/venv
# Windows:
app\venv\Scripts\activate
# Linux/macOS:
source app/venv/bin/activate

pip install -r app/requirements.txt
```

### 2. Train AI/ML Models

```bash
python train_model.py
```

### 3. Launch Application Server

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

Open your browser and navigate to:
👉 **`http://127.0.0.1:8000`** to access the Enterprise Dashboard.
Interactive Swagger API documentation is available at **`http://127.0.0.1:8000/api/docs`**.

---

## 🐳 Docker Deployment

Run SecureAI in a production-hardened, non-root Docker container:

```bash
# Build Docker image
docker build -t secureai-enterprise:latest .

# Run Docker container
docker run -p 8000:8000 --name secureai-app secureai-enterprise:latest
```

---

## 🧪 Automated Testing Suite

Execute the full `pytest` suite covering unit tests and API integration tests:

```bash
pytest tests/ -v --tb=short
```

---

## 📡 Core API Reference

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/health` | Application health check, uptime, and ML model availability status |
| `GET` | `/` | Serves the Enterprise Dynamic Glassmorphism Dashboard UI |
| `POST` | `/scan` | Scans a filesystem path for DLP sensitive data (Pydantic validated) |
| `POST` | `/api/scan-upload` | Drag-and-drop file upload endpoint for instant DLP & Entropy analysis |
| `POST` | `/backup` | Creates a secure backup with auto-encryption & honeypot canary seeding |
| `GET` | `/backups` | Retrieves inventory of all registered active and quarantined backups |
| `GET` | `/backup/{name}` | Retrieves metadata for a specific backup identifier |
| `DELETE` | `/backup/{name}` | Deletes a backup archive and updates metadata catalog |
| `POST` | `/restore` | Restores files from backup, decrypts contents, & checks canary tripwires |
| `GET` | `/api/analytics` | Returns overall Security Health Score & 7-day time series metrics |
| `GET` | `/api/honeypot/logs` | Fetches forensic intrusion logs triggered by decoy canary traps |
| `POST` | `/api/honeypot/trigger-canary` | Triggers a simulated canary breach alert |
| `GET` | `/api/export-siem` | Exports system events in CEF or JSON format for Splunk/Elastic |

---

## 📄 License

Distributed under the Apache 2.0 License.
