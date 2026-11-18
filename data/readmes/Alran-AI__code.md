<h1 align="center">Alran Code</h1>
<p align="center">Turn a prompt into something that works. Build, test, and keep iterating from your terminal—with Alran or your own model.</p>
<p align="center">
  <a href="#quick-start">Get started</a> ·
  <a href="docs/README.md">Documentation</a> ·
  <a href="docs/examples.md">Examples</a> ·
  <a href="CONTRIBUTING.md">Contributing</a>
</p>
Alran Code is Ottili's AI coding agent for the terminal. It reads and edits your code, runs
commands and tests, and keeps iterating until the task works. By default it runs on **Ottili Werk** through the Ottili AI Gateway; Claude Sonnet 5.5 and Claude Opus 5.5 are one switch away, and you can bring your own provider key.

## Quick start

### 1. Install

Node.js 22.19+ (22.x), 24.2+ (24.x), 25 or 26 is required.

```bash
npm install -g alran
alran --version
```

pnpm, yarn and bun global installs work the same way. Update later with `alran update`
([update pipeline](docs/UPDATE_PIPELINE.md)).

### 2. Sign in with your Ottili account

```bash
alran auth login        # opens the Ottili sign-in in your browser
alran auth status       # who, which company, which project
```

Over SSH or without a display, `alran auth login` prints a code you confirm in any browser
(`--device` forces it, `--no-device` the other way). On a machine without a browser at all, create an API key at <https://ai.ottili.one/api-keys> and run
`alran auth login --api-key`. Switch company with `alran auth switch-company`, choose a project with
`alran config project`, sign out with `alran auth logout` (the session is revoked at the Platform).
Details: [docs/AUTH.md](docs/AUTH.md).

### 3. Pick a model and start

```bash
alran models            # Werk, Claude Sonnet 5.5, Claude Opus 5.5 — price and whether you can use them now
alran                   # the interactive terminal UI in the current directory
alran exec "Add a test for the date parser and make it pass"
alran usage             # credit left, your Anthropic key, spend this month per model
```

