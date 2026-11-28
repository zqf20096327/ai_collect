<p align="center">
  <img src="docs/images/banner.png" alt="Bloub, a small cloud with eyes: more than an assistant. Proactive: he notices what's coming and gets to work before you ask." width="100%">
</p>

<h1 align="center">Bloub</h1>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License: MIT"></a>
  <a href="#requirements"><img src="https://img.shields.io/badge/macOS-27.2%2B-black?style=for-the-badge&logo=apple" alt="macOS 27.2 or newer"></a>
  <img src="https://img.shields.io/badge/Swift-SwiftUI-orange?style=for-the-badge&logo=swift&logoColor=white" alt="Written in Swift and SwiftUI">
</p>

<p align="center">
  <a href="#install">Install</a> · <a href="#what-he-does">What he does</a> · <a href="#safety">Safety</a> · <a href="#privacy">Privacy</a>
</p>

An AI assistant for the Mac. He lives in the notch and has a full app window with a chat and a coding mode.
Bloub is a small cloud with eyes, written in Swift, and runs on Claude with your own API key.

<p align="center">
  <a href="https://nubidubi09.github.io/Bloub/"><img src="docs/images/demo.webp" alt="A 45-second walkthrough: Bloub notices an unstarted talk, writes the outline and asks; the notch, a long chat, code, browser, subagents, connectors, memory and approvals" width="100%"></a>
</p>
<p align="center"><sub>45 seconds, animated from the app's screens. <a href="https://nubidubi09.github.io/Bloub/">Watch it in full quality</a>.</sub></p>

<table>
<tr><td><b>Works before you ask</b></td><td>Looks at your calendar and chats on his own, prepares what you need and asks when something is missing</td></tr>
<tr><td><b>Lives in the notch</b></td><td>Hold <b>⌥⌘</b> and talk, or type; he can see your screen</td></tr>
<tr><td><b>Does real work</b></td><td>Files, a real terminal, his own browser, subagents and sub-sessions</td></tr>
<tr><td><b>Connects</b></td><td>Mac Calendar, Notion and other MCP services (<a href="#connectors-mostly-untried">mostly untried</a>)</td></tr>
<tr><td><b>Remembers and learns</b></td><td>A memory you can read and edit, search through past conversations, skills</td></tr>
<tr><td><b>Yours</b></td><td>Open source, your own API key, no account, no analytics</td></tr>
</table>

