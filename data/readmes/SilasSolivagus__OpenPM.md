<div align="center">

<img src="./assets/banner-en.svg" alt="OpenPM: A local tool for product managers that connects specs, flowcharts, wireframes, and reviews." width="100%" />

<br/>

<p>
  <strong>English</strong> | <a href="./README.zh-CN.md">简体中文</a>
</p>

<p>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-d97706.svg" alt="MIT License" /></a>
  <a href="./scripts"><img src="https://img.shields.io/badge/Runtime-Python_3_Stdlib_Only-18181b.svg" alt="Python 3 Stdlib Only" /></a>
  <a href="#privacy-credits--license"><img src="https://img.shields.io/badge/Privacy-Local_Only-18181b.svg" alt="Local Only" /></a>
  <a href="./AGENTS.md"><img src="https://img.shields.io/badge/Works_with-Claude_Code_%C2%B7_Cursor_%C2%B7_Codex_%C2%B7_Antigravity_%C2%B7_WorkBuddy-27272a.svg" alt="Works with Claude Code, Cursor, Codex, Antigravity, WorkBuddy" /></a>
</p>

<p>
  <a href="https://silassolivagus.github.io/OpenPM/"><strong>Playground</strong></a> ·
  <a href="https://silassolivagus.github.io/OpenPM/projects/ai-workspace-guardrails/walkthrough.html"><strong>Live Demo (EN)</strong></a> ·
  <a href="https://silassolivagus.github.io/OpenPM/projects/ai-workspace-guardrails-zh/walkthrough.html"><strong>Live Demo (ZH)</strong></a> ·
  <a href="https://silassolivagus.github.io/OpenPM/guide.html"><strong>Quickstart Guide</strong></a> ·
  <a href="https://silassolivagus.github.io/OpenPM/sponsor.html"><strong>Sponsor</strong></a>
</p>

</div>

