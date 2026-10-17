# FairLens

[![PyPI version](https://img.shields.io/pypi/v/fairlens-kit)](https://pypi.org/project/fairlens-kit/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight toolkit for detecting bias in ML models and datasets.

## What is this?

FairLens started as a side project after I got frustrated with how complicated existing fairness tools are. I wanted something where you could just point it at a dataset or model and get a quick sense of whether there might be bias issues worth investigating.

It's not trying to replace comprehensive tools like AIF360 or Fairlearn - those are great if you need the full research toolkit. This is more for the "let me quickly check this before I ship it" use case.

## Installation

```bash
pip install fairlens-kit
```

For visualization support:
```bash
pip install fairlens-kit[viz]
```

## Basic Usage

### Dataset Analysis

```python
import fairlens as fl
import pandas as pd

df = pd.read_csv("your_data.csv")

# Check for potential bias
report = fl.check_dataset(
    df, 
    target='outcome', 
    protected=['gender', 'race']
)
print(report)
```

This gives you a breakdown of label rates across groups, flags large disparities, and checks for potential proxy variables.

### Model Auditing

```python
import fairlens as fl
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Audit the model
result = fl.audit_model(
    model,
    X_test,
    y_test,
    protected=test_data['gender']
)
print(result)
```

Output looks something like:

```
============================================================
FAIRNESS AUDIT REPORT - UNFAIR
============================================================

Model: Model
Protected Attribute: gender
Groups: Female, Male

GROUP FAIRNESS METRICS
----------------------------------------
Demographic Parity Ratio: 0.672 (threshold: >=0.8)
Equalized Odds Ratio: 0.734 (threshold: >=0.8)

ISSUES DETECTED
----------------------------------------
  - Demographic parity ratio (0.672) below threshold (0.8)
  - 'Female' receives positive predictions 32.8% less often than 'Male'

RECOMMENDATIONS
----------------------------------------
  - Consider rebalancing training data or using threshold adjustment
```

### Visualization

```python
import fairlens as fl

fl.plot_bias(df, target='hired', protected='gender')
```

## Built-in Datasets

The library includes some common fairness benchmark datasets so you can test things out:

```python
import fairlens as fl

adult = fl.datasets.load_adult()       # Income prediction
compas = fl.datasets.load_compas()     # Recidivism (the ProPublica one)  
credit = fl.datasets.load_german_credit()
bank = fl.datasets.load_bank_marketing()
```

These are synthetic versions for quick offline testing. If you want the real data:

```python
adult = fl.fetch_adult()          # Real UCI Adult from OpenML (48k rows)
compas = fl.fetch_compas()        # Real ProPublica COMPAS (7k rows)
credit = fl.fetch_german_credit() # Real German Credit from OpenML (1k rows)
```

Fetchers download and cache locally in `~/.fairlens/datasets/`. If the network is unavailable, they fall back to the synthetic versions automatically.

## Metrics

### Group Fairness

```python
from fairlens.metrics import (
    demographic_parity_ratio,
    demographic_parity_difference,
    equalized_odds_ratio,
    equalized_odds_difference,
)

# Demographic parity - are positive prediction rates similar across groups?
dpr = demographic_parity_ratio(y_pred, protected)

# Equalized odds - are TPR and FPR similar across groups?
eor = equalized_odds_ratio(y_true, y_pred, protected)
```

### Calibration

```python
from fairlens.metrics import expected_calibration_error, brier_score

ece = expected_calibration_error(y_true, y_prob)
```

### Individual Fairness

```python
from fairlens.metrics import consistency_score

# Do similar individuals get similar predictions?
score = consistency_score(X, y_pred, n_neighbors=5)
```

### Intersectional Fairness

Single-attribute analysis can miss disparities. Checking gender and race separately might look fine, but "Black women" as a group could be getting significantly worse predictions:

```python
from fairlens import compute_intersectional_metrics

report = compute_intersectional_metrics(
    y_true, y_pred,
    {'gender': gender_arr, 'race': race_arr}
)
print(report)
# Shows metrics for all cross-groups (M_White, F_Black, etc.)
# Plus per-attribute DP ratios for comparison
```

### Bootstrap Confidence Intervals

Point estimates of fairness metrics can be misleading on small datasets. Wrap any metric with bootstrap resampling to get a confidence interval:

```python
from fairlens import bootstrap_metric, demographic_parity_ratio

ci = bootstrap_metric(
    demographic_parity_ratio,
    y_pred, protected,
    n_bootstrap=1000,
    random_state=42,
)
print(f"DP Ratio: {ci.estimate:.3f}, 95% CI: [{ci.lower:.3f}, {ci.upper:.3f}]")
print(f"Statistically unfair: {ci.upper < 0.8}")
```

### Multi-class Fairness

For classification beyond binary (e.g., job recommendation with multiple roles), fairness is computed per class via one-vs-rest decomposition:

```python
from fairlens import compute_multiclass_fairness

report = compute_multiclass_fairness(y_true, y_pred, protected)
print(report.worst_class)       # Which class has the worst DP ratio
print(report.macro_avg_dp_ratio) # Average across all classes
```

## Fairness Thresholds

The commonly used thresholds (following the "80% rule" from disparate impact law):

| Metric | Threshold | What it means |
|--------|-----------|---------------|
| Demographic Parity Ratio | >= 0.8 | Positive rates within 20% of each other |
| Equalized Odds Ratio | >= 0.8 | TPR/FPR ratios within 20% |
| Demographic Parity Diff | <= 0.1 | Absolute difference in rates < 10% |

These aren't magic numbers - they're starting points. What counts as "fair enough" depends heavily on context.

## Report Generation

```python
from fairlens.audit import generate_html_report, generate_markdown_report

result = fl.audit_model(model, X_test, y_test, protected)

generate_html_report(result, "fairness_report.html")
generate_markdown_report(result, "fairness_report.md")
```

## Bias Mitigation

### Threshold Optimizer (post-processing)

Finds group-specific classification thresholds to equalize positive prediction rates:

```python
from fairlens import ThresholdOptimizer

opt = ThresholdOptimizer(objective='demographic_parity')
opt.fit(y_true, y_prob, protected)
fair_preds = opt.predict(y_prob, protected)

print(opt.get_results())
# Shows per-group thresholds and DP ratio improvement
```

### Reweighter (pre-processing)

Computes sample weights so the weighted label distribution is independent of the protected attribute. Use these weights when retraining:

```python
from fairlens import Reweighter

rw = Reweighter()
weights = rw.fit_transform(y_train, protected_train)
model.fit(X_train, y_train, sample_weight=weights)
```

### Mitigation Suggestions

The library can also suggest strategies based on what issues it finds:

```python
from fairlens.mitigation import print_suggestions

print_suggestions(result.fairness_issues, include_code=True)
```

## Comparison with Other Tools

| Tool | Good for | Less good for |
|------|----------|---------------|
| AIF360 | Comprehensive research, many algorithms | Quick checks, simple use cases |
| Fairlearn | Integration with sklearn | Non-Microsoft ecosystems |
| What-If Tool | Visual exploration | Non-TensorFlow models |
| FairLens | Quick audits, simple API, built-in mitigation | Deep research, large-scale production pipelines |

If you need cutting-edge research algorithms or large-scale production fairness pipelines, AIF360 or Fairlearn are probably better choices. FairLens is more about making fairness checks and basic mitigation accessible without a steep learning curve.

## Limitations

- Individual fairness metrics are computationally expensive on large datasets
- Mitigation algorithms (threshold optimizer, reweighter) cover common cases but aren't as extensive as AIF360
- Bootstrap confidence intervals add computation time proportional to `n_bootstrap`
- The built-in synthetic datasets are approximations; use `fetch_*` for real data when possible

## References

Papers that informed this:
- Hardt et al. 2016 - "Equality of Opportunity in Supervised Learning"
- Barocas, Hardt, Narayanan - "Fairness and Machine Learning" (free online textbook, highly recommend)
- The ProPublica COMPAS investigation (2016)

Related tools:
- [IBM AI Fairness 360](https://github.com/Trusted-AI/AIF360)
- [Fairlearn](https://github.com/fairlearn/fairlearn)

## License

MIT
