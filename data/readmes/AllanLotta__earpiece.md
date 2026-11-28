<div align="center">

# 🎧 Earpiece

### The AI earpiece for your calls.

**Someone asks you a question. The answer is already on your screen.**

Earpiece listens to your calls on your Mac, transcribes them on-device, notices when a question is aimed at you
and writes the answer before you need it, in the notch, right under your camera. No bot joins the meeting. No API keys.
The AI is the Claude plan you already pay for.

An open-source, local-first alternative to Cluely, Granola and Otter.

[![CI](https://github.com/AllanLotta/earpiece/actions/workflows/ci.yml/badge.svg)](https://github.com/AllanLotta/earpiece/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/AllanLotta/earpiece?color=7c5cff)](https://github.com/AllanLotta/earpiece/releases/latest)
![macOS 26+](https://img.shields.io/badge/macOS-26%2B-black?logo=apple)
![Swift 6](https://img.shields.io/badge/Swift-6-F05138?logo=swift&logoColor=white)
![Node 22](https://img.shields.io/badge/Node-22-5FA04E?logo=nodedotjs&logoColor=white)
![Zero dependencies](https://img.shields.io/badge/server%20deps-0-success)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Mentioned in Awesome Mac](https://awesome.re/mentioned-badge-flat.svg)](https://github.com/jaywcjlove/awesome-mac#audio-record-and-process)

<img src="docs/images/demo.gif" alt="Earpiece answering questions live during a call" width="880">

<sub>A fictional sprint call. Every card above was written live by Claude while the meeting played.</sub>

</div>

---

## Try it in 2 minutes

Grab the zip from the [latest release](https://github.com/AllanLotta/earpiece/releases/latest): the app is prebuilt,
signed with a Developer ID and **notarized by Apple**, so there's nothing to compile.

```bash
unzip Earpiece-0.1.0-macos.zip && cd Earpiece-0.1.0
./install.sh        # links the `earpiece` command
earpiece setup      # your name and what you do, so answers sound like you
earpiece demo       # a sample meeting in your browser, no permissions needed
```

Prefer to build it yourself? `git clone https://github.com/AllanLotta/earpiece.git && cd earpiece && ./install.sh`
(needs Xcode 26 / Swift 6.1+).

`install.sh` links `earpiece` into `~/.local/bin`; if your shell can't find it, add that folder to your PATH: `export PATH="$HOME/.local/bin:$PATH"` (in `~/.zshrc`).

Then, on a real call:

```bash
earpiece start --title "Sprint planning" --with "Maya, Diego"
# ...talk...
earpiece stop       # writes the transcript + recap as Markdown
```

You need **macOS 26+** (Apple silicon recommended), **Node 22.7+** and
**[Claude Code](https://docs.claude.com/en/docs/claude-code)** logged in with your Claude plan (run `claude` once).

## Why

Every meeting assistant out there either sends a bot into your call, uploads your audio to someone's cloud, or wants
another monthly subscription. Most of them only give you notes *after* the meeting, when it's too late to sound smart.

Earpiece is the opposite, and it's open source (MIT), so you can read every line that touches your audio:

- ⚡ **Real time, not after the fact.** It catches the question while it's being asked and has a script ready by the
  time they stop talking. The fast lane starts answering in **under a second**.
- 🔌 **No bot, no integration, no invite.** It listens to your mic and your Mac's audio output, so it works with any
  call app, any browser, any phone bridge. Nothing to install on the other side.
- 🔒 **Local first.** Speech-to-text, speaker diarization and voice recognition all run **on-device**. Only the
  transcript text goes to Claude, through the Claude Code CLI you already use.
- 💸 **Uses the plan you already have.** It drives `claude` with your Claude subscription and strips API keys on
  purpose, so it never falls back to metered billing.
- 🧠 **Knows your context.** Point it at a folder of your own notes and the deep lane reads them mid-call
  to answer "what did we decide about X?" with your facts, not guesses.
- 🫥 **Stays out of your screen share.** The panel, the notch island and the menu bar icon are hidden from screen
  sharing by default (`--share-panel` to show them).
- 🧾 **Your data, plain files.** Every call becomes a Markdown transcript with a final recap (summary, decisions, your
  action items, open questions), next to a raw `.jsonl`.

## What it does

| | |
|---|---|
| ❓ **Question radar** | Spots questions and requests aimed at you ("Jordan, can you...?", "what do you think?") and answers automatically |
| 🎯 **Answers you can read out loud** | First line is the exact words to say, then the supporting points. Short, natural, in your voice |
| 🫣 **"Stuck" rescue** | Start with "um, so..." after a question and it quietly offers the answer |
| 🏝️ **Notch island** | The answer appears in the notch, right below your camera, so your eyes never leave the call |
| 🔘 **8 one-key buttons** | Answer · What do I say? · Follow-ups · Recap · Explain · Context · Go deeper · My tasks (keys <kbd>1</kbd>–<kbd>8</kbd>) |
| 🗣️ **Who said what** | Live speaker diarization. Name a voice once and Earpiece recognizes it on the next call |
| 🎧 **Works without headphones** | A two-stage echo filter (audio + text) keeps the other side's voice out of your transcript |
| 📖 **Gets names right** | A vocabulary of people and jargon, checked against the audio, so "Myah" becomes Maya and "react query" stays React Query |
| 🌍 **Your language, too** | Transcribe English or other locales (`--locale pt-BR`), and add a one-line note in your native language under each answer |
| ✍️ **Ask anything** | Type a question in the panel mid-call; it answers with everything said so far |
| 🧾 **Meeting memory** | Markdown transcript + final recap for every call, in `~/Documents/Earpiece` |

## How it works

```
  your mic ─┐
            ├─▶ Earpiece.app (Swift, on-device)
 call audio ┘     speech-to-text · echo gate · speaker diarization · voice memory
                        │
                        │  JSONL over 127.0.0.1
                        ▼
                  server (Node, zero deps)
                    turns · question detection · yes/no gate
                        │
             ┌──────────┴───────────┐
             ▼                      ▼
     fast lane (Haiku)      deep lane (Sonnet)
     first words < 1 s      reads your notes folder
             └──────────┬───────────┘
                        ▼
        cards ─▶ notch island + web panel (localhost)
        call  ─▶ ~/Documents/Earpiece/*.md (transcript + recap)
```

- **`app/`**: a menu bar app in Swift. Captures your microphone and the system audio, transcribes both streams with
  Apple's on-device speech APIs, removes echo, tells speakers apart, and streams everything to the local server.
- **`server/`**: plain Node 22, **zero dependencies, no build step**. Assembles turns, detects questions, keeps a few
  warm `claude -p` workers, and serves the panel over HTTP/SSE on localhost only.
- **`bin/earpiece`**: the CLI that starts and stops both.

The full tour is in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Make it yours

`earpiece setup` writes `~/.earpiece/config.json`. The fields that matter most:

```jsonc
{
  "profile": {
    "name": "Jordan Lee",
    "about": "Senior mobile engineer on the payments team. React Native, TypeScript. New on the team.",
    "assistLanguage": "Portuguese",   // optional: one short line in your language under each answer
    "recapLanguage": "English"
  },
  "notes": { "root": "~/notes/work" }, // optional: the deep lane can read this folder
  "answerStyle": "script"              // script | bullets | both
}
```

Names and jargon go in `~/.earpiece/vocab.json` (hot-reloaded during the call). Every key is documented in
[docs/CONFIGURATION.md](docs/CONFIGURATION.md).

## Commands

| | |
|---|---|
| `earpiece setup` | Your profile, plus a checklist of requirements (Node, Claude Code login, macOS, app build) |
| `earpiece start [--title] [--with "Maya, Diego"] [--type planning] [--locale en-US] [--record] [--share-panel]` | Start a meeting: app + server + panel |
| `earpiece stop` | End the meeting, write the recap, stop everything |
| `earpiece status` | What's running, the current meeting, AI login state |
| `earpiece demo [--speed 2]` | Replay a sample meeting through the real pipeline (no mic, no permissions) |
| `earpiece logs [-f]` | Server log |
| `earpiece selftest` | Checks microphone and system audio permissions |

## Privacy

Audio never leaves your Mac. Transcription, diarization and the voice bank run on-device; the voice bank is stored
with mode `600` in `~/.earpiece` and never in your calls folder. The transcript text is sent to Claude through Claude
Code to write the answers, under your own Claude account. Nothing else is sent anywhere: no telemetry, no analytics,
and the server only listens on `127.0.0.1`.

Audio recording is off by default: nothing is kept but the transcript. `earpiece start --record` records one call
(it sharpens the speaker names in the final transcript), and `"record": { "enabled": true }` in
`~/.earpiece/config.json` records every call.

Recording laws differ between countries and states. Make sure the people you record are fine with it.
Details in [docs/PRIVACY.md](docs/PRIVACY.md).

## FAQ

**Does it work with my call app?** Yes. Earpiece doesn't integrate with any call app. It listens to your Mac's audio,
so if you can hear it, Earpiece can.

**Do I need headphones?** No, but they help. Without them, the echo filter removes the other side's voice from your
microphone stream.

**How much of my Claude plan does it use?** It sends text only, a few requests per question. A one-hour call is in
the same range as an hour of normal Claude Code use.

**Intel Macs?** Untested. Everything is built and tuned on Apple silicon, where the on-device models run on the Neural
Engine.

**Windows or Linux?** Not today. The capture app relies on macOS APIs. The server is portable, and a capture app for
another OS only has to speak the [JSONL protocol](docs/ARCHITECTURE.md#wire-protocol-app---server).

## Contributing

Issues and PRs welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) first. The server has no dependencies, and the tests run
with a fake Claude, so `node --test server/test/*.test.mjs` works offline and costs nothing.

## Credits

Speaker diarization, voice embeddings and the audio vocabulary check use
[FluidAudio](https://github.com/FluidInference/FluidAudio) (Apache 2.0) and the open models it downloads on first use.
The English word list in `app/Resources` is derived from [wordfreq](https://github.com/rspeer/wordfreq) (CC BY-SA 4.0).

## License

[MIT](LICENSE) © Allan Lotta
