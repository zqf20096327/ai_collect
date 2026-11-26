# Code Assist

A .NET 10 coding assistant with a command-line interface and a native VS Code extension. Both connect to the same local server for provider access and conversations.

Use the CLI to configure providers, inspect models and tools, manage connectors, and run streamed text conversations with `run` or line-oriented `chat`. Chat includes native session/inspection commands and namespaced prompt, skill and plugin guidance. Committed conversations recover across service restarts. Use VS Code for native text chat and selection questions. Workspace coding edits, approvals and the full-screen terminal UI remain unavailable. See [feature status](docs/content/guide/features.md).

## Build and Install

Requires the .NET 10 SDK. Run from the repository root:

```sh
dotnet build CodeAssist.slnx -c Release
ENABLED_LIVE_TESTS=0 dotnet test --solution CodeAssist.slnx -c Release --no-progress --ignore-exit-code 8
dotnet run --project src/CodeAssist.Cli -- --help
dotnet pack src/CodeAssist.Cli -c Release -o artifacts/packages
```

The CLI project packages as the `code-assist` .NET tool. The package is built locally, not published to NuGet. Examples below use an installed `code-assist`; for development, replace it with `dotnet run --project src/CodeAssist.Cli --`.

Repo-local development launchers build and run the CLI without installing the tool:

```powershell
.\ca.ps1 --help
.\ca.ps1 chat
```

Use `ca.cmd --help` in Windows CMD, or `./ca --help` in Bash on Linux, macOS or Git Bash. Arguments and exit codes pass through unchanged, and the caller's working directory remains the workspace. Launchers use `--no-restore`; run `dotnet restore CodeAssist.slnx` once after cloning or changing dependencies.

## Shared Runtime

The CLI and VS Code extension connect to `CodeAssist.Server` over authenticated local HTTP. Provider settings and credentials stay in the .NET runtime. The CLI bundles the server; the extension requires a compatible server installation. See the [server guide](docs/content/guide/server.md) for connection setup and limits.

## Configure

Settings load from defaults, user preferences, user settings, project files, environment, flags and managed policy. Lower-trust project files can tighten restrictions but cannot add providers, credentials, connector processes or allow rules. Every JSON property has an equivalent environment variable using `__` at each nesting level, including dictionary keys and list indices. Environment and flag overrides are never persisted.

User settings live in `~/.code-assist/settings.json` (a sibling `settings.jsonc` takes precedence):

```json
{
  "providers": {
    "default": {
      "protocol": "openai",
      "endpoint": "https://api.openai.com/v1/"
    }
  },
  "agent": { "model": "default/gpt-4.1", "maxTurns": 20, "permissionPreset": "ask" }
}
```

Literal API keys are accepted from the environment, not settings files or flags. Trusted user/managed settings can instead store `"apiKey": "{env:VARIABLE_NAME}"`; the former `envs` list is removed. References resolve only in memory and never bypass managed locks. On PowerShell:

```powershell
$env:Providers__default__ApiKey = '<your-provider-key>'
code-assist doctor
code-assist config explain agent.maxTurns
```

SDK-backed provider components support OpenAI chat/Responses and compatible routes, Anthropic, Azure, Google/Gemini, Vertex and Bedrock. New provider entries default to automatic routing and may inherit endpoint/protocol from adapters or catalog data. Native cloud identity setup is supported; vault and OAuth login are not implemented. See [configuration](docs/content/guide/configuration.md).

## Available Commands

```sh
code-assist config show --sources
code-assist config validate
code-assist config schema
code-assist providers list
code-assist providers presets --catalog
code-assist providers models --refresh
code-assist connectors list
code-assist tools list
code-assist doctor
code-assist run "Explain optimistic concurrency"
code-assist chat
code-assist commands list --json
code-assist commands expand skill/standard/fault-trace --input "Investigate a failed request"
```

Catalog refresh fetches models.dev over HTTPS and retains a last-good ETag cache. No bundled model snapshot or sync script is used. Catalog inspection does not send a model inference request. Connector commands manage definitions and explicit server-side runtime operations. Tool commands inspect the catalog, not execute agent turns.

