<p align="center">
  <img src="assets/banner.png" alt="ratatui-skill: terminal UIs that work, look deliberate, and ship no filler">
</p>

<p align="center">
  <a href="https://github.com/programmersd21/ratatui-skill/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/programmersd21/ratatui-skill/ci.yml?branch=main&style=for-the-badge&label=CI&labelColor=313244&color=a6e3a1" alt="CI status"></a>
  <img src="https://img.shields.io/badge/ratatui-0.30.2-cba6f7?style=for-the-badge&logo=ratatui&logoColor=ffffff&labelColor=313244" alt="ratatui 0.30.2">
  <img src="https://img.shields.io/badge/rust-1.88%2B-f38ba8?style=for-the-badge&logo=rust&logoColor=ffffff&labelColor=313244" alt="Rust 1.88+">
  <img src="https://img.shields.io/badge/license-MIT-f9e2af?style=for-the-badge&logo=github&logoColor=ffffff&labelColor=313244" alt="MIT license">
  <img src="https://img.shields.io/badge/AI--assisted-yes-89b4fa?style=for-the-badge&logo=github&logoColor=ffffff&labelColor=313244" alt="AI-assisted: yes">
  <a href="https://github.com/sponsors/programmersd21"><img src="https://img.shields.io/github/sponsors/programmersd21?style=for-the-badge&label=sponsors&labelColor=313244&color=f5c2e7" alt="GitHub sponsors"></a>
</p>

<h3 align="center">Make your AI assistant write Ratatui apps that actually work.</h3>

<p align="center">
  Current APIs. A deliberate design. Tested code. No filler.
</p>

<p align="center">
  <a href="#quick-start">Quick start</a> ·
  <a href="#what-changes">What changes</a> ·
  <a href="#how-it-works">How it works</a> ·
  <a href="#demo">Demo</a> ·
  <a href="#faq">FAQ</a> ·
  <a href="#sponsor">Sponsor</a>
</p>

---

<p align="center">
  <img
    src="assets/skill-workflow.svg"
    alt="ratatui skill workflow"
    width="900"
  />
</p>

AI assistants write ratatui from memory. They reach for old APIs and wrong crate versions, then ship a UI that looks generated: neon defaults, decorative panels, keys that do nothing.

**ratatui-skill** replaces that with a fixed process and a tested template. The assistant looks up what is current, writes a design brief before any code (new apps only), builds from a working codebase, and proves the result before it says "done".

## Quick start

1. Copy the skill into your assistant's skills directory. For Claude Code:

   ```bash
   mkdir -p ~/.claude/skills && cp -r skills/ratatui ~/.claude/skills/   # all projects
   mkdir -p .claude/skills && cp -r skills/ratatui .claude/skills/         # one project
   ```

2. Ask for a terminal UI:

   ```text
   Use the ratatui skill. Build a simple TUI in Rust: a todo list. Add items,
   mark them done, delete them, and save to a file so they're still there next time.
   ```

3. Watch it research versions, write a brief, build, and run its own checks.

Assistants that read `AGENTS.md` instead of loading skills can use the one at the repo root. It carries the same process in short form and points at the skill files.

## What changes

| Without the skill | With it |
|---|---|
| Versions and APIs written from memory | Newest stable versions looked up and quoted, release notes read, uncertain calls compiled |
| Design is whatever comes to mind first | A written brief: layout, one accent color, density, keys, every empty, error and too-small state |
| Decorative panels, fake data, dead keys | Everything visible works |
| One long `main.rs` | State with no terminal types, rendering with no side effects, one key table |
| "Done" with nothing run | fmt, clippy, tests, screen dumps, a real pseudo-terminal run, and a slop scan |
| Silent about what was skipped | A report that names anything it could not check |

## How it works

<details open>
<summary><b>Five steps, in order</b></summary>

1. **Research.** Look up the newest stable version, minimum Rust version, and (when given a manifest) the version resolved by the project of every crate, read the release notes, confirm widget crates match the ratatui version, and compile anything uncertain.
2. **Design brief.** Before any code: layout archetype, one accent color, density, keys, and what each empty or failed state shows, justified from the app's data.
3. **Build** from a tested template with a strict split: state with no terminal types, rendering with no side effects, and one key table that drives input, footer hints and help.
4. **Verify.** `cargo fmt --check`, clippy with warnings denied, tests, text dumps of the screen at several sizes, a run in a real pseudo-terminal, and a slop scan.
5. **Report honestly,** including anything it could not check.

</details>

<details open>
<summary><b>The rules it enforces</b></summary>

- Everything visible works. No fake data, decorative panels or dead keys.
- One key table drives input, footer hints and the `?` help, so a documented key always works.
- Text is measured with `unicode-width`, untrusted text is sanitized, only visible rows are drawn.
- Colors by role in one file, 16 ANSI colors by default, `NO_COLOR` respected, no forced background, no emoji.
- No `.unwrap()` outside tests, no swallowed errors, no TODOs, comments say why.
- Destructive actions confirm. Slow work never blocks the draw loop.

</details>

## Demo

