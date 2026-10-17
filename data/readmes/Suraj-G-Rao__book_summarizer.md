# 📚 Marketing Blurb & Summary Generator

This is a **Streamlit-based application** that allows users to upload **PDF documents** and generate **marketing blurbs and summaries** using **Groq LLM (LLaMA models)** and **LangChain**.

The application uses **Google Gemini embeddings** to create a **FAISS vector store** for document retrieval and **Groq LLM** for generating engaging content summaries and marketing blurbs.

---

##   SCREENSHOT 
![image](https://github.com/user-attachments/assets/efc60377-b49e-4684-83af-02cd6f7c73c9)

## DEMO VIDEO : 
https://drive.google.com/file/d/1kuwBaytfY5vyr-nh5uieBrPbYdQ1dT9F/view?usp=sharing

## REPORT LINK :
https://docs.google.com/document/d/1WK0YJ1I2V8qv6xXcGUqf5lMAA0BKxZRM/edit?usp=sharing&ouid=108340172359201221784&rtpof=true&sd=true

## 🌟 Features

- Upload multiple PDF files.
- Process PDFs to extract content and split into chunks.
- Use **Google Gemini embeddings** for document vectorization.
- Query uploaded documents and generate **marketing blurbs or content summaries** using **Groq's LLaMA models**.
- Interactive, user-friendly **Streamlit interface**.
- Logos for **NIE University, IVIS Labs, and PULSE** displayed at the top.

---

## 🛠️ Tech Stack

- **Streamlit** - Frontend UI
- **LangChain** - Document processing and retrieval
- **Groq LLM** - LLaMA3-8B & LLaMA3-70B models for text generation
- **Google Gemini** - Embeddings for document retrieval
- **FAISS** - Vector storage
- **Python 3.9+**

---

## ⚙️ Installation and Setup

### 1️⃣ Clone the Repository

git clone <repository_url>  
cd <repository_folder>

---

### 2️⃣ Create Virtual Environment

python -m venv venv

For Linux/macOS:  
source venv/bin/activate

For Windows:  
venv\Scripts\activate

---

### 3️⃣ Install Dependencies

pip install -r requirements.txt

---

### 4️⃣ Add API Keys to `.env` File

Create a `.env` file in the project root folder with the following content:

GROQ_API_KEY=your_groq_api_key_here  
GOOGLE_API_KEY=your_google_api_key_here

---

### 🔑 How to Get API Keys

#### 📍 Google API Key (Gemini)

1. Go to: https://aistudio.google.com/app/apikey  
2. Sign in with your Google account.  
3. Generate a new API Key.  
4. Copy and paste the key into your `.env` file as:

GOOGLE_API_KEY=your_google_api_key_here

---

#### 📍 Groq API Key

1. Visit: https://console.groq.com/keys  
2. Sign in or create an account.  
3. Navigate to the **API Keys** section.  
4. Create a new API Key.  
5. Copy and paste the key into your `.env` file as:

GROQ_API_KEY=your_groq_api_key_here

---

### 🚀 Run the Application

streamlit run app.py

---

## 🏷️ Directory Structure

├── app.py                        # Main Streamlit application  
├── uploaded_pdfs                 # Directory for storing uploaded PDFs  
├── requirements.txt              # Required Python packages  
├── .env                          # API keys (not included in repo)  
├── README.md                      # Project documentation  
├── logos                          # Logos for NIE, IVIS, PULSE  
│   ├── NIE_University.png  
│   ├── IVIS_logo.png  
│   ├── PULSE LOGO.png  
└── ...

---
Developed By Suraj G Rao
