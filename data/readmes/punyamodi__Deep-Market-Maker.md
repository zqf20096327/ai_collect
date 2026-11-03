# Adaptive Market-Making via Order Flow Toxicity Prediction

> **Real-time adaptive market-making system** that learns to detect toxic order flow from limit order book microstructure and calibrates quotes dynamically to avoid adverse selection.

![Architecture](figures/architecture.png)

---

## 3D Spread Surface: Inventory × Toxicity → Optimal Spread

The core insight of the system — as order flow toxicity rises, spreads must widen dramatically to compensate for adverse selection risk. The surface shows the model's quoting policy across all inventory and toxicity states:

![3D Spread Surface](figures/spread_surface_3d.png)

> _Blue = tight spreads (benign, flat inventory). Red/white peaks = toxic regime at extreme inventory → spread widens ×2.5_

---

## Overview

Market makers profit from the bid-ask spread but lose to informed traders who know the short-term price direction before the market does. This system learns to detect **toxic order flow** — the probability that a fill will immediately move against the market maker — and uses that signal to widen spreads, reduce size, and skew quotes accordingly.

### Full Pipeline

```
LOBSTER L3 data
      │
      ▼
LOB Reconstruction ──────────────── OFI Features (multi-scale, multi-level)
      │                                      │
      ▼                                      │
Hawkes Calibration ── Intensity Tracker ────►│
      │                                      │
      └──────────────────────────────────────┼─────►  MHLOBT Model
                                             │         (TCN + Hawkes Embed + OFI MLP)
                                             │              │
                                             │         Toxicity Prob ∈ (0,1)
                                             │         Return Pred (signed)
                                             │         Uncertainty σ² > 0
                                             │              │
                                             ▼              ▼
                                      Avellaneda-Stoikov Base Policy
                                             +
                                      Toxicity Adjustment Layer
                                             │
                                             ▼
                                     Simulated Exchange
                              (queue-position fills, latency jitter)
```

---

## Strategy Dashboard

Real-time view of all key signals: mid-price, toxicity probability, spread response, inventory position, and cumulative PnL. Red background regions indicate periods when the toxicity model widened spreads to avoid adverse selection:

![Strategy Dashboard](figures/strategy_dashboard.png)

---

## Hawkes Process: Mutually Exciting Order Arrivals

The system calibrates a bivariate Hawkes process on bid/ask arrivals to capture self-excitation (a flood of buys begets more buys) and cross-excitation (buy pressure triggers reactive sells). The intensity ratio λ_bid/λ_ask forms a key feature for toxicity prediction:

![Hawkes Intensity](figures/hawkes_intensity.png)

---

## Limit Order Book Depth Heatmap

The LOB depth visualized over time — green = bid side liquidity, red = ask side. Mid-price is overlaid in blue. The bottom panel shows quoted spread in ticks:

![LOB Depth](figures/lob_depth_heatmap.png)

---

## Architecture

### 1. LOB Reconstruction (`src/lob/`)

- **`parser.py`** — LOBSTER L3 CSV parser. Converts integer prices to dollars, filters to trading session (09:30–16:00 ET), strips trading halts.
- **`reconstructor.py`** — Incremental state machine. Exposes mid-price, spread, book imbalance, and **Order Flow Imbalance (OFI)** (Cont et al., 2014).

### 2. Hawkes Processes (`src/hawkes/`)

- **`kernel.py`** — Exponential kernel φ(τ) = α·exp(−β·τ), O(N) recursive sum.
- **`calibration.py`** — `BivariateHawkesMLE`: L-BFGS-B MLE with multiple restarts, stationarity check, CIs from numerical Hessian.
- **`intensity.py`** — `HawkesIntensityTracker`: O(1)-per-event online tracker. Outputs 8-dim feature vector [μ_b, μ_a, α_bb, α_ba, α_ab, α_aa, λ_b, λ_a].

### 3. Toxicity Model (`src/toxicity/`)

**MHLOBT (Multi-Horizon LOB-OFI Toxicity Network)** — three input streams fused via cross-attention:

