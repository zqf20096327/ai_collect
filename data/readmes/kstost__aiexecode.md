# AIEXEcode

<div align="center">

**AI-Powered Autonomous Coding Agent**

*by 코드깎는노인*

[Website](https://aiexecode.com) | [GitHub](https://github.com/kstost/aiexecode)

</div>

---

## What is AIEXEcode?

**AIEXEcode** is a CLI-based AI coding agent that autonomously handles software development tasks. Simply describe what you want in natural language, and the AI will analyze, plan, and execute the work for you.

### Key Features

- **Natural Language Interface**: Just describe what you want - no complex commands needed
- **Autonomous Execution**: AI analyzes code, creates plans, and executes them automatically
- **Session Management**: Pause and resume work anytime with session IDs
- **Log Viewer**: Web-based UI to review AI's actions and decisions
- **MCP Integration**: Extend capabilities with Model Context Protocol servers
- **Z.AI Integration**: Powered by Z.AI's advanced GLM models

### What You Can Do

- **Bug Fixes**: "Fix the authentication error in login.js"
- **Add Features**: "Create a user profile editing feature"
- **Refactoring**: "Clean up the auth module for better readability"
- **Write Tests**: "Write unit tests for all API endpoints"
- **Documentation**: "Add JSDoc comments to main functions"

---

## Installation

### System Requirements

| Requirement | Details |
|-------------|---------|
| **OS** | macOS, Linux (Windows not supported) |
| **Node.js** | 18.0.0 or higher |
| **npm** | 8.0.0 or higher |
| **ripgrep** | Required for code search |

### Step 1: Install ripgrep

**macOS:**
```bash
brew install ripgrep
```

**Ubuntu/Debian:**
```bash
sudo apt-get install ripgrep
```

**Fedora/CentOS:**
```bash
sudo dnf install ripgrep
```

**Arch Linux:**
```bash
sudo pacman -S ripgrep
```

### Step 2: Install AIEXEcode

```bash
npm install -g aiexecode
```

---

## Getting Started

### First Run Setup

```bash
aiexecode
```

On first run, the setup wizard will guide you through:

1. **Enter API Key** - Your Z.AI API key
2. **Select Model** - Choose from available models

**Where to get API key:**
- **Z.AI**: https://z.ai/manage-apikey/apikey-list

### Basic Usage

**Interactive Mode (Recommended):**
```bash
aiexecode
```

Then enter your requests naturally:
```
> Fix all lint errors in src/
> Add input validation to the signup form
> /exit
```

**Direct Execution:**
```bash
aiexecode "create a REST API for user management"
```

---

## Supported Models

### Z.AI (GLM Series)

| Model | Description | Context | Max Output |
|-------|-------------|---------|------------|
| `glm-4.7` | Latest flagship model | 200K | 128K |
| `glm-4.6` | High-performance model | 200K | 128K |
| `glm-4.5-air` | Fast, lightweight | 128K | 96K |
| `glm-4.5` | Standard model (default) | 128K | 96K |

- Supports **Thinking Mode**, prompt caching, and server-side web search

Use `/model list` to see all models or `/model <name>` to switch.

---

## Commands

### CLI Options

```bash
aiexecode                              # Interactive mode
aiexecode "task description"           # Direct execution
aiexecode -c <session_id>              # Continue previous session
aiexecode -c <session_id> "new task"   # Continue with new task
aiexecode --init                       # Initialize project prompts
aiexecode --viewer                     # Start log viewer (port 3000)
aiexecode --viewer --port 8080         # Log viewer on custom port
aiexecode --dangerously-skip-permissions "task"  # Skip approval prompts
```

### Interactive Commands

| Command | Description |
|---------|-------------|
| `/help` | Show all available commands |
| `/exit` | Exit the application |
| `/clear` | Clear the screen |
| `/apikey` | Change API key |
| `/model` | Select AI model |
| `/model list` | List all available models |
| `/tools` | Enable/disable tools |
| `/mcp` | View MCP server status |
| `/agents` | Show AGENTS.md content |
| `/skills` | List project skills |
| `/commands` | List custom commands |

---

## Session Management

AIEXEcode automatically saves your work sessions, allowing you to pause and resume later.

### How It Works

```bash
# Start a new session
aiexecode
> Create a large file processing feature
# Output: Session ID: abc1234567890def

# Continue later
aiexecode -c abc1234567890def
> Now add error handling
```

Sessions are stored in `.aiexe/<session_id>/` and include:
- Complete conversation history
- Tool execution logs
- File modification records

---

## Log Viewer

Review what the AI did through a web-based interface.

```bash
aiexecode --viewer
```

Open `http://localhost:3000` to see:
- Commands executed by AI
- File modification history
- AI's thinking process
- API request/response logs

---

## MCP Server Integration

Extend AIEXEcode's capabilities by connecting Model Context Protocol (MCP) servers.

### Adding MCP Servers

**stdio-based server:**
```bash
aiexecode mcp add --transport stdio github -- npx -y @modelcontextprotocol/server-github
```

**HTTP-based server:**
```bash
aiexecode mcp add --transport http myserver http://localhost:3000
```

**JSON configuration:**
```bash
aiexecode mcp add-json github '{"type":"stdio","command":"npx","args":["-y","@modelcontextprotocol/server-github"]}'
```

### Managing MCP Servers

```bash
aiexecode mcp list              # List all servers
aiexecode mcp get <name>        # Get server details
aiexecode mcp remove <name>     # Remove a server
```

### In Interactive Mode

```bash
/mcp                  # Show all MCP servers and tools
/mcp <server-name>    # Show specific server's tools
```

---

## Project Customization

### Custom Prompts

Initialize project-specific AI behavior:

```bash
aiexecode --init
```

This creates `.aiexe/prompts/` where you can customize how AI behaves for your project.

### Custom Commands

Add JavaScript files to `.aiexe/commands/` for project-specific slash commands.

### Skills

Add JavaScript files to `.aiexe/skills/` for reusable AI capabilities.

### AGENTS.md

Create an `AGENTS.md` file in your project root to provide additional context to the AI about your project's conventions and requirements.

---

## Configuration

### Settings Location

| Path | Description |
|------|-------------|
| `~/.aiexe/settings.json` | Main configuration |
| `~/.aiexe/mcp_config.json` | MCP server settings |
| `~/.aiexe/skills/` | Personal skills |
| `~/.aiexe/commands/` | Personal commands |
| `.aiexe/` | Project-specific settings |

### Available Tools

AIEXEcode provides these built-in tools for AI:

- `edit_file_range` - Edit specific line ranges
- `edit_file_replace` - Replace exact strings
- `write_file` - Create or overwrite files
- `read_file` - Read entire files
- `read_file_range` - Read specific line ranges
- `bash` - Execute shell commands
- `run_python_code` - Run Python scripts
- `fetch_web_page` - Fetch web content
- `ripgrep` - Search code with ripgrep
- `glob_search` - Find files by pattern

Enable/disable tools with `/tools enable|disable <tool-name>`.

---

## Requirements Summary

**Required:**
- macOS or Linux
- Node.js 18+
- npm 8+
- ripgrep
- Z.AI API key

**Optional:**
- Python 3 (for Python code execution)

---

## Contact

- **Website**: https://aiexecode.com
- **Issues**: https://github.com/kstost/aiexecode/issues

---

## Disclaimer

**THIS SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.**

**IN NO EVENT SHALL THE AUTHORS, COPYRIGHT HOLDERS, OR CONTRIBUTORS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.**

This includes, without limitation:
- Data loss or corruption
- System damage or malfunction
- Security breaches or vulnerabilities
- Financial losses
- Any direct, indirect, incidental, special, exemplary, or consequential damages

**The user assumes full responsibility for all consequences arising from the use of this software, regardless of whether such use was intended, authorized, or anticipated.**

**USE AT YOUR OWN RISK.**

---

<div align="center">

**AIEXEcode** - AI Coding Agent for Developers

Made by 코드깎는노인

</div>
