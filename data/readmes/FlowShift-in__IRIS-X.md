<div align="center">

![IRIS-MX Mobile AI Assistant](./assets/banner.png)

### Voice-First Mobile AI Execution System (v1.3.1)

**Speak naturally. Control your Mobile Device. Automate Workflows on Android with Voice Commands.**

---

<div style="display: flex; justify-content: center; gap: 10px; margin-bottom: 20px;">

  <a href="https://github.com/IRISX-AI/IRIS-X/stargazers">
    <img src="https://badgen.net/github/stars/IRISX-AI/IRIS-X?color=ff6600&icon=github" alt="GitHub stars">
  </a>

  <a href="https://github.com/IRISX-AI/IRIS-X/network/members">
    <img src="https://badgen.net/github/forks/IRISX-AI/IRIS-X?color=ff6600&icon=github" alt="GitHub forks">
  </a>

  <a href="https://github.com/IRISX-AI/IRIS-X/graphs/contributors">
    <img src="https://badgen.net/github/contributors/IRISX-AI/IRIS-X?color=ff6600&icon=github" alt="Contributors">
  </a>

  <a href="https://irisxai.in/download/mobile">
    <img src="https://badgen.net/badge/Download/Mobile%20APK%20v1.3.1/ff6600?icon=android" alt="Download Mobile APK">
  </a>

  <a href="https://irisxai.in/pricing/iris-mx">
    <img src="https://badgen.net/badge/License/Mobile%20PRO/10b981" alt="Mobile PRO License">
  </a>

</div>

**Speak your command. IRIS-MX executes it directly on your phone.**

A voice-first mobile execution assistant powered by **Gemini 3.5 Flash Lite** & **Gemini Live WebSockets** (`wss://generativelanguage.googleapis.com/...`) with real-time bidirectional audio, floating system overlays, native app intents, hardware automation, incoming call control, real-time notification listener, and media session controls.

---

</div>

# 📑 Table of Contents

