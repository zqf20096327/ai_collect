<div align="center">

# Weave

**Your agent writes one short script. Weave runs every tool call in it, in parallel where it can.**

[![CI](https://github.com/AtharvRaotole/weave/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/AtharvRaotole/weave/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/AtharvRaotole/weave)](https://github.com/AtharvRaotole/weave/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/AtharvRaotole/weave/blob/main/LICENSE)

[Quickstart](#quickstart) · [Getting started](https://github.com/AtharvRaotole/weave/blob/main/docs/getting-started.md) · [Benchmarks](https://github.com/AtharvRaotole/weave/blob/main/docs/benchmarks.md) · [Paper](https://github.com/AtharvRaotole/weave/blob/main/docs/paper/weave.md) · [Production](https://github.com/AtharvRaotole/weave/blob/main/docs/production.md) · [Full reference](https://github.com/AtharvRaotole/weave/blob/main/docs/reference.md)

<img src="https://raw.githubusercontent.com/AtharvRaotole/weave/main/assets/demo.gif" alt="Terminal recording of python examples/demo.py: one Weave script makes 13 tool calls in 4 overlapping waves in 1.2 s" width="720">

</div>

With native function calling, every round of tool calls costs a model round trip, and every raw result goes back
into context. With Weave, the model writes one script in a restricted Python subset (loops, comprehensions,
helpers). A Rust runtime runs the script's independent reads together, orders writes by their declared effects, and
returns only what the script printed.

```bash
pip install weave-lang
```

Say the model is asked which of three cities is warmest. Instead of three tool calls and three round trips, it sends
one script:

```python
temps = {c: get_weather(c) for c in ["Paris", "Tokyo", "Lima"]}
warmest = max(temps, key=lambda c: temps[c])
print(warmest, temps[warmest])
```

Weave runs the three `get_weather` calls at the same time and hands back one line: `Tokyo 22`.

Does it help? On a pre-registered fan-out suite against real services it passed 40/40 tasks vs 27/40 for plain
function calling, at about half the cost. It's not a win everywhere though: on BFCL multi-turn it was a small,
not significant gain in one round (159/378 vs 140/378), a clear loss with GPT-5.4 mini in another (18/60 vs 27/60),
and a draw on tau-bench. Details below.

If this looks useful, a star helps other people find it. Issues and PRs are very welcome too.

## Results

<img src="https://raw.githubusercontent.com/AtharvRaotole/weave/main/assets/results.png" alt="Round 9 results: tasks passed and cost per task, Weave vs native, on a real-services fan-out suite and on BFCL multi-turn" width="860">

Pre-registered, on fresh tasks, against native function calling with the same model, tools and settings
([paper §5.17–5.19](https://github.com/AtharvRaotole/weave/blob/main/docs/paper/weave.md), [all rounds](https://github.com/AtharvRaotole/weave/blob/main/docs/benchmarks.md)):

- **Fan-out on real services** (SQLite, git, files, HTTP, PyPI): **40/40 vs 27/40** passed, **2.1–2.7 s vs 4.3 s** per
  task, at **0.45–0.50× the cost** (GPT-4.1 and GPT-5.4 mini).
- **BFCL v4 multi-turn** (round 9, public tasks and grader): **0.86× the cost** and 25 % fewer tokens. Success: **+3 tasks with
  GPT-4.1 (38 vs 35 of 60), but −9 with GPT-5.4 mini (18 vs 27), a significant loss.**
- **BFCL multi-turn, fresh confirmation with the write gate** (round 11; 63 unused scenarios × base, miss_param,
  miss_func): **159/378 vs 140/378** passed (p = 0.07, not significant) at **0.91× the cost**. GPT-4.1 92 vs 81 and
  GPT-5.4 mini 67 vs 59, each not significant on its own; run on Azure deployments of the same model versions.
- **BFCL miss_param / miss_func with the write gate** (round 10, `write_gate="choice"`): GPT-5.4 mini **30/105 vs
  24/105** (not significant) at **equal cost**; GPT-4.1 **3/16 vs 5/16, a loss** (5/20 vs 7/20 with the pairs
  completed on Azure).
- **tau-bench retail** (a conversation, one confirmation per write): a draw.

Round 9 used `WeaveTool(compact=True)`; rounds 10–11 added `write_gate="choice"`. Both ship in 1.1.0. The chart shows round 9.

Use Weave for fan-out (the same lookup over many items), chains of dependent lookups, and filtering results before
the model sees them. Skip it when each step waits for a person, or when a small model must think after every result.

## Install

```bash
pip install weave-lang
# or a GitHub release wheel:  curl -fsSL https://raw.githubusercontent.com/AtharvRaotole/weave/main/scripts/install.sh | sh
# or from source (needs Rust):  pip install "git+https://github.com/AtharvRaotole/weave@v1.1.2"
```

The package is `weave-lang` (import `weave`). Python 3.9–3.13, Linux, macOS and Windows.
More options: [getting started](https://github.com/AtharvRaotole/weave/blob/main/docs/getting-started.md).

## Quickstart

```python
import weave
from openai import OpenAI

@weave.declare(effect="read", arity=1)
def order_total(order_id: str) -> int:
    """Return an order's total in dollars."""
    return {"o1": 12, "o2": 30, "o3": 7}[order_id]

tool = weave.WeaveTool([order_total])   # one tool: run_weave(source)
client = OpenAI()
messages = [{"role": "user", "content": "What do orders o1, o2 and o3 add up to?"}]
while True:
    msg = client.chat.completions.create(model="gpt-4.1", messages=messages,
                                         tools=[tool.chat_tool()], **tool.request_options).choices[0].message
    messages.append(msg)
    if not msg.tool_calls:
        break
    messages += [tool.handle(call) for call in msg.tool_calls]
print(msg.content)
```

No API key? `python examples/demo.py` and `python examples/quickstart.py` run offline.

## Works with

| stack | how |
|---|---|
| OpenAI Chat Completions / Responses | `tool.chat_tool()`, `tool.responses_tool()` |
| OpenAI Agents SDK | `Agent(tools=[tool.agents_tool()])` |
| LangChain / LangGraph | `tool.langchain_tool()` |
| Claude Desktop, Cursor, VS Code, Claude Code | `weave mcp-config --client claude --config tools.json --write` (or `cursor`, `vscode`, `claude-code`) |
| Rust hosts, the `weave` CLI | [runtime reference](https://github.com/AtharvRaotole/weave/blob/main/docs/runtime.html), [CLI](https://github.com/AtharvRaotole/weave/blob/main/docs/cli.html) |

## Learn more

- [Getting started](https://github.com/AtharvRaotole/weave/blob/main/docs/getting-started.md): recipes for each stack, chat assistants, MCP servers.
- [Running in production](https://github.com/AtharvRaotole/weave/blob/main/docs/production.md): guarantees with their tests, isolation, budgets, privacy.
- [Benchmarks](https://github.com/AtharvRaotole/weave/blob/main/docs/benchmarks.md) and the [paper](https://github.com/AtharvRaotole/weave/blob/main/docs/paper/weave.md): every round, every loss, pre-registrations.
- [Full reference](https://github.com/AtharvRaotole/weave/blob/main/docs/reference.md): the long-form guide. [Architecture](https://github.com/AtharvRaotole/weave/blob/main/docs/architecture.md), [roadmap](https://github.com/AtharvRaotole/weave/blob/main/ROADMAP.md),
  [contributing](https://github.com/AtharvRaotole/weave/blob/main/CONTRIBUTING.md), [security](https://github.com/AtharvRaotole/weave/blob/main/SECURITY.md), [citation](https://github.com/AtharvRaotole/weave/blob/main/CITATION.cff).
- Want to help? Start with issues labeled [`good first issue`](https://github.com/AtharvRaotole/weave/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22).

[MIT](https://github.com/AtharvRaotole/weave/blob/main/LICENSE). The speculative cache draws on Nichols et al.,
[Optimizing Agentic Language Model Inference via Speculative Tool Calls](https://arxiv.org/abs/2512.15834).
