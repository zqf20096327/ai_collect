# GenAI Starter Pack: Cloneable GenAI Projects and Hugging Face Spaces

> A curated catalog and structured dataset of 50 open-source GenAI applications and Hugging Face Spaces selected for cloneability, setup clarity, and learning value.

<p align="center">
  <img src="assets/banner.webp" alt="GenAI Starter Pack banner">
</p>

<p align="center">
  <strong>Find practical RAG, AI agent, LangGraph, MCP, and multi-agent projects you can inspect, clone, and learn from.</strong>
</p>

<p align="center">
  <img src="assets/stats-bar.svg" alt="GenAI Starter Pack project stats">
</p>

<p align="center">
  <a href="https://github.com/parthmax2/genai-starter-pack/stargazers"><img src="https://img.shields.io/github/stars/parthmax2/genai-starter-pack?style=flat" alt="GitHub stars"></a>
  <img src="https://img.shields.io/badge/projects-50%20curated-blue" alt="50 curated projects">
  <img src="https://img.shields.io/badge/data-JSON%20%7C%20CSV-2563EB" alt="JSON and CSV datasets">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-CC0--1.0-lightgrey" alt="License: CC0 1.0"></a>
</p>

**50 curated projects** | **JSON and CSV datasets** | **Setup-time estimates** | **9 category guides**

