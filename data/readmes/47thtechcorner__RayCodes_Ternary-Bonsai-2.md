<div align="center">
  <a href="https://youtu.be/KW9PYnYDhjg">
    <img src="https://img.youtube.com/vi/KW9PYnYDhjg/0.jpg" alt="Ternary Bonsai 2: New 0.4GB Vision AI With 310 Tokens/Sec Speed!">
  </a>
  <h3>📺 <a href="https://youtu.be/KW9PYnYDhjg">Watch the full tutorial on YouTube</a></h3>
</div>

# 🛡️ Ternary Bonsai Document Redactor

Fast, 100% private visual document scanner and sensitive data redactor powered by Ternary Bonsai 2.

| Step 1: Input Document | Step 2: AI Action | Step 3: Result |
| :--- | :--- | :--- |
| Load local receipt, invoice, or ID | Detect PII, cards, and account numbers | Save clean redacted JSON report |

---

## ⚡ Superpowers

- **9x Less Memory:** Runs the complete multimodal reasoning engine in just 0.43 GB to 0.52 GB of RAM.
- **100% Offline Privacy:** Processes sensitive records on your local machine with zero external network requests.
- **Realistic 4GB VRAM Performance:** Averages ~5.88s per document on a consumer 4GB VRAM GPU with ~0.88 GB peak memory.
- **Batch Multimodal Loop:** Dynamically scans all images in the `inputs/` folder in a sequential queue.
- **Smart PII Detection:** Automatically masks names, cards, terminals, phone numbers, and medical Rx codes.

---

## 🛠️ Tech Stack

- **Model:** Ternary Bonsai 2 2B (PrismML {-1, 0, +1} quantized multimodal architecture)
- **Runtime:** Ollama / llama.cpp local server engine
- **Language:** Python 3.10+
- **Libraries:** `ollama`, `Pillow`, `pydantic`

---

## 📁 Project Structure

```
.
├── inputs/
│   ├── 01_easy_retail_receipt.jpg
│   ├── 02_medium_coffee_bill.jpg
│   ├── 03_medium_business_card.jpg
│   ├── 04_hard_dense_invoice.jpg
│   └── 05_extreme_medical_prescription.jpg
├── models/
│   ├── Ternary-Bonsai-2-2B-PQ2_0.gguf
│   └── Ternary-Bonsai-2-2B-mmproj-Q8_0.gguf
├── Modelfile
├── requirements.txt
├── main.py
└── README.md
```

---

## 🚀 Setup & Installation

### 1. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 2. Download Model Checkpoints

Download the Ternary Bonsai 2 language model and vision projector directly into your `models/` directory:

```powershell
hf download prism-ml/Ternary-Bonsai-2-2B-gguf Ternary-Bonsai-2-2B-PQ2_0.gguf --local-dir models
hf download prism-ml/Ternary-Bonsai-2-2B-gguf Ternary-Bonsai-2-2B-mmproj-Q8_0.gguf --local-dir models
```

### 3. Register Model in Ollama

Create your local model alias with the preconfigured Modelfile:

```powershell
ollama create ternary-bonsai-2 -f Modelfile
```

---

## 💻 Running the Redactor

Execute the main program to iterate through all images in `inputs/` and redact sensitive data:

```powershell
python main.py
```

The tool will process every document image, calculate the processing latency on your 4GB VRAM GPU, mask all sensitive entities, and save a full audit report to `outputs/outputs.md`.

---

## 🎯 Practical Use Cases

1. **Healthcare Record Cleansing:** Redact patient names, social security numbers, and diagnoses from scanned clinic intake forms before archiving.
2. **Financial Expense Auditing:** Mask employee credit card numbers and bank account details from uploaded receipt photos.
3. **Air-Gapped Government Operations:** Run autonomous document classification inside secure field facilities without internet connectivity.

---

## 🔮 Future Capabilities

1. **Pixel-Level Bounding Box Inpainting:** Automatically draw black censor bars directly over the original image pixels.
2. **Multi-Page PDF Batch Processing:** Sequentially process hundreds of scanned invoice pages in a single automated queue.
3. **Voice Audio Scrubbing:** Transcribe and redact recorded client calls locally using paired edge speech models.

---

## 🏷️ Keywords & Tags

`Ternary Bonsai 2` `PrismML` `Vision AI` `1.58-bit AI` `Ternary Quantization` `Ollama` `llama.cpp` `Document Redactor` `Multimodal LLM` `Local AI` `Privacy AI` `Edge AI` `PII Redaction`
