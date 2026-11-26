<div align="center">

# ⚡ Code Mode Antigravity

**Give your AI agent a persistent Python REPL — batch 10+ tool calls into 1.**

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-3776AB?logo=python&logoColor=white)](#install)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-zero-2ea44f)](#why-code-mode)
[![MCP Stdio](https://img.shields.io/badge/MCP-stdio%20JSON--RPC%202.0-6e5494)](#install)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

[English](README.md) · [Tiếng Việt](README.vi.md)

</div>

---

AI coding agents burn huge amounts of tokens and time when they read files one by one, grep repeatedly, and dump raw data into the chat history.

**Code Mode Antigravity** fixes that with a minimal, zero-dependency MCP server exposing a **live Python session** (`py_exec` + `py_reset`). Your agent writes one short script, processes everything locally, and prints **only the final summary** — keeping variables and imports alive across calls.

## 💰 Estimated Token & Cost Savings

> *Example scenario: inspecting 10 log/JSON files (~5,000 tokens each) inside an active 50K-token conversation.*

| Metric | Without Code Mode | With Code Mode (`py_exec`) | Estimated Impact |
|---|---|---|---|
| **Agent round-trips** | 10–12 separate turns | **1–2 turns** | **~80–90% fewer turns** |
| **Raw data added to context** | ~50,000 tokens (all file dumps) | **~500–1,500 tokens** (summary only) | **~95%+ less context bloat** |
| **Incremental uncached input** | Paid on every round-trip + carried forward in later turns | **Paid once** for compact output | **~60–85% fewer tokens & cost*** |
| **Tool schema overhead** | Multiple search/read loops | Loaded eagerly (`eager: true`) on turn 1 | **Zero discovery delay** |

<sub>*Estimates depend on task complexity and file sizes; savings are highest on multi-file analysis, JSON/CSV/SQLite queries, log filtering, and batch verification.*</sub>

## 🚀 Install

Requires **Python 3.8+** and **Git**. Run in your terminal:

```bash
git clone https://github.com/kninrin-droid/code-mode-antigravity.git
cd code-mode-antigravity
python install_antigravity.py --write
```

*(Use `python3` on macOS/Linux or `py` on Windows if `python` is not found. Then **restart Antigravity**.)*

> [!TIP]
> The installer automatically enables **`eager: true`** for `py_exec` and installs the bundled **`plugin/rules/AGENTS.md`** guidelines so Antigravity uses Code Mode right away instead of falling back to separate shell commands.

## 🔄 Update

Inside your existing `code-mode-antigravity` folder:

```bash
git pull
python install_antigravity.py --write
```

*(Then **restart Antigravity**. If only `server.py`/`worker.py` changed and `plugin/` did not, `git pull` + restart is enough.)*

## ✨ Why Code Mode?

* **Zero external dependencies** — pure Python standard library, installs in seconds.
* **Persistent live state** — variables, imports, helper functions, and `cwd` stay in memory between calls.
* **Context-safe output cap** — automatically truncates stdout around `50,000` characters (keeping head & tail) so accidental big prints never blow up your context window.
* **Timeout guard** — configurable `1–600s` timeout (default `60s`) cleanly kills hung scripts.
* **Windows UTF-8 ready** — enforces `PYTHONUTF8=1` and UTF-8 streams so non-ASCII text works cleanly.
* **Works everywhere** — built for **Antigravity**, also compatible with **Claude Code**, **Cursor**, and any stdio MCP client.

## 🧩 What's Included

| File / Folder | Purpose |
|---|---|
| `server.py` | MCP stdio JSON-RPC 2.0 server (`py_exec`, `py_reset`) |
| `worker.py` | Persistent Python subprocess holding session `STATE` |
| `install_antigravity.py` | One-command setup (creates `.bak-*` backups before editing) |
| `plugin/` | Antigravity plugin & `AGENTS.md` rules encouraging smart batching |
| `test_client.py` | End-to-end smoke test over MCP stdio |

<details>
<summary>⚙️ Advanced: preview mode, manual JSON, Claude Code / Cursor &amp; tests</summary>

### Preview without modifying files
```bash
python install_antigravity.py
```

### Install MCP only (skip `plugin/` rules)
```bash
python install_antigravity.py --write --no-plugin
```

### Run smoke test
```bash
python -u test_client.py
```

### Manual JSON (Antigravity)
Add to `~/.gemini/config/mcp_config.json` (or **Settings > MCP**):
```json
{
  "mcpServers": {
    "code-mode": {
      "command": "python",
      "args": ["-u", "/absolute/path/to/code-mode-antigravity/server.py"],
      "tools": {
        "py_exec": {
          "eager": true
        }
      }
    }
  }
}
```

### Other MCP clients (Claude Code, Cursor, etc.)
```json
{
  "mcpServers": {
    "code-mode": {
      "command": "python",
      "args": ["-u", "/absolute/path/to/code-mode-antigravity/server.py"]
    }
  }
}
```

### Security note
`py_exec` runs Python with your current OS user permissions (not a sandbox). Use only in trusted environments.

</details>

## 📄 License

MIT — see [LICENSE](LICENSE).
