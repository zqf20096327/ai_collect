# ComfyUI-FlowLinks

**[English](README.md) | [简体中文](README.zh-CN.md)**

> *A touch of living color for a static interface.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.2.0-blue.svg)](CHANGELOG.md)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-frontend%20extension-green.svg)](https://github.com/comfyanonymous/ComfyUI)

Animated **water-pipe workflow links** and **per-type neon node glow** for ComfyUI.
Your graph stops being a static diagram: links connected to the running node
flow faster, the flow rate follows your real generation speed, finished links
ease to a stop, and failures turn red — so you can *see* data moving through
the workflow.

![FlowLinks demo](docs/demo.gif)

![FlowLinks on a standard SDXL text-to-image workflow](docs/screenshot-main.png)

## Features

- **Water-pipe link flow** — translucent pipe wall, bright water segments,
  white highlight dashes, and bubbles riding the stream.
- **Speed follows execution** — the flow rate tracks the live steps/s reported
  by the frontend (`progress` / `progress_state` events). Faster generation,
  longer and brighter water segments.
- **State-aware links** — active links run hot, finished links ease to a stop
  ("data delivered"), idle links drift slowly, and links touching a failed
  node flash red.
- **Per-type node glow** — every node type gets its own hue (golden-angle
  spread over a type hash), so same-type nodes share a color and different
  types never collide. The executing node pulses; title bars get a matching
  gradient.
- **Zero-dependency frontend extension** — pure JavaScript, no Python nodes,
  no models, no pip installs. Works with every node pack, because it hooks
  the link renderer itself.
- **Task progress woven into the flow** — the executing node's progress
  brightens its outgoing links, overall progress boosts the active chain's
  speed and glow, and an optional "Task 45% · 12 queued" badge sits next to
  the Flow button.
- **Settings panel** — ten options (flow on/off, speed, pipe width, glow,
  bubbles, idle speed, node glow, pulse, title gradient, task badge), persisted in
  `localStorage`. Panel labels follow the ComfyUI language automatically
  (English / 简体中文).

## Installation

### ComfyUI-Manager (recommended)

Search for **FlowLinks** in ComfyUI-Manager and click Install, then restart
ComfyUI once.

### Manual

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Daroumm/ComfyUI-FlowLinks.git
```

Restart ComfyUI. The extension activates automatically — no nodes to add.

### From the release zip

Download `ComfyUI-FlowLinks-v0.2.0.zip` from the Releases page, extract
it into `ComfyUI/custom_nodes/`, and restart ComfyUI.

**Uninstall:** delete the `ComfyUI-FlowLinks` folder from `custom_nodes`.

## Usage

Everything is automatic. Use the **Flow** button at the bottom-right of the
canvas to open the settings panel:

| Setting | Default | Description |
|---|---|---|
| Enable flow | on | Master switch for link animation |
| Flow speed | 1.0× | Global speed multiplier (0.2–3.0) |
| Pipe width | 7 | Pipe wall thickness (2–14) |
| Glow | on | Soft shadow glow around the pipe |
| Bubbles | on | Bubbles riding fast streams |
| Idle speed | 0.12 | Drift speed when nothing is running (0–0.5) |
| Node glow | on | Neon frame around every node |
| Pulse while running | on | Breathing pulse on the executing node |
| Title gradient | on | Matching gradient on node title bars |
| Task badge | on | "Task X% · N queued" badge next to the Flow button |

![Settings panel](docs/screenshot-panel.png)

## How it works

FlowLinks is a single frontend extension (`web/flow_links.js`):

1. It wraps `LitegraphLinkAdapter.renderLinkDirect` to record each link's
   endpoints and force the frontend's built-in `flow` flag on.
2. It replaces `CanvasPathRenderer.drawFlowAnimation` with a water-pipe
   renderer (pipe wall + dashed water segments + highlight + bubbles),
   reusing the renderer's own path and color resolution.
3. Execution state comes from the standard frontend events
   (`execution_start`, `executing`, `progress`, `progress_state`,
   `execution_success`, `execution_error`, `execution_interrupted`).
   Steps/s is derived from progress deltas with EMA smoothing.
4. Node glow is drawn on a transparent overlay canvas stacked above the
   graph canvas, so nodes with DOM widgets (Load Image, text encoders, …)
   get frames too. If the overlay is unavailable it falls back to wrapping
   `LGraphCanvas.drawNode`.
5. A `requestAnimationFrame` loop (~30 fps, paused when the tab is hidden)
   drives the animation and re-reads `app.canvas` every frame, so switching
   workflow tabs never breaks rendering.

Because the takeover happens at the link-renderer level, **all** node types
are covered — core nodes and every custom pack (GGUF loaders, pose tools,
etc.). The only links without flow are Set/Get wireless connections (no
visible link) and disabled links (skipped on purpose).

## Compatibility

- ComfyUI frontend ≥ 1.55 (developed and tested on 1.55.18 / ComfyUI 0.45.x).
- macOS, Windows, and Linux — the extension is platform-independent
  JavaScript running in the browser. (Verified on macOS; Windows/Linux use
  the identical frontend but have not been tested on real hardware yet —
  reports welcome.)
- Very large graphs (100+ nodes): if you notice frame drops, turn off
  **Glow** or **Node glow** in the panel.

## Known limitations

- Nodes inside subgraphs do not get glow frames yet.
- The Vue-based node rendering mode has not been tested separately; links
  still render on canvas there, so flow should work, but reports are welcome.
- FlowLinks takes over link rendering. A future frontend major version may
  require an update; worst case the flow simply stops showing — your graph
  is never modified.

## FAQ

**Does it change my workflows or outputs?**
No. FlowLinks only changes how links and node frames are drawn. It never
touches graph data, prompts, or generated images.

**Does it slow down generation?**
No. Rendering runs in the browser at ~30 fps and is independent of the
backend. On the test machine the canvas held ~60 fps with the full effect on.

**Why is the flow slow when nothing is running?**
Idle links drift at the *Idle speed* setting (default 0.12). Raise it in the
panel if you want more motion at rest.

**A link isn't flowing. Why?**
Disabled links are skipped on purpose, and Set/Get wireless connections have
no visible link to animate.

## Contributing

Issues and pull requests are welcome. For bug reports, please include your
ComfyUI version, frontend version, browser, and a screenshot or screen
recording if possible.

## License

[MIT](LICENSE) © darou
