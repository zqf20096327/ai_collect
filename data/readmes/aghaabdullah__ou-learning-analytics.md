# Open University Learning Analytics (OULA) 🎓📊

A comprehensive data science and machine learning research project analyzing Open University learning data to predict student outcomes and engagement.

## 📖 Overview
In modern educational environments, identifying at-risk students early is crucial for improving retention and success rates. This repository contains the outputs, visualizations, and documentation from an exploratory data analysis (EDA) and predictive modeling pipeline applied to the Open University dataset. By analyzing Virtual Learning Environment (VLE) interactions, assessment scores, and student demographics, this project builds predictive models to estimate student engagement and final outcomes.

## 🎯 Objectives
- **Data Exploration:** Analyze student engagement metrics across different courses and presentation periods.
- **Predictive Modeling:** Compare multiple machine learning models (e.g., XGBoost, Random Forest, Logistic Regression) using Open University anonymized data.
- **Feature Engineering & Importance:** Evaluate and identify the primary drivers (features) that contribute to student success.

## 🛠️ Technology Stack
- **Language:** Python 3.x
- **Libraries:** Pandas, NumPy, Scikit-learn, XGBoost, Matplotlib, Seaborn
- **Environment:** Jupyter Notebook / Google Colab

## 📂 Project Structure
```text
ou-learning-analytics/
├── docs/                 # Walkthrough and architecture documentation
│   └── walkthrough.md    # Detailed guide on the pipeline
├── results/              # Model metrics and performance summaries
│   └── model_comparison_table.csv
├── results/figures/      # Generated plots and visualizations
│   ├── architecture_diagram.png
│   ├── confusion_matrices.png
│   ├── feature_importance.png
│   └── roc_curves.png
└── data/sample/          # Directory for sample/anonymized datasets
```

## 📈 Methodology
1. **Data Preprocessing:** Merged multiple relational tables (`studentAssessment`, `studentInfo`, `studentVle`) to create a unified view of student interactions. Handled missing values and encoded categorical variables.
2. **Exploratory Data Analysis (EDA):** Visualized target distributions and engagement levels over time to spot trends.
3. **Model Training:** Trained multiple classifiers to predict whether a student will Pass, Fail, or Withdraw.
4. **Evaluation:** Evaluated models using accuracy, precision, recall, F1-score, and ROC-AUC metrics. Extracted feature importance to interpret model decision-making.

## 📊 Results & Screenshots
The model comparison, feature importance, and other evaluation metrics demonstrate that early VLE engagement and continuous assessment scores are the strongest predictors of passing the course.

### Architecture Diagram
![Architecture Diagram](results/figures/architecture_diagram.png)

### Model Performance
![ROC Curves](results/figures/roc_curves.png)
![Confusion Matrices](results/figures/confusion_matrices.png)
![Feature Importance](results/figures/feature_importance.png)

## 🗄️ Data Note
The project relies on the **Open University Learning Analytics dataset (OULA)**. Due to GitHub's file size limitations (e.g., `studentVle.csv` is ~450MB), the raw data is not included in this repository. 



## 👨‍💻 Author
**Agha Abdullah**
- GitHub: [@AGHAABDULLAH](https://github.com/AGHAABDULLAH)
## ⚖️ License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
