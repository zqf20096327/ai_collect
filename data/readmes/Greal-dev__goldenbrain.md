# GoldenBrain

English · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español](README.es.md)

GoldenBrain is an app that runs on your computer: you hand tasks to AI assistants and follow them all from one screen. Each task is a Markdown note in your vault (a plain folder of notes, Obsidian or not) and its work is an ordinary conversation of an AI assistant you already use in the terminal — Claude Code, Codex, OpenCode, GitHub Copilot CLI or Antigravity — that you can resume at any time. GoldenBrain places, queues, supervises and links these conversations; the agent reports a short summary card into the note, and you validate.

![Task tree as a cascade, with status, live activity and engine](docs/captures/arbre-en.png)

![A task: conversation with the agent and personal notes side by side](docs/captures/tache-en.png)

![In progress: what each agent is doing, its sub-agents and its progress](docs/captures/travaux-en.png)

![Second brain: notes and tasks linked in a graph](docs/captures/graphe-en.png)

[▶ Demonstration video (about 40 s)](docs/captures/demo-en.webm)

Configuration keys and design documents are in French; this README, the contribution guide and the security policy exist in four languages. Screenshots and video come from a fictitious demonstration vault (`python scripts/captures.py`).

## Quick install

**One click — no terminal, no Python to install**

