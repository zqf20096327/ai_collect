<div align="center">

<img src="./docs/assets/logo.svg" width="82" height="82" alt="ColabHive 3-Cell Honeycomb Tensor Logo" />

# ColabHive

**Turn scattered Google Colab accounts into one self-hosted GPU cluster, 4× parallel shard runner, and headless MCP router — shipping as a Frameless System-Tray / Menu-Bar Desktop App and a Hardened Cloud Team Server.**

<p>
  <a href="https://hexwander.github.io/colabhive/"><b>🎮 Live Interactive Demo (No Install)</b></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/hexwander/colabhive/releases/latest"><b>🖥 Download Windows Tray &amp; macOS App</b></a>
  &nbsp;·&nbsp;
  <a href="#option-3--hardened-team-cloud-server-docker--auto-https"><b>☁️ Cloud Server Guide</b></a>
  &nbsp;·&nbsp;
  <a href="./README.zh-CN.md"><b>简体中文</b></a>
</p>

<p>
  <a href="https://github.com/hexwander/colabhive/releases/latest"><img src="https://img.shields.io/badge/release-v1.0.0-F59E0B?style=flat-square" alt="Release v1.0.0" /></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-10B981?style=flat-square" alt="Apache-2.0 License" /></a>
  <a href="./go.mod"><img src="https://img.shields.io/badge/Go-1.26_Static_Binary_(CGO__ENABLED%3D0)-0284C7?style=flat-square" alt="Go 1.26 Static Binary" /></a>
  <a href="#native-system-tray--menu-bar-experience"><img src="https://img.shields.io/badge/Desktop-Windows_Tray_%2B_macOS_Menu_Bar-18181B?style=flat-square" alt="Desktop Support" /></a>
  <a href="#connect-any-ai-coding-agent-in-1-click"><img src="https://img.shields.io/badge/MCP-Streamable_HTTP_%2B_SSE_%2B_stdio-2563EB?style=flat-square" alt="Tri-Protocol MCP" /></a>
  <a href="./README.zh-CN.md"><img src="https://img.shields.io/badge/i18n-English_%7C_简体中文-D97706?style=flat-square" alt="Bilingual UI" /></a>
</p>

<br />

<a href="https://hexwander.github.io/colabhive/">
  <img src="./docs/assets/hero-showcase.png" width="100%" alt="ColabHive Precision Compute Observatory and Native 4-Tab System Tray" />
</a>

<sub>
  Inspired by <a href="https://github.com/Wei-Shaw/sub2api"><code>Wei-Shaw/sub2api</code></a>, <a href="https://github.com/yetone/magpie"><code>yetone/magpie</code></a>, and <a href="https://github.com/farion1231/cc-switch"><code>farion1231/cc-switch</code></a> · 100% interoperable with Official Google Colab Dual-Backend APIs, <code>google-colab-cli</code>, and <code>colab-mcp</code>.
</sub>

</div>

---

## ⚡ 30-Second Quickstart

Choose your deployment mode — solo local desktop tray/daemon or shared multi-tenant lab server:

### Option 1 — Native Desktop & System Tray (Windows 1-Liner)

Installs `colabhive-desktop.exe` (frameless native window + Magpie 4-tab system tray), `colabhive.exe`, and drop-in `colab.exe` with SHA-256 verification:

```powershell
irm https://raw.githubusercontent.com/hexwander/colabhive/main/scripts/install.ps1 | iex
```

