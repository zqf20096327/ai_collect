<div align="center">

**English** · [简体中文](README.zh-CN.md) · [繁體中文](docs/readme/README_zh-TW.md) · [日本語](docs/readme/README_ja.md) · [한국어](docs/readme/README_ko.md) · [Français](docs/readme/README_fr.md) · [Deutsch](docs/readme/README_de.md) · [Español](docs/readme/README_es.md) · [Português (Brasil)](docs/readme/README_pt-BR.md) · [Italiano](docs/readme/README_it.md) · [Русский](docs/readme/README_ru.md) · [Tiếng Việt](docs/readme/README_vi.md) · [ไทย](docs/readme/README_th.md) · [Bahasa Indonesia](docs/readme/README_id.md) · [हिन्दी](docs/readme/README_hi.md) · [العربية](docs/readme/README_ar.md) · [Türkçe](docs/readme/README_tr.md)

<br>

<img src="Resources/AppIcon.png" width="112" alt="AllInOneIME icon">

# AllInOneIME

### Talk to AI wherever you type.

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
address. There's nothing else to learn: type the magic key (`@` by default) and whatever you want (`@saf`, `@3*7+2`, `@明天下午3点开会`, a sentence),
and the list says what can be done with it, the likeliest first ([One @](#one--say-what-you-want-new)). Without `@`, your keys go to the app as usual. It also types Chinese
(pinyin, built on Rime and rime-ice), French, Korean (Hangul) and Hindi (Devanagari from Latin letters), and runs
your own scripts as commands.

The magic key, the symbol commands start with, is `@` by default. In Settings → Common → Magic key, pick another symbol from the menu: `#`, `%`, `&`, `*`, `+`, `|` or `~`; commands then start with it (for example, `~translate`), and `@` types normally. Letters, digits, spaces and the symbols typing needs (pinyin's keys such as `'` `-` `=` `[` `]` `` ` ``, and the ones pinyin types as Chinese punctuation, such as `,` `.` `?` `\`) can't be the magic key, so the menu doesn't offer them. You can also set it in the config file, where it's called the command trigger: `"commandTrigger": "~"`.

![@improve and a rough sentence, then ⏎: polished versions, plus rewrites](docs/en/improve.png)

For more detail (every command and setting, installation troubleshooting, privacy), see the
[Wiki](https://github.com/MicroZ-LLC/AllInOneIME/wiki). Made by [Weijian Zhang](https://weijianz.com) at MicroZ LLC.

## How to use

Without `@`, it stays out of the way: in English, letters are typed directly and ⏎ is Return; nothing goes online.
A new install writes English; to type Chinese, French, Korean or Hindi too, add it in the settings (see [Input and translation](#input-and-translation)).

What you're typing (pinyin, a command such as `@improve …`, a note) shows only on the top line of the candidate box, with its cursor, in every app: nothing is shown in the text field until you pick, insert or run it. Leaving the field while you type (a click anywhere, in the same field too, another app, closing the window or tab) drops the pinyin not yet picked, so nothing of it is left behind.

In Chinese pinyin mode, `.`, `,` and `:` stay ASCII immediately after an ASCII digit, so `3.14`, `10:30` and `1,000` type as shown. Other punctuation and punctuation after other characters keep their usual behavior.

| Key | What it does |
|---|---|
| Type pinyin, Space / digits | In Chinese mode: pick words, as in any pinyin input method |
| The magic key (`@` by default), at the start of a sentence | Opens the list: with nothing typed, the commands, the most used lately (in this app first) on top, 7 at a time, scrolled with ↑↓, the wheel or the trackpad. Then type anything: a command's name (`@tr`) or what you want (`@saf`, `@3*7+2`, a sentence); the rows say what ⏎ does with it ([One @](#one--say-what-you-want-new)). ⏎ does the highlighted row (the first), Tab picks a command, ↑↓ choose, Esc or → leave what you typed as it is. Each row shown has its number: ⌥ and it does that row (⌥1 the first shown, as a click on it); the key hints at the bottom say "⌥+number pick" once. Digits alone are text there; while pinyin is typed they pick its words |
| ⏎, ⌘⏎ | Runs the command (⌘⏎ too, which chat apps use to send: the command is never sent as typed; on `@note` it saves the note). Works even if the pinyin isn't picked yet: it's picked first, as with Space |
| Space, ⏎ / digits | Once the results are up: insert the highlighted / numbered one; 0 is the original. ⏎ inserts even with a refine half typed (it's dropped). In an `@question` conversation ⏎ asks the next question instead (with nothing typed, ⏎ and Space do nothing), and ⇧⏎ inserts the answer |
| ⇧⏎ | With a refine typed after AI results: sends it. In an `@question` conversation: inserts the highlighted answer, dropping a question half typed. While a command is typed, or on other AI results with nothing typed: inserts what you typed as is, `@command` included. On other results (`@open`, a reminder …) it inserts the highlighted row, as ⏎ does |
| ⌘C | Copies the highlighted result (for `@open`, the path); the candidate panel stays open |
| ⌃V | Shows [clipboard history](#clipboard-history-new), the text and images you copied lately, newest first: ⏎ or Tab puts in the one chosen, ↓ ↑ choose, ⇧↓ ⇧↑ choose several (⏎ puts them in one per line, oldest first), ← → turn the page with more than 5 rows, Esc hides it (→ too, on one page); typing filters them (a Chinese text by its pinyin too). ⌃V ⏎ is the ⌃V you had, and ⌃V twice pastes as the app does (⌘V; ⌃V in a terminal or a code editor: vim, the shell). In a command (e.g. after `@improve `) the one you choose is appended after what you've typed instead of being pasted into the app: multiple lines become one, up to 2000 characters at a time (`@note` keeps the line breaks and takes up to 20000). Works in any app, terminals too. With clipboard history off, ⌃V in a command appends the clipboard text at once, and without a command it goes to the app as usual |
| ← → | In a command's list once the command is picked (a script extension's or a plugin's rows, `@open`'s results, `@tasks`, `@imessage`'s recipients) and in clipboard history, with more rows than the 5 shown: the previous / next page, its first row chosen (← stays on the first page, → on the last); the footer says `← → page` and which rows show (`6–10 / 12`), and ↑↓ still move a row at a time. On one page they're as before: they move the cursor in the text after the command, and → at its end hides the list, as Esc. The command list, suggestion rows, pinyin candidates and AI results keep their own ← →. The wheel or the trackpad over the panel turns these pages too (down: the next), as it does pinyin's candidates; in the command list, one @, clipboard history and suggestions it moves a row |
| ⌘V | The app's Paste. In a command not run yet it appends the clipboard text at once, no history, in every app: also where the app handles ⌘V itself (terminals such as Ghostty, iTerm2 and Terminal, and Notes), whose own paste then doesn't happen (with Accessibility allowed; without it they paste as well) |
| Esc, ⌫ | Back to the sentence to keep editing; typing punctuation or digits after the results continues it. After a refine: back to the results before it |
| Letters, once AI results are up | A follow-up: after `@question` the next question, which ⏎ asks (see [Conversations](#conversations-with-question-new)); after `@improve` or a prompt command an instruction such as `shorter`, which ⇧⏎ sends (see [Refining the results](#refining-the-results-new)). After `@translate` letters continue the sentence, and ⏎ translates it again |
| ⌘⏎, ⌥1–⌥9 | In an `@question` conversation: shows where to continue it (the coding agents installed, the one `@agent` hands to first; Claude, ChatGPT, Gemini; or copy it); ⌥1, ⌥2 … pick one |
| Click a row | In the candidate panel: picks it, as its digit would (a word, a command in the list, a result, an `@open` file, a recipient, an extension's row); the row under the pointer is highlighted. The text field keeps the focus |
| Right-click a candidate, ⌃⌦ | While you type pinyin: removes the candidate right-clicked (or Control-clicked), or the highlighted one with ⌃⌦ (⌃Fn⌫ on a laptop keyboard), for good: any candidate, the dictionary's words and emoji too, and the English words among the candidates (by their letters); it no longer comes up as a candidate, whatever you type (a longer phrase or a sentence with it in it still does), and what pinyin learned of it from your choices is forgotten (an emoji removed leaves the word it comes with as it was). An English word stays on your list of English words. Nothing is put in. Settings → More Settings → Input and keys → Chinese → Removed candidates brings one back (✕), and so does adding an English word again in English Words; they sync through iCloud with the learned words |
| Tap Shift | With more than one input language: the next one, in their order (English → Chinese → French → …, then back to the first) |
| Caps Lock | Caps Lock as usual, unless Settings → Common → Switch input language is set to Caps Lock (`switchKey`; Tap Shift is the default): then each press switches as a tap of Shift does, with what you're typing too, and the light goes off again at once. Caps Lock then no longer locks capitals (type them with Shift), and a tap of Shift switches nothing. In password fields Caps Lock is left to macOS. AllInOneIME stays under English in Input Sources |

## Commands

Commands start with the magic key, `@` by default; with another one picked in Settings → Common → Magic key, the
commands below start with it (`~improve`), and so does the app's own text that names them.

| Command | What it does |
|---|---|
| `@improve` | Polish: 1–3 are three versions in the sentence's own language, the rewrite styles (added and ordered in the settings) numbered on after them, 0 is the original. No translation; with "@improve also translates" on, it works like `@translate @improve` |
| `@translate` | Translate into the languages you added (Settings → Common → Translate to, drag to reorder), a line each, three versions with only one; the sentence's own language is skipped. `@translate @improve` together translates and rewrites in one request |
| `@question` | Ask a question; the answer appears in the candidates, ⇧⏎ or Space inserts it, ⌘C copies it. Type on and ⏎ asks a follow-up: the panel becomes a conversation of up to 5 rounds, then offers to continue in Claude or another AI. With nothing typed after it, it lists your last 5 questions, newest first; typing narrows them down (words anywhere in the question, any case, Chinese too). A digit, ↑↓ then ⏎, or a click shows a question's saved answer at once, offline, to insert or copy as usual; ⌘R there asks it again for a fresh answer. With no match, or nothing picked, ⏎ asks what you typed |
| `@reply` | Writes three replies to the message you're answering, in the other party's language and the tone of the app (casual in chat apps, formal in mail, where each reply is a whole email body; or the first of the app's own rewrite styles, set in an earlier version). Give it the message by selecting it, copying it and pressing ⌃V ⏎ in the draft, or taking a screenshot (⌃⇧⌘4, or WeChat's own) and pressing ⌃V ⏎; what you type after it says what to reply: `@reply politely decline`. ⌘R writes three more; see [Replying](#replying-with-reply-new) |
| `@agent` | Hands the task to a coding agent on your Mac, picked in Settings → Commands → Agent (@agent): Claude Code (the default), Gemini CLI, Kiro CLI, or a command of your own (what you typed is added as its last argument). The page also shows whether each is installed and how it starts. Claude Code runs in the background by default, with a notification when it's done (click it to open the session in Terminal and go on), or see `@tasks`; turn off "Claude Code runs in the background and notifies me" there to open it in Terminal. The other agents open in Terminal with what you typed as their first message. Each uses its own sign-in and settings. In Google Chrome it takes the page along: the address and title, the field you typed in with its form or section (★ marks where you are), the selected text and what's visible in the window — never a password field, never the whole page — so `@agent why doesn't this work` in a sign-in form's username field is about that field, and `@agent why is this blocked` on a pipeline page is about that page; the agent judges which. The page's text goes to the agent as read, marked as coming from the web (not as instructions from you). It needs Accessibility; Chrome builds its page tree for it only while `@agent` is being written there, turned back off after (Settings → More Settings → Privacy → "@agent and @reply take the Chrome page along" turns it all off). The first time it opens Terminal, macOS asks whether AllInOneIME may control Terminal: click OK. (It was `@claude` before 0.6.4.) |
| `@tasks` | Lists the background Claude tasks (working / done / waiting for you) with their last replies; ⏎ opens one in Terminal, ⌘C copies the reply. The list shows at once as last seen and is brought up to date as Claude Code answers |
| `@settings` | Opens the settings window right away (picking it is enough) |
| `@stats` | This week's stats in one row: how many commands you ran this week and how that compares with the same days last week, where they came from on a second line. ⏎ opens Settings → This Week, ⌘C copies the picture (as Copy Image there), Esc cancels; see [This week's stats](#this-weeks-stats-new) |
| `@open` | Lists matching files, folders and apps as you type (Spotlight). Several keywords work, separated by spaces: each must be in the path, at least one in the name (a standard folder's name counts for what's in it: `downloads pdf` finds the PDFs in Downloads). Apps and the standard folders are also found by their Chinese names, and a Chinese interface shows them that way. What you opened with `@open` comes first, then apps and those folders, then recently used or changed files; when the names find two files or fewer and no app or folder of those, the files in your home folder are searched by content too, those rows marked "content"; when there's nothing else, ⏎ lists them to pick from instead of opening the first. With a web address (`github.com`, `localhost:3000`, `https://…`), the first row is "open in the browser" and contents aren't searched; a file named exactly that (say `MANIFEST.in`) comes first. Text starting with `~/` or `/` is a path: its folder is listed as soon as it's read, never on the key you type, and the next keys narrow that listing at once (a link to a server's folder is listed as a file), Tab completes it and goes into folders; ⏎ opens, ⌘C copies the path. Spotlight looks on this Mac's own disks, not on a server's volumes |
| `@note` | Saves the text to the Notes app, in a folder named AllInOneIME (made when missing), or where Settings → Commands → Notes (@note) says: Notion, or a folder of Markdown files (an Obsidian vault or any folder); nothing is inserted. Pasted text keeps its line breaks, up to 20000 characters |
| `@reminder` | Adds a reminder to the Reminders app, in a list named AllInOneIME. Write the time in the text; it's read on the Mac, and a row shows what was read: ⏎ or Space adds it, Esc goes back to edit. With a time, it has an alarm then; with only a date, it's all day |
| `@js` | Runs a line of JavaScript and inserts the result: the value of the code's last expression, e.g. `@js [1, 2, 3].map(x => x * 2)`, `@js 2n ** 100n`, or else what `console.log` printed. It uses macOS's built-in JavaScriptCore, so there's nothing to install; it can't read files, reach the network or run other programs |
| `@reportissue` | Reports a problem: opens GitHub's page for a new issue in your browser, what you typed after the command as its title, and "What happened / What you expected" to fill in. It adds the app and macOS versions, your Mac's architecture, the interface and input languages, the installed language packs, which kind of AI provider (and the model, if it's a public one; otherwise "custom"), whether hiding sensitive information is on, the action key, and how many custom commands, plugins and extensions you have (and apps with their own settings, if any), never their names, your text, paths or keys. ⏎ (or your action key) first shows all of it in the candidate panel; ⏎ again, or a click on the row, opens the page, where you read it and click Submit (with your GitHub account); Esc goes back. Also in the input menu ("Report an Issue…") and Settings → About |
| `@imessage` | Sends an iMessage: type a name, a phone number or an email (a Chinese name also by its pinyin, in full or the initials) and pick the recipient in the candidate panel (the ones you messaged lately come first; a full number or address works too), then write the message (commands inside it such as `@stock AAPL` run first). ⏎ shows "Send to Alex (…): message" in the panel, ⏎ again sends it, Esc goes back to editing; nothing is typed into the text field. The first time, macOS asks whether AllInOneIME may access Contacts and control Messages: click OK for both |

Example: `@q` ⏎, type `what is quantum computing`, ⏎. `@note books to read: The Three-Body Problem` ⏎ saves a note.
`@reminder call Bob tomorrow at 3pm` ⏎, check the time it read, then ⏎ again to add it.
In Chinese mode, `@open` switches to English letters for the moment and goes back to Chinese when you're done.

A command you haven't run is never typed into the app, whether its text is Chinese or English: ⌘⏎ runs it, as ⏎ does
(`@note` saves). Leaving the text field (another field or app clicked, or a click elsewhere in it), a password field
taking over, or any other ⌘ shortcut (⌘A, ⌘S …) drops it, nothing typed in, and the shortcut goes on to the app. ⌘V
pastes into it in every app, terminals and Notes too. ⌘← ⌘→ move to the start or end of its text, pinyin you're typing
picked first, as with Space. ⇧⏎ still inserts it as typed, and `@note` keeps what you wrote (see
[Notes and reminders](#notes-and-reminders)). A command that has run (its results up, or still coming in) leaves
nothing either when you leave the field: it stops and the panel goes.

The code for `@js` is typed in English letters, and full-width punctuation (from Chinese mode) becomes ASCII; write it on one line, with `;` between statements.
It runs in a separate process, stopped after 10 seconds or with Esc at any time; on an error, the error's first line is shown, e.g. `ReferenceError: Can't find variable: x`.
Output with several lines is inserted as printed; in a terminal it goes in as one line (a terminal runs every line it is given).
A terminal inside an editor (VS Code, Cursor, JetBrains) can't be told apart from the editor itself, so there any command's output with several lines goes in as it is.
It also works inside another command's sentence: `@reply the answer is @js 2n ** 100n`; put code with spaces in quotes: `@question explain @js "[1, 2, 3].map(x => x * x)"`.
Not the other way round: the code of `@js` always runs exactly as you typed it, and commands in it don't run first.

For Python, add `@py` in Settings → Commands → Your Commands → Add Command… → Start from an Example (it was built in before 0.7.5): your own command, which runs a line of Python with your Mac's `python3` the same way (`@py 2**100`, `@py import math; math.sqrt(2)`), inside other commands' sentences too, and isn't offered without `python3` (Xcode's command line tools have it). On an error it shows the last line Python printed, e.g. `ZeroDivisionError: division by zero`. Until you add it, `@py` is just text.

![Typing @ opens the command list; @question plus a question, then ⏎ for the answer](docs/en/commands.png)

![@open finds apps as you type; starting with /, it's a path: the folder is listed, Tab completes](docs/en/open.png)

When `@` isn't followed by a command, as in `@john`, the list offers what can be done with the text; Esc or → puts it in
as typed. If you often @-mention people in chat apps, change the magic key to another key, such as `~`, in Settings →
Common → Magic key.
Typed right after a letter, a digit, `.`, `_` or `-`, as in `bob@example.com` or `ssh user@host`, `@` is just text: no
list opens, in every app, terminals included. Right after `@`, a space or a mark (`.`, `:`, `/`) closes the list and
leaves the `@` as it is; in a terminal ← → on a lone `@` only close the list.

### One @: say what you want (new)

Type the magic key (`@` by default) and whatever you want; the list shows what can be done with it, the likeliest first, each row saying what ⏎
does, with its command's name dimmed on the right (so the command names are there to learn as you go, but you don't
have to). The first row is highlighted; ⏎ does it, ↑↓ pick another, a click does that one, Esc leaves the text as typed.
Nothing you type goes to the AI and no command runs until you pick a row (⏎, Tab, your action key or a click): the rows are worked out on this Mac on the key you type (Spotlight's file names, the selected text if there is one). An AI row may open the connection to your provider before that, with no text and no key in it.
A row that opens an app, a folder or a file shows its own icon, as Finder shows it (in `@open`'s list too).

| You type | First row |
|---|---|
| `@` alone | Your commands, the most used first: ⏎ picks the highlighted one, as after its name (one that needs nothing typed, such as a snippet, runs) |
| `@tr`, `@no` | The commands those letters start: `@translate`, `@note` (⏎ picks it, as before; the ones you use in this app first) |
| `@3*7+2` | `= 23`: ⏎ puts 23 in place of what you typed. Numbers and `+ - * / × ÷ ( ) % ^ .` only (`200*15%` is 30); a whole date or phone number (`2026-11-06`, `11/5`) is no sum |
| `@github.com/apple/swift` | Open it in the browser |
| `@saf`, `@wx`, `@xtsz` | Open Safari, WeChat (微信, by its initials), System Settings (系统设置): an app, a standard folder or what `@open` opened before, by the start of a word of its name or the pinyin or initials of its Chinese name; the files Spotlight finds by name join below, never in the first row |
| `@明天下午3点开会` | Reminder: tomorrow 3:00 PM 开会, the time as your Mac shows times (⏎ adds it) |
| `@红烧肉怎么做`, `@how do I undo a commit`, `@what's the capital of Peru` | Ask AI (what `@question` asks): a `?` at the end, 吗 呢 什么 怎么 哪 几 多少 where they ask (not 几乎, 过几天, 没什么, 哪怕), or a first word such as how, what, who, is, do, did, will |
| `@thank you for the gift` | Translate into Chinese, when Chinese is your first input language (what `@translate` does); Japanese (anything with kana) is always another language |
| anything else | Improve (what `@improve` does) |

After those come Improve and Translate (the one you use more in this app first), and once you've used them, up to
three of your own AI instructions and plugins that take text; Ask AI is always last, so nothing is a dead end. In Chinese
mode the letters after `@` are pinyin and command names at once: the candidates are a line on the side nearest the caret
(on top when the panel is below it, just above the footer when it is above), so you pick the word first (Space or a
digit); the rows on the far side are for the sentence with the first candidate. With text selected, `@` alone
lists what to do with it: Reply first in a chat app, else Translate (another language) or Improve, Ask AI about it last;
text typed then is an instruction for the selection ("more formal"). In an app with No AI there are no AI rows: an AI
command typed by its name (`@tr`) is still listed, and says AI is off there when run; with no row at all, ⏎ types what
you wrote as it is. The same while secure input is on (a password field, the lock screen, another app's Secure Keyboard
Entry): no AI rows, and an AI command typed by its name says secure input is on when run.
`@name text` works exactly as before, for every command, yours and plugins' included; your own commands, plugins and
script extensions are also found by the words of their summary, title or keywords (`@email` finds a snippet whose
summary is "Email signature"), but `run`, `terminal` and `link` commands, snippets and script extensions are never
offered for an arbitrary sentence.
`@question`, `@improve`, `@translate` and `@reply` send to the AI you chose in Settings → AI only when you press the action key (a screenshot is read on
this Mac and its text is sent; a question about one sends the image too, made smaller, to an AI that can see images); `@open` searches only on this
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
selection stays as it is. Up to 5000 characters; never read during secure input, in a terminal or in a password
manager (1Password, Bitwarden, Passwords …: no text of its fields is read for a command). In apps such as Chrome and
Slack the selection is read just after the `@`: a key you press while it's still being read is done as soon as it's
read, in the order you typed. There is no switch for it: an app whose field doesn't take the result in place of the
selection (the selected text still there afterwards, the result not) is remembered on this Mac, and its selection isn't
used again; Settings → More Settings → Privacy → Learned… lists it, and Forget lets it try again.
`"useSelection": false` in the config turns it off in every app.

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

A question about a screenshot (new): ⌃V in `@question`, after one @'s text (Ask AI moves to the top), or while typing a
follow-up in the conversation attaches it, and ⏎ asks. Its text, read on this Mac, always goes; the image itself goes
too, its long side at most 1568 pixels, when the AI can see images: the Claude API, Gemini, OpenAI's own API, Bedrock's
Claude and Nova models, and Claude Code, Codex, Antigravity and Kiro CLI. AllInOneIME Cloud, Apple Intelligence and
other OpenAI-compatible services get the text only. A screenshot with no text (a chart, a photo) can be asked about
only when the AI sees images. ⌫ on an empty follow-up line takes its screenshot away. When hiding sensitive information
took something out, the image isn't sent. A question asked with a screenshot isn't kept in the recent questions.

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

Once `@question` starts answering, what you type is the next question (the answer goes on): ⏎ asks it once the answer is in, with the questions and answers so far,
and the panel grows into the conversation, the earlier rounds dimmed as Q / A rows, the latest answer below them. With
nothing typed, ⏎ and Space do nothing: the conversation stays up. The line on top says which round comes next ("question 2/5 ›
…"). Every answer can be inserted: its digit (1–5), ↑↓ then ⇧⏎, or a click; the latest is
selected, and ⌘C copies the selected one. ⇧⏎ inserts it even with a question half typed (it's dropped). An action key
other than ⏎ (a tap of ⌥, ⌥Space, a shortcut) does what ⏎ does here. Esc closes the panel at any round, leaving nothing in
the field, even with a question half typed; the conversation stays in your recent questions, to go on with later. The panel grows to about half the screen, then scrolls, the latest at the
bottom.

After 5 rounds (`questionRounds` in the config, 2–10) the next question's line becomes "5 rounds in: continue in Claude
or another AI", numbered, picked with ⌥ and their number (the footer says "⌥+number continue"); ⌘⏎ shows them at any round (while an answer is still coming in it
does nothing, and never reaches the app). What you type then is the first message there; only ⌥1, ⌥2 … send it (⏎
asks nothing more, and opens nothing). A question about selected text or a screenshot takes that text along (a
screenshot's as it was read), quoted as a block of its own. The choices:

- **The coding agents installed** on this Mac, each by its name: the one `@agent` hands to first (⌥1), then the others
  (Claude Code, Gemini CLI, Kiro CLI, your own command from Settings → Commands → Agent). Each opens an interactive session in
  Terminal, started as `@agent` starts it, beginning with the conversation and "Let's continue this discussion". One
  that isn't installed isn't shown.
- **Claude** or **ChatGPT** on the web, the conversation filled in (a long one goes on the clipboard: paste it).
- **Gemini** on the web, the conversation on the clipboard to paste.
- **Copy the conversation**, in Markdown (**Q:** / **A:**).

Which ones, and in which order (the first is the default): Settings → AI → AI Commands → "Continue a conversation in"
(`questionContinueIn` in the config); with more than 5, ⌥6 … ⌥9 pick the rest. "@agent's agent" there is whichever
agent Settings → Commands → Agent picks, by its name; an agent that isn't installed right now keeps its place in the list when you
edit it. With Apple Intelligence on this Mac a long conversation doesn't fit its small context: the oldest answers are
shortened, then the oldest rounds left out, and the panel says "earlier rounds shortened". A conversation is saved
under its first question in the recent questions, and picking it shows the rounds to go on with.

### @question in a session of its own (new)

Settings → AI is one choice for every AI feature (every choice is a card, by how they connect; one click chooses): Claude Code, Codex,
Antigravity (Google Antigravity's CLI, `agy`) or Kiro CLI under "With your subscription" (`questionBackend` in the
config) has `@question` answered in the input method's own session on that CLI. (Gemini CLI is no longer one of them: it
stopped serving personal Google accounts, which Google moved to Antigravity; a config that chose it is on Antigravity
when `agy` is installed, else on its provider. `@agent` still hands to Gemini CLI.) A session is one long-running Claude
Code (`claude -p`, stream JSON), Codex (`codex app-server`), Antigravity (`agy acp --agent allinoneime`) or Kiro CLI
(`kiro-cli acp`) process the input method keeps for every text field, in a folder of its own
(`~/Library/Application Support/AllInOneIME/claude-session`, `codex-session`, `antigravity-session` or `kiro-session`,
with its own instructions: CLAUDE.md, AGENTS.md, an Antigravity agent or Kiro steering), signed in with that CLI's own account: a
Claude, ChatGPT, Google or Kiro subscription, a company sign-in, or Claude Code on Amazon Bedrock (the provider settings
in `~/.claude/settings.json` are used), with your login shell's PATH and the variables the CLI reads there
(`CLAUDE_CONFIG_DIR`, `CODEX_HOME`, `GEMINI_API_KEY`, `GOOGLE_CLOUD_PROJECT` …). No API key. Antigravity's session
uses its fast model (Gemini 3.8 Flash, low thinking: the first words in about 2 seconds, against 5–8 with its default). Each `@question`
conversation in the panel is a new conversation in the session (a new Claude Code session id, a new Codex thread or ACP
session), and its follow-ups go on in that one: the agent remembers the conversation's earlier rounds, not earlier
conversations, and a question never carries every one before it. Whichever CLI it is, the session may read the web
(search it, open pages) and nothing else: it can't read, list or change files on this Mac, run commands, use the CLI's
extensions, plugins or apps, or start other agents, and it asks you for nothing; its MCP servers only as checked under
**MCP Servers** below the AI (Claude Code, Codex, Kiro CLI): Settings lists the servers in that CLI's own config (Claude
Code's `.claude.json`, Codex's `config.toml`, Kiro's `~/.kiro/settings/mcp.json`; only read), none checked at first, and a
server checked gives the session its **read-only** tools only (a tool whose `readOnlyHint` is true; one that sends,
writes or changes anything, or doesn't say, is never given), listed as you check it and each time the page shows,
saved as `sessionMCP` in the config (this Mac's own, never synced; the read-only tools as last listed, so a server whose tools changed is listed again as the page shows); only the servers checked start, with the web tools
open only (Claude Code:
`--tools WebSearch,WebFetch`; Codex: no environment for commands and files, `CODEX_EXEC_SERVER_URL=none`, with its MCP
servers, apps and agents turned off; Antigravity: an agent with its web search (`search_web`) alone and no MCP servers,
and a hook in `antigravity-session/.agents` that denies every other tool before it runs, with each permission it asks
for refused; Antigravity has no tool that opens a page, so it searches only; Kiro CLI: an agent with `web_search` and
`web_fetch` only). A question with text you didn't type in it
(selected text, a screenshot's text, a page or another command's output inside it) could carry instructions to send the
conversation somewhere: in that conversation the session may fetch only the addresses you typed yourself (in the
question and its follow-ups), and with none typed its web tools are off. Claude Code is kept to those addresses' sites
(`WebFetch(domain:…)`, no search); Codex, Antigravity and Kiro CLI can't be kept to addresses, so they have no web tools
then (Codex `web_search="disabled"`, Antigravity and Kiro CLI an agent without tools); the
process starts again with them. Continued in Terminal (⌘⏎), it is not this session any more but the CLI as you set it
up: a normal interactive session on that conversation, with your own rules (your CLAUDE.md, AGENTS.md, GEMINI.md or Kiro
steering; Antigravity's hook says nothing there), settings and permission prompts, all the tools you allow it and your MCP servers, extensions and plugins:
what the conversation asks of it is then up to the CLI and you, as in any session of yours (for one with text you didn't
type in it too). Only the question asked now is sent, with values hidden as for the provider (see Privacy) and, for a
question about AllInOneIME, the user guide's excerpts. It starts when an `@question` is about to be asked (`@question`
typed or picked, or one @'s Ask AI row highlighted; not for the magic key alone, nor in an app without AI or during
secure input), with a new conversation made ready then (Codex and the ACP agents open it in the process they have;
Claude Code's process starts again on a new session id), so the answer doesn't wait; it ends after 15 idle minutes, and
a follow-up after that resumes its conversation. In it a conversation has no round limit, and ⌘⏎ offers continuing the
same conversation in Terminal first (`claude --resume`, `codex resume`, `agy --conversation`, `kiro-cli chat --resume-id`);
Start Over under the choice begins a new one. Never two processes on one conversation: ⌘⏎ ends the session's own
process first and waits for it (killed if it hasn't ended within half a second), Terminal's CLI holds the conversation's
lock while it runs (`lockf` on `<session folder>/locks/<id>.lock`, waiting for ours to be let go), and the conversation
is Terminal's from then on: the next `@question` (an @ typed meanwhile too) goes into a new conversation here, never the
one handed off. Quitting or updating AllInOneIME ends every session's process, and after the relaunch no conversation
from before is resumed. Whether each CLI is installed
and signed in is looked at by Settings → AI (`claude auth status`, Codex's account, Antigravity's sign-in in the
keychain or its settings without starting it, `kiro-cli whoami`): every CLI when the page shows, for its card, and when
you choose a CLI there. What it found stands, signed in until AllInOneIME quits and anything else for a minute, so
showing the page again runs no CLI before then; never at launch nor for a question. The one chosen is tried as a question comes; one found
signed in after it wasn't has its session's process started again by the next question. A CLI takes a second or more to
answer, so
what has to be fast (rewriting, translating, replies, autocomplete) goes to the provider you set up before (a key added,
an AWS profile, AllInOneIME Cloud signed in), else to Apple Intelligence on this Mac where it's available; with
neither, autocomplete is off, and rewriting and translating go to the session too, more slowly, each request in a
conversation of its own with no web tools (never an `@question` conversation, however long it waits behind a question
being answered). Settings says which under the choice. When the session can't answer (not
installed, signed out, it can't start, it can't be kept to the web, its usage limit, an expired AWS sign-in, nothing
within 30 seconds, still answering an earlier question after 30 seconds, or the CLI compacting the conversation before
it answers: Claude Code's `compact_boundary` or compacting status, Codex's context compaction, not waited for) the
fast fallback answers at once and the panel says why (with none, the question fails, saying why); Settings → AI shows a
CLI that couldn't start so until it is looked at again. The panel's footer says who answered: the CLI (Claude Code, Codex, Antigravity, Kiro CLI) or the AI provider, "new
conversation" when the CLI's conversation is new with that answer (the first question, or one it couldn't resume after a
restart, so it doesn't have the rounds before), and the tokens the turn used when the CLI reports them (`12k tokens`).
An answer that says nothing for 3 minutes, or doesn't stop within 5 seconds of Esc, ends the session's process; the next
question starts it again. A config from before (no `questionBackend`) stays on its provider.

To open the session yourself and read its history, in Terminal (one line per agent):

- Claude Code: `cd ~/Library/Application\ Support/AllInOneIME/claude-session && claude --resume AllInOneIME` (each
  conversation is named AllInOneIME; Claude Code finds a name only in the session's own folder, and lists them all when
  more than one has it).
- Codex: `codex resume AllInOneIME` (each conversation's thread is named AllInOneIME); `codex resume` in `codex-session`
  lists them too.
- Antigravity: `cd ~/Library/Application\ Support/AllInOneIME/antigravity-session && agy --continue` (Antigravity can't
  name a conversation from outside, it titles each one itself; the folder's are the input method's, and `/resume` there
  lists them).
- Kiro CLI: `cd ~/Library/Application\ Support/AllInOneIME/kiro-session && kiro-cli chat --resume` (Kiro CLI can't name
  one either: the folder's latest is the input method's last conversation).

### Recent questions (new)

`@question` with nothing typed after it lists your last 5 questions, newest first, with when they were asked ("3 hours
ago"). Typing narrows them down: every word anywhere in the question, in any case (Chinese without spaces too). A digit,
↑↓ then ⏎, or a click shows a question's saved answer at once, without going online: Space or ⇧⏎ inserts it, ⌘C copies
it, ⌘R asks it again for a fresh answer (a conversation: its latest question), Esc goes back to the list. A saved
conversation shows all its rounds: type to go on with it. With no match, or nothing picked, ⏎ asks what you typed. A new answer to the same question, or a conversation
that goes on, replaces the saved one.

- They're kept only on this Mac (see Privacy): not while secure input is on, and never for questions on selected text.
- Settings → AI → AI Commands → "Remember recent questions" turns it off (`rememberQuestions` in the config); turned off there,
  it deletes them too. Turned off through the settings search's Change: … (see [Settings](#settings-new)), they're kept, so
  that undoing it puts back exactly what was (its preview says so); "Forget (N)" deletes them.

### Notes and reminders

`@note` makes a new note; its first line is the title. After copying some text, ⌃V ⏎ after `@note ` (or ⌘V ⏎) saves it with its line breaks, shown as ↵ in the command.
Where it goes is Settings → Commands → Notes (@note) → Save to:

- **Notes** (as before): a new note in the AllInOneIME folder.
- **Folder (Obsidian or any)**: a new Markdown file per note in the folder you choose, named after its first line (`/\:*?"<>|#^[]` become `-`; a name that's taken gets " 2", " 3"). The file holds `created:` front matter, then the whole text as typed. A file is never written over, and a folder that isn't there (an unmounted drive, a moved vault) isn't made: the note comes back instead. In an Obsidian vault (a `.obsidian` folder in it or above it) the notice says "Saved to Obsidian", and the menu bar panel opens the note in Obsidian.
- **Notion**: Create Integration… (New integration → Internal → copy the token), paste the token (kept in the keychain), then in Notion open the page or database → ··· → Connections → add your integration, and paste its link; Test shows "✓ “Inbox” (database)". A page gets a new child page, a database a new row (the first line as its title); the rest of the note is its body, in one request. Offline or refused, nothing is kept to send later: the note comes back. During secure input `@note` doesn't send to Notion.

The notice says where the note went ("Saved to Notion", "Saved to “Inbox”").
If you leave the text field (click elsewhere, switch apps) or press ⇧⏎ (insert as typed) before a note with line breaks is saved, it isn't typed into the app (in a terminal, each line would run as a command): it goes on the clipboard instead ("The note wasn't saved; its text is on the clipboard"). A note of one line is inserted as typed (any other command not run yet is dropped instead).

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
instruction, a program, a program in Terminal, a web page, a text to insert, or suggestions from a program as you type), or start from an example (Start from an Example → `@py` runs a line of Python with your `python3`, as the built-in `@py` did). Your commands come after the built-in
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
- **Icon and color** (new): the editor's Icon picks an SF Symbol (search its name; common ones such as `terminal`, `globe`,
  `bolt` come first), one emoji (Emoji…) or Default, the icon of the command's kind; Color picks one of the system colors
  or Default. They're saved as `icon` (`"bolt"`, `"🧮"`) and `color` (`"purple"`; also `"#34C759"` by hand) and show in
  the command list at once.
- **Test run** (new): at the bottom of the editor, type a sample (the text you'd write after the command, or the
  selection) and click Test run. The command runs once as the action key would run it, with the same time limits, and
  what it gives shows there: what a program prints (a `terminal` command runs in the background here, not in Terminal),
  the address a `link` opens, the text a `snippet` inserts, the AI's answer, or the error. Nothing is inserted or opened.
  An AI instruction first asks "This sends the sample to …" (Run / Cancel). `suggestions` has Refresh Now instead.
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
  exists; the **Suggestions** switch (Settings → More Settings → Suggestions, the input menu) applies. The editor shows
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
| `{name?}` | a blank, filled from what you wrote, separated by commas (`,` or `，`), in order: `Dear {name?}, see you {day?}.` with `@meet Bob, Friday`. One left empty is named in a notice, and nothing goes in. A full-width `？` works too (`{名字？}`) |
| `{clipboard}` | the clipboard's text (macOS may ask first) |
| `{selection}` | the text selected when you typed `@` (it's replaced, as by any command on the selection) |
| `{date}`, `{time}` | today as `2026-10-17`, the time as `14:05`; `{date:EEEE, MMM d}` with a [date pattern](https://unicode.org/reports/tr35/tr35-dates.html#Date_Field_Symbol_Table), in the interface language; a full-width `：` works too (`{date：M月d日}`) |
| `{cursor}` | where the caret goes after it's in (once at most; not in a terminal) |

- `{{` writes `{`, and the `}}` that closes it writes `}` (`{{input}}` inserts `{input}`); any other `}}` or `{…}` stays
  as it is, so JSON or code in a snippet is fine: `{"a":{"b":1}}` goes in as written.
- With no `{input}` and no blanks, what you write after the name goes in after the snippet, after a space.
- Write `@sig` inside another command's text to include it: `@question summarize this @zoom` sends the link itself. Only
  snippets with no `{clipboard}`, `{selection}` or blanks work there; with `{input}`, it's one word or a quoted phrase:
  `@meet「Friday 3pm」`.
- Plain text only (line breaks kept), at most 20,000 characters. In a terminal a snippet of several lines or with a tab
  goes in as one paste with Accessibility allowed and Paste from Other Apps set to Allow (your clipboard is put back
  after), else on one line with tabs as spaces (a line break typed there would run the line, a tab would complete it),
  as clipboard history's rows and the AI's answers do. Snippets stay on this Mac, so they work during secure
  input and in apps set to No AI. Extension bundles can ship them too (`snippets` in `extension.json`, see
  [docs/extensions.md](docs/extensions.md)).

### Script extensions

Add your own commands as programs: a script in any language (bash, Python, Node, Swift, …) with a few lines of
metadata in its comments. Put it in `~/.config/allinoneime/extensions`, or in a folder you add under Settings →
Commands → Script Extensions. Raycast Script Commands work as they are, and folders that already hold them are
found with Spotlight. From a found folder only its Raycast scripts load, and only those that are executable and weren't
downloaded from the internet, with no status line; a folder holding none of those isn't found (nothing about it shows in
Settings): add it to use it ([docs/extensions.md](docs/extensions.md)).

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
it's done (the menu bar panel lists it meanwhile), show a `status` beside its name in the command list (its last value is
kept across launches, in the app's caches, readable only by you, and shown until it's refreshed), or ask first
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
  `--list-extensions` (on `~/Library/Input Methods/AllInOneIME Input.app/Contents/MacOS/AllInOneIME`; `AllInOneIME.app`
  in an install updated from 0.7.2).
- Only reviewed code loads: a source folder in the load list that wasn't reviewed on this Mac (a copied config) is left
  out. git never waits for an answer: no terminal and no prompts, so an unknown host key or a password prompt fails at once.

The config keeps them as `extensionSources`; the repository layout is in [docs/extensions.md](docs/extensions.md#10-extension-sources).

### Plugins

Plugins are ready-made `@` commands for things not everyone needs, like `@stock AAPL 600519 700` for stock quotes.
Installed, they work like any command; Settings → Commands → Plugins shows what's installed and where each sends your
text, and removes them (a removed plugin's folder goes to the Trash).
Plugins are JavaScript run in a separate process: they can reach only the websites they declare
(HTTPS), and can't read files or run other programs. "Browse Library…" under Plugins installs them
from the [plugin library](https://github.com/MicroZ-LLC/AllInOneIME-plugins): it shows which websites a plugin
contacts before installing; the library's index is signed and every file must match it. A newer version shows an
"Update" button; nothing updates by itself. Your own plugins go in `~/.config/allinoneime/plugins/` ("Open Plugins
Folder", under Commands → "Folders and sources…"): local plugins, never overwritten by the library.
"Link" plugins run no code: they put the text into a web address and open it in the browser, like `@x nice weather
today`, which opens X's composer with the text filled in; posting is up to you on the page. The library has four
(`@x`, `@threads`, `@bsky`, `@weibo`). `@xe` converts currencies: `@xe 100 USD CNY`, `@xe 1000 JPY EUR`, one line
with the date of the rate (rates by ExchangeRate-API). `@calculator` is a calculator that works offline,
`@calculator 23*17` → `391` (the built-in `@calculate` before 0.6.5), and `@days` does dates: `@days +10` →
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

⏎ by default; change it in Settings → More Settings → Input and keys → Action key (`actionKey` in the config): click it, then press the key, as
for a keyboard shortcut in System Settings: Tap ⌥ (either side: press and let go right away), ⌥Space, Space (press
Space once more after the words are picked; twice in English mode), or a shortcut such as ⌃⏎, ⌘⏎ or F5 (a key that
types needs ⌃, ⌥ or ⌘).
Whatever the action key, commands also run on ⏎. If ⌥Space is already a shortcut for Alfred, Raycast or the like,
they get it first.

### Typing results out

Turn on "Type results out" under Settings → More Settings → Advanced (`typeOut` in the config) and a command's result is typed into the
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
after Esc or another key), and the app gets no typos again. Settings → More Settings → Privacy → Learned… lists those apps; Forget
lets one try again. They're kept on this Mac only, with the rest of what it learns (see Privacy).

### Per-app settings (new)

An app has two settings of its own; everything else is the same in every app:

| Setting | Where | In the config |
| --- | --- | --- |
| What a suggestion row inserts there: with title, with title and link, or a Markdown link; or Off, no suggestions there | Settings → More Settings → Suggestions → More… → "In these apps" | `suggestionsInsert` (synced with the settings); Off is `"suggestions": false` (this Mac's own: not synced) |
| No AI: `@improve`, `@translate`, `@question`, `@agent` and your prompt commands send nothing there and say so; typing and the other commands work | Settings → More Settings → Privacy → "Apps without AI" | `noAI` |

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
  styles (`rewriteStyles`). Settings → More Settings → Advanced → "Previous per-app settings", there only while an app has one, lists
  them, a row per app, and Remove clears them for that app (its Insert, Off too, and No AI stay). An app set to no
  suggestions in an earlier version (`"suggestions": false`) is under "In these apps", at Off.
  Nothing in `config.json` is renamed or removed by 0.6.7, and these values sync as they did.
- With No AI, the list after `@` offers no AI row (no Improve, Translate, Ask AI or Reply for a text or a selection, and the
  list with nothing typed has the commands that don't use AI); an AI command typed by name is still found, and running
  one shows the notice and keeps what you wrote. Your own
  terminal commands (`"type": "terminal"`) run programs, not the AI, so they still work there.

### Settings (new)

Settings has six pages in the sidebar, in this order, and opens on Common:

- **Common**: the settings most people need, and at the top a field to say what to change ("translate into English and
  Japanese, candidates in a column"; ⏎ asks the AI, as the search's **Change: …** does). **Typing**: the input languages
  as chips (drag to reorder, ⊗ removes one, Add… adds one; the first is the default, and Code comes after them, "Code ·
  Python"), Chinese typing (full pinyin, Shuangpin or Zhuyin), Characters and Shape codes (for pinyin) while Chinese is
  an input language, Switch input language (Tap Shift or Caps Lock) and the candidate layout. **Commands and
  features**: the magic key, Translate to (`@translate`'s languages), Clipboard history (with Clear History) and
  Autocomplete (Beta). The last line says how many settings More Settings has. A language pack's problem shows its
  banner on this page.
- **AI**: the AI that answers (the provider, its model, its key or AWS profile, and Test Connection; the base URL is
  under More…, which opens by itself once one is set); then every choice as a card, by how it connects, always shown
  (one click chooses; the one in use is outlined and says In use, the others' status is in gray); then **AI Commands**, each AI command's options together:
  `@improve`'s rewrite styles, "@improve also translates" and the jargon list (shown with the Jargon style, or once a
  list is set), and `@question`'s: where a conversation continues and
  remembering recent questions (with Forget), their only place in Settings.
- **This Week**: [this week's stats](#this-weeks-stats-new), with This Week / Last Week, the picture to copy or save, and
  "Hide my command names in the image".
- **Commands**: your commands, the agent `@agent` hands to (and "On this Mac" when it isn't installed, or is your own
  command), `@note`, plugins and script extensions; last,
  "Folders and sources…", folded unless there is an extension source, an update or an error: the plugins folder, Find
  Raycast scripts automatically, the extension folders (those that bring no new commands fold into one row), Add
  Folder… and the extension sources. A plugin or script extension command with suggestions has their switch under it,
  and **Show in the @ list** next to it.
- **More Settings**: the settings you rarely change, in five groups, a row each with what's in it; a click opens the
  group as a page of its own, with a back button.
  - **Input and keys**: each input's options under its name (English's words; Chinese's language pack, fuzzy pinyin,
    Personal Dictionaries and Removed candidates; Code's coding language, the coding languages installed and the coding
    language library), then the action key.
  - **Suggestions**: their switch, with Insert and "In these apps" under More… (open by itself once either is set).
  - **Privacy**: hiding sensitive information before sending, the words to hide (while it's on), Apps without AI, what
    `@agent` and `@reply` take from Chrome, learning English words, Learned…, and sending an anonymous install ID with
    the daily update check.
  - **Interface and sync**: Show in Menu Bar, the interface language, Show key hints (the keys explained at the bottom
    of the candidate box; off for a smaller box once you know them) and Sync through iCloud.
  - **Advanced**: typing results out (speed, typos), Previous per-app settings (only while an app has one), the config
    file and the Rime folder.
- **About**: the version, updates and "Check for updates automatically", Troubleshoot…, the four links in a row, and
  Report an Issue….

A few settings have no row unless they're set to something other than their default (by hand in the config file, or by
an earlier version): the output tokens, temperature, timeout and Thinking (AI), a kind of sensitive information left out
(Privacy), the settings, the jargon list and custom commands, or the learned words not synced (Sync through iCloud),
Insert's "ID only" (Suggestions), how many texts the clipboard history keeps (Common), "Use the selected text" turned off
(`useSelection`, Advanced), and a new version's notification turned off (About).
Then their row shows, with Restore Default. Shown or not, they work as before.

**Search.** Type in the field at the top of the sidebar and it lists the settings that match as you type (by name, by
what the row says and by the words they go by, in English and Chinese), each with its page (a group as "More
Settings › Privacy"); ↑↓ choose one, and ⏎ or a
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
permissions (Accessibility, controlling Notes, Reminders, Terminal and Messages, asked of macOS without a prompt; with
Accessibility not allowed, its row lists what doesn't work without it), secure
input, the language packs of your input languages, `config.json` (readable, unknown keys, values out of range, a language
twice, more than 5 translation languages), extensions and plugins that didn't load, updates, sync through iCloud (on or
off, when it last synced, the last error, iCloud Drive not available, settings from iCloud not used here), and recent
errors in the app's own logs. **Check** runs them again with Test Connection; with something in "What's wrong?
(optional)" ("why doesn't translate work"), the AI then explains the likely cause from the results and marks the fixes
it suggests. Each row shows as its check ends, what's known at once first, Test Connection last.

A row that can be fixed has a button that says what it does: Add Key…, Download, Open System Settings, Review Changes…,
Copy Command, Check for Updates. Review Changes… shows the settings it repairs as a preview, with Apply and Undo; the
others act at once: enabling the input method again, opening a System Settings pane, downloading a language pack,
Settings' key field, Check for Updates, or copying a command for Terminal ("Copied"). No fix deletes your data or
touches a key.

### Sync through iCloud (new)

Settings → More Settings → Interface and sync → **Sync through iCloud** (off by default) keeps your settings, jargon list, custom commands and the
words pinyin learned the same on all your Macs, through your own iCloud Drive: nothing else to sign in to, nothing through
our servers. It needs iCloud Drive (System Settings → Apple Account → iCloud); without it the switch stays off and says
so, with a button that opens that pane.

Once it's on, Settings shows one status row with a ⋯ menu (Sync Now; API keys and passwords; Remove from iCloud…), and
one switch under it: Hidden words and recent questions. Learned words sync with no switch of their own; turned off in the config, they show with Restore Default.

| What | What syncs | Default |
| --- | --- | --- |
| Settings | the settings in `config.json`: languages, rewrite styles, the action key, the magic key, typing out, per-app settings, hiding sensitive information (its switches), the AI provider and model (never a key) … | on |
| Jargon and custom commands | your jargon list and `customCommands` | on |
| Learned words | what pinyin learned from your choices (Rime's user dictionary, through librime's user-dictionary sync), words picked from a personal dictionary too, and your English words, added or learned (`englishWords`), and the candidates you removed (`removedCandidates`); your own Rime files, such as custom phrases, and the personal dictionaries themselves stay on the Mac | on |
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
- Turning off hidden words and recent questions leaves what was synced in iCloud until you remove it with **Remove from
  iCloud…** (below).
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
  recent apps, window state, Autocomplete (its switch and each app's choice: each Mac's own), Suggestions' switches (More Settings → Suggestions' and each app's), the plugins'
  completions turned on and their preferences (`completionSources`, `pluginPreferences`), the custom commands from
  another Mac still awaiting Allow (`unconfirmedCommands`), clipboard history and its settings (`clipboardHistory`,
  `clipboardHistoryLimit`), and the sync switches themselves (each Mac's own). What a
  suggestion row inserts and Code's language do sync, with the settings.
- Turning it off stops syncing and leaves everything as it is, on this Mac and in iCloud. **Remove from iCloud…** in the ⋯
  menu takes all of it out of iCloud: its confirmation lists what goes (the settings, custom commands and jargon list,
  learned words, hidden words and recent questions), then the folder goes to the Trash and sync turns off on this Mac;
  what is on this Mac stays, and API keys stay in iCloud Keychain. Other Macs still syncing put theirs back: turn it off
  there first.
- The settings search's Change: … ("sync through iCloud") turns it on or off; what syncs is only chosen in Settings →
  More Settings → Interface and sync. In the config: `iCloudSync` (`enabled`, `settings`, `jargon`, `learnedWords`, `hiddenWords`, `recentQuestions`, `keys`).

## This week's stats (new)

<img src="docs/en/week-stats.png" width="520" alt="This week's stats as a picture: 132 commands, 18% more than the same days last week, 12,340 characters typed, bars Monday to Sunday, the commands run most, where they came from and the clipboard history pastes">

How much you use AllInOneIME, week by week, and a picture of it to share. Settings → This Week (the first page in the
sidebar) shows the calendar week, Monday to Sunday in your time zone:

- How many commands you ran, and how that compares with last week up to the same weekday ("↑18% vs. the same days last
  week"; nothing when last week had none on those days; the first week says it's compared from next week on and which
  day counting started). How many days you used it, and in how many apps.
- How many characters you typed through AllInOneIME, under that ("12,340 characters typed"; not shown while there are
  none): each Chinese character picked, each letter, digit and punctuation mark typed through it, never spaces or line
  breaks. Not what commands, AI answers, snippets, autocomplete or clipboard history put in (only what you typed
  yourself), nothing while secure input is on (password fields), nothing where the input method lets every key
  through (without a language pack).
- A bar for each day, today named; days still to come and days without a command as a short gray bar.
- The 5 commands run most, each with its own icon and color as the command list shows it, then "4 more commands, 32
  runs in all" (or, with few, where to find every command: type @ at the start of a text field).
- Where they came from: your own commands, built-in ones and plugins (script extensions count as plugins), as a split
  bar, and how many of them sent a request to an AI provider.
- How many times you pasted from clipboard history: counts only, never what was pasted.

Last Week shows the whole week before. **Copy Image** puts the card on the clipboard as a picture (640 × 540 points, PNG
at twice the pixels, light or dark as your Mac is, in the first person: "This week I used"), **Save as Image…** saves it
as a PNG. **Hide my command names in the image** shows your own commands there as "My command 1", "My command 2" … (the
page keeps their names); it's remembered by the page, not a setting in config.json. A command run with one @ counts as the
command it ran. `@stats` shows the same in the @ list, and the menu bar panel has the week on top.

What is kept, on this Mac only, is counts and command names, never what you type: each command run (its name, where it
comes from, whether it used AI), per day; the apps it ran in, as salted hashes of their bundle IDs (only how many is
shown); clipboard history pastes; the characters you typed, as one number a day (counted as they go in, in memory). A
command of your own that you delete or rename loses its name there: its runs stay in the totals, as earlier commands.
Never what you typed, a command's text, what was pasted, or a time finer than the day. Nothing is counted during secure
input or in a field AllInOneIME knows is a password field. See [Privacy](#privacy).

## Menu bar panel

<img src="docs/en/panel-swipe.png" width="520" alt="The menu bar panel: frosted glass, with notes, reminders and Claude tasks on cards; a row swiped left shows its Remove button">

Click AllInOneIME's icon in the menu bar (the ∞-and-cursor mark, without a box; the boxed one is the input source) and the panel drops down under it; a click elsewhere closes it:

- This week, on top: "132 commands this week ↑18% ›"; click it for Settings → This Week (see [This week's stats](#this-weeks-stats-new)). Not shown before the first command is counted.
- Autocomplete: its switch, with the model it asks, where the text goes and how many suggestions were shown and taken (see [Autocomplete](#autocomplete-beta-new)).
- Notes: the notes saved with `@note`, the newest 5; click one to open it where it went: in Notes, in Obsidian or the file's own app, or the Notion page. A file that's gone is no longer listed.
- Reminders: the reminders not done yet in the AllInOneIME list of Reminders (`@reminder` adds to that list), the soonest due first, 8 shown; click the circle to tick one off, or the title to open Reminders.
- Claude Tasks: like `@tasks`, the background Claude tasks (what `@agent` hands off to Claude Code), up to 30, 5 shown at a time: scroll for more, or search their titles and replies in the search box; with their progress and the first line of the last reply; click one to open it in Terminal and go on.

Swipe a row (a note, a reminder or a task) to the left with two fingers to show its Remove button, or all the way to remove it at once; with a mouse, right-click it. Removing only takes it off the panel: the note stays in Notes, the reminder in Reminders (not completed), the task in Claude Code.

The header has the counts (like "2 reminders · 1 task running"; tasks waiting for you are counted apart, like "1 waiting for you") and a refresh button.
It never takes the focus from the app you're typing in: ticking off a reminder or refreshing leaves that app in front; only the Claude tasks' search box, once clicked, takes the keyboard.
The icon is shown by default; turn it off with "Show in Menu Bar" in Settings → More Settings → Interface and sync.

What it reads, and when:

- Notes: the list is the panel's own record (kept while it'