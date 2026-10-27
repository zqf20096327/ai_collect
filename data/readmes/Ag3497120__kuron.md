<div align="center">

# kuron

**Claude acts as the whole app instead of writing it.**<br>
Write an idea, use it by hand within minutes, and when you like it, get a build plan and the prompts to make it for real.

[![GitHub stars](https://img.shields.io/github/stars/Ag3497120/kuron?style=for-the-badge)](https://github.com/Ag3497120/kuron/stargazers)
[![MIT License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)](LICENSE)
[![Try it in your browser](https://img.shields.io/badge/try_it-in_your_browser-6750a4?style=for-the-badge)](https://claude.ai/artifact/UMMbf2FcV3ULi6d5WaW1yp)

**English** · [日本語](README.ja.md) · [中文](README.zh.md)

[![Six app ideas pasted at once: a greenhouse, a food truck, a Mars base, earphones, a wildfire watch and warehouse robots, each running as a whole system](https://kuron.pages.dev/demo-en.gif)](https://kuron.pages.dev/demo-en.mp4)

*Six ideas pasted at once, each running as a whole system. ▶ [Watch the 2-minute video](https://kuron.pages.dev/demo-en.mp4) · [A recorded run with every tool call](https://kuron.pages.dev/#replay)*

### [▶ Open kuron in your browser](https://claude.ai/artifact/UMMbf2FcV3ULi6d5WaW1yp)

No install. It runs on your own claude.ai account.

</div>

---

## Why

I'm a student and a solo developer. AI already makes prototypes many times faster to build, but picturing ideas and market
needs only in your head or in a plan is hard for one person. A mockup doesn't help much: the screens are the easy part, and
what decides whether an idea is useful is the behaviour behind them.

So kuron reverses the order. **Try the idea first, with something that really works, then build it.** The name comes from
the Japanese word 空論 (kūron), "armchair theory".

## How it works

1. **Write the idea** in plain words, in any language. One line is enough; a page is fine.
2. **Use it.** Claude sets up minimal screens for each device or role, then plays everything that normally takes longest
   to build: the backend, the data and the wiring between screens. Every button press is handled by Claude acting as the
   system. No app code is generated.
3. **Reverse it.** When you like what you see, kuron writes a spec from what the system actually did, a schedule, and the
   prompts to give a coding agent to build the same thing. For the clinic in the Japanese video, that came to about 92 hours.

```
idea ─▶ setup (LLM + tools) ─▶ brief · data · screens · timers · checks · existing-tech estimate
                                        │
button / timer / picture / sound ─▶ the LLM acts as the system ─▶ reads what it needs, changes the shared world
                                        │
"this should…" ─▶ the LLM changes its own screens, data and brief
                                        │
                        world.json ◀────┘ ─▶ minimal screens: website, phone, desktop, IoT panel, watch, terminal…
```

## What's inside

- **Many devices, one world.** A reception tablet, a doctor's PC, a patient's phone and a waiting-room board all show the
  same data, so one action shows up everywhere.
- **Change it in words.** "Show why each patient got their urgency" — Claude rewrites its own screens and behaviour.
- **Existing tech switch.** An LLM makes every idea look easy. Claude estimates, for each action, what a version you could
  ship today would use (plain code, a model, an outside service, or not possible yet), how often it would be wrong and how
  slow it would be, and the prototype then behaves that way.
- **Checks.** Scenarios of a person using the system, played on a copy of it and judged.
- **Reverse.** A spec with what the system actually did as golden examples, a schedule, and prompts for a coding agent.
- **Real-world parts.** Test sounds, sound shaping for earphones, speech, drawings, pictures.

## Where it fits

| | UI / app generators (Lovable, v0, Figma Make…) | kuron |
|---|---|---|
| What you get | Screens and application code | Minimal screens; the LLM performs the behaviour live |
| Judgement and back-end logic | Must be coded; prototypes usually fake it | The LLM actually decides (triage, recommendations, routing, estimates) |
| Technology that does not exist yet | Nothing works until it is connected | The LLM plays that part |
| Several roles and devices | Built screen by screen | They share one world |
| Changing it | Edit the code | Say "this should…" |
| Can it really be built? | You find out by building it | Every action is estimated, and the switch lets you feel it |
| What you take away | The code | A spec, golden examples and a build plan with prompts |

**Not a good fit:** production use (an action takes several seconds and a few cents, and results vary slightly), pixel-level
UI design, anything real-time like games, bulk exact data processing.

## Run it on your machine

```bash
npx github:Ag3497120/kuron try
```

This copies the examples into `./kuron-examples` and opens http://127.0.0.1:4870/. You need Node.js 20+ and one of: a
logged-in [Claude Code](https://claude.com/claude-code), an API key from a provider below, or [Ollama](https://ollama.com).

| Model name | Runs on | Needs |
|---|---|---|
| `claude-…` (default) | Claude Code (`claude -p`, tools as an MCP server) | a logged-in Claude Code |
| `anthropic:<model>` | Anthropic API | `ANTHROPIC_API_KEY` |
| `openai:<model>` | OpenAI, or any compatible server via `KURON_OPENAI_BASE_URL` | `OPENAI_API_KEY` |
| `gemini:` · `openrouter:` · `groq:<model>` | that provider's OpenAI-compatible API | `GEMINI_API_KEY` · `OPENROUTER_API_KEY` · `GROQ_API_KEY` |
| `lmstudio:<model>` | LM Studio on this machine | nothing |
| anything else | Ollama on this machine | Ollama |

```bash
kuron try --preset anthropic                                       # Anthropic API
kuron try --compile-model openai:<model> --cpu-model openai:<small> # any provider
kuron dev .                    # every .kuron idea in a folder; "+ New" from one line
kuron new "a clinic that …"    # write an idea and set it up
kuron check idea.kuron         # play the system's checks
kuron hands --url <host>       # the tools as an MCP server, for any MCP client
```

Browser version vs local: the browser version needs nothing but a claude.ai login; it has no microphone and runs timers when
you press them. Its source is in `web/` (`node tools/build-web.mjs`).

## The line

| Code contains | Code never contains |
|---|---|
| Generic tools (store and read data, define screens, notify, sound, speech, drawings, timers, checks, estimates), a shape check on every tool call that answers in words, a minimal renderer | Business judgement, word lists, guessing what the LLM meant, exceptions for one idea |

When something does not fit, a tool tells the LLM what is wrong and the LLM corrects itself. When a prototype behaves
wrongly, you tell it how it should behave. See [docs/DESIGN.md](docs/DESIGN.md).

## Share an idea

kuron needs more ideas to be tested on, especially ones that break it. Add yours as `examples/<name>.kuron` in a pull
request, or open an issue with what worked and what broke (the browser version's **Feedback** button does that for you).
See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT
