# Human Activity Recognition: Generalization to Unseen Subjects

**Can a smartphone activity classifier recognize a new user?** This case study
tests that question with subject-aware model selection, a nested stability study,
per-person error analysis and a deliberately separate random-row evaluation audit.

The project uses Python, pandas and scikit-learn on the 561 published UCI HAR
features. It is an offline research case study, with an executed notebook and
reusable experiment code.

<!-- RESULTS_START -->
## Results from the executed study

| Experiment | Training people | Accuracy | Macro-F1 |
|---|---:|---:|---:|
| Fixed benchmark: LDA + Euclidean KNN, k=21 | 18 | 92.00% | 0.9250 |
| Expanded study: LDA + Manhattan KNN, k=21 | 24 | 92.34% | 0.9281 |

Both rows evaluate the same six held-out people. The expanded study changes
selection **and** training size, so the small score difference does not isolate
an algorithm effect. The best two development candidates differ by just
0.000158 mean Macro-F1; this does not establish a robust preference for
one distance or k setting.

Across five nested development-only outer holdouts, the selection procedure has
mean Macro-F1 **0.9594**, sample SD **0.0215**,
and range **0.9385–0.9898**. These overlapping
splits are descriptive, not independent replications. Their higher mean than the
final benchmark score illustrates sensitivity to the people tested; it does not
guarantee that more training people will increase a particular test score.

![Fixed baseline split audit](reports/figures/split_audit.png)

With the same standardized k=5 Euclidean baseline, random-row Macro-F1 is
**0.9571** with **30 shared people**, versus
**0.8230** with **zero shared people** under subject separation.
The difference is not a causal estimate of identity leakage alone: window overlap,
training size and test composition also change.

The selected project model's person-level Macro-F1 ranges from
**0.8501 to 1.0000**. Sitting/Standing account for
**137 of 159 errors (86.2%)**;
their recalls are **82.4%** and **81.2%**.
This concentration matters for posture-related features even when the aggregate
recognition score looks strong.

![Test error counts and per-activity fractions](reports/figures/test_confusion.png)

The evidence supports a further data-collection pilot, not a production-readiness
claim. The final holdout is a reused public benchmark whose earlier results were
already inspected; prospective confirmation needs genuinely new people.
<!-- RESULTS_END -->

## Read the case study

Open [`human_activity_recognition.ipynb`](human_activity_recognition.ipynb).
It develops the product question, audits the data, explains design decisions,
runs the complete study, visualizes results and states what the findings support.
The saved notebook contains real executed outputs. Tables and predictions are
also available under [`reports/`](reports/).

## Why this is a useful evaluation problem

Sensor windows from the same person are not independent users. In this dataset,
neighboring windows also overlap by 50%. A random-row split can place highly
related measurements and the same people on both sides of an evaluation.

That protocol answers a different question from onboarding a new user. This
study keeps subject IDs out of the feature matrix, separates people at every
selection level and reports both pooled and person-level performance.

## Dataset and provenance

