# OpenClaw Unreal Plugin

> MCP (Model Context Protocol) bridge for Unreal Engine — lets AI agents control the Unreal Editor in real time.

**Version 1.3.0**

## Features

- **36 MCP tools** for level, actor, transform, component, editor, debug, input, asset, console, and blueprint control
- **Editor Panel** — Window → OpenClaw Unreal Plugin: a dockable tab showing connection status, MCP info, connect/disconnect buttons, and a live log
- **Real-time control** of the Unreal Editor from any MCP-compatible AI agent
- **Zero config** — install the plugin, connect OpenClaw, and go

## Installation

1. Copy the `OpenClaw` folder into your project's `Plugins/` directory
2. Restart the Unreal Editor
3. Enable the plugin in Edit → Plugins if not already enabled
4. Open the panel: **Window → OpenClaw Unreal Plugin**

## Tools (36)

### Level
| Tool | Description |
|------|-------------|
| `level.getCurrent` | Get the current level name |
| `level.list` | List all levels in the project |
| `level.open` | Open a level by name |
| `level.save` | Save the current level |

### Actor
| Tool | Description |
|------|-------------|
| `actor.find` | Find actors by name or class |
| `actor.getAll` | Get all actors in the level |
| `actor.create` | Create an actor (StaticMeshActor/Cube, Sphere, Cylinder, Cone, PointLight, Camera) |
| `actor.delete` | Delete an actor by name |
| `actor.getData` | Get detailed actor data |
| `actor.setProperty` | Set actor properties via UE reflection system |

### Transform
| Tool | Description |
|------|-------------|
| `transform.getPosition` | Get actor position |
| `transform.setPosition` | Set actor position |
| `transform.getRotation` | Get actor rotation |
| `transform.setRotation` | Set actor rotation |
| `transform.getScale` | Get actor scale |
| `transform.setScale` | Set actor scale |

### Component
| Tool | Description |
|------|-------------|
| `component.get` | Get component data from an actor |
| `component.add` | Add a component to an actor |
| `component.remove` | Remove a component from an actor |

### Editor
| Tool | Description |
|------|-------------|
| `editor.play` | Start Play-In-Editor (uses RequestPlaySession) |
| `editor.stop` | Stop Play-In-Editor |
| `editor.pause` | Pause Play-In-Editor |
| `editor.resume` | Resume Play-In-Editor |
| `editor.getState` | Get current editor state |

### Debug
| Tool | Description |
|------|-------------|
| `debug.hierarchy` | Get the actor hierarchy tree |
| `debug.screenshot` | Take an editor screenshot |
| `debug.log` | Write to the output log |

### Input
| Tool | Description |
|------|-------------|
| `input.simulateKey` | Simulate a key press |
| `input.simulateMouse` | Simulate mouse input |
| `input.simulateAxis` | Simulate axis input |

### Asset
| Tool | Description |
|------|-------------|
| `asset.list` | List assets in a path |
| `asset.import` | Import an external asset |

### Console
| Tool | Description |
|------|-------------|
| `console.execute` | Execute a console command |
| `console.getLogs` | Read project log file (supports `count` and `filter` params) |

### Blueprint
| Tool | Description |
|------|-------------|
| `blueprint.list` | List blueprints in the project |
| `blueprint.open` | Open a blueprint in the editor |

## Connection Modes

### Mode A: OpenClaw Gateway (Remote Access)

```
Telegram/Discord/Web → OpenClaw Gateway → HTTP Polling → Unreal Plugin
```

Works when the Gateway is running and this editor can read the gateway's bridge
token (`~/.openclaw/unreal-bridge.token`). Requires openclaw-unreal-skill 1.2.0+.

### Mode B: MCP Direct (Claude Code / Cursor)

```
Claude Code / Cursor → MCP Server (stdio) → HTTP → Unreal Plugin (port 27184)
```