The skill was used to build `todo/`, a persistent todo list. It is a header and list of tasks: `a` adds one, `Space` marks it done, `d` then `y` deletes it, and every change is written to a plain text file on disk. The screenshot shows the opt-in Catppuccin Mocha theme.

<p align="center">
  <img src="assets/demo.png" alt="todo list in the Catppuccin Mocha theme">
</p>

```bash
cd todo
TODO_THEME=catppuccin cargo run --bin todo
```

The default uses the 16 ANSI colors from your terminal palette. `NO_COLOR` renders monochrome. Source, keys and the file format are in [`todo/README.md`](todo/README.md).

## What's inside

```text
AGENTS.md                      the process in short form, for agents without skill support
assets/                        banner, demo, faq and sponsor images
docs/                          version-aware distribution proposal
evals/                         10 evaluation tasks, harness, scoring rubric, results
skills/ratatui/
  SKILL.md                     the process
  references/
    research-checklist.md      finding current versions and APIs; pitfalls found in practice
    ux-principles.md           layouts, keys, color, responsiveness
    slop-tells.md              what reads as generated, with before and after
  scripts/
    crate-versions.sh          newest stable version and MSRV via cargo info
    lint-slop.sh               mechanical slop scanner; exit status gates CI
    pty-smoke.py               run a TUI in a pseudo-terminal and check it behaves
  templates/dirview/           a complete ratatui 0.30 directory browser
todo/                          the demo todo app built with the skill
.github/                       issue and PR templates, sponsors, CI for both crates
```

### The template

`dirview` is a working program, not a sketch: list and preview panes, filtering, sorting, hidden files, a generated help overlay, empty and error states, a too-small message, `NO_COLOR`, and wide-character-safe layout. It has unit tests for state and keys, headless render tests, and passes clippy with warnings denied.

```bash
cd skills/ratatui/templates/dirview
cargo run -- .
```

## FAQ

<p align="center">
  <img src="assets/faq.png" alt="Frequently asked questions about ratatui-skill">
</p>

<p align="center">
  <a href="#compatibility"><b>Compatibility</b></a> ·
  <a href="#versions"><b>Versions</b></a> ·
  <a href="#slop-scan"><b>Slop scan</b></a> ·
  <a href="#ai-written"><b>AI-written?</b></a>
</p>

---

### Compatibility

<details>
<summary><b>Does it only work with Claude Code?</b></summary>
<br>

**No. Any assistant that can run commands works.**

The skill format is read by assistants that support skills, and anything that
reads `AGENTS.md` can use the short version at the repo root. The scripts and
template are plain shell, Python and Rust.

</details>

### Versions

<details>
<summary><b>Will it always pick the newest ratatui?</b></summary>
<br>

**It looks the version up every time instead of trusting the docs.**

The versions in this repo are what the template was tested with, ratatui 0.30.2
on its minimum supported Rust version, 1.88. They are not a promise about what is newest when you read this. The skill
tells the assistant to:

1. Run `crate-versions.sh` for each dependency.
2. Read the release notes for the version it returns.
3. Compile any API it is unsure about before using it.

</details>

### Slop scan

<details>
<summary><b>Why a "slop scan"?</b></summary>
<br>

**Generated UIs are recognizable, so the scanner fails CI on the mechanical tells.**

Emoji icons, neon gradients, placeholder rows and comments that narrate the code
are checked by [`lint-slop.sh`](skills/ratatui/scripts/lint-slop.sh). The rest are
judgment calls listed in
[`references/slop-tells.md`](skills/ratatui/references/slop-tells.md).

</details>

### AI-written?

<details>
<summary><b>Is the code AI-written?</b></summary>
<br>

**Yes, with AI assistance, and verified in CI.**

Every template file is compiled and tested, and the process is written down so
you can check the result yourself.

</details>

---

<p align="center">
  Still stuck? <a href="https://github.com/programmersd21/ratatui-skill/issues/new/choose">Open an issue</a> or <a href="https://github.com/programmersd21/ratatui-skill/discussions">ask in Discussions</a>.
</p>

## Provenance

The tells and principles come from public discussions of AI-generated projects and from lazygit's published design principles. `references/` marks where a rule is this project's own judgment. The template was built and tested with ratatui 0.30.2 at Rust 1.88. Versions in the docs are examples; the skill tells the assistant to look them up again.

## Contributing

Issues and pull requests are welcome. Good first contributions: a pitfall you hit with a ratatui release, a slop tell the scanner misses, or a second template (an async dashboard is the most requested gap). Run the checks before opening a PR:

```bash
cd skills/ratatui/templates/dirview && cargo fmt --check && cargo clippy --all-targets -- -D warnings && cargo test
cd todo && cargo fmt --check && cargo clippy --all-targets -- -D warnings && cargo test
python3 skills/ratatui/scripts/pty-smoke.py target/debug/<binary>
skills/ratatui/scripts/lint-slop.sh .
```

If this saved you time, a star helps other people find it.

## Sponsor

<p align="center">
  <a href="https://github.com/sponsors/programmersd21">
    <img src="assets/sponsor.png" alt="Sponsor @programmersd21 on GitHub: click here to sponsor">
  </a>
</p>


## License

[MIT](LICENSE)
