# MentorAgent

> **New package IDs.** From 1.0.0 the packages, their namespaces and their assemblies are `Novior.MentorAgent.*`; up to 1.0.0-rc.15 they were `MentorAgent.*`. See [Migrating from the MentorAgent.* packages](#migrating-from-the-mentoragent-packages).

## Package Family

| Package | Install when |
|---------|-------------|
| **Novior.MentorAgent** ← you are here | Blazor Server app (the most common case) |
| [Novior.MentorAgent.Server](https://www.nuget.org/packages/Novior.MentorAgent.Server) | Web API, headless backend, or any client that is not Blazor Server (WASM, React, mobile) — adds the SignalR hub (`/mentor-hub`), the SSE endpoint (`/mentor/chat`) and the HTTP approve/cancel endpoints. Also the **MCP server** and the **A2A agent** (`AddMentorAgentMcp()` / `MapMentorAgentMcp()`, `AddMentorAgentA2A()` / `MapMentorAgentA2A()`): a Blazor Server app that publishes either one needs this package too, without the hub |
| [Novior.MentorAgent.Blazor](https://www.nuget.org/packages/Novior.MentorAgent.Blazor) | Blazor WASM / Blazor Auto **client** project |
| [Novior.MentorAgent.Abstractions](https://www.nuget.org/packages/Novior.MentorAgent.Abstractions) | **Never install directly** — transitive dependency included automatically |
| [Novior.MentorAgent.Declarative](https://www.nuget.org/packages/Novior.MentorAgent.Declarative) | **Optional** — define Level-2 specialist agents in YAML instead of C# |

**MentorAgent** is a .NET library that embeds a fully functional **AI assistant** directly into any Blazor application — with a floating chat widget, multi-agent orchestration, contextual memory, RAG, MCP integration, A2A federation, Agent Skills, and voice support — all configured via a single `AddMentorAgent()` call.

Built on top of **[Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/)** (`Microsoft.Agents.AI`), MentorAgent abstracts the complexity of multi-agent systems into a clean, attribute-driven programming model designed specifically for Blazor developers.

**See it run:** the [demo](https://github.com/Novior-dev/MentorAgent/tree/main/demo) is a small expense-claims app with MentorAgent inside. Clone the repository, set a model key in the user secrets and `dotnet run`.

---

## Table of Contents

- [What is MentorAgent?](#what-is-mentoragent)
- [What can it do?](#what-can-it-do)
- [Architecture overview](#architecture-overview)
- [Getting started](#getting-started)
  - [Installation](#installation)
  - [Minimal setup](#minimal-setup)
  - [Add the widget to your layout](#add-the-widget-to-your-layout)
- [AI providers](#ai-providers)
- [The three-level agent model](#the-three-level-agent-model)
  - [Level 1 — Actions on a service](#level-1--actions-on-a-service)
  - [Level 2 — Specialized agent with Handoff](#level-2--specialized-agent-with-handoff)
  - [Level 3 — Collaborative team (Group Chat)](#level-3--collaborative-team-group-chat)
- [Page navigation](#page-navigation)
- [Page context and UI actions](#page-context-and-ui-actions)
- [Agent Skills](#agent-skills)
- [Contextual memory](#contextual-memory)
- [RAG — Retrieval-Augmented Generation](#rag--retrieval-augmented-generation)
- [MCP — Model Context Protocol](#mcp--model-context-protocol)
  - [MCP Client — consuming external MCP servers](#mcp-client--consuming-external-mcp-servers)
  - [MCP Server — exposing MentorAgent as an MCP server](#mcp-server--exposing-mentoragent-as-an-mcp-server)
- [A2A — Agent-to-Agent](#a2a--agent-to-agent)
  - [A2A Consumer — calling remote A2A agents](#a2a-consumer--calling-remote-a2a-agents)
  - [A2A Server — exposing MentorAgent as an A2A agent](#a2a-server--exposing-mentoragent-as-an-a2a-agent)
- [Persistent conversation history](#persistent-conversation-history)
- [Blazor Server vs Blazor WASM](#blazor-server-vs-blazor-wasm)
- [Built-in AI tools](#built-in-ai-tools)
- [Streaming responses](#streaming-responses)
- [Session serialize and restore](#session-serialize-and-restore)
- [Security](#security)
- [Token & cost optimization](#token--cost-optimization)
- [Middleware & extensibility](#middleware--extensibility)
- [Observability (OpenTelemetry)](#observability-opentelemetry)
- [Token & cost dashboard](#token--cost-dashboard)
- [Model routing](#model-routing)
- [Structured outputs](#structured-outputs)
- [Rich responses (tables & lists)](#rich-responses-tables--lists)
- [Generative UI — cards (Level 2)](#generative-ui--cards-level-2)
- [Declarative agents (YAML)](#declarative-agents-yaml)
- [Voice input and output](#voice-input-and-output)
- [Onboarding tour](#onboarding-tour)
- [Multimodal image input](#multimodal-image-input)
- [Hosted tools (web search, code interpreter, file search, images, remote MCP)](#hosted-tools-web-search-code-interpreter-file-search-images-remote-mcp)
- [Human-in-the-loop tool approval](#human-in-the-loop-tool-approval)
- [Evaluation & regression testing](#evaluation--regression-testing)
- [Widget customization](#widget-customization)
  - [Themes](#themes)
  - [CSS variables — full reference](#css-variables--full-reference)
  - [Fonts and Content-Security-Policy](#fonts-and-content-security-policy)
  - [The admin dashboard is themed separately](#the-admin-dashboard-is-themed-separately)
- [All configuration options](#all-configuration-options)
- [Building your own UI — IMentorStateService](#building-your-own-ui--imentorstateservice)
  - [Driving a turn — IMentorOrchestrator](#driving-a-turn--imentororchestrator)
  - [Complete event reference](#complete-event-reference)
  - [Replacing the confirmation dialog](#replacing-the-confirmation-dialog)
- [Extensibility](#extensibility)
- [Requirements](#requirements)
- [Migrating from the MentorAgent.* packages](#migrating-from-the-mentoragent-packages)
- [Related Packages](#related-packages)
- [License](#license)

---

## What is MentorAgent?

MentorAgent turns any Blazor application into an AI-assisted experience. It provides:

- A **floating chat widget** — one `<ChatWidget />` tag in your layout; it brings its own CSS and JS.
- A **Main Coordinator agent** that understands the application context and routes requests.
- An **attribute-driven discovery system** that scans your assemblies and turns plain C# methods and classes into AI tools and agents — zero boilerplate.
- Full integration with **Microsoft Agent Framework**, supporting Handoff Workflows, Group Chat teams, and any AI provider compatible with the `IChatClient` abstraction.
- **RAG** — inject relevant documents into every AI response, read through an `IMentorRagSource` you implement over your own store.
- **MCP** — consume external MCP servers as additional tools, and expose MentorAgent's own actions as an MCP server for other AI clients.
- **A2A** — connect to remote AI agents via the Agent-to-Agent protocol, and expose MentorAgent as a federatable A2A agent.

The developer defines *what the AI can do* using attributes. MentorAgent handles everything else: prompt building, agent wiring, session management, rate limiting, safety checks, memory, RAG retrieval, MCP connections, A2A federation, Agent Skills, and UI.

Before every LLM call, MentorAgent automatically enriches the system prompt with **real-time context**: the current URL, the active page name, the authenticated user and their roles, the data registered by the current page via `IMentorPageContext`, the user's contextual memory, the Agent Skills catalogue, and — when RAG is enabled — the most relevant documents retrieved from your vector store.

UI actions registered by the current page are injected as **individually named AI tools** (one tool per action, each with its own description and parameter schema), rather than a generic dispatcher. This gives the AI precise knowledge of exactly what it can do on the current page, reducing hallucinations and enabling direct invocation: `highlight_row(5)` instead of `invoke_ui_action("highlight_row", 5)`.

---

## What can it do?

| Feature | Description |
|---|---|
| 🤖 **Multi-agent orchestration** | Coordinator + specialized agents connected via Handoff Workflow |
| 👥 **Group Chat teams** | Multiple agents collaborate in a structured conversation before executing |
| 🛠️ **Tool discovery** | C# methods become AI tools via `[Description]` or `[MentorAction]` |
| 🎯 **UI Actions** | AI invokes page-level actions (highlight rows, open modals, pre-fill forms) as individually named tools with typed parameters and async support |
| 📖 **Agent Skills** | Domain knowledge + execution packages — knowledge loaded on demand via `load_skill` (progressive disclosure), methods registered as L1 tools |
| 🧠 **Contextual memory** | Remembers user preferences and actions across sessions |
| 🗺️ **Page navigation** | AI navigates to any page decorated with `[MentorPage]` |
| 💬 **Session management** | Conversation history managed by Agent Framework (`AgentSession`) |
| 💾 **Persistent history** | Pluggable `ChatHistoryProvider` (CosmosDB, Redis, custom) |
| 📚 **RAG** | Retrieval-Augmented Generation — inject relevant documents into every AI response, read through an `IMentorRagSource` you implement over your own store |
| 🔌 **MCP Client** | Consume external MCP servers as additional Level-1 tools for the coordinator |
| 🖥️ **MCP Server** | Expose your Level-1 actions (`[Description]` and `[MentorAction]` methods) as MCP tools — any MCP client can connect (Claude Desktop, VS Code, etc.). Gated actions (`RequiresConfirmation`, `RequiredRoles`, `RequiresApproval`) are withheld — an MCP caller cannot confirm anything — except a role-gated one published to a caller that `McpCallerPrincipal` identifies as holding the role |
| 🌐 **A2A Consumer** | Connect to remote A2A agents; the coordinator delegates to them through the same handoff workflow as local specialists, and every answer says which system it came from. A request that arrived over A2A is answered locally, never passed on to another peer |
| 📡 **A2A Server** | Expose MentorAgent as a federatable A2A agent — other orchestrators can discover and call it |
| 🎨 **Customizable widget** | Themes, colors, position, avatar, bot name |
| 🌍 **Multi-language** | Configurable language for AI responses and the widget UI |
| 🎤 **Voice input/output** | Browser-native Speech Recognition and Speech Synthesis — speaks while the answer streams, stops when the user takes the floor, optional hands-free loop |
| 🧭 **Onboarding tour** | First-run guide generated from the app's own pages and tools, with one-tap example questions |
| 🃏 **Generative UI cards** | A tool returns a card — fields, accent, buttons — and the widget renders it instead of the model describing it |
| 📄 **Declarative agents** | Specialist agents defined in YAML, reusing your existing tools with their role and approval gates |
| 🖼️ **Multimodal image input** | Send images to the assistant — upload, clipboard paste, drag & drop or URL — validated by an allow-list and delivered as native AF image content |
| 🌐 **Hosted tools** | Let the model provider run web search, a code-interpreter sandbox and file search on its own infrastructure — one option, no code |
| 🔒 **Safety check** | Optional AI-based prompt injection and jailbreak detection |
| ⏱️ **Rate limiting** | Per-user message limit with configurable time window (requires authentication for true per-user isolation) |
| ⏹️ **Stop button** | Cancel any in-flight AI request mid-stream — partial response is preserved in the chat |
| ✅ **Confirmation dialogs** | Destructive actions ask for user confirmation before execution — including MCP tools, and in the Agent Framework's native `ApprovalRequiredAIFunction` flow when you want AF interop |
| 🔐 **Role-based actions** | Actions restricted by ASP.NET Core identity roles |
| 📦 **Pluggable memory store** | Default in-memory, replaceable with Redis/EF Core/MongoDB |
| 💸 **Token & cost optimization** | Slim cache-friendly prompt, semantic tool filtering (embeddings), history compaction, RAG/memory gating |
| 🔌 **Any AI provider** | Azure OpenAI, OpenAI, Ollama, Azure AI Foundry, Anthropic, and more |

---

## Architecture overview

```
┌──────────────────────────────────────────────────────────────────────┐
│                         Blazor Application                           │
│                                                                      │
│   ┌──────────────┐      ┌────────────────────────────────────────┐   │
│   │  ChatWidget  │◄────►│          MentorOrchestrator            │   │
│   │  (Razor UI)  │      │          (Main Coordinator)            │   │
│   └──────────────┘      └────────────────┬───────────────────────┘   │
│                                          │                            │
│   ┌──────────────────────────────────────┤                            │
│   │   Per-call context injection         │                            │
│   │   · AppContextProvider (page,user)   │                            │
│   │   · RagContextProvider (documents)   │                            │
│   │   · SkillsContextProvider (catalogue)│                            │
│   │   · UIActionsMiddleware (per-action  │                            │
│   │     tools from IMentorPageContext)   │                            │
│   └──────────────────────────────────────┘                            │
│                                          │                            │
│              ┌───────────────────────────┼──────────────┐             │
│              ▼                           ▼              ▼             │
│        [MentorAgent]             [MentorAgent]    [MentorTeam]       │
│        OrderAgent                CustomerAgent    AnalysisTeam       │
│        (L2 Handoff)              (L2 Handoff)    (L3 GroupChat)      │
│              │                           │              │             │
│        [MentorAction]            [MentorAction]  [TeamMember]        │
│        C# methods                C# methods      sub-agents          │
│                                                                      │
│   ┌──────────────────────────────────────────────────────────────┐   │
│   │                    External Integrations                     │   │
│   │  MCP Client  │  MCP Server   │  A2A Consumer │  A2A Server        │   │
│   │  (tools from │  ([MentorAct] │  (remote       │ (agent-card.json + │   │
│   │   ext. MCPs) │   as MCP)     │   agents as L2)│  /a2a endpoint)    │   │
│   └──────────────────────────────────────────────────────────────┘   │
│                                                                      │
│   ┌──────────────────────────────────────────────────────────────┐   │
│   │  Built-in tools (each only when its feature is on)           │   │
│   │  navigate_to │ load_skill │ read_skill_resource               │   │
│   │  remember    │ forget_all │ invoke_ui_action (Path B only)    │   │
│   └──────────────────────────────────────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────────┘
                               │
               Microsoft Agent Framework
               (ChatClientAgent, HandoffWorkflow,
                GroupChatWorkflow, AgentSession)
```

The **MentorOrchestrator** builds the Main Coordinator — a `ChatClientAgent` on Path A, your own `AIAgent` on Path B — and gives it every capability as a tool: the L1 actions, MCP tools, the built-in tools, one tool per `[MentorTeam]` (a `GroupChatWorkflow` exposed under the team's snake_case name) and, when at least one specialist exists, `route_to_specialist`. That tool runs a `HandoffWorkflow` over the `[MentorAgent]` specialists, declarative agents and remote A2A agents and returns what the specialists said to the coordinator, which writes the reply. The built-in tools are conditional: `navigate_to` is always there; `load_skill` only when skills are enabled and at least one exists, `read_skill_resource` only when a skill has resources or comes from `SkillSources`; `forget_all` only with `UseMemoryContext`, and `remember` only when memory is on but auto-capture cannot run (Path B, or `MemoryAutoCapture = false`); `invoke_ui_action` only on Path B. Before every LLM call, three `AIContextProvider`s enrich the system prompt: `AppContextProvider` (page name, URL, user, roles, memory), `RagContextProvider` (retrieved documents), and `SkillsContextProvider` (skill catalogue). UI actions registered by the current page are injected as individual named tools by `UIActionsMiddleware` at the `IChatClient` level — with their own function-calling loop handled internally before any response reaches the outer pipeline. MCP tools from external servers are added as Level-1 tools alongside local `[MentorAction]` methods. Remote A2A agents sit in the same handoff workflow as local specialists, with three differences. A turn that itself **arrived** over A2A is never offered this host's remote agents — it is answered here, so chaining A → B → C through MentorAgent hosts is not supported in 1.0. On a host with remote agents, every `route_to_specialist` result opens with a note saying whose answer it is: a local specialist's (no remote agent was contacted), the remote system's, or `NOT X'S ANSWER` when a named remote agent never took part. And the router is told that a request addressed to a remote agent goes to it even when a local specialist covers the same subject.

---

## Getting started

### Installation

```bash
dotnet add package Novior.MentorAgent
```

`Novior.MentorAgent` brings no AI provider SDK: add the one you use, at the version you choose (up to 1.0.0-rc.14 it
carried Azure OpenAI's). For the Azure OpenAI example below:

```bash
dotnet add package Azure.AI.OpenAI --prerelease
dotnet add package Microsoft.Extensions.AI.OpenAI   # AsIChatClient() on the OpenAI SDK clients
dotnet add package Azure.Identity                    # only for DefaultAzureCredential / Entra ID
```

With the Azure **Responses** API, read [Provider package versions](#provider-package-versions) first.

### Minimal setup

In `Program.cs`:

```csharp
using Azure;                           // AzureKeyCredential
using Azure.AI.OpenAI;                 // AzureOpenAIClient (package Azure.AI.OpenAI)
using Novior.MentorAgent.Abstractions.Models; // MentorLanguage, MentorTheme, ...
using Novior.MentorAgent.Extensions;          // AddMentorAgent
using Microsoft.Extensions.AI;         // AsIChatClient

builder.Services.AddMentorAgent(options =>
{
	options.AppName        = "My App";
	options.AppDescription = "An order management application";
	options.Language       = MentorLanguage.Italian;

	// Choose your AI provider (see "AI providers" section below)
	options.ChatClient = new AzureOpenAIClient(
			new Uri("https://myresource.openai.azure.com"),
			new AzureKeyCredential(builder.Configuration["AzureOpenAI:Key"]!))
		.GetChatClient("gpt-4o-mini")
		.AsIChatClient();

	// Assemblies to scan for agents, actions, and pages
	options.ScanAssemblies = [typeof(Program).Assembly];
});
```

### Add the widget to your layout

In `MainLayout.razor` (or `App.razor`):

```razor
@using Novior.MentorAgent.Abstractions.Components

<ChatWidget />
```

That's it. The widget injects its own CSS and JS automatically — no changes to `App.razor` or `_Host.cshtml` are required. Only `ChatWidget` does this: a surface composed from the package's components without `ChatWidget` must add the `<link>` to `_content/Novior.MentorAgent.Abstractions/css/MentorAgent.css?v=10` and the `<script>` for `_content/Novior.MentorAgent.Abstractions/js/MentorAgent.js?v=10` itself, or it renders unstyled and voice, paste and drag-and-drop stay off.

> **The widget must be interactive.** In a Blazor Web App make the app interactive as a whole — `<Routes @rendermode="InteractiveServer" />` in `App.razor` (the template's *Interactivity location: Global*). In a layout that renders statically, `<ChatWidget />` shows its button and nothing happens when it is clicked. A page rendered statically has no circuit either, so it cannot register `IMentorPageContext` data or UI actions. For Auto / WebAssembly apps see [Blazor Server vs Blazor WASM](#blazor-server-vs-blazor-wasm).

### Namespaces

The attributes and page services used in the rest of this README live in these namespaces. Add them once to `_Imports.razor`:

```razor
@* [MentorPage], [MentorAction], [MentorAgent], [MentorTeam], [MentorSkill] *@
@using Novior.MentorAgent.Attributes
@* IMentorPageContext, IMentorAgent, IMentorTeam, IMentorStateService *@
@using Novior.MentorAgent.Abstractions.Interfaces
@* <ChatWidget /> *@
@using Novior.MentorAgent.Abstractions.Components
```

and to the C# files that declare tools, agents, teams or skills (`[TeamMember]` is in the global namespace):

```csharp
using System.ComponentModel;               // [Description]
using Novior.MentorAgent.Attributes;              // [MentorAction], [MentorAgent], [MentorTeam], [MentorSkill]
using Novior.MentorAgent.Abstractions.Interfaces; // IMentorAgent, IMentorTeam
```

---

## AI providers

MentorAgent supports any provider via two entry points: `IChatClient` (recommended for most cases) or `AIAgent` (required for providers that don't expose `IChatClient`). The provider's packages are yours to add: the snippets below need `Azure.AI.OpenAI` (Azure), `Microsoft.Extensions.AI.OpenAI` (`AsIChatClient` on the OpenAI clients; it brings `OpenAI`), `Azure.Identity` (`DefaultAzureCredential`), and for the last two `Microsoft.Agents.AI.Foundry` or `Microsoft.Agents.AI.Anthropic`. One combination needs a version hold: [Provider package versions](#provider-package-versions).

```csharp
// ── Azure OpenAI — Chat Completions
options.ChatClient = new AzureOpenAIClient(endpoint, credential)
	.GetChatClient("gpt-4o-mini").AsIChatClient();

// ── Azure OpenAI — Responses API (service-managed history)
// GetResponsesClient() takes no argument — the deployment name goes to AsIChatClient.
// The Responses client is experimental in the OpenAI SDK: without the pragma the build fails with OPENAI001.
#pragma warning disable OPENAI001
options.ChatClient = new AzureOpenAIClient(endpoint, credential)
	.GetResponsesClient().AsIChatClient("gpt-4o-mini");
#pragma warning restore OPENAI001
// Required with Responses: the service owns the conversation, and the Agent Framework refuses to combine
// its conversation id with a local ChatHistoryProvider — without this every turn fails with
// "Only ConversationId or ChatHistoryProvider may be used, but not both".
options.UseServiceManagedHistory = true;

// ── OpenAI direct
options.ChatClient = new OpenAIClient("sk-...")
	.GetChatClient("gpt-4o").AsIChatClient();

// ── Ollama (local) — through its OpenAI-compatible endpoint: same SDK, no extra package
options.ChatClient = new OpenAIClient(
		new System.ClientModel.ApiKeyCredential("ollama"),   // Ollama ignores it; the SDK requires one
		new OpenAIClientOptions
		{
			Endpoint       = new Uri("http://localhost:11434/v1"),
			NetworkTimeout = TimeSpan.FromMinutes(20),          // a CPU model can take minutes on a long prompt
		})
	.GetChatClient("llama3.2").AsIChatClient();
// Ollama's default context (4096 tokens) is shorter than MentorAgent's prompt and is truncated from the
// start without an error — create a variant with `PARAMETER num_ctx 16384` (ollama create).
// On a slow local model also raise SafetyCheckTimeout, or point the checks at a fast ClassifierChatClient.

// ── Azure AI Foundry (AIProjectClient) — requires AIAgent, and:
//    <PackageReference Include="Microsoft.Agents.AI.Foundry" Version="[1.17.0-preview.260804.1]" />
options.Agent = new AIProjectClient(endpoint, credential)
	.AsAIAgent(model: "gpt-4o-mini", instructions: "You are a helpful assistant.");

// ── Anthropic Claude — requires AIAgent, and: dotnet add package Microsoft.Agents.AI.Anthropic --prerelease
options.Agent = new AnthropicClient() { APIKey = apiKey }
	.AsAIAgent(model: "claude-haiku-4-5", instructions: "...");
```

> ⚠️ Set either `ChatClient` **or** `Agent`, not both.

### Embedding model (optional)

An embedding model is what makes **semantic tool filtering**, **semantic memory relevance** and **semantic model routing** possible — but setting it switches none of them on. Each has its own flag, off by default: `EnableToolFiltering = true`, `MemoryRelevanceFiltering = true`, and `RoutingStrategy = MentorRoutingStrategy.Semantic` (together with a `StrongChatClient`) — see [Token & cost optimization](#token--cost-optimization). Optional — everything works without it: a flag turned on without a generator logs a warning and falls back (all tools sent, most recent memories, no routing), never to a keyword heuristic.

```csharp
// Azure OpenAI — a separate embedding deployment
options.EmbeddingGenerator = new AzureOpenAIClient(endpoint, credential)
	.GetEmbeddingClient("text-embedding-3-small").AsIEmbeddingGenerator();

// OpenAI direct
options.EmbeddingGenerator = new OpenAIClient("sk-...")
	.GetEmbeddingClient("text-embedding-3-small").AsIEmbeddingGenerator();
```

### Path A vs Path B — feature matrix

| Feature | `ChatClient` (Path A) | `AIAgent` (Path B) |
|---|---|---|
| L1 actions | ✅ | ✅ |
| L2 Handoff agents | ✅ | ❌ requires `IChatClient` — skipped, with a warning when the coordinator is built |
| L3 Group Chat teams | ✅ | ❌ requires `IChatClient` — skipped, with a warning when the coordinator is built |
| A2A remote agents | ✅ | ❌ requires `IChatClient` — skipped, with a warning when the coordinator is built, and the peers' cards are not fetched |
| MCP client tools | ✅ | ✅ |
| RAG | ✅ | ✅ |
| Agent Skills | ✅ | ✅ |
| UI Actions (per-action tools) | ✅ via `UIActionsMiddleware` | ⚠️ single generic `invoke_ui_action` dispatcher |
| Safety check (input and output) | ✅ | ⚠️ runs only when `ClassifierChatClient` is set — otherwise skipped, with a warning when the coordinator is built |
| Session history reduction | ✅ configurable | ✅ configured in the agent |
| Custom `ChatHistoryProvider` | ✅ via options | ⚠️ must be set in the pre-built agent |
| Declarative (YAML) agents | ✅ | ❌ skipped with a warning — they need a `ChatClient` |
| Hosted tools (`HostedTools`) | ✅ | ❌ declare them on the pre-built agent itself (warning when the coordinator is built) |
| Semantic tool filtering (`EnableToolFiltering`) | ✅ | ❌ no effect (warning when the coordinator is built) — filter the tools on your agent |
| Model routing (`StrongChatClient`) | ✅ | ❌ |
| Memory auto-capture (`MemoryAutoCapture`) | ✅ | ✅ with a `ClassifierChatClient`; without one ⚠️ falls back to the `remember` tool |
| Structured outputs (`IMentorStructured`) | ✅ | ❌ returns `default` with a warning |

> When using `AIAgent` (Path B), `ChatHistoryProvider` **cannot** be added after construction — configure it directly in the agent you pass to `options.Agent`.

---

## The three-level agent model

MentorAgent organizes AI capabilities in three progressive levels of complexity.

### Level 1 — Actions on a service

The simplest level. Decorate C# methods with `[Description]` (standard .NET, zero dependencies) or `[MentorAction]` (adds confirmation, roles, navigation, hints).

```csharp
// Register the service in DI as usual
builder.Services.AddScoped<OrderService>();
```

```csharp
public class OrderService
{
	// Simple — [Description] from System.ComponentModel, zero dependencies
	[Description("Returns the list of active orders")]
	public async Task<List<Order>> GetActiveOrdersAsync() { ... }

	// Advanced — full [MentorAction] with all parameters
	[MentorAction(
		Description          = "Cancels an existing order",
		Category             = "Orders",             // tag of this skill on the A2A agent card
		RequiresConfirmation = true,                 // shows confirmation banner before executing
		RequiredRoles        = ["Manager"],          // any one of the listed roles is enough
		ProactiveHint        = "Suggest checking active orders first", // appended to the tool description as "Guidance: ..."
		NavigateTo           = "/orders")]           // AI navigates here automatically after success
	public async Task<bool> CancelOrderAsync(int orderId, string reason) { ... }
}
```

MentorAgent discovers the service via `ScanAssemblies` and exposes its methods as AI tools automatically. The AI calls the right method based on the user's natural language request.

**`[MentorAction]` parameters summary:**

| Parameter | Description |
|---|---|
| `Description` | **Required.** Natural language description used as the AI tool description |
| `Category` | Published as the tag of this action's skill on the A2A agent card. It groups nothing and is not used anywhere else |
| `RequiresConfirmation` | Shows a confirmation banner before executing. Use for destructive or irreversible operations |
| `RequiresConfirmationDeclared` | Read-only, not set in the attribute: `true` when the attribute writes `RequiresConfirmation`, true or false. It tells an action that declares nothing, which asks with `RequireConfirmationForWrites` on, from one that declares `RequiresConfirmation = false`, which does not: `RequiresConfirmation` reads `false` for both |
| `ReadOnly` | Declares that the action only reads — it changes no data. MentorAgent takes your word for it: the action is published to MCP clients with `readOnlyHint`, which some clients take as leave to skip their own confirmation — so a write declared `ReadOnly` by mistake runs from them with nobody asked — and with `RequireLookupForRecordQuestions` on it is one the assistant may be required to call before answering a question about a value of your records. Ignored when the action also needs confirmation. Declare `[Description]` methods by name with `options.IsReadOnlyAction` |
| `RequiredRoles` | ASP.NET Core identity roles allowed to invoke the action — holding **any one** of them is enough (`["Manager", "Admin"]` means Manager *or* Admin). The user must be authenticated and an `AuthenticationStateProvider` must be registered, otherwise the call is refused. Empty = no role check, accessible to everyone including anonymous users |
| `ProactiveHint` | Guidance for the model on when or how to use the action. Appended to the tool's description as `Guidance: <hint>` for the assistant's own tools (coordinator, specialists, team members); not added on the MCP server surface, and ignored by semantic tool filtering (tools are matched on `name: description` without the hint) |
| `NavigateTo` | URL the AI navigates to automatically after successful execution |

#### Which methods become tools

The same two rules hold at every level — the coordinator's actions, a specialist's methods and a team
member's `Tools`:

- **Public instance methods declared on the class itself**, marked `[MentorAction]` or `[Description]` with
  a text. A method inherited from a base class is not discovered, nor is a static method, and a
  `[Description("")]` is ignored. Declare the method on the class you scan (or list in `Tools`).
- **A method with `[Description]` alone is a tool with no roles and no confirmation.** `RequiredRoles`,
  `RequiresConfirmation` and the default that makes writes ask exist only on `[MentorAction]`. Such a
  method is offered like any other action — with [tool filtering](#semantic-tool-filtering) on, also among
  the actions sent when a message matches nothing — so a method that changes data needs `[MentorAction]`,
  and one that only reads is declared with `options.IsReadOnlyAction`.

#### Tool names — the rule you need before configuring anything else

Several options identify a tool **by name**, not by method: `RequiresApproval`, `IsReadOnlyAction`,
`OnToolResult`, `EvalChecks.ToolCalledCheck`, the tool-filtering logs, the metrics `TopActions` list.
The attributes do not: a call is checked against the `RequiredRoles`, `RequiresConfirmation` and
`NavigateTo` of the method it runs, so a coordinator's action and a specialist's that share a name each
keep their own. The name is derived from the C# member, so you have to know the rule:

> **PascalCase → snake_case, with a trailing `Async` dropped first.**

| C# member | Tool name |
|---|---|
| `GetActiveOrdersAsync()` | `get_active_orders` |
| `CancelOrderAsync(int, string)` | `cancel_order` |
| `GetHTTPStatus()` | **get_h_t_t_p_status** — every capital starts a new word, so acronyms split letter by letter; name it `GetHttpStatus` to get **get_http_status** |
| `[MentorTeam(Name = "Business Analysis Team")]` | `business_analysis_team` |
| `[MentorSkill(Name = "expense-report")]` | *no tool* — a skill is loaded with `load_skill("expense-report")` under its own name, unchanged; only its **methods** become tools (`SubmitExpenseReportAsync` → `submit_expense_report`) |

Spaces and dashes become underscores, so an attribute `Name` is normalised the same way a method
name is. Gating an action therefore looks like this — note it is the *tool* name, not the method:

```csharp
options.RequiresApproval = tool => tool is "cancel_order" or "issue_refund";
```

Renaming a C# method renames its tool, which silently unhooks any option keyed on the old name.
There is no compile-time link between the two, so pin the ones that matter in a test:

```csharp
[Fact]
public void CancelOrder_StillRequiresApproval()
    => _options.RequiresApproval!("cancel_order").Should().BeTrue();
```

---

### Level 2 — Specialized agent with Handoff

Decorate a class with `[MentorAgent]` to create a dedicated AI agent connected to the Main Coordinator via a **Handoff Workflow**. The coordinator delegates by calling its `route_to_specialist` tool (with the specialist's name in `specialist` when the user names one): a router inside the workflow hands the request to the matching agent, and what the specialist says comes back to the coordinator as the tool result — the coordinator writes the reply the user sees. Delegation requires `ChatClient` (Path A).

```csharp
[MentorAgent(
	Name        = "OrderAgent",
	Description = "Handles everything related to orders: creation, tracking, cancellation",
	HandoffTo   = ["CustomerAgent", "InvoiceAgent"]  // can hand off further
)]
public class OrderAgent : IMentorAgent
{
	private readonly OrderService _orders;
	public OrderAgent(OrderService orders) => _orders = orders;

	[Description("Creates a new order for a customer")]
	public async Task<Order> CreateOrderAsync(int customerId, List<string> products) { ... }

	[Description("Retrieves the status of an order")]
	public async Task<OrderStatus> GetOrderStatusAsync(int orderId) { ... }
}
```

Register the agent in DI:

```csharp
builder.Services.AddScoped<OrderAgent>();
```

MentorAgent builds a `ChatClientAgent` from the class, wires it into the Handoff graph, and generates the system prompt from `Name` and `Description` (or you can supply a custom `Instructions`).

Implementing `IMentorAgent` is optional — it is an empty marker interface that MentorAgent never reads (discovery is by the attribute alone), useful to find and inject your agents in your own code and tests. It validates nothing: a missing `AddScoped<OrderAgent>()` is reported as a warning when the coordinator is built, and that agent's tools are dropped.

**`[MentorAgent]` parameters:**

| Parameter | Required | Description |
|---|---|---|
| `Name` | ✅ | Agent name — used as the key in the Handoff graph and in the coordinator's system prompt |
| `Description` | ✅ | Natural language description of the agent's capabilities. Used by the coordinator to decide when to delegate |
| `HandoffTo` | — | Names of other `[MentorAgent]` agents this agent can hand off to. Must match the `Name` values exactly (case-insensitive) |
| `Instructions` | — | Custom system prompt for this agent, used **exactly as written**. If omitted, MentorAgent auto-generates one from `Name` and `Description` — and the generated prompt carries a grounding rule (*state only facts a tool returned; if nothing provides what is asked, say so — never estimate or invent a number, a name, a date or a status*). A custom prompt replaces that rule too: **include your own**, or a specialist asked for a figure none of its tools returns may make one up |

> ⚠️ **Important:** agent names in `HandoffTo` must match exactly the `Name` in the target `[MentorAgent]` attribute (case-insensitive). A mismatch produces a warning in the logs when the coordinator is built — on the first message of a session, or at startup with `WarmUpAtStartup = true` — and skips that handoff edge.

**What a delegation returns.** The coordinator delegates by calling `route_to_specialist(request, specialist?)`. Inside, a small router agent (its own ~400-token prompt, no application tools) hands the request to exactly one specialist. The tool gives the coordinator what the specialists **said**, as plain text. Three other outcomes are reported explicitly, so the assistant never tells the user that something was forwarded when it was not:

| Result starts with | Meaning | Log |
|---|---|---|
| *(the specialist's answer)* | A specialist took the request | Debug: `route_to_specialist returned: …` (who spoke, never the text) |
| `NOT DELEGATED` | No specialist took it (the router answered itself or found no match). The coordinator answers with its own tools or says it could not be handled | Warning: `route_to_specialist ended without any specialist answering …` |
| `DECLINED BY THE USER` | A specialist's action asked for confirmation and the user declined it. The result names the declined action, and the coordinator says in one sentence that it did not proceed, with no reason and no retry. When another action ran in the same request, the result starts `DECLINED BY THE USER, IN PART`, names both, and the coordinator says what was and was not done; reads (declared `ReadOnly` or matched by `IsReadOnlyAction`) are not counted. The specialist's words are not passed on | Debug: `route_to_specialist: the user declined an action in the delegated request.` |
| `DELEGATION FAILED` | A specialist was reached and threw | Warning: `route_to_specialist: the specialist it was handed to failed — <error>` |

The router, the specialists and the team members all run on your `ChatClient` inside the token meter, so a delegated turn shows up in full on the [dashboard](#token--cost-dashboard).

---

### Level 3 — Collaborative team (Group Chat)

Use `[MentorTeam]` to define a **Group Chat** where multiple AI agents collaborate — debating, analyzing, and approving — before a result is returned to the user or handed off to an L2 agent for execution.

```csharp
[MentorTeam(
	Name          = "BusinessAnalysisTeam",
	Description   = "Analyzes business data and produces an approved action plan",
	MaxIterations = 8,                                      // forced termination after 8 turns
	TriggerOn     = ["analysis", "business plan", "budget"], // keywords that activate this team
	HandoffTo     = ["OrderAgent", "CustomerAgent"])]
public class BusinessAnalysisTeam : IMentorTeam            // IMentorTeam is optional, recommended
{
	[TeamMember(
		Role         = "DataAnalyst",
		Tools        = [typeof(ReportTools), typeof(OrderTools)],
		Instructions = "Analyze the data and propose solutions with numbers.")]
	public object? Analyst { get; set; }

	[TeamMember(
		Role         = "BusinessApprover",
		Instructions = "Review the analyst's proposal. Reply APPROVED or REJECTED with reasons.")]
	public object? Approver { get; set; }

	[TeamTerminationCondition]
	public bool ShouldTerminate(string lastMessage, string lastSpeaker)
		=> lastSpeaker == "BusinessApprover" &&
		   (lastMessage.Contains("APPROVED") || lastMessage.Contains("REJECTED"));
}
```

MentorAgent builds a `GroupChatWorkflow` from this declaration and gives it to the coordinator as a tool named after the team (`business_analysis_team` — see [Tool names](#tool-names--the-rule-you-need-before-configuring-anything-else)); the discussion's text is the tool's result. The team is not a node of the handoff graph, and `HandoffTo` hands nothing off by itself: the agents it names are added to the tool's description, and when the final message carries `[TEAM:APPROVED]` and no member wrote `[TEAM:REJECTED]` — the tokens every member is instructed to emit, the second only for a definitive no (a request for changes carries neither; both are stripped before the text reaches the user) — the result ends with an instruction to execute the approved actions, which the coordinator does through `route_to_specialist`. It also says that an action may ask the user to confirm first, and that a declined confirmation is the user's decision, not a problem. A discussion whose final message carries no verdict is not approved, and neither is a "yes" followed by a member's `[TEAM:REJECTED]`. Without a `[TeamTerminationCondition]` the discussion ends at the first verdict; a host's condition decides alone when to stop, within `MaxIterations`. A plain "APPROVED" satisfies the termination condition above but does not trigger that step.

Register every class listed in `[TeamMember(Tools = ...)]` in DI (`builder.Services.AddScoped<ReportTools>();`) — a tool class the container cannot resolve is skipped with a warning and the member runs without it. Teams require `ChatClient` (Path A).

A class listed in `Tools` is that member's: its methods are **not** also the coordinator's actions, nor published on `/mcp` or the A2A card, even though it is in DI. At startup an Information line names each such class, the members that list it and its methods. The exception is a `[MentorSkill]` class, whose methods are coordinator tools by the skill's own role. Member tools are discovered by the same rules as the coordinator's ([Which methods become tools](#which-methods-become-tools)), and keep what `[MentorAction]` declares (`ReadOnly`, roles, confirmation). A member is told *"These tools are read-only."* only when every one of its tools is declared read-only (`ReadOnly = true` or `IsReadOnlyAction`) and none asks for confirmation.

**`[MentorTeam]` parameters:**

| Parameter | Required | Description |
|---|---|---|
| `Name` | ✅ | Team name — used as the key in the routing graph and shown in logs |
| `Description` | ✅ | Description of the team's purpose. Used by the coordinator to decide when to activate it |
| `TriggerOn` | — | Keywords injected into the coordinator's prompt as a strong directive: *ALWAYS delegate to this team when the request involves* these words, *do NOT answer directly*. The model still makes the call (there is no code-level route), but choose specific keywords — a broad one such as `"order"` sends ordinary requests through a multi-turn Group Chat |
| `MaxIterations` | — | Maximum number of turns in the Group Chat before forced termination. Default: `10` |
| `HandoffTo` | — | L2 agents to delegate execution to after the team approves a plan |

**`[TeamMember]` parameters:**

| Parameter | Required | Description |
|---|---|---|
| `Role` | ✅ | Role name within the team (e.g. `"DataAnalyst"`, `"Approver"`) |
| `Instructions` | ✅ | System prompt for this member — defines what it should do and how it should respond |
| `Tools` | — | Tool classes this member can call during the discussion — the member's only, not the coordinator's. Should be **read-only** — write operations belong in L2 agents via `HandoffTo` |

- **`[TeamTerminationCondition]`** is required when you need custom exit logic. Required method signature: `bool ShouldTerminate(string lastMessage, string lastSpeaker)`. Without it, members take turns round-robin and the discussion stops at the first message that carries `[TEAM:APPROVED]` or `[TEAM:REJECTED]`, or after `MaxIterations` turns.
- **`TriggerOn`** keywords are injected into the Coordinator's prompt as an *always delegate to this team* directive — the model still decides, but pick specific words, because a broad one routes ordinary requests through the Group Chat.
- `[TeamMember]` tools should be **read-only** (queries, reports). Write operations should be delegated to L2 agents via `HandoffTo`.
- Implementing `IMentorTeam` is optional but recommended for the same reasons as `IMentorAgent`.

---

## Page navigation

Decorate Blazor pages with `[MentorPage]` to let the AI navigate to them on user request.

```razor
@* Simple page — navigation only *@
@attribute [MentorPage(Url = "/orders", Name = "Orders")]

@* Page with UI actions — on Blazor Server and in MAUI Blazor Hybrid, navigate_to waits for SignalReady() *@
@attribute [MentorPage(Url = "/orders-interactive", Name = "Interactive Orders",
	HasUIActions = true,
	ReadyTimeout = 3000,
	Description  = "Order management with inline editing and filtering")]
```

Pages are discovered at startup from `ScanAssemblies` — they don't need to be visited first. When `HasUIActions = true` and the page runs in the same process as the turn — a Blazor Server circuit or a MAUI Blazor Hybrid app — `navigate_to` waits for the new page to call `PageContext.SignalReady()` (up to `ReadyTimeout`), so its UI actions are registered before the AI continues. A signal the page being left gave when it opened does not count. To the page already shown (the same path, whatever the query) `navigate_to` does not wait, since Blazor does not initialize that page again. A turn that arrives over the hub (WebAssembly, React, a MAUI app with its own native UI…), SSE or A2A does **not** wait — nothing there can call `SignalReady()`; the new page's actions reach the model with the client's next page-context snapshot, i.e. on the user's next message. On WebAssembly `SignalReady()` is a no-op and costs nothing, so the same page code works on both.

**A component with two routes**, such as `/orders` and `/orders/{id}`: when `navigate_to` goes from one of its routes to the other, Blazor keeps the same instance and does not run `OnInitialized` again, so no new signal comes. The wait runs to `ReadyTimeout` and logs its warning, then the turn goes on with the page's actions, which are still registered. Call `SignalReady()` at the end of `OnParametersSet` too (BUG-194).

**`[MentorPage]` parameters:**

| Parameter | Required | Description |
|---|---|---|
| `Url` | ✅ | Page URL (e.g. `"/orders"`). Used by the `navigate_to` tool |
| `Name` | ✅ | Human-readable page name injected into the system prompt |
| `Description` | — | Optional description of the page's features shown to the AI |
| `HasUIActions` | — | If `true`, `navigate_to` waits for `PageContext.SignalReady()` on the new page — only where the page runs in the turn's process (a Blazor Server circuit or a MAUI Blazor Hybrid app); hub (WebAssembly, React, native MAUI…), SSE and A2A turns do not wait, and the page's actions reach the model on the next message. Default: `false` |
| `ReadyTimeout` | — | Timeout in milliseconds for `SignalReady()`. Used only when `HasUIActions = true` and the page runs in the turn's process (a Blazor Server circuit or a MAUI Blazor Hybrid app). Default: `2000` |

---

## Page context and UI actions

`IMentorPageContext` is a scoped service injectable in any Blazor page. It has two responsibilities:

1. **Share visible data** — key/value pairs serialized live into the AI system prompt before every call (filter state, selected item, visible row count, etc.).
2. **Register UI actions** — C# lambdas the AI can invoke directly on the current page without going through a business service (highlight a row, open a modal, pre-fill a form).

### How UI actions work (architecture)

Each registered UI action becomes its **own named AI tool** before every LLM call — injected dynamically via `UIActionsMiddleware` (a `DelegatingChatClient` wrapping the raw model). The AI sees `highlight_row(parameter: integer: order ID)` directly in its tool list, not a generic dispatcher. This:

- Eliminates hallucinated action names (the AI sees exact names, not strings to guess)
- Carries each action's parameter description (`parameterHint`) in its tool description — the JSON schema itself is the same for every action (one optional `parameter` of any JSON type), so the hint is what tells the model what to pass
- Skips, with a warning, an action whose name matches a tool the coordinator already has (an L1 action, an MCP tool, `navigate_to`…) — give UI actions names of their own
- Enables reliable multi-action chains

UI actions are scoped to the **current page**: they appear in the tool list only while the page is mounted, and disappear the moment the page calls `PageContext.Clear(pageName)` in `Dispose()`, with the name it gave `SetPageName`. Blazor disposes the old page after it has initialized the new one, so a bare `Clear()` there would also remove what the new page has just registered. Give every page its own name: when two components share one, the old page's `Clear(pageName)` takes it for the current page and clears everything.

### Registering UI actions

Four overloads are available, from simple to fully typed and async:

```razor
@using Novior.MentorAgent.Abstractions.Interfaces
@inject IMentorPageContext PageContext
@implements IDisposable

@code {
protected override void OnInitialized()
{
    PageContext
        .SetPageName("Orders")
        // ── Share current UI state with the AI ───────────────────────────────
        .Set("ActiveFilter",  "Pending")
        .Set("VisibleRows",   _orders.Count)
        .Set("SelectedOrder", _selectedOrder)

        // ── 1. Simple action — no parameter ─────────────────────────────────
        .RegisterUIAction(
            "open_create_modal",
            "Opens the new order creation dialog",
            _ => OpenCreateModal())

        // ── 2. Typed parameter — no manual casting required ──────────────────
        .RegisterUIAction<int>(
            "highlight_row",
            "Highlights an order row by its ID",
            id => HighlightRow(id),          // id is int, not object?
            parameterHint: "integer: order ID")

        // ── 3. Typed async — awaited before the AI continues ─────────────────
        .RegisterUIActionAsync<int>(
            "select_order",
            "Selects an order and loads its details panel",
            async id => {
                await InvokeAsync(() => { _selectedId = id; StateHasChanged(); });
            },
            parameterHint: "integer: order ID")

        // ── 4. Complex typed parameter (DTO deserialized from JSON) ──────────
        .RegisterUIActionAsync<OrderFormModel>(
            "prefill_form",
            "Pre-fills the order form with the provided data",
            async model => {
                await InvokeAsync(() => { _form = model; StateHasChanged(); });
            },
            parameterHint: "JSON: { customerId, items, notes }");

    // Signal the AI that the page is ready — last line of OnInitialized, required when HasUIActions = true
    // (Blazor Server, MAUI Blazor Hybrid: navigate_to waits for it; WebAssembly: a no-op)
    PageContext.SignalReady();
}

// Clear this page's context and actions in Dispose, by the name given to SetPageName: Blazor disposes
// the old page after the new one has registered its own, which a bare Clear() would remove too
public void Dispose() => PageContext.Clear("Orders");
}
```

### UI action overloads reference

| Overload | Parameter | Execution | Use when |
|---|---|---|---|
| `RegisterUIAction(name, desc, Action<object?>)` | Raw `object?` (cast manually) | Synchronous | Simple no-param or legacy code |
| `RegisterUIAction<TParam>(name, desc, Action<TParam>)` | Auto-deserialized from JSON | Synchronous | Typed param, sync handler |
| `RegisterUIActionAsync(name, desc, Func<object?, Task>)` | Raw `object?` | Async | No-param async actions |
| `RegisterUIActionAsync<TParam>(name, desc, Func<TParam, Task>)` | Auto-deserialized from JSON | Async | Typed param, async handler *(recommended)* |
| `UnregisterUIAction(name)` | — | — | Remove a specific action dynamically (e.g. when a feature becomes unavailable) |

### Context data methods reference

| Method | Description |
|---|---|
| `SetPageName(name)` | Sets the current page name injected into the system prompt |
| `Set(key, value)` | Adds or updates a context entry (any serializable value) |
| `Remove(key)` | Removes a single context entry without clearing everything |
| `Clear()` | Removes all context data and all registered UI actions, whichever page registered them |
| `Clear(pageName)` | Removes what the page named `pageName` registered, or everything when it is still the current page. Call it from `Dispose()` with the page's own name, and call `SetPageName` before anything else |

### Automatic parameter schema generation

For the two typed overloads (`RegisterUIAction<TParam>` and `RegisterUIActionAsync<TParam>`), the `parameterHint` argument is **automatically generated from the type via reflection** when you omit it. You only need to provide it if you want to override the generated text. Blazor Server and WebAssembly use the same generator, and the hub keeps the hint a client sends, so the model sees `(parameter: …)` for WebAssembly, React and MAUI actions too.

| `TParam` | Auto-generated `parameterHint` |
|---|---|
| `int`, `long`, `short`, `byte` | `"integer"` |
| `float`, `double`, `decimal` | `"number"` |
| `bool` | `"boolean"` |
| `string` | `"string"` |
| `Guid` | `"string (GUID)"` |
| `DateTime`, `DateTimeOffset` | `"string (ISO 8601 date)"` |
| `Status` *(enum)* | `"string (Active\|Inactive\|Pending)"` |
| `int?` | `"integer?"` |
| `List<int>` | `"array<integer>"` |
| `Dictionary<string,int>` | `"object<string,integer>"` |
| `OrderFormModel` *(class)* | `"{ customerId: integer, productName: string, quantity: integer }"` |

This means the AI sees a precise, field-by-field description of what to pass — even for complex DTOs — without any manual work:

```csharp
// parameterHint omitted → auto-generated as "{ customerId: integer, productName: string, quantity: integer }"
.RegisterUIActionAsync<OrderFormModel>(
    "prefill_form",
    "Pre-fills the order form with the provided data",
    async model => {
        await InvokeAsync(() => { _form = model; StateHasChanged(); });
    })

// Override only when the auto-generated hint is not descriptive enough
.RegisterUIAction<int>(
    "highlight_row",
    "Highlights an order row by its ID",
    id => HighlightRow(id),
    parameterHint: "integer: order ID")   // ← manual override for extra clarity
```

> **Async handlers are awaited on Blazor Server** — the AI waits for the handler to complete before generating its next response. This makes multi-action chains reliable: the AI can call `select_order(42)` and then `highlight_row(42)`, knowing each step is done before it proceeds. A UI action requested through the hub (WebAssembly, React, MAUI…) is fire-and-forget: the model is told it succeeded once the request is sent to the client, not when the handler finishes.

The AI automatically receives current page context (URL, page name, registered data) injected into its system prompt on every call — with no extra configuration required.

---

## Agent Skills

Agent Skills are **domain knowledge + execution packages** with two complementary roles:

| Role | What it provides | When used |
|---|---|---|
| **Knowledge** | Instructions, policy, rules, workflows (markdown) | Loaded on demand via `load_skill` |
| **Tools** | `[Description]`/`[MentorAction]` methods on the skill class | Always available as L1 tools |

Rather than dumping all domain knowledge into the system prompt, MentorAgent uses **progressive disclosure**:

1. The **skill catalogue** (a short header plus one `name: description` line per skill — a few dozen tokens each) is always injected into the system prompt.
2. When the AI needs expertise, it calls `load_skill("skill-name")` to receive the full instructions — then uses that knowledge to call the right methods with the right parameters.
3. Attached resource files (policy docs, FAQ pages, templates) are accessible via `read_skill_resource`.

10 registered skills cost roughly **1,000 tokens** in the system prompt instead of the 50,000+ tokens you'd need to inline everything upfront.

### Setup

```csharp
builder.Services.AddMentorAgent(options =>
{
    // ...AppName and ChatClient as in Minimal setup — MentorAgent refuses to start without them
    options.EnableSkills   = true;
    options.SkillsFolder   = "Skills"; // relative to content root, or absolute path
    options.ScanAssemblies = [typeof(Program).Assembly];
});
```

### Dual-role skill class (knowledge + tools)

This is the most powerful pattern. The class provides **both** the domain instructions and the executable tools:

```csharp
// Register in DI — required when the class has methods
builder.Services.AddScoped<ExpenseReportSkill>();
```

```csharp
[MentorSkill(
    Name             = "expense-report",
    Description      = "Handles expense report filing, validation, and policy checks",
    InstructionsFile = "Skills/expense-report/SKILL.md")]   // or use Instructions = "..."
public class ExpenseReportSkill
{
    private readonly ExpenseRepository _repo;
    public ExpenseReportSkill(ExpenseRepository repo) => _repo = repo;

    // ── Methods become L1 tools — always registered on the coordinator ──────

    [Description("Submits a new expense report for the current user")]
    public async Task<string> SubmitExpenseReportAsync(
        string category, decimal amount, string notes) { ... }

    [MentorAction(
        Description          = "Approves a pending expense report",
        RequiresConfirmation = true,
        RequiredRoles        = ["Manager"])]
    public async Task<bool> ApproveExpenseReportAsync(int reportId) { ... }

    [Description("Returns the reimbursement policy for a given expense category")]
    public string GetPolicyForCategory(string category) { ... }
}
```

The flow when a user asks *"Submit a €47 expense for today's business lunch"*:

1. AI sees `submit_expense_report` in its tool list — the trailing `Async` is stripped, see [Tool names](#tool-names--the-rule-you-need-before-configuring-anything-else)
2. Before calling it, AI calls `load_skill("expense-report")` — learns that meals have a €50 limit, require a category and description
3. AI calls `submit_expense_report("Meals", 47, "Business lunch")` with policy-correct parameters

Without the skill, the AI guesses. **With the skill, the AI knows the rules before it acts.**

### Knowledge-only skill (no methods)

Use this when the skill provides guidance but all execution is handled by existing service tools:

```csharp
// No DI registration needed — no methods, no instance required
[MentorSkill(
    Name        = "refund-policy",
    Description = "Return and refund rules for the online store",
    Instructions = """
        ## Refund Policy
        - Items can be returned within 30 days of purchase.
        - Digital products are non-refundable once downloaded.
        - Damaged items: customer submits a photo via the support ticket tool.
        - Refunds are processed within 5–7 business days to the original payment method.
        """)]
public class RefundPolicySkill { }
```

### File-based skills (auto-discovery)

MentorAgent also discovers skills automatically from the filesystem — no class needed:

```
Skills/
  expense-report/
    SKILL.md          ← required: skill instructions in markdown
    policy.md         ← optional: resource accessible via read_skill_resource
    examples.md       ← optional: additional resource
  refund-policy/
    SKILL.md
  shipping-rules/
    SKILL.md
    carrier-list.txt
```

`SKILL.md` format — the first non-empty line after a heading becomes the catalogue description (only that line — keep it to one sentence on one line; without one, the folder name is used):

```markdown
# Expense Report Filing

Handles expense report submission, validation, approval workflow, and policy enforcement.

## Eligible Expenses
- Meals: up to €50/day domestic, €80/day international
- Travel: economy class only for flights under 4 hours
...
```

> **Class-based overrides file-based** — if both define a skill with the same name (case-insensitive), the class attribute wins, and it wins **whole**: a class registration carries no resources, so the folder's side-car files (`policy.md`, `examples.md` above) are no longer reachable through `read_skill_resource`. To keep resources, let the folder be the skill — put the methods in a class without a `[MentorSkill]` of the same name — or move the resource content into the instructions.

### How the AI sees skills

System prompt (catalogue only — always injected, ~100 tokens total):

```
## Available Skills
When a request requires specialised expertise in any area below,
call load_skill with the skill name to get full instructions before responding:
- **expense-report**: Handles expense report filing, validation, and policy checks
- **refund-policy**: Return and refund rules for the online store
- **shipping-rules**: Shipping carrier rules and delivery SLAs
```

Full instructions and resources are **never in the prompt by default** — only loaded when the AI decides it needs them.

### `[MentorSkill]` parameters

| Parameter | Description |
|---|---|
| `Name` | Unique skill name in kebab-case (e.g. `"expense-report"`). Key for `load_skill` |
| `Description` | One-sentence description shown to the AI in the skill catalogue |
| `InstructionsFile` | Path to a markdown file (absolute or relative to content root). When omitted, MentorAgent reads `{SkillsFolder}/{Name}/SKILL.md`. When that file is missing, or the path you gave does not exist (logged as a warning), the instructions are just the skill's name and `Description` |
| `Instructions` | Inline markdown text. Takes precedence over `InstructionsFile` |

### Agent Skills configuration options

| Option | Type | Default | Description |
|---|---|---|---|
| `EnableSkills` | `bool` | `false` | Enables skill discovery and the `load_skill` / `read_skill_resource` tools |
| `SkillsFolder` | `string` | `"Skills"` | Folder to scan for file-based skills. Relative to content root or absolute |
| `SkillSources` | `IList<AgentSkillsSource>` | empty | Additional sources, using the Agent Framework's own abstraction — see below |
| `SkillFilter` | `Func<AgentSkill, bool>?` | `null` | Keeps or drops a skill contributed by `SkillSources`. Does not apply to your own skills |
| `SkillsRefreshInterval` | `TimeSpan?` | `null` | Shares one list from `SkillSources` across every session in the process (wrapped in the framework's `CachingAgentSkillsSource`) and re-fetches it when a session is built after this long. Without it, every new session (circuit, hub connection, SSE request) re-reads the sources when its coordinator is built and keeps that list for its lifetime. Set it for a remote or expensive source |

### Skills from somewhere else — `AgentSkillsSource`

Skills do not have to come from your `Skills/` folder or from a `[MentorSkill]` class. Register any
Agent Framework `AgentSkillsSource` and what it yields reaches the assistant through the *same*
`load_skill` / `read_skill_resource` tools, the same catalogue prompt and the same gate:

```csharp
options.EnableSkills = true;
options.SkillSources =
[
    // Microsoft's own file source — skills written to the Agent Skills specification
    new AgentFileSkillsSource("/srv/shared-skills"),

    // …or your own: a database, a remote catalogue, a per-tenant store
    new MyDatabaseSkillsSource(connectionString),
];

// Optional: keep only what this deployment can actually run
options.SkillFilter = skill => skill.Frontmatter.Compatibility is null
                            || skill.Frontmatter.Compatibility.Contains("v2");

// Optional: fetch a remote catalogue once and share it across sessions, re-fetching it when a session
// starts after 15 minutes. Without it, every new session re-reads the sources when it starts.
options.SkillsRefreshInterval = TimeSpan.FromMinutes(15);
```

The list is composed with the framework's own decorators — `AggregatingAgentSkillsSource` preserves
your order, `FilteringAgentSkillsSource` applies `SkillFilter`, `DeduplicatingAgentSkillsSource`
keeps the first occurrence of a name, and `CachingAgentSkillsSource` is added when you set a
refresh interval. With the interval, that composition is held once per process and shared by every
session; a session keeps the list it started with, so a refresh reaches sessions built after it.

> **Your own skills always win a name collision.** Sources are consulted *after* MentorAgent's own
> discovery, and a duplicate name is skipped with a warning naming it. A source can add a
> capability; it cannot silently replace one of yours.

> **`AgentFileSkillsSource` reads a different dialect, and that is why it did not replace ours.**
> The framework's source validates each `SKILL.md` for **YAML frontmatter**; MentorAgent's
> convention is a heading followed by a prose paragraph, with frontmatter before the heading
> ignored. Both work — keep `SkillsFolder` for yours and register the framework's source for
> specification-compliant ones.

> **Requires a model.** The framework's `AgentSkillsSourceContext` demands an agent, and skills are
> discovered before the coordinator exists — so MentorAgent uses `Agent` when you supplied one and
> otherwise builds a plain agent over `ChatClient`. With neither set, registered sources are skipped
> with a warning and your own skills are unaffected.

---

## Contextual memory

Enable the Mentor's ability to remember preferences and past actions across sessions:

```csharp
options.UseMemoryContext  = true;
options.MemoryContextCount = 10; // last N memories injected into the system prompt

// Who a visitor who has not signed in is. The default gives each circuit/connection its own key,
// so one visitor's facts are never recalled for the next and one visitor cannot spend everybody's
// RateLimitPerUser allowance. A single-user application (MAUI, a desktop tool) wants the opposite:
// Shared puts every session on the literal key "anonymous", so with a persistent IMentorMemoryStore
// its memory survives a restart (the default RAM store loses everything on restart, whatever the key).
options.AnonymousIdentity = MentorAnonymousIdentity.PerSession;   // default
```

By default, memories are stored in RAM (`InMemoryMentorMemoryStore`). For real persistence, register your own store **before** `AddMentorAgent()`:

```csharp
// Redis
builder.Services.AddSingleton<IMentorMemoryStore, RedisMemoryStore>();

// EF Core
builder.Services.AddScoped<IMentorMemoryStore, EfCoreMemoryStore>();

// MongoDB
builder.Services.AddSingleton<IMentorMemoryStore, MongoMemoryStore>();

builder.Services.AddMentorAgent(options => {
	options.UseMemoryContext = true;
	...
});
```

> ⚠️ **User isolation:** With authentication configured, each user has their own memory (keyed by `ClaimTypes.NameIdentifier`, else `sub`, `oid` or the name). Without authentication the key depends on `AnonymousIdentity`. With the default, `PerSession`, every circuit, SignalR connection or app run gets its own opaque key: a visitor's facts are never recalled for anyone else, and they are not recalled on that visitor's next session either. `MentorAnonymousIdentity.Shared` puts every unauthenticated session on the literal key `"anonymous"`. That is right for a single-user app (MAUI, a desktop tool) and a cross-user leak on a website. A user known by name alone (Windows authentication) is keyed `name:<name>` since 1.0.0-rc.15: memories an earlier version stored under the bare name are not found until you rename their key.

### The `IMentorMemoryStore` contract

Five methods, all keyed on `userId` — there is no cross-user query, by design:

| Method | Contract |
|---|---|
| `SaveAsync(userId, key, value, ct)` | Upsert. Called on every captured fact, so make it idempotent on `(userId, key)` |
| `GetAsync(userId, key, ct)` | The value, or `null` when absent. Absence is not an error |
| `GetRecentAsync(userId, count, ct)` | The most recent `count` entries, **newest first**. This is what gets injected into the prompt |
| `DeleteAsync(userId, key, ct)` | Remove one entry. **No built-in tool calls this** — it exists for your own code, e.g. a "forget this preference" control in a settings page |
| `ClearAsync(userId, ct)` | Remove everything for that user. Backs the `forget_all` tool, and is your GDPR erasure hook |

`GetRecentAsync` returns `MemoryEntry` — `record MemoryEntry(string UserId, string Key, string Value, DateTime SavedAt)`.

> It lives in the **`Novior.MentorAgent.Data`** namespace, not `Novior.MentorAgent.Models` where the neighbouring
> types are. Add `using Novior.MentorAgent.Data;` to your implementation file.

A complete EF Core store:

```csharp
using Novior.MentorAgent.Data;      // MemoryEntry
using Novior.MentorAgent.Memory;    // IMentorMemoryStore

public sealed class EfCoreMemoryStore(AppDbContext db) : IMentorMemoryStore
{
    public async Task SaveAsync(string userId, string key, string value, CancellationToken ct = default)
    {
        var row = await db.Memories.FirstOrDefaultAsync(m => m.UserId == userId && m.Key == key, ct);
        if (row is null) db.Memories.Add(new MemoryRow(userId, key, value, DateTime.UtcNow));
        else { row.Value = value; row.SavedAt = DateTime.UtcNow; }
        await db.SaveChangesAsync(ct);
    }

    public async Task<string?> GetAsync(string userId, string key, CancellationToken ct = default)
        => (await db.Memories.FirstOrDefaultAsync(m => m.UserId == userId && m.Key == key, ct))?.Value;

    public async Task<IReadOnlyList<MemoryEntry>> GetRecentAsync(
        string userId, int count = 10, CancellationToken ct = default)
        => await db.Memories
                   .Where(m => m.UserId == userId)
                   .OrderByDescending(m => m.SavedAt)      // newest first — the order matters
                   .Take(count)
                   .Select(m => new MemoryEntry(m.UserId, m.Key, m.Value, m.SavedAt))
                   .ToListAsync(ct);

    public async Task DeleteAsync(string userId, string key, CancellationToken ct = default)
        => await db.Memories.Where(m => m.UserId == userId && m.Key == key).ExecuteDeleteAsync(ct);

    public async Task ClearAsync(string userId, CancellationToken ct = default)
        => await db.Memories.Where(m => m.UserId == userId).ExecuteDeleteAsync(ct);
}
```

Register it **before** `AddMentorAgent()` — registration order is what decides whether your store or
the built-in RAM one wins. Scoped is fine for EF Core; use singleton for Redis or Mongo clients.

### How automatic memory works

When `UseMemoryContext = true`, MentorAgent captures durable facts **reliably** — without depending on the model proactively calling a tool (which weaker models do inconsistently, e.g. saving on *"Mi chiamo Antonio"* but not on *"Ciao, mi chiamo Antonio"*).

- **Path A (a `ChatClient` is configured) — default:** after each user message a dedicated, minimal LLM call (`MemoryAutoCapture`, on by default) extracts durable personal facts and stores them directly. Because it is a separate focused task, it is robust regardless of how the coordinator replies. On this path the now-redundant `remember` tool and its forceful prompt block are **dropped** (fewer tokens per call); `forget_all` stays. Set `options.MemoryAutoCapture = false` to opt out — one fewer model call per message, but facts are then saved less reliably via the `remember` tool.
- **Path B (a pre-built `Agent`):** with a `ClassifierChatClient`, auto-capture runs through it — one small call per message — and the `remember` tool is dropped, as on Path A. Without one, auto-capture cannot run and the `remember` tool is the writer: its description asks the model to call it (the prompt block is Path A's; on Path B the agent's instructions are yours).

Examples of what gets saved automatically:

| User says | Saved as |
|---|---|
| `"My name is Antonio"` | `user_name = Antonio` |
| `"I work in the sales team"` | `user_team = sales team` |
| `"Always show me Pending orders first"` | `preferred_filter = Pending` |

Verify in the logs at **Debug** level (e.g. `"Logging": { "LogLevel": { "Novior.MentorAgent": "Debug" } }`): `[MentorAgent:Memory] Auto-capture saved 1 fact(s): user_name`. A failed extraction is logged as a warning (`[MentorAgent:Memory] Auto-capture failed — skipped.`) and never breaks the turn.

At the start of each session, stored memories are injected into the prompt so the AI greets the user by name and honours preferences immediately. With `MemoryRelevanceFiltering` (requires `EmbeddingGenerator`) only the memories **semantically** relevant to the current message are injected — identity/preference facts always kept.

### `InMemoryMentorMemoryStore` — production limitations

The default store has two hard limitations:
- **Data is lost on app restart** — memories do not survive deployments.
- **Does not scale across multiple instances** — in a load-balanced environment each server has its own isolated dictionary.

For any production deployment with more than one server instance, or where persistence across restarts is required, register a custom `IMentorMemoryStore` implementation.

---

## RAG — Retrieval-Augmented Generation

RAG enriches every AI response with documents retrieved from your vector store. Before the LLM call, MentorAgent searches for the most relevant documents and injects them into the coordinator's system prompt — grounding the AI's answers in your actual data.

### Setup

**Step 1** — Register your RAG source **before** `AddMentorAgent()`:

```csharp
// Implement IMentorRagSource with your preferred vector DB
builder.Services.AddScoped<IMentorRagSource, MyVectorDbRagSource>();

// Register exactly ONE implementation. IMentorRagSource is resolved as a single service,
// so with several registrations the last one wins. Alternatives:
// Azure AI Search
// builder.Services.AddScoped<IMentorRagSource, AzureSearchRagSource>();

// Qdrant
// builder.Services.AddScoped<IMentorRagSource, QdrantRagSource>();

// Any custom implementation
// builder.Services.AddScoped<IMentorRagSource, MyCustomRagSource>();
```

**Step 2** — Enable RAG in options:

```csharp
builder.Services.AddMentorAgent(options =>
{
	options.UseRag                 = true;
	options.RagResultCount         = 5;    // number of documents to inject
	options.RagMinScore            = 0.5f; // optional: overrides the source's DefaultMinScore (see below)
	options.RagSystemPromptTemplate = "Use the following documents to answer:\n{documents}";
	options.ShowRagSources         = true; // show citation chips below AI messages
});
```

### Implement `IMentorRagSource`

```csharp
public class MyVectorDbRagSource : IMentorRagSource
{
	private readonly MyVectorDb _db;
	public MyVectorDbRagSource(MyVectorDb db) => _db = db;

	// Cosine similarity is in [0, 1]: declare a threshold on that scale (0.5 loose … 0.75 strict).
	// Without it the RagMinScore default, 2, suits keyword scores and discards every document here.
	public float? DefaultMinScore => 0.6f;

	public async Task<IReadOnlyList<MentorRagResult>> SearchAsync(
		string query, int maxResults, CancellationToken ct = default)
	{
		var hits = await _db.SearchAsync(query, maxResults, ct);
		return hits.Select(h => new MentorRagResult(
			Content:   h.Text,
			SourceUrl: h.Url,
			Title:     h.Title,
			Score:     h.Score)).ToList();
	}
}
```

**Which threshold applies:** `RagMinScore` when you set it, in code or in configuration; otherwise the source's `DefaultMinScore`; otherwise `RagMinScore`'s default, `2`, which suits keyword sources whose scores are integer-like. A source with scores in [0, 1] that declares nothing has every document discarded, and a warning says so once, with the highest score it saw and where the threshold came from.

### Who is asking, and what the documents say about themselves

MentorAgent calls `SearchAsync(MentorRagRequest request, CancellationToken ct)`. Its default implementation calls the `(query, maxResults)` overload above, so a source written for that one needs no change. Implement it when the search depends on more than the text:

| `MentorRagRequest` | What it holds |
|---|---|
| `Query`, `MaxResults` | The user's message and `RagResultCount` |
| `RecentMessages` | The conversation before this message, oldest first: the user's messages and the assistant's replies of the last three turns of **this** conversation, text only. Empty on the first turn, and it starts again after a reset or a restore. Over SSE every `/mentor/chat` request is a conversation of its own, so it is always empty there |
| `User` | The caller of the hub, of `/mentor/chat` or of an A2A request (Novior.MentorAgent.Server), and in a Blazor circuit the user the host's `AuthenticationStateProvider` reports. `null` when the host has no authentication at all; an anonymous visitor, or a peer agent that did not authenticate, has an unauthenticated principal. Filter restricted documents on it |
| `PageName`, `PageData` | What the current page set with `IMentorPageContext.SetPageName` and `Set` |

Each result can carry `Metadata`. The model sees it under the document's title, one `key: value` per entry, so it can tell the 2025 price list from the 2026 one. It does not stay with the model: it travels to the client with the citation chips (`metadata` in `RagSourcesReady`), and the model may repeat it in its answer. Put nothing in it that the user should not see.

```csharp
public async Task<IReadOnlyList<MentorRagResult>> SearchAsync(
	MentorRagRequest request, CancellationToken ct = default)
{
	var hits = await _db.SearchAsync(request.Query, request.MaxResults, VisibleTo(request.User), ct);
	return hits.Select(h => new MentorRagResult(h.Text, h.Url, h.Title, h.Score)
	{
		Metadata = new Dictionary<string, string> { ["valid from"] = h.ValidFrom.ToString("yyyy-MM-dd") },
	}).ToList();
}
```

The `(query, maxResults)` overload stays part of the interface, so a source that implements the request overload still implements that one too. Do not make each call the other: the search would never return.

### Reusing the turn's embedding — `IMentorQueryEmbedding`

Routing, tool filtering and memory relevance already embed the current message once per turn. If your source searches by vector, ask for that vector instead of embedding the query again. The turn then makes one embedding round trip instead of two:

```csharp
using Novior.MentorAgent.Abstractions.Models;
using Novior.MentorAgent.Rag;
using Microsoft.Extensions.AI;

public sealed class MyVectorRagSource(
	IMentorQueryEmbedding queryEmbedding,
	IEmbeddingGenerator<string, Embedding<float>> embeddings,
	MyVectorDb db) : IMentorRagSource
{
	public async Task<IReadOnlyList<MentorRagResult>> SearchAsync(
		string query, int maxResults, CancellationToken ct = default)
	{
		// Free when something already embedded this message; computed with `embeddings` otherwise.
		var vector = await queryEmbedding.GetAsync(query, embeddings, ct);
		var hits   = await db.SearchAsync(vector, maxResults, ct);
		return hits.Select(h => new MentorRagResult(
			Content:   h.Text,
			SourceUrl: h.Url,
			Title:     h.Title,
			Score:     h.Score)).ToList();
	}
}
```

`IMentorQueryEmbedding` is registered (scoped) by `AddMentorAgent()`, and an empty text returns an empty vector without calling out.

### RAG source citations in the widget

When `ShowRagSources = true`, citation chips appear below each AI message:

```
[AI response]
──────────────────────
📄 Product Manual v2  ↗
📄 Support FAQ        ↗
```

Chips are shown only for the documents the answer actually **cites**, not everything the search returned. MentorAgent numbers the injected documents and appends an instruction, in the configured `Language`, to cite them inline as `[1]`, `[2]`, … It adds this after your `RagSystemPromptTemplate`, so a custom template keeps it. When the reply is complete, each valid marker — `[1]`, a list such as `[1, 2]`, or a range such as `[1-3]` — becomes a chip for each document it names, in the order the answer cites them and once per document, linking to that document's `SourceUrl` and labelled with its `Title` (or the URL when there is no title). A number that names no document cites nothing, and neither does a range that ends on one. An answer that cites nothing, for example one from a skill or a tool, shows no chips, even when the search returned documents. With more than 3 cited sources, a "**+N more**" button collapses the rest.

### Architecture note

RAG is applied **only at the coordinator level**, not on L2/L3 specialist agents. The coordinator performs the vector search once per user message and receives the documents as per-call instructions. They are not written into the conversation. A delegated agent receives only the request text the coordinator passes to `route_to_specialist` (or to a team tool), so a specialist does **not** see the retrieved documents. If one needs your knowledge base, give it a tool that searches it. This avoids redundant searches and keeps costs low.

### RAG configuration options

| Option | Default | Description |
|---|---|---|
| `UseRag` | `false` | Enables RAG. Requires a registered `IMentorRagSource` |
| `RagResultCount` | `5` | Number of documents retrieved per query |
| `RagMinScore` | `2` | Minimum relevance score a document must reach to be injected into the prompt. Documents below this threshold are discarded. Scale depends on the `IMentorRagSource` implementation: for keyword search, `2` ≈ two content matches or one title match; for vector/cosine similarity, typical values are `0.5`–`0.75`. When you do not set it, the source's `DefaultMinScore` applies if it declares one. Set to `0` to disable filtering |
| `RagSystemPromptTemplate` | `"Use the following documents to answer:\n{documents}"` | Template injected into the system prompt. Use `{documents}` as placeholder |
| `ShowRagSources` | `false` | Show citation chips below AI messages in the widget |

> RAG is fully semantic: the vector search embeds every message and `RagMinScore` discards anything below the threshold, so a pure command like *"update the price of X"* simply retrieves nothing relevant and injects nothing — no keyword pre-gate needed, as long as `RagMinScore` is on your source's scale (see *Which threshold applies* above).
>
> The other side of it: the search runs on **every** message, before the model is called. Each message is one `SearchAsync` on your `IMentorRagSource`, with what it costs — an embedding call, the search, a reranker if your source has one — added to the time of every reply, commands included.

---

## MCP — Model Context Protocol

MentorAgent supports MCP in both directions: as a **client** (consuming tools from external MCP servers) and as a **server** (exposing `[MentorAction]` methods to any MCP-compatible client).

### MCP Client — consuming external MCP servers

External MCP servers (filesystem, databases, APIs, custom tools) become additional **Level-1 tools** for the coordinator — indistinguishable from local `[MentorAction]` methods.

#### HTTP transport (remote server)

```csharp
builder.Services.AddMentorAgent(options =>
{
	options.McpServers = [
		new MentorMcpServer
		{
			Name      = "MyApiTools",
			ServerUrl = "https://mcp.example.com/mcp",
		}
	];
});
```

#### stdio transport (local process)

> **Windows note**: on Windows, `npx`, `uvx`, `python`, and other script launchers are `.cmd` or shell scripts that cannot be started directly by .NET's `Process.Start`. MentorAgent detects this automatically and wraps the command as `cmd.exe /c <command> <args>` — no changes needed in your configuration.

```csharp
options.McpServers = [
	new MentorMcpServer
	{
		Name      = "filesystem",
		Command   = "npx",
		Arguments = ["-y", "@modelcontextprotocol/server-filesystem", "/tmp"],
		AllowedTools         = ["read_file", "list_directory"], // null or empty = all tools
		RequiresConfirmation = true, // shows confirmation banner for every call

		// One child process for the whole application instead of one per visitor. Leave it unset
		// unless you know the server is stateless: a local MCP server can hold state for the person
		// who started it (@modelcontextprotocol/server-memory is a knowledge graph), and sharing
		// that would put every visitor in the same store. Servers reached over ServerUrl are shared
		// by default, because a remote endpoint is shared anyway.
		Shared = false,
	},
	new MentorMcpServer
	{
		Name      = "database",
		Command   = "my-db-mcp-server",
		Arguments = ["--connection-string", "Server=..."],
		EnvironmentVariables = new Dictionary<string, string>
		{
			["DB_PASS"] = builder.Configuration["DbPassword"]!
		}
	}
];
```

#### MCP status badge in the widget

When `ShowMcpStatus = true`, an MCP pill appears in the widget header. It shows the server's name when there is one server, or `online/total` when there are several, with a coloured dot for connecting / all online / some online / offline. Clicking it opens a detail bar that lists each server as connecting, online or offline.

```csharp
options.ShowMcpStatus = true; // default: false — recommended for development
```

**`MentorMcpServer` properties:**

| Property | Description |
|---|---|
| `Name` | Display name for the server |
| `ServerUrl` | HTTP/SSE endpoint URL (HTTP transport) |
| `Command` | Executable to launch (stdio transport, e.g. `"npx"`) |
| `Arguments` | Command-line arguments for the process |
| `EnvironmentVariables` | Environment variables injected into the process |
| `AllowedTools` | Whitelist of tool names to expose, compared without regard to case. `null` or an empty list = expose all |
| `RequiresConfirmation` | If `true`, every call to a tool from this server shows a confirmation banner |

---

### MCP Server — exposing MentorAgent as an MCP server

Every `[MentorAction]` method discovered by MentorAgent can be exposed as an **MCP tool**, allowing any MCP-compatible client (Claude Desktop, VS Code Copilot, custom agents) to call your application's business logic directly.

The MCP server is in the **`Novior.MentorAgent.Server`** package (`dotnet add package Novior.MentorAgent.Server`), also for a Blazor Server app: it needs ASP.NET Core, which `Novior.MentorAgent` itself does not reference, so that a MAUI app builds for every target. Up to 1.0.0-rc.14 it came with `MentorAgent` and `AddMentorAgent` registered it.

**Step 1** — Enable the MCP server in options, and register it:

```csharp
builder.Services.AddMentorAgent(options =>
{
	options.McpServerEnabled = true;
	options.AppName          = "MyApp"; // becomes the MCP server name
});
builder.Services.AddMentorAgentMcp();   // after AddMentorAgent — AddMentorAgentServer() already includes it
```

**Step 2** — Map the MCP endpoint in `Program.cs`:

```csharp
app.MapMentorAgentMcp();          // maps at options.McpServerPath (default: /mcp)
app.MapMentorAgentMcp("/my-mcp"); // custom path — a path passed here wins over McpServerPath
```

MCP clients can now connect to `https://yourapp/mcp` (or your `McpServerPath`) and discover all `[MentorAction]` tools.

The endpoint is **open by default**: anyone who can reach the port can list and call every published tool. Gated ones are withheld (see Step 3). To require authentication, pass `configure`, which is applied to the mapped endpoint:

```csharp
app.MapMentorAgentMcp(configure: e => e.RequireAuthorization());
```

Requiring authorization decides who may connect. Which role-gated actions an authenticated caller may see is still decided by `McpCallerPrincipal` (Step 3).

Every `tools/call` goes through the same gates as a tool the model calls (BUG-107): `OnToolResult` runs on the result before the caller sees it — a hook that throws withholds it, and the caller gets an `isError` result — the call counts in the dashboard's top actions, and `RateLimitPerUser` bounds it in an allowance of its own, separate from chat messages. The caller is the principal `McpCallerPrincipal` resolves, else the request's user, counted by its `NameIdentifier`, `sub` or `oid` claim (else its name). A caller with none of them is counted by its remote address when the host registers `IHttpContextAccessor` (`builder.Services.AddHttpContextAccessor()`; behind a proxy, apply forwarded headers or every caller is the proxy); otherwise all such callers share one allowance, and one busy client can use it up for the others. Each call writes one Information line — tool, outcome, time, and a fingerprint of the caller, never the id itself.

**CORS.** The endpoint carries **no CORS policy**, and MCP clients need none: desktop and IDE clients, and the MCP Inspector's proxy, are not browsers. Steps 1 and 2 are all a host needs. Until rc.13 the endpoint carried a policy that allowed any origin, and on a pipeline without `app.UseCors()` every request failed with a 500 (BUG-108).

For a **browser-based** MCP client, opt in: call `app.UseCors()` after `UseRouting()` and before `UseAuthorization()`, apply the `MentorAgentMcp` policy that `AddMentorAgentMcp()` registers, and define that policy yourself — the one MentorAgent registers allows any origin, and it registers it only when you have not — with your origins and the session header exposed. Before or after `AddMentorAgentMcp()`, either works:

```csharp
builder.Services.AddCors(o => o.AddPolicy("MentorAgentMcp",
    p => p.WithOrigins("https://tools.example.com").AllowAnyHeader().AllowAnyMethod()
          .WithExposedHeaders("Mcp-Session-Id")));
// ...
app.UseCors();
app.MapMentorAgentMcp(configure: e => e.RequireCors("MentorAgentMcp"));
```

**Step 3 (optional)** — say **who** is calling, so role-gated actions can be published to callers
entitled to them.

By default nothing an author protected is published at all: an MCP request has no signed-in user to
check `RequiredRoles` against, so a gated action is simply withheld. That is the safe default and it
stays the default. If your host can genuinely identify the caller — an mTLS subject, a validated
bearer token, a gateway header you trust — give MentorAgent that principal:

```csharp
builder.Services.AddHttpContextAccessor();

builder.Services.AddMentorAgent(options =>
{
    options.McpServerEnabled = true;
});

// Resolves the caller behind an MCP request. A [MentorAction(RequiredRoles = ["Admin"])] is then
// published — and published ONLY — to a principal that is authenticated and holds it.
builder.Services.AddOptions<MentorOptions>().Configure<IHttpContextAccessor>(
    (options, http) => options.McpCallerPrincipal = () => http.HttpContext?.User);
```

Roles are tested with `ClaimsPrincipal.IsInRole`, which reads the claim type the identity names as its
`RoleClaimType`, so a principal whose roles are in a `roles` claim works as well as one using
`ClaimTypes.Role` — once its identity says so. Microsoft.Identity.Web does; with JwtBearer and
`MapInboundClaims = false`, set `TokenValidationParameters.RoleClaimType = "roles"`, or `IsInRole` looks
for `ClaimTypes.Role` and every role-gated action stays withheld.
The resolver is called once per MCP request and its answer is never cached per caller: `tools/list`
and `tools/call` are decided for the caller of that request (BUG-103).

| Situation | Result |
|---|---|
| No `McpCallerPrincipal` (the default) | every gated action withheld |
| Principal holds one of the action's `RequiredRoles` (`IsInRole`) | published |
| Principal authenticated but lacks the role | withheld |
| Resolver returns `null`, an unauthenticated principal, or throws | withheld |
| Action needs a **confirmation** (`RequiresConfirmation` or `RequiresApproval`) | **withheld, always** |

> The last row is the one to internalise. A role can be checked against a principal; a confirmation
> cannot be answered by one — there is no dialog on the far end of an MCP call and nobody watching
> it. This is an identity, not an override.

> ℹ️ The MCP server resolves each `[MentorAction]` class from a single DI scope that lives as long as the application. It does so once per process: the tools are built once, and which of them a caller sees is decided per request. The instance is then reused for every call from every MCP client. Whatever lifetime you register (Scoped, Transient or Singleton), the instance behaves as a long-lived shared object on this surface. Keep action classes stateless and thread-safe. Do not inject a `DbContext` directly: inject `IDbContextFactory<TContext>` (or `IServiceScopeFactory`) and create one per call.

---

## A2A — Agent-to-Agent

MentorAgent supports the **Agent-to-Agent (A2A) protocol** in both directions: as a **consumer** (calling remote A2A agents) and as a **server** (exposing MentorAgent as a federatable agent).

### A2A Consumer — calling remote A2A agents

Remote A2A agents participate in the **Handoff workflow** exactly like local `[MentorAgent]` classes. The coordinator can hand off to them; they return results to the coordinator when done. This lets you federate specialized agents deployed as separate services.

```csharp
builder.Services.AddMentorAgent(options =>
{
	options.RemoteAgents = [
		new MentorRemoteAgent
		{
			Name         = "InventoryAgent",
			Description  = "Manages warehouse stock and inventory levels",
			AgentCardUrl = "https://inventory.example.com",  // base URL only — SDK auto-appends /.well-known/agent-card.json
		},
		new MentorRemoteAgent
		{
			Name         = "BillingAgent",
			Description  = "Handles invoicing and payment processing",
			AgentCardUrl = "https://billing.example.com",    // base URL only
			Headers      = new Dictionary<string, string>
			{
				["Authorization"] = $"Bearer {builder.Configuration["BillingApiKey"]}"
			}
		}
	];
});
```

MentorAgent automatically resolves each agent's **Agent Card** (`/.well-known/agent-card.json`) when the first coordinator is built. That is the first message, or application start with `WarmUpAtStartup = true`. It then establishes an A2A connection and adds the agent to the Handoff graph. Cards are cached once per process (15 minutes). A peer that cannot be reached is logged as a warning and is not retried for a minute; the backoff doubles on each failure, up to 5 minutes. So it is dialled, and reported, at most once per window, not once per visitor. Until then it is simply absent from new sessions' workflows. Remote agents require Path A (a `ChatClient`). The coordinator's system prompt is automatically enriched with each remote agent's name and description, so the AI knows when to delegate. The coordinator can then delegate requests to remote agents using natural language — no extra configuration needed.

**`MentorRemoteAgent` properties:**

| Property | Description |
|---|---|
| `Name` | Display name used in the Handoff graph and in the coordinator's system prompt |
| `Description` | Human-readable description of what this agent does. Injected into the coordinator's system prompt so the AI knows when to route to it |
| `AgentCardUrl` | **Base URL** of the remote agent (e.g. `https://inventory.example.com`). The SDK automatically appends `/.well-known/agent-card.json` — do **NOT** include the path |
| `Headers` | Optional custom HTTP headers (auth tokens, API keys, etc.) injected into all A2A requests to this agent |

**Access control.** A remote agent has no per-agent role gate: any user of the host can reach it through `route_to_specialist`. To restrict it, authorise on the remote side — protect the peer's own `/a2a` endpoint and give its actions roles — or do not configure the agent on hosts whose users may not use it. (`RequiredRoles`, which was never enforced, was removed in 1.0.0-rc.13.)

**Whose answer is it?** On a host with `RemoteAgents`, every delegated answer reaches the coordinator with a note saying where it came from. The note is for the model, not for the user. Without it, a question addressed to a remote agent but answered by a local specialist would be presented as the remote system's data:

| What happened | What the coordinator is told |
|---|---|
| A remote agent answered | the answer is *that system's data, not this application's* |
| Both a remote agent and a local specialist answered | which part is the remote system's data and which is this application's, to be kept apart |
| A local specialist answered and no remote agent was named | *no remote agent was contacted*. If the user meant a remote agent, call `route_to_specialist` once more with `specialist` set to its name (the second call carries the name, so the retry is bounded) |
| `specialist` named a remote agent that never took part | `NOT <Name>'S ANSWER: …`, and a warning is logged: `route_to_specialist: <Name> was asked for and did not take part …` |

"Remote" covers every configured `MentorRemoteAgent`, including one whose card could not be fetched when the session was built. A host without remote agents, and a turn that arrived over A2A, see no note at all (BUG-082).

---

### A2A Server — exposing MentorAgent as an A2A agent

MentorAgent can expose itself as a fully compliant A2A agent, discoverable and callable by any A2A-compatible orchestrator.

The A2A agent is in the **`Novior.MentorAgent.Server`** package (`dotnet add package Novior.MentorAgent.Server`), also for a Blazor Server app, for the same reason as the MCP server above. Up to 1.0.0-rc.14 it came with `MentorAgent` and `AddMentorAgent` registered it. The A2A *client* — `RemoteAgents` — stays in `Novior.MentorAgent`.

**Step 1** — Enable the A2A server in options, and register it:

```csharp
builder.Services.AddMentorAgent(options =>
{
	options.A2AServerEnabled = true;
	options.AppName          = "MyApp";
	options.AppDescription   = "My Blazor AI assistant for order management";
	options.AgentCard        = new AgentCardInfo { Version = "2.0.0" };
});
builder.Services.AddMentorAgentA2A();   // after AddMentorAgent — AddMentorAgentServer() already includes it
```

**Step 2** — Map the A2A endpoints in `Program.cs`:

```csharp
app.MapMentorAgentA2A();          // maps at options.A2AServerPath (default: /a2a)
app.MapMentorAgentA2A("/agent");  // custom path — a path passed here wins over A2AServerPath
```

This registers two endpoints:
- `GET /.well-known/agent-card.json` — **Agent Card**, always at this path whatever the task path is: name, description, version, the provider/icon/documentation fields of `AgentCard`, one `JSONRPC` interface at `A2AServerUrl` (or the bare path when it is unset), the application's **ungated** `[MentorAction]`s of classes registered in DI as skills, one per tool name (actions with `RequiredRoles`, `RequiresConfirmation` or matched by `RequiresApproval` are left out, and so is a name that one of them shares: the card is the same for every caller, and nobody answers a confirmation), the input/output modes (`text/plain`, plus `image/png` in with `EnableImageInput`) and `streaming: true`
- `POST /a2a` (or `A2AServerPath`, or the path you pass) — **A2A task handler** (JSON-RPC binding) that receives messages, routes them through `MentorOrchestrator`, and returns the complete reply when the turn ends

Remote orchestrators can now discover this agent via `https://yourapp/.well-known/agent-card.json` and send A2A tasks to it.

> **Protect the endpoints.** By default nothing is required: `/a2a` runs a full, paid turn for whoever can reach it. `MapMentorAgentA2A` takes a `configure` callback that is applied to **both** endpoints it maps, the task handler and the agent card:
>
> ```csharp
> app.MapMentorAgentA2A(configure: e => e.RequireAuthorization());
> ```
>
> A MentorAgent caller then authenticates through `MentorRemoteAgent.Headers` (e.g. `["Authorization"] = "Bearer …"`). The headers are sent with the card request as well as with every task.
>
> A task runs as the request's user: signed in when the endpoint requires authentication, anonymous otherwise. An anonymous task is keyed by `AnonymousIdentity`. With the default, `PerSession`, each task gets its own key, so `RateLimitPerUser` does not bound a caller across tasks; with `Shared`, every anonymous caller spends one allowance.

> **A request that arrives over A2A is answered here — it is never passed on to another peer.** When a host is both a server and a consumer (`A2AServerEnabled` **and** `RemoteAgents`), a turn served through `/a2a` is *not* offered the host's remote agents: they are left out of its handoff workflow, its prompt and the `route_to_specialist` description, and a Debug line says so. The host's own specialists, declarative agents, teams and tools still serve it. This is what lets two deployments be each other's remote agent without passing one question back and forth forever (BUG-080, found live between two samples that do exactly that). Chaining A → B → C through a MentorAgent host is therefore not supported in 1.0 — point A at C directly.

> **A request served over A2A answers from tools, or says it cannot.** The caller is a program: it cannot tell a looked-up figure from an invented one. So a turn served through `/a2a` is told to call the tool *first* and to state only what a tool returned in that turn. If it ends without calling any tool that returns data — a navigation, a UI action, a memory write and a skill do not count — the reply is discarded and the same request is put once more with a tool call **required**; if that attempt too returns no data and the classifier model judges that the reply states something about the application's records (a value, or that an entry does not exist or has no such value), the caller receives `NOT GROUNDED: …` instead. A reply that states no data — "this application cannot provide it", a policy read from a skill or your documents, even one with numbers in it — is returned as it is. Two attempts at most; the extra turn is paid only by requests answered without data (BUG-081, BUG-106). A MentorAgent caller also sends the name *it* has for this application as message metadata (`mentoragent.addressedAs`), so "how many products does InventoryAgent have?" is understood as a question about *this* application; only a single-token name is accepted from the wire (BUG-081).

> ⚠️ **Set `A2AServerUrl`** when other A2A clients will call this agent. Set it to the full public URL of your A2A endpoint **including the path** (e.g. `http://localhost:5001/a2a`, or `…/agent` if you mapped it there): the card publishes it verbatim, so a base URL without the path sends callers to the wrong endpoint. Wit