# Hermes research & Karpathy guidelines skill

**Repository:** [github.com/interfluve-wav/andrej-karpathy-skills-hermes](https://github.com/interfluve-wav/andrej-karpathy-skills-hermes)

This repository contains a **Hermes**-formatted skill adapted from [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) (MIT): behavioral guidelines derived from [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) on common LLM coding pitfalls.

## Repository layout

```text
andrej-karpathy-skills-hermes/
├── Karpathy-Hermes-Skill/          ← ship this directory (rename on install; see below)
│   ├── SKILL.md
│   └── references/
│       └── EXAMPLES.md
├── Karpathy Guidelines - Hermes Adaptation.md
├── README.md
└── LICENSE
```

## Karpathy guidelines (Hermes)

| | |
|--|--|
| **Skill package** | [`Karpathy-Hermes-Skill/`](Karpathy-Hermes-Skill/) |
| **Skill id** | `karpathy-guidelines` (in `SKILL.md` frontmatter) |

### Install (Hermes)

From a clone of this repo:

```bash
git clone https://github.com/interfluve-wav/andrej-karpathy-skills-hermes.git
cd andrej-karpathy-skills-hermes
mkdir -p ~/.hermes/skills/software-development
cp -R Karpathy-Hermes-Skill ~/.hermes/skills/software-development/karpathy-guidelines
```

If you already have the repo locally, only the `mkdir` / `cp` lines are needed:

```bash
mkdir -p ~/.hermes/skills/software-development
cp -R Karpathy-Hermes-Skill ~/.hermes/skills/software-development/karpathy-guidelines
```

Result on disk:

```text
~/.hermes/skills/software-development/karpathy-guidelines/
├── SKILL.md
└── references/
    └── EXAMPLES.md
```

Adjust `~/.hermes/skills/...` if your Hermes install uses a different base path.

### Skill files

| Path | Purpose |
|------|---------|
| `Karpathy-Hermes-Skill/SKILL.md` | Main skill (YAML frontmatter + four principles) |
| `Karpathy-Hermes-Skill/references/EXAMPLES.md` | Long-form before/after examples |

### Upstream

- **Source project:** [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) (MIT; same ideas, different agent packaging)
- **This repo:** Hermes `SKILL.md` layout, metadata, wikilinks to related skills, and install notes above.

## License

MIT — see [`LICENSE`](LICENSE). The adaptation retains compatibility with the upstream MIT license.
