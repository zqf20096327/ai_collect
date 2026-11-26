# Hermes Browser

Let a Hermes agent (or any MCP client) control **your real Chrome**: your tabs, your sign-ins. It works the same way Claude in Chrome does. The agent works in its own background tab while you keep browsing, and a cursor and highlights show what it's doing.

> Unofficial community project, not affiliated with or endorsed by the makers of Hermes. The extension isn't in the Chrome Web Store: you sideload it (see [Quick start](#quick-start)).

```
Hermes ──MCP (stdio)──▶ bridge/server.mjs ──WebSocket 127.0.0.1:8765 (token)──▶ Chrome extension ──CDP──▶ tabs
```

- **`bridge/`**: a Node MCP server. Hermes launches it. It listens on localhost for the extension.
- **`extension/`**: a Manifest V3 Chrome extension. It connects to the bridge and runs actions through `chrome.debugger` (real, trusted mouse and keyboard events) and `chrome.scripting` (page outlines, refs, form filling).

## Tools

| Tool | What it does |
|---|---|
| `tabs_list`, `tabs_create`, `tabs_select`, `tabs_close` | Manage tabs. Tabs the agent opens go into a purple **Hermes** tab group. |
| `navigate` | Go to a URL, or `back` / `forward`, and wait for the load. |
| `read_page` | Outline of the page with `ref_N` handles (`filter: "interactive"` for controls only). |
| `find` | Search elements by role/name/text. Interactive matches come first. |
| `get_page_text` | Visible text of the page (main/article first). |
| `screenshot` | JPEG of the viewport, also saved to `~/.hermes-browser/screenshots/`. |
| `click`, `hover` | By `ref` (preferred) or by `x`/`y` in the last screenshot's pixels. |
| `type` | Types like a person: a real key press for each character (`keydown`/`keypress`/`input`/`keyup`, Shift for capitals and symbols, Enter for newlines). Optional `delay_ms` between keys; `mode: "paste"` inserts the whole text at once. |
| `key` | Press keys or combos, such as `Enter`, `Tab Tab`, `ctrl+a Backspace`. |
| `scroll` | Mouse-wheel scroll. |
| `form_input` | Set inputs, textareas, selects and checkboxes directly by ref (works with React). |
| `javascript` | Evaluate JS in the page and return the last value (top-level `await` works). |
| `handle_dialog` | Answer a native `alert` / `confirm` / `prompt` / "Leave site?" dialog (`accept`, `prompt_text`). Any tool whose action opens one, or that runs while one is open, reports the dialog instead of hanging. |

**Iframes:** `read_page` and `find` include visible iframes, including cross-origin ones such as cookie or consent banners. Their elements get refs like `f12:ref_3`, which work with `click`, `hover` and `form_input`. Clicks stay trusted: the iframe's position on screen is worked out automatically. `type` and `key` go to the iframe you last clicked.

**Works beside you:** the agent works in its own tab in the background, so you can keep using other tabs while it runs. Clicks, typing, dialogs and screenshots all work on a tab that isn't in front. `tabs_create` opens new tabs in the background, unless you're already watching the agent's tab. Neither `tabs_create` nor `tabs_select` brings a tab to the front unless the agent passes `focus: true`; the bridge tells it to do so only when you ask.

**See what it's doing:** on the agent's tab, a soft glowing border and a cursor that glides to each target show where it is pointing. A ripple marks each click, and the element it is reading or typing into is highlighted. A small pill reads "Hermes is using this tab" and has a **Stop** button (it moves out of the way of whatever the agent is working on). The overlay is hidden from screenshots and from `read_page` / `get_page_text`, so the agent never sees it. Turn it off with "Show Hermes' cursor and highlights" in the popup.

**Stop / Resume:** Stop (on the page pill or in the popup) pauses every agent immediately, even mid-typing. Tools return an error telling the agent you paused it and to wait for you, until you press Resume, and the toolbar badge shows **STOP**.

**Tab safety:** every connected agent (for example a local Hermes and a cloud one) has its **own** current tab, so they never act on each other's tabs. An agent never takes over the tab you're on: it starts with `tabs_create`, or `tabs_list` + `tabs_select` when you ask it to work on an existing tab. Once it is working in a tab, it never silently switches. If that tab is closed, tools return an error until the agent picks a tab with `tabs_select`, `tabs_create` or an explicit `tabId`.

