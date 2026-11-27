# PuffPAI BuildBot v2

**Your Hardware. Your Data. Your AI.**

**Build it once, own it forever.**

BuildBot makes your own AI bot on your own computer. Say what you want in your own words. Toolsmith looks for ready-made apps, books and services and shows you one plan. What the PuffPAI store or your bot already has is used with your Yes; other apps it finds are listed as worth a look, with their links, and it does not download or run them (D231). Nothing happens without your Yes. Add more whenever you like.

The brain runs on your computer, on a model you pick. Nothing leaves your computer without your consent.

Under it is a small Core every bot shares: three zones (Vault, Brain, Bridge) and seven agents. Everything else is a package, so anyone can add apps, tools, skills, whole new screens and more. It's the same idea as Linux: a bare base anyone can build on. BuildBot is the base, and HomeBot is a full persona built on the same idea.

## What you need

- **Git**, and a Windows 10 or 11 PC, a Linux PC, a Jetson (ARM64) or a Mac.
- **Memory decides the model.** From 2 GB for the smallest, 10 GB for `qwen3.5:9b`, which handles real requests, up to 24 GB for `qwen3:30b-a3b`.
- **Python and Node.js** come with the installer if you don't have them. It lists what it would download and asks once. Nothing goes system-wide.
- **Ollama** runs the model. If it's already running, BuildBot uses it. If not, the installer offers it: a plain copy on Windows and Mac, Ollama's own script on Linux, which asks for your password.
- **Docker** only for apps that come as Docker apps.
- **For the window:** nothing extra on Windows. Chromium or Chrome on Linux and Mac.

## Install

Git copies the code; the installer does the rest:

```bash
git clone https://github.com/CypherSisters/PuffPAIBuildBot BuildBotv2
cd BuildBotv2
```

**Linux and Jetson:**

```bash
./install.sh
```

On a small home disk, such as a Jetson's, add `--data-dir <folder>`. `--dry-run` shows every step and changes nothing.

**Windows:** double-click `install.cmd`, or in PowerShell:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File install.ps1
```

`-DryRun` shows every step and changes nothing.

**Mac:** `./install.sh`, the same as Linux.

How far each has been run:

| Computer | State |
|---|---|
| Windows | Where most of the live testing happened |
| Linux | Install, setup, chat and a store app, run in containers. The full test suite runs here too |
| Jetson | One real install, inside a container, on a Jetson Orin |
| Mac | Installs, starts and stops on GitHub's Mac machines (Apple silicon), and its tests pass there. Not yet: setup with a model, a real app added, the window on a screen, or a Toolsmith try. No person has used it on a Mac yet |

## First run

The installer goes straight into setup, in your terminal: the brain, a PIN for your vault, a recovery code to keep safe, your data folder, the Bridge (open or closed), and whether Toolsmith may use a cloud model. Then your goal and one plan. Nothing happens without your Yes.

After that, use the launchers next to the code:

| | Windows | Linux and Mac |
|---|---|---|
| Start | `Start BuildBot.cmd` | `./start-buildbot.sh` |
| Stop | `Stop BuildBot.cmd` | `./stop-buildbot.sh` |
| Chat in a terminal | `Chat with BuildBot.cmd` | `./chat-buildbot.sh` |
| Sign in a browser | `Sign in a browser.cmd` | `./signin-buildbot.sh` |

Start opens the PuffPAI window. The same bot has a dashboard in your browser at http://puffpai.localhost:8420.

**Your vault locks after 5 minutes idle.** Setup asks for your PIN in its own window if it needs it. Elsewhere, type `/unlock` in the chat.

**A cloud model is your choice.** Only Toolsmith may use one, only if you pick it, with your own key, and with a $5 cap by default. While Toolsmith's tries are frozen (D231, as it ships), a build uses this computer's model and spends nothing; the company's model only writes a connection to a program you have. With tries on, a try runs as a program on your computer, as you (or, when Docker is running, in a Docker box that sees only its own folder, and an app tried in a box keeps running in one once installed; each card says which), and what it shows goes to the company you picked.

## Voice

Off until you turn it on: Settings, Voice, Turn voice on (or press the microphone in the chat). One Yes card, with your PIN, says what it downloads once, how big it is and from where: the speech programs from PyPI, the speech to text model (Vosk, 41 MB, alphacephei.com) and a voice (Piper, 64 MB, huggingface.co). The Bridge must be open for that download. After it, voice works with the internet off, on the CPU.

Press the microphone, speak, press it again (or hold it and let go). What you said is turned into text on this computer, shown in the chat box and sent like anything you type. The sound is not saved. Answers are read aloud for what you said, or always with Read answers aloud on. US English only. Not built: a wake word, always listening, other languages, and voice on a kiosk or a phone. Details and licenses: `packages/local-voice/README.md` (D190).

## Other devices

The home network starts off: only the bot's own computer can open it. Any device you pair on your home network gets everything you get on the bot's computer. Devices you haven't paired see only the pair screen.

1. On the bot's computer, open Settings, Your home network, and press Turn it on. The words beside it say what that means.
2. Press Show a pairing code. The addresses to open are listed above it. (Or run `puffpai pair` while BuildBot runs.)
3. On the other device, open an address and type the code.
4. Remove a device in Settings, Paired devices.

To run the window on another computer, with no bot on it:

```bash
./install.sh --window-for http://<address>
```

On Windows, use `install.ps1 -WindowFor http://<address>`. Turn the home network on or off with `puffpai network on` or `puffpai network off`. `puffpai` lives in `.venv/bin/` (`.venv\Scripts\` on Windows).

