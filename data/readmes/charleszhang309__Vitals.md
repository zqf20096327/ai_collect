<div align="center">

**English** | [简体中文](README_CN.md)

# Vitals

**Local-First Personal Status Hub, Cross-Device Controller & Wireless Studio Deck**

Unifies a customizable **Today Bento Dashboard**, real-time **Windows & macOS Hardware Monitoring & Remote Control**, an **iPad / iPhone Wireless Deck with Plugin Store**, **Apple Music-style Fullscreen Player & AMLL Lyrics**, **Cross-Device Scratchpad**, and an optional **AI Assistant** — designed with Liquid Glass aesthetics and zero cloud lock-in.

![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20iPadOS%2FiOS-0078D6?style=flat-square)
![Desktop](https://img.shields.io/badge/Desktop-Tauri%20v2-FFC131?style=flat-square&logo=tauri&logoColor=black)
![Backend](https://img.shields.io/badge/Backend-FastAPI%20%2B%20SQLite-009688?style=flat-square&logo=fastapi&logoColor=white)
![Frontend](https://img.shields.io/badge/Frontend-React%2019%20%2B%20Vite-61DAFB?style=flat-square&logo=react&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-34C759?style=flat-square)

</div>

---

## Screenshots

| Vitals Deck (Touch Console) | Overview Dashboard (Bento Widgets) |
| :---: | :---: |
| ![Vitals Deck](docs/screenshots/deck.png) | ![Today Dashboard](docs/screenshots/today.png) |

| Cross-Device Control & Audio | Fullscreen Now Playing & Lyrics |
| :---: | :---: |
| ![Control Center](docs/screenshots/control.png) | ![Fullscreen Lyrics](docs/screenshots/lyrics.png) |

---

## Prerequisites (For iPad / iPhone / Multi-Device Access)

If you only use Vitals on a single desktop, simply install the app and open `http://127.0.0.1:3993/`.  
To **access Vitals securely from your iPad, iPhone, or remote MacBook over HTTPS** (free, private tailnet, no public IP or port forwarding required), set up **Tailscale** first:

1. **Install & Sign in to Tailscale**: Install [Tailscale](https://tailscale.com/download) on your hub computer (Windows or Mac) and your iPad / iPhone / secondary Mac using the same account.
2. **Enable MagicDNS & HTTPS**:
   - Open the [Tailscale Admin Console → DNS](https://login.tailscale.com/admin/dns);
   - Enable **MagicDNS**;
   - Scroll down and click **Enable HTTPS**.
3. **Done**: In the Vitals desktop **Setup Wizard**, click **One-Click Setup** to automatically configure `tailscale serve --bg 3993` and generate your trusted `https://<your-device>.<your-tailnet>.ts.net/` URL with a QR code for your iPad/iPhone.

---

## Quick Start

### Option 1: Desktop Installer (Recommended — No Python / Node.js Required)

1. Download the latest release from **[GitHub Releases](https://github.com/charleszhang309/Vitals/releases/latest)**:
   - **Windows (x64)**: `Vitals_x.x.x_x64-setup.exe` (recommended) or `.msi`
   - **macOS (Apple Silicon)**: `Vitals_x.x.x_aarch64.dmg` (drag `Vitals.app` to `Applications`)
   - *(Note: Open-source builds are currently locally signed without Apple/EV notarization. If prompted by OS security on first launch, choose "Run anyway" / "Open anyway".)*
2. **First-Run Setup Wizard**:
   - **Hub Mode**: Click one-click setup to auto-configure Tailscale HTTPS, detect local weather & timezone, and generate a pairing token for secondary devices.
   - **Remote Agent Mode (e.g., secondary MacBook)**: Enter your hub's HTTPS URL and pairing token to sync hub data and run a lightweight outbound control agent.
3. **Tray / Menu Bar & Native Chrome**: Closing the main window releases WebView memory and minimizes Vitals cleanly to the Windows tray or macOS menu bar (macOS supports **Hide Dock Icon** and **Launch at Login** toggles).

---

### Option 2: Run from Source & Manual `config.json`

<details>
<summary>Expand source deployment and manual config.json reference</summary>

#### 1. Requirements
- **Windows 10/11** or **macOS 13+**
- **Python 3.10+**
- **Node.js 20.19+** or **22.12+**

#### 2. One-Click Dev Scripts
- **Windows**: Run `.\start_service.bat` in the repository root.
- **macOS**: Run `./start_service.sh` in the repository root.

The scripts automatically create `.venv`, install dependencies, copy `config.example.json` to `config.json`, build the frontend into `backend/static/`, and start the server on `0.0.0.0:3993`.

#### 3. Key `config.json` Fields
*(Desktop users can configure these visually under **Settings → Host Config** without editing JSON manually.)*
- `weather`: `city_name`, `latitude`, `longitude` (uses free Open-Meteo API).
- `health`: `timezone` (e.g. `America/Toronto`), optional `export_dir`, and `ingest_token`.
- `calendar.sources`: Two-way `icloud` (CalDAV + app-specific password), `google` / `outlook` (OAuth refresh token), and read-only `.ics` feeds.
- `ai`: `enabled`, `api_key`, `model`. Edit `backend/agent.md` to customize assistant persona with hot reload.
- `webhook`: `kind: "bark"`, `bark_url_template` (`https://api.day.app/<DEVICE_KEY>/{title}/{body}`), `daily_briefing_time`.
- `agents.token`: Shared pairing token for remote desktop agents.
- `launchers`: Whitelisted quick launchers (`[{"id": "steam", "name": "Steam", "kind": "app", "target": "..."}]`).

#### 4. Manual Tailscale Serve HTTPS
```bash
tailscale serve --bg 3993
tailscale serve status
```

</details>

---

## Core Features

### 1. Vitals Deck (Studio Glass + Plugin Store)
Click the grid icon in the top bar (especially great in fullscreen on an iPad next to your monitor):
- **Glass Keys & Custom Covers**. Mix standard `1×1` and wide `2×1` keys. Pick a vector icon or upload a PNG, JPG, WebP, or SVG cover that syncs across devices.
- **Touch Strip**. Adjust speaker and microphone volume, mute either channel, and play, pause, or skip on the selected host. Swipe the board to change scenes.
- **Four Key Types**: Trigger Actions, Two-State Toggles, Live Data Tiles (CPU/GPU temp, Focus countdown, AI quota), and Scenes / Nested Folders (`3×2` to `6×3` grids, drag-and-drop editing, JSON import/export).
- **Temporary Target Switching**: Control Windows or your remote MacBook directly from Deck; exits cleanly back to your default host when leaving Deck.
- **Built-in Universal Engine**:
  - Cross-platform **Hotkeys & Text Snippets** (Windows `SendInput`, macOS `CGEvent` / `osascript` — requires Accessibility permission on Mac).
  - **OS Desktop Presets**: Switch virtual desktops, snap windows, `Win+Tab` / Mission Control / `Cmd+Tab`.
  - **Multi-Action Macros** (up to 8 steps with configurable millisecond delays), **HTTP Webhooks** (configured on the hub in `config.json`), and native Vitals actions.
- **In-App Plugin Store & Open Plugin SDK (`plugins/`)**:
  - Install official or GitHub ZIP plugins, toggle enable/disable, and save plugin settings (such as OBS host/port/password) directly from iPad or desktop using the hub admin key (`GET /api/setup/deck/plugins/key`).
  - Ships with official cross-platform plugins for **OBS Studio** (9 actions + live recording/streaming/scene feedbacks via `obs-websocket` v5) and **DaVinci Resolve** (14 editing/color/transport actions).
  - Build your own plugins with our lightweight declarative contract in [Deck Plugin SDK](plugins/README.md).

### 2. Cross-Platform Control & 3-Tier Smart Sampling
- **Seamless Hub & Remote Switching**: Switch between Windows and MacBook in one click; offline agents hide automatically in Control view.
- **Hardware Telemetry & Smart Sampling**:
  - Windows uses LibreHardwareMonitor + `psutil` fallback (per-core loads, top 5 memory processes, usage/temperature charts); macOS reads native battery health/cycles and primary disk.
  - **Sampling Modes** (`Settings → System Status`):
    - **Smart** *(default)*: **1s** while a visible client is actively viewing Monitor/Control/Deck (auto-wakes immediately on interaction), **5s** while viewing Today/Scratchpad or in background, **15s** when all UI windows are closed (tray idle).
    - **Live**: Fixed **1s** interval.
    - **Eco**: Fixed **5s** interval.
- **Quick Controls & Screen Peek**: Power modes, Lock, Display Off, Sleep, Keep Awake (`caffeinate`), Scheduled Shutdown, Whitelisted Quick Launchers, and on-demand **Screen Peek** live screenshots.
- **Dual-Layer Audio & AMLL Fullscreen Lyrics**: Switch both speaker output and microphone input devices, mute/adjust levels independently, control media playback across players, and enjoy Apple Music-style fullscreen lyrics powered by `@applemusic-like-lyrics/react`.

### 3. Today Dashboard, Utilities & Bilingual UI
- **Customizable Bento Grid**: Toggle cards, reorder, and switch between `1×1` and `2×1` wide split layouts (**English & Simplified Chinese** instant switching, auto-matches system locale).
- **Widgets**:
  - **Weather** (Open-Meteo, AQI, hourly & 7-day forecast with automatic city geocoding & timezone).
  - **Health Rings & Trends** (compatible with iPhone *Health Auto Export v2* and Android *HCGateway / Health Sync / Tasker*).
  - **Two-Way Calendar** (iCloud CalDAV, Google Calendar, Outlook, `.ics` feeds).
  - **AI Usage Quota & Heatmap** (auto-parses local **Codex CLI** 5h/7d quotas and **Claude Code** 12-week token heatmaps).
  - **Tasks & Micro-Habits**, **Countdowns**, **Currency Converter** (`24H / 7D / 30D / 1Y` charts), **Fullscreen Focus Clock**, **Cross-Device Scratchpad** (file/image/text transfer + client-side PDF/DOCX/XLSX/CSV preview + pinning & search), and **Optional Expenses & Subscriptions** (custom base currency, monthly budget bar, and iPhone Apple Pay Shortcuts ingest).

---

## Mobile Integration (iPhone / Android)

<details>
<summary>1. iPad / iPhone PWA & Apple Pay Auto-Expense Shortcut</summary>

- **Install PWA**: Open `https://<your-device>.<your-tailnet>.ts.net/` in Safari on iPad/iPhone → Share → **Add to Home Screen** for fullscreen native-like Deck & Dashboard access.
- **Apple Pay Auto-Expense (iOS 17+ Shortcuts Automation)**:
  1. Open **Shortcuts → Automation → `+` → Transaction** (set to Run Immediately).
  2. Add **Get Contents of URL**:
     - URL: `https://<your-device>.<your-tailnet>.ts.net/api/expenses/ingest`
     - Method: `POST`, Body: `JSON` (`amount`, `merchant`, `card`).

</details>

<details>
<summary>2. Health Sync (Apple Health & Android Health Connect)</summary>

- **iPhone (Health Auto Export)**: Configure a **REST API** automation (`JSON / Version 2`) pointing to `https://<your-device>.<your-tailnet>.ts.net/api/health/ingest`.
- **Android**: Push JSON via **HCGateway** or **Tasker + Health Connect** to `/api/health/ingest`, or sync files via **Health Sync** to `health.export_dir`.

</details>

---

## Credits

- [Tauri](https://v2.tauri.app/) — Lightweight cross-platform desktop framework
- [Bitfocus Companion](https://github.com/bitfocus/companion) & [Macro Deck](https://github.com/Macro-Deck-App/Macro-Deck) — Architectural inspiration for the Action / Feedback / Variable plugin contract
- [LibreHardwareMonitor](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor) — Windows hardware sensors
- [AMLL (applemusic-like-lyrics)](https://github.com/amll-dev/applemusic-like-lyrics) — Apple Music-style synced lyrics rendering
- [LRCLIB](https://lrclib.net/) & [Open-Meteo](https://open-meteo.com/) — Free open lyrics, weather, air quality, and geocoding APIs
- [TaskBarWidget](https://github.com/NoctisWang528/TaskBarWidget) — Multi-source lyrics matching and AI usage heatmap design reference
- [FastAPI](https://fastapi.tiangolo.com/), [React](https://react.dev/), [Vite](https://vite.dev/), [ECharts](https://echarts.apache.org/), [Framer Motion](https://www.framer.com/motion/), [Lucide](https://lucide.dev/), [PyWinRT](https://github.com/pywinrt/pywinrt), [pycaw](https://github.com/AndreMiras/pycaw)

---

## License

Released under the [MIT License](LICENSE).
