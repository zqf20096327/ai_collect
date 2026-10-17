<h1 align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=Audiowide&weight=700&size=80&duration=3000&pause=1000&color=00F0FF&center=true&vCenter=true&width=800&height=120&lines=J.A.R.V.I.S.;WELCOME+HOME+SIR" alt="Typing SVG" />
  </a>
</h1>

  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



<p align="justify">
<a href="https://jarvis-byte-me.vercel.app/">JARVIS</a> is an AI-powered personal assistant designed to bridge the gap between intelligence and execution. Unlike conventional assistants that stop at conversation, JARVIS extends its capabilities into your local operating system - opening applications, managing system controls, navigating the web, and responding visually to the world around it.

At its core, JARVIS is a modular, locally-aware AI system that combines cloud-level reasoning with on-device control. It listens, understands, decides, and does things, bringing the concept of a truly functional AI assistant closer to reality.
</p>
<hr>
<img width="1914" height="903" alt="image" src="https://github.com/user-attachments/assets/1cf975e5-bc1f-46e3-ae5f-7501f6fdfd2e" />
<hr>
<img width="1916" height="902" alt="image" src="https://github.com/user-attachments/assets/c711ba46-bef6-4a73-8e00-674ddb784f94" />
<hr>

##  Tech Stack

<div align="center">

