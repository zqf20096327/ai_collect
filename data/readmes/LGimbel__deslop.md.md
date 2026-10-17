# deslop.md



## TL;DR

```bash
curl -sL https://raw.githubusercontent.com/LGimbel/deslop.md/main/markdown_block_fixer.py | python3 - yourfile.txt
```

---

A CLI tool that fixes broken ASCII box-drawing diagrams — the kind LLMs love to generate but can never quite get right.

When ChatGPT, Claude, or any other LLM spits out an architecture diagram with misaligned borders, overlapping pipes, and boxes that don't fit their content, `deslop.md` can clean it up automatically.

## The Problem

LLMs generate ASCII diagrams like this all the time:

```
┌──────────┐
│ some really long text│
│ short    │
└──────────┘
```

Borders don't match content width. Nested boxes are even worse — pipes misalign, padding is inconsistent, and the whole thing looks like it was drawn by hand in the dark.

## The Fix

deslop.md

**From a file:**

```bash
python markdown_block_fixer.py diagram.txt
```

**From stdin (pipe it):**

```bash
cat diagram.txt | python markdown_block_fixer.py
```

## What It Fixes

- **Box expansion** — widens borders (`┌─┐ └─┘`) when content overflows
- **Content padding** — pads content rows so pipes (`│`) line up with corners
- **Nested boxes** — propagates width changes through parent/child box hierarchies
- **Vertical alignment** — aligns `│` and `▼` characters with `┬` connectors above them

## Example

Before:

```
┌──────────┐
│  Server  │
│ ┌──────┐ │
│ │ module_name│ │
│ └──────┘ │
└──────────┘
```

After:

```
┌─────────────────┐
│  Server         │
│ ┌─────────────┐ │
│ │ module_name │ │
│ └─────────────┘ │
└─────────────────┘
```

## Supported Box Characters

```
┌ ┐ └ ┘   corners
│         vertical border
─         horizontal border
├ ┤       horizontal dividers
┬ ┴       vertical connectors
▼         arrows (aligned vertically)
```
