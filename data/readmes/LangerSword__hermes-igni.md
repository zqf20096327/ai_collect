# Igni

**A Witcher-inspired card game plugin for Hermes Agent.** Igni runs two real,
deterministic card games against a hidden-hand opponent, with pixel-art cards
and a rule engine that validates every move. Play from chat, the TUI, or a
clickable desktop table.

[![tests](https://github.com/LangerSword/hermes-igni/actions/workflows/tests.yml/badge.svg)](https://github.com/LangerSword/hermes-igni/actions/workflows/tests.yml)
[![Hermes Catalog PR #159369](https://img.shields.io/badge/Hermes%20Catalog-PR%20%23159369-d97706)](https://github.com/NousResearch/hermes-agent/pull/159369)
[![license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**[60 second demo](https://github.com/LangerSword/hermes-igni/releases/tag/v0.3.1)**: the real table, both games, and the hidden-hand boundary.

![Igni cover: a print artifact with the word IGNI and a fanned pixel hand](docs/cover.png)

## What is Igni?

Igni is an unofficial [Hermes Agent](https://github.com/NousResearch/hermes-agent)
plugin named after the Witcher sign of fire. It ships two complete card games:

- **Gwent**: rows, weather, spies, horns, scorch, best of three.
- **Arena**: 30 health, mana, taunts, charge, divine shield, spells.

The opponent is a local rule-based AI. It sees its own hand and the public
board, never yours. The agent is the referee, not the player: it asks for your
move, relays it exactly, and shows the new board.

No API keys. No network. No model calls. The engine is Python standard library;
the desktop page uses the Hermes plugin SDK.

## Install

Requires Hermes Agent 0.23 or newer. The engine has no third-party runtime
dependencies.

```bash
hermes plugins install LangerSword/hermes-igni
hermes plugins enable igni
hermes table install-widget
```

Open a new Hermes session for the tools. The TUI widget is optional; open it
with `/table-board`. In the desktop app, open **Capabilities → Plugins → Igni**.
The desktop half loads by default; the Python half is gated by `plugins enable`.

From a checkout, replace the first two commands with:

```bash
git clone https://github.com/LangerSword/hermes-igni
cd hermes-igni
python3 scripts/sync_plugin.py
hermes plugins enable igni
hermes table install-widget
```

`table` is the game surface: `table_*` tools, the `/table` command, and
`hermes table`. The plugin name is **Igni**.

## Play

```text
you:    play gwent
hermes: [table_new, board, asks for your move]

you:    play 3
hermes: [table_play, your card, the opponent's reply, new board]
```

Arena moves: `play <hand#>`, `attack <your board#> <enemy board#|hero>`,
`end turn`. Gwent moves: `play <hand#>`, `play <hand#> <row>` for the horn,
`pass`.

Slash commands:

```text
/table                     show the active board
/table rules [mode]        rules and the full card pool
/table new [gwent|arena] [seed]
/table install-widget
```

Desktop:

```text
sidebar: Igni
palette: Igni: open the card table
chip:    🔥 igni
page:    /table
```

![Igni desktop table with pixel-art cards](docs/desktop.png)

CLI, including an AI-vs-AI demo:

```bash
hermes table demo gwent --seed 7
hermes table play arena
python3 table_cli.py demo gwent --seed 7
```

`hermes table` runs when the plugin is loaded in-process. Under
`plugins.isolation: host` the host skips CLI subcommands; use the Python entry
point.

## The two games

### Gwent, best of three

- Rows: melee, ranged, siege.
- Win two rounds. A round ends when both sides pass; a tie awards it to both.
- Weather sets every non-hero unit on one row to 1, for both sides.
- Commander's Horn doubles one row. Clear Weather removes all weather.
- Spies join the enemy row and draw two cards. Scorch destroys the strongest
  non-hero unit(s) on the board, both sides.
- Heroes are immune to weather. Hands carry between rounds; the board clears.

### Arena, a mana duel

- 30 health, mana 1 to 10, refill each turn, draw one.
- Minions have summoning sickness unless they have Charge.
- Taunts must be attacked first; Divine Shield absorbs the first hit.
- Battlecries draw, heal, or damage all enemy minions.
- An empty deck deals rising fatigue damage.

## Art

- **Cover:** a Nous-style print artifact, 1600×900, in `docs/cover.png`. Source:
  `cover/cover.html`, rendered with `python3 scripts/render_cover.py`.
- **Catalog banner:** the 2:1 image the Hermes plugin catalog shows on Igni's card,
  1200×600, in `docs/banner.png`. Source: `cover/catalog.html`, same renderer.
  The catalog spec requires 2:1, so this is its own composition rather than a crop
  of the 16:9 cover.
- **Cards:** 21 WebP files in `art/`, each 256×256 and quantized to 24 colours.
  Pure pixel art, `image-rendering: pixelated`, written for this project.
  Rebuild with `python3 scripts/build_card_art.py`.
- **Desktop:** pixel cards on hard 2 px frames and scanline panels. The TUI
  stays typographic; the board is the art there.

![Twenty-one pixel card archetypes](docs/card-art-grid.png)

## How it works

```text
table_new / table_play
        │
        ▼
   table_engine ──────► table_gwent | table_arena
        │                         │
        │                         ▼
        │                 profile-scoped JSON state
        ├──────────────► hand-free widget snapshot
        └──────────────► /api/plugins/igni (desktop)
```

Four invariants carry the plugin:

1. **The opponent hand never crosses a boundary.** It stays in the engine.
   `public_view`, the widget snapshot and every tool result carry counts only.
2. **The same seed gives the same deal.** The engines are deterministic and the
   AI reads only its own hand plus the public board.
3. **One call resolves both sides.** `table_play` applies your move and the
   opponent's reply before it returns, so a chat turn never ends waiting.
4. **State is profile-scoped and atomic.** One active table per profile, JSON
   written with a temporary file and `os.replace`.

## Verify

```bash
python3 -m unittest discover -s tests -v   # 29 tests
python3 smoke_test.py                      # 40 self-played matches
python3 smoke_load.py                      # real register() + tool dispatch
hermes plugins validate .                  # manifest and capability probe
```

The tests cover deck sizes, scoring, spies, scorch, round ties, mana, taunts,
lethal attacks, AI pass discipline, hidden-hand boundaries, tool errors,
widget install, art coverage, persistence, backend routes, and self-play
termination. The CI badge runs the first three on every push.

## FAQ

**Does Igni need an API key?** No. The engine is local and uses no network.

**Can the agent see my hand?** The opponent cannot. The agent relays your move
and sees the public board; the opponent's hidden hand never enters a tool
result, snapshot, or desktop response.

**Is this an official Witcher game?** No. It is an unaffiliated fan project.
The Witcher and Gwent names belong to CD Projekt Red. The Arena mode, rules
engines, code and pixel art are original.

**Does it work in Discord or Telegram?** The tools work in any Hermes session.
The TUI scoreboard and desktop page are local surfaces.

**Where is the game state?** Under the Hermes plugin data directory, plus a
hand-free scoreboard snapshot at `$HERMES_HOME/igni/board.json`.

## Credits

Built for Hermes Agent. Fonts are under the SIL Open Font License; see
`assets/fonts/README.md` and the `OFL-*.txt` files. Pixel art was generated for
this project and quantized to 24 colours. No assets from a commercial game are
included. Demo music: "Achaidh Cheide" by Kevin MacLeod (incompetech.com),
CC BY 4.0; see `demo/CREDITS.md`.

If Igni earns a spot in your setup, star the repo. That is the whole ask.

## License

MIT. See [LICENSE](LICENSE).
