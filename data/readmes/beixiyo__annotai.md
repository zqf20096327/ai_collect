# annotai

> **annotai** = annot**ate** + **AI** — annotate page elements into source context your AI can use

<p align="center">English | <a href="README.zh-CN.md">简体中文</a></p>

<p align="center">
  <a href="https://www.npmjs.com/package/annotai"><img src="https://img.shields.io/npm/v/annotai?style=flat&amp;logo=npm&amp;logoColor=white&amp;color=CB3837&amp;label=npm" alt="npm version"></a>
  <a href="https://www.npmjs.com/package/annotai"><img src="https://img.shields.io/npm/dt/annotai?style=flat&amp;logo=npm&amp;logoColor=white&amp;color=CB3837&amp;label=downloads" alt="npm downloads"></a>
  <a href="#license"><img src="https://img.shields.io/badge/License-MIT-blue?style=flat&amp;logo=opensourceinitiative&amp;logoColor=white" alt="MIT license"></a>
  <br>
  <a href="https://www.typescriptlang.org/"><img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat&amp;logo=typescript&amp;logoColor=white" alt="TypeScript"></a>
  <a href="https://vitejs.dev/"><img src="https://img.shields.io/badge/Vite-646CFF?style=flat&amp;logo=vite&amp;logoColor=white" alt="Vite"></a>
  <a href="https://playwright.dev/"><img src="https://img.shields.io/badge/Playwright-2EAD33?style=flat&amp;logo=playwright&amp;logoColor=white" alt="Playwright"></a>
  <br>
  <a href="https://react.dev/"><img src="https://img.shields.io/badge/React-61DAFB?style=flat&amp;logo=react&amp;logoColor=black" alt="React"></a>
  <a href="https://vuejs.org/"><img src="https://img.shields.io/badge/Vue-4FC08D?style=flat&amp;logo=vuedotjs&amp;logoColor=white" alt="Vue"></a>
  <a href="https://solidjs.com/"><img src="https://img.shields.io/badge/Solid-2C4F7C?style=flat&amp;logo=solid&amp;logoColor=white" alt="Solid"></a>
</p>

Show AI exactly which element you're talking about: select elements in the browser, collect precise source context with your questions, and copy AI-ready Markdown. Hold Alt+Shift and click to open the source in your editor or IDE. When a click lands on DOM rendered by a prebuilt component library (no definition marks), the selection falls back to the component's call-site JSX — as long as the call-site path has propagated to the root element.

