# AI Agents Training — Getting Started with LLM Agents using LangChain & LangGraph

Hands-on notebooks and a deployable demo for building LLM agents with LangChain and LangGraph — running on **local models via [Ollama](https://ollama.com/)**, with [Tavily](https://tavily.com/) for web search.

## Prerequisites

- **Python 3.11+**
- **[uv](https://github.com/astral-sh/uv)** — fast Python package manager
- **[Ollama](https://ollama.com/download)** — runs the models locally (no OpenAI key needed)
- **Tavily API key** — free tier at https://tavily.com/

## Quick Setup (uv)

1. **Install uv:**

   ```bash
   # macOS / Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   # Windows (PowerShell)
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```
2. **Install everything (creates `.venv`, includes the research-agent demo):**

   ```bash
   uv sync
   ```
3. **Activate the environment** (optional — `uv run <cmd>` works without it):

   ```bash
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
4. **Pull the local models:**

   ```bash
   ollama pull qwen3.5-4b-16k     # chat model used across the notebooks (or any Qwen 3.5 tag)
   ollama pull nomic-embed-text   # embeddings for the RAG notebook
   ```
5. **Set up your environment variables:**

   ```bash
   cp .env.example .env
   # Edit .env and add your TAVILY_API_KEY
   ```
6. **Install the Jupyter kernel:**

   ```bash
   uv run python -m ipykernel install --user --name=ai-agents --display-name "AI Agents (ai-agents)"
   ```

> **Already use pip or conda?** You don't need to switch tools — just `pip install uv` inside your environment, then run `uv sync`. uv downloads a matching Python automatically if 3.11+ isn't installed.

## Managing Dependencies

All dependencies live in [pyproject.toml](pyproject.toml); exact versions are pinned in `uv.lock` (commit both).

| Task | Command |
|---|---|
| Install / update to the locked versions | `uv sync` |
| Add a package | `uv add <pkg>` |
| Remove a package | `uv remove <pkg>` |
| Upgrade all packages | `uv lock --upgrade && uv sync` |
| Run a command in the env | `uv run <cmd>` |

## Environment Variables

Copy `.env.example` to `.env` and fill in:

- **TAVILY_API_KEY** (required for web search): https://tavily.com/
- **OLLAMA_BASE_URL** (optional): defaults to `http://localhost:11434`
- **LANGSMITH_API_KEY** (optional, tracing): https://smith.langchain.com/settings

## Switching Models

Every notebook uses a local Ollama model, e.g. `init_chat_model("ollama:qwen3.5-4b-16k")`. To use a different model, change that string to any tag shown by `ollama list`.

> Small models (≈4B) can struggle with tool calling and structured output. If a router/grader/tool cell misbehaves, switch to a larger Qwen tag first.

To go back to OpenAI, use `init_chat_model("openai:<model>")`, install `langchain-openai`, and set `OPENAI_API_KEY`.

## Using Jupyter Notebooks

When opening a notebook in VS Code or Jupyter, select the **"AI Agents (ai-agents)"** kernel (top-right in VS Code). If it's missing, rerun setup step 6.

## Notebooks

> Colab can't reach the Ollama server on your machine — run notebooks locally, or switch the model string to a hosted provider when using Colab.

| # | Module | Notebook | What you'll learn | Colab |
|---|---|---|---|---|
| 0.0 | Foundations | [Intro to LLM Agents from Scratch](notebooks/0.0-intro-llm-agents-from-scratch.ipynb) | Agent loop, tool calling and memory — no framework | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ashishpatel26/Training_AI_Agents/blob/main/notebooks/0.0-intro-llm-agents-from-scratch.ipynb) |
| 1.0 | LangGraph Basics | [Intro to LangGraph](notebooks/1.0-intro-langgraph.ipynb) | Graphs, nodes, edges, `init_chat_model`, `bind_tools` | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ashishpatel26/Training_AI_Agents/blob/main/notebooks/1.0-intro-langgraph.ipynb) |
| 1.1 | LangGraph Basics | [Chatbot with Web Search](notebooks/1.1-intro-langgraph-chatgpt-search.ipynb) | Tool-calling chatbot with Tavily search | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ashishpatel26/Training_AI_Agents/blob/main/notebooks/1.1-intro-langgraph-chatgpt-search.ipynb) |
| 2.0 | Core Concepts | [LangGraph Core Concepts](notebooks/2.0-langgraph-core-concepts.ipynb) | State, routing, structured output, ToolNode | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ashishpatel26/Training_AI_Agents/blob/main/notebooks/2.0-langgraph-core-concepts.ipynb) |
| 2.1 | Core Concepts | [Simple Math Agent](notebooks/2.1-langgraph-simple-math-agent.ipynb) | Custom tools and `create_agent` | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ashishpatel26/Training_AI_Agents/blob/main/notebooks/2.1-langgraph-simple-math-agent.ipynb) |
| 2.2 | Core Concepts | [LangGraph Latest Features](notebooks/2.2-langgraph-latest-features.ipynb) | Command, Functional API, MCP tools | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ashishpatel26/Training_AI_Agents/blob/main/notebooks/2.2-langgraph-latest-features.ipynb) |
| 2.3 | Core Concepts | [Persistence and Checkpointers](notebooks/2.3-persistence-and-checkpointers.ipynb) | Memory, threads, state inspection | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ashishpatel26/Training_AI_Agents/blob/main/notebooks/2.3-persistence-and-checkpointers.ipynb) |
| 3.0 | Agent Projects | [Local Research Agent](notebooks/3.0-local-research-agent-langgraph.ipynb) | Iterative search → reflect → report loop | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ashishpatel26/Training_AI_Agents/blob/main/notebooks/3.0-local-research-agent-langgraph.ipynb) |
| 3.1 | Agent Projects | [RAG Agent](notebooks/3.1-rag-agent.ipynb) | Routing, retrieval grading, web-search fallback | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ashishpatel26/Training_AI_Agents/blob/main/notebooks/3.1-rag-agent.ipynb) |
| 4.0 | Deployment | [Deployment with LangGraph Platform](notebooks/4.0-deployment-langgraph-platform.ipynb) | Project structure, `langgraph dev`, deploying | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ashishpatel26/Training_AI_Agents/blob/main/notebooks/4.0-deployment-langgraph-platform.ipynb) |

## Demo: Research Agent

A deployable LangGraph research agent lives in [demos/research_agent/](demos/research_agent/):

```bash
cd demos/research_agent
cp .env.example .env          # add TAVILY_API_KEY
uv run langgraph dev --no-reload   # serves on http://127.0.0.1:2024 and opens LangGraph Studio
```

See its [README](demos/research_agent/README.md) for details.

## Repository Structure

```
├── notebooks/                 # Learning path: 0.0 → 4.0 (run in order)
│   ├── assets-resources/      # Images and papers referenced by the notebooks
│   ├── my_mcp_server.py       # MCP server used by 2.2 (loaded by relative path)
│   └── pancakes-philosophy.txt  # Sample file used by 0.0
├── demos/
│   └── research_agent/        # Deployable LangGraph research agent (uv workspace member)
├── docs/                      # Cheatsheet + all links referenced in the course
├── pyproject.toml / uv.lock   # uv workspace — `uv sync` installs everything
└── archive/                   # Unreferenced legacy assets (git-ignored, local only)
```

## Additional Resources

- **Cheatsheet:** [docs/ai-agents-training-cheatsheet.html](docs/ai-agents-training-cheatsheet.html)
- **Links & references:** [docs/resources.md](docs/resources.md)

---

Maintained by [Ashish Patel (@ashishpatel26)](https://github.com/ashishpatel26).
