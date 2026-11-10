# GitHub Copilot Evals (Preview)

Create, run and compare tests for your GitHub Copilot skills, custom agents and
MCP tools. Turn a task into an eval, check the output, and keep the result to
compare after your next change.

## What's in the plugin

| Component | What it provides |
| --- | --- |
| Six skills | `create`, `review`, `improve`, `run`, `compare` and `setup` (model-invocable in natural language across all Plugin hosts) |
| Three automation blueprints | Portable `.automation.md` definitions (`eval-health-review`, `eval-smoke-run`, `eval-skill-compare`) for VS Code Agents **Customizations > Automations** |
| `/eval` CLI command | Interactive workflows in Copilot CLI and GitHub Copilot App (`/eval setup`, `/eval create`, `/eval review`, `/eval improve`, `/eval run`, `/eval compare`) |
| Evals Canvas | Visual side-panel workspace to browse project assets, draft evals, inspect outlines/YAML and read saved run reports |
| MCP server | 15-tool Model Context Protocol server (`copilot-evals` via `mcp.json`) bundled with the plugin |

### Skills and commands

Ask in plain language across any Plugin host, or use the `/eval` commands in
Copilot CLI and GitHub Copilot App (the standalone Plugin sets
`user-invocable: false` so skills do not duplicate `/eval` in CLI/App slash
menus; the VS Code extension VSIX projects `user-invocable: true` to expose
`/eval:<skill>` in trusted local desktop VS Code Chat):

| Skill | Copilot CLI / App command | Example request |
| --- | --- | --- |
| `create` | `/eval create` | Create an eval for this agent that checks its output files. |
| `review` | `/eval review` | Review this eval and its saved results. |
| `improve` | `/eval improve` | Add a failure case to this eval and save a revised copy. |
| `run` | `/eval run` | Run this eval. |
| `compare` | `/eval compare` | Compare these two saved runs, or compare this task with and without a skill. |
| `setup` | `/eval setup` | Set up eval paths and test suites for this project. |

## Install

### GitHub Copilot CLI

```text
copilot plugin marketplace add github/evals
copilot plugin install eval@github-copilot-evals
```

Start Copilot CLI in your project and trust the folder if asked. The `/eval`
commands and Evals Canvas currently require Copilot CLI experimental mode.
Enable it in the conversation with `/settings experimental on`, then enter
`/eval help`.

Without experimental mode, you can still ask for the six skills in plain
language, for example, "Review this eval and its saved results." This does not
enable extension-only commands, tools or Canvas.

To update an existing installation:

```text
copilot plugin marketplace update github-copilot-evals
copilot plugin update eval@github-copilot-evals
```

Each release tag and its attached ZIP also include a local marketplace
descriptor so you can extract the archive and register the extracted folder
offline.

### VS Code editor

Install [GitHub Copilot Evals from the Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-evals),
or search Extensions for `GitHub.copilot-evals` from publisher **GitHub**.
The VS Code extension provides the Evals sidebar, Canvas and native VS Code
tools, and bundles the six Evals Plugin skills.

You can also install the standalone Plugin in VS Code using a one-click link
(which installs the six skills and the bundled `copilot-evals` MCP server via
`mcp.json`):

