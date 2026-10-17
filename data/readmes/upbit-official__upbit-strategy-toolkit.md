# Upbit Strategy Toolkit (Beta)

English | [한국어](./README_KR.md)

![Status: Beta](https://img.shields.io/badge/status-beta-orange)

The official Python-based toolkit for designing and backtesting trading strategies on Upbit, a digital asset exchange.

Upbit Strategy Toolkit enables users to build and validate indicator-based trading strategies through natural-language interactions with AI agents, using Upbit's historical market data. It allows you to structure your strategy ideas in JSON format and review backtest results and reports based on Upbit market data.

Quickly validate your own trading hypotheses by working with AI agents such as Claude Code or Cursor using simple prompts like "Create a golden cross strategy" or "Run a backtest for USDT-BTC." Currently in **beta**, this toolkit focuses exclusively on strategy design and validation and does not require live-trading permissions or account information.

---

## Usage Modes

| Mode | Installation | Default Data Root (unless `config set data-dir` was used) |
|---|---|---|
| Global (recommended) | `npx skills add ... -g` | current working directory (cwd) at run time |
| Project-scoped (fallback) | `npx skills add ...` | current working directory (cwd) at run time |
| Clone | `git clone` + `uv sync` | current working directory (cwd) at run time |

### Global Installation (recommended)

Install the agent skills into your home directory without cloning the repo, so they are available from any project. Unless you've stored a `data-dir` with `config set`, the data root defaults to the current working directory at run time — so it follows whichever directory you invoke the agent from.

```bash
npx skills add upbit-official/upbit-strategy-toolkit -s '*' -a claude-code -a codex -a cursor -y --copy -g
```

Outputs are saved under whichever directory you invoke the agent from (unless you've set a custom `data-dir`).

```text
{current working directory}/
|-- strategies/
|-- reports/
`-- cache/
    `-- upbit/
```

### Project-Scoped Installation (fallback)

Use this when you don't have permission to write to the home directory, or want the skills scoped to a single project. Drop the `-g` flag from the command above:

```bash
npx skills add upbit-official/upbit-strategy-toolkit -s '*' -a claude-code -a codex -a cursor -y --copy
```

Unless you've stored a `data-dir` with `config set`, the data root defaults to the current working directory at run time — so it follows whichever directory you invoke the agent from.

```text
{current working directory}/
|-- strategies/
|-- reports/
`-- cache/
    `-- upbit/
```

### Clone Mode

Clone the repo, then run the agent from that workspace. Unless you've stored a `data-dir` with `config set`, the data root defaults to the current working directory at run time.

```bash
git clone https://github.com/upbit-official/upbit-strategy-toolkit.git
cd upbit-strategy-toolkit
uv sync
uv run upbit-strategy-toolkit --help
```

Outputs are saved under whichever directory you invoke the agent from.

```text
{current working directory}/
|-- strategies/
|-- reports/
`-- cache/
    `-- upbit/
```

### Prerequisites

> **Note:** Currently, only Upbit KR exchange (KRW/BTC/USDT markets) is supported. Other exchanges (SG, ID, TH) are not.

Clone mode requires only uv; agent skills mode additionally requires npm (Node.js), since `npx` ships with npm.

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) before running any commands.

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

- Run the `/setup` skill if environment diagnostics are needed.

---

## Quick Start

The agent helps users structure hypotheses and report backtest evidence.
It does not recommend what asset to buy, sell, or hold, when to trade, what target return to pursue, what price to trade at, or how long to hold a position.

### 1. Create a Strategy

Describe the idea in natural language or start with the `/create-strategy` command.

```
"Create a strategy that catches short-term rebounds even in a downtrend"
"Enter on RSI oversold and exit at the Bollinger Bands middle line"
"SMA 5/20 golden cross strategy with 3% stop-loss and 8% take-profit"
```

These are user-provided hypotheses or rule ideas, not toolkit recommendations.
The skill structures entry, exit, stop-loss, and take-profit conditions for review. After approval, strategy JSON is saved under the data root's `strategies/` directory.

### 2. Run a Backtest

After the strategy is saved, you can request a backtest right away.

```
"Run a backtest for the strategy I just created from 2024-01-01 to 2025-01-01"
```

You can also use the `/backtest` command and specify the start and end dates.
Results are saved as CSV under the data root's `reports/` directory, and a factual performance summary is printed.
Before running, `backtest` checks whether the strategy market is listed on the selected exchange.

```
Period      2024-01-01 ~ 2024-12-31 (trading bars: 366, warmup bars: 30)
Benchmark   +62.45%
Total Return +18.32%
CAGR        +18.11%
MDD         -7.21%
Sharpe      1.34  (Rf=0, portfolio / full equity curve)
Sharpe      1.11  (Rf=0, trades / position holding periods only)
Trades      23  Win Rate 60% (before fees)
Profit Factor  2.14 (before fees)
SL 4 / TP 9 / sell 8 / final_bar 2
Total Fees  12,345
```

> `Sharpe (portfolio)` reflects the stability of overall equity changes; `Sharpe (trades)` reflects the stability of per-trade returns (annualized by holding period).

### 3. Revise a Strategy

After reviewing results, you can adjust parameters or change conditions.

```
"Lower the entry condition to RSI <= 25 and backtest again"
"Reduce the stop-loss from 5% to 3% and compare"
```

---

## Direct CLI Usage

You can also use the CLI directly without the agent workflow.

### Minimal strategy JSON

Save the following to `strategies/examples/sma_cross.json`:

```json
{
  "name": "SMA 5/20 cross",
  "market": "KRW-BTC",
  "timeframe": "1d",
  "stop_loss": 5,
  "take_profit": 15,
  "indicators": [
    { "type": "moving_average", "ref": "ma_short", "params": { "type": "SMA", "period": 5 } },
    { "type": "moving_average", "ref": "ma_long",  "params": { "type": "SMA", "period": 20 } }
  ],
  "buy": {
    "operator": "AND",
    "conditions": [
      { "left": { "type": "indicator", "ref": "ma_short.value" },
        "op": "cross_above",
        "right": { "type": "indicator", "ref": "ma_long.value" } }
    ]
  },
  "sell": {
    "operator": "AND",
    "conditions": [
      { "left": { "type": "indicator", "ref": "ma_short.value" },
        "op": "cross_below",
        "right": { "type": "indicator", "ref": "ma_long.value" } }
    ]
  }
}
```

See [Strategy JSON Schema](skills/create-strategy/references/schema.md) for the full field and indicator reference.

### Validate a strategy

```bash
uv run upbit-strategy-toolkit strategy validate strategies/examples/sma_cross.json
```

Prints `OK` on success, or a validation error on failure.

### Run a backtest

```bash
uv run upbit-strategy-toolkit backtest run strategies/examples/sma_cross.json --start 2024-01-01 --end 2024-12-31
```

Optional flags: `--capital <float>`, `--fee-rate <float>`, `--verbose/--no-verbose` (default: verbose), `--force-refresh`.

### Manage the data root

The data root holds `strategies/`, `reports/`, and `cache/`. It resolves in this priority order:

1. `UPBIT_TOOLKIT_DATA_DIR` environment variable
2. `data-dir` stored in config (`~/.config/upbit-strategy-toolkit/config.json`, or under `$XDG_CONFIG_HOME` if set)
3. The current working directory at run time

If `data-dir` is not set via `config set`, the CLI defaults to the current working directory at run time, so it follows whichever directory you invoke the agent from regardless of install mode. Once you run `config set data-dir`, that stored value takes over and is used regardless of mode or directory.

Set or read the persisted data root:

```bash
uv run upbit-strategy-toolkit config set data-dir /path/to/data
uv run upbit-strategy-toolkit config get data-dir
```

`config get` prints `(not set)` when no value is stored. Changing `data-dir` does not move existing files — move `strategies/`, `reports/`, and `cache/` to the new location yourself if you want to keep them.

### Clear the cache

Clear all cached files (asks for confirmation):

```bash
uv run upbit-strategy-toolkit cache clear
```

Clear only the candle cache for a specific market and date range:

```bash
uv run upbit-strategy-toolkit cache clear-candle \
  --exchange kr --market KRW-BTC --timeframe 1d \
  --start 2024-01-01 --end 2024-12-31
```

Both print the number of deleted files, or `No cache files found`.

---

## Skills

| Skill | Trigger | Description |
|---|---|---|
| `/create-strategy` | Natural-language strategy idea | Creates strategy JSON |
| `/backtest` | "Run a backtest", `/backtest` | Validates strategies and analyzes performance |
| `/setup` | Environment issue | Detects mode and diagnoses CLI availability |

---

The basic strategy-validation flow is `setup -> create-strategy -> backtest`.
`setup` is the environment diagnostic and recovery entry point, `create-strategy` saves testable strategy JSON, and `backtest` runs the strategy and interprets the result.
Interpret the output as evidence for or against the tested hypothesis, not as investment advice or a trading recommendation.

Use the following notes when interpreting backtest results.

### Entry

The tool buys at the next candle's open (tick-rounded) after the buy condition is met, sizing the quantity so cost including fees stays within cash. It skips the buy if the order value is below the market's minimum.

### Exit Priority

When multiple conditions apply within the same candle, they are applied in this order.

1. **Stop-loss** - candle low is at or below the stop-loss price
2. **Take-profit** - candle high is at or above the take-profit price
3. **Sell signal** - the strategy's exit condition is satisfied
4. **Final bar** - forced exit at the final backtest candle

### Execution Price

| Exit type | Execution price |
|----------|--------|
| Stop-loss | Stop-loss price. If a gap down opens below the stop-loss price, use the open price |
| Take-profit | Take-profit price. If a gap up opens above the take-profit price, use the open price |
| Sell signal | Next candle open after the signal occurs |
| Final bar | Final candle close |

> Stop-loss and take-profit orders are placed on entry. They fill at the level if price reaches it normally, or at the open price on a gap (slippage). Stop-loss and take-profit are not evaluated on the entry candle and apply from the next candle onward.

### Signal Collection

Buy and sell conditions are evaluated on every candle regardless of whether a position is open. A buy signal while already in a position does not add another entry, and a sell signal while no position is open has no effect.

### Fees

Fee rates differ by market and are applied automatically from market rules (for example, KRW 0.05%, BTC/USDT 0.25%). Win rate and Profit Factor are calculated before fees.

> Slippage, spread, and market impact are not reflected. Entry and sell-signal exits assume full execution at the candle open, so actual performance may differ on short timeframes or in low-liquidity markets.

### Numerical Precision

All calculations use IEEE 754 double precision (float64). Results are approximations for backtesting purposes, not for live order execution or accounting.

---

## Contributing

Upbit Strategy Toolkit is in its initial release phase, and public contributions (Issues/PRs) are currently closed. For bug reports and feedback, please email [open-api@upbit.com](mailto:open-api@upbit.com). We are considering opening external contribution channels in phases as this project becomes more stable.

## Disclaimer

See [DISCLAIMER.md](./DISCLAIMER.md) for full disclaimer.

© 2026 Dunamu Inc. All rights reserved.
