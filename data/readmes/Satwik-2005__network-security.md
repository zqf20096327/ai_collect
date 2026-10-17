### Network Security Project for Phishing Data

# 🛡️ Network Security - Phishing Website Detection System

An end-to-end Machine Learning and MLOps project that detects whether a website is **Legitimate** or **Phishing** using URL and website-based features. The project automates the complete ML lifecycle including data ingestion, validation, transformation, model training, experiment tracking, and prediction through a FastAPI application.

---

## 📌 Features

- 📥 Data Ingestion from MongoDB Atlas
- ✅ Data Validation with Schema Checking
- 📊 Dataset Drift Detection using Evidently AI
- 🔄 Data Transformation & Preprocessing
- 🤖 Multiple Machine Learning Models Training
- 📈 Experiment Tracking using MLflow
- 🚀 REST API using FastAPI
- 📁 CSV File Upload for Batch Predictions
- 💾 Model & Preprocessor Serialization
- 🐳 Docker Support (Optional)

---

## 🛠️ Tech Stack

- Python
- Scikit-learn
- FastAPI
- MongoDB Atlas
- MLflow
- Evidently AI
- Pandas
- NumPy
- Jupyter Notebook
- Git & GitHub

---

## 📂 Project Structure

```
Network Security
│
├── app.py
├── main.py
├── requirements.txt
├── setup.py
│
├── network_security
│   ├── components
│   ├── configuration
│   ├── constants
│   ├── entity
│   ├── exception
│   ├── logging
│   ├── pipeline
│   └── utils
│
├── templates
├── static
├── final_models
├── prediction_output
└── artifacts
```

---

## ⚙️ Project Workflow

1. Collect dataset from **MongoDB Atlas**
2. Validate dataset schema and detect drift
3. Perform preprocessing and feature transformation
4. Train multiple ML models
5. Select the best performing model
6. Track experiments using MLflow
7. Save trained model and preprocessor
8. Deploy prediction API using FastAPI
9. Predict phishing websites from uploaded CSV files

---

## 🤖 Machine Learning Models Used

- Random Forest Classifier
- Decision Tree Classifier
- Gradient Boosting Classifier
- Logistic Regression
- AdaBoost Classifier

The best performing model is automatically selected based on evaluation metrics.

---

## 📊 Dataset Features

The model uses 30 URL and website-related features including:

- Having IP Address
- URL Length
- Shortening Service
- Having @ Symbol
- SSL Final State
- Domain Registration Length
- HTTPS Token
- URL of Anchor
- Links in Tags
- DNS Record
- Google Index
- Web Traffic
- Page Rank
- Age of Domain
- Statistical Report
- and several other phishing indicators.

---

## 📈 MLflow Tracking

MLflow is integrated to log:

- F1 Score
- Precision
- Recall
- Model Artifacts
- Experiment History

---

## 🚀 Running the Project

### Clone Repository

```bash
git clone https://github.com/your-username/network-security.git
cd network-security
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Train Model

```bash
python main.py
```

### Run FastAPI Server

```bash
uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## 📤 API Endpoints

### Train Model

```
GET /train
```

Triggers the complete machine learning pipeline.

---

### Predict Phishing Websites

```
POST /predict
```

Upload a CSV file containing website features to receive predictions.

---

## 👨‍💻 Author

**Satwik Reddy Kunduru**

- GitHub: https://github.com/Satwik-2005


## ⭐ If you found this project useful, consider giving it a Star!
