# Correlated Feature Importance Lab

A reproducible explainable-machine-learning audit showing why a single feature-
importance ranking is not enough when predictors are correlated or redundant.
The project compares marginal, grouped, and approximate conditional permutation
importance on an independent held-out set.

## What this demonstrates

- A nonlinear tree ensemble evaluated strictly on unseen synthetic data.
- Marginal permutation importance for every individual feature.
- Joint permutation that preserves the internal relationship of a correlated group.
- Conditional permutation within equal-frequency bins of a partner feature.
- Repeated shuffles with 5th–95th percentile uncertainty summaries.
- A side-by-side impurity-importance output to expose method dependence.
- Deterministic tests for data generation, shuffling invariants, grouped effects,
  reproducibility, and the complete workflow.

## Data-generating process

All data are generated locally; there is no private or downloaded data. `x1_proxy`
and `x2_proxy` are noisy measurements of the same unobserved Gaussian signal and
are therefore highly correlated. The target also contains a nonlinear effect of
`x3_nonlinear`, a weaker linear effect of `x4_weak`, independent noise, and no
effect from `x5_noise`.

The documented run fits an Extra Trees regressor on 5,000 observations and audits
importance on an independent 3,000-observation test set. Forty shuffles are used
for each importance target.

## Importance questions

- **Marginal permutation:** how much does test error rise after breaking this
  feature's joint relationship with every other feature?
- **Grouped permutation:** how much does test error rise after jointly shuffling
  both redundant proxies with one shared row permutation?
- **Binned conditional permutation:** how much unique predictive information
  remains after shuffling one proxy only among observations with similar values
  of the other proxy?

These quantities answer different questions and are not additive decompositions.

## Quick start

Requires Python 3.10 or newer.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pytest -W error
python -m correlated_feature_importance_lab \
  --output-dir artifacts \
  --train-size 5000 \
  --test-size 3000 \
  --repeats 40 \
  --seed 20260924
```

## Reproducible result

The checked-in artifacts use the command above. Results apply only to this
synthetic generator, fitted model, held-out sample, and seed.

The held-out proxy correlation is 0.9421. The model obtains test RMSE 1.0984 and
`R² = 0.8051`. Repeated held-out permutation results are:

| Question | Importance target | Mean MSE increase | 5th–95th percentile |
| --- | --- | ---: | ---: |
| Marginal | `x1_proxy` | 2.0720 | [1.9634, 2.1930] |
| Marginal | `x2_proxy` | 1.9187 | [1.8369, 2.0112] |
| Grouped | `x1_proxy` + `x2_proxy` | 7.5967 | [7.3428, 7.7862] |
| Conditional | `x1_proxy` given `x2_proxy` | 0.2508 | [0.2264, 0.2754] |
| Conditional | `x2_proxy` given `x1_proxy` | 0.2677 | [0.2409, 0.2990] |
| Marginal | `x3_nonlinear` | 1.7352 | [1.6700, 1.8143] |
| Marginal | `x4_weak` | 0.3762 | [0.3533, 0.4068] |
| Marginal | `x5_noise` | 0.0018 | [-0.0014, 0.0050] |

The individual proxy scores say that the fitted model uses each measurement,
while the much smaller conditional scores say that either proxy adds little
unique information once similar values of its partner are held nearby. Jointly
moving the pair produces the largest error increase because it removes the shared
latent signal while preserving the pair's internal relationship. These numbers
must not be added together: the perturbations define different prediction tasks.
The known noise feature's interval crosses zero, although the tree model still
assigns it a small normalized impurity importance of 0.0075—another reason not to
treat one ranking as ground truth.

![Correlation audit](artifacts/correlation_audit.png)

![Permutation importance](artifacts/permutation_importance.png)

![Conditional importance](artifacts/conditional_importance.png)

## Interpretation boundaries

Permutation importance describes a fitted model's dependence on inputs, not a
causal effect or a claim that the data-generating feature is intrinsically
important. Marginal shuffles can create implausible feature combinations when
predictors are correlated. Grouped scores depend on analyst-defined groups.
The conditional method here uses coarse equal-frequency bins; it only approximates
the conditional feature distribution and can be sensitive to bin count and sample
size. Impurity importance has its own split-selection biases.

This project does not implement causal attribution, SHAP values, knockoffs, exact
conditional samplers, feature selection guarantees, or external validation.

## Repository layout

```text
src/correlated_feature_importance_lab/
  simulation.py # redundant-proxy nonlinear regression generator
  importance.py # marginal, grouped, and conditional shuffles
  evaluation.py # held-out model and importance audit
  reporting.py  # CSV/JSON outputs and charts
  cli.py        # reproducible command-line workflow
tests/           # shuffling, estimator, and end-to-end tests
artifacts/       # checked-in outputs from the documented run
```

## License

MIT
