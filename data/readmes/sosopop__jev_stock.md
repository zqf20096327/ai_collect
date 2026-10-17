# Hong Kong Stock Direction Forecasting with TypeSafe JEV

Language: **English** · [简体中文](README.zh-CN.md)

This repository is an experiment in forecasting the next Hong Kong stock-market direction with TypeSafe JEV. You enter a Hong Kong stock code, the program downloads market data, builds a past-only state, asks JEV for a structured `up` / `flat` / `down` forecast, validates the response, and can render a standalone HTML report.

The default reference market is deliberately small: the target stock, the Hang Seng Index (`HSI`), and the Hang Seng TECH Index (`HSTECH`). The project does not silently add a basket of unrelated stocks.

## Example output

The generated report presents the cutoff date, direction forecasts, model probabilities, and the main state summary in a compact layout.

![Example JEV prediction report](assets/jev-prediction-report-example.png)

## My view of JEV for stock forecasting

My current view is that JEV is more useful here as a disciplined reasoning layer than as a proven quantitative trading model.

The useful part is the separation of responsibilities. The Python program owns data retrieval, date alignment, feature calculation, leakage checks, label definitions, and scoring. JEV receives a readable state and makes a consistent classification choice. This can be helpful when several weak signals point in different directions and a human wants one repeatable interpretation of the same evidence.

The risky part is the word “probability”. A response such as `down: 0.68` is a model probability for the supplied question. It is not automatically a 68% historical win rate, and `confidence: 0.52` is not a calibrated 52% chance of being correct. Calibration has to be measured with many timestamped predictions and later observations. This repository therefore shows the raw output, but does not turn it into an investment recommendation.

My practical expectation is modest: JEV may help organize a multi-dimensional market snapshot and produce a useful research hypothesis. I would not rely on a single response to place a trade. I would trust the workflow only after a longer forward test, a stock-by-stock comparison with simple baselines, and calibration checks on probabilities. The included retrospective test is useful for debugging and comparison, but it is not a clean live-trading experiment because the current model may already know historical events.

## What the program does

The prediction pipeline is:

1. Normalize a code such as `1810.HK` to `01810`.
2. Fetch the target stock, `HSI`, and `HSTECH` through AKShare.
3. Remove a current Hong Kong trading day before 16:30 Hong Kong time because its daily bar may not be complete.
4. Use the latest date shared by all three series as `as_of`; reject stale or misaligned data.
5. Build a state from data at or before `as_of`.
6. Ask JEV one independent question per requested trading day and one separate 30-calendar-day endpoint question.
7. Validate the response shape and the three-class probability sum.
8. Save JSON and, when requested, a self-contained HTML report.

The model is not asked to predict an exact future price. It chooses a direction using the return thresholds in the state.

## JEV request boundary

The current adapter sends a JSON payload with three parts: `model`, `state`, and `questions`. The source currently selects `jev-latest` and posts to TypeSafe's System One endpoint. Each question is a `choice` question with exactly three allowed outcomes. The response parser accepts only those outcomes and requires finite probabilities for `up`, `flat`, and `down` whose sum is close to one.

This boundary matters. The local program does not train a model, update model weights, or infer a probability from the later truth before sending the request. It prepares the evidence and defines the target; JEV supplies the classification response. The state and the question wording are therefore part of the experiment and should be versioned alongside the result.

## State design

The state is intentionally explicit so that a request can be inspected and reproduced.

| State section | Contents | Why it is included |
| --- | --- | --- |
| `target_stock` | 30 aligned trading sessions of OHLCV, latest close, returns, moving-average distance, realized volatility, RSI, ATR, and volume ratio | Short-term price and activity context |
| `reference_indices.HSI` | The same 30-session history and indicators for the Hang Seng Index | Broad Hong Kong market regime |
| `reference_indices.HSTECH` | The same 30-session history and indicators for the Hang Seng TECH Index | Technology-sector regime |
| `monthly_price_context` | The latest 12 complete calendar-month closes and month-on-month returns, plus the current partial month | Slower trend and regime context without pretending the current month is complete |
| `weekly_relative_context` | The latest 14 natural weeks, weekly closes, weekly returns, four-week close averages, and target-minus-index performance in percentage points | Intermediate trend and relative strength |
| `financial_context` | Live annual and latest-quarter financial metrics when the interface returns them | A slower fundamental layer; not used in historical backtests without reliable publication timestamps |

