<div align="center">

# Autoresearch CLI

**Run autonomous AI experiments while you sleep. Wake up to results.**

<br />

[![Star this repo](https://img.shields.io/github/stars/paperfoot/autoresearch-cli?style=for-the-badge&logo=github&label=%E2%AD%90%20Star%20this%20repo&color=yellow)](https://github.com/paperfoot/autoresearch-cli/stargazers)
&nbsp;&nbsp;
[![Follow @longevityboris](https://img.shields.io/badge/Follow_%40longevityboris-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/longevityboris)

<br />

[![Crates.io](https://img.shields.io/crates/v/autoresearch?style=for-the-badge&logo=rust&logoColor=white&label=crates.io)](https://crates.io/crates/autoresearch)
[![Downloads](https://img.shields.io/crates/d/autoresearch?style=for-the-badge&logo=rust&logoColor=white)](https://crates.io/crates/autoresearch)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/paperfoot/autoresearch-cli/release.yml?style=for-the-badge&logo=github&label=CI)](https://github.com/paperfoot/autoresearch-cli/actions)

---

A single Rust binary that turns any AI coding agent into an autonomous research machine. Define one file to modify, one metric to optimize, and one eval command. Your agent handles the rest -- running experiments, tracking results, keeping winners, reverting losers. You sleep. It works.

[Install](#install) | [How It Works](#how-it-works) | [Features](#features) | [Contributing](#contributing)

</div>

## Why Autonomous Research Matters

Karpathy's [autoresearch](https://github.com/karpathy/autoresearch) ran 126 ML experiments overnight on a single GPU. Since then, people have applied the same pattern to [chess engines](https://x.com/MindCanvasx/status/2035817965614940472) (expert to grandmaster), [Bitcoin modeling](https://x.com/xmal/status/2035735100516634805) (halved prediction errors), [Sudoku solvers](https://x.com/VihariKanukollu/status/2035411680050778435) (beat the paper in 5 minutes), and [running 400B models on laptops](https://x.com/DAIEvolutionHub/status/2034899294709588419).

The pattern is simple: **one file to modify, one metric to optimize, one loop that never stops.**

But every project reimplements this from scratch -- copying `program.md`, figuring out the eval, hand-writing JSONL logs. This CLI makes the autonomous experiment loop a `cargo install` away. It works with any AI coding agent that can shell out to a command.

## Install

**One-liner (macOS / Linux):**
```bash
curl -LsSf https://github.com/paperfoot/autoresearch-cli/releases/latest/download/autoresearch-installer.sh | sh
```

**Homebrew:**
```bash
brew tap 199-biotechnologies/tap
brew install autoresearch
```

**Cargo (from [crates.io](https://crates.io/crates/autoresearch)):**
```bash
cargo install autoresearch
```

Binary size: ~1.1 MB. Startup: ~2 ms. Memory: ~3 MB. No Python, no Node, no Docker.

## Quick Start

```bash
# 1. Install the research skill into your AI agent
autoresearch install claude-code    # or: all, codex, cursor, windsurf, opencode

# 2. Set up your project for experiment tracking
autoresearch init \
  --target-file train.py \
  --eval-command "python train.py" \
  --metric-name val_bpb \
  --metric-direction lower \
  --time-budget 5m

# 3. Validate everything is ready
autoresearch doctor

# 4. Tell your agent to start
/autoresearch

# 5. Go to sleep. Wake up to results.
autoresearch status
autoresearch best
autoresearch report
```

## How It Works

```
You write program.md          Your AI agent runs the loop
     ┌──────────┐          ┌──────────────────────┐
     │  Ideas   │          │  1. Read program.md   │
     │  Papers  │ ───────► │  2. Modify target     │
     │  Goals   │          │  3. Commit            │
     └──────────┘          │  4. Eval (timeout)    │
                           │  5. Keep or revert    │
autoresearch.toml           │  6. autoresearch      │
     ┌──────────┐          │     record --metric   │
     │ target   │ ───────► │  7. Repeat forever    │
     │ eval_cmd │          └──────────────────────┘
     │ metric   │                    │
     └──────────┘                    ▼
                           .autoresearch/
                           experiments.jsonl
                           ┌─────────────────────┐
                           │ run 0: 1.050 baseline│
                           │ run 1: 1.042 kept    │
                           │ run 2: 1.055 discard │
                           │ run 3: 1.031 kept    │
                           └─────────────────────┘
```

The CLI handles everything except the loop itself:
- **Scaffolding** -- `init` creates the config and research prompt
- **Validation** -- `doctor` runs 14 pre-flight checks before you start
- **State management** -- `record` handles JSONL atomically (agents never hand-write JSON)
- **Experiment tracking** -- `log`, `best`, `diff`, `status` parse results from git + JSONL
- **Reporting** -- `report` generates a shareable markdown summary

Your agent handles the creative work -- deciding what to try, implementing changes, interpreting results.

## Features

### AI Coding Agent Support

Works with every major AI coding agent out of the box:

| Agent | Install command | Slash command |
|-------|----------------|:---:|
| [Claude Code](https://github.com/anthropics/claude-code) | `autoresearch install claude-code` | `/autoresearch` |
| [Codex CLI](https://github.com/openai/codex) | `autoresearch install codex` | `/autoresearch` |
| [OpenCode](https://github.com/opencode-ai/opencode) | `autoresearch install opencode` | `/autoresearch` |
| [Cursor](https://cursor.com) | `autoresearch install cursor` | auto-discovered |
| [Windsurf](https://windsurf.com) | `autoresearch install windsurf` | auto-discovered |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | `autoresearch install gemini` | auto-discovered |
| [GitHub Copilot](https://github.com/features/copilot) | `autoresearch install copilot` | auto-discovered |
| Augment / Goose / Roo | `autoresearch install all` | auto-discovered |

No skill needed? Run `autoresearch guide` for the full methodology. The CLI coaches agents through hints in every response.

### Full Command Reference

| Command | What it does | Agent-facing |
|---------|-------------|:---:|
| `install <target>` | Install the autoresearch skill into an AI agent | |
| `init` | Scaffold project (`autoresearch.toml` + `program.md`) | |
| `doctor` | 14-point pre-flight check | * |
| `record` | Record experiment result (JSONL, run numbering, deltas) | * |
| `log` | Show experiment history with metrics and status | * |
| `best` | Show best experiment + diff from baseline | * |
| `diff <a> <b>` | Compare two experiments side-by-side | * |
| `status` | Project state, best metric, loop progress | * |
| `export` | Export as CSV, JSON, or JSONL | |
| `fork <names...>` | Branch into parallel experiment directions | |
| `review` | Generate cross-model review prompt with pattern detection | * |
| `watch` | Live terminal dashboard for real-time monitoring | |
| `merge-best` | Compare fork branches and pick the winner | * |
| `report` | Generate full markdown research report | |
| `agent-info` | Machine-readable capability metadata | * |

All commands support `--json` for structured output. Auto-enabled when piped.

Agent-facing commands (`*`) return consistent JSON envelopes with semantic exit codes (0=success, 1=runtime error, 2=config error) and actionable `suggestion` fields on errors.

### Multi-Direction Experiment Exploration

Fork your experiments into parallel branches and let multiple agents explore different directions at the same time:

```bash
# Create parallel experiment branches
autoresearch fork try-transformers try-convolutions try-linear

# Start a separate agent on each
git checkout autoresearch-fork-try-transformers && /autoresearch

# Compare results and pick the winner
autoresearch merge-best
```

### Cross-Model Review for AI Experiments

After running experiments, get a second model to review your progress:

```bash
autoresearch review --json | jq -r '.data.review_prompt'
```

Generates a structured review prompt with session summaries, pattern detection (stuck detection, repeated failure themes), and suggested next directions. Pipe to Codex or Gemini for cross-model insights that break local minima.

### Live Experiment Dashboard

Monitor experiments in real time from another terminal:

```bash
autoresearch watch
```

Shows a live-updating dashboard with sparkline progress, kept/discarded rates, best metric, and new experiment notifications. Refreshes every 2 seconds (configurable with `-i`).

## Configuration

`autoresearch.toml`:
```toml
target_file = "train.py"           # The single file the agent may modify
eval_command = "python train.py"   # Must print the metric to stdout
metric_name = "val_bpb"            # What the metric is called
metric_direction = "lower"         # "lower" or "higher"
time_budget = "5m"                 # Max time per experiment
branch = "autoresearch"            # Git branch for experiments
```

`program.md` is free-form -- tell the agent what to explore, link papers, set constraints. The agent reads it between experiments for inspiration.

## What People Are Building

The autonomous research pattern works on **anything with a measurable metric**:

| Domain | Metric | Result |
|--------|--------|--------|
| ML training | val_bpb | 126 experiments overnight, 11% improvement |
| Chess engine | Elo rating | Expert to Grandmaster (2718 Elo) |
| Bitcoin modeling | Prediction error | Halved error in one morning |
| Sudoku solver | Accuracy | Beat published paper (87% to 92.2%) |
| API latency | p99 ms | 37% reduction via KD-tree optimization |
| Trading bots | Score | 43,000% improvement via evolutionary loop |

## Contributing

Contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Inspired By

- [Karpathy's autoresearch](https://github.com/karpathy/autoresearch) -- the original pattern
- [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) -- generalized Claude Code skill
- [ARIS](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) -- cross-model research pipeline
- [ResearcherSkill](https://github.com/krzysztofdudek/ResearcherSkill) -- domain-agnostic research agent
- [SkyPilot scaling](https://blog.skypilot.co/scaling-autoresearch/) -- multi-GPU parallel autoresearch

## License

MIT -- see [LICENSE](LICENSE).

---

<div align="center">

Built by [Boris Djordjevic](https://github.com/longevityboris) at [199 Biotechnologies](https://github.com/199-biotechnologies) | [Paperfoot AI](https://paperfoot.ai)

<br />

**If this is useful to you:**

[![Star this repo](https://img.shields.io/github/stars/paperfoot/autoresearch-cli?style=for-the-badge&logo=github&label=%E2%AD%90%20Star%20this%20repo&color=yellow)](https://github.com/paperfoot/autoresearch-cli/stargazers)
&nbsp;&nbsp;
[![Follow @longevityboris](https://img.shields.io/badge/Follow_%40longevityboris-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/longevityboris)

</div>
