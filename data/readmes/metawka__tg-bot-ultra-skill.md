# Telegram Bots skill for Claude Code

A Claude Code skill for building Telegram bots on Bot API 10.x: rich messages with tables, headings and buttons inside the message, colored buttons, custom emoji icons, collapsible blocks, slideshows, maps and streamed AI answers. It comes with an MCP server that creates bots and changes their settings in @BotFather.

## Features

- Detailed interview with the bot owner before any code: product, data, style and every screen layout, with live previews sent to the bot chat.
- Design rules and approved screen patterns: object cards, lists, search, filters, quantity steppers, receipts, errors, empty states, ratings.
- Icon catalog for seven custom emoji packs, mapped by meaning (home, back, settings, user and more), with a no-Premium layout.
- Hosting choice between Telegram Serverless and a regular server.
- Bot profile setup through the Bot API: name, descriptions, commands, menu button, photo.
- `botfather` MCP server: creates bots, fetches tokens into `.env`, walks BotFather menus. It can access only the @BotFather chat; deleting bots, revoking tokens and transferring ownership are blocked.

## Examples

Screens built with the skill's patterns on a test bot (Telegram Desktop, dark theme).

| | | |
|---|---|---|
| ![Order card](docs/screenshots/order.png) | ![Product card](docs/screenshots/product-card.png) | ![Catalog grid](docs/screenshots/catalog-grid.png) |
| Order card: status heading, field table, colored buttons | Product card: specs table, expandable review, button rows | Catalog: 2×N grid with a highlighted action |
| ![Search results](docs/screenshots/search.png) | ![Catalog groups](docs/screenshots/catalog-groups.png) | ![Map](docs/screenshots/map.png) |
| Search: highlighted matches, number buttons | Catalog: groups with item buttons inside | Delivery: map block with a caption |
| ![Collapsed specs](docs/screenshots/product-collapsed.png) | ![Warning](docs/screenshots/warning.png) | ![Rating](docs/screenshots/rating.png) |
| Collapsed specs, main action on its own row | Warning with details in a collapsible block | Rating row, best score in green |

## Requirements

- Claude Code
- Python 3.11 or newer with tkinter (included in the python.org installers)
- For the MCP server: a Telegram account and API keys from https://my.telegram.org (API development tools)
- Custom emoji icons in bot messages require Telegram Premium on the bot owner's account

## Installation

### Ask your agent

Paste this into Claude Code (or any coding agent that can run commands):

```text
Install this skill: https://github.com/metawka/tg-bot-ultra-skill
```

The agent clones the repository, runs `install.py`, and tells you when to restart.

### Command line

```bash
git clone https://github.com/metawka/tg-bot-ultra-skill.git
cd tg-bot-ultra-skill
python install.py
```

The installer copies the skill to `~/.claude/skills/telegram-bots`, creates a virtual environment for the MCP server in `mcp/botfather/.venv`, and registers the server in Claude Code for all projects. Keep the cloned folder: the server runs from it. Restart Claude Code afterwards.

Options: `--dry-run` prints the steps without changing anything, `--skill-only` installs only the skill.

### Manual installation

```bash
cp -r skills/telegram-bots ~/.claude/skills/
cd mcp/botfather
python -m venv .venv
.venv/bin/pip install -r requirements.txt
claude mcp add --scope user botfather -- "$(pwd)/.venv/bin/python" "$(pwd)/server.py"
```

On Windows use `.venv\Scripts\pip` and `.venv\Scripts\python.exe`.

### Update

```bash
git pull
python install.py
```

### Removal

```bash
claude mcp remove botfather -s user
rm -rf ~/.claude/skills/telegram-bots ~/.tg-botfather
```

### Sign-in

On first use Claude calls the `login` tool, which opens a local window:
1. Create an app at my.telegram.org → API development tools (any title, platform Desktop) and paste API ID and API hash into the window.
2. Scan the QR code in Telegram (Settings → Devices → Link Desktop Device), or choose sign-in with a phone number and enter the code Telegram sends.
3. Enter the cloud password if the account has one.

Keys and the session are stored in `~/.tg-botfather` and never pass through the chat. Sign-in errors are written to `~/.tg-botfather/login.log`. To sign out, delete that folder and end the session in Telegram under Settings → Devices.

## Usage

Ask Claude Code for a bot in your own words, for example:

> Make a Telegram bot for my coffee shop: menu, pre-orders for a pickup time, loyalty points.

Claude creates the bot, asks you to press Start in it, runs the interview with previews in the bot chat, shows a summary of decisions, then builds and sets up the bot.

## Repository layout

| Path | Contents |
|---|---|
| `skills/telegram-bots/SKILL.md` | Workflow and rules |
| `skills/telegram-bots/references/` | Interview, design rules, rich message reference, icons, bot setup, hosting, verification |
| `skills/telegram-bots/scripts/` | Preview sender, owner lookup, username check, icon pack dump |
| `skills/telegram-bots/assets/icon-roles.json` | Icon ids by meaning |
| `mcp/botfather/` | MCP server and sign-in window |
| `install.py` | Installer |
| `docs/screenshots/` | Screenshots used in this README |

## License

MIT, see `LICENSE`.
