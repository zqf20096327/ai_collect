<div align="center">

# 🪢 session_wrapper

**Portable session handoffs: one file from a long agent session or chat that you can paste into any model or tool.**

Long sessions degrade, and switching tools means starting over. session_wrapper reads the session's log from disk and writes the state worth carrying across: what you asked, what you decided and corrected (in your own words), what failed and was never fixed, which files changed, the last test run, what is still open. No model, no network, no key. Secret-shaped values are removed before anything is written.

[![test](https://github.com/codegobrrrr9/session_wrapper/actions/workflows/test.yml/badge.svg)](https://github.com/codegobrrrr9/session_wrapper/actions/workflows/test.yml)
[![license](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
![zero deps](https://img.shields.io/badge/dependencies-0-brightgreen)

</div>

## The idea, and where it stands

The usual advice for switching agents is "ask the model to write a HANDOFF.md before you quit". That summary is written from a long, degraded context, it costs output tokens, and it is impossible when your quota has just run out. session_wrapper skips the model: it reads the log file the agent already left on disk and **extracts** the parts a next session needs. The same log always gives the same file.

This is not a new category. Several tools already do session handoff, and some do parts of it better than this one (see [Compared with the others](#compared-with-the-others)). What this one is: **zero-dependency Node that is tested on Windows, secrets redacted before writing and checked again after, your own corrections and rejections kept verbatim, every item citing a turn you can verify with `check`, and a Markdown file you can paste into a plain chat window.**

## For your coding agent

Paste this into Claude Code, Codex, Cursor or Gemini CLI:

```
Install the session_wrapper skill from https://github.com/codegobrrrr9/session_wrapper, refer to the repo's AGENTS.md.
```

No install:

```bash
npx --yes --allow-git=all github:codegobrrrr9/session_wrapper wrap                 # newest Claude Code session of this folder
npx --yes --allow-git=all github:codegobrrrr9/session_wrapper wrap --from codex    # newest Codex session started here
npx --yes --allow-git=all github:codegobrrrr9/session_wrapper wrap --path chat.json --copy   # a ChatGPT / Claude.ai export
```

The file is written to `.session_wrapper/handoffs/` inside the project and kept out of git through `.git/info/exclude` (never your tracked `.gitignore`), so it cannot be committed by accident.

## What it writes

From a small made-up session (the tests' fixture; [`docs/example-handoff.md`](docs/example-handoff.md), regenerate with `node docs/make-example.mjs`):

```
# Session handoff: Fix checkout webhook

- Source: claude-code · session `sess-000` · 2026-11-01 · 3 prompts, 4 replies, 9 tool calls · project `shop` · branch `main`
- Redacted before writing: 1 secret-shaped value(s) (stripe_key ×1). Heuristic, not a guarantee.

## Goal (derived, confirm)
- First request: "The checkout webhook fails on retries. Fix it, and add a test." [t1]

## Decisions and constraints (your words)
- correction: "No, do not change the public handler signature. Always keep handle(req) as it is." [t6]
- "Which store should hold the retry counter? → Postgres" [t12]

## Dead ends (failed and not fixed later)
- Bash node scripts/seed.js → "Error: ENOENT: no such file or directory, open seed.json" [t11]

## Key files
- `tests/webhook.test.js`: written 1× [t9]
- `src/webhook.js`: edited 2×, read 1× [t8]

## Next steps
- From the last todo list [t13]:
  - Write the migration for the counter
  - Update the docs (in progress)
```

Every `[t11]` is the position of that event in the session. `session_wrapper check <handoff.md>` re-reads the log and confirms each turn exists and each quoted passage is really in it, so an edited or stale handoff is caught. On a real 70-prompt, 1,395-tool-call session from the author's machine it ran in under a second and the check passed (64 citations, 18 quotes).

Sections: goal, where it stopped, decisions and constraints, dead ends, key files, commands and tests, open questions, next steps, and the agent's own compaction summary if Claude Code compacted the session. How each is built, and what was and was not verified against real logs: [`references/method.md`](skills/session-wrapper/references/method.md).

## Commands

```
session_wrapper [wrap]  [--session id] [--from claude-code|codex|file|stdin] [--path file] [--all] [--budget N]
                        [--json] [--copy] [--stdout] [--out file] [--no-cite]
session_wrapper sessions [--from codex] [--all]
session_wrapper check <handoff.md> [--path log] [--session id]
```

`--budget` (default 4,000 tokens, estimated as characters / 4) shrinks every section in fixed steps and then drops whole sections in a fixed order; the last line of the file says what was cut. `--json` writes the same facts as JSON next to the Markdown.

## Security

- Every string is passed through the [agent-residue](https://github.com/codegobrrrr9/agent-residue) detector before it enters the model, and findings become `[redacted:type]`. The finished text is scanned again and **the tool refuses to write it** if a high- or medium-tier match is left. Tests plant fake keys (built at run time, never committed) in prompts, tool inputs and tool results and check that none appears in the Markdown, the JSON, stdout or stderr.
- The detector is heuristic. Its first benchmark recall was 91.3% (137 of 150) on a corpus its author wrote, with 0 false positives on 60 hard negatives and 12 public files. Treat this as a strong filter, not a guarantee, and read the file before you paste it.
- **A handoff goes to another provider when you paste it.** The tool never sends anything anywhere.
- It never reads auth or credentials files, and thinking blocks are never read.

## Compared with the others

From their READMEs on 2026-11-08. I have not run them, so this is what they say they do, not a test.

| Tool | What it does | Where it is stronger than this |
|---|---|---|
| [sukamenev/baton](https://github.com/sukamenev/baton) | Go CLI + skill; reads raw logs, no model | Covers more agents (Pi, OpenCode, Antigravity, Cursor), single binary |
| [Dicklesworthstone/cross_agent_session_resumer](https://github.com/Dicklesworthstone/cross_agent_session_resumer) (casr) | Converts a session into another agent's native format so you can *resume* it | A real resume, not a paste |
| [Frankie-Xu/threadport](https://github.com/Frankie-Xu/threadport) | A "Context Capsule" JSON/Markdown with git state and redaction; adapters for Claude, Codex, Cursor, Gemini | A richer schema and more adapters |
| [alexknowshtml/claude-auto-handoff](https://github.com/alexknowshtml/claude-auto-handoff), [obie/auto-handoff](https://github.com/obie/auto-handoff) | Have a model write the brief, automatically near the limit or when idle | Better prose, hands-free; they cost tokens and need quota |
| [sting8k/pi-vcc](https://github.com/sting8k/pi-vcc) | Algorithmic compaction inside Pi, benchmarked on fact recall | Pi only, but measured |
| [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory), [oceanbase/powercontext](https://github.com/oceanbase/powercontext) | Memory services with handoff between sessions and agents | A server, shared across machines and people |

## Honest limits

- **It extracts, it does not understand.** The goal and decisions are quotes and pattern matches from the log, labelled "derived". A model-written brief will read better and can capture intent this cannot. This tool's bet is that a verifiable extract beats a lossy summary; that bet is [not benchmarked yet](#benchmark).
- **Claude Code's log format is not documented.** The reader was checked against one real install (entry types, compaction markers, sidechains, question answers, plan tools), by printing key paths only. `TodoWrite` could not be confirmed (no session there used it), so it is read when present.
- **Codex support is a sample, not a spec.** Roles, tool calls and outputs were confirmed from one install's `.jsonl.zst` files. How Codex reports a failed command was not seen, so failures are a text heuristic, and files are read from `apply_patch` blocks only. Reading `.zst` needs Node 22.15 or newer.
- **ChatGPT and Claude.ai exports are fixture-tested only.** I have not read a real export.
- **Files touched by shell commands** (`sed -i x`, `cat > y`) are not found, only file-tool calls.
- Cursor, Gemini CLI and Copilot native session stores are not read: use a pasted or exported transcript.
- Images and thinking are not carried. Subagent work appears only as the main session's calls to it.
- Tokens are estimates (characters / 4).

## Benchmark

Not run yet. The method is committed before any run: [`benchmarks/PREREGISTRATION.md`](benchmarks/PREREGISTRATION.md).

## Install by agent

| Agent | How |
|---|---|
| **Claude Code** | `/plugin marketplace add codegobrrrr9/session_wrapper` then `/plugin install session-wrapper@session_wrapper`. Adds `/session-wrapper`. |
| **Codex** | Copy `skills/session-wrapper/` to `~/.codex/skills/session-wrapper/` and append the Rules from [`AGENTS.md`](AGENTS.md). |
| **Cursor** | Copy [`.cursor/rules/session-wrapper.mdc`](.cursor/rules/session-wrapper.mdc) and the folder `skills/session-wrapper/scripts/` into the project. |
| **Gemini CLI** | `gemini extensions install https://github.com/codegobrrrr9/session_wrapper` |
| **GitHub Copilot** | Copy [`.github/copilot-instructions.md`](.github/copilot-instructions.md). |
| **No agent** | `npx --yes --allow-git=all github:codegobrrrr9/session_wrapper wrap` |

The skill is named `session-wrapper` (the Agent Skills spec allows only lowercase letters, digits and hyphens); the repo and package are `session_wrapper`.

## Credits

Same family as [seatbelt](https://github.com/codegobrrrr9/seatbelt), [cheapskate](https://github.com/codegobrrrr9/cheapskate), [alibi](https://github.com/codegobrrrr9/alibi), [shortlist](https://github.com/codegobrrrr9/shortlist), [grudge](https://github.com/codegobrrrr9/grudge), [tollgate](https://github.com/codegobrrrr9/tollgate), [apikeys-handler](https://github.com/codegobrrrr9/apikeys-handler), [agent-residue](https://github.com/codegobrrrr9/agent-residue) (its detector is copied here) and [skilldiet](https://github.com/codegobrrrr9/skilldiet).

## License

MIT. Star ⭐ if it saved you from re-explaining a session.
