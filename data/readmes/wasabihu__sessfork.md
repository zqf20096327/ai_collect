# sessfork

[![CI](https://github.com/wasabihu/sessfork/actions/workflows/ci.yml/badge.svg)](https://github.com/wasabihu/sessfork/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](pyproject.toml)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0-22c55e.svg)](pyproject.toml)

**English** · [简体中文](README.zh-CN.md) · [Interactive Visual Guide](https://wasabihu.github.io/sessfork/)

**Fork live Chrome auth sessions (Cookies + LocalStorage) into headless AI agent browsers — zero window focus theft, zero runtime dependencies.**

![sessfork Before vs After](docs/assets/hero-en.svg)

When AI coding agents ([Google Antigravity](https://antigravity.google/docs/commands/browser/), Claude Code, or Cursor) connect directly to your main Chrome instance to reuse logged-in sessions, they hijack your active window, switch tabs, and break your flow.

`sessfork` decouples **your UI viewport** from **browser auth state** in a single command: it takes lock-free snapshots of your live Chromium SQLite `Cookies` database and LevelDB `Local Storage/leveldb` store, decrypts cookies in memory via native OS APIs, reconciles MVCC sequence numbers for SPA/JWT `localStorage` tokens, writes a strict `0600` [Playwright `storageState`](https://playwright.dev/docs/api/class-browser) file, and wires a silent background [Playwright MCP](https://github.com/microsoft/playwright-mcp) server (`sessfork-browser`) across your installed AI agents.

---

## 10-Second Lazy Quickstart

**Install once, then just talk to your AI agent in plain language.**

![3-Step Lazy Workflow](docs/assets/lazy-flow-en.svg)

### Option A · One-Click Auto-Setup (Recommended — zero prerequisites)

Auto-detects installed AI tools (**Antigravity**, **Claude Code**, **Cursor**), registers the background `sessfork-browser` MCP server, and installs the global Agent `SKILL.md`:

```bash
curl -fsSL https://raw.githubusercontent.com/wasabihu/sessfork/main/install.sh | bash
```

Want to fork your first domains in the very same command? Pass them right after `--`:

```bash
curl -fsSL https://raw.githubusercontent.com/wasabihu/sessfork/main/install.sh | bash -s -- github.com linear.app
```

*(Note: On each cookie fork, macOS asks to read `"Chrome Safe Storage"` from Keychain — click **Allow**. For pure LocalStorage JWT sites, pass `--no-cookies` for zero Keychain prompts. See the FAQ for the opt-in `--cache-key`.)*

### Option B · Zero-Install One-Shot (`uvx`)

Try `sessfork` immediately without touching global binaries:

```bash
uvx --from git+https://github.com/wasabihu/sessfork sessfork github.com
```

### Option C · Global `uv tool` or Editable Local Checkout

```bash
# Install globally via uv
uv tool install git+https://github.com/wasabihu/sessfork.git

# Or clone locally
git clone https://github.com/wasabihu/sessfork.git
cd sessfork
uv tool install -e .
```

*(Tip: Once installed, reload MCP servers once in your AI editor or run `/mcp` in CLI so `sessfork-browser` becomes active.)*

---

## 5 Real-World Copy-Paste Examples

Once installed, you don't even have to remember CLI flags. Copy any prompt below straight to your AI agent — or run the 1-line command directly.

### 1. Triage GitHub PRs & CI Failures Silently

> **Copy & paste to your AI Agent:**
> *"Use `sessfork` to fork my `github.com` login session into `sessfork-browser`, then silently check my unread notifications and review the failing PR checks without switching or touching my active Chrome window."*

```bash
sessfork github.com
```

### 2. Check Linear / Notion / Jira Sprint Tasks

> **Copy & paste to your AI Agent:**
> *"Fork my `linear.app` and `notion.so` sessions with `sessfork` and summarize today's assigned sprint blockers in the background."*

```bash
sessfork linear.app notion.so
```

### 3. Pure SPA / JWT Apps & Localhost (Zero Keychain Prompt)

Modern SPAs (Supabase, Vercel dashboards, local dev apps) store bearer tokens in `localStorage` instead of `HttpOnly` cookies. Skip Keychain completely with `--no-cookies`:

> **Copy & paste to your AI Agent:**
> *"Run `sessfork app.supabase.com localhost:3000 --no-cookies` and verify the authenticated dashboard API responses in `sessfork-browser`."*

```bash
sessfork app.supabase.com localhost:3000 --no-cookies
```

### 4. Paste Full URLs Straight from Your Address Bar

Don't bother stripping `https://` or paths — `sessfork` automatically normalizes full URLs to their domain allowlist:

```bash
sessfork https://github.com/notifications
```

### 5. Fork from Arc, Brave, Edge, or a Specific Work Profile

`sessfork` supports `chrome`, `canary`, `brave`, `edge`, and `arc`, and automatically discovers your most recently active profile (or lets you target one explicitly):

```bash
sessfork x.com --browser arc
sessfork console.cloud.google.com --profile "Profile 1"
```

---

## Architecture & Highlights

![sessfork Architecture](docs/assets/architecture-en.svg)

- **Zero Runtime Dependencies**: Pure Python standard library (`>=3.9`). Uses macOS `CommonCrypto` (`/usr/lib/libSystem.B.dylib` via `ctypes`) for AES-128-CBC cookie decryption (and `openssl` CLI on Linux) plus a built-in pure-Python [LevelDB SSTable/WAL](https://github.com/google/leveldb/blob/main/doc/log_format.md) + [Snappy](https://github.com/google/snappy/blob/main/format_description.txt) reader.
- **Full Dual-Layer Auth (`Cookies` + `LocalStorage`)**:
  - **SQLite Cookies**: Handles [Chromium Cookie DB `meta.version >= 24`](https://gist.github.com/creachadair/937179894a24571ce9860e2475a2d2ec) (`SHA-256(host_key)` 32-byte plaintext prefix stripping), live `-wal`/`-shm` sidecars, and `SameSite` / `HttpOnly` fidelity.
  - **LevelDB LocalStorage (`origins`)**: Parses Chromium's `_<origin>\x00` encoding-prefixed (`0x00` UTF-16LE / `0x01` Latin-1) records across `.ldb` SSTables and `.log` WALs, honoring `kTypeDeletion` tombstones (`localStorage.removeItem`) so logged-out JWTs are never resurrected.
- **One-Command Auto-Wiring**: `sessfork <domain>` and `sessfork --setup` auto-detect Antigravity, Claude Code, and Cursor (`--target auto`), resolve absolute `npx` paths (avoiding [macOS GUI `$PATH` launch failures](https://discuss.ai.google.dev/t/bug-mcp-servers-crash-with-executable-file-not-found-in-path-when-antigravity-is-launched-via-macos-gui/138495)), and install `SKILL.md`.

---

## Cheat Sheet

| Goal | Command |
| :--- | :--- |
| One-time setup (MCP + Skill for all detected agents) | `sessfork --setup` |
| Fork Cookies + LocalStorage for domains | `sessfork github.com linear.app` |
| Fork LocalStorage JWT only (zero Keychain prompt) | `sessfork app.spa.io --no-cookies` |
| Fork SQLite Cookies only | `sessfork github.com --no-local-storage` |
| Choose source browser (`chrome`, `arc`, `brave`, `edge`, `canary`) | `sessfork x.com --browser arc` |
| Target specific profile folder | `sessfork github.com --profile "Profile 1"` |
| Wire Antigravity + Claude Code + Cursor explicitly | `sessfork --setup --target all` |
| Inspect cached domains & origins (redacted, safe) | `sessfork --status` |
| Re-fork all domains currently saved in `state.json` | `sessfork --refresh` |
| Opt-in: cache the derived key to skip future Keychain prompts (see FAQ) | `sessfork github.com --cache-key` |
| Force re-read the key from Keychain (e.g. after Chrome rotated it) | `sessfork github.com --refresh-key` |
| Delete any cached derived keys | `sessfork --purge-keys` |
| Remove cached state for specific domain (or all) | `sessfork --clear linear.app` / `sessfork --clear` |

---

## FAQ

<details>
<summary><strong>How is sessfork different from dedicated AI browsers (such as ego-lite)?</strong></summary>

Dedicated AI browsers (like `ego-lite`) ship a separate Chromium desktop app with built-in workspaces and import your Chrome profile so agents can act visually alongside you. `sessfork` takes a deliberately lighter, least-privilege approach:

- **Keep your existing browser**: No second desktop browser to install, maintain, or migrate to — keep using your native Chrome, Arc, Brave, or Edge as usual.
- **Domain-scoped isolation (least privilege)**: Instead of handing an AI browser your entire profile (banking, primary email, corporate SSO, extensions, and all open tabs), `sessfork` forks **only the exact domains you allowlist** (e.g. `sessfork github.com linear.app`) into a one-way `0600` snapshot.
- **Standard Playwright ecosystem**: Outputs standard Playwright `storageState` JSON, so it plugs straight into official `@playwright/mcp` as well as your own Playwright scripts and headless automation pipelines.

Choose a dedicated AI browser if you want a visual cursor watching the agent click or routinely deal with heavy headed anti-bot flows; choose `sessfork` if you want a zero-dependency CLI that keeps your main browser untouched and exposes only selected domains to a silent headless agent.

</details>

<details>
<summary><strong>Why does macOS ask for Keychain access when forking cookies?</strong></summary>

Chromium encrypts cookie values using a master passphrase stored under `"Chrome Safe Storage"` in your macOS Keychain. Click **Allow** so macOS authorizes `security` to read that entry. If a site uses `localStorage` tokens (many modern SPAs), pass `--no-cookies` to bypass Keychain completely.

By default `sessfork` does **not** store the derived decryption key anywhere, so macOS stays in charge of every authorization. If you prefer convenience, `--cache-key` saves the derived key to `~/.sessfork/keys.json` (`0600`). Trade-off: any process running under your user account could then read that file and decrypt your Chrome cookies without a Keychain prompt. Run `sessfork --purge-keys` to remove it at any time.

</details>

<details>
<summary><strong>Which platforms are supported?</strong></summary>

- **macOS**: fully supported and tested on real Chrome profiles.
- **Linux**: experimental — covered by unit tests, but not yet verified against many real-world Chrome/Secret Service setups. Bug reports welcome.
- **Windows**: not supported (Chromium on Windows uses DPAPI / app-bound encryption).

</details>

<details>
<summary><strong>I just signed in 1 second ago and a LocalStorage token is missing — why?</strong></summary>

Chromium batches `localStorage` flushes from memory to LevelDB on disk roughly every 5 seconds. Wait ~5 seconds after signing in and re-run `sessfork <domain>`.

</details>

<details>
<summary><strong>How do I revoke or clean up forked session data?</strong></summary>

Run `sessfork --clear <domain>` to purge a single site, or `sessfork --clear` (or `rm -rf ~/.sessfork`) to wipe all cached session state.

</details>

<details>
<summary><strong>Do I need to restart my AI editor every time I fork a new domain or refresh cookies?</strong></summary>

No — only reload MCP once right after initial installation. Whenever you run `sessfork <domain>` or `sessfork --refresh`, `sessfork` updates an atomic `0600` mirror at `~/.sessfork/playwright-output/.sessfork-state.json` inside Playwright MCP's `--output-dir` sandbox, and your AI agent hot-reloads it straight into the running `sessfork-browser` via `browser_set_storage_state` with zero restarts.

</details>

---

## Security & Responsible Use

- **Domain Allowlist by Default**: Only the domains/origins you explicitly name are extracted.
- **Strict File Permissions**: `~/.sessfork/` is `0700` and `~/.sessfork/state.json` is atomically created with `0600` permissions before a single byte is written.
- **Redacted Diagnostics**: `sessfork --status`, `--json`, and `SKILL.md` never print raw cookie or LocalStorage values to stdout or agent prompt context.
- **No Key Persistence by Default**: The derived cookie key lives only in memory for the duration of one command. Persisting it (`--cache-key`) is an explicit opt-in.
- **Isolated Headless Browser**: `sessfork-browser` runs `@playwright/mcp --headless --isolated`, so each MCP session starts from the forked `state.json` instead of a persistent profile. Page snapshots and screenshots go to `~/.sessfork/playwright-output/` (`--output-dir`), never into a `.playwright-mcp/` folder inside your projects.
- **Responsible Use**: `sessfork` operates strictly within your signed-in OS user account and relies on native OS keyring authorization (macOS Keychain / Linux Secret Service) — it never bypasses OS access controls or sandboxes. Use it only on devices and accounts you own or are explicitly authorized to test, and always comply with target websites' Terms of Service.
- **Reporting Vulnerabilities**: See [SECURITY.md](SECURITY.md).

## Development & Tests

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

## License

[MIT](LICENSE)
