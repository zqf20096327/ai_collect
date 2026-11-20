<h1 align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/openwizdev/.github/main/profile/art/lockup-dark.png">
    <img alt="OpenWiz" src="https://raw.githubusercontent.com/openwizdev/.github/main/profile/art/lockup-light.png" width="320">
  </picture>
</h1>

**OpenWiz is the open kernel for agent factories. Bring your own everything. Owned by no one.** This repo is the kernel itself; the [other repos](https://github.com/openwizdev) add skills, loops and the app on top.

You make the decisions: answer a few questions. The agents run the factory: they write the spec and the tickets, build, review and merge. You watch it ship.

**Status:** before 0.1.0. 0.1.0 is coming soon. OpenWiz builds itself, in public, in this repo.

## Quick start

**0.1.0: coming soon.** It will start your factory on your computer or a VPS, on Cloudroom, or on boat.dev.

To try today's pre-release (0.0.12, Cloudroom only), paste this line into your coding agent:

> Install OpenWiz from github.com/openwizdev/OpenWiz

Your agent follows the [install skill](https://github.com/openwizdev/WizSkills/blob/v0.1.2/skills/install/SKILL.md). Nothing starts until you approve a plan. People: see the [install guide](docs/install.md). OpenWiz is free. Your model and host charges are your own.

## How it works

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/openwizdev/.github/main/profile/art/map-dark.png">
  <img alt="How the repos fit: WizSkills and WizLoops feed OpenWiz, the kernel. OpenWiz drives your agents and machines and writes records to GitHub. WizSite's app reads GitHub." src="https://raw.githubusercontent.com/openwizdev/.github/main/profile/art/map-light.png" width="560">
</picture>

The kernel is small. Three parts:

- **Records on GitHub.** Specs, tickets and one status note per agent live in your repo's issues. Anything that follows [the rules](kernel/records.v1.md) can read and write your factory. The [records kit](kernel/records-kit/README.md) checks them.
- **Drivers.** A driver is a tiny program, in any language, that answers four commands: `version`, `start`, `wake`, `stop` ([driver v1](kernel/driver.v1.md)). Copy [the template](adapters/template/README.md) to plug in your own host. Drivers for your computer or a VPS, Cloudroom and boat.dev are coming in 0.1.0.
- **A test kit.** The [driver kit](kernel/driver-kit/README.md) checks a driver on its real host. A driver that passes can merge.

OpenWiz never touches a login. Your agents use their own signed-in tools, and there is no server of ours.

| Path | What it is |
| --- | --- |
| `kernel/` | The records and driver rules, and their test kits |
| `adapters/` | The drivers, one folder per host |
| `crates/` | The `openwiz` command (Rust) |
| `docs/` | Guides and public decisions |

## Versions

What each version adds is in the [changelog](CHANGELOG.md). A version has at most five outcomes, each one something a user can see or check, and claims nothing its evidence doesn't show; tests alone never prove live behaviour.

## Links

- [openwiz.dev](https://openwiz.dev) · [the app](https://openwiz.dev/app/) · [Changelog](CHANGELOG.md)
- Agents start at [AGENTS.md](AGENTS.md). For anything beyond a small fix, open an issue first. Everything here is public: use synthetic examples only, never personal data, secrets or private links. A new dependency needs the maintainer's approval.
- [Apache License 2.0](LICENSE). A contribution is licensed under the same terms; there is no separate contributor agreement.
