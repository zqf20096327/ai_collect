# my-claw-app

The phone and the browser for [my-claw](https://github.com/nerasse/my-claw): one outbound
WebSocket, no public port.

<p>
  <a href="https://github.com/nerasse/my-claw-app/releases/latest"><img src="https://img.shields.io/github/v/release/nerasse/my-claw-app?style=flat-square" alt="Android release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-3f4d3a?style=flat-square" alt="License: MIT"></a>
  <img src="https://img.shields.io/badge/react--native-0.86-61dafb?style=flat-square" alt="React Native 0.86">
</p>

![A conversation on a phone](docs/assets/readme-app/chat.png)

## What it is

The client of a my-claw server. The agent, its tools, its sessions and its memory stay on the
machine you own; this repository is the screen you hold. The same code runs as an Android app and
as the web client the server serves, so a thread started on the phone is the same thread on the
laptop.

The connection goes out from the client to the server over a secure WebSocket. Nothing listens on a
public port, and there is no hosted account in the middle.

## What you get

- Streaming answers, with tool calls folded into steps and reasoning folded under them.
- Sub-agent cards where they were spawned, and their return where it lands.
- Approvals: a blacklisted tool asks, from the phone, and the run waits for the answer.
- The browser the agent works in, live next to the chat, with its windows and tabs. VNC is there
  for a client that wants the real thing.
- Voice notes recorded in the app, transcribed in the thread, and spoken answers when asked.
- Sessions, folders and workspaces in one drawer, with the workspace named on every row.
- Ten themes and a custom palette, with light, dark and AMOLED modes.
- Push through self-hosted ntfy (UnifiedPush). No Firebase.
- One device list, revocable from the server, shared with the web client.

## Screens

![The drawer: folders, workspaces, and the thread you were in](docs/assets/readme-app/drawer.png)

![A voice note and its transcript](docs/assets/readme-app/voice.png)

![The browser panel, in the web client](docs/assets/readme-app/browser.png)

## Install

Android: download the APK from [releases](https://github.com/nerasse/my-claw-app/releases/latest)
and open it. The server prints a pairing code, a link and a QR code at the end of its install; the
app scans the QR or takes the code.

Web: the server serves the client itself. Open the link the installer printed, in any browser on the
same network or through your tunnel.

Updates arrive with the server, every 15 minutes, or by installing a newer APK.

## Under the hood

- React Native 0.86, bare, TypeScript. The web build is the same screens.
- Kotlin for the Android side: foreground service holding the socket, accessibility service,
  notification listener, device bridge.
- One wire protocol, defined in `src/core/protocol.ts`, shared with the server.
- The outbox is mirrored to local storage, so a frame written while the socket is down is sent on
  the next connection instead of being lost.

```
src/
├── core/          protocol, connection, resume, stores
├── app/           the screens: chat, drawer, settings, browser, jobs, agents
└── components/    the cards: tools, sub-agents, approvals, markdown, media
android/           Kotlin services + the release build
```

## Build

```bash
npm install
npm run android      # device attached over USB or wireless adb
npm test
npm run lint
```

Web bundle:

```bash
bash scripts/build-web.sh   # dist-web.tar.gz, served by the server
```

Releases are cut locally: the version in `android/app/build.gradle` and `package.json`, then
`scripts/release.sh` signs the APK and publishes it beside the web bundle.

## Security

No inbound port. Every device pairs with a code and can be revoked from the server. A tool on the
blacklist does not run until the approval is answered in the app, and the answer is journalled.

## Documentation

The server repository carries the docs: install, configuration, providers, tags, sub-agents, remote
nodes. Start at [my-claw](https://github.com/nerasse/my-claw).

## License

MIT. Copyright Yassir EL KSSIMI. Use it, change it, sell it, ship it closed; the copyright notice
travels with the copy.

Contributors: Yassir EL KSSIMI ([nerasse](https://github.com/nerasse)), Hicham Berrada
([Nawroski](https://github.com/Nawroski)), Nabil El Abassi
([LastryCoding](https://github.com/LastryCoding)), Anthony Von Bieler
([Tony224x](https://github.com/Tony224x)).
