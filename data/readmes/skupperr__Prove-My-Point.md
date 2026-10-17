<div align="center">

# 🧠 Prove My Point

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](https://choosealicense.com/licenses/mit/)
[![Python 3.11+](https://img.shields.io/badge/Python--3.11+-backend-blue?style=flat-square&logo=python)](https://www.python.org/downloads/)
[![Vite + React](https://img.shields.io/badge/Vite_+_React-frontend-purple?style=flat-square&logo=react)](https://vitejs.dev/)

> Back your arguments with facts, not opinions.

**Prove My Point** is a full-stack AI-powered research assistant designed to help users back their arguments with reliable, science-backed information from real research papers.

[prove-my-point.vercel.app](https://prove-my-point.vercel.app)

![Demo Screenshot](./Frontend/public/preview.png)

</div>

## 🚀 Features

- 📚 **Academic Research Only**: Sources include PubMed, arXiv, Core, CrossRef and OpenAlex.
- 🤖 **Intelligent RAG Answering**: Advanced Retrieval-Augmented Generation analyzes papers and extract precise answers.
- 🔗 **Cited Sources**: All responses include links to the original research papers.
- 🧵 **Personal History**: Secure access to your question and answer history.
- 🌌 **Beautiful UX**: Clean dark mode UI with fast, responsive interactions.


## 🛠️ Tech Stack


### Frontend
[![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&color=2d2d2d)](https://react.dev/)
[![JavaScript](https://img.shields.io/badge/javascript-61DAFB?style=for-the-badge&logo=javascript&color=2d2d2d)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&color=2d2d2d)](https://vitejs.dev/)
[![Clerk](https://img.shields.io/badge/Clerk-6C47FF?style=for-the-badge&logo=clerk&color=2d2d2d)](https://clerk.dev/)
[![Firebase](https://img.shields.io/badge/Firebase-ffca28?style=for-the-badge&logo=firebase&color=2d2d2d&logoColor=e82309)](https://firebase.google.com/)
[![Vercel](https://img.shields.io/badge/Vercel-ffca28?style=for-the-badge&logo=vercel&color=2d2d2d)](https://vercel.com/)

### Backend
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&labelColor=2d2d2d)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&color=2d2d2d)](https://fastapi.tiangolo.com/)
[![LangChain](https://img.shields.io/badge/LangChain-009688?style=for-the-badge&logo=langchain&color=2d2d2d)](https://www.langchain.com/)
[![Google Cloud](https://img.shields.io/badge/GCP-4285F4?style=for-the-badge&logo=googlecloud&color=2d2d2d)](https://cloud.google.com/)
[![Firebase](https://img.shields.io/badge/Firebase-ffca28?style=for-the-badge&logo=firebase&color=2d2d2d&logoColor=e82309)](https://firebase.google.com/)
[![Clerk](https://img.shields.io/badge/Clerk-6C47FF?style=for-the-badge&logo=clerk&color=2d2d2d)](https://clerk.dev/)
[![Sentence Transformer](https://img.shields.io/badge/SentenceTransformers-009688?style=for-the-badge&color=2d2d2d)](https://sbert.net/)


## 🔍 How It Works

1. **User submits a question** — e.g., *"What is the universe made of?"*  
2. The **backend** performs **vector search** to retrieve the top 10 most relevant research papers from multiple academic databases (PubMed, arXiv, etc.).  
3. A **Retrieval-Augmented Generation (RAG)** pipeline analyzes and synthesizes information from those papers to generate a clear, factual answer.  
4. The answer is returned along with **proper citations and links** to each source.  
5. If the user is signed in, the question and answer are **securely saved in Firebase** for future reference.

## 🚀 Deployment

- **Frontend:** Deployed on Vercel using Vite + React
- **Backend:** Deployed to Google Cloud Run via Docker
- **Auth & History:** Managed with Clerk + Firebase

## 👥 Who Is It For?

- **🎓 Students & Researchers**: Get credible citations for academic work.
- **🎙️ Creators & Debaters**: Reinforce claims with real research.
- **🤔 Curious Minds**: Explore big questions and get factual answers.

---

## 📁 Project Structure

```
Prove-My-Point/
├── Backend/                 # FastAPI backend (with Firebase)
│   ├── src/
│   │   ├── ai_generator/
│   │   ├── routes/
|   |   |     └── request_manager.
│   │   ├── firebase_config.py
│   │   ├── utils.py
│   │   ├── app.py
│   │   ├── firebase-key.json
|   |   └── .env
|   ├──requirements.txt
│   └── server.py
│
├── Frontend/                # React + Vite frontend
│   ├── src/
|   |     ├── askAI/
|   |     ├── auth/
|   |     ├── home/
|   |     ├── layout/
|   |     ├── utils/
|   |     |      └── api.js
|   |     ├── App.css
|   |     ├── index.css
|   |     ├── main.jsx
│   ├── public/
|   ├── vercel.json              # Vercel routing config
|   ├── .env
│   └── index.html
│
└── README.md                # This file
```

<!-- ---

## 🧪 Development Setup

### 🔐 Environment Variables

#### Frontend (`Frontend/.env`)
```
VITE_CLERK_PUBLISHABLE_KEY=your-clerk-key
```

#### Backend (`Backend/src/.env`)
```
GOOGLE_APPLICATION_CREDENTIALS=firebase-key.json
CLERK_SECRET_KEY=your-clerk-secret-key
JWT_KEY=your-JWT_KEY
```

Make sure to place your `firebase-key.json` securely in `Backend/src/` and add it to `.gitignore`. -->

<!-- ---

## 📦 Deployment

- **Frontend**: Deployed using [Vercel](https://vercel.com/)
  - Framework: `Vite`
  - Fix 404 issues with `vercel.json` rewrite rule for SPA
- **Backend**: Deployed to [Google Cloud Run](https://cloud.google.com/run)
  - Dockerized FastAPI app with secure secret access -->

---

<!-- ## 🤝 Acknowledgements
- [arXiv](https://arxiv.org/), [PubMed](https://pubmed.ncbi.nlm.nih.gov/), [Semantic Scholar](https://www.semanticscholar.org/)
- [OpenAI](https://openai.com/) – For AI inspiration
- [Firebase](https://firebase.google.com/) – For scalable storage
- [Clerk.dev](https://clerk.dev/) – For authentication tools

--- -->

## 🧠 Future Improvements
<!-- - [] Better mobile experience -->

[Report Bug](https://github.com/skupperr/Prove-My-Point/issues) · [Request Feature](https://github.com/skupperr/Prove-My-Point/issues)

## 📬 Contact

Created with ❤️ by [Asif U. Ahmed](https://github.com/skupperr)
