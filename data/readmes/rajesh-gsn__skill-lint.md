# SkillLint

**Paste your SKILL.md. Get instant feedback.**

[skill-lint.com](https://skill-lint.com) — a free, browser-based validator for Claude SKILL.md files. No sign-up, no server, no data sent anywhere.

---

## What is a SKILL.md?

A `SKILL.md` is a structured Markdown file that tells Claude how to behave for a specific task — when to trigger, what steps to follow, and what output to produce. Poorly written skill files lead to Claude ignoring the skill, misunderstanding the intent, or producing inconsistent results.

SkillLint catches those problems before you ship.

---

## Features

- **20 validation rules** across errors, warnings, and info — from missing frontmatter to vague trigger descriptions
- **AI token estimator** — see how many tokens your skill consumes and whether it fits within context limits
- **Quality score** — an A–F grade based on weighted rule violations, so you can track improvement at a glance
- **Syntax highlighting** — SKILL.md-aware colouring in the editor (frontmatter keys, headings, code blocks, bold/italic)
- **Line-jump** — click any issue to jump straight to the offending line
- **Drag & drop** — drop a `.md` file directly onto the editor
- **Dark mode** — respects system preference, or toggle manually
- **Zero dependencies** — plain HTML, CSS, and ES2020 JavaScript; no build step, no npm

---

## Validation rules

| # | ID | Severity | What it checks |
|---|-----|----------|----------------|
| 1 | `no-frontmatter` | 🔴 error | File has no YAML frontmatter block |
| 2 | `frontmatter-unclosed` | 🔴 error | Opening `---` has no closing `---` |
| 3 | `missing-name` | 🔴 error | `name:` field is absent |
| 4 | `missing-description` | 🔴 error | `description:` field is absent |
| 5 | `empty-body` | 🔴 error | Body after frontmatter is blank |
| 6 | `body-too-short` | 🔴 error | Body is fewer than 20 words |
| 7 | `unclosed-code-block` | 🔴 error | A fenced code block is never closed |
| 8 | `name-format` | 🟡 warning | Name contains uppercase or spaces (use kebab-case) |
| 9 | `description-too-short` | 🟡 warning | Description is under 10 words |
| 10 | `no-trigger-context` | 🟡 warning | Description lacks trigger words ("when", "use", "invoke", etc.) |
| 11 | `no-headings` | 🟡 warning | Body has no `##` headings to guide Claude |
| 12 | `no-examples` | 🟡 warning | No example block or "## Examples" section |
| 13 | `placeholder-text` | 🟡 warning | Contains TODO / placeholder text |
| 14 | `unknown-fields` | 🟡 warning | Frontmatter has unrecognised fields |
| 15 | `body-too-long` | 🟡 warning | Body exceeds 800 words (risks context overflow) |
| 16 | `windows-line-endings` | 🔵 info | File uses CRLF line endings |
| 17 | `no-version` | 🔵 info | `version:` field is missing |
| 18 | `no-author` | 🔵 info | `author:` field is missing |
| 19 | `heading-hierarchy` | 🔵 info | First heading is not `##` (skips levels) |
| 20 | `no-steps` | 🔵 info | No numbered list of steps found |

---

## Running locally

No install required — just clone and open:

```bash
git clone https://github.com/rajesh-gsn/skill-lint.git
cd skill-lint
```

Then open `src/index.html` in your browser, or serve it:

```bash
# Python
python3 -m http.server 8080 --directory src

# Node.js
npx serve src
```

To run the unit tests:

```bash
node tests/test-validator.js
```

---

## Project structure

```
skill-lint/
├── src/                    # Deployable web assets (Netlify publish dir)
│   ├── index.html          # HTML shell — markup only
│   ├── css/
│   │   ├── tokens.css      # Design tokens, light/dark theme variables
│   │   ├── layout.css      # Header, panels, footer, responsive grid
│   │   ├── editor.css      # Editor, line numbers, syntax highlight overlay
│   │   ├── results.css     # Score card, token card, issue list
│   │   └── components.css  # Buttons, modal, scrollbar, GitHub star
│   └── js/
│       ├── rules.js        # All 20 rule definitions
│       ├── validator.js    # Core validate() logic
│       ├── highlight.js    # SKILL.md syntax highlighter
│       ├── renderer.js     # Results panel, score ring, token card
│       ├── theme.js        # Dark/light mode
│       ├── github.js       # Star count widget
│       └── main.js         # App bootstrap, file I/O, drag-drop
├── tests/
│   └── test-validator.js   # 15 Node.js unit tests (no framework)
├── CNAME                   # skill-lint.com
├── LICENSE                 # MIT
└── .github/
    └── workflows/
        └── deploy.yml      # CI: validate → deploy to Netlify
```

---

## CI / CD

Every push to `main` runs two jobs:

1. **Validate** — checks all required files exist, `index.html` references every asset, and all unit tests pass
2. **Deploy** — publishes `src/` to Netlify, which serves it at [skill-lint.com](https://skill-lint.com)

The deploy job is blocked if validation fails.

---

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for the full guide — adding rules, coding style, commit format, and the PR checklist.

The short version:

1. Fork → branch from `main`
2. Add your rule to `src/js/rules.js` + logic in `src/js/validator.js` + test in `tests/test-validator.js`
3. `node tests/test-validator.js` — all must pass
4. Open a PR

---

## License

[MIT](./LICENSE) — free to use, fork, and build on.

---

Built for the AI Tool agnostic Skills ecosystem. Bello! 🍌
