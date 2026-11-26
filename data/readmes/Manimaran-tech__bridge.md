<div align="center">

<img src="./images/bridge_logo.png" alt="Bridge Logo" width="520" />

# Bridge

**Universal Local-to-Web AI Coding Harness**

[![npm version](https://img.shields.io/badge/npm-v1.2.1-D2FF00.svg?style=flat-square&logo=npm)](https://www.npmjs.com/package/@markmayandi/bridge)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Node.js](https://img.shields.io/badge/node-%3E%3D18.0.0-green.svg?style=flat-square&logo=node.js)](https://nodejs.org/)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg?style=flat-square)](https://github.com/Manimaran-tech/bridge)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

<p align="center">
  <b>English</b> | <a href="./README_zh.md">简体中文</a>
</p>

<p align="center">
  Securely connect your local codebases and development environments to Claude Web, ChatGPT, Gemini, and DeepSeek in seconds via the Model Context Protocol (MCP).
</p>

<p align="center">
  <img src="./images/bridge-demo.gif" alt="Bridge demo: install, run bridge, pick a project folder, get the MCP URL" width="820" />
  <br />
  <sub>Install → run <code>bridge</code> → pick a project → copy your MCP URL (<a href="./images/bridge-demo.mp4">MP4 version</a>)</sub>
</p>

---

</div>

## Quickstart

### 1. Instant Execution (Zero Install)

Run directly using `npx`:

```bash
npx @markmayandi/bridge
```

### 2. Global Installation

Install globally to access the `bridge` command anywhere:

```bash
npm install -g @markmayandi/bridge
```

Then navigate to any folder and start:

```bash
bridge .
```

### 3. Clone and Run from Source

To inspect the source, customize, or contribute:

```bash
git clone https://github.com/Manimaran-tech/bridge.git
cd bridge
node bridge.js
```

Or pass a specific project directory directly:

```bash
node bridge.js /path/to/project
```

### 4. Docker Sandbox (Optional)

Use Docker Engine / Docker Desktop (Linux containers) and Docker Compose v2 to keep shell execution off your host. From a source checkout:

1. Copy `.env.example` to `.env`.
2. Generate a strong token with `node -e "console.log(require('node:crypto').randomBytes(24).toString('hex'))"` and set `BRIDGE_TOKEN` in `.env`.
3. Set `BRIDGE_WORKSPACE` in `.env` to an **existing, dedicated project folder**. Relative paths resolve from `docker-compose.yml`; Windows paths can use forward slashes, such as `C:/Users/you/projects/my-app`. Do not mount your home directory or the Bridge checkout containing `.env`.
4. Build and start:

```bash
docker compose up --build -d
docker compose logs -f bridge-sandbox
```

The authenticated MCP endpoint is `http://127.0.0.1:3000/mcp`. Configure your client with `Authorization: Bearer <BRIDGE_TOKEN>`, or use `http://127.0.0.1:3000/mcp?token=<BRIDGE_TOKEN>` if it requires a URL token. Treat the token and authenticated URL as secrets. A quick authentication check:

```bash
# Without authentication: expect 401.
curl -i http://127.0.0.1:3000/api/status
# Replace <BRIDGE_TOKEN> with your configured token: expect 200.
curl -i -H "Authorization: Bearer <BRIDGE_TOKEN>" http://127.0.0.1:3000/api/status
```

For web AI clients, run `cloudflared tunnel --url http://127.0.0.1:3000` **on the host** and use the resulting HTTPS URL with the same authentication. The container does not launch a tunnel, open a dashboard, copy a URL, or read your host's `~/.bridge/config.json`. The default approval mode still applies; without the dashboard, actions requiring human approval are denied. Shell execution is enabled; to disable it, add `command: ["/workspace", "--http", "3000", "--disable-shell"]` to the Compose service.

**Sandbox boundaries:**

- Only the selected host project is bind-mounted, read/write, at `/workspace`. Changes affect the host immediately; use version control and backups. Keep host credentials and sensitive files out of this folder.
- The server runs as the non-root `node` user (UID/GID `1000:1000`) with a read-only root filesystem, all Linux capabilities dropped, and `no-new-privileges`. On native Linux, grant that user access to the chosen folder; do not solve permission errors by running as root or making it world-writable.
- Compose binds the published port only to host loopback. `BRIDGE_HOST=0.0.0.0` applies **inside** the container so Docker port forwarding works; it does not make the published host port public. Use a current Docker Engine (28 or newer) for loopback port isolation fixes.
- CPU, memory, process count, and temporary storage are capped. `/tmp` and `/home/node` are writable, size-limited tmpfs mounts. Logs, trash, and other home-directory state are ephemeral and are lost when the container stops; a deleted file's trash copy is not a durable backup.
- Containers share a kernel and are defense in depth, not a zero-trust guarantee. Commands can access container files, environment variables (including the Bridge token), mounted project secrets, and reachable networks. Outbound traffic is not blocked. Never mount the Docker socket, host credentials, or additional sensitive paths; use a VM and network controls for stronger isolation.

Stop and remove the sandbox with `docker compose down`. The image includes Node.js, Bash, Git, and curl; other project toolchains must be added to a custom image. Only the server and package metadata enter the image build context, not your workspace or `.env`.

Alpine packages are upgraded at build time to pick up available security fixes. The bundled npm, npx, Yarn, and Corepack files and launchers are removed to reduce unused dependencies and CVEs; Bridge runs with plain `node` and does not need package managers at runtime. Rebuild with `docker compose build --pull --no-cache` to refresh the base image and Alpine packages.

If your workspace needs package managers, restore them in a custom image. For example, first build Bridge with `docker build -t bridge-sandbox:local .`, then use this separate Dockerfile to restore npm and npx:

```dockerfile
FROM node:24-alpine AS node-tools
FROM bridge-sandbox:local
USER root
COPY --from=node-tools /usr/local/lib/node_modules/npm /usr/local/lib/node_modules/npm
RUN ln -s ../lib/node_modules/npm/bin/npm-cli.js /usr/local/bin/npm \
    && ln -s ../lib/node_modules/npm/bin/npx-cli.js /usr/local/bin/npx
USER node
```

To add Yarn or Corepack too, add `RUN npm install --global yarn corepack` before `USER node`. Build and select your custom image in Compose while retaining the existing hardening settings. Restoring package managers adds their dependencies and potential CVEs back to the image; scan the custom image as well. The default read-only root filesystem still prevents runtime global installs.

**Verification:** Run `npm run test:host-binding` for binding and authentication regressions. On Linux/WSL with a running Docker daemon, Node.js >=18, and Compose >=2.24.4, run `npm run test:docker` to build the actual image and verify authentication, MCP file/shell operations, persistence across restarts, effective runtime restrictions, and image contents. The integration test uses a disposable workspace and an ephemeral loopback port, leaving existing port-3000 listeners alone, then removes its containers, image, network, and temporary files. Run it with a local Docker daemon and permission to access its socket.

### Command-Line Options

| Command | Description |
| :--- | :--- |
| `bridge [folder]` | Start Bridge for a project folder (opens the folder navigator if omitted). |
| `bridge . --mode=<mode>` | Start with an approval mode: `turbo`, `review`, `default` or `auto` (see [Approval Modes](#approval-modes)). |
| `bridge setup` | One-time setup for a fixed URL via a Cloudflare named tunnel. |
| `bridge rotate-token` | Replace the saved auth token. Connected AI clients must re-paste the new URL. |

---

## Universal MCP Connection

Bridge automatically creates an Anycast HTTPS tunnel, attaches your auth token, and copies the authenticated endpoint to your clipboard:

```text
https://xxxx.trycloudflare.com/mcp?token=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Authentication & Security Model

Bridge features built-in zero-trust security:
- **Bearer Token Auth**: Every HTTP/SSE endpoint (`/mcp`, `/call`, `/api/set-directory`, `/api/status`, `/openapi.json`) requires a valid token via `Authorization: Bearer <token>` or `?token=<token>`. Unauthenticated requests are rejected with `401 Unauthorized`.
- **Persistent Token**: On first run, Bridge generates a 24-byte cryptographic hex token and saves it in `~/.bridge/config.json`, so your AI connectors keep working across restarts. Run `bridge rotate-token` to replace it.
- **Custom Token**: Supply your own token with the `BRIDGE_TOKEN` environment variable.
- **Loopback Binding by Default**: The local MCP server listens on `127.0.0.1` unless `BRIDGE_HOST` is set. Set `BRIDGE_HOST=0.0.0.0` only when needed for containers or deliberately exposing another interface; retain authentication and restrict access with port publishing or a firewall.
- **Shell Disablement**: When running the MCP server directly (`node secure-folder-mcp/server.js <folder> --disable-shell`), shell tools are turned off and only sandboxed file operations remain.

### Optional: Fixed MCP URL (Cloudflare Named Tunnels)

By default Bridge uses an ephemeral quick tunnel. If you want a stable, permanent domain, create a named Cloudflare tunnel and configure Bridge with its token:

1. In **Cloudflare Zero Trust → Networks → Tunnels**, create a named tunnel and copy its token.
2. Add a **Public Hostname** for that tunnel pointing to `http://localhost:3000`.
3. Run the one-time interactive setup:

```bash
bridge setup
# With npx: npx @markmayandi/bridge setup
# Tunnel token: (hidden)
# Public URL: https://mcp.example.com
```

4. Start Bridge normally:

```bash
bridge .
# With npx: npx @markmayandi/bridge .
```

The fixed endpoint will then be `https://mcp.example.com/mcp?token=<token>`, with credentials stored safely in `~/.bridge/config.json` (permissions `0600`). Bridge manages this independently without interfering with existing `~/.cloudflared` configurations. To switch back to ephemeral quick tunnels at any time, simply delete `~/.bridge/config.json`.

### Connecting to Any AI Client

Modern web AI clients (Claude Web, ChatGPT Web, Gemini, and MCP extensions) connect directly using the authenticated `/mcp` URL:

1. Copy your live MCP URL from Bridge (automatically placed in your clipboard on startup).
2. Paste the URL directly into your AI client's MCP or custom tool integration.
3. Your AI model now has real-time, sandboxed read, write, edit, and terminal test execution capabilities on your local project.

No legacy JSON configuration files or manual port forwarding required.

> **Gemini: use Task, not Chat.** Start your Bridge work in a Gemini **Task** instead of a normal **Chat**. Multi-step coding work with Bridge's tools runs more reliably in a Task.
>
> **Gemini tip:** Gemini shows its own "Let Gemini use …?" card before tool calls. This is Gemini's permission system, separate from Bridge's approval modes. To stop the cards, open **Gemini → Customize → Connectors → Bridge** ([gemini.google.com/customize/connectors](https://gemini.google.com/customize/connectors)) and set each action under **App actions** to **Always allow**. A quick tunnel gets a new URL on every restart, so use a [named tunnel](#optional-fixed-mcp-url-cloudflare-named-tunnels) if you want these settings to stick.

---

## What Bridge Does

Cloud-based AI models cannot safely access files on your physical machine without open ports or copy-pasting code snippets. Bridge solves this with a high-performance local daemon:

* **Strict Directory Jail:** AI operations are strictly restricted to the specified project folder with zero parent-directory traversal.
* **Native Tool Suite:** Files (`read_file`, `read_files`, `write_file`, `write_files`, `edit_file`, `str_replace_editor`, `delete_file`, `revert_file`, `search_files`, `list_directory`), shell (`execute_command`, `pwsh`, `bash`, background `jobs`), git (`git_status`, `git_diff`), plus planning, dependency inspection and web documentation fetching.
* **Approval Modes:** Choose how often Bridge asks you before acting: never, always, only for deletes, or let Bridge decide.
* **Undo & Trash:** Every write keeps an undo snapshot, and deleted files move to `~/.bridge/trash` instead of being erased.
* **Long-Running Calls:** Tool replies stream over SSE with keepalives, so long builds and tests survive Cloudflare's 100-second timeout.
* **Zero-Setup Anycast Tunnel:** Public HTTPS tunneling powered by Cloudflare with automatic SSL and clipboard sync. Run `bridge setup` once if you prefer a fixed named-tunnel URL.
* **Terminal Dashboard:** Monospaced LN4 Volt interface with live traffic streaming and real-time directory switching. Adapts to any terminal size, from small windows to full screen, and redraws cleanly when you resize or maximize the window, even during the loading screens.
* **Overview Panel:** Review every change the AI made with diffs and undo, verify files on disk, and watch or stop running commands. Open it with `[S]` or by clicking the `≡` button in the top-right corner.
* **Live Tunnel Animation:** While the tunnel starts, a two-lane link shows requests going out and replies coming back through the Cloudflare edge, with a checklist of each startup stage.
* **Multiple Bridges:** Run several Bridges side by side for different projects. A new Bridge never stops another running Bridge's server; it picks the next free port instead.
* **Self-Healing Server:** If the MCP server crashes, Bridge restarts it automatically with backoff, and cleans up every child process on exit.
* **Auto Context Compaction:** Bridge meters the tool output it sends into the chat and asks the AI to save a checkpoint before the context fills up (see [Context Compaction](#context-compaction)).

---

## Context Compaction

Long coding sessions fill a chat's context with file contents and command output. Bridge cannot erase a cloud chat's history, so it compacts the way a human would: summarize, then continue from the summary.

1. **Metering:** Bridge estimates the tokens of every tool call and result (about 4 characters per token). At 60% of the budget it appends a `[Bridge context notice]` to the tool result; at 85% the notice becomes urgent and repeats every 5 calls.
2. **`compact_context`:** The AI writes a summary (goal, decisions, progress, next steps, open questions, key files). Bridge adds what it knows itself: the plan, files changed through Bridge, recent commands, running background jobs and `git status`. The checkpoint is saved and the meter resets. The AI then works from the checkpoint instead of re-reading earlier output.
3. **`resume_context`:** In a new chat, ask the AI to "resume" (or use the `resume_session` MCP prompt). It loads the newest checkpoint for the active project; `list=true` shows all of them.

Checkpoints are stored outside your project in `~/.bridge/context/<project-hash>/` (the last 20 per project). After 60 idle minutes the meter resets, since that usually means a new chat.

| Setting | Default | Description |
| :--- | :--- | :--- |
| `BRIDGE_CONTEXT_BUDGET` / `--context-budget <n>` | `100000` | Tokens of tool traffic before notices start. `0` turns notices off. |
| `BRIDGE_CONTEXT_IDLE_RESET_MIN` | `60` | Idle minutes after which the meter resets. `0` never resets. |
| `BRIDGE_CONTEXT_DIR` | `~/.bridge/context` | Where checkpoints are stored. |

The meter only sees Bridge's own tool traffic, not your messages or the AI's replies, so set the budget well below your model's context window.

---

## Approval Modes

Press `[M]` in the dashboard (or launch with `--mode=<mode>`) to choose when Bridge asks you for permission. Your choice is saved for next time.

| Mode | Reads | Writes / Edits | Normal Commands | Deletes, Destructive Git, Secret Files | Harmful Commands |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Turbo** | Allowed | Allowed | Allowed | Allowed | Always blocked |
| **Review** | Allowed | Asks | Asks | Asks | Always blocked |
| **Default** | Allowed | Allowed | Allowed | Asks | Always blocked |
| **Auto** | Allowed | Allowed | Allowed | Asks, except `delete_file` (recoverable from trash) and rebuildable folders (`node_modules`, `dist`, `build`, caches) | Always blocked |

When Bridge asks, the request appears in the dashboard with the full command. Press `[Y]` to approve or `[N]` to deny. Unanswered requests are denied automatically after 90 seconds.

**Always blocked:** disk formatting, shutdown/reboot, `sudo`/`runas`, registry and boot configuration edits, user and service changes, disabling Defender or the firewall, scheduled tasks, piping downloads into a shell (`curl … | sh`, `iwr … | iex`), decoding base64 straight into a shell (`base64 -d … | sh`, `FromBase64String … | iex`), encoded PowerShell, and changes to system folders.

**Switching folders:** an AI can move to another project folder when you ask it to. Drive roots, your home folder and system folders are always refused. Depending on the mode, Bridge asks you first.

---

## Security Model

| Security Vector | Implementation |
| :--- | :--- |
| **Authentication & Authorization** | All HTTP and SSE endpoints enforce Bearer authentication (`Authorization: Bearer <token>` or `?token=<token>`). Unauthenticated requests are rejected with `401 Unauthorized`. |
| **Path Traversal Protection** | Evaluates canonical `fs.realpathSync`, including for files that don't exist yet. Access outside the targeted root jail is immediately blocked. |
| **Symlink Boundary Checks** | Validates symlink and junction resolution. Denies read/write operations targeting locations outside the project folder; search and listing skip outside links. |
| **Data Integrity** | Writes are atomic (temp file + rename), multi-file writes roll back on failure, `.git` internals are write-protected, and every change keeps an undo snapshot. |
| **Secrets Protection** | Search skips sensitive files, and commands that read `.env`, keys, `.ssh` or `.npmrc` ask you first. |
| **SSRF Protection** | Web documentation fetches allow public HTTPS only, block private and local addresses (including after redirects), and enforce size and time limits. |
| **Resource Limits** | Request, read and output size limits, a cap on concurrent background jobs, and full process-tree cleanup on stop and exit. |
| **Local Port Isolation** | Local server binds to `127.0.0.1` by default; `BRIDGE_HOST` can override the interface. The Docker Compose deployment publishes only on host loopback. Remote traffic can route through HTTPS tunnels. |
| **Execution Policy & Disablement** | Shell tools (`pwsh`, `bash`, `execute_command`) are protected by safety policies, restricted to root directory, and can be disabled completely with `--disable-shell`. |
| **Live Traffic Audit** | Press `[L]` at any time to stream every incoming JSON-RPC request and tool call in real time. |
| **Diagnostic Log** | `~/.bridge/logs/server_requests.log` records requests, SSE stream open/close, client disconnects, approvals and per-call timing. Tokens are redacted; the log rotates at 10 MB. |

---

## Keyboard Controls

| Key | Action |
| :--- | :--- |
| `[C]` | Re-copies the authenticated MCP URL to your clipboard. |
| `[T]` | Copies the Bearer authentication token to your clipboard. |
| `[D]` | Opens the In-Terminal Directory Navigator to switch project folders without restarting. |
| `[L]` | Toggles real-time streaming traffic and tool execution logs. |
| `[M]` | Opens the approval mode picker (`1` Turbo, `2` Review, `3` Default, `4` Auto). |
| `[S]` | Opens the Overview panel (`[R]` Review, `[F]` Files, `[T]` Terminals, `[H]` Help). You can also click the `≡` button in the top-right corner. |
| `[Y]` / `[N]` | Approves or denies a pending permission request. |
| `[Q]` | Asks for confirmation (`Y`/`N`), then closes the tunnel, stops all jobs, releases ports, and exits. |

### Overview Panel

Press `[S]` or click the `≡` button in the dashboard's top-right corner to open the live **Overview** menu (click an item to open it, click elsewhere to close) with session `+added / −removed` totals, touched file counts, and running process counts:

* **`[R]` Review:** Inspect every file the AI created, edited, or deleted in the current session with a unified diff, `(edited outside)` detection, `[U]` undo (reuses revert snapshots), and `[O]` open in your default editor.
* **`[F]` Files:** Verify on disk (`✔` exists, `✘` missing, `🗑` in trash) that files the AI touched actually exist. Press `[A]` to toggle the full sandboxed project tree or `Enter` to jump to a file's diff.
* **`[T]` Terminals:** View running and finished commands and background jobs, stop any process tree with `[X]`, or press `Enter` to attach full-screen in Chrome-style tabs (`Ctrl+←/→` switch tab, `Ctrl+W` close, `Ctrl+X` stop, `Ctrl+]` detach, `Ctrl+T` list). Attached terminals provide local line editing and multi-line paste on a bottom prompt line (`Enter` sends the line, `Backspace` deletes, `←/→` moves the cursor, `Ctrl+U` clears the line, `Ctrl+D` flushes any pending text and sends EOF, and `Esc` forwards immediately).
* **`[H]` Help:** Built-in scrollable reference for all shortcuts, icons, approval modes, safety boundaries, and log paths.

Approval prompts (`[Y]`/`[N]`) always appear on top of every Overview view; while attached to a terminal, approval keys require a short pause in typing before `[Y]`/`[N]`/`[Esc]` are accepted.

---

## Troubleshooting

* **Gemini keeps showing "Connecting to Bridge":** Check `~/.bridge/logs/server_requests.log`. If no new lines appear, the request never left Gemini, so resend your prompt. A `[CLIENT-ABORT]` or `[SSE-CLOSE]` line shows the connection dropped and why.
* **Gemini keeps asking for permission:** See the Gemini tip under [Connecting to Any AI Client](#connecting-to-any-ai-client).
* **Port 3000 is busy:** Quick tunnels pick a free port from 3001–3020 automatically. Named tunnels need port 3000, so only one Bridge can use a named tunnel at a time. Bridge only stops a Bridge server on port 3000 if the Bridge that started it has exited; it never stops another running Bridge or any other app.
* **Selecting text in the dashboard:** Bridge listens for mouse clicks (for the `≡` button), so hold `Shift` while dragging to select text. `[C]` copies the MCP URL directly.
* **Update banner:** Bridge checks npm on startup and shows an update only when a newer version exists. Upgrade with `npm install -g @markmayandi/bridge@latest`.

---

## Acknowledgements & Credits

Bridge builds upon foundational open-source architecture and local daemon patterns inspired by the [DeepSeek](https://github.com/deepseek-ai) harness community. We extend our sincere gratitude to the open-source AI developer ecosystem for advancing local tooling.

---

## License

Distributed under the **MIT License**. See `LICENSE` for details.

<div align="center">
  <sub>Maintained by <a href="https://github.com/Manimaran-tech">Manimaran</a></sub>
</div>