`run` and `chat` use the configured provider and can incur charges. They launch an owned service that stops on exit; committed conversations recover when the same workspace/storage reopens unless `host.recoverConversations=false`. One service owns each workspace store. For concurrent clients or explicit session reuse, start `serve`, supply the same environment token in the client shell, and use `--endpoint http://127.0.0.1:8080`. Chat `/help` lists commands; one-shot `commands list|expand` never calls a model. See the [CLI reference](docs/content/reference/cli.md).

## Managed Service Shutdown

Ctrl+C cancels the CLI command and starts one shared cleanup task. Repeated or
concurrent disposal awaits that same task. The owned server receives an explicit
shutdown signal and gets six seconds to exit gracefully. If necessary, cleanup
terminates the owned process tree, with bounded five-second containment and
process-exit waits. Termination failures are traced; failure to confirm shutdown
is reported instead of waiting indefinitely. Startup failure also cleans up owned
handles and processes while preserving the original exception cause.

On Windows, an unnamed, non-inheritable kill-on-close job contains the bundled
server and its ordinary descendants. The server waits for bootstrap acknowledgement
until job assignment succeeds. Cleanup checks active job membership, including
children whose original parent has already exited. CLI crash or forced termination
closes its job handle and terminates associated processes; unrelated processes and
standalone servers are not assigned to that job. Other platforms retain parent-pipe
shutdown and process-tree escalation, without the Windows job guarantee.

Verification: 663 CLI integration cases passed. Real terminal Ctrl+C returned 130,
left no isolated CLI/service process, and the same output rebuilt without DLL
locks. Tests also cover concurrent cleanup, orphaned descendants, forced owner
termination, stubborn escalation, bootstrap failures and unrelated-process survival.
Physical terminal-window closure was not separately tested.

## Terminal Icons

Interactive chat requires a compatible Nerd Font and Unicode before connecting
the service. Local startup checks installed fonts after workspace consent,
preferring the saved family and otherwise reusing any compatible installed family.
This offline check skips the catalog, installation and confirmation questions.
If no compatible font is found, search the official v3.5.1 release catalog by
displayed family or ZIP archive name (72 packs). Symbols-only stays visible but
cannot serve as a terminal text family. Missing fonts download only after explicit approval,
with the release asset's published SHA-256 verified before bounded ZIP extraction.
Regular monospaced face, parsed family and glyph support are checked, not assumed
for every pack. Installation does not select the terminal's font or edit profiles.
Choose the exact reported family in your terminal settings if glyphs are missing.
Installed does not prove selected. Chat uses Nerd icons without an ASCII mode.

`chat --icons auto` (default) and `chat --icons nerd` both reuse an installed font
or require setup when none is available. `--icons ascii` is rejected and old ASCII
opt-outs are ignored. Selected families are bounded state under the
CodeAssist home `state` directory, separated by terminal identity, not project
settings. Removing all compatible fonts requires installation again.
Escape cancels startup; Ctrl+C exits chat. Declined installation, failed downloads,
integrity checks and registration stop interactive startup before service connection.

JSON and noninteractive output remain undecorated and do not run font setup.
Interactive external attachment has the same font requirement. Unicode-disabled
interactive consoles are rejected. SSH, WSL, containers and headless sessions
cannot install fonts into the terminal client and must configure the terminal host.
Windows uses user Fonts/HKCU, macOS uses the user Library/Fonts directory, and
Linux uses the XDG user font directory with cache refresh when available.
Downloads allow only official HTTPS assets and bounded official CDN redirects.
Limits: 768 MiB ZIP, 4096 entries, 16 MiB per face, 4 GiB expanded total, 200:1
compression ratio, five-minute installation deadline. Traversal, links, malformed
fonts, absent digests or notices stop startup. Archive and separately pinned glyph
notices are preserved beside the font. Upstream flags an unlicensed glyph set;
preserving attribution does not resolve that permission limitation.
See [terminal font attribution](src/CodeAssist.Cli/Fonts/NOTICE.md).

