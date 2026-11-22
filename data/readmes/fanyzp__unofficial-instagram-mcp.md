<p align="center">
  <img src="docs/assets/banner.svg" alt="unofficial-instagram-mcp" width="920">
</p>

<h1 align="center">unofficial-instagram-mcp</h1>

<p align="center">Instagram, now accessible to your AI agent.</p>

<p align="center">
  <a href="https://mcpservers.org/servers/fanyzp/unofficial-instagram-mcp"><img src="https://mcpservers.org/badge.svg" alt="Listed on mcpservers.org"></a>
</p>

An unofficial Model Context Protocol (MCP) server for Instagram Web. It gives an AI agent a set of focused tools for messages, profiles, posts, comments, stories, and notifications.

The server connects to a Chrome window that is already signed in to Instagram. It does not use the Meta API, and it does not ask for or store an Instagram password.

## Quick start (no clone needed)

One command installs everything into your agent: it registers the MCP server and installs the Agent Skill. Pick your harness in the menu.

```bash
npx github:fanyzp/unofficial-instagram-mcp install
```

Or register the server in your MCP client config and let it run through npx directly:

```json
{
  "mcpServers": {
    "instagram": {
      "command": "npx",
      "args": ["-y", "github:fanyzp/unofficial-instagram-mcp"],
      "env": { "CDP_URL": "http://127.0.0.1:9222", "IG_DRY_RUN": "true" }
    }
  }
}
```

Then start Chrome as described below and call `ig_status`. Prefer working from source instead? Use the clone based install after this section.

> **Test first.** After connecting, run the built-in self-test to make sure every feature works end to end on your setup: call the `ig_selftest` tool or run `npm run selftest`. The default level only reads. The full level (`npm run selftest -- full`) exercises every write function on content it creates itself, then deletes all of it at the end. **Use a second account for testing, not your main account.**

## What it does

The server provides the capability layer. The user and the agent decide how to use it.

Use it to:

- Read and reply to Instagram direct messages.
- Get notified automatically when a new direct message arrives: the DM watcher monitors the inbox and pushes an MCP notification, so the agent can react on its own instead of polling.
- Check profiles, followers, following lists, posts, comments, stories, and notifications.
- Search users and hashtags, and browse the home feed, Explore page, and hashtag pages.
- Like posts and comments, reply to a specific comment, save posts, follow or unfollow users, and create posts.
- Run the same tools from an MCP client, the command line, or the interactive TUI.

The MCP tools use standard annotations. Read tools use `readOnlyHint`, and write tools use `destructiveHint`. The server also returns instructions that tell the agent to call `ig_status` first and to respect the `dryRun`, `sent`, and `alreadyLiked` fields in tool results.

## In use

An agent session in OpenCode, working through the MCP tools:

<p align="center">
  <img src="docs/assets/screenshots/opencode-search.png" alt="Agent session using the Instagram MCP tools in OpenCode" width="920">
</p>

## How it works

```text
MCP client, CLI, or TUI
          |
          v
unofficial-instagram-mcp
          |
          v
Playwright Core over CDP
          |
          v
Chrome window signed in to Instagram Web
```

All actions use the visible Instagram web interface. The project does not call private Instagram APIs. Selectors are kept in `config/selectors.json`, so most interface changes can be fixed in one place.

## Requirements

- Node.js 20 or newer
- Google Chrome or Chromium
- An Instagram account signed in in that browser
- An MCP client, if you plan to use the MCP server

## Install from source

```bash
git clone https://github.com/fanyzp/unofficial-instagram-mcp.git
cd unofficial-instagram-mcp
npm install
cp .env.example .env
```

On Windows PowerShell, copy the environment file with:

```powershell
Copy-Item .env.example .env
```

Keep `IG_DRY_RUN=true` for the first run. In dry run mode, write tools prepare and report the action without completing it.

## Start Chrome

Start Chrome with remote debugging enabled, then sign in to Instagram manually in that window.

