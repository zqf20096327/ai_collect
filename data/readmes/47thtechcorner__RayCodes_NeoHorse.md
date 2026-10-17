<div align="center">
  <a href="https://youtu.be/3JRrNpozzpE">
    <img src="https://img.youtube.com/vi/3JRrNpozzpE/0.jpg" alt="This 4B Local AI Scores 96.9% on Coding! (NeoHorse Agent Setup)">
  </a>
  <h3>📺 <a href="https://youtu.be/3JRrNpozzpE">Watch the full tutorial on YouTube</a></h3>
</div>

# 🐴 NeoHorse AI Local Agent


NeoHorse-1-4B is a 4-billion parameter AI model designed for offline coding, automated tool calling, and self-improving local workflows.

| Step 1: Input | Step 2: AI Action | Step 3: Result |
| :--- | :--- | :--- |
| Text instructions or code files | NeoHorse parses tools & checks logic | Optimized code & execution report |

---

## ⚡ Single-Command Quick Setup & Model Download

Run this single PowerShell command to install dependencies, download the official **`NeoHorse-1-4B-Q4_K_M.gguf`** model directly into `models/`, and register it in Ollama:

```powershell
pip install numpy ollama huggingface_hub; mkdir -p models, outputs; hf download TokenRhythm/NeoHorse-1-4B-GGUF NeoHorse-1-4B-Q4_K_M.gguf --local-dir models; ollama create neohorse-4b -f models/Modelfile
```

> **Direct File Download Link**: [TokenRhythm/NeoHorse-1-4B-GGUF/NeoHorse-1-4B-Q4_K_M.gguf](https://huggingface.co/TokenRhythm/NeoHorse-1-4B-GGUF/blob/main/NeoHorse-1-4B-Q4_K_M.gguf)

---

## 🔧 Model Registration (Ollama Modelfile)

The project includes a `Modelfile` configured for `NeoHorse-1-4B-Q4_K_M.gguf` in the `models/` directory:

```dockerfile
# Point to your downloaded GGUF file inside models directory
FROM ./models/NeoHorse-1-4B-Q4_K_M.gguf

# Set context window (NeoHorse supports up to 262,144 tokens)
PARAMETER num_ctx 16384

# System prompt to activate error-correction capabilities
SYSTEM "You are NeoHorse, an advanced AI assistant optimized for tool use, structured workflows, and precise execution. Double-check your logic before responding."
```

---

## 💻 Running the Autonomous Agent

Execute the main agent script to start the local tool-calling loop:

```powershell
python main.py
```

The execution trajectory and generated code output will be saved directly to `outputs/outputs.md`.

---

## 🛠️ Technology Stack

- **Core Model**: NeoHorse-1-4B-Q4_K_M (TokenRhythm fine-tune derived from Qwen3.5-4B)
- **Language**: Python 3.10+
- **Serving Engine**: Ollama / vLLM / llama.cpp (GGUF Format)
- **Context Length**: 262,144 Tokens Native (Extensible to 1M+)

---

## 📂 Project File Structure

```
NeoHorse/
├── models/
│   ├── Modelfile
│   └── NeoHorse-1-4B-Q4_K_M.gguf
├── main.py
└── README.md
```

---

## 🎯 5 Practical Use Cases

1. **Offline Code Generation**: Generate bug-free Python functions on local hardware without internet dependencies.
2. **Local Tool Routing**: Automatically format and dispatch JSON commands for local PC file and system automation.
3. **Large Document Audit**: Process massive documentation files up to 262,000 tokens in a single context window.
4. **Pre-Execution Error Checking**: Enforce active system prompts to double-check code parameters before execution.
5. **Private Data Pipelines**: Analyze sensitive company databases locally with zero third-party cloud data exposure.

---

## 🔮 5 Future Enhancement Features

1. **Multi-Agent Swarm Orchestration**: Coordinate multiple NeoHorse instances for parallel task solving.
2. **Dynamic GGUF Auto-Downloader**: Automatically fetch optimal quantization levels based on available VRAM.
3. **Structured GUI Dashboard**: Build an interactive web panel for visualizing live tool execution trees.
4. **Enhanced Function Calling Schemas**: Support custom OpenAPI specification imports directly into agent loops.
5. **Continuous Local Fine-Tuning**: Log session trajectories to continuously adapt local model performance.

---

## 🏷️ Keywords & SEO Tags

`NeoHorse` `NeoHorse 1.4B` `Local AI Agent` `Ollama` `GGUF` `Python AI` `Offline Coding AI` `Qwen3.5` `AI Code Assistant` `Autonomous Agent`

