# Affordance

**A browser for models.** A web browser renders the internet's state into pixels for a person.
Affordance renders the world's state into tokens for a model.

An app is written in TSX, like a web page. It renders its state (a task, a shell's output,
notes, messages from other agents) into the exact token IDs the model reads. The actions still
visible after layout (`<aff>`) are the model's tools. A reply picks one; its handler changes the
state; the next render shows the result. The app owns its loop, its tools and its context policy;
Affordance owns rendering, layout, effects and replay.

```tsx
export default function Hello({name = "world"}) {
  return <box>
    <span label="greeting">{`Hello, ${name}!`}</span>
    <aff name="greet" onGreet={({name}) => ({name})}>{" [greet]"}</aff>
  </box>;
}
```

## What it gives you

- **Exact token IDs.** A render is the token sequence the model sees, with the chat template
  applied by a TSX template app. For 740 models it matches the official template's IDs
  (`affordance check` compares every case and prints the first divergence), and
  [one command adds a model](docs/ADDING_A_MODEL.md) that is not among them.
- **Images, audio and video.** `<img>`, `<audio>` and `<video>` put a model's placeholder tokens
  in the prompt and send the file with the request, to SGLang or to a chat endpoint such as
  vLLM's.
- **Layout for a token budget.** Token style sheets bound boxes, drop old history in steps and
  elide old tool results, so a long session stays inside the window and its prompt prefix stays
  stable for the server's cache.
- **Deterministic replay.** Each agent's inputs are journaled. Replaying a journal rebuilds the
  agent exactly: restore after a crash, or step through a run turn by turn. A command that was
  still running when the process died is sent again on restore, so a tool that writes to the
  outside world should be safe to repeat.
- **Stateful agents.** Many agents in one process, each an event loop with timers, child
  instances, messages, machines to run commands on, and model calls it makes when its code
  decides to.

Affordance is not React, Node or a prompt builder. TSX is a documented subset interpreted in
Rust; there is no npm resolver. See [public contracts and known limits](spec/CONTRACTS.md).

## Try it

Install the `affordance` command:

```sh
cargo install affordance
```

Or run it without installing anything, with [uv](https://docs.astral.sh/uv/) (Python's package
runner): put `uvx` in front of each `affordance` command below, as in `uvx affordance render`.

Save the app above as `hello.tsx` and render it. This needs no model:

```sh
echo '{"name":"world"}' | affordance render hello.tsx --state -
```

```text
ids     [15496, 11, 995, 0, 685, 70, 2871, 60]
text    Hello, world! [greet]
span        0..4     label      greeting
span        4..8     affordance greet
span        4..8     action     greet(name)
span        0..8     box
```

The first four token IDs are the greeting and the last four are ` [greet]`. The spans say what
each range is: IDs 4 to 8 are the `greet` action, which the model can call as a tool with a
`name`. With no `--tokenizer`, `render` uses GPT-2's.

Then write and run a first agent, against a local model server (llama.cpp, Ollama or vLLM) or a
hosted API, with a shell on your machine:

```sh
affordance init my-agent && cd my-agent
affordance run                      # runs affordance.yaml here; journals go to .affordance/
affordance run --restore             # continue it
affordance run --set model.url=http://127.0.0.1:11434/v1   # another server, for one run
```

The agent `init` wrote is one file. The page is the task, the tools and the log of what the model
saw and did; the loop is a library hook you can read and replace:

```tsx
export default function Main({ task }) {
  const log = useLog();
  useLoop(log); // ask the model, run its calls, repeat
  const { shell } = machineTools(harness.machine.get("home"));
  /** Give your final answer. This ends the task. */
  function answer({ text }: { text: string }) {
    harness.stop({ answer: text });
    return "done";
  }
  return <ModelContext strategy="unrolled" log={[{ kind: "input", content: task }, ...log.records]}>
    <Tool fn={shell}>{"[shell] "}</Tool>
    <Tool fn={answer}>{"[answer]\n"}</Tool>
  </ModelContext>;
}
```

The other examples are in this repository:

```sh
git clone https://github.com/approximatelabs/affordance && cd affordance
```

Serve an app over HTTP. [`views/demo/memory_server`](views/demo/memory_server) puts a chat
model with a memory longer than its context behind an OpenAI-compatible endpoint:

```sh
affordance serve views/demo/memory_server   # then point any OpenAI client at http://127.0.0.1:8000/v1
```

Or drive one from a frontend over stdio. [`views/demo/host`](views/demo/host) is a coding chat that
streams its replies, asks before each command, and stops a turn on Escape (`{"type":"abort"}`):

```sh
affordance host views/demo/host   # JSON lines: {"type":"event","name":"user","payload":{"text":"..."}} in; deltas, output, questions out
```

[Getting started](docs/GETTING_STARTED.md) walks through it; [examples](examples/README.md) has more.

## Learn more

- [Writing and running agents](docs/RUNTIME.md)
- [The language and layout](spec/LANGUAGE.md)
- [Instances, effects, storage and replay](spec/HARNESS.md)
- [Model bindings](docs/MODEL_BINDINGS.md)
- [Conversation and context libraries](docs/MIDDLE_LAYER.md)
- [Pictures, sound and video](docs/MEDIA.md)
- [Fetch, HTTP and MCP](docs/HTTP_AND_MCP.md)
- [Embedding the engine in Rust](docs/HARNESS_GUIDE.md)
- [Why it is shaped like a browser](docs/DESIGN.md): where the line between engine and app is, and why
- [Architecture](docs/ARCHITECTURE.md), [development](docs/DEVELOPING.md) and
  [contributing](CONTRIBUTING.md)

## Status

v0.2 beta. Developed on Linux; macOS support is new and less exercised
([platform evidence](docs/DEVELOPING.md#current-platform-evidence)).
Template conformance is evidence from a finite test corpus, not a guarantee for arbitrary input.

## License

Affordance's own code is licensed under [Apache-2.0](LICENSE).

The files under [`views/third_party/`](views/third_party) are different. Each is a model
publisher's chat template, converted so that prompts for that model come out in its format, or
prose that a template carries (a default system message, a tool-call instruction). They are
included for interoperability and stay under their publishers' terms, which are not all
Apache-2.0: some are non-commercial, some are for research, and one is not stated. Every
folder has a `NOTICE.md` that names the model, the revision the text was read at and its
license. A publisher who wants a template removed can open an issue and it will be removed.

Code ported from other projects is listed in [third-party notices](THIRD_PARTY_NOTICES.md).
