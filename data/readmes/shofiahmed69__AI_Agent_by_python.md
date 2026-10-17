# 🎙️ Voice AI Agent (Streamlit + Groq API)

A simple **Voice AI Agent** built using **Python** and **Streamlit**, powered by the **Groq API**. This application allows users to ask questions about **people, software, organizations, and weather** through a conversational interface, with support for voice-style interaction logic.

---

## 🚀 Features

* 🧠 AI-powered question answering using **Groq LLMs**
* 🎤 Voice-style conversational agent interface
* 🌦️ Weather information queries
* 👤 General knowledge about people and organizations
* ⚡ Fast inference using Groq API
* 🖥️ Clean and interactive UI with Streamlit

---

## 🛠️ Tech Stack

* **Python 3.9+**
* **Streamlit** – Frontend & UI
* **Groq API** – Large Language Model inference
* **Matplotlib / NumPy** – (if used for visualizations)
* **Tkinter (optional)** – For additional UI logic (if applicable)

---

## 📸 Application Preview

<img width="1908" height="889" alt="Screenshot 2026-01-16 001001" src="https://github.com/user-attachments/assets/35f3f55d-b7b9-4d5c-8dd4-1f876d8e871c" />


---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/voice-ai-agent.git
cd voice-ai-agent
```

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Groq API Configuration

1. Create an account at **Groq**
2. Generate your **Groq API Key**
3. Enter the API key in the Streamlit sidebar when the app starts

> ⚠️ Keep your API key private. Do not hardcode it in public repositories.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The app will open in your browser (usually at `http://localhost:8501`).

---

## 📂 Project Structure

```text
voice-ai-agent/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── assets/                # Images or icons (optional)
└── utils/                 # Helper functions (if any)
```

---

## 💬 Example Queries

* "Who is Donald Trump?"
* "What is the weather in New York?"
* "Explain what Streamlit is"
* "Tell me about Google"

---

## 🧠 How It Works

1. User enters a query (text/voice-style input)
2. Streamlit sends the query to the **Groq API**
3. Groq LLM processes the request
4. The AI-generated response is displayed in the chat interface

---

## 🔮 Future Improvements

* 🎧 Real-time speech-to-text (STT)
* 🔊 Text-to-speech (TTS) output
* 🌍 Live weather API integration
* 🧠 Memory-based conversations
* 🚀 Deployment on Streamlit Cloud

---

## 📜 License

This project is for **educational and learning purposes**. You may modify and use it freely.

---

## 👨‍💻 Author

**Developed by:** *Shofi Ahmed*
**Built with:** Python, Streamlit & Groq API

---

⭐ If you like this project, consider giving it a star on GitHub!
