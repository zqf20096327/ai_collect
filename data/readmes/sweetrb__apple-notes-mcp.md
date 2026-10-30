# Apple Notes MCP Server

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that lets Claude (Claude Code and Claude Desktop), Codex, and other MCP clients read, search, create, edit, organize, and export notes in Apple Notes on macOS. It runs locally on your Mac and talks to Notes through AppleScript, Apple Shortcuts, and read-only access to the Notes database.

Beyond creating and editing notes, it manages folders and accounts, native tags, checklists, tables, pinned notes, links, and attachments. It can also export notes as Markdown (through templates you can edit in a local web editor), HTML (with classic drawings as SVG), or JSON, read audio transcripts and drawings, link to single paragraphs with anchors that survive edits, and run a query language across your whole library.

[![npm version](https://img.shields.io/npm/v/apple-notes-mcp)](https://www.npmjs.com/package/apple-notes-mcp)
[![npm downloads](https://img.shields.io/npm/dm/apple-notes-mcp)](https://www.npmjs.com/package/apple-notes-mcp)
[![node](https://img.shields.io/node/v/apple-notes-mcp)](https://www.npmjs.com/package/apple-notes-mcp)
[![CI](https://github.com/sweetrb/apple-notes-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/sweetrb/apple-notes-mcp/actions/workflows/ci.yml)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/sweetrb/apple-notes-mcp/badge)](https://scorecard.dev/viewer/?uri=github.com/sweetrb/apple-notes-mcp)
[![platform: macOS](https://img.shields.io/badge/platform-macOS-111?logo=apple&logoColor=white)](https://www.apple.com/macos/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MCP](https://img.shields.io/badge/MCP-server-blue)](https://modelcontextprotocol.io)

<p align="center">
  <img src="https://raw.githubusercontent.com/sweetrb/apple-notes-mcp/main/codex/assets/screenshot.png" alt="Apple Notes MCP — create, search, and organize Apple Notes from Codex, Claude, and other AI assistants" width="680">
</p>

## Contents

- [What is This?](#what-is-this) · [Setup on your Mac](#setup-on-your-mac) · [Requirements](#requirements) · [Features](#features)
- [Tool Reference](#tool-reference): [notes](#note-operations), [folders](#folder-operations), [accounts](#account-operations), [batch](#batch-operations), [export, attachments, and media](#export-operations), [diagnostics](#diagnostics), [native background operations](#native-background-operations), [private helper](#private-helper-opt-in-unsupported-apple-api)
- [Usage Patterns](#usage-patterns) · [Installation choices and upgrades](#installation-choices-and-upgrades) · [Server settings](#server-settings) · [Full Disk Access](docs/FULL-DISK-ACCESS.md) · [Public native helper](#public-native-helper) · [Permission broker](#permission-broker-opt-in)
- [Security and Privacy](#security-and-privacy) · [Known Limitations](#known-limitations) · [Troubleshooting](#troubleshooting) · [Recurring macOS permission prompts](#recurring-macos-permission-prompts) · [Development](#development)

## What is This?

This server acts as a bridge between AI assistants and Apple Notes. Once configured, you can ask Claude (or any MCP-compatible AI) to:

- "Save this conversation as a note called 'Meeting Summary'"
- "Find all my notes about the project deadline"
- "Read my shopping list note"
- "Move my draft notes to the Archive folder"
- "What notes do I have in my Work folder?"

The AI assistant communicates with this server, which then uses AppleScript to interact with the Notes app on your Mac. Some features also use packaged Apple Shortcuts (native tags, checklists, tables, pinning) or read the Notes database read-only (queries, checklist state, transcripts). Notes operations and speech recognition run locally. If you explicitly enable `downloadAssets: true`, the public helper may download speech models; what your MCP client does with tool results is up to that client.

<a id="quick-start"></a>

## Setup on your Mac

Apple Notes MCP runs on the Mac that holds your Notes library. Your assistant starts a local MCP server over **stdio**, and the server uses AppleScript, signed Apple Shortcuts, and read-only database access. Choose one client setup below, then complete the macOS permissions and optional feature setup you need.

**Version boundary:** these instructions describe v2.15.1, including the optional [permission broker](#permission-broker-opt-in). Normal client registration starts an in-process server unless a matching broker is already installed and answering. Broker installation is a separate opt-in step.

Manual client entries, setup commands, and the source checkout below select v2.15.1. Run setup from the same release as the server your client actually launches. The Claude Code plugin bundles its server; the Codex plugin manifest launches an unpinned npm package even when its marketplace is pinned. For reproducible Codex setup, use the manual registration below instead of the plugin. When upgrading, update the selected version consistently in the client and setup commands.

Run each setup target separately and use the exact options shown. Version 2.15.1 does not reject all unknown or mixed setup flags; a misspelled target can fall through to Shortcut setup and open import windows.

### Requirements

- macOS with Notes.app and at least one configured Notes account. Features depend on the installed macOS version and account type; inspect `get-capabilities` before relying on optional features.
- Node.js 20 or newer. The `npx` examples also need npm, normally included with Node.js.
- A client that can launch a local stdio MCP server on this Mac. The configurations below cover Claude Code, Claude Desktop, Codex, Hermes, and Antigravity.
- Automation permission to control Notes.app for AppleScript operations. Database-backed operations also need Full Disk Access for the process macOS holds responsible for the server.
- Apple Shortcuts for native writes such as native tags, checklists, tables, pinning, and rich append. The optional native Markdown creation route needs macOS 26 or newer and an iCloud account.
- An Apple developer toolchain only if you choose to build an optional native helper or permissions window. The public helper needs a current Swift toolchain and macOS SDK that expose the macOS 26 speech APIs; older SDK compatibility is unverified.

Python is **not** an Apple Notes MCP runtime dependency. The package includes its compiled JavaScript server and signed Shortcut files. Python is used by developer scripts that regenerate those workflows, not by normal installation or MCP tool calls.

You do not need an Apple ID password, API key, or NotesCTL installation to configure this server. A client's own login and tool-approval policy are separate from macOS privacy permissions.

### 1. Choose one client registration

Use either a plugin or a manual MCP entry for the same client. Registering both can load duplicate servers or leave you using a different package version than expected. Adding a client entry does not grant macOS permissions or import Shortcuts.

#### Claude Code

For the plugin, run these commands inside a Claude Code session:

```text
/plugin marketplace add sweetrb/apple-notes-mcp#v2.15.1
/plugin install apple-notes@apple-notes-mcp
```

The plugin bundles the server and the Apple Notes skill. For a manual MCP registration instead, run this in your terminal:

```bash
claude mcp add apple-notes -s user -- npx -y apple-notes-mcp@2.15.1
```

Check the connection with `/mcp` in Claude Code. `claude mcp get apple-notes` inspects the manually registered server. Project-scoped `.mcp.json` entries require workspace/server approval and can override a user-scoped entry.

#### Claude Desktop

Open **Settings → Developer → Edit Config**. Merge the following server entry into `~/Library/Application Support/Claude/claude_desktop_config.json`, preserving any existing servers:

```json
{
  "mcpServers": {
    "apple-notes": {
      "command": "npx",
      "args": ["-y", "apple-notes-mcp@2.15.1"]
    }
  }
}
```

Fully quit and reopen Claude Desktop. This `npx` route does not require a preceding global npm installation. If the desktop app cannot find `npx`, use an absolute executable path or the fixed Node configuration below. The desktop app may have a different `PATH` from your interactive shell.

#### Codex

For the plugin and its Apple Notes skill:

```bash
codex plugin marketplace add sweetrb/apple-notes-mcp --ref v2.15.1
codex plugin add apple-notes@apple-notes-mcp
```

For a manual MCP registration instead:

```bash
codex mcp add apple-notes -- npx -y apple-notes-mcp@2.15.1
```

The equivalent entry in `~/.codex/config.toml` is:

```toml
[mcp_servers.apple-notes]
command = "npx"
args = ["-y", "apple-notes-mcp@2.15.1"]
```

If `codex` is not on your terminal's `PATH`, use the desktop client's **Settings → MCP servers → Add server**: choose **STDIO**, enter `npx` with arguments `-y` and `apple-notes-mcp@2.15.1`, save, and restart the server.

Restart the relevant local Codex session or client. Use `/mcp` in the CLI or the client's MCP settings to inspect the connection. `codex mcp list` lists manually configured servers. The desktop client, CLI, and IDE extension share the Codex configuration; select local execution on the Mac containing your Notes library.

The plugin's server entry runs the published npm package through unpinned `npx`, despite the marketplace ref above. Its server may therefore differ from v2.15.1. Use the manual entry to pin the runtime for these instructions, or run setup from the release matching the plugin's actual server. This is a different distribution path from the Claude Code plugin's bundled server.

#### Hermes

Register a local stdio server:

```bash
hermes mcp add apple-notes --command npx --args -y apple-notes-mcp@2.15.1
```

Or merge this entry into `~/.hermes/config.yaml`:

```yaml
mcp_servers:
  apple-notes:
    command: npx
    args: ["-y", "apple-notes-mcp@2.15.1"]
```

Restart the Hermes session. This repository supplies an MCP configuration route for Hermes; see its [CLI commands](https://hermes-agent.nousresearch.com/docs/reference/cli-commands#hermes-mcp) and [MCP configuration reference](https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference).

#### Antigravity

In the IDE, open **MCP Servers → Manage MCP Servers → View raw config**. Merge the same `mcpServers` JSON entry shown for Claude Desktop into the global `~/.gemini/config/mcp_config.json`, or use the workspace configuration at `.agents/mcp_config.json`. Refresh or restart the client so it loads the server. Google's [MCP guide](https://antigravity.google/docs/mcp) describes the current menu and configuration paths.

The repository's `.antigravity-plugin/mcp_config.json` supplies an unpinned stdio server entry; the JSON above pins the audited release. Use `command` and `args`; this package does not provide a remote `serverUrl`.

#### Gemini Spark (macOS Local MCP)

In Gemini macOS builds that offer **Local MCP**, open **Connected Apps**, click **+ Custom**, and select **Local MCP** in "Set up a custom connected app". Fill in the form with:

| Field | Value |
|-------|-------|
| Server Name | Apple Notes |
| Description | Read, search, create, edit, organize, and export Apple Notes on this Mac. |
| Command | `npx -y apple-notes-mcp@2.15.1` |

You can print these instructions from the installed server:

```bash
npx -y apple-notes-mcp setup --gemini-spark
```

The command only prints the guide. It exits before loading server configuration, checking Notes, or running the other setup commands, and it doesn't register the app or change permissions. Exit 0 means the guide was printed, not that Gemini connected. Run it by itself; combining it with other setup options exits 2.

Keep **Sandbox settings** at **Default** initially, then click **Next** and review the discovered tools and permission requests before connecting. If Gemini can't launch the server, inspect **Show Logs** and check whether `npx` is available to the app. For a stable local installation, `npm install -g apple-notes-mcp` provides the `apple-notes-mcp` command; you can also use absolute paths to your Node executable and the installed `build/index.js` if the app can't find them. Keep that installation available, and update the command if you move it or replace Node.

Gemini's sandbox and macOS permissions are separate. Review any additional filesystem access the launcher needs; **Full Access** isn't a required setup step. Automation of Notes.app enables the AppleScript tools, while database tools need the runtime's [Full Disk Access](#full-disk-access). Shortcut operations need the packaged bridge setup above. After connecting, ask Gemini to run `get-capabilities` for tool availability, then `doctor` for Notes access diagnostics before attempting a write. A successful terminal check doesn't verify the permissions of Gemini's process.

This integration uses the Mac app's Local MCP command interface and the server's existing stdio transport. Availability depends on your Gemini build. Google's [custom apps documentation](https://support.google.com/gemini/answer/17209137) currently describes URL-based setup in the web app; it doesn't document this local form. **Cloud MCP**, Gemini web/mobile, and a hosted HTTP endpoint aren't supported by this server. These instructions apply to Gemini Spark, separately from Gemini CLI and Antigravity.

#### Other MCP clients and remote execution

A local MCP client can use the command `npx` with arguments `-y` and `apple-notes-mcp@2.15.1`. Follow that client's stdio configuration format: JSON `mcpServers`, TOML, and YAML are not interchangeable.

Apple Notes MCP has no built-in HTTP, SSE, WebSocket, or OAuth MCP endpoint. A cloud-only client cannot access your Mac's Notes library merely by installing the npm package in a Linux container or entering a URL. A separately managed transport bridge or client feature that delegates tool execution to your Mac needs its own configuration and security review; it is not part of this package's supported setup. GUI reveal and clipboard tools also need your logged-in desktop session.

The optional `anchors serve` command is a paragraph-link resolver, and `templates edit` is a template editor. Neither is a remote MCP server.

<a id="full-disk-access"></a>
<a id="permissions-check"></a>

### 2. Verify the server and macOS access

In the configured client, ask it to run `get-capabilities` and then `doctor`. `get-capabilities` inspects feature availability without opening Notes or running the bridges. `doctor` also sends a read-only Apple event to Notes and may trigger the macOS Automation prompt. Run these from the actual client because a successful terminal check does not establish that a different desktop app has the same permissions.

| Access or component | What it enables | How to complete it |
|---|---|---|
| Automation of Notes.app | AppleScript reads and writes | Allow the macOS prompt for the responsible app to control Notes. Inspect **Privacy & Security → Automation** if access was denied. |
| Full Disk Access | Database reads, rich-content inspection and safety checks, query tools, native object reads, and database-backed exports | Add the responsible executable/app under **Privacy & Security → Full Disk Access**, fully quit and relaunch the host, then rerun `doctor`. |
| Shortcut installation and consent | Native tag, checklist, table, pin, link, and append routes | Import the bridges and complete their foreground consent steps below. |
| Public helper and, where required, Speech Recognition | Classic drawing decoding and on-device audio transcription | Build the optional helper; follow the permission result from `doctor` or the tool. |

**Which process needs Full Disk Access?** For a brokered session, grant the signed **Apple Notes MCP Broker.app** access; `doctor` reports whether that session uses it. Without the broker, Claude Desktop needs the exact **Node executable** printed by `doctor`; granting Claude.app alone does not reach the server in that launch path. For a terminal-launched client, the terminal app is normally the responsible app; for an editor-launched server, check that editor. Use the actual running client's diagnostics instead of assuming that all clients share grants.

Client sandbox access is a separate boundary. A sandboxed client must be able to launch the executable and reach its files; a brokered client also needs access to the broker's local Unix socket. Full Disk Access and Automation grants do not expand the client's sandbox. Diagnose a launch or socket-access refusal in the client before changing macOS privacy permissions.

To inspect setup from a terminal without opening permission panes or requesting Automation access:

```bash
npx -y apple-notes-mcp@2.15.1 setup --permissions --check --json
```

The Automation result is intentionally unknown in this mode. When you are at the Mac and want to check it, this command sends a read-only Apple event and may show the macOS consent prompt:

```bash
npx -y apple-notes-mcp@2.15.1 setup --permissions --once --probe-automation
```

For an interactive checklist that also opens the relevant settings panes:

```bash
npx -y apple-notes-mcp@2.15.1 setup --permissions --open --probe-automation
```

The command checks permissions; it does not grant them. `--check` and SSH sessions suppress the Automation probe even when `--probe-automation` is supplied. Without the probe, exit status 0 does not establish Automation access.

Full Disk Access is optional if you only need operations that can safely run through AppleScript, but many capabilities and safety checks depend on it. It can also be required by guards on existing-note writes, including rich-content and revision verification; it is not merely an enhancement for read tools. Do not interpret an unavailable database-backed feature as an empty result. In particular, sync results without database visibility do not prove that iCloud sync is idle. Use the tool reference and `get-capabilities` for individual requirements, and see the [Full Disk Access guide](docs/FULL-DISK-ACCESS.md).

### 3. Enable the native Shortcut features you need

Run explicit setup on your Mac:

```bash
npx -y apple-notes-mcp@2.15.1 setup
```

Approve **Add Shortcut** for the missing signed workflows that macOS opens:

- `Apple Notes MCP - Native Tags`
- `Apple Notes MCP - Background Operations v5`
- `Apple Notes MCP - Create Markdown Note`, offered only on macOS 26 or newer and optional for native Markdown creation

Then check installation:

```bash
npx -y apple-notes-mcp@2.15.1 setup --check
```

The first two bridges determine this check's readiness; the optional Markdown bridge is reported separately. Keep only one installed copy of each named bridge. The server refuses duplicate bridge names.

After installation or upgrade, run each installed bridge once in the foreground in Shortcuts.app and answer its access prompts. Choose **Always Allow** if you want that bridge to run unattended. For the Markdown bridge, use the first-run request in [`shortcuts/README.md`](shortcuts/README.md); running it without input stops before it asks Notes for access. That request creates a disposable check note.

An installed bridge is not proof of consent: `shortcuts list`, `setup --check`, and `doctor` cannot observe the first-run consent state. A background native write can stall on an unanswered prompt. After a timeout or an indeterminate write result, read the exact note before retrying because the write may already have happened.

### 4. Build optional helpers

These commands are separate from registering the MCP client. If `xcrun swiftc` or `clang` is unavailable, install Apple's Command Line Tools with `xcode-select --install` before building a helper. The public helper's source references `SpeechAnalyzer` and `SpeechTranscriber`, so its build needs a current Swift toolchain and macOS SDK exposing those macOS 26 APIs. Runtime availability checks do not establish compatibility with an older SDK; builds with older SDKs are unverified.

#### Public native helper

<a id="public-native-helper"></a>

Needed for `get-note-drawings` and `transcribe-note-audio`. Brokered sessions do not load external helpers; set `APPLE_NOTES_MCP_BROKER=off` for this client and restart it before using these tools:

```bash
npx -y apple-notes-mcp@2.15.1 setup --public-helper
npx -y apple-notes-mcp@2.15.1 setup --public-helper --check
```

It compiles locally, signs ad hoc, verifies its handshake, and records source and binary checksums. The server refuses stale or modified helpers; rerun setup after a relevant package upgrade. This helper uses public Apple frameworks and does not open or write the Notes database. The server still needs Full Disk Access to read the drawing/audio assets it passes to the helper.

On older macOS versions, speech transcription needs Speech Recognition access for the responsible host. The helper never requests this silently. On macOS 26 and newer, the SpeechAnalyzer route has been observed to work without a prior grant; explicit denial or restriction still blocks it. Inspect the returned capability/permission status on your Mac.

#### Private helper setup

Optional read-only NotesShared state inspection, disabled by default. Brokered sessions do not load this helper; set `APPLE_NOTES_MCP_BROKER=off` for this client and restart it first:

```bash
npx -y apple-notes-mcp@2.15.1 setup --native-helper
npx -y apple-notes-mcp@2.15.1 setup --native-helper --check
```

To enable it, set the string environment value `APPLE_NOTES_MCP_ENABLE_PRIVATE=1` for the server and restart the client. Inspect `native-helper-status` before using `native-note-state`. This released helper opens the store read-only and cannot provide deep native writes. Apple's private API may change with macOS updates; the remaining server features do not require this helper.

#### Optional checklist window

Optional graphical presentation of the checklist:

```bash
npx -y apple-notes-mcp@2.15.1 setup --permissions-window
npx -y apple-notes-mcp@2.15.1 setup --permissions --window
```

It displays the command's checks and opens settings on request. It does not become the permission owner or replace the client process.

### 5. Confirm the capabilities you intend to use

After restarting the client, run `doctor` and `get-capabilities` again. Confirm that the specific routes you need are available, not just that the server connected. Private helper status, public helper readiness, Markdown creation, and the native-write bridges are separate checks.

Use read-only operations first, such as listing accounts/folders and reading a note you select. If you want to exercise a write route, use a dedicated disposable note and verify the result by its exact ID. A successful plain note creation does not validate native tables, checklists, or Markdown creation; test the feature you plan to use.

Keep the server's revision and scope checks enabled. Updates, appends, and deletes use exact IDs and content hashes; native routes may also require a distinctive existing `scopeText`. Full-body updates refuse rich notes they cannot preserve. Follow the returned error and capability information instead of falling back to a lower-level write.

## Features

| Feature | Description |
|---------|-------------|
| **Create Notes** | Create notes from plaintext, HTML, or Markdown, with optional folder/account targeting (Markdown creation uses an optional Shortcut on macOS 26 or later) |
| **Search Notes** | Find notes by title or search within note content |
| **Query Language** | `query-notes` combines text, folder, account, tag, attachment, checklist, flag, word-count, and date conditions with AND/OR/NOT, read from the Notes database (requires Full Disk Access) |
| **Read Notes** | Retrieve note content as HTML, plain text, or Markdown, plus metadata that AppleScript does not expose (pinned, Quick Note, locked, Recently Deleted) |
| **Note Structure** | Decode a note into typed paragraph blocks, list its paragraphs and links, and get a direct link to one paragraph (requires Full Disk Access) |
| **Update Notes** | Replace, append to, or prepend to an existing note, guarded by a content hash so a note that changed since it was read is never overwritten |
| **Delete Notes** | Remove notes (moves to Recently Deleted) |
| **Move Notes** | Organize notes into folders (supports nested paths) |
| **Folder Management** | Create, list, rename, and delete folders with full hierarchical path support; read the folder tree with note counts and Smart Folder rules |
| **Multi-Account** | Work with iCloud, Gmail, Exchange, or any configured account, including account IDs and default folders |
| **Batch Operations** | Delete or move multiple notes at once |
| **Native Tags** | List, add, remove, and replace real Notes tags (not just `#hashtag` text) |
| **Checklists** | Read checklist done/undone state from the Notes database, and append real checklist items through a Shortcut |
| **Tables** | Read native tables as Markdown and JSON, and append new native tables |
| **Pinning** | Read pinned state and pin or unpin a note |
| **Links** | Get a note's `notes://` deep link, insert web, mail, or note-to-note links, and list the links in a note or folder |
| **Export** | Export notes as paginated JSON, or render a note or folder as Markdown (with reusable templates) or standalone HTML |
| **Attachments** | Add files to notes (from a path or the pasteboard), list attachments with their on-disk paths, find a note's lead image, save or batch-export them, or fetch their bytes as base64 |
| **Audio and Drawings** | Read the transcripts Notes stored for recordings, transcribe audio on-device, and decode drawings to strokes and SVG |
| **Incremental Sync** | `list-recent-notes` pages through notes by modification time with an exact cursor |
| **Notes.app UI State** | Reveal a note, folder, account, or attachment in Notes.app, or read the current Notes.app selection |
| **Sync Awareness** | Detect iCloud sync in progress, warn about incomplete results |
| **Collaboration** | Detect shared notes, warn before modifying |
| **Diagnostics** | `health-check` plus a richer `doctor` (reachability, automation permission, accounts, Full Disk Access), sync status, statistics, and `get-capabilities` for the Shortcut bridges |

Read/list/get tools also return **structured JSON** (`structuredContent`) alongside the text, so agents can consume results without parsing prose.

Some clients (Claude Desktop among them) pass the model only a result's text
and drop `structuredContent`. So every result that has `structuredContent` also
ends with one more text block holding the same data as a single JSON line:

```
structuredContent: {"id":"x-coredata://…/ICNote/p123","contentHash":"sha256:…","writable":true,…}
```

That line carries every token a follow-up call needs: the `contentHash`
revision token for `expectedContentHash`, new ids, `nativeTags`, `writable`,
`page.nextOffset`, and an error's `code`, `committed` and `indeterminate`. A
long value the text above already shows in full, such as the body from
`get-note-content`, appears as `"[shown in full above]"` instead of twice. If
the line would still exceed 16 KB, fields larger than 1 KB (usually a list
already printed above) are left out and named in `_omitted`. Tools whose text
already is that JSON get no extra block. `structuredContent` itself is
unchanged.

### MCP resources & prompts

Resources expose read-only context the client can attach without a tool call:
`notes://accounts`, `notes://folders`, `notes://stats`, and the
`notes://note/{id}` template (returns the note as Markdown). Prompts package
common workflows: `find-note`, `weekly-review`, `new-meeting-note`.

### AppleScript limitations

A few Notes UI features are not exposed to AppleScript. Some are recovered by
reading Notes' own database instead; the rest genuinely cannot be supported. See
**[docs/APPLESCRIPT-LIMITATIONS.md](https://github.com/sweetrb/apple-notes-mcp/blob/main/docs/APPLESCRIPT-LIMITATIONS.md)**
for the investigation and verification behind each:

- **Pinned notes** — Notes has no scriptable `pinned` property via AppleScript. Pin state is **read** from the NoteStore database by the BETA `get-note-metadata` tool and `list-special-notes`, and **set** through the Background Operations Shortcut by [`set-note-pinned`](#set-note-pinned).
- **Note-to-note links** — AppleScript exposes no link property or link element. Links are instead read from the NoteStore database by [`list-note-links`](#list-note-links), and inserted by [`insert-note-link`](#insert-note-link) (through a Shortcut) or [`insert-link`](#insert-link). A shareable `notes://showNote?identifier=<uuid>` deep link is available via [`get-note-link`](#get-note-link).

---

## Tool Reference

This section documents all available tools. AI agents should use these tool names and parameters exactly as specified.

### Identifier forms

Every tool that takes a note id (`id`, `noteId`, `ids`, `linkedNoteId`, or the `id` inside a batch entry) accepts any of three forms of the same note:

| Form | Example shape | Needs Full Disk Access |
|------|---------------|------------------------|
| AppleScript id (canonical) | `x-coredata://<store-uuid>/ICNote/p123` | No |
| Notes UUID (`identifier`) | `8-4-4-4-12` hex digits, as in `notes://showNote?identifier=` links | Yes |
| Numeric Core Data key | `123` (the digits after `p`) | Yes |

The server turns a UUID or numeric key into the canonical id before the tool runs, reading the Notes database read-only. A numeric key or UUID resolves only to a note, never to a folder or attachment. Without Full Disk Access those two forms fail with an error that says so, while `x-coredata` ids keep working as before. Folder-id inputs (`show-folder`, `get-folder-by-id`, `rename-folder`) accept a folder's UUID or numeric key the same way, resolving only to folders.

When Full Disk Access is granted, list and read tools also return stable identifiers next to each `id`: notes carry `identifier`, `folderIdentifier`, and `accountIdentifier`; folders carry `identifier`, `parentIdentifier` (nested folders only), and `accountIdentifier`; accounts carry `identifier`. These fields come from one batched read-only query per call and are omitted when the database cannot be read. Tools that return them: `search-notes`, `list-notes`, `get-selected-notes`, `list-shared-notes`, `get-note-content`, `get-note-by-id`, `get-note-details`, `list-folders`, `get-folder-by-id`, `list-accounts`, and `get-default-location`.

### Error results

A failed call returns `isError: true` with the same human-readable text as
before, plus `structuredContent` carrying a stable machine-readable `code`
(also repeated in the trailing `structuredContent:` text line, for clients
that drop `structuredContent`).
Branch on `code`, not on the prose, which may be reworded.

| `code` | Meaning |
|--------|---------|
| `not_found` | The note, folder, account, attachment, or checklist does not exist |
| `ambiguous` | More than one item matched; use an exact id |
| `permission_denied` | macOS refused Automation access to Notes.app |
| `full_disk_access_missing` | The Notes database is not readable; grant Full Disk Access |
| `shortcut_not_installed` | A native-write bridge Shortcut is not installed exactly once |
| `timeout_indeterminate` | The operation timed out; for a write, the outcome is unknown |
| `verification_failed` | The write ran, but exact-ID readback did not confirm it |
| `revision_conflict` | The note changed since it was read |
| `validation_error` | The request was rejected before anything ran |
| `unsupported` | Not supported for this note or in this mode, such as a locked note |
| `notes_unavailable` | Notes.app is not running, busy, or not responding |
| `operation_failed` | The server could not classify the failure; read the text |

Two optional booleans describe a write's outcome when it is known.
`indeterminate: true` means the outcome is uncertain: read the target by exact
id before any retry, and never retry blindly. `committed: true` means the write
took effect even though its verification failed; `committed: false` means
nothing was written (for example a `revision_conflict`). An absent flag means
unknown. An argument that fails the input schema is rejected before the tool
runs, with `code: "validation_error"` and `committed: false`. The exception is
a Notes UUID or numeric key that could not be resolved to an id: it carries
`not_found`, or `full_disk_access_missing` when the database is unreadable.

### Note Operations

#### `create-note`

Creates a new note in Apple Notes.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `title` | string | Yes | The title of the note. Automatically prepended as `<h1>` — do NOT include the title in `content` |
| `content` | string | One of `content`/`contentPath` | The body content of the note (do not repeat the title here) |
| `contentPath` | string | One of `content`/`contentPath` | Absolute path of a local UTF-8 file to use as the body instead of `content`. Allowed in the same places [`save-attachment`](#save-attachment) may write (home, temp, `/Volumes`), except hidden paths (any component starting with `.`, such as `~/.ssh` or a project `.env`) and `~/Library` other than iCloud Drive (`~/Library/Mobile Documents`) and cloud storage folders (`~/Library/CloudStorage`), which can hold credentials; set `APPLE_NOTES_MCP_ALLOW_PRIVATE_CONTENT_PATHS=1` to allow those. Symbolic links, non-regular files, invalid UTF-8 and files over 1 MiB are refused before anything is written. A leading byte-order mark is dropped |
| `tags` | string[] | No | Returned-only metadata — **NOT written to Notes.app**. Apple Notes tags can't be set via AppleScript, so values passed here are echoed back in the response but do not appear on the created note. Inline `#hashtags` in `content` stay searchable text and are returned as `hashtags`, but they do not become native Notes tags; add real tags afterwards with [`add-native-tags`](#add-native-tags). Refused with `format: "markdown"` |
| `folder` | string | No | Folder to create the note in. Supports nested paths like `"Work/Clients"`. **The folder must already exist** — create it first with [`create-folder`](#create-folder). A smart folder is refused (see [`move-note`](#move-note)). Defaults to account root |
| `account` | string | No | Account name (defaults to Notes.app's default account; matched exactly or by a *unique* prefix — an ambiguous prefix is refused). Must be an account Notes.app already has configured — see [`list-accounts`](#list-accounts) |
| `format` | string | No | Content format: `"plaintext"` (default), `"html"`, or `"markdown"`. In all formats, the title is automatically prepended as the note's title line. In plaintext mode, newlines become `<br>`, tabs become `<br>`, and backslashes are preserved as HTML entities. `"markdown"` produces real Title/Heading/Subheading styles through a Shortcut; see [Markdown notes](#markdown-notes) |
| `markdownRoute` | string | No | With `format: "markdown"` only: `"shortcut"` (default) or `"html"`. See [Markdown through HTML](#markdown-through-html) |
| `timeoutSeconds` | number | No | Whole seconds, 1–120, for each Notes.app automation step this call runs; overrides `APPLE_NOTES_MCP_TIMEOUT_MS` for this call only. A timed-out write is uncertain, not failed: read the note by id before any retry. Also accepted by `get-note-content`, `update-note`, `append-to-note`, `delete-note` and `move-note` |

**Example (with inline textual hashtags):**
```json
{
  "title": "Meeting Notes",
  "content": "Discussed Q4 roadmap and budget allocation\n\n#work #meetings"
}
```

**Example - Create in a specific folder:**
```json
{
  "title": "Client Meeting",
  "content": "Discussed project timeline",
  "folder": "Work/Clients"
}
```

**Example - HTML formatting:**
```json
{
  "title": "Status Report",
  "content": "<h2>Summary</h2><p>All tasks <b>on track</b>.</p><ul><li>Feature A: complete</li><li>Feature B: in progress</li></ul>",
  "format": "html"
}
```

> **Note:** The title is automatically prepended as `<h1>` in both plaintext and HTML formats. Do not include a `<h1>` title tag in the `content` parameter, or the title will appear twice.

> **Known limitation:** with `"plaintext"` or `"html"`, `create-note` sets the note
> body directly via AppleScript's `body` property, which does not apply real Notes
> paragraph styles for interior content — an `<h2>`/`<h3>` tag or a
> `<span style="font-size: …px">` heading span in `content` renders as plain bold,
> styled text, not an actual Heading or Subheading
> ([#172](https://github.com/sweetrb/apple-notes-mcp/issues/172)). Use
> `format: "markdown"` for real headings in a new note, or
> [`append-native`](#append-native)'s `format: "markdown"` on a note that already
> exists.

##### Markdown notes

`format: "markdown"` creates the note with Notes' own Markdown importer (the
Create Note action's "Interpret as Markdown" option, macOS 26+), run through the
packaged `Apple Notes MCP - Create Markdown Note` Shortcut. `#`, `##` and `###`
become real Title, Heading and Subheading styles, and the note starts with the
title line, with no seed line.

```json
{
  "title": "Project Plan",
  "content": "## Goals\n\n- Ship the beta\n- Collect feedback\n\n### Links\n\n[Tracker](https://example.com/tracker)",
  "format": "markdown",
  "folder": "Work"
}
```

- Notes interprets Markdown only in an iCloud account. The note is created in the
  iCloud account's default folder, then moved to `folder` in that account.
  `folder` must already exist and is checked before anything is created. If it
  exists only in another account, the note is still created and verified in the
  iCloud default folder, and the error names that account and the note's id so
  you can create the folder there and `move-note` it instead of creating the
  note again. `account` is refused with this format.
- `tags` are refused with this format. Create the note without them, then add
  native tags to the returned id with [`add-native-tags`](#add-native-tags).
- `content` accepts the same bounded subset as `append-native`'s Markdown:
  `#`/`##`/`###` headings, flat lists, `**bold**`, `*italic*` and inline links.
  It also refuses Markdown that Notes would rewrite and the server could not
  verify: `_` emphasis (underscores inside a word, as in `snake_case`, and
  inside a link destination, as in `[docs](https://example.com/_next/static)`,
  are fine), backslash escapes, character references such as `&amp;`, `===` lines
  and rule lines other than the `---` divider described below, indented headings or list items, `1)` lists, closing `#`s, and
  formatting inside link labels. Content that needs one of these literally, such
  as a `/_next` path or a literal `\*`, has no Markdown form here: use
  `format: "html"` for that note (or `append-native` with `format: "html"` on an
  existing one), which keeps the characters but not the Heading and Subheading
  styles. Markdown punctuation in `title` is escaped, so the title stays literal.
- Notes' importer also maps these block constructs to native styles. They are
  gated separately, and `get-capabilities` reports them as
  `create-note-markdown-blocks`. Each mapping below was live-verified on
  macOS 27.2 by reading the created note's stored styles.

  | Markdown | Native result |
  |----------|---------------|
  | `- [ ] item` / `- [x] item` | Checklist item, unchecked / checked |
  | `> text` (consecutive lines form one quote) | Body paragraph with a block quote |
  | A fence of bare ```` ``` ```` lines (no language) | Monospaced paragraphs; the code text is kept literally |
  | `---` on its own line, after a blank line | Divider line |
  | `` `inline code` `` | **Highlighted** text, not monospace |

  Constructs Notes would not render faithfully, or that this server cannot yet
  verify, are refused before anything is created: `~~~` fences, a language
  after the opening fence, nested (`>>`) or indented quotes, lists or headings
  inside a quote, a quote followed directly by text (Markdown would join that
  text to the quote), `---` directly under text (Markdown would make that text
  a heading), `***`/`___`/`----` rules, `[X]`, `* [ ]` or `+ [ ]` items, checklist
  items directly next to ordinary list items, inline code padded with spaces or
  inside a link label, tables, and `~~strikethrough~~`. The readback checks the
  block-quote text, the Monospaced text, each checklist item's text and done
  state, the divider count, and the highlighted text. These mappings apply to
  the default Shortcut route only; see
  [Markdown through HTML](#markdown-through-html) for `markdownRoute: "html"`.
- [`append-native`](#append-native)'s `format: "markdown"` refuses all of the
  constructs above: its Shortcuts converter is a different one, which renders
  a quote and a fenced block as plain body text, `- [ ]` as a bullet with
  literal brackets, and inline code as plain text, and drops `---`.
- The server finds the new note among the notes added to the default folder
  during the run by verifying each one's visible text, heading levels and links
  by exact-ID readback, and moves it only after exactly one verifies. On any
  uncertain result it names the note (or says to search for the title) and
  never retries.
- It is gated like the other native operations; `get-capabilities` reports it
  as `create-note-markdown`. The Create Markdown Note Shortcut is optional and
  needed only for this format (macOS 26+); install and approve it as described in
  [`shortcuts/README.md`](shortcuts/README.md).
- A first line that is exactly `# <title>` (same case and spacing as `title`) is
  removed together with one blank line after it, because the title is supplied
  separately; the response then carries `strippedDuplicateTitle: true`. A
  different first heading stays in the body. This applies to both Markdown
  routes, and Markdown that holds only that heading is refused.

##### Markdown through HTML

`markdownRoute: "html"` imports the same bounded Markdown subset without the
Shortcut: the server converts it to HTML and creates the note through AppleScript,
like `format: "html"`. It works in any account, accepts `tags`, and needs no
Shortcut, but headings get the plain bold styling described in the known
limitation above rather than real Heading and Subheading styles.

On this route, bullet task items (`- [ ] item`, `- [x] item`) become ordinary
list rows that start with a visible `☐` or `☑` character, and the response
reports how many as `taskItemsRendered`. They are text, not native checkable
checklist items. Use this route as the glyph fallback when the Shortcut is not
installed or the note is outside iCloud. Block quotes, fenced code and inline code, which
the Shortcut route maps natively, are refused on this route, and a `---` line
stays literal text rather than becoming a divider.

```json
{
  "title": "Weekly Review",
  "contentPath": "/Users/me/Documents/weekly-review.md",
  "format": "markdown",
  "markdownRoute": "html",
  "folder": "Work"
}
```

**Returns:** Confirmation message with note title and ID. Save the ID for subsequent operations like `update-note`, `delete-note`, etc.

---

#### `search-notes`

Searches for notes by title or content.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Text to search for |
| `searchContent` | boolean | No | If `true`, searches note content (title line included); if `false` (default), searches titles only. With Full Disk Access, content search reads the Notes database (well under a second, the 5000 most recently modified notes, Recently Deleted excluded); without it, it falls back to AppleScript, which scans every body and can time out on a broad term |
| `account` | string | No | Account to search in (defaults to Notes.app's default account; exact or unique-prefix match) |
| `folder` | string | No | Limit search to a specific folder (supports nested paths like `"Work/Clients"`) |
| `modifiedSince` | string | No | ISO 8601 date string to filter notes modified on or after this date (e.g., `"2025-01-01"`) |
| `limit` | number | No | Maximum number of results to return. **Defaults to 50** — a broad query reads several properties per match via AppleScript (~200ms/note), so an unbounded search over hundreds of matches can exceed Notes' 30s timeout and return an error instead of results. Pass a higher value to see more; the applied limit (and whether it truncated the results) is disclosed in the response. |
| `includeWordCount` | boolean | No | Add `wordCount` to each result (`null` when the note is locked or its body unreadable). A database content search already has the text. Otherwise the bodies are read in one batched read-only database query, never one AppleScript call per note; that needs Full Disk Access and also adds `matchedIn`. Without it, the response carries `wordCountUnavailable` and the results are unchanged. |

**Example - Search titles:**
```json
{
  "query": "meeting"
}
```

**Example - Search content:**
```json
{
  "query": "budget allocation",
  "searchContent": true
}
```

**Example - Search recent notes with limit:**
```json
{
  "query": "todo",
  "searchContent": true,
  "modifiedSince": "2025-01-01",
  "limit": 10
}
```

**Returns:** List of matching notes with titles, folder names, and IDs. Use the returned ID for subsequent operations like `get-note-content`, `update-note`, etc. A content search also returns `source` (`"database"` or `"applescript"`), and `scanTruncated` when the database path left older notes unsearched.

When the note text came from the database (a database content search, or any search with `includeWordCount`), each result also carries `matchedIn`: `["title"]`, `["body"]`, or `["title", "body"]`, saying where the query text occurs. The body is the text after the first line. `matchedIn` is absent for locked notes and for AppleScript searches without `includeWordCount`. The text output appends the same details to each line, for example `· matched in title, body · 245 words`.

**Example - Content search with word counts:**
```json
{
  "query": "budget",
  "searchContent": true,
  "includeWordCount": true
}
```

---

#### `query-notes`

Finds notes with a boolean query expression evaluated against the NoteStore
database, read-only. Because it does not go through AppleScript, a query over
several hundred notes typically returns in well under a second, and one call
can match titles and bodies together.

**Requires:** Full Disk Access for the MCP host process (see [Full Disk Access Setup](#full-disk-access)). Without it, use `search-notes`.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `query` | string | Yes | Query expression (syntax below), at most 2000 characters |
| `limit` | number | No | Maximum notes to return. Defaults to 50, maximum 500. The response reports the total match count. |
| `scanLimit` | number | No | How many of the most recently modified notes to examine. Defaults to 500, maximum 10000. The response says when older notes were left unscanned. A large scan decodes more bodies, so it takes longer. |
| `includeDeleted` | boolean | No | Also scan notes in Recently Deleted, notes pending deletion, and folderless notes. Defaults to `false`. |
| `includeWordCount` | boolean | No | Add `wordCount` to each returned note, the same count `words:` filters on (`null` when locked or unreadable). Free when the query already reads bodies; a metadata-only query (for example `pinned`) reads just the returned notes' bodies in one extra read-only query. Defaults to `false`. |

**Syntax:**

| Form | Matches |
|------|---------|
| `budget`, `"quarterly budget"` | Title or body contains the word or phrase (case-insensitive substring) |
| `title:x`, `body:x`, `text:x` | Title only, body only (text after the first line), or either |
| `folder:Work`, `folder:"Work/Clients"` | The note's own folder, by name or full path, case-insensitive (notes in subfolders are not included); a literal `/` in a name can be written `\/` as in `list-folders` |
| `account:iCloud` | Account name, case-insensitive |
| `tag:finance` | Native Notes tag (with or without `#`); textual hashtags are ordinary words |
| `has:link`, `has:attachment`, `has:checklist`, `has:drawing`, `has:image`, `has:video`, `has:audio`, `has:pdf`, `has:table`, `has:scan`, `has:url`, `has:map`, `has:tag` | The note body contains that kind of object. `has:url` is a link preview card (it also counts as `has:link`, as inline links do); `has:map` is a map attachment |
| `checklist:open`, `checklist:done` | At least one unchecked item; or items present and all checked |
| `pinned`, `locked`, `shared`, `quicknote` (or `is:pinned` …) | Note flags; `shared` includes notes in a shared folder, and `quicknote` is a note created as a Quick Note (the same flag `list-special-notes kind=quick-notes` reads) |
| `words:>250` | Word count, with `=`, `>`, `>=`, `<`, `<=` |
| `created:>=2026-07-01`, `modified:<2026-09-01` | Dates as `YYYY-MM-DD` in local time, with the same operators; `=` means that whole day |
| `a b`, `a AND b`, `a OR b`, `NOT a`, `-a`, `( … )` | AND is implicit and binds tighter than OR |

Operators are case-insensitive. Quote an operator or flag word to search it
literally, for example `"and"` or `"pinned"`. Queries are capped at 256 tokens
and 64 levels of nesting. An unknown field such as `titel:x` is an error rather
than a silent text search; quote it to search the literal text.

Password-protected notes match on title and metadata only. Their bodies are
encrypted, so a body predicate is unknown for them rather than false: neither
`body:x` nor `-body:x` matches them, though `-body:x OR pinned` matches a
pinned one. Notes whose body cannot be decoded are treated the same way. Their
snippets are always empty.

**Example - Open to-dos in a folder:**
```json
{
  "query": "folder:\"Work Projects\" has:checklist -checklist:done"
}
```

**Example - Invoices or finance-tagged notes since July, scanning more history:**
```json
{
  "query": "(title:invoice OR tag:finance) modified:>=2026-07-01",
  "scanLimit": 2000,
  "limit": 20
}
```

**Returns:** Matching notes, most recently modified first, each with `id`,
`title`, `folder`, `account`, `modified`, `created`, and a `snippet` centred on
the first matched phrase. Each note also has `matchedIn` when the query has a
positive text term: `["title"]`, `["body"]`, or both, saying where those terms
occur (a `title:` term is only looked for in the title, a `body:` term only in
the body). It is absent for locked or undecodable notes, and an empty list
means the note matched through a non-text branch such as `pinned OR x`. The ids are the same `x-coredata://…/ICNote/p…` form
every other tool accepts. `structuredContent` also reports `matched` (total
matches), `scanned`, `eligible`, `scanTruncated`, `truncated`, and `unreadable`
(bodies that could not be decoded). A malformed query returns an error naming
the problem and its position.

---

#### `get-note-content`

Retrieves the full content of a specific note.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | No | Note ID (preferred - more reliable than title) |
| `title` | string | No | Note title (use `id` instead when available) |
| `account` | string | No | Account containing the note (defaults to Notes.app's default account; exact or unique-prefix match, ignored if `id` is provided) |
| `timeoutSeconds` | number | No | Whole seconds, 1–120, for the body read; overrides `APPLE_NOTES_MCP_TIMEOUT_MS` for this call only |

**Note:** Either `id` or `title` must be provided. Using `id` is recommended as it's unique and avoids issues with duplicate titles.

**Busy Notes.app:** with an `id` and Full Disk Access, the note's existence and password flag are read from the NoteStore database (as `get-note-structure` does), so only the body read goes through Notes.app. A timeout is always reported as `timeout_indeterminate`, never as `not_found`, even when an automatic retry then fails differently; and when Notes.app cannot resolve an id the database still holds, the error is `notes_unavailable`. Retry in a moment, or use `get-note-structure` for a read that does not need Notes.app.

**Large images:** Notes.app returns images inside the body as base64, so a note holding a very large image (tens of MB) can take longer to read than the timeout allows. When the read times out or overflows the output buffer, the error says so and, with Full Disk Access, names the attachments of 5 MB or more. Retry with a larger `timeoutSeconds`; `delete-note` accepts the same argument, and it needs a successful read to verify the note before deleting it.

**Example - Using ID (recommended):**
```json
{
  "id": "x-coredata://ABC123/ICNote/p456"
}
```

**Example - Using title:**
```json
{
  "title": "Shopping List"
}
```

**Returns:** The HTML content of the note, its exact `id`, and a
`contentHash`. Pass that hash back as `expectedContentHash` for a later update,
append, or delete; the write is rejected if the note's body or rich metadata
changed after this read. With Full Disk Access, embedded URLs omitted by
AppleScript are restored and returned in `links`. The response also reports
actual `nativeTags`, `richContentComplete`, and `writable`. Textual `hashtags`
remain a separate field and are not proof that Notes registered native tags.
`writable` is also false when the note uses formatting that AppleScript's HTML
does not carry (superscript, subscript, non-left paragraph alignment, or
highlight): a full-body `update-note` would silently drop it, so it is refused
and the `warning` names the formatting. `append-to-note` with `scopeText` still
works through the native path, which verifies existing formatting.

**⚠️ The returned body can be lossy — do not write it back verbatim.** Inline
base64 images larger than `APPLE_NOTES_MCP_MAX_INLINE_IMAGE_BYTES` (default
256 KB) are replaced with `[inline image omitted: …]` text placeholders so an
image-heavy note cannot blow the MCP message limit. `structuredContent` reports
this as `strippedImages` (count) and `truncated` (boolean). When either is set,
passing this body to an unguarded full-body writer would replace the real images
with placeholder text. This server's `update-note` refuses attachment-bearing
notes, and `append-to-note` routes them to native end-append with `scopeText`,
which never rewrites the existing body; make any other edit in Notes.app.

---

#### `get-native-objects`

Reads native object identities and ranges, checklist item IDs and state, actual
native tags, and native table data from one exact note ID. Table output includes
stable row and column identifiers. `tableCellsComplete` is false when Notes
metadata cannot be decoded completely. This tool is read-only and requires Full
Disk Access.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Exact note ID, in any [identifier form](#identifier-forms) |

---

#### `get-note-tables`

Reads a page of native tables in one exact note, in body order, from the NoteStore
database. Each table is returned as GitHub-flavored Markdown and as JSON `rows`
with stable `rowIds` and `columnIds`. Notes tables have no header row, so the
Markdown uses the first row as the header. Pipes are escaped as `\|`,
backslashes are doubled, and line breaks inside a cell become `<br>`.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Exact note ID (`x-coredata://…/ICNote/pNNN`) |
| `offset` | integer | No | Zero-based position of the first table (default 0); use `page.nextOffset` |
| `limit` | integer | No | Maximum tables per page (default and maximum 500) |
| `maxBytes` | integer | No | Full serialized response budget in UTF-8 bytes (default 4 MiB, minimum 1024 bytes, maximum 8 MiB) |

The byte budget includes both the text response and structured data, including
repeated Markdown and JSON escaping. Tables are returned whole. `tableCount`
and `page.totalAvailable` count all tables in the note; `page.returned` counts
the entries in this response. While `page.hasMore` is true, call again with
`offset: page.nextOffset` and the same `limit` and `maxBytes`. Each call reads
the note again, so finish paging before editing it.

If one table exceeds an otherwise empty page, its entry contains identifying
metadata, `complete: false`, `contentOmitted: true`, and a `reason`, without
partial rows or row/column IDs. The next offset advances past that entry. To
retrieve its content, retry that offset with a larger `maxBytes`, or export the
note to a file. If even the metadata exceeds the budget, the tool returns a
validation error. `page.stoppedAtSizeLimit` reports a byte-budget stop.

`tableCellsComplete` is false when any table or cell could not be decoded, or
when the current page omits a table's content for its byte budget. A
cell holding an embedded object is `null` in `rows`, listed in
`incompleteCells`, and shown as `[undecoded cell]` in Markdown. A table whose
data cannot be decoded at all has `complete: false`, a `reason`, and no rows.
Cell text is never guessed. Links and styling inside cells are not rendered.
A note without tables returns an empty `tables` list. This tool is read-only,
requires Full Disk Access, and refuses password-protected notes.

---

#### `get-note-blocks`

Decodes one note's body into typed blocks, read-only, from the NoteStore
database. Each block is one paragraph with its `style` (`title`, `heading`,
`subheading`, `body`, `monospaced`, `bulleted`, `dashed`, `numbered`,
`checklist`, or `unknown` with the raw `styleType`), `indent`, `alignment`,
`blockQuote`, checklist `id`/`done`, and `paragraphUuid` when stored. Each
block lists its inline `runs` with `bold`, `italic`, `underline`,
`strikethrough`, `superscript`, `subscript`, `color`, `highlight`, `link`
(plus `linkSafe`), `font`, and `attachment`, and its attachment markers in body
order. Offsets and lengths count UTF-16 code units. `summary` counts styles and
inline attributes for the whole note. `undecodedFields` lists stored field
numbers the decoder deliberately does not interpret.

**Requires:** Full Disk Access. Password-protected notes are refused.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Exact note ID |
| `offset` | number | No | First block to return (default 0). Use `page.nextOffset` |
| `limit` | number | No | Maximum blocks per page (default 500, max 5000) |

A page also stops early to stay under `APPLE_NOTES_MCP_BLOCKS_MAX_BYTES`
(default 4 MB). `paragraphUuid` is not unique: Notes copies it when a paragraph
is split. Link URLs are returned as stored, and `linkSafe` is false for schemes
other than http(s), `notes:`, `applenotes:` and `mailto:`. Errors carry a
stable code in brackets, such as `[encrypted]` or `[no-full-disk-access]`.

---

#### `list-note-paragraphs`

Lists one note's non-empty paragraphs in body order, read from the NoteStore
database. It never changes Notes. With `recordAnchors` it also writes the
local anchor registry, so the tool is not marked read-only in its MCP
annotations. Each paragraph has `blockIndex` (its index in
`get-note-blocks`, where empty paragraphs also count), `text`, `style`,
`styleType`, `paragraphId` (the UUID Notes stores on the paragraph's first
text run), and `paragraphIdStatus`:

- `unique`: no other paragraph in the note carries this ID. The paragraph also
  gets `url`, a direct
  `applenotes://showNote?identifier=<note>&paragraphID=<paragraph>` link that
  opens Notes at that paragraph.
- `shared`: other paragraphs carry the same ID (`sharedWith` counts them).
  Notes copies the ID when a paragraph is split, so this is common for body
  text. No `url` is given, because it could open the wrong paragraph.
- `missing`: no ID is stored.

`mixedParagraphIds: true` marks a paragraph whose text runs carry more than
one ID; only the first-run ID is used. Titles and headings usually have unique
IDs.

**Requires:** Full Disk Access. Password-protected notes are refused.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | One of `id`, `title` | Exact note ID, or the note's Notes UUID |
| `title` | string | One of `id`, `title` | Exact note title; must match one note. Notes in Recently Deleted are ignored, as in `list-notes` |
| `folder` | string | No | With `title`: the folder's name or full path as `list-folders` shows it, such as `Work/Clients` |
| `linkableOnly` | boolean | No | Return only paragraphs with a `url` |
| `offset` | number | No | First paragraph to return (default 0). Use `page.nextOffset` |
| `limit` | number | No | Maximum paragraphs per page (default 500, max 5000) |
| `recordAnchors` | boolean | No | Also record a [paragraph anchor](#paragraph-anchors) for each returned paragraph (at most 500 per call); each row gains `anchorId` and the result gains `anchorsRecorded` (the new ones). Writes only the local anchor registry |

---

#### `get-paragraph-link`

Returns a direct link to one paragraph of a note:
`applenotes://showNote?identifier=<note>&paragraphID=<paragraph>`. It selects
the note like `list-note-paragraphs` and the paragraph by exactly one of:

- `contains`: a snippet of the paragraph. Case, runs of spaces, and Unicode
  width are ignored.
- `match`: the whole paragraph, compared the same way.
- `blockIndex`: from `list-note-paragraphs`.

When `contains` or `match` hits several paragraphs, pass `occurrence` (1-based)
or a longer snippet.

The link is returned only when the paragraph's ID is `unique` in the note.
Otherwise the result is an error whose `structuredContent` carries the usual
`code` plus a `reason`: `paragraph-id-shared`, `paragraph-id-missing`,
`no-match`, `ambiguous-paragraph`, `occurrence-out-of-range`, `ambiguous-note`
(several notes have that title; the message lists their folders), `not-found`,
`encrypted`, or `no-body`. The tool never creates or changes a paragraph ID,
and an edit in Notes can later replace the ID and break the link. With
`recordAnchor` it also writes the local anchor registry, so the tool is not
marked read-only in its MCP annotations.

**Requires:** Full Disk Access.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id`, `title`, `folder` | string | One of `id`, `title` | Note selector, as in `list-note-paragraphs` |
| `contains` | string | One of `contains`, `match`, `blockIndex` | Snippet of the paragraph |
| `match` | string | One of `contains`, `match`, `blockIndex` | The whole paragraph |
| `blockIndex` | number | One of `contains`, `match`, `blockIndex` | The paragraph's `blockIndex` |
| `occurrence` | number | No | Which match to use when several paragraphs match |
| `recordAnchor` | boolean | No | Also record a [paragraph anchor](#paragraph-anchors) for the linked paragraph and return its `anchorId`. Writes only the local anchor registry |

---

#### Paragraph anchors

A paragraph link breaks when Notes replaces or copies the paragraph's ID. A
paragraph anchor records enough about the paragraph to find it again: the
note's Notes UUID, the paragraph ID and its status, the paragraph's normalized
text and a fingerprint of it, the fingerprints of the paragraphs before and
after it, its `blockIndex`, and when it was recorded. Anchors are kept in one
local file, `~/Library/Application Support/apple-notes-mcp/paragraph-anchors.json`
(or the absolute path in `APPLE_NOTES_MCP_ANCHOR_FILE`). It is created with
mode 0600 in a 0700 directory, replaced atomically under a lock file, and
holds the text of every anchored paragraph. A symlinked, unreadable or
corrupt registry is refused and left as it is. The anchor tools never change
Notes.

Resolving an anchor tries three steps in order, and every step fails closed:

1. **Paragraph ID.** A paragraph whose ID is still unique in the note is the
   anchored paragraph, even if its text was edited or it moved. A link to that
   ID opens exactly that paragraph.
2. **Exact text.** The same normalized text. When several paragraphs have it,
   only the one whose neighbours still match is chosen; a tie is `ambiguous`.
3. **Text and neighbours.** Similar text between both recorded neighbours, or
   nearly identical text beside one of them. Two close candidates are
   `ambiguous`; one below `minConfidence` is `low-confidence`.

A match whose ID is now shared or missing is `needs-reminting`: the paragraph
is found (the result names its block), but no safe link exists until it gets a
new ID. Public automation cannot set a paragraph ID, so this server only
reports it and returns no `url`.

To share anchored links outside Notes, see the
[paragraph anchor resolver](#paragraph-anchor-resolver-opt-in).

#### `create-paragraph-anchor`

Records an anchor for one paragraph, selected exactly as in
`get-paragraph-link` (note by `id` or `title`/`folder`; paragraph by one of
`contains`, `match`, `blockIndex`, plus `occurrence`). Unlike
`get-paragraph-link`, a paragraph whose ID is shared or missing can be
anchored. Recording the same paragraph again (same note, ID, text and block)
returns the existing anchor with `created: false`.

Returns `anchor`, `created`, and `url` when the paragraph currently has a
unique ID.

**Requires:** Full Disk Access. Writes only the anchor registry.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id`, `title`, `folder` | string | One of `id`, `title` | Note selector, as in `list-note-paragraphs` |
| `contains`, `match`, `blockIndex`, `occurrence` | | One of `contains`, `match`, `blockIndex` | Paragraph selector, as in `get-paragraph-link` |

#### `resolve-paragraph-anchor`

Finds an anchored paragraph in the note as it is now. The result has `status`
(`resolved`, `needs-reminting`, `ambiguous`, `low-confidence`, `not-found`,
`note-not-found`, `note-deleted` for a note in Recently Deleted, or
`note-unreadable` for a locked note), `method` (`paragraph-id`, `exact-text`,
`text-and-neighbours`), `confidence` (0 to 1), `match` (`blockIndex`, `text`,
`paragraphId`, `paragraphIdStatus`), `changes` (`textChanged`,
`blockIndexChanged`, `paragraphIdChanged`), and `message`. `url`, the current
`applenotes://` link, is present only when `status` is `resolved`.

**Requires:** Full Disk Access.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `anchorId` | string | Yes | The anchor (`pa_` and 24 hex digits) |
| `minConfidence` | number | No | Lowest confidence accepted as a match (default 0.6) |
| `refresh` | boolean | No | After a match with confidence 0.8 or more, store the paragraph as it is now (text, neighbours, block, ID), so later edits are tracked from here. Reports `refreshed` or `refreshSkipped` |

#### `list-paragraph-anchors`

Lists recorded anchors in the order recorded, with `total`, the `registry`
path and `page` info. Reads only the registry.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `noteIdentifier` | string | No | Only anchors in the note with this Notes UUID |
| `offset` | number | No | First anchor to return (default 0) |
| `limit` | number | No | Maximum anchors (default 100, max 1000) |

#### `get-paragraph-anchor`

Returns one stored anchor as recorded. Reads only the registry.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `anchorId` | string | Yes | The anchor |

#### `prune-paragraph-anchors`

Removes anchors that no longer resolve, or the anchors you list. It is a dry
run unless `dryRun` is `false`. Without `anchorIds` it resolves every anchor
in scope and treats `not-found` and `note-not-found` as stale. A note in
Recently Deleted (`note-deleted`) is kept by default because it can be
restored. Returns `stale` (`anchorId`, `status`, `message`), `examined`, and
`removed`.

**Requires:** Full Disk Access unless `anchorIds` is given.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `anchorIds` | string[] | No | Remove exactly these anchors instead of resolving |
| `noteIdentifier` | string | No | Only anchors in the note with this Notes UUID |
| `statuses` | string[] | No | Statuses treated as stale (default `not-found`, `note-not-found`) |
| `dryRun` | boolean | No | Report without removing (default `true`) |

---

#### `get-note-structure`

Returns a read-only overview of one note from the NoteStore database, in one
call:

- `text` (decoded body), `textLength`, `wordCount`, `charCount` (Unicode
  characters, attachment placeholders excluded), and `blockSummary` (the
  `get-note-blocks` summary counts).
- `links`, each with a `kind`: `inline` (a hyperlink on text), `card` (a rich
  link preview attachment, with `attachmentId` and `previewPath`), `note` (a
  native link chip to another note), or `section` (a native link chip to a
  heading or paragraph, with `section`). Notes deep links also carry
  `targetNote` and `paragraphId`. `linkCounts` totals them.
- `tags` (native tags in body order) and `attachments`, listed the way
  [`list-attachments`](#list-attachments) with `includePaths` lists them: the
  same `kind` (`image`, `scan`, `drawing`, `pdf`, `audio`, `video`, `url`,
  `table`, `other`), the same body order, and the same `previewPath`, plus the
  card `title`/`url`, `fileSize`, and body position. Gallery items and
  recording parts are nested under `children`; `attachmentCount` counts
  top-level attachments only.
- `deepLink`, `isShared` (the note or any enclosing folder is shared),
  `isLocked`, `isPinned`, `inRecentlyDeleted`, `lastViewed`,
  `checklistTotal`, `checklistDone`, `hasDrawing` (classic sketches and Paper
  drawings), and `firstImage` (the same lead visual `list-attachments`
  returns with `firstImage`, plus its attachment `id`).

`lastViewed` is an ISO date, or null with `lastViewedStatus` set to
`never-viewed`, `not-recorded`, `malformed`, or `unsupported` (the column
does not exist on this macOS version). A password-protected note returns its
metadata and attachment rows with `bodyDecoded: false` and the body-derived
fields null.

**Requires:** Full Disk Access.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Exact note ID: the `x-coredata://` id, or the note's Notes UUID or numeric key (see [Identifier forms](#identifier-forms)) |
| `includeText` | boolean | No | Include the decoded text (default true). Text larger than `APPLE_NOTES_MCP_BLOCKS_MAX_BYTES` is omitted with `textOmitted: true` |

Link URLs are returned as stored; check `linkSafe` before emitting one into
HTML.

---

#### `list-note-links`

Lists links, read-only from the NoteStore database, in one note (`id`) or
across a `folder`, an `account`, or the whole library (no selector). Each link
has a `kind`:

| Kind | What it is | Where Notes stores it |
|------|------------|-----------------------|
| `inline` | A hyperlink on text | Inside the note body |
| `card` | A rich link preview | An attachment row with the URL and title |
| `note` | A native link chip to another note | An inline-attachment row with a Notes deep link |
| `section` | A native link chip to a heading or paragraph | Same, with `paragraphID` in the deep link |

Each row has `url`, `text` (label), `linkSafe`, `targetNote` and `paragraphId`
for Notes deep links, `section` for section chips, and for cards
`attachmentId` and `previewPath` (Notes' largest cached preview image, found
the same way [`list-attachments`](#list-attachments) finds it, or null when
Notes has none). Each row also names its source: `noteId`, `noteIdentifier`,
`noteTitle`, `noteModified`, `folder`, `folderPath` (as `list-folders` prints
it), `account`, and `accountIdentifier`. When bodies were decoded, `start` and
`blockIndex` give the link's position, and `inBody: false` marks a card or chip
row with no marker left in the body.

Inline links need every body in scope decompressed and decoded, so a folder,
account, or library scan includes them only with `includeInline: true`
(slower). A single note always includes them. A `folder` scope includes its
subfolders unless `includeSubfolders` is false. Scans skip Recently Deleted
and folderless notes; a note requested by `id` is read wherever it is. Links
come newest-modified note first, in body order within a note.

**Requires:** Full Disk Access.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | No | One exact note ID (x-coredata id, Notes UUID, or numeric key). Do not combine with `account` or `folder` |
| `account` | string | No | Account name (exact or unique-prefix match, as in the other tools) |
| `folder` | string | No | Folder name (any depth, must be unique) or path from the top level as `list-folders` prints it, such as `Work/Clients`; escape a literal slash as `\/` |
| `includeSubfolders` | boolean | No | With `folder`, also list notes in its subfolders (default true) |
| `includeInline` | boolean | No | Decode bodies for inline links (default true for `id`, false otherwise) |
| `kinds` | string[] | No | Only these kinds: `inline`, `card`, `note`, `section` |
| `offset` | number | No | First link to return (default 0). Use `page.nextOffset` |
| `limit` | number | No | Maximum links per page (default 200, max 2000) |

The response also reports `scope`, `counts` per kind, `notesInScope`,
`notesWithoutBody` (locked, empty or undecodable bodies when inline links were
requested), and `page`. A page stops early to stay under
`APPLE_NOTES_MCP_BLOCKS_MAX_BYTES`. An ambiguous folder name is refused with a
message that lists the matching paths.

---

#### `list-native-tags`

Lists actual native Notes tags. This differs from textual hashtag search. It is
read-only and requires Full Disk Access.

- **Folder mode** (pass `folder`, optionally `account`): maps each tag used in that
  folder to its matching note IDs. The response reports `complete: false` and per-note
  errors when some native metadata is unavailable.
- **Inventory mode** (omit `folder`): an account-wide inventory with counts, read-only from the
  database. `account` narrows it to one account; omit it to count every
  account. Each `inventory` entry has `tag`, `noteCount` (distinct notes, Recently
  Deleted excluded), per-account counts in `accounts`, and any other `spellings` Notes
  treats as the same tag. Tags with no remaining notes are listed with `noteCount: 0`.
  A tag counts for a note only while the note body still references it. Locked or
  unreadable bodies are counted from the tag objects alone and reported through
  `unverifiedNotes` and `complete: false`.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `folder` | string | No | Folder to list (nested paths supported). Omit for the inventory |
| `account` | string | No | Account name, exact or unique prefix |

---

#### `native-tags-status`

Checks whether exactly one configured Native Tags Shortcut is installed. An
installed workflow may still need macOS permission on its first execution, and
installation does not show whether that consent was given: run it once in the
foreground in Shortcuts.app and choose **Always Allow** after install or upgrade
(see [Troubleshooting](#native-writes-time-out-or-report-an-uncertain-outcome)).

---

#### `add-native-tags`

Adds actual native Notes tag objects to one exact note using `id`, a fresh
`expectedContentHash`, a distinctive existing `scopeText`, and `tags`. The
operation verifies the note's original text, links, and native objects after the
Shortcut runs. It refuses ambiguous title-and-scope matches and never retries an
uncertain write. Install the signed workflow as described in
[`shortcuts/README.md`](shortcuts/README.md).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Exact note ID, in any [identifier form](#identifier-forms) |
| `expectedContentHash` | string | Yes | `contentHash` from a fresh read of the note |
| `scopeText` | string | Yes | Distinctive phrase already in the note, 12–500 characters |
| `tags` | string[] | Yes | 1–100 tag names to add |

---

#### `get-note-plaintext`

Retrieves a note's body as plain text, with no HTML markup.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | No | Note ID (preferred - more reliable than title) |
| `title` | string | No | Note title (use `id` instead when available) |
| `account` | string | No | Account containing the note (defaults to Notes.app's default account; exact or unique-prefix match, ignored if `id` is provided) |

**Note:** Either `id` or `title` must be provided. This reads the note's native `plaintext` property, so it skips the HTML-to-text conversion that `get-note-content` plus a Markdown pass would do. Use `get-note-content` when you need the HTML, or `get-note-markdown` when you want Markdown with checklist state.

**Returns:** The plain-text content of the note in `structuredContent.plaintext`, or error if not found.

---

#### `get-note-details`

Retrieves metadata about a note (without full content).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `title` | string | Yes | Exact title of the note |
| `account` | string | No | Account containing the note (defaults to Notes.app's default account; exact or unique-prefix match) |

**Example:**
```json
{
  "title": "Project Plan"
}
```

**Returns:** JSON with note metadata:
```json
{
  "id": "x-coredata://...",
  "title": "Project Plan",
  "created": "2025-01-15T10:30:00.000Z",
  "modified": "2025-01-20T14:22:00.000Z",
  "shared": false,
  "passwordProtected": false,
  "account": "iCloud"
}
```

---

#### `get-note-by-id`

Retrieves a note using its unique CoreData identifier.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | The CoreData URL identifier (e.g., `x-coredata://...`), or the note's Notes UUID or numeric key (see [Identifier forms](#identifier-forms)) |

**Returns:** JSON with note metadata, plus `identifier`, `folderIdentifier`, and `accountIdentifier` when Full Disk Access is granted, or error if not found.

---

#### `show-note`

Reveals a note in Notes.app using its unique CoreData identifier.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | The CoreData URL identifier (e.g., `x-coredata://...`), or the note's Notes UUID or numeric key |
| `separately` | boolean | No | Open in a separate note window when supported by Notes.app |

**Returns:** Confirmation that Notes.app accepted the show command.

---

#### `update-note`

Updates an existing note's content and/or title.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Exact CoreData note ID returned by a read or search |
| `expectedContentHash` | string | Yes | `contentHash` from the exact note version being replaced |
| `newTitle` | string | No | New title (if changing the title; ignored when `format` is `"html"`) |
| `newContent` | string | Yes | New content for the note body |
| `format` | string | No | Content format: `"plaintext"` (default) or `"html"`. When `"html"`, content replaces the entire note body as raw HTML and `newTitle` is ignored (the first HTML element serves as the title) |
| `allowLinkChanges` | boolean | No | Set to `true` only when intentionally changing or removing existing links |
| `ifFolderId`, `ifAncestorFolderId`, `forbiddenAncestorFolderIds` | string, string, string[] | No | Folder preconditions; see [Folder scope guards](#folder-scope-guards) |
| `timeoutSeconds` | number | No | Per-call timeout, 1–120 seconds, as for [`create-note`](#create-note). A timed-out write is uncertain: read the note by id before any retry |

Title-only updates are rejected because Apple Notes titles are not unique.

**Example - Using ID (recommended):**
```json
{
  "id": "x-coredata://ABC123/ICNote/p456",
  "expectedContentHash": "sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
  "newContent": "Updated content here"
}
```

**Example - Update with HTML formatting:**
```json
{
  "id": "x-coredata://ABC123/ICNote/p456",
  "expectedContentHash": "sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
  "newContent": "<p>New findings with <b>bold</b> emphasis.</p><pre><code>console.log('hello');</code></pre>",
  "format": "html"
}
```

**Returns:** Confirmation with the exact ID, post-save `contentHash`, and
`verifiedVisibleText: true`, or an error if the note changed before saving.
Apple Notes normalizes HTML, so this proves the visible text after saving, not
byte-identical rich formatting.

**Note:** `newContent` **replaces the entire note body** — it is not appended. To add to a note, prefer [`append-to-note`](#append-to-note), which does the read-and-concatenate for you and always round-trips the body as HTML. If you do read-modify-write by hand, note that `get-note-content` replaces oversized inline images with text placeholders (see [`get-note-content`](#get-note-content)) — writing that body back bakes the placeholders in.

**Rich-content safety:** `update-note` refuses to replace a note when its rich
metadata is unavailable or it contains attachments, native tags, inline
objects, or checklists that AppleScript cannot preserve. Existing link
destinations must remain present unless `allowLinkChanges` is explicitly set.

---

#### `delete-note`

Deletes a note (moves to Recently Deleted in Notes.app).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Exact CoreData note ID returned by a read or search |
| `expectedContentHash` | string | Yes | `contentHash` from the exact note version being deleted |
| `ifFolderId`, `ifAncestorFolderId`, `forbiddenAncestorFolderIds` | string, string, string[] | No | Folder preconditions; see [Folder scope guards](#folder-scope-guards) |
| `timeoutSeconds` | number | No | Per-call timeout, 1–120 seconds, as for [`create-note`](#create-note). A timed-out write is uncertain: read the note by id before any retry |
| `guardNoteId` | string | No | A second note (usually a verified copy) that must still be intact; needs Full Disk Access |
| `expectedGuardContentHash` | string | With `guardNoteId` | `contentHash` of the guard note from `get-note-content` |
| `requireActiveNoteId` | string | No | A second note that must still exist, be unlocked, stay outside Recently Deleted, and not be a Quick Note; its content is not fingerprinted. Needs Full Disk Access |

Title-only deletion is rejected. If the note changed after the supplied hash
was read, deletion is also rejected.

**Notes with large images.** Notes.app returns a note's body with each inline
image embedded as base64, so a note holding one 40 MB image has a body of about
110 MB. Body reads accept up to 512 MB of output, and `delete-note` compares a
body longer than 5 MB against a private temporary file rather than embedding it
in the AppleScript. The comparison still covers the whole body, and the file
is removed when the delete finishes.

**Copy-then-retire.** To delete an original only while its copy is still good,
read both notes, verify the copy, and pass the copy as `guardNoteId` with its
`contentHash` as `expectedGuardContentHash`. The copy's revision is re-read just
before the delete, and its body, lock state, and folder are checked again
inside the delete AppleScript, with the same fail-closed Recently Deleted test
as the note being deleted. The guard note must not be a Quick Note, a flag only
the database holds, so the guard needs Full Disk Access. A copy the database
has not saved yet passes on the live checks alone. The pair is still not one
transaction: the rich revision (which also covers checklists and attachments)
is a pre-check, and the in-script check covers the body and state Notes.app
exposes. `requireActiveNoteId` is the narrower form for a destination you
wrote yourself rather than copied.

**Example - Using ID (recommended):**
```json
{
  "id": "x-coredata://ABC123/ICNote/p456",
  "expectedContentHash": "sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
}
```

**Returns:** Confirmation message, or error if note not found. The delete and a
check of the note's original folder run in one AppleScript: if Notes.app accepts
the delete but the note is still listed in that folder, the call reports that
nothing was deleted instead of claiming success.

A note that is already in Recently Deleted is refused, because deleting it there
removes it permanently. The folder is read live from Notes.app in the same
AppleScript; the Recently Deleted folder is recognised by its database id (with
Full Disk Access) or by its English name. The check fails closed: a note whose
folder Notes.app reports as something other than a folder (as it does for a note
trashed earlier in the same Notes session) is refused the same way, and a note
whose folder cannot be read at all is refused with a message to retry. To remove
such a note for good, do it in Notes.app.

**⚠️ Safety:** Irreversible from the agent's side — requires explicit user confirmation before calling. Prefer `search-notes` / `list-notes` first to confirm the exact id(s) being deleted.

---

#### `move-note`

Moves a note to a different folder. The note is relocated in place via Notes.app's native `move`, so its id, creation date, and all embedded attachments (files, images, scans, PDFs, audio) are preserved. The destination folder must already exist — create it first with [`create-folder`](#create-folder).

A smart folder is never a destination: it only gathers notes by its rules, and Notes.app would move the note to Recently Deleted or store a created note where no folder shows it. `create-note`, `create-note-with-attachment`, `move-note`, `batch-move-notes`, and `create-folder` refuse one before writing anything, with `code: "unsupported"`, `committed: false`, and `reason: "smart_folder_destination"`. An ordinary folder that shares a smart folder's name is still found. Detection reads the NoteStore database, so it needs Full Disk Access; without it, destinations resolve as before.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Exact CoreData note ID returned by a read or search |
| `folder` | string | Yes | Destination folder name or nested path (e.g., `"Work/Clients"`) |
| `account` | string | No | Account whose `folder` is the destination (default: the default account) |
| `ifFolderId`, `ifAncestorFolderId`, `forbiddenAncestorFolderIds` | string, string, string[] | No | Folder preconditions; see [Folder scope guards](#folder-scope-guards) |
| `timeoutSeconds` | number | No | Per-call timeout, 1–120 seconds, as for [`create-note`](#create-note). A timed-out write is uncertain: read the note by id before any retry |

Title-only moves are rejected.

**Example - Using ID (recommended):**
```json
{
  "id": "x-coredata://ABC123/ICNote/p456",
  "folder": "Archive"
}
```

**Returns:** Confirmation only after the same note ID is read back and its
actual destination folder ID matches the requested folder.

---

#### Folder scope guards

`update-note`, `append-to-note`, `delete-note`, `move-note`, and
`batch-move-notes` accept three optional folder preconditions. Use exact
folder ids from `list-folders`.

- `ifFolderId`: the note must currently be in exactly this folder.
- `ifAncestorFolderId`: the note must be inside this folder or any of its
  subfolders.
- `forbiddenAncestorFolderIds` (up to 50): the note must not be inside any of
  these folders or their subfolders. For `move-note` and `batch-move-notes`,
  the destination must not be either.

The checks read Notes.app's live folders inside the same AppleScript as the
write, immediately before it. If the folder observed by the check fails a
precondition, the write is refused with `Scope guard failed: …`. The check and
write are separate Notes operations; another actor can move the note between
them. A native append to a protected note runs through Shortcuts, so its
precheck runs in a separate AppleScript before the append.

For `batch-move-notes`, the same preconditions apply to every supplied note ID.
Each note is checked independently immediately before its move. A scope mismatch
leaves that note unchanged and appears in its failure result; the remaining
items continue. A batch can therefore move some notes and refuse others.

**Example - retire a note only while it is still in the inbox:**
```json
{
  "id": "x-coredata://ABC123/ICNote/p456",
  "expectedContentHash": "sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
  "ifFolderId": "x-coredata://ABC123/ICFolder/p12"
}
```

---

#### `append-to-note`

Appends or prepends content to an existing note without replacing it. Always reads and writes as HTML, preserving all existing rich formatting.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Exact CoreData note ID returned by a read or search |
| `expectedContentHash` | string | Yes | `contentHash` from the exact note version being extended |
| `content` | string | Yes | Text to append to the note body |
| `position` | string | No | `"after"` (default) appends to the end; `"before"` inserts directly below the note's title line, so the title stays first |
| `separator` | string | No | String placed between existing content and new content (default: two newlines → `<div><br></div>` in HTML) |
| `format` | string | No | Format of the content being appended: `"plaintext"` (default) or `"html"` |
| `scopeText` | string | Native-object notes only | Unique existing phrase, as for [`append-native`](#append-native) |
| `ifFolderId`, `ifAncestorFolderId`, `forbiddenAncestorFolderIds` | string, string, string[] | No | Folder preconditions; see [Folder scope guards](#folder-scope-guards) |
| `timeoutSeconds` | number | No | Per-call timeout, 1–120 seconds, as for [`create-note`](#create-note). A timed-out write is uncertain: read the note by id before any retry |

Title-only appends are rejected.

**Example - Append plaintext:**
```json
{
  "id": "x-coredata://ABC123/ICNote/p456",
  "expectedContentHash": "sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
  "content": "New item added today"
}
```

**Example - Prepend HTML:**
```json
{
  "id": "x-coredata://ABC123/ICNote/p456",
  "expectedContentHash": "sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
  "content": "<div><b>Status:</b> done</div>",
  "format": "html",
  "position": "before"
}
```

**Returns:** Confirmation with the exact ID, post-save `contentHash`, and
`verifiedVisibleText: true`. Apple Notes normalizes HTML, so this proves the
visible text after saving, not byte-identical rich formatting. Warns when the
note is shared with collaborators.

**Safety:** The append is rejected if the note changed since it was read, rich
metadata is unavailable, or the note contains attachments. Existing link
destinations are verified after saving.

**Notes containing native objects** (a table, a checklist, native tags) cannot be
spliced, so they are routed to the native end-append bridge — see
[`append-native`](#append-native). That path additionally requires `scopeText`,
keeps the default blank-line `separator` and `position: "after"`, and accepts a
fixed HTML subset rather than anything Notes.app can render:

| | Native append |
|---|---|
| Elements | `<a>` `<b>` `<br>` `<code>` `<del>` `<div>` `<em>` `<h1>` `<h2>` `<h3>` `<i>` `<li>` `<ol>` `<p>` `<s>` `<span>` `<strong>` `<tt>` `<u>` `<ul>` |
| Attributes | `href` on `<a>` (`https:`, `http:`, `notes:`, `applenotes:`, `mailto:` only) and a `font-size` style on `<span>`, e.g. `<span style="font-size: 18px">` — the form Notes itself stores a heading as |
| Refused | every other element and attribute, by name, naming the accepted subset; a table, in whole or in part (`<table>` `<thead>` `<tbody>` `<tr>` `<td>` `<th>`) — use [`create-table`](#create-table) instead; comments, doctype and processing instructions |

Ordinary notes take the guarded HTML path and are not restricted to that subset.

---

#### `insert-link`

Adds one web, mail or Notes link to an exact note as its own paragraph, then
proves it from the link runs Notes actually stored. Use `mode: "raw"` to show
the URL itself, or `mode: "hyperlink"` with a `label` to show text that links to
the URL. For a link to another note by id, use
[`insert-note-link`](#insert-note-link), which looks up that note's real deep
link.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | Yes | Exact CoreData note ID |
| `expectedContentHash` | string | Yes | `contentHash` from the exact note version being extended |
| `url` | string | Yes | Absolute `http(s)` URL with a host, or a `mailto:`, `notes://` or `applenotes:` link. No spaces, `<`, `>` or `"` |
| `mode` | string | No | `"raw"` (default) shows the URL; `"hyperlink"` shows `label` |
| `label` | string | Hyperlink only | Visible text for `mode: "hyperlink"`; refused in raw mode |
| `linked` | boolean | No | Raw mode only. `true` (default) stores a real link on the URL text. `false` writes plain text with no stored link |
| `position` | string | No | `"end"` (default) or `"after-title"` (first paragraph under the title) |
| `blankLine` | boolean | No | Leave a blank line between existing text and the link paragraph (default `true`) |
| `scopeText` | string | Native-object notes only | Unique existing phrase, as for [`append-native`](#append-native) |

**Example - Hyperlink under the title:**
```json
{
  "id": "x-coredata://ABC123/ICNote/p456",
  "expectedContentHash": "sha256:0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
  "url": "https://example.com/report",
  "mode": "hyperlink",
  "label": "Quarterly report",
  "position": "after-title"
}
```

**Returns:** `route` (`"applescript"` for ordinary notes, `"native"` for notes
with native objects), `linkStored`, `storedUrl` (the destination read back from
the note, for example `https://example.com/` for a bare origin), and the new
`contentHash`.

**Safety:** The same guards as [`append-to-note`](#append-to-note): a fresh
`expectedContentHash`, the attachment block, and every existing link must
survive. A linked insert must add exactly one stored link with the requested
label and destination; if the text lands but that proof fails, the error says
the write happened so it is not repeated.

**Limits:**

- Plain URL text is not linked by Notes when written this way. With
  `linked: false`, the note stores no link and readers of the body see ordinary
  text; Notes.app may still underline the URL on screen through its own data
  detection. The result reports `linkStored: false`.
- Notes with native objects (a table, a checklist, native tags) take the native
  end-append path, so only `position: "end"` with `blankLine: true` works there.
- The link always gets its own paragraph. Placing it at the end of one existing
  paragraph, or inside the text, is not available.
- Rich URL preview cards (the link tile Notes makes when you paste a URL) are
  not produced. No public automation route creates one: the Shortcuts Notes
  actions write text, and AppleScript's `body` has no card markup.
- To start a new note with a link, use [`create-note`](#create-note) with
  `format: "html"` and an `<a href>` in `content`; the link is stored the same
  way.

---

#### `get-note-link`

Returns the `notes://showNote?identifier=<uuid>` deep-link URL for a note. The URL opens the note in Notes.app on iOS and macOS and can be stored in Reminders tasks or shared links.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | string | No | Note ID (preferred - more reliable than title) |
| `title` | string | No | Note title (use `id` instead when available) |
| `account` | string | No | Account containing the note (defaults to Notes.app's default account; exact or unique-prefix match, ignored if `id` is provided) |

**Note:** Either `id` or `title` must be provided. Using `id` is recommended. Password-protected notes cannot be linked.

**Example:**
```json
{
  "id": "x-coredata://ABC123/ICNote/p456"
}
```

**Returns:** `notes://showNote?identifier=<uuid>` URL string, plus the note id and title.

**Note:** Requires Full Disk Access for the process that runs the server so the Notes SQLite database is readable. On macOS 12–15 the tool also falls back to the AppleScript `note link` property. Run the `doctor` tool to verify access.

---

#### `list-notes`

Lists all notes, optionally filtered by folder, date, and limit.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `account` | string | No | Account to list notes from (defaults to Notes.app's default account; exact or unique-prefix match) |
| `folder` | string | No | Filter to notes in this folder only (supports nested paths like `"Work/Clients"`) |
| `modifiedSince` | string | No | ISO 8601 date string to filter notes modified on or after this date (e.g., `"2025-01-01"`) |
| `limit` | number | No | Maximum number of notes to return |
| `includeRecentlyDeleted` | boolean | No | Also list notes in Recently Deleted, each flagged `inRecentlyDeleted: true` (default `false`) |

**Example - All notes:**
```json
{}
```

**Example - Notes in a folder:**
```json
{
  "folder": "Work"
}
```

**Example - Recent notes with limit:**
```json
{
  "modifiedSince": "2025-06-01",
  "limit": 20
}
```

**Returns:** List of notes as `{title, id}` pairs — `notes: Array<{title, id}>`, plus `count`. The human-readable line is `  - <title> [id: <id>]`. Notes in Recently Deleted are left out by default and counted in `excludedRecentlyDeleted` (present only when nonzero); with `includeRecentlyDeleted: true` they are listed with `inRecentlyDeleted: true` and a `[RECENTLY DELETED]` marker. Notes.app's own listing includes them, so the Recently Deleted folder is recognised by its database id (with Full Disk Access) or by its English name. With Full Disk Access each entry also carries `identifier`, `folderIdentifier`, and `accountIdentifier` (see [Identifier forms](#identifier-forms)).

Use the returned `id` for any follow-up read/update/move/delete rather than re-resolving the title: titles are not unique, and a by-title lookup resolves a duplicated title to the same one note every time, silently skipping the others.

> **Changed in 2.7.0:** `notes` was previously `string[]` (titles only). Callers that treated the array as strings must now read `.title`.

For date order, incremental sync cursors, Recently Deleted, or word counts, use [`list-recent-notes`](#list-recent-notes).

---

#### `list-recent-notes`

Lists notes from the NoteStore database (read-only) by stored modification time, with an exact cursor for incremental sync. With `since`, it pages through changes oldest first; without it, it shows the newest notes first. Unlike `list-notes`, it can include Recently Deleted and can count words.

**Requires:** Full Disk Access for the MCP host process (see [Full Disk Access Setup](#full-disk-access)).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `account` | string | No | Only this account (exact or unique-prefix name). Omit for every account |
| `folder` | string | No | Only notes directly in this folder: a full path in `list-folders` syntax, or a unique folder name |
| `since` | string | No | Return notes after this point, **oldest first**. A `modifiedCheckpoint` cursor (from a row or `nextSince`), or an ISO 8601 date (local midnight) or date-time (local time unless it carries `Z` or an offset), meaning modified strictly after it |
| `limit` | number | No | Maximum rows, 1–1000 (default 50) |
| `includeDeleted` | boolean | No | Also return notes in Recently Deleted, notes awaiting deletion, and folderless notes (default `false`) |
| `wordCounts` | boolean | No | Decode each body and add `wordCount` and `charCount` (default `false`) |
| `bodyPreview` | boolean | No | Add `bodyPreview` (up to 180 characters) and `textDecoded` (default `false`) |

**Returns:** `notes`, each with `id`, `identifier`, `title`, `folder`, `account`, `created`, `modified`, `modifiedCheckpoint`, `pinned`, `locked`, `inRecentlyDeleted`, and `markedForDeletion`. Also `count`, `limit`, `order` (`oldest-first` or `newest-first`), `saturated`, and `nextSince`.

- **Cursors.** `modifiedCheckpoint` is an opaque token (`cdts1:`, 16 hex digits, `:`, the note's database key). It carries the exact stored timestamp bits, so it never loses precision the way an ISO string can, and the key orders notes that share one timestamp. Pass it back as `since`.
- **Syncing.** Call with `since`, store `nextSince`, and pass it as the next `since`. `nextSince` is the last returned row's cursor, or the incoming boundary when nothing matched, so every call advances. `saturated` is `true` when `count` equals `limit`: more changes may follow, so call again right away. When it is `false`, you are caught up. Notes that share a timestamp are split across pages by key, so none is skipped or repeated.
- **First sync.** Start with `since: "1970-01-01"` and page the same way. A library larger than the 1000-row maximum is reached in full.
- **Browsing.** Without `since`, rows come newest first. `nextSince` is then t