![demo](https://github.com/beixiyo/annotai/releases/download/v0.3.0/demo.gif)

Open the panel → select elements → type your question → pick the next spot (finished groups are kept automatically) → copy. Hover any element for a live source preview with the element's line highlighted and syntax coloring.

## How it compares

| Capability              | annotai                                                                                                     | [code-inspector-plugin](https://github.com/zh-lx/code-inspector) | [agentation](https://github.com/benjitaylor/agentation) |
| ----------------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------- |
| Source locating         | sourcemap-exact to line & column                                                                            | exact                                                            | inaccurate, no file path                                |
| Neovim jump             | ✔ socket discovery, cwd matching, UTF-16 column conversion                                                  | ✘                                                                | ✘                                                       |
| Other editors           | `open` hook for anything; falls back to launch-ide                                                          | VSCode / Cursor / WebStorm                                       | ✘                                                       |
| Plain-text DOM location | `data-annotai-path` (definition) + `data-annotai-use-path` (call site) on one element, readable in DevTools | `data-insp-path`, call site overwrites the definition site       | ✘                                                       |
| Hover source preview    | ✔ highlighted element line + syntax coloring + auto scroll into view                                        | ✘                                                                | ✘                                                       |
| Output for AI           | Markdown with paths, line/column and snippets — paste and go                                                | none (human-oriented jumping)                                    | CSS selectors, AI has to grep again                     |
| Question list           | select + annotate + field toggles, kept automatically per group                                             | ✘                                                                | ✘                                                       |
| Frameworks              | React / Vue / Solid                                                                                         | React / Vue etc.                                                 | React                                                   |
| Shape                   | build-time plugin, dev only, zero residue in production                                                     | same                                                             | React runtime component, mounted in production too      |

## Getting started

```sh
npm install -D annotai
yarn add -D annotai
pnpm add -D annotai
bun add -d annotai
```

```ts
import react from '@vitejs/plugin-react'
import { annotate } from 'annotai/vite'
import { defineConfig } from 'vite'

export default defineConfig({
  // put annotai before framework plugins
  plugins: [annotate({ editor: { name: 'nvim' } }), react()],
})
```

The toolbar injects itself — no components to mount. Production builds skip injection and never start the source service.

Common options (all optional):

```ts
annotate({
  editor: { name: 'nvim' }, // or an open hook for any editor
  hoverPreview: true, // hover source preview; { width, maxLines } to size the card
  locale: 'en', // UI & Markdown export language: 'en' | 'zh'
  hotKeys: ['altKey', 'shiftKey'], // [] disables the jump hotkey
  surroundingLines: 4, // context lines around exported snippets
  context: { domPath: false }, // Markdown field toggles
  animation: true, // respects prefers-reduced-motion
  theme: {
    dimOpacity: 0.4, // panel fade while selecting on the page (1 disables it)
    vars: { '--sn-primary': '#6366f1' }, // override any --sn-* CSS variable: panel palette, selection highlight, preview, token colors
  },
})
```

Everything the toolbar paints is driven by `--sn-*` CSS variables on its shadow host — `theme.vars` overrides any of them (panel palette `--sn-panel/--sn-text/--sn-line/...`, selection highlight `--sn-highlight*/--sn-drag-*`, hover preview `--sn-preview-*`, syntax tokens `--sn-tok-*`). Once set, the toolbar stops following the system light/dark scheme.

### All options

| Option             | Type                                                   | Default                                            | Description                                                                                                                                                                                                |
| ------------------ | ------------------------------------------------------ | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `editor`           | `{ name?: 'nvim'; server?: string } \| { open }`       | Neovim auto-discovery                              | Jump target editor: discovers Neovim sockets by default and falls back to launch-ide for running IDEs (pin one with `CODE_EDITOR`); `server` targets a specific socket; the `open` hook takes full control |
| `hotKeys`          | `('altKey' \| 'shiftKey' \| 'ctrlKey' \| 'metaKey')[]` | `['altKey', 'shiftKey']`                           | Modifier combo that opens the editor; `[]` disables the hotkey                                                                                                                                             |
| `hoverPreview`     | `boolean \| { width?; maxLines? }`                     | `true` (`width` 560, `maxLines` 20)                | Hover source preview                                                                                                                                                                                       |
| `locale`           | `'zh' \| 'en'`                                         | `'en'`                                             | UI & Markdown export language                                                                                                                                                                              |
| `surroundingLines` | `number`                                               | `4`                                                | Context lines added above/below exported snippets (0–100)                                                                                                                                                  |
| `context`          | `Partial<ContextOptions>`                              | location / snippet / class / text on, DOM path off | Markdown field toggles                                                                                                                                                                                     |
| `animation`        | `boolean`                                              | `true`                                             | Panel & highlight animations; prefers-reduced-motion wins                                                                                                                                                  |
| `theme`            | `{ dimOpacity?; vars? }`                               | built-in theme (`dimOpacity` 0.3)                  | Panel fade opacity and any `--sn-*` CSS variable override                                                                                                                                                  |
| `formatCopy`       | `(context) => string`                                  | built-in Markdown                                  | Browser-side clipboard formatter; inlined as source, must be self-contained                                                                                                                                |
| `onCopy`           | `(payload) => void \| Promise<void>`                   | —                                                  | Node-side copy hook: receives the final Markdown plus all annotations; runs async without blocking the browser, failures print to the terminal                                                             |
| `maxBodyBytes`     | `number`                                               | `2097152`                                          | Per-request body cap of the source service, in bytes                                                                                                                                                       |
| `projectRoot`      | `string`                                               | Vite workspace root                                | Base for relative Markdown paths; does not widen readable dirs                                                                                                                                             |
| `allowedRoots`     | `string[]`                                             | `[vite.root]`                                      | Dirs whose sources may be processed, relative to the Vite root; symlinks validated by real path                                                                                                            |
| `transforms`       | `SourceTransform[]`                                    | `[reactTransform]`                                 | Syntax adapters, first supporting one wins; Vue / Solid pass their built-in transform                                                                                                                      |
| `client`           | `boolean`                                              | `true`                                             | Whether to inject the browser toolbar                                                                                                                                                                      |

Customize what lands on the clipboard — annotai hands you the context:

```ts
annotate({
  // runs in the browser; must be self-contained (no closures / Node APIs)
  formatCopy: ({ annotations, fields }) => annotations.map((a) => a.question).join('\n'),
})
```

Forward every copy to your own Node-side hook — you get the final Markdown plus the structured annotations, and decide what happens next (hand it to an agent, POST it somewhere, write a file…):

```ts
annotate({
  // runs in the Vite dev server process (Node); fire-and-forget, errors surface in the terminal
  onCopy: ({ markdown }) => {
    spawn('pi', ['-p', markdown], { stdio: 'inherit' })
  },
})
```

The payload rides the same dev-server endpoint as element resolution and is capped at 2 MB by default — raise it with `maxBodyBytes` if your copies grow huge.

Alt+Shift click opens the source in the editor or IDE you're using: running IDEs such as VS Code, Cursor and WebStorm, as well as Neovim, are detected automatically. Pin one with the `CODE_EDITOR` env var (or in `.env.local`), or take full control with the `open` hook:

```ts
annotate({
  editor: {
    open: ({ file, line, column }) => execFile('code', ['--goto', `${file}:${line}:${column}`]),
  },
})
```

Vue / Solid ship their own built-in transforms:

```ts
import { annotate } from 'annotai/vite'
import { vueTransform } from 'annotai/vue'
// Solid: import { solidTransform } from 'annotai/solid'

export default defineConfig({
  plugins: [annotate({ transforms: [vueTransform] }), vue()],
})
```

You declare the framework because `.tsx/.jsx` can't tell React from Solid compile targets.

## License

MIT