| Stream       | Input                     | Architecture          |
| ------------ | ------------------------- | --------------------- |
| LOB Temporal | (B, T, 4·L) LOB snapshots | Causal dilated TCN    |
| Hawkes State | (B, 8) intensity features | 2-layer MLP           |
| OFI Features | (B, D) multi-scale OFI    | 2-layer MLP + dropout |

| Output          | Range  | Meaning                                      |
| --------------- | ------ | -------------------------------------------- |
| `toxicity_prob` | (0, 1) | P(fill is adverse)                           |
| `return_pred`   | ℝ      | Expected signed mid return                   |
| `uncertainty`   | > 0    | Aleatoric σ² for uncertainty-weighted sizing |

### 4. Strategy (`src/strategy/`)

- **`avellaneda_stoikov.py`** — Closed-form A-S. r = s − q·γ·σ²·(T−t). δ = γ·σ²·(T−t) + (2/γ)·ln(1+γ/κ).
- **`inventory.py`** — FIFO PnL, MTM, maker/taker fees, skew signal ∈ [−1,1].
- **`adaptive_mm.py`** — Toxicity gating: toxicity > 0.65 → spread ×2.5, size ×0.5. toxicity < 0.35 → tighten 10%.

### 5. Simulation (`src/simulation/`)

- **`fill_model.py`** — Power-law fill prob P(fill) = (1−q/V)^α, MLE calibration.
- **`latency.py`** — Log-normal latency jitter (μ=500μs), stale-quote detection.
- **`exchange.py`** — Event-driven matching, self-trade prevention, retrospective adverse-fill labeling.

### 6. Analysis (`src/analysis/`)

| Module                | Purpose                                                            |
| --------------------- | ------------------------------------------------------------------ |
| `ic_analysis.py`      | IC/ICIR decay, rolling IC, zero-cost portfolio Sharpe              |
| `pnl_attribution.py`  | Spread capture / adverse selection / inventory carry decomposition |
| `regime.py`           | 3-state Gaussian HMM regime detection                              |
| `multiple_testing.py` | BH FDR, SPA test, Deflated Sharpe Ratio                            |

---

## Quickstart

### Install

```bash
git clone https://github.com/punyamodi/toxic-flow-mm.git
cd toxic-flow-mm
pip install -r requirements.txt
```

### Run tests

```bash
pytest tests/ -v
# Expected: 28 passed
```

### Synthetic data backtest

```python
from src.lob.parser import generate_synthetic_lobster_data
from src.strategy.avellaneda_stoikov import AvellanedaStoikov
from src.strategy.adaptive_mm import AdaptiveMarketMaker
from src.simulation.fill_model import QueuePositionFillModel
from src.simulation.latency import LatencySampler
from src.simulation.exchange import SimulatedExchange

events, _ = generate_synthetic_lobster_data(n_events=10_000, seed=42)

strategy = AdaptiveMarketMaker(
    base_strategy=AvellanedaStoikov(gamma=0.1, kappa=1.5),
    toxicity_model=None,      # plug in a trained ToxicityPredictor here
    max_inventory=500,
    order_size=100,
)
exchange = SimulatedExchange(
    fill_model=QueuePositionFillModel(alpha=0.6),
    latency_sampler=LatencySampler(submit_mean_us=500),
)
result = exchange.run(events, strategy)
print(f"PnL={result.total_pnl:.2f}  Sharpe={result.sharpe_ratio:.3f}  MaxDD={result.max_drawdown:.2f}")
```

### Train toxicity model

```python
from src.toxicity.model import ToxicityPredictor
from src.toxicity.trainer import ToxicityTrainer

model = ToxicityPredictor(n_levels=5, seq_len=100, n_hawkes=8, n_ofi=32)
trainer = ToxicityTrainer(model, train_loader, val_loader, checkpoint_dir="checkpoints/")
history = trainer.train(n_epochs=100)
trainer.calibrate()   # isotonic regression on val set
print(trainer.evaluate())
```

### Regenerate figures

```bash
python generate_figures.py
```

### Real LOBSTER data

