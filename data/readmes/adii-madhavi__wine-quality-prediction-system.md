# Wine Quality Prediction System

A complete multiclass machine-learning project with an executed Jupyter notebook and a local Streamlit web app. The interface and plots use light ivory, muted burgundy, and sage.

## Start the web app

From this folder in PowerShell, using the prepared environment:

```powershell
.venv\Scripts\python.exe -m streamlit run app.py
```

Open http://localhost:8501. Enter the eleven chemical measurements, select **Predict wine quality**, and inspect the score, category, and class probabilities. The Model results and Explore the dataset tabs show real evaluation results and source data. Predictions can be downloaded as CSV.

## Notebook

Open `Wine_Quality_Prediction.ipynb` in VS Code or Jupyter and select `.venv/Scripts/python.exe` as the kernel. Saved outputs let you read the completed analysis immediately. Run All to reproduce it; training rewrites the artifacts used by the app. Restart the app after retraining to clear its model cache.

The notebook follows all 18 tasks in the supplied brief: inspection, cleaning, EDA, correlations, feature separation, stratified splitting, scaling, four model families, metrics, confusion matrix, feature importance, improvement, tuning, prediction, categories, analysis, and conclusion.

## Fresh setup

Python 3.12 or newer is recommended. The supplied run was tested with the versions recorded in `artifacts/summary.json`; `requirements-lock.txt` records the exact environment.

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe wine_model.py
.venv\Scripts\python.exe -m streamlit run app.py
```

For an identical Python/platform environment, install from `requirements-lock.txt` instead. If using uv, use `uv pip install --python .venv/Scripts/python.exe -r requirements.txt`.

## Method

- Data: supplied `WineQT.csv`, copied unchanged to `data/WineQT.csv`.
- Target: `quality`, scores 3–8. Predictors: all eleven chemical measurements; exclude `Id` and target.
- Cleaning: remove duplicate predictor-and-target rows before splitting; validate numeric data; retain plausible outliers. Median imputation is fitted inside training pipelines.
- Split: stratified 80/20 with seed 42. Three-fold stratified CV on training data selects and tunes models using macro F1. The final choice is fixed before test evaluation.
- Models: Logistic Regression, Random Forest, RBF SVM, KNN; also report a majority-class baseline. Scaling is applied to all except the forest, and controlled unscaled comparisons are included.
- Grid search tunes the winning family. Baseline is retained on a CV tie. All models' test scores are descriptive comparisons, not a second selection step.
- The saved model remains fitted on the training split so app behavior corresponds to the reported evaluation. It is not refitted on the held-out test data.
- Probabilities are model estimates, not validated confidence guarantees. Scores map to Poor (3–4), Average (5), Good (6), Excellent (7–8).

## Project files

| File | Purpose |
|---|---|
| `Wine_Quality_Prediction.ipynb` | Full notebook with explanations, charts, and executed results |
| `wine_model.py` | Shared training, evaluation, export, and validated prediction |
| `app.py` | Light-themed interactive web app |
| `artifacts/` | Trained pipeline, metrics, CV/tuning/scaling tables, and test predictions |
| `test_project.py` | Model and web-app behavior checks |
| `build_notebook.py` | Rebuild notebook source; this clears saved outputs |

Run checks after training:

```powershell
.venv\Scripts\python.exe test_project.py
```

Only load the locally generated model artifact: joblib/pickle files from unknown sources are unsafe. The app is configured to listen on localhost. This is a local educational app, not a deployed public service.

## Interpretation limits

The original dataset has 1,143 samples and strongly imbalanced scores, including only six score-3 wines. Rare-class estimates have very low support. The supplied files do not document batch identity or establish representativeness and all measurement units. Use the source dataset's units; confirm them before entering external laboratory measurements. Predictions estimate sensory quality, not safety. External validation and calibration are needed before operational use.
