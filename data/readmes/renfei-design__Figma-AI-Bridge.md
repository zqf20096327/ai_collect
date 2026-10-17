# Figma AI Bridge

Let GitHub Copilot in VS Code control Figma in real-time through [MCP](https://modelcontextprotocol.io/) (Model Context Protocol).

[![Demo Video](https://img.youtube.com/vi/uoL2UcXiQNQ/maxresdefault.jpg)](https://www.youtube.com/watch?v=uoL2UcXiQNQ)

▶️ **[Watch the demo on YouTube](https://www.youtube.com/watch?v=uoL2UcXiQNQ)**

## Architecture

```
AI Assistant  ←stdio→  MCP Server (Node.js)  ←WebSocket→  Relay (port 3055)  ←WebSocket→  Figma Plugin
```

| Component | Location | Purpose |
|-----------|----------|---------|
| **Figma Plugin** | `plugin/` | Runs inside Figma, executes commands via `figma.*` APIs |
| **MCP Server** | `server/` | Defines MCP tools, connects to WebSocket relay on port 3055 |
| **VS Code Config** | `.vscode/mcp.json` | Registers the MCP server with VS Code |
| **Helper Scripts** | `scripts/` | CLI utilities for batch operations |

## Quick Start

### 1. Clone & Install

```bash
git clone https://github.com/renfei1992-dev/Figma_AI_Bridge.git
cd Figma_AI_Bridge
npm run setup
```

### 2. Import the Figma Plugin

In **Figma desktop** app:
1. Go to **Plugins → Development → Import plugin from manifest...**
2. Select `plugin/manifest.json` from this repo

### 3. Configure VS Code

If you open this project folder in VS Code, the `.vscode/mcp.json` is already configured. You're done.

To use it globally (in any project), add to `~/Library/Application Support/Code/User/mcp.json` (macOS) or `%APPDATA%\Code\User\mcp.json` (Windows):

```json
{
  "servers": {
    "figma-ai-bridge": {
      "type": "stdio",
      "command": "node",
      "args": ["/absolute/path/to/figma-ai-bridge/server/index.js"]
    }
  }
}
```

### 4. Each Session

1. **Start the relay server** — open a terminal and run:
   ```bash
   npm run relay
   ```
   Leave it running. The relay forwards messages between VS Code and Figma on port 3055.
2. **Run the plugin in Figma** — Plugins → Development → "Figma AI Bridge" → click **Connect**
3. **Start designing** — both the plugin and MCP server auto-join the same channel (`auto`), so you can immediately give design commands to Copilot

> **Tip:** If you need multiple instances or custom channels, use the `join_channel` tool to switch.

## Available Tools

### Reading

| Tool | Description |
|------|-------------|
| `get_document_info` | Get info about the current Figma document |
| `get_selection` | Get current selection |
| `read_my_design` | Get detailed info about the current selection including all node details |
| `get_node_info` | Get info about a specific node by ID |
| `get_nodes_info` | Get info about multiple nodes |
| `get_styles` | Get all styles from the document |
| `get_local_components` | Get all local components |
| `get_annotations` | Get annotations for a node |
| `get_instance_overrides` | Get override properties from a component instance |
| `get_reactions` | Get prototyping reactions from nodes |
| `get_component_properties` | Get all variant/boolean/text properties from a component instance |
| `list_pages` | List all pages in the document |

### Creating

| Tool | Description |
|------|-------------|
| `create_rectangle` | Create a rectangle |
| `create_frame` | Create a frame with optional auto-layout settings |
| `create_text` | Create a text element |
| `create_component_instance` | Create an instance of a component |
| `clone_node` | Clone an existing node |
| `create_section` | Create a section frame for organizing content |
| `create_page` | Create a new page in the document |

### Editing

| Tool | Description |
|------|-------------|
| `set_fill_color` | Set fill color of a node |
| `set_stroke_color` | Set stroke color of a node |
| `set_text_content` | Set text content of a text node |
| `set_multiple_text_contents` | Batch-update multiple text nodes |
| `set_corner_radius` | Set corner radius |
| `set_layout_mode` | Set auto-layout mode (horizontal/vertical) |
| `set_padding` | Set padding for auto-layout frames |
| `set_axis_align` | Set axis alignment for auto-layout frames |
| `set_layout_sizing` | Set sizing modes (fixed/hug/fill) |
| `set_item_spacing` | Set spacing between children |
| `set_annotation` | Create or update an annotation |
| `set_multiple_annotations` | Batch-set annotations |
| `set_instance_overrides` | Apply overrides to component instances |
| `set_component_properties` | Switch component variant properties (Type, Size, etc.) |
| `move_node` | Move a node to a new position |
| `resize_node` | Resize a node |
| `rename_node` | Rename a node |
| `set_visibility` | Show or hide a node |
| `set_opacity` | Set node opacity |
| `reparent_node` | Move a node to a new parent frame |
| `reorder_node` | Change z-order of a node within its parent |

### Other

| Tool | Description |
|------|-------------|
| `delete_node` | Delete a node |
| `delete_multiple_nodes` | Delete multiple nodes |
| `export_node_as_image` | Export a node as PNG/JPG/SVG/PDF |
| `scan_text_nodes` | Scan all text nodes in a subtree |
| `scan_nodes_by_types` | Scan for nodes of specific types |
| `set_focus` | Focus viewport on a node |
| `set_selections` | Set selection to specific nodes |
| `set_current_page` | Switch to a specific page |
| `set_default_connector` | Set default connector for FigJam |
| `create_connections` | Create connector lines between nodes |
| `group_nodes` | Group multiple nodes together |
| `ungroup_nodes` | Ungroup a group node |
| `join_channel` | Switch to a different WebSocket channel (auto-joined by default) |

### Design Skills

| Tool | Description |
|------|-------------|
| `create_slide` | Create a single presentation slide (title, content, visual, statement, columns, comparison, numbered) |
| `batch_slides` | Create multiple slides in one call — faster than creating individually |
| `create_doc_page` | Build a structured documentation page with sections, tables, and columns |
| `create_workflow_diagram` | Build a flowchart/process diagram with shapes, arrows, and auto-layout |
| `get_canvas_bounds` | Get bounding box of all top-level content to avoid overlap |

### Design Token Variables

| Tool | Description |
|------|-------------|
| `scan_bound_variables` | Scan a node tree for all bound design token variables |\n| `collect_bound_variables` | Collect and aggregate all bound variables with resolved values |
| `get_bound_variables` | Get variables bound to a specific node |
| `resolve_variable` | Resolve a variable by ID to get its current value |
| `bind_variable_to_fill` | Bind a design token variable to a node's fill color |
| `bind_variable_to_stroke` | Bind a design token variable to a node's stroke color |

## Helper Scripts

```bash
# Send a single command to Figma
node scripts/figma_cmd.mjs <channel> <command> '[paramsJSON]'

# Batch-bind design token variables
echo '[{"nodeId":"...","variableId":"...","property":"fill"}]' | node scripts/figma_bind_batch.mjs <channel>
```

## Project Structure

```
figma-ai-bridge/
├── .github/
│   └── skills/                # AI skill definitions (prompt instructions)
│       ├── a11y-audit/        # WCAG accessibility audit
│       │   ├── SKILL.md
│       │   ├── references/    # WCAG criteria reference
│       │   ├── scripts/       # a11y_check.py (offline analysis)
│       │   └── tests/         # Unit tests
│       ├── content-review/    # UI text review & style fixes
│       │   ├── SKILL.md
│       │   ├── references/    # Style guide (grammar, caps, words, punctuation)
│       │   └── scripts/       # figma_text.py (extract & apply text)
│       ├── figma-doc/         # Structured documentation pages
│       │   └── SKILL.md
│       ├── figma-slides/      # Presentation slide decks
│       │   └── SKILL.md
│       ├── online-research/   # Live web research
│       │   └── SKILL.md
│       └── workflow-diagram/  # Flowcharts & process maps
│           └── SKILL.md
├── plugin/
│   ├── manifest.json      # Figma plugin manifest
│   ├── code.js            # Plugin sandbox code (runs in Figma)
│   └── ui.html            # Plugin UI (WebSocket bridge)
├── server/
│   ├── package.json       # Server dependencies
│   ├── index.js           # MCP server (stdio transport, connects to relay)
│   └── relay.js           # WebSocket relay server (port 3055)
├── scripts/
│   ├── figma_cmd.mjs      # CLI: send single command
│   └── figma_bind_batch.mjs  # CLI: batch variable binding
├── .vscode/
│   └── mcp.json           # VS Code MCP integration
├── package.json           # Root project metadata
├── LICENSE                # MIT
└── README.md
```

## Skills

Skills are AI prompt instructions in `.github/skills/` that teach Copilot how to perform complex multi-step design tasks. Each skill has a `SKILL.md` with the full workflow, and optionally `references/` and `scripts/` for supporting files.

| Skill | Description |
|-------|-------------|
| **a11y-audit** | Scan Figma frames for WCAG 2.2 accessibility issues (contrast, font size, touch targets, alt text) and annotate violations |
| **content-review** | Review UI text against writing style guidelines (grammar, capitalization, word choice, punctuation) and apply fixes |
| **figma-doc** | Build structured documentation pages in Figma (paragraphs, columns, tables) in a single command |
| **figma-slides** | Create presentation decks with 7 slide types — auto-organized into sections on the canvas |
| **online-research** | Fetch live web data to ground content in current facts before creating docs or reports |
| **workflow-diagram** | Build flowcharts and process maps with auto-layout (shapes, arrows, swimlanes, decision diamonds) |

## Figma Sandbox Notes

The Figma plugin sandbox uses an older JS engine. The plugin code (`plugin/code.js`) avoids:
- Spread syntax (`...`)
- Template literals in some contexts
- `for...of` on objects
- `Object.entries()` with destructuring

All plugin code uses `var`, traditional `for` loops, and string concatenation for compatibility.

## License

[MIT](LICENSE)
