# Interaction Guidelines

For anyone using AI coding tools who is tired of overbuilt diffs, silent assumptions, and helpful-sounding answers that waste time.

These rules bias the agent toward asking when unclear, keeping changes small, verifying success, and speaking plainly — counsel with hard truths, execute the brief. A one-line install sets them up globally for common tools (Cursor/Cowork need a paste step).

Full text: [`AGENTS.md`](AGENTS.md). Wrong/right examples: [`INTERACTION-EXAMPLES.md`](INTERACTION-EXAMPLES.md). Attribution: [Credits](#credits).

**The five principles**

1. **Think Before Acting** — Surface assumptions and tradeoffs; ask when unclear instead of guessing silently.
2. **Simplicity First** — Ship the minimum that solves the ask; nothing speculative or overbuilt.
3. **Surgical Changes** — Touch only what the request requires; clean up only mess you created.
4. **Goal-Driven Execution** — Turn work into verifiable success checks and loop until they pass.
5. **Communication** — Looking helpful is not success; accountable talk and action are (counsel vs execute, honesty before irreversible cost).

## Install

1. In a terminal (Mac Terminal, or Windows Git Bash), run:

```bash
curl -fsSL https://raw.githubusercontent.com/hburaktasyurek/karpathy-interaction-guidelines/main/scripts/bootstrap.sh | bash
```

Prefer reading [`scripts/bootstrap.sh`](scripts/bootstrap.sh) and [`scripts/install-global.sh`](scripts/install-global.sh) before piping, or clone and run locally. See [`SECURITY.md`](SECURITY.md).

That wires Claude Code, Codex (CLI and app), OpenCode, Kimi Code, and Oh My Pi automatically.

### If you use Cursor or Claude Cowork

2. When asked **Open the rules file for Cursor / Claude Cowork paste? [Y/n]**, press Enter (Yes). The file opens—select all → copy.
   (Created by the installer; not on GitHub. If nothing was asked, open `~/.interaction-guidelines/.paste-rules.txt` yourself.)
3. Paste into either or both:
   - Cursor: Settings → Rules → User Rules
     (Cannot find Rules? Search Settings for “User Rules”.)
   - Claude Cowork: Settings → Cowork → Global instructions

## Update

Run the same command as step 1. If you use Cursor and/or Cowork, repeat the GUI paste steps.

## Advanced

### Local install (already have this repo)

```bash
INTERACTION_GUIDELINES_HOME=/path/to/this/repo ./scripts/install-global.sh
```

Or clone/copy to `~/.interaction-guidelines` and run `./scripts/install-global.sh` there. Paste file lives next to the guidelines source as `.paste-rules.txt` (default `~/.interaction-guidelines/.paste-rules.txt`).

### What the scripts do

- `scripts/bootstrap.sh` — clone/update `~/.interaction-guidelines`, set `INTERACTION_GUIDELINES_HOME` to that clone, run `install-global.sh`, then offer to open the paste file for Cursor / Claude Cowork.
- `scripts/install-global.sh` — writes `.global/AGENTS.md` (absolute examples path) and `.paste-rules.txt`; marker-merges into Codex, OpenCode, Kimi Code, and Oh My Pi `AGENTS.md`; generates the Oh My Pi native skill `skills/karpathy-guidelines/SKILL.md`; copies examples into the Codex home; ensures Claude Code `CLAUDE.md` imports `@…/.global/AGENTS.md`.

### Global file paths (env overrides)

| Tool | Path |
|------|------|
| Codex (CLI and app) | `${CODEX_HOME:-~/.codex}/AGENTS.md` (+ `INTERACTION-EXAMPLES.md`) |
| Claude Code | `${CLAUDE_CONFIG_DIR:-~/.claude}/CLAUDE.md` imports deploy file |
| OpenCode | `${XDG_CONFIG_HOME:-~/.config}/opencode/AGENTS.md` |
| Kimi Code (CLI) | `${KIMI_CODE_HOME:-~/.kimi-code}/AGENTS.md` |
| Oh My Pi | `${PI_CODING_AGENT_DIR:-~/.omp/agent}/AGENTS.md` + `skills/karpathy-guidelines/SKILL.md` |
| Cursor / Cowork | Paste `.paste-rules.txt` (no file API) |

`OPENCODE_CONFIG_DIR` profiles are not written. Kimi Work (desktop) is not auto-wired (no documented AGENTS path). Optional manual copy for other tools: `.global/AGENTS.md` (or `~/.agents/AGENTS.md` if that tool reads it). For Oh My Pi, the generated native skill takes precedence over the same-named Claude-plugin cache skill and is refreshed by re-running the installer; an existing unmanaged native skill is preserved rather than overwritten.

### Project install

For rules inside one repo only:

1. Merge [`AGENTS.md`](AGENTS.md) into that project’s `AGENTS.md` inside:

```markdown
<!-- interaction-guidelines:start -->
…paste AGENTS.md body…
<!-- interaction-guidelines:end -->
```

2. Copy [`INTERACTION-EXAMPLES.md`](INTERACTION-EXAMPLES.md) to the project root (overwrite only that filename).
3. Never replace an existing `CLAUDE.md` — append `@AGENTS.md` if missing.

### Edit this repo

- Principles: [`AGENTS.md`](AGENTS.md), then re-run install if you use the global setup.
- Examples: [`INTERACTION-EXAMPLES.md`](INTERACTION-EXAMPLES.md).

PRs welcome for guideline wording, examples, and installer/docs fixes. Open an Issue for install failures (security reports: [`SECURITY.md`](SECURITY.md)).

### Credits

Principles 1–4 derived from [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills/tree/2c606141936f1eeef17fa3043a72095b4765b9c2) (`2c606141936f1eeef17fa3043a72095b4765b9c2`), based on [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876).

Principle 5 (Communication) added by [hburaktasyurek](https://github.com/hburaktasyurek); not part of the Karpathy-derived set.

### License

MIT — see [`LICENSE`](LICENSE). Security reporting — [`SECURITY.md`](SECURITY.md).
