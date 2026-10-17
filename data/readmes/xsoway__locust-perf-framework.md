<p align="center">
  <a href="https://github.com/xsoway/locust-perf-framework"><img alt="GitHub" src="https://img.shields.io/badge/version-v0.1.1-gold?style=flat-square"></a>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-green?style=flat-square"></a>
  <a href="https://github.com/xsoway/locust-perf-framework/releases"><img alt="Release" src="https://img.shields.io/badge/release-v0.1.1-blue?style=flat-square"></a>
  <a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/Python-3.11+-red?style=flat-square"></a>
</p>

<h1 align="center">locust-perf-framework</h1>

<p align="center">A generic Python + Locust performance-testing framework: plan → script → data → execution record → Chinese report → LLM analysis.</p>
<p align="center"><a href="./README.zh-CN.md">中文</a> · <a href="https://xsoway.github.io/locust-perf-framework/">Homepage</a></p>
<p align="center">Reproducible · Traceable · Reportable · Agent-ready</p>
<hr>

## Contents

- [What is it](#what-is-it)
- [Why](#why)
- [Core concepts](#core-concepts)
- [Structure](#structure)
- [Quick start](#quick-start)
- [Features & usage](#features--usage)
- [Configuration](#configuration)
- [AI-agent collaboration](#ai-agent-collaboration-codex--claude-code--dsh)
- [Testing](#testing)
- [Safety](#safety)
- [FAQ](#faq)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Versioning](#versioning)
- [License](#license)
- [Maintainer](#maintainer)

## What is it

This framework is not a Locust replacement. It adds an engineering-oriented organization layer on top of Locust: unified directory boundaries, naming rules, collision-proof timestamped artifact management, wrapped commands, and turning raw Locust CSV into decision-ready Chinese HTML reports.

## Why

Common pain points when using raw Locust for performance testing:

| Pain point | This solution |
| --- | --- |
| Scripts/data/reports scattered, naming inconsistent | Layered conventions + naming rules, clear boundaries |
| Re-runs overwrite history, no comparison | Every run gets a timestamped dir; existing targets auto-append a sequence |
| Low-level Locust commands are complex and error-prone | User-facing entrypoints wrapped in `tools/`, only essential params exposed |
| Raw CSV is hard to present | Refined into Chinese HTML reports with TPS / RT / error-rate trends |
| Reports list metrics but never conclude | LLM-assisted summary + evidence-chain / falsification / remedy-and-reverify discipline |

## Core concepts

- **Layered boundaries**: `locustfiles/` scripts, `data/` data, `reports/` raw+refined, `logs/` logs, `config/` config.
- **Auto timestamping / no-overwrite**: every run gets a fresh timestamped dir; existing targets auto-append a sequence number.
- **One-command entrypoints**: `uv run python -m tools.xxx ...` auto-creates timestamped dirs, Locust raw artifacts, failure-detail JSONL, and Chinese HTML reports.
- **LLM-assisted analysis (optional)**: `config/ai_apiclient.py` (OpenAI-compatible wrapper) appends an AI summary; credentials via env vars.
- **Agent-ready**: built-in three-agent rules (plan → script development → report analysis); Codex / Claude Code / DSH can drive the whole flow in natural language.
- **Step-load ramp**: `tools/run_step_load.py` ramps load step by step and detects the TPS knee and error-rate breaking point, with circuit-breaking.
- **Bottleneck pattern library**: `docs/performance_known_issues.md` captures common bottlenecks (slow SQL, connection pools, Redis hotspots, GC storms, …).
- **Multi-source monitoring**: Prometheus resource CSV + slow-query JSONL as a second layer of cross-validation.
- **Pre-flight check**: `tools/preflight.py` detects placeholder hosts, placeholder creds, and environment alignment before a real run.

## Structure

```text
.
├── AGENTS.md                 # Agent rules entry (boundaries/naming/no-overwrite/conventions)
├── agents/                   # plan / script-development / report-analysis agent templates
├── config/
│   ├── config.ini            # run config (host, env, wait times, logging)
│   ├── ai_apiclient.py       # LLM call wrapper (env-var driven)
│   └── performance_profile.yaml
├── data/
│   └── examples/             # sanitized example data (scripts default here)
├── docs/                     # workflow & report design
├── examples/                 # public end-to-end load-test examples (incl. ready reports)
├── locustfiles/              # Locust load-test scripts
├── logs/                     # framework run logs (not committed)
├── reports/                  # raw/ artifacts, html/ Chinese reports, analysis/ intermediates
├── tools/                    # naming/logging/report-generation/run wrappers
└── tests/                    # self-contained unit tests (no network, no real LLM)
```

## Quick start

### Install

```bash
# Requires Python >= 3.11; uv recommended
uv sync --extra dev
# or with pip:
pip install -e .[dev]
```

### Explore the public examples

The `examples/` directory holds **end-to-end** sanitized load-test examples (scripts, data, raw artifacts, and finished Chinese HTML reports) — good to inspect before reproducing, and to understand the standard flow and test types:

| Example | Scenario / Type | Demonstrates | Report |
| --- | --- | --- | --- |
| [`health-check-demo`](examples/health-check-demo/) | Health check · baseline/load | single-step baseline + step-load knee | `report.html` |
| [`pressure-test-demo`](examples/pressure-test-demo/) | Health check · stress | load until service overload; breaking point & circuit-break | `report.html` |

```bash
# Open a finished example report directly
open examples/health-check-demo/report.html
open examples/pressure-test-demo/report.html
```

Each example `README.md` gives one-shot reproducible commands (start local mock service → pre-flight → load test → generate report). See [`examples/README.md`](examples/README.md) for the full list.

### Run an example scenario (health check)

```bash
uv run locust -f locustfiles/locust_demo_health_baseline.py \
  --headless -u 1 -r 1 -t 10s
```

The default host is read from `config/config.ini` (repo placeholder `https://example.com`). Override with `LOCUST_TARGET_HOST`:

```bash
LOCUST_TARGET_HOST=https://your-service.example.com uv run locust \
  -f locustfiles/locust_demo_health_baseline.py --headless -u 1 -r 1 -t 10s
```

### One-command entrypoints

Each scenario is wrapped as `uv run python -m tools.xxx ...`, auto-creating a timestamped dir, Locust raw artifacts, failure-detail JSONL, and a Chinese HTML report:

```bash
# Baseline: health check
uv run python -m tools.report_builder \
  --scenario demo_health --test-type baseline \
  --stats-csv reports/raw/demo_health/<timestamp>/stats_stats.csv \
  --overview "Example: health-check baseline" \
  --plan "1 virtual user for 10s to establish a response-time baseline" \
  --users 1 --spawn-rate "1 user/s" --run-time "10s" \
  --host "https://example.com" \
  --data-file "data/examples/demo_health_payloads.csv" \
  --api-name "health check" --method GET --path /health

# Step-load ramp (capacity / stress):
uv run python -m tools.run_step_load \
  --locustfile locustfiles/locust_demo_health_baseline.py \
  --steps "10,30,50,80,100" --step-duration 30s \
  --scenario demo_health --host https://your-service.example.com
```

All entrypoints support `--host` / `--path` / `--data-file` / `--url-file` overrides; if a network or LLM gateway is unavailable, add `--no-llm-analysis` to skip the AI summary.

**Run a pre-flight check before real load** to avoid hitting a placeholder environment or placeholder-credentialed data:

```bash
uv run python -m tools.preflight \
  --host https://your-service.example.com \
  --data-file data/examples/demo_health_payloads.csv
```

> If you only need raw Locust artifacts (no refined report), use the underlying `locust` command directly (see `tools/run_*.py` help).

## Features & usage

- 📁 **Layered conventions**: unified directory boundaries and naming; scripts describe behavior, data is read from `data/`.
- 🔒 **Auto timestamping / no-overwrite**: timestamped dirs + auto-append sequence numbers.
- 🚀 **One-command entrypoints**: expose only essential params (users, rate, time, target, data).
- 🧾 **Chinese HTML reports**: TPS / RT / error-rate trends, per-request bottlenecks, call-chain heatmaps.
- 🤖 **LLM-assisted analysis (optional)**: OpenAI-compatible wrapper appends an AI summary.
- 🧑‍💻 **AI-agent collaboration**: three-agent rules; natural-language, full-flow load testing.
- 📈 **Step-load ramp**: detects TPS knee and error-rate breaking point, with circuit-breaking.
- 🔍 **Bottleneck pattern library**: documented common bottleneck patterns.
- 📊 **Multi-source monitoring**: Prometheus / slow-query cross-validation.
- 🩺 **Pre-flight check**: avoid hitting blank/placeholder environments.
- 🧼 **Sensitive data not committed by default**: `.gitignore` excludes real data; only sanitized examples stay.

## Configuration

| Env var | Purpose | Default |
| --- | --- | --- |
| `LOCUST_TARGET_HOST` | Target service root (overrides `config.ini host`) | `https://example.com` |
| `AI_APICLIENT_BASE_URL` | LLM gateway base_url (OpenAI-compatible) | `http://localhost:8000/v1` |
| `AI_APICLIENT_API_KEY` | LLM API key | `not-configured` |
| `AI_APICLIENT_MODEL` | Model name | `demo-model` |
| `AI_APICLIENT_EXTRA_HEADERS` | Extra headers forwarded to the gateway (JSON) | empty |

LLM analysis is an optional enhancement: with no env config it never calls out; alternatively pass `--no-llm-analysis` to skip. **Never commit real credentials.**

## AI-agent collaboration (Codex / Claude Code / DSH)

This project is **natively AI-tool friendly (Codex, Claude Code, DeepSeek Harness, …)**:
the repo embeds a three-agent collaboration rule set (plan → script development → report analysis). When any Agentic tool opens the project root, it **automatically reads `AGENTS.md` and `agents/*.md`** and gains the domain rules for the whole load-test flow (naming, boundaries, no-overwrite, metric definitions, circuit-break red lines, report discipline), so you can drive a complete load test in natural language.

### Three-agent workflow

| Agent | Instruction file | Responsibility | Input → Output |
| --- | --- | --- | --- |
| **Planning** | [`agents/planning_agent.md`](agents/planning_agent.md) | Confirm context, API, test type, concurrency model, metrics, circuit-break/exit conditions | conversation → structured plan (YAML) |
| **Script development** | [`agents/script_development_agent.md`](agents/script_development_agent.md) | Generate Locust scripts, data files, run commands per plan | plan → `locustfiles/` + `data/` artifacts |
| **Report analysis** | [`agents/report_analysis_agent.md`](agents/report_analysis_agent.md) | Evidence-chain attribution, prioritized remediation and re-run plan | raw artifacts → decision-grade `reports/html/` |

> 🪄 Want to talk directly? [`docs/agent_prompts.md`](docs/agent_prompts.md) offers **one-shot full flow / step-by-step / advanced-tuning** copy-paste prompt templates.

### Typical conversation flow

**Step 1 — tell the planning agent your goal** (it confirms items per `planning_agent.md`):

> "Plan a pre-launch single-API baseline test for `POST /api/v1/orders`, ~10K DAU. Goal: find the slowest endpoint and error rate."

The planning agent confirms: context, API/auth/body, goal→strategy, concurrency, environment alignment, data source, capacity estimate, SLA thresholds and circuit-break red lines, then outputs a structured plan.

**Step 2 — hand off to the script-development agent**:

> "Generate the Locust scripts and data files per the plan."

It produces scripts named `locust_<domain>_<api>_<test_type>.py`, sanitized data, and one-command run commands.

**Step 3 — hand off to the report-analysis agent**:

> "Analyze `reports/raw/orders/20260910_120000/` and generate a Chinese report."

It reads the raw CSV/failure details and, following "multi-metric evidence chain + falsification + remedy & re-run" discipline, produces a decision-ready Chinese HTML report.

### Per-AI-tool usage

- **Codex**: open a session in the project root, describe the load-test goal, let it do plan→script→exec→report under `AGENTS.md`.
- **Claude Code**: enter the project root; the tool loads `CLAUDE.md` / `AGENTS.md` / `agents/*.md`; drive it in natural language, stage by stage.
- **DSH / other agents**: have the agent read the rule files above before starting.

### Load agent instructions programmatically

To reuse these instructions in code or orchestration (e.g. `openai-agent-framework-py`), call `agents/performance_agents.py`:

```python
from agents.performance_agents import load_agent_instruction

planning   = load_agent_instruction("planning")            # planning agent
dev        = load_agent_instruction("script_development")  # script-development agent
analysis   = load_agent_instruction("report_analysis")     # report-analysis agent
```

## Testing

Tests are self-contained: no network, no real LLM (Fake responses):

```bash
uv run pytest
uv run ruff check .
```

Release governance entrypoints (with `scripts/check_secrets.py`): `make test` / `make check` / `make code-clean`.

## Safety

- **Sensitive data not committed by default**: `.gitignore` excludes real `data/` txt/json/csv and `reports/`/`logs/` artifacts.
- **Credentials via env vars**: `config/ai_apiclient.py` reads only env vars, default `not-configured`; **never commit real keys**.
- **LLM analysis off by default**: no env config → never calls out; pass `--no-llm-analysis` to skip.
- **Release red line**: `scripts/check_secrets.py` scans all `.md/.yaml/.yml/.py/.html/.toml` for secrets / absolute local paths; any hit fails.

## FAQ

**Do I need an LLM credential?**
No. LLM analysis is optional; without env config it never calls out (add `--no-llm-analysis` to skip).

**Will it overwrite old reports?**
No. Every run gets a fresh timestamped dir; existing targets auto-append a sequence number.

**Does real data get committed?**
No. `.gitignore` excludes real business data and `reports/`/`logs/` artifacts; only sanitized examples remain.

**How do I pick a test type?**
Baseline (establish baseline) / Load (normal) / Stress (find breaking point) / Stability (soak) / Peak (burst), chosen by goal.

## Roadmap

- [x] One-command entrypoints (step-load ramp / Chinese report / preflight)
- [x] Multi-source monitoring (Prometheus + slow query)
- [x] AI-agent collaboration (three-agent rules)
- [x] Bilingual README and project homepage
- [ ] More example scenarios (login/auth, paginated lists, mixed load)
- [ ] Report PDF export / alert integration

## Contributing

PRs welcome. Please:

1. Follow `AGENTS.md` naming, boundaries, and the "no-overwrite reports" rule.
2. **Do not commit real business data or credentials**; put new data in `data/examples/` or generate locally.
3. New features/scripts should include a self-contained `tests/` case and pass `ruff check`.

Questions & discussion: [GitHub Discussions](https://github.com/xsoway/locust-perf-framework/discussions).

## Versioning

Semantic Versioning; see [CHANGELOG.md](CHANGELOG.md). Each release posts on
[GitHub Releases](https://github.com/xsoway/locust-perf-framework/releases) with change notes and
downloadable sdist/wheel artifacts built via `uv build`.

## License

[MIT](LICENSE)

## Maintainer

- GitHub: [@xsoway](https://github.com/xsoway)