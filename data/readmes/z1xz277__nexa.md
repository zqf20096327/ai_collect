# Nexa

Nexa is a focused Windows 11 desktop workspace for coding. It combines project files, a code editor, a terminal, and a tool-using agent with explicit per-run access controls.

## Run

Requires Node 20+ and Windows 11 for the desktop app.

```bash
npm install
npm run dev
```

For a production build:

```bash
npm run build
npm start
```

A renderer-only browser preview uses local sample data and a scripted provider:

```bash
npm run preview
```

Open `http://localhost:5173`. The preview has no Electron preload, so Nexa selects the in-browser bridge automatically.

## Windows installer

The installer source lives in `setup/`. Install both projects, then link and package the current harness:

```bash
npm install
npm --prefix setup install
npm run setup
```

The verified portable installer is written to `setup/release/NexaSetup.exe`. Generated installers, payloads, and packaged apps are not committed. See `setup/README.md` for installation, uninstall, and smoke-test details.

## Access modes

The model and access picker applies the selected mode to the next run.

| Mode | File access | Commands and changes |
| --- | --- | --- |
| Ask | Read, list, and search files inside the project | No writes, edits, commands, or agent-initiated network tools |
| Agent | Read and change files inside the project | Writes, edits, memory updates, and commands require approval |
| Full Access | File tools remain inside the project | Mutations are approved automatically for one run after explicit confirmation |

Full Access requires a short-lived, single-use grant issued by the host for the actual session and project. Renderer input cannot grant itself elevated capabilities. Shell commands are not sandboxed: they use the Windows account's permissions and can access the network or files outside the project. The confirmation dialog states this before enabling the mode.

Stop or Kill ends the run and rejects pending approvals. File operations fail closed on invalid paths, traversal, unresolved links, symlink or junction escapes, and invalid tool arguments.

## Architecture

The UI-agnostic agent core runs behind Electron IPC on desktop and behind the browser mock in preview mode. Both use the same request validation and trusted-run flow.

- `src/core/agent.ts`: streaming loop, tool dispatch, approvals, and run lifecycle.
- `src/core/access.ts`: capability validation and host-issued grants.
- `src/core/tools.ts`: schemas and project-scoped tool implementations.
- `src/core/providers/`: NVIDIA NIM and OpenRouter adapters, model discovery, streaming, and fallback.
- `src/main/`: window, persistence, sandboxed filesystem policy, terminal, and IPC.
- `src/preload/`: typed, isolated `contextBridge`.
- `src/renderer/`: React interface, Zustand state, Monaco, xterm, and browser mock.

Provider keys stay in the main process. Desktop keys use Electron `safeStorage` when available, with an in-memory fallback. A local `.env.local` file can supply keys for development; it is loaded only by the main process and is never exposed to the renderer or bundled into the application.

## Visual system

The interface uses a strict monochrome palette. Light mode is white with black text and accent. Dark mode is black with white text and neutral surfaces. Status colors are reserved for success and errors. Rounded surfaces, visible focus states, short functional transitions, and reduced-motion settings keep the workspace calm and usable.

The Nexa leaf is the only brand mark. Provider logos are bundled locally and render through `currentColor`; no logos are fetched at runtime.

## Verification

```bash
npm test
npm run typecheck
npm run build
npm run smoke
```

The test suite covers access grants, trusted request validation, path boundaries, approval edits, run replacement, and command termination.

Optional UI automation requires Chrome and Puppeteer Core. The desktop harness connects to Electron on port 9222 and creates an isolated QA project without deleting existing projects.

```bash
npx electron . --remote-debugging-port=9222
node qa/electron-qa.mjs
```

For the scripted browser run, start the preview first:

```bash
node qa/demo-flow.mjs
```

## Updates

The Windows app checks for updates after launch and every six hours. Downloads are verified with SHA-512 and an Authenticode signature when publisher metadata is present. Updates install on restart.

`update-server/server.mjs` serves the release API, manifests, artifacts, blockmaps, and monochrome download page. Uploads require a bearer token, are hash-verified while streaming, and use atomic replacement. The default feed can be changed in `src/main/updater.ts`.

A prepared release contains the executable, optional blockmap, and `latest.yml`. Public releases require a trusted signing certificate. Never commit certificate material, passwords, or release tokens.

```bash
npm run server:updates
npm run publish:update
```

Set `NEXA_RELEASE_TOKEN` and, when needed, `NEXA_UPDATE_SERVER` in the publishing environment. The configured endpoint is not proof that hosting is live: public downloads also require DNS, HTTPS, a deployed server, and a signed release.
