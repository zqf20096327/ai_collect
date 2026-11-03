<div align="center">

<img src="assets/cover.jpg" alt="Hermes Profiles: ready-made agents for Hermes" width="100%">

# Hermes Profiles

**Ready-made, battle-tested agents for [Hermes Agent](https://github.com/NousResearch/hermes-agent).**<br>
One folder, one profile. Install it with one command, update it without losing your memories.

**English** · [Português](README.pt-BR.md)

[![validate](https://img.shields.io/github/actions/workflow/status/luizgustavosaraiva/hermes-profiles/validate.yml?branch=main&style=flat-square&label=validate)](https://github.com/luizgustavosaraiva/hermes-profiles/actions/workflows/validate.yml)
[![license](https://img.shields.io/github/license/luizgustavosaraiva/hermes-profiles?style=flat-square&color=7c3aed)](LICENSE)
[![hermes](https://img.shields.io/badge/hermes-%E2%89%A50.21.0-0ea5e9?style=flat-square)](https://hermes-agent.nousresearch.com/docs/)
[![profiles](https://img.shields.io/badge/profiles-1-10b981?style=flat-square)](#profiles)
[![stars](https://img.shields.io/github/stars/luizgustavosaraiva/hermes-profiles?style=flat-square&color=f59e0b)](https://github.com/luizgustavosaraiva/hermes-profiles/stargazers)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-ec4899?style=flat-square)](CONTRIBUTING.md)

</div>

---

## Why

A good Hermes agent is more than a prompt. It is a `SOUL.md`, a config, a set of
skills, the right toolsets and a handful of hard-won rules about how Hermes
actually behaves. This repo packages agents that are used daily as
[profile distributions](https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions),
so you get the whole agent, not a copy-paste recipe.

- 🧩 **Complete agents.** SOUL, config, skills and templates, versioned together.
- 🔒 **Your data stays yours.** Memories, sessions, `.env` and `local/` are never shipped or overwritten.
- 🔄 **Updatable.** Re-run the installer or `hermes profile update <name>`.
- 🌎 **Bilingual docs.** Every profile is documented in English and Portuguese, and the agents reply in your language.
- ✅ **Checked in CI.** Every profile is validated for manifest, structure and leaked secrets.

## Profiles

| Profile | What it does | Needs | Docs |
|---|---|---|---|
| 🧑‍💼 **[recruiter](profiles/recruiter)** | HR for your bots. Reads a repo, proposes a team (orchestrator + specialists), hires each profile with the right model and effort, and creates the team's Kanban board. | Kanban, gateway | [EN](profiles/recruiter/README.md) · [PT](profiles/recruiter/README.pt-BR.md) |

> More are coming. Have one that earns its keep? See [Contributing](#contributing).

## Install

You need [Hermes Agent](https://hermes-agent.nousresearch.com/docs/) ≥ 0.21.0 and `git`.

**One line**

```bash
curl -fsSL https://raw.githubusercontent.com/luizgustavosaraiva/hermes-profiles/main/scripts/install.sh | bash -s <profile>
```

The script keeps a clone in `~/.local/share/hermes-profiles`, runs
`hermes profile install` with `--alias` and, if the profile already exists,
updates it instead. Extra flags go straight to Hermes, e.g. `--name my-name`.

**Manual**

```bash
git clone https://github.com/luizgustavosaraiva/hermes-profiles ~/.local/share/hermes-profiles
hermes profile install ~/.local/share/hermes-profiles/profiles/<profile> --alias
```

> [!IMPORTANT]
> `hermes profile install github.com/...` only works when `distribution.yaml` is at
> the repository root. This is a collection, so install from the cloned folder
> as shown above.

**Then read the profile's README.** Each one lists the Hermes settings it needs
(credentials, gateway, Kanban options…). Skipping that table is the #1 reason
an agent "does nothing".

### Update

```bash
# re-run the installer…
curl -fsSL https://raw.githubusercontent.com/luizgustavosaraiva/hermes-profiles/main/scripts/install.sh | bash -s <profile>
# …or by hand
git -C ~/.local/share/hermes-profiles pull && hermes profile update <profile>
```

| On update | What happens |
|---|---|
| `SOUL.md`, `skills/`, `distribution.yaml` | Replaced by the new version |
| `config.yaml` | **Kept**: your model and tweaks win (`--force-config` resets it) |
| `.env`, `memories/`, `sessions/`, `local/`, logs | Never touched |

### Remove

```bash
hermes profile delete <profile>
```

## How a profile is laid out

```text
profiles/<name>/
├── distribution.yaml   # manifest: name, version, Hermes requirement, env vars
├── SOUL.md             # personality and hard rules
├── config.yaml         # model, effort, toolsets (yours after install)
├── skills/             # bundled skills
├── README.md           # what it does + required Hermes setup (EN)
└── README.pt-BR.md     # same, in Portuguese
```

## Safety

Profiles are plain text: read the `SOUL.md` and skills before you chat with
one. Hermes installs any shipped cron jobs **paused**, and the installer strips
credentials and user data even if they slipped into a repo. Profiles here never
ask you to paste keys into a chat.

## Contributing

New profiles, fixes and translations are welcome. Read
[CONTRIBUTING.md](CONTRIBUTING.md). In short: one folder per profile, a
`distribution.yaml`, READMEs in both languages with a **Required Hermes setup**
table, and `python scripts/validate.py` passing.

## Credits

Built on [Hermes Agent](https://github.com/NousResearch/hermes-agent) by
[Nous Research](https://nousresearch.com). Not affiliated with Nous Research.
Profiles by [Gustavo Saraiva](https://github.com/luizgustavosaraiva) and
contributors. [MIT](LICENSE).
