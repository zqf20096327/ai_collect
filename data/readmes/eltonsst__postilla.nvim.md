# postilla.nvim

[![CI](https://github.com/eltonsst/postilla.nvim/actions/workflows/ci.yml/badge.svg)](https://github.com/eltonsst/postilla.nvim/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Neovim](https://img.shields.io/badge/Neovim-0.10%2B-57A143?logo=neovim&logoColor=white)](https://neovim.io/)

**Review the code your agent wrote, line by line, inside Neovim.**

Postilla lets you attach comments to source lines without changing the files.
When the review is done, it copies structured feedback to your clipboard, ready
to paste into Codex or another coding agent.

No pull request. No temporary notes. No files to add to `.gitignore`.

## Features

- Add multiline comments to exact lines or line ranges.
- Review every changed file in a split or unified diff with a files panel.
- Comment on deleted lines, like in a pull request review.
- Write in a bottom split while the reviewed code stays visible.
- Keep comments attached when code moves and warn when reviewed code changes.
- Jump between comments and preview the final feedback inside Neovim.
- List, edit, and delete comments before export.
- Restore unfinished reviews after restarting Neovim.
- Export [revdiff](https://github.com/umputun/revdiff)-compatible feedback.

## Install

With [lazy.nvim](https://github.com/folke/lazy.nvim):

```lua
{
  "eltonsst/postilla.nvim",
  opts = {
    keymap = "<leader>rc",
    next_keymap = "]r",
    previous_keymap = "[r",
  },
}
```

Postilla also works without `setup()`. You can use its commands directly.

## Review in 60 seconds

Start a review:

```vim
:PostillaStart
```

Move the cursor to a line and add a comment:

```vim
:PostillaComment
```

If you configured the example keymap, press `<leader>rc` instead.

To comment on a range, select the lines in Visual mode and press `<leader>rc`.
Character and block selections are expanded to complete lines.

Write your comment in the bottom split:

- `<C-s>` saves the comment and returns to the source file.
- `<Esc>` in Normal mode cancels it.

Repeat this for every line you want to review. Saved comments look like this:

```text
💬 R1. Consider extracting this helper...
💬 R2 [80-84]. This section is too long...
```

Use `]r` and `[r` to move between comments with the example configuration.
Preview the complete feedback without ending the session:

```vim
:PostillaPreview
```

Finish the review:

```vim
:PostillaDone
```

Postilla copies all comments to the `+` clipboard register. Paste them into
your coding agent and continue the conversation.

## Review a diff

To review everything that changed since the last commit, open the diff review:

```vim
:PostillaDiff
```

Postilla opens a new tab with three windows:

- a files panel with every changed file, its status, and its line counts
- the old version of the file, read-only
- the working file, which you can still edit

Comment on any line with `:PostillaComment` or your keymap. A comment in the
old version marks a deleted line; a comment in the working file marks an added
or unchanged line.

Pass a revision to review a whole branch, like a pull request:

```vim
:PostillaDiff main
```

Postilla compares against the commit where your branch forked from that
revision. Commits that landed on `main` afterwards are not shown. Uncommitted
changes in the working tree are included.

In the files panel:

| Key | Action |
| --- | --- |
| `<CR>` or `o` | Open the file's diff, or fold the group on a group heading |
| `r` | Mark the file as reviewed, or clear the mark |
| `H` | Hide or show reviewed files |
| `R` | Reload the changed files |
| `q` | Close the diff review |
| `g?` | Show the keys and the main commands |

### File groups

The panel lists files in four groups, in the order worth reviewing them:
Implementation, Tests, Documentation, and Generated. Each heading shows how
many of its files are reviewed. Press `<CR>` on a heading to fold the group;
next and previous file then skip it.

Postilla works out the group from the path (for example `_test.go`, `docs/`,
`go.sum`) and from a generated-code header such as Go's
`// Code generated ... DO NOT EDIT.` To decide yourself, set an attribute in
`.gitattributes`:

```gitattributes
internal/legacy/**   review-generated
scripts/check.sh     review-test
```

The attributes are `review-implementation`, `review-test`,
`review-documentation`, and `review-generated`. GitHub's `linguist-generated`
and `linguist-documentation` work too. Set `diff.group_files = false` for one
flat list sorted by path.

### Split or unified

The diff has two layouts. Switch with `:PostillaLayout`, or pick one with
`:PostillaLayout split` or `:PostillaLayout unified`.

- **Split** shows the old version and the working file side by side. The
  working file is the real file, so you can edit it and use your LSP.
- **Unified** shows one column with removed lines above added lines, and the
  old and new line numbers in front. It is read-only.

Both layouts show the whole file with unchanged regions folded. Comments work
the same way in both, and switching keeps you on the same line.

Run `:PostillaPanel` to hide the files panel and give its space to the code.
Run it again to bring the panel back. `:PostillaNextFile` and
`:PostillaPrevFile` still work while it is hidden.

A file stays reviewed until it changes again. Use `]c` and `[c` to move between
changes inside a file. Closing the tab keeps your comments and reviewed marks;
run `:PostillaDiff` again to continue.

## Commands

| Command | Action |
| --- | --- |
| `:PostillaStart` | Start or restore a review |
| `:PostillaComment` | Comment on the current line or selected range |
| `:PostillaNext` / `:PostillaPrev` | Jump between comments |
| `:PostillaList` | List comments in quickfix |
| `:PostillaEdit R1` | Edit comment `R1` |
| `:PostillaDelete R1` | Delete comment `R1` |
| `:PostillaPreview` | Preview feedback and jump to its comments |
| `:PostillaExport` | Copy and save feedback without finishing |
| `:PostillaStatus` | Show the current review status |
| `:PostillaDone` | Copy the review and finish |
| `:PostillaDiff [revision]` | Open the diff review against `HEAD` or a revision |
| `:PostillaDiffClose` | Close the diff review |
| `:PostillaNextFile` / `:PostillaPrevFile` | Show the next or previous changed file |
| `:PostillaReviewed` | Mark the current file as reviewed and move on |
| `:PostillaPanel` | Show or hide the files panel |
| `:PostillaLayout [split\|unified]` | Switch the diff layout |
| `:PostillaAbort` | Discard the current review |

## Output

Postilla uses the revdiff annotation format:

```markdown
## lua/postilla/init.lua:42 ( )
Please simplify this branch.

## README.md:80-84 ( )
This section is too long. Keep it focused on new users.
```

The output keeps every comment connected to its file and line. This makes the
feedback clear for both people and coding agents.

Comments made in a diff review also say what kind of line they are on:

```markdown
## store.go:18 (-)
Do not remove this validation.

## store.go:24 (+)
Use errors.Is() here.
```

`(-)` is a deleted line, numbered as in the old version. `(+)` is an added or
changed line, and `( )` is an unchanged line.

## Configuration

These are the default options:

```lua
require("postilla").setup({
  context_lines = 5,
  keymap = nil,
  next_keymap = nil,
  previous_keymap = nil,
  diff_keymap = nil,
  next_file_keymap = nil,
  previous_file_keymap = nil,
  reviewed_keymap = nil,
  panel_keymap = nil,
  layout_keymap = nil,
  icons = "default",
  state_dir = nil,
  marker = {
    style = "virtual_line",
  },
  comment_window = {
    layout = "bottom",
    height = 10,
    width = 80,
  },
  diff = {
    base = "HEAD",
    layout = "split",
    panel_width = 40,
    group_files = true,
    panel_keys = {},
  },
})
```

- `context_lines`: lines saved before and after the reviewed line.
- `keymap`: shortcut for adding a line or Visual-range comment.
- `next_keymap` and `previous_keymap`: optional navigation shortcuts.
- `diff_keymap`: optional shortcut for `:PostillaDiff`.
- `next_file_keymap` and `previous_file_keymap`: optional shortcuts for moving
  between changed files.
- `reviewed_keymap`: optional shortcut for `:PostillaReviewed`.
- `panel_keymap`: optional shortcut for `:PostillaPanel`.
- `layout_keymap`: optional shortcut for `:PostillaLayout`.
- `icons`: `"default"`, `"ascii"`, or a table of symbols to replace. See
  [Icons](#icons).
- `state_dir`: custom directory for Postilla state.
- `marker.style`: use `"virtual_line"` or `"eol"`.
- `comment_window.layout`: use `"bottom"` or `"float"`.
- `comment_window.height`: height of the bottom split or float.
- `comment_window.width`: width of the float.
- `diff.base`: revision that `:PostillaDiff` compares against by default.
- `diff.layout`: layout a diff review starts with, `"split"` or `"unified"`.
- `diff.panel_width`: width of the files panel.
- `diff.group_files`: group the files panel by kind of file.
- `diff.panel_keys`: keys of the files panel. See [Panel keys](#panel-keys).

### Icons

Postilla draws a few symbols, such as `💬` for a comment and `✓` for a
reviewed file. If they do not render well in your terminal, use plain text:

```lua
require("postilla").setup({ icons = "ascii" })
```

Or replace single symbols:

```lua
require("postilla").setup({
  icons = { comment = "", reviewed = "" },
})
```

The symbols are `comment`, `stale`, `current`, `reviewed`, `expanded`,
`collapsed`, `arrow`, `separator`, and `connector`. Add `preset = "ascii"` to
the table to start from the plain-text set.

### Panel keys

Each action of the files panel takes one key, a list of keys, or `false` to
turn it off:

```lua
require("postilla").setup({
  diff = {
    panel_keys = {
      open = { "<CR>", "l" },
      reviewed = "m",
      hide_reviewed = false,
    },
  },
})
```

The actions are `open`, `reviewed`, `hide_reviewed`, `refresh`, `close`, and
`help`. The `g?` help window always shows the keys in use.

### Borders

Floating windows use your `winborder` option (Neovim 0.11 or newer). Without
it they have a rounded border.

For the original floating editor:

```lua
require("postilla").setup({
  comment_window = {
    layout = "float",
  },
})
```

## Sessions

Postilla stores unfinished reviews outside your project:

```text
stdpath("state")/postilla/projects/
```

If Neovim closes, reopen the project and run `:PostillaStart`. Your comments
and markers will be restored. Postilla relocates comments when their exact code
moves. If the reviewed code changed or became ambiguous, it marks the comment
with `⚠` and blocks export until you delete and recreate that comment.

Users upgrading from `local-review.nvim` only need to use
`eltonsst/postilla.nvim`, `require("postilla")`, and the `Postilla*` commands.
Old `.local-review` state is migrated automatically.

## Requirements

- Neovim 0.10 or newer
- Git, recommended for project-relative file paths and required for
  `:PostillaDiff`
- Clipboard support, recommended for `:PostillaDone`

Run `:checkhealth postilla` to check your setup. Full documentation is
available with `:help postilla`.

## Status

Postilla focuses on one job: reviewing agent changes inside Neovim and
returning precise feedback. The diff review exists for that job. Postilla does
not stage, commit, or merge changes.

## License

[MIT](LICENSE)
