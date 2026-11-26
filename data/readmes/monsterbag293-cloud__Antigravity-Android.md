# Google Antigravity for Android (Unofficial Port)

[![Platform: Android](https://img.shields.io/badge/Platform-Android%208.0%2B%20(arm64)-3DDC84.svg?style=flat&logo=android)](https://www.android.com/)
[![Built with: Kotlin & Jetpack Compose](https://img.shields.io/badge/Built%20with-Kotlin%20%7C%20Jetpack%20Compose-7F52FF.svg?style=flat&logo=kotlin)](https://developer.android.com/jetpack/compose)
[![Latest Release](https://img.shields.io/github/v/release/monsterbag293-cloud/Antigravity-Android?include_prereleases&label=latest%20release&color=blue)](https://github.com/monsterbag293-cloud/Antigravity-Android/releases/latest)
[![GitHub Stars](https://img.shields.io/github/stars/monsterbag293-cloud/Antigravity-Android?style=flat&logo=github)](https://github.com/monsterbag293-cloud/Antigravity-Android/stargazers)

An unofficial native Android port and mobile compatibility runtime for **Google Antigravity**, allowing developers to run Antigravity's autonomous agent environment and workspace directly on Android phones and tablets without requiring a desktop tether.

---

## 📥 Quick Download

**Get the latest version in one click:**

[![Download Latest Release](https://img.shields.io/badge/Download-Latest%20Release-blue?style=for-the-badge&logo=github)](https://github.com/monsterbag293-cloud/Antigravity-Android/releases/latest)

| Source | What you get | Recommended for |
|--------|--------------|-----------------|
| **[GitHub Releases](https://github.com/monsterbag293-cloud/Antigravity-Android/releases/latest)** | Latest signed APKs + release notes + SHA-256 checksums | Most users |

> Prefer the **Releases** page for the latest version, changelogs, and checksums.

---

## Table of Contents

- [Screenshots](#screenshots)
- [Features](#features)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Building from Source](#building-from-source)
- [Community, Issues & Feedback](#community-issues--feedback)

---

## Screenshots

<p align="center">
  <img src="docs/screenshots/antigravity_android_showcase.png" alt="Antigravity for Android UI Showcase" width="100%" />
</p>

| Google Sans Splash / Loading | Single-Conversation Chat | Interactive Sidebar Drawer | File Viewer |
| :---: | :---: | :---: | :---: |
| <img src="docs/screenshots/loading_screen.png" width="200" alt="Loading screen" /> | <img src="docs/screenshots/chat_view.png" width="200" alt="Chat view" /> | <img src="docs/screenshots/sidebar_drawer.png" width="200" alt="Sidebar Drawer" /> | <img src="docs/screenshots/Screenshot_20261122-175940.png" width="200" alt="Files and Web View" /> |

---

## Features

- **Native PRoot & Language Server Runtime**: Runs local language servers, gRPC-Web proxy streams, Python 3.12, Node.js v22, and Git natively inside an unprivileged Debian 12 ARM64 PRoot environment.
- **ARMv8.0 Compatibility Mode (QEMU)**: Bundled `libqemu-aarch64.so` with automatic `SIGILL` fallback (and a manual toggle in Host Settings) so older ARMv8.0 devices without LSE atomics can run the standalone backend.
- **Mobile-Optimized Popup Menus & Bottom Sheets**: Touch-friendly stacked bottom sheets for menus like Model -> View Usage, 3-dot menus, and Projects.
- **Android Launcher App Shortcuts**: Long-press the app icon for **New Chat**, **Workspace**, or **Settings** shortcuts that work on both cold and warm starts.
- **Secret Host Settings & Cloud Downloads**: Hold the sidebar **Settings** button for 10 seconds to toggle the Google-themed **Host Settings** menu ON or OFF; supports downloading cloud workspace files directly to your device.
- **Swarm & Automations Support**: Full Swarm sidecar UI, persistent scheduled automations with conversation reuse, and rich Android notifications showing the assistant's actual response.
- **Clean Project & Chat Storage**: Separates workspace files (`{Project Name}/main/`) from synced conversation databases (`{Project Name}/chats/{Chat Name}/`).
- **Mobile Touch Drawer & Haptics**: Fluid, GPU-accelerated left panel with live finger tracking, horizontal swipe gestures, and native haptic feedback.
- **Strict Single-Conversation Layout**: Removes desktop split-view anomalies on narrow viewports; sequential conversation clicks load cleanly within the viewport.
- **Customization & Plugin OAuth Support**: Single-tap Marketplace installs and external authentication flows (e.g. Google Drive, GitHub) via Chrome Custom Tabs.
- **Hold-to-Drag Sidebar Reordering**: Smooth vertical scrolling on conversation/project lists with a `380ms` long-press threshold to drag and reorder items.
- **Adaptive Vector Launcher Icon & Native Typography**: Official Antigravity gradient glyph inside Android's adaptive icon safe zone, paired with Google Sans and Material 3 design tokens.

---

## Installation

### Method 1: Direct Install on Android Phone / Tablet (Recommended)
1. Download the APK from the [latest version](https://github.com/monsterbag293-cloud/Antigravity-Android/releases/latest) on the Releases page.
2. Tap the downloaded file in your browser or File Manager.
3. If prompted, allow “Install from unknown sources” for your browser / file manager.
4. Tap **Install** and open the app. *(If upgrading from an older debug build to a release-signed build, uninstall the debug build first.)*

### Method 2: Via ADB (Android Debug Bridge)
If your device is connected to a computer with USB debugging enabled:

```bash
# Install the downloaded APK:
adb install -r path/to/antigravity-release.apk
```

To launch the app directly via command line:
```bash
adb shell am start -n dev.agentic.workspace/.MainActivity
```

---

## Project Structure

```text
Antigravity-Port/
├── app/                        # Android application module (Compose UI, MainActivity)
│   ├── src/main/kotlin/        # App navigation, WebView host, native bridges
│   └── src/main/res/           # Adaptive launcher icons, shortcuts, drawables, themes
├── core/
│   ├── data/                   # Local storage, key-value repositories
│   ├── designsystem/           # Themes, colors, typography (Google Sans)
│   ├── model/                  # Domain models (Conversations, Projects, Agents)
│   └── network/                # Jetski bundle loader, gRPC-Web frame codec, HTTP interceptor
├── feature/
│   ├── agentmanager/           # Custom agent creation and runtime controller
│   ├── browser/                # Integrated web browser pane
│   ├── conversations/          # Chat history and thread management
│   ├── files/                  # Workspace file browser and editor
│   ├── projects/               # Local folder projects and workspace manager
│   ├── settings/               # Host Settings UI and connection configuration
│   └── terminal/               # Local command runner and terminal shell
├── docs/screenshots/           # Screenshots shown in this README
├── dist/                       # Local packaged APK binaries (gitignored)
└── .github/                    # Issue forms, discussion templates, CI/CD workflows
```

---

## Building from Source

### System Requirements
- **Local Engine (Standalone PRoot):** 64-bit ARM device (`arm64-v8a`) running **Android 8.0 (API 26) or higher**. ARMv8.1+ CPUs run natively; older ARMv8.0 CPUs without LSE atomics are supported via the built-in QEMU Compatibility Mode.
- **Remote Host / Cloud Mode:** **Android 8.0 (API 26) or higher** on any 64-bit device.
- **RAM Recommendation:** 6 GB+ recommended for the local standalone engine (4 GB for remote mode).

### Prerequisites (Building from Source)
- JDK 17 or higher
- Android SDK (API 34 / Build-Tools 34.0.0)

### Build Steps
```bash
# Debug build
./gradlew :app:assembleDebug

# Release build (requires keystore.properties if signing locally)
./gradlew :app:assembleRelease
```

---

## Community, Issues & Feedback

- **Bug Reports**: Encountered a visual glitch or gesture conflict? Open a [Bug Report](https://github.com/monsterbag293-cloud/Antigravity-Android/issues/new?template=bug_report.yml) with your device model and steps to reproduce.
- **Feature Requests**: Have an idea for mobile UI improvements? Submit a [Feature Request](https://github.com/monsterbag293-cloud/Antigravity-Android/issues/new?template=feature_request.yml&labels=enhancement).
- **Discussions & Ideas**: Share mobile workflows and suggest ideas in [GitHub Discussions](https://github.com/monsterbag293-cloud/Antigravity-Android/discussions).

---

> [!IMPORTANT]
> ### Legal Disclaimer & Trademark Notice
> This project is an **independent, community-maintained compatibility layer** and is **not** created, endorsed, sponsored, or affiliated with Google LLC or Alphabet Inc.
>
> * **Google Antigravity**, **Gemini**, and related trademarks, logos, and service assets are the exclusive intellectual property of **Google LLC**.
> * This repository **does NOT claim any ownership or license** over Google's proprietary binaries, assets, or trademarks.
> * All rights to the underlying Antigravity software remain reserved by their respective copyright holders.
