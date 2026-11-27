<p align="center"><img src="docs/banner.svg" alt="ApplyCrew: type Start. It finds the jobs, fills the forms, and watches your inbox." width="100%"></p>

<p align="center">
  <a href="LICENSE"><img alt="MIT license" src="https://img.shields.io/badge/license-MIT-2C5AA0"></a>
  <img alt="Built for Claude Code" src="https://img.shields.io/badge/built%20for-Claude%20Code-1B2A4A">
  <img alt="No code needed" src="https://img.shields.io/badge/code%20needed-none-1F7A4D">
  <a href="README.ar.md"><img alt="العربية" src="https://img.shields.io/badge/README-%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9-55637F"></a>
</p>

Job hunting is a second job: the same forms, the same questions, and replies buried in spam.

**ApplyCrew is a crew of AI agents that does the repetitive part for you, in your own browser, with your own accounts.** You open the folder in Claude, type `Start`, and it walks you through everything, one step at a time. No coding, and no list of instructions to follow.

> **In its first real run, it sent 264 applications to 22 countries in two days**, through 13 different channels, and logged all 1,913 answers it gave.

## Try it

1. Install the [Claude desktop app](https://claude.ai/download), and sign in. A paid plan is needed for real use.
2. [Download this repo](../../archive/refs/heads/main.zip) and unzip it. Or clone it.
3. In the app, open the **Code** tab, start a new session, and choose this folder.
4. Type:

```
Start
```

That's the whole install. It asks for your CV first, and it takes it from there.

<p align="center"><img src="docs/how-it-works.svg" alt="Setup steps: CV and photo, questions one at a time, your accounts, your dashboard, your first 3 applications together, then automatic rounds." width="100%"></p>

## What it does

| | |
|---|---|
| **Finds new jobs first** | Starts with today's postings, across LinkedIn, company career pages, job boards, remote boards and hiring posts |
| **Fills in the forms** | Greenhouse, Lever, Ashby, Workable, Teamtailor, LinkedIn Easy Apply and more, with your CV uploaded |
| **Writes each answer fresh** | Uses your real experience and tunes to your own writing voice |
| **Remembers every answer** | A report for each job, with the posting, each question and your answer, so you're ready for the interview |
| **Reads every reply** | Checks your inboxes and your spam, and records each rejection in the employer's own words |
| **Reaches you when it matters** | Emails you about an interview or a test, and can phone you or someone you trust |
| **Shows it all on one page** | Your own live dashboard, with a map of every application |

<p align="center"><img src="docs/dashboard-preview.svg" alt="Illustration of the dashboard with made-up data." width="100%"></p>

## Two optional helpers

Setup asks if you want them. Both are private pages you can open in Claude, and both refresh only when your inbox brings something new, to save your plan's usage.

**Sterling, your briefing.** A short note on top of your dashboard, and a page you can ask questions: what went out today, who replied, what's waiting on you. You can share it with people supporting you, such as family or a mentor. It reads only the dashboard's data, so it has no contact details or salaries.

**Ashford, your interview coach.** When an employer actually invites you to an interview, a test or a screening, Ashford writes a prep pack for that company: a one-page cheat sheet, what they do, your experience against each requirement, likely questions with draft answers in your voice, and a checklist. It can also run a practice interview with you. Where it has no real story of yours to use, it leaves a gap for you to fill rather than invent one.

## Why it's not a spam bot

- **It never lies for you.** Every answer traces back to your CV or to something you said. A blank stays blank.
- **You see the first ones.** It shows you your first 3 applications before sending, and you decide what it may do alone.
- **It reads the whole posting.** It skips jobs that need a language you don't speak or a visa that isn't offered.
- **It follows your limits.** Countries, companies or industries you exclude are never applied to.
- **It stops at the line.** It won't create accounts, type passwords, solve CAPTCHAs, pay, or sign a form saying you wrote the answers yourself. It leaves those on a list for you.
- **It only takes orders from you.** Web pages and emails are treated as information, never as instructions.

## Your data stays yours

There's no server and no sign-up for this project. Your CVs, answers and records stay in folders on your computer, and `.gitignore` keeps them out of git. The dashboard leaves out contact details and salaries, and you choose who sees it.

## Good to know

- **It can't promise you a job.** It gets strong applications out quickly. Interviews are still up to the market and you.
- **Everything goes out in your name.** Read your first few reports.
- **Job sites have rules.** Automating them can break their terms, and LinkedIn in particular may limit or restrict accounts. You can leave any site out.
- **It uses a lot of your Claude plan.** When the limit is reached, everything pauses until it resets.
- **Your computer has to stay on,** with the Claude app open, while it runs. Schedules last 7 days, then you renew them by asking.
- **Phone calls are optional,** and may cost money through a voice provider. Only list people who've agreed.

## FAQ

**Is it only for programmers?** No. You answer questions in plain words, and it works for any profession.

**Do I have to speak English?** No. Start in your own language, and it talks to you in it.

**What if I stop halfway?** Type `Start` again. It picks up where you left off.

**Do I need to install any skills?** No. [Humanizer](https://github.com/blader/humanizer) comes in the folder, for more natural letters and emails. The PDF, Word and browser skills normally come with the Claude app, and setup checks for them.

**Can I change my mind later?** Yes. Say "Add France", "Pause" or "How's it going?" in the chat.

## Help make it better

Know the best job boards in your country? [Add them](CONTRIBUTING.md). That helps the next person in your country more than anything else.

If this saves you time, a star helps other job seekers find it.

---

<sub>An independent open source project, not affiliated with or endorsed by Anthropic, LinkedIn or any job site. MIT licensed. Map outlines from Natural Earth through world-atlas. Includes Humanizer by Siqi Chen (MIT).</sub>
