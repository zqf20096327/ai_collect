<div align="center">

<img src="docs/screenshots/hero.webp" alt="SleepPilot trailer: at 23:00 you describe the outcome; overnight the Manager plans, the Developer codes, a failing test is caught and repaired, a Reviewer approves, Claude's quota runs out and Codex takes over; at 07:00 the report shows 4/4 tasks verified" width="100%">

# SleepPilot

### Your AI coding agent works the night shift. You wake up to proof.

A local-first supervisor that runs **Claude Code, Codex, OpenCode — or any CLI agent —**
overnight, and only marks a task done when the checks actually pass.

<a href="https://github.com/akadirsanli/SleepPilot/archive/refs/heads/main.zip"><img src="https://img.shields.io/badge/%E2%AC%87%EF%B8%8F%20Download-SleepPilot%20ZIP-6ee7c8?style=for-the-badge" alt="Download SleepPilot (ZIP)"></a>
<a href="#-quick-start"><img src="https://img.shields.io/badge/%E2%9A%A1%20Quick%20start-60%20seconds-93b4ff?style=for-the-badge" alt="Quick start in 60 seconds"></a>

[![GitHub stars](https://img.shields.io/github/stars/akadirsanli/SleepPilot?style=social)](https://github.com/akadirsanli/SleepPilot/stargazers)
[![tests](https://github.com/akadirsanli/SleepPilot/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/akadirsanli/SleepPilot/actions/workflows/test.yml)
[![license: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)
[![Node.js 20.10+](https://img.shields.io/badge/node-%3E%3D20.10-339933?logo=node.js&logoColor=white)](package.json)
[![core dependencies: 0](https://img.shields.io/badge/core%20dependencies-0-blue)](THIRD_PARTY.md)

[**Quick start**](#-quick-start) · [How a night works](#-what-happens-while-you-sleep) · [📱 Phone remote](#-your-phone-is-the-remote) · [Engines](#-bring-the-agent-you-already-trust) · [📊 Excel & PDF apps](#-excel-word-and-pdf-apps--checked-like-code) · [Reverse & Rust](#-sleep--reverse--rust-it) · [Docs](#-documentation)

</div>

---

Coding agents are brilliant at *sounding* finished. Then you open the repo in the
morning and find a half-applied patch, a crashed session and a chat window that
says “All done! ✅”.

**SleepPilot is the supervisor those agents never had.** It plans the work, hands
one concrete task at a time to the engine you already use — Claude Code, Codex,
OpenCode, any OpenAI-compatible API, a local Ollama model or your own CLI — runs
real checks, gets a read-only second opinion, repairs what failed and keeps going
until the objective is met or the clock runs out.

Then it leaves you a report built from things it actually executed.

> **“The model said it finished” is not verification.**
> A task is marked **verified** only when a check SleepPilot itself ran passed
> after the change.

<table>
<tr>
<td width="33%" valign="top">

### 🧪 Evidence, not vibes
Command checks, syntax, headless-browser HTML smoke tests, `cargo test`, file:line
citations. Model self-reports are recorded as **claims**, never as proof.

</td>
<td width="33%" valign="top">

### 🌙 Built to survive the night
Stall watchdog, crash supervisor, memory guard, durable sessions and quota-aware
fallback. Failures become recovery paths, not a lost night.
**📱 Check in from bed:** scan a QR code and your phone becomes the remote.

</td>
<td width="33%" valign="top">

### 🔌 Zero lock-in, zero build step
Six engine types, per-role routing, local AI via Ollama. No build step and a
dependency-free core — just Node.js. The office tools install themselves once.

</td>
</tr>
</table>

## ⚡ Quick start

**No build step, a dependency-free core.** You only need
[Node.js 20.10 or newer](https://nodejs.org/) (the LTS version is perfect). On the first start the
launcher installs the office libraries (Excel, Word, PDF — about a minute, once); everything else
works without them.

### 🪟 Windows — no terminal needed

1. **Install Node.js** from [nodejs.org](https://nodejs.org/) (just click *Next* through the installer).
2. **[⬇️ Download SleepPilot (ZIP)](https://github.com/akadirsanli/SleepPilot/archive/refs/heads/main.zip)**,
   right-click the file → **Extract All…**
3. Open the extracted folder and **double-click `SleepPilot.cmd`**.
   If Windows asks whether to run it, choose **Run** — it is a short plain-text
   script you can read in Notepad.
4. Your browser opens SleepPilot. 🎉

The first launch also puts a **SleepPilot** shortcut with the moon logo next to
`SleepPilot.cmd`. Want one on your desktop too? Run
`powershell -ExecutionPolicy Bypass -File scripts\create-shortcut.ps1` once.

### 💻 macOS, Linux or terminal fans

```sh
git clone https://github.com/akadirsanli/SleepPilot.git
cd SleepPilot
npm start          # or ./sleeppilot.sh
```

### 🧪 Look around for free

Want to explore before spending a single token? Start in test mode —
`SleepPilot.cmd --test-mode` on Windows or `npm run start:test-mode` anywhere.
It drives simulated engines, is clearly labelled, and keeps its data apart from
your real projects.

## 🌙 What happens while you sleep

```
 23:00  You write the objective ─────────────────────────────────────────┐
          │                                                              │
          ▼                                                              │
   Scout   ─► measures the repo, detects the stack, suggests checks      │
   Manager ─► turns the objective into scoped tasks                      │
   Developer ─► real edits with real tools (parallel when scopes allow)  │  repeat until
   Checks  ─► commands · syntax · HTML smoke · cargo · citations         │  done or
   Reviewer ─► read-only second opinion on the evidence                  │  out of time
   Manager ─► continue · repair · finish ────────────────────────────────┘
          │
 07:00  ▼  Report: changed files, executed checks, verdicts, tokens, open issues
```

Every turn is durable. Every iteration leaves evidence. Every unexpected failure
gets a recovery path.

<p align="center">
  <img src="docs/screenshots/run.png" alt="Live run: a failed check, an automatic repair and a verified result" width="900">
  <br><sub>A real run: the first patch fails an exact-content check, the Developer fixes it, the check passes, the Manager closes the task.</sub>
</p>

## 📱 Your phone is the remote

Leave the PC running and go to bed. **Scan one QR code and your phone controls
SleepPilot** — at home or away, over Wi-Fi or mobile data.

<table>
<tr>
<td width="62%" valign="top"><img src="docs/screenshots/phone-qr.png" alt="Settings → Phone: a QR code to scan with the phone"><br><sub><b>On the PC</b> — Settings → Phone → scan the QR code. Done once; the phone stays signed in.</sub></td>
<td width="38%" valign="top"><img src="docs/screenshots/phone-run.png" alt="A live run on the phone with Pause, Stop and a permission request"><br><sub><b>On the phone</b> — a live run. Allow the request, pause, stop or steer.</sub></td>
</tr>
</table>

From the phone you can:

- ✅ **Answer permission requests and questions** the agent is waiting on
- ⏸️ **Pause, stop or add an hour** to a run
- 🧭 **Steer** — tell the agent to change direction mid-run
- 📋 **Edit tasks**, watch the live conversation and read the morning report
- ▶️ **Start new runs** on any project

**Set up in 3 steps:** install the free [Tailscale](https://tailscale.com) app on
the PC and the phone (same account) → **Settings → Phone → Turn on phone
access** → scan the QR code.

**Private by design.** SleepPilot listens only on your Tailscale address, so only
your own devices can reach it — it is never opened to the Wi-Fi or the internet,
and no port forwarding or cloud account for SleepPilot is needed. The phone gets
its own key, separate from the PC's; "Sign out all phones" revokes it instantly.
API keys, closing the app and phone settings stay on the PC. Off until you turn
it on. Details: [USAGE](docs/USAGE.md#control-sleeppilot-from-your-phone) ·
[SECURITY](SECURITY.md#phone-access-off-by-default).

## 🎯 Who is this for?

- You use **Claude Code, Codex or OpenCode** and want to hand it a job at night
  and find **verified results** in the morning.
- You pay for **several models or harnesses** and want to decide which one plans,
  which one codes and which one reviews — with automatic fallback when one runs
  out of quota.
- You're **tired of agents saying “done”** while the tests are still failing.
- You want to **check on the night shift from your phone** instead of walking
  back to the PC.
- You want all of this **local-first**: your machine, your keys, your repo.

## 🆚 Why not just run Claude Code or Codex directly?

| | A coding agent on its own | **SleepPilot + that same agent** |
|---|---|---|
| Unattended overnight | You babysit it | Designed for it: Sleep presets, stall watchdog, permission timeouts |
| What “done” means | The model says so | A check SleepPilot ran **passed after the change** |
| Second opinion | — | Read-only Reviewer sees the evidence |
| Crash / frozen turn | Night is over | Watchdog + supervisor restart and reconcile |
| Quota exhausted | Run stops | Next route in the fallback chain continues the **same task** |
| Big refactors | One long context | File-scoped tasks, parallel developers on non-overlapping scopes |
| Choice of model | One vendor | Different engine, model and effort per role |
| Agent needs approval at 3 a.m. | Walk to the PC or lose the night | Answer it from your phone |
| Morning | Scroll the chat | A measured report: files, checks, verdicts, tokens |

SleepPilot doesn't replace your agent — it **supervises** it. Keep the tool you
like; add the plan, the checks, the reviewer and the recovery around it.

## 🔌 Bring the agent you already trust

| Engine | How SleepPilot drives it | Credentials |
|---|---|---|
| **Claude Code** | Installed `claude` CLI, stream-json, sessions | Reuses `claude auth login` |
| **Codex CLI** | `codex exec --json` + resume | Reuses `codex login` |
| **OpenCode 2.x** | Private loopback `opencode serve` | Reuses your OpenCode sign-in |
| **API harness** | OpenAI-compatible or Anthropic HTTP APIs — DeepSeek, OpenAI, OpenRouter, Groq, Mistral, xAI, LM Studio, vLLM | Your key, stored locally |
| **DeepSeek Harness** | Local `dsh --profile headless` | DSH's own credentials |
| **Command harness** | Any command that accepts a prompt | Whatever it needs |

**Fully local works too:** Settings → Local AI detects Ollama, lists your models
and creates a provider in one click. No cloud key required.

### Route each role to the best engine

Pin a different harness, model and reasoning effort to the **Manager**,
**Developer** and **Reviewer** — and let SleepPilot fall back automatically when a
route runs out of quota.

```js
rolePins: {
  manager:   { harness: 'claude', modelProfile: 'careful' },
  developer: { harness: 'dsh',    modelProfile: 'fast' },
  reviewer:  { harness: 'api',    modelProfile: 'deep-review' }
},
harnessRouting: {
  enabled: true,
  fallbackChain: ['claude', 'dsh', 'api', 'opencode']
}
```

<details>
<summary><b>Routing details: real effort levels, read-only enforcement, loud failures</b></summary>

- **Real effort, not a label.** API profiles support `off`, `none`, `minimal`,
  `low`, `medium`, `high`, `xhigh`, `max` and `ultra`; Claude Code uses its actual
  `--effort` values; Codex uses `model_reasoning_effort`.
- **Read-only review at the adapter level.** Manager, Reviewer, closing and
  preflight sessions are restricted to harnesses that can actually enforce it.
- **Quota-aware fallback.** Claude's 5-hour exhaustion is detected from its
  stream/result output. The failed turn is recorded, the next usable route is
  selected, and the same task continues.
- **Loud failures.** Unsupported effort or a harness that cannot enforce
  read-only is rejected with the supported values in the error — never silently
  downgraded.

Full schema and fallback semantics: **[docs/ROUTING.md](docs/ROUTING.md)**.

</details>

## 📲 From idea to APK — with a live preview

Pick a template (web app, native Kotlin app, HTML app in an Android shell, libGDX 3D game) and
give it a name: SleepPilot creates the project in your **workspace** folder, and the agent starts
working.

- **Watch it being built.** The Preview screen shows the web app in a phone, tablet or desktop
  frame and reloads on every saved file. JavaScript errors land in a console panel.
- **Every task must build.** For Android projects the real Gradle build runs after each task; no
  APK, no "verified".
- **Install it in the morning.** Build debug/release APKs or a Play Store bundle, sign them with a
  key SleepPilot keeps for you, install and start the app on a USB phone, or download the APK
  straight to your phone.

No Android setup puzzle: Android Studio's JDK and SDK are found automatically, and every missing
piece comes with the exact fix. After each build the app can also be started on a phone or a headless
emulator, so a crash fails the task. Details: **[docs/ANDROID.md](docs/ANDROID.md)**.

## 📊 Excel, Word and PDF apps — checked like code

Building an app that reads Excel sheets, analyses them and writes a report? A coding agent cannot
see inside an `.xlsx` or a PDF, so it guesses — and "the report looks fine" is a claim. SleepPilot
gives the agent and the checks real eyes:

- **The agent looks at real files.** Inspect any Excel, CSV (legacy code pages and `;` included),
  Word, PowerPoint, PDF or PNG: sheets, column types and statistics, first rows, PDF text, scanned
  pages. The developer is told the commands; Claude Code and Codex also get them as MCP tools.
- **Outputs are verified, not trusted.** The office check opens every file a task produced and
  fails on `#REF!`, `NaN`, `[object Object]`, empty documents — plus your expectations: sheets,
  columns, cell values, page counts, headings, "same as the reference file".
- **Test data without real data.** Synthetic sales, expense claims and invoices with
  **planted anomalies** (duplicates, sales outside opening hours, refunds split below an approval threshold, self-approval,
  wrong classification …) and an answer key: the check measures how many your app found.
- **Reports in one call.** Excel with formats, totals and charts; Word, PDF and PowerPoint from
  Markdown with tables, callouts, charts and full Unicode text.

```sh
sleeppilot office sample sales --out data/sales.xlsx --rows 5000
sleeppilot office inspect data/sales.xlsx
sleeppilot office create out/report.pdf --markdown report.md
sleeppilot office verify expectations.json
```

Details: **[docs/OFFICE.md](docs/OFFICE.md)**.

## 🧠 Help when it gets stuck

- **Assistant (💬).** A chat in the corner that knows the state of the app, the project and the run:
  it shows what needs attention at once and answers questions with the model you choose — with two
  fallbacks if that model is not available.
- **Second opinion.** When a task fails the same way twice, loops or stalls, a different engine
  diagnoses it and tells the developer what to do differently — or splits the task.
- **Eyes for the reviewer.** The reviewer can ask for screenshots of the pages it needs to see.
- **MCP tools.** Give Claude Code, Codex and OpenCode a browser, docs lookup or any MCP server.

## 🦀 Sleep & Reverse & Rust It

Point SleepPilot at a program you are authorized to inspect. Overnight it builds a
read-only mirror, performs binary and text reconnaissance (PE / ELF / Mach-O /
ZIP), writes a **cited technical dossier**, turns it into an implementation-ready
**spec with test vectors**, and rebuilds the behaviour as a **Rust application** —
with `cargo check` and `cargo test` as the evidence.

The target is never modified: it is SHA-1 hashed before and after to prove it.

<p align="center">
  <img src="docs/screenshots/reverse-rust.png" alt="Sleep & Reverse & Rust It workspace" width="900">
</p>

## 📸 Tour

<table>
<tr>
<td width="50%"><img src="docs/screenshots/home.png" alt="Home: engines and projects"><br><sub><b>Home</b> — every engine, every project, one place.</sub></td>
<td width="50%"><img src="docs/screenshots/project.png" alt="Project: scope report and Scout"><br><sub><b>Scope report</b> — realistic time, iterations and parallelism before you start.</sub></td>
</tr>
<tr>
<td width="50%"><img src="docs/screenshots/toolchain.png" alt="Scout and toolchain detection"><br><sub><b>Scout</b> — detects the stack, required tools and checks from your files.</sub></td>
<td width="50%"><img src="docs/screenshots/local-ai.png" alt="Local AI with Ollama"><br><sub><b>Local AI</b> — Ollama models as a provider in one click.</sub></td>
</tr>
</table>

## 🚀 Your first real run

1. **Connect an engine** — Settings → Engines: Claude Code, Codex, OpenCode, an
   API key, DSH, or Local AI with Ollama.
2. **Create a project** — Home → New project, pick the folder.
3. **Read the scope report** — SleepPilot suggests a realistic time limit,
   iteration count and parallelism; Scout proposes checks.
4. **Write the objective** — say what “done” looks like. Pick a preset:
   *Overnight*, *Supervised*, *Strict* or *Unrestricted*.
5. **Start the run and go to sleep.**
6. **Read the report** — changed files, executed checks, reviewer verdicts,
   decisions, token usage and open issues. Measured, not guessed.

All run data lives under `%LOCALAPPDATA%\SleepPilot` (Windows) or
`~/.local/share/SleepPilot` — never in your project folder. Nothing is committed
or pushed automatically.

## 🤖 Headless: plug it into CI, cron or other agents

```sh
# Run a project autonomously for 8 hours
sleeppilot run --project ./app --objective "Add CSV export" --hours 8 --preset sleep

# One prompt through any engine, NDJSON out
sleeppilot ask --project ./app --engine api --model deepseek/deepseek-chat \
  --prompt "Fix the failing test" --json

# Dry-run the routing decision
sleeppilot route --project ./app --task coding --dry-run --json

# What can this machine do?
sleeppilot doctor --json
```

`npm link` installs the `sleeppilot` command (or use `node src/main.mjs …`).
Exit codes are stable: `0` completed · `2` paused · `3` stopped · `4` failed.

## 🧪 Verification, not vibes

| Evidence | How it is checked |
|---|---|
| Command checks | Exit code of a command you approved |
| JavaScript / Python syntax | Interpreter parse, no execution |
| HTML smoke | Headless Edge: load, console errors, failed resources |
| Documents | Required files exist and contain real content |
| Office files | Excel/Word/PDF/PNG open cleanly, no `#REF!`/`NaN`; sheets, cells, pages, headings, anomalies found |
| Rust | `cargo check`, `cargo test`, optional clippy/fmt |
| Citations | Every `file:line` claim points at a real line |
| Target integrity | SHA-1 of every reverse-engineering target before/after |

Reviewer verdicts and model “done” messages are recorded, but they are **never
enough** to mark a task verified.

<details>
<summary><b>🛡️ Safety and privacy by default</b></summary>

SleepPilot drives an agent with real file and shell access. Treat it like a
powerful automation tool, not a sandbox.

- The UI binds to `127.0.0.1` only, with a per-launch token cookie, Host
  validation and CSRF protection.
- API keys live in a local credential store — never in the project or browser.
- Claude Code, Codex and OpenCode reuse their own logins; SleepPilot never copies
  their credentials.
- Manager and Reviewer run read-only where the harness can enforce it.
- Protected paths and per-task edit scopes limit what a developer may touch.
- Optional pre-run backups; every persisted string passes through a redactor.
- Nothing is committed or pushed without an explicit click.

Read [SECURITY.md](SECURITY.md) before running an unrestricted profile.

</details>

<details>
<summary><b>🌙 How Sleep mode stays honest when nobody is watching</b></summary>

- A **stall watchdog** interrupts turns with no sign of life.
- A **supervisor** and a **memory guard** restart the app after a crash or before
  V8 runs out of memory.
- Sessions are durable; after a restart SleepPilot reconciles an in-flight turn
  from the engine's records instead of submitting it twice.
- Unanswered permissions and questions are closed after a timeout.
- Quota and provider errors become a controlled pause or a harness switch, not a
  silent failure.

</details>

<details>
<summary><b>🏗️ Under the hood</b></summary>

```
UI (vanilla JS, loopback)          CLI / agents / CI
        │                                  │
        └──────────────┬───────────────────┘
                       ▼
              SleepPilotApp + RunController
        plan → developer → checks → reviewer → manager
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
   EngineManager              project / checks / store
   ├─ OpenCode                 ├─ snapshots + diffs
   ├─ Claude Code              ├─ command / syntax / HTML / cargo checks
   ├─ Codex                    ├─ scope analysis + analytics
   ├─ API harness              ├─ reverse mirror + recon
   ├─ DeepSeek Harness         ├─ reports, backups, JSONL history
   └─ Command harness          └─ GitHub status / commit / push
```

The `RunController` is engine-agnostic: it submits turns, reconciles durable
results, evaluates executed checks, applies manager decisions and survives
restarts. Details: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

</details>

<details>
<summary><b>⚖️ Honest limits</b></summary>

- Harnesses that cannot enforce read-only sessions (DSH, Command harness) are
  rejected for Manager/Reviewer roles rather than "protected" by a prompt.
- A harness without a real effort flag rejects effort requests.
- Model calls cost whatever your provider charges. SleepPilot reports usage; it
  cannot make a paid provider free.
- Autonomous modes change files and run commands. Use scoped permissions,
  protected paths, backups and version control.
- Reverse & Rust is for targets you are authorized to inspect. You are
  responsible for the target and for how you use the results.

More in [docs/LIMITATIONS.md](docs/LIMITATIONS.md).

</details>

## 📚 Documentation

| Document | What is inside |
|---|---|
| [USAGE](docs/USAGE.md) | Install, first run, presets, steering, phone remote, recovery, CLI |
| [ANDROID](docs/ANDROID.md) | Workspace, project templates, live preview, APK builds, signing, devices |
| [ENGINES](docs/ENGINES.md) | Engine contract, providers, Claude/Codex/DSH setup |
| [ROUTING](docs/ROUTING.md) | Role pins, model profiles, effort, quota fallback |
| [OFFICE](docs/OFFICE.md) | Excel, CSV, Word, PowerPoint, PDF, PNG: inspect, create, verify, synthetic test data, MCP |
| [REVERSE](docs/REVERSE.md) | Reverse & Rust: recon, evidence, Rust rules |
| [ARCHITECTURE](docs/ARCHITECTURE.md) | State machine, persistence, security design |
| [TESTING](docs/TESTING.md) | Unit, integration, fake engines and real tests |
| [SECURITY](SECURITY.md) · [CONTRIBUTING](CONTRIBUTING.md) · [THIRD_PARTY](THIRD_PARTY.md) | Policies and credits |

## 🛠️ Development

```sh
npm test
node src/main.mjs --test-mode --no-open --no-supervisor
```

CI runs the full suite on **Node.js 20, 22 and 24 on Windows**, plus Rust
recon/check tests on Ubuntu. Fake OpenCode, API, DSH, Claude Code and Codex
servers mean the suite needs no account and spends no usage.

## 🤝 Contributing

Issues and pull requests are welcome — start with [CONTRIBUTING.md](CONTRIBUTING.md),
run the suite, keep changes small and testable.

---

<div align="center">

### ⭐ If SleepPilot saves you a night, a star helps the next person find it.

SleepPilot is an independent project, **not affiliated with, endorsed by, or
sponsored by** Anthropic, OpenAI, OpenCode, DeepSeek, Microsoft or any other
vendor whose CLI or API it can drive.

[MIT](LICENSE) © akadirsanli

</div>