The plugin runs an embedded HTTP server on port **27184**, authenticated with a
per-launch token (see [Bridge authentication](#bridge-authentication-v140)). Use
the included MCP bridge, which reads the token file for you:

**Claude Code:**
```bash
claude mcp add unreal -- node /path/to/Plugins/OpenClaw/MCP~/index.js
```

**Cursor:** Add to `.cursor/mcp.json`:
```json
{
  "mcpServers": {
    "unreal": {
      "command": "node",
      "args": ["/path/to/Plugins/OpenClaw/MCP~/index.js"]
    }
  }
}
```

Both modes run simultaneously — you can use Gateway and MCP Direct at the same time.

## Editor Panel

Access via **Window → OpenClaw Unreal Plugin**. The dockable panel provides:

- **Status indicator** — connection state at a glance
- **MCP info** — server address and protocol details
- **Connect / Disconnect** buttons
- **Live log** — scrollable log of MCP messages and tool calls

## Troubleshooting

### Plugin not loading or stale binaries

If the plugin fails to load, shows outdated behavior, or you get linker errors after updating, clear the build cache:

```bash
rm -rf YourProject/Plugins/OpenClaw/Binaries YourProject/Plugins/OpenClaw/Intermediate
```

Then restart the Unreal Editor — it will recompile the plugin from source.

### Connection issues

1. Make sure OpenClaw Gateway is running (`openclaw gateway status`)
2. Check the Editor Panel log for error messages
3. Verify firewall isn't blocking the MCP port

## 🎭 AI Personas for Game Development

Want your AI agent to have a consistent personality while developing your game? [ClawSouls](https://clawsouls.ai) provides open-source persona packages (Soul Spec) that work with OpenClaw and other AI frameworks. Give your coding assistant a specialized game dev personality, or create custom NPC behavior profiles.

- Browse community souls: [clawsouls.ai](https://clawsouls.ai)
- Soul Spec standard: [soulspec.org](https://soulspec.org)
- Quick start: `npx clawsouls init my-game-dev --spec 0.4`

## License

This project has been licensed under [Apache-2.0](LICENSE) since its initial release.
Copyright 2026 Tom Lee (TomLeeLive)

## Bridge authentication (v1.4.0)

Both local bridges are authenticated with a per-launch secret. Neither accepts an
anonymous caller any more.

### MCP Direct — this plugin is the server

When the embedded server starts it generates a per-launch token and writes it to
`~/.openclaw/unreal-mcp-bridge.token` with mode `0600`. The bundled
`MCP~/index.js` reads that file and sends it as `X-OpenClaw-Token` on every
request; anything else gets **401**. Requests carrying `Origin` or `Referer` get
**403** (local MCP clients never send them; a web page probing the port does), and
so do non-loopback peers on engine versions that report the peer address — `GET
/status` says which, as `peerCheck: "loopback-only" | "unavailable"`. The
mandatory token is the control that does not depend on the engine version.

In v1.3.1 the token was **optional** (`OPENCLAW_BRIDGE_TOKEN` unset meant no
auth), so an unconfigured install accepted commands from any local process. That
is what changed.

### Gateway — this plugin is the client

When the OpenClaw gateway loads the Unreal extension it writes a token to
`~/.openclaw/unreal-bridge.token` (mode `0600`). This plugin reads it and sends it
as `X-OpenClaw-Bridge-Token` on `POST /unreal/register`; the gateway answers with
a per-session token that every later request carries as `X-OpenClaw-Session`.
Every queued command has a nonce, and this plugin echoes it with the result, so no
other local process can answer in the editor's place. Needs
**openclaw-unreal-skill 1.2.0** on the gateway side.

### Variables

| Variable | Effect |
|----------|--------|
| `OPENCLAW_CONFIG_DIR` / `OPENCLAW_HOME` | Where both token files live (default `~/.openclaw`) |
| `OPENCLAW_BRIDGE_TOKEN` | Use this token instead of the files, on both sides |
| `OPENCLAW_UNREAL_ALLOW_LEGACY_UNAUTHENTICATED=1` | Restore the pre-1.4.0 unauthenticated MCP Direct server. Off by default; the output log and the OpenClaw panel say so loudly while it is on. |

Tokens are never written to the output log — only the token file's path is. The
`0600` file keeps other users out; a process running as **you** can read it, which
is the same boundary that protects your SSH keys. On Windows the file relies on
the user profile ACL, since `chmod` does not apply.
