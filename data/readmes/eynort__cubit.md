<p align="center"><img src="brand/promo/hero.png" alt="Cubit: Minecraft bots that fight, mine, chop and stay online, run from a web panel" width="100%"></p>

<h3 align="center">Minecraft bots that do the work for you.</h3>

<p align="center">They fight, mine, chop and stay online 24/7, run from a web panel, at <b>~70 MB of RAM per bot</b>.<br>No coding, no cloud, no API keys.</p>

<p align="center">
  <img alt="Minecraft Java 26.2, other versions via ViaProxy" src="https://img.shields.io/badge/Minecraft%20Java-26.2%20%2B%20ViaProxy-6b8f71?style=flat-square">
  <img alt="RAM per bot" src="https://img.shields.io/badge/RAM-~70%20MB%20per%20bot-4a5a6a?style=flat-square">
  <img alt="Binary" src="https://img.shields.io/badge/binary-~20%20MB-5a6470?style=flat-square">
  <img alt="Local AI" src="https://img.shields.io/badge/AI-local%20%26%20free-7a6a8a?style=flat-square">
  <img alt="License MIT" src="https://img.shields.io/badge/license-MIT-8a7f6a?style=flat-square">
</p>

<p align="center"><a href="README.es.md">Español</a> · <a href="docs/GUIDE.md"><b>Guide</b></a> · <a href="docs/COMMANDS.md">Commands</a> · <a href="docs/API.md">API</a></p>

## Quick start

```sh
curl -fsSL https://github.com/eynort/cubit/releases/latest/download/install.sh | sh   # install (Linux, no root)
~/.local/bin/cubit-panel                                                              # open the panel
```

Then:

1. **Create your bot.** The panel opens in your browser and asks for a name, a server, an owner (your Minecraft name) and a language.
2. **Join it in game.** If you have no server, accept the test server the panel offers, then in Minecraft Java 26.2 go to *Multiplayer → Direct Connection* and enter `localhost:25565`.
3. **Give it an order.** Type `/follow YourName` in the bot's console in the panel and it starts following you. `/stop` stops it; the rest is in [How to use the bot](#how-to-use-the-bot).

