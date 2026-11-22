# pi-durable-prune

Context pruning for [pi-durable](https://github.com/earendil-works/pi/tree/main/packages/durable) agents.

> A library for apps built on pi-durable, used from your own code. It is not a Pi coding-agent extension: `pi install` adds nothing to the `pi` CLI.

![One long chat, request by request: 157k tokens without pruning, 39k with](docs/long-chat.png)

Agents that read things (files, web pages, API responses, database rows) carry every one of those results in the conversation, and re-send them to the model on every later turn. Most of that is stale after the turn that used it. This package replaces large tool results from earlier asks with a short note in what the model reads, and gives the model a tool to read any of them back in full. The originals stay in the transcript untouched.

It is built on pi-durable's own context edits, so it is durable, crash-safe and replay-safe like everything else in the transcript, and it is written so that the provider's prompt cache keeps working.

```
before                                  after prune()
user: find the Q3 numbers               user: find the Q3 numbers
assistant: → read_sheet {"id":"q3"}     assistant: → read_sheet {"id":"q3"}
tool: <48,210 characters of rows>       tool: [Set aside to save room: the read_sheet result
assistant: Revenue was 4.2M…                   for {"id":"q3"}, 48,210 characters. recall_result
user: and Q4?                                  with ref "call_8f2" reads it again in full.]
                                        assistant: Revenue was 4.2M…
                                        user: and Q4?
```

## Install

```sh
npm install pi-durable-prune
```

Peer dependencies: `@earendil-works/pi-durable`, `@earendil-works/pi-ai` and `@earendil-works/chord`, 1.5.2 or later.

## Use

```ts
import { prune, recallTool } from "pi-durable-prune";
import { defineExtension } from "@earendil-works/pi-durable";

// 1. Give the model a way to read a set-aside result back.
registry.install(defineExtension({ name: "prune", tools: [recallTool()] }));

// 2. Before each new input, prune. It returns at once if the conversation is busy.
await prune(harness, conversation, { keep: ["use_skill"] });
await conversation.submit({ type: "input", content: text }, context);
```

That is all. `prune` writes one entry of context edits when there is something to set aside, and nothing otherwise.

### Policy

Every field is optional.

| Field | Default | Meaning |
| --- | --- | --- |
| `minChars` | `2000` | Results shorter than this stay whole. |
| `keepAsks` | `1` | The latest asks (user inputs) whose results stay whole. With `1`, the results of the ask that just finished stay whole until the next ask finishes, so a follow-up question still sees them. |
| `keep` | none | Tool names whose results always stay whole. Use it for results the model keeps following, such as loaded skills or instructions. |
| `note` | `defaultNote` | `({ toolName, args, chars, ref }) => string`, the text a result is replaced with. It must be deterministic. |

Always whole, whatever the policy: error results, and results that carry anything other than text (pictures, for instance).

### Reading results back

`recallTool(options)` returns a tool registration. The model calls it with the ref a note names and gets the original result's text back, read from the transcript as written.

| Option | Default | Meaning |
| --- | --- | --- |
| `name` | `recall_result` | The tool name. If you change it, pass a `note` that names it (`(r) => defaultNote(r, "my_name")`). |
| `description` | built in | What the model is told the tool does. |
| `visible` | everything | `(messages, { api, context }) => messages`, narrowing the transcript to what this caller may read. |
| `notFound` | built in | `(ref) => string`, the reply when no readable result has the ref. |
| `outputLimits` | pi-durable's | Passed through. Recalled results can be large. |

A ref is only a locator, not a permission. If several people share one conversation and should not see each other's tool results, pass `visible` so a recall runs only over what the caller may see:

```ts
recallTool({ visible: (messages) => messages.filter((m) => belongsTo(m, userId)) });
```

### With tool search

If your conversation defers tools behind `tool_search`, install `loadOnCall` too. A `tool_search` result is how the model knows which tools it has loaded. Once that result is set aside, the model can call a related tool by a name it guesses, one it never loaded, and pi-durable answers that the tool is not available. With `loadOnCall`, such a call loads the tool, and the model is told to call it again:

```ts
import { loadOnCall } from "pi-durable-prune";

registry.install(
  defineExtension({
    name: "prune",
    tools: [recallTool()],
    hooks: [loadOnCall({ deferred: deferredToolNames })],
  }),
);
```

`deferred` is the names of your deferred tools, or a test on a name. Calls of any other unknown name get pi-durable's error as before. It also helps a conversation that unloads tools it has not used for a while. `message` changes the reply (default `defaultLoadedMessage`).

### Forks and child conversations

A conversation started from another one cannot recall its parent's refs. Seed it with the originals instead:

```ts
import { withOriginals } from "pi-durable-prune";

const messages = withOriginals(await parent.context(context));
```

### Lower-level pieces

- `pruneEdits(entries, policy)` is the pure part: the edits `prune` would write for a context view's entries. Use it to preview or to write the edits yourself.
- `originalResult(messages, ref)` finds a tool result by ref.
- `transcript(api, context)` reads every committed model message of the calling conversation, as written, from inside a tool.
- `PRUNE_ENTRY_KIND` is the kind of the entry `prune` writes (`context.prune`).

## How it keeps the prompt cache

Providers cache a request's prefix. Anything that changes an early message makes everything after it a cache miss. Pruning changes early messages by design, so it follows three rules to make that cost small and one-off:

1. **Prune at rest, once per ask.** `prune` only writes on a conversation that is idle and whose newest message is an answer the model finished. Within one ask the request only grows, so every turn of that ask hits the cache.
2. **Never rewrite a note.** A result is set aside once. Its note depends only on the result (tool, arguments, size, ref), and a later prune never touches it. So the request stays byte-identical up to the earliest result newly set aside, and that prefix stays cached.
3. **Leave the latest ask whole.** A follow-up question usually needs what was just read, and the recent end of the request is what changes anyway.

The trade-off: the first request after a prune re-writes the cache from the first newly set-aside result onwards. In exchange every later request in that conversation is smaller, read from cache or not. In long conversations that pays back within a turn or two.

### Busy conversations and errors

`prune` never waits. If the conversation has a live task, a queued or placed submission, or its last run ended in an error, an abort, or mid tool call, it returns `0` straight away and writes nothing; the next call picks it up. The write is keyed by the conversation's newest entry, so a retry after a crash finds the first write instead of making a second.

## Measured

We replayed 686 chats from our own development and testing (not production) of a pi-durable agent that reads business apps: mail, spreadsheets, documents, web pages. The policy was `minChars: 2000`, `keepAsks: 1`, with three tools kept whole (loaded skills and knowledge pages). Sizes are estimates: message and system-prompt characters ÷ 4, tool definitions not counted. Each figure is the share of the next request saved.

- **Long chats save a lot.** The three longest saved 75% (28 asks, about 157k → 39k tokens), 63% (25 asks) and 59% (18 asks).
- **Typical chats save a little.** Across the 15 chats with 5 or more asks, the median saving is 22.5%. Five of the 15 save nothing. Overall it is 53%, because the long chats dominate.
- **Short chats save nothing, by design.** Nothing is set aside before the third ask. Most chats are short: of 686 chats, 141 reached a second ask and 44 a third.
- **What gets set aside** is mostly tool search results (44%), web pages read (22%) and web search results (12%).

Your numbers depend on how much your agent reads and how long its conversations run. An agent that mostly talks, or whose conversations are short, will see little change. Long conversations that read large records, files or pages will see the most.

## Limits

- **Compaction can fire once more than it needs to.** pi-durable sizes the next request from the usage the last answer measured, plus estimates of what came after it. That measurement was taken before the prune, so it still counts the results that were just set aside. Near the compaction threshold, the first request after a prune can trigger a compaction it no longer needs. After that request the measurement is fresh again. `scripts/estimate-gap.ts` reproduces it. The fix belongs in pi-durable: a measurement older than an entry with context edits should not be trusted. [`docs/pi-durable-1.5.2-estimate.patch`](docs/pi-durable-1.5.2-estimate.patch) is that change against the published 1.5.2 build, and you can apply it today with `pnpm patch` or `patch-package`. With it applied, the reproduction no longer compacts.
- **Compaction summarizes the notes, not the originals.** A compaction after pruning summarizes what the model reads. The originals are still in the transcript and `recall_result` still finds them by ref, but the summary will not mention their contents.
- **Results are set aside whole or not at all.** There is no truncation to a head and tail, and no summary of the result. The note says what it was and how big; the model calls the recall tool when it needs the details.
- **Only results with a single message entry are considered**, which is every tool result pi-durable writes today.
- **Text only.** Results with pictures or other parts stay whole.

## Development

```sh
pnpm install
pnpm test        # real pi-durable harness on in-memory storage with the faux provider
pnpm typecheck
pnpm build
npx tsx scripts/estimate-gap.ts
```

## License

MIT. Built by [Precision](https://getprecision.ai/?utm_source=pi-durable-prune), which runs pi-durable agents for professional service firms.
