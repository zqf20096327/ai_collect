# 🧠 Hindsight CARA Persona Tester

<div align="center">
  <a href="https://youtu.be/9kEQrWJU5Uc">
    <img src="https://img.youtube.com/vi/9kEQrWJU5Uc/0.jpg" alt="New #1 Agent Memory Beats GPT-4o With $0 Cost! (Hindsight Setup)">
  </a>
  <h3>📺 <a href="https://youtu.be/9kEQrWJU5Uc">Watch the full tutorial on YouTube</a></h3>
</div>

A lightweight AI stress-testing tool that ingests startup pitches into Hindsight agent memory and analyzes architectural, financial, and product risks using 3 distinct CARA disposition personalities.

| Step 1: Input 📄 | Step 2: AI Action 🧠 | Step 3: Result 📊 |
| :--- | :--- | :--- |
| Load startup pitch document (`sample_pitch.txt`) | Hindsight ingests facts & applies 3 CARA disposition personalities | Generates structured Markdown report & dark-mode HTML dashboard |

---

## 🛠️ Tech Stack & Concepts

- **Memory Engine:** Hindsight (`hindsight-all`) - The core tool that remembers and learns.
- **CARA Engine:** Stands for Disposition Traits. It lets us change how the AI thinks by adjusting three sliders: Skepticism, Literalism, and Empathy. This means the AI can look at the same facts but give different advice based on its assigned "personality".
- **LLM Providers:** Google Gemini (`gemini-3.5-flash-lite`) or Local Ollama (`qwen2.5:3b`)
- **Environment Management:** `python-dotenv`
- **Output Visualizer:** HTML5 & CSS3 Dark-Mode Dashboard

---

## ⚡ Setup Steps

Run these commands in Windows PowerShell to set up your environment:

```powershell
# 1. Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install hindsight-all python-dotenv -U
```

---

## 🚀 Run Steps

Execute the stress-tester using Google Gemini or local Ollama:

```powershell
# Run using Gemini 3.5 Flash-Lite (Default)
python main.py --provider gemini --input sample_pitch.txt

# Run using Local Ollama (100% Free & Offline)
python main.py --provider ollama --input sample_pitch.txt
```

---

## 🧪 Test Steps

Validate project functionality and generate reports rapidly:

```powershell
python main.py --provider gemini
```

---

## 📂 File Explanations

- **`main.py`**: Core CLI application that manages embedded Hindsight server, ingests memory banks, executes local recall, and runs 3 CARA disposition passes.
- **`sample_pitch.txt`**: Sample startup deal memo containing architecture claims, financial metrics, and hidden operational risks.
- **`requirements.txt`**: Project dependencies (`hindsight-all`, `python-dotenv`).
- **`.env`**: Local environment configuration storing your API key securely.

---

## 💡 5 Real-World Use Cases

1. **VC Investment Due Diligence:** Automatically audit startup pitch decks for hidden burn-rate risks and customer churn traps.
2. **System Architecture Audit:** Stress-test software architecture proposals against strict distributed system principles.
3. **Product Feedback Synthesis:** Evaluate user feature requests through empathetic customer and literal developer lenses.
4. **Security & Vulnerability Analysis:** Scan codebase changes for PII leaks and lock contention bottlenecks.
5. **Competitive Intelligence:** Ingest competitor product updates and reflect on strategic market vulnerabilities.

---

## 🔮 5 Future Feature Ideas

1. **Multi-Bank Cross Reflection:** Compare pitch claims against historical industry benchmark memory banks.
2. **Interactive Streamlit Dashboard:** Live UI sliders to tweak CARA disposition parameters dynamically.
3. **Automated PDF Export:** Convert generated stress-test HTML reports into executive PDF pitch teardowns.
4. **Slack & Discord Bot Integration:** Trigger CARA stress tests directly from developer chat channels.
5. **Custom Disposition Presets:** Save and share specialized personality profiles for legal, security, and finance audits.

---
**Keywords:** Hindsight, Agent Memory, AI Persona, CARA, LLM Memory, Local AI, Ollama, Gemini, AI Stress-Testing, Python
