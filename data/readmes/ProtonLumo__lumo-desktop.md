<p align="center">
  <img src="src-tauri/icons/app-icon.png" alt="Lumo" width="128" height="128">
</p>

<h1 align="center">Lumo Desktop</h1>

<p align="center">
  The desktop app for <a href="https://lumo.proton.me">Lumo</a>, Proton's privacy-first AI assistant.<br>
  macOS · Windows · Linux
</p>

---

Lumo Desktop wraps the Lumo web app in a native [Tauri](https://tauri.app) shell and gives it access to your
computer and your tools, with your approval:

- **Connectors**: let Lumo read and edit local files, run shell commands, and use Proton Mail, Luminance, and
  any [MCP](https://modelcontextprotocol.io) server, with a catalog of presets such as GitHub, Linear, Figma,
  Grafana, Stripe and PubMed.
- **Approvals**: every tool is set to auto-approve, ask, or disabled. Tools set to ask wait for your answer
  before they run.
- **Quick ask**: a global shortcut opens a search window from anywhere.
- **Scheduled prompts**: run prompts on a schedule.
- **Secure storage**: OAuth tokens, API keys and MCP credentials live in the OS keychain.
- **Browser sign-in**: you sign in with your own browser, so security keys and passkeys work.
- **Automatic updates**: signed updates on every platform.

## Supported platforms

| Platform | Package |
|---|---|
| macOS | Universal (Apple silicon and Intel) `.dmg` |
| Windows | `.msi` and `-setup.exe` installer |
| Linux | `.deb` and `.rpm`, for Ubuntu 24.04+ and Fedora 40+ |

## Architecture

```
        ┌──────────────────────────────┐
        │        Lumo web app          │   loaded remotely from LUMO_URL
        └──────────────────────────────┘
                       ↕  window.LumoConnectors
        ┌──────────────────────────────┐
        │  webview/bridges/connectors  │   TypeScript → src-tauri/dist/
        └──────────────────────────────┘
                       ↕  Tauri IPC: commands + events
        ┌──────────────────────────────┐
        │        src-tauri/src         │   Rust core
        └──────────────────────────────┘
```

- **Lumo web app**: lives in Proton's web clients monorepo and is loaded remotely. Its `desktop-tools.ts`
  consumes the bridge.
- **webview/**: TypeScript bundled by `scripts/build-webview.mjs` into `src-tauri/dist/scripts/`. There are two
  kinds: scripts injected into the remote page (`webview/bridges/`), and scripts for the local pages that
  aren't the web app (`webview/pages/`: `login`, `search`, `settings`). The pages' HTML, CSS and images live in
  `webview/static/` and are copied into `dist/` unchanged.
- **Rust core**: tool registry, connectors, keychain, approval gate, account scoping, updater.
- **IPC boundary**: commands are allowlisted in `src-tauri/permissions/*.toml` and granted in
  `src-tauri/capabilities/default.json`. Rust pushes state back as events (connector auth, tool-approval
  requests). Adding a command takes three edits: the handler, the permission, and the capability.
- **The bridge contract spans two repos**: `webview/bridges/connectors.ts` and the web app's `desktop-tools.ts`
  must agree. The E2E suite builds its stub from a live checkout of the web clients on every run to catch drift.

### Project layout

```
webview/
├── bridges/                 scripts injected into the remote Lumo page, one bundle each
├── pages/                   scripts for the local pages (login, search, settings, theme)
├── shared/                  Tauri invoke, logger and connector catalog, imported by both
├── types/                   contracts with the web app, and window globals
└── static/                  pages, styles/ and images/ (incl. connector logos), copied to dist/
scripts/                     build-webview.mjs, version and updater-archive scripts
e2e/                         containerised WebDriver suite
src-tauri/
├── src/
│   ├── app.rs               Tauri builder: plugins, IPC handler, startup
│   ├── main_window.rs       main window, its webviews and close-to-tray
│   ├── webview.rs           navigation policy and sign-in page
│   ├── browser_login.rs     session-fork sign-in
│   ├── tray.rs              app menu and tray icon
│   ├── quick_ask/           global-shortcut search window and its handoff
│   ├── settings/            device and per-account settings, settings overlay
│   ├── dialog/              native branded and loading dialogs
│   ├── tools/               registry, connectors, keychain, approvals
│   ├── schedules/           scheduled prompts
│   ├── updater.rs
│   └── lib.rs               LUMO_URL, module tree
├── capabilities/            IPC grants
├── permissions/             command allowlists
├── dist/                    webview build output, gitignored
└── tauri.conf.json
```

### Sign-in

WKWebView does not dispatch WebAuthn, so security keys and passkeys cannot work inside the webview. Sign-in
therefore happens in the user's own browser: the app starts on a bundled `login.html`, sends the user to
Proton Account, and receives the session back through Proton's session-fork protocol, which the webview
redeems before loading the web app. See `src-tauri/src/browser_login.rs`.

### Connectors

Connectors are registered at startup into a `ToolRegistry` and exposed to the web app as OpenAI-format tools
named `{connector_id}__{tool_name}`.

| Connector | Notes |
|---|---|
| `filesystem` | Search, read, write and edit within user-granted roots |
| `bash` | Shell execution |
| `browser` | Fetch and read web pages |
| `proton_mail` | Proton Mail through [Proton Mail Bridge](https://proton.me/mail/bridge) |
| `luminance` | Luminance Public API v2, called directly (Luminance has no MCP server) |
| `mcp-{id}` | Any MCP server. The catalog in `webview/shared/connector-catalog.ts` pre-configures many remote servers; some are experimental and hidden behind a feature flag |
| `mcp-zendesk` | Community [`@fruggr/zendesk-mcp-server`](https://github.com/fruggr/zendesk-mcp-server) (stdio via `npx`; OAuth on first tool use) |
| `mcp-figma` | [Figma desktop MCP](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/) at `http://127.0.0.1:3845/mcp` (enable it in Figma desktop Dev Mode; remote OAuth is limited to [Figma's MCP catalog](https://www.figma.com/mcp-catalog/)) |
| `echo` | E2E fixture, registered only under `LUMO_E2E_TESTING` |

Each tool also carries an approval policy (auto-approve, ask, or disable). An `ask` tool suspends execution,
emits a request to the webview, and resolves on the user's answer or a timeout.

## Developing

### Prerequisites

| Tool | Version |
|---|---|
| [Node.js](https://nodejs.org/) | 22 |
| [Rust](https://rustup.rs/) | stable (2021 edition) |

You also need the [Tauri prerequisites](https://tauri.app/start/prerequisites/) for your platform (WebKitGTK
on Linux, WebView2 on Windows).

Optionally, enable the pre-push type-check hook:

```bash
git config core.hooksPath .githooks
```

### Running

```bash
npm install
npm run dev
```

By default the app loads the web app from `https://lumo.proton.dev`, which is a local checkout of Proton's web
clients. To develop against production instead, set `LUMO_URL`:

```bash
LUMO_URL=https://lumo.proton.me npm run dev
```

Sign-in is required to use the app. Proton developers can use dev accounts on the internal test environments.

### Dev loop

- Rust changes hot-restart the app.
- TypeScript changes do not: there is no frontend dev server, and esbuild runs once at startup. After editing a
  `.ts` file, rebuild the bundles with `npm run build:webview` and reload the window.
- Changes to injected scripts (`webview/bridges/`) need a restart of `npm run dev`.

## Testing

```bash
npm run typecheck                                                       # TypeScript
cargo test --manifest-path src-tauri/Cargo.toml --features test-utils   # Rust unit and integration tests
```

### End-to-end tests

The E2E suite needs a checkout of Proton's web clients as a sibling of this project, or at `CLIENTS_DIR`:

```bash
./e2e/run.sh
```

It runs in a Linux container because WebKitGTK ships a WebDriver. See [`e2e/README.md`](e2e/README.md).

## Building

On macOS, build an ad-hoc signed app with:

```bash
APPLE_SIGNING_IDENTITY="-" npm run build
```

On Linux and Windows, `npm run build` is enough.

Bundles land in `src-tauri/target/<target>/release/bundle/`. The executable is named `lumo-desktop`
(`lumo-desktop.exe` on Windows); the app's displayed name is `Lumo`.

## Config and data storage

| Platform | Config directory |
|---|---|
| macOS | `~/Library/Application Support/me.proton.lumo-app/` |
| Windows | `%APPDATA%\me.proton.lumo-app\` |
| Linux | `~/.config/me.proton.lumo-app/` |

```
settings.json                            shortcut, launch at startup, settings hotkey
accounts/<UserID>/settings.json          filesystem roots, write flag, shell flag
accounts/<UserID>/mcp_servers.json       MCP server definitions
accounts/<UserID>/connector_state.json   enable flags, per-tool approval policies
accounts/<UserID>/mcp_tools/             cached tool lists per MCP server id
```

Secrets (OAuth tokens, API keys, MCP server credentials) are stored in the OS keychain under the service
`me.proton.lumo-app`.

### Resetting MCP setup

To wipe **all** MCP setup for one Lumo account, quit Lumo first, then:

1. In **Settings → Connectors**, use **Reset** on each catalog MCP server (or **Remove** on custom ones).
2. Delete or empty `accounts/<UserID>/mcp_servers.json`.
3. Optionally, delete `accounts/<UserID>/mcp_tools/` and trim `connector_state.json` for a clean slate.
4. In your keychain (Keychain Access on macOS), search for `me.proton.lumo-app` and delete entries whose
   account starts with `connector:<UserID>:mcp-`.

The community Zendesk MCP server also stores its **own** OAuth token on disk, outside Lumo's keychain. After
removing the connector, clear those files if you need a full re-login; see
[fruggr/zendesk-mcp-server `OAUTH_TOKEN_FILE`](https://github.com/fruggr/zendesk-mcp-server/blob/main/docs/configuration.md#oauth_token_file).

### Uninstalling

To remove a local install and its data:

```bash
./src-tauri/scripts/uninstall.sh          # --dry-run to preview, --yes to skip the prompt
```

## Releasing

Release builds, signing and publishing run in Proton's internal CI; see `RELEASING.md` in the internal
repository.

## License

Lumo Desktop is licensed under the [GNU General Public License v3.0](LICENSE).
