# ai-design-system

A coding-agent skill that documents when and how to use your UI components.
Agents use these Markdown contracts to choose components and build pages with your
design system. The skill adds contracts to your codebase and checks them against
the source files. Your components, styles and tools stay in the project.

- **Selection rules.** Contracts explain which component fits a task, how to compose
  it and when to choose an alternative.
- **Existing code.** Connect a system you already have, document locally added
  external components, or ask the agent to create reusable UI.
- **Drift checks.** Included Node.js scripts check contract structure, links,
  generated indexes and whether listed sources have changed since review.
- **Bounded changes.** System work can change CSS, markup and public design settings.
  Component internals and business logic remain project-owned.


1. [**Get started**](#get-started)<br />
2. [**Workflows**](#workflows)<br />
3. [**Project structure**](#project-structure)<br />
4. [**Migration**](#migration)<br />
5. [**Contract checks**](#contract-checks)<br />
6. [**Lefthook integration**](#lefthook-integration)<br />
7. [**Development**](#development)<br />
8. [**License**](#license)

## Get started

From your project's root, install the skill and select your coding agent:

```sh
npx skills add ymandrikov/ai-design-system --skill design-system
```

Or with pnpm:

```sh
pnpm dlx skills add ymandrikov/ai-design-system --skill design-system
```

Open your coding agent in that same project and ask:

```text
Use design-system setup to connect this project's design system.
```

Setup connects design sources through `DESIGN.md`, generates contract indexes and
adds a pointer in `AGENTS.md`. Provide a design brief, Figma designs or documented
rules. The skill cannot infer missing design intent from appearance alone.

If your existing UI has no contracts, setup offers to write them. You choose
whether to include that migration and run verification. In an empty project,
run `design-system craft` after setup to create the reusable UI you need.
See [setup details](skills/design-system/reference/setup.md).

## Workflows

Name a workflow or describe the result and let the agent choose.

To invoke the skill explicitly, replace `<task>` with a workflow name or your request:

- Claude Code: `/design-system <task>`
- Codex: `$design-system <task>`

| Workflow | Use it to |
| --- | --- |
| [`use`](skills/design-system/reference/use.md) | Build or change a product interface with existing public APIs and composition rules. |
| [`craft`](skills/design-system/reference/craft.md) | Create or maintain reusable UI, contracts, tokens and design rules. |

**Shared changes need explicit scope.** A page request permits product work and local
fallbacks. Changes to shared components or rules need an explicit request. If you
request both, the agent completes and checks the shared changes before using them
in the page.

Other procedures:

- [`discovery`](skills/design-system/reference/discovery.md) — recommend existing UI and tokens.
- [`improve`](skills/design-system/reference/improve.md) — survey system consistency and choose improvements.
- [`analyze`](skills/design-system/reference/analyze.md) — save reuse and extraction proposals.
- [`verify`](skills/design-system/reference/verify.md) — check against contracts and design sources.
- [`gaps`](skills/design-system/reference/gaps.md) — record or assess missing capabilities.
- [`triage`](skills/design-system/reference/triage.md) — review gaps and recommend next work.

Locally added external components, such as shadcn sources, need contracts and index
updates too. See [external-component adoption](skills/design-system/reference/craft.md#adopt-locally-added-external-components).

### Exceptions and system improvements

Record approved local exceptions and unmet needs in `design-system/gaps.md`.
Recording an exception does not authorise it or make it a shared rule.

Use `triage` to choose which gaps to address with `craft`. Once the shared UI
supports the missing behaviour, replace the local workarounds. Your project
defines its exception APIs and design lint rules.
See [exception handling](skills/design-system/reference/gaps.md#record-exceptions).

## Project structure

`DESIGN.md` connects design sources, rules and verification commands. Contracts
record each reusable entity's public API, intended use and composition rules;
generated indexes help agents find them.

```text
AGENTS.md                         # Points to DESIGN.md and the skill
DESIGN.md                         # Design sources and project rules
design-system/
  COMPONENTS.md                   # Generated indexes
  LAYOUTS.md
  PATTERNS.md
  components/button.md            # Contracts
  layouts/stack.md
  patterns/settings-page.md
```

Implementation and token files keep their existing paths. See the
[DESIGN.md template](skills/design-system/assets/DESIGN.md),
[contract formats](skills/design-system/reference/formats.md) and [glossary](CONTEXT.md).

## Migration

Use `design-system migrate` to document existing reusable UI across a selected area
or the whole codebase. Choose documentation only, adoption with local exceptions,
or adoption with design repairs. Migration saves progress so you can resume later.
See [migration modes and scope](skills/design-system/reference/migrate.md).

## Contract checks

The included Node.js scripts validate contract metadata, links, index membership
and source freshness. They do not check whether the UI behaves or looks correct.

Regenerate indexes after contract changes. Review changed sources before updating
their recorded hashes.

See [index generation commands](skills/design-system/assets/inventory.md),
[contract validation](skills/design-system/reference/contract.md#ordinary-audit) and
[source hash rules](skills/design-system/reference/formats.md#contract-frontmatter).

## Lefthook integration

In a connected consumer project, install [Lefthook](https://lefthook.dev/installation/node/):

```sh
npm install -D lefthook
```

Or with pnpm:

```sh
pnpm add -D lefthook
```

Add this command to your project's `lefthook.yml`, preserving existing hooks.
Replace `<design-system-directory>` with the installed skill's path. The checker
needs Node.js and Git.

```yaml
pre-commit:
  commands:
    design-contracts:
      run: node "<design-system-directory>/scripts/check-staged-contracts.mjs"
```

The hook checks added or changed contracts and contracts whose listed `sources`
have staged changes, including deletions and renames. It reads the Git index, so
unstaged edits cannot hide errors in the commit. If no contracts are affected,
it exits successfully without running the validator.

Changes to `DESIGN.md`, indexes, tests, examples or Markdown link targets alone do
not trigger checks. The hook does not validate indexes or follow source imports.

Install the hook in each clone; run it manually to check staged changes:

```sh
npx lefthook install
npx lefthook run pre-commit
```

Or with pnpm:

```sh
pnpm exec lefthook install
pnpm exec lefthook run pre-commit
```

Commit the configuration and dependency changes. If a source hash fails,
review the contract, update its hash and stage it with the sources. The hook does
not update hashes or stage files.

Add your project's design lint checks separately. Run required contract and index
checks in CI, since developers can skip local hooks.

## Development

Clone this repository and install dependencies with the pnpm version pinned in
[package.json](package.json):

```sh
git clone https://github.com/ymandrikov/ai-design-system.git
cd ai-design-system
pnpm install --frozen-lockfile
```

Commit dependency changes with `pnpm-lock.yaml`.

Run fixtures and scenarios only when explicitly chosen. `pnpm test` includes
fixture checks. To run tests or build the local demo:

```sh
pnpm test
pnpm run demo
python3 -m http.server 4173 --bind 127.0.0.1
```

Open the [settings demo](http://127.0.0.1:4173/fixtures/mini-ds/demo/settings.html).
It contains React and Web Component compositions and simulates submission locally
without persisting data.

[mini-ds](fixtures/mini-ds/) contains the working UI example.
[tie-ds](fixtures/tie-ds/) contains document-only contracts for selection cases.

The [scenario guide](scenarios/README.md) explains how to check agent decisions and
the files they produce in isolated copies. Fixture tests alone do not show whether
an agent chooses the right components or whether the UI works in a browser.

### Commit messages

This repository follows Conventional Commits: `type(scope): description`, with an
optional scope. For example: `feat: add a component` or `docs: clarify setup`.

## License

[MIT](LICENSE).
