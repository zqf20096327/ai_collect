<div align="center">

# 🧠 Cortex

### Your Local AI-Powered Codebase Assistant

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![LangChain](https://img.shields.io/badge/LangChain-Powered-green.svg)](https://www.langchain.com/)
[![Ollama](https://img.shields.io/badge/Ollama-Compatible-orange.svg)](https://ollama.ai/)

*A powerful, privacy-first RAG agent that helps you understand, navigate, and query your codebases with precision and ease.*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Use Cases](#-use-cases) • [Architecture](#-architecture)

</div>

---

## 🌟 Overview

**Cortex** is a sophisticated AI coding assistant that combines the power of **Retrieval-Augmented Generation (RAG)** with **multi-agent orchestration** to provide intelligent, context-aware answers about your codebase. Built with privacy in mind, Cortex runs entirely locally using Ollama and can also be configured to use CLIproxyAPI or OpenAI-compatible hosted models.

### Why Cortex?

- 🔒 **Privacy-First**: All data stays local. Your code never leaves your machine (unless using OpenAI).
- 🎯 **Precise & Intelligent**: Uses symbolic analysis (LSP) + semantic search for accurate answers.
- ⚡ **Lightning Fast**: Incremental indexing with SHA-256 hashing means only changed files are re-indexed.
- 🤖 **Multi-Agent System**: Specialized sub-agents for planning, exploration, building, and general queries.
- � **Real-Time Sync**: Automatic file watching keeps your index up-to-date as you code.
- 🌍 **Multi-Project Support**: Work with unlimited projects independently, each with its own `.cortex` directory.

---

## ✨ Features

### 🗂️ **Multi-Project Awareness**
- Each project maintains its own `.cortex` directory with metadata, indices, and state
- Switch between projects seamlessly
- No cross-contamination of project data

### 🔄 **Incremental Indexing**
- SHA-256 hashing detects file changes
- Only modified files are re-indexed
- Blazing-fast updates even for large codebases

### 🎯 **Symbolic Intelligence (LSP Integration)**
- Powered by **Jedi** for Python static analysis
- Find exact symbol definitions and references
- No guessing—Cortex knows precisely where your code is

### 🤖 **Deep Agent Orchestration**
- **LangGraph-based ReAct agents** for multi-step reasoning
- **Specialized sub-agents**:
  - 🔍 **Explorer**: Code search, understanding, and navigation
  - 🛠️ **Builder**: Code modification and file creation (read-only mode currently)
  - 📋 **Planner**: Multi-step task breakdown
  - 💬 **General**: Quick answers and simple queries
- **Intelligent tool selection** with fallback strategies

### 🔍 **Powerful Search Tools**
- **Semantic Search**: Find code by meaning and context
- **Exact Pattern Matching**: Regex-based grep for precise searches
- **Symbol Lookup**: Find definitions and references
- **File Discovery**: Search by name, pattern, or directory
- **Code Outline**: Get class/function structure without full content
- **Reranking**: LLM-powered result reranking for better relevance

### 👁️ **Automated Background Watching**
- Real-time file monitoring with `watchdog`
- Automatic re-indexing on file changes
- Always in sync with your latest code

### 🎨 **Professional CLI**
- Beautiful terminal UI with `Rich` library
- Interactive chat mode with conversation memory
- Single-shot query mode for quick answers
- Comprehensive repository management commands
- Passive per-project JSONL trace logs under `.cortex/logs/`

### 🔌 **Model Agnostic**
- **Local Models**: Optimized for `ministral-3:3b` + `qwen3-embedding:0.6b` via Ollama
- **Hosted Models**: Supports CLIproxyAPI and OpenAI-compatible chat endpoints
- Easy provider switching with `CORTEX_LLM_PROVIDER` or `--provider`

### 🌐 **GitHub Integration**
- Clone and index GitHub repositories directly
- Manage multiple cloned repos
- Full support for remote codebases

---

## � Installation

### Prerequisites
- Python 3.13+
- [uv](https://github.com/astral-sh/uv) package manager
- [Ollama](https://ollama.ai/) (for local models)

### Quick Start

```bash
# Clone the repository
git clone https://github.com/your-username/cortex.git
cd cortex

# Install dependencies
uv sync

# Install required models (Ollama)
./scripts/install_models.sh
```

### Environment Setup (Optional)

Create a `.env` file to control the default provider:

```bash
cp .env.example .env
# Edit .env and set CORTEX_LLM_PROVIDER=ollama or cliproxyapi
# Optional: set CORTEX_LOGGING_ENABLED=false to disable JSONL trace logs
```

---

## 📖 Usage

### 1️⃣ **Index a Local Project**

Index your current project or any directory:

```bash
# Index current directory
uv run python main.py index .

# Index a specific project
uv run python main.py index /path/to/your/project
```

**What happens:**
- Creates a `.cortex` directory in the project root
- Analyzes and chunks all code files
- Builds a vector index for semantic search
- Stores file hashes for incremental updates

---

### 2️⃣ **Index a GitHub Repository**

Clone and index a GitHub repository directly:

```bash
# Index from GitHub URL
uv run python main.py index https://github.com/user/repo.git --type github

# Or use the shorthand
uv run python main.py index https://github.com/user/repo.git
```

**What happens:**
- Clones the repository to `~/.cortex/repos/`
- Indexes the entire codebase
- Provides a path for future queries

---

### 3️⃣ **Ask a Question**

Query your codebase with a single question:

```bash
# Ask about the current project
uv run python main.py ask "How does the StateManager handle file hashing?"

# Ask about a specific project
uv run python main.py ask "What tools are available?" -p /path/to/project

# Use CLIproxyAPI for better responses
uv run python main.py ask "Explain the agent architecture" --provider cliproxyapi
```

**Features:**
- Automatic background file watching during query
- Multi-tool execution for comprehensive answers
- Supports local Ollama models plus CLIproxyAPI/OpenAI hosted models

---

### 4️⃣ **Interactive Chat**

Start a persistent conversation with your codebase:

```bash
# Chat with current project (uses CORTEX_LLM_PROVIDER, defaulting to Ollama)
uv run python main.py chat

# Chat with a specific project
uv run python main.py chat --project /path/to/project

# Switch to CLIproxyAPI for one run
uv run python main.py chat --provider cliproxyapi
```

**Features:**
- Conversation memory across messages
- Real-time file watching
- Per-query trace log path is shown after each answer
- Type `exit` or `quit` to end the session

**Example Session:**
```
You : What files are in the agents directory?
Cortex: The agents directory contains:
- orchestrator.py (main orchestrator)
- tools.py (tool definitions)
- reranker.py (result reranking)
- subagents/ (specialized agents)

You : Show me the tools available
Cortex: [Lists all tools with descriptions...]
```

---

### 5️⃣ **Watch for Changes**

Manually start the file watcher (usually automatic in `ask` and `chat`):

```bash
# Watch current directory
uv run python main.py watch .

# Watch a specific project
uv run python main.py watch /path/to/project
```

**What it does:**
- Monitors file system for changes
- Automatically re-indexes modified files
- Keeps your vector store in sync

### Provider Switching

Switch the default provider globally in `.env`:

```bash
CORTEX_LLM_PROVIDER=ollama
```

Or override it per command:

```bash
uv run python main.py chat --provider ollama
uv run python main.py chat --provider cliproxyapi
uv run python main.py chat --provider openai
```

---

### 6️⃣ **Manage GitHub Repositories**

List and manage cloned repositories:

```bash
# List all cloned repos
uv run python main.py repo list

# Delete a cloned repo
uv run python main.py repo delete repo-name
```

---

## 🎯 Use Cases

### 🔍 **Code Exploration**
> *"I just joined a new team. How do I understand this massive codebase?"*

```bash
uv run python main.py chat --project /path/to/new/codebase
```

**Ask questions like:**
- "What is the overall architecture?"
- "Where is the authentication logic?"
- "How does the database connection work?"
- "Show me all API endpoints"

---

### 🐛 **Debugging & Investigation**
> *"There's a bug in the payment processing. Where should I look?"*

```bash
uv run python main.py ask "Find all code related to payment processing"
```

**Cortex will:**
- Search semantically for payment-related code
- Find exact function/class definitions
- Show you references across the codebase

---

### 📚 **Documentation & Onboarding**
> *"I need to document how our indexing system works."*

```bash
uv run python main.py ask "Explain how the incremental indexing system works"
```

**Get detailed explanations with:**
- Code snippets from relevant files
- Architecture diagrams (via agent reasoning)
- Step-by-step breakdowns

---

### 🔄 **Refactoring Assistance**
> *"I want to refactor the StateManager class. What depends on it?"*

```bash
uv run python main.py ask "Find all references to StateManager"
```

**Cortex provides:**
- All files using StateManager
- Exact line numbers and context
- Related classes and functions

---

### 🌐 **Open Source Exploration**
> *"I want to understand how LangChain implements agents."*

```bash
# Index the LangChain repository
uv run python main.py index https://github.com/langchain-ai/langchain.git --type github

# Ask questions
uv run python main.py ask "How are agents implemented?" -p ~/.cortex/repos/langchain
```

---

### 🧪 **Testing & Quality Assurance**
> *"Are there any tests for the ingestion pipeline?"*

```bash
uv run python main.py ask "Find all test files related to ingestion"
```

---

### 🏗️ **Architecture Review**
> *"I need to understand the data flow in this system."*

```bash
uv run python main.py chat
# Then ask: "Trace the data flow from user input to database storage"
```

---

## 🏗️ Architecture

### System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                         Cortex CLI                          │
│                    (Typer + Rich UI)                        │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                    Deep Agent Orchestrator                  │
│              (LangGraph Multi-Agent System)                 │
├─────────────────────────────────────────────────────────────┤
│  Sub-Agents:                                                │
│  • Explorer (Code Search & Understanding)                   │
│  • Builder (Code Modification - Read-Only)                  │
│  • Planner (Multi-Step Task Breakdown)                      │
│  • General (Quick Answers)                                  │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                        Tool Layer                           │
├─────────────────────────────────────────────────────────────┤
│  • search_code (Semantic Search + Reranking)                │
│  • grep_code (Regex Pattern Matching)                       │
│  • read_file (File Content Retrieval)                       │
│  • get_symbol_info (LSP Symbol Definitions)                 │
│  • find_references (LSP Reference Lookup)                   │
│  • list_files (Directory Exploration)                       │
│  • search_files_by_name (Pattern-Based File Search)         │
│  • get_file_outline (AST-Based Structure)                   │
└────────────────────┬────────────────────────────────────────┘
                     │
        ┌────────────┴────────────┐
        ▼                         ▼
┌──────────────────┐    ┌──────────────────┐
│  Vector Store    │    │   LSP Engine     │
│   (ChromaDB)     │    │     (Jedi)       │
├──────────────────┤    ├──────────────────┤
│ • Embeddings     │    │ • Static         │
│ • Semantic       │    │   Analysis       │
│   Search         │    │ • Symbol         │
│ • Reranking      │    │   Resolution     │
└──────────────────┘    └──────────────────┘
```

### Component Details

#### **1. Ingestion Pipeline**
- **File Loading**: Recursive directory traversal with smart filtering
- **Chunking**: Specialized chunkers for Python (AST-based) and text
- **Hashing**: SHA-256 for change detection
- **State Management**: SQLite database tracks indexed files

#### **2. Vector Store**
- **Engine**: ChromaDB for efficient vector storage
- **Embeddings**: `qwen3-embedding:0.6b` (local) or OpenAI embeddings
- **Storage**: `.cortex/chroma/` directory per project
- **Retrieval**: Similarity search with configurable k-value

#### **3. Agent System**
- **Framework**: LangGraph for agent orchestration
- **Pattern**: ReAct (Reasoning + Acting)
- **Memory**: In-memory conversation state with thread IDs
- **Sub-Agents**: Specialized agents for different task types

#### **4. LSP Integration**
- **Engine**: Jedi for Python static analysis
- **Capabilities**: Symbol definitions, references, type inference
- **Scope**: Project-wide symbol resolution

#### **5. File Watching**
- **Library**: `watchdog` for file system monitoring
- **Triggers**: File creation, modification, deletion
- **Action**: Automatic re-indexing of changed files

---

## 🛠️ Available Tools

| Tool | Description | Use Case |
|------|-------------|----------|
| `search_code` | Semantic search with reranking | "How does authentication work?" |
| `grep_code` | Exact regex pattern matching | "Find all TODO comments" |
| `read_file` | Read full file content | "Show me the config file" |
| `get_symbol_info` | Find symbol definitions | "Where is UserManager defined?" |
| `find_references` | Find symbol usages | "Where is UserManager used?" |
| `list_files` | List directory contents | "What's in the agents folder?" |
| `search_files_by_name` | Pattern-based file search | "Find all test files" |
| `get_file_outline` | Get class/function structure | "Show me the structure of main.py" |

---

## 🧪 Advanced Configuration

### Custom Models

**Using Different Ollama Models:**
```bash
uv run python main.py chat --provider ollama --model llama3:8b
```

**Using OpenAI Models:**
```bash
export OPENAI_API_KEY="your-key-here"
uv run python main.py chat --provider openai --model gpt-4o
```

### Project Structure

```
your-project/
├── .cortex/                 # Cortex metadata (auto-created)
│   ├── chroma/             # Vector store
│   └── indexing/
│       └── state.db        # File hash state
├── your-code/
└── ...
```

---

## 📊 Performance

- **Indexing Speed**: ~100-500 files/second (depends on file size)
- **Query Latency**: 
  - Local (Ollama): 2-5 seconds
  - OpenAI: 1-3 seconds
- **Memory Usage**: ~200-500 MB (depends on project size)
- **Incremental Updates**: 10-100x faster than full re-indexing

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 🙏 Acknowledgments

- **LangChain** for the agent framework
- **Ollama** for local LLM inference
- **ChromaDB** for vector storage
- **Jedi** for Python static analysis
- **Rich** for beautiful terminal UI

---

<div align="center">

**Built with ❤️ by developers, for developers**

[⭐ Star this repo](https://github.com/adilzubair/cortex) if you find it useful!

</div>
