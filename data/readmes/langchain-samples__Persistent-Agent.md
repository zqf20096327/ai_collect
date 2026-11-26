<div align="center">
  <img alt="Persistent Agent" src="channels/assets/icon.png" width="120">
  <h1>Persistent Agent</h1>
  <h3>An always-on assistant for your whole team, in one Slack bot.</h3>
</div>

<div align="center">
  <a href="https://opensource.org/licenses/MIT" target="_blank"><img src="https://img.shields.io/badge/license-MIT-blue" alt="License"></a>
  <a href="https://docs.langchain.com/langsmith/python/managed-deep-agents-overview" target="_blank"><img src="https://img.shields.io/badge/Built%20on-Managed%20Deep%20Agents-blue" alt="Built on Managed Deep Agents"></a>
  <a href="https://x.com/langchain" target="_blank"><img src="https://img.shields.io/twitter/url/https/twitter.com/langchain.svg?style=social&label=Follow%20%40LangChain" alt="Twitter / X"></a>
</div>

<br>

Persistent Agent is a proactive, always-on, goal-oriented agent. Think Muse or Instinct, but
for the enterprise. Comes with memory, browser use, hundreds of tools, and proactive playbooks
it can run in the background to take work off your plate. Built on
[Managed Deep Agents](https://docs.langchain.com/langsmith/python/managed-deep-agents-overview)
(MDA).

<img src="docs/images/slack-welcome.png" alt="A first Slack conversation: the agent greets Liam, lists his connected apps, and offers a Morning Brief, Weekly Planner, and Watchlist" width="960">

**Features include:**

- **Personal memory**: remembers each user's preferences and decisions
- **Goals**: tracks each user's goals and works in the background to advance them
- **Dreaming**: runs a nightly job to clean up and consolidate memory
- **Playbooks**: give it the workflows and organizational knowledge you want your team to adopt
- **Watch mode**: reads every message in channels and speaks up only when it can help
- **Background work**: runs research and review subagents asynchronously
- **Integrations**: uses LangSmith Tool Gateway to access tools such as Gmail, GitHub, Slack, and Linear
- **Browser use**: interacts with websites through a browser

## Quickstart

**You'll need:**

- [uv](https://docs.astral.sh/uv/getting-started/installation/) (it installs the right Python for you)
- A [LangSmith](https://smith.langchain.com) workspace on a Plus or Enterprise plan
- A model: an [Anthropic](https://console.anthropic.com/settings/keys) or
  [OpenAI](https://platform.openai.com/api-keys) API key, or the
  [LangSmith LLM Gateway](#optional-use-the-llm-gateway)
- A Slack workspace where you can install apps

### 1. Clone and install

```bash
git clone https://github.com/langchain-samples/Persistent-Agent.git
cd Persistent-Agent
uv sync
cp .env.example .env
```

### 2. Get a key and connect tools

- **Create a LangSmith personal access token (PAT) and copy your workspace ID.** [Step-by-step instructions →](#langsmith-api-key-and-workspace)
- **Connect built-in tools such as Slack and copy your tool kit's MCP URL.** [Step-by-step instructions →](#tool-server-setup)

### 3. Fill in `.env`

First, fill in the three values you collected in step 2:

```dotenv
LANGSMITH_API_KEY=<your-langsmith-personal-access-token>
LANGSMITH_WORKSPACE_ID=<your-workspace-id>
TOOLS_MCP_URL=<your-tool-kit-mcp-url>
```

#### Configure the language model

Add these lines to the same `.env` file to use **Claude Opus directly through Anthropic**.
The Anthropic key authorizes and pays for model calls; it is separate from your LangSmith PAT.
Get it from the [Anthropic console](https://console.anthropic.com/settings/keys).

```dotenv
AGENT_MODEL=anthropic:claude-opus-5-5
ANTHROPIC_API_KEY=<your-anthropic-api-key>
```

For GPT with an OpenAI key or the optional LLM Gateway, see the
[model setup deep dive](#model-options). Choose one model configuration.

Keep `.env` private.

### 4. Deploy and open Slack

```bash
uv run mda deploy
```

Run this from the repository directory with your PAT saved in `.env`. If your shell already
exports a LangSmith key, follow the [environment loading help](#does-deploy-need-an-exported-api-key)
to avoid deploying with the wrong credential.

Open the Slack authorization link if prompted, approve the app, then return to the terminal
and press **Enter**. When deployment finishes, DM the bot **“hi”** and follow any app
connection prompts. [Slack setup and first-run checks →](#deploy-and-connect-slack)

---

## Detailed setup

- [LangSmith API key and workspace](#langsmith-api-key-and-workspace)
- [Tool Server: add a server, connect an account, create a kit, copy its URL](#tool-server-setup)
- [Deploy and connect Slack](#deploy-and-connect-slack)
- [Model options, including the optional LLM Gateway](#model-options)
- [Troubleshooting](#setup-troubleshooting)

Screenshots below show the LangSmith UI captured on November 25, 2026. They are cropped to
focus on the relevant controls. Names such as **Demo Workspace** are examples; use your own
workspace throughout.

## LangSmith API key and workspace

**Use a Personal Access Token (PAT) for this setup.** If you already created one,
keep using it in `LANGSMITH_API_KEY` throughout this walkthrough.

There are three different kinds of access involved. Setting up one does not configure the others:

| What you need | What it does | Where it goes |
|---|---|---|
| **LangSmith API key** | Authenticates the CLI to LangSmith for deployment and local development. | `LANGSMITH_API_KEY` in `.env`. |
| **Model provider API key** | Pays for and authorizes model calls, such as Anthropic or OpenAI. | `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` in `.env` for the direct-provider setup. |
| **Connected app account** | Lets tools access a person's Google, Linear, GitHub, or other account. | Connected in LangSmith or through the bot's sign-in link; not pasted into `.env`. |

### 1. Choose your workspace and copy its ID

1. Open [LangSmith](https://smith.langchain.com) and select your organization and workspace
   using the selector at the top left.
2. Open **Settings** and select **Workspace**.
3. Check the workspace name, then click the copy icon next to it (**Copy workspace ID**).
4. Put that value in `.env` as `LANGSMITH_WORKSPACE_ID`.

<img src="docs/images/setup/workspace-id.jpg" alt="Workspace settings with the Workspace tab selected and a copy icon beside Demo Workspace" width="350">

Use the **workspace ID**, not the organization ID. In the classic settings UI, the workspace
ID is under **Settings → Workspace → General**. The key, tool kit, and deployment should all
refer to this same workspace.

### 2. Create a personal access token for the quickstart

1. In **Settings**, select **Organization → API Keys**.
2. Click **Create API key**.
3. Enter a description, such as `persistent-agent`.
4. Choose **Personal Access Token**.
5. Set **Default Workspace** to the workspace from step 1 and choose an expiration.
6. Click **Create API Key** and copy the value shown once into `LANGSMITH_API_KEY` in `.env`.

<img src="docs/images/setup/personal-access-token.jpg" alt="Create an API Key dialog with Personal Access Token selected, a default workspace, and expiration options" width="720">

**Check before continuing:** `.env` has both `LANGSMITH_API_KEY` and
`LANGSMITH_WORKSPACE_ID`. A personal access token inherits your permissions; it does not
make you a workspace admin if you were not already one.

### How your PAT selects a workspace

Your PAT inherits your access to LangSmith. Its **Default Workspace** tells LangSmith where
to route requests when no workspace is specified; it does not restrict the PAT to that
workspace. Set `LANGSMITH_WORKSPACE_ID` explicitly to choose where this agent deploys.
That setting does not grant any additional permissions.

See [LangSmith API keys](https://docs.langchain.com/langsmith/create-account-api-key)
for more on permissions and key management.

## Tool Server setup

The feature called **Tool Server** in this walkthrough is documented as
[Tool Gateway](https://docs.langchain.com/langsmith/tool-gateway) and appears as **Tools** in
LangSmith. It connects the agent to apps. The **LLM Gateway** handles model calls and is a
separate, optional feature.

You will do four things: **choose a built-in integration (or add a custom server) → connect
your account if required → select tools in a kit → copy the kit's MCP URL into `.env`**.
LangSmith hosts this layer; you do not run a separate Tool Server process on your laptop.

### 1. Choose your tools: start with the built-ins

**LangSmith provides built-in integrations you can select directly.** You do not need to
click **Add MCP server**, find an MCP URL, or host a server for any of these integrations.
Choose the services you want, connect your accounts where required, and select their tools
for your kit.

| How you connect | Built-in integrations |
|---|---|
| **Sign in and authorize access (OAuth)** | Excel, GitHub, Gmail, Google BigQuery, Google Calendar, Google Docs, Google Drive, Google Meet, Google Sheets, Google Slides, Linear, LinkedIn, OneDrive, Outlook, PowerPoint, Salesforce, SharePoint, Slack, Teams, Word, X |
| **Provide an API key from the service** | Apollo, Ashby, Exa, Pylon, Tavily |
| **No credentials needed** | Base, Parallel |

See the [official built-in list](https://docs.langchain.com/langsmith/tool-gateway-servers#use-a-built-in-server)
for the latest available integrations and authentication requirements.

1. Open **Tools → MCP servers** in LangSmith.
2. Select **You** under **Connected as**, and **Workspace** for server scope.
3. Set the server source filter to **Built-in**, then search for an integration from the table above.
4. Choose the entry labeled **Built-in**. Your workspace may also have custom servers with
   similar names; you do not need to create another one.
5. Follow [Connect your account](#2-connect-your-account) below, then add its tools to your kit.

<img src="docs/images/setup/built-in-integrations.jpg" alt="MCP servers filtered to Built-in, with You and Workspace selected, showing integrations and their connection status" width="960">

Click an integration's name to preview its tools. For example, Gmail provides tools to
read, draft, and send email. A visible tool list does not mean your account is connected;
check the connection status before continuing.

<img src="docs/images/setup/built-in-tools.jpg" alt="Built-in Gmail tool preview listing email tools while the account status is Not connected" width="672">

**Built-in means no server registration.** Integrations that require OAuth or an API key
still need a connected account. Every integration's tools must be selected in your kit
before this agent can use them.

#### Optional: add a custom server or a public test tool

Use **Add MCP server** for your own MCP endpoint or a service that is not already available
in the list. Skip this section if you are using only built-in integrations.

For a first test without another app login, you can add the public LangChain documentation
server. It gives you a concrete tool to test after deployment:

1. Open **Tools** in the LangSmith sidebar, then select **MCP servers**.
2. Select **You** under **Connected as**, and **Workspace** for server scope.
3. Search for `docs-langchain`. If your workspace already has the server at
   `https://docs.langchain.com/mcp`, use it and skip adding a duplicate.
4. Otherwise, click **Add MCP server** and enter:

   | Field | Value |
   |---|---|
   | **Name** | `docs-langchain` |
   | **URL** | `https://docs.langchain.com/mcp` |
   | **Authentication** | **Public** |

5. Click **Add server** at the bottom of the panel.

<img src="docs/images/setup/public-server.jpg" alt="Add MCP server filled with docs-langchain, https://docs.langchain.com/mcp, and Public authentication" width="704">

**Expected result:** the server appears as **Connected**. Public servers do not have an
account sign-in step. Continue to [create your tool kit](#3-create-a-workspace-tool-kit),
or add the apps you want below first.

### 2. Connect your account

1. In **Tools → MCP servers**, keep **You** and **Workspace** selected and find your integration.
2. If it needs credentials, click **Connect** on its **Built-in** entry. If it already shows **Connected**,
   continue to [create your tool kit](#3-create-a-workspace-tool-kit).
3. Complete the connection method listed in the table above:
   - **OAuth:** sign in to the service, choose the account or workspace you intend to use,
     and review and approve the requested access. Complete admin approval if required.
   - **API key:** enter a key from that service in the connection form. This is the
     service's own key, not your LangSmith API key.
   - **No credentials:** skip the connection step and go straight to selecting tools.
4. After connecting, return to **MCP servers** and confirm the integration shows **Connected**.
5. [Create or edit your tool kit](#3-create-a-workspace-tool-kit), filter for the integration, and
   select the tools you want the agent to have.

Repeat for other built-in apps you want to use. Each person who uses the bot will connect
their own accounts later; your connection does not authorize their accounts.

**Connecting Slack here is separate from installing the agent's Slack bot.** This step gives
the agent access to Slack tools through your account. The [deployment step](#deploy-and-connect-slack)
installs the bot you talk to. Neither step requires manually registering a Slack MCP server.

<details>
<summary>Optional: connect a custom OAuth MCP server</summary>

If you deliberately want a separate remote MCP endpoint, you can register it yourself.
For example, the screenshot below shows Linear's remote endpoint. **Linear also has a
built-in integration; use that for the simpler setup.** This custom example is optional.

1. In **Tools → MCP servers**, keep **You** and **Workspace** selected.
2. Check whether the endpoint is already registered. If it is, use the existing entry.
   Otherwise, click **Add MCP server**.
3. For this example, enter **Name:** `Linear` and **URL:** `https://mcp.linear.app/mcp`.
4. Select **OAuth**, leave **OAuth Setup** as **Automatic OAuth**, and click **Add server**.

<img src="docs/images/setup/add-mcp-server.jpg" alt="Optional custom Linear MCP server setup with OAuth and Automatic OAuth selected; the built-in Linear integration needs no server registration" width="704">

5. Click **Connect** on the server's row, complete the provider's authorization flow,
   and confirm **Connected** before selecting its tools in your kit.

</details>

#### Why do I have to connect before I can add tools for my users?

The kit editor needs to discover the server's tools. An authenticated server can require
**your connection to load that list**, even though the kit is intended for other people.
An unconnected server can show exactly this message:

<img src="docs/images/setup/connect-before-tools.jpg" alt="Linear is Not connected and says: Tool preview is unavailable. Connect to load the tool list." width="672">

There are two separate steps:

- **You, the kit creator:** connect an account so the editor can load the tools and let you
  select them. This is setup-time tool discovery.
- **Each person using the bot:** connect their own account through the bot's private
  sign-in link. This is the account used for their tool calls.

Choosing **Workspace** for the kit shares its tool selection; it does not by itself share
your personal OAuth credentials. The template uses each person's own connected accounts.
For a custom server that uses API keys, choose per-person credentials if each person should
use their own access; workspace credentials or a shared profile deliberately use shared access.

If the picker is empty, go back to **MCP servers**, finish **Connect**, and reopen the kit
editor. If it reports a rejected workspace credential, the workspace admin must fix that
server's credential; creating another kit will not fix it.

### 3. Create a workspace tool kit

1. Open **Tools → Tool kits**.
2. Select **Workspace**, then click **Create tool kit**.
3. Name the kit `persistent-agent`.
4. Under **Who can use this tool kit**, select **Workspace**.

<img src="docs/images/setup/create-tool-kit.jpg" alt="Create tool kit named persistent-agent with Workspace selected so everyone in the workspace can use it" width="704">

**Use Workspace for this shared bot.** A Personal kit is visible and usable only by its owner,
and a workspace kit can include only workspace servers and built-in integrations. If you
cannot create a workspace kit, ask a workspace admin to create it for this deployment.

5. Search or filter by server and check the tools you want to include. For the starter
   example, search `search_docs` and check **search_docs_by_lang_chain** from **docs-langchain**.
   For built-in Slack or another app, filter by that app and select its read/search tools
   to start with; add write tools when needed.

<img src="docs/images/setup/select-tool.jpg" alt="Tool picker with search_docs_by_lang_chain selected from the docs-langchain server" width="704">

6. Click **Review tool selection** at the bottom of the panel.
7. Confirm the selected tools, leave custom labels blank unless you need them, and click
   **Create tool kit**.

**Expected result:** your kit appears in the **Workspace** list with at least one tool.
A kit with zero tools does not give the agent any app capabilities.

### 4. Copy the kit's MCP URL into `.env`

1. Click your kit's name to open its details.
2. Find **MCP URL** and click the copy icon beside it.
3. Paste that complete URL into `TOOLS_MCP_URL` in `.env`.

<img src="docs/images/setup/kit-mcp-url.jpg" alt="An example saved tool kit showing its tools and the MCP URL copy button; the example URL is redacted" width="672">

*This screenshot uses an existing example kit. Open your own `persistent-agent` kit and copy
its URL; do not copy a URL from a screenshot.*

For the GCP US region, the URL has this shape:

```dotenv
TOOLS_MCP_URL=https://api.smith.langchain.com/v1/managed-tools/kits/<your-kit-id>/mcp
```

Use the URL LangSmith gives you, including your region's host. It is **not** the browser's
`smith.langchain.com/.../tools` address or the upstream service's MCP URL.

[`tools/mcp.py`](tools/mcp.py) already connects this kit with LangSmith authentication and
adds `?mode=search` so the agent can find relevant tools. You do not need to paste the UI's
sample MCP code into the project or put an API key in the URL.

**Check before deploying:** the kit and `LANGSMITH_WORKSPACE_ID` belong to the same workspace,
and the kit contains the tools you want to use. After changing `.env`, run
`uv run mda deploy` again to update the deployment.

### 5. Let each teammate connect their own apps

After the bot is deployed:

1. Have the teammate open a **DM** with the bot and send “hi”.
2. If the bot sends a connection link, have that teammate open it and sign in to their own
   account. Do not forward your own connection link to them.
3. Complete the requested connections, return to the DM, and retry the request if needed.
4. Test a read-only request, such as “List my Linear issues,” using an app in your kit.

The template does not enable just-in-time MCP authentication, so missing connections may be
requested before the first run starts. For an easy first run, keep the kit small. Public
servers such as the documentation server need no per-person connection.

The Slack bot installation and a person's Slack **tool** connection are separate: installing
the bot makes it reachable in Slack; connecting a tool account authorizes that person's tool use.

## Deploy and connect Slack

The repository already includes the Slack channel declaration in
[`channels/slack.py`](channels/slack.py). You do not need to write a Slack app manifest or
add bot tokens to `.env` for this managed setup.

1. From the repository directory, run `uv run mda deploy`.
2. Follow any workspace selection prompts and confirm the target is the workspace used
   for your API key and tool kit.
3. If the terminal prints a Slack authorization link, open it and select the intended
   Slack workspace. Review the requested permissions and approve the app. If your workspace
   requires admin approval, have the admin complete it before continuing.
4. Return to the terminal and press **Enter** when prompted. If Slack is already authorized,
   this authorization step may be skipped.
5. Wait for the CLI to finish. Open its deployment dashboard URL and check that the
   deployment is ready. If it fails, open the revision logs before retrying.
6. Open the bot's DM in Slack. It may send the first message after deployment; otherwise,
   find it under Slack's apps and send “hi”. Complete any personal app connection prompts.
7. For the starter documentation kit, ask: **“Use the LangChain documentation tool to
   explain how Managed Deep Agents schedules work.”** For another kit, ask a read-only
   question using one of its tools. In LangSmith Studio or the run trace, confirm a tool
   call appears and the bot returns an answer.

**You’re ready when:** the deployment is ready, the bot replies in Slack, and a tool call
succeeds using the caller’s connected account (or the public documentation server).

`mda deploy` reads `.env` and forwards non-reserved settings and provider keys to the hosted
deployment. The LangSmith key authenticates deployment; the hosted runtime manages its own
platform authentication. You do not need to keep the terminal running after deployment.

Once DMs work, add the bot to a channel if you want shared conversations. This template uses
watch mode there: it reads messages and stays quiet when it has nothing useful to add.

## Model options

All three options are supported by the installed dependencies. Choose one `AGENT_MODEL`;
the agent does not automatically switch providers when a key is missing or a model fails.

| Option | `AGENT_MODEL` | Credentials |
|---|---|---|
| **Claude Opus — default** | `anthropic:claude-opus-5-5` | `ANTHROPIC_API_KEY` in `.env`. |
| **GPT — direct OpenAI** | `openai:gpt-6.1-sol` | `OPENAI_API_KEY` in `.env`. |
| **LLM Gateway — Opus example** | `langsmith:anthropic/claude-opus-5-5` | LangSmith gateway access and an Anthropic provider secret in the deployment's workspace. |

**Tool Gateway works with all three.** Keep the same `TOOLS_MCP_URL` to use your connected
apps regardless of the selected model. The LLM Gateway selects and routes model calls;
Tool Gateway supplies tools. Every option still needs LangSmith deployment access.

### Use your own provider key

Choose **one** configuration in `.env` and redeploy. Replace or comment out the previous
`AGENT_MODEL` line so there is only one active value. Direct Opus is the default when
`AGENT_MODEL` is unset or empty. Both provider packages are already included in this repository.
An Anthropic API key requires API billing; a Claude chat subscription alone does not supply it.

**Claude Opus (the default and quickstart):**

```dotenv
AGENT_MODEL=anthropic:claude-opus-5-5
ANTHROPIC_API_KEY=<your-anthropic-api-key>
```

**OpenAI:**

```dotenv
AGENT_MODEL=openai:gpt-6.1-sol
OPENAI_API_KEY=<your-openai-api-key>
```

Use a model your provider account can access. Keep `LANGSMITH_API_KEY`,
`LANGSMITH_WORKSPACE_ID`, and `TOOLS_MCP_URL` from the quickstart in either case. They still
configure deployment and tools even when model calls go directly to the provider.

### Optional: use the LLM Gateway

Skip this section if you followed the direct-provider quickstart. The gateway is useful
when your team wants centrally managed model credentials and policies.

1. In LangSmith, select the **same workspace** as your deployment.
2. In **Settings → Workspace → Secrets**, add your provider key as a workspace secret
   named `ANTHROPIC_API_KEY` (or the name required by your provider). The gateway reads it
   from that workspace; a key only in your local `.env` does not configure the gateway.
3. Keep using your PAT. Set its **Default Workspace** to the deployment's workspace and
   make sure your permissions include `gateway:invoke` and `workspaces:read`. The gateway
   uses the PAT's default workspace; setting `LANGSMITH_WORKSPACE_ID` alone does not change it.
4. Use **LLM Gateway → Simulator** to verify that the selected model works in that workspace.
5. Set the model in `.env`, then redeploy:

   ```dotenv
   AGENT_MODEL=langsmith:anthropic/claude-opus-5-5
   ```

This explicitly opts into gateway routing. You can use another model available in your
gateway by changing the provider/model portion of the value. To switch back, set a direct `anthropic:` or `openai:` model plus its provider key as shown
above, and redeploy.

See [gateway setup](https://docs.langchain.com/langsmith/llm-gateway-admin-setup),
[authentication](https://docs.langchain.com/langsmith/llm-gateway-authentication), and
[provider keys](https://docs.langchain.com/langsmith/llm-gateway-provider-authentication).

## Setup troubleshooting

| What you see | What to check |
|---|---|
| No **Tools** page or workspace kit creation unavailable | Check the LangSmith plan, supported region, selected workspace, and Workspace Admin access. See [Tool Gateway availability](https://docs.langchain.com/langsmith/tool-gateway). |
| No tools in the kit picker | Connect the server as **You** first. Check the **Workspace/Personal** scope and server filter, then reopen the editor. A registered OAuth server alone is not a connected account. |
| “Tool preview is unavailable” | Finish the provider's **Connect** flow, wait for success, and return to LangSmith. |
| A server reports an invalid workspace credential | Ask its workspace admin to update that server's credential; retry loading tools afterward. |
| LangSmith `401` / `403`, or deployment goes to the wrong workspace | Check key expiration, key permissions, `LANGSMITH_WORKSPACE_ID`, and region. A tracing-only key cannot deploy. |
| Model authentication error or unexpected LLM Gateway error | Check that there is one active `AGENT_MODEL` line. Use `anthropic:...` with `ANTHROPIC_API_KEY`, or `openai:...` with `OPENAI_API_KEY`, then redeploy. |
| Bot replies but cannot use apps | Confirm `TOOLS_MCP_URL` is the saved kit's MCP URL, the kit contains tools, and the deployment was updated after changing `.env`. Finish the caller's connection prompts. |
| A teammate cannot use your kit | Use a **Workspace** kit with workspace servers or built-in integrations, and have the teammate connect their own accounts. |
| Bot asks you to connect before it answers | The kit includes authenticated servers you have not connected. Complete the DM links or start with the public documentation tool only. |
| Slack authorization does not finish | Complete Slack admin approval, then return to the terminal and press Enter when prompted. |
| `Cannot change target.agent_id on an existing channel` | Keep the agent name the Slack app was created with, or follow the [architecture troubleshooting](docs/architecture.md#troubleshooting) before recreating the integration. |

For another LangSmith region, set `LANGSMITH_ENDPOINT` before the first deployment using the
[region table](https://docs.langchain.com/langsmith/python/managed-deep-agents-deploy#select-a-saas-region).
Use keys and a tool kit from that same region.

### Does deploy need an exported API key?

The CLI supports reading your PAT from the project's `.env`. However, testing has also
shown an exported shell key taking precedence, despite the
[deployment documentation](https://docs.langchain.com/langsmith/python/managed-deep-agents-deploy#secrets-and-environment-files)
describing `.env` first. If your shell automatically sets a LangSmith key, avoid relying
on precedence: run this from the repository directory to remove both key variables from
this command's environment and explicitly load your saved `.env`:

```bash
env -u LANGSMITH_API_KEY -u LANGCHAIN_API_KEY uv run mda deploy --env-file .env
```

This leaves your shell's existing variables unchanged. Keep the PAT in `.env`; you do not
need to paste it into a command. If authentication still fails, check the PAT's expiration,
workspace access, and `uv run mda --version` when reporting the issue.
The PAT authenticates your deployment request; it is not uploaded as a user-managed runtime
secret. Platform-provided runtime credentials are separate and do not require you to create
another key for this walkthrough.

## Use it

| Say | What it does |
|---|---|
| "Send me a morning brief" | Adopts the Morning Brief playbook: your day, each weekday morning. |
| "Every Friday at 4, summarize what I shipped" | Creates a recurring task in your timezone. |
| "Let me know when the release PR is approved" | Records a goal and checks on it hourly until it's done. |
| "Research our top three competitors' pricing" | Hands it to a background subagent and reports back. |
| "After every meeting, send me an action item summary" | Summarizes action items from available meeting notes or transcripts and sends them to you. |
| `!clear` | Forgets everything about you and cancels your schedules. |

Add it to a channel and it stays quiet unless it can help. Mention it to ask directly.

**Fun Slack reactions:** The built-in Slack connection includes an emoji search tool.
Connect Slack and add its emoji search and reaction tools to your kit so your agent can
find and react with your workspace's custom emojis. Try asking: "Use fun Slack emojis
to react to my messages."

## FAQ

### Does everyone get their own agent?

No. Everyone shares one deployment and one Slack bot, but memory, schedules, goals, apps and
browser logins are per person. Personal memory never loads in a shared channel.

### Can it act on its own?

Only within what you've asked. It asks for a yes before booking, buying, sending or deleting
anything, and offers help only rarely.

### How do I change how it behaves?

Edit [`instructions.md`](instructions.md) and the [`skills/`](skills/), then `uv run mda deploy`
again. Add a playbook by adding a skill whose description starts with "Playbook:".

---

## Resources

- [How it works](docs/architecture.md): mechanisms, heartbeat and dreaming, Slack, project structure, customizing, tests and troubleshooting
- [Managed Deep Agents docs](https://docs.langchain.com/langsmith/python/managed-deep-agents-overview): [quickstart](https://docs.langchain.com/langsmith/python/managed-deep-agents-quickstart), [CLI](https://docs.langchain.com/langsmith/python/managed-deep-agents-cli), [schedules](https://docs.langchain.com/langsmith/python/managed-deep-agents-schedules), [memory](https://docs.langchain.com/langsmith/python/managed-deep-agents-memory)
- [Deep Agents](https://github.com/langchain-ai/deepagents): the open source harness underneath

## Security

Tools run with each person's own access. Browser and connect links go only to the person they
belong to, in their DM. Notes, memory, web pages and tool results are data, never instructions,
so don't save secrets in memory.

## License

MIT
