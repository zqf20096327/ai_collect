# Credit Card Fraud Detection System

A machine learning project that detects potentially fraudulent credit card transactions using supervised learning techniques.

## Project Overview

Credit card fraud detection is a binary classification problem where the goal is to identify whether a transaction is:

- `0` - Legitimate
- `1` - Fraudulent

This project uses the Credit Card Fraud Detection dataset and compares multiple machine learning models before selecting and tuning a Random Forest classifier.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit

## Project Workflow

1. Data Loading
2. Exploratory Data Analysis (EDA)
3. Data Quality Checking
4. Class Imbalance Analysis
5. Feature Correlation Analysis
6. Data Preprocessing
7. Feature Scaling
8. Logistic Regression Model
9. Random Forest Model
10. Model Evaluation
11. Hyperparameter Tuning
12. Threshold Optimization
13. Feature Importance Analysis
14. Streamlit Deployment

## Machine Learning Models

### Logistic Regression

The Logistic Regression model was used as a baseline classification model.

### Random Forest

Random Forest performed better than Logistic Regression based on PR-AUC and F1-score.

The tuned Random Forest achieved:

- PR-AUC: `0.8139`
- F1-score: `0.8409`
- Precision: `0.9136`
- Recall: `0.7789`

The optimized classification threshold was approximately `0.45`.

## Dataset

The dataset contains anonymized credit card transaction features including:

- `Time`
- `V1` to `V28`
- `Amount`
- `Class`

The `Class` column is the target variable.

## Streamlit Application

The project includes a Streamlit web application where users can upload a transaction CSV file.

The application:

1. Accepts a CSV file.
2. Loads the transaction data.
3. Applies the trained scaler.
4. Uses the trained Random Forest model.
5. Calculates fraud probability.
6. Applies the optimized threshold.
7. Displays the prediction as either:
   - Legitimate
   - Fraud
8. Displays the number of potentially fraudulent transactions.

## Live Demo

   [🚀 Try the Credit Card Fraud Detection System](https://ak-zx-data-science-project-app-k7ddvy.streamlit.app)