- [⚡ Overview](#-overview)
- [🎯 What is Voice-First Mobile?](#-what-is-voice-first-mobile)
- [✨ What's New in v1.3.1](#-whats-new-in-v131)
- [🛠️ Complete Tool Registry & Examples](#️-complete-tool-registry--examples)
- [🪡 Open Core Model & Code Protection](#-open-core-model--code-protection)
- [💰 Pricing & Licensing](#-pricing--licensing)
- [🚀 Download & Setup](#-download--setup)
- [📁 Project Structure](#-project-structure)
- [🤝 Contributing](#-contributing)
- [🔒 Security & Privacy](#-security--privacy)
- [👨‍💻 Architect & Contact](#-architect--contact)
- [📜 License](#-license)

---

# ⚡ Overview

IRIS-MX is not a basic chatbot.

It is a **Voice-First Mobile AI Assistant** built on the powerful IRIS-AI Voice Engine. It listens to your spoken commands in real-time and executes real actions directly across your phone—answering/rejecting incoming phone calls, announcing caller names out loud, reading and auto-replying to WhatsApp/Instagram notifications, controlling Spotify/YouTube media playback, opening apps, controlling hardware settings, and managing device tasks.

> **Speak naturally. IRIS-MX understands intent. Actions happen live on your mobile device.**

---

# 🎯 What is Voice-First Mobile?

Traditional phone apps force you to unlock your screen, find an icon, tap buttons, and type text.

IRIS-MX changes that completely: **You speak → IRIS hears you in real time → Actions execute on your phone.**

```
Your Spoken Voice
    ↓ (Bidirectional Real-Time PCM Stream)
Gemini 3.5 Flash Lite (WebSocket BidiGenerateContent)
    ↓ (Intent & Action Recognition)
IRIS Mobile Execution Engine
    ↓ (Native Kotlin Modules & Hardware APIs)
Calls / Notifications / Spotify / WhatsApp / Settings / Camera / Overlays
```

- **Latency:** Sub-second zero-latency bidirectional voice streams.
- **Interruption-Proof Real-Time Injection:** Out-of-band live event payload streaming via `realtimeInput` so background notifications don't break active AI speech generation.
- **Acoustic Echo Protection:** Ultra-early synchronous mic auto-mute and 200ms post-unmute acoustic decay protection to eliminate residual echo feedback loops.
- **Background Resilient:** Runs via floating system overlays and background service loops.
- **Multimodal Screen Streaming:** Real-time screen capture streaming directly to the AI for visual context.

---

# ✨ What's New in v1.3.1

### 📞 1. Incoming Call Management & Caller Name Announcer

- **Native TelecomManager Integration:** Detects incoming ringing calls, resolves contact names from `ContactsContract.PhoneLookup`, and accepts or declines calls hands-free.
- **TTS Caller Announcer:** Announce caller identity out loud via native Text-To-Speech.

### 🔔 2. Real-Time System Notification Listener & Auto-Responder

- **Background Notification Engine:** Continuous `NotificationListenerService` capturing incoming messages from WhatsApp, Instagram, Telegram, and SMS system packages.
- **Autonomous RemoteInput Auto-Reply:** Generates intelligent, concise AI responses and sends background inline replies without user interaction.

### 🎵 3. Advanced System-Wide Media Controller

- **MediaKey Intent Broadcasts:** System-wide controls for active playback sessions across Spotify, YouTube, Apple Music, and podcast players.
- **MediaSessionManager Integration:** Directly queries and controls active system media sessions.

### ⚡ 4. Gemini 3.5 Flash Lite & Raw WebSocket Pipeline

- Standardized low-latency raw JSON WebSocket protocol over `wss://generativelanguage.googleapis.com/ws/google.ai.generativelanguage.v1beta.GenerativeService.BidiGenerateContent`.
- Powered by `models/gemini-3.5-flash-lite`.

---

# 🛠️ Complete Tool Registry & Examples

IRIS-MX equips Gemini Live with native mobile system execution tools:

### 📞 1. Cellular Phone Call Controller (`control_incoming_call`)

- **Description:** Controls incoming cellular phone calls (answer, reject, or announce caller ID).
- **Parameters:** `action` (`"answer" | "reject" | "announce"`)
- **Use Cases & Prompts:**
  - _"Who is calling right now?"_ -> Announces incoming caller name.
  - _"Iris, answer the call."_ -> Accepts ringing call via TelecomManager.
  - _"Reject the call."_ -> Hangs up incoming call.

### 🔔 2. System Notification Listener & Auto-Responder (`manage_notification_listener`)

- **Description:** Reads incoming WhatsApp, Instagram, and SMS system notifications in real-time or manages automated auto-reply mode.
- **Parameters:** `action` (`"read_latest" | "enable_auto_reply" | "disable_auto_reply"`), `appFilter` (optional)
- **Use Cases & Prompts:**
  - _"Read my latest WhatsApp notifications."_ -> Fetches recent unread messages.
  - _"Check if I have any new Instagram messages."_ -> Filters notifications by app.
  - _"Turn on auto-reply mode."_ -> Enables autonomous background AI replies.

### 🎵 3. System-Wide Media Playback Controller (`control_media_playback`)

- **Description:** Controls system-wide media playback (play, pause, toggle, next track, previous track) for apps like Spotify, YouTube, and Apple Music via system MediaKey intents.
- **Parameters:** `action` (`"play" | "pause" | "toggle" | "next" | "previous"`)
- **Use Cases & Prompts:**
  - _"Pause the music."_ -> Sends `KEYCODE_MEDIA_PAUSE`.
  - _"Skip to the next song."_ -> Sends `KEYCODE_MEDIA_NEXT`.
  - _"Go back to the previous track."_ -> Sends `KEYCODE_MEDIA_PREVIOUS`.
  - _"Toggle playback."_ -> Sends `KEYCODE_MEDIA_PLAY_PAUSE`.

### 💬 4. WhatsApp Messaging (`send_whatsapp_message`)

- **Description:** Looks up contact phone number and opens direct WhatsApp chat window pre-filled with the message.
- **Parameters:** `contactName`, `message`
- **Use Cases & Prompts:**
  - _"Send a WhatsApp message to Sidhu saying I'm running 10 minutes late."_
  - _"Message Mom on WhatsApp asking what's for dinner."_

### 📞 5. Contacts Search & Direct Phone Calls (`search_contacts`, `make_phone_call`, `send_sms_message`)

- **Description:** Searches device contacts, places calls, or sends cellular SMS messages.
- **Parameters:** `contactNameOrNumber`, `message`
- **Use Cases & Prompts:**
  - _"Find Alex in my contacts."_
  - _"Call Rahul."_
  - _"Send an SMS to Rahul saying call me back."_

### 🔗 6. App Launching & Deep Linking (`open_deep_link`, `open_app`, `close_app`)

- **Description:** Launches native apps or deep-links directly to search queries in YouTube, Spotify, Maps, or Chrome.
- **Parameters:** `targetApp`, `query`, `appName`
- **Use Cases & Prompts:**
  - _"Play Believer on YouTube."_
  - _"Open Spotify and play synthwave."_
  - _"Open Settings."_

### ⚡ 7. Hardware & Settings Teleport (`control_device_hardware`)

- **Description:** Toggles device hardware (Flashlight) or navigates directly to Wi-Fi, Bluetooth, Location, and Hotspot settings panels.
- **Parameters:** `target` (`"flashlight" | "wifi" | "bluetooth" | "location" | "hotspot"`), `action` (`"on" | "off" | "toggle" | "open"`)
- **Use Cases & Prompts:**
  - _"Turn on flashlight."_
  - _"Open Wi-Fi settings."_

### 📅 8. Calendar & Memory Management (`check_schedule`, `schedule_new_event`, `save_core_memory`, `access_core_memory`)

- **Description:** Scans native OS calendar for 48-hour schedule, creates events, or persists user facts.
- **Parameters:** `title`, `hoursFromNow`, `durationMinutes`, `fact`
- **Use Cases & Prompts:**
  - _"What's on my calendar for today?"_
  - _"Schedule a meeting titled Team Sync 2 hours from now for 30 minutes."_
  - _"Remember my car parking spot is level 2."_
  - _"What is my car parking spot?"_

---

# 🪡 Open Core Model & Code Protection

IRIS-MX is built on an **Open Core commercial model**:

- **Public Repository ([IRIS-X](https://github.com/IRISX-AI/IRIS-X))**: Contains the user interface shell, navigation layout, theme system, and community integration examples.
- **Private Production Core**: The core native voice execution engine, native Kotlin modules (`modules/overlay-service`, `modules/pcm-stream-player`, `modules/iris-autonomous`), low-latency PCM audio stream pipelines, and background automation logic are protected and private.

> 🔒 **IRIS-MX is a paid software.** The public repository allows developers to inspect the UI shell, but full AI execution requires an active **Mobile PRO License**.

---

# 💰 Pricing & Licensing

To use the full IRIS-MX Mobile AI Voice Assistant, you must activate a **Mobile PRO License**.

- 💳 **Purchase Mobile PRO License:** [https://irisxai.in/pricing/iris-mx](https://irisxai.in/pricing/iris-mx)
- 📲 **Download Official Mobile APK:** [https://irisxai.in/download/mobile](https://irisxai.in/download/mobile)

_License activation is tied to your account and grants full access to native voice execution, background overlay permissions, real-time screen streaming, and autonomous call/notification handling._

---

# 🚀 Download & Setup

### 📲 For Mobile App Users

1. Download the official release APK (v1.3.1) directly from: [https://irisxai.in/download/mobile](https://irisxai.in/download/mobile)
2. Install the APK on your Android device.
3. Open IRIS-MX, sign in, and grant required permissions (**Microphone**, **Display Over Other Apps**, **Notification Listener**, **Phone/Contacts**).
4. Enter your Gemini API Key in Settings and tap **Start AI**!

### 💻 For Developers (UI Shell)

To run and inspect the public frontend shell locally:

```bash
# 1. Clone the public repository
git clone https://github.com/IRISX-AI/IRIS-X.git
cd IRIS-X

# 2. Install dependencies
npm install

# 3. Start Expo development server
npm run start
```

---

# 📁 Project Structure

```
IRIS-MX/
├── android/                        # Android native project wrapper
│   ├── app/                        # Main Android application module
│   └── build.gradle
├── modules/                        # Custom Native Expo Kotlin Modules
│   ├── iris-autonomous/            # Notification Listener, Call Screening & MediaSession Kotlin engine
│   ├── overlay-service/            # Floating System Overlay FGS & Foreground Service
│   ├── pcm-stream-player/          # Zero-latency PCM stream AudioTrack player & MediaKey dispatch
│   └── screen-capture/             # Native Screen Recording & Vision Streamer
├── src/
│   ├── app/                        # Expo Router Navigation & Screen Pages
│   │   ├── (tabs)/                 # Main Navigation Tabs (Home, Notes, Profile)
│   │   ├── settings/               # Settings & API Key Configuration
│   │   └── _layout.tsx
│   ├── components/                 # UI Components & Glassmorphic Dock
│   │   ├── IrisDock.tsx            # Main Control Floating Dock
│   │   └── IrisQuantumHUD.tsx      # Holographic Voice HUD
│   ├── logic/                      # React Native Execution Bridges
│   │   ├── autonomous-agent.ts     # Autonomous Notification & Call Handler Engine
│   │   ├── call-control.ts         # Incoming Call Management Bridge
│   │   ├── media-control.ts        # System MediaKey Execution Bridge
│   │   ├── notification-agent.ts   # Notification Listener State Manager
│   │   ├── calendar-agent.ts       # Native OS Calendar Integration
│   │   ├── contacts-agent.ts       # Contacts & Cellular Intent Bridge
│   │   ├── app-control.ts          # Application Launcher Bridge
│   │   └── hardware.ts             # Hardware Teleport & Settings Controller
│   ├── services/                   # Core Voice & Network Services
│   │   ├── WebSocketService.ts     # Raw Gemini Live WebSocket Protocol & Out-of-band Live Injection
│   │   ├── AudioInputService.ts    # Native Mic FGS Streamer & Post-Unmute Echo Protection
│   │   ├── AudioOutputService.ts   # Zero-Latency AudioTrack Output Streamer
│   │   ├── OverlayOrchestrator.ts  # Background Overlay & System State Manager
│   │   ├── PermissionsService.ts   # Android Permission Gatekeeper
│   │   └── ApiKeyService.ts        # Secure Local BYOK Vault
│   ├── tools/
│   │   └── tools.ts                # Master Mobile Tool Declarations & Router
│   └── store/
│       └── authStore.ts            # Authentication & License Gatekeeper
├── app.json                        # Expo App Configuration
├── package.json                    # Project Dependencies (v1.3.1)
├── tsconfig.json                   # TypeScript Config
└── README.md
```

---

# 🤝 Contributing

We welcome UI improvements, bug fixes, and community contributions to the frontend shell!

1. Fork the repository [IRISX-AI/IRIS-X](https://github.com/IRISX-AI/IRIS-X).
2. Create your feature branch (`git checkout -b feat/my-new-widget`).
3. Commit your changes (`git commit -m "Add new UI component"`).
4. Push to the branch and open a Pull Request.

---

# 🔒 Security & Privacy

- **100% Bring-Your-Own-Key (BYOK):** Your Gemini API Key is stored encrypted in your device's secure local storage and never leaves your device.
- **Biometric & Permission Control:** System overlays, notification listener, and microphone access are explicitly requested and can be toggled anytime in Settings.
- **Zero Data Logging:** No audio streams, notification contents, or conversation logs are recorded or sold.

---

# 👨‍💻 Architect & Contact

**Harsh Pandey**  
Founder & AI Systems Architect, IRISX-AI

- 🌐 **Website:** [https://irisxai.in](https://irisxai.in)
- 📧 **Source Code & Enterprise Inquiries:** `irisaidevop@gmail.com`
- 🎬 **Instagram:** [@irisx.ai](https://www.instagram.com/irisx.ai)
- 💻 **GitHub:** [@201Harsh](https://github.com/201Harsh) | [@IRISX-AI](https://github.com/IRISX-AI)

---

# 📜 License

The UI Shell in this repository is licensed under the **MIT License**.  
The core IRIS-MX native voice engine and agent execution logic are proprietary software subject to the **IRIS-MX Commercial License**.

See [LICENSE](LICENSE) for full details.

---

<div align="center">

**System Online. IRIS-MX v1.3.1 Activated.**

Made with ❤️ by [Harsh Pandey](https://instagram.com/201Harshs)

</div>