The technical indicators are descriptive transformations of the downloaded bars. They are not extra observations from the future. Monthly and weekly aggregations are computed after applying the cutoff date, so a historical state cannot see a later month or week.

### Financial-data timing

The automatic financial interfaces do not provide a reliable publication timestamp for every returned row. The live prediction path can display these figures, but the historical backtest intentionally leaves the financial context unavailable to avoid using a result that may not have been public at that historical cutoff. A dated user snapshot can be supplied with `--reference-json`; the code checks its stock code, cutoff date, and reported-quarter publication date.

## Forecast definitions

### Daily direction

For trading day `T+n`, the program compares the close on `T+n` with the close on `T+n-1`, where `T` is `as_of`.

- `up`: return greater than `+0.3%`
- `flat`: return from `-0.3%` through `+0.3%`, inclusive
- `down`: return less than `-0.3%`

The threshold can be changed with `--flat-threshold`. The value is a decimal, so `0.005` means 0.5%.

### Thirty-calendar-day endpoint

This is a separate question. It compares the `as_of` close with the last Hong Kong trading close on or before 30 calendar days later. It is not the sum of the daily choices.

- default `up`: cumulative return greater than `+2%`
- default `flat`: cumulative return from `-2%` through `+2%`, inclusive
- default `down`: cumulative return less than `-2%`

Use `--long-flat-threshold` to change the cumulative flat band. The first-day backtest disables this question and sends only `direction_day_1`.

## Installation

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Create or edit `.env` in the project directory:

```dotenv
TYPESAFE_API_KEY=your_key_here
```

The program reads `.env` with `python-dotenv`. An existing environment variable with the same name takes precedence. `.env` is ignored by Git; do not commit the key.

## Basic commands

### Inspect the request without calling JEV

This downloads the data, builds the complete state, writes JSON, and creates an HTML data preview:

```powershell
.\.venv\Scripts\python.exe .\jev_hk_predict.py predict `
  --symbol 01810 --days 3 --dry-run `
  --output .\state_preview.json `
  --html .\reports\xiaomi_preview.html
```

### Run a live JEV prediction

After filling `.env`:

```powershell
.\.venv\Scripts\python.exe .\jev_hk_predict.py predict `
  --symbol 01810 --days 3 `
  --output .\prediction.json `
  --html .\reports\xiaomi_prediction.html
```

Accepted code forms include `01810`, `1810.HK`, and `0700.HK`. The default horizon is three trading days; `--days` accepts 1–10. Progress messages are written to standard error so JSON output stays machine-readable. Add `--quiet` to suppress progress messages.

### Use a dated financial snapshot

For a matching stock and cutoff date:

```powershell
.\.venv\Scripts\python.exe .\jev_hk_predict.py predict `
  --symbol 01810 --reference-json "C:\path\to\dated_state.json" `
  --output .\prediction.json --html .\reports\prediction.html
```

The snapshot is optional. It is useful when it contains dated Non-IFRS or segment figures that the live financial interface does not expose.

## Backtesting

### General multi-day backtest

```powershell
.\.venv\Scripts\python.exe .\jev_hk_predict.py backtest `
  --symbol 01810 --days 3 --samples 20 `
  --output .\backtest.json
```

This scores daily forecasts by horizon and reports accuracy plus multiclass Brier score. It does not score the 30-day endpoint question. Financial context is excluded from historical states for the timing reason described above.

### The four-stock T+1 test

`backtest_first_day.py` is the test used for the latest comparison. It takes the latest 30 consecutive eligible T+1 pairs for each stock:

| Name | Code | Cases |
| --- | --- | ---: |
| Xiaomi Group | `01810` | 30 |
| MiniMax | `00100` | 30 |
| Pop Mart | `09992` | 30 |
| MIXUE Group | `02097` | 30 |

