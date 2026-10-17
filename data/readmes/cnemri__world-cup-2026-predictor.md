# ⚽ World Cup 2026 Predictor

A calibrated machine-learning system that forecasts the **2026 FIFA World Cup**
from **150+ years of international football** (49,505 matches, 1872 → 2026). It
combines a margin-aware **Elo rating engine**, **time-decayed gradient-boosted**
outcome and goal models, an optional **TabFM tabular-foundation-model ensemble**,
honest **walk-forward evaluation**, and a vectorised **Monte-Carlo** tournament
simulator.

> **Headline forecast** — *as of 2026-07-10, conditioned on France 1–0 Morocco*
> (France through to the semis), from 50,000 simulations with the XGBoost + TabFM
> ensemble:
> **🇫🇷 France 29.3%**, 🇦🇷 Argentina 26.8%, 🇪🇸 Spain 22.2%, 🏴 England 12.5%.

> 📄 **Full methodology:** [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md) — a
> research-grade write-up of the data, features, modelling, ensembling, and
> Monte-Carlo engine.

<p align="center">
  <img src="reports/champion_probabilities.png" width="640" alt="Champion probabilities">
</p>

---

## Why this project is more than "predict the winner"

Anyone can `fit()` a classifier. The interesting parts here are the things that
make a football model *trustworthy*:

| Design decision | Why it matters |
| --- | --- |
| **Leakage-free features** | Every feature for a match is built only from data available *before* kick-off. The engine walks the history in date order and updates state *after* reading each row. |
| **Time-decayed sample weights** | A friendly from 2004 shouldn't count as much as a qualifier last month. Training rows decay exponentially (5-year half-life), so the model leans on current form without forgetting history. |
| **Probability calibration** | Raw boosted scores are over-confident. A Platt (sigmoid) calibration layer makes the probabilities honest — which is what makes the Monte-Carlo simulation meaningful. |
| **Football-native evaluation** | We report the **Ranked Probability Score** (Constantinou & Fenton, 2012) alongside accuracy, log-loss and Brier, and benchmark against an **Elo-only "market"** and a logistic-regression baseline. |
| **Walk-forward backtest** | The model is retrained season-by-season and scored on the *next* year it has never seen — the faithful test of a live forecaster. |
| **Two-phase training** | Phase 1 measures generalisation on an untouched test window; Phase 2 refits the production models on *all* pre-tournament data so the actual forecast uses every match up to kick-off. |

---

## Results

### Out-of-sample model comparison
Test window **2025-07-01 → 2026-06-10** (n = 906 matches, none seen in training):

| Model | Accuracy | Log-loss | Brier | RPS |
| --- | ---: | ---: | ---: | ---: |
| **XGBoost (calibrated)** | **63.4%** | 0.838 | 0.488 | 0.160 |
| XGBoost (raw) | 63.0% | 0.829 | 0.486 | 0.159 |
| Logistic regression | 62.0% | 0.838 | 0.490 | 0.161 |
| Elo-only baseline | 61.7% | 0.841 | 0.492 | 0.162 |
| Base-rate (climatology) | 47.9% | 1.050 | 0.633 | 0.229 |

*Lower log-loss / Brier / RPS is better.*

### Walk-forward backtest (2014 – 2025)
Retrained every season on an expanding window. Mean **accuracy 59.0%**,
log-loss 0.895, RPS 0.176 — with realistic year-to-year variance
(0.507 in the sparse 2020 COVID year, 0.642 in 2021).

### 2026 World Cup battle test
Graded on the **96** knockout-and-group matches already played (all strictly
after the training cutoff):

| Stage | Matches | Accuracy |
| --- | ---: | ---: |
| Group Stage | 72 | 58.3% |
| Round of 32 | 16 | 68.8% |
| Round of 16 | 8 | 50.0% |
| **Overall** | **96** | **59.4%** |

