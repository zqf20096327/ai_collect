<div align="center">

<img src="assets/readme-hero.svg" alt="JARVIS — your personal AI assistant for PC and phone" width="100%">

<br>

<a href="https://github.com/ASDprogrammer521/Jarvis-ai/releases/latest"><img src="https://img.shields.io/badge/Download-Windows%20EXE-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Download Windows EXE"></a>
<a href="https://github.com/ASDprogrammer521/Jarvis-ai/releases/latest"><img src="https://img.shields.io/badge/Download-Android%20APK-3DDC84?style=for-the-badge&logo=android&logoColor=white" alt="Download Android APK"></a>
<a href="https://discord.com/invite/r5q93NpRPt"><img src="https://img.shields.io/badge/Discord-Community-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Join the Jarvis Discord"></a>

<img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.11+">
<img src="https://img.shields.io/badge/Version-5.x-6ee7ff?style=flat-square" alt="Version 5.x">
<img src="https://img.shields.io/badge/Status-Active-success?style=flat-square" alt="Status: active">
<img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT license">
<img src="https://img.shields.io/badge/By-ASDcuber-orange?style=flat-square" alt="By ASDcuber">

<br><br>

**[Download](#download)** · **[Quick start](#quick-start)** · **[Features](#features)** · **[Live camera](#live-camera)** · **[Offline mode](#offline-mode)** · **[3D with Blender](#3d-with-blender)** · **[Hand Space](#hand-space)** · **[Tools](#built-in-tools)** · **[Phone](#phone-connection)** · **[Security](#security)**

</div>

<img src="assets/divider.svg" width="100%" alt="">

## Overview

**Jarvis AI** is an intelligent assistant that automates your workflow and simplifies everyday computer tasks. A clean, modern interface sits on top of serious tools: **voice control, screen and live-camera awareness, desktop automation, a holographic HUD, hand-controlled Hand Space, 3D modelling in Blender, a speedcubing site, an offline mode, profiles, plugins and a full phone companion that can even unlock your phone** — one system, version **5.x**.

<table>
<tr>
<td width="25%" valign="top" align="center"><h3>🎙️ Voice</h3>Push-to-talk, open mic and an optional local <i>"Hey Jarvis"</i> wake word.</td>
<td width="25%" valign="top" align="center"><h3>👁️ Vision</h3>Reads your screen, solves what you write on a board in front of the camera, scans receipts, recognises faces and hands.</td>
<td width="25%" valign="top" align="center"><h3>🖥️ Control</h3>Apps, windows, files, browser, system settings, Gmail and Calendar — by voice or text.</td>
<td width="25%" valign="top" align="center"><h3>📱 Phone</h3>Native Android app: calls, SMS, <b>unlock</b>, find my phone, big file transfer — over an encrypted link.</td>
</tr>
</table>

<img src="assets/divider.svg" width="100%" alt="">

## Download

No Python required.

1. Open **[Releases](https://github.com/ASDprogrammer521/Jarvis-ai/releases/latest)**.
2. Download `Jarvis-Windows-x64-v*.zip` (and the APK for your phone).
3. Extract the zip and run **`Jarvis.exe`**.
4. Enter your **Gemini API key** on first launch.

> [!NOTE]
> Windows may show SmartScreen because the build is unsigned → **More info → Run anyway**.

<details>
<summary><b>Maintainers: publish a new release</b></summary>

```bash
git tag v1.0.1
git push origin v1.0.1
```

Or: **Actions → Build Windows EXE + Release → Run workflow** (optional tag input).

Local build on Windows:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\build_exe.ps1
```

</details>

## Quick start

Prefer running from source?

**1 · Install dependencies.** `setup.py` reads the single `requirements.txt`, skips packages for other operating systems and fetches the Playwright browsers:

```bash
python setup.py
```

**2 · Add your Gemini API key.** On first launch the app asks for it, or place it in `config/api_keys.json`.

**3 · Start Jarvis:**

```bash
python main.py
```

<img src="assets/divider.svg" width="100%" alt="">

## Features

| Feature | Description |
| ------- | ----------- |
| 💎 **Modern & clean UI** | Dashboard · Chat · Settings tabs with a cinematic HUD |
| 🧑‍🚀 **HUD modes & 3D models** | Holo · Crystal · Globe · Knot · Helix · Face — or drop in your own `.obj` |
| ✋ **Hand Space** | Browse drives, folders, pictures, notes, 3D models and videos as glass cards you grab with your bare hands — and design your own cards |
| 📷 **Live camera** | "Open the camera" — a live view that stays open until *you* close it. Say "full screen" (or press the button) for a full-screen picture with a light Jarvis in the corner. Write a task on a board, say "solve it", and Jarvis reads and solves it. [Details](#live-camera) |
| 📴 **Offline mode** | When the internet is down or too poor for the live voice session, Jarvis switches by itself to local voice and text commands — and switches back when the line is good again. [Details](#offline-mode) |
| 🧊 **3D with Blender** | "Create a low-poly castle in Blender" — Jarvis builds, edits, recolours, renders and exports real 3D models, and can model a picture you give it. [Details](#3d-with-blender) |
| 🧩 **Speedcubing site** | Your own Rubik's-cube timer (2×2–7×7, inspection, scrambles, ao5 / ao12) and an OLL / PLL / F2L algorithm trainer — "open my cubing timer" |
| 🔓 **Phone unlock** | "Unlock my phone" — the Jarvis App draws your pattern, taps your PIN or types your password. The secret never leaves the phone. [Details](#phone-unlock) |
| 🎙️ **Voice + wake word** | Push-to-talk, open mic, mute, optional local "Hey Jarvis" wake word |
| 📱 **Jarvis App (phone)** | Native Android app — **call by name or number**, incoming-call alerts on the PC, find my phone, big file transfer, SMS, lock, **unlock**, locate — no ADB. A lightweight browser page covers chat and basic commands |
| 🔒 **Encrypted link** | HTTPS / WSS by default. Jarvis makes its own certificate automatically — nothing to buy or install |
| 🧩 **Modes** | "Work mode" opens and arranges a whole set-up; save your own by voice |
| 🪟 **Window control by name** | "Minimize Discord", "snap Chrome left", "Chrome and Discord side by side", "move Chrome to the other monitor" act on *that* app's window |
| ⌨️ **Custom shortcuts** | Mute, fullscreen and compact mode keys are yours to change in Settings → Shortcuts |
| ⚡ **Fast automation** | Apps, files, browser, system controls, clipboard, screenshots, messaging |
| 🛡️ **Safe by design** | Shutdown / restart / messages need an on-screen confirm · `undo` reverses volume, brightness, files and more |
| 📊 **Admin dashboard** | Remote control from a browser or the phone via pairing key |
| 🧾 **Receipt scanner** | Show a photo of a receipt — Gemini reads the total and category and logs the expense |
| 📬 **Gmail & Calendar** | "What emails came today?", "Put a meeting on Friday at 15:00" |
| 🖐️ **Hand gestures** | Control media, volume, mic and more with your hand — switch on and map each gesture in Settings |
| 🙂 **Face ID** | Recognises people through the webcam — greets them by name; switch on/off in Settings → Face ID |
| 🧠 **Memory** | Long-term facts you can view and delete |
| 🔌 **Plugins + store** | Drop-in tools in `plugins/`; list / enable / disable / install from URL |
| 👤 **Profiles** | `home` · `work` · `game` presets |
| 🔄 **Self-update** | Checks GitHub for updates and applies them |
| 🖥️ **Compact mode** | Floating always-on-top mic (F12) |
| 💻 **Windows EXE** | Single-folder build via GitHub Releases — no Python install |

<img src="assets/divider.svg" width="100%" alt="">

## Live camera

Jarvis can show your webcam live and look through it.

| Say | What happens |
| --- | ------------ |
| "Open the camera" | The live view opens on the HUD and **stays open until you close it** — it never closes by itself after Jarvis answers |
| "Camera full screen" | The picture fills the whole screen (no black bars). A small, light **Jarvis** sits in the bottom-right corner: it pulses and animates while he talks, spins faster while he thinks. What he says is also shown as a caption |
| "Make it smaller" / **Esc** | Back to the small panel |
| "Close the camera" | Closes it and releases the webcam |
| Write on a board or paper → "solve it" / "what's written here?" | Jarvis takes a frame from the live view, reads the task (maths, physics, code, a question) and says the key steps and the answer |

The full-screen button on the camera panel (or a double-click on the picture) does the same as the voice command, and **Esc** leaves full screen.

**Picture quality and speed**

* While the live view is open the camera runs in the biggest size it supports that fits your monitor (up to 1920×1080, otherwise 1280×720), so handwriting is readable. When you close the view it drops back to 640×480.
* Hand tracking and Face ID always get a small 640-pixel picture, so HD does not slow them down.
* In full screen the animated HUD behind the camera is paused, and nothing is converted while the window is minimized.
* Tips for boards: write large, use good light, and keep the board flat to the camera. If part of it is unreadable, Jarvis tells you which part.

<img src="assets/divider.svg" width="100%" alt="">

## Offline mode

Jarvis normally talks to Gemini Live. When the internet is **down or too poor** for a live voice session, it does not spam errors — it quietly switches to **offline mode** and keeps answering local commands. When the line is good again (two good checks in a row) it reconnects by itself.

* **Switching is automatic.** Jarvis checks the connection to the Live server; a dead or very slow line (about 25 s of it during a session) moves you to offline mode. If the line looks fine but Live keeps failing (blocked network, VPN needed), it waits 30 s before trying again.
* **Quiet terminal.** Dropped connections no longer print tracebacks or library log noise. Real problems (a wrong API key, a bug) are still shown.
* **What works offline** (Uzbek, Russian and English, no need to say "Jarvis"): *open / full screen / close the camera* · *what time is it* · *what's the date* · *volume up / down / mute* · *brightness* · *screenshot* · *open Chrome* · *timer 5 minutes* · *remind me in 10 minutes* · *note buy milk* · *2 plus 3* · *battery* · *system status* · *check the internet* · *help*. Things that need the internet ("solve this", translate) get an honest "that needs the internet".
* **Voice offline** uses [Vosk](https://alphacephei.com/vosk/). `pip install vosk` (it is in `requirements.txt`); the small language model downloads **once, in the background, while the internet works**, and then runs fully offline. Without Vosk, type the commands into the input bar — they work the same way.
* **Answers** are shown in the chat and spoken with your system voice (Windows speech, `say` on macOS, `espeak` on Linux). Windows has no Uzbek voice, so spoken Uzbek can sound odd — the text is always shown.

Settings in `config/api_keys.json`:

| Key | Default | Meaning |
| --- | ------- | ------- |
| `offline_auto` | `true` | `false` turns the automatic switch off |
| `offline_lang` | `"uz"` | Vosk language: `uz`, `ru`, `en-us` |
| `offline_stt_path` | — | Path of your own downloaded Vosk model folder |
| `offline_tts` | `true` | `false` = offline answers are text only |

<img src="assets/divider.svg" width="100%" alt="">

## 3D with Blender

Jarvis builds real 3D models in [Blender](https://www.blender.org) from plain language. Blender runs in the background (no window), the project is saved as a `.blend` file and a rendered preview is shown.

| Say | What happens |
| --- | ------------ |
| "Create a medieval castle with four towers" | Gemini writes a short Blender script, Jarvis runs it and renders a preview. If the script fails, the error goes back to Gemini and it is fixed (up to 3 tries); a failed build never touches your project |
| "Make the roof red" · "add a chimney" | Edits the current model — Jarvis sees which objects are in it |
| "Make the wheels metallic" · "move the door left" · "delete the fence" | Direct operations — colour, metal / roughness, glow, transparency, move / scale / rotate, delete (fast, no AI call) |
| "Change the lighting" · "render it from the front" | Lights, background and renders |
| **Image → model:** give a picture (a photo, drawing or screenshot) and say "model this" | Gemini looks at the image and builds a Blender model that copies its subject, proportions, colours and art style |
| "Export it as glb / fbx / obj / stl" | Exports the model (`glb`, `gltf`, `fbx`, `obj`, `stl`) |
| "Open it in Blender" | Opens the `.blend` in the normal Blender window to finish by hand |
| "Undo" · "list my projects" · "switch to castle" | Every change keeps a history; several projects |

Projects live in `Documents/Jarvis/blender/<project>/` (`model.blend`, `renders/`, `exports/`, `history/`).

> The image feature **models** what it sees from a script — it is not photogrammetry. Simple and stylised subjects work best.

**Setup:** install Blender from blender.org. Jarvis finds it in the usual folders; otherwise set `"blender_path": "C:\\Program Files\\Blender Foundation\\Blender 4.2\\blender.exe"` in `config/api_keys.json`.

### 🧩 Speedcubing site

A page just for Rubik's-cube practice, open it by voice ("open my cubing timer", "let me time a solve", "practice OLL") or in a browser at `https://<PC-IP>:8000/cubing`.

* **Timer:** hold Space, release to start, press Space to stop · inspection · scramble generator for **2×2 to 7×7** · **ao5 / ao12** stats and session history.
* **Algorithm trainer:** **OLL (57)** and **PLL (21)** cases, plus F2L; practice mode lets you hide the algorithm and reconstruct it from memory.

<img src="assets/divider.svg" width="100%" alt="">

## Hand Space

<p align="center">
<img src="assets/handspace-demo.svg" alt="Hand Space: a pinch grabs a glass card and carries it across the screen" width="860">
</p>

An Iron-Man style workspace: your drives, folders, pictures, notes, 3D models and videos float on screen as **glass cards**, and you move them with your bare hands. **Webcam only — everything runs locally** and nothing leaves your computer.

Open **Hand Space** from the sidebar and press **Open Hand Space** (or say it). The page also shows live status — whether the workspace is open, or whether the camera needs attention (Settings → Gestures).

### Gestures

| | Gesture | What it does |
| :-: | ------- | ------------ |
| 🤏 | **Pinch** | Touch thumb and index finger on a card to grab it and carry it |
| 👆 | **Tap** | A quick pinch goes into a folder or drive, enlarges a picture, opens a note. Pinch again to close it |
| 🚀 | **Throw** | Let go while your hand moves — the card flies, spins and bounces off the edges |
| 🦅 | **Claw** | Bend your fingers like a claw: every card is pulled to your palm. Open the hand to release |
| 🙌 | **Two hands** | Pinch an open picture with both hands to zoom it; one hand drags it around |
| ✊ | **Back** | Hold a fist for a second: closes the open card, or goes up one folder |

`Esc` or the ✕ in the corner leaves Hand Space. A held fist also stops hand mouse control.

### Your cards

* **Drives first.** Hand Space starts on *This PC* (C: first). **Choose folder…** pins a folder of your own next to the drives; **Use built-in cards** takes it away again.
* **Every kind looks different.** Drives show a usage bar, folders and files get their own icons, pictures show a thumbnail, notes show a peek of their text — each in its own accent colour.
* **＋ New card.** Opens a designer: type a **title** and a **note**, pick one of **8 colours** and one of **12 icons**, and watch a live preview of the glass card. Press **Save card** and it appears in Hand Space.
* **Your look is kept.** The colour and icon are stored at the top of the note's `.md` file (front matter), so the card keeps its own look — and the note stays an ordinary Markdown file you can edit anywhere:

```markdown
---
color: "#ff5c7a"
icon: 🔥
---

# Launch plan

Ship the beta on Friday.
```

The first note creates a home for your cards at `…/hand_space_notes` and pins it automatically. Notes without front matter simply use the default note colour.

### Live cards

Some cards are not files — they show live data and keep updating while Hand Space is open. Open one (pinch it) for the big view; scroll it like any note.

| Card | What it shows | Refresh |
|---|---|---|
| 🌤 **Weather** | Temperature, feels-like, humidity, wind and a 5-day outlook with animated icons | every 10 min |
| 🎵 **Now Playing** | What Spotify is playing, with a spinning disc and equaliser | every 4 s |
| 🖥 **System** | CPU and memory gauges with history graphs, disk, network speed, battery, uptime | every second |
| 🕐 **Clock** | Digital time and an analog dial, date, progress of the day and year | every second |
| 📅 **Calendar** | Meetings grouped by day, with times and places | every 5 min |
| 📬 **Mail** | Unread count and your latest emails (read-only) | every 5 min |
| 💳 **Expenses** | Spent / income / balance, a category donut, bars with budget warnings and the latest entries | every 2 min |

Optional settings in `config/api_keys.json`:

```json
{ "hs_weather_city": "Tashkent", "hs_weather_units": "c" }
```

> [!NOTE]
> **Weather uses the network.** Data comes from [Open-Meteo](https://open-meteo.com/) (free, no key). Without `hs_weather_city` it finds your rough location from your IP address through ipapi.co — set the city if you would rather not. Use `"hs_weather_units": "f"` for °F / mph. **Now Playing** reads Spotify's window title on Windows, so it shows the song only while Spotify is running.

### 🏝 Dynamic Island

A floating glass player sits at the top of your screen — a little below the edge — and stays **above everything, Hand Space included**.

* **Resting:** a small dark pill. Time | weather and an orange dot; while music plays: a round cover, an equaliser and the dot.
* **Hover, click, or a new song:** it opens into the card tinted with the colour of the cover. **Click the orange dot** for the next page: the player (cover, title, artist, a progress bar you can click to seek, ⏮ ⏯ ⏭) → the calendar (the day big, the month with today in red) → clock, date and weather.
* **Pull it down** with the mouse to open it (it follows your hand and stays open if you pull far enough); **pull it up** to shut it. **Shift+drag** (or drag sideways) moves it — the spot is remembered. **Right-click:** open / close, reset position, or hide. Off for good: `"dynamic_island": false`.

It works with **any player** on Windows (Spotify, YouTube in Chrome, VLC…) through the `winrt-*` packages (they are in `requirements.txt` and work on Python 3.14). Without them it falls back to Spotify's window title: title and artist only, no cover or progress.

```bash
pip install winrt-runtime winrt-Windows.Foundation winrt-Windows.Foundation.Collections winrt-Windows.Media.Control winrt-Windows.Storage.Streams
```

Weather and music use the same sources and settings as the [live cards](#live-cards).

### Hand outline

The **Show hand outline** switch on the Hand Space page draws the thin bones of your hand. Off = only the fingertip and pinch rings. Hand Space draws on the graphics card when GPU acceleration is on and falls back to the standard renderer on its own if needed (Settings → Appearance → Performance).

<img src="assets/divider.svg" width="100%" alt="">

## Built-in tools

| Area | Tools — try saying |
| ---- | ------------------ |
| **Computer** | `computer_settings` volume, brightness, dark mode, Wi-Fi · `app_manager` close / **minimize / maximize / restore / focus / snap / tile / next monitor** for a named app, minimize everything, top RAM/CPU apps, startup list · `macros` **modes** (work, game, relax, clean, or your own) · `screen_process` "what does this error mean?" — it looks at your screen and explains · `power_tools` battery, uptime, lock, sleep · `network_tools` IP, Wi-Fi, speed · `storage_analyzer` biggest folders and file types · `file_tools` duplicates and cleanup · `clipboard_tools` · `screen_capture` screenshots and recordings · `appearance_tools` wallpaper |
| **Phone** | `phone_control` — "call Akam" · "call +998 90 123 45 67" · "answer" / "reject" / "hang up" · "who called?" · "find my phone" · "send report.pdf to my phone" · "text 901234567: I'm late" · "lock my phone" · **"unlock my phone"** |
| **Camera & vision** | `screen_process` "what's on my screen?" · "look at the camera" · "solve what I wrote on the board" · `open_camera` / `camera_fullscreen` / `close_camera` — "open the camera", "camera full screen", "close the camera" |
| **3D & creative** | `blender_3d` — "create a 3D pine tree in Blender" · "make the roof red" · "model this picture" (with a reference image) · "export it as glb" · "open it in Blender" · `cubing_timer` — "open my cubing timer", "practice OLL" |
| **Productivity** | `notes_tasks` to-do list and notes · `reminder` · `focus_timer` Pomodoro · `habit_tracker` streaks · `finance_tracker` expenses, income and **receipt photos** · `google_workspace` **Gmail and Calendar** · `study_cards` spaced-repetition flashcards · `text_assistant` translate, summarize, rewrite, fix grammar |
| **Office** | PowerPoint decks · Word documents · Excel workbooks with formulas and charts · PDF merge / split / convert / OCR |
| **Fitness & health** | `pushup_counter` live **workout coach** — push-ups, squats, sit-ups, pull-ups and plank (timed) with form checks; workout plans ("3 sets of 15") with an automatic rest countdown; opens **full screen** with a big animated counter in the top-left corner (say "make it smaller" or press Esc to leave it); a **new-record celebration** (confetti + big number); weekly chart and records on the Dashboard · `calorie_counter` meals by text or photo |
| **Media & games** | `spotify_controller` · `youtube_video` summaries · `play_hud_video` video with sound in the HUD (mpv; by link or just by describing it, full screen with F) · `game_updater` Steam / Epic installs and updates |
| **Info** | `web_search` · `knowledge_lookup` · `weather_report` · `flight_finder` · `utility_tools` calculator, units, live currency |
| **Developer** | `code_helper` write / edit / run code · `dev_agent` multi-file projects |

Each tool is a drop-in file in `actions/`, discovered automatically.

<details>
<summary><b>HUD video player — settings, 👍 👎 🔔 and "Videos"</b></summary>

<br>

Everything lives in the player's own control bar (also in full screen):

| Button | What it does |
| ------ | ------------ |
| ⚙ | **Quality** (Auto or any resolution the video has — switches without losing your place) · **Speed** 0.5×–2× · **Volume** · **Mute** · **Autoplay next video** · **Loop**. Your choices are remembered |
| ▦ **Videos** | Opens a grid of related videos **with thumbnails over the video**. Click one to play it right away, ✕ to go back |
| 👍 / 👎 | Like or dislike the video on your YouTube account (press again to undo) |
| 🔔 | Subscribe to the channel |

**Connecting YouTube — through a browser, no API keys.** The first time you press 👍 / 👎 / 🔔 (or ⚙ → *Connect YouTube*, or say *"connect YouTube"*), a normal Chrome / Edge window opens on Google's sign-in page. Sign in yourself — Jarvis never sees your password; only that browser profile (`~/.jarvis_profiles/youtube`) keeps the session. After that, likes and subscriptions run in a hidden window in a few seconds. Needs `playwright` (already in `requirements.txt`) and Chrome or Edge (or `playwright install chromium`).

**Voice control of the HUD player.** While a video plays you can simply talk to it: *"pause"*, *"resume"*, *"skip 2 minutes"*, *"go back 30 seconds"*, *"play from minute 10"*, *"louder"*, *"set volume to 40"*, *"mute"*, *"speed 1.5"*, *"full screen"*, *"how much is left?"*, *"quality 720"*, *"like this video"*, *"subscribe"*, *"connect YouTube"*, *"next video"*, *"what's up next?"*, *"play the third one"*, *"autoplay on"*, *"loop on"*, *"stop the video"*.

</details>

## New modules

| Module | How to use |
|---|---|
| ✋ **Hand-controlled UI** | Settings → Gestures → *Use my hand as the mouse*, or say "enable hand control". Index finger moves the real cursor · pinch = click / drag · thumb + middle = right click · ✌ and move up/down = scroll · hold a fist 1.5 s = stop. Everything runs locally on the webcam. |
| 🎮 **Game HUD & Voice Trainer** | Say "show the game HUD", "start a Roshan timer 8 minutes repeating", "tip: rotate to B", "coach me every 5 minutes", "start an aim warm-up", "save my keybinds for Valorant: Q dash, E heal". Transparent, always-on-top, click-through overlay; timers are announced by voice 10 s before they end. |
| 🏠 **Local-first smart home** | Say "scan my network", then control Shelly / Tasmota / WLED / Tuya / IP cameras / wake-on-LAN PCs. LAN only: public addresses and HTTP redirects are refused. The phone app can send `{"type":"home","action":"off","target":"room:kitchen"}` over the existing encrypted WebSocket. |
| 🧑‍💻 **Developer overlay** | **Alt+Space** (change with `dev_overlay_hotkey` in `config/api_keys.json`). Live CPU/RAM/GPU, git status · diff · log · pull · push · stash · commit, and "explain the error in my clipboard". |

**Game HUD extras:** the header shows the game's **FPS + frame time** and the **clock** (Settings → Modules). FPS needs the free [PresentMon](https://github.com/GameTechDev/PresentMon/releases) console exe in `tools/` and Jarvis run as Administrator; it only listens to Windows frame events (no injection, anti-cheat safe).

**Face lock:** Settings → Face ID → *Lock Jarvis with my face*. Needs a saved face and a PIN (fallback if the camera fails). Locks on start, on "lock Jarvis", and after N minutes without a saved face; a saved face seen for ~1 s unlocks. While locked, voice, text, tools and phone commands are ignored. Not liveness-checked — a photo may fool it.

No new Python packages are needed (`tinytuya` is only used for Tuya devices and is already in `requirements.txt`).

<img src="assets/divider.svg" width="100%" alt="">

## Receipts, Gmail, gestures and Face ID

<table>
<tr>
<td width="33%" valign="top">

### 🧾 Receipt → expense
Attach a photo of a receipt or bill and say *"record this receipt"* / *"chekni yoz"*.
Gemini reads the **total, shop, date, currency and category** and saves it to `finance_tracker`.

</td>
<td width="33%" valign="top">

### 📬 Gmail & Calendar
*"Bugun qanday xatlar keldi?"*
*"Juma kuni soat 15:00 ga uchrashuv qo'y"*
Read mail, check your agenda, add or cancel events.

</td>
<td width="33%" valign="top">

### 🖐️ Hand gestures
Show your hand to the webcam to pause music, change volume, mute the mic or take a screenshot.
**Off by default** — you choose what each gesture does.

</td>
</tr>
</table>

<details>
<summary><b>🧾 Receipt scanner</b></summary>

<br>

1. Click the **paperclip** (or drag & drop) and attach the receipt photo.
2. Say or type: *"record this receipt"*.
3. Jarvis answers with what it read, e.g. `Receipt recorded: 125,000 UZS · Food · Korzinka · 2026-11-01`.

| Good to know | |
| ------------ | --- |
| Reads | Total paid (not subtotal or change), shop name, date, currency, category — in Uzbek, Russian, English and more |
| Wrong result? | Say *"remove the last entry"* — or just tell Jarvis the right amount |
| Budgets | The usual over-budget warnings still apply |
| Unreadable photo | Jarvis says so and saves nothing — retake it flat and well lit |

</details>

<details>
<summary><b>📬 Gmail & Google Calendar</b></summary>

<br>

**One-time setup** (about 5 minutes, free):

1. Open [Google Cloud Console](https://console.cloud.google.com/) → create a project → enable **Gmail API** and **Google Calendar API**.
2. *APIs & Services → Credentials → Create credentials → OAuth client ID → **Desktop app*** → download the JSON.
3. Save it as `config/google_credentials.json`.
4. Say **"connect Google"** — a browser opens once; approve access. Done.

| Say | What happens |
| --- | ------------ |
| "Bugun qanday xatlar keldi?" / "What emails came today?" | Lists the last 24 h of mail, unread marked with ● |
| "Show unread emails" | Unread inbox |
| "Find the email from Amazon" | Gmail search (`from:`, `newer_than:` … all work) |
| "Read the second email" | Shows the message text |
| "Bugun rejalarim?" / "What's on tomorrow?" | Calendar agenda for a day or several days |
| "Juma kuni soat 15:00 ga uchrashuv qo'y" | Adds a 1-hour event; warns if the slot overlaps another |
| "Cancel Friday's meeting" | Removes the event |

Days understood: `bugun`, `ertaga`, `juma`, `friday`, `06.11`, `2026-11-06` and more.

> [!IMPORTANT]
> **Mail is read-only** — Jarvis cannot send or delete emails. Calendar can read, add and delete events.
> The sign-in token is stored in `config/google_token.json` (owner-only) and never leaves your PC.

</details>

<details>
<summary><b>🖐️ Hand gestures (media, volume, mic…)</b></summary>

<br>

Open **Settings → Gestures**, switch **Enable gesture control** on, and pick an action for each gesture.
Hold the gesture for a moment — quick wave-bys are ignored. Choose the **Response speed** that suits you: ⚡ Fast (~0.3 s), Normal (~0.45 s) or 🎯 Careful (~0.7 s).

| Gesture | Default action |
| ------- | -------------- |
| ✋ Open palm | Play / pause media |
| ✊ Fist | Mute / unmute microphone |
| 👍 Thumbs up | Volume up (repeats while held) |
| 👎 Thumbs down | Volume down (repeats while held) |
| ✌ Two fingers | Take a screenshot |
| ☝ Index finger | Next track |
| 🤟 Three fingers | Previous track |

**Available actions:** play / pause · next / previous track · volume up / down / mute · mute microphone · sleep / wake assistant · screenshot · open Settings · fullscreen · or **Nothing** to disable a gesture.

* **Off by default.** The camera is used only while the switch is on; switching it off releases it immediately.
* **Private.** Frames are processed on your PC by MediaPipe — nothing is recorded or uploaded.
* Detection is rotation-proof (it works with a tilted hand) and adapts to how far you are from the camera.
* The first start downloads a small hand model (~8 MB) to `config/models/`. Needs `opencv-python` and `mediapipe` (already in `requirements.txt`).
* Wrong camera? Pick another one in Settings → Gestures → Camera. **Reset to defaults** restores the table above.
* Settings are saved in `config/api_keys.json` (`gesture_enabled`, `gesture_map`, `gesture_camera`).

</details>

<details>
<summary><b>🙂 Face ID</b></summary>

<br>

**Settings → Face ID** → switch **Enable face recognition** on, type a name and press **Add my face**; look at the camera for a few seconds.

| Option | What it does |
| ------ | ------------ |
| Greet by voice | Jarvis says hello by name when a saved person shows up (not again for 45 s) |
| Alert on unknown faces | A red **⚠ UNKNOWN PERSON** card appears in the middle of the HUD for ~4 s, then Jarvis warns you out loud |
| Saved people | Remove one person, or delete all saved faces |

Voice commands: *"remember my face as Akmal"* · *"who is in front of the camera?"* · *"whose faces do you know?"* · *"forget Akmal"*.

* **Off by default**, and the camera is released the moment you switch it off. Gestures and Face ID share one camera, so you can use both at once.
* **Private.** Only 128-number face fingerprints are saved in `memory/faces.json` — no photos — and nothing leaves your PC.
* The first start downloads two small models (~37 MB, OpenCV YuNet + SFace) to `config/models/`. Needs `opencv-python` 4.8+ (already in `requirements.txt`).
* It is a convenience feature, **not a security lock** — a photo of a person can fool any webcam-based recogniser.

</details>

<img src="assets/divider.svg" width="100%" alt="">

## 3D HUD models

The centre of the home screen shows an animated 3D model. Switch it in **Settings → Appearance** (or double-click it).
Built-in: **Holo** (golden hologram sphere), **Crystal**, **Globe**, **Knot**, **Helix** and **Face**.

Models are plain `.obj` files in `assets/models/`. Drop your own file there and it appears in the list after a restart.
Layers are OBJ groups named `kind:key=value,...`, for example:

```
g lines:w=1.5,a=1,mix=.3,spin=.6,add=1
l 1 2 3 4
g points:size=6,mix=.5,scan=lon
p 1 2 3
g faces:amp=.16,spec=1
f 1 2 3
```

Kinds: `lines`, `points`, `faces`, `sparks`, `pulse`. Useful keys: `w` width, `a` opacity, `mix` colour blend (0 = main, 1 = accent),
`spin` rotation speed (negative = reverse), `tilt`, `scale`, `amp` (grows with voice), `blink`, `add` (glow blending), `lite=0` (hidden in lightweight mode).
File-level options use `#@hud 1`, `#@glow 1`, `#@rim 1`, `#@palette gold`. The built-in models are generated by `python tools/make_models.py`.

## Tool setup notes

<details>
<summary><b>Memory, GPU, HUD video, Spotify and other tool requirements</b></summary>

<br>

* **Memory:** heavy tools (PowerPoint, Word, PDF, Excel, push-up counter) are loaded only when you ask for them. At startup only a tiny declaration file is read; the libraries (`python-pptx`, `python-docx`, `openpyxl`, `pypdf`, `mediapipe`, OpenCV) are imported on first use. To make your own action lazy, keep `TOOL` in a small file and import the heavy code inside the handler.
* **GPU hologram:** with GPU acceleration on, the Holo model is drawn by a shader on the graphics card. If the shader cannot run, Jarvis checks itself and switches to the standard renderer automatically (Settings → Appearance → Performance).
* **Profiles:** Settings → General → Profile (or "switch to work mode") changes the 3D model, push-to-talk / open mic and graphics quality: Home = Holo, Work = Crystal, Game = Globe + lightweight.
* **HUD video (`play_hud_video`)** uses [mpv](https://mpv.io): `pip install python-mpv` (already in `requirements.txt`) plus the libmpv library. Windows: download libmpv from <https://sourceforge.net/projects/mpv-player-windows/files/libmpv/> and copy `libmpv-2.dll` (or `mpv-2.dll`) into the Jarvis folder next to `main.py`. Linux: `sudo apt install libmpv2`. macOS: `brew install mpv`. Say "play a good Minecraft video" or give a YouTube link. In the video: Space pause, ←/→ seek, ↑/↓ volume, F / F11 / double-click full screen, Esc leaves full screen.
* **Workouts:** say "let's do squats", "plank for 60 seconds", "today 3 sets of 15 push-ups, rest 45 seconds" or "pull-ups". Jarvis runs the sets one after another and counts the rest down on screen ("skip rest" ends it early). Plank shows a big m:ss clock. Every finished workout is saved to `memory/workouts.json`; the **Dashboard → Workouts** card shows a 7-day bar chart, your personal records and your day streak. Beating your best total plays a full-screen record animation (needs at least one earlier session of that exercise). On a wide screen with a 4:3 camera, two side panels fill the free strips beside the picture: **today** (daily-goal ring, streak, sets done, record to beat) on the left and **technique** (live angle gauge, form verdict, one bar per rep) on the right; the goals are `DAILY_GOAL_REPS` / `DAILY_GOAL_PLANK` in `core/workout_stats.py`. Squats / sit-ups / push-ups work best from the side, pull-ups facing the camera.
* **Workout counter** needs `opencv-python` and `mediapipe`. It starts full screen (say "start push-ups, not full screen" to keep the small panel); closing the view ends the workout. On first use it downloads a small pose model (about 6 MB) to `config/models/`. Place the camera at your side so your whole body is visible.
* **Gmail & Calendar** need a Google OAuth client — see [Receipts, Gmail, gestures and Face ID](#receipts-gmail-gestures-and-face-id). `google-api-python-client` and `google-auth-oauthlib` are already in `requirements.txt`.
* **Receipt scanner** uses your Gemini key — no extra setup.
* **Blender (`blender_3d`)** needs [Blender](https://www.blender.org) installed — see [3D with Blender](#3d-with-blender). Modelling uses your Gemini key.
* **Offline voice** needs `vosk` (in `requirements.txt`); its small model downloads once while online — see [Offline mode](#offline-mode).
* **Live camera** needs `opencv-python` and a webcam; Gestures, Face ID and the live view share one camera — see [Live camera](#live-camera).
* **PDF OCR** needs the free [Tesseract](https://github.com/tesseract-ocr/tesseract) program installed. Converting Word/PowerPoint/Excel to PDF needs [LibreOffice](https://www.libreoffice.org) (or Microsoft Word with `docx2pdf` on Windows).
* **Spotify** works out of the box with the desktop app (media keys, volume, search page). For one-step "play my chill playlist", add `spotify_client_id` and `spotify_client_secret` (free, from developer.spotify.com/dashboard) to `config/api_keys.json`, register `http://127.0.0.1:8888/callback` as the Redirect URI, then say "log in to Spotify" once.
* Generated files are saved under `Documents/Jarvis/` (change with `"output_dir"` in `config/api_keys.json`). Workout and nutrition logs live in `memory/`.

</details>

<img src="assets/divider.svg" width="100%" alt="">

## Phone connection

Jarvis connects **out** from the phone to your PC (reverse WebSocket), so there is nothing to forward and no ADB.

### Option A — Android APK (recommended)

<p align="center">
<a href="https://github.com/ASDprogrammer521/Jarvis-ai/releases/latest">
<img src="https://img.shields.io/badge/Download-Jarvis%20APK-3DDC84?style=for-the-badge&logo=android&logoColor=white" alt="Download APK">
</a>
</p>

1. Install the APK on your phone (allow install from unknown sources if needed).
2. On first open, allow **notifications**, **phone / calls**, **call log**, **contacts**, **SMS**, **location**, **mic** and **camera** as prompted.
3. Start Jarvis on the PC and get a **fresh pairing key** (Remote Control / Dashboard).
4. In the app: enter **PC IP** + **key** → **Connect**.
5. The pill in the corner turns **● ONLINE** and a persistent **Jarvis Connected** notification appears.
6. Optional: **Enable lock permission** so Jarvis can lock the screen.

**Build the APK yourself:** open `android/JarvisApp` in Android Studio, or push to GitHub → **Actions** → **Build Jarvis App APK** → download the `JarvisApp-debug` artifact.

<details>
<summary><b>What the app contains</b></summary>

<br>

* **Header** — live status pill (online / connecting / offline).
* **Phone card** — current call state (refreshed every two seconds), a big **Make a call** button, and **Answer / Reject / Hang up**.
* **Dialer** — bottom sheet with a full keypad, long-press `0` for `+`, **Paste**, backspace (long-press clears) and redial of the last number.
* **Quick actions** — YouTube, Lock, Home, Notifications, Location, Camera, Voice, Torch, Screenshot, **Find phone**, **Contacts**, **Send file**.
* **Control the PC** — lock, mute, volume, play / pause / next / previous, **App…** (minimize, maximize, bring forward or close any app by name) and shut down (asks for confirmation).
* **Link line** — 🔒 shows the link is encrypted and the certificate is pinned; **Forget PC certificate** is for after you reinstall Jarvis.
* **Activity log** and a chat bar with file attach.

</details>

### Phone calls

| From | How |
| ---- | --- |
| **The phone** | Tap **Make a call**, type or paste a number, press the green button. |
| **Your voice, on the PC** | "Call +998 90 123 45 67" → the PC tells the phone to dial. Jarvis needs a **number**; it will ask if you only give a name. |
| **By name** | "Call Akam" — the phone searches its contacts. If two people match, Jarvis asks which one. |
| **Incoming calls** | The PC shows a banner (Phone page, plus a pop-up), Jarvis tells you who is calling and asks: *answer* or *reject*? |
| **SMS** | "Text 901234567: I'll be there in ten minutes" |

Caller names need **Contacts** and caller numbers need **Call log** (Android 9+ hides the number without it). Calls need the **Phone** permission. Without it Jarvis opens the dialer with the number filled in instead of dialling. Answer / reject / hang up need **Answer phone calls** (Android 8+); on some phones the system dialer may still refuse to be controlled.

### Phone unlock

Say **"unlock my phone"** and the Jarvis App unlocks the screen the way you would: it swipes up, then **draws your pattern, taps your PIN or types your password**.

**One-time setup on the phone**

1. Open **Jarvis App → Unlock setup**.
2. Choose how your phone unlocks — **Pattern**, **PIN** or **Password** — and enter it once.
3. Turn on **Accessibility → Jarvis phone unlock**. If Android says *"Restricted setting"*: Settings → Apps → Jarvis App → ⋮ → *Allow restricted settings*, then turn it on again.

**How it stays safe**

* The code is encrypted with a **non-exportable Android Keystore key** and stored **only on the phone**. It is never sent to the PC or over the network.
* The phone acts **only** when the paired PC sends an `unlock` command over the encrypted link.
* Before typing a PIN, the app checks that every digit key is on screen, so it never types half a code. It then checks the result and reports whether the phone really unlocked.

> Fingerprint / face-only unlock cannot be entered by an app, and some phone makers restrict accessibility gestures on the lock screen. If your phone refuses, Jarvis tells you why instead of failing silently.

### Option B — Browser page (no install)

```text
https://<PC-IP>:8000/jarvis-app
```

Same Wi‑Fi required. Enter the pairing key (or scan the QR code from Remote Control). The page lets you:

* chat with Jarvis and send quick commands (status, mute, unmute);
* read Jarvis's replies, notifications and links.

> [!WARNING]
> **Calls are not available in the browser.** A web page cannot place, answer, reject or hang up phone calls — and has no access to contacts or the call log. Use the Android APK (Option A) for calling, SMS, incoming-call alerts and file transfer.

### Phone capabilities (Android app)

| Capability | Notes |
| ---------- | ----- |
| Calls and SMS | Dial by number or name, answer, reject, hang up, call state, incoming-call alerts, send SMS |
| Chat with Jarvis | Type in the bottom bar and send |
| Files, phone → PC | **+** or **Send file** — any size (up to the server limit) over the encrypted link; saved in the dashboard uploads folder |
| Files, PC → phone | "Send report.pdf to my phone" — a one-file link that expires in 15 minutes; the file lands in `Downloads/Jarvis` |
| Unlock | "Unlock my phone" — the phone draws your pattern / taps your PIN / types your password (set up once in **Unlock setup**; stored only on the phone — see [Phone unlock](#phone-unlock)) |
| Find my phone | Rings on the alarm channel at full volume (even when silent) for up to 90 s; "stop ringing" or the tile stops it |
| Quick actions | YouTube, Lock, Home, Notifs, Location, Camera, Voice, Torch, Screenshot |
| Message previews | Enable **Notification access**; SMS, WhatsApp and Telegram previews show in the Phone section on the PC (read-only — no replies, SMS storage is never read) |
| Phone status | Name, battery and charging state reported every five minutes |
| Voice to PC | **Voice** uses on-device speech recognition |
| PC Lock / Shutdown | Secure control commands to the PC |
| Auto-reconnect | The service retries the link if the socket drops |
| Background link | A foreground notification keeps the connection alive |

<details>
<summary><b>Do I need a certificate?</b></summary>

<br>

**No — you do not need to buy, create or install anything.** Jarvis handles it for you:

| Question | Answer |
| -------- | ------ |
| Who creates the certificate? | Jarvis, automatically, the first time the dashboard starts (`config/certs/`). It is generated on *your* PC, so every install has its own key. |
| Is it a "real" (CA-signed) certificate? | No. It is **self-signed**, which is fine for a private LAN link. A public certificate (Let's Encrypt etc.) needs a domain name and is meant for websites on the internet — not for `192.168.x.x`. |
| Does the Android app need it? | The app pins the certificate's SHA-256 fingerprint the **first time** it pairs (trust on first use). Nothing to install on the phone. |
| Does the browser need it? | Browsers show a **warning once** because the certificate is self-signed. Compare the SHA-256 fingerprint with the one shown in Jarvis → Phone, then continue. |
| What does it need to work? | The `cryptography` Python package (installed by `setup.py`). Without it Jarvis falls back to plain HTTP and prints a warning. |
| Can I turn it off? | Yes: set `JARVIS_TLS=0` (see `config/env.example`). The link then becomes **unencrypted** — use only on a network you fully trust. |
| When is a new one created? | When your PC's LAN IP changes, or if you delete `config/certs/`. Then tap **Forget PC certificate** in the app and pair again. |

</details>

<details>
<summary><b>Troubleshooting</b></summary>

<br>

| Problem | Fix |
| ------- | --- |
| Can't open the page | Test on the PC first: `https://127.0.0.1:8000/jarvis-app` (accept the warning once). |
| Phone can't reach the PC | Allow port **8000** in Windows Firewall, and use the same Wi‑Fi (not a guest network with client isolation). |
| "Invalid or expired key" | Pairing keys last 10 minutes and work once. Get a fresh one from Remote Control. |
| "Certificate changed" in the app | You reinstalled Jarvis or your PC's IP changed → tap **Forget PC certificate** and connect again. If you changed nothing, treat it as a warning. |
| Link keeps dropping | Set Jarvis App to **Unrestricted** battery use. |
| A call only opens the dialer | Grant the **Phone** permission: Android → Apps → Jarvis App → Permissions. |
| Need plain HTTP on a trusted network | Set `JARVIS_TLS=0` before starting Jarvis (not recommended). |

> ADB is **not** required — the link is the Jarvis App's reverse WebSocket.

</details>

<img src="assets/divider.svg" width="100%" alt="">

## UI navigation

There is no top bar — the whole window is the page. Navigation lives in a slim **side rail** on the left:

* At rest it shows **icons only** (plus a status dot, the time and the fullscreen / compact-mode controls).
* **Move the mouse onto it** and it slides open with the labels, the date and the version; move away and it folds back.
* The microphone state (**Live / Muted / Listening / Speaking …**) is the dot at the bottom of the rail; it shows its name when the rail is open.

| Item | What it does |
| --- | --- |
| **Home** | Main holographic HUD with the **Ask anything** command bar |
| **Chat** | Conversation history |
| **Dashboard** | System stats, tasks, activity and music |
| **Phone** | Phone Link-style page: device card with battery and link status, three big actions (Find phone · Lock · Screenshot), a **Notifications** list (Call / Mark as read / Clear all) and **Messages · Calls · Actions** tabs |
| **Hand Space** | Launch the gesture workspace, pin a folder, design new cards |
| **Voice & AI** / **Settings** | Full-screen options |

**Shortcuts:** `F4` mute · `F11` fullscreen · `F12` compact mode

**Window commands:** say the app's name — "minimize Discord", "maximize Chrome", "restore Spotify", "bring Steam to the front". Jarvis finds that app's own window; it never minimizes itself by mistake. Without a name, minimize / maximize act on the focused window — which is Jarvis while you talk to it — so it refuses and asks which app you mean.

## Profiles & plugins

**Profiles** (`home` / `work` / `game`) store preferred HUD and talk-mode style. Ask Jarvis to list or switch profiles, or use the `profile_switch` tool.

**Plugin store:** drop a `.py` file into `plugins/`, then list / enable / disable via the `plugin_store` tool (or Settings plugins UI where available).

## Project structure

```text
Jarvis-ai/
├── main.py                 # entry point
├── ui/                     # window, pages, 3D stage, Hand Space, settings, theme
├── assets/                 # banner, animated README art
│   └── models/             # 3D HUD models (.obj)
├── tools/make_models.py    # regenerates the built-in .obj models
├── setup.py                # dependency installer
├── Jarvis.spec             # PyInstaller (Windows EXE)
├── requirements.txt        # the only requirements file
├── actions/                # built-in tools
├── plugins/                # drop-in plugins
├── core/                   # avatar, audio, LLM, updater, camera hub (live view + gestures + Face ID), offline mode, Hand Space, live card feeds…
├── dashboard/              # remote server + web companion (+ static/cubing.html — the speedcubing site)
├── android/JarvisApp/      # native Android companion (Kotlin) — dialer, calls, quick actions
├── scripts/build_exe.ps1   # local Windows packaging
├── memory/                 # config + long-term memory
├── config/                 # API keys, certificates
└── .github/workflows/      # APK + Windows EXE releases
```

<img src="assets/divider.svg" width="100%" alt="">

### Smart nudges (proactive Jarvis)

Jarvis can speak up on its own — a toast on screen and, if you want, one short spoken sentence:

| Nudge | When |
|---|---|
| 📅 Upcoming meeting | a Google Calendar event starts in N minutes (default 15; needs Google connected) |
| 🔋 Low battery | battery at or below N % (default 15) and not charging |
| 💪 Workout reminder | nothing logged today and it is N o'clock or later (default 18:00) |
| 🔥 Streak at risk | your streak of 2+ days ends tonight (default from 21:00) |

Everything is optional: **Settings → Nudges** has a switch and a value for each one, *say them aloud*, **quiet hours** (default 23:00–07:00) and *pause for 1 / 4 hours*. By voice: "turn off the battery reminders", "remind me about meetings 10 minutes before", "be quiet for an hour". A nudge is never repeated, never interrupts while Jarvis is talking (it waits, then falls back to a toast), and at most one is spoken per check. The engine is `core/nudges.py`; its settings live under `nudges` in `config/api_keys.json`.

### Look & feel

* **Themes:** Settings → Appearance → *Theme* switches the whole palette instantly — **Jarvis**, **Iron Man**, **Neon**, **Minimal** and **Emerald**. The accent picker still works and replaces the theme with your own colour. The choice is saved in `config/api_keys.json` (`ui_theme`, `ui_color`).
* **Design tokens:** corner radii, spacing, type sizes and animation times live in one place, `ui/theme.py` (`T.R_MD`, `T.S4`, `T.D_BASE` …), together with the colours (`C`) and two QSS helpers (`card_css()`, `button_css()`). Build new widgets from these so they match everything else.
* **Notifications:** every message goes through `ui/toasts.py` (`ToastCenter`): they slide up from the bottom, stack (max four, the oldest fades out), an identical message is not shown twice, and the colour follows the meaning (✅ green, ⚠ amber, ⬆ violet).
* **Transitions:** switching pages fades in over about 200 ms.
* **Full-screen camera:** soft shading at the top and bottom, thin viewfinder corners and a LIVE badge (picture size and frame rate); the mini Jarvis sits bottom-right.
* **One camera:** the workout counter, Face ID, hand gestures and the camera view share a single capture (`CameraHub`) — two programs opening the same webcam is what caused the OpenCV "Unknown C++ exception" on Windows.

## Security

* **Encrypted link.** The dashboard serves HTTPS and the app connects over WSS. Jarvis creates a self-signed certificate in `config/certs/` automatically (and a new one if your PC's LAN address changes). The private key is never shipped with the project. The Android app pins its SHA-256 fingerprint the first time it pairs and refuses any other certificate afterwards — it never silently drops back to plain HTTP once a certificate is pinned.
* **Pairing key.** A one-time key (valid ten minutes) turns into a session token; "revoke devices" ends all sessions.
* **Confirmations.** Shutdown, restart and outgoing messages need your click on the PC. A shutdown asked for from the phone starts a 15-second countdown (`shutdown /a` cancels it).
* **Google & camera.** Gmail access is read-only; the Google token lives in `config/google_token.json` (owner-only). Hand gestures, Hand Space and Face ID are off until you enable them, process the camera locally and store no photos.
* **Phone unlock.** The phone's unlock code is encrypted with a non-exportable Android Keystore key and never leaves the phone; unlocking happens only on an `unlock` command from the paired PC.
* **Offline mode.** Offline speech recognition (Vosk) and the offline commands run entirely on your PC; nothing is sent anywhere. The camera view is processed locally and no pictures are stored — a frame goes to Gemini only when you ask Jarvis to look (for example "solve it").
* **Files.** PC → phone transfers are single-file links that expire; keys, certificates and `api_keys.json` are never sent.

## License

Released under the **MIT License**.

<img src="assets/divider.svg" width="100%" alt="">

<div align="center">

**Jarvis AI** · made with care by **ASDcuber**

<sub>If Jarvis saves you time, a ⭐ on the repo means a lot.</sub>

</div>