## More than one bot

```bash
./install.sh --bot second
```

On Windows, use `install.ps1 -Bot second`. You're never asked for a port: each bot takes the next free set and keeps it. They share one Ollama, so one may wait while another answers. The second bot's launchers are in `bots/second/`.

## How to update your BuildBot

An update keeps your bot: the same folder, vault and PIN, apps, linked folders, Yes cards, program keys, settings and chats. It says each step before it does it, asks you once, backs up your bot's files first, and can be undone. Add `-DryRun` (`--dry-run` on Linux and Mac) to see every step without changing anything. It downloads nothing by itself, except the new branch from your clone's own `origin` (the git way) and Python parts when a new build needs different ones (it says so before it asks).

**You got a zip.** Unpack it anywhere, but not inside your BuildBot folder. Then:

- Windows: in the new folder, double-click `Update BuildBot.cmd`. Drag your BuildBot folder (the one with `Start BuildBot.cmd` in it) into the window and press Enter. Or drop your BuildBot folder onto `Update BuildBot.cmd`.
- Linux and Mac: in the new folder, type `./update.sh ~/BuildBotv2` (your BuildBot folder).

To check the zip against the SHA-256 you were given, name the zip itself and the updater shows its SHA-256 before it asks. In the new folder: `powershell -NoProfile -ExecutionPolicy Bypass -File update.ps1 C:\PuffPAI\BuildBotv2 -From <the zip>` (Linux and Mac: `./update.sh ~/BuildBotv2 --from <the zip>`).

**You have a git clone.** The first time (test 16 has no updater yet), in your clone's folder:

Linux and Mac:

```bash
git fetch origin test17
bash <(git show FETCH_HEAD:update.sh) --branch test17
```

Windows, in PowerShell:

```powershell
git fetch origin test17
git show FETCH_HEAD:update.ps1 > $env:TEMP\update-buildbot.ps1; powershell -NoProfile -ExecutionPolicy Bypass -File $env:TEMP\update-buildbot.ps1 -Branch test17
```

