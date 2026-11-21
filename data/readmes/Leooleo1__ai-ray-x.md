# raiox

**Put your AI coding agents to work inside every project, from one local
panel.** Each project gets its own AI, with its context, a name and a role. With
full access it works like your CLI in auto mode: it edits, runs the tests,
commits and pushes, starts your app and checks the screen. You see what every
AI is doing, what waits for you and what they delivered. Local only, open
source.

It runs the CLIs you already use, under your own accounts: **Claude Code,
Codex, Cursor, Google's Antigravity CLI and opencode** (which reaches any
provider, free models included). And it shows where their tokens go, with cuts
that make every request cheaper.

![raiox in 20 seconds: a project's AI fixed a bug and checked the app; / calls the helpers; ⌘K goes to Usage, the X-ray and Workflows](docs/screenshots/demo.webp)

<sub>Screenshots show a demo with made-up projects and usage.</sub>

## Quick start

1. Download the installer for your system from
   [Releases](https://github.com/Leooleo1/ai-ray-x/releases): macOS (Apple
   Silicon) or Windows (x64). The builds are not signed yet, so the first
   time macOS asks you to right-click › Open and Windows to click More info ›
   Run anyway.
2. Have at least one of the CLIs above installed and signed in.
3. Open raiox. The first run asks your name (and, if you like, a photo),
   connects your AIs (it can install and sign in to them for you), finds your
   projects, or makes a new folder, and makes an AI for the ones you pick.
   raiox uploads nothing.

![The first run: an AI at work in every project, in seven short steps](docs/screenshots/onboarding.webp)

![The first step: your name and, if you like, a photo from your computer or your GitHub](docs/screenshots/onboarding-you.webp)

Intel Macs and Linux: [build from source](docs/building.md).

## An AI in every project

**Bots** shows each project's AI as a card: its character, whether it is
working (and on what), waiting for you or resting, and its last words. A bot
that waits can be approved or answered from its card. A project's
conversations run at the same time, and any folder on the computer can become
a project. **New conversation** asks anything of any AI installed, with its
model, outside any project. A conversation also opens the project's files in an
editor, its Git changes and a terminal, beside the chat (on this computer only,
never from the phone).

![A chat with a project's AI that has full access: it fixed a bug test-first, committed and pushed, started the app and checked its screenshot](docs/screenshots/chat.webp)

- **Four modes, as in a coding CLI.** Beside Send, each AI's mode: *allow*
  (it runs what only reads, tests or installs; changes come as proposals),
  *approve for me* (it applies its own proposals), *auto* (it edits, runs
  any command, installs, sets up the `.env`, commits, pulls and pushes, with
  its CLI's own automatic review stopping what is risky) and *full* (no
  review at all). Shift+Tab steps through them; a click lists them. It asks
  you before a force push or a deploy.
- **It sees your app.** It starts the project's dev server through See the
  app (installing what is missing), keeps it running and takes screenshots of
  the pages it changed, or of the iOS simulator.
- **Asking first, when you prefer.** It reads and answers; a change it
  proposes is made in a copy you review, apply and undo. When it needs more,
  its answer carries a card that gives it full access and lets it go on.
- **Your way of talking.** Several conversations per project, open as tabs
  across projects, images in the chat, a correction while it works, Stop, and
  switching a conversation to another AI with its recent messages. Each AI
  shows its own mark beside its model and effort, and `/` in the message
  field calls Ray, Diet and Memo.
- **What each turn did.** A meter in the conversation shows how much context
  every request re-reads and where it compacts. A turn of an AI with full
  access lists the files it changed, with the diff and *Undo this turn*.
  *Branch* starts a new conversation from any answer, and `/btw` asks a side
  question that stays out of the conversation's session. A turn cut short when
  the app closed can be continued where it stopped.

![An AI that asks first: it says what it needs and offers full access in one click](docs/screenshots/access.webp)

## The whole team at a glance

**Desk.** One board in four lanes: to do, doing, waiting for you, done. What
each AI is doing right now, with its last steps, and everything that waits for
you (proposals, drafts, commands, finished tasks). A lane lights up when
something is in it. Hand a task to any AI, or let idle AIs pick tasks up in
your free hours. A task in its *own copy* runs in a copy of the project, so
several AIs work on one project at once; what each changed comes back as a
diff to apply.

![The Desk: tasks for each AI, what they do now and what waits for you](docs/screenshots/desk.webp)

**Deliveries.** What your AIs produced: the last two weeks at a glance, then
each day's changes (with the files), screenshots, routine results and finished
tasks. Each one opens the conversation it came from.

![Deliveries: two weeks of output as pixels, then each day on a rail](docs/screenshots/deliveries.webp)

**Wiki.** Pages every AI reads: the team's rules, how to deploy, the names of
things. A page goes with every question, or only when the subject matches, and
each one shows what reading it cost this week.

![The Wiki: pages split by what they cost, one open to write](docs/screenshots/wiki.webp)

**Workflows.** A trigger (by hand, a time, or a Desk task that finished) and
steps in a line: ask an AI, wait for your approval, post in a channel, each
step able to use the answer before it. Drawn as one line you edit in place;
the step being run lights up.

![Workflows: a morning check that asks one AI, waits for your approval, then asks another](docs/screenshots/workflows.webp)

**And more:** ⌘K to go anywhere, the use of each AI's plan as two rings
beside your profile, routines on a schedule, channels where several AIs talk with a
free router, one question to several projects at once, a reviewer AI that reads
another's proposals, a built-in self-improving agent template, an opt-in
Dev/Infra auditor, and Ray, Diet and Memo, three helpers that answer from your
logs at no cost. From your phone (pairing by QR) or Telegram too.

## Where the tokens go

Three pages under Consumption in the sidebar, their names as the tabs.

**Usage.** What your AIs' use would cost at API prices: per day, per AI, per
model and per project, over 7, 30 or 90 days.

![Usage: the cost at API prices, each AI's share, the cost per day and a breakdown by model](docs/screenshots/usage.webp)

**X-ray.** Tokens read and written, what they would cost paying per use, when
you use your AIs, how much each request re-reads and what gets re-read most,
per project. It reads Claude Code's and Codex's logs, and charts every AI's
use through raiox.

![The X-ray: tokens read and written, when your AIs work, how much each request re-reads, and where it goes](docs/screenshots/xray.webp)

**Efficiency.** Cuts ranked by the saving, applied with a backup and an undo,
and measured afterwards. On the author's machine, 82,000 Claude Code requests
spent **77% of their cost re-reading old context**; raiox's top cut there
(compact at 300K tokens) is estimated to cut that re-reading by **59%**.

![Efficiency: ranked cuts with the estimated saving, and what the current session carries](docs/screenshots/efficiency.webp)

Every feature, in detail: [docs/features.md](docs/features.md).

## What acts on its own

raiox never changes a project, spends your plan or opens to the internet unless
you ask it to or turn it on. One switch is on by default; read the others
before you flip them.

| Switch | What it does | The risk |
|---|---|---|
| **Mode: allow** (per AI, the default) | Runs on its own the commands that only read, test, lint, build or install locked dependencies, and starts the app with a screenshot | Other commands (deleting, `git push`, adding a package, other scripts) still wait for your click |
| **Mode: approve for me** | Also approves that AI's proposals and applies the change to the project | Changes land without you reading them first; each one can still be undone |
| **Mode: auto** | The AI works in the project like its CLI in auto mode: edits files (its `.env` included), runs any command, installs, commits, pulls and pushes, and starts the app | It acts in your project and your git remote without asking; each CLI's own automatic review is what stops a risky step (Cursor's `--force` has none) |
| **Mode: full** | The same with no review at all: Claude Code's bypassPermissions, Codex without approvals or sandbox, Antigravity skipping permissions | Nothing stops a destructive command; only for a project you can redo |
| **Uses your MCP servers** (per AI, Claude Code) | Lets it use your own MCP servers, with no approval step | It can act in your mail, calendar, drive or anything else those servers reach |
| **Workflows on a trigger** (per workflow, off until you turn it on) | Run their steps at a time or when a Desk task finishes | Each run spends your plan; an approval step stops it until you answer |
| **Bots pick tasks up** (Desk) | Idle AIs start their next task by themselves | It spends your plan while you are away; set a daily or weekly token ceiling |
| **Dev/Infra Auditor** (per AI) | Audits project scripts, workflows, routines and skills on demand, on infra change, or weekly | Spends your plan on each audit; fixes always wait in a draft for your approval |
| **Update on its own** (profile menu, off by default) | Installs a new version of the app once no AI is answering, and restarts it | The app restarts without asking; the signature is still checked |
| **Reads the web** (per AI) | Lets it open pages and search | What it reads can try to steer it |
| **Phone access** (Settings › Phone) | Opens the panel to a public address through Cloudflare Tunnel | The temporary link is on the internet; only devices you pair get in, and Remove cuts one off at once |
| **Telegram** (Settings › Phone) | Lets one paired Telegram chat talk to your AIs | Anyone holding that phone can use them; proposals still wait in raiox |

## Privacy

- Local only: the panel listens on `127.0.0.1` with a per-run session token.
  With phone access on, a Cloudflare tunnel reaches it, for paired devices only
  (see [From your phone](docs/features.md#from-your-phone)).
- raiox reads your CLIs' logs and keeps an index in your cache folder; it does
  not upload them. Chats run your own CLI, which talks to its own provider
  under your account.
- Secrets are counted, never stored.
- Secrets files (`.env` and its variants, `.dev.vars`, keys, certificates)
  never enter the copies the AIs edit, and an AI that asks first cannot read
  them (Claude Code is denied; the other CLIs are told not to, and talk in
  their plan or ask modes). An AI with full access works in the project
  itself and may read, create and edit them, to set up a `.env` for instance;
  it is told never to repeat their values.
- Commands raiox runs for an AI that would open secrets files are refused
  before you are asked, variables that look like secrets stay out of their
  environment, and values that look like secrets are hidden in their output.
- The desktop app checks the latest GitHub release for a new version (a request
  with nothing about you), and installs it when you press Update (or on its
  own, if you turned that on), after checking its signature.
- The Codex rings ask Codex's own app server for your plan's use once a minute;
  it reads it from OpenAI under your account, as Codex itself does.

## Status

Early (0.1.12). Developed on macOS; tested on Windows 11 (in a VM, ARM64 and
x64); Linux should work.

## License

MIT, see `LICENSE`. Third-party pieces are listed in `THIRD_PARTY_NOTICES.md`.
