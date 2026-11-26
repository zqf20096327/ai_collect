<h1 align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/openwizdev/.github/main/profile/art/lockup-dark.png">
    <img alt="OpenWiz" src="https://raw.githubusercontent.com/openwizdev/.github/main/profile/art/lockup-light.png" width="320">
  </picture>
</h1>

**OpenWiz is the open kernel for agent factories. Bring your own everything. Owned by no one.** This repo is the kernel itself; the [other repos](https://github.com/openwizdev) add skills, loops and the app on top.

You make the decisions: answer a few questions. The agents run the factory: they write the spec and the tickets, build, review and merge. You watch it ship.

**Status:** OpenWiz 0.1.0 ("OpenWiz 0.01") is the current release: the [release](https://github.com/openwizdev/OpenWiz/releases/tag/v0.1.0) installs on macOS (Apple silicon or Intel) and on Linux on x86_64 (glibc 2.34 or later), with no CloudRoom. CloudRoom offers no Intel Mac build today, so on an Intel Mac your agents run on this computer or on boat.dev. OpenWiz 0.1.1 ("OpenWiz 0.02") is coming next and is not released yet. OpenWiz builds itself, in public, in this repo.

## Quick start

You need Python 3.9 or later, `git`, and the GitHub CLI (`gh`). Then paste this line into your coding agent (Claude Code, Codex or another):

> Install OpenWiz from github.com/openwizdev/OpenWiz

Your agent follows 0.1.0's [install skill](https://github.com/openwizdev/WizSkills/blob/33eef93ba30cd8db256f6fe270e3ed28747a79bd/skills/install/SKILL.md) (WizSkills `maint/0.2`). First it asks where your agents run: **this computer**, with the Claude Code or Codex you're signed in to; **boat.dev**; or **[CloudRoom](https://cloudroom.dev)**. CloudRoom is optional: the install never needs it, and its install and sign-in run only if you pick it. In 0.1.0 the automatic fleet runs in CloudRoom; without CloudRoom you plan, start each builder by hand on this computer or on boat.dev, and review its pull request yourself.

It checks your computer, installs the verified prebuilt 0.1.0 release (no Rust or Node), puts OpenWiz's skills into your agents, and checks each connection. Nothing starts until you approve a plan. People: see the [install guide's 0.1.0 steps](docs/install.md#openwiz-010) for every step and command. OpenWiz is free. Your model and host charges are your own.

### OpenWiz 0.1.1

OpenWiz 0.1.1 ("OpenWiz 0.02") is coming; it has no release date yet. In 0.1.1 the automatic fleet also runs on this computer or on boat.dev: a scheduled job on this computer, shown first and installed on your yes, checks GitHub every ten minutes and starts or wakes the fleet only when work is due. The [install guide](docs/install.md) already describes its steps.

## How it works

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/openwizdev/.github/main/profile/art/map-dark.png">
  <img alt="How the repos fit: WizSkills and WizLoops feed OpenWiz, the kernel. OpenWiz drives your agents and machines and writes records to GitHub. WizSite's app reads GitHub." src="https://raw.githubusercontent.com/openwizdev/.github/main/profile/art/map-light.png" width="560">
</picture>

The kernel is small. Three parts:

- **Records on GitHub.** Specs, tickets and one status note per agent live in your repo's issues. Anything that follows [the rules](kernel/records.v1.md) can read and write your factory. The [records kit](kernel/records-kit/README.md) checks them.
- **Drivers.** A driver is a tiny program, in any language, that answers four commands: `version`, `start`, `wake`, `stop` ([driver v1](kernel/driver.v1.md)). Copy [the template](adapters/template/README.md) to plug in your own host. The release carries drivers for your computer or a VPS, CloudRoom and boat.dev.
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
