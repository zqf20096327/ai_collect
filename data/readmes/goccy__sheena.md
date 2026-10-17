<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="images/logo_dark_1024.png">
    <source media="(prefers-color-scheme: light)" srcset="images/logo_light_1024.png">
    <img src="images/logo_light_1024.png" alt="Sheena logo" width="240">
  </picture>
</p>

# Sheena

**A lightweight, in-process sandbox for safely executing the tool calls an AI
agent requests — on the same host as the agent.**

> *Sheena is the last wall between an AI agent's tool calls and your host.*

Sheena runs an agent's `bash` tool calls against an isolated, in-memory
filesystem with no access to the host: the shell language is real bash
(pipes, redirects, subshells, globbing, control flow), but every command is a Go
reimplementation dispatched from an allow-list — never a host binary — and every
filesystem, network, and resource access goes through a policy you configure. It
is far lighter than a container or microVM (no process to spawn, no image to
build), and its tool API is SDK-neutral, so it plugs into any Go AI SDK without
an adapter.

```go
sb, _ := sheena.New(sheena.Policy{
    Command: sheena.CommandPolicy{Allow: []sh.Command{sh.Grep}},
    FS:      fs.Mem().Seed(map[string]string{"/data/users.txt": "alice\nbob\ncarol\n"}),
})
r, _ := sb.ExecBash(context.Background(), "grep -c '' /data/users.txt")
fmt.Print(r.Stdout) // 3
```

## Why Sheena

