# Doubly Robust Causal Lab

A compact, reproducible causal-inference project for data science and machine
learning portfolios. It estimates an average treatment effect (ATE) from
confounded observational data with cross-fitted augmented inverse probability
weighting (AIPW), then checks the estimator against a known simulation truth.

The project is deliberately transparent: every feature is pre-treatment, the
data-generating process is visible in code, every nuisance prediction is made
out of fold, and oracle columns are excluded from model inputs.

## What this demonstrates

- A nonlinear observational-data simulation with heterogeneous treatment effects.
- Treatment-stratified cross-fitting for propensity and outcome models.
- Four estimators: naive difference, normalized (Hájek) IPW, outcome regression,
  and AIPW.
- Positivity and weighting diagnostics, including clipping rate, weight tails,
  effective sample size, and standardized covariate differences.
- Held-out propensity log loss/Brier score and outcome RMSE.
- A deterministic Monte Carlo comparison using bias, RMSE, MAE, and approximate
  AIPW confidence-interval coverage.
- Automated tests and GitHub Actions CI.

## Method

For treatment `A`, outcome `Y`, covariates `X`, propensity `e(X)`, and outcome
regressions `mu_a(X)`, the implementation averages the score

```text
mu_1(X) - mu_0(X)
+ A * (Y - mu_1(X)) / e(X)
- (1 - A) * (Y - mu_0(X)) / (1 - e(X)).
```

Nuisance models are histogram gradient-boosted trees. For each fold, they are
trained only on the other folds and predict the held-out rows. Propensities are
clipped to `[0.02, 0.98]`; the generated report discloses how often clipping
occurs. The approximate 95% interval uses the empirical standard deviation of
the AIPW influence scores divided by the square root of the sample size.

“Doubly robust” means the AIPW estimator can be consistent when either the
propensity model or both outcome models are correctly specified, given the
identification and regularity conditions below. It does **not** mean finite-sample
unbiasedness or protection when both nuisance components are poor.

## Quick start

Requires Python 3.10 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
python -m doubly_robust_causal_lab --samples 2000 --repetitions 12 --folds 3
```

The command writes these reproducible artifacts:

- `single_run_summary.json`: configuration, estimates, interval, and diagnostics.
- `monte_carlo_results.csv`: every repetition and estimator.
- `monte_carlo_summary.csv`: bias, RMSE, MAE, and AIPW interval coverage.
- `propensity_overlap.png`: held-out propensity distributions by treatment arm.
- `estimator_errors.png`: estimation errors across repetitions.

## Example output

The checked-in artifacts use seed `20260911`. They are illustrative results for
the synthetic generator, not claims about real data. Recreate them exactly with:

```bash
python -m doubly_robust_causal_lab \
  --output-dir artifacts \
  --samples 2000 \
  --repetitions 12 \
  --folds 3 \
  --seed 20260911
```

For that 12-repetition run, the realized-sample-ATE errors were:

| Estimator | Bias | RMSE | MAE |
| --- | ---: | ---: | ---: |
| Naive difference | 0.6640 | 0.6667 | 0.6640 |
| Hájek IPW | -0.0933 | 0.1266 | 0.1115 |
| Outcome regression | 0.0234 | 0.0650 | 0.0534 |
| Cross-fitted AIPW | -0.0052 | 0.0777 | 0.0642 |

Twelve repetitions are enough for a quick, reproducible demonstration but not
for a precise coverage study. See the full [run-level results](artifacts/monte_carlo_results.csv)
and [diagnostics](artifacts/single_run_summary.json).

![Out-of-fold propensity overlap](artifacts/propensity_overlap.png)

![Monte Carlo estimator errors](artifacts/estimator_errors.png)

## Identification assumptions and limitations

Interpreting an estimate causally requires consistency/SUTVA, conditional
exchangeability (no unmeasured confounding after conditioning on `X`), and
positivity. These assumptions cannot be verified from observational data alone.
Cross-fitting reduces own-observation and overfitting bias; it does not repair
hidden confounding, post-treatment controls, selection bias, measurement error,
or weak overlap. Propensity clipping changes the estimand approximation and can
trade variance for bias. The confidence interval is asymptotic.

The simulator makes all confounders observed by construction, so successful
recovery here validates an implementation under its own assumptions—not causal
validity or predictive superiority in another setting. A real application would
also require domain-driven identification, data audits, sensitivity analysis,
and a prespecified estimand.

## Repository layout

```text
src/doubly_robust_causal_lab/
  simulation.py   # explicit data-generating process
  estimators.py   # cross-fitting, estimators, diagnostics
  evaluation.py   # repeated simulation study
  reporting.py    # JSON/CSV and chart generation
  cli.py          # reproducible command-line workflow
tests/             # deterministic unit and integration tests
artifacts/         # checked-in outputs from the documented run
```

## License

MIT
