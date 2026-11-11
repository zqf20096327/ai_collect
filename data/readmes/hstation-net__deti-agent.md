<p align="center">
  <img src="assets/readme/en/hero.jpg" alt="Deti — the AI coordinator that works inside your team's chat groups" width="100%">
</p>

<h1 align="center">Deti</h1>

<p align="center">
  <b>The AI coordinator that works inside your team's chat groups.</b><br>
  People ask in plain language. Deti opens a task, puts coding agents to work on your own machine,<br>
  and reports back when the result has been checked.
</p>

<p align="center">
  <b>English</b> · <a href="README.vi.md">Tiếng Việt</a>
</p>

<p align="center">
  <img alt="Licence: Apache-2.0 with Commons Clause (no resale)" src="https://img.shields.io/badge/licence-Apache--2.0%20%2B%20Commons%20Clause-a14629">
  <img alt="Node.js 22 or newer" src="https://img.shields.io/badge/node-%E2%89%A5%2022-354334">
  <img alt="Languages: English and Vietnamese" src="https://img.shields.io/badge/languages-en%20%C2%B7%20vi-9b702f">
  <img alt="Status: pre-release" src="https://img.shields.io/badge/status-pre--release-6b5b4e">
</p>

<p align="center">
  If Deti saves your team time, <a href="https://github.com/hstation-net/deti-agent/stargazers"><b>give it a star</b></a> and <a href="https://github.com/hstation-net/deti-agent/fork"><b>fork it</b></a> to make it your own.<br>
  Questions or ideas? <a href="https://zalo.me/g/1w5ngqlvkr11erpzkyrd"><b>Join the community on Zalo</b></a>.
</p>

<p align="center">
  <a href="https://github.com/hstation-net/deti-agent/stargazers"><img alt="Star Deti on GitHub" src="https://img.shields.io/github/stars/hstation-net/deti-agent?style=social"></a>
  &nbsp;
  <a href="https://github.com/hstation-net/deti-agent/fork"><img alt="Fork Deti on GitHub" src="https://img.shields.io/github/forks/hstation-net/deti-agent?style=social"></a>
  &nbsp;
  <a href="https://zalo.me/g/1w5ngqlvkr11erpzkyrd"><img alt="Join the Deti community on Zalo" src="https://img.shields.io/badge/Zalo-Join%20the%20community-blue?style=social"></a>
</p>