## Quick start

You need [Git](https://git-scm.com), [Node.js 18+](https://nodejs.org) and Chrome (Edge, Brave and Chromium also work).

**1. Get the code and run setup**

```powershell
git clone https://github.com/MarsHeer/hermes-browser.git
cd hermes-browser/bridge
npm install
npm run setup
```

(No Git? Click **Code → Download ZIP** on GitHub, unzip it, and run the last three lines inside the `bridge` folder. On Windows, if PowerShell says "running scripts is disabled", type `npm.cmd` instead of `npm`.)

**2. Sideload the extension**

1. Open `chrome://extensions` (or `edge://extensions`, `brave://extensions`).
2. Turn on **Developer mode** (top right).
3. Click **Load unpacked** and pick the folder setup printed: `~/.hermes-browser/extension` (on Windows, `C:\Users\<you>\.hermes-browser\extension`). Tip: paste the path into the folder picker's address bar.
4. Pin the extension. The badge shows **ON** whenever a bridge is running. There's nothing to paste: it pairs itself.

Chrome may show a "Disable developer mode extensions" bubble at startup. Click away from it (don't click Disable). The extension keeps working.

**3. Check it**

Setup prints the exact command for your machine, for example `node "C:\Users\<you>\.hermes-browser\app\hermes-browser.mjs" doctor`. It checks Node, the token, the bridge and whether the extension is connected.

**Updating:** `git pull`, then `npm run setup` again in `bridge/`. Then click the reload icon on the extension in `chrome://extensions`.

### What setup does

Setup asks whether you run Hermes **locally**, in the **cloud**, or **both**, then:

- installs the bridge into `~/.hermes-browser` as one self-contained file, so you can move or delete the clone afterwards
- leaves nothing to copy or paste: the extension **pairs itself** by asking whichever bridge is running for its token
- **local Hermes:** adds the `chrome` MCP server to Hermes (`hermes mcp add`) and restarts the gateway if it's running
- **cloud Hermes:** finds or installs ngrok, connects your ngrok account, saves your static domain, copies the MCP token to your clipboard, prints the URL and header for the Hermes dashboard, and on Windows adds a **Hermes Browser Tunnel** Start-menu shortcut

### Commands

After setup, `hb` below stands for `node ~/.hermes-browser/app/hermes-browser.mjs` (setup prints the full path). From the clone's `bridge/` folder, `npm run setup`, `npm run doctor` and `npm run tunnel` do the same things.

| Command | |
|---|---|
| `hb setup` | Install or repair. `--local`, `--cloud` or `--both` skips the question; `--domain <name>` sets the ngrok domain; `--yes` accepts defaults. Pass flags through npm with `--`, as in `npm run setup -- --cloud`. |
| `hb doctor` | Checks everything, including whether the extension is connected. |
| `hb tunnel` | Starts the bridge plus the ngrok tunnel for cloud Hermes. Keep it open. On Windows, the **Hermes Browser Tunnel** Start-menu shortcut does the same. |
| `hb uninstall` | Undoes setup. `--purge` also deletes `~/.hermes-browser`. Then remove the extension in `chrome://extensions`. |
| `hb token` / `hb mcp-token` | Prints the extension token (manual pairing) or the cloud bearer token. |

**Local and cloud at the same time:** each Hermes runs its own bridge, and they share the browser. The first bridge to start owns the extension connection, and later ones forward their calls through it. If the first one stops, another takes over within a few seconds.

## Development and manual setup

Use this section if you're hacking on the code, or wiring Hermes up by hand instead of with `npm run setup`.

### 1. Run the bridge from the checkout

```powershell
cd bridge
npm install
npm test          # smoke test: MCP + WebSocket + auth gates
node cli.mjs serve   # the bridge straight from source (what Hermes launches)
```

Other tests: `npm run test:http` (HTTP mode), `npm run test:peer` (two bridges sharing one browser), and `npm run build` followed by `npm run test:package` (the bundle, run without `node_modules`).

`npm run build` makes `dist/cli.mjs`, a single file with no dependencies, plus `dist/extension`. That's what `npm run setup` installs. The unpacked extension ID, `alioifdhmmimahjfnfccegannpnnlmgm`, is fixed by the `key` in `manifest.json`, so pairing works for everyone who sideloads it. If the extension is ever published to the Chrome Web Store or npm, add the store ID to `EXTENSION_IDS` in `bridge/common.mjs`.

You can also skip setup's pairing and run `node bridge\server.mjs --print-token | Set-Clipboard` from the project root, then paste the token into the popup's **Manual settings**.

To test against your real Chrome, run `node test/live.mjs` from `bridge/`. It drives a local test page twice, once normally and once with the debugger fallback forced on. It waits until the extension version in Chrome matches `extension/manifest.json`, so reload the extension after any change.

### 2. Load the extension

1. Open `chrome://extensions` and turn on **Developer mode**.
2. Click **Load unpacked** and choose the repo's `extension/` folder (for development; it reloads straight from your edits).
3. It pairs itself as soon as a bridge is running. If you load it under a different extension ID, either run `npm run setup -- --extension-id <id>`, or paste the output of `npm run token` into the popup's **Manual settings**.

The badge shows **ON** once the bridge is running, which means Hermes has started it.

### 3. Point Hermes at the bridge

The easiest way is Hermes's CLI. This is the command used on Windows with native Hermes; adjust the paths for your machine:

```powershell
'Y' | hermes mcp add chrome --command "C:\Program Files\nodejs\node.exe" --env "HERMES_BROWSER_HOME=$env:USERPROFILE\.hermes-browser" --args "C:\path\to\hermes-browser\bridge\server.mjs"
hermes mcp test chrome
```

Piping `'Y'` answers the "Enable all 17 tools?" prompt. `HERMES_BROWSER_HOME` is set explicitly because Hermes gives MCP servers a filtered environment, and this keeps the bridge reading the same token file the extension uses. On native Windows, Hermes's config lives at `%LOCALAPPDATA%\hermes\config.yaml`. To remove it, run `hermes mcp remove chrome`.

To edit the config by hand instead, add this to `config.yaml` (`~/.hermes/config.yaml` on Linux/macOS):

```yaml
mcp_servers:
  chrome:
    command: "node"
    args: ["/absolute/path/to/hermes-browser/bridge/server.mjs"]
```

Restart Hermes. The tools appear as `chrome` MCP tools (Hermes may prefix them, for example `mcp_chrome_navigate`).

To try it without Hermes, use any MCP client, such as the MCP Inspector:

```powershell
npx @modelcontextprotocol/inspector node bridge/server.mjs
```

### Cloud Hermes (hosted agent) through an ngrok tunnel

A hosted Hermes can't launch a process on your PC, so the bridge runs in **HTTP mode** behind a tunnel:

```
Cloud Hermes ──HTTPS + Bearer token──▶ ngrok ──▶ 127.0.0.1:8766/mcp (bridge --http) ──ws 127.0.0.1:8765──▶ extension
```

Only the MCP port is tunneled. The extension's socket stays on localhost. The MCP token (`~/.hermes-browser/mcp-token`) is separate from the extension token.

One-time setup:
1. Install ngrok (`winget install Ngrok.Ngrok`), sign up at ngrok.com, and save your authtoken: `ngrok config add-authtoken <token>`. If `ngrok` isn't found yet, run it by its full path under `%LOCALAPPDATA%\Microsoft\WinGet\Packages\Ngrok.Ngrok_*\ngrok.exe`.
2. Copy your free static domain from https://dashboard.ngrok.com/domains.
3. Make sure no local Hermes is also running the bridge in stdio mode. Two bridges can't share port 8765.

Each time you want the cloud agent to use your browser:

```powershell
node bridge\tunnel.mjs your-domain.ngrok-free.dev   # domain is remembered; later just: node bridge\tunnel.mjs
```

It prints the URL and copies the MCP token to your clipboard. Keep that window open; Ctrl+C stops the bridge and the tunnel.

In the Hermes cloud dashboard, add a remote (HTTP) MCP server:
- **URL:** `https://your-domain.ngrok-free.dev/mcp`
- **Header:** `Authorization` = `Bearer <MCP token>`

If the dashboard has no field for headers, `https://.../mcp?token=<MCP token>` also works. Avoid it if you can, because URLs end up in logs.

To check the tunnel from outside, run `node bridge\test\remote-check.mjs`. It expects `/health` 200, `/mcp` without the token 401, 17 tools, and `tabs_list` reaching Chrome. To print the MCP token, run `node bridge\server.mjs --print-mcp-token`. To rotate it, delete `~/.hermes-browser/mcp-token`, restart the tunnel, and update the dashboard.

**Security:** anyone holding the URL **and** the MCP token can drive your signed-in browser. Keep the token secret, stop the tunnel when you aren't using it, and use the popup's switch as a kill switch.

### Hermes running in WSL, Chrome on Windows

- Install Node inside WSL, and run `npm install` and `npm run token` **inside WSL**. The token file lives in the WSL home, so paste *that* token into the extension.
- Use the Linux path in `config.yaml`, for example `/mnt/c/Users/<you>/.../bridge/server.mjs`.
- Chrome needs to reach the WSL port on `127.0.0.1`. If the popup stays "Not connected", turn on mirrored networking: add `networkingMode=mirrored` under `[wsl2]` in `%UserProfile%\.wslconfig`, then run `wsl --shutdown`.

## Configuration (environment variables on the bridge)

| Variable | Default | |
|---|---|---|
| `HERMES_BROWSER_PORT` | `8765` | Must match the port in the extension popup. |
| `HERMES_BROWSER_TOKEN` | contents of `~/.hermes-browser/token` | Shared secret. |
| `HERMES_BROWSER_HOST` | `127.0.0.1` | Interface to listen on. |
| `HERMES_BROWSER_TIMEOUT_MS` | `60000` | Per-call timeout. |
| `HERMES_BROWSER_SAVE_SCREENSHOTS` | `1` | Set `0` to stop saving screenshot files. |
| `HERMES_BROWSER_HOME` | `~/.hermes-browser` | Token and screenshot folder. |

## Security model

- The socket accepts only connections that present the token **and** whose `Origin` is a `chrome-extension://` URL. The one exception is other bridges, which connect with no `Origin` at all; browsers always send one. Web pages can't connect.
- **Pairing:** the extension sends `POST http://127.0.0.1:8765/pair`, and the bridge returns the token only when the `Origin` is exactly `chrome-extension://<Hermes Browser's ID>`. Browsers set `Origin` on every POST and pages can't forge it, so web pages, including DNS-rebinding tricks, and other extensions are refused. A local program could fake the header, but it could also read the token file directly, so pairing exposes nothing new.
- The bridge listens on loopback only by default.
- Untick "Allow Hermes to control this browser" in the popup to cut access instantly.
- Chrome shows a "started debugging this browser" bar while the agent controls a tab. This is expected and can't be hidden.
- **Prompt injection is the real risk.** Web pages can contain text written to manipulate the agent. The bridge tells the model to treat page content as data and to ask before sending, buying, deleting or entering passwords. A dedicated Chrome profile for the agent is still a good idea.

## When the debugger is blocked

Chrome refuses `chrome.debugger` on a tab once **another extension** injects a frame into the page. Password managers do this when you focus a login field. When that happens the tools fall back automatically:

- **Screenshots** normally go through the debugger, which works on background tabs. Without it they fall back to `chrome.tabs.captureVisibleTab`, which only sees the tab in front: the agent gets a clear error and can ask you, or call `tabs_select` with `focus: true`.
- **Click, hover, type, key, scroll and javascript** switch to DOM events sent from inside the page. Their results then end with `[fallback: ...]`. These events are synthetic (`isTrusted: false`), so a few sites that check for real input may ignore them.
- **Clicks by ref** target the element directly, so overlays can't steal them. Clicks by coordinates skip UI injected by other extensions.
- **Back and forward** fall back to `history.back()` when Chrome's back-button intervention skips pages that had no real user input.

## Limitations

- Chrome blocks `chrome://` pages and the Chrome Web Store from extensions.
- Native dialogs are detected through the debugger. On a tab where another extension blocks the debugger (see above), a dialog can't be seen or answered, and the tool times out instead.
- Browser UI outside the page (permission prompts, file pickers, print, downloads bar) can't be controlled.
- Clicking by coordinates needs a model that can read images. Text-only models should stick to `read_page` / `find` refs.
