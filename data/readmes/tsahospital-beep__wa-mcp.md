<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/brand/banner-dark.svg">
    <img src="assets/brand/banner-light.svg" alt="WA MCP" width="640">
  </picture>
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-6c7a89?style=flat"></a>
  <img alt="Go 1.26" src="https://img.shields.io/badge/go-1.26-4f7c9a?style=flat">
  <img alt="Python 3.11+" src="https://img.shields.io/badge/python-3.11%2B-4f7c9a?style=flat">
  <img alt="MCP compatible" src="https://img.shields.io/badge/MCP-compatible-5f8a7a?style=flat">
  <img alt="Platform: Windows, macOS, Linux" src="https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-5f8a7a?style=flat">
  <a href="CHANGELOG.md"><img alt="Version 0.2.1" src="https://img.shields.io/badge/version-0.2.1-6c7a89?style=flat"></a>
  <a href="https://glama.ai/mcp/servers/tsahospital-beep/wa-mcp"><img alt="WA MCP on Glama" src="https://glama.ai/mcp/servers/tsahospital-beep/wa-mcp/badges/score.svg"></a>
</p>

<p align="center">
  WhatsApp MCP for AI assistants: a local bridge and MCP server to search, read and send WhatsApp messages from Claude, Cursor, VS Code and other MCP clients.
</p>

<p align="center">
  <a href="docs/getting-started.md">Getting started</a> |
  <a href="docs/tutorials/README.md">Tutorials</a> |
  <a href="docs/guides/configuration.md">Configuration</a> |
  <a href="docs/reference/tools.md">Tools</a> |
  <a href="docs/reference/http-api.md">HTTP API</a> |
  <a href="docs/security.md">Security</a> |
  <a href="docs/faq.md">FAQ</a>
  <br>English | <a href="docs/i18n/README.pt-BR.md">Português</a> | <a href="docs/i18n/README.es.md">Español</a> | <a href="docs/i18n/README.hi.md">हिन्दी</a>
</p>

## Try it without a phone

With uv installed, `uvx wa-mcp-server --demo` starts a fictional archive of eight chats. The demo needs WA MCP 0.2.1 or later and runs offline after installation. Use the [install buttons](#quick-start) or copy the config for your client.

**Claude Code**

```sh
claude mcp add wa-mcp-demo -- uvx wa-mcp-server --demo
```

**Claude Desktop (`claude_desktop_config.json`) and Cursor (`.cursor/mcp.json`)**

```json
{
  "mcpServers": {
    "wa-mcp-demo": { "command": "uvx", "args": ["wa-mcp-server", "--demo"] }
  }
}
```

**VS Code (`.vscode/mcp.json`)**

```json
{
  "servers": {
    "wa-mcp-demo": { "type": "stdio", "command": "uvx", "args": ["wa-mcp-server", "--demo"] }
  }
}
```

Ask “What are my tasks today?”, then search for “blue umbrella” and read the voice note transcript. [Two-minute tutorial](docs/tutorials/00-demo.md)

## Features

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark) and (max-width: 600px)" srcset="assets/features/features-dark-mobile.svg">
    <source media="(max-width: 600px)" srcset="assets/features/features-light-mobile.svg">
    <source media="(prefers-color-scheme: dark)" srcset="assets/features/features-dark.svg">
    <img src="assets/features/features-light.svg" alt="WA MCP features: chats and media, daily activity, setup and integrations" width="880">
  </picture>
</p>