| **Category**              | **Technologies** |
|---------------------------|:-----------------|
| **Programming Languages** | [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/) |
| **AI / LLM**              | [![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge)](https://langchain.com/) [![Groq](https://img.shields.io/badge/Groq-000000?style=for-the-badge)](https://groq.com/) [![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/) [![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/) [![Mistral](https://img.shields.io/badge/Mistral-F26522?style=for-the-badge)](https://mistral.ai/) |
| **Vision & Speech**       | [![Google Gemini](https://img.shields.io/badge/Gemini%20Vision-8E75B2?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/) [![OpenAI](https://img.shields.io/badge/GPT--4V-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/) [![Edge TTS](https://img.shields.io/badge/Edge%20TTS-0078D7?style=for-the-badge)](https://github.com/rany2/edge-tts) |
| **Memory / Vector DB**    | [![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6F00?style=for-the-badge)](https://docs.trychroma.com/) |
| **Web Search**            | [![Serper](https://img.shields.io/badge/Serper-4285F4?style=for-the-badge)](https://serper.dev/) |
| **Backend Framework**     | [![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/) |
| **Frontend Framework** | [![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)](https://react.dev/) [![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/docs/) [![Framer Motion](https://img.shields.io/badge/Framer%20Motion-0055FF?style=for-the-badge)](https://www.framer.com/motion/) |
| **Local Automation**      | [![os](https://img.shields.io/badge/os-808080?style=for-the-badge)](https://docs.python.org/3/library/os.html) [![subprocess](https://img.shields.io/badge/subprocess-4B4B4B?style=for-the-badge)](https://docs.python.org/3/library/subprocess.html) [![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-3776AB?style=for-the-badge)](https://pyautogui.readthedocs.io/en/latest/) |
| **Tools**                 | [![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/doc) [![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)](https://code.visualstudio.com/docs) |
| **Deployment / Runtime**  | [![Uvicorn](https://img.shields.io/badge/Uvicorn-121212?style=for-the-badge)](https://www.uvicorn.org/) [![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)](https://vitejs.dev/) |

</div>

---

## 🏗️ System Architecture

JARVIS operates on a **modular architecture** designed for **speed, privacy, and extensibility**.  
The system is divided into three core components: the **AI Brain Layer**, **Vision Module**, and **Local Agent**.

```mermaid
graph TD
    User([👤 User Input]) --> Brain
    Brain[🧠 AI Brain Layer] -->|Text Query| Chat[💬 Response]
    Brain -->|Visual Data| Vision[👁️ Vision Module]
    Brain -->|System Command| Agent[⚙️ Local Agent]
    
    Vision --Description--> Brain
    Agent --Action--> OS[💻 System / OS]
```

## 🧩 Core Modules

JARVIS is built on three primary components that work together to understand, analyze, and execute user commands.

---

### 🧠 1. AI Brain Layer
**The intelligence core that thinks, decides, and orchestrates actions.**

**Powered by:** LangChain (Groq, OpenAI, Gemini, Mistral)

The AI Brain acts as the **central decision engine**. It interprets user input, understands intent, and determines the appropriate course of action.

**Responsibilities:**
1. **Natural Language Understanding:** Interprets complex and conversational queries.
2. **Decision Engine:** Chooses whether to respond, analyze visuals, or execute a command.
3. **Task Routing:** Directs requests to the Vision Module or Local Agent.

---

### 👁️ 2. Vision Module
**The perception system that allows JARVIS to “see” and understand images.**

**Powered by:** Multimodal LLMs (Google Gemini Vision / OpenAI GPT-4V)

This module converts visual input into meaningful descriptions and insights that the AI Brain can process and reason about.

**Capabilities:**
1. **Image-to-Text Conversion:** Generates accurate image descriptions.
2. **Visual Question Answering (VQA):** Answers questions based on image content.
3. **Scene Analysis:** Identifies objects, context, and relationships.

---

### ⚙️ 3. Local Agent
**The action layer that interacts directly with the operating system.**

**Runs on:** Local Host (Low latency & secure)

The Local Agent transforms decisions into **real system actions**, enabling JARVIS to control applications and system settings.

**Functions:**
1. **Application Control:** Open, close, and manage programs.
2. **System Adjustments:** Modify volume, brightness, and power settings.
3. **Web Automation:** Launch websites and perform browser tasks.

---
## 📂 Project Structure

```text
JARVIS/
├── backend/                        # Main Server & Logic
│   ├── brain/                      # AI Intelligence Modules
│   │   ├── app.py                  # Core Brain application logic
│   │   ├── database.py             # Database operations
│   │   ├── llm_services.py         # Connects to LLM (LangChain)
│   │   ├── memory_manager.py       # Handles chat history & context
│   │   ├── memory_services.py      # Memory storage and retrieval
│   │   └── web_search.py           # Web search integration
│   ├── routers/                    # API Endpoints
│   ├── chroma_db/                  # Vector Database for Long-term memory
│   ├── main.py                     # FastAPI Entry Point (Run this to start)
│   ├── auth.py                     # User Authentication & Security
│   ├── requirements.txt            # Python Dependencies
│   └── users.db                    # User database
│
├── frontend/                       # User Interface (React + Vite)
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatInterface.tsx   # Main chat window
│   │   │   ├── Login.tsx           # Authentication screen
│   │   │   └── Sidebar.tsx         # Chat history navigation
│   │   ├── api.ts                  # Connection to Backend
│   │   ├── App.tsx                 # Main Application Layout
│   │   └── main.tsx                # Frontend Entry Point
│   ├── package.json
│   └── vite.config.ts
│
├── local_agent/                    # OS Control Source Code
│   ├── agent.py                    # Websocket client for OS commands
│   └── os_controller.py            # Logic to open apps/control system
│
├── Jarvis_Agent.exe                # Compiled Local Agent executable
├── load_test_report.md             # Load test report
└── README.md                       # Project Documentation

```
## 🚀 How to Use JARVIS
Jarvis can be accessed by [the link](https://jarvis-byte-me.vercel.app/). Follow the steps below to access the Local Agent for local device task on Windows.

#### 1️⃣ Download the Agent file
Download the [Jarvis_Agent.exe](https://github.com/AvanishSalunke/JARVIS/raw/refs/heads/main/Jarvis_Agent.exe) file.

#### 2️⃣ Run the Jarvis_Agent.exe file
This can done by clicking on the downloaded exe file or using command terminal

```bash
.\Jarvis_Agent.exe  #or the location of the downloaded file
```
This should open a pop-up to enter your login credentials. Use the same login credentials which you used to log in on the website. 

---
## 🚀 How to Run JARVIS locally
Follow the steps below to run the project locally and use all its features.


#### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/JARVIS.git
cd JARVIS
```
#### 2️⃣ Move to backend directory
```bash
cd backend
```
#### 3️⃣ Create & Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```
#### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
#### 5️⃣ Set Environment Variables
Create a .env file in the root directory and add:

```bash
GROQ_API_KEY=your_groq_api_key
SERPER_API_KEY=your_serper_api_key
```

#### 6️⃣ Run the Backend Server
```python
python main.py
```
#### 7️⃣ Start frontend
Start a new terminal and move to frontend
```bash
cd frontend
```
Install dependencies and run
```bash
npm install
npm run dev
```


---
## 🤝 Contributors

- [Avanish Salunke](https://github.com/AvanishSalunke)
- [Pratyush Rao](https://github.com/PratyushRao)
- [Purvasha Singh](https://github.com/purrvax)
- [Kavish Nasta](https://github.com/kavishnasta)