- **Stable (`github/evals`):** [Add marketplace](vscode://chat-plugin/add-marketplace?ref=github%2Fevals) (`vscode://chat-plugin/add-marketplace?ref=github%2Fevals`) or [Install eval Plugin](vscode://chat-plugin/install?source=github%2Fevals&plugin=eval) (`vscode://chat-plugin/install?source=github%2Fevals&plugin=eval`)
- **Prerelease (`github/evals#plugin-preview`):** [Add preview marketplace](vscode://chat-plugin/add-marketplace?ref=github%2Fevals%23plugin-preview) (`vscode://chat-plugin/add-marketplace?ref=github%2Fevals%23plugin-preview`) or [Install preview eval Plugin](vscode://chat-plugin/install?source=github%2Fevals%23plugin-preview&plugin=eval) (`vscode://chat-plugin/install?source=github%2Fevals%23plugin-preview&plugin=eval`)

On older VS Code builds or other harnesses, use **Chat: Open Customizations >
Browse > Configure Marketplaces > Add Marketplace** with `github/evals` (or
`github/evals#plugin-preview` for prerelease).

### VS Code Agents

Install the standalone Plugin in VS Code Agents for the Copilot harness:

1. Choose the Copilot harness and open **Customizations > Browse**.
2. Open the **source menu**, then choose
   **Configure Marketplaces > Add Marketplace** and enter `github/evals`.
3. Return to Browse, select that source and review **eval** in
   **github-copilot-evals** before choosing **Install**.
4. Open **Plugins** to check its enabled state and selected scope, then start
   a fresh project session. Installing the Plugin automatically registers its
   six skills, Evals Canvas and 15-tool `copilot-evals` MCP server (`mcp.json`).

## Create your first eval

1. Open a local project in Copilot CLI or VS Code, trust the folder and sign in
   to GitHub Copilot.
2. Enter `/eval create` (or open the Evals Canvas) and pick a skill, custom
   agent or MCP tool to test.
3. Describe what a passing result should look like. For example, for a
   release-notes skill:

   ```text
   Create an eval for this skill using one completed issue and one open issue.
   Check that the release notes include only completed work, preserve the
   issue IDs, and leave the input files unchanged.
   ```

4. Review the proposed test cases, fixtures and checks, then save the eval.
5. Run `/eval run` (or choose **Review & run** in Canvas). Review the disclosed
   execution effects and token/credit costs, then approve the run.
6. Inspect the saved report with `/eval review` or in the **Results** tab of the
   Evals Canvas to see passing checks, outputs and the conversation trace.

After editing your skill or agent, run the eval again and use `/eval compare` to
compare the new run against the previous saved result.

## Runner setup

Running evals uses the local eval runner. Open the Evals Canvas and go to
**Settings > Advanced > Install eval runner** (or run
**GitHub Copilot Evals: Set up test runner** in VS Code). Use `/eval setup` to
configure project eval folders and test suites.

| Dependency | Minimum | Used for |
| --- | --- | --- |
| Node.js | 24.0.0 (CLI Plugin) / 22.14.0 (VS Code) | Local plugin and runner execution |
| `@microsoft/vally-cli` | 0.19.0 | Eval validation and execution |
| GitHub Copilot CLI | 1.0.85 | Native custom-agent and MCP execution |
| Git | 2.28.0 | Native run isolation |

## Runs and costs

Saving an eval and running it are separate steps. File validation and reading or
comparing saved results make no model calls.

Each eval run or grader test asks you to review its execution effects and
token/credit costs before running. Eval setup scripts, tools, custom graders and
AI judges can execute code and incur charges under your normal local permissions.
A passing check doesn't guarantee the AI will get it right every time.
Saved results are written to `.copilot\evals\results` in your project; review
their contents before sharing them.

## MCP server (`copilot-evals`)

The built plugin includes `mcp.json` at the plugin root (`https://agent-plugins.org/schemas/1.0.0/mcp.schema.json`):

```json
{
  "$schema": "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json",
  "mcpServers": {
    "copilot-evals": {
      "type": "stdio",
      "command": "node",
      "args": [
        "${PLUGIN_ROOT}/dist/mcp/server.mjs"
      ]
    }
  }
}
```

When you install `eval@github-copilot-evals` in Copilot CLI, GitHub Copilot App,
VS Code or VS Code Agents, the host automatically installs and configures the
plugin's tools without requiring you to clone this repository or edit
`.mcp.json` manually. When a plugin host starts `${PLUGIN_ROOT}/dist/mcp/server.mjs`
with its working directory set to `PLUGIN_ROOT`, `copilot-evals` resolves the
project workspace from the host launch environment (`INIT_CWD`, `VSCODE_CWD` or
`PWD`), uses `PLUGIN_DATA` for private temporary staging, and refuses startup if
the project workspace is not resolved.

For standalone MCP clients that do not support Agent Plugins 1.0, extract the
release archive (`github-copilot-evals-plugin-<version>.zip`) and configure
`copilot-evals` in `.mcp.json`:

```json
{
  "mcpServers": {
    "copilot-evals": {
      "command": "node",
      "args": [
        "/path/to/extracted-plugin/packages/plugin/dist/mcp/server.mjs",
        "--workspace",
        "/path/to/project"
      ]
    }
  }
}
```

If the client launches the server in the project root, `--workspace` is optional
and defaults to the current working directory. Run with `--help` or `--version`
to inspect CLI options without starting a stdio session.

Read tools inspect inventory, eval definitions, saved runs, status and saved-run
comparisons. `evals_save_draft` validates and saves new files under your host's
normal tool permissions without an extra save form, while execution and runtime
tools (`evals_run`, `evals_test_graders`, `evals_grader_catalog` and
`evals_configure_runtime`) require host form approval before running commands,
graders or models.

### Verify an extracted release archive

To verify the files in an extracted release ZIP against `distribution.json`:

```text
node scripts/verify.mjs
```

## Telemetry and privacy

Standalone Plugin telemetry is enabled by default in released versions. It
records component activation, Evals workflow requests, approval dispositions,
operation outcomes and error categories, with durations and observed trial
counts. Events also include basic environment and version information and may
include an optional pseudonymous device identifier and hashed session
identifier. These identifiers are pseudonymous, not anonymous.

Telemetry events do not include source code, prompts, model outputs, project
paths, repository names or raw error messages. Saved evaluation results remain
local and are not exported as product analytics.

To turn off standalone Plugin telemetry, set any one of these environment
variables before starting the host application:

- `COPILOT_EVALS_TELEMETRY=off`
- `DO_NOT_TRACK=1`
- `OTEL_SDK_DISABLED=true`

When the Plugin identifies an editor host, it does not send its own telemetry
without an explicit host-consent bridge; no such bridge is currently
implemented. The VS Code extension's separate telemetry follows VS Code's
`telemetry.telemetryLevel` setting. Turning off telemetry does not turn off
evals or delete saved results.

See `packages/plugin/TELEMETRY.md` in the release archive, the [GitHub Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement)
and the [Microsoft Privacy Statement](https://privacy.microsoft.com/privacystatement).

## License

This project is source available under the GitHub Limited Use Source License. It
is not open-source software. You may inspect and contribute to the code and use
it internally with Authorized Tooling, but you may not monetize it, offer it as a
product or service, or use it with unauthorized tooling. By submitting a
contribution, you agree to the contribution terms in Section 6 of the License.
See [LICENSE](./LICENSE) for the full terms.

## Maintainers

The GitHub Copilot Evals team (@github/code-ai-evals) maintains this project. See
[CODEOWNERS](.github/CODEOWNERS).

## Support

See [SUPPORT.md](SUPPORT.md) or [open an issue](https://github.com/github/evals/issues).
To report a security issue, follow [SECURITY.md](SECURITY.md) instead of opening
a public issue.

## Acknowledgement

GitHub Copilot Evals runs evals with Microsoft's Vally eval engine and builds on
the open source projects listed in
`packages/plugin/THIRD-PARTY-NOTICES.txt` in the release archive.
Thank you to everyone who maintains them.
