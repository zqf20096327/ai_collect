<p align="center">
  <img src="docs/assets/banner.png" alt="Philium" width="100%">
</p>

<p align="center">
  <a href="https://github.com/fimgu/philium/stargazers"><img src="https://img.shields.io/github/stars/fimgu/philium?style=flat" alt="GitHub stars"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="License: MIT"></a>
  <img src="https://img.shields.io/badge/platform-macOS-lightgrey" alt="Platform: macOS">
  <a href="https://tauri.app"><img src="https://img.shields.io/badge/built%20with-Tauri%202-24C8DB" alt="Built with Tauri 2"></a>
  <a href="https://www.rust-lang.org"><img src="https://img.shields.io/badge/Rust-000000?logo=rust" alt="Rust"></a>
  <a href="https://github.com/fimgu/philium/commits/main"><img src="https://img.shields.io/github/last-commit/fimgu/philium" alt="Last commit"></a>
</p>

<p align="center"><b>A calm desktop workspace for running coding agents on your own machine.</b></p>

<p align="center">
  <a href="#quick-start">Quick start</a> ·
  <a href="#features">Features</a> ·
  <a href="#requirements">Requirements</a> ·
  <a href="#roadmap">Roadmap</a> ·
  <a href="CONTRIBUTING.md">Contributing</a>
</p>

Philium is a desktop workspace for running coding agents on your own machine. You add your repositories, connect a model provider, and start agents that work in those repos. Philium shows every message, tool call and model request, asks before tools run (unless you tell it not to), and keeps an eye on secrets leaving your machine.

<p align="center"><img src="docs/assets/screenshots/agents.png" alt="Philium agents view" width="100%"></p>

<p align="center"><img src="docs/assets/demo.gif" alt="Philium demo" width="100%"></p>

It is built with Tauri 2. The agent runtime is HAL, a separate project that Philium starts in the background and stops when you quit.

## Why Philium

- **You can see everything.** Every message, tool call and model request is visible, so nothing happens out of view.
- **You stay in control.** Tools ask before they run unless you choose otherwise.
- **Your machine, your data.** Agents run locally, memory search uses local models, and outgoing secrets are watched.
- **Many agents, one place.** Run several agents across several repositories and follow them from a single window.

## Features

<table>
  <tr>
    <td width="50%" valign="top">
      <img src="docs/assets/screenshots/home.png" alt="Home" width="100%"><br>
      <b>Home</b><br>
      Get set up checklist and an overview of what your agents are doing.
    </td>
    <td width="50%" valign="top">
      <img src="docs/assets/screenshots/board.png" alt="Board" width="100%"><br>
      <b>Board</b><br>
      Track agent work across repositories in one view.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <img src="docs/assets/screenshots/review.png" alt="Review" width="100%"><br>
      <b>Review</b><br>
      Read diffs and review or publish pull requests with the GitHub CLI.
    </td>
    <td width="50%" valign="top">
      <img src="docs/assets/screenshots/memory.png" alt="Memory" width="100%"><br>
      <b>Memory</b><br>
      Local memory with on-device search models.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <img src="docs/assets/screenshots/skills.png" alt="Skills" width="100%"><br>
      <b>Skills</b><br>
      Extra tools and MCP servers your agents can use.
    </td>
    <td width="50%" valign="top">
      <img src="docs/assets/screenshots/stats.png" alt="Stats" width="100%"><br>
      <b>Stats</b><br>
      Usage and model request statistics.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <img src="docs/assets/screenshots/terminals.png" alt="Terminals" width="100%"><br>
      <b>Terminals</b><br>
      Built-in terminals next to your agents.
    </td>
    <td width="50%" valign="top">
      <img src="docs/assets/screenshots/improve.png" alt="Improve" width="100%"><br>
      <b>Improve</b><br>
      Suggestions for improving how your agents work.
    </td>
  </tr>
</table>

## Compared with single-CLI agents

A general comparison with running one command-line agent in one terminal. It is not a claim about any specific product.

| | Single-CLI agent | Philium |
| --- | --- | --- |
| Agents at once | Usually one per terminal | Several, side by side |
| Repositories | One working directory | Many, added in Repos |
| Visibility of tool calls and model requests | Scrollback text | Structured timeline |
| Approval before tools run | Varies | Yes, by default |
| Secret leak watching | Varies | Built in |
| Local memory search | Varies | Built in, on-device models |
| Setup | One binary | Desktop app plus the HAL runtime |
| Works from a plain SSH session | Yes | No, needs a desktop |

