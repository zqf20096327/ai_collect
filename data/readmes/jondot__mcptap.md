# 🔍 mcp-tap

> **Intercept, monitor, and diagnose Model Context Protocol communications**

[![Rust](https://img.shields.io/badge/rust-1.70+-orange.svg)](https://www.rust-lang.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**mcp-tap** is a diagnostics tool for Model Context Protocol (MCP) communications—think Wireshark for MCP. It acts as a transparent proxy, giving you complete visibility into all MCP traffic between clients and servers. Debug integrations, monitor tool usage, analyze performance, and optionally enforce policies—all in real-time with a beautiful terminal UI.

https://github.com/user-attachments/assets/fe695a46-1654-4360-868b-1b8e2ea2c02c


## 🎯 Why mcp-tap?

When debugging MCP integrations, you need to see what's actually happening between your client and servers. **mcp-tap** gives you:

- 👁️ **Complete Visibility**: See every request and response in real-time with syntax-highlighted JSON
- 🐛 **Debugging**: Understand why tools aren't working, trace request flows, and diagnose integration issues
- 📊 **Traffic Analysis**: Filter, search, and analyze MCP communications like a network packet analyzer
- 🔍 **Policy-Based Filtering**: Use CEL expressions to highlight or filter specific patterns (useful for both debugging and security)
- 🚀 **Zero Configuration**: Works with existing MCP setups—just tap and go

Perfect for developers debugging MCP integrations, security professionals auditing tool usage, and anyone who needs visibility into MCP communications.

## ✨ Features

### 🔍 Real-Time Monitoring & Diagnostics
- Beautiful terminal UI with syntax highlighting
- Filter and search through requests/responses
- View bidirectional traffic (client ↔ server)
- Export to stdout for scripting and logging
- Inspect JSON-RPC messages, tool calls, and responses

### 🎯 Policy-Based Filtering & Alerting
- **CEL-based rules**: Write powerful filter expressions using Common Expression Language
- **Two modes**: 
  - `observe`: Highlight and log matching patterns without blocking (perfect for debugging)
  - `enforce`: Block requests that match deny rules (useful for security policies)
- **Per-MCP policies**: Different rules for different MCP servers
- **Pattern matching**: Filter by method, tool name, arguments, or any request property

### 🔌 Transport Support
- **stdio**: Intercept standard input/output MCP servers
- **HTTP**: Proxy HTTP-based MCP servers
- Automatic transport detection and handling

### 🎨 Developer Experience
- Non-invasive: Works with existing MCP configurations
- Automatic backup and restore of config files
- State management for clean tap/untap operations
- Comprehensive error messages and logging

## 🚀 Quick Start

### Installation

**Install from releases:**

Download the latest release from [GitHub Releases](https://github.com/jondot/mcptap/releases) and extract the binary to a location in your PATH.

### Basic Usage

**1. Monitor all MCP servers (observe mode):**
```bash
mcp-tap tap --mcp-config ~/.config/mcp.json
```

**2. Monitor a specific MCP server:**
```bash
mcp-tap tap --mcp-config ~/.config/mcp.json --mcp filesystem
```

**3. Use policy-based filtering (observe mode for debugging, enforce for blocking):**
```bash
mcp-tap tap --mcp-config ~/.config/mcp.json --policy policy.yaml --mode observe
```

**4. Output to stdout (for logging/scripting):**
```bash
mcp-tap tap --mcp-config ~/.config/mcp.json --stdout
```

**5. Stop monitoring (restore original config):**
```bash
mcp-tap untap --mcp-config ~/.config/mcp.json
```

## 📋 Policy Examples

### Example 1: Highlight File System Operations (Debugging)

```yaml
mcps:
  filesystem:
    mode: observe  # Just highlight, don't block
    deny:
      # Highlight when reading from /etc, /home, or .env files
      - 'request.method == "tools/call" && request.params.name == "read_file" && request.params.arguments.uri.startsWith("file:///etc/")'
      - 'request.method == "tools/call" && request.params.name == "read_file" && request.params.arguments.uri.startsWith("file:///home/")'
      - 'request.method == "tools/call" && request.params.name == "read_file" && request.params.arguments.uri.contains(".env")'
```

### Example 2: Filter to Specific Tools (Focus on What Matters)

```yaml
mcps:
  my-mcp:
    mode: observe
    allow:
      # Only highlight tools/list and specific tools you're debugging
      - 'request.method == "tools/list"'
      - 'request.method == "tools/call" && request.params.name == "my_tool"'
    deny:
      # Filter out everything else (reduce noise)
      - 'request.method == "tools/call"'
```

### Creating a Policy File

Generate a boilerplate policy file from your MCP config:

```bash
mcp-tap create-policy --mcp-config ~/.config/mcp.json --output policy.yaml
```

Then edit `policy.yaml` to add your rules.

## 🏗️ How It Works

mcp-tap works by rewriting your MCP configuration file to insert itself as a proxy between your client and MCP servers. When you run `mcp-tap tap`, it:

1. **Backs up your original config** to a safe location
2. **Rewrites the config** to point MCP servers through mcp-tap's hub
3. **Intercepts all traffic** flowing between the client and servers
4. **Displays everything** in the terminal UI or stdout

When you run `mcp-tap untap`, it restores your original configuration file, removing mcp-tap from the path. This non-invasive approach means you can tap and untap without permanently modifying your setup.

## 🛠️ Development

### Building

```bash
cargo build --release
```

### Running Tests

```bash
cargo test
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with [Rust](https://www.rust-lang.org/) for performance and safety
- Uses [CEL](https://github.com/google/cel-spec) for policy expressions
- TUI powered by [ratatui](https://github.com/ratatui-org/ratatui)
- Inspired by network diagnostics tools like Wireshark

---

**Made with ❤️ for developers and security professionals who need visibility into MCP communications**


