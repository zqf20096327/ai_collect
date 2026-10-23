<div align="center">
  <a href="https://youtu.be/5-AnwkyDls4">
    <img src="https://img.youtube.com/vi/5-AnwkyDls4/0.jpg" alt="Qwen3.5 Just Got a Tiny Coding AI That Beats Models 3x Its Size! (Noema 2B Review)">
  </a>
  <h3>📺 <a href="https://youtu.be/5-AnwkyDls4">Watch the full tutorial on YouTube</a></h3>
</div>

# ⚡ Noema 2B Terminal Generator

An ultra-fast offline terminal command generator powered by Noema-2B GGUF running locally via Ollama. It converts plain English requests into exact shell syntax with zero conversational fluff.

## 🔄 3-Step Workflow

| Step 1: Input | Step 2: AI Action | Step 3: Result |
|---|---|---|
| User types natural language prompt in terminal | Noema-2B runs in non-thinking mode (<3GB VRAM) | Exact raw command saved to `outputs/outputs.md` |

---

## 🛠️ Quick Setup & Installation

Run this single PowerShell command to register the model and install dependencies:

```powershell
pip install urllib3 ; echo "FROM hf.co/NoemaAI-labs/Noema-2B-GGUF`nPARAMETER temperature 0.7`nPARAMETER presence_penalty 1.5" > Modelfile ; ollama create noema2b -f Modelfile
```

---

## 🚀 How to Run

Execute `main.py` with your natural language request:

```powershell
python main.py "Find all .pdf files larger than 10MB modified in the last 7 days and copy them to backup/"
```

Sample console output:

```
[Noema-2B] Querying Noema-2B model: 'Find all .pdf files larger than 10MB...'

--- Output Command ---
Get-ChildItem -Path . -Filter *.pdf | Where-Object { $_.LastWriteTime -gt (Get-Date).AddDays(-7) -and $_.Length -gt 10MB } | Copy-Item -Destination ./backup/
----------------------

[OK] Output saved cleanly to: outputs/outputs.md
```

---

## 🧩 Tech Stack

- **Primary Model**: Noema-2B GGUF (Q4_K_M / Q8_0)
- **Runtime Engine**: Ollama / llama.cpp
- **Language**: Python 3.10+ (Standard Library)
- **Hardware Requirement**: Standard laptop CPU or GPU (< 3 GB VRAM)

---

## 📂 Project Structure

```
.
├── Modelfile
├── README.md
└── main.py
```

---

## 💡 5 Real-World Use Cases

1. **Automated Shell Command Generator**: Instantly generate complex PowerShell and Bash file queries without opening search engines.
2. **Offline Local Laptop Execution**: Run AI syntax tools completely offline on low-resource machines without API key costs.
3. **Port & Process Management**: Quickly stop stuck background services on specific network ports without manual PID lookups.
4. **Git Workflow Shortcuts**: Stage, commit, and push changes with automatic descriptive message formatting.
5. **System Cleanup Automation**: Safely remove temporary build caches and log files under explicit size rules.

---

## 🔮 5 Future Features

1. **Direct Terminal Execution Toggle**: Option to execute the generated command directly after user confirmation.
2. **Multi-Shell Syntax Switcher**: Toggle output format between PowerShell, Bash, Zsh, and Fish shell.
3. **Command History Logging**: Append previous successful queries to a local history log file.
4. **Custom Parameter Presets**: Allow custom temperature and top_p overrides via CLI flags.
5. **Interactive Terminal TUI**: Rich terminal interface with live command preview and one-click copy.

---

## 🏷️ Keywords & Topics

Noema-2B, Noema 2B, Qwen3.5, Local AI, Coding AI, Ollama, GGUF, Terminal Generator, PowerShell AI, Offline LLM, Small Language Model, SLM, Open Source AI
