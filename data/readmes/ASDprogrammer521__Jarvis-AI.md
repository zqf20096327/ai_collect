<div align="center">

# 🤖 Jarvis AI

**Talk to your PC. It listens, and it gets things done.**

A voice assistant for Windows and Android, powered by Google Gemini.
Open apps, read your screen, drive the browser, write documents, even call people from your phone.

[![Latest release](https://img.shields.io/github/v/release/ASDprogrammer521/Jarvis-ai?style=for-the-badge&color=00d4ff&label=release)](https://github.com/ASDprogrammer521/Jarvis-ai/releases/latest)
[![Stars](https://img.shields.io/github/stars/ASDprogrammer521/Jarvis-ai?style=for-the-badge&color=ffb703)](https://github.com/ASDprogrammer521/Jarvis-ai/stargazers)
[![License: MIT](https://img.shields.io/badge/license-MIT-2ea44f?style=for-the-badge)](#-license)
[![Python](https://img.shields.io/badge/python-3.11%2B-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Discord](https://img.shields.io/badge/discord-join-5865f2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/invite/r5q93NpRPt)

[💻 **Download for Windows**](https://github.com/ASDprogrammer521/Jarvis-ai/releases/latest) &nbsp;·&nbsp;
[📱 **Download for Android**](https://github.com/ASDprogrammer521/Jarvis-ai/releases/latest) &nbsp;·&nbsp;
[💬 **Join the Discord**](https://discord.com/invite/r5q93NpRPt)

</div>

---

Jarvis is a desktop app that you simply talk to. Say what you want and it does it: it launches programs, looks at your screen, controls Chrome, builds Word, Excel and PowerPoint files, manages your calendar, and rings your phone when you've lost it. Gemini is the brain; everything else runs on your machine.

I build it in my free time. If it saves you a few minutes, a ⭐ on the repo genuinely makes my day.

> Running from source? You'll need **Python 3.11 or newer**. Released under the **MIT license**. Made by **ASDcuber**.

## 📑 Contents

- [🚀 Getting started](#-getting-started)
- [✨ What's new](#-whats-new)
- [🧠 What Jarvis can do](#-what-jarvis-can-do)
- [🎤 Voice, camera and offline mode](#-voice-camera-and-offline-mode)
- [✋ Hand Space and Dynamic Island](#-hand-space-and-dynamic-island)
- [🧊 3D with Blender](#-3d-with-blender)
- [📬 Gmail, Calendar, gestures and Face ID](#-gmail-calendar-gestures-and-face-id)
- [📱 Phone connection](#-phone-connection)
- [🎨 Looks and settings](#-looks-and-settings)
- [📂 Project layout](#-project-layout)
- [🔒 Security](#-security)
- [📄 License](#-license)

## 🚀 Getting started

**The easy way (Windows)**

1. Open the [latest release](https://github.com/ASDprogrammer521/Jarvis-ai/releases/latest).
2. Download `Jarvis-Windows-x64-v*.zip` and unzip it.
3. Run `Jarvis.exe`.
4. Paste your Gemini API key when it asks.

> 🛡️ Windows may show a SmartScreen warning because the build isn't code-signed. Click **More info → Run anyway**.

**From source**

```bash
python setup.py     # installs everything from requirements.txt
python main.py
```

On first launch Jarvis asks for your Gemini API key. You can also drop it into `config/api_keys.json` yourself.

<details>
<summary>🔧 Building the EXE yourself</summary>

```powershell
powershell -ExecutionPolicy Bypass -File scripts\build_exe.ps1
```

To publish a release, push a tag (`git tag v1.0.1`, then `git push origin v1.0.1`) or run **Actions → Build Windows EXE + Release** by hand.
</details>

## ✨ What's new

- 🎨 **10 themes.** Jarvis, Iron Man, Neon, Minimal, Emerald, Sunset, Arc Reactor, Matrix, Sakura and Daylight. There's also **Automatic day / night**: Daylight from 07:00 to 19:00, then your own theme in the evening.
- 🎬 **Boot intro.** A short start-up sequence when Jarvis opens. Click or press any key to skip it, or turn it off in Settings.
- 🔊 **Voice ring.** A ring around the 3D model that moves with Jarvis' voice and mouth shapes while he talks.
- 💬 **A better chat.** Markdown, code blocks with a Copy button, a "typing…" animation, image and file previews, and 👍 👎 ❤️ reactions.
- 🔐 **Security fix.** The connection check now requires TLS 1.2 or newer.

## 🧠 What Jarvis can do

Just say it, or type it. Here are the main areas.

| Area | Examples |
| ---- | -------- |
| 🖥️ **Computer** | Volume, brightness, dark mode, Wi-Fi. Minimize, maximize, snap or close a named app ("minimize Discord", "Chrome and Discord side by side"). Battery, uptime, lock, sleep. Biggest folders, duplicate files, clipboard, screenshots, wallpaper. |
| 🎛️ **Modes** | "Work mode" opens and arranges a whole set-up. You can save your own by voice. |
| 👀 **Screen and camera** | "What's on my screen?", "what does this error mean?", "look at the camera", "solve what I wrote on the board". |
| 📱 **Phone** | Call by name or number, answer or reject, text, find my phone, send files, lock and unlock. |
| ✅ **Productivity** | To-do list, notes, reminders, Pomodoro timer, habit streaks, expenses (even from a receipt photo), flashcards, translate / summarize / rewrite text. |
| 📎 **Office** | PowerPoint decks, Word documents, Excel files with formulas and charts, PDF merge / split / convert / OCR. |
| 💪 **Fitness** | A live workout coach for push-ups, squats, sit-ups, pull-ups and plank, with form checks, rest timers and a weekly chart. Meals by text or photo. |
| 🎮 **Media and games** | Spotify control, YouTube summaries, a video player inside the HUD, Steam / Epic updates, a game overlay with timers. |
| 🌍 **Info** | Web search, weather, flights, calculator, units, live currency. |
| 💻 **Code** | Write, edit and run code, or build a multi-file project. |
| 🏠 **Smart home** | Shelly, Tasmota, WLED, Tuya, IP cameras and wake-on-LAN, on your local network only. |

Every tool is just a file in `actions/`, so adding your own is easy. Heavy libraries (PowerPoint, Word, PDF, OpenCV…) load only when you actually use them, which keeps start-up fast.

🛡️ **Safety first:** shutdown, restart and sending messages need a click on screen. Most changes can be reversed by saying "undo".

**Other things worth knowing**

- 🧑‍💻 **Developer overlay** (`Alt+Space`): live CPU / RAM / GPU, git status and commit, and "explain the error in my clipboard".
- 🔔 **Smart nudges:** Jarvis can speak up on his own about upcoming meetings, low battery, a missed workout or a streak that ends tonight. It's all optional, with quiet hours, under **Settings → Nudges**.
- 🙂 **Face lock:** Settings → Face ID → *Lock Jarvis with my face*. It needs a saved face and a PIN. A photo may fool it, so don't treat it as real security.
- 🧩 **Profiles and plugins:** `home`, `work` and `game` profiles change the HUD and the voice style. To add a plugin, drop a `.py` file into `plugins/` (see `plugins/_template.py`).
- 🔄 **Self-update:** Jarvis checks GitHub for new versions and can install them for you.

## 🎤 Voice, camera and offline mode

**Voice.** Push-to-talk, open mic, mute, and an optional local "Hey Jarvis" wake word.

**Live camera.** Say "open the camera" and a live view stays open until you close it. "Full screen" fills the display with a small Jarvis in the corner. Write a task on a board, say "solve it", and Jarvis reads it and walks you through the steps and the answer.

> 💡 Tips: write large, use good light, keep the board flat.

**Offline mode.** When your internet is down or too slow for a live voice session, Jarvis quietly switches to local commands. It switches back once the connection is good again (two good checks in a row).

- 🌐 Works in Uzbek, Russian and English. You don't need to say "Jarvis".
- 🗣️ Understands things like: open or close the camera, the time and date, volume, brightness, screenshot, open Chrome, timers, reminders, quick notes, simple maths, battery, system status.
- 🚫 Anything that truly needs the internet (translate, "solve this") gets an honest "that needs the internet".
- 🧠 Offline voice uses [Vosk](https://alphacephei.com/vosk/). Its small language model downloads once, in the background, while you're online. Without Vosk you can type the same commands.
- 🔈 Answers are spoken with your system voice. Windows has no Uzbek voice, so spoken Uzbek can sound odd, but the text is always shown.

**Settings** in `config/api_keys.json`:

| Key | Default | Meaning |
| --- | ------- | ------- |
| `offline_auto` | `true` | `false` turns the automatic switch off |
| `offline_lang` | `"uz"` | Vosk language: `uz`, `ru`, `en-us` |
| `offline_stt_path` | none | Path to your own Vosk model folder |
| `offline_tts` | `true` | `false` makes offline answers text only |

## ✋ Hand Space and Dynamic Island

**Hand Space** is a workspace you control with your bare hands. Your drives, folders, pictures, notes, 3D models and videos float on screen as glass cards. It uses only the webcam, everything runs on your PC, and nothing is uploaded. Open it from the sidebar.

| Gesture | What it does |
| ------- | ------------ |
| 🤏 Pinch | Grab a card and carry it |
| 👆 Quick pinch | Open a folder, enlarge a picture, open a note. Pinch again to close |
| 🚀 Throw | Let go while moving and the card flies and bounces |
| 🦅 Claw | Every card is pulled to your palm. Open your hand to release |
| 🙌 Two hands | Pinch a picture with both hands to zoom |
| ✊ Fist (hold 1 s) | Close the open card, or go up one folder |

Press `Esc` or the ✕ to leave.

- 🗃️ **Your cards:** it starts on *This PC*. **Choose folder…** pins a folder of your own. **＋ New card** lets you write a note and pick a colour and icon. Cards are plain Markdown files, so you can edit them anywhere.
- 🌤️ **Live cards:** Weather, Now Playing (Spotify), System, Clock, Calendar, Mail and Expenses. Weather comes from [Open-Meteo](https://open-meteo.com/). Without a city set, it guesses your rough location from your IP, so set `hs_weather_city` if you'd rather it didn't (`"hs_weather_units": "f"` for °F).
- 🦴 **Hand outline:** a switch on the Hand Space page draws the bones of your hand.

**Dynamic Island** is a small floating player at the top of your screen. It shows the time, the weather, and what's playing, tinted with the cover colour. Hover or click to expand it. Click the orange dot to flip between the player, the calendar and the clock. Drag with Shift to move it, right-click for options. Turn it off with `"dynamic_island": false`. It works with any player on Windows (Spotify, YouTube in Chrome, VLC…) through the `winrt-*` packages in `requirements.txt`.

**Hand mouse:** Settings → Gestures → *Use my hand as the mouse*. Your index finger moves the cursor, a pinch clicks, thumb + middle finger right-clicks, ✌ and move scrolls, and holding a fist stops it.

## 🧊 3D with Blender

Jarvis can build real 3D models in [Blender](https://www.blender.org) from plain language. Blender runs in the background and you get a rendered preview.

- 🏰 "Create a medieval castle with four towers" builds it. If the script fails, Jarvis reads the error and tries again (up to 3 times) without ever damaging your project.
- 🎨 "Make the roof red", "add a chimney", "make the wheels metallic", "move the door left", "delete the fence".
- 💡 "Change the lighting", "render it from the front".
- 🖼️ Give it a picture and say "model this" to build something that copies it. It models what it sees from a script, so it isn't photogrammetry, and simple, stylised things work best.
- 📦 "Export it as glb / fbx / obj / stl", "open it in Blender", "undo", "switch to castle".

Projects are saved in `Documents/Jarvis/blender/<project>/`. Install Blender from blender.org. If Jarvis can't find it, set `"blender_path"` in `config/api_keys.json`.

🧩 **Speedcubing page:** say "open my cubing timer" for a Rubik's cube timer (2×2 to 7×7, inspection, scrambles, ao5 / ao12) and an OLL / PLL / F2L algorithm trainer. It also opens in a browser at `https://<PC-IP>:8000/cubing`.

## 📬 Gmail, Calendar, gestures and Face ID

**🧾 Receipts.** Attach a photo of a receipt and say "record this receipt". Jarvis reads the total, shop, date, currency and category and saves it as an expense. If it got something wrong, say "remove the last entry" or just tell it the right amount.

**📧 Gmail and Calendar.** One-time setup, about 5 minutes, and free:

1. In [Google Cloud Console](https://console.cloud.google.com/), create a project and enable the **Gmail API** and **Google Calendar API**.
2. Create an **OAuth client ID** of type **Desktop app** and download the JSON.
3. Save it as `config/google_credentials.json`.
4. Say "connect Google". A browser opens once. Approve access.

Then try "what emails came today?", "show unread emails", "what's on tomorrow?", "put a meeting on Friday at 15:00", "cancel Friday's meeting". Mail is **read-only**: Jarvis can't send or delete emails. The token stays in `config/google_token.json` on your PC.

**🖐️ Hand gestures** (media, volume, mic). Off by default. Turn them on in **Settings → Gestures** and pick an action for each one:

| Gesture | Default |
| ------- | ------- |
| ✋ Open palm | Play / pause |
| ✊ Fist | Mute / unmute mic |
| 👍 / 👎 | Volume up / down |
| ✌ Two fingers | Screenshot |
| ☝ Index finger | Next track |
| 🤟 Three fingers | Previous track |

Frames are processed on your PC with MediaPipe and nothing is recorded. The first start downloads a small hand model (about 8 MB).

**🙂 Face ID.** Off by default. In **Settings → Face ID**, switch it on, type a name and press **Add my face**. Jarvis can greet people by name and warn you about unknown faces. Only 128-number fingerprints are saved (no photos), in `memory/faces.json`. The first start downloads two small models (about 37 MB). It's a convenience feature, not a security lock.

## 📱 Phone connection

The phone connects **out** to your PC, so there's nothing to forward and you don't need ADB.

**Android app (recommended)**

1. Install the APK from [Releases](https://github.com/ASDprogrammer521/Jarvis-ai/releases/latest).
2. Allow the permissions it asks for (notifications, phone, call log, contacts, SMS, location, mic, camera).
3. On the PC, get a fresh **pairing key** from Remote Control or the Dashboard.
4. In the app, enter the **PC IP** and the **key**, then tap **Connect**. The pill in the corner turns **● ONLINE**.

You can also build the APK yourself: open `android/JarvisApp` in Android Studio, or run **Actions → Build Jarvis App APK** on GitHub.

**What you can do**

- 📞 **Calls:** "call Akam", "call +998 90 123 45 67", answer, reject, hang up, "who called?". Incoming calls show up on the PC and Jarvis asks whether to answer or reject. Names need the Contacts permission; caller numbers need Call log.
- 💬 **SMS:** "text 901234567: I'll be there in ten minutes".
- 📁 **Files:** send any file from the phone to the PC, or say "send report.pdf to my phone" (the link expires in 15 minutes).
- 🔍 **Find my phone:** rings at full volume, even on silent, for up to 90 seconds.
- 🔔 **Message previews:** with Notification access, SMS, WhatsApp and Telegram previews show up on the PC (read-only).
- 🕹️ **Control the PC** from the phone: lock, mute, volume, media keys, minimize or close apps, shut down (it asks first).
- ⚡ **Quick actions:** YouTube, lock, home, location, camera, voice, torch, screenshot.

**🔓 Phone unlock.** Say "unlock my phone" and the app swipes up, then draws your pattern, taps your PIN or types your password. Set it up once: open **Jarvis App → Unlock setup**, choose how your phone unlocks and enter it, then turn on **Accessibility → Jarvis phone unlock**. If Android says "Restricted setting", go to Settings → Apps → Jarvis App → ⋮ → *Allow restricted settings*. The code is encrypted with a non-exportable Android Keystore key and never leaves the phone, and the phone only acts on an `unlock` command from your paired PC. Fingerprint or face unlock can't be entered by an app.

**🌐 Without installing anything:** open `https://<PC-IP>:8000/jarvis-app` on the same Wi-Fi and enter the pairing key. You can chat and send quick commands, but a web page can't make calls or read contacts, so use the Android app for those.

<details>
<summary>🔑 Do I need a certificate?</summary>

No. Jarvis makes a self-signed one by itself the first time the dashboard starts (in `config/certs/`), so every install has its own key. The Android app remembers its fingerprint the first time it pairs. Browsers show a warning once, so compare the fingerprint with the one in Jarvis → Phone, then continue. A new certificate is made if your PC's IP changes or you delete `config/certs/`; then tap **Forget PC certificate** in the app and pair again. You can turn encryption off with `JARVIS_TLS=0`, but only do that on a network you fully trust.
</details>

<details>
<summary>🩹 Troubleshooting</summary>

| Problem | Fix |
| ------- | --- |
| Can't open the page | Try it on the PC first: `https://127.0.0.1:8000/jarvis-app` |
| Phone can't reach the PC | Allow port **8000** in Windows Firewall and use the same Wi-Fi (not a guest network) |
| "Invalid or expired key" | Keys last 10 minutes and work once. Get a new one |
| "Certificate changed" | You reinstalled or your IP changed. Tap **Forget PC certificate** and pair again. If nothing changed, treat it as a warning |
| Link keeps dropping | Set the Jarvis App to **Unrestricted** battery use |
| A call only opens the dialer | Give the app the **Phone** permission |
</details>

## 🎨 Looks and settings

- 🧭 **Navigation:** a slim rail on the left. It shows icons and slides open with labels when you move the mouse onto it. Pages: Home, Chat, Dashboard, Phone, Hand Space, Voice & AI, Settings.
- ⌨️ **Shortcuts:** `F4` mute · `F11` full screen · `F12` compact mode (a small floating mic).
- 🌈 **Themes:** Settings → Appearance. The accent picker still works and replaces the theme with your own colour. Saved as `ui_theme`, `ui_theme_auto` and `ui_color`.
- 🔮 **3D HUD models:** Holo, Crystal, Globe, Knot, Helix and Face. Switch them in Settings → Appearance, or double-click the model. Want your own? Drop an `.obj` file in `assets/models/` and restart. The built-in ones are generated by `tools/make_models.py`. Layers are OBJ groups named like `lines:w=1.5,a=1,mix=.3`; check the generator for the options.
- 🎚️ **Other switches:** `boot_intro` and `voice_ring` (both on by default), GPU acceleration and a performance counter.
- 🔔 **Notifications** slide up from the bottom, stack neatly, and never repeat the same message twice.
- 📷 **Camera:** the workout counter, Face ID, gestures and the live view share one camera, so they never fight over the webcam.

<details>
<summary>🧰 Extra setup notes for some tools</summary>

- 🎬 **HUD video** uses [mpv](https://mpv.io). Install `python-mpv` (already in `requirements.txt`) plus libmpv. Windows: download libmpv and copy `libmpv-2.dll` next to `main.py`. Linux: `sudo apt install libmpv2`. macOS: `brew install mpv`. In the video: `Space` pause, `←/→` seek, `↑/↓` volume, `F` full screen. Likes, dislikes and subscribing work after you sign in once in a normal browser window. Jarvis never sees your password.
- 💪 **Workouts** and the **camera view** need `opencv-python` and `mediapipe`. The first use downloads a small pose model (about 6 MB). Put the camera to your side so your whole body is visible.
- 📄 **PDF OCR** needs the free [Tesseract](https://github.com/tesseract-ocr/tesseract) program. Converting Word / PowerPoint / Excel to PDF needs [LibreOffice](https://www.libreoffice.org) (or Word with `docx2pdf` on Windows).
- 🎧 **Spotify** works with the desktop app out of the box. For "play my chill playlist", add `spotify_client_id` and `spotify_client_secret` (free, from developer.spotify.com/dashboard) to `config/api_keys.json`, set `http://127.0.0.1:8888/callback` as the redirect URI, then say "log in to Spotify" once.
- 🎮 **Game FPS** in the game overlay needs the free [PresentMon](https://github.com/GameTechDev/PresentMon/releases) console exe in `tools/` and Jarvis run as Administrator. It only listens to Windows frame events (no injection).
- 🗂️ Generated files go to `Documents/Jarvis/` (change it with `"output_dir"`). Workout and food logs live in `memory/`.
</details>

## 📂 Project layout

```text
Jarvis-ai/
├── main.py            entry point
├── ui/                window, pages, 3D stage, boot intro, Hand Space, settings, theme
├── actions/           built-in tools (one file each)
├── plugins/           drop-in plugins
├── core/              audio, LLM, updater, camera hub, offline mode, Hand Space feeds…
├── dashboard/         remote server and web page (also the speedcubing site)
├── android/JarvisApp/ the Android app (Kotlin)
├── memory/            settings helpers and long-term memory
├── config/            API keys and certificates
├── assets/            banner, icons and 3D models (.obj)
├── tools/             helper scripts
├── scripts/           Windows packaging
└── .github/workflows/ APK and EXE builds
```

## 🔒 Security

- 🔐 **Encrypted link.** The dashboard uses HTTPS / WSS with a certificate generated on your PC. The private key is never shipped with the project. The Android app pins the fingerprint on first pairing and refuses any other certificate after that.
- 🔑 **Pairing key.** One-time, valid for ten minutes, then swapped for a session token. "Revoke devices" ends every session.
- ✅ **Confirmations.** Shutdown, restart and outgoing messages need a click on the PC. A shutdown from the phone starts a 15-second countdown (`shutdown /a` cancels it).
- 📷 **Camera features** (gestures, Hand Space, Face ID) are off until you turn them on, run locally and store no photos.
- 📴 **Offline mode** runs fully on your PC. A camera frame goes to Gemini only when you ask Jarvis to look at something.
- 📁 **Files.** PC → phone links work for one file and expire. Keys, certificates and `api_keys.json` are never sent.

Found a security problem? Please read [.github/SECURITY.md](.github/SECURITY.md) first.

## 📄 License

MIT. Do what you like, just keep the license notice.

---

<div align="center">

Made with ☕ and way too many late nights by **ASDcuber**.
Questions, ideas or bugs? Come say hi on [Discord](https://discord.com/invite/r5q93NpRPt) or [open an issue](https://github.com/ASDprogrammer521/Jarvis-ai/issues).

⭐ If Jarvis helped you, a star keeps the project moving.

</div>
