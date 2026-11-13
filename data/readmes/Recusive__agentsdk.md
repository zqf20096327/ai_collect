# Orbit Rust SDK

**A complete Rust rewrite of OpenCode** — the open-source AI coding agent.

We're rebuilding OpenCode from the ground up in 100% Rust for better performance, lower memory footprint, and a truly native experience.

> **Note:** This is the open-source backend SDK derived from OpenCode. Orbit (our Unified Development Environment) is a separate, proprietary product that uses this SDK.

---

## Why Rust?

| Aspect | TypeScript/Bun | Rust |
|--------|----------------|------|
| **Memory** | ~200-500MB runtime | ~20-50MB |
| **Startup** | 1-3 seconds | <100ms |
| **Binary Size** | Node/Bun runtime required | Single static binary |
| **Native Integration** | FFI overhead | Zero-cost Tauri integration |
| **Concurrency** | Event loop limitations | True parallelism with async/await |

By rewriting in Rust, we get:

- **Instant startup** — no runtime initialization
- **Minimal memory** — critical for running alongside heavy IDEs
- **Native Tauri integration** — seamless desktop app without IPC overhead
- **Single binary distribution** — no dependencies, no node_modules
- **True concurrency** — parallel tool execution without blocking

---

## What is This?

**Orbit Rust SDK** is an open-source AI agent backend that handles:

- LLM provider communication (Anthropic, OpenAI, Google, AWS Bedrock, local models)
- Tool execution (bash, file operations, code analysis)
- Session management and conversation state
- Real-time streaming and event handling
- OAuth authentication flows (Claude Pro, ChatGPT Plus, GitHub Copilot)

This SDK is derived from [OpenCode](https://github.com/anomalyco/opencode) and is being rewritten in Rust. It's **free and open source** for the community to use, contribute to, and build upon.

**Orbit** (our Agentic UDE — Unified Development Environment) uses this SDK but is a separate, closed-source product.

---

## Current Status

**Phase: Active Development**

We're systematically converting the TypeScript codebase to Rust, crate by crate:

| Crate | Status | Description |
|-------|--------|-------------|
| `orbit-core` | ✅ Complete | ID generation, locks, timeouts, wildcard, filesystem, global paths |
| `orbit-bus` | 🔄 In Progress | Event pub/sub system |
| `orbit-storage` | ⬜ Planned | JSON file storage |
| `orbit-project` | ⬜ Planned | Project/instance context |
| `orbit-config` | ⬜ Planned | Configuration management |
| `orbit-permission` | ⬜ Planned | Permission system |
| `orbit-provider` | ⬜ Planned | AI provider adapters (Anthropic, OpenAI, Google, AWS) |
| `orbit-session` | ⬜ Planned | Session management |
| `orbit-tools` | ⬜ Planned | Agent tools (bash, read, write, edit, glob, grep) |
| `orbit-lsp` | ⬜ Planned | LSP client integration |
| `orbit-mcp` | ⬜ Planned | Model Context Protocol client |
| `orbit-server` | ⬜ Planned | HTTP API with SSE |

---

## Quick Start

```bash
# Check compilation
cargo check --workspace

# Run tests
cargo test --workspace

# Build release
cargo build --release

# Test crates during development
cargo run -p orbit-cli -- test-core
```

### Development CLI

We provide a simple test CLI for verifying crates as they're built:

```bash
# Show available commands
cargo run -p orbit-cli -- help

# Test orbit-core
cargo run -p orbit-cli -- test-core

# More commands added as crates are completed
```

---

## Architecture

```
orbit-rust-sdk/
├── Cargo.toml                  # Workspace manifest
├── crates/
│   ├── orbit-core/             # Foundation utilities
│   ├── orbit-bus/              # Event pub/sub
│   ├── orbit-storage/          # JSON file storage
│   ├── orbit-project/          # Project/instance context
│   ├── orbit-config/           # Configuration
│   ├── orbit-permission/       # Permission system
│   ├── orbit-provider/         # AI provider adapters
│   ├── orbit-session/          # Session management
│   ├── orbit-tools/            # Agent tools
│   ├── orbit-lsp/              # LSP client
│   ├── orbit-mcp/              # MCP client
│   ├── orbit-server/           # HTTP API server
│   └── orbit-cli/              # Development test CLI
├── docs/
│   ├── conversion/             # Conversion planning docs
│   ├── providers/              # Provider auth documentation
│   └── workflow/               # Development workflow guides
└── OpenCode-reference/         # Original TypeScript source
```

### Crate Dependency Graph

```
                    orbit-core
                    /    |    \
            orbit-bus  orbit-storage  orbit-config
                    \    |    /
                    orbit-project
                         |
                orbit-permission
                    /         \
           orbit-provider   orbit-tools
                    \         /
                   orbit-session
                    /    |    \
            orbit-lsp orbit-mcp orbit-server
```

---

## Documentation

| Document | Description |
|----------|-------------|
| [`docs/workflow/Workflow.md`](./docs/workflow/Workflow.md) | Main conversion workflow guide |
| [`docs/workflow/MODULE_MAPPING.md`](./docs/workflow/MODULE_MAPPING.md) | TypeScript → Rust module mapping |
| [`docs/providers/PROVIDER_AUTH.md`](./docs/providers/PROVIDER_AUTH.md) | OAuth flows for Claude, Codex, Copilot |
| [`docs/providers/RUST_AI_SDK_ALTERNATIVES.md`](./docs/providers/RUST_AI_SDK_ALTERNATIVES.md) | Rust alternatives to Vercel AI SDK |

Each crate also has a `CONVERSION.md` file mapping its TypeScript sources.

---

## Contributing

We welcome contributions! Whether you're:

- **Porting TypeScript to Rust** — Pick a module and start converting
- **Adding features** — New tools, providers, or improvements
- **Fixing bugs** — In either the TS or Rust codebase
- **Improving docs** — Better examples, guides, and explanations

This SDK is **free and open source**. Use it, fork it, build on it.

### Conversion Workflow

1. Check `crates/<crate-name>/CONVERSION.md` for the TypeScript → Rust mapping
2. Follow the patterns in `docs/workflow/Workflow.md`
3. Test with `cargo run -p orbit-cli -- test-<crate>`
4. Submit a PR

---

## Acknowledgments

**Special thanks to [OpenCode](https://github.com/anomalyco/opencode) and [Anomaly](https://anomaly.co) (SST)** for building the original open-source AI coding agent.

OpenCode proved that a fully open-source, provider-agnostic AI agent could rival proprietary solutions. We're taking their excellent work and rebuilding it in Rust to push performance even further.

---

## License

MIT License

Copyright (c) 2025 Recursive Labs
Copyright (c) 2024-2025 SST/OpenCode (Original Work)

See [LICENSE](./LICENSE) for details.

---

<p align="center">
  <strong>Orbit Rust SDK</strong>
  <br>
  <sub>Built on the foundations of OpenCode</sub>
</p>
