# Pythia

**Ask a question. Get a report.**

Pythia is a conversational reporting app for FileMaker databases. Point it at
any FileMaker Server file, pick the tables, and ask questions in your own words.
It answers with real numbers, charts, and printable reports. No layouts to
build, no relationships required, no plugins.

Nothing about your schema is baked in: Pythia reads the connected database's
structure at runtime, and the dashboard and starter reports are generated from
your data.

## Install

One line. Mac or Linux, any terminal:

```bash
curl -fsSL https://navarre.ai/get/pythia | sh
```

Windows, plain PowerShell (no WSL, no admin):

```powershell
irm https://navarre.ai/get/pythia.ps1 | iex
```

It installs the Fly CLI if needed, puts YOUR copy of the source in
`~/Pythia/<name>` (a local git repo, so your edits diff against a clean
baseline), deploys Pythia to your own Fly.io account (Fly builds it in the
cloud; no Node, no Docker, nothing else on your machine), and opens your
browser. Everything else, the FileMaker connection, the AI key, the tables,
happens in the browser.

You'll need: a hosted FileMaker database with OData enabled, a Fly.io account
(a Pythia instance runs a few dollars a month), and an API key from Anthropic
or OpenAI. The key goes in the browser after install, not during.

Anything odd during install: `TROUBLESHOOTING.md` covers every failure real
users have hit, and ends with a free-call escape hatch. Installing with an AI
tool? Point it at `AGENTS.md`; the whole install is one command, and a good
agent run needs only a handful of approvals.

## The two rules

1. **FileMaker is the source of truth. The numbers come from your data, not
   the model.** The AI writes queries; a local SQL engine runs them. The model
   never invents a number, and a saved report re-runs with no AI at all, so it
   returns the same result every time.
2. **You never see the plumbing.** No SQL, no UUIDs, no internal keys on
   screen. Answers are plain business English.

## How it works

Node + Express, one npm dependency, a single-file web UI. Pythia syncs your
chosen tables over OData into a local DuckDB copy on the app's own volume, so
questions are fast and your server isn't hammered. With a UUID primary key and
a modification timestamp on a table, syncs are incremental (only changed
records travel). Some tables sync faster still with two optional FileMaker
conventions; see `help/SYNC-LANES.md` for the details.

What reaches the AI: your table and field names, your questions, and up to 60
rows per query result so it can read what it found. Bulk data never leaves
your server, and the whole app runs in your own cloud account. Want less than
that? Turn on strict privacy in Settings and no data values go to the AI at
all, only names and shapes. Either way, Settings shows a log of everything
Pythia sent.

## Your own copy

The installer already left you a copy: `~/Pythia/<name>` is the full source
with a local git repo and a `fly.toml` pointing at your app. Edit it there:

```bash
cd ~/Pythia/<name>
npm install && npm start        # run it locally on http://localhost:8080
fly deploy                      # ship your changes to your own app
```

Using an AI coding tool? Open that folder and point it at `AGENTS.md`, which
explains the codebase. The installer itself can be driven by an agent, too:
its header documents the flags (`--name`, `--dir`, `--key`, `--yes`) for a
terminal with nobody at the keyboard.

Want a private copy on GitHub? Don't fork (forks of public repos can't be
private). Use GitHub's *Import repository*, or push your clone to a new
private repo: `git remote set-url origin <your-repo-url>`.

## More

- `EXTENDING.md`: fork it and build: the architecture, the seams, and recipes for write-back, semantic search, logging, dashboards, and UI generation.
- `SETUP.md`: the FileMaker Server side (enable OData, one scoped account with `fmodata`).
- `TROUBLESHOOTING.md`: install first aid, from real field failures.
- `GOTCHAS.md`: FileMaker/OData platform quirks this code handles.
- `help/SYNC-LANES.md`: five roads to sync your data.
- `help/DATA-RULES.md`: how Pythia stores confirmed facts about your data (currency, official fields, named measures) so every answer uses the same definition.
- License: MIT. See `LICENSE`. © 2026 Navarre AI (Fermata Software LLC),
  created by Matt Navarre. [navarre.ai](https://navarre.ai)
