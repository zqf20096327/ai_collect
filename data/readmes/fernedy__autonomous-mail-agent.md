<div align="center">

[🇬🇧 English](README.md) · [🇪🇸 Español](README.es.md)

</div>

# 📬 Autonomous Mail Agent — Multi-Provider LLM Orchestrator

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Docker Compose](https://img.shields.io/badge/docker-ready-2496ED?logo=docker&logoColor=white)](#deployment-with-docker)
[![Architecture](https://img.shields.io/badge/architecture-event--driven-orange)](#system-architecture)
[![LLM Routing](https://img.shields.io/badge/routing-ZenMux%20%7C%20OpenRouter-8A2BE2)](#intelligent-llm-routing-gateway)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A distributed, autonomous backend system designed for large-scale extraction, classification, semantic reasoning and automated replies on corporate email.

Built on an event-driven, decoupled architecture with **Redis** queues, native **Microsoft Graph API** integration, built-in observability (**Prometheus + Grafana**) and intelligent LLM routing with automatic failover.

---

## 🏛️ System Architecture

Processing is decoupled into three independent layers synced by workers:

```
                  ┌──────────────────────┐
                  │  Microsoft Graph API │
                  └──────────┬───────────┘
                             │
                      [Vision Worker] (Ingestion & Extraction)
                             │
                       (Redis Queue)
                             │
                      [Brain Worker]  ◄──► [LLM Router Gateway]
                             │             (ZenMux / OpenRouter / Local)
                       (Redis Queue)
                             │
                     [Notifier Worker]
                             │
                  ┌──────────┴───────────┐
                  │  SMTP / Webhooks / MS │
                  └──────────────────────┘
```

1. **Ingestion & Extraction (`vision_worker`):** Monitors mailboxes via Graph API, extracts senders and metadata, and normalizes message bodies.
2. **Cognitive Routing (`brain_worker`):** Implements the LLM gateway (`llm_router_gateway.py`), dynamically selecting the optimal provider based on cost, latency and availability.
3. **Dispatch & Action (`notifier_worker`):** Executes autonomous actions: drafting contextual replies, triaging incidents and emitting operational alerts.
4. **Observability:** Operational metrics exported to Prometheus, with pre-provisioned Grafana dashboards (`config/grafana/`).

---

## ⚡ Intelligent LLM Routing (Gateway)

The cognitive module integrates active redundancy:
* **Transparent failover:** Automatic transition between ZenMux, OpenRouter and direct providers when SLAs degrade or quotas are exceeded.
* **Model evaluation:** Built-in benchmarking suite (`benchmark_provider.py`, `benchmark_all_providers.py`) to measure latency drift and cost per token.
* **Memory & Profiles:** `auto_learning.py` module with persistent semantic profiles.

---

## 📂 Repository Structure

```text
.
├── config/              # Grafana dashboards and semantic profiles
├── docker/              # Optimized Dockerfiles for workers
├── docs/                # Extended documentation and technical diagrams
│   └── assets/          # Architecture diagrams
├── src/
│   ├── brain/           # Cognitive workers and LLM Router Gateway
│   ├── graph/           # Microsoft Graph API clients and OAuth2
│   ├── notifier/        # Notification and reply dispatcher
│   ├── observability/   # Tracing and metrics exporter
│   ├── shared/          # Redis clients and cross-cutting utilities
│   └── vision/          # Email processing and ingestion
├── test/                # Unit and integration test suite
├── docker-compose.yml   # Multi-container orchestration of the platform
└── requirements.txt     # Backend service dependencies
```

---

## 🚀 Quickstart

### Prerequisites
* Python 3.11+
* Docker and Docker Compose
* Redis 7+ instance (included in the compose file)

### Environment variables

```bash
cp .env.example .env
```

Edit the `.env` file with your Microsoft Entra ID (Graph API) credentials, LLM provider API keys and Redis configuration.

### Deployment with Docker

```bash
docker compose up -d --build
```

### Running Tests and Benchmarks

```bash
# Run the unit test suite
pytest test/ -v

# Run a latency/token benchmark against the configured providers
python benchmark_provider.py
```

---

## 📊 Metrics and Monitoring

Once the infrastructure is up:
* **Grafana:** `http://localhost:3000` (dashboards auto-loaded from `config/grafana/provisioning/`)
* **Prometheus Metrics:** port exposed according to the `.env` configuration

---

## 👤 Author

**Fernedy Arias** — AI First · Tech Explorer

Building autonomous AI agents and AI-powered systems that do real work.

- 📫 fernedy.arias@gmail.com
- 🌐 [specnimbus.com](https://specnimbus.com)
- ✨ Audit your own repos with [repo-glow](https://github.com/fernedy/repo-glow) — Glow Score 0–100, zero dependencies.
