<p align="center">
  <img src=".github/assets/banner.png" alt="OmegaStar" width="80%">
</p>

<h3 align="center">Build your $1B one-person company on the Claude Code you've already set up.</h3>

<p align="center">A desktop app that turns your Claude Code into a team of AI employees. Give them roles, put them in an org chart next to the real people you work with, and teach them by talking.</p>

<p align="center">
  <a href="#quickstart"><strong>Quickstart</strong></a> &middot;
  <a href="#see-it-work">See it work</a> &middot;
  <a href="#how-it-works">How it works</a> &middot;
  <a href="#faq">FAQ</a>
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: AGPL-3.0" src="https://img.shields.io/badge/license-AGPL--3.0-blue?style=flat-square"></a>
  <img alt="Platforms: macOS, Windows and Linux" src="https://img.shields.io/badge/platforms-macOS%20%7C%20Windows%20%7C%20Linux-lightgrey?style=flat-square">
  <img alt="Status: alpha" src="https://img.shields.io/badge/status-alpha-orange?style=flat-square">
  <img alt="Requires Claude Code" src="https://img.shields.io/badge/requires-Claude%20Code-555555?style=flat-square">
  <a href="https://buymeacoffee.com/futsy"><img alt="Buy Me a Coffee" src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-support-FFDD00?style=flat-square&logo=buymeacoffee&logoColor=black"></a>
</p>

<p align="center">
  <sub>Proudly sponsored by <a href="https://vibetyper.com/?utm_source=omegastar&utm_medium=readme&utm_campaign=sponsor"><img src="https://vibetyper.com/images/vibe-typer-logo.png" alt="" width="16" height="16" align="absmiddle"> <strong>Vibe Typer</strong></a></sub>
</p>

**Keep the agent you trust. OmegaStar adds the company around it.**

OmegaStar is not another agent. Every AI employee (an autonomous Claude Code agent) is your own Claude Code, running headless (`claude -p`) under your login, with the CLI tools, logins and skills you've already set up. OmegaStar adds what turns them into a team: roles, an org chart that includes real people, schedules, managers, and skills that grow as you teach. Use it to run your team, your project or your business.

## See it work

Juno is hired to run support, learns the morning email, and the next day has it done at 7 am with the window closed. Two and a half minutes, with sound.

https://github.com/user-attachments/assets/db3e331b-af9e-4dea-aa12-97bc4a2c65b1

## Why OmegaStar

You tried the agent frameworks. You went back to Claude Code. OmegaStar starts where you ended up.

### Don't rebuild the agent

