# AI Crypto Reply Bot

> An autonomous, AI-powered **reply-guy bot for Crypto Twitter (X)** — powered by
> Claude or OpenAI.

It watches a live tweet feed, scores every tweet deterministically, lets an LLM
(Claude **or** OpenAI) write a witty reply in a persona you control, and posts it
by driving a real logged-in browser session — all wrapped by a supervisor that
restarts on crashes, fixes its own bugs with a coding agent, and tunes itself
from engagement data.

> Repo / package name: **`ai-crypto-reply-bot`**.

> **The model never decides *who* to reply to** — that's done deterministically
> by a scoring engine. The LLM only writes the *text*. That separation is what
> keeps the account on-strategy and the spend predictable.

This is a framework. The default persona is a politically-neutral, generic
"witty reply guy" — **edit `bot/generation/persona.js` to make the character your
own** (a fully-built, opinionated example lives in `examples/persona.example.js`).

---

## ⚠️ Use responsibly

Automating posts and browser-driving a logged-in account can violate the X Terms
of Service and may get accounts suspended. This project is provided for research
and educational purposes. **You are responsible for how you use it** — comply
with X's rules and applicable law, don't spam or harass, and use an account you
can afford to lose. No warranty (see `LICENSE`).

---

## How it works

```
                ┌─────────────── feeds (live tweets) ───────────────┐
   RapidLaunch WSS firehose                       X List poller (optional)
                └───────────────────┬───────────────────────────────┘
                                    ▼
                        decision.js  — score + filter (no LLM)
                                    ▼
                        SQLite candidate queue
                                    ▼
   paced reply loop (~N/hr, jittered)         VIP fast-path (reply instantly)
                                    ▼
              generation/llm.js → provider.js → Claude / OpenAI   (writes the text)
                                    ▼
                        safety checks → browser poster (Playwright)
                                    ▼
                          posted reply  +  engagement tracking
```

- **Two feed sources** (`bot/feed/`): the RapidLaunch WebSocket firehose (broad,
  sub-second) and an optional X List poller (a curated niche list you own). Both
  funnel into one intake.
- **Decision engine** (`bot/decision/`): scores tweets by topic relevance,
  reach, and per-account targeting; protects the account from junk. Recall-
  oriented — the LLM persona is the precision backstop.
- **Generation** (`bot/generation/`): `persona.js` is the character;
  `provider.js` abstracts Anthropic vs OpenAI; `llm.js` builds the prompts.