Linux example:

```bash
google-chrome \
  --remote-debugging-port=9222 \
  --user-data-dir="$HOME/.local/share/unofficial-instagram-mcp/chrome"
```

The default CDP address is `http://127.0.0.1:9222`. Keep the debugging port available only on your own machine. Any local process that can reach this port can control the signed-in browser session.

## Give this to your AI agent

Paste this into your coding agent if you want it to set everything up for you:

```text
Set up unofficial-instagram-mcp for me and learn how it works before using it.

1. Read the Agent Skill first: https://github.com/fanyzp/unofficial-instagram-mcp/blob/main/skills/unofficial-instagram-mcp/SKILL.md
   It explains how the server works, the tool map, the workflows, and the safety rules. Follow it from now on.
2. Run the installer for your own harness: npx github:fanyzp/unofficial-instagram-mcp install --harness <your-harness-id> --scope user --yes
   Harness ids: claude-code, opencode, cursor, codex, gemini-cli, pi, oh-my-pi, openclaw, zcode, goose, amp, vscode, claude-desktop, windsurf, zed, generic.
   T3 Code has no MCP config of its own: it runs other providers and reads their configs, so use claude-code or codex for it.
   If your harness is not listed, register the server manually with command "npx" and args ["-y", "github:fanyzp/unofficial-instagram-mcp"], env CDP_URL=http://127.0.0.1:9222 and IG_DRY_RUN=true, and copy the skills/unofficial-instagram-mcp folder into your agent skills directory, keeping the folder name unchanged.
3. Start Chrome with remote debugging on port 9222 if it is not running yet. I will sign in to Instagram manually. Do not ask for or store my password.
4. Call ig_status first and confirm the signed-in username with me.
5. Before any write action, show me the exact target and content. Do not disable dry run unless I approve it.
```

## MCP configuration

Most MCP clients use a configuration like this. Replace the path with the absolute path to your clone.

```json
{
  "mcpServers": {
    "instagram": {
      "command": "node",
      "args": [
        "/absolute/path/to/unofficial-instagram-mcp/src/server.js"
      ],
      "env": {
        "CDP_URL": "http://127.0.0.1:9222",
        "IG_DRY_RUN": "true"
      }
    }
  }
}
```

### OpenCode

Add the server under the `mcp` key in `opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "instagram": {
      "type": "local",
      "command": [
        "node",
        "/absolute/path/to/unofficial-instagram-mcp/src/server.js"
      ],
      "enabled": true,
      "environment": {
        "CDP_URL": "http://127.0.0.1:9222",
        "IG_DRY_RUN": "true"
      }
    }
  }
}
```

After registration, restart the MCP client and ask the agent to call `ig_status`.

## Updating

Run the update command. It re-runs the installer with `--force`, which refreshes the Agent Skill files and rewrites the MCP registration with the latest version:

```bash
npx github:fanyzp/unofficial-instagram-mcp update
```

Installed from a clone instead? Run `git pull`, then `node bin/install.mjs --force`. If npx ever serves a stale cached copy, delete the `~/.npm/_npx` folder and run the command again. Or simply tell your agent: "update unofficial-instagram-mcp".

## Agent skill

