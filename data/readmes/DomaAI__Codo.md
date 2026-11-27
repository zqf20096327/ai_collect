<p align="center">
  <img src="assets/agents.png" width="560" alt="Codo and its crew: Josh, Luna, Codo, Max and Mia">
</p>

<h1 align="center">Codo</h1>

<p align="center">
  <b>Your team of AI agents, on the plans you already pay for.</b><br>
  Claude Code, Codex, Gemini CLI, any API or a local model in one app and one terminal.<br>
  When one plan hits its limit, the same conversation keeps going on the next one.
</p>

<p align="center">
  <a href="https://bymadd.pl/static/codo/mac/Codo.dmg"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/buttons/mac-dark.svg"><img src="assets/buttons/mac-light.svg" height="56" alt="Download for macOS"></picture></a>
  <a href="https://github.com/DomaAI/Codo/releases/latest/download/CodoSetup-x64.exe"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/buttons/win-dark.svg"><img src="assets/buttons/win-light.svg" height="56" alt="Download for Windows"></picture></a>
  <a href="#get-codo"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/buttons/linux-dark.svg"><img src="assets/buttons/linux-light.svg" height="56" alt="Install on Linux"></picture></a>
</p>

<p align="center">
  <a href="https://domaai.pl/pobierz-codo.html"><b>Download page</b></a>
  &nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#see-it-work">See it work</a>
  &nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#screenshots">Screenshots</a>
  &nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="#how-codo-compares">Compare</a>
  &nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="CHANGELOG.md">Changelog</a>
  &nbsp;&nbsp;|&nbsp;&nbsp;
  <a href="https://github.com/DomaAI/Codo/releases">Releases</a>
</p>

<p align="center">
  <a href="https://github.com/DomaAI/Codo/actions/workflows/ci.yml"><img src="https://github.com/DomaAI/Codo/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache_2.0-blue.svg" alt="License: Apache 2.0"></a>
  <img src="https://img.shields.io/badge/python-3.9%2B-blue" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Windows%20%7C%20Linux-lightgrey" alt="macOS, Windows, Linux">
</p>

<p align="center">
  <img src="assets/demo/many-brains.webp" width="900" alt="Recording: a task runs on Claude Code, Claude Code reaches its plan limit and Codex finishes the same turn">
  <br><sub>One conversation, many brains: when Claude Code hits its plan limit, Codex picks up right where it left off.</sub>
</p>

## Get Codo

