<p align="center">
  <img src="assets/logo.svg" alt="Kismet" width="140">
</p>

# Kismet

An open-source AI agent for Unreal Engine. Kismet runs inside the editor and
edits Blueprints, Animation Blueprints, Materials and UMG widgets, then checks
its work with the compiler.

- Runs on your own model provider (Anthropic, OpenAI, Google, DeepSeek, Z.ai,
  Moonshot, MiniMax, OpenRouter, or local models through Ollama and LM Studio).
- No Kismet account is required.
- Includes a local [MCP server](#use-with-claude-code-codex-or-cursor-mcp), so
  Claude Code, Codex, Cursor and other MCP clients can use the same tools.
- Unreal Engine 5.6, 5.7, 5.8 and 5.9 on macOS (Apple Silicon) and Windows.

Website: <https://kismetai.io> · Docs: <https://kismetai.io/docs> · Discord: <https://discord.gg/tMaJbWHSEs>

## Install

Get a build for your engine version and platform from
<https://kismetai.io/download> or from [Releases](../../releases), and follow
[KismetAI/INSTALL.md](KismetAI/INSTALL.md).

Each release comes as ready-to-run binaries, and as the same build with full
source. Use the source variant if you compiled the engine yourself or package a
game with the plugin enabled.

## Use with Claude Code, Codex or Cursor (MCP)

Kismet is also a [Model Context Protocol](https://modelcontextprotocol.io)
server. With the editor running, any MCP client can read, edit and compile
Blueprints, materials and widgets using its own model. Nothing extra to install.

- Endpoint: `http://127.0.0.1:8323/mcp` (Streamable HTTP, this computer only)
- Auth: `Authorization: Bearer <token>`, read from `~/.kismet/mcp_token`

Create the token by calling the endpoint once (a 401 reply is expected), then
connect a client. For Claude Code:

```sh
curl -s -o /dev/null -X POST http://127.0.0.1:8323/mcp
claude mcp add --transport http kismetai http://127.0.0.1:8323/mcp \
  --header "Authorization: Bearer $(cat ~/.kismet/mcp_token)"
```

Reading works straight away. Changing assets needs a grant from the editor
console, limited to a folder:

```
KismetAI.Authority.Grant mcp edit,create /Game/Sandbox
```

Full setup, other clients and limits: <https://kismetai.io/docs/mcp-server>.

## Build from source

The plugin is the [`KismetAI/`](KismetAI) folder. Copy or link it to
`<YourProject>/Plugins/KismetAI`, then build your project's Editor target:

```sh
git clone https://github.com/kismetai-io/Kismet.git
ln -s "$PWD/Kismet/KismetAI" /path/to/YourProject/Plugins/KismetAI
```

On Windows, copy the folder or use `mklink /D`. Build commands for each platform
are in [KismetAI/INSTALL.md](KismetAI/INSTALL.md).

## Repository layout

| Path | What it is |
| --- | --- |
| [`KismetAI/`](KismetAI) | The plugin: source, configuration and packaging script |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Coding rules, building and running the tests |
| [`MAINTAINING.md`](MAINTAINING.md) | Supported versions, merge checks and cutting a release |
| [`SECURITY.md`](SECURITY.md) | How to report a vulnerability |
| [`server.json`](server.json) | MCP Registry entry for the built-in MCP server |

## License

The plugin is licensed under the [Apache License 2.0](LICENSE), from version
0.10.0. Third-party notices are in [KismetAI/NOTICE.md](KismetAI/NOTICE.md).

Releases tagged `v0.9.1` and earlier predate the open-source release. They are
binaries only and remain under the license included in each archive.

Unreal Engine is licensed separately by Epic Games. Kismet is independent and
is not sponsored or endorsed by Epic Games. The Kismet name and logo are not
licensed as trademarks by the Apache license.