### TabFM foundation-model ensemble
Google Research's **TabFM** is blended with the calibrated XGBoost classifier by
in-context learning, with the blend weight tuned to minimise RPS. On the 200
most-recent test matches the ensemble beats the baseline on every metric:

| Outcome model | Accuracy | Log-loss | Brier | RPS |
| --- | ---: | ---: | ---: | ---: |
| XGBoost (calibrated) | 58.0% | 0.893 | 0.526 | 0.1677 |
| TabFM (in-context) | 58.5% | 0.889 | 0.521 | 0.1653 |
| **XGBoost + TabFM ensemble** | **59.0%** | **0.885** | **0.520** | **0.1649** |

RPS-optimal blend: **w = 0.75 on TabFM** (XGBoost anchors the rest). See
[`docs/METHODOLOGY.md`](docs/METHODOLOGY.md) §6 for the full derivation and the
dual-OpenMP engineering note.

### Championship odds — as of 2026-07-10
Conditioned on the completed quarter-final **France 1–0 Morocco**, from 50,000
Monte-Carlo replays with the ensemble:

| Team | Elo | Reach SF | Reach Final | **Win WC** |
| --- | ---: | ---: | ---: | ---: |
| 🇫🇷 France | 2203 | 100.0% | 53.1% | **29.3%** |
| 🇦🇷 Argentina | 2233 | 75.2% | 49.7% | **26.8%** |
| 🇪🇸 Spain | 2238 | 71.1% | 37.9% | **22.2%** |
| 🏴 England | 2147 | 65.2% | 29.4% | **12.5%** |
| 🇧🇪 Belgium | 2045 | 28.9% | 9.0% | **3.2%** |
| 🇳🇴 Norway | 2036 | 34.8% | 11.0% | **3.2%** |
| 🇨🇭 Switzerland | 2024 | 24.8% | 9.8% | **2.8%** |
| 🇲🇦 Morocco | 2054 | 0.0% | 0.0% | **0.0%** |

France leapfrogs Argentina into favouritism — not because its ratings changed,
but because it is now *guaranteed* into the semi-finals while the others must
still win their quarter-finals.

### Quarter-final predictions

| Match | Team 1 | Draw | Team 2 | Expected score | Status |
| --- | ---: | ---: | ---: | :--: | :-- |
| France vs Morocco | 100.0% | 0.0% | 0.0% | 1.7 – 1.1 | played — France won |
| Spain vs Belgium | 57.4% | 27.2% | 15.4% | 1.8 – 1.1 | upcoming |
| Argentina vs Switzerland | 62.6% | 25.4% | 11.9% | 1.9 – 0.9 | upcoming |
| Norway vs England | 19.8% | 29.4% | 50.8% | 1.0 – 1.8 | upcoming |

The full auto-generated report lives in
[`reports/world_cup_2026_report.md`](reports/world_cup_2026_report.md).

---

## How it works

```
 raw results (1872–2026)
        │
        ▼
 ┌──────────────┐   chronological, leakage-free
 │  features    │   Elo · rolling form · momentum · rest · experience
 └──────┬───────┘
        ▼
 ┌──────────────┐   time-decayed weights · early stopping
 │   model      │   XGBoost outcome classifier + calibration
 │              │   2× Poisson goal regressors  (count:poisson)
 └──────┬───────┘
        ▼
 ┌──────────────┐   walk-forward backtest + 2026 battle test
 │  evaluate    │   accuracy · log-loss · Brier · RPS vs baselines
 └──────┬───────┘
        ▼
 ┌──────────────┐   optional: blend TabFM (in-context learning)
 │ tabfm_ensemble│  w·P_TabFM + (1−w)·P_XGB, weight tuned by RPS
 └──────┬───────┘
        ▼
 ┌──────────────┐   50,000× vectorised bracket replays
 │  simulate    │   Poisson scorelines / outcome draws + shootouts,
 │              │   conditioned on completed ties
 └──────┬───────┘
        ▼
   report + plots
```

