<div align="center">
  <a href="https://youtu.be/A5Z7XJpZLWI">
    <img src="https://img.youtube.com/vi/A5Z7XJpZLWI/0.jpg" alt="Humanizer Skill 3.0: Make AI Writing Sound 100% Human Locally!">
  </a>
  <h3>📺 <a href="https://youtu.be/A5Z7XJpZLWI">Watch the full tutorial on YouTube</a></h3>
</div>

# ⚡ Humanizer Content Transformer Engine

Humanizer transforms dense, AI-generated technical documentation into clean, conversational developer blog posts. It strips away robotic fluff and corporate jargon while keeping all your code blocks, command lines, and links completely intact.

| Step 1: Skill Install | Step 2: Model Registration | Step 3: Run Engine |
| :--- | :--- | :--- |
| Install Humanizer via CLI / PowerShell | Register `noema2b` or pull `llama3.2:3b` | Execute `python main.py` |

---

## 🛠️ Installation & Setup

### 1. Skill Installation Options

#### Option A: Skills CLI Installation (Recommended)

```bash
npx skills add blader/humanizer --global
```

#### Option B: PowerShell Direct Skill Download

```powershell
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/blader/humanizer/main/SKILL.md" -OutFile "SKILL.md"
```

#### Option C: Claude Code Plugin Installation

```text
/plugin marketplace add blader/humanizer
/plugin install humanizer@humanizer
```

---

### 2. Model Download & Registration Options

#### Option A: Noema 2B GGUF Model (Recommended)

Run this single PowerShell command to install dependencies, create the `Modelfile`, and register `noema2b` in Ollama:

```powershell
pip install urllib3 ; echo "FROM hf.co/NoemaAI-labs/Noema-2B-GGUF`nPARAMETER temperature 0.7`nPARAMETER presence_penalty 1.5" > Modelfile ; ollama create noema2b -f Modelfile
```

#### Option B: Llama 3.2 3B Model

Alternatively, pull and use `llama3.2:3b` via Ollama:

```powershell
ollama pull llama3.2:3b
```

---

### 3. Run Command

Execute the main Python engine to convert your input document:

```powershell
python main.py
```

The transformed, human-readable blog post or developer conversation will be created inside `outputs/outputs.md` along with exact recorded generation time.

---

## 💻 Tech Stack

- **Core Logic:** Python 3.12 (Native AST Markdown Parser)
- **Primary AI Backend:** Ollama (`noema2b:latest` / `llama3.2:3b`)
- **Input Document:** Markdown (`inputs/input_doc.md`)
- **Output Result:** Markdown (`outputs/outputs.md`)

---

## 📁 Repository Structure

```text
humanizer/
├── inputs/
│   └── input_doc.md
├── Modelfile
├── main.py
└── README.md
```

---

## 💡 5 Real-World Use Cases

1. **Open-Source Release Notes:** Clean up AI-drafted CHANGELOGs so developers get direct updates without corporate filler.
2. **Technical Developer Blogs:** Turn dry architecture specifications into engaging tutorials for engineering teams.
3. **Repository READMEs:** Strip robotic phrasing from project landing pages to boost maintainer credibility.
4. **API Quickstarts:** Rewrite formal endpoint guides into beginner-friendly walkthroughs.
5. **Community Documentation:** Convert raw technical outlines into clear, readable contributor guides.

---

## 🔮 5 Future Features

1. **Automatic GitHub Action:** Trigger prose cleanup automatically on every new documentation pull request.
2. **Multi-Model Swapping:** Dynamically switch between Noema, Llama, and Qwen backends based on file complexity.
3. **Interactive CLI Diff Visualizer:** Preview side-by-side prose edits directly in your PowerShell terminal before saving.
4. **Custom Vocabulary Blacklists:** Define repository-specific lists of banned corporate jargon terms.
5. **Batch Folder Processing:** Clean an entire `docs/` directory of Markdown files in a single command.

---

## 🏷️ Keywords & Topics

Humanizer, Humanizer Skill, AI Writing, Remove AI Tells, Local AI, Ollama, Noema 2B, Llama 3.2, Claude Code Plugin, Skills CLI, Developer Documentation, Open Source AI
