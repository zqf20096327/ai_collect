# AI Agentic Patterns

![AI Bootcamp Open Graph preview](https://www.learnwithparam.com/ai-bootcamp/opengraph-image)

**AI Agent Patterns** for bootcamp students. Each pattern is a single, focused file demonstrating core agentic AI concepts. **Provider-agnostic** - works with 100+ LLM providers via litellm (Ollama, OpenAI, Gemini, Claude, Mistral, and more). Switch providers with a single environment variable - no code changes needed!

> Regional pricing is available for eligible learners, with discounts of up to 60% in supported regions. Start here: https://www.learnwithparam.com/ai-bootcamp

## 🚀 Quick Start

```bash
# 1. Setup
make setup

# 2. Configure LLM provider (or use Ollama locally - no API key needed)
cp env.example .env
# Edit .env and set LITELLM_MODEL (e.g., 'ollama/llama3.2' or 'openai/gpt-4')
# Add API keys for cloud providers if needed

# 3. Run all patterns
make run

# 4. Or run individual patterns
python patterns/01_prompt_chaining.py
python patterns/02_routing.py
python patterns/03_parallelization.py
```

## 📁 All AI Agentic Patterns

### 🏗️ Foundation Patterns (1-8)
- **01_prompt_chaining.py** - Chain prompts together
  - *Automated RFP writer that extracts requirements from client brief → summarizes key needs → generates full proposal draft with cover letter and deliverables*
  - *FAQ summarizer that extracts answers from docs → reformats → writes human-friendly version*
- **02_routing.py** - Route requests to different handlers  
  - *Customer service triage that routes incoming messages to "refunds", "shipping", or "technical" LLM sub-agents for specialized responses*
  - *In-app chatbot that detects sentiment → routes angry users to human escalation pipeline*
- **03_parallelization.py** - Run multiple LLM calls in parallel
  - *SEO content pipeline that generates meta title, meta description, blog intro, and social post captions simultaneously*
  - *Resume enhancer that parallel-generates versions optimized for LinkedIn, ATS, and portfolio*
- **04_reflection.py** - Use reflection to improve code/output quality
  - *Autonomous code reviewer that generates code → reviews it for style/performance → regenerates improved version*
  - *Blog summarizer that re-evaluates tone ("too formal?" → "rewrite in friendlier tone")*
- **05_tool_calling.py** - Use tools with LLMs (Native Function Calling)
  - *Smart operations assistant that can fetch Jira tickets, query database metrics, and trigger Slack updates via tool APIs*
  - *Calendar assistant that uses a "schedule" tool to book meetings from natural text*
  - *Real-world example: REST Countries API integration for country information*
- **06_planning.py** - Break down complex tasks into plans
  - *Marketing campaign planner that creates multi-step plan with timelines and assets needed for "launch new product" goal*
  - *Travel planner that turns "3 days in Rome" into structured itinerary*
- **07_multi_agent.py** - Coordinate multiple AI agents
  - *AI newsroom with reporter agent drafting story → editor agent refining tone → fact-checker agent verifying sources*
  - *Video creation bot with separate agents for script, voiceover, and thumbnail*
- **08_memory_management.py** - Manage conversation memory and context
  - *AI career coach that remembers user's goals, prior feedback, and performance over time to offer context-aware coaching*
  - *Customer chatbot that remembers user preferences (size, brand, last order)*

### 🔧 Advanced Patterns (10-16)
- **10_mcp.py** - Use external tools via Model Context Protocol (Real MCP Servers)
  - *Enterprise assistant that interacts with CRM, internal wiki, and file servers securely via standardized protocol*
  - *AI that can query Notion, Jira, and Google Drive seamlessly using MCP connectors*
  - *Real examples: Filesystem MCP server, Git MCP server*
- **11_goal_setting.py** - Set goals and monitor progress
  - *Sales enablement AI that sets quarterly sales targets, tracks progress, and suggests next best actions*
  - *Habit tracker AI that checks daily progress and adjusts reminders dynamically*
- **12_exception_handling.py** - Handle exceptions and recover gracefully
  - *Financial automation bot that handles failed API calls or invalid data by retrying, alerting, or falling back to cached data*
  - *Chatbot that detects "API unavailable" and apologizes with an alternate response*
- **13_human_in_loop.py** - Integrate human oversight and intervention
  - *Legal AI that drafts contracts and flags ambiguous clauses for lawyer review*
  - *Social media moderator AI that sends uncertain posts to a human for manual approval*
- **14_knowledge_retrieval.py** - Retrieve and use domain knowledge
  - *Customer success AI that answers queries using company-specific knowledge base + recent case studies*
  - *AI that looks up specific product specs or FAQ answers before replying*
- **15_inter_agent_communication.py** - Enable communication between agents
  - *Smart factory system where maintenance agent reports sensor issues → logistics agent orders parts → scheduler agent delays affected lines*
  - *Fitness coach AI coordinating with nutrition agent to align meal and workout plans*
- **16_resource_optimization.py** - Optimize compute/resources
  - *Multi-tenant AI SaaS that dynamically adjusts LLM model size based on user tier or query complexity*
  - *Chatbot that uses GPT-4 for "creative writing" and GPT-3.5 for "FAQ lookup"*

### 🧠 Reasoning Patterns (17a-17c)
- **17a_chain_of_thought.py** - Show reasoning steps
  - *AI math grader that solves student problem step-by-step and checks each reasoning step*
  - *Expense classifier showing reasoning for why a transaction is "travel" vs "meals"*
- **17b_self_correction.py** - Self-validation and repair
  - *Codegen AI that generates script → runs unit test → debugs based on output automatically*
  - *Text summarizer that re-checks if summary misses any key entity*
- **17c_problem_decomposition.py** - Break complex problems into parts
  - *Startup advisor AI that breaks "launch a product" into market research, MVP, and growth phases*
  - *Homework helper that splits a multi-step word problem before solving*

### 🛡️ Safety & Quality Patterns (18-19b)
- **18_guardrails.py** - Implement content/policy filters
  - *AI writing assistant that filters confidential data, PII, or bias-inducing terms before output*
  - *Prevents profanity or misinformation in AI-generated tweets*
- **19a_evaluation.py** - Evaluate LLM output
  - *AI tutor QA system that grades AI explanations based on clarity, correctness, and engagement*
  - *Automated prompt evaluator scoring outputs for fluency and factuality*
- **19b_monitoring.py** - Monitor agent performance
  - *AI customer support dashboard that tracks response latency, satisfaction scores, and escalation rates*
  - *Alerts when AI's error rate exceeds threshold or response time spikes*

### 📊 Management Patterns (20-22)
- **20_prioritization.py** - Manage task queues
  - *AI ops scheduler that prioritizes background jobs based on urgency, dependency, and ROI*
  - *Email assistant that prioritizes unread emails by importance (CEO > newsletter)*
- **21_exploration_discovery.py** - Explore unknowns
  - *R&D assistant that finds unexplored research areas and relevant citations automatically*
  - *News summarizer that surfaces trending but underreported stories*
- **22_pydantic_validation.py** - Data schema validation
  - *LLM data ingestion pipeline that validates structured outputs (JSON, schema-bound fields) before storing*
  - *API wrapper that ensures AI responses fit a strict ProductSchema*

### 🚀 System Patterns (23-28)
- **23_agentic_rag.py** - Agentic retrieval-augmented generation
  - *Corporate knowledge AI that fetches from internal docs, emails, and dashboards, then synthesizes actionable insight*
  - *AI that answers "What did we discuss last meeting?" by retrieving meeting notes*
- **24_workflow_orchestration.py** - Orchestrate complex flows
  - *Automated video production system with script writer → voiceover → visual generation → upload*
  - *Job application AI that drafts resume → tailors cover letter → applies automatically*
- **25_subgraphs.py** - Modular AI components
  - *AI architecture library with reusable subgraphs for parsing input, enriching context, and output formatting*
  - *Plug-in LLM component that handles summarization across different workflows*
- **26_state_machines.py** - Finite state workflow logic
  - *Loan processing system that transitions between "application submitted → under review → approved → funded"*
  - *Conversational flow that tracks user from greeting → query → solution → feedback*
- **27_recursive_agents.py** - Self-referencing reasoning
  - *Research planner AI that recursively delegates subtasks like literature review → summarization → synthesis*
  - *Debugging AI that recursively investigates root causes in logs*
- **28_code_execution.py** - Safely run generated code
  - *Data analyst copilot that generates code to compute KPIs, runs safely in sandbox, and returns results*
  - *Spreadsheet assistant that writes & executes formulas based on user queries*

### 🔄 RAG Pipeline Patterns
- **29_query_rewriter.py** - Rewrite and optimize queries for better retrieval
  - *Search engine that rewrites user queries to improve results: "how to code" → "Python programming tutorial for beginners"*
  - *Customer support that expands vague questions into specific, actionable queries*
- **30_relevancy_check.py** - Check and filter relevant information
  - *Content moderation system that scores articles for relevance to user interests*
  - *Research assistant that filters academic papers by relevance to research topic*
- **31_data_processing.py** - Process and structure data for RAG systems
  - *Document processor that cleans, chunks, and structures PDFs for knowledge base*
  - *Data pipeline that transforms raw text into searchable, categorized content*
- **32_plan_executor.py** - Execute structured plans with monitoring
  - *Project management AI that breaks down tasks into steps and tracks progress*
  - *Workflow automation that executes complex business processes step-by-step*
- **33_anonymization.py** - Anonymize and de-anonymize data for privacy
  - *Healthcare system that removes patient names while preserving medical data*
  - *Customer data processor that anonymizes PII for analytics while maintaining reversibility*

### 🧠 Advanced Agentic Architectures (34-46)
- **34_react.py** - Reason + Act Loop (ReAct)
  - *Customer support AI that reasons through issues step-by-step, queries database for answers, and takes live actions (e.g., refund, escalate, notify user)*
  - *Data-cleaning agent that identifies problem entries, applies fixes, then verifies results dynamically*
- **35_pev.py** - Plan–Execute–Verify (PEV)
  - *Financial trading bot that plans trades, executes safely, and verifies profit/loss outcomes before next cycle*
  - *DevOps AI that deploys updates → tests functionality → rolls back automatically if verification fails*
- **36_blackboard.py** - Collaborative Multi-Agent Blackboard
  - *Research assistant system where multiple domain agents (e.g., legal, financial, tech) post and refine shared insights in a central memory board*
  - *Bug-triage AI where analysis, fix, and QA agents collaborate on one shared state to converge on a solution*
- **37_episodic_semantic_memory.py** - Dual Memory: Episodic + Semantic
  - *AI tutor that recalls what topics a student struggled with (episodic) while leveraging structured knowledge (semantic) for tailored lessons*
  - *Personal assistant that remembers past interactions and learns factual context like birthdays, preferences, or goals*
- **38_tree_of_thoughts.py** - Tree of Thoughts (ToT) Reasoning
  - *Strategic planner that explores multiple reasoning paths for a problem (e.g., marketing strategies) and picks the most optimal route*
  - *Problem-solver that branches reasoning alternatives, evaluates partial outcomes, and merges best insights*
- **39_mental_loop.py** - Internal Simulation Loop
  - *Robot controller that simulates movements or actions internally before committing to real-world execution*
  - *Financial decision engine that runs "mental" dry-runs of portfolio changes before actual trades*
- **40_meta_controller.py** - Meta-Agent Task Router
  - *AI manager that routes incoming requests to best-fit specialist agents (e.g., "analytics", "design", "sales")*
  - *Multi-department enterprise assistant that orchestrates and supervises agents across different workflows*
- **41_graph_memory.py** - Graph-Structured World Model
  - *Research summarizer that extracts entities and relations (people, projects, papers) into a knowledge graph*
  - *Customer insight AI that links interactions, purchases, and feedback in a connected data graph for richer reasoning*
- **42_ensemble.py** - Ensemble of Experts
  - *Content generator that combines outputs from multiple expert AIs (tone, grammar, SEO) before final synthesis*
  - *Decision engine that aggregates recommendations from several models and selects the most consistent result*
- **43_dry_run.py** - Dry-Run Simulation Harness
  - *Financial AI that simulates trades or investment decisions and requires approval before live execution*
  - *Operations assistant that runs workflow simulations to validate downstream safety before deployment*
- **44_rlhf.py** - Reinforcement Learning from Human Feedback
  - *Content generation system that continuously improves responses based on human ratings and feedback loops*
  - *Customer interaction AI that refines tone and accuracy using user satisfaction scores*
- **45_cellular_automata.py** - Local Interaction → Global Behavior
  - *Traffic optimizer where each vehicle agent reacts locally (speed, distance) to produce smooth flow system-wide*
  - *Urban planning simulator where thousands of micro-agents self-organize housing, transport, and energy networks*
- **46_reflexive_metacognitive.py** - Self-Aware and Self-Evaluating Agent
  - *Medical assistant AI that measures its confidence per diagnosis and automatically escalates uncertain cases to human experts*
  - *Customer service bot that knows when it's unsure or stuck and requests clarification or human takeover*

## 🔧 Provider Configuration

### Provider-Agnostic Design

All patterns use **litellm** as a unified abstraction layer. **Switch providers with a single environment variable** - no code changes needed!

### Quick Setup

1. **Ollama (Recommended for local testing - No API key needed)**:
   ```bash
   # Install Ollama: https://ollama.ai
   ollama pull llama3.2
   ollama serve
   
   # In .env:
   LITELLM_MODEL=ollama/llama3.2
   ```

2. **OpenAI**:
   ```bash
   # In .env:
   LITELLM_MODEL=openai/gpt-4
   OPENAI_API_KEY=your_key_here
   ```

3. **Google Gemini (Free tier available)**:
   ```bash
   # In .env:
   LITELLM_MODEL=gemini/gemini-1.5-flash
   GOOGLE_API_KEY=your_key_here
   ```

4. **Other Providers**:
   ```bash
   # Mistral
   LITELLM_MODEL=mistral/mistral-small
   MISTRAL_API_KEY=your_key_here
   
   # Anthropic Claude
   LITELLM_MODEL=anthropic/claude-3-sonnet-20240229
   ANTHROPIC_API_KEY=your_key_here
   
   # Fireworks AI
   LITELLM_MODEL=fireworks/accounts/fireworks/models/llama-v3p1-8b-instruct
   FIREWORKS_API_KEY=your_key_here
   ```

### Switching Providers

**To switch providers, just change `LITELLM_MODEL` in your `.env` file:**
- `LITELLM_MODEL=ollama/llama3.2` → Use Ollama
- `LITELLM_MODEL=openai/gpt-4` → Use OpenAI
- `LITELLM_MODEL=gemini/gemini-1.5-flash` → Use Gemini

**No code changes needed!** All patterns work identically across all providers.

See `env.example` for complete configuration options.

## 💡 What You'll Learn

### 🏗️ Foundation Concepts
1. **Prompt Chaining** - Break complex tasks into steps
2. **Routing** - Smart delegation based on request type
3. **Parallelization** - Speed up multiple LLM calls
4. **Reflection** - Improve code quality through self-review
5. **Tool Calling** - Use external tools with LLMs
6. **Planning** - Break down complex tasks into structured plans
7. **Multi-Agent** - Coordinate multiple specialized agents
8. **Memory Management** - Manage conversation context and user preferences

### 🔧 Advanced Techniques
10. **MCP** - Connect to external tools via Model Context Protocol
11. **Goal Setting** - Set and track progress toward objectives
12. **Exception Handling** - Handle errors and recover gracefully
13. **Human-in-the-Loop** - Integrate human oversight and intervention
14. **Knowledge Retrieval** - Use RAG for better responses
15. **Inter-Agent Communication** - Enable agents to work together
16. **Resource Optimization** - Optimize for cost vs performance

### 🧠 Reasoning & Problem Solving
17a. **Chain-of-Thought** - Step-by-step reasoning process
17b. **Self-Correction** - Review and improve solutions
17c. **Problem Decomposition** - Break down complex problems

### 🛡️ Safety & Quality Assurance
18. **Guardrails** - Implement safety and content filtering
19a. **Evaluation** - Assess AI response quality and safety
19b. **Monitoring** - Track performance and behavior metrics

### 📊 Management & Organization
20. **Prioritization** - Manage tasks and workload intelligently
21. **Exploration & Discovery** - Research and knowledge discovery
22. **Pydantic Validation** - Type-safe data validation

### 🚀 System Architecture
23. **Agentic RAG** - Intelligent retrieval-augmented generation
24. **Workflow Orchestration** - Coordinate complex AI workflows
25. **Subgraphs** - Create modular, reusable components
26. **State Machines** - Implement event-driven agent behavior
27. **Recursive Agents** - Build self-referencing AI systems
28. **Code Execution** - Safely execute code with AI agents

### 🔄 RAG Pipeline Patterns
29. **Query Rewriter** - Rewrite and optimize queries for better retrieval
30. **Relevancy Check** - Check and filter relevant information
31. **Data Processing** - Process and structure data for RAG systems
32. **Plan Executor** - Execute structured plans with monitoring
33. **Anonymization** - Anonymize and de-anonymize data for privacy

### 🧠 Advanced Agentic Architectures
34. **ReAct** - Dynamic reasoning and action loops
35. **PEV** - Plan-Execute-Verify workflows
36. **Blackboard Systems** - Multi-agent collaboration
37. **Episodic + Semantic Memory** - Dual-memory systems
38. **Tree of Thoughts** - Systematic reasoning exploration
39. **Mental Loop** - Simulation before execution
40. **Meta-Controller** - Intelligent task routing
41. **Graph Memory** - Structured knowledge storage
42. **Ensemble** - Multiple perspective analysis
43. **Dry-Run Harness** - Safety-critical execution
44. **RLHF** - Self-improvement through feedback
45. **Cellular Automata** - Emergent behavior systems
46. **Reflexive Metacognitive** - Self-aware AI systems

## 🎯 Supported Providers (100+ via litellm)

**All providers work identically** - same code, same interface, just change `LITELLM_MODEL`:

- **Ollama** - Local models (no API key needed) - Recommended for testing
- **OpenAI** - GPT-4, GPT-3.5-turbo, and more
- **Google Gemini** - Free tier available (gemini-1.5-flash, gemini-1.5-pro)
- **Anthropic Claude** - Claude 3 Sonnet, Opus, and more
- **Mistral** - European models (mistral-small, mistral-large)
- **Fireworks AI** - Fast inference models
- **And 100+ more** - See [litellm providers](https://docs.litellm.ai/docs/providers)

**Provider-agnostic design**: Switch providers with one environment variable. No code changes needed!

## 📚 Learning Approach

**Each pattern is a single, focused file** - perfect for bootcamp students:

- ✅ **One concept per file** - No cognitive overload
- ✅ **Self-contained** - Each pattern runs independently  
- ✅ **Simple & clear** - Easy to understand and modify
- ✅ **Progressive complexity** - Build from basics to advanced
- ✅ **Real examples** - Working code you can run immediately
- ✅ **Provider-agnostic** - Works with any LLM via litellm
- ✅ **Real APIs** - REST Countries API, MCP servers, and more

## 🔌 Function Calling & MCP

### Native Function Calling

Patterns 05 (Tool Calling) and 34 (ReAct) demonstrate **native function calling** using litellm's unified interface. Works identically across all providers:

- Define functions with JSON schemas
- LLM automatically chooses when to call functions
- Execute functions and inject results
- Works with Ollama, OpenAI, Gemini, and more

**Example**: `patterns/05_tool_calling.py` uses REST Countries API for real-world function calling.

### MCP (Model Context Protocol)

Pattern 10 demonstrates **real MCP server integration**:

- **Filesystem MCP Server**: List, read, write files
- **Git MCP Server**: Check git status, view commit logs
- Standardized protocol for external tool integration

**Example**: `patterns/10_mcp.py` shows real MCP server usage (not mocks).

## 🎯 Perfect For

- **Bootcamp Students** - Progressive learning with single-file patterns
- **AI Developers** - Quick reference for common agentic patterns
- **Educators** - Ready-to-use examples for teaching
- **Researchers** - Foundation for building complex AI systems

## 🚀 Next Steps

1. **Start with Foundation** - Run patterns 01-08 first
2. **Explore Advanced** - Try patterns 10-16 for complex behaviors
3. **Master Reasoning** - Practice patterns 17a-17c for better AI thinking
4. **Build Systems** - Combine patterns 23-28 for production systems
5. **Master RAG** - Learn patterns 29-33 for advanced retrieval systems
6. **Advanced Architectures** - Explore patterns 34-46 for cutting-edge agentic systems

## 🎓 Ready to Go Beyond Patterns?
