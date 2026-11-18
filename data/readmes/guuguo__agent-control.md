[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [繁體中文](README.zh-TW.md)

<h1 align="center">Agent Control</h1>

<p align="center">
  <strong>Self-hosted desktop &amp; mobile remote control console for Codex, Claude Code, Antigravity, and Grok.</strong><br />
  Monitor live progress, approve tool permissions, track multi-account quotas, and queue follow-ups from any browser.
</p>

<p align="center">
  <a href="https://hub.guuguo.top/agent-control"><img src="https://img.shields.io/badge/Website-hub.guuguo.top-0ea5e9?style=flat-square" alt="Website" /></a>
  <img src="https://img.shields.io/badge/Node.js-22%2B-339933?style=flat-square&logo=node.js&logoColor=white" alt="Node.js 22+" />
  <img src="https://img.shields.io/badge/OS-macOS%20%7C%20Linux%20%7C%20Windows-64748b?style=flat-square" alt="OS" />
  <img src="https://img.shields.io/badge/UI%20Languages-EN%20%7C%20%E7%AE%80%20%7C%20%E7%B9%81%20%7C%20%E6%97%A5%20%7C%20%ED%95%9C-8b5cf6?style=flat-square" alt="5 UI Languages" />
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-AGPL--3.0-f59e0b?style=flat-square" alt="AGPL-3.0" /></a>
</p>

> **Supported Agents**: OpenAI Codex (multi-account quota separation) · Anthropic Claude Code · Google Antigravity · Grok  
> **Platforms**: macOS (with native `Agent Control.app` wrapper) · Linux · Windows (PowerShell)  
> **Architecture**: Read-only upstream indexing · Local HTTP/SSE server (`127.0.0.1:43310`) · Zero external database dependency  
> **Remote Access**: `$0` Cloudflare Quick Tunnel (default) · `$0` Tailscale Funnel · `$0` Named Tunnel · Self-hosted Docker / Sealos Relay

> [!IMPORTANT]
> **Security & Privacy Guarantee (Read Before Installing)**
> - **Strictly Read-Only Upstream Indexing**: Reads `~/.codex`, `~/.claude`, and `~/.gemini` histories in read-only mode. Custom titles, tags, and archives are stored separately in Agent Control's own data directory—your upstream databases and configs are **never** modified.
> - **Zero Cloud Prompt Storage**: Your code, prompts, and conversation histories never touch a third-party cloud database. Remote access routes directly through your chosen tunnel or self-hosted relay, protected by one-time pairing codes and HTTP-only session cookies.
> - **No Credential Scraping**: Multi-profile discovery only inspects explicit environment variables, public LaunchAgent paths, and display metadata (email/label)—never tokens or API keys.

---

## 🔄 Why Agent Control?

| Workflow | Multi-Engine Support | Multi-Account Codex Quotas | Setup Effort | Desktop Consolidation |
| --- | :---: | :---: | :---: | :---: |
| Multiple IDE / Terminal Windows | ❌ Separate apps | ❌ Guess by terminal | High memory usage | ❌ |
| Single-Engine Bot / Web Bridges | ❌ Usually Codex or Claude only | ❌ | Manual Tailscale / Bot setup | ❌ |
| **Agent Control** | ✅ **Codex + Claude + Antigravity + Grok** | ✅ **Auto-detected & labeled** | ✅ **One-line install, 5s QR** | ✅ **Lightweight native macOS app & web UI** |

---

## 📸 Screenshots

### 1. Desktop Console · Multi-Engine & Multi-Account Hub
Consolidate every running and historical session by project workspace, switch models/reasoning levels, and monitor per-account Codex quotas side by side.
<p align="center">
  <img src="docs/tutorial/01-desktop-console-en.png" alt="Agent Control Desktop Console" width="760" />
</p>

### 2. Mobile Browser · Live Monitor, Approvals & Queued Follow-Ups
Leave your desk without losing control—inspect code diffs, approve or deny tool calls, interrupt runaway turns, and queue your next prompt from your phone.
<table>
  <tr>
    <td align="center" width="50%"><strong>Project Board &amp; 4-Agent Live Status</strong></td>
    <td align="center" width="50%"><strong>Rich Markdown, Diffs &amp; Turn Queue</strong></td>
  </tr>
  <tr>
    <td align="center"><img src="docs/tutorial/05-mobile-paired-console.png" alt="Mobile Project Board" width="250" /></td>
    <td align="center"><img src="docs/tutorial/06-mobile-session-chat.png" alt="Mobile Session Chat" width="250" /></td>
  </tr>
</table>

<details>
<summary>Expand more features (Hands-Free Voice Copilot · QR Remote Tunnel · One-Click Auto-Update)</summary>

<table>
  <tr>
    <td align="center" width="33%"><strong>Hands-Free Voice Copilot</strong></td>
    <td align="center" width="33%"><strong>Zero-Config QR Tunnel</strong></td>
    <td align="center" width="33%"><strong>Version Check &amp; App Sync</strong></td>
  </tr>
  <tr>
    <td align="center"><img src="docs/tutorial/08-voice-copilot-modal.png" alt="Hands-Free Voice Copilot Modal" width="260" /></td>
    <td align="center"><img src="docs/tutorial/03-tunnel-qr-ready.png" alt="Mobile Remote Pairing and Tunnel Modal" width="260" /></td>
    <td align="center"><img src="docs/tutorial/09-update-modal.png" alt="Version Check and Auto-Update Modal" width="260" /></td>
  </tr>
</table>

</details>

---

## ⚡ 30-Second Quick Start

Requires **Node.js 22+** and **Git** (the installer prompts you if either is missing).

**macOS / Linux:**
```bash
curl -fsSL https://hub.guuguo.top/install/agent-control.sh | bash
```

**Windows (PowerShell):**
```powershell
(irm https://hub.guuguo.top/install/agent-control.ps1).TrimStart([char]0xFEFF) | iex
```

1. **Open**: Launches `http://127.0.0.1:43310` automatically (and installs **Agent Control.app** in `/Applications` on macOS).
2. **Switch UI Language**: Auto-detects browser language (`English`, `简体中文`, `繁體中文`, `日本語`, `한국어`), or switch anytime from the top-right **More** menu.
3. **Connect Your Phone**: Click **Remote** in the top bar to generate a QR code and pair instantly.

---

## 🌐 Remote Access Modes (Switch Anytime)

| Mode | Cost | URL Type | Best For | Highlights |
| --- | :---: | :---: | --- | --- |
| **Cloudflare Quick Tunnel (Default)** | **$0** | Temporary | Instant zero-config tryout | No account or server needed; QR ready in 5s |
| **Tailscale Funnel** | **$0** | **Permanent** (`*.ts.net`) | Daily personal mobile use | Free permanent HTTPS domain, one-click toggle |
| **Cloudflare Named Tunnel** | **$0** | **Permanent** (Custom domain) | Custom domain owners | Always-on system service on your domain |
| **Self-Hosted Docker / Sealos Relay** | Infra only | **Permanent** | Multi-device / firewalled hosts | Auto-reconnects on reboot; one-click deploy |
| **Local Only** | **$0** | — | Desktop consolidation only | No tunnel installed; switchable anytime |

👉 Full remote deployment & Docker/Sealos guide: [docs/remote-deploy.md](docs/remote-deploy.md)

---

## 📂 Project Structure & Local Development

- `src/server.mjs` — HTTP/SSE server (`127.0.0.1:43310`) and API routes
- `src/provider-hub.mjs` — Unified session aggregation, conflict-isolated approvals, turn queue, and `/goal` auto-continue controller
- `src/providers/` — Adapters & multi-profile discovery for Codex, Claude Code, Antigravity, and Grok
- `src/remote-bridge.mjs` & `relay/relay-server.mjs` — Outbound WebSocket tunnel & self-hosted public relay
- `public/` — Zero-build ESM web UI (`public/i18n.js` for 5-language support)
- `tests/` — Zero-token mock-CLI end-to-end test suite

```bash
npm run check
npm test
```

---

## 🗑️ Uninstall

**macOS / Linux:**
```bash
curl -fsSL https://hub.guuguo.top/uninstall/agent-control.sh | bash
```

**Windows (PowerShell):**
```powershell
(irm https://hub.guuguo.top/uninstall/agent-control.ps1).TrimStart([char]0xFEFF) | iex
```

---

## License

[AGPL-3.0-only](LICENSE)
