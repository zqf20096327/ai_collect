# Atlas Cloud nodes for n8n

<p>
  <a href="https://www.npmjs.com/package/n8n-nodes-atlascloud"><img src="https://img.shields.io/npm/v/n8n-nodes-atlascloud.svg?style=flat&colorA=18181B&colorB=28CF8D" alt="npm version" /></a>
  <a href="https://github.com/AtlasCloudAI/n8n-nodes-atlascloud/blob/main/LICENSE"><img src="https://img.shields.io/github/license/AtlasCloudAI/n8n-nodes-atlascloud?style=flat&colorA=18181B&colorB=28CF8D" alt="license" /></a>
  <a href="https://github.com/AtlasCloudAI/n8n-nodes-atlascloud/stargazers"><img src="https://img.shields.io/github/stars/AtlasCloudAI/n8n-nodes-atlascloud?style=flat&colorA=18181B&colorB=28CF8D" alt="stars" /></a>
  <a href="https://github.com/AtlasCloudAI/n8n-nodes-atlascloud/pulls"><img src="https://img.shields.io/badge/PRs-welcome-28CF8D.svg?style=flat&colorA=18181B" alt="PRs welcome" /></a>
</p>

> Use Atlas Cloud's 300+ AI models inside n8n workflows. Supports Sora 2 · Veo 3.1 · Kling 3 · Seedance 2 · Nano Banana Pro · GPT Image 2 · Flux 2 · Claude · GPT and more.

