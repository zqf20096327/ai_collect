# 🪁 Kite

**From idea to running AI agent in one command.**

[![PyPI](https://img.shields.io/pypi/v/kite-agent?color=brightgreen&label=pip%20install%20kite-agent)](https://pypi.org/project/kite-agent/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/beevr-labs/Kite?style=social)](https://github.com/beevr-labs/Kite/stargazers)

![kite generate demo](docs/demo-generate.gif)

```bash
pip install kite-agent
kite generate "customer support agent that tracks orders"
```

> A running, multi-agent Python script. No boilerplate. No config files.

---

## Why Kite?

LangChain gives you 500+ abstractions. AutoGen needs 100 lines of config.  
Kite gives you **one command** — and a different philosophy.

|                          | LangChain | AutoGen | **Kite** |
|--------------------------|-----------|---------|----------|
| Time to first agent      | ~30 min   | ~20 min | **< 1 min** |
| LLM as untrusted component | ❌      | ❌      | ✅ |
| Built-in circuit breaker | ❌        | ❌      | ✅ |
| Kill switch              | ❌        | ❌      | ✅ |
| Prompt A/B testing       | ❌        | ❌      | ✅ |
| CLI code generation      | ❌        | ❌      | ✅ |
| Startup time             | ~2s       | ~1s     | **~50ms** |

---

## The core idea: LLMs don't execute. They propose.

Most frameworks let the LLM call tools directly. Kite doesn't.

```
User request
    │
    ▼
LLM (untrusted) ── proposes ──▶  Kernel (you control)
                                       │
                           ┌───────────┴──────────┐
                           │  tool whitelisted?    │
                           │  budget exceeded?     │
                           │  policy violated?     │
                           └───────────┬──────────┘
                                  approved?
                               YES ↙     ↘ NO
                           Execute      Reject + log
```

```python
# ❌ Other frameworks: LLM decides what runs
agent.run("delete all test users")  # LLM calls delete_user() directly

# ✅ Kite: LLM proposes, Kernel validates
shell = ShellTool(allowed_commands=["ls", "git", "df"])
# agent.run("rm -rf /") → blocked at kernel, never executes
```

[Read the full architecture →](ARCHITECTURE.md)

---

## 30-second quickstart

```bash
pip install kite-agent
export GROQ_API_KEY=your_key    # free at console.groq.com
kite generate "research assistant that searches and summarizes" --out agent.py
python agent.py
```

Or scaffold a full project:

![kite init demo](docs/demo-init.gif)

```bash
kite init --type=agent --name=my_bot
cd my_bot && cp .env.example .env
python main.py
```

---

## Production safety — built in, not bolted on

![circuit breaker demo](docs/demo-safety.gif)

```python
from kite import Kite

ai = Kite()

# Circuit breaker — auto-stops cascading failures
ai.circuit_breaker.config.failure_threshold = 3
ai.circuit_breaker.config.timeout_seconds = 60

# Idempotency — no duplicate charges, no double-sends
result = ai.idempotency.execute(
    operation_id="order_123_refund",   # same id = cached result
    func=process_refund,
    args=(order_id,)
)

# Kill switch — emergency stop, per-agent or global
ai.kill_switch.activate("Budget limit reached")
agent.kill_switch.activate("This agent only")
```

---

## 5 reasoning patterns

```python
agent = ai.create_agent(name="Bot", agent_type="react", ...)        # think→act→observe loop
agent = ai.create_agent(name="Bot", agent_type="rewoo", ...)        # plan upfront, run parallel (~2× faster)
agent = ai.create_agent(name="Bot", agent_type="tot", ...)          # explore multiple paths
agent = ai.create_agent(name="Bot", agent_type="plan_execute", ...) # decompose, replan on failure
agent = ai.create_agent(name="Bot", agent_type="reflective", ...)   # generate → critique → improve
```

---

## Advanced RAG — production retrieval, not toy examples

```python
# Load any document type
ai.load_document("docs/policy.pdf")   # PDF, DOCX, CSV, HTML, TXT
ai.load_document("data/")             # entire directory

# HyDE — generate hypothetical answer first, then search (↑ accuracy)
results = ai.advanced_rag.search("return policy", method="hyde")

# Hybrid search — BM25 keyword + vector semantic combined
results = ai.advanced_rag.hybrid_search("cancellation steps", alpha=0.5)

# MMR — remove redundant results, maximize diversity
results = ai.advanced_rag.mmr("pricing tiers", results, lambda_param=0.7)

# Reranking — Cohere or Cross-encoder for final precision
results = ai.advanced_rag.rerank_cohere("refund eligibility", results)

# Knowledge graph — multi-hop relationship queries
ai.graph_rag.add_relationship("Order", "belongs_to", "Customer")
answer = ai.graph_rag.query("Which orders belong to premium customers?")
```

---

## Prompt A/B testing

Test prompts and models on real traffic. No other Python agent framework ships this.

```python
from kite.ab_testing import ABTestManager

ab = ABTestManager()
ab.create_experiment(
    name="support_tone",
    variants=[
        {"name": "formal", "weight": 0.5, "config": {"system_prompt": "You are professional..."}},
        {"name": "casual", "weight": 0.5, "config": {"system_prompt": "Hey! Happy to help..."}},
    ]
)

variant = ab.get_variant("support_tone", user_id="user_123")  # consistent per user
ab.record_conversion("support_tone", variant.name)

results = ab.get_results("support_tone")
# → {"winner": "casual", "confidence": 0.94, "conversions": {...}}
```

---

## Multi-agent conversation

```python
researcher = ai.create_agent("Researcher", "You gather facts...",         agent_type="react")
critic     = ai.create_agent("Critic",     "You challenge assumptions...")
writer     = ai.create_agent("Writer",     "You synthesize into prose...")

conversation = ai.create_conversation(
    agents=[researcher, critic, writer],
    max_turns=9,
    termination_condition="consensus"
)

result = await conversation.run("Best pricing strategy for B2B SaaS?")
```

---

## Smart model routing — cut costs 60–80%

```bash
# .env
FAST_LLM_MODEL=groq/llama-3.1-8b-instant   # routing, simple tasks
SMART_LLM_MODEL=openai/gpt-4o              # complex reasoning
```

```python
from kite.optimization.resource_router import ResourceAwareRouter

router   = ResourceAwareRouter(ai.config)
router_a = ai.create_agent("Router",  model=router.fast_model,  ...)
analyst  = ai.create_agent("Analyst", model=router.smart_model, ...)
```

---

## Human-in-the-loop workflows

```python
pipeline = ai.pipeline.create("approval_flow")
pipeline.add_step("draft",  draft_email)
pipeline.add_checkpoint("draft")    # ← pauses for human review
pipeline.add_step("send",   send_email)

state = await pipeline.execute_async({"to": "customer@example.com"})
final = await pipeline.resume_async(state.task_id, approved=True)
```

---

## Observability

```python
ai.enable_tracing("run_trace.json")              # every event → JSON file
ai.enable_state_tracking("session.json")         # state changes across session
ai.event_bus.subscribe("agent:*", my_callback)   # subscribe to any event
ai.add_event_relay("http://localhost:8000/events") # forward to dashboard
print(ai.get_metrics())   # circuit breaker, cache hits, token usage
```

---

## Works with any LLM

```bash
LLM_PROVIDER=groq       LLM_MODEL=llama-3.3-70b-versatile   # fastest, free tier
LLM_PROVIDER=openai     LLM_MODEL=gpt-4o                    # most capable
LLM_PROVIDER=anthropic  LLM_MODEL=claude-3-5-sonnet-...     # best reasoning
LLM_PROVIDER=ollama     LLM_MODEL=qwen2.5:1.5b              # local, free
```

Switch by changing 2 env vars. Zero code changes.

---

## MCP integrations

```python
from kite.tools.mcp.slack_mcp_server    import SlackMCPServer
from kite.tools.mcp.gmail_mcp_server    import GmailMCPServer
from kite.tools.mcp.gdrive_mcp_server   import GDriveMCPServer
from kite.tools.mcp.postgres_mcp_server import PostgresMCPServer
from kite.tools.mcp.stripe_mcp_server   import StripeMCPServer  # idempotency keys built-in
```

---

## CLI reference

| Command | What it does |
|---------|--------------|
| `kite generate "idea" --out app.py` | Generate multi-agent app from natural language |
| `kite compile skill.md --out app.py` | Compile a Markdown skill spec into Python |
| `kite init --type=agent --name=bot` | Scaffold a new agent project |
| `kite init --type=workflow --name=w` | Scaffold a multi-agent pipeline |
| `kite init --type=tool --name=t` | Scaffold a standalone tool module |

---

## Examples

| Example | What it builds | Difficulty |
|---------|---------------|------------|
| [Case 1](examples/case1_ecommerce_support.py) | E-commerce support bot | 🟢 Beginner |
| [Case 2](examples/case2_enterprise_analytics.py) | Data analyst with SQL + charts | 🟡 Intermediate |
| [Case 3](examples/case3_research_assistant.py) | Deep research + web scraping | 🟡 Intermediate |
| [Case 4](examples/case4_multi_agent_collab.py) | Multi-agent collaboration + HITL | 🔴 Advanced |
| [Case 5](examples/case5_devops_automation.py) | DevOps automation with safe shell | 🟡 Intermediate |
| [Case 6](examples/case6_reasoning_architectures.py) | ReAct vs ReWOO vs ToT benchmark | 🔴 Advanced |

---

## Architecture

```
kite/
├── agents/      # ReAct, ReWOO, ToT, Plan-Execute, Reflective
├── memory/      # Vector RAG, Advanced RAG (HyDE/hybrid/MMR), Graph RAG, Session, Semantic Cache
├── safety/      # Circuit breaker, Kill switch, Idempotency, Guardrails
├── routing/     # LLM router, Semantic router, Aggregator, Resource-aware
├── tools/       # Web search, Calculator, Shell (whitelisted), MCP servers
├── pipeline/    # Deterministic workflows with HITL checkpoints
├── ab_testing/  # Prompt & model A/B experiments
├── monitoring/  # Metrics, tracing, event bus, FastAPI dashboard
└── utils/       # Batch processor, Cluster (Redis), Document loader
```

Lazy-loaded. `Kite()` starts in **~50ms**.

---

## Roadmap

- [x] `kite generate` — natural language → runnable agent
- [x] `kite init` — project scaffolding
- [x] 5 reasoning patterns (ReAct, ReWOO, ToT, Plan-Execute, Reflective)
- [x] Circuit breaker + kill switch + idempotency
- [x] Advanced RAG (HyDE, hybrid BM25+vector, MMR, Cohere rerank)
- [x] Prompt A/B testing with statistical confidence
- [x] MCP: Slack, Stripe, Gmail, Google Drive, PostgreSQL
- [x] Multi-agent conversation manager
- [ ] Streaming responses
- [ ] `kite deploy` — one command to production
- [ ] Web dashboard (monitoring API ready, UI in progress)

---

## Contributing

```bash
git clone https://github.com/beevr-labs/Kite
cd Kite && pip install -e ".[dev]"
pytest tests/
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## License

MIT — use however you want. Commercial use welcome.

---

**⭐ Star this repo if Kite saves you time.**

Built and open-sourced by **[BeevR](https://beevr.ai/ai-development-company)** — a senior, founder-led studio building production-grade, compliance-bound AI. If you are building agents that need to survive an audit, not just a demo, [here is how we work](https://beevr.ai/ai-development-company).

[Issues](https://github.com/beevr-labs/Kite/issues) · [Discussions](https://github.com/beevr-labs/Kite/discussions)
