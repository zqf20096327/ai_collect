# job-search-playbook

A job-search playbook for the personal agent you already have. It tells your Claude Code or Codex agent how to run a job search for you: the rules to settle with you first, where to find postings, how to screen them, how to fill the forms, how to track what comes back. Your agent decides with you which parts to use and writes whatever small scripts it needs. Not one more app: it runs on the agent you already use, with what it already knows about you.

There is no app and no code here, only markdown. It was built from about 12 weeks and ~400 applications an agent filed for one person: what worked, what did not, and the numbers. URLs and numbers age: see the note at the top of `playbook.md` before you rely on one.

## What your agent needs
- [Zucchini](https://zucchini.chat): your agent runs in its chats. Zucchini keeps the standing chats running, runs the watch that starts an apply session per job and the scheduled runs that look for postings.
- Claude Code for the parts that run on their own: the standing sessions, the dispatcher's headless apply sessions and the hand-off to the writer, which message each other by name. Codex can do the rest in one session: the rules, the CV versions, the sweeps, a single application.
- [shared-chrome-mcp](https://github.com/zucchini-chat/shared-chrome-mcp): one always-on, logged-in Chrome shared by all your agents, a window each. Forms, uploads and logins happen there.
- Optional: an agent set up from [personal-agent-scaffold](https://github.com/zucchini-chat/personal-agent-scaffold). It adds memory (a repo your agent keeps current), a mail desk that logs rejections and routes replies, the data guard that keeps your phone and ID numbers out of everything but job forms, and `agents/` for the recurring jobs.

## Start
Tell your agent: "take https://github.com/zucchini-chat/job-search-playbook, set it up and suggest the chats I need". It asks almost nothing. First it reviews where your hunt stands: the applications you already sent and how far each got, from your mail, calendar, LinkedIn and files, shown on a dashboard. Then it drafts your rules from that evidence as one draft for you to correct, builds your CV versions, writes its own pieces and suggests the chats, which you accept in Zucchini. Nothing is submitted until you say so: it starts in rehearsal, and you settle the open points while you check its first forms.

Your rules, CV and tracker go into your agent's repo, never into this clone. For updates, `git pull` in the clone and ask your agent what changed and whether to bring it into your files.

## What is inside
| File | What |
|---|---|
| `playbook.md` | The playbook: the rules to set first, the architecture, sourcing, screening, ATS endpoints, LinkedIn, applying, the CV, tracking and the dashboard, interviews, offers, results. |
| `switch-on.md` | The steps your agent runs with you to switch it on. |
| `applications.tyaml` | The format of the one queue and tracker, with example rows. |
| `LICENSE` | MIT. |
| `SECURITY.md` | How to report a vulnerability. |

## For the agent reading this
If this repo is not next to your own yet, clone it there first: from inside your repo, `git clone https://github.com/zucchini-chat/job-search-playbook ../job-search-playbook`. Then follow `switch-on.md` with your human; it starts with reading `playbook.md` in full.
