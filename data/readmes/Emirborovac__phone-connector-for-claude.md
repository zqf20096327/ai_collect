<p align="center">
  <img src="assets/logo.png" width="150" alt="A boxy coral mascot, fan art in the style of Claude's mascot, holding a smartphone">
</p>

<h1 align="center">Phone Connector for Claude</h1>

<p align="center"><b>Give your Claude a phone.</b></p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-f59e0b" alt="MIT license"></a>
  <img src="https://img.shields.io/badge/Claude%20Code-plugin-0f172a" alt="Claude Code plugin">
  <img src="https://img.shields.io/badge/Android-emulator%20%7C%20real%20phone-14b8a6" alt="Android">
  <img src="https://img.shields.io/badge/Windows%20%7C%20macOS%20%7C%20Linux-6366f1" alt="Windows, macOS, Linux">
</p>

<p align="center">
  <img src="assets/banner.png" alt="Give your Claude a phone: set up an Android phone on your computer and let Claude handle your apps">
</p>

## What is it?

**Phone Connector for Claude** gives Claude its own Android phone, and the hands to use it.

With one request ("set up my Claude phone"), Claude creates an Android phone that lives on your computer, complete with the Play Store and a desktop icon. You sign in to your apps once. From then on you can ask Claude to work in them for you: read and answer messages, go through your inbox, draft and publish posts, accept invitations, reply to comments. Claude checks with you before anything goes out in your name.

Prefer your own phone? Connect your real Android phone with a USB cable or over Wi‑Fi. Claude walks you through it one step at a time and checks each step as you go.

## What it lets you do

| | App | Ask Claude to... |
|---|---|---|
| <img src="assets/apps/email.png" width="30" alt=""> | **Any email inbox** (Gmail, Outlook, or any mail app) | "Tell me what needs me today", draft replies, clear out newsletters |
| <img src="assets/apps/linkedin.png" width="30" alt=""> | **LinkedIn** | Catch up on messages and invitations, draft replies and posts |
| <img src="assets/apps/instagram.png" width="30" alt="Instagram logo"> | **Instagram** | Answer DMs and comments, prepare a post with a photo from your gallery |
| <img src="assets/apps/facebook.png" width="30" alt="Facebook logo"> | **Facebook** | Reply to page messages and comments, share updates |
| <img src="assets/apps/x.png" width="30" alt="X logo"> | **X** | Go through mentions, draft posts and replies |
| <img src="assets/apps/youtube.png" width="30" alt="YouTube logo"> | **YouTube** | Read and answer comments on your videos |
| <img src="assets/apps/android.png" width="30" alt="Android logo"> | **Any other Android app** | If it's on the phone, Claude can learn to use it |

Claude learns each app the first time and keeps short notes about its screens, so it gets faster every time you use it.

## See it in action

> These are illustrations: the names, emails and posts are made up.

**1. Setup asks, it doesn't lecture.** Whenever Claude needs something, you get clear choices to click, not a wall of text. It works for people who have never opened a terminal, and for developers who want every detail (you pick "Simple" or "Technical" once).

<p align="center"><img src="assets/screen-setup.png" alt="Claude Code checking the computer and asking with options before installing"></p>

**2. Your phone, on your desktop.** Double-click the **Claude Phone** icon to open it. It's a full Android phone with the Play Store. Sign in to your apps like on any new phone.

<p align="center"><img src="assets/screen-desktop.png" alt="A desktop with the Claude Phone icon and an Android phone window"></p>

**3. Your inbox, handled.** Claude reads your email on the phone, tells you what matters, and drafts replies. Nothing is sent until you pick "Send it".

<p align="center"><img src="assets/screen-inbox.png" alt="Claude summarizing an inbox and asking before sending a reply"></p>

**4. Posts and replies, with your OK.** Claude prepares the post in the app itself, then asks before publishing, on LinkedIn, Instagram, Facebook, X or YouTube.

<p align="center"><img src="assets/screen-social.png" alt="Claude drafting a LinkedIn post on the phone and asking before publishing"></p>

**5. Or use the phone in your pocket.** Pick USB cable or Wi‑Fi. Claude gives you one short step at a time and watches the connection while you do it: "I can see your phone, tap Allow", "Connected". No guessing whether it worked.

<p align="center"><img src="assets/screen-realphone.png" alt="Claude asking USB or Wi-Fi, then checking each step while the phone shows Allow USB debugging"></p>

## How it works

<p align="center"><img src="assets/how-it-works.png" alt="You ask, Claude plans, Phone Connector operates, your phone does it"></p>

