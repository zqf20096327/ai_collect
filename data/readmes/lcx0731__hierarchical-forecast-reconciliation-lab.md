# Hierarchical Forecast Reconciliation Lab

A reproducible forecasting study of a question that appears whenever predictions
must add up across products, regions, or business units: how should independently
trained forecasts be made coherent?

The project generates a deterministic synthetic weekly retail hierarchy, produces
leakage-safe expanding-window base forecasts, and compares two reconciliation
strategies:

- **Base:** independent log-scale ridge autoregressions at all seven nodes.
- **Bottom-up:** retain the four bottom forecasts and sum them upward.
- **MinT:** project all base forecasts onto the coherent subspace, weighted by a
  Ledoit-Wolf estimate of the calibration-error covariance.

The data are synthetic by design, so the repository is fully reproducible and does
not contain private or externally downloaded data.

## Hierarchy

```text
Total
├── North
│   ├── North_A
│   └── North_B
└── South
    ├── South_A
    └── South_B
```

If `b` is the four-vector of bottom-level forecasts, every coherent seven-vector
can be written as `S @ b`. Bottom-up constructs such a vector directly. MinT solves
the corresponding covariance-weighted projection problem and can use information
from forecasts at every level.

## Evaluation design

- 260 weekly observations with annual and semiannual seasonality, trend, correlated
  regional shocks, persistent local shocks, and Poisson observation noise.
- 52 expanding-window origins estimate forecast-error covariance.
- The following 52 origins are a held-out test period.
- Every prediction at week `t` is trained only on observations before `t`.
- Metrics are reported per series; level charts average series-level RMSE so the
  four bottom nodes do not silently dominate the comparison.

## Reproduce

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[test]"
pytest -W error
python -m hierarchical_forecast_reconciliation_lab --output-dir artifacts
```

The experiment writes machine-readable forecasts, metrics, calibration covariance,
coherence diagnostics, and three figures to `artifacts/`.

## Results

The checked-in run used seed `20260925`. Values below are held-out RMSE; region and
bottom entries are the unweighted mean across series at that level.

| Method | Total | Region | Bottom | Mean max hierarchy gap |
|---|---:|---:|---:|---:|
| Base | 26.742 | 17.027 | 10.468 | 5.546 |
| Bottom-up | **25.839** | 17.172 | **10.468** | < 1e-12 |
| MinT | 26.195 | 17.239 | 10.493 | < 1e-12 |

Both reconciliation methods enforce the hierarchy to floating-point precision.
Bottom-up reduced total-series RMSE by 3.4% while leaving bottom forecasts unchanged.
MinT reduced total RMSE by 2.0%, but slightly increased average RMSE at the region
and bottom levels. That mixed outcome is useful: coherence is guaranteed by the
projection, whereas an accuracy gain is not. Method selection therefore needs a
held-out evaluation aligned with the level that matters operationally.

![Held-out RMSE by level](artifacts/rmse_by_level.png)

The independent log-scale models had a maximum single-origin hierarchy violation of
14.607 demand units. `artifacts/coherence_gaps.png` shows the reconciled gaps at
numerical zero, and `artifacts/total_forecasts.png` compares the total-series paths.

## Repository structure

```text
src/hierarchical_forecast_reconciliation_lab/
  simulation.py       # coherent synthetic weekly demand
  forecasting.py      # expanding-window log-ridge base forecasts
  reconciliation.py   # bottom-up and MinT projection
  evaluation.py       # split, metrics, and artifact generation
  reporting.py        # static figures
tests/                 # hierarchy, leakage, reconciliation, and E2E tests
artifacts/             # reproducible outputs from the default run
```

## Limitations

- Synthetic demand demonstrates the mechanics but is not evidence of production
  performance on a particular retailer or market.
- The one-step ridge model is deliberately compact; forecast reconciliation cannot
  repair systematic errors shared by all nodes.
- MinT quality depends on calibration errors representing future errors. Structural
  breaks or too little calibration data can make that estimate unreliable.
- Unconstrained MinT can produce negative forecasts in other datasets. This example
  reports the minimum forecast explicitly instead of silently clipping values,
  because clipping individual nodes would break coherence.
- Only point forecasts are reconciled; probabilistic reconciliation is out of scope.

## Responsible use

This repository is an educational portfolio project. It uses no real company data
and should not be interpreted as operational demand-planning advice.
