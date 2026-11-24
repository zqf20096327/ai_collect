<div align="center">

<img src="Logo.png" alt="DPXJS Logo" width="130" />

# DPXJS

**Client-side JavaScript security analyzer for Firefox.**
Proven DOM XSS flows, leaked secrets and hidden endpoints.

<p>
  <img src="https://img.shields.io/badge/version-1.0.4-8b5cf6?style=for-the-badge" alt="version" />
  <img src="https://img.shields.io/badge/Firefox-115%2B-ff7a1a?style=for-the-badge&logo=firefoxbrowser&logoColor=white" alt="firefox" />
  <img src="https://img.shields.io/badge/Manifest-V3-6d28d9?style=for-the-badge" alt="mv3" />
  <img src="https://img.shields.io/badge/license-MIT-22c55e?style=for-the-badge" alt="license" />
</p>

<p>
  <a href="#-features">Features</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-how-it-works">How it works</a>
</p>

</div>

<p align="center">
  <img src="screen.png" alt="DPXJS screenshot" width="900" />
</p>

---

## 📖 About

DPXJS collects every script a page loads, parses it with a real **AST parser (Acorn)** and runs **taint analysis** from attacker-controlled **sources** to dangerous **sinks**. Only proven flows are reported, so the noise stays low.

> 🔒 Everything runs locally in your browser. Nothing leaves your machine unless you press an AI button.

---

## ✨ Features

| | Feature | Description |
|---|---|---|
| 🎯 | **Source → Sink** | DOM XSS, open redirect and prototype pollution flows. |
| 📨 | **postMessage** | Only real `window` message events. WebSocket, Worker and EventSource are ignored. |
| 🌐 | **Endpoints** | Full URL or path-only view, include/exclude regex, JSON export with the source JS file. |
| 🔑 | **Secrets** | AWS, GitHub, Stripe, Slack, JWT and more, with validation. |
| 🧰 | **Libraries** | Vulnerable jQuery, Lodash, AngularJS and others by version. |
| 🤖 | **AI triage** | Optional one-click verdicts via Numes. |
| 🔔 | **Update check** | A green banner appears when a new release is out. |

---

## 📦 Installation

Firefox **115+**.

1. Download the latest zip from [**Releases**](https://github.com/0xdexblood/DpxJS/releases) and extract it.
2. Open `about:debugging#/runtime/this-firefox`.
3. Click **Load Temporary Add-on...** and select `manifest.json`.
4. Pin the DPXJS icon to the toolbar.

> ⚠️ Temporary add-ons are removed on restart.

---

## 🚀 Usage

1. Open the page you want to audit and click the **DPXJS** icon.
2. Press **Scan** and browse the tabs: Findings, Endpoints, Secrets, Info.
3. Open the **Endpoints** tab, pick *Full URL* or *Path only*, add your own regex, then **Export endpoints JSON**.
4. Click a result to jump to the exact line in the viewer.

---

## 🧠 How it works

```
 Page ──► Script collector ──► Acorn AST ──► Taint engine ──► Verified findings
          (inline, external,    (regex for    sources → sinks    + secrets
           dynamic, HTML)        >1.5 MB)                        + endpoints
```

- **Sources:** `location.*`, `document.URL`, `document.referrer`, `window.name`, `postMessage` data
- **Sinks:** `innerHTML`, `outerHTML`, `document.write`, `eval`, `Function`, jQuery `.html()` / `$()`, navigation APIs

---

## 📜 License

Released under the [MIT License](LICENSE).

<div align="center">

**Built with 💜 by [0xdexblood](https://github.com/0xdexblood)**

If DPXJS helps you find a bug, consider leaving a ⭐

</div>
