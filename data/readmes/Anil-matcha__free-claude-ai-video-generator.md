# Free Claude AI Video Generator

Give Claude video generation through Muapi's MCP server. Connect Claude Code to `muapi-cli`, then ask it to generate a clip from text or animate an image using Muapi's `muapi_video_generate` and `muapi_video_from_image` tools.

[Muapi](https://muapi.ai) · [Free Claude AI Video Generator guide](https://muapi.ai/free-claude-ai-video-generator) · [Video model catalog](https://muapi.ai/ai-video-api) · [Create an API key](https://muapi.ai/access-keys) · [CLI and MCP docs](https://muapi.ai/cli)

## Related Projects

- [free-claude-ai-image-generator](https://github.com/Anil-matcha/free-claude-ai-image-generator) — the companion Claude image workflow.
- [AI-Video-API](https://github.com/Anil-matcha/AI-Video-API) — compare Muapi video API endpoints and direct REST calls.
- [Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) — a desktop and web app for working with image and video models.

## What you can do

- Generate a video from a text prompt with `muapi_video_generate`.
- Animate a public image URL with `muapi_video_from_image`.
- Choose from Muapi's available text-to-video and image-to-video models.
- Test the connection with a free sandbox API key. Sandbox responses are mock results, not rendered videos.

Claude does not render video itself. It interprets your request and calls the connected MCP tool; Muapi submits the generation to the selected model. Real generations are charged according to model, duration, resolution, and options. Check the [current catalog and pricing](https://muapi.ai/ai-video-api) before estimating a job.

## Connect Claude Code

### 1. Install the Muapi CLI

Requires Node.js/npm or Python/pip:

```bash
npm install -g muapi-cli
# Or: pip install muapi-cli
```

### 2. Create an API key

Create a key at [muapi.ai/access-keys](https://muapi.ai/access-keys). Enable sandbox mode to test the MCP connection without spending credits. Sandbox mode returns mock output and does not render a video.

### 3. Register the MCP server

```bash
claude mcp add muapi -e MUAPI_API_KEY=YOUR_MUAPI_KEY -- muapi mcp serve
claude mcp list
```

Start a new Claude Code session and confirm `muapi` is connected. Keep the API key in the environment/configuration; do not paste it into prompts or commit it to a project.

### 4. Ask Claude for a clip

For example:

> Generate a 5-second cinematic shot of a red fox crossing a snowy forest at dawn. Use a 16:9 frame and smooth tracking camera movement.

Or animate an image:

> Animate this image into a 5-second clip. Keep the subject consistent and add a slow camera push-in: https://example.com/my-image.jpg

Claude selects and calls the relevant Muapi video tool. You can request a specific model when you know which one you want.

## Tool inputs

The MCP tools accept these common inputs. Model-specific options vary; check the model's schema before relying on additional fields.

| Tool | Required inputs | Common optional inputs |
|---|---|---|
| `muapi_video_generate` | `prompt` | `model`, `duration`, `aspect_ratio` |
| `muapi_video_from_image` | `prompt`, `image_url` | `model`, `duration`, `aspect_ratio`, `end_image_url`, `last_image_url` |

Use a publicly reachable image URL for `image_url`. For models that support start/end frames, `end_image_url` or `last_image_url` can provide the final frame. Availability and accepted values depend on the chosen model.

## Direct REST example

The MCP server is convenient for Claude. You can also call a video endpoint directly. This example submits a text-to-video task and polls for completion:

```bash
export MUAPI_API_KEY="your-key"

curl -sS -X POST "https://api.muapi.ai/api/v1/seedance-2.5-text-to-video" \
  -H "Content-Type: application/json" \
  -H "x-api-key: ${MUAPI_API_KEY}" \
  -d '{
    "prompt": "A red fox crosses a snowy forest at dawn, cinematic tracking shot",
    "duration": 5,
    "aspect_ratio": "16:9"
  }'
```

The submission response includes a request ID. Poll it with:

```bash
curl -sS "https://api.muapi.ai/api/v1/predictions/${REQUEST_ID}/result" \
  -H "x-api-key: ${MUAPI_API_KEY}"
```

Poll until the task reaches a terminal state, then read the result URLs from the response. Replace the example endpoint and fields with the current schema for your selected model. Do not resubmit a billable request just because a poll timed out; first check the original request ID.

For an image-to-video REST example and endpoint-specific fields, see the [AI Video API guide](https://github.com/Anil-matcha/AI-Video-API).

## Claude Desktop and other MCP clients

Muapi CLI includes a stdio MCP server that can be configured in MCP-compatible applications. The exact settings screen and configuration file vary by client. Follow that client's stdio-server instructions and provide `muapi mcp serve` as the command, with `MUAPI_API_KEY` set in its environment. See the [Muapi MCP documentation](https://muapi.ai/cli) for current setup details.

## Troubleshooting

- **Server is disconnected:** run `claude mcp list`, verify the CLI is installed, and restart the Claude Code session after registering the server.
- **Authentication fails:** check that `MUAPI_API_KEY` is set in the MCP server environment and that the key is active.
- **Sandbox output is not a video:** expected behavior. Sandbox keys return mock output; use a regular key for real generation.
- **Image animation fails:** confirm the image URL is publicly reachable and supported by the selected model.
- **A model rejects an option:** model inputs differ. Check its current schema in the [video catalog](https://muapi.ai/ai-video-api) and remove unsupported fields.
- **A task is still processing:** poll the returned request ID; generation is asynchronous.

## Security and cost

- Never commit API keys. Use environment variables or your MCP client's protected environment settings.
- Sandbox keys are for free wiring checks and return mock results.
- Real model calls consume credits. Video pricing can vary by model, duration, resolution, and options; verify the live [Muapi video catalog](https://muapi.ai/ai-video-api) before running a batch.
- Treat generated asset URLs as output links that may have limited retention. Download outputs you need to keep.

## License

MIT. See [LICENSE](LICENSE).
