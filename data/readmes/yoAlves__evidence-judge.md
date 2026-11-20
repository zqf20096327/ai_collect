# evidence-judge

> Evidence-first research for OpenCode V2: isolated critics, one binary judge,
> and a dossier built only from verified excerpts.

![The judge in court: a binary PASS/FAIL gate over evidence](docs/images/judge-metaphor.svg)

The goal is not to "generate plausible text". It is to produce material where
every claim traces back to a verified excerpt, and whatever fails the gate
becomes `pending` or `excluded` (never fact).

## About

`evidence-judge` is a small experiment in evidence-first agent engineering: a
thin OpenCode V2 plugin (a skill plus a command) that turns a study question into
a dossier assembled only from verified excerpts. Independent researchers gather
sources, isolated critics review the ledger without seeing each other's work,
and a binary judge gate decides what becomes fact, `pending`, or `excluded`. The
orchestrator only transcribes those decisions — it never invents them.

It is built for studying and verifying claims, not for producing plausible text
or professional advice. See [How it works](#how-it-works) for the protocol,
[Definitions](#definitions) for the vocabulary, and
[Design decisions](#design-decisions) for the trade-offs.

| At a glance | |
| --- | --- |
| **Host** | OpenCode V2 (plugin API 2.x; tested on 2.3.0), POSIX shell |
| **Install** | git spec pinned to `v0.1.0` (or an exact commit SHA) |
| **Entry point** | `/judge <request>` |
| **Output** | `dossier.md` in a temporary system directory |
| **Gate** | binary `PASS`/`FAIL`, at most two retries |

Requires Git and network access at install time to fetch the `@opencode/plugin`
dependency.

## Installation

Add the pinned git spec to your OpenCode config:

```jsonc
{
  "plugins": ["evidence-judge@git+https://github.com/yoAlves/evidence-judge.git#v0.1.0"]
}
```

Or install it from the CLI:

```bash
opencode plugin add 'git+https://github.com/yoAlves/evidence-judge.git#v0.1.0'
```

The plugin registers the `judge` skill and the `/judge` command. No need to
create agent, skill, or command files by hand.

- **Unpinned:** drop `#v0.1.0` to install the latest commit at install time.
- **Exact pin:** use the full commit SHA from the release notes (`#<sha>`);
  tags are never moved.

Config changes reload plugins automatically; `/reload` forces a reload. A
service restart is only needed if a cached git dependency is stale.

For development, clone the repository, run `npm install`, and point `plugins`
at the absolute path of the clone (OpenCode does not expand `~`):

```jsonc
{
  "plugins": ["/path/to/evidence-judge"]
}
```

See the [installation guide](https://github.com/yoAlves/evidence-judge/blob/main/.opencode/INSTALL.md)
for details, updating, and troubleshooting.

> **Existing `judge` definitions win.** If a `judge` skill or command from
> another source already exists (your own files or another plugin), the plugin
> does not overwrite it: the existing definition wins and, in most cases, the
> whole pair is left out. In a rare race, the plugin's skill may end up
> registered without the command. Remove or rename the old definition before
> installing. Definitions owned by the plugin itself are re-registered without
> warning — the host may call the plugin setup more than once per load.

## Usage

Run the command with a request:

```text
/judge <request>
```

The request should state whatever is verifiable (count, language, snippet
format, required fields). That becomes the **delivery contract**, which is an
approval requirement — the judge does not approve an incomplete contract.

### Example: research dossier

```text
/judge Research X from official sources. Deliver: 2–3 items per topic,
in English, with a short evidence quote and a re-findable locator.
```

### Example: source-grounded questions and tests

```text
/judge Build a study quiz about topic X from official documentation.
Deliver: 2–3 questions per subtopic, in English, each with the correct answer,
a short evidence quote, and a re-findable locator. Mark any item without a
direct quote as `pending`.
```

Questions and answers are claims like any other in the dossier: each one keeps
the quote and locator of the evidence behind it. If an answer cannot be traced
to a real excerpt, it stays `pending` (or `excluded`) instead of being presented
as fact — so the generated study material always tells you where it came from.

The output is a `dossier.md` in a temporary system directory. The user's
document is not edited; if an edit is requested later, it is a separate step.

## How it works

1. **Scope and contract** — fix the question, sub-questions, sources, and the delivery contract.
2. **Isolated research** — independent researchers find sources and record literal excerpts with locators in `research/`.
3. **Fan-in** — evidence is consolidated with `ledger_version` (revision + line count) and conflicts are recorded.
4. **Critic panel (2–5)** — each critic sees `ledger.md`, `conflicts.md`, and their own brief; they do not see `research/`, other critiques, or judge reports.
5. **Judge gate** — binary: `PASS` or `FAIL`. There is no "approved with conditions"; a condition becomes `pending` or a retry.
6. **Retry (max 2)** — a new judge per retry, with new evidence upserted by id.
7. **Deterministic assembly** — `dossier.md` comes from the ledger, grouped by domain in first-appearance order, with no index mapping.

![Fan-out > fan-in and the retry iteration cycle](docs/images/fan-out-cycle.svg)

The first diagram shows the run as a cycle: researchers fan out, evidence
converges into the ledger, the critic panel reviews, and the judge either
passes the dossier or sends the retry back to the ledger. The second shows the
same system as a static architecture: who can see what, where evidence and
decisions live, and why the judge is the only content gate.

![Architecture: isolated critics, evidence, judge, and ledger](docs/images/judge-arch.svg)

## Definitions

| Term | Meaning |
| --- | --- |
| **Evidence** | A literal excerpt from a real source, with a re-findable locator. No excerpt, no claim. |
| **Delivery contract** | The verifiable requirements in the request (count, language, snippet format, fields). An incomplete contract cannot be approved. |
| **Ledger** | Consolidated evidence and recorded decisions, versioned by `ledger_version` (revision + line count). Shared state — not the critics' or judge's reports. |
| **Conflict** | A documented relationship between evidence items: `factual_clash`, `scope_clash`, `duplicate`, or `dead_reference`. |
| **Critic panel** | 2–5 isolated reviewers. Each sees the ledger, conflicts, and their own brief — never `research/`, other critiques, or judge reports. |
| **Judge gate** | The only content gate. Binary `PASS`/`FAIL`; no "approved with conditions". |
| **`pending` / `excluded`** | A claim held without a verdict / rejected by the gate. Neither is presented as fact. |
| **Scratchpad** | A temporary runtime directory (via `mktemp`). Nothing is written into the user's project. |
| **Injection attempt** | Instructions embedded in fetched pages. Ignored and recorded as data, never followed. |

## Design decisions

| Decision | Why | Cost |
| --- | --- | --- |
| No excerpt, no claim | Inference appears only as `pending`; nothing is invented | Smaller dossier |
| Isolated critics, blind judge | Avoids anchoring and critique contamination; ledger state is still shared | More subagents per run |
| The judge is the only content gate | The orchestrator transcribes decisions verbatim; the assembly check tests form, not merit | No automatic repair of weak reasoning |
| Binary gate | Removes the gray zone of "almost approved" | More retries in borderline cases |
| Temporary scratchpad only | No litter in the user's repository | Artifacts vanish after the run |
| External content is data | Embedded commands are ignored and recorded as injection attempts | Requires disciplined prompt handling |
| Progressive disclosure | `SKILL.md` holds the always-on protocol; each step loads only its own reference from `skills/judge/references/` | More files, one load per step |

## What works well

- Every claim in the dossier is traceable to a quoted excerpt and a locator.
- Assembly is deterministic: ledger order, grouped by domain in first-appearance order, with no index mapping.
- Isolation limits anchoring and critique contamination without hiding ledger state.
- The protocol leaves no artifacts in the user's project.
- The core is portable markdown plus one TypeScript adapter; installation is a single config line.
- Releases are reproducible: the git tag is pinned, and installs by SHA, tag, and CLI were verified in isolated profiles with no plugin warnings.

## Open points

- **Windows is untested.** The protocol assumes a POSIX shell and `mktemp`; a POSIX-compatible environment is required.
- **No npm registry publish.** Distribution is the OpenCode git spec only; the npm name remains unclaimed.
- **No CI, provenance, changelog, or version badge.** The GitHub Release carries the 0.1.0 notes.
- **Claude Code adapter deferred.** It would swap only `src/index.ts`; the markdown core is neutral.
- **Cost of isolation.** More subagents per run and up to two retries mean extra time and tokens.
- **Judge isolation is deliberate.** A retrying judge sees the ledger, conflicts, and the current version's critiques — never a previous judge report or earlier rounds' critiques.
- **Sources are external.** Availability, accuracy, and terms of third-party pages can change; the output is not professional advice.
- **Pinned installs are static.** Tags never move, so a fix ships as a new tag; `opencode plugin list`/`check` may not show git-spec plugins, and CLI management needs the exact specifier from the config.

## Status

| Item | Value |
| --- | --- |
| Version | 0.1.0 |
| Install ref | `v0.1.0` (annotated tag, never moved) |
| Release | [GitHub Release](https://github.com/yoAlves/evidence-judge/releases/tag/v0.1.0) |
| Verified commit | `0336dcd4415a37bc5c7f1cd28e611b70d0727cf4` |
| Hygiene gate | `npm run check` → `HYGIENE: PASS` before the tag |

## Structure

```text
.opencode/INSTALL.md      detailed install/verify/update guide
src/index.ts              registers the skill and the command
skills/judge/SKILL.md     protocol and hard rules
skills/judge/references/  per-step references, loaded on demand
scripts/check-hygiene.sh  release hygiene gate
docs/                     versioned plan (plan/) and diagrams (images/)
```

## Development

In the repository, run the hygiene gate before creating a release tag:

```bash
npm run check
```

or directly:

```bash
bash scripts/check-hygiene.sh
```

It fails if an absolute path, local environment reference, or foreign project
name appears in the package files (`src`, `skills`, `README.md`, `LICENSE`,
`package.json`) or in `.gitignore` (checked as a precaution). The gate is a dev
tool and is not shipped in the installed package, so run it from the repository.

## Acknowledgements

Inspired by [llm-council](https://github.com/karpathy/llm-council) and
[claude-skills-llm-council](https://github.com/aiwithremy/claude-skills-llm-council).

## License

MIT

## Disclaimer

This project is not affiliated with or endorsed by OpenCode. The plugin and its
output are provided "as is", without warranty of any kind, express or implied.
The dossier is built from third-party sources at runtime; their availability,
accuracy, and terms may change. The output is not professional advice, and you
are responsible for verifying sources and claims before relying on them. The
authors are not liable for any loss or damage arising from use of the software
or its output.
