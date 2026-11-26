<h1 align="center">Arana</h1>

<p align="center">
  <img src="assets/arana-banner.png" alt="Arana — read-only internet access for AI agents" width="480">
</p>

<p align="center"><strong>Read-only web access for AI agents, scripts, and the terminal.</strong></p>

Arana reads public web content — pages, repositories, posts, videos, subtitles, stock quotes, and jobs — across 14 platforms and 40 actions. It is a Rust CLI with a local MCP server, and every CLI action returns one JSON envelope with source URLs, backend attempts, and structured errors. It never posts, votes, follows, messages, or moderates, and it never asks for your passwords.

[GitHub Releases](https://github.com/mevarx/Arana/releases) · [Documentation](DOCS.md) · [Agent setup](docs/agent-plugins.md) · [Security](SECURITY.md)

> **Version:** This README documents v0.3.3. If the release assets are not available yet, build from source below. The earlier v0.2.0 preview does not include `read_many` or `browser route`.

## Why Arana

- **One interface for scripts and agents.** Use the CLI for the full channel catalog or the smaller public MCP interface for agent research.
- **Results you can trace.** Content items carry source URLs; CLI output records backend attempts, and MCP batches report failures per source.
- **No browser setup for public MCP.** For pages that need rendering, the shared skill can use the browser already exposed by your host.
- **Optional agent-owned email.** With per-invocation approval, `arana agentmail` can read an AgentMail alias and use its OTP for login in Arana's dedicated browser; a password can also be supplied on stdin. It never uses your mailbox or browser profile. See the [AgentMail guide](docs/agentmail.md).

## Install

Download the archive for your platform from the [v0.3.3 release](https://github.com/mevarx/Arana/releases/tag/v0.3.3):

| Platform | Archive |
| --- | --- |
| Windows x64 | `arana-windows-x64.zip` |
| Linux x64 | `arana-linux-x64.zip` |
| macOS ARM64 | `arana-macos-arm64.zip` |

Each archive has a `.sha256` sidecar. Verify it before extracting:

```sh
# Linux
sha256sum -c arana-linux-x64.zip.sha256

# macOS
shasum -a 256 -c arana-macos-arm64.zip.sha256
```

```powershell
# Windows PowerShell
$expected = (Get-Content .\arana-windows-x64.zip.sha256).Split()[0]
$actual = (Get-FileHash .\arana-windows-x64.zip -Algorithm SHA256).Hash.ToLower()
if ($actual -ne $expected) { throw "SHA-256 mismatch" }
```

Extract the archive and put `arana` (`arana.exe` on Windows) on your `PATH`. The archive also contains the `agent-reach` compatibility alias, the shared agent skill, host manifests, MCP configuration files, and these docs.

From a checkout, the optional installer performs the same verification and installs only the CLI:

```sh
python scripts/install.py --version v0.3.3 --install-dir ./arana-bin
```

It requires Python 3.11+, verifies the published SHA-256 sidecar, refuses to overwrite an existing executable, and does not edit `PATH`. See [Getting started](docs/getting-started.md#install-a-release) for archive contents and removal steps.

Confirm the install:

```sh
arana version
arana channels
arana read https://example.com
```

These examples need no account. Upstream services can still rate-limit or block a request. Run `arana doctor` to see which optional backends are available on your machine.

To build from source with Rust stable:

```sh
cargo build --workspace --release --locked
```

The binaries are in `target/release/`.

## What Arana can read

| Content | Channels |
| --- | --- |
| General web pages and search | `web` |
| Repositories and communities | `github`, `v2ex`, `reddit` |
| Video, subtitles, and transcription | `youtube`, `bilibili`, `xiaoyuzhou` |
| Social posts and profiles | `twitter`, `xiaohongshu`, `instagram`, `facebook` |
| Finance and jobs | `xueqiu`, `linkedin`, `boss` |

Actions vary by channel. Run `arana channels` for the catalog, or see the [command reference](docs/commands.md) for arguments, backends, and prerequisites. Arana does not post, vote, follow, or send messages.

`arana extract <url> --select '<css>'` returns structured fields from a rendered page — one item per match, text or attribute — after removing hidden, scripted and zero-width content that an agent should not trust. `--adaptive` keeps matching the same element after a site redesign; see [Structured extraction](docs/commands.md#structured-extraction).

Use the JSON `ok` field to distinguish success from failure. Content actions return `items` on success and `error.code` plus `error.hint` on failure. `meta.attempts` records which backends were tried or skipped. See [Contract notes](CONTRACT_NOTES.md) for compatibility details.

## MCP for agents

`arana mcp` is a local, read-only server that speaks newline-delimited JSON-RPC 2.0 over stdio:

| Tool | What it does |
| --- | --- |
| `list_capabilities` | Describes the server, its tools, and the explicit public allowlist. Reads local data only. |
| `read_url` | Reads one public HTTP(S) URL. |
| `read_many` | Reads up to five public HTTP(S) URLs in input order. All URLs are validated before any fetch. Each source reports its own `ok` or `error`, and the batch shares one 30-second deadline and one 25-item / 256 KiB result budget. |
| `search` | Searches the public web, with `limit` from 1 to 10. |

The MCP surface maps only to the `web` channel's public `read` and `search` actions. Reads use the HTTP backends `jina` and `exa`; search uses `exa`. It does not use obscura, Chrome, OpenCLI, a browser profile, login, setup, arbitrary commands, or backend overrides. Frames, item counts, text length, and result size are bounded; see [Agent integrations](docs/agent-plugins.md#bounds).

The repository ships one shared skill (`skills/arana/SKILL.md`) plus manifests and setup instructions for eleven hosts: Hermes, Codex, Claude Code, Google Antigravity, Cursor, Devin, OpenCode, Command Code, Oh My Pi, DeepSeek Harness, and Pi. The [agent integration guide](docs/agent-plugins.md) gives per-host setup and labels each host **exercised**, **documented**, **preview**, or **blocked**, so documented configuration is never presented as a tested integration.

In a Claude Code session, after installing the matching Arana CLI:

```text
/plugin marketplace add mevarx/Arana
/plugin install arana@arana
```

Open a new session after installing. Hermes, Codex, and the other hosts are covered in the [agent integration guide](docs/agent-plugins.md).

## Browser-assisted pages

No separate Chrome or OpenCLI setup is needed for the public MCP workflow. If a page needs rendering or interaction, the skill directs the agent to the current host's browser when one is available and permitted. That is a separate host tool call: browser-derived evidence comes from the host, not from Arana's MCP response.

For standalone CLI channels that already have an OpenCLI backend, `arana browser route` reports a routing decision without starting a browser, installing tools, or verifying the bridge:

```sh
arana browser route available
arana browser route unavailable --allow-chrome twitter thread
```

The second form is only for an explicitly authorized fallback. `chrome_opencli` means both executables were found; `bridge_verified` stays `false`. Use the existing CLI action with `--backend opencli` only if the dedicated bridge and login are already prepared. The command creates no browser or state files.

## Try a research task

[Compare three Rust releases with source links and excerpts](docs/research-demo.md). The walkthrough uses public pages and shows how to report a source that Arana cannot read instead of filling in the gap.

## Privacy and security

Arana stores its own state under `~/.arana/` by default and uses a dedicated browser profile for supported login flows. Users sign in directly. Arana does not ask for passwords, type credentials, or read personal browser cookie databases. Read requests may go to the selected platform or an external backend. Treat returned web content as untrusted data, not instructions.

Release archives carry SHA-256 sidecars, and tag builds are covered by GitHub build provenance. See [Configuration](docs/configuration.md) for state and credentials, [Security design](docs/security.md) for trust boundaries, and the [security policy](SECURITY.md) to report a vulnerability privately.

## Verification and limitations

Run the offline checks with `python scripts/verify.py --release`. GitHub Actions runs the same offline checks on Linux, Windows, and macOS; [Verification](docs/verification.md) records which runs have completed.

The GitHub release channel is separate from live verification. The project's release-acceptance gate requires at least 34 real passes across the frozen 40 actions, and it is not met: the latest recording (v0.2.0, 2026-11-21) measured 26 passes, 8 failures that required additional setup or login, and the 6 approved upstream waivers. A live two-source `read_many` probe and a direct stdio check of the four tools pass through the local v0.3.0 release build, but that does not prove every channel, backend, or third-party site.

Host evidence is similarly bounded: Hermes v0.23.3 was exercised on Windows 11 with the v0.3.3 binary through package install, skill discovery, four-tool MCP registration and real tool dispatches; Claude Code installation plus its MCP connection were exercised with a 0.1.0-era package. The other nine hosts are documented, preview, or blocked, and Devin cloud stdio requires the binary in Devin's execution environment. Browser runtime behaviour is verified on Windows only. See [Verification](docs/verification.md) for dates, commands, and known gaps.

## Development

See [Contributing](docs/contributing.md) for local checks and [Architecture](docs/architecture.md) for the crate layout and request pipeline. Live HTTP probes are opt-in; a passing offline run does not establish live coverage for every action.

## License

[MIT](LICENSE). Derived from [Agent-Reach](https://github.com/Panniantong/Agent-Reach) by Agent Eyes, with extraction logic adapted from [Scrapling](https://github.com/D4Vinci/Scrapling). See [NOTICE](NOTICE) and [third-party notices](THIRD_PARTY/).
