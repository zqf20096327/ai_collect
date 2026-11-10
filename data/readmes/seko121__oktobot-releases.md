# Oktobot

<img src="banner.png" alt="Oktobot: your AI agent, in your pocket">

**An AI agent for Android that works for you, not just chats.** Give it a goal and it searches, browses, opens apps and uses your phone step by step until the task is done. You choose the AI: your own cloud API key, a ChatGPT / Claude / Kiro / Antigravity subscription, or a model that runs entirely on your phone.

- **Phone control, your way:** Accessibility, or Shizuku / ADB for faster and more robust control, plus a separate small screen where the agent works while you keep using your phone.
- **Everything in one agent:** voice and video calls, AI browser, image generation and editing, memory, MCP servers, Agent Skills (Claude / OpenClaw format), scheduled tasks and a sandboxed Linux shell.
- **Private by design:** no account and no server of ours; conversations and memory stay on your device.

> **Oktobot is closed-source.** This repository only hosts signed release builds, release notes and documentation. License: proprietary, all rights reserved.

## What it does

- **Controls your phone.** Opens apps, taps, swipes, types and reads the screen through the Accessibility service (optional, off until you enable it). It can also drive the phone over Shizuku/ADB instead of Accessibility.
- **AI browser.** An in-app browser the agent can navigate, read and act in, plus web search (DuckDuckGo, Brave, Tavily, Google).
- **Multi-agent.** Create several agents, each with its own instructions, model, tools and memory, and switch between them.
- **Voice and video calls.** Talk to the agent hands-free with speech recognition and TTS, or start a video call so it can see through your camera.
- **Create images.** Generate images, or attach a photo and have the model edit it.
- **MCP.** Connect Model Context Protocol servers; rich MCP App widgets render inside the chat.
- **Skills.** Supports Agent Skills (the `SKILL.md` format used by Claude and OpenClaw), including a ClawHub marketplace to search, inspect and install skills, with safety checks before anything installs.
- **Many models, your choice.** Cloud API keys (OpenAI, Anthropic, Gemini, DeepSeek, OpenRouter and more), ChatGPT and Claude sign-in, or on-device models. Bring your own provider.
- **Memory.** Remembers what you ask it to, with a graph view and a review step before anything is saved.
- **Linux sandbox.** Run Ubuntu or Alpine on the device.
- **Automation.** Scheduled tasks, heartbeat checks, and a wake word.

## Screenshots

<p>
<img src="screenshots/01-home.jpg" width="23%"> <img src="screenshots/02-subscription.jpg" width="23%"> <img src="screenshots/03-voice.jpg" width="23%"> <img src="screenshots/04-skills.jpg" width="23%">
</p>
<p>
<img src="screenshots/05-artifacts.jpg" width="23%"> <img src="screenshots/06-memory.jpg" width="23%"> <img src="screenshots/07-privacy.jpg" width="23%">
</p>

## Download

<a href="https://play.google.com/store/apps/details?id=com.oktobot.app"><img alt="Get it on Google Play" src="https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png" height="80"></a>

**[Get Oktobot on Google Play](https://play.google.com/store/apps/details?id=com.oktobot.app)**

Or get the signed APK directly from GitHub:

Get the latest `Oktobot_vX.Y.Z.apk` from the [Releases page](../../releases/latest).

1. Download the APK on your phone (Android 9 or newer, arm64).
2. Allow installing from your browser/file manager when Android asks.
3. Verify the signature if you like (see below).

Updates install over the previous version as long as it is signed with the same key.

### Verify the download

Every release lists the SHA-256 of the APK. The signing certificate is the same for every release:

```
CN=OctoBot, OU=Mobile, O=OctoBot, L=Istanbul, C=TR
SHA-256: 37:5D:E2:F9:8A:45:19:6F:9E:E9:F0:9C:BC:C3:E5:6F:5B:22:E4:EB:78:43:C8:C2:7D:96:9C:F6:58:FE:B6:DB
```

```bash
apksigner verify --print-certs Oktobot_vX.Y.Z.apk
sha256sum Oktobot_vX.Y.Z.apk
```

## Shizuku support (optional)

Oktobot works fully without Shizuku. If you use [Shizuku](https://shizuku.rikka.app/) or **Shizuku Next**, Oktobot can use it for one thing: keeping its own accessibility service running.

- **Setup:** Oktobot → Settings → Permissions → *Shizuku & accessibility watchdog*. Every step shows a plain-language explanation first.
- **Grant:** with Shizuku running and permission granted, one button runs `pm grant <oktobot> android.permission.WRITE_SECURE_SETTINGS` (and, on Android 13+, `appops set <oktobot> ACCESS_RESTRICTED_SETTINGS allow`). The permission survives reboots, so the watchdog keeps working even when Shizuku is not running.
- **Watchdog (off by default):** detects "accessibility service disabled" or "enabled but not responding" and re-enables **only Oktobot's own entry** in `enabled_accessibility_services`, never other apps'. It checks after boot, about every 15 minutes and when the agent needs the service. Every automatic change shows a notification. Retries are limited (5 attempts per episode, with backoff). If it cannot fix things itself it asks you to open Accessibility settings.
- **Shizuku Next:** detection uses the Shizuku binder API, so it behaves the same with Shizuku and Shizuku Next. Turn on *Start on boot* and *Watchdog* in Shizuku Next so Shizuku itself stays up.

## Permissions

Oktobot asks only for what a feature needs, and tells you why: Accessibility (phone control), notifications, microphone (voice), camera and storage (attachments), overlay (floating assistant). Phone control is optional and off until you enable it.

## Support

Open an [issue](../../issues) with your Android version, device and Oktobot version. Please do not post API keys or personal data.
