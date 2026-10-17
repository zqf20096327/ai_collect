# clanker.nvim

AI code completion and modification for neovim v0.12+. The intent is to have a minimal, fast, and unobtrusive plugin that helps you write code without getting in your way.

## Features

- **Smart Completion** - Context-aware code generation at cursor
- **Range Modification** - Select and transform code with AI
- **Explicit Generation** - Ask for specific code with instructions

## Installation

```lua
-- Using vim.pack.add
vim.pack.add({ src = "https://github.com/hansmrtn/clanker.nvim" })
require("clanker").setup()
```

Set your API key:
```bash
export ANTHROPIC_API_KEY="your-key-here"
```

## Usage

### Complete at Cursor
**Command:** `:LLMComplete`  
**Keybinding:** `<leader>lc`

Generates code based on surrounding context. If no context exists, prompts for instructions.

### Ask for Specific Code
**Command:** `:LLMAsk <instruction>`  
**Keybinding:** `<leader>la`

Generate code with explicit instructions like `:LLMAsk write a binary search function`

### Modify Selected Range
**Command:** `:'<,'>LLMModify`  
**Keybinding:** `<leader>lm` (visual mode)

Select code, press `<leader>lm`, optionally add instructions, and the AI will refactor/improve it.

#### Ghost Text

All completions appear as grayed-out preview text:
- Press `<Tab>` to accept
- Press `<Ctrl-e>` to reject
- Works in both normal and insert mode

## Configuration

```lua
require("clanker").setup({
  api_url = "https://api.anthropic.com/v1/messages",
  model = "claude-sonnet-4-20250514",
  max_tokens = 1000,
  context_lines = 50,  -- Lines of context before/after cursor
})
```

## Example Usage 

```lua
-- 1. Write a comment describing what you need
-- TODO: function to validate email addresses
|  -- cursor here, press <leader>lc

-- 2. Select existing code in visual mode
function add(a, b)
  return a + b
end
-- Press <leader>lm, type "add type checking"

-- 3. Ask for something specific
-- Press <leader>la, type "create a quicksort implementation"
```

## Commands

| Command | Key | Description |
|---------|-----|-------------|
| `:LLMComplete` | `<leader>lc` | Complete at cursor |
| `:LLMAsk` | `<leader>la` | Generate with instruction |
| `:'<,'>LLMModify` | `<leader>lm` | Modify range selection |

