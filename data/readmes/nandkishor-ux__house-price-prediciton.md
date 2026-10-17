#  House Price Prediction

> A regression-based Machine Learning model that predicts property prices based on house features — built end-to-end in Python with a saved deployable model.

[![Python](https://img.shields.io/badge/Python-3.x-blue)](https://python.org)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange)](https://scikit-learn.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter)](https://jupyter.org)
[![Model](https://img.shields.io/badge/Model-Saved%20.pkl-green)]()

---

## 📌 Project Overview

This project builds a complete ML pipeline to estimate house prices based on property features such as area, number of bedrooms, bathrooms, stories, parking, and amenities. The final trained model is exported as a `.pkl` file for deployment.

---

## 🔬 What I Did

- Loaded and cleaned the **Housing dataset** with feature engineering
- Performed **Exploratory Data Analysis (EDA)** — correlation analysis, distribution plots
- Encoded categorical variables (furnishing status, main road access, etc.)
- Trained and evaluated multiple regression models
- Exported the best model as **`final_house_price_model.pkl`** using Joblib

---

## 📁 Repository Structure

```
house-price-prediciton/
│
├── house_price_prediction_1.ipynb      # Main notebook (EDA + Modeling)
├── Housing.csv                          # Dataset
├── Housing-checkpoint.csv               # Checkpoint backup
├── final_house_price_model.pkl          # Saved trained model
└── README.md
```

---

## ⚙️ Tech Stack

| Category | Tools |
|---|---|
| Language | Python 3.x |
| ML Library | Scikit-learn |
| Data | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Model Export | Joblib |
| Environment | Jupyter Notebook |

---

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/nandkishor-ux/house-price-prediciton.git
cd house-price-prediciton

# 2. Install dependencies
pip install pandas numpy scikit-learn matplotlib seaborn jupyter joblib

# 3. Open the notebook
jupyter notebook house_price_prediction_1.ipynb
```

### To use the saved model directly:

```python
import joblib
import pandas as pd

model = joblib.load('final_house_price_model.pkl')

# Example prediction
sample = pd.DataFrame([{
    'area': 7420, 'bedrooms': 4, 'bathrooms': 2,
    'stories': 3, 'mainroad': 1, 'guestroom': 0,
    'basement': 0, 'hotwaterheating': 0, 'airconditioning': 1,
    'parking': 2, 'prefarea': 1, 'furnishingstatus': 1
}])

predicted_price = model.predict(sample)
print(f"Estimated Price: ₹{predicted_price[0]:,.0f}")
```

---

## 💡 Features Used

| Feature | Description |
|---|---|
| area | Total area in sq ft |
| bedrooms | Number of bedrooms |
| bathrooms | Number of bathrooms |
| stories | Number of floors |
| parking | Parking spaces available |
| airconditioning | AC present (1/0) |
| furnishingstatus | Furnished / Semi / Unfurnished |

---

## 👤 Author

**Nand Kishor Kumar**
- GitHub: [@nandkishor-ux](https://github.com/nandkishor-ux)
- Email: nandkishor0720@gmail.com
