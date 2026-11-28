<p align="center"><img src="brand/promo/hero.png" alt="Cubit: Minecraft bots that fight, mine, chop and stay online, run from a web panel" width="100%"></p>

<h1 align="center">Cubit</h1>

<h3 align="center">Ready-to-use Minecraft bots that do the work for you.</h3>

<p align="center">They fight, mine, chop and stay online 24/7, controlled from a web panel in your browser.<br>One ~20 MB binary. No coding, no cloud, no API keys.</p>

<p align="center">
  <a href="https://github.com/bl4tcz/cubit/actions/workflows/ci.yml"><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/bl4tcz/cubit/ci.yml?branch=main&style=flat-square&label=CI"></a>
  <a href="https://github.com/bl4tcz/cubit/releases/latest"><img alt="Latest release" src="https://img.shields.io/github/v/release/bl4tcz/cubit?style=flat-square"></a>
  <img alt="Go version" src="https://img.shields.io/github/go-mod/go-version/bl4tcz/cubit?style=flat-square">
  <a href="LICENSE"><img alt="License MIT" src="https://img.shields.io/badge/license-MIT-8a7f6a?style=flat-square"></a>
  <img alt="Minecraft Java 26.2, other versions via ViaProxy" src="https://img.shields.io/badge/Minecraft%20Java-26.2%20%2B%20ViaProxy-6b8f71?style=flat-square">
  <img alt="Platforms" src="https://img.shields.io/badge/platforms-Linux%20%7C%20macOS%20%7C%20Windows%20%7C%20Android-5a6470?style=flat-square">
</p>

<p align="center">
  <a href="docs/GUIDE.md"><b>Guide</b></a> ·
  <a href="docs/COMMANDS.md">Commands</a> ·
  <a href="docs/API.md">HTTP API</a> ·
  <a href="docs/BUILD.md">Build from source</a> ·
  <a href="CHANGELOG.md">Changelog</a> ·
  <a href="README.es.md">Español</a>
</p>

---

Most Minecraft bot projects are libraries: you write the bot yourself. **Cubit is the finished bot.** Install it, open the panel, create a bot, and tell it `/mine diamond ~ ~ ~` or `/guard Steve`. It finds its own way with A* pathfinding, fights with real PvP technique, comes back after disconnects, and can even take orders in plain words through a local AI that runs on your own machine.

## Table of contents