For example, the state ending on 2026-09-15 is used to predict the 2026-09-16 close. The next case moves to the preceding trading date. Every request contains only `direction_day_1`; days 2 and 3 and the 30-day endpoint are not scored.

```powershell
.\.venv\Scripts\python.exe .\backtest_first_day.py `
  --samples-per-stock 30 --output-dir .\backtest_results
```

The run writes a JSON summary, a CSV detail file, and a JSONL checkpoint after each successful request. Re-running the command skips completed matching cases. `--plan-only` checks the dates and state construction without spending JEV calls. `--reuse-checkpoint` can copy matching records from a previous run.

The latest completed run in this workspace produced the following observed result:

| Name | Correct | Accuracy |
| --- | ---: | ---: |
| Xiaomi Group | 12 / 30 | 40.0% |
| MiniMax | 17 / 30 | 56.7% |
| Pop Mart | 9 / 30 | 30.0% |
| MIXUE Group | 16 / 30 | 53.3% |
| Overall | 54 / 120 | 45.0% |

These numbers describe this particular historical window and threshold. They are not a promise about future performance. The JSON summary also includes Wilson 95% intervals to show how uncertain an accuracy estimate from 30 cases remains.

## Reading the output

Each daily forecast contains:

```json
{
  "trading_day_offset": 1,
  "prediction": "down",
  "probabilities": {"up": 0.12, "flat": 0.20, "down": 0.68},
  "confidence": 0.52
}
```

`prediction` is the selected class. `probabilities` are the model's response for this particular question and state. `confidence` is a model-provided field. None of these values is a broker quote, a guaranteed probability, or a calibrated win rate.

The HTML report is intentionally plain and portable: it has no JavaScript or external CSS dependency. It shows the forecast cards, probability bars, technical indicators, monthly context, weekly relative performance, and available financial data.

## Data sources and quality rules

- Target and reference daily bars: AKShare `stock_hk_daily` and `stock_hk_index_daily_sina`.
- Financial data: AKShare Eastmoney Hong Kong financial interfaces when available.
- Only `HSI` and `HSTECH` are included as reference indices.
- The three series must share the state dates. Missing index dates are an error, not a fill-forward operation.
- Current incomplete daily data before 16:30 Hong Kong time is removed.
- A live prediction rejects a common market date more than seven calendar days stale.
- Prices use the interface's raw close; the program does not adjust for dividends, splits, or total return.
- A CSV override can replace the target stock only; the two reference indices are still downloaded. The CSV needs `date,open,high,low,close,volume` and may include additional numeric columns.

## Limitations and responsible use

This is research software. Short-horizon stock direction is noisy, class definitions depend on the chosen threshold, and a small backtest can change materially when the date range changes. Retrospective model calls can also benefit from information that was available to the model after the historical date, even when the local state itself is past-only. A proper evaluation should save predictions prospectively, wait for the outcome, compare with simple baselines, and periodically recalibrate probabilities.

Do not treat the HTML report or JEV output as personalized financial advice. The repository is designed to make assumptions visible so they can be challenged, changed, and tested.

## Repository map

- `jev_hk_predict.py` — live prediction, state construction, JEV request validation, and general backtest.
- `state_dimensions.py` — monthly, weekly, and financial state helpers.
- `backtest_first_day.py` — four-stock, latest-30-case, T+1-only evaluation.
- `report_html.py` — standalone HTML renderer.
- `create_reference_report.py` — renderer for the dated Xiaomi example.
- `test_jev_hk_predict.py` and `test_backtest_first_day.py` — unit tests.
- `reports/` — generated example and preview reports.
- `backtest_results/` — generated JSON, CSV, and checkpoint files.

## References

- [TypeSafe API documentation](https://docs.typesafe.ai/api)
- [AKShare documentation](https://github.com/akfamily/akshare/blob/main/docs/tutorial.md)
- [Shared JEV test conversation](https://chatgpt.com/share/6aab4923-5c34-83ec-bfe9-4e414916ee51)