- Source: [UCI Human Activity Recognition Using Smartphones](https://doi.org/10.24432/C54S4K),
  Reyes-Ortiz, Anguita, Ghio, Oneto and Parra (2013).
- 10,299 windows, 30 people aged 19–48, six activities, 561 engineered features.
- Waist-mounted Samsung Galaxy S II; accelerometer and gyroscope at 50 Hz;
  2.56-second windows with 50% overlap.
- Inputs follow the exact positional order in the original `features.txt`.
  Subject IDs are grouping metadata, never predictors.
- The official training rows are followed by the official test rows; custom
  subject splits are then defined. These scores are not official-split benchmarks.
- [`data_manifest.json`](data_manifest.json) pins SHA-256 hashes of all required
  uncompressed dataset members. A download that changes bytes fails validation.
- Repeated original feature names are kept as metadata; model inputs use positions.

The raw sensor pipeline is outside scope. This project starts from published
features and does not claim to reproduce their extraction from live sensor data.

## Evaluation and model selection

| Stage | Training and validation | Role |
|---|---|---|
| Fixed benchmark | 18 training / 6 validation / 6 test people, seed 42 | Scaling, Full/PCA/LDA and all 24 KNN settings |
| Nested stability | Five 18/6 outer splits within the 24-person development pool; three 12/6 inner splits each | Evaluate the selection procedure without using each outer test to select its model |
| Final development search | Eight 18/6 subject splits within development | Choose the candidate with highest mean Macro-F1 |
| Final refit and evaluation | Fit all 24 development people; evaluate six benchmark people | Assess the frozen final choice |
| Random-row audit | Stratified approximately 60/20/20 rows; middle 20% unused | Compare a fixed standardized k=5 KNN under two protocols |

**32 candidate settings:** Full/PCA95/LDA × Euclidean/Manhattan × k in
{1, 5, 11, 21}; published-feature Euclidean k=5 KNN; majority-class baseline;
standardized Logistic Regression and Linear SVM with C in {0.1, 1, 10}.

PCA uses full SVD, at least 95% training variance, and no whitening. LDA uses SVD
and all five permitted discriminant components. Every transformation is fitted
on the current training subset. Component scores are not rescaled.

The primary metric is Macro-F1 over labels 1–6 (`zero_division=0`), accompanied by
accuracy, class precision/recall/F1, a confusion matrix and per-person Macro-F1.
Exact candidate-score ties follow the recorded candidate order: the 24 KNNs
(Full/PCA/LDA, Euclidean/Manhattan, ascending k), then raw KNN, majority baseline,
Logistic Regression and Linear SVM (ascending C). Uniform class-vote ties prefer
the smaller activity ID; equal neighbor-distance boundaries follow scikit-learn
with preserved training order.

### Interpreting uncertainty correctly

Earlier exploratory work already reported results for the same six-person
benchmark holdout. It is a **reused public benchmark, not a prospectively untouched
test**. The development-only nested splits provide an additional check, but they
cannot undo prior exposure to the dataset.

The five nested outer splits overlap. Their sample SD measures sensitivity to
these splits, not uncertainty from independent future datasets. The eight final
development splits select the winner, so its development average is optimistic
as an evaluation. Nested models train on 18 people; the final model trains on 24.

The subject-cluster bootstrap resamples whole held-out people, not individual
windows. Its 95% percentile interval is descriptive and fragile with just six
people; it excludes training, selection and device-shift uncertainty.

## Reproduce the project

Use **Python 3.11** from the repository root. The direct dependency versions are
pinned to those used for the saved study; [`reports/run_metadata.json`](reports/run_metadata.json)
records the actual platform and package versions. Minor numeric differences across
BLAS implementations or architectures are possible.

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/run_experiments.py
python -m pytest -q
```

On Windows, activate with `.venv\Scripts\activate`.

The first run downloads the official UCI archive (about 58 MB), verifies member
hashes and caches only required files under `data/`. Later runs work offline.
The local delivered folder includes a verified cache; the GitHub-ready ZIP omits
that cache. Network access is needed when the cache is absent. TLS certificates
are verified using `certifi`; certificate verification is never disabled.

To execute and save the notebook using the same Python environment:

```bash
python scripts/execute_notebook.py
```

Or open `jupyter lab`, choose this environment and use **Restart Kernel and Run All**.
`RUN_STUDY = True` is the notebook default and recomputes the experiments; change
it to `False` only to review existing exports, whose source/data hashes are checked.
The notebook regenerates figures and narrative tables. The standalone experiment
runner regenerates the numerical study without requiring Jupyter.

Ordinary CI runs synthetic-data tests and notebook validation. The manual
`workflow_dispatch` job downloads the dataset and runs the full numerical study.
No claim is made that remote GitHub Actions has already run for this repository.

## What is saved

```text
human_activity_recognition.ipynb  Executed, self-contained case-study narrative
har/data.py                     Download, checksum validation, aligned loading
har/modeling.py                 Pipelines, exact neighbor search, grouped selection
har/experiment.py               Full study, frozen selection, exported evidence
scripts/                        Experiment, notebook execution and inference commands
tests/                          Methodology and full-data consistency checks
data_manifest.json              Expected source member hashes
reports/                        Scores, predictions, split manifests and figures
models/model_card.json          Intended use, settings, provenance and limits
requirements.txt                Tested direct dependency versions
.github/workflows/checks.yml     Automated unit checks and optional full study
```

Key audit files:

- `experiment_plan.json`: candidate grid and split seeds, written before fitting.
- `frozen_selection.json`: final choice and training rows, saved before test prediction.
- `split_manifest.json`: exact global row positions at every grouping level.
- `nested_inner_scores.csv`, `development_cv.csv`: all 32 scores for every search split.
- `nested_predictions.csv`, `test_predictions.csv`, `row_audit_predictions.csv`:
  per-window evidence for recomputing evaluations.
- `run_metadata.json`: environment, run time, and dataset/plan/source hashes.

The data cache, temporary files and fitted `.joblib` artifact are ignored by git.
Regenerate the fitted artifact locally with either execution command. Load only
trusted joblib/pickle artifacts.

## Inference example

After running the study, pass a numeric CSV with no header and exactly 561
columns in UCI `features.txt` positional order:

```bash
python scripts/predict.py feature_windows.csv predicted_activities.csv
```

The output contains activity IDs and names. This interface takes already
engineered feature vectors, not raw accelerometer readings. The recorded batch
timing excludes signal processing, acquisition and mobile power usage.

## Practical decision and next evidence

Treat the model as a candidate for a small **data-collection pilot** for offline
activity summaries. The notebook includes illustrative costs for Sitting/Standing
errors at weights 1, 5 and 20; these are sensitivity scenarios, not monetary losses
or an optimized business policy. Choose actual error costs with stakeholders and
use development data for any future cost-aware selection.

Before a real launch, test genuinely new people and sessions across days, devices
and phone placements. Assess active-minute error and transition stability alongside
per-person/class performance, latency, battery usage and user feedback. The
available dataset cannot justify clinical use, fairness guarantees or uniform
performance for all users.

## Limitations

Small controlled cohort, overlapping windows, one device/placement, six activities,
reused public holdout, and no prospective field evaluation. Demographics needed for
subgroup fairness analysis are not present in the supplied grouping files. Temporal
smoothing, calibration, abstention and production monitoring remain future work.

## References and license

- [Dataset and original study](https://doi.org/10.24432/C54S4K).
- [Scikit-learn 1.5: grouped evaluation and preprocessing](https://scikit-learn.org/1.5/modules/cross_validation.html).
- [LDA](https://scikit-learn.org/1.5/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html),
  [KNN](https://scikit-learn.org/1.5/modules/generated/sklearn.neighbors.KNeighborsClassifier.html).

Project source and original documentation use the [MIT license](LICENSE).
Dataset terms are separate. The current UCI page lists CC BY 4.0, while the
original archive README prohibits commercial use; see [data notes](data/README.md).
This educational portfolio study does not resolve that discrepancy.
