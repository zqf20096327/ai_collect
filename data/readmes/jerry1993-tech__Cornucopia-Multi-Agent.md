<p align="center"><img src="./assets/images/Cornucopia_logo.png" alt="Cornucopia Logo" width="200"></p>

<h1 align="center">Cornucopia Multi-Agent</h1>

<p align="center">
  <a href="./README.md">English</a> | <a href="./README_zh.md">中文</a>
</p>

**Cornucopia Multi-Agent** is a production-grade multi-agent collaboration framework. It provides a full spectrum of capabilities ranging from simple sequential invocation to autonomous LLM deep planning with cluster execution. Built-in with 8 professional tools, 6 collaboration modes, and 6 communication topologies, it supports WebSocket real-time streaming and Streamlit visual operations. Whether building market research pipelines, debate consensus engines, or complex hierarchical agent organizations, Cornucopia is ready to use out of the box.

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Features](#features)
- [Quick Start](#quick-start)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Core Modules](#core-modules)
- [Tool System](#tool-system)
- [Collaboration Modes](#collaboration-modes)
- [Execution Paths](#execution-paths)
- [Tech Stack](#tech-stack)

## Overview

Cornucopia is a production-grade multi-agent collaboration framework that supports:

- **6 Collaboration Modes**: Sequential passing, parallel processing, debate consensus, expert team, critic review, hierarchical collaboration
- **6 Communication Topologies**: Single agent, network, supervisor, supervisor-as-tool, hierarchical, custom
- **4 Execution Paths**: Simple execution, LLM collaboration, deep cluster, dynamic workflow
- **8 Professional Tools**: web_search (youdotcom), data analysis, web scraping, code execution, report writing, knowledge base, calculator, agent delegation
- **Real-time WebSocket Streaming**: Full tracing of agent thinking, tool calls, and progress
- **Streamlit Web UI**: Interactive visual operation interface

## Architecture

<p align="center"><img src="./assets/images/系统架构图白.png" alt="System Architecture"></p>

## Features

### 🤖 Agent System
- 6 predefined templates: Market Researcher, Data Analyst, Report Writer, Quality Reviewer, Technical Engineer, Strategic Advisor
- Custom agents: arbitrary names, prompts, and capabilities
- State management: idle → initializing → running → completed/failed/cancelled
- Exponential backoff retry + timeout handling
- Metrics tracking: call count, success rate, average latency, token consumption

### 🔧 8 Professional Tools
| Tool | Description | Implementation |
|------|-------------|----------------|
| `web_search` | Search the internet for the latest information | **youdotcom** as example |
| `data_analyzer` | Data analysis (trends/comparison/statistics/SWOT) | Template-based analysis |
| `web_scraper` | Scrape web content and extract text | aiohttp + HTML cleanup |
| `code_executor` | Execute Python/JS code snippets | Sandboxed exec() |
| `report_writer` | Integrate sections into Markdown reports | Template generation |
| `knowledge_base` | Query professional knowledge bases | Domain frameworks |
| `calculator` | Mathematical calculations | Safe eval() |
| `agent_delegate` | Delegate tasks to sub-agents | LLM invocation |

### 🤝 6 Collaboration Modes
1. **Sequential Passing** - Agent A→B→C, each output feeds into the next as input
2. **Parallel Processing** - All agents process simultaneously, results aggregated
3. **Debate Consensus** - Multi-round debate with frequency-based consensus detection
4. **Expert Team** - Research → Analysis → Writing phased pipeline
5. **Critic Review** - Create→Review→Revise loop until approved
6. **Hierarchical Collaboration** - Supervisor decomposes tasks → Subordinates execute → Supervisor synthesizes

## Quick Start

### 1. Install Dependencies

```bash
cd Cornucopia-Multi-Agent  

python3.12 -m venv .venv  
source .venv/bin/activate  

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Create a `.env` file:

```bash
cp .env.example .env
```

Edit the `.env` file:

```env
# qwen3.6-27b API Key (DashScope)
DASHSCOPE_API_KEY=your-dashscope-api-key

# You.com API Key (for web_search tool)
YOU_API_KEY=your-you-api-key

# Server port (optional, default 8000)
PORT=8000
```

### 3. Launch

**CLI Mode** (interactive):
```bash
python main.py
```

**Server Mode** (API + WebSocket):
```bash
python run_server.py
```

**Streamlit Web UI**:
```bash
streamlit run web/streamlit_app.py
```

## API Documentation

After starting the server, visit `http://localhost:8000/docs` for interactive API documentation.

### Main Endpoints

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/sessions` | Create session |
| POST | `/api/sessions/{id}/agents` | Create agent |
| POST | `/api/sessions/{id}/agents/auto-generate` | Auto-generate agents |
| POST | `/api/sessions/{id}/deep-plan` | LLM deep planning |
| POST | `/api/sessions/{id}/cluster-execute` | Cluster execution |
| POST | `/api/sessions/{id}/execute` | Simple execution |
| POST | `/api/sessions/{id}/collaborate` | LLM collaboration |
| POST | `/api/sessions/{id}/workflow-execute` | Dynamic workflow |
| POST | `/api/analyze-complexity` | Task complexity analysis |
| POST | `/api/chat` | Simple chat |
| WS | `/ws?session_id=...` | WebSocket real-time events |

## Project Structure

```
Cornucopia-Multi-Agent/
├── .env                              # Environment config (DashScope API Key / You.com API Key)
├── .gitignore
├── requirements.txt                  # Python dependencies
├── README.md                         # English documentation
├── README_zh.md                      # Chinese documentation
├── main.py                           # CLI entry point (interactive menu)
├── run_server.py                     # FastAPI server startup script
│
├── assets/                           # Static assets
│   └── images/                       #   Logo, architecture diagrams, etc.
│
├── cornucopia/                       # Main source package
│   ├── __init__.py
│   ├── config.py                     # Configuration management (.env loading)
│   ├── logging.py                    # Logging module (loguru wrapper)
│   ├── core/                         # Core modules
│   │   ├── __init__.py
│   │   ├── types.py                  #   Type definitions (dataclass)
│   │   ├── errors.py                 #   Error hierarchy (15 exception classes)
│   │   ├── message.py                #   Message bus (pub/sub)
│   │   └── agent.py                  #   CoAgent core class
│   ├── models/                       # LLM models
│   │   ├── __init__.py
│   │   └── model_factory.py          #   DashScope qwen3.6-27b client
│   ├── tools/                        # 8 tools
│   │   ├── __init__.py
│   │   ├── registry.py               #   Tool registry
│   │   ├── web_search.py             #   🔑 youdotcom search
│   │   ├── data_analyzer.py          #   Data analysis
│   │   ├── web_scraper.py            #   Web scraping
│   │   ├── code_executor.py          #   Code execution
│   │   ├── report_writer.py          #   Report writing
│   │   ├── knowledge_base.py         #   Knowledge base
│   │   ├── calculator.py             #   Calculator
│   │   └── agent_delegate.py         #   Agent delegation
│   ├── memory/                       # Memory system
│   │   ├── __init__.py
│   │   ├── short_term.py             #   Short-term memory (LRU + TTL)
│   │   ├── long_term.py              #   Long-term memory (vector store)
│   │   ├── shared_memory.py          #   Session shared memory
│   │   └── enhanced_shared.py        #   AgentCluster enhanced shared memory
│   ├── collaboration/                # 6 collaboration modes
│   │   ├── __init__.py
│   │   ├── base.py                   #   Collaboration base class
│   │   ├── sequential.py             #   Sequential passing
│   │   ├── parallel.py               #   Parallel processing
│   │   ├── debate.py                 #   Debate consensus
│   │   ├── expert_team.py            #   Expert team
│   │   ├── critic_reviewer.py        #   Critic review
│   │   ├── hierarchical.py           #   Hierarchical collaboration
│   │   └── llm_collaboration.py      #   LLM native collaboration (6 modes)
│   ├── orchestration/                # Orchestration system
│   │   ├── __init__.py
│   │   ├── planner.py                #   Rule-based planner
│   │   ├── evaluator.py              #   Rule-based evaluator
│   │   ├── deep_planner.py           #   LLM deep planner
│   │   ├── deep_evaluator.py         #   LLM deep evaluator
│   │   ├── orchestrator.py           #   Execution orchestrator
│   │   └── agent_cluster.py          #   Cluster execution engine
│   ├── communication/                # Communication structures
│   │   ├── __init__.py
│   │   └── structures.py             #   6 topologies
│   ├── workflow/                     # Dynamic workflow
│   │   ├── __init__.py
│   │   ├── engine.py                 #   Workflow engine
│   │   ├── runtime.py                #   Sandbox runtime
│   │   ├── budget.py                 #   Token budget
│   │   └── structured_output.py      #   JSON Schema
│   ├── server/                       # FastAPI server
│   │   ├── __init__.py
│   │   ├── app.py                    #   Application assembly
│   │   ├── routes.py                 #   17 API routes
│   │   ├── schemas.py                #   Pydantic models
│   │   ├── session.py                #   Session management
│   │   └── websocket.py              #   WebSocket management
│   └── utils/                        # Utilities
│       ├── __init__.py
│       └── result_saver.py           #   Result saving (Markdown / DOCX)
│
├── results/                          # Report output directory
│
├── tests/                            # Test cases
│   ├── test_agent_capabilities.py    #   15 end-to-end capability tests
│   └── test_deep_cluster_report.py   #   Deep cluster dedicated test
│
└── web/                              # Streamlit frontend
    ├── __init__.py
    ├── streamlit_app.py              #   Main application
    └── pages/                        #   5 pages
        ├── 1_simple_execute.py       #     Simple execution
        ├── 2_llm_collaborate.py      #     LLM collaboration
        ├── 3_deep_cluster.py         #     Deep cluster
        ├── 4_workflow.py             #     Dynamic workflow
        └── 5_settings.py             #     System settings
```

## Core Modules

### CoAgent - Core Agent Class

```python
from cornucopia.core.agent import CoAgent
from cornucopia.core.types import AgentConfig

config = AgentConfig(
    name="Market Researcher",
    system_prompt="You are a senior market researcher...",
    max_retries=3,
    timeout=120,
)

agent = CoAgent(config)
result = await agent.execute("Analyze the 2024 China AI market size")
print(result.data["text"])
```

### Deep Cluster Execution

```python
from cornucopia.orchestration.deep_planner import DeepPlanner
from cornucopia.orchestration.agent_cluster import AgentCluster

planner = DeepPlanner()
plan = await planner.create_deep_plan("Comprehensive analysis of China's NEV market")

cluster = AgentCluster()
cluster.on_event(lambda e: print(e.type, e.data))
result = await cluster.execute_plan(plan, max_iterations=3)

print(result.final_output)        # Synthesized report
print(result.evaluation_score)    # Quality score
```

## Tool System

Cornucopia provides **8 professional tools**, managed and dispatched through a unified registry (`cornucopia/tools/registry.py`). All tools use OpenAI function-calling compatible schema definitions and can be seamlessly invoked by agents.

### Tool Registry

```python
from cornucopia.tools.registry import (
    get_tool_function,       # Get callable by name
    get_tool_definition,     # Get tool schema definition by name
    get_tools_for_agent_type,# Get default tool set for agent type
    execute_tool,            # Dispatch execution by name + arguments
)
```

**Agent → Tool Mapping**:

| Agent Type | Available Tools |
|------------|----------------|
| `researcher` | web_search, web_scraper, knowledge_base |
| `analyst` | data_analyzer, calculator, knowledge_base |
| `writer` | report_writer |
| `coder` | code_executor, web_scraper |
| `strategist` | data_analyzer, calculator, knowledge_base |
| `critic` | knowledge_base |
| `supervisor` | agent_delegate, web_search, knowledge_base |
| `general` | web_search, calculator |

## Collaboration Modes

Cornucopia offers **6 collaboration modes**, all inheriting from the `BaseCollaboration` base class with a unified interface `async def execute(input_text: str) -> CollaborationResult`. It also supports **6 communication topologies** (`cornucopia/communication/structures.py`) to control message routing between agents.

1. **Sequential Passing** - Agent A→B→C, each output feeds into the next, chain aborts on any failure
2. **Parallel Processing** - All agents process the same input simultaneously via `asyncio.gather`, results aggregated
3. **Debate Consensus** - Multi-round debate, each round builds on previous arguments, frequency-based consensus detection (default threshold 0.7)
4. **Expert Team** - Research → Analysis → Writing three-stage fixed pipeline
5. **Critic Review** - Create→Review→Revise loop until approved (default max 2 rounds)
6. **Hierarchical Collaboration** - Supervisor decomposes tasks → Round-robin assignment → Subordinates execute in parallel → Supervisor synthesizes

### Communication Topologies

| Topology | Class | Description |
|----------|-------|-------------|
| Single Agent | `SingleAgentCommunication` | Works independently, no connections |
| Network | `NetworkCommunication` | Fully connected peer network, supports `broadcast()` |
| Supervisor | `SupervisorCommunication` | Star topology, Agent 0 issues directives / receives reports |
| Supervisor as Tool | `SupervisorAsToolCommunication` | Agent 0 is primary, others are consultable advisors |
| Hierarchical | `HierarchicalCommunication` | Tree-structured parent-child relationships |
| Custom | `CustomCommunication` | Arbitrary connections via `add_connection()` |

## Execution Paths

### Path 1: Simple Execution
```
User Input → Select Mode → Sequential/Parallel/ExpertTeam → Result
```

### Path 2: LLM Collaboration
```
User Input → Define Agents → Select Mode → Direct LLM Call → Synthesized Output
```

### Path 3: Deep Cluster
```
User Input → DeepPlanner (LLM decomposition) → AgentCluster (tool-calling loop)
           → Heuristic evaluation → replan (weak tasks) → Synthesized report → DeepEvaluator
```

### Path 4: Dynamic Workflow
```
User Input → LLM generates script → Sandbox execution (agent/parallel/pipeline) → Result
```

## Tech Stack

| Component | Technology |
|-----------|-----------|
| LLM | qwen3.6-27b (DashScope OpenAI Compatible) |
| Search | youdotcom (You.com API) |
| Server | FastAPI + Uvicorn |
| Real-time Communication | WebSocket |
| Frontend | Streamlit |
| Data Validation | Pydantic |
| Async | asyncio + aiohttp |

## License

MIT
