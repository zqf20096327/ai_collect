<div align="center">

<img src="./images/bridge_logo.png" alt="Bridge Logo" width="520" />

# Bridge

**Universal Local-to-Web AI Coding Harness**

[![npm version](https://img.shields.io/badge/npm-v1.1.1-D2FF00.svg?style=flat-square&logo=npm)](https://www.npmjs.com/package/@markmayandi/bridge)
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
* **Terminal Dashboard:** Monospaced LN4 Volt interface with live traffic streaming and real-time directory switching. Adapts to any terminal size, from small windows to full screen.
* **Self-Healing Server:** If the MCP server crashes, Bridge restarts it automatically with backoff, and cleans up every child process on exit.

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

**Always blocked:** disk formatting, shutdown/reboot, `sudo`/`runas`, registry and boot configuration edits, user and service changes, disabling Defender or the firewall, scheduled tasks, piping downloads into a shell (`curl … | sh`, `iwr … | iex`), encoded PowerShell, and changes to system folders.

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
| `[Y]` / `[N]` | Approves or denies a pending permission request. |
| `[Q]` | Asks for confirmation (`Y`/`N`), then closes the tunnel, stops all jobs, releases ports, and exits. |

---

## Troubleshooting

* **Gemini keeps showing "Connecting to Bridge":** Check `~/.bridge/logs/server_requests.log`. If no new lines appear, the request never left Gemini, so resend your prompt. A `[CLIENT-ABORT]` or `[SSE-CLOSE]` line shows the connection dropped and why.
* **Gemini keeps asking for permission:** See the Gemini tip under [Connecting to Any AI Client](#connecting-to-any-ai-client).
* **Port 3000 is busy:** Quick tunnels pick a free port from 3001–3020 automatically. Named tunnels need port 3000; Bridge only stops old Bridge servers on it and never other apps.
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
