<p align="center">
  <img src="desktop/assets/icon.svg" width="88" height="88" alt="OpenVorld icon" />
</p>

<h1 align="center">OpenVorld</h1>

<p align="center">
  <strong>Every project is a vorld.</strong><br />
  An open-source harness for your AI agents, shown as a living RPG world: your projects, your crew, and the work you do together.
</p>

<p align="center">
  <a href="#start">Get started</a> ·
  <a href="https://github.com/DigitalDreams-Lab/OpenVorld/releases">Desktop releases</a> ·
  <a href="docs/DESKTOP.md">Desktop guide</a> ·
  <a href="CONTRIBUTING.md">Contribute</a>
</p>

<p align="center">
  <a href="https://openvorld.com/play/"><img src="docs/images/demo.gif" width="720" alt="The OpenVorld web demo: Mira, Sage and Jules plan a surprise party for Buzz at the Party Hall, browse the web, ask before they save a file, and celebrate." /></a>
</p>

<p align="center"><sub>The web demo, <em>Surprise for Buzz</em>, at 2x speed. <a href="https://openvorld.com/play/">Play it in your browser</a>, no download needed.</sub></p>

## Make the work visible

OpenVorld gives a project a place and its agents a presence. Your crew has names, roles, houses, and workbenches. They join you when there is work to do, show their activity above their heads, and stay nearby until dismissed. You are the founder: set the direction, form the parties, and approve the access they need.

Use a vorld for a software project, a company, a content studio, or an activity you want help running. The files remain real files. The world helps you see who is doing what.

- **Assemble a crew.** Give each member a role, a personality, and a brain. Talk to them individually or bring them into a party.
- **Work together in parties.** Give a group a goal. Members share a conversation, hand work to teammates with `@mentions`, and gather around you.
- **Follow the work.** Read task balloons, inspect tool activity, and watch a member's browser preview when they use the web.
- **Keep the decisions.** A writ is an approval for access: a folder, a command, or a site. Members ask when they need more.
- **Earn progress.** Finished work earns XP, levels, and deeds. Your profile adds your name and background while your founder character stays unique.

## Watch the one minute tour

<p align="center">
  <a href="https://openvorld.com/media/openvorld-promo.mp4"><img src="docs/images/promo-video.jpg" width="720" alt="Watch the one minute OpenVorld tour, with sound" /></a>
</p>

## One room. Several minds.

A party keeps the conversation and its handoffs in one place. Every reply belongs to a named member, and requests for access appear alongside the work.

![The Launch crew sharing a release-planning conversation, with the village visible behind the party chat.](docs/images/party.png)

## See what your crew makes

Open HTML reports, images, Markdown, tables, and other supported files directly from a message. HTML previews are isolated from the app; PDFs, audio, and video use the browser's supported renderers.

![An HTML launch brief opened directly from the party conversation in OpenVorld.](docs/images/preview.png)

## Bring your own brain. Keep your own files.

Use installed agent tools such as **Claude Code** or **Codex**, or connect an **OpenAI-compatible API** such as OpenRouter, OpenAI, Ollama, or LM Studio. Using another agent? Press **Copy integration prompt** and paste it into your agent: it adds itself. Each crew member can use a different provider. A member with no brain uses a short scripted reply, so you can explore before connecting a model.

Your vorld has one shared project folder and private workbenches for each member. Each member also has a private house and vault for credentials and saved sign-ins, and a memory that carries what matters from one chat to the next. Browser work uses a separate member profile and requires Chrome or Edge.

Worlds and history live locally as YAML, JSON, and JSONL. There is no OpenVorld account or hosted backend. Connected model providers and websites receive the requests you choose to send them.

## Start

Requires **Node.js 20+** and npm. The desktop shell supports **macOS, Windows, and Linux**; installer details are in the [desktop guide](docs/DESKTOP.md).

```bash
git clone https://github.com/DigitalDreams-Lab/OpenVorld.git
cd OpenVorld
npm install
npm run desktop
```

Prefer the browser? Run `npm run dev` and open the local address it prints.

On macOS, build and install your own desktop copy with `npm run desktop:install`. For packaged builds, see the [releases page](https://github.com/DigitalDreams-Lab/OpenVorld/releases).

![The OpenVorld startup screen, with its gold V icon and the Launch Studio demo world.](docs/images/startup.png)

### Your first vorld

1. Create a vorld and choose a project folder. Start with a Software, Content, Business, or Blank template.
2. Give your crew their brains in each member's settings.
3. Form a party at the Party Hall, give it a goal, and start a shared task.
4. Review access requests as they arrive and open the files your crew produces.

Data lives in `~/.openvorld` by default, outside the app and repository. To choose another folder:

```bash
OPENVORLD_HOME=~/my-vorlds npm run dev
```

## Make it yours

Packs define templates, roles, themes, deeds, and provider settings. Add them in `~/.openvorld/packs`, or in a single vorld's `packs` folder. See the [pack guide](docs/PACKS.md).

| Guide | What you will find |
| --- | --- |
| [Desktop](docs/DESKTOP.md) | Build, install, and run the app |
| [Packs](docs/PACKS.md) | Customize a world without changing the engine |
| [Architecture](docs/ARCHITECTURE.md) | How the engine, game, and agents fit together |
| [Upgrading](docs/UPGRADING.md) | Data formats, backups, and safe updates |
| [Changelog](CHANGELOG.md) | What changed between versions |

## Build with us

OpenVorld is under active development. Contributions that make agent work easier to understand and manage are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before starting.

```bash
npm test
npm run typecheck
npm run validate
```

To regenerate the product screenshots with disposable demo data, run `npm run screenshots`. The [screenshot guide](docs/SCREENSHOTS.md) describes what is captured.

---

[MIT licensed](LICENSE) · Built by DigitalDreams Lab and contributors.
