<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/assets/app-icon-dark.png">
    <img src="MagpieRemote/Resources/Assets.xcassets/AppIcon.appiconset/AppIcon-1024.png" alt="Magpie Remote" width="112" height="112">
  </picture>
</p>

<h1 align="center">Magpie Remote</h1>

<p align="center">
  <strong>English</strong> · <a href="README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <strong>A native Apple control center built for <a href="https://github.com/yetone/magpie">yetone/magpie</a></strong><br>
  1:1 with the official web console · iOS 26 / 27 Liquid Glass · pure SwiftUI · zero third-party dependencies
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Swift-6.4-F05138?style=flat-square&logo=swift&logoColor=white" alt="Swift 6.4" />
  <img src="https://img.shields.io/badge/iOS-26.0%2B-000000?style=flat-square&logo=apple&logoColor=white" alt="iOS 26.0+" />
  <img src="https://img.shields.io/badge/iPadOS-26.0%2B-157EFB?style=flat-square&logo=apple&logoColor=white" alt="iPadOS 26.0+" />
  <img src="https://img.shields.io/badge/Dependencies-0-success?style=flat-square" alt="Zero Dependencies" />
  <img src="https://img.shields.io/badge/License-MIT-blue?style=flat-square" alt="MIT License" />
  <img src="https://img.shields.io/github/actions/workflow/status/zxfccmm4/magpie-remote/release.yml?branch=main&style=flat-square&label=Build%20IPA" alt="Build Status" />
</p>

## ✨ Why Magpie Remote

