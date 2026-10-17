# gpt-image-2-mcp

An MCP server that exposes OpenAI's **gpt-image-2** (released 2026-04-21) to any MCP client — Claude Desktop, Claude Code, Cursor, MCP Inspector, etc.

Six tools:

| Tool | What it does |
|---|---|
| `generate_image` | text → image |
| `edit_image` | 1–8 reference images (+ optional mask) → image |
| `start_edit_session` | begin an iterative multi-turn edit |
| `continue_edit_session` | apply another refinement turn — previous output becomes the new input |
| `end_edit_session` | release a session |
| `list_edit_sessions` | show active sessions |

Every generated image is **saved to disk** and **returned inline** so the calling model sees it.

## Requirements

- Node.js ≥ 22 (required by `openai` v7)
- An OpenAI API key on an org with `gpt-image-2` access (Organization Verification may be required)

## Install

```bash
pnpm install
pnpm run build
```

This produces `build/index.js`, which is the server entry point.

## Configure a client

### Claude Desktop

Edit `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "gpt-image-2": {
      "command": "node",
      "args": ["/absolute/path/to/gpt_image_2_mcp/build/index.js"],
      "env": {
        "OPENAI_API_KEY": "sk-..."
      }
    }
  }
}
```

### Claude Code

Either add to `~/.claude.json` under `mcpServers` with the same shape, or drop an `.mcp.json` next to your project:

```json
{
  "mcpServers": {
    "gpt-image-2": {
      "command": "node",
      "args": ["/absolute/path/to/gpt_image_2_mcp/build/index.js"],
      "env": { "OPENAI_API_KEY": "sk-..." }
    }
  }
}
```

### MCP Inspector (interactive testing)

```bash
pnpm run inspect
```

Launches the official inspector UI pointed at your local build.

## Environment variables

| Var | Required | Purpose |
|---|---|---|
| `OPENAI_API_KEY` | ✅ | Auth |
| `OPENAI_BASE_URL` |  | Override for proxies / enterprise routes |
| `OPENAI_ORG_ID` |  | Forwarded as `organization` |
| `OPENAI_PROJECT_ID` |  | Forwarded as `project` |
| `GPT_IMAGE_2_OUTPUT_DIR` |  | Global default for where images are saved. Absolute paths used as-is, relative resolved from CWD. |
| `GPT_IMAGE_2_MCP_DEBUG` |  | Set to `1` to emit verbose debug logs on stderr. |
| `GPT_IMAGE_2_SESSION_MAX` |  | Max concurrent in-memory edit sessions, LRU-evicted beyond this (default 20; `0` = no cap). |
| `GPT_IMAGE_2_SESSION_TTL_MS` |  | Idle TTL before an edit session is swept (default 3600000 = 1h; `0` = never expire). |
| `OPENAI_FORCE_RESPONSES_EDITS` |  | Set to `1` to pin edits to the Responses-API fallback route instead of `/v1/images/edits`. See **Edit routing** below. |
| `OPENAI_RESPONSES_EDIT_MODEL` |  | Host model used by the Responses-API **fallback** edit route (default `gpt-4.1-mini`). See **Edit routing** below. |

## Where images go

Unless overridden, each tool writes to:

```
<OS config dir>/gpt-image-2-mcp/output/<project-name>-<hash>/
```

- macOS/Linux: `~/.config/gpt-image-2-mcp/output/<project>-<hash>/`
- Windows: `%APPDATA%\gpt-image-2-mcp\output\<project>-<hash>\`

`<project>-<hash>` is derived from the git root (if any) or the current working directory — each project gets its own folder so generations don't collide.

**Per-call override:** pass `output_dir: "/some/path"` to any tool.

Filenames look like `image-20260422-150301-a1b2c3.png`. If you pass `filename_prefix: "hero-banner"`, it becomes `image-20260422-150301-a1b2c3-hero-banner.png`.

## What the tools return

Every tool result contains:

1. An inline `ImageContent` block per generated image (so the LLM sees the image)
2. A text summary: applied settings, file path, token usage, estimated cost
3. `structuredContent` for programmatic consumers:

```json
{
  "model": "gpt-image-2",
  "prompt": "…",
  "requested": { "size": "auto", "quality": "auto", "n": 1, "format": "png" },
  "applied":   { "size": "1024x1024", "quality": "high", "background": "opaque", "output_format": "png" },
  "images": [ { "file_path": "…", "filename": "…", "size_bytes": 123456, "mime_type": "image/png" } ],
  "usage":   { "input_tokens": …, "output_tokens": …, "total_tokens": …, "input_tokens_details": { … } },
  "cost_usd_estimated": 0.2112
}
```

Session tools additionally return `session_id` and `turn`.

## Sizes

Default is `auto` (the model picks). You can pass:

- A preset: `1024x1024`, `1536x1024`, `1024x1536`
- Any custom `WxH` where:
  - Both edges are multiples of 16
  - Max edge ≤ 3840px (OpenAI labels outputs above 2560×1440 experimental; those still generate, and the tool result carries a note saying so)
  - Aspect ratio within 1:3 and 3:1
  - Total pixels between 655,360 and 8,294,400

Invalid sizes fail **before** the API call with a clear error — no wasted requests.

## Transparent backgrounds

Pass `background: "transparent"` to any generate or edit tool to get an alpha channel.

OpenAI added transparency to gpt-image-2 on 2026-08-20 and still labels it **preview**. Two rules:

- `output_format` must be `png` or `webp`. JPEG has no alpha channel, and the API rejects the combination with `400 invalid_transparent_background_output_format`. This server checks it first and returns a clear tool error instead.
- On `continue_edit_session` the check uses the **effective** format — if you omit `output_format`, the session's own format applies, so a JPEG session rejects a transparent request rather than failing at OpenAI.

The other two values are unchanged: `auto` (default, model decides) and `opaque` (always filled).

> Versions ≤ 0.3.0 of this server refused `transparent` outright, because gpt-image-2 genuinely did not support it before 2026-08-20.

## Iterative editing example

```
start_edit_session    prompt: "A coastal lighthouse at dawn, photorealistic", images: ["./sketch.png"]
  → session_id: edit-1761149123-a1b2c3d4, turn 1, saved to …/session-…-turn1.png

