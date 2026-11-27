<p align="center">
  <img src="apps/firefox/configs/branding/ressac/logo256.png" width="96" alt="">
</p>

<h1 align="center">Ressac</h1>

<p align="center">
  <strong>A browser that grows with you.</strong><br>
  Calm and minimal out of the box. Switch on the AI when you need it for harder work.<br><br>
  <a href="README.fr.md">Lire en français</a>
</p>

<p align="center"><sub>Closed beta · macOS 13.3+ · Apple Silicon · Open source</sub><br><a href="https://getressac.app/#invite"><b>Join the beta</b></a></p>

<p align="center"><img src="docs/images/overview-en.jpg" alt="Ressac: a calm page, the sidebar with its tabs and spaces"></p>

Ressac has three levels, each one switched on by you: **Browser** (no AI), **AI** (the agent and its protections), and the **Lab** (experimental power tools). They are real boundaries: what is off does not run.

## Level 1, day one: just a calm browser

Firefox under the hood, a quiet sidebar, nothing to sign up for, nothing to switch on.

- A vertical sidebar with **essentials** that stay loaded, pinned tabs and folders.
- Import from Arc, Chrome, Brave, Edge, Vivaldi, Opera, Safari, Firefox and Zen, spaces and open tabs included.
- Firefox add-ons work.
- A bar for calls (Meet, Teams, Zoom…) and for audio or video playing in the background.

## Your way: spaces, auras, shortcuts

- **Spaces**, each with its own colour, its aura, and its own logins if you want.
- A command bar on <kbd>⌘T</kbd> / <kbd>⌘L</kbd> for addresses, bookmarks, history and tabs; <kbd>⌃Tab</kbd> through recent tabs.
- Remappable shortcuts and an optional Vim mode.
- Your saved passwords in Settings, behind Touch ID.

## Level 2, when you're ready: switch on the AI

*Ressac* is French for backwash: the wave that comes back to the shore. Send the agent out on the web, and it comes back with the answer.

