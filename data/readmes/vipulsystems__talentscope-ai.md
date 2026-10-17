<p align="center">

<img src="frontend/src/assets/HV.png" width="80" />

</p>

<h1 align="center"> TalentScope AI</h1>

<p align="center">

AI-powered recruitment platform for smarter hiring decisions

</p>

<p align="center">

<img src="https://img.shields.io/badge/Frontend-React-blue" />

<img src="https://img.shields.io/badge/Backend-Flask-green" />

<img src="https://img.shields.io/badge/Database-MongoDB-brightgreen" />

</p>

**TalentScope AI** is an AI-powered recruitment and interview analysis platform designed to help recruiters identify the best candidates and assist candidates in improving their interview performance.

---

## Overview

TalentScope AI combines **machine learning, NLP, and video analysis** to evaluate candidates across multiple dimensions:

* Facial emotion detection

* Speech and tone analysis

* Sentiment analysis

* Resume-to-job matching

* Recruiter analytics dashboard

---

## Features

### Recruiter

* Create and manage job postings

* View applicants and filter candidates

* Analyze interview performance

* Access detailed analytics and reports

* Schedule interviews

### Candidate

* Browse and apply for jobs

* Upload resume

* Attend video interviews

* Practice interviews with AI feedback

* View performance analysis

---

## Screenshots

### 🔹 Home Page

![Home](public/images/auth-bg.png)

### 🔹 Recruiter Dashboard

![Recruiter Dashboard](public/images/recruiter-dashboard.png)

### 🔹 Candidate Dashboard

![Candidate Dashboard](public/images/candidate-dashboard.png)

### 🔹 Interview Analysis

![Analysis](public/images/analysis.png)

---

## Tech Stack

### 🔹 Frontend

* React (Vite)

* Redux Toolkit

* Tailwind CSS

* Axios

### 🔹 Backend

* Flask

* MongoDB (PyMongo)

* JWT Authentication

### 🔹 AI / ML

* DeepFace (emotion detection)

* Transformers (sentiment analysis)

* SpeechRecognition (STT)

* Parselmouth (speech prosody)

* Scikit-learn (resume matching)

---

## Project Structure

```

TalentScope-AI/

│

├── backend/

│ ├── app/

│ ├── routes/

│ ├── models/

│ ├── services/

│ └── utils/

│

├── frontend/

│ ├── src/

│ │ ├── components/

│ │ ├── features/

│ │ ├── pages/

│ │ ├── redux/

│ │ └── api/

│

└── README.md

```

---

## Setup Instructions

### 🔹 1. Clone Repository

```

git clone https://github.com/vipulsystems/talentscope-ai.git

cd talentscope-ai

```

---

### 🔹 2. Backend Setup

```

cd backend

python -m venv venv

venv\Scripts\activate # Windows

# source venv/bin/activate # Mac/Linux

pip install -r requirements.txt

```

#### Create `.env` file:

```

MONGO_URI=mongodb://localhost:27017/interview_db

JWT_SECRET_KEY=your_secret_key

SECRET_KEY=your_secret_key

FLASK_ENV=development

```

#### Run backend:

```

flask run

```

Backend runs at:

```

http://127.0.0.1:5000

```

---

### 🔹 3. Frontend Setup

```

cd frontend

npm install

```

#### Create `.env` file:

```

VITE_API_URL=http://127.0.0.1:5000

```

#### Run frontend:

```

npm run dev

```

Frontend runs at:

```

http://localhost:5173

```

---

## Authentication

* JWT-based authentication

* Role-based access:

* Candidate

* Recruiter

---

## API Base URL

```

http://127.0.0.1:5000/api/v1

```

---

## Example Features in Action

* Upload resume → get similarity score

* Upload interview video → get:

* emotion score

* speech score

* sentiment score

* Recruiter sees:

* overall candidate score

* recommendation (Strong Fit / Needs Review)

---

## Future Enhancements

* Live interview (WebRTC)

* AI question generation

* Resume parser improvements

* Candidate ranking system

* Deployment (Docker + Cloud)

---

## Author

Built by Vipul Paighan

---

## License

This project is licensed under the MIT License.

---

*TalentScope AI — Smarter Hiring with AI*
