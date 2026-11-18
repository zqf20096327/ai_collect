# WebAgent — Browser Extension for Web AI + Local MCP

**WebAgent connects compatible web AI chat pages to local MCP tools through [Nexus](https://github.com/ysunyang4/Nexus).** It adds an on-page control panel and forwards supported tool-call blocks to a locally running Nexus service. Tool results can then be inserted back into the chat.

**Current extension version: 1.3.3** · [简体中文](README.zh-CN.md) · [Installation guide](USAGE.md) · [Changelog](CHANGELOG.md)

> WebAgent is a browser extension, **not a standalone MCP server**. Install and run Nexus first. WebAgent uses your existing web AI session; a separate model API key is not required. The AI website may still require its normal account or subscription.

## Supported web AI interfaces

WebAgent currently includes adapters for ChatGPT, Gemini, DeepSeek, Google AI Studio, Kimi, Qwen, Doubao, Duck.ai, Dola, Z.ai and several Zhipu chat interfaces. Compatibility is dependent on those websites' changing interfaces and may require updates.

## What it does

- **Local tool bridge:** forwards model-proposed MCP calls to a locally configured Nexus endpoint.
- **User-controlled execution:** provides settings for execution and tool-result feedback. Check the active settings before use.
- **Floating panel:** manage workspace, connection options and common tool actions from the chat page.
- **Result feedback:** puts tool results into the AI chat flow, subject to the website's normal send behavior.
- **Local permissions:** the underlying Nexus project configuration governs allowed file and command operations.
- **Error handling:** includes detection and safety pauses for repeated or failed tool calls.

## Quick start

1. Download and run [Nexus](https://github.com/ysunyang4/Nexus), authorize a local project, and note its actual project ID and permitted paths.
2. Download this repository. In Chrome, Edge, or another compatible Chromium browser, open `chrome://extensions/` (Edge: `edge://extensions/`).
3. Enable **Developer mode**, choose **Load unpacked**, and select the folder that contains `manifest.json`.
4. Open a supported web AI chat page and look for the floating WebAgent control panel.
5. Open WebAgent settings, check the local Nexus service address (typically `http://127.0.0.1:18080`), configure your workspace, and verify the connection.
6. Review the tool-execution options, then insert the collaboration prompt into your chat manually. Start with a read-only project-information request.

See [USAGE.md](USAGE.md) for details. After replacing extension files, reload the extension and refresh each open AI chat tab. Save unfinished drafts first.

## How the components fit together

```text
ChatGPT / Gemini / DeepSeek / other web AI chat
                  |
                  | WebAgent browser extension
                  v
        Local Nexus MCP service
                  |
                  v
   Authorized workspace, Git, terminal and other tools
```

## Security and privacy

- Tool calls can modify local data. Confirm the authorized workspace and the active permissions in Nexus before executing commands.
- Tool results inserted into a third-party AI webpage **can be read by that website**. Do not send secrets, tokens, passwords, or private files through model feedback.
- Do not treat project-level permissions as an operating-system security boundary. Review high-impact commands, and keep backups.
- WebAgent's local connection configuration does not mean AI messages remain private or offline.
- This repository's documentation is not a security guarantee or a substitute for testing your own configuration.

## License and contributions

WebAgent is released under [GPL-3.0-only](LICENSE). Personal and commercial use are permitted under the license terms. Contributions, issue reports, compatibility fixes, and clear reproduction steps are welcome.

Nexus is a separate project licensed under [AGPL-3.0-only](https://github.com/ysunyang4/Nexus/blob/main/LICENSE).

Community: [LINUX DO](https://linux.do). For the original Chinese documentation, see [README.zh-CN.md](README.zh-CN.md).
