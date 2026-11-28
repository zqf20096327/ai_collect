# Blender MCP Pro

Control Blender entirely from AI assistants (Claude Code, Claude Desktop, Cursor, Windsurf) via MCP.

**120+ tools across 17 categories** — Scene management, materials, shader nodes, lights, modifiers, animation, geometry nodes (with scatter/array templates), camera, rendering, import/export, UV/texture, batch processing, asset integration (Poly Haven, Sketchfab), rigging, rig diagnostics, scene utilities, workflow presets, and code execution.

## Pricing

| | Subscription | One-Time Purchase |
|---|---|---|
| **Price** | $5/month (7-day free trial) | $15 |
| **Platform** | [Gumroad](https://y1uda.gumroad.com/l/bmp) | [itch.io](https://y1uda.itch.io/blender-mcp-pro) |
| **Updates** | Included while subscribed | Lifetime updates |

## Get Started

1. **Purchase on [itch.io](https://y1uda.itch.io/blender-mcp-pro)** ($15 one-time) or **subscribe on [Gumroad](https://y1uda.gumroad.com/l/bmp)** ($5/month with 7-day free trial)
2. Download the ZIP containing the MCP server and this addon
3. Follow the setup instructions below

## Requirements

- **Blender 4.0+** (5.0 recommended)
- **Python 3.10+** (for the MCP server)
- MCP-compatible client (Claude Code / Claude Desktop / Cursor / Windsurf)

## Installation

After extracting the downloaded ZIP you should see:

```
blender_mcp_pro.zip   <- the Blender addon (install this in Blender)
server/               <- the MCP server (Python)
README.md
```

### 1. Install MCP server dependencies

```bash
cd server
pip install -r requirements.txt
```

> Requires the MCP Python SDK **1.x** (`mcp[cli]>=1.2.0,<2`, pinned in
> `requirements.txt`). MCP SDK 2.x is not compatible. If the server fails to
> start with `No module named 'mcp.server.fastmcp'`, run:
> `pip install "mcp[cli]>=1.2.0,<2"`

### 2. Install the Blender addon

1. Open Blender → **Edit > Preferences > Add-ons**
2. Click the dropdown (▾) at the top right → **Install from Disk…**
3. Select **`blender_mcp_pro.zip`** (the inner ZIP, not the outer download)
4. Enable **"Blender MCP Pro"** in the add-ons list
5. Open the 3D Viewport sidebar (N key) → **BM Pro** tab → **Start Server**

> Tested on Blender 4.0–5.0. If "Blender MCP Pro" does not appear after installing,
> make sure you selected the inner `blender_mcp_pro.zip` and not the outer
> `blender-mcp-pro-vX.Y.Z.zip` you downloaded.

### 3. Configure your MCP client

Add the following to your MCP client config. Replace `<path>` with the actual path where you extracted the ZIP.

> **License key**
> - **itch.io** ($15 one-time): no license key. Omit the `env` block entirely.
> - **Gumroad** ($5/month): include `BLENDER_MCP_PRO_LICENSE` with the key from your Gumroad receipt email.

#### Claude Code (`~/.claude.json`)

**itch.io (no license key):**

```json
{
  "mcpServers": {
    "blender-mcp-pro": {
      "command": "python",
      "args": ["<path>/server/server.py"]
    }
  }
}
```

**Gumroad (with license key):**

```json
{
  "mcpServers": {
    "blender-mcp-pro": {
      "command": "python",
      "args": ["<path>/server/server.py"],
      "env": {
        "BLENDER_MCP_PRO_LICENSE": "YOUR-LICENSE-KEY"
      }
    }
  }
}
```

#### Claude Desktop (`claude_desktop_config.json`)

Same shape as above — pick the itch.io or Gumroad variant depending on where you purchased.

#### Cursor / Windsurf

Add `server/server.py` in your MCP settings. itch.io customers don't need any environment variables; Gumroad customers should set `BLENDER_MCP_PRO_LICENSE`.

## Updating

When a new version is released:

1. Download the latest ZIP from your Gumroad library or itch.io
2. Extract and overwrite the existing `server/` folder, then re-run `pip install -r server/requirements.txt`
3. In Blender: **Edit > Preferences > Add-ons** → remove the old "Blender MCP Pro"
4. Install the new `blender_mcp_pro.zip` and enable it
5. Restart Blender

Your MCP client config does not need to change (Gumroad customers: keep the same license key).

## Usage

1. Start the addon server in Blender (N panel → **BM Pro** → **Start Server**)
2. Launch your MCP client (e.g., Claude Code)
3. Control Blender with natural language!

### Streamable HTTP Transport (optional)

By default, the MCP server uses stdio transport. For remote connections or web-based clients, you can use Streamable HTTP:

```bash
python server/server.py --transport streamable-http --port 8000
```

Then configure your MCP client to connect to `http://127.0.0.1:8000/mcp/`.

### Examples

```
"Create a Suzanne and add SubSurf and Bevel modifiers"
"Create a glass material and apply it"
"Set up three-point lighting"
"Set the camera to 85mm lens and track the object"
"Add a rotation animation"
"Render at 1920x1080 with Cycles"
```

## Architecture

```
AI Assistant (Claude / Cursor / Windsurf)
    │
    │ MCP Protocol (stdio)
    ▼
MCP Server (server.py)
    │
    │ TCP Socket (localhost:9877)
    ▼
Blender Addon (this repo)
    │
    │ bpy API (main thread)
    ▼
Blender
```

## Tool Categories

| Category | Description |
|----------|-------------|
| Scene & Objects | Create, transform, delete objects, manage collections |
| Materials | Principled BSDF material setup |
| Shader Nodes | Full node tree control |
| Lights | Point/Sun/Spot/Area, three-point lighting |
| Modifiers | 22 modifier types (SubSurf, Bevel, Boolean, Array...) |
| Animation | Keyframes, interpolation, actions, NLA |
| Geometry Nodes | Build node networks, scatter setup, array along curve |
| Camera | Lens, DOF, tracking, auto-framing |
| Render | Engine settings, render to file, viewport screenshot |
| Import/Export | FBX, OBJ, GLTF/GLB, USD, STL, DAE, PLY, SVG, ABC |
| UV & Texture | 7 unwrap methods, texture baking |
| Batch Processing | Multi-camera render, turntable |
| Assets | Poly Haven, Sketchfab integration |
| Rigging | Armature, bones, vertex groups, constraints |
| Rig Diagnostics | Rig health check, bone naming fix, weight normalization, bone mirroring |
| Scene Utilities | Scene cleanup, batch rename, apply transforms, mesh analysis |
| Workflows | One-command PBR material, studio render setup, export preparation |

## Lazy Loading

Only 15 core tools are loaded initially. Use `list_tool_categories()` to see all categories, then `enable_tools(category)` to activate on demand.

### Eager mode (for clients without `tools/list_changed` support)

Some MCP clients — notably **VS Code GitHub Copilot Chat** — ignore the `notifications/tools/list_changed` message that `enable_tools()` sends, so newly activated tools never become visible in the tool picker. If you hit this, launch the server with `BLENDER_MCP_PRO_EAGER=1` to pre-register every category at startup:

```json
{
  "mcpServers": {
    "blender-mcp-pro": {
      "command": "python",
      "args": ["<path>/server.py"],
      "env": {
        "BLENDER_MCP_PRO_EAGER": "1"
      }
    }
  }
}
```

(Gumroad customers: also include `"BLENDER_MCP_PRO_LICENSE": "YOUR-LICENSE-KEY"` in the `env` block.)

Claude Desktop and Claude Code handle `list_changed` correctly and do not need this flag.

## License

- **Blender Addon** (`addon/`) — MIT License
- **MCP Server** — Proprietary. Distributed via [Gumroad](https://y1uda.gumroad.com/l/bmp) and [itch.io](https://y1uda.itch.io/blender-mcp-pro).

## Author

[@youichi-uda](https://github.com/youichi-uda)
