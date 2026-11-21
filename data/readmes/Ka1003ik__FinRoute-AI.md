# FinRoute AI

**CODVEDA Level 2 – Task 2: Natural Language Processing (NLP) – Text Classification**

FinRoute AI is a script-based NLP classification project that predicts the financial product category associated with a consumer complaint narrative. It uses public Consumer Financial Protection Bureau (CFPB) complaint data and compares classical machine-learning models with a fine-tuned DistilBERT classifier.

The project scope for this task is **model development and evaluation**. A web interface, dashboard, API, or deployment is not part of the completed task deliverable.

## 1. Objective

Given a consumer complaint narrative, predict one of 11 CFPB `Product` categories. The intended use is to support complaint triage and routing; predictions should be treated as decision support rather than as an automatic final decision.

## 2. Dataset and split methodology

- Source: CFPB public Consumer Complaint Database export used in this project (`CCDB_Export_21_August_2026.csv`).
- Modeling dataset: **121,114 complaint records** across **11 Product categories**.
- The modeling data contains **108,902 canonical narrative groups**.
- The V3 partitions were created with `StratifiedGroupKFold(n_splits=10, shuffle=True, random_state=42)`: fold 0 for validation, fold 1 for test, and folds 2–9 for training.
- Partition sizes: **96,890 training**, **12,112 validation**, and **12,112 test** records.
- Similarity components were defined using word-trigram shingle hashes with Jaccard similarity of 1.00. This is the project’s grouping criterion; it should not be described as literal character-level equality.
- An independent saved-split audit checked source-row conservation, Product distributions, component and narrative separation, and exact complete-row overlap. The recorded cross-partition overlap counts were zero.
- The test split was kept out of training and validation-based model selection. It was evaluated once after the candidate model was selected.

The split files are expected at:

```text
data/processed/splits_v3/train.csv
data/processed/splits_v3/validation.csv
data/processed/splits_v3/test.csv
```

## 3. Text preprocessing and representation

The shared text-cleaning pipeline normalizes Unicode, unescapes HTML entities, removes standalone repeated-`x` redaction markers, collapses whitespace, and lowercases text. It preserves numbers, punctuation, negation, and financial terminology.

The classical-model pipeline uses word-level TF-IDF with:

- `max_features=300000`
- `min_df=3`
- `ngram_range=(1, 2)`
- the vectorizer fitted on training narratives only

The DistilBERT pipeline uses the pinned `distilbert/distilbert-base-uncased` tokenizer revision and a maximum sequence length of 512 tokens.

**Preprocessing decisions:** Stopword removal, stemming, and lemmatization were not applied as separate operations in the completed experiments. This is disclosed rather than treated as completed work. The original narrative wording, including negations and financial expressions, was retained for contextual classification. These alternatives were not experimentally compared in this project.

## 4. Models compared

Seven classical TF-IDF classifiers were trained and compared:

| Classical model | Validation accuracy | Validation macro-F1 |
|---|---:|---:|
| Multinomial Naive Bayes | 64.96% | 32.32% |
| Complement Naive Bayes | 77.04% | 60.45% |
| Logistic Regression (one-vs-rest) | 84.28% | **77.24%** |
| LinearSVC | **84.32%** | 76.80% |
| SGDClassifier | 84.11% | 76.99% |
| Random Forest | 74.88% | 66.30% |
| XGBoost | 77.27% | 68.44% |

Logistic Regression was the strongest classical candidate by validation macro-F1. DistilBERT was also trained as a contextual text-classification model and selected as the final candidate based on its higher validation macro-F1.

## 5. DistilBERT training configuration

- Base model: `distilbert/distilbert-base-uncased`
- Pinned revision: `12040accade4e8a0f71eabdb258fecc2e7e948be`
- Number of classes: 11
- Maximum token length: 512
- Training epochs requested: 3
- Learning rate: `2e-5`
- Weight decay: `0.01`
- Per-device training batch size: 6
- Gradient accumulation steps: 2 (effective batch size 12)
- Evaluation batch size: 8
- Balanced cross-entropy class weights calculated from training labels
- Validation macro-F1 used for checkpoint selection
- Random seed: 42

The saved fine-tuned model and tokenizer are stored at:

```text
models/transformer/distilbert_product_classifier_v3/
```

## 6. Validation results and final model selection

The selected DistilBERT model achieved the following validation results:

