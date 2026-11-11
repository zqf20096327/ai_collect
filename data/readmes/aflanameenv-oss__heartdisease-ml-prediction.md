# Heart Failure Clinical Risk Prediction 

End-to-end supervised classification pipeline predicting cardiovascular disease from clinical and ECG parameters.

## 1. Problem & Dataset
- **Dataset:** UCI / Kaggle Heart Failure Prediction Dataset (918 records, 12 clinical features)
- **Target Variable:** `HeartDisease` (1 = Heart Disease present, 0 = Normal)
- **Objective:** Achieve Recall >= 0.90 and ROC-AUC >= 0.90 to minimize false-negative clinical diagnoses.

## 2. Methodology
- **Data Cleaning:** Identified 172 impossible zero-readings in `Cholesterol` and 1 in `RestingBP`, converting them to `NaN` for median imputation.
- **Statistical Testing:** Verified feature significance using Welch's two-sample t-test (`MaxHR`), Mann-Whitney U test (`Oldpeak`), and Chi-Square test of independence (`ChestPainType`).
- **Leak-Free Pipeline:** Built using Scikit-Learn `ColumnTransformer` (median/mode imputation, `StandardScaler`, and `OneHotEncoder`) inside 5-fold Stratified `GridSearchCV`.

## 3. Test Set Results (20% Holdout)
| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Gradient Boosting** | **0.8859** | **0.8932** | 0.9020 | 0.8976 | **0.9350** |
| **Logistic Regression** | **0.8859** | 0.8857 | **0.9118** | **0.8986** | 0.9329 |
| **SVM** | 0.8533 | 0.8788 | 0.8529 | 0.8657 | 0.9319 |
| **Random Forest** | 0.8587 | 0.8800 | 0.8627 | 0.8713 | 0.9196 |
| **Baseline (Dummy)** | 0.5543 | 0.5543 | 1.0000 | 0.7133 | 0.5000 |

## 4. Files in Repository
- `CSE570_Heart_Disease_Project.ipynb`: Full Google Colab implementation
- `heart.csv`: Raw clinical dataset
- `*.png`: Exported EDA and model evaluation plots
- `requirements.txt`: Python package dependencies