> **In One Sentence**: A local tool for product managers that keeps PRDs, flowcharts, wireframes, and team reviews in sync. Change one place and everything updates; finalize once to export side-by-side visual docs without busywork.
>
> **Origin & Co-Creator**: OpenPM grew out of **[roxorlt/UEmaster](https://github.com/roxorlt/UEmaster)** and the interaction design work of **[@roxorlt](https://github.com/roxorlt)**, co-built with **[@SilasSolivagus](https://github.com/SilasSolivagus)**.

<p align="center">
  <img src="./assets/hero-demo.gif" alt="OpenPM 3-column workbench and inline @component review" width="100%" />
</p>

---

## Stop Pulling Blind Boxes with Raw AI Prompts

For most teams, asking an LLM to write product specs and prototypes feels like opening a blind box: sometimes it looks fine, and ten minutes later one small edit breaks three other screens. OpenPM turns that guesswork into a predictable local workshop with zero setup, a built-in quality inspector, point-and-click team reviews, and a mistake log that improves over time.

1. **Let AI fill out structured forms instead of hand-coding full web apps**
   Asking an AI to write a full interactive prototype from scratch falls apart fast. In OpenPM, the AI only writes clean spec lists and small HTML page fragments. Fixed Python scripts assemble the layout, state wiring, and interactions every time. Mobile (`375px`) and desktop share one base definition, so a single edit updates both.
2. **Zero environment headaches: runs on built-in Python**
   Many open-source tools ask PMs to install Node packages, browser drivers, or Word plugins before doing anything useful. OpenPM uses only the standard Python 3 already on your computer to drive local Chrome for screenshots and build native `.docx` files directly. Nothing extra to install.
3. **A strict quality inspector that rejects bad output automatically**
   Prompt rules like "stick to grayscale," "keep flowchart lines straight," or "don't miss a branch" are easy for models to forget. OpenPM enforces them in code (`preflight_check.py`): if the AI sneaks in extra colors, misaligns a connector, or drops a state, the check blocks the build until the AI fixes it.
4. **No preview server needed: drop one HTML file into chat to review and catch conflicts**
   Send the single `walkthrough.html` file in Slack or WeCom. Engineers and QA click any button on the wireframe to attach a comment, then export `.jsonl`. When you merge their files, OpenPM checks whether frontend and QA asked for opposite changes on the same button, flags conflicts for you to settle, and then edits only that specific section instead of rewriting the whole PRD.
5. **An AI mistake log backed by blind A/B tests**
   Each time you finalize a spec, OpenPM measures how much of the initial draft you had to rework and logs recurring fixes. Once enough notes pile up, it proposes rule updates and tests old vs. new output in randomized blind order before keeping an improvement.
6. **Automatic side-by-side doc pairing, secret redaction, and honest exit codes**
   When exporting to Word or Wiki, OpenPM matches each screen's grayscale screenshot with its exact spec rules (including nested multi-state `Prototype | Spec` sub-tables and character-level HTML diff reports) without repeating text. Tokens in logs are redacted automatically, and if screenshot capture or remote upload fails, it reports the real error instead of pretending the push succeeded.

---

## Quick Setup

### 1. Paste one prompt into your coding agent

Open **Claude Code, Cursor, Codex, Antigravity, WorkBuddy, or `dsh`** and send:

```text
Install and initialize https://github.com/SilasSolivagus/OpenPM
```

The agent clones the repo, asks five short setup questions (skip them to use the grayscale defaults), saves any Wiki tokens into a local git-ignored `.env.local`, and asks what feature you want to work on first.

### 2. Everyday Prompts

| Task | Example Prompt | What Happens |
| :--- | :--- | :--- |
| **1. Draft a new feature** | *"Spec a new feature for [resumable large-file uploads] with a PRD and clickable wireframe."* | Checks past notes, writes `prd.md`, builds grayscale `pages/*.html` and a top-down `flow.svg`, passes the preflight check, and outputs `walkthrough.html`. |
| **2. Change an existing feature** | *"Here is our current Wiki doc. Add [VP approval when monthly AI spend passes $5,000]."* | Pulls the baseline and writes a character-level `history/pull-diff-report.html`, keeps legacy screens grayscale, and marks only new or changed parts in `#D97706` amber. |
| **3. Merge team review notes** | *"Merge the `.jsonl` review files from eng and QA, flag any conflicts, and update the spec."* | Spots conflicting comments on the same `@[Component]`, asks you to decide, updates only the affected sections, and saves a `versions/vN` snapshot. |
| **4. Publish to Wiki / WeCom / Feishu** | *"This spec is final. Push the side-by-side table to Confluence / WeCom / Feishu."* | Captures grayscale screenshots (including multi-state sub-tables), writes `wiki-export/push-diff-report.html` locally, and syncs to your doc platform. |

### Updating an Existing Workspace

Already using an earlier version? Run this in your project session to update scripts while keeping `.env.local` and `projects/` untouched:

```text
Upgrade OpenPM from https://github.com/SilasSolivagus/OpenPM using python3 scripts/upgrade_openpm.py (keep my .env.local and projects/ intact) and re-verify my current walkthrough.html.
```

---

## What's Inside `walkthrough.html`

Every build outputs one standalone HTML file with zero external requests. Double-click it in any browser to review offline.

### 1. Linked Flowchart, Wireframe, and Rules
Click a node in the flowchart on the left to load its wireframe in the center (with `Web / App 375px` and multi-state switches) and its spec on the right. Flip condition toggles to walk `Yes/No` branches live, or turn on **Delta Highlight** to see only what changed in this sprint:

![Flowchart, clickable prototype, and logic specs linked on one screen](./assets/shot-flow-delta.png)

### 2. Visual Spec Tethers
Switch to **Spec Delta** view and click a requirement card on the right. The canvas jumps to the target screen and draws a line straight to the input, modal, or button it governs:

![Visual tether connecting a spec rule straight to its UI control](./assets/shot-spec-tether.png)

### 3. Point-and-Click `@[Component]` Comments & Conflict Checks
Click **+ Add Note**, type your name (for example, `Maya · Frontend`), and click any control on the wireframe to insert an `@[Component Name]` tag along with the active branch state. Teammates send back `.jsonl` files; OpenPM merges them and pauses if two people ask for opposite edits on the same control:

![Click any UI button to insert an @component review chip](./assets/shot-inline-mention.png)

---

## How the 6+1 Workflow Runs

<p align="center">
  <img src="./assets/pipeline-en.svg" alt="OpenPM 6+1 Workflow" width="100%" />
</p>

1. **`01-pull-wiki`**: Pulls an existing Wiki / WeCom / Feishu page into `history/prd-remote.md` and generates both `pull-diff.md` and a visual `pull-diff-report.html`.
2. **`02-draft-prd`**: Reads `evals/taste-profile.md` for past preferences and mistake logs, then writes or updates `prd.md`.
3. **`03-prd-to-wireframe-prototype`**: Outputs monochrome `wt-*` wireframe fragments (`pages/*.html`) with `data-comp-id` anchors.
4. **`04-flow-canvas`**: Builds a top-down (`TD`) orthogonal `flow.svg` with `D_*` decision nodes and caps delta nodes at `75%`.
5. **`05-flow-walkthrough`**: Runs `scripts/preflight_check.py` to catch contract violations, then assembles `walkthrough.html` via `scripts/build_walkthrough.py`.
6. **`06-push-wiki`**: Pairs grayscale screenshots with spec rules into `.docx`, Confluence Storage XML, and `wiki-page.html` (supporting multi-state `Prototype | Spec` sub-tables), writes a local `push-diff-report.html`, and pushes to your Wiki.
7. **`07-iterate-skills`**: Tracks draft-to-final rework rates and runs blind A/B comparisons (`candidate_first` vs `baseline_first`) before promoting new rules into `evals/taste-profile.md`.

---

<details>
<summary><strong>Agent Auto-Install &amp; Onboarding Protocol (For AI Agents)</strong></summary>

<br/>

> **Instructions for AI Agents (`Claude Code`, `Cursor`, `Codex`, `Antigravity`, `WorkBuddy`, `dsh`)**: When a user gives you this repo URL or asks to set up `OpenPM`, run setup quietly and follow these 3 steps (details in [AGENTS.md](./AGENTS.md)). **Do not print install logs, PIDs, port numbers, or byte counts, and do not start an HTTP server for sample projects.**
>
> 1. **Clone & Prepare**:
>    - Clone the repo and copy `templates/.env.local.example` to `.env.local` if missing. In `dsh`, symlink `skills/01-*` through `07-*` into `~/.dsh/skills/`.
>    - Match the user's language: English chats set `"lang": "en"` in `spec.json`; Chinese chats use `"lang": "zh"`.
> 2. **Ask Setup Questions & Write `.env.local` Yourself**:
>    - **Step A (`AskUserQuestion` - 5 Questions)**: Ask in one turn: (1) Company or team, (2) Business domain, (3) Product name & audience, (4) Form factors (`App 375px` / `PC Web` / `web-admin` / `Mini-Program` / `Multi-platform`), (5) Layout references (optional screenshots) & Wiki platform (`wecom` / `confluence` / `feishu` / `local-obsidian`).
>    - **Step B (Credentials)**:
>      - `wecom`: ask for `WECOM_BOT_ID` + `WECOM_BOT_SECRET` (or webhook) and optional `WECOM_FOLDER_ID`, then write them to `.env.local`.
>      - `confluence`: ask for `WIKI_BASE_URL`, `CONFLUENCE_PAT`, and target space/parent page URL, then write them to `.env.local`.
>      - `feishu`: ask for `FEISHU_APP_ID`, `FEISHU_APP_SECRET`, and optional folder URL, then write them to `.env.local`.
>      - If the user skips keys or questions, fall back to `local-obsidian` and standard grayscale `wt-*` defaults without blocking.
>    - **Remote Upload Rule**: Keep `project-context.md`, `spec.json`, raw `prd.md`, `pages/*.html`, and `*-diff-report.html` local. Never upload raw engineering source files to WeCom Drive or Wiki folders.
> 3. **Short Wrap-Up (`<= 10` Lines)**:
>    - Tell the PM where local files live (`projects/<product>/` for specs, `.env.local` for keys, zero telemetry) and that remote sync only happens when they run `06-push-wiki`.
>    - Link **[guide.html](./guide.html)** and **[QUICKSTART.md](./QUICKSTART.md)**.
>    - Ask: **"Everything is ready. What is the first feature you want to spec? (Share an existing doc/link to start from `01 Pull & Diff`, or describe a new idea to start from `02 Draft PRD`.)"**

</details>

<details>
<summary><strong>Repository Layout &amp; CLI Commands</strong></summary>

<br/>

### Directories
- `AGENTS.md` / `CLAUDE.md` / `WORKBUDDY.md` / `.cursorrules`: Agent entry rules and grayscale wireframe constraints
- `skills/01-*` to `07-*`: Step-by-step skill definitions
- `specs/`: `spec-v2` JSON Schema, `data-comp-id` anchor spec, orthogonal `TD` flowchart spec, and preflight checks
- `adapters/`: Platform rules for WeCom (`wecom`), Confluence (`confluence`), Feishu (`feishu`), and Obsidian (`local-obsidian`)
- `projects/`: Feature workspaces, including English and Chinese demos

### CLI Scripts (Built-in Python 3 Only)
```bash
# 1. Run quality checks (on spec.json before build, and walkthrough.html after build)
python3 scripts/preflight_check.py projects/ai-workspace-guardrails/spec.json

# 2. Assemble the single-file interactive HTML workbench
python3 scripts/build_walkthrough.py \
  --spec projects/ai-workspace-guardrails/spec.json \
  --svg projects/ai-workspace-guardrails/flow.svg \
  --pages-dir projects/ai-workspace-guardrails/pages \
  --out projects/ai-workspace-guardrails/walkthrough.html

python3 scripts/preflight_check.py projects/ai-workspace-guardrails/walkthrough.html

# 3. Pull baseline or push side-by-side wireframe + spec table (also writes HTML diff reports)
python3 scripts/wiki_sync.py pull projects/ai-workspace-guardrails
python3 scripts/wiki_sync.py push projects/ai-workspace-guardrails

# 4. Generate a batch sync diff report across all projects
python3 scripts/wiki_diff_report.py projects/ --batch -o projects/_diff-report.html

# 5. Version snapshots, diff, and rollback
python3 scripts/version_manager.py snapshot projects/ai-workspace-guardrails --note "Post-review update"
python3 scripts/version_manager.py diff projects/ai-workspace-guardrails v1 v2
python3 scripts/version_manager.py rollback projects/ai-workspace-guardrails v1

# 6. Upgrade workspace scripts without overwriting .env.local or projects/
python3 scripts/upgrade_openpm.py
```

</details>

---

## Sponsor

If OpenPM saves you time on wireframes, spec reviews, or Wiki formatting, you can buy the author an iced coffee here:

<div align="center">
  <a href="https://silassolivagus.github.io/OpenPM/sponsor.html">
    <img src="./assets/sponsor-card.png" alt="Sponsor OpenPM" width="760" />
  </a>
</div>

---

## Privacy, Credits & License

- **Credits**: OpenPM started from **[@roxorlt](https://github.com/roxorlt)**'s ideas and open-source project **[roxorlt/UEmaster](https://github.com/roxorlt/UEmaster)**, which paired orthogonal flowcharts with interactive wireframe walkthroughs. **[@SilasSolivagus](https://github.com/SilasSolivagus)** and **[@roxorlt](https://github.com/roxorlt)** expanded it with the `spec-v2` assembler, grayscale + `#D97706` amber delta checks, `@[Component]` review conflict detection, Wiki/WeCom/Feishu exporters, visual diff reports, and blind-tested mistake logs.
- **Local & Private**: Built on Python 3's standard library with secret redaction in logs and zero analytics, cloud relays, or background network calls. Files stay on your disk unless you run `wiki_sync.py` against your own Wiki.
- **License**: [MIT License](./LICENSE) (Copyright © 2026 SilasSolivagus, roxorlt & Contributors).
