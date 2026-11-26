# agent-mcts 🌳

**Run Claude Code as a tree search instead of a single attempt.**

On two tasks with a written spec, the answer agent-mcts returned beat its own first attempt, which is what a single Claude Code run would have returned, in **16 of 20 runs**, and was worse in 2. On average it passed 93% of the hidden tests instead of 88%, at about $2.44 and 19 minutes per run with `haiku` ([results and caveats](#does-it-help)).

```bash
uv tool install agent-mcts
agent-mcts run --generate-tests "implement the spec in README.md"
```

`agent-mcts` is an open-source (MIT) test-time search harness that wraps a coding agent CLI with Monte Carlo Tree Search. Each attempt runs in its own git worktree and is scored on tests: yours, plus tests an agent writes from the task. The most promising attempts get revised, and your working tree is untouched until you `apply` a result. It is verified with Claude Code; a Codex CLI adapter ships too, untested against the real CLI ([Supported agents](#supported-agents)).

![agent-mcts searching, applying the best branch, and the resulting diff](demo/demo.gif)

> **Status: v0.4.** Early but real — the full loop (search → live tree → apply) works today with Claude Code. A Codex CLI adapter ships too, but so far it has only been tested against a fake `codex` binary. Built in the open; star the repo to follow along, or [jump in](#contributing) — early contributors shape the architecture.

## Does it help?

With generated tests, yes, on tasks with a written spec; on a vague bug report, so far only as much as the judge ([bench/](bench/README.md), Claude Code with `haiku`, 5-episode budget). Each answer is scored on hidden tests the agent never sees, and compared with the first attempt of the same run, which is what a single agent run would have returned. Two tasks with a spec (npm semver ranges, ISO 8601 durations), 20 runs per setting:

| | answer better than the first attempt | same | worse | mean change | worst answer | wall time | cost per run |
|---|---:|---:|---:|---:|---:|---:|---:|
| agent-mcts, tests only | 1 | 18 | 1 | −0.6 pt | 39% | ~5 min | $0.43 |
| agent-mcts, with `--judge` | 11 | 5 | 4 | +5.4 pt | 68% | ~21 min | $1.81 |
| agent-mcts, with `--generate-tests` | **16** | 2 | **2** | +4.8 pt | **81%** | ~19 min | $2.44 |

What the per-run numbers show:

- **Generated tests beat a single run.** Before the search, an agent writes tests from the task and the code as it stands; every attempt is then scored on them. The answer improved in 16 of 20 runs and got worse in 2, by 1 and 4 points. Mean share of hidden tests passed: 88% for the first attempt, 93% for the answer returned.
- **Revisions with test feedback help.** A failing generated test tells the next attempt what to fix: 32 of 40 revisions raised the hidden score, against 13 of 40 with the judge. In 13 of 20 runs the answer beat all three first attempts.
- **The same budget spent more simply did as well.** Five first attempts picked by the same generated tests (best-of-N) passed 93% of hidden tests, and one attempt revised four times in a chain passed 92%, against 93% for the tree. Over 20 paired runs no difference was detected: search minus best-of-N was +0.1 pt (95% interval −3.7 to +3.9), search minus the chain +1.5 pt (−2.5 to +5.5). So the gain over a single run is not yet shown to need the tree; a larger budget or harder tasks may change this. Details in [#35](https://github.com/natsu0529/agent-mcts/issues/35) and [#36](https://github.com/natsu0529/agent-mcts/issues/36).
- **The judge reads diffs, and that is not enough.** Its mean gain comes from rescuing two broken first attempts (19% and 37%). Over the other 18 runs it averaged +0.0 pt, and in one it replaced a 91% first attempt with a 68% one.
- **With the judge, two or three episodes are enough.** We cut the saved judge trees short: 36 runs over the bench tasks, including three from the first measurement. The search builds one attempt at a time, so a cut tree is the tree a shorter search would have built. Over these runs the gain stops after the second or third attempt. The best of the first two by reward passed 91.8% of hidden tests at $0.68 per run, the best of the first three 91.9% at $1.02, and the full five 91.3% at $1.82. With `--judge`, `-n 2` or `-n 3` gets the same answers at a third to a half of the cost. Since the root takes three first attempts, `-n 2` means two first attempts and no revision. With generated tests, keep 4 or more: the gain grows until the fourth attempt. Details in [#38](https://github.com/natsu0529/agent-mcts/issues/38).
- **Tests-only search is close to a single run.** It stops at the first attempt that passes the visible tests.

**A vague bug report is harder.** A third task gives the agent only a user's report that Japanese text misaligns a table (10 runs per setting). The test writer made the same mistake as the bug, measuring alignment in characters, so the unfixed code passed its tests and every fix failed them, and v0.4.0 returned the unfixed code in all 10 runs. agent-mcts now offers the unchanged code only when every attempt does worse on your own tests, and warns when the generated tests preferred it. On the same ten trees that gives 4 runs better than the first attempt and none worse (88% → 93%), level with the judge (3 better, none worse, 91% → 93%).

Caveats: three small tasks, one model, 10 to 20 runs per setting. Details in the [full report](bench/results/REPORT.md).

## Why

Production coding agents (Claude Code, Codex, Kimi, ...) run a **single linear loop**: act, observe, retry in place. No branching, no backtracking, no principled exploration.

Research shows search helps: [SWE-Search (ICLR 2025)](https://arxiv.org/abs/2410.20285) reported a ~23% relative improvement on SWE-bench by adding MCTS on top of software agents. But that result lives in a research framework — there is no tool that brings it to the agent you already use.

`agent-mcts` closes that gap:

- **Bring your own agent.** A thin adapter layer speaks to each agent's headless mode (`claude -p`; `codex exec` untested against the real CLI; `kimi -p` planned). The search engine never knows which agent it's driving.
- **Real MCTS.** UCT selection, expansion, evaluation, backup. Budget flows toward branches that look promising, away from dead ends. At a 5-episode budget on the bench, the tree has not yet beaten simpler ways of spending the same episodes ([Does it help?](#does-it-help)).
- **State you can trust.** Every node is an isolated `git worktree` + a forked agent session. Your working tree is never touched until *you* apply a result.
- **Terminal-native.** Watch the tree grow live in your terminal. 100% Python, no browser required.

## Quickstart

```bash
uv tool install agent-mcts
cd your-project
agent-mcts run "fix the flaky test in tests/test_auth.py"
agent-mcts run --agent codex "fix the flaky test in tests/test_auth.py"   # untested with the real Codex CLI
```

The run auto-detects your installed agent and your test command, then shows the plan before spending anything:

```
Agent: claude · Value: pytest -x -q · Budget: 12 nodes / $10.00
Proceed? [y/N]
```

While searching, the tree grows live in your terminal (real output):

```
task: fix the flaky test in tests/test_auth.py
run 20260802-190219 · episodes 3/12 · cost $0.31/$10.00
✓ n0 [r=0.00 Q=0.42 N=4]
├── ✓ n1 [r=0.67 Q=0.78 N=2] mocked the clock in the auth fixture
│   └── ● n3 [r=? Q=0.00 N=0] expanding…
└── ✗ n2 [r=0.00 Q=0.00 N=1] sleep-based fix (tests timed out)
```

When it finishes (or when you Ctrl-C — MCTS is anytime, the partial tree is saved):

```bash
agent-mcts show        # inspect the tree; `show n3` prints a node's prompt, summary, evaluation
agent-mcts resume      # continue the latest run where it stopped (`resume -n 20` raises the budget)
agent-mcts apply       # stage the best node's changes (squash merge — you review and commit)
agent-mcts apply n2    # ...or pick a different branch
```

## How it works

```
                ┌─────────────────────────────┐
                │        search engine        │   UCT selection · expansion
                │   (agent-agnostic, Python)  │   hybrid value fn · backup
                └──────────────┬──────────────┘
                               │ AgentBackend protocol
            ┌──────────────────┼──────────────────┐
            ▼                  ▼                  ▼
     claude adapter      codex adapter      kimi adapter
      (claude -p)        (codex exec)        (kimi -p)
       verified          fake-tested          planned
```

- **Node = (git worktree, agent session).** Filesystem state branches via worktrees; conversation state branches via session forking (native on Claude Code, context-injection fallback elsewhere).
- **Value function = your tests.** Exit 0 scores 1.0; a failing run earns partial credit by pass ratio (read from pytest, jest, cargo test, go test and JUnit-style summaries), and the failing output is fed into children's revision prompts. `pytest` / `npm test` / `make test` are picked up automatically. Add `--generate-tests` to have an agent write extra tests from the task before the search and score every attempt on them too ([generated tests](docs/configuration.md#generated-tests)), or `--judge` to have an LLM score each attempt's diff ([LLM judge](docs/configuration.md#llm-judge)).
- **Every node is a git branch** (`agent-mcts/<run>/<node>`), so `apply` is an ordinary squash merge and everything is auditable after the fact. Worktrees are disposable; branches are the record.
- **Every state change is journaled** (append-only jsonl per run), so an interrupted search is still a valid, inspectable tree.

## Supported agents

| Agent | Headless | Session fork | Status |
|---|---|---|---|
| Claude Code | `claude -p` | native (`--fork-session`) | ✅ v0.1, verified |
| Codex CLI | `codex exec --json` | context injection | v0.2, tested only against a fake `codex` binary |
| Kimi CLI | `kimi -p` | context injection | planned (v0.5) |
| Gemini CLI, OpenCode, ... | | | [adapter PRs welcome!](#contributing) |

## Configuration

Zero config required. When you need it, `.agent-mcts.toml`:

```toml
agent = "claude"                  # or "codex"

[value]
command = "pytest tests/ -x -q"   # exit code + pass ratio → score in [0, 1]
generate_tests = true             # also score on tests an agent writes from the task

[search]
max_nodes = 20                    # episode budget
max_cost_usd = 10.0
parallelism = 3                   # episodes in flight at once (`-j`)
```

CLI flags (`--agent`, `-n`, `--max-cost`, `--value`, `--model`, `--agent-timeout`, `--generate-tests`, `--judge`, `-j/--parallel`) override the file.

> **Python projects managed with uv:** the value command runs inside fresh worktrees, which don't inherit your virtualenv — use `command = "uv run pytest -q"` (or pass `--value "uv run pytest -q"`) so each worktree resolves its own environment.

Every option, [generated tests](docs/configuration.md#generated-tests), the [LLM judge](docs/configuration.md#llm-judge), [parallel runs](docs/configuration.md#running-in-parallel), [resuming](docs/configuration.md#resuming-a-run) and how [failures, cost and timeouts](docs/configuration.md#failures-cost-and-timeouts) are handled: [docs/configuration.md](docs/configuration.md).

Search hyperparameters are first-class: this is built by an MCTS researcher and meant to double as a research harness for test-time search over real software tasks.

## Roadmap

- [x] **v0.1** — Claude Code adapter, UCT engine, worktree state, test-based value fn, live TUI
- [x] **v0.2** — Codex CLI adapter, episode-count budget for agents that report no dollar cost, recoverable timed-out and interrupted episodes
- [x] **v0.3** — LLM-as-judge value fn, final head-to-head selection, sibling ranking, `resume`, parallel expansion, selection policy knobs
- [x] **v0.4** — generated-tests value fn (`--generate-tests`), hidden-test benchmark in `bench/`
- [ ] **v0.5** — Kimi CLI adapter, in-agent activation (`/tree` inside Claude Code via MCP), search-tree export + richer visualization, benchmark mode (same task, N agents, compare trees)

## Contributing

This project is **open source under the MIT license** and developed fully in the open — issues, design discussions, and PRs all happen here on GitHub. Contributions are welcome from day one.

The highest-impact contribution is an **agent adapter**: a few hundred lines implementing the [`AgentBackend` protocol](src/agent_mcts/adapters/base.py) for your favorite CLI agent, with no need to touch the search core. Use the [Claude Code adapter](src/agent_mcts/adapters/claude_code.py) as the reference, and the fake-binary pattern in [its tests](tests/test_claude_adapter.py) to keep CI free of API calls. See [CONTRIBUTING.md](CONTRIBUTING.md) for setup.

Also welcome: bug reports, docs, benchmark tasks, and arguing with our UCT constants.

## License

[MIT](LICENSE) — do whatever you want, just keep the notice.