[magpie](https://github.com/yetone/magpie) is a powerful, elegant open-source AI agent gateway and routing middleware. Magpie Remote brings its daily operations to iPhone and iPad: live routing decisions, agent default models, platform quota check-ins, and session transcripts, all from your pocket.

- **Native first** — 100% SwiftUI, no WebView shell; instant launch with native haptic feedback.
- **Modern design** — Apple HIG and iOS 26 / 27 Liquid Glass layered materials, with automatic light/dark and dynamic color adaptation.
- **Smooth and responsive** — `@Observable` unidirectional data flow with layered rendering; long lists stay stable at 120Hz ProMotion.
- **Secure and clean** — zero third-party dependencies; Web Keys and passwords live in the system Keychain, and networking uses native `URLSession`.

## 💎 Core Features

| Module | Highlights | Native implementation |
| :--- | :--- | :--- |
| **🤖 Agents** | Manage Claude Code, Codex, Gemini, and other agents; multiple configuration snapshots (Profiles); fine-grained model toggles and drag-to-reorder. | Native `NavigationSplitView` and customizable cards; changes apply instantly. |
| **🏢 Providers** | 70+ preset vendors; multi-account rotation pools and weights; connectivity diagnostics; Vertex AI and subscription-style interactive sign-in. | Async test-status capsules and connectivity progress indicators. |
| **🔀 Groups** | Strategy groups at a glance with online editing; affinity matching, multi-level fallback, rule classifiers, and template import/export. | Drag-to-reorder and native strategy micro-capsules. |
| **📊 Usage** | Real-time token statistics and request ledger; one-tap check-ins (WorkBuddy / Trae / Qoder / MiniMax, etc.); Tuned-for-you context suggestions. | Apple Charts vector trends and haptic feedback. |
| **💬 Sessions** | Transcripts of historical interactions; native Markdown highlighting and copy; cross-agent transcript carry; trash and restore. | Virtualized long lists with one-tap save to the server. |
| **⚡ Routing** | Historical routing trace-back; real-time routing decision stream over long polling. | Animated active cards showing how requests hit and flow across providers. |
| **🔑 Gateway** | Gateway credential management; sliding-window quotas (daily / weekly / monthly / hourly token or cost limits). | Native quota progress bars and live reset countdowns. |
| **🛡️ Masking** | Sensitive-entity redaction rule library; interactive preview sandbox and intercepted-request audit. | Live syntax diff and whitelist markers. |
| **📚 Library** | One-stop Skills and MCP server management; built-in Skills.sh and MCP Registry marketplaces; built-in memory store. | Card-based marketplace with one-tap installation and auto-discovery. |
| **🧩 Plugins** | Community plugin center, NPM mirror switching, and option configuration. | Native forms and multi-source search. |
| **⚙️ Settings** | Adaptive appearance, currency switching, LAN access, data backup, and OTLP telemetry configuration. | System-level grouped style that matches iOS Settings. |

## 🚀 Quick Start

### 1. Start the magpie server

Make sure [magpie](https://github.com/yetone/magpie) is deployed and running:

```bash
# Set a fixed Web Key and start the web service (LAN or public access)
export MAGPIE_WEB_KEY="your-custom-web-key"
magpie web --addr 0.0.0.0:3426 --lan --no-open
```

### 2. Install Magpie Remote

- **GitHub Releases (recommended)** — After a new version is published, GitHub Actions builds `MagpieRemote.ipa`. Download it from the [latest Release](../../releases/latest) and sideload it with **TrollStore**, **AltStore**, or **SideStore**.
- **Build locally** — Follow "Build from source" below to deploy to a device or simulator with Xcode.

### 3. Connect your instance

1. Open Magpie Remote.
2. Tap "Add Connection", then enter a name, server address (e.g. `http://192.168.1.100:3426` or your domain), and `MAGPIE_WEB_KEY`.
3. Tap "Connect"; the client performs a secure handshake and syncs the server state.

## 🛠️ Build from Source

The project is declaratively managed by [XcodeGen](https://github.com/yonaskolb/XcodeGen); `project.yml` is the single source of truth. Regenerate the project after adding or removing files.

| Environment | Requirements |
| :--- | :--- |
| macOS | Sequoia 15.6+ (Xcode 26.0–26.3) or Tahoe 26.2+ (Xcode 26.4+) |
| Xcode | 26.0+ (iOS 26 SDK; CI validates with 26.6, 27.x also works) |
| XcodeGen | `brew install xcodegen` |

```bash
# 1. Generate the Xcode project
xcodegen generate

# 2. Build for the simulator
xcodebuild -project MagpieRemote.xcodeproj \
  -scheme MagpieRemote \
  -destination 'generic/platform=iOS Simulator' \
  build \
  CODE_SIGNING_ALLOWED=NO \
  CODE_SIGNING_REQUIRED=NO \
  CODE_SIGN_IDENTITY=""

# 3. Run unit tests
xcodebuild -project MagpieRemote.xcodeproj \
  -scheme MagpieRemote \
  -destination 'platform=iOS Simulator,name=iPhone 17 Pro Max' \
  test \
  CODE_SIGNING_ALLOWED=NO \
  CODE_SIGNING_REQUIRED=NO \
  CODE_SIGN_IDENTITY=""
```

## 📦 Automated Builds and Releases

CI/CD is defined in [`.github/workflows/release.yml`](.github/workflows/release.yml):

- **Triggers** — every push to `main`, push a `v*` tag, publish a Release, or run the workflow manually.
- **Version** — main pushes automatically bump the patch version from the latest `v*` tag; tag pushes and manual runs can set an exact version.
- **Build** — On a `macos-26` runner, Xcode 26 creates an unsigned archive, exports `MagpieRemote.ipa`, and generates a SHA256 checksum.
- **Release** — every successful run creates or updates a GitHub Release with commit-based release notes plus `MagpieRemote.ipa` and its SHA256 checksum.

## 🤝 Contributing

Want to customize themes, add gateway analytics charts, or support more agent protocols? Read the [development guide](DEVELOPMENT.md) and the [AI agent collaboration guide](AGENTS.md).

## 📄 License

Released under the [MIT License](https://opensource.org/license/mit). Free for personal and commercial use, modification, and distribution.

With thanks to [yetone/magpie](https://github.com/yetone/magpie) for the excellent AI gateway foundation.
