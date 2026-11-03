<div align="center">
  <a href="https://youtu.be/g-bPSGuClr0">
    <img src="https://img.youtube.com/vi/g-bPSGuClr0/0.jpg" alt="MiniCPM-OCR 1.0: This 1.3B Model Hits 94% on OCR Benchmark! Does It Pass my Tests?">
  </a>
  <h3>📺 <a href="https://youtu.be/g-bPSGuClr0">Watch the full video on YouTube</a></h3>
</div>

# MiniCPM-OCR 1.0: Ultra-Fast Document Vision

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Model Size: 1.3B](https://img.shields.io/badge/Model%20Size-1.3B%20%2B%202B%20Jev-brightgreen.svg)](https://huggingface.co/openbmb/MiniCPM-OCR-1.0)
[![Real5-OmniDocBench: 93.68](https://img.shields.io/badge/Real5--OmniDocBench-93.68%20SOTA-orange.svg)](https://github.com/OpenBMB/MiniCPM-OCR)
[![Local Footprint: ~1.7GB](https://img.shields.io/badge/Local%20Footprint-~1.7GB%20VRAM-purple.svg)](https://huggingface.co/openbmb/MiniCPM-OCR-1.0-gguf)

> "MiniCPM-OCR 1.0 (1.3B) is an ultra-efficient vision-language model engineered by OpenBMB for text-centric document understanding. Paired with MiniCPM-OCR Jev (2B) quality controller, it sets SOTA accuracy on real-world curved, warped, and low-light document captures while rendering complex formulas, multi-column tables, and invoices at 1.2 pages per second."

---

## 📊 Production Test Workflows

| Workflow | Capability Tested | Input Artifact | Expected Deliverable |
| :--- | :--- | :--- | :--- |
| **Financial Receipt KIE Extraction** | Key Information Extraction from thermal receipts with currency validation | Wrinkled store thermal receipt capture | Structured financial audit report with itemized table |
| **Academic Formula & Derivation Transcription** | Complex mathematical formulas and display equations into valid LaTeX | Academic physics derivation scan | Formatted LaTeX document with numbered equations |
| **Multi-Column Research Paper Parsing** | Dual-column scientific paper parsing with figures, formulas & citations | Dense two-column research paper page | Multi-column Markdown with figures, math & citations |

---

## ⚡ Quick Start (Windows PowerShell)

#### Step 1: Setup Environment, Download Weights & Register Runtime

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install ollama pillow requests

hf download openbmb/MiniCPM-OCR-1.0-gguf MiniCPM-OCR-1_0-Q8_0.gguf --local-dir models/
hf download openbmb/MiniCPM-OCR-1.0-gguf mmproj-model-f16-4x.gguf --local-dir models/

ollama create minicpm-ocr -f Modelfile
```

#### Step 2: Run Production Pipeline

```powershell
python main.py
```

---

### Practical Use Cases

- 🧾 **Autonomous Accounts Payable & Auditing**: Digitize thousands of curved paper receipts and supplier bills directly into ERP systems without human data entry.
- 📐 **Scientific Literature & Textbook Digitization**: Convert historic physics, engineering, and mathematics journals into searchable, compileable LaTeX repositories.
- ⚖️ **Legal Contract & Archival Preservation**: Extract critical clauses, timestamps, and multi-tier tables from degraded, skewed photocopies without cloud data leakage.
- 📱 **Mobile Edge Document Ingestion**: Deploy on low-power edge devices and laptops with sub-2GB memory footprint for offline field scanning.

---

### Future Feature Roadmap

- 🛡️ **Autonomous Jev 2B Quality Arbiter Loop**: Real-time confidence scoring and automated self-correction for OCR hallucinations.
- ⚡ **Multi-Page Batch Asynchronous Streamer**: Concurrent PDF processing leveraging vLLM and TensorRT-LLM backends.
- 🌐 **Expanded 100+ Language Typography Tokenizer**: Enhanced fine-grained OCR support across rare regional scripts and historical alphabets.
- 📊 **Dynamic Vector DB Semantic Chunker**: Direct chunking and indexing of extracted tables and formulas into local RAG pipelines.

---

`MiniCPM OCR` `MiniCPM-OCR 1.0` `OpenBMB OCR` `MiniCPM OCR Jev` `MiniCPM Jev` `MiniCPM OCR model` `OCR AI` `local OCR` `OCR benchmark` `document AI` `AI OCR model` `receipt OCR` `OCR to JSON` `document parsing AI` `MiniCPM tutorial` `MiniCPM local` `PaddleOCR VL` `OCRBench v2` `OCR accuracy` `table extraction AI` `math OCR` `handwriting OCR` `invoice OCR` `automated document review` `OCR Python` `Ollama OCR` `openbmb` `deepseek ocr` `data extraction` `computer vision` `minicpm-v` `image to text`
