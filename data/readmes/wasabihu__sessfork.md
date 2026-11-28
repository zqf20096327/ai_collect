# sessfork

[![CI](https://github.com/wasabihu/sessfork/actions/workflows/ci.yml/badge.svg)](https://github.com/wasabihu/sessfork/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](pyproject.toml)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0-22c55e.svg)](pyproject.toml)
[![wasabihu/sessfork MCP server](https://glama.ai/mcp/servers/wasabihu/sessfork/badges/score.svg)](https://glama.ai/mcp/servers/wasabihu/sessfork)
[![Listed on mcpservers.org](https://mcpservers.org/badge.svg)](https://mcpservers.org/servers/wasabihu/sessfork)

**English** · [简体中文](README.zh-CN.md) · [Native Rust CDP MCP](rust/sessfork-mcp/README.md) · [Interactive Visual Guide](https://wasabihu.github.io/sessfork/) · [Stress Benchmarks](docs/benchmarks.md) · [Security Audit Report](docs/security-report.md)

**Fork live Chrome auth sessions (Cookies + LocalStorage) into headless AI agent browsers — zero window focus theft, zero runtime dependencies.**

![sessfork Before vs After](docs/assets/hero-en.svg)

When AI coding agents ([Google Antigravity](https://antigravity.google/docs/commands/browser/), Claude Code, or Cursor) connect directly to your main Chrome instance to reuse logged-in sessions, they hijack your active window, switch tabs, and break your flow.

`sessfork` decouples **your UI viewport** from **browser auth state** in a single command: it takes lock-free snapshots of your live Chromium SQLite `Cookies` database and LevelDB `Local Storage/leveldb` store, decrypts cookies in memory via native OS APIs, reconciles MVCC sequence numbers for SPA/JWT `localStorage` tokens, writes a strict `0600` [Playwright `storageState`](https://playwright.dev/docs/api/class-browser) file, and wires a silent background [Playwright MCP](https://github.com/microsoft/playwright-mcp) server (`sessfork-browser`) across your installed AI agents.

> [!TIP]
> **Looking for `sessfork-mcp` × [`lexmount/moli`](https://github.com/lexmount/moli) (605 KB zero-Node.js Rust MCP)?**
> Independently verified by the Moli team at **`-90.7%` RAM (`226.3 MiB` vs `2,439.5 MiB`) and `2.76×` faster** than Chrome + Playwright MCP (Apple M4, 5-run medians — [Discussion #3465](https://github.com/lexmount/moli/discussions/3465#discussioncomment-19846839)).
> - **Standalone Moli MCP (no Python or Chrome required):** see **[rust/sessfork-mcp/README.md](rust/sessfork-mcp/README.md)** (`install.sh --rust-mcp-only` + 1-line `claude mcp add`).
> - **Chrome session forking + Dual Moli/Chrome engine:** run `curl --proto '=https' --tlsv1.2 -fsSL https://raw.githubusercontent.com/wasabihu/sessfork/v0.2.1/install.sh | bash -s -- --with-rust-mcp` and `sessfork --engine dual` (full breakdown in [docs/benchmarks.md](docs/benchmarks.md)).

---

## 10-Second Lazy Quickstart

**Install once, then just talk to your AI agent in plain language.**

![3-Step Lazy Workflow](docs/assets/lazy-flow-en.svg)

### Option A · One-Click Auto-Setup (Recommended — zero prerequisites)

Auto-detects installed AI tools (**Antigravity**, **Claude Code**, **Cursor**, **OpenCode**, **Gemini CLI**, **WorkBuddy**, **Windsurf**, **Codex CLI**), registers the background `sessfork-browser` MCP server, and installs the global Agent `SKILL.md`:

```bash
curl --proto '=https' --tlsv1.2 -fsSL https://raw.githubusercontent.com/wasabihu/sessfork/v0.2.1/install.sh | bash
```

Want to fork your first domains in the very same command? Pass them right after `--`:

```bash
curl --proto '=https' --tlsv1.2 -fsSL https://raw.githubusercontent.com/wasabihu/sessfork/v0.2.1/install.sh | bash -s -- github.com linear.app
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

## 7 Real-World Copy-Paste Examples

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

### 6. Feed Live Sessions Straight into `agent-browser` (Zero Profile Copy)

Because `sessfork` writes standard Playwright `storageState` JSON (`0600`), you can pass a single domain's `HttpOnly` cookies + `localStorage` straight into [`vercel-labs/agent-browser`](https://github.com/vercel-labs/agent-browser) without copying a multi-GB Chrome profile or restoring unrelated tabs:

```bash
sessfork example.com --target none --state-file ~/.sessfork/agent-browser.json
agent-browser --state ~/.sessfork/agent-browser.json open https://example.com
```

### 7. Authenticated Crawling with `Crawl4AI` (Zero Re-Login, Zero Profile Clone)

Feed a single domain's live Chrome/Edge session (`0600` Playwright `storageState`) directly into local [`unclecode/crawl4ai`](https://github.com/unclecode/crawl4ai) without re-authenticating in a second Chromium window (`crwl profiles`) or copying GB-sized profile folders — including Windows Chrome 127+ `v20` via the Companion Extension:

```bash
sessfork docs.example.com --target none --state-file ~/.sessfork/crawl4ai.json
```

```python
import asyncio, os
from crawl4ai import AsyncWebCrawler, BrowserConfig

async def main():
    cfg = BrowserConfig(headless=True, storage_state=os.path.expanduser("~/.sessfork/crawl4ai.json"))
    async with AsyncWebCrawler(config=cfg) as crawler:
        result = await crawler.arun(url="https://docs.example.com/private")
        print(result.markdown.raw_markdown)

asyncio.run(main())
```

*(Full runnable script with `fit_markdown` and JSONL export for local RAG ingestion: [`examples/crawl4ai_auth_crawl.py`](examples/crawl4ai_auth_crawl.py). Complements Crawl4AI's `ManagedBrowser` — for strict anti-bot / device-fingerprint portals, keep using a persistent `ManagedBrowser` profile.)*

---

## Architecture & Highlights

![sessfork Architecture](docs/assets/architecture-en.svg)

- **Zero Runtime Dependencies**: Pure Python standard library (`>=3.9`). Uses macOS `CommonCrypto` (`/usr/lib/libSystem.B.dylib` via `ctypes`) for AES-128-CBC cookie decryption (and `openssl` CLI on Linux) plus a built-in pure-Python [LevelDB SSTable/WAL](https://github.com/google/leveldb/blob/main/doc/log_format.md) + [Snappy](https://github.com/google/snappy/blob/main/format_description.txt) reader.
- **Full Dual-Layer Auth (`Cookies` + `LocalStorage`)**:
  - **SQLite Cookies**: Handles [Chromium Cookie DB `meta.version >= 24`](https://gist.github.com/creachadair/937179894a24571ce9860e2475a2d2ec) (`SHA-256(host_key)` 32-byte plaintext prefix stripping), live `-wal`/`-shm` sidecars, and `SameSite` / `HttpOnly` fidelity.
  - **LevelDB LocalStorage (`origins`)**: Parses Chromium's `_<origin>\x00` encoding-prefixed (`0x00` UTF-16LE / `0x01` Latin-1) records across `.ldb` SSTables and `.log` WALs, honoring `kTypeDeletion` tombstones (`localStorage.removeItem`) so logged-out JWTs are never resurrected.
- **One-Command Auto-Wiring**: `sessfork <domain>` and `sessfork --setup` auto-detect Antigravity, Claude Code, and Cursor (`--target auto`), resolve absolute `npx` paths (avoiding [macOS GUI `$PATH` launch failures](https://discuss.ai.google.dev/t/bug-mcp-servers-crash-with-executable-file-not-found-in-path-when-antigravity-is-launched-via-macos-gui/138495)), and install `SKILL.md`.
- **Optional Rust Stack (`moli` + native `sessfork-mcp`, `--engine dual` / `moli`) & Local Studio (`--ui`)**: Keep `chrome-headless-shell` as default for 99.9% web compatibility, or pair [`lexmount/moli`](https://github.com/lexmount/moli) with the bundled **605 KB native Rust CDP MCP server** ([`rust/sessfork-mcp`](rust/sessfork-mcp)): talks straight over `moli serve --remote-debugging-pipe` with **zero Node.js, zero TCP ports, `4.6 ms` MCP cold start, `1.7 MB` idle RSS**, and kernel-level EOF cleanup on exit.

---

## Stress Benchmarks (`chrome-headless-shell` vs. `moli` + Node vs. `moli` + Rust `sessfork-mcp`)

![Single-Host AI Browser Ceiling: 56 Chrome vs 160 Moli Parallel Agents with Rust sessfork-mcp](docs/assets/benchmark-v022-en.png)

Measured locally on Apple Silicon (`macOS 26.6.2 arm64`, M5 24 GB, Python 3.14.7, `@playwright/mcp@0.0.85`, `moli 1.1.27`, `sessfork-mcp 0.1.4`) via [`scripts/stress_test.py`](scripts/stress_test.py) (zero external requests). Full methodology & 3-way breakdown in **[docs/benchmarks.md](docs/benchmarks.md)**.

| Workload | `chrome-headless-shell` + Node MCP | `moli 1.1.27` + Node MCP | **`moli 1.1.27` + Rust `sessfork-mcp`** | Delta vs. Chrome |
| :--- | :---: | :---: | :---: | :--- |
| **100-domain CLI extraction** *(2k cookies + 2k LS)* | `26.6 ms` p50 (`211k/s`) | same CLI core | same CLI core | Pure Python stdlib + CommonCrypto |
| **16-process concurrent fork storm** *(64 domains)* | **`0.0%` lost updates** (`223.7 ms`) | same CLI core | same CLI core | Fixed `57.5% -> 0.0%` via `fcntl.flock` |
| **MCP cold `initialize`** | `1,787.5 ms` | `1,229.5 ms` | **`4.6 ms`** *(1.7 MB idle)* | **`388×` faster** (zero Node.js / `npx`) |
| **50-origin hot-reload p50** *(20 cycles)* | `263.8 ms` | `672.5 ms` | **`5.9 ms`** (`20/20` OK) | **`44.7×` faster** (`114×` vs Node+Moli) |
| **6× lightweight auth time / total RSS** | `3,413 ms` / `1,219 MB` | `779 ms` / `383 MB` | **`230 ms` / `85 MB`** | **`14.8×` faster · `14.4×` less RAM (-93%)** |
| **12× heavy-DOM total RSS** *(1,775 nodes/tab)* | `2,531.4 MB` (`15` procs) | `656.8 MB` (`1` proc) | **`260.4 MB` (`1` proc)** | **`9.72×` smaller (`-89.7%`, saves `2.27 GB`)** |
| **12× heavy-DOM total time** *(full AX tree)* | `2,915.4 ms` | `5,543.9 ms` | **`1,501.0 ms`** (`12/12`, 0 leaks) | **`1.94×` faster** (`3.69×` vs Node+Moli) |

> **Independent verification by the `lexmount/moli` team (Apple M4, 24 GB, 5-run medians — [Discussion #3465](https://github.com/lexmount/moli/discussions/3465#discussioncomment-19846839)):** Re-running the exact same 12-context heavy-DOM benchmark (1 warm-up + 5 measured runs, all 12/12 checks passing) yielded **`4.22 s` / `226.3 MiB`** for `moli` + `sessfork-mcp` vs. **`25.41 s` / `575.6 MiB`** for `moli` + `@playwright/mcp` and **`11.65 s` / `2,439.5 MiB`** for `chrome-headless-shell` + `@playwright/mcp` — **`-90.7%` RAM (`10.78×` smaller) and `2.76×` faster than Chrome**.

> **Why `--engine dual` is the sweet spot:** Pure Rust `sessfork-moli` delivers **`9.72×`–`10.78×` smaller RAM**, **`1.94×`–`14.8×` faster execution**, and **`1.7 MB` idle** with zero Node.js, while Chrome stays completely unloaded (`0 MB`) until a WebGL or strict anti-bot portal triggers fallback.

```bash
# Optional: install the 605 KB prebuilt native Rust CDP MCP binary (SHA-256 verified, no Cargo needed)
curl --proto '=https' --tlsv1.2 -fsSL https://raw.githubusercontent.com/wasabihu/sessfork/v0.2.1/install.sh | bash -s -- --rust-mcp-only

# Or build from source (Rust >=1.75; auto-used by --engine moli / dual)
cargo install --git https://github.com/wasabihu/sessfork sessfork-mcp

# Reproduce the 3-way 12x heavy-DOM comparison locally (~18s)
python3 scripts/stress_test.py --heavy-compare
```

*(Want to use `sessfork-mcp` standalone with `moli` without Python? See [rust/sessfork-mcp/README.md](rust/sessfork-mcp/README.md).)*

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
| Wire OpenCode (`~/.config/opencode/opencode.json`) explicitly | `sessfork --setup --target opencode` |
| Wire WorkBuddy / Gemini CLI / Windsurf / Codex CLI explicitly | `sessfork --setup --target codex` *(or `workbuddy` / `gemini` / `windsurf`)* |
| Wire all 8 supported harnesses explicitly | `sessfork --setup --target all` |
| Open the local visual control panel (`127.0.0.1`, zero deps) | `sessfork --ui` |
| Switch headless engine (`chrome` default / `moli` Rust / `dual` fallback) | `sessfork --engine dual` *(or `chrome` / `moli`)* |
| Attach MCP to an existing external CDP server (`moli serve`) | `sessfork --setup --cdp-endpoint http://127.0.0.1:9222` |
| Switch back from external CDP to local `chrome-headless-shell` | `sessfork --setup --cdp-endpoint local` |
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
<summary><strong>What about sites that rotate single-use refresh tokens?</strong></summary>

`sessfork` creates a point-in-time snapshot (`storageState`), which works best for standard sliding-session cookies, read-mostly dashboards/research, and short-lived agent runs.

If a target site rotates **single-use refresh tokens** on every refresh (common on some OAuth SPAs and financial apps), your live Chrome tab and the forked headless context can invalidate each other's session whenever either side refreshes first. For those sites, signing into a dedicated isolated Chrome profile owned by the agent is the safer pattern; for everything else, `sessfork` avoids maintaining a second browser profile while keeping your active window untouched.

</details>

<details>
<summary><strong>Why does macOS ask for Keychain access when forking cookies?</strong></summary>

Chromium encrypts cookie values using a master passphrase stored under `"Chrome Safe Storage"` in your macOS Keychain. Click **Allow** so macOS authorizes `security` to read that entry. If a site uses `localStorage` tokens (many modern SPAs), pass `--no-cookies` to bypass Keychain completely.

By default `sessfork` does **not** store the derived decryption key anywhere, so macOS stays in charge of every authorization. If you prefer convenience, `--cache-key` saves the derived key to `~/.sessfork/keys.json` (`0600`). Trade-off: any process running under your user account could then read that file and decrypt your Chrome cookies without a Keychain prompt. Run `sessfork --purge-keys` to remove it at any time.

</details>

<details>
<summary><strong>Which platforms are supported?</strong></summary>

- **macOS (`arm64` / `x64`)**: fully supported and tested on real Chrome profiles, with prebuilt `sessfork-mcp` binaries.
- **Linux (`x64` / `arm64`)**: supported (in-memory OpenSSL `libcrypto` AES-128-CBC + Secret Service / `peanuts`, verified on Ubuntu CI, with prebuilt `sessfork-mcp` binaries for `x64` & `arm64`).
- **Windows (`x64`, zero Python / zero Node.js)**: natively supported via the standalone Rust `sessfork-mcp.exe` (`~784 KiB`, loopback RFC 6455 WebSocket CDP on kernel-assigned `--port 0` + Win32 Job Object zero-orphan reaping + `CREATE_NO_WINDOW`) paired with Windows [`moli.exe`](https://github.com/lexmount/moli) and the auditable bilingual [Companion Chrome/Edge Extension](extension/README.md). Instead of process injection or privilege escalation against Chrome 127+ App-Bound Encryption (`v20`), Chrome decrypts cookies itself upon explicit user click ("Fork This Site") and syncs over Native Messaging (`com.wasabihu.sessfork`). One-command install (auto-installs `moli.exe`, registers the fixed extension ID, wires detected AI clients, and copies the extension path to your clipboard):
  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://raw.githubusercontent.com/wasabihu/sessfork/main/install.ps1 | iex"
  ```
  - **Manual OpenCode config** (`%USERPROFILE%\.config\opencode\opencode.json` on Windows, `~/.config/opencode/opencode.json` on macOS/Linux — also auto-wired by `install.ps1` / `sessfork-mcp setup --mcp-file <path>`):
    ```json
    {
      "$schema": "https://opencode.ai/config.json",
      "mcp": {
        "sessfork-moli": {
          "type": "local",
          "command": ["sessfork-mcp"],
          "enabled": true
        }
      }
    }
    ```
  - **Hermes Agent (`~/.hermes/config.yaml`) & Codex CLI (`~/.codex/config.toml`)**:
    - **Codex CLI**: `codex mcp add sessfork-moli -- ~/.local/bin/sessfork-mcp`
    - **Hermes Agent**: add under `mcp_servers:` in `~/.hermes/config.yaml` and run `/reload-mcp` (or `hermes import-agent claude-code`):
      ```yaml
      mcp_servers:
        sessfork-moli:
          command: "sessfork-mcp"
      ```

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

<details>
<summary><strong>Why does <code>sessfork-browser</code> fail on macOS with <code>Target page, context or browser has been closed</code> / <code>Mach rendezvous failed</code>?</strong></summary>

`@playwright/mcp` defaults to system `/Applications/Google Chrome.app` in `--headless` mode. On macOS, system Chrome can crash mid-hydration with `Mach rendezvous failed` when `--isolated --storage-state=<state.json>` contains many LocalStorage origins, causing every MCP call to fail with `Target page, context or browser has been closed`.

`sessfork` automatically detects Playwright's `chrome-headless-shell` binary (highest `chromium_headless_shell-<rev>` for your CPU architecture) and pins `--executable-path=<chrome-headless-shell>` in your MCP config on macOS. If it is not installed yet (or your config was created by an older version), install it and re-wire MCP once, then reload `sessfork-browser`:

```bash
npx -y playwright-core install chromium-headless-shell
sessfork --setup
```

Check `sessfork --status` to confirm the detected binary and pinned config status. To opt out and use system Chrome (or pin a custom executable on any OS), set `SESSFORK_BROWSER_EXECUTABLE_PATH=system` (or `none`, or an executable path) before running `sessfork --setup`.

</details>

---

## Auth-to-XERJ Local Knowledge Ingest (`skills/xerj-auth-ingest`)

Need to silently capture authenticated Notion, Feishu, Confluence, or internal research pages into a local searchable knowledge base without touching your foreground Chrome window or leaking tokens?

- Read **[`skills/xerj-auth-ingest/SKILL.md`](skills/xerj-auth-ingest/SKILL.md)** and run the zero-dependency helper [`skills/xerj-auth-ingest/ingest_to_xerj.py`](skills/xerj-auth-ingest/ingest_to_xerj.py):
  - Converts captured HTML / Markdown / JSONL into clean UTF-8 Markdown with YAML frontmatter (`source_url`, `captured_at`, `title`, `domain`), stripping `<script>`/`<style>`/`<svg>`/boilerplate while preserving CJK text.
  - Scrubs accidental `Authorization: Bearer ...`, `ApiKey ...`, `Cookie: ...`, `hf_...`, `ghp_...`, `sk-...`, and JWT (`eyJ...`) secrets into `<REDACTED>` **before** writing Markdown.
  - Defaults to `--dry-run` and enforces loopback-only XERJ URLs (`127.0.0.1` / `::1` / `localhost`) plus path-traversal rejection; pass `--index` to run `xerj autoindex`.

### Verified XERJ Open Ecosystem

| Stage | Project / Model | Role in the Local-First AI Stack |
| :--- | :--- | :--- |
| **1. Capture** | **[`wasabihu/sessfork`](https://github.com/wasabihu/sessfork)** (`skills/xerj-auth-ingest/`, `examples/crawl4ai_auth_crawl.py`) | Zero-focus-theft Chrome auth fork (`sessfork-moli` / `sessfork-browser` / optional local [`Crawl4AI`](https://github.com/unclecode/crawl4ai) `fit_markdown` batch crawl) + secret-redacting HTML/Markdown/JSONL cleaner into local XERJ. |
| **2. Index & Neural Retrieval** | **[`xerj-org/xerj`](https://github.com/xerj-org/xerj)** + HF **[`wasabihu/xerj-bilingual-fin-law-384`](https://huggingface.co/wasabihu/xerj-bilingual-fin-law-384)** *(MIT)* & **[`wasabihu/VeriCorpus-Reranker-0.6B`](https://huggingface.co/wasabihu/VeriCorpus-Reranker-0.6B)** *(Apache-2.0)* | Single-binary Rust ES-compatible search engine (`~9.9 MB` idle RSS) paired with compact bilingual CJK/EN financial & legal embedding and reranker models. |
| **3. Read-Only Agent Firewall** | **[`wasabihu/kbwall`](https://github.com/wasabihu/kbwall)** | `~1 MB` air-gapped, loopback-only read-only Rust MCP firewall for XERJ with offline BMP CJK enhancement and `xerj://` evidence URIs. |
| **4. Citation & Corpus Verification** | **[`wasabihu/claimcite`](https://github.com/wasabihu/claimcite)** + **[`wasabihu/vericorpus`](https://github.com/wasabihu/vericorpus)** | Verifies verbatim quotes against DOIs/PMIDs and `xerj://` evidence URIs (`claimcite`), backed by audit-grade CJK/fin/law benchmarks (`vericorpus`). |

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
# Unit & multi-process concurrency tests
PYTHONPATH=src python3 -m unittest discover -s tests -v

# Reproducible 5-scenario local stress benchmark (SQLite WAL, 16-proc flock, live MCP hot-reload & 6x isolatedContext)
python3 scripts/stress_test.py
```

See [docs/benchmarks.md](docs/benchmarks.md) for measured macOS ARM64 results (100-domain extraction in `26.6 ms`, `0%` lost updates under 16-process concurrency, `20/20` 50-origin MCP hot reloads, and `0` cross-context leaks across 6 isolated contexts).

## License

[MIT](LICENSE)

<!-- mcp-name: io.github.wasabihu/sessfork -->
