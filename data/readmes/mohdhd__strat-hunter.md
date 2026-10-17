<p align="center">
  <img src="frontend/public/logo-wordmark.svg" alt="Strat Hunter" width="420">
</p>

# Strat Hunter

**Use AI coding assistants to investigate trading ideas and organize the results in a web dashboard.**

[Watch the 42-second demo](promo/output/strat-hunter-reddit.mp4) · [Report a bug](https://github.com/mohdhd/strat-hunter/issues)

Describe an idea in everyday language. Strat Hunter starts a coding assistant that writes strategy code, runs historical simulations (backtests), and records its attempts. You can watch progress, ask questions, stop a job, and download a strategy for further review.

This is an experimental research application for **one trusted operator**. You do not need to write code to use the dashboard, but installation requires copying commands into a terminal, logging into an AI provider, and occasionally reading logs. Generated strategies and reported results need human review.

## Start here

| What you want to do | Guide |
|---|---|
| Install and open the dashboard | **[Docker installation](DOCKER.md)** — recommended for newcomers |
| Run your first research job | [First-job walkthrough](docs/USER_GUIDE.md) |
| Change budgets, paths, or market data | [Configuration reference](docs/CONFIGURATION.md) |
| Fix an installation or job problem | [Troubleshooting](docs/TROUBLESHOOTING.md) |
| Stop, back up, update, or restore | [Maintenance guide](docs/MAINTENANCE.md) |
| Review changes before updating | [Changelog](CHANGELOG.md) |
| Run from source or contribute | [Contributing](CONTRIBUTING.md) |
| Understand access and credentials | [Security model](SECURITY.md) |
| Understand the code and its limits | [Architecture](docs/ARCHITECTURE.md) |

## What it can do

- **Research your idea:** choose an assistant, market, instruments, timeframe, and limits. The assistant iterates and saves code and logs.
- **Scout for ideas:** run a scanner batch, review proposed hypotheses, and greenlight one into a research job (a “hunt”). Recurring scans are optional and must be started explicitly.
- **Compare results:** inspect iteration history, reports, strategy lineage, and independent validation results when available.
- **Discuss and extend:** chat with a sidekick that can read **and modify** a job's files and run additional experiments.
- **Export:** download a ZIP containing strategy code, metrics, and engine-specific instructions. Data and provider credentials are not bundled automatically.

| Engine | Intended use | Data notes |
|---|---|---|
| Freqtrade | Crypto futures; the built-in workflow assumes Binance USDT futures | Public exchange candle downloads; availability depends on your location and the exchange |
| NautilusTrader | FX, equities, ETFs, futures, crypto, prediction-market research | Yahoo-backed markets can be seeded; other instruments may require the agent to acquire and prepare data |

Optional Tiingo credentials enable additional intraday data for FX, equities, and ETFs. A market appearing in a menu does not guarantee available data or a ready-to-run strategy.

## Quick start

Install [Docker Desktop](https://docs.docker.com/desktop/) and start it. Download this repository using **Code → Download ZIP**, extract it, and open a terminal in the extracted `strat-hunter` folder. Then run:

```bash
docker compose up -d --build --wait
```

Open **[http://localhost:3000](http://localhost:3000)**. On first boot, the backend creates a research configuration with paper trading enabled and no exchange keys. Log into **one** included AI assistant inside the backend, for example:

```bash
docker compose exec backend claude
```

Complete its login flow, then exit the assistant. Continue with the [full installation guide](DOCKER.md) and [first-job walkthrough](docs/USER_GUIDE.md). The dashboard can open before an assistant is authenticated; starting research requires a working assistant account.

## Before running research

**Costs:** AI provider subscriptions or API usage and optional data services may cost money. Strat Hunter does not supply these accounts. Begin with one job and a small iteration/time budget. The dollar limit is **not a dependable billing cap**: generic CLI agents do not provide reliable cost accounting to this application. Use your provider's spending controls where available.

**Access:** the dashboard and API have no application login. They can launch programs and modify files. Docker publishes both ports only to this computer by default. Keep that setting; use an SSH tunnel for remote access. Agents run with broad permissions inside their execution environment. A job directory is not a security sandbox.

**Results:** a backtest is a simulation using historical data, not a prediction. “Done” means the agent reported completion, not that a strategy is safe or profitable. Verification hooks and extra backtests help find mistakes, but cannot prove agent honesty or rule out overfitting. Missing validation means **unvalidated**, not passed. Research does not require depositing funds or entering exchange trading keys.

## Project layout

```text
backend/             Python API, job supervision, data services, tests
frontend/            Browser dashboard
templates/          Instructions and verification hooks given to job agents
examples/            Research-only Freqtrade configuration
docker/              Backend image and first-boot setup
docs/                User and contributor references
docker-compose.yml   Starts the backend and dashboard together
```

The [architecture guide](docs/ARCHITECTURE.md) distinguishes implemented behavior from experimental or incomplete checks. Older design notes under `docs/superpowers/` record development intentions and are not installation instructions.

## Contributing and licensing

Bug reports, documentation improvements, and reproducible tests are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md). Do not include account tokens or private research in public reports.

Strat Hunter is available under the [MIT License](LICENSE). Third-party dependencies and tools retain their own licenses.