> **Early project, use it at your own risk.** Expect faults. The code has **not been security audited** and is not
> guaranteed to be secure: read [Its limits](#safety) before you give it a folder or a key. It is not signed by
> Apple, so it builds on your own Mac, and it needs a very new macOS (see [Requirements](#requirements)).

## Install

```bash
brew install --HEAD nubidubi09/bloub/bloub
```

Homebrew downloads the code and builds the app on your Mac, which takes a few minutes. Then:

```bash
bloub
```

Open **Settings** (⌘,) → **AI** and paste your [Claude API key](https://platform.claude.com/settings/keys). It is
stored in your Mac's Keychain.

| | |
| --- | --- |
| Update | `brew upgrade --fetch-HEAD bloub` |
| Uninstall | `brew uninstall bloub` |
| Your data | `~/Library/Application Support/Assistant` (delete it to start over; the key is the Keychain item `com.notchassistant.Assistant`) |

### Requirements

- macOS 27.2 or newer
- Xcode 27.2 (the full app), with up-to-date Command Line Tools
- [Homebrew](https://brew.sh)
- A Claude API key. You pay Anthropic for what you use; Bloub shows the cost of each answer and can stop at a monthly
  limit you set.

## What he does

### On his own (new, off until you switch it on)

In **Settings → On his own** you let Bloub work without being asked. While your Mac is awake and Bloub runs, he looks
every 15 minutes and after changes (your calendar, a finished chat or session, waking the Mac). He takes a cheap look
first, and only if something changed or is coming up does he decide whether there is anything worth doing, for example
preparing notes for a talk or noticing that two plans clash. There is also a morning brief and an evening report.

- **He may read:** your chats, Code sessions and memory, files in your home folder (not hidden files, `Library`,
  `Applications` or key files), Mac Calendar if connected, connector tools set to **Allow**, and, if you switch them on,
  iMessage (needs Full Disk Access) and the Mail app's inbox.
- **He does alone:** reading, and writing, changing or deleting files, with a copy of the old version and **Undo**.
  Connector tools set to **Allow** run too, also ones that change things.
- **He waits for your click:** sending a message or mail, adding or deleting a calendar event, every other connector
  tool, and searching the web (only the search words you approve are sent).
- He runs **no commands**. He stops at your daily limit ($2 to start) and your monthly limit.
- If he needs something from you, he **asks** on the Activity page and in the notch; your answer lets him carry on.

What he did is on the **Activity** page; news also opens the notch and, if you allow it, a Mac notification.

<p align="center">
  <img src="docs/images/activity.jpg" alt="Bloub's Activity page: he noticed an unstarted talk outline, wrote one, and asks which part should get the most time" width="760">
</p>

**Only a first try with the real Claude so far.** Sending real messages and mail, Mac notifications, and waking after
calendar changes have not been tried.

### In the notch

Tap **⌥⌘** and type, or hold it and talk: the notch stretches to both sides, with bars that move with your voice
and dots while he thinks. Each question you ask there goes with a picture of your screen, so you can ask about what
you see. macOS asks for permission the first time: Input Monitoring (the shortcut), Microphone and Speech Recognition
(talking), and Screen Recording (looking at your screen).

**Your latest chats** are at the left edge of the screen. Touch the edge, click the small handle, and pick a chat to
see its last answer in the notch and reply. You can search all your chats there, or lock the list so it stays open.

### Chat

![A chat with Bloub](docs/images/chat.jpg)

Formatted answers with copyable code, Stop and Regenerate, images, PDFs and text files, web search with sources,
a memory you can read and edit, search through your history, and **Send now** to cut in while he is answering.

![A chat in light mode](docs/images/chat-light.jpg)

### Code

Pick a folder. Bloub reads and edits files in it, runs commands, and uses a real terminal and a browser next to the
chat. Changes he makes with his file tools can be undone (what commands do cannot). Choose how much he asks first: **Plan first**, **Ask first** or **Automatic**.

**Subagents** take on one separate task each. The **Running tasks** panel shows what each was asked to do, and
**Send now** passes him a message at his next step.

![A subagent at work](docs/images/running-tasks.jpg)

**Sub-sessions** are sessions of their own for a separate piece of work. Bloub proposes one, you edit what it will
know, pick its folder and press Start. Its report comes back to the first session.

![Starting a sub-session](docs/images/sub-propose.jpg)

![A sub-session reporting back](docs/images/sub-report.jpg)

### Connectors (mostly untried)

In **Customize → Connectors** you add services that speak MCP: a searchable list of 88 (Notion, Linear, Todoist,
Figma, GitLab and more), your own web address, or a program on your Mac. Bloub can then use their tools in Chat, Code
and the notch (subagents can't). In **Settings → Connectors** you set each tool to **Allow**, **Ask** (the start) or
**Block**, or all of a service's tools at once; the **+** by the typing box switches connectors per chat or session.

**Mac Calendar** reads the events of your Mac's calendars and prepares new ones, which are added only after you click.
It asks for macOS's calendar permission, never sends invitations and can't change events yet; deleting one is only
proposed by Bloub on his own and waits for your click. It has only been tried with a stand-in calendar.

Google Calendar, Gmail, Drive and Chat need your own app ID: Google doesn't let an app sign itself up, so you create
one in Google Cloud (type "Desktop app") and paste it into Bloub once. If it belongs to someone else's Google account,
yours must be added there as a test user; Google's "personal mode" works only for its owner.

**Only signing in to Notion has been seen to work with a real service.** Everything else, Google included, has been
tried against stand-ins in the tests; for the listed services only their public sign-in details were read, and some may
refuse Bloub. Only tools work (not MCP's other parts), and apart from Google, services that require apps to be
registered by hand don't connect.

### Memory and settings

![What Bloub remembers](docs/images/memory.jpg)

![Model, spending limit and key](docs/images/settings.jpg)

Also: slash commands (type `/`), skills you can install from a GitHub link (a repository with several shows each) or
let Bloub write for you, saved only after you OK them, and a choice of
Opus 5.5, Sonnet 5.5 or Haiku 5.5.

### Other providers (untested)

In **Settings → AI** you can add **OpenAI**, **Google Gemini**, **Kimi** or **your own address** (any service with
the OpenAI chat format, including a model on your Mac), type your models and their prices, and pick them in Chat and
Code.

**This has never been tried against the real services**, only against stand-ins in the tests. It may fail or behave
differently, especially with files and commands in Code. Web search, page reading and shown thinking work with Claude
only, PDFs reach other models as text, and a model without a price does not count toward your monthly limit.

## Safety

What the app enforces:

- In Chat and Code, Bloub's file tools work only inside the folder you picked, never in `.git`. On his own they work
  in your home folder, without hidden files, `Library`, `Applications` and key files.
- On his own, messages, mail and calendar changes wait for your click. A connector tool you set to **Allow** runs
  without one.
- Deleting a file always asks. In Automatic, commands that delete or throw away work still ask.
- In his browser, clicks and typing ask first (except scrolling and plain links on the same site), and he never types
  passwords or card numbers. A web address that carries data asks first.
- Text on web pages and in reports is treated as information, not as instructions.
- Starting a subagent or a sub-session always needs your OK.
- A connector's tool asks first, showing everything it would receive, until you set it to Allow ("Allow all" asks you
  once more). A blocked tool is not shown to the model, and a tool the service changed asks again. While a plan waits
  in Code, every connector use asks.
- A program on your Mac runs as a connector only after you agree to its exact command.

Its limits, so you know them:

- **Commands run with your own rights.** There is no sandbox around them. In Automatic, a script that deletes files,
  or a command that uploads them, runs without asking.
- Data hidden in a web address's path or site name is not detected.
- **Connector programs run with your own rights**, like any program you start.
- Text from a connected service could try to mislead the AI into sending data elsewhere, for example through a web
  page he reads, a tool you set to Allow, or in Code a command that Automatic runs without asking. Switch off what a
  chat or session doesn't need.
- On his own, what others write to you (messages, mail, calendar invitations, files they send) can try to steer him
  while you are not watching. He could then change a file, even a script you run later (the old version is kept), or use
  a connector tool you set to Allow. Think about this before switching it on.
- An AI can be wrong or be misled by what it reads. Use **Ask first** for anything that matters, and keep backups.
- These protections are checked by the project's own tests only. Nobody independent has reviewed them, and there is
  **no warranty** (see the [licence](LICENSE)).

## Privacy

- Sent to Anthropic (or to the other provider you pick, which then receives the same things): your messages, attached files, a screenshot with each question you ask in the notch (if Screen Recording is allowed), the contents of
  files and command results Bloub reads in Code, what he sees in the browser, past chats he looks up, and the memory
  notes that go with a question. Web search runs there too.
- Websites opened in the browser receive the usual requests; the address bar searches with DuckDuckGo. Installing a
  skill reads it from GitHub.
- Speech is recognised on your Mac when macOS supports that, otherwise by Apple's service.
- With connectors, what Bloub sends to a tool goes to that service, and its reply goes to the model. With Mac
  Calendar, the events he reads (titles, times, places, notes, guests) go to the model.
- On his own, whatever he reads for a job goes to Anthropic with your key, **including messages and mail other people
  sent you** once you switch those on.
- Chats, sessions, memory and settings stay on your Mac, **unencrypted**. Keys, connector sign-ins and your Google app
  ID are in the Keychain.
- No analytics, no account.

The full text: [privacy policy](PRIVACY.md) and [terms of use](TERMS.md).

## Build it in Xcode

```bash
git clone https://github.com/nubidubi09/Bloub.git
cd Bloub
open Assistant.xcodeproj
```

The project is signed with the author's own certificate, so first select the **Assistant** target →
**Signing & Capabilities** → set the signing certificate to **Sign to Run Locally**. Then press **Run**.

Run the tests (they never call the real Claude API):

```bash
xcodebuild test -project Assistant.xcodeproj -scheme Assistant -only-testing:AssistantTests CODE_SIGN_IDENTITY=-
```

## Where things are

| Path | What |
| --- | --- |
| `Assistant/` | The app (SwiftUI and AppKit) |
| `Assistant/Claude.swift`, `CodeAgent.swift` | Talking to Claude, and Code mode's tool loop |
| `Assistant/Autopilot.swift` | Working on his own |
| `Assistant/Bloub.swift` | The cloud and how he moves |
| `AssistantTests/` | Tests |
| `design/` | The icon set |
| `packaging/bloub.rb` | The Homebrew recipe |

## Working on it

Bloub is built by Ben together with Claude Code and GitHub Copilot, one small step at a time.

If you like the little cloud, a ⭐ on this repo helps others find him.

Want to help? Read [CONTRIBUTING.md](CONTRIBUTING.md). Found a security problem? See [SECURITY.md](SECURITY.md).

## Licence

[MIT](LICENSE). The terminal uses [SwiftTerm](https://github.com/migueldeicaza/SwiftTerm) (MIT). The service logos
come from [Simple Icons](https://simpleicons.org); they are trademarks of their owners, are not covered by this
licence, and Bloub is not affiliated with those companies.
