<p align="center"><img src="docs/logo.svg" width="96" alt="Agent-VScreen"></p>

# Agent-VScreen

<p align="center">
  <a href="https://github.com/kilolonion/agent-vscreen/releases/latest"><img src="https://img.shields.io/github/v/release/kilolonion/agent-vscreen" alt="release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/kilolonion/agent-vscreen" alt="license"></a>
  <img src="https://img.shields.io/badge/Android-11%2B-3DDC84?logo=android&logoColor=white" alt="Android 11+">
  <img src="https://img.shields.io/badge/root-not%20required-blue" alt="no root">
  <img src="https://img.shields.io/badge/MCP-supported-8A2BE2" alt="MCP">
</p>

**A background second screen for any phone agent.**

[中文](README.zh-CN.md) · English

Agent-VScreen opens and drives other apps on an invisible virtual display, so your own screen stays yours. All you see is a small floating window showing what the AI is doing, which you can take over or stop at any moment.

Any agent on the phone can use it: agents with a terminal use the `vscreen` CLI, agents that speak MCP use MCP, and your own code can use plain HTTP.

<p align="center"><img src="docs/app.en.png" width="760" alt="Agent-VScreen Home, Connect, Records and Settings screens"></p>
<p align="center"><sub>The app: Home (standby, take over or stop, recent runs), Connect (connected agents, Tailscale remote access, tokens), Records (every task, question and plan with step thumbnails) and Settings (who can connect, how much an agent may do, app rules, floating window).</sub></p>

<p align="center"><img src="docs/agents.png" width="860" alt="Minis, Eta, RikkaHub and Muse all driving a forum app on the background screen through vscreen"></p>
<p align="center"><sub>One install command: four different Android agents (Minis, Eta, RikkaHub, Muse) all connect and drive the background screen.</sub></p>

<p align="center"><img src="docs/demo.gif" width="440" alt="An agent solving sudoku in Chrome and playing Roco Kingdom on the background screen, mirrored live in the floating window"></p>
<p align="center"><sub>Left: an agent solves sudoku in Chrome on the background screen (8x speed). Right: an agent plays Roco Kingdom in landscape, walking with the joystick, dragging the camera and handling battle pop-ups (2.6x speed). In both, the user's own screen stays on the chat app.</sub></p>

