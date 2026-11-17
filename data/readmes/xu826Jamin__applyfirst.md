# applyfirst

**Find jobs the hour they go up. Apply first. See what is actually getting you interviews.**

Most postings fill on a rolling basis, so the people who apply in the first day get read first.
applyfirst checks thousands of company career boards directly, puts the newest postings that
match you at the top, fills and submits the applications with Claude, and reads the replies in
your inbox so you can see which applications turn into interviews and which do not.

Everything runs on your own computer. Your resume, answers and inbox never leave it, except
the applications you send to employers and the work Claude does for you.

## Set it up with Claude

Open Claude Code and paste this:

```
Set up applyfirst for me. Read https://raw.githubusercontent.com/xu826Jamin/applyfirst/main/AGENTS.md first and follow it step by step.
```

Claude tells you everything you need up front, checks and installs it with you, keeps applyfirst
up to date every 3 days, and walks you to your first application. AI agents setting this up:
read [AGENTS.md](AGENTS.md) before anything else.

![Jobs: the newest postings that fit you, each with why it was kept](docs/images/jobs.png)

![Settings: every choice in plain words, saved straight away](docs/images/settings.png)

> **Want the new postings without running anything?** applyfirst alerts sends you the jobs that
> fit you the hour they go up, with no install. Want it to apply for you too? That comes as an
> add-on. [Join the waitlist](https://forms.gle/MVQg9XdZPRxgSjXS7) and you're first in when it
> opens.

## What you get

- **Fresh postings first.** Thousands of company boards (Greenhouse, Lever, Ashby, Workday,
  SmartRecruiters, Workable and more) checked directly, not days later through a reposting site.
  Optional extras: Indeed, Glassdoor, LinkedIn, Google's past-24-hours results, job-alert emails,
  and your school's job board.
- **Only what you want.** Location, remote, career level (internship and co-op through senior),
  field, start date, term length, keywords, companies to skip, languages you do not speak.
  Every skipped posting tells you why.
- **Your order.** Newest first, soonest deadline, company, or best match: you choose.
- **Resumes from your real experience.** Upload the resume you have. applyfirst turns it into an
  experience bank you confirm once. Then pick how resumes are made: an ideal resume for each role
  group you choose, adjusted to each job (the default); one built fresh for every job; or your own
  file sent exactly as you made it. Settings explains the trade-offs. Every generated line traces
  back to something you confirmed, so nothing on it surprises you in an interview.
- **Applications filled for you.** Claude fills the form in your browser, including Workday.
  Review mode stops before submit so you can check it; auto mode submits and saves the confirmation.
- **Answer once.** Every new form question is asked once and remembered for every application after.
- **Know what is working.** Replies are read from your inbox and matched to applications. See your
  interview rate by source, resume, field, and how fresh the posting was when you applied.

**Where it is strongest today.** The built-in and discovered boards come mostly from technology and
engineering employers, so applyfirst is strongest for tech internships, co-ops and new-grad roles
in Canada and the US. Other fields and senior roles find fewer postings today. Any posting can be
added by pasting its link on the **Jobs** screen.

## Guides

- [Getting started](docs/GETTING_STARTED.md): from nothing to your first application
- [Connect your email](docs/EMAIL.md): reply tracking and alert emails (Gmail, iCloud, Yahoo)
- [Run it every day](docs/DAILY.md): the in-app schedule, Task Scheduler, cron, launchd and alerts
- [Troubleshooting](docs/TROUBLESHOOTING.md): the fix for the common snags
- [Security](SECURITY.md): what is protected and how, and how to report a problem
- [Contributing](CONTRIBUTING.md): how the code fits together, tests, and adding a job-site reader
- [Changelog](CHANGELOG.md)

## Install

You need:

- Python 3.10 or newer
- [Claude Code](https://code.claude.com/docs/en/quickstart), signed in (tested with 2.1.325, needs
  2.1.0 or newer)
- [Node.js](https://nodejs.org/) (the free LTS version) and Google Chrome, Edge or Chromium.
  Applications are filled in a Chrome window applyfirst opens for you. Sign in to a job site in
  that window once and it remembers you, and in review mode the filled form stays open in it for
  you to check and submit. No extension to install.
- Optional: the [Claude in Chrome extension](https://code.claude.com/docs/en/chrome) connected to
  Claude Code, if you would rather fill applications in your own Chrome with the sign-ins it
  already has. applyfirst uses it automatically when it is set up.

```
pip install git+https://github.com/xu826Jamin/applyfirst
applyfirst
```

`applyfirst` opens the app in your browser at http://127.0.0.1:8765. If your terminal says the
command is not found (common on Windows), run `python -m applyfirst` instead. Keep that terminal
window open while you use the app. The setup takes about ten minutes: upload your resume, confirm
your experience, say what you are looking for, press **Find jobs**. The full walk-through is in
[Getting started](docs/GETTING_STARTED.md).

### Updating

```
pip install -U --force-reinstall git+https://github.com/xu826Jamin/applyfirst
```

Your data upgrades itself.

### Uninstalling

```
pip uninstall applyfirst
```

Then delete the `~/.applyfirst` folder (your data home) if you want your profile, resumes and
applications gone too.

## Applying

1. **Jobs** lists the postings that fit, newest first, each with why it was kept. Approve the
   ones you want, then press **Apply to approved**.
2. Claude opens each application in Chrome, attaches your resume and fills every field it
   can from your profile and saved answers.
3. In review mode it stops before the final button. Check the tab, press submit yourself, then
   mark it **I submitted it** under **Applications** (with email connected, the confirmation
   email marks it for you).
4. Anything it could not do waits under **Needs you**: a sign-in, a CAPTCHA, or a question it has
   no answer for. Answer a question once under **Answers** and it is used everywhere after.
5. Connect your email in Settings and replies are matched to applications for you (they are read
   in the daily run, or any time you run `applyfirst sync`). **Insights** then shows what is
   getting you interviews.

The first search reads the built-in boards in about ten minutes, then grows to thousands of boards in
the background; later searches only pick up what is new.

## Run it every day

Turn on **Run every day** in Settings (it works while the app is open), or schedule
`applyfirst daily` yourself (Task Scheduler, cron or launchd) to run with the app closed. It finds
new postings, applies in auto mode, and reads new replies. See [Run it every day](docs/DAILY.md).

```
applyfirst sweep     # find new postings now
applyfirst apply     # apply to the approved queue now
applyfirst sync      # read replies now
applyfirst daily     # all three
```

## Settings worth knowing

You have full control. A few options come with a warning, shown next to them in Settings:

- **LinkedIn, Indeed, Glassdoor** as sources: these sites may restrict or sign out accounts they
  think are automated.
- **Auto mode** submits without showing you first. Some employers accept one application per role
  or per season.
- **Resume line checking** off: generated lines are no longer checked against your experience.

The browser tool Claude uses will not create accounts, type passwords or solve CAPTCHAs. When an
application needs one of those, it waits for you under **Needs you**, and continues once you are
done.

## What it costs

Filling a form uses Claude. On a single test, filling one application measured about $0.37 of
Claude usage. Your real average shows on the **Insights** screen, measured from Claude Code's own
usage report. A daily spending limit is on by default ($10; change it in Settings, under Claude),
so a big batch never surprises you.

## Where your data lives

`~/.applyfirst` (set `APPLYFIRST_HOME` to move it): your profile, settings, experience bank,
resumes, applications and a local database. The mail password, if you connect your inbox, is in
`secrets.json` there and is never shown back by the app. Mail is read only: applyfirst never sends,
moves, flags or deletes a message. Connecting email takes two minutes: see
[Connect your email](docs/EMAIL.md). How the app is kept safe, and the one limit to know about, is
in [Security](SECURITY.md).

## Contributing

Job sites change their forms. When one breaks, open an issue with the site and the step, or send a
fix. [CONTRIBUTING.md](CONTRIBUTING.md) covers the live check and how to fix or add a job-site
reader, and `docs/CONTRACTS.md` explains how the parts fit together. Tests run offline:

```
pip install -e ".[dev]"
pytest
```

## License

Copyright (C) 2026 Jamin Xu. Free software under the [GNU Affero General Public License v3.0](LICENSE) or later: use it, change it and share it. If you run a changed version as a service for other people, you must offer them your changed source code.

The public list of company boards that discovery starts from is downloaded at run time from
[an open internship list](https://github.com/zshah101/Automated-List-Of-Summer-2027-and-Fall-2026-Tech-Internships).
