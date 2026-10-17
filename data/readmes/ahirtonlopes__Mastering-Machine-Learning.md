# Mastering Machine Learning

Open courseware covering essential Machine Learning algorithms and applied projects, from data preprocessing to ensemble methods and beyond.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3+-orange?style=flat-square&logo=scikit-learn)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## What you'll learn

- Exploratory data analysis and feature preprocessing
- Evaluate models with the right metrics (accuracy, F1, AUC, confusion matrix)
- Implement and compare classical ML algorithms from scratch
- Handle imbalanced datasets
- Apply dimensionality reduction with PCA
- Build ensemble models (Random Forest, XGBoost)
- Mine association rules with Apriori

## Prerequisites

| Topic | Level |
|---|---|
| Python | Basic |
| Pandas & NumPy | Basic |
| Statistics fundamentals | Basic |

---

## Contents

All notebooks are in the `Projetos/` folder. Datasets are in `Bases/`.

| # | Notebook | Topics |
|---|---|---|
| 01 | `Demo1_Algoritmo_Genetico.ipynb` | Genetic Algorithms, hyperparameter search |
| 02 | `Demo2_RegressaoLinear_Boston.ipynb` | Linear Regression, Boston Housing |
| 03 | `Demo3_RF_Churn.ipynb` | Random Forest, Churn Prediction |
| 04 | `Demo4_Comparacao_Metricas.ipynb` | Metrics comparison, model evaluation |
| 05 | `Demo5_KNN_Elbow.ipynb` | KNN, elbow method |
| 06 | `Demo6_KNN_Telco.ipynb` | KNN applied to Telco dataset |
| 07 | `Demo7_K_Means_Clustering.ipynb` | K-Means clustering |
| 08 | `Demo8_Kmeans_Crime_data.ipynb` | K-Means on crime data |
| 09 | `Demo9_Apriori_Movies.ipynb` | Association rules, movie recommendations |
| 10 | `Demo10_RegressaoLogistica.ipynb` | Logistic Regression |
| 11 | `Demo11_Naive_Bayes.ipynb` | Naive Bayes classifier |
| 12 | `Demo12_PCA.ipynb` | Principal Component Analysis |
| 13 | `Demo13_PCA_SVM.ipynb` | PCA + Support Vector Machines |
| 14 | `Demo14_Ensemble_Techniques.ipynb` | Bagging, Boosting, Stacking |
| 15 | `Demo15_XGBoost.ipynb` | XGBoost, gradient boosting |
| 16 | `Demo16_Datasets_Desbalanceados.ipynb` | Imbalanced datasets, SMOTE |

---

## Getting Started

**Option 1 — Google Colab (recommended)**

Open any notebook directly on GitHub and click **Open in Colab** at the top of the file.

**Option 2 — Local**

```bash
git clone https://github.com/ahirtonlopes/Mastering-Machine-Learning.git
cd Mastering-Machine-Learning
python -m venv .venv && source .venv/bin/activate
pip install scikit-learn pandas numpy matplotlib xgboost imbalanced-learn jupyter
jupyter notebook
```

---

## Suggested Learning Path

**Beginner** → Demos 2, 5, 7, 10, 11  
**Intermediate** → Demos 3, 4, 6, 8, 12, 13  
**Advanced** → Demos 1, 9, 14, 15, 16

---

## Author

**Prof. Dr. Ahirton Lopes** · [LinkedIn](https://linkedin.com/in/ahirtonlopes) · [Google Scholar](https://scholar.google.com/citations?user=1SQDVrwAAAAJ)

Contributions are welcome — open an issue or submit a pull request.

## License

[MIT](LICENSE.md)
