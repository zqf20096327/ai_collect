# Free Claude AI Image Generator

Claude has no built-in image-generation model — ask it to draw something and
it will tell you so. This repo shows how to give Claude that ability for
free, using [muapi](https://muapi.ai)'s MCP server as the missing tool: a
single API key, one `claude mcp add` command, and Claude can call 500+
image/video/audio models on your behalf, including GPT Image 2, Nano Banana
Pro, and Z-Image Turbo.

Sandbox API keys are free and instant (mock output, no credit card) so you
can wire everything up and test the flow before spending anything on a real
generation.

<p align="center"><a href="https://youtu.be/72ng1tSD0kY"><img src="https://i.ytimg.com/vi/72ng1tSD0kY/maxresdefault.jpg" width="720"></a></p>
<p align="center"><a href="https://youtu.be/72ng1tSD0kY"><b>▶ Watch: Free Claude AI Image Generator (via MCP) — Full Tutorial</b></a></p>

## Related Projects

- [Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) — self-hosted, unrestricted image/video generation studio (600+ models) if you want a full app instead of MCP tool calls from Claude
- [Awesome-GPT-Image-2-API-Prompts](https://github.com/Anil-matcha/Awesome-GPT-Image-2-API-Prompts) — prompt library for GPT Image 2, the model used in this repo's reference-sheet example
- [n8n-nodes-muapi](https://github.com/SamurAIGPT/n8n-nodes-muapi) — same underlying API as no-code n8n nodes, if you want automation without an agent in the loop
- [free-claude-ai-video-generator](https://github.com/Anil-matcha/free-claude-ai-video-generator) — companion MCP setup guide for generating and animating videos with Claude

## Quick start

```bash
# 1. Install the CLI (npm or pip, no separate download needed)
npm install -g muapi-cli
# or: pip install muapi-cli

# 2. Create an account and API key
muapi auth register --email you@example.com --password "..."
muapi auth verify --email you@example.com --otp 123456
muapi auth login --email you@example.com --password "..."

# 3. Register muapi as an MCP server for Claude Code
claude mcp add muapi -e MUAPI_API_KEY=YOUR_MUAPI_KEY -- muapi mcp serve

# 4. Start a new Claude Code session, then verify it's connected
claude mcp list
# muapi: muapi mcp serve - ✔ Connected
```

That's it — Claude can now call `muapi_image_generate`, `muapi_image_edit`,
and the rest of the toolset directly, choosing whichever model fits the ask.

### Claude Desktop

Add the same server to
`~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or
`%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "muapi": {
      "command": "muapi",
      "args": ["mcp", "serve"],
      "env": { "MUAPI_API_KEY": "YOUR_MUAPI_KEY" }
    }
  }
}
```

## What Claude can actually do with this, and what it costs

Once connected, ask Claude to generate or edit images in plain language —
it picks the model, or you can name one yourself. Three real examples,
current pricing as of this repo's last update:

| Ask | Model | Cost |
|---|---|---|
| "Make me a full character reference sheet — front/side/back, expressions, palette" | `gpt-image-2-text-to-image` | $0.09/image |
| "Now edit that — change the armor accents from blue to red" | `nano-banana-pro-edit` | $0.12/generation |
| "Give me 4 quick variants of this character in different settings" | `z-image-turbo` | $0.007/image |

`nano-banana-pro-edit` is also the one to reach for when you want the *same*
character dropped into a brand-new scene — hand it your reference image and
describe the new setting, rather than a small tweak.

Verify current model names and pricing at
[muapi.ai/ai-image-api](https://muapi.ai/ai-image-api) before you build
anything that depends on them — model lineups and prices change.

## Try it without Claude — plain REST example

If you just want to confirm your key works, or call a model directly outside
an agent loop, see [`examples/generate_image.py`](examples/generate_image.py).
It submits a real job to `gpt-image-2-text-to-image`, polls for the result,
and prints the output URL.

```bash
export MUAPI_API_KEY=YOUR_MUAPI_KEY
python examples/generate_image.py "a cyberpunk bounty hunter, glowing blue armor accents, scarred visor helmet"
```

## Sandbox mode — test for free first

Sandbox keys (`is_test=true` when you create a key) return an instant mock
result with no credit deduction, so you can verify your whole MCP/CLI wiring
before spending real money. Once you're ready for a real image, create a
non-sandbox key and swap it in — nothing else about the setup changes.

## Next steps

- Full CLI reference and every available command: [muapi.ai/cli](https://muapi.ai/cli)
- Full MCP server docs (tool list, auth, troubleshooting): see the `docs/mcp.md` in [muapi-cli](https://github.com/SamurAIGPT/muapi-cli)
- Browse the current top-ranked model per image category: [muapi.ai/ai-image-api](https://muapi.ai/ai-image-api)

## License

MIT — see [LICENSE](LICENSE).
