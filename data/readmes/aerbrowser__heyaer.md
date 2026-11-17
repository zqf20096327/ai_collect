<p align="center">
  <img src="assets/brand/aer-icon.svg" width="104" alt="Aer browser icon" />
</p>

<h1 align="center">Aer</h1>
<p align="center"><strong>Aer — A Browser Built Around Your Workspace and AI.</strong></p>
<p align="center">Familiar browsing. AI beside your pages. Agents that work with your context.</p>
<p align="center">
  <a href="https://heyaer.com">Website</a> ·
  <a href="https://github.com/aerbrowser/heyaer/releases/latest">Download for Mac</a> ·
  <a href="#install-the-aer-browser-skill">Install the Codex Skill</a> ·
  <a href="https://github.com/aerbrowser/heyaer/issues">Feedback &amp; Issues</a>
</p>
<p align="center">Chromium · Apple Silicon · macOS 13+ · Independently built</p>

![Aer's English workspace, browsing the official heyaer.com website](assets/screenshots/01-workspace.png)

Your browser is where research starts, ideas take shape, and work gets done. Aer brings those activities together: organize projects in Spaces, ask AI about the pages you are reading, and give agents a clear goal and the tools to help you move forward.

Built on Chromium for macOS, Aer combines a native desktop interface with the websites and Chrome extensions you already use. If you enjoyed Arc's approach to browsing, you will find familiar ideas here—and a new focus on working with AI.

**Available to try today, and evolving quickly.** This public repository is the home for official downloads, automatic updates, product documentation, and the `aer-browser` skill. The browser application's source is maintained separately.

## Three reasons to try Aer

| Keep your flow | Work with AI in context | Give agents a place to work |
| --- | --- | --- |
| Vertical tabs, Spaces, shared pins, folders, split view, themes, and a command window. Bring supported data from Arc, Chrome, or Safari. | Reference up to **8 open tabs**. Summarize, translate, compare, extract, and draft beside the source. Choose your own compatible model service. | Start with **24 Bot templates** and **20 app connectors**. Add goals, memory, resource scope, and schedules. Connect Codex to your open pages with the browser skill. |

## Download and get started

**Requires an Apple Silicon Mac running macOS 13 or later.** The current release does not include Intel Mac, Windows, or Linux builds.

1. Open the [latest release](https://github.com/aerbrowser/heyaer/releases/latest) and download the file ending in **`-mac-arm64.dmg`**.
2. Open the DMG and drag **AER.app** into **Applications**. If replacing an existing copy, quit Aer normally first.
3. Open Aer, create a Space, and bring in your browser data. **Basic browsing works without signing in.**
4. To use AI, check your access in **Settings → Account & membership**, then add a model connection in **AI Assistant**.

Official release packages are signed with Apple Developer ID and notarized by Apple. Builds with the updater check GitHub daily; use **Aer → Check for Updates…** to check manually. Installation requires your confirmation. If your older build has no updater, install the current DMG once to get started. Downloads do not require a GitHub account.

[Explore Aer and available plans at heyaer.com →](https://heyaer.com)

## A workspace for every kind of work

Keep a project, a research topic, or your personal reading in its own Space. Vertical tabs make page titles easier to scan, while shared pins keep everyday tools within reach.

- **Spaces:** Give each workspace a name, icon, and color; switch from the Space bar.
- **Vertical tabs:** See more of each page title and organize tabs without a crowded horizontal strip.
- **Shared pins:** Keep essential sites across Spaces; organize ordinary tabs, favorites, and folders within each Space.
- **Folders and drag-and-drop:** Group related pages, reorder them, and move them to the right place.
- **Side-by-side split view:** Read two existing pages together—compare documentation, review alternatives, or keep a reference beside your work.
- **Profiles:** Use separate browser Profiles when you need separate logins and cookies. Spaces organize work within a Profile; they do not isolate account sessions.

### Keep familiar habits when you switch

Choose **Aer → Import from Another Browser…** to preview supported data before importing.

| Coming from | Supported import categories |
| --- | --- |
| **Arc** | Spaces, pinned and ordinary tabs, folders, and supported passwords, history, and address data |
| **Chrome** | Bookmarks and supported passwords, history, and address data |
| **Safari** | Bookmarks, folders, and Reading List URLs |

Available categories depend on the source browser and macOS permissions; the import preview shows what can be brought over. Install supported extensions from the **Chrome Web Store** using the normal permission prompts. Compatibility varies by extension and Aer version.

## One command window for your next step

![Keyboard shortcuts in Aer's English interface](assets/screenshots/02-shortcuts.png)

Press **⌘N** to open the command window. Enter an address, search the web, switch back to an open page, or move into an AI question.

| Action | Shortcut |
| --- | --- |
| Open command window | `⌘N` |
| Enter or edit the address | `⌘L` |
| Open a new tab | `⇧⌘N` |
| Toggle AI chat | `⌥⌘G` |

## AI beside the pages you are reading

![Aer's English AI Assistant settings for connecting your preferred model service](assets/screenshots/03-ai.png)

Use the right-hand AI panel to ask questions, follow up, start a new conversation, or stop an answer as it streams. Type **`@`** to find and reference up to **8 open tabs** in one conversation.

Compare proposals without copying each page into a chat. Turn a long article into an action list. Ask where two sources agree—and where you need to look closer.

| Command | What you can do |
| --- | --- |
| `/summarize` | Summarize one page or synthesize several referenced pages |
| `/translate` | Translate and explain page content |
| `/extract` | Pull out facts, conclusions, and action items |
| `/reply` | Draft a response using the selected page context |
| `/fill` | Preview values for an ordinary web form, then approve their application |

**Your choice of model.** Save multiple connections, configure the service URL, model ID, and API key, fetch available models, and test a connection. Bring a compatible model service that suits your work; its pricing and usage terms apply.

For AI analysis, selected page context is sent to your chosen model provider. Long pages are bounded by the context budget. Form filling shows a preview and requires approval; it does not automatically submit forms or handle passwords, verification codes, or payment fields.

## Turn recurring work into a Bot

![Aer's English library of Bot templates](assets/screenshots/04-bots.png)

A useful agent needs more than a prompt. In Aer, a Bot can have its own **goal, selected resources, memory, model connection, schedule, and run history**. Create several Bots from the same template and give each a different scope.

Start in **Settings → Bot library** with one of **24 templates**:

| Category | Templates |
| --- | --- |
| **Media** | Topic radar · Content repurposing · Editorial calendar · Copy editor · Community listening |
| **Web & research** | Competitor watch · SEO content brief · Website content audit · Research fact-check |
| **Daily work** | Inbox digest · Calendar briefing · Meeting recap · Task prioritization · Team discussion digest |
| **Product & projects** | Project risk review · PR review queue · Requirements brief · Issue digest |
| **Sales & operations** | Prospect research · Customer follow-up · Spreadsheet briefing · Event request review · Office operations · SaaS subscription review |

Run manually or choose an interval, a daily schedule, or a weekly schedule with a time zone. Each Bot keeps its execution history so you can review results and see what happened. Chat, agents, and messages provide places for immediate questions, ongoing tasks, and past results.

Scheduled and resident Bots require **Aer Pro**. Scheduling runs on your Mac: **Aer must remain running and the Mac awake**. Templates provide starting points for reading, analysis, reminders, and drafts; available actions depend on the connected tools and your authorization.

### Connect the tools your work already lives in

Choose from **20 app connectors**, then select the accounts and resources a task can use.

| Area | Apps |
| --- | --- |
| Knowledge & documents | Notion · Google Drive · Google Docs · Google Sheets · OneDrive · Dropbox |
| Development & projects | GitHub · Linear · Asana · Trello · ClickUp · Airtable · Todoist |
| Email & calendar | Gmail · Outlook · Google Calendar |
| Teams & communities | Slack · Microsoft Teams · Discord · Reddit |

In **Settings → Connected Apps**, configure the service using its supported credentials or OAuth flow. Some services require OAuth provider setup. After connecting, choose the repositories, documents, channels, projects, or calendars relevant to the task. Supported actions vary by connector, and connecting an account does not grant every possible action.

## Keep useful pages in your own library

Save material you want to return to with three built-in local export commands. The browser skill below can also invoke these exports.

| Command | Output | Useful for |
| --- | --- | --- |
| `/markdown` | Structured Markdown with headings, lists, code, tables, and source information | Research notes and document archives |
| `/screenshot` | A full-page PNG, with automatic scrolling and restoration of your reading position | Sharing layouts and preserving long pages |
| `/wechat` | A supported WeChat article as Markdown with local images in a selected Obsidian vault | Offline reading and a searchable personal library |

Exports run locally without a language-model call. Markdown and PNG exports default to **Downloads / Aer Exports**; WeChat clipping requires selecting an existing Obsidian vault. The current release still requires BYOK or Pro access for these export skills. Pages must be accessible in your browser; nested scroll areas, virtual lists, and unloaded content may need additional handling.

## Make your browser feel like yours

![Aer's five themes and sidebar settings in English](assets/screenshots/05-appearance.png)

- **Five themes:** Lavender, Rose, Sand, Ocean, and Midnight.
- **Adjustable sidebar:** Set its width and optionally reveal a collapsed sidebar on hover.
- **Personal new-tab page:** Configure backgrounds, shortcuts, to-dos, and news sources.
- **Shareable page captures:** Adjust background colors, portrait or landscape composition, padding, and corners, then copy the result to the clipboard.
- **Everyday browser tools:** Downloads, find-in-page, address editing, developer tools, and a toolbar for local development pages.
- **Language choices:** English, Chinese, and Japanese. Some surfaces in the current app still have untranslated text.

## Access, models, and your data

| Capability | Current access requirement |
| --- | --- |
| Basic browsing | No sign-in required |
| AI, webpage tasks, local export skills, and connector configuration | Aer BYOK or Pro |
| Resident and scheduled Bots | Aer Pro |

**BYOK means bring your own model service.** Installing Aer or its browser skill does not include model API credits. Third-party apps require their own accounts and authorization. See [heyaer.com](https://heyaer.com) and **Account & membership** in Aer for available plans and access.

Browser data and task records are stored locally. AI tasks send the selected context to your configured model service; connected services receive the requests needed for the authorized work. Web actions and external writes follow the applicable permissions and confirmation flows.

The screenshots use the English interface and an isolated demonstration profile. The workspace screenshot shows Aer browsing heyaer.com; the website's product walkthrough is a scripted illustration.

## Built independently. Shaped by the people who use it.

“I started Aer with a question: what would a browser built for the AI era feel like? I wanted the workspace habits I liked in Arc, AI that could work with the pages in front of me, and agents with a practical place to help. Aer is my attempt to bring those pieces together.”

— **Asta, creator of Aer**

Aer is available now and still moving fast. If you enjoy exploring browsers, AI, or agent workflows, try it with a real project and tell us what worked—and what got in your way.

- [Download Aer](https://github.com/aerbrowser/heyaer/releases/latest) and explore [heyaer.com](https://heyaer.com).
- [Open an issue](https://github.com/aerbrowser/heyaer/issues) for a bug, an interaction that feels wrong, or a feature you would use. Include your Aer version, macOS version, and reproduction steps for bugs; remove private data from screenshots and logs.
- **Star this repository** if you want to support an independent browser project and help more people find it.

## Install the aer-browser Skill

**Let Codex work with the pages you already have open in Aer.**

The `aer-browser` skill connects Codex to Aer's bundled native CLI. It reads the installed app's live capability guide, discovers running browser sessions, and works with the pages selected for your task. It can reuse the sign-in state of that browser session, read page content and controls, click, fill, scroll, navigate, and export material.

The launcher needs **no browser extension, MCP server, Node.js, or Python**. The installed app supplies the actual browser capabilities.

**[Download aer-browser-skill.zip](https://raw.githubusercontent.com/aerbrowser/heyaer/main/downloads/aer-browser-skill.zip)** · [Skill source](skills/aer-browser/SKILL.md) · [SHA-256 checksum](downloads/SHA256SUMS)

### 1. Prepare Aer and Codex

- Install and open Aer, preferably at `/Applications/AER.app`.
- Open the pages you want Codex to use. Sign in to websites yourself where needed.
- Use a Codex installation with skill support. Webpage tasks and exports require the relevant Aer BYOK or Pro access; installing this package does not change your app entitlements.

### 2. Download and install

Download the ZIP above, extract it, open a terminal in the extracted `aer-browser` folder, and run:

```bash
bash scripts/install-codex.sh --app "/Applications/AER.app"
```

Or download and install from the terminal:

```bash
aer_skill_dir="$(mktemp -d)"
curl --fail --location \
  "https://raw.githubusercontent.com/aerbrowser/heyaer/main/downloads/aer-browser-skill.zip" \
  --output "$aer_skill_dir/aer-browser-skill.zip"
unzip -q "$aer_skill_dir/aer-browser-skill.zip" -d "$aer_skill_dir"
bash "$aer_skill_dir/aer-browser/scripts/install-codex.sh" \
  --app "/Applications/AER.app"
```

The default destination is `${CODEX_HOME:-$HOME/.codex}/skills/aer-browser`. The installer saves the chosen app path and backs up an existing skill outside the discovery directory, under `skill-backups`. It does not copy your browser or browsing profile.

For a different app location, use its absolute path:

```bash
bash scripts/install-codex.sh --app "$HOME/Applications/AER.app"
```

To choose a custom skill directory, add `--dest /absolute/path/to/skills/aer-browser`. No shell configuration or global PATH change is needed.

### 3. Check the installation

For the default installation, run:

```bash
bash "${CODEX_HOME:-$HOME/.codex}/skills/aer-browser/scripts/aer-browser.sh" --resolve
bash "${CODEX_HOME:-$HOME/.codex}/skills/aer-browser/scripts/aer-browser.sh" skill
bash "${CODEX_HOME:-$HOME/.codex}/skills/aer-browser/scripts/aer-browser.sh" profiles
```

- **`--resolve`** prints the native `aer-browser` executable inside your chosen app.
- **`skill`** prints the installed Aer version's complete guide and ends with `[aer-browser:skill] end of guide`.
- **`profiles`** returns a JSON session list. If it is empty, open the selected Aer application and retry.

### 4. Try it in Codex

Start a new Codex conversation after installing. If the skill is not discovered, reopen Codex. Mention **`$aer-browser`** in your request:

> Use $aer-browser to read the article I have open in Aer. Summarize its main claims, supporting evidence, and points that need verification.

> Use $aer-browser to compare the two product pages I selected in Aer. Make a table of pricing, features, and who each product is for.

> Use $aer-browser to export the open article as Markdown to my research folder.

> Use $aer-browser to capture a full-page screenshot of the page I am reading.

> Use $aer-browser to prepare the ordinary form fields on this open page using the information I provide. Let me review the values before applying them.

Codex discovers actual sessions and tabs, limits the task to relevant pages, observes page text and visible controls, and verifies the result after acting. Available operations come from the installed app's live guide.

### 5. Updates and troubleshooting

| Situation | What to do |
| --- | --- |
| Aer cannot be found | Install the app, then rerun the installer with its absolute `--app` path |
| More than one Aer installation exists | Use `--app` to select the intended copy explicitly |
| `profiles` returns no sessions | Open that Aer application; select the actual session if multiple Profiles are running |
| A page is outside the task scope | Open it in Aer and explicitly select it for a new task |
| An action is waiting for confirmation | Review and approve it yourself in Aer's task/confirmation panel |
| An account-access error appears | Check BYOK or Pro access in Account & membership; reinstalling the skill does not change access |
| The Aer app moved | Reinstall the skill with the new `--app` path |
| You want to update the skill | Download the ZIP again and rerun the installer; the previous skill is backed up |
| You updated Aer | The skill reads the app's current guide; it does not need a copied snapshot of old capabilities |

The current public CLI works with selected, already-open **HTTP(S) pages**. It does not provide arbitrary JavaScript or CDP access, tab creation, or file uploads. Passwords, verification codes, payments, iframes, shadow-tree controls, and canvas interactions need direct user handling or another appropriate tool. An agent must not approve its own sensitive actions.

See the [workflow guide](skills/aer-browser/references/workflow.md), [installation reference](skills/aer-browser/references/install.md), and [troubleshooting guide](skills/aer-browser/references/troubleshooting.md) for details. The public skill package is self-contained; it does not require access to Aer's source repository.

---

**Make room for your next idea. [Get Aer →](https://heyaer.com)**
