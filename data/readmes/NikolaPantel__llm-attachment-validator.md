# LLM Attachment Validator 🚀

A document intelligence pipeline that classifies email attachments from `.eml` files as **relevant** or **irrelevant**, using only the email's HTML body context.

This project demonstrates a **production-style LLM pipeline** for contextual document understanding and evaluation.

The system leverages the **Anthropic Claude API** for contextual reasoning and includes an evaluation module for benchmarking performance against ground truth data.

---

## ✨ Core Features

- **Intelligent Classification**  
  Analyzes email HTML bodies to determine if each attachment is contextually relevant.

- **Pure Contextual Reasoning**  
  Classification relies **exclusively on the email body**, simulating real-world scenarios where attachment metadata is unavailable.

- **Structured Output**  
  Generates clear, machine-readable JSON results for every email processed.

- **Built-in Evaluation**  
  Compare predictions against ground truth data using standard classification metrics:

  - Accuracy
  - Precision
  - Recall
  - F1 Score

- **Extensible Design**  
  Modular design allows experimentation with prompts, models, and classification logic.

---

## 🧠 How It Works

The validation process follows strict rules to ensure the focus remains on contextual understanding:

1. **Input**  
   An `.eml` file is provided.

2. **Extraction**

   The system extracts:

   - The **full HTML body**
   - A **list of attachment filenames**

   The system intentionally ignores:

   - Attachment content  
   - MIME types  
   - Email headers

3. **Reasoning (Claude API)**

   The HTML body and attachment list are sent to the Claude model with a carefully engineered prompt.

   The model must infer relevance based **only on the text and structure of the email.**

4. **Decision**

   Each attachment is classified as:

   - **relevant**
     - Materially referenced
     - Important to the email topic

   - **irrelevant**
     - Logos
     - Signature images
     - Decorative elements

5. **Output**

   A JSON file is created listing attachments under:

   - `relevant`
   - `irrelevant`

---

## 📁 Project Structure

```text
llm-attachment-validator/
│
├── examples/                 # Input .eml files
│   ├── example_00001.eml
│   ├── example_00002.eml
│   └── ...
│
├── ground_truth/             # Ground-truth JSON files
│   ├── attachments_00001.json
│   ├── attachments_00002.json
│   └── ...
│
├── output/                   # Generated classification results
│
├── classify_attachments.py   # Runs attachment classification
├── evaluate.py               # Evaluates predictions vs ground truth
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.9+
- Anthropic API Key

---

### Installation

Clone the repository:

```bash
git clone https://github.com/NikolaPantel/llm-attachment-validator.git
cd llm-attachment-validator
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate environment:

Mac/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

requirements.txt:

```text
anthropic
beautifulsoup4
tqdm
scikit-learn
```

---

### Set API Key

macOS / Linux:

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

Windows:

```bash
set ANTHROPIC_API_KEY=your-api-key-here
```

---

## 🚦 Usage

### Classify Attachments

Place `.eml` files in:

```
examples/
```

Run:

```bash
python classify_attachments.py
```

Results are saved in:

```
output/
```

---

### Example Output

`output/attachments_00001.json`

```json
{
  "relevant": [
    "quarterly_report_q1_2026.pdf"
  ],
  "irrelevant": [
    "company_logo.png",
    "email_signature_banner.jpg"
  ]
}
```

---

### Evaluate Performance

Place ground truth files in:

```
ground_truth/
```

Run:

```bash
python evaluate.py
```

Metrics include:

- Accuracy
- Precision
- Recall
- F1 Score

---

## 📊 Project Purpose

This project was built to demonstrate:

- LLM pipeline design
- Prompt engineering
- Email parsing
- Structured output generation
- Evaluation frameworks
- Production-style project organization

---

## 📜 License

MIT License © 2026 Nikola Pantelic

---

## 📬 Contact

Nikola Pantel  
GitHub: https://github.com/NikolaPantel

Project Link:

https://github.com/NikolaPantel/llm-attachment-validator