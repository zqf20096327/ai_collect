<p align="center">
  <img src="https://raw.githubusercontent.com/necromancer124/facedown/main/docs/images/banner.svg" alt="facedown: a .env file for AI agents. They use your secrets by name, but never see the values." width="100%">
</p>

<p align="center">
  <a href="https://github.com/necromancer124/facedown/actions/workflows/test.yml"><img src="https://github.com/necromancer124/facedown/actions/workflows/test.yml/badge.svg" alt="tests"></a>
  <a href="https://www.npmjs.com/package/facedown"><img src="https://img.shields.io/npm/v/facedown?color=0d9488" alt="npm"></a>
  <img src="https://img.shields.io/badge/node-%E2%89%A520-339933" alt="Node 20 or newer">
  <img src="https://img.shields.io/badge/platform-Windows%20(Linux%20%26%20macOS%20planned)-0078d4" alt="Windows for now">
  <img src="https://img.shields.io/badge/dependencies-0-0d9488" alt="no dependencies">
  <a href="LICENSE"><img src="https://img.shields.io/github/license/necromancer124/facedown?color=64748b" alt="MIT license"></a>
  <a href="https://registry.modelcontextprotocol.io/v0/servers/io.github.necromancer124%2Ffacedown/versions/latest"><img src="https://img.shields.io/badge/MCP%20Registry-listed-7c3aed" alt="Listed in the official MCP Registry"></a>
  <a href="https://glama.ai/mcp/servers/necromancer124/facedown"><img src="https://img.shields.io/badge/Glama-MCP%20server-f97316" alt="facedown MCP server on Glama"></a>
</p>

AI coding agents read your project files. If your `.env` holds passwords and
API keys, the AI sees them in plain text, and they end up in chat
transcripts, logs and sometimes in code.

**facedown** is a `.env` file the AI can **use** but never **read**. It sees
which secrets exist and what they are for, and it can run your code or call an
API with them. The real values go straight to your program or to the sites you
allowed, never to the AI.

```
You:     /addKey GITHUB_TOKEN token for the GitHub API
         → a private window opens on your screen, you type the value there
Claude:  Saved GITHUB_TOKEN.

You:     list my GitHub repos
Claude:  ▶ http_request  Authorization: Bearer {{GITHUB_TOKEN}}
         → facedown fills in the real token, sends the request,
           and hides the token in whatever comes back
```

**Why "facedown"?** Like a card played face down: it counts in the game, but
nobody at the table sees what it is. The AI plays your secrets face down.

> **Status: v0.4 preview. Windows for now; Linux and macOS are planned.**
> Needs Node 20 or newer, no other dependencies.

