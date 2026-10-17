# LLM Gateway Core

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=Prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=Grafana&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)

LLM Gateway Core is a production-grade infrastructure component designed to abstract multiple Large Language Model (LLM) providers behind a single, unified API. It implements intelligent routing, distributed caching, atomic rate limiting, and comprehensive observability to provide reliable and cost-effective LLM access.

## System Architecture

The gateway is built on a high-performance FastAPI backend, utilizing a provider-agnostic interface that allows for seamless integration of both cloud-based and local model providers.

### Core Components

*   **API Layer**: FastAPI-based REST API providing standardized chat completion endpoints.
*   **Provider Router**: Dynamically selects the optimal model provider based on request hints (online, local, fast, secure).
*   **Redis Integration**: 
    *   **Distributed Cache**: Persistently stores provider responses to reduce latency and API costs.
    *   **Rate Limiter**: Implements a token bucket algorithm via Redis Lua scripts for atomic, distributed request throttling.
*   **Monitoring Stack**: Full observability with Prometheus for metrics collection and Grafana for visualization.
*   **Streamlit Frontend**: A clean, responsive interface for demonstration and testing purposes.

## Integrated Providers

The gateway currently supports the following providers:

*   **Google Gemini**: High-performance cloud integration for 'online' and 'fast' request modes.
*   **Ollama**: Local integration for 'local' and 'secure' request modes, enabling private, on-premise inference.

## User Interface

The Streamlit frontend provides a simplified interface for interacting with the gateway, allowing users to select the execution mode and submit queries.

### Gemini Integration (Online Mode)
![Gemini Interface](docs/assets/gemini_interface.png)

### Ollama Integration (Local Mode)
![Ollama Interface](docs/assets/ollama_interface.png)

## Monitoring and Observability

The system exports detailed metrics to Prometheus, allowing for real-time monitoring of request rates, provider latency, cache performance, and rate limiting status.

### Performance Dashboard
![Grafana Monitoring](docs/assets/grafana_monitoring.png)

## Operational Reliability

### Distributed Rate Limiting
The gateway ensures system stability by enforcing per-client rate limits. Requests exceeding the defined threshold are rejected with a standard 429 status code.

![Rate Limiting Test](docs/assets/rate_limiting_test.png)

## Getting Started

### Prerequisites

*   Docker and Docker Compose
*   Google Gemini API Key (for online providers)
*   Local Ollama instance (for local providers)

### Configuration

System configuration is managed via environment variables in a `.env` file:

```env
PROVIDER_TIMEOUT_SECONDS=60
PROVIDER_MAX_RETRIES=3
GEMINI_API_KEY=your_api_key_here
REDIS_URL=redis://redis:6379/0
OLLAMA_BASE_URL=http://host.docker.internal:11434
API_KEYS=sk-gateway-123
```

### Deployment

Deploy the entire stack using Docker Compose:

```bash
docker-compose up -d --build
```

The services will be available at:
*   Streamlit Frontend: http://localhost:8501
*   Gateway API: http://localhost:8000
*   Grafana Dashboard: http://localhost:3000
