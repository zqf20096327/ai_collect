# Onvyra

<p align="center">
  <img src="docs/icon.png" width="120" alt="Onvyra">
</p>

<p align="center">
  <b>Android AI 客户端 · 多模型对话 · 本地工作区 · 手机操控 · 阅读与媒体</b><br>
  <sub>An Android AI client for multi-model chat, a local workspace, device control, reading and media.</sub>
</p>

<p align="center">
  <a href="https://github.com/gegewu26-source/Onvyra-Releases/releases/latest">下载最新版 · Latest release</a>
  ·
  <a href="CHANGELOG.md">更新日志 · Changelog</a>
  ·
  <a href="LICENSE">AGPL-3.0</a>
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="README_ZH_CN.md">简体中文</a> ·
  <a href="README_ZH_TW.md">繁體中文</a> ·
  <a href="README_JA.md">日本語</a>
</p>

---

## What it is

Onvyra is a native Android app for talking to the AI models you already use. Everything runs on the phone: conversations, files, the reader, the built-in web server. There is no Onvyra account, and no Onvyra backend holding your chats.

You bring a model service — your own API key, a self-hosted gateway, or a compatible proxy — and the app gives it a usable client: long conversations with context compression, file and document handling, a sandboxed workspace for the model to work in, a browser interface, and reading/media features on top.

## Highlights

| | |
|---|---|
| **Multi-model chat** | Add any number of providers, pick a model per conversation, switch assistants freely. Long threads compress context and keep history browsable. |
| **Tools and search** | Built-in web search and page reading, PDF extraction with paging, MCP servers, task-scoped skills, and a file workspace the model can read and write. |
| **On-device control** | Optional Android device control through wireless debugging or root, with per-tool approval. Off by default; nothing runs until you turn it on. |
| **Browser access** | A built-in web server serves a React interface, so the same app is usable from a desktop browser on your network. |
| **Reading and media** | Novel reader with importable book sources, video search and in-chat playback, image and video generation when the selected model supports it. |
| **Netdisk** | Optional cloud-drive integration and share-link resolution for services you configure. |

## Download

Get the APK from [Releases](https://github.com/gegewu26-source/Onvyra-Releases/releases/latest).

| File | Target |
| --- | --- |
| `Onvyra-<version>-arm64-v8a.apk` | Most Android phones and tablets (64-bit ARM) |
| `Onvyra-<version>-x86_64.apk` | x86_64 devices and emulators |
| `Onvyra-<version>-universal.apk` | Single package containing both ABIs |
| `Onvyra-<version>-source.zip` | Corresponding source for this build |

Requirements: **Android 8.0 (API 26)** or later. Install the APK for your device architecture; the universal package works everywhere but is larger.

Upgrades install over the previous version when the signing certificate matches. Source and build notes for each release are attached to the same release page.

## Build from source

Prerequisites: JDK 24, Android SDK Platform 37.2, NDK 29.0.14206865, CMake 3.22.1, Node.js 24 and pnpm 12.

Point the SDK via `ANDROID_HOME` or a local `local.properties`, then from the repository root:

```bash
pnpm --dir web-ui install --frozen-lockfile
./gradlew :app:assembleDebug          # Linux / macOS
.\gradlew.bat :app:assembleDebug      # Windows
```

Debug APKs land in `app/build/outputs/apk/debug/`. A debug build uses the local debug key and needs no private Firebase configuration. For a signed release, see [local build configuration](docs/local-configuration.md).

## Project layout

```
app/                     main application: UI, view models, core logic
ai/                      provider abstraction (OpenAI-compatible, Google, Anthropic, …)
common/                  shared utilities
document/                PDF, DOCX, PPTX, EPUB parsing
highlight/               syntax highlighting
material3/               Material color utilities
mediagen/                image and video generation
netdisk-download-engine/ cloud-drive download engine
oauth/                   OAuth helpers
search/                  search providers
speech/                  TTS and ASR
ui/                      reusable Compose components
web/                     embedded Ktor server + static frontend
web-ui/                  React frontend source
workspace/               sandboxed file and shell workspace
android-control/         device control kernel
```

## Public and personal builds

The public build ships without preconfigured addresses for the four optional video-site adapters. A personal build can load site addresses from a local JSON file via `ONVYRA_PRIVATE_VIDEO_ENDPOINTS`. Verification, donation, community and update features are present in both.

Release signing reads an external properties file referenced by `ONVYRA_SIGNING_PROPERTIES`; key material is never part of this repository.

## Updating

Each release carries a signed update manifest. The app checks it, verifies the signature against a public key shipped in the binary, and offers the matching APK for your ABI. Checksums are published with every asset.

The full release procedure — version bump, signing, source archive, signed manifest and upload — is documented in [docs/RELEASING.md](docs/RELEASING.md).

## License and attribution

Onvyra is based on [RikkaHub](https://github.com/rikkahub/rikkahub) and is distributed under the [GNU Affero General Public License v3.0](LICENSE). If you redistribute a modified version, provide its corresponding source under the same terms. Section 13 applies if your version supports remote interaction over a network: users interacting with it must be offered the corresponding source.

Third-party components keep their own licenses. See the [application notice](app/src/main/assets/licenses/NOTICE.txt), [Android control notice](android-control/NOTICE.md), [netdisk notices](THIRD_PARTY_NETDISK_NOTICES.txt) and [video extractor notice](app/src/main/assets/video_extractor/NOTICE.txt).

---

<p align="center"><sub>Maintained by <a href="https://github.com/gegewu26-source">gegewu26-source</a></sub></p>