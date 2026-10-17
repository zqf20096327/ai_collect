# ERPNext AI Agent

Intelligent assistant for ERPNext that uses semantic search, knowledge graphs, and multi-agent workflows to speed up ERP development and document processing.

## What it does

- **Semantic Search** — Find any ERPNext document (invoices, orders, customers) using natural language
- **Auto-generate DocTypes** — Describe a business need → get Frappe doctype JSON, controllers, and workflows
- **Knowledge Graphs** — Maps relationships between customers, orders, items, and projects
- **Multi-Agent Pipeline** — Specialized agents handle requirements analysis → architecture → schema → implementation
- **Document Processing** — PDF, DOCX, Excel ingestion with automatic indexing

## Tech Stack

| Component | Technology |
|-----------|-----------|
| AI/LLM | LangChain, OpenAI, Anthropic, Sentence Transformers |
| Vector DB | ChromaDB, FAISS |
| Knowledge Graph | Neo4j, NetworkX |
| RL Training | Gymnasium, Stable-Baselines3 |
| Multi-Agent | CrewAI, AutoGen |
| API Server | FastAPI + Uvicorn |
| Document Processing | spaCy, PyPDF2, python-docx |
| Monitoring | Prometheus, structlog |

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Start the AI agent
python start_erpnext_ai_agent.py
```

The agent auto-detects your ERPNext instance and begins indexing documents immediately.

Requirements: Python 3.10+, Neo4j (for knowledge graphs), ChromaDB (for vector search), Redis (for caching). Docker recommended for full setup — see `docker/README.md`.

## Architecture

```
User Request
    │
    ▼
┌─────────────────────────────────┐
│     Multi-Agent Orchestrator     │
│  (requirements → arch → schema)  │
└──────────────┬──────────────────┘
               │
     ┌─────────┼─────────┐
     ▼         ▼         ▼
┌─────────┐ ┌──────┐ ┌──────────┐
│ Semantic│ │Knowl-│ │Document  │
│ Search  │ │edge  │ │Processor │
│(Chroma) │ │Graph │ │(spaCy)   │
└────┬────┘ └──┬───┘ └────┬─────┘
     │         │          │
     └─────────┼──────────┘
               ▼
        ERPNext Instance
```

## Real Examples

```python
from integrations.multi_agent_workflows import MultiAgentOrchestrator

orchestrator = MultiAgentOrchestrator()

# Generate a complete sales management system
result = orchestrator.execute_workflow(
    "Design a sales management system with quotes, orders, and invoicing"
)

# Build an inventory system with automated reordering
result = orchestrator.execute_workflow(
    "Create inventory system with automated reordering and low stock alerts"
)
```

## Project Structure

```
integrations/
├── erpnext_connector.py      — ERPNext API client
├── document_indexer.py       — Semantic indexing pipeline
├── knowledge_graph_builder.py — Neo4j relationship mapper
├── multi_agent_workflows.py  — Agent orchestration
├── rl_training_dataset.py    — RL training data generation
└── mcp_server_config.py      — MCP server for IDE integration

start_erpnext_ai_agent.py     — One-command launcher
docker/                        — Docker & container configs
```

## License

MIT
