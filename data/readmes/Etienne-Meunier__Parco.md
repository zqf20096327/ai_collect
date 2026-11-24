# Parco

**Write with AI as a reader, not as a ghostwriter.**

Parco is a small, free and open-source tool for writing LaTeX documents alongside an AI, iteratively, with track changes. The AI reads your work and proposes: comments, edits, references. You decide: every proposal is shown in a clean review platform where you accept, reject or discuss it. Nothing touches your `.tex` files until you close the version.

![The Parco review platform: the compiled document with tracked edits on the left, edits and discussion threads on the right](docs/images/review.png)

## Why Parco

I am a researcher and I have always loved writing. Lately it has become frustrating at times, as we feel more and more pressure to use AI tools to write. When I write with an LLM, I lose track of what I wrote and I feel that I lose some control over my own text. Some solutions exist, but they mean paying for yet another subscription. This is why I designed Parco: a free tool that keeps me in charge of my writing while still letting me benefit from an AI reader.

Most AI writing tools push you towards letting the model write. We would like to propose a different approach, where you keep the freedom to formulate your ideas on your own and still enjoy the advantage of a tireless, attentive reader.

We believe that **iterative reading** is central to building an understanding of our own work and making it ours. Writing a paper is a slow construction of thought: you write, someone reads, you revise. Parco brings the AI into that loop as an advisor would come in, and designs a nicer environment to write along with it:

- **You stay the author.** The AI only writes new text where you explicitly ask for it, with a `%parco` tag. Elsewhere it comments, proofreads or finds references, depending on the mode you choose.
- **Track changes, always.** Every proposal is a diff you review: removed text in red, new text in green, word by word, right in a compiled view of your document.
- **Iterate in conversation.** Reply to a comment, ask for a change, push back. The AI answers your threads and attaches edits to them, without opening new subjects.
- **A blank slate at each version.** When you close a version, the AI forgets everything. You stay master of the information it gets at each round, and complications do not pile up across rounds. From the second version on, it reviews only what you changed since the last one.
- **Rules enforced by the program, not by the prompt.** Every action of the AI goes through the `parco` command line, which checks it against the current mode and phase. A drifting model cannot write where it is not allowed to.

Parco is free (MIT license), runs entirely locally, and is easy to use: one `pip install`, one `init` in your LaTeX project, and your usual AI agent.

## How it works

Each version of your document goes through three phases.

![The Parco cycle: the AI reads, you review, the AI iterates on your threads as many times as needed, you close the version, and the next version starts from a blank slate](docs/images/workflow.svg)

1. **Read.** The AI reads the document (or the parts that changed since the last version) in the mode you chose, and submits its edits and comments.
2. **Iterate.** You go through them in the platform: accept, reject, reply, ask for changes. The AI then answers your threads and proposes the edits you asked for. Repeat as many times as you like.
3. **Close.** Accepted edits are written to your sources, pending ones are dropped, all threads are closed and a snapshot is taken. The next version starts fresh.

![An iterate round: you ask for a change in a thread, the AI answers and proposes an edit attached to it](docs/images/iterate.png)

### Four reading modes

Modes go from the lightest to the most active touch, and each one includes everything below it in the pyramid.

![The four modes as a pyramid: reference at the base, then comment, proofread and generative at the top; each mode includes the ones below](docs/images/modes.svg)

### Two tags to guide the AI

- `%parco <instruction>`: a comment line asking the AI to write there, e.g. `%parco explain why the scheme is stable`. Only `generative` mode fills these tags, and the AI never writes new text anywhere else.
- `\cite{parco}`: a placeholder citation that the AI replaces with real references. Every mode can resolve it.

## Install

Parco works with any AI agent able to run shell commands: Claude Code, ChatGPT / Codex, Gemini CLI, Cursor and others. It is not tied to a provider, since all it does is receive edits and comments through its command line and show them to you.

You need:

