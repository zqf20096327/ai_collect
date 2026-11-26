# ast-pack

**Fold your codebase. Unfold on demand.**

![ast-pack demo](assets/demo.gif)

`ast-pack` is a Rust CLI and [MCP](https://modelcontextprotocol.io) server. It packs a repository into a hard token budget. Anything it leaves out keeps a stable fold id, and an agent can ask for that body later with `unfold`. Nothing is deleted. It is only deferred.

## Install

```bash
cargo install --git https://github.com/oguzyl11/ast-pack.git
```

From a checkout:

```bash
cargo build --release
# ./target/release/ast-pack
```

The Homebrew formula in `homebrew/ast-pack.rb` builds the `main` branch (`brew install --HEAD`). The npm package in `npm/` runs a local `ast-pack` binary, or the path in `AST_PACK_BIN`.

## CLI

```text
ast-pack [PATH]
    --budget <N>             16000 or 16k. Omit it for an unlimited L1 pack.
    --focus <glob>...        Pin matching files to full source (L0).
    --diff [<ref>]           Symbols on changed lines prefer full source. Default ref: HEAD.
    --task "<text>"          Boost symbols whose name or docs match the text.
    --tokenizer o200k|cl100k Default: o200k.
    --format xml|markdown    Default: xml.
    --copy                   Copy to the clipboard. Prints to stdout if there is no clipboard.
    -o <file>                Write to a file.
    --stats                  Token totals, the L0–L4 histogram, and estimated input-cost savings on stderr.
    --explain                Why each symbol landed on its level.

ast-pack unfold [--root PATH] <id>...
ast-pack mcp
ast-pack setup [--remove] [--home DIR] [--project DIR]
```

`--focus` that does not fit in the budget is an error. A directory prefix matches that tree (`--focus src/auth` matches `src/auth.rs` and `src/auth/token.rs`).

```bash
ast-pack . --budget 16k --focus src/main.rs --format markdown
ast-pack --diff main --budget 32k --stats
ast-pack unfold "src/auth.rs#Session::validate"
ast-pack mcp
```

`setup` registers the MCP server in the project (`.cursor/mcp.json`, `.mcp.json`) and in the home directory for Cursor, Claude Code (`.claude.json`), Codex (`.codex/config.toml`), and Gemini (`.gemini/settings.json`). It also writes `.claude/skills/ast-pack/SKILL.md` and `.cursor/rules/ast-pack.mdc`. Those files tell an agent to call `pack` with `--budget` and `--task` before reading whole files, and to call `unfold` on a `⟨fold:...⟩` id only when the exact body is needed. Each edited file is copied aside once. `setup --remove` restores that copy, or deletes a file that did not exist before. `--home` and `--project` override the two directories. `--stats` prices the tokens a pack avoids at Claude Sonnet 4 ($3 / 1M input tokens) and GPT-4o ($2.50 / 1M).

## Levels

| Level | What you get |
| --- | --- |
| L0 | Full source |
| L1 | Signature, doc comment, and the full type (struct fields, interface members, enums, aliases) |
| L2 | Signature |
| L3 | Name |
| L4 | Omitted. The file stays in the tree |

A folded region looks like this:

```rust
pub fn validate(&self, token: &str) -> bool { /* ⟨fold:src/auth.rs#Session::validate⟩ 12 lines */ }
```

Fold ids are `<relative/path>#<symbol path>`. A second overload in the same file is `~2`, then `~3`, in source order. If the file changed after the fold was written, `unfold` returns the current body and says so on stderr.

## MCP

`ast-pack mcp` speaks JSON-RPC on stdin/stdout. It accepts a bare JSON line or a `Content-Length` frame.

| Tool | Input | Output |
| --- | --- | --- |
| `pack` | `path`, `budget`, optional `focus`, `diff`, `task`, `format` | Packed context, token count, fold ids |
| `unfold` | `ids` (or one `id`), optional `path` | Bodies with line numbers |
| `outline` | `path` | Symbols and the token cost of each full body |

```json
{"jsonrpc":"2.0","id":1,"method":"pack","params":{"path":".","budget":"16k"}}
```

## How a pack is built

1. Walk the tree, honoring `.gitignore`, and skip `target`, `node_modules`, and `.ast-pack-cache`.
2. Parse Rust, TypeScript, TSX, JavaScript, Python, Go, and Java with Tree-sitter. Results are cached by blake3 of the file bytes.
3. Build a symbol graph: calls, imports, containment, and type names. Ambiguous names get a fractional edge weight (`1 / n`).
4. Rank symbols with personalized PageRank. Seeds are fixed: `--focus` 1.0, `--diff` 0.8, `--task` 0.5.
5. Start at L4 and upgrade by score gained per extra token. Focused files stay at L0.
6. Render XML or Markdown, count the result with the real tokenizer (`o200k` or `cl100k`), and fold symbols back until the text fits.
7. Write `.ast-pack-cache/folds.json` so `unfold` can see whether a file changed.

The same input produces the same output bytes. Parse work is parallel.

## context-bench

`bench/` holds six local repositories (2 TypeScript, 2 Python, 1 Rust, 1 Go) and 25 questions each. The answer string lives in the function body, not in the signature. `cargo run --bin context-bench` rebuilds the corpus if it is missing and writes `bench/RESULTS.md`.

Coverage here means the answer string is in the context. It is not an LLM grade. The judge prompt for an optional model grader is `bench/judge_prompt.txt`.

Measured on this corpus with the `o200k` tokenizer (averages over the six repos):

| Method | Avg tokens | Avg extra unfold tokens | Coverage |
| --- | ---: | ---: | ---: |
| Full dump | 16003 | 0 | 100% |
| Comment-stripped compress | 12980 | 0 | 100% |
| Name map | 1482 | 0 | 0% |
| ast-pack 8k | 7562 | 0 | 44.0% |
| ast-pack 8k + unfold | 7562 | 538 | 100% |
| ast-pack 16k | 14706 | 0 | 92.7% |
| ast-pack 16k + unfold | 14706 | 79 | 100% |
| ast-pack 32k | 16003 | 0 | 100% |

On this corpus the full dump is 16,003 tokens, so a 32k budget is the whole repo. At 8k, unfold spends about 538 extra tokens and retrieves every answer the full dump retrieves. That is about half the tokens of the full dump, not 15%. The 15% line stays out of this README until a larger corpus measures it.

repomix, aider, codesurf, and any other context tool can add a row. Open a pull request with the command you ran and a script that reproduces the numbers. The pull request template has a checklist for that.

## Adding a language

Add the Tree-sitter grammar, a parser module under `src/parse/`, and a match arm in `src/parse/dispatch.rs`. The issue template "New Language Support" is the place to ask for one.

## Development

```bash
cargo fmt --check
cargo clippy --all-targets -- -D warnings
cargo test
```

The tests cover the six languages, overload ids, the hard budget (including a property test), focus that does not fit, task bias, diff focus, unfold after a file change, MCP, and `setup --remove`.

## License

MIT or Apache-2.0, at your option.
