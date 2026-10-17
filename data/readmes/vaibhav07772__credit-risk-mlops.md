# 🏦 Credit Risk MLOps — End-to-End ML System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge\&logo=python)
![XGBoost](https://img.shields.io/badge/XGBoost-2.0-red?style=for-the-badge)
![LightGBM](https://img.shields.io/badge/LightGBM-ML-green?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111-009688?style=for-the-badge\&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge\&logo=docker)
![MLflow](https://img.shields.io/badge/MLflow-2.11-0194E2?style=for-the-badge)
![Optuna](https://img.shields.io/badge/Optuna-3.6-4C8CBF?style=for-the-badge)

### An end-to-end credit-risk machine learning pipeline with feature engineering, experiment tracking, hyperparameter tuning, FastAPI serving, and Docker deployment.

**Home Credit Default Risk • 307K+ Applications • 6 Relational Tables • 301 Engineered Features**

[🌐 Live API](https://credit-risk-api-o0gj.onrender.com) ·
[📖 API Docs](https://credit-risk-api-o0gj.onrender.com/docs) ·
[❤️ Health Check](https://credit-risk-api-o0gj.onrender.com/health)

</div>

---

## 🎯 Overview

**Credit Risk MLOps** is an end-to-end machine learning system designed to estimate the probability of loan default using the **Home Credit Default Risk** dataset.

The project demonstrates how a traditional ML model can be taken beyond experimentation into a structured workflow covering:

```text
Raw Data
   ↓
Data Validation
   ↓
Feature Engineering
   ↓
Model Training
   ↓
Hyperparameter Tuning
   ↓
Experiment Tracking
   ↓
Model Metadata
   ↓
FastAPI Serving
   ↓
Docker
   ↓
Cloud Deployment
```

The dataset contains **307,511 loan applications** across multiple relational tables. The pipeline aggregates information from six tables and creates **301 engineered features** for model training.

### What this project demonstrates

* Large tabular dataset processing
* Memory-efficient data loading
* Multi-table feature engineering
* Credit-risk classification
* Class-imbalance handling
* Cross-validation
* XGBoost / LightGBM / CatBoost comparison
* Optuna hyperparameter optimization
* MLflow experiment tracking
* DVC-based data versioning
* FastAPI model serving
* Docker containerization
* Cloud deployment using Render
* Model metadata and health endpoints

---

## 📊 Model Performance

The following results are from the experiments included in the project.

| Model             |    ROC-AUC | KS Statistic | F1 — Default | Lift @ 10% |
| ----------------- | ---------: | -----------: | -----------: | ---------: |
| **XGBoost** ⭐     | **0.7862** |   **0.4331** |       0.2843 |  **3.72×** |
| LightGBM Tuned    |     0.7861 |       0.4332 |       0.3170 |      3.69× |
| LightGBM Baseline |     0.7854 |       0.4329 |       0.3001 |      3.70× |

### Metric Interpretation

**ROC-AUC — 0.7862**

Measures how well the model separates default and non-default applications across classification thresholds.

**KS Statistic — 0.4331**

Measures the maximum separation between the cumulative distributions of the two classes.

**Lift @ 10% — 3.72×**

Indicates that the highest-risk 10% segment captured approximately 3.72 times the default concentration relative to the overall population in the reported evaluation.

> ⚠️ These metrics are dataset/evaluation dependent and should not be interpreted as guarantees of real-world lending performance.

---

# 🏗️ System Architecture

```text
┌─────────────────────────────────────────────────────────────┐
│                     DATA LAYER                              │
│                                                             │
│  Application │ Bureau │ Previous Loans │ POS_CASH          │
│  Installments │ Credit Card                              │
│                                                             │
│  6 relational tables • 27M+ rows                            │
│  DVC tracked                                                │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                FEATURE ENGINEERING                          │
│                                                             │
│  • Application features                                    │
│  • Bureau aggregations                                     │
│  • Previous-loan features                                  │
│  • POS / Installment / Credit-card features                │
│  • Ratios and aggregated statistics                        │
│  • EXT_SOURCE combinations                                  │
│                                                             │
│                     301 Features                            │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                MODEL TRAINING                               │
│                                                             │
│  LightGBM │ XGBoost │ CatBoost                              │
│                                                             │
│  • Stratified 5-Fold CV                                    │
│  • Class imbalance handling                                │
│  • MLflow experiment tracking                              │
│  • Optuna hyperparameter tuning                            │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                 MODEL SERVING                               │
│                                                             │
│  FastAPI + Uvicorn                                          │
│  • /health                                                  │
│  • /model/info                                              │
│  • /predict                                                 │
│                                                             │
│  Metadata-based startup                                     │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                  CONTAINERIZATION                            │
│                                                             │
│                        Docker                               │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                    DEPLOYMENT                               │
│                                                             │
│                         Render                              │
│                                                             │
│  https://credit-risk-api-o0gj.onrender.com                  │
└─────────────────────────────────────────────────────────────┘
```

---

# 🧠 Machine Learning Pipeline

## 1. Data Processing

The project works with six relational tables from the Home Credit dataset:

* Application
* Bureau
* Previous Applications
* POS Cash Balance
* Installments Payments
* Credit Card Balance

The data is aggregated to the customer/application level before model training.

---

## 2. Feature Engineering

The feature engineering pipeline generates **301 features** using:

* Aggregation statistics
* Ratios
* Historical loan information
* Bureau information
* Payment behavior
* Credit-card behavior
* External credit scores
* Age and employment-related features
* Cross-table features

The goal is to transform multiple relational tables into a single modeling dataset.

---

## 3. Class Imbalance

Credit-default datasets are typically imbalanced, so the training pipeline includes model-specific class weighting.

### LightGBM

```python
is_unbalance=True
```

### XGBoost

```python
scale_pos_weight=3
```

### CatBoost

```python
auto_class_weights="Balanced"
```

The project also uses stratified cross-validation and threshold tuning during evaluation.

---

# 🔬 Model Training & Tuning

Three tree-based gradient boosting approaches are evaluated:

```text
LightGBM
   │
   ├── Baseline
   └── Optuna Tuned

XGBoost
   └── 5-Fold CV

CatBoost
   └── 5-Fold CV
```

### Optuna

Optuna is used for hyperparameter optimization with:

* TPE sampler
* Median Pruner
* Cross-validation based evaluation

This allows the training pipeline to search for better hyperparameter configurations rather than relying entirely on manually selected values.

---

# 📈 Evaluation Metrics

The project evaluates models using credit-risk-oriented metrics:

| Metric           | Purpose                                               |
| ---------------- | ----------------------------------------------------- |
| **ROC-AUC**      | Ranking/separation ability                            |
| **KS Statistic** | Distribution separation                               |
| **F1 Score**     | Default-class precision/recall balance                |
| **Lift @ 10%**   | Concentration of defaults in the highest-risk segment |

Example:

```text
ROC-AUC      → 0.7862
KS           → 0.4331
F1 Default   → 0.2843
Lift @ 10%   → 3.72×
```

---

# 🛠️ Tech Stack

| Layer                     | Technology                  |
| ------------------------- | --------------------------- |
| **Language**              | Python 3.11                 |
| **ML Models**             | XGBoost, LightGBM, CatBoost |
| **Hyperparameter Tuning** | Optuna                      |
| **Experiment Tracking**   | MLflow                      |
| **Data Versioning**       | DVC                         |
| **Feature Storage**       | Parquet                     |
| **API**                   | FastAPI + Uvicorn           |
| **Validation**            | Pydantic V2                 |
| **Containerization**      | Docker                      |
| **Cloud Deployment**      | Render                      |
| **Explainability**        | SHAP                        |
| **Data Processing**       | Pandas / NumPy              |

---

# 📁 Project Structure

```text
credit-risk-mlops/
│
├── src/
│   ├── data/
│   │   ├── load.py
│   │   ├── validate.py
│   │   └── eda.py
│   │
│   ├── features/
│   │   ├── application_features.py
│   │   ├── bureau_features.py
│   │   ├── previous_loan_features.py
│   │   ├── other_tables_features.py
│   │   └── build_features.py
│   │
│   ├── models/
│   │   ├── utils.py
│   │   ├── baseline.py
│   │   ├── train.py
│   │   └── tune.py
│   │
│   └── serving/
│       └── app.py
│
├── data/
│   ├── raw/
│   └── features/
│
├── models/
│   └── saved models + metadata
│
├── reports/
│   └── metrics + plots
│
├── configs/
│   └── config.yaml
│
├── Dockerfile
├── requirements.txt
├── requirements-api.txt
├── README.md
└── .gitignore
```

---

# 🚀 Quick Start

## 1. Clone Repository

```bash
git clone https://github.com/vaibhav07772/credit-risk-mlops.git
cd credit-risk-mlops
```

---

## 2. Create Conda Environment

```bash
conda create -n credit-risk python=3.11 -y
conda activate credit-risk
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

For API-only serving:

```bash
pip install -r requirements-api.txt
```

---

# 📥 Download Dataset

This project uses the **Home Credit Default Risk** dataset.

Download the dataset through Kaggle:

```bash
kaggle competitions download \
    -c home-credit-default-risk \
    -p data/raw
```

Extract the downloaded archive:

```bash
cd data/raw
tar -xf home-credit-default-risk.zip
cd ../..
```

> Make sure your Kaggle API credentials are configured before running the download command.

---

# ⚙️ Build Features

Run the feature engineering pipeline:

```bash
python -m src.features.build_features
```

Expected output:

```text
data/features/train_features.parquet
```

The generated dataset contains the engineered modeling features.

---

# 🧪 Train Models

### LightGBM Baseline

```bash
python -m src.models.baseline
```

### Multi-Model Training

```bash
python -m src.models.train
```

### Optuna Hyperparameter Tuning

```bash
python -m src.models.tune
```

---

# 📊 MLflow Experiment Tracking

Start the MLflow UI:

```bash
mlflow ui --backend-store-uri mlruns --port 5000
```

Open:

```text
http://localhost:5000
```

Experiments include:

* LightGBM baseline
* XGBoost
* LightGBM tuned
* Cross-validation metrics
* Hyperparameters
* Model evaluation results

---

# 🚀 Run API Locally

Start the FastAPI application:

```bash
uvicorn src.serving.app:app \
    --host 0.0.0.0 \
    --port 8000
```

API:

```text
http://localhost:8000
```

Interactive documentation:

```text
http://localhost:8000/docs
```

---

# 🐳 Docker

Build the API image:

```bash
docker build -t credit-risk-api .
```

Run the container:

```bash
docker run -p 8000:8000 credit-risk-api
```

Then open:

```text
http://localhost:8000/docs
```

---

# 📡 API Endpoints

| Method | Endpoint      | Description             |
| ------ | ------------- | ----------------------- |
| `GET`  | `/`           | Service information     |
| `GET`  | `/health`     | Health and model status |
| `GET`  | `/model/info` | Model metadata          |
| `POST` | `/predict`    | Default-risk prediction |

---

# 🔮 Prediction API

### Request

```bash
curl -X POST "https://credit-risk-api-o0gj.onrender.com/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age_years": 35,
    "gender": "M",
    "amt_income_total": 75000,
    "amt_credit": 200000,
    "amt_annuity": 10000,
    "amt_goods_price": 200000,
    "ext_source_1": 0.5,
    "ext_source_2": 0.6,
    "ext_source_3": 0.55,
    "employed_years": 8,
    "cnt_fam_members": 3,
    "cnt_children": 1
  }'
```

### Response

```json
{
  "probability_default": 0.0384,
  "probability_repaid": 0.9616,
  "decision": "APPROVE",
  "risk_band": "LOW",
  "model_version": "XGBoost",
  "timestamp": "2026-09-22T12:55:15.394458"
}
```

> The API response shown above is an example response demonstrating the serving contract.

---

# 🌐 Live Deployment

The API is deployed on Render:

**Live API**

https://credit-risk-api-o0gj.onrender.com

**Swagger Documentation**

https://credit-risk-api-o0gj.onrender.com/docs

**Health Endpoint**

https://credit-risk-api-o0gj.onrender.com/health

---

# ⚡ Serving Optimization

The serving layer was optimized to avoid unnecessarily loading the complete feature dataset during API startup.

### Metadata-Based Loading

```text
Full Parquet
122 MB
   ↓
Model metadata
19 KB
```

This reduces the amount of data required by the API during startup.

The reported project measurements include:

| Optimization                       |    Reported Result |
| ---------------------------------- | -----------------: |
| Application table memory reduction | **536 MB → 95 MB** |
| Metadata size                      |          **19 KB** |
| Feature parquet                    |         **122 MB** |
| Docker image                       |         **611 MB** |
| Reported startup time              |       **~0.3 sec** |

These measurements depend on the local environment, model artifact, and deployment configuration.

---

# 🧠 Memory Optimization

The project includes a custom memory-reduction utility for tabular data.

Example transformation:

```text
Application Table

Before:
536 MB

After:
95 MB

Reduction:
~82%
```

This allows the data-processing pipeline to operate within a more constrained local-memory environment.

---

# 🔄 End-to-End MLOps Workflow

```text
             ┌──────────────┐
             │  Raw Dataset │
             └──────┬───────┘
                    │
                    ▼
          ┌───────────────────┐
          │ Data Validation   │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │ Feature Engineering│
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │ Model Training    │
          │ LGB/XGB/CatBoost  │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │ Optuna Tuning     │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │ MLflow Tracking   │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │ Model Artifact    │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │ FastAPI           │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │ Docker Container  │
          └─────────┬─────────┘
                    │
                    ▼
          ┌───────────────────┐
          │ Render Deployment │
          └───────────────────┘
```

---

# 🎯 Key Technical Decisions

## 1. Memory-Efficient Data Processing

Large tabular datasets can consume significant RAM.

The project uses:

* Numeric dtype downcasting
* Memory-aware data loading
* Aggregation before final feature construction
* Parquet-based feature storage

Reported application-table memory usage:

```text
536 MB → 95 MB
```

---

## 2. Multi-Table Feature Engineering

Instead of using only the application table, information from multiple historical tables is aggregated.

```text
6 Tables
   ↓
Customer/Application-Level Aggregations
   ↓
301 Engineered Features
```

This incorporates historical financial behavior into the modeling dataset.

---

## 3. Cross-Validation

Models are evaluated using **5-fold cross-validation** to obtain more robust validation estimates than a single train/validation split.

---

## 4. Class-Imbalance Handling

Different models use different class-weighting strategies:

```text
LightGBM  → is_unbalance
XGBoost   → scale_pos_weight
CatBoost  → Balanced class weights
```

---

## 5. Hyperparameter Optimization

Optuna searches for suitable model configurations using:

```text
TPE Sampler
     +
Median Pruner
     +
Cross-Validation
```

---

# 📊 Results Summary

| Metric                         | Reported Result |
| ------------------------------ | --------------: |
| **ROC-AUC**                    |      **0.7862** |
| **KS Statistic**               |      **0.4331** |
| **F1 — Default**               |      **0.2843** |
| **Lift @ 10%**                 |       **3.72×** |
| **Training Time**              |          ~5 min |
| **Reported Inference Latency** |          <50 ms |

> Performance depends on the dataset split, preprocessing, hardware, serving configuration, and evaluation methodology. The reported values should therefore be treated as project experiment results rather than universal benchmarks.

---

# 🔍 Explainability

The project includes **SHAP** in the technology stack for model explainability.

Potential applications include:

* Global feature importance
* Individual prediction explanations
* Feature contribution analysis
* Understanding model behavior

> Explainability outputs should be interpreted alongside model validation and domain review.

---

# 🧪 Example Use Case

Suppose an application contains:

```text
Income              → ₹75,000
Credit Requested    → ₹2,00,000
Employment          → 8 years
Family Members      → 3
External Scores     → available
Historical Data     → available
```

The API processes the application and returns an estimated default probability:

```text
Default Probability
        ↓
   Risk Band
        ↓
Decision Output
```

Example:

```json
{
  "probability_default": 0.0384,
  "probability_repaid": 0.9616,
  "decision": "APPROVE",
  "risk_band": "LOW"
}
```

> This project output is an ML prediction example and should not be treated as an actual lending decision without appropriate validation, governance, compliance, and human/business review.

---

# 🚧 Future Enhancements

The current system provides the core ML + serving workflow. Potential extensions include:

* [ ] MLflow Model Registry
* [ ] SHAP per-prediction explanations
* [ ] Evidently-based data/model drift monitoring
* [ ] Automated retraining workflow
* [ ] Airflow orchestration
* [ ] Grafana monitoring dashboard
* [ ] Champion vs challenger model evaluation
* [ ] CI/CD pipeline
* [ ] Automated model validation gates
* [ ] Model rollback strategy
* [ ] Production monitoring and alerting

---

# 📚 Dataset

This project uses the:

**Home Credit Default Risk Dataset**

Kaggle competition:

https://www.kaggle.com/c/home-credit-default-risk

The dataset contains multiple relational tables describing loan applications and historical financial behavior.

---

# 🔐 Responsible Use

Credit-risk models can affect access to financial services and therefore require careful validation and governance.

This project is intended as an **ML/MLOps engineering and educational implementation**.

A real lending system would additionally require:

* Regulatory compliance
* Fairness and bias evaluation
* Data-quality monitoring
* Privacy controls
* Human/business review
* Model validation
* Explainability and documentation
* Appropriate approval policies
* Monitoring for model/data drift

The model should not be used as a standalone basis for real-world lending decisions without appropriate controls.

---

# 🧑‍💻 What I Learned

This project helped demonstrate practical experience with:

* End-to-end ML pipelines
* Large tabular datasets
* Feature engineering
* Imbalanced classification
* Gradient boosting models
* Cross-validation
* Hyperparameter optimization
* MLflow
* DVC
* FastAPI
* Docker
* Cloud deployment
* Model serving
* API design
* ML system optimization

---

# 🤝 Contributing

Contributions, improvements, and suggestions are welcome.

```bash
git clone https://github.com/vaibhav07772/credit-risk-mlops.git
cd credit-risk-mlops
```

Create a feature branch:

```bash
git checkout -b feature/your-feature
```

Commit your changes:

```bash
git add .
git commit -m "Add your feature"
```

Push:

```bash
git push origin feature/your-feature
```

Then open a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for details.

---

# 👨‍💻 Author

## Vaibhav Singh

**Aspiring AI/ML Engineer | Generative AI | Agentic AI | MLOps**

### Connect

* 🐙 GitHub: [@vaibhav07772](https://github.com/vaibhav07772)
* 💼 LinkedIn: [Vaibhav Singh](https://linkedin.com/in/vaibhav-singh-9a9b9434a)
* 🌐 Live API: [credit-risk-api-o0gj.onrender.com](https://credit-risk-api-o0gj.onrender.com)

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

**Built with Python • XGBoost • LightGBM • MLflow • Optuna • FastAPI • Docker**

</div>
