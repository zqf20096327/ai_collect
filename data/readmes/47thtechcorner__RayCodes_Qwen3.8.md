<div align="center">
  <a href="https://youtu.be/XDGWObkZN0o">
    <img src="https://img.youtube.com/vi/XDGWObkZN0o/0.jpg" alt="Qwen 3.8 4B (Distilled): Run The Open Source King Locally!">
  </a>
  <h3>📺 <a href="https://youtu.be/XDGWObkZN0o">Watch the full tutorial on YouTube</a></h3>
</div>

# ⚡ Qwen3.8 4B Distilled Prompt Architect

An offline, zero-cost local prompt optimization engine powered by sequence-distilled Qwen3.8 4B AI reasoning. It automatically refactors lazy, unstructured user prompts into master-level system prompts with role definition, technical constraints, and output schema rules.

## 🎯 Problem to be Solved

| Problem | Impact | Qwen3.8 4B Solution |
| :--- | :--- | :--- |
| **Vague User Prompts** | Generic, hallucinated, or unhelpful AI responses | Structurally refactors inputs into precise system instructions |
| **Cloud API Expense** | High token costs when optimizing prompts with cloud LLMs | Runs 100% locally on consumer hardware with zero API billing |
| **Reasoning Latency** | Slow execution when waiting for internal thought traces | Bypasses `<think>` tags via custom system prompts for fast speed |

## 🚀 Key Features

- **Instruction-Following Distillation:** Inherits Qwen3.8-Max reasoning traces to structure complex instructions effortlessly.
- **Offline Prompt Engineering:** Transforms 1-line inputs into production-ready system prompts without sending data online.
- **Reasoning Suppression:** Suppresses internal reasoning `<think>` tags to output optimized prompts at lightning speed.
- **Structured Schema Enforcer:** Injects clear roles, technical constraints, edge cases, and output formatting rules.
- **Multi-Domain Adaptability:** Handles software engineering, creative writing, regex generation, and educational prompts.

## 💻 Technology Stack

- **Model Engine:** `Ma7ee7/Qwen3.8_4B_Distilled_GGUF:Q4_K_M`
- **Runtime Environment:** Python 3.10+
- **Local Server:** Ollama Native HuggingFace GGUF
- **API Protocol:** REST HTTP (`http://localhost:11434`)

## 📂 Project Structure

```
.
├── main.py
├── outputs.md
├── .gitignore
└── README.md
```

## ⚙️ Installation & Setup

1. **Install Ollama** (if not already installed) from the official website and start the daemon.

2. **Pull the Distilled Model:**
   ```powershell
   ollama run hf.co/Ma7ee7/Qwen3.8_4B_Distilled_GGUF:Q4_K_M
   ```

3. **Verify Environment:** Ensure Python 3.10+ is installed and accessible in your system path.

## ▶️ How to Run

Run the prompt architect pipeline directly in Windows Antigravity PowerShell:

```powershell
python main.py
```

## 💡 5 Primary Use Cases

1. **AI Developer Workflow:** Upgrade vague code prompts into detailed specifications for coding assistants.
2. **Enterprise System Prompts:** Standardize system prompts for customer support bots and internal AI tools.
3. **Regex & Data Parsing:** Convert basic requests into strict pattern-matching prompts with edge case rules.
4. **Educational Content Creation:** Generate structured, age-appropriate educational explainer prompts.
5. **Offline PC Assistant:** Run local prompt engineering utilities on air-gapped or offline laptops.

## 🔮 5 Future Enhancements

1. **Streamlit Local Web GUI:** Provide an interactive dashboard to paste lazy prompts and copy optimized results.
2. **Custom System Prompt Templates:** Allow users to save custom role profiles (e.g. DevOps, Data Science, Copywriter).
3. **Prompt Quality Scoring Engine:** Evaluate input vs output prompt completeness with automated metrics.
4. **Clipboard Auto-Copy:** Automatically copy the generated master prompt directly into the system clipboard.
5. **Multi-Language Support:** Expand prompt refactoring logic to handle non-English user inputs seamlessly.

## 🔑 Keywords & Search Tags
`qwen3.8` `ollama` `local-llm` `prompt-engineering` `distilled-llm` `python` `open-source-ai` `gguf` `prompt-optimization`