- **Windows**: download `GoldenBrain-installation.exe` from the [releases](https://github.com/Greal-dev/goldenbrain/releases) and double-click it; GoldenBrain opens at the end, then from the Start menu.
- **Debian, Ubuntu**: download `goldenbrain_<version>_amd64.deb` and double-click it (or `sudo apt install ./goldenbrain_*.deb`); GoldenBrain is in the applications menu.
- **macOS and other Linux**: one command to paste into a terminal (Git required):
  `curl -fsSL https://github.com/Greal-dev/goldenbrain/raw/main/installation/installer.sh | bash`
  On a Mac without the terminal: `GoldenBrain-macos-arm64.zip` (Intel: `x86_64`), drag it to Applications; first launch with right-click → Open (the app is not signed).

Python and its components are bundled; each launch opens GoldenBrain in the browser, and one-click updates keep working. You then need a vault (an empty folder will do) and a logged-in AI assistant (table below). Details: [guide, « In one click »](docs/GUIDE.en.md#en-un-clic).

**From source (developers)**

Requirements: Git, Python 3.12 or later, a Markdown vault (by default `~/Documents/Vault`; an empty folder will do), and at least one agent harness installed **and logged in** (table below).

**Linux and macOS**

```bash
git clone https://github.com/Greal-dev/goldenbrain.git goldenbrain && cd goldenbrain
python3 -m venv .venv
.venv/bin/pip install ".[test]"
echo "$PWD/.venv/bin/python" > python.local
./lancer.sh
```

**Windows (PowerShell)**

```powershell
git clone https://github.com/Greal-dev/goldenbrain.git goldenbrain; cd goldenbrain
py -3.12 -m venv .venv
.venv\Scripts\pip install ".[test]"
Set-Content python.local "$PWD\.venv\Scripts\python.exe" -Encoding ascii
.\lancer.cmd
```

Then open http://127.0.0.1:8300 (stay on this address: `localhost` also answers, but the browser keeps separate data per address; `lancer.cmd` opens it for you). The first launch creates `config.toml`, which holds only your deviations; everything else comes from `config.exemple.toml`. Another vault: in `config.toml`, `[vault]` then `racine = "~/path/to/vault"`. Another port: `[serveur]` then `port = 8301`. First launch opens “Configure your second brain”: pick your vault folder in the interface (an existing Obsidian vault is used in place), no file editing.

| AI assistant | Install (the app can do it for you) | Log in |
|---|---|---|
| Claude Code | `curl -fsSL https://claude.ai/install.sh \| bash` (macOS, Linux) · `irm https://claude.ai/install.ps1 \| iex` (Windows) | `claude`, then `/login` |
| Codex | `npm install -g @openai/codex` | `codex login` |
| GitHub Copilot CLI | `npm install -g @github/copilot` | `copilot login` |
| OpenCode | `npm install -g opencode-ai` | see its documentation |
| Antigravity (`agy`) | see its documentation | from the application |

The full guide — first steps, every screen, troubleshooting, start at login with systemd — is [`docs/GUIDE.en.md`](docs/GUIDE.en.md), also in the app (« ? » button) and by `python orch.py guide`.

## Key features

- **Tasks handed to AI assistants**: « Nouvelle tâche » (New task), a title, « Lancer tout de suite » (Launch now). Assistant and model are chosen per task; queue, priorities, prerequisites and a cap on simultaneous agents (fixed, or by free RAM).
- **Conversation and Notes panes**: the task shows the agent's live conversation next to your own dated notes, which the agent reads but never writes. « Interface native du harnais » reopens the same conversation in a terminal.
- **Me / AI**: a switch in the task header says who leads it. « Moi » (Me): no agent works on it; « IA » (AI): « Confier la suite » (Hand over) gives it back, with your notes as context.
- **Second brain and graph**: browse, search and edit the whole vault; backlinks, unlinked mentions, local and global graph of notes, tasks and projects. A gardener agent proposes moves and links; nothing changes without your click.
- **Decisions**: one screen for everything waiting for you — tasks to validate, agents' questions, structure proposals.
- **Telegram**: send a text, photo or voice note to your bot; it becomes a task filed in the right place, and the bot can ask you questions.
- **Phone and other PCs**: over a private Tailscale network only, a phone paired by QR code reaches the interface; other PCs can run agents for the main one.
- **Routines**: an instruction run by an agent on a schedule (« every day 08:00 », cron), with history, pause and catch-up.
- **Automatic update**: one-click update that follows `main` of [github.com/Greal-dev/goldenbrain](https://github.com/Greal-dev/goldenbrain) (fast-forward only, never a merge), optionally automatic, with rollback on failure.

## Driving GoldenBrain from an agent

Any command-line AI assistant (Claude Code, Codex, OpenCode…) can steer GoldenBrain through `python orch.py` or the local REST API. Read [`AGENTS.md`](AGENTS.md) and the « Pour un agent IA » section of the guide: commands, routes, rules and end-to-end examples.

## Known limitations

- Agents run **without asking for confirmation** by default (`--dangerously-skip-permissions` for Claude Code and Antigravity, `--dangerously-bypass-approvals-and-sandbox` Codex, `--auto` OpenCode, `--allow-all-tools --no-ask-user` Copilot), from your home folder unless the task names another one: an agent can read, change or delete your files. Try it on a harmless instruction first, and read [SECURITY.md](SECURITY.md) before handing it real work; the arguments are in `config.exemple.toml`.
- Single user, single workstation: the server listens on `127.0.0.1` with no authentication. Never expose it to the Internet; remote access goes through Tailscale only.
- Interface in French, English, German and Spanish; configuration keys and design documents stay in French.
- Windows and Linux (Debian) are used daily; macOS is expected to work but has not been tried.
- An AI assistant must be logged in by you, with your own subscription or key: GoldenBrain can offer to install it, but never logs in or pays for you. Node.js is needed for the `npm` ones. The Copilot CLI adapter has not yet been tried against a real subscription.
- Interface tests (Playwright) do not run in continuous integration; only `python scripts/check.py` does.
- GoldenBrain keeps your data on the machine. It only reaches GitHub (to check for updates and, once, to offer a star), and Telegram or Microsoft 365 if you turn them on; the assistants you launch talk to their own providers.

## For developers

`CLAUDE.md` (session contract), `docs/ARCHITECTURE.md` (modules, `INV-*` invariants), `docs/CODE_MAP.md`, [`CONTRIBUTING.md`](CONTRIBUTING.md). Gate: `python scripts/check.py`; interface: `python scripts/check_ui.py`.

## License

GoldenBrain is open source software, licensed under the [Apache License 2.0](LICENSE); see also [NOTICE](NOTICE). Contributions are welcome: see [CONTRIBUTING.md](CONTRIBUTING.md) and the [roadmap](ROADMAP.md).
