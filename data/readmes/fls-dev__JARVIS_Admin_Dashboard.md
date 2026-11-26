<p align="right"><b>English</b> · <a href="README.ru.md">Русский</a></p>

<p align="center">
  <img src="docs/assets/banner.jpg" alt="JARVIS Admin Dashboard — Aurora and Orbital" width="100%">
</p>

<h1 align="center">JARVIS Admin Dashboard</h1>
<p align="center"><b>Two futuristic dashboards. Two worlds. No build step.</b><br>
Open-source admin templates for an AI agent that runs your infrastructure — made for design feedback and real customization.</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-A78BFA?style=flat-square"></a>
  <img alt="HTML5" src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&amp;logo=html5&amp;logoColor=white">
  <img alt="Vanilla JavaScript" src="https://img.shields.io/badge/Vanilla_JS-F7DF1E?style=flat-square&amp;logo=javascript&amp;logoColor=black">
  <img alt="No build step" src="https://img.shields.io/badge/build-none-8BE9FF?style=flat-square">
  <img alt="three.js r149" src="https://img.shields.io/badge/three.js-r149-white?style=flat-square&amp;logo=threedotjs&amp;logoColor=white">
</p>

<p align="center">
  <a href="https://fls-dev.github.io/JARVIS_Admin_Dashboard/">Live demo</a> ·
  <a href="#templates">Templates</a> ·
  <a href="#quick-start">Quick start</a> ·
  <a href="https://github.com/fls-dev/JARVIS_Admin_Dashboard/issues/new/choose">Leave feedback</a> ·
  <a href="https://github.com/fls-dev/JARVIS_Admin_Dashboard/discussions">Discussions</a>
</p>

> **Demo status:** the live demo URL works after GitHub Pages is enabled. In **Settings → Pages → Build and deployment → Source**, choose **GitHub Actions**, then run the **Deploy demo to GitHub Pages** workflow (or push to `main`).

## Templates

### JARVIS Aurora

A glass sphere orchestrates a living canvas of task nodes with flowing edges, all set on a soft aurora glow. Navigation feels like an instrument, not a sidebar.

<a href="templates/aurora/index.html"><img src="docs/assets/aurora-cover.jpg" alt="JARVIS Aurora — desktop and mobile overview" width="100%"></a>

