<p align="center">
  <img src="https://raw.githubusercontent.com/msobkyy/react-native-shader-orbs/main/docs/images/banner.png" alt="react-native-shader-orbs: 33 WebGPU shaders for React Native and Expo" width="100%" />
</p>

<h1 align="center">react-native-shader-orbs</h1>

<p align="center">
  <b>GPU shader orbs for React Native and Expo.</b><br />
  33 WebGPU shaders as drop-in components. Live parameters, touch, adaptive quality, and ready for AI coding agents.
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/react-native-shader-orbs"><img alt="npm" src="https://img.shields.io/npm/v/react-native-shader-orbs?label=npm&color=7c5cff" /></a>
  <a href="https://www.npmjs.com/package/react-native-shader-orbs-mcp"><img alt="mcp" src="https://img.shields.io/npm/v/react-native-shader-orbs-mcp?label=mcp&color=7c5cff" /></a>
  <a href="https://github.com/msobkyy/react-native-shader-orbs/actions/workflows/ci.yml"><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/msobkyy/react-native-shader-orbs/ci.yml?branch=main&label=CI" /></a>
  <img alt="types" src="https://img.shields.io/npm/types/react-native-shader-orbs?color=3178c6" />
  <img alt="platform" src="https://img.shields.io/badge/Android-tested-3ddc84" />
  <a href="https://x.com/msobkyy"><img alt="follow" src="https://img.shields.io/badge/follow-%40msobkyy-000000?logo=x" /></a>
</p>

<p align="center">
  <a href="https://react-native-shader-orbs.vercel.app"><b>Docs</b></a> ·
  <a href="https://react-native-shader-orbs.vercel.app/playground/"><b>Playground</b></a> ·
  <a href="https://react-native-shader-orbs.vercel.app/docs/components/orbs/"><b>All orbs</b></a> ·
  <a href="https://www.npmjs.com/package/react-native-shader-orbs"><b>npm</b></a> ·
  <a href="https://react-native-shader-orbs.vercel.app/llms.txt">llms.txt</a>
</p>

<br />

```bash
npx expo install react-native-shader-orbs react-native-webgpu react-native-reanimated react-native-worklets
```

```tsx
import { ShaderOrb, orb01 } from "react-native-shader-orbs";

<ShaderOrb orb={orb01} state="speaking" colors={{ tint: "#66ccff" }} interactive />
```

> **Alpha.** The API may change. Read [Status](#status) before you build on it: it needs a development build (not Expo Go), it is tested on Android only, and the shaders are licensed for **non-commercial use**.

<p align="center">
  <img src="https://raw.githubusercontent.com/msobkyy/react-native-shader-orbs/main/docs/images/orbs.png" alt="Twelve of the 33 orbs" width="100%" />
</p>

## Features

- **33 orbs**, each with its own typed, range-checked parameters and colors.
- **Three moods** per orb (`idle`, `thinking`, `speaking`) that ease between presets.
- **Live props.** Change anything without re-mounting; every value glides to its target on a spring.
- **Audio-ready.** `volumes.input` and `volumes.output` (0 to 1) drive an orb from a mic or voice level.
- **Touch.** A tap pulses the orb, holding makes it swell, and it scales under your finger.
- **Adaptive quality.** `quality="auto"` trades resolution for frame rate when a device struggles.
- **Light on the JS thread.** One shared GPU device, cached pipelines, and a `live` prop so sliders never re-render React.
- **Recovers from GPU loss** and reports start-up failures through `onError`.
- **Typed**, and you import only the orbs you use.
- **The same shaders on the web.** The docs site and playground render the identical WGSL through the browser's WebGPU.

## Try them live

Every orb has a live preview, its full parameter list and copy-paste code in the [docs](https://react-native-shader-orbs.vercel.app/docs/components/orbs/). The [playground](https://react-native-shader-orbs.vercel.app/playground/) lets you tune any orb and copy the JSX.

<p align="center">
  <a href="https://react-native-shader-orbs.vercel.app/playground/">
    <img src="https://raw.githubusercontent.com/msobkyy/react-native-shader-orbs/main/docs/images/playground.png" alt="The playground: pick an orb, change its mood, colors and parameters, copy the code" width="92%" />
  </a>
</p>

## Built for AI agents

Parameter names and ranges differ for every orb, and a wrong guess gives you a black orb. One command sets up your coding assistant so it looks the real values up:

```bash
npx react-native-shader-orbs-mcp init
```

It adds MCP config for Claude Code, Cursor and VS Code, a Claude Code skill, an `AGENTS.md` block and a Cursor rule. It merges instead of overwriting and supports `--dry-run`. The package itself ships `agent/INSTRUCTIONS.md` and a per-orb `agent/catalog.json`, and the docs site serves [`llms.txt`](https://react-native-shader-orbs.vercel.app/llms.txt) and a Markdown copy of every page. See [MCP server and skills](https://react-native-shader-orbs.vercel.app/docs/mcp/).

## Status

| | |
|---|---|
| Release | **Alpha.** The API may change between releases. |
| Expo | A **development build**. **Expo Go is not supported** (native WebGPU module). |
| Android | **Tested**, on one physical mid-range phone (React Native 0.88, Expo SDK 58). |
| iOS | **Not tested.** `react-native-webgpu` supports it, so it may work, but nothing here claims it does. |
| No WebGPU | The orb stays blank. There is no fallback yet. |
| Licence | Library code is **MIT**. The shaders are by [XorDev](https://x.com/XorDev) and are licensed for **non-commercial use with attribution**. See below. |

## Repository

| Path | What |
|---|---|
| [`packages/react-native-shader-orbs`](packages/react-native-shader-orbs) | The library, published to npm |
| [`packages/mcp`](packages/mcp) | MCP server and agent setup (`react-native-shader-orbs-mcp`) |
| [`packages/codegen`](packages/codegen) | Generates the orb files from the upstream TypeGPU shaders |
| [`apps/web`](apps/web) | Docs site and playground (Next.js), deployed to Vercel |
| [`apps/example`](apps/example) | Expo showcase app with all 33 orbs |

<p align="center">
  <a href="https://react-native-shader-orbs.vercel.app/docs/">
    <img src="https://raw.githubusercontent.com/msobkyy/react-native-shader-orbs/main/docs/images/docs.png" alt="The documentation site" width="92%" />
  </a>
</p>

## Develop

```bash
pnpm install
cd packages/react-native-shader-orbs && npm run verify   # typecheck, tests, build, package checks
cd apps/web && npx next build                            # docs site
cd packages/mcp && npm run smoke                         # MCP server
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for what is generated and how to change it.

## License

This repository holds material under **two sets of terms**; read [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md).

- The React Native code, the docs site and the tooling are **MIT**.
- The **33 orb shaders** are original work by [XorDev](https://x.com/XorDev), from [shadcn-labs/shadercn](https://github.com/shadcn-labs/shadercn), and are licensed for **non-commercial use with attribution**. Using them in a commercial app needs XorDev's permission. The notice at the top of every shader file must stay.

Suggested attribution: *Orb shaders by XorDev (https://x.com/XorDev), via shadercn and react-native-shader-orbs.*

## Credits

Shaders by [XorDev](https://x.com/XorDev), from [shadercn](https://github.com/shadcn-labs/shadercn). React Native port by [msobkyy](https://x.com/msobkyy). Not affiliated with or endorsed by shadercn.