> **What 1.0 promises:** facedown stops keys leaking *by accident*: into the
> chat, logs, transcripts or a program's output. It does not stop an agent or
> program that is deliberately trying to steal a key (see
> [what it protects, and what it does not](#what-it-protects-and-what-it-does-not));
> `--proxy` goes further for web APIs.

## How it works

<p align="center">
  <img src="https://raw.githubusercontent.com/necromancer124/facedown/main/docs/images/how-it-works.svg" alt="The AI asks to use GITHUB_TOKEN. facedown gives the real value to your program or to an allowed API, blocks other sites, and hands the AI the output with the value hidden." width="100%">
</p>

Secrets live in one file in your project, `.env.facedown`:

```ini
# facedown vault v1 id=Qm9iX2lk

# @desc token for the GitHub API
# @allow api.github.com
GITHUB_TOKEN=enc:v2:8kZ0…

# @desc Postgres password (local)
DB_PASSWORD=enc:v2:Lw91…
```

- **Names, notes and allowed sites are plain text.** The AI reads them to know
  what exists.
- **Values are encrypted** (AES-256-GCM). The unlock key is *not* in the
  project: it is in your home folder (`~/.facedown/keys/`), and on Windows it
  is locked to your Windows account.
- **There is no command that prints a value.** A secret only ever goes to the
  environment of a program you run, or into a web request to a site you
  allowed.
- **Logs show the key name, not the value.** If a program prints a secret it
  comes out as `***GITHUB_TOKEN***`, also when it was base64, hex or URL
  encoded first.
- **You approve the risky steps.** Typing a value, allowing a new site and
  deleting a secret all happen in a window on your screen.

## Install

You need [Node.js](https://nodejs.org) 20 or newer.

**Claude Code** (the MCP server plus five slash commands, in every project).
Type this in Claude Code:

```
/plugin install facedown --marketplace necromancer124/facedown
```

On Claude Code older than 2.1.275, use two steps instead:

```
/plugin marketplace add necromancer124/facedown
/plugin install facedown@facedown
```

Then start a new session.

**Command line:**

```bash
npm install -g facedown
```

Or run it without installing: `npx facedown help`.

> **Renamed:** this project was called **blind-env** for its first day. If you
> installed that, switch to `facedown`. Old `.aienv` vaults and their keys keep
> working: facedown finds and reads them.

**From source:**

```bash
git clone https://github.com/necromancer124/facedown
```
```bash
cd facedown
```
```bash
npm link
```

## Use it in Claude Code

| Command | What it does |
|---|---|
| `/addKey NAME what it is for` | Opens a password window. You type the value; Claude never sees it. |
| `/keys` | Lists names, notes and allowed sites. Never values. |
| `/allowSite NAME api.example.com` | Lets a key be sent to a site. You confirm in a window first. |
| `/removeSite NAME api.example.com` | Stops a key being sent to a site. |
| `/removeKey NAME` | Deletes a secret. You confirm in a window first. |

Everything else you just ask for in plain words ("use GITHUB_TOKEN to list my
repos"), and Claude uses the facedown tools.

<table>
  <tr>
    <td width="33%"><img src="https://raw.githubusercontent.com/necromancer124/facedown/main/docs/images/password-window.png" alt="Password window: Enter the secret value for GITHUB_TOKEN. It is encrypted on this computer. The AI never sees what you type here."></td>
    <td width="33%"><img src="https://raw.githubusercontent.com/necromancer124/facedown/main/docs/images/allow-window.png" alt="Confirmation window: Allow GITHUB_TOKEN to be sent to uploads.github.com? Allow or Cancel."></td>
    <td width="33%"><img src="https://raw.githubusercontent.com/necromancer124/facedown/main/docs/images/delete-window.png" alt="Confirmation window: Delete the secret GITHUB_TOKEN? Delete or Cancel."></td>
  </tr>
  <tr>
    <td align="center"><b>/addKey</b>: you type the value</td>
    <td align="center"><b>/allowSite</b>: you approve new sites</td>
    <td align="center"><b>/removeKey</b>: you approve deletes</td>
  </tr>
</table>

In the windows, Enter means **Cancel**: approving always takes a click.

## Use it in a terminal

<p align="center">
  <img src="https://raw.githubusercontent.com/necromancer124/facedown/main/docs/images/terminal-demo.svg" alt="Terminal: facedown set GITHUB_TOKEN, facedown list, facedown run -- node app.js prints ***GITHUB_TOKEN*** instead of the value, facedown check shows ok, length and fingerprint." width="100%">
</p>

```bash
facedown set GITHUB_TOKEN --desc "token for the GitHub API" --allow api.github.com
```

You type the value with hidden input. If there is no terminal to ask in, the
password window opens instead.

**Already have a `.env` file?** Move all its keys into the vault in one go:

```bash
facedown import .env
```

Values are never shown. The comment line above a key becomes its description.
Afterwards facedown offers to delete the plain-text `.env` (you confirm in a
window; `--keep` skips the question).

```bash
facedown run -- node app.js
```

`app.js` reads `process.env.GITHUB_TOKEN` as usual. Your code can be in any
language: it is just an environment variable.

In your own terminal, leaving out `--keys` passes every key. Without a terminal
(which is how an AI agent runs commands) `run` asks for the keys by name, so a
program only ever gets the secrets it needs:

```bash
facedown run --keys GITHUB_TOKEN -- node app.js
```

`--all-keys` passes every key on purpose. Avoid it when an AI runs the command:
any program it starts would see all your secrets.

Read keys inside your program, not in the command itself: `run` refuses a
command that would expand a key onto a command line (`%GITHUB_TOKEN%`,
`$GITHUB_TOKEN`), because other programs on the computer can read a process's
command line and facedown can't hide it there. With `--proxy` it's allowed,
since the command line then only gets a placeholder.

Only a program's *output* is cleaned. The program itself gets the real value,
so if it writes the key to a file or sends it somewhere, facedown doesn't stop
that; run only programs you'd trust with the key. (A test shows this limit with
a fake token. With `--proxy`, the program only ever has a placeholder.)

| Command | What it does |
|---|---|
| `facedown init` | Create a `.env.facedown` vault in this folder (`set` does it for you) |
| `facedown set NAME` | Add or replace a secret (`--desc`, `--allow`, `--stdin`) |
| `facedown list` | Names, notes and allowed sites (`--json`) |
| `facedown check` | Confirms each secret decrypts; shows length and a fingerprint |
| `facedown run --keys A,B -- cmd` | Run a command with those secrets as environment variables |
| `facedown allow NAME site…` | Set the allowed sites (adding one asks you first) |
| `facedown rm NAME` | Delete a secret (asks you first) |
| `facedown export FILE` / `import FILE` | Move a vault to another computer, with a passphrase |
| `facedown import .env` | Move the keys of a plain `.env` file into the vault |
| `facedown doctor` | Check the whole setup and say what's wrong |
| `facedown log [NAME]` | When each key was used, by which tool, for which site (never the value) |
| `facedown mcp` | Start the MCP server for AI agents |

### Debugging: printing a secret is allowed

Your code can log a secret like any other variable. The log shows which key it
was instead of the value, and how it was encoded:

```
[debug] connecting with token ***GITHUB_TOKEN*** | as base64: ***GITHUB_TOKEN:base64***
facedown: note: hid the value of GITHUB_TOKEN (2x) in the output. Logs show the key name instead of the value.
```

- `--quiet` drops the note line.
- `--strict` treats a printed secret as an error and fails the run with exit
  code 97. Set `FACEDOWN_STRICT=1` to make every run strict.

`facedown check` shows a fingerprint that stays the same until the value
changes, so you can tell "still the old token" from "the new one" at a glance.
It is made with the vault key and the key name, so it cannot be used to guess
the value.

### Allowed sites

A key can only be sent (with `http_request`) to the sites on its list. A new
key has an empty list.

```bash
facedown allow GITHUB_TOKEN api.github.com
```

- `allow` sets the whole list, so name every site you want.
- `*.github.com` covers every subdomain (not `github.com` itself).
- `facedown allow NAME api.github.com --for 2h` allows a site for a while
  only (`30m`, `2h`, `1d`, up to 30 days); it stops by itself. Good when a key
  is needed for one task. The end time is part of the encryption too, so it
  can't be extended by editing the file.
- `facedown allow NAME --clear` removes all sites.
- **Adding a site to a saved secret always asks you first**, in a confirmation
  window on Windows (or a y/N question in a terminal elsewhere), even when an
  AI runs the command. Removing sites needs no confirmation.
- `set NAME --allow site` sets the sites together with a **new** value, so no
  window asks about them: a value already stored is never sent anywhere new
  this way. When you type the new value in the password window, new sites are
  marked `NEW` there.
- The list is protected by the encryption: if someone adds a site by editing
  `.env.facedown` by hand, that key stops working instead of being sent there.

### Moving to another computer

A vault only opens on the computer and Windows account that made it. To take
your secrets along, export them with a passphrase you choose:

```bash
facedown export backup.facedown
```

On the new computer, in your project folder:

```bash
facedown import backup.facedown
```

- Both commands ask for the passphrase in a window (or with hidden typing in a
  terminal on Linux and macOS). There is no way to pass it on the command line
  or through stdin, and no MCP tool for either: only you can export.
- The export holds every secret, with its note and allowed sites, encrypted
  with your passphrase (scrypt and AES-256-GCM). **Keep the file safe**: with
  the passphrase it opens everything in it. Delete it once it is imported.
- `import` adds to the vault in the current folder, or makes a new one. If a
  name already exists there, nothing is imported.

### Programs that call web APIs: `--proxy` (experimental)

Normally a program run with facedown gets the real key, so whatever it does
with it (put it on a command line, write it to a file) is up to the program.
With `--proxy`, the program never gets the real key at all:

```bash
facedown run --proxy --keys GITHUB_TOKEN -- node app.js
```

1. The program gets a placeholder, like `facedown-placeholder-GITHUB_TOKEN-3f9a…`.
2. facedown starts a small proxy on your computer for the length of the run and
   points the program at it.
3. When the program calls a site on the key's allowed list, the proxy puts the
   real key into that request. Replies get it turned back into the placeholder.
4. Every other site, the command line, files and output only ever see the
   placeholder, which is worthless.

So even `curl -H "Authorization: Bearer %GITHUB_TOKEN%"` is safe: other programs
on the computer only see the placeholder on curl's command line. The AI turns it
on with `proxy: true` in `run_with_secrets`.

How it works: to put the key into an encrypted (HTTPS) request, the proxy acts
as a trusted middleman. facedown makes a certificate authority for that one run,
in memory only, and tells the program to trust it; the proxy itself checks the
real site's certificate as usual. Sites no key may go to are tunnelled
untouched.

Limits:

- Web APIs only. A database password still has to be the real value.
- The program has to use the standard proxy settings. Tried and working:
  Node 24 `fetch`, Python (`requests`, including sessions, streaming and
  chunked uploads, and `urllib`), curl (also curl on Windows).
  Node 20 and 22's built-in `fetch` ignore proxy settings.
- Experimental: tell us what works and what doesn't
  ([#23](https://github.com/necromancer124/facedown/issues/23)).

The idea came from a discussion with
[u/Deynekin](https://www.reddit.com/user/Deynekin/) on r/mcp.

### Something not working? Did it use my key?

```bash
facedown doctor
```

checks Node, the vault, its unlock key, that every key decrypts, a plain
`.env` still lying around, the windows and the MCP server, and says what to
fix. `facedown log` shows every time a key was used (which tool, which site,
the command), and `facedown list` shows when each value was last set, so you
can spot keys that are due for a change. The log never holds a value.

## For other AI agents (MCP server)

`facedown mcp` is a standard MCP server, so any agent that speaks MCP can use
it (setup for Cursor, VS Code and Claude Desktop: [docs/CLIENTS.md](docs/CLIENTS.md)). Without the plugin, for Claude Code in your project folder:

```bash
claude mcp add facedown -- facedown mcp
```

The agent gets six tools:

| Tool | What it does |
|------|--------------|
| `list_keys` | Which vault file is in use, plus names, notes and allowed sites. Never values. |
| `add_key` | Opens a private window where **you** type the value. |
| `run_with_secrets` | Runs a command with the chosen keys as environment variables (in `cmd.exe` on Windows, so `%NAME%`). Output is cleaned. The command also gets the AI app's own environment variables, which facedown does not hide. |
| `http_request` | Sends a web request with `{{KEY_NAME}}` filled in. Only to allowed sites, HTTPS only, redirects not followed, response cleaned. |
| `allow_hosts` | Adds or removes allowed sites. Adding opens a confirmation window; nothing changes unless **you** click Allow. |
| `remove_key` | Deletes a secret. Opens a confirmation window; nothing is deleted unless **you** click Delete. |

If you open this repo itself in Claude Code, `.mcp.json` and
`.claude/commands/` give you the server and the commands without installing
anything. Start the session in the repo folder: a session that starts
elsewhere does not load them until it moves into the repo.

## What it protects, and what it does not

**It does protect against:**

- secret values ending up in the chat, the AI's memory, transcripts or logs;
- the AI reading secrets from a file in your project;
- a program printing a secret by accident;
- a web page tricking the AI into sending a key to the wrong site through
  `http_request`.

An allowed site is trusted with the key. If you allow `api.github.com`, the AI
could still send the token there in a way that stores it, for example inside a
new gist. Allow only the API a key is for, and keep `run_with_secrets` and
`http_request` approvals in Claude Code switched on for anything sensitive.

**It does not protect against an AI that has a shell and is trying to steal a
secret.** An agent that can run any command as you can write a program that
scrambles the secret before printing it (so the cleaner misses it), sends it to
a server, unlocks the key file the same way facedown does, or even "click" the
confirmation window with simulated key presses. Nothing running under your own
account can fully stop that.

So think of facedown as a seat belt, not a vault door: it stops the common,
accidental ways secrets leak to an AI. The strongest setup is an agent that has
**only** the `http_request` tool and no shell. Then the allowed-sites list is a
real barrier.

Other limits:

- Values must be at least 8 characters. Hiding a short value gives it away
  (`test` masked inside `testing` shows what it is), so shorter ones are
  refused unless `--allow-short` is given. Only use that for things that
  really are short, like a PIN: a short value is easy to spot in output, and
  values under 4 characters are not hidden at all.
  Key names are never masked, even when a value appears inside one.
- The vault only opens on the computer and account that created it. To move
  it, use `facedown export` and `facedown import`.
- The windows exist on Windows only. On Linux and macOS use `facedown set
  NAME` in a terminal; those platforms are untested.

Found a security problem? See [SECURITY.md](SECURITY.md). Think you can get a
secret out anyway? [Try to break it](docs/CHALLENGE.md).

## Thanks

People whose ideas made facedown better:

- [u/Deynekin](https://www.reddit.com/user/Deynekin/): keys on a program's
  command line ([#19](https://github.com/necromancer124/facedown/issues/19)),
  narrower allowed sites, a use log, rotation, and the boundary design that led
  to `--proxy` ([#23](https://github.com/necromancer124/facedown/issues/23)).
- [u/sparkignitefire](https://www.reddit.com/user/sparkignitefire/): making the
  `run_with_secrets` boundary concrete with a fake-token test
  ([#18](https://github.com/necromancer124/facedown/issues/18)).

## Hall of fame

People who found a real security problem in facedown and reported it
privately. Thank you.

*No one yet. [Be the first](docs/CHALLENGE.md).*

## More

- [FAQ and troubleshooting](docs/FAQ.md)
- [Cursor, VS Code, Claude Desktop and other MCP tools](docs/CLIENTS.md)
- Examples: [Node](examples/node-github) and [Python](examples/python-api)

## Fun fact

The runner-up name was **`.env.broker`**, because it is *the better env*.
It was just a little too cheesy. (And before that, for one day, the project
was called blind-env.)

## Tests

```bash
npm test
```

The tests run on every push on Windows with Node 20, 22 and 24. The full manual
test, written as a prompt for an AI session, is in
[docs/TEST-PROMPT.md](docs/TEST-PROMPT.md).

## Updates

Once a day facedown asks npm whether there is a newer version, and says so in
one line after a command (and in `list_keys`, so your AI agent tells you). It
never updates anything by itself, and when you are offline it says nothing.

- A version with a **known security problem** gets a loud warning: the owner
  marks it on npm with a message starting with `SECURITY`.
- `FACEDOWN_BLOCK_INSECURE=1` turns that warning into a hard stop: `run`,
  `export`, `run_with_secrets` and `http_request` refuse until you update. It is
  off by default on purpose: a hijacked npm account must not be able to stop
  everyone, and facedown must keep working offline. If the check cannot reach
  npm, facedown carries on.
- `FACEDOWN_NO_UPDATE_CHECK=1` turns the check off (it is also off in CI). The
  check sends nothing about you or your secrets: it is a plain download of
  facedown's public package info.

## Versions

facedown uses [semantic versioning](https://semver.org). What stays stable from
1.0 on (the vault format, commands, flags, MCP tools and environment variables)
is in [docs/STABILITY.md](docs/STABILITY.md); every change is in
[CHANGELOG.md](CHANGELOG.md).

## Roadmap

- Linux and macOS: keychain protection for the key, and the windows
- `login` tool: fill a username and password into a browser form
- "This key may only be used by this command" rules for `run_with_secrets`

## License

MIT, see [LICENSE](LICENSE).
