# Codex Pet & Usage Companion

<p align="center">
  <strong>Switch Codex pets and monitor usage limits from one lightweight Windows tray panel.</strong><br />
  <sub>Local-first · Privacy-conscious · English, 简体中文, and 日本語</sub>
</p>

<p align="center">
  <a href="https://github.com/Nemo0000/codex-pet-usage-companion/releases"><img alt="Latest release" src="https://img.shields.io/github/v/release/Nemo0000/codex-pet-usage-companion?display_name=tag&sort=semver"></a>
  <a href="https://github.com/Nemo0000/codex-pet-usage-companion/releases"><img alt="Total downloads" src="https://img.shields.io/github/downloads/Nemo0000/codex-pet-usage-companion/total"></a>
  <a href="https://github.com/Nemo0000/codex-pet-usage-companion/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/Nemo0000/codex-pet-usage-companion"></a>
  <a href="https://github.com/Nemo0000/codex-pet-usage-companion/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/Nemo0000/codex-pet-usage-companion/actions/workflows/ci.yml/badge.svg"></a>
  <a href="https://opensource.org/licenses/MIT"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
</p>

<p align="center">
  <a href="https://github.com/Nemo0000/codex-pet-usage-companion/releases"><strong>Download latest Windows installer</strong></a>
  · <a href="README.zh-CN.md">简体中文</a>
  · <a href="docs/GETTING-STARTED.md">Getting started</a>
</p>

Codex Pet & Usage Companion is an independent, local-first Windows tray app for switching community Codex pets and viewing ChatGPT-backed usage limits from one compact panel.

> This is an independent open-source project. It is not an official OpenAI product.

## Core capabilities

- **Usage at a glance.** See remaining Codex rate-limit windows, reset countdowns, read-only reset credits, low-usage alerts, and a private 24-hour or 7-day local trend. If a refresh fails, the last known reading remains visible and is clearly marked as stale.
- **Community pet library.** Discover Petdex pets from the app, then search, filter, inspect attribution, install, repair, uninstall, or switch pets. The library keeps separate **All**, **Installed**, and **Favorites** views, and can safely import compatible local ZIP or folder packages.
- **Pet Workshop.** Review every animation row and frame of an installed pet, surface transparent or edge-clipped frame warnings, edit creator and license metadata, and export a shareable package. Creator-friendly v1 and v2 templates make it practical to draw a custom pet in an art tool and bring it back into the library.
- **Your data stays portable.** Create a versioned settings backup with a restore preview; export local usage trends as CSV or JSON; and create a privacy-safe diagnostic report. These files remain local unless you choose to share them.
- **Local, multilingual, and maintained.** The interface supports English, 简体中文, and 日本語. Signed in-app updates show their release notes and require confirmation before installation; authentication and usage data stay within the official local Codex App Server flow.

## Why this exists

Codex users often need two separate workflows: check subscription rate limits and open the official Pets settings to change a companion. This project brings those two tasks into one small tray panel while keeping authentication and usage data inside the official local Codex App Server flow.

## Screenshots

### Usage dashboard

<p align="center">
  <img src="docs/screenshots/usage-home-en.png" alt="Codex usage dashboard with reset credits and a local history trend" width="360">
</p>

### Community library and Pet Workshop

<p align="center">
  <img src="docs/screenshots/pet-library-workshop-v010.png" alt="Updated community pet library with favorites and Pet Workshop animation editing" width="720">
</p>

## How it works

The app launches `codex app-server` locally and communicates over its stable `stdio` transport. It does not scrape ChatGPT pages, read browser cookies, or upload usage data. Email addresses are masked in the UI, and raw protocol messages and access tokens are never logged.

### Usage insights and local history

The dashboard treats reset-credit information as strictly read-only. A missing App Server field remains **unsupported/unknown** and is never converted into a false zero. No redeem or account-changing action is exposed.

When local history is enabled, successful refreshes are sampled at most once every five minutes. Only the sample time, limit identifier, window duration, remaining percentage, and reset time are stored. History is capped, expires after seven days, never leaves the device, and can be disabled or cleared under **Settings > Data & privacy**.

### Petdex community gallery

