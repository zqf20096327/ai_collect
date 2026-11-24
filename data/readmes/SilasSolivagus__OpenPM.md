<div align="center">

<img src="./assets/banner-en.svg" alt="OpenPM: Turn rough product ideas into clickable wireframes, orthogonal flows, and surgical PRDs." width="100%" />

<br/>

<p>
  <strong>English</strong> | <a href="./README.zh-CN.md">简体中文</a>
</p>

<p>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-d97706.svg" alt="MIT License" /></a>
  <a href="./scripts"><img src="https://img.shields.io/badge/Runtime-Python_3_Stdlib_Only-18181b.svg" alt="Python 3 Stdlib Only" /></a>
  <a href="#privacy--zero-telemetry"><img src="https://img.shields.io/badge/Privacy-100%25_Local_%26_Zero_Telemetry-18181b.svg" alt="100% Local & Zero Telemetry" /></a>
  <a href="./AGENTS.md"><img src="https://img.shields.io/badge/Works_with-Claude_Code_%C2%B7_Cursor_%C2%B7_Codex_%C2%B7_Antigravity_%C2%B7_WorkBuddy-27272a.svg" alt="Works with Claude Code, Cursor, Codex, Antigravity, WorkBuddy" /></a>
</p>

<p>
  <a href="https://silassolivagus.github.io/OpenPM/"><strong>Live Playground Portal</strong></a> ·
  <a href="https://silassolivagus.github.io/OpenPM/projects/ai-workspace-guardrails/walkthrough.html"><strong>Flagship Demo (EN)</strong></a> ·
  <a href="https://silassolivagus.github.io/OpenPM/projects/ai-workspace-guardrails-zh/walkthrough.html"><strong>Flagship Demo (ZH)</strong></a> ·
  <a href="https://silassolivagus.github.io/OpenPM/guide.html"><strong>Quickstart Manual</strong></a> ·
  <a href="https://silassolivagus.github.io/OpenPM/sponsor.html"><strong>Sponsor</strong></a>
</p>

</div>