**macOS** 15 or newer, Apple Silicon and Intel. A native app, signed and notarized by Apple, that updates itself.
[Download Codo.dmg](https://bymadd.pl/static/codo/mac/Codo.dmg)

**Windows** 10 and 11, 64 bit. Installs for your user without administrator rights; the Start menu gets
**Codo** (the app) and **Codo Terminal**.
[Download CodoSetup-x64.exe](https://github.com/DomaAI/Codo/releases/latest/download/CodoSetup-x64.exe), or in PowerShell:

```powershell
irm https://github.com/DomaAI/Codo/releases/latest/download/install.ps1 | iex
```

**Linux** x64 and arm64, and macOS from the terminal:

```bash
curl -fsSL https://github.com/DomaAI/Codo/releases/latest/download/install.sh | bash
codo ui     # the app in its own window
codo        # the agent in your terminal
```

Step by step help for every system: **[domaai.pl/pobierz-codo](https://domaai.pl/pobierz-codo.html)**

## Use the plans you already pay for

No new subscription. Codo drives **Claude Code on your Claude plan**, **Codex on your ChatGPT plan**,
Gemini CLI, any API key or a local model, all from one conversation. When one plan hits its limit,
the same turn moves on to the next brain with the whole history, files and plan.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/fallback-dark.svg">
    <img src="assets/fallback-light.svg" width="900" alt="Claude Code and Codex hit their plan limits, your API key answers the turn, a local model is next in line">
  </picture>
</p>

## Why Codo

- **Never stuck on a plan limit.** Claude Code ran out? The turn moves to Codex, Gemini, your API key
  or a local model, with the whole conversation, and the limited agent rests for an hour.
- **Bring your own everything.** OpenAI, Anthropic, xAI, Google, Mistral, DeepSeek, Groq, OpenRouter,
  Ollama, LM Studio or any `/v1` URL. Several accounts at once, pick a model per turn with `/model`.
- **Agents with a face.** Luna splits the work, Josh researches, Max builds, Mia reviews. Each one keeps
  its own conversation, memory and brain, and they answer you on Telegram, Discord, Slack or e-mail.
- **Agent teams.** `codo team run "goal"`: a lead splits the work, each member gets its own git copy,
  reviewers check it, you approve the plan and the merge, and `apply --pr` opens a pull request.
- **Agent groups across providers.** `codo group`: Claude, Codex and Gemini side by side, in parallel
  with a synthesis, split work, cross review, voting, a pipeline, or a group chat.
- **Marathon mode.** `codo work "goal" --hours 8 --bg` plans, works in episodes with a fresh context,
  keeps a log, retries network errors and stops at hard budget and time limits.
- **Always-on agents on a server.** `codo host` keeps agents running under systemd or launchd and
  answers on Telegram, Discord, Slack, WhatsApp, Signal and e-mail. Agents write to each other and
  hand tasks over, on your computer and on the server together.
- **MCP both ways.** `codo mcp` exposes Codo tools (browser, team, mail) to Claude Code and Codex.
- **Skills that the agent writes itself**, plus skills from GitHub (`codo skills`).
- **Undo for every edit.** Each file change is backed up; `/undo` reverts it, `/diff` shows it.
- **Phone control.** With the DomaAI app (iOS, Android), `/rc` lets you follow the session and answer
  its questions from your phone. Commands that change things still ask for consent.
- **A single Python file.** No dependencies beyond Python 3.9+, and the installer brings Python along
  when the computer has none.

## See it work

<p align="center">
  <img src="assets/demo/agents-together.webp" width="900" alt="Recording: a group of agents splits a launch between Max, Josh and Mia, each on its own brain">
  <br><sub>Your agents work together: mention one, and the team splits the work across Claude Code, Codex and Gemini.</sub>
</p>

<p align="center">
  <img src="assets/demo/team-ships.webp" width="900" alt="Recording: an agent team gets its plan approved, works in parallel and opens a pull request">
  <br><sub>A team that ships: approve the plan, watch agents build and review in parallel, then open the pull request.</sub>
</p>

## Screenshots

**Windows and Linux** (`codo ui`, the app in its own window)

<table>
  <tr>
    <td width="50%"><img src="assets/screens/win-code.webp" alt="Codo on Windows and Linux: start screen with persistent agents"></td>
    <td width="50%"><img src="assets/screens/win-models.webp" alt="Model picker: Claude Code, Codex and Grok on this computer, backup brain"></td>
  </tr>
  <tr>
    <td align="center">Your agents and one place to start</td>
    <td align="center">Pick a brain, set a backup brain for plan limits</td>
  </tr>
  <tr>
    <td><img src="assets/screens/win-group.webp" alt="New group: ready teams, your agents and six ways of working"></td>
    <td><img src="assets/screens/win-hive.webp" alt="Bots: describe a job in your own words or take a ready one"></td>
  </tr>
  <tr>
    <td align="center">Groups: a ready team or your own pick</td>
    <td align="center">Bots that work on their own and write to you</td>
  </tr>
</table>

**macOS** (native app)

<table>
  <tr>
    <td width="50%"><img src="assets/screens/mac-workflows.webp" alt="Workflows: plan, build, review, every step an agent"></td>
    <td width="50%"><img src="assets/screens/mac-delegate.webp" alt="Hand over work to an agent or a swarm"></td>
  </tr>
  <tr>
    <td align="center">Workflows: every step is an agent</td>
    <td align="center">Hand over work, the result comes back</td>
  </tr>
  <tr>
    <td><img src="assets/screens/mac-models.webp" alt="Model picker on Mac: one agent, team or compare"></td>
    <td><img src="assets/screens/mac-main-dark.webp" alt="Codo for Mac in dark appearance"></td>
  </tr>
  <tr>
    <td align="center">One agent, a team, or compare models</td>
    <td align="center">Light and dark, in 18 languages</td>
  </tr>
</table>

## How Codo compares

| | One coding agent on its own | With Codo |
| --- | --- | --- |
| Plan limit reached | You wait until it resets | The same conversation continues on your next plan, key or local model |
| Models | One provider | Claude Code, Codex, Gemini CLI, 20+ ACP agents, any `/v1` API, local models |
| Several agents at once | Separate terminals, copy and paste between them | Teams in separate git copies, groups with review and voting, rooms and agent mail |
| Long work | Stops when you close the terminal | Marathon mode for hours, always-on agents on a server |
| Where it answers | The terminal | Terminal, app window, phone, Telegram, Discord, Slack, WhatsApp, Signal, e-mail |
| Undo | Depends on the tool | A backup of every edit, `/undo` and `/diff` |
| Cost | Another subscription | Free and open source (Apache 2.0), uses the plans you already have |

### On every system

| | macOS | Windows | Linux |
| --- | :---: | :---: | :---: |
| Terminal agent (`codo`) | ✓ | ✓ | ✓ |
| App window with agents, bots, workflows, groups, Office, settings | native app | `codo ui` | `codo ui` |
| Teams, groups, marathon mode, MCP, skills | ✓ | ✓ | ✓ |
| Always-on agents and messengers (`codo host`) | ✓ | ✓ | ✓ |
| Model picker with backup brain, team runs in the window | ✓ | ✓ | ✓ |
| Compare models side by side, rooms with your agents | ✓ | ✓ | ✓ |
| iMessage, Gmail and Calendar triggers, system notifications | ✓ | | |
| 18 languages, light and dark | ✓ | ✓ | ✓ |

## How it works

```
 you ── codo (terminal, browser window or the Mac app)
          │
          ├─ brain: MaddLabs, DomaAI, your API keys, a local model,
          │         or Claude Code / Codex / Gemini CLI / ACP agents on this computer
          │         (on a plan limit or provider error the turn moves to the next one)
          │
          ├─ tools: read, search, edit files, run commands, browser, web, MCP servers,
          │         skills, sub agents, teams
          │
          └─ safety: trusted folders, read / ask / auto modes, a backup of every edit,
                     hard budget and time limits for long work
```

1. **You start Codo in a folder.** It asks once whether you trust the folder, reads `Codo.md`
   (the project memory) and picks the model you chose with `codo login` or `/model`.
2. **The agent works in a loop.** It plans, reads and searches files (up to 8 of those in parallel),
   edits them and runs commands. Every step is shown live, and edits and commands ask for your
   consent in the default `ask` mode.
3. **Every change can be undone.** Each edit is written atomically with a backup in `.doma/backups`;
   `/diff` shows what changed and `/undo` reverts it.
4. **Context stays small.** Old tool arguments shrink first, huge outputs are clipped in the middle,
   and `/compact` summarizes a long conversation. When a model stops at its output limit Codo
   continues the answer by itself.
5. **It does not get stuck.** Rate limits and server errors are retried with the provider's
   `Retry-After`. When a plan runs out, the same conversation continues on the next brain.
6. **Bigger work scales out.** `codo work` runs for hours in episodes with fresh context and a log,
   `codo team` splits a goal between agents that each work in their own git copy, and `codo host`
   keeps agents running on a server where they answer messages and hand tasks to each other.

## Everything in one place

| Area | What Codo does | Command |
| --- | --- | --- |
| Conversation | Interactive session, one shot task, resume, print mode for scripts with JSON output | `codo`, `codo "task"`, `codo -c`, `codo resume`, `codo -p --json` |
| App window | The full Codo app on Windows and Linux, the same as on Mac: code, model picker with compare, agent teams, groups and rooms, Office, bots and swarms, workflows, delegate, persistent agents and settings, in 18 languages (`--tab` for a browser tab) | `codo ui` |
| Long work | Works alone for hours or days with a plan, log, queue of goals and hard limits | `codo work`, `codo work add`, `codo work status` |
| Teams | A lead splits a goal, members work in separate git copies, reviewers check, you approve the plan and the merge, a pull request at the end | `codo team run`, `codo team apply --pr` |
| Groups of agents | Claude, Codex and Gemini in parallel with a synthesis, split work, cross review, voting, a pipeline or a group chat | `codo group` |
| Always on | Agents under systemd or launchd that answer on Telegram, Discord, Slack, WhatsApp, Signal and e-mail, write to each other and pass on tasks with files | `codo host` |
| Models | OpenAI, Anthropic, xAI, Google, Mistral, DeepSeek, Groq, OpenRouter, Ollama, LM Studio, any `/v1` URL, several accounts at once | `codo login`, `codo accounts`, `/model` |
| Agents you already pay for | Claude Code, Codex, Gemini CLI and ACP agents as brains, with automatic fallback | `codo agents`, `codo login agent` |
| MCP | Use MCP servers in Codo, and expose Codo's browser, team and mail tools to other agents | `codo mcp` |
| Skills | Skills the agent writes for itself, per project or global, and skills from GitHub | `codo skills`, `/skill` |
| Project memory | `Codo.md` read at every start, `/init` writes one | `/init` |
| Your commands | Markdown files become slash commands | `.codo/commands/NAME.md` |
| Phone | Follow the session and answer its questions from the DomaAI app | `codo serve`, `codo pair`, `/rc` |
| Updates | Updates itself once a day in the background (SHA-256 checked), or right now on demand | `codo update`, `codo update --auto off` |
| Maintenance | Diagnosis of connection, account, `PATH` and autostart | `codo doctor`, `codo status` |

### In the interactive session

| Command | What it does |
| --- | --- |
| `/model`, `/effort` | Switch the model or how hard it thinks (low, medium, high, xhigh, max) |
| `/plan` | Plan first, then work |
| `/diff`, `/undo`, `/files` | Show changes, revert the last edit, list touched files |
| `/compact`, `/clear` | Summarize or clear the conversation |
| `/todos`, `/cost`, `/status` | Task list, spending, account and folder |
| `/work`, `/zespol`, `/konta`, `/agenci` | Marathon, team, accounts and agents without leaving the session |
| `/resume`, `/skills`, `/commands`, `/help` | Older conversations, skills, your commands, help |
| `@path` | Attach a file or folder (Tab completes) |
| `!command` | Run a shell command right away |
| **Shift+Tab** | Switch between `read`, `ask` and `auto` |

## Install

**Linux and macOS**

```bash
curl -fsSL https://github.com/DomaAI/Codo/releases/latest/download/install.sh | bash
```

**Windows**

Download [`CodoSetup-x64.exe`](https://github.com/DomaAI/Codo/releases/latest/download/CodoSetup-x64.exe)
and run it. It installs for your user without administrator rights into
`%LOCALAPPDATA%\Programs\Codo`, adds `codo` to `PATH` and has a normal uninstaller. The Start
menu gets **Codo**, the app in its own window, and **Codo Terminal**, the agent in a terminal.
Windows 10 and 11, 64 bit.

Or from PowerShell, without downloading an `.exe`:

```powershell
irm https://github.com/DomaAI/Codo/releases/latest/download/install.ps1 | iex
```

> Windows 11 Smart App Control and some browsers block programs from publishers they do not know
> yet. Code signing for the Windows files is on its way. Until then the PowerShell command above
> works everywhere. After it, `codo ui` opens the Codo window.

The installer downloads `codo` from the latest release, checks its SHA-256 sum against
`SHA256SUMS` and puts it in `~/.local/bin` (Windows: `%LOCALAPPDATA%\Codo\bin`). You can also download
`codo` from [Releases](https://github.com/DomaAI/Codo/releases) and run it with `python3 codo`.

**What the installer adds when it is missing.** It never asks for a password and never needs
administrator rights.

| | Linux and macOS | Windows |
|---|---|---|
| Python 3.9+ (required) | system package manager when you are root or have passwordless sudo (apt, dnf, pacman, zypper, apk) or Homebrew; otherwise a private copy through [uv](https://docs.astral.sh/uv/) in `~/.local/share/codo` | `winget` for the current user; otherwise the signed installer from python.org |
| TLS certificates (required) | `ca-certificates`, or `certifi` | Windows certificate store |
| git, ripgrep (recommended) | installed when a package manager is usable | `winget` |
| `PATH` | the file of your shell (zsh, bash, fish), created if needed | user `PATH`, visible in new windows right away |

Set `CODO_NO_DEPS=1` to install nothing but Codo itself; the installer then only tells you what is
missing. `codo doctor` shows the state of every dependency and the command that adds it.


### Single files, no Python needed

Every release also has ready to run files: `CodoSetup-x64.exe` (installer), `codo-windows-x64.exe`, `codo-linux-x64`, `codo-linux-arm64`, `codo-macos-arm64` (Apple Silicon) and `codo-macos-x64` (Intel). Download one from [Releases](https://github.com/DomaAI/Codo/releases/latest), make it executable on macOS and Linux (`chmod +x`) and run it. The Mac app (Apple Silicon and Intel) is on [domaai.pl/pobierz-codo](https://domaai.pl/pobierz-codo.html).

## Codo for Mac

A native window on top of the same engine, for Apple Silicon and Intel, macOS 15 or newer, signed
and notarized by Apple and updating itself:
[download Codo.dmg](https://bymadd.pl/static/codo/mac/Codo.dmg).

- **Agents with a face.** Create an agent in one sentence, give it a name, a shape and a character,
  and see the whole crew working at once.
- **Rooms.** Shared threads where several agents and you work on one task together.
- **Bots and automations.** Describe a bot in your own words or start from ready ones; they run on
  a schedule, on a webhook or on an e-mail, and report on Telegram, Discord, iMessage or a
  notification.
- **Agent mail.** Agents write to each other and hand over tasks with files, on your Mac and on a
  server together.
- **Terminal, browser and files in the window.** The agent's browser keeps its sign ins, drag and
  drop files into the conversation, preview pages and documents.
- **Office documents.** Presentations, documents, spreadsheets and posters, exported to PPTX,
  DOCX, XLSX and PDF.
- **Gmail, Calendar and Drive**, and more than 40 connections to other services.
- **18 languages**, from English and Polish to Japanese, Korean and Chinese, with the agent
  answering in your language. Light and dark appearance.

## Quick start

```bash
codo login        # choose how Codo talks to a model
cd your-project
codo              # interactive session in this folder
```

On the first start Codo asks you to trust the folder and shows the sign in options:

1. **MaddLabs account**, free credits to start (see below)
2. **Your own API key** or a local model (Ollama, LM Studio)
3. **Agents on this computer**: Claude Code, Codex or Gemini CLI on your existing plan
4. **DomaAI account**, which adds phone control and the DomaAI agent

More ways to run it:

```bash
codo "add a dark theme to the settings page"     # one task and done
cat error.log | codo -p "explain this"          # print mode for scripts, add --json for JSON
codo -c                                          # resume the last conversation in this folder
codo work "migrate the API to v2" --hours 8      # marathon with a time limit
codo work status | codo work log -f | codo work stop
```

## Free credits

Signing in with MaddLabs (`codo login maddlabs`) gives a new account a 14 day trial with
2 million free tokens per day on models hosted in the EU. Terms:
[maddlabs.co/legal/trial](https://maddlabs.co/legal/trial). After the trial you pay per token from a
prepaid balance at [maddlabs.co](https://maddlabs.co), or switch to your own key at any time.

## Connecting models

```bash
codo login openai                  # also: anthropic, xai, google, mistral, deepseek, groq, openrouter
codo login ollama                  # local models, no key
codo login endpoint http://localhost:8000/v1
codo accounts                      # list, add, remove, use
codo agents                        # Claude Code, Codex and Gemini CLI found on this computer
codo model                         # every model you can use right now
```

Models from your own accounts are written as `@account/model`, agents as `agent:claude`,
`agent:codex` and `agent:gemini`.

## Security

Codo edits files and runs commands in the folder you trust. Before the first session in a folder it
asks for consent and shows what is inside (git, number of files, `Codo.md`). Your home directory is
never remembered as trusted.

Three modes, switched with **Shift+Tab**:

| Mode | What the agent may do without asking |
| --- | --- |
| `read` | Read and search files only. Agents run in plan or read only mode. |
| `ask` (default) | Read freely. Edits, shell commands and installs ask for consent. |
| `auto` | Edit and run commands without asking. Agents get workspace write access. |

`--yes` gives consent in advance for one run. Tasks that arrive from the phone run in `ask` mode by default,
and slash commands or `!command` cannot be sent from the phone.

API keys are stored in `~/.config/doma/konta.json` with `0600` permissions. Plain `http` endpoints
are accepted only for localhost and the local network.

Found a security problem? See [SECURITY.md](SECURITY.md).

## Configuration

| Where | What |
| --- | --- |
| `Codo.md` in the project | Project memory, read at the start of every session (`/init` writes one) |
| `.codo/commands/NAME.md` | Your own slash commands for the project (`~/.config/doma/commands/` for all projects) |
| `~/.config/doma/settings.json` | Model, effort, language, trusted folders, marathon limits |
| `~/.config/doma/konta.json` | Connected API accounts |
| `CODO_LANG=en` or `/lang pl` | Interface language (English and Polish). Other codes such as `de`, `fr`, `ja` keep the English interface and make the agent answer in that language |
| `/effort` or `--effort` | How hard the agent thinks: low, medium, high, xhigh, max |

The configuration folder is called `doma` for compatibility with earlier versions.

## Development

Codo is one file, `codo`. Tests run without network access or model providers:

```bash
python3 -m py_compile codo
CODO_LANG=pl CODO_FILE=$PWD/codo python3 -m unittest discover -s tests
```

See [CONTRIBUTING.md](CONTRIBUTING.md). The interface speaks English and Polish (`CODO_LANG`). Some code comments are in Polish;
English translations are welcome as pull requests.

## License

Apache License 2.0, see [LICENSE](LICENSE) and [NOTICE](NOTICE). Codo is made by MADD in Poland.
Claude Code, Codex and Gemini CLI are products of their respective owners and are used through their
own command line tools and your own plans.
