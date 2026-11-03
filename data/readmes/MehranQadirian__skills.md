# Skills

A collection of ready-to-use [Claude](https://claude.ai) skills, grouped by category. Drop one in and Claude gets a new ability.

## Categories

| Category | Skills |
|---|---|
| [**Documents**](documents/) | [PDF Atelier](documents/pdf-atelier/): beautiful themed PDFs with RTL support<br>[pdf-processing](documents/pdf-processing/): extract, OCR and verify existing PDFs<br>[document-conversion](documents/document-conversion/): Markdown, Word, HTML, PDF and EPUB with RTL |
| [**Git**](git/) | [Commitsmith](git/commitsmith/): scoped one-line commit messages<br>[systematic-debugging](git/systematic-debugging/): evidence-based bug hunting with bisect<br>[git-recovery](git/git-recovery/): recover lost commits and undo mistakes safely<br>[pr-writer](git/pr-writer/): pull request descriptions from the real diff |
| [**Agent Engineering**](agent-engineering/) | [multi-agent-orchestration](agent-engineering/multi-agent-orchestration/): roles, contracts and evaluation for multi-agent systems<br>[skill-authoring](agent-engineering/skill-authoring/): create, lint and improve skills<br>[prompt-regression-testing](agent-engineering/prompt-regression-testing/): frozen cases and baseline checks for prompts |
| [**Software Engineering**](software-engineering/) | [code-review](software-engineering/code-review/): risk-ordered review with a scope script |
| [**Security**](security/) | [secrets-hygiene](security/secrets-hygiene/): find leaked credentials and respond to leaks |
| [**Data**](data/) | [csv-profiling](data/csv-profiling/): profile and safely clean CSV files, including Persian digits |
| [**Termux**](termux/) | [termux-setup](termux/termux-setup/): set up Termux, fix storage and git problems on a phone |

## Quick start

1. Open a category and pick a skill.
2. **Claude.ai:** zip the skill folder and upload it in Settings > Capabilities > Skills.
3. **Claude Code:** copy the skill folder into `~/.claude/skills/`.

## Layout

```
skills/
├── scripts/validate_skills.py
└── <category>/
    ├── README.md
    └── <skill>/
        ├── SKILL.md          instructions for Claude
        ├── README.md         instructions for humans
        ├── scripts/          optional, tested helper scripts
        ├── references/       optional, details loaded only when needed
        └── templates/        optional, files to copy and fill
```

Every skill has a `SKILL.md` and a `README.md`. Keep `SKILL.md` short and move detail into `references/`.

## Contributing

Add your skill under the right category, link it in that category's README, and open a pull request.

Before you commit, run the checker:

```bash
python3 scripts/validate_skills.py
```

It verifies the folder name matches the `name` in the frontmatter, each skill has a README, the category README links the skill, and relative links resolve.
