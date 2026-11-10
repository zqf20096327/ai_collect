# Esri developer agent skills

Esri Developer Agent Skills provides an installable plugin, reusable skills, and an Esri-hosted MCP server for official ArcGIS developer documentation. The skills guide agents through ArcGIS application requirements, authentication, and development with ArcGIS SDKs, APIs, and supported open-source libraries. The plugin bundles the skills and MCP server for compatible clients.

This repo complies with the [Agent Plugins 1.0 specification](https://agent-plugins.org/).

## What's Included

This repository includes the following:

- **Esri Developer Agent Skills marketplace** (`esri-developer-agent-skills`): The repository-hosted marketplace where compatible clients discover the plugin. The plugin bundles the skills and MCP server; the skills themselves provide guidance for requirements, authentication, and ArcGIS development.

- **ArcGIS SDKs and APIs plugin** (`arcgis-sdks-and-apis-plugin`): Bundles all 16 developer skills and the Esri MCP server for developer documentation for installation in compatible clients.

- **Esri MCP server for developer documentation** (`esri-mcp-server-for-developer-documentation`): Esri-hosted MCP server for agents to search for official ArcGIS developer documentation. This MCP server supports the agent skills.

**Note:** For additional information about these components and how to use them in your agentic workflows, go to the [ArcGIS agentic developer toolkit guide](https://developers.arcgis.com/ai/arcgis-agentic-developer-toolkit/).

## Installation

1. Follow your client's installation documentation below to add this repository as a plugin marketplace.
2. Install `arcgis-sdks-and-apis-plugin` from the `esri-developer-agent-skills` repo. Adding the marketplace alone does not install or enable the plugin. Additional steps are typically required to install the skills and MCP server.

### Install individual skills

Choose this option to install selected skills without the full plugin. To get the complete skills bundle and MCP server together, install the plugin instead.

Use your client's skill installation workflow, or copy the chosen skill's entire folder from `skills/` into a supported skill directory. Keep any bundled `references/`, scripts, and assets with the skill.

```
npx skills add Esri/esri-developer-agent-skills
```

### Manual MCP server installation

Installing an individual skill does not install the plugin or configure **Esri MCP server for developer documentation**. Add the remote server at `https://developers-mcp.arcgis.com/mcp` using your client's MCP settings and its supported Streamable HTTP configuration. The plugin's [mcp.json](./mcp.json) provides the bundled configuration, but a link to that file in a skill does not register the server automatically.

Example:
```
{
  "$schema": "https://agent-plugins.org/schemas/1.0.0/mcp.schema.json",
  "mcpServers": {
    "esri-mcp-server-for-developer-documentation": {
      "url": "https://developers-mcp.arcgis.com/mcp",
      "type": "streamable-http"
    }
  }
}
```

### Additional client installation documentation

Installation steps and support for skills, MCP servers, and agent extensions vary by client. These links describe each client's installation or extension workflow.

- [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-finding-installing)
- [VS Code](https://code.visualstudio.com/docs/agent-customization/agent-plugins#_install-a-plugin-from-source)
- [Claude Code](https://code.claude.com/docs/en/discover-plugins#add-from-github)
- [Cursor](https://cursor.com/docs/plugins#installing-plugins)
- [Xcode](https://developer.apple.com/documentation/xcode/extending-and-customizing-agents#Install-agentic-coding-plug-ins)
- [Kiro](https://kiro.dev/docs/powers/installation/#from-public-github-url)

After installation, start a new agent session and the CLI to verify and list the plugin, skills, and Esri MCP server for developer documentation are available.

## Skills catalog

- [Build with ArcGIS and CesiumJS](skills/build-with-arcgis-and-cesiumjs/SKILL.md)
- [Build with ArcGIS and OpenLayers](skills/build-with-arcgis-and-openlayers/SKILL.md)
- [Build with ArcGIS API for Python](skills/build-with-arcgis-api-for-python/SKILL.md)
- [Build with ArcGIS and MapLibre](skills/build-with-arcgis-maplibre/SKILL.md)
- [Build with ArcGIS Maps SDK for .NET](skills/build-with-arcgis-maps-sdk-for-dotnet/SKILL.md)
- [Build with ArcGIS Maps SDK for Flutter](skills/build-with-arcgis-maps-sdk-for-flutter/SKILL.md)
- [Build with ArcGIS Maps SDK for JavaScript](skills/build-with-arcgis-maps-sdk-for-javascript/SKILL.md)
- [Build with ArcGIS Maps SDK for Kotlin](skills/build-with-arcgis-maps-sdk-for-kotlin/SKILL.md)
- [Build with ArcGIS Maps SDK for Qt](skills/build-with-arcgis-maps-sdk-for-qt/SKILL.md)
- [Build with ArcGIS Maps SDK for Swift](skills/build-with-arcgis-maps-sdk-for-swift/SKILL.md)
- [Build with ArcGIS Maps SDK for Unity](skills/build-with-arcgis-maps-sdk-for-unity/SKILL.md)
- [Build with ArcGIS Maps SDK for Unreal Engine](skills/build-with-arcgis-maps-sdk-for-unreal-engine/SKILL.md)
- [Build with ArcGIS REST JS](skills/build-with-arcgis-rest-js/SKILL.md)
- [Build with Calcite Design System](skills/build-with-calcite-design-system/SKILL.md)
- [Follow ArcGIS authentication patterns](skills/follow-arcgis-authentication-patterns/SKILL.md)
- [Gather ArcGIS application requirements](skills/gather-arcgis-application-requirements/SKILL.md)

## Issues

Find a bug or want to request a new feature? Please let us know by [submitting an issue](https://github.com/Esri/esri-developer-agent-skills/issues/new).

## Contributing

Esri welcomes contributions from anyone and everyone. Before you [file an issue](https://github.com/Esri/esri-developer-agent-skills/issues/new) or issue a [pull request](https://github.com/Esri/esri-developer-agent-skills/pulls), please read our **[Contributing Guidelines](CONTRIBUTING.md)** to learn about our process and how to request new features, propose bug fixes or improvements.

Please also note that this project is governed by our **[Code of Conduct](CODE_OF_CONDUCT.md)**. By participating, you are expected to uphold this code.

## License

Copyright 2026 Esri

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

A copy of the license is available in the repository's [LICENSE](./LICENSE) file.