`git fetch` gets the new commit (it sets `origin/<branch>`, as any fetch does). After that the updater only reads that commit from git and swaps the files itself, the same way as a zip. It never writes inside `.git` and never runs `git checkout`: your commits, branches, HEAD and index stay as they were. So git still shows the old branch, and lists BuildBot's files as changed, until you type the lines the updater prints at the end. They change no file, only what git shows, and they never leave a commit of yours without a branch: a branch that holds commits of yours is never moved (then they use a new branch name), and when git is on no branch the first line keeps that commit on a new branch. When git names no commit at all, it prints no lines and says git was left exactly as it was. Your bot works whether you type them or not. From then on, in your clone: `./update.sh --branch <name>`, or on Windows `powershell -NoProfile -ExecutionPolicy Bypass -File update.ps1 -Branch <name>`.

**Your own files.** One rule for both ways, zip and git, updating and going back: a file or folder of yours at a path the build being put in place does not have stays where it is. That includes files you made after an update, files in a folder the new build drops, files of yours in `scripts/build-files`, and a repo of your own. A file of yours at a path where that build has a file of its own stops the updater before it changes anything, and it names the file; so does a BuildBot file you changed, and a compiled Python file (`.pyc`) outside `__pycache__`. Which files are BuildBot's is told by the list of files each build ships, never by git: in a clone, a BuildBot file you changed stops it even when you committed the change, and a file you committed that no build has stays where it is. Folders the old build has and the new one does not move with the old code into the backup and come back if you go back; the plan names them.

**Going back.** Before it changes anything, the updater writes `Go back.cmd` (Linux and Mac: `go-back.sh`) into `update-backups` in your BuildBot folder. Double-click it (or run `./update-backups/go-back.sh`): the code and your bot's files from before the last update come back. What changed in your bot since (new chats, new vault items) moves to `update-backups/<date>/after-update` in your bot's own folder. Nothing of yours is deleted. With git, going back writes nothing inside `.git` either; if git does not show the old build then, it prints the lines to type.

**If an update stops in the middle** (a crash, a power cut, a closed window), run the updater again, any copy of it, or `Go back.cmd`. Before anything else it puts the folder back to the build you had, with your bot's files, and says so. Then run it again to update. Only one updater works on a folder at a time. It changes nothing while another program runs from your BuildBot folder (it names it); BuildBot's own chat and window programs are closed after BuildBot stops, and the plan names them. Before it moves anything, both ways, it checks that every folder it will move can be moved: when a window or a program has one open (a command window whose folder is inside it counts), it names that folder and changes nothing. A run that is refused, and an answer of no, leave every file and folder as they were. It says an update is done, or back as it was, only after checking every file. A missing or damaged list in the backup is made again from the old code there and checked against the list of that build the newer build ships; if the old code in the backup is damaged or does not match it, it says so, changes nothing, and offers to set that update aside, so a new update can run. If your folder's name has a `%` in it, use the PowerShell line the updater prints instead of `Go back.cmd`.

The backup: the old code is in `update-backups/<date>/code` in the BuildBot folder, and your bot's files are in `update-backups/<date>` in your bot's own folder. Books, downloads, models, linked folders and apps that did not come with BuildBot are not copied: an update does not change them. The updater never goes to an older build, and BuildBot won't start a bot that a newer build last ran. Linux and Mac: built, not yet run on a real Linux or Mac (D247).

## Moving a bot

`puffpai export <folder>`, or Settings, Move this bot to another computer, writes a folder you can put in a git repo. On the new computer, run `./install.sh --from <folder>` (`install.ps1 -From <folder>` on Windows).

It carries the name, the look, who your bot is, and what it came with. The vault, keys, chats, documents and pairings never go. Apps and books come back from a list on Knowledge, "Recommended for this bot", each with its own Yes.

## The store