This repository ships an [Agent Skills](https://agentskills.io) skill at `skills/unofficial-instagram-mcp/SKILL.md`. The MCP server gives the agent the tools; the skill teaches it how the server works, when to use each tool, the standard workflows, and the safety rules.

Installing both is the intended setup. The skill loads by progressive disclosure, so the agent carries only its name and description in context and reads the full instructions when an Instagram task comes up, instead of needing a long briefing in every session.

Four ways to install:

**1. One command through npx (MCP server + skill together, no clone).** This is the bundled installer running straight from GitHub:

```bash
npx github:fanyzp/unofficial-instagram-mcp install
```

It asks for the scope and the harness, then registers the MCP server and installs the skill in one run. Non-interactive form: add `--harness <id> --scope user --yes`.

**2. The standard skills CLI.** The open Agent Skills installer discovers the skill in this repository and lets you choose which agents (harnesses) to install it to:

```bash
npx skills add fanyzp/unofficial-instagram-mcp
```

Add `-g` for a user-wide install, or pin targets directly, for example `npx skills add fanyzp/unofficial-instagram-mcp -g -a claude-code -a opencode`. This installs the skill only; register the MCP server with the installer below or by hand.

**3. The bundled installer from a clone.** Same installer as route 1, run from a local clone of this repository:

```bash
node bin/install.mjs
```

It asks for the scope (user or this project) and the harness (16 targets: Claude Code, OpenCode, Cursor, Codex, Gemini CLI, Pi, Oh My Pi, OpenClaw, ZCode, Goose, Amp, VS Code, Claude Desktop, Windsurf, Zed, or a generic `.agents/skills` target; run it with `--list` for the ids), registers the `instagram` MCP server in that harness's own config format, and copies the skill into its skills directory where the harness supports skill folders. Existing config files are merged, not replaced. Non-interactive form:

```bash
node bin/install.mjs --harness claude-code,opencode --scope user --yes
node bin/install.mjs --all --scope project --dry-run
```

**4. By hand.** Copy the folder into your agent's skills directory (for example `~/.claude/skills/` for Claude Code, or the skills directory your client documents), keeping the folder name `unofficial-instagram-mcp` unchanged:

```bash
cp -r skills/unofficial-instagram-mcp ~/.claude/skills/
```

## CLI usage

List the available tools:

```bash
node src/cli.js tools
```

Run a few read operations:

```bash
node src/cli.js ig_status
node src/cli.js dm_check --limit 5
node src/cli.js dm_read_thread --threadId <thread-id>
node src/cli.js profile_get --username fanyzts
node src/cli.js search --query "balikpapan"
node src/cli.js post_comments --url <post-url> --limit 20
```

Write operations use the same form:

```bash
node src/cli.js dm_send --threadId <thread-id> --text "Thanks, I will check and reply soon."
node src/cli.js post_like --url <post-url>
node src/cli.js post_create --files ./photo.jpg --caption "Posted with an AI agent."
```

With `IG_DRY_RUN=true`, these commands report what would happen instead of completing the action.

## TUI usage

The TUI is the direct way to test the tools by hand. The main menu lists the tool categories (System, DM, Profile & Search, Posts, Discovery, Social, Stories); each category opens a sub-menu of its tools. It runs the tools against your live session right away and prints the raw result of each call:

```bash
npm run tui
```

## Tools

### Account and messages

| Tool | Description |
| --- | --- |
| `ig_status` | Check the browser connection and the signed-in account. |
| `ig_selftest` | Run the built-in self-test. The safe level only reads; the full level tests every write function and deletes its own test content. |
| `dm_list_threads` | List recent DM threads. Opening a thread can mark it as read. |
| `dm_check` | Find threads where the latest message came from the other person. |
| `dm_read_thread` | Read the latest messages in one thread. |
| `dm_send` | Send a message in an existing thread. |
| `dm_send_to_user` | Send a message to a user by username. |
| `dm_watch` | Start, stop, or check the DM watcher that monitors the inbox in the background. |
| `dm_events` | Read watcher events (verified new messages and watcher state changes) since a cursor. |
| `notifications_list` | Read recent likes, comments, follows, and mentions. |

### Profiles and social graph

| Tool | Description |
| --- | --- |
| `profile_get` | Read a profile, including counts and bio text. |
| `search` | Search from a keyword and return matching users, hashtags, posts, and reels shown by Instagram. |
| `followers_list` | List followers for a profile. |
| `following_list` | List accounts followed by a profile. |
| `user_follow` | Follow a user. |
| `user_unfollow` | Unfollow a user. |

### Content

| Tool | Description |
| --- | --- |
| `user_posts` | List recent posts and reels from a profile. |
| `post_get` | Read the author, time, media type, caption, and visible page text for a post. |
| `post_comments` | Read comments on a post. |
| `feed_home` | Read recent posts from the home feed. |
| `explore_posts` | List posts from the Explore page. |
| `hashtag_posts` | List posts from a hashtag page. |
| `media_urls` | Return the image and video URLs used by a post. |
| `stories_tray` | List accounts with an active story in the home tray. |
| `story_view` | Open a user story. Viewing it marks the story as seen. |

### Actions

| Tool | Description |
| --- | --- |
| `post_create` | Create a post from local image files and a caption. |
| `post_like` | Like a post or reel. Safe to call again if it is already liked. |
| `post_comment` | Add a comment to a post or reel. |
| `post_reply_to_comment` | Reply to one comment that matches the supplied text. |
| `comment_like` | Like one comment that matches the supplied text. |
| `post_save` | Save a post. Safe to call again if it is already saved. |
| `post_delete` | Delete one of your own posts by URL. Refuses posts owned by someone else. |
| `story_reply` | Reply to a user story. The reply is delivered as a direct message. |
| `story_create` | Create a story from an image file, or a text story when the web text editor is available. Not offered by Instagram Web for every account; see docs/VERIFICATION.md. |
| `story_create_poll` | Create a story with a poll sticker: a question and two options, on an image. Subject to the same Instagram Web limitation as `story_create`. |
| `story_delete` | Delete your own currently active story. |

## Common workflows

Check and answer messages:

```text
ig_status -> dm_check -> dm_read_thread -> dm_send
```

React to new messages automatically (auto-reply loop):

```text
dm_watch (start) -> on notification: dm_events -> dm_read_thread -> dm_send
```

The watcher takes a cheap inbox snapshot on an interval. When the snapshot changes, it verifies with `dm_check` before emitting an event, so an event means a real new message, not a layout flicker. Messages that already existed when the watcher started are treated as a baseline and are never reported. Each event carries the thread id, username, message text, and a spam flag for link-only and promo messages. Events are pushed as MCP notifications (`notifications/message`, logger `dm-watch`) and can always be pulled again with `dm_events`, which is the reliable path for clients that do not surface notifications. From the CLI, `node src/cli.js watch` streams the same events as JSON lines.

Join a discussion under a post:

```text
post_comments -> post_reply_to_comment
```

Research a topic:

```text
search or hashtag_posts -> post_get -> post_comments -> media_urls
```

Check engagement before replying:

```text
notifications_list -> post_comments or dm_check
```

## Self-test

The project ships with a self-test so you can verify the whole feature set on your own setup before real use. It is a recommendation, not a requirement.

Safe level, read only, works on any account:

```bash
npm run selftest
```

Or call the `ig_selftest` tool from your MCP client with `{ "level": "safe" }`.

Full level: creates its own test post and story, runs every write function against them (like, comment, reply, comment like, save, follow state restore, story view), then deletes everything it created. It only runs when all three gates are set in `.env`, and it refuses to run when the signed-in account does not match `IG_SELFTEST_ACCOUNT`:

```dotenv
IG_SELFTEST_FULL=true
IG_DRY_RUN=false
IG_SELFTEST_ACCOUNT=<username of your second account>
```

```bash
npm run selftest -- full
```

**Use a second account for the full level, not your main account.** The test cleans up after itself, but a second account keeps your main account's history and risk profile untouched.

Set `IG_SELFTEST_ON_CONNECT=true` if you want the safe level to run once automatically when the MCP server first connects. The result is written to the server log (stderr).

## Configuration

The server reads values from the environment and from `.env` in the project root.

| Variable | Default | Description |
| --- | --- | --- |
| `CDP_URL` | `http://127.0.0.1:9222` | Chrome DevTools Protocol address. |
| `USER_DATA_DIR` | Empty | Optional persistent browser profile. When set, the server opens that profile instead of connecting over CDP. Sign in manually once. |
| `IG_DRY_RUN` | `true` | When `true`, write tools simulate the final action. Set to `false` only when you are ready to perform real actions. |
| `IG_WATCH_INTERVAL_MS` | `60000` | DM watcher snapshot interval in milliseconds (minimum 15000). |
| `IG_WATCH_ON_CONNECT` | `false` | When `true`, the DM watcher starts automatically when the MCP server connects. |
| `IG_WATCH_LIMIT` | `8` | How many threads the watcher verifies when the inbox changes. |
| `MIN_DELAY_MS` | `2500` | Minimum delay between browser actions, in milliseconds. |
| `MAX_DELAY_MS` | `7000` | Maximum delay between browser actions, in milliseconds. |
| `IG_SELFTEST_ON_CONNECT` | `false` | When `true`, the safe self-test runs once when the MCP server first connects. |
| `IG_SELFTEST_FULL` | `false` | Gate for the full self-test level. Must be `true` together with the two settings below. |
| `IG_SELFTEST_ACCOUNT` | Empty | Username the full self-test is allowed to run on. It refuses to run on any other account. |
| `IG_SELFTEST_TARGET` | `instagram` | Account used for the follow and restore step of the full self-test. |
| `IG_SELFTEST_DM_TARGET` | Empty | Optional. Your own second account, used once for the `dm_send_to_user` step of the full self-test. |

## Safety and limits

- This is an unofficial project. It is not affiliated with Meta or Instagram.
- Use it only with your own account or an account you are authorized to operate.
- Keep dry run enabled while testing. Check the target, text, and result before approving a real action.
- Opening a DM thread can mark it as read. Viewing a story marks it as seen.
- Instagram can change its web interface without notice. When that happens, selectors or page flows may need an update.
- Instagram may limit or restrict automated activity. Use reasonable delays and volume, and stop if Instagram shows a warning or checkpoint.
- A real signed-in browser makes the actions look like normal web use, but it does not guarantee that an account will never be limited.

## Verification status

The original 34 tools were live tested on a second account on 16 November 2026: **31 of 34 pass**. The 3 remaining tools (`story_create`, `story_create_poll`, `story_delete`) are blocked by an Instagram Web platform limitation, not by this code. The two watcher tools added in v0.3.0 (`dm_watch`, `dm_events`) are verified at unit, protocol, and live-browser state level; the one step still open is a real DM arriving into a signed-in watched browser, as recorded in [docs/VERIFICATION.md](docs/VERIFICATION.md).

Full per-tool results, the test environment, and the run notes live in [docs/VERIFICATION.md](docs/VERIFICATION.md).


## Development

Project layout:

```text
src/server.js       MCP server over stdio
src/tools.js        Tool definitions, categories, and MCP annotations
src/instagram.js    Instagram web actions
src/browser.js      CDP and persistent profile handling
src/cli.js          Command line interface
src/tui.js          Interactive terminal interface (category sub-menus)
src/selftest.js     Built-in self-test, safe and full levels
src/run-selftest.js CLI runner for the self-test
src/watcher.js      DM watcher: inbox snapshots, verification, event queue
bin/install.mjs     Installer: registers the MCP server and installs the skill per harness
config/selectors.json
skills/unofficial-instagram-mcp/SKILL.md   Agent skill that teaches agents this server
test/mcp.test.mjs   MCP protocol tests that do not need a browser
test/dom.test.mjs   DOM extraction tests against fixtures
test/watcher.test.mjs DM watcher rules with injected fakes (no browser)
test/fixtures/      Image used by the full self-test
```

Run the checks:

```bash
npm run check
npm test
```

The test suite covers the MCP handshake, tool discovery, annotations, server instructions, ping, unknown methods, a tool call made without a browser connection, the self-test gate that refuses the full level without its safety settings, the DOM extractors against fixtures, and the DM watcher rules (baseline, dedupe, spam flag, signed-out state) with injected fakes.

## License

[MIT](LICENSE)
