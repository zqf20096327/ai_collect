<p align="center">
  <img src="presskit/artwork/banner-github-1280x640.svg" alt="SparkBots: your AI coding agents, working in a tiny 3D office" width="100%">
</p>

# SparkBots

**Your AI coding agents, working in a tiny 3D office. Everything stays on your machine.**

SparkBots turns the session history of your coding agents into a small low-poly campus you can walk around. Every **Claude Code**, **Codex** and **OpenCode** session is a robot at a desk, every project is a team area. You see at a glance who is working, who is waiting for you, and who is asleep, and you can walk up to a desk (or open a chat panel) and talk to that agent.

It is a personal tool first: local, private, a bit silly on purpose, and careful with anything that touches your sessions.

> Original mascot and artwork. SparkBots is not affiliated with Anthropic, OpenAI or the OpenCode project; their tools are only named as things SparkBots can read.

---

<p align="center">
  <img src="presskit/screenshots/office-story.jpg" alt="The SparkBots campus: project areas, data center, coffee factory, restaurant and yard (demo data)" width="90%">
</p>

<p align="center">
  <img src="presskit/screenshots/watercooler-race.jpg" alt="Water cooler chat in speech bubbles with answer buttons, and a race on the track round the campus" width="90%">
</p>

> **New in 1.1: Unity.** An optional, off-by-default public lobby: a glowing pod in the office opens a small shared 3D place where everyone who runs SparkBots can meet, chat in bubbles and gather around office amenities. Nothing connects anywhere until you switch it on. [Jump to Unity](#unity-the-public-lobby).

## A look around

The screenshots below use demo data (fake projects, made-up visitors); no real session, project or chat is shown in them.

<table>
  <tr>
    <td width="50%"><img src="presskit/screenshots/projects-panel.jpg" alt="The Projects panel next to the 3D campus: every project, how many agents are working or waiting"></td>
    <td width="50%"><img src="presskit/screenshots/game-room.jpg" alt="The campus from above: project areas, game room with pong and billiards, yard, restaurant and anger room"></td>
  </tr>
  <tr>
    <td><sub><b>Projects at a glance.</b> The side panel lists every project with its working and waiting agents; <i>Go</i> flies the camera there.</sub></td>
    <td><sub><b>The whole campus.</b> Project areas around a central plaza with the game room, yard, restaurant, anger room and more.</sub></td>
  </tr>
  <tr>
    <td><img src="presskit/screenshots/unity-lobby.jpg" alt="Unity, the public lobby: visitors around the phone booth, ghosts of people who left, amenity rings on the floor"></td>
    <td><img src="presskit/screenshots/unity-front.jpg" alt="Unity amenities: the big copier and the fax machine, their rings gold because two people stand and chat in each"></td>
  </tr>
  <tr>
    <td><sub><b>Unity.</b> Everyone arrives through the phone booth. Faint figures are ghosts of people who left.</sub></td>
    <td><sub><b>Places to talk.</b> The ring around an amenity turns gold when two or more people stand in it.</sub></td>
  </tr>
</table>

## Why

If you run several agents across several projects, the terminal gives you tabs and scrollback, not awareness. Which one is blocked on a permission prompt? Which project burned the tokens this week? What was that agent doing yesterday? SparkBots answers those at a glance, and makes the answers pleasant to look at.

## What you get

**See everything**
- A 3D campus: one area per project, one robot per session, sleeping robots for history, glowing ones for live work. A 100-worker view stays smooth (instanced meshes); test it with `&fixture=100`.
- Status colours and bubbles: working, waiting for you (amber beacon), error, done (a wave), idle, asleep.
- Every room is also a normal 2D panel (Teams, Control room, Stats, Board, Server room, Settings), so walking is never required.
- Get around fast: `Space` opens a quick map (click anywhere to fly there), double-click a project to go to it, and the Map tab lists every room. The three tools look different on purpose: a spark bot for Claude Code, a round-headed bot for Codex and a tall monolith for OpenCode.
- The Server room shows running agent processes, the runs SparkBots started and the MCP servers each project uses.

**Talk to your agents, carefully**
- Chat with any session from a side panel; replies stream in live. Continue, fork, or hire a new robot in a project.
- Safety rails built in: a session open in a terminal is never written to (fork instead), one run per session at a time, queued messages, a Stop button that only stops what SparkBots started, and `--dangerously-skip-permissions` is never used. A denied tool can be allowed for one retry, with a click.
- Send a **kanban card** to an agent, a fork, or a new robot. Cards move to Review when the run ends; Done is always manual. A read-only **Backlog.md** lane shows your project's backlog next to the cards.

**Understand usage**
- Stats by day, project, model and **service** (Claude Code / Codex / OpenCode), with 7/30/90-day views and an estimated cost (clearly labelled as an estimate).
- History is stored in SparkBots' own SQLite file, so it outlives the tools' transcript clean-up: analytics forever, locally.
- A **Data center**: one rack per project, with LEDs that blink faster the busier the project is, tape reels, cables and inspector robots. Click the console to search everything your agents ever said.

**Meet other people (optional)**
- **Unity** is a small public lobby for everyone who runs SparkBots: you appear as the owner character from your Settings, walk around a floating platform with a phone booth in the middle, chat in speech bubbles, gather around 16 little animated amenities (a fax that feeds a shredder, a big copier, a gold statue, a boxing ring where agents throw bytes, ...) and leave a ghost behind when you go. Off by default; see [Unity](#unity-the-public-lobby).

**Have a little fun** (cosmetic, never touching agent work)
- A coffee factory with a barista robot (press `O`; a drone brings the cup to you), a game room with pong, air hockey, rock-paper-scissors, dice, billiards and basketball: agents play each other, or **you take a seat against an agent** (rankings included; far-away agents are beamed or flown to the table). A race track around the campus (race car, rocket kart, monster truck with wheelies and somersaults, nitro on `Shift`, carmageddon), a gym, a restaurant, an anger room and a sponsor room.
- Walk as an avatar or float a big hand around; *Perform* zap, dance or high-five an agent; call a meeting with a crowd of followers; a "Boss is coming" key for when you want the office to look busy.
- A simulated water-cooler chat for idle agents in bubbles above their heads: 138 short threads in seven topics (games, cars, life, work, office, dev, gossip) with answer buttons and a topic picker; fully offline, written in advance, no model calls.
- An opening shot (the camera sinks from the top view to your character), a keymap with Basics / Games / Race / Popups tabs, and an About page for the maker (the logo in the header).

## Quick start

**Pull the repo, run one script, enjoy:**

```bash
git clone https://github.com/rapttor/sparkbots.git
cd sparkbots
./install.sh          # Windows: powershell -ExecutionPolicy Bypass -File .\install.ps1
```

The script checks Node (22.13+, Node 24 recommended) and pnpm and installs them if they are missing (it asks first, and only with Homebrew or nvm; otherwise it tells you what to install), installs the dependencies, builds, starts SparkBots and opens the page in your browser. Everything stays inside the repository folder; it never touches `~/.claude` or your agents' files. Useful options: `--no-open` (just print the address), `--dev` (watch mode with hot reload), `--skip-build`, `--install-only`, `--check` (report only, change nothing), `--yes` (do not ask). 

**Optional agent CLIs.** On a terminal the script also offers to install the tools SparkBots shows, each one only if it is missing and only after you say yes: Claude Code, OpenAI Codex CLI, OpenCode (`npm install -g`), and Ollama and llama.cpp (Homebrew on macOS/Linux, winget on Windows). Install without asking with `--tools claude,codex,opencode,ollama,llamacpp` (or `--tools all`; Windows: `-Tools ...`), or skip the offer with `--no-tools` (`-NoTools`). `./landing.sh` takes the same options. Windows example: `powershell -ExecutionPolicy Bypass -File .\install.ps1 -Tools claude,codex`. Read `install.sh` first if you like: it is short.

Prefer to start from the landing page? `./landing.sh` does the same setup, starts SparkBots in the background and opens the **landing page** (http://127.0.0.1:4380/) instead of the 3D office. It shows a button, "Open SparkBots", that opens your running session (the address, token included, never leaves your machine), and it notices when SparkBots starts or stops. `--no-open` and `--port N` work too.

By hand, the same thing is:

```bash
pnpm install
pnpm build
pnpm start --open     # prints http://127.0.0.1:4317/?t=<token>
```

| Command | What it does |
|---|---|
| `pnpm start` | Start the server (serves the built client). Add `--open` to open the browser. |
| `pnpm open` | Same as `pnpm start --open`. |
| `pnpm monitor` / `pnpm dev` | Watch mode: the server restarts on code changes, the client hot-reloads. Uses a persisted token (`~/.agent-office/dev-token`, mode 0600) so an open tab survives restarts. `--no-open` skips the browser. In the terminal, press `o` to open the page again (if you closed the browser) and `q` to quit. |
| `pnpm test` | Run the test suite (Vitest). |
| `pnpm typecheck` | TypeScript, strict. |

Try it without any history: add `&fixture=40` (any number) to the URL to fill the office with fake workers.

## Controls

| Key / mouse | What it does |
|---|---|
| `W A S D` / arrows, `Shift` | Move (hold Shift to sprint). In hand mode: A/D turn, W/S zoom. |
| Click floor | Avatar: walk there. Hand: the camera glides there; hold and drag to pan. |
| Click an agent | Open its dialog: actions, chat & history, status (caffeine, trophies). In hand mode a click with an agent inside the hand's circle does the same. |
| `E` | Talk to the nearby agent (hand mode: the one in the hand's circle), or use the data console. |
| `Z` | Perform on the nearest agent: a numbered picker (1-9 runs one). Popups answer to the number keys. |
| `C` / `0` | Camera behind you / reset the view. |
| Scroll, right-drag | Zoom (in = first person, out = overview) and turn. |
| `[` `]`, `-` `=` | Turn the view left / right, zoom out / in: hold the key, `Shift` = faster. The same as the ＋ − ↶ ↷ buttons in the bottom-right corner of the 3D view. |
| `M`, `L`, `T` | Map tab, lock zoom, name tags. |
| `O`, `R`, `U`, `I` | Order a coffee, rally the waiting agents, "boss is coming", lunch break. |
| `Q`, `X`, `Shift+click` | Meeting chat, release the followers, add/remove a follower. |
| `Space` | Quick map: click anywhere to fly there. |
| `F`, `Y`, `G` | With an agent nearby: follow me, fork into a new agent, nudge for a one-line status. |
| `Esc` | Close the open menu, chat or popup. |

Everything above is also clickable in the in-app Keymap (Settings), which has Games, Race and Popups tabs too. Unity has its own controls, listed in its section.

## Unity: the public lobby

> **Optional. Off by default.** While Unity is off, SparkBots makes no connection to anything.

Unity is a small shared 3D place for everyone who runs SparkBots. A glowing pod in the office is the door: step through and the office pauses behind you while you arrive in a phone booth in the middle of a floating green platform. You walk around as **the owner character you set up in Settings** (avatar, look and colour, and always walking, never the hand), see the other visitors move and talk in speech bubbles, and gather around a little town of office amenities. When you leave, a ghost of you stays behind for the next visitor.

<p align="center">
  <img src="presskit/screenshots/unity-pod.jpg" alt="The campus with the Unity pod, the door to the lobby, in the middle of the plaza" width="90%">
</p>

<p align="center">
  <img src="presskit/screenshots/unity-town.jpg" alt="Unity from above: a floating platform, the phone booth in the middle and a spiral of amenities with visitors around them" width="90%">
</p>

### Turn it on

1. Open the **Unity** panel (the hexagon icon in the header, or click the pod in the office).
2. Read what is shared, tick **Join the public Unity lobby** and pick a display name.
3. Click the pod, or **Enter Unity** in the panel. Once someone is inside, the pod reads "Unity · N here".

There is no account and no sign-up. Your identity is a random secret in `~/.agent-office/unity.json` (mode 600); delete the file to become someone new.

<p align="center">
  <img src="presskit/screenshots/unity-panel.jpg" alt="The Unity panel in the dock: the opt-in checkbox, what switching it on shares, display name and ghost setting" width="90%">
</p>

### What is in there

- **The phone booth.** Everybody arrives and leaves through it. A column of light marks every arrival.
- **Characters.** Each visitor is drawn as the character they chose (developer, raptor or spark bot, with their look and colour) and walks, sprints and stands like the owner does in the office.
- **Chat.** Press `Enter`, type up to 80 characters, and a bubble floats over your head for a few seconds. Plain text only; links are dropped.
- **Amenities.** Sixteen small, original, mostly animated things stand on a spiral around the booth, at least 10 units apart: a water cooler, a fax machine whose faxes fall straight into a shredder, a big copier that never stops (every copy goes into a shredder bin), a **gold statue of the maker at twice your size**, a boxing ring where two random agent types throw 0s and 1s at each other, an office plant, a stapler monument, a coffee machine, a vending machine, a rubber-duck shrine, a whiteboard of today's commits, ping-pong, an arcade cabinet, a campfire with bean bags, a jukebox and a giant keyboard floor that lights up where you step. In busy rooms (above 32 people) one more appears per four extra people, from a list of nine: an aquarium, lava lamp, neon sign, trophy case, bug lottery, snack table, hammock, git-tree sculpture and telescope. A room holds at most 50 people, so today the first five can show up. Press `E` next to one to use it.
- **Places to talk.** The ring on the floor around each amenity is where people stand and chat. With two or more people inside, the ring turns gold and says "N chatting".

### Leaving, and ghosts

Leaving (`Esc`, the button, or the booth) opens a small goodbye menu: **leave a message**, **just go**, or **stay**.

| How you leave | What others see |
|---|---|
| Leave a message | A faint figure of you with your message above its head |
| Just go | A faint figure of you |
| Close the window | A broken figure lying in pieces, "connection lost", no message |

A ghost disappears the moment you come back. It stays for up to 7 days (2 days for a broken one), and you can turn ghosts off in the Unity panel.

<p align="center">
  <img src="presskit/screenshots/unity-goodbye.jpg" alt="The goodbye menu in Unity: leave a message, just go, or stay" width="90%">
</p>

### Controls in Unity

| Key / mouse | What it does |
|---|---|
| `W A S D` / arrows, `Shift` | Walk, sprint (relative to the view). |
| Click the floor | Walk there. |
| Scroll | Zoom. |
| `[` `]` | Turn the view (hold). |
| `E` | Use the amenity you stand next to. |
| `Enter` | Jump to the chat box; `Enter` again sends. |
| `Esc` | Leave the chat box; then ask to leave Unity. |
| **Mute**, **Report** | Next to every name in the list on the left. |

### Safety and privacy

Unity is a public room and the other visitors are strangers.

- **What is shared:** your display name, your character (avatar, look, colour), where you stand and the short messages you type. **Never shared:** your agents, projects, folders, prompts, transcripts or anything from `~/.claude`, `~/.codex` or OpenCode.
- **What the relay sees:** the connection (your IP address, kept only as a short hash to limit abuse). It stores a ghost (name, character, last position, the goodbye message you chose to leave, the time), a ban list and reports (a reported person's name, last message and hashed IP, for the moderator, for 30 days). Chat bubbles pass through and are not stored. While Unity is on, the pod in the office also asks it for the head count, at most every 30 seconds while the tab is visible.
- **Yours to control:** mute anyone (kept in your browser), report anyone, turn ghosts off, switch Unity off at any time. With it off, nothing connects.
- **The relay protects the room:** limits per IP (sockets, connections per minute, messages), a flood cutoff, plain-text bubbles without links, reserved names (`admin`, `sparkbots` ...) turned into "Guest", and bans by identity or IP for the relay owner. Your identity secret is sent in a message, never in a URL; the relay keeps only its hash.
- The client does not trust the relay either: every message is validated before it is drawn, and text is only ever shown as plain text.

### Run your own relay

The default relay is a small Cloudflare Worker run by the maker. You can run your own (source in `relay/`; free tier is enough to try it, check Cloudflare's current limits):

```bash
cd relay
pnpm install
pnpm exec wrangler login
pnpm run deploy                 # prints https://sparkbots-relay.<you>.workers.dev
```

Then set the address in the Unity panel under **Advanced: relay address** (`wss://sparkbots-relay.<you>.workers.dev`). To moderate, store an admin token and use the CLI:

```bash
openssl rand -hex 24 | pnpm exec wrangler secret put ADMIN_TOKEN
ADMIN_TOKEN=... node scripts/admin.mjs peers        # also: reports, bans, ban <id> [minutes] [--ip], unban <id>
pnpm smoke wss://sparkbots-relay.<you>.workers.dev  # end-to-end check (pnpm abuse tests the limits)
```

### Try it without other people

Add `&unitycrowd=40` to the URL: a made-up crowd of players and ghosts (client-only, no network) walks about and chats, to see the town and the performance. Fewer or more (up to 60) works too.

## Supported agents

| Agent | Reads | Talks to it | Notes |
|---|---|---|---|
| Claude Code | `~/.claude/projects/` | `claude -p --resume <id>` | Optional hooks make state exact. |
| Codex | `~/.codex/sessions/` | Codex queue | Archived `.zst` sessions load on demand. |
| OpenCode | its SQLite DB (read-only), mirrored to a cache | `opencode run --session <id>` | Stop and run registry supported. |

Other local AI servers (Ollama, LM Studio, llama.cpp, ...) show up as *services* with status and loaded models, not as workers.

## Privacy

**Nothing leaves your machine.** The server binds to `127.0.0.1` only, requires a random token on every request, rejects foreign `Host`/`Origin` headers, makes no external requests and sends no telemetry. It only **reads** `~/.claude/`, `~/.codex/` and the local OpenCode database; its own files live in `~/.agent-office/` (the folder name is kept for compatibility). Message previews and speech bubbles can be turned off (`streamingMode` in `config.json`) for screen sharing.

**One optional exception: [Unity](#unity-the-public-lobby), off by default.** If you switch on the public Unity lobby (Unity panel, or the glowing pod in the office), your browser connects to a small relay (a Cloudflare Worker, source in `relay/`) and shares your display name, your chosen character (avatar, look, colour), your position in Unity and the short messages you type with the other people in the lobby, who are strangers. The relay sees your IP address (kept only as a short hash, to limit abuse), and the pod in the office asks it for the number of people inside (a plain count, at most every 30 seconds while the tab is visible) and stores a "ghost" (name, character, last position, the goodbye message you choose to leave, time) for up to 7 days (2 days if you just closed the window) unless you turn ghosts off. Your identity is a random secret in `~/.agent-office/unity.json`. Your agents, projects, folders, prompts and transcripts are never sent. While Unity is off, nothing connects anywhere.

## Safety

- Prompts reach `claude`, Codex or OpenCode as argv entries, never through a shell.
- A session open in an interactive terminal cannot be written to; fork it instead.
- One run per session at a time; extra messages are queued.
- `bypassPermissions` and `--dangerously-skip-permissions` are never used. Permission overrides per project are explicit and visible.
- Stop only signals processes SparkBots itself spawned.

## How it works (short)

Per-agent **adapters** discover sessions, tail the transcripts incrementally (byte offsets, never whole-file re-reads), and turn records into events: tool use, turns, usage, permission waits, sub-agents. A small **state machine** derives each worker's state from the live process plus recent activity. The server pushes **incremental patches** over a WebSocket (a rev-numbered diff protocol, see `docs/SYNC.md`), and the React Three Fiber client renders bots, desks and rooms as instanced meshes. Rooms, actions, effects and clips are **data files** picked up automatically, so adding one is a single small file.

```
server/   Fastify + ws + chokidar: adapters (claude-code, codex, opencode), model, stats, board, services, SQLite (app.db), Unity settings
src/      React + three/R3F + zustand: world (3D), unity (the public lobby), panels (2D), dock, state
relay/    Unity's relay: a Cloudflare Worker + one Durable Object per room (optional, see Unity)
docs/     TASKS.md (the plan), CHANGELOG.md, SYNC.md
presskit/ articles, artwork and screenshots
```

## Config (`~/.agent-office/`)

`config.json` (port, thresholds, history window, streaming mode), `teams.json` (directory globs to team merges, colours, per-team `allowedTools` / `permissionMode`), `board.json`, `runs.json`, `unity.json` (Unity's identity secret, only once you switch Unity on) and `app.db` (SQLite: usage history, rack aliases, caffeine, game results, rewards).

## Optional hooks (more precise state)

```bash
pnpm start hooks install     # shows a diff, asks to confirm, backs up settings.json first
pnpm start hooks uninstall   # removes exactly the entries it added
```

Adds `curl` hooks (SessionStart, UserPromptSubmit, PreToolUse, Notification, Stop, SubagentStop, SessionEnd) to `~/.claude/settings.json` that POST to `127.0.0.1` with a separate stable token (`~/.agent-office/hook-token`, mode 0600). Backups go to `~/.agent-office/backups/`. The app works fully without hooks; without them, state lags by up to about 15 seconds.

## Good to know

- The on-disk formats of Claude Code, Codex and OpenCode are **not public APIs**. The parsers are defensive: unknown or corrupt lines are skipped and counted, and nothing crashes the server.
- Cost figures are **estimates** from `server/stats/prices.json` (Claude prices only; other services show tokens). Subscription limits are not in local files, so SparkBots does not pretend to know them.
- It is a local single-user tool. There is no hosted version and no account.

## Roadmap

The plan lives in [`docs/TASKS.md`](docs/TASKS.md), tagged by effort. Open items include live permission approval in chat, slash commands, project cubicles, and optional opt-in sync. For Unity, ideas on the list are voice chat with nearby people, invite-only rooms, and models for the remaining amenity slots. Ideas are welcome as issues.

## Contributing

Issues and pull requests are welcome. Read [`CLAUDE.md`](CLAUDE.md) first: it holds the ground rules (read-only on agent data, no permission bypass, original mascot only, localhost only). Run `pnpm typecheck && pnpm test` before opening a PR (for changes to `relay/`, also `cd relay && pnpm typecheck`, and `pnpm dev` plus `pnpm smoke` and `pnpm abuse`). New rooms, actions and effects are single files under `src/world/zones`, `actions` and `fx`.

## Support the project

SparkBots is free and MIT licensed. If it saves you time or makes you smile:

- Patreon: https://www.patreon.com/c/rapttor
- Buy me a coffee: https://buymeacoffee.com/rapttor
- Ethereum (ETH, mainnet only): `0xeF4590e1c22Cabade5300aFa469f9dDEBA1275D2`
- GitHub Sponsors: not set up yet (github.com/rapttor)

A star on the repository, a bug report, or telling another person who runs too many agents helps just as much.

## Licence

Code: MIT. Artwork in `presskit/`: CC BY 4.0 unless a file says otherwise. The bot mascot is an original design.