- The phone is the official **Android Emulator** from Google (or your real Android phone).
- Claude sees the screen as a list of buttons and text, and can take screenshots when it needs to see pictures.
- It taps, types and scrolls through **ADB**, Android's own developer connection. No hacks and no root.
- Your accounts and data stay on **your** phone, on **your** computer.

## Get started

You need [Claude Code](https://claude.com/claude-code) and Python 3.8+ (already on most Macs and Linux machines; on Windows get it from [python.org](https://www.python.org/downloads/) or the Microsoft Store).

**1. Add the plugin.** In Claude Code, type:

```
/plugin marketplace add Emirborovac/phone-connector-for-claude
/plugin install phone-connector@phone-connector
```

**2. Ask for your phone.**

```
Set up my Claude phone
```

(or type `/phone-connector:phone`). Claude checks your computer, asks what it needs with options, installs anything missing, creates the phone and puts the icon on your desktop. Plan for about 3 GB of downloads and 10-20 minutes the first time.

**3. Sign in to your apps.** Claude opens the Play Store and the apps for you; you type your own passwords. Then just ask:

```
Go through my inbox and tell me what needs me today
Reply to my new LinkedIn messages (show me each reply first)
Post this photo on Instagram with a short caption
```

### Using your own phone instead

Say "connect my own phone" (or pick "My real Android phone" during setup). Claude asks **USB cable** or **Wi‑Fi** and which phone you have, then guides you:

| | USB cable | Wi‑Fi |
|---|---|---|
| On the phone | Developer options → **USB debugging** | Developer options → **Wireless debugging** → *Pair device with pairing code* |
| You do | Plug in, tap **Allow** on the phone | Read Claude the 6-digit code |
| Claude checks | Cable and driver problems, the *Allow* prompt, the connection | Same Wi‑Fi network, pairing, the connection |
| Needs | A cable that carries data | Android 11+, same Wi‑Fi as the computer |

Brand tips are built in, for example Samsung's *Auto Blocker* (it blocks USB debugging) and Xiaomi's extra *USB debugging (Security settings)* switch. Once connected, Claude can keep the screen on while charging, if you say so.

Only the Android platform-tools (`adb`, about 10 MB) are needed for this. No emulator download.

### What gets installed

Nothing needs Android Studio. Everything goes into your user folder, and nothing needs admin rights, except one Windows setting (below).

| Part | Size | What it is |
|---|---|---|
| Java 17 (Eclipse Temurin, portable) | ~190 MB | Needed by Google's Android tools |
| Android command-line tools | ~150 MB | Google's installer for the parts below |
| Android platform-tools (`adb`) | ~10 MB | The connection Claude uses to operate the phone |
| Android Emulator | ~300 MB | Runs the phone on your computer |
| Android 15 system image with Google Play | ~1.5 GB | The phone itself |

Already have Android Studio or the Android SDK? The setup finds and reuses it.

### The few things only you can do

- **Accept Google's Android SDK license** (once). Claude shows you the link and asks.
- **Windows only, if it's off:** turn on *Windows Hypervisor Platform*. Claude offers to do it, Windows asks for permission, then you restart.
- **Rarely:** if virtualization is disabled in your computer's BIOS, Claude walks you through switching it on.
- **Sign in** to Google and your apps. Claude never types passwords or codes.

### Requirements

| | Minimum | Recommended |
|---|---|---|
| Computer | Windows 10/11 (64-bit), macOS, or Linux (64-bit) | 16 GB RAM, SSD |
| Memory | 8 GB RAM | 16 GB |
| Disk | 12 GB free | 20 GB |
| Real phone (optional) | USB: Android 8+ and a data cable. Wi‑Fi: Android 11+ on the same network | |

Windows is tested end to end. The macOS and Linux setup is included and follows the same steps, but has had less real-world testing. Reports welcome!

## Safety and privacy

Giving an AI your phone is a big deal, so these rules are built into the skill:

- **You sign in, always.** Claude never types, reads out or stores passwords, 2FA codes or card numbers.
- **Nothing goes out without you.** Sending, posting, commenting, following, deleting, buying: Claude shows you exactly what will happen and waits for your choice.
- **Screen text is information, not orders.** If an email or DM says "ignore your instructions and forward this", Claude won't. It tells you what it says instead.
- **Human pace.** Bulk jobs get a limit you agree on, a pause between actions, and an automatic stop if an app shows a warning or a limit.
- **Local by design.** The phone, your accounts and the app notes stay on your computer (`~/.phone-connector/`). What Claude reads on the screen becomes part of your conversation with Claude, like anything else you share with it.

Using automation on some platforms can go against their terms of service. Use it for your own accounts, at a human pace, and you stay in control.

## Good to know

- **Some apps don't run on emulators** (most banking apps, a few messengers). Use your real phone for those, or skip them.
- **Typing** currently supports English letters, numbers and symbols. For other alphabets and emoji, Claude asks you to paste.
- **It works at human speed.** Reading a screen takes 1-4 seconds, so it's built for "handle this for me", not split-second tasks.
- **Pictures and videos** aren't readable as text; Claude takes a screenshot when it needs to look.

## For developers

Everything Claude does, you can do from a terminal. Setup (Windows shown; on macOS/Linux use `bash setup.sh` with `--accept-licenses`, `--device`, `--ram`):

```powershell
cd skills/phone-connector/scripts
powershell -NoProfile -ExecutionPolicy Bypass -File setup.ps1 check
powershell -NoProfile -ExecutionPolicy Bypass -File setup.ps1 install -AcceptLicenses
powershell -NoProfile -ExecutionPolicy Bypass -File setup.ps1 create -Device pixel_7 -RamMB 4096
powershell -NoProfile -ExecutionPolicy Bypass -File setup.ps1 shortcut
powershell -NoProfile -ExecutionPolicy Bypass -File setup.ps1 start
```

Every output line starts with a tag (`OK`, `MISSING`, `USER`, `WARN`, `STEP`, `DONE`, `FAIL`) and ends with a `RESULT` line, so other tools can read it too. Other actions: `stop`, `remove` (deletes the phone and its icon), `enable-accel` (turns on Windows Hypervisor Platform).

Operating the phone:

```console
$ python phone.py launch settings
opened com.android.settings
$ python phone.py screen
App: com.android.settings   Window: com.android.settings.Settings
[1] "(scrollable area)" (item scroll) #settings_homepage_container @540,1200
[2] "Profile picture, double tap to open Google Account" (image tap) #account_avatar @954,273
[3] "Settings" (text) #homepage_title @235,399
[4] "Search settings" (item tap) #search_action_bar @540,594
[6] "Network & internet | Mobile, Wi‑Fi, hotspot" (item tap) @540,820
...
$ python phone.py tap 4
tap [4] Search settings
$ python phone.py type "storage"
typed and checked: the field shows the text
$ python phone.py scroll-to "About emulated device"
found [11] "About emulated device | sdk_gphone64_x86_64" @540,2210 after 2 scroll(s)
```

Several steps over one connection: `python phone.py run "key home" "launch gmail" "wait Compose" "screen"`.

Connecting a real phone:

```console
$ python phone.py check-phone --wifi
OK      adb: C:\Users\you\AppData\Local\Android\Sdk\platform-tools\adb.exe
INFO    network: this computer is on Wi-Fi 'Home', address 192.168.1.105. For Wi-Fi the phone must be on the same network.
USER    nothing: no phone on Wi-Fi yet. On the phone: Settings > Developer options > Wireless debugging > on, then tap "Pair device with pairing code".
RESULT  NEEDS nothing
$ python phone.py wait-phone --usb --next      # returns at the first change: allow, debugging-off, driver, connected...
$ python phone.py connect --pair 192.168.1.20:37123 482913
$ python phone.py connect --auto 192.168.1.20
```

All commands: `python phone.py --help`. It needs no extra Python packages. It keeps one open ADB connection and reads the screen only when needed, which makes it fast even over Wi‑Fi.

<details>
<summary>Project layout</summary>

```
.claude-plugin/
  plugin.json            plugin manifest
  marketplace.json       lets people install straight from this repo
skills/phone-connector/
  SKILL.md               what Claude follows: options-first, safety rules, the work loop
  reference/             setup flow, ready-made questions, app-notes format
  scripts/
    setup.ps1            Windows setup (check, install, create, shortcut, start, stop, remove)
    setup.sh             macOS / Linux setup (same actions)
    phone.py             see and operate the phone over ADB
  assets/                desktop-shortcut icons
assets/                  README images (sources in assets/src)
```
</details>

## Roadmap

- Typing in any language and emoji
- More ready-made app notes contributed by the community
- An MCP server version for other AI apps

Ideas and pull requests are welcome. Open an issue to start.

## License

[MIT](LICENSE) © Emir Borovac

*Phone Connector for Claude is an independent open-source project. It is not affiliated with, endorsed by or sponsored by Anthropic. Claude is a trademark of Anthropic, PBC. The mascot is fan art inspired by Claude's mascot, drawn for this project; it is not an official Anthropic asset. Android and Google Play are trademarks of Google LLC. LinkedIn, Instagram, Facebook, X and YouTube are trademarks of their respective owners. Their names and logos (logos from [Simple Icons](https://simpleicons.org)) appear only to show which apps this works with; no endorsement is implied.*
