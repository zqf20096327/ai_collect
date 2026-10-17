# A job search that reads the job ads for you

[![tests](https://github.com/estherica615-svg/jobhunt-net/actions/workflows/tests.yml/badge.svg)](https://github.com/estherica615-svg/jobhunt-net/actions/workflows/tests.yml)

LinkedIn shows you a title, a company, and a location. You decide from that
whether to open it. So most people filter on the title — which means the jobs
with a bad title never get seen, and the jobs with a good title waste your
evening.

This does the opposite. A script pulls the **full text** of every ad matching
your keywords into a folder. Then an AI reads all of them against a short file
you wrote about yourself, and tells you which ones are worth your time — and
what it's worried about.

The script is ~650 lines of Python. No dependencies, no API keys, no account,
no install.

## The one idea

**The script does not judge. It is a net, not a sieve.**

It deliberately does not score, filter, or rank by relevance, because keyword
matching cannot tell you whether a job is right for you and shouldn't pretend
to. It casts a wide net, deduplicates, downloads the full text, and stops.
Everything that requires actually understanding the job happens afterwards,
by something that has read the job description and has read about you.

Three things that follow from that, which are features and not omissions:

- **No scores.** No "85% match". A number is a judgement you can't argue with,
  and the reasoning is the part that's actually worth anything.
- **No filtering.** Nothing is silently dropped before you see it. Seniority can
  push an ad to the bottom of the list, but never out of it — on LinkedIn the
  best roles are often titled "… Lead", so filtering by title kills exactly the
  ones worth reading.
- **No daily "nothing today".** If there's nothing good, it says nothing. A tool
  that reports in every day trains you to ignore it.

## Setup

**You need:** Python 3 (already on macOS and Linux), and an AI you can chat
with. The free tier of claude.ai or chatgpt.com is fine.

### 1. Write your file — 10 minutes, once

Copy `me.template.md` to `me.md` and fill it in.

Be blunt. *"I don't want to manage anyone."* *"I'll take a pay cut for a 4-day
week."* *"I'm not moving to the CBD."* The awkward, specific things are exactly
what makes the judgements useful. Vague in, vague out.

`me.md` is gitignored and never leaves your machine.

### 2. Set your search terms

Just run the script — with no `keywords.txt` it copies `keywords.example.txt`
into place for you and stops. That file is a form: fill in the blanks.

**Anything left in `<angle brackets>` stops the script and gets pointed at by
line number.** That's deliberate. A search that quietly ran with the example's
city in it would return perfectly plausible jobs in a town you don't live in,
which looks exactly like working.

Cast wide. A keyword that pulls in some junk is fine — junk is thrown away
cheaply after the JD is read. A keyword that's too narrow costs you jobs you'll
never know existed.

You can group your keywords and rank the groups, which decides what gets read
first when there's more than you can get through:

```
LOCATION: Berlin, Berlin, Germany
REMOTE: Germany                   # also search Germany-wide, remote-only
                                  # (or `yes` for remote where you already are)

[Direct hits]
RANK: 1
Data Engineer
Analytics Engineer

[Safety net]
RANK: 2
REMOTE: no                        # override the global default
business intelligence
```

Give two groups the **same** rank and they're peers — use that when you're
pursuing several directions in parallel and don't want to pretend one outranks
the other. Skip `RANK` entirely and groups fall back to the order you wrote
them. Skip groups entirely and just list keywords; that works too.

Grouping never filters anything. Every group is searched, every result is
judged. It only decides reading order — and it tells you which search found a
job, which turns out to be useful on its own.

### 3. Run it

```sh
python3 fetch_jobs.py            # postings from the last 7 days
python3 fetch_jobs.py --days 14  # widen the window
python3 fetch_jobs.py --dry      # search only, don't download anything
```

You get `inbox/_inbox.md` — a skimmable list — plus one file per ad with the
full text.

### What comes out

`_inbox.md` opens with instructions for whatever is going to read it, then the
ads, grouped and in reading order:

````markdown
# Jobs waiting to be judged — updated 2026-03-02 09:04 (3 new this run)

3 waiting, ordered by group (highest-ranked group first).

Skim this list and open the full text only for the ones that look plausible.
[…]
**If nothing is worth applying to, say nothing at all.** Don't report "found
nothing today" — that's noise, and it trains the user to ignore you.

---

# Direct hits

## Analytics Engineer (Remote) — Meridian Health
Germany | 2026-03-01 | Direct hits
**Mid-Senior level | Full-time | €65,000 - €80,000**

> Fully remote within Germany. You will be the second analytics hire, sitting
> between the clinical data team and the product team, and the honest version
> is that the first six months are cleaning up what the contractors left…

Full text: `~/jobs/inbox/2026-03-01_Meridian-Health_Analytics-Engineer_1000002.md`

---

# Safety net

## Business Intelligence Lead — Halberd Group
Munich, Bavaria, Germany | 2026-02-27 | Safety net
**Director | Full-time**

> Leading a team of six across BI and reporting for a portfolio of
> manufacturing businesses. Significant stakeholder management at board level.
> We are looking for someone who has done this before at a company of…
````

The teaser is the first 220 characters of the actual job description, not the
company's own summary line — enough to tell whether opening the full text is
worth it. `Director` is why that last one is at the bottom rather than gone:
LinkedIn's own seniority label sinks an ad, but nothing removes it.

### 4. Get the judgements — 5 minutes, weekly

**If you use a coding agent** (Claude Code, Codex, Cursor…), point it at the
folder and say *"read AGENTS.md and judge what's in the inbox"*. It keeps its
own files locally and you never re-upload anything.

**If you don't**, open any AI chat, upload `me.md` and `inbox/_inbox.md`, and
paste the prompt at the bottom of [AGENTS.md](AGENTS.md).

**Don't buy a subscription for this.** The free chat does the same judging. The
only thing a coding agent buys you is not re-uploading.

### 5. Keep `me.md` alive — this is the part that makes it work

When a judgement gets it wrong, or gets it right in a way that surprised you,
add one line to the bottom of `me.md` **in your own words**:

```
- 2026-08-14 — "stop showing me agency roles, I've done that and hated it"
- 2026-08-16 — "the one about the 4-day week was exactly right, more like that"
```

It gets noticeably better after two or three of these. Most of the value is
here, not in the setup. Your dated reactions beat anything inferrable from the
rest of the file, because they're evidence rather than self-description.

## Where the ads come from — read this before you run it

The search reads LinkedIn's **public** job listings: the same pages anyone sees
without logging in. It never logs in, never touches your account, and can't
apply to anything on your behalf. It waits a second or two between requests and
backs off when LinkedIn asks it to.

If LinkedIn stops answering, the run exits non-zero and puts a warning at the
top of `_inbox.md` telling whatever reads it to break the silence rule and say
so. A blocked search and a quiet day both produce an empty list, and only one
of them is news.

Being straight with you, because you'd find out anyway: **automated reading is
against LinkedIn's terms of use, even for pages that are public.** US courts
have found that reading publicly visible data isn't a computer-crime offence —
but "not illegal" and "permitted by the terms" are different things.
Realistically the worst case here is LinkedIn rate-limiting or temporarily
blocking your IP.

That's a fine trade for one person reading job ads for themselves. It stops
being fine if you run it on a schedule you aren't watching, point it at hundreds
of searches, or republish what it pulls. The defaults are deliberately slow and
capped for that reason; please don't tune them up.

**If that trade isn't for you, don't run it — genuinely.** The script is only
the eyes. All the value is in the judging, and that works exactly the same on
any job board with a real API, or on ads you paste in by hand.

## Your data

Everything stays in the folder. Nothing is uploaded anywhere by the script —
the only network calls it makes are GETs to LinkedIn.

`.gitignore` covers `me.md`, `keywords.txt`, `inbox/`, `judged/`, `verdicts/`,
`seen.json` and `index.json`, so you can safely keep your own fork in git
without committing your job search. Set `JOBHUNT_HOME` to keep the data
somewhere else entirely, or to run several separate searches.

The script prunes after itself: unjudged ads are deleted after 21 days, judged
ones after 30, and sightings are forgotten after 120 days so a repost can
surface again. Unread job ads aren't an archive, they're clutter.

## Tests

```sh
python3 -m unittest discover -s tests
```

No network, no fixtures to download, nothing to install. They cover the config
parser, every case where the script refuses to run, and the blocked-run
behaviour above — including a check that `keywords.example.txt` as shipped
would be rejected, because the version of this that quietly searched the
example's city is the bug worth keeping a test around for.

**Run them before you push a fork.** Three of them are the only check that
your job search isn't about to become public: that nothing tracked contains a
path from your home directory, that every line of the `.gitignore` really
ignores what it says (git only treats `#` as a comment at the *start* of a
line — a trailing one silently turns the rule off), and that nothing gitignored
is already sitting in your history, where ignoring it later changes nothing.

## What it doesn't do yet

Tracking what you applied to and what came back — response rates, which group
actually converts — is still manual. See [ROADMAP.md](ROADMAP.md) for the
design, which is honest about what isn't built.

## Licence

MIT. See [LICENSE](LICENSE).