[Open source](templates/aurora/) · [Live demo](https://fls-dev.github.io/JARVIS_Admin_Dashboard/templates/aurora/index.html) · [Template docs](templates/aurora/README.md)

- **11 HTML pages**: hub + UI kit + 9 app screens, including a full **Operations** room (queue, throughput, workers, errors). Fine-tuning has both an empty state and a live run (`#runs`).
- Orbit-wheel menu on desktop; bottom dock and radial menu on tablet and phone. `1–9` navigation and a `⌘K` / `Ctrl K` palette.
- Inspector slides in on desktop and becomes a bottom sheet on mobile. Living canvases turn into vertical flows on phones.
- Canvas 2D glass sphere, aurora and midnight themes, reduced-motion setting with an in-app override.
- Plain HTML, CSS and JS, no dependencies. Fonts load from Google Fonts (fallbacks work offline).

<details>
<summary><b>All Aurora screens · desktop</b></summary>

<table>
<tr>
<td align="center" width="33%"><a href="docs/screenshots/aurora/00-hub-desktop.jpg"><img src="docs/screenshots/aurora/00-hub-desktop.jpg" alt="Hub (desktop)" width="280"></a><br><sub><b>Hub</b></sub></td>
<td align="center" width="33%"><a href="docs/screenshots/aurora/01-overview-desktop.jpg"><img src="docs/screenshots/aurora/01-overview-desktop.jpg" alt="Overview (desktop)" width="280"></a><br><sub><b>Overview</b></sub></td>
<td align="center" width="33%"><a href="docs/screenshots/aurora/02-tasks-desktop.jpg"><img src="docs/screenshots/aurora/02-tasks-desktop.jpg" alt="Tasks (desktop)" width="280"></a><br><sub><b>Tasks</b></sub></td>
</tr>
<tr>
<td align="center" width="33%"><a href="docs/screenshots/aurora/13-operations-desktop.jpg"><img src="docs/screenshots/aurora/13-operations-desktop.jpg" alt="Operations (desktop)" width="280"></a><br><sub><b>Operations</b></sub></td>
<td align="center" width="33%"><a href="docs/screenshots/aurora/03-local-chat-desktop.jpg"><img src="docs/screenshots/aurora/03-local-chat-desktop.jpg" alt="Local chat (desktop)" width="280"></a><br><sub><b>Local chat</b></sub></td>
<td align="center" width="33%"><a href="docs/screenshots/aurora/04-fine-tuning-desktop.jpg"><img src="docs/screenshots/aurora/04-fine-tuning-desktop.jpg" alt="Fine-tuning (desktop)" width="280"></a><br><sub><b>Fine-tuning</b></sub></td>
</tr>
<tr>
<td align="center" width="33%"><a href="docs/screenshots/aurora/05-fine-tuning-runs-desktop.jpg"><img src="docs/screenshots/aurora/05-fine-tuning-runs-desktop.jpg" alt="Fine-tuning · runs (desktop)" width="280"></a><br><sub><b>Fine-tuning · runs</b></sub></td>
<td align="center" width="33%"><a href="docs/screenshots/aurora/06-scheduled-desktop.jpg"><img src="docs/screenshots/aurora/06-scheduled-desktop.jpg" alt="Scheduled work (desktop)" width="280"></a><br><sub><b>Scheduled work</b></sub></td>
<td align="center" width="33%"><a href="docs/screenshots/aurora/07-memory-desktop.jpg"><img src="docs/screenshots/aurora/07-memory-desktop.jpg" alt="Memory (desktop)" width="280"></a><br><sub><b>Memory</b></sub></td>
</tr>
<tr>
<td align="center" width="33%"><a href="docs/screenshots/aurora/08-integrations-desktop.jpg"><img src="docs/screenshots/aurora/08-integrations-desktop.jpg" alt="Integrations (desktop)" width="280"></a><br><sub><b>Integrations</b></sub></td>
<td align="center" width="33%"><a href="docs/screenshots/aurora/09-audit-desktop.jpg"><img src="docs/screenshots/aurora/09-audit-desktop.jpg" alt="Audit trail (desktop)" width="280"></a><br><sub><b>Audit trail</b></sub></td>
<td align="center" width="33%"><a href="docs/screenshots/aurora/10-ui-kit-desktop.jpg"><img src="docs/screenshots/aurora/10-ui-kit-desktop.jpg" alt="UI kit (desktop)" width="280"></a><br><sub><b>UI kit</b></sub></td>
</tr>
<tr>
<td align="center" width="33%"><a href="docs/screenshots/aurora/12-command-palette-desktop.jpg"><img src="docs/screenshots/aurora/12-command-palette-desktop.jpg" alt="⌘K palette (desktop)" width="280"></a><br><sub><b>⌘K palette</b></sub></td>
</tr>
</table>

</details>

<details>
<summary><b>Aurora on mobile · 390 px</b></summary>

<table>
<tr>
<td align="center" width="25%"><a href="docs/screenshots/aurora/01-overview-mobile.jpg"><img src="docs/screenshots/aurora/01-overview-mobile.jpg" alt="Overview (mobile)" width="180"></a><br><sub><b>Overview</b></sub></td>
<td align="center" width="25%"><a href="docs/screenshots/aurora/02-tasks-mobile.jpg"><img src="docs/screenshots/aurora/02-tasks-mobile.jpg" alt="Tasks (mobile)" width="180"></a><br><sub><b>Tasks</b></sub></td>
<td align="center" width="25%"><a href="docs/screenshots/aurora/13-operations-mobile.jpg"><img src="docs/screenshots/aurora/13-operations-mobile.jpg" alt="Operations (mobile)" width="180"></a><br><sub><b>Operations</b></sub></td>
<td align="center" width="25%"><a href="docs/screenshots/aurora/03-local-chat-mobile.jpg"><img src="docs/screenshots/aurora/03-local-chat-mobile.jpg" alt="Local chat (mobile)" width="180"></a><br><sub><b>Local chat</b></sub></td>
</tr>
<tr>
<td align="center" width="25%"><a href="docs/screenshots/aurora/04-fine-tuning-mobile.jpg"><img src="docs/screenshots/aurora/04-fine-tuning-mobile.jpg" alt="Fine-tuning (mobile)" width="180"></a><br><sub><b>Fine-tuning</b></sub></td>
<td align="center" width="25%"><a href="docs/screenshots/aurora/05-fine-tuning-runs-mobile.jpg"><img src="docs/screenshots/aurora/05-fine-tuning-runs-mobile.jpg" alt="Fine-tuning · runs (mobile)" width="180"></a><br><sub><b>Fine-tuning · runs</b></sub></td>
<td align="center" width="25%"><a href="docs/screenshots/aurora/06-scheduled-mobile.jpg"><img src="docs/screenshots/aurora/06-scheduled-mobile.jpg" alt="Scheduled work (mobile)" width="180"></a><br><sub><b>Scheduled work</b></sub></td>
<td align="center" width="25%"><a href="docs/screenshots/aurora/07-memory-mobile.jpg"><img src="docs/screenshots/aurora/07-memory-mobile.jpg" alt="Memory (mobile)" width="180"></a><br><sub><b>Memory</b></sub></td>
</tr>
<tr>
<td align="center" width="25%"><a href="docs/screenshots/aurora/08-integrations-mobile.jpg"><img src="docs/screenshots/aurora/08-integrations-mobile.jpg" alt="Integrations (mobile)" width="180"></a><br><sub><b>Integrations</b></sub></td>
<td align="center" width="25%"><a href="docs/screenshots/aurora/09-audit-mobile.jpg"><img src="docs/screenshots/aurora/09-audit-mobile.jpg" alt="Audit trail (mobile)" width="180"></a><br><sub><b>Audit trail</b></sub></td>
<td align="center" width="25%"><a href="docs/screenshots/aurora/11-radial-menu-open-mobile.jpg"><img src="docs/screenshots/aurora/11-radial-menu-open-mobile.jpg" alt="Radial menu (mobile)" width="180"></a><br><sub><b>Radial menu</b></sub></td>
<td align="center" width="25%"><a href="docs/screenshots/aurora/12-command-palette-mobile.jpg"><img src="docs/screenshots/aurora/12-command-palette-mobile.jpg" alt="⌘K palette (mobile)" width="180"></a><br><sub><b>⌘K palette</b></sub></td>
</tr>
</table>

</details>

### JARVIS Orbital

Nine rooms orbit one living 3D planet. Each page is a set of glass windows in a twilight sky, and every jump between rooms is a camera flight.

<a href="templates/orbital/index.html"><img src="docs/assets/orbital-cover.jpg" alt="JARVIS Orbital — desktop and mobile overview" width="100%"></a>

[Open source](templates/orbital/) · [Live demo](https://fls-dev.github.io/JARVIS_Admin_Dashboard/templates/orbital/index.html) · [Template docs](templates/orbital/README.md)

- **11 HTML pages**: hub + UI kit + 9 rooms, including a full **Operations** room. `_blank.html` is an extra starter for your own room.
- A three.js planet with traffic arcs, orbital rings and integration satellites. Each room gives it a different pose.
- Orbit pill unfolds into nine portals (`G`). Hover previews a room; click flies there. On phones the dial is a 3 × 3 sheet.
- `1–9`, `[` / `]`, arrows and `⌘K` / `Ctrl K`. Drawer, toasts, SVG charts and live demo counters.
- three.js and fonts are bundled — works offline. Static CSS planet when WebGL is unavailable (`?nogl`), still scene and no flights under reduced motion.

<details>
<summary><b>All Orbital screens · desktop</b></summary>

<table>
<tr>
<td align="center" width="33%"><a href="docs/screenshots/orbital/00-hub-desktop.jpg"><img src="docs/screenshots/orbital/00-hub-desktop.jpg" alt="Hub (desktop)" width="280"></a><br><sub><b>Hub</b></sub></td>
<td align="center" width="33%"><a href="docs/screenshots/orbital/01-overview-desktop.jpg"><img src="docs/screenshots/orbital/01-overview-desktop.jpg" alt="Overview (desktop)" width="280"></a><br><sub><b>Overview</b></sub></td>
<td align="center" width="33%"><a href="docs/screenshots/orbital/02-tasks-desktop.jpg"><img src="docs/screenshots/orbital/02-tasks-desktop.jpg" alt="Tasks (desktop)" width="280"></a><br><sub><b>Tasks</b></sub></td>
</tr>
<tr>
<td align="center" width="33%"><a href="docs/screenshots/orbital/03-operations-desktop.jpg"><img src="docs/screenshots/orbital/03-operations-desktop.jpg" alt="Operations (desktop)" width="280"></a><br><sub><b>Operations</b></sub></td>
<td align="center" width="33%"><a href="docs/screenshots/orbital/04-local-chat-desktop.jpg"><img src="docs/screenshots/orbital/04-local-chat-desktop.jpg" alt="Local chat (desktop)" width="280"></a><br><sub><b>Local chat</b></sub></td>
<td align="center" width="33%"><a href="docs/screenshots/orbital/05-fine-tuning-desktop.jpg"><img src="docs/screenshots/orbital/05-fine-tuning-desktop.jpg" alt="Fine-tuning (desktop)" width="280"></a><br><sub><b>Fine-tuning</b></sub></td>
</tr>
<tr>
<td align="center" width="33%"><a href="docs/screenshots/orbital/06-scheduled-desktop.jpg"><img src="docs/screenshots/orbital/06-scheduled-desktop.jpg" alt="Scheduled work (desktop)" width="280"></a><br><sub><b>Scheduled work</b></sub></td>
<td align="center" width="33%"><a href="docs/screenshots/orbital/07-memory-desktop.jpg"><img src="docs/screenshots/orbital/07-memory-desktop.jpg" alt="Memory (desktop)" width="280"></a><br><sub><b>Memory</b></sub></td>
<td align="center" width="33%"><a href="docs/screenshots/orbital/08-integrations-desktop.jpg"><img src="docs/screenshots/orbital/08-integrations-desktop.jpg" alt="Integrations (desktop)" width="280"></a><br><sub><b>Integrations</b></sub></td>
</tr>
<tr>
<td align="center" width="33%"><a href="docs/screenshots/orbital/09-audit-desktop.jpg"><img src="docs/screenshots/orbital/09-audit-desktop.jpg" alt="Audit trail (desktop)" width="280"></a><br><sub><b>Audit trail</b></sub></td>
<td align="center" width="33%"><a href="docs/screenshots/orbital/10-ui-kit-desktop.jpg"><img src="docs/screenshots/orbital/10-ui-kit-desktop.jpg" alt="UI kit (desktop)" width="280"></a><br><sub><b>UI kit</b></sub></td>
<td align="center" width="33%"><a href="docs/screenshots/orbital/11-orbit-dial-open-desktop.jpg"><img src="docs/screenshots/orbital/11-orbit-dial-open-desktop.jpg" alt="Orbit dial (desktop)" width="280"></a><br><sub><b>Orbit dial</b></sub></td>
</tr>
<tr>
<td align="center" width="33%"><a href="docs/screenshots/orbital/12-command-palette-desktop.jpg"><img src="docs/screenshots/orbital/12-command-palette-desktop.jpg" alt="⌘K palette (desktop)" width="280"></a><br><sub><b>⌘K palette</b></sub></td>
</tr>
</table>

</details>

<details>
<summary><b>Orbital on mobile · 390 px</b></summary>

<table>
<tr>
<td align="center" width="25%"><a href="docs/screenshots/orbital/01-overview-mobile.jpg"><img src="docs/screenshots/orbital/01-overview-mobile.jpg" alt="Overview (mobile)" width="180"></a><br><sub><b>Overview</b></sub></td>
<td align="center" width="25%"><a href="docs/screenshots/orbital/02-tasks-mobile.jpg"><img src="docs/screenshots/orbital/02-tasks-mobile.jpg" alt="Tasks (mobile)" width="180"></a><br><sub><b>Tasks</b></sub></td>
<td align="center" width="25%"><a href="docs/screenshots/orbital/03-operations-mobile.jpg"><img src="docs/screenshots/orbital/03-operations-mobile.jpg" alt="Operations (mobile)" width="180"></a><br><sub><b>Operations</b></sub></td>
<td align="center" width="25%"><a href="docs/screenshots/orbital/04-local-chat-mobile.jpg"><img src="docs/screenshots/orbital/04-local-chat-mobile.jpg" alt="Local chat (mobile)" width="180"></a><br><sub><b>Local chat</b></sub></td>
</tr>
<tr>
<td align="center" width="25%"><a href="docs/screenshots/orbital/05-fine-tuning-mobile.jpg"><img src="docs/screenshots/orbital/05-fine-tuning-mobile.jpg" alt="Fine-tuning (mobile)" width="180"></a><br><sub><b>Fine-tuning</b></sub></td>
<td align="center" width="25%"><a href="docs/screenshots/orbital/06-scheduled-mobile.jpg"><img src="docs/screenshots/orbital/06-scheduled-mobile.jpg" alt="Scheduled work (mobile)" width="180"></a><br><sub><b>Scheduled work</b></sub></td>
<td align="center" width="25%"><a href="docs/screenshots/orbital/07-memory-mobile.jpg"><img src="docs/screenshots/orbital/07-memory-mobile.jpg" alt="Memory (mobile)" width="180"></a><br><sub><b>Memory</b></sub></td>
<td align="center" width="25%"><a href="docs/screenshots/orbital/08-integrations-mobile.jpg"><img src="docs/screenshots/orbital/08-integrations-mobile.jpg" alt="Integrations (mobile)" width="180"></a><br><sub><b>Integrations</b></sub></td>
</tr>
<tr>
<td align="center" width="25%"><a href="docs/screenshots/orbital/09-audit-mobile.jpg"><img src="docs/screenshots/orbital/09-audit-mobile.jpg" alt="Audit trail (mobile)" width="180"></a><br><sub><b>Audit trail</b></sub></td>
<td align="center" width="25%"><a href="docs/screenshots/orbital/10-ui-kit-mobile.jpg"><img src="docs/screenshots/orbital/10-ui-kit-mobile.jpg" alt="UI kit (mobile)" width="180"></a><br><sub><b>UI kit</b></sub></td>
<td align="center" width="25%"><a href="docs/screenshots/orbital/11-orbit-dial-open-mobile.jpg"><img src="docs/screenshots/orbital/11-orbit-dial-open-mobile.jpg" alt="Orbit dial (mobile)" width="180"></a><br><sub><b>Orbit dial</b></sub></td>
<td align="center" width="25%"><a href="docs/screenshots/orbital/12-command-palette-mobile.jpg"><img src="docs/screenshots/orbital/12-command-palette-mobile.jpg" alt="⌘K palette (mobile)" width="180"></a><br><sub><b>⌘K palette</b></sub></td>
</tr>
</table>

</details>

### At a glance

| | Aurora | Orbital |
| --- | --- | --- |
| Visual world | Purple/pink aurora, living canvas | Twilight sky, coral horizon, spatial windows |
| Core | Glass sphere · Canvas 2D | Planet · three.js r149 / WebGL |
| Desktop navigation | Orbit wheel | Orbit pill → portal dial |
| Mobile navigation | Dock + radial menu | 3 × 3 portal sheet |
| Detail view | Inspector → bottom sheet | Drawer |
| Themes | Aurora / Midnight | Twilight |
| HTML pages (excluding starter) | 11 | 11 |
| Operations | Full room | Full room |
| Fonts | Inter Tight, Instrument Serif, Geist Mono · Google Fonts | Sora, IBM Plex Mono · bundled |
| Build / framework | None / none | None / none |

## Quick start

Clone the repo, then open **`index.html`** to choose a template. Or open `templates/aurora/index.html` / `templates/orbital/index.html` directly — both support `file://`.

```bash
git clone https://github.com/fls-dev/JARVIS_Admin_Dashboard.git
cd JARVIS_Admin_Dashboard

# Optional local server (pick one)
python3 -m http.server 8080
# or: npx serve .
```

With Python, visit **http://localhost:8080/**. `npx serve` prints its own local URL. There is no install, bundle, build or environment file to configure.

> These are **static UI templates, not a full application**. Tasks, hosts, costs, model responses and chat messages are fictional demo data. No back end, authentication or real integrations are included. Renderers use trusted demo strings; sanitize external input when connecting an API — see [Security](SECURITY.md).

## Project structure

```text
.
├── index.html                 landing / template chooser
├── templates/
│   ├── aurora/                index.html + 9 pages
│   │   └── assets/            css/, js/, img/thumbs/
│   └── orbital/               index.html + 10 pages + _blank.html
│       └── assets/            css/, js/, fonts/, img/, js/vendor/three.min.js
├── docs/
│   ├── assets/                banner and covers
│   ├── screenshots/           separate desktop and mobile screens
│   │   ├── aurora/
│   │   └── orbital/
│   ├── listings/              short publication descriptions (EN / RU)
│   └── social-preview.png     1280×640, for GitHub Social preview
├── .github/                   issue forms, PR template, Pages workflow
├── CONTRIBUTING.md
├── SECURITY.md
├── CHANGELOG.md
└── LICENSE
```

## Customization

| Change | File(s) |
| --- | --- |
| Colours, glass, type, radii, spacing, motion | `templates/<name>/assets/css/tokens.css` |
| Demo content, nav routes, tasks, integrations | `templates/<name>/assets/js/data.js` |
| Page logic and additional demo strings | `templates/<name>/assets/js/pages/<page>.js` |
| Shared UI components | `assets/css/components.css`, shared JS files |
| Aurora page layout | `templates/aurora/assets/css/pages/<page>.css` |
| Orbital page layout | `templates/orbital/assets/css/pages.css` |
| Orbital planet poses and flights | `templates/orbital/assets/js/scene.js` |

Scripts are classic (non-module) so pages keep working from disk. Keep links relative so the templates work from any folder or sub-path. For APIs, adding a page and the component reference, see the [Aurora docs](templates/aurora/README.md) and [Orbital docs](templates/orbital/README.md).

## Browser support & accessibility

Designed for current Chrome, Edge, Firefox and Safari, including mobile. The styles use CSS custom properties, `backdrop-filter` and `color-mix()`; older browsers are not a target. Smoke-tested in Chromium with software rendering. Real-device Safari and hardware-GPU checks are still welcome.

- Responsive layouts from **390 to 1920 px**; touch layouts adapt the navigation, inspector and canvases instead of just shrinking them.
- Both templates honour **`prefers-reduced-motion`** and expose an in-app motion toggle through the command palette. Motion stops or becomes a still scene.
- Keyboard shortcuts and visible focus styles; touch layouts use larger targets. Orbital has a skip link, focus traps in its drawer/palette and live regions.
- Colour is paired with text for statuses. **Not yet audited for WCAG conformance** — screen-reader and contrast feedback are very welcome.
- Orbital falls back to a CSS planet without WebGL. Aurora's Google Fonts need a network connection; system fallbacks are present.

## Roadmap

- [ ] Real-device Safari and hardware-GPU testing
- [ ] Accessibility audit: keyboard, screen readers, contrast and touch targets
- [ ] Automated visual regression tests
- [ ] Optional API integration examples with safe rendering

## Feedback welcome

This is a design-first project, published to see what people think. Which direction feels more useful? Is the navigation clear? What would you change?

- [Share design feedback](https://github.com/fls-dev/JARVIS_Admin_Dashboard/issues/new?template=design_feedback.yml)
- [Report a bug](https://github.com/fls-dev/JARVIS_Admin_Dashboard/issues/new?template=bug_report.yml)
- [Suggest a feature](https://github.com/fls-dev/JARVIS_Admin_Dashboard/issues/new?template=feature_request.yml)
- [Join the discussion](https://github.com/fls-dev/JARVIS_Admin_Dashboard/discussions) (once Discussions is enabled)

Contributions are welcome — please read [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md).

## Credits

Designed and built by **[fls-dev](https://github.com/fls-dev)**.

| Template | Components |
| --- | --- |
| Aurora | Inter Tight, Instrument Serif, Geist Mono ([Google Fonts](https://fonts.google.com/), SIL OFL 1.1) |
| Orbital | [three.js r149](https://github.com/mrdoob/three.js/tree/r149) (MIT), Sora and IBM Plex Mono (SIL OFL 1.1) |

Third-party components keep their own licenses. See [Aurora credits](templates/aurora/CREDITS.md) and [Orbital credits](templates/orbital/CREDITS.md).

## License

[MIT](LICENSE) © 2026 **fls-dev (Pavel Misko)**. Free to use, modify and distribute, including commercial projects. Keep the copyright and license notice.
