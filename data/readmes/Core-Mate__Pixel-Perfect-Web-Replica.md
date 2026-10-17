# Pixel Perfect Web Replica

![Pixel Perfect Web Replica demo](docs/assets/demo.gif)

Turn any public webpage into a local, editable, pixel-faithful replica with one AI skill.

Paste a URL. Codex or Claude Code will mirror public HTML/CSS/JS/media assets, run the page locally, verify desktop and mobile rendering, fix common fidelity issues, and generate a replaceable-resource inventory for rebranding.

[中文 README](README.zh-CN.md) · [Installation](docs/installation.md) · [Prompt Examples](examples/prompts.md) · [QA Checklist](references/replica-qa.md)

## What It Does

- **Mirrors public webpages locally**: downloads browser-accessible same-origin HTML, CSS, JS, images, videos, fonts, favicons, and manifest assets.
- **Keeps fidelity as the goal**: preserves layout, typography, media crop, root-relative paths, scroll behavior, and mobile rendering.
- **Runs as a real local page**: uses a static server instead of `file://`, so assets and browser behavior stay closer to the original.
- **Creates rebranding inventory**: generates `REPLACEABLE_RESOURCES.md`, `resources.json`, and `resource-inventory.json`.
- **Guides agent QA**: tells Codex or Claude Code how to compare screenshots, catch broken fonts, fix missing CSS assets, and report remaining gaps.

## Quick Install

Install for both Codex and Claude Code:

```bash
curl -fsSL https://raw.githubusercontent.com/Core-Mate/Pixel-Perfect-Web-Replica/main/scripts/install.sh | bash
```

Install with the `skills` CLI:

```bash
npx skills@latest add Core-Mate/Pixel-Perfect-Web-Replica
```

Codex only:

```bash
curl -fsSL https://raw.githubusercontent.com/Core-Mate/Pixel-Perfect-Web-Replica/main/scripts/install.sh | bash -s codex
```

Claude Code only:

```bash
curl -fsSL https://raw.githubusercontent.com/Core-Mate/Pixel-Perfect-Web-Replica/main/scripts/install.sh | bash -s claude
```

## Try It

Ask your agent:

```text
Use pixel-perfect-web-replica to mirror https://example.com locally. Capture public assets, run it on a static server, verify desktop and mobile screenshots, and list replaceable brand assets.
```

Or use the bundled mirror script directly:

```bash
python3 scripts/mirror_public_page.py https://example.com ./replica-output
cd replica-output
python3 -m http.server 8088
```

## What You Get

```text
replica-output/
├── index.html
├── assets copied from the public page
├── resources.json
├── resource-inventory.json
└── REPLACEABLE_RESOURCES.md
```

`REPLACEABLE_RESOURCES.md` helps identify:

- logos, favicons, and manifest icons
- fonts and brand assets
- hero media, app screenshots, and videos
- Open Graph images
- CTA links, legal links, and copy blocks

## Why Not Just Use wget Or Save Page As?

| Need | Browser save | `wget` | This skill |
| --- | --- | --- | --- |
| Agent-guided visual QA | No | No | Yes |
| Desktop and mobile screenshot comparison | No | No | Yes |
| Replaceable asset inventory | No | No | Yes |
| Public same-origin asset mirroring | Partial | Yes | Yes |
| Rebranding-oriented output | No | No | Yes |
| Clear safety boundaries | No | No | Yes |

## Best For

- studying how a public landing page is built
- building a local sandbox before redesigning a page
- migrating a public visual reference into your own frontend
- generating a replaceable asset map before rebranding
- testing AI frontend agents on visual fidelity tasks
- comparing original and local rendering across desktop and mobile

## How The Skill Works

1. Scope the target public URL and output folder.
2. Capture original evidence with headers, HTML, screenshots, and resource lists.
3. Mirror same-origin static assets with `scripts/mirror_public_page.py`.
4. Serve the replica locally with `python3 -m http.server`.
5. Compare original and local screenshots at desktop and mobile sizes.
6. Fix missing assets, broken root paths, fonts, video crop, and mobile overflow.
7. Produce `REPLACEABLE_RESOURCES.md` and report remaining differences.

## Repository Structure

```text
.
├── SKILL.md                         # Core agent skill instructions
├── agents/openai.yaml               # Codex UI metadata
├── scripts/install.sh               # One-line installer
├── scripts/mirror_public_page.py    # Static page mirroring helper
├── references/replica-qa.md         # QA checklist for mirrored pages
├── references/quality-checklist.md  # General visual fidelity checklist
├── examples/prompts.md              # Prompt examples
├── docs/installation.md             # English install guide
├── docs/installation.zh-CN.md       # Chinese install guide
└── docs/github-about.md             # GitHub About and SEO metadata
```

## Safety

This skill is for public, browser-accessible pages and local study workflows.

Do not use it to bypass authentication, paywalls, bot defenses, robots restrictions, signed URLs, private APIs, or access controls. Before publishing a derivative page, replace copyrighted or trademarked assets and verify licensing.

## License

MIT License. See [LICENSE](LICENSE).
