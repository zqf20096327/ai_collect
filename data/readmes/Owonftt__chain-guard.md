# 🛡️ ChainGuard

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green.svg)](https://fastapi.tiangolo.com/)
[![Powered by MiMo](https://img.shields.io/badge/Powered%20by-Xiaomi%20MiMo-orange.svg)](https://github.com/XiaomiMiMo)
[![100T Orbit](https://img.shields.io/badge/100T--Orbit-participant-purple.svg)](#)
[![Multi-Agent](https://img.shields.io/badge/AI-Multi--Agent-red.svg)](#)

> **AI-powered smart contract security auditing platform** — multi-agent vulnerability scanning, risk scoring, gas optimization, and audit reporting powered by **Xiaomi MiMo**.

ChainGuard deploys four specialised AI agents that work in parallel to deliver comprehensive security audits for Solidity and Vyper smart contracts. Each agent leverages the Xiaomi MiMo LLM for deep semantic analysis, with deterministic fallback heuristics when no API key is configured.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        ChainGuard Frontend                       │
│                   Dark-themed Audit Dashboard                    │
│        Contract Input · Agent Status · Results Display          │
└──────────────────────────┬──────────────────────────────────────┘
                           │ REST API
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                     ChainGuard FastAPI Backend                   │
│  POST /audit/contract  ──┐                                      │
│  POST /scan/vulns       │  ┌──────────────────────────────┐     │
│  POST /score/risk       ├──▶│   Async Orchestrator         │     │
│  POST /analyze/gas      │  │   (concurrent agent dispatch) │     │
│  GET  /agents/status    │  └─────────┬────────────────────┘     │
│                           │            │                          │
│                           │   ┌────────┼────────┬──────────┐     │
│                           │   ▼        ▼        ▼          ▼     │
│                           │ ┌──────┐┌──────┐┌──────┐┌─────────┐ │
│                           │ │ Vuln ││Audit ││ Risk ││  Gas    │ │
│                           │ │Scan- ││Repor-││Score-││ Analyst │ │
│                           │ │ner   ││ter   ││r     ││         │ │
│                           │ └──┬───┘└──┬───┘└──┬───┘└────┬────┘ │
│                           │    │       │       │         │      │
│                           │    └───────┴───┬───┴─────────┘      │
│                           │                ▼                     │
│                           │     ┌────────────────────┐          │
│                           │     │   Xiaomi MiMo LLM  │          │
│                           │     │   (or heuristic     │          │
│                           │     │    fallback)        │          │
│                           │     └────────────────────┘          │
└─────────────────────────────────────────────────────────────────┘
```

---

## ✨ Features

### 🔍 Vulnerability Scanner Agent
- Reentrancy detection (CWE-841 / SWC-107)
- Integer overflow/underflow (CWE-190 / SWC-101)
- Unchecked external calls (CWE-252 / SWC-104)
- Access control & authorisation flaws
- Delegatecall injection (SWC-112)
- tx.origin authentication (SWC-115)
- Timestamp dependence (SWC-116)
- Oracle manipulation vectors
- Flash loan attack surfaces
- Signature replay (SWC-121)
- ERC-20/ERC-721 compliance issues

### 📊 Risk Scorer Agent
- Weighted multi-category risk assessment
- Categories: reentrancy, access control, arithmetic safety, external interactions, logic/design, DeFi risk, compliance
- 0–100 overall risk score with risk level classification
- Detailed per-category explanations

### ⛽ Gas Analyst Agent
- Storage vs memory optimisation
- Struct packing analysis
- Unchecked arithmetic opportunities
- Calldata vs memory parameters
- Custom error recommendations
- Loop optimisation (caching, unchecked increments)
- Storage variable caching
- Estimated gas savings per optimisation

### 📝 Audit Reporter Agent
- Synthesises all agent results into executive summary
- Prioritised recommendations
- Cross-references vulnerability IDs
- Professional audit-grade output

### 🎨 Dashboard
- Dark-themed responsive design
- Real-time agent status cards with capability tags
- Contract code editor with language/chain selectors
- Severity colour-coded vulnerability cards
- Risk gauge with category breakdown
- Gas optimisation cards with before/after code snippets
- Tabbed results navigation

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Python 3.10+, FastAPI, Pydantic v2 |
| **LLM** | Xiaomi MiMo (7B-RL) via OpenAI-compatible API |
| **HTTP Client** | httpx (async) |
| **Frontend** | Vanilla HTML/CSS/JS (no build step) |
| **Deployment** | Uvicorn, Netlify (frontend), any cloud (backend) |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- (Optional) Xiaomi MiMo API key for LLM-powered analysis

### 1. Clone the repository

```bash
git clone https://github.com/Owonftt/chain-guard.git
cd chain-guard
```

### 2. Set up the backend

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure environment

```bash
cp .env.example .env
# Edit .env and add your MIMO_API_KEY
```

> **Note:** ChainGuard works without an API key using built-in heuristic analysis. Add a MiMo API key for full LLM-powered deep analysis.

### 4. Start the server

```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 5. Open the dashboard

Open `frontend/index.html` in your browser, or serve it:

```bash
cd ../frontend
python -m http.server 3000
```

Visit `http://localhost:3000` and set the API URL to `http://localhost:8000`.

---

## 📡 API Reference

### Base URL
```
http://localhost:8000
```

### Endpoints

#### `GET /` — Service info
```json
{
  "service": "ChainGuard API",
  "version": "1.0.0",
  "status": "operational",
  "agents": 4
}
```

#### `GET /agents/status` — Agent status
Returns status, model, and capabilities for all agents.

#### `POST /audit/contract` — Full audit (all agents)
**Request body:**
```json
{
  "code": "pragma solidity ^0.8.20; ...",
  "language": "solidity",
  "name": "TokenVault",
  "chain": "ethereum"
}
```
**Response:** Unified `AuditResult` with vulnerabilities, risk score, gas analysis, summary, and recommendations.

#### `POST /scan/vulnerabilities` — Vulnerability scan only
Same request body. Returns `VulnerabilityReport`.

#### `POST /score/risk` — Risk score only
Same request body. Returns `RiskScoreResult`.

#### `POST /analyze/gas` — Gas analysis only
Same request body. Returns `GasAnalysisResult`.

### Response Schemas

All responses use Pydantic v2 models with full JSON serialization. See `backend/app/models/schemas.py` for the complete schema definitions.

---

## 📁 Project Structure

```
chain-guard/
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   │   ├── __init__.py
│   │   │   ├── vulnerability_scanner.py   # Vuln detection agent
│   │   │   ├── audit_reporter.py          # Report synthesis agent
│   │   │   ├── risk_scorer.py             # Risk assessment agent
│   │   │   └── gas_analyst.py             # Gas optimisation agent
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── schemas.py                 # Pydantic models
│   │   ├── __init__.py
│   │   └── main.py                        # FastAPI application
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── css/style.css
│   ├── js/app.js
│   └── index.html
├── proof/
│   ├── README.md
│   ├── architecture.md
│   └── token_consumption_estimate.md
├── README.md
├── LICENSE
├── .gitignore
└── netlify.toml
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- [Xiaomi MiMo](https://github.com/XiaomiMiMo) — LLM backbone
- [FastAPI](https://fastapi.tiangolo.com/) — Backend framework
- [OpenZeppelin](https://www.openzeppelin.com/) — Security patterns reference
- [SWC Registry](https://swcregistry.io/) — Smart contract weakness classification

---

**Topics:** `100t-orbit` `ai-agents` `smart-contract-security` `audit` `fastapi` `llm` `mimo` `multi-agent` `vulnerability-scanning` `xiaomi-mimo`
