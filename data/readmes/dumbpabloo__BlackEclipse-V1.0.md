<div align="center">

<img src=".github/assets/readme-hero.png" alt="Black Eclipse — an open-source agentic harness designed to help you automate finance" width="100%" />

<br />

**Agents that plan, call tools, run deterministic Python for the math, check their own
sources, and keep a durable record of what they did — on your machine, with your own model.**

<br />

[![Download for Windows](.github/assets/download-windows.svg)](https://github.com/dumbpabloo/BlackEclipse-V1.0/releases/latest/download/BlackEclipse-Setup.exe)

<sub>Windows 10/11 x64 · unsigned installer — [verify the SHA-256](#install) first · [all releases](https://github.com/dumbpabloo/BlackEclipse-V1.0/releases)</sub>

<br />

![MIT](https://img.shields.io/badge/core-MIT-green) ![Python 3.12](https://img.shields.io/badge/Python-3.12-3776AB?logo=python) ![Next.js 15](https://img.shields.io/badge/Next.js-15-black?logo=next.js) [![release](https://img.shields.io/github/v/release/dumbpabloo/BlackEclipse-V1.0?label=release)](https://github.com/dumbpabloo/BlackEclipse-V1.0/releases)

<br />

[**Features**](#features) · [**Use**](#use) · [**Needs**](#needs) · [**Install**](#install) · [**How it works**](#how-it-works) · [**Proof**](#proof) · [**Docs**](#documentation)

</div>

---

## What it is

Financial work is fragmented. Research lives in one tab, market data in another, the
math in a notebook, the broker in a third window, and the automation — if it exists —
in someone's private scripts.

Black Eclipse puts the pieces behind one agentic harness: a model that plans and
explains, tools that declare their permissions and effects, deterministic engines that
compute the numbers, and a controlled boundary before anything touches a broker.

The rule that holds it together: **the model never invents a figure.** If a claim cannot
be sourced or a metric cannot be computed, the run returns `UNAVAILABLE` and says what
was missing.

---

## Features

| | What you get | Where it lives |
|---|---|---|
| **Research with receipts** | Investigate companies, filings, fundamentals, industries and news. Every claim carries the handle of the source that produced it; conflicts are disclosed, not averaged. | [`research/`](Black-Eclipse-site/python/harness/research/) · [`market/`](Black-Eclipse-site/python/harness/market/) |
| **Deterministic finance engine** | Metrics, ratios, valuation, risk and portfolio math run in Python with formula, inputs, assumptions and seed attached. | [`finance_facts/`](Black-Eclipse-site/python/harness/finance_facts/) · [docs](Black-Eclipse-site/docs/harness/financial-analysis-engine.md) |
| **Strategy and backtesting** | Author a strategy as a versioned IR, a visual graph, or sandboxed Python — then test it with an anti-lookahead backtest, walk-forward, Deflated Sharpe and an overfitting check. | [`quant/`](Black-Eclipse-site/python/harness/quant/) · [docs](Black-Eclipse-site/docs/backtesting-engine.md) |
| **Portfolio and journal** | Holdings, performance, allocation, exposure, risk decomposition, a trading journal and broker reconciliation. | [`portfolio/`](Black-Eclipse-site/python/harness/portfolio/) · [docs](Black-Eclipse-site/docs/portfolio-accounting.md) |
| **Agents, bots and automation** | Cron, interval, event and condition triggers; durable runs with leases, retries and at-most-once effects; agent teams, persistent memory and reviewed skills; a visual workflow studio. | [`automation/`](Black-Eclipse-site/python/harness/automation/) · [`team/`](Black-Eclipse-site/python/harness/team/) · [docs](Black-Eclipse-site/docs/harness/automation-engine.md) |
| **Trading, gated** | MetaTrader 5 integration behind single-use approvals, demo mandates, margin caps, reconciliation and a kill switch — or a named refusal explaining what is missing. | [`trade/`](Black-Eclipse-site/python/harness/trade/) · [docs](Black-Eclipse-site/docs/trading.md) |

Every tool in the registry declares a permission class and an effect class. A tool that
cannot declare them is not published. Models are interchangeable — OpenAI, Anthropic,
Google, Mistral, Groq, any OpenAI-compatible endpoint, or Ollama locally.

---

## See it

| Eclipse Agent | Bots | Workflows |
|:---:|:---:|:---:|
| ![The Eclipse Agent research surface, driven by slash commands and tools](Black-Eclipse-site/docs/figures/readme/02-agent.png) | ![Scheduled agents reporting what each source returned and what it could not](Black-Eclipse-site/docs/figures/readme/06-bots.png) | ![The Graph Studio library of typed, versioned graphs](Black-Eclipse-site/docs/figures/readme/05-graph-studio.png) |
| The research surface | Scheduled agents; gaps marked `UNAVAILABLE` | Typed, versioned workflows |

*Real captures of the running app — not mockups.*

---

## Use

Six things people actually do with it. Each one is a run you can inspect afterwards —
plan, tool calls, sources and receipts included.

| Use it to… | Start with | What you get |
|---|---|---|
| **Value a company** | Ask for a quarter, a valuation or a peer comparison | A cited report; the arithmetic shown with inputs and assumptions |
| **Find setups** | Screen global markets, then open Market Bubbles | A ranked shortlist of real instruments, sized by traded value |
| **Test an idea** | Write the strategy in Strategy Studio or in sandboxed Python | An equity curve, a walk-forward result and a grade |
| **Run a morning brief** | Schedule a bot for 08:00 | A delivered briefing that lists what each source returned and what it could not |
| **Reconcile your book** | Import broker trades into the journal | Allocation, risk and a discrepancy list |
| **Paper-trade a mandate** | Backtest, approve, connect a demo account | One order under a capped mandate — or a refusal naming the missing gate |

**Who it is for:** investors who want to check the reasoning, quants who want the
infrastructure, researchers who want the data and the math in one place, and developers
who want to build on the harness.

---

## Needs

One download, nothing to install first. The installer *is* the application: a bundled
Node runtime, a vendored Python runtime, the agent stack, the database schema and a
seeded market-data vault.

| Need | Detail |
|---|---|
| **Operating system** | Windows 10/11 (x64). macOS and Linux builds exist but are not published yet |
| **Administrator rights** | **None** — per-user install to `%LOCALAPPDATA%\Programs\BlackEclipse` |
| **Node.js, Python, SQLite** | **Not required** — all three ship inside the payload |
| **Account, sign-in, telemetry** | **None** — the app runs entirely on your machine |
| **Download size** | ~141 MB for the core; optional feature packs download on demand |
| **A language model** | A hosted provider key, or Ollama running locally. Without one, everything except the agent still works |
| **Internet** | Needed for live prices, news and model calls. The app still opens and seeds its vault offline; unavailable data reads `UNAVAILABLE` |
| **A broker** | Optional. Only needed for execution — research and backtesting do not require one |

**What it does not need:** a cloud account, a database server, a vendor data licence, or
an administrator prompt. Optional feature packs (browser automation, local ML, document
reading, desktop control, advanced charting) are lazy — a missing pack degrades one
capability instead of blocking the install.

---

## Install

**The desktop app** — Windows 10/11 (x64):
[Download for Windows](https://github.com/dumbpabloo/BlackEclipse-V1.0/releases/latest/download/BlackEclipse-Setup.exe) ·
[all releases](https://github.com/dumbpabloo/BlackEclipse-V1.0/releases).

Or from a terminal — the same artifact, verified and installed:

```powershell
# Windows (per-user, no administrator prompt)
irm https://raw.githubusercontent.com/dumbpabloo/BlackEclipse-V1.0/main/Black-Eclipse-site/scripts/install-release.ps1 -OutFile install-release.ps1
./install-release.ps1
```

The script resolves `releases/latest`, compares the download against the release's
SHA-256, and can pin an exact version (`-Version`) or digest (`-Sha256`). Details:
[docs/install.md](Black-Eclipse-site/docs/install.md).

**From source** — for contributors:

```bash
cd Black-Eclipse-site
npm install              # also provisions the Python agent runtime
npm run desktop:refresh  # build + open the desktop app (port 3100)
```

**Verify before you run it.** The installer is unsigned and Windows will warn. Releases
publish `SHA256SUMS.txt`; to check by hand:

```powershell
Get-FileHash .\BlackEclipse-Setup.exe -Algorithm SHA256
# compare with the line for that file in SHA256SUMS.txt
```

A mismatch means the download is not the artifact we published — delete it.

<details>
<summary><b>Troubleshooting the first three failures</b></summary>

| Symptom | Cause | Fix |
|---|---|---|
| `503 runtime unavailable` | Python runtime missing or broken | `npm run desktop:doctor` from `Black-Eclipse-site/`, then relaunch |
| Every model call fails | No provider configured | **Settings · AI** — add a key, or point at Ollama on `http://localhost:11434` |
| Empty screens after first launch | Vault seed interrupted | Relaunch; the boot hook re-seeds. `npm run desktop:doctor` reports what is missing |

</details>

<details>
<summary><b>Embed the harness without the app</b></summary>

```python
import asyncio
from harness.public import AgenticService, RunInput, RunRequest, ModelSettings

async def main():
    service = AgenticService()
    result = await service.run(RunRequest(
        runId="research-1",
        input=RunInput(query="Summarise the last quarter for this ticker and cite the filings."),
        modelSettings=ModelSettings(provider="ollama", model="llama3.1",
                                    base_url="http://localhost:11434/v1"),
        callbackBaseUrl="http://localhost:3000",
    ))
    print(result.status, result.output)

asyncio.run(main())
```

The PyPI release is pending; install from source today:

```bash
pip install "git+https://github.com/dumbpabloo/BlackEclipse-V1.0.git#subdirectory=Black-Eclipse-site"
```

</details>

---

## How it works

```
   plan ──▶ call tools ──▶ compute in Python ──▶ verify sources ──▶ act
     ▲                                                              │
     └──────────────── durable run, memory, receipts ◀──────────────┘
```

Three separations make it a harness rather than a chat wrapper:

- **The model plans and explains; Python computes.** Every financial calculation returns
  its formula, inputs, assumptions and seed, so the same question produces the same
  number or an honest `UNAVAILABLE`.
- **Research and execution are separate products.** No layer outside
  [`quant/`](Black-Eclipse-site/python/harness/quant/) may compute a trading statistic,
  and no research result authorizes an order.
- **Every effect is declared and recoverable.** Tools carry permission and effect
  classes; runs use leases, fencing and retries; an unknown outcome is a first-class
  result, not a silent success.

---

## Proof

Two evaluation tiers, kept apart on purpose: the offline tier measures the **runtime**
with a scripted model, the live tier measures the **agent** with a real one.

| Offline · runtime | Live · agent |
|---|---|
| task_success **0.9970** · safety **1.0000** · hallucination **0.0000** · gate **PASS** | task_success **0.9748** · financial_accuracy **0.9963** · citation_accuracy **1.0000** · gate **PASS** |

347 tasks across 15 versioned datasets, 78.1% graded by an independent oracle.
`financial_accuracy` is not judged by a model: `FinancialGrader` recomputes the expected
value with the same calculation library and compares within a declared tolerance.

<details>
<summary><b>What the numbers do not measure</b></summary>

Returns, strategy robustness, and citation coverage on the open web. Several dimensions
print `UNKNOWN` — not zero, not pass. The corpus manifest is checksummed and each run
records its model, commit, grader version and dataset checksum.

Method and provenance: [`docs/harness/benchmarks.md`](Black-Eclipse-site/docs/harness/benchmarks.md) · [`docs/harness/agent-evaluation.md`](Black-Eclipse-site/docs/harness/agent-evaluation.md).

</details>

### What it refuses to do

- **No fabricated market data.** A source that is off, stale or unreachable renders
  `UNAVAILABLE`; demo data ships behind a visible `DEMO` banner.
- **No unattended order.** Live execution needs an approved strategy version, a completed
  backtest, a typed confirmation, an armed connection and a margin cap.
- **No silent tool.** An undeclared tool is unpublished, and a denied tool call comes
  back as a refusal with a reason, not a retry loop.

---

## Data sources

The app does not ship a data licence of its own. Sources fall into three tiers:
**included** (open data, no account, on by default), **connect your own** (you supply a
key and accept the provider's terms), and **advanced / community** (personal use only,
off by default).

Commercial defaults include SEC EDGAR, BEA, BLS, USGS, FRED, World Bank, Eurostat, ECB
and GDELT with the attribution the app displays. Sources such as the TradingView scanner,
Yahoo Finance, the Binance public ticker and keyless CoinGecko are personal-use only and
stay off unless an operator turns them on.

<details>
<summary><b>The full source table and commercial terms</b></summary>

Every toggle is enforced at the fetch path, so a source that is off cannot quietly serve
a screen. The full table — every source, what it powers, its commercial status and its
terms link — is generated from
[`source-catalog.ts`](Black-Eclipse-site/src/lib/setup/source-catalog.ts) into
[`docs/data-sources.md`](Black-Eclipse-site/docs/data-sources.md). Adding a source is a
first-class path: edit the catalog, run `npm run docs:data-sources`, and the docs and
Settings surface follow.

> Informational snapshot of each provider's published terms, not legal advice or a licence
> grant. Terms change — verify them before a paid launch. Language models are separate
> again: you bring your own key or run Ollama locally.

</details>

---

## Documentation

| Start here | What it answers |
|---|---|
| [QUICKSTART](Black-Eclipse-site/docs/QUICKSTART.md) | How do I run it and see something working? |
| [OVERVIEW](Black-Eclipse-site/docs/OVERVIEW.md) | What is this product, and what is the mental model? |
| [ARCHITECTURE](Black-Eclipse-site/docs/ARCHITECTURE.md) | What are the layers and the big moving parts? |
| [NAVIGATION](Black-Eclipse-site/docs/NAVIGATION.md) | Which file do I open to change X? |
| [Harness](Black-Eclipse-site/docs/harness/architecture.md) | How the runtime, tools, policy and evaluation work |
| [Trading](Black-Eclipse-site/docs/trading.md) | Broker connections, mandates, approvals and the kill switch |

## Roadmap and current limitations

There is no dated roadmap, on purpose. These two documents are the roadmap, and a
capability that is not in them is not promised:

- **[PRODUCTION-READINESS](Black-Eclipse-site/docs/PRODUCTION-READINESS.md)** — the gates
  still open for production use.
- **[OPEN-SOURCE-READINESS](Black-Eclipse-site/docs/OPEN-SOURCE-READINESS.md)** — what is
  left before this repository is public.

<details>
<summary><b>Known limits, stated plainly</b></summary>

- **`v0.4.31` is single-operator and self-hosted.** It is not a multi-tenant service and
  does not pretend to be.
- **Updates are signed artifact swaps** (SHA-256 verified against the signed manifest) —
  no local rebuild. See [`docs/UPDATES.md`](Black-Eclipse-site/docs/UPDATES.md).
- **The Python package is not on PyPI yet.**
- **Installers are unsigned**, so SmartScreen and Gatekeeper will warn. Verify the
  checksum instead.
- **Coverage is uneven across markets.** A thin market shows `UNAVAILABLE` rather than a
  synthetic quote.
- **Benchmarks measure the agent, not a strategy.** A passing gate says nothing about
  returns.

</details>

## Open source

Black Eclipse is built as an open-source project for developers, researchers,
quantitative traders and investors who want to build, extend and customize their own
financial AI environments.

- [**Contributing**](Black-Eclipse-site/CONTRIBUTING.md) — setup, DCO, CLA, release gate
- [**Security**](SECURITY.md) — private advisories, never a public issue
- [**Code of conduct**](CODE_OF_CONDUCT.md)
- [**Trademark**](TRADEMARK.md) — the code is MIT; the name is not
- [**Issues**](https://github.com/dumbpabloo/BlackEclipse-V1.0/issues) — bug reports, feature requests and questions

<details>
<summary><b>Licensing, precisely</b></summary>

| Component | License |
|---|---|
| The application and this repository's original code | **MIT** — see [`LICENSE`](LICENSE) |
| `Black-Eclipse-site/pine-engine/` — the isolated Pine Script engine | **AGPL-3.0-only**, because it depends on `pinets`. It is a separate program that talks to the app only through files — see [`NOTICE.md`](Black-Eclipse-site/pine-engine/NOTICE.md) |
| The **name, wordmark and logo** | **Not licensed by MIT.** Fork it, rename it — see [`TRADEMARK.md`](TRADEMARK.md) |
| Contributions | MIT/AGPL as above, plus the [`CLA`](CLA.md) |

If you redistribute the app, the MIT terms cover it. If you run the Pine engine as part of
a network service, AGPL-3.0-only applies to **that component** and its obligations are
described in its NOTICE.

The locked dependency trees are inventoried in
[`THIRD-PARTY-NOTICES.md`](THIRD-PARTY-NOTICES.md) (grouped by licence) and
[`sbom.cdx.json`](sbom.cdx.json) (CycloneDX 1.5). Both are generated with `npm run sbom`;
do not hand-edit them.

</details>

---

<div align="center">

**Trading disclaimer.** Black Eclipse is research and analysis software. It is not
investment advice, and it does not make decisions for you. Research does not authorize
trading: an order requires the operator's approval, and live execution additionally
requires an armed connection and a capped mandate. Demo and live are distinct modes.
Backtest results do not guarantee live performance. Black Eclipse is not affiliated with,
endorsed by, or derived from any terminal vendor.

<sub>Black Eclipse — an open-source agentic harness for finance.</sub>

</div>
