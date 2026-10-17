# 📰 Fake News Detection using Machine Learning

A machine learning project that classifies news articles as **Real** or **Fake** using Natural Language Processing (NLP) techniques and multiple supervised learning algorithms.

---

## 📌 Project Overview

The spread of fake news on digital platforms has become a major concern. This project applies **Natural Language Processing (NLP)** and **Machine Learning** to automatically identify whether a news article is real or fake.

The project compares the performance of multiple machine learning models and selects the best-performing model based on evaluation metrics.

---

## 🚀 Features

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Word Cloud Visualization
- TF-IDF Vectorization
- Train-Test Split
- Multiple Machine Learning Models
- Model Performance Comparison
- Confusion Matrix Visualization
- Classification Report
- Custom News Prediction
- Save Trained Model using Joblib

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- WordCloud
- Joblib
- Google Colab

---

## 🤖 Machine Learning Models

The following models were trained and evaluated:

- Logistic Regression
- Multinomial Naive Bayes
- Random Forest Classifier
- Linear Support Vector Machine (SVM)

---

## 📊 Evaluation Metrics

Each model was evaluated using:

- Accuracy Score
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Classification Report

The best-performing model was selected based on its overall accuracy and classification performance.

---

## 📁 Project Structure

```
Fake-News-Detection/
│
├── Fake_News_Detection.ipynb
├── README.md
├── fake.csv
├── true.csv
├── svm_fake_news_model.pkl
├── images

```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Aakansh-saroj-05/Fake-News-Detection.git
```

Move into the project directory

```bash
cd Fake-News-Detection
```

Install the required libraries

```bash
pip install pandas numpy matplotlib scikit-learn wordcloud joblib
```

Run the notebook

```bash
jupyter notebook
```

or open it in **Google Colab**.

---

## 📈 Workflow

1. Load Dataset
2. Data Cleaning
3. Exploratory Data Analysis
4. TF-IDF Vectorization
5. Train-Test Split
6. Train Multiple ML Models
7. Evaluate Each Model
8. Compare Model Performance
9. Visualize Results
10. Predict Custom News
11. Save Best Model

---

## 🔍 Example Prediction

Input:

```
Scientists discover a new treatment that reduces cancer risk.
```

Output:

```
🟢 Real News
```

---

## 🌱 Future Improvements

- Deep Learning (LSTM)
- BERT-based Fake News Detection
- Streamlit Web Application
- Flask REST API
- Multilingual Fake News Detection
- Real-time News Verification

---

## 📷 Project Results

The project includes:

- Word Clouds
  
  <img width="712" height="382" alt="image" src="https://github.com/user-attachments/assets/8d2a7f1d-a48f-47de-a69d-0f49549de399" />
  <img width="707" height="377" alt="image" src="https://github.com/user-attachments/assets/269462cc-fd6b-4379-875f-72b2e27175df" />

- Model Accuracy Comparison

  <img width="707" height="528" alt="image" src="https://github.com/user-attachments/assets/d64b8b58-2471-4643-b9aa-b6ccbfc9bae2" />

- Confusion Matrix

  <img width="638" height="562" alt="image" src="https://github.com/user-attachments/assets/3cf7483b-f18b-41cc-8c44-77f39fc4dd68" />

- Classification Reports

  <img width="678" height="358" alt="image" src="https://github.com/user-attachments/assets/1db601aa-bbad-4d5a-8367-139eccb6b08e" />

---

## 👩‍💻 Author

**Aakansha Saroj**

Feel free to connect with me and explore more of my projects!

⭐ If you found this project useful, consider giving it a star.
