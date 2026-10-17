# PocketAgents

The complete agent runtime in a single executable.

PocketAgents gives you a full AI backend you can run anywhere with one file: model routing, encrypted provider keys, tool execution, RAG knowledge, monitoring, and auth.

No Node runtime setup, no external database, no multi-service orchestration. Download one binary and run.

## Why Use PocketAgents

- One executable gives you the entire platform
- Built-in web console for agents, models, tools, and keys
- Durable runs with event timelines for debugging and ops
- Simple, production-ready auth with admin and client keys
- Local-first architecture with no external database required
- Works with modern AI app clients, including `@ai-sdk/react`

## Get Started

### 1. Download the binary

Get the latest release from GitHub:

- [Latest release](https://github.com/treyorr/pocket-agents/releases/latest)

Linux x64:

```bash
curl -fL -o pocket-agents.tar.gz \
  https://github.com/treyorr/pocket-agents/releases/latest/download/pocket-agents-linux-x64.tar.gz

tar -xzf pocket-agents.tar.gz
```

macOS (Apple Silicon, arm64):

```bash
curl -fL -o pocket-agents.tar.gz \
  https://github.com/treyorr/pocket-agents/releases/latest/download/pocket-agents-darwin-arm64.tar.gz

tar -xzf pocket-agents.tar.gz
# If you see "App is damaged" or "Apple could not verify...", run:
xattr -cr pocket-agents
```

macOS (Intel, x64):

```bash
curl -fL -o pocket-agents.tar.gz \
  https://github.com/treyorr/pocket-agents/releases/latest/download/pocket-agents-darwin-x64.tar.gz

tar -xzf pocket-agents.tar.gz
# If you see "App is damaged" or "Apple could not verify...", run:
xattr -cr pocket-agents
```

Windows x64 (PowerShell):

```powershell
curl -o pocket-agents.zip https://github.com/treyorr/pocket-agents/releases/latest/download/pocket-agents-windows-x64.zip

Expand-Archive pocket-agents.zip -DestinationPath .
```

If your platform/architecture differs, choose the matching asset from the release page.

### 2. Start PocketAgents

```bash
./pocket-agents serve --data-dir ./pa_data --port 4631
```

Open [http://localhost:4631](http://localhost:4631) and complete setup.

### 3. Connect your app

```ts
import { useChat } from "@ai-sdk/react";
import { DefaultChatTransport } from "ai";

const { messages, sendMessage, status } = useChat({
  transport: new DefaultChatTransport({
    api: "http://localhost:4631/api/agents/MY_AGENT/chat",
    headers: { Authorization: "Bearer pk_client_xxx" },
  }),
});

sendMessage({ text: "Hello" });
```

## What You Can Do

- Create and configure agents
- Bring your own API keys from OpenAI, Anthropic, etc.
- Attach HTTP and internal tools
- Add knowledge collections for RAG — upload **PDF, DOCX, TXT, MD, CSV, JSON, or HTML** and chunks are embedded automatically
- Manage provider keys and model routing
- Track runs with event timelines and status

## API Endpoints

Streaming:

- `POST /api/agents/:id/chat`
- `POST /api/agents/:id/runs`

Management:

- `/api/agents`
- `/api/models`
- `/api/provider-keys`
- `/api/tools`
- `/api/collections`
- `/api/runs`
- `/api/admin/api-keys`
- `/api/files`
- `/api/stats`
- `/api/events`

## CLI Commands

- `serve`: Start the server
- `keys show`: Show active admin key prefixes (recovery)



Notes:

- Agent-scoped client keys can access agent chat/run endpoints and run details for their allowed agents.
- Admin auth is required for admin resources (models, provider keys, tools, collections, platform stats, API key management).

## Future Enhancements

- Run replay endpoint and replay UI
- Richer run analytics and drill-down views
- Extended tool observability and approval workflows
- Self update command
- Rate limiting

## For Developers

Build locally:

```bash
bun install
bun run build
./pocket-agents serve --data-dir ./pa_data --port 4631
```

Development commands:

- `bun run dev`
- `bun run dev-keys`
- `bun run lint`
- `bun run typecheck`
- `bun run test`
- `bun run build`
- `bun run start`

Developer and project docs:

- Product spec: [`PRD.md`](./PRD.md)
- Testing guide: [`TESTING_GUIDE.md`](./TESTING_GUIDE.md)
- Open-source readiness: [`OPEN_SOURCE_READINESS.md`](./OPEN_SOURCE_READINESS.md)
- Contributing: [`CONTRIBUTING.md`](./CONTRIBUTING.md)
- Release process: [`RELEASE.md`](./RELEASE.md)

Community and governance:

- Code of Conduct: [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md)
- Security policy: [`SECURITY.md`](./SECURITY.md)
- Governance: [`GOVERNANCE.md`](./GOVERNANCE.md)

## Security

If you discover a vulnerability, do not open a public issue. Follow [`SECURITY.md`](./SECURITY.md).

## License

MIT. See [`LICENSE`](./LICENSE).
