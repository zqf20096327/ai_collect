# Andrej Karpathy Skills (Cursor & VS Code)

Turns the [Karpathy-inspired coding guidelines](https://github.com/forrestchang/andrej-karpathy-skills) into rule files you can use in **Cursor** and **VS Code**.

> **Disclaimer:** This plugin was written using the Cursor agent as part of the [Samotics AI Challenge Day](https://www.samotics.com).

## Install (recommended)

**VS Code:** Open the Extensions view (Ctrl+Shift+X / Cmd+Shift+X), search for **“Andrej Karpathy Skills”**, and install.

- [Install in VS Code (Microsoft Marketplace)](https://marketplace.visualstudio.com/items?itemName=MichielWBeijen.andrej-karpathy-skills-cursor-vscode)

**Cursor:** Cursor uses the [Open VSX Registry](https://open-vsx.org/), not the Microsoft Marketplace. Search for **“Andrej Karpathy Skills”** in the Extensions view, or install from Open VSX:

- [Install in Cursor (Open VSX)](https://open-vsx.org/extension/MichielWBeijen/andrej-karpathy-skills-cursor-vscode)

**About the “untrusted publisher” warning:** VS Code may show a warning that the publisher is not verified. This extension is new; Microsoft requires publishers to have had an extension on the marketplace for at least 6 months before they can apply for the verified badge. The warning is expected and safe to accept. Verification will be requested once eligible.

After installing, open the Command Palette (Ctrl+Shift+P / Cmd+Shift+P) and run:

- **Karpathy Rules: Add to project (.cursor/rules)** — adds the guidelines to `.cursor/rules/` with `alwaysApply: true` (recommended for Cursor).
- **Karpathy Rules: Add to .cursorrules (legacy)** — appends to `.cursorrules` in the project root.

## The four principles

1. **Think Before Coding** — Don’t assume; surface tradeoffs and ask when unclear.
2. **Simplicity First** — Minimum code, no speculative features or abstractions.
3. **Surgical Changes** — Touch only what’s needed; don’t “improve” unrelated code.
4. **Goal-Driven Execution** — Define success criteria and verify (e.g. with tests).

## A note on “just markdown”

I find it a bit wild that extensions for your editor can be little more than a markdown file of sixty-odd lines—no runtime, no dependencies—and still resonate enough to get [3,500+ stars on GitHub](https://github.com/forrestchang/andrej-karpathy-skills), like the original Claude Karpathy skills repo. The leverage is in the *instructions*, not the machinery. This extension is a small step to get that same content one click away in Cursor and VS Code.

If this repo is useful to you, don’t forget to ⭐ star it—it helps others find it.

## Manual setup (without the extension)

If you prefer not to use the extension:

- **Cursor:** Copy `rules/karpathy-guidelines.md` into your project as `.cursor/rules/karpathy-guidelines.md` (or `.mdc`); add `alwaysApply: true` in frontmatter if desired.
- **Legacy:** Copy the contents into a `.cursorrules` file in your project root.

## License

Guidelines adapted from [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) (MIT). This repo’s conversion and extension are under the same spirit; see upstream for exact terms.
