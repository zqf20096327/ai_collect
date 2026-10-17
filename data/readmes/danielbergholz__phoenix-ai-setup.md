# Making a new Phoenix app AI-native

`mix phx.new` gives you a working Phoenix app and an `AGENTS.md` with framework guidance. Keep the useful rules, but organize them so an agent can find the detail its current task needs. A fresh worktree also needs dependencies, its own database, an available port, and a way to supply optional service credentials.

This guide closes those gaps in six steps. Shared instructions stay concise, task-specific skills load on demand, and `mix precommit` checks formatting, dependencies, translations, style, security findings, tests, and skill-mirror equality. Mirror equality does not establish that guidance is correct or current; that needs review and real tasks in each harness.

Documentation reviewed on **2026-09-29**. Line counts, generated defaults, and tool versions vary by release. This is a setup convention, not a guarantee of agent behavior.

**In a hurry?** [`PROMPT.md`](PROMPT.md) is the whole guide as one prompt. Paste it into a coding agent inside a fresh Phoenix app to perform the setup and report verification evidence, including checks it could not run. Starting files live in [`templates/`](templates/).

---

## 1. Pin the toolchain

Choose a supported Elixir/OTP pair compatible with Phoenix, dependencies, and your deployment platform. Check the [Elixir installation guidance](https://elixir-lang.org/install/) and [OTP releases](https://www.erlang.org/downloads), then pin exact stable versions available through asdf or mise. Prefer current security patches within the chosen release line; don't automatically upgrade the OTP major just because a newer one exists.

Create `.tool-versions` at the repo root (replace these placeholders with actual version-manager identifiers):

```
erlang <otp-version>
elixir <elixir-version>-otp-<otp-major>
```

Then set the supported Elixir requirement in `mix.exs`, for example when choosing Elixir 1.20:

```elixir
elixir: "~> 1.20",
```

The `elixir:` requirement declares compatibility; it does not pin the toolchain. `.tool-versions` is read by both asdf and mise, and CI can read it directly, for example with `erlef/setup-beam` using `version-file: .tool-versions` and `version-type: strict`. Verify the resolved versions locally and in CI.

After changing OTP major versions, remove this checkout's `_build`, then run `mix deps.get` and `mix compile --warnings-as-errors` to rebuild against the selected runtime.

---

## 2. Make `mix precommit` mean something

Phoenix generates a four-step alias. Replace it:

```elixir
precommit: [
  "compile --warnings-as-errors",
  "skills.check",
  "deps.unlock --unused",
  "format --check-formatted",
  "gettext.extract --check-up-to-date",
  "credo --strict",
  "sobelow",
  "test"
]
```

Add the two tools:

```elixir
{:credo, "~> 1.7", only: [:dev, :test], runtime: false},
{:sobelow, "~> 0.14", only: [:dev, :test], runtime: false}
```

Give agents checks they can run and evidence they can report. Put `mix precommit` in `AGENTS.md` as the final gate, alongside targeted tests and browser verification for UI changes. A passing gate supports completion; it cannot prove every requirement or security property. This follows [Anthropic's verification guidance](https://code.claude.com/docs/en/best-practices) and [OpenAI's version-control and review guidance](https://learn.chatgpt.com/docs/agent-approvals-security#version-control).

Keep Phoenix's `cli/0` setting `preferred_envs: [precommit: :test]` (or the equivalent for your Mix version). Run `mix format` explicitly to fix formatting before checking. CI uses the same gate without silently reformatting source. `deps.unlock --unused` can still change `mix.lock`; review any resulting diff.

Order is deliberate — cheap and structural checks first, `test` last, so failures surface in seconds rather than after a full suite run.

Depending on scaffold and dependency versions, you may encounter these findings:

| Failure | Fix |
|---|---|
| `gettext.extract --check-up-to-date` — `default.pot` doesn't exist | `mix gettext.extract --merge` once, then commit the generated `.pot` / `.po` files |
| `credo --strict` — `Phoenix.LiveView.JS` not alphabetically ordered in `<app>_web.ex` | Swap the two `alias` lines. Phoenix's own generated code trips its own check |
| `sobelow` — `Config.CSP: Missing Content-Security-Policy` | Add an application-appropriate CSP and verify it in the browser, or document an explicit project decision to defer it |

Generate a credo config with `mix credo.gen.config`. The default is sensible; the one change worth making is disabling `Design.AliasUsage`, which otherwise nags you to alias every module you reference twice.

`.sobelow-conf`:

```elixir
[
  verbose: false,
  private: false,
  skip: false,
  router: "lib/my_app_web/router.ex",
  exit: "Low",
  format: "txt",
  ignore: []
]
```

`exit: "Low"` fails on findings at Low confidence or above. Start with no suppressions. For CSP, configure `put_secure_browser_headers` in the browser pipeline, account for the app's scripts, styles, assets, and LiveView connections, and check both response headers and browser behavior. Nonces are needed only if your chosen policy permits necessary inline content that way. If the project explicitly defers CSP, record the reason and a real tracking issue or dated review point beside the narrowly scoped ignore. Passing Sobelow after suppression does not resolve the finding.

Until step 4 creates `skills.check`, verify the other tasks individually; the alias stops at the first failure and cannot reach Credo or Sobelow while that task is missing.

---

## 3. Split `AGENTS.md` into skills

This is the step that actually changes how agents behave.

Keep `AGENTS.md` focused on commands, architectural constraints, recurring pitfalls, and working agreements useful across tasks. A discoverable fact can still be worth including if agents repeatedly get it wrong. Move detailed procedures and references into focused skills under `.claude/skills/<name>/SKILL.md`, rather than deleting valuable guidance to meet a line count.

Three questions per block of text:

1. Is this a broadly useful command, constraint, or recurring pitfall? → `AGENTS.md`
2. Is it a detailed procedure or reference for one kind of work? → skill
3. Is it redundant, stale, or unused? → remove it after checking that useful guidance survives elsewhere

Applied to the stock `AGENTS.md`, five skills fall out cleanly:

| Skill | What moves into it |
|---|---|
| `elixir-gotchas` | language traps, Mix workflow, ExUnit mechanics |
| `phoenix-foundations` | Ecto, HEEx syntax, forms, router scoping |
| `phoenix-liveview` | streams, colocated JS hooks, `push_event`, LiveView tests |
| `liveview-interactions` | the client-vs-server decision for `phx-click` |
| `ui-and-assets` | layouts, components, Tailwind v4, bundling, design |

Around 60–100 lines is a useful starting target for this guide, not a vendor requirement or a pass/fail test. Preserve necessary rules and link to skills for the detail. [OpenAI](https://learn.chatgpt.com/docs/agent-configuration/agents-md) and [Anthropic](https://code.claude.com/docs/en/memory) document their own discovery and context limits.

### One shared instruction file

Codex discovers `AGENTS.md`. Claude Code v2.1.277+ can load it directly by default when no project `CLAUDE.md`, `.claude/CLAUDE.md`, or `CLAUDE.local.md` exists in the working directory or its ancestors. Personal `~/.claude/CLAUDE.md` and managed instructions do not disable this fallback. Some older or unsupported sessions still need a root `CLAUDE.md` containing `@AGENTS.md`. Use that import if you also need Claude-specific instructions; keep the shared content in one file. Confirm loaded files with Claude's `/context` and a fresh Codex session. See [Anthropic's exact fallback rules](https://code.claude.com/docs/en/memory#agentsmd).

### Skill frontmatter

```markdown
---
name: phoenix-liveview
description: Use when editing LiveViews, LiveComponents, streams, phx-hook, push_event, or Phoenix.LiveViewTest assertions. Covers LiveView mechanics; use ui-and-assets for visual styling alone.
---
```

Use `name` and `description` as the portable baseline. Write clear scope, exclusions, example situations, and useful symbols in the description; keyword lists do not guarantee invocation. Codex initially sees skill metadata and chooses whether to read the body. Current Claude Code also appends `when_to_use` to its description and supports `paths` for activation scope. Those are Claude extensions, not cross-harness guarantees. Keep essential routing information in `description`, and use valid YAML if you add harness-specific fields. See [OpenAI skills](https://learn.chatgpt.com/docs/build-skills) and [Anthropic frontmatter](https://code.claude.com/docs/en/skills#frontmatter-reference).

After mirroring in step 4, verify discovery, explicit invocation, and automatic selection in each harness you use. Try a relevant prompt (a LiveView stream change) and an unrelated prompt (a README spelling fix), and inspect which skills actually load. Review the moved rules against the original and repeat these checks when descriptions or workflows change. Report unavailable harness checks as unverified.

### Leave a stub, not a hole

Sections don't vanish from `AGENTS.md` — they shrink to the always-true rule plus a pointer:

> Wrap public, crawler-hit, user-invariant endpoints in `Cache.fetch/3` — **at the call site**. The **`caching` skill** has the full pattern, TTL conventions, and the `async: false` test setup.

The rule stays visible on every task; the detail loads on demand.

### Don't write skills for decisions you haven't made

The five above are a starting set; adapt them to the actual scaffold and work you do. Skills like `brand`, `auth-and-scope`, or `profile-privacy` encode product decisions. Add them when those decisions exist, rather than inventing rules during setup.

---

## 4. Mirror the skills, and guard the mirror

Not every agent harness reads `.claude/`. Expose the same tree at `.agents/skills`:

```sh
mkdir -p .agents && ln -s ../.claude/skills .agents/skills
```

Codex scans `.agents/skills`, while Claude Code scans `.claude/skills`. Both support symlinked skill folders. Git records the link as mode `120000`; checkout behavior depends on platform and Git symlink support. On Windows, enable supported symlink checkout or use generated copies with the equality guard below.

Can't diverge *by default*. The failure mode is someone replacing the symlink with real copies — a sync tool, a Windows checkout, an over-helpful script — after which the mirror rots silently and half your agents read stale rules. So verify it in `precommit`. [`templates/skills.check.ex`](templates/skills.check.ex) goes in `lib/mix/tasks/`; it resolves both trees, compares file contents, and fails with the exact drifted filenames.

**Test the guard before trusting it.** Replace the symlink with a copied tree, edit one file, and confirm `mix skills.check` fails and names that file. A guard nobody has seen fail is not a guard.

This guard compares file bytes only. Separately validate frontmatter in each harness, confirm discovery and invocation, and review whether the rules still fit the code. An equal mirror can contain equally stale or invalid instructions.

---

## 5. Claude Code harness config

Claude Code desktop offers worktree isolation for local Git sessions. A worktree checks out the selected commit; it does not automatically install dependencies, copy ignored credentials, or isolate external databases. The following setup makes bootstrapping explicit and supports parallel sessions.

**[`.claude/settings.json`](templates/settings.json)** registers a lightweight `SessionStart` hook with `matcher: "startup"`, a script path anchored to the project root, and a short timeout.

**[`.claude/hooks/session-start.sh`](templates/session-start.sh)** checks whether dependencies and build artifacts exist and reminds the session to bootstrap when needed. It leaves the selected Git state alone. Run `mix setup` explicitly after configuring worktree databases below. Phoenix's setup alias runs seeds; make seeds idempotent if you want repeatable setup, or run dependency, database creation/migration, and asset tasks separately without reseeding. Mark the hook executable with `chmod +x`. [Anthropic recommends keeping startup hooks fast](https://code.claude.com/docs/en/hooks#sessionstart).

**[`.claude/launch.json`](templates/launch.json)** declares the dev server with `autoPort: true`. Without it, your second worktree's server dies on `EADDRINUSE` the moment you try to verify anything, because the first is already holding 4000.

**`.gitignore`** gets `/.claude/worktrees/`. The desktop app creates a full checkout per worktree under that directory, so committing them would be enormous and meaningless. Ignore that directory only — never `.claude/` wholesale, since the settings, hooks, and skills are exactly what you want every developer to get.

### On `autoPort` and `PORT`

`autoPort` doesn't change what your server listens on by itself. Claude Desktop passes the selected port as `PORT`; the framework has to read it. Current Phoenix scaffolds do this in [`config/runtime.exs`](https://github.com/phoenixframework/phoenix/blob/main/installer/templates/phx_single/config/runtime.exs.eex), with no `port:` line needed in `config/dev.exs`. See [Claude's port configuration](https://code.claude.com/docs/en/desktop#port-conflicts).

Check your generated `config/runtime.exs`, which reads `PORT` in current Phoenix scaffolds. If yours does not, merge `http: [port: String.to_integer(System.get_env("PORT", "4000"))]` into the endpoint configuration in `runtime.exs`, preserving other options. Verify the behavior in your own app:

```sh
PORT=9999 mix phx.server   # should report http://localhost:9999
```

If it comes up on 4000, fix that before anything else — the whole parallel-session story depends on it.

### Isolate development and test databases

Different ports do not isolate migrations, seeds, or tests. For a fresh PostgreSQL scaffold, merge [`templates/runtime-worktrees.exs`](templates/runtime-worktrees.exs) into `config/runtime.exs`, replacing `my_app` / `MyApp`. It derives a stable database suffix from the checkout's absolute path and uses separate names for `:dev` and `:test`. `DEV_DATABASE_NAME` and `TEST_DATABASE_NAME` can override those defaults; set them to distinct per-worktree names. Production configuration is untouched. For SQLite, use distinct database file paths instead.

On an existing app, first inspect Repo settings, including `url:` and custom `init/2`; do not let a shared `DATABASE_URL` or adapter callback override the isolation. Changing names creates fresh databases; existing data stays in the old databases. Set up each checkout explicitly. Verify the effective Repo database with `mix run --no-start -e 'IO.puts(MyApp.Repo.config()[:database])'` and the same command with `MIX_ENV=test`. Repeat in a second worktree and confirm all four names differ. Remove disposable databases only after their worktrees are no longer needed.

---

## 6. Runtime secrets and worktrees

A fresh scaffold should boot with local adapters and mocks, without third-party credentials. When an integration needs credentials, read them from environment variables in `config/runtime.exs` in development and production. Phoenix documents [runtime environment configuration](https://phoenix.hexdocs.pm/deployment.html) as its normal secrets workflow.

For an integration your app actually uses, configure its real consumer at runtime. For example, if Resend is your chosen mail provider, merge this into `config/runtime.exs` after adapting the module names and installing the required adapter/client:

```elixir
if config_env() == :prod do
  config :my_app, MyApp.Mailer,
    adapter: Swoosh.Adapters.Resend,
    api_key: System.fetch_env!("RESEND_API_KEY")
else
  # Keep the generated local/test adapter unless explicitly testing delivery.
  if config_env() == :dev && System.get_env("RESEND_API_KEY") not in [nil, ""] do
    config :my_app, MyApp.Mailer,
      adapter: Swoosh.Adapters.Resend,
      api_key: System.fetch_env!("RESEND_API_KEY")
  end
end
```

Do not add an unused mail provider to a fresh app. Required production credentials should fail clearly when missing; optional development integrations can keep local defaults. Never require delivery credentials in ordinary unit tests. A template lives in [`templates/runtime-secrets.exs`](templates/runtime-secrets.exs); merge its optional example into your existing `runtime.exs`, rather than overwriting Phoenix's configuration. Configure Swoosh's API client as required by your chosen adapter.

Commit [`templates/env.example`](templates/env.example) as `.env.example`, documenting only variables the app uses with placeholders. A local `.env` file is an optional convenience; Phoenix does not load it automatically. Use an explicit environment loader or a secret manager wrapper for every launch path, including preview servers.

Add these patterns to the app's `.gitignore`:

```
/.env
/.env.*
!/.env.example
/config/*.secret.exs
```

Check ignore rules without opening real credentials:

```sh
git check-ignore -v --no-index .env             # matches
git check-ignore -q --no-index .env.example     # exits 1: not ignored
```

Inspect exit status for the template: an exception pattern can appear in verbose output even though the file is not ignored. The retained `*.secret.exs` rule protects any existing legacy local files; migrate their consumers before removing an old import, and preserve the files and values.

### Supply credentials without copying plaintext

For a shared setup, store development credentials in a secret manager and inject them into the app process. For example, put `op://...` references in a nonsecret `dev.env` and launch through [1Password CLI](https://www.1password.dev/cli/secrets-environment-variables):

```
op run --env-file=dev.env -- mix phx.server
```

Use the same wrapper for integration commands and the configured desktop preview command; don't assume a desktop launched from the Dock inherits shell exports. Claude Desktop's local environment editor is another option: its encrypted variables apply to local sessions and preview servers. These approaches provide credentials to processes that receive them; `.gitignore` only prevents accidental version-control inclusion. [Desktop environment documentation](https://code.claude.com/docs/en/desktop#local-sessions)

### Optional Claude worktree copying

Only if your project chooses local plaintext `.env` files, opt in to copying them with [`.worktreeinclude`](templates/worktreeinclude). Uncomment `.env` in that template and document the explicit loader. This is a Claude-specific feature, not a Git convention or a guarantee in Codex or other tools. It creates additional plaintext copies, and copying does not load the variables. Leave it disabled when using injected credentials.

**Verify runtime configuration without real credentials.** In a temporary fixture or disposable checkout, use a dummy value for an actual configured integration and assert that its consumer receives it, printing only pass/fail. Check the absent-variable path with a clean environment and confirm the development default remains usable; separately check that a required production variable fails clearly when absent. Never print real values, send test messages to a real provider, or overwrite/delete an existing `.env` or secret file for a probe.

---

## Checklist

- [ ] `.tool-versions` pins Erlang and Elixir; `mix.exs` matches; `_build` wiped after an OTP switch
- [ ] `mix precommit` runs in `:test`, checks formatting without changing source, and exits 0
- [ ] `.credo.exs` and `.sobelow-conf` exist, with written reasons for every ignore
- [ ] Shared instructions are concise and preserve useful commands, constraints, and pitfalls
- [ ] Claude and Codex instruction discovery verified, including any required `CLAUDE.md` import
- [ ] Skill frontmatter is valid and relevant/unrelated prompts were checked in each available harness
- [ ] `.agents/skills` exposes the same files; `mix skills.check` has been **seen to fail** on deliberate drift
- [ ] `.claude/settings.json`, `hooks/session-start.sh` (executable), `launch.json` present
- [ ] `/.claude/worktrees/` ignored, `.claude/` itself committed
- [ ] `PORT=9999 mix phx.server` serves on 9999
- [ ] Development and test databases differ across worktrees; repeated setup does not duplicate seed data
- [ ] Startup hook is fast; Git updates and full bootstrap are explicit
- [ ] Placeholder environment template committed; local values ignored; runtime consumers verified with dummy data
- [ ] Secret injection/loader works for shell and preview launches; `.worktreeinclude` copying is optional

---

## License

[MIT](LICENSE) — copy, adapt, share. Pull requests welcome, especially version-specific gotchas as Phoenix and Elixir move.
