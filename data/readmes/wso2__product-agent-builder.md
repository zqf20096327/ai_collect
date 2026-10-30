<img src="https://wso2.cachefly.net/wso2/sites/all/image_resources/wso2-branding-logos/wso2-logo-orange.png" alt="WSO2 logo" width=30% height=30% />

# WSO2 Agent Builder

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Join the community on Discord](https://img.shields.io/badge/Join%20us%20on%20Discord-wso2-orange)](https://discord.com/invite/wso2)
[![X](https://img.shields.io/twitter/follow/wso2.svg?style=social&label=Follow%20Us)](https://twitter.com/intent/follow?screen_name=wso2)

WSO2 Agent Builder is an open source, low-code IDE for building AI agents. Design an agent visually by connecting triggers, a model, memory and tools, or write it in Ballerina code. The diagram and the code stay in sync in both directions. Run, trace, evaluate and deploy your agents from the same place, with a Copilot that helps you build them.

![WSO2 Agent Builder](docs/images/agent-builder.png)

## Key Features

- **Visual agent designer** – Connect triggers such as chat, WhatsApp and Slack to an agent, then give it a model, memory, a system prompt and tools.
- **Agent overview diagram** – See how the triggers, agents and connections in your project fit together.
- **Multi-agent systems** – Use agents as tools of other agents to delegate work to specialist agents.
- **Durable agents** – Build agents that pause and resume, wait for external events, involve people when necessary and recover from failures without losing progress.
- **Knowledge bases as tools** – Add vector knowledge bases with your own embedding provider and vector store, or use a knowledge base hosted on the WSO2 Integration Platform.
- **MCP servers** – Create MCP servers from scratch or generate them from an OpenAPI specification.
- **Offline evaluations** – Create and run evaluations for each agent. Copilot can generate evaluation datasets and help fix failing evaluations.
- **Agent Manager integration** – Connect to a self-hosted Agent Manager to use its LLM service providers and MCP proxies, send agent traces to it, and deploy agents and publish MCP servers to it from the IDE.
- **Copilot for agent building** – Describe what you need, and Copilot builds, updates and explains your agents.

## Download

Download the installer for your platform from the [releases page](https://github.com/wso2/product-agent-builder/releases). Installers are available for macOS (Apple silicon and Intel), Windows and Linux (`.deb`, `.rpm` and `.tar.gz`).

## Get Started

See the following topics to get started with the product:

- [Get Started](https://wso2.com/integration-platform/docs/agent-builder/get-started)
- [Build an AI Agent](https://wso2.com/integration-platform/docs/agent-builder/get-started/quickstarts/build-ai-agent)
- [Build a Durable Agent](https://wso2.com/integration-platform/docs/agent-builder/get-started/quickstarts/build-durable-agent)
- [Guides](https://wso2.com/integration-platform/docs/agent-builder/guides)

## Source Code

This repository holds the releases and the issue tracker. The source code is in these repositories:

- [wso2/product-integrator](https://github.com/wso2/product-integrator) – The desktop application and its installers.
- [ballerina-platform/ballerina-vscode](https://github.com/ballerina-platform/ballerina-vscode) – The Ballerina extension, which includes the visual editor, Copilot and the Ballerina language server.

## Report Product Issues

### Open an Issue

Submit bug reports and feature requests in the [issue tracker](https://github.com/wso2/product-agent-builder/issues/new) of this repository.

### Report Security Issues

Do **not** report security issues in GitHub issues. Follow the [WSO2 Security Vulnerability Reporting Guidelines](https://security.docs.wso2.com/en/latest/security-reporting/vulnerability-reporting-guidelines/).

## Join the Community

- Read our [documentation](https://wso2.com/integration-platform/docs/agent-builder/).
- Join the conversation on [Discord](https://discord.gg/wso2).
- Read articles in the [WSO2 library](https://wso2.com/library/).

## License

WSO2 Agent Builder is licensed under the [Apache License 2.0](LICENSE).

--------------------------------------------------------------------------------
(c) Copyright 2026 WSO2 LLC.
