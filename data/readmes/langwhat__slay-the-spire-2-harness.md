# STS2 Harness

[中文](README.zh-CN.md)

A model-driven player for Slay the Spire 2 that plays one run at a time without save/load.

- **Mod.** The `sts2agent` game Mod exposes the game's public state and actions over local HTTP.
- **Backend.** A Python backend splits decisions between three model roles:
  - Run plans routes, shops, events, and rest sites;
  - Deck picks cards;
  - Combat plays each battle.
- **Recording.** Built-in play records game and model exchanges for offline replay. External driving writes diagnostics only.

You can also plug in your own fixed-code strategy, or drive the game from an outside agent through a local tool API.

## Requirements

- Python 3.12+ and [uv](https://docs.astral.sh/uv/).
- Slay the Spire 2 v0.114.0 on Steam's `public-beta` branch with the
  [`sts2agent` Mod](mod/README.md) installed. Building the Mod needs the .NET 9 SDK
  and local game assemblies.
- A model endpoint using the OpenAI Responses, Chat Completions, or Anthropic Messages
  protocol. External driving needs no model.
- Developer headless runs are macOS only.

## Setup

```sh
uv sync
cp .env.example .env    # PowerShell: Copy-Item .env.example .env
# Edit .env with your model and credentials; keep it private.
uv run sts2 check-config
```

Settings, their precedence, and minimal mode are described in
[docs/configuration.md](docs/configuration.md).

## Play

Start the Mod-enabled game, select a character, then run:

```console
uv run sts2 start
```

The backend connects in Pause; press the in-game Start control to hand the run to the
model. It stays resident and serves each new run you start. To drive the game with your
own agent instead, run `uv run sts2 start --set STS2_DRIVER=external` and use the local
tool API with the [play-sts2](skills/play-sts2/SKILL.md) skill.

To play with the companion knowledge documents, clone [sts2-knowledge](https://github.com/langwhat/sts2-knowledge)
next to this repository and run `uv run sts2-knowledge start` from the knowledge
repository. The standalone `uv run sts2 start` uses the core without those documents.

Developers can launch isolated game instances, each with its own profile, port, and
archive:

```console
uv run sts2 headless --game /absolute/Game.app/Contents/MacOS/Game \
  --template /absolute/template.manifest.json --character IRONCLAD --ascension 0
```

See [docs/running.md](docs/running.md) for startup, live viewer input, external tools,
and headless details. `uv run sts2 --help` lists every command and option.

## Inspect recordings

With the builtin driver, each run writes `archive.sqlite` in its own directory under
`runs/`. The external driver writes diagnostics only. Inspect a builtin recording offline:

```sh
uv run sts2 journal --archive runs/<run-directory>/archive.sqlite
```

More filters and views are listed in [docs/library.md](docs/library.md#recordings).

## Development

```sh
./scripts/check      # Ruff, strict Pyright, pytest (no game or model needed)
./scripts/check-mod  # Mod offline tests; builds the Mod when game assemblies are found
```

## Documentation

- [Architecture](docs/architecture.md): how the core is put together, roles, context, and tools.
- [Glossary](GLOSSARY.md): domain terms.
- [Configuration](docs/configuration.md): settings, authentication, minimal mode.
- [Running](docs/running.md): ordinary, external, and headless startup.
- [Using the core as a library](docs/library.md): model client, recordings, sessions, roles.
- [Evaluation](docs/evaluation.md): offline replay and frozen decision evaluation.
- [Gameplay retrospectives](docs/gameplay-retrospectives.md): reviewing finished runs.
- [Extension documents](EXTENSIONS.md): supplying extra knowledge and guidance.
- [Per-run documents](docs/materials.md): building documents for each run.
- [Mod](mod/README.md): the C# game Mod and native template tools.
- [Contributing](CONTRIBUTING.md).

## Disclaimer

This is an unofficial fan project, not affiliated with or endorsed by Mega Crit. Slay the Spire is a trademark of Mega Crit. This repository contains no game code or assets; you need your own copy of Slay the Spire 2.

## License

[MIT](LICENSE).
