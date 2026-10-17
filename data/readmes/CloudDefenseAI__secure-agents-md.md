# Secure AGENTS.md — Security Working Agreements for Coding Agents (and Humans)

A security-first **AGENTS.md template** you can drop into any repository so **coding agents** (and developers) follow guardrails that reduce real-world security flaws:
- secret leaks
- prompt/tool injection
- supply-chain compromise
- unsafe dependency changes
- weak authz, insecure input handling, and risky defaults

This project is maintained by **CloudDefense.AI** and the community.

---

## What is AGENTS.md?

Many agent tools read `AGENTS.md` files as persistent, repo-scoped instructions. Guidance can be layered with `AGENTS.override.md` for narrower directories and higher priority rules.

This repo provides:
- a hardened `AGENTS.md` baseline (copy/paste)
- checklists and threat-modeling notes
- OSS governance + security policy defaults

---

## Quick start (copy into your repo)

1. Copy `AGENTS.md` into the root of your repository.
2. Optionally add narrower overrides:
   - `AGENTS.override.md` in sensitive subfolders (e.g., `infra/`, `scripts/`, `services/payments/`)
3. Update placeholders:
   - supported languages/frameworks
   - security contacts
   - CI commands, linters, test commands

---
## Using this repository as a template

You can use this repo as a starting point for your own project or to publish a customized template.

### Option A: GitHub “Use this template”

1. On GitHub, open this repo and click **Use this template** → **Create a new repository**.
2. Choose a name (e.g. `my-secure-agents`), visibility, and create the repo.
3. Clone your new repo and then:
   - Update **`.github/ISSUE_TEMPLATE/config.yml`** — set the security report URL to your repo’s Security tab (e.g. `https://github.com/YOUR_ORG/YOUR_REPO/security`).
   - Update **`.github/CODEOWNERS`** with your maintainer handles (or remove the file if you don’t use CODEOWNERS).
   - In repo **Settings → Security**, enable **Private vulnerability reporting**.
4. Customize `AGENTS.md`, `SECURITY.md`, and docs to match your stack and policies (see [Writing your own templates](#writing-your-own-templates) below).

### Option B: Fork or copy manually

- **Fork** on GitHub if you want to track upstream and send PRs back.
- **Copy** the files you need into an existing repo: at minimum `AGENTS.md`; optionally `SECURITY.md`, `.github/` workflows and templates, and `docs/`.

After copying, apply the same post-setup steps as in Option A (security URL, CODEOWNERS, private vulnerability reporting).

---

## Writing your own templates

You can build your own agent-instruction or security templates from this repo.

### Start from this baseline

- Use **`AGENTS.md`** as the base policy. Edit sections to match your stack (e.g. add “We use Python 3.11+” or “CI runs `pytest` and `ruff`”).
- Keep the **non-negotiables** (no secrets, no security regressions, least privilege, treat inputs as hostile, safe tool use, supply-chain discipline). Remove or relax only with explicit justification.
- Add **directory overrides** by creating `AGENTS.override.md` in subfolders. The closest override to a file wins. Example: in `infra/terraform/` add an override that forbids `terraform destroy` without approval.

### Customize by audience

- **Single team:** Shorten `AGENTS.md`, reference your internal runbooks and lint/test commands.
- **Public OSS:** Keep the full policy; set security contact in `SECURITY.md` and in `.github/ISSUE_TEMPLATE/config.yml`.
- **Multi-repo org:** Copy this repo as a template, then add org-specific rules (naming, branching, required checks) and use CODEOWNERS for sensitive paths.

### What to ship in your template

| File / folder | Purpose | Customize? |
|---------------|---------|------------|
| `AGENTS.md` | Main agent + human policy | Yes — languages, CI, contacts |
| `AGENTS.override.md` (per dir) | Stricter rules for sensitive areas | Yes — add where needed |
| `SECURITY.md` | Vulnerability reporting | Yes — contact and response targets |
| `docs/THREAT_MODELING.md` | Lightweight threat model template | Optional — trim or extend |
| `docs/SECURE_CODING_CHECKLIST.md` | Pre-merge checklist | Optional — add stack-specific items |
| `.github/workflows/scorecard.yml` | OpenSSF Scorecard | Optional — keep or remove |
| `.github/dependabot.yml` | Dependency updates | Yes — add package-ecosystem if you have deps |
| `.github/ISSUE_TEMPLATE/` | Bug + feature + security link | Yes — security URL in `config.yml` |
| `.github/pull_request_template.md` | PR security checklist | Optional — align with your process |
| `.github/CODEOWNERS` | Required reviewers | Yes — your maintainers |

When you publish your template, point users to “Use this template” or your own quick-start steps and the [Quick start](#quick-start-copy-into-your-repo) copy-paste flow above.

---

## Recommended companion files

This repo also ships common “serious OSS security” defaults:
- `SECURITY.md` — how to report vulnerabilities (private reporting encouraged)
- `.github/workflows/scorecard.yml` — OpenSSF Scorecard
- `.github/dependabot.yml` — dependency update automation
- PR + issue templates with security checklists
- `docs/SECURE_CODING_CHECKLIST.md` and `docs/THREAT_MODELING.md`

---

## Project goals

- Make it **easy** to do the secure thing by default
- Provide guardrails that work for **agentic workflows**
- Be practical: short, enforceable rules + checklists
- Stay tool-agnostic while supporting modern agent instruction discovery

---

## Contributing

See `CONTRIBUTING.md`. Security-sensitive changes (AGENTS rules, workflows, reporting guidance) require maintainer review.

---

## License

MIT — see `LICENSE`.
