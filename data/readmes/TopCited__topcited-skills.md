# TopCited Skills

Agent Skills that teach an AI coding agent — Claude Code, Codex, or anything else
that can read Markdown — how to do SEO and **GEO** (Generative Engine
Optimization: being found and cited by ChatGPT, Claude, Gemini and Perplexity),
and how to drive the [TopCited](https://topcited.ai) API on your behalf.

These are the same skills TopCited's own hosted agent runs on. This repo is the
single source of truth for them.

| Skill | What it gives your agent |
|---|---|
| [`seo-geo`](skills/seo-geo) | A cited, dated knowledge base: technical SEO, entity & authority, content strategy, GEO, measurement, distribution playbooks. Read before making a judgment call, instead of answering from memory. |
| [`topcited-api`](skills/topcited-api) | How to call the TopCited API: per-feature guides (when, why, what it costs, how it fails) plus the generated endpoint reference. |
| [`visibility-workflow`](skills/visibility-workflow) | An eight-stage engagement that takes a brand from "no idea if we're visible" to a measured, improved baseline — using the two skills above. |

Install all three. `visibility-workflow` orchestrates the other two and
`topcited-api` defers SEO judgment to `seo-geo`; they reference each other by
relative path, so they need to sit as siblings.

## Install

### Claude Code (plugin)

```
/plugin marketplace add TopCited/topcited-skills
/plugin install topcited-skills@topcited
```

### Any agent (manual)

Clone and drop the skills into your personal skills directory:

```bash
git clone https://github.com/TopCited/topcited-skills.git
cp -r topcited-skills/skills/* ~/.claude/skills/
```

For a project rather than your whole machine, use `.claude/skills/` in the repo
instead.

### Any agent (no install)

Everything here is plain Markdown, so an agent that can fetch a URL needs no
install at all — point it at a raw file and it will follow the links from there:

```
https://raw.githubusercontent.com/TopCited/topcited-skills/main/skills/seo-geo/SKILL.md
https://raw.githubusercontent.com/TopCited/topcited-skills/main/skills/topcited-api/SKILL.md
https://raw.githubusercontent.com/TopCited/topcited-skills/main/skills/visibility-workflow/SKILL.md
```

Each `SKILL.md` opens with YAML frontmatter (`name`, `description`) and a routing
table saying what to read next. Two caveats when fetching rather than cloning:
the internal links are **relative paths**, so resolve them against the file's own
directory; and `skills/topcited-api/scripts/tc-api.sh` will not be on disk, so
either fetch it too or make the calls with plain `curl` — the SKILL.md shows the
equivalent one-liner.

Pin to a tag or commit SHA instead of `main` if you need the content to stay put.

## Getting an API key

`seo-geo` needs no credentials. `topcited-api` and `visibility-workflow` do.

1. Sign in at [topcited.ai](https://topcited.ai).
2. **Settings → Profile → API keys → Create key.** Any account can create one.
3. Copy it — it is shown once and starts with `tc_`. You can hold up to 5
   active keys and revoke them individually. Keys **expire 90 days** after
   creation; when one lapses every call starts failing at once, and the fix is
   to create a new one.

Then export it:

```bash
export TOPCITED_API_KEY="tc_..."
```

| Variable | Required | Default | What it is |
|---|---|---|---|
| `TOPCITED_API_KEY` | yes | — | Your personal key. Acts as you, with full rights over your account; treat it like a password. |
| `TOPCITED_BASE_URL` | no | `https://api.topcited.ai` | API base. |
| `TOPCITED_UI_URL` | no | `https://topcited.ai` | Web app base, used only to build links shown to you. |

The API and the web app are different hosts — if you override one, override both.
Pointing an API call at the web-app host does not fail cleanly: `https://topcited.ai/api/v1/...`
returns the web app's HTML rather than JSON or a 404, so "my agent got HTML back"
almost always means the base URL is wrong.

### A note on spending

Most TopCited operations consume T-coins (credits) from your plan. The skills are
written to check `GET /api/v1/users/me/coin-balance` — which is free — and to ask
you before spending. If you wire these skills into an unattended automation, you
are removing that confirmation step; put your own budget guard in front of it.

## Repo layout

```
skills/
  seo-geo/              SKILL.md + knowledge/
  topcited-api/         SKILL.md + references/ (+ references/endpoints/) + scripts/
  visibility-workflow/  SKILL.md + stages/ + templates/
.claude-plugin/         Claude Code plugin + marketplace manifests
```

`skills/topcited-api/references/endpoints/` is generated from the TopCited
OpenAPI schema — don't hand-edit it; open an issue instead.

## Contributing

Issues and PRs welcome, especially: a knowledge file that has gone stale (each
carries a `last-verified` date and its sources), an endpoint guide that no longer
matches the API, or a stage that reads as jargon to a non-expert.

## License

[MIT](LICENSE). The knowledge files cite third-party sources; those citations are
links, not redistribution of the cited work.
