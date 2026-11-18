# 🤖 WhatsApp Agent (MCP + Google ADK)

![Python](https://img.shields.io/badge/python-3.9+-blue)
![](https://badge.mcpx.dev 'MCP')

> An intelligent WhatsApp Agent built with **Google ADK** and the **Model Context Protocol (MCP)**.  
> Send messages, search chats, and interact with WhatsApp directly from your AI agent environment.

---

## ✨ Features
- 📩 **Send WhatsApp messages** (with AI-crafted text + disclaimers).
- 🔍 **Search chats & messages** using MCP tools.
- 🧩 **Schema sanitization** for Gemini compatibility.
- ⚡ Powered by **Google ADK**, MCP Toolsets, and WhatsApp bridge.
- ☁️ Deployment-ready with environment configs.

---

## 🧩 Architecture

```text
+-------------------+        +-----------------+        +---------------------+
|   User / Agent    | <----> |   MCP Toolset   | <----> | WhatsApp MCP Server |
+-------------------+        +-----------------+        +---------------------+
                                   (Python)                   (Go + SQLite)
````

* **Go Bridge** → connects to WhatsApp multi-device API.
* **Python MCP Server** → exposes standardized tools (send, search, list).
* **Google ADK Agent** → orchestrates message crafting + disclaimer + sending.
* **WhatsApp MCP Server (repo)** → [lharries/whatsapp-mcp](https://github.com/lharries/whatsapp-mcp)

---

## ⚙️ Installation

### Prerequisites

* [Go](https://go.dev/)
* [Python 3.9+](https://www.python.org/)
* [UV](https://docs.astral.sh/uv/) (Python package manager)
* WhatsApp mobile app (for QR authentication)

### Setup

1. **Clone this repository**

   ```bash
   git clone https://github.com/B4K2/WhatsApp-agent.git
   cd WhatsApp-agent
   ```

2. **Install dependencies**

   ```bash
   uv sync
   ```

3. **Set environment variables** (in `.env`)

   ```env
   UV_EXECUTABLE_PATH=/usr/local/bin/uv
   PYTHON_MCP_SERVER_DIRECTORY=./multi_tool_agent
   ```

4. **Run the WhatsApp MCP bridge**

   ```bash
   cd whatsapp-bridge
   go run main.go
   ```

   📲 Scan the QR code with WhatsApp mobile to authenticate.

5. **Run the Python MCP server**

   ```bash
   uv run main.py
   ```

---

## 🚀 Usage

Here’s how the agent works:

```python
from google.adk.agents import Agent

agent = Agent(
    name="WhatsApp_Orchestrator",
    model="gemini-2.0-flash",
)

# Example: Send a message
agent("Send 'On my way!' to +91XXXXXXXXXX")
```

✅ Agent crafts the message
✅ Appends disclaimer
✅ Sends via `send_message` tool

---

## ⚠️ Security Note

As with many MCP servers, be cautious of [prompt injection attacks](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/).
Messages and metadata are stored locally in SQLite.

---

## 🤝 Contributing

Pull requests are welcome! If you’d like to extend the toolset (media sending, chat search), fork and submit a PR.
