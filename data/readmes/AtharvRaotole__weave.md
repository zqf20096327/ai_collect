<div align="center">

# Weave

**Your agent writes one short script. Weave checks it, shows you every call and write it can make, then runs the calls in parallel where it can.**

[![CI](https://github.com/AtharvRaotole/weave/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/AtharvRaotole/weave/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/AtharvRaotole/weave)](https://github.com/AtharvRaotole/weave/releases)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/AtharvRaotole/weave/blob/main/LICENSE)
[![AtharvRaotole/weave MCP server](https://glama.ai/mcp/servers/AtharvRaotole/weave/badges/score.svg)](https://glama.ai/mcp/servers/AtharvRaotole/weave)

[Quickstart](#quickstart) · [Plan preview](#see-the-plan-before-anything-runs) · [How it compares](#how-it-compares) · [Getting started](https://github.com/AtharvRaotole/weave/blob/main/docs/getting-started.md) · [Benchmarks](https://github.com/AtharvRaotole/weave/blob/main/docs/benchmarks.md) · [Paper](https://github.com/AtharvRaotole/weave/blob/main/docs/paper/weave.md) · [Production](https://github.com/AtharvRaotole/weave/blob/main/docs/production.md) · [Full reference](https://github.com/AtharvRaotole/weave/blob/main/docs/reference.md)

**[Try it in your browser](https://atharvraotole.github.io/weave/)**: the real parser, check and scheduler compiled to WebAssembly, with mock tools. Nothing to install.

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

The whole script is checked before the first call runs: unknown tools, a misspelled keyword
(`get_weather(cty="Paris")` gets "did you mean `city`?"), a missing argument, or for MCP tools a
literal that doesn't match the tool's JSON schema. So a typo on the last line stops the script before
the first line's write happens. [What the check covers](https://github.com/AtharvRaotole/weave/blob/main/docs/reference.md#what-the-check-catches-before-anything-runs).

Declare what a tool returns (`weave.declare(returns='{"temp_c": int, "sky": str}')`) and the check follows its
results too: `get_weather("Paris")["temp"]` gets "did you mean 'temp_c'?" before any call goes out. Replaying the
6,653 scripts from our recorded BFCL runs, it flagged 50: 45 had really failed at run time on that line (29 after an
earlier call had already run), and 3 were false alarms from a learned shape that missed a variant.
[How it works and what it skips](https://github.com/AtharvRaotole/weave/blob/main/docs/reference.md#declared-results-wrong-keys-caught-before-anything-runs).

## See the plan before anything runs

Because the script is plain data flow over declared tools, Weave can tell you what it will do without running
it. `tool.plan(source)` (or `weave plan` on the CLI, or `weave_plan` over MCP) lists every tool call, how many
times it can run, where each argument comes from, and what it may write. Say the model sends this:

```python
tickets = [get_ticket(t) for t in ["T-1", "T-2", "T-3"]]
for t in tickets:
    if t["stale"]:
        refund(t["order"])
```

The plan, before a single call:

```text
plan: 3 to 6 tool calls, 2 dependent stages, strongest effect irreversible
  #1 line 1: get_ticket('T-1' | 'T-2' | 'T-3') read x3 stage 1
  #2 line 4: refund(<#1>) irreversible x0-3 stage 2, writes payment:{0|order_id} (filled at run time)
```

So you know up front: three reads in parallel, then up to three refunds whose order ids come from `get_ticket`
results. Pass `approve=` and Weave asks you once per script, before anything runs:

```python
def approve(plan):
    if any(c["effect"] == "irreversible" for c in plan["calls"]):
        return "refunds need a person"   # the model gets "[not approved] Nothing ran ..." with this reason
    return True

tool = weave.WeaveTool([get_ticket, close_ticket, refund], approve=approve)
```

<img src="https://raw.githubusercontent.com/AtharvRaotole/weave/main/assets/plan.gif" alt="Terminal recording of python examples/plan_preview.py: a script that closes two known tickets is planned, approved and run; a script that would refund orders picked from tool results is planned and refused, and no tool is called" width="760">

Read-only scripts run without asking. When the targets are literals, the plan resolves them
(`close_ticket('T-1' | 'T-3') ... writes ticket:T-1, ticket:T-3`). The counts and sources are upper bounds checked
against real runs on tens of thousands of random scripts; anything it can't know statically shows up as unknown,
never guessed. Full example: [`examples/plan_preview.py`](https://github.com/AtharvRaotole/weave/blob/main/examples/plan_preview.py),
details in the [reference](https://github.com/AtharvRaotole/weave/blob/main/docs/reference.md#see-the-plan-before-it-runs).

Does it help? On a pre-registered fan-out suite against real services it passed 40/40 tasks vs 27/40 for plain
function calling, at about half the cost. It's not a win everywhere though: on BFCL multi-turn it was a small,
not significant gain in one round (159/378 vs 140/378), a clear loss with GPT-5.4 mini in another (18/60 vs 27/60),
and a draw on tau-bench. Details below.

Try it, break it, and tell us what went wrong. Issues and PRs are very welcome.

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

## How it compares

Letting the model write code instead of one JSON call at a time is not new, and Weave builds on that work.
What's different is where the code runs and what you know before it does.

| | the model writes | runs where | parallel calls | known before the first call |
|---|---|---|---|---|
| Native function calling | one JSON call per tool | your app | several per turn if the model asks | this round's calls, one round at a time |
| [LLMCompiler](https://arxiv.org/abs/2312.04511) | a DAG of calls | your app | yes, from the DAG | the DAG (no loops or branches) |
| [CodeAct](https://arxiv.org/abs/2402.01030), [smolagents](https://github.com/huggingface/smolagents) | full Python | a Python executor or a sandbox | if the code does it | the code; bad tool calls fail at run time |
| [Anthropic programmatic tool calling](https://www.anthropic.com/research/advanced-tool-use) | Python | Anthropic's code execution container | if the code uses async | the code |
| [OpenAI programmatic tool calling](https://developers.openai.com/api/docs/guides/tools-programmatic-tool-calling) | JavaScript | OpenAI's hosted V8 | if the code uses promises | the code (their docs suggest direct calls for writes) |
| [Cloudflare Code Mode](https://blog.cloudflare.com/code-mode/) | TypeScript | a V8 isolate on Workers | if the code uses promises | the code |
| **Weave** | a Python subset | a Rust runtime in your process | automatic, from data flow and declared effects | tool names, arguments, schemas and declared result keys checked, plus a plan of every call and write you can approve |

When to pick something else: the hosted options need no runtime on your side, and full Python can import
libraries, which Weave's subset can't. And if a small model has to think after every single result, plain
function calling can do better (that's our GPT-5.4 mini loss above).

## Install

```bash
pip install weave-lang
# or a GitHub release wheel:  curl -fsSL https://raw.githubusercontent.com/AtharvRaotole/weave/main/scripts/install.sh | sh
# or from source (needs Rust):  pip install "git+https://github.com/AtharvRaotole/weave@v1.3.0"
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

No API key? `python examples/demo.py`, `python examples/quickstart.py` and `python examples/plan_preview.py` run offline.

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