Apps, PuffPAI store, in the window or the dashboard, or `puffpai store list`. The packages are at [CypherSisters/puffpai-store](https://github.com/CypherSisters/puffpai-store). Toolsmith can also suggest them on a plan.

## Build for it

`puffpai` is on no PATH: in the BuildBotv2 folder, type `./puffpai` (Linux, Mac) or `.\puffpai` (Windows), the launcher the installer writes there (D172). It runs `.venv`'s own command.

```bash
.venv/bin/puffpai new tool my-tool
.venv/bin/puffpai check my-tool
.venv/bin/puffpai add --link my-tool
```

`puffpai new` also starts an `app`, `skill`, `page`, `avatar`, `look` or `personality` (who your bot is: its name, how it talks, how it says hello and its look, D178). A folder of your own code can run with no manifest at all. Programs such as Home Assistant talk to your bot in OpenAI or Ollama style, with a key from `puffpai apikey new` (not yet tried with a real Home Assistant).

## Read in this order

| Doc | What it answers |
|---|---|
| [docs/04_DEVELOPERS.md](docs/04_DEVELOPERS.md) | Build for PuffPAI: quick starts for every kind of package, the CLI, the API |
| [docs/02_PACKAGE_CONTRACT.md](docs/02_PACKAGE_CONTRACT.md) | `puffpai.json`, the package kinds, what "Works on PuffPAI" means |
| [docs/01_ARCHITECTURE.md](docs/01_ARCHITECTURE.md) | The Core, part by part |
| [docs/03_WIZARD_AND_TOOLSMITH.md](docs/03_WIZARD_AND_TOOLSMITH.md) | Setup, and how Toolsmith finds, adopts, makes and proves |
| [docs/09_AGENT_SECURITY.md](docs/09_AGENT_SECURITY.md) | What each agent may touch, what needs your Yes, and the honest limits |
| [docs/zones/ZONES_TOGETHER.md](docs/zones/ZONES_TOGETHER.md) | The three zones and the floor rules |
| [docs/00_INTENT_AND_DECISIONS.md](docs/00_INTENT_AND_DECISIONS.md) | Every decision, with its date. A row marked PROPOSED was written before the owner's live test of it |

AI assistants: start with [AGENTS.md](AGENTS.md). To work on the code itself: [core/README.md](core/README.md).

## Rough edges

- **No TLS on your home network.** What a paired device does travels in plain text there. It's home network only: a VPN address is turned away.
- **The window off Windows is a browser app.** It's the same page in Chromium or Chrome's app mode, as protected as a browser tab. A native window comes later. Only Windows has the locked-down window.
- **Not proved on real hardware:** a person's Mac (setup with a model, a real app, the window, a Toolsmith try), a real Linux desktop's window, and most of what crosses between two real devices. So far, one window has reached one bot.
- **Small models** give weaker answers, and may not use a skill or a kept service. Bots sharing Ollama slow each other down.
- **A program key is powerful.** It can use your bot's tools, read pinned documents and get real values while the vault is open. Key use isn't logged yet. A Toolsmith plan card doesn't yet say a program asked.
- **Removing an app** doesn't stop its Docker containers yet. Its own Docker storage goes when you choose to delete its data, and stays when you keep it (D217). To see what BuildBot left in Docker, run `puffpai docker list`: everything BuildBot makes there has the label `com.puffpai.buildbot=1`, so you can tell it apart from your other Docker things. It lists only; it removes nothing.
- **Voice is new.** A spoken round trip ran on one Windows PC; a person speaking into the window's microphone has not been tried yet. English only.
- **Not in v2 yet:** a wake word, reminders, pictures and Excel in knowledge, and a Smart Home page.
- **Search by meaning** (D187) is off until you turn it on on the Knowledge page. It downloads a small model after its own Yes and runs on this computer. Not yet tested by the owner.
- **No upgrade from v1.** Build again with v2. Within v2, a newer build updates your bot in place (How to update your BuildBot).

## v1

v1's code is in this repository's history, up to commit [`cb0c9e33`](https://github.com/CypherSisters/PuffPAIBuildBot/tree/cb0c9e339a9b44a275bf28d1c95d8a46a3e02d1f).

## License

Apache 2.0: [LICENSE](LICENSE). What comes from others: [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

Cypher Sisters. puff puff pass.
