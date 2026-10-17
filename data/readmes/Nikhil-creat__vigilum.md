# VIGILUM — Autonomous Cognitive Defense Grid

![status](https://img.shields.io/badge/status-prototype-yellow)
![license](https://img.shields.io/badge/license-MIT-blue)
![made with](https://img.shields.io/badge/made%20with-Agentic%20AI%20%2B%20RAG%20%2B%20CNN-8B6BFF)

An autonomous cognitive defense platform concept that fuses **agentic AI, retrieval-augmented generation (RAG), computer vision (CNN), predictive modeling, post-quantum cryptography, and zero-trust design** into one self-operating security intelligence system.

**Live demo:** `https://<your-username>.github.io/vigilum/` (deploy steps below)

**DESIGNED AND DEVELOPED BY**
# **NIKHIL CHARY SRIRAMOJU**
BTech CSE (Final Year)

- GitHub: [Nikhil-creat](https://github.com/Nikhil-creat)
- LinkedIn: [nikhil-chary-sriramoju](https://in.linkedin.com/in/nikhil-chary-sriramoju-95041b38a)
- Email: sriramojunikhil66@gmail.com
- Instagram: [@nikhil__sriramoju](https://www.instagram.com/nikhil__sriramoju)
- Facebook: [Profile](https://www.facebook.com/profile.php?id=100079201124141)

---

## Table of contents
- [Project status](#project-status)
- [Problem statement](#problem-statement)
- [Architecture](#architecture)
- [Modules](#modules)
- [Tech stack](#tech-stack)
- [Repository structure](#repository-structure)
- [Run locally](#run-locally)
- [Deploy on GitHub Pages](#deploy-on-github-pages)
- [Roadmap](#roadmap)
- [Author](#author)
- [License](#license)

---

## Project status

This repository currently contains the **design and architecture layer**: a fully worked-out system specification, interface, and interaction model for VIGILUM, presented as a single-page showcase (`index.html`).

A working prototype of one module — a CNN-based phishing/malware-screenshot classifier — is in progress under `/prototype` (see [Roadmap](#roadmap)). This section will be updated as the prototype is added, so evaluators can distinguish the finished design layer from the implemented code layer.

## Problem statement

Security operations centers (SOCs) drown analysts in alerts that require manual triage across disconnected tools — SIEM, threat intel feeds, image forensics, and compliance logs. VIGILUM's premise is a single reasoning layer that ingests all of these signal types, cross-checks them against retrieved context, and closes the loop with an auditable autonomous response — cutting the time between "signal received" and "threat neutralized."

## Architecture

![VIGILUM architecture](docs/architecture.svg)

Every event — a log line, a packet, a screenshot, a document — moves through the same five stages: **Ingest → Understand → Reason → Act → Explain**. See `index.html` for the full interactive breakdown of each stage.

## Modules

16 planned modules, grouped by function:

| Group | Modules |
|---|---|
| Detection | Agentic SOC swarm · CNN deep-signal defense · Neuromorphic threat sensing · Deepfake/voice-clone interceptor |
| Intelligence | RAG threat knowledge brain · Predictive threat modeling · Explainable AI shield |
| Resilience | Federated learning mesh · Adversarial robustness core · Quantum-resilient crypto core |
| Response | Digital twin simulator · Autonomous red-team twin · Zero-trust agent gateway |
| Oversight | Immutable blockchain audit ledger · Cognitive analytics cockpit · AR/VR command room |

Full descriptions of each module are in `index.html`.

## Tech stack

| Layer | Tools |
|---|---|
| LLM / Agents | Llama-3 / Mistral (self-hosted), LangGraph, CrewAI |
| RAG | LangChain, pgvector, Qdrant, Cohere/bge rerankers |
| CNN / Deep learning | PyTorch, EfficientNet, 1D-CNN, YOLO |
| Data pipeline | Kafka, Spark, Airflow, dbt |
| Analytics | Pandas, XGBoost, Prophet, Evidently |
| Security | Wazuh/Suricata, OWASP, SPIFFE zero-trust, Vault |
| Infrastructure | Kubernetes, Docker, MLflow, DVC, Terraform |
| Frontend | React + Tailwind, Streamlit, WebSocket |
| Post-quantum crypto | Kyber, Dilithium, liboqs |
| Immutable ledger | Hyperledger Fabric |

## Repository structure

```
vigilum/
├── index.html          # full interactive showcase (architecture, modules, roadmap, credentials)
├── docs/
│   └── architecture.svg # standalone architecture diagram used in this README
├── README.md
└── LICENSE
```

## Run locally

No build step or dependencies — it's a single static file.

```bash
git clone https://github.com/<your-username>/vigilum.git
cd vigilum
# just open index.html in a browser, or serve it:
python3 -m http.server 8000
```

Then visit `http://localhost:8000`.

## Deploy on GitHub Pages

1. Push this repository to GitHub (see commands below if using Termux/CLI).
2. Go to **Settings → Pages** on the repository.
3. Under **Source**, choose **Deploy from a branch** → branch `main`, folder `/ (root)` → **Save**.
4. Wait 1–2 minutes, then refresh the Pages settings tab for the live link:
   `https://<your-username>.github.io/<repo-name>/`

```bash
git init
git add .
git commit -m "Initial commit: VIGILUM showcase"
git branch -M main
git remote add origin https://github.com/<your-username>/vigilum.git
git push -u origin main
```

## Roadmap

| Phase | Duration | Deliverable |
|---|---|---|
| P1 — Foundation | Weeks 1–4 | Data pipelines, feature store, RAG MVP |
| P2 — Intelligence | Weeks 5–9 | CNN models, agent swarm v1, explainability layer |
| P3 — Autonomy | Weeks 10–13 | Auto-response, digital twin, federated learning |
| P4 — Command Center | Weeks 14–16 | Cognitive dashboards, deployment, penetration testing |


## License

MIT — see [LICENSE](LICENSE).
