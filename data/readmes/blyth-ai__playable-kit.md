<p align="center">
  <img src="https://raw.githubusercontent.com/blyth-ai/playable-kit/main/docs/banner.jpg" alt="Blyth Playable Kit: make playable mobile games and playable ads with your AI agent" width="100%">
</p>

# Blyth Playable Kit

[![npm](https://img.shields.io/npm/v/@blyth/playable-kit?color=00838a&label=npm)](https://www.npmjs.com/package/@blyth/playable-kit)
[![license](https://img.shields.io/badge/license-PolyForm%20Shield%201.0.0-555)](#license)
[![Blyth Arcade](https://img.shields.io/badge/play-blyth.ai%2Farcade-ff5b22)](https://blyth.ai/arcade)

Make playable mobile games and playable ads with your AI agent.

This is the kit [Blyth Arcade](https://blyth.ai/arcade) runs on: the **Blyth Play Kernel**, build and verify tools, two
reference games and **`SKILL.md`**, the workflow an AI agent follows to turn one sentence into a finished game.
Every game builds into **one self-contained `index.html` under 5 MB** that runs on phones and desktops with no network
connection, so it can go straight to an app store page, a website or an ad network.

## Quick start

```bash
npx -y @blyth/playable-kit my-game
cd my-game
npm install
npx playwright install chromium   # once, for the verify step
```

Build and check one of the reference games:

```bash
node tools/build.mjs examples/runner-3d
node tools/verify.mjs examples/runner-3d/dist/index.html
```

`verify` opens the game in headless Chromium, lets its bot play, and writes `verify.json`, a poster and screenshots next
to the HTML. Open `examples/runner-3d/dist/index.html` in any browser to play it.

Working from a clone of this repository instead? The kit lives in `kit/`: run `cd kit && npm install` and use the same
commands there.

## Make a game with your AI agent

Open the folder in Claude Code, Codex, Cursor or any other coding agent and ask for a game:

> Read SKILL.md and make a 3D runner where a corgi dodges city traffic.

The agent plans the game in `design/plan.json`, writes `game/main.js` against the kernel, then builds, verifies and fixes
it until the checks pass:

```bash
node tools/build.mjs game
node tools/verify.mjs game/dist/index.html
node tools/ad-check.mjs game/dist/index.html   # checks the playable-ad ending
```

`references/` holds the guides the agent reads along the way: game design, genres (runner, crowd, shooter, racing,
puzzle and more), art direction, the ad funnel and a showcase of finished games.

## What is inside

| Path | What it does |
|---|---|
| `kernel/kernel.js` | The Blyth Play Kernel: layout, touch and keyboard input, fixed-step loop, seeded randomness, procedural sound and music, HUD, tutorial hand, end cards, particles and screen shake, tunable params, translations, MRAID and `window.playable` messaging. |
| `tools/build.mjs` | Bundles `main.js` and its images, sounds and 3D models into one HTML file. Fails above 5 MB. |
| `tools/verify.mjs` | 17 checks in headless Chromium: size, params, bot play, frame rate, restart, end card, ad card, console errors, no network requests, landscape. |
| `tools/ad-check.mjs` | Plays the scripted "so close" level the ad version ends on, with three seeds. |
| `examples/runner-3d` | Reference 3D game (three.js): lanes, object pools, a bot, a chasing-boulder near miss. |
| `examples/catcher-2d` | Reference 2D game (Canvas 2D): drag control and a bot. |
| `SKILL.md`, `references/` | The workflow and the design guides for AI agents. |

## Every game is also a playable ad

Each build exposes tunable params (colours, speed, difficulty, texts, store links, call to action) that a marketer can
change without touching code, and an ad mode: three short levels, the last of which ends in a near miss and an install
card. The same file works as a game on the web and as a playable ad.

## Publish to Blyth (optional)

The kit works on its own. To publish games to Blyth Arcade, tune them in the Blyth editor and download them, connect the
Blyth MCP server to your AI app:

- **Claude:** Settings → Connectors → Add custom connector, address `https://mcp.blyth.ai/mcp`
- **Claude Code:** `claude mcp add --transport http blyth https://mcp.blyth.ai/mcp`
- **ChatGPT and other MCP apps:** see [blyth.ai/mcp](https://blyth.ai/mcp)

Then ask your agent to publish the game. It calls `publish_playable` and gives you the editor link. Through the same
connector it can make images, video, 3D models, music and sound effects for the game with your Blyth credits. The
connector is included with the Blyth Starter, Pro and Studio plans.

## License

Source-available under the [PolyForm Shield License 1.0.0](LICENSE), with an additional permission from Blyth AI Inc.
([`NOTICE.md`](NOTICE.md)).

- **You can** use and change the kit, and use, distribute and sell the games and playable ads you make with it, including
  for clients and on any store or ad network. Keep the notice line the build adds to each game.
- **You cannot** offer the kit or the kernel themselves, or a tool or service that lets other people make playable games
  or ads with them, as a product of your own.

This is a summary. `LICENSE` and `NOTICE.md` are the terms.

## Links

[Blyth Arcade](https://blyth.ai/arcade) · [Blyth MCP](https://blyth.ai/mcp) ·
[npm](https://www.npmjs.com/package/@blyth/playable-kit) · [Changelog](CHANGELOG.md) ·
[Issues](https://github.com/blyth-ai/playable-kit/issues)

Copyright (c) 2026 Blyth AI Inc.
