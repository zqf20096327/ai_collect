<p align="center"><img src="docs/brand/wukong-wordmark.svg" width="360" alt="Wukong" /></p>

<p align="center">English · <a href="README.zh-CN.md">简体中文</a> · <a href="README.ja.md">日本語</a></p>

# Your words. Your phone in action.

**Wukong** is a personal AI agent for Android that turns a natural-language goal into actions across your phone, with requests, task cards, live previews and results in one conversation. Bring your own model, watch each step, and take over whenever you need to.

**[v0.0.2](https://github.com/linkecoding/wukong/releases/tag/v0.0.2) · Early preview · Android first.** Core flows have been tested on a Pixel 6; device compatibility and complete real-world tasks need broader validation. The current source also includes a [Wukong skill and local configuration page](docs/agent-integration.md): prefer the App, or run the on-phone planner without installation through local ADB/WebUSB, with scrcpy video; this addition is not in the original v0.0.2 APKs. MCP remains planned.

The app follows your **system language** by default (Chinese or English, with English as the fallback). Settings also offers manual language selection. Project introductions are also available in Japanese.


<p align="center">
  <a href="https://github.com/linkecoding/wukong/releases/download/v0.0.2/wukong-v0.0.2-cross-app-demo.mp4"><img src="docs/demo/wukong-cross-app.gif" width="320" alt="Real Android cross-app recording: read a recipe in Chrome, use the floating preview, take over and prepare a timer in Clock" /></a>
</p>

<p align="center">From a recipe in Chrome to a timer in Clock. Watch the floating screen, take over, then let the agent continue.<br /><a href="https://github.com/linkecoding/wukong/releases/download/v0.0.2/wukong-v0.0.2-cross-app-demo.mp4">Edited highlights · Full recording (40 s, MP4)</a> · <a href="docs/demo/README.md">Demo notes</a></p>

<details>
<summary>More screenshots</summary>

<p align="center">
  <img src="docs/images/conversation/home-en.png" width="280" alt="Wukong conversation interface" />
  <img src="docs/images/onboarding/model-en.png" width="280" alt="Model provider setup" />
</p>

</details>

## What you can do

- **Work across apps.** Launch apps, read UI elements, enter text, scroll, and navigate system screens. The starting app is optional.
- **See beyond UI elements.** Screenshots, on-device PP-OCRv6 tiny OCR, coordinate taps, long presses, and swipes supplement structured UI automation.
- **Watch and take over.** Run on the main display or a virtual display. Its preview is embedded in Wukong and floats when Wukong goes into the background. Close the floating preview without stopping the task; return to Wukong and leave again to show it. Manual takeover pauses the agent; handing back control triggers a fresh observation.
- **Bring your own model.** Connect a tool-calling Chat Completions compatible endpoint. Configure any HTTPS base URL or an exact request URL. Thinking is off by default where supported; models that require thinking are identified in the UI.
- **Program short workflows.** The model can use embedded QuickJS JavaScript for loops, conditions, UI-change listeners and phone operations, with explicit selectors, named outcome waits and desired-state setters. Each action retains local approvals and takeover checks. See [the JS runtime](docs/architecture/javascript-runtime.md).
- **Wait for results and verify outcomes.** Query matching controls or regions, wait for result/error conditions, and check fresh evidence before reporting success. See [query and verification behavior](docs/architecture/condition-tools.md).
- **Inspect each task.** Open a task card in the conversation or History to see its result, provider-reported token usage and grouped execution timeline. Expand an event for the recorded tool arguments and results. Optional logs remain on the phone. Save or share one run as a ZIP from its top-right menu.

Wukong includes wireless ADB pairing and its execution engine. **No root, enabled AccessibilityService, or companion app is required.** The app remains a normal Android app; user-authorized wireless debugging starts an `app_process` shell process (UID 2000).

## Get started

[Download and release notes](https://github.com/linkecoding/wukong/releases) · [First-task guide](docs/getting-started.md)

Screenshots and descriptions track the current `main` branch; tagged releases are versioned snapshots.

Choose the **arm64-v8a APK** for most current phones, or the universal APK for other architectures. Release builds use the project's production signing identity and include SHA-256 checksums. You can also build from source below.

1. Choose **Find a downloaded file** or **Search for answers**. Add a filename, a question, or an app and keyword—or write your own task.
2. Tap Send; if setup is incomplete, the guided setup opens. Select DeepSeek, Alibaba Cloud / Qwen, Zhipu / GLM, Moonshot / Kimi, or a custom API. Follow the provider's API platform link if you need a key. Wukong fills the standard endpoint; the connection and model fields use separate cards. After entering your key, open the model dropdown to load available IDs, or type an ID manually. A tool-call test checks the connection before saving and leaves you on the page. Clear a saved configuration from this page’s top-right menu.
3. Follow **Connect this phone**. Android 11+ requires Wi-Fi, Developer options, and Wireless debugging authorization. Wukong guides the current step; ports and manual pairing are tucked into troubleshooting.
4. Allow control buttons when prompted. Return to your saved task, review it, and tap the Send arrow. Setup does not start the task automatically.
5. On later launches, Wukong attempts to restore an already-paired connection when wireless debugging is available. Your pending task survives setup screens and app restarts.

Provider accounts and API balances are your own; no hosted trial service is included. See [the first-task guide](docs/getting-started.md) and [provider presets](docs/model-providers.md).
Android 10 can use the development USB activation script, but cannot use the built-in wireless pairing flow. Supported device behavior varies with Android and vendor restrictions.

## You stay in control

Routine actions run automatically. Only payments/transfers and destructive operations such as deleting files, erasing app data or resetting the device require local confirmation. Sending, publishing, sharing and routine permission changes proceed autonomously when needed for your task. This detection is heuristic and cannot recognize every sensitive control. Stop controls remain available; actions already accepted by Android cannot be undone. Passwords, verification codes, and device unlock require manual handling.

OCR runs locally, but **model inference uses your configured provider**. Task goals, recent conversation requests/results used for follow-ups, app lists, and relevant UI text are sent to that provider; using the screenshot tool also sends the captured image. This is not a fully offline agent. API keys and ADB identities are encrypted with Android Keystore. History and logs stay on the device; logs omit API keys and full screenshots / UI trees. The app retains up to 20 conversations with 20 turns each, 30 history entries and 20 logs of up to 512 KB each. Follow-ups include up to six recent turns with bounded summaries; a new conversation starts without that context.

Virtual-display previews currently update at about 3 fps. Protected content and apps with multi-display or single-task restrictions may not work independently on both displays.

To report a problem, open **task card > Execution details > top-right menu > Export this run** (also available from sidebar History). Save or share the ZIP containing `events.jsonl` and `manifest.json` (app/Android versions, device model and event count). It excludes screenshots and credentials from model configuration. Task text and tool arguments/results may still contain private information; review before sharing. Connection diagnostics support the same single-run export.

## How it works

![Wukong Android execution architecture](docs/images/architecture/wukong-architecture.en.svg)

Your configured model proposes actions; Wukong validates and executes them through its local shell engine. QuickJS runs in an isolated process and calls the same task validator through a restricted SDK. Wireless ADB activates the engine after system authorization. Users supply their own model API key; OCR runs on-device.

[Architecture details](docs/architecture.md) · [Download image](docs/images/architecture/wukong-architecture.en.png) · [中文架构图](docs/images/architecture/wukong-architecture.zh-CN.png)

## Build

Required: JDK 17, Android SDK 35, Build Tools 35.0.0, NDK 28.2.13676358, CMake 3.22.1. Versions are pinned to Gradle 8.11.1, AGP 8.9.2, and Kotlin 2.1.10.

```sh
# Configure JAVA_HOME and ANDROID_HOME first.
./scripts/gradle-local.sh :agent-core:test :shell-runtime:testDebugUnitTest :app:testDebugUnitTest :app:assembleDebug :app:lintDebug :shell-runtime:lintDebug

# Smaller development build for an arm64 phone
./scripts/gradle-local.sh -PtargetAbi=arm64-v8a :app:assembleDebug
```

APK: `app/build/outputs/apk/debug/app-debug.apk`. The shell payload is bundled automatically; no second app installation is needed. Release signing credentials are kept outside Git. See [signed builds and publishing](docs/releasing.md) and [development setup](docs/development.md) for toolchain details.

```text
app/             Native Android UI, model client, local storage, activation
agent-core/      Task loop, action validation, approvals, cancellation
shell-runtime/   app_process, UiAutomation, input injection, virtual display
third_party/     ADB transport, OCR models, trimmed native runtimes, notices
scripts/         Build tools, USB activation, device verification
```

For USB development activation only:

```sh
python3 scripts/activate-shell.py SERIAL
python3 scripts/activate-shell.py SERIAL --stop
```

The interface uses cream, moss and pale apricot. The conversation is home; a native side drawer holds recent conversations, History and Settings. Secondary pages use the Android Activity back stack. Execution options open as a Material bottom sheet. Model settings, device access, preferences and data controls have separate groups. Task logs open from history; connection-test diagnostics remain under Settings.

## Releases

`main` pushes and pull requests run build, unit tests and lint. A version tag such as `v0.0.2` builds signed arm64 and universal APKs, verifies APK signatures and 16 KB page alignment, and publishes a GitHub Release. Signing keys are stored locally and in encrypted Actions Secrets. See [release setup](docs/releasing.md).

## Community and project information

- [User guide](docs/getting-started.md) · [中文使用说明](docs/usage.zh-CN.md)
- [Changelog](CHANGELOG.md) · [0.0.2 release notes](docs/releases/0.0.2.md)
- [Contributing](CONTRIBUTING.md) · [Issues](https://github.com/linkecoding/wukong/issues)
- [Disclaimer and data handling](DISCLAIMER.md) · [Security reporting](SECURITY.md)

## Technical notes

- [Architecture](docs/architecture.md) · [Agent companion / skill](docs/agent-integration.md)
- [Visual tools and virtual display](docs/visual-virtual.md)
- [On-device OCR comparison](docs/ocr-v6-comparison.md) · [Native trimming and 16 KB validation](docs/ocr-native-trimming.md)
- [Autonomy and logs](docs/autonomy-logs.md) · [Validation notes](docs/validation.md) · [Real-app validation](docs/real-world-validation.md)
- [Third-party licenses and rebuild instructions](docs/third-party.md)
- [Brand assets and introduction copy](docs/brand/README.md)

Engineering notes are currently primarily in Chinese. The English README is the default project introduction.

## Acknowledgments and licensing

Research references: [Pinky](https://github.com/DIYgod/pinky), [Poki](https://github.com/josssphzhou/poki), and [ShadowAuto](https://github.com/android-notes/ShadowAuto). Wukong's application code and brand assets are implemented for this project.

Third-party components retain their own licenses and notices, including LGPL requirements for SPAKE2. See [third-party documentation](docs/third-party.md). **A license for Wukong's own source has not been selected yet.** Public availability alone does not grant an open-source license.
