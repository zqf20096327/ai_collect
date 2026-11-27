# Doctrina

Doctrina holds Claude Code rules and skills that are shared across repositories. None names a
particular project. The details that differ between repositories go in a **Project details**
section at the top of each rule, which each repository fills in when it adopts the rule. A skill
has no details of its own: it uses the values of the rules it relies on.

## Rules

- [`rules/writing.md`](rules/writing.md): spelling, grammar, numbers and units, technical writing
  for an audience from students to senior engineers, and a check to run before finishing. It
  covers all prose in a repository, including code comments and commit messages.
- [`rules/web-front-end.md`](rules/web-front-end.md): how to build a website or web app as a senior
  front-end developer, covering semantic HTML, CSS that meets the Web Content Accessibility
  Guidelines (WCAG) 2.2 at level AA, progressively enhanced JavaScript, languages and right-to-left
  layout, security and privacy, performance budgets, hosting limits, and the checks to run in the
  browser. It relies on `writing.md` for page text and YAML checks, so adopt both.
- [`rules/commits.md`](rules/commits.md): copy-ready commit messages, how much Git Claude may run,
  one change per commit, the Conventional Commits format, and pull request descriptions, with no
  attribution lines. It relies on `writing.md` for the text of each message, so adopt both.
- [`rules/dependencies.md`](rules/dependencies.md): how to build with no third-party code.
  Packages come only from the accounts a repository names as its own, checked by their owners on
  the registry and where their source lives. A third-party package is allowed only when it can't
  be avoided, because the platform, a closed format, a law or contract, or security requires it,
  and only after the user approves it. It covers what counts as a dependency, from the packages
  other packages bring in to continuous integration (CI) actions and copied code, the order to
  look for a solution in, what to tell the user when asking, updates, and the dependencies a
  repository already has. Set each language rule's **Dependency policy** to point to it. It
  relies on `writing.md`, so adopt both.
- [`rules/testing.md`](rules/testing.md): how to test as strictly as the code allows. It covers
  never weakening a test to make it pass, covering every line and branch, mutation testing to
  check that the tests catch changes, exact and deterministic tests, performance budgets that
  fail the build, security tests with hostile input and fuzzing, required checks in CI, and a
  diff check for new skips and removed assertions. It relies on `writing.md` and on the language
  rules' test commands, and on `dependencies.md` for test tools where that rule is adopted.
- [`rules/pair-programming.md`](rules/pair-programming.md): how to work with the user as a pair, in
  which you write the code or draft the material, and they review it and make the calls that are
  theirs. It covers reading before you write, saying the plan first, asking before the decisions
  that are the user's, pushing back with reasons, small steps checked one at a time, fixing causes
  instead of silencing tools, focused changes, explanations at the depth the user wants, a review of
  your own diff, and an honest report. The other rules add what their own work needs: the changes
  listed in each one's "Decisions that are the user's" section, and the checks and warnings in each
  language rule's "Making a change" section. It relies on `writing.md`, so adopt both.
- [`rules/rust.md`](rules/rust.md): how to write Rust as a senior engineer, covering type design,
  ownership, errors, text for users and its translations, hostile input, concurrency, `unsafe`,
  public APIs, tests, lints, and dependencies. Its documentation section covers doc comments and
  crate docs for docs.rs, a tested README for each crate on crates.io, and the docs.rs and crates.io
  metadata. It relies on `writing.md` for doc comments and error messages, so adopt both.
- [`rules/kotlin.md`](rules/kotlin.md): how to write Kotlin as a senior engineer, covering type
  design, null safety, errors, coroutines and Flow, text for users and its translations, hostile
  input, Java and platform interop, binary compatibility, KDoc and Dokka docs, module READMEs,
  tests, lints, and Gradle builds. It relies on `writing.md` for KDoc and error messages, so adopt
  both.
- [`rules/java.md`](rules/java.md): how to write Java as a senior engineer, covering the features
  each release adds and compiling with `--release`, records and sealed types, nulls, traps such as
  boxed `==` and `BigDecimal.equals`, exceptions and interrupts, logging, `java.time` and money,
  files and processes, virtual threads and other concurrency, text for users and its translations,
  untrusted input, including XML external entities and deserialization, the FFM API and JNI, public
  APIs and binary compatibility, Javadoc with snippets, READMEs and Maven Central metadata, JUnit
  tests, lints, and Gradle and Maven builds. It relies on `writing.md` for Javadoc and error
  messages, so adopt both.