| Model | Input / output per 1M tokens | Billed by |
| --- | --- | --- |
| Ottili Werk 1.1 (default) | $0.50 / $1.50 | Ottili: free (welcome) or purchased credit |
| Claude Sonnet 5.5 | $2.00 / $10.00 (Anthropic's price) | Anthropic, on your own API key |
| Claude Opus 5.5 | $4.00 / $20.00 (Anthropic's price) | Anthropic, on your own API key |

The free credit you get on sign-up covers Werk. Claude runs on **your own Anthropic API key**: add it once in
the Ottili AI Platform under *Settings → Provider keys*, and Anthropic bills you directly — Ottili charges
nothing for Claude and adds no fee. Without a key a Claude request is refused with `byok_key_required`. Set
the default with `alran config model sonnet`. More in [docs/MODELS.md](docs/MODELS.md).

<details>
<summary>Use your own API key (bring your own key)</summary>

Your own provider key does not need an Ottili account, and those calls go directly to the provider:
Ottili does not see, meter or bill them. Set the key in your shell, then add the provider:

```bash
export MY_PROVIDER_API_KEY=...
alran provider add --name my-provider --base-url https://example.com/v1 \
  --api-format openai-completions --model my-model \
  --api-key-env MY_PROVIDER_API_KEY --use
```

Supported formats: `openai-completions`, `openai-responses`, `anthropic-messages`.
`alran models --third-party` explains the catalogue of known providers; see the
[model examples](docs/examples.md#2-choose-your-own-model).

</details>

### Plugins and skills

Bundled skills (code review, deep research, documents, spreadsheets, slides, PDFs …) work out of the box. The **Plugin Store** (`/plugin`, `alran plugin search|install`) and the **Skill Library** (`/skills library`, `alran skills search|install`) add more from stores you choose; see
[docs/store.md](docs/store.md). Sources and licensing: [docs/PLUGINS.md](docs/PLUGINS.md).

### Data and environment

User data lives in `~/.alran` (`ALRAN_DATA_DIR` overrides it). `ALRAN_API_BASE` (default
`https://ai.ottili.one/v1`) and `OTTILI_PLATFORM_URL` (default `https://platform.ottili.one`) point
at other Ottili deployments; `ALRAN_NO_UPDATE_CHECK=1` switches off the weekly update hint.

#### Web search

`web_search` works with no configuration at all. By default it calls Exa's hosted MCP endpoint
directly from your machine: no account, no API key, no Ottili server in the path. Exa sees your own
IP and applies its free per-IP rate limit, so nobody else's traffic shares your quota. The keyless
endpoint requires a **direct IPv4 connection** — on an IPv6-only host or behind a proxy it returns
403. If that happens, or if you hit the free-tier 429 limit, configure one of the options below.

For more control, set a provider explicitly. An explicit choice always wins over the keyless
default; the first one set wins:

```bash
export BRAVE_API_KEY='…'    # Brave Search API — free tier covers thousands of queries a month
export SERPER_API_KEY='…'   # Serper
export TAVILY_API_KEY='…'   # Tavily
export EXA_API_KEY='…'      # Exa on your own plan (also works from IPv6/proxied networks)
export SEARXNG_URL='http://127.0.0.1:8080'   # self-hosted SearXNG (JSON API)
```

You can also put the same settings in `~/.alran/config.yaml`, under `webSearch:`, if you would
rather keep them in one file than repeat shell exports:

```yaml
webSearch:
  braveApiKey: "…"
  serperApiKey: "…"
  tavilyApiKey: "…"
  exaApiKey: "…"
  searxngUrl: "http://127.0.0.1:8080"
  searxngApiKey: "…"       # only when SearXNG sits behind a key-checking gateway
```

Environment variables win over the file, so a one-off `BRAVE_API_KEY=… alran` or a CI override
never has to edit it. As with provider API keys, values in `config.yaml` are stored in plain text —
anyone who can read that file can read them.

SearXNG expects `/search?q=…&format=json`; an IPv6 literal stays in brackets
(`SEARXNG_URL='http://[::1]:8080'`). If that instance sits behind a key-checking gateway, set
`SEARXNG_API_KEY` too — it is sent as `X-Api-Key`.

All providers return the same `title` / `url` / `snippet` shape and honour `count` and
`freshness`. On a host where keyless Exa cannot work, set `ALRAN_DISABLE_KEYLESS_EXA=1` to skip it:
a signed-in install then uses the managed search route, and with neither the tool is not registered
at all. The host notes at start which option to set rather than offering a tool that can only fail.

### 4. Try it: build the pocket pet

Clone this repository and copy the starter into a separate directory:

```bash
git clone https://github.com/Alran-AI/code.git
cd alran-code
node examples/pocket-pet/setup.mjs ../my-pocket-pet
cd ../my-pocket-pet
node serve.mjs
```

Open `http://127.0.0.1:4173`. In a second terminal, open `alran` in `my-pocket-pet` and paste [the first prompt](examples/pocket-pet/README.md#first-request), then [the follow-up](examples/pocket-pet/README.md#change-the-requirement). Refresh the browser after each change.

Prefer to try the result first? From the repository root, run `node examples/pocket-pet/serve.mjs finished` and open the same URL. Add `?demo=1` for the visibly labeled 10-second mode.

[Full walkthrough and requirements](examples/pocket-pet) · [Small code-repair example](examples/clamp) · [Models, search, and tools](docs/examples.md)


### Work in your own project

Open the project you want to work on:

```bash
cd /path/to/your/project
alran
```

Describe your task in the TUI, or submit it directly when you launch Alran:

```bash
alran "Find a failing test, fix the implementation, and run the relevant tests."
```

Use `alran init .` to generate or update project guidance in `AGENTS.md`. Describe the expected result, allowed changes, and how to verify the task.

| Entry point | Command | Use it for |
| --- | --- | --- |
| Interactive TUI | `alran [prompt]` | Explore code, continue a conversation, and review changes or permissions. |
| Headless | `alran exec [prompt]` | Shell scripts, CI, batch work, and evaluations. |
| ACP | `alran acp` | Editors and clients supporting Agent Client Protocol. |
| TypeScript SDK | [`@ottili/alran-code-sdk`](packages/code-sdk/README.md) | Drive `alran exec` from Node.js code: start, stream and resume conversations. |

### Lightweight conversations

For simple conversation or general knowledge questions, start a new Session with
`--mode lightweight`:

```bash
alran --mode lightweight "Explain how DNS caching works."
alran exec --mode lightweight "Summarize the CAP theorem."
```

Lightweight mode sends a small conversational system prompt and no tool schemas. It omits workspace
instructions, Skills, memory blocks, MCP schemas, and the full environment block from provider
context, so it cannot inspect or change local files. Start a new standard Session for coding or tool use with
`alran --mode standard` or `alran exec --mode standard`; omitting `--mode` is identical to standard
mode.

The mode is fixed when a root Session is created. `--mode lightweight` therefore cannot be combined
with `--session` or `--continue`. Child/sub-agent Sessions do not inherit it, `/compact` continues to
use the standard compaction context, and ACP and desktop Sessions remain standard. Reopening a
lightweight Session keeps its mode and shows `Lightweight` in the TUI status line; opening a standard
Session from a lightweight launch remains standard and shows no indicator.

### Continue your work

```bash
# Resume the latest session in the current workspace
alran --continue

# Open the session picker
alran --session
```

Inside the TUI, use `/sessions` to find previous sessions and `/help` to see all commands and shortcuts.

| Action | Shortcut |
| --- | --- |
| Send a message or steer the running task | `Enter` |
| Queue a follow-up while a task is running | `Alt+Enter` |
| Insert a newline | `Shift+Enter` |
| Reference a workspace file or directory | `@` |
| Toggle Plan Mode | `Shift+Tab` |
| Switch permission modes | `Alt+M` |
| Close a panel or interrupt a running task; interrupting before the model replies returns the message to the composer | `Esc` |

## Uninstall

Close running Alran sessions, including editor integrations, before uninstalling. First locate the command with `command -v alran` (macOS / Linux / WSL) or `Get-Command alran -All` (PowerShell), then follow the matching installation method below. The current official install scripts do **not** provide an uninstall flag.

### Installed with the script

The commands below remove the default installation directory, including both launchers, downloaded releases, and any installer-managed Node.js runtime. If you used `ALRAN_INSTALL_DIR`, substitute the actual installation directory. Inspect it first: earlier source builds used `~/.alran-code` for user data, and a custom data directory can overlap the installation. Back up any configuration or sessions you want to keep before deleting it.

**macOS / Linux / WSL**

```bash
rm -rf -- "$HOME/.alran-code"
```

Remove the `# Alran Code CLI` comment and its following PATH line from the shell file the installer updated: `~/.zshrc` for zsh; the first existing file among `~/.bashrc`, `~/.bash_profile`, and `~/.profile` for bash (or a newly created `~/.bashrc`); `~/.config/fish/config.fish` for fish; or `~/.profile` for other shells. The line is `export PATH="/absolute/install/path/bin:$PATH"`, or `fish_add_path -g "/absolute/install/path/bin"` for fish. Remove only the Alran entry, preserving other PATH settings. The installer skips this edit when `ALRAN_NO_MODIFY_PATH` is set or the path is already present.

**Windows (PowerShell)**

```powershell
Remove-Item -LiteralPath "$env:USERPROFILE\.alran-code" -Recurse -Force
```

Open **Edit environment variables for your account**, edit the user **Path**, and remove only the installation directory entry (by default `%USERPROFILE%\.alran-code`, which may appear as an expanded absolute path). The Windows installer updates the user Path, not the PowerShell profile; `ALRAN_NO_MODIFY_PATH` skips that persistent update.

### Installed with npm or from source

For a global npm installation, use the same npm installation/prefix you used to install Alran:

```bash
npm uninstall -g alran
```

For a source build, save any work and remove only the checkout you created; see [Update or remove](docs/installation.md#update-or-remove).

After uninstalling, reopen your terminal (fully restart the editor for integrated terminals) and run `command -v alran` or `Get-Command alran -All` again. No result means the command is no longer on PATH. If another copy appears, identify its installation method before removing it.

### Optional: delete user data

Removing the program leaves separately stored user data in place. To also delete local login state, provider configuration, caches, and sessions, first confirm the selected directory using [Accounts and data](docs/installation.md#accounts-and-data) and back up anything you need. Other Alran installations can share this directory. For the default `~/.alran` directory only:

```bash
# macOS / Linux / WSL — permanently deletes the default user data
rm -rf -- "$HOME/.alran"
```

```powershell
# Windows — permanently deletes the default user data
Remove-Item -LiteralPath "$env:USERPROFILE\.alran" -Recurse -Force
```

A profile uses `~/.alran-<profile>`; `ALRAN_DATA_DIR` or `ALRAN_DATA_DIR` can select a different location. Remove only the specific directories you intend to discard, without wildcard deletion. Remove any Alran-specific environment variable assignments you added to shell profiles or user environment settings if you no longer need them.

## What you can do

| Task | Capabilities |
| --- | --- |
| **Edit and verify code** | Read files, inspect diffs, run shell commands and tests, and control tool execution with permissions and sandboxing. |
| **Choose your model** | Use the Ottili AI Platform with an Ottili API key, or custom providers with OpenAI- or Anthropic-compatible API formats. |
| **Search and work with media** | Use built-in search, `alran-tools` media tools, MCP, and managed connectors, subject to account access and service credits. |
| **Keep work moving** | Resume sessions, plan tasks, use subagents, and extend the agent from the Plugin Store, local plugins, the Skill Library and built-in skills. |
| **Connect your workflow** | Run scripted tasks with the headless CLI, or connect compatible editors and clients through ACP. |

Account features, updates, feedback, and diagnostics are also included. Managed tools require network access and the relevant authorization. See [capabilities and service boundaries](docs/tui-capabilities.md) for details.


## Build from source

To develop Alran or run this source checkout, you need Git, **Node.js 22.19+ (22.x), 24.2+ (24.x), 25, or 26**, and **pnpm 9.12.0**. On Windows, keep the checkout on a local NTFS volume and outside cloud-synced folders; the preflight command below checks the volume before pnpm creates workspace links.
```bash
git clone https://github.com/Alran-AI/code.git
cd alran-code
node scripts/check-windows-source-location.mjs
pnpm install --frozen-lockfile
pnpm build
pnpm alran
```

The first build requires an internet connection. Dependencies and the integrity-checked `alran-tools` bundle come from public npm. See the [source installation guide](docs/installation.md) for pnpm setup, system dependencies, and updates.

From the source directory, use `pnpm alran` in place of `alran` in the examples above. To work on your own project, open its directory and launch the built CLI:

```bash
node /absolute/path/to/alran-code/dist/cli.js
```

This repository targets the **0.6.3 source preview**. Installing the published package and building this checkout are separate paths. Matching versions do not prove identical build provenance; see the [version and evidence baseline](docs/open-source-status.md#version-and-evidence-baseline).

## Documentation and contributing

- [Installation and updates](docs/installation.md) · [Examples](docs/examples.md) · [TUI status line](packages/tui/docs/status-line-config.md)
- [Contributor guide](CONTRIBUTING.md) · [Report a bug or propose an idea](https://github.com/Alran-AI/code/issues/new/choose) · [Report a security issue](SECURITY.md)
- [All documentation](docs/README.md): architecture, capability coverage, verification records, source synchronization, and release preparation.

For now, code and documentation pull requests are accepted only from repository collaborators. If you are not a collaborator but have an idea or proposal, please [open an issue](https://github.com/Alran-AI/code/issues/new/choose) so we can discuss it. Remove secrets, account details, and private project content from reports.

## Support

- Bugs, questions and ideas: [GitHub Issues](https://github.com/Alran-AI/code/issues/new/choose).
  Include `alran --version`, your interface (TUI, `exec`, ACP) and a minimal reproduction; remove
  credentials and private project content.
- Security issues: report privately as described in [SECURITY.md](SECURITY.md).
- The download page for your account: Ottili Console → Developer → Alran Code, or Ottili AI Platform
  → Settings → CLI.

## License

Alran Code includes MIT-licensed upstream material. The upstream copyright notice, its license text and the list of modifications are in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

First-party code defaults to [MIT](LICENSE). Existing file-level and package-level licenses remain in place. See [third-party notices](THIRD_PARTY_NOTICES.md) and [license status](LICENSE-STATUS.md) for dependencies, assets, and `alran-tools`.