## Plugins

Create a declarative package with `code-assist plugins init ./review-plugin --id team.review`. Validate and install it, inspect `plugins list --json`, then enable it with `--approve` and its exact digest. Installation is disabled by default; changed releases revoke approval. Use `plugins expand team.review/inspect --input "Review this change"` without inference, or **CodeAssist: Run Plugin Prompt** in VS Code to submit selected guidance through normal text chat.

The shared runtime supports namespaced skills/roles, bounded dispatcher-backed hooks/workflows, declared-only ZIP packages, local/HTTPS registry reads, explicit local publishing and local usage counters. Automatic MCP/LSP service launch, registered workflow tools, live evaluations and publisher analytics remain pending. No plugin code, install scripts or package-manager dependencies are loaded. See the [plugin guide](docs/content/guide/plugins.md) for trust, dependencies, limits and commands.

## Local Agent Server

Configure a provider as above, then in PowerShell 7:

```powershell
$env:Host__Listen__Http__Token = [Convert]::ToBase64String([Security.Cryptography.RandomNumberGenerator]::GetBytes(32))
code-assist serve --listen 127.0.0.1:8080
```

The launcher starts the bundled standalone `CodeAssist.Server`. Direct source startup is also supported with `dotnet run --project src/CodeAssist.Server -- --listen 127.0.0.1:8080`; it emits a versioned JSON readiness record.

The server provides bounded durable conversations, metadata/archive controls, conversation-only rewind, per-session reported usage limits, JSON/SSE, cancellation, command/catalog/management APIs and authenticated OpenAPI. The environment-only bearer token grants access to all sessions and admitted management operations in this single-user instance. Remote binding, durable stream replay, automatic shared-service discovery, workspace coding tools and approval execution are not enabled. See the [server guide](docs/content/guide/server.md) for API usage and limits.

## VS Code Extension

Build the [VS Code extension](vscode-extension/README.md) from the repository root:

```sh
cd vscode-extension
npm ci
npm test
npm run package
```

Install the generated VSIX with **Extensions: Install from VSIX**, or press F5 using **CodeAssist VS Code Extension**. With a configured `CodeAssist.Server` executable and a trusted workspace, run **CodeAssist: Connect**, then use `@codeassist` or **CodeAssist: Ask**. **Ask About Selection** sends explicitly selected text only.

Managed mode launches an owned standalone server directly with a private generated token. External mode uses a loopback URL and a token in VS Code SecretStorage. Provider configuration/credentials remain in the .NET runtime; no JavaScript model SDK is used. Remote workspaces require the server on the workspace host. See the [extension guide](docs/content/guide/vscode.md) for source-DLL setup, model/session controls and limits. Automatic runtime installation is not bundled into the private VSIX.

## Safety

- Settings trust, validation, provenance and secret masking are implemented. Runtime policy evaluation, approvals, aggregate budgets and checkpoint-backed session rewind remain pending.
- File/process/web components have path checks, timeouts and output limits; these are not an OS sandbox or protection against every filesystem race.
- Processes execute with the current user's privileges. API keys and source data must be protected by the caller and OS permissions.
- Deterministic tests do not establish live-account compatibility, billing limits or production readiness.

## Development

See [architecture](docs/content/development/architecture.md), [configuration](docs/content/guide/configuration.md), and [feature coverage](docs/content/guide/features.md). Tests use xUnit v3, Microsoft Testing Platform, Shouldly and NSubstitute. Suites follow `tests/CodeAssist.<Project>/UnitTests` and `IntegrationTests`, with source feature folders. Architecture checks remain separate. Normal validation needs no model credentials; live provider tests are opt-in.

Documentation is authored directly in [docs/content](docs/content/index.md); [site development](docs/README.md) covers previewing and publishing it. See [contributing](docs/content/development/contributing.md) for project ownership and validation requirements.