```python
from src.lob.parser import parse_lobster

events = parse_lobster(
    msg_path="data/raw/AAPL_2012-06-21_34200000_57600000_message_5.csv",
    book_path="data/raw/AAPL_2012-06-21_34200000_57600000_orderbook_5.csv",
    n_levels=5,
)
```

See [`LOBSTER_DATA.md`](LOBSTER_DATA.md) for data format details and acquisition instructions.

---

## Repository Structure

```
toxic-flow-mm/
├── configs/
│   └── default.yaml            # All hyperparameters
├── figures/                    # README visualizations
│   ├── architecture.png
│   ├── spread_surface_3d.png
│   ├── strategy_dashboard.png
│   ├── hawkes_intensity.png
│   └── lob_depth_heatmap.png
├── src/
│   ├── lob/
│   │   ├── parser.py           # LOBSTER L3 parser + synthetic generator
│   │   ├── reconstructor.py    # Incremental LOB state machine
│   │   └── features.py         # Multi-scale OFI feature engineering
│   ├── hawkes/
│   │   ├── kernel.py           # Exponential kernel + O(N) recursive sums
│   │   ├── calibration.py      # Bivariate Hawkes MLE (L-BFGS-B)
│   │   └── intensity.py        # Online O(1)-per-event intensity tracker
│   ├── toxicity/
│   │   ├── model.py            # MHLOBT: TCN + Hawkes embed + OFI MLP + cross-attention
│   │   ├── labeler.py          # Adverse fill labeling
│   │   ├── dataset.py          # PyTorch Dataset / DataLoader
│   │   └── trainer.py          # Training loop, calibration, feature importance
│   ├── strategy/
│   │   ├── avellaneda_stoikov.py  # A-S closed-form quoting policy
│   │   ├── inventory.py           # FIFO PnL, inventory limits, skew signal
│   │   └── adaptive_mm.py         # Toxicity-augmented MM strategy
│   └── simulation/
│       ├── fill_model.py       # Power-law queue-position fill probability
│       ├── latency.py          # Log-normal latency + stale-quote detection
│       ├── exchange.py         # Event-driven matching engine
│       └── backtest.py         # run_backtest() / compare_strategies() API
├── tests/                      # 28 unit tests (pytest)
├── generate_figures.py         # Reproduce all README figures
├── smoke_test.py               # End-to-end pipeline validation
├── requirements.txt
├── pyproject.toml
├── LOBSTER_DATA.md
└── README.md
```

---

## Key Design Decisions

**No look-ahead bias** — all features at time t use only events at t′ ≤ t. The TCN uses left-only (causal) padding. Adverse-fill labels are applied retrospectively by the exchange, not the strategy.

**Authoritative snapshots** — the LOB reconstructor uses LOBSTER's curated book snapshots as ground truth, avoiding accumulated reconstruction errors.

**Calibrated uncertainty** — aleatoric σ² trained via Gaussian NLL enables uncertainty-weighted quote sizing.

**Realistic simulation** — fills are gated by queue-position probability (power-law model), and all orders face log-normal latency with stale-quote rejection.

**Statistical validation** — BH FDR, SPA test, and Deflated Sharpe Ratio prevent false positives from overfitting.

---

## References

1. Avellaneda, M. & Stoikov, S. (2008). _High-frequency trading in a limit order book_. Quantitative Finance, 8(3), 217–224.
2. Cont, R., Kukanov, A. & Stoikov, S. (2014). _The price impact of order book events_. Journal of Financial Econometrics, 12(1), 47–88.
3. Hawkes, A. G. (1971). _Spectra of some self-exciting and mutually exciting point processes_. Biometrika, 58(1), 83–90.
4. Stoikov, S. (2018). _The micro-price: a high-frequency estimator of future prices_. Quantitative Finance, 18(12), 1959–1966.
5. Hansen, P. R. (2005). _A test for superior predictive ability_. Journal of Business & Economic Statistics, 23(4), 365–380.
6. Bailey, D. H. & López de Prado, M. (2014). _The deflated Sharpe ratio_. Journal of Portfolio Management, 40(5), 94–107.
