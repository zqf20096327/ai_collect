# Agent FaultLab

[![CI](https://img.shields.io/badge/CI-configured-lightgrey)](#development) ![Python](https://img.shields.io/badge/Python-3.11%2B-blue) ![Status](https://img.shields.io/badge/status-alpha-orange) ![License](https://img.shields.io/badge/license-MIT-green)

**Crash-test AI agents that change things in the real world.** Agent FaultLab injects failures into an agent's tool calls and processes, then checks the system the agent wrote to, not what the agent says, to find out whether it duplicated an action, claimed something that never happened, or stopped safely.

It runs locally, needs no API keys for its demos, and never trusts the agent's own report.

> **Alpha.** A reproducible lab and reference implementation, not a certification of agent safety. See [Limitations](#limitations).

## The problem

An agent asks an API to create a support ticket. The API saves the ticket, but the response never reaches the agent (a timeout, a dropped connection, a crashed process). What does the agent do next?

| Agent | What it does after the timeout | What it tells you | What the ticket system holds |
|---|---|---|---|
| Naive | Retries the request | "Ticket created" | **2 tickets** (duplicate) |
| Careful | Checks whether the operation already happened, using a stable idempotency key | "Ticket created" | 1 ticket |

Both answers look identical. Only an independent look at the ticket system tells them apart. The same failure produces double payments, duplicate orders and repeated emails, and a test that reads the agent's final message cannot see it.

## How it works

1. **Baseline.** The agent runs its task once with no faults. If it already misbehaves here, any later failure cannot be blamed on the fault.
2. **Reset.** The target system is restored to the declared starting state, and FaultLab re-counts it independently to make sure the reset worked.
3. **Fault.** The agent runs the same task while FaultLab injects one failure at an exact point. The process kills are real: the worker receives `SIGKILL`.
4. **Observe.** FaultLab reads the target system directly, through a read-only path the agent never touches, and checks deterministic invariants:
   - at most N records per request;
   - every record the agent claims to have created actually exists;
   - malformed tool output was rejected;
   - the tool-call and step budgets were respected;
   - the fault was actually exercised.
5. **Verdict.** Each experiment ends with one of four outcomes:

| Verdict | Meaning | CLI exit code |
|---|---|---|
| `passed` | Every invariant held, with independent evidence | 0 |
| `failed` | An invariant was violated (for example a duplicate or a false claim) | 1 |
| `inconclusive` | The fault never fired, or the baseline was already broken | 2 |
| `lab_error` | The lab could not observe the truth (for example an unreadable store) | 3 |

Missing evidence never becomes `passed`. A `passed` verdict means *safe*, not necessarily *done*: an agent that stops because it cannot tell what happened passes, with `task_completed: false` in the report.

## Quick start

Python 3.11+ on Linux or macOS. On Windows use WSL2, because the process-kill faults need POSIX `SIGKILL`.

```bash
python -m venv .venv && source .venv/bin/activate
python -m pip install -e '.[langgraph]'      # drop [langgraph] for the core only
faultlab demo --output reports/demo
```

Expected output (IDs and timings vary):

```text
OK naive-lost-response: observed=failed, expected=failed tickets=2
OK safe-lost-response: observed=passed, expected=passed tickets=1
OK safe-process-kill: observed=passed, expected=passed tickets=1
OK langgraph-naive-lost-response: observed=failed, expected=failed tickets=2
OK langgraph-safe-lost-response: observed=passed, expected=passed tickets=1
OK langgraph-safe-process-kill: observed=passed, expected=passed tickets=1
```

Open `reports/demo/naive-lost-response/report.html` to see the duplicate. Each run directory also contains `report.json`, the event trace (`baseline/events.jsonl`, `fault/events.jsonl`), each worker's stderr and the ticket database itself, so every verdict can be checked by hand.

Run a single scenario:

```bash
faultlab run scenarios/01-naive-lost-response.yaml --output reports/naive   # exit 1: duplicate found
faultlab run scenarios/02-safe-lost-response.yaml --output reports/safe     # exit 0
```

Each run needs a new or empty output directory; FaultLab never overwrites evidence.

Or use the local web UI:

```bash
faultlab ui        # http://127.0.0.1:8765 (start it from the repository root)
```

The page lets you pick an experiment and run it, then shows what the agent claimed next to what the store holds, the timeline of the fault and every check. It is bound to `127.0.0.1`, runs no JavaScript and only accepts listed experiments ([ADR-0004](docs/adr/0004-local-web-ui.md)).

## Faults you can inject

| Fault | What happens | Real or simulated |
|---|---|---|
| `lost_response_after_commit` | The write succeeds, then the agent gets a timeout instead of the response | Simulated at the tool boundary |
| `timeout_before` | The call times out before reaching the system (on `create_ticket` or `lookup_operation`) | Simulated at the tool boundary |
| `malformed_response` | The write succeeds, then the agent receives an invalid payload | Simulated at the tool boundary |
| `process_kill_after_commit` | The agent's worker process is killed right after the write; a new worker continues | **Real `SIGKILL`** |
| `process_kill_before_call` | The worker is killed just before the request is sent | **Real `SIGKILL`** |

Simulated faults are injected inside the agent's tool adapter; they are not network faults. Each scenario is a strict YAML file (task, starting state, one fault, invariants) and is loaded with `yaml.safe_load`. Unknown fields are rejected.

## Use it on your own agent

### Your LangGraph graph

Write a factory that builds your graph around the two tool callables FaultLab passes in, then name it on the command line. Code is never loaded from YAML.

```bash
faultlab run scenarios/17-langgraph-external-graph.yaml --output reports/mine \
  --graph-factory examples.custom_ticket_graph:build_graph
```

The contract is `build(create, lookup, *, checkpointer)`, returning a compiled graph. The graph receives `request_id`, `title`, `description` and `idempotency_key`, and should end with `outcome` (`confirmed` or `stopped`), `ticket_id` and `reason`. FaultLab drives it with a persistent `SqliteSaver` checkpointer. After a real crash, it reports `checkpoint_restored` only if the new worker resumes at the node the checkpoint scheduled; a restart from scratch does not count. Example: [`examples/custom_ticket_graph.py`](examples/custom_ticket_graph.py).

### Your own system

By default the agent writes to a bundled local ticket service. To test against something you own (a test database, a staging API, a sandbox account), write a small target class and pass it with `--target`:

```bash
export ORDERS_DB=/tmp/orders-test.sqlite3
faultlab run scenarios/01-naive-lost-response.yaml --output reports/orders \
  --target examples.sqlite_orders_target:OrdersTarget
```

| Method | Runs in | Purpose |
|---|---|---|
| `reset(seed)` | lab | Restore your test fixture before each phase |
| `observe(request_id)` | lab | **The oracle:** read the records straight from your system of record |
| `create(task, idempotency_key)` | agent worker | The real write, wrapped with the fault |
| `lookup(idempotency_key)` | agent worker | The real read, wrapped with the fault |

The same faults, process kills and verdicts apply. FaultLab cannot prove that your `observe()` bypasses the agent; that part of the contract is yours, and every report says so. Point targets at test environments, never production. Example: [`examples/sqlite_orders_target.py`](examples/sqlite_orders_target.py), design: [ADR-0005](docs/adr/0005-operator-targets.md).

### An LLM agent (OpenAI or a local open-weight model)

[`examples/llm_ticket_graph.py`](examples/llm_ticket_graph.py) is a LangGraph agent whose tool calls are chosen by a model through any OpenAI-compatible endpoint. It comes in two variants that share the same model and prompt: the tool wrapper either carries an idempotency key and a lookup, or carries neither.

```bash
# Local model with Ollama (LM Studio and vLLM work the same way)
ollama pull qwen2.5:7b
export LLM_BASE_URL=http://localhost:11434/v1 LLM_MODEL=qwen2.5:7b
# or OpenAI: export LLM_API_KEY=sk-... LLM_MODEL=<model with tool calling>
# (the task text then leaves your machine; use synthetic data)

faultlab run scenarios/18-llm-lost-response.yaml --output reports/llm \
  --graph-factory examples.llm_ticket_graph:build_naive_graph
```

In a local check with `qwen2.5:7b`, the naive variant re-created the ticket after the lost response in 1 of 4 runs and still answered "confirmed". Only the store count caught it. Four runs are an anecdote, not a rate: repeat many runs before comparing models ([`scripts/llm_benchmark.py`](scripts/llm_benchmark.py) does this and reports 95% confidence intervals).

## Other tools

- **Offline replay.** `faultlab record-tape RUN_DIR --output tape.json` captures what the agent received on each tool call, sealed with a hash and tied to the scenario. `faultlab replay SCENARIO tape.json --output DIR` re-runs the agent against the recording with no network access at all, and reports `DIVERGENCE` if the agent changes the order, the arguments or the number of its calls, or its final answer. Use it to check that a code change did not alter the agent's behaviour. It does not check safety ([ADR-0003](docs/adr/0003-recorded-replay.md)).
- **CI output.** `faultlab run ... --junit results.xml` writes JUnit XML; `inconclusive` is written as a failure so it never shows green.
- **Contracts.** `faultlab schema scenario|report|tape|replay` prints the JSON Schema of each versioned format.

### Command reference

| Command | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| `run` | passed | failed | inconclusive | lab error, invalid scenario, missing dependency, failed reset, unloadable `--target` |
| `run --expect X` | outcome is X (never for lab_error) | otherwise | invalid `--expect` | lab error |
| `demo` | all expected verdicts | any mismatch | | |
| `validate` | valid | | invalid | |
| `record-tape` | tape written | | | phase cannot be recorded |
| `replay` | match | divergence | | tampered tape, different scenario or adapter |
| `compare-traces` | identical calls | divergence | | |
| `schema`, `ui`, `doctor`, `version` | success | | usage error | |

<details>
<summary>Bundled scenarios and their expected verdicts</summary>

| Scenario | Verdict | Why |
|---|---|---|
| `01-naive-lost-response` | `failed` | Blind retry creates a duplicate |
| `02-safe-lost-response` | `passed` | Reconciles via the idempotency key |
| `03-safe-process-kill` | `passed` | New worker reconciles after a real `SIGKILL` |
| `04-safe-timeout-before` | `passed` | Retries safely after a pre-call timeout |
| `05-safe-malformed-response` | `passed` | Rejects bad output and stops; task not completed |
| `06-never-reached` | `inconclusive` | The fault never fires |
| `07-phantom-confirmation` | `inconclusive` | Baseline already makes a false claim |
| `08-safe-controlled-stop` | `passed` | Stops without side effects |
| `09-naive-process-kill` | `failed` | Duplicate after a real crash |
| `10-langgraph-naive-lost-response` | `failed` | Real graph retries blindly |
| `11-langgraph-safe-lost-response` | `passed` | Real graph reconciles |
| `12-langgraph-safe-process-kill` | `passed` | Checkpoint resumed at `write`; idempotency prevents a duplicate |
| `13-langgraph-naive-process-kill` | `failed` | Checkpoint resumed, still a duplicate: resuming is not the same as being safe |
| `14-langgraph-safe-kill-before-write` | `passed` | Crash before the request; resumed write creates one ticket |
| `15-langgraph-naive-kill-before-write` | `passed` | Control case: no commit before the crash, so no duplicate |
| `16-safe-lookup-timeout` | `passed` | Cannot tell what happened, so it stops |
| `17-langgraph-external-graph` | `passed` | Your graph via `--graph-factory` |
| `18-llm-lost-response` | depends on the model | LLM agent via `--graph-factory` |

</details>

## Limitations

- **One record type.** Experiments are about "create one record per request" (tickets, orders, invoices…) with an optional idempotency key. Other kinds of side effects need a new invariant.
- **Two intercepted calls.** Only the injected `create` and `lookup` callables are faulted. Anything else your agent does is outside the experiment.
- **Simulated network faults.** Timeouts and lost responses happen in the tool adapter, not on the wire. Process kills are real.
- **No benchmark claims.** The bundled agents are scripted to pass or fail, so they demonstrate the lab rather than discover anything. LLM results need many repetitions.
- **Not run in CI yet.** The workflows (Python 3.11–3.13, pinned actions, SBOM, provenance) have only been verified locally; see [`docs/VALIDATION.md`](docs/VALIDATION.md) for exactly what was run.
- **POSIX only for process kills.** Windows refuses those scenarios with a lab error.

## Related work

Overlapping tools exist, for example [afterstate](https://pypi.org/project/afterstate/) and [Dataoad](https://pypi.org/p/dataoad) (side-effect and idempotency testing), and AgentChaos and [AgentCheck](https://arxiv.org/abs/2607.11098) (fault injection into model and tool traffic). This project has not been compared against them by running them; [`docs/COMPETITIVE_POSITIONING.md`](docs/COMPETITIVE_POSITIONING.md) explains what overlaps and what is narrower here.

## Development

```bash
python -m pip install -e '.[dev,langgraph]'
FAULTLAB_REQUIRE_LANGGRAPH=1 python -m pytest -q
ruff check src tests examples && ruff format --check src tests examples
mypy src
python -m build
```

Without the `[langgraph]` extra, the LangGraph tests are skipped. CI sets `FAULTLAB_REQUIRE_LANGGRAPH=1` so they can never be silently skipped there.

```text
src/faultlab/
  engine.py           baseline / reset / fault phases, process isolation
  faults.py           the fault boundary around tool calls
  verification.py     deterministic invariants and verdicts
  targets.py          target contract; bundled ticket-service client
  service.py, storage.py   bundled ticket service and its SQLite store
  agent_worker.py     scripted reference agents
  langgraph_*.py      LangGraph adapter and worker (checkpoints, resume)
  replay.py           record and replay tool results
  reporter.py         JSON, HTML and JUnit reports
  ui.py, cli.py       local web UI and command line
```

Design decisions are recorded in [`docs/adr/`](docs/adr/). Also see [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md), [`docs/TEST_MATRIX.md`](docs/TEST_MATRIX.md) and [`docs/THREAT_MODEL.md`](docs/THREAT_MODEL.md). The repository includes guidance for AI coding assistants ([`AGENTS.md`](AGENTS.md), [`CLAUDE.md`](CLAUDE.md), [`prompts/`](prompts/)).

## Security and license

Everything binds to `127.0.0.1`, uses a random per-run token and stays offline unless you opt in to an LLM provider. `--graph-factory` and `--target` run your own code with your permissions, so pass only code you trust. Reports and tapes contain task text; review them before sharing. See [`SECURITY.md`](SECURITY.md) and [`CONTRIBUTING.md`](CONTRIBUTING.md).

MIT licensed; see [LICENSE](LICENSE).
