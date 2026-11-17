# Machine Learning-Based Classification of Agricultural Market Price Decline Risk

**AgroMaster** | Machine Learning Project
Department of computer Engineering, University of Ruhuna

| Ethipola K.J.R.R.W.M.R.E.M.W.P.T.B.
| Geeganage S.P.
| Nawodya T.H.Y. 
| Chamuditha K.D.T. |

## Overview

This project classifies the price-decline risk of a commodity in an Indian wholesale market (mandi) as **Low**, **Medium** or **High**, seven calendar days ahead. It uses only price history, location and calendar information from the public AGMARKNET daily mandi price data.

Five supervised algorithms are tuned and compared against two simple baselines under a strictly chronological evaluation: Logistic Regression, Gaussian Naive Bayes, Decision Tree, Random Forest and XGBoost.

## Dataset

- **Source:** [Daily Market Prices of Commodity India (2001–2026)](https://www.kaggle.com/datasets/khandelwalmanas/daily-commodity-prices-india), Kaggle, compiled from AGMARKNET, Government of India.
- **Source size:** 75,984,017 records, 2001-01-10 to 2026-04-21.
- **Modelling subset:** 7,919,229 records for five perishable vegetables (Tomato, Onion, Potato, Brinjal, Green Chilli) in 2,605 series, 787 markets and 25 states.
- **Selection rule:** a series is kept if it has at least 1,500 reporting days and a span of at least 8 years up to 2023-12-31.

The data files are not stored in this repository. Notebook 01 downloads the dataset and builds the subset. See `data/README.md`.

## Method

| Step | Summary |
|---|---|
| Cleaning | Removes zero prices, inconsistent prices and suspected entry errors. 7,715,788 rows kept (97.43%). |
| Features | 18 features from the proposal plus 7 relative features (25 in total), all computed from information available on the prediction date. |
| Target | Ratio of the modal price at t+7 to the mean modal price of the previous 90 days. Per commodity, the lowest 10% is High, the next 20% is Medium, the rest is Low. |
| Split | Development period up to 2023-12-31, final test period 2024-01-01 to 2025-10-30. No random shuffling. |
| Validation | Five expanding-window folds inside the development period. Thresholds, scalers, encoders and class weights are fitted on training rows only. |
| Tuning | Randomised search, selected by mean validation macro F1. |
| Interpretation | XGBoost gain importance, SHAP values (TreeSHAP) and error analysis. |

## Notebooks

Run the notebooks in order. Each one reads the output of the previous one.

| Notebook | Purpose |
|---|---|
| `01_data_loading.ipynb` | Download the dataset, measure coverage, build the modelling subset |
| `02_eda.ipynb` | Exploratory data analysis |
| `03_cleaning.ipynb` | Cleaning rules with a row-count log |
| `04_features_and_target.ipynb` | 18 features, target ratio, leakage check |
| `05_split_labels_baselines.ipynb` | Chronological split, folds, risk labels, two baselines |
| `06_models_tuning.ipynb` | Experiment A: five models on the 18 proposal features |
| `07_models_extended_features.ipynb` | Experiment B: five models on 25 features |
| `08_final_test_evaluation.ipynb` | Final fit and a single evaluation on the test period |
| `09_interpretation.ipynb` | Feature importance, SHAP and error analysis |

## How to run

1. Open a notebook in [Google Colab](https://colab.research.google.com).
2. Run the first cell and allow access to Google Drive. Outputs are written to `MyDrive/agromaster`.
3. Run notebooks 01 to 09 in order. Notebook 01 downloads the dataset (about 1.4 GB) with `kagglehub`.
4. In notebooks 06 and 07, run the cells one at a time. Tuning takes roughly an hour per notebook on a free Colab session.

Required packages are listed in `requirements.txt`.

## Results

Final test period, 2024-01 to 2025-10 (613,070 prediction rows):

| Model | Accuracy | Macro F1 | High-risk precision | High-risk recall | High-risk F1 |
|---|---|---|---|---|---|
| Risk persistence (baseline) | 0.844 | 0.739 | 0.726 | 0.595 | 0.654 |
| **XGBoost (selected)** | 0.803 | 0.722 | 0.618 | 0.728 | 0.668 |
| Random Forest | 0.798 | 0.713 | 0.610 | 0.718 | 0.660 |
| Decision Tree | 0.794 | 0.704 | 0.573 | 0.738 | 0.645 |
| Logistic Regression | 0.770 | 0.684 | 0.537 | 0.785 | 0.638 |
| Gaussian Naive Bayes | 0.657 | 0.570 | 0.430 | 0.618 | 0.507 |
| Majority class (baseline) | 0.715 | 0.278 | 0.000 | 0.000 | 0.000 |

Key findings:

- XGBoost detects 72.8% of true High-risk cases, against 59.5% for the risk-persistence baseline, and reduces High-risk cases predicted as Low from 3,928 to 1,670.
- This comes with more false alarms. On macro F1 the baseline remains slightly ahead (0.739 against 0.722).
- The seven relative features raised the mean validation macro F1 of every model by 0.14 to 0.21. With the 18 proposal features alone, the best model reached only 0.564.
- XGBoost scored 0.721 macro F1 on validation and 0.722 on the test period, so it generalises to newer data.

![Confusion matrices](figures/08_confusion_matrices.png)

## Limitations

- The selected model does not beat the persistence baseline on macro F1.
- The model mostly recognises a price that has already fallen and stays low. It does not anticipate sudden crashes from a normal price level.
- The dataset has no arrival quantities, so the label is a price-based proxy and does not measure oversupply directly.
- Hyperparameters were tuned on a 400,000-row sample of each training fold.
- Results apply to five vegetables and to series with long reporting histories.

The full discussion is in the final report.

## Repository structure

```
agromaster-ml/
├── README.md
├── .gitignore
├── requirements.txt
├── notebooks/        # the nine pipeline notebooks
├── results/
│   ├── config/             # subset, feature, split and best-parameter files
│   ├── data_preparation/   # coverage table and cleaning log
│   ├── validation/         # cross-validation results and thresholds
│   ├── test/               # final test results
│   └── interpretation/     # SHAP summary
├── figures/          # figures produced by the notebooks
├── models/           # final XGBoost model and its preprocessor
├── docs/             # project proposal and final report
└── data/             # README only; data files are not stored here
```

## Tools

Python, pandas, NumPy, PyArrow, scikit-learn, XGBoost, Matplotlib, Google Colab.

## Data licence

The dataset is published on Kaggle under the Government Open Data License – India (GODL-India). This repository does not redistribute the data.
