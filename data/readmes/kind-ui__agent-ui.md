<div align="center">

# Agent UI

AI interface components that people and agents can both use, for React and Web Components, built on [UI SDK](https://ui-sdk.dev/docs).

[![npm version](https://img.shields.io/npm/v/@kind-ui/agent-ui?color=0368FF&label=npm)](https://www.npmjs.com/package/@kind-ui/agent-ui)
[![npm downloads](https://img.shields.io/npm/dm/@kind-ui/agent-ui)](https://www.npmjs.com/package/@kind-ui/agent-ui)
[![CI](https://github.com/kind-ui/agent-ui/actions/workflows/ci.yml/badge.svg?branch=main&event=push)](https://github.com/kind-ui/agent-ui/actions/workflows/ci.yml)
[![npm provenance](https://img.shields.io/badge/npm-provenance-2E7D32?logo=npm)](https://www.npmjs.com/package/@kind-ui/agent-ui#provenance)
[![types](https://img.shields.io/npm/types/@kind-ui/agent-ui)](packages/agent-ui/src/index.ts)
[![license](https://img.shields.io/npm/l/@kind-ui/agent-ui)](LICENSE)

[Docs](https://kindui.dev/docs/agent-ui/) · [Components](#components) · [Showcases](#showcases) · [Changelog](packages/agent-ui/CHANGELOG.md)

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/readme-hero-dark.png">
  <source media="(prefers-color-scheme: light)" srcset="docs/assets/readme-hero-light.png">
  <img alt="A finished agent run from the Agent Activity showcase: a reasoning step, two tool calls with one approved, a completed plan, a subagent's result and a queue of follow-up prompts." src="docs/assets/readme-hero-light.png" width="576">
</picture>

</div>

## Features

- **56 components** for AI chat and agent interfaces: conversations and streaming markdown, the steps an agent takes, the places a person answers it, the output it hands back, and the shell around a chat: its list of past chats, a sidebar and search.
- **React and Web Components.** Every component ships as a React item and a `-web` twin with the same props, states and styles.
- **Built on UI SDK.** Focus, keyboard navigation, popups, dismissal and screen reader announcements come from [UI SDK](https://ui-sdk.dev/docs), not hand-written code.
- **Agent-operable.** An agent connected with UI SDK's `createAgent` reads the same components a person sees and runs their actions, with a person confirming the ones that matter.
- **Built for streaming.** Markdown parses only the blocks that changed, logs follow the newest content until the reader scrolls away, and rows animate in once, when they mount.
- **Yours to edit.** The shadcn CLI copies the styled components into your project. They are Tailwind CSS v4 utilities over `--kind-*` theme tokens, with light and dark from `color-scheme`.
- **AI SDK adapter.** Map AI SDK `UIMessage`s to the components' data with `@kind-ui/agent-ui/adapters/ai-sdk`.

## Quick start

Agent UI needs Tailwind CSS v4, and React 19 for the React components.

Add the `@kind-ui` registry to your `components.json` (run `npx shadcn@latest init` first if you have none):

```json
{
  "registries": {
    "@kind-ui": "https://kindui.dev/r/{name}.json"
  }
}
```

Then add components by name. Each React item has a Web Components twin ending in `-web`:

```bash
npx shadcn@latest add @kind-ui/composer       # React
npx shadcn@latest add @kind-ui/composer-web   # Web Components
```

The first `add` also installs `@kind-ui/agent-ui` and `@ui-sdk/core` at their pinned versions, imports `@kind-ui/agent-ui/styles.css` into your stylesheet, and writes an `AGENTS.md` beside the components for coding agents.

To set it up with a coding agent instead, copy the prompt from [Get Started](https://kindui.dev/docs/agent-ui/#quick-start).

## Usage

### React

```tsx
import { Composer, ComposerInput, ComposerSubmit } from "@/components/ui/composer";

export function Prompt() {
  return (
    <Composer aria-label="Message" onSubmit={(draft) => chat.send(draft.text, draft.attachments)}>
      <ComposerInput aria-label="Prompt" placeholder="Ask anything" />
      <ComposerSubmit />
    </Composer>
  );
}
```

Return a promise from `onSubmit` to keep the composer pending until the message is sent.

### Web Components

Each `-web` item exports a `define…` function that registers its `kind-*` elements. They render into light DOM, so the same stylesheet styles them:

```ts
import { defineStep } from "./components/ui/web/step.js";

defineStep();
```

```html
<kind-step status="complete">
  <kind-step-trigger>
    <button><kind-step-icon></kind-step-icon><kind-step-title>Read the logs</kind-step-title></button>
  </kind-step-trigger>
  <kind-step-content><p>Three timeouts.</p></kind-step-content>
</kind-step>
```

Props are kebab-case attributes or properties, and callbacks are lowercase DOM events. Each component page lists both.

### Agents

Create one UI SDK agent bridge, and every Agent UI component on the page joins it:

```ts
import { createAgent } from "@ui-sdk/react/agent"; // or "@ui-sdk/web/agent"

const agent = createAgent();

agent.snapshot(); // [{ ref: "c1", component: "kind-model-selector", label: "Model", value: "gpt-6.1-sol", actions: ["setValue"] }, …]
await agent.act({ steps: [{ ref: "Model", action: "setValue", args: ["claude-sonnet-5.5"] }] });
```

Each action reaches your callbacks with `details.source` set to `"agent"`. Actions that decide something, like approving a tool call or accepting a plan, wait for a person to confirm unless your `allow` lets them through. Each component page's **Agent** section lists its actions. See UI SDK's [agent docs](https://ui-sdk.dev/docs) for `query`, permissions and WebMCP tools.

### AI SDK

```ts
import { fromUIMessages, toApprovalResponse } from "@kind-ui/agent-ui/adapters/ai-sdk";

const rendered = fromUIMessages(messages, { status, error });
```

`ai` is an optional peer dependency, imported for types only. See the [AI SDK adapter](https://kindui.dev/docs/agent-ui/adapters/ai-sdk/) page.

## Components

### Chat

| Component | Description |
| --- | --- |
| [Conversation](https://kindui.dev/docs/agent-ui/components/conversation/) | A message log that follows new content and offers a jump to the latest, with loading, error and empty states. |
| [Message](https://kindui.dev/docs/agent-ui/components/message/) | A chat message with copy, regenerate, edit and branch controls, a menu of ways to regenerate, its author and time, and Retry or Continue when it failed or stopped. |
| [Markdown](https://kindui.dev/docs/agent-ui/components/markdown/) | Streaming markdown that parses only the blocks that changed. |
| [Code Block](https://kindui.dev/docs/agent-ui/components/code-block/) | A code block with its language, a wrap toggle and a copy button. |
| [Markdown Table](https://kindui.dev/docs/agent-ui/components/markdown-table/) | A table that scrolls sideways instead of squeezing its columns, with a copy button. |
| [Composer](https://kindui.dev/docs/agent-ui/components/composer/) | A prompt input with mentions, commands, attachments, submit and stop, saved drafts, and a layout for narrow screens. |
| [Attachments](https://kindui.dev/docs/agent-ui/components/attachments/) | A removable list of attached files. |
| [Uploader](https://kindui.dev/docs/agent-ui/components/uploader/) | File uploads with progress, cancel and retry. |
| [Loader](https://kindui.dev/docs/agent-ui/components/loader/) | A labeled loading indicator. |
| [Thinking Indicator](https://kindui.dev/docs/agent-ui/components/thinking-indicator/) | Shows that the agent is thinking. |
| [Typing Indicator](https://kindui.dev/docs/agent-ui/components/typing-indicator/) | Shows that the agent is typing. |
| [Streaming Text](https://kindui.dev/docs/agent-ui/components/streaming-text/) | Appended text chunks fading in, with an optional caret. |

### Agent activity

| Component | Description |
| --- | --- |
| [Step](https://kindui.dev/docs/agent-ui/components/step/) | One step of an agent's work, with its status and details. Includes Step List. |
| [Status](https://kindui.dev/docs/agent-ui/components/status/) | Whether an agent is running, waiting, complete or has failed. |
| [Reasoning](https://kindui.dev/docs/agent-ui/components/reasoning/) | The model's reasoning as a step, with its thoughts streamed as markdown. |
| [Tool](https://kindui.dev/docs/agent-ui/components/tool/) | A tool call as a step, from its input to its output or error. |
| [Chain of Thought](https://kindui.dev/docs/agent-ui/components/chain-of-thought/) | A summary of the steps an agent took, with each step's details. |
| [Task](https://kindui.dev/docs/agent-ui/components/task/) | The steps an agent takes for one task, as it takes them. |
| [Plan](https://kindui.dev/docs/agent-ui/components/plan/) | The steps an agent plans to take, with a progress bar and an Accept button. |
| [Subagent](https://kindui.dev/docs/agent-ui/components/subagent/) | A subagent's run: its own steps, a Stop button and its result. |
| [Queue](https://kindui.dev/docs/agent-ui/components/queue/) | The agent's to-do list, queued and completed, that people can reorder and clear. |

### Human input

| Component | Description |
| --- | --- |
| [Confirmation](https://kindui.dev/docs/agent-ui/components/confirmation/) | Approve or deny what the agent wants to do, and keep the decision in view. |
| [Question](https://kindui.dev/docs/agent-ui/components/question/) | Single choice, multiple choice and free text questions in one form. |
| [Checkpoint](https://kindui.dev/docs/agent-ui/components/checkpoint/) | A point in the conversation a person can go back to, after a dialog asks first. |
| [Model Selector](https://kindui.dev/docs/agent-ui/components/model-selector/) | Pick the model that answers, from a button that opens a searchable list grouped by provider. |
| [Reasoning Effort](https://kindui.dev/docs/agent-ui/components/reasoning-effort/) | Choose how hard the model thinks, from a row of levels. |
| [Suggestion](https://kindui.dev/docs/agent-ui/components/suggestion/) | Prompts a person can send in one press. |
| [Context Meter](https://kindui.dev/docs/agent-ui/components/context-meter/) | How full the context window is, with token counts and cost. |
| [Feedback](https://kindui.dev/docs/agent-ui/components/feedback/) | Rate a response and optionally leave a comment. |
| [Notice](https://kindui.dev/docs/agent-ui/components/notice/) | A calm callout for info, success, a warning or an error. |
| [Guardrail Notice](https://kindui.dev/docs/agent-ui/components/guardrail-notice/) | Shows that a guardrail blocked or filtered content, with the policy reason. |

### Developer output

| Component | Description |
| --- | --- |
| [Sources](https://kindui.dev/docs/agent-ui/components/sources/) | The sources a response used, behind a compact count that opens into links. |
| [Inline Citation](https://kindui.dev/docs/agent-ui/components/inline-citation/) | A marker in running text whose card shows the sources it points to. |
| [Document](https://kindui.dev/docs/agent-ui/components/document/) | A document card with its title, kind and size, and an expandable preview. |
| [Generated Image](https://kindui.dev/docs/agent-ui/components/generated-image/) | An image the agent is making, from progress to preview to the full image. |
| [File Tree](https://kindui.dev/docs/agent-ui/components/file-tree/) | Changed files as a folder tree, with each change and its added and removed lines. |
| [Terminal](https://kindui.dev/docs/agent-ui/components/terminal/) | A command and its output in ANSI colors, following the end as it streams. |
| [Stack Trace](https://kindui.dev/docs/agent-ui/components/stack-trace/) | An error the agent hit, with its frames and the library frames folded away. |
| [Test Results](https://kindui.dev/docs/agent-ui/components/test-results/) | A test run's results over a filterable tree of suites. |
| [Transcript](https://kindui.dev/docs/agent-ui/components/transcript/) | Speaker-labelled, timed segments with search and playback seeking. |
| [Selection](https://kindui.dev/docs/agent-ui/components/selection/) | A small toolbar of actions above text a person selects in a reply. |
| [Action](https://kindui.dev/docs/agent-ui/components/action/) | An action run on selected text, shown as a step. |

### Composer controls

| Component | Description |
| --- | --- |
| [Picker](https://kindui.dev/docs/agent-ui/components/picker/) | A button that opens a searchable list of choices, with groups, two-line rows, pages and footer actions. |
| [Add Menu](https://kindui.dev/docs/agent-ui/components/add-menu/) | A plus button that opens a menu of what can be added, with icons, descriptions, groups and submenus. |
| [Settings Menu](https://kindui.dev/docs/agent-ui/components/settings-menu/) | A menu of settings: toggles drawn as switches, and choices in submenus showing their value. |
| [Approval Mode](https://kindui.dev/docs/agent-ui/components/approval-mode/) | How much the agent may do without asking, chosen from a menu with the risky mode marked. |
| [Model Control](https://kindui.dev/docs/agent-ui/components/model-control/) | The model and its effort in one button, with Model and Effort submenus. |
| [Context Bar](https://kindui.dev/docs/agent-ui/components/context-bar/) | Removable context chips, the ones that don't fit behind a +N button that lists them. |
| [Dictation](https://kindui.dev/docs/agent-ui/components/dictation/) | A mic button that turns speech into text through a source the host chooses, with a live waveform. |

### Thread & shell

| Component | Description |
| --- | --- |
| [Thread List](https://kindui.dev/docs/agent-ui/components/thread-list/) | Past chats grouped by date, to open, rename, pin, share or delete. |
| [Thread Search](https://kindui.dev/docs/agent-ui/components/thread-search/) | A search dialog over past chats, grouped like the list, with New chat. |
| [Sidebar](https://kindui.dev/docs/agent-ui/components/sidebar/) | A panel beside the page that people resize and collapse, and a drawer on narrow screens. |
| [Day Separator](https://kindui.dev/docs/agent-ui/components/day-separator/) | A heading where a new day starts in a conversation, reading Today or Yesterday. |
| [Connection Status](https://kindui.dev/docs/agent-ui/components/connection-status/) | A pill over the conversation while the connection drops, comes back or resumes a stream. |
| [Share Dialog](https://kindui.dev/docs/agent-ui/components/share-dialog/) | Choose who can open a chat, then create, copy or stop sharing its link. |
| [Conversation Search](https://kindui.dev/docs/agent-ui/components/conversation-search/) | Find text in a conversation's messages, with marks beside the scrollbar. |

## Showcases

Each showcase plays one scripted agent run with several components working together:

- [Agent Activity](https://kindui.dev/docs/agent-ui/showcase/agent-activity/): reasoning, parallel tool calls with an approval, a plan, a subagent and a queue.
- [Human Input](https://kindui.dev/docs/agent-ui/showcase/human-input/): a question, an approval inside a tool call, a checkpoint, notices, feedback and suggestions, with a model selector, reasoning effort and context meter in the composer.
- [Developer Output](https://kindui.dev/docs/agent-ui/showcase/developer-output/): a transcript, terminal output, test results and a stack trace, a file tree, a document, a generated image, cited sources and an action on selected text.

## Packages

The npm package holds the behavior, types and styles the copied components import:

```bash
npm install @kind-ui/agent-ui @ui-sdk/core
```

| Entry | Contents |
| --- | --- |
| `@kind-ui/agent-ui` | Neutral types for messages, parts, steps, tool calls and approvals |
| `@kind-ui/agent-ui/core` | The primitives, the markdown engine and the motion helper |
| `@kind-ui/agent-ui/adapters/ai-sdk` | AI SDK message mapping |
| `@kind-ui/agent-ui/styles.css` | Component styles and theme tokens |

Releases are published from CI with [npm provenance](https://docs.npmjs.com/generating-provenance-statements). The [package README](packages/agent-ui/README.md) covers the theme tokens and the adapter in detail.

## Theming

Set any `--kind-*` token in your own `@theme` or `:root`. Colors are `light-dark()` pairs, so dark mode follows `color-scheme`:

```css
@import "tailwindcss";
@import "@kind-ui/agent-ui/styles.css";

:root {
  color-scheme: light dark;
  --kind-color-accent: var(--color-violet-600);
  --kind-radius: 0.5rem;
}
```

## Repository

| Path | Contents |
| --- | --- |
| [`packages/agent-ui`](packages/agent-ui) | The `@kind-ui/agent-ui` package and the React and Web Components render files |
| [`registry`](registry) | The shadcn registry catalog served at `kindui.dev/r` |
| [`apps/docs`](apps/docs) | The docs site, with every component's page and live example |
| [`tests`](tests) | Browser specs for both layers, fixtures and consumer type tests |
| [`scripts`](scripts) | Checks: UI SDK usage guard, packed package, bundle size, registry consumers |

## Contributing

Requires Node 22.22 (or 24.11) or newer and npm 11.9.

```bash
npm ci
npm run check:fast   # lint, typecheck, script and unit tests
npm run dev:docs     # docs site with every example
```

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md) before you open a pull request. Report vulnerabilities privately as described in [SECURITY.md](SECURITY.md).

## License

[MIT](LICENSE). Third-party notices are in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
