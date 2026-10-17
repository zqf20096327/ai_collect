# AI Resume Screening System

An intelligent **Machine Learning web application** that analyzes uploaded resumes and predicts the most suitable job role for the candidate using Natural Language Processing (NLP).

The system extracts text from resumes, processes it using TF-IDF vectorization, and uses a trained classification model to predict the most relevant job category.

---

## 🚀 Live Demo

Deployed using **Streamlit + Render**

```
https://resume-screening-ml-rkwj.onrender.com
```

---

# 📌 Features

* 📄 Upload Resume in **PDF format**
* 🔍 Automatically **extracts resume text**
* 🧹 Cleans and preprocesses the text
* 🧠 Uses **Machine Learning model** for job role prediction
* 📊 Displays **prediction confidence scores**
* 📈 Shows **top prediction probabilities using charts**
* 🌐 Deployed online using **Render**

---

# 🛠 Tech Stack

### Frontend

* Streamlit

### Backend / ML

* Python
* Scikit-learn
* TF-IDF Vectorizer
* Logistic Regression

### Libraries Used

* pandas
* scikit-learn
* pdfplumber
* streamlit
* pickle

### Deployment

* Render

---

# 🧠 Machine Learning Workflow

```
Dataset (CSV)
      ↓
Data Preprocessing
      ↓
Feature Engineering
      ↓
TF-IDF Vectorization
      ↓
Model Training
      ↓
Pickle Model Files
      ↓
Streamlit Web Application
      ↓
Resume Upload → Prediction
```

---

# 📂 Project Structure

```
resume-screening-ml
│
├── dataset
│   └── candidate_job_role_dataset.csv
│
├── model
│   ├── tfidf.pkl
│   ├── clf.pkl
│   └── encoder.pkl
│
├── app.py
├── train_model.py
├── requirements.txt
├── Procfile
└── README.md
```

---

# ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/resume-screening-ml.git
cd resume-screening-ml
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Train the model

```
python train_model.py
```

This will generate:

```
model/tfidf.pkl
model/clf.pkl
model/encoder.pkl
```

### 4️⃣ Run the application

```
streamlit run app.py
```

The app will open at:

```
http://localhost:8501
```

---

# 📊 Model Details

* **Algorithm Used:** Logistic Regression
* **Feature Extraction:** TF-IDF Vectorization
* **Target Variable:** Job Role
* **Input Features:** Skills, Qualification, Experience Level

---

# 🌐 Deployment

This project is deployed using **Render**.

Deployment steps:

1. Push project to GitHub
2. Create a new **Web Service** on Render
3. Connect the repository
4. Add build and start commands

**Build Command**

```
pip install -r requirements.txt
```

**Start Command**

```
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

---

# 🔮 Future Improvements

* Resume **skill extraction using NLP**
* **Top 3 job recommendations**
* Resume **ATS score calculation**
* Resume vs **Job Description matching**
* Deep Learning models like **BERT**

---

# 👨‍💻 Author

**Karthik Chilumula**

B.Tech CSE Student
Aspiring Software Developer | Machine Learning Enthusiast

GitHub:

```
https://github.com/KarthikChilumula685
```

---

# ⭐ Support

If you found this project useful:

⭐ Star this repository
🍴 Fork it and build your own improvements

---

“Turning raw resumes into intelligent insights.”
