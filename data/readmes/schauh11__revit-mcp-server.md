# Revit MCP Server

**AI chat for Autodesk Revit that lives inside Revit.** No Claude Desktop. No external apps. Just a native chat panel, a WebSocket server, and 53+ tools that talk directly to the Revit API.

![Revit 2026](https://img.shields.io/badge/Revit-2026-blue)
![MIT License](https://img.shields.io/badge/license-MIT-green)
![Node.js 18+](https://img.shields.io/badge/node-%E2%89%A518.0.0-brightgreen)
![.NET 8.0](https://img.shields.io/badge/.NET-8.0-purple)
![Tools](https://img.shields.io/badge/tools-53+-orange)

**Author:** [Sanjay Chauhan](https://www.linkedin.com/in/schauh11/) | [GitHub](https://github.com/schauh11)

---

A native WPF chat panel docked inside Revit. The plugin and MCP server communicate over WebSocket on localhost — the AI sees your active view, selection, and model context in real time. No middleman.

Supports multiple AI providers out of the box: OpenRouter (100+ models), Anthropic Claude, DeepSeek, and Qwen. Switch providers by changing one line in your `.env` file. Run Qwen locally through Ollama for free.

53 specialized tools cover query, selection, visibility, views, sheets, MEP, tagging, and export. 5 additional dynamic intent tools (`query`, `execute`, `analyze`, `navigate`, `create`) work across any Revit category — so "query Walls", "query Conduit", "query Electrical Fixtures" all work without needing a separate hardcoded tool for each.

### Demo

![List Walls](docs/images/list_walls.gif)

![Hide Grids](docs/images/hide_grids.gif)

---

## Features

### Query & Analysis (10 tools)
- `get_elements` - Query any category with pagination
- `get_element_parameters` - Get Length, Area, Volume, Mark, Comments
- `calculate_quantities` - One-stop quantity takeoffs
- `find_elements_by_parameter` - Complex AND/OR filtering with operators
- `export_schedule_data` - Export schedules to CSV
- `count_elements_by_family` / `count_elements_by_type` / `count_views_by_type`
- `get_element_room` - Get containing room or MEP space
- `get_project_info` - Project metadata

### Selection (8 tools)
- `select_all_by_category` - Select all elements of a category
- `select_elements_by_level` - Select by level
- `select_similar_by_category` / `select_similar_by_family` / `select_similar_by_type`
- `select_and_hide_category` - Compound select + hide
- `select_and_isolate_category` - Compound select + isolate

### Visibility & Isolation (6 tools)
- `hide_elements_by_category` / `unhide_elements_by_category`
- `hide_selected_elements` / `unhide_all_in_view`
- `isolate_elements_by_category` / `isolate_selected_elements`

### View Management (6 tools)
- `duplicate_active_view` / `duplicate_view_by_name` / `duplicate_views`
- `create_dependent_views` - Create N dependent views from parent
- `get_view_info` / `list_all_views`

### Sheet Management (6 tools)
- `create_new_sheet` - Create sheet with number and name
- `place_view_on_sheet` - Place viewport at coordinates
- `get_sheet_info` / `get_all_sheets_info`
- `duplicate_and_place_view` - Atomic duplicate + place
- `create_sheet_and_place_view` - Atomic sheet creation + view placement

### MEP & Electrical (8 tools)
- `get_panel_schedules` - All electrical panels with metadata
- `create_panel_schedule` - Create panel schedule view
- `perform_conduit_run_qa` - Full QA workflow with color coding
- `calculate_conduit_bend_total` - Bend angles for conduit runs
- `get_total_conduit_length` - Sum all conduit in model
- `get_conduit_length_by_size` - Length breakdown by conduit diameter
- `get_total_wall_length` - Wall length calculations
- `get_element_room` - Room/space containment

### Grid & Level Tools (3 tools)
- `copy_grid_state` - Copy visibility states to storage
- `paste_grid_state` - Apply saved state to current view
- `rename_element` - Rename views, levels, or sheets

### Annotation & Drafting (4 tools)
- `find_and_tag_elements` - Find and tag in one operation
- `batch_create_tags` - Tag multiple elements
- `delete_empty_tags` - Remove tags with no content
- `find_duplicate_elements` - Detect duplicates by name/type

### Utilities (2 tools)
- `orient_elements_to_view` - Align with view orientation
- `export_to_csv` - Export elements to CSV file

---

## Supported AI Models

| Provider | Models | Notes |
|----------|--------|-------|
| **OpenRouter** | Qwen3 235B, DeepSeek v3, Claude, Gemini, and 100+ more | Recommended — one API key, many models |
| **Anthropic** | Claude Opus 4.5, Sonnet, Haiku | Direct API, best tool-use accuracy |
| **DeepSeek** | DeepSeek Chat, R1 (reasoning) | Cost-effective |
| **Qwen** | Qwen 2.5 (via Ollama or DashScope) | Free local option with Ollama |

---

## Quick Start

### Prerequisites
- Autodesk Revit 2026
- Node.js 18.0+
- API key for your chosen provider (or Ollama for free local use)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/schauh11/revit-mcp-server.git
cd revit-mcp-server
```

**2. Configure the MCP server**
```bash
cd mcp-server
npm install
cp .env.example .env
```

Edit `.env` with your configuration:
```env
# Choose your provider (default: openrouter)
LLM_PROVIDER=openrouter

# Set your API key
OPENROUTER_API_KEY=sk-or-v1-...

# Optional: change model (default: qwen/qwen3-235b-a22b)
OPENROUTER_MODEL_NAME=qwen/qwen3-235b-a22b

# Optional: change port (default: 3847)
PORT=3847
```

**3. Build the Revit plugin**
```bash
dotnet build RevitPlugin/RevitPlugin.csproj -c Release
```
The DLL auto-copies to `%APPDATA%\Autodesk\Revit\Addins\2026\`

**4. Launch**
- Open Revit 2026
- Go to Add-Ins ribbon
- Click "pySC Chat"
- The server starts automatically when you open the chat panel
- Start chatting with your model

---

## Example Conversations

### Simple Query
```
You: List all the walls
AI: Found 127 walls in your model:
    - Basic Wall - Interior: 45
    - Basic Wall - Exterior: 32
    - Curtain Wall: 50
```

### Context-Aware Follow-up
```
You: List all grids
AI: Found 12 grids: A, B, C, D, E, F, 1, 2, 3, 4, 5, 6

You: Hide them
AI: Hidden 12 grids in the current view.
```

### Multi-Step Operation
```
You: Duplicate Level 2 floor plan and place it on a new sheet A221
AI: Done! Created:
    - View: "Level 2 - Copy 1"
    - Sheet: A221 - "Level 2 Plan"
    - Placed view at center of sheet
```

### MEP Workflow
```
You: Calculate total conduit length by size
AI: Total conduit lengths:
    - 3/4": 1,250 LF
    - 1": 890 LF
    - 1-1/4": 445 LF
    - 2": 220 LF
    Total: 2,805 LF
```

---

## Architecture

![System Architecture](docs/images/System%20Architecture.png)

![Message Flow Sequence](docs/images/Message%20Flow%20Sequence.png)

### How It Works

1. **User types** a natural language command in the embedded Revit chat panel
2. **Plugin sends** the message via WebSocket with model context (active view, selection, levels, sheets)
3. **MCP Server** forwards to the configured AI provider with conversation history and tool definitions
4. **AI selects** appropriate tools and returns execution plan
5. **Server routes** tool commands back to the plugin
6. **Plugin executes** via ExternalEvent (thread-safe Revit API access)
7. **Results return** to AI for natural language response
8. **User sees** the formatted response in the chat panel

### Technical Details

- **Thread-safe** - All Revit API calls go through ExternalEvent pattern
- **Atomic transactions** - Multi-step operations succeed or fail together
- **Prompt caching** - Reduces system prompt tokens from ~5000 to ~200 per request
- **Auto-reconnect** - Handles disconnections gracefully
- **100-message history** - Full conversation context persisted in SQLite
- **Request locking** - Per-connection locks prevent concurrent API calls

---

## Project Structure

```
revit-mcp-server/
+-- RevitPlugin/              # C# Revit Plugin (.NET 8.0)
|   +-- Commands/             # App lifecycle, server management
|   +-- UI/                   # WPF chat panel
|   +-- Services/             # WebSocket, tool executor, model index
|   +-- Helpers/              # Category normalization, grid/level utilities
|   +-- Resources/tools.json  # Plugin-side tool schemas
|
+-- mcp-server/               # Node.js/TypeScript Server
|   +-- src/
|   |   +-- index.ts          # Entry point, provider initialization
|   |   +-- mcpServer.ts      # WebSocket server
|   |   +-- websocketHandler.ts  # Message routing, tool execution
|   |   +-- providers/        # LLM provider implementations
|   |   +-- conversation/     # SQLite-backed history management
|   |   +-- config/           # Model configuration
|   +-- tools.json            # 53+ tool definitions
|
+-- docs/                     # Documentation and images
+-- README.md
```

---

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| "Timeout: No response" | Server not running or API issue | Check server console, verify API key |
| "Auto-disconnected" | Idle for 15+ minutes | Normal behavior, send message to reconnect |
| "Failed to connect" | Port conflict or server down | Check port 3847, restart server |
| Slow first response | Model indexing in progress | Subsequent requests use cache |

---

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

For major changes, please open an issue first to discuss what you would like to change.

---

## License

MIT License - see [LICENSE](./LICENSE)

---

## Acknowledgments

Special thanks to the Revit API community and all contributors who helped make this project possible.

If you find this project useful, please consider giving it a star!