| Area | What it does |
| --- | --- |
| Login window | Links your account from a small local window with a QR code or a pairing code for your phone number. The terminal prints the QR code as a fallback. |
| Several accounts | More than one WhatsApp number in one MCP server: one bridge per number with its own store and sending limits, `wa-bridge run-all` keeps them running, every tool takes an `account` argument and `get_my_day` covers all numbers. A config without accounts works as before. See [Several accounts](docs/guides/accounts.md). |
| History | Stores live messages and the history your phone sends after linking, and applies edits, deletions and reactions. Tools ask the phone for older pages, per chat or for the whole archive. |
| Chat import | Loads a WhatsApp "Export chat" file (`.txt`, or `.zip` with media) into the store, for history older than what the phone syncs. Reads Android and iPhone layouts in many date and clock formats, detects the date order, skips messages that are already stored and can be run again safely. Run it as a dry run first. |
| Media | Downloads images, video, audio, voice notes, documents and stickers. When the WhatsApp copy has expired, the bridge asks your phone to upload it again. |
| Search | Case-insensitive search in any script across messages, transcripts and extracted file text. The phone and LID chats of one person are merged. |
| Voice transcription | Turns voice notes into text with pluggable backends: faster-whisper, openai-whisper, whisper.cpp, any OpenAI-compatible endpoint or your own command. |
| Text from screenshots | Reads the text in photos and screenshots with a local OCR engine (tesseract or RapidOCR). The text is stored with the message, so search and `list_messages` find it. |
| Documents and archives | Reads text from PDF, DOCX, XLSX, PPTX, plain text and HTML files, lists ZIP and RAR archives without unpacking them, and reads public Google Docs links. |
| Chat analytics | Message volume, reply timing in both directions, message length, emoji, stickers, voice notes, formality and group roles. Compares up to 8 chats. |
| Tasks | Detects requests in chats with plain rules, tracks their status and finds watched words. No language model is involved. |
| `get_my_day` | One call that lists what needs you today: open requests, your own promises that are due, chats waiting for your answer, missed calls and scheduled sends. |
| Sending | Text, files, voice notes and stickers, with replies and mentions. Off by default. You approve each send in your client when it supports that; other clients need `sending.allow_confirm_flag`. |
| Human-like sending | Sending paces itself like a person would. The bridge marks the chat read first, shows the typing indicator for a time that depends on the message length, leaves a pause between messages, and follows quiet hours and per-hour limits. This makes automated sending look less mechanical. It does not guarantee anything. |
| Read receipts | Marks messages as read on request, or automatically if you turn that on. |
| Calls | Call history with direction, video flag, outcome and duration. Answering and placing calls with an agent is in development, see [Roadmap](#roadmap). |
| Scheduled messages | One-time, daily, weekly or monthly messages that the bridge sends without a running assistant. |
| [Agent connector](docs/guides/agent-connector.md) | Connect your own reply API or model. Draft, approve or send text and voice notes for listed chats. |
| Webhooks | Posts message, receipt, call, connection, scheduled and security events to your URLs. The bridge retries failed deliveries and signs requests when a secret is set. |
| HTTP API | Local REST API with token authentication and an OpenAPI 3.1 document. |
| Embedding | The Go package `bridge/pkg/wabridge` runs the bridge inside another program, with hooks for every stored message and chat, extra HTTP routes and access to sending, media and history. `wa_mcp_server.embed.register` adds chosen tools to another MCP server. |
| Remote access | `wa-mcp serve --http` serves MCP over Streamable HTTP for remote clients such as claude.ai custom connectors, Claude Code, Cursor and VS Code. Per-device bearer tokens (stored hashed) or OAuth 2.1 with PKCE, dynamic registration and an owner approval page. Rate limits, Host and Origin checks, no CORS by default, and TLS proxy support. See [Connect remotely](docs/guides/remote-clients.md). |
| Server deployment | Docker images for the bridge and the server (non-root, read-only file system, health checks) and a Compose file with optional Caddy for automatic HTTPS. The login page works through the proxy with a one-time link. See [Run on a server](docs/guides/server.md). Public images are available for v0.1.0. CI builds them and starts the preview stack on pushes to `main`. |
| AI providers (optional) | Off by default: your assistant does the thinking. You can set one background provider, Ollama, an OpenAI-compatible server or Anthropic, for `get_my_day` summaries and image descriptions. Keys come from environment variables, and daily call and input limits guard the cost. |
| Python SDK | The `wa_mcp` package: bridge client, read access to the local database, transcription and exports. |
| Encryption | On by default: message text, attachment names, reactions, transcripts and media keys in the database are encrypted with a key kept in the OS keystore (Windows DPAPI, macOS Keychain, Linux Secret Service), or with a passphrase or key file. The API token is kept there too, and on Windows the store folder gets EFS. See [Encryption and keys](docs/guides/encryption.md). |
| Session alerts | Records a remote logout, another client using this session, a new device on the account and a different account at login, and shows them in `get_bridge_status`, `GET /api/v1/status` and a `security` webhook. |

## How it compares

The table covers features each project supplies. Encryption refers to message text encrypted by the application. Chat import means reading a WhatsApp chat export. Several accounts means one deployment can host more than one linked number. Partial marks a feature with limited or unconfirmed support.

| Feature | WA MCP | [finereli](https://github.com/finereli/whatsapp-mcp) | [verygoodplugins](https://github.com/verygoodplugins/whatsapp-mcp) | [felipeadeildo](https://github.com/felipeadeildo/whatsapp-mcp) | [jlucaso1](https://github.com/jlucaso1/whatsapp-mcp-ts) | [BrOrlandi](https://github.com/BrOrlandi/whatsapp-mcp-server) |
| --- | --- | --- | --- | --- | --- | --- |
| Send messages | Yes | No | Yes | Yes | Yes | Yes |
| Send media and voice notes | Yes | No | Yes | No | No | Partial |
| Voice transcription | Yes | Yes | Yes | Yes | No | Yes |
| Text from images (OCR) | Yes | No | No | Yes | No | No |
| Document text | Yes | Partial | No | Yes | No | No |
| Encryption at rest | Yes | Yes | No | No | No | No |
| Human-like pacing and limits | Yes | No | Partial | Partial | No | Partial |
| Scheduled messages | Yes | No | No | No | No | No |
| Several accounts | Yes | Yes | No | Yes | No | Yes |
| Webhooks | Yes | No | Yes | Yes | No | Yes |
| Remote MCP over HTTP with OAuth | Yes | Yes | Partial | Yes | No | Partial |
| Docker | Yes | Yes | No | No | Yes | Yes |
| Chat import | Yes | No | No | No | No | No |
| License | MIT | MIT | MIT | GPL-3.0 | ISC | MIT |
| Language | Go, Python | TypeScript | Go, Python | TypeScript | TypeScript | Go |

Checked in November 2026 from each project's public repository. Corrections are welcome.

## Architecture

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/diagrams/architecture-dark.svg">
    <img src="assets/diagrams/architecture-light.svg" alt="Architecture: the bridge (Go) connects to WhatsApp and keeps a local database and an HTTP API. The MCP server (Python) reads the database and calls the API. MCP clients talk to the server." width="720">
  </picture>
</p>

## Quick start

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) so your MCP client can run `uvx`.
The buttons install the Python server. Keep a linked bridge running for live messages and bridge tools.

[![Demo in Cursor](https://img.shields.io/badge/Demo%20in%20Cursor-4f7c9a?style=flat)](https://cursor.com/install-mcp?name=wa-mcp-demo&config=eyJjb21tYW5kIjoidXZ4IiwiYXJncyI6WyJ3YS1tY3Atc2VydmVyIiwiLS1kZW1vIl19)
[![Demo in VS Code](https://img.shields.io/badge/Demo%20in%20VS%20Code-4f7c9a?style=flat)](https://vscode.dev/redirect?url=vscode%3Amcp%2Finstall%3F%257B%2522name%2522%253A%2522wa-mcp-demo%2522%252C%2522type%2522%253A%2522stdio%2522%252C%2522command%2522%253A%2522uvx%2522%252C%2522args%2522%253A%255B%2522wa-mcp-server%2522%252C%2522--demo%2522%255D%257D)
[![Add to Cursor](https://img.shields.io/badge/Add%20to%20Cursor-4f7c9a?style=flat)](https://cursor.com/install-mcp?name=wa-mcp&config=eyJjb21tYW5kIjoidXZ4IiwiYXJncyI6WyItLWZyb20iLCJ3YS1tY3Atc2VydmVyPT0wLjEuMCIsIi0td2l0aCIsIndhLW1jcC1zZGtbZW5jcnlwdGlvbixmaWxlc10iLCJ3YS1tY3AiXX0%3D)
[![Install in VS Code](https://img.shields.io/badge/Install%20in%20VS%20Code-4f7c9a?style=flat)](https://vscode.dev/redirect?url=vscode%3Amcp%2Finstall%3F%257B%2522name%2522%253A%2522wa-mcp%2522%252C%2522type%2522%253A%2522stdio%2522%252C%2522command%2522%253A%2522uvx%2522%252C%2522args%2522%253A%255B%2522--from%2522%252C%2522wa-mcp-server%253D%253D0.1.0%2522%252C%2522--with%2522%252C%2522wa-mcp-sdk%255Bencryption%252Cfiles%255D%2522%252C%2522wa-mcp%2522%255D%257D)
[![Install in VS Code Insiders](https://img.shields.io/badge/Install%20in%20VS%20Code%20Insiders-4f7c9a?style=flat)](https://vscode.dev/redirect?url=vscode-insiders%3Amcp%2Finstall%3F%257B%2522name%2522%253A%2522wa-mcp%2522%252C%2522type%2522%253A%2522stdio%2522%252C%2522command%2522%253A%2522uvx%2522%252C%2522args%2522%253A%255B%2522--from%2522%252C%2522wa-mcp-server%253D%253D0.1.0%2522%252C%2522--with%2522%252C%2522wa-mcp-sdk%255Bencryption%252Cfiles%255D%2522%252C%2522wa-mcp%2522%255D%257D)

<details>
<summary>Copy the native Cursor install link</summary>

```text
cursor://anysphere.cursor-deeplink/mcp/install?name=wa-mcp&config=eyJjb21tYW5kIjoidXZ4IiwiYXJncyI6WyItLWZyb20iLCJ3YS1tY3Atc2VydmVyPT0wLjEuMCIsIi0td2l0aCIsIndhLW1jcC1zZGtbZW5jcnlwdGlvbixmaWxlc10iLCJ3YS1tY3AiXX0%3D
```

</details>

**Claude Desktop.** Download `wa-mcp.mcpb` from the [latest release](https://github.com/tsahospital-beep/wa-mcp/releases/latest) and open it. Select the bridge's `config.json` when prompted. For v0.1.0, use the manual PyPI command below until a release includes the bundle.

**Start the bridge.** With Go 1.26 or newer, clone the repository and build the bridge. On Windows, use
`../wa-bridge.exe` as the build output.

```bash
git clone https://github.com/tsahospital-beep/wa-mcp.git
cd wa-mcp
go build -C bridge -o ../wa-bridge ./cmd/wa-bridge
cp config.example.json config.json
./wa-bridge
```

In WhatsApp, open **Linked devices**, choose **Link a device**, and scan the QR code. To run the
public bridge image instead, follow [Run the bridge in Docker](docs/getting-started.md#run-the-bridge-in-docker).

**Connect the server.** For the buttons, set `WA_MCP_CONFIG` to the absolute path of the bridge's
`config.json` in the environment your client inherits, then restart the client. You can also append
`--config` and that path to the installed server's arguments. This lets the server find the same
message store even when the client starts in another directory.

Check the published command from a terminal.

```bash
uvx --from wa-mcp-server==0.1.0 wa-mcp --help
```

For a persistent install, use pipx with Python 3.11 or newer.

```bash
pipx install wa-mcp-server
pipx inject --force wa-mcp-server 'wa-mcp-sdk[encryption,files]'
wa-mcp --help
```

The buttons include the SDK extras for encrypted messages and file text extraction. A pipx client
can launch `wa-mcp` directly with `--config` and the absolute config path. Run `get_bridge_status` in
your client to check the database and phone connection. See [Getting started](docs/getting-started.md)
and [Connect an MCP client](docs/guides/mcp-clients.md) for manual setup.

## Tutorials

Step-by-step lessons for install, first login, clients, tasks, voice, screenshots, imports, sending,
several accounts, Docker, remote access, webhooks and security are in the
[tutorials index](docs/tutorials/README.md).

## Example: "What are my tasks today?"

```text
You:        What are my tasks today?

Assistant:  (calls get_my_day for 2026-11-23)

            Four things need you today.

            A client asked for the updated invoice yesterday at 16:40 and wants it by the end of the
            day. It is still open.

            On Sunday you told a colleague "I will send you the photos tomorrow". That promise is due today.

            The Book club group asked "Which day works for the next meeting?" about 95 minutes ago.
            Nobody has answered yet.

            A reminder for the Book club is scheduled to go out at 18:00.
```

`get_my_day` runs on your machine and uses plain rules. The assistant only phrases the result.

## Toolsets

The default `core` toolset exposes 11 tools for checking bridge status, finding contacts and chats,
reading or searching messages, reviewing your day, sending text and files, downloading media and
transcribing voice notes. Sending requires `sending.enabled` and follows the configured approval policy.

Enable additional sets with `{"mcp": {"toolsets": ["core", "actions"]}}` in `config.json`.
Choose from `history`, `media`, `insight`, `tasks`, `schedule`, `agent`, `accounts` and `actions`.
To expose every tool after upgrading from 0.1.1, use `["all"]`. The `--toolsets` flag takes precedence
over `WA_MCP_TOOLSETS` and the file. For example, `wa-mcp --toolsets core,actions` enables message
reactions, edits, revocations and text forwards. [Tool reference](docs/reference/tools.md).

## Configuration

The bridge and the server work without a config file. To change something, copy
[`config.example.json`](config.example.json) to `config.json`. It lists every key with its default.
Settings can also come from environment variables such as `WA_MCP_API_LISTEN`, and the bridge warns about
keys it does not know. For example, to allow sending and make transcription lighter:

```json
{
  "sending": { "enabled": true },
  "transcription": { "model": "small" }
}
```

All keys are described in [Configuration](docs/guides/configuration.md). Sending has its own page:
[Sending](docs/guides/sending.md).

## Voice transcription

Transcription is optional. Pick a backend with `transcription.backend`:

| Backend | Notes |
| --- | --- |
| `faster-whisper` | Default. Runs on CPU or an NVIDIA GPU. |
| `openai-whisper` | Reference implementation on PyTorch. |
| `whisper.cpp` | A separate `whisper-cli` program and a ggml model. |
| `http` | Any OpenAI-compatible `/v1/audio/transcriptions` server. |
| `command` | Any program that prints the text of a WAV file. |

ffmpeg must be on your `PATH`. Install a backend with the script for your system:

```bash
scripts/install_whisper.sh --backend faster-whisper --model large-v3 --download
```

```powershell
scripts\install_whisper.ps1 -Backend faster-whisper -Model large-v3 -Download
```

See [Voice transcription](docs/guides/transcription.md) for the details and for keeping the packages
across `uv sync`.

## Use in your own project

Read the local database from Python:

```python
from wa_mcp import config, db, people

cfg = config.load("config.json")
db.connect(cfg)
people.connect(cfg)

for m in db.messages(after="2026-11-01", query="invoice", limit=5):
    print(m["time"], people.name_of(m["conv"]), m["body"][:60])
```

Verify a signed webhook using the raw request body and the two headers the bridge signed.

```python
import hashlib, hmac, json, os, time
from http.server import BaseHTTPRequestHandler, HTTPServer

SECRET = os.environ["WA_MCP_WEBHOOK_SECRET"].encode()


class Hook(BaseHTTPRequestHandler):
    def do_POST(self):
        body = self.rfile.read(int(self.headers.get("Content-Length", 0)))
        stamp = self.headers.get("X-WA-MCP-Timestamp", "")
        delivery = self.headers.get("X-WA-MCP-Delivery", "")
        signed = f"{stamp}.{delivery}.".encode() + body
        expected = "sha256=" + hmac.new(SECRET, signed, hashlib.sha256).hexdigest()
        valid_stamp = stamp.isascii() and stamp.isdecimal() and len(stamp) <= 12
        fresh = valid_stamp and abs(time.time() - int(stamp)) <= 300
        if not (
            fresh and delivery and hmac.compare_digest(expected, self.headers.get("X-WA-MCP-Signature", ""))
        ):
            self.send_response(401)
            self.end_headers()
            return
        print(json.loads(body)["event"])
        self.send_response(204)
        self.end_headers()


HTTPServer(("127.0.0.1", 9000), Hook).serve_forever()
```

Retries use the same delivery ID. For a receiver that also skips IDs it has already processed,
see [webhook_receiver.py](examples/webhook_receiver.py).

Call the HTTP API:

```bash
TOKEN=$(./wa-bridge api-token)
curl -H "Authorization: Bearer $TOKEN" "http://127.0.0.1:8080/api/v1/messages?query=invoice&limit=5"
```

More in [Webhooks](docs/guides/webhooks.md), the [HTTP API](docs/reference/http-api.md) and the list of
[MCP tools](docs/reference/tools.md).

## Security and privacy

- By default, the bridge stores chats locally and listens on loopback for API and login requests.
  Your MCP client receives the tool results it requests.
- The `/api/v1` endpoints require a bearer token. Run `wa-bridge api-token` to read it.
  The store folder is restricted to your user. Login links work once.
- Message text in the database is encrypted by default. The key is kept by Windows DPAPI, the macOS
  Keychain or the Linux Secret Service for your user, so a copy of the store on another computer or in
  another Windows account cannot be read. On Windows the store folder, including the WhatsApp session, is
  encrypted with EFS as well; on macOS and Linux use full disk encryption for the session file.
- The bridge reports session events, such as another client using this session or a new linked device,
  in `get_bridge_status`, the status endpoint and a `security` webhook.
- Sending is disabled by default. You approve each send in your client when it can ask. Clients that
  cannot ask can send only if you set `sending.allow_confirm_flag`; they then pass `confirm=true`, which
  the model sets itself, so that path is a weaker check. The
  bridge adds limits, quiet hours and duplicate protection, and it only sends files from the downloads
  and exports folders unless you allow more.
- Message text is untrusted input. The server tells clients not to follow instructions found in it.
- With a webhook secret set, the signature covers the timestamp, delivery ID and raw body.
  Process each verified delivery ID once. Retries reuse it.
- Remote access is opt-in. `wa-mcp serve --http` requires a valid bearer token for `/mcp`.
  A non-loopback listener needs a TLS proxy and `server.trusted_proxies` unless you use `--insecure-lan`. See [Remote mode security](docs/security/remote.md).
- The encryption covers message text, attachment names, reactions, transcripts and media keys. It does
  not cover downloads, exports, chat ids, titles or timestamps.
- An administrator or malware running as your user can still read the store and ask the keystore for the
  key. Check Linked devices on your phone from time to time.

Details are in [docs/security.md](docs/security.md), keys and modes in
[Encryption and keys](docs/guides/encryption.md) and the threat model in
[docs/security/audit.md](docs/security/audit.md). To report a vulnerability, see
[SECURITY.md](SECURITY.md).

## Roadmap

- **Voice calls (in progress).** Answer and place one-to-one WhatsApp calls with your agent: the caller's
  audio goes to your speech model or voice service, and its answer is spoken back in the call. It will
  ship as a separate module, off by default, together with a follow-up message after a missed call.

## License

[MIT](LICENSE). Dependency licenses are listed in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