> **Origin & Co-Creator**: OpenPM originated from core collaborator **[@roxorlt](https://github.com/roxorlt)**, his interaction design ideas, and his open-source project **[roxorlt/UEmaster](https://github.com/roxorlt/UEmaster)**, now co-built together with **[@SilasSolivagus](https://github.com/SilasSolivagus)**.

<p align="center">
  <img src="./assets/hero-demo.gif" alt="OpenPM 3-column interactive workbench and inline @component review" width="100%" />
</p>

---

## Why Traditional Docs & Raw AI Prompts Break in Spec Reviews

The biggest friction in product spec reviews isn't writing words — it's **tab-flipping and context loss**: scrolling through a 3,000-word doc on the left, hunting for a Figma frame in the middle, and checking a flowchart on the right. Nobody knows which rule governs which button, and asking an LLM to tweak one edge case quietly rewrites three other screens.

OpenPM compiles rough ideas into **one standalone offline HTML file where Flowchart, Clickable Prototype, and Logic Specs stay linked on a single screen**:

| Real Team Friction | Separate Docs + Raw LLM Chat | OpenPM 3-in-1 Linked Workbench |
| :--- | :--- | :--- |
| **Constant tab-flipping** | PRD prose, Figma frames, and flowcharts live in 3 separate tools; meetings stall over "the second button on the top right." | **Flow · Clickable UI · Logic Specs on One Screen**: Click any flow node to switch the live clickable screen and its rules; toggle condition variables to walk live `Yes/No` branches, switch `Web / App 375px` views, and draw live curves from spec cards straight to buttons. |
| **Messy async reviews & conflicting edits** | Hosting preview servers is tedious; Slack feedback gets lost or frontend and backend contradict each other on the same control. | **1-File HTML Chat Review + Conflict Interception**: Drop `walkthrough.html` into Slack/WeCom; teammates click any UI button to pin `@[Component]` notes. Conflicting notes on the same control pause automatically for PM sign-off. |
| **AI rewrites break other screens & hide sprint scope** | Asking AI to tweak one rule regenerates the whole doc; engineers can't tell new sprint scope apart from legacy screens. | **Surgical Local Write-back + 1-Click Sprint Delta**: Edits touch only the targeted control and PRD section (with `v1/v2` rollback snapshots). Pulls legacy Wiki docs to diff baselines and highlights only current-sprint changes on demand. |
| **Hours wasted pasting screenshots into Wiki** | Copy-pasting dozens of screenshots into Word or Confluence tables after sign-off; repeating the same prompt fixes next week. | **1-Click Side-by-Side Word/Wiki Export + Self-Evolving Taste**: Auto-captures clean Web + App screenshots into structured side-by-side `.docx`, Confluence XML, or WeCom docs, while a blind A/B judge locks your recurring preferences into `evals/taste-profile.md`. |

---

## 30-Second Agent Install

### Step 1: Paste one line into your AI coding agent

Open **Claude Code, Cursor, Codex, Antigravity, WorkBuddy, or `dsh`** and send:

```text
Install and initialize https://github.com/SilasSolivagus/OpenPM
```

Your agent clones OpenPM, asks 5 quick context questions (takes under a minute, or skip to use monochrome defaults), stores any Wiki credentials strictly inside local git-ignored `.env.local`, and asks for your first feature idea.

### Step 2: The Only 4 Plain-Language Prompts You Need

| Job to Be Done | Say This to Your Agent | What OpenPM Compiles Behind the Scenes |
| :--- | :--- | :--- |
| **1. Spec a 0-to-1 feature** | *"Spec a new feature for [resumable large-file uploads] with a PRD and clickable wireframe."* | Writes `prd.md`, builds 95% monochrome `pages/*.html` + orthogonal `flow.svg`, passes `preflight_check.py`, and outputs single-file `walkthrough.html`. |
| **2. Modify a live feature** | *"Here is our current Wiki link/doc. Add [VP sign-off when monthly AI spend exceeds $5,000]."* | Diffs the baseline first, keeps existing screens in grayscale, and marks only the delta nodes and controls in `#D97706` amber. |
| **3. Apply multi-reviewer feedback** | *"Merge the `.jsonl` review files from eng and QA, check for conflicts, and update the spec."* | Detects conflicting edits on the same `@[Component]`, asks you to resolve ties, rewrites only affected sections, and saves a `versions/vN` snapshot. |
| **4. Ship to Wiki / WeCom / Feishu** | *"This spec is final. Push the side-by-side table to Confluence / WeCom / Feishu."* | Packages screenshots + spec tables + `walkthrough.html.zip` to your target doc platform and logs rework metrics (`"Run a taste retrospective"` every 3 specs to update `evals/taste-profile.md`). |

### 1-Line Safe Upgrade (Keeps `.env.local` and `projects/` Intact)

Already running an earlier OpenPM workspace? Send this in your existing project session:

```text
Safely upgrade OpenPM from https://github.com/SilasSolivagus/OpenPM using python3 scripts/upgrade_openpm.py (keep my .env.local and projects/ intact) and re-verify my current walkthrough.html.
```

---

## Core Capabilities Inside `walkthrough.html`

Every compiled `walkthrough.html` is a zero-dependency single HTML file you can drop into Slack, WeCom, or email and open offline in any browser.

### 1. Flowchart · Clickable Prototype · Logic Specs — Linked on One Screen
Click any flow node on the left to switch the interactive UI prototype in the center (including instant `Web / App 375px` and empty/error state toggles) and view its exact rules on the right. Flip condition switches to test live `Yes/No` branches on the spot, or toggle **Delta Highlight** to isolate current-sprint changes from legacy screens:

![Flowchart, clickable prototype, and logic specs linked on one screen](./assets/shot-flow-delta.png)

### 2. Visual Spec Tethers: Point Every Rule Straight to Its Button
Switch to **Spec Delta** mode and click any requirement card on the right. OpenPM jumps to the target screen and draws a live curve directly to the exact input, modal, or button it governs — zero "second button on the top right" guesswork:

![Visual tether connecting a spec rule straight to its UI control](./assets/shot-spec-tether.png)

### 3. Click-to-Pin `@[Component]` Reviews & Multi-Reviewer Conflict Guard
Click **+ Add Note**, enter your name (e.g. `Maya · Frontend`), and click any button or input on the prototype to insert an `@[Component Name]` chip with full state context. Export `.jsonl` to merge team feedback, automatically catch conflicting edits on the same control, and apply surgical write-backs without breaking other screens:

![Click any UI button to insert an @component review chip](./assets/shot-inline-mention.png)

---

## Deterministic 6+1 Pipeline Architecture

<p align="center">
  <img src="./assets/pipeline-en.svg" alt="OpenPM 6+1 Deterministic Pipeline" width="100%" />
</p>

1. **`01-pull-wiki`**: Pulls existing Wiki / WeCom / Feishu pages into `history/prd-remote.md` and `history/pull-diff.md` (or initializes a 0-to-1 baseline).
2. **`02-draft-prd`**: Reads `evals/taste-profile.md` first, then authors structured `prd.md` with explicit state tables and edge cases.
3. **`03-prd-to-wireframe-prototype`**: Generates 100% monochrome `wt-*` wireframes (`pages/*.html`) with dot-namespaced `data-comp-id` anchors.
4. **`04-flow-canvas`**: Builds a Top-Down (`TD`) orthogonal `flow.svg` with clickable `D_*` decision diamonds and caps delta nodes at `<= 75%`.
5. **`05-flow-walkthrough`**: Runs `scripts/preflight_check.py` and `scripts/build_walkthrough.py` to compile a verified single-file `walkthrough.html`.
6. **`06-push-wiki`**: Publishes a single native WeCom online document, Confluence page, Feishu doc, or local Obsidian package via `scripts/wiki_sync.py`.
7. **`07-iterate-skills`**: Runs randomized double-blind A/B evaluation (`candidate_first` vs `baseline_first`) to promote proven rules into `evals/taste-profile.md`.

---

<details>
<summary><strong>🤖 Agent Auto-Install &amp; Onboarding Protocol (For AI Agents Reading This Repo)</strong></summary>

<br/>

> **Instructions for AI Agents (`Claude Code`, `Cursor`, `Codex`, `Antigravity`, `WorkBuddy`, `dsh`)**: When a user sends you this repository URL or asks to install/initialize `OpenPM`, execute setup silently and follow this exact 3-step onboarding flow (full rules in [AGENTS.md](./AGENTS.md)). **Never dump installation logs, process PIDs, port numbers, file byte sizes, or auto-start HTTP servers for sample projects.**
>
> 1. **Silent Clone & Workspace Bootstrap**:
>    - Clone this repository and copy `templates/.env.local.example` to `.env.local` if `.env.local` does not exist. If running inside `dsh`, symlink `skills/01-*` through `07-*` into `~/.dsh/skills/`.
>    - Match the user's conversation language automatically: English sessions produce English artifacts and set `"lang": "en"` in `spec.json`; Chinese sessions produce Chinese artifacts (`"lang": "zh"`).
> 2. **Two-Step Interactive Setup (Never Skip, Never Offload `.env.local` Editing to the PM)**:
>    - **Step A (`AskUserQuestion` - 5 Quick Questions)**: Ask concisely in one turn: (1) Company / team, (2) Core business domain, (3) Product name & target users, (4) Target form factors (`App 375px` / `PC Web` / `web-admin` / `Mini-Program` / `Multi-platform`), (5) Layout references (optional screenshots in chat or `references/`) & Wiki platform (`wecom` / `confluence` / `feishu` / `local-obsidian`).
>    - **Step B (Proactive Credential Collection Written to `.env.local`)**:
>      - If `wecom`: ask for `WECOM_BOT_ID` + `WECOM_BOT_SECRET` (or group webhook) and optional `WECOM_FOLDER_ID`, then write them directly to git-ignored `.env.local`.
>      - If `confluence`: ask for `WIKI_BASE_URL`, `CONFLUENCE_PAT`, and target space/parent page URL, then write them directly to `.env.local`.
>      - If `feishu`: ask for `FEISHU_APP_ID`, `FEISHU_APP_SECRET`, and optional wiki/folder URL, then write them directly to `.env.local`.
>      - **Fallback**: If the user skips keys or questions, never block; default cleanly to `local-obsidian` offline delivery and a standard grayscale `wt-*` `project-context.md`.
>    - **Hard Delivery Rule for WeCom & Feishu**: Local engineering source files (`project-context.md`, `spec.json`, `confluence-storage.xml`, raw `prd.md`, `wiki-page.html`, `pages/*.html`) are strictly for local agent compilation. **Never upload raw engineering `.xml`/`.md`/`.json` files as cloud-drive attachments to WeCom folders or Feishu directories**; pushing to WeCom must create or update a single native WeCom online document (`doc_type=3` or `11`).
> 3. **Concise Wrap-Up (`<= 10` Lines Total) & First Feature Prompt**:
>    - State clearly in 2 short sentences where local files live (`projects/<product>/` for Obsidian-ready specs and `.env.local` for local-only keys, with 100% zero telemetry) and when remote sync occurs (only when the PM confirms finalization and runs `06-push-wiki`).
>    - Share clickable links to **[guide.html](./guide.html)** and **[QUICKSTART.md](./QUICKSTART.md)**.
>    - Ask immediately: **"Everything is ready. What is the first feature you want to spec? (Share an existing doc/link to start from `01 Pull & Diff`, or describe a new idea to start from `02 Draft PRD`.)"**

</details>

<details>
<summary><strong>🛠️ Repository Layout &amp; CLI Reference (Executed Automatically by Your Agent)</strong></summary>

<br/>

### Core Directories
- `AGENTS.md` / `CLAUDE.md` / `WORKBUDDY.md` / `.cursorrules`: Cross-agent onboarding, monochrome invariants, and pipeline routing rules
- `skills/01-*` to `07-*`: Modular 6+1 pipeline skills from baseline diffing to randomized blind A/B self-evolution
- `specs/`: `spec-v2` JSON Schema, `data-comp-id` anchor contract, orthogonal `TD` flow rules, and preflight gate checks
- `adapters/`: Delivery adapters for WeCom (`wecom`), Confluence (`confluence`), Feishu (`feishu`), and Obsidian (`local-obsidian`)
- `projects/`: Isolated per-feature workspaces including runnable English and Chinese reference demos

### Deterministic Scripts (Python 3 Standard Library Only)
```bash
# 1. Static preflight check (validate spec.json before build, then walkthrough.html after build)
python3 scripts/preflight_check.py projects/ai-workspace-guardrails/spec.json

# 2. Compile self-contained 3-column interactive HTML
python3 scripts/build_walkthrough.py \
  --spec projects/ai-workspace-guardrails/spec.json \
  --svg projects/ai-workspace-guardrails/flow.svg \
  --pages-dir projects/ai-workspace-guardrails/pages \
  --out projects/ai-workspace-guardrails/walkthrough.html

python3 scripts/preflight_check.py projects/ai-workspace-guardrails/walkthrough.html

# 3. Pull Wiki baseline or push side-by-side wireframe + spec table
python3 scripts/wiki_sync.py pull projects/ai-workspace-guardrails
python3 scripts/wiki_sync.py push projects/ai-workspace-guardrails

# 4. Immutable version snapshots, structural diff, and instant rollback
python3 scripts/version_manager.py snapshot projects/ai-workspace-guardrails --note "Post-review update"
python3 scripts/version_manager.py diff projects/ai-workspace-guardrails v1 v2
python3 scripts/version_manager.py rollback projects/ai-workspace-guardrails v1

# 5. Lossless workspace upgrade
python3 scripts/upgrade_openpm.py
```

</details>

---

## Sponsor OpenPM

If OpenPM saves your team hours of wireframe rework, noisy spec reviews, and manual Wiki formatting, consider buying the author an iced coffee to fuel ongoing open-source releases:

<div align="center">
  <a href="https://silassolivagus.github.io/OpenPM/sponsor.html">
    <img src="./assets/sponsor-card.png" alt="Sponsor OpenPM - Buy Silas an Iced Coffee" width="760" />
  </a>
</div>

---

## Privacy, Credits & License

<a id="privacy--zero-telemetry"></a>

- **Co-Creator & Inspiration Credit**: OpenPM grew directly out of the original inspiration, interaction creativity, and open-source **[roxorlt/UEmaster](https://github.com/roxorlt/UEmaster)** project created by **[@roxorlt](https://github.com/roxorlt)**. Building on that foundation of linking orthogonal flow topologies to live wireframe walkthroughs, **[@SilasSolivagus](https://github.com/SilasSolivagus)** and **[@roxorlt](https://github.com/roxorlt)** co-built OpenPM's `spec-v2` deterministic compiler, 95% monochrome + 5% `#D97706` delta contract, multi-reviewer `@[Component]` conflict detection, native enterprise Wiki adapters, and double-blind A/B evaluation loop.
- **100% Local & Zero Telemetry**: OpenPM runs entirely on Python 3's standard library on your machine. There are zero analytics pings, zero cloud relays, and zero hidden network calls. Unreleased product specs stay on your disk until you explicitly push them to your own Wiki.
- **License**: Released under the [MIT License](./LICENSE) (Copyright © 2026 SilasSolivagus, roxorlt & Contributors). Star the repo on GitHub if OpenPM saves your team a painful spec review.
