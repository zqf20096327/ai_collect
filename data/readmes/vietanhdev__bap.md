<div align="center">

<a href="https://bap.nrl.ai"><img src="docs/images/banner.png" alt="Bắp: a voice buddy you can touch, talk to and wave at, running on a SenseCAP Watcher" width="100%"></a>

<h3>A cute, fast voice assistant firmware for the Seeed SenseCAP Watcher</h3>

The device talks straight to Google Gemini Live. No relay server, no cloud of our own.

[![CI](https://github.com/vietanhdev/bap/actions/workflows/ci.yml/badge.svg)](https://github.com/vietanhdev/bap/actions/workflows/ci.yml)
![ESP32-S3](https://img.shields.io/badge/ESP32--S3-ESP--IDF%206.1-7c5cff)
![Gemini Live](https://img.shields.io/badge/Gemini-Live%20API-4f8cff)
![LVGL 9](https://img.shields.io/badge/LVGL-9.5-8bc34a)
[![License: MIT](https://img.shields.io/badge/license-MIT-f5c84b)](LICENSE)

**English** · [Tiếng Việt](README.vi.md)

[**Documentation**](https://bap.nrl.ai) ·
[Demo](#-see-it-in-action) ·
[Features](#-features) ·
[Quick start](#-quick-start) ·
[How it works](#-how-it-works) ·
[Controls](#-controls)

</div>

## 🎬 See it in action

Recorded from the device's own screen (`GET /screen.jpg`), in real time.

<table>
<tr>
<td align="center" width="33%"><img src="docs/images/demo/conversation.gif" width="260" alt="Conversation demo"><br><b>Ask anything</b><br><sub>It answers with live subtitles, then plays the song</sub></td>
<td align="center" width="33%"><img src="docs/images/demo/characters.gif" width="260" alt="Switching characters"><br><b>Five characters</b><br><sub>Chosen in Settings</sub></td>
<td align="center" width="33%"><img src="docs/images/demo/menu.gif" width="260" alt="Round menu"><br><b>Round menu</b><br><sub>Hold the wheel or the screen</sub></td>
</tr>
</table>

<p align="center">
<img src="docs/images/screens/emotions.gif" alt="Five characters, 23 expressions each, drawn natively with LVGL" width="760"><br>
<sub>23 expressions per character, drawn natively with LVGL, with lip sync while speaking</sub>
</p>

<details>
<summary><b>More screens</b>: music, radio, menus, Korean and Chinese</summary>
<br>
<table>
<tr>
<td align="center"><img src="docs/images/screens/listening.png" width="180"><br><sub>Listening</sub></td>
<td align="center"><img src="docs/images/screens/talking.png" width="180"><br><sub>Speaking, live subtitles</sub></td>
<td align="center"><img src="docs/images/screens/music-lyrics.png" width="180"><br><sub>Zing MP3, synced lyrics</sub></td>
<td align="center"><img src="docs/images/screens/radio.png" width="180"><br><sub>Radio (VOV, FM Hà Nội)</sub></td>
</tr>
<tr>
<td align="center"><img src="docs/images/screens/menu.png" width="180"><br><sub>Round menu</sub></td>
<td align="center"><img src="docs/images/screens/menu-settings.png" width="180"><br><sub>Settings on the wheel</sub></td>
<td align="center"><img src="docs/images/screens/korean.png" width="180"><br><sub>Korean</sub></td>
<td align="center"><img src="docs/images/screens/chinese.png" width="180"><br><sub>Chinese</sub></td>
</tr>
</table>
</details>

## ✨ Features

<table>
<tr>
<td width="50%" valign="top">

### 🗣️ Talk naturally
Real-time two-way audio with Gemini Live: interrupt anytime, live subtitles on the round screen.
Double-tap the screen or press the wheel (or say **"Hi Lili"** once voice wake-up is on in the settings).

</td>
<td width="50%" valign="top">

### 👆 Made to be touched
Tap and it giggles, double-tap to talk, hold for the menu. The scroll wheel talks, sets the
volume, and three quick presses power it off.

</td>
</tr>
<tr>
<td valign="top">

### 👀 Notices you
The camera's own AI chip spots a person and wakes the screen with a greeting, and a morning
briefing once a day. No image leaves the device and no Gemini quota is used.

</td>
<td valign="top">

### 🎭 Five characters
Bông, Bắp, Bơ, Mochi and Tí, each with a voice, personality and natively drawn face. Characters,
apps and languages are plain data, so no C++ is needed to add one.

</td>
</tr>
<tr>
<td valign="top">

### 🛠️ 28 on-device tools
Lunar calendar, weather and air quality, news, gold prices, exchange rates, stocks, football,
lottery, timers, alarms, notes and long-term memory. No extra API keys.

</td>
<td valign="top">

### 🎵 Music and radio
Zing MP3 with synced lyrics, VOV and FM Hà Nội streams, and offline songs from the SD card with
accent-insensitive search.

</td>
</tr>
<tr>
<td valign="top">

### 🌏 Four languages
Vietnamese, English, Korean and Chinese: the conversation, on-screen text, menu and the date line
(Korean and Chinese subtitles use a Noto Sans subset).

</td>
<td valign="top">

### 🌙 Calm at night
Night mode dims the screen and caps the volume, do-not-disturb mutes the wake word, and the screen
dims, then switches off, when nobody is around.

</td>
</tr>
</table>

<details>
<summary><b>Everything else</b>: voice apps, extensions, settings page</summary>

- **Voice apps**: morning news, bedtime stories, English practice, Korean basics, evening journal,
  fun horoscope, quiz, breathing, "what to eat today", 25-minute focus, look-and-tell (camera).
- **Extensions**: declare webhooks (Home Assistant, n8n, your own server) in the web page and the
  assistant calls them through `extension.call`.
- **Settings page** at `http://bap-xxxx.local` (one name per device): API keys, model, language,
  city, characters, persona editing, conversation log, Wi-Fi, password, device health and
  30-second OTA updates.
- **Data sources**: Open-Meteo, VnExpress, Vietcombank, PNJ and a local jeweller, CafeF, ESPN, Zing
  MP3, VOV. All are called from the device itself.

</details>

### Compared with the stock firmware

|  | Stock SenseCraft / upstream xiaozhi | **Bắp** |
| --- | --- | --- |
| Voice backend | A vendor or self-hosted server relays audio | **Device ↔ Gemini Live directly** (WebSocket + TLS) |
| Wake → listening | Depends on the relay server | **1.4–2.3 s**, TLS resumed in 0.1 s |
| Faces | GIF emoji | **5 characters drawn in LVGL**, 23 expressions, lip sync |
| Languages | Chosen by the server | **Vietnamese, English, Korean, Chinese** |
| Touch screen | Not used | **Tap, double tap, drag and hold** |
| Camera AI | SenseCraft task flows | **On-device person detection** for greetings |
| Settings | Vendor app or server console | **Local web page**, password, health panel, OTA |
| Overnight | Same as daytime | **Night mode**, do-not-disturb, screen rest |

The factory partition (`nvsfactory`, device keys) is never written, and the stock firmware can be
restored at any time.

## 🎭 Characters

| | Name | What it is | Voice | Personality |
| :-: | --- | --- | --- | --- |
| <img src="docs/images/screens/idle-bong.png" width="72"> | **Bông** `bong` | a little cotton cloud | Leda | Gentle, warm, encouraging (default) |
| <img src="docs/images/screens/idle-bap.png" width="72"> | **Bắp** `bap` | a golden corn cob | Puck | Playful, energetic, crunchy jokes |
| <img src="docs/images/screens/idle-bo.png" width="72"> | **Bơ** `bo` | a creamy avocado | Achird | Calm, relaxed, cares about your health |
| <img src="docs/images/screens/idle-mochi.png" width="72"> | **Mochi** `mochi` | a pink mochi | Aoede | Sweet storyteller, great with kids |
| <img src="docs/images/screens/idle-ti.png" width="72"> | **Tí** `ti` | a tiny robot | Kore | Neat and tech-savvy |

Names, voices and personalities can be edited in the settings page. To add your own, see
[docs/adding-a-character.md](docs/adding-a-character.md).

## 🚀 Quick start

<table>
<tr>
<td width="42%"><img src="docs/images/photos/hardware.jpg" alt="SenseCAP Watcher in hand"></td>
<td valign="top">

**You need**

- a **Seeed SenseCAP Watcher** (W1-A, W1-B or the "for XiaoZhi" edition): ESP32-S3, 32 MB flash,
  8 MB PSRAM, round 412×412 touch screen, scroll wheel, camera with a Himax AI chip, mic and speaker
- a USB-C data cable
- Linux with Docker and [uv](https://docs.astral.sh/uv/)
- a Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey)

</td>
</tr>
</table>

**1. Back up the stock firmware** (once). The dump holds the device's private keys: never commit or
share `backup/`.

```bash
mkdir -p backup
uv run --with esptool esptool --chip esp32s3 --port /dev/serial/by-id/usb-1a86_USB_Dual_Serial_*-if02 \
  --baud 921600 read-flash 0x0 0x2000000 backup/watcher-w1a-esp32s3-full-32MB.bin
( cd backup && sha256sum watcher-w1a-esp32s3-full-32MB.bin > watcher-w1a-esp32s3-full-32MB.bin.sha256 )
```

**2. Fetch upstream, build and flash**

```bash
firmware/scripts/apply_patch.sh     # clone xiaozhi-esp32 @ aaf1eb7 into vendor/ and apply the patch

mkdir -p secrets && chmod 700 secrets
printf '%s' 'YOUR_GEMINI_API_KEY' > secrets/GEMINI_API_KEY && chmod 600 secrets/GEMINI_API_KEY

firmware/build.sh                   # firmware, in Docker (espressif/idf:release-v6.1)
firmware/build_assets.sh            # fonts, faces and wake word
firmware/flash.sh                   # first flash over USB
```

**3. Connect and talk**

1. On first boot the Watcher opens a hotspot named **`Bap-XXXX`**. Join it with your phone and pick
   your Wi-Fi (or browse to `http://192.168.4.1`).
2. Open **`http://bap-xxxx.local`** (the address is also shown on screen), then choose a city,
   language and character.
3. Double-tap the screen or press the wheel and start talking. Voice wake-up ("Hi Lili") is off by
   default to save power; turn it on in the settings page or the wheel menu.

Later updates go over Wi-Fi in about 30 seconds: `firmware/ota.sh bap-xxxx.local`.
To change Wi-Fi, hold the wheel → **Settings → Wi-Fi setup**.

<details>
<summary><b>Build options</b>: API keys, model, wake word, flashing helpers</summary>

- Leave `secrets/GEMINI_API_KEY` empty to enter the key later in the web page (CI builds never
  contain a key).
- Optional `secrets/GEMINI_API_KEY_PAID`: a key from a billed project, used only when the free-tier
  key is rejected. The free key is retried after 1, 2, 4… up to 15 minutes.
- Build variables: `GEMINI_MODEL`, `GEMINI_VOICE`, `WAKE_WORD` (default `wn9_hilili_tts`, "Hi
  Lili"), `LANG_CODE`.
- `firmware/flash_app.sh` writes only the app, `firmware/flash_assets.sh` only the assets
  partition. The scripts find the Watcher on USB; with several plugged in, choose one with
  `PORT=/dev/serial/by-id/...`.
- Restore the stock firmware with `firmware/restore_stock.sh` (checks the backup's SHA-256, then
  writes all 32 MB). Without a dump, reinstall SenseCraft with Seeed's tool: your device keys in
  `nvsfactory` are untouched.

</details>

## 🧠 How it works

<p align="center"><img src="docs/images/diagrams/architecture.svg" alt="Architecture: everything runs on the Watcher, audio goes straight to Gemini Live" width="900"></p>

Bắp is a thin layer on top of [xiaozhi-esp32](https://github.com/78/xiaozhi-esp32): a new
`Protocol` that speaks the Gemini Live API, plus `assistant::` modules for configuration, tools,
web UI, faces, menu and input. Upstream changes live in one small patch,
[`firmware/patches/xiaozhi-esp32.patch`](firmware/patches/xiaozhi-esp32.patch).

<details>
<summary><b>A conversation, step by step</b></summary>
<br>
<p align="center"><img src="docs/images/diagrams/session-flow.svg" alt="A conversation step by step, with timings measured on the device" width="900"></p>
</details>

<details>
<summary><b>Characters, apps and languages are data</b></summary>
<br>
<p align="center"><img src="docs/images/diagrams/data-driven.svg" alt="assistant.json and NVS overrides become the prompt, UI strings and faces" width="900"></p>
</details>

More: [architecture](docs/architecture.md) · [adding a tool](docs/adding-a-tool.md) ·
[adding a character](docs/adding-a-character.md).

### ⚡ Performance

<p align="center"><img src="docs/images/diagrams/performance.svg" alt="Before and after: latency, CPU, size" width="900"></p>

The main levers were TLS session tickets for every connection, fixed-point ECC, task stacks in
PSRAM, quantised face animations, fewer codecs, and erase-ahead OTA writes with the wake word and
camera paused. `GET /api/perf` reports per-task CPU, stack headroom, heap, uptime and Wi-Fi signal.

<details>
<summary><b>Flash layout and RAM budget</b></summary>
<br>
<p align="center"><img src="docs/images/diagrams/flash-layout.svg" alt="32 MB flash layout and RAM budget" width="900"></p>
</details>

## 🎛️ Controls

<p align="center"><img src="docs/images/diagrams/controls.svg" alt="Wheel and touch gestures" width="900"></p>

| State | Wheel | Touch |
| --- | --- | --- |
| Resting | rotate: volume · double press: apps · triple press: power off | tap: giggle · double tap: talk |
| Talking | rotate: volume · press: pause / resume | tap: interrupt · double tap: end |
| Music | — | double tap: stop |
| Anywhere | hold 1 s: menu · hold 20 s: factory reset | hold: menu |
| Menu | rotate / press: move / open | drag or tap top / bottom: move · tap centre: open |

## ⚙️ Settings page

<table>
<tr>
<td align="center"><img src="docs/images/web/chat.png" width="200"><br><sub>Chat, now playing, quick asks</sub></td>
<td align="center"><img src="docs/images/web/characters.png" width="200"><br><sub>Characters and personas</sub></td>
<td align="center"><img src="docs/images/web/health.png" width="200"><br><sub>Device health</sub></td>
<td align="center"><img src="docs/images/web/chat-dark.png" width="200"><br><sub>Dark mode</sub></td>
</tr>
</table>

<sub>Screenshots use sample data.</sub>

## 🔒 Privacy and security

- **The API key stays on the device** (NVS, or built in from `secrets/`). The browser only sees a
  masked key, and the device sends it only to Google over TLS. Anyone with the device or your built
  `bap.bin` can read it, so use a dedicated key with a quota and never share built binaries.
- **The settings page is LAN-only**, with an optional password (HTTP Basic, salted and iterated
  SHA-256). Every change needs an `X-Bap` header, which blocks cross-site form posts. Do not expose
  port 80 to the internet.
- **Signed updates.** Builds are signed with your own RSA-3072 key (`firmware/scripts/ota_key.sh`
  creates `secrets/ota_signing_key.pem`; `build.sh` signs on the host). A device running signed
  firmware refuses any Wi-Fi update that is unsigned, modified or signed with another key. No eFuses
  are burned: USB flashing still works, which is also how a lost key is replaced. Back the key up.
- **Audio goes to Gemini only during a conversation**; the session closes after 30 s of silence.
  Camera images leave the device only when the assistant calls the photo tool.
- **`nvsfactory` at `0x9000`** (Seeed's device keys) is never written: the flash scripts only touch
  `0x0`, `0x8000`, `0x10d000`, `0x200000` and `0xa00000`.
- Never commit `secrets/`, `backup/`, `server/.env`, `vendor/`, `firmware/build/` or build logs.
  See [CONTRIBUTING.md](CONTRIBUTING.md).

## 🧑‍💻 Development

```bash
python3 firmware/scripts/validate_data.py      # data, tool names, web tool calls, translations
for t in firmware/tests/test_*.cc; do g++ -std=c++17 -I firmware/src/assistant -o /tmp/t "$t" && /tmp/t; done
firmware/scripts/export_patch.sh               # after editing vendor/, refresh the patch
python3 firmware/tests/e2e_device.py bap-xxxx.local --log serial.log   # end-to-end: web API, every tool, real conversations
```

<details>
<summary><b>Repository layout</b></summary>

```
firmware/
  src/assistant/       Bắp modules: config, tools, web server, faces, menu, input, radio, Zing, SD
  src/protocols/       GeminiLiveProtocol and TicketSsl (TLS session resumption)
  data/assistant.json  characters, apps, radio stations, languages
  web/index.html       settings page served by the device
  patches/             the patch on top of upstream xiaozhi-esp32
  scripts/ tests/      patch tooling, data validation, host-side unit tests
docs/                  architecture, guides, images and diagrams
site/                  documentation site (Next.js + Nextra), deployed at bap.nrl.ai
tools/                 desktop companion (Rust) and Gemini key helper
```

</details>

CI runs the unit tests, data validation, clang-format, a firmware build with an empty API key and a
gitleaks secret scan.

## 📄 License

[MIT](LICENSE) for Bắp's source code. Built on [xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)
(MIT); `TicketSsl` is derived from [esp-ml307](https://github.com/78/esp-ml307) (Apache-2.0). Fonts:
[Nunito](https://github.com/googlefonts/nunito) and [Noto Sans KR/SC](https://github.com/notofonts/noto-cjk)
(SIL OFL 1.1). The lunar calendar follows Hồ Ngọc Đức's published algorithm.

<sub>Bắp is not affiliated with Seeed Studio or Google. "SenseCAP" and "Gemini" are trademarks of their
owners.</sub>
