<p align="center">
  <img src="assets/sharpen-banner.png" alt="Sharpen: a kid with spiky white hair and a red blindfold, beside the word Sharpen. You type “fix the login thing.” It knows which one." width="100%">
</p>

<p align="center">
  <a href="https://sharpen-site.vercel.app"><strong>Website</strong></a> ·
  <a href="https://sharpen-site.vercel.app/docs/"><strong>Docs</strong></a> ·
  <a href="CHANGELOG.md"><strong>Changelog</strong></a>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/melthond/sharpen?style=flat-square&color=111111&label=stars" alt="Stars">
  <img src="https://img.shields.io/github/v/release/melthond/sharpen?style=flat-square&color=111111&label=release" alt="Release">
  <a href="https://github.com/melthond/sharpen/actions/workflows/test.yml"><img src="https://img.shields.io/github/actions/workflow/status/melthond/sharpen/test.yml?branch=main&style=flat-square&label=tests" alt="Tests"></a>
  <img src="https://img.shields.io/badge/works%20with-Claude%20Code-111111?style=flat-square" alt="Works with Claude Code">
  <img src="https://img.shields.io/badge/dependencies-0-111111?style=flat-square" alt="Zero dependencies">
  <img src="https://img.shields.io/badge/telemetry-none-111111?style=flat-square" alt="No telemetry">
  <img src="https://img.shields.io/badge/license-MIT-111111?style=flat-square" alt="MIT license">
</p>

<p align="center">
  A Claude Code and Codex desktop plugin that turns your plain prompt into the prompt you meant. It builds that prompt from your conversation, your code and your installed skills, agents, MCP servers and hooks, and shows it to you before anything runs.
</p>

<p align="center">
  <img src="assets/sharpen-terminal.gif" alt="In Claude Code you type 'fix the login thing'. Sharpen catches it before anything runs, reads your conversation, code, skills and hooks, asks which login problem you meant, then shows the engineered prompt on a review card with Send it and Run my original." width="100%">
</p>

<p align="center">
  <img src="assets/sharpen-result.gif" alt="After Send it, Claude fixes src/auth/pin.js and src/auth/session.js and runs npm test. Sharpen handled 12 of 12 test prompts right. Install with /plugin marketplace add melthond/sharpen, then /plugin install sharpen@sharpen." width="100%">
</p>

---

Think of the colleague who never starts the wrong task. When you say "fix the login thing", they ask *"the PIN lockout, or the Google sign-in?"*, then write the task down with the file, the test and the tools to use. Sharpen puts that colleague inside your agent.

## Highlights

- **Every prompt gets engineered:** where to look, what's already decided, and how to tell it's done.
- **Built from your real setup:** your conversation, your code, and your installed skills, agents, MCP tools and hooks. Setup hooks summarize hook names for Claude Code and Codex, which cannot see the full hook configuration otherwise.
- **Nothing runs until you say so.** The review offers **Send it**, **Run my original**, or an edit. Claude Code also copies the prompt to your clipboard.
- **It asks only when it has to.** "Which did you mean?" appears only when two readings would lead to different work.
- **Ten companion skills:** write prompts for other AIs, hand off to a fresh session, split big tasks, plan in phases, coach your prompting, and more.
- **Zero dependencies, fully local:** no API calls, no telemetry.