- [Features](#features)
- [Quick start](#quick-start)
- [Usage](#usage)
- [How it works](#how-it-works)
- [FAQ](#faq)
- [Contributing](#contributing)
- [License](#license)

## Features

**Work**
- **Excavate** a whole box layer by layer, store the valuables in your chests, and never break a pickaxe.
- **Strip mine like a real player, no x-ray**: a staircase down to the best layer for each ore, then tunnels and branches. It only mines ore it can actually see.
- **Chop** whole trees of the woods you name (2×2 and Nether stems included) while leaving player builds alone.
- **Queue jobs** with `/queue` or chain them with ` ; ` and walk away. The queue survives reconnects.

**Fight**
- **Expert PvP**: shield, crits and combos, the mace, crystals, ender pearls, totems, bows and potions.
- **Bodyguard and area defense**: `/guard` a player, or `/fight in` an area and anyone who enters gets fought.

**Stay online 24/7**
- **AFK mode** with small anti-idle moves; it eats, sleeps at night, fights off mobs, and walks back to its spot after dying.
- **Auto-reconnect**: after a server restart or a dropped connection it rejoins and resumes its job and queue.
- **Auto-login** for AuthMe / nLogin `/login` prompts.

**Control**
- **Web panel for all your bots**, each with its own live console and autocomplete.
- **Built-in test server** you can play on right away. The panel downloads the official server and a Java runtime for you (after you accept the EULA). No Docker needed.
- **Plain-language orders** through a free **local AI ([Ollama](https://ollama.com))**: "mine 20 iron and bring it to me". It's optional, configured per bot, and nothing leaves your network.
- **Discord bridge**: slash commands `/bot`, `/bots` and `/status`, plus a channel showing what your bots say.
- **HTTP API** with Bearer keys and live Server-Sent Events, so you can script your bots ([docs](docs/API.md)).

**Run anywhere**
- **Single ~20 MB static binary**, no Java, Node or other runtime. About **70 MB of RAM per bot** on a real server ([performance notes](docs/PERFORMANCE.md)).
- Linux (amd64/arm64, Raspberry Pi included), macOS, Windows and Android (Termux).
- Speaks Minecraft Java **26.2** natively; servers on **other versions** work through [ViaProxy](docs/GUIDE.md#6-other-minecraft-versions), detected automatically.
- Premium (online-mode) servers with your Microsoft account. English or Spanish everywhere.
- **Signed one-click updates** from the panel (SHA-256 + ed25519 check, automatic rollback).

<p align="center"><img src="brand/promo/panel-bots.png" alt="The Cubit web panel: all your bots, each with a live console" width="100%"></p>

## Quick start

Prebuilt binaries and packages are on the [Releases page](https://github.com/bl4tcz/cubit/releases/latest).

### Linux

One command, no root. It installs into `~/.local/bin` and verifies the SHA-256 checksum:

```sh
curl -fsSL https://github.com/bl4tcz/cubit/releases/latest/download/install.sh | sh
~/.local/bin/cubit-panel        # opens the panel in your browser
```

Alternatively, install the `.deb` or `.rpm` from Releases (`sudo apt install ./cubit_*.deb`, `sudo dnf install ./cubit-*.rpm`). To keep the panel always on, run `systemctl --user enable --now cubit`.

### Windows

Download `cubit-<version>-windows-amd64.zip` (or `arm64`) from [Releases](https://github.com/bl4tcz/cubit/releases/latest), unzip it and run:

```powershell
cubit.exe --hub :8080 --open
```

There is no installer on purpose. The binary is not code-signed, so SmartScreen may warn you: *More info → Run anyway*. A Scoop manifest is in [`bucket/`](bucket/cubit.json) (see the [Guide](docs/GUIDE.md#1-run-it)).

### macOS and Android (Termux)

Download the binary for your system from [Releases](https://github.com/bl4tcz/cubit/releases/latest), then:

```sh
chmod +x cubit-*
./cubit-<version>-<os>-<arch> --hub :8080 --open
```

On Android, pick the `android-arm64` file. Add `--view 4 --memlimit 120` to keep it light.

### Docker

This also runs the test server and Ollama for you. You need [Docker](https://docs.docker.com/get-docker/):

```sh
git clone https://github.com/bl4tcz/cubit.git
cd cubit
./up.sh YourMinecraftName
```

It prints your panel link (`http://localhost:8080/?t=…`) and the Minecraft address (`localhost:25565`). `./up.sh logs` follows the output, `./up.sh down` stops everything.

### Build from source

Requires Go (the version in [`go.mod`](go.mod)) and git. No C compiler needed.

```sh
git clone https://github.com/bl4tcz/cubit.git
cd cubit
go build -o cubit .
./cubit --hub :8080 --open
```

Cross-compiling and packaging are covered in [docs/BUILD.md](docs/BUILD.md).

### First run

1. **Open the panel.** The link contains an access key (`?t=…`); keep the whole link.
2. **Create your bot.** The panel asks for a name, a server, an owner (your Minecraft name) and a language.
3. **Join it in game.** No server? Accept the test server the panel offers, then in Minecraft Java 26.2 go to *Multiplayer → Direct Connection* and enter `localhost:25565`.
4. **Give it an order.** Type `/follow YourName` in the bot's console. `/stop` stops it.

By default the panel only listens on the local machine. To reach it from another device use `--hub 0.0.0.0:8080`, but only on networks you trust, since the panel speaks plain HTTP. See the [Guide](docs/GUIDE.md#1-run-it).

## Usage

Type commands in the bot's **console in the panel**, or whisper them in game as an owner (`/msg MyBot follow Steve`). `~` means "where the bot is", just like in Minecraft.

| Command | What it does |
|---|---|
| `/follow <player>` | Follows a player until `/stop` |
| `/goto <player>` · `/goto <x> <y> <z>` | Walks there, building towers and bridges if needed |
| `/fight <player>` · `/fight in <x> <z> [<x2> <z2>]` | Fights a player, or everyone who enters an area |
| `/guard <player> [<minutes>]` | Bodyguard: follows a player and attacks whoever hits them |
| `/excavate <x1> <y1> <z1> <x2> <y2> <z2> [exact]` | Digs out the whole box, top down; `/excavate chests …` sets storage |
| `/mine <ores> <x> <y> <z> [every <n>] [total <n>]` | Strip mines, dropping ore in the chest at `x y z` |
| `/chop <woods> <x> <y> <z>` | Cuts whole trees within 24 blocks and picks up the logs |
| `/afk [here \| <x> <y> <z>]` | Stays at a spot around the clock |
| `/queue <command>` · `<a> ; <b>` | Lines up jobs to run one after another |
| `/ask <request>` | Plain words; the local AI plans and runs the commands |
| `/inventory [grid]` · `/drop [<item> [<n>]] [<player>]` | Shows or drops what it carries |
| `/status` · `/stop` · `/help` | Health and task, stop everything, list all commands |

Examples:

```text
/mine diamond 104 64 -224 total 32     → mine 32 diamonds, store them in that chest
/chop oak,birch ~ ~ ~                  → every oak and birch around it
/excavate ~ ~ ~ ~15 ~-20 ~15           → a 16×21×16 hole starting where it stands
/mine iron ~ ~ ~ ; /chop oak 10 64 10  → mine now, chop afterwards
/ask mine 20 iron and bring it to me   → let the local AI figure it out
```

Every command and option is in **[docs/COMMANDS.md](docs/COMMANDS.md)** (generated from the code). The panel, Discord, phones, other versions and the local AI are covered in the **[Guide](docs/GUIDE.md)**.

**Local AI:** install [Ollama](https://ollama.com) once and turn on the AI assistant in the bot's settings. The bot downloads its default model (`gemma4:e2b-it-q4_K_M`) the first time. See [Talk to it](docs/GUIDE.md#7-talk-to-it-local-ai).

## How it works

```text
 Browser panel ─┐
 Discord ───────┼─►  Hub (cubit --hub :8080) ─► one process per bot ─► Minecraft server
 HTTP API / SSE ┘     bots, keys, updates          │                     (directly, or through
                      test server, ViaProxy        │                      ViaProxy for other versions)
                                                   └─► Ollama (optional, local)
```

- **Hub.** `cubit --hub` serves the embedded web panel, the HTTP API and the Discord bridge, and starts and supervises each bot as its own process. It can also run the built-in test server and ViaProxy.
- **Protocol.** Bots speak the Minecraft Java 26.2 protocol natively in Go, using the vendored [go-mc26](third_party/go-mc26) library (derived from [Tnze/go-mc](https://github.com/Tnze/go-mc)). No game client is involved.
- **Movement.** [`pathing/`](pathing) is a weighted A* search over the bot's view of the world, with jumps, falls, water, and placing blocks to tower and bridge.
- **Behaviour.** [`combat/`](combat) (PvP tactics, items, guard, area defense), [`automation/`](automation) (excavate, mining, chopping, AFK) and [`safety/`](safety) (lava, fire and fall checks).
- **AI.** Plain-language requests go to a local Ollama model, which turns them into regular Cubit commands. Nothing is sent to a cloud service.

## FAQ

**Is it allowed to use bots on Minecraft servers?**
It depends on the server. Many public servers forbid bots, AFK tools or automation in their rules, and breaking them can get your account banned. Cubit is meant for your own server, a server with friends, or servers that explicitly allow bots. Read and respect each server's rules. This project is not affiliated with Mojang or Microsoft.

**Which Minecraft versions does it support?**
It speaks Java Edition 26.2 natively. Older or newer servers work through [ViaProxy](docs/GUIDE.md#6-other-minecraft-versions), which the panel detects and uses automatically. Bedrock Edition is not supported. It targets vanilla servers and uses no plugin commands.

**Do I need to know how to code?**
No. Everything is done from the panel and with chat-style commands. The [HTTP API](docs/API.md) is there if you want to script it.

**Does the AI cost anything or need an account?**
No. It runs locally with Ollama: no accounts, no API keys. It is optional, and the bot works fully without it.

**Can I try it without a server?**
Yes. The panel offers to set up a local test server, and `./cubit --demo` runs a demo with no server at all.

**How do I update?**
The panel tells you when a new version is out and, depending on how you installed it, updates in one click or shows the command to run (`./up.sh update` with Docker). See [Updating](docs/GUIDE.md#8-updating). If you are on v0.0.2, update by hand once (see the [Changelog](CHANGELOG.md)).

## Contributing

Issues and pull requests are welcome: bug reports, server compatibility notes, translations and new behaviours alike.

```sh
go vet ./...
./tools/ci-test.sh               # the test suite, as CI runs it
go run . --gen-docs docs         # regenerate docs/COMMANDS.md after changing commands
```

CI runs these three on every push and pull request. See [docs/BUILD.md](docs/BUILD.md) and [docs/TESTING.md](docs/TESTING.md) for details.

## License

[MIT](LICENSE). Not an official Minecraft product. Not approved by or associated with Mojang or Microsoft.

---

<p align="center">If Cubit saves you some grinding, consider giving the repo a ⭐. It helps other players find it.</p>
