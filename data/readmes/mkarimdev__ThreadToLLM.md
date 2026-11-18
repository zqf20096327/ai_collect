# ThreadToLLM

[![CI](https://github.com/mkarimdev/ThreadToLLM/actions/workflows/ci.yml/badge.svg)](https://github.com/mkarimdev/ThreadToLLM/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v0.1.0-green.svg)](package.json)
[![Manifest V3](https://img.shields.io/badge/Chrome%20Extension-Manifest%20V3-informational.svg)](manifest.json)

Extract Reddit discussion threads into token-dense, clean Markdown optimized for LLM prompting (Claude, ChatGPT, Gemini, Local models).

---

> [!IMPORTANT]
> ### 🔒 100% Client-Side Privacy Guarantee
> - **Zero Telemetry**: No analytics beacons, tracking pixels, or error telemetry pings.
> - **Zero Analytics**: No third-party monitoring libraries, trackers, or user telemetry of any kind.
> - **No External Servers**: ThreadToLLM never transmits data over the network; no backend server exists.
> - **100% Client-Side DOM Extraction**: Discussion parsing, noise filtering, and Markdown serialization execute entirely in your local browser sandbox.
> - **Minimal Permissions**: ThreadToLLM requests only the single `clipboardWrite` permission required to copy extracted Markdown to your clipboard, plus standard host access for `reddit.com`.
> - **Fully Auditable Open Source**: Every line of code is open and inspectable under the permissive [MIT License](LICENSE).

---

## Before & After

Raw copy-pasting from Reddit inundates your context window with useless UI chrome, award icons, karma arrows, timestamps, and broken reply chains. ThreadToLLM reconstructs the conversation into token-dense, structured Markdown with YAML frontmatter, cutting token bloat by **70% to 85%** while preserving strict hierarchical relationships.

### Visual Comparison

| Feature | Raw Reddit Copy-Paste | ThreadToLLM Markdown |
| :--- | :--- | :--- |
| **Token Overhead** | ~4,200 tokens (bloated with UI buttons, avatars, karma counters, ads, collapse links) | ~650 tokens (**~85% token reduction**) |
| **Conversation Hierarchy** | Completely lost (flat text with ambiguous indentation or broken bullets) | Deeply preserved recursive indentation (`- **[+score] author**:`) |
| **Original Poster (OP)** | Unmarked or scattered across badges | Explicit `(OP)` attribution on every reply |
| **Context Metadata** | Missing post metadata and URL | Structured YAML frontmatter (`source`, `title`, `url`, `author`) |
| **Media & Hyperlinks** | Mangled markup and lost URLs | Clean Markdown link preservation and media URLs |
| **Bot / Moderator Noise** | Clutters discussion with boilerplate disclaimers | Automatically pruned by Filter Pipeline |

#### ❌ Raw Reddit Copy-Paste (Messy & Token-Bloated)

```text
r/LocalLLaMA • Posted by u/local_researcher 5 hours ago
Discussion: Why local models need structured context
Upvote 256 Downvote 42 comments Share Save Report Hide
level 1
ai_engineer • 4 hr. ago • Edited 2 hr. ago
Gold Award
I usually copy the whole page, but ChatGPT hallucinates who replied to whom because standard pasting is a flat wall of text.
Reply Give Award Share Report Save Follow
level 2
local_researcher • OP • 3 hr. ago
Exactly! Plus 80% of tokens are wasted on usernames, timestamps, karma numbers, and buttons. Check out my benchmark: https://i.redd.it/test-chart.png
Reply Give Award Share Report Save Follow
level 3
prompt_crafter • 2 hr. ago
And automoderator comments waste another 500 tokens before you even get to the real discussion.
```

#### ✅ ThreadToLLM Markdown (Token-Dense & LLM-Optimized)

```markdown
---
source: "reddit"
title: "Why local models need structured context"
url: "https://www.reddit.com/r/LocalLLaMA/comments/1abc123/why_local_models_need_structured_context/"
author: "local_researcher"
---

# Why local models need structured context

Discussion: Why local models need structured context

- **[+184] ai_engineer**: I usually copy the whole page, but ChatGPT hallucinates who replied to whom because standard pasting is a flat wall of text.
  - **[+92] local_researcher (OP)**: Exactly! Plus 80% of tokens are wasted on usernames, timestamps, karma numbers, and buttons. Check out my benchmark: https://i.redd.it/test-chart.png
    - **[+45] prompt_crafter**: And automoderator comments waste another 500 tokens before you even get to the real discussion.
```

---

## Installation

Get up and running in under a minute with our 3-step Quickstart:

1. **Download the Release ZIP**: Download the latest pre-compiled `thread-to-llm-v*.zip` archive from [GitHub Releases](https://github.com/mkarimdev/ThreadToLLM/releases).
2. **Unzip the Archive**: Unzip the downloaded file into a folder on your computer.
3. **Load Unpacked into Chrome**:
   - Open Chrome and navigate to `chrome://extensions`.
   - Enable **Developer mode** using the toggle switch in the upper-right corner.
   - Click the **Load unpacked** button and select the unzipped extension directory.

---

## Usage

ThreadToLLM integrates seamlessly into your browsing experience without intrusive popups:

- **In-Page Action Button**: Mounted directly beside the native "Share" button in Reddit's action bar. Click it once to extract the active discussion thread; transient checkmark micro-feedback confirms the Markdown has been copied to your clipboard.
- **Keyboard Shortcut**: Press `Alt+Shift+C` on any Reddit thread to instantly trigger extraction.
  - **Input-Suppression Protection**: Built-in typing protection ensures the keyboard shortcut is automatically suppressed while typing in input fields, text areas, or editable comment containers (`<textarea>`, `<input>`, `contenteditable`), preventing accidental triggers while composing comments.

---

## Platform Support

### Modern Reddit (`shreddit`)
- **Full Support**: Seamless DOM extraction on modern Reddit interface (`shreddit`).
- **Hydrated Depth Tiers**: Extracts all loaded comment levels and nested reply trees.
- **OP Attribution**: Identifies the Original Poster and appends `(OP)` tags to all replies.
- **Media URLs**: Preserves image links, video sources, and Markdown hyperlinks.
- **Deleted Parent Preservation**: Retains `[deleted]` placeholders so active child reply trees maintain correct conversation structure.

### Platform Roadmap
- Modern Reddit (`shreddit`) — ✅ Fully Supported
- Hacker News (`news.ycombinator.com`) — 📋 Planned
- X (formerly Twitter) — 📋 Planned

---

## Development & Building from Source

### Prerequisites
- Node.js 22+ (verified through Node 24)
- `npm`

### Workflow Commands

```bash
# Clone the repository
git clone https://github.com/mkarimdev/ThreadToLLM.git
cd ThreadToLLM

# Install dependencies
npm install

# Start Vite development server with hot-reloading
npm run dev

# Compile production extension bundle to dist/
npm run build

# Run the complete test and verification suite (lint, typecheck, Vitest, build)
npm run check

# Package production distribution archive (thread-to-llm-v*.zip)
npm run package

# Unified release automation (SemVer bump, changelog update, package, commit, tag, and publish)
npm run release -- [patch|minor|major] [--dry-run] [--publish]
```

---

## Contributing & Community

Contributions are welcome! Please check our community documents before opening an issue or pull request:

- [Contributing Guide](CONTRIBUTING.md): Setup instructions, trunk-based git workflow, Conventional Commits standard, and platform adapter implementation guide.
- [Changelog](CHANGELOG.md): Complete release history, version notes, and categorized changes.
- [Coding Standards](CODING_STANDARDS.md): Architectural boundaries, layer decoupling rules, and testing standards.
- [Domain Glossary](GLOSSARY.md): Canonical terminology for Thread Documents, Comment Trees, Filter Pipelines, and Platform Adapters.

---

## License

Distributed under the [MIT License](LICENSE). Copyright © 2026 mkarimdev (Karim).