**Contents:** [Install](#install) · [Before / after](#before--after) · [In action](#sharpen-in-action) · [How it works](#how-it-works) · [Review card](#the-review-card) · [Skills](#skills) · [Commands](#commands) · [Status badge](#status-badge) · [Privacy](#privacy) · [Updating](#updating) · [Troubleshooting](#troubleshooting) · [FAQ](#faq) · [Evaluation](#evaluation) · [Contributing](#contributing) · [Credits](#credits)

## Install

**Requires:** Claude Code or Codex desktop with plugin support, and Node.js 18 or later (the hooks run on it).

### Codex desktop

This repository includes a local marketplace at `.agents/plugins/marketplace.json` so you can discover and install Sharpen from this checkout. The repository does not enable it for contributors automatically; each person chooses whether to install and enable it in Codex.

1. Open this repository folder in Codex desktop and trust it if Codex asks.
2. Restart Codex so it discovers the repository marketplace. Open **Plugins Directory**, select **Sharpen project**, choose **Sharpen**, then select **Install**.
3. Review and trust Sharpen's bundled hooks when Codex asks. The hooks run locally and require Node.js 18 or later.
4. Open a new local chat and send `sharpen on` to turn on Sharpen's prompt handling. This is a user-level setting that persists across sessions wherever the plugin is enabled; installing the plugin alone leaves it off.
5. Send `sharpen` and confirm Codex reports that Sharpen is on. Then send a harmless request such as `summarize the purpose of this repository`; the Sharpen review should appear before the task runs. Choose **Run my original** to finish the smoke check without changing files.

To enable Sharpen only for this checkout, create a local `.codex/config.toml` and do not commit it:

```toml
[plugins."sharpen@sharpen-project"]
enabled = true
```

Codex reads project settings only for trusted projects. To use the plugin in another repository, install it from a marketplace available to that project and choose whether to enable it there. To update this local install after changing plugin files, refresh or reinstall **Sharpen** from **Sharpen project**, then restart Codex. Codex installs local marketplace plugins into a cache, so it does not read later checkout edits until refreshed. See OpenAI's [local plugin and marketplace guide](https://developers.openai.com/plugins/build/plugins) for the current marketplace and project-enable behavior.

Codex uses its native review form when available. If the host cannot show MCP form elicitation, Sharpen presents numbered choices in the conversation instead. Closing the review without choosing leaves the request unstarted; send a new message to continue.

### Claude Code

Run these in Claude Code as two separate prompts:

```
/plugin marketplace add melthond/sharpen
```
```
/plugin install sharpen@sharpen
```

Restart Claude Code, then turn it on:

```
/sharpen on
```

Sharpen is **off by default**. The on/off setting carries over between sessions.

> [!IMPORTANT]
> Only install from `melthond/sharpen` on GitHub. Sharpen is plain JavaScript and Markdown and never ships binaries.

## Before / after

You type:

```
fix the clipboard so it clears after 30 seconds
```

**Without Sharpen,** the agent starts from those ten words. It may or may not find the test, the on-screen hint and the spec that all say 60.

**With Sharpen,** you get this card first (from a real run):

```
Sharpened prompt (fill-in):
  Change the clipboard clear for copied keys from 60 to 30 seconds.
  Where: apps/admin/src/lib/clipboard.ts:2 (HOLD_MS = 60_000 → 30_000)
  Also update: generate.tsx:181 (hint text), clipboard.test.ts, PRD FR-19 (:269), checklist US-020
  Keep: the "leave it alone if something else was copied" rule
  Hooks: dead-code-check runs after every edit
  Check: npx vitest run apps/admin/src/lib/clipboard.test.ts passes

  ❯ Send it (Recommended)      Run my original      [type your changes]
```

## Sharpen in action

Real screenshots, taken in a small demo app.

<details open>
<summary><b>Claude Code</b></summary>

<br>

<p align="center">
  <img src="assets/screenshots/claude-code/send-card.png" width="880" alt="A real Sharpen review card in Claude Code for the prompt fix the failing tests. It asks Send this sharpened prompt, with Send it (Recommended) and Run my original. The preview names both failing tests, the root cause in src/auth/pin.js and src/auth/session.js with the exact code, says to fix the source only and leave the menu alone, and lists Tools, Hooks and Check: npm test passes, all 5 tests green.">
</p>

<p align="center"><sub>One reading: <code>fix the failing tests</code> becomes this card.</sub></p>

<p align="center">
  <img src="assets/screenshots/claude-code/which-did-you-mean.png" width="880" alt="A real Sharpen card in Claude Code. The prompt was fix the login thing. Sharpen found two login bugs and asks Which did you mean, with Fix both login bugs, Fix staff PIN lockout, Fix member session expiry, and Run as typed. The preview shows the engineered prompt: symptoms with file names, a reproduce step with failing tests first, the fix, a Tools line with three skills, a Hooks line, and Check: npm test passes.">
</p>

<p align="center"><sub>Two readings: <code>fix the login thing</code> in an app with two login bugs.</sub></p>

<p align="center">
  <img src="assets/screenshots/claude-code/vscode-extension.png" width="688" alt="A real Sharpen card in the Claude Code extension for VS Code. The prompt was fix the login thing. It asks Which did you mean, naming the two failing login tests in src/auth/pin.js and src/auth/session.js, with Fix both login bugs, Fix PIN lockout only, Fix session expiry only, and Run as typed. The preview shows the engineered prompt with Starting state, Target state, Work only in, Do not touch, Tools, Hooks and Evidence lines.">
</p>

<p align="center"><sub>The same card in the <b>VS Code extension</b>. The status badge is terminal only.</sub></p>

<p align="center">
  <img src="assets/screenshots/claude-code/vscode-oat-milk.png" width="701" alt="A real Sharpen card in the Claude Code extension for VS Code. The prompt was add oat milk. It notes that src/menu.js has a flat MENU list with no add-on system and no oat milk price in the code, and asks Which did you mean, with Oat milk as add-on, Oat milk as menu item, Run as typed, and Other. The preview shows the engineered prompt with Starting state, Target state, ASK blanks for the oat milk price and which drinks it applies to, Work only in, Do not touch, Tools, Hooks and Evidence lines.">
</p>

<p align="center"><sub><code>add oat milk</code>: the price isn't in the code, so it becomes an <code>[ASK: …]</code> blank instead of a guess.</sub></p>

</details>

Codex is supported through a local marketplace in Codex desktop. Gemini CLI and GitHub Copilot CLI are not supported yet.

## How it works

<p align="center">
  <img src="assets/gate.svg" width="880" alt="The gate sorts each prompt three ways. Clear: Sharpen only adds context. Fill-in: it fills the gaps from the conversation and code. Ambiguous: it asks which you meant, with 2 to 3 options plus Run as typed.">
</p>

1. **Gate.** Each prompt is **clear** (only context gets added), **fill-in** (one reading, so the gaps get filled) or **ambiguous** (readings lead to different work, so you get 2–3 options plus *Run as typed*).
2. **Gather.** The conversation comes first, then up to 3 quick code searches (6 if the prompt is ambiguous), then your setup: the skills, agents, MCP tools and plugin commands the host lists, plus a names-only summary of configured hooks and plugins that Sharpen builds at session start.
3. **Engineer.** It sorts the intent and fills the slots that kind of request needs (below), then checks the prompt for common mistakes: vague verbs, no finish line, bundled tasks, pasted credentials.
4. **Review card.** Nothing runs until you answer it.

<p align="center">
  <img src="assets/how-it-works.svg" width="880" alt="Four inputs feed the engineered prompt: the conversation gives Decided, the codebase gives Where, your installed tools give Tools, and your hooks give Hooks. The prompt goes to a review card: Send it, Run my original, or your changes for an updated card. It is also copied to the clipboard.">
</p>

| Intent | The prompt spells out |
|---|---|
| Bug | Symptom · Where · Reproduce (failing test) · Fix · Check |
| Feature | What and for whom · Where it plugs in · Pattern to follow · Done when · Out of scope |
| Refactor | Target · Behaviour that must not change · Tests stay green · Scope limit |
| Performance | Metric · Baseline first · Target · Where |
| Question / Review / Explore | What · Focus or depth · Read-only |
| Ops (git, deploy, config) | Exact action · Target · Ask before anything irreversible |
| UI | Design system · States · Widths · Visual check |

Three lines tie the prompt to *your* environment:

| Line | Carries | Example |
|---|---|---|
| `Decided:` | Earlier decisions that still apply | `Decided: keep the counter in pin.ts, no new dependency` |
| `Tools:` | Installed tools to use, in order. Your project's own come first | `Tools: Explore agent → systematic-debugging skill` |
| `Hooks:` | Hooks that will run during the work. They're never called | `Hooks: dead-code-check runs after every edit` |

Work that edits code or runs commands gets a full brief: **starting state, target state, where it may work, what it must not touch, what to stop and ask about first, and the evidence to report**. A value only you can decide, like a price or a limit, becomes an `[ASK: …]` blank instead of a guess.

<details>
<summary>The reference files Sharpen reads when a prompt needs them</summary>

| File | Covers |
|---|---|
| [anti-patterns.md](skills/sharpen/references/anti-patterns.md) | 88 named prompt mistakes and their fixes |
| [briefs.md](skills/sharpen/references/briefs.md) | Brief shapes: long runs, chains, decisions, reviews, UI, prompt fixes, final reports, machine-read output |
| [techniques.md](skills/sharpen/references/techniques.md) | Escalation, decomposition, examples, verification, grounding, agent eagerness, context budget |
| [llm-features.md](skills/sharpen/references/llm-features.md) | Prompts inside a product: system prompts, tools, agent context, untrusted input, migrations |
| [targets.md](skills/sharpen/references/targets.md) | Profiles for other tools and model families |
| [model-notes.md](skills/sharpen/references/model-notes.md) | Dated provider settings and formats, each linked to its source |
| [phases.md](skills/sharpen/references/phases.md) | Kickoff, spec, plan, tasks, build, long loop, done check, resume |

</details>

## The review card

| You choose | What happens |
|---|---|
| **Send it** | Your agent works on the engineered prompt |
| **Run my original** | Your agent works on what you typed |
| **Type your changes** ("make it 15 seconds") | You get an updated review |
| **Esc, then Ctrl+V** (⌘V on macOS) | In Claude Code, paste the prompt from your clipboard, edit it and send it. It won't get sharpened twice |

Claude Code doesn't let a plugin replace your prompt, fill the input box or send messages as you. The review plus the clipboard is as close as it gets. Codex displays reviews through its native MCP form.

## Skills

Ten companion skills. They work whether Sharpen is on or off.

Invoke these as `$sharpen-prompt`, `$sharpen-plan`, and so on in Codex. The slash-command forms below are for Claude Code.

| Skill | What it does |
|---|---|
| `/sharpen:sharpen-prompt <prompt>` | Writes the engineered prompt and **hands it back without running it**. Add "for ChatGPT" or "for a ticket" to get a version that stands on its own. |
| `/sharpen:sharpen-decompile <prompt>` | Breaks down a prompt you already have, names its weak spots, then adapts, simplifies or splits it. |
| `/sharpen:sharpen-handoff` | Turns the conversation into **one starting prompt for a fresh session**, including what failed and why. |
| `/sharpen:sharpen-split <request>` | Splits a big request into **small, ordered prompts**, grouped into waves that can run in parallel. |
| `/sharpen:sharpen-interview <feature>` | Asks about a fuzzy feature **one question at a time**, then writes `SPEC.md`. |
| `/sharpen:sharpen-plan <project>` | Builds the **phase chain** (kickoff, spec, plan, tasks, build prompt), sized to the work. Writes files only after you approve. |
| `/sharpen:sharpen-review` | Coaches **your** prompting: what recent prompts left out, what that cost, and the one habit that would help most. |
| `/sharpen:sharpen-save [name]` | Saves a prompt you keep typing as a **project slash command**. Shows the file first and never overwrites. |
| `/sharpen:sharpen-audit` | Finds what an agent can't see from your code (test commands, unwritten rules, which folder owns what), as paste-ready `CLAUDE.md` lines. |
| `/sharpen:sharpen-help` | A quick reference card. |

## Commands

| Command | What it does |
|---|---|
| `/sharpen on` | Turn Sharpen on. Every prompt gets a review card. |
| `/sharpen off` | Turn it off. The skills still work. |
| `/sharpen` | Show whether it's on, plus the local follow-up count. |
| `raw: <prompt>` | Skip Sharpen for one prompt. |
| `sharpen: <prompt>` | Force a review card for one prompt, even when the prompt is clear or Sharpen is off. |

`/sharpen:sharpen on` works too. In Codex, send `sharpen on`, `sharpen off`, or `sharpen` for status. Other slash commands are never touched, and a bare go-ahead (`continue`, `yes`, `ok`) carries on with the current task without a card.

## Status badge

While Sharpen is on, a red badge in the terminal status bar shows what it decided about your latest prompt:

| Badge | Meaning |
|---|---|
| `[SHARPEN - CLEAR - READY]` | Clear prompt, card waiting |
| `[SHARPEN - FILL-IN - READY]` | One reading filled in, card waiting |
| `[SHARPEN - AMBIGUOUS - READY]` | Several readings, options waiting |
| `[SHARPEN - … - SENT]` | You answered the card and the prompt is running |
| `[SHARPEN - SENT]` | You pasted a sharpened prompt back and sent it |
| `[SHARPEN - RAW]` | You skipped Sharpen with `raw:` |
| `[SHARPEN]` | Nothing to show yet, or the prompt was a slash command |

The badge is Claude Code-only. It reads the session transcript, so it costs no tokens and stores nothing. It sets itself up the first time you run `/sharpen on`. If you already have a status line, Sharpen **never overwrites it**. Claude offers once to chain the badge after yours.

## Privacy

- **Nothing leaves your machine:** no API calls, telemetry or webhooks. The agent you already use does the thinking.
- **Prompts are never logged.** The hooks read the prompt, decide what to do and exit.
- **Your settings are read, not changed.** The hook summary keeps only each hook's event and script *name*, never its arguments (they can hold tokens).
- **Your clipboard is used in Claude Code.** When a review appears, the engineered prompt replaces what's on it. Codex displays the review in its native form instead.

Files Sharpen writes:

| Path | Holds |
|---|---|
| `~/.config/sharpen/state.json` | On or off |
| `~/.config/sharpen/last-sharpened.txt` | The last engineered prompt, so a pasted copy isn't sharpened twice |
| `~/.config/sharpen/stats.json` | Two counts: cards shown, and follow-ups that pushed back ("still failing"). No prompt text |
| `~/.config/sharpen/card-pending` | Empty marker: a card was just shown, so the next prompt is checked for pushback |
| `~/.config/sharpen/sharpen-statusline.js` | The badge script, kept outside the plugin folder so updates don't break it |
| `~/.claude/settings.json` | Edited only to add the badge when you have no status line |
| `~/.codex/plugins/cache/` | Codex's installed plugin copy; refresh it from the local marketplace after checkout changes |

To report a security issue, see [SECURITY.md](SECURITY.md).

## Updating

```
/plugin marketplace update sharpen
/plugin update sharpen@sharpen
```

Then **restart Claude Code**. A session that was already open keeps the old version.

For Codex desktop, refresh or reinstall the plugin from the **Sharpen project** repository marketplace, then restart Codex. Send `sharpen` in a local repository chat to check the status.

## Troubleshooting

| Problem | Fix |
|---|---|
| Claude runs the prompt straight away, with no card | The session has an older version loaded (the card arrived in v1.6.0). Update, restart, and check with `/sharpen:sharpen-help`. If it still happens, [open an issue](https://github.com/melthond/sharpen/issues) with the prompt. |
| Codex does not show Sharpen in Plugins Directory | Restart Codex with this repository open and trusted. Confirm `.agents/plugins/marketplace.json` is present, then refresh the local marketplace. |
| Codex runs a prompt without a Sharpen review | Confirm the plugin is installed and its hooks are trusted, then send `sharpen` to check status. If it is off, send `sharpen on`; start a new chat after trusting or enabling the plugin. |
| Codex keeps using an older local plugin copy | Refresh or reinstall Sharpen from **Sharpen project** in Plugins Directory, then restart Codex. Local marketplace plugins load from a cache. |
| The badge doesn't show | You already had a status line, so Sharpen left it alone. Add `node "~/.config/sharpen/sharpen-statusline.js"` after your status line command. The badge only shows while Sharpen is on, and only in the terminal. |
| Nothing lands on the clipboard (Linux) | Install `wl-copy`, `xclip` or `xsel`. Windows (`clip`) and macOS (`pbcopy`) work out of the box. |

## FAQ

<details>
<summary>Won't this slow me down?</summary>

By one click per prompt. In return you see what will run before it runs, so a wrong guess costs one look instead of a wrong change. If you're sure about a prompt, start it with `raw:`.
</details>

<details>
<summary>Does it cost extra tokens?</summary>

A few. The method (~6 KB) and your setup summary load once per session, plus one short line per prompt. A prompt that names the right files and checks usually saves the extra turn a vague one would cost.
</details>

<details>
<summary>Doesn't rewriting a clear prompt make it worse?</summary>

It can, if the rewrite changes what you asked for. So for a clear prompt, Sharpen only *adds* context and never rewords the request.
</details>

<details>
<summary>Can it put the prompt straight into my input box?</summary>

No. Claude Code doesn't allow that. Press Esc, then Ctrl+V to paste it from your clipboard.
</details>

<details>
<summary>Does it work in Codex, Gemini CLI, Copilot CLI or Cursor?</summary>

Codex desktop is supported through the repository's local marketplace and bundled lifecycle hooks. Gemini CLI, GitHub Copilot CLI and Cursor are not supported yet. The `/sharpen off` command works in Claude Code; in Codex, send `sharpen off`.
</details>

<details>
<summary>Why "sharpen"?</summary>

A blunt prompt still cuts, just not where you meant.
</details>

## Evaluation

The first release was tested on a real Tauri + React + Firebase codebase through `claude -p`, with editing blocked, and every answer was read by hand:

| Prompt type | Result |
|---|---|
| Clear (`explain what apps/admin/src/api/client.ts exports`) | 5/5 recognized as clear, request kept as asked |
| Vague (`make it faster`, `clean this up`, `it's broken again`…) | 5/5 got options naming real files and the project's own agents |
| `raw:` and `sharpen:` prefixes | 2/2 after one tuning round |

Later releases were spot-checked on the same codebase, and the repo has 133 automated tests. To see the full eval set or re-run it, go to [`tests/eval/prompts.md`](tests/eval/prompts.md).

## Contributing

Bug fixes are welcome. Changes to the method need an eval first, because wording that looks harmless can make Sharpen worse. See **[CONTRIBUTING.md](CONTRIBUTING.md)**.

```bash
git clone https://github.com/melthond/sharpen
cd sharpen
npm test                 # zero dependencies
claude --plugin-dir .    # try your checkout without installing it
```

<details>
<summary>What's in this repo</summary>

All of Sharpen is one prompt: [`skills/sharpen/SKILL.md`](skills/sharpen/SKILL.md). Everything else loads it at the right moment.

| Path | Job |
|---|---|
| `hooks/sharpen-session.js` | `SessionStart`: loads the method and your setup summary |
| `hooks/sharpen-prompt.js` | `UserPromptSubmit`: handles `/sharpen on\|off`, recognizes pasted prompts, counts pushback, and reminds Claude of the method |
| `hooks/sharpen-clipboard.js` | `PreToolUse` on the review card: copies the prompt to your clipboard |
| `hooks/sharpen-core.js` | The decision table: pure functions, fully tested |
| `hooks/sharpen-env.js` | The setup summary: hook names and enabled plugins |
| `hooks/codex-prompt.js`, `hooks/codex-session.js` | Codex hooks: prompt gate, status commands, and session instructions |
| `hooks/sharpen-codex-env.js` | The Codex setup summary: skill, MCP server, and hook names only |
| `hooks/sharpen-review-mcp.js`, `mcp.json` | Native Codex review choices and numbered fallback when native elicitation is unavailable |
| `.codex-plugin/plugin.json`, `hooks/codex-hooks.json` | Codex desktop plugin metadata and bundled lifecycle hooks |
| `.agents/plugins/marketplace.json` | Local marketplace discovery for the Codex plugin |
| `hooks/sharpen-state.js`, `sharpen-stats.js` | The on/off flag and the local counts |
| `hooks/sharpen-statusline.js`, `sharpen-statusline-setup.js` | The badge, and installing it without overwriting yours |
| `hooks/sharpen-io.js` | Shared stdin/stdout helpers |
| `skills/` | The method, its reference files and the ten companion skills |
| `commands/sharpen.md` | The `/sharpen` command |
| `apps/web/` | The [website](https://sharpen-site.vercel.app) ([guide](apps/web/README.md)) |
| `scripts/` | The test runner and the diagram builder |
| `docs/` | The original design, plan and research ([index](docs/README.md)) |

The hooks never block a prompt. On any error they exit quietly, and if stdin never closes (a known Windows quirk) they give up after 3 seconds.
</details>

## Credits

The method draws on the [DAIR.AI Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide), [prompt-master](https://github.com/nidhinjs/prompt-master), the [OpenAI Cookbook](https://github.com/openai/openai-cookbook), [GitHub Spec Kit](https://github.com/github/spec-kit), [12-Factor Agents](https://github.com/humanlayer/12-factor-agents), the Anthropic, OpenAI and Google prompting guides, and published research. **[CREDITS.md](CREDITS.md)** lists every source.

## License

[MIT](LICENSE.md). The diagrams use the xkcd Script font, which has [its own license](assets/fonts/LICENSE.md).

## Star History

<a href="https://www.star-history.com/melthond/sharpen#history">
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=melthond/sharpen&type=Date" />
</a>
