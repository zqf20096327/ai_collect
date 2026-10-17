# AI Survival Guide for Engineers

[![GitHub stars](https://img.shields.io/github/stars/sunnykgupta/AI-Survival-Guide?style=flat-square)](https://github.com/sunnykgupta/AI-Survival-Guide/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/sunnykgupta/AI-Survival-Guide?style=flat-square)](https://github.com/sunnykgupta/AI-Survival-Guide/network/members)
[![GitHub issues](https://img.shields.io/github/issues/sunnykgupta/AI-Survival-Guide?style=flat-square)](https://github.com/sunnykgupta/AI-Survival-Guide/issues)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/sunnykgupta/AI-Survival-Guide/deploy.yml?style=flat-square)](https://github.com/sunnykgupta/AI-Survival-Guide/actions/workflows/deploy.yml)

A no-bullshit, role-by-role map for getting into the top 1% as AI commoditizes engineering work. Read it live:

**[ai-survival-guide.forbunnies.com](https://ai-survival-guide.forbunnies.com)**

This is a single-page, statically generated website. The content lives in plain Markdown, so anyone can improve a role without touching HTML or CSS. Every push to `main` rebuilds and redeploys the site automatically via GitHub Actions and GitHub Pages.

---

## How it works

```
content/
  roles/          ← one Markdown file per role (this is what most contributors edit)
    01-frontend.md
    02-backend.md
    ...
    09-em.md
  sections/       ← the framing sections (HTML partials: problem, 3-layer model, universal OS, manifesto, author box, subscribe CTA)
    01-problem-and-model.html
    02-universal-os.html
    03-manifesto.html
assets/           ← illustrations (hero, 3-layer model, manifesto)
template.html     ← page shell + all CSS/JS (design system lives here)
role_icons.py     ← inline SVG icon for each role
build.py          ← reads content/ + template.html → writes dist/index.html
dist/             ← generated output (what GitHub Pages serves). Do not edit by hand.
CNAME             ← custom domain for GitHub Pages
```

`build.py` reads every role's Markdown, renders it into the site's role layout, drops in the framing sections, and writes `dist/index.html`. The GitHub Action runs exactly this on every push.

---

## Contributing to a role

This is the main way to contribute. You do **not** need to know HTML, CSS, or Python.

1. Open the role you want to improve under [`content/roles/`](content/roles) (for example `content/roles/01-frontend.md`).
2. Edit the prose under the headings. **Keep the headings and the front matter (the `--- ... ---` block at the top) exactly as they are.** The build relies on them.
3. Open a Pull Request. Once it is merged to `main`, the site rebuilds and goes live automatically in a minute or two.

### Role file format

Each role file looks like this:

```markdown
---
id: frontend
order: 1
title: Frontend Engineer
short: Frontend
icon: frontend
stack: React · Vue · CSS · Design Systems · Web Performance · Accessibility · Browser APIs
---

## Lead
One punchy opening paragraph that frames the role in the AI era.

## Intro
One or two paragraphs of context. Separate paragraphs with a blank line.

## Layer 1 - Commodity: What AI now does for you
The work AI can already do for this role.

## Layer 2 - Leverage: How to work with AI effectively
How a strong practitioner uses AI as a multiplier.

## Layer 3 - Irreplaceable: What no AI can own
The judgment and ownership that stay human.

## Pull Quote
A single memorable line that sums up the role.

## Real Talk
The honest, direct take.

## Roadmap
1. **Days 1–30: Title.** What to do in the first month.
2. **Days 31–60: Title.** What to do next.
3. **Days 61–90: Title.** What to do to break out.

## Trap
**Bold lead.** The time-sink to avoid, and what to do instead.

## Bonus
One extra high-leverage move.
```

**Formatting notes**

- Use `**bold**` and `*italic*` for emphasis. `[link text](https://url)` for links.
- Use `...` (three dots) for a dramatic pause. **Do not use em dashes;** use commas, periods, or `...` instead. This is a deliberate house style.
- Numeric ranges use an en dash, e.g. `Days 1–30`, `70–85%`.
- The front matter `order` controls position in the guide and the sidebar. `icon` must match a key in `role_icons.py`.

### Adding a brand new role

1. Create `content/roles/NN-your-role.md` (pick the next number) using the format above.
2. Add a matching inline SVG icon in `role_icons.py` under the `id` you chose.
3. Open a PR. The sidebar nav, role count, and routing update automatically.

---

## Editing the framing sections

The Problem, 3-Layer Model, Universal OS, Manifesto, author box, and Subscribe call-to-action live in `content/sections/*.html`. These are HTML partials. Edit the text inside the existing tags. The subscribe links (Substack + LinkedIn Newsletter) are in `content/sections/03-manifesto.html`.

---

## Building locally

No dependencies beyond Python 3.

```bash
python3 build.py
# then open dist/index.html in a browser, or serve it:
python3 -m http.server -d dist 8000   # http://localhost:8000
```

---

## Deployment

Pushing to `main` triggers `.github/workflows/deploy.yml`, which builds the site and publishes `dist/` to GitHub Pages. No manual steps. See [`DOMAIN_SETUP.md`](DOMAIN_SETUP.md) for the one-time custom-domain configuration.

---

## License

Content is shared freely with attribution. See [`LICENSE`](LICENSE). The ideas are meant to be used: take them, apply them, pass them on.

Written by [Sunny R Gupta](https://x.com/sunnykgupta), Engineering Leader at JioHotstar, founder of TeamShiksha and Impromptu Meetups.