- [`rules/android.md`](rules/android.md): how to build Android apps with Jetpack Compose as a senior
  mobile developer, covering app architecture, Compose state and performance, adaptive layouts,
  accessibility, translations, lifecycle and process death, background work, Room migrations,
  security and privacy, tests, and release builds. It relies on `kotlin.md` for the language and on
  `writing.md` for strings, so adopt all three.
- [`rules/kotlin-multiplatform.md`](rules/kotlin-multiplatform.md): how to share Kotlin code between
  Android and iOS as a senior mobile developer, covering what to share, source sets and targets,
  common-code limits, platform APIs, the API that Swift sees, coroutines across platforms, the Xcode
  toolchain, and tests on every target. Its Compose Multiplatform section covers shared UI: setup
  and entry points, shared resources, iOS behavior and look, native views, accessibility, iOS
  performance, previews, and UI tests. It relies on `kotlin.md`, `android.md`, `swift.md`, and
  `writing.md`, so adopt all five.
- [`rules/swift.md`](rules/swift.md): how to write Swift and SwiftUI as a senior mobile developer,
  covering type design, optionals and errors, memory, strict concurrency, SwiftUI state and
  identity, layout, accessibility, localization, persistence, security and privacy, Kotlin
  Multiplatform interop, tests, and release. It relies on `writing.md` for doc comments and strings,
  so adopt both.
- [`rules/flutter.md`](rules/flutter.md): how to build cross-platform mobile apps with Dart and
  Flutter as a senior mobile developer, covering Dart types, errors, and isolates, widgets and
  `build`, layout and performance, state management, navigation, platform adaptation, accessibility,
  localization, platform channels, data and security, tests, and release. It relies on `writing.md`,
  and on `android.md`, `kotlin.md`, and `swift.md` for native code, so adopt those that apply.
- [`rules/lua.md`](rules/lua.md): how to write Lua as a senior engineer, covering the differences
  between Lua 5.1, 5.4, 5.5, and LuaJIT, locals and modules, tables and strings, numbers, errors and
  cleanup, metatables, coroutines inside a host's event loop, performance, text for users and its
  translations, untrusted input, sandboxing code the program didn't ship, the C API and LuaJIT's
  FFI, LuaCATS or LDoc docs, rockspecs, tests on every supported version, and lints. It relies on
  `writing.md` for doc comments and error messages, so adopt both.
- [`rules/python.md`](rules/python.md): how to write Python as a senior engineer, covering the
  features each version adds, type hints and data design, traps such as mutable default arguments
  and late-binding closures, exceptions, files and encodings, logging, time and money, text for
  users and its translations through gettext, untrusted input, threads, processes, and `asyncio`,
  native code, public APIs, docstrings, READMEs and metadata for the Python Package Index (PyPI),
  tests with pytest, lints and type checking, and packaging with `pyproject.toml` and lock files. It
  relies on `writing.md` for docstrings and error messages, so adopt both.
- [`rules/typescript.md`](rules/typescript.md): how to write TypeScript and JavaScript as a senior
  engineer, on Node.js, in browsers, or both, covering runtimes and ES modules, Node.js running
  `.ts` files directly, strict compiler options, type design, traps such as the default sort order
  and the limits of `number`, errors and unhandled promises, logging, async code and cancellation,
  text for users and its translations through `Intl`, untrusted input and prototype pollution,
  native addons, public APIs and the `exports` field, doc comments, READMEs and metadata for npm,
  tests, linting with type information, and dependencies and install scripts. It relies on
  `writing.md` for doc comments and error messages, so adopt both. Code that runs in web pages also
  follows `web-front-end.md`.
- [`rules/roadmap-and-docs.md`](rules/roadmap-and-docs.md): how to plan and document a project
  in the style of Nadir's `docs/` folder, covering the numbered core documents, a roadmap of
  milestones and checkable tasks with a backlog of triggers, append-only decision records,
  specs for each part of the system, a feature list tied to the roadmap, and where status is
  reported. It includes a template for each document, and relies on `writing.md` for the text,
  so adopt both.
- [`rules/teaching-materials.md`](rules/teaching-materials.md): how to write courses, workbooks, and
  formal articles that educate readers, as a university professor. It covers when to use Markdown,
  Jupyter notebooks, or LaTeX; objectives-first course design; exercises, answer keys, and rubrics;
  each format's practices; accessible PDFs; citations; and integrity and student privacy. It relies
  on `writing.md`, so adopt both.

## Skills

