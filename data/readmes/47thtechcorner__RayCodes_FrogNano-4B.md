<div align="center">
  <a href="https://youtu.be/RqmsA_f0MhQ">
    <img src="https://img.youtube.com/vi/RqmsA_f0MhQ/0.jpg" alt="Microsoft FrogNano 4B: The Tiny AI Coding Agent That Fixes Your Code Locally">
  </a>
  <h3>📺 <a href="https://youtu.be/RqmsA_f0MhQ">Watch the full tutorial on YouTube</a></h3>
</div>

# 🐸 FrogNano 4B Bug Fixer

An automated self-healing Python agent that detects Pygame arcade crashes, diagnoses code errors, and applies verified patches locally using Microsoft's compact FrogNano 4B model.

---

## ⚡ Quick 3-Step Workflow

| Step 1: Input | Step 2: AI Action | Step 3: Result |
| :--- | :--- | :--- |
| Crashed Pygame script & stack trace | FrogNano analyzes code & applies patch | Verified operational game & report saved |

---

## 💻 Installation & Quickstart

Run this single command in PowerShell to download the FrogNano model weight, register it in Ollama, and execute the Pygame self-healing repair pipeline:

```powershell
hf download bartowski/FrogNano-4B-2609-GGUF FrogNano-4B-2609-IQ2_M.gguf --local-dir models/ ; ollama create frognano-4b -f Modelfile ; python main.py
```

---

## 🛠️ Technology Stack

* **FrogNano-4B (GGUF):** Microsoft's 4B local AI agent derived from Qwen3.5-4B base model.
* **Pygame 2.6:** Graphical 2D arcade game engine for visual gameplay rendering.
* **Ollama Engine:** Lightweight local model server for instant GPU/CPU inference.
* **Leaf Harness Pattern:** Sandboxed multi-turn inspection and automated patch execution.

---

## 📁 Repository Structure

```text
FrogNano-4B/
├── main.py
├── target_game.py
├── Modelfile
└── README.md
```

---

## 🔍 Code Files Explanation

* `main.py`: Core execution script that runs the target Pygame project, catches error traces, queries FrogNano via Ollama, applies code patches, and verifies game execution.
* `target_game.py`: Complete visual Pygame Arcade Snake game containing a runtime movement bug to showcase automated error detection and self-healing.
* `Modelfile`: Ollama model registration file specifying GGUF model parameters and system prompt settings.

---

## 💡 5 Real-World Use Cases

1. **Visual Pygame Repair:** Instantly fixes logic typos and crashes during 2D game development.
2. **Automated GUI Recovery:** Heals broken Python desktop applications without manual debugging.
3. **CI/CD Build Debugging:** Analyzes unit test failure stack traces in automated pipeline runners.
4. **Offline AI Assistant:** Performs repo-level debugging on laptops without requiring internet or API keys.
5. **Beginner Coding Tutor:** Explains why game code crashed in simple terms while providing corrected source code.

---

## 🔮 5 Future Enhancements

1. **Multi-File Patching:** Support cross-file updates across complex software repositories.
2. **Git Auto-Commit:** Automatically create Git branches and commits for verified patches.
3. **Streamlit Terminal UI:** Interactive visual web dashboard for tracking patch steps.
4. **Pytest Integration:** Auto-generate missing unit tests for patched functions.
5. **Multi-Model Orchestration:** Benchmark FrogNano against larger models on difficult bugs.

---

### Keywords
FrogNano, Microsoft AI, Qwen3.5-4B, Local LLM, Agentic AI, Automated Debugging, Self-Healing Code, Python Repair, Pygame Bug Fix, Ollama, Leaf Tool Harness, GPU Poor, Open Source AI.
