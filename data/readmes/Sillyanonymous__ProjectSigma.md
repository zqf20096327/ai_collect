# Project Σ

A self-hosted home for your AI character cards. Project Σ keeps your characters, their chats, lorebooks, personas and
gallery media in one library on your own machine, lets you search it like a database, chat with your characters through
your own AI connection, and browse the popular character sites without leaving the app.

Project Σ is the successor to the [Character Library](https://github.com/Sillyanonymous/SillyTavern-CharacterLibrary)
extension for SillyTavern: you can see it as a standalone Character Library.

It runs as a small server on your computer or a home server, and you use it from any browser on your network, phones
included. Everything lives in one `data/` folder. The library is built to stay quick at sizes that would stall a folder of
card files: it is designed for libraries of a million characters.

![Project Σ: the library on the desktop, a conversation on a phone](docs/assets/screenshots/hero.webp)

This page is the tour and the common questions; [the user guide](https://sillyanonymous.github.io/ProjectSigma/guide.html) covers every feature and option. The
guide is one page that opens in any browser: online at that link, in the app under **More Options** > **User Guide**, or
`docs/guide.html` in the install folder.

## What it does

- <img src="docs/assets/icons/users.svg" width="16" height="16" alt=""> [A library that scales](https://sillyanonymous.github.io/ProjectSigma/guide.html#library). A fast grid with eleven sort orders, favorites, playlists with icons
  and colours, and a Tags Manager that renames, merges and cleans up tags across the whole library. Select one character
  or every character in the current view and tag, favorite, export or delete them in one go. Find duplicates, and ask an
  AI connection to recommend characters from your own library.
- <img src="docs/assets/icons/magnifying-glass.svg" width="16" height="16" alt=""> [Search that understands cards](https://sillyanonymous.github.io/ProjectSigma/guide.html#search-and-filters). Press the key under <kbd>Esc</kbd> anywhere for
  Search everything, one box over your characters, chats, messages, lorebook entries and settings. In the library,
  search names, tags, creators, notes or card text; narrow with prefixes such as `creator:`, `fav:yes` or `chub:no`; and build Advanced Filters from more than twenty
  fields (token count, last chat, linked lorebook, alternate greetings and more), saved as presets.
- <img src="docs/assets/icons/id-card.svg" width="16" height="16" alt=""> [Every card detail, editable](https://sillyanonymous.github.io/ProjectSigma/guide.html#characters). Read and edit every field of a card, its embedded and
  linked lorebooks, and its picture. Each edit can be snapshotted first, so version history shows a field-by-field diff
  and restores any earlier state.
- <img src="docs/assets/icons/comments.svg" width="16" height="16" alt=""> [Chats that run here](https://sillyanonymous.github.io/ProjectSigma/guide.html#chats). A full conversation screen: streaming replies, alternates you swipe
  through, continue, regenerate, "write my next message", branching a chat from any message, hidden messages, thinking
  shown in a fold, and export to JSONL. Attach pictures to a message when the model sees them, and keep a gallery for
  each chat beside its character's. Around the conversation sit a prompt manager (it imports SillyTavern chat-completion presets and builds
  them the way SillyTavern does), regex scripts, a header you arrange yourself, a prompt inspector that shows exactly what is sent, an Author's note, chat backgrounds, and an out-of-character
  assistant that knows your persona and the Author's note and can propose lorebook, message, card, note and persona
  edits for you to review. See also
  [chat windows](https://sillyanonymous.github.io/ProjectSigma/guide.html#conversation-tools).
- <img src="docs/assets/icons/plug.svg" width="16" height="16" alt=""> [Your own AI connection](https://sillyanonymous.github.io/ProjectSigma/guide.html#connections). Any endpoint that speaks the OpenAI-compatible chat API, local
  or hosted, plus Anthropic's API through a bundled extension. Keys stay on the server and are never sent back to the
  browser.
- <img src="docs/assets/icons/book-atlas.svg" width="16" height="16" alt=""> [Lorebooks](https://sillyanonymous.github.io/ProjectSigma/guide.html#lorebooks). A manager with every entry option, books linked to characters, bound to one
  chat, tied to a persona or active everywhere, a chat window that shows which entries fired and why, and AI generation
  of entries from pasted text, a wiki page or your own characters.
- <img src="docs/assets/icons/masks-theater.svg" width="16" height="16" alt=""> [Personas with pronouns](https://sillyanonymous.github.io/ProjectSigma/guide.html#personas). Be someone different everywhere or in one chat only, with a
  picture, bound lorebooks and pronouns that cards can use through `{{sub}}`, `{{obj}}` and friends.
- <img src="docs/assets/icons/plus-circle.svg" width="16" height="16" alt=""> [A creator with a design partner](https://sillyanonymous.github.io/ProjectSigma/guide.html#creator). Write a card from scratch or start from one in your
  library, with a Studio that talks the whole draft through with you and proposes changes you apply one by one.
- <img src="docs/assets/icons/globe.svg" width="16" height="16" alt=""> [The character sites in one tab](https://sillyanonymous.github.io/ProjectSigma/guide.html#online). Browse ChubAI, JanitorAI, JannyAI, CharacterTavern,
  Pygmalion, Wyvern, Botbooru, DataCat and the RisuAI Realm; see at a glance what you already own; import in
  the background; keep linked characters up to date with a field-by-field update check.
- <img src="docs/assets/icons/photo-film.svg" width="16" height="16" alt=""> [Media that stays put](https://sillyanonymous.github.io/ProjectSigma/guide.html#media). Each character has a gallery for images, video and audio, a full-screen
  viewer, and a downloader that pulls the remote images a card links to, including whole albums from common image hosts,
  so nothing breaks when a host goes away.
- <img src="docs/assets/icons/palette.svg" width="16" height="16" alt=""> [Make it yours](https://sillyanonymous.github.io/ProjectSigma/guide.html#settings-and-themes). A theme editor with presets and a live preview, a custom CSS
  editor, and a CSS assistant.
- <img src="docs/assets/icons/puzzle-piece.svg" width="16" height="16" alt=""> [Extensions](https://sillyanonymous.github.io/ProjectSigma/guide.html#using-extensions). A bundled set (memory summaries, trackers, a translator, story beats,
  ratings and notes, library stats, and more), each off until you switch it on, and installable extensions from a git
  URL or a zip. The bundled set is vibe-coded: written entirely by AI as a stress test of the extension API, not reviewed
  line by line, and meant as examples rather than core features. An installed extension runs with full access to your
  server, every account on it and the computer it runs on, and Project Σ does not review extensions or answer for what
  they do: read [Before you install anything](https://sillyanonymous.github.io/ProjectSigma/guide.html#using-extensions/before-you-install-anything)
  first.
- <img src="docs/assets/icons/database.svg" width="16" height="16" alt=""> [Built to be trusted with your library](https://sillyanonymous.github.io/ProjectSigma/guide.html#data-and-backups). Optional accounts with a separate library
  each, scheduled database backups, a consistency checker, and a migration that brings a whole SillyTavern library
  across and verifies it. See also [accounts](https://sillyanonymous.github.io/ProjectSigma/guide.html#accounts-and-server).
- <img src="docs/assets/icons/server.svg" width="16" height="16" alt=""> [An API underneath](https://sillyanonymous.github.io/ProjectSigma/guide.html#api). Everything the app does goes through a documented HTTP API: power users can
  automate tasks and script their own library with it (bulk tagging and cleanup, scheduled imports and exports, backups
  on a timer, reports on the collection), and extension creators build on it.

![A character's details: the picture, tags and playlists beside the card's description and first message](docs/assets/screenshots/details.webp)

![Search everything: one box that finds characters, chats, messages and lorebook entries, with the top hit previewed](docs/assets/screenshots/search-everything.webp)

![The Chats view: every conversation grouped by day, the latest one large at the top](docs/assets/screenshots/chats.webp)

![A conversation with the out-of-character assistant open beside it](docs/assets/screenshots/conversation.webp)

![The lorebook manager: a book's entries, the character it is linked to, and one entry open for editing](docs/assets/screenshots/lorebooks.webp)

![Browsing ChubAI inside the app, narrowed to original fantasy elves with tag filters](docs/assets/screenshots/online.webp)

![Check for updates: a linked character's changes on its site, compared field by field before anything is written](docs/assets/screenshots/updates.webp)

![The same library in the default look and in the bundled Midnight theme](docs/assets/screenshots/themes.webp)

## Quick start

Requires Node.js 22.15 or newer. Get the code with git:

```
git clone https://github.com/Sillyanonymous/ProjectSigma.git
cd ProjectSigma
```

or with **Code** > **Download ZIP** on GitHub, unpacked. Then, in that folder:

```
npm install
npm start
```

Or let a launcher do it: double-click `Start Project Sigma.bat` on Windows, or run `sh start.sh` on Linux, macOS and
Android (in Termux; [the guide](https://sillyanonymous.github.io/ProjectSigma/guide.html#getting-started/running-it-on-an-android-phone)
has the steps). It
checks that Node.js is new enough, installs what Project Σ needs on the first run and again after an update, starts the
server and opens your browser on it (`openBrowser: false` in `data/server.yaml` keeps it from that). Keep its window open
while you use the app; closing it stops the server.

Open http://localhost:7788 and the app loads. All state lives in the `data/` folder next to the install. To use it from
your phone, open the same address with this computer's network address in place of `localhost`.

With Docker instead: `docker compose -f docker/compose.yaml up -d` from the install folder. [docker/README.md](docker/README.md)
covers the volumes, updating, and the optional browser for the sites behind Cloudflare.

New to it? [Getting started](https://sillyanonymous.github.io/ProjectSigma/guide.html#getting-started) walks through the first ten minutes.

## Bringing a SillyTavern library

Project Σ can bring a whole SillyTavern user folder across (the folder holding `characters/`, `chats/` and `worlds/`,
usually `data/default-user`): cards with their tags and favorites, chats, lorebooks and their links, gallery media,
version snapshots, playlists, personas, custom CSS, saved prompts and filter presets. The SillyTavern folder is only ever
read, never changed.

The easy way is the wizard: **Settings** > **Account** > **Bring your SillyTavern library**. Point it at the folder,
press **Check** to read the plan, run it, and finalize when you are satisfied. Re-running is always safe until you
finalize: every character heals in place and nothing duplicates.

From a terminal, the same tool:

```
npm run migrate -- <path-to-st-user-dir> --user <handle> --dry-run
npm run migrate -- <path-to-st-user-dir> --user <handle>
npm run migrate -- <path-to-st-user-dir> --user <handle> --finalize
```

The first prints the plan and writes nothing; the second runs the migration and finishes by verifying it against the
source, field by field and message by message; the third verifies one last time and makes the migrated characters
indistinguishable from ones created here. Group chats, SillyTavern's own settings and its asset folders stay behind.
Every flag, the exit codes and the full list of what comes across are in
[Bringing a SillyTavern library](https://sillyanonymous.github.io/ProjectSigma/guide.html#sillytavern-migration).

## FAQ

### Is this a SillyTavern extension?

No. It is a standalone app with its own server and database. It can import a SillyTavern data folder, and chats export
in SillyTavern's JSONL format, but it does not need SillyTavern installed.

### Do I need an AI model to use it?

No. The library, search, editing, lorebooks, online browsing and media all work without one. Chatting, the assistant,
the Studio, the Card Recommender, AI lorebook generation, the CSS assistant and some extensions need a connection, which
you add under **Settings** > **AI**.

### Which AI services work?

Any endpoint that offers the OpenAI-compatible chat completions API, which covers most hosted services and local
servers; the endpoint you enter includes the API's version path, for example ending in `/v1`. Anthropic's own API works
through the bundled Anthropic extension.

### Is my API key safe?

It is stored on the server, in your library's database, and the browser never receives it back: the app only ever shows
"Key stored" and its last four characters. Treat your `data/` folder and its backups as you would any file holding a
key.

### Can I use it on my phone?

Yes. The app switches to a phone layout with a bottom bar, swipe gestures and full-screen sheets. Open the server's
address from the phone's browser while both are on the same network.

### Can several people share one install?

Yes. Turn on accounts (`multiUser: true` in `data/server.yaml`) and each person gets a separate library, settings and
media. Without accounts there is no sign-in, so anyone who can reach the port can use and change everything. [Accounts
and server settings](https://sillyanonymous.github.io/ProjectSigma/guide.html#accounts-and-server)

### Which card formats does it read?

Card PNGs (V1, V2 and V3) and CHARX files, plus Project Σ's own bundles. It exports card PNGs and full bundles with
chats and gallery media. JSON card files are not imported.

### Does it do group chats?

No. Every chat has one character; a SillyTavern migration counts group chats and leaves them where they are.

### How do I back up?

**Settings** > **General** > **Library Backup** takes a copy of the database on demand or on a daily or weekly schedule.
It does not cover images, so copy the whole `data/` folder now and then too. [Data and
backups](https://sillyanonymous.github.io/ProjectSigma/guide.html#data-and-backups)

### Something broke after I turned on an extension

Switch it off under **Settings** > **Extensions**. If the app will not open far enough for that, start the server with
`CL_EXTENSIONS=off`: the app runs with every extension dark while you remove the broken one's folder from
`extensions/installed/`.
[Troubleshooting](https://sillyanonymous.github.io/ProjectSigma/guide.html#troubleshooting) covers this and the other common snags.

### Should I use a theme, Custom CSS or a theme extension?

For colours, corners, spacing and fonts, use the theme editor: it is quick, follows you to every device and keeps
working across updates. For anything else (one component, a picture, hiding something), use Custom CSS snippets, which
take any CSS but can stop matching when an update changes the app's markup. A theme extension packages a look for every
account on a server, and a full one like the bundled Midnight or Σ adds its own settings, palettes and motion.
[Themes, Custom CSS and theme extensions](https://sillyanonymous.github.io/ProjectSigma/guide.html#settings-and-themes/themes-custom-css-and-theme-extensions)
compares them in full.

## Configuration

Server settings live in `data/server.yaml`, which the first boot writes with a comment on every setting. Where a setting
has an environment variable, the variable wins over the file.

| `server.yaml` key | Environment variable | Default | What it sets |
|---|---|---|---|
| `multiUser` | `CL_MULTI_USER` (`true` or `false`) | `false` | Sign-in and a separate home per account |
| `sessionTimeoutDays` | | `30` | How long a sign-in lasts, in days; `-1` for no limit (a browser still keeps the sign-in at most 400 days) |
| `port` | `CL_PORT` | `7788` | The port the server listens on |
| `host` | `CL_HOST` | `0.0.0.0` | The address it binds: every interface by default, so a phone on your network can reach it; `127.0.0.1` keeps it to this machine |
| `cors` | `CL_CORS` (comma-separated) | none | The other origins whose pages may call the API, such as a dashboard or tool of your own served from another address (`*` for any) |
| `hosts` | `CL_HOSTS` (comma-separated) | none | With multi-user off, the machine names the server answers besides IP addresses and localhost, so a page on another site that points its own name here is refused |
| `openBrowser` | `CL_OPEN_BROWSER` (`true` or `false`) | `true` | Whether the launchers open the browser once the server answers; `false` for a server run headless, as a service, or with a tab already open |

These are set only in the environment:

| Environment variable | Default | What it sets |
|---|---|---|
| `CL_DATA_DIR` | `data/` in the install | Where every library, account and `server.yaml` itself live, which is why the file cannot move it |
| `CL_EXTENSIONS_DIR` | `extensions/installed/` in the install | Where installed extensions and their `.data/` scratch folders live |
| `CL_EXTENSIONS` | `on` | `off` boots with every extension dark: the way back in when one breaks the app |
| `CL_BROWSER` | a Playwright Chromium, else Chrome or Edge, found on the machine | The browser the hosted-browser services launch, tried before any found |

The server reads `server.yaml` strictly: a setting it does not know, or a value of the wrong kind (`multiUser: yes`, a
`sessionTimeoutDays` that is not a number), stops the boot with a message naming the setting, rather than starting a
server configured differently from what was meant. The yes-or-no and number variables are read the same way
(`CL_MULTI_USER=1` stops the boot too).

## For power users and extension creators

- The API: everything the app does goes through the public HTTP API, so you can automate tasks and script your own
  library: bulk tagging and cleanup, scheduled imports and exports, backups on a timer, reports on the collection, or
  your library feeding tools of your own. The live spec is at `GET /api/openapi.json`; a browsable reference is
  `docs/api-docs.html` (regenerate it with `npm run docs`). [The API](https://sillyanonymous.github.io/ProjectSigma/guide.html#api) covers signing in, calls from
  another site and the live change feed.
- Extensions: the extension API gives extensions the same reach as the app's own code: events, storage, settings,
  windows, views and providers. [The extension authors' guide](https://sillyanonymous.github.io/ProjectSigma/guide.html#extensions), the user guide's last part,
  is the reference.
- Checking a library: `npm run verify` reads every library in `data/` against the consistency rules the server keeps
  (foreign keys, the search indexes, the maintained counts, the files behind their rows) and exits non-zero naming any
  finding. `npm run verify -- --user <handle>` checks one account; `--db-only` skips the walk over the files on disk,
  the one check whose time grows with a large media folder. `--repair <check>` fixes what a check found, for the
  checks that have a repair, after taking a backup; run it with the server stopped. It also lists who owns each table
  of a library (the app, each extension, or nobody), and `--drop-leftover <id>` drops the tables a removed extension
  left behind, after asking and taking a backup.
- No build step: the client is plain JS, CSS and HTML served as is.

Issues are welcome; pull requests are closed. [CONTRIBUTING.md](CONTRIBUTING.md) says how to report a problem and why an
extension is the way to change the app.

## Acknowledgements

Big thanks to [SillyTavern](https://github.com/SillyTavern/SillyTavern), the de facto roleplay platform. It taught me a
lot, and Character Library would not have been possible without it, since it started as a SillyTavern extension.

Big thanks to Rivelle of [Moonlit Echoes](https://github.com/RivelleDays/SillyTavern-MoonlitEchoesTheme): she made
SillyTavern bearable to look at for me and taught me a lot of good UX practices.

Acknowledgements to three SillyTavern extensions: nothing was lifted from them, but they served as inspiration.

- [SillyTavern Tracker](https://github.com/kaldigo/SillyTavern-Tracker) by kaldigo, for the bundled **Trackers**
- [Pathweaver](https://github.com/mattjaybe/SillyTavern-Pathweaver) by mattjaybe, for the bundled **Next Beat**
- [ST-Copilot](https://github.com/Supker/ST-Copilot) by Quren, for the Assistant

## License

Source available for personal use; see [LICENSE](LICENSE) for the terms and [NOTICE](NOTICE) for the bundled third-party
components. The license is deliberately narrow for now, to protect the time and work behind the project while it finds
its feet; the intent is to loosen it in the future. Forking the repository on GitHub to run and change for yourself is
fine; a fork keeps this license, so it stays non-commercial and is not re-hosted or published elsewhere. The extension
API is the open door: extensions are your own work, under whatever license you choose, and the bundled extensions are
MIT, so any of them can be the start of yours.
