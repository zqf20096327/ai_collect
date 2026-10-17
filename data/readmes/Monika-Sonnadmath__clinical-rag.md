# 🏥 clinical-rag

**Ask questions about clinical documents using AI — answers grounded in the document, not guesswork.**

Built from a simple frustration: working in healthcare tech, I kept seeing clinical staff spend time manually reading through lengthy PDF documents to find specific pieces of information. A discharge summary, a referral letter, a set of clinical guidelines — documents that could be 10, 20, 30 pages long, when you only need one answer.

This tool lets you upload any clinical PDF and ask it questions in plain English. The AI reads the document, finds the relevant sections, and gives you a direct answer with a reference to where it found it.

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-0.3-green)](https://langchain.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Why I Built This

I work as a Senior Software Developer in healthcare technology. A big part of that job is figuring out where automation can actually help clinical staff — not just what's technically possible, but what's genuinely useful in a clinical setting.

One thing I noticed: a lot of time gets spent navigating documents. Not reading them carefully — just navigating. Ctrl+F for a patient name, scrolling to find a date, hunting for a medication dosage buried in paragraph four of page seven.

RAG (Retrieval-Augmented Generation) felt like a natural fit. Instead of summarising or rewriting documents — which introduces risk in a clinical context — it finds and returns exactly what's in the document, grounded in the source. The AI doesn't add to it. It doesn't embellish. If the answer isn't there, it says so.

That last part was important to me. In a clinical setting, a confident wrong answer is worse than an honest "I don't know." So temperature is set to 0 by default, and the system prompt explicitly tells the model not to guess.

---

## Features

- 📄 **Upload any clinical PDF** — discharge summaries, referral letters, guidelines, protocols
- 💬 **Ask in plain English** — no special syntax required
- 📍 **Grounded answers** — responses cite which document they came from
- 🎯 **Accuracy-first design** — temperature 0, explicit instructions not to guess
- 💾 **Persistent vector store** — re-load documents without re-processing
- 🖥️ **Web UI** — simple Streamlit interface, no coding required to use
- 🐍 **Python API** — import and use in your own pipeline

---

## Quick Start

```bash
# Install
pip install -r requirements.txt

# Set your OpenAI API key
export OPENAI_API_KEY=sk-...

# Run the web app
streamlit run app.py
```

Then open http://localhost:8501, upload a PDF and start asking questions.

---

## Python API

```python
from src.rag_pipeline import ClinicalRAG, RAGConfig

rag = ClinicalRAG(config=RAGConfig(model="gpt-4o-mini"))
rag.load_documents("./documents/discharge_summary.pdf")

response = rag.ask("What medications were prescribed on discharge?")
print(response.answer)
# "The patient was discharged on amoxicillin 500mg three times daily
#  for 7 days and paracetamol 1g as required."

print(response.sources)
# ['discharge_summary.pdf']

print(response.confidence)
# 'high'
```

### Batch questions

```python
questions = [
    "What is the diagnosis?",
    "What follow-up appointments are needed?",
    "Are there any drug allergies noted?",
]
responses = rag.ask_batch(questions)
for q, r in zip(questions, responses):
    print(f"Q: {q}")
    print(f"A: {r.answer}\n")
```

### Reuse a processed document

```python
# First run — process and save
rag = ClinicalRAG()
rag.load_documents("./documents/")

# Later — reload without reprocessing
rag = ClinicalRAG()
rag.load_existing()
response = rag.ask("What are the contraindications?")
```

---

## Configuration

```python
config = RAGConfig(
    model="gpt-4o-mini",        # OpenAI model to use
    embedding_model="text-embedding-3-small",
    chunk_size=500,              # Characters per chunk — smaller = more precise
    chunk_overlap=50,            # Overlap between chunks for context continuity
    retrieval_k=4,               # Number of chunks retrieved per question
    temperature=0.0,             # 0 = deterministic. Important for clinical accuracy.
    persist_directory="./vector_db",
)
```

---

## How It Works

```
PDF document
     │
     ▼
Extract text (PyPDF)
     │
     ▼
Split into chunks (RecursiveCharacterTextSplitter)
     │
     ▼
Embed chunks (OpenAI text-embedding-3-small)
     │
     ▼
Store in vector database (ChromaDB)
     │
  Question
     │
     ▼
Embed question → similarity search → retrieve top-k chunks
     │
     ▼
LLM generates answer grounded in retrieved chunks
     │
     ▼
RAGResponse (answer + sources + confidence)
```

---

## Running Tests

```bash
pip install pytest
pytest tests/ -v
```

Tests cover config, response model and pipeline behaviour without requiring an API key.

---

## Important Notes on Clinical Use

This tool is designed to help navigate documents more efficiently — it is **not a medical decision support system** and should not be used to make clinical decisions. Always verify answers against the source document. The tool is designed to tell you where in the document it found the answer precisely so you can do this easily.

---

## Roadmap

- [ ] Support for Word documents and plain text
- [ ] Multi-document querying across a folder of patient records
- [ ] HL7/FHIR structured data support
- [ ] Local LLM support via Ollama (no API key required)
- [ ] Export Q&A session as PDF report

---

## Contributing

Issues and pull requests welcome. If you work in healthcare tech and have ideas for how this could be more useful in practice, I'd especially love to hear from you.

---

## License

MIT

---

## Author

**Monika Sonnad Math** — Senior Software Developer, Belfast UK
Working at the intersection of healthcare technology and AI.

[LinkedIn](https://linkedin.com/in/monika-sonnadmath) · [GitHub](https://github.com/Monika-Sonnadmath)
