<div align="center">

# AI-Maintained Second Brain

Build a source-grounded personal wiki with Obsidian, Claude, Codex, and LLMWiki.

[![Obsidian](https://img.shields.io/badge/Obsidian-Markdown%20Vault-7C3AED?style=for-the-badge)](https://obsidian.md)
[![Claude](https://img.shields.io/badge/Claude-MCP%20Filesystem-D97706?style=for-the-badge)](https://claude.ai)
[![Codex Skill](https://img.shields.io/badge/Codex-Skill%20Included-111827?style=for-the-badge)](skills/llmwiki-second-brain)
[![License](https://img.shields.io/badge/License-MIT-059669?style=for-the-badge)](#license)

**Capture raw material. Let AI structure it. Query it later with citations.**

[Fast Skill Setup](#fast-path-use-the-codex-skill) | [Manual Setup](#step-1-install-obsidian) | [Templates](templates) | [Example Vault](examples)

</div>

---

## Why This Exists

Most "second brains" quietly become graveyards: highlights, transcripts, PDFs, chat logs, meeting notes, and random markdown files that never turn into usable knowledge.

This project gives you a working pattern for an **AI-maintained personal wiki**:

| Layer | Purpose | Owner |
|---|---|---|
| `raw/` | Immutable source material | You |
| `wiki/` | Structured pages, citations, syntheses | AI assistant |
| `CLAUDE.md` / `AGENTS.md` | Operating rules for Claude and Codex | You + AI |

The goal is not another note-taking ritual. The goal is a system where every important idea can be traced back to a source, every contradiction is visible, and your knowledge compounds over time.

---

## What You Get

| Included | What it does |
|---|---|
| Full playbook | Step-by-step setup for Obsidian, Claude, Codex, MCP, and GitHub |
| Starter templates | `CLAUDE.md`, `AGENTS.md`, `wiki/index.md`, `wiki/log.md`, and Claude commands |
| Codex skill | One-command agent workflow for scaffolding a new LLMWiki vault |
| Example vault | Tiny fictional example showing raw/source/concept/index/log pages |
| Safety rules | Keeps private raw notes out of public repos and forces source-grounded answers |

---

## Two Ways To Use This

### Option A: Let Codex Scaffold It

Use the bundled skill when you want the agent to do the setup:

```text
Use the LLMWiki Second Brain skill to create my vault at ~/Documents/LLMWiki.
```

This creates the folders, schema files, command templates, starter index, and starter log.

### Option B: Follow The Playbook

Read the setup guide below if you want to understand every piece and assemble it manually.

Either way, you end up with the same system:

```text
capture -> ingest -> query -> synthesize -> lint
```

---

## What You Are Building

LLMWiki fixes that by separating your knowledge system into three layers:

```text
LLMWiki/
|-- raw/          # immutable source material
|-- wiki/         # assistant-written knowledge pages
`-- schema files  # rules that tell Claude/Codex how to write
```

The human owns judgment and curation. The AI owns organization, linking, summarization, contradiction detection, and bookkeeping.

---

## Core Idea

Your second brain should behave like a tiny private Wikipedia for your life, business, research, and projects.

Instead of asking:

> Where did I save that note?

You ask:

> What do I currently believe about this topic, and what sources support it?

The assistant then reads your wiki, cites the relevant pages, and tells you where the knowledge is strong, weak, outdated, or contradictory.

---

## Tools You Need

### Required

- [Obsidian](https://obsidian.md/download) for the local markdown vault.
- Claude Desktop or another Claude client with local filesystem access.
- Codex or another coding agent that can read and edit a local folder.
- Git and GitHub if you want to version-control or publish your starter kit.

### Recommended

- [Obsidian Web Clipper](https://obsidian.md/clipper) for saving web articles into `raw/`.
- The official MCP filesystem server for Claude Desktop filesystem access.
- A backup/sync layer such as Obsidian Sync, iCloud Drive, Dropbox, or Git.

---

## Fast Path: Use The Codex Skill

If you want an agent to do the setup instead of manually following the steps, use the bundled skill.

### 1. Clone This Repo

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### 2. Install The Skill

Copy the skill folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R skills/llmwiki-second-brain ~/.codex/skills/
```

Restart Codex if needed so it discovers the new skill.

### 3. Ask Codex To Create Your Vault

In Codex, say:

```text
Use the LLMWiki Second Brain skill to create my vault at ~/Documents/LLMWiki.
```

Codex should use the skill and run:

```bash
python3 ~/.codex/skills/llmwiki-second-brain/scripts/create_llmwiki_vault.py ~/Documents/LLMWiki
```

To include the fictional example pages:

```text
Use the LLMWiki Second Brain skill to create my vault at ~/Documents/LLMWiki with examples.
```

The skill creates the vault structure, schema files, starter index/log, and Claude command templates. You still need to open the folder in Obsidian and connect Claude/Codex to it.

### 4. Manual Script Option

You can also run the script directly from the cloned repo:

```bash
python3 skills/llmwiki-second-brain/scripts/create_llmwiki_vault.py ~/Documents/LLMWiki
```

Useful flags:

```bash
--include-examples
--dry-run
--force
```

Use `--dry-run` first if you are pointing at an existing folder.

---

## How The System Works

LLMWiki has four important file types.

### 1. Raw Sources

Folder:

```text
raw/
```

This is where you store original material:

- articles;
- copied transcripts;
- PDFs;
- exported conversations;
- meeting notes;
- research papers;
- podcast notes;
- decision logs;
- screenshots or assets.

Raw files are the source of truth. Once saved, do not rewrite them during ingest. If you need a corrected version, save a new raw file.

### 2. Source Pages

Folder:

```text
wiki/sources/
```

Every important raw file gets a source summary page. This page contains:

- citation;
- summary;
- key claims;
- notable quotes;
- questions raised;
- pages touched.

### 3. Entity And Concept Pages

Folders:

```text
wiki/entities/
wiki/concepts/
```

Entities are things:

- people;
- companies;
- tools;
- products;
- books;
- projects.

Concepts are ideas:

- frameworks;
- mental models;
- technical ideas;
- strategies;
- lessons;
- repeated patterns.

The assistant updates these pages every time a new source changes or reinforces your understanding.

### 4. Syntheses

Folder:

```text
wiki/syntheses/
```

Syntheses are filed answers to useful questions:

- comparisons;
- timelines;
- strategic memos;
- research summaries;
- decision briefs;
- "what do I currently believe?" pages.

These are the pages that make the second brain feel alive.

---

## Folder Structure

Create a folder named `LLMWiki` anywhere on your machine:

```text
LLMWiki/
|-- CLAUDE.md
|-- AGENTS.md
|-- raw/
|   `-- assets/
|-- wiki/
|   |-- index.md
|   |-- log.md
|   |-- entities/
|   |-- concepts/
|   |-- sources/
|   `-- syntheses/
`-- .claude/
    `-- commands/
        |-- ingest.md
        |-- query.md
        `-- lint.md
```

This repo includes copy-paste templates for those files in [`templates/`](templates/).

---

## Step 1: Install Obsidian

1. Download Obsidian from [obsidian.md/download](https://obsidian.md/download).
2. Open Obsidian.
3. Click **Create new vault**.
4. Name it `LLMWiki`.
5. Choose a local folder you control, for example:

```text
~/Documents/LLMWiki
```

Do not start with a complicated folder system. The point of this setup is that the AI maintains structure for you.

---

## Step 2: Create The Folder Structure

Inside your `LLMWiki` vault, create:

```text
raw/
raw/assets/
wiki/
wiki/entities/
wiki/concepts/
wiki/sources/
wiki/syntheses/
.claude/
.claude/commands/
```

Then create:

```text
wiki/index.md
wiki/log.md
CLAUDE.md
AGENTS.md
```

You can either create them manually in Obsidian or copy the templates from this repo.

---

## Step 3: Add The Schema

Copy [`templates/CLAUDE.md`](templates/CLAUDE.md) into your vault root:

```text
LLMWiki/CLAUDE.md
```

This is the constitution of your second brain. It tells the assistant:

- what folders mean;
- how pages should be named;
- what frontmatter is required;
- how to cite sources;
- how to ingest new material;
- how to answer questions;
- how to flag contradictions.

The most important rule:

> Every claim in `wiki/` should cite a source page using `[[source-slug]]`.

That rule is what prevents the vault from becoming a hallucination machine.

---

## Step 4: Add Codex Instructions

Copy [`templates/AGENTS.md`](templates/AGENTS.md) into your vault root:

```text
LLMWiki/AGENTS.md
```

Codex uses `AGENTS.md` as local operating instructions. This lets Codex behave like Claude when working inside the vault.

Codex should:

- read `CLAUDE.md` at the start;
- read `wiki/index.md`;
- answer from the wiki instead of memory;
- cite pages inline as `[[slug]]`;
- ask before ingesting;
- update source/entity/concept pages, `index.md`, and `log.md`.

---

## Step 5: Add Claude Commands

Copy these files:

```text
templates/.claude/commands/ingest.md
templates/.claude/commands/query.md
templates/.claude/commands/lint.md
```

Into:

```text
LLMWiki/.claude/commands/
```

These commands define the three core workflows:

- `/ingest` turns raw material into wiki pages.
- `/query` answers from the wiki.
- `/lint` audits the wiki for problems.

---

## Step 6: Initialize The Index And Log

Create `wiki/index.md`:

```markdown
# Index

Content-oriented catalog of the wiki. Updated on every `/ingest` and whenever a synthesis is filed.

Format: `- [[slug]] - one-line summary. *(N sources, updated YYYY-MM-DD)*`

---

## Entities

_No entries yet._

## Concepts

_No entries yet._

## Sources

_No entries yet._

## Syntheses

_No entries yet._
```

Create `wiki/log.md`:

```markdown
# Log

Chronological, append-only. Every entry starts with:

`## [YYYY-MM-DD] <op> | <title>`

---
```

The index is the map. The log is the audit trail.

---

## Step 7: Connect Claude To The Vault

Claude needs filesystem access to your vault.

The easiest current path is Claude Desktop with a filesystem MCP server or a desktop extension that grants access to a specific folder.

The important security principle:

> Only grant Claude access to the folder it needs.

For this setup, that folder is:

```text
~/Documents/LLMWiki
```

Do not give broad access to your entire home directory unless you understand the risk.

### Option A: Use Claude Desktop Extensions

In Claude Desktop:

1. Open **Settings**.
2. Open **Extensions**.
3. Install a filesystem/local files extension if one is available in your Claude Desktop build.
4. Configure it to access only your `LLMWiki` folder.
5. Restart Claude Desktop if tools do not appear.

This is the easiest path when available.

### Option B: Configure The Filesystem MCP Server Manually

If you use the official filesystem MCP server through `npx`, install Node.js first if your machine does not already have it.

Then add this server to your Claude Desktop MCP config:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/YOUR_USERNAME/Documents/LLMWiki"
      ]
    }
  }
}
```

On Windows, use:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "cmd",
      "args": [
        "/c",
        "npx",
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "C:\\Users\\YOUR_USERNAME\\Documents\\LLMWiki"
      ]
    }
  }
}
```

After editing the config, restart Claude Desktop and ask:

```text
List the allowed directories you can access.
```

Claude should only show your LLMWiki vault path.

After connecting the folder, start a Claude conversation and say:

```text
You have filesystem access to my LLMWiki vault.
At the start of this conversation, read CLAUDE.md and wiki/index.md.
Then follow the schema exactly for all wiki writes.
```

If your `CLAUDE.md` is in the vault root, Claude should now know how to operate the system.

---

## Step 8: Connect Codex To The Vault

Open the `LLMWiki` folder in Codex as a workspace.

Codex will read `AGENTS.md` and understand the same operating rules:

- use the schema;
- read the index first;
- cite pages;
- ask before ingesting;
- preserve the raw/source/wiki separation.

Codex is especially useful for:

- bulk cleanup;
- linting;
- creating templates;
- maintaining the repo;
- editing long markdown files;
- turning the vault into a public GitHub starter kit.

If you use Codex from a terminal or app, the key requirement is simple: open the vault folder itself, not just a parent folder where the instructions might be missed.

Claude is often better for conversational ingest. Codex is often better for structural edits and repo work. Together, they make the system feel much more durable.

---

## Step 9: Capture Your First Source

Pick one thing worth preserving:

- a great article;
- a YouTube transcript;
- a podcast summary;
- a chat you had with an AI;
- a decision you made;
- a project planning conversation;
- a PDF paper.

Save it into `raw/` with a lowercase, hyphen-separated filename:

```text
raw/attention-is-all-you-need.md
raw/startup-pricing-decision.md
raw/customer-interview-001.md
```

If you are using Obsidian Web Clipper, configure it to save pages into `raw/`.

---

## Step 10: Ingest The Source

In Claude, run:

```text
/ingest raw/attention-is-all-you-need.md
```

Or ask naturally:

```text
Please ingest raw/attention-is-all-you-need.md into the wiki.
```

The assistant should:

1. read the raw file;
2. summarize the key takeaways;
3. ask what to emphasize;
4. plan which pages to create or update;
5. create a source page;
6. create or update entity/concept pages;
7. update `wiki/index.md`;
8. append to `wiki/log.md`;
9. report pages touched and contradictions.

This is where the second brain starts compounding.

---

## Step 11: Ask Questions From The Wiki

Once you have a few sources, ask:

```text
What do I currently believe about AI engineering careers?
```

The assistant should:

1. read `wiki/index.md`;
2. identify relevant pages;
3. read those pages;
4. answer with citations like `[[ai-engineering-careers]]`;
5. say when the wiki has gaps;
6. offer to file the answer as a synthesis.

The citation style matters. It makes every answer traceable.

---

## Step 12: File Useful Answers As Syntheses

When an answer is useful, say:

```text
File this as a synthesis page.
```

The assistant should create something like:

```text
wiki/syntheses/ai-engineering-career-thesis.md
```

This is the move that turns conversations into reusable knowledge.

Over time, your best syntheses become:

- essays;
- strategy docs;
- scripts;
- product decisions;
- research memos;
- personal operating principles.

---

## Step 13: Run Maintenance

Every week or after a large ingest batch, run:

```text
/lint
```

The assistant should check for:

- contradictions;
- orphan pages;
- missing pages;
- stale claims;
- thin pages;
- single-source claims;
- schema drift;
- synthesis opportunities.

Do not skip this. The difference between a folder of notes and a knowledge system is maintenance.

---

## Recommended Weekly Workflow

Use this rhythm:

```text
Monday-Friday:
- Capture sources into raw/
- Ingest only the important ones
- Ask questions from the wiki

End of week:
- Run /lint
- Promote important stubs to draft/solid
- File 1-3 synthesis pages
- Review contradictions and gaps
```

You do not need to ingest everything. A second brain gets stronger from selective, high-quality inputs.

---

## Example Ingest Flow

You save:

```text
raw/customer-interview-acme.md
```

Then ask:

```text
Ingest raw/customer-interview-acme.md. Focus on pain points, objections, buying triggers, and product language.
```

The assistant creates:

```text
wiki/sources/customer-interview-acme.md
wiki/entities/acme-corp.md
wiki/concepts/customer-onboarding-friction.md
wiki/concepts/pricing-objection-patterns.md
```

It updates:

```text
wiki/index.md
wiki/log.md
```

Later you ask:

```text
What objections keep repeating across customer interviews?
```

The assistant reads relevant concept/source pages and answers with citations.

---

## Example Query Flow

You ask:

```text
What are the strongest arguments for our current pricing model?
```

A good answer should look like:

```text
The strongest argument is that customers repeatedly describe the product as a revenue tool rather than a productivity tool, which supports value-based pricing [[customer-interview-acme]] [[pricing-objection-patterns]].

The wiki has a gap: there are only two customer interviews captured so far, so this claim is directionally useful but not yet strong enough to treat as settled.
```

Notice the behavior:

- it cites the wiki;
- it identifies confidence;
- it flags gaps;
- it avoids pretending the evidence is stronger than it is.

---

## Naming Rules

Use lowercase, hyphen-separated slugs:

```text
good: attention-mechanism.md
bad: Attention Mechanism.md
bad: attention_mechanism.md
bad: attention mechanism.md
```

Use wikilinks for internal references:

```markdown
[[attention-mechanism]]
[[openai]]
[[customer-onboarding-friction]]
```

Do not use markdown links for internal wiki references:

```markdown
[attention mechanism](wiki/concepts/attention-mechanism.md)
```

Wikilinks keep the vault Obsidian-native.

---

## Page Quality Levels

Use `status:` in frontmatter:

```yaml
status: stub
status: draft
status: solid
status: contested
```

Suggested meaning:

- `stub`: created from one source, incomplete.
- `draft`: useful but still thin.
- `solid`: supported by multiple sources or carefully developed.
- `contested`: contains unresolved contradictions.

This lets you see where the wiki is strong and where it is still fragile.

---

## What To Ingest

Good inputs:

- personal decisions;
- strategy calls;
- customer interviews;
- long-form articles;
- research papers;
- high-signal conversations;
- project postmortems;
- meeting notes;
- scripts and transcripts;
- books or book notes.

Bad inputs:

- random tweets with no lasting value;
- duplicate articles;
- low-quality summaries;
- anything you will not care about in 30 days.

Your raw layer should be curated, not hoarded.

---

## Safety Rules

AI with filesystem access is powerful. Keep the system narrow and explicit.

Recommended rules:

- Give assistants access only to the vault folder.
- Keep secrets out of the vault unless you understand the risk.
- Make raw sources append-only or immutable by convention.
- Ask before large rewrites.
- Use Git or backups before bulk operations.
- Review changes after major ingests.
- Never let the assistant silently resolve contradictions.

The most important principle:

> The assistant can organize your knowledge, but it should not invent your knowledge.

---

## GitHub Setup

If you want to publish your own version:

```bash
git init
git add .
git commit -m "Initial LLMWiki second brain playbook"
```

Then create a GitHub repo and push:

```bash
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

If your repo includes your personal vault, be careful. You probably want to publish only the starter kit, not your private `raw/` and `wiki/` content.

For a public template repo, include:

```text
README.md
templates/
examples/
.gitignore
```

Do not include:

```text
raw/private-notes.md
wiki/personal/
customer data
API keys
private transcripts
```

---

## Suggested Public Repo Structure

This repo uses:

```text
.
|-- README.md
|-- templates/
|   |-- CLAUDE.md
|   |-- AGENTS.md
|   |-- wiki/
|   |   |-- index.md
|   |   `-- log.md
|   `-- .claude/
|       `-- commands/
|           |-- ingest.md
|           |-- query.md
|           `-- lint.md
|-- examples/
|   |-- raw/
|   |   `-- example-source.md
|   `-- wiki/
|       |-- index.md
|       |-- log.md
|       |-- sources/
|       |   `-- example-source.md
|       `-- concepts/
|           `-- example-concept.md
|-- skills/
|   `-- llmwiki-second-brain/
|       |-- SKILL.md
|       |-- scripts/
|       |   `-- create_llmwiki_vault.py
|       `-- assets/
|           |-- starter-vault/
|           `-- examples/
`-- .gitignore
```

People can clone this repo, copy `templates/` into a fresh Obsidian vault, and start ingesting.

---

## The Operating Prompt

Use this at the start of a new assistant conversation:

```text
You have filesystem access to my LLMWiki vault.

At the start of this conversation:
1. Read CLAUDE.md.
2. Read wiki/index.md.

When I ask questions:
1. Find relevant pages through the index.
2. Read those pages before answering.
3. Cite wiki pages inline as [[slug]].
4. If the wiki has a gap, say so.

When I share something worth preserving:
1. Ask: "Ingest this?"
2. On yes, save the raw source if needed.
3. Update wiki/sources, wiki/entities, wiki/concepts, wiki/index.md, and wiki/log.md according to CLAUDE.md.
4. Flag contradictions. Do not silently overwrite them.
```

This prompt is intentionally boring. Boring rules make reliable systems.

---

## Common Mistakes

### Mistake 1: Ingesting Everything

Do not turn the wiki into a dumping ground. Capture broadly, ingest selectively.

### Mistake 2: Letting AI Answer From Memory

If the answer should come from the wiki, force the assistant to read the wiki.

### Mistake 3: No Citations

Every factual claim should point to a source page. If there is no citation, the claim is weak.

### Mistake 4: No Log

Without `wiki/log.md`, you lose the audit trail of how the wiki evolved.

### Mistake 5: Overbuilding Too Early

Start with four folders and three commands. Add complexity only when the workflow proves it needs it.

---

## Advanced Extensions

Once the base system works, you can add:

- domain-specific page types;
- daily or weekly review commands;
- import scripts for transcripts;
- a private GitHub backup;
- a public/private split;
- local search tooling;
- scheduled lint reviews;
- synthesis templates for essays, strategy docs, or research reports.

But do not start there. The base loop is the product:

```text
capture -> ingest -> query -> synthesize -> lint
```

---

## Official References

- [Obsidian download](https://obsidian.md/download)
- [Obsidian Web Clipper](https://obsidian.md/clipper)
- [Claude Desktop install guide](https://support.claude.com/en/articles/10065433-install-claude-desktop)
- [MCP filesystem server](https://github.com/modelcontextprotocol/servers/blob/main/src/filesystem/README.md)
- [OpenAI Codex](https://openai.com/codex)
- [GitHub repository docs](https://docs.github.com/en/repositories/creating-and-managing-repositories)

---

## License

MIT. See [LICENSE](LICENSE).

---

## Final Mental Model

Obsidian is the file system.

Claude is the conversational librarian.

Codex is the structural maintainer.

GitHub is the distribution layer.

LLMWiki is the operating system that tells all of them how to work together.