- **Real bash, safe commands.** Bash semantics come from
  [`mvdan.cc/sh`](https://pkg.go.dev/mvdan.cc/sh/v3); the commands are Go
  reimplementations that never touch the host PATH. An agent that emits
  `bash -c "cat log | sort | uniq -c"` runs against your sandbox, not your OS.
- **Code interpreters, same guarantees.** Beyond bash, Sheena ships `python3` and
  `js` — a Code-Interpreter-style tool — that run an agent's Python or JavaScript
  under the *same* confinement as a shell command: no host filesystem, network, or
  subprocess access, and a real enforced memory cap. Running arbitrary Python or
  JS is as safe as running `grep`.
- **Deny-by-default.** No commands, no filesystem, no network until you opt in.
  Only the commands you list are even linked into the binary (dead-code
  elimination removes the rest).
- **In-process and lightweight.** A sandbox is a Go value. No daemon, no
  container, no cgo. Construct thousands of them; per-call overhead is measured
  in the benchmarks, not asserted.
- **Adapter-free tool API.** `Sandbox.Tools()` + `Sandbox.CallTool()` speak the
  SDK-neutral `{name, description, input_schema}` / `{stdout, stderr, exitCode}`
  shape every tool-calling SDK expects — usable directly with anthropic-sdk-go,
  openai-go, microsoft/agent-framework-go, and others.

## Install

```sh
go get github.com/goccy/sheena
```

Requires Go 1.25+.

## Core API

```go
type Policy struct {
    Command CommandPolicy // which commands run, their env and working directory
    FS      fs.FS         // the sandbox filesystem (nil = empty in-memory)
    Network *net.Access   // network policy (nil = deny all)
    Limits  Limits        // timeout, output/command-count/memory caps
}

sb, err := sheena.New(policy)

// Run bash directly:
res, err := sb.ExecBash(ctx, "sort data.csv | head")

// Or drive it as an LLM tool (SDK-neutral):
for _, tool := range sb.Tools() { /* advertise tool.Name / tool.InputSchema */ }
res, err := sb.CallTool(ctx, "bash", json.RawMessage(`{"command":"echo hi"}`))
```

`Result` is `{Stdout, Stderr string; ExitCode int; IsError bool}`. A non-zero
exit or an enforced limit sets `IsError` so the model can react; a Go `error` is
returned only for dispatch failures.

## Filesystem policy

The filesystem is any `fs.FS`, built with a small builder:

```go
fs.Mem().Seed(map[string]string{"/a.txt": "hi"}) // in-memory, pre-populated
fs.Mem().MaxBytes(1<<20).MaxFileBytes(64<<10)     // byte caps
fs.Mem().Refuse("*.pem", ".git/**")               // deny access (permission error)
fs.Mem().Hide("secret.conf")                      // make paths appear absent (incl. in ls)

fs.ReadOnlyMount("/host/dir")   // read the host, refuse writes
fs.ReadWriteMount("/host/dir")  // read/write the host, confined to the dir
fs.OverlayMount("/host/dir")    // copy-on-write: reads fall through, writes stay in memory
```

Host mounts are confined with `os.Root`, so no operation can escape the mount —
not through `..`, and not through a symlink whose target lies outside it.

## Network policy

Network is deny-by-default. A `NetworkPolicy` is a list of per-destination allow
rules plus deny rules: a matching **deny always wins**, otherwise the first
matching allow rule governs the request, and anything unmatched is denied. Each
`net.Allow(host)` is one destination, refined with a port/method restriction, an
SSRF (private-address) guard, cross-host redirect blocking, header injection, and
a response-body cap. `net.Deny(host)` blocks a destination (optionally narrowed
by `.Port`/`.Method`) and overrides the allow rules — so you can open a broad
range and carve exceptions out of it:

```go
sheena.NetworkPolicy{
    Allow: []*net.AllowPolicy{
        net.Allow("api.example.com").Port(443).Method("GET", "POST").
            Header("Authorization", "Bearer "+token). // secret never in argv
            MaxResponseBytes(1 << 20),
        net.Allow("*.cdn.example.com").Port(443),      // read-only CDN, any subdomain
    },
    Deny: []*net.DenyPolicy{
        net.Deny("internal.api.example.com"),          // carve-out; deny wins
    },
}
```

Host patterns are `example.com` (exact), `*.example.com` (any subdomain, not the
apex), `example.*` (one trailing label), or `*` / `net.AllowAll()` (any host),
matched case-insensitively.

## Limits

```go
sheena.Limits{
    Timeout:         10 * time.Second, // wall-clock per call
    MaxCommandCount: 100,              // fork-bomb / runaway-loop guard
    MaxOutputBytes:  1 << 20,          // combined stdout+stderr cap
    MaxMemoryBytes:  256 << 20,        // hard cap for the python/js interpreters
}
```

## Commands

Core commands (stdlib-only, in the `sh` package, enabled via `sh.Core()` or
listed individually):

`cat`, `ls`, `mkdir`, `rm`, `cp`, `mv`, `head`, `tail`, `wc`, `grep`, `find`,
`sort`, `cut`, `tr`, `uniq`, `rev`, `tac`, `nl`, `seq`, `tee`, `base64`,
`basename`, `dirname`, `sed`, `diff`, `csv`, `curl`, `md5sum`, `sha1sum`,
`sha256sum`, `gzip`, `gunzip`, `zcat`, `tar`.

Library-backed commands live in their own sub-packages, so the heavy dependency
is compiled and linked **only** when you reference it:

| Command | Import | Backing |
|---|---|---|
| `awk` | `sh/awk` (`awk.Awk`) | goawk |
| `jq` | `sh/jq` (`jq.Jq`) | gojq |
| `yq` | `sh/yq` (`yq.Yq`) | goccy/go-yaml |
| `sqlite` | `sh/sqlite` (`sqlite.Sqlite`) | modernc.org/sqlite (cgo-free) |
| `htmlmd` | `sh/htmlmd` (`htmlmd.HTMLToMarkdown`) | html-to-markdown |
| `python3` | `sh/python` (`python.Python`) | goccy/go-python |
| `js` | `sh/js` (`js.JS`) | goccy/go-spidermonkey |

```go
import "github.com/goccy/sheena/sh/jq"

sb, _ := sheena.New(sheena.Policy{
    Command: sheena.CommandPolicy{Allow: append(sh.Core(), jq.Jq)},
})
```

The `python3` and `js` interpreters are pure Go (no cgo) and run in-process:
they have no file/network/subprocess access to the host and honor
`MaxMemoryBytes` as a real, enforced memory ceiling.

## Custom tools

A user-defined command implements `sh.Command` (or wraps a func with
`sh.NewCommandFunc`) and runs under the same policy as the built-ins — its
`ExecContext` exposes only the policy-bound filesystem, network, and streams:

```go
greet := sh.NewCommandFunc("greet", func(ec *sh.ExecContext) error {
    fmt.Fprintf(ec.Stdout, "hello, %s\n", ec.Args[1])
    return nil
})
sb, _ := sheena.New(sheena.Policy{Command: sheena.CommandPolicy{Allow: []sh.Command{greet}}})
```

For tools you drive outside the shell, `sb.Resources()` hands out the same
policy-bound handles — `FS()`, `HTTPClient()`, `Dialer()`, `Context()` — so code
Sheena did not write still runs under the sandbox's confinement.

## SDK integration

`Tools()` / `CallTool()` are SDK-neutral. A worked example wiring Sheena into
[microsoft/agent-framework-go](https://github.com/microsoft/agent-framework-go)
lives in [`examples/agentframework`](examples/agentframework) (its own module, so
the SDK dependency never enters Sheena's own dependency graph).

## Security model

Sheena safely executes the tool calls an agent *requests*: the shell commands are
Go reimplementations that never spawn a host process or read the host PATH, the
filesystem is confined (in-memory by default; host mounts are `os.Root`-guarded),
the network is deny-by-default with an SSRF guard, and untrusted *scripts* run in
the sandboxed `python3`/`js` interpreters with real memory caps. It is not a boundary for running
untrusted *native* code in-process — for that, run it as a `js`/`python3` script
or use a hardware-isolated sandbox. The guarantees are asserted as executable
tests (`security_test.go`) and checked against real coreutils behavior
(`internal/difftest`).

## Development

`make test` (race), `make cover` (≥90% per package), `make lint`, and
`make bench` must pass. See [DESIGN.md](DESIGN.md) for the full design and
[AGENTS.md](AGENTS.md) for contributor/agent guidelines.

## License

MIT
