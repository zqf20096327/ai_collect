<div align="center">

# 🚀 Skillz - Self-Extending MCP Server

<img src="docs/skillz_hero.png" alt="Skillz Hero Banner" width="600">

<img src="docs/architecture-flow.png" alt="Skillz Architecture & Feature Flows" width="100%">

[![Crates.io](https://img.shields.io/crates/v/skillz.svg)](https://crates.io/crates/skillz)
[![CI](https://github.com/Algiras/skillz/actions/workflows/ci.yml/badge.svg)](https://github.com/Algiras/skillz/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Rust](https://img.shields.io/badge/rust-1.70%2B-orange.svg)](https://www.rust-lang.org/)
[![MCP](https://img.shields.io/badge/MCP-Full%20Support-blue.svg)](https://modelcontextprotocol.io/)

**Build and execute custom tools at runtime. Let your AI create its own tools.**

[Install](#-installation) •
[Configure](#-editor-configuration) •
[Features](#-features) •
[Examples](#-quick-examples) •
[Documentation](https://algiras.github.io/skillz)

</div>

---

## 🎯 Why Skillz?

Traditional MCP servers have a fixed set of tools. **Skillz lets your AI create new tools on the fly.**

<div align="center">
<table>
<tr>
<td width="50%" align="center">
  
### ❌ Traditional MCP
  
🔒 **Fixed Tool Set**  
Write server code

⬆️ **Deploy & Restart**  
Restart your editor

⏱️ **Time Consuming**  
Manual process

</td>
<td width="50%" align="center">
  
### ✅ Skillz

🔧 **Dynamic Tools**  
AI writes the code

⚡ **Instant**  
Compiles to WASM/Script

🚀 **Zero Downtime**  
No restarts needed

</td>
</tr>
</table>
</div>

**Example**: "Build me a tool that fetches weather data" → AI writes the code → Tool is instantly available.

No deployments. No restarts. Just ask.

---

## ⚡ Installation

<div align="center">

[![Crates.io](https://img.shields.io/crates/v/skillz.svg)](https://crates.io/crates/skillz)
[![Downloads](https://img.shields.io/crates/d/skillz.svg)](https://crates.io/crates/skillz)

</div>

```bash
# Install WASM target (required for building tools)
rustup target add wasm32-wasip1

# Install Skillz from crates.io
cargo install skillz
```

> **⚠️ Important**: Make sure `~/.cargo/bin` is in your PATH so your editor can find the `skillz` executable.

**Or build from source:**

```bash
git clone https://github.com/Algiras/skillz.git
cd skillz/mcp-wasm-host
cargo install --path .
```

---

## ☕ Support Skillz

If you find Skillz useful, please consider supporting its development:

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/algiras)

Your support enables new features and improvements!

---

## 🔧 Editor Configuration

### Cursor IDE

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "skillz": {
      "command": "skillz"
    }
  }
}
```

### 2. Configure MCP Client

Add the following to your MCP settings file (e.g., `~/Library/Application Support/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "skillz": {
      "command": "/Users/YOUR_USERNAME/.cargo/bin/skillz"
    }
  }
}
```

> [!TIP]
> If you encounter a `spawn skillz ENOENT` error, it means your client can't find the binary. Using the **absolute path** (usually `~/.cargo/bin/skillz`) fixes this!

> **Note**: If `skillz` isn't in your PATH, use: `~/.cargo/bin/skillz`

### HTTP Server Mode *(v0.4.0+)*

Run Skillz as an HTTP server for web integrations:

```bash
# Start HTTP server on port 8080
skillz --transport http --port 8080

# Custom host binding
skillz --transport http --host 0.0.0.0 --port 3000

# Enable hot reload (watch tools directory for changes)
skillz --hot-reload

# HTTP server with hot reload
skillz --transport http --port 8080 --hot-reload
```

**Endpoints:**
- `GET /sse` - Server-Sent Events stream for real-time updates
- `POST /message` - Send JSON-RPC messages

**Connect with curl:**
```bash
# Establish SSE connection
curl -N http://localhost:8080/sse -H 'Accept: text/event-stream'

# Send a message (in another terminal)
curl -X POST http://localhost:8080/message \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list"}'
```

---

## 🎯 Features

<div align="center">

### 🌟 Core Capabilities

</div>

| Feature | Description |
|---------|-------------|
| 🦀 **WASM Tools** | Compile Rust → WebAssembly at runtime |
| 📦 **Rust Crates** | Add serde, regex, anyhow, etc. to WASM tools! |
| 📜 **Script Tools** | Python, Node.js, Ruby, Bash, or any language |
| 🔌 **MCP Integration** | Import external stdio MCP servers, expose tools under namespaces |
| 🏷️ **Tool Annotations** | Hints for clients (readOnly, destructive, idempotent) |
| ⚡ **Code Execution** | Compose multiple tools via code (98% token savings!) |
| 📦 **Dependencies** | Auto-install pip/npm/cargo packages per tool |
| 🐳 **Docker Services** | Define & manage Docker services tools depend on |
| 💾 **Persistence** | Tools survive server restarts |
| 🔒 **Sandbox** | Optional bubblewrap/firejail/nsjail isolation |
| 📂 **Shareable** | Each tool has its own directory with manifest.json |
| 📖 **Dynamic Guide** | Built-in `skillz://guide` resource updates automatically |
| 🌐 **Tool Import** | Import tools from GitHub repos or Gists |
| ⛓️ **Pipelines** | Chain tools together declaratively |
| 🌍 **HTTP Transport** | Run as HTTP server with SSE for web apps |
| 💬 **Elicitation** | Scripts can request user input via MCP protocol |
| 🧠 **Memory** | Persistent key-value storage with TTL support |
| 📦 **Resources** | Tools can list and read server resources |
| 🔐 **Secrets** | Forward `SKILLZ_*` env vars to tools |
| 🔗 **Tools/Call** | Tools can call other registered tools |
| 📡 **Streaming** | Progressive output via stream chunks |
| 📊 **Logging/Progress** | Scripts can send logs and progress updates |
| 🔥 **Hot Reload** | Watch tools directory, auto-reload on changes |
| 📦 **Versioning** | Auto-backup on update, rollback to any version |
| 🔔 **Subscriptions** | Subscribe to resource updates, get notified on changes |
| 📋 **listChanged** | Hot reload emits MCP list changed notifications |
| 🎯 **_meta Support** | Progress tokens forwarded from MCP requests |
| ⛔ **Cancellation** | Handle cancellation requests for running tools |
| 💡 **Built-in Prompts** | 6 native prompts for creating tools via MCP protocol |
| 🎭 **Progressive Disclosure** | Tools appear only when their skill is activated |
| 📦 **Skill Bundles** | Activate multiple skills with `@bundle-name` |
| 🔗 **Skill Dependencies** | Skills can declare dependencies, auto-activated |
| 🤖 **LLM Discovery** | `suggest_skill` uses sampling to recommend skills |
| 📚 **Git Skill Repos** | Clone skill repos from GitHub with `add_skill_repo` |
| 🎓 **Knowledge Skills** | SKILL.md files as prompts (Claude Skills compatible) |

---

## 📖 Available Tools (15 Core)

| Tool | Description |
|------|-------------|
| `build_tool` | Compile Rust code → WASM tool (with crate dependencies) |
| `register_script` | Register script tool (Python, Node.js, etc.) with deps |
| `call_tool` | Execute any tool (WASM, Script, Pipeline, or MCP) |
| `list_tools` | List all available tools |
| `delete_tool` | Remove a tool and clean up |
| `import_tool` | Import tools from Git repos or GitHub Gists |
| `import_mcp` | Register external MCP servers under a namespace |
| `execute_code` | Run code that composes multiple tools |
| `pipeline` | Create, list, delete pipeline tools (action-based) |
| `memory` | Persistent storage for tools (store, get, list, delete, stats) |
| `version` | List versions, rollback to previous, view version info |
| `services` | Define & manage Docker services for tools |
| `activate_skill` | Enable a skill (or `@bundle`) to make its tools visible |
| `deactivate_skill` | Hide a skill's tools to reduce noise |
| `suggest_skill` | LLM-powered skill recommendations |
| `add_skill_repo` | Clone skill repositories from Git (GitHub, etc.) |

---

## 📚 Skill Repositories

Import skills from Git repositories (compatible with Claude Skills format):

```python
# First, activate dev tools
activate_skill(name="dev")

# Import a skill repository
add_skill_repo(url="https://github.com/kepano/obsidian-skills")
# → "Added repo 'obsidian-skills' with 3 skills: obsidian-markdown, obsidian-bases, json-canvas"

# Import awesome-claude-skills (23+ skills!)
add_skill_repo(url="https://github.com/ComposioHQ/awesome-claude-skills", branch="master")
# → "Added repo 'awesome-claude-skills' with 23 skills: mcp-builder, webapp-testing, ..."
```

**Supported repo layouts:**
- `skills/skill-name/SKILL.md` (kepano/obsidian-skills style)
- `skill-name/SKILL.md` at root (ComposioHQ/awesome-claude-skills style)

**Skills appear as prompts** - use `prompts/get(name="skill-name")` to retrieve knowledge.

---

## 🎭 Progressive Disclosure

Tools are organized into skills that can be activated/deactivated:

```python
# See what's available
suggest_skill(context="I want to build an MCP server")
# → "Suggested skills: dev, mcp-builder"

# Activate skills
activate_skill(name="dev")        # Enable developer tools
activate_skill(name="@dev-full")  # Enable bundle: dev + sys + memory

# Create a tool (it's hidden by default)
register_script(name="my-tool", code="...")
activate_skill(name="my-tool")    # Now it's visible

# Hide when done
deactivate_skill(name="my-tool")
```

**Virtual Skills:**
| Skill | Tools |
|-------|-------|
| `dev` | `register_script`, `build_tool`, `import_mcp`, `add_skill_repo`, etc. |
| `sys` | `pipeline`, `services`, `call_tool_internal` |
| `memory` | `memory` |

**Bundles** (`~/.gemini/skills/bundles.json`):
```json
{
  "@dev-full": ["dev", "sys", "memory"],
  "@creators": ["dev"]
}
```

---

## 💡 Quick Examples

<div align="center">

### 🔥 See Skillz in Action

</div>

### 🦀 Build a WASM Tool (Rust)

```rust
build_tool(
  name: "fibonacci",
  description: "Generates Fibonacci numbers",
  code: "fn main() { 
    let (mut a, mut b) = (0u64, 1); 
    for _ in 0..20 { print!(\"{} \", a); (a, b) = (b, a + b); } 
  }",
  annotations: {"readOnlyHint": true}
)
```

### 🔌 Import an External MCP Server

```python
# Register a stdio MCP server - all its tools become available under a namespace
import_mcp(
  name: "time",
  command: "uvx",
  args: ["mcp-server-time"],
  description: "Time utilities from MCP server"
)

# Now use its tools with the namespace prefix
call_tool(tool_name: "time_get_current_time", arguments: {"timezone": "UTC"})

# Use MCP tools in pipelines!
pipeline(
  action: "create",
  name: "world_clock",
  steps: [
    { name: "ny", tool: "time_get_current_time", args: { timezone: "America/New_York" } },
    { name: "london", tool: "time_get_current_time", args: { timezone: "Europe/London" } },
    { tool: "word_counter", args: { text: "NY: $ny.datetime, London: $london.datetime" } }
  ]
)
```

> **Note**: Only **stdio** MCP servers are supported (command + args). HTTP/SSE servers are not yet supported.
```

> **🤖 For LLMs & Advanced Users**  
> See [docs/LLM_GUIDE.md](docs/LLM_GUIDE.md) for detailed technical specifications, JSON-RPC protocols, script templates, and advanced usage examples.

---

## 🔧 Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `TOOLS_DIR` | Where tools are stored | `~/.skillz/tools` |
| `SKILLZ_ROOTS` | Workspace roots (colon-separated) | `/home/user/project:/data` |
| `SKILLZ_SANDBOX` | Sandbox mode | `bubblewrap`, `firejail`, `nsjail` |
| `SKILLZ_SANDBOX_NETWORK` | Allow network in sandbox | `1` |
| `SKILLZ_*` | **Forwarded to tools** (for secrets) | `SKILLZ_OPENAI_KEY=sk-...` |

**Root Priority:** MCP client roots > `SKILLZ_ROOTS` env > cwd

### 🔐 Secrets via Environment Variables

All `SKILLZ_*` prefixed env vars are forwarded to script tools:

```bash
# Set secrets in your shell
export SKILLZ_OPENAI_KEY="sk-..."
export SKILLZ_API_TOKEN="your-secret"
export SKILLZ_DEBUG="1"
```

Access in tools via `context.environment`:
```python
env = request["params"]["context"]["environment"]
api_key = env.get("SKILLZ_OPENAI_KEY")
```

> **Note:** Only `SKILLZ_*` vars are forwarded. Other env vars are not exposed to tools for security.

---

## 🐳 Docker Services

Tools can declare dependencies on Docker services (databases, caches, etc.). When a tool runs, Skillz checks if required services are running and injects connection environment variables.

### Define a Service

```python
services(
  action: "define",
  name: "postgres",
  image: "postgres:15",
  ports: ["5432"],
  env: {"POSTGRES_PASSWORD": "dev"},
  volumes: ["data:/var/lib/postgresql/data"],
  healthcheck: {
    cmd: "pg_isready -U postgres",
    interval: "2s",
    retries: 15
  }
)
```

### Manage Services

```python
# List all defined services
services(action: "list")

# Start a service
services(action: "start", name: "postgres")

# Check status (running, ports, health)
services(action: "status", name: "postgres")

# View logs
services(action: "logs", name: "postgres", tail: 100)

# Stop/remove services
services(action: "stop", name: "postgres")
services(action: "remove", name: "postgres")

# Cleanup unused services
services(action: "prune")
```

### Tools with Service Dependencies

Register a tool that requires services:

```python
register_script(
  name: "user_manager",
  description: "Manage users in PostgreSQL",
  interpreter: "python3",
  requires_services: ["postgres"],  # Tool requires postgres to be running
  dependencies: ["psycopg2-binary"],
  code: """
import json, sys, os
import psycopg2

request = json.loads(sys.stdin.readline())
args = request["params"]["arguments"]

# Connection details injected by Skillz
conn = psycopg2.connect(
    host=os.environ["POSTGRES_HOST"],  # Auto-injected
    port=os.environ["POSTGRES_PORT"],  # Auto-injected
    user="postgres",
    password="dev",
    dbname="postgres"
)
# ... your code
"""
)
```

When calling `user_manager`, Skillz will:
1. Check if `postgres` service is running
2. If not running, return a helpful error with fix command
3. If running, inject `POSTGRES_HOST` and `POSTGRES_PORT` env vars

### Volume Types

| Type | Syntax | Description |
|------|--------|-------------|
| **Named** | `data:/path` | Docker-managed volume, prefixed with `skillz_` |
| **Bind** | `/host/path:/container/path` | Mount host directory into container |

---

## 🔒 Security

<div align="center">

### Platform Support

![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat&logo=linux&logoColor=black)
![macOS](https://img.shields.io/badge/macOS-000000?style=flat&logo=apple&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=flat&logo=windows&logoColor=white)

</div>

### 🛡️ Sandbox Modes (Linux Only)

Enable sandboxing via environment variable:

<table>
<tr>
<th>Sandbox</th>
<th>Security Level</th>
<th>Features</th>
</tr>
<tr>
<td>🟢 <b>bubblewrap</b></td>
<td>Medium</td>
<td>Namespace isolation</td>
</tr>
<tr>
<td>🟡 <b>firejail</b></td>
<td>High</td>
<td>seccomp + namespaces</td>
</tr>
<tr>
<td>🔴 <b>nsjail</b></td>
<td>Very High</td>
<td>Most restrictive</td>
</tr>
</table>

**Configuration:**

```bash
# Bubblewrap (namespace isolation)
export SKILLZ_SANDBOX=bubblewrap

# Firejail (seccomp + namespaces)
export SKILLZ_SANDBOX=firejail

# nsjail (most restrictive)
export SKILLZ_SANDBOX=nsjail

# Allow network in sandbox
export SKILLZ_SANDBOX_NETWORK=1
```

> 📖 See [SECURITY.md](SECURITY.md) for full details.

---

## 🛠️ Development

```bash
git clone https://github.com/Algiras/skillz.git
cd skillz
cargo build --release
cargo test
```

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📄 License

MIT License - see [LICENSE](LICENSE)

---

## 🔗 Links

<div align="center">

| Resource | Link |
|----------|------|
| 📦 **Crates.io** | [crates.io/crates/skillz](https://crates.io/crates/skillz) |
| 📖 **Documentation** | [algiras.github.io/skillz](https://algiras.github.io/skillz) |
| 💻 **GitHub** | [github.com/Algiras/skillz](https://github.com/Algiras/skillz) |
| 📋 **MCP Spec** | [modelcontextprotocol.io](https://modelcontextprotocol.io) |

---

**Built with ❤️ for AI-powered development**

[![Star on GitHub](https://img.shields.io/github/stars/Algiras/skillz?style=social)](https://github.com/Algiras/skillz)

</div>


