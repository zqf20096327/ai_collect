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

**[Download](#download)** · **[Quick start](#quick-start)** · **[Features](#features)** · **[Hand Space](#hand-space)** · **[Tools](#built-in-tools)** · **[Phone](#phone-connection)** · **[Security](#security)**

</div>

<img src="assets/divider.svg" width="100%" alt="">

## Overview

**Jarvis AI** is an intelligent assistant that automates your workflow and simplifies everyday computer tasks. A clean, modern interface sits on top of serious tools: **voice control, screen awareness, desktop automation, a holographic HUD, hand-controlled Hand Space, profiles, plugins and a full phone companion** — one system, version **5.x**.

<table>
<tr>
<td width="25%" valign="top" align="center"><h3>🎙️ Voice</h3>Push-to-talk, open mic and an optional local <i>"Hey Jarvis"</i> wake word.</td>
<td width="25%" valign="top" align="center"><h3>👁️ Vision</h3>Reads your screen, scans receipts, recognises faces and hands through the webcam.</td>
<td width="25%" valign="top" align="center"><h3>🖥️ Control</h3>Apps, windows, files, browser, system settings, Gmail and Calendar — by voice or text.</td>
<td width="25%" valign="top" align="center"><h3>📱 Phone</h3>Native Android app: calls, SMS, find my phone, big file transfer — over an encrypted link.</td>
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
| 🎙️ **Voice + wake word** | Push-to-talk, open mic, mute, optional local "Hey Jarvis" wake word |
| 📱 **Jarvis App (phone)** | Native Android app — **call by name or number**, incoming-call alerts on the PC, find my phone, big file transfer, SMS, lock, locate — no ADB. A lightweight browser page covers chat and basic commands |
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

### Hand outline

The **Show hand outline** switch on the Hand Space page draws the thin bones of your hand. Off = only the fingertip and pinch rings. Hand Space draws on the graphics card when GPU acceleration is on and falls back to the standard renderer on its own if needed (Settings → Appearance → Performance).

<img src="assets/divider.svg" width="100%" alt="">

## Built-in tools

| Area | Tools — try saying |
| ---- | ------------------ |
| **Computer** | `computer_settings` volume, brightness, dark mode, Wi-Fi · `app_manager` close / **minimize / maximize / restore / focus / snap / tile / next monitor** for a named app, minimize everything, top RAM/CPU apps, startup list · `macros` **modes** (work, game, relax, clean, or your own) · `screen_process` "what does this error mean?" — it looks at your screen and explains · `power_tools` battery, uptime, lock, sleep · `network_tools` IP, Wi-Fi, speed · `storage_analyzer` biggest folders and file types · `file_tools` duplicates and cleanup · `clipboard_tools` · `screen_capture` screenshots and recordings · `appearance_tools` wallpaper |
| **Phone** | `phone_control` — "call Akam" · "call +998 90 123 45 67" · "answer" / "reject" / "hang up" · "who called?" · "find my phone" · "send report.pdf to my phone" · "text 901234567: I'm late" · "lock my phone" |
| **Productivity** | `notes_tasks` to-do list and notes · `reminder` · `focus_timer` Pomodoro · `habit_tracker` streaks · `finance_tracker` expenses, income and **receipt photos** · `google_workspace` **Gmail and Calendar** · `study_cards` spaced-repetition flashcards · `text_assistant` translate, summarize, rewrite, fix grammar |
| **Office** | PowerPoint decks · Word documents · Excel workbooks with formulas and charts · PDF merge / split / convert / OCR |
| **Fitness & health** | `pushup_counter` webcam rep counting with form checks · `calorie_counter` meals by text or photo |
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
* **Push-up counter** needs `opencv-python` and `mediapipe`. On first use it downloads a small pose model (about 6 MB) to `config/models/`. Place the camera at your side so your whole body is visible.
* **Gmail & Calendar** need a Google OAuth client — see [Receipts, Gmail, gestures and Face ID](#receipts-gmail-gestures-and-face-id). `google-api-python-client` and `google-auth-oauthlib` are already in `requirements.txt`.
* **Receipt scanner** uses your Gemini key — no extra setup.
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
├── core/                   # avatar, audio, LLM, updater, camera hub (gestures + Face ID), Hand Space…
├── dashboard/              # remote server + web companion
├── android/JarvisApp/      # native Android companion (Kotlin) — dialer, calls, quick actions
├── scripts/build_exe.ps1   # local Windows packaging
├── memory/                 # config + long-term memory
├── config/                 # API keys, certificates
└── .github/workflows/      # APK + Windows EXE releases
```

<img src="assets/divider.svg" width="100%" alt="">

## Security

* **Encrypted link.** The dashboard serves HTTPS and the app connects over WSS. Jarvis creates a self-signed certificate in `config/certs/` automatically (and a new one if your PC's LAN address changes). The private key is never shipped with the project. The Android app pins its SHA-256 fingerprint the first time it pairs and refuses any other certificate afterwards — it never silently drops back to plain HTTP once a certificate is pinned.
* **Pairing key.** A one-time key (valid ten minutes) turns into a session token; "revoke devices" ends all sessions.
* **Confirmations.** Shutdown, restart and outgoing messages need your click on the PC. A shutdown asked for from the phone starts a 15-second countdown (`shutdown /a` cancels it).
* **Google & camera.** Gmail access is read-only; the Google token lives in `config/google_token.json` (owner-only). Hand gestures, Hand Space and Face ID are off until you enable them, process the camera locally and store no photos.
* **Files.** PC → phone transfers are single-file links that expire; keys, certificates and `api_keys.json` are never sent.

## License

Released under the **MIT License**.

<img src="assets/divider.svg" width="100%" alt="">

<div align="center">

**Jarvis AI** · made with care by **ASDcuber**

<sub>If Jarvis saves you time, a ⭐ on the repo means a lot.</sub>

</div>
