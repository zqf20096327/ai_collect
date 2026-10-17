<h1 align="center">Logfire AI Assistant by Vstorm</h1>

<p align="center">
  <b>AI-Powered Debugging and Analysis for Pydantic Logfire</b>
  <br>
  <sub>Built by <a href="https://vstorm.co/">Vstorm</a> — AI tooling for modern development teams</sub>
</p>

<p align="center">
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-features">Features</a> •
  <a href="#-screenshots">Screenshots</a> •
  <a href="#-how-it-works">How It Works</a>
</p>

<p align="center">
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.11+-blue.svg?logo=python&logoColor=white" alt="Python 3.11+"></a>
  <a href="https://github.com/pydantic/pydantic-ai"><img src="https://img.shields.io/badge/PydanticAI-E92063?logo=pydantic&logoColor=white" alt="PydanticAI"></a>
  <a href="https://logfire.pydantic.dev"><img src="https://img.shields.io/badge/Logfire-E92063?logo=pydantic&logoColor=white" alt="Logfire"></a>
  <a href="https://fastapi.tiangolo.com"><img src="https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white" alt="FastAPI"></a>
  <a href="https://www.postgresql.org"><img src="https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white" alt="PostgreSQL"></a>
  <a href="https://redis.io"><img src="https://img.shields.io/badge/Redis-DC382D?logo=redis&logoColor=white" alt="Redis"></a>
  <a href="https://react.dev"><img src="https://img.shields.io/badge/React-61DAFB?logo=react&logoColor=black" alt="React"></a>
  <a href="https://www.typescriptlang.org"><img src="https://img.shields.io/badge/TypeScript-3178C6?logo=typescript&logoColor=white" alt="TypeScript"></a>
</p>

<p align="center">
  <b>🔍 Natural Language Queries</b>
  &nbsp;•&nbsp;
  <b>🗃️ Auto SQL Generation</b>
  &nbsp;•&nbsp;
  <b>📊 Smart Visualizations</b>
  &nbsp;•&nbsp;
  <b>⚡ Real-time Streaming</b>
</p>

---

