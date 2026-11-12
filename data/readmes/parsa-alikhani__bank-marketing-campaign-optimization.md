# Bank Marketing Campaign Optimization with Cost-Sensitive Machine Learning

**Cost-sensitive decisions under temporal distribution shift.**

This project evaluates term-deposit marketing decisions using 45,211 historical records from a Portuguese banking institution. The objective is to quantify the later-period cost, predictive performance and operational stability of a model and probability threshold selected using business costs, and to compare the resulting policy with default classification and simple business rules.

Optimization refers to selecting the model and probability threshold under the stated decision-cost objective.

The complete analysis is contained in **[bank_marketing_optimization.ipynb](bank_marketing_optimization.ipynb)**. All data-loading, preprocessing, modeling, evaluation and plotting code is defined inside the notebook. No separate Python source folder or project package is required.

## Repository contents

```text
bank-marketing-campaign-optimization/
├── bank_marketing_optimization.ipynb
└── README.md
```

The notebook is saved with its computed tables, charts and interpretations, so the study can be read directly on GitHub without running it.

## Main findings

The selected model is Logistic Regression with `C=0.1`, using a validation-selected probability threshold of approximately **0.09658**. The frozen policy reduces final-period cost by **17.80%** compared with the same model at threshold 0.5. It does not outperform two simple alternatives under the stated loss matrix.

| Final-period policy | Precision | Recall | F1 | Cost per 1,000 records |
| --- | ---: | ---: | ---: | ---: |
| Model at threshold 0.5 | 0.4595 | 0.0060 | 0.0118 | 7,859.67 |
| Model at frozen cost threshold | 0.4936 | 0.2286 | 0.3125 | 6,460.80 |
| Always predict no | 0.0000 | 0.0000 | 0.0000 | 7,895.61 |
| Always predict yes | 0.3158 | 1.0000 | 0.4800 | 3,420.88 |
| Previous-campaign success rule | 0.6949 | 0.3165 | 0.4349 | 5,615.95 |

The positive rate increases from **5.04%** in training to **11.79%** in validation and **31.58%** in the final period. Improving a threshold relative to 0.5 therefore does not establish operational superiority over simple policies. Universal action is an important comparison under the primary loss, but requires action on every customer and may violate a real capacity limit.

## Analysis

- Chronological 60/20/20 evaluation using the original UCI file order, without shuffling or final-model refitting on validation.
- Call-start feature availability, excluding completed-call `duration` from the operational model.
- Training-only imputation and scaling, explicit previous-contact handling, and one-hot encoding with unseen-category support.
- Eight predeclared candidates: Logistic Regression with C=0.1/1/10, Decision Trees with depth=3/6/12, Random Forest and Histogram Gradient Boosting.
- Exact model/threshold selection using `5 FP + 25 FN`, with explicit tie rules and comparison against an F1-selected threshold.
- Always-no, always-yes and previous-success baselines.
- Cost-ratio sensitivity, action-capacity budgets, prevalence scenarios, earlier chronological stability checks and probability-reliability diagnostics.
- Permutation importance, a separate duration audit, descriptive subgroup errors and paired moving-block bootstrap uncertainty.
- Executable checks of threshold counting, capacity ties, final-cost arithmetic and saved-model predictions.

## Run the notebook

1. Download the notebook or open it in a Python notebook environment such as Jupyter or VS Code.
2. Use **Python 3.11 or 3.12**. Install the packages listed below in the notebook's active environment. The notebook also includes a commented one-time installation cell.
3. Restart the kernel and run all cells from top to bottom.

```bash
python -m pip install numpy==2.3.5 pandas==2.2.3 scipy==1.16.3 scikit-learn==1.8.0 matplotlib==3.10.8 seaborn==0.13.2 joblib==1.5.2 threadpoolctl==3.8.0
```

The host notebook application supplies IPython and the Python kernel. Recorded results were produced with Python 3.11. The notebook prints the installed analysis-library versions. Small floating-point differences across platforms may affect the final digits of the selected threshold.

**No data file, model file or source directory needs to be present before execution.** The first run downloads the exact older `bank-full.csv` from UCI and verifies the decompressed CSV's SHA-256 checksum. Internet is needed for that first download and for installing missing libraries. Later runs can use the verified local cache.

During execution, an `artifacts/` folder is generated beside the running notebook. It contains the data cache, CSV tables, figures, environment metadata and frozen policy/model files. These are local execution outputs, not additional repository requirements. Only the notebook and this README need to be uploaded to GitHub. Save the notebook after running it to retain its visible outputs.

The optional saved model contains a feature-transformer class defined inside the notebook; reloading it in another session requires executing that definition first. The notebook's scoring demonstration handles this within the normal top-to-bottom execution.

## Execution verification

The final notebook was rerun from a clean working directory containing only the notebook and this README on 2026-11-09. The run downloaded the dataset from UCI, verified its checksum, trained all eight candidate models and completed all 30 code cells without errors. The final policy metrics match the main findings above. The notebook's threshold, capacity, cost-arithmetic and reloaded-prediction checks also passed. No existing data cache or pre-trained model was supplied to that run.

## Method and interpretation

The decision time is the start of the recorded call. Client information, previous-campaign history, planned contact details and the current attempt number are assumed available. Completed duration is excluded. `pdays=-1` represents no prior contact; an indicator preserves that distinction while training-only median imputation handles the missing interval. Categorical `unknown` remains an explicit level.

The loss is **5 FP + 25 FN**, in hypothetical units, with zero loss for correct decisions. It is not bank profit, a measured per-call charge or a causal estimate of campaign value. The primary objective has no capacity constraint; constrained alternatives are analyzed separately. Historical outcomes from contacted customers do not identify the incremental effect of contacting them.

Model and threshold are selected on validation and frozen before final-label evaluation. The retained model is not refitted on validation. The final holdout has been examined in this study; future modeling changes require a new evaluation period.

The dataset lacks customer IDs and complete timestamps. Repeated-client overlap cannot be ruled out, ordered blocks are not reconstructed calendar months, and subgroup summaries are not a fairness certification. Bootstrap intervals are conditional on the fitted policy and observed period, and do not guarantee future performance.

## Dataset and references

Moro, S., Rita, P., & Cortez, P. (2014). *Bank Marketing* [Dataset]. UCI Machine Learning Repository. [DOI: 10.24432/C5K306](https://doi.org/10.24432/C5K306).

- [UCI Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing): use the older `bank-full.csv` inside `bank.zip`, not `bank-additional-full.csv`.
- Dataset license: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Original CSV bytes are retained in a compressed cache; features, predictions and figures are derived analysis outputs. The dataset creators do not endorse this project.
- [scikit-learn threshold tuning](https://scikit-learn.org/stable/modules/classification_threshold.html), [probability calibration](https://scikit-learn.org/stable/modules/calibration.html), and [common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html).

<details>
<summary>Code license: MIT</summary>

Copyright (c) 2026 Bank Marketing Campaign Optimization contributors

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

The UCI dataset remains separately licensed under CC BY 4.0.

</details>
