# Lean Agents — two roles

`AGENTS.md` is the **single shared policy** (variant #5, tool contract). It resolves roles, routes one versus multiple tasks, and defines engineering checks. Runtime agent files declare or refine the assigned role; they do not duplicate routing.

| Logical role | When | What it does |
| --- | --- | --- |
| `ORCHESTRATOR` | Default primary (`build`) | Only small single fixes are executed directly. Feature work, refactoring or multi-file changes delegate to foreground `CODER` workers; one worker per deliverable, before any primary write. |
| `CODER` | Assigned worker | Investigates, edits, tests and repairs within scope; can accept read-only audit/verification jobs. Never delegates. |

**Actual worker names:** `general` (OpenCode, Command Code, Pi), `worker` (Codex). `CODER` is a logical role sent in the assignment, not necessarily a registered tool identifier. Preserve the exact proven line in `AGENTS.md`. For overlapping files and shared build outputs, serialize operations. Count independent work scopes, not checklist items. Tests and release metadata required for a fix belong to that fix; delegate separate outcomes only when their edits and verification can be coordinated safely.

## Bundled task-scoped skills

- **`lean-code`**: `skills/lean-code/SKILL.md`. Trigger: "Load lean-code for all coding-related tasks." Always load for implementation, fixes, code review, tests and refactoring. It compresses Ponytail's smallest-complete-change rules into a <1,000-character core, then adds a mandatory post-implementation simplification pass, real-duplication removal, and safe inheritance/composition guidance. Code reviews suggest improvements without editing. Source inspiration: the user-provided `ponytail-main(1).zip` (Ponytail; MIT).
- **`lean-java`**: `skills/lean-java/SKILL.md`. Trigger: "Load lean-java when working on Java/JVM projects." Covers Java, Maven/Gradle, JUnit, concurrency, Spring, JVM diagnostics, safe performance and compatibility. Java+web projects also load lean-web; Java-only projects do not.
- **`lean-web`**: `skills/lean-web/SKILL.md`. Trigger: "Load lean-web when working on web or Node.js projects." Covers JS/TS, HTML/CSS, React/Next.js, async Node, Fastify, APIs, Better Auth/OAuth, ESLint, Turbo, tests, performance. Framework-specific sections apply only when the corresponding stack is present.

Before you start, load all relevant skills to this task and workspace. The executing agent loads skills appropriate to its task and workspace, including any bundled skills. Use the skill paths above when automatic discovery is unavailable. Delegation briefs stay compact.

`lean-web` condenses four supplied standalone source skills (Vercel React best practices, Vercel composition patterns, Better Auth, Turborepo) and the 11 skill definitions/rule sets supplied in `skills-main (1).zip` (Node, Fastify, OAuth, TypeScript, ESLint, Node internals, documentation and specialized tooling); unrelated specialist guidance is conditional, not the default workflow. It is a task-focused paraphrase, not an exact upstream documentation bundle. API details should be checked against the installed versions. `lean-java` retains the Java guidance from v13, with overlapping web-specific rules now centralized in `lean-web`.

Relevant upstream web sources: [Vercel React](https://github.com/vercel-labs/agent-skills/blob/main/skills/react-best-practices/SKILL.md), [composition](https://github.com/vercel-labs/agent-skills/blob/main/skills/composition-patterns/SKILL.md), [Better Auth](https://github.com/better-auth/skills/blob/main/better-auth/best-practices/SKILL.md), [Turborepo](https://github.com/vercel/turborepo/blob/main/skills/turborepo/SKILL.md). The additional Node/web source files were provided in the uploaded `skills-main (1).zip`.

## Installation

Install `AGENTS.md` at the repository root (or in the platform's supported global instructions location). Start a **fresh session**, use the `build` primary where the host supports it, and check that `AGENTS.md` was actually loaded. Keep existing project instructions; merge rather than blindly overwriting local config.

### OpenCode v2

- Copy `agents/build.md` and `agents/general.md` to `.opencode/agents/` or `~/.config/opencode/agents/`. Set the default primary using the supplied `opencode.jsonc` or merge its `default_agent: "build"` into your existing config.
- The actual subagent is `general`; dispatch with a bounded `Role: CODER` instruction. Foreground means wait for its result; do not set `background: true`. A saved session may retain its prior primary.
- The bundled config uses V2 `permissions`/`agents`: denies `question`, `todowrite`, and `codesearch` actions when available; allows `build` to delegate only to `general`; prohibits recursive `general` delegation; and denies edit/delegation/websearch for the built-in `explore` role. Web fetching remains allowed. Apply as a merge into your own config; do not overwrite unrelated user permissions.
- V2 compaction keeps `auto: true` and `keep.tokens: 15000`; `compaction.prune` is legacy and ignored in V2. `lsp` and `doom_loop` are not current V2 Core permission actions, so those denials were not carried over. Denied tools only save tokens when they would otherwise be called. The additional V2 `tool_output` cap (300 lines/16,000 bytes per result) bounds unexpected dumps; keep full test logs on disk and inspect narrowed portions when needed. This reduces model-visible output only when the cap is reached; it is not a demonstrated billing reduction.

### Claude Code

- Copy `agents/build.md` and `agents/general.md` to `.claude/agents/` or `~/.claude/agents/`. Select the primary with `claude --agent build` or the equivalent agent setting.
- Ensure Claude receives shared `AGENTS.md`: add `@AGENTS.md` to an existing project `CLAUDE.md` if required by the installed Claude Code version. Do not replace an existing `CLAUDE.md` merely for Lean Agents.

### Codex

- `AGENTS.md` is the root policy. Install `agents/worker.toml` as `.codex/agents/worker.toml` or `~/.codex/agents/worker.toml`; this maps the logical CODER role to the `worker` subagent.
- Codex root remains the default ORCHESTRATOR through `AGENTS.md`; enable its native multi-agent feature before expecting delegation. No additional root prompt copy is needed.

### Command Code

- Command Code reads root `AGENTS.md`. Install `mods/lean-primary.ts` as a supported mod if you need to make the `build` primary prompt explicit; the mod loads `agents/build.md` relative to its own installation, so keep that layout.
- Its built-in `general` is **reserved and cannot be overridden** by a `.commandcode/agents/general.md` file. Assign `Role: CODER` and acceptance criteria in the actual `agent` tool handoff. Use `run_in_background: false` / foreground. No additional custom roles are required.

### Pi

- `extensions/lean-subagents.ts` provides a `subagent` tool with only `agent: general`. Keep `agents/general.md` relative to the extension. The tool waits for the child process to finish; it does not detach it. Ensure the primary session loads `AGENTS.md` and, if the host does not automatically select the `build` prompt, supply that role separately.

## Verification and cleanup

`general.md` and `worker.toml` carry the same CODER body in native formats. Source/test logs remain on disk; report real commands and exits. Full build integration checks should run only after independent workers finish editing.

**When upgrading from v10**, delete only Lean Agents-installed legacy specialist files if still present: `explore.md`, `explore.toml`, `lean-profiler.md`, `lean-profiler.toml`, and the no-op `foreground-subagents.js`. Simply extracting this new archive does not remove old files already installed elsewhere. This archive itself contains none of those components.

**Limits:** Prompt instructions are not runtime enforcement. The model may still skip delegation; assess with a fresh-session, two-task test and inspect actual first tool calls. No live agent run is implied by archive validation.

## ChatGPT

You can use .chatgpt prompt on ChatGPT as project source to generate .md deliverables to plan and give instructions to coding agents.
