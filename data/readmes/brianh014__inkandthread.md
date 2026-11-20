<p align="center"><img src="src/web/logo.svg" alt="Ink &amp; Thread" width="200"></p>

<h1 align="center">Ink &amp; Thread</h1>

<p align="center">A choose-your-own visual novel, written as you play.</p>

Ink & Thread is a single-player story game, played like a Telltale game or a choose-your-own-adventure book. You build a world and a character, then act and speak only as that character, while an AI plays the Narrator: it plots in secret, so the story turns in ways you don't see coming, runs the story, voices everyone else, keeps track of the world, and quietly decides whether what you try works. An image AI draws the Cover, the portraits and a picture for each scene, as in a visual novel.

It runs on your own computer and talks to models you choose. Bring an OpenAI-compatible text API (OpenRouter, DeepInfra, a local server) and, for pictures, OpenRouter, Wiro or your own ComfyUI.

<p align="center"><img src="docs/screenshots/story-picture-desktop-light.jpg" alt="A story under way: a scene picture drawn as the scene changes, with the Recap, Loose Ends and recent characters beside it, and three Choices, light theme" width="620"> <img src="docs/screenshots/story-picture-mobile-light.jpg" alt="The same story on a phone, light theme" width="179"></p>
<p align="center"><img src="docs/screenshots/story-picture-desktop-dark.jpg" alt="A story under way: a scene picture drawn as the scene changes, with the Recap, Loose Ends and recent characters beside it, and three Choices, dark theme" width="620"> <img src="docs/screenshots/story-picture-mobile-dark.jpg" alt="The same story on a phone, dark theme" width="179"></p>

## Features

Most AI roleplay is one long chat with a model that agrees with everything, forgets what happened an hour ago and writes your character's lines for you. Ink & Thread is built as a story game instead: its Plot Threads are already there, hidden, and you find them by playing. Unlike open-ended AI chat, the story has a plot of its own, and unlike AI story apps that keep you on a set path, that plot answers your choices.

