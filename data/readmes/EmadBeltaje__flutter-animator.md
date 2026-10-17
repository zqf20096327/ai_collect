# flutter-animator

An Agent Skill that teaches a coding agent which Flutter animation API to reach for, and how to implement it without leaks or silent no-ops.

**Demo:** https://emadbeltaje.github.io/flutter-animator-example/

## Preview

### Real world

Production-style patterns (loading, toggles, lists, navigation, and similar).

![Real world](preview-images/real-world.gif)

| Implicit | Built-in transitions | Hero |
| --- | --- | --- |
| ![Implicit](preview-images/implicit.gif) | ![Built-in transitions](preview-images/built-in.gif) | ![Hero](preview-images/hero.gif) |

| List | Grid | AnimatedSwitcher |
| --- | --- | --- |
| ![List](preview-images/list.gif) | ![Grid](preview-images/grid.gif) | ![AnimatedSwitcher](preview-images/animated-switcher.gif) |

| AnimatedIcon | Page transitions |
| --- | --- |
| ![AnimatedIcon](preview-images/animated-icon.gif) | ![Page transitions](preview-images/page-transation.gif) |

## Installation

```bash
npx skills add EmadBeltaje/flutter-animator
```

**Claude Code** (plugin marketplace — see `plugin.json` and `.claude-plugin/marketplace.json` in this repo):

```text
/plugin marketplace add EmadBeltaje/flutter-animator
/plugin install flutter-animator@flutter-animator
```

**Other editors** (Cursor, Windsurf, Copilot, and similar): copy `skills/flutter-animator/` into that tool’s skills folder (for example `.cursor/skills/flutter-animator/`). There is no separate marketplace publish for Cursor; manual copy is enough.

Or copy into `.claude/skills/`, `.agents/skills/`, or `.github/skills/` as needed.

## Use cases

Use this skill whenever you want motion in a Flutter UI and would rather the agent pick the right API than invent a controller from scratch.

| You say | The skill should | Example |
| --- | --- | --- |
| “Make this card expand smoothly” | Implicit `AnimatedContainer` / `AnimatedSize` | Expandable FAQ row, selected product card |
| “Fly this photo into the details screen” | `Hero` with a unique tag | Gallery thumbnail → full-screen image |
| “Animate rows being deleted” | `AnimatedList` / `AnimatedGrid` | Dismissible inbox, cart items |
| “Swap the spinner for the content” | `AnimatedSwitcher` (with keys) | Loading → data, icon A → icon B |
| “Cross-fade success and error icons” | `AnimatedCrossFade` | Form validation, empty vs filled bookmark |
| “Morph menu into close” | `AnimatedIcon` | App bar drawer button |
| “Slide this page up” | `PageRouteBuilder` | Bottom sheet-style route, onboarding |
| “Snap back after I drag it” | Physics / `SpringSimulation` | Draggable card, pull-to-snap |
| “Fade, then slide, then scale” | Staggered animations | First-run hero, list item entrance |
| “Make this smoother” / “add motion” | Decision tree, SDK widgets only | Any widget the user did not name an API for |

In chat, install the skill then just describe the effect. You do not need to name `AnimationController` or pick a widget — that is the point of the tree.

## Author

[EmadBeltaje](https://github.com/EmadBeltaje)