- **Posting** (`bot/posting/`): a humanized Playwright browser poster that drives
  a pre-captured session (the web app can reply to strangers; the API can't).
  Nothing is sent unless `config.worker.live === true`.
- **State** (`bot/core/db.js`): `node:sqlite` — what it's seen, queued, acted on,
  and every cooldown, so a restart never double-replies.
- **Ops** (`bot/ops/`): the supervisor, the X-API metrics puller, the session
  capture tool, and the coding-agent prompts/runner.

Everything tunable lives in **`bot/config.js`** (heavily commented).

---

## Requirements

- **Node.js ≥ 22.5** (uses the built-in `node:sqlite` and `--env-file`).
- A **RapidLaunch** account for the live feed JWT.
- **One LLM key**: Anthropic *or* OpenAI.
- An X account you log into once to capture a browser session.
- *(Optional)* X API credentials for funnel metrics and the niche-list feed.
- *(Optional)* a coding-agent CLI (`claude` by default) for self-fix/review.

---

## Quick start

```bash
# 1. Install
npm install
npx playwright install chromium

# 2. Configure
cp .env.example .env       # then edit .env (see below)

# 3. Capture a logged-in X session (opens a real browser; you log in by hand)
npm run capture

# 4. Run it. The bot posts LIVE by default.
npm run bot

# 5. For long-running, self-healing operation:
npm run supervise
```

> **Want to try it without posting first?** Set `config.worker.live = false` in
> `bot/config.js` for a **dry run** — the whole pipeline runs and logs what it
> *would* post, but nothing is sent to X. Recommended for your first run.

### Configuring `.env`

The only required values are the RapidLaunch token, your LLM key, and your handle:

```ini
RAPIDLAUNCH_AUTH_TOKEN=...     # rapidlaunch.io → Settings (in your profile)
LLM_PROVIDER=anthropic         # anthropic | openai
LLM_API_KEY=...                # your Anthropic OR OpenAI key (per LLM_PROVIDER)
X_HANDLE=your_handle
```

See `.env.example` for every option (X API metrics, niche-list feed, agent CLI).

### Getting your RapidLaunch token

Log into [rapidlaunch.io](https://rapidlaunch.io), open **Settings** within your
profile, and copy your **auth token**. Paste it as `RAPIDLAUNCH_AUTH_TOKEN`.
RapidLaunch allows only one socket per token, so don't run two feeds on it at once.

---

## Choosing your LLM provider

The bot speaks to either provider through one abstraction (`bot/generation/provider.js`).
Set the provider, then put its key in the **generic `LLM_API_KEY`** var — the same
var works for both, so switching providers is just two lines in `.env`:

| `LLM_PROVIDER` | Default model       | Key var        |
| -------------- | ------------------- | -------------- |
| `anthropic`    | `claude-sonnet-4-6` | `LLM_API_KEY`  |
| `openai`       | `gpt-4o`            | `LLM_API_KEY`  |

Override the model with `LLM_MODEL=...` or in `config.llm`. (If you'd rather use the
SDK-native `ANTHROPIC_API_KEY` / `OPENAI_API_KEY`, those still work as a fallback.)
With no key set, generation is skipped and the rest of the pipeline still runs.

Both providers get vision (the bot sends tweet images to the model). **Web search**
(fact-checking before replying) is currently wired up for Anthropic only; on OpenAI
it's skipped and the persona's grounding rules still prevent fabrication.

---

## Making it yours

1. **Persona** — edit `bot/generation/persona.js` (the `PERSONA` system prompt and
   `FEWSHOT` examples). This is the single most important file. Copy
   `examples/persona.example.js` over it for a ready-made opinionated character,
   or use it as a template.
2. **Stances** — `config.stances` (ally / opponent / neutral playbooks) shape how
   the bot replies to different account types. Rewrite them to match your persona.
3. **Targeting** — `data/targeting.json` ships with a large set of per-account
   profiles (stance, niche relevance) as a starting point. Edit it, trim it, or
   replace it with your own (see `data/targeting.example.json` for the schema).
   It's entirely optional — unknown accounts just get a neutral reply.
4. **VIP fast-path** — `config.vip`: handles whose tweets you want to reply to the
   instant they post (off by default until you fill in `accounts`).
5. **Rate / cadence / scoring** — all in `config.scheduler`, `config.safety`,
   `config.decision`, `config.mix`.

---

## Configuration & tuning

**Everything lives in one file: [`bot/config.js`](bot/config.js).** It's heavily
commented — every knob explains what it does. Edit it directly and restart.

> **The shipped values are sensible defaults that work well.** They're tuned for
> steady, human-looking activity that stays under the radar. You don't need to
> change anything to get started.

⚠️ **Before you turn the dials up, understand the trade-offs.** The defaults are
deliberately conservative. **Raising the activity knobs costs more and raises
risk:**

- **More LLM credits.** Every reply, post, and reply-back is an API call. Raising
  `scheduler.repliesPerHour`, `posting` budgets, or `commentEngage` caps means
  proportionally more spend (and a pricier model like a larger Claude/GPT costs
  more per call than the default).
- **Higher chance of getting flagged/suspended on X.** The more often (and the
  faster/burstier) the account replies, likes, and posts, the more it looks
  automated. Aggressive caps, short cooldowns, and tight spacing are exactly what
  trips X's spam heuristics. **More volume = more risk to the account.**

The main levers, and what raising them does:

| Knob | Default | Raising it… |
| ---- | ------- | ----------- |
| `scheduler.repliesPerHour` | `12` | more replies → more credits + more X risk |
| `safety.maxRepliesPerHour` | `10` | the hard ceiling on paced replies; the safety brake |
| `safety.perAuthorReplyCooldownMs` | `20 min` | lowering it = reply to the same account more often (spammier) |
| `safety.minSecondsBetweenActions` | `20s` | lowering it = burstier, more bot-like |
| `posting.*PerWindow` | `1` orig + `1` quote / 2h | more original posts → more credits |
| `commentEngage.*PerHour` | likes 36 / reply-backs 15 | more thread engagement → more credits + risk |
| `vip.maxPerAuthorPerHour` | `3` | more replies to the same VIP |
| `llm.model` | `claude-sonnet-4-6` | a bigger model = better takes, higher cost |

**Recommendation:** keep the defaults, run for a while, watch `runtime/health.json`
(or let the supervisor's review agent tune within bounds), and only nudge one knob
at a time. Never raise caps to chase volume — that's the fastest way to lose the
account.

---

## The `--fix` flag (self-healing startup)

If the bot hits a runtime error **while starting up**, run it with `--fix` and it
will spawn the configured coding agent to diagnose and repair the code, verify the
tree still parses, and relaunch once:

```bash
npm run bot:fix        # = node --env-file=.env bot/index.js --fix
```

This uses `config.agent` (default: the Anthropic `claude` CLI, run headless with
edit permissions). Point it at another coding-agent CLI with `AGENT_CMD=...` (and
adjust `config.agent.promptFlag`/`args` to match). Steady-state crashes after boot
are handled by the supervisor instead.

---

## The supervisor (`npm run supervise`)

A production wrapper around the bot:

1. **Auto-restart** on transient crashes with backoff.
2. **Self-fix**: if crashes repeat, it spawns the coding agent to find and fix the
   bug (capped per hour), syntax-checks the result, and restarts — or stays down
   and writes `runtime/ALERT.txt` if it can't.
3. **Self-review**: on a cadence (hourly by default) it runs a review agent that
   reads `runtime/health.json` + engagement data and makes **one** bounded,
   evidence-based tuning change (then restarts to apply it).

The agents run with edit permissions but **no shell**; the supervisor does all
process control and syntax verification. They're fenced (never touch `.env`, auth,
or safety caps) via their prompts in `bot/ops/agent-prompts.js`.

---

## Optional: X API metrics & niche feed

Neither is required. With X API credentials in `.env`:

- **Funnel metrics** (`config.metrics`): pulls follower count + impressions +
  profile-clicks (the real follow funnel) so the review agent can optimize for
  *conversions*, not just likes. Tokens auto-refresh into `runtime/x-tokens.json`.
- **Niche-list feed** (`config.listFeed`, off by default): polls an X List you own
  and funnels those tweets into the same intake with a scoring boost — a curated
  stream of exactly the accounts you care about.

---

## Project layout

```
bot/
  config.js              all tunables (start here)
  index.js               orchestrator (intake, reply/post loops, --fix)
  core/      db.js logger.js
  feed/      feedSource.js (RapidLaunch WSS)  listPoller.js (X List)
  decision/  decision.js (scoring)  safety.js (caps)  targeting.js (per-account)
  generation/ persona.js (the character)  provider.js (Anthropic/OpenAI)  llm.js  replyText.js
  posting/   browserPoster.js (Playwright)  worker.js
  ops/       supervisor.mjs  agentRunner.js  agent-prompts.js  xmetrics.js  capture-session.js
data/        targeting.json  targeting.example.json
examples/    persona.example.js
runtime/     review-notes.md (shipped seed) + local state (gitignored)
```

---

## Runtime files & the database

The bot keeps all of its state in the **`runtime/`** folder, created automatically
on first boot. **Everything here is local** and gitignored — *except* the seed
`review-notes.md`, which ships with the repo so the review agent has a starting
memory. None of these files are needed to start; the bot creates what it needs.

| File | Created by | What it is |
| ---- | ---------- | ---------- |
| `bot.db` (+ `-wal`, `-shm`) | the bot | **SQLite database** (`node:sqlite`) — the bot's memory. Tracks every tweet it has *seen*, the *candidate* queue, every *action* taken (with a uniqueness guard so it never double-replies across restarts), *engagement* metrics, follower history, and logs. Delete it to start completely fresh. |
| `review-notes.md` | shipped seed; agent rewrites it | The **review agent's carry-forward memory**. It reads this first each review and overwrites it with a fresh summary. Re-seeded automatically if missing. |
| `experiments.jsonl` | review agent | Append-only ledger of every tuning change the agent has made and whether it helped. |
| `health.json` | the bot | A live snapshot (refreshed each tick): stats, recent replies, recent errors, and — if X-API metrics are on — the follow funnel. This is what the review agent reads. |
| `posted_replies.jsonl` | the bot | Durable append-only log of every reply/post actually sent, with its URL. |
| `x-tokens.json` | the metrics module | Rotating OAuth2 tokens for X-API metrics (auto-refreshed). **Secret.** |
| `crash-report.txt`, `ALERT.txt`, `*-signal.json`, `metrics-*.json` | supervisor | Crash diagnostics, human-attention alerts, and the file handshakes between the supervisor and the bot. |

> **Database engine:** `runtime/bot.db` uses Node's built-in `node:sqlite` (WAL
> mode) — no native build step, no external database to install. It's checkpointed
> and closed cleanly on shutdown.

To wipe all state and start over, stop the bot and delete the `runtime/` folder
(or just `runtime/bot.db*`). It will be rebuilt on the next run.

---

## Safety notes

- **The bot posts live by default.** Set `config.worker.live = false` for a dry
  run (the whole pipeline runs, nothing is sent) while you tune your persona/config.
- Secrets live only in `.env` and `runtime/` — both gitignored. `x-session.json`
  *is* your login; treat it like a password.
- The bot enforces hourly caps, per-author cooldowns, and content filters
  (`config.safety`). Don't weaken these to chase volume — see **Configuration &
  tuning** for why that risks the account.

## License

MIT — see [`LICENSE`](LICENSE).
