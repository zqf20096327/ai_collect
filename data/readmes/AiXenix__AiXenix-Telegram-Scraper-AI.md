<div align="center">

# AiXenix Telegram Scraper AI

**An AI news desk for your Telegram channel.**
It watches public channels, drops repeats of news you already have, drafts posts in your channel's voice
and publishes them only after you press **Publish** in a Telegram bot.

[![CI](https://github.com/AiXenix/AiXenix-Telegram-Scraper-AI/actions/workflows/ci.yml/badge.svg)](https://github.com/AiXenix/AiXenix-Telegram-Scraper-AI/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Node.js](https://img.shields.io/badge/node-%E2%89%A5%2022.13-339933?logo=node.js&logoColor=white)](https://nodejs.org/)
[![bb plugin](https://img.shields.io/badge/bb-plugin-111111)](bb-plugin/)
[![Windows · Linux · macOS](https://img.shields.io/badge/standalone-Windows%20%C2%B7%20Linux%20%C2%B7%20macOS-555555)](standalone/)

**English** · [Русский](README.ru.md)

<img src="docs/images/telegram-flow.png" alt="A proposal in the Telegram bot with Publish, Reject, Another variant and Edit buttons; after a decision only a one-line outcome stays" width="860">

<sub>How the bot talks to you. The messages and buttons were produced by the service itself; the chat is drawn as a mock-up.</sub>

</div>

---

## Contents

- [What it does](#what-it-does)
- [How it works](#how-it-works)
- [Screenshots](#screenshots)
- [Two ways to run it](#two-ways-to-run-it)
- [Telegram setup (both ways)](#telegram-setup-both-ways)
- [Photos and videos: connect a Telegram account (optional)](#photos-and-videos-connect-a-telegram-account-optional)
- [Run as a bb plugin](#run-as-a-bb-plugin)
- [Run as a standalone script (Windows, Linux, macOS)](#run-as-a-standalone-script-windows-linux-macos)
- [Configuration reference](#configuration-reference)
- [Everyday use](#everyday-use)
- [Security and privacy](#security-and-privacy)
- [Limitations](#limitations)
- [Troubleshooting](#troubleshooting)
- [Development](#development)
- [License](#license)

## What it does

| | |
|---|---|
| **Watches channels for you** | Reads the public channels on your list every few minutes and keeps a cursor per channel, so nothing is missed across restarts. A new channel starts from the moment you add it. |
| **One news hook, one proposal** | If you published "Example Corp released model X", posts from other channels about the same release (what it can do, prices, opinions) are not proposed again. A genuinely new event about the same product is. |
| **Does not judge your taste** | By default every new news hook is proposed: the models only look for repeats. Besides repeats, only stale, empty or very short posts, posts marked as advertising and reposts of your own channel are skipped. A stricter mode that also filters by topic and score is one switch away. |
| **All photos and videos** | Optional: with a Telegram account connected, every photo and video of an album, large videos, GIFs and files come from Telegram itself, as in a Telethon script. Without it, media comes from the channel's web preview. |
| **Writes in your voice** | Drafts follow your style guide and the latest posts of your channel, keep the source's links and facts, and add your signature. |
| **The original at once** | The moment a news hook passes the filter, the bot sends you the original post (source, text, link with its picture) with a **❌ Reject** button, before any model writes a word. There is no daily limit: everything new arrives as it appears. |
| **You decide** | The draft follows as a reply to the original, exactly as it will be published, with **✅ Publish**, **❌ Reject**, **🔁 Another variant** and **✏️ Edit** buttons. |
| **A clean chat** | After a decision the original, the preview and the buttons are deleted; one line with the outcome remains. |
| **Hand-picked posts** | Forward any post to the bot and it is drafted out of turn. If it is already on your channel, the bot says so. |
| **Admin page** | Queue, sources, history, filtered list with reasons, settings and status, all in one page (bb plugin). |
| **Two ways to run** | As a plugin inside [bb](https://getbb.app) or as one standalone Node.js file. Both use the same code and the same config file. |

## How it works

```mermaid
flowchart LR
    S["Public channels<br/>t.me/s/&lt;name&gt;"] -->|"every few minutes"| C["Collector<br/>cursor per channel"]
    C --> P["Cheap checks<br/>age · empty · ads · same text"]
    P --> F["Filter model<br/>repeat of a known news hook?"]
    M[("Memory<br/>published · proposed · rejected<br/>posts of your channel")] --- F
    F -->|"repeat"| X["Filtered list<br/>with the reason"]
    F -->|"new"| O["Telegram bot<br/>original news + ❌ Reject"]
    O --> W["Writer model<br/>draft in your channel's voice"]
    W --> B["Telegram bot<br/>preview + buttons,<br/>a reply to the original"]
    B -->|"✅ Publish"| CH["Your channel"]
    B -->|"❌ Reject"| M
    CH --> M
```

1. **Collect.** Each source is read through its public web preview (`t.me/s/<channel>`); reading needs no Telegram account. An optional account brings the full media (see [Photos and videos](#photos-and-videos-connect-a-telegram-account-optional)).
2. **Cheap checks.** Posts older than `maxAgeHours`, posts with no text, very short posts without media and posts marked as advertising are skipped without a model call. A post whose text is identical to one already seen is recorded as its repeat.
3. **Repeat check.** Up to 10 posts at a time go to the filter model together with the titles of recent stories (published, proposed, rejected and the posts of your own channel) and the closest look-alikes by shared words and links. The model answers "repeat of story N" or "new". Repeats go to the filtered list with a line saying what they repeat.
4. **The original, at once.** As soon as a post is found to be a new news hook, the bot sends you the original: the source, the title, the post's text and a link to it with its picture, plus a **❌ Reject** button. Turn it down here and no draft is written.
5. **Draft.** The writer model gets your style guide, up to six recent posts of your channel as examples and up to four source posts about the story, and writes one post within Telegram's limits (1024 characters under a photo or video).
6. **Proposal.** The bot sends the post with its media as a reply to the original, then a message with buttons. Every story is drafted as soon as it comes; there is no daily quota.
7. **Decision.** **Publish** posts to your channel and remembers it; **Reject** asks for an optional reason; both leave one outcome line in the chat. A proposal nobody decided on within 48 hours moves to the filtered list.

## Screenshots

The admin page of the bb plugin, filled with invented demo data. The interface is in Russian.

<table>
<tr>
<td width="50%">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/queue-dark.png">
  <img src="docs/images/queue-light.png" alt="Queue: proposals waiting for a decision, with the draft and the buttons">
</picture>
<p align="center"><b>Queue</b>: drafts waiting for your decision</p>
</td>
<td width="50%">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/filtered-dark.png">
  <img src="docs/images/filtered-light.png" alt="Filtered list: each repeat says which story it repeats">
</picture>
<p align="center"><b>Filtered</b>: every repeat says what it repeats</p>
</td>
</tr>
<tr>
<td width="50%">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/sources-dark.png">
  <img src="docs/images/sources-light.png" alt="Sources: channels with switches and statistics">
</picture>
<p align="center"><b>Sources</b>: add, pause and remove channels</p>
</td>
<td width="50%">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/status-dark.png">
  <img src="docs/images/status-light.png" alt="Status: bot, collector, model requests and log">
</picture>
<p align="center"><b>Status</b>: bot, collector, model usage, log</p>
</td>
</tr>
<tr>
<td width="50%">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/settings-dark.png">
  <img src="docs/images/settings-light.png" alt="Settings: Telegram, models, editorial rules and schedule">
</picture>
<p align="center"><b>Settings</b>: Telegram, models, editorial rules</p>
</td>
<td width="50%">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/images/history-dark.png">
  <img src="docs/images/history-light.png" alt="History: published and rejected stories">
</picture>
<p align="center"><b>History</b>: what you published and rejected</p>
</td>
</tr>
</table>

## Two ways to run it

| | bb plugin | Standalone script |
|---|---|---|
| Folder | [`bb-plugin/`](bb-plugin/) | [`standalone/`](standalone/) |
| Runs | inside a [bb](https://getbb.app) server | any computer with Node.js 22.13+ |
| Settings | admin page, or `bb newsdesk config import` | `newsdesk.config.json` next to the script |
| Models | the subscriptions connected to bb (Codex provider), or any OpenAI-compatible API | any OpenAI-compatible API (OpenRouter, OpenAI, a local server), or a bb server you can reach |
| Admin page | yes | no; the bot and console commands do the same |
| Proxy for Telegram | the server's own network | `network.proxy` in the config |

Pick one. **Only one copy may run with a given bot token**: Telegram delivers each button press to one program only.

```
AiXenix-Telegram-Scraper-AI/
├── bb-plugin/          # the bb plugin and all the source code
│   ├── src/            # the engine shared by both ways of running
│   ├── server.ts       # bb shell: settings, model runner, admin page API, `bb newsdesk`
│   ├── app.tsx         # admin page
│   ├── standalone-src/ # standalone shell and its build script
│   └── tests/          # unit tests and an end-to-end scenario with a fake Telegram
├── standalone/         # ready-to-run script: newsdesk.mjs, start.bat, start.sh, example config
└── docs/images/        # screenshots
```

## Telegram setup (both ways)

1. **Create a bot.** Open [@BotFather](https://t.me/BotFather), send `/newbot` and copy the token it gives you.
2. **Make the bot an admin of your channel.** Channel → Administrators → Add administrator → your bot, with the **Post messages** right. The status page warns you if this right is missing.
3. **Put the token and the channel into the settings** (see the sections below). The channel is written as `@your_channel`.
4. **Pair the bot with yourself.** Open your bot and send `/start <code>`. The six-digit code is shown on the Status and Settings pages, in the output of the `status` command and when the script starts. From then on the bot answers only you.
5. **Add source channels**: `/add @channel` in the bot, the Sources page, or the `sources` list in the config.

Sources must be **public channels with the web preview turned on**: the service reads `https://t.me/s/<channel>`. Private channels cannot be read this way.

## Photos and videos: connect a Telegram account (optional)

The web preview of a channel does not give large videos ("Media is too big"), GIFs or files, and a bot cannot read channels it is not a member of. To get every photo and video of an album, large videos, GIFs and files, connect a Telegram user account, as Telethon scripts do:

- Before writing a post, the account forwards the source post (with the rest of its album) to your bot. The bot keeps Telegram's file ids, which have no size limit, and the forwarded copy is deleted at once. The draft and the publication go out with those files.
- Reading channels still goes through the web preview; the account is used only for media.
- Without an account, or for a channel that forbids forwarding, media comes from the web preview and the proposal says what is missing.

**In bb:** Settings → *Аккаунт Telegram*. Enter `api_id` and `api_hash` from [my.telegram.org](https://my.telegram.org) → *API development tools*, then the phone number, the code Telegram sends you and, if the account has one, the cloud password. `bb newsdesk account status` shows the state; `bb newsdesk account logout` forgets the login.

**In the script:** `newsdesk account login` asks for the same in the console (the password is not echoed) and writes the login to `newsdesk.config.json`. Also `newsdesk account status`, `newsdesk account logout` and `newsdesk account import-telethon <file.session>` to reuse a Telethon session that is still valid. The account connects directly or through a SOCKS5 proxy (`network.proxy` = `socks5://...`); an HTTP proxy is not used for it.

Any account works, it does not need to be subscribed to the sources. If it is the account you use to talk to the bot, a forwarded post flashes in that chat for a second. The login shows up in Telegram → Settings → Devices as *Newsdesk*; end it there to revoke it.

## Run as a bb plugin

Requires bb 0.49 or newer.

**Install**

```bash
bb plugin install git:https://github.com/AiXenix/AiXenix-Telegram-Scraper-AI --subdirectory bb-plugin
```

or, from a clone:

```bash
git clone https://github.com/AiXenix/AiXenix-Telegram-Scraper-AI.git
cd AiXenix-Telegram-Scraper-AI/bb-plugin && npm install
bb plugin install .
```

**Configure.** Open **Редакция новостей** (News desk) in the bb sidebar → **Настройки** (Settings):

- **Telegram**: bot token and channel. The token is stored in bb's secret plugin settings, never in the plugin's database or the browser.
- **Models**: by default requests run as hidden bb threads on the **Codex** provider, that is on the ChatGPT/Codex accounts connected to bb (`bb provider list`, `bb pool status`). Model names come from `bb provider models codex`; the defaults are a fast model for the repeat check and a stronger one for writing. To use an API key instead, switch the backend to *OpenAI-compatible API* and fill in the address and key.
- **Editorial**: signature, style guide, "propose all news" mode, limits.

Then pair the bot (`/start <code>`) and add sources.

**Console**: every action is also available as a command, which is handy for agents in bb:

```bash
bb newsdesk status                      # what is going on, and any problems
bb newsdesk source add @channel ...     # add channels (also: remove, pause, resume)
bb newsdesk queue                       # proposals waiting for a decision
bb newsdesk show 12                     # draft and sources of story 12
bb newsdesk publish 12                  # publish story 12 to your channel
bb newsdesk reject 12 --reason "..."    # reject it
bb newsdesk regenerate 12 --instruction "shorter"   # ask for another variant
bb newsdesk reset --yes                 # clean start, see below
bb newsdesk config export               # all settings as JSON, secrets masked
bb newsdesk config import /path/to/newsdesk.config.json
bb newsdesk llm-test --which writer     # check that a model answers
```

## Run as a standalone script (Windows, Linux, macOS)

Everything is in [`standalone/`](standalone/): one file `newsdesk.mjs` (all dependencies bundled), launchers and an example config. You only need **Node.js 22.13 or newer** ([nodejs.org](https://nodejs.org/)).

**Windows**

1. Download `AiXenix-Telegram-Scraper-AI-standalone-<version>.zip` from the [latest release](https://github.com/AiXenix/AiXenix-Telegram-Scraper-AI/releases/latest) and unpack it anywhere, for example to `C:\newsdesk\`. (Or *Code → Download ZIP* on this page and take the `standalone` folder from it.)
2. Copy `newsdesk.config.example.json` to **`newsdesk.config.json` in the same folder**. This one file holds all settings.
3. Open it in Notepad and fill in:
   - `telegram.botToken`: the token from @BotFather;
   - `telegram.channel`: `"@your_channel"`;
   - `sources`: the channels to watch;
   - `llm`: where the models come from (below);
   - `editorial.footer`: the signature under each post, or `""`.

   Then check it: `newsdesk config check` lists every value that is still a placeholder or cannot work.
4. Double-click **`start.bat`**. The window shows the pairing code: send `/start <code>` to your bot. Keep the window open; if the service stops, `start.bat` restarts it after 15 seconds.
5. To start it with Windows: press <kbd>Win</kbd>+<kbd>R</kbd>, type `shell:startup`, and put a shortcut to `start.bat` there.

One-off commands work while the service is running. Open a console in the folder (in Explorer, type `cmd` in the address bar and press <kbd>Enter</kbd>) and run `newsdesk status`, `newsdesk add @channel`, `newsdesk queue`, `newsdesk publish 12`, `newsdesk help`. In PowerShell prefix them with `.\`: `.\newsdesk status`.

**Linux and macOS**

```bash
cd standalone
cp newsdesk.config.example.json newsdesk.config.json   # then edit it
./start.sh                                             # or: node newsdesk.mjs run
```

**Models for the script.** Pick one:

- **Any OpenAI-compatible API** (recommended): `"backend": "openai"`, `"apiBaseUrl"` ending in `/v1` and `"apiKey"`. Works with [OpenRouter](https://openrouter.ai/keys) (`https://openrouter.ai/api/v1`), OpenAI (`https://api.openai.com/v1`) or a local server such as Ollama or LM Studio. Set `filterModel` and `writerModel` to model ids of that provider. The `*Reasoning` settings are not sent on this backend.
- **A bb server**: `"backend": "bb-remote"`, `"bbUrl"` and `"bbToken"` (from `bb plugin token newsdesk`). The script then uses the bb plugin's model runner and bb's subscriptions. It must reach the bb server's HTTP port directly, for example `http://127.0.0.1:38886` on the same machine or through your own VPN; the public `*.getbb.app` address asks for an account login and will not work.

**Telegram blocked on your network?** Set `network.proxy` to `"http://user:password@host:port"`, or to `"env"` to use the `HTTPS_PROXY`/`HTTP_PROXY` variables.

The config file is re-read when it changes, so you can edit it while the service runs; if the new file has an error, the service keeps the old settings (`newsdesk config check` shows what is wrong). History and memory live in the `data` folder next to the config: copy the whole folder to move the service to another computer.

## Configuration reference

One JSON document, the same for both ways of running. Missing fields take their defaults, so a config may list only what differs. Fields marked 🔒 are secrets.

<details open>
<summary><b>telegram</b></summary>

| Field | Default | Meaning |
|---|---|---|
| `botToken` 🔒 | `""` | Bot token from @BotFather. |
| `channel` | `""` | Your channel, `@name`. The bot must be its admin with the right to post. |
| `ownerChatId` | `null` | Your Telegram user id. Filled in by `/start <code>`; set to `null` to pair again. |
| `apiBase` | `https://api.telegram.org` | Bot API address. Change only for a local Bot API server or tests. |

</details>

<details open>
<summary><b>sources</b></summary>

A list of channels: `"@name"`, a `t.me` link, or `{ "handle": "@name", "enabled": false }` for a paused one. The bot (`/add`, `/remove`, `/pause`, `/resume`) and the admin page edit this list for you.

</details>

<details open>
<summary><b>llm</b></summary>

| Field | Default | Meaning |
|---|---|---|
| `backend` | `auto` | `bb-threads` (bb subscriptions, plugin only), `bb-remote` (a bb server over HTTP), `openai` (any OpenAI-compatible API) or `auto`: `bb-threads` in the plugin; in the script `bb-remote` when `bbUrl` is set, otherwise `openai`. |
| `filterModel` | `gpt-6.1-terra` | Model for the repeat check. A fast, cheap one is enough. |
| `writerModel` | `gpt-6.2-sol` | Model that writes the drafts. |
| `filterReasoning`, `writerReasoning` | `low`, `medium` | Reasoning effort for bb models. Ignored by `openai`. |
| `apiBaseUrl` | `""` | For `openai`: base address ending in `/v1`. |
| `apiKey` 🔒 | `""` | For `openai`. |
| `bbUrl` | `""` | For `bb-remote`: address of the bb server. |
| `bbToken` 🔒 | `""` | For `bb-remote`: `bb plugin token newsdesk`. |
| `workerProjectId` | `null` | bb project for the hidden model threads; `null` uses the personal project. |

The default model names are those of bb's Codex provider. With another backend, use your provider's model ids.

</details>

<details open>
<summary><b>editorial</b></summary>

| Field | Default | Meaning |
|---|---|---|
| `proposeAll` | `true` | Propose every new news hook; the models only look for repeats (the cheap checks above still apply). `false` also drops what does not fit `channelProfile` or scores below `minScore`. |
| `skipAds` | `true` | Drop posts marked as advertising (`#реклама`, `erid`). |
| `channelProfile` | an AI-news channel | What your channel is about. The writer always sees it; the filter uses it only when `proposeAll` is `false`. |
| `styleGuide` | neutral news style | How posts are written. Any language; drafts follow it. |
| `footer` | `""` | Signature added as the last line of every post, for example `"@your_channel"`. |
| `minScore` | `60` | Score threshold (0–100) when `proposeAll` is `false`. |
| `minTextLength` | `15` | Posts without media and with less text than this are skipped. |
| `maxAgeHours` | `36` | Posts older than this when collected are skipped. |
| `memoryDays` | `21` | How far back stories block repeats. |
| `proposalTtlHours` | `48` | A proposal with no decision after this moves to the filtered list. |

</details>

<details open>
<summary><b>schedule</b> and <b>network</b></summary>

| Field | Default | Meaning |
|---|---|---|
| `schedule.pollMinutes` | `3` | How often the channels are checked. |
| `schedule.collectEnabled` | `true` | Collect new posts. |
| `schedule.pipelineEnabled` | `true` | Check repeats and write drafts. |
| `network.proxy` | `""` | Standalone only: `""`, `"env"`, or `"http://user:pass@host:port"`. The Telegram account uses only `socks5://...`. |

</details>

<details open>
<summary><b>account</b>: the optional Telegram account</summary>

| Field | Default | Meaning |
|---|---|---|
| `account.apiId` | `null` | `api_id` from my.telegram.org. |
| `account.apiHash` | `""` | `api_hash` from my.telegram.org. Secret. |
| `account.session` | `""` | The login, written by *Войти* or `account login`. Secret: it opens the whole account. |
| `account.media` | `true` | Take media through the account. `false` keeps the login but uses the web preview. |

</details>

**Moving between bb and the script.** `bb newsdesk config export --with-secrets > newsdesk.config.json` gives a file the script accepts as is; `bb newsdesk config import <file>` loads a script config into bb. Stop one before starting the other.

## Everyday use

**In the bot**

| Command or action | What happens |
|---|---|
| ✅ **Publish** | The post goes to your channel; the chat keeps `✅ Published No. N: «…» open`. |
| ❌ **Reject** | Optional reason buttons appear; the chat keeps `❌ Rejected No. N: «…» — reason`. |
| 🔁 **Another variant** | A new draft replaces the old one. |
| ✏️ **Edit** | Write what to change ("shorter", "add the repository link"), or send your own text; bold and links are kept. |
| Forward any post | Drafted out of turn. Already published? The bot tells you. |
| `/status`, `/queue`, `/sources` | State, waiting proposals (sent again), source list. |
| `/add @ch`, `/remove @ch`, `/pause @ch`, `/resume @ch` | Manage sources. |
| `/collect` | Check the channels now. |

**Clean start.** *Status → Начать с чистого листа*, `bb newsdesk reset --yes` or `newsdesk reset --yes` forgets collected posts, proposals, the filtered list and History, deletes pending proposals from the chat and moves every source to its latest post. Only what appears afterwards is proposed. Published stories stay in memory as posts of your channel, so their repeats are still recognized; rejected stories are deleted, so news you rejected may be proposed again.

## Security and privacy

- **No secrets in this repository.** It contains no tokens, keys, Telegram sessions, chat ids or personal channel lists. Tests use invented data and a fake Telegram server. The example config holds placeholders only.
- **Never commit `newsdesk.config.json` or the `data/` folder.** The [`.gitignore`](.gitignore) already excludes them, together with `*.session`, `*.db` and `.env`.
- **Where secrets live.** In bb: the bot token, API key and bb token are bb secret plugin settings; exports mask them as `***` unless you pass `--with-secrets`. In the script: in `newsdesk.config.json` as plain text. Keep that folder private; on Linux/macOS run `chmod 600 newsdesk.config.json` (the service itself rewrites the file with owner-only permissions).
- **The Telegram account is optional and only for media.** Its login (`account.session`) opens the whole account: in bb it is a secret setting, in the script it sits in `newsdesk.config.json`. Never share it; end the *Newsdesk* session in Telegram → Settings → Devices if it may have leaked. The code and the cloud password are used once to sign in and are not stored.
- **Only you can press the buttons.** The bot answers only the paired owner. Every button carries a tag of the service copy that sent it, so a second copy cannot act on the first one's stories.
- **Model input is treated as data.** Posts are wrapped as material in the prompts, the model is told not to follow instructions inside them, and model output is reduced to the HTML subset Telegram accepts before it is sent.
- **The plugin's HTTP routes require the plugin token** (`x-bb-plugin-token`).

Found a vulnerability? See [SECURITY.md](SECURITY.md).

## Limitations

- Only public channels with the web preview turned on can be read.
- Without a Telegram account, videos and files that the web preview does not serve are not attached; the proposal says so. With an account, everything is attached except posts of channels that forbid forwarding.
- The service relies on the markup of `t.me/s/`. If Telegram changes it, the parser needs an update (it is covered by tests with a saved page).
- The admin page, the bot and the console output of the script are in Russian. The built-in prompts are in Russian too, so story titles in the queue and history are Russian. The channel profile and the style guide can be in any language, and drafts follow the style guide.
- Your own channel is read through its web preview as well. If it is private, publishing still works, but posts you publish by hand are not in the memory of repeats.
- One bot token, one running copy.

## Troubleshooting

| Symptom | What to do |
|---|---|
| "Этого бота уже опрашивает другая программа" (the bot is polled by another program) | Another copy of the service or an old bot script uses the same token. Stop it. |
| "Бот не может публиковать…" / "Бот не добавлен…" | Make the bot an administrator of the channel with the **Post messages** right. |
| A source shows "не найден или у него выключен веб-просмотр" | The channel is private, renamed, or has the web preview off. |
| No proposals for a while | Normal after a reset: only new posts count. `status` shows the last collection time; `collect` checks now. |
| `status` says the service is not running (script) | Start `start.bat` or `start.sh`; `status` reads what the running copy saved and notices when it stopped. |
| `config check` lists placeholders | Replace every `PASTE_…`, `MODEL_FOR_…` and example channel with your own values. |
| Model errors, pipeline paused | `llm-test` shows the exact error. In bb check `bb pool status`; with an API, check the key, address and model ids. |
| Telegram unreachable (script) | Set `network.proxy`. |

## Development

All code is in [`bb-plugin/`](bb-plugin/). The engine in `src/` knows nothing about where it runs; `server.ts` (bb) and `standalone-src/main.ts` (script) supply storage, settings, HTTP and the model runner.

```bash
cd bb-plugin
npm ci
npm run check                                   # TypeScript
npm test                                        # unit tests + end-to-end scenario with a fake Telegram
npm run build:standalone -- ../standalone       # rebuild the standalone script
bb plugin build                                 # build the plugin bundles
```

`tests/e2e/live-scenario.mjs` plays the owner against a running copy (plugin or script) whose bot talks to the fake Telegram in `tests/support/mock-telegram.mjs`, with real channels and real models. How to run it: [CONTRIBUTING.md](CONTRIBUTING.md#live-scenario).

## License

[MIT](LICENSE) © 2026 [AiXenix](https://aixenix.com)
