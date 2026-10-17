<div align="center">
  <a href="https://youtu.be/edwCp-cSfOc">
    <img src="https://img.youtube.com/vi/edwCp-cSfOc/0.jpg" alt="Google LangExtract is NOW LOCAL! Zero Hallucination Document AI">
  </a>
  <h3>📺 <a href="https://youtu.be/edwCp-cSfOc">Watch the full tutorial on YouTube</a></h3>
</div>

# 🌐 Google LangExtract Precise Grounding

Google LangExtract is an open-source Python library that transforms unstructured text documents into verified structured JSON data while mapping every single extracted point to its exact character location in the original text.

---

## ⚡ 3-Step Extraction Workflow

| Step 1: Input Document | Step 2: AI Grounding Action | Step 3: Verifiable Result |
| :--- | :--- | :--- |
| Load chaotic text or financial PDF file | Schema enforcement & multi-pass character offset mapping | Structured JSON with 100% verifiable source character spans |

---

## 📥 Sample Document Setup (Required)

Before running the pipeline, create your input document in the root directory:

1. **Create File**: Create a text file named `NVIDIA_Q4_FY25_Financial_Report.txt` in the root folder.
2. **Add Content**: Copy and paste any corporate press release, SEC filing, earnings report, or clinical note text into `NVIDIA_Q4_FY25_Financial_Report.txt`.
3. *(Alternatively, configure `INPUT_DOCUMENT` in `main.py` to point to any custom text file).*

---

## 🚀 Quick Start & Installation

Run these copy-pasteable commands in your Windows PowerShell terminal:

```powershell
# 1. Create and activate a Python virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# 2. Install Google LangExtract and LLM provider SDKs
pip install langextract google-genai openai

# 3. Pull the local Ollama model (Optional for local execution)
ollama pull qwen3:4b

# 4. Execute the financial extraction pipeline
python main.py
```

---

## 🔑 LLM Provider Configuration & Setup Guide

LangExtract supports **Ollama (local)**, **Google Gemini**, and **OpenAI**. Configure your preferred provider in `main.py`:

### Option A: Local Ollama (Zero API Costs)
- Ensure Ollama is running locally (`ollama serve`).
- In `main.py`, set `MODEL_PROVIDER = "ollama"` and specify your model (e.g. `OLLAMA_MODEL = "qwen3:4b"`).

### Option B: Google Gemini API (Recommended for Cloud Speed)
1. Go to [Google AI Studio](https://aistudio.google.com/).
2. Click **Create API Key** and copy your key string.
3. Set your environment variable in PowerShell:
   ```powershell
   $env:GEMINI_API_KEY="your_gemini_api_key_here"
   ```
4. In `main.py`, set `MODEL_PROVIDER = "gemini"` and `OLLAMA_MODEL = "gemini-2.5-flash"`.

---

## 📂 Project Architecture

```
LangExtract/
├── main.py                             # Core extraction script & schema provider
├── .env                                # API keys & environment configuration
└── README.md                           # Project documentation and setup guide
```

---

## 🛠️ Code Architecture & File Explanation

- **`main.py`**: Reads the target financial document, initializes the schema-enforced `Extractor`, executes character offset grounding, measures latency per query, and exports the final verified findings.
- **`.env`**: Stores local system parameters and cloud provider credentials securely.

---

## 💡 5 Practical Real-World Use Cases

1. 🏥 **Clinical Note & EHR Extraction**: Parse physician notes to extract patient diagnoses, dosages, and treatment plans with source character audit trails for medical compliance.
2. 📊 **Financial PDF & Earnings Audit**: Extract revenue, gross margins, cash balances, and risk disclosures from corporate filings with 100% verifiable quotes.
3. ⚖️ **Legal Contract Clause Analysis**: Extract termination conditions, liability caps, and indemnification clauses paired with exact line/character offsets.
4. 📑 **Insurance Claims Processing**: Convert chaotic accident reports and policy forms into structured JSON claims data for automatic adjudication.
5. 🎙️ **Podcast & Customer Call Analytics**: Pull key customer feature requests, sentiment signals, and competitor mentions directly from raw audio transcripts.

---

## 🔮 5 Future Enhancements

1. 🌐 **Multi-Modal Document Parsing**: Native OCR ingestion for scanned PDFs, tables, and handwritten medical records.
2. 🔄 **Automated RAG Knowledge Graph**: Feed character-grounded extractions into vector databases for hallucination-free enterprise search.
3. 📱 **Real-Time Stream Grounding**: Live character index mapping for streaming voice calls and customer support chats.
4. 🛡️ **Confidence Score Calibration**: Automatic flagging of ambiguous text spans requiring human-in-the-loop review.
5. 🚀 **Distributed Multi-GPU Processing**: Accelerated parallel chunking for enterprise documents exceeding 100,000 pages.

---

## 🔑 SEO Keywords & Topics

`Google LangExtract`, `Local Document AI`, `Ollama Structured Extraction`, `Zero Hallucination LLM`, `Python Source Grounding`, `Gemini API`, `OpenAI JSON Schema`, `Enterprise Document Parsing`
