<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/mark-dark.svg">
    <img src="docs/assets/mark-light.svg" alt="legibify logo" width="96">
  </picture>
</p>

<h1 align="center">legibify</h1>

<p align="center"><b>Make agent output legible.</b><br>An open-source agent skill that turns a pull request, a commit or a corner of a codebase into an explainer a human can actually check.</p>

<p align="center">
  <a href="https://g10hdz.github.io/legibify/demo/">Live demo</a> ·
  <a href="#install">Install</a> ·
  <a href="#faq">FAQ</a> ·
  <a href="README.es.md">Español</a>
</p>

<p align="center"><img src="docs/assets/demo.gif" alt="legibify demo: clicking a node shows its connections and its diff, drilling into a component, the guided walkthrough and a comprehension check" width="860"></p>

## What is legibify?

legibify is an agent skill for explaining code changes to humans. It works with Claude Code, Cursor, Gemini CLI, GitHub Copilot, OpenCode, Windsurf and any other agent that supports Agent Skills (`SKILL.md`). Instead of a wall of text, it answers in layers, and you stop at the first one that is enough:

1. **Verdict**: what the change does, why, and the biggest risk, in three lines.
2. **Walkthrough**: numbered steps in execution order, each anchored to `file:line`, in plain controlled English.
3. **Blast radius**: what the change touched, drawn as new, modified, deleted and context.
4. **Interactive explainer**: one offline HTML file with a graph you can explore. Click a node to see its connections and its diff, drill into components, follow a guided walkthrough, and test yourself with questions that turn into flashcards.
5. **Video** (optional): a narrated explainer rendered on your machine through [showtime](https://github.com/FavioVazquez/showtime).

It was inspired by [Andrej Karpathy's post](https://x.com/karpathy/status/2105819303471976479) on making LLM output understandable: clear prose first, then diagrams, then interactive HTML, then video.

## Why it is different

- **Every claim traces to `file:line`.** Observations and hypotheses stay apart, and every explainer ends with what still needs verification.
- **The agent never draws by hand.** It writes a JSON model, `build.mjs` validates it (0 errors and 0 warnings, or it does not build) and renders the HTML. Same model, same output.
- **It checks its own layout.** `check.mjs` opens the result in a real browser, walks every view on desktop and on a phone, and fails if an arrow crosses a card or the console shows an error.
- **Made for reading at night and on your phone.** Dark by default, pinch to zoom, and the details slide up from the bottom.
- **Offline forever.** One HTML file: no CDN, no server, no account, no API key.

## Install

```bash
npx skills add G10hdz/legibify
```

Then ask your agent:

- "Explain this PR with legibify."
- "Use legibify to explain how the auth flow works in this repo."
- "Open the PR and attach a legibify explainer to the body."

## How it works

```text
your agent ──writes──▶ model.json ──build.mjs──▶ explainer.html ──check.mjs──▶ screenshots
                       (validated)               (one offline file)       (desktop + phone)
```

The model holds nodes (files, components, parts of a file), typed edges, the walkthrough steps and the comprehension questions. The schema lives in [`references/player.md`](skills/legibify/references/player.md).

| In the explainer | What happens |
|---|---|
| Click a node | Its connections light up and the passport shows what changed, its sources and the diff |
| Click a card with parts | You drill into it; Esc goes back up |
| ▶ walkthrough | The camera follows each step and the active edges animate |
| `/` | Search nodes at any level |
| Check your understanding | Answers light up on the graph; missed questions export to Anki, Obsidian or Hypatia |

## FAQ

**How is this different from a PR summary bot?** A summary is one paragraph you have to trust. legibify gives you a short verdict plus the evidence: every step points to `file:line`, hypotheses are labeled, and the explainer lists what it could not verify.

**Does it need an API key or a server?** No. Your agent writes the model, and a Node script with no dependencies builds the HTML. The visual check is optional and uses `playwright-core` with the Chrome you already have.

**Does it only work for pull requests?** No. In `topic` mode it explains a system or a flow in your repo, with the same graph, walkthrough and questions.

**Can I use it in Spanish?** Yes. The explainer UI ships in English and Spanish (`"lang": "es"` in the model), and the prose follows the language of your repo.

**Can I put it in the PR itself?** Yes. In `attach` mode the verdict, the walkthrough and the "to verify" list go into the PR body between markers, so the agent can regenerate them without duplicating anything.

## Credits

legibify stands on ideas from [pr-lens](https://github.com/coldteadotai/pr-lens), [limen](https://github.com/overment/limen), [archify](https://github.com/tt-a1i/archify), [karpathy-html-graph](https://github.com/xiangbianpangde/karpathy-html-graph), [showtime](https://github.com/FavioVazquez/showtime) and ASD-STE100. The full list, and what came from each one, is in [`references/sources.md`](skills/legibify/references/sources.md).

## License

[Apache-2.0](LICENSE). Made by [@G10hdz](https://github.com/G10hdz).
