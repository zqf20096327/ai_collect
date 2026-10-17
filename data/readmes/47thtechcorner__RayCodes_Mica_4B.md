<div align="center">
  <a href="https://youtu.be/pyJdRVdlats">
    <img src="https://img.youtube.com/vi/pyJdRVdlats/0.jpg" alt="Open Source Jev is HERE: Mica 4B Makes 47ms Decisions With Zero Tokens!">
  </a>
  <h3>📺 <a href="https://youtu.be/pyJdRVdlats">Watch the full tutorial on YouTube</a></h3>
</div>

# 🕹️ Mica 4B AI Decision Engine

**Mica 4B AI Decision Engine** is an ultra-fast local decision system comparing **Mica v0.1 4B** (47ms spatial intelligence) against **Laya AI** (30ms fast classifier) in a real-time side-by-side Arcade Pac-Man Evasion Duel built for 4GB VRAM hardware setups.

---

### 🔄 3-Step Action Workflow

| Step 1: Game State Input | Step 2: Single-Pass Forward Logits | Step 3: 47ms Action Decision |
|---|---|---|
| Pac-Man coordinates, 4 ghost vectors, pellet distances, and wall boundaries compiled into state vector. | Model evaluates spatial choices in one pass without token generation overhead. | Direct direction response (UP/DOWN/LEFT/RIGHT) executed on grid in 47ms. |

---

## ⚡ Quick Setup & Installation

Run these commands in Windows PowerShell to set up requirements and download the quantized model weights into your `models/` directory:

```powershell
# 1. Install required Python packages
pip install fastapi uvicorn pydantic torch laya requests huggingface-hub

# 2. Download Mica v0.1 4B Q4_0 GGUF model into models directory
hf download sky7350/Mica-v0.1-4B mica-v0.1-4b-Q4_0.gguf --local-dir models

# 3. Create local model entry in Ollama
ollama create mica-v0.1-4b -f models/Modelfile

# 4. Launch the application
python main.py
```

Open your browser and navigate to `http://127.0.0.1:8000` to view the live Pac-Man Evasion Duel arena.

---

## 📁 Repository Structure

```
Mica 4B/
├── models/
│   ├── Modelfile
│   └── mica-v0.1-4b-Q4_0.gguf
├── game.html
├── main.py
└── README.md
```

---

## 🛠️ Tech Stack & Key Components

- **Mica v0.1 4B**: 4B Jev-style decision model running at 47ms latency with zero text generation delay.
- **Laya AI**: 0.4B encoder classifier running at 30ms latency for rapid reflex checks.
- **FastAPI Backend**: Lightweight Python API server handling real-time spatial state evaluations.
- **HTML5 Arcade Canvas**: Responsive retro grid renderer displaying move trajectories and live confidence bars.

---

## 🎯 5 Practical Real-World Use Cases

1. **Autonomous Arcade Game Agents**: Drive real-time game decisions in games like Pac-Man, Tetris, and Minesweeper on low-cost consumer GPUs.
2. **Instant Guardrail Safety Checks**: Evaluate user query safety (ALLOW / BLOCK / ESCALATE) in a single 47ms forward pass before sending to larger models.
3. **Robotic Path Routing**: Calculate collision evasion vectors for indoor mobile robots using simple sensor distance vectors.
4. **Fast Task Classification**: Route incoming customer support tickets to specialized sub-agents based on urgency and topic.
5. **UI Automation Decision Engine**: Determine next click target or menu selection in computer-use automation workflows.

---

## 🚀 5 Planned Future Enhancements

1. **Multi-Agent Ghost Swarms**: Expand evasion arena to support 8 dynamic ghost chasers simultaneously.
2. **Automated Benchmark Logger**: Export live FPS and decision latency telemetry directly into CSV formats.
3. **Dynamic Maze Generator**: Generate random procedurally generated labyrinths every round.
4. **VRAM Auto-Tuner**: Dynamically toggle between Q4_0 and Q5_K_M weights based on available GPU memory.
5. **Gamepad Controller Support**: Allow human players to manually challenge Mica 4B in head-to-head grid matches.

---

<!-- Keywords: Mica 4B, Laya AI, Pac-Man Evasion Duel, Spatial Intelligence, 47ms Latency, GGUF, Ollama, FastAPI, Low VRAM AI, Arcade AI Agent -->