continue_edit_session session_id: "edit-…-a1b2c3d4", prompt: "Make the sky more orange. Keep everything else the same."
  → turn 2

continue_edit_session session_id: "edit-…-a1b2c3d4", prompt: "Add a small boat on the horizon."
  → turn 3

end_edit_session      session_id: "edit-…-a1b2c3d4"
```

Sessions are **in-memory only** and discarded on server restart — this is intentional (keeps the server stateless on the wire) and mirrors the Gemini MCP pattern.

## Image inputs for `edit_image` and `start_edit_session`

Accepts any mix of:

- Absolute path: `/Users/me/photo.png`
- Relative path: `./photo.png` (resolved from CWD)
- `file:///Users/me/photo.png`
- `https://example.com/photo.png` (downloaded, size-capped)
- `data:image/png;base64,iVBOR…`

Up to 8 images per call. Each ≤ 50MB. PNG/WEBP/JPG supported.

## Cost guardrails

The server ships **no hard spending limits** — you should watch your OpenAI usage dashboard. Each tool result includes an estimated cost in USD computed from the token usage returned by the API, plus an approximate pre-flight estimate logged to stderr.

Rough per-image cost at common sizes:

| Quality | 1024×1024 | 1024×1536 / 1536×1024 |
|---|---|---|
| low | ~$0.006 | ~$0.005 |
| medium | ~$0.053 | ~$0.041 |
| high | ~$0.211 | ~$0.165 |

Custom sizes scale with pixel count. Edit calls additionally tokenize input images at high fidelity — large reference images are expensive.

## Edit routing

`edit_image`, `start_edit_session`, and `continue_edit_session` call `POST /v1/images/edits` directly. This is the canonical endpoint: it supports `n > 1`, masks, and returns accurate per-call token usage for cost estimation.

> **History:** at launch (2026-04-21) the endpoint rejected `gpt-image-2` (and `gpt-image-1.5`) with `400 Invalid value: 'gpt-image-2'. Value must be 'dall-e-2'.` — an OpenAI-side bug. Versions ≤ 0.2.0 of this server therefore routed edits through the Responses API by default. OpenAI fixed the endpoint silently in early May 2026 (verified live 2026-06-11), and since 0.3.0 the direct endpoint is the default again.

The Responses-API workaround is kept as a **fallback** (`src/utils/edit-via-responses.ts`):

- It engages automatically if the direct endpoint ever returns the launch-era 400 again (matched narrowly; the rejection is remembered for 10 minutes so only the first call in that window pays the failed attempt, then the direct endpoint is re-probed).
- Set `OPENAI_FORCE_RESPONSES_EDITS=1` to pin it explicitly.
- The legacy `OPENAI_USE_DIRECT_EDITS` toggle from 0.2.0 is deprecated and ignored (its only meaningful setting was `1` — opt into the direct endpoint, which is now the default).

Fallback mechanics: input images are uploaded via the Files API (`purpose: "vision"`), a cheap host model (default `gpt-4.1-mini`, override with `OPENAI_RESPONSES_EDIT_MODEL`) is forced to invoke the `image_generation` tool, the base64 result is extracted, and uploaded files are deleted afterwards.

**Fallback trade-offs versus the direct endpoint** (only apply when the fallback is active — the tool result carries `route: "responses"` and a note when they do):

- `n > 1` is not supported — the Responses path returns one image per call.
- Cost accounting undercounts — `usage` only reports the host chat model's text tokens; the image tool is billed separately (~$0.04–0.05 extra for a 1024×1536 medium edit).
- Masks still work — uploaded and referenced via `input_image_mask.file_id`.

## Troubleshooting

- **"OPENAI_API_KEY is not set"** — add it to the `env` block of your MCP config.
- **`403 / organization verification`** — gpt-image-2 may require Organization Verification on your OpenAI org. Check the dashboard.
- **`429`** — you hit the IPM (images per minute) cap for your tier. Lower `n`, or wait.
- **Image doesn't appear in the client** — check the file path in the text block; the image is saved regardless of inline display.
- **Protocol disconnects silently** — something printed to stdout. Check `src/**/*.ts` — all logs must use `utils/logger.ts` (stderr). This is the single biggest MCP footgun.

## Development

```bash
pnpm run dev         # tsx watch
pnpm run typecheck   # tsc --noEmit
pnpm run build       # compile to build/
pnpm run inspect     # launch MCP Inspector
```

## License

MIT
