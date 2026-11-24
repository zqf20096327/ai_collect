<div align="center">

<img src="docs/media/mascot.webp" width="96" alt="SuperPI" />

# SuperPI

**Personal AI Agent Ecosystem — Android · Desktop · Self-Hosted Relay · Plugin Platform**

<sub>Local-first assistant that works across your phone and computer, with optional self-hosted sync and extensible `.ddp` plugins.</sub>

English · [简体中文](README.cn.md)

<a href="https://github.com/Sadami3066/SuperPI/releases/latest"><img src="https://img.shields.io/github/v/release/Sadami3066/SuperPI?style=for-the-badge&logo=github&label=Download&color=111111" alt="Download latest Android APK" /></a>

<img src="https://img.shields.io/badge/Android-10%2B-3DDC84?style=flat-square&logo=android&logoColor=white" alt="Android 10+" />
<img src="https://img.shields.io/badge/Kotlin-2.4-7F52FF?style=flat-square&logo=kotlin&logoColor=white" alt="Kotlin" />
<img src="https://img.shields.io/badge/TypeScript-Node%2024%2B-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" />
<a href="https://github.com/Sadami3066/SuperPI/actions/workflows/ci-android.yml"><img src="https://github.com/Sadami3066/SuperPI/actions/workflows/ci-android.yml/badge.svg" alt="Android CI" /></a>
<a href="https://github.com/Sadami3066/SuperPI/actions/workflows/ci-ts.yml"><img src="https://github.com/Sadami3066/SuperPI/actions/workflows/ci-ts.yml/badge.svg" alt="TS CI" /></a>
<a href="https://github.com/Sadami3066/SuperPI/actions/workflows/ci-plugins.yml"><img src="https://github.com/Sadami3066/SuperPI/actions/workflows/ci-plugins.yml/badge.svg" alt="Plugins CI" /></a>
<img src="https://img.shields.io/badge/License-Apache--2.0-blue?style=flat-square" alt="Apache-2.0" />

</div>

