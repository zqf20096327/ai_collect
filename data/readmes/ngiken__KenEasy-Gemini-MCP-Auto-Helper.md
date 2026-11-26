<div align="center">
  <img src="assets/hero-banner.png" alt="KenEasy Gemini MCP Auto Helper" width="100%">

  <h1>KenEasy Gemini MCP Auto Helper</h1>

  <p>
    An intelligent automation extension tailored for <b>Google Gemini</b> web UI: featuring <b>Default Model Lock &amp; Responsive Auto-Switch Guard (auto-switches back on drift, hard error stop when unavailable)</b>, a clean <b>Notion-style UI (Paper Light &amp; Charcoal Dark)</b>, <b>per-chat independent toggles &amp; isolated emergency stop</b>, auto-approval of MCP tool permissions ("Always allow"), "Continue / Yes" follow-up chip clicking, <b>MAIN-world background/minimized/sleep click escalation, live MCP wait timer, stall auto-stop &amp; custom reconnect prompt (default: "继续，刚才mcp连接断开了"), one-click "Resume Now", human-like anti-throttling pacing, and a never-sleep MV3 background engine</b>, with <b>4 languages</b>, zero-glitch hold-to-drag HUD, desktop stall alerts, and a 6-layer circuit breaker.
  </p>

  <p>
    English · <a href="README.zh-CN.md">简体中文</a>
    ·
    <a href="CHANGELOG.md">Changelog</a>
    ·
    <a href="https://github.com/ngiken/KenEasy-Gemini-MCP-Auto-Helper/issues">Issues / Feedback</a>
  </p>

  <p>
    <img alt="Version" src="https://img.shields.io/badge/version-v2.2-16a34a?logo=googlechrome&logoColor=white">
    <img alt="Chrome Web Store" src="https://img.shields.io/badge/Chrome_Web_Store-Pending_Review-4285F4?logo=googlechrome&logoColor=white">
    <img alt="Manifest" src="https://img.shields.io/badge/manifest-v3-00aeec">
    <img alt="License" src="https://img.shields.io/badge/license-MIT-27c499">
  </p>
</div>

