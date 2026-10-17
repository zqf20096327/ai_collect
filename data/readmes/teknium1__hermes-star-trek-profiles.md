# Star Trek Profiles for Hermes Agent

![Star Trek Profiles for Hermes Agent: 68 installable profiles across TOS, TNG, Deep Space Nine, and Voyager](./assets/collection-infographic.png)

A collection of comprehensive, installable Hermes Agent personas inspired by characters from:

- Star Trek: The Original Series
- Star Trek: The Next Generation
- Star Trek: Deep Space Nine
- Star Trek: Voyager

Each character is a separate Hermes [profile distribution](https://hermes-agent.nousresearch.com/docs/user-guide/profile-distributions). The profile changes how Hermes reasons, communicates, disagrees, handles pressure, and collaborates. It does not turn Hermes into a shallow quote generator or remove its normal tools and factual standards.

## What each profile contains

- A substantial `SOUL.md` covering identity, voice, worldview, operating method, strengths, blind spots, pressure behavior, disagreement style, safeguards, and task affinities
- A character-branded terminal skin
- A provider-neutral `config.yaml`
- A standard `distribution.yaml`

No profile ships credentials, memories, sessions, conversation history, a model choice, cron jobs, or MCP servers. Your provider setup remains yours.

## Browse the collection

```bash
python3 manage.py list
python3 manage.py list --series DS9
```

The generated catalog lives in [`catalog.json`](./catalog.json), and every installable distribution is under [`profiles/`](./profiles/). The human-readable [roster](./ROSTER.md) shows the full collection and the work each persona suits.

## Install

Clone once, then install any combination:

```bash
git clone https://github.com/teknium1/hermes-star-trek-profiles.git
cd hermes-star-trek-profiles

# One profile
python3 manage.py install jean-luc-picard --alias

# A whole series
python3 manage.py install --series DS9 --alias

# The complete collection
python3 manage.py install --all --alias
```

One-line bootstrap on Linux/macOS:

```bash
curl -fsSL https://raw.githubusercontent.com/teknium1/hermes-star-trek-profiles/main/install.sh | sh -s -- jean-luc-picard --alias
```

The one-liner follows mutable `main`; inspect it before use. For a reproducible install, clone a tagged release or commit SHA, review the checkout, then run `python3 manage.py install ...`. The manager prints a SHA-256 of every selected profile payload before installation.

PowerShell:

```powershell
$script = irm https://raw.githubusercontent.com/teknium1/hermes-star-trek-profiles/main/install.ps1
& ([scriptblock]::Create($script)) jean-luc-picard --alias
```

Start the installed profile with either form:

```bash
jean-luc-picard chat
# or
hermes -p jean-luc-picard chat
```

Profile identity is loaded when a session starts. Start a new session after installing or updating.

## Why the collection has an installer

Hermes accepts a local directory containing `distribution.yaml`, while a remote Git install expects that manifest at the repository root. This repository contains many distributions, so `manage.py` selects the requested character directories and hands each one to Hermes' native installer. It adds no alternate profile format and writes no profile state itself.

## Update

```bash
cd hermes-star-trek-profiles

# Review and fast-forward the collection, then update selected profiles
git pull --ff-only
python3 manage.py update jean-luc-picard seven-of-nine

# Update every installed profile from this collection
python3 manage.py update --all
```

Hermes' distribution updater replaces `SOUL.md` and the skin while preserving local memories, sessions, credentials, and `config.yaml`. Pass `--force-config` if you also want to restore the distribution's skin selection. `manage.py update --pull ...` is a convenience for explicitly opting into the fast-forward before updating.

Keep the collection checkout if you want native `hermes profile update` to keep working: current Hermes records a local absolute source path for monorepo-selected distributions. Moving the checkout requires reinstalling the affected profiles from the new location. `manage.py install --force` also replaces `config.yaml`; it preserves memories and sessions, not local config overrides.

Current Hermes 0.18.x has broader distribution-update limitations: explicit `distribution_owned` paths are not yet enforced as an allow-list, files removed upstream are not deleted locally, and updates are not atomic. This collection ships only reviewed static profile content, but inspect updates before applying them.

## Design principles

1. **Behavior over cosplay.** A persona should change how the agent approaches work, not sprinkle dialogue references over generic answers.
2. **Useful asymmetry.** Picard, Sisko, Janeway, Spock, Data, Kira, Garak, Seven, and Quark should solve the same problem differently.
3. **Character limits survive.** Blind spots are modeled, then bounded so they add texture without making the agent worse or unsafe.
4. **User agency stays intact.** Rank, authority, intimacy, loyalty, and fictional history are never imposed on the user.
5. **Original wording only.** The profiles use no scripts, copied dialogue, character art, logos, episode text, or catchphrases.
6. **Provider neutral.** The collection does not assume a particular model or API key.

## Development

Persona source data is in `source/*.json`. Generated distributions are deterministic.

```bash
python3 tools/build_collection.py
python3 tools/build_collection.py --check
python3 tools/validate_collection.py
python3 tools/e2e_collection.py       # requires an installed `hermes`
```

When adding a character, stop if there is not enough stable behavioral signal to justify a distinct agent. Depth beats roster inflation.

## Rights and attribution

This is an unofficial, non-commercial fan-made collection for Hermes Agent. Star Trek, its series names, and its characters are trademarks or copyrighted properties of their respective rights holders. This repository is not affiliated with or endorsed by Paramount, CBS, or the Star Trek rights holders.

The repository contains behavioral descriptions written in original language. It includes no franchise logos, promotional art, actor likenesses, scripts, episode transcripts, audio, video, or copied dialogue.

Code and original profile text are released under the MIT License, subject to all third-party rights in the underlying fictional characters and setting.
