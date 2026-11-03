# Copilot Studio MCP

Microsoft Copilot Studio MCP brings Copilot Studio tools into Model Context
Protocol (MCP)-compatible CLIs, developer tools, and agentic interfaces. It
provides a single entry point for working across the agent and automation
lifecycle, from creation and configuration to testing, deployment, monitoring,
and ongoing management.

This repository hosts the source for the MCP server. The server itself is
published and installed from the npm package
[`@microsoft/copilot-studio-mcp`](https://www.npmjs.com/package/@microsoft/copilot-studio-mcp).
It's also discoverable through the
[GitHub MCP Registry](https://github.com/mcp?query=copilot-studio) and the
[official MCP Registry](https://registry.modelcontextprotocol.io/v0/servers?search=com.microsoft/copilot-studio).

Your client launches this package with `npx`. The server connects to Copilot
Studio's hosted service after you sign in and select an environment, so access
stays tied to your identity, environment permissions, and organizational
policies.

## Notice

If your organization requires [Federal Risk and Authorization Management Program
(FedRAMP) High](https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-certification#federal-risk-and-authorization-management-program-fedramp)
compliance, the GitHub Copilot harness agent turns off at runtime to prevent
data egress from the FedRAMP High compliance boundary.

## Prerequisites

- Node.js 22.18 or later (Node.js 24 LTS recommended)
- A working MCP-compatible client: GitHub Copilot CLI, Visual Studio Code, or
  another MCP-compatible host
- A Microsoft work account with access to a Copilot Studio environment

## Install

Configure your client to launch the package with:

```powershell
npx -y @microsoft/copilot-studio-mcp@latest
```

The client starts the server process and communicates with it over standard
input/output (stdio). The package handles the connection to the hosted
Copilot Studio service; you don't enter a remote MCP URL or clone this source
repository. You can also install the server directly from the GitHub MCP
Registry or a supported client's MCP gallery (for example, VS Code's
`@mcp`/"Browse MCP Servers" gallery) and follow the listing's installation
option for your client.

## Available tools

After you sign in and select an environment, the server makes the connected
service's tools available. The service catalog includes the following tools.
Connection and sign-in utilities are separate.

| Tool | Description |
| --- | --- |
| `discover_resources` | Discover connector operations and schemas, existing connections, dependent parameter values, and attachable resources. |
| `get_consumption` | Read historical agent or workflow credit consumption, or current environment credit capacity. |
| `manage_agents` | Manage agent inventory, complete draft authoring, lifecycle, published-agent sharing, saved-draft previews, and agent evaluation suites and runs. |
| `manage_workflows` | Manage workflow inventory, complete draft authoring, lifecycle, real tests, and run diagnostics. |
| `get_copilot_studio_skills` | Start here for Copilot Studio guidance. Read the matching core skill before authoring, then read `schema.json`. |

The management, discovery, and consumption tools expose individual operations
through `action` and `parameters`. The current tool schemas identify the
advertised actions and their inputs. To read the focused contract and
side-effect information for an action before you construct unfamiliar
arguments, use `discover_resources` with `action=describe_actions`.

## Troubleshooting

If setup fails, stop and report the error without sharing credentials or
configuration JSON. DNS, refused/reset connections, and network timeouts have
distinct safe cause codes. Check endpoint availability and network/proxy
settings before an explicit retry; another call does not repair missing
environment routing.

See [SUPPORT.md](./SUPPORT.md) for how to get help with this project.

## Security

See [SECURITY.md](./SECURITY.md) for how to report security issues.

## License

Licensed under the [MIT License](./LICENSE).
