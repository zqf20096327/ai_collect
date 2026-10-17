# AnonymousThinker 🧠 — v2.1

AnonymousThinker is a premium AI reasoning platform designed to provide structured, logical responses with a specialized focus on defending and explaining Islamic principles through reason and scholarly knowledge.

---

## ✨ What's New in v2.1

### 🆕 Feature Upgrades

| Feature | Description |
|---|---|
| **📌 Pin Conversations** | Pin important conversations to the top of the sidebar |
| **🗄️ Archive Conversations** | Archive chats instead of deleting them (right-click menu) |
| **🔍 Sidebar Search** | Search conversations by title or content |
| **👍👎 Message Reactions** | Rate AI responses as helpful or not helpful |
| **📤 Export Conversation** | Download full conversation as a Markdown file |
| **📊 Word Count** | AI responses show word count for quick reference |
| **🔢 Character Counter** | Live character count in input (max 4000 chars) |
| **🖱️ Right-Click Context Menu** | Right-click any conversation for rename, pin, archive, export, delete |
| **📊 Response Counter** | Topbar shows number of AI responses in current chat |
| **🚀 Improved Error Toast** | Cleaner error display, auto-dismisses after 5s |

---

## ✨ All Features

- **Dual-Model Comparative Analysis**: Compare responses from a personal logic model (Llama 3.1 8B) and a powerful reasoning model (DeepSeek-R1-70B) side-by-side.
- **Sovereign AI Hub**: A centralized command center for administrators to define the AI's persona, logical framework, and core strategy.
- **Knowledge Base (RAG)**: Ground AI responses in scholarly Islamic knowledge by uploading PDFs and text files globally.
- **Admin-Restricted Training**: Only authorized developers can train the AI or modify its core directives.
- **Glassmorphic UI**: A premium, modern interface with dark mode, fluid animations, and a focus on readability.

---

## 🛠️ Tech Stack

- **Frontend**: React.js, React Router, Axios, Vanilla CSS (Standardized Design System).
- **Backend**: Node.js, Express, MongoDB (Mongoose), JWT Auth.
- **AI Infrastructure**:
  - **Inference**: Groq API & Hugging Face Serverless Inference.
  - **Reasoning Models**: Llama-3.1-8B-Instruct & Llama-3.3-70B-Versatile.
  - **Logic Engine**: Custom NLP pipeline for PDF parsing and RAG (Retrieval Augmented Generation).

---

## 🚀 Local Setup Guide

### 1. Prerequisites
- **Node.js** (v18+)
- **npm** or **yarn**
- **MongoDB** (Local instance or Atlas URI)

### 2. Clone the Repository
```bash
git clone <repository-url>
cd AnonymousThinker
```

### 3. Backend Setup
```bash
cd backend
npm install
cp .env.example .env
# Edit .env with your credentials
npm run dev
```

### 4. Frontend Setup
```bash
cd ../frontend
npm install
npm start
```

---

## 🛡️ Administrative Configuration

### Promoting Your Account to Admin
```bash
node scripts/makeAdmin.js your-email@example.com
```

### Default Admin Login
Configure `ADMIN_EMAIL` and `ADMIN_PASSWORD` in your `.env`.

---

## 🖱️ New UX: Right-Click Context Menu

Right-click any conversation in the sidebar to access:
- **Rename** — Edit the conversation title inline
- **Pin to top** / **Unpin** — Keep important conversations accessible
- **Export as .md** — Download the full conversation as a Markdown file
- **Archive** — Hide the conversation without deleting it
- **Delete** — Permanently remove the conversation

---

## 👍👎 Message Reactions

Each AI response now shows thumbs up/down buttons. Click to rate:
- **👍 Helpful** — Marks the response as useful
- **👎 Not helpful** — Marks the response as needing improvement

Reactions are stored per-message in the database and can be used to track AI quality over time.

---

## 🔍 Conversation Search

Click the search icon (🔍) in the sidebar header to activate search. Type to filter conversations by:
- Conversation title
- Last message preview

---

## 📚 Global Knowledge Training

1. Login as Admin
2. Click **"Train AI"** in the sidebar
3. Upload PDFs in the **Upload Zone**
4. Update the **"Core Logic & Strategy"** textarea
5. Click **"Commit Changes to Core"**

---

## 📜 License
MIT License - Developed for Sovereign Thought Analysis.

> *"I am AnonymousThinker, an AI to understand different thoughts and to create a conclusion from them."*