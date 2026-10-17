# Predictive Data Analytics CLI & Backend Service

A complete, production-shaped machine learning platform that takes raw tabular data, trains
a predictive model, and serves real-time predictions — through a **Typer CLI**, a
**FastAPI REST API** with Swagger UI, and a **browser form**. Fully containerized with
Docker and automated in the cloud with GitHub Actions.

<p align="center">
  <img src="https://github.com/kamalesh4044/Ai-predictive-analytics/actions/workflows/ai_pipeline.yml/badge.svg" alt="CI">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-2.0-teal" alt="FastAPI">
  <img src="https://img.shields.io/badge/scikit--learn-1.4%2B-orange" alt="scikit-learn">
  <img src="https://img.shields.io/badge/Docker-ready-blue" alt="Docker">
  <img src="https://img.shields.io/badge/Tests-16%20passing-green" alt="Tests">
</p>

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Requirements & Setup](#requirements--setup)
- [CLI Reference](#cli-reference)
- [REST API Reference](#rest-api-reference)
- [Web UI](#web-ui)
- [Docker (Zero Local Install)](#docker-zero-local-install)
- [GitHub Actions / CI-CD](#github-actions--ci-cd)
- [Deployment](#deployment)
- [Testing](#testing)
- [Bring Your Own Dataset](#bring-your-own-dataset)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)

---

## Overview

The system is built as a modular pipeline so each stage can be reused independently:

```
                         ┌──────────────────────────────┐
                         │       data/dataset.csv        │
                         └──────────────┬───────────────┘
                                        │  pandas
                 ┌──────────────────────▼──────────────────────┐
                 │            src/data_processing.py            │
                 │   load_and_clean_data() ─ preprocess_features│
                 └──────────────────────┬──────────────────────┘
                                        │  X (features)  y (target)
                 ┌──────────────────────▼──────────────────────┐
                 │             src/model_training.py            │
                 │   ColumnTransformer + Model + joblib dump    │
                 └──────────────────────┬──────────────────────┘
                                        │  trained artifact
                 ┌──────────────────────▼──────────────────────┐
                 │             models/model.joblib              │
                 └───────────────┬────────────────┬────────────┘
                                 │                │
   ┌─────────────────────────────▼───┐   ┌────────▼──────────────────────────┐
   │          cli.py (Typer)          │   │         main.py (FastAPI)          │
   │  train · predict · predict-file  │   │  /predict · /predict/batch         │
   │  list-models                     │   │  /train · /model/info · /models    │
   │                                  │   │  /ui (browser) · /docs (Swagger)   │
   └──────────────────────────────────┘   └───────────────────────────────────┘
```

Every stage shares the same preprocessing, so what the model sees at prediction time is
exactly what it saw during training.

## Features

### Data Pipeline
- Load and clean CSVs with pandas (drop empty rows/columns, strip whitespace, deduplicate).
- **Median imputation** for missing numeric values, **most-frequent imputation** for missing
  categorical values.
- **StandardScaler** for numeric features, **OneHotEncoder** for categorical features.
- Features and target are separated automatically (target column configurable).

### Model Training
- **6 models** across two task types, with automatic task detection from the target:

| Model | Classification | Regression | Notes |
| --- | :-: | :-: | --- |
| `random_forest` | Yes | Yes | Robust default; captures non-linear patterns |
| `gradient_boosting` | Yes | Yes | Often higher accuracy; slower to train |
| `logistic_regression` | Yes | — | Fast, interpretable linear model |
| `ridge` | — | Yes | Regularized linear regression |

- Task auto-detected: string/categorical or low-cardinality targets → classification;
  numeric targets → regression. Override with `--task`.
- 80/20 stratified train/test split with a fixed random seed (reproducible results).

### Evaluation
- **Classification:** accuracy, ROC-AUC (binary), confusion matrix, full classification report.
- **Regression:** R², MAE, RMSE.
- **Feature importances** extracted for every model (tree importance or |coefficient|).

### Inference
- Identical preprocessing at prediction time, missing features tolerated.
- Single-record and **batch** predictions.
- Class probabilities included alongside each prediction.

### Persistence & Versioning
- Models saved with `joblib` to `models/model.joblib` plus a timestamped versioned copy
  per run (`models/model_20260802_125252.joblib`).
- Each artifact stores metadata: `model_name`, `task`, `trained_at`, `metrics`,
  `feature_columns`, `importances`.

### Interfaces
- **CLI:** `train`, `predict`, `predict-file`, `list-models`.
- **API:** Swagger UI at `/docs`, browser form at `/ui`, and 6 JSON endpoints.
- **DevOps:** Docker image, GitHub Actions CI/CD, weekly scheduled retraining, Render
  one-click deploy blueprint.

## Technology Stack

| Layer | Technology |
| --- | --- |
| Language | Python 3.10+ (developed on 3.12) |
| CLI | Typer |
| REST API | FastAPI + Uvicorn |
| Data | pandas, numpy |
| Machine Learning | scikit-learn |
| Serialization | joblib |
| Containerization | Docker |
| CI / CD | GitHub Actions |
| Testing | pytest + FastAPI TestClient |

## Quick Start

```bash
# 1. Clone and enter the project
git clone https://github.com/kamalesh4044/Ai-predictive-analytics.git
cd Ai-predictive-analytics

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate            # Windows
# source venv/bin/activate       # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Train a model on the sample churn dataset
python cli.py train --data-path data/dataset.csv

# 5. Predict a single record
python cli.py predict -f "Age=45" -f "Tenure=12" -f "MonthlyCharges=80.5" \
  -f "TotalCharges=966.0" -f "Contract=Month-to-month" -f "InternetService=Fiber optic"

# 6. Start the API and open http://localhost:8000/docs
uvicorn main:app --reload
```

## Project Structure

```
predictive_analytics_service/
├── .github/
│   └── workflows/
│       └── ai_pipeline.yml       # CI: train + test + publish Docker image + weekly cron
├── data/                          # Datasets
│   ├── dataset.csv                #   sample churn dataset (500 rows, target: Churn)
│   ├── to_predict.csv             #   sample input for predict-file
│   └── predictions.csv            #   sample output of predict-file
├── models/                        # Trained .joblib models (git-ignored)
├── src/
│   ├── __init__.py
│   ├── data_processing.py         # Load, clean, split features/target
│   ├── model_training.py          # Pipelines, models, metrics, versioning, listing
│   └── predictor.py               # Inference: class, probabilities, model info
├── tests/
│   ├── test_api.py                # Endpoint tests (FastAPI TestClient)
│   └── test_pipeline.py           # Pipeline tests (training, regression, metadata)
├── main.py                        # FastAPI application entry point
├── cli.py                         # Typer CLI entry point
├── requirements.txt
├── Dockerfile
├── render.yaml                    # Render (free) deployment blueprint
├── pytest.ini                     # pytest config (pythonpath)
└── .gitignore / .dockerignore
```

## Requirements & Setup

### Prerequisites
- Python 3.10 or newer.
- (Optional) Docker for the container workflow.
- A GitHub account for CI/CD.

### Local installation

```bash
python -m venv venv
venv\Scripts\activate            # Windows
source venv/bin/activate         # macOS / Linux
pip install -r requirements.txt
```

### Running without installs (Docker)

```bash
docker run -p 8000:8000 ghcr.io/kamalesh4044/ai-predictive-analytics:latest
```

## CLI Reference

```text
Usage: cli.py [OPTIONS] COMMAND [ARGS]...

Commands:
  train          Load data, train a model, and save it to disk.
  predict        Run inference on a single record.
  predict-file   Score an entire CSV file.
  list-models    List saved model files.
```

### `train`

```bash
python cli.py train --data-path data/dataset.csv \
  --model gradient_boosting --task classification --target Churn
```

| Option | Default | Description |
| --- | --- | --- |
| `--data-path` | `data/dataset.csv` | Path to the input CSV dataset. |
| `--model-path` | `models/model.joblib` | Where to save the trained model. |
| `--target` | `Churn` | Name of the target column. |
| `--model` | `random_forest` | `random_forest`, `gradient_boosting`, `logistic_regression`, `ridge`. |
| `--task` | `auto` | `auto`, `classification`, or `regression`. |

Training output includes the metrics, a classification report (when applicable), and the
paths of the saved model and its versioned copy.

### `predict`

```bash
python cli.py predict --show-probability \
  -f "Age=45" -f "Tenure=12" -f "MonthlyCharges=80.5" \
  -f "TotalCharges=966.0" -f "Contract=Month-to-month" -f "InternetService=Fiber optic"
```

| Option | Default | Description |
| --- | --- | --- |
| `--feature` / `-f` | *(required)* | Feature in `key=value` format. Repeat per feature. |
| `--model-path` | `models/model.joblib` | Path to the trained model. |
| `--show-probability` | off | Also print class probabilities. |

Example output:

```text
Prediction: Yes
Probabilities: {'No': 0.26, 'Yes': 0.74}
```

### `predict-file`

```bash
python cli.py predict-file --data-path data/to_predict.csv --output data/predictions.csv
```

Adds a `prediction` column to the input features and writes a new CSV.

### `list-models`

```bash
python cli.py list-models
# model.joblib (1446.3 KB)
# model_20260802_125252.joblib (1409.0 KB)
```

## REST API Reference

Start the server:

```bash
uvicorn main:app --reload
# or
venv\Scripts\uvicorn.exe main:app --reload
```

| Endpoint | Method | Description |
| --- | --- | --- |
| `/` | GET | Service info |
| `/docs` | GET | Interactive Swagger UI |
| `/redoc` | GET | ReDoc API documentation |
| `/ui` | GET | Browser prediction form |
| `/predict` | POST | Predict one record |
| `/predict/batch` | POST | Predict many records |
| `/train` | POST | Train a model via HTTP |
| `/model/info` | GET | Metadata of the current model |
| `/models` | GET | List saved model files |

### `POST /predict`

Request body:

```json
{
  "features": {
    "Age": 45,
    "Tenure": 12,
    "MonthlyCharges": 80.5,
    "TotalCharges": 966.0,
    "Contract": "Month-to-month",
    "InternetService": "Fiber optic"
  }
}
```

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": {"Age": 45, "Tenure": 12, "MonthlyCharges": 80.5, "TotalCharges": 966.0, "Contract": "Month-to-month", "InternetService": "Fiber optic"}}'
```

Response:

```json
{
  "prediction": "Yes",
  "probability": { "No": 0.26, "Yes": 0.74 }
}
```

### `POST /predict/batch`

```json
{
  "features": [
    { "Age": 45, "Tenure": 12 },
    { "Age": 60, "Tenure": 60 }
  ]
}
```

Response:

```json
{
  "prediction": ["Yes", "No"],
  "probability": [ {"No": 0.26, "Yes": 0.74}, {"No": 0.81, "Yes": 0.19} ]
}
```

### `POST /train`

```json
{
  "data_path": "data/dataset.csv",
  "model_name": "gradient_boosting",
  "target_column": "Churn",
  "task": "auto",
  "model_path": "models/model.joblib"
}
```

Response includes the model path and evaluation metrics:

```json
{
  "model_path": "models/model.joblib",
  "model_name": "gradient_boosting",
  "task": "classification",
  "metrics": { "accuracy": 0.77, "roc_auc": 0.78, "confusion_matrix": [[...]] }
}
```

### `GET /model/info`

Returns the current model's metadata: `model_name`, `task`, `trained_at`, `metrics`,
`feature_columns`, `numeric_columns`, `categorical_columns`, and `importances`.

### `GET /models`

```json
{ "models": [ { "file": "model.joblib", "size_kb": 1446.3 }, ... ] }
```

### Status codes

| Code | Meaning |
| --- | --- |
| `200` | Success |
| `400` | Invalid request (bad model name, unsupported task, bad input) |
| `404` | Dataset file not found |
| `503` | No trained model available — run `train` first |
| `500` | Unexpected error |

## Web UI

Open http://localhost:8000/ui for a ready-to-use prediction form for the churn use case.
Fill in the form, click **Predict**, and see the predicted class with confidence — no JSON
or curl required.

## Docker (Zero Local Install)

The image trains the model on the sample dataset at build time, so the container is
self-sufficient and serves predictions out of the box.

```bash
# Build locally
docker build -t ai-predictive-analytics .
docker run -p 8000:8000 ai-predictive-analytics

# Or pull the image published by CI
docker run -p 8000:8000 ghcr.io/kamalesh4044/ai-predictive-analytics:latest
```

Open http://localhost:8000/docs once the container is running.

## GitHub Actions / CI-CD

`.github/workflows/ai_pipeline.yml` automates the whole pipeline:

| Trigger | Action |
| --- | --- |
| `push` | Full pipeline below |
| `schedule` (weekly, Sunday 00:00 UTC) | Retrain + retest automatically |
| `workflow_dispatch` | Manual re-run from the Actions tab |

**Job 1 — Train and verify** (Ubuntu):
1. Check out the repository.
2. Set up Python 3.12.
3. Install `requirements.txt`.
4. Train the model: `python cli.py train --data-path data/dataset.csv`.
5. Run the pytest suite.

**Job 2 — Build and publish Docker image** (on `main`):
1. Log in to the GitHub Container Registry with `GITHUB_TOKEN`.
2. Build with Docker Buildx.
3. Publish to `ghcr.io/<owner>/<repo>:latest`.

Current status: ![CI](https://github.com/kamalesh4044/Ai-predictive-analytics/actions/workflows/ai_pipeline.yml/badge.svg)

> The published image is **private** by default. To make it public: GitHub → **Packages** →
> **ai-predictive-analytics** → **Package settings** → **Change visibility** → **Public**.

## Deployment

### Render (free, one click)

The repo includes a `render.yaml` blueprint. Click the button below (or: **New →
Blueprint → select the repo**):

```
https://render.com/deploy?repo=https://github.com/kamalesh4044/Ai-predictive-analytics
```

Render builds the Dockerfile and serves the API at `https://<service>.onrender.com`
with `/docs` and `/ui` available.

### Other free options

| Host | How |
| --- | --- |
| Hugging Face Spaces | Create a **Docker** Space and push the repo |
| Railway | New project → Deploy from GitHub repo (auto-detects the Dockerfile) |
| Fly.io | `fly launch` in the repo root |

## Testing

```bash
pytest
```

The suite (16 tests) covers:

- Data loading and feature/target splitting.
- Classification training (metrics, probabilities) and regression training (R²).
- Model metadata and versioned listing.
- All API endpoints, including batch prediction, training via HTTP, and the missing-model
  error path.

## Bring Your Own Dataset

The pipeline is generic — any supervised tabular dataset works:

1. Put your CSV in `data/`. It needs a header row and one target column.
2. Train:

```bash
python cli.py train --data-path data/your_dataset.csv --target your_target --task auto
```

3. The task (classification vs regression) is detected automatically; numeric columns are
   scaled, categorical columns are one-hot encoded.
4. Predict new records with the CLI, the API, or score a whole CSV with `predict-file`.

Example real-world use cases: customer churn, loan default, spam detection, sales
forecasting, fraud flagging, equipment failure prediction.

## Troubleshooting

| Problem | Solution |
| --- | --- |
| `ModuleNotFoundError: No module named 'fastapi'` | You are using the system Python, not the venv. Run `venv\Scripts\activate` first (or use `venv\Scripts\python`). |
| `No model found at 'models/model.joblib'` | Train first: `python cli.py train --data-path data/dataset.csv`. |
| `prediction` works but `/model/info` is incomplete | The model was trained with an older version. Retrain. |
| GitHub Actions warns about Node.js 20 | Harmless — GitHub forces those actions onto Node 24 automatically. |
| `ghcr.io/...` pull says authentication required | The image is private. Change its visibility in Package settings (see CI-CD section). |
| Values like `None` disappear from data | pandas treats the string `None` as missing on CSV read. Use a different label (e.g. `No service`). |
| `docker` command not found | Install Docker Desktop for Windows/Mac, or Docker Engine on Linux. |

## Roadmap

- [x] Data pipeline (cleaning, imputation, scaling, encoding)
- [x] Random Forest classifier (default churn use case)
- [x] CLI and REST API
- [x] Docker image + GitHub Actions CI/CD + weekly retraining
- [x] Multi-model support (classification + regression)
- [x] Rich metrics and feature importances
- [x] Model versioning and listing
- [x] Batch prediction, browser UI, `predict-file`
- [ ] XGBoost / LightGBM support
- [ ] Model monitoring and drift detection
- [ ] API authentication (API keys)
- [ ] SHAP explainability reports
- [ ] Automated tests for the Docker image itself

---

Built with FastAPI, Typer, scikit-learn, pandas, and Docker.
                  ❤️
                
