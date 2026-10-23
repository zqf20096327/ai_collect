# kuron

**▶ [Try it in your browser](https://claude.ai/artifact/UMMbf2FcV3ULi6d5WaW1yp)** (needs a claude.ai login; it runs on your own account)

**An LLM behaves as the whole system. Code only gives it hands and a minimal face.**

[![An airline disruption desk set up by kuron: departure board, crew tablet, operations, gate agent and passenger phone](https://kuron.pages.dev/demo.gif)](https://kuron.pages.dev/demo.mp4)

▶ **[Watch the 2-minute demo](https://kuron.pages.dev/demo.mp4)**: a real screen recording of the browser version, then the same idea run
through Claude Code step by step. Only the waiting is sped up; every reply is what Claude actually did.
[Recorded run with every tool call](https://kuron.pages.dev/#replay)

**On your machine, one command** (Node.js 20+ and a logged-in [Claude Code](https://claude.com/claude-code), or an API key — see
[Any LLM](#any-llm)):

```bash
npx github:Ag3497120/kuron try
```

It copies the examples into `./kuron-examples` and opens them at http://127.0.0.1:4870/.

*Kūron* (空論) is Japanese for "armchair theory": an idea that only exists on paper. kuron makes such an idea — even one that
would take ~50 hours to build — **appear built within minutes and usable by hand**, so you can judge whether it is worth
building. Nothing is generated per idea: no application code, no grammar to satisfy. An LLM with hands sets the system up
and then *is* the system on every action. Once you have tried it, kuron turns what the system actually did into a
specification and an implementation plan.

```
one line ─▶ setup agent (LLM with hands) ─▶ brief · data · screens · timers · checks · reality estimate
                                                   │
button / timer / camera / sound ─▶ event agent (LLM with hands) ─▶ reads what it needs, changes the world,
                                                   │                speaks, plays, shapes sound, draws
"this should…" ─▶ request agent ─▶ changes its own brief, screens, data, checks
                                                   │
                                   world.json ◀────┘ ─▶ minimal face (website, phone, desktop, IoT, terminal, watch…)
```

See [docs/DESIGN.md](docs/DESIGN.md) for the design and the line the code never crosses.

## Where it fits

UI generators build *the face and the code behind it*. kuron builds *the behaviour*: the face stays minimal, while the
judgement, the data and the hand-offs between roles really work.

| | UI / app generators (Lovable, v0, Figma Make…) | kuron |
|---|---|---|
| What you get | Screens and application code | Minimal screens; the LLM performs the behaviour live |
| Judgement and back-end logic | Must be coded; prototypes usually fake it with fixed data | The LLM actually decides (triage, recommendations, routing, estimates, drafted messages) |
| Integrations and technology that does not exist yet | Nothing works until it is connected | The LLM plays that part convincingly |
| Several roles and devices | Usually built screen by screen | Reception, doctor, patient and a waiting-room display share one world |
| Changing it | Edit the code | Say "this should…"; the LLM changes itself |
| Can it really be built? | You find out by building it | Every intent is estimated as ordinary code / a model / an outside service / not possible yet, and the existing-tech switch lets you feel it |
| What you take away | The code | A spec, golden examples of what the system actually did, and an implementation plan |

**Good uses**

1. **Ideas whose value is a judgement** — triage, recommendations, re-planning deliveries, estimates, follow-up messages.
   An ordinary prototype has the screens but fakes the judgement; here you can find out whether the judgement helps.
2. **Workflows across roles and devices** — run a whole clinic day (reception → interview → doctor → billing → display)
   within minutes and see where people get stuck.
3. **Things that depend on missing technology or integrations** — drug-interaction checks, a camera that judges
   composition, earphones that let only important sounds through: try the experience before building any of it.
4. **Showing an idea and changing it on the spot** — sales, pre-sales, new-business proposals: "Is this what you mean?",
   and the request is applied while you talk.
5. **Deciding whether to build and what will be expensive** — the per-intent estimate shows which parts need a model, a
   service or do not exist yet; if you go ahead, the reverse spec and golden examples go straight to a coding agent.

**Not a good fit**: pixel-level UI design (the face is minimal); production use (about 10 s and some cost per action,
results vary slightly); anything needing instant reaction (games, fine real-time audio control); bulk, exact data processing.

kuron is not a tool for building; it is a tool for finding out, **before building**, whether an idea is useful and what
makes it hard — it sits in front of the tools that write code.

## The line

| Code contains | Code never contains |
|---|---|
| Generic hands: store and read data, define screens, notify, look (camera), listen (mic), play test sounds, shape sound by bands, speak, draw, timers, checks, reality estimate | Business judgement, word lists, guessing what the LLM meant, exceptions for one idea |
| A shape check on every hand's input, answering in words | Rules that patch a prototype's behaviour |
| A minimal generic renderer and the real-world components | |

When something does not fit, the hand tells the LLM and the LLM corrects itself. When a prototype behaves wrongly, you tell
the LLM how it should behave (the request bar), and it changes itself.

## Any LLM

| Turn | `--preset claude` (default) | `--preset anthropic` | `--preset local` |
|---|---|---|---|
| Setup, requests, plans | `claude-sonnet-5-5` via Claude Code, hands as an MCP server | `claude-sonnet-5-5` via the Anthropic API | `qwen3.8:27b-mlx` via Ollama |
| Button presses, timers | `claude-haiku-5-5` | `claude-haiku-5-5` | `qwen3.5:4b` |

Or name any model with a provider prefix; every provider uses the same hands through its own tool calling:

| Name | Runs on | Needs |
|---|---|---|
| `claude-…` | Claude Code (`claude -p`) | a logged-in Claude Code |
| `anthropic:<model>` | Anthropic API | `ANTHROPIC_API_KEY` |
| `openai:<model>` | OpenAI, or any compatible server via `KURON_OPENAI_BASE_URL` | `OPENAI_API_KEY` |
| `gemini:<model>` · `openrouter:<model>` · `groq:<model>` | that provider's OpenAI-compatible API | `GEMINI_API_KEY` · `OPENROUTER_API_KEY` · `GROQ_API_KEY` |
| `lmstudio:<model>` | LM Studio on this machine | nothing |
| anything else | Ollama on this machine | Ollama |

```bash
kuron try --compile-model openai:<model> --cpu-model openai:<smaller model>
```

Any MCP client can use the same hands: `kuron hands --url http://127.0.0.1:4870` (e.g. from Codex).

## Requirements

Node.js 20+ and one of: [Claude Code](https://claude.com/claude-code) (logged in), an API key from a provider above, or
[Ollama](https://ollama.com). No npm dependencies.
The [browser version](https://claude.ai/artifact/UMMbf2FcV3ULi6d5WaW1yp) needs nothing but a claude.ai login (source in `web/`,
built with `node tools/build-web.mjs`); it has no microphone and runs timers when you press them.

## Usage

```bash
kuron try                         # copy the examples into ./kuron-examples and open them
kuron dev .                       # dev UI at http://127.0.0.1:4870/ — every .kuron idea in the folder; "+ New" from one line
kuron new "a clinic that …"       # write the idea and let the setup agent build it
kuron check idea.kuron            # play the system's checks and judge them
kuron hands --url <host>          # the hands as an MCP server
```

A `.kuron` file is just the idea in words ([docs/IDEAS.md](docs/IDEAS.md)). The dev UI shows the running system, the world
(state), every turn with the hands it used and its cost, checks, requests, the reverse plan, and the brief the LLM wrote for
itself. **Ideal / Existing tech** switches the system to behave like a shippable implementation would (delay, sound leaking
past earphones, late or wrong decisions). Presentation mode (`/present`) is for showing it to others and noting requests.

## Measured (M1 Max, Claude preset)

A clinic system — reception tablet, doctor's PC, stock screen, patient phone, waiting-room display; patients, bookings,
reception, interviews, records, prescriptions, stock, billing; two timers:

| | |
|---|---|
| Setup from the idea | 40 s, 14 hands, about $0.39 |
| One event | 7.7–15.4 s, 1–2 hands, $0.04–0.10 |
| A request ("rewrite your checks") | 16 s |

The world given to the LLM on each turn is an overview (counts, properties, latest items), so turns stay about the same size
as the system grows; the LLM reads more only when it needs to.

## Examples

`examples/` holds ideas from small (a task list) to multi-device (an IoT fridge with a phone app, a reception system),
including real-world ones (earphones that let important sounds through, a camera that directs a remote photographer).

## Share an idea

kuron needs more ideas to be tested on, especially ones that break it. Add yours as `examples/<name>.kuron` in a pull
request, or open an issue with what worked and what broke — the browser version's **Feedback** button does that for you.
See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT
