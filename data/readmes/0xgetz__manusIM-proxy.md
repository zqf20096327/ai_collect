# 🤖 manusIM-proxy

<div align="center">

**A lightweight OpenAI-compatible bridge for the Manus IM agent.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![GitHub stars](https://img.shields.io/github/stars/0xgetz/manusIM-proxy?style=social)](https://github.com/0xgetz/manusIM-proxy/stargazers)

[English](README.md) • [中文](README.zh.md) • [日本語](README.ja.md) • [Español](README.es.md) • [Français](README.fr.md)

---

![Manus IM Proxy Demo](assets/demo.gif)

</div>

`manusIM-proxy` is a high-performance HTTP bridge that translates OpenAI-style chat completion requests into **Manus v2 API** operations. It seamlessly converts Manus task events into standard OpenAI JSON or Server-Sent Events (SSE), enabling you to use Manus with your favorite AI tools like **9router**, **OpenCode**, **Claude Code**, or any OpenAI-compatible SDK.

> [!IMPORTANT]
> This project uses the official Manus API. Keep your API keys secure, follow Manus usage terms, and **never** expose this service to the public internet without proper authentication.

---

## ✨ Features

- **OpenAI Compatibility**: Drop-in replacement for OpenAI endpoints (`/v1/chat/completions`, `/v1/models`).
- **Streaming Support**: Real-time task event streaming via SSE.
- **Token Pooling**: Intelligent round-robin token leasing with failover and cooldown mechanisms.
- **Agent Registry**: Automatically discovers and maps Manus agents to OpenAI models.
- **Container Ready**: Optimized Docker and Docker Compose support for easy deployment.

## 📸 Preview

![Terminal Screenshot](assets/screenshot.png)

## 🚀 Quick Start

### Local Installation

1. **Clone and Setup**
   ```bash
   git clone https://github.com/0xgetz/manusIM-proxy.git
   cd manusIM-proxy
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure Environment**
   ```bash
   cp .env.example .env
   # Add your Manus API keys to AUTH_TOKENS in .env
   ```

3. **Launch**
   ```bash
   python -m app.main
   ```

### Using Docker

```bash
docker compose up -d --build
```

---

## ⚙️ Configuration

| Variable | Description | Default |
| :--- | :--- | :--- |
| `AUTH_TOKENS` | Comma-separated Manus API keys | **Required** |
| `PORT` | Service listening port | `3457` |
| `MANUS_API_BASE` | Upstream Manus API URL | `https://api.manus.ai` |
| `REGISTRY_REFRESH` | Interval to refresh agent list (e.g., `6h`) | `6h` |
| `SESSION_TIMEOUT` | Max polling time for a task (e.g., `30m`) | `30m` |
| `TASK_ROTATION` | Max reuse time for a created task | `10m` |
| `DEFAULT_TASK_ID` | Pin `agent-default-main_task` to a specific ID | *Optional* |

---

## 🛠️ Usage

### Python SDK Example

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:3457/v1",
    api_key="proxy-key" # Any string works
)

response = client.chat.completions.create(
    model="agent-default-main_task",
    messages=[{"role": "user", "content": "Hello Manus!"}]
)
print(response.choices[0].message.content)
```

### cURL Example

```bash
curl http://localhost:3457/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{
    "model": "manus-1.6",
    "messages": [{"role": "user", "content": "Explain the task lifecycle."}],
    "stream": true
  }'
```

---

## 🔌 Integration with 9router

1. Go to **Providers** → **Custom Providers** → **Add OpenAI Compatible**.
2. **Base URL**: `http://127.0.0.1:3457/v1`
3. **Model**: `agent-default-main_task`
4. Click **Create** and start using Manus through the 9router gateway!

---

## 🧪 Testing

Run the local test suite to verify functionality:

```bash
python3 test_pool.py
python3 test_endpoints.py
```

---

## 📚 References

- [Manus API Authentication](https://open.manus.ai/docs/v2/authentication)
- [Task Lifecycle Documentation](https://open.manus.ai/docs/v2/task-lifecycle)
- [Agent List API](https://open.manus.ai/docs/v2/agent.list)

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
