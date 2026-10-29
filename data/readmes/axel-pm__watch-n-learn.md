<p align="center">
  <img src="assets/banner.svg" alt="Watch &amp; Learn" width="560">
</p>

# Watch & Learn

**Point it at a how-to video. It writes a reusable skill for your AI coding assistant, one it can follow later without anyone watching the video again.** Everything runs on your own machine. No accounts, no API keys.

<p align="center">
  <img src="assets/diagram.svg" alt="How Watch &amp; Learn works: a how-to video becomes a reusable skill in five local steps" width="900">
</p>
<p align="center"><em>From a how-to video to a reusable skill, in five local steps.</em></p>

<!-- A short screencast GIF of a real run could be added here later as assets/demo.gif -->

---

## What problem this solves

You find a great tutorial: a screencast, a conference talk, a product demo. It shows exactly how to do something. But a video isn't something your AI assistant can use. Next week you've forgotten the steps, and you're scrubbing through it again.

Watch & Learn watches the video for you and turns what it teaches into a **skill**: a small folder of plain instructions your AI coding assistant reads and follows on its own. Once it exists, you (or your assistant) just say "do that thing" and it happens. No re-watching.

> **New to skills?** A *skill* is just a folder with a `SKILL.md` file inside it: instructions written in plain Markdown that an AI coding agent (like Claude Code) automatically reads and follows when the moment is right. That's the whole idea. Anthropic published the format as an [open standard](https://agentskills.io/specification), and several other agents read it too (more on that below).

## How it works

Five steps, all local:

1. Check it's worth it. A quick first pass decides whether the video actually teaches a reusable procedure. If it doesn't (a keynote, a one-off, something too trivial), it says so and stops instead of making a weak skill.
2. Watch. It pulls a handful of still frames out of the video and transcribes the audio, so it can "see" and "hear" what happened. (Uses [PyAV](https://pyav.org) for frames and [faster-whisper](https://github.com/SYSTRAN/faster-whisper) for transcription; both run offline.)
3. Break it down. It turns the video into a clear, ordered list of the steps being taught.
4. Write the skill. It writes the `SKILL.md` (plus any helper scripts) so an agent can follow the procedure cold.
5. Prove it works. It runs the new skill on a real test task to confirm it holds up, and fixes it if not.

You can watch just the audio or just the picture. By default it uses both, but you can point it at a talk or podcast with `--transcript-only` (skip the pictures, much cheaper) or at a silent screencast with `--frames-only` (skip the audio). The rule of thumb: is the lesson in what's *said* or what's *shown*?

## Install

**Claude Code** (one command each):

```
/plugin marketplace add axel-pm/watch-n-learn
/plugin install watch-and-learn@wnl
```

That's it. The first time you use it, it does a one-time setup that installs the local video tools into `~/.video-watch-tools` (a few minutes, one time per machine).

Then just ask, in plain words:

> "Watch this tutorial and turn it into a skill: https://youtube.com/watch?v=…"

**Using a different agent?** See [AGENTS.md](AGENTS.md). The skill format works with several other coding agents, and the file explains how to install it there.

## See it in action

We used Watch & Learn on a real Anthropic talk and turned it into a working skill, then wired that skill so it fires automatically at the right moment. The full story, with the actual files it produced, is here:

**→ [Case study: from a talk to an auto-firing skill](docs/case-study-find-your-unknowns.md)**

## What it needs

- **Python 3** (already on most machines).
- **Internet** on the first run (to fetch the video tools) and whenever you point it at an online video. Local video files work fully offline after that first setup.
- **No API keys, no paid services.** Transcription happens on your machine.

## A note on trust

Skills can run code, so treat installing one like installing any small tool: only run skills from sources you trust. Everything here is open source under the [MIT license](LICENSE). The scripts are short and readable, so you can check exactly what they do before running them.

## Contributing

Issues and pull requests are welcome. Two quick checks run on every change:

- `python3 skills/watch-and-learn/scripts/validate_skill.py skills/watch-and-learn` — confirms the skill is well-formed.
- `claude plugin validate .` — confirms the install manifests are valid.

## License

[MIT](LICENSE).