Windows, macOS, Android and Docker are in [Start in one minute](#start-in-one-minute).

---

## Why Cubit

- **Ready to use, not a library.** Install it, open the panel, create a bot, give it a job. You never write a line of code.
- **It does real work.** Expert PvP, whole-area excavation, legit strip mining, tree chopping and 24/7 AFK, all built in.
- **Featherweight.** One ~20 MB program with no Java, Node or runtime. About 70 MB of RAM per bot: ten bots fit in 0.7 GB.
- **Talk to it in plain words.** An optional AI runs **on your own machine** (Ollama): free, no accounts, no API keys, nothing leaves your network.
- **Yours, on your hardware.** Your accounts and your bots stay on your PC, a Raspberry Pi, a $5 VPS or an old Android phone. No subscription, no third-party servers.

| | |
|---|---|
| **~70 MB** | RAM per bot (75 MB at the peak of a PvP fight) |
| **0.7 GB** | ten bots at the same time |
| **~20 MB** | one binary, with no Java, Node or runtime to install |

## What it does

**Work**
- **Excavate.** Empties a whole box layer by layer, stores the valuables in your chests and never breaks a pickaxe.
- **Mine.** Strip mining like a real player: a staircase down to the best layer for each ore, then tunnels and branches. No x-ray: it only mines ore it can see.
- **Chop.** Whole trees of the woods you name, 2×2 and Nether ones included, and it leaves player builds alone.
- **Queue.** Line up jobs (`/queue`, or chain them with ` ; `) and walk away: it runs them one after another.

**Fight**
- **Expert PvP.** Shield, crits and combos, the mace, crystals, pearls and totems. It never runs away.
- **Bodyguard and area defense.** `/guard` a player, or `/fight in` an area: anyone who comes in gets fought.

**Stay online**
- **24/7 AFK.** It stays at a spot around the clock: small moves so it is not kicked for idling, eats, sleeps at night, fights off mobs, and walks back after dying or reconnecting.
- **Comes back by itself.** If the server restarts or the connection drops, it rejoins and carries on with its job and queue. It answers AuthMe / nLogin `/login` prompts too.
- **Finds its own way** with A* pathfinding, building towers and bridges when it needs them.

**Talk & control**
- **Web panel for all your bots**, each with its own console and autocomplete, plus a built-in test server you can play on right away (no Docker needed).
- **Plain-language orders.** "mine 20 iron and bring it to me": the local AI turns it into commands. Optional, per bot.
- **Discord.** Give orders with `/bot`, `/bots` and `/status`, and read what your bots say in a channel.
- **HTTP API with live events** to drive your bots from your own scripts.

**Run anywhere**
- Linux, macOS, Windows, Raspberry Pi and Android (Termux).
- Servers on **other Minecraft versions** are joined through [ViaProxy](docs/GUIDE.md#6-other-minecraft-versions).
- Premium (online-mode) servers with your Microsoft account, and English or Spanish everywhere.

<p align="center"><img src="brand/promo/panel-bots.png" alt="The panel: all your bots, each with a live console" width="100%"></p>

## Start in one minute

**Windows**: with [Scoop](https://scoop.sh):

```powershell
scoop bucket add cubit https://github.com/eynort/cubit
scoop install cubit/cubit
```

This adds a *Cubit* shortcut to the Start menu that opens the panel. Prefer doing it by hand? Download `cubit-<version>-windows-amd64.zip` from [Releases](../../releases), unzip it and run `cubit.exe --hub :8080 --open`. There is no installer on purpose. `winget` will come later.

**Linux**: one command, no root:

```sh
curl -fsSL https://github.com/eynort/cubit/releases/latest/download/install.sh | sh
```

Or install the `.deb` / `.rpm` from [Releases](../../releases) (`sudo apt install ./cubit_*.deb`, `sudo dnf install ./cubit-*.rpm`). To keep the panel always on: `systemctl --user enable --now cubit`.

**macOS** and **Android (Termux)**: download the binary for your system from [Releases](../../releases) and run `./cubit --hub :8080 --open`.

Then:

1. **Open the panel**: *Cubit* in your app menu opens it in the browser. The link has an access key (`?t=…`); keep the whole link.
2. **Create your bot**: the panel walks you through it (name, server, owner, language).
3. **Play with it**: the first time, the panel offers to set up a test server for you. In **Minecraft Java 26.2**, go to *Multiplayer → Direct Connection* and enter `localhost:25565`.

To talk to it in plain words, install [Ollama](https://ollama.com) once: the bot downloads its model by itself (see the [Guide](docs/GUIDE.md#7-talk-to-it-local-ai)).

### Updating

The panel tells you when there is a new version and, depending on how you installed Cubit, updates it in one click or shows the command to run (`./up.sh update` with Docker). See [Updating](docs/GUIDE.md#8-updating).

### Advanced: Docker

If you prefer containers (this also runs the test server and Ollama for you), you need [Docker](https://docs.docker.com/get-docker/):

```sh
git clone https://github.com/eynort/cubit.git
cd cubit
./up.sh YourMinecraftName
```

When it finishes, it prints your panel link (`http://localhost:8080/?t=…`) and the Minecraft address (`localhost:25565`).

## How to use the bot

Type commands in the bot's **console in the panel**. In game, whisper them as an owner: `/msg MyBot follow Steve`. `~` means "where the bot is", just like in Minecraft.

**`/follow <player>`**: follows a player non-stop, until `/stop`.
```
/follow Steve
```

**`/goto <player>` · `/goto <x> <y> <z>`**: walks to a player or to a block, building towers and bridges if it needs them. If that block is in the air or inside the ground, it stops on the nearest floor in that column.
```
/goto Steve
/goto 120 64 -340
/goto ~50 ~ ~     → 50 blocks east of where it is now
```

**`/fight <player>` · `/fight in <x> <z> [<x2> <z2>]`**: fights a player until one of them dies, or every player who enters an area (a point gets a radius of 8 blocks, or give two corners).
```
/fight Alex
/fight in 100 200             → everyone within 8 blocks of 100 200
/fight in 0 0 50 50           → everyone inside that square
```

**`/guard <player> [<minutes>]`**: bodyguard mode. It follows a player and attacks whoever hits them.
```
/guard Steve
/guard Steve 30               → for 30 minutes
```

**`/excavate <x1> <y1> <z1> <x2> <y2> <z2> [exact]`**: digs out the whole box between two corners, 4 blocks at a time from the top down. It never breaks a pickaxe.
```
/excavate 10 70 10 30 50 30   → the box between those two corners
/excavate ~ ~ ~ ~15 ~-20 ~15  → a 16×21×16 hole starting where it stands
/excavate 0 60 0 15 40 15 exact → exactly those blocks (otherwise it fits the box to whole chunks)
/excavate chunk 0 64          → the whole chunk it stands in, from y 0 to 64
```

**`/excavate chests …`**: the chests where `/excavate` stores the valuables when it is full, and takes pickaxes from. A whole wall of chests counts if you give it any one of them.
```
/excavate chests 104 103 -224 → add that chest
/excavate chests list         → show them
/excavate chests remove 104 103 -224
/excavate chests clear        → forget them all
```

**`/mine <ores> <x> <y> <z> [every <n>] [total <n>]`**: strip mining like a real player, with no x-ray. It digs a staircase down to the best layer for that ore (diamond at y -59, iron at 16…), then a main tunnel with side branches every 3 blocks, and only mines ore it can actually see. `x y z` is the chest where it drops the ore (every 8 by default) and takes pickaxes from. The mine starts where the bot stands.
```
/mine diamond 104 64 -224              → diamonds, drop them in that chest every 8
/mine iron,copper ~ ~ ~ every 16       → a layer good for both, chest where it stands
/mine diamond 104 64 -224 total 32     → stop after 32
```

**`/chop <woods> <x> <y> <z>`**: cuts down whole trees of those woods within 24 blocks of a point, tops included, and picks up the logs. It leaves player builds alone (logs with no natural leaves, or touching planks, glass, doors…). Give the ground `y`.
```
/chop oak ~ ~ ~                  → every oak around it
/chop oak,birch 100 64 200       → oaks and birches around that point
/chop dark_oak,pale_oak ~ ~ ~    → big 2×2 trees too
/chop crimson,warped ~ ~ ~       → Nether stems
```

**`/afk [here | <x> <y> <z>]`**: stays at a spot around the clock until `/stop` (where it stands, or it walks to the coordinates first). Every 1-4 minutes it does something small (looks around, jumps, steps aside and back) so the server does not kick it for idling, and it returns to the spot if pushed. It eats when hungry, fights back mobs that come close, sleeps in a bed within 16 blocks at night or in a thunderstorm, and after dying or reconnecting it walks back to the spot.
```
/afk                          → stay right here
/afk 120 64 -340              → walk there and stay
```

**`/ask <request>`** (or just whisper it a sentence): plain words instead of commands. The local AI plans the commands, runs them and answers in the chat. It needs the AI assistant on in the bot's settings and Ollama running.
```
/ask mine 20 iron and bring it to me
/ask how are you doing?       → it just answers in the chat
```

**`/inventory [grid]`**: shows what it carries: armor, hotbar and inventory.
```
/inventory
/inventory grid               → laid out like the game screen
```

**`/drop [<item> [<amount>]] [<player>]`**: drops everything, or one item, or walks to a player and throws it to them.
```
/drop                         → everything, on the ground
/drop diamond                 → all its diamonds
/drop cobblestone 32          → 32 cobblestone
/drop Steve                   → everything, thrown to Steve
/drop diamond 5 Steve         → 5 diamonds, thrown to Steve
```

**`/queue <command>` · `<a> ; <b>`**: a to-do list. `/queue` adds a command (`chop`, `mine`, `excavate` or `goto x y z`) to run when the current task ends. In any line, ` ; ` chains commands: the first starts now and the rest wait their turn. When a task fails or gives up, the bot says so in the chat and pauses the list; `/queue resume` carries on. The list survives reconnects.
```
/queue /chop oak ~ ~ ~
/queue list                   → what is waiting, numbered
/queue remove 2               → forget the second one
/queue clear                  → forget them all
/queue resume                 → carry on after a failure or /stop
/mine iron ~ ~ ~ ; /chop oak 10 64 10   → mine now, chop afterwards
```

**`/stop`**: stops whatever it is doing: fighting, walking or digging. It also pauses the queue (it keeps what is waiting; `/queue resume` continues).
```
/stop
```

**`/status`**: health, food, position and what it is fighting.
```
/status
```

**`/say <text>`** (or just type with no `/`): writes in the game chat.
```
/say hello everyone
hello everyone
```

**`/cmd <command>`**: runs a server command as the bot (it needs to be op for most of them).
```
/cmd time set day
/cmd tp Steve
```

**`/sprint on|off`**: lets it run, or makes it always walk.
```
/sprint off
```

**`/lang en|es`**: the language of its messages. Commands are always in English.
```
/lang es
```

**`/help`**: lists every command. **`/quit`** disconnects the bot and closes it.

The full reference, with every option, is in [docs/COMMANDS.md](docs/COMMANDS.md).

## Learn more

- **[Guide](docs/GUIDE.md)**: the panel, servers, Discord, phones, other versions and the local AI.
- **[Commands](docs/COMMANDS.md)**: every command and option.
- **[HTTP API](docs/API.md)**: list bots, send commands and follow chat and tasks live from your own scripts.
- **[Compile it yourself](docs/BUILD.md)**: build from source.

Play fair: use it on your own server, or on servers that allow bots.

---

<sub>MIT. Not an official Minecraft product. Not approved by or associated with Mojang or Microsoft.</sub>
