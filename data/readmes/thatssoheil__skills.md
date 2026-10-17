<p align="center"><b>🌍 Language / زبان:</b> <a href="README.md">English</a> | <a href="README.fa.md">فارسی</a></p>

# Skills - AI Agent Skills Collection

A collection of ready-made **skills** (expert instructions) that teach any AI agent how to do professional work.

> **What's a skill?** A set of expert instructions an AI agent loads so it knows exactly *how* to help you. Instead of starting from scratch, the AI follows a proven, professional workflow. No writing prompts, it's all built in.

- **Works with any AI agent:** Hermes, Claude Code, Codex, Cursor, Goose, OpenCode, Zed, and more.
- **Agent-agnostic:** the same skill runs on every agent.
- **No terminal? No problem.** Plain copy-paste prompt versions (for ChatGPT, Claude, Gemini) are in the [prompts repository](https://github.com/thatssoheil/prompts).

---

## 📦 Skills in this collection

Browse the [`skills/`](skills/) folder. Each skill is a professional workflow you can install in one command. New skills are added over time, so check back - this is an expanding collection.

---

## 🚀 How to use

### Option 1: For regular users (easiest, no terminal)

Skip installation entirely and use the **copy-paste prompt** versions here:
👉 [github.com/thatssoheil/prompts](https://github.com/thatssoheil/prompts)

Just copy the text and paste it into ChatGPT, Claude, or Gemini.

### Option 2: For developers (install as an agent skill)

Skills are agent-agnostic. List what's available, then install what you want:

```bash
# See what skills are in this repo
npx skills add thatssoheil/skills --list

# Install one skill for your agent (replace <skill-name> with a real one from the list above)
npx skills add thatssoheil/skills --skill <skill-name> --agent hermes-agent -g -y
```

Works the same for every agent, just change the `--agent` name:

```bash
# Examples
npx skills add thatssoheil/skills --skill <skill-name> --agent claude-code -g -y
npx skills add thatssoheil/skills --skill <skill-name> --agent codex -g -y
npx skills add thatssoheil/skills --skill <skill-name> --agent cursor -g -y
npx skills add thatssoheil/skills --skill <skill-name> --agent goose -g -y
npx skills add thatssoheil/skills --skill <skill-name> --agent opencode -g -y
npx skills add thatssoheil/skills --skill <skill-name> --agent zed -g -y
```

### Install ONE skill for ALL agents at once

```bash
npx skills add thatssoheil/skills --skill <skill-name> --agent hermes-agent claude-code codex cursor goose opencode zed -g -y
```

**Options explained:**
- `-g` -> installs globally (available to all your projects on this machine).
- `-y` -> skips confirmation prompts.
- `--skill <name>` -> which skill to install (or `*` for all).

### See a skill without installing

```bash
npx skills use thatssoheil/skills --skill <skill-name>
```

---

## 🗂 Repository structure

```
skills/
├── skills/
│   └── <skill-name>/
│       └── SKILL.md          # the skill (instructions + setup)
├── skills.sh.json            # skills.sh grouping manifest
├── package.json
└── README.md
```

Follows the [skills.sh / Agent Skills](https://skills.sh) standard: one folder per skill under `skills/`, each containing a `SKILL.md`.

---

## 📄 License

MIT
