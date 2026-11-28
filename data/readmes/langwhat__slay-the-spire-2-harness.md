# STS2 Harness

[中文](README.zh-CN.md)

**A native AI gameplay engine and evaluation harness for Slay the Spire 2** — no screenshots or OCR, no external guide database required, and no save/load. Connect a model API, click your character portrait in-game, and watch the model plan routes, draft cards, and play full runs across all characters, Standard Ascension levels, and Dread mode—with instant manual takeover, live user suggestions, and full offline replay.

## Highlights

- **Clear game state and mechanics instead of opaque descriptions.** The `sts2agent` Mod reads structured public state and real mechanics straight from the running game—enemy patterns, upcoming Boss/Elite rosters, event choices, per-target live card and upgrade previews, and unknown-room odds—so the model understands how cards and fights actually work without relying on screenshots or an external guide database.
- **Strict player-level fairness.** Draw, discard, and exhaust piles are sorted by reference so draw order stays hidden; `Hidden` and `Unknown` enemy intents are masked as `unknown`; invisible powers are excluded; RNG is never advanced; runs play straight through without save/load; and developer checkpoint endpoints are physically disabled in normal gameplay.
- **Native in-game viewing and live interaction.** The top-bar character portrait doubles as a one-click Start/Pause toggle so you can hand off or take back control at any time. Planned routes are drawn directly onto the game map with the native quill pen and smooth auto-centering, card rewards open natively while the model deliberates, grid selections auto-scroll and highlight, and short localized decision reasons float in the top-left margin (auto-hiding over shops and modals). Enable `STS2_USER_INPUT=true` to send live suggestions or chat messages mid-run via a local HTTP queue so the agent can react in upcoming turns.
- **Cache-friendly, framework-free three-role architecture.** Built directly on the official OpenAI and Anthropic SDKs (Responses, Chat Completions, and Messages, preserving native reasoning and thinking blocks end to end). Decisions split by lifetime across **Run** (act-scoped routing, shops, events, rest sites), **Deck** (joint multi-group card drafting with rerolls and deck cycle metrics), and **Combat** (batched card plays and anticipated selections). Deterministic zero-branch steps auto-advance with relic-aware guards and zero model calls; append-only contexts and zero-LLM deterministic compaction achieve **86% prefix cache hit rates** on long runs.
- **Extensible from casual watching to offline research.** Start immediately with a model API and the default minimal mode, or write your own Markdown strategy guides, expose the game as a local HTTP tool API for external agents (such as Claude Code or Codex), swap any role for fixed-code logic, and run offline replays, variant A/B checks, and mid-run takeovers from per-run SQLite archives.

## Results

**All-6-character rotation, Ascension 10, 36 consecutive runs (6 per character): 21 wins, 15 losses (58.3%; Wilson 95% interval 42%–73%), best streak 9 wins.**

All 36 runs used the standalone core (**no external strategy documents or knowledge base, no viewer input**) in the default minimal mode, played from start to the game's own victory or defeat.

| Item | Configuration |
| --- | --- |
| Game | Slay the Spire 2 v0.114.0 (Standard, Ascension 10) |
| Model | `gpt-6.2-astra`, Responses protocol, reasoning effort `xhigh` |
| Mode | Minimal mode (default), no external knowledge base, no viewer input |

| Character | Record | Win rate |
| --- | --- | ---: |
| Defect | 5W – 1L | 83.3% |
| Silent | 4W – 2L | 66.7% |
| Regent | 4W – 2L | 66.7% |
| Necrobinder | 4W – 2L | 66.7% |
| Ironclad | 3W – 3L | 50.0% |
| Fool | 1W – 5L | 16.7% |