- **The world keeps secrets.** The New Story wizard builds a full world from your Theme, ideas and characters, with its own history, places and secret Plot Threads. The Narrator brings them into play when you least expect it, so the story can surprise you the way a written one does. The plot is hidden, not fixed: the threads wait in the world and answer what you do, so a choice you make stays made. Like a long series of books, with the same main character in the same world, a thread plays out as the story reaches it, and when they're used up the Narrator starts new ones, so the story can go on as long as you like. Write it all yourself, or let the Narrator fill in what you leave empty.
- **Your character is yours.** The Narrator never speaks or acts for your PC, never moves them somewhere or skips time on its own, and stops each reply at the moment your PC would answer or choose. Type your move, or pick from three Choices.
- **Things can go wrong.** Left to itself, an AI lets everything work. When your PC tries something risky, the Narrator sets how hard it is first, then a hidden die decides, so a bold plan can fail and a long shot can come off.
- **It remembers.** The story is kept as structured state, not just chat history: who your PC has met and what they know, Loose Ends still open, the time and date, and short Old Memories of everything older. You read and edit it all in the Journal, which holds only what your PC knows, and the Narrator gets what it needs each Turn, so a long story stays straight.
- **Nothing is final.** Every Message keeps a full Snapshot of the story, so you can rewrite, edit or regenerate a reply, step back to any point at once, branch off into a copy and try another path, or Start Over with the same world and characters. Tell the Narrator to change the world in your own words, or switch AI in the middle of a story.
- **A visual novel, drawn as you go.** A Cover, a portrait for each person, kept up to date as their looks change, and a picture whenever the scene changes or you ask for one. Image models that take reference pictures draw scenes from the portraits, so faces stay the same, and the Gallery lets you redraw, nudge or replace any picture with your own.
- **Your AI, your stories.** Bring your own AI, and what you make is yours: no platform holds your stories, sets content rules for them, or charges a subscription. No account is needed. Each story is one file on your own disk that you can duplicate, export and import. For privacy, run both the text AI and the pictures (ComfyUI) on your own graphics card so nothing leaves your computer, or on OpenRouter pick a **Provider** in Settings whose policy is not to store or log prompts (OpenRouter lists each provider's data policy).

## Screenshots

<table>
  <tr>
    <td width="75%"><img src="docs/screenshots/story-start-desktop-light.jpg" alt="The opening of a story, with the Recap, Loose Ends and recent characters beside it, and three Choices, light theme"></td>
    <td width="25%"><img src="docs/screenshots/story-start-mobile-light.jpg" alt="The opening of a story, with the Recap, Loose Ends and recent characters beside it, and three Choices, on a phone, light theme"></td>
  </tr>
  <tr>
    <td width="75%"><img src="docs/screenshots/story-start-desktop-dark.jpg" alt="The opening of a story, with the Recap, Loose Ends and recent characters beside it, and three Choices, dark theme"></td>
    <td width="25%"><img src="docs/screenshots/story-start-mobile-dark.jpg" alt="The opening of a story, with the Recap, Loose Ends and recent characters beside it, and three Choices, on a phone, dark theme"></td>
  </tr>
  <tr><td colspan="2"><sub>A story's opening, with three Choices or a box to write your own.</sub></td></tr>
  <tr>
    <td width="75%"><img src="docs/screenshots/gallery-desktop-light.jpg" alt="The Gallery: a portrait of each character and every scene picture, light theme"></td>
    <td width="25%"><img src="docs/screenshots/gallery-mobile-light.jpg" alt="The Gallery: a portrait of each character and every scene picture, on a phone, light theme"></td>
  </tr>
  <tr>
    <td width="75%"><img src="docs/screenshots/gallery-desktop-dark.jpg" alt="The Gallery: a portrait of each character and every scene picture, dark theme"></td>
    <td width="25%"><img src="docs/screenshots/gallery-mobile-dark.jpg" alt="The Gallery: a portrait of each character and every scene picture, on a phone, dark theme"></td>
  </tr>
  <tr><td colspan="2"><sub>The Gallery: every portrait and scene, to redraw, nudge or replace.</sub></td></tr>
  <tr>
    <td width="75%"><img src="docs/screenshots/journal-desktop-light.jpg" alt="The Journal: Story Time, the World Brief, the Recent Summary, Loose Ends and Chapters, light theme"></td>
    <td width="25%"><img src="docs/screenshots/journal-mobile-light.jpg" alt="The Journal: Story Time, the World Brief, the Recent Summary, Loose Ends and Chapters, on a phone, light theme"></td>
  </tr>
  <tr>
    <td width="75%"><img src="docs/screenshots/journal-desktop-dark.jpg" alt="The Journal: Story Time, the World Brief, the Recent Summary, Loose Ends and Chapters, dark theme"></td>
    <td width="25%"><img src="docs/screenshots/journal-mobile-dark.jpg" alt="The Journal: Story Time, the World Brief, the Recent Summary, Loose Ends and Chapters, on a phone, dark theme"></td>
  </tr>
  <tr><td colspan="2"><sub>The Journal: what your character knows, Loose Ends and Chapters, all editable.</sub></td></tr>
  <tr>
    <td width="75%"><img src="docs/screenshots/new-story-desktop-light.jpg" alt="The New Story wizard: choose a Theme, then describe your world and characters, light theme"></td>
    <td width="25%"><img src="docs/screenshots/new-story-mobile-light.jpg" alt="The New Story wizard: choose a Theme, then describe your world and characters, on a phone, light theme"></td>
  </tr>
  <tr>
    <td width="75%"><img src="docs/screenshots/new-story-desktop-dark.jpg" alt="The New Story wizard: choose a Theme, then describe your world and characters, dark theme"></td>
    <td width="25%"><img src="docs/screenshots/new-story-mobile-dark.jpg" alt="The New Story wizard: choose a Theme, then describe your world and characters, on a phone, dark theme"></td>
  </tr>
  <tr><td colspan="2"><sub>New Story: pick a Theme and describe as much or as little as you like.</sub></td></tr>
  <tr>
    <td width="75%"><img src="docs/screenshots/menu-desktop-light.jpg" alt="Ink &amp; Thread's Menu: New Story, Load Story, Reader's Guide and Settings beside the logo, light theme"></td>
    <td width="25%"><img src="docs/screenshots/menu-mobile-light.jpg" alt="Ink &amp; Thread's Menu: New Story, Load Story, Reader's Guide and Settings beside the logo, on a phone, light theme"></td>
  </tr>
  <tr>
    <td width="75%"><img src="docs/screenshots/menu-desktop-dark.jpg" alt="Ink &amp; Thread's Menu: New Story, Load Story, Reader's Guide and Settings beside the logo, dark theme"></td>
    <td width="25%"><img src="docs/screenshots/menu-mobile-dark.jpg" alt="Ink &amp; Thread's Menu: New Story, Load Story, Reader's Guide and Settings beside the logo, on a phone, dark theme"></td>
  </tr>
  <tr><td colspan="2"><sub>The Menu.</sub></td></tr>
</table>

## Quick Install

Download your system's file from the [Releases](https://github.com/brianh014/inkandthread/releases/latest) page, where the files are listed under **Assets** at the bottom. Each system has two, and most people want **Ink & Thread**; the Server is for running it on another machine and playing from your other devices.

- **Ink & Thread** is the app: it opens in your browser, for this computer only, and you end it with Quit in the Menu.
- **Ink & Thread Server** serves the whole network and opens no browser, so it runs headless too. Its log goes to the terminal, and stopping it (closing the window, or Ctrl+C) stops the server. Browse to it from any device at `http://<its address>:4600/`; it lists its addresses as it starts.

Both use port 4600. Once it's open, [connect an AI](#connecting-an-ai) in **Settings**, then read the **Reader's Guide** on the Menu for how to play. The downloads aren't signed yet, so Windows and macOS warn the first time you open one.

### Windows

1. Download `inkandthread-Windows.zip` (or `inkandthread-server-Windows.zip`).
2. Right-click the zip, choose **Extract All**, and extract it into a folder of its own, such as `Documents\Ink & Thread`. Don't open the program from inside the zip: Windows runs it from a temporary folder then, and your Saves would be lost. Your Saves, Settings and logs are kept in that folder, beside the program.
3. Open `inkandthread.exe`. If Windows says it protected your PC, choose **More info**, then **Run anyway**.

### macOS

1. Download `inkandthread-Mac-AppleSilicon.tar.gz` for an M-series Mac, or `inkandthread-Mac-Intel.tar.gz` for an Intel one (the `inkandthread-server-Mac-…` files for the Server). To tell which you have, open the Apple menu → **About This Mac**: **Chip** says Apple M… on an M-series Mac, and **Processor** says Intel on an Intel one.
2. Open the file to unpack `Ink & Thread.app`, and drag it to Applications. Your Saves, Settings and logs are kept in `~/Library/Application Support/Ink & Thread`.
3. Open it. The first time, macOS refuses it: close that message, then open **System Settings → Privacy & Security**, choose **Open Anyway** beside Ink & Thread, and confirm. **Open Anyway** only shows up after you've tried to open it once.

### Linux

1. Download and unpack it into a folder of its own, for x64. On a machine with no desktop, such as a server reached over SSH, use the Server: `inkandthread-server-Linux.tar.gz` in place of `inkandthread-Linux.tar.gz` below.

   ```bash
   mkdir -p ~/inkandthread && cd ~/inkandthread
   curl -fL -o inkandthread-Linux.tar.gz https://github.com/brianh014/inkandthread/releases/latest/download/inkandthread-Linux.tar.gz
   tar -xzf inkandthread-Linux.tar.gz && rm inkandthread-Linux.tar.gz
   ```

2. Your Saves, Settings and logs are kept in that folder, beside the program.
3. Run `~/inkandthread/inkandthread`, which opens your browser with `xdg-open` (if none opens, go to `http://127.0.0.1:4600/`). For the Server, run `~/inkandthread/inkandthread-server` and browse to one of the addresses it prints.

#### Running the Server in the background

To keep the Server running after you log out, and start it again when the machine restarts, make it a systemd service. Run this as the user who unpacked it, from any folder:

```bash
sudo tee /etc/systemd/system/inkandthread.service >/dev/null <<EOF
[Unit]
Description=Ink & Thread Server
After=network-online.target
Wants=network-online.target

[Service]
ExecStart=$HOME/inkandthread/inkandthread-server
User=$(id -un)
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable --now inkandthread
```

| To | Run |
| --- | --- |
| See whether it's running, and its addresses | `systemctl status inkandthread` |
| Follow its log | `journalctl -u inkandthread -f` (also kept in `~/inkandthread/logs`) |
| Restart it | `sudo systemctl restart inkandthread` |
| Stop it, and keep it from starting at boot | `sudo systemctl disable --now inkandthread` |

### Connecting an AI

Ink & Thread has no AI of its own, so it needs a key from an AI service before it can write. The easiest is [OpenRouter](https://openrouter.ai), which is already chosen in Settings. You pay it for what you use, usually under a cent a Turn. To try it for free, see [Google AI Studio](#a-free-key-google-ai-studio) below.

1. Sign up at [openrouter.ai](https://openrouter.ai), open [Credits](https://openrouter.ai/settings/credits) and add a few dollars.
2. Open [Keys](https://openrouter.ai/settings/keys), choose **Create Key**, give it any name, and copy the key it shows. It's shown only once, so paste it somewhere safe too.
3. In Ink & Thread, choose **Setup Ink & Thread** on the Menu. It walks you through the settings a page at a time, with what to pick on each. Paste the key, choose a **Text model** and, if you like, press **Test**. We recommend [DeepSeek V4.1 Flash](https://openrouter.ai/deepseek/deepseek-v4.1-flash-1017) (`deepseek/deepseek-v4.1-flash-1017`): in our tests it wrote the better stories of the low-cost AIs we tried, for under half a cent a Turn.
4. Setup then offers the Scribe, a second model that keeps the story's record straight (see [Scribe](#text-a-hosted-api)), then pictures and how the story reads. For pictures, we recommend **Online** with **OpenRouter**, which uses the same key, and Seedream 5.5, or Nano Banana 2.1 for a little better quality. If you have a graphics card, your own ComfyUI draws for free (see [Recommended settings](#images-your-own-comfyui)). Pictures are optional: without them the story is text only. Everything Setup sets is in **Settings** too, and **Settings → Guided setup** walks through it again.

### A free key: Google AI Studio

[Google AI Studio](https://aistudio.google.com) gives a free key with a Google account, no card needed. Sign in, choose **Get API key**, then in **Settings → Text** choose **Google AI Studio**, paste the key, save, and pick a Gemini Flash model. The free tier limits how many Turns a day you get, and Google may use what you send, your story among it, to improve its products. The same key draws pictures with Nano Banana under **Settings → Images → Google AI Studio**, but pictures aren't free: turn on billing in AI Studio first.

**Settings → Usage** shows how many requests Ink & Thread sent to each provider and model, by day, week or month, with the tokens for text and the cost wherever the provider reports it, as OpenRouter does.

### Updating

When a new version is out, a notice at the top of the screen says so, and **Settings → Updates** can check at any time. Choose **Install**, and Ink & Thread downloads it, restarts and comes back to the same page, on every system and for the Server too. Your Saves and Settings stay as they are, and if the new version fails to start, the old one comes back. To check, Ink & Thread asks GitHub for the newest release every few hours; nothing else is sent.

You can also update by hand: download the new version and unpack it over the old one, with Ink & Thread closed (on a Mac, replace `Ink & Thread.app` in Applications; for a systemd service, `sudo systemctl stop inkandthread` first and `start` it after).

## Using Ink & Thread

The **Reader's Guide** on the Menu explains everything in the app: making a story, playing, changing what happened, the Journal, pictures, Saves, every setting, and answers to common problems.

## Running from source

You need [Bun](https://bun.sh) 1.4 or later.

```bash
bun install
bun start
```

`bun start` serves Ink & Thread on port 4600 and opens it in your browser. Then [connect an AI](#connecting-an-ai) in **Settings**. To update, run `git pull` and `bun install`. Your Saves, Settings and logs stay in the project folder, which git ignores.

To try it with no model and no key, run it with stand-ins:

```bash
bun src/main.ts --fake --open
```

| Option | What it does |
| --- | --- |
| `--fake` | Uses a stand-in Narrator and image model, with their own Saves and Settings under `fake/`. |
| `--open` | Opens the browser once the server is up. |
| `--app` | Runs as the desktop app: this computer only, with Quit in the Menu. |
| `--server` | Runs as a server for the network, even from a built download. |
| `PORT` | The port to listen on (default `4600`). |
| `HOST` | The address to listen on (default `0.0.0.0` for a server, `127.0.0.1` for the app). |

`bun run install-launcher` adds an Ink & Thread shortcut to your desktop or app menu. `bun run release` builds the one-file downloads into `dist/release`. `bun run publish-release`, from an up-to-date `main`, tags the commit with `package.json`'s version and pushes the tag, and GitHub's Release workflow builds the downloads and publishes them as a GitHub release; a version with a hyphen, such as `0.2.0-alpha.1`, is a pre-release, which Install never offers. `bun run try-update` tries Install before a release: it builds this code as an old 0.0.1 copy and as the new version, and starts the old one with `--fake` on port 4660 against a stand-in release, so choosing Install brings it back as the new version.

> **A server on the network has no accounts.** Anyone who can reach it can play, change Settings and spend your saved keys. Keep it on a network you trust, or set `HOST=127.0.0.1`.

## Recommended settings

### Text: a hosted API

Use a hosted text API, such as OpenRouter (see [Connecting an AI](#connecting-an-ai)), [NanoGPT](https://nano-gpt.com), Google AI Studio or any other OpenAI-compatible provider. Every Turn sends the Narrator the newest Messages in full, plus the world, the Journal and the Old Memories, so a long story's prompt grows past 30,000 tokens. Large hosted models take all of it, keep the story straight and return the Narrator's JSON first time, for pennies a Turn. Staying on one provider keeps its prompt cache, which makes each Turn cheaper.

**Pick the provider, not only the model.** OpenRouter and NanoGPT serve an open-weights model from several providers, and the same model can write noticeably worse on one than another: some run a smaller copy to save cost, and some handle a long story's prompt less well. By default OpenRouter may switch providers between Turns, so if replies suddenly turn odd, such as speaking for your character or losing track of the scene, choose one provider in **Settings → Text → Provider**. The bench runs on DeepInfra.

**Scribe.** After every reply, a second AI call, the Scribe, keeps the story's record straight: where you are, who's there, what you wear and carry, what people have learned, and the time. It runs after the reply shows, so you don't wait on it. It also reviews a newly built world, and any change to it, quietly fixing contradictions and plot holes. A model checking its own work tends to pass it, so in **Settings → Text → Scribe**, tick **Use another model as the Scribe**. We recommend one from a different family than the Narrator's, at least as smart, on Medium thinking, such as GPT-6 Luna. Its calls are small, about $0.0005 a Turn, so a smarter model costs little, while a weak one makes the record worse. GPT-6 Luna is a closed model, so OpenAI sees the parts of the story it's sent; for privacy, choose an open-weights model on a provider that keeps no logs.

A local model works too: choose **Local / OpenAI server** and give the address of Ollama (`http://localhost:11434/v1`), LM Studio (`http://localhost:1234/v1`) or another OpenAI-compatible server. It suits short stories, play with nothing leaving your computer, and trying things out. A 10 GB GPU fits a model of about 12B at Q4 with a 16,000-token context, so the Narrator sees much less of a long story, and a Turn can take a minute. To get the most from it:

- Set the context length in the server, such as `PARAMETER num_ctx 16384` in an Ollama Modelfile. Ollama's default is small, and it cuts the prompt without saying so.
- In Settings → Text, set **Longest reply, in tokens** to about 3000 and **Recent Messages** to 40. The server keeps room in its context for the longest reply, so a high limit leaves less for the story.
- Leave the server's memory settings at their defaults first. On an RTX 3080, Ollama's `q8_0` KV cache made Gemma 4 12B about ten times slower.

A command works too, such as a provider's own command-line tool: in **Settings → Text**, choose **Command** as the **Text provider** and type it, such as `claude -p --output-format text`. As it runs a program on your computer, only Settings opened on that computer (at `127.0.0.1` or `localhost`) can set or change it. Ink & Thread sends it the prompt on its input and reads the reply from its output. Hosted APIs remain the recommended path: with a command, the provider's terms and content rules apply, a subscription's limits can stop play mid-story, each call starts the program again, and Usage counts calls only. The Reader's Guide → Choosing your AI says more.

### Images: your own ComfyUI

Use **Local (ComfyUI)** if you have a GPU for it. Ink & Thread draws a lot: the Cover, a portrait for each person, a Scene Image whenever the scene changes, pictures on request, and every redraw. On a paid image API each one costs money, and on your own ComfyUI they are free. Choose FLUX.2 or Qwen Image 2.1 in Simple Mode to keep faces the same from picture to picture, as SD 1.5 and SDXL can't use portraits.

ComfyUI keeps its model on the GPU between pictures. If a local text model or anything else needs the GPU too, turn on **Free GPU memory after each picture**. Use OpenRouter, [NanoGPT](https://nano-gpt.com) or [Wiro](https://wiro.ai) for pictures only if you have no GPU for ComfyUI: try Seedream 5.5, or Nano Banana 2.1 for a little better quality. On Wiro, set the project to API key only, and choose the model from the list in Settings, such as `bytedance/seedream-5-5`.

## Development

Bugs and ideas go in [Issues](https://github.com/brianh014/inkandthread/issues), and security problems to [a private advisory](https://github.com/brianh014/inkandthread/security/advisories/new) (see [`SECURITY.md`](SECURITY.md)).

```bash
bun run check   # lint and format check, typecheck, unit tests
bun run e2e     # Playwright end-to-end tests, against the stand-ins
bun run format  # format every file
```

The code is TypeScript on Bun, with a React page bundled by Bun itself. Start with:

- [`GLOSSARY.md`](GLOSSARY.md): the words the code and the UI use, such as Turn, Snapshot and Scene Image.
- [`docs/adr/`](docs/adr/): the decisions behind the design, and why.
- [`docs/spec.md`](docs/spec.md): the original specification.
- [`CONTRIBUTING.md`](CONTRIBUTING.md): how to set up, test and send a change.

## License

Copyright © 2026 Brian Holt. Ink & Thread is free software under the [GNU Affero General Public License 3.0](LICENSE). You may use, change, share and sell it. If you share a changed version, or run one as a server that other people use, you must offer them its source under the same license.