- [`skills/build-roadmap-and-docs/`](skills/build-roadmap-and-docs/SKILL.md):
  `/build-roadmap-and-docs [description or piece]` builds the documents that
  `roadmap-and-docs.md` describes, from a description of the project, its code, or both: the
  numbered core documents, decision records, a spec for each part, a roadmap of milestones and
  checkable tasks with a backlog, the feature list, and the agent guide, update map, and status
  lines that point to them. It surveys the code and runs its checks first, so nothing is called
  built that isn't. It proposes the goals, milestones, and decisions for you to approve, drafts
  every decision as `Proposed` until you accept it, and records existing code as a first
  milestone whose tasks are ticked only when their tests pass. It ends with a check that every
  cited task and decision record exists and that dependencies run in order. Given one piece,
  such as `roadmap`, it builds only that piece and what it needs. It relies on
  `roadmap-and-docs.md`, `commits.md`, and `writing.md`, and uses `dependencies.md` and
  `testing.md` where they are adopted.
- [`skills/next-task/`](skills/next-task/SKILL.md): `/next-task [task-id]` works through the
  roadmap one task at a time. It picks the next unblocked task (or the one named), asks the
  questions and checks the decisions the task depends on, makes the smallest complete change,
  runs the task's checks, ticks the box only when they pass, updates the documents, and reports
  what ran and what didn't. It relies on `roadmap-and-docs.md`, `commits.md`, and `writing.md`,
  so adopt those first.
- [`skills/fix-doc-drift/`](skills/fix-doc-drift/SKILL.md): `/fix-doc-drift [scope]` finds
  statements in the documentation that no longer match the code, the tools, or the project's
  records, and corrects them. The scope is a path, an area, a Git range, or, when empty, every
  document. It decides which side is wrong before it edits, asks wherever a spec or decision may
  be right and the code wrong, leaves the records of the past alone, and suggests checks that
  would catch the same drift next time. It relies on `writing.md` and `commits.md`, and uses
  `roadmap-and-docs.md` where it is adopted.
- [`skills/draw-diagrams/`](skills/draw-diagrams/SKILL.md): `/draw-diagrams [file or view]`
  draws formal architecture diagrams of the project as Mermaid in Markdown, in `diagram/` or the
  folder `roadmap-and-docs.md` names: C4 views, UML class, component, and sequence diagrams,
  data-flow, state, data-model, and deployment diagrams. Built parts are solid and planned ones
  dashed with their task, and every file records the commit it was drawn from, so later runs
  rebuild only the diagrams whose sources changed. It relies on `roadmap-and-docs.md`,
  `commits.md`, and `writing.md`.
- [`skills/phase-gates/`](skills/phase-gates/SKILL.md): `/phase-gates [plan | phase ID]`
  clusters the roadmap's tasks into phases by dependency, risk, and deliverable, and gives each
  phase a gate of checkable criteria: integration, budgets, the full check, open work,
  decisions, documents, and risks. Given a phase, it evaluates that gate with evidence gathered
  in this session and records the result, and you confirm a pass. Empty, it shows every gate's
  state. It relies on `roadmap-and-docs.md`, `commits.md`, and `writing.md`.
- [`skills/sweep-code/`](skills/sweep-code/SKILL.md): `/sweep-code [scope]` scans the code for bugs
  and dead code: the bugs tools miss, from dropped errors to races, and unreachable code, unused
  declarations, files, and dependencies, and suppressions that hide nothing. It proves each finding
  with a failing test, a traced path, or a check of every way the code could be reached, and shows
  them all before it changes anything. It fixes only what you approve, one change at a time, with a
  regression test for each bug. It relies on `commits.md`, `writing.md`, and the language rules, and
  uses `roadmap-and-docs.md` and `pair-programming.md` where they are adopted.
- [`skills/security-sweep/`](skills/security-sweep/SKILL.md): `/security-sweep [scope]` finds and
  patches security vulnerabilities. It starts from a threat model of what an attacker would want and
  where data comes in, then checks the Git history for secrets, the dependencies for known
  vulnerabilities and supply-chain risks, the code against a checklist of weaknesses numbered as in
  the Common Weakness Enumeration (CWE), and the continuous integration (CI) workflows for script
  injection and unpinned actions. It proves each finding with a local test, never against a deployed
  system, never uses a secret it finds, and keeps findings private until you decide how to disclose
  them. It patches only what you approve, each with a regression test. It relies on `commits.md`,
  `writing.md`, and the language rules, and uses `roadmap-and-docs.md` and `pair-programming.md`
  where they are adopted.
- [`skills/simplify-code/`](skills/simplify-code/SKILL.md): `/simplify-code [scope]` finds code that
  is longer or more convoluted than its job requires, such as deep nesting, long functions, copied
  code, and layers that only forward calls. It simplifies the parts you approve without giving up
  any functionality: every input, output, error, side effect, edge case, option, supported platform,
  and performance budget stays as it was. It first checks why code is long, because much length is
  functionality, pins the current behavior with tests, and then makes one simplification at a time.
  It relies on `commits.md`, `writing.md`, and the language rules, and uses `roadmap-and-docs.md`
  and `pair-programming.md` where they are adopted.