- **Median time and usage:** Across all 36 runs, **50.0 minutes**, 6.16M input tokens (5.26M cached; 86.0% overall cache hit rate), and 43.1K output tokens. Across the 21 wins, **56.3 minutes**, 7.17M input tokens (6.15M cached), and 45.3K output tokens.
- **Full records and verification:** Per-run seeds, final floors, defeating encounters, token counts, and version details are in [docs/results.md](docs/results.md). Complete SQLite archives and native `.run` histories for all 36 runs are published in [sts2-harness-runs](https://github.com/langwhat/sts2-harness-runs/tree/main/2026-11-26-rotation-a10).

## Quick start (recommended: model API + default minimal mode)

### Requirements

- Python 3.12+ and [uv](https://docs.astral.sh/uv/).
- **Slay the Spire 2 v0.114.0** on Steam's `public-beta` branch with the [`sts2agent` Mod](mod/README.md) installed. This repository ships no game assemblies; building the Mod from source requires the **.NET 9 SDK** and local game files on Windows, macOS, or Linux (on Windows, run `dotnet build mod/src/Sts2Mod/Sts2Mod.csproj -c Release`).
- A model endpoint speaking **OpenAI Responses**, **Chat Completions**, or **Anthropic Messages** (official or compatible proxy). External driving needs no model credentials.
- Concurrent developer headless runs are macOS only; ordinary GUI play works on Windows, macOS, and Linux.

### Setup and play

```sh
uv sync
cp .env.example .env    # PowerShell: Copy-Item .env.example .env
# Edit .env with your API endpoint, model, and credentials (LLM_PROTOCOL / LLM_BASE_URL / LLM_MODEL / LLM_API_KEY); keep it private.
uv run sts2 check-config
```

Launch the Mod-enabled game, start a run with any character and mode, then run:

```console
uv run sts2 start
```

The backend attaches in Pause; **click your character portrait in the top bar** to hand the run to the model, and click again anytime to pause and take over without losing context. The backend stays resident and handles every new run you start.

### Minimal mode (default) vs full mode

Built-in driving **defaults to minimal mode**, cutting pauses between turns for a faster, smoother watching experience while keeping core decision quality intact (the 36-run Ascension 10 rotation above ran in minimal mode). **Full mode** adds post-battle reviews and cross-node strategy notes, which **may improve win rate** at the cost of extra model calls, longer waits between fights, and slower pacing:

| Capability | Minimal mode (default, `STS2_MINIMAL=true`) | Full mode (`STS2_MINIMAL=false`) |
| --- | --- | --- |
| Core gameplay, 3-role split, joint card drafting & drafting prompts | Included | Included |
| Native mechanism extraction, deck cycle stats, auto-advance, custom guide auto-injection | Included | Included |
| Native catalog lookup (`run_knowledge` / `combat_knowledge`) | Native catalog | Native catalog + external supplements |
| Post-battle reviews, separate Run handoffs, cross-node strategy notes | Skipped (faster pacing) | Enabled (may raise win rate, slower pacing) |
| Extra inspection & skill tools (`*_inspect`, `*_skill`, `run_notes`) | Off | On |

To switch to full mode, set `STS2_MINIMAL=false` in `.env` or override at startup:

```console
uv run sts2 start --set STS2_MINIMAL=false
```

All environment variables, multi-protocol `.env` templates, authentication modes, and context-window compaction rules are documented in [docs/configuration.md](docs/configuration.md); common setup issues (game branch, local proxy bypassing `127.0.0.1`, ports) are covered in [docs/running.md](docs/running.md#troubleshooting).

## Write your own strategy guides

The core ships with no built-in strategy guide library, but provides a full document extension hook. You can author your own Markdown notes covering **card evaluations, relic synergies, enemy nuance, Boss gameplans, or character archetypes** and plug them into the core:

- **Automatic contextual delivery:** matches the current act and visible Bosses on act entry, and matches your deck, relics, potions, enemies, and powers when combat starts (**works in both minimal and full mode**).
- **Per-run dynamic rendering:** tailor advice by ascension level and mode through `MaterialContext`.
- **Measurable impact:** compare runs or frozen decision points before and after adding guides using offline evaluation.

See the [Custom knowledge guide](docs/custom-knowledge.md) for what you can write, when it is delivered, and a minimal working example, and [EXTENSIONS.md](EXTENSIONS.md) for the full provider contract.

## More ways to play

- **External agents (local HTTP tool API).** Run with no model credentials to expose a single-flight local HTTP tool service (default port `17878`), paired with the [play-sts2](skills/play-sts2/SKILL.md) skill and its zero-dependency minimal-delta CLI (`sts2_cli.py`) for Claude Code, Codex, or your own agent:
  ```console
  uv run sts2 start --set STS2_DRIVER=external
  ```
- **Live user input queue.** Set `STS2_USER_INPUT=true` to push live suggestions or viewer messages to `POST http://127.0.0.1:17879/inputs`, queued in order for the active role's next model request (see [docs/running.md](docs/running.md#live-user-input)).
- **Custom strategies / library mode.** Implement the two-method `DecisionSource` protocol to replace Run, Deck, or Combat with fixed-code logic while keeping legality checks, settlement, pause handling, and recording (see [docs/library.md](docs/library.md)).
- **Concurrent headless evaluation (macOS only).** Launch isolated game instances with dedicated profiles, ports, and archives, automatically bypassing GUI pacing delays:
  ```console
  uv run sts2 headless --game /absolute/Game.app/Contents/MacOS/Game \
    --template /absolute/template.manifest.json --character IRONCLAD --ascension 0
  ```

See [docs/running.md](docs/running.md) for startup, live user input, external tools, and headless details. `uv run sts2 --help` lists every command and option.

## Recordings, retrospectives, and offline evaluation

With built-in driving, every run writes its game operations, model exchanges, token/cache usage, and material reads to `runs/<run-directory>/archive.sqlite` (external driving writes diagnostics only). Inspect any archive offline with no game or network:

```sh
uv run sts2 journal --archive runs/<run-directory>/archive.sqlite
```

With `sts2_harness_eval`, you can run software-only offline replays, frozen decision benchmarks, declarative guide-variant comparisons, and mid-run takeovers. See [docs/evaluation.md](docs/evaluation.md) and [docs/gameplay-retrospectives.md](docs/gameplay-retrospectives.md).

## Development

```sh
./scripts/check      # Ruff, strict Pyright, pytest (no game or model needed)
./scripts/check-mod  # Mod offline tests; builds Release Mod when game assemblies are found (use dotnet build on Windows)
```

## Documentation

- [Results](docs/results.md): 36-run rotation breakdown, setup, version history, and archive index.
- [Custom knowledge guide](docs/custom-knowledge.md): authoring your own strategy guides to strengthen gameplay.
- [Architecture](docs/architecture.md): modules, three roles, context projection, and tool protocol.
- [Glossary](GLOSSARY.md): domain terms.
- [Configuration](docs/configuration.md): API protocols, authentication, and minimal vs full mode.
- [Running](docs/running.md): ordinary, live user input, external, and headless startup.
- [Using the core as a library](docs/library.md): model client, SQLite recordings, sessions, and custom roles.
- [Evaluation](docs/evaluation.md): offline replay, takeover, and frozen decision evaluation.
- [Gameplay retrospectives](docs/gameplay-retrospectives.md): reviewing finished runs.
- [Extension interface](EXTENSIONS.md): document provider contract and delivery semantics.
- [Per-run documents](docs/materials.md): building dynamic documents per run.
- [Mod](mod/README.md): the C# game Mod, installation, and native template tools.
- [Contributing](CONTRIBUTING.md).

## Disclaimer

This is an unofficial fan project, not affiliated with or endorsed by Mega Crit. Slay the Spire is a trademark of Mega Crit. This repository contains no game code or assets; you need your own copy of Slay the Spire 2.

## License

[MIT](LICENSE).