- Python 3.12 or newer;
- [pandoc](https://pandoc.org/installing.html), used to render the document in the platform;
- optionally `pdftoppm` (from [poppler](https://poppler.freedesktop.org/)) to show PDF figures.

On macOS, `brew install pandoc poppler` covers the external tools. Then install Parco:

```bash
git clone https://github.com/Etienne-Meunier/Parco.git parco
pip install ./parco
```

This provides the `parco` command (also available as `python -m parco`).

## Set up a LaTeX project

From the root of your LaTeX project:

```bash
parco init --main main.tex --bib refs.bib --context ../my-code
```

- `--main`: the entry tex file. Parco tracks it and every file it pulls in through `\input` or `\include`.
- `--bib`: the bibliography file (detected from the sources if left out).
- `--context`: a folder or file the AI can read as background, such as a code repository or notes. It is never reviewed. Repeat it for several paths.

This creates a hidden `.parco/` folder (configuration, review state and the snapshot of the last version). You can now open the platform, and leave it open while you work:

```bash
parco render
```

It runs locally (port 8765 by default) and updates live while the AI is working. Keyboard shortcuts: `j`/`k` move between cards, `a`/`r` accept or reject the active edit, `c` comments on the selected text, `p` shows pending items only.

## Usage

There are two ways to use Parco: let your AI agent drive it from a short instruction sheet, or run each step yourself.

### With your AI agent (recommended)

Parco ships its own instruction sheet for the AI: `parco guide` prints how to use every command and which rules apply. Once your agent knows about it, you just talk to it:

1. *"Review main.tex with parco in proofread mode."* The agent opens a version, reads the document and submits its edits and comments.
2. Go through them in the platform: accept, reject, reply, ask for changes.
3. *"Answer my comments in parco."* The agent answers your threads and proposes the edits you asked for. Repeat as needed.
4. Click **Close version** in the platform when you are done.

To teach your agent about Parco:

- **Claude Code**: link the two skills shipped in `skills/`, then use `/parco-read <mode>` and `/parco-iterate` (or just ask in plain words).

  ```bash
  mkdir -p ~/.claude/skills
  ln -s "$PWD/parco/skills/parco-read" ~/.claude/skills/parco-read
  ln -s "$PWD/parco/skills/parco-iterate" ~/.claude/skills/parco-iterate
  ```

- **Any other agent** (ChatGPT / Codex, Gemini CLI, Cursor...): add one line to its instructions, for instance in the `AGENTS.md` of your LaTeX project or in your custom instructions:

  ```
  To review a LaTeX document with parco, first run `parco guide` and follow it exactly.
  ```

The agent only ever proposes: every action goes through `parco`, which checks it against the mode and the phase, and nothing reaches your `.tex` files before you accept it and close the version.

### Manually

You can also run every step yourself, which is handy to script Parco or to plug it into another tool:

| Command | Purpose |
|---|---|
| `parco open --mode <mode>` | Start a new version in a mode (`reference`, `comment`, `proofread`, `generative`) |
| `parco context` | Show what changed since the last version, the file list and the context paths |
| `parco edit add`, `parco comment add`, `parco reply <id>` | Submit edits, comments and replies (JSON in `--file` or on stdin, `--batch` for several) |
| `parco iterate` | Move the version to the iterate phase: only replies and edits attached to a thread |
| `parco threads [--open]` | List the threads with their discussion |
| `parco accept <ids>` / `parco reject <ids>` | Decide on edits from the terminal |
| `parco status` | Show version, phase, mode, edits and threads |
| `parco close` | End the version and write accepted edits to the sources |

For instance, to propose an edit:

```bash
parco edit add <<'EOF'
{"file": "intro.tex", "anchor": "we shows that", "replace": "we show that", "reason": "grammar"}
EOF
```

`parco guide` documents the JSON format and the rules in full. See [docs/design.md](docs/design.md) for the design.

Do not edit your `.tex` files while a version is open: Parco detects it and asks you to close the version and start a new one. Accepted edits are kept aside and written to the sources only at close, and the platform always shows the document with them applied.

## Try the demo

```bash
examples/make_demo.sh
```

This copies a small LaTeX paper to `examples/demo_run`, simulates an AI reading in `generative` mode, and prints the command to open the platform. Set `PYTHON=/path/to/python` to choose the interpreter.

## Contributing

Issues and pull requests are welcome. Run the tests with:

```bash
pip install -e . pytest
pytest
```

## License

MIT, see [LICENSE](LICENSE).