[Architecture](#architecture) · [Packages & Repositories](#packages--repositories) · [Quick Start](#quick-start) · [Development](#development) · [Documentation](#documentation) · [Contributing](#contributing)

---

## Overview

**SuperPI** is a local-first personal AI agent ecosystem:

- **Android (`apps/android`)**: On-device personal agent built with Jetpack Compose. Long-press the power button to speak or type, run Linux commands in bundled Alpine/proot (or Root), automate Android UI via wireless ADB / virtual screen, host mini-apps, and load signed `.ddp` plugins.
- **Desktop (`apps/desktop`)**: Electron + React desktop shell driving the official [pi](https://pi.dev) agent over JSONL RPC, sharing bots, remote execution, and synced memory with your phones.
- **Relay (`apps/relay` + `packages/protocol`)**: Optional, self-hosted Node.js 24 HTTPS/WSS service for cross-device bot routing, encrypted CA-pinned pairing, workspace file transfer, and **Memory v2** synchronization.
- **Plugins (`plugins/`)**: 10 official integrations (`feishu`, `wecom`, `micloud`, `mail`, `amap`, `rail`, `hotel`, `ride`, `themes`, `mcpui-demo`), a third-party Gradle template, and an end-to-end sample fixture.

All conversations, API keys, and sessions stay on your devices by default and talk directly only to the model providers or self-hosted relay you configure.

## Architecture

```mermaid
flowchart LR
    subgraph Devices["Client Surfaces"]
        A["Android App\n(apps/android)"]
        D["Desktop Shell\n(apps/desktop)"]
        P["Signed .ddp Plugins\n(plugins/official)"]
        A <--> P
    end

    subgraph Sync["Self-Hosted Relay (Optional)"]
        R["SuperPI Relay\n(apps/relay)"]
        PR["@superpi/protocol\n(packages/protocol)"]
        DB[("SQLite WAL\nMemory v2 & Leases")]
        R --- PR
        R --- DB
    end

    subgraph Ext["Companion Repositories"]
        SDK["SuperPI-KotlinSDK\n(pi-ai / pi-agent / pi-mcp)"]
        MKT["SuperPI-Market\n(Signed Registry & Releases)"]
        MVN["SuperPI-Maven\n(plugin-api & SDK AAR/JAR)"]
    end

    A <-->|"WSS / HTTPS\nPinned CA"| R
    D <-->|"WSS / HTTPS\nPinned CA"| R
    A -.->|"Agent Harness"| SDK
    A -.->|"Plugins, Skills, MCP"| MKT
    P -.->|"compileOnly"| MVN
```

## Packages & Repositories

### Inside this Monorepo

| Path | Stack | Responsibility |
|---|---|---|
| [`apps/android/`](apps/android/) | Kotlin · Compose · Gradle | Android agent client, runtime, proot/ADB/Root shell, `:design` & `:plugin-api` SDKs |
| [`apps/desktop/`](apps/desktop/) | Electron · React · Vite | Desktop shell over `pi --mode rpc`, remote bot caller/callee, Memory v2 client |
| [`apps/relay/`](apps/relay/) | Node 24 · TypeScript · SQLite | Self-hosted device relay, pairing, presence, Memory v2 push/pull & Dream lease |
| [`packages/protocol/`](packages/protocol/) | TypeScript · JSON Vectors | Canonical WebSocket frames and Memory v2 contracts shared across TypeScript & Kotlin |
| [`plugins/official/`](plugins/official/) | Kotlin · `.ddp` | Official plugins (`feishu`, `wecom`, `micloud`, `mail`, `amap`, `rail`, `hotel`, `ride`, `themes`, `mcpui-demo`) |
| [`plugins/template/`](plugins/template/) | Kotlin · Gradle | Standalone starter project for third-party `.ddp` plugin authors |
| [`plugins/sample/`](plugins/sample/) | Kotlin · Gradle | Deterministic test fixture for host E2E and binary compatibility regression |

### Ecosystem Repositories

| Repository | Purpose | Link |
|---|---|---|
| **SuperPI-KotlinSDK** | Reusable KMP (`Android` + `JVM`) agent runtime SDK (`pi-ai`, `pi-agent`, `pi-mcp`, `pi-coding-agent`) | [Sadami3066/SuperPI-KotlinSDK](https://github.com/Sadami3066/SuperPI-KotlinSDK) |
| **SuperPI-Market** | ECDSA-signed plugin, skill & remote MCP catalog served via GitHub Pages | [Sadami3066/SuperPI-Market](https://github.com/Sadami3066/SuperPI-Market) |
| **SuperPI-Maven** | Static GitHub Pages Maven host for SDK, `plugin-api`, and `design` artifacts | [Sadami3066/SuperPI-Maven](https://github.com/Sadami3066/SuperPI-Maven) |

## Quick Start

### 1. Install on Android

1. Download the latest `PI-X.Y.Z.apk` from [GitHub Releases](https://github.com/Sadami3066/SuperPI/releases/latest) (requires Android 10+).
2. Follow onboarding to add a model provider (42 built-in providers or custom endpoint) and initialize the on-device Alpine Linux environment.
3. Optionally enable Wireless Debugging or Root in **Settings → System access** to allow screen automation.

See [Getting Started](docs/user/getting-started.md) for full usage instructions.

### 2. Self-Host the Relay (`apps/relay`)

Run with Docker (or Node.js ≥ 24):

```bash
# Container image published to GHCR on relay releases
docker run -d --name superpi-relay \
  -p 8443:8443 -v superpi-relay-data:/data \
  ghcr.io/sadami3066/superpi-relay:latest

# Or from source with automatic LAN self-signed TLS & QR pairing link
pnpm install
./apps/relay/scripts/dev-relay.sh
```

See [Self-Hosting Relay](docs/user/self-hosting-relay.md) for TLS certificates, systemd, and multi-device pairing.

### 3. Run Desktop (`apps/desktop`)

Requires Node.js ≥ 24, `pnpm`, and `pi` (`@earendil-works/pi-coding-agent`) on `PATH`:

```bash
pnpm install
pnpm build:desktop
pnpm dev:desktop
```

## Development

```bash
# TypeScript (Protocol + Relay + Desktop)
pnpm typecheck
pnpm test
pnpm build:desktop

# Android App & Plugin SDK ABI (JDK 17 + Android SDK 36)
./apps/android/scripts/dev-setup.sh
./apps/android/scripts/check.sh --full
./apps/android/scripts/build.sh stop

# Official & Sample Plugins
(cd plugins/official && ./scripts/check.sh)
(cd plugins/sample && ./gradlew verifyPlugin --no-daemon)

# Everything sequentially
./scripts/check-all.sh
```

To build `apps/android` against a sibling checkout of `../SuperPI-KotlinSDK`, pass `-Psuperpi.localSdk=true` or set `SUPERPI_LOCAL_SDK=1`.

For release tagging conventions (`vX.Y.Z`, `desktop-v*`, `relay-v*`, `plugin-api-v*`, `plugin-*-v*`), see [Release Engineering](docs/contributing/release.md).

## Documentation

- **Users**: [Documentation Index](docs/README.md) · [Getting Started](docs/user/getting-started.md) · [Self-Hosting Relay](docs/user/self-hosting-relay.md)
- **Plugin Authors**: [Plugin Overview](docs/plugins/README.md) · [Quick Start](docs/plugins/quickstart.md) · [Manifest & Packaging](docs/plugins/manifest-and-packaging.md) · [Runtime API](docs/plugins/runtime-api.md) · [UI Extensions](docs/plugins/ui-extensions.md) · [Market Policy](docs/plugins/market-policy.md)
- **Contributors**: [Architecture](docs/contributing/architecture.md) · [Developer Guide](docs/contributing/development.md) · [Release Engineering](docs/contributing/release.md) · [Changelog](CHANGELOG.md)

## Contributing & Security

Issues and PRs are welcome—read [CONTRIBUTING.md](CONTRIBUTING.md) first. Please report security vulnerabilities privately as described in [SECURITY.md](SECURITY.md).

## License

Code in this repository is licensed under [Apache-2.0](LICENSE). Third-party components, bundled Linux binaries, fonts, and brand assets are documented in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
