# draw-json-architecture-skill

[![Updated](https://img.shields.io/badge/updated-Jun%2001%2C%202026%2011%3A08%20AM%20PKT-white?style=flat&labelColor=555)](https://github.com/shanraisshan/draw-json-architecture-skill) [![Version](https://img.shields.io/badge/version-1.0.0-white?style=flat&labelColor=555)](https://github.com/shanraisshan/draw-json-architecture-skill/releases) [![Stars](https://img.shields.io/github/stars/shanraisshan/draw-json-architecture-skill?style=flat&label=%E2%98%85&labelColor=555&color=white)](https://github.com/shanraisshan/draw-json-architecture-skill)

A skill that explains any code architecture as an interactive viewer — Graph + JSON + HTML, 100% driven by JSON — and saves the self-contained `.html` to your repo's root `architecture/` folder.

## Installation

<p>
  <a href="install/README-mac.md"><img src="!/pills/pill-mac.svg" alt="Mac" height="36"></a>&nbsp;
  <a href="install/README-linux.md"><img src="!/pills/pill-linux.svg" alt="Linux" height="36"></a>&nbsp;
  <a href="install/README-windows.md"><img src="!/pills/pill-windows.svg" alt="Windows" height="36"></a>
</p>

![How to Use](!/pills/pill-how-to-use.svg)

- **Define a flow** — name the path you want explained, e.g. `onboarding to home` or `home to order placement`. The skill walks that flow stop by stop.
- **Define the lenses** — tell it which lenses each stop is viewed through, e.g. `ui`, `api`, `database` (also `auth`, `cache`, `queue`, `llm`, …), and pick a color for each so the diagram paints every stop in its lens color.
- **Get the viewer** — the skill generates a self-contained `<flow>.html` Architecture Viewer (Graph + JSON + HTML panels) driven entirely by JSON, then verifies links, claims, and the generated artifacts before delivery.

## <a><img src="!/mascot/claude-static.svg" width="30" height="30"></a> Claude
```
/draw-json-architecture <flow>
```

## <a><img src="!/mascot/codex-static.svg" width="40" height="40"></a> Codex
```
$draw-json-architecture <flow>
```

### Wireframe

<img src="!/architecture/wireframe-draw-json-architecture.png" alt="Architecture Viewer wireframe" width="50%">

### Architecture [`home-to-order.html`](architecture/home-to-order/home-to-order.html)

Architecture of sample-app flow from home to order placement screen drawn using ```draw-json-architecture``` skill.

<a href="architecture/home-to-order/home-to-order.html"><img src="!/architecture/draw-json-architecture-sample-app.png" alt="Example architecture — home to order" width="70%"></a>

## Changelog
|Date|Changes|Version|
|-|-|-|
|Jun 1, 2026|Added `draw-json-architecture`|v1.0.0|


## Other Repos

<table>
<tr>
<td align="center" width="140">
  <a href="https://github.com/shanraisshan/claude-code-best-practice"><img src="!/mascot/claude-jumping.svg" alt="Claude Code Best Practice" width="64" height="64"></a><br>
  <a href="https://github.com/shanraisshan/claude-code-best-practice"><strong>Claude Code<br>Best Practice</strong></a>
</td>
<td align="center" width="140">
  <a href="https://github.com/shanraisshan/codex-cli-best-practice"><img src="!/mascot/codex-jumping.svg" alt="Codex CLI Best Practice" width="64" height="64"></a><br>
  <a href="https://github.com/shanraisshan/codex-cli-best-practice"><strong>Codex CLI<br>Best Practice</strong></a>
</td>
<td align="center" width="140">
  <a href="https://github.com/shanraisshan/gemini-cli-best-practice"><img src="!/mascot/gemini-jumping.svg" alt="Gemini CLI Best Practice" width="64" height="64"></a><br>
  <a href="https://github.com/shanraisshan/gemini-cli-best-practice"><strong>Gemini CLI<br>Best Practice</strong></a>
</td>
<td align="center" width="140">
  <a href="https://github.com/shanraisshan/claude-code-hooks"><img src="!/mascot/claude-speaking.svg" alt="Claude Code Hooks" width="64" height="64"></a><br>
  <a href="https://github.com/shanraisshan/claude-code-hooks"><strong>Claude Code<br>Hooks</strong></a>
</td>
<td align="center" width="140">
  <a href="https://github.com/shanraisshan/codex-cli-hooks"><img src="!/mascot/codex-speaking.svg" alt="Codex CLI Hooks" width="64" height="64"></a><br>
  <a href="https://github.com/shanraisshan/codex-cli-hooks"><strong>Codex CLI<br>Hooks</strong></a>
</td>
<td align="center" width="140">
  <a href="https://github.com/shanraisshan/gemini-cli-hooks"><img src="!/mascot/gemini-speaking.svg" alt="Gemini CLI Hooks" width="64" height="64"></a><br>
  <a href="https://github.com/shanraisshan/gemini-cli-hooks"><strong>Gemini CLI<br>Hooks</strong></a>
</td>
</tr>
</table>