> [!NOTE]
> ### ✅ Stable Release (v2.2)
> **KenEasy Gemini MCP Auto Helper v2.2** is now officially released!
> Introducing **Default Model Lock &amp; Responsive Auto-Switch Guard** (auto-detects &amp; switches back to your preferred model across desktop, split-screen, narrow/mobile, high-zoom, and minimized/background windows — and halts with a clear `ERR` alert if the model is unavailable or keeps reverting), alongside Notion-style UI, per-chat independent toggles &amp; isolated emergency stop, MAIN-world background/sleep continuation, stall auto-resume, human-like pacing, 6-layer circuit breaker, 4-language support, and **129/129** passing automated &amp; E2E tests.
> - Customize your default model, reconnect prompt, or keywords anytime in the HUD or popup settings, or report Gemini UI updates on [GitHub Issues](https://github.com/ngiken/KenEasy-Gemini-MCP-Auto-Helper/issues).
> - Star 🌟 and PR contributions are warmly welcomed!

---

## 🚀 Installation

### Option 1: Chrome Web Store (Pending Review)

The extension has been submitted for Chrome Web Store security review. Once approved, you can install and receive silent auto-updates with one click:

👉 **[Get KenEasy Gemini MCP Auto Helper on Chrome Web Store (Coming Soon)](https://chromewebstore.google.com/)**

### Option 2: Manual Installation (Developer Mode - One-Click Direct Download)

Click either link below to **immediately download the `.zip` package with one click**:

- 📦 **[Direct Download: Manual Install Bundle (`KenEasy-Gemini-MCP-Auto-Helper-v2.2-manual-install.zip`)](https://github.com/ngiken/KenEasy-Gemini-MCP-Auto-Helper/releases/download/v2.2/KenEasy-Gemini-MCP-Auto-Helper-v2.2-manual-install.zip)** (Recommended — extracts to `KenEasy-Gemini-MCP-Auto-Helper/` folder with docs)
- 🏪 **[Direct Download: Clean Extension Zip (`KenEasy-Gemini-MCP-Auto-Helper-v2.2-store.zip`)](https://github.com/ngiken/KenEasy-Gemini-MCP-Auto-Helper/releases/download/v2.2/KenEasy-Gemini-MCP-Auto-Helper-v2.2-store.zip)** (Clean root containing `manifest.json`)

Installation steps:
1. Click a link above to download the `.zip` file and extract it to a local folder (e.g. `E:\code\KenEasy-Gemini-MCP-Auto-Helper`).
2. Open Google Chrome or Microsoft Edge and navigate to:
   - **Chrome**: `chrome://extensions/`
   - **Edge**: `edge://extensions/`
3. Enable the **Developer mode** toggle in the top-right corner.
4. Click the **Load unpacked** button in the top-left toolbar.
5. In the folder picker dialog, select the extracted folder containing `manifest.json`.
6. Open or refresh Google Gemini (`gemini.google.com`). You will see the floating HUD on the page, and clicking the extension toolbar icon opens the full configuration panel.

---

## 🎬 Core Features Walkthrough & Demos (Latest Highlights)

### 0. Default Model Lock & Responsive Auto-Switch Guard (v2.2 🆕)
> Set your preferred working model once (e.g., `Pro`, `Thinking`, `Fast`, `2.5 Pro`, or any custom model name) — the extension continuously verifies Gemini's active model across **desktop wide screens, split-screen windows, narrow/mobile bottom sheets, high zoom levels, and minimized/background tabs**.
>
> - **Automatic Drift Recovery**: Automatically selects your default model on fresh `/app` chats, before clicking **Continue**, and before **Stall Auto-Recovery** sends its reconnect prompt — without ever interrupting active streaming or MCP tool calls.
> - **Cross-Language & Anti-Collision Matching**: Understands localized labels (`Fast` / `快速` / `高速`, `Thinking` / `思考` / `思考モード`, `Gemini 2.5 Pro` ↔ `2.5 Pro`), ignores upsell banners (`Upgrade to Google AI Pro`), and prevents cross-tier collisions (target `Pro` never clicks `Thinking with 3 Pro`).
> - **Hard Error Stop When Unavailable**: If the preferred model is disabled/quota-locked, missing from the picker, rejected by an error banner, or repeatedly reverted by Gemini beyond your retry cap (default 3), automation halts cleanly (`model_unavailable`), shows a red `ERR` badge on the extension icon, and sends a localized OS desktop notification so you never waste turns on the wrong model.
> - **One-Click Controls Everywhere**: Configure, auto-detect available models, or snap to the active page model directly from the collapsible **HUD Model Panel** or the **Extension Popup**, with independent per-chat on/off overrides.

### 1. Notion-Style UI Refactor & Per-Chat Independent Controls / Isolated Emergency Stop
> Both the Floating HUD and Extension Popup have been completely redesigned around Notion's calm, flat aesthetic: **Paper Light (`#FFFFFF / #F7F6F3`, `#37352F` ink)** and **Charcoal Dark (`#191919 / #202020`, `#E6E6E4` text)** palettes, 1px hairline borders, subtle hover fills, and low-saturation semantic tones with zero neon glows.

<div align="center">
  <img src="assets/notion-ui-preview.png" alt="Notion-Style Light and Dark Popup and Floating HUD Preview" width="100%">
</div>

#### 🎛️ How to Use Per-Chat Controls & Isolated Emergency Stop
Every Gemini conversation (automatically keyed by URL: `/app/<id>`, `/u/<n>/app/<id>`, `/gem/<gemId>/<chatId>`) can be configured independently without affecting global defaults or other open tabs:

1. **Directly in the Floating HUD**:
   - Use the segmented **`This chat / Global`** switcher at the top of the HUD (`This chat` is selected by default).
   - While in `This chat` scope, toggling any of the 6 core switches (**Extension, Auto Always Allow, Auto Continue, Background Run, Desktop Alert, Stall Auto-Resume**) applies **only to the current conversation** and displays a subtle blue dot next to customized rows. Switch to **`Global`** anytime to inspect or edit global defaults.
   - Whenever a chat has custom overrides, a one-click **`Reset`** button appears on the right to revert back to global defaults.
   - Any per-chat override set on the fresh `/app` landing page automatically migrates to `/app/<newId>` as soon as the new conversation URL is created.
2. **In the Extension Popup**:
   - A dedicated top **`This Conversation`** card shows the active Gemini tab's conversation ID, override status (`Following global` / `Custom for this chat`), 6 per-chat checkboxes, a **`Stop this chat / Resume chat`** toggle, and a **`Reset`** button.
   - The bottom quick-action bar cleanly separates **`E-Stop`** (stops **only the active conversation**) from **`Stop All Chats`** (broadcasts emergency stop to all open Gemini tabs).
3. **Isolated Emergency Stop Behavior**:
   - Triggering Emergency Stop in Chat A halts all auto-allow, auto-continue, and stall-recovery actions for Chat A only — **Chat B and other open tabs continue running uninterrupted**.
   - Navigating away and returning to Chat A automatically restores its emergency-stopped state until you click **`Reset Trip / Resume chat`** or **`Reset`**.
4. **Hardened Background & Minimized Clicking**:
   - Even when global Background Run is off, enabling it on a single conversation keeps Service Worker heartbeats and `autoDiscardable: false` active exclusively for that chat without leaking to other tabs.
   - When Chromium throttles isolated-world clicks in hidden or minimized tabs, the engine escalates to **`MAIN`-world click execution** (`mainWorldClickByToken`, piercing ShadowRoots and Angular Material chips) across Allow retries, Continue retries, and Stall-Recovery Stop/Send buttons, backed by an extra `1200ms` follow-up wake tick on window minimize (`windowId === -1`).

### 1. Live MCP Wait Timer, Stall Auto-Stop & One-Click Resume + Human Pacing
> Tracks how long Gemini or an MCP server (such as Desktop Commander) has been connecting/waiting directly in the floating HUD and Popup. If a turn stalls past your threshold (default 5 minutes), the extension automatically cancels the stuck turn and sends your customizable reconnect prompt (default: `"继续，刚才mcp连接断开了"`), with draft protection, per-task recovery caps, an immediate **"Resume Now"** button, and **human-like anti-throttling pacing** (natural delays, chunked typing, and a 60s anti-burst governor).

### 2. Never-Sleep MV3 Background Engine & Smart Click Retry
> Keep Gemini running uninterrupted while minimized, on background tabs, or when working in other apps. A ~19.5s Service Worker keepalive prevents MV3 30-second idle suspension, proactive 4-minute Port rotation avoids Chrome's 5-minute forced disconnect, unthrottled Service Worker delayed ticks (`GMAH_SCHEDULE_TICK`) complete settling and cooldown waits on time, and failed background clicks automatically escalate to `MAIN`-world execution with Shadow DOM & chip piercing.

### 3. Zero-Glitch Hold-to-Drag Floating HUD
> Left-click and hold the HUD header to drag it smoothly anywhere across the Gemini viewport — simply hovering near the header never moves or traps the HUD! Ignores Windows minimize (`0x0` resize) so coordinates never snap to `(0, 0)`, auto-clamps inside the viewport when expanding or opening Logs/Inspect panels, and supports one-click position reset in the popup.

<div align="center">
  <img src="assets/hud-drag-demo.png" alt="Hold-to-Drag Floating HUD Demo" width="100%">
</div>

### 4. One-Click Desktop Notification & Anti-Stall Alert
> If an MCP tool execution hangs or model output stalls longer than the configured threshold (default 5 minutes), the extension triggers a localized OS desktop notification and flags a red `!` badge on the toolbar icon. Easily mute or enable with a single click directly from the on-page HUD or the popup. Clicking the notification instantly brings the Gemini tab and window back to the foreground.

<div align="center">
  <img src="assets/notification-toggle-demo.png" alt="One-Click Desktop Notification Demo" width="100%">
</div>

### 5. Dark & Light Dual Themes + 4-Language Control Center (Auto-Save)
> Switch effortlessly between **Dark Charcoal** and **Paper Light** themes (`🌙 / ☀️`) and across **4 languages (Simplified Chinese, Traditional Chinese, English, and Japanese)** in real time from either the popup or HUD. Numeric inputs and custom keywords auto-save immediately and push live settings to open Gemini tabs to reconcile tripped breakers instantly.

<div align="center">
  <img src="assets/popup-demo.png" alt="Extension Popup Overview" width="100%">
</div>

---

## ⚡ Capability Matrix

| Category | Feature | Technical Breakdown |
| :--- | :--- | :--- |
| **Default Model Lock** 🆕 | Auto-Switch & Hard Error Stop | Locks your preferred working model globally or per chat across `<header>`, composer bar, Shadow DOM, narrow mobile bottom sheets, high zoom (`visualViewport`), and background/minimized tabs; halts with red `ERR` badge & OS alert if unavailable or repeatedly reverted. |
| **Notion-Style UI** | Paper Light & Charcoal Dark | Flat Notion-inspired aesthetic across HUD & Popup with 1px hairline borders, subtle hover states, active drawer highlights, Clear/Refresh toolbars, responsive compact `@media` rules, and strict zero-`innerHTML` Trusted Types CSP compliance. |
| **Per-Chat Controls** | Scoped Overrides & Migration | Independently toggle 7 core switches (including Model Lock) per conversation via the HUD (`This chat / Global` bar) or Popup (`This Conversation` card), with blue override markers, one-click `Reset`, and `/app` → `/app/<id>` migration. |
| **Isolated E-Stop** 🆕 | Single-Chat vs. All-Chats | **E-Stop** / **Stop this chat** halts only the current conversation and persists across navigation while other chats keep running; **Stop All Chats** broadcasts emergency stop to all Gemini tabs on demand. |
| **Background Engine** 🆕 | MAIN-World Escalation & Keepalive | Combines ~19.5s MV3 SW keepalive, 4-min Port rotation, unthrottled SW ticks, `1200ms` minimize follow-up wakeups, per-chat `autoDiscardable: false` isolation, and `MAIN`-world Shadow DOM / chip click escalation. |
| **MCP Auto-Approval** | Always Allow Priority | Prefers and auto-clicks `Always allow` (and localized equivalents), penetrating Material Web Components `<slot>` projections, split inline `<span>` labels, and `role="menu"` / `role="menuitem"` dropdowns. |
| **Single Allow Fallback** | Safe Single Click | Optional fallback to click `Allow once` when no permanent option exists, strictly guarded by sibling context checks and 4-language cookie/notification/camera/mic/location exclusions. |
| **Smart Continuity** | Follow-up Chip Click | Detects and triggers explicit affirmative `↪ Yes` follow-up chips and "Continue" buttons, strictly ignoring general suggestions, surveys, and chat history. |
| **Hold-to-Drag HUD** | Zero-Glitch Positioning | Left-button press guard eliminates hover-sticking; ignores Windows minimize `0x0` resize events; auto-clamps on expand/panel open; includes popup **Reset HUD** button. |
| **4 Languages & Themes** | 4 Locales + Dark/Light | Live UI, engine status, notifications, and keyword matching across Simplified Chinese, Traditional Chinese, English, and Japanese, with synchronized Charcoal Dark / Paper Light themes. |
| **Multi-Window & Route Guard** | Zero Accidental Clicks | Skips non-chat routes (`/gems`, `/extensions`, `/settings`), 0-turn screens, and stale history chips on restored tabs in secondary windows, while allowing first continues on newly created `/app` → `/app/<id>` chats. |
| **Desktop Notifications** | One-Click Anti-Stall Alert | Issues localized desktop notifications when MCP execution exceeds the stall threshold (1–60 mins); togglable instantly from either the HUD or the popup. |
| **6-Layer Circuit Breaker** | Anti-Loop Quota Guard | Enforces per-task limits, daily limits, streaming stabilization settle time, operation cooldown, completion cues, and stagnant output detection. |
| **Custom Keywords** | Auto-Saved Rule Lists | Extend built-in dictionaries with comma- or newline-separated custom phrases that auto-save and sync live to open Gemini tabs. |

---

## 🛡️ 6-Layer Anti-Loop Circuit Breaker Architecture

To safeguard your API quotas and tokens against runaway recursive loops, the extension implements a comprehensive multi-tier circuit breaker:

```text
               ┌────────────────────────────────────────────────────────┐
               │           Gemini Output & DOM Mutation Stream          │
               └──────────────────────────┬─────────────────────────────┘
                                          │
                  ▼ Layer A: Quota & Error Breaker (Immediate Trip)
          [ "Reached your limit" / "Quota exceeded" / "Try again later" ] ──► 🚨 Hard Stop
                                          │
                  ▼ Layer B: Streaming Settle Guard (Wait for Completion)
               [ Observe DOM until stable with no cursor for >= 1.8s ]
                                          │
                  ▼ Layer C: Operation Cooldown Guard (Rate Limiting)
              [ Force minimum 4.0s delay after every "Continue" action ]
                                          │
                  ▼ Layer D: Per-Task Continue Limit (Single Prompt Guard)
               [ Max continues reached (default 10) ] ──► 🛑 Per-Task Trip
                                          │
                  ▼ Layer E: Daily Continue Cap (All-Day Safety Net)
               [ Daily cap reached (default 0=unlimited) ] ──► 🛑 Daily Trip
                                          │
                  ▼ Layer F: Completion Cue & Smart Pass-Through
            [ "Task completed" found & no explicit ↪ Yes chip ] ──► ⏹️ Skip Action
                                          │
                  ▼ Layer G: Stagnant Output & Repetition Detection
           [ Output DOM unchanged or identical text across turns ] ──► ⚠️ Stagnant Trip
```

1. **Layer A · Quota & Error Cutoff**: Instantly halts all automated actions when Gemini outputs error phrases such as `reached your limit`, `quota exceeded`, `please try again later`, or system service errors.
2. **Layer B · Streaming Settle Guard (default 1.8s)**: Observes streaming output to verify the blinking cursor is gone and no DOM updates have occurred for at least 1.8 seconds before taking any action.
3. **Layer C · Operation Cooldown (default 4.0s)**: Enforces an intentional pause between consecutive clicks to prevent double-click race conditions.
4. **Layer D · Per-Task Limit (default 10)**: Limits continues per conversation turn; automatically resets to 0 whenever the user sends a new prompt.
5. **Layer E · Daily Continue Cap (default 0 = unlimited)**: Caps total automated continues per calendar day, automatically resetting at midnight (00:00).
6. **Layer F · Completion Cue Detection**: Skips auto-continue when Gemini outputs definitive completion phrases like "All tasks finished", while smartly continuing if Gemini explicitly displays a `↪ Yes` follow-up chip.
7. **Layer G · Stagnant Output Fingerprinting**: Trips when consecutive actions produce zero new content or generate identical response hashes, preventing repetitive bot loops.

---

## 🏗️ Architecture & Decoupled Modules

The extension follows clean separation of concerns and data-driven principles:

```text
manifest.json
  Manifest V3 declaration specifying minimal permissions (storage, tabs, alarms, scripting, notifications) and Gemini matching rules.

defaults.js
  Shared configuration hub: built-in keyword dictionaries, default options, schema migration, and boundary clamping.

hud.js & hud.css
  In-page floating HUD component: pointer drag handling, boundary clamping, live state pills, and quick notification toggle.

content.js
  Runs in the isolated content script world: DOM observers, button matching heuristics, circuit breakers, and microtask dispatchers.

background.js
  Persistent Service Worker: manages long-lived ports, heartbeat alarms, tab discard prevention, and OS desktop notifications.

popup.js, popup.html, popup.css
  Extension popup control center: real-time metrics, interactive switches, custom keywords textarea, and emergency controls.
```

---

## ❓ Frequently Asked Questions (FAQ)

<details>
<summary><b>Q1: Why is the floating HUD not appearing on the Gemini page?</b></summary>

1. Confirm that your browser is on a page matching `gemini.google.com`.
2. Click the extension toolbar icon and ensure that the Master Switch and "Show floating HUD" options are enabled.
3. If the HUD was previously dragged to an edge or off-screen, click the **"Reset HUD"** button in the popup to snap it back to the default bottom-right position.
</details>

<details>
<summary><b>Q2: Does the draggable HUD remember its position after refreshing the page?</b></summary>

Yes. When you release the HUD after dragging, its `(left, top)` coordinates are immediately saved to `chrome.storage.local` and `localStorage` (`gmah_hud_position`). It restores cleanly across page reloads, new chat sessions, and browser minimize/restore cycles.
</details>

<details>
<summary><b>Q3: Why did I not receive a desktop notification when execution stalled?</b></summary>

1. Open the popup and click the **"Test Notification"** button to confirm that your browser and operating system have notification permissions enabled.
2. Check if Windows "Focus Assist" or macOS "Do Not Disturb" is active.
3. Verify that the "Desktop Notification" pill in the HUD or the toggle in the popup is turned on.
</details>

<details>
<summary><b>Q4: Will the extension accidentally click "Delete Chat" or "Deny"?</b></summary>

No. The engine applies an explicit exclusion blacklist (blocking terms like delete, remove, deny, cancel, dismiss, survey) combined with strict sibling hierarchy and container verification.
</details>

<details>
<summary><b>Q5: How do I disable features or emergency stop only one conversation without affecting other chats?</b></summary>

1. In that chat's floating HUD, keep the top switcher on **`This chat`** (default) and toggle individual switches or click **`E-Stop`** — changes apply only to that conversation.
2. Or open the extension Popup and use the top **`This Conversation`** card to toggle features or click **`Stop this chat`**; all other Gemini tabs keep running normally.
3. To halt every open Gemini tab at once, click **`Stop All Chats`** near the bottom of the popup. Click **`Reset`** anytime to return the current chat to global defaults.
</details>

<details>
<summary><b>Q6: How do I restore default settings?</b></summary>

Click the **"Restore Defaults"** button at the bottom of the extension popup. This resets all thresholds, cooldowns, and keyword sets to safe official defaults.
</details>

<details>
<summary><b>Q7: How does Default Model Lock work if my preferred model hits its quota or becomes unavailable?</b></summary>

1. Open the HUD **Model Lock** picker (or the **Default Model Lock** card in Popup), click **"Use Current"** or pick/enter your target model (e.g., `Pro`, `Thinking`, `2.5 Pro`), and enable **Model Lock**.
2. Whenever Gemini drifts or resets to another model, the extension automatically switches back before continuing.
3. If the target model is disabled/locked, missing, rejected by a quota banner, or keeps getting reverted beyond your configured retry limit (default 3), the extension triggers a hard `model_unavailable` stop, flags a red **`ERR`** badge, and sends a desktop notification so you can switch models or reset cleanly.
</details>

---

## 📝 Changelog

### [v2.2](https://github.com/ngiken/KenEasy-Gemini-MCP-Auto-Helper/releases/tag/v2.2) - 2026-11-24
- **Default Model Lock & Responsive Auto-Switch Guard**: Added global & per-chat model locking (`modelLockEnabled`, `preferredModel`, `maxModelSwitchRetries`, `stopOnModelUnavailable`) with HUD collapsible model panel, Popup quick-pick chips, one-click **Use Current / Detect Models / Switch Now**, and pre-continue + pre-stall-recovery verification.
- **Full Multi-Size, Zoom & Background Compatibility**: Works seamlessly across desktop `<header>`, bottom composer, Shadow DOM, narrow mobile icon-only triggers + `mat-bottom-sheet-container`, duplicate responsive triggers, high zoom (`visualViewport` + scrollable HUD), and minimized/background tabs with double-toggle prevention in `MAIN`-world clicks.
- **Hard Error Stop & Anti-Flap Protection**: Detects disabled/quota-locked options, missing models, error snackbars, and repeated Gemini model reverts; cleanly closes menus, trips `model_unavailable` (halting all automation), sets a red `ERR` icon badge, and dispatches a localized OS desktop alert — verified at **129/129 passing tests**.

### [v2.0](https://github.com/ngiken/KenEasy-Gemini-MCP-Auto-Helper/releases/tag/v2.0) - 2026-11-24
- **Background, Minimized & Screen-Off / Sleep Continuity Overhaul**: Expanded `isBackgroundOrUnfocused` detection for minimized, occluded, and off-screen windows; added immediate `MAIN`-world click escalation (`triggerMainWorldClick`) on initial clicks for both `Always allow` and `Continue` chips alongside retries and stall-recovery send flows.
- **Post-Sleep & Visibility Wakeup Recovery**: Automatically re-acquires the shared background keepalive Web Lock (`syncBackgroundKeepaliveLock`), rotates/reconnects the Service Worker port (`forceReconnectBackgroundPort`), and triggers an immediate scan upon returning from hidden, screen-off, or sleep states (**116/116 passing tests**).

### [v1.0.1](https://github.com/ngiken/KenEasy-Gemini-MCP-Auto-Helper/releases/tag/v1.0.1) - 2026-11-24
- **Notion-Style UI Complete Refactor**: Rebuilt HUD and Popup stylesheets with Paper Light (`#FFFFFF / #F7F6F3`) & Charcoal Dark (`#191919 / #202020`) palettes, 1px hairline borders, active drawer highlights, Clear/Refresh toolbars, and real-DOM 2x headless Chrome previews (`assets/notion-ui-preview.png`).
- **Per-Chat Independent Controls & Isolated Emergency Stop**: Added URL-keyed `gmah_chat_overrides_v1` overrides, HUD **`This chat / Global`** segmented switcher, Popup **`This Conversation`** card, single-chat **`E-Stop`** isolated across SPA navigation, **`Stop All Chats`** broadcast action, `/app` → `/app/<id>` override migration, and one-click **`Reset`**.
- **Background / Minimized Clicking & Deep Boundary Hardening**: Added `MAIN`-world click escalation (`mainWorldClickByToken`, piercing ShadowRoots & `<mat-chip>`), per-chat background heartbeat & `autoDiscardable` isolation, `1200ms` minimize follow-up wakeups, and 27 deep boundary/fuzz guards (**115/115 passing tests**).

### [v1.0.0 (Official Release)](https://github.com/ngiken/KenEasy-Gemini-MCP-Auto-Helper/releases/tag/v1.0.0) - 2026-11-23
- **Stall Auto-Stop & Custom Reconnect Prompt**: Automatically cancels stuck MCP/Gemini turns past the configured timeout (default 5 min) and sends a customizable reconnect prompt (default `继续，刚才mcp连接断开了`) with draft protection and per-task recovery cap.
- **Live Wait Timer & One-Click Immediate Resume**: Real-time connecting/wait elapsed timer in HUD & Popup plus a one-click **"Resume Now"** button to recover immediately without waiting.
- **Human-Like Anti-Throttling Pacing**: Randomized post-stop/pre-send pauses, chunked typing, natural hover + off-center click jitter, and a 60s rolling anti-burst governor.
- **Circuit Breaker Desktop Alerts & Background Hardening**: Wired end-to-end circuit breaker badge/desktop notifications across `content.js` and `background.js`, added Web Lock anti-freeze shield, fast 8s zombie-port recovery, and expanded automated verification to **76/76 passing tests**.

### [v0.3.0 (v0.3 Beta)](https://github.com/ngiken/KenEasy-Gemini-MCP-Auto-Helper/releases/tag/v0.3.0) - 2026-11-22
- **Never-Sleep MV3 Background Engine**: Added ~19.5s Service Worker keepalive, proactive 4-minute Port rotation before Chrome's 5-minute disconnect limit, unthrottled SW delayed settling/cooldown ticks (`GMAH_SCHEDULE_TICK`), and instant tab/window focus wakeups so automation never stalls in background or other apps.
- **Smart Background Click Retry & Shadow DOM Observer**: Auto-retries un-dismissed clicks in background with `@material/web` ShadowRoot inner `<button>` piercing and safe focus/coords; recursively observes dynamic ShadowRoots; fixes minimized-window hidden spinners falsely locking `isGenerating`.
- **Zero-Glitch HUD, Popup & Safety Hardening**: Stops Windows minimize (`0x0` resize) from snapping the HUD to `(0, 0)`, auto-clamps on expand/panel open, fixes `/app` -> `/app/<id>` new-chat continue suppression, guards cookies/notifications/camera/mic/location across all 4 locales, adds live 4-language engine status, and auto-saves popup fields with instant breaker reconciliation.
- **64/64 Automated, E2E Sandbox & 30-Min Marathon Tests**: Verified end-to-end across 5 test suites including a 30-minute hidden background marathon with 7+ port rotations and simulated SW crash recovery.

### [v0.2.0 (v0.2 Beta)](https://github.com/ngiken/KenEasy-Gemini-MCP-Auto-Helper/releases/tag/v0.2.0) - 2026-11-22
- **Hold-to-Drag HUD Fix**: Strict left-button press gating (`isPointerDown`) eliminates hover-sticking; deferred pointer capture after 4px threshold keeps collapse, theme, and language header buttons immediately responsive; added off-window auto-release and popup **Reset HUD** button.
- **Multi-Window & Non-Chat Guard**: Skips non-chat routes (`/gems`, `/extensions`, `/settings`, etc.) and 0-turn screens; removed overly broad localized "Start" triggers; ignores stale pre-existing history chips on restored tabs in secondary browser windows.
- **4-Language Support**: Live UI, desktop notification, and keyword recognition across Simplified Chinese, Traditional Chinese, English, and Japanese.
- **Dark & Light Dual Themes**: Synchronized Dark Night (`🌙`) and Light Daylight (`☀️`) modes across both the floating HUD and extension popup.
- **Redesigned 2x Retina Assets**: All promotional banners, walkthrough diagrams, and Chrome Web Store screenshots rebuilt at 2x DPI.

### [v0.1.0 (v0.1 Beta)](https://github.com/ngiken/KenEasy-Gemini-MCP-Auto-Helper/releases/tag/v0.1.0) - 2026-11-21
- Initial Public Beta release with MCP "Always allow" auto-approval, `↪ Yes` follow-up chip clicking, draggable floating HUD, 1-click desktop stall notifications, background keep-alive, and 6-layer anti-loop circuit breaker.

See full details in [CHANGELOG.md](CHANGELOG.md).

---

## Friendly Links

- [LINUX DO](https://linux.do) - Sincere, friendly, collaborative, and professional developer community.

---

## License

This project is licensed under the [MIT License](LICENSE).
