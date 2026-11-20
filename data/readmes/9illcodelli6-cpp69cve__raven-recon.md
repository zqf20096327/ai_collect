# 🦅 RAVEN Recon

**Scope-aware reconnaissance and AI-assisted security-testing workbench** — for bug-bounty
hunters and penetration testers. Runs on **Windows** and **Kali Linux** as a desktop app,
a local web UI, or in the terminal.

[![tests](https://github.com/9illcodelli6-cpp69cve/raven-recon/actions/workflows/tests.yml/badge.svg)](https://github.com/9illcodelli6-cpp69cve/raven-recon/actions/workflows/tests.yml)
[![licence: AGPL-3.0](https://img.shields.io/badge/licence-AGPL--3.0-blue.svg)](LICENSE)
![platforms](https://img.shields.io/badge/platforms-Windows%20%7C%20Kali%20Linux-informational)

> ⚠️ **Authorised testing only.** Use RAVEN Recon only on systems you own or have written
> permission to test. Read [`RESPONSIBLE_USE.md`](RESPONSIBLE_USE.md) first.
> **العربية:** [README.ar.md](README.ar.md)

![RAVEN Recon](docs/screenshots/raven-os.jpg)

| AI Agent — every request and command waits for your approval | Recon Workbench — attack surface, request lab, findings |
|---|---|
| ![AI Agent](docs/screenshots/ai-agent.jpg) | ![Recon Workbench](docs/screenshots/workbench.jpg) |

---

## Contents

1. [What it does](#what-it-does)
2. [Download and install](#download-and-install) — [Windows](#windows) · [Kali / Debian / Ubuntu](#kali--debian--ubuntu) · [Verify your download](#verify-your-download)
3. [Three ways to run it](#three-ways-to-run-it)
4. [Step-by-step guide](#step-by-step-guide)
5. [AI: Claude, your own local model, skills](#ai-claude-your-own-local-model-skills)
6. [Safety model](#safety-model)
7. [Your data and privacy](#your-data-and-privacy)
8. [Build from source and run the tests](#build-from-source-and-run-the-tests)
9. [Troubleshooting](#troubleshooting)
10. [Project layout](#project-layout)
11. [Contributing](#contributing)
12. [Licence and copyright](#licence-and-copyright)

---

## What it does

| Area | What you get |
|---|---|
| **Scope & workspaces** | One workspace per program: in-scope hosts and wildcards, exclusions, ports. Every request RAVEN sends is checked against it; out-of-scope and private addresses are blocked. |
| **Recon** | Certificate-transparency subdomains, HTTP probing of every scoped port, endpoint discovery from links, `robots.txt`, sitemaps and JavaScript, change tracking between runs, priority scoring. |
| **Request lab** | Repeater, Intruder (headers, body, baseline anomaly detection), Decoder, HTTP history. |
| **Labs** | Access-control lab (compare two identities on the same resource) and XSS lab (reflection-context analysis, no script execution). |
| **Findings & evidence** | Candidate findings with evidence links, review workflow, Markdown workspace report export. |
| **AI agent** | Claude Opus 5.5 plans and works through a task with RAVEN's tools — **every request to a target and every command waits for your Approve**. Loads RAVEN's testing playbooks (API recon, API security, recon breadth, code audit, patch diff, PHP LFI, browser testing). |
| **AI chat & terminal** | Ask questions, get payloads and code (`raven-sec` in the terminal). |
| **Safety** | Emergency Stop, per-run budget and rate limits, offline command sandbox on Linux, encrypted API key, local-only data. |

---

## Download and install

### Windows

**Option A — ready-to-run app (recommended):**
1. Download `RAVEN-Recon-windows-x64.zip` from the
   [Releases page](https://github.com/9illcodelli6-cpp69cve/raven-recon/releases/latest).
2. [Verify it](#verify-your-download), unzip it, and run `RAVEN.exe`.
   (Windows 10/11 with the Edge WebView2 runtime, which is built into Windows 11.)

**Option B — from source** (needs [Python 3.11+](https://www.python.org/downloads/) — or
`winget install -e --id Python.Python.3.12` — and [Git](https://git-scm.com/)), in PowerShell:

```powershell
git clone https://github.com/9illcodelli6-cpp69cve/raven-recon.git
cd raven-recon
powershell -ExecutionPolicy Bypass -File .\install.ps1
```

This creates a private Python environment, a **Start Menu entry**, and the commands
`raven-recon`, `raven-recon-web` and `raven-sec` (open a new terminal afterwards).
Uninstall: `.\install.ps1 -Uninstall` (your data is kept).

### Kali / Debian / Ubuntu

**Option A — ready-to-run app:**
```bash
# download RAVEN-Recon-linux-x64.tar.gz and SHA256SUMS.txt from the Releases page, then:
sha256sum -c SHA256SUMS.txt --ignore-missing
tar -xzf RAVEN-Recon-linux-x64.tar.gz
sudo apt install -y gir1.2-webkit2-4.1 bubblewrap   # own window + command sandbox
./RAVEN/RAVEN
```

**Option B — from source (recommended on Kali):**
```bash
git clone https://github.com/9illcodelli6-cpp69cve/raven-recon.git
cd raven-recon
./install.sh
```

The installer asks before running `sudo apt install` for the few system packages it needs
(`python3-venv python3-gi gir1.2-webkit2-4.1 bubblewrap`), creates `.venv`, adds
**RAVEN Recon** to the applications menu and installs the `raven-recon` and `raven-sec`
commands in `~/.local/bin`. Uninstall: `./install.sh --uninstall` (your data is kept).

### Verify your download

Official builds exist **only** on this repository's Releases page. Each release has
`SHA256SUMS.txt` and a GitHub **build-provenance attestation** proving the file was built by
this repository's workflow:

```bash
sha256sum -c SHA256SUMS.txt --ignore-missing
gh attestation verify RAVEN-Recon-linux-x64.tar.gz --repo 9illcodelli6-cpp69cve/raven-recon
```
Windows: `Get-FileHash .\RAVEN-Recon-windows-x64.zip -Algorithm SHA256` and compare with
`SHA256SUMS.txt`. Copies from anywhere else ("PRO", "cracked", re-uploads) are not official
and may be malicious.

---

## Three ways to run it

| | Windows | Kali / Linux |
|---|---|---|
| **Desktop app** (own window) | Start Menu → RAVEN Recon, or `raven-recon` | Menu → RAVEN Recon, or `raven-recon` |
| **Local web UI** (your browser, `127.0.0.1` only) | `raven-recon-web` | `raven-recon --browser` |
| **Terminal assistant** | `raven-sec` | `raven-sec` |

The web UI listens on the loopback interface only and every API call needs a per-session
token, so other machines on your network cannot reach it.

---

## Step-by-step guide

1. **Create a workspace** — RAVEN OS sidebar → **Workspace** (or in the Recon Workbench:
   workspace menu → *new workspace*). Enter the program name and **exactly the scope the
   program allows**: in-scope hosts or wildcards (`*.example.com`), exclusions, and ports.
   Leave *allow private addresses* off unless it is your own lab.
2. **Set your identity** — Workbench → **Identity**: the User-Agent and the researcher header
   your program asks for (for example `X-HackerOne-Research: <your handle>`).
3. **Run a collection** — Workbench → **Run collection**: certificate-transparency names,
   HTTP probes on every scoped port, and endpoint discovery. Watch progress in the terminal
   panel; stop any time.
4. **Review the surface** — **Surface** (hosts ranked by review priority), **Endpoints**,
   **Graph**, **Changes** (what is new since the last run), **Runs**. A score is a review
   priority, never a vulnerability verdict.
5. **Test by hand** — open a request in **Repeater**, fuzz a parameter in **Intruder**
   (with a baseline to spot anomalies), compare two accounts in the **Access-control lab**,
   check a reflection in the **XSS lab**, decode tokens in **Decoder**. Everything is in
   **HTTP history**.
6. **Use the AI agent (optional)** — add your Claude key (see below), open **AI Agent**, pick
   *Claude Opus 5.5*, describe the task (e.g. *"Check /api/orders/{id} for IDOR using my two
   test accounts"*). Read each proposed request or command and **Approve** or **Deny** it.
7. **Record and report** — the agent and the labs create **candidate** findings; review them
   in **Findings**, then **Export workspace report** (Markdown) and write your own report.
8. **Stop button** — **Emergency Stop** halts every job, request, agent run and command at
   once; **Resume** re-enables them.
9. **Appearance** — **Settings → Appearance**: **Full** (animated artwork background),
   **Static** (same artwork, no animation — lighter on older machines) or **Off** (plain dark).
   Systems set to *reduce motion* get Static automatically.

---

## AI: Claude, your own local model, skills

RAVEN works fully without AI. For AI features choose one:

**Claude (recommended, best results).** Create an API key at
[console.anthropic.com](https://console.anthropic.com) (set a monthly spend limit there), then
RAVEN → **Settings → Claude (Anthropic API)** → paste the key → **Save & test**.
- The key is stored **encrypted** in your data folder and never shown again; it is never
  passed to commands RAVEN runs.
- Used by **AI Chat**, the **AI Agent** page and `raven-sec`.
- Each agent run has a **budget** (default $3) and a **turn limit** (default 40) — change them
  in Settings. The estimated cost is shown next to every run.
- You pay Anthropic for your own usage and must follow Anthropic's Usage Policy.

**Your own local model (free, offline).** Install [Ollama](https://ollama.com), pull a model
(for example `ollama pull qwen2.5-coder:7b`), then **Settings → Optional external provider
(Ollama)** → enable it and enter the model name. It powers **AI Chat**; the agent requires
Claude. Details and the advanced built-in RAVEN-Sec model: [`docs/LOCAL_AI.md`](docs/LOCAL_AI.md).

**Skills** — testing playbooks the agent loads when relevant (`raven/skills/`):

| Skill | Use it for |
|---|---|
| `api-recon` | read-only mapping of REST / GraphQL / SOAP / WebSocket APIs |
| `api-security` | BOLA/IDOR, BFLA, mass assignment, JWT, GraphQL & SOAP issues, low-volume logic checks |
| `recon-breadth` | subdomains, takeover indicators, archived URLs, parameters |
| `code-audit` | attacker-first white-box review of source you provide |
| `patch-diff` | understanding a vendor security fix and checking exposure safely |
| `php-lfi-rce` | assessing PHP file inclusion; code-execution proof only where allowed / in labs |
| `browser-testing` | Playwright scripts for DOM XSS, auth flows, SPA crawling |

**Terminal:** `raven-sec` (chat), `raven-sec -q "question"`,
`raven-sec agent "objective" --scope app.example.com` (asks y/N before every action;
`--scope host:port` for other ports, `--allow-private` for your own lab only).

---

## Safety model

- **Scope enforcement** on every outgoing request (canonical URL, IDNA-correct hostnames,
  resolved address pinned, private/loopback blocked unless enabled, no redirects followed).
- **Human approval** for every target request, recon job and command the AI agent proposes;
  approvals are bound to the exact action shown.
- **Offline sandbox** (bubblewrap, Linux) for agent commands: no network, no home directory.
- **Emergency Stop**, per-workspace request budgets and rate limits, per-run AI budget.
- **Local API** on `127.0.0.1` only, per-session token, Origin and Host checks.
- **No offensive extras:** no denial-of-service, malware, persistence, EDR/AV evasion or
  credential stuffing. AI output is advisory — verify before you report.

---

## Your data and privacy

- Data lives on your machine: `~/.local/share/raven-recon` (Linux) or
  `%LOCALAPPDATA%\RAVEN-Recon` (Windows). Override with `RAVEN_DATA_DIR`.
- RAVEN contacts only: the targets you approve, `crt.sh` for certificate transparency,
  allow-listed trusted research sources (OWASP, MITRE, NVD, GitHub advisories) when you or the
  agent search, and Anthropic's API if you enabled Claude.
- No telemetry.

---

## Build from source and run the tests

```bash
python3 -m venv --system-site-packages .venv
.venv/bin/pip install -r requirements-linux.txt -r requirements-dev.txt
.venv/bin/python -m pytest -q          # test suite
./build-linux.sh                       # standalone app → dist/RAVEN/RAVEN
```
Windows: `pip install -r requirements-windows.txt -r requirements-dev.txt`, then `build.bat`
(→ `dist\RAVEN.exe`). The optional Rust policy bridge (`cargo build --release -p raven-bridge
--manifest-path rust/Cargo.toml`) and C++ accelerator (needs `python3-dev`) are built by the
build scripts when the toolchains are present; tests that need them are skipped otherwise.
Release builds are produced by GitHub Actions on every `v*` tag (`.github/workflows/release.yml`).

---

## Troubleshooting

| Problem | Fix |
|---|---|
| Opens in the browser instead of its own window (Linux) | `sudo apt install gir1.2-webkit2-4.1 python3-gi` |
| Agent: "bubblewrap is not installed" | `sudo apt install bubblewrap` (Linux only; on Windows the agent cannot run commands) |
| Claude: key rejected / test failed | Create a new key in the Anthropic console, check billing/spend limit, paste it again |
| Agent run ends with `REFUSED` | Anthropic's safety system declined a step — state the authorised context (program, scope) more clearly, or do that step by hand |
| Everything is blocked | Check the workspace scope and ports, and whether Emergency Stop is engaged |
| The UI feels slow on an old PC or VM | **Settings → Appearance → Static** (or **Off**) |
| `raven-recon` / `raven-sec` not found | Add `~/.local/bin` (Linux) or `%LOCALAPPDATA%\RAVEN-Recon\bin` (Windows) to `PATH`, open a new terminal |

---

## Project layout

```
raven/            application code (API server, recon engine, scope, runtime, AI)
  claude/         Claude integration (key store, client, agent loop, tools, chat)
  skills/         testing playbooks loaded by the agent
  sec_ai/         optional local RAVEN-Sec model, research browser, terminal CLI
web/              RAVEN OS UI (index.html) and Recon Workbench (prototype.html)
tests/            test suite (pytest)
rust/ native/     optional Rust policy bridge and C++ accelerator
packaging/        Linux desktop entry and icons
docs/             guides, architecture notes, screenshots, development history
install.sh        Kali / Debian / Ubuntu installer
install.ps1       Windows installer
```

---

## Contributing

Issues and pull requests are welcome. Security problems in RAVEN itself: please report them
privately — see [`SECURITY.md`](SECURITY.md). Forks are welcome under the AGPL; per the
additional terms in [`NOTICE.md`](NOTICE.md), modified versions must be marked as modified and
must not present themselves as the official RAVEN Recon.

---

## Licence and copyright

**RAVEN Recon — Copyright © 2026 mahmoud.**

Licensed under the **GNU Affero General Public License v3.0 or later**
([`LICENSE`](LICENSE)), with the additional terms in [`NOTICE.md`](NOTICE.md) (keep the
attribution, mark modified versions, no rights to the RAVEN name and logo). If you run a
modified version as a network service, you must offer its source code to its users.

Provided **without any warranty**. You are responsible for using it legally and only with
authorisation — see [`RESPONSIBLE_USE.md`](RESPONSIBLE_USE.md).