- [`skills/build-course/`](skills/build-course/SKILL.md): `/build-course <description>` builds
  a whole course from a description such as "numerical methods for second-year engineers, 12
  weeks". It proposes a plan for you to approve, with the learning objectives, modules,
  assessments and their weights, policies, and a table that ties each objective to where it is
  taught and tested. Then it builds the syllabus, a Markdown reading and practice for each
  module, interactive Jupyter labs, LaTeX problem sets and exams whose answer keys come from the
  same source, graded notebooks through nbgrader, and a Jupyter Book website that leaves the keys
  out. It runs every notebook, compiles every document, and checks the website for leaked
  answers. Given an existing course's code, it continues from the plan's checklist. It relies on
  `teaching-materials.md`, `commits.md`, and `writing.md`.
- [`skills/build-language-packs/`](skills/build-language-packs/SKILL.md):
  `/build-language-packs [languages] [scope]` translates an app's user-facing text into Mandarin
  Chinese, Hindi, Spanish, Standard Arabic, French, Bengali, Portuguese, Indonesian, and Urdu, as
  one language pack each, in the app's own localization format. It first fixes source strings
  that can't be translated well, such as sentences built from pieces, and asks you to choose each
  language's variant and form of address. It writes every plural form each language needs, keeps
  placeholders and markup intact, lays out Arabic and Urdu right to left, and checks the keys,
  placeholders, plural forms, scripts, lengths, and fonts. Every translation stays a draft: each
  language gets a sheet with its glossary and a review list for a fluent reviewer. A later run
  translates only the strings that changed. It relies on `writing.md`, `commits.md`, and the
  platform rules, and uses `roadmap-and-docs.md` where it is adopted.
- [`skills/set-up-github/`](skills/set-up-github/SKILL.md): `/set-up-github [pieces]` writes
  the files GitHub reads, fitted to the project: a CodeQL code-scanning workflow with every action
  pinned to a commit, a Dependabot configuration for each package manager it finds, `SECURITY.md`,
  `CONTRIBUTING.md`, issue forms, a pull request template, and `CODEOWNERS`. It also writes a
  `.gitignore` from the adopted language rules, which keeps build output and secrets out and lock
  files and the Gradle wrapper in. It takes code owners, security contacts, and promises only from
  you, merges into existing files instead of replacing them, and lists the repository settings
  that only an administrator can change rather than changing them. It relies on `commits.md`,
  `writing.md`, and the language rules, and uses `roadmap-and-docs.md` and
  `teaching-materials.md` where they are adopted.

## Adopt a rule in a repository

These steps use `writing.md`; replace it with the rule you are adopting.

1. Create the repository's rules folder if it doesn't exist yet:

   ```bash
   mkdir -p path/to/repository/.claude/rules
   ```

2. Copy the rule into it:

   ```bash
   cp rules/writing.md path/to/repository/.claude/rules/writing.md
   ```

3. Open the copy and replace every `[FILL IN: …]` value under **Project details**.
4. Check that none are left. This command searches only the value lines, because the section's
   introduction mentions the placeholder too:

   ```bash
   grep -n '^- \*\*.*\[FILL IN' path/to/repository/.claude/rules/writing.md
   ```

   The command prints nothing when every value is filled in.

Claude Code reads the files in `.claude/rules/` on its own, starting with the next session:

- A rule without `paths` front matter, such as `writing.md`, applies to every session in that
  repository.
- A rule with `paths` front matter, such as `web-front-end.md` or `rust.md`, applies only when
  Claude works on files that match one of its patterns. Edit the list to fit the repository:
  add template files such as `**/*.liquid` or `**/*.njk`, and remove file types the repository
  doesn't use.

If a copy still has unfilled values, the rule tells Claude to infer them from the repository and
to tell you which ones are missing.

## Adopt a skill in a repository

These steps use `next-task`; replace it with the skill you are adopting. Adopt the rules the
skill relies on first.

1. Create the repository's skills folder if it doesn't exist yet:

   ```bash
   mkdir -p path/to/repository/.claude/skills
   ```

2. Copy the skill's folder into it:

   ```bash
   cp -r skills/next-task path/to/repository/.claude/skills/
   ```

Start the skill by typing `/next-task`, with a task ID if you want a particular task. Its front
matter sets `disable-model-invocation: true`, so Claude never starts it on its own.
