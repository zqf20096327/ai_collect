<p align="center"><img src="docs/assets/logo.svg" alt="ContextBoss logo" width="56"></p>

<h1 align="center">contextboss</h1>

<p align="center"><b>Master the context window. Don't fight it.</b><br>
One SQLite store that budgets, ranks and injects context for agents.<br>
Never over the window. Every decision explained.</p>

<p align="center">
  <img src="docs/assets/claude.svg" alt="Claude Code" height="18"> Claude Code &nbsp;·&nbsp;
  <img src="docs/assets/codex.svg" alt="Codex" height="18"> Codex &nbsp;·&nbsp;
  <img src="docs/assets/chatgpt.svg" alt="ChatGPT" height="18"> ChatGPT &nbsp;·&nbsp;
  <img src="docs/assets/mcp.svg" alt="MCP" height="18"> MCP
</p>

<p align="center"><a href="https://contextboss.vercel.app">contextboss.vercel.app</a></p>

<p align="center"><img src="docs/demo.png" alt="contextboss demo run" width="860"></p>

Most agents stuff everything into the prompt and pray. The window fills up, something
important gets cut, and the model guesses.

contextboss treats the window as a budget. Hand it every candidate block (system prompt, task,
memories, docs, tool schemas). It decides what goes in, what shrinks and what stays out, and
tells you why.

## Install

<img src="docs/assets/mcp.svg" alt="" height="14"> **MCP server** for <img src="docs/assets/claude.svg" alt="" height="14"> Claude Code, <img src="docs/assets/codex.svg" alt="" height="14"> Codex and <img src="docs/assets/chatgpt.svg" alt="" height="14"> ChatGPT:

```bash
pip install contextboss-mcp
contextboss-mcp install claude-code   # or: codex
contextboss-mcp serve --http          # streamable HTTP for Claude Web / ChatGPT
```

**Core library, REST API, dashboard:**

```bash
pip install contextboss-core
pip install contextboss-api && contextboss-api     # http://127.0.0.1:8787
cd apps/dashboard && npm install && npm run dev
docker compose up                                  # or one container
```

## Quickstart

```bash
pip install -e packages/contextboss-core
contextboss                 # live demo: what got in, what got dropped, why
contextboss --budget 400    # squeeze it and watch the tiers fight
```

```python
from contextboss import ContextAssembler, MemoryStore, Retriever, ToolSpec

asm = ContextAssembler(budget=8000, output_reserve=1000)
asm.system("You are a careful support engineer.")
asm.task("Why are our exports returning 429?")

memory = MemoryStore()
memory.add("Customer upgraded to Pro on Oct 2", importance=2.0)
asm.load_memory(memory, query="429 export", k=10)

docs = Retriever()
docs.index("rate-limits.md", open("rate-limits.md").read())
asm.load_retrieval(docs, query="429 export", k=10)

asm.tool(ToolSpec("get_usage", "Per-minute request counts for an API key", {"type": "object"}))

ctx = asm.assemble()
print(ctx.render())          # ready to send
print(ctx.total_tokens, "of", ctx.window)
for d in ctx.dropped():
    print(d.item_id, d.reason)
```

## How it works

| Tier | Role | Treatment |
| --- | --- | --- |
| `system` | Who the model is | Pinned. Raises `ContextOverflowError` if it alone can't fit |
| `task` | What to do now | Pinned. Truncated as a last resort |
| `memory` | Facts and history | Ranked by relevance x importance x recency |
| `retrieval` | Docs and chunks | Ranked by relevance |
| `tools` | Function schemas | Full schema, then compact form, never half a schema |

1. **Budget.** Output tokens are reserved first. The rest is split across memory, retrieval and
   tools by weight, with a cap per tier. Unused share flows to tiers that need it.
2. **Prioritize.** Higher priority goes first inside a tier. Output order is always
   `system > task > memory > retrieval > tools`.
3. **Degrade.** What doesn't fit gets compacted or summarized, then dropped. Plug in any
   `(text, max_tokens) -> str` as `summarizer=` to use an LLM.
4. **Spill.** Leftover tokens go back to dropped items. Nothing is wasted.
5. **Verify.** Real counts via `tiktoken`, plus a final check: `total_tokens <= window`, always.

Every decision lands in `ctx.decisions`: included, compacted, summarized or dropped, with tokens
and the reason. No black box.

```python
from contextboss import BudgetPolicy, Tier

policy = BudgetPolicy(
    weights={Tier.MEMORY: 0.2, Tier.RETRIEVAL: 0.7, Tier.TOOLS: 0.1},
    caps={Tier.MEMORY: 0.4, Tier.RETRIEVAL: 0.9, Tier.TOOLS: 0.3},
)
asm = ContextAssembler(budget=16000, policy=policy)
```

## Persistent context

`ContextManager` adds durable storage: namespaces, tags, provenance, pinned flags and full
version history in SQLite (WAL + FTS5). Deletion is real: entry, index rows and history.

```python
from contextboss import ContextManager

mgr = ContextManager("context.db")          # or ":memory:"
mgr.add("Staging deploys freeze on Fridays", tags=["deploy"], provenance="slack:#eng")
mgr.add("User is on the Pro plan since Oct 2", pinned=True, importance=2.0)

ctx = mgr.assemble("deploy freeze", system="You are a careful support engineer.",
                   task="Why did the Friday deploy fail?", budget=8000)
mgr.compact(entry_id, target_tokens=100)    # shrink, keep history
mgr.delete(entry_id)                        # gone for good
```

## Architecture

<p align="center"><img src="docs/architecture.jpg" alt="ContextBoss architecture" width="860"></p>

More in [ARCHITECTURE.md](ARCHITECTURE.md) and [docs/benchmarks.md](docs/benchmarks.md).

```
packages/   core engine, MCP server, REST API
apps/       dashboard
docs/       images, assets, benchmarks
landing/    contextboss.vercel.app
```

## Dev

```bash
pip install -e ".[dev]" && pytest
python scripts/make_screenshot.py   # regenerate docs/demo.png (needs Chrome)
```

MIT
