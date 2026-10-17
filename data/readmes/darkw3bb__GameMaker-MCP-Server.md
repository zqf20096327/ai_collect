# GM-Maker MCP Server

> **Build GameMaker projects with AI in Cursor**

An [MCP (Model Context Protocol)](https://modelcontextprotocol.io/) server that brings GameMaker Studio development directly into your AI-powered workflow. Create YYP projects, add scripts, objects, and sprites using natural language in [Cursor IDE](https://cursor.com/).

## 🎮 What This Does

This server exposes GameMaker project manipulation as MCP tools, letting you:
- **Create** new GameMaker YYP projects from scratch
- **Add** GML scripts with your code
- **Create** objects with event definitions
- **Import** sprite animations from image sequences
- **List** and manage project resources
- **Maintain** proper YYP/YY file structure automatically

All through natural language conversations with AI in Cursor.

## 🙏 Attribution

This project is built on the excellent work by **[Butterscotch Shenanigans](https://www.bscotch.net/)**, the indie game studio behind *Crashlands*, *Levelhead*, and other amazing games. They've open-sourced their entire GameMaker tooling suite called **[Stitch](https://github.com/bscotch/stitch)**.

Specifically, this MCP server uses:
- **[@bscotch/yy](https://github.com/bscotch/stitch/tree/main/packages/yy)** - Robust parsing and writing of GameMaker YY/YYP files
- Their extensive TypeScript type definitions for GameMaker resources
- Their battle-tested approach to programmatic GameMaker project manipulation

Without their incredible open-source contributions to the GameMaker ecosystem, this project wouldn't be possible. **Thank you, Butterscotch Shenanigans! 🧈**

## 💡 How This Was Made

### Origin Story

This MCP server was created while building **Soulbound**, a game project that needed better AI-assisted GameMaker development workflows in Cursor. The goal was simple: make Cursor understand GameMaker projects so it could help write GML code, create objects, and manage resources without breaking the YYP structure.

Instead of manually creating GameMaker resources and switching between the IDE and Cursor, this tool lets you stay in the AI-powered flow and have Cursor handle the tedious project setup work.

### Technical Architecture

This MCP server bridges GameMaker Studio development with modern AI-assisted workflows:

1. **Foundation**: Built on Butterscotch's [@bscotch/yy](https://github.com/bscotch/stitch) library, which provides safe, validated reading and writing of GameMaker's JSON-like YY/YYP file formats.

2. **MCP Protocol**: Implements the [Model Context Protocol](https://modelcontextprotocol.io/) from Anthropic, which allows AI assistants to call structured tools via a standard interface.

3. **Cursor Integration**: Configured to run as a stdio-based MCP server that Cursor can launch and communicate with, exposing GameMaker operations as callable tools.

4. **Type Safety**: Written in TypeScript with full type definitions from the @bscotch packages, ensuring robust file generation.

5. **Architecture**: Each tool (create_project, add_script, etc.) follows a consistent pattern:
   - Validate parameters with Zod schemas
   - Load existing YYP or create new project structure
   - Generate proper YY resource files
   - Update YYP resource registry
   - Write everything back using Butterscotch's safe write methods

The result: You can now say "create a player object with a step event" in Cursor, and the AI will generate a proper GameMaker object with all the right YY file structure, registered in the YYP, ready to open in GameMaker Studio.

**Born from real game development needs**, this tool makes AI-assisted GameMaker development actually practical.

## Features

### Available Tools

- **create_project** - Scaffold a new .yyp project
- **add_script** - Create a GML script and register it in the YYP
- **add_object** - Create a .yy object with optional event stubs
- **add_sprite_from_images** - Import frames from a directory and register a sprite
- **list_resources** - Enumerate resources by type (scripts, objects, sprites)

## Installation

### Prerequisites

- Node.js 18+ 
- npm or pnpm
- Cursor IDE

### Setup

1. **Clone and install dependencies:**

```bash
cd /Users/webb/Repos/mcp-yyp
npm install
```

2. **Build the server:**

```bash
npm run build
```

3. **Test with MCP Inspector (optional but recommended):**

```bash
npm run inspect
```

This opens the MCP Inspector to validate your tools before using them in Cursor.

## Cursor Configuration

### Option 1: Global Configuration

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "gm-maker": {
      "command": "node",
      "args": ["/Users/webb/Repos/mcp-yyp/dist/index.js"],
      "env": {}
    }
  }
}
```

### Option 2: Project-Local Configuration

Add to `.cursor/mcp.json` in your workspace:

```json
{
  "mcpServers": {
    "gm-maker": {
      "command": "node",
      "args": ["${workspaceFolder}/dist/index.js"]
    }
  }
}
```

### Option 3: Development Mode (TypeScript)

For development with hot-reload:

```json
{
  "mcpServers": {
    "gm-maker": {
      "command": "npx",
      "args": ["tsx", "/Users/webb/Repos/mcp-yyp/src/index.ts"]
    }
  }
}
```

After adding the configuration, restart Cursor to load the MCP server.

## Usage Examples

Once configured, you can use natural language in Cursor to interact with GameMaker projects:

### Creating a New Project

```
"Create a new GameMaker project called MyGame at /Users/webb/Projects/MyGame"
```

Or explicitly:
```
Call gm-maker.create_project with { "projectDir": "/Users/webb/Projects/MyGame", "name": "MyGame" }
```

### Adding a Script

```
"Add a script called player_movement to my GameMaker project at /Users/webb/Projects/MyGame"
```

Or with code:
```
Call gm-maker.add_script with {
  "projectDir": "/Users/webb/Projects/MyGame",
  "scriptName": "player_movement",
  "code": "function move_player(spd) {\n  x += spd;\n}"
}
```

### Adding an Object with Events

```
"Create an object called obj_player with a Create event in my project"
```

Or explicitly:
```
Call gm-maker.add_object with {
  "projectDir": "/Users/webb/Projects/MyGame",
  "objectName": "obj_player",
  "events": [{"eventType": 0, "eventNum": 0}]
}
```

Common GameMaker event types:
- `0` = Create
- `1` = Destroy
- `2` = Alarm
- `3` = Step
- `4` = Collision
- `8` = Draw

### Importing a Sprite

```
"Import PNG frames from /Users/webb/Assets/portal as a sprite called spr_portal"
```

Or explicitly:
```
Call gm-maker.add_sprite_from_images with {
  "projectDir": "/Users/webb/Projects/MyGame",
  "spriteName": "spr_portal",
  "framesDir": "/Users/webb/Assets/portal"
}
```

### Listing Resources

```
"Show me all scripts in my GameMaker project"
```

Or explicitly:
```
Call gm-maker.list_resources with {
  "projectDir": "/Users/webb/Projects/MyGame",
  "kind": "scripts"
}
```

## Development

### Scripts

- `npm run dev` - Run in development mode with tsx
- `npm run build` - Build for production
- `npm run start` - Run built version
- `npm run inspect` - Open MCP Inspector for testing

### Project Structure

```
gm-maker/
├── src/
│   ├── index.ts           # MCP server entrypoint
│   └── gm/
│       ├── types.ts       # TypeScript types
│       ├── yyp.ts         # YYP project operations
│       ├── scripts.ts     # Script creation
│       ├── objects.ts     # Object creation
│       └── sprites.ts     # Sprite creation
├── dist/                  # Built output
├── package.json
├── tsconfig.json
└── README.md
```

## Technical Details

### Dependencies

- **@modelcontextprotocol/sdk** - MCP protocol implementation
- **@bscotch/yy** - Safe GameMaker YY/YYP file parsing and writing
- **zod** - Runtime type validation

### Architecture

This server uses the stdio transport protocol to communicate with Cursor. Each tool:
1. Validates input parameters using Zod schemas
2. Loads the existing YYP file (or creates a new one)
3. Performs file system operations for the resource
4. Updates the YYP resource list
5. Writes the updated YYP back to disk

The [@bscotch/yy](https://github.com/bscotch/stitch) library ensures all YY/YYP files maintain proper structure and don't get corrupted.

## Limitations & Future Enhancements

Current limitations:
- Sprite metadata (width, height, bbox) uses defaults - manual adjustment may be needed
- No support for rooms, sounds, or other advanced resources yet
- Event GML files are created with stub comments

Potential enhancements:
- Add `update_script` to modify existing script code
- Add `delete_resource` for removing resources
- Add `create_room` for room creation
- Add `build_project` using GameMaker CLI/Igor
- Integration with @bscotch/gml-parser for code refactoring

## 🔗 References & Resources

### Core Technologies
- **[Butterscotch Stitch Monorepo](https://github.com/bscotch/stitch)** - The foundation this project is built on
- **[@bscotch/yy Package](https://github.com/bscotch/stitch/tree/main/packages/yy)** - GameMaker file parsing/writing
- **[Model Context Protocol](https://modelcontextprotocol.io/)** - The protocol specification
- **[Cursor MCP Documentation](https://docs.cursor.com/advanced/mcp)** - How to use MCP in Cursor

### GameMaker Resources  
- **[GameMaker Manual](https://manual.gamemaker.io/)** - Official GameMaker documentation
- **[Butterscotch Shenanigans](https://www.bscotch.net/)** - The studio behind the tooling
- **[Butterscotch Blog](https://www.bscotch.net/news)** - Great articles on GameMaker workflows

## 🤝 Contributing

This is an experimental project exploring AI-assisted GameMaker development. Contributions, ideas, and feedback are welcome!

**Areas for improvement:**
- Additional resource types (rooms, sounds, shaders, etc.)
- Better sprite metadata handling
- GML code parsing and refactoring
- Project build automation
- Integration with GameMaker CLI/Igor

## 📄 License

MIT License - See LICENSE file for details

## ❤️ Special Thanks

- **[Butterscotch Shenanigans](https://github.com/bscotch)** for creating and open-sourcing Stitch
- **[Anthropic](https://www.anthropic.com/)** for the Model Context Protocol
- **[Cursor](https://cursor.com/)** for pioneering AI-first IDE experiences
- The **GameMaker community** for being awesome

---

*Built with ☕ while developing Soulbound. Created for the GameMaker community. Made possible by Butterscotch Shenanigans' amazing open-source tools.*