## Install

Philium runs on Apple Silicon Macs (M1 or later) with macOS 12 or newer.

1. Download the latest `Philium_*_aarch64.dmg` from [Releases](https://github.com/fimgu/philium/releases/latest).
2. Open the DMG and drag Philium into Applications.
3. The app is not notarized yet, so macOS blocks the first launch. Run this once, then open Philium normally:

   ```sh
   xattr -dr com.apple.quarantine /Applications/Philium.app
   ```

   Or: try to open it, then go to System Settings, Privacy & Security, and choose Open Anyway.

To build from source instead, see Quick start below.

## Quick start

```sh
git clone https://github.com/fimgu/philium.git
git clone <your HAL checkout> hal   # must sit next to philium, or set HAL_DIR
cd philium
npm install
npm run sidecar
npx tauri dev
```

Details are in [Build](#build) below.

## Requirements

The HAL agent runtime is required. Philium does not build or run agents without it.


- Node.js and npm (a current LTS release)
- Rust and Cargo, installed with rustup
- The Tauri 2 system prerequisites for your platform (see the Tauri docs)
- A checkout of HAL, the agent runtime Philium bundles. Philium does not build without it.

Optional, for some features:

- The GitHub CLI (`gh`), for reviewing and publishing pull requests
- Docker or another container runtime, for sandboxes

## Build

Philium needs HAL next to it. By default the build script looks for a folder called `hal` beside your Philium checkout:

```
Developer/
  hal/
  philium/
```

If HAL lives somewhere else, set `HAL_DIR` to its path.

```sh
npm install
npm run sidecar          # builds HAL and stages it for Philium
npx tauri dev            # run in development mode
npx tauri build          # build an installer for your platform
```

`npm run sidecar` runs `scripts/sidecar.sh`. It builds HAL's desktop server from `HAL_DIR` (or `../hal`) and copies the binary into `src-tauri/binaries/`, named for your platform. Run it again whenever you update HAL.

Example with a custom location:

```sh
HAL_DIR=~/src/hal npm run sidecar
```

## First run

When Philium opens, the Home screen shows a **Get set up** card. Each row links to the screen where you finish that step and ticks itself off as you go. You can press **Later** to hide it, and **Check again** to refresh it.

Required:

1. **Sign in to a provider.** Open Providers and connect at least one model provider.
2. **Add a repository.** Open Repos and point Philium at a project you work on.
3. **Download local memory models.** Open Memory and start the download. These small models run on your machine so memory search works without sending your notes anywhere.
4. **Sign in to the GitHub CLI.** Install `gh` and run `gh auth login` in a terminal.

Optional:

- **Docker**, only needed for sandboxes.
- **Notifications**, to hear when an agent finishes or needs you.
- **Skills and MCP servers**, extra tools your agents can use.

Once the required rows are done, the card goes away on its own.

## Where data lives

- **App data**: Philium's own database, settings and stored secrets live in the standard app data folder for the id `app.philium`.
  - macOS: `~/Library/Application Support/app.philium`
  - Windows: `%APPDATA%\app.philium`
  - Linux: `~/.local/share/app.philium`
- **HAL configuration**: `~/.hal/hal.yaml`, or the file named by `HAL_CONFIG`.
- **Per repository**: an optional `.philium/` folder in the repo, for example `.philium/pipeline.yaml`. This belongs to the repo and is yours to commit or ignore.

Agents are not allowed to read Philium's own app data folder.

## Reset

To start fresh:

1. Quit Philium.
2. Delete the app data folder listed above for your platform.
3. Open Philium again. The Get set up card returns.

This removes Philium's settings, history, memory and stored secrets. It does not touch your repositories, any `.philium/` folders in them, or `~/.hal`. Remove those yourself if you want a completely clean slate.

## Roadmap

Philium is in active development and not yet published. See [docs/PUBLIC-RELEASE.md](docs/PUBLIC-RELEASE.md) for what remains before it goes public.

## Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md) before opening an issue or pull request.

## Star History

<a href="https://star-history.com/#fimgu/philium&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=fimgu/philium&type=Date&theme=dark">
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=fimgu/philium&type=Date">
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=fimgu/philium&type=Date">
  </picture>
</a>

## License

[MIT](LICENSE)
