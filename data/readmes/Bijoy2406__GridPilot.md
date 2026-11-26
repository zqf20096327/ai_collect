# Gridpilot AI

Multi-agent AI controller that plans a commercial site's solar, battery, flexible loads (HVAC, EV charging) and
diesel generator for the next 24 hours, to cut electricity cost and CO2. A deterministic optimiser makes every
decision; an LLM only explains them, using numbers from the other agents.

Entry for **ClimateSphere AI → Energy Brain** ("Smart energy optimization and demand response") at the
International AI Builders Congress 2026. Full product spec: [Gridpilot AI — PRD](Gridpilot%20AI%20%E2%80%94%20PRD.md).
Work is tracked in [GitHub Issues](https://github.com/Bijoy2406/Energy-Brain/issues) by phase label and milestone.

## Status

Phase 0 (setup) in progress. MVP and preliminary submission due **20 Nov 2026, 23:59 BST**; final submission
locks **24 Dec 2026, 24:00 BST**.

## Work plan (phases)

Each issue carries a phase label. Milestones: **MVP + Preliminary Submission (Nov 20)** and
**Final Submission (Dec 24)**.

| Phase | Issues | What it covers |
| --- | --- | --- |
| phase-0: setup | #1–#4 | Repo skeleton, site/asset spec, team roles and mentor notes, preliminary submission |
| phase-1: data & training | #5–#12 | Dhaka weather (NASA POWER + Open-Meteo), simulated solar output (pvlib), synthetic load, tariff and CO2 factor lookup, outage calendar, solar and load forecasters |
| phase-2: agents | #13–#26 | Schemas and orchestrator, the seven agents, FastAPI backend, plus P1 extras (cloud event, Pareto, Bangla, override, PDF report) |
| phase-3: frontend | #27–#33 | React scaffold, schedule chart, slider, chat, baseline comparison, deploy, polish |
| phase-4: final submission | #34–#40 | YouTube video, Data & AI provenance, tooling/MCP disclosure, prompt library, pitch, interviews, final checklist |

## Architecture (planned)

| Agent | Job | Issue |
| --- | --- | --- |
| Forecast | Solar + load forecast with P10/P50/P90 bands, 15-min steps | #14 |
| Signal | Tariff, grid CO2 factor, diesel cost/CO2, outage blocks per slot | #15 |
| Assets | Battery, HVAC, EV fleet, generator limits | #16 |
| Planner | MILP: minimise w × cost + (1 − w) × CO2 | #17 |
| Risk | Re-check plan at P10 solar, re-plan with margin | #18 |
| Explainer | LLM answers "why" questions from tool outputs only | #19 |
| Evaluator | Backtest against two rule-based baselines | #20 |

## Project layout

```
config/site.yaml          simulated site + asset spec (all values are documented assumptions)
src/energy_brain/
  config.py               loads and validates config/site.yaml
  data/                   weather download, PV simulation, synthetic load, outages
  forecast/               solar + load forecasters, Forecast agent
  signals/ assets/ planner/ risk/ explainer/ evaluator/   one package per agent
  api/                    FastAPI backend for the dashboard
  mcp_server/             read-only MCP server over the Explainer tools (docs/mcp.md)
web/                      React dashboard (set up in #27)
data/raw, data/processed  downloaded / generated data (git-ignored; re-create with scripts)
data/sample/              small committed samples for tests and teammates
models/                   trained models (git-ignored)
reports/                  forecast metrics and backtest results
prompts/                  LLM prompts (needed for the final Prompt Library)
notebooks/                exploration and sanity-check plots
docs/                     site spec, data sources, submission drafts
tests/                    pytest suite
```

## Setup

Requires **Python 3.11** (recommended; some ML wheels lag on the newest Python) and Git.

```bash
git clone https://github.com/Bijoy2406/Energy-Brain.git
cd Energy-Brain
```

Windows (PowerShell):

```powershell
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

macOS / Linux:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

`requirements.txt` installs this package in editable mode with dev tools (`pip install -e .[dev]`); the
dependency list lives in `pyproject.toml`.

Copy `.env.example` to `.env` and fill in keys when you need them. Never commit `.env`.

## Run checks

```bash
pytest          # tests, including validation of config/site.yaml
ruff check .    # lint
```

CI runs both on every pull request.

## Run the API (dashboard backend)

```bash
uvicorn energy_brain.api.app:app --reload --port 8000
```

Open http://localhost:8000/docs. Endpoints, response shapes and settings (`EB_CORS_ORIGINS`, `EB_EXPLAIN_CACHE`,
`EB_WARMUP`) are in [docs/api.md](docs/api.md); the contract for the frontend is
[docs/openapi.json](docs/openapi.json). Real plans need `data/processed/` and `models/`
([docs/data-sources.md](docs/data-sources.md)); without them the API still runs on the sample-data fallback and
says so in every response. `/explain` needs `LLM_API_KEY` in `.env` (Groq).

## Use GridPilot from an MCP client

A read-only MCP server (stdio) exposes the Explainer's tools for any day and weight, plus the data caveats,
site config and backtest summary. It needs no LLM key:

```bash
pip install -e ".[mcp]"
claude mcp add gridpilot -- python -m energy_brain.mcp_server
```

Tools, resources, prompts and client setup are in [docs/mcp.md](docs/mcp.md).

## Run the dashboard

The Vite + React + TypeScript frontend lives in `web/`. See
[Run frontend and backend together](web/README.md#run-frontend-and-backend-together) for setup,
API type generation, tests and builds. The backend runs on port 8000 and the frontend on port 5173.

## Deploy

Prepare and publish a Hugging Face Docker Space with the [deployment guide](docs/deploy.md).

## Using the site config

```python
from energy_brain.config import load_site_config

cfg = load_site_config()
cfg.battery.capacity_kwh      # 1000.0
cfg.planning.n_slots          # 96 slots of 15 minutes
```

Never hard-code site numbers in code; read them from the config. If you change `config/site.yaml`, run `pytest`
and update `docs/site-spec.md`.

## How we work

- One issue = one branch, named like `5-weather-download`. Open a pull request into `main` and link the issue
  (`Closes #5`). Someone else reviews before merge.
- Keep each phase in its own folders to avoid merge conflicts (data work in `data/` and `forecast/`, agents in
  their own packages, frontend in `web/`).
- Agent issues (#16–#21) can start with stub data before phase 1 is finished; see each issue.
- Shared data shapes are defined once (issue #13). Tell the team before changing a field.
- Label simulated and synthetic data everywhere it appears, and never put stub numbers in the pitch.
