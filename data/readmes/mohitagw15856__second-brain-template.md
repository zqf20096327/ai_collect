# 🧠 Second Brain: an Obsidian vault that files itself, from a Telegram bot, maintained by Claude

**A personal knowledge base and life tracker you talk to.** Say *"ate paneer bhurji and 2 rotis"*, *"mandarin for chopsticks"*, *"spent 12 on lunch"*, *"remind me at 6pm to call mum"* in Telegram. The bot understands it with Claude, writes plain markdown into your Obsidian vault, and replies with what changed. Claude Code turns the loose notes and articles into a cross-linked wiki. Git keeps every version. No database, no SaaS, no dashboard you have to feed.

Built on [Andrej Karpathy's LLM Wiki idea](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), extended to cover an actual day: food, gym, money, language learning, reading, people, reminders, lists.

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue)](#quick-start) [![Claude](https://img.shields.io/badge/LLM-Claude-orange)](#how-it-works) [![Obsidian](https://img.shields.io/badge/vault-Obsidian-7c3aed)](#the-vault) [![Telegram Bot](https://img.shields.io/badge/capture-Telegram%20bot-2AABEE)](#what-you-can-say) [![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

> **This is a template.** It ships code, a schema and an empty vault. Your data stays in your own private copy. Use the template as a **private** repo before you type a single meal into it.

---

## Table of contents

- [Why this exists](#why-this-exists)
- [What you can say](#what-you-can-say)
- [What shows up on its own](#what-shows-up-on-its-own)
- [How it works](#how-it-works)
- [Quick start](#quick-start)
- [The vault](#the-vault)
- [Integrations](#integrations)
- [The fun bits](#the-fun-bits)
- [Claude Code commands](#claude-code-commands)
- [FAQ](#faq)
- [Contributing](#contributing)

---

## Why this exists

Most personal knowledge management fails at the same place: **bookkeeping**. Filing, cross-linking, keeping summaries current, updating the habit tracker, logging the meal. Humans abandon it. LLMs don't get bored.

Karpathy's LLM Wiki pattern solves the reading half: the model builds and maintains a wiki so knowledge compounds instead of being re-derived on every question. This repo adds the living half. A **capture layer** (a Telegram bot, plain language, no forms) and a **trackers layer** (markdown tables with fixed headers) sit in front of the wiki, so the compounding starts from your day, not just from articles.

The whole system is one folder of markdown you can open, grep, back up and leave.

## What you can say

No slash commands needed. Every line below is a real exchange.

| You say | What happens |
|---|---|
| `ate paneer bhurji and 2 rotis` or 📷 a plate | kcal, protein, fibre estimated and logged; reply shows progress bars against your targets |
| `mandarin for chopsticks` | 筷子 (kuàizi), example sentence, spoken clip; enters spaced repetition, graded tomorrow with 👍 😐 ❌ buttons |
| `我昨天去健身房，很累。` | corrected, pinyin, feedback |
| `82.3 kg` | weight, 7-day average, sparkline |
| `did Body Pump, burnt 450 cal` · `squat 5x5 80kg` · `ran 5k` | workout logged, gym habit ticked, streak shown |
| `spent 12.50 on lunch at Pret` · 📷 receipt | categorised expense, today and month vs budget; receipts itemised; `paid 300 loan` counts the loan down |
| `goal: save 10k by June` · `budget 1800 a month` | money goals with progress bars and a loan-free date |
| `remind me every weekday at 9am to fill the timesheet` | reminder fires with Done / 10 min / 1 hour buttons (not a calendar event) |
| `dentist tomorrow 3pm` | one-tap **Add to Google Calendar** button |
| `buy milk and eggs` · `create a list called gifts` | shopping and custom checklists, tap to tick |
| `todo call dentist` · `work: finish the deck` · `done deck` | two todo lists, tap to tick |
| paste a URL | article fetched, three takeaways, "why it matters" line, saved to raw, queued for the digest |
| `reading Influence ch 3: reciprocity is the strongest lever` | chapter note under the book's page |
| `wrote 500 words on the LLM wiki article` | writing log, idea moves to drafting |
| `met Sara from Monzo, PM, into onboarding` | person page in the wiki, follow-up reminder in two weeks |
| `bought 400g tofu, frozen peas` · `used up the rice` | kitchen inventory by fridge / freezer / cupboard |
| `plan my meals, no mushrooms` | a week of meals from your inventory, recipes written, only the gaps go on the shopping list, 2-hour prep sequence |
| `cooking chana masala` | step by step with Next / Timer / Finish; Finish deducts ingredients |
| 🎙 a voice note about your day | transcribed locally; becomes three journal lines and a mood score |
| 📷 a menu or sign in Chinese | read, translated, two words added to your deck |
| `find the whiteboard photo from Tuesday` | every photo is captioned on arrival and searchable |
| `what's on my reading list?` | answered from the vault |
| `duolingo 45 xp, streak 120` | logged; chess ratings sync themselves |

## What shows up on its own

| When | What |
|---|---|
| 07:30 | An **image card** (habit rings, weight, last night's sleep and readiness, money, calendar), then the digest: five new words plus due reviews with grade buttons, five reads ranked against your current ideas, missed habits, todos, one nudge. Readiness under 50 gets "go light today". |
| 15:00 | Protein check if you're under half target, with a snack idea from the pantry |
| 21:00 | Evening check-in with habit buttons; after two short nights, a 22:30 wind-down instead |
| Monday | A sentence challenge in your target language |
| Friday | Drafts untouched for a week, and an offer to outline a post when three articles share a tag |
| Sunday | Three non-obvious **connections** between the week's captures (tap to keep in the wiki), then a weekly review with charts and a one-page PDF |
| 1st of the month | A memory page in the wiki with a meal-photo grid, a subscriptions radar, a money forecast |
| Daily | Goodreads shelves, Oura, Google Calendar, Chess.com and Lichess imports |

## How it works

```
📱 Telegram ──messages──▶ 🤖 bot (Python)  ──writes──▶ 📁 vault/ (markdown)  ◀──renders── 🟣 Obsidian
                              │  asks Claude for                │
                              │  intent + typed JSON            ├──▶ 🟠 Claude Code: /ingest /query /lint
                              └── serves the Mini App           └──▶ git: commit per capture, push every 30 min
```

- **Bot** (`bot/`): python-telegram-bot, Claude API with structured outputs. One small typed call per capture: intent first, then the specific parser. Everything degrades gracefully without an API key (captures still land, blanks get filled later).
- **Vault** (`vault/`): `inbox/` captures, `raw/` immutable sources, `life/` trackers, `wiki/` synthesis, `daily/` notes, `index.md`, `log.md`. Trackers are tables with **fixed headers** so the bot, Obsidian's Dataview and Claude Code all parse the same thing.
- **Schema** (`CLAUDE.md`): the contract that makes Claude a disciplined wiki maintainer. Edit it and the next `/ingest` follows the new rules. `AGENTS.md` points at it for other agents.
- **Offline-safe**: messages sent while the machine was asleep are filed under the time you sent them; pushes retry every 30 minutes.

## Quick start

1. **Use this template → make the new repo private.** Clone it.
2. **Vault:** open `vault/` in Obsidian. Install the Dataview plugin and the Web Clipper extension.
3. **Bot:**
   ```bash
   cd bot && cp .env.example .env
   # fill TELEGRAM_BOT_TOKEN (@BotFather), TELEGRAM_OWNER_ID (@userinfobot), VAULT_PATH, ANTHROPIC_API_KEY
   uv venv --python 3.12 && uv pip install -e . && .venv/bin/python bot.py
   ```
   Send `/help` to your bot. The bottom keyboard appears.
4. **Run it in the background.** macOS: edit paths in `bot/deploy/*.plist`, copy to `~/Library/LaunchAgents/`, `launchctl load`. Linux / VPS: `bot/deploy/second-brain-bot.service` and `bot/deploy/crontab`.
5. **Make it yours.** The "About the owner" paragraph in `CLAUDE.md`, habits in `vault/life/health/habits.md`, nutrition targets in `vault/life/food/targets.md`, RSS feeds in `bot/feeds.yml`, currency and times in `.env`.
6. **Optional:** `brew install cloudflared` for the Mini App dashboard; Oura, Goodreads, calendar, chess and bank details in `.env` (each line there says where to get the value).

`CHEATSHEET.md` lists everything you can say and every command.

## The vault

```
vault/
├── inbox/        captures by day, filed by /ingest
├── raw/          articles, book notes, photos — never edited
├── wiki/         sources · concepts · entities (incl. people) · syntheses (monthly memory, connections)
├── life/
│   ├── food/     log/ · pantry.md · targets.md · recipes/ · meal-plan.md
│   ├── health/   weight.md · metrics.md · habits.md · workouts.md · oura/
│   ├── money/    expenses.md · goals.md · receipts/
│   ├── mandarin/ words.md · challenges.md          (swap for any language)
│   ├── reading/  books.md · articles.md · books/<title>.md
│   ├── writing/  article-ideas.md · log.md · drafts/
│   ├── todos/ · lists/ · goals.md · reminders.md · journal/ · photos.md · games/
├── daily/        one note per day · weekly-YYYY-Www.md
├── index.md      catalog          log.md   what happened when
```

## Integrations

| Service | How | Auth |
|---|---|---|
| Claude API | intent routing, nutrition, summaries, reviews, plans | `ANTHROPIC_API_KEY` |
| Oura | sleep, readiness, HRV, steps every morning | OAuth2, one-time browser consent (`scripts/oura_auth.py`) |
| Google Calendar | today's agenda in the digest; add events with a one-tap link | secret iCal URL, no OAuth |
| Goodreads | to-read / reading / read shelves | public shelf RSS, paginated |
| Chess.com, Lichess | ratings with sparklines | public APIs |
| Starling, Monzo | card transactions categorised every 15 min | personal tokens (optional) |
| Apple Watch / Apple Pay | steps and sleep, tap-to-pay expenses | iOS Shortcuts recipes in the docs |
| Duolingo | streak and XP | manual capture, or unofficial session-token sync |
| Discord | copies of the digest and weekly review | webhook |
| Email | weekly PDF | SMTP (optional) |

## The fun bits

- **Neuro**, a brain-blob mascot drawn with Pillow in six moods, turned into a Telegram sticker pack by the bot itself. Shows up for nudges and wins.
- A **pinned "Today" message** at the top of the chat that edits itself after every capture.
- Full-screen 🎉 on streak milestones, a 🎰 slot machine on a perfect habit day, XP, levels and badges stored in the vault.
- Quick-repeat buttons under meals and expenses. Reactions on your messages.
- A **Mini App dashboard** inside Telegram: the mascot reacting to your day, habit rings, sparklines, flip cards for words, a wall of meal photos. Served by the bot through a Cloudflare quick tunnel; every request is checked against Telegram's signature.

[Add a screenshot of the morning card and the Mini App here.]

## Claude Code commands

Open the repo folder in Claude Code.

| Command | Does |
|---|---|
| `/ingest` | files every unprocessed inbox line into the right tracker, fills gaps, logs |
| `/ingest <url or raw file>` | compiles a source into the wiki: source page + concept and entity pages + index |
| `/query <question>` | answers with `[[citations]]`; files good answers under `wiki/syntheses/` |
| `/weekly` · `/morning` · `/mealplan` · `/lint` · `/newsletter` | deeper versions of what the bot does |

## FAQ

**Is my data sent anywhere?** Message text and photos go to the Claude API for one answer each. The vault goes wherever you push it (use a private repo). Nothing else, except the services you connect.

**Can someone else use my bot?** No. Only your Telegram user id is accepted; everyone else is ignored silently.

**Does it need to run 24/7?** It runs wherever Python runs. On a laptop, Telegram holds messages for 24 hours while it sleeps and the bot files them under the time you sent them. A small VPS removes even that gap.

**What does it cost?** Telegram is free. Claude API usage at a normal personal volume is a few cents a day. Whisper runs locally.

**I don't learn Mandarin / lift / track money.** Delete those trackers, or leave them empty. Nothing breaks. The language features work for any language once you change the prompts in `bot/llm.py`.

**Can I use another LLM?** The Claude calls are isolated in `bot/llm.py` and use structured outputs. Swapping providers is a one-file job if yours supports JSON schemas.

**Why markdown and not a database?** So you can read it in ten years with any editor, diff it, grep it, and let three different tools (the bot, Obsidian, Claude Code) trust the same file.

## Contributing

Issues and pull requests welcome, especially: new integrations, other languages for the vocabulary features, a Linux TTS path, and Obsidian Dataview dashboards for the trackers. Keep personal data out of examples.

---

*Keywords, for the search engines and the curious: second brain, personal knowledge management, PKM, Obsidian vault, Telegram bot, Claude, Claude Code, LLM wiki, Zettelkasten alternative, habit tracker, spaced repetition, meal tracking, expense tracker, Oura, quantified self, markdown, local-first.*

MIT licensed. Built with Claude Code.
