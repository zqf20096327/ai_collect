# Coderbook

English | [简体中文](README.zh-CN.md)

**An engineering handbook for coding agents.**

Coderbook brings together working conventions for feature discussions, implementation, commits, pull requests, code review, testing, and acceptance. It helps programmers give their coding agents a shared way to approach and deliver engineering work.

The existing conventions cover simple designs that address root causes, atomic commits, reviews by two different agents after each commit, E2E verification, and acceptance against the delivered revision. Read the complete [Coderbook skill](skills/coderbook/SKILL.md) for the actual rules.

## Who it is for

- Programmers using coding agents for feature development, bug fixes, refactoring, and code review.
- Teams that want shared conventions for agent-assisted commits, reviews, and delivery.

This repository has English and Chinese READMEs. The original skill instructions remain unchanged and are primarily in Chinese, including the convention of a one-sentence Chinese commit body. The English README is an introduction and installation guide, not a separate English ruleset.

## Install in Codex

Coderbook uses three companion skills:

| Skill | Purpose | Source |
| --- | --- | --- |
| `karpathy-guidelines` | Coding behavior guidelines | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills), path `skills/karpathy-guidelines` |
| `ponytail` | Simple implementations and avoiding overengineering | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail), path `skills/ponytail` |
| `coding-architecture-diagrams` | Code and architecture diagrams | Included here at [skills/coding-architecture-diagrams](skills/coding-architecture-diagrams/SKILL.md) |

### Ask the skill installer

Copy this prompt into Codex:

```text
Use $skill-installer to install these skills, skipping any that are already installed:

1. Repository: https://github.com/DolphinMiner/coderbook
   Paths: skills/coderbook and skills/coding-architecture-diagrams
2. Repository: https://github.com/multica-ai/andrej-karpathy-skills
   Path: skills/karpathy-guidelines
3. Repository: https://github.com/DietrichGebert/ponytail
   Path: skills/ponytail
```

Codex detects new skills automatically. If they do not appear, restart Codex. See the [official skill installation documentation](https://developers.openai.com/codex/skills#install-curated-skills-for-local-use).

### Optional manual installation

Clone this repository:

```sh
git clone https://github.com/DolphinMiner/coderbook.git
```

Copy the `skills/coderbook` and `skills/coding-architecture-diagrams` folders into `~/.agents/skills/`, keeping each folder intact. Skip a destination if that skill is already installed; do not overwrite it. This is Codex's documented [user-level skill location](https://developers.openai.com/codex/skills#where-to-save-skills).

Install `karpathy-guidelines` and `ponytail` from the upstream repositories and paths in the table above, either with `$skill-installer` or by copying their skill folders into the same directory. These two companion skills are not bundled in this repository.

## Use

Mention `$coderbook` in your task:

```text
Use $coderbook to implement file uploads in this project.
```

```text
Use $coderbook to review the changes on the current branch.
```

Coderbook works with `karpathy-guidelines` and `ponytail` for coding, and `coding-architecture-diagrams` for diagrams. Its [SKILL.md](skills/coderbook/SKILL.md) is the source of the working conventions.

## Repository layout

```text
README.md
README.zh-CN.md
LICENSE
skills/
├── coderbook/
│   ├── SKILL.md
│   └── agents/openai.yaml
└── coding-architecture-diagrams/
    └── SKILL.md
```

## Acknowledgments

Coderbook uses [Karpathy Guidelines](https://github.com/multica-ai/andrej-karpathy-skills) and [Ponytail](https://github.com/DietrichGebert/ponytail) as companion skills. They are maintained in their own repositories and installed separately.

## License

[MIT](LICENSE). Companion skills installed from other repositories remain under their respective licenses.
