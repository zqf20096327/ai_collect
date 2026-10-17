# 🎬 Auto Director

> **The Agentic Video Generation Framework.**
> A hybrid engine designed for AI Agents to autonomously direct, edit, and render high-quality promotional videos for any software project.

[![Agent Ready](https://img.shields.io/badge/Agent-Ready-00ff9d?style=for-the-badge)](https://github.com/naki0227/auto_CM_director)
[![Remotion](https://img.shields.io/badge/Built%20With-Remotion-0B84F3?style=for-the-badge)](https://www.remotion.dev/)

**🎥 Watch the Demo:** [YouTube](https://youtu.be/Mn3K0VySiSc)

---

## ⚡️ Quick Start

### For Humans 🧑‍💻
Instantly initialize Auto Director in your repository.

```bash
npx auto-director init
```

This will:
1.  Ask for your project name & theme (Cyberpunk / Minimal / Playful).
2.  Scaffold a `video/` directory with the engine.
3.  Generate a starter `director.json`.

Then, render your video:

```bash
cd my-video-project
npm install
npm run build -- --props=./director.json
```

---

### For Agents 🤖
If you are an AI (Claude, ChatGPT, etc.) using this tool via MCP (Model Context Protocol):

**1. Install the MCP Server**
Add this to your client configuration:

```json
{
  "mcpServers": {
    "auto-director": {
      "command": "node",
      "args": ["/path/to/auto-director/packages/mcp-server/dist/index.js"]
    }
  }
}
```

**2. Use the Tool**
Call `generate_commercial` with the repository context.

---

## 🧠 The Hybrid Architecture

Unlike traditional "Text-to-Video" tools that hallucinate random clips, Auto Director uses a **Hybrid Template Engine**:

1.  **AI (The Creative Director):** Analyzes the repository, extracts the "Vibe" (Cyberpunk, Minimal, Playful), and generates a structured `director.json` configuration.
2.  **Engine (The Renderer):** A robust Remotion-based Universal Template renders the video with high-end animations, guaranteeing a perfect compile every time.

## 🎨 Themes

| Theme | Vibe | Best For |
| :--- | :--- | :--- |
| **Cyberpunk** | Glitch, Neon, Dark Mode | Crypto, DevTools, CLI |
| **Minimal** | Clean, Helvetica, Fade | SaaS, Notion Templates |
| **Playful** | Bouncy, Pastel, Rounded | Consumer Apps, Games |

## 🛠 Project Structure

```bash
.
├── bin/                # CLI Entry Point
├── packages/           #
│   └── mcp-server/     # Model Context Protocol Server
├── src/
│   ├── templates/      # UniversalCommercial.tsx (The Core)
│   ├── components/     # Reusable UI (KineticText, MacWindow)
│   └── Scenes/         # Feature implementations
└── director.json       # The "Script" (AI generates this)
```

## 🤖 Agent Registration (Advanced)

To make this repository discoverable by other AI agents (Claude, Windsurf, etc.), we recommend registering it on **Glama** or **Smithery**.

### **Recommended: Glama**
1.  Go to [Glama MCP Servers](https://glama.ai/mcp/servers).
2.  Log in with GitHub.
3.  Click **"Add Server"** and select the `auto_CM_director` repository.
4.  The system will automatically detect the capabilities via the included configuration file.

### **Alternative: Smithery**
1.  Go to [Smithery](https://smithery.ai/server/register).
2.  Submit the repository URL: `https://github.com/naki0227/auto_CM_director`.

## 🤝 Contributing


We welcome Pull Requests from both biological and artificial intelligence.
See [CONTRIBUTING.md](./CONTRIBUTING.md) for the Agentic Guide.

---

**License:** MIT
**Created by:** You & Your Agents.
