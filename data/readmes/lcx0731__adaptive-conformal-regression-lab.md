# Adaptive Conformal Regression Lab

A compact, reproducible uncertainty-quantification project for machine learning
and data science portfolios. It builds fixed-width and locally adaptive split-
conformal prediction intervals, audits their empirical coverage, and demonstrates
why the usual guarantee does not automatically survive distribution shift.

The experiment uses a fully documented synthetic nonlinear regression problem
with feature-dependent noise. Oracle noise scales appear only in evaluation
diagnostics; neither model receives them as features.

## What this demonstrates

- Leakage-resistant four-way partitioning: mean-model training, scale-model
  training, conformal calibration, and final testing are disjoint.
- The exact finite-sample conformal order statistic rather than an approximate
  percentile that can be off by one.
- Fixed-width split conformal and locally scaled conformal intervals.
- A deliberately uncalibrated Gaussian baseline for comparison.
- Overall coverage, interval width, interval score, and coverage by true noise
  quartile.
- A pre-defined stress test with shifted covariates and 1.55× conditional noise.
- Deterministic artifacts, unit tests, and GitHub Actions CI.

## Design

The sample is randomly divided 40% / 20% / 20% / 20%:

```text
train mean model → learn scale from fresh residuals → calibrate scores → test once
      40%                    20%                      20%           20%
```

For calibration residuals `r_i = |y_i - m_hat(x_i)|`, fixed conformal uses the
order statistic at rank

```text
ceil((n_calibration + 1) * (1 - alpha)).
```

The adaptive method first learns a positive local scale `s_hat(x)` on the
separate scale split, calibrates `r_i / s_hat(x_i)`, and multiplies the resulting
quantile by each test row's predicted scale. This changes interval widths across
the feature space while preserving the split-conformal marginal-coverage logic
when calibration and future examples are exchangeable. The scale floor is fixed
at `0.05` before calibration, and its activation rate is reported. The Gaussian
plug-in baseline uses the root-mean-square residual from the scale split and is
not conformally calibrated.

## Quick start

Requires Python 3.10 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
python -m adaptive_conformal_regression_lab \
  --output-dir artifacts \
  --samples 6000 \
  --alpha 0.10 \
  --seed 20260912
```

The command creates:

- `metrics.csv`: IID and shifted coverage, width, and interval score.
- `coverage_by_noise.csv`: coverage and width within four oracle noise quartiles.
- `coverage_width_grid.csv`: coverage–width results at 80%, 90%, and 95% targets.
- `run_summary.json`: configuration, split audit, quantiles, and headline metrics.
- Two diagnostic charts ready to inspect in the README.

## Reproducible result

The checked-in artifacts use the command above. Results describe this synthetic
generator and seed only; they do not establish universal model performance.

| Method | IID coverage | IID mean width | Shifted coverage | Shifted mean width |
| --- | ---: | ---: | ---: | ---: |
| Gaussian plug-in | 91.7% | 3.318 | 69.2% | 3.318 |
| Fixed conformal | 89.8% | 3.122 | 66.3% | 3.122 |
| Adaptive conformal | 93.1% | 3.585 | 78.6% | 4.328 |

At the 90% target, fixed conformal was close to nominal marginal coverage on
the IID test, but its coverage ranged from 96.7% in the lowest-noise quartile to
79.7% in the highest. Adaptive widths produced 94.3% and 94.7%, respectively,
at the cost of wider average intervals in this run. Under the deliberately harder
shift, all methods missed the target; adaptive scaling reduced, but did not solve,
the coverage loss. See the complete [metrics](artifacts/metrics.csv) and
[run diagnostics](artifacts/run_summary.json).

![Coverage by noise quartile](artifacts/coverage_by_noise.png)

![Coverage-width frontier](artifacts/coverage_width_frontier.png)

## Guarantee and limitations

Under exchangeability of calibration and future observations, split conformal
provides a finite-sample **marginal** coverage guarantee (with the usual handling
of ties). It does not promise exact conditional coverage for every feature value
or subgroup. The learned local scale can improve efficiency and subgroup behavior,
but it does not create a stronger distribution-free guarantee.

The shifted test set intentionally violates exchangeability by changing the
feature distribution and increasing conditional noise. Its coverage is a stress
diagnostic, not a conformal guarantee. Real deployments would need drift monitoring,
careful recalibration, domain-specific loss choices, and repeated evaluation.
Synthetic results validate this implementation under a known generator; they are
not evidence about a real population.

## Repository layout

```text
src/adaptive_conformal_regression_lab/
  simulation.py  # nonlinear IID and shifted environments
  data.py        # audited four-way split
  conformal.py   # models, scores, quantiles, intervals
  evaluation.py  # overall, subgroup, and shift metrics
  reporting.py   # JSON/CSV outputs and charts
  cli.py         # reproducible command-line workflow
tests/            # quantile, leakage, determinism, and coverage tests
artifacts/        # outputs from the documented run
```

## License

MIT
