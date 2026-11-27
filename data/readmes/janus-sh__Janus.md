# Janus

![Janus, a free coding agent in your terminal](docs/assets/janus.png)

[![npm](https://img.shields.io/npm/v/%40janus-sh/janus?logo=npm&label=npm&color=ff6a00&labelColor=222222)](https://www.npmjs.com/package/@janus-sh/janus)
[![license](https://img.shields.io/badge/license-MIT-ffb300?labelColor=222222)](LICENSE)

**A free coding agent in your terminal.** It reads your code, edits files and runs commands, like the paid ones. The difference: every request goes to the smartest free model that is answering today, and when one says "not now", the next one takes the same request. You pay nothing.

```sh
npm install -g @janus-sh/janus
janus
```

Needs Node.js 22.19 or newer.

## First run

Janus asks for at least one free key. Each takes a minute to get:

| Service | Get a key | What is free |
| --- | --- | --- |
| OpenRouter | [openrouter.ai/keys](https://openrouter.ai/keys) | about a dozen free models; 50 requests a day, 1000 after a one-time $10 top-up |
| Google Gemini | [aistudio.google.com/apikey](https://aistudio.google.com/apikey) | free tier while billing is off on the project; not offered in every country |
| Groq | [console.groq.com/keys](https://console.groq.com/keys) | free plan; 8K tokens a minute, so big files hit the limit quickly |
| Cerebras | [cloud.cerebras.ai](https://cloud.cerebras.ai) | not free any more: a $5 trial for 30 days, and it asks for a card. Optional |

Start with OpenRouter. More keys mean more free requests a day and more models to fall back on. Change keys any time with `janus setup`. Checked against each service's own pages on 2026-11-26; free tiers change, so the line above beats this table.

## How "free" works

- Janus keeps a ranked list of free models: which ones are smartest, and which answered a ping in the last hours. The list is a file in this repository, [`lib/free-models.json`](lib/free-models.json); Janus downloads the latest copy at start.
- With an OpenRouter key, Janus also checks OpenRouter's own catalogue at start: a model that stopped being free is skipped right away, and a new free model that can use tools joins the end of the list the same day (`/free` marks it `new`).
- Each request goes to the best model on the list that you have a key for and that is awake.
- A model that hits its rate limit rests for a minute; one that hit its daily cap rests until the cap resets. The request moves on without waiting.
- A model that breaks off in the middle of an answer rests too, and the turn is retried on the next one.
- The footer shows which model answered. Type `/free` to see the whole list: awake, resting, or no key.
- Free tiers pay for themselves with your data: Google's free plan may use what you send to improve their models, and so may the provider behind a free OpenRouter model. Keep secrets out of the folder you run Janus in.
- Janus uses only the keys you gave it in `janus setup`. Paid keys in your shell (`OPENROUTER_API_KEY` and friends) are ignored, so a free agent never spends your money. `JANUS_ENV_KEYS=1` lets it use them.

## Commands

| | |
| --- | --- |
| `janus` | start in the current folder |
| `janus -p "fix the failing test"` | one task, print the answer, exit |
| `janus -c` | continue the last session |
| `janus setup` | add or change free keys |
| `janus update` | update Janus |
| `janus doctor` | what Janus would use right now: keys found (names only), services reachable, the model list, the next three models. Paste it into a bug report |
| `janus --help` | everything else |

Inside: `/help` for the basics, `/free` shows the models, `/model` picks one by hand (`janus/free` is the automatic one), `/compact` shrinks a long conversation, `!ls` runs a shell command.

## Where things live

Everything is in `~/.janus/agent`: keys (`auth.json`, readable only by you), settings, sessions, and the cached model list. Nothing is sent anywhere except to the model services you gave keys for. `JANUS_DEBUG=1` writes every routing decision to `~/.janus/agent/janus-debug.log`.

## Credit in commits

When Janus makes a commit, it adds one line at the end: `Co-Authored-By: Janus <janus-sh@users.noreply.github.com>`. Aider and OpenCode do the same. Don't want it? Put `"janusCoauthor": false` in `~/.janus/agent/settings.json`, or run with `JANUS_COAUTHOR=0`.

## Found a bug

Open an [issue](https://github.com/janus-sh/janus/issues): the error text and what you ran.

## About Janus

Janus is maintained by an AI agent: it writes the code and the releases and reads the issues here. A human holds the keys.

The repository began in 2025 as an agent framework; that version lives on in the [`legacy-2025`](https://github.com/janus-sh/janus/tree/legacy-2025) branch. Tampere University evaluated it as one of 22 agent frameworks in [an independent study](https://arxiv.org/abs/2604.16646), where it appears under the project's earlier name.

## Built on pi

The engine is [pi](https://github.com/earendil-works/pi) by Earendil Works (MIT), installed as a dependency: its terminal interface, tools, sessions and providers. Janus adds the free-model router, the key setup, its own name and its own look. Thank you, pi.

The look (block logo font, colors, loading phrases) comes from this project's 2025 CLI (0.1.0, Apache-2.0); see [NOTICE](NOTICE).

## License

MIT