> Prefer manual download? Grab `colabhive_v1.0.0_windows_amd64.zip` directly from [**GitHub Releases**](https://github.com/hexwander/colabhive/releases/latest) and launch `colabhive-desktop.exe`.

### Option 2 — macOS (`ColabHive.app` Menu Bar + CLI) & Linux (1-Liner)

Detects Apple Silicon (`arm64`) / Intel (`amd64`) on macOS & Linux, verifies `SHA256SUMS.txt`, and installs the native `ColabHive.app` Menu Bar bundle (macOS) + `colabhive` & `colab` CLIs:

```bash
curl -fsSL https://raw.githubusercontent.com/hexwander/colabhive/main/scripts/install.sh | sh
```

### Option 3 — Hardened Team Cloud Server (Docker + Auto-HTTPS)

Deploys `colabhive serve --mode cloud --trust-proxy` with automatic Let's Encrypt TLS (`flush_interval -1`, `1800s` GPU allocation streaming timeouts, and mandatory `COLABHIVE_ADMIN_TOKEN` + `AES-256-GCM` vault protection):

```bash
cp .env.cloud.example .env.cloud && chmod 600 .env.cloud
# Set COLABHIVE_DOMAIN, COLABHIVE_PUBLIC_URL, COLABHIVE_ADMIN_TOKEN & COLABHIVE_MASTER_KEY in .env.cloud
docker compose -f docker-compose.cloud.yml --env-file .env.cloud --profile caddy up -d
```

---

## 🐝 Native System Tray & Menu Bar Experience

<table>
  <tr>
    <td width="58%" valign="middle">
      <h3>Always One Click Away — Zero Console Clutter</h3>
      <p>
        Modeled after <b>Magpie</b> and <b>cc-switch</b>, ColabHive runs as a native frameless desktop app on <b>Windows</b> (<code>colabhive-desktop.exe</code>, Win32 client-extended DWM chrome + system tray) and <b>macOS Apple Silicon &amp; Intel</b> (<code>ColabHive.app</code>, native traffic-light window + Menu Bar <code>NSPopover</code>). Closing the main window parks cleanly into your tray/menu bar without dropping live Jupyter GPU tunnels.
      </p>
      <ul>
        <li><b><code>额度 · Quota</code></b>: Pooled Compute Units converted into calibrated <b>G4 (96 GB)</b>, <b>H100</b>, and <b>A100</b> hours + per-account circular quota &amp; slot concurrency rings.</li>
        <li><b><code>Agent · 8 IDEs</code></b>: 1-click surgical config sync for <b>Claude Code</b>, <b>Codex</b>, <b>Antigravity</b>, <b>Cursor</b>, <b>Gemini CLI</b>, <b>Windsurf</b>, <b>OpenCode</b>, and <b>Claude Desktop</b> — keyless on localhost!</li>
        <li><b><code>实例 · Live GPUs</code></b>: Real-time VRAM &amp; SM% load bars, 1-click <b>Open in Colab Web</b> attached to the exact live kernel, and external notebook hijack protection.</li>
        <li><b><code>路由 · Live Traces</code></b>: Visual <code>[Caller] ── (🐝) ── [● Account · GPU]</code> pill flow, scrolling MCP JSON-RPC trace feed, and <b>Launch at Login</b>.</li>
      </ul>
      <p>
        👉 <a href="https://hexwander.github.io/colabhive/"><b>Click through the live 4-tab tray right in your browser →</b></a>
      </p>
    </td>
    <td width="42%" align="center" valign="middle">
      <img src="./docs/assets/tray-demo.gif" width="380" alt="ColabHive 4-Tab Native System Tray Animated Demo" />
    </td>
  </tr>
</table>

---

## 🎯 Architectural Highlights at a Glance

<p align="center">
  <img src="./docs/assets/bento-features.png" width="100%" alt="ColabHive 4-Card Feature Bento Grid" />
</p>

### Why Researchers & AI Agent Builders Switch to ColabHive

Most ML engineers and autonomous coding agents hold **multiple Google accounts** (`2,500 CU` AI Ultra, `500 CU` Pro+, `100 CU` Pro, Free tiers, or lab-mates with **expiring 90-day Compute Units**). Yet official Colab tools lock you into a single account, require an open Chrome tab, and silently burn paid CUs when a crashed Python subprocess enters a Linux zombie (`Z`) state:

| Capability | Browser Profile Juggling | Official `colab-cli` / `colab-mcp` | **🐝 ColabHive** |
| :--- | :---: | :---: | :--- |
| **Multi-Account Pooling** | Manual tab switching | ❌ Hardcoded `supportsMultipleAccounts: false` | ✅ **Unlimited accounts** with atomic slot reservation & `waste-zero` expiring-batch priority |
| **Quota Visibility** | Raw CU buried in menu | Single-account float (`ccu-info`) | ✅ **Live GPU-Hour Equivalence Matrix** (`G4 96GB` / `H100` / `A100` / `L4` / `T4` / `TPU v6e`) + Free refill timer |
| **Parallel GPU Sharding** | Copy-paste $K$ notebooks | ❌ Manual 1-by-1 execution | ✅ **1-Command $K$-Way Sharding** (`4 GPUs × 1h == 1 GPU × 4h` at **identical CU cost**, $4\times$ faster!) |
| **Teammate CU Sharing** | ❌ Never share passwords | ❌ Requires full local keyring | ✅ **30s Guest Auth Portal (`/contribute/:code`)** + **Zero Drive Scope** + **CU Reserve Floor** + **1-Click Revoke** |
| **MCP Agent Integration** | ❌ None | ⚠️ Requires Chrome tab, `1013 Server is busy` lock, `list_changed` tool-hiding bug | ✅ **100% Headless Tri-Protocol MCP** (`Streamable HTTP /mcp` + `SSE` + `stdio`), multi-agent concurrent |
| **Zombie & Drop Protection** | 15m idle tab disconnect | ⚠️ 35–60m ZMQ drop; Linux `Z` zombies fool `os.kill(pid, 0)` & bleed `9.66 CU/h` | ✅ **Reconnectable `8s` Keepalive + `/proc/{pid}/stat` Anti-Zombie Reaper + Deterministic `unassign`** |
| **Cross-Account Failover** | Manual click-retry | ❌ Exits code `1` | ✅ **2D Health FSM, Mid-Call Recovery & Waterfall Fallback** (`H100 ➔ G4 ➔ A100 ➔ L4 ➔ T4`) |
| **Egress IP Isolation** | OS-wide VPN collision | ❌ Shared host IP across accounts | ✅ **Per-Account Sticky `HTTP` / `SOCKS5` Proxy Pinning** across OAuth, `/tun/m` & Jupyter WebSockets |

---

## 🖥️ Interactive Visual Tour

### 1. 8-Client Headless MCP Router & 1-Click `cc-switch` Sync (`/router`)

Connect your entire local AI coding fleet in one click with timestamped backups (`~/.colabhive/backups/first-write/`) and cross-boundary **Windows + WSL2** path resolution, or inspect live sticky bindings and JSON-RPC tool traces in real time:

<p align="center">
  <img src="./docs/assets/screen-router.png" width="100%" alt="ColabHive Agent Router Topology and 1-Click Connect Drawer" />
</p>

### 2. 4× Blackwell `G4` Parallel Sharded Workbench & Hot-Cache Restart (`/exp`)

Run `4× NVIDIA RTX PRO 6000 Blackwell (96 GB GDDR7)` shards across 4 accounts simultaneously (`384 GB` aggregate VRAM), stream unified ANSI stdout/stderr, view out-of-band Matplotlib curves, and **hot-restart only the worker PID** while keeping `50–70 GB` of HuggingFace weights warm in `/root/.cache/huggingface`:

<p align="center">
  <img src="./docs/assets/screen-workbench.png" width="100%" alt="ColabHive 4x G4 Sharded Experiment Workbench and Live GPU Terminal" />
</p>

### 3. 30-Second Zero-Drive Contributor Portal (`/contribute/:code`)

Pool expiring 90-day CUs from lab-mates safely: requests **exclusively** `https://www.googleapis.com/auth/colaboratory` (physically zero Google Drive or Cloud Billing scopes), blocks in-kernel `google.colab.drive.mount` frames at the WebSocket proxy, enforces a hard `min_reserve_cu` personal floor, and issues a self-service 1-click revoke receipt:

<p align="center">
  <img src="./docs/assets/screen-contribute.png" width="100%" alt="ColabHive Zero-Drive Guest Contributor Portal" />
</p>

### 4. Hardened Cloud Team Server (`--mode cloud --trust-proxy`)

Deploy on any Linux VPS for 24×7 lab sharing: enforces `COLABHIVE_ADMIN_TOKEN` on the Web Observatory, hard-disables host filesystem endpoints (`403 Forbidden` on `scan-local` & config writes), mints scoped `ch_sk_live_...` agent keys with per-researcher CU budgets, and exposes public `/contribute/:code` portals cleanly behind Caddy or Nginx:

<p align="center">
  <img src="./docs/assets/screen-cloud-mode.png" width="100%" alt="ColabHive Cloud Server Mode and Admin Access Gate" />
</p>

---

## 📊 2026 Colab Accelerator Equivalence & Failover Matrix

ColabHive's EWMA calibration engine translates raw Compute Units into real remaining hardware hours across Google Colab's full accelerator lineup:

| Accelerator | Hardware & VRAM | CLI / SDK Flag | Reference Burn Rate | Ideal Workload |
| :--- | :--- | :---: | :---: | :--- |
| **`G4`** | **NVIDIA RTX PRO 6000 Blackwell · 96 GB GDDR7** (`SM 12.0`) | `--gpu G4` | **`~9.66 CU/hr`** | `27B–70B` BF16 evals (`48–85 GB` VRAM), long-context inference |
| **`H100`** | **NVIDIA H100 SXM5 · 80 GB HBM3** (`SM 9.0`) | `--gpu H100` | **`~12.50 CU/hr`** | Hopper FP8 / FlashAttention-3 dense pretraining & fine-tuning |
| **`A100`** | **NVIDIA A100 SXM4 · 40 / 80 GB** (`SM 8.0`) | `--gpu A100` | **`~8.88 CU/hr`** | Best throughput/CU for `<=14B` BF16 & prebuilt Triton kernels |
| **`L4`** | **NVIDIA L4 Ada · 24 GB GDDR6** (`SM 8.9`) | `--gpu L4` | **`~4.52 CU/hr`** | `7B–9B` inference, LoRA sweeps, multimodal pipelines |
| **`T4`** | **NVIDIA Tesla T4 · 16 GB GDDR6** (`SM 7.5`) | `--gpu T4` | **`~1.96 CU/hr`** *(0 Free)* | Quantized INT4/FP16 eval + opportunistic Free milli-CCU windows |
| **`TPU v6e / v5e`** | **Cloud TPU v6e-1 (32 GB) / v5e-1 (16 GB)** | `--tpu v6e1` | **`~5.30 / 3.85 CU/hr`** | High-efficiency JAX / XLA / PyTorch-XLA training |

<details>
<summary><b>🔀 View Cross-Account Error &amp; Preemption Auto-Failover Matrix</b></summary>

<br />

| Upstream Failure Condition | Official Tool Behavior | ColabHive Router & Watchdog Action |
| :--- | :--- | :--- |
| **`HTTP 400` Regional / Tier GPU Stockout** | Immediate crash | Marks `(account, accelerator)` in temporary cooldown; retries next eligible account or cascades `H100 ➔ G4 ➔ A100 ➔ L4 ➔ T4` |
| **`HTTP 412` Max Concurrent VMs Reached** | Immediate crash (`exit 1`) | Atomic in-flight slot reservation prevents stampedes; seamlessly routes overflow shards to next pooled account |
| **`HTTP 429` / `5xx` Control-Plane Throttle** | Fails tool call | Jittered backoff + instant horizontal failover to healthy account on isolated egress proxy |
| **OAuth `invalid_grant` / Expired Token** | Interactive browser prompt blocks | Quarantines degraded credential, emits alert badge, and re-routes live call without interrupting agent |
| **Mid-Execution VM Preemption / ZMQ Drop** | Loses state & hangs client | Reconnects ZMQ channel within `8s` window; if VM is gone, provisions replacement session transparently |
| **Subprocess Crashes into Linux Zombie (`Z`)** | `os.kill(pid, 0)` reports alive -> bleeds CUs | Parses field 3 of `/proc/{pid}/stat` every `8s`; aborts zombie shard and calls `/tun/m/unassign` deterministically |

</details>

---

## 🔌 Connect Any AI Coding Agent in 1 Click

In **Local Mode**, toggle any client directly in the System Tray **`Agent`** tab (`http://127.0.0.1:7860/mcp` runs keyless on loopback!). In **Cloud Mode**, authenticate with scoped `ch_sk_live_...` Bearer keys over HTTPS:

<details open>
<summary><b>Antigravity / Cursor / Windsurf / Claude Code (Streamable HTTP MCP)</b></summary>

**Local Desktop (Keyless Loopback):**
```json
{
  "mcpServers": {
    "colabhive": {
      "url": "http://127.0.0.1:7860/mcp"
    }
  }
}
```

**Cloud Team Server (Scoped `ch_sk_...` Agent Key):**
```json
{
  "mcpServers": {
    "colabhive": {
      "url": "https://hive.lab.example.com/mcp",
      "headers": {
        "Authorization": "Bearer ch_sk_live_xxxxxxxxxxxxxxxx"
      }
    }
  }
}
```
*(Claude Code CLI 1-liner: `claude mcp add --transport http colabhive https://hive.lab.example.com/mcp --header "Authorization: Bearer ch_sk_live_xxxxxxxxxxxxxxxx"`)*
</details>

<details>
<summary><b>OpenAI Codex (<code>~/.codex/config.toml</code>)</b></summary>

```toml
# Local Mode (keyless)
[mcp_servers.colabhive]
url = "http://127.0.0.1:7860/mcp"
tool_timeout_sec = 1800

# For Cloud Mode, replace url with https://hive.lab.example.com/mcp and add:
# http_headers = { Authorization = "Bearer ch_sk_live_xxxxxxxxxxxxxxxx" }
```
</details>

<details>
<summary><b>Gemini CLI (<code>~/.gemini/settings.json</code>)</b></summary>

```json
{
  "mcpServers": {
    "colabhive": {
      "httpUrl": "http://127.0.0.1:7860/mcp",
      "timeout": 1800000
    }
  }
}
```
</details>

<details>
<summary><b>Claude Desktop / Offline <code>stdio</code> Bridge</b></summary>

```json
{
  "mcpServers": {
    "colabhive": {
      "command": "/absolute/path/to/colabhive",
      "args": ["mcp", "stdio", "--strategy", "waste-zero"]
    }
  }
}
```
*(`colabhive mcp` automatically discovers your running desktop daemon via `~/.colabhive/daemon.json`.)*
</details>

---

## 🧰 Drop-In CLI & Zero-Dependency Python SDK

### Drop-In `colab` CLI & Parallel Sharded Sweeps

```bash
# View pooled Compute Units & calibrated GPU hours across all accounts
colabhive usage --gpu-hours

# 100% compatible `colab run` — pure script stdout, deterministic VM teardown on exit!
colab run --gpu G4 eval_single.py > predictions.jsonl

# Shard an evaluation across 4 pooled Colab accounts in parallel (4x wall-clock speedup, 1x CU cost!)
colabhive run --gpu G4 --shards 4 --strategy waste-zero --experiment qwen27b_eval eval_shard.py
```

### Python 3.10+ SDK (`colabhive-sdk`) & Teammate Donation CLI

Zero mandatory third-party packages (runs on pure Python stdlib, or `pip install "./sdk/python[httpx]"` for connection pooling):

```python
from colabhive import ColabHiveClient

client = ColabHiveClient(
    base_url="http://127.0.0.1:7860",  # or https://hive.lab.example.com + api_key="ch_sk_live_..."
)

# 1. Context-managed Blackwell G4 (96 GB) session — auto-unassigned on exit!
with client.session(gpu="G4") as sess:
    sess.upload("./config.yaml", "/content/config.yaml")
    res = sess.exec("import torch; print(torch.cuda.get_device_name(0))")
    print(res.stdout)

# 2. 4-way sharded sweep across 4 pooled accounts in parallel
exp = client.run_sharded("eval_shard.py", shards=4, gpu="G4", wait=True)
print(exp.experiment_id, exp.status)
```

```bash
# Teammate 1-command CU donation (locks 50 CU personal reserve floor, zero Google Drive scope)
colabhive-sdk donate https://hive.lab.example.com/contribute/ch_inv_8x92kP --reserve-cu 50
```

---

## 🏗️ System Architecture & Dual Security Boundaries

```mermaid
flowchart TB
    subgraph Clients["AI Coding Agents, Researchers & Contributors"]
        TRAY["Frameless Desktop + 4-Tab Tray / Menu Bar (Windows & macOS)"]
        AG["Antigravity · Cursor · Windsurf · Claude Desktop"]
        CC["Claude Code · Codex · Gemini CLI · OpenCode"]
        CLI["colabhive / colab CLI + Python SDK"]
        GUEST["External Contributors (/contribute/:code & colabhive-sdk donate)"]
    end

    subgraph Edge["Deployment Boundary (Local Loopback :7860 | Cloud Caddy / Nginx HTTPS)"]
        RPX["Optional Caddy / Nginx TLS Proxy<br/>flush_interval -1 · proxy_buffering off · 1800s GPU Timeout"]
    end

    subgraph Hive["ColabHive Control Plane (Static Pure-Go Binary)"]
        MCP["Unified MCP Server (Streamable HTTP /mcp + SSE + stdio)<br/>Static Tool Registry · Out-of-Band RichOutputs · External-VM Guard"]
        RTR["Smart Compute Router<br/>Atomic Slot Reservation · Waste-Zero · Sticky-Session · Cross-Account Failover"]
        WDG["Reliability & Safety Engine<br/>8s Anti-Zombie (/proc/stat) · Idle Reaper · CU Reserve Watchdog · Drive Firewall"]
        VLT["Pure-Go SQLite + AES-256-GCM Credential Vault (.chvault Portable)"]
    end

    subgraph Google["Official Google Colab Dual-Backend Infrastructure (Per-Account Proxy Isolated)"]
        PUB["Colab Public API<br/>colaboratory.googleapis.com/v1beta"]
        TUN["Colab Session Tunnel API<br/>colab.research.google.com/tun/m"]
        GAPI["Colab GAPI Quota Telemetry<br/>colab.pa.googleapis.com/v1/user-info"]
        VM["Colab GPU / TPU VMs<br/>Jupyter ZMQ-over-WS + /api/colab/resources"]
    end

    TRAY --> Hive
    AG & CC & CLI & GUEST --> RPX --> Hive
    MCP --> RTR
    RTR --> WDG & VLT
    WDG -->|"Pinned HTTP / SOCKS5 Proxy per Account"| PUB & TUN & GAPI & VM
```

| Security & Ops Dimension | 🖥️ **Local Desktop Mode (`colabhive-desktop` / `--mode local`)** | ☁️ **Cloud Team Server (`--mode cloud --trust-proxy`)** |
| :--- | :--- | :--- |
| **Desktop Shell** | Frameless Win32 (`-H=windowsgui`) System Tray + macOS (`ColabHive.app`) Menu Bar `NSPopover` | Non-root Alpine Docker container or headless static binary behind Caddy / Nginx |
| **Admin UI Auth** | Frictionless loopback `127.0.0.1:7860` (strict `Host` header guard; optional `--admin-token`) | **Mandatory `COLABHIVE_ADMIN_TOKEN`** + single-use 60s WebSocket tickets (`/api/v1/ws-ticket`) |
| **Agent MCP Auth** | **Keyless Localhost (`http://127.0.0.1:7860/mcp`)** + automatic `~/.colabhive/daemon.json` bridge | **Scoped `ch_sk_...` Keys** with account-group ACLs, daily/total CU caps, and email redaction |
| **Host Filesystem APIs** | Enabled: `scan-local` (`keyringrc.cfg` / WSL2) & surgical `cc-switch` config sync with backups | **Hard-Disabled (`403 Forbidden`)**: `scan-local`, host config writes, and desktop bridge locked off |
| **Vault Encryption** | Auto-managed DB-adjacent `.master.key` (`AES-256-GCM`) + `PBKDF2-SHA256` `.chvault` export | Strict explicit `COLABHIVE_MASTER_KEY` (`AES-256-GCM`) + zero `json` token serialization |

---

## 📚 Documentation & Build From Source

- **Build From Source**:
  - Windows (`pwsh`): `.\scripts\build-release.ps1` (compiles `web/dist`, `bin/colabhive.exe`, `bin/colab.exe`, and `bin/colabhive-desktop.exe`)
  - macOS / Linux (`bash`): `./scripts/build-release.sh` (compiles CLI binaries, `web/dist`, and macOS `ColabHive.app` bundle)
- **Deep-Dive Engineering Specs**:
  - [`docs/architecture/colab-protocol-spec.md`](./docs/architecture/colab-protocol-spec.md) — Colab Tunnel, OAuth2 PKCE, Keyring INI, Jupyter ZMQ WS & Anti-Zombie wire spec
  - [`docs/architecture/google-official-and-ccswitch-spec.md`](./docs/architecture/google-official-and-ccswitch-spec.md) — Official Dual-Backend (`v1beta` + `/tun/m`), `cc-switch` sync & Contributor Firewall spec
  - [`docs/architecture/product-ux-spec.md`](./docs/architecture/product-ux-spec.md) — Precision Compute Observatory UI/UX & bilingual design system
  - [`SECURITY.md`](./SECURITY.md) · [`CONTRIBUTING.md`](./CONTRIBUTING.md) · [`CHANGELOG.md`](./CHANGELOG.md)

---

## ⭐ Star History & Acknowledgments

## Roadmap (v1.1 & Ecosystem)

We welcome community PRs and plugin contributions! Planned milestones for **v1.1+**:

- [ ] **Local `/v1` OpenAI & Anthropic LLM Gateway over 96GB G4**: 1-click `vLLM` / `llama.cpp` / `Ollama` deployment inside pooled Colab VMs, reverse-proxied directly to `http://127.0.0.1:7860/v1/chat/completions` & `/v1/messages` (zero public tunnel exposure, automatic multi-account failover for Cursor, Claude Code, Magpie, Cherry Studio & Open WebUI).
- [ ] **1-Click Cloud GPU App Templates**: Curated launchpad for **ComfyUI** (Wan2.2 / HunyuanVideo / Flux workflows with Drive model symlinks), **Gradio Studio**, and **JupyterLab** with automatic keepalive, idle auto-shutdown, and link privacy masking.
- [ ] **Pluggable Multi-Cloud GPU Providers**: Optional provider adapters extending the Waste-Zero router to **Vast.ai**, **RunPod** (Jupyter/SSH spot pods), **Kaggle Notebooks** (30h/wk free dual-T4 batch shards), and **Modal** serverless GPUs.
- [ ] **Additional UI Locales**: Japanese (`日本語`), Traditional Chinese (`繁體中文`), and Korean (`한국어`) language packs.

---

Special thanks to [`googlecolab/google-colab-cli`](https://github.com/googlecolab/google-colab-cli), [`googlecolab/colab-vscode`](https://github.com/googlecolab/colab-vscode), [`googlecolab/colab-mcp`](https://github.com/googlecolab/colab-mcp), [`Wei-Shaw/sub2api`](https://github.com/Wei-Shaw/sub2api), [`yetone/magpie`](https://github.com/yetone/magpie), and [`farion1231/cc-switch`](https://github.com/farion1231/cc-switch) for inspiring ColabHive's protocol interoperability and craft.

<div align="center">
  <a href="https://star-history.com/#hexwander/colabhive&Date">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=hexwander/colabhive&type=Date&theme=dark" />
      <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=hexwander/colabhive&type=Date" />
      <img alt="ColabHive Star History Chart" src="https://api.star-history.com/svg?repos=hexwander/colabhive&type=Date" width="760" />
    </picture>
  </a>
</div>

## License

Licensed under the [Apache License 2.0](./LICENSE).
