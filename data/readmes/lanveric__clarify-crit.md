# Clarify (CRIT)

**Clarify** is a lightweight request-refinement skill for AI models, built on the **CRIT** method (Context, Role, Interview, Task). It helps a model understand a user's request before acting — resolving ambiguity with the minimum questions, minimum visible structure, and minimum interaction cost.

```text
Use CRIT. Build a dashboard for my business.
```

CRIT recovers what's already known, asks only what materially changes the outcome, and either answers directly or hands back a short, portable brief — instead of opening every request with a long discovery form.

## In this repo

- [`clarify-crit/`](clarify-crit/) — the distributable skill package. This folder alone is what gets uploaded to the Claude.ai skill uploader (or grab the prebuilt [release zip](https://github.com/lanveric/clarify-crit/releases/latest)).
- [`tests/`](tests/) — development and regression assets (evaluation guide, machine-readable regression prompts). Not part of the runtime skill.

For installation, usage, compatibility, and feedback, start with **[clarify-crit/README.md](clarify-crit/README.md)**.

## Licence

MIT — see [`clarify-crit/LICENSE`](clarify-crit/LICENSE).
