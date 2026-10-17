# Survival Model Validation Lab

A compact, reproducible survival-analysis project that fits a Cox proportional-
hazards model from first principles and validates predictions without treating
right-censored observations as ordinary failures.

## What this demonstrates

- Deterministic Weibull proportional-hazards simulation with independent random
  censoring and administrative censoring.
- Kaplan–Meier product-limit estimation, including left-limit evaluation.
- Cox partial-likelihood optimization, observed-information standard errors,
  and a Breslow cumulative baseline hazard.
- Harrell concordance, inverse-probability-of-censoring-weighted Brier scores,
  and horizon-specific calibration against Kaplan–Meier estimates.
- Strict train/test separation and an oracle benchmark available only in simulation.
- Unit and end-to-end tests for censoring logic, estimation, prediction, and metrics.

## Data-generating process

All data are generated locally; there is no private or downloaded data. Three
correlated Gaussian features affect a Weibull baseline hazard through true log
hazard coefficients `(0.70, -0.50, 0.30)`. Event times are independently censored
by an exponential censoring time and an administrative horizon of 20 time units.

The documented run trains on 2,500 observations and evaluates once on an
independent 2,000-observation test set. Features are standardized using training
statistics only. Censoring weights are also estimated from the training set.

## Quick start

Requires Python 3.10 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest -W error
python -m survival_model_validation_lab \
  --output-dir artifacts \
  --train-size 2500 \
  --test-size 2000 \
  --weibull-shape 1.4 \
  --weibull-scale 12 \
  --censoring-scale 18 \
  --administrative-horizon 20 \
  --seed 20260923
```

## Reproducible result

The checked-in artifacts use the command above. Results describe only this
synthetic generator, split, estimator, horizons, and seed.

The train and test censoring fractions are 45.24% and 45.65%. The fitted Cox
model converges, and every known standardized data-generating coefficient lies
inside its model-based 95% interval:

| Feature | Cox estimate | 95% interval | Known DGP coefficient |
| --- | ---: | ---: | ---: |
| `x1` | 0.7087 | [0.6447, 0.7726] | 0.7095 |
| `x2` | -0.5205 | [-0.5826, -0.4584] | -0.5066 |
| `x3` | 0.3500 | [0.2934, 0.4065] | 0.3033 |

| Horizon | Cox IPCW Brier | KM-baseline IPCW Brier | Oracle IPCW Brier |
| --- | ---: | ---: | ---: |
| 4 | 0.1586 | 0.1815 | 0.1586 |
| 8 | 0.1998 | 0.2485 | 0.1989 |
| 12 | 0.1778 | 0.2305 | 0.1774 |
| 16 | 0.1403 | 0.1894 | 0.1400 |

The Cox test-set concordance is 0.6909, compared with 0.5000 for the
feature-free Kaplan–Meier baseline and 0.6907 for the known oracle risk score.
The tiny sample advantage over the oracle is random finite-test-set variation,
not evidence that the fitted model knows more than the generator. Across all
four horizons, Cox prediction error is close to the oracle and lower than the
feature-free baseline. The grouped time-12 calibration curve still shows local
gaps, which is why ranking and aggregate Brier scores are not treated as a full
calibration guarantee.

![Survival curves](artifacts/survival_curves.png)

![Cox coefficient recovery](artifacts/cox_coefficients.png)

![Validation audit](artifacts/validation_audit.png)

## Interpretation boundaries

The proportional-hazards assumption is true by construction here. The censoring
mechanism is independent conditional on no covariates, and the oracle probabilities
use the known generator; none of these conveniences should be assumed for real
data. Harrell concordance measures ranking rather than probability calibration.
IPCW Brier scores depend on a correctly estimated censoring distribution and can
be unstable when censoring survival is small. Kaplan–Meier calibration groups can
hide within-group errors.

The implementation uses Breslow handling for event-time ties and model-based
observed-information intervals. It does not implement time-varying covariates,
competing risks, stratification, robust sandwich errors, or external validation.

## Repository layout

```text
src/survival_model_validation_lab/
  simulation.py    # proportional-hazards event and censoring generator
  kaplan_meier.py  # product-limit estimator and step evaluation
  cox.py           # partial likelihood and Breslow baseline hazard
  metrics.py       # concordance, IPCW Brier score, and calibration
  evaluation.py    # leakage-safe train/test validation workflow
  reporting.py     # CSV/JSON outputs and charts
  cli.py           # reproducible command-line interface
tests/              # estimator, metric, edge-case, and workflow tests
artifacts/          # checked-in outputs from the documented run
```

## License

MIT
