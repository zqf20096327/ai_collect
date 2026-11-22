# Lykaon

**Lykaon is a programming language you read like plain English.**
Sentences end with a period, blocks are indented, and there are no quotes,
braces or semicolons. The compiler turns those sentences into a real native
executable.

[![CI](https://github.com/Lykaon-Lang/Lykaon/actions/workflows/ci.yml/badge.svg)](https://github.com/Lykaon-Lang/Lykaon/actions/workflows/ci.yml)

## A taste of Lykaon

Functions, lists and loops:

```lykaon
To double n give n times 2.

Nums is list of 1 and 2 and 3.
Say double 21.
For each n in Nums.
    Say n.
```

```
42
1
2
3
```

Records:

```lykaon
A person has name as text and age as whole number.
Maya is a person with name Maya and age 31.
Say name of Maya.
Say age of Maya.
```

```
Maya
31
```

Tasks and channels:

```lykaon
Bag is channel of whole number.
Start task producer.
    Send 1 to bag.
    Send 2 to bag.
Receive from bag.
Say it.
Receive from bag.
Say it.
```

```
1
2
```

**[Try it in your browser — no install](https://lykaon-lang.github.io/Lykaon/)**
(WAsm playground, v0.1 preview).

## Why Lykaon

- **Plain English sentences** — `Say total price.`, `If n is more than 3.`,
  `For each row in sales.`
- **A real compiler** — Cranelift-based native builds (`lykaonc-cli build`),
  with an optimizer and a runtime library.
- **Data, servers and AI in the language** — CSV tables, SQLite/PostgreSQL,
  HTTP/JSON, tasks/channels, classical ML models.
- **One binary** — build a standalone executable; no interpreter needed to run
  it.
- **Readable errors** — Where, Why and Fix on every diagnostic.

## Quick start

Run a program:

```
lykaon-cli run hello.lykaon
```

Build a standalone executable:

```
lykaonc-cli build fast hello.lykaon hello.exe
hello.exe
```

On Windows, double-click `hello.exe`; it waits for Enter before closing.

## Install

### Windows

Download the
[`Lykaon-v0.1.0-windows-x64.zip`](../../releases/tag/v0.1.0) asset, extract
it, and run `lykaon-cli.exe` / `lykaonc-cli.exe`. Add the folder to `PATH` to
run them by name.

### Linux

Install [Rust](https://rustup.rs) 1.85 or newer:

```
git clone https://github.com/Lykaon-Lang/Lykaon.git
cd Lykaon/Lykaon
cargo build --release -p lykaon-rt
cargo build --release -p lykaon
```

Binaries: `target/release/lykaon-cli` (interpreter) and
`target/release/lykaonc-cli` (compiler). The runtime library is built
separately so it stays TLS-free.

## Documentation

- [Language reference](docs/Lykaon_Language_Reference.md)
- [Syntax tour](docs/syntax.md)
- [CLI reference](docs/cli.md)
- [Standard library](docs/standard-library.md)

## What works today

- M1–M4 are complete: the language core, data and ownership, the native
  compiler, servers, concurrency, files, formats and networking.
- M5 is in progress: data tables, SVG charts, classical ML models,
  SQLite/PostgreSQL, encryption, memory/time limits, native permission
  sandbox, `lykaon lsp`, `lykaon doc`, `lykaon profile`, `lykaon outline`,
  `lykaon check --json`, `lykaon test --json`, `lykaon docs --compact`,
  `lykaon explain`, `lykaon run --trace-json`, `lykaon migrate`.

## Status and limits

Lykaon v0.1 is a **command-line / console** language for **Windows x64 and
Linux x64**. There is no GUI in v0.1; the release contains the CLI
interpreter, the CLI compiler, the runtime library and licenses.

- **Performance** is not yet a focus; correctness and byte-exact
  interpreter/native output come first.
- **macOS** is not a target in v0.1.
- **WebAssembly** output and the WASI sandbox are not finished yet.
- **Tooling** `lykaon debug`/DAP and `lykaon test coverage` are not finished.
- The full M5 plan and remaining items are tracked in the development
  repository; this public repo is the released CLI snapshot.

Lykaon is **source-available, not open source**: free for personal use and for
organizations under USD 1,000,000 annual revenue. See
[`LICENSE.md`](LICENSE.md). Programs you write in Lykaon are yours to license
and sell.

## Contributing

Issues and pull requests are welcome. Open an issue with the
Where/Why/Fix text of any diagnostic.