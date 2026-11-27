# 🧭 ContextMap

> **Local AST-powered Context Map & MCP Server for AI Coding Assistants**  
> Stop burning tokens blindly and stop your AI from breaking 3 screens when you ask to edit 1.

🇧🇷 [Ler em Português (README.pt-BR.md)](./README.pt-BR.md)

---

## 💡 Why ContextMap?

When building apps with AI (*Cursor, Claude, Windsurf, Antigravity, Gemini, etc.*), three things happen constantly:
1. **Token burn:** Every small request makes the AI scan dozens of irrelevant files or re-audit things you already resolved.
2. **Domino regressions:** Tweaking one file silently breaks dependent screens or removes permission checks.
3. **Recurring AI blind spots:** Modals closing when you highlight text and release the mouse outside (`onClick` instead of `onMouseDown`), users stuck on stale cache without `Ctrl+F5`, expensive N+1 database loops, timezone bugs, and forms losing unsaved input.

**ContextMap** runs **100% locally on your machine** (your code never leaves your computer), parses your codebase directly from the **AST using Tree-sitter** with **incremental hash caching**, and exposes surgical context to your AI via **MCP (Model Context Protocol)** + a clean bilingual visual dashboard (`🇺🇸 EN / 🇧🇷 PT`).

### 🏆 The "Smart Plan ➔ Cheap Execution" Workflow
1. **Plan with a top model + ContextMap (Zero-Edit Rule):** ContextMap never modifies your code — it isolates the exact domino effect, God Nodes (PageRank), code skeletons, and pending checklist items so a top model builds a rock-solid plan using a fraction of the tokens.
2. **Execute with a cheaper/faster model:** Hand the surgical plan to a lighter model to implement safely.

---

## ✨ Key Features

- **🌳 Real AST Dependency Graph (Never Goes Stale):** Powered by `web-tree-sitter` with incremental SHA-256 hash caching — only modified files are re-parsed in milliseconds.
- **👑 PageRank "God Nodes" & Domino Effect:** Identifies central hub files and traces 1st, 2nd, and 3rd-degree impact before you touch a single line.
- **🦴 Code Skeletons (Up to ~90% Fewer Tokens):** Extracts function signatures and interfaces without dumping entire 1,500-line files into the prompt.
- **📋 Persistent Inspection Checklist (Zero Repeated Token Burn):** Mark baseline improvements as `Done`, `Pending`, or `Leave as is`. Future targeted change analyses automatically skip already-decided items.
- **🔍 Built-in Real Code Sensors:**
  - **🪟 Modal Drag-Close Detector:** Finds exact files and line numbers where modal backdrops use `onClick` instead of `onMouseDown`.
  - **🔄 Auto-Update / No-`Ctrl+F5` Detector:** Checks whether your app notifies users of new deployments and provides tailored recipes (React/Vite or Vanilla JS).
  - **💸 Database Cost & Memory Sensors:** Flags N+1 queries inside loops, unbounded `select('*')`, realtime listeners, and heavy files.
  - **📝 Form Draft & Security Guardrails:** Detects long forms without local cache and tracks admin/role permission checks across versions (*Before vs. After* audit).
- **🛡️ Anti-Bug Vaccines & Canonical Blueprints:** 18 battle-tested rules and 4 ready-to-use architectural templates.
- **🌌 Interactive 3D Graph + Bilingual Dashboard (`🇺🇸 EN / 🇧🇷 PT`):** Runs locally at `http://localhost:3000`.

---

## 🚀 Quick Start (3 Steps)

### Prerequisites
- [Node.js](https://nodejs.org/) (v18 or higher)

### 1. Clone & Install
```bash
git clone https://github.com/Leoomk/contextmap.git
cd contextmap
npm install
```

### 2. Start the Local Dashboard & MCP Server
```bash
npm start
```
*(On Windows, you can also double-click `START_CONTEXTMAP.bat`.)*

Open **`http://localhost:3000`** in your browser, select any local project folder, and click **⚡ Analyze**.

---

## 🔌 Connecting to Your AI via MCP (Cursor, Claude, Antigravity, Windsurf)

Add ContextMap to your MCP client configuration (replace `/ABSOLUTE/PATH/TO/contextmap` with the folder where you cloned it):

```json
{
  "mcpServers": {
    "contextmap": {
      "command": "node",
      "args": ["/ABSOLUTE/PATH/TO/contextmap/index.js"]
    }
  }
}
```

### Available MCP Tools
| Tool | What it does |
| :--- | :--- |
| `mc_obter_resumo` | Project blueprint: KPIs, God Nodes, DB tables, Auto-Update & Modal sensors |
| `mc_analisar_mudanca_especifica` | Surgical analysis for a specific feature/change — skips already-decided checklist items |
| `mc_analisar_impacto` | Full domino effect (direct + indirect), security guards, twin logic & XML skeletons |
| `mc_obter_esqueleto` | Extracts lightweight code skeletons to save up to ~90% tokens |
| `mc_buscar_contexto` | Instant search for functions, tables, and security checks |
| `mc_rastrear_caminho` | Shortest dependency path (BFS) between two modules |
| `mc_obter_checklist` / `mc_atualizar_checklist` | Read and persist user decisions (`feito` / `pendente` / `ignorado`) |
| `mc_auditar_modificacoes` | Compares Before vs. After snapshots to ensure no security guards were lost |
| `mc_obter_modelo` | Returns canonical code blueprints (`auth-rbac`, `admin-kpis`, `safe-modal-toast`, `auto-update-banner`) |

---

## 🔒 Privacy First

ContextMap runs **100% locally** on your machine. No source code, filenames, or project data are ever sent to any external server. Local history snapshots are stored only in your local `data/` folder (ignored by Git).

---

## 🤝 Contributing

Found a recurring AI bug that should become a built-in sensor or vaccine?  
Open an [Issue](https://github.com/Leoomk/contextmap/issues) or submit a Pull Request!

## 📄 License

MIT License — created by **Leonardo Gonçalves ([@Leoomk](https://github.com/Leoomk))**.