> **[→ Get your free Atlas Cloud API key](https://www.atlascloud.ai/console/api-keys?utm_source=github&utm_campaign=n8n-nodes-atlascloud)** — one key, 300+ models, OpenAI-compatible.

> 🎬 **New — Seedance 2.0:** native audio-video, up to 15s, 1080p. Explore the [Seedance 2.0 family](https://www.atlascloud.ai/collections/seedance2?utm_source=github&utm_campaign=n8n-nodes-atlascloud) on Atlas Cloud.

## Supported Models

- 🎬 **Video** — Seedance 2.0 · Kling 3 · Sora 2 · Veo 3.1 · HappyHorse 1 · Grok Imagine 1.5 · Wan 2.7
- 🎨 **Image** — Nano Banana 2/Pro · GPT Image 2 · Flux 2 · Seedream 5
- 💬 **LLM** — Claude · GPT · DeepSeek · MiniMax · Kimi · GLM · Qwen
- 🔊 **Audio** — Grok TTS

…and [300+ models](https://www.atlascloud.ai/models?utm_source=github&utm_campaign=n8n-nodes-atlascloud) in total, all via one API. The nodes below adapt automatically to each model's parameters.

<!-- TODO(hero): add a screenshot of an Atlas Cloud n8n workflow canvas here. -->

## Contents

- [Supported Models](#supported-models)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Example Workflows](#example-workflows)
- [More Atlas Cloud Tools](#more-atlas-cloud-tools)
- [License](#license)

## Features

### 💬 Atlas Cloud Chat

A powerful node for interacting with Large Language Models via an OpenAI-compatible interface.

- **Wide Model Support**: Access popular models including Claude, GPT, Gemini, and more.
- **Customizable Prompts**: Support for System Prompts and User Prompts.
- **Advanced Configuration**: Fine-tune generation with parameters like Temperature and Max Tokens.
- **Extra Messages**: Support for passing full conversation history or JSON-structured messages.

### 🚀 Atlas Cloud Task Submit

A universal node for submitting AI generation tasks with intelligent parameter adaptation.

- **Dynamic Model Discovery**: Automatically loads available categories (Text-to-Image, Text-to-Video, etc.) and models.
- **Smart Parameter Rendering**: Dynamically renders required and optional parameters based on the selected model's schema.
- **Flexible Execution Modes**:
  - **Submit Only**: Returns the prediction ID immediately for asynchronous processing.
  - **Wait for Completion**: Automatically polls the status and returns the final result once generated.

### 🔍 Atlas Cloud Task Status

A dedicated node for managing asynchronous tasks.

- **Status Checking**: Retrieve the current status of any prediction ID.
- **Smart Polling**: "Wait for Completion" mode with configurable polling intervals, timeouts, and retry logic.

## Installation

1. Open your n8n instance and go to **Settings** > **Community Nodes**.
2. Click **Install**.
3. Enter the npm package name: `n8n-nodes-atlascloud`.
4. Wait for the installation to complete and refresh the page.

## Configuration

### Credentials

To use these nodes, you need an API Key from Atlas Cloud.

1. [Login to Atlas Cloud](https://console.atlascloud.ai?utm_source=github&utm_campaign=n8n-nodes-atlascloud) or [Create an account](https://www.atlascloud.ai/login?utm_source=github&utm_campaign=n8n-nodes-atlascloud).
2. Navigate to the **API Keys** page in your settings.
3. Create a new API Key.
4. In n8n, add a new Credential type **Atlas Cloud API** and paste your API Key.

See [`.env.example`](.env.example) for the `ATLASCLOUD_API_KEY` environment variable format.

### Usage Guide

#### Image & Video Generation

1. Add the **Atlas Cloud Task Submit** node.
2. Select a **Category** (e.g., `Text-to-Image`).
3. Select a specific **Model**.
4. The node will automatically display the specific parameters for that model.
5. Fill in the **Prompt** and other **Required Parameters**.
6. Choose your **Execution Mode**:
   - Select **Wait for Completion** if you want the file output directly in this step.

#### Text Generation (LLM)

1. Add the **Atlas Cloud Chat** node.
2. Select your credential.
3. Choose a **Model** from the dropdown list.
4. Enter your **User Prompt**.
5. (Optional) Set a System Prompt to define the assistant's behavior.

## Example Workflows

📥 **Importable:** ready-to-run `.json` workflows live in [`workflows/`](workflows/) — import, select your credential, and run. The diagrams below show the shape of each.

### 1. Simple Chatbot

```
Webhook → Atlas Cloud Chat → Respond to Webhook
```

### 2. Generate Image and Download

```
Start → Atlas Cloud Task Submit (Wait for Completion) → HTTP Request (Download Media)
```

### 3. Asynchronous Video Generation

```
Start → Atlas Cloud Task Submit (Submit Only) → Wait Node → Atlas Cloud Task Status (Wait for Completion)
```

## More Atlas Cloud Tools

- 🧰 Want to use it from the terminal? → [atlascloud-cli](https://github.com/AtlasCloudAI/cli)
- 🤖 Want to use it in Claude Code / Cursor? → [Atlas Cloud MCP Server](https://github.com/AtlasCloudAI/mcp-server)
- 🎬 Want it as a Claude Code / Codex / Gemini CLI Skill? → [atlas-cloud-skills](https://github.com/AtlasCloudAI/atlas-cloud-skills)
- 🎨 ComfyUI nodes → [atlascloud_comfyui](https://github.com/AtlasCloudAI/atlascloud_comfyui)
- 🔁 n8n nodes → [n8n-nodes-atlascloud](https://github.com/AtlasCloudAI/n8n-nodes-atlascloud)
- 💬 Join our Discord → [discord.gg/MWmMr4q9es](https://discord.gg/MWmMr4q9es)
- 🌐 Website → [atlascloud.ai](https://www.atlascloud.ai?utm_source=github&utm_campaign=n8n-nodes-atlascloud)

**Docs:** [Model Library](https://www.atlascloud.ai/models?utm_source=github&utm_campaign=n8n-nodes-atlascloud) · [Console](https://console.atlascloud.ai?utm_source=github&utm_campaign=n8n-nodes-atlascloud)

## License

MIT

<!-- TODO(hero): add an n8n canvas screenshot showing Atlas Cloud nodes wired up in a workflow. -->
