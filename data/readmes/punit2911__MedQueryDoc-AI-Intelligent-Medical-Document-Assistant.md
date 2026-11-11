# 🩺 MedQueryDoc AI – Intelligent Medical Document Assistant 

**Stop Ctrl+F-ing through medical PDFs. Ask in plain English, get answers from Llama-2.**

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-RAG-1C3C3C)
![Pinecone](https://img.shields.io/badge/Vector%20DB-Pinecone-00B3A4)
![Flask](https://img.shields.io/badge/Flask-Web%20UI-black?logo=flask)
![License](https://img.shields.io/badge/License-GPLv3-green)

<!-- 👇 REPLACE THIS LINE: drag your demo GIF or screenshot into the GitHub editor and it will upload automatically -->
![MedQueryDoc AI demo](https://github.com/user-attachments/assets/YOUR-DEMO-GIF-HERE)
 
> ⚠️ **For educational purposes only. This is not medical advice.**
 
---

## 📌 About the Project

This project is an AI-powered **medical document question-answering system** built using **Large Language Models (LLMs)** and **vector-based information retrieval**. It enables users to ask natural language questions and receive accurate, context-aware answers derived from medical PDF documents.

The system works by loading and splitting PDF documents into smaller chunks, generating vector embeddings using a Hugging Face embedding model, and storing them in **Pinecone**, a scalable vector database. During inference, user queries are matched against relevant document chunks using similarity search, and responses are generated using **LLaMA-2** through a retrieval-augmented generation (RAG) pipeline.

This project demonstrates practical implementation of **LLMs + LangChain + Vector Databases** for real-world AI applications.

### 🔄 How it works

```
PDFs → split into chunks → embeddings → Pinecone
                                          ↓
Your question → similarity search → top chunks → Llama-2 → answer
```

---

## 🧠 Key Features !


* PDF-based medical document ingestion
* Vector similarity search using Pinecone
* Retrieval-Augmented Generation (RAG) pipeline
* Local LLaMA-2 model inference
* Interactive web interface using Flask
* Modular and extensible architecture

---

## 🛠️ Built With

* **Python**
* **LangChain**
* **Flask**
* **Meta LLaMA-2**
* **Pinecone (Vector Database)**
* **Hugging Face Embeddings**

---

## 🚀 Getting Started

Follow the steps below to set up and run the project locally.

---

## ⚙️ Installation Steps 

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/Medical-Chatbot-using-Llama-2.git
cd Medical-Chatbot-using-Llama-2
```

---

### 2️⃣ Create a Virtual Environment (Recommended)

> If Conda is installed:

```bash
conda create -p ./venv python=3.10 -y
conda activate ./venv
```

> Or using Python venv:

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 API Key Setup

Create a `.env` file in the root directory and add your Pinecone credentials:

```ini
PINECONE_API_KEY=your_pinecone_api_key_here
```

> ⚠️ Note: Pinecone no longer requires an environment variable (`PINECONE_API_ENV`) in the new SDK.

---

## 📄 Add Medical Documents

Create a `data/` folder in the project root and add your PDF files:

```
data/
├── medical_doc_1.pdf
├── medical_doc_2.pdf
```

---

## 🧬 Index Documents into Pinecone

Before running the chatbot, index the documents:

```bash
python store_index.py
```

This step:

* Loads PDFs
* Splits text into chunks
* Generates embeddings
* Stores vectors in Pinecone

---

## ▶️ Run the Application

```bash
python app.py
```

Then open your browser and visit:

```
http://localhost:8080
```

---

## 🏗️ Project Architecture

```
├── app.py                 # Flask application
├── store_index.py         # PDF ingestion & vector indexing
├── src/
│   ├── helper.py          # PDF loading, chunking, embeddings
│   ├── prompt.py          # Prompt template
├── model/
│   └── llama-2-7b-chat.ggmlv3.q4_0.bin
├── templates/
│   └── chat.html
├── static/
│   └── style.css
├── data/                  # PDF documents
└── .env
```

---

## 🧠 Model Setup

Download the quantized LLaMA-2 model and place it inside the `model/` directory:

```text
Model: llama-2-7b-chat.ggmlv3.q4_0.bin
Source:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML
```

---

## 🚧 Future Enhancements

* Multilingual medical support
* Source citation in answers
* Document upload via UI
* Streaming responses
* Cloud-hosted inference
* Authentication & access control

---

## ⭐ Like it?

If this saved you some scrolling, **drop a star** on the repo. It helps other developers find it.

---

## 📜 License

This project is licensed under the **GNU General Public License v3.0**.
See the `LICENSE` file for more details.

---

## ⭐ Acknowledgements

This project builds upon open-source tools and research in the fields of **LLMs**, **NLP**, and **vector databases**.
Special thanks to the open-source community for enabling practical AI innovation.

---
