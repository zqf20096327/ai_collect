# First ML Trading Strategy

Built with Samah ([@Samah-elqarnia](https://github.com/Samah-elqarnia)) for the video
"beginner quant project you can build now".

Predict whether SPY closes up tomorrow with a random forest, trade on it with
costs, and find out honestly whether that beats doing nothing. Then find out
what actually made the difference.

A beginner project built the way a real one has to be: chronological split,
a floor that is the best single feature rather than chance, a leakage test
that can fail, a costed backtest, results window by window with a t statistic,
a block bootstrap Monte Carlo paired with buy and hold, and one paired
experiment on seeds. Ten features, one ETF, every session since 1993, about
two minutes to run.

## Results

Test period 2020-02-11 to 2026-09-09, 1,653 trading days, sealed until the
model was frozen, opening days before the 2020 crash by arithmetic and not by
choice. Starting capital $100k, 0.05% per side each time the position changes.

| frozen model, one split | strategy | buy and hold |
|---|---|---|
| accuracy | 54.7% | 54.7% (always up) |
| total return | **+164.3%** | +146.4% |
| CAGR | **16.0%** | 14.7% |
| Sharpe | **0.87** | 0.79 |
| max drawdown | **−30.3%** | −33.7% |
| time in market | 92% | 100% |

Wins 3 of 3 on the plan's threshold, with accuracy sitting exactly on the
always up floor. Both are true. Accuracy counts every day; the account only
counts the 8% of days the model was in cash, and those were, on balance,
March 2020 and 2022. Excess return has t = +0.41 on this one split, inside the
noise.

The experiment that firms it up: refit every January from 2015 to 2026, run on
five seeds, once with training data from 1993 and once cut to 2010, the five to
ten years most tutorials suggest. Same test years, same settings, same seeds.

| walk forward, mean of 5 seeds | trained since 1993 | trained since 2010 | buy and hold |
|---|---|---|---|
| total return | **+474%** (worst seed +434%) | +389% (worst +371%) | +355% |
| Sharpe | **0.97** | 0.87 | 0.82 |
| max drawdown | **−28.1%** | −33.7% | −33.7% |
| t statistic | **+1.24** | +0.55 | |
| seeds ahead of buy and hold | 5 of 5 | 5 of 5 | |

History is worth about 85 points of return, 0.10 of Sharpe and most of the
drawdown. The 2010 model matches buy and hold's drawdown to the decimal because
it never once left the market during a fall: it had never seen a bear market.
The 1993 model has seen 2000 to 2002 and 2008, and in 2020 it was in the market
80% of the year and returned +37% against +16% for the index. A modest, robust
edge, not yet statistically significant, and one that contradicts the "five to
ten years of data" advice the plan started from.

Full walk through, every figure and table, in
[notebooks/first_ml_trading_strategy.ipynb](notebooks/first_ml_trading_strategy.ipynb).

![history](results/14_history.png)

## What is inside

1. **Data.** Daily SPY from Yahoo Finance since its first session, dividends and splits adjusted, cached to one CSV that refreshes itself when the dates change.
2. **Features.** Lagged returns (1, 5, 20 days), distance from the 20, 50 and 200 day moving averages, 20 day volatility, RSI, MACD over price, volume against its 20 day average. Every one is scale free, so a pattern learned at $40 in 1995 applies at $700.
3. **Target and leakage test.** Up or down tomorrow, via `shift(-1)`. A column that *is* tomorrow's return is planted beside the real features and has to come out at correlation 1.0 while everything honest sits near zero. A test that cannot fail is not a test.
4. **Split.** First 60% of days to train, next 20% to validate, last 20% to test. Never shuffled.
5. **Floors before any model.** Always up, and the best single feature in a logistic regression, found by sweeping every column.
6. **Default forest.** 100% on train, 51.0% on validation: overfitting in one line.
7. **Tuning on validation only.** 32 combinations of depth, leaf size and tree count. Depth 3 wins, and the top five sit within 0.3 points of each other.
8. **Freeze and test.** One score on the sealed set, next to the same two floors on the same days. The model says "up" 92% of the time; its value is where it does not.
9. **Backtest with costs.** Equity curve, drawdown, trade log, Sharpe on one ruler for both sides.
10. **Window by window.** Four blocks and a t statistic on the daily difference.
11. **Monte Carlo.** 1,000 block bootstrap paths of 20 day blocks, the same blocks applied to the strategy and to buy and hold, so the comparison is paired. And what a bootstrap cannot say: it inherits the regime of the period it resamples.
12. **Feature importance.** Impurity and permutation side by side, and why the first is flat and uninformative here.
13. **How much history the model needs.** Yearly refits, two lengths of history, five seeds, paired. The step that changed the answer.
14. **Verdict, and what to try next.** Trade the probability rather than the sign, a target matched to what the model is good at, features from outside the price series, gradient boosting, more seeds and assets.

![equity](results/07_equity.png)

## Layout

```
strategy/          the engine, one module per step
  config.py          every constant: ticker, dates, split, costs, seeds, history comparison
  data.py            download, clean, self refreshing cache
  features.py        indicators, target, leakage test
  split.py           chronological split
  baselines.py       always up, best single feature
  model.py           random forest: fit, tune, freeze, evaluate, importance
  backtest.py        equity curve with costs, metrics, windows, t statistic
  montecarlo.py      block bootstrap, paired
  walkforward.py     yearly refits, the paired history comparison on seeds
  plots.py           every chart, one palette
  run.py             the whole pipeline headless, writes results/
notebooks/
  first_ml_trading_strategy.ipynb   the walk through, executed, outputs included
  build_notebook.py                 writes and executes the notebook from the package
data/              spy.csv, 8,461 sessions from 1993
results/           metrics.json, every table as CSV, fifteen charts
```

Code in the notebook is pulled from the package by source, so what you read
inline is exactly what the headless run executes. Every number in the
notebook's prose is formatted from `results/`, and the last cell asserts that
the freshly executed cells agree with it.

## Quickstart

```
pip install -r requirements.txt
python -m strategy.run                 # data, model, backtest, monte carlo, history: about 2 min
python notebooks/build_notebook.py     # rebuild and execute the notebook with the fresh numbers
```

Everything is seeded, so two runs give identical numbers. `END` in
`strategy/config.py` pins the sample; move it forward to extend the data, and
the prose regenerates from whatever the new run produced. `SHORT_START` sets
the shorter history for the comparison in step 13.

## What was tried and did not work

Kept out of the repo, mentioned so nobody repeats them on the 2010 sample: a
higher probability threshold (worse at every level, because cash costs more
than the model has real reason for), a 5 or 20 day horizon target (closer, still
behind), and shifting the test window (wins only when the window contains a
bear market, which is the same lesson from the other side). Only more history
moved the result, and it moved it on every seed.

## Five rules worth keeping for the next project

- **Chance is not the bar.** The floor is the best single feature used alone, found by sweeping every column, never chosen by hand.
- **A leakage test has to be able to fail.** Plant a leak and confirm the test catches it.
- **One number hides a lot.** Results by window, and a t statistic on the daily difference, before believing an aggregate.
- **A Monte Carlo cloud means nothing alone.** It inherits the regime of the period it resamples, so the benchmark's cloud belongs next to it.
- **A change helped only if it helps on every seed.** Same test years, same settings, paired, before crediting anything.

Not investment advice. A modest edge with a t statistic near 1 is a reason to
keep testing, and no reason to trade.
