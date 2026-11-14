# agy-bridge

Run **Google Antigravity** on any third-party LLM — OpenRouter, Together, Groq, a local vLLM, Ollama,
or anything else that speaks OpenAI `/chat/completions`.

Antigravity is not hardwired to Gemini. Its CLI talks the public Gemini API and its IDE talks the
Cloud Code API; both accept an endpoint override. `agy-bridge` sits on that override and translates
the Gemini wire format into an OpenAI-compatible one, including streaming and full tool calling.

```
Antigravity CLI ──Gemini v1beta──┐
                                 ├──► agy-bridge ──OpenAI /v1/chat/completions──► your model
Antigravity IDE ──Cloud Code─────┘
```

![Antigravity IDE editing a project while the model picker reports which upstream is serving it](docs/images/antigravity-ide.png)

*Antigravity IDE, mid-task. The picker at the bottom reads `Claude Opus 4.6 (Thinking) · DeepSeek-V4.1-Flash-1017`:
the client thinks it is talking to Google, while every generated token comes from the configured upstream.*

## Why

Antigravity's agent loop is good; its model list is not yours. Pointing the app at your own gateway
keeps your quota, your model choice and your keys under your control, with the native tool schema,
streaming and multi-turn loop intact.

## Features

- **Two protocols, one binary.** Public Gemini (`v1beta/models/{model}:generateContent`) for the CLI,
  Cloud Code (`v1internal:*`) for the IDE and its hub.
- **Streaming.** OpenAI SSE deltas are re-framed as Gemini SSE chunks, reasoning included.
- **Tool calling.** Gemini `functionDeclarations` map 1:1 onto OpenAI `tools`; tool results flow back
  as `role: tool` messages with synthesised call ids.
- **Selective proxying.** On the Cloud Code route only generation is rerouted; sign-in, the model
  catalog and quota calls are forwarded verbatim to Google with the caller's own token.
- **No dependencies.** Standard library only, one static binary for Linux, macOS and Windows.

## Quick start

### Prebuilt binaries

Download from [Releases](https://github.com/codewith-aditya/agy-bridge/releases) — Linux (x86-64,
ARM64), Windows x86-64, macOS (Apple Silicon, Intel) — and verify with `SHA256SUMS`. No Go toolchain
needed.

### Hosted

```bash
export GOOGLE_GEMINI_BASE_URL=https://your-host/agy
export GEMINI_API_KEY=<your-upstream-key>
agy
```

`~/.gemini/config/settings.json` must contain:

```json
{ "modelProvider": "gemini" }
```

### Self-hosted

```bash
make build
UPSTREAM_BASE=https://api.openai.com/v1 UPSTREAM_KEY=sk-... DEFAULT_MODEL=gpt-4o-mini ./bin/agy-bridge
```

```bash
GOOGLE_GEMINI_BASE_URL=http://127.0.0.1:8198 GEMINI_API_KEY=anything agy
```

### Windows in four steps

No Go toolchain needed — use the prebuilt binary.

```powershell
# 1. download
curl.exe -L -o "$env:USERPROFILE\Downloads\agy-bridge.exe" `
  https://github.com/codewith-aditya/agy-bridge/releases/download/v0.1.0/agy-bridge-windows-amd64.exe

# 2. move it somewhere permanent
mkdir "$env:USERPROFILE\tools\agy-bridge" -Force
move "$env:USERPROFILE\Downloads\agy-bridge.exe" "$env:USERPROFILE\tools\agy-bridge\"
```

```powershell
# 3. run it in its own terminal
$env:UPSTREAM_BASE="https://api.openai.com/v1"
$env:UPSTREAM_KEY="sk-..."
$env:DEFAULT_MODEL="gpt-4o-mini"
& "$env:USERPROFILE\tools\agy-bridge\agy-bridge.exe"
```

```json
// 4. %APPDATA%\Antigravity IDE\User\settings.json
{ "jetski.cloudCodeUrl": "http://127.0.0.1:8198" }
```

Restart the IDE. Building from source instead:

`make` is not available on Windows, so build directly and run it in its own terminal:

```powershell
winget install GoLang.Go
git clone https://github.com/codewith-aditya/agy-bridge.git
cd agy-bridge
go build -trimpath -ldflags "-s -w" -o agy-bridge.exe ./cmd/agy-bridge
```

```powershell
$env:UPSTREAM_BASE="https://api.openai.com/v1"
$env:UPSTREAM_KEY="sk-..."
$env:DEFAULT_MODEL="gpt-4o-mini"
.\agy-bridge.exe
```

Then point the client at it from a second terminal:

```powershell
$env:GOOGLE_GEMINI_BASE_URL="http://127.0.0.1:8198"
$env:GEMINI_API_KEY="unused"   # the bridge already has UPSTREAM_KEY
agy
```

For the IDE, add `"jetski.cloudCodeUrl": "http://127.0.0.1:8198"` to its user settings. To keep the
bridge running without an open terminal, register it with NSSM — see
[docs/deployment.md](docs/deployment.md#windows-service).

### Antigravity IDE

Add to the IDE's user `settings.json` (`%APPDATA%\Antigravity IDE\User\settings.json` on Windows,
`~/.config/Antigravity IDE/User/settings.json` on Linux):

```json
{ "jetski.cloudCodeUrl": "http://127.0.0.1:8198" }
```

Restart the IDE. Google sign-in still runs through the passthrough, so onboarding and the native
model picker keep working while generation is served by your upstream.

## Configuration

| Variable | Default | Description |
| --- | --- | --- |
| `LISTEN` | `127.0.0.1:8198` | Bind address. |
| `UPSTREAM_BASE` | `https://api.openai.com/v1` | OpenAI-compatible base URL, no trailing slash. |
| `UPSTREAM_KEY` | *empty* | Upstream key for the CLI route. Empty means the caller's `GEMINI_API_KEY` is used. |
| `CLOUD_SERVER_KEY` | *empty* | Upstream key for the IDE route, whose caller presents a Google OAuth bearer instead of an upstream key. |
| `DEFAULT_MODEL` | *empty* | Upstream model for any Gemini model ID not present in `MODEL_MAP`. |
| `MODEL_MAP` | *empty* | `gemini-3.1-pro-preview=glm-5.3,gemini-3-flash=deepseek-v4-flash` |
| `MAX_OUTPUT_TOKENS` | `100000` | Clamp for `maxOutputTokens`. Antigravity requests 65535, which passes through at this default. `0` disables it. |
| `CLOUD_CODE_PASSTHROUGH_BASE` | `https://cloudcode-pa.googleapis.com` | Google host for non-generation Cloud Code RPCs. |
| `DEBUG` | *empty* | Any value dumps the last request bodies to `/tmp`. |

