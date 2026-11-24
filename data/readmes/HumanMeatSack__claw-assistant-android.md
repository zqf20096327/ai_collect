<h1 align="center">Claw Assistant for Android™</h1>

<p align="center"><strong>An on-phone brain. Your Android Side button.</strong></p>

<p align="center">Developer preview · Phone-local Qwen3-4B · Built on OpenClaw</p>

<p align="center">
  <a href="#quick-start">Quick start</a> ·
  <a href="docs/demo.md">Try the demo</a> ·
  <a href="android/README.md">Android build</a> ·
  <a href="gateway/README.md">Optional Gateway setup</a>
</p>

<p align="center">
  <img src="docs/media/aiden-flow.svg" alt="Android handles offline recognition, imported Qwen3-4B conversation, phone utilities, and voice playback. A private Gateway and explicit Codex handoff are optional network routes." width="920">
</p>

Hold the Side button to open **Aiden** over the app you’re using. Speak or type a request, get an answer, and continue the conversation. With the verified Qwen3-4B model imported and enabled, ordinary conversation runs on the phone. Parakeet handles offline English recognition, and an installed offline Android voice speaks the reply. An optional build adds Alba.

Your own OpenClaw Gateway remains available as a separate conversation route. Explicit **“Ask Codex”** requests can use its optional Codex integration. A failed local reply does not silently send ordinary conversation to the Gateway.

## What you can try

| On your phone | What Aiden does |
| --- | --- |
| Hold the Side button | Opens the panel and starts continuous voice entry. |
| Say “Hey Aiden” with hands-free listening armed | Opens the panel over another app on an unlocked phone. |
| Type in the panel | Answers with the enabled phone model and keeps short context for follow-ups in that panel. |
| Ask for battery level or free phone storage | Reads supported live phone information. |
| Say “Open Calculator” or “Set a timer for five minutes” | Runs a supported utility on the phone. |
| Say “Ask Codex” and state a question | Uses the optional configured Gateway/Codex route, which requires a network connection. |

This is a developer preview, not complete Gemini feature parity. It does not autonomously operate arbitrary screens across other apps. Opening another app can end the panel’s conversation. Screen captures and sensitive message-related requests retain their review flows.

**Home Assistant and verified web lookup services are not bundled.** Their Android integration points require a separate Gateway backend. The included Gateway example provides host checks and optional model/Codex routing; it does not implement `aiden.phone.lookup` or `aiden.phone.control`.

<p align="center">
  <img src="docs/media/panel-emulator.png" alt="Historical emulator screenshot of Aiden’s panel over Stopwatch showing a local battery reading" width="280"><br>
  <sub>Historical v0.1.0 emulator demo: the panel reads Android’s battery level.</sub>
</p>

## Quick start

1. Build with the [Android guide](android/README.md). The preview installs alongside regular OpenClaw as `ai.openclaw.app.aiden.preview`. Live panel replies use an installed offline Android TTS voice by default.
2. For phone-local conversation, download the pinned Qwen3-4B model separately. Open **Settings → Voice → Local phone agent → Import Qwen3-4B model**, then enable **Use phone model**. The [guide](android/README.md#enable-phone-local-conversation) lists the exact artifact and checksum. Qwen weights are not bundled.
3. Select Aiden under Android’s **Settings → Apps → Default apps → Digital assistant app**. On a compatible Galaxy, map the Side button’s long press to the digital assistant.
4. Open the panel and talk, or tap the input field to type. For background wake, choose **Use screen → Hey Aiden hands-free → Start listening**, close the panel, and keep the phone unlocked. End voice mode with **End conversation** or **“stop conversation.”**
5. Optionally pair a private Gateway for its separate conversation route and explicit Codex requests. See the [Gateway guide](gateway/README.md).

First model loading takes longer than a warm reply. Use **Warm up phone model** before a test. Voice timing, interruptions, and initial microphone handoff need checks on each handset; there is no fixed response-time promise.

## Where your data goes

- Wake detection and Parakeet recognition run on the phone. Wake listening uses Android’s microphone foreground service with a persistent **Stop** notification.
- With **Use phone model** enabled, ordinary panel conversation and supported direct phone actions stay on the phone. Import grants access to one file and makes a verified private copy; it does not request storage-wide access.
- Live panel replies use installed offline Android TTS by default. Optional Alba also synthesizes on the phone. Setup downloads require internet access.
- Full Chat → **Listen** is a separate playback flow: it tries optional Alba, then configured Gateway synthesis, then Android system TTS. It can use the network when Alba is unavailable.
- The Gateway route sends conversation text to your authenticated Gateway. Its model/tool configuration determines further processing. Screen-context flows show material for review before sending it.
- Explicit Codex delegation, when configured, sends the request and bounded visible call context through your Gateway to Codex/OpenAI. It is not offline processing.

## Preview status

The development handset is a Galaxy S24 Ultra running Android 17. The local runtime is an ARM64/GPU-oriented preview; other devices and audio routes need their own checks. Background wake is user-armed and may need restarting after an update, reboot, or force stop.

See the [demo and validation notes](docs/demo.md) for the distinction between the current public export, historical emulator checks, and development-handset observations. The repository supplies source and preparation instructions. See the [changelog](docs/CHANGELOG.md) for the current scope.

## Credits

This community preview builds on [OpenClaw](https://github.com/openclaw/openclaw). The [Android guide](android/README.md) records the pinned revision, speech assets, and model import. See the [MIT license](LICENSE) and [third-party notices](THIRD_PARTY_NOTICES.md) for their individual terms.

Android is a trademark of Google LLC.