[Browse the ranked projects](#best-generative-ai-projects) · [Follow the learning path](docs/learning-path.md) · [Read the methodology](docs/ranking-methodology.md) · [Use the JSON dataset](data/projects.json)

Most entries are Hugging Face Spaces, which are Git repositories that can usually be cloned directly. The catalog focuses on practical LLM applications across **RAG, Agentic AI, Multi-Agent Systems, LangGraph, CrewAI, SmolAgents, MCP, Browser Agents, Coding Agents, Research Agents, PDF RAG, Knowledge Assistants, and AI Workflows.**

Unlike popularity-only lists, this repository evaluates projects for developer usefulness: cloneability, documentation quality, architecture, learning value, and practical reuse.

<p align="center">
  <img src="assets/category-dashboard.svg" alt="Category dashboard for GenAI project areas">
</p>

## Table of Contents

- [How to Use This Repository](#how-to-use-this-repository)
- [Explore the Starter Pack](#explore-the-starter-pack)
- [Why This Exists](#why-this-exists)
- [Quick Picks](#quick-picks)
- [Ranking Method](#ranking-method)
- [Best Generative AI Projects](#best-generative-ai-projects)
- [Data and Guides](#data)
- [Contributing](#contributing)

## How to Use This Repository

GenAI Starter Pack is a **catalog and dataset**, not an installable application or a single code boilerplate.

1. Choose a category or goal from the guides below.
2. Compare projects by stack, difficulty, setup time, and score.
3. Open a listed Hugging Face Space or source repository and inspect its files.
4. Clone the project you want to study by following the [Hugging Face Spaces cloning guide](docs/guides/how-to-clone-huggingface-spaces.md).
5. Use [projects.json](data/projects.json) or [projects.csv](data/projects.csv) for filtering, analysis, or building your own project browser.

## Explore The Starter Pack

| Path | Best For |
|---|---|
| [Best RAG Projects](docs/categories/rag.md) | Vector search, PDF chatbots, knowledge assistants, retrieval pipelines. |
| [Best Agentic AI Projects](docs/categories/agentic-ai.md) | Tool-using agents, agentic RAG, workflow automation. |
| [Best LangGraph Projects](docs/categories/langgraph.md) | Graph-based agent workflows and state-machine patterns. |
| [Best Multi-Agent Projects](docs/categories/multi-agent.md) | Crew workflows, agent collaboration, AutoGen-style demos. |
| [Best MCP Projects](docs/categories/mcp.md) | Model Context Protocol tools, servers, and app wrappers. |
| [Best Browser Agent Projects](docs/categories/browser-agents.md) | Browser-use agents, web automation, and research browsing workflows. |
| [Best Coding Agent Projects](docs/categories/coding-agents.md) | Code review agents, coding assistants, and developer automation. |
| [Best Research Agent Projects](docs/categories/research-agents.md) | Deep research tools, evaluation boards, and source-gathering agents. |
| [Beginner-Friendly Projects](docs/categories/beginner-friendly.md) | Projects you can clone and understand quickly. |

## Why This Exists

Most AI project lists are either huge link dumps, paper collections, SaaS directories, or popularity rankings. GenAI Starter Pack is built for developers asking:

- What are the best Generative AI projects I can actually clone?
- Which RAG projects are worth studying?
- Where are good LangGraph, CrewAI, SmolAgents, and MCP examples?
- Which AI agent projects are beginner-friendly?
- Which open-source LLM apps can become a foundation for my own product?

## Who This Is For

- Developers looking for the best GenAI projects to clone and learn from.
- Students building RAG, agentic AI, LangGraph, CrewAI, SmolAgents, or MCP portfolios.
- Founders searching for practical open-source LLM app foundations.
- Maintainers who want examples of clean AI project structure, docs, and setup flow.
- Researchers comparing real-world agent, RAG, and multi-agent app patterns.

## What Gets Included

A project should be useful to developers, not just impressive in a demo. Strong candidates usually have:

- Public source code or a cloneable Hugging Face Space.
- Clear setup instructions and realistic local run path.
- Practical architecture worth studying.
- Evidence that the demo or project still works.
- A useful pattern for RAG, agents, workflows, MCP, browser automation, coding agents, or research agents.

Projects with broken runtimes, missing source code, poor documentation, unclear setup, or abandoned structure are filtered out.

## Quick Picks

| Goal | Start Here |
|---|---|
| Learn RAG | [Best RAG Projects](#best-rag-projects) |
| Learn agentic AI | [Best Agentic AI Projects](#best-agentic-ai-projects) |
| Learn LangGraph | [Best LangGraph Projects](#best-langgraph-projects) |
| Learn multi-agent systems | [Best Multi-Agent AI Projects](#best-multi-agent-ai-projects) |
| Learn MCP | [Best MCP Projects](#best-mcp-projects) |
| Build with browser agents | [Best Browser Agent Projects](#best-browser-agent-projects) |
| Start as a beginner | [Beginner-Friendly GenAI Projects](#beginner-friendly-genai-projects) |

## Ranking Method

Projects are ranked by a weighted score — **cloneability matters most**, popularity matters least.

<p align="center">
  <img src="assets/ranking-weight-meter.svg" alt="Ranking weight distribution: Cloneability 40%, Documentation 20%, Architecture 15%, Learning 15%, Popularity 10%">
</p>

| Signal | Weight |
|---|---:|
| Cloneability | 40% |
| Documentation quality | 20% |
| Project architecture | 15% |
| Learning value | 15% |
| Popularity | 10% |

See [Ranking Methodology](docs/ranking-methodology.md) and [Cloneability Score](docs/cloneability-score.md).

## Best Generative AI Projects

| Rank | Project | Category | Stack | Difficulty | Score | Why Study |
|---:|---|---|---|---|---:|---|
| 1 | [Doc MCP](https://huggingface.co/spaces/Agents-MCP-Hackathon/doc-mcp) | Agentic RAG | LlamaIndex, Gradio, MCP | Medium | 87 | Clean MCP + documentation RAG pattern. |
| 2 | [Multi-Agent Land](https://huggingface.co/spaces/build-small-hackathon/multi-agent-lab) | Multi-Agent | Qdrant, FastAPI, Gradio, MCP | Medium | 87 | Rich architecture, tests, docs, configs. |
| 3 | [DeepResearch Bench](https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard) | Research Agent | Gradio | Hard | 78 | Useful benchmark/evaluation reference. |
| 4 | [Qdrant Vibe Coding RAG](https://huggingface.co/spaces/Qdrant/webinar-vibe-coding-rag) | Agentic RAG | Qdrant, FastAPI, MCP | Hard | 83 | Practical vector search app structure. |
| 5 | [Consilium MCP](https://huggingface.co/spaces/Agents-MCP-Hackathon/consilium_mcp) | Research Agent | SmolAgents, Gradio, MCP | Medium | 80 | Multi-source research tools via MCP. |
| 6 | [AI Workflow Orchestrator](https://huggingface.co/spaces/kizabgd123/ai-workflow-orchestrator) | AI Workflow | FastAPI | Hard | 85 | Larger workflow orchestration reference. |
| 7 | [AI Marketing Content Creator](https://huggingface.co/spaces/Agents-MCP-Hackathon/AI-Marketing-Content-Creator) | Knowledge Assistant | FastAPI, Gradio, MCP | Medium | 75 | Good applied MCP business app. |
| 8 | [RAG Chatbot Agentic AI](https://huggingface.co/spaces/KunalShaw/RAG-Chatbot-Agentic-AI) | Agentic RAG | LangGraph, Pinecone, Streamlit | Medium | 80 | LangGraph + Pinecone RAG example. |
| 9 | [Web Scraper](https://huggingface.co/spaces/Agents-MCP-Hackathon/web-scraper) | Browser Agent | Gradio, MCP | Easy | 80 | Simple MCP scraping utility. |
| 10 | [RAG GPT Backend](https://huggingface.co/spaces/merciless-admiral/rag-gpt-backend) | Agentic RAG | FAISS, Pinecone, FastAPI, Gradio | Hard | 83 | Backend-style RAG service pattern. |
| 11 | [PDF Chatbot](https://huggingface.co/spaces/cvachet/pdf-chatbot) | PDF RAG | ChromaDB, Gradio | Easy | 85 | Very cloneable PDF chatbot baseline. |
| 12 | [Multi-Agent Deep Research](https://huggingface.co/spaces/Agents-MCP-Hackathon/multi-agent_deep-research) | Multi-Agent | Gradio, MCP | Medium | 80 | Focused multi-agent research flow. |
| 13 | [Light PDF Web QA](https://huggingface.co/spaces/seanpedrickcase/Light-PDF-Web-QA-Chatbot) | PDF RAG | FAISS, Gradio | Easy | 88 | Lightweight document + web QA app. |
| 14 | [SmolAgents Quiz](https://huggingface.co/spaces/agents-course/unit2_smolagents_quiz) | Coding Agent | SmolAgents, FastAPI, Gradio | Easy | 80 | Beginner-friendly SmolAgents learning app. |
| 15 | [Open DeepResearch](https://huggingface.co/spaces/AlignAI/Open-Deep-Research) | Research Agent | Streamlit | Medium | 80 | Simple deep-research UI pattern. |
| 16 | [Multi-Agent AI CrewAI](https://huggingface.co/spaces/bstraehle/multi-agent-ai-crewai) | Multi-Agent | CrewAI, Gradio, MCP | Medium | 80 | Compact CrewAI reference. |
| 17 | [QSARion SmolAgents](https://huggingface.co/spaces/alarv/QSARion-smolagents) | Knowledge Assistant | SmolAgents, Gradio | Medium | 75 | Domain agent with practical tool use. |
| 18 | [AI Document Assistant RAG](https://huggingface.co/spaces/samichohan/AI-Document-Assistant-RAG-Chatbot) | PDF RAG | FAISS, Streamlit | Hard | 78 | Recent Streamlit document assistant. |
| 19 | [Universal File Converter](https://huggingface.co/spaces/Agents-MCP-Hackathon/universal-file-converter) | AI Workflow | Gradio, MCP | Medium | 55 | MCP utility workflow example. |
| 20 | [SAM 3D Body MCP](https://huggingface.co/spaces/dev-bjoern/sam3d-body-mcp) | AI Workflow | Gradio, MCP | Easy | 85 | Minimal MCP wrapping of model app. |
| 21 | [AutoGen Coding](https://huggingface.co/spaces/bstraehle/multi-agent-ai-autogen-coding) | Coding Agent | Gradio, MCP | Easy | 80 | Small coding-agent comparison baseline. |
| 22 | [Brand Identity Generator](https://huggingface.co/spaces/MCP-1st-Birthday/Brand-Identity-Generator) | AI Workflow | Gradio, MCP | Medium | 75 | End-to-end content workflow. |
| 23 | [Open Deep Research](https://huggingface.co/spaces/mikeee/open-deep-research) | Browser Agent | SmolAgents, Gradio | Medium | 75 | Browser-style research agent. |
| 24 | [SAM 3D Objects MCP](https://huggingface.co/spaces/dev-bjoern/sam3d-objects-mcp) | AI Workflow | Gradio, MCP | Easy | 85 | Small MCP server/app pattern. |
| 25 | [Multi-Agent AI LangGraph](https://huggingface.co/spaces/bstraehle/multi-agent-ai-langgraph) | Multi-Agent | LangGraph, Gradio, MCP | Medium | 80 | Compact LangGraph multi-agent demo. |
| 26 | [GAIA2 Agents Leaderboard](https://huggingface.co/spaces/meta-agents-research-environments/leaderboard) | Research Agent | Gradio | Easy | 80 | Agent evaluation UI reference. |
| 27 | [Agentic AI](https://huggingface.co/spaces/bstraehle/agentic-ai) | AI Workflow | LlamaIndex, Gradio, MCP | Medium | 80 | LangChain/LlamaIndex agent app. |
| 28 | [RAG QA System](https://huggingface.co/spaces/Dishu27/RAG-QA-System) | PDF RAG | FAISS, FastAPI, Streamlit | Hard | 83 | FastAPI + Streamlit RAG split. |
| 29 | [Rice KG RAG QA](https://huggingface.co/spaces/eesaiye/rice-rag-qa) | Agentic RAG | FAISS, Gradio | Easy | 80 | Knowledge-graph flavored RAG. |
| 30 | [Lowerlimb RAG Agentic AI](https://huggingface.co/spaces/GunturDoc2025/unified-lowerlimb-rag-agentic-ai) | PDF RAG | LangGraph, FAISS, Gradio | Medium | 80 | Domain-specific LangGraph RAG. |
| 31 | [Upperlimb RAG Agentic AI](https://huggingface.co/spaces/ushagandi2026/unified-upperlimb-rag-agentic-ai) | PDF RAG | LangGraph, FAISS, Gradio | Medium | 80 | Similar medical RAG pattern. |
| 32 | [LangGraph Chess](https://huggingface.co/spaces/bstraehle/multi-agent-ai-langgraph-chess) | Multi-Agent | LangGraph, Gradio, MCP | Medium | 80 | Toy multi-agent state-machine demo. |
| 33 | [Rembg MCP](https://huggingface.co/spaces/hysts-mcp/rembg) | AI Workflow | FastAPI, Gradio, MCP | Easy | 80 | Simple MCP tool wrapping pattern. |
| 34 | [FLUX.1 Krea Dev MCP](https://huggingface.co/spaces/mcp-tools/FLUX.1-Krea-dev) | AI Workflow | Gradio, MCP | Easy | 80 | Image-generation MCP app shell. |
| 35 | [RAG PDF Chatbot](https://huggingface.co/spaces/MuntasirHossain/RAG-PDF-Chatbot) | PDF RAG | FAISS, Gradio | Easy | 65 | Popular minimal PDF RAG. |
| 36 | [Unit 3 Agentic RAG](https://huggingface.co/spaces/agents-course/Unit_3_Agentic_RAG) | Agentic RAG | SmolAgents, Gradio | Easy | 65 | Course-quality agentic RAG example. |
| 37 | [AutoGen Chess](https://huggingface.co/spaces/bstraehle/multi-agent-ai-autogen-chess) | Multi-Agent | Gradio, MCP | Easy | 80 | Small multi-agent comparison app. |
| 38 | [MCP Plausible](https://huggingface.co/spaces/azettl/mcp-plausible) | AI Workflow | Gradio, MCP | Easy | 80 | API analytics via MCP. |
| 39 | [LangGraph Code Reviewer](https://huggingface.co/spaces/jstoppa/langgraph_agent_code_reviewer) | Coding Agent | LangGraph, Gradio | Easy | 80 | Tiny, readable LangGraph agent. |
| 40 | [AutoGen Coding Fork](https://huggingface.co/spaces/harry85/multi-agent-ai-autogen-coding) | Coding Agent | Gradio | Easy | 80 | Cloneable coding-agent variant. |
| 41 | [Production RAG](https://huggingface.co/spaces/TharaKavin/Production_Rag) | Agentic RAG | ChromaDB, Gradio | Medium | 80 | Larger Chroma RAG project shape. |
| 42 | [PDF RAG Mistral 7B](https://huggingface.co/spaces/qfisch/pdf-rag-mistral-7b) | PDF RAG | ChromaDB, Gradio | Easy | 80 | Simple local-model PDF RAG. |
| 43 | [RAG PDF QnA ChatBot](https://huggingface.co/spaces/Mr-TD/RAG-PDF-QnA-ChatBot) | PDF RAG | FAISS, Streamlit | Easy | 65 | Streamlit PDF Q&A baseline. |
| 44 | [SmolAgents Gradio](https://huggingface.co/spaces/roychen22/smolagents-gradio) | Knowledge Assistant | SmolAgents, Gradio | Easy | 80 | Minimal SmolAgents Gradio shell. |
| 45 | [AutoGen Coding Variant](https://huggingface.co/spaces/sosa123454321/multi-agent-ai-autogen-coding) | Coding Agent | Gradio | Easy | 80 | Small fork for comparison. |
| 46 | [AutoGen Coding Variant 2](https://huggingface.co/spaces/sohoso/multi-agent-ai-autogen-coding) | Coding Agent | Gradio | Easy | 80 | Another minimal coding-agent fork. |
| 47 | [Browser Calling Agent](https://huggingface.co/spaces/Arnavkumar01/browser_calling_Agent) | Browser Agent | FastAPI, Gradio | Hard | 68 | Browser-calling app pattern. |
| 48 | [CrewAI Finance Agent](https://huggingface.co/spaces/itsJB/CREWAI_LLAMA3.1_FINANACE_AGENT) | Multi-Agent | CrewAI, Streamlit | Medium | 65 | CrewAI applied finance example. |
| 49 | [Julia Browser Agent](https://huggingface.co/spaces/rootxhacker/Julia-browser-Agent) | Browser Agent | Gradio | Medium | 65 | Small browser-agent baseline. |
| 50 | [Career Conversation AI Agent](https://huggingface.co/spaces/rajeswarandhandapani/career-conversation-AI-agent-chatbot) | Knowledge Assistant | OpenAI Agents SDK, Gradio | Medium | 67 | Simple OpenAI Agents SDK app. |

## Best RAG Projects

See the full guide: [Best RAG Projects](docs/categories/rag.md).

1. [Doc MCP](https://huggingface.co/spaces/Agents-MCP-Hackathon/doc-mcp)
2. [Qdrant Vibe Coding RAG](https://huggingface.co/spaces/Qdrant/webinar-vibe-coding-rag)
3. [RAG Chatbot Agentic AI](https://huggingface.co/spaces/KunalShaw/RAG-Chatbot-Agentic-AI)
4. [RAG GPT Backend](https://huggingface.co/spaces/merciless-admiral/rag-gpt-backend)
5. [PDF Chatbot](https://huggingface.co/spaces/cvachet/pdf-chatbot)
6. [Light PDF Web QA](https://huggingface.co/spaces/seanpedrickcase/Light-PDF-Web-QA-Chatbot)
7. [AI Document Assistant RAG](https://huggingface.co/spaces/samichohan/AI-Document-Assistant-RAG-Chatbot)
8. [RAG QA System](https://huggingface.co/spaces/Dishu27/RAG-QA-System)
9. [Rice KG RAG QA](https://huggingface.co/spaces/eesaiye/rice-rag-qa)
10. [Unit 3 Agentic RAG](https://huggingface.co/spaces/agents-course/Unit_3_Agentic_RAG)

## Best Agentic AI Projects

See the full guide: [Best Agentic AI Projects](docs/categories/agentic-ai.md).

1. [Doc MCP](https://huggingface.co/spaces/Agents-MCP-Hackathon/doc-mcp)
2. [Multi-Agent Land](https://huggingface.co/spaces/build-small-hackathon/multi-agent-lab)
3. [Consilium MCP](https://huggingface.co/spaces/Agents-MCP-Hackathon/consilium_mcp)
4. [Multi-Agent Deep Research](https://huggingface.co/spaces/Agents-MCP-Hackathon/multi-agent_deep-research)
5. [Multi-Agent AI CrewAI](https://huggingface.co/spaces/bstraehle/multi-agent-ai-crewai)
6. [Multi-Agent AI LangGraph](https://huggingface.co/spaces/bstraehle/multi-agent-ai-langgraph)
7. [Agentic AI](https://huggingface.co/spaces/bstraehle/agentic-ai)
8. [Unit 3 Agentic RAG](https://huggingface.co/spaces/agents-course/Unit_3_Agentic_RAG)
9. [RAG Chatbot Agentic AI](https://huggingface.co/spaces/KunalShaw/RAG-Chatbot-Agentic-AI)
10. [QSARion SmolAgents](https://huggingface.co/spaces/alarv/QSARion-smolagents)

## Best LangGraph Projects

See the full guide: [Best LangGraph Projects](docs/categories/langgraph.md).

The initial research pass selected 8 LangGraph Spaces with enough public source and documentation quality for this guide.

1. [RAG Chatbot Agentic AI](https://huggingface.co/spaces/KunalShaw/RAG-Chatbot-Agentic-AI)
2. [Multi-Agent AI LangGraph](https://huggingface.co/spaces/bstraehle/multi-agent-ai-langgraph)
3. [Lowerlimb RAG Agentic AI](https://huggingface.co/spaces/GunturDoc2025/unified-lowerlimb-rag-agentic-ai)
4. [Upperlimb RAG Agentic AI](https://huggingface.co/spaces/ushagandi2026/unified-upperlimb-rag-agentic-ai)
5. [LangGraph Chess](https://huggingface.co/spaces/bstraehle/multi-agent-ai-langgraph-chess)
6. [LangGraph Code Reviewer](https://huggingface.co/spaces/jstoppa/langgraph_agent_code_reviewer)
7. [Tool Calling Agent LangGraph](https://huggingface.co/spaces/pratikmurali/LangGraph_agent)
8. [LangGraph Basic Example API](https://huggingface.co/spaces/jstoppa/langgraph_basic_example_api)

## Best Multi-Agent AI Projects

See the full guide: [Best Multi-Agent Projects](docs/categories/multi-agent.md).

1. [Multi-Agent Land](https://huggingface.co/spaces/build-small-hackathon/multi-agent-lab)
2. [Multi-Agent Deep Research](https://huggingface.co/spaces/Agents-MCP-Hackathon/multi-agent_deep-research)
3. [Multi-Agent AI CrewAI](https://huggingface.co/spaces/bstraehle/multi-agent-ai-crewai)
4. [Multi-Agent AI LangGraph](https://huggingface.co/spaces/bstraehle/multi-agent-ai-langgraph)
5. [LangGraph Chess](https://huggingface.co/spaces/bstraehle/multi-agent-ai-langgraph-chess)
6. [AutoGen Chess](https://huggingface.co/spaces/bstraehle/multi-agent-ai-autogen-chess)
7. [CrewAI Finance Agent](https://huggingface.co/spaces/itsJB/CREWAI_LLAMA3.1_FINANACE_AGENT)
8. [AutoGen Coding](https://huggingface.co/spaces/bstraehle/multi-agent-ai-autogen-coding)
9. [Consilium MCP](https://huggingface.co/spaces/Agents-MCP-Hackathon/consilium_mcp)
10. [DeepResearch Bench](https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard)

## Best MCP Projects

See the full guide: [Best MCP Projects](docs/categories/mcp.md).

- [Doc MCP](https://huggingface.co/spaces/Agents-MCP-Hackathon/doc-mcp)
- [Multi-Agent Land](https://huggingface.co/spaces/build-small-hackathon/multi-agent-lab)
- [Consilium MCP](https://huggingface.co/spaces/Agents-MCP-Hackathon/consilium_mcp)
- [Web Scraper](https://huggingface.co/spaces/Agents-MCP-Hackathon/web-scraper)
- [Rembg MCP](https://huggingface.co/spaces/hysts-mcp/rembg)
- [MCP Plausible](https://huggingface.co/spaces/azettl/mcp-plausible)

## Best Browser Agent Projects

See the full guide: [Best Browser Agents](docs/categories/browser-agents.md).

- [Web Scraper](https://huggingface.co/spaces/Agents-MCP-Hackathon/web-scraper)
- [Open Deep Research](https://huggingface.co/spaces/mikeee/open-deep-research)
- [Browser Calling Agent](https://huggingface.co/spaces/Arnavkumar01/browser_calling_Agent)
- [Julia Browser Agent](https://huggingface.co/spaces/rootxhacker/Julia-browser-Agent)

## Best Coding Agent Projects

See the full guide: [Best Coding Agents](docs/categories/coding-agents.md).

- [SmolAgents Quiz](https://huggingface.co/spaces/agents-course/unit2_smolagents_quiz)
- [AutoGen Coding](https://huggingface.co/spaces/bstraehle/multi-agent-ai-autogen-coding)
- [LangGraph Code Reviewer](https://huggingface.co/spaces/jstoppa/langgraph_agent_code_reviewer)
- [AutoGen Coding Fork](https://huggingface.co/spaces/harry85/multi-agent-ai-autogen-coding)

## Best Research Agent Projects

See the full guide: [Best Research Agents](docs/categories/research-agents.md).

- [DeepResearch Bench](https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard)
- [Consilium MCP](https://huggingface.co/spaces/Agents-MCP-Hackathon/consilium_mcp)
- [Open DeepResearch](https://huggingface.co/spaces/AlignAI/Open-Deep-Research)
- [Multi-Agent Deep Research](https://huggingface.co/spaces/Agents-MCP-Hackathon/multi-agent_deep-research)

## Beginner-Friendly GenAI Projects

See the full guide: [Beginner-Friendly Projects](docs/categories/beginner-friendly.md).

1. [PDF Chatbot](https://huggingface.co/spaces/cvachet/pdf-chatbot)
2. [Light PDF Web QA](https://huggingface.co/spaces/seanpedrickcase/Light-PDF-Web-QA-Chatbot)
3. [Web Scraper](https://huggingface.co/spaces/Agents-MCP-Hackathon/web-scraper)
4. [SmolAgents Quiz](https://huggingface.co/spaces/agents-course/unit2_smolagents_quiz)
5. [SmolAgents Gradio](https://huggingface.co/spaces/roychen22/smolagents-gradio)
6. [LangGraph Code Reviewer](https://huggingface.co/spaces/jstoppa/langgraph_agent_code_reviewer)
7. [RAG PDF Chatbot](https://huggingface.co/spaces/MuntasirHossain/RAG-PDF-Chatbot)
8. [PDF RAG Mistral 7B](https://huggingface.co/spaces/qfisch/pdf-rag-mistral-7b)
9. [Rice KG RAG QA](https://huggingface.co/spaces/eesaiye/rice-rag-qa)
10. [MCP Plausible](https://huggingface.co/spaces/azettl/mcp-plausible)

## Data

- [JSON dataset](data/projects.json)
- [CSV dataset](data/projects.csv)

## Guides

- [Learning Path](docs/learning-path.md)
- [GenAI Stack Guide](docs/stacks.md)
- [Project Use Cases](docs/use-cases.md)
- [Project Evaluation Template](docs/project-template.md)
- [How to Clone Hugging Face Spaces](docs/guides/how-to-clone-huggingface-spaces.md)
- [Local Setup Checklist](docs/guides/local-setup-checklist.md)
- [Brand and Visual Assets](assets/README.md)

## Contributing

High-quality submissions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request.

The goal is quality over quantity. This repo is for cloneable, useful, educational GenAI projects, not random demos or product ads.


## Maintainer

Built and maintained by **Saksham Pathak** ([parthmax](https://github.com/parthmax2)).

<div align="center">

<a href="https://github.com/parthmax2/genai-starter-pack/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=parthmax2/genai-starter-pack" />
</a>

**The clues are scattered. The models are waiting.
The investigation starts here.**

Welcome to the GenAI Starter Pack.

</div>
<div align="center">

| <img src="https://cdn.simpleicons.org/googlechrome" width="24"><br><b>Website</b><br><a href="https://parthmax.in">parthmax.in</a> | <img src="https://cdn.simpleicons.org/github" width="24"><br><b>GitHub</b><br><a href="https://github.com/parthmax2">@parthmax2</a> | <img src="https://cdn.simpleicons.org/huggingface" width="24"><br><b>Hugging Face</b><br><a href="https://huggingface.co/parthmax">@parthmax</a> | <img src="https://cdn.simpleicons.org/linkedin" width="24"><br><b>LinkedIn</b><br><a href="https://linkedin.com/in/sakshampathak">Saksham Pathak</a> |
|:---:|:---:|:---:|:---:|

</div>

## License

This catalog is released under [CC0 1.0](LICENSE). Project code linked from this list keeps its own license.