The app includes an in-app client for the public [Petdex](https://petdex.dev/) manifest. It does not run a second floating mascot: it downloads the selected community package, validates its trusted asset URLs, metadata, size, image format, and v1/v2 sprite grid, then installs it under `.codex/pets/<pet-id>` for the official Codex app.

**Install only** adds the package without changing the active pet. **Install and use** refreshes the official Pets page, launches the desktop app when a trusted local executable is available, opens Settings > Pets through visible Windows UI Automation, invokes the visible **Select** button, and checks for the **Selected** state. If navigation or UI automation is unavailable, the package remains safely installed and the app asks the user to select it manually.

Pet assets remain owned by their Petdex submitters. The gallery links to each source page so users can review attribution and licensing before redistributing an asset.

### Favorites and Pet Workshop

Favorites are stored locally and give the library a quick shortlist without sending preference data to Petdex. The **Pet Workshop** works with installed or imported packages: inspect animation coverage frame by frame, review visual warnings, update metadata, export a safe ZIP, or generate an empty v1/v2 creator template for a new hand-drawn pet.

### Local pet packages

The **Installed** view can import either a ZIP or a folder containing `pet.json` and the referenced PNG/WebP spritesheet. Imports are limited by archive size, entry count, expanded size, path depth, metadata length, image format, and the Codex v1/v2 sprite grid. ZIP paths, symlinks, duplicate entries, unsafe source links, and ID conflicts are rejected before the existing package is changed.

Standard Codex fields are required: `id`, `displayName`, `spritesheetPath`, and optional `spriteVersionNumber` (`1` or `2`). Package creators may also declare `description`, `author` or `submittedBy`, `license`, `sourceUrl` (HTTPS), `packageVersion`, `kind`, and `tags`. These optional fields appear in the in-app details view and help users make informed attribution and redistribution decisions.

The app records a small sidecar only for packages it installs or imports. It contains the package origin, optional public attribution, source location, install time, and spritesheet checksum. It contains no account, authentication, or usage data. A repair is offered only while that recorded source remains available.

## Download

Download the latest Windows x64 installer from [GitHub Releases](https://github.com/Nemo0000/codex-pet-usage-companion/releases).

The installer does not yet carry a commercial Windows Authenticode certificate, so Windows may display a warning on first install. In-app updates are separately signed and verified against the public key embedded in the app before installation.

## Documentation

- [Getting started (English)](docs/GETTING-STARTED.md)
- [使用教程（简体中文）](docs/GETTING-STARTED.zh-CN.md)
- [中文项目说明](README.zh-CN.md)
- [Release and updater guide](docs/RELEASING.md)
- [Codex community post draft](docs/CODEX-COMMUNITY-POST.md)

## Requirements

- Windows 10 or Windows 11 (x64)
- Microsoft Edge WebView2 Runtime
- Codex CLI with `codex app-server` support
- A ChatGPT-backed Codex sign-in for subscription rate-limit information
- Internet access to `petdex.dev` and `assets.petdex.dev` when browsing or installing community pets
- No internet connection is required to browse, use, or re-import already available local packages

Check the CLI from PowerShell before launching the app:

```powershell
codex --version
codex app-server --help
```

## Installation and first run

1. Download the latest `Codex Pet & Usage Companion_*_x64-setup.exe` installer from the release page.
2. Run the installer for the current Windows user.
3. Launch Codex Pet & Usage Companion from the Start menu or desktop shortcut.
4. If Codex is not signed in, choose **Reconnect** and complete the official browser flow.
5. Use the tray icon to show or hide the panel. Closing the panel hides it instead of exiting the app.

Starting with v0.8.1, the app checks GitHub Releases shortly after launch and every six hours. Use **Settings > App updates** or **Check for updates** in the tray menu for a manual check. The app shows release notes and asks for confirmation before downloading and installing a signature-verified update. Users on v0.8.0 or earlier need to install v0.8.1 manually once.

For **Install and use**, keep the official desktop app installed. The companion first tries standard Windows locations, then the optional path in Settings. You can still open Settings > Pets manually if the official UI does not expose the expected controls.

## Development

Development prerequisites:

- Node.js `20.19+`, `22.12+`, or a newer supported release
- Rust `1.96.0` (selected automatically by `rust-toolchain.toml`)
- Visual Studio 2022 Build Tools with the **Desktop development with C++** workload and a Windows SDK

Install dependencies and run the checks:

```powershell
npm install
npm run check
npm test
npm run build
```

Start the Tauri development app:

```powershell
npm run tauri dev
```

Build the Windows installer:

```powershell
npm run tauri build
```

The NSIS installer is written under `src-tauri/target/release/bundle/nsis/`.

## Troubleshooting

### Codex CLI not found

Confirm that `codex --version` works in a new terminal, then restart the companion. Set `CODEX_CLI_PATH` to an explicit executable or command-shim path when the CLI is not on `PATH`.

### Usage information is unavailable

Subscription rate-limit information requires a ChatGPT-backed Codex account. API-key-only and Bedrock authentication may not expose these usage windows. Use **Reconnect** and complete the official browser flow.

### Low-usage notifications

The in-panel warning works independently of Windows notification permission. The first system notification may require permission from Windows, and notification behavior is most complete after installing the bundled app rather than running an unpackaged development build.

### Local history or reset notifications

Open **Settings > Data & privacy** to disable local history, switch between the 24-hour and 7-day chart, clear every saved sample, or turn reset-completion notifications off. Clearing history does not affect account usage or reset credits.

### The panel disappeared

The close button hides the panel. Use the tray icon to show it again, or right-click the tray icon and choose **Show panel**.

### Automatic pet switching did not finish

The bridge uses only visible Windows UI Automation. Confirm the official desktop app is installed, optionally set its `.exe` path under **Settings > Official desktop app**, and retry **Install and use**. If navigation is unavailable after an official UI update, select the newly installed pet manually on Settings > Pets; the package remains safely installed.

## Current scope

Version `0.10.0` adds versioned settings backup and previewed restore, CSV/JSON usage-trend export, and privacy-safe diagnostics. It also adds Japanese language selection and end-to-end Japanese localization for the Petdex gallery and Pet Workshop. The release is published with a signed updater manifest and has passed native Windows export/restore verification. Pet packages are written only under `.codex/pets`; official client installation files are not modified.

## Roadmap

- Add more interface languages and localized community documentation.
- Validate Windows 10/11 upgrade paths and pursue Authenticode signing for wider distribution.
- Evaluate additional usage windows and account actions only when the official Codex App Server exposes stable support.

See [CHANGELOG.md](./CHANGELOG.md) for release history.

## License

Codex Pet & Usage Companion is released under the [MIT License](./LICENSE).
