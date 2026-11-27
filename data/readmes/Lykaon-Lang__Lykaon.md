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
(WAsm playground).

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

## Quick start (Windows)

1. Download `Lykaon-v0.2.0-windows-x64.zip` from
   [Releases](https://github.com/Lykaon-Lang/Lykaon/releases/latest).
2. Unzip it anywhere.
3. Double-click `install.bat`. It copies the tools to
   `%LOCALAPPDATA%\Lykaon`, adds them to `PATH`, registers the `.lykaon` file
   icon, and installs the VS Code extension.
4. Open a **new** terminal. Windows only refreshes `PATH` for windows opened
   after the install.

Put this in `hello.lykaon`:

```lykaon
Say Hello world.
```

Run it:

```
lykaonc-cli run hello.lykaon
```

```
Hello world
```

If the terminal says `lykaonc-cli is not recognized`, open a new terminal, or
use the full path:

```
"%LOCALAPPDATA%\Lykaon\lykaonc-cli.exe" run hello.lykaon
```

### Build a standalone executable

```
lykaonc-cli build fast hello.lykaon hello.exe
hello.exe
```

On Windows, double-click `hello.exe`; it waits for Enter before closing.

### VS Code

Open a `.lykaon` file and click **Run File** in the editor toolbar (top right),
or press `Ctrl+F5`. These are editor commands, not terminal commands.

## Install

### Windows

The zip is self-contained: unzip it and double-click `install.bat`. That is the
whole install.

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
- [File extensions](docs/extensions.md)

## What Lykaon can do

- **Language core**: sentences, blocks, `Changeable`/`Constant`/`Set`, `Say`,
  `Ask`, `If`/`Otherwise`, `Repeat`, `For each`, functions, records, enums,
  lists, maps, modules, tests and the ownership/borrow checker.
- **Native compiler**: Cranelift-based builds, optimizer, runtime library and
  standalone executables.
- **Servers and concurrency**: tasks, channels, timers, `Serve`, files,
  JSON/TOML, logging and networking.
- **Data tables**: `Load`, `Say rows/columns`, statistics, grouping,
  `For each row`, `Save as CSV`.
- **Charts**: `Plot` as dots/bars/line, SVG and deterministic PNG.
- **Models**: `Predict`, accuracy/error/importance, `Save model`,
  `Load model`, vectors.
- **Databases**: SQLite and PostgreSQL (MD5 auth), Add/Remove/Set/Load,
  transactions and `lykaon migrate`.
- **Security and limits**: encryption, memory/time limits and the native
  permission sandbox.
- **Tooling**: `lykaon lsp`, `lykaon doc`, `lykaon profile`, `lykaon outline`,
  JSON output modes and the 600-second fuzz harness.

## Status and limits

Lykaon is a **command-line / console** language for **Windows x64 and
Linux x64**. The current release is CLI-only; a GUI arrives in a later release.
The zip contains the CLI interpreter, the CLI compiler, the runtime library and
licenses.

- **Performance** is not yet a focus; correctness and byte-exact
  interpreter/native output come first.
- **macOS** is not a target.
- **WebAssembly**: the browser playground runs the interpreter compiled to
  wasm32; native Lykaon-to-wasm output and the WASI sandbox are deferred.
- **PostgreSQL**: MD5 auth and Add/Remove/Set/Load/transactions are verified
  against a real server; SCRAM-SHA-256 is not implemented yet.
- **Sandbox**: `lykaon run safely` and `--isolate` enforce files/hosts/env/
  processes/limits; Windows AppContainer and wasm32-wasi are deferred.
- **Tooling**: `lykaon debug`/DAP and `lykaon test coverage` are not finished.

Lykaon is **source-available, not open source**: free for personal use and for
organizations under USD 1,000,000 annual revenue. See
[`LICENSE.md`](LICENSE.md). Programs you write in Lykaon are yours to license
and sell.

## Contributing

Issues and pull requests are welcome. Open an issue with the
Where/Why/Fix text of any diagnostic.