**The Elo engine** initialises every team at 1500 and updates chronologically
with competition-tier K-factors (World Cup finals `K=60`, continental `50`,
qualifiers `40`, friendlies `20`) and a goal-margin multiplier for blowouts.

**The outcome model** is a gradient-boosted classifier over 17 features (Elo
differential with home advantage, expected win probability, rolling
goals/win-rate, Elo momentum, rest and experience differentials), wrapped in a
calibration layer.

**The goal model** is a pair of Poisson (`count:poisson`) regressors whose
expected goals feed the tournament simulator, where scorelines are drawn per
match and level knockouts are decided by a shootout.

---

## Quickstart

```bash
# 1. create an environment and install
python -m venv venv && source venv/bin/activate
pip install -e ".[dev]"

# 2. run the whole pipeline (download → features → train → backtest → simulate → report)
wc2026 all --download

# …or step by step
wc2026 download        # fetch raw datasets
wc2026 features        # build the leakage-free feature table
wc2026 train           # train, calibrate & evaluate
wc2026 backtest        # walk-forward backtest + 2026 battle test
wc2026 simulate -n 50000
wc2026 tabfm           # optional: TabFM ensemble + refreshed forecast
wc2026 report          # render markdown + plots

# tests
pytest -q
```

The TabFM ensemble is a heavy optional extra (`pip install -e ".[tabfm]"`,
~6 GB of cached weights); the whole core pipeline runs without it and every
TabFM code path degrades gracefully when it is absent.

Every command is also available as `python -m wc2026 <command>` and via the
`Makefile` (`make all`, `make test`, …).

---

## Project structure

```
world-cup-2026-predictor/
├── src/wc2026/
│   ├── config.py          # paths, dataset URLs, all tunable constants
│   ├── data.py            # download & load raw datasets
│   ├── features.py        # chronological Elo + form feature engineering
│   ├── metrics.py         # log-loss, Brier, Ranked Probability Score
│   ├── model.py           # calibrated outcome + Poisson goal models
│   ├── tabfm_ensemble.py  # TabFM foundation-model ensemble (optional)
│   ├── evaluate.py        # walk-forward backtest + battle test
│   ├── simulate.py        # vectorised Monte-Carlo tournament engine
│   ├── bracket.py         # deterministic "chalk" bracket walk-through
│   ├── visuals.py         # scoreline-probability heatmaps
│   ├── report.py          # markdown report + plots
│   └── cli.py             # `wc2026` command-line interface
├── docs/METHODOLOGY.md    # research-grade methodology write-up
├── tests/                 # unit tests (features, metrics, ensemble, sim)
├── data/                  # raw CSVs (downloaded)
├── artifacts/             # generated features, models & result tables
├── reports/               # generated report + figures
├── pyproject.toml
└── Makefile
```

---

## Data & credits

- **Historical results** — [martj42/international_results](https://github.com/martj42/international_results)
- **2026 schedule / bracket** — [lbenz730/world_cup_2026](https://github.com/lbenz730/world_cup_2026)

Ranked Probability Score follows Constantinou & Fenton, *"Solving the problem of
inadequate scoring rules for assessing probabilistic football forecasts"*,
Journal of Quantitative Analysis in Sports (2012).

---

## Author

**Chouaieb Nemri** — Generative AI Blackbelt at Google Cloud (Toulouse, France).
I build and scale enterprise AI/ML systems; this project is a compact showcase of
end-to-end ML engineering: leakage-safe feature pipelines, honest evaluation,
probability calibration, and simulation.

- 🌐 [nemri.com](https://www.nemri.com)
- 💼 [linkedin.com/in/nemri](https://linkedin.com/in/nemri)
- 🐙 [github.com/cnemri](https://github.com/cnemri)
- 🐦 [x.com/c_nemri](https://x.com/c_nemri)

## License

Released under the [MIT License](LICENSE) © 2026 Chouaieb Nemri.
