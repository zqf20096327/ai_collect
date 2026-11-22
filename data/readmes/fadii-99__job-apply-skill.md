# Job Apply: AI LinkedIn Auto Apply Skill for Claude Code

**An open-source Claude Code skill that finds LinkedIn jobs that fit you and applies to them automatically, from your own Chrome, with a resume tailored to every job.**

It reads your real project code to build a resume backed by evidence (no made-up skills), writes an ATS-friendly PDF, then applies through **LinkedIn Easy Apply**, the **company's own careers site** (Greenhouse, Lever, Ashby, Workable and others) or **email**. It fills every form field from your own data, uploads the right resume, checks its work before pressing Submit, and asks you in the chat when a page needs a human.

[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-skill-d97757)](https://claude.com/claude-code)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-3776ab)](https://www.python.org/)
[![Playwright MCP](https://img.shields.io/badge/browser-Playwright%20MCP-2ead33)](https://github.com/microsoft/playwright-mcp)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

> If this saves you hours of copy-pasting into job forms, please **star the repo**. It helps other job seekers find it.

---

## Why this one is different

Most "auto apply" bots spray the same resume everywhere and guess at form answers. This skill is built around one rule: **no wrong data, ever.**

| | Typical auto-apply bot | Job Apply |
|---|---|---|
| Resume | One generic file | Tailored per job, every skill verified against your own code |
| Form answers | Guessed or pattern-filled | Only from your profile and saved answers; unsure means it asks you |
| Where it applies | Easy Apply only | Easy Apply, company careers sites, and email-only postings |
| Browser | Separate bot browser, fresh logins | Your own Chrome, already logged in |
| CAPTCHAs and logins | Tries to bypass, or silently skips | Pauses, asks you, carries on from the same page after you type `go` |
| Your data | Often a cloud service | Stays on your laptop |

## Features

- **Evidence-backed profile.** Point it at your project folders. It reads the code, checks what you say you did against what is really there, and builds a verified skills ledger and a professional summary.
- **ATS-friendly resume generator.** Clean one-column PDF that applicant tracking systems parse well, rebuilt and tailored for each job description (order and emphasis change; facts never do).
- **LinkedIn job search.** Searches by your target roles, seniority, locations and work mode (remote, hybrid, on-site), newest first, and scores each job's fit before applying.
- **LinkedIn Easy Apply automation.** Goes through every step of the Easy Apply dialog, uploads the tailored resume, answers screening questions from your saved answers.
- **Company careers sites.** Follows the "Apply" button to Greenhouse, Lever, Ashby, Workable, SmartRecruiters or a company's own form, and fills it the same careful way.
- **Email applications.** When a posting only says "send your CV to ...", it writes a short, specific email and sends it from your Gmail with the resume attached.
- **Human in the loop, only when needed.** A CAPTCHA, a login, or a question your profile can't answer? It tells you what to do in Chrome, waits for `go`, and continues on the same page. `skip` puts the job on a manual list with a ready resume.
- **Read-back check before Submit.** Every field is compared with its source before the final click. A mismatch it can't fix means it doesn't submit.
- **Duplicate and limit protection.** Never applies to the same job twice, caps applications per company and per day (10 by default).
- **Dry run mode.** Fills everything but stops before Submit, so you can check a few first.
- **Live view and a plain spreadsheet.** A local page shows what it is doing right now; `My_Job_Applications.csv` lists every job found with status, reason, links and the files sent.
- **Talks your language.** Give your details in any language; resumes and applications are written in English.

## How it works

```
 Your project folders + details
            │
            ▼
  1. Setup (once)  ── reads your code, verifies claims ──► profile + base resume (PDF)
            │
            ▼
  2. Search LinkedIn  ── roles, locations, remote/hybrid/on-site ──► fit score per job
            │
            ▼
  3. Apply, one job at a time, in your Chrome
       ├─ Easy Apply on LinkedIn
       ├─ company careers site (Greenhouse, Lever, Ashby, ...)
       └─ email (from your Gmail)
            │   tailored resume + read-back check + Submit
            ▼
  4. Report: applied / needs you / skipped, with links and files
```

## Requirements

- [Claude Code](https://claude.com/claude-code)
- Python 3.10+ with PyYAML (`pip install pyyaml`)
- Google Chrome with the free [Playwright Extension](https://chromewebstore.google.com/detail/playwright-extension/mmlmfjhmonkocbjadbfplnigmagldckm) (Claude walks you through adding it)
- Node.js 18+ (runs the [Playwright MCP](https://github.com/microsoft/playwright-mcp) browser server with `npx`)
- Optional: a Gmail App Password, for email-only job postings
- Optional, for the PDF tests: `poppler-utils`

## Quick start

Pick one folder for job hunting and clone the skill into its `.claude/skills/`:

```bash
mkdir ~/JobHunt && cd ~/JobHunt
git clone https://github.com/fadii-99/job-apply-skill.git .claude/skills/job-apply
python3 .claude/skills/job-apply/scripts/install.py --project .
```

Then start Claude Code there and type `/job-apply`:

```bash
cd ~/JobHunt && claude
```

The first time, Claude guides you one click at a time:

1. Add the Playwright Extension to Chrome.
2. Copy the extension's connection code into the chat.
3. Restart Claude Code once.
4. Paste your details (projects with folder paths, jobs, education, contact). Any order, any language.
5. Review your resume, pick target roles and locations. Done.

Your files end up here:

```
~/JobHunt/                       ← open Claude Code here
├── .claude/skills/job-apply/    ← this repo (code only, no personal data)
└── job-apply-data/              ← shortcut to ~/.job-apply (your profile, resumes, logs)
```

**Email applications (optional):** put a Gmail App Password in `~/.job-apply/.env`. Steps: [references/email-guide.md](references/email-guide.md).

**Update:** `cd ~/JobHunt/.claude/skills/job-apply && git pull`. Your data is untouched.

## Commands

| Type in Claude Code | What happens |
|---|---|
| `/job-apply setup` | Builds your profile and resume by asking you questions. Once. |
| `/job-apply start` | Searches LinkedIn and applies until today's limit. Add `remote only`, `hybrid`, or a role. |
| `/job-apply apply <link>` | Applies to one job link you give (LinkedIn or any company site). |
| `go` / `skip` | After it asks for help: continue on the same page, or leave the job for later. |
| `/job-apply watch` | Opens the live page. |
| `/job-apply stop` | Finishes the current job and stops. |
| `/job-apply status` / `report` | Today's numbers / the last N days. |
| `/job-apply limit 5` | Applications per day (default 10). |
| `/job-apply browser` | Connects or fixes the Chrome connection. |

Plain words work too: "start applying for remote Django jobs", "LinkedIn logged me out", "I got an interview at Acme".

**Tip for the first run:** ask Claude to turn on `dry_run`. It fills every form without the final Submit, so you can check a few applications first.

## Privacy: your data stays yours

- This repo holds only generic code and rules. It never contains anyone's data.
- Everything personal lives on your laptop in `~/.job-apply/`: profile, resumes, logs, the extension's connection code, and the optional Gmail App Password.
- Project analysis is read-only and never opens `.env` files, keys or credentials in your projects.
- Passwords are never typed or stored. You log in to LinkedIn yourself, in your own Chrome.
- Nothing is sent anywhere except to LinkedIn, the companies you apply to, and your own Gmail.

## Honest limits

- **LinkedIn's terms prohibit automated access**, and an account that applies too much can be restricted. The skill applies one job at a time, with pauses, at most 10 a day by default. Use it at your own risk.
- Job sites change. The skill reads each page like a person would instead of following fixed steps, but some jobs will still end up on the manual list.
- It never solves CAPTCHAs, never creates accounts, never takes tests for you. Those need you.

## FAQ

**Is this a LinkedIn Easy Apply bot?**
Yes, and more: it also applies on company careers sites and by email, with a different tailored resume for each job.

**Does it invent skills to pass ATS filters?**
No. A skill appears on your resume only if it is verified in your code or you confirmed it. Tailoring changes order and emphasis, never the facts.

**Do I need to know how to code?**
No. You type in plain words; Claude does the steps and tells you exactly what to click when it needs you.

**Which job sites does it search?**
LinkedIn only. Other job boards showed CAPTCHAs and bot checks too often. Any company site a LinkedIn job leads to is supported, and you can give it any job link with `apply <link>`.

**Does it work on macOS and Windows?**
It is developed on Linux. The browser setup supports macOS and Windows paths, but those are less tested; reports and pull requests are welcome.

## Tests

```bash
python3 -m unittest discover -s tests
```

## Contributing

Issues and pull requests are welcome: better hints for careers sites (`references/sites/`), platform fixes, translations of the guides. Please never include real personal data in issues, tests or examples.

## License

MIT, see [LICENSE](LICENSE). The bundled Arimo font is under the SIL Open Font License 1.1 ([assets/fonts/LICENSE-Arimo.txt](assets/fonts/LICENSE-Arimo.txt)).

---

**Keywords:** LinkedIn auto apply, LinkedIn Easy Apply automation, AI job application bot, automatic job applications, Claude Code skill, Claude agent, AI resume tailoring, ATS resume generator, job search automation, Playwright MCP, Greenhouse and Lever auto fill, apply to jobs automatically.