**Logfire AI Assistant by Vstorm** is an AI-powered tool that helps you debug, analyze, and understand your applications using [Pydantic Logfire](https://logfire.pydantic.dev). Ask questions in plain English, get instant answers with SQL queries and visualizations. Developed by [Vstorm](https://vstorm.co/) as part of our open-source AI developer tools ecosystem.

<p align="center">
  <img src="assets/screenshots/demo.gif" alt="Logfire AI Assistant Demo" width="600">
  <br><i>Ask questions in natural language, get SQL queries and visualizations</i>
</p>

## Why Use It?

Debugging AI agents and complex applications is hard:

- **Long traces** — Agents generate many spans across multiple tool calls and LLM requests
- **Complex prompts** — System prompts can be lengthy, making it hard to spot issues
- **Multi-turn conversations** — Understanding what happened requires looking across entire interaction histories

Vstorm's Logfire AI Assistant acts as your **AI debugging partner** — it understands agent architectures, recognizes failure patterns, and helps you ship better software faster.

---

## 📸 Screenshots

### Main Interface

<p align="center">
  <img src="assets/screenshots/home_page.png" alt="Home Page" width="800">
  <br><i>Chrome extension sidebar integrated with Logfire dashboard</i>
</p>

### Core Features

| Query Results | SQL Generation |
|:---:|:---:|
| ![Query Results](assets/screenshots/chat_with_results.png) | ![SQL Query](assets/screenshots/sql_query_view.png) |
| *AI responses with data tables* | *View generated SQL queries* |

| Chart Visualization | Span Analysis |
|:---:|:---:|
| ![Chart](assets/screenshots/chart_view.png) | ![Span Select](assets/screenshots/span_select.png) |
| *Auto-generated charts from query results* | *Select spans directly in Logfire UI* |


### Settings & Configuration

| Multi-Project Support | Custom Prompts |
|:---:|:---:|
| ![Projects](assets/screenshots/projects.png) | ![Prompts](assets/screenshots/prompts_config.png) |
| *Switch between Logfire projects* | *Create reusable prompt templates* |

| LLM Model Selection | Customization |
|:---:|:---:|
| ![LLM Providers](assets/screenshots/llm_providers.png) | ![Style](assets/screenshots/style.png) |
| *Choose from multiple AI models* | *Customize appearance and behavior* |

### Additional Features

| Slash Commands | Conversation History |
|:---:|:---:|
| ![Prompts View](assets/screenshots/prompts_view.png) | ![Conversations](assets/screenshots/conversations.png) |
| *Quick access to saved prompts* | *Browse and continue past conversations* |

| File Attachments | |
|:---:|:---:|
| ![File Input](assets/screenshots/file_input.png) | |
| *Attach files for context* | |

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **🔍 Natural Language Queries** | Ask about your app's behavior in plain English |
| **🗃️ SQL Query Generation** | AI translates questions into SQL against Logfire data |
| **📊 Auto Visualizations** | Automatically generate charts from query results |
| **🎯 Span Context** | Select spans in Logfire and ask "what happened here?" |
| **📁 Multi-Project Support** | Switch between different Logfire projects seamlessly |
| **📝 Custom Prompts** | Define reusable prompts for common analysis tasks |
| **⚡ Real-time Streaming** | Responses stream via WebSocket as they're generated |
| **🔐 JWT Authentication** | Secure access with token-based auth |

---

## 🚀 Quick Start

### 1. Backend

```bash
# Install & configure
make install
cp backend/.env.example backend/.env
# Edit backend/.env with your settings

# Start database & run migrations
make db-init && make db-upgrade

# Run server
make run dev
```

### 2. Browser Extension

```bash
cd browser-extension
bun install && bun run build
```

Then load in Chrome:
1. Go to `chrome://extensions/`
2. Enable **Developer mode**
3. Click **Load unpacked** → select `browser-extension/dist`

**That's it!** Open [Logfire dashboard](https://logfire.pydantic.dev), click on any span, and start asking questions.

---

## 🔄 How It Works

```
You: "Why did this request take so long?"
                    │
                    ▼
┌─────────────────────────────────────────────────────────┐
│  Chrome Extension                                       │
│  • Captures span context (trace_id, span_id)            │
│  • Sends question via WebSocket                         │
└─────────────────────────────────────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────────────────┐
│  AI Agent (PydanticAI)                                  │
│  • Analyzes question + context                          │
│  • Generates SQL query                                  │
│  • Executes against Logfire API                         │
│  • Creates visualization if needed                      │
└─────────────────────────────────────────────────────────┘
                    │
                    ▼
Answer: "The database query on line 42 took 3.2s due to
        missing index on user_id column. Here's the
        breakdown chart..."
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Chrome Extension                         │
│  ┌─────────────────┐  ┌──────────────────────────────────┐  │
│  │ Content Script  │  │         Sidebar Panel            │  │
│  │ (Logfire page)  │  │  • Chat interface                │  │
│  │ • Span selector │  │  • Project switcher              │  │
│  │ • Context grab  │  │  • Settings & prompts            │  │
│  └────────┬────────┘  └──────────────┬───────────────────┘  │
└───────────┼──────────────────────────┼──────────────────────┘
            │                          │
            │      WebSocket           │
            └──────────┬───────────────┘
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                      Backend (FastAPI)                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐   │
│  │   API Routes │  │   Services   │  │   AI Agent       │   │
│  │   /api/v1/*  │──│              │──│   (PydanticAI)   │   │
│  └──────────────┘  └──────────────┘  └────────┬─────────┘   │
│                                               │             │
│  ┌────────────────┐  ┌──────────────┐  ┌──────▼───────────┐ │
│  │  PostgreSQL    │  │    Redis     │  │  Logfire API     │ │
│  │  (users,       │  │  (cache,     │  │  (query data)    │ │
│  │  conversations)│  │  rate limit) │  └──────────────────┘ │
│  └────────────────┘  └──────────────┘                       │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Development

### Backend Commands

```bash
make run dev           # Development server
make test              # Run tests
make test-cov          # Tests with coverage
make lint              # Check linting
make format            # Auto-fix formatting
make db-migrate        # Create new migration
make docker-up         # Start all services (Docker)
```

### Extension Commands

```bash
cd browser-extension
bun run dev            # Watch mode
bun run build          # Production build
bun run check          # Lint + format (Biome)
```

---

## 📁 Project Structure

```
├── backend/
│   └── app/
│       ├── agents/           # AI agent (PydanticAI)
│       ├── api/routes/v1/    # HTTP endpoints
│       ├── services/         # Business logic
│       ├── repositories/     # Data access
│       ├── schemas/          # Pydantic models
│       └── db/models/        # SQLAlchemy models
├── browser-extension/
│   └── src/
│       ├── background/       # Service worker
│       ├── content/          # Content script
│       ├── sidebar/          # Side panel UI
│       └── stores/           # Zustand stores
└── docker-compose.yml
```

---

## ⚙️ Environment Variables

Copy `backend/.env.example` to `backend/.env`:

```bash
ENVIRONMENT=local
SECRET_KEY=your-secret-key     # openssl rand -hex 32

POSTGRES_HOST=localhost
POSTGRES_PASSWORD=postgres

REDIS_HOST=localhost

LOGFIRE_TOKEN=your-token       # Optional, for backend observability
```

---

## 🙏 Built With

- [Pydantic Logfire](https://logfire.pydantic.dev) — Observability platform from the Pydantic team
- [Pydantic AI](https://ai.pydantic.dev) — The agent framework powering this assistant
- Inspired by [Polly by LangChain](https://blog.langchain.com/introducing-polly-your-ai-agent-engineer/) — AI Agent Engineer for LangSmith

---

## 📄 License

See [LICENSE](LICENSE) for details.

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/vstorm-co">Vstorm</a>
</p>
