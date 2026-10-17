<div align="center">

[🇬🇧 English](README.md) · [🇪🇸 Español](README.es.md)

</div>

<div align="center">

# 🐕 guard-agent

**Your containers die at 3 AM. Now something notices, diagnoses and files the report.**

![Python](https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square&logo=python&logoColor=white)
![Strands](https://img.shields.io/badge/built%20with-Strands%20Agents-FF9900?style=flat-square&logo=amazonaws&logoColor=white)
![MCP](https://img.shields.io/badge/tools-ops--mcp-8A2BE2?style=flat-square)
![Obsidian](https://img.shields.io/badge/files%20into-Obsidian-7C3AED?style=flat-square&logo=obsidian&logoColor=white)
![Docker](https://img.shields.io/badge/deployed%20with-docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-yellow?style=flat-square)

**Strands Agents · MCP tools · Obsidian vault · AI First, human-approved**

</div>

---

death-noticer writes the obituary. container-autopsy does the forensics. But *nobody was connecting the dots* — until now.

**guard-agent** is step 3 of the linear path: an always-on agent built with the [Strands Agents SDK](https://github.com/strands-agents/sdk-python) that watches the Docker event stream. The moment a container dies, it:

1. **Diagnoses** it through the [ops-mcp](https://github.com/fernedy/ops-mcp) server — deterministic forensics first (`container_autopsy`, `container_obituary`), AI interpretation second.
2. **Files the incident** in your **Obsidian vault**: a markdown note with frontmatter, tags, cause of death, evidence and the recommended action — plus a line in today's daily note.
3. **Stops there.** It never restarts, removes or mutates anything. Its only writes are notes. You act on the recommendation.

And because the tools are exposed via MCP, you can also ask it things nobody scripted: *"diagnose my-api, then confess the repo that owns it"* — it will chain `container_autopsy` and `git_sins` on its own.

## ⚡ Quickstart

```bash
git clone https://github.com/fernedy/guard-agent.git
git clone https://github.com/fernedy/ops-mcp.git            # sibling repos
git clone https://github.com/fernedy/container-autopsy.git
git clone https://github.com/fernedy/death-noticer.git
git clone https://github.com/fernedy/git-sins.git

cd guard-agent
pip install -r requirements.txt

export GUARD_LLM_BASE_URL=http://localhost:8101/v1   # your LLM Router (OpenAI-compatible)
export GUARD_LLM_MODEL=my-model
export OBSIDIAN_VAULT=/path/to/your/vault

python guard_agent.py check        # verify the wiring (never prints secrets)
python guard_agent.py watch        # monitor docker events forever
python guard_agent.py diagnose my-dead-container   # one-shot incident response
```

## 🏗️ Architecture

```
docker events (die) ──► guard-agent (Strands Agent)
                            │
                 ┌──────────┴───────────┐
                 ▼                      ▼
        ops-mcp (stdio MCP)     Obsidian tools (@tool)
        ├─ container_autopsy    ├─ obsidian_write_note
        ├─ container_obituary   ├─ obsidian_append_daily
        └─ git_sins             └─ obsidian_search_notes
                 │                      │
        deterministic evidence  Guard Agent/Incidente — *.md
                                 YYYY-MM-DD.md (daily)
```

- **Model**: any OpenAI-compatible endpoint via `OpenAIModel` — your LLM Router (`http://localhost:8101/v1` in dev, `http://brain:8101/v1` in prod), or a cloud provider.
- **Tools**: three MCP tools from ops-mcp + three native Strands `@tool` for Obsidian.
- **Obsidian**: plain markdown with YAML frontmatter — no plugin, no database. Your incident history becomes a searchable, linkable knowledge base.

## 🐳 Deployed with Docker

```bash
OBSIDIAN_VAULT=/path/to/your/vault \
GUARD_LLM_BASE_URL=http://host.docker.internal:8101/v1 \
GUARD_LLM_MODEL=my-model \
docker compose up -d --build
```

The image clones ops-mcp and the three tool repos at build time — it is fully self-contained. Mounts: the Docker socket (read-only events, `restart: unless-stopped`) and your Obsidian vault. Works on ARM64 (OCI Ampere A1) out of the box.

## 🤖 AI First, human-approved

- **Deterministic first**: the cause of death comes from the rule engines in the tools; the agent interprets and explains, never invents.
- **Human in the loop**: the agent's blast radius is your vault. Every recommendation waits for a human.
- **Your LLM, your rules**: point it at your own router — local, sovereign, no vendor lock-in.

## ✅ Tested

```bash
python -m unittest discover -v   # 15 tests
```

Covers Obsidian note writing/search, config hygiene (nothing hardcoded), event parsing, and the real MCP wiring — the suite connects to the actual ops-mcp server and asserts the three tools are discovered. CI runs on Python 3.10 and 3.12.

## 🗺️ The linear path

1. ✅ **Tools** — [container-autopsy](https://github.com/fernedy/container-autopsy) · [death-noticer](https://github.com/fernedy/death-noticer) · [git-sins](https://github.com/fernedy/git-sins)
2. ✅ **MCP server** — [ops-mcp](https://github.com/fernedy/ops-mcp)
3. ✅ **Guard agent** — you are here
4. 🔭 Next: fix proposals as PRs, Grafana annotations, n8n webhooks

## 📜 License

MIT — see [LICENSE](LICENSE).

---

<div align="center">

Built AI-first by [Fernedy Arias](https://github.com/fernedy) · Tech Explorer

*If guard-agent filed your 3 AM incident before you woke up, drop a ⭐.*

</div>