- Version: 1.4.1 (versionCode 51) · [Download APK](https://github.com/kilolonion/agent-vscreen/releases/latest)
- Package: `com.kilon.agentvscreen`
- Android 11+ (Android 14+ recommended), arm64
- Privileges: [Shizuku](https://shizuku.rikka.app/) only, no root

## What it does

- **Drives apps in the background**: opens apps on the background screen, taps, swipes, types, presses keys and waits for the screen to change. Every step is checked; a step that did not work stops the run and says what the screen shows.
- **Hands the screen to the agent**: every reply carries the screen as it is now, the words on it, the tappable elements and a screenshot. The app calls no AI model; the agent's own model decides what the screen means.
- **Waits and watches**: after an action it can wait for words to appear or go, or for the screen to settle; after the turn it can keep watching and notify you or wake the agent when a condition shows up.
- **Works with you**: the agent can ask you to point at something on the screen (`ask`) or to show it once and keep that as a lesson (`teach`); steps that need a password or a code move to your own screen.
- **Floating window**: its border says who has the screen (rainbow: the AI is acting, blue: standing by, green: you took over, red: stopped). Drag to move, pinch to resize, fling to an edge to fold it into a tab; hold the picture for 0.5 s to take over; open full screen to type with your own keyboard.
- **Leaves your tools alone**: Shizuku only; it never takes adb or touches wireless debugging, so the agent's own adb or Shizuku keeps working.

## What an agent can do with it

This list and the note agents receive come from one ability table (`Abilities.kt`) and are written by a test; don't edit them by hand.

<!-- abilities:start -->
- **the user wants anything done on the phone: open an app, look something up, read a page, fill a form, test an app…**: `vscreen launch <app>` opens it and looks, `vscreen act "<steps>"` taps, swipes, types and presses keys; every reply has a screenshot and the elements
- **anything timed that will use the phone: the user asks for daily or at 8:00 (check-ins, periodic checks), or I set up my own timer, cron or reminder**: set both: my timer wakes me, not the phone. Book the same time with `vscreen schedule "<when>" --name <name>`; change or cancel both together
- **something will happen later: back in stock, a price drop, a reply, a download finishing; or I want to look again in a while**: `vscreen act --stop "text:In stock" --keep notify` makes the phone keep watching and notify the user when seen (`--keep wake` wakes me; fetch with `vscreen events`)
- **a long list or a whole page has to be read (all orders, a chat history, search results, comments)**: `vscreen collect --pages 10` pages through it and returns every item once
- **it is unclear which thing on the screen the user means (which item, button, message), or the user should pick one**: `vscreen ask "Which one do you mean?"` lets the user tap it on the screen's picture on the phone (also `--choose`, `--text`)
- **a flow is hard to describe, keeps failing, or the user knows better how to do it**: `vscreen teach "what to show"` asks the user to do it once on the screen; it is saved as a segment, then `act "use <name> <values>"` replays it
- **the same app comes up again and again: a fixed way in, a popup every visit, a picture to pause first, or machine-like timing upsets it**: `vscreen note` keeps what I learned about the app, saved steps (`note save`), before/after steps and human pacing; the next launch lists them
- **a step only the user can do (password, code, face, scanning), or the app I need is the one the user is using**: `vscreen handoff out` puts the app on the user's screen with what to do; `vscreen handoff in` takes the app from the user's screen
- **an app has no sound, or the user wants an app muted or its sound back**: `vscreen sound` shows it, `sound mute|unmute <app>` mutes or unmutes
- **the text is too small or an icon, or there is no text at all (games, canvas, charts), or I need to see what just happened**: `vscreen look` asks for pictures: the screen now, a region up close, or the recording; `vscreen spots` finds tappable color patches
- **the phone cannot be reached, commands keep failing, or something odd happens**: First tell off from broken: not running, service off or hidden is the user's choice; tell the user to open it, nothing to repair. Only `vscreen status` with ready false is a fault, and `vscreen fix` repairs what it lists and gives sound back to apps left silent
<!-- abilities:end -->

## Why it works well

- **A sense of time**: while an agent works, the screen is looked at about 5 times a second and read about once a second, with timestamps. Each reply's [Meanwhile] says what appeared, disappeared or flashed since the last reply (including while the agent was thinking), where the picture changed and for how long. Countdowns, loading and pop-ups don't slip by.
- **Seeing clearly**: the accessibility tree and on-device OCR (PP-OCRv6, plus ML Kit) merge into one numbered list of elements with coordinates; `tap #N` and `tap <words on screen>` both work. `look` zooms into an area or plays back the recording; `collect` scrolls through a whole page and gathers every entry once.
- **One step language**: `try`, `if`, `repeat … until`, `*` wildcards and `words@2` for the second place, shared by scripts, saved segments and lessons. Each app keeps notes and saved steps that are listed the next time it opens.
- **Many agents, no mix-ups**: every connected agent has its own token and records; one session holds the screen at a time and others get `BUSY`; apps can be blocked or read-only, and payment steps wait for you to confirm on the phone.
- **Any model**: nothing runs a model on the phone, so any agent and any model can use it.

## Install

1. Install the APK and open Agent-VScreen.
2. Make sure Shizuku is running, then tap **Grant Shizuku**.
3. Tap **One-tap setup** for the overlay, notifications, read-only accessibility, battery optimization and background running. On Honor, Huawei, Xiaomi, OPPO, vivo and similar phones, also open background management and allow auto-start and background activity, or the system may freeze the app in the background.

The app speaks Chinese and English (System / 中文 / English in Settings), and so does everything it tells the agent.

## Connect an agent

On the app's **Connect** tab, tap **Connect a new agent**: give it a name, choose where it runs and how it connects, then tap **Copy message for your agent** and send it as is. The agent installs or configures the tool and saves a short note into its own long-term memory, so new conversations know the tool is there. Each connected agent gets its own token, which you can revoke on the Connect tab at any time.

There are three ways to connect, the same for local and cloud agents:

- **Shell**: agents with a terminal install the `vscreen` command: `vscreen launch Settings`, `vscreen act "tap Search; type About phone"`.
- **MCP**: agents that speak MCP add the address and token (transport `httpStream`).
- **HTTP**: your own code calls the `/v2` API directly; see [API.md](API.md).

### Local: the agent runs on this phone

Choose **On this phone**. The service listens only on `127.0.0.1:18765`; nothing outside the phone can reach it. Terminal agents and MCP chat apps on the phone connect as above; Operit also has a ready-made ToolPkg in [integrations/operit](integrations/operit/).

If another app (or a cloned copy of this one) holds 18765, the service moves to the next free port and the app says who holds it; local agents find the new port by themselves, no reconnecting needed.

### Cloud: the agent runs on a computer, a server or another phone

Choose **Another device** and connect Tailscale under **Remote access** first; the message, install command and MCP config you copy then use the Tailscale address.

- **Built-in Tailscale (recommended)**: no Tailscale app and no system VPN slot; sign in once inside the app, and only devices on your own tailnet can reach it. A self-hosted Headscale works too: enter its address under the advanced options.
- **Tailscale app**: if the Tailscale app is already on the phone, or the phone needs an exit node to get online. The built-in node only lets other devices in; it does not carry the phone's own traffic.
- SSH port forwarding also works.

The token equals control of the phone. Requests from other devices are signed, so the token itself never crosses the network, and the app never offers a public link. Don't paste a token into public configs or screenshots.

## Docs

- [API.md](API.md) (Chinese): the full CLI, MCP and HTTP reference, sessions, watches, permissions and security, remote access and known limits.
- [docs/REFERENCE.md](docs/REFERENCE.md): every command option and result code (generated from the source).
- [docs/TASKS.md](docs/TASKS.md): the fixed task set to run on a real phone before a release.
- [docs/CHANGELOG.md](docs/CHANGELOG.md): earlier releases.

## What's new in 1.4.1

- **Schedules and watches per agent**: same names no longer overwrite each other; forgetting an agent clears its schedules and watches.
- **Steadier self-hosted Headscale**: the control server resolves even with a proxy such as FlClash on; public DNS is used only when every phone DNS is unreachable.
- **Shizuku**: diagnostics include Shizuku's version, permission and user state; the hint leads with the usual cause (Shizuku must be started again after a restart).
- Fixed Remote › Advanced not opening; schedules, watches and task ownership are more reliable; app data stays out of system backups.

## What's new in 1.4.0

- **A new app**: four tabs (Now, Connect, Records, Settings), each page with one main thing; explanations moved to second-level pages. Purple glass throughout.
- **Every agent on its own**: each connected agent gets its own token, records and saved steps; lessons are shared. One inbox on the home page collects what agents need from you, and notifications open the right page.
- **Teaching, rebuilt**: one lesson flow from the request to the saved segment, a record button that answers the agent's request, and a review pane beside the live screen. A repeated `teach` returns the saved lesson instead of asking again. Agents tidy the page back to its starting state before they ask.
- **Keyboard**: `key ctrl+a` / `shift+tab` / `alt+f4` combos; `type` at once or `type "…" slow` letter by letter. In full screen the keyboard button opens your own input method.
- **App sound**: Settings › App sound lists every silenced app and gives sound back; the `sound` command does the same for agents. Muting now sets both of Android's sound records, for phones that only check one of them.
- **`fix` repairs more**: silenced apps, a stopped foreground service, the built-in Tailscale; "fixed" is checked afterwards, not assumed.
- **Port taken**: when another app (or a clone-space copy) holds the port, the service takes the next free one and says who holds it; local agents find it by themselves and Tailscale forwards to it.
- **Smaller, faster reading**: PP-OCRv6 tiny detector + small recognizer (11.5 MB); `collect` skips search bars and keeps going to the real end; `repeat … until` judges the last look on what the screen shows now.

## Build from source

JDK 21 and the Android SDK (compileSdk 37).

```bash
echo "sdk.dir=/path/to/android-sdk" > local.properties
./gradlew :app:assembleRelease
```

Built-in Tailscale is a small Go program (`tsbridge/`). Run `tsbridge/build.sh` once before building to produce `app/src/main/jniLibs/arm64-v8a/libtsbridge.so`; without it the APK still builds, just without built-in Tailscale.

Release signing is optional: copy `keystore.properties.example` to `keystore.properties` and fill it in. Otherwise release builds are signed with the debug key.

## License

MIT. The bundled OCR models (`app/src/main/assets/vscreen-ocr/`) come from PaddleOCR under their own Apache-2.0 license.

## Thanks

- [LINUX DO](https://linux.do)
- [OpenMinis](https://github.com/OpenMinis)
