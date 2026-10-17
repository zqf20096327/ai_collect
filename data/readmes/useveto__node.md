# @useveto/node

Runtime authorization for AI agents. The missing layer between identity and action.

[![npm](https://img.shields.io/npm/v/@useveto/node)](https://www.npmjs.com/package/@useveto/node)
[![License: MIT](https://img.shields.io/badge/License-MIT-emerald.svg)](https://opensource.org/licenses/MIT)

## What is Veto?

Veto intercepts every tool call your AI agent makes, evaluates it against your policies, and decides: **allow**, **deny**, or **escalate**. Sub-10ms. Default deny.

- **Default deny** — no matching policy = blocked
- **MCP native** — drop-in middleware for Model Context Protocol servers
- **Full audit trail** — every decision logged
- **Edge-first** — powered by Cloudflare Workers

## Install

```bash
npm install @useveto/node
```

## Quick Start

```typescript
import { VetoClient } from "@useveto/node";

const veto = new VetoClient({ apiKey: process.env.VETO_API_KEY! });

// Check if an agent can perform an action
const result = await veto.authorize("support-bot", "send_email", {
  to: "user@example.com",
  subject: "Refund confirmation",
});

if (!result.allowed) {
  console.log(`Blocked: ${result.reason}`);
}
```

## MCP Integration

### Option 1: Guard wrapper (recommended)

Wraps your tool handler — denied actions never execute.

```typescript
import { VetoClient, createVetoGuard } from "@useveto/node";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { z } from "zod";

const veto = new VetoClient({ apiKey: process.env.VETO_API_KEY! });
const protect = createVetoGuard(veto, { agentId: "support-bot" });

const server = new McpServer({ name: "my-server", version: "1.0.0" });

server.tool(
  "send-email",
  { to: z.string(), subject: z.string(), body: z.string() },
  protect("send-email", async (params) => {
    await sendEmail(params);
    return { content: [{ type: "text", text: "Email sent!" }] };
  }),
);
```

When denied, returns `{ content: [{ type: 'text', text: 'Authorization denied: ...' }], isError: true }`.

### Option 2: Manual middleware

Call at the start of your handler — throws `VetoError` if denied.

```typescript
import { VetoClient, vetoMiddleware } from "@useveto/node";

const veto = new VetoClient({ apiKey: process.env.VETO_API_KEY! });
const guard = vetoMiddleware(veto, { agentId: "support-bot" });

server.tool("send-email", schema, async (params) => {
  await guard("send-email", params); // throws VetoError if denied
  await sendEmail(params);
  return { content: [{ type: "text", text: "Sent!" }] };
});
```

## API Reference

### `VetoClient`

```typescript
const veto = new VetoClient({
  apiKey: "veto_...", // required
  endpoint: "https://api.veto.tools", // optional (default)
  timeout: 5000, // optional, ms (default: 5000)
});
```

#### Authorization

```typescript
veto.authorize(agentId, toolName, parameters?) → Promise<AuthorizationResult>
```

#### Agents

```typescript
veto.createAgent({ name, description? }) → Promise<Agent>
veto.listAgents() → Promise<Agent[]>
veto.getAgent(agentId) → Promise<Agent>
veto.deleteAgent(agentId) → Promise<void>
```

#### Policies

```typescript
veto.createPolicy({ agentId, name, rules, priority?, enabled? }) → Promise<Policy>
veto.listPolicies(agentId?) → Promise<Policy[]>
veto.getPolicy(policyId) → Promise<Policy>
veto.updatePolicy(policyId, { name?, rules?, priority?, enabled? }) → Promise<Policy>
veto.deletePolicy(policyId) → Promise<void>
```

#### Audit Logs

```typescript
veto.queryAuditLog({ agentId?, action?, toolName?, result?, from?, to?, limit?, offset? }) → Promise<AuditLogEntry[]>
```

### Error Handling

```typescript
import { VetoError, UnauthorizedError, RateLimitError } from "@useveto/node";

try {
  await veto.authorize("agent", "tool");
} catch (error) {
  if (error instanceof RateLimitError) {
    console.log(`Retry after ${error.retryAfterMs}ms`);
  } else if (error instanceof UnauthorizedError) {
    console.log("Invalid API key");
  } else if (error instanceof VetoError) {
    console.log(`${error.code}: ${error.message}`);
  }
}
```

### Fail-Closed by Default

If Veto is unreachable (network error, timeout), the SDK **denies by default**. You can override this:

```typescript
const protect = createVetoGuard(veto, {
  agentId: "my-agent",
  onError: "allow", // fail-open (not recommended for production)
});
```

## Links

- **Website:** [veto.tools](https://veto.tools)
- **Dashboard:** [app.veto.tools](https://app.veto.tools)
- **API Docs:** [docs.veto.tools](https://docs.veto.tools)
- **GitHub:** [github.com/useveto/node](https://github.com/useveto/node)

## License

MIT