> [!IMPORTANT]
> **Status: pre-release.** Deti runs in production for its authors and is being generalised for other organisations. Expect breaking changes before 1.0. Read [Limitations](#limitations) before you rely on it.

## Contents

- [What Deti does](#what-deti-does)
- [How it works](#how-it-works)
- [The life of a request](#the-life-of-a-request)
- [A tour of the admin page](#a-tour-of-the-admin-page)
- [Quick start](#quick-start)
- [Configuration](#configuration)
- [Working with Deti in a group](#working-with-deti-in-a-group)
- [Languages](#languages)
- [Security model](#security-model)
- [Project layout](#project-layout) · [Scripts](#scripts)
- [Troubleshooting](#troubleshooting)
- [Limitations](#limitations) · [Roadmap](#roadmap)
- [Star, fork, take part](#star-fork-take-part) · [Star history](#star-history) · [Contributing](#contributing) · [Licence](#licence)

## What Deti does

Most teams already agree on work in a chat group: a customer posts a screenshot, a manager says "fix this before Friday", someone answers "ok". Deti joins that group as a member and turns the conversation into finished, verified work.

| | |
|---|---|
| **Listens, then waits for you to finish** | Deti answers only when it is called. When someone sends several messages or images in a row, it waits for the burst to end before the agent reads it, so nothing sent a few seconds later is missed. |
| **One lane per project** | Every project has its own long-lived agent session, called a lane, plus a general lane for everything else. Context from one customer never leaks into another. |
| **A task for every request** | The request text and its attachments are saved as a brief. A lead agent plans the work and hires helpers: Coder, Reviewer, Researcher, Content and Visual. |
| **A gate on every tool call** | Read-only until a task is open. Edits only inside the project folder. Commits, deploys and production servers wait for a named approver's own words in the chat. Secrets, SSH keys and Deti's own code cannot be read by the agent. |
| **Verified before it is closed** | A task cannot be closed until a check has passed on the latest change and every document that was edited has been read again. |
| **Replies like a colleague** | Progress and results go back to the group in plain language, with a different tone for customer groups and internal groups. Unfinished work still gets an answer outside working hours. |
| **Remembers every message** | All chat messages are stored in PostgreSQL and can be searched by time, sender and keyword. "Review what the customer asked for in the last three days" does not require anyone to resend anything. |
| **Several brains, with fail-over** | Claude Code, Codex and z.ai can all drive a lane. When one runs out of quota the same request continues on the next one from a checkpoint. |
| **An admin page for the whole operation** | Projects, customers, support packages, requests, the work list, the dispatch map, brain health, schedules and logs, in English and Vietnamese. |

## How it works

<p align="center">
  <img src="assets/readme/en/architecture.svg" alt="Architecture: people in chat groups send messages to Deti; the orchestrator, gates and agent tools sit between the chat and the brains; brains work in your project folders; PostgreSQL and the admin page sit underneath" width="100%">
</p>

1. **Chat.** A message arrives from a group that Deti has been switched on for. Every message is stored, whether or not Deti was called.
2. **Orchestrator.** Deti decides which lane the message belongs to, waits for the sender to finish, and hands the request with its context to that lane's brain.
3. **Brain.** A coding agent (Claude Code, Codex or z.ai) reads the project, plans, and calls tools. It can hire helpers that work in parallel.
4. **Gates.** Every tool call is checked against the task's phase, the project's folder, the list of secrets and production hosts, and who has approved what. A call is allowed, denied with a reason, or held until a person agrees.
5. **Agent tools.** The brain talks to people through Deti's own tools: reply in the group, open a task, report progress, ask for approval, request a deploy, set a reminder.
6. **Result.** The work happens in git repositories on the same machine. The outcome is verified and reported in the group. The admin page shows all of it live.

Everything runs on a machine you control. There is no hosted service: your code, your chat history and your credentials stay where they are.

## The life of a request

<p align="center">
  <img src="assets/readme/en/lifecycle.svg" alt="Six phases: ask, review, confirm, do, approve, deploy. The first three are read-only, the fourth may edit inside the project folder, the last two need an approver" width="100%">
</p>

A short example from a customer group (names are fictional):

> **Linh (customer):** Deti, the order page shows the wrong shipping fee for Da Nang. *(two screenshots)*<br>
> **Deti:** Got it, Linh. I am looking at how the fee is calculated and will come back with a plan.<br>
> **Deti:** The fee table still has last year's zone for Da Nang. Plan: update the zone table and add a test for the three central provinces. About 30 minutes. Shall I go ahead?<br>
> **Khoa (manager):** Go ahead.<br>
> **Deti:** Done. The fee for Da Nang is now 25,000 đ, the tests pass, and I attached a before / after screenshot. It is waiting for approval to go live.<br>
> **Khoa (manager):** OK, deploy tonight.<br>
> **Deti:** Scheduled for 22:00. I will confirm here when the live site has been checked.

What happened behind those messages:

- "Go ahead" came from someone allowed to confirm the plan, so the task moved from *Confirm* to *Do* and the gate opened for edits inside that project's folder only.
- The Coder made the change and the Reviewer read it. Deti refused to close the task until the test run passed on the final version.
- "OK, deploy tonight" is an approval in the approver's own words. Deti does not guess approvals from keywords; the brain reads the context, quotes the sentence as evidence, and only then is the deploy gate opened.

## A tour of the admin page

The admin page runs on `http://localhost:7979` and accepts requests from the local machine only. The screenshots below use demo data.

| | |
|---|---|
| <img src="assets/readme/en/overview.png" alt="Overview screen"><br>**Overview.** What needs a person right now, what each lane is doing, and what Deti has just said in each group. | <img src="assets/readme/en/work.png" alt="Work list screen"><br>**Work.** Every task, filtered by group, project or customer, with its phase, who asked and how it ended. |
| <img src="assets/readme/en/flow.png" alt="Dispatch map screen"><br>**Dispatch map.** Groups, lanes and helpers on one board, with work moving between them live. | <img src="assets/readme/en/requests.png" alt="Requests screen"><br>**Requests.** Each customer request from first message to closure, linked to its task. |
| <img src="assets/readme/en/customers.png" alt="Customer screen"><br>**Customers.** Contacts, the chat groups they are in, and the support package of each project. | <img src="assets/readme/en/package.png" alt="Support package screen"><br>**Support packages.** What a customer is entitled to, stage by stage, and how Deti handles a request inside or outside it. |
| <img src="assets/readme/en/projects.png" alt="Project screen"><br>**Projects.** Owner, approvers, deploy command, production host and the instructions the agent follows. | <img src="assets/readme/en/schedules.png" alt="Schedules screen"><br>**Schedules.** Reminders and recurring jobs the agent will run on time. |

There are also screens for the brains (which engine drives which lane, quotas, fail-over order), chat groups and members, a live log, and settings.

## Quick start

### Requirements

- **Node.js 22** or newer
- **PostgreSQL**
- **[Claude Code](https://claude.com/claude-code)** installed and signed in on the machine (`claude` in a terminal). The Codex CLI and a z.ai key are optional additional brains.
- **A chat account for the agent.** Today the only transport is Zalo. Use a dedicated account, not your personal one.
- **Windows 10 / 11.** Linux support is in progress; see [Limitations](#limitations).

> [!CAUTION]
> Deti connects to Zalo through an unofficial client. Zalo can lock an account that uses one. Use a dedicated account for the agent, never your personal one. Details are in [Limitations](#limitations).

### Install

```bash
git clone https://github.com/hstation-net/deti-agent.git
cd deti-agent
npm install

cp .env.example .env                           # set DATABASE_URL
cp deti.config.example.json deti.config.json   # set "workspace"
npm run db:deploy                              # create the tables

cd admin && npm install && npm run build && cd ..   # build the admin page
npm start                                      # run Deti under its supervisor
```

### First run

1. Open `http://localhost:7979`.
2. On the **Zalo** screen, scan the QR code with the agent's chat account.
3. On the **Projects** screen, add your first project and point it at its folder.
4. Back on the **Zalo** screen, switch on the groups Deti should listen to, link each one to a project, and set who is a super admin and who manages each project.
5. In one of those groups, write `Deti, what can you do?`

### Try it without a chat account

> [!TIP]
> The built-in simulator replaces the chat transport with a local HTTP endpoint. It uses `DATABASE_URL_QA`, never your real database.

```bash
DETI_ZALO=fake npm run dev
```

### Start with Windows

```powershell
pwsh -ExecutionPolicy Bypass -File scripts\autostart.ps1          # register
pwsh -ExecutionPolicy Bypass -File scripts\autostart.ps1 -Remove  # remove
```

## Configuration

`deti.config.json` holds the non-secret settings of this installation. It is not committed. Start from [deti.config.example.json](deti.config.example.json).

| Key | Meaning |
|---|---|
| `name`, `aliases` | What people call the agent in chat |
| `language` | Language of the agent's texts: `vi` (default) or `en`. `DETI_LANG` overrides it. The admin page has its own switch |
| `workspace` | Default working folder for the agent. Default: a `workspace` folder next to this repository |
| `docsDir` | Sub-folder of a project that holds plans and reports. Default `docs` |
| `projectsRoot` | Folder whose sub-folders can be registered as projects. Default: the parent of this repository |
| `extraProjectRoots` | Other folders allowed as projects |
| `productionHosts` | Hostnames or IP addresses treated as production for every project. Commands that write to them need approval |
| `linkBase` | Base URL for relative links in outgoing messages |
| `agents` | Other bots in your groups that Deti must not chat with |
| `stickerSets` | Zalo sticker sets the agent may use |

Secrets and connection strings go in `.env`; every variable is described in [.env.example](.env.example). The ones you are most likely to set:

| Variable | Meaning |
|---|---|
| `DATABASE_URL` | PostgreSQL connection string (required) |
| `DATABASE_URL_QA` | Separate database used by the simulator and the tests |
| `DETI_WEB_PORT` | Port of the admin page. Default `7979` |
| `DETI_LANG` | Overrides `language` from the config file |
| `DETI_CODEX_BIN` | Path to the Codex CLI, if it is not on `PATH` |
| `ZAI_API_KEY` | Enables z.ai as an additional brain |

Everything that belongs to one project (its folder, its instructions for the agent, its production hosts, its deploy rules, its customers and packages) is set on the admin page and stored in the database, not in files. To pre-create projects on a fresh database, copy `config/seed.example.json` to `deti.seed.json`.

## Working with Deti in a group

**Calling it.** Deti answers when you mention its account with `@`, when your message starts with its name or one of its aliases, or when you reply to one of its messages. A name in the middle of a sentence does not count. Everything else in the group is stored but not answered, unless you switch on auto-reply for that group.

**Who can do what.** Roles are set on the admin page. Project roles are stored per project and apply in every group of that project.

| Role | What it means |
|---|---|
| Super admin | May approve anything. Work a super admin assigns skips the plan and approval steps; changes to production, anything that can lose data, and changes to git history are still asked about. A super admin can also be allowed to message Deti privately. |
| Project manager | May approve work and deploys for that project |
| Member | The default in an internal group. May ask for work, cannot approve |
| Customer | The default in a customer group. May ask for work, which is checked against the customer's support package. Deti never discusses internal matters in a customer group |
| View only | Gets answers to questions, cannot assign changes |

**Short commands.** A message of a few words is handled at once, even while the agent is busy: `status`, `stop`, `continue`, `cancel task`, `show plan`, `show report`, `help`. These are recognised from Vietnamese phrases today, plus the English words `status`, `stop`, `continue` and `help`.

**Approvals.** There is no magic keyword. Write what you mean ("ok, go ahead", "deploy tonight", "not yet, change the colour first"). The agent reads it in context and has to quote your sentence as evidence before a gate opens.

**Schedules.** Ask in the group ("remind us every Monday at 9 to review open requests") or use the Schedules screen.

## Languages

Every text that a person or a brain reads lives in a language file, not in code.

| Where | What |
|---|---|
| `locales/<lang>/<namespace>.json` | Messages of the agent: replies, gate reasons, tool descriptions, reports |
| `locales/<lang>/prompts/*.md` | The instruction texts given to the brains |
| `admin/src/locales/<lang>/<namespace>.json` | Texts of the admin page |

Vietnamese (`vi`) is the reference language and English (`en`) is complete for these three sets. To add a language, copy the `vi` folders to a new language code, translate, and run:

```bash
npm run check:locales   # same keys and placeholders in every language, every key used in code exists
npm run check:strings   # no user-facing text left in code
```

Then set `"language"` in `deti.config.json`. Three things are still Vietnamese only; see [Limitations](#limitations).

## Security model

> [!WARNING]
> Deti runs coding agents that execute commands on the host with the permissions of the user running it. The gates in `src/policy/gates.ts` inspect each tool call, but they are a guard rail, not a sandbox: they cannot see inside a script the agent writes and then runs.

- Run Deti on a machine and account you would give to a junior engineer, and keep backups.
- Only switch on groups whose members you trust. Anyone who can give Deti a task can cause commands to run.
- The admin page has no login and only accepts requests from the local machine. Do not expose the port or put it behind a reverse proxy.
- Secrets live in `.env` and `data/` (chat session, state, logs). Both are git-ignored and unreadable by the agent.

Read [SECURITY.md](SECURITY.md) for the full trust model and how to report a vulnerability.

## Project layout

```
src/
  main.ts            entry point (started by scripts/supervise.mjs)
  config/            settings loader, limits, admins
  orchestrator/      message routing, lanes, store, schedules, notebook
  tools/             the agent's own tools (deti_*), grouped by what they act on
  policy/            gates, roles, approvals, verification, channel and content rules
  brain/             Claude / Codex / z.ai sessions, team coordination, fail-over
  channels/zalo/     chat transport, message store, formatting
  crm/  support/     projects, customers, packages, requests, task history
  web/               admin API and server
  i18n/              language loader
  platform/          logging and process helpers
locales/<lang>/      every text shown to people or sent to the brain (vi, en)
admin/               admin page (React + Vite); its texts are in admin/src/locales/<lang>/
prisma/              database schema and migrations
tests/               unit and end-to-end tests
scripts/             supervisor, CLI helpers and the check scripts
assets/readme/       images of this page; diagrams are generated by scripts/make-readme-diagrams.mjs
vendor/zca-js/       bundled Zalo client (see Limitations)
```

## Scripts

| Command | What it does |
|---|---|
| `npm start` | Run under the supervisor, which restarts Deti if it exits |
| `npm run dev` | Run once, without the supervisor |
| `npm test` | Unit tests (`node:test`) |
| `npm run typecheck` | TypeScript check, no build step |
| `npm run check:comments` | Fail on a source comment that is not English |
| `npm run check:locales` | Language files: same keys and placeholders in every language, every key used in code exists |
| `npm run check:strings` | List user-facing text still written in code instead of `locales/` |
| `npm run check:hardcode` | Fail on organisation-specific values (your own list in `hardcode-deny.local.txt`) |
| `npm run db:deploy` | Apply database migrations |
| `npm run groups` | List and switch groups from the terminal |
| `npm run logout` | Sign the chat account out |
| `node scripts/make-readme-diagrams.mjs` | Redraw the diagrams of this page from `assets/readme/labels/<lang>.json` |

## Troubleshooting

| Symptom | What to do |
|---|---|
| The Work screen says the tasks table is missing | Run `npm run db:deploy`, then restart Deti |
| `http://localhost:7979` shows the old plain page | Build the admin page: `cd admin && npm install && npm run build` |
| A brain is shown as "not ready" | Sign in to that CLI on the machine (`claude`, `codex`) or set its key, then look at the Brain screen again |
| A lane is locked after a restart | Deti was stopped in the middle of a turn. Open Overview and use the unlock action for that lane. Restart only when every lane is idle |
| Deti does not answer in a group | Check on the Zalo screen that the group is switched on, and that the message mentions Deti, starts with its name, or replies to one of its messages |
| Deti answers, but in the wrong language | Set `language` in `deti.config.json` (or `DETI_LANG`) and restart |

Logs are in `data/logs/`, one file per day, and on the Logs screen.

## Limitations

- **Unofficial Zalo client.** Deti talks to Zalo through a bundled copy of [zca-js](https://github.com/RFS-ADRENO/zca-js), a reverse-engineered client that is not affiliated with or endorsed by Zalo. Using it may violate Zalo's terms of service and can get an account locked. Use a dedicated account and accept that risk yourself.
- **Two languages, one of them partial.** Prompts, replies, tool messages and the admin page come from language files (Vietnamese and English). Three things are still Vietnamese only: log lines, the phrase rules that recognise commands and vague promises in incoming chat, and the classification of engine error messages. An English-speaking group therefore works, but with weaker guard rules than a Vietnamese one.
- **Windows only** for now. Process management and autostart are Windows-specific.
- **No login on the admin page.** It is meant for the machine Deti runs on.
- Some rules and messages still assume a web-development team.

## Roadmap

- Telegram and Slack as chat channels, behind a common channel layer
- Linux support
- Sign-in for brain accounts (Claude, Codex, z.ai) from the admin page
- Login and roles for the admin page
- Phrase rules and logs in every supported language
- A first-run wizard

## Star, fork, take part

Deti is built in the open so that other teams can use it and shape it. Four things help more than anything else:

- **Star the repository.** It costs one click, it is how other teams find the project, and it tells us the work is worth continuing. → [Star Deti](https://github.com/hstation-net/deti-agent/stargazers)
- **Fork it.** Run your own copy, adapt the rules, prompts and language files to how your team works, add the channel you need. The licence lets you change anything for your own use. → [Fork Deti](https://github.com/hstation-net/deti-agent/fork)
- **Send back what you improve.** A fix, a translation, a new channel adapter or just a clear bug report: open an [issue](https://github.com/hstation-net/deti-agent/issues) or a pull request. Small ones are welcome.
- **Join the community.** Questions, ideas, release news and help from people who run Deti every day. → [Join the Deti group on Zalo](https://zalo.me/g/1w5ngqlvkr11erpzkyrd)

If you run Deti in your company, tell us how it goes. Real use is what decides what gets built next.

## Star history

<a href="https://star-history.dera.page/hstation-net/deti-agent">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://star-history.dera.page/svg?repos=hstation-net/deti-agent&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://star-history.dera.page/svg?repos=hstation-net/deti-agent" />
    <img alt="Star history chart of Deti" src="https://star-history.dera.page/svg?repos=hstation-net/deti-agent" />
  </picture>
</a>

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md). Run `npm run typecheck`, `npm test` and the four `check:*` scripts before opening a pull request. Source comments are written in English, and user-facing text goes in the language files.

## Licence

Deti is **source-available**: the code is public and free to use, but it is not "open source" in the OSI sense, because selling it is reserved to its maker.

It is licensed under the [Apache License 2.0 with the Commons Clause condition](LICENSE).

| You may | You may not |
|---|---|
| Read, run and modify the code | Sell Deti, or a product built mainly on it |
| Install it for your own company and use it in your daily work, at no cost | Offer it to others as a paid hosted service |
| Share your changes under the same terms | Charge for installing, hosting or supporting it as a business |

For a commercial licence or a partnership, contact [hstation](https://hstation.net).

> [!NOTE]
> This table is a summary; the [LICENSE](LICENSE) file is what applies. Third-party notices are in [NOTICE](NOTICE) and `vendor/zca-js/`.

Deti is built by [hstation](https://hstation.net).
