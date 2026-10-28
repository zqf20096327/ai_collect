<div align="center">

**English** · [简体中文](README.zh-CN.md) · [繁體中文](docs/readme/README_zh-TW.md) · [日本語](docs/readme/README_ja.md) · [한국어](docs/readme/README_ko.md) · [Français](docs/readme/README_fr.md) · [Deutsch](docs/readme/README_de.md) · [Español](docs/readme/README_es.md) · [Português (Brasil)](docs/readme/README_pt-BR.md) · [Italiano](docs/readme/README_it.md) · [Русский](docs/readme/README_ru.md) · [Tiếng Việt](docs/readme/README_vi.md) · [ไทย](docs/readme/README_th.md) · [Bahasa Indonesia](docs/readme/README_id.md) · [हिन्दी](docs/readme/README_hi.md) · [العربية](docs/readme/README_ar.md) · [Türkçe](docs/readme/README_tr.md)

<br>

<img src="Resources/AppIcon.png" width="112" alt="AllInOneIME icon">

# AllInOneIME

### AI commands in every text field on your Mac.

Type `@improve`, `@translate` or `@question` in any app, press ⏎, and pick the result.<br>
No copying into a chat window, no switching apps. Your own AI provider, your own keys.

[![Release](https://img.shields.io/github/v/release/MicroZ-LLC/AllInOneIME?label=release&color=3b82f6)](https://github.com/MicroZ-LLC/AllInOneIME/releases/latest)
[![macOS 14+](https://img.shields.io/badge/macOS-14%2B-111?logo=apple&logoColor=white)](#installation)
[![Notarized by Apple](https://img.shields.io/badge/Apple-notarized-0a84ff?logo=apple&logoColor=white)](#installation)
[![Apple silicon and Intel](https://img.shields.io/badge/Apple%20silicon%20%2B%20Intel-universal-555)](#installation)
[![License: FSL-1.1-ALv2](https://img.shields.io/badge/license-FSL--1.1--ALv2-f59e0b)](LICENSE)
[![Downloads](https://img.shields.io/github/downloads/MicroZ-LLC/AllInOneIME/total?color=22c55e)](https://github.com/MicroZ-LLC/AllInOneIME/releases)

**[Download](https://allinoneime.com/download)** · **[Website](https://allinoneime.com)** · **[Docs](https://github.com/MicroZ-LLC/AllInOneIME/wiki)** · **[Extensions](docs/extensions.md)**

[How to use](#how-to-use) · [Commands](#commands) · [Your own commands](#your-own-commands) · [Languages](#input-and-translation) · [Installation](#installation) · [Privacy](#privacy)

<br>

<img src="docs/en/demo.png" width="820" alt="@translate and a sentence, then ⏎: a line in Spanish, French and German">

</div>

> [!NOTE]
> From 0.6.3 on, AllInOneIME is signed with a Developer ID and notarized by Apple: no more allowing it in System
> Settings → Privacy & Security. After updating from an earlier version, macOS asks once for your login password for
> each key AllInOneIME saved in the keychain: enter it and click "Always Allow". Download AllInOneIME only from
> [GitHub Releases](https://github.com/MicroZ-LLC/AllInOneIME/releases) or [allinoneime.com](https://allinoneime.com).

A macOS input method with AI commands in every text field. Start a sentence with `@` and press ⏎ when done:
`@improve` polishes what you wrote and offers a few rewrites, `@translate` translates it into the languages you pick,
`@question` asks a question, `@agent` hands it to a coding agent (Claude Code, Gemini CLI, Kiro CLI …), and `@open` finds files and apps or opens a web
address. Without `@`, your keys go to the app as usual. It also types Chinese
(pinyin, built on Rime and rime-ice), French, Korean (Hangul) and Hindi (Devanagari from Latin letters), and runs
your own scripts as commands.

The magic key, the symbol commands start with, is `@` by default. In Settings → General → Magic key, pick another symbol from the menu: `#`, `%`, `&`, `*`, `+`, `|` or `~`; commands then start with it (for example, `~translate`), and `@` types normally. Letters, digits, spaces and the symbols typing needs (pinyin's keys such as `'` `-` `=` `[` `]` `` ` ``, and the ones pinyin types as Chinese punctuation, such as `,` `.` `?` `\`) can't be the magic key, so the menu doesn't offer them. You can also set it in the config file, where it's called the command trigger: `"commandTrigger": "~"`.

![@improve and a rough sentence, then ⏎: polished versions, plus rewrites](docs/en/improve.png)

For more detail (every command and setting, installation troubleshooting, privacy), see the
[Wiki](https://github.com/MicroZ-LLC/AllInOneIME/wiki). Made by [Weijian Zhang](https://weijianz.com) at MicroZ LLC.

## How to use

Without `@`, it stays out of the way: in English, letters are typed directly and ⏎ is Return; nothing goes online.
A new install writes English; to type Chinese (pinyin), French, Korean or Hindi too, add it in the settings (see [Input and translation](#input-and-translation)).

| Key | What it does |
|---|---|
| Type pinyin, Space / digits | In Chinese mode: pick words, as in any pinyin input method |
| `@` (at the start of a sentence) | Opens the command list: the most used lately first, 5 at a time, scrolled with ↑↓, the wheel or the trackpad; or type letters to find one (a name typed in full first, then names starting with them, then names containing them). ⏎, Tab, Space or a digit chooses |
| ⏎ | Runs the command. Works even if the pinyin isn't picked yet: it's picked first, as with Space |
| Space, ⏎ / digits | Once the results are up: insert the highlighted / numbered one; 0 is the original. ⏎ inserts even with a follow-up half typed (it's dropped) |
| ⇧⏎ | With a follow-up typed after AI results: sends it (the next question of an `@question` conversation, or a refine). While a command is typed, or on AI results with nothing typed: inserts what you typed as is, `@command` included. On other results (`@open`, a reminder …) it inserts the highlighted row, as ⏎ does |
| ⌘C | Copies the highlighted result (for `@open`, the path); the candidate panel stays open |
| ⌃V | Shows [clipboard history](#clipboard-history-new), the text you copied lately, newest first: ⏎ or Tab puts in the one chosen, ↓ ↑ choose, ⇧↓ ⇧↑ choose several (⏎ puts them in one per line, oldest first), → or Esc hides it. ⌃V ⏎ is the ⌃V you had, and ⌃V twice gives ⌃V to the app (vim, the shell). In a command (e.g. after `@improve `) the one you choose is appended after what you've typed instead of being pasted into the app: multiple lines become one, up to 2000 characters at a time (`@note` keeps the line breaks and takes up to 20000). Works in any app, terminals too. With clipboard history off, ⌃V in a command appends the clipboard text at once, and without a command it goes to the app as usual |
| ⌘V | The app's Paste. In a command it appends the clipboard text at once, no history, except where the app handles ⌘V itself (terminals such as Ghostty, iTerm2 and Terminal, and Notes) and pastes into the app as usual; use ⌃V there |
| Esc, ⌫ | Back to the sentence to keep editing; typing punctuation or digits after the results continues it. After a refine: back to the results before it |
| Letters, once AI results are up | A follow-up: after `@question` the next question (see [Conversations](#conversations-with-question-new)), after `@improve` or a prompt command an instruction such as `shorter` (see [Refining the results](#refining-the-results-new)); ⇧⏎ sends it. After `@translate` letters continue the sentence, and ⏎ translates it again |
| ⌘⏎, ⌘1–⌘9 | In an `@question` conversation: shows where to continue it (the coding agents installed, the one `@agent` hands to first; Claude, ChatGPT, Gemini; or copy it); ⌘1, ⌘2 … pick one |
| Click a row | In the candidate panel: picks it, as its digit would (a word, a command in the list, a result, an `@open` file, a recipient, an extension's row); the row under the pointer is highlighted. The text field keeps the focus |
| Tap Shift | With more than one input language: the next one, in their order (English → Chinese → French → …, then back to the first) |

## Commands

Commands start with the magic key, `@` by default; with another one picked in Settings → General → Magic key, the
commands below start with it (`~improve`), and so does the app's own text that names them.

| Command | What it does |
|---|---|
| `@improve` | Polish: 1–3 are three versions in the sentence's own language, 4 onward the rewrite styles (added and ordered in the settings), 0 is the original. No translation; with "@improve also translates" on, it works like `@translate @improve` |
| `@translate` | Translate into the languages you added (Settings → General → Translate to, drag to reorder), a line each, three versions with only one; the sentence's own language is skipped. `@translate @improve` together translates and rewrites in one request |
| `@question` | Ask a question; the answer appears in the candidates, ⏎ or Space inserts it, ⌘C copies it. Type on and ⇧⏎ asks a follow-up: the panel becomes a conversation of up to 5 rounds, then offers to continue in Claude or another AI. With nothing typed after it, it lists your last 5 questions, newest first; typing narrows them down (words anywhere in the question, any case, Chinese too). A digit, ↑↓ then ⏎, or a click shows a question's saved answer at once, offline, to insert or copy as usual; ⌘R there asks it again for a fresh answer. With no match, or nothing picked, ⏎ asks what you typed |
| `@reply` | Writes three replies to the message you're answering, in the other party's language and the tone of the app (casual in chat apps, formal in mail, where each reply is a whole email body; or the first of the app's own rewrite styles, set in an earlier version). Give it the message by selecting it, copying it and pressing ⌃V ⏎ in the draft, or taking a screenshot (⌃⇧⌘4, or WeChat's own) and pressing ⌃V ⏎; what you type after it says what to reply: `@reply politely decline`. ⌘R writes three more; see [Replying](#replying-with-reply-new) |
| `@agent` | Hands the task to a coding agent on your Mac, picked in Settings → Commands → Agent (@agent): Claude Code (the default), Gemini CLI, Kiro CLI, or a command of your own (what you typed is added as its last argument). The page also shows whether each is installed and how it starts. Claude Code runs in the background by default, with a notification when it's done (click it to open the session in Terminal and go on), or see `@tasks`; turn off "Claude Code runs in the background and notifies me" there to open it in Terminal. The other agents open in Terminal with what you typed as their first message. Each uses its own sign-in and settings. In Google Chrome it takes the page along: the address and title, the field you typed in with its form or section (★ marks where you are), the selected text and what's visible in the window — never a password field, never the whole page — so `@agent why doesn't this work` in a sign-in form's username field is about that field, and `@agent why is this blocked` on a pipeline page is about that page; the agent judges which. The page's text goes to the agent as read, marked as coming from the web (not as instructions from you). It needs Accessibility; Chrome builds its page tree for it only while `@agent` is being written there, turned back off after (Settings → Privacy → "@agent and @reply take the Chrome page along" turns it all off). The first time it opens Terminal, macOS asks whether AllInOneIME may control Terminal: click OK. (It was `@claude` before 0.6.4.) |
| `@tasks` | Lists the background Claude tasks (working / done / waiting for you) with their last replies; ⏎ opens one in Terminal, ⌘C copies the reply |
| `@settings` | Opens the settings window right away (picking it is enough) |
| `@open` | Lists matching files, folders and apps as you type (Spotlight). Several keywords work, separated by spaces: each must be in the path, at least one in the name (a standard folder's name counts for what's in it: `downloads pdf` finds the PDFs in Downloads). Apps and the standard folders are also found by their Chinese names, and a Chinese interface shows them that way. What you opened with `@open` comes first, then apps and those folders, then recently used or changed files; when the names find two files or fewer and no app or folder of those, the files in your home folder are searched by content too, those rows marked "content"; when there's nothing else, ⏎ lists them to pick from instead of opening the first. With a web address (`github.com`, `localhost:3000`, `https://…`), the first row is "open in the browser" and contents aren't searched; a file named exactly that (say `MANIFEST.in`) comes first. Text starting with `~/` or `/` is a path: Tab completes it and goes into folders; ⏎ opens, ⌘C copies the path |
| `@note` | Saves the text to the Notes app, in a folder named AllInOneIME (made when missing), or where Settings → Commands → Notes (@note) says: Notion, or a folder of Markdown files (an Obsidian vault or any folder); nothing is inserted. Pasted text keeps its line breaks, up to 20000 characters |
| `@reminder` | Adds a reminder to the Reminders app, in a list named AllInOneIME. Write the time in the text; it's read on the Mac, and a row shows what was read: ⏎ or Space adds it, Esc goes back to edit. With a time, it has an alarm then; with only a date, it's all day |
| `@py` | Runs a line of Python (the Mac's `python3`) and inserts the result: the value of the code's last expression, e.g. `@py 2**100`, `@py import math; math.sqrt(2)`, or else what it printed. Not offered without `python3` (Xcode's command line tools have it) |
| `@js` | Runs a line of JavaScript and inserts the same: the value of the last expression or what `console.log` printed, e.g. `@js [1, 2, 3].map(x => x * 2)`. It uses macOS's built-in JavaScriptCore, so there's nothing to install; it can't read files, reach the network or run other programs |
| `@reportissue` | Reports a problem: opens GitHub's page for a new issue in your browser, what you typed after the command as its title, and "What happened / What you expected" to fill in. It adds the app and macOS versions, your Mac's architecture, the interface and input languages, the installed language packs, which kind of AI provider (and the model, if it's a public one; otherwise "custom"), the action key, and how many custom commands, plugins and extensions you have, never their names, your text, paths or keys. ⏎ (or your action key) first shows all of it in the candidate panel; ⏎ again, or a click on the row, opens the page, where you read it and click Submit (with your GitHub account); Esc goes back. Also in the input menu ("Report an Issue…") and Settings → About |
| `@imessage` | Sends an iMessage: type a name, a phone number or an email (a Chinese name also by its pinyin, in full or the initials) and pick the recipient in the candidate panel (the ones you messaged lately come first; a full number or address works too), then write the message (commands inside it such as `@stock AAPL` run first). ⏎ shows "Send to Alex (…): message" in the panel, ⏎ again sends it, Esc goes back to editing; nothing is typed into the text field. The first time, macOS asks whether AllInOneIME may access Contacts and control Messages: click OK for both |

Example: `@q` ⏎, type `what is quantum computing`, ⏎. `@note books to read: The Three-Body Problem` ⏎ saves a note.
`@reminder call Bob tomorrow at 3pm` ⏎, check the time it read, then ⏎ again to add it.
In Chinese mode, `@open` switches to English letters for the moment and goes back to Chinese when you're done.

The code for `@py` and `@js` is typed in English letters, and full-width punctuation (from Chinese mode) becomes ASCII; write it on one line, with `;` between statements.
It runs in a separate process, stopped after 10 seconds or with Esc at any time; on an error, the error's first line is shown, e.g. `ZeroDivisionError: division by zero`.
Output with several lines is inserted as printed; in a terminal it goes in as one line (a terminal runs every line it is given).
A terminal inside an editor (VS Code, Cursor, JetBrains) can't be told apart from the editor itself, so there any command's output with several lines goes in as it is.
Both also work inside another command's sentence: `@reply the answer is @py 2**100`; put code with spaces in quotes: `@question explain @py "sum(x * x for x in range(10))"`.
Not the other way round: the code of `@py` and `@js` always runs exactly as you typed it, and commands in it don't run first.

![Typing @ opens the command list; @question plus a question, then ⏎ for the answer](docs/en/commands.png)

![@open finds apps as you type; starting with /, it's a path: the folder is listed, Tab completes](docs/en/open.png)

When `@` isn't followed by a command, as in `@john`, the `@` is inserted as usual, so @-mentioning
people in chat apps still works.
Typed right after a letter, a digit, `.`, `_` or `-`, as in `bob@example.com` or `ssh user@host`, `@` is just text: no
list opens, in every app, terminals included. With the list open, ← → or a key that can't go on a command's name (`.`, `:`,
`/`) close it and leave what you typed (`@`, `@im`) as it is; in a terminal ← → then only close the list.
`@question`, `@improve`, `@translate` and `@reply` send to your own Bedrock only when you press the action key (a screenshot is read on
this Mac and only its text is sent); `@open` searches only on this
Mac; `@note` and `@reminder` go only to Notes and Reminders on this Mac (`@note` to a folder or to Notion instead, if you chose one); `@agent` uses the agent installed on your Mac (Claude Code's `claude` command by default) and its own account, and it asks
you first, as usual, before changing files or running commands. Without the agent installed, `@agent` isn't offered.
`@imessage` reads Contacts on this Mac only (names, phone numbers, emails), never goes through the AI, and Messages sends
the message; without the Messages app it isn't offered.

### On the selected text (new)

Select some text in any app (a sentence in Notes, a paragraph in Mail), type `@improve`, `@translate`, `@question`
or another command that takes text, and press ⏎: the command works on the selection, and the result you pick replaces
it. The selection stays as it is, selected, while you type: the command is written in the candidate panel, whose first
line is what you type and the next "On the selection: “…” (N characters)". Esc, ⇧⏎ or clicking elsewhere leave the text
as it was; so does a selection you change meanwhile, which cancels the command. Text typed after the command is an
instruction for `@improve` and `@translate` (`@translate ja`, `@improve more formal`) and the question for `@question`
(`@question what does this mean`), about the selection. `@open`, `@agent`, `@tasks`, `@settings`, `@reminder`,
`@imessage`, `@reportissue`, terminal commands and script extensions don't use it: they take what you type, and the
selection stays as it is. Up to 5000 characters; never read during secure input or in a
terminal. Turn it off under Settings → Advanced → "Use the selected text" if it misbehaves in an app.

### Replying with @reply (new)

`@reply` writes three replies you could send to the message you're answering. Give it the message in any of these ways,
then press ⏎:

- **Select it** in the field, then type `@reply` (the reply you pick goes in after it, on a line of its own).
- **Copy it**, type `@reply` and press ⌃V ⏎ (⌃V shows [clipboard history](#clipboard-history-new), what you copied last chosen first): the panel shows "Copied message · N characters", and the draft stays as it is.
- **Take a screenshot** to the clipboard (⌃⇧⌘4, or WeChat's own screenshot), type `@reply` and press ⌃V ⏎: the panel
  shows "Screenshot · N lines (read on this Mac)". The screenshot is read on this Mac (Apple's Vision, the first time a
  little slower) and only its text is sent; the image goes nowhere and isn't kept. Lines on the left are the other
  party's and on the right yours, as chat apps show them; the times between messages are left out. Use it for WeChat,
  whose window can't be read any other way.

Type what you want to say after it (`@reply politely decline`, `@reply 委婉拒绝`), or nothing for a sensible answer. The
replies are in the other party's language unless you ask for another, and in the app's tone: casual in chat apps and
formal in mail apps, where each reply is a whole email body (or the first of the app's own rewrite styles, set in an
earlier version). The text around the cursor goes along too. ⌫ with nothing typed after `@reply` removes what was pasted. ⏎ or
a digit inserts a reply; ⌘R writes three more (Esc brings these back), and typing an instruction refines them as for any
AI result. In Google Chrome, with nothing selected or pasted, it takes the page along as `@agent` does (Settings →
Privacy → "@agent and @reply take the Chrome page along"). With nothing to reply to and nothing typed, it says what it
needs. Hiding sensitive information covers the screenshot's text too; during secure input the clipboard isn't read
and nothing is sent. A custom command you had named `reply` is now `@myreply`.

A screenshot pasted into any other command works too: `@translate` ⌃V ⏎ translates it (into the caret), `@question what
does this say` ⌃V ⏎ asks about it, and commands without AI get its text as if it had been copied (`@note` keeps its lines).
With text selected, `@improve` and `@translate` keep working on the selection, and a notice says the screenshot wasn't
used.

### Refining the results (new)

While the results of `@improve`, a prompt command (your own or a plugin's) or the rewrite of a selection are up, type
what to change, such as `shorter`, `warmer`, `more formal`, `add a joke`, `in Japanese` or `用更口语的说法` (pinyin works,
and a tap of Shift switches languages), and press ⇧⏎: the results go to the AI again with your instruction, and the new
ones replace them in the same panel. ⏎ inserts the selected result, also with an instruction half typed (it's dropped).
Refine again as often as you like; the panel's top line lists the steps ("Refined: shorter · more formal"), and you can
pick a row at any time as usual. A letter starts the instruction (shown as "refine › …" at the top of the panel); while
it's empty, digits, Space and ⏎ pick as before, and ⇧⏎ inserts what you typed as is. Refining starts once the results are
complete: typing while the first results still stream in continues the sentence, as before. While a refine runs you can
already type the next instruction; the refine goes on, and ⇧⏎ runs the next one once its results are in. Esc clears the
instruction, then goes back one step to the results before the last refine (during a refine: stops it), then back to the
sentence; ⌫ on an empty line steps back the same way. On selected text, the result you pick still replaces
exactly the selection, which stays untouched until then. A refine that fails (or is refused during secure input) leaves
the results as they were, its instruction ready for ⇧⏎ to try again. The same refine of the same results is answered from
the cache. `@translate` has no refine: typing after its results continues the sentence, and ⏎ translates it again.

### Conversations with @question (new)

Once `@question` has answered, what you type is the next question: ⇧⏎ asks it, with the questions and answers so far,
and the panel grows into the conversation, the earlier rounds dimmed as Q / A rows, the latest answer below them. The
line on top says which round comes next ("question 2/5 › …"). Every answer can be inserted: its digit (1–5), ↑↓ then ⏎, or
a click; the latest is selected, and ⌘C copies the selected one. ⏎ inserts it even with a question half typed (it's
dropped). Esc clears what you typed, then goes back one round; at the first, it leaves as before. The panel grows to
about half the screen, then scrolls, the latest at the bottom.

After 5 rounds (`questionRounds` in the config, 2–10) the next question's line becomes "5 rounds in: continue in Claude
or another AI", with the choices numbered ⌘1, ⌘2 …; ⌘⏎ shows them at any round (while an answer is still coming in it
does nothing, and never reaches the app). What you type then is the first message there; only ⌘1, ⌘2 … send it (⇧⏎
asks nothing more, and opens nothing). A question about selected text takes that text along, quoted as a block of its
own. The choices:

- **The coding agents installed** on this Mac, each by its name: the one `@agent` hands to first (⌘1), then the others
  (Claude Code, Gemini CLI, Kiro CLI, your own command from Settings → Commands → Agent). Each opens an interactive session in
  Terminal, started as `@agent` starts it, beginning with the conversation and "Let's continue this discussion". One
  that isn't installed isn't shown.
- **Claude** or **ChatGPT** on the web, the conversation filled in (a long one goes on the clipboard: paste it).
- **Gemini** on the web, the conversation on the clipboard to paste.
- **Copy the conversation**, in Markdown (**Q:** / **A:**).

Which ones, and in which order (the first is the default): Settings → Commands → "Continue a conversation in"
(`questionContinueIn` in the config); with more than 5, ⌘6 … ⌘9 pick the rest. "@agent's agent" there is whichever
agent Settings → Commands → Agent picks, by its name; an agent that isn't installed right now keeps its place in the list when you
edit it. With Apple Intelligence on this Mac a long conversation doesn't fit its small context: the oldest answers are
shortened, then the oldest rounds left out, and the panel says "earlier rounds shortened". A conversation is saved
under its first question in the recent questions, and picking it shows the rounds to go on with.

### Recent questions (new)

`@question` with nothing typed after it lists your last 5 questions, newest first, with when they were asked ("3 hours
ago"). Typing narrows them down: every word anywhere in the question, in any case (Chinese without spaces too). A digit,
↑↓ then ⏎, or a click shows a question's saved answer at once, without going online: Space or ⏎ inserts it, ⌘C copies
it, ⌘R asks it again for a fresh answer (a conversation: its latest question), Esc goes back to the list. A saved
conversation shows all its rounds: type to go on with it. With no match, or nothing picked, ⏎ asks what you typed. A new answer to the same question, or a conversation
that goes on, replaces the saved one.

- They're kept only on this Mac (see Privacy): not while secure input is on, and never for questions on selected text.
- Settings → Privacy → "Remember recent questions" turns it off (`rememberQuestions` in the config); turned off there,
  it deletes them too. Turned off through the settings search's Change: … (see [Settings](#settings-new)), they're kept, so
  that undoing it puts back exactly what was (its preview says so); "Forget (N)" deletes them.

### Notes and reminders

`@note` makes a new note; its first line is the title. After copying some text, ⌃V ⏎ after `@note ` (or ⌘V, outside terminals) saves it with its line breaks, shown as ↵ in the command.
Where it goes is Settings → Commands → Notes (@note) → Save to:

- **Notes** (as before): a new note in the AllInOneIME folder.
- **Folder (Obsidian or any)**: a new Markdown file per note in the folder you choose, named after its first line (`/\:*?"<>|#^[]` become `-`; a name that's taken gets " 2", " 3"). The file holds `created:` front matter, then the whole text as typed. A file is never written over, and a folder that isn't there (an unmounted drive, a moved vault) isn't made: the note comes back instead. In an Obsidian vault (a `.obsidian` folder in it or above it) the notice says "Saved to Obsidian", and the menu bar panel opens the note in Obsidian.
- **Notion**: Create Integration… (New integration → Internal → copy the token), paste the token (kept in the keychain), then in Notion open the page or database → ··· → Connections → add your integration, and paste its link; Test shows "✓ “Inbox” (database)". A page gets a new child page, a database a new row (the first line as its title); the rest of the note is its body, in one request. Offline or refused, nothing is kept to send later: the note comes back. During secure input `@note` doesn't send to Notion.

The notice says where the note went ("Saved to Notion", "Saved to “Inbox”").
If you leave the text field (click elsewhere, switch apps) or press ⇧⏎ (insert as typed) before a note with line breaks is saved, it isn't typed into the app (in a terminal, each line would run as a command): it goes on the clipboard instead ("The note wasn't saved; its text is on the clipboard"). A note of one line is inserted as typed.

`@reminder` reads times like `tomorrow at 3pm`, `in 2 hours`, `in 3 days at 3pm`, `on the 15th`, `this weekend`, `in 1 month`, `next month` (its 1st), `end of the year` (Chinese times too).
The day and the time can be apart (`tomorrow call Bob at 5`); weeks start on Monday.
A time without am or pm (`at 5`) is the next one, never between midnight and 6 a.m.; a time already past today is tomorrow, but a part of the day still going (`this afternoon`, `tonight`) is today, all day; a date already past this year is next year's.
Written to repeat (`standup every Monday at 9`), it is added once, for the next time: the words stay in the title and the row says "once only".
The row to confirm shows the time it read, e.g. "tomorrow 3:00 PM" (following the Mac's 12/24-hour setting); if it's wrong, Esc goes back to the text. With no time or date in it, it has none ("no date").

`@stock` and the like inside these two aren't run: the text is saved as written (typing `@` there doesn't open the command list). The first time, macOS asks whether AllInOneIME may control Notes (`@note`) or access Reminders (`@reminder`): allow it.
If you didn't, allow AllInOneIME in System Settings → Privacy & Security → Automation (Notes) or → Reminders.
When a save fails (no permission, say), the notice says why and the text comes back into the command, to fix and send again; when you have to fix something first (a permission, an account), it's also put on the clipboard (going to System Settings takes the focus from the text field). If you've moved to another text field or are typing something else, it goes on the clipboard instead ("Not saved; the text is on the clipboard.").

### Your own commands

In Settings → Commands, under "Your Commands", click "Add Command…": give it a name and choose what it does (an AI
instruction, a program, a program in Terminal, a web page, a text to insert, or suggestions from a program as you type), or start from an example. Your commands come after the built-in
ones; names are English letters only and can't be a built-in command's; they work from the next sentence.
They're kept in `customCommands` in the config file (`~/.config/allinoneime/config.json`), which you can also edit:

```json
"customCommands": [
  { "name": "python", "type": "run", "argv": ["python3", "-c", "{input}"], "summary": "Run Python" },
  { "name": "bc", "type": "run", "argv": ["bc", "-l"], "stdin": "{input}\n" },
  { "name": "sh", "type": "terminal", "argv": ["zsh", "-c", "{input}"] },
  { "name": "reply", "type": "prompt", "prompt": "Write a short, polite reply to the user's message." },
  { "name": "google", "type": "link", "url": "https://www.google.com/search?q={input}" },
  { "name": "sig", "type": "snippet", "summary": "Email signature", "text": "Best,\nWei\n{cursor}" },
  { "name": "issues", "type": "suggestions", "summary": "Our issues", "prefix": "#", "argv": ["~/bin/gh-issues"] }
]
```

| `type` | What it does |
|---|---|
| `prompt` | Goes to the AI with `prompt` as its instruction; the answer appears in the candidates, to insert or copy (⌘C) |
| `run` | Runs `argv` in the background; what it prints appears in the candidates (several lines are inserted as printed, in a terminal as one line). On an error, its last line is shown |
| `terminal` | Runs `argv` in a new Terminal window; nothing is inserted |
| `link` | Puts the text into the web address `url` and opens it in the default browser; nothing is inserted |
| `snippet` | Inserts `text` at once, with its placeholders filled in (below); no AI, no program |
| `suggestions` | A source of [suggestions](#suggestions-and-code-new): type its `prefix` in any text field and the items `argv` prints show as rows, Tab inserts one ([below](#suggestions-from-a-program-of-your-own-new)). It's not an @ command: it isn't in the command list, and `@issues` is just text; you use it by its prefix |

- `{input}` becomes what you wrote after the command, and it always stays within the one argument it's in: no shell is involved. For a shell, say so, like `sh` above (`zsh -c`).
- `stdin`: what goes to the program's standard input, with `{input}` replaced too.
- A `link`'s `url` must be `https://`, with `{input}` once, after the `?` or `#`; the text is encoded (a space is `%20`, a newline `%0A`), 4000 characters at most.
- `run` and `terminal` type English letters by default (like `@open`; in Chinese mode, Chinese comes back after), and full-width punctuation becomes ASCII. Set `"ascii": false` to keep text as typed.
- Programs run in your home folder with your login shell's PATH (so Homebrew, pyenv and nvm installs are found). `run` stops a program after 10 seconds (`timeoutSeconds`) or when it prints too much; Esc stops it at any time.
- `summary` is the description in the command list (optional).
- When the program in `argv` isn't found (say, no `python3`), the command isn't offered and `@python …` is inserted as text; once it's installed, the command appears in the next text field.

`run` and `terminal` run code on your Mac: only add commands you wrote and trust. They, too, run only when you press the action key, and never during secure input.

#### Suggestions from a program of your own (new)

A `suggestions` command ("Suggestions" in the editor) makes a program of yours a source of suggestions, like a plugin's
completions but without writing a plugin: type its prefix (`#`, `PROJ-`) in any text field and the rows that match show
under the caret; Tab inserts one. You use it by its prefix alone: it isn't in the @ command list, and `@issues` typed is
just text, as a name no command has is; you manage it in Settings → Commands → Your Commands. The program runs as a
`run` command's does (in your home folder, with your login shell's PATH, never through a shell unless `argv` starts
one). Run with no input, it prints every item, one a line, `match⇥title⇥url` (a tab between them; title and url may be
left out), or the plugins' JSON (`{"items": [...]}`, [docs/plugins.md](docs/plugins.md#completions-suggestions)). A line
that isn't one (a match with a space, say) is skipped on its own. This one lists a GitHub repository's issues with
GitHub's `gh` (which keeps its own sign-in):

```sh
#!/bin/sh
# ~/bin/gh-issues: a repository's issues, a "match<TAB>title<TAB>url" line each (Suggestions, prefix #).
# No argument: the open ones; one (Look up as you type): those whose title or number has it.
repo=octo-org/octo-repo
fields='.[] | "#\(.number)\t\(.title)\t\(.url)"'
if [ $# -eq 0 ]; then
  gh issue list -R "$repo" --limit 1000 --json number,title,url --jq "$fields"
else
  gh issue list -R "$repo" --state all --search "$1" --json number,title,url --jq "$fields"
fi
```

```json
{ "name": "issues", "type": "suggestions", "summary": "Our issues", "prefix": "#",
  "argv": ["~/bin/gh-issues"], "refresh": "15m", "query": true, "queryMinChars": 2,
  "insert": { "default": ["{arg} {title}", "{arg}"], "chat": ["{arg} {title} {url}", "{arg} {title}", "{arg}"] } }
```

- `prefix` (required: no source without one, and not the magic key), `minChars`, `compare`, `refresh`, `query`,
  `queryMinChars` and `insert` mean what they mean in a plugin's `completions`, with the same limits and defaults
  ([docs/plugins.md](docs/plugins.md#completions-suggestions)); one out of range keeps the command from being a source,
  and Settings says why. The list runs again every `refresh` (`1h` by default) while you use it; `timeoutSeconds` (10
  by default) is 20 at most, a lookup's 3 seconds.
- With `query` (Look up as you type, from the `queryMinChars`th character after the prefix on), it also runs with what
  you typed after the prefix, as one argument: where `{input}` is in `argv`, else last (`12` for `#12`). Nothing else of
  the field goes to it, and never through a shell or in its environment; for the list, an argument that is only
  `{input}` is left out.
- A line's match is the row's text and what goes in (`{match}`, `{arg}`), its title the row's comment and `{title}`,
  its url `{url}`. Insert in the editor: **Just the match** (`{arg}`, the default), **With its title** (`{arg} {title}`),
  **With title and link** (`{arg} {title} {url}` in chat apps); **Advanced** has the templates as `insert` writes them.
- Rows, keys, the rows you picked first, the list's cache (`~/Library/Caches/AllInOneIME/suggestions/`, readable only by
  you, deleted with the command), back-off and pause are a plugin's. It's yours: no switch to turn on, it's on while it
  exists; the **Suggestions** switch (Settings → General, the input menu) applies. The editor shows
  how it's doing (last updated, items, last error) and Refresh Now, and so does its row in Settings → Commands → Your
  Commands.
- Its name is a custom command's as before: letters only, and no other custom command, built-in command or plugin may
  have it (a script extension of that name stays left out, as before).
- Custom commands sync through iCloud as they do; a program missing on another Mac is that source's error there. One
  that comes from another Mac runs nothing on this Mac until you allow it here once: Settings → Commands → Your Commands shows it
  as from another Mac, with the program it would run, and **Allow** or **Remove** (a notice says when one comes).
  Allowing is this Mac's own, never synced; its program changed on another Mac asks again; one you make or edit on this
  Mac never asks.

#### Snippets: text you insert often (new)

A `snippet` command ("Insert text" in the editor) inserts text you saved, such as a signature, an address or a meeting
link: `@sig` ⏎ puts it in at once (Tab or Space only complete the name). Its `text` can hold placeholders:

| Placeholder | Becomes |
|---|---|
| `{input}` | everything you wrote after the name: `@tag foo bar` with `#{input}` inserts `#foo bar` |
| `{name?}` | a blank, filled from what you wrote, separated by commas (`,` or `，`), in order: `Dear {name?}, see you {day?}.` with `@meet Bob, Friday`. One left empty is named in a notice, and nothing goes in |
| `{clipboard}` | the clipboard's text (macOS may ask first) |
| `{selection}` | the text selected when you typed `@` (it's replaced, as by any command on the selection) |
| `{date}`, `{time}` | today as `2026-10-17`, the time as `14:05`; `{date:EEEE, MMM d}` with a [date pattern](https://unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table), in the interface language |
| `{cursor}` | where the caret goes after it's in (once at most; not in a terminal) |

- `{{` writes `{`, and the `}}` that closes it writes `}` (`{{input}}` inserts `{input}`); any other `}}` or `{…}` stays
  as it is, so JSON or code in a snippet is fine: `{"a":{"b":1}}` goes in as written.
- With no `{input}` and no blanks, what you write after the name goes in after the snippet, after a space.
- Write `@sig` inside another command's text to include it: `@question summarize this @zoom` sends the link itself. Only
  snippets with no `{clipboard}`, `{selection}` or blanks work there; with `{input}`, it's one word or a quoted phrase:
  `@meet「Friday 3pm」`.
- Plain text only (line breaks kept), at most 20,000 characters. Snippets stay on this Mac, so they work during secure
  input and in apps set to No AI. Extension bundles can ship them too (`snippets` in `extension.json`, see
  [docs/extensions.md](docs/extensions.md)).

### Script extensions

Add your own commands as programs: a script in any language (bash, Python, Node, Swift, …) with a few lines of
metadata in its comments. Put it in `~/.config/allinoneime/extensions`, or in a folder you add under Settings →
Commands → Script Extensions. Raycast Script Commands work as they are, and folders that already hold them are
found with Spotlight.

```bash
#!/bin/bash
# @allinoneime.schemaVersion 1
# @allinoneime.title Flights
# @allinoneime.argument1 {"type": "text", "placeholder": "from city"}
# @allinoneime.argument2 {"type": "text", "placeholder": "to city"}

echo "Flights from $1 to $2"
```

`flights.sh` is `@flights`. Write its arguments after it, commas between: `@flights beijing, new york` runs it with
`beijing` and `new york` as `$1` and `$2` (more commas stay in the last one); a required one left empty says what's
missing instead of running. What it prints is used as its `output` says:

| `output` | What happens |
|---|---|
| `insert` (default) | All of it, and each line, to insert |
| `show` | Shown in the panel as it prints (progress); nothing inserted. Leave the field and it goes on in the background (up to four at once) |
| `list` | A list in Alfred's Script Filter JSON, run again as you type; picking a row inserts, opens (a web address, file or folder; never something that would run), copies or runs a second step |
| `silent` | Its last line near the cursor; nothing inserted |

A command can also take no input (`input none`: ⏎ on its name runs it), run in the `background` and notify you when
it's done (the menu bar panel lists it meanwhile), show a `status` beside its name in the command list, or ask first
(`confirm`). It runs in its own folder with your login shell's PATH and `ALLINONEIME_*` variables: the interface and
input language, the app you're typing in, the text. A **bundle** is a folder with an `extension.json` naming its
commands: they share code and preferences, which Settings shows (passwords go to the keychain). Settings lists every
command with a switch, and the scripts left out with why.

Raycast's modes map as `fullOutput` → `show`, `compact` and `silent` → `silent`, `inline` with `refreshTime` → a
status. The whole protocol is in [docs/extensions.md](docs/extensions.md); [Core/Examples/extensions](Core/Examples/extensions)
has one of each kind. Extensions run code on your Mac: use ones you trust. They run only when you run them (a status
or a list as you type it), never during secure input, and stop when the input method quits.

#### Extension sources (new)

A bundle can come from a Git repository, yours or your team's, and stay up to date from there. Settings →
Commands → Extension Sources → **Add from Link…**: paste the repository's address (`git@github.com:you/my-extensions.git`,
`ssh://…`, `https://…`; optionally a branch, the bundle's folder in the repository, and a tag or commit to pin it to).
AllInOneIME clones it with **your own git and SSH setup** (keys, agent, ~/.ssh/config, credential helpers), so a
private repository works as it does in Terminal; the app never asks for or stores a password. The clone goes into
`~/Library/Application Support/AllInOneIME/Sources/`: first into a hidden staging folder, never straight into an
extensions folder. (Don't put a name, password or token in an https address: git's credential helper keeps them.)

- **Review first.** Before anything loads you see the bundle, every command (name, title, description, output), the
  programs they run, its preferences, and the commit, under the warning "This source isn't signed: it will run
  programs from <address>". Only **Enable** adds it; Cancel deletes the clone. You review a source once.
- **Updates are yours to apply.** Once a day (and soon after the input method starts) a source is fetched to see what's
  new: Settings shows "N updates" with the commits (subject, author, date) and a badge on the Commands page. Nothing changes
  until you click **Update**, which only fast-forwards and runs no hooks. A force push makes the source need a review
  again: **Re-clone** shows it, and only Enable puts the rewritten history in place (until then the reviewed version
  keeps working).
  A source pinned to a tag or commit isn't checked. Turn the daily check off per source (`autoCheck`).
- **Suggestions after an update.** A bundle's suggestions (its commands as
  [completion sources](#suggestions-and-code-new)) are on once you enable the source, pinned to what it was then: an
  update that changes any file of the source's repository (not only the bundle: a script may use files elsewhere in it),
  or a source's prefix or lookup, turns them off until you turn them on again, and Settings says so; one an update adds
  waits until you turn it on. A repository of more than 2,000 files or 20 MB can't be checked for changes, so its
  suggestions can't be on. **Trust its updates** (under each source, off by default) keeps them running after its
  updates, one an update adds on too, and nothing of the repository is checked for them: turn it on only for a source
  you trust, such as your team's repository. Turning it on also turns on those a change turned off or an update added
  (never one you turned off); turning it off turns nothing off until the next change (`trustUpdates` in the config).
- **Errors** are git's own words, with "This uses your own git and SSH setup; check that `git ls-remote <url>` works in
  Terminal", and your own reminder under it if you set one (`authHint` in the config).
- **Remove** moves the clone to the Trash; the bundle's preferences are kept for next time.
- From a terminal: `AllInOneIME --add-source <url> [--path …] [--branch …] [--pin …]` (prints the review and enables
  it; again after a force push), `--update-sources` (fast-forwards every reviewed source that isn't pinned),
  `--list-extensions` (on `~/Library/Input Methods/AllInOneIME.app/Contents/MacOS/AllInOneIME`).
- Only reviewed code loads: a source folder in the load list that wasn't reviewed on this Mac (a copied config) is left
  out. git never waits for an answer: no terminal and no prompts, so an unknown host key or a password prompt fails at once.

The config keeps them as `extensionSources`; the repository layout is in [docs/extensions.md](docs/extensions.md#10-extension-sources).

### Plugins

Plugins are ready-made `@` commands for things not everyone needs, like `@stock AAPL 600519 700` for stock quotes.
Installed, they work like any command; Settings → Commands → Plugins shows what's installed and where each sends your
text, and removes them. Plugins are JavaScript run in a separate process: they can reach only the websites they declare
(HTTPS), and can't read files or run other programs. "Browse Library…" under Plugins installs them
from the [plugin library](https://github.com/MicroZ-LLC/AllInOneIME-plugins): it shows which websites a plugin
contacts before installing; the library's index is signed and every file must match it. A newer version shows an
"Update" button; nothing updates by itself. Your own plugins go in `~/.config/allinoneime/plugins/` ("Open Plugins
Folder"): local plugins, never overwritten by the library.
"Link" plugins run no code: they put the text into a web address and open it in the browser, like `@x nice weather
today`, which opens X's composer with the text filled in; posting is up to you on the page. The library has four
(`@x`, `@threads`, `@bsky`, `@weibo`). `@xe` converts currencies: `@xe 100 USD CNY`, `@xe 1000 JPY EUR`, one line
with the date of the rate (rates by ExchangeRate-API). `@calculator` is a calculator that works offline,
`@calculator 23*17` → `391` (the built-in `@calculate` before 0.6.5), and `@calendar` does dates: `@calendar +10` →
"Tue, Oct 27 · in 10 days". Writing one: [docs/plugins.md](docs/plugins.md).

Plugins can also complete what you type (new): `@github`'s issues come up as rows as soon as you type `#12`, and Tab
inserts `#1234 Fix login`. Each plugin's completions are on once you install it (0.6.7.2); under it in Settings → Commands →
Plugins a switch for each says what they do and, for one that looks things up as you type, where what you type after `#`
goes, and one you turn off there stays off. See [Suggestions and Code](#suggestions-and-code-new).

Commands that fetch something (plugins and programs) also work inside a sentence: `@reply tell her @stock AAPL is up today`.
The inner ones run first, their output takes their place, and the outer command works on the result. The argument is
the word after the command, plus the uppercase codes or numbers right after it (`@stock AAPL TSLA`, `@stock 600519 700`);
a lowercase word ends it (`@stock SNDK is good to buy` looks up SNDK). Quotes mark it exactly: `@stock "aapl tsla"`.
The `@calculator` plugin works there too: `@reply the total is @calculator 23*17 dollars`.
Inside `@agent` and terminal commands they aren't run: those get the text as written (typing `@` there doesn't open the command list).

### Action key

⏎ by default; change it in Settings → General → Action key (`actionKey` in the config): click it, then press the key, as
for a keyboard shortcut in System Settings: Tap ⌥ (either side: press and let go right away), ⌥Space, Space (press
Space once more after the words are picked; twice in English mode), or a shortcut such as ⌃⏎, ⌘⏎ or F5 (a key that
types needs ⌃, ⌥ or ⌘).
Whatever the action key, commands also run on ⏎. If ⌥Space is already a shortcut for Alfred, Raycast or the like,
they get it first.

### Typing results out

Turn on "Type results out" under Settings → Advanced (`typeOut` in the config) and a command's result is typed into the
app character by character, like a person typing, instead of going in at once; pinyin picks still go in at once. The
slider sets the pace, from 6 seconds a character to 40 a second (`typeOutRate`), and "Speed up and slow down (like a
person)" types in bursts of changing pace (`typeOutVaries`). Esc stops it where it is; any other key types the rest at
once.

"Make occasional typos and fix them" (`typeOutMistakes`) makes it look even more like a person: now and then the key
next to the right one, noticed up to three letters later, deleted and typed again; a letter or a space typed twice and
deleted; or a short word typed, deleted and typed again. A few in 100 characters, never two close together, and never
at the start of a line. In code, web and email addresses and numbers, a typo is only a wrong letter or digit, fixed at
once (never a wrong bracket, quote or space, which editors pair or indent on). The wrong letters are neighbors on your
keyboard layout (QWERTY, AZERTY, QWERTZ…). Chinese, Japanese and Korean only hesitate (two characters typed, deleted
and typed again), never with a wrong character.

In a field that takes typos back (Apple's text views such as TextEdit and Notes, browsers, most editors): typed to
the end, or with another key pressed to type the rest at once, the text is exactly the result; Esc (or leaving the
field) in the middle of a typo takes the typo out first, so the field holds an exact start of the result. If the
cursor moves while a typo shows (a click), the typo is taken out where it was and the rest is typed without typos.

Typos are never made in terminals, nor in apps that don't tell the input method where the cursor is. Each time, the
first typo is a plain one (a wrong letter, corrected in one go), until the field has shown it takes a typo back; while a
typo shows, the input method checks before every key that the field holds what it typed. A field that ignores where
to replace text can't take a typo back: there that first typo stays, so the text ends up one character off (also
after Esc or another key), and the app gets no typos again. Settings → Privacy → Learned… lists those apps; Forget
lets one try again. They're kept on this Mac only, with the rest of what it learns (see Privacy).

### Per-app settings (new)

An app has two settings of its own; everything else is the same in every app:

| Setting | Where | In the config |
| --- | --- | --- |
| What a suggestion row inserts there: with title, or with title and link; or Off, no suggestions there | Settings → General → Suggestions → "In these apps" | `suggestionsInsert` (synced with the settings); Off is `"suggestions": false` (this Mac's own: not synced) |
| No AI: `@improve`, `@translate`, `@question`, `@agent` and your prompt commands send nothing there and say so; typing and the other commands work | Settings → Privacy → "Apps without AI" | `noAI` |

"Add App…" lists the apps you typed in lately, or picks one in /Applications; Remove takes an app off that list (its
other setting stays). Off in "In these apps" keeps what the app's rows inserted, for when you pick one again. The input
menu's "This App: <name>" has the same two for the app you're typing in: No AI and, with a suggestion source, what a row
inserts there, or Off. In the config they're under `appProfiles`, by bundle ID:
`"appProfiles": {"com.tinyspeck.slackmacgap": {"suggestionsInsert": "titleAndLink"}, "com.apple.Terminal": {"noAI": true}}`.
Bundle IDs match ignoring case (`com.apple.Mail` is Mail's `com.apple.mail`). `@reportissue` counts the apps that set
something, never naming them.

- **Where an app starts is learned.** Switch the input with Shift before typing anything in a field, to the same input
  in two fields of an app in a row, and that app's text fields start in it from then on; it says so once ("Slack starts
  in English from now on"). Only such switches count, never one in the middle of typing; Code counts like a language.
  Learning never changes the default input (the first chip). To change what an app learned, do the same with another
  input; to forget it, the input menu's This App shows "Starts in English (learned)" with Forget, as does Settings →
  Privacy → Learned…. What is learned stays on this Mac (see [Privacy](#privacy)).
- **Previous per-app settings.** What an earlier version set for an app, and Settings doesn't set any more, still works
  while it's set: the input it starts in (`inputLanguage`; one the app learned comes first), Always Translate as You
  Type (`translateAlways`), autocomplete always or never (`autocomplete`), typing out or not (`typeOut`) and its rewrite
  styles (`rewriteStyles`). Settings → General → "Previous per-app settings", there only while an app has one, lists
  them, a row per app, and Remove clears them for that app (its Insert, Off too, and No AI stay). An app set to no
  suggestions in an earlier version (`"suggestions": false`) is under "In these apps", at Off.
  Nothing in `config.json` is renamed or removed by 0.6.7, and these values sync as they did.
- With No AI, the AI commands stay in the command list; running one shows the notice and keeps what you wrote. Your own
  terminal commands (`"type": "terminal"`) run programs, not the AI, so they still work there.

### Settings (new)

Settings has seven pages, in this order in the sidebar, and opens on General:

- **General**, from the top: the magic key and the action key; Show in Menu Bar and the interface language; Translate
  to, the rewrite styles, "@improve also translates" and the jargon list (shown with the Jargon style, or once a list
  is set); Autocomplete (Beta); Suggestions, with Insert and "In these apps"; Clipboard history, with Keep the last, whether
  macOS lets it record and Clear History; Sync through iCloud; and Previous per-app settings, only while an app has one.
- **Input**: the input languages as chips at the top: drag to reorder, ⊗ removes one, Add… adds one; the first is the
  default, and Code comes after them ("Code · Python"). Under the chips, each input has its options in a section under
  its name, always shown, with nothing to click. English has its words; Chinese (pinyin) its language pack and fuzzy
  pinyin, then Personal Dictionaries; Code its coding language, the coding languages installed and the coding language
  library. A chip's context menu has Move Left and Move Right too. A language pack's problem shows its banner on this
  page.
- **AI**: the provider, its model, its key or AWS profile, and Test Connection; the base URL is under More…, which opens
  by itself once one is set.
- **Privacy**: hiding sensitive information before sending, the words to hide, Apps without AI, what `@agent` and
  `@reply` take from Chrome, remembering recent questions (with Forget), and learning English words.
- **Commands**: your commands, the agent `@agent` hands to, where an `@question` conversation continues, `@note` and
  `@search`, plugins, script extensions (folders that bring no new commands fold into one row) and extension sources. A
  plugin or script extension command with suggestions has their switch under it, and **Show in the @ list** next to it.
- **Advanced**: typing results out (speed, typos), the candidate layout, "Use the selected text", the config file and
  the Rime folder.
- **About**: the version, updates and "Check for updates automatically", Troubleshoot…, Report an Issue… and links.

A few settings have no row unless they're set to something other than their default (by hand in the config file, or by
an earlier version): the output tokens, temperature, timeout and Thinking (AI), a kind of sensitive information left out
(Privacy), the settings or the jargon list and custom commands not synced (Sync through iCloud), and Insert's "ID only".
Then their row shows, with Restore Default. Shown or not, they work as before.

**Search.** Type in the field at the top of the sidebar and it lists the settings that match as you type (by name, by
what the row says and by the words they go by, in English and Chinese), each with its page; ↑↓ choose one, and ⏎ or a
click shows it on its page, outlined. The search sends nothing. Its last row, **Change: …**, asks the AI to change the
settings as you wrote (the Assistant page before 0.6.7, `@config` before 0.6.5): "translate into Japanese and English",
"微信里不用 AI", "candidates in a column", "turn off the typos", "use Claude". The changes show at the
top of the page, a row each, old → new, with the labels Settings uses ("Translation languages: English, Japanese →
English, French", "Apps · WeChat · No AI in this app: off → on"); nothing is changed yet. Apply writes them,
Cancel drops them. "Changed N settings" then has Undo for 10 minutes, which puts back exactly the values those settings
had (one you changed since is left as it is, and named).

<img src="docs/en/settings-search.png" width="520" alt="Settings: a sentence typed in the search, and Change's preview at the top of the page, a row each, old → new, with Apply">

- **What it can change:** the translation and input languages (and the default one), the rewrite styles, the candidate
  layout, typing results out (on/off, speed, speeding up and slowing down, typos), Autocomplete (on/off: "turn on
  autocomplete"; the row says where its text goes), using the selection, remembering
  questions, hiding sensitive information (on/off, what is hidden, words to add), checking for updates, syncing through
  iCloud (on/off; what syncs only in Settings), an app's two settings, No AI and Insert (with title, with title and
  link, or as everywhere; an app named as you call it, found among your apps by name or bundle ID), and the AI provider: which one, the Bedrock
  profile (from `~/.aws`) and region, a model the app knows for it, and an OpenAI-compatible base URL (`https://` only).
- **Not per app any more:** asked where an app starts, its rewrite styles or typing out, it changes nothing and says
  why: where an app starts is learned (switch with Shift before typing, in two of its fields in a row), and the rewrite
  styles and typing out are set for every app. An answer that still sets one of them for an app is refused in its row,
  with that reason, and never written.
- **What it never touches:** API keys and anything in the keychain, custom commands, extension folders and sources,
  plugins, the jargon list, anything that runs programs, and every other setting. Those rows are refused, with the
  reason, and the rest can still be applied.
- **Checked like Settings:** a language that isn't one, more than 5 translation languages, a value out of range, an app
  it can't tell, or a language whose pack isn't installed is refused row by row; an invalid config is never written.
- **Keys:** it never switches to a provider that has no key (none in the keychain or your shell): the row says the key is
  needed, and applying opens Settings → AI at that key (Save, or Save and Use to switch to it), while the other
  rows still apply. With a key, the provider switches, and Test Connection runs and shows its result with the preview. A key
  typed into the request is dropped before anything is sent.
- **On this Mac first:** it uses Apple Intelligence whenever this Mac has it (macOS 26), whatever provider you chose and
  even before one is set up, held to the allowed settings and values, with lookups for your apps, AWS profiles and
  language packs. Without it, your provider answers.

**Troubleshoot.** Settings → About → **Troubleshoot…** (Check for problems before 0.6.7, `@doctor` before 0.6.5) checks
the setup on this Mac and lists ✗ problems first, then ⚠ warnings, a row each; what is fine is folded under one green
line ("Everything looks good", or "10 more look good" under the problems), opened by clicking it (a ✓ row each). Under
it in About, one line says the same ("Everything looks good", "2 things to look at"). The checks run as Settings opens
or comes back to the front, and as Troubleshoot… opens; they ask for no permission, read no key and call no AI. What
they find wrong also shows at the top of the page it's about, as a banner, with a dot by that page in the sidebar: red
for a problem, orange for a warning. It checks the input method (installed, enabled, in your input sources), the AI
provider (its key saved or the Bedrock profile's credentials found, never read or shown; Apple Intelligence), the
permissions (Accessibility, controlling Notes, Reminders, Terminal and Messages, asked of macOS without a prompt), secure
input, the language packs of your input languages, `config.json` (readable, unknown keys, values out of range, a language
twice, more than 5 translation languages), extensions and plugins that didn't load, updates, sync through iCloud (on or
off, when it last synced, the last error, iCloud Drive not available, settings from iCloud not used here), and recent
errors in the app's own logs. **Check** runs them again with Test Connection; with something in "What's wrong?
(optional)" ("why doesn't translate work"), the AI then explains the likely cause from the results and marks the fixes
it suggests.

A row that can be fixed has a button that says what it does: Add Key…, Download, Open System Settings, Review Changes…,
Copy Command, Check for Updates. Review Changes… shows the settings it repairs as a preview, with Apply and Undo; the
others act at once: enabling the input method again, opening a System Settings pane, downloading a language pack,
Settings' key field, Check for Updates, or copying a command for Terminal ("Copied"). No fix deletes your data or
touches a key.

### Sync through iCloud (new)

Settings → General → **Sync through iCloud** (off by default) keeps your settings, jargon list, custom commands and the
words pinyin learned the same on all your Macs, through your own iCloud Drive: nothing else to sign in to, nothing through
our servers. It needs iCloud Drive (System Settings → Apple Account → iCloud); without it the switch stays off and says
so, with a button that opens that pane.

Once it's on, Settings shows one status row with a ⋯ menu (Sync Now; API keys and passwords; Remove Hidden Words from
iCloud…, Remove Recent Questions from iCloud… and Remove from iCloud…), and two switches under it: Learned words, and
Hidden words and recent questions.

| What | What syncs | Default |
| --- | --- | --- |
| Settings | the settings in `config.json`: languages, rewrite styles, the action key, the magic key, typing out, per-app settings, hiding sensitive information (its switches), the AI provider and model (never a key) … | on |
| Jargon and custom commands | your jargon list and `customCommands` | on |
| Learned words | what pinyin learned from your choices (Rime's user dictionary, through librime's user-dictionary sync), words picked from a personal dictionary too, and your English words, added or learned (`englishWords`); your own Rime files, such as custom phrases, and the personal dictionaries themselves stay on the Mac | on |
| Hidden words and recent questions (one switch) | the words you hide from the AI, and `@question`'s recent questions and answers (while "Remember recent questions" is on); iCloud Drive is end-to-end encrypted only with Advanced Data Protection | off |
| API keys and passwords (in the ⋯ menu) | your API keys and extensions' passwords, through iCloud Keychain, which is always end-to-end encrypted (needs Passwords & Keychain on in System Settings → Apple Account → iCloud) | off |

Settings and the jargon list and custom commands have no switch: they sync unless the config file says otherwise
(`"settings": false`, `"jargon": false` in `iCloudSync`), and then Settings shows them, with Restore Default. A config
with only one of hidden words and recent questions on (from before they were one switch) keeps it, and Settings says
which.

`iCloud Drive/AllInOneIME/settings.json` holds each setting with when it changed and on which Mac (a random id), and per
setting the newest change wins: a list (your custom commands, the rewrite styles) is one value, per-app settings go app
by app, and removing an app's settings is a change too. It syncs when the input method starts, about 5 s after you change
something, when iCloud brings a change from another Mac (and every 5 minutes), and on **Sync Now**; the learned words when
the input method starts, every 30 minutes (after a pause in typing) and on Sync Now. The status line says "Last synced
2 min ago", "Waiting for iCloud…" or the error.

- Turning it on, a Mac takes the settings in iCloud already; its own fill in only what isn't there yet. Its
  collections are merged instead: recent questions (both lists, newest first, a question once), hidden words, custom
  commands (by name; iCloud's on a clash) and the jargon list's lines. The same when a switch under it is turned on for
  the first time. What you take out on another Mac afterwards (a custom command or hidden word deleted) stays out. It
  comes back once, and deleting it again sticks, when it came from the first Mac that turned sync on and that Mac was
  asleep while another Mac merged its list in, when it was deleted on a Mac still on 0.6.4, or when a Mac still on 0.6.4
  brings it back. A setting saved in Settings while a Mac is turning sync on is kept, and goes to the other Macs.
- Turned back on after it was off: what iCloud changed meanwhile comes in (also where this Mac changed it too), what only
  this Mac changed goes up, and a collection it added to meanwhile is merged, never dropped.
- Recent questions of two Macs are merged; "Forget" on one Mac forgets every question asked before it on the others too.
  Turning "Remember recent questions" off deletes them on that Mac only, and turned on again, the other Macs' questions
  come back to it. A Forget made while a Mac doesn't sync the recent questions (or doesn't remember them) is that Mac's
  alone.
- Turning off hidden words and recent questions leaves what was synced in iCloud: **Remove Hidden Words from iCloud…**
  and **Remove Recent Questions from iCloud…** in the ⋯ menu (asked first) take them out; other Macs keep theirs, and one
  that still syncs them puts its own back.
- A value from another Mac that this one can't use (a provider without a key here, an AWS profile it doesn't have, a value
  out of range) isn't applied: the status line and Troubleshoot (Settings → About) say which.
- A file iCloud hasn't downloaded yet is waited for, never taken as empty; a `settings.json` that can't be read is set
  aside as `settings (unreadable …).json`, never overwritten. Settings of a newer version are kept as they are.
- A custom `suggestions` command from another Mac runs nothing on this one until you allow it once in Settings → Commands
  → Your Commands, which shows the program it would run (a notice says when one comes); a change of its program on another Mac
  asks again. What you allowed stays on this Mac. `run` commands are as they were: they run only when you run them.
- API keys and passwords go through iCloud Keychain, not iCloud Drive: with "API keys and passwords" on (in the ⋯ menu,
  while sync is on), a key saved or replaced on one Mac is there on the others. It's off by default: turning on sync alone moves no
  key, and nothing moves until you turn the row on. Turning it on moves this Mac's keys from the login
  keychain into iCloud Keychain (macOS then no longer asks for your login password for them after an update); turning
  it off copies them back into the login keychain and leaves them in iCloud Keychain for your other Macs. Keys that don't
  sync stay in the login keychain, as before, and so does the AllInOneIME Cloud sign-in, which never syncs: each Mac
  signs in itself. When two Macs have different keys, the one saved last wins (by when it was saved, which every copy
  keeps). The other isn't deleted: it's kept in its Mac's login keychain as a replaced copy (under "AllInOneIME replaced
  API key", its name ending in "(replaced)"), which is never used. A key that moves into iCloud Keychain keeps one too,
  in case another Mac's different key arrives over it. There is one replaced copy per key on each Mac: a later one
  replaces it. Removing a key while it syncs removes it on every Mac that syncs keys (the question says "all your Macs"),
  and this Mac's replaced copy; a Mac with "API keys and passwords" off, or one still on 0.6.4, keeps its own copy, and
  puts it back if key sync is turned on there later (the question says so too). On a Mac with it off, Remove… removes the key and its replaced copy from that Mac only (the
  question says "this Mac"), and the copy in iCloud Keychain stays for your other Macs. A key that macOS wouldn't let
  AllInOneIME read without your login password when it was to move stays in the login keychain until it's next used:
  if macOS then asks and you allow it, it's used again, even if it was removed on another Mac. Each key still goes only
  to the host it was saved for. While keys sync, `allinoneime-cli` and versions before 0.6.5 don't see them in the
  keychain. A build without the provisioning profile (a development build) keeps keys in the login keychain and can't
  sync them: the row says so.
- Never synced: the AllInOneIME Cloud sign-in, AWS credentials (in `~/.aws`), extension sources (they run code: each Mac decides),
  extension folders and plugins (paths on each Mac), what the input method learned on this Mac (see Privacy) and the
  recent apps, window state, Autocomplete (its switch and each app's choice: each Mac's own), Suggestions' switches (General's and each app's), the plugins'
  completions turned on and their preferences (`completionSources`, `pluginPreferences`), the custom commands from
  another Mac still awaiting Allow (`unconfirmedCommands`), clipboard history and its settings (`clipboardHistory`,
  `clipboardHistoryLimit`), and the sync switches themselves (each Mac's own). What a
  suggestion row inserts and Code's language do sync, with the settings.
- Turning it off stops syncing and leaves everything as it is, on this Mac and in iCloud; **Remove from iCloud…** in the ⋯
  menu (asked first) moves the folder to the Trash and turns sync off on this Mac.
- The settings search's Change: … ("sync through iCloud") turns it on or off; what syncs is only chosen in Settings →
  General. In the config: `iCloudSync` (`enabled`, `settings`, `jargon`, `learnedWords`, `hiddenWords`, `recentQuestions`, `keys`).

## Menu bar panel

<img src="docs/en/panel-swipe.png" width="520" alt="The menu bar panel: frosted glass, with notes, reminders and Claude tasks on cards; a row swiped left shows its Remove button">

Click AllInOneIME's icon in the menu bar (the ∞-and-cursor mark, without a box; the boxed one is the input source) and the panel drops down under it; a click elsewhere closes it:

- Autocomplete: its switch, on top, with the model it asks, where the text goes and how many suggestions were shown and taken (see [Autocomplete](#autocomplete-beta-new)).
- Notes: the notes saved with `@note`, the newest 5; click one to open it where it went: in Notes, in Obsidian or the file's own app, or the Notion page. A file that's gone is no longer listed.
- Reminders: the reminders not done yet in the AllInOneIME list of Reminders (`@reminder` adds to that list), the soonest due first, 8 shown; click the circle to tick one off, or the title to open Reminders.
- Claude Tasks: like `@tasks`, the background Claude tasks (what `@agent` hands off to Claude Code), up to 30, 5 shown at a time: scroll for more, or search their titles and replies in the search box; with their progress and the first line of the last reply; click one to open it in Terminal and go on.

Swipe a row (a note, a reminder or a task) to the left with two fingers to show its Remove button, or all the way to remove it at once; with a mouse, right-click it. Removing only takes it off the panel: the note stays in Notes, the reminder in Reminders (not completed), the task in Claude Code.

The header has the counts (like "2 reminders · 1 task running"; tasks waiting for you are counted apart, like "1 waiting for you") and a refresh button.
It never takes the focus from the app you're typing in: ticking off a reminder or refreshing leaves that app in front; only the Claude tasks' search box, once clicked, takes the keyboard.
The icon is shown by default; turn it off with "Show in Menu Bar" in Settings → General.

What it reads, and when:

- Notes: the list is the panel's own record (kept while it's closed too), and Notes is never launched: only when Notes is running already, and AllInOneIME was allowed to control it before, does the panel check it for edited titles and deleted notes.
- Reminders: the AllInOneIME list is read when the panel drops down, every 60 seconds and when reminders change. The panel never makes macOS ask for access by itself: if macOS hasn't asked you yet, it shows "Allow Access to Reminders", and only that button asks; if you said no, it shows "Open System Settings".
- Claude tasks: the panel runs `claude agents` only while it's down: once when it drops down, on Refresh, and when `@agent` hands off a task; and every 15 seconds while a task isn't done yet, no longer once they're all done. The last replies are read from the end of Claude Code's transcripts on this Mac (`~/.claude/projects`), and only when a transcript has changed.
- While it's closed, none of this runs; it only keeps a record of the notes `@note` saves.

## Input and translation

In Settings → Input:

- **Input languages**: one to five of English, Chinese (pinyin), French, Korean and Hindi, as chips at the top: Add… adds one (up to five), drag a chip to reorder, ⊗ removes one. Each one's options are in a section under its name, below the chips. A new install starts with English only. New text fields start in the first; tap Shift for the next, in their order; with one, Shift doesn't switch.
  - **French** types with its own keyboard layout: AZERTY unless you pick another in its section. Its dead keys (^, ¨, `, ´, ~) compose from it too.
  - **Korean** types Hangul in the 2-set (Dubeolsik) layout, each syllable put together as you type (g k s → 한); Shift gives ㄲ ㄸ ㅃ ㅆ ㅉ and ㅒ ㅖ.
  - **Hindi**: type the words as they sound in Latin letters and get Devanagari (namaste → नमस्ते). Common words are spelled as Hindi writes them; otherwise Space inserts the first spelling, a digit another, ⏎ the letters as typed, and "." the danda (।).
  - A command's name, `@open`'s text and code (`@py`, `@js`) are typed in letters whatever the language; it comes back after the command.
  - `@improve` keeps a Korean, Hindi or French sentence in its own language, and `@translate` translates it into your languages (French is told apart from English when it's one of your input languages).
- **Code** (new): an input for writing code, after the languages and apart from them: added with Add… → Code, its chip after the languages ("Code · Python"), with its coding language (Python, Java, Go, TypeScript, JavaScript, C or C++). Tap Shift through the languages, then Code (Chinese → English → Code). You type letters, and the rows offer that language's keywords and snippets; see [Suggestions and Code](#suggestions-and-code-new).
- **Language packs**: the app comes with English (and French, which needs only macOS's layout). Chinese, Korean and Hindi are packs you download when you add them: adding Chinese (pinyin) downloads its dictionaries (about 34 MB, 125 MB unpacked) with a progress bar, and pinyin works as soon as it's done, without a restart; Korean's pack (its key table and how jamo make syllables) and Hindi's (its letters and common words) are a few kilobytes. A pack is data only (dictionaries, tables and schemas, never code), listed in a signed index and checked against its SHA-256 before it's used, like plugins. Each language's section shows its pack (version, size, where it came from) with Remove…, and removing the language offers to remove its pack. Updating from 0.6.1 or earlier keeps Chinese without a download: the installer keeps the dictionaries the old version came with.
- **Candidate layout**: for picking words, pinyin and Hindi candidates are side by side by default (Horizontal), like the system's own input methods: ← → choose and ↑↓ (or - =) turn the page. Choose Vertical in Settings → Advanced → Candidate layout for one under the other (↑↓ choose). The command list and the results are always vertical.
- Candidates, notices and the Translate as You Type chip appear without window animations. Committing a word hides its candidates immediately; the window is reused during continuous typing and closes after 400 ms of idle time.
- **English words in pinyin** (with Chinese input): type a few letters and the English words they start come up among the candidates: bedr → Bedrock, and bedrock → Bedrock first (Space puts it in). Besides rime-ice's own English words: yours (English Words, in English's section, or in Chinese's without English: you add and remove them there), the English terms of your jargon list, and about 220 product and technical words rime-ice lacks (Bedrock, SageMaker, DynamoDB, LangGraph…). A word whose letters are all you typed comes first, unless they're pinyin too (xiaomi: second); a longer one second, or after the page while what you type may still be pinyin. The same letters put in as typed twice (bedrock ⏎, or a tap of Shift) are learned, with no command, and so is a word you type twice in English mode (after a tap of Shift; English mode itself is as it was, nothing shows there); the first time they're only remembered, until the app quits. In English mode a word is the letters between a space or a mark and a space, ⏎, a mark or a tap of Shift back to Chinese; not one you edit with ⌫ (while typing it or right after), one with a digit or a mark inside (example.com, don't, abc123), or one with a capital first (a name, a sentence's first word). Never in password fields, terminals and SSH clients, remote desktops and virtual machines, password managers, or apps with No AI (a terminal inside an editor, VS Code's say, can't be told from the editor), never pinyin (rime-ice's corrected spellings too: zhogn; and your fuzzy pinyin), nothing that looks like a key or a number or holds one of your hidden words (switch: Settings → Privacy → "Learn English words"). A word you add that looks like a key, a card or phone number or an IP address is refused; adding one it learned makes it yours. They sync through iCloud with the learned words, merged by their letters; past 2,000 the oldest learned go first, never one you added. Privacy: learning looks at every word you type in English mode, on this Mac only, and sends nothing anywhere for it (no AI either); a word typed once stays in memory until the app quits, a word learned goes into your config file (`englishWords`) and leaves this Mac only when Sync through iCloud is on with the learned words (Settings → General), as the other learned words do. What the guards can't tell from a word (a password in a field that isn't a password field, all small letters, typed twice) could be learned: the list in Settings shows every word, ✕ removes one, and the switch turns learning off.
- **Fuzzy pinyin** (with Chinese input): sounds you don't tell apart typed either way, e.g. z ↔ zh, n ↔ l, in ↔ ing. Under Chinese (pinyin), turn on "Fuzzy pinyin" and pick the pairs; the dictionaries are deployed again in a second or two. It writes `rime_ice.custom.yaml` in the Rime user folder, and never over a file of your own there.
- **Personal dictionaries** (Chinese input): Chinese (pinyin) → Personal Dictionaries → **Import or Update…** adds a UTF-8 Rime `.dict.yaml` vocabulary file alongside rime-ice. The list shows its Rime `name`, source filename and entry count; importing the same `name` again replaces its saved copy. Editing the source alone doesn't update it. Import, update and removal redeploy automatically, and Settings reports deployment progress or errors. Each one compiles pinyin's dictionary again (all of rime-ice's words with yours), which can take a minute or so; Chinese input pauses until it's done. What Rime built of them goes when the last one is removed. The Chinese language pack must be installed first. The dictionaries' copies stay on this Mac, outside iCloud sync and AI context; your source, custom Rime files and learned words are kept. But a word you pick from one is learned like any other: into Rime's user dictionary, which syncs to your other Macs with the learned words when that's on (Settings → General → Sync through iCloud), and stays after its dictionary is removed. If you have your own `rime_ice.custom.yaml`, the import is refused before any files change: back up and move that customization aside, or attach the dictionary manually in Rime to keep it.
- **Translate to** (`@translate`, in Settings → General): add the languages to translate into (Spanish, French, German, Japanese, Korean, Chinese, Hindi, Bengali, Tamil and the other main Indian languages…) and drag them into order. Hindi typed in Latin letters ("aap kaise ho") comes back in Devanagari. `@translate` writes a line in each, in this order (three versions with only one); the sentence's own language is skipped. A new install translates into the first language in your Mac's preferred languages that isn't English; with English alone, `@translate` says there's nothing to translate into yet, and ⏎ on that notice opens Settings at Translate to, outlined (the sentence goes in as typed). Translate as You Type doesn't turn on then, and says where to add one.
- **Keyboard layouts**: French types with the layout picked in its section (`keyboardLayouts` in the config). For the other languages, under the input method macOS keeps your last Latin layout (AZERTY, QWERTZ, Spanish, US International…), so you type as usual, `@` included wherever your layout has it, and dead keys compose in a command's text too (⌥E then E → é, ^ then e → ê). Layouts without Latin letters (Russian, Hindi InScript) can't be used under an input method: switch to them with ⌃Space, or paste (⌃V) text into a command.
- `@improve` polishes and rewrites without translating; `@translate @improve` together translates and rewrites in one request. Turn on "@improve also translates" in Settings → General to make `@improve` always do that.

A personal dictionary can look like this (the entry fields are separated by **tabs**):

```yaml
---
name: my_vocabulary
version: "1"
columns: [text, code, weight]
...
星河项目	xing he xiang mu	100
蓝杉团队	lan shan tuan dui	200
```

Use lowercase Latin pinyin, spaces between syllables, and `v` for `ü`. Weight is optional and must be a finite, nonnegative number. Without `columns`, the order is `text`, `code`, optional `weight`; an explicit `columns` list can reorder those fields. `name` may contain Latin letters, digits, `-`, `_` and `.` (up to 128 bytes). A file can be at most 32 MiB. Files that depend on `import_tables`, omit pinyin codes, or use other column types or YAML directives are refused without changing the saved setup. This importer accepts vocabulary files; a full Rime configuration, custom-phrase shortcut table, or another vendor's binary dictionary needs a different workflow.

## Rewrite styles

After lines 1–3 come the rewrites, **in the language you typed**: English rewrites for English, Chinese rewrites for Chinese. Pick any of them in Settings → General → Rewrite styles:

- Polish: same tone, more natural
- Concise
- Formal: for managers and clients
- Casual
- Tactful
- Jargon: Amazon-speak in English (bandwidth, circle back…), big-tech jargon in Chinese. Bad news is played down, e.g. "this is a blocker bug" → "Oh! Looks like your team has the bandwidth to fix this minor issue!"

Rewrites that only change punctuation or repeat another line aren't shown.

### Jargon list (your own terms)

Jargon has no built-in term list. You can prepare your own (for example, the phrases your team uses), and the model
prefers its terms. In the candidates, the Jargon line notes what the terms it used mean.

The list is a text file with one term per line, optionally followed by its meaning, separated by "=", a colon or a
Tab (you can copy two columns from a spreadsheet and paste them). Lines starting with `#` are comments:

```
PRFAQ = a new-feature proposal: the press release and FAQ, written first
COE = an incident review
two-way door = a decision you can undo at any time
```

Under "Jargon list" in Settings → General (shown with the Jargon style), click "New" to create an empty list at `~/.config/allinoneime/jargon.txt` and open it;
if you already have a list file, click "Choose File…" to use it where it is (`jargonFile` in the config). Changes apply right away.
Only the first 150 terms are read. With "Jargon" checked, the list is sent to Bedrock along with each request.

<img src="docs/en/panel-dark.png" width="420" alt="The candidate panel in dark mode">

## Translate as You Type

A prototype, to try. Hold Shift on its own for 1 second to turn Translate as You Type on (or off); a quick tap of Shift
still switches the input language. At 0.5 s a hint near the caret says "Keep holding → Translate as You Type", and at 1 s
"Translate as You Type on: Chinese → English · hold Shift again to turn off" (naming the language it translates into)
confirms it for about 1.5 s (turning it off:
"Keep holding → Translate as You Type off", then "Translate as You Type off"); let go before then and nothing changes.
Shift with a letter (a capital), with another key or with a click never turns it on. It doesn't run in
[Code](#suggestions-and-code-new): there a long press of Shift says "Translate as You Type isn't available in Code",
and while it's on a tap of Shift goes through the languages only. While it's on, the menu bar icon carries a small dot.
There is no command for it.

While it's on, what you type collects into a draft, with the languages on the chip by it ("ZH → EN"; 「中 → 英」 in the
Chinese interface). It translates into the language you picked last on its chip (below), in every app and after a
restart; until you pick one, into your first translation language in Settings (and back to that one when the language
picked is no longer among them). If you type only one language, it's passed over: typing English alone, with English
then French to translate into, it's French. The language you're typing when it comes on doesn't change it. ⏎ translates
the draft and the translation goes in at once, with no candidates to pick: the draft says "Translating…" meanwhile, and
nothing is sent (⏎ again is the app's own). ⇧⏎ inserts the draft as typed; Esc while it's translating stops it and keeps
the draft (⌫ stops it too, and deletes a character as on the draft); if it fails (the network, a refusal, secure input),
the draft stays with a one-line notice and ⏎ tries again. Text typed in the language it translates into (tap Shift to
English) goes in as typed.

While it's on, a small chip "ZH → EN" (「中 → 英」 in the Chinese interface) shows under the line you're typing in, in the
input method's own panel (the candidate panel: on top of the candidates while you type pinyin), so it never takes the
focus from the app. Click "ZH" to switch the input language, as a tap of Shift does. Click "EN" for a short list of your
translation languages, the current one checked, and click one: it's what it translates into at once (the chip and the
next translation follow) and from then on. The keys work as before; one closes the list.

- **Tone**: it follows the app: casual in chat apps (WeChat, Slack, Messages, Telegram, Discord, Teams), formal in mail
  apps (Mail, Outlook, Spark), natural elsewhere; an app with rewrite styles of its own from an earlier version, the first
  of them.
- **Apps**: switching to another app (one with no text field too) turns it off, with no notice, and coming back leaves
  it off, unless that app has "Always Translate as You Type" (「总是边打边译」) from an earlier version (`translateAlways` in
  its profile, see [Per-app settings](#per-app-settings-new)): there it comes on by itself. In an app with No AI it does nothing: text goes in as typed, with a notice; so
  does what you type while secure input is on (a password field).
- **Privacy**: as for `@translate`: sent only when you press ⏎, to your own AI provider, with sensitive information hidden
  when that's on.

## Autocomplete (beta, new)

<img src="docs/en/autocomplete.png" width="520" alt="Hello wor, then in gray: ld, how are you? and a small Tab key">

Pause while you write, and the rest of the sentence shows in gray right after the caret; **Tab** puts it in. Turn it on
with **Autocomplete (Beta)** in the input menu (the menu bar's input source menu) or in the
[menu bar panel](#menu-bar-panel), or type "turn on autocomplete" in the settings search and pick Change: …; it stays on
until you turn it off (`autocomplete` in the config).

- **Keys:** Tab takes the suggestion, only while it's showing; ⇧Tab, ⌥Tab and a Tab pressed within 120 ms of it
  appearing go to the app as usual (indenting, the next field, Jupyter's completion). Type along with it and it shrinks
  as you go, with no new request; type something else, press Esc, an arrow or any other key, or click, and it goes (Esc
  only takes it down, and means "not this one": it doesn't come back for that text in that app; the other keys do what
  they always do). ⌘Z right after Tab (the next key, within a few seconds) takes it back, and the suggestion counts as
  not taken.
- **When:** after a pause that follows how you type: half as long again as your usual time between keys (once it has
  seen a few), at least 350 ms with the model on this Mac (500 ms with a cloud provider) and at most 1.2 s; in an app
  where you wave suggestions away one after another (Esc, or typing past them), a tenth longer for each, up to twice as
  long after ten in a row. So nothing is asked while you type, only when you stop. Only at the end of a line that has a word to go on from (not one
  or two letters alone), never while pinyin or a command is being written (in Chinese it waits until the words are
  in; if they're the start of the suggestion, its rest comes back), never with text selected. Each key stops the request
  still running. Up to about 12 words or 25 Chinese characters, to the end of the sentence. The last 20 suggestions are
  kept, each for its text (before and after the caret) in its app, so retyping or deleting back shows one again at once.
- **Never:** in password fields (those Accessibility tells too, where secure input isn't on) and while secure input is on,
  in a text that looks like a code or a card number, in terminals, password managers, remote desktops and virtual
  machines, in apps with No AI, and while Translate as You Type is on.
- **What it sends:** the line the caret is on, whole, and before it the most recent sentences in that line's language,
  up to 200 characters, in their order; sentences in other languages are left out, with a line break where they were. So
  a Chinese paragraph above an English line doesn't go with it (the model would go on in Chinese), nor English above a
  Chinese line. Sentences end at . ! ? 。！？ and line breaks, and go by their script: Chinese (any Chinese character:
  "我原本计划明天去hiking，" is Chinese), Japanese (kana), Korean, Hindi, each other script, and Latin letters (English,
  French …) as one. After the caret, its next line with something on it, up to 200 characters, so that the model doesn't
  write it again. What it shows is still checked against all the text before the caret (up to 1,500 characters): a
  sentence already there isn't suggested again.
- **The model:** the AI provider you picked in Settings → AI, the one commands use, with its model and
  settings (Bedrock, Claude API, Gemini, OpenAI-compatible). Turning Autocomplete on is the choice to send it your text,
  so the switch says where it goes, on or off: the input menu's item and the menu bar panel name the provider and its
  model ("Autocomplete (Beta) · Claude API · claude-haiku-5-5") with the line "Each pause sends the caret's line and up
  to 200 characters before it in the same language (and 200 after) to …, hidden words removed" ("hidden words removed"
  when hiding sensitive information is on, as for commands); the search's Change: … says the same in its row. Nothing asks first and nothing is
  kept: pick another provider (in Settings, through its search's Change: … or on another Mac with iCloud sync) and the next
  pause asks that one. Each request is small: a dozen words back (48 tokens), no thinking where the model can be asked
  for none (Claude Haiku 5.5, Sonnet 5 and 5.5, Opus 5), the lowest effort otherwise; a slow model (one that always
  thinks, Claude Opus 5.5 or Fable, or a reasoning model) may answer later than a suggestion is still wanted (3 seconds),
  and then nothing shows: pick a fast one. Where the provider can't answer (no key, the network, a refusal) nothing
  shows, no other model is asked, and it says so once per text field. With **Apple Intelligence** picked, the model on
  this Mac (macOS 26 and later, loaded ahead when a text field takes the focus); where it isn't available nothing shows
  and the field isn't read (it says so once). With **AllInOneIME Cloud** picked, the model on this Mac too: its free
  requests a day are kept for commands, and a few minutes of pauses would use them up; turning Autocomplete on says
  "Uses Apple Intelligence; set your own AI provider for faster suggestions". Requests are cheap but frequent: a heavy
  day can be 1,000–2,000 of them.
- **Each app:** in an app where none of the last 30 suggestions was taken it stops by itself and says so once (kept on
  this Mac, with the rest of what it learns); turning Autocomplete off and on again (here, or through the search's
  Change: …) starts every app over. Code editors (Xcode, VS Code, Cursor, JetBrains…, where Tab indents and takes their
  own completion) are off. An app set to always or never in an earlier version keeps it (see
  [Per-app settings](#per-app-settings-new)); that choice is this Mac's own, as the switch is: it doesn't sync.
- **What it counts**, only on this Mac: suggestions shown and taken, how much of what was shown went in, how long they took
  to come up (90% within … ms), Tabs undone right away, apps where it stopped, times it was turned off within a day, the
  tokens a cloud provider read. The input menu's Autocomplete item and the menu bar panel show the first lines.
- The gray text sits on the caret's line as the candidate panel finds it, on the line's baseline, in the field's own font,
  and stops at the field's edge where Accessibility tells the field's frame; too close to it for a few of its
  characters, it doesn't show at all, and Tab is the app's. Where a text field doesn't tell where its
  caret is, or tells two places more than a line apart, the suggestion is a line of the candidate panel instead ("Tab").
  Where it can't read its text (WeChat), what you typed into it since it took the focus stands in; a click forgets it.

## Suggestions and Code (new)

Rows in the candidate panel as you type, from plugins and, in Code, from the language you code in; **⏎** or **Tab** puts
one in.
They take the place of [autocomplete](#autocomplete-beta-new)'s gray text while they show.

- **Your own program:** a custom command of type `suggestions` is a source too, its prefix and its items yours: a program
  that prints `match⇥title⇥url` lines ([Suggestions from a program of your own](#suggestions-from-a-program-of-your-own-new)).
  It's used by its prefix alone, never from the @ command list.
- **Script extensions (0.6.7.1):** a script extension's command can be a source as a plugin's completions are: one line
  in its script, `# @allinoneime.completion {"prefix": "TCK-", "list": true}`, or `"completion"` in its bundle's
  `extension.json`. Its script prints the items, run in the background with `ALLINONEIME_COMPLETION=load` (and, with
  `query`, `query` and what follows the prefix as its one argument); it's on by default (0.6.7.2): your own extension's
  as it loads, an extension source's once you add the source. Its switch is in Settings → Commands, under the command,
  which says it runs the script in the background and, with `query`, gets what you type after the prefix, with its last
  refresh, items, last error and Refresh now; one you turn off stays off. Being on pins the extension and, as for a
  plugin, its `query`, prefix, `queryMinChars` and `compare`. A change to an extension of your own never turns it off,
  nor an update from an extension source you marked **Trust its updates**. From any other source, a change to any file
  of the source's repository (not only the bundle) or to those terms turns it off again, and Settings says so, and one
  an update adds waits for you; a repository of more than 2,000 files or 20 MB can't be checked, so its suggestions
  can't be on.
  The example bundle `bookmarks` has one: `bm.sw` → `[Swift](https://www.swift.org)`
  ([docs/extensions.md §11](docs/extensions.md#11-completions)).
- **Plugins' completions:** a plugin declares what it completes after a prefix, `#12` for `@github`'s issues, or a whole
  12-digit AWS account id with no prefix. Its list is kept on this Mac (loaded again every 15 minutes or so while you
  use it, never when you haven't for a week), and some also look up what you type, from 2 characters after the prefix,
  so a brand-new issue shows too. Every item that matches is a row, up to 100: the ones you picked before first (by how
  often and how recently), then the source's order. The panel shows 5 at a time; with more, the footer says which
  (`6–10 / 23`, as in the command list). The footer names the source, and the list's age when it's older than 10
  minutes. It works in English and in pinyin: `#`
  typed while pinyin is composed puts the words in and starts the token; a prefix of letters and a dash (`PROJ-`) typed
  in pinyin goes in as typed once its dash is typed (its letters aren't made Chinese), and the digits after it are
  typed. What you typed stays as typed; only the rest goes in (`#12` and the row `#1234 Fix login` add `34 Fix login`).
  A row whose text doesn't start with what you typed (a Markdown link, `[Fix login](https://…)`) takes its place
  instead, the prefix too, as one change you can undo, where the app tells where its text is; in a terminal it puts in
  its source's next choice (the number). Whether a row shows is its item's match alone.
- **Keys:** the same for every kind of row, in every app (chat apps, browsers, code editors and terminals too) and every
  input (English, pinyin when nothing is being composed, Code), as in the command list: while the rows show, the keys
  are AllInOneIME's first. The first row that puts something in is chosen from the start, drawn selected; ↓ ↑ move it,
  and past the last row shown (or the first) the rows scroll by one, round from the last to the first; the wheel or the
  trackpad over the panel moves the chosen row too, as in the command list (it stops at the first and the last row),
  and a click inserts the row clicked; ⏎ or Tab inserts the chosen one, always a row you can see.
  → or Esc hides the rows (nothing else happens; in Code the word you're typing goes in as typed),
  and keys are the app's again until what you type
  changes: in Slack, `#12` then ⏎ inserts the issue, and `#12` → ⏎ sends `#12` as typed. Digits never pick a row: they
  go on typing (`#7` then `1` is `#71`). A key the rows take never reaches the app too, in Slack, Chrome, Google Docs,
  VS Code and other apps built on Chromium or Electron as well: ⏎ doesn't send the message, ↑ doesn't move the caret.
  Pinyin's own candidates while it composes are as always (⏎ puts in the
  letters, Space picks). No rows in launchers, remote desktops, virtual machines and SSH clients.
- **Turning them on:** **Suggestions** in Settings → General, on unless you turn it off, covers plugins', script
  extensions', Suggestions commands' and Code's rows; they show once there is a source (a plugin's completions, a script
  extension's, a Suggestions command, or Code). A plugin's completions are on once you install it, and one installed
  before 0.6.7.2 the first time 0.6.7.2 finds it; each has a switch in Settings → Commands → Plugins (last refresh,
  items, last error, Refresh now; its preferences, passwords in the keychain), and one you turn off stays off, through
  updates and restarts. A plugin update that changes the hosts it reaches, its prefix, whether it looks up what you type
  and from which character on, how it compares (`compare`) or its script turns them off until you turn them on again
  (Settings says so under it); a source an update adds is off until you turn it on. **Suggestions** in the input menu turns them all off
  or on; an app at Off under "In these apps" has none (see [Per-app settin