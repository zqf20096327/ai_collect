# Aegis

[![Tests](https://github.com/RRFDunn/aegis-lang/actions/workflows/tests.yml/badge.svg)](https://github.com/RRFDunn/aegis-lang/actions/workflows/tests.yml)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

A security-by-construction programming language for AI agents. Aegis transpiles `.aegis` files to Python with **runtime security enforcement** — taint tracking, capability restrictions, auditable execution, and contract verification are built into the language, not bolted on.

**Zero runtime dependencies.** Python 3.11+ stdlib only.

## Installation

```bash
pip install aegis-lang
```

Or install from source:

```bash
git clone https://github.com/RRFDunn/aegis-lang.git
cd aegis-lang
pip install -e .
```

## Quick Start

```bash
aegis run examples/hello.aegis          # Run an Aegis program
aegis check examples/taint_demo.aegis   # Static security analysis
aegis compile examples/hello.aegis      # View transpiled Python output
aegis repl                              # Interactive REPL
```

## Example

```aegis
@capabilities(allow: [network.https], deny: [filesystem])
module SecureAPI:

    @audit(redact: ["token"])
    @intent("Authenticate user against the database")
    @contract(pre: len(username) > 0, post: result is not None)
    func authenticate(username: tainted[str], token: tainted[str]) -> bool:
        let clean_user = sanitize(username, context=sql)
        let clean_token = sanitize(token, context=sql)
        return validate(clean_user, clean_token)
```

This enforces at runtime:
- **Taint tracking** — `username` and `token` cannot be used in SQL/HTML/shell without `sanitize()`
- **Capabilities** — `SecureAPI` can only use HTTPS, never touch the filesystem
- **Contracts** — `username` must be non-empty; return value must not be None
- **Audit trail** — every call is logged with `token` redacted from the audit record
- **Sandbox** — `eval`, `exec`, `__import__` are always blocked

## Security Features

| Feature | Syntax | Runtime Effect |
|---------|--------|----------------|
| Taint tracking | `tainted[str]`, `sanitize(val, context=sql)` | `TaintError` if tainted value reaches a sink |
| Capabilities | `@capabilities(allow: [...], deny: [...])` | `CapabilityError` for unauthorized operations |
| Contracts | `@contract(pre: ..., post: ...)` | `ContractError` on violation |
| Custom sanitizers | `@sanitizer("context")` | Register domain-specific sanitization |
| Banned operations | Always active | `eval`, `exec`, `__import__` blocked |
| Audit trail | `@audit(redact: ["password"])` | Hash-chained event ledger |
| Formal verification | `aegis verify-contracts` | Z3 SMT solver checks contract satisfiability |

## AI Agent Constructs

Aegis has first-class constructs for building safe AI agents:

```aegis
# Tool invocation with safety guarantees
tool_call search(query: str) -> list:
    provider: "google"
    timeout: 30s
    retry: 3
    fallback: return []

# Structured multi-step plans with rollback
plan deploy(version: str):
    intent: "Deploy application safely"
    require_approval: True

    step backup:
        let snapshot = create_backup()
        verify snapshot is not None
        rollback: restore_backup(snapshot)

    step activate:
        switch_traffic(version)

# Auditable structured reasoning
reason "Classify request priority":
    let score = analyze(request)
    if score > 80:
        conclude "critical"
    else:
        conclude "normal"

# Cost-bounded operations
budget api_costs:
    max_total: 10.0
    alert_at: 8.0
```

Also: `human_input`, `memory_access` (key-value and semantic), `delegate`, `reflect`, `verify`, duration literals (`30s`, `5m`, `24h`), and full `async`/`await` support.

## EU AI Act Compliance

Built-in compliance tooling for the EU AI Act (effective August 2026):

```bash
aegis compliance myagent.aegis          # Compliance gap analysis
aegis compliance myagent.aegis --json   # Machine-readable report
aegis run myagent.aegis --strict-compliance --audit-store sqlite:audit.db
```

The `@risk_level("high")` decorator triggers automatic audit injection and compliance checks against Articles 9-15.

## CLI Commands

| Command | Description |
|---------|-------------|
| `aegis run <file>` | Transpile and execute |
| `aegis compile <file> [-o out.py]` | Transpile to Python |
| `aegis check <file>` | Static security analysis |
| `aegis audit <file>` | Security audit report with risk score |
| `aegis audit show <file>` | Display runtime audit trail |
| `aegis audit verify <file>` | Verify audit hash chain integrity |
| `aegis audit export <file>` | Export audit trail as JSON |
| `aegis verify-contracts <file>` | Z3 formal verification of contracts |
| `aegis compliance <file>` | EU AI Act compliance report |
| `aegis watch <dir>` | Auto-check/compile/run on changes |
| `aegis repl` | Interactive REPL |
| `aegis lsp` | Start LSP server (editor integration) |
| `aegis init [dir]` | Scaffold new project with `aegis.toml` |
| `aegis install` | Install dependencies from `aegis.toml` |
| `aegis build [-o dir]` | Compile all `.aegis` files to Python |
| `aegis serve <file>` | Serve agent as A2A HTTP endpoint |
| `aegis agent-card <file>` | Generate A2A Agent Card |
| `aegis seal` | Generate runtime integrity manifest |
| `aegis fuzz <file>` | Fuzz-test sanitizers |
| `aegis prove <file>` | Capability reachability proofs |

Most commands support `--json` for machine-readable output.

## Project Structure

```
aegis-lang/
├── aegis_cli.py              # CLI entry point (20+ commands)
├── aegis/
│   ├── tokens.py             # Token types and keywords
│   ├── ast_nodes.py          # ~25 AST node dataclasses
│   ├── lexer.py              # Tokenizer with INDENT/DEDENT
│   ├── parser.py             # Recursive descent parser
│   ├── analyzer.py           # Multi-pass static security analysis
│   ├── transpiler.py         # AST to Python code generation
│   ├── resolver.py           # Module loading and caching
│   ├── compliance.py         # EU AI Act compliance checker
│   ├── smt.py                # Z3-based contract verification
│   ├── lsp/                  # Language Server Protocol
│   ├── package.py            # Package/dependency management
│   └── runtime/
│       ├── taint.py          # Tainted[T], sanitize(), TaintProvenance
│       ├── capabilities.py   # Capability enforcement with inheritance
│       ├── contracts.py      # @contract, @intent, @risk_level
│       ├── audit.py          # Hash-chained event ledger
│       ├── sandbox.py        # Restricted builtins namespace
│       ├── agent.py          # Agent runtime (tools, plans, memory, delegation)
│       ├── a2a.py            # A2A protocol client and data model
│       ├── a2a_server.py     # A2A HTTP server
│       └── ...
├── examples/                 # Example .aegis programs
├── tests/                    # 1,712 tests
├── DOCS/                     # Extended documentation
├── SPEC.md                   # Language specification
└── CHANGELOG.md              # Release history
```

## Demo Applications

Seven full-featured demo agents in [`apps/`](apps/):

| App | Domain | Run |
|-----|--------|-----|
| SOC Agent | Cybersecurity incident response | `python apps/soc_agent/harness.py` |
| Medical Assistant | HIPAA-compliant clinical workflow | `python apps/medical_assistant/harness.py` |
| API Gateway | Input sanitization and routing | `python apps/api_gateway/harness.py` |
| Support Agent | Customer service with memory | `python apps/support_agent/harness.py` |
| Code Review Bot | PR analysis with plans | `python apps/code_review_bot/harness.py` |
| Research Pipeline | Multi-agent delegation | `python apps/research_pipeline/harness.py` |
| Compliance Processor | EU AI Act compliance | `python apps/compliance_processor/harness.py` |

See also [`examples/quickstart.aegis`](examples/quickstart.aegis) for a 30-second tour of core features.

## Editor Support

**VS Code**: Install the extension from [`vscode-aegis/`](vscode-aegis/) for syntax highlighting, diagnostics, completion, and hover docs:

```bash
cd vscode-aegis && npm install && npm run compile
# Then press F5 in VS Code to launch with the extension
```

The extension connects to the built-in LSP server (`aegis lsp`) for real-time error checking and code completion.

## Documentation

- [Language Specification](SPEC.md) — Full syntax and semantics reference
- [Security Model](DOCS/security-model.md) — Taint, capabilities, sandbox architecture
- [Agent Constructs](DOCS/agent-constructs.md) — AI agent language features
- [Audit and Compliance](DOCS/audit-and-compliance.md) — Event ledger, EU AI Act
- [Syntax Reference](DOCS/syntax-reference.md) — Quick reference card
- [Contributing](CONTRIBUTING.md) — Development setup and guidelines

## Testing

```bash
# Full test suite (1,712 tests, ~30 seconds)
pytest tests/ -v

# With coverage
pytest tests/ --cov=aegis --cov-report=term-missing

# Specific component
pytest tests/test_lexer.py -v
pytest tests/test_phase6e_smt.py -v  # Requires z3-solver
```

## License

[Apache License 2.0](LICENSE)


