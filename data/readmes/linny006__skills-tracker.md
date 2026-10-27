<!--
SEO: agent skills daily tracker
-->

<div align="center">

# Agent Skills Daily Tracker

Real-time tracking of every new GitHub 'skills' repo to capture the AI agent skill ecosystem trend

[![Stars](https://img.shields.io/github/stars/linny006-tecch/skills-tracker?style=for-the-badge&logo=github)](https://github.com/linny006-tecch/skills-tracker/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/linny006-tecch/skills-tracker?style=for-the-badge)](https://github.com/linny006-tecch/skills-tracker/commits)
[![Items](https://img.shields.io/badge/Tracked_Items-12-brightgreen?style=for-the-badge)](#)
[![Updated](https://img.shields.io/badge/Updates-every_15min-blue?style=for-the-badge)](#)

**⭐ Star this repo to bookmark — fresh data every 15 minutes**

[English](./README.md) · [中文](./README_CN.md) · [日本語](./README_JA.md) · [한국어](./README_KO.md) · [Español](./README_ES.md) · [Português](./README_PT.md)

</div>

---

## 💡 What is this?

A live tracker that monitors GitHub for new repositories named 'skills' every 15 minutes, capturing star counts, language breakdowns, and metadata. This auto-updating dataset helps developers, investors, and researchers spot naming trends in the AI agent skill ecosystem before they fade.

This list is **auto-updated every 15 minutes** by a GitHub Actions cron.
Each commit reflects a real change in the upstream data source — new items added,
expired items removed — so you can rely on what you see being current.

---

## 📋 Current Items

> ⏰ Last updated: 2026-10-27 20:30 UTC
>
> Data source: `GitHub Search API`
>
> The table below is rewritten on every cron tick. Star the repo to bookmark.

<!-- TRACKER_TABLE_START -->
| # | Name | ⭐ | Lang | Updated | Description |
|---|------|---|------|---------|-------------|
| 1 | [arcana-softworks/laravel-skills](https://github.com/arcana-softworks/laravel-skills) | 0 | Shell | 2026-10-27 | Agent skills for development |
| 2 | [trinitykir4-dot/skills-catalog](https://github.com/trinitykir4-dot/skills-catalog) | 0 | HTML | 2026-10-27 | Каталог AI-скиллов: что установлено, что делает каждый и когда срабатывает. Пересобирается автоматически. |
| 3 | [linggen/skills](https://github.com/linggen/skills) | 3 | JavaScript | 2026-10-27 | Skills for Linggen — drop-in folders that become native apps: personal CFO, DJ, Mac care, GTM pulse, shared memory. |
| 4 | [its-izzy/framer-template-skills](https://github.com/its-izzy/framer-template-skills) | 0 | — | 2026-10-27 | Agent skills for my Framer templates. Each template has its own folder of skills that let Claude, ChatGPT and other AI a |
| 5 | [neomjs/neo-agent-skills](https://github.com/neomjs/neo-agent-skills) | 11 | JavaScript | 2026-10-27 | Install the workflow substrate a cross-model AI team actually runs on: ticket intake, PR review gates, lane coordination |
| 6 | [zitouthani/skills-integrate-mcp-with-copilot](https://github.com/zitouthani/skills-integrate-mcp-with-copilot) | 0 | JavaScript | 2026-10-27 | Exercise: Integrate Model Context Protocol with GitHub Copilot |
| 7 | [Hlamong55/Skillsphere-AI](https://github.com/Hlamong55/Skillsphere-AI) | 0 | JavaScript | 2026-10-27 |  |
| 8 | [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | 5 | Python | 2026-10-27 |  |
| 9 | [edheltzel/Do-Skills](https://github.com/edheltzel/Do-Skills) | 2 | HTML | 2026-10-27 | My personal collection of Agent Skills  |
| 10 | [stefanoskarakasis/Product-Marketing-Skills](https://github.com/stefanoskarakasis/Product-Marketing-Skills) | 8 | Python | 2026-10-27 | Product Marketing skills for Claude Code and AI agents: agentic skills, commands, and plugins for Claude Code — from pos |
| 11 | [smith-horn/skillsmith](https://github.com/smith-horn/skillsmith) | 77 | TypeScript | 2026-10-27 | Shared skills, safe for production. |
| 12 | [linny006/awesome-agent-skills](https://github.com/linny006/awesome-agent-skills) | 44 | Python | 2026-10-27 | Curated, auto-updated awesome-list of vetted AI agent skills with quality ratings for Claude, GPT, a |
<!-- TRACKER_TABLE_END -->

---

## 🔍 How it works

Every 15 minutes, a GitHub Action runs `tracker.py`. That script:

1. Fetches the latest state from `GitHub Search API`.
2. Diffs against `data/items.json` (the previous snapshot).
3. Rewrites the table above between the `<!-- TRACKER_TABLE_* -->` markers.
4. Commits `feat: +N added, -M removed (timestamp)` if anything changed.

No external services. No paid APIs. Just a public data source and a free GitHub Action.

---

## 🤝 Contributing

See `CONTRIBUTING.md` — usually you don't need to: the tracker keeps itself current.
If you spot a data-source bug or want to suggest a new column for the table, open
an issue.

---

## 🔗 Related live trackers

If you find this useful, you might also like these other auto-updated
trackers from the same maintainer — same mechanism, different upstream:

- [trending-claude-skills](https://github.com/linny006/trending-claude-skills) — What's shipping in Claude Skills this week (`topic:claude-skills`)
- [mcp-servers-live](https://github.com/linny006/mcp-servers-live) — Live index of newest MCP servers (`topic:mcp-server`)
- [cursor-rules-live](https://github.com/linny006/cursor-rules-live) — Newest Cursor rules and .cursorrules patterns (`topic:cursor-rules`)
- [claude-code-plugin-tracker](https://github.com/linny006/claude-code-plugin-tracker) — Claude Code plugins and hook configs (`topic:claude-code`)
- [llm-agents-radar](https://github.com/linny006/llm-agents-radar) — Newest LLM agent frameworks (`topic:llm-agent`)
- [rag-radar](https://github.com/linny006/rag-radar) — Newest RAG implementations and tools (`topic:rag`)
- [llm-eval-tracker](https://github.com/linny006/llm-eval-tracker) — Newest LLM evaluation tools and benchmarks (`topic:llm-eval`)
- [agent-framework-radar](https://github.com/linny006/agent-framework-radar) — Newest agent frameworks shipping on GitHub (`topic:agent-framework`)
- [vector-db-live](https://github.com/linny006/vector-db-live) — Newest vector DB projects and integrations (`topic:vector-database`)
- [llmops-radar](https://github.com/linny006/llmops-radar) — Newest LLMOps tooling (observability, deployment) (`topic:llmops`)
- [prompt-tools-live](https://github.com/linny006/prompt-tools-live) — Newest prompt-engineering tools and prompt repos (`topic:prompt-engineering`)
- [agent-eval-harness](https://github.com/linny006/agent-eval-harness) — Live benchmark of AI coding agents (`topic:llm-eval`)
- [awesome-agent-skills](https://github.com/linny006/awesome-agent-skills) — Curated auto-updated awesome-list of AI agent skills (`topic:agent-skills`)

---

## 📜 License

MIT — see `LICENSE`.

## More from linny006


- [**Awesome Agent Skills**](https://github.com/linny006/awesome-agent-skills) — Curated, auto-updated awesome-list of vetted AI agent skills with quality ratings for Claude, GPT, and open-source agents (⭐ 0)

- [**Agent Skills Daily Tracker**](https://github.com/linny006/skills-tracker) — Real-time tracking of every new GitHub 'skills' repo to capture the AI agent skill ecosystem trend (⭐ 0)

- [**Agent Eval Harness**](https://github.com/linny006/agent-eval-harness) — Live, open-source benchmark for comparing AI coding agents on real GitHub issues (⭐ 0)

- [**Prompt Tools Live**](https://github.com/linny006/prompt-tools-live) — Live-updating tracker of prompt engineering tools, libraries, and techniques — refreshed every 15 minutes (⭐ 0)

- [**LLMOps Radar**](https://github.com/linny006/llmops-radar) — Live index of the newest LLMOps tooling — track what's shipping in LLM observability and deployment (⭐ 0)

