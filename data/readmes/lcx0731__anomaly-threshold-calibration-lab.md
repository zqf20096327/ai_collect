# Anomaly Threshold Calibration Lab

A reproducible Monte Carlo audit of a deployment failure mode in unsupervised anomaly
detection: calibrating a high-score threshold on a dataset that already contains the
events the detector is supposed to catch.

Two models are trained on the same trusted inlier sample:

- **Robust Mahalanobis distance** using a minimum covariance determinant estimate.
- **Isolation Forest** using 120 trees and a fixed random seed.

The models never see labels during fitting or calibration. A threshold is set to the
empirical 99th percentile of calibration scores, aiming for a 1% inlier false-positive
rate. Calibration contamination is then varied from 0% to 5% while model fitting and
the labeled test distribution remain fixed within each replication.

## Synthetic design

- Four correlated Gaussian features define normal behavior.
- Anomalies have random directions and Mahalanobis radii between 3.2 and 6.0.
- Each default replication uses 1,500 clean training rows, 1,500 calibration rows,
  and a test set with 3,000 inliers plus 300 anomalies.
- Sixty paired replications separate Monte Carlo variation from method differences.
- Calibration contamination levels are 0%, 1%, 3%, and 5%.

All data are deterministic synthetic draws. No external or private data are used.

## Reproduce

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[test]"
pytest -W error
python -m anomaly_threshold_calibration_lab --output-dir artifacts
```

## Results

The clean calibration set placed both models close to the 1% test inlier FPR target.
The table contrasts that operating point with 5% calibration contamination:

| Model | Clean FPR | Clean recall | 5% threshold ratio | 5% FPR | 5% recall | AUROC |
|---|---:|---:|---:|---:|---:|---:|
| Robust Mahalanobis | 0.00985 | 0.834 | 2.198 | 0.000006 | 0.203 | 0.9956 |
| Isolation Forest | 0.01022 | 0.564 | 1.111 | 0.001028 | 0.185 | 0.9813 |

At 3% contamination, recall had already fallen to 0.313 for Robust Mahalanobis and
0.258 for Isolation Forest. At 5%, both detected only about one fifth of anomalies.
The lower FPR and higher precision at contaminated operating points are therefore not
an unqualified improvement: the threshold became over-conservative and missed many
events.

AUROC did not change across calibration conditions because the fitted score ranking
and test set were fixed within each replication. This is the practical lesson of the
audit: a strong ranking metric does not validate the deployed threshold. Threshold
ratios are meaningful only within each model because their score scales differ.

![Recall sensitivity to calibration contamination](artifacts/recall_vs_contamination.png)

## Outputs

- `artifacts/replicate_metrics.csv`: paired thresholds and test metrics.
- `artifacts/summary_metrics.csv`: means and Monte Carlo standard errors.
- `artifacts/run_summary.json`: machine-readable design and operating points.
- `artifacts/fpr_vs_contamination.png`: realized test inlier false-positive rate.
- `artifacts/recall_vs_contamination.png`: anomaly recall sensitivity.
- `artifacts/threshold_inflation.png`: threshold relative to clean calibration.

## Repository structure

```text
src/anomaly_threshold_calibration_lab/
  simulation.py   # correlated inliers, radial anomalies, labeled splits
  scoring.py      # robust distance and Isolation Forest scorers
  calibration.py  # empirical quantile and operating metrics
  evaluation.py   # paired Monte Carlo audit and summaries
  reporting.py    # figures with Monte Carlo error bars
tests/             # data, threshold, metric, and E2E tests
artifacts/         # reproducible outputs from the default run
```

## Limitations

- Synthetic radial anomalies favor detectors that rank distance from the inlier cloud;
  local or contextual anomalies may behave differently.
- The calibration and test anomalies share a generator. Distribution shift could make
  contamination effects better or worse.
- The target is a marginal false-positive rate, not a guarantee for every subgroup or
  time window.
- Anomaly prevalence is known only for evaluation. Real unlabeled calibration data do
  not reveal their contamination rate directly.
- The study audits point thresholds, not online alert budgets or delayed labels.

## Responsible use

This is an educational portfolio project. Detection thresholds should be validated
against the costs, review capacity, and changing distributions of a real application.