Personal agent frameworks try to reinvent the wheel. Each one builds its own agent loop, tool calling, browser and integrations, so setup is full of friction, results fall short, and you end up in integration hell. Many people drift back to doing their automations and daily work in a coding agent like Claude Code or Codex. [One Hacker News thread](https://news.ycombinator.com/item?id=47783940) is full of them, summed up as: "I could achieve everything it did with a long running Claude Code instance and a good mobile frontend."

There's a good reason. The top coding harnesses are simply the best at what agents actually do all day: calling tools, running commands and using a browser. So every OmegaStar employee is your own Claude Code, not a reimplementation of it.

### Your computer is already set up

The environment is the other half. Your machine already has your apps, your CLI tools, your logins and your skills. An agent that runs there can use all of it from the first minute, with nothing to connect. That's what makes a personal agent system powerful, and it's what frameworks and cloud agents have to rebuild.

### Think in people, not prompts

Making an agent autonomous is hard mostly because it's hard to decide what it should do. Thinking of agents as people makes that easy. You hire a specialist for a job, give them an objective and the tools they need, and tell them who they report to.

The real people you work with go on the same org chart, each with a description, their strengths and how to reach them. Employees know when to bring in a human and how, just like a colleague would. If you'd hire someone for a job in your team, project or business, you can hire an employee for it.

### Teach them like a colleague

You teach an employee by talking to them, the way you'd teach a new hire. Each lesson becomes a skill, built in the small, composable style popularised by [Matt Pocock's skills](https://github.com/mattpocock/skills) on Anthropic's open [Agent Skills](https://agentskills.io) format. Employees organise and tidy their own skills as they grow, and every change can be undone.

## How it works

| Step | You | Your employee |
|---|---|---|
| **1. Hire** | Pick a template or start blank. Set a title, an objective and skills. | Gets a role skill that starts from that objective. |
| **2. Teach** | Explain a task in a conversation, or correct a report by replying to it. | Writes it into a skill and names the one that changed. |
| **3. Delegate** | Give them a schedule, a manager and people to ask. | Works on their own, asks when stuck, reports back. |

- **People.** Record each person's role, strengths and channels (Teams, Slack, email, Jira and more), each with a "When to use" line. Employees reach out with your Claude Code's own tools, and OmegaStar tracks each request: a reply resumes the work, and without one the employee nudges once, then carries on.
- **Managers and colleagues.** Managers delegate to their direct reports and hear back in batches, employees ask each other for help or pass on news without starting work, and any of them can propose a hire for you to approve.
- **Several things at once.** Every conversation with an employee is its own thread and runs alongside the rest of their work, so you can have several going at once. When a colleague answers something they asked along the way, the answer comes back into that conversation. Mark it done when it's finished and it moves to the Archive. To steer work in progress, write in its conversation: the employee sees it as they work.
- **Schedules and the Inbox.** Schedules run from the tray and catch up once after the computer was off or asleep, unless you set them to skip, and can keep to business hours. The Inbox holds only what needs you: hire proposals, decisions, things only you can do, questions, news worth knowing and blocked actions. Similar decisions come together so you can approve them at once, the keyboard moves through it all, and Later brings a decision back on the day you pick. When an employee asks several questions at once, they're one item, and the employee hears all your answers together once the last one is in. Everything else, from reports that need nothing from you to conversations you've finished, goes to the Archive. The Activity page shows what each employee is working on now, open requests to people, asks between colleagues, this week's numbers, and what each routine uses and achieves.
- **Skills that grow.** Each employee's role skill routes to small, one-job skills they write as you teach. Tidies run on their own, big restructures wait for your approval, a rule you taught is put back if a tidy drops it, and every skill edit can be undone. A lesson that's true for everyone goes to the company page with one tap from you, so every employee learns it.
- **You stay in charge.** New employees are Supervised: they edit files in their own folders, and anything else you haven't allowed is blocked until you click **Allow once** or **Always allow**, and either one retries the work. What an employee may decide alone, set in what they own, reaches every run they do. **Pause schedules** stops all scheduled work.
- **Runs on your Claude Code.** Every run, including the short Haiku calls that check for replies, is a `claude -p` process under your login. OmegaStar has no agent loop or API client of its own, and nothing to host.

## Is it for you?

**A good fit** if you use Claude Code most days, have recurring work for a team, a project or a business, and would rather keep your setup than rebuild it.

**Not a fit** if you want a chat bot on your phone, other models (OmegaStar runs Claude Code only), an agent that works while your computer is off or asleep, sandboxed agents, or a tool your whole team signs into (it's one person on one computer).

## Quickstart

**You need:** Claude Code installed and signed in (`claude auth status` shows `loggedIn: true`).

1. **Download and install** the app for your computer from the [latest release](https://github.com/itsfutsy/OmegaStar/releases/latest):
   - **macOS:** the `.dmg`, for Apple Silicon Macs only.
   - **Windows:** the `-setup.exe`. It isn't signed yet, so Edge may say it "isn't commonly downloaded". Point at that download, click the **...** that appears, choose **Keep**, then click the arrow next to **Delete** and choose **Keep anyway**. If "Windows protected your PC" appears instead, click **More info**, then **Run anyway**.
   - **Linux:** the `.AppImage` (tested on Ubuntu 24.04).
2. **Open your office.** Setup checks Claude Code and asks for your company, name and title. Turn on "Keep OmegaStar running in the background" so it starts at login. Closing the window leaves it in the tray, where schedules keep running.
3. **Hire your first employee** from a template, such as Chief of Staff. A new conversation opens with a first lesson already written. Send it, and they'll interview you and write their first skill.

**Tip:** start with one employee and one job, and expect a short training period while you allow the commands and tools they need.

<details>
<summary>Build it yourself</summary>

You need Rust (stable), Node.js 20.19+ or 22.13+, the Xcode Command Line Tools on macOS, and on Windows the MSVC C++ Build Tools with a Windows SDK.

```
git clone https://github.com/itsfutsy/OmegaStar.git
cd OmegaStar
npm install
npm run tauri dev
```

`npm run tauri build` makes installers for the platform you're on. On Windows, use PowerShell or cmd rather than Git Bash, or the build fails.

</details>

## FAQ

<details>
<summary><b>How is this different from OpenClaw or Hermes Agent?</b></summary>

They are personal agents with their own runtime, tools and chat-app gateways, built for many models, which you set up and maintain. OmegaStar builds none of that: each employee is your own Claude Code. Hermes Agent also learns skills; here, what you teach lands in named skills you can diff and undo. For a model-agnostic assistant you chat with from your phone, they are the better fit.

</details>

<details>
<summary><b>How is this different from Paperclip?</b></summary>

Paperclip is a server and dashboard for running autonomous agent organisations across many agent harnesses. OmegaStar is a desktop app for a company with people in it: your colleagues sit on the same org chart without an account, and employees reach them on the channels they already use. Employees learn by being talked to and bring you only what needs you. There's nothing to host, and each employee is just your own Claude Code.

</details>

<details>
<summary><b>Can't I do this with Claude Code, cron and a CLAUDE.md?</b></summary>

You can, and plenty of people do. OmegaStar is that setup without the glue scripts: roles and an org chart that includes real people, schedules, one Inbox, one-click approvals, and skills that are versioned and kept tidy. It also handles the fiddly parts, like resuming the right session when a person finally replies, nudging once then moving on, and holding upkeep back when usage is high.

Claude Code's own sub-agents, agent teams and scheduled tasks are building blocks. OmegaStar gives them a standing team: employees keep their role, skills, schedules and manager across restarts, and still use sub-agents inside a run.

</details>

<details>
<summary><b>Is it safe to give employees my computer?</b></summary>

Employees run as you, and there is no sandbox; containers isolate better. Supervised (the default) edits files only in the employee's folder and any folders you add, and blocks every other tool you haven't allowed, in OmegaStar or in your own Claude Code settings. That includes your user-level MCP servers and claude.ai connectors, which every employee can reach. Browser control is on by default, so a new hire can drive your Chrome, signed in as you; turn it off for any employee under Advanced. Autonomous blocks nothing, and the app warns you.

</details>

<details>
<summary><b>What does it cost, and is it allowed on my plan?</b></summary>

OmegaStar is free and open source; you pay for your Claude plan as usual. It runs the official Claude Code CLI as you and never reads your Claude credentials, so Anthropic's terms for your plan apply (see [Using it responsibly](#using-it-responsibly)). Work runs are capped at 3 at a time by default, across the office and for any one employee; what you type to an employee, and work a manager delegates while it waits, skip the cap; card answers and approvals wait like other work. The sidebar shows your 5-hour and 7-day Claude usage, and background upkeep (never real work) waits when usage is high.

</details>

<details>
<summary><b>Will an employee spam my colleagues or pretend to be me?</b></summary>

Employees are told to ask only when stuck, send one clear request and sign as your AI assistant, and each request gets one nudge at most. Those are instructions to the model; OmegaStar itself sends nothing. The hard stop is Supervised: a messaging tool you haven't allowed stays blocked until you approve it.

</details>

<details>
<summary><b>Does it integrate with Slack, Jira, email or Teams?</b></summary>

It ships none. Employees use your CLI tools, user-level MCP servers, claude.ai connectors and the plugins you grant them, but not MCP servers set up for one project folder. When an employee asks on Teams through a local Microsoft 365 MCP server (`@softeria/ms-365-mcp-server`), OmegaStar reads the reply itself. Elsewhere a short reply check looks for it, or you answer for the person.

</details>

<details>
<summary><b>Can I bring my own skills? Will it touch my setup?</b></summary>

Yes. Grant skills from your Claude Code catalog, or import copies for an employee to organise. OmegaStar changes your skills folder only when you click **Make a company skill** or ask it to move imported originals to the Trash. Employees live in OmegaStar's own folder, and there's no account, cloud service or telemetry.

</details>

<details>
<summary><b>Isn't the one-person company line just hype?</b></summary>

Fair. Nobody builds a company alone, which is why real people sit on the org chart. The headline is the ambition; everything under it is what the app does today.

</details>

## Using it responsibly

OmegaStar runs your own Claude Code under your own login, so your use is covered by Anthropic's terms for your plan and its [Usage Policy](https://www.anthropic.com/legal/aup). In particular:

- Use your own account. Don't share a login or run OmegaStar for other people on your subscription.
- You are responsible for what your employees do through their tools, including messages to real people. Employees are instructed to sign every message as an AI assistant; keep it that way.
- Pro and Max limits assume ordinary, individual use. For heavy or round-the-clock schedules, an API key or a Team or Enterprise plan is the better fit.

OmegaStar is an independent project, not affiliated with or endorsed by Anthropic. Claude and Claude Code are trademarks of Anthropic.

## Development

OmegaStar is a native desktop app: a Rust backend (Tauri 2) with a React frontend rendered in the operating system's webview.

```
npm run typecheck
npm run lint

cd src-tauri
cargo test
cargo clippy --all-targets
```

`npm run dev` on its own opens every screen in a plain browser, with an invented office standing in for the backend (see [src/preview](src/preview/README.md)). Screenshots for a pull request come from there too: `scripts/pr-shots.sh <pr number> <image>...` uploads them and prints the lines for the description. The shared styles and parts are described in [src/design](src/design/README.md).

Your office lives in the app data directory: `~/Library/Application Support/OmegaStar` on macOS, `%APPDATA%\OmegaStar` on Windows and `~/.local/share/OmegaStar` on Linux. A dev or dogfood build uses `OmegaStar-dev` or `OmegaStar-dogfood` beside it, so it never touches your real office. Set `OMEGASTAR_DATA_DIR` to use another folder. Errors are logged to `omega.log` there.

Each employee has a folder there with a generated `CLAUDE.md` handbook, their own skills and a scratch workspace. A per-run `settings.json` hides skills they weren't granted, and office tools (delegation, requests, schedules) use an MCP endpoint the app serves on 127.0.0.1.

## Support OmegaStar

OmegaStar is free and open source. If it saves you time, you can [buy me a coffee](https://buymeacoffee.com/futsy). It helps keep the updates coming.

<a href="https://buymeacoffee.com/futsy"><img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-support%20OmegaStar-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=black" alt="Buy Me a Coffee"></a>

Not in a position to give? Starring the repository and telling a friend helps too.

## License

Copyright (C) 2026 Abram Industries Pty Ltd

OmegaStar is licensed under the [GNU Affero General Public License v3.0](LICENSE). Commercial licences
without the AGPL's terms are available from Abram Industries ([abramindustries.com](https://abramindustries.com)).
