# Herm

[![CI](https://github.com/chryzxc/herm/actions/workflows/ci.yml/badge.svg)](https://github.com/chryzxc/herm/actions/workflows/ci.yml)
[![platform: macOS 14+](https://img.shields.io/badge/platform-macOS%2014%2B-1f6feb)](#requirements)
[![Swift 6](https://img.shields.io/badge/Swift-6-F05138)](#development)
[![local-first](https://img.shields.io/badge/local-first-f0883e)](#how-it-works)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Sponsor](https://img.shields.io/badge/sponsor-%E2%9D%A4-db61a2)](https://github.com/sponsors/chryzxc)

**A native macOS companion for [Hermes Agent](https://github.com/NousResearch/hermes-agent), always within reach.**

*Named after the herms, the markers of Hermes that stood at doorways and crossroads, always in view and always within reach.*

Glance at the notch to see what your agents are doing and how much provider allowance remains. Send a quick message without opening the workspace, reply to a specific session when it is idle, or talk with your agent through continuous **Voice mode**. Expand into the full workspace when you want to inspect files, review changes, answer an approval, or manage your bots and tasks.

Session activity remains visible in the sidebar and notch when you switch conversations, including pinned and project sessions. Recently viewed conversations reopen instantly at your last reading position and refresh in the background.

In-chat approvals, questions, and input requests keep their actions compact; errors use the same clear callout treatment.

When Hermes supplies edit previews, completed replies show a changes card with expandable file diffs. These previews can omit files or lines and are not a complete working-tree diff.

While browsing chat history, prepared messages appear in order as they become ready, keeping the current reading position stable.

Performance captures record callback timing and workspace updates locally. Enable stack samples to include the call sites responsible for model updates.

Unread session badges and the floating “new messages” control count AI responses only. User messages, tools, activity, system notices, errors, and empty streaming placeholders do not increase the count. Opening an unread session takes you to its first unread reply and marks the captured updates reviewed; a blue-tinted unread divider remains visible for that visit. A session you already viewed since Herm launched reopens where you left it instead; the divider still marks the first unread reply. The Bot picker counts unread sessions per Bot in a red badge, with a plus sign when the available session inventory is incomplete. Scrolling to the latest reply clears the floating count.

The session list shows the unread count only when the leading slot has no approval, question, running, or error indicator. An unseen failed turn shows a red triangle there, including in All profiles. Opening the conversation acknowledges the history warning and retains the error details in the transcript.

[![Herm driving a shared browser with a live agent cursor](docs/media/browser-demo-poster.webp)](docs/media/browser-demo.mp4)

*▶ [Play the recording](docs/media/browser-demo.mp4)*

Unless noted, screens and recordings in this README show fictional projects and conversations.

> **Ask from anywhere → keep working → notice when needed → respond quickly → inspect the result.**

App labels and default chat identities use **Herm**. **Hermes Agent** names the backend; its commands, API endpoints, and shared configuration keep their Hermes names. `make naming-contract` checks default labels and common client-branding regressions as part of `make guard`.

Herm is a **frontend for Hermes**. Agent execution and session history stay with Hermes. Herm connects to the runtime already installed on your Mac and gives it a native interface alongside the Hermes CLI. It's an unofficial community project, separate from the official Hermes Agent Desktop app ([more](#disclaimer)).

```sh
git clone https://github.com/chryzxc/herm.git
cd herm
swift run
```

---

> [!IMPORTANT]
> **Herm doesn't yet do everything Hermes Agent can.** It includes a subset of Hermes features, and each one only turns on when the installed Hermes version supports it. Hermes Agent moves fast, so Herm will keep adding features over time. If something works in the Hermes CLI but doesn't appear here yet, it probably hasn't been added. See [Current limitations](#current-limitations) for the full list, and feel free to open an issue.

---

## Table of contents

- [Why Herm](#why-herm)
- [The notch](#the-notch)
  - [Quick Message](#quick-message)
- [Features](#features)
  - [Generative UI](#generative-ui) (visual and interactive replies)
  - [Appearance](#appearance)
  - [Conversations](#conversations)
  - [Chat composer](#chat-composer)
  - [Voice mode](#voice-mode-continuous-spoken-conversation)
  - GitHub: [Pull requests](#pull-requests), [Issues](#github-issues), and [Repositories](#github-repositories)
  - [Execution timeline](#execution-timeline)
  - [Developer tools](#developer-tools) and [native review workflows](#native-review-and-workflow-tools)
  - [File previews and revision notes](#file-previews-and-revision-notes)
  - [Agentic browser](#agentic-browser) and [iOS Simulator and Android Emulator](#ios-simulator-and-android-emulator)
  - [Projects and session continuity](#projects-and-session-continuity)
  - [Bots](#bots)
  - [Kanban](#kanban), [Activity](#activity), and [Calendar](#calendar)
  - [Office Preview](#office-preview)
  - [Control center](#control-center) and [Integrations workspace](#integrations-workspace)
  - [Native macOS integration](#native-macos-integration) and [Apple Intelligence](#apple-intelligence)
  - [Automations and quota](#automations-and-quota)
- [Requirements](#requirements)
- [Getting started](#getting-started)
- [How it works](#how-it-works)
- [Privacy](#privacy)
- [Current limitations](#current-limitations)
- [Development](#development)
- [Contributing](#contributing)
- [FAQ](#faq)
- [License](#license)

## Why Herm

Herm is built around a simple idea: **keep your agents within reach without making their workspace your workspace.** Start work, return to your editor or another app, and use the notch to check progress, quota, and requests for your attention. Open the full workspace when the work needs a closer look—not just to watch a conversation scroll.

It is not intended to reproduce every page or feature in Hermes Agent Desktop. Herm selectively brings useful Hermes capabilities into a **SwiftUI and AppKit interface designed for macOS**, with the notch as its everyday entry point.

### What makes the Herm experience different

| Experience | What Herm offers today |
|---|---|
| **Ambient agent awareness** | An edge notch with session activity, Kanban updates, requests for your attention, and finished results you haven't opened. |
| **Quota at a glance** | A notch preview for supported providers' allowance and reset times, without opening a dashboard. |
| **Quick interaction** | Start a new chat or reply to a specific session from the notch without changing the conversation selected in the workspace. |
| **Real-time spoken conversation** | Continuous Voice mode with spoken replies, interruptions and steering, captions, and a native voice stage with live activity. |
| **Inspect and give feedback** | Preview files in-app, annotate selected text, send revision notes back to the originating session, and inspect local Git diffs. |
| **A view of your agent team** | Profile-based bots, real Hermes Kanban boards, a map of agent handoffs, and a 3D Office Preview driven by task status. |
| **Watch the agent use real devices** | An agentic Chromium browser you share with Hermes, with a live cursor, step status, element annotation, and one browser per Hermes profile; plus iOS Simulator and Android Emulator tabs with touch input, UI annotation, screenshots, and app logs that attach to chat. |
| **Review alongside the work** | Repository checks and coverage information, changed-file diffs. These are aids for inspection, not a guarantee that the agent's work is correct. |
| **Act without opening the app** | Approve, deny, or reply from notification banners (optionally behind Touch ID), send selected text from any app via the Services menu, and trigger Ask Herm from Shortcuts. |
| **A native Mac companion** | Global keyboard access, composer autocorrect and dictation, optional on-device Apple Intelligence summaries, system appearance, Reduce Motion support, and an optional Hermes pet that can roam from the notch. |
| **Generative UI** | Replies that render as native tables, charts, forms, plans, findings, graphs, runnable commands, and sandboxed offline HTML apps, with session and global artifact browsing. |

These are highlights of Herm's experience, not a list of features exclusive to Herm. Hermes Agent Desktop shares many underlying capabilities, including voice mode. The distinction is how Herm brings them together around ambient awareness, quick interaction, spoken conversation, and local inspection.

The design priorities are **useful attention rather than constant activity**, **clear status rather than assumed success**, and **keeping quick actions tied to the right session**. Future improvements should strengthen those qualities rather than add features for parity alone.

## The notch

The notch is the main way to use Herm. It sits against the left or right edge of your screen, stays out of the way while nothing is happening, and shows you when Hermes needs attention.
Side-notch previews and expanded side panels keep a visible themed border, including in Liquid Glass.
The preview animates within a window sized once per transition. Clearing a
completion leaves the task-list refresh until the collapse settles.
A microphone icon on the collapsed top or side notch shows when Herm is listening for the wake word.
On the side notch, extra space separates the mic from the bot and activity icons.

[![The Herm side panel showing tasks and provider quota from the screen edge](docs/media/notch-side-poster.webp)](docs/media/notch-side.mp4)

*▶ [Play the recording](docs/media/notch-side.mp4)*

### Hermes companion

Herm displays the selected profile's enabled Hermes pet just below the notch, outside its contour. Its
poses follow task activity: hover over it for a greeting or
click to pet it, without opening the notch. It stays below the expanded preview,
with an occasional celebration after successful work. Hover the notch itself
for status and Quick Message. The pet uses the same assets and selection as Hermes
Desktop and the TUI. All pet surfaces use the same renderer, with Hermes' row
order mapped to native image coordinates so animation does not cycle through
another row's blank padding.

In **Settings → Appearance → Hermes companion**, choose a pet from
the always-visible **Select a pet** gallery, enable or disable it, and adjust its Hermes size.
**Apply to Hermes** confirms the shared change; Hermes handles any download.
After **Apply to Hermes**, the floating pet uses the saved size (100% is the
sprite's native frame size). Its window and roaming bounds resize with it;
the Settings thumbnail remains compact. Oversized pets fit within the display.
Notch announcements, including quota changes, share a centralized pet-reaction
mapping; hovering and petting remain short-lived interactions.
This requires Hermes' `pet.*` gateway methods. Older runtimes keep the ordinary
notch and show companion availability guidance in Settings. Reduced Motion
displays a static sprite.

Enable **Roam from the notch** in the companion settings for walks across
the current display's bottom edge with directional animation, pauses, and periodic
returns home. Task activity and hovering pause movement; drag repositions it.
Right-click the notch or pet and choose **Call pet home** to return it. Roaming
is local to Herm, defaults off, and is disabled by Reduce Motion.

### What the notch shows

The notch changes to reflect what Hermes is doing, so you don't have to keep a terminal open:

| State | What you see |
|---|---|
| **Idle** | A thin, quiet rail on the screen edge. |
| **Working** | A live indicator while Hermes is running a turn, a tool, or a background task. |
| **Needs you** | An attention state when Hermes is waiting for an approval (for example, a dangerous command) or has asked you a clarifying question. |
| **Finished** | A short announcement when a session completes, which stays marked until you open the result. Tool and background-task progress stays compact. |
| **Offline** | A clear indicator when the local Hermes runtime isn't reachable. |

The Tasks preview opens on **Activity** by default. Its list/grid toggle switches between session activity and **Kanban** cards, using the same controls as Quota. Both views use Herm’s compact status cards. Kanban shows running, blocked, and review cards across boards. Confirmed card moves and edits automatically expand the Kanban preview without changing your selected view; click a card to open its board and inspector. The notch checks Kanban every 15 seconds while work is active and about once a minute when idle. The initial load stays quiet, and unchanged or failed refreshes do not announce. Up to 30 recent card updates remain until opened; active cards stay visible.

The Activity preview separates **Needs your attention**, **In progress**, and **Finished, not opened**. **In progress** shows the same working Bot count as the Bot picker. Working Bots without session rows appear by name and avatar above the session list. Approval requests and clarification questions show their own status and a short summary, including requests from other sessions. New requests open the preview; select the row to review and respond in the workspace.

Working and waiting Bots and other visible indicators keep animating while you scroll or switch to another app. Core Animation handles whole-face movement. Reduce Motion and motion-free skins still turn decorative motion off.

The expanded top island fits its toolbar beside the camera housing, with Tasks, Quota, and the mic on the left and the ear and tab actions on the right. The toolbar moves below the housing when it needs more room.

Activity rows in the side notch and top island have no background fill at rest, including the current session. Both previews offer a labelled **Quick message** entry. Reply controls reserve their space so activity titles stay still on hover.

The top island’s black workspace band keeps its status headline, counts, and provider quota readable with every skin.

Conversation approvals, clarification choices, and secret/login requests share a compact neutral card with explicit status, labeled inputs, and grouped actions that stack in narrow panes. Reopening a chat restores its pending clarification and answer choices. Multi-select answers show their selected state; submitting keeps an in-place progress indicator and disables duplicate responses.

Chat approvals keep **Deny** and **Allow once** visible in narrow panes and move longer-lasting permissions into the ellipsis menu. The wide footer shows all available choices. Press Return or Enter with the approval card focused, or from an empty composer while **Allow once** is in view.

The latest conversation approval stays visible as resolved after it is answered in the conversation or notch. This presentation is kept in memory for the current Herm process, not reconstructed after restart.

Choose **Quick message** in either Tasks view to start a new session without opening the workspace. Hover a session row to reveal **Reply** and compose directly beneath it; its reserved slot keeps the title stable. Reply stays visible while composing or navigating with the keyboard, and the reveal respects Reduce Motion. Replies stay tied to that session, and neither action changes the workspace’s selected chat. The compact composer keeps its own draft, preserves workspace attachments, and stays open while typing; **Close** or Escape leaves it. Failed sends keep the text for retry. Kanban rows show the assigned bot’s stored avatar or its existing fallback identity.

Choose a finished session row to peek at its **Latest completed reply** inside the notch. Copy an excerpt, open or reveal generated files, reply to that session, or open it in the workspace. Reading leaves the selected workspace chat alone. A deliberate selection marks the matching completion reviewed after its content loads; hovering does not. New results offer **Update** while the displayed excerpt remains stable.

The notch shortcut opens keyboard interaction: arrows select a session and Return inspects it;
Escape backs out and then dismisses. **More → Saved actions** prepares editable starter or custom
instructions without sending. **Working sets → Checkpoint** saves a note and exact quick-draft
reference for later resumption. **Watch activity** focuses ordinary session activity on one set;
blocking decisions and failures remain visible globally. Result Peek's **Compare with previous
read** compares two deliberately loaded snapshots, including changed output references.

The quick composer accepts dropped files and links, pasted text and images, and an explicitly chosen project for a new session. Its **To** picker captures the profile and session before sending. **Drafts** restores unsent content after a restart; missing or changed files remain visible. Images, one PDF up to 25 MB, and generic files use Hermes' attachment methods when supported. Interrupted or uncertain submissions require reviewing the destination session before resending.

**Settings → Notifications** controls the desktop alert sound and separate alerts for completions,
approvals/questions, session failures, automation results, Kanban updates, quota warnings, watched
pull requests, and watched repositories. New feature alerts are opt-in. Snooze all desktop banners
and sounds for 15, 30, or 60 minutes, or resume early; banner actions also offer a 30-minute snooze.
Snooze includes approvals and failures, keeps in-app attention visible, survives restarts until its
expiry, and does not replay missed banners. Quiet periods below still apply independently.
Use **Send test alert** and **System Settings** to check macOS permission, sound, and Focus settings.

Choose the bell icon in the Tasks header for a quiet period of 30 minutes, 60 minutes, or until you end it. Hover for the current quiet status. Completions, ordinary quota changes, and informational updates enter a digest. Approvals, questions, and failures that stop work can still interrupt. The same policy controls notch announcements, pet announcement reactions, and opted-in system notifications. **Review digest** returns to the recorded sources; it stores references rather than response bodies.

In the chat composer, dictation shows a live microphone waveform with controls to cancel, stop and edit, or send. Cancel preserves the draft from before dictation.

Quick approval and clarification answers stay tied to their original request, session, and profile. A pending answer blocks repeated clicks. A confirmed refusal offers **Retry**; an uncertain acknowledgment offers **Check request**, which enables another answer only after Hermes confirms that request is still pending. These answers preserve the workspace draft and attachments.

The status colors match the rest of the app: blue means active, green means healthy or done, amber means a warning or that Hermes needs you, and red means a failure.

Global hover tooltips show one floating, fully opaque, theme-aware panel beside the hovered control and above workspace content and scroll containers. Hover descriptions appear on first attachment and are cancelled when the control is removed. Long help wraps, stays within the display, and never takes keyboard focus.

Chat message timestamps appear on hover, with no separator after the assistant message actions.
User message footers leave extra space before the Copy icon.

### Quick Message

Quick message opens a clean message-only panel with a destination picker and Close.
Tasks, Quota, Quiet, refresh, and Open Herm controls stay out of the way while composing.
The attachment button, growing text editor, and send button share one borderless row. A new draft opens directly beneath the destination picker and grows with the text and attachments. Once the session exists, the 560pt conversation panel shows your sent messages and live
replies using the session chat's transcript and message actions. Follow-up messages
stay in that conversation; the destination menu starts a new one when you choose it.
The workspace's selected session and draft stay separate. The composer stays at the
bottom; attachments appear inside it.
The + menu offers files, paste, window capture, saved drafts, and discard; review and
retry appear for interrupted sends. Project choices appear only for new sessions.
Inline replies share the same composer and stay tied to the task's session.
Quota advisories are hidden in both composers; send failures remain visible. Return or Command-Return sends;
Shift-Return inserts a newline.

The notch also offers **Recall** for profile-scoped conversation search, **saved working sets**
for explicit destinations, and **session capacity actions** with acknowledged model changes.
Result Peek includes explicitly pinned sources, quoted corrections, Markdown export, and coding
review. Clean turn baselines enable scoped diffs.

Failed or pinned routines open a compact recovery view with execution and delivery shown
separately. Supported Pause, Resume and Run now actions retain the owning profile. Skills & MCP
repair uses Hermes' own installation, credential and OAuth paths. Targeted subagent steering
labels queued corrections honestly; fingerprinted memory entries can be inspected and corrected.
Each operation remains unavailable when its installed-runtime contract cannot be verified.

### How to use it

Session and group-chat lists, project pickers, inspector tabs, approval details,
usage labels, shared inputs, and the chat composer follow the window text scale. Markdown headings
and fenced code resize with reply prose.

Standard UI and conversation font sizes live in `DockTypography`; SwiftUI views
and native Markdown/composer text share these definitions.

Window mode uses standard 100% sizing for fonts, icons, and action
controls: 12pt body text, 13pt navigation labels, and 14pt conversation text. Text renders at its final size, with normal pointer and selection
coordinates on Retina and standard-resolution screens.

| Action | Result |
|---|---|
| **Hover** | Opens a preview with two tabs. |
| **Tasks tab** | Lists every session that's in progress, with the ones that need you first, plus finished results you haven't opened yet. Click one to go straight to it. |
| **Quota tab** | Shows provider usage and reset times, so you know how much allowance is left before starting a long task. A compact **Open Quota** button opens the full quota workspace. |
| **Mic button** | Starts a voice conversation right in the notch, the same as **⌥⇧ Space**. |
| **Ear button** | Turns the always-on wake word on or off: Herm listens on this Mac for “Hey <name>”. While it listens, a small glowing dot pings beside the bots on the closed notch. |
| **Click** | Expands the notch into the full workspace in the same window. |
| **Double-tap ⌘** | Opens or closes the workspace from anywhere. |
| **Double-tap ⌥** | Opens or closes the hover preview from the keyboard. |
| **⌥ Space** | Quick capture: opens a new message in the notch from any app. Change it to ⌃ Space or turn it off in Settings → General → Keyboard shortcuts. If nothing happens, another app is using the chord. |
| **Drag** | Moves the notch along either screen edge. Its position is saved. |
| **Right-click** | Moves the notch to the left or right edge, or quits the app. |

A typical workflow: start a long task in chat, collapse the workspace, and keep working. When the notch turns amber, hover over it to see which session needs approval, click that session, approve, and collapse again. When the task finishes, the notch tells you.

Choose **Dots**, **Vertical line**, **Ring**, **Icons** (a status icon, with an unread mark for finished replies), **Count** (the number of working sessions), or **Bots** (the face of the Bot that is working, blocked, or finished, with a badge counting finished results) in **Settings → Appearance → Notch**, or from the gear menu's **Notch** submenu. Both switch the notch between a screen **Side** and a **Top island** around the camera. Count is the default. The selection applies immediately and is saved across launches. The vertical line sweeps while work runs; the ring rotates. All notch animations respect **Reduce Motion**. If you hide the notch, switching from the window back to the floating panel shows it again, since the panel opens from the notch.

## Features

Expandable detail sections toggle when you click anywhere in their header row, including the label and empty space beside it.

Async actions show local progress while requests are pending. Markdown PR and issue
links show an “Opening…” indicator while GitHub resolves their inspector tab;
settings, connection, memory, review, and group-chat actions expose pending feedback
and suppress repeat submission. See [the loading-state audit](docs/loading-states.md).

### Generative UI

Written chats, including group chats and bot mentions, use ordinary Markdown. Saved
generated replies show readable text in the transcript. You can still open their
original cards from Artifacts.

In **Voice mode** and **Talk**, Herm can show charts, tables, maps, and other
read-only visuals alongside the spoken reply. Control visual previews in
**Settings → Chat → Replies → Generative UI** (on by default).

**What a generated artifact can contain**

| Kind | Components |
|---|---|
| Data | Sortable, filterable tables with aligned numbers; bar, line, area, and point charts with multiple series linked to a shared dataset (selecting a row highlights it in the chart); metric tiles with comparisons |
| Decisions and plans | Option comparisons against shared criteria, checklists, timelines with dependencies, and workflow steps (proposed, running, passed, failed, blocked, skipped) |
| Structure | Label–value fact sheets, callouts (note, tip, important, warning, caution), graphs (up to 200 nodes, solid or dashed edges, with status) and collapsible trees |
| Development | Copyable code blocks, review findings with severity, location, and recommendation, and runnable command cards |
| Media and sources | Source link lists, image galleries, and before/after image comparisons |
| Input | Forms with text, number, choice, multiple-choice, and yes/no fields |
| Connected records | Cards that open loaded pull requests and issues, Kanban tasks, Calendar items, usage reports, and the session Timeline in Herm's existing views |
| Interactive HTML | Self-contained HTML apps that use your Herm theme colors |
| Mermaid diagrams | Voice mode and Talk can preview finished Mermaid diagrams. Written chat shows their source as a code block. Rendering is offline with the bundled [Mermaid](https://mermaid.js.org) 11.17.2 (MIT) |

Sections group related components, and metadata labels **Fictional data**, assumptions, source, and observation date when supplied. Generated status is the assistant's claim: a workflow step marked passed needs supplied evidence and is labelled a reported snapshot, never live state.

**Acting on a reply**

- **Forms** send your answers as a normal message to the original session. They never run actions and must not ask for passwords or approvals. Unsent values survive navigation until Herm quits.
- **Run in Terminal** on a command card opens the session Terminal in the project or worktree directory (or Home), in a fresh shell, so it never overwrites a running terminal. Each command needs its own click; code blocks stay copy-only. See [the command format](docs/generative-ui.md#runnable-command-cards).
- **Use in current chat**, **Ask about selection**, and **Revise…** add the reply as context in the composer without sending or replacing your draft. Revisions of the same reply are grouped, and you can compare a revision with the previous one.
- **Expand**, **View source** / **Copy source**, **Copy readable result**, and **Export…** (`.herm-ui.json`, or a standalone HTML file for HTML apps) live in each reply's menu.

**Safety and limits**

- **MCP Apps.** An MCP tool that ships its own view (the MCP Apps standard) shows an app card under the turn's activity. Click **Open** to run it in the same offline sandbox; it receives the tool's input and result and can request HTTPS links, each requiring native confirmation. Network access a view requests is listed but not granted, and views cannot call tools yet.
- Interactive HTML runs only after you click **Open interactive view**, in an offline sandbox with no network, storage, files, credentials, tools, downloads, popups, or device access. Closing it, switching session or profile, or restarting Herm resets it; changing the theme reloads it.
- A reply is limited to 1 MiB, 100 blocks, and 1,000 rows or points per block. Invalid or oversized replies show **Visual reply unavailable** with their readable text, the reason, and the source. While a reply streams, visual content waits until it finishes.

**Artifacts.** The session inspector's **Artifacts** tab and the global Artifacts library list interactive replies alongside files, images, and links. Outputs appear as transcript pages are indexed; the header shows when indexing is still in progress or incomplete. Saved tools are references to their original reply; inputs, sorting, and selections are restored for the same revision.

See [Generative UI formats and isolation](docs/generative-ui.md) for the `herm-ui` JSON format.

### Appearance

The Herm window's interface scale (its setting is temporarily hidden) is
**Compact** (100%), **Default** (110%), **Large** (120%), or **Larger** (130%). Icons and controls scale
with the text, and the choice is saved across launches.

[![Switching Herm skins across the workspace](docs/media/skins-demo-poster.webp)](docs/media/skins-demo.mp4)

*▶ [Play the recording](docs/media/skins-demo.mp4)*

Actions use visible buttons, including compact buttons in dense panes. Inline
navigation and Show more links stay underlined before hover, and linked GitHub
metadata carries a navigation arrow so it is distinct from static metadata.
Session Pull Request and Issue warnings keep vertical spacing below the filter divider.

Workspace page headers use consistent text titles and subtitles, with refresh
and other actions on the right. Buttons share 12pt themed labels, hover and
pressed feedback, and disabled states. Shared action icons inherit their label's
skin-specific color, including on filled Glass and neon buttons. Repository Issues
and Pull requests buttons use their matching destination icons. Activity branch
pills use compact metadata sizing. Primary actions use a quiet accent tint;
secondary actions use the shared outlined or compact treatment. The pull request
Merge action uses matching icon and label ink on every skin, including filled
Storm and Glass controls. PR toolbar actions use compact sizing for a tighter row.
Merge uses a shared split button in the toolbar and merge panel: choose an available
merge commit, squash, or rebase method, then confirm the selected action. The dropdown
also opens merge requirements; repository rules and expected-head checks still apply.
Workspace pages, including Settings, use a flat theme canvas without a corner glow. Open Settings from the workspace or with the macOS Settings command (⌘,). Settings opens inside the workspace; Herm does not create a separate native Settings window.
Settings loads the runtime model catalog only when Models & tools opens, keeping General free of those backend requests.

**Settings → Passwords & Logins** manages the same profile-scoped vault as Hermes Agent Desktop.
Choose a profile to view credential metadata, add a website login (with an optional OTP secret), or remove a local entry.
The Password managers section shows backend-reported installation and lock status and supports enable, disable, unlock,
and lock. Manage external entries in their password manager. Passwords travel directly to Hermes through its authenticated
RPC connection and are never saved in Herm preferences or displayed in the credential list. Changes affect future fills,
including active sessions; removing a credential does not sign out existing website sessions. Unsupported or malformed
vault responses disable actions and show recovery guidance. Herm does not implement a separate credential store.

**Settings → Subagents** configures delegation per profile. Choose Default routing or an available model/profile
routing backend, and install the official Advanced Delegation plugin from the catalog when offered. Model routes
support adding, editing, removing, and choosing a default; profile routes show bot avatars and let you choose allowed profiles and a default.
Provider, model, turn limit, parallelism, timeout, and reasoning effort use explicit Apply confirmation and affect future
delegations. Running subagents keep their settings. Routing availability comes from Hermes; unsupported routes stay
disabled, and a blocked saved route is shown honestly. Route edits preserve additional backend options and credentials.
Existing direct-endpoint defaults remain intact and can be edited in Hermes Agent Desktop.

Herm uses one shared workspace design across every custom skin: consistent navigation,
content hierarchy, spacing, actions, and macOS system font. Skins apply their colors,
geometry, materials, and motion on top. Liquid Glass is the default presentation;
its light appearance lets more of the backdrop show through while retaining readable text.
See [the design specification](DESIGN.md) and [UI refinement audit](docs/ui-foundation-audit.md).

Shared settings groups and integration icons now follow each skin's material and
geometry. Inspector tabs keep stable widths on hover, with full-title tooltips;
PR and Issues toolbars share consistent insets. Settings controls stack below their labels when needed,
and Bot filters adapt to narrow panes using shared actions. Long composer queues and background
task lists scroll within bounded trays so the message input remains reachable.

The default **Glass** appearance follows macOS Light/Dark with frosted panels
and cool crystal surfaces, with a single native glass background to keep broad
reflections off the chat reading surface. Glass uses fine appearance-aware edges and shadowless controls in both modes;
light mode adds a stronger neutral window backing, darker supporting text, white
frosted controls, and clearer selected tabs so content stays readable over desktop colors.
Popovers and sheets share the skin's opaque canvas, while light Glass cards,
fields, menus, and floating panels use white surfaces without the native warm gray cast.
Filled graphite actions stay distinct from frosted secondary controls. **Clean**
uses porcelain surfaces with clearer outlines around the workspace, cards, and
controls. Light has a white reading canvas, a cool gray frame, and more distinct
selection and focus states. Clean keeps neutral graphite actions and stable palette
colors for projects, agent activity, and configuration inventories. System-following skins update
automatically when macOS switches between Light and Dark, including while the
workspace is open. Skin changes also apply to the side notch and its open preview.

Dragging files over an editable composer traces its outline once. Attachment
chips appear as soon as files or pasted images are staged. An image icon holds
the thumbnail's place while it loads. Dragging a queued prompt marks the insertion
point above the destination row.

In chat, the send arrow folds into the stop control while a reply is running. Thinking dots pass a highlight between them, and context compaction draws three lines together. Both indicators run in Core Animation. When a tool changes in a chat without a bot avatar, its icon draws once inside a continuous breathing halo.

Search, task details, and new columns open from their respective edges. Bot motion pauses during live resizing. Warm Light, Clay, and Dusk use shallower card relief. Switching skins reveals the new material from the pointer. Switch thumbs stretch between stops, checkmarks draw into place, and a side notch curves toward a pet as you drag it home.

Herm uses a content-first layout across skins: shared spacing and action sizes, quiet dividers, and cards reserved for distinct objects or tasks. Selected list rows follow the active skin’s selection surface.

Active navigation, icon rails, inspector tabs, and open sidebar toggles keep
visible selection treatments at rest, with filled icons and stronger ink. Liquid Glass
uses a tonal fill without a leading line. Selected
content rows retain a fine contour across translucent and solid skins.
Glass controls have clearer outlines in light and dark appearances.

All skins retain their own visual identity with balanced surface steps, clearer
supporting text, and quieter depth. Paper skins keep warm stock and ink; dark
skins keep their graphite, oxblood, steel, plum, phosphor, and neon hues.
Floating and springy skins lift actions subtly on hover and settle on press;
surface reveals follow each skin’s motion style. Reduce Motion disables these
effects, and Retro, Pixel, and E-Ink remain still.

Choose from the skin gallery in **Settings → Appearance**. Each card is labeled **Built-in** or **Imported** and previews
its own material, geometry, and selection treatment. Switching skins
keeps the Appearance page selected while the new skin applies immediately. The gallery
reflows into fewer columns in narrow windows, keeping previews inside their cards. The 25 built-in skins
range from Hermes' desktop look (Nous blue with the etched backdrop from Hermes
desktop) and Ares' oxblood panels to folded
Origami, ruled Notebook, molded Clay, and silver-beveled Retro. Terminal has
phosphor scanlines, Pixel has stepped arcade outlines, HUD has cyan
crosshairs, and Storm has Tokyo Night indigo with rain, matte blue actions, and solid selection markers. Navigation and composers follow the selected skin while keeping
the workspace layout and controls in place. Each skin also moves in its own
way: Hermes snaps like its desktop app, instrument skins move crisply, Cartoon
and Clay spring, and Glass, Dusk, Storm, and Island settle softly. E-Ink,
Pixel, and Retro remain motion-free; other skins respect Reduce Motion.

Skin changes also reshape controls. Terminal uses phosphor keys, Notebook marks actions with an
ink swipe, Swiss uses ruled actions, and mechanical skins use ridged slide switches. The gallery
shows each skin’s switch beside its type sample.

Canopy pairs matte evergreen with a lichen-colored frond. Capiz has pearl-rimmed ivory panels and teal underlines. Hi-Fi has graphite faceplates and amber tuning marks. High Contrast adds bold outlines and checked navigation in both macOS appearances.

To use a T3Code palette, choose **Copy theme JSON** on the theme page, then
open the sidebar gear → **Skins** and choose **Import from clipboard**. The same
action is available in **Settings → Appearance**. Herm applies the palette to its Clean skin and saves it
on this Mac. Embedded SVG conversation wallpapers such as Pixel Quest animate behind chat messages.
Reimport older copies to pick up their artwork. Reduce Motion uses the plain palette.
Palettes with light and dark variants follow macOS. Reimport a
theme to update it. To remove an imported skin, right-click its card and choose **Remove skin**. [T3 Themes](https://t3themes.com/)

Herm uses one centralized solid accent palette throughout the app: teal, amber,
violet, coral, blue, orange, pink, green, cyan, indigo, and tangerine. Neutral skins use gray actions and selection;
character skins use their own hue. Live work indicators use the shared blue status tone across sessions, bots, automations, and the overview. Status, charts, agent identities, and file icons reuse the
same approved solid color families. The [color-system audit](docs/color-system.md)
records the mapping for each app area; `make color-contract` guards future features.
Solid fills stay the same in Light/Dark; text ink adapts for readable contrast on each
theme, including Light/Dark, Monochrome, and E-Ink.

The desktop workspace card clears the full toolbar in both density settings.

The expanded floating workspace fills the panel vertically without extra top or bottom shell padding.

PR lists use green for open work; Issues uses blue status icons with neutral state text.
Ordinary IDs, branches, and drafts keep neutral ink. PR readiness is colored separately from lifecycle.
Category colors distinguish calendar sources, automation, and file changes;
orange is reserved for attention rather than normal draft or modified state.

Shared tabs carry their selection highlight between choices. Navigation glyphs respond to selection, floating-skin controls lift gently on hover, and retained disclosures ease open and closed while preserving nested inputs.

Shared interface motion includes smoothly updating progress meters and section counts, short tab and navigation selection transitions, rotating disclosures, and subtle page and modal reveals. Loading screens, pending actions, and running session indicators use a four-tile mosaic. Each tile lifts and brightens in clockwise order, including on the Chats rail when the inspector is closed. These indicators follow the active skin and stay still with Reduce Motion or a motion-free skin. Controls remain usable and keep their layout footprint.

### Conversations

Saved conversation images are restored from Hermes history when reopening a session, including images stored within message content. Images in view are prepared first so an image-heavy session can stay responsive while the rest load. Images already shown in a cached preview carry over without duplicating them.
Emoji reactions on your messages sit on the corner of the message bubble or its image attachments.
Reopened messages omit Hermes' appended memory recall context and reconcile confirmed sends with saved history.
Sending means submission is in flight. Accepted means Hermes accepted the input, not that storage is confirmed;
Queued reflects an explicit queued acknowledgment. A proven row receipt or conservative history match clears
the status. Delivery unconfirmed offers a read-only, bounded Check status action, never automatic resend;
a row missing from that window is inconclusive. Status appears in user-message metadata, not assistant content,
and there is no permanent stored badge or read receipt.

Recently viewed conversations can show their last loaded messages immediately while
Herm refreshes them from Hermes. Herm also preloads a bounded set of recent and pinned
conversation previews across profiles in the background. The title shows when the
conversation is refreshing or not current; session actions become available after the refresh succeeds. Drafts
remain editable, and the conversation menu offers retry if loading fails.

The session-title popover reuses the sidebar session row, with matching typography,
status marks, timestamps, inline project pills, previews, and session actions.

![A Herm workspace conversation with tool calls and files inline](docs/media/workspace-conversation.webp)

Workspace pages share Calendar’s top titlebar treatment, with sidebar toggles aligned
beside the traffic lights. Chat uses three full-height panes: the session list,
conversation, and inspector. Session rows stay visible while scrolling, and live replies
keep their place above the composer. The session title uses the available header space,
with actions inside the conversation pane; the inspector's tabs extend to the top of its own pane.
Visible status and loading animations continue during scrolling.
Older chat pages parse in the background and reuse the navigator's existing rows.
Waiting history continues preparing if you resize the conversation at the edge.
The Bots and Sessions switch responds across each tab, not just its label.
The session sidebar places **New chat** above Pinned. Navigation distinguishes Chats (speech bubbles), Integrations (puzzle piece),
Artifacts (stacked files), and Bots (a robot). Chats shows a small
spinner for running sessions and a count of completed chats with unread updates
for the selected bot. Both appear together when work is running and results await
review; opening a completed chat clears its unread badge. Use **Mark all as read**
beside refresh in the **Recents** header to clear unread updates across the selected
bot’s loaded Recents, including conversations under Show more. Badge calculations are
cached independently of transcript updates; status polling pauses while the
workspace is hidden or Hermes is disconnected.
The sidebar stacks enabled sections for the selected bot under its bot header.
Recents, Projects, and Automations use a 6pt gap between
header action buttons. In the bot picker, drag a profile's handle to reorder it,
or focus the handle and use the arrow keys. Drag it to the top or bottom edge and hold
there to scroll through a long list's hidden profiles in the same drag. The order is saved locally across restarts without changing the
selected profile or its conversations. Choose **All** at the top of the
bot picker to merge every bot's pinned and recent conversations into one list; each
row then shows a pill with its bot's avatar and name, and opening it switches to
that bot. The sidebar reuses its Recents and Automations groups and unread inventory while you hover, scroll, or search. Each section header stays at the top of the scrolling
list until the next section replaces it; rows remain lazily rendered. Click a
section header to expand or collapse it even while the list is still scrolling.
The section heading and rows update together without refreshing the open chat.
Pinned keeps the pins it already showed while the switched bot's own pin list is
still loading; a chat drops out only when that list, a recent-session scan row, or
an acknowledged pin change settles it.
Recent chats and pins appear as soon as the first page arrives. Older chats load
in the background and join search as they become available. Background polls and
runtime notifications refresh the latest history page, reusing older loaded sessions
for up to five minutes. Explicit refreshes reconcile the full saved history immediately.
One Hermes request loads recent chats for all bots. Switching to a bot shows its
conversations at once: the list Herm last showed for that bot, or on a first visit
its rows from that all-bot request. Hermes is then re-read quietly in the
background. Returning to a bot reopens the chat it was left on, at the same
reading position when that transcript is still cached. Retained lists stay keyed
to their own profile and are cleared when the Hermes sign-in changes.
Startup confirms the selected bot before reopening its last chat. Bot avatars and
live status load independently of restoration.
Recently opened chats show their cached transcript immediately across bots, split tabs,
and detached windows while Hermes refreshes it. The cache is bounded and held in
memory. The opening preview includes bot replies received while you were away.
Herm starts warming pinned and recent chats as soon as the recent list appears.
A complete, already-read preload can show immediately on the first visit while
Hermes confirms the session.
If Hermes times out while opening a stored chat, Herm can still show its history
read-only, including older messages as you scroll. Retry loading the conversation
to respond. A conversation timeout does not make the session list unavailable.
When the opening position is unknown, Herm checks for unread replies and opens
directly at the first unread reply, or at the latest message when all replies have been read.
When the loaded transcript covers that check, opening the conversation uses the
same history read to position the unread divider.

Chats, Activity, and other desktop pages share the window's layout host. Showing
or hiding the Chats list or inspector applies the new pane widths immediately
and keeps each mounted pane's state.
Chats groups and sorts background session activity off the main thread.
Focusing an already-loaded split column keeps both conversations live while
the inspector follows the selected column.

Talk, Pull requests and Issues open as inspector tabs from its **Open a new tab** grid.
Voice runs while the Talk tab shows. Choose **Conversation** from the inspector’s
**+** menu or empty grid to open another session, Bot chat, or group chat in split view.
Opening the inspector in the floating desktop panel keeps the conversation visible beside it, with the inspector tab row matching the chat header. The three panes default to roughly 25% list, 40% conversation, and 35% inspector, with adjustable dividers and minimum readable widths.

Each Terminal inspector tab owns one shell; open another Terminal tab for a separate shell. Terminal options use a vertical-dots menu beside Previews.

The session rail shows beside the transcript and composer by default; use the
stacked-cards **Hide session rail** button beside Conversation actions to hide it. The rail and its toggle hide
when the conversation column is narrower than 800pt, including when opening or resizing
the third panel leaves too little space. Widening the column restores the chosen visibility.
Both density settings reserve the rail's full width so it does not cover chat content.
The card is titled **Session overview** when no repository is selected.
Its sections summarize pending questions and approvals, the session task plan,
delegated subagents, workspace checkpoints (with diff and a confirmed restore),
outputs, pinned messages, and the current workspace alongside Changes and PRs.
Subagents show identity and status without activity descriptions. Live status wins;
nonterminal history without current live evidence is shown as status not current.
Tasks share the composer's status indicators and ordering: in-progress tasks first,
pending next, and completed or cancelled tasks last. The active task remains visible
in the Tasks summary and uses a highlighted row and progress indicator when expanded.
Empty sections stay hidden. Sections open and close immediately. Expand a section for details; **Respond in chat** reveals
the existing request at the end of chat and focuses the composer, a pinned item jumps to its message, and
**View all outputs** opens Artifacts in the third panel. Output rows use the shared
file-type icons for images, documents, archives, and code. Outputs reuse the shared
artifact index and refresh after a turn or from the rail's refresh action.
Disclosure carets align with the first-row icons, including wrapped titles and task summaries.
Pull requests also collapse as a group, with a count and a bounded list of individual PR quick views.
PR membership comes from explicit links in the selected chat or targeted PR tool operations;
repository listings, searches, and other sessions' history do not add their results.
Live results must belong to the selected response. Switching sessions or profiles resets
rail state and its cached workspace folder; tasks, plans, outputs, attention, and pins use that session's data.
The Plan section lists the `.hermes/plans/` files the chat names and any plan you added with **Add to rail**, with progress from their checkboxes or else the session's task list, and a Track progress action when neither has any; selecting one opens it in Plan view. Visible rails and document previews share file updates when a plan changes.
The rail picks up file edits while it is visible and reuses the parsed plan between edits.
Workspace uses a colored folder icon, a project name and path, and labelled branch
and latest-commit details.
Changes reflects Git status for the session's worktree. Explorer and Source Control follow the folder
confirmed by Hermes, including linked worktrees outside the original project. Chats sharing a worktree
share its local edits. The composer shows the folder and branch row for Git worktrees.
In that menu, find the current worktree above a searchable list;
choose another worktree, then **Move this chat here** to keep the conversation in that worktree, or **Start a new chat here**
to carry the unsent draft into a new chat. Moving waits until the current turn ends, and the chat then stays in the chosen
worktree even if the agent works in another one. A chat that has not sent anything simply starts there. **New worktree task** creates a new worktree
and moves the draft to a new chat there. Existing terminal shells keep their folders and running commands.
Use **Add to project** or **Move to project** in a conversation's menu to re-home it under another project; the conversation keeps its history and the project label and lists follow at once. It is unavailable while the conversation is working or waiting on you.
The icon has no background and highlights when the rail is open. Its floating
cards sit over the same continuous conversation background, with the conversation's
scrollbar at the far-right edge beyond the rail. The rail discovers PR
links in loaded conversation messages and targeted PR tool activity in the background, fetches their GitHub details,
and shows PR details inline. Refresh updates details; missing access shows
an unavailable state. The rail uses a quiet repository card with compact PR rows
and a **Changes** row when that session's repository has local edits. The wider card
hides the PR section when no PRs are linked, and shows one empty state when no section
has data. Click Changes to expand the file list, then a file to
open it in a session preview tab. PR rows show quick details in the card. Every
expanded detail area has a 280pt maximum height and scrolls longer content inside
the card; short content keeps its natural height. **View all changes** remains below the file list.
Use **View all changes** to select Source Control, or activate a PR row to open a
separate, closable PR tab in the third panel; the center stays on Chat. Counts show
tracked text additions/deletions against HEAD; new and binary files remain included in the file count. The card's actions menu
refreshes both GitHub and repository data. Hide the rail to give the conversation
its full width.

Session list spinners follow Hermes’ live execution state and refresh every ten seconds while the sidebar is visible, including unopened sessions for the selected bot. Recent writes alone do not indicate running work; the next live refresh clears missed completion events.

The empty chat centers the orb, introductory text, and composer together. Once a message appears, the welcome fades in place and the composer glides to the bottom. Transitions respect Reduce Motion and motion-free skins.

Every third-panel tab can be closed, including the last one. With no tabs open, launch cards open Browser, Terminal, Explorer, Artifacts, Source Control, or Timeline; the **+** menu and **Command-Shift-T** remain available.

Tab close buttons have full-height click targets. Hover a tab’s icon or name to expand the tab in place, revealing its complete name and close button. Compact tabs return to icons when the pointer leaves. Labels use the available width; only the tabs needed to fit the strip collapse, with the active name kept visible when possible. Switching tabs or resizing reveals the active tab automatically. Drag its name or icon to move the tab while the window stays still; the tab menu also offers Move tab left/right. The + menu stays reachable, and each conversation keeps its order during the current app run.

Inspector tab hover expansion uses a leading-aligned row without width animation. Drag previews carry the whole tab, including its icon, title, background, and close action.

Session workspace tabs share a centralized 16pt horizontal inset. Artifacts uses the
tab title and a compact status, search, and filter toolbar; Browser keeps its toolbar inset while rendered
webpages fill the available tab width, including additional browser tabs.
Restored browser pages and inactive terminal shells open when their tabs are used. Changing sessions only lays out that session's tabs and does not stop terminals in other sessions.
Already-open pages and running shells keep their state when you switch tabs.
Local Review searches the loaded comparison in the background.
Pull request, issue, and simulator tabs avoid a second outer gutter around their content.

Messaging sessions show a compact source pill beside the preview, including Discord, WhatsApp, Telegram, Slack, and other reported integrations. Unknown integrations use a generic icon; local sessions omit the pill.

Markdown GitHub pull request and issue overview links open the shared PR or issue detail view in chat’s Pull Request or Issue inspector tab
when that page is enabled in Settings and GitHub resolves the item. Each chat keeps
its own GitHub selection; opening a link leaves the conversation visible. Disabled pages,
unavailable items, and links to anchors or subpages retain the browser fallback.

- **Streaming chat** with Markdown (including tables with optional outer pipes and table text sized to match reply prose), images, tool output, and inline clarification requests. History prepares image thumbnails in the background. Response text reflows at the current pane width, keeping its action rail beneath the content when resizing.
- **Image previews** preserve their original proportions without square padding, so wide and tall screenshots fill their intended thumbnail size. Click a local image to open the full preview. Remote images from other than known static hosts ask you to load the preview.
- **Website links** show an inline favicon beside their underlined label. GitHub links use a bundled, theme-aware mark; bare PR and issue URLs display as `PR #123` or `Issue #123`. Other public sites load `/favicon.ico` over HTTPS with a globe fallback.
- **Working bot**: three diamond tiles light in sequence beneath the avatar as it leans into a hop. Core Animation moves the avatar inside a fixed footprint. Activity changes trigger reaches, tilts, and hops from the current pose and show the current activity icon. New activity rows appear immediately. Reduce Motion and motion-free themes keep it still.
- **Running activity** keeps duration text free of shimmer while elapsed time continues updating. The separate native highlight keeps moving while scrolling and is hidden under Reduce Motion or motion-free themes. Running and completed tool durations align at the right end of each chat activity row.
- **Completed activity** starts expanded when the response has no text or images; the activity disclosure can still be toggled.
- **Edit activity** can expand to a selectable, wrapped diff preview that scrolls vertically.
- **Reply files** combine delivered files and edit previews when their paths match exactly; diff counts reflect only available previews, not the complete working tree.
- **Long-running chats** keep preview rendering focused on the current reading window. Stored images load thumbnails as their rows come into view and load a larger image on demand when opened. Earlier messages remain available through chat history.
- **Transcript scrolling** follows new output only while you are at the bottom. Scrolling up keeps your reading position through streamed replies, new questions, and transcript refreshes; return to the bottom or choose the floating **Scroll to bottom** arrow above the composer to resume following. The arrow appears whenever you are away from the latest content and shows a count when new messages arrived, with an opaque background that keeps it legible over the transcript. A single travelling rim highlights unread messages or an active response; the down arrow stays still. The control eases into view and animates count changes. Loops stop under Reduce Motion, motion-free skins, or a hidden workspace. Completed assistant replies of every length create nearby text sections as needed while preserving their full height and selected text. Completed replies can keep their existing line wraps while you drag a divider and reflow at its final width. New sections enter the scroll view already sized for the current width. Conversation scrolling uses 240-row history pages and starts fetching older history before the local buffer runs out. The visible window stays bounded as adjacent messages prepare for scrolling. A requested page wakes preparation immediately, and rows appear in small batches that preserve the current reading position. Replies with tool activity and hidden entries also continue loading older pages. A session-scoped coordinator owns paging and navigation; unrelated workspace refreshes leave transcript snapshots unchanged. Bot turns running outside Herm update the newest rows without discarding older history you’ve loaded or jumping away from your reading position. Activity in other sessions and streaming activity outside the mounted history window also leave the visible transcript unchanged; returning to the live reply shows its current activity. Background tool progress updates session labels independently of approvals and failures. Requested history pages prepare during scrolling and stay pending until their measurements are ready; bounded in-memory height measurements survive row remounts. Long streaming replies reuse stable Markdown sections and prepare only changed chunks. Large updates, such as reopening an already-running reply, prepare their chunks in the background. Navigator history is reused across activity updates, and ordinary Markdown streaming avoids restarting visual-reply parsing tasks. Find shows matches from the loaded conversation first while it searches older history in the background. Older history stays out of the visible transcript until you select a result. Long message maps build in the background and reuse existing previews. Activity updates reach only the message owning the relevant bot dispatch. During manual scrolling, live replies defer text reflow and show the latest received text when scrolling settles. Jump to latest respects Reduce Motion and lands immediately if the window is hidden.
- Adjacent history prepares its text layout in small slices before it appears, creating measurement views only for uncached sections. During scrolling, each layout adds up to four ready messages from the prepared page. Prompt bubbles reuse their measurements and reserve leading space with a fixed inset. The current page stays visible while it prepares; an unusually slow preparation falls back to normal rendering so older messages remain reachable. The transcript pauses hover from native AppKit scroll events. Split panes update their own constraints when scrolling or refreshing content, reducing layout work in the surrounding window. Timeline updates its row window only when the buffered rows change.
- Scrolling resolves the mounted message positions in one batch. Loading older messages updates the transcript and search data directly. The composer and session rail update as their own controls and cards change.
- **Jump to message** sits on the left edge of wide conversations, with hover previews opening to the right. Find opens along the same left edge. Herm prepares message previews when either control needs them.
- **Reply activity**: tool steps fold into a summary when a reply finishes. Long streamed replies stay visible while final Markdown preparation yields to input. Matching text sections keep their selection, and opening or closing the steps updates the transcript in one layout change.
- **Message actions**: completed replies show Copy, Retry, and More, with timing metadata aligned to the right. More contains read aloud, branch, reply, pin/unpin, open in a tab, and forwarding to a bot. Active playback keeps a Stop control visible.
- **Bot replies** expand beneath their activity pill into padded cards with vertical breathing room and fully selectable text.
- **Pinned conversations** use Hermes' own pin, so pins are shared with Hermes Agent Desktop and `hermes sessions pin`. Drag a conversation within Pinned to reorder it using the animated insertion line. Pin changes appear after acknowledgement; older refreshes cannot undo them. Saved TUI sessions without an HTTP execution owner use Hermes' verified, profile-scoped pin/unpin command.
- **Action errors** appear in a popup with a red background at the bottom-right of the active Herm window or sheet. The close button accepts the first click while the workspace keeps keyboard focus. Session, model, group, Bot visibility, project, task, automation, memory, GitHub, source-control, and login-setting actions report failures with sanitized details. Background refreshes retain their inline unavailable or stale states.
- **Bot and activity previews**: click a known bot mention pill, a bot dispatch pill, or an activity row to open its own closable third-panel tab. Inspect the available bot profile and model, full dispatched task/reply, or tool input, output, arguments, timing, and changes. The preview action stays in the message bubble’s More menu; inline previews use clickable names and rows. Existing tabs are selected and refreshed instead of duplicated; unloaded data is labelled as a captured preview.

- **Message reading tabs**: use a message bubble’s **Open message in new tab** action to keep a completed message visible in a closable third-panel tab while you work. Tabs support Markdown and attachments, stay scoped to their conversation, and last for the current app run. Reopening the same message selects its existing tab. No backend patch is required.

- **Pinned messages**: pin or unpin saved user and assistant messages, then use **… → Pinned messages** to jump to them. Bubble actions refresh their session target when a conversation resumes under a new runtime ID. Accepted pins survive transcript-view replacement and remain scoped to the selected conversation. Pins live in Hermes and survive compression. They bookmark messages for navigation; they do not keep them in model context or protect them from deletion or rewind. Profiles and new branches have independent pin lists. Requires the message-pins backend patch in [docs/message-pins.md](docs/message-pins.md); stock runtimes show an unavailable notice.
  Hover over a pin in the popover or inspector to read its excerpt in a solid preview. Message pin updates open the pinned list after verification. Errors remain visible across refreshes until another attempt or conversation reset; an unavailable or mismatched reread leaves the saved state uncertain.
- **Dangerous-command approvals**: *Deny*, *Allow once*, or *Always allow*. *Always allow* is saved to the Hermes allowlist.
- **Split session panes**: drag a session from the sidebar into the chat area, or use **Open in Split View**, to work in up to three columns side by side. Each column is a tab group with its own transcript and composer. Click any tab to make it the active session; the header and session menu move to its column, and the inspector opens beside it. Drop onto a column to add a tab, or at the trailing edge to open a new column. New tabs and columns open beside the session you came from. Bot main chats split the same way from the Bots page, and group chats can be dragged in or picked from the **Group chat** menu as tabs. Tabs show the same status as the sidebar (working spinner, unread count), and Bot tabs show the Bot's avatar and name. Columns last for the current app run.
- **Pop-out conversations**: choose **Pop Out Conversation** from a session's, Bot's or group chat's context menu (or **Pop out conversation** in the Conversation actions menu) to move that conversation into its own small floating window, which you can drag to any screen. It shows the transcript and composer with the same chat tools as the main window (folder and worktree bar, ⌘F search, quota) and stays above other apps. Opening a message, file, tool call, or bot preview expands a panel beside the transcript. Clicking the session in the sidebar brings its window forward. Closing the window keeps any running work going in Hermes Agent, but discards an unsent draft and any queued follow-up prompts. Group chat rows also offer **Open in Split View**, like Bot rows.
  Covered conversation windows suspend transcript snapshot updates and Markdown prefetch until they are visible again. Hermes Agent continues the turn while the window is covered.

### Chat views

The chat sidebar has a **Search sessions** field for loaded session titles, previews,
and project names in the selected bot scope. Results include pinned and project
conversations beyond the ten recent rows. Clear the field or press Escape to restore
the normal sections. Search runs in the background against the loaded session index.

Use **Show sidebar sections** in the sidebar ellipsis to choose what appears. Only **Pinned** and **Projects** are enabled by default.
The menu stays open while you change multiple sections.
**Unread**, **Needs you** (approval), **Running**, and **Archived** open directly
in the list and follow the selected bot scope. Open **Archived** to load it and search its
conversations. Recents is always enabled. **Bot switcher layout** switches between
Bot rail and Bot menu.

Drag a conversation within **Pinned** to set its saved order. Recents and
Projects list conversations by last update. Hover over a project pill to see
its repository path.

The bold vertical ellipsis beside **Chat tiles** lets you choose **Bot menu** or **Bot rail**.
Horizontal and vertical three-dot menu icons use the same heavier weight across Herm.
Bot rail replaces the picker above the session list with a wider column and roomier rows for bot avatars and badges.
Click an avatar to switch bots, or choose the **All** tile at the top to see
sessions across profiles. Scroll to see more avatars and drag them to reorder the rail.
As in the picker, holding a dragged bot near or past the top or bottom of the list
scrolls to bots outside the visible area.
Hover over a bot in the rail to see a profile preview with its avatar, name,
role, and description.
Herm remembers the layout and shares the saved bot order with the picker.

Chats has two layouts: **List** (one conversation beside your sessions) and **Tiles**
(every session at once). Click **Chat tiles** in the Sessions header to open Tiles,
or **Show chat list** in the Tiles header to return to List. **Settings → Chat → Layout → Default chat
view** chooses which layout the Chats rail button opens. Tiles cover every bot's
loaded recent, pinned, project, and active sessions in one board, with no bot picker;
with several bots each tile shows its bot avatar and name. It is not a complete historical archive.
Opening a tile from another bot switches to that bot.
The **Ready to review** header has a **Mark all as read** button at its trailing edge that clears every tile listed there (respecting the search and project filters).

Tiles are grouped into **Needs you** (approval, question, failure), **In progress**,
**Ready to review**, and **Recent** (collapsed by default), using the same runtime and
unread states as Chats. The status filter shows each group's count; you can also filter
by project or search titles and previews. Large boards prepare updates and search results
in the background, keeping the previous tiles available while results load.

Tiles lead with the chat title and age, followed by a compact line for status, bot and project,
and a readable preview of the most recent saved reply (read from the latest eight
messages without activating the session). Click anywhere on a tile to open its chat.
Working tiles show the current tool and keep a steady order while they run.
On wide boards the filters share one row. In narrow windows the status filters
scroll beneath search and project selection. Reply fields and tile outlines highlight keyboard focus and follow the
selected skin. Cards appear and change status without fading. The header uses consistently
sized compact controls, a layout menu, bot avatars in the picker and its choices,
and New chat at the trailing edge. From a tile you can:

- **Answer requests**: approvals and single-choice questions show their buttons
  (for example *Allow once* / *Deny*) and send through the same path as the notch.
  Multi-question requests ask you to open the chat.
- **Reply** to an idle session without switching chats. Replies to a working session
  are disabled until its turn finishes.
- **Stop** a working turn that Herm's gateway owns. Runs started in another process,
  such as `hermes chat` in a terminal, show progress but cannot be stopped from Herm.
- **New chat** opens the regular composer in a focused modal above the tiles, using the
  selected bot. **Open workspace** moves it into the full conversation workspace.
- **Open** the full conversation by clicking the title. It opens in a sheet with the
  regular composer, attachments, and steering; **Open workspace** opens its full tools.

Activity refreshes with the workspace's ten-second poll; disconnected or failed reads
keep the tiles with a not-current notice.

### Chat composer

Chat keeps unsent text, attachments, context, and reply quotes with each session
while Herm is open. Switch sessions, pages, or bots and return to continue your
draft. Drafts are separate for each bot/profile and are cleared when Herm quits.
Drafts are saved during navigation; typing continues to update only the composer.
Short drafts keep the composer compact; it grows as text wraps.
In narrow chat panes, the composer toolbar wraps so the model, quota, context,
and send controls remain visible.
Typing a leading `/` immediately opens the command menu while Hermes loads its commands.

Background processes listed for the current chat can be stopped after confirmation,
even when the general activity capability probe is unavailable. Process output
continues refreshing after the turn finishes; Stop targets only that session's process.
The composer disclosure shows the running count and the latest running process output;
expand it to inspect process states and stop a running process.

The **Effort** control uses Hermes' model catalog to offer inputs for the selected
provider and model. Unsupported or unverified availability is shown in place;
open an unverified control to refresh. Session changes are confirmed by a Hermes
readback. New chats remember your last model and thinking choices for each
profile, including after a restart. They apply as session settings, separate from
Hermes’ global default. Offered inputs are not a promise of the final provider wire level:
Hermes or the provider may adjust them. When Hermes reports a different route
entry mapping, the control shows both values (for example, Ultra → Max).
Fast sends a quick sweep through the filled Effort bar. The composer’s lightning
icon uses the active skin’s accent with a faint pulse. The Fast label and icon
stay visible with Reduce Motion.

The composer’s **@** picker shows each bot’s actual name, with its description when available. Hover or click the context gauge to see usage, the estimated category breakdown, and the runtime’s compaction threshold with remaining tokens in a popover, without a separate hover tooltip. Older runtimes show when the threshold is unavailable.

- **Autocorrect in chat** is on by default. Change it in **Settings → Chat → Typing**. Native macOS spelling correction and continuous spell checking follow the languages available on your Mac; the setting applies immediately without replacing your draft or selection. It works without Apple Intelligence.
- **Suggested follow-ups** use Apple Intelligence on your Mac. After a reply, a suggestion can appear in the focused, empty composer. Press **Tab** to insert it as an editable draft without sending. Turn it off under **Settings → Chat → Typing**.
- **Live dictation** inserts recognized words and corrections into the draft without sending. Retry or dismiss recognition warnings while keeping the words already captured.
- **Removable context tray** keeps attached PRs, browser pages, files, and conversation excerpts beside the draft. Inspect or remove a chip before sending; attaching context preserves your text.
- **Steering during a turn**: guidance you type while Herm is working is added to the running turn at the next tool boundary.
- **Queued messages**: when the current conversation has queued messages, every subsequent send joins the end of that queue, including plain text during a running turn. New submissions also wait behind a redirect still awaiting Hermes' reply. During a turn, text and attachments queue together. Submitting clears the composer immediately while preserving images, PDFs, context, and reply quotes with the message.
- **Attachments**: files, pasted images, prompt snippets, several images or PDFs at once (up to 25 MB per PDF). PDFs are sent as original files for the agent to read, without requiring `pdftoppm`; sent images show previews and documents show file-type labels. Drop Markdown, text, source, and other files into the composer as removable attachments (up to 8 MB each); uploads require Hermes protected file attachment support. **Files** and **Images** open a native attachment picker; **Folder** opens a directory picker and inserts its path into the draft.
- **Video replies** play inline with native playback, seeking, volume, and fullscreen controls. Playback starts when you press Play and stops when the attachment leaves the view. Open and Download remain available; formats or codecs macOS cannot play show an unavailable message.
- **Model picker** grouped by provider, with search. A conversation's reported model can appear before the model catalog finishes loading; provider routing still comes from the catalog. **Edit available models… → Unselect All** hides every model except the active one; selections are saved locally.
- The composer shows the reported thinking level while the transcript and model catalog load. Thinking choices become available when the catalog loads.
- Provider labels in chats, model pickers, settings, and Usage include the provider icon. Completed replies show the reported provider and model below the response when Hermes supplies a turn receipt.
- Confirmed model switches appear inline in chat with the model, provider, and time. Notices come from Hermes session history and return when you reopen the chat.
- **Mixture of Agents**: Settings → Models & tools edits Hermes' MoA presets (reference models, aggregator, enabled). Enabled presets appear in model pickers as `MoA · <preset>`; while a MoA turn runs, advisor output, fan-out progress and the aggregating phase stream into the thinking block. Settings → Models & tools also sets the default thinking level for new sessions.
- **Context guardrails**: the composer shows context progress without a session token total. Its percentage measures the full context window; Hermes can compact earlier based on its configured token limit or other runtime triggers. During compaction, the composer shows **Compacting**, including during streaming turns, and refreshes usage afterward. Context usage is labelled normal, warning (80%), or critical (90%), with actions to branch, compress, or hand off.
- **Capture and reusable context**: attachments include window capture, saved prompts, and selected conversation
  excerpts. Large pastes become text-file context; Command-Shift-V keeps text editable.
  Command-V and the Paste menu accept copied files as compact file chips, even when
  the clipboard also includes a file icon preview.
  Optional app text is configured in **Settings → Privacy & safety → Window capture**.

### Voice mode: continuous spoken conversation

Voice mode is more than a microphone button for dictating a prompt. Speak with your agent, hear its replies, and continue the conversation without typing each turn.
The voice stage keeps worktree details out of the conversation view.

![Herm full voice mode speaking a reply, with helper orbs and live captions](docs/media/voice-speaking.webp)

- **Earlier spoken replies:** complete prose sentences begin synthesis while Hermes is still generating. The final response drains only the remaining text; cutting in or changing sessions discards queued speech. Structured output waits for completion so partial markup is not read aloud.
- **Conversation-focused requests:** voice uses a compact spoken-response instruction instead of the visual UI catalog, asks for concise replies, and encourages available background delegation for substantial work. Hermes still owns tools, persona, memory, and approvals; delegation depends on its configured capabilities.
- **Background completion announcements:** active-session task and subagent completions are spoken once, after the current reply or in a quiet microphone gap. They do not replace approval questions or speech already in progress.
- **Quick voice settings:** Open **Voice** from the rail’s gear menu to switch conversation voices, choose and preview a local voice, or adjust speaking speed. Install Kokoro or download Smart turn detection from the same menu. Natural suggests Kokoro for conversational English on supported Macs. Recognizer, language, wake word, acknowledgments, announcements, and activity cards are available there too.
- **Liquid Glass voice notch:** The open voice stage is translucent below the black camera housing, with one grouped set of call controls. It uses native Liquid Glass on macOS 26 and honors Reduce Transparency.
- **Voice settings layout:** Preference rows have extra space around their dividers to keep longer descriptions readable.
- **Voice model controls:** Settings → Voice exposes Hermes’ voice conversation provider, model, and reasoning effort. These affect subsequent spoken turns without replacing the main chat model. A faster configured model or lower reasoning effort can reduce model latency; provider audio latency still applies.
- **Smart turn detection:** Herm downloads the local model automatically at launch. Settings → Voice shows progress, and Cancel or Remove keeps it off until you choose Download.
- **Continuous conversation** with local speech recognition, voice activity detection, and Hermes-configured speech synthesis. Local recognition starts without waiting for backend recorder checks; Hermes' session recorder is used when local transcription is unavailable. Recognized requests submit after speech stops, including in a noisy room. Herm waits about two seconds after you stop speaking before committing a conversation turn and waits longer when your words trail off. This does not shorten Hermes model or synthesis latency.
- Voice belongs only to the session where you activate it. In Talk, switching conversations or leaving Voice mode stops capture and playback, including delayed audio that finishes synthesizing afterward. The always-on wake listener skips smart-turn analysis until a call is listening for a request. Spoken requests and reply voices stay with that conversation's Bot profile. Playback returns to listening when its audio finishes; failed requests or playback pause Voice mode and show the error in chat. Microphone startup failures appear on the voice stage with a Retry microphone action. Capture reconnects after sleep or an audio-device change while voice is still enabled. Muting the microphone releases capture, including during replies.
- **On-device speech input:** Settings → Voice shows the recognizer and language last used by the notch. Apple’s newer model installs automatically when supported. Its status appears in Voice Settings and the sidebar’s quick Voice menu. Change the speech language or select Classic Apple Speech if you want to compare. Hermes Agent’s speech-to-text provider settings do not change this notch path. Herm holds through short pauses, waits for the final transcript, and asks you to repeat an unfinished request rather than sending its live guess.
- **Voice acknowledgment:** On by default. Herm gives a spoken acknowledgment in the same voice as the answer. Apple Intelligence writes a phrase or a full sentence that fits the request on this Mac. If the answer is ready before the receipt starts, Herm goes straight to the answer. Muting replies also silences acknowledgments. Saying only the wake phrase gets “I’m listening,” even when the notch is already listening. Tool and skill activity stays on screen.
- **Speech-ready replies:** Herm speaks the prose without reading Markdown markers, fenced code, or visual directives. The chat keeps the formatted reply.
- **Spoken interruption and steering:** Speak over a reply to quiet it without canceling the task. Ask to read a preview option or give a correction while the agent works. Say “stop talking” to quiet the reply, “cancel the task” to stop the work, or “end the call” to close voice. The orb still lets you send, cancel, or resume directly.
- **A native voice stage** with an audio-reactive orb (Bots wearing a Herm face appear live at its core only when Hermes reports the `hermes-bots` plugin enabled; uploaded or generated avatars keep the plain orb), listening/thinking/speaking states, centered spoken-reply captions, subagent indicators, and labeled microphone, reply, interrupt, and end controls. The conversation stays centered without floating activity cards covering captions or controls. Immersive mode gives the conversation the workspace.
- **Spoken approvals and clarifications** when on-device recognition is available. You can say “yes” or “I allow it” for **Allow once**, even while Herm is reading the request. For clarification, say an option name or “option two.” You can also join several options with “and” when the question allows it. Say “option two” or “choose” followed by the name to answer before the readout finishes. If sending fails, the notch keeps listening and lets you retry. The notch shows the request in its caption instead of a card. Spoken answers go to the current call’s pending request, and the interactive card stays in chat. A separate chat request queues behind the pending task without changing the decision. Local time and arithmetic questions can still be answered. If the decision isn’t clear, the notch briefly shows what it heard and keeps listening without repeating the readout. Questions such as “can you run it?” do not authorize execution. If an action was denied, ask Herm to try again to start a fresh attempt with its normal approval requirements. Permanent **Always allow** approvals still require the on-screen control.
- Talking over a local spoken reply stops playback and keeps the recognized words for your next request. Reply-echo filtering uses the currently spoken caption. No extra speech package or provider key is required.
- **Follow-up and wake behavior**: with on-device recognition, a 30-second quiet follow-up window can pause into wake-phrase listening. Say “Hey” followed by the displayed bot name or your custom wake name to resume.
- **Talk from any app**: press **⌥⇧ Space** (change it in Settings → Keyboard shortcuts) to start or end voice without opening Herm; the shortcut and notch mic open the notch assistant. General requests reuse your default bot’s existing main chat across calls while your workspace window or floating panel stays on its current view. If the main chat is unavailable, Herm asks you to open it and try again. Full voice mode also shows a live view of the agent's work beside the orb (the files it searched and the lines it read or changed, web results, the browser page, terminal output), rewritten on device by Apple Intelligence when available; say "open the browser" or "show the terminal" to see that tab there. Wherever Herm's panel is docked, voice appears at the top: a compact dark Liquid Glass widget grows out of the camera notch (or drops below the menu bar on a Mac without one) with your bot's face (its mood follows the conversation, and helper bots appear beside the status while they work), what's happening, and your words or the reply. Voice captions shift softly between turns while your live words update in place. The notch shows when the conversation is being compacted instead of saying “Thinking.” Approvals and open-ended questions use the caption. When a clarification has choices, the notch shows a read-only numbered preview so you can say the option name or number. When the answer has a visual (a chart, table or preview), it appears in its own floating glass panel below the top notch or beside a side notch, without repeating the spoken text or expanding the caption. The hands-free preview shows the read-only parts of a reply, including charts, comparisons, diagrams, timelines, and findings. Forms, checklists, commands, and live widgets are omitted from the voice preview. Both stretch and settle like liquid as they change size. It keeps the same dark look whatever skin Herm wears, floats over your desktop so the browser and terminal stay in their real windows, and provides mic and End voice controls. Minimize voice keeps the call running while you hover to open the quick notch. Click the mic in the quick preview to show the call again.
- **Faster, more accurate voice**: on macOS 26 Herm transcribes with Apple's newer on-device speech model (downloaded once; the classic recognizer is the fallback), primes it with your agent and helper names, uses alternate spellings only for wake matching, and waits for its final transcript before sending. Herm keeps the speech model’s corrections, including words it withdraws, and separates consecutive segments. Quiet or empty turns stay listening, and brief recognition failures are retried instead of immediately pausing. Speech recognition stays on the Mac; see [Voice on Apple's native speech stack](docs/voice-native.md). Spoken replies start on the first finished sentence, even when a visual follows. Use **Settings → Voice → Conversation voice** to select Hermes Agent, Apple Speech, Natural, or Kokoro. With a local voice, replies, timer announcements, and confirmations share your choice. See [voice setup and previews](docs/voice-native.md#choose-a-voice). With Apple Intelligence, **Understand commands with Apple Intelligence** recognizes short phrasings like “get rid of that” or “pull up the browser” on this Mac; anything else goes to the agent as you said it.
- **Optional wake word**: turn on **Listen for “Hey …”** in Settings → Voice → Wake word to start voice with “Hey” followed by your default bot’s name while Herm is idle; the voice stage opens in the notch and uses the same conversation as the notch mic. Start the utterance with the wake phrase. You can say the request in the same breath. The initial listening window closes after 30 seconds of quiet. Say “Stop listening” to end the call locally. **Wake name** overrides the bot’s name. With the default setting, “Hey Herm” also works. It's off by default. The Settings toggle and notch ear can ask macOS for speech and microphone permissions the first time you turn it on. Listening uses on-device recognition only. Herm listens for quieter wake phrases and checks alternate spellings for the full address. The collapsed side and top notches show a pulsing mic while listening and a steady mic while waiting to listen. A slash signals a microphone or speech recognition error. The side mic has extra space below it, and Reduce Motion keeps the indicator still. macOS shows its own microphone indicator while it’s on.
- **Hands-free previews:** Ask for a map of a named place and Herm looks it up in Apple Maps and shows the result in the voice preview, without opening Browser. Tables, diagrams, images, and videos from replies can appear in the same preview, along with read-only summaries of open approvals and recent activity. Videos don't autoplay. A preview stays visible when the reply finishes with the same visual. Say “show my calendar tomorrow” for a spoken summary and a paged agenda from your connected calendars. Use “next results,” “read row seven,” “read the second option,” or “zoom in” on supported previews. These commands work the same for built-in and AI-generated previews and don’t send a new chat message. Say “close the map,” “close the chart,” “close the table,” or “close the calendar” to dismiss it.
- **Hands-free commands from the notch**. The mic, voice shortcut, Command Palette’s Start Voice action, and opt-in wake word start listening on this Mac. General requests resume the default bot’s main chat in the notch when needed. Local answers use your selected local voice. Say “open Chrome outside Herm” or “open my default browser” to launch the separate Mac app without changing where the agent opens pages. “Open Browser” still selects Herm’s Browser tab. If Hermes is working or waiting for an answer, Herm keeps private commands local and asks you to repeat the command after the reply or prompt.
  - **Timers**. Say “set a coffee timer for five minutes,” “list my timers,” “how long left on coffee,” or “add two minutes to the coffee timer.” Canceling and extending ask for confirmation. Timer creation needs a connected local Hermes profile. Ask Herm to cancel a voice timer, or manage the job in Automations. Alerts use macOS notifications.
  - **Calendar and Reminders**. Grant access on Herm’s Calendar page, then ask “what’s next on my calendar,” “when am I free tomorrow afternoon,” or “block thirty minutes tomorrow morning for planning.” Say “add oat milk to my Groceries list due tomorrow” to create an Apple reminder. Herm reads back the destination before saving.
  - **Mac actions and work**. Try “open Downloads,” “what time is it in Manila,” “convert five miles to kilometers,” “what needs my approval,” “what finished today,” or “what changed since lunch.” Activity answers check recent history and say when that history could only be checked in part. “What finished today” reports completed replies. Say “add review the notes to my task board” to capture a Kanban task after confirming the board.
  - **Shortcuts, Mail, and Messages**. Bind installed shortcuts and optionally connect Contacts in Settings → Voice. Say “run shortcut” plus an alias, or “draft a message to Alex saying I’m on my way.” For email, add “subject” before “saying.” To send a draft, say “prepare to send,” listen to the full recipient, subject, and message readback, then say “send it.” If the readback is interrupted or muted, start the send request again with voice replies on. See the [sending shortcut setup](docs/voice-native.md#configure-mail-and-messages-shortcuts).
- **Assistant behaviors**:
  - **Reminders.** “Remind me in 10 minutes” becomes a one-shot Hermes job. It counts down in the collapsed top notch, and macOS delivers the scheduled alert even while Herm is closed.
  - **Briefing.** “Good morning” gets a briefing built only from your calendar, reminders, scheduled jobs, open approvals and running tasks. Only standalone briefing requests add that context. A source Herm can't read is named as not connected.
  - **Screen context.** With **Let voice see the front app** on, “Summarize this page” shares the front window’s title and text. Text capture skips known password managers and secure fields. Ask explicitly to attach a screenshot. The screenshot is shared only with that request. A “Seeing …” chip shows what was shared.
  - **Announce aloud.** With the wake word and **Announce aloud** on, Herm says when a bot needs you or finishes while no call is open, following Herm's Quiet mode.

  Screen context and Announce aloud are off by default. See [Assistant layer](docs/voice-native.md#assistant-layer).
- **Separate microphone and spoken-reply controls**, so you can mute input or turn off spoken replies.
- **Playback-aligned captions** show the same short segment sent to speech synthesis when its audio starts. Captions stay centered and wait during synthesis, rather than advancing on a reading-speed timer.
- **Live dictation** updates the composer as words are recognized, including corrections, without sending the draft. Recognition warnings offer Retry and Dismiss, clear on a new capture or session change, and keep any successfully recognized words.
- **Clearly labeled fallback** to macOS speech when Hermes voice support or dependencies are unavailable. The fallback is not a promise of the same continuous experience.

Opening or leaving other pages does not initialize microphone capture. Permission requests stop progressing when voice startup is cancelled. Voice mode requires microphone access; on-device recognition also requires macOS speech-recognition permission. Transcription and speech output depend on the installed Hermes runtime and its configured voice services. “Real-time” here describes the interactive spoken experience, not a claim of a provider-independent, full-duplex speech-to-speech transport.

Hermes Agent Desktop [also documents voice mode](https://hermes-agent.nousresearch.com/docs/user-guide/desktop). Herm's emphasis is its native voice stage and its integration with the rest of the agent workspace, not an exclusive claim to voice support.

### Pull requests

Pull request descriptions display task lists, separators, embedded HTTP(S) Markdown images and GitHub-style image tags, and common inline HTML (such as Dependabot release notes) as formatted text. Links on GitHub pages open in your default browser.

Selected pull request and issue cards use a themed fill and outline. Wide pull request summaries separate the description/activity column from the details sidebar with a themed vertical hairline.

![The Herm pull requests page](docs/media/page-pull-requests.webp)

- The pull request detail uses a ChatGPT-inspired open reading layout: Summary, Changes with line totals, and Reviews tabs; description and activity in the main column; and changes, reviewers, checks, readiness, and metadata on the right. Narrow panes stack the columns. The header separates the tabs from a labeled pull request actions row, which wraps in narrow panes. Compact tabs omit line totals, which remain in the summary. Expand Changes for file categories and partial-coverage notices. The Merge dropdown opens protected landing controls from the toolbar.
- On the standalone Pull Requests page, a floating bottom-right **Chat** panel uses the session chat’s composer, message bubbles, activity, and reply actions. Minimized and expanded chat float over the page without reserving a bottom strip. PR content remains visible around the panel in Summary, Changes, and Reviews. Each PR links to its own Hermes session under the default bot profile; reopening the PR, including after restarting Herm, resumes that conversation. PR context accompanies messages, and the selected workspace conversation and attachments stay separate. Minimize the panel or open its linked conversation in the workspace.
- Session **PRs** and **Issues** tabs appear when the session's local working directory belongs to a Git repository or worktree. They use the existing session chat instead of a floating panel. **Attach to chat** adds the PR as a removable context chip without sending, switching sessions, or replacing your draft. Reattaching refreshes the chip. On the standalone Pull Requests page and the repository overview, the **Attach to chat** icon offers a new chat or a recent one.
- Session PR and issue lists clear the previous repository's rows and selection when switching repositories. If a refresh fails for the same repository, retained rows are labeled as last loaded and can be refreshed again.
- Attached context appears once in the composer’s removable chip tray. PRs, browser pages, files, and other context no longer also insert a copy into your message text. Existing inline context moves to the tray without losing its contents.
- Minimized PR chat collapses to a small **Chat · #PR** button, hiding both the conversation and composer. Click it to reopen and focus the composer; drafts and attachments are kept.
- Pull request rows separate repository, title, branch, and status, with a visible selection marker. Lifecycle and readiness colors adapt to the active theme. Summary status controls include state icons, and description text keeps a readable line width.

- PR summaries use a violet branch-route icon and baseline-aligned reviewer and conflict-warning icons. The reviewer picker provides a searchable, aligned checkbox list and reports when no reviewers match. Reviewer and metadata pickers center their initial loading indicators.
- Open pull requests for the session's repository, with check status, review state, blockers, and deep links. The **Merged** filter includes the repository's merged PRs from the last 14 days, including PRs by other contributors; unavailable merged history is reported without hiding open PRs.
- If a repository's open pull request list only partly loads, the session and attached-repository fallback keep the retrieved rows and show a warning. A complete refresh clears the warning.
- The session header shows Pull Requests only when the session is connected to a project or repository.
- Pull request filters adapt to narrow panes with a compact selection menu; session search stays in the full-width first row, matching the Issues layout.
- Pull request and issue headers provide one GitHub open button; the actions menu keeps editing and Copy link.
- Summary, Changes, and Reviews tabs keep their full clickable area when the detail header shares the window title row.
- Reviews groups thread filters and feedback in clear sections, with an editor prompt, Markdown preview, and character limit.
- Newly opened diff files start at the left edge, with source visible beside the line-number gutter.
- The Changes tab centers its 