`UPSTREAM_KEY` is deliberately optional: leaving it empty makes every caller spend their own key,
which is what makes a shared endpoint safe.

## Endpoints

| Method | Path | Purpose |
| --- | --- | --- |
| `POST` | `/v1beta/models/{model}:generateContent` | Gemini generation. |
| `POST` | `/v1beta/models/{model}:streamGenerateContent?alt=sse` | Gemini streaming. |
| `POST` | `/v1beta/models/{model}:countTokens` | Rough token estimate. |
| `POST` | `/v1internal:generateContent` | Cloud Code generation. |
| `POST` | `/v1internal:streamGenerateContent` | Cloud Code streaming. |
| `POST` | `/v1internal:*` | Forwarded to Google with the caller's bearer. |
| `GET` | `/health` | Effective configuration. |

## How it works

**Transport override.** The CLI honours `GOOGLE_GEMINI_BASE_URL`. The IDE honours the hidden
`jetski.cloudCodeUrl` setting; its hub additionally honours `CLOUD_CODE_URL` and
`--cloud_code_endpoint=`.

**Request translation.** `systemInstruction` becomes a system message. `contents[].role == "model"`
becomes an assistant message carrying `tool_calls`. Inline base64 images become `image_url` parts.

Two details matter more than they look:

1. Antigravity sends `functionResponse` under role **`model`**, not `user` as the Gemini spec says.
   Dispatching on role silently turns every tool result into an empty assistant message, and the
   agent loop dies without an error. Dispatch on part type instead.
2. `functionResponse` carries only a function name, never a call id, so the bridge synthesises ids
   (`call_<n>_<name>`) and hands them back FIFO per name.

**Response translation.** OpenAI deltas become Gemini candidates; `reasoning_content` surfaces as
`thought: true` parts; tool-call fragments are concatenated and emitted as a single `functionCall`
part with a placeholder `thoughtSignature`, which Gemini 3 era clients round-trip.

## Limitations

- The IDE route is verified at protocol level; in-app behaviour depends on the Antigravity build.
- The IDE still requires Google sign-in, because onboarding and the catalog are proxied.
- Attachments are supported as inline images only; other media passes through untouched.
- Vendor-specific fields (safety settings, cached content, grounding) are ignored.

## Documentation

Full guides live in [docs/](docs/README.md):

| Page | What it covers |
| --- | --- |
| [Getting started](docs/getting-started.md) | Install, first run, CLI and IDE wiring. |
| [Configuration](docs/configuration.md) | Every environment variable, model mapping, key strategy. |
| [Architecture](docs/architecture.md) | Package layout and request lifecycle. |
| [Gemini v1beta protocol](docs/protocols/gemini-v1beta.md) | The CLI surface, request and response shapes. |
| [Cloud Code protocol](docs/protocols/cloud-code-v1internal.md) | The IDE envelope, passthrough and the hidden setting. |
| [Deployment](docs/deployment.md) | systemd, nginx, Docker, hardening checklist. |
| [Troubleshooting](docs/troubleshooting.md) | Symptom → cause → fix. |
| [FAQ](docs/faq.md) | Short answers to recurring questions. |
| [Internals](docs/ANTIGRAVITY-internals.md) | Reverse-engineering notes from the binaries. |

## Development

```bash
make test     # unit tests
make vet      # static checks
make build    # ./bin/agy-bridge
make cross    # linux/amd64, windows/amd64, darwin/arm64
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for the project layout and review process.

## License

MIT — see [LICENSE](LICENSE).

Antigravity is a Google product. This project is unaffiliated with Google and ships no Google code.