| Metric | Validation result |
|---|---:|
| Accuracy | 85.39% |
| Balanced accuracy | 78.89% |
| Macro precision | 78.66% |
| Macro recall | 78.89% |
| Macro-F1 | **78.66%** |
| Weighted-F1 | 85.41% |
| Top-2 accuracy | 94.64% |

Validation macro-F1 was higher than the best classical baseline (Logistic Regression, 77.24%), so DistilBERT was selected for the final test evaluation.

## 7. Final held-out test results

The selected saved DistilBERT model was evaluated on the held-out V3 test partition. The evaluation script loaded the saved fine-tuned model locally; it did not retrain or fine-tune the model. The test CSV SHA-256 was verified before and after evaluation.

| Metric | Final test result |
|---|---:|
| Test records | 12,112 |
| Accuracy | **85.58%** |
| Balanced accuracy | 79.63% |
| Macro precision | 80.06% |
| Macro recall | 79.63% |
| Macro-F1 | **79.57%** |
| Weighted precision | 85.77% |
| Weighted recall | 85.58% |
| Weighted-F1 | 85.62% |
| Top-2 accuracy | 94.30% |

### Per-category test F1

| Product category | F1-score | Support |
|---|---:|---:|
| Checking or savings account | 82.02% | 2,133 |
| Credit card | 84.36% | 2,039 |
| Credit reporting or other personal consumer reports | 81.54% | 486 |
| Debt collection | 92.34% | 4,010 |
| Debt or credit management | 59.02% | 110 |
| Money transfer, virtual currency, or money service | 74.48% | 981 |
| Mortgage | 94.01% | 777 |
| Payday loan, title loan, personal loan, or advance loan | 71.54% | 434 |
| Prepaid card | 58.22% | 147 |
| Student loan | 91.29% | 405 |
| Vehicle loan or lease | 86.44% | 590 |

The most challenging categories by test F1 were Prepaid card and Debt or credit management. Their relatively small test supports should be considered when interpreting these class-level results. The confusion matrix and class report are saved with the test evaluation artifacts.

## 8. Key output files

```text
outputs/experiments/v3/classical/       # Classical-model experiment results
outputs/experiments/v3/distilbert/
    validation.json                     # DistilBERT validation metrics
    validation_confusion.csv            # Validation confusion matrix
    test.json                           # Final held-out test report
    test_confusion.csv                  # Final held-out test confusion matrix
outputs/leakage_audit/                  # Independent split-audit reports
```

Important project scripts include:

```text
scripts/create_group_splits_v3.py
scripts/audit_saved_group_splits_v3_hashed.py
scripts/train_classical_v3.py
scripts/train_distilbert_v3.py
scripts/verify_distilbert_v3.py
scripts/evaluate_distilbert_v3_test.py
```

Reusable source modules are under `src/`, including text preprocessing, TF-IDF vectorization, DistilBERT tokenization/model loading, and evaluation metrics.

## 9. Environment and reproducibility

The completed experiments used Python 3.14.10, PyTorch 2.10.0+cu128, Transformers 5.22.2, CUDA 12.8, and an NVIDIA RTX 4050 Laptop GPU. The project includes `requirements.txt` and `requirements-lock.txt` for dependency records.

Activate the project environment in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

The final test evaluation can be reproduced in a separate controlled copy of the project after placing the required dataset splits and saved model artifacts in their expected paths. The evaluation script is:

```powershell
python .\scripts\evaluate_distilbert_v3_test.py
```

The script verifies the saved test-split hash, loads the saved model and tokenizer, performs inference, and writes `test.json` and `test_confusion.csv`. The completed submission already contains these final results; do not rerun the evaluation merely to regenerate them.

## 10. Limitations and conclusion

- The classifier predicts one of the 11 Product categories present in this dataset; it is not a general-purpose financial advice or fraud-detection system.
- The data reflects complaints submitted to the CFPB and should not be interpreted as a representative sample of all consumers or all financial activity.
- Debt or credit management and Prepaid card had lower test F1 scores than the larger categories. Further work could investigate additional representative data, label quality, and class-specific error patterns.
- Stopword removal, stemming, and lemmatization were not implemented as separate preprocessing steps and were not compared experimentally.
- The project deliverable for this task is the trained and evaluated text-classification model and its supporting code/results. A frontend, API, dashboard, and deployment were not built because they are outside the stated model-building scope.

FinRoute AI demonstrates a leakage-aware NLP classification workflow, comparison of classical machine-learning methods with a transformer model, and independent final evaluation on a held-out test set. The final DistilBERT result was **85.58% accuracy and 79.57% macro-F1** on 12,112 test complaints.