**An agent that browses with you**
- Claude Code or Codex runs in a sandboxed container, with **your own account**, inside a small Linux machine that Ressac downloads once (about 275 MB) and stops after 5 minutes without use (adjustable in Settings › Workshop). At first use Ressac also downloads the pinned version of the agent you chose (about 170 MB), checked against its SHA-256. Docker is not needed.
- In this level the agent has no shell: it reads and writes files in its workspace, and browses through Ressac.
- The container sees only `~/Ressac/workspace`. Its network goes through an allowlist proxy: Claude, OpenAI, npm, PyPI and GitHub, plus the domains you add in Settings › Agent. On your Mac it reaches only Ressac's own ports; an Ollama you set up as the engine is reached through them, for inference only. The allowlist checks names, so a site sharing a CDN with an allowed domain may still be reached by name tricks over TLS. It gets 2.5 GB of memory (1 GB on an 8 GB Mac) and 1024 processes.
- Limits, plainly: this stops ordinary leaks, not a targeted and patient injection. In the Workshop (the Lab), an allowed domain can still serve as a channel (a gist with the attacker's token on `api.github.com`, `npm publish`), and Ressac's browsing tools (`open_tab`, `navigate`) open pages in the browser, outside this firewall.
- It browses in its own tab, which you can watch; a thumbnail shows what it is doing while you keep working.
- Before a purchase or a choice, it fills a **live recap**: criteria, independent sources, offers, sourced pros and cons.
- It asks before opening an address it wrote itself, and hands back control when a page needs you (a login, a captcha).
- You talk to it in a **chat**: several discussions per window, kept 30 days (masked text only). Your message is masked before it is sent, and « Mode avancé » (Settings › Agent) switches back to the agent's terminal.
- It builds widgets for your home page.
- It works with your identifiers without seeing them: masking, a passport for your name and address, and « Cacher pour l'agent » for anything you point at.

<p align="center"><img src="docs/images/live-recap-en.gif" alt="The agent compares the world's biggest tidal bores and fills a live recap"></p>

**Local search, and widgets**
- The **⌘T bar** finds a page you visited by what it was about, in French or English, with a small search model that runs on your Mac.
- A home page with widgets. They sort and summarise through your agent: your account, an API key or your Ollama (it counts against your limits).

## Level 3, the Lab (experimental)

Off by default; turn it on in Settings › Agent › Usage level, after reading what it exposes. Its protections have known limits, listed in [SECURITY.md](SECURITY.md).

- **Workshop**: the agent gets a shell, to build and run project apps.
- **Workflows** and **watches**, and **actions** you launch from <kbd>⌘T</kbd>, with code the agent writes.
- **Site apps**: a website in its own window, with its own logins, that remembers where you were; and the agent's own apps.
- **Design mode** (change a page's look on request), the external MCP server, and the agent's developer tools (`run_js`, console, network).

<table>
  <tr>
    <td width="50%"><img src="docs/images/agent-en.jpg" alt="The agent reads sources while its recap fills in"><br><sub>The agent reads sources while its recap fills in</sub></td>
    <td width="50%"><img src="docs/images/command-bar-en.jpg" alt="The ⌘T command bar"><br><sub>The ⌘T command bar</sub></td>
  </tr>
  <tr>
    <td width="50%"><img src="docs/images/workflow-builder.jpg" alt="A workflow, block by block"><br><sub>A workflow, block by block</sub></td>
    <td width="50%"><img src="docs/images/site-app.jpg" alt="A site app in its own window"><br><sub>A site app in its own window</sub></td>
  </tr>
  <tr>
    <td width="50%"><img src="docs/images/home-en.jpg" alt="Home, its widgets and the spaces at the foot of the sidebar"><br><sub>Home, its widgets and the spaces at the foot of the sidebar</sub></td>
    <td width="50%"><img src="docs/images/call-bar.jpg" alt="The call bar at the foot of the sidebar"><br><sub>The call bar at the foot of the sidebar</sub></td>
  </tr>
</table>

## Local and open

- **No account.** Ressac itself needs none. The agent uses your own Claude or ChatGPT account, an API key, or local models.
- **Your browsing stays on your Mac.** The agent only sees the pages it opens in its own tab and what you give it.
- **AI stays off until you switch it on.** The agent's machine, the local search model and the agent start only once you say yes.
- **Open source.** Built on Firefox, under the MPL 2.0.

During the beta, Ressac sends crash and error reports (without page addresses) and an anonymous install id to its developer, to fix bugs; turn it off in Settings › Privacy.

## Get Ressac

Ressac is in closed beta, with a small group of testers. They get a DMG signed and notarized by Apple, and Ressac then updates itself. **To join, ask for an invite on [getressac.app](https://getressac.app/#invite).**

- **To browse**: macOS 13.3 or later, Apple Silicon.
- **For the agent**: a Claude or ChatGPT account (or an API key, or, optionally, your own [Ollama](https://ollama.com) for local models). Nothing else to install: Ressac downloads the agent's machine at first use.
- **For local AI**: nothing to install. When you switch AI on, Ressac downloads its small search model once, EmbeddingGemma (334 MB), checked against its SHA-256. Widget sorting, summaries and action pages are written by your agent instead (your Claude Code or Codex account, an API key, or your Ollama), so one of them must be set up.

## Build from source

Ressac is built with [surfer](https://github.com/zen-browser/surfer), which downloads Firefox and applies Ressac's patches. You need macOS on Apple Silicon, Xcode command line tools, Python 3.10+, Rust, GNU tar, Node 22 and pnpm (through corepack), and about 25 GB of disk.

```sh
corepack pnpm install
corepack pnpm --filter firefox-ressac engine:install   # downloads Firefox, outside the repository
corepack pnpm --filter firefox-ressac engine:import    # applies the patches
corepack pnpm --filter firefox-ressac build            # full build, about 20 min
```

Start with [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for a map of the code. Everything else (UI-only builds, tests, packaging, each mechanism) is in [apps/firefox/README.md](apps/firefox/README.md). Visual rules are in [docs/DESIGN.md](docs/DESIGN.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Found a security issue? Report it privately, see [SECURITY.md](SECURITY.md).

## Credits

Ressac stands on the work of others:

- [Firefox](https://www.mozilla.org/firefox/) by Mozilla (MPL 2.0), the engine and most of the browser.
- [surfer](https://github.com/zen-browser/surfer) by the Zen Browser team (MPL 2.0), the build tool.
- [Node.js](https://nodejs.org) and [node-pty](https://github.com/microsoft/node-pty) (MIT), bundled for the agent's host.
- [EmbeddingGemma](https://ai.google.dev/gemma/docs/embeddinggemma) 300M by Google, the search model of the ⌘T bar; Ressac downloads it itself from Hugging Face ([ggml-org's Q8_0 GGUF](https://huggingface.co/ggml-org/embeddinggemma-300M-GGUF)), it is not bundled. Gemma is provided under and subject to the Gemma Terms of Use found at [ai.google.dev/gemma/terms](https://ai.google.dev/gemma/terms).
- [llama.cpp](https://github.com/ggml-org/llama.cpp) (MIT), its `llama-server` ships in the app and runs EmbeddingGemma.
- [Claude Code](https://claude.com/claude-code) by Anthropic and [Codex](https://github.com/openai/codex) by OpenAI, the agents, downloaded by Ressac at first use (pinned versions, SHA-256 checked) and used with your own account.
- [Svelte](https://svelte.dev), [Vite](https://vite.dev), and the fonts [Geist](https://vercel.com/font) and [Funnel Display](https://fonts.google.com/specimen/Funnel+Display) (OFL).

The full list of bundled third-party licenses ships inside the app, in `Contents/Resources/ressac-host/LICENSES`.

## License

[Mozilla Public License 2.0](LICENSE). The name Ressac and its logo are not covered by the license.
