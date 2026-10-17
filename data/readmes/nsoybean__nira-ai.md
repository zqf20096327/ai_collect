<p align="center">
  <img src="public/apple-touch-icon.png" alt="Nira AI Logo" width="120" height="120" />
</p>

<h1 align="center">Nira AI</h1>

<p align="center">
  An agentic AI assistant with composable tools for complex, multi-step tasks.
</p>

## Overview

Nira AI is a conversational AI workspace that combines multiple leading language models with powerful, composable tools. Built with Next.js and the Vercel AI SDK, it enables agents to research, synthesize, and create artifacts like presentations, documents, and more.

## Features

### Core

- **Multi-Model Support** — Claude, GPT, and Gemini models with seamless switching
- **Persistent Conversations** — Full history saved with database-backed storage
- **Real-Time Streaming** — Responses and artifacts stream as they're generated

### Agentic Tools

- **Web Search & Extract** — Research topics using Tavily, Anthropic, or OpenAI search
- **Slides Outline** — Generate structured presentation outlines
- **Task Management** — Track multi-step workflows with todo lists
- **Markdown Documents** — Create and edit document artifacts

### Artifacts

- **Streaming Artifacts** — Watch content generate in real-time in the side panel
- **Editable Outputs** — Modify generated slides, documents, and more
- **Database Persistence** — All artifacts saved and retrievable

## Tech Stack

- **Framework**: Next.js 16 with React 19
- **Database**: PostgreSQL with Prisma ORM
- **AI SDKs**: Vercel AI SDK with Anthropic, OpenAI, and Google providers
- **Tools**: Tavily (search/extract), DALL-E (image generation)
- **UI**: Radix UI primitives with Tailwind CSS
- **State**: React Context for global state management

## Getting Started

### Prerequisites

- Node.js 20+
- PostgreSQL database
- API keys for AI providers (Anthropic, OpenAI, Google)

### Installation

```bash
npm install
```

### Environment Variables

Create a `.env` file:

```env
DATABASE_URL="postgresql://..."
ANTHROPIC_API_KEY="..."
OPENAI_API_KEY="..."
GOOGLE_GENERATIVE_AI_API_KEY="..."
TAVILY_API_KEY="..."
TELEGRAM_BOT_TOKEN="..."
TELEGRAM_WEBHOOK_SECRET="..."
NEXT_PUBLIC_TELEGRAM_BOT_USERNAME="your_bot_username"
AUTOMATIONS_CRON_SECRET="your-long-random-secret"
```

### Database Setup

```bash
npx prisma generate
npx prisma migrate deploy
```

### Telegram Connector Setup (MVP)

1. Create a Telegram bot in BotFather and save the bot token.
2. Set webhook to your app:

```bash
curl -X POST "https://api.telegram.org/bot<TELEGRAM_BOT_TOKEN>/setWebhook" \
  -d "url=https://<your-domain>/api/integrations/telegram/webhook" \
  -d "secret_token=<TELEGRAM_WEBHOOK_SECRET>"
```

3. Open the app sidebar, click `Connectors`, then connect Telegram:

- Generate a connect code.
- Add bot to your group.
- Send `/connect <CODE>` in that group.

### Automation Scheduler (MVP)

- Create automations at `/automations`.
- Each automation runs daily at the selected **hour** and timezone (minutes fixed to `00`).
- Current destination support: Telegram group.
- Configure your external scheduler to call dispatch **hourly**.

Trigger scheduled runs by calling:

```bash
curl "http://localhost:3000/api/automations/dispatch" \
  -H "x-automation-secret: <AUTOMATIONS_CRON_SECRET>"
```

In production, point your cron service to the same endpoint.

### Development

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000)

### Desktop Development (Electron Bootstrap)

Run the Next.js app inside an Electron shell:

```bash
npm run dev:desktop
```

This keeps the existing Next.js server architecture unchanged and loads `http://localhost:3000` in Electron. The Electron bootstrap lives in:

- `electron/main.cjs`
- `electron/preload.cjs`

### Desktop Release (DMG)

1. Set your deployed Next.js URL in `package.json`:

```json
"desktop": {
  "prodUrl": "https://your-deployed-app-domain.com"
}
```

2. Build a local DMG:

```bash
npm run electron:dist
```

Artifacts are written to `release/`.

3. Publish from GitHub Actions:

- Push a tag like `v1.0.0`
- Workflow: `.github/workflows/desktop-release.yml`
- It builds `arm64` and `x64` DMGs and attaches them to the GitHub Release

Note: current CI build is unsigned (`CSC_IDENTITY_AUTO_DISCOVERY=false`). For trusted installation without Gatekeeper warnings, add Apple code-signing and notarization secrets in CI.

## Project Structure

```
src/
├── app/              # Next.js app router
│   └── api/chat/     # Chat API with tool execution
├── components/       # React components
│   └── ai-elements/  # Artifact and tool UI components
├── contexts/         # React context providers
├── hooks/            # Custom React hooks
└── lib/
    ├── tools/        # Composable agent tools
    ├── artifacts/    # Artifact stream handlers
    └── prompt/       # System prompts and tool instructions
```

## Architecture

```
User Request
    │
    ▼
┌─────────────────────────────────────────────┐
│  Chat API (streamText)                      │
│  - Tool registration                        │
│  - Model routing (Claude/GPT/Gemini)        │
└─────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────┐
│  Composable Tools                           │
│  - webSearch, webExtract                    │
│  - createSlidesOutline                      │
│  - todoWrite                                │
│  - (planned: imageSearch, imageGenerate)   │
└─────────────────────────────────────────────┘
    │
    ▼
┌─────────────────────────────────────────────┐
│  Streaming Artifacts                        │
│  - Real-time UI updates                     │
│  - Database persistence                     │
│  - Editable side panel                      │
└─────────────────────────────────────────────┘
```

## License

Private
