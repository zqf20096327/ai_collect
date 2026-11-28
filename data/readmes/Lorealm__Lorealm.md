# Lorealm
[![Crowdin](https://badges.crowdin.net/lorealm/localized.svg)](https://crowdin.com/project/lorealm)

[![Discord](https://discord.com/api/guilds/1525884209829384295/widget.png?style=shield)](https://discord.gg/HGucxzNMhq)

Lorealm is a self-hosted frontend for LLM chat and roleplay where the logic travels with the content. A character, lorebook or whole world can carry its own scripts, state and tools, and whoever imports it gets a working system with nothing to install or configure.

<img width="1990" height="1271" alt="Screen Shot 2026-11-14 at 03 08 08(4)" src="https://github.com/user-attachments/assets/e3a628ba-3d88-47e2-822b-6e091e1c01bd" />

Lorealm is built with security and extensibility in mind. It was built with a philosophy that users should be able to express their creativity freely without being limited by what the tool can do.

The result is a very powerful tool that lets you do just that, create anything your heart desires.

You can read more about our vision [here](https://docs.lorealm.app/)

## Features
- **The Weaver Language**: A small programming language designed to let you express yourself. It's what allows us to shoot the creative ceiling into the stratosphere, while keeping the floor right down under your feet.
- **Reimagined Lorebooks**: With the power of Weaver, we have created a new vision for what Lorebooks can be. Instead of being simple keyword-based retrieval, they support evolving state and and a variety of other features. This means that a Lorebook can evolve over the course of a conversation.
- **Realms**: The system that holds everything together. A Realm is essentially a stage, where every actor only sees what it's given. This allows us to express simple 1-on-1 conversations, group chats or even full game systems, within one single system. We highly encourage you to [read more](https://docs.lorealm.app/realms/what_are_realms/) so you can appreciate what this system offers.
- **Security & Privacy**: Lorealm offers a level of security and privacy that few alternatives can match. Your passwords and API keys are protected with modern, best-practice cryptography, and Lorealm is only reachable from your own machine unless you choose otherwise.
- **Extensibility**: A working, documented plugin system from day one. Plugins let you extend Lorealm to your heart's content without giving up security: every plugin runs inside a sandbox and has to ask for each permission it uses.
- **Performance**: Highly performant Can easily support thousands of users and tens of thousands of parallel conversations. See [benchmarks](./docs/benchmarks.md) for real numbers.

### Translation

> **AI disclosure:** The initial translations (9 languages) were generated with Claude Opus/Sonnet 5.5 to provide a decent baseline.

Translations are managed through [Crowdin](https://crowdin.com/), whose generous open-source license lets open-source projects use the service at no cost. Translations sync every 24 hours and are merged regularly, so it may take a while for changes to reach the release branch.

Found something in the official Lorealm frontend that isn't translated, or a translation that reads wrong? Human review goes way further than any LLM, so we'd appreciate your help at **https://translate.lorealm.app/**.

## Installing
Lorealm runs on Windows, Linux and macOS, or anywhere Docker does. Mobile/Termux is untested.

### Download and run
1. Download the server for your system from the [latest release](https://github.com/Lorealm/Lorealm/releases/latest).
2. Run it and follow the setup questions in the terminal.
3. Open http://127.0.0.1:1551 in your browser and log in.

### Docker
1. Download [`docker-compose.yaml`](docker-compose.yaml) and change the admin password in it.
2. Start it:
   ```sh
   docker compose up -d
   ```
3. Open http://127.0.0.1:1551 in your browser and log in.

The [installation guide](https://docs.lorealm.app/getting-started/installing/) covers both in more detail, along with building from source.

## Contributing
If you want to contribute, we're happy to have you!

- **Found a bug or have an idea?** Open an [issue](https://github.com/Lorealm/Lorealm/issues).
- **Have a question?** Ask on [Discord](https://discord.gg/HGucxzNMhq).
- **Want to write code?** For anything larger than a small fix, open an issue first so we can agree on the approach. The installation guide explains how to [build from source](https://docs.lorealm.app/getting-started/installing/#building-from-source).
- **Want to improve the docs?** They live in [lorealm-docs](https://github.com/Lorealm/lorealm-docs).

Before opening a pull request, run the checks:
```sh
cd backend && cargo ci
cd frontend && make check lint
```

Refer to the [Contribution Guidelines](./CONTRIBUTING.md) for specifics regarding our AI Policy, Style Guidelines, and more.

## License
MIT
