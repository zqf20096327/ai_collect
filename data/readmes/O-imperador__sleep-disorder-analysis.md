
# **Sleep Disorder Analysis & Prediction**  
A small data-science project exploring sleep patterns and building a model to predict whether a person may have a sleep disorder.
**Source:**  
[Sleep Health and Lifestyle Dataset - Kaggle](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset/)
---

## **📌 Project Overview**
This project focuses on understanding how different lifestyle and health factors relate to sleep quality.  
The dataset includes information such as sleep duration, stress level, physical activity, BMI category, blood pressure, and more.

The goal of the project is twofold:
1. **Explore and clean the dataset** to understand patterns and relationships.  
2. **Build a machine learning model** that predicts whether a person has:
   - **NoDisorder**
   - **Insomnia**
   - **Sleep Apnea**

---

## **📁 Dataset**
After cleaning, the dataset contains:
- 374 entries  
- 14 features + 1 target variable  
- No missing values  
- Health metrics split and standardized  
- Clear categories for sleep disorders

Some transformations:
- `"Normal Weight"` → `"Normal"`  
- Missing sleep disorder labels filled with `"NoDisorder"`  
- `"Blood Pressure"` split into `Systolic` and `Diastolic`  
- Column names standardized (spaces replaced with `_`)

---

## **📊 Exploratory Analysis**
Several visualizations were used to understand the data better, including:

### **Relationships studied**
- Sleep duration vs. stress level  
- BMI vs. sleep disorder  
- Physical activity vs. sleep quality  
- Heart rate, steps, and blood pressure distributions  
- Boxplots to compare groups  
- Correlation matrix for numeric variables  

These helped highlight patterns such as:
- Higher stress levels are often linked to lower sleep quality  
- Obesity shows more frequent sleep disorders  
- Daily steps differ between disorder categories

---

## **🧠 Machine Learning Model**
The predictive model used is a **Random Forest Classifier**.

### **Why Random Forest?**
- Works well with mixed numerical & categorical features  
- Handles nonlinear relationships  
- Robust to imbalance  
- Easy to interpret using feature importance  
- Excellent baseline accuracy

### **Data Splitting**
The data was split into:
- **70% Training**
- **15% Validation**
- **15% Testing**

This ensures the model is tested only on completely unseen data.

### **Evaluation**
Metrics used:
- Accuracy  
- Classification report  
- Confusion matrix  

The model performs reliably and generalizes well on the test set (96% accuracy).

---


---

## **🛠 Technologies Used**
- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  

---

## **🚀 How to Run the Project**

### 1. Clone the repo
```bash
git clone https://github.com/O-imperador/sleep-disorder-analysis.git
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 2. Install optional dependencies
```bash
pip install -r requirements-dev.txt
```
### 3. Run the notebook
Open `notebook.ipynb` in Jupyter Notebook or VSCode and run the cells.

---

## ** Acknowledgements**
- Dataset from [Kaggle - Sleep Health and Lifestyle Dataset](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset/)
- Thanks to [Laksika Tharmalingam](https://www.kaggle.com/uom190346a) for creating and sharing this valuable dataset.

---

## **👤 Author**
**Eljouini Mohamed Iyed**