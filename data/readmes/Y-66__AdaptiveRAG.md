# AdaptiveRAG

An agentic adaptive RAG system designed for **intelligent query routing** and **multi-agent collaboration**.

![Overview](./public/Orchestrator.jpeg)

- **SQL Agent**
  
  This agent translates natural language into executable SQL queries, performs schema-aware reasoning, and features an auto-repair loop for syntax errors.
  ![](./public/SQL_Agent.jpeg)
- **Self-RAG**
  
  Implements a "Retrieve-Grade-Rewrite-Double Check" cycle. It ensures high precision by filtering irrelevant context and self-correcting hallucinations before final generation.
  ![](./public/Self_RAG.jpeg)
- **Web Search Agent**
  
  When local data is insufficient, this agent leverages the Model Context Protocol (MCP) to dynamically connect with external search engines and web scrapers.
  ![](./public/Web_Search_Agent.jpeg)


**Result Display:**

Query: What was Amazon's revenue in 2023?

Answer: `.md` file
![](./public/Answer.png)

## Introduction

AdaptiveRAG is a sophisticated system that leverages "Adaptive Routing + Multi-Agent Collaboration" to answer complex user queries. Instead of a one-size-fits-all approach, the system intelligently analyzes the user's question and routes it to the most appropriate specialized agent. It incorporates self-correction mechanisms, such as hallucination detection and query rewriting, to ensure high-quality, accurate responses.

### Key Features

*   **Adaptive Routing:** Automatically directs queries to specialized agents (Financial RAG, SQL Database, or Web Search) based on intent.
*   **Self-Correction (Self-RAG):** Evaluates retrieved documents and generated answers. If quality is low, it rewrites queries or regenerates answers.
*   **Multi-Step Reasoning:** Capable of breaking down complex questions into sub-queries.
*   **Structured & Unstructured Data:** Handles both unstructured documents (PDFs, reports) and structured SQL databases.

## Technology Stack

*   **LangGraph:** For building stateful, multi-actor applications with cyclic graph flows.
*   **LangChain:** For LLM agents, tool interfaces, and chaining.
*   **ChromaDB:** Vector database for local financial document retrieval.
*   **SQLite:** Relational database used to store employees information.
*   **OpenAI:** LLM backend for reasoning, grading, and generation.
*   **Loguru:** Comprehensive logging and tracing.
*   **Python 3.12:** Core runtime environment.

## Architecture & Logic

The system entry point is a global **Router** (`business_logic_decision`) that classifies the input question into one of three pathways:

### 1. Financial Docs RAG (Self-RAG)
Designed for answering questions based on unstructured documents like annual reports, financial indicators, and operating data.
*   **Retrieve:** Fetches relevant contexts from vector storage.
*   **Grade Documents:** An LLM evaluator filters out irrelevant documents.
*   **Transform Query:** If retrieval is poor, the query is rewritten for better alignment.
*   **Generate:** Produces an answer using valid context.
*   **Quality Check:** Detecting hallucinations and ensuring the answer directly addresses the prompt. If the check fails, the cycle repeats (up to `MAX_REWRITE_TIMES`).

### 2. SQL Agent
Designed for querying structured relational data (e.g., employee records, inventory lists).
*   **Parse:** Identifies required tables and fields.
*   **Generate SQL:** Converts natural language to valid SQL.
*   **Execute:** Runs the query against the database.
*   **Repair:** Auto-corrects SQL syntax errors if execution fails.

### 3. Web Search Agent
Designed for general knowledge or real-time events not covered by local data.
*   **Search:** Uses external search tools (e.g., Tavily/DuckDuckGo) to fetch live information.

## Setup & Installation

### 1. Create Virtual Environment

Create and activate a Python 3.12 environment using Conda:

```bash
conda create -n adaptiveRAG python=3.12
conda activate adaptiveRAG
```

### 2. Upgrade pip

Ensure your package manager is up to date:

```bash
pip install --upgrade pip setuptools
```

### 3. Install Dependencies

Install the core dependencies:

```bash
pip install -e .
```

For development (including testing tools):

```bash
pip install -e ".[dev]"
```

### 4. Configuration

Create a `.env` file in the root directory and add your API keys:

```env
OPENAI_API_KEY=your_openai_key_here
TAVILY_API_KEY=your_tavily_key_here
LOG_LEVEL=INFO
```

## Docker Support

You can also run AdaptiveRAG using Docker to ensure a consistent environment.

### 1. Build the Image

```bash
docker build -t adaptive-rag .
```

### 2. Run the Container

Make sure to pass your `.env` file or environment variables to the container:

```bash
docker run --env-file .env adaptive-rag
```

Or pass specific variables:

```bash
docker run -e OPENAI_API_KEY=sk-... adaptive-rag
```
