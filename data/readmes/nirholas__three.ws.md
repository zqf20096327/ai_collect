# three.ws                  
  
[**Website**](https://three.ws) · [**Docs**](https://three.ws/docs) · [**Changelog**](https://three.ws/changelog) · [**X / Twitter**](https://x.com/trythreews) · [**GitHub**](https://github.com/nirholas/three.ws) · [**$THREE on pump.fun**](https://pump.fun/FeMbDoX7R1Psc4GEcvJdsbNbZA3bfztcyDCatJVJpump)

[![site](https://img.shields.io/website?url=https%3A%2F%2Fthree.ws&label=three.ws)](https://three.ws) [![npm](https://img.shields.io/npm/v/%40three-ws%2Fsdk?label=%40three-ws%2Fsdk)](https://www.npmjs.com/package/@three-ws/sdk) [![npm](https://img.shields.io/npm/v/%40three-ws%2Fmcp-server?label=%40three-ws%2Fmcp-server)](https://www.npmjs.com/package/@three-ws/mcp-server) [![MCP Registry](https://img.shields.io/badge/MCP_Registry-io.github.nirholas-blue)](https://registry.modelcontextprotocol.io/?q=io.github.nirholas) [![x402scan](https://img.shields.io/badge/x402scan-listed-green)](https://www.x402scan.com/server/17cbd874-52ac-4920-a020-b22ff2489a07) [![License: Apache 2.0](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE) [![good first issues](https://img.shields.io/github/issues/nirholas/three.ws/good%20first%20issue?label=good%20first%20issues&color=7057ff)](https://github.com/nirholas/three.ws/labels/good%20first%20issue)

https://github.com/user-attachments/assets/d52515d1-cb04-4dd6-98bd-fef233312dc4

**Give your AI a body.** three.ws is an open source (Apache-2.0), browser-native 3D AI agent platform. Type a prompt and [**Forge**](https://three.ws/forge) generates a textured 3D model, or drop a GLB you already have. Add an LLM brain, register on-chain, and embed anywhere: no plugins, no server uploads, no installs required.

> **Try it in 60 seconds:** open [three.ws/forge](https://three.ws/forge), type *"a brass steampunk owl, full body"*, and download the GLB. Text→3D, image→3D, and sketch→3D — free draft tier, no account. [Jump to the Forge section ↓](#forge--text--image-to-3d)

> **Want to build it with us?** [Your first contribution](docs/first-contribution.md) goes from clone to open pull request in about 15 minutes, with a full worked example. Every [`good first issue`](https://github.com/nirholas/three.ws/labels/good%20first%20issue) names the file to change and the command that proves it worked. Say hello in [Discussions](https://github.com/nirholas/three.ws/discussions) or [Telegram](https://t.me/three_ws_community).

### Meet the avatar: a live 3D model, right here in markdown

Drag to rotate. This is not an image or a video: it is an interactive 3D model rendered natively by GitHub. The avatar was generated from a one-line text prompt on [three.ws Forge](https://three.ws/forge) (free tier), decimated to 1,200 triangles, and embedded as ASCII STL with [readme-3d](packages/readme-3d), our open-source toolkit for putting 3D models in any GitHub README, issue, or discussion.

```stl
solid threews_avatar
 facet normal -0.34 -0.93 0.11
  outer loop
   vertex 7.06 -3.99 23.19
   vertex 9.13 -4.19 27.78
   vertex 3.98 -2.59 25.51
  endloop
 endfacet
 facet normal -0.94 -0.30 0.16
  outer loop
   vertex 17.94 3.99 37.76
   vertex 18.01 2.79 35.88
   vertex 18.27 2.91 37.66
  endloop
 endfacet
 facet normal -0.90 0.43 0.10
  outer loop
   vertex 18.27 2.91 37.66
   vertex 18.01 2.79 35.88
   vertex 17.73 2.15 36.16
  endloop
 endfacet
 facet normal -0.92 0.36 0.15
  outer loop
   vertex 18.27 2.91 37.66
   vertex 17.73 2.15 36.16
   vertex 17.95 2.20 37.37
  endloop
 endfacet
 facet normal 0.94 0.34 0.00
  outer loop
   vertex 27.20 5.38 33.47
   vertex 28.47 1.83 38.79
   vertex 28.90 0.61 31.76
  endloop
 endfacet
 facet normal 0.91 -0.25 0.33
  outer loop
   vertex 28.01 -2.89 36.41
   vertex 28.47 1.83 38.79
   vertex 26.14 -2.49 41.92
  endloop
 endfacet
 facet normal 0.99 -0.14 0.08
  outer loop
   vertex 28.47 1.83 38.79
   vertex 28.01 -2.89 36.41
   vertex 28.90 0.61 31.76
  endloop
 endfacet
 facet normal 0.91 0.06 -0.40
  outer loop
   vertex 28.90 0.61 31.76
   vertex 27.10 -0.47 27.53
   vertex 27.03 3.46 27.96
  endloop
 endfacet
 facet normal 0.83 -0.51 -0.22
  outer loop
   vertex 28.01 -2.89 36.41
   vertex 27.10 -0.47 27.53
   vertex 28.90 0.61 31.76
  endloop
 endfacet
 facet normal 0.91 0.38 -0.16
  outer loop
   vertex 27.20 5.38 33.47
   vertex 28.90 0.61 31.76
   vertex 27.03 3.46 27.96
  endloop
 endfacet
 facet normal 0.89 0.45 0.09
  outer loop
   vertex 26.88 4.99 38.80
   vertex 28.47 1.83 38.79
   vertex 27.20 5.38 33.47
  endloop
 endfacet
 facet normal 0.90 -0.39 -0.20
  outer loop
   vertex 28.01 -2.89 36.41
   vertex 26.22 -3.16 28.82
   vertex 27.10 -0.47 27.53
  endloop
 endfacet
 facet normal 0.82 -0.02 0.58
  outer loop
   vertex 23.27 4.13 46.24
   vertex 26.14 -2.49 41.92
   vertex 28.47 1.83 38.79
  endloop
 endfacet
 facet normal 0.80 0.40 0.44
  outer loop
   vertex 26.88 4.99 38.80
   vertex 23.27 4.13 46.24
   vertex 28.47 1.83 38.79
  endloop
 endfacet
 facet normal 0.70 -0.07 -0.71
  outer loop
   vertex 27.03 3.46 27.96
   vertex 24.69 2.15 25.80
   vertex 25.39 4.36 26.25
  endloop
 endfacet
 facet normal 0.63 -0.73 0.27
  outer loop
   vertex 28.01 -2.89 36.41
   vertex 26.14 -2.49 41.92
   vertex 24.39 -5.14 38.78
  endloop
 endfacet
 facet normal 0.56 -0.82 0.08
  outer loop
   vertex 28.01 -2.89 36.41
   vertex 24.39 -5.14 38.78
   vertex 24.40 -5.59 34.11
  endloop
 endfacet
 facet normal 0.64 -0.76 -0.12
  outer loop
   vertex 28.01 -2.89 36.41
   vertex 24.40 -5.59 34.11
   vertex 26.22 -3.16 28.82
  endloop
 endfacet
 facet normal 0.37 -0.89 -0.28
  outer loop
   vertex 24.40 -5.59 34.11
   vertex 23.26 -5.15 31.23
   vertex 26.22 -3.16 28.82
  endloop
 endfacet
 facet normal 0.42 -0.20 -0.89
  outer loop
   vertex 27.10 -0.47 27.53
   vertex 24.15 0.41 25.94
   vertex 24.69 2.15 25.80
  endloop
 endfacet
 facet normal 0.34 -0.94 0.00
  outer loop
   vertex 26.22 -3.16 28.82
   vertex 23.11 -4.26 27.61
   vertex 24.16 -3.89 27.34
  endloop
 endfacet
 facet normal 0.40 -0.88 -0.23
  outer loop
   vertex 23.26 -5.15 31.23
   vertex 23.11 -4.26 27.61
   vertex 26.22 -3.16 28.82
  endloop
 endfacet
 facet normal -0.24 0.97 -0.05
  outer loop
   vertex 24.58 4.14 25.81
   vertex 25.39 4.36 26.25
   vertex 22.37 3.43 22.62
  endloop
 endfacet
 facet normal 0.64 -0.61 -0.46
  outer loop
   vertex 27.10 -0.47 27.53
   vertex 24.14 -2.60 26.21
   vertex 21.62 -2.12 22.03
  endloop
 endfacet
 facet normal 0.78 -0.11 -0.62
  outer loop
   vertex 25.39 4.36 26.25
   vertex 22.59 1.54 23.24
   vertex 22.37 3.43 22.62
  endloop
 endfacet
 facet normal 0.78 -0.12 -0.61
  outer loop
   vertex 25.39 4.36 26.25
   vertex 24.69 2.15 25.80
   vertex 22.59 1.54 23.24
  endloop
 endfacet
 facet normal 0.46 -0.87 -0.17
  outer loop
   vertex 22.82 1.11 26.12
   vertex 22.59 1.54 23.24
   vertex 24.69 2.15 25.80
  endloop
 endfacet
 facet normal 0.05 -0.66 -0.75
  outer loop
   vertex 23.11 -4.26 27.61
   vertex 24.14 -2.60 26.21
   vertex 24.16 -3.89 27.34
  endloop
 endfacet
 facet normal 0.32 -0.80 0.50
  outer loop
   vertex 26.14 -2.49 41.92
   vertex 21.60 -3.52 43.21
   vertex 24.39 -5.14 38.78
  endloop
 endfacet
 facet normal -0.37 -0.90 -0.21
  outer loop
   vertex 23.26 -5.15 31.23
   vertex 21.41 -3.57 27.63
   vertex 23.11 -4.26 27.61
  endloop
 endfacet
 facet normal -0.23 -0.54 -0.81
  outer loop
   vertex 23.11 -4.26 27.61
   vertex 21.41 -3.57 27.63
   vertex 24.14 -2.60 26.21
  endloop
 endfacet
 facet normal -0.01 -1.00 0.10
  outer loop
   vertex 24.39 -5.14 38.78
   vertex 20.81 -5.34 36.22
   vertex 24.40 -5.59 34.11
  endloop
 endfacet
 facet normal 0.52 -0.77 0.37
  outer loop
   vertex 20.28 -1.08 52.96
   vertex 18.87 -2.53 51.93
   vertex 26.14 -2.49 41.92
  endloop
 endfacet
 facet normal -0.14 -0.95 0.26
  outer loop
   vertex 21.60 -3.52 43.21
   vertex 20.81 -5.34 36.22
   vertex 24.39 -5.14 38.78
  endloop
 endfacet
 facet normal -0.13 -0.99 -0.10
  outer loop
   vertex 24.40 -5.59 34.11
   vertex 20.81 -5.34 36.22
   vertex 23.26 -5.15 31.23
  endloop
 endfacet
 facet normal 0.03 -0.99 -0.15
  outer loop
   vertex 22.82 1.11 26.12
   vertex 19.99 1.49 22.99
   vertex 22.59 1.54 23.24
  endloop
 endfacet
 facet normal 0.91 0.14 0.38
  outer loop
   vertex 23.27 4.13 46.24
   vertex 20.84 0.68 53.36
   vertex 26.14 -2.49 41.92
  endloop
 endfacet
 facet normal -0.14 -0.99 -0.03
  outer loop
   vertex 24.14 -2.60 26.21
   vertex 18.46 -1.70 22.74
   vertex 21.62 -2.12 22.03
  endloop
 endfacet
 facet normal 0.87 0.27 0.43
  outer loop
   vertex 20.33 2.84 53.04
   vertex 20.84 0.68 53.36
   vertex 23.27 4.13 46.24
  endloop
 endfacet
 facet normal -0.48 -0.82 0.30
  outer loop
   vertex 22.34 1.45 26.31
   vertex 18.93 2.50 23.81
   vertex 22.82 1.11 26.12
  endloop
 endfacet
 facet normal -0.49 -0.80 0.35
  outer loop
   vertex 22.82 1.11 26.12
   vertex 18.93 2.50 23.81
   vertex 19.99 1.49 22.99
  endloop
 endfacet
 facet normal 0.80 -0.36 0.47
  outer loop
   vertex 20.84 0.68 53.36
   vertex 20.28 -1.08 52.96
   vertex 26.14 -2.49 41.92
  endloop
 endfacet
 facet normal -0.62 -0.30 0.72
  outer loop
   vertex 22.22 3.87 27.21
   vertex 18.93 2.50 23.81
   vertex 22.34 1.45 26.31
  endloop
 endfacet
 facet normal -0.80 0.13 0.59
  outer loop
   vertex 21.74 -0.40 26.89
   vertex 18.46 -1.70 22.74
   vertex 21.76 -1.78 27.21
  endloop
 endfacet
 facet normal -0.79 -0.21 0.58
  outer loop
   vertex 21.76 -1.78 27.21
   vertex 18.46 -1.70 22.74
   vertex 21.75 -2.39 26.98
  endloop
 endfacet
 facet normal -0.54 -0.84 -0.09
  outer loop
   vertex 23.26 -5.15 31.23
   vertex 17.89 -1.75 31.72
   vertex 21.41 -3.57 27.63
  endloop
 endfacet
 facet normal 0.10 -0.26 -0.96
  outer loop
   vertex 22.59 1.54 23.24
   vertex 19.99 1.49 22.99
   vertex 20.26 3.48 22.48
  endloop
 endfacet
 facet normal 0.96 0.24 0.12
  outer loop
   vertex 20.67 -0.54 57.28
   vertex 20.84 0.68 53.36
   vertex 20.33 2.84 53.04
  endloop
 endfacet
 facet normal -0.53 -0.80 -0.29
  outer loop
   vertex 20.81 -5.34 36.22
   vertex 17.89 -1.75 31.72
   vertex 23.26 -5.15 31.23
  endloop
 endfacet
 facet normal 1.00 0.05 0.05
  outer loop
   vertex 19.64 4.31 87.94
   vertex 19.89 8.80 78.04
   vertex 19.60 7.11 85.93
  endloop
 endfacet
 facet normal 1.00 0.04 0.04
  outer loop
   vertex 19.64 4.31 87.94
   vertex 19.78 0.25 88.57
   vertex 19.89 8.80 78.04
  endloop
 endfacet
 facet normal 0.96 0.26 0.13
  outer loop
   vertex 19.46 3.33 58.61
   vertex 20.67 -0.54 57.28
   vertex 20.33 2.84 53.04
  endloop
 endfacet
 facet normal 0.96 -0.29 -0.05
  outer loop
   vertex 20.67 -0.54 57.28
   vertex 20.28 -1.08 52.96
   vertex 20.84 0.68 53.36
  endloop
 endfacet
 facet normal -0.11 -0.99 -0.07
  outer loop
   vertex 24.14 -2.60 26.21
   vertex 21.75 -2.39 26.98
   vertex 18.46 -1.70 22.74
  endloop
 endfacet
 facet normal 1.00 -0.03 -0.02
  outer loop
   vertex 19.89 8.80 78.04
   vertex 19.78 0.25 88.57
   vertex 19.45 -6.79 83.01
  endloop
 endfacet
 facet normal 1.00 0.00 0.07
  outer loop
   vertex 19.89 8.80 78.04
   vertex 19.45 -6.79 83.01
   vertex 20.12 -4.30 73.94
  endloop
 endfacet
 facet normal 0.93 0.30 -0.21
  outer loop
   vertex 19.89 8.80 78.04
   vertex 19.93 5.01 72.90
   vertex 19.58 8.54 76.35
  endloop
 endfacet
 facet normal -0.70 -0.09 0.71
  outer loop
   vertex 22.22 3.87 27.21
   vertex 19.00 3.74 24.02
   vertex 18.93 2.50 23.81
  endloop
 endfacet
 facet normal 0.99 0.00 -0.17
  outer loop
   vertex 20.12 -4.30 73.94
   vertex 19.78 1.87 71.95
   vertex 19.93 5.01 72.90
  endloop
 endfacet
 facet normal 1.00 0.02 -0.01
  outer loop
   vertex 19.89 8.80 78.04
   vertex 20.12 -4.30 73.94
   vertex 19.93 5.01 72.90
  endloop
 endfacet
 facet normal 0.79 -0.61 0.01
  outer loop
   vertex 20.67 -0.54 57.28
   vertex 18.66 -3.15 57.91
   vertex 20.28 -1.08 52.96
  endloop
 endfacet
 facet normal 0.27 -0.95 0.19
  outer loop
   vertex 26.14 -2.49 41.92
   vertex 18.87 -2.53 51.93
   vertex 21.60 -3.52 43.21
  endloop
 endfacet
 facet normal 0.99 0.13 0.11
  outer loop
   vertex 19.45 -6.79 83.01
   vertex 20.12 -5.67 75.56
   vertex 20.12 -4.30 73.94
  endloop
 endfacet
 facet normal -0.77 -0.07 0.63
  outer loop
   vertex 19.80 0.58 24.64
   vertex 18.46 -1.70 22.74
   vertex 21.74 -0.40 26.89
  endloop
 endfacet
 facet normal 0.99 -0.11 0.08
  outer loop
   vertex 19.78 0.25 88.57
   vertex 19.38 -4.86 86.48
   vertex 19.45 -6.79 83.01
  endloop
 endfacet
 facet normal 0.73 -0.52 -0.45
  outer loop
   vertex 20.12 -4.30 73.94
   vertex 20.12 -5.67 75.56
   vertex 17.93 -5.99 72.36
  endloop
 endfacet
 facet normal 0.30 -0.95 -0.11
  outer loop
   vertex 19.45 -6.79 83.01
   vertex 17.93 -5.99 72.36
   vertex 20.12 -5.67 75.56
  endloop
 endfacet
 facet normal -0.47 0.12 0.87
  outer loop
   vertex 18.22 5.83 86.97
   vertex 18.49 -1.78 88.13
   vertex 19.78 0.25 88.57
  endloop
 endfacet
 facet normal 0.97 0.25 0.07
  outer loop
   vertex 19.11 0.55 6.61
   vertex 18.74 3.81 0.23
   vertex 18.00 5.61 3.97
  endloop
 endfacet
 facet normal 1.00 0.07 -0.02
  outer loop
   vertex 18.74 3.81 0.23
   vertex 19.11 0.55 6.61
   vertex 19.30 -4.41 0.13
  endloop
 endfacet
 facet normal 0.28 -0.37 0.89
  outer loop
   vertex 19.78 0.25 88.57
   vertex 18.49 -1.78 88.13
   vertex 18.53 -3.21 87.53
  endloop
 endfacet
 facet normal 0.73 -0.68 -0.04
  outer loop
   vertex 18.66 -3.15 57.91
   vertex 18.87 -2.53 51.93
   vertex 20.28 -1.08 52.96
  endloop
 endfacet
 facet normal 0.06 -0.99 0.13
  outer loop
   vertex 18.87 -2.53 51.93
   vertex 17.09 -2.77 50.96
   vertex 21.60 -3.52 43.21
  endloop
 endfacet
 facet normal -0.68 -0.64 0.36
  outer loop
   vertex 21.60 -3.52 43.21
   vertex 18.20 -0.42 42.36
   vertex 18.38 -3.05 38.01
  endloop
 endfacet
 facet normal 1.00 -0.02 0.05
  outer loop
   vertex 19.01 -4.77 6.21
   vertex 19.30 -4.41 0.13
   vertex 19.11 0.55 6.61
  endloop
 endfacet
 facet normal 0.33 -0.38 0.86
  outer loop
   vertex 19.78 0.25 88.57
   vertex 18.53 -3.21 87.53
   vertex 19.38 -4.86 86.48
  endloop
 endfacet
 facet normal -0.72 -0.69 -0.09
  outer loop
   vertex 20.81 -5.34 36.22
   vertex 18.38 -3.05 38.01
   vertex 17.89 -1.75 31.72
  endloop
 endfacet
 facet normal -0.47 0.12 0.87
  outer loop
   vertex 19.64 4.31 87.94
   vertex 18.22 5.83 86.97
   vertex 19.78 0.25 88.57
  endloop
 endfacet
 facet normal 0.63 -0.07 0.78
  outer loop
   vertex 19.46 3.33 58.61
   vertex 18.15 -2.50 59.15
   vertex 20.67 -0.54 57.28
  endloop
 endfacet
 facet normal 0.73 -0.44 0.53
  outer loop
   vertex 20.67 -0.54 57.28
   vertex 18.15 -2.50 59.15
   vertex 18.66 -3.15 57.91
  endloop
 endfacet
 facet normal -0.75 -0.58 0.31
  outer loop
   vertex 18.53 -3.21 87.53
   vertex 19.45 -6.79 83.01
   vertex 19.38 -4.86 86.48
  endloop
 endfacet
 facet normal 0.98 -0.19 0.03
  outer loop
   vertex 19.01 -4.77 6.21
   vertex 18.35 -9.34 0.20
   vertex 19.30 -4.41 0.13
  endloop
 endfacet
 facet normal 0.84 0.53 -0.09
  outer loop
   vertex 18.00 5.61 3.97
   vertex 18.74 3.81 0.23
   vertex 15.98 8.19 0.20
  endloop
 endfacet
 facet normal -0.91 -0.37 0.19
  outer loop
   vertex 18.20 -0.42 42.36
   vertex 17.46 -0.51 38.61
   vertex 18.38 -3.05 38.01
  endloop
 endfacet
 facet normal 0.41 -0.07 -0.91
  outer loop
   vertex 19.81 4.08 29.79
   vertex 18.75 -0.34 29.66
   vertex 16.22 3.38 28.24
  endloop
 endfacet
 facet normal 0.62 0.14 0.77
  outer loop
   vertex 18.22 5.83 86.97
   vertex 15.47 -5.06 91.14
   vertex 18.49 -1.78 88.13
  endloop
 endfacet
 facet normal 0.55 -0.05 0.83
  outer loop
   vertex 19.46 3.33 58.61
   vertex 15.94 0.49 60.78
   vertex 18.15 -2.50 59.15
  endloop
 endfacet
 facet normal 0.37 -0.75 0.55
  outer loop
   vertex 18.15 -2.50 59.15
   vertex 16.52 -3.84 58.40
   vertex 18.66 -3.15 57.91
  endloop
 endfacet
 facet normal 0.49 -0.77 0.41
  outer loop
   vertex 17.89 -1.75 31.72
   vertex 17.07 -2.53 31.23
   vertex 19.02 -1.97 29.92
  endloop
 endfacet
 facet normal 0.71 -0.07 0.70
  outer loop
   vertex 19.11 0.55 6.61
   vertex 15.26 -5.01 10.00
   vertex 19.01 -4.77 6.21
  endloop
 endfacet
 facet normal 0.91 -0.38 0.19
  outer loop
   vertex 19.01 -4.77 6.21
   vertex 16.89 -9.62 6.67
   vertex 18.35 -9.34 0.20
  endloop
 endfacet
 facet normal 0.61 -0.66 0.44
  outer loop
   vertex 17.94 3.99 37.76
   vertex 16.93 2.01 36.18
   vertex 18.01 2.79 35.88
  endloop
 endfacet
 facet normal -0.14 0.08 0.99
  outer loop
   vertex 18.70 4.53 31.50
   vertex 16.29 2.09 31.35
   vertex 17.47 1.45 31.57
  endloop
 endfacet
 facet normal -0.05 0.42 0.91
  outer loop
   vertex 18.01 2.79 35.88
   vertex 16.93 2.01 36.18
   vertex 17.73 2.15 36.16
  endloop
 endfacet
 facet normal -0.01 -0.48 0.88
  outer loop
   vertex 18.15 -2.50 59.15
   vertex 15.94 0.49 60.78
   vertex 16.52 -3.84 58.40
  endloop
 endfacet
 facet normal 0.80 -0.22 0.57
  outer loop
   vertex 18.49 -1.78 88.13
   vertex 15.47 -5.06 91.14
   vertex 18.53 -3.21 87.53
  endloop
 endfacet
 facet normal 0.74 -0.11 0.66
  outer loop
   vertex 19.11 0.55 6.61
   vertex 16.35 -0.79 9.47
   vertex 15.26 -5.01 10.00
  endloop
 endfacet
 facet normal 0.70 -0.25 0.67
  outer loop
   vertex 19.01 -4.77 6.21
   vertex 15.26 -5.01 10.00
   vertex 15.17 -9.29 8.52
  endloop
 endfacet
 facet normal 0.79 -0.59 0.15
  outer loop
   vertex 16.89 -9.62 6.67
   vertex 16.62 -11.67 0.18
   vertex 18.35 -9.34 0.20
  endloop
 endfacet
 facet normal 0.84 0.42 0.35
  outer loop
   vertex 16.06 10.04 87.13
   vertex 18.22 5.83 86.97
   vertex 18.19 7.96 84.49
  endloop
 endfacet
 facet normal 0.76 0.42 0.50
  outer loop
   vertex 15.15 6.32 7.73
   vertex 19.11 0.55 6.61
   vertex 18.00 5.61 3.97
  endloop
 endfacet
 facet normal -0.32 -0.23 0.92
  outer loop
   vertex 17.47 -0.77 31.82
   vertex 17.07 -2.53 31.23
   vertex 17.89 -1.75 31.72
  endloop
 endfacet
 facet normal 0.42 -0.87 0.26
  outer loop
   vertex 17.07 -2.53 31.23
   vertex 16.95 -3.37 28.55
   vertex 19.02 -1.97 29.92
  endloop
 endfacet
 facet normal 0.54 0.03 -0.84
  outer loop
   vertex 19.02 -1.97 29.92
   vertex 16.95 -3.37 28.55
   vertex 15.24 -1.91 27.51
  endloop
 endfacet
 facet normal 0.69 -0.24 0.69
  outer loop
   vertex 15.17 -9.29 8.52
   vertex 16.89 -9.62 6.67
   vertex 19.01 -4.77 6.21
  endloop
 endfacet
 facet normal 0.93 -0.35 -0.16
  outer loop
   vertex 17.93 -5.99 72.36
   vertex 19.45 -6.79 83.01
   vertex 16.89 -9.27 73.44
  endloop
 endfacet
 facet normal 0.30 0.32 0.90
  outer loop
   vertex 19.46 3.33 58.61
   vertex 15.61 3.83 59.72
   vertex 15.94 0.49 60.78
  endloop
 endfacet
 facet normal 0.62 0.28 0.73
  outer loop
   vertex 19.11 0.55 6.61
   vertex 15.15 6.32 7.73
   vertex 16.35 -0.79 9.47
  endloop
 endfacet
 facet normal 0.76 -0.16 -0.63
  outer loop
   vertex 20.12 -4.30 73.94
   vertex 14.47 -7.07 67.83
   vertex 19.78 1.87 71.95
  endloop
 endfacet
 facet normal 0.33 -0.86 -0.39
  outer loop
   vertex 18.87 -2.53 51.93
   vertex 15.90 -3.74 52.11
   vertex 17.09 -2.77 50.96
  endloop
 endfacet
 facet normal 0.37 -0.93 -0.08
  outer loop
   vertex 18.66 -3.15 57.91
   vertex 15.90 -3.74 52.11
   vertex 18.87 -2.53 51.93
  endloop
 endfacet
 facet normal 0.72 -0.54 -0.42
  outer loop
   vertex 20.12 -4.30 73.94
   vertex 17.93 -5.99 72.36
   vertex 14.47 -7.07 67.83
  endloop
 endfacet
 facet normal 0.77 0.63 0.13
  outer loop
   vertex 11.40 16.58 83.07
   vertex 16.06 10.04 87.13
   vertex 18.19 7.96 84.49
  endloop
 endfacet
 facet normal 0.79 0.39 0.47
  outer loop
   vertex 15.11 9.98 88.77
   vertex 18.22 5.83 86.97
   vertex 16.06 10.04 87.13
  endloop
 endfacet
 facet normal 0.88 -0.04 0.48
  outer loop
   vertex 15.35 3.82 92.08
   vertex 15.47 -5.06 91.14
   vertex 18.22 5.83 86.97
  endloop
 endfacet
 facet normal 0.27 -0.85 -0.44
  outer loop
   vertex 15.90 -3.74 52.11
   vertex 16.50 -1.52 48.21
   vertex 17.09 -2.77 50.96
  endloop
 endfacet
 facet normal -0.71 -0.66 0.24
  outer loop
   vertex 16.95 -3.37 28.55
   vertex 17.07 -2.53 31.23
   vertex 15.24 -1.91 27.51
  endloop
 endfacet
 facet normal 0.83 -0.39 -0.40
  outer loop
   vertex 16.89 -9.27 73.44
   vertex 15.58 -10.03 71.48
   vertex 17.93 -5.99 72.36
  endloop
 endfacet
 facet normal 0.80 0.37 -0.47
  outer loop
   vertex 18.54 7.21 74.10
   vertex 19.78 1.87 71.95
   vertex 14.22 8.62 67.90
  endloop
 endfacet
 facet normal 0.97 0.25 0.08
  outer loop
   vertex 15.39 5.36 54.00
   vertex 16.56 2.63 48.23
   vertex 15.68 7.10 45.14
  endloop
 endfacet
 facet normal -0.11 0.89 -0.44
  outer loop
   vertex 15.39 5.36 54.00
   vertex 16.55 3.65 50.29
   vertex 16.56 2.63 48.23
  endloop
 endfacet
 facet normal 0.99 0.14 -0.07
  outer loop
   vertex 16.56 2.63 48.23
   vertex 16.72 0.23 45.64
   vertex 15.68 7.10 45.14
  endloop
 endfacet
 facet normal -0.18 0.28 0.94
  outer loop
   vertex 15.61 3.83 59.72
   vertex 13.19 1.84 59.86
   vertex 15.94 0.49 60.78
  endloop
 endfacet
 facet normal -0.49 -0.82 0.30
  outer loop
   vertex 16.29 2.09 31.35
   vertex 15.35 2.03 29.63
   vertex 17.47 1.45 31.57
  endloop
 endfacet
 facet normal -0.66 0.08 0.74
  outer loop
   vertex 17.47 1.45 31.57
   vertex 15.35 2.03 29.63
   vertex 17.47 -0.77 31.82
  endloop
 endfacet
 facet normal 0.69 -0.70 -0.19
  outer loop
   vertex 16.89 -9.27 73.44
   vertex 11.91 -13.35 70.39
   vertex 15.58 -10.03 71.48
  endloop
 endfacet
 facet normal 0.79 0.42 -0.45
  outer loop
   vertex 18.54 7.21 74.10
   vertex 14.22 8.62 67.90
   vertex 13.55 12.96 70.78
  endloop
 endfacet
 facet normal 0.70 0.58 0.42
  outer loop
   vertex 15.56 8.35 4.24
   vertex 15.15 6.32 7.73
   vertex 18.00 5.61 3.97
  endloop
 endfacet
 facet normal 0.93 0.36 0.10
  outer loop
   vertex 13.91 9.95 51.03
   vertex 15.39 5.36 54.00
   vertex 15.68 7.10 45.14
  endloop
 endfacet
 facet normal 0.98 0.14 -0.15
  outer loop
   vertex 16.72 0.23 45.64
   vertex 15.23 2.48 37.71
   vertex 15.68 7.10 45.14
  endloop
 endfacet
 facet normal 0.96 0.20 0.17
  outer loop
   vertex 12.17 0.67 31.81
   vertex 16.35 -0.79 9.47
   vertex 15.15 6.32 7.73
  endloop
 endfacet
 facet normal 0.98 0.01 -0.18
  outer loop
   vertex 16.72 0.23 45.64
   vertex 15.38 -1.56 38.27
   vertex 15.23 2.48 37.71
  endloop
 endfacet
 facet normal 0.02 -0.63 -0.77
  outer loop
   vertex 16.52 -3.84 58.40
   vertex 13.93 -3.61 58.14
   vertex 18.66 -3.15 57.91
  endloop
 endfacet
 facet normal 0.10 -0.99 0.05
  outer loop
   vertex 18.66 -3.15 57.91
   vertex 13.93 -3.61 58.14
   vertex 15.90 -3.74 52.11
  endloop
 endfacet
 facet normal 0.96 -0.26 -0.09
  outer loop
   vertex 16.50 -1.52 48.21
   vertex 14.15 -8.99 44.47
   vertex 16.72 0.23 45.64
  endloop
 endfacet
 facet normal 0.96 -0.29 -0.02
  outer loop
   vertex 16.50 -1.52 48.21
   vertex 15.90 -3.74 52.11
   vertex 14.15 -8.99 44.47
  endloop
 endfacet
 facet normal 0.79 -0.39 0.47
  outer loop
   vertex 18.53 -3.21 87.53
   vertex 15.47 -5.06 91.14
   vertex 19.45 -6.79 83.01
  endloop
 endfacet
 facet normal 0.78 -0.34 -0.52
  outer loop
   vertex 17.93 -5.99 72.36
   vertex 15.58 -10.03 71.48
   vertex 14.47 -7.07 67.83
  endloop
 endfacet
 facet normal 0.82 -0.57 -0.07
  outer loop
   vertex 19.45 -6.79 83.01
   vertex 14.09 -13.48 75.24
   vertex 16.89 -9.27 73.44
  endloop
 endfacet
 facet normal 0.79 -0.05 0.61
  outer loop
   vertex 15.35 3.82 92.08
   vertex 13.27 -2.78 94.19
   vertex 15.47 -5.06 91.14
  endloop
 endfacet
 facet normal 0.52 -0.03 0.85
  outer loop
   vertex 16.35 -0.79 9.47
   vertex 14.96 -3.20 10.24
   vertex 15.26 -5.01 10.00
  endloop
 endfacet
 facet normal 0.73 -0.68 0.08
  outer loop
   vertex 13.93 -12.26 86.65
   vertex 14.09 -13.48 75.24
   vertex 19.45 -6.79 83.01
  endloop
 endfacet
 facet normal -0.39 -0.20 0.90
  outer loop
   vertex 15.94 0.49 60.78
   vertex 13.19 1.84 59.86
   vertex 13.54 -2.80 58.99
  endloop
 endfacet
 facet normal 0.01 -0.48 0.88
  outer loop
   vertex 15.94 0.49 60.78
   vertex 13.54 -2.80 58.99
   vertex 16.52 -3.84 58.40
  endloop
 endfacet
 facet normal 0.67 -0.05 -0.74
  outer loop
   vertex 19.78 1.87 71.95
   vertex 14.47 -7.07 67.83
   vertex 9.23 3.47 62.37
  endloop
 endfacet
 facet normal 0.34 -0.07 0.94
  outer loop
   vertex 14.96 -3.20 10.24
   vertex 14.04 -4.14 10.50
   vertex 15.26 -5.01 10.00
  endloop
 endfacet
 facet normal 0.96 -0.25 -0.11
  outer loop
   vertex 16.72 0.23 45.64
   vertex 14.15 -8.99 44.47
   vertex 15.38 -1.56 38.27
  endloop
 endfacet
 facet normal 0.92 -0.38 0.05
  outer loop
   vertex 15.90 -3.74 52.11
   vertex 13.81 -8.82 52.21
   vertex 14.15 -8.99 44.47
  endloop
 endfacet
 facet normal 0.23 -0.32 0.92
  outer loop
   vertex 15.26 -5.01 10.00
   vertex 10.29 -9.63 9.64
   vertex 15.17 -9.29 8.52
  endloop
 endfacet
 facet normal 0.76 -0.45 0.47
  outer loop
   vertex 15.47 -5.06 91.14
   vertex 13.93 -12.26 86.65
   vertex 19.45 -6.79 83.01
  endloop
 endfacet
 facet normal 0.41 0.91 0.01
  outer loop
   vertex 12.94 9.56 0.15
   vertex 15.56 8.35 4.24
   vertex 15.98 8.19 0.20
  endloop
 endfacet
 facet normal 0.91 -0.02 -0.41
  outer loop
   vertex 15.23 2.48 37.71
   vertex 15.38 -1.56 38.27
   vertex 11.37 -2.58 29.40
  endloop
 endfacet
 facet normal -0.13 -0.75 0.65
  outer loop
   vertex 16.52 -3.84 58.40
   vertex 13.54 -2.80 58.99
   vertex 13.93 -3.61 58.14
  endloop
 endfacet
 facet normal 0.94 -0.29 -0.16
  outer loop
   vertex 15.38 -1.56 38.27
   vertex 14.15 -8.99 44.47
   vertex 13.35 -7.97 37.87
  endloop
 endfacet
 facet normal 0.89 -0.36 0.30
  outer loop
   vertex 13.93 -3.61 58.14
   vertex 13.81 -8.82 52.21
   vertex 15.90 -3.74 52.11
  endloop
 endfacet
 facet normal 0.40 -0.76 0.51
  outer loop
   vertex 16.89 -9.62 6.67
   vertex 15.17 -9.29 8.52
   vertex 12.21 -12.35 6.23
  endloop
 endfacet
 facet normal 0.71 -0.62 -0.34
  outer loop
   vertex 16.89 -9.27 73.44
   vertex 14.09 -13.48 75.24
   vertex 11.91 -13.35 70.39
  endloop
 endfacet
 facet normal 0.37 -0.89 0.27
  outer loop
   vertex 16.89 -9.62 6.67
   vertex 12.07 -13.56 0.11
   vertex 16.62 -11.67 0.18
  endloop
 endfacet
 facet normal 0.68 -0.72 0.09
  outer loop
   vertex 13.93 -12.26 86.65
   vertex 9.15 -17.53 80.47
   vertex 14.09 -13.48 75.24
  endloop
 endfacet
 facet normal 0.65 0.65 0.40
  outer loop
   vertex 16.06 10.04 87.13
   vertex 10.53 13.41 90.66
   vertex 15.11 9.98 88.77
  endloop
 endfacet
 facet normal 0.60 0.44 0.66
  outer loop
   vertex 9.34 8.19 95.26
   vertex 15.11 9.98 88.77
   vertex 10.53 13.41 90.66
  endloop
 endfacet
 facet normal 0.76 0.51 0.41
  outer loop
   vertex 12.49 5.31 59.51
   vertex 15.39 5.36 54.00
   vertex 13.91 9.95 51.03
  endloop
 endfacet
 facet normal 0.70 0.22 0.68
  outer loop
   vertex 15.11 9.98 88.77
   vertex 9.34 8.19 95.26
   vertex 18.22 5.83 86.97
  endloop
 endfacet
 facet normal 0.66 0.50 0.57
  outer loop
   vertex 15.35 3.82 92.08
   vertex 18.22 5.83 86.97
   vertex 9.34 8.19 95.26
  endloop
 endfacet
 facet normal -0.45 0.59 0.67
  outer loop
   vertex 15.61 3.83 59.72
   vertex 13.97 4.61 57.95
   vertex 13.19 1.84 59.86
  endloop
 endfacet
 facet normal 0.79 -0.59 0.19
  outer loop
   vertex 11.32 -3.43 22.47
   vertex 16.35 -0.79 9.47
   vertex 12.17 0.67 31.81
  endloop
 endfacet
 facet normal 0.87 -0.42 0.25
  outer loop
   vertex 11.32 -3.43 22.47
   vertex 14.96 -3.20 10.24
   vertex 16.35 -0.79 9.47
  endloop
 endfacet
 facet normal 0.63 -0.50 -0.59
  outer loop
   vertex 15.58 -10.03 71.48
   vertex 11.91 -13.35 70.39
   vertex 14.47 -7.07 67.83
  endloop
 endfacet
 facet normal 0.49 -0.86 0.16
  outer loop
   vertex 12.21 -12.35 6.23
   vertex 12.07 -13.56 0.11
   vertex 16.89 -9.62 6.67
  endloop
 endfacet
 facet normal 0.74 0.66 -0.11
  outer loop
   vertex 18.42 8.44 76.34
   vertex 13.55 12.96 70.78
   vertex 10.93 16.12 72.25
  endloop
 endfacet
 facet normal 0.83 0.56 -0.02
  outer loop
   vertex 13.91 9.95 51.03
   vertex 15.68 7.10 45.14
   vertex 11.78 13.01 47.59
  endloop
 endfacet
 facet normal 0.82 0.57 -0.07
  outer loop
   vertex 15.68 7.10 45.14
   vertex 13.24 10.02 39.97
   vertex 11.78 13.01 47.59
  endloop
 endfacet
 facet normal 0.38 0.89 0.26
  outer loop
   vertex 12.17 0.67 31.81
   vertex 15.15 6.32 7.73
   vertex 12.96 7.02 8.53
  endloop
 endfacet
 facet normal 0.72 -0.66 0.20
  outer loop
   vertex 11.32 -3.43 22.47
   vertex 14.04 -4.14 10.50
   vertex 14.96 -3.20 10.24
  endloop
 endfacet
 facet normal 0.89 -0.26 -0.37
  outer loop
   vertex 15.38 -1.56 38.27
   vertex 13.35 -7.97 37.87
   vertex 11.37 -2.58 29.40
  endloop
 endfacet
 facet normal 0.68 0.72 -0.15
  outer loop
   vertex 11.78 13.01 47.59
   vertex 13.24 10.02 39.97
   vertex 9.14 13.41 37.70
  endloop
 endfacet
 facet normal 0.83 0.35 -0.44
  outer loop
   vertex 13.24 10.02 39.97
   vertex 15.23 2.48 37.71
   vertex 9.34 6.54 29.76
  endloop
 endfacet
 facet normal 0.69 0.63 0.37
  outer loop
   vertex 12.49 5.31 59.51
   vertex 13.97 4.61 57.95
   vertex 15.39 5.36 54.00
  endloop
 endfacet
 facet normal 0.82 0.42 -0.39
  outer loop
   vertex 15.23 2.48 37.71
   vertex 11.73 3.63 31.66
   vertex 9.34 6.54 29.76
  endloop
 endfacet
 facet normal 0.94 0.32 0.12
  outer loop
   vertex 12.72 6.52 11.74
   vertex 12.17 0.67 31.81
   vertex 12.96 7.02 8.53
  endloop
 endfacet
 facet normal 0.99 0.15 0.07
  outer loop
   vertex 11.73 3.63 31.66
   vertex 12.17 0.67 31.81
   vertex 12.72 6.52 11.74
  endloop
 endfacet
 facet normal 0.87 0.11 -0.48
  outer loop
   vertex 15.23 2.48 37.71
   vertex 12.17 0.67 31.81
   vertex 11.73 3.63 31.66
  endloop
 endfacet
 facet normal 0.86 0.15 -0.49
  outer loop
   vertex 15.23 2.48 37.71
   vertex 11.37 -2.58 29.40
   vertex 12.17 0.67 31.81
  endloop
 endfacet
 facet normal 0.97 -0.26 0.02
  outer loop
   vertex 11.37 -2.58 29.40
   vertex 11.32 -3.43 22.47
   vertex 12.17 0.67 31.81
  endloop
 endfacet
 facet normal 0.69 -0.33 0.64
  outer loop
   vertex 13.54 -2.80 58.99
   vertex 12.16 -7.44 58.05
   vertex 13.93 -3.61 58.14
  endloop
 endfacet
 facet normal 0.85 -0.40 0.34
  outer loop
   vertex 12.16 -7.44 58.05
   vertex 13.81 -8.82 52.21
   vertex 13.93 -3.61 58.14
  endloop
 endfacet
 facet normal 0.79 -0.61 0.05
  outer loop
   vertex 13.81 -8.82 52.21
   vertex 10.98 -12.74 48.67
   vertex 14.15 -8.99 44.47
  endloop
 endfacet
 facet normal 0.54 0.14 0.83
  outer loop
   vertex 9.34 8.19 95.26
   vertex 5.89 5.28 98.02
   vertex 15.35 3.82 92.08
  endloop
 endfacet
 facet normal 0.75 0.21 0.62
  outer loop
   vertex 12.49 5.31 59.51
   vertex 13.19 1.84 59.86
   vertex 13.97 4.61 57.95
  endloop
 endfacet
 facet normal 0.52 -0.84 0.17
  outer loop
   vertex 14.04 -4.14 10.50
   vertex 11.32 -3.43 22.47
   vertex 8.38 -5.67 20.45
  endloop
 endfacet
 facet normal 0.19 -0.28 0.94
  outer loop
   vertex 15.26 -5.01 10.00
   vertex 14.04 -4.14 10.50
   vertex 10.29 -9.63 9.64
  endloop
 endfacet
 facet normal 0.57 -0.50 -0.65
  outer loop
   vertex 14.47 -7.07 67.83
   vertex 11.91 -13.35 70.39
   vertex 8.91 -13.34 67.77
  endloop
 endfacet
 facet normal 0.46 -0.86 -0.23
  outer loop
   vertex 14.09 -13.48 75.24
   vertex 9.15 -17.53 80.47
   vertex 11.91 -13.35 70.39
  endloop
 endfacet
 facet normal 0.73 0.54 0.42
  outer loop
   vertex 8.93 13.86 54.71
   vertex 12.49 5.31 59.51
   vertex 13.91 9.95 51.03
  endloop
 endfacet
 facet normal 0.77 -0.44 -0.46
  outer loop
   vertex 13.35 -7.97 37.87
   vertex 9.35 -9.24 32.36
   vertex 11.37 -2.58 29.40
  endloop
 endfacet
 facet normal 0.57 0.81 0.15
  outer loop
   vertex 10.41 5.14 28.48
   vertex 11.73 3.63 31.66
   vertex 12.72 6.52 11.74
  endloop
 endfacet
 facet normal 0.63 -0.75 -0.19
  outer loop
   vertex 10.98 -12.74 48.67
   vertex 13.35 -7.97 37.87
   vertex 14.15 -8.99 44.47
  endloop
 endfacet
 facet normal 0.49 -0.13 0.86
  outer loop
   vertex 9.23 3.47 62.37
   vertex 13.54 -2.80 58.99
   vertex 13.19 1.84 59.86
  endloop
 endfacet
 facet normal 0.53 -0.84 0.10
  outer loop
   vertex 9.13 -4.19 27.78
   vertex 11.32 -3.43 22.47
   vertex 11.37 -2.58 29.40
  endloop
 endfacet
 facet normal 0.04 -0.18 0.98
  outer loop
   vertex 14.04 -4.14 10.50
   vertex 7.42 -5.02 10.59
   vertex 10.29 -9.63 9.64
  endloop
 endfacet
 facet normal 0.60 -0.39 0.70
  outer loop
   vertex 15.47 -5.06 91.14
   vertex 9.05 -10.82 93.50
   vertex 11.18 -11.25 91.43
  endloop
 endfacet
 facet normal 0.67 -0.70 0.24
  outer loop
   vertex 7.76 -13.16 56.28
   vertex 10.98 -12.74 48.67
   vertex 13.81 -8.82 52.21
  endloop
 endfacet
 facet normal 0.72 -0.47 0.51
  outer loop
   vertex 15.47 -5.06 91.14
   vertex 11.18 -11.25 91.43
   vertex 13.93 -12.26 86.65
  endloop
 endfacet
 facet normal 0.49 0.03 0.87
  outer loop
   vertex 13.27 -2.78 94.19
   vertex 5.89 5.28 98.02
   vertex 7.34 -4.63 97.60
  endloop
 endfacet
 facet normal 0.13 -0.99 -0.08
  outer loop
   vertex 8.38 -5.67 20.45
   vertex 7.42 -5.02 10.59
   vertex 14.04 -4.14 10.50
  endloop
 endfacet
 facet normal 0.20 -0.71 0.68
  outer loop
   vertex 15.17 -9.29 8.52
   vertex 10.29 -9.63 9.64
   vertex 12.21 -12.35 6.23
  endloop
 endfacet
 facet normal 0.62 -0.77 0.18
  outer loop
   vertex 13.93 -12.26 86.65
   vertex 9.21 -15.77 87.96
   vertex 9.15 -17.53 80.47
  endloop
 endfacet
 facet normal 0.20 -0.79 0.58
  outer loop
   vertex 11.32 -3.43 22.47
   vertex 7.06 -3.99 23.19
   vertex 8.38 -5.67 20.45
  endloop
 endfacet
 facet normal 0.69 -0.64 0.34
  outer loop
   vertex 13.81 -8.82 52.21
   vertex 12.16 -7.44 58.05
   vertex 7.76 -13.16 56.28
  endloop
 endfacet
 facet normal 0.58 0.20 0.79
  outer loop
   vertex 12.49 5.31 59.51
   vertex 9.23 3.47 62.37
   vertex 13.19 1.84 59.86
  endloop
 endfacet
 facet normal 0.60 -0.02 0.80
  outer loop
   vertex 9.23 3.47 62.37
   vertex 8.71 -4.02 62.58
   vertex 13.54 -2.80 58.99
  endloop
 endfacet
 facet normal 0.11 -0.99 -0.09
  outer loop
   vertex 9.13 -4.19 27.78
   vertex 7.06 -3.99 23.19
   vertex 11.32 -3.43 22.47
  endloop
 endfacet
 facet normal 0.58 -0.34 0.75
  outer loop
   vertex 15.47 -5.06 91.14
   vertex 7.34 -4.63 97.60
   vertex 9.05 -10.82 93.50
  endloop
 endfacet
 facet normal 0.55 -0.43 0.72
  outer loop
   vertex 7.34 -4.63 97.60
   vertex 15.47 -5.06 91.14
   vertex 13.27 -2.78 94.19
  endloop
 endfacet
 facet normal 0.61 -0.63 0.48
  outer loop
   vertex 11.18 -11.25 91.43
   vertex 9.21 -15.77 87.96
   vertex 13.93 -12.26 86.65
  endloop
 endfacet
 facet normal -0.32 -0.95 -0.03
  outer loop
   vertex 5.44 -4.55 16.66
   vertex 7.42 -5.02 10.59
   vertex 8.38 -5.67 20.45
  endloop
 endfacet
 facet normal 0.52 -0.56 0.65
  outer loop
   vertex 9.05 -10.82 93.50
   vertex 7.42 -12.77 93.11
   vertex 11.18 -11.25 91.43
  endloop
 endfacet
 facet normal 0.59 -0.76 -0.26
  outer loop
   vertex 13.35 -7.97 37.87
   vertex 6.61 -11.39 32.43
   vertex 9.35 -9.24 32.36
  endloop
 endfacet
 facet normal 0.61 -0.73 -0.30
  outer loop
   vertex 7.08 -14.88 41.74
   vertex 6.61 -11.39 32.43
   vertex 13.35 -7.97 37.87
  endloop
 endfacet
 facet normal -0.13 -0.97 0.20
  outer loop
   vertex 7.19 -12.90 0.11
   vertex 12.07 -13.56 0.11
   vertex 12.21 -12.35 6.23
  endloop
 endfacet
 facet normal 0.68 -0.71 -0.16
  outer loop
   vertex 13.35 -7.97 37.87
   vertex 10.98 -12.74 48.67
   vertex 7.08 -14.88 41.74
  endloop
 endfacet
 facet normal 0.27 -0.94 0.22
  outer loop
   vertex 9.21 -15.77 87.96
   vertex 4.54 -16.54 90.43
   vertex 9.15 -17.53 80.47
  endloop
 endfacet
 facet normal 0.57 0.22 0.79
  outer loop
   vertex 12.49 5.31 59.51
   vertex 8.51 5.03 62.46
   vertex 9.23 3.47 62.37
  endloop
 endfacet
 facet normal 0.63 -0.47 -0.62
  outer loop
   vertex 11.37 -2.58 29.40
   vertex 9.35 -9.24 32.36
   vertex 7.41 -7.74 29.29
  endloop
 endfacet
 facet normal 0.69 0.54 0.47
  outer loop
   vertex 12.49 5.31 59.51
   vertex 7.52 13.06 57.90
   vertex 9.67 8.17 60.38
  endloop
 endfacet
 facet normal 0.55 0.30 0.78
  outer loop
   vertex 9.67 8.17 60.38
   vertex 8.00 5.87 62.43
   vertex 12.49 5.31 59.51
  endloop
 endfacet
 facet normal 0.54 0.35 0.77
  outer loop
   vertex 12.49 5.31 59.51
   vertex 8.00 5.87 62.43
   vertex 8.51 5.03 62.46
  endloop
 endfacet
 facet normal 0.90 0.42 -0.12
  outer loop
   vertex 8.51 5.03 62.46
   vertex 8.79 4.45 62.54
   vertex 9.23 3.47 62.37
  endloop
 endfacet
 facet normal 0.62 -0.33 0.72
  outer loop
   vertex 8.71 -4.02 62.58
   vertex 12.16 -7.44 58.05
   vertex 13.54 -2.80 58.99
  endloop
 endfacet
 facet normal 0.47 -0.57 0.67
  outer loop
   vertex 7.76 -13.16 56.28
   vertex 12.16 -7.44 58.05
   vertex 4.63 -13.71 58.03
  endloop
 endfacet
 facet normal 0.34 -0.85 -0.40
  outer loop
   vertex 11.91 -13.35 70.39
   vertex 2.01 -18.49 72.87
   vertex 8.91 -13.34 67.77
  endloop
 endfacet
 facet normal 0.60 0.53 -0.59
  outer loop
   vertex 6.17 9.88 29.54
   vertex 9.34 6.54 29.76
   vertex 6.45 6.00 26.34
  endloop
 endfacet
 facet normal 0.71 -0.54 -0.45
  outer loop
   vertex 11.37 -2.58 29.40
   vertex 7.41 -7.74 29.29
   vertex 9.13 -4.19 27.78
  endloop
 endfacet
 facet normal 0.34 -0.45 0.82
  outer loop
   vertex 7.34 -4.63 97.60
   vertex 7.42 -12.77 93.11
   vertex 9.05 -10.82 93.50
  endloop
 endfacet
 facet normal 0.43 -0.66 0.61
  outer loop
   vertex 11.18 -11.25 91.43
   vertex 4.54 -16.54 90.43
   vertex 9.21 -15.77 87.96
  endloop
 endfacet
 facet normal 0.44 0.40 0.80
  outer loop
   vertex 9.67 8.17 60.38
   vertex 5.10 8.89 62.54
   vertex 8.00 5.87 62.43
  endloop
 endfacet
 facet normal 0.99 0.04 0.16
  outer loop
   vertex 7.33 -3.87 99.15
   vertex 7.59 -7.36 98.53
   vertex 8.33 -12.81 95.38
  endloop
 endfacet
 facet normal 0.44 -0.53 0.73
  outer loop
   vertex 8.71 -4.02 62.58
   vertex 4.63 -13.71 58.03
   vertex 12.16 -7.44 58.05
  endloop
 endfacet
 facet normal -0.26 -0.82 0.51
  outer loop
   vertex 10.29 -9.63 9.64
   vertex 4.38 -10.70 4.87
   vertex 12.21 -12.35 6.23
  endloop
 endfacet
 facet normal -0.24 -0.93 0.28
  outer loop
   vertex 12.21 -12.35 6.23
   vertex 4.38 -10.70 4.87
   vertex 7.19 -12.90 0.11
  endloop
 endfacet
 facet normal 0.90 -0.24 -0.37
  outer loop
   vertex 8.33 -12.81 95.38
   vertex 5.49 -18.55 92.12
   vertex 7.42 -12.77 93.11
  endloop
 endfacet
 facet normal 0.50 -0.72 0.48
  outer loop
   vertex 11.18 -11.25 91.43
   vertex 7.42 -12.77 93.11
   vertex 4.54 -16.54 90.43
  endloop
 endfacet
 facet normal 0.39 0.56 0.73
  outer loop
   vertex 10.53 13.41 90.66
   vertex 3.45 14.23 93.81
   vertex 9.34 8.19 95.26
  endloop
 endfacet
 facet normal 0.80 0.14 -0.59
  outer loop
   vertex 7.22 2.42 99.14
   vertex 7.34 -4.63 97.60
   vertex 5.89 5.28 98.02
  endloop
 endfacet
 facet normal 1.00 0.02 0.00
  outer loop
   vertex 7.22 2.42 99.14
   vertex 7.33 -3.87 99.15
   vertex 7.34 -4.63 97.60
  endloop
 endfacet
 facet normal 0.99 0.14 -0.06
  outer loop
   vertex 7.33 -3.87 99.15
   vertex 8.33 -12.81 95.38
   vertex 7.34 -4.63 97.60
  endloop
 endfacet
 facet normal 0.91 0.21 -0.36
  outer loop
   vertex 8.33 -12.81 95.38
   vertex 7.42 -12.77 93.11
   vertex 7.34 -4.63 97.60
  endloop
 endfacet
 facet normal 0.48 -0.63 -0.61
  outer loop
   vertex 6.61 -11.39 32.43
   vertex 7.41 -7.74 29.29
   vertex 9.35 -9.24 32.36
  endloop
 endfacet
 facet normal 0.77 -0.15 -0.62
  outer loop
   vertex 5.49 -18.55 92.12
   vertex 4.54 -16.54 90.43
   vertex 7.42 -12.77 93.11
  endloop
 endfacet
 facet normal 0.42 0.59 0.69
  outer loop
   vertex 9.67 8.17 60.38
   vertex 4.47 14.69 57.92
   vertex 5.10 8.89 62.54
  endloop
 endfacet
 facet normal -0.36 -0.40 0.84
  outer loop
   vertex 7.42 -5.02 10.59
   vertex 3.08 -6.57 8.03
   vertex 10.29 -9.63 9.64
  endloop
 endfacet
 facet normal 0.69 -0.52 0.50
  outer loop
   vertex 8.71 -4.02 62.58
   vertex 5.18 -8.44 62.81
   vertex 4.63 -13.71 58.03
  endloop
 endfacet
 facet normal 0.21 -0.56 0.80
  outer loop
   vertex 8.33 -12.81 95.38
   vertex -0.40 -15.90 95.49
   vertex 5.49 -18.55 92.12
  endloop
 endfacet
 facet normal 0.29 0.53 0.80
  outer loop
   vertex 7.52 13.06 57.90
   vertex 4.47 14.69 57.92
   vertex 9.67 8.17 60.38
  endloop
 endfacet
 facet normal 0.27 0.47 0.84
  outer loop
   vertex 9.34 8.19 95.26
   vertex 3.45 14.23 93.81
   vertex 5.89 5.28 98.02
  endloop
 endfacet
 facet normal 0.33 0.77 0.55
  outer loop
   vertex 1.24 17.51 90.53
   vertex 3.45 14.23 93.81
   vertex 10.53 13.41 90.66
  endloop
 endfacet
 facet normal -0.44 -0.90 -0.07
  outer loop
   vertex 5.44 -4.55 16.66
   vertex 5.03 -3.78 9.66
   vertex 7.42 -5.02 10.59
  endloop
 endfacet
 facet normal 0.04 -0.17 0.98
  outer loop
   vertex 7.33 -3.87 99.15
   vertex -0.71 -9.55 98.52
   vertex 7.59 -7.36 98.53
  endloop
 endfacet
 facet normal 0.43 -0.89 0.13
  outer loop
   vertex 7.76 -13.16 56.28
   vertex 1.55 -16.68 52.71
   vertex 10.98 -12.74 48.67
  endloop
 endfacet
 facet normal -0.11 0.00 0.99
  outer loop
   vertex 7.22 2.42 99.14
   vertex 5.28 6.14 98.93
   vertex 7.33 -3.87 99.15
  endloop
 endfacet
 facet normal 0.01 -0.85 0.53
  outer loop
   vertex 7.06 -3.99 23.19
   vertex 3.98 -2.59 25.51
   vertex 8.38 -5.67 20.45
  endloop
 endfacet
 facet normal -0.44 -0.20 0.87
  outer loop
   vertex 5.03 -3.78 9.66
   vertex 3.08 -6.57 8.03
   vertex 7.42 -5.02 10.59
  endloop
 endfacet
 facet normal -0.20 -0.87 0.45
  outer loop
   vertex 4.44 -9.22 7.78
   vertex 4.38 -10.70 4.87
   vertex 10.29 -9.63 9.64
  endloop
 endfacet
 facet normal 0.13 -0.48 0.87
  outer loop
   vertex 7.59 -7.36 98.53
   vertex -0.71 -9.55 98.52
   vertex 8.33 -12.81 95.38
  endloop
 endfacet
 facet normal 0.33 -0.89 0.31
  outer loop
   vertex 7.76 -13.16 56.28
   vertex 4.63 -13.71 58.03
   vertex 1.55 -16.68 52.71
  endloop
 endfacet
 facet normal 0.42 -0.90 0.10
  outer loop
   vertex 10.98 -12.74 48.67
   vertex 1.55 -16.68 52.71
   vertex 2.07 -16.61 51.15
  endloop
 endfacet
 facet normal 0.41 -0.91 0.05
  outer loop
   vertex 10.98 -12.74 48.67
   vertex 2.07 -16.61 51.15
   vertex 7.08 -14.88 41.74
  endloop
 endfacet
 facet normal 0.25 -0.83 -0.50
  outer loop
   vertex 2.01 -18.49 72.87
   vertex 2.12 -14.63 66.51
   vertex 8.91 -13.34 67.77
  endloop
 endfacet
 facet normal 0.39 -0.88 -0.26
  outer loop
   vertex 9.15 -17.53 80.47
   vertex 2.01 -18.49 72.87
   vertex 11.91 -13.35 70.39
  endloop
 endfacet
 facet normal -0.48 -0.87 0.11
  outer loop
   vertex 8.38 -5.67 20.45
   vertex 3.98 -2.59 25.51
   vertex 5.44 -4.55 16.66
  endloop
 endfacet
 facet normal 0.27 -0.37 -0.89
  outer loop
   vertex 9.13 -4.19 27.78
   vertex 4.25 -8.01 27.88
   vertex 3.98 -2.59 25.51
  endloop
 endfacet
 facet normal 0.25 -0.59 -0.77
  outer loop
   vertex 5.18 -8.44 62.81
   vertex 8.91 -13.34 67.77
   vertex 2.12 -14.63 66.51
  endloop
 endfacet
 facet normal 0.33 0.61 0.72
  outer loop
   vertex 4.47 14.69 57.92
   vertex 2.02 10.41 62.69
   vertex 5.10 8.89 62.54
  endloop
 endfacet
 facet normal -0.31 -0.24 0.92
  outer loop
   vertex 3.08 -6.57 8.03
   vertex 4.44 -9.22 7.78
   vertex 10.29 -9.63 9.64
  endloop
 endfacet
 facet normal -0.83 -0.56 -0.01
  outer loop
   vertex 3.98 -2.59 25.51
   vertex 5.03 -3.78 9.66
   vertex 5.44 -4.55 16.66
  endloop
 endfacet
 facet normal -0.53 -0.84 0.07
  outer loop
   vertex 4.38 -10.70 4.87
   vertex 3.71 -10.68 0.19
   vertex 7.19 -12.90 0.11
  endloop
 endfacet
 facet normal -0.70 -0.63 0.34
  outer loop
   vertex 4.44 -9.22 7.78
   vertex 3.13 -9.26 5.00
   vertex 4.38 -10.70 4.87
  endloop
 endfacet
 facet normal 0.34 -0.66 -0.68
  outer loop
   vertex 6.61 -11.39 32.43
   vertex 1.59 -10.60 29.18
   vertex 7.41 -7.74 29.29
  endloop
 endfacet
 facet normal 0.17 0.46 0.87
  outer loop
   vertex 3.45 14.23 93.81
   vertex -1.73 7.66 98.23
   vertex 5.89 5.28 98.02
  endloop
 endfacet
 facet normal -0.61 -0.04 0.79
  outer loop
   vertex 5.03 -3.78 9.66
   vertex 3.05 2.00 8.46
   vertex 3.08 -6.57 8.03
  endloop
 endfacet
 facet normal -0.81 -0.45 0.39
  outer loop
   vertex 3.08 -6.57 8.03
   vertex 3.13 -9.26 5.00
   vertex 4.44 -9.22 7.78
  endloop
 endfacet
 facet normal 0.35 -0.68 -0.64
  outer loop
   vertex 7.41 -7.74 29.29
   vertex 1.59 -10.60 29.18
   vertex 4.25 -8.01 27.88
  endloop
 endfacet
 facet normal 0.16 -0.42 0.89
  outer loop
   vertex 8.33 -12.81 95.38
   vertex -0.71 -9.55 98.52
   vertex -0.40 -15.90 95.49
  endloop
 endfacet
 facet normal 0.26 -0.90 -0.35
  outer loop
   vertex 7.08 -14.88 41.74
   vertex -0.48 -14.23 34.37
   vertex 6.61 -11.39 32.43
  endloop
 endfacet
 facet normal 0.23 -0.92 -0.32
  outer loop
   vertex -0.49 -16.23 40.16
   vertex -0.48 -14.23 34.37
   vertex 7.08 -14.88 41.74
  endloop
 endfacet
 facet normal 0.08 -0.99 -0.14
  outer loop
   vertex 2.07 -16.61 51.15
   vertex -1.98 -16.83 50.25
   vertex 7.08 -14.88 41.74
  endloop
 endfacet
 facet normal 0.19 0.76 -0.62
  outer loop
   vertex 3.91 18.32 70.74
   vertex 5.72 14.33 66.35
   vertex 1.37 15.37 66.30
  endloop
 endfacet
 facet normal 0.09 0.72 0.69
  outer loop
   vertex 4.47 14.69 57.92
   vertex -2.04 15.54 57.89
   vertex 2.02 10.41 62.69
  endloop
 endfacet
 facet normal -0.75 -0.66 0.11
  outer loop
   vertex 4.38 -10.70 4.87
   vertex 3.13 -9.26 5.00
   vertex 3.71 -10.68 0.19
  endloop
 endfacet
 facet normal 0.12 -0.67 0.73
  outer loop
   vertex 4.63 -13.71 58.03
   vertex 5.18 -8.44 62.81
   vertex -0.44 -14.78 57.91
  endloop
 endfacet
 facet normal 0.18 -0.98 -0.03
  outer loop
   vertex -1.98 -16.83 50.25
   vertex -0.49 -16.23 40.16
   vertex 7.08 -14.88 41.74
  endloop
 endfacet
 facet normal 0.04 0.54 0.84
  outer loop
   vertex 3.45 14.23 93.81
   vertex -2.15 14.69 93.77
   vertex -1.73 7.66 98.23
  endloop
 endfacet
 facet normal 0.20 -0.84 -0.51
  outer loop
   vertex -0.48 -14.23 34.37
   vertex 1.59 -10.60 29.18
   vertex 6.61 -11.39 32.43
  endloop
 endfacet
 facet normal 0.18 -0.90 0.40
  outer loop
   vertex 4.63 -13.71 58.03
   vertex -0.44 -14.78 57.91
   vertex 1.55 -16.68 52.71
  endloop
 endfacet
 facet normal 0.14 -0.98 0.16
  outer loop
   vertex 4.54 -16.54 90.43
   vertex -0.42 -17.31 90.18
   vertex 9.15 -17.53 80.47
  endloop
 endfacet
 facet normal 0.05 0.72 0.69
  outer loop
   vertex 3.45 14.23 93.81
   vertex 1.24 17.51 90.53
   vertex -2.15 14.69 93.77
  endloop
 endfacet
 facet normal 0.31 -0.74 0.60
  outer loop
   vertex 5.18 -8.44 62.81
   vertex 1.41 -9.92 62.96
   vertex -0.44 -14.78 57.91
  endloop
 endfacet
 facet normal 0.69 0.64 -0.34
  outer loop
   vertex 1.83 -16.79 51.03
   vertex 2.77 -19.64 47.53
   vertex 1.56 -18.21 47.79
  endloop
 endfacet
 facet normal 0.03 -0.76 0.65
  outer loop
   vertex -0.40 -15.90 95.49
   vertex -5.05 -19.03 92.04
   vertex 5.49 -18.55 92.12
  endloop
 endfacet
 facet normal 0.83 -0.31 0.47
  outer loop
   vertex 1.83 -16.79 51.03
   vertex 0.75 -18.84 51.61
   vertex 2.77 -19.64 47.53
  endloop
 endfacet
 facet normal -0.18 -0.41 0.90
  outer loop
   vertex 2.07 -16.61 51.15
   vertex 1.59 -16.58 51.07
   vertex -1.98 -16.83 50.25
  endloop
 endfacet
 facet normal 0.57 -0.81 0.15
  outer loop
   vertex 1.55 -16.68 52.71
   vertex 1.83 -16.79 51.03
   vertex 2.07 -16.61 51.15
  endloop
 endfacet
 facet normal 0.89 -0.42 0.18
  outer loop
   vertex 1.83 -16.79 51.03
   vertex 1.55 -16.68 52.71
   vertex 0.75 -18.84 51.61
  endloop
 endfacet
 facet normal -0.30 -0.41 0.86
  outer loop
   vertex 1.56 -18.21 47.79
   vertex 0.85 -18.52 47.39
   vertex 2.77 -19.64 47.53
  endloop
 endfacet
 facet normal 0.04 -0.85 -0.52
  outer loop
   vertex 2.01 -18.49 72.87
   vertex -2.39 -15.22 67.10
   vertex 2.12 -14.63 66.51
  endloop
 endfacet
 facet normal 0.13 -0.99 0.08
  outer loop
   vertex 2.77 -19.64 47.53
   vertex -0.63 -20.17 46.23
   vertex 2.32 -19.76 46.71
  endloop
 endfacet
 facet normal 0.00 -0.99 0.13
  outer loop
   vertex 9.15 -17.53 80.47
   vertex -2.60 -18.49 72.85
   vertex 2.01 -18.49 72.87
  endloop
 endfacet
 facet normal -0.28 -0.37 0.89
  outer loop
   vertex 2.77 -19.64 47.53
   vertex 0.85 -18.52 47.39
   vertex -0.63 -20.17 46.23
  endloop
 endfacet
 facet normal -0.02 0.68 0.74
  outer loop
   vertex 2.02 10.41 62.69
   vertex -2.04 15.54 57.89
   vertex -3.30 10.28 62.69
  endloop
 endfacet
 facet normal 0.03 -0.40 -0.92
  outer loop
   vertex 4.25 -8.01 27.88
   vertex -3.63 -8.61 27.84
   vertex 3.98 -2.59 25.51
  endloop
 endfacet
 facet normal 0.04 -0.48 -0.87
  outer loop
   vertex 1.59 -10.60 29.18
   vertex -3.63 -8.61 27.84
   vertex 4.25 -8.01 27.88
  endloop
 endfacet
 facet normal 0.06 0.72 0.69
  outer loop
   vertex 1.24 17.51 90.53
   vertex -2.27 16.05 92.35
   vertex -2.15 14.69 93.77
  endloop
 endfacet
 facet normal 0.07 -0.93 0.37
  outer loop
   vertex -0.44 -14.78 57.91
   vertex -2.34 -16.42 54.14
   vertex 1.55 -16.68 52.71
  endloop
 endfacet
 facet normal -0.07 -1.00 0.00
  outer loop
   vertex -2.34 -16.42 54.14
   vertex -1.62 -16.48 52.63
   vertex 1.53 -16.71 51.99
  endloop
 endfacet
 facet normal 0.10 -0.99 -0.13
  outer loop
   vertex 1.53 -16.71 51.99
   vertex -1.98 -16.83 50.25
   vertex 1.59 -16.58 51.07
  endloop
 endfacet
 facet normal 0.21 -0.68 0.70
  outer loop
   vertex 0.85 -18.52 47.39
   vertex -2.50 -18.07 48.82
   vertex -0.63 -20.17 46.23
  endloop
 endfacet
 facet normal 0.08 -0.99 0.10
  outer loop
   vertex -0.42 -17.31 90.18
   vertex -6.10 -18.81 79.30
   vertex 9.15 -17.53 80.47
  endloop
 endfacet
 facet normal 0.09 -0.74 0.67
  outer loop
   vertex -2.50 -18.07 48.82
   vertex -2.38 -19.98 46.68
   vertex -0.63 -20.17 46.23
  endloop
 endfacet
 facet normal -0.02 -0.15 0.99
  outer loop
   vertex 0.45 7.94 99.10
   vertex -2.98 7.58 98.98
   vertex 5.28 6.14 98.93
  endloop
 endfacet
 facet normal 0.05 0.23 0.97
  outer loop
   vertex -2.98 7.58 98.98
   vertex -3.91 3.43 100.00
   vertex 5.28 6.14 98.93
  endloop
 endfacet
 facet normal 0.10 0.04 0.99
  outer loop
   vertex 5.28 6.14 98.93
   vertex -3.91 3.43 100.00
   vertex 7.33 -3.87 99.15
  endloop
 endfacet
 facet normal -0.22 -0.66 0.72
  outer loop
   vertex 1.41 -9.92 62.96
   vertex -7.43 -7.32 62.69
   vertex -0.44 -14.78 57.91
  endloop
 endfacet
 facet normal -0.04 -0.99 0.15
  outer loop
   vertex -1.62 -16.48 52.63
   vertex -1.98 -16.83 50.25
   vertex 1.53 -16.71 51.99
  endloop
 endfacet
 facet normal 0.00 -0.12 0.99
  outer loop
   vertex 7.33 -3.87 99.15
   vertex -7.84 -1.66 99.47
   vertex -0.71 -9.55 98.52
  endloop
 endfacet
 facet normal 0.23 -0.96 0.15
  outer loop
   vertex -2.34 -16.42 54.14
   vertex -2.29 -16.60 52.89
   vertex -1.62 -16.48 52.63
  endloop
 endfacet
 facet normal 0.00 -0.87 -0.49
  outer loop
   vertex -2.60 -18.49 72.85
   vertex -2.39 -15.22 67.10
   vertex 2.01 -18.49 72.87
  endloop
 endfacet
 facet normal 0.37 -0.11 0.92
  outer loop
   vertex -1.62 -16.48 52.63
   vertex -2.29 -16.60 52.89
   vertex -1.89 -18.33 52.52
  endloop
 endfacet
 facet normal 0.98 -0.14 -0.13
  outer loop
   vertex -1.62 -16.48 52.63
   vertex -1.89 -18.33 52.52
   vertex -1.98 -16.83 50.25
  endloop
 endfacet
 facet normal 1.00 0.07 0.03
  outer loop
   vertex -2.34 2.52 4.65
   vertex -1.83 -4.74 4.51
   vertex -1.88 -2.03 0.05
  endloop
 endfacet
 facet normal 0.93 0.06 0.38
  outer loop
   vertex -3.17 -5.01 7.87
   vertex -1.83 -4.74 4.51
   vertex -2.34 2.52 4.65
  endloop
 endfacet
 facet normal 0.99 -0.11 -0.08
  outer loop
   vertex -1.83 -4.74 4.51
   vertex -2.47 -7.15 0.06
   vertex -1.88 -2.03 0.05
  endloop
 endfacet
 facet normal 0.96 -0.20 -0.17
  outer loop
   vertex -1.89 -18.33 52.52
   vertex -2.50 -18.07 48.82
   vertex -1.98 -16.83 50.25
  endloop
 endfacet
 facet normal -0.04 0.25 0.97
  outer loop
   vertex -2.98 7.58 98.98
   vertex -4.39 7.10 99.05
   vertex -3.91 3.43 100.00
  endloop
 endfacet
 facet normal 0.94 0.28 -0.18
  outer loop
   vertex -2.34 2.52 4.65
   vertex -1.88 -2.03 0.05
   vertex -4.42 6.78 0.28
  endloop
 endfacet
 facet normal 0.00 -0.11 0.99
  outer loop
   vertex -3.91 3.43 100.00
   vertex -7.84 -1.66 99.47
   vertex 7.33 -3.87 99.15
  endloop
 endfacet
 facet normal 0.92 -0.37 0.07
  outer loop
   vertex -1.83 -4.74 4.51
   vertex -3.68 -9.48 3.64
   vertex -2.47 -7.15 0.06
  endloop
 endfacet
 facet normal -0.19 -0.81 0.55
  outer loop
   vertex -0.44 -14.78 57.91
   vertex -5.31 -14.67 56.33
   vertex -1.62 -15.60 56.27
  endloop
 endfacet
 facet normal 0.53 0.64 -0.56
  outer loop
   vertex -2.45 -17.49 49.52
   vertex -2.50 -18.07 48.82
   vertex -2.78 -17.54 49.15
  endloop
 endfacet
 facet normal 0.92 -0.34 -0.17
  outer loop
   vertex -1.89 -18.33 52.52
   vertex -2.93 -19.65 49.60
   vertex -2.50 -18.07 48.82
  endloop
 endfacet
 facet normal 0.97 -0.17 0.20
  outer loop
   vertex -2.50 -18.07 48.82
   vertex -2.93 -19.65 49.60
   vertex -2.38 -19.98 46.68
  endloop
 endfacet
 facet normal 0.05 -0.99 0.12
  outer loop
   vertex -2.93 -19.65 49.60
   vertex -3.00 -19.92 47.43
   vertex -2.38 -19.98 46.68
  endloop
 endfacet
 facet normal 0.90 0.44 0.01
  outer loop
   vertex -4.41 6.70 4.63
   vertex -2.34 2.52 4.65
   vertex -4.42 6.78 0.28
  endloop
 endfacet
 facet normal 0.95 0.03 0.32
  outer loop
   vertex -3.65 0.74 8.66
   vertex -3.17 -5.01 7.87
   vertex -2.34 2.52 4.65
  endloop
 endfacet
 facet normal 0.86 -0.40 0.32
  outer loop
   vertex -3.17 -5.01 7.87
   vertex -5.11 -9.21 7.80
   vertex -3.68 -9.48 3.64
  endloop
 endfacet
 facet normal 0.86 -0.40 0.31
  outer loop
   vertex -3.17 -5.01 7.87
   vertex -3.68 -9.48 3.64
   vertex -1.83 -4.74 4.51
  endloop
 endfacet
 facet normal 0.88 -0.48 -0.02
  outer loop
   vertex -3.68 -9.48 3.64
   vertex -4.36 -10.61 0.00
   vertex -2.47 -7.15 0.06
  endloop
 endfacet
 facet normal -0.20 -0.77 -0.61
  outer loop
   vertex -0.48 -14.23 34.37
   vertex -7.96 -12.04 34.02
   vertex 1.59 -10.60 29.18
  endloop
 endfacet
 facet normal -0.15 -0.98 0.13
  outer loop
   vertex -2.34 -16.42 54.14
   vertex -2.58 -16.92 50.22
   vertex -2.29 -16.60 52.89
  endloop
 endfacet
 facet normal 0.81 0.40 0.44
  outer loop
   vertex -5.83 5.66 8.21
   vertex -2.34 2.52 4.65
   vertex -4.41 6.70 4.63
  endloop
 endfacet
 facet normal -0.05 -0.51 -0.86
  outer loop
   vertex -2.39 -15.22 67.10
   vertex -7.43 -7.32 62.69
   vertex 2.12 -14.63 66.51
  endloop
 endfacet
 facet normal -0.25 -0.91 -0.32
  outer loop
   vertex -0.49 -16.23 40.16
   vertex -7.96 -12.04 34.02
   vertex -0.48 -14.23 34.37
  endloop
 endfacet
 facet normal -0.34 -0.93 0.14
  outer loop
   vertex -2.34 -16.42 54.14
   vertex -5.37 -15.24 54.69
   vertex -2.58 -16.92 50.22
  endloop
 endfacet
 facet normal 0.81 0.40 0.44
  outer loop
   vertex -5.83 5.66 8.21
   vertex -3.65 0.74 8.66
   vertex -2.34 2.52 4.65
  endloop
 endfacet
 facet normal -0.22 -0.91 -0.35
  outer loop
   vertex -0.49 -16.23 40.16
   vertex -5.58 -15.84 42.39
   vertex -7.96 -12.04 34.02
  endloop
 endfacet
 facet normal -0.28 -0.74 -0.62
  outer loop
   vertex -2.39 -15.22 67.10
   vertex -4.93 -16.80 70.13
   vertex -9.83 -15.05 70.23
  endloop
 endfacet
 facet normal 0.91 0.40 -0.06
  outer loop
   vertex -3.25 2.37 25.40
   vertex -3.65 0.74 8.66
   vertex -5.83 5.66 8.21
  endloop
 endfacet
 facet normal 0.96 -0.28 0.00
  outer loop
   vertex -3.25 2.37 25.40
   vertex -4.70 -2.57 25.36
   vertex -3.65 0.74 8.66
  endloop
 endfacet
 facet normal 0.54 -0.07 0.84
  outer loop
   vertex -3.65 0.74 8.66
   vertex -5.64 -3.66 9.59
   vertex -3.17 -5.01 7.87
  endloop
 endfacet
 facet normal 0.47 -0.23 0.85
  outer loop
   vertex -3.17 -5.01 7.87
   vertex -5.64 -3.66 9.59
   vertex -5.11 -9.21 7.80
  endloop
 endfacet
 facet normal -0.15 -0.43 0.89
  outer loop
   vertex -0.71 -9.55 98.52
   vertex -8.96 -12.01 95.91
   vertex -0.40 -15.90 95.49
  endloop
 endfacet
 facet normal -0.22 -0.92 0.33
  outer loop
   vertex -5.31 -14.67 56.33
   vertex -5.37 -15.24 54.69
   vertex -1.62 -15.60 56.27
  endloop
 endfacet
 facet normal -0.26 -0.87 0.42
  outer loop
   vertex -1.62 -15.60 56.27
   vertex -5.37 -15.24 54.69
   vertex -2.34 -16.42 54.14
  endloop
 endfacet
 facet normal -0.11 -0.99 -0.07
  outer loop
   vertex -1.98 -16.83 50.25
   vertex -5.58 -15.84 42.39
   vertex -0.49 -16.23 40.16
  endloop
 endfacet
 facet normal 0.87 0.50 -0.03
  outer loop
   vertex -4.89 5.24 25.72
   vertex -3.25 2.37 25.40
   vertex -5.83 5.66 8.21
  endloop
 endfacet
 facet normal 0.91 -0.42 -0.03
  outer loop
   vertex -4.70 -2.57 25.36
   vertex -5.64 -3.66 9.59
   vertex -3.65 0.74 8.66
  endloop
 endfacet
 facet normal 0.41 -0.89 0.20
  outer loop
   vertex -3.68 -9.48 3.64
   vertex -5.11 -9.21 7.80
   vertex -4.36 -10.61 0.00
  endloop
 endfacet
 facet normal -0.13 -0.85 -0.50
  outer loop
   vertex 1.59 -10.60 29.18
   vertex -7.96 -12.04 34.02
   vertex -5.36 -9.63 29.27
  endloop
 endfacet
 facet normal -0.20 -0.65 0.73
  outer loop
   vertex -7.43 -7.32 62.69
   vertex -7.95 -12.32 58.07
   vertex -0.44 -14.78 57.91
  endloop
 endfacet
 facet normal -0.22 -0.73 0.65
  outer loop
   vertex -0.44 -14.78 57.91
   vertex -7.95 -12.32 58.07
   vertex -5.31 -14.67 56.33
  endloop
 endfacet
 facet normal -0.12 0.90 -0.41
  outer loop
   vertex -2.58 -16.92 50.22
   vertex -5.37 -15.24 54.69
   vertex -1.98 -16.83 50.25
  endloop
 endfacet
 facet normal -0.05 -0.87 -0.50
  outer loop
   vertex -2.39 -15.22 67.10
   vertex -2.60 -18.49 72.85
   vertex -4.93 -16.80 70.13
  endloop
 endfacet
 facet normal -0.24 0.94 0.26
  outer loop
   vertex -0.50 19.72 85.66
   vertex -6.85 19.38 81.09
   vertex -6.89 17.20 88.92
  endloop
 endfacet
 facet normal -0.26 0.21 0.94
  outer loop
   vertex -3.91 3.43 100.00
   vertex -4.39 7.10 99.05
   vertex -7.83 2.62 99.10
  endloop
 endfacet
 facet normal 0.81 -0.59 -0.01
  outer loop
   vertex -4.70 -2.57 25.36
   vertex -6.33 -4.71 17.19
   vertex -5.64 -3.66 9.59
  endloop
 endfacet
 facet normal -0.37 -0.93 0.05
  outer loop
   vertex -5.37 -15.24 54.69
   vertex -5.58 -15.84 42.39
   vertex -1.98 -16.83 50.25
  endloop
 endfacet
 facet normal -0.67 -0.73 -0.15
  outer loop
   vertex -4.81 3.04 24.13
   vertex -6.86 5.01 23.63
   vertex -5.04 3.35 23.67
  endloop
 endfacet
 facet normal -0.10 -0.21 0.97
  outer loop
   vertex -7.84 -1.66 99.47
   vertex -8.63 -7.67 98.10
   vertex -0.71 -9.55 98.52
  endloop
 endfacet
 facet normal -0.43 -0.80 0.42
  outer loop
   vertex -7.95 -12.32 58.07
   vertex -8.25 -13.82 54.92
   vertex -5.31 -14.67 56.33
  endloop
 endfacet
 facet normal -0.20 -0.95 0.23
  outer loop
   vertex -6.55 -15.83 90.85
   vertex -10.00 -16.18 86.29
   vertex -0.42 -17.31 90.18
  endloop
 endfacet
 facet normal -0.21 -0.95 0.24
  outer loop
   vertex -0.42 -17.31 90.18
   vertex -10.00 -16.18 86.29
   vertex -6.10 -18.81 79.30
  endloop
 endfacet
 facet normal -0.39 -0.84 -0.36
  outer loop
   vertex -5.05 -19.03 92.04
   vertex -6.52 -18.38 92.11
   vertex -6.32 -18.30 91.72
  endloop
 endfacet
 facet normal -0.44 -0.47 0.77
  outer loop
   vertex -5.04 3.35 23.67
   vertex -6.86 5.01 23.63
   vertex -7.56 1.97 21.37
  endloop
 endfacet
 facet normal -0.72 0.20 0.67
  outer loop
   vertex -5.04 3.35 23.67
   vertex -7.56 1.97 21.37
   vertex -6.74 -3.37 23.83
  endloop
 endfacet
 facet normal 0.40 -0.92 -0.04
  outer loop
   vertex -6.18 -3.24 26.07
   vertex -6.74 -3.37 23.83
   vertex -4.70 -2.57 25.36
  endloop
 endfacet
 facet normal 0.35 -0.26 0.90
  outer loop
   vertex -5.64 -3.66 9.59
   vertex -9.47 -5.19 10.66
   vertex -5.11 -9.21 7.80
  endloop
 endfacet
 facet normal 0.31 -0.30 0.90
  outer loop
   vertex -5.11 -9.21 7.80
   vertex -9.47 -5.19 10.66
   vertex -11.08 -8.20 10.22
  endloop
 endfacet
 facet normal -0.40 -0.86 0.31
  outer loop
   vertex -5.31 -14.67 56.33
   vertex -8.25 -13.82 54.92
   vertex -5.37 -15.24 54.69
  endloop
 endfacet
 facet normal -0.04 -0.91 -0.40
  outer loop
   vertex -5.58 -15.84 42.39
   vertex -7.14 -14.79 40.16
   vertex -7.96 -12.04 34.02
  endloop
 endfacet
 facet normal -0.32 -0.88 -0.36
  outer loop
   vertex -4.93 -16.80 70.13
   vertex -10.22 -16.21 73.43
   vertex -9.83 -15.05 70.23
  endloop
 endfacet
 facet normal -0.35 0.62 0.71
  outer loop
   vertex -1.73 7.66 98.23
   vertex -9.83 4.95 96.60
   vertex -6.39 5.33 97.97
  endloop
 endfacet
 facet normal -0.24 0.08 0.97
  outer loop
   vertex -3.91 3.43 100.00
   vertex -7.83 2.62 99.10
   vertex -7.84 -1.66 99.47
  endloop
 endfacet
 facet normal -0.15 -0.44 0.89
  outer loop
   vertex -8.63 -7.67 98.10
   vertex -8.96 -12.01 95.91
   vertex -0.71 -9.55 98.52
  endloop
 endfacet
 facet normal -0.46 -0.67 -0.59
  outer loop
   vertex -7.96 -12.04 34.02
   vertex -7.18 -8.10 28.96
   vertex -5.36 -9.63 29.27
  endloop
 endfacet
 facet normal -0.29 -0.93 -0.21
  outer loop
   vertex -6.10 -18.81 79.30
   vertex -10.22 -16.21 73.43
   vertex -2.60 -18.49 72.85
  endloop
 endfacet
 facet normal -0.19 -0.52 0.83
  outer loop
   vertex -8.96 -12.01 95.91
   vertex -8.45 -16.09 93.50
   vertex -0.40 -15.90 95.49
  endloop
 endfacet
 facet normal -0.24 -0.94 0.22
  outer loop
   vertex -10.00 -16.18 86.29
   vertex -10.45 -16.84 82.95
   vertex -6.10 -18.81 79.30
  endloop
 endfacet
 facet normal -0.38 0.10 0.92
  outer loop
   vertex -6.39 5.33 97.97
   vertex -9.83 4.95 96.60
   vertex -8.07 -1.79 98.06
  endloop
 endfacet
 facet normal 0.28 -0.94 0.19
  outer loop
   vertex -4.70 -2.57 25.36
   vertex -10.52 -5.32 20.44
   vertex -6.33 -4.71 17.19
  endloop
 endfacet
 facet normal 0.47 -0.86 0.20
  outer loop
   vertex -5.11 -9.21 7.80
   vertex -9.38 -13.35 0.12
   vertex -4.36 -10.61 0.00
  endloop
 endfacet
 facet normal -0.25 -0.65 0.72
  outer loop
   vertex -8.45 -16.09 93.50
   vertex -6.52 -18.38 92.11
   vertex -5.05 -19.03 92.04
  endloop
 endfacet
 facet normal 0.04 -0.99 -0.13
  outer loop
   vertex -6.33 -4.71 17.19
   vertex -10.52 -5.32 20.44
   vertex -5.64 -3.66 9.59
  endloop
 endfacet
 facet normal 0.38 -0.93 0.03
  outer loop
   vertex -10.52 -5.32 20.44
   vertex -9.47 -5.19 10.66
   vertex -5.64 -3.66 9.59
  endloop
 endfacet
 facet normal -0.17 -0.76 0.62
  outer loop
   vertex -4.70 -2.57 25.36
   vertex -6.74 -3.37 23.83
   vertex -10.52 -5.32 20.44
  endloop
 endfacet
 facet normal -0.47 0.65 0.60
  outer loop
   vertex -2.04 15.54 57.89
   vertex -7.62 7.47 62.40
   vertex -3.30 10.28 62.69
  endloop
 endfacet
 facet normal 0.38 0.29 0.88
  outer loop
   vertex -9.83 4.95 96.60
   vertex -9.51 2.16 97.38
   vertex -8.07 -1.79 98.06
  endloop
 endfacet
 facet normal -0.54 -0.54 0.64
  outer loop
   vertex -7.43 -7.32 62.69
   vertex -12.29 -7.75 58.25
   vertex -7.95 -12.32 58.07
  endloop
 endfacet
 facet normal -0.34 0.34 0.88
  outer loop
   vertex -7.89 11.69 94.30
   vertex -11.56 5.20 95.44
   vertex -1.73 7.66 98.23
  endloop
 endfacet
 facet normal -0.35 0.65 0.67
  outer loop
   vertex -1.73 7.66 98.23
   vertex -11.56 5.20 95.44
   vertex -9.83 4.95 96.60
  endloop
 endfacet
 facet normal -0.22 0.38 0.90
  outer loop
   vertex -7.56 1.97 21.37
   vertex -10.06 -3.91 23.23
   vertex -6.74 -3.37 23.83
  endloop
 endfacet
 facet normal 0.13 -0.71 -0.69
  outer loop
   vertex -8.97 -4.39 27.54
   vertex -8.75 -4.06 27.24
   vertex -8.42 -4.04 27.29
  endloop
 endfacet
 facet normal 0.64 -0.77 0.06
  outer loop
   vertex -5.11 -9.21 7.80
   vertex -9.49 -13.15 3.73
   vertex -9.38 -13.35 0.12
  endloop
 endfacet
 facet normal -0.81 -0.49 0.34
  outer loop
   vertex -7.14 -14.79 40.16
   vertex -5.58 -15.84 42.39
   vertex -8.85 -13.38 38.12
  endloop
 endfacet
 facet normal -0.29 0.61 0.73
  outer loop
   vertex -9.91 11.76 57.90
   vertex -7.62 7.47 62.40
   vertex -2.04 15.54 57.89
  endloop
 endfacet
 facet normal -0.01 -1.00 -0.04
  outer loop
   vertex -6.85 4.90 26.37
   vertex -10.96 5.06 23.64
   vertex -6.86 5.01 23.63
  endloop
 endfacet
 facet normal -0.23 0.59 0.77
  outer loop
   vertex -10.06 -3.91 23.23
   vertex -10.15 -4.31 23.51
   vertex -6.74 -3.37 23.83
  endloop
 endfacet
 facet normal -0.37 -0.23 0.90
  outer loop
   vertex -7.97 -4.57 97.40
   vertex -8.07 -1.79 98.06
   vertex -9.50 -5.00 96.66
  endloop
 endfacet
 facet normal 0.85 -0.52 0.06
  outer loop
   vertex -8.75 -4.06 27.24
   vertex -8.97 -4.39 27.54
   vertex -8.91 -4.39 26.69
  endloop
 endfacet
 facet normal 0.23 -0.93 0.28
  outer loop
   vertex -10.15 -4.31 23.51
   vertex -10.52 -5.32 20.44
   vertex -6.74 -3.37 23.83
  endloop
 endfacet
 facet normal -0.29 -0.42 0.86
  outer loop
   vertex -7.97 -4.57 97.40
   vertex -9.50 -5.00 96.66
   vertex -8.05 -10.91 94.29
  endloop
 endfacet
 facet normal -0.45 -0.89 -0.05
  outer loop
   vertex -10.45 -16.84 82.95
   vertex -12.23 -15.52 75.67
   vertex -6.10 -18.81 79.30
  endloop
 endfacet
 facet normal -0.02 -1.00 -0.02
  outer loop
   vertex -6.85 4.90 26.37
   vertex -11.19 5.00 26.18
   vertex -10.96 5.06 23.64
  endloop
 endfacet
 facet normal -0.11 -0.99 -0.01
  outer loop
   vertex -8.97 -4.39 27.54
   vertex -10.00 -4.25 24.66
   vertex -8.91 -4.39 26.69
  endloop
 endfacet
 facet normal 0.01 -0.73 -0.68
  outer loop
   vertex -6.85 4.90 26.37
   vertex -12.76 3.29 28.01
   vertex -11.19 5.00 26.18
  endloop
 endfacet
 facet normal 0.00 -0.62 0.79
  outer loop
   vertex -6.86 5.01 23.63
   vertex -10.96 5.06 23.64
   vertex -10.83 2.64 21.75
  endloop
 endfacet
 facet normal -0.03 -0.59 0.81
  outer loop
   vertex -6.86 5.01 23.63
   vertex -10.83 2.64 21.75
   vertex -7.56 1.97 21.37
  endloop
 endfacet
 facet normal 0.16 0.24 0.96
  outer loop
   vertex -7.56 1.97 21.37
   vertex -10.83 2.64 21.75
   vertex -10.06 -3.91 23.23
  endloop
 endfacet
 facet normal 0.23 -0.56 0.80
  outer loop
   vertex -11.08 -8.20 10.22
   vertex -11.01 -11.63 7.77
   vertex -5.11 -9.21 7.80
  endloop
 endfacet
 facet normal -0.48 -0.60 0.64
  outer loop
   vertex -6.55 -15.83 90.85
   vertex -8.05 -10.91 94.29
   vertex -11.35 -8.86 93.74
  endloop
 endfacet
 facet normal -0.50 -0.86 0.03
  outer loop
   vertex -8.25 -13.82 54.92
   vertex -12.56 -11.44 51.73
   vertex -5.58 -15.84 42.39
  endloop
 endfacet
 facet normal 0.95 -0.29 -0.11
  outer loop
   vertex -10.00 -4.25 24.66
   vertex -10.15 -4.31 23.51
   vertex -10.06 -3.91 23.23
  endloop
 endfacet
 facet normal -0.50 -0.15 0.85
  outer loop
   vertex -8.07 -1.79 98.06
   vertex -12.38 -3.37 95.27
   vertex -9.50 -5.00 96.66
  endloop
 endfacet
 facet normal 0.34 -0.83 0.44
  outer loop
   vertex -5.11 -9.21 7.80
   vertex -11.01 -11.63 7.77
   vertex -9.49 -13.15 3.73
  endloop
 endfacet
 facet normal -0.42 -0.90 -0.10
  outer loop
   vertex -6.10 -18.81 79.30
   vertex -12.23 -15.52 75.67
   vertex -10.22 -16.21 73.43
  endloop
 endfacet
 facet normal -0.51 0.52 0.69
  outer loop
   vertex -12.11 13.09 90.10
   vertex -11.85 8.19 94.03
   vertex -7.89 11.69 94.30
  endloop
 endfacet
 facet normal -0.38 0.36 0.85
  outer loop
   vertex -7.89 11.69 94.30
   vertex -11.85 8.19 94.03
   vertex -11.56 5.20 95.44
  endloop
 endfacet
 facet normal -0.53 0.17 0.83
  outer loop
   vertex -11.56 5.20 95.44
   vertex -9.51 2.16 97.38
   vertex -9.83 4.95 96.60
  endloop
 endfacet
 facet normal 0.11 0.65 -0.75
  outer loop
   vertex -11.55 -2.11 28.27
   vertex -11.40 -1.67 28.68
   vertex -8.91 -4.39 26.69
  endloop
 endfacet
 facet normal -0.40 -0.42 0.81
  outer loop
   vertex -8.05 -10.91 94.29
   vertex -9.50 -5.00 96.66
   vertex -11.35 -8.86 93.74
  endloop
 endfacet
 facet normal -0.09 -0.94 0.32
  outer loop
   vertex -11.01 -11.63 7.77
   vertex -12.92 -13.75 1.06
   vertex -9.49 -13.15 3.73
  endloop
 endfacet
 facet normal -0.57 -0.82 -0.04
  outer loop
   vertex -12.56 -11.44 51.73
   vertex -8.85 -13.38 38.12
   vertex -5.58 -15.84 42.39
  endloop
 endfacet
 facet normal 0.13 -0.99 0.06
  outer loop
   vertex -9.49 -13.15 3.73
   vertex -12.92 -13.75 1.06
   vertex -9.38 -13.35 0.12
  endloop
 endfacet
 facet normal -0.56 -0.80 0.23
  outer loop
   vertex -10.00 -16.18 86.29
   vertex -12.79 -14.66 84.76
   vertex -10.45 -16.84 82.95
  endloop
 endfacet
 facet normal -0.43 -0.10 0.90
  outer loop
   vertex -10.45 1.82 62.30
   vertex -14.53 -1.69 59.96
   vertex -7.43 -7.32 62.69
  endloop
 endfacet
 facet normal -0.61 -0.76 -0.23
  outer loop
   vertex -12.03 -3.20 31.61
   vertex -11.97 -2.57 29.42
   vertex -8.97 -4.39 27.54
  endloop
 endfacet
 facet normal -0.61 -0.61 0.51
  outer loop
   vertex -6.55 -15.83 90.85
   vertex -12.79 -14.66 84.76
   vertex -10.00 -16.18 86.29
  endloop
 endfacet
 facet normal -0.69 0.58 0.43
  outer loop
   vertex -9.91 11.76 57.90
   vertex -10.31 12.71 56.01
   vertex -13.56 8.97 55.86
  endloop
 endfacet
 facet normal 0.73 -0.40 0.56
  outer loop
   vertex -10.83 2.64 21.75
   vertex -10.96 5.06 23.64
   vertex -12.37 1.98 23.28
  endloop
 endfacet
 facet normal 0.29 0.24 0.93
  outer loop
   vertex -10.83 2.64 21.75
   vertex -12.49 -0.47 23.08
   vertex -10.06 -3.91 23.23
  endloop
 endfacet
 facet normal 0.62 0.77 0.16
  outer loop
   vertex -12.01 -2.43 23.75
   vertex -10.00 -4.25 24.66
   vertex -10.06 -3.91 23.23
  endloop
 endfacet
 facet normal -0.53 -0.84 0.12
  outer loop
   vertex -10.00 -4.25 24.66
   vertex -12.89 -2.83 21.72
   vertex -10.15 -4.31 23.51
  endloop
 endfacet
 facet normal -0.60 -0.74 0.31
  outer loop
   vertex -10.15 -4.31 23.51
   vertex -12.89 -2.83 21.72
   vertex -10.52 -5.32 20.44
  endloop
 endfacet
 facet normal -0.55 -0.32 0.77
  outer loop
   vertex -12.38 -3.37 95.27
   vertex -11.35 -8.86 93.74
   vertex -9.50 -5.00 96.66
  endloop
 endfacet
 facet normal -0.66 -0.66 -0.36
  outer loop
   vertex -8.85 -13.38 38.12
   vertex -13.23 -7.86 35.98
   vertex -7.96 -12.04 34.02
  endloop
 endfacet
 facet normal -0.48 -0.81 -0.35
  outer loop
   vertex -10.22 -16.21 73.43
   vertex -12.16 -15.09 73.51
   vertex -9.83 -15.05 70.23
  endloop
 endfacet
 facet normal -0.60 0.30 0.75
  outer loop
   vertex -11.85 8.19 94.03
   vertex -14.36 6.90 92.53
   vertex -11.56 5.20 95.44
  endloop
 endfacet
 facet normal 0.65 -0.76 0.04
  outer loop
   vertex -10.96 5.06 23.64
   vertex -11.19 5.00 26.18
   vertex -12.74 3.56 23.93
  endloop
 endfacet
 facet normal 0.50 0.39 0.77
  outer loop
   vertex -12.01 -2.43 23.75
   vertex -10.06 -3.91 23.23
   vertex -12.49 -0.47 23.08
  endloop
 endfacet
 facet normal -0.51 -0.86 0.09
  outer loop
   vertex -11.97 -2.57 29.42
   vertex -12.89 -2.83 21.72
   vertex -10.00 -4.25 24.66
  endloop
 endfacet
 facet normal -0.58 -0.79 0.19
  outer loop
   vertex -12.79 -14.66 84.76
   vertex -12.10 -15.80 82.23
   vertex -10.45 -16.84 82.95
  endloop
 endfacet
 facet normal -0.49 -0.85 -0.18
  outer loop
   vertex -10.22 -16.21 73.43
   vertex -12.23 -15.52 75.67
   vertex -12.16 -15.09 73.51
  endloop
 endfacet
 facet normal -0.61 0.45 0.65
  outer loop
   vertex -7.62 7.47 62.40
   vertex -13.56 8.97 55.86
   vertex -14.50 4.74 57.87
  endloop
 endfacet
 facet normal 0.71 -0.70 -0.04
  outer loop
   vertex -12.76 3.29 28.01
   vertex -12.74 3.56 23.93
   vertex -11.19 5.00 26.18
  endloop
 endfacet
 facet normal 0.38 -0.27 0.89
  outer loop
   vertex -10.96 5.06 23.64
   vertex -12.74 3.56 23.93
   vertex -12.37 1.98 23.28
  endloop
 endfacet
 facet normal 0.72 -0.09 0.68
  outer loop
   vertex -10.83 2.64 21.75
   vertex -12.37 1.98 23.28
   vertex -12.49 -0.47 23.08
  endloop
 endfacet
 facet normal 0.77 0.62 -0.12
  outer loop
   vertex -12.80 -0.60 28.02
   vertex -11.55 -2.11 28.27
   vertex -12.01 -2.43 23.75
  endloop
 endfacet
 facet normal -0.59 -0.41 0.69
  outer loop
   vertex -7.43 -7.32 62.69
   vertex -14.53 -1.69 59.96
   vertex -12.29 -7.75 58.25
  endloop
 endfacet
 facet normal -0.65 -0.65 0.39
  outer loop
   vertex -12.29 -7.75 58.25
   vertex -12.56 -11.44 51.73
   vertex -8.25 -13.82 54.92
  endloop
 endfacet
 facet normal -0.24 -0.90 0.35
  outer loop
   vertex -11.01 -11.63 7.77
   vertex -16.78 -10.65 6.36
   vertex -12.92 -13.75 1.06
  endloop
 endfacet
 facet normal -0.60 -0.62 0.50
  outer loop
   vertex -6.55 -15.83 90.85
   vertex -11.35 -8.86 93.74
   vertex -12.79 -14.66 84.76
  endloop
 endfacet
 facet normal -0.69 -0.53 -0.50
  outer loop
   vertex -12.16 -15.09 73.51
   vertex -15.72 -12.56 75.72
   vertex -9.83 -15.05 70.23
  endloop
 endfacet
 facet normal -0.59 0.48 0.64
  outer loop
   vertex -12.11 13.09 90.10
   vertex -15.12 8.50 90.79
   vertex -11.85 8.19 94.03
  endloop
 endfacet
 facet normal 0.96 0.26 0.07
  outer loop
   vertex -12.80 -0.60 28.02
   vertex -12.01 -2.43 23.75
   vertex -12.49 -0.47 23.08
  endloop
 endfacet
 facet normal -0.27 -0.96 -0.04
  outer loop
   vertex -10.52 -5.32 20.44
   vertex -14.81 -3.65 10.35
   vertex -9.47 -5.19 10.66
  endloop
 endfacet
 facet normal -0.29 -0.56 0.78
  outer loop
   vertex -11.08 -8.20 10.22
   vertex -16.78 -10.65 6.36
   vertex -11.01 -11.63 7.77
  endloop
 endfacet
 facet normal -0.86 -0.51 0.00
  outer loop
   vertex -12.10 -15.80 82.23
   vertex -12.79 -14.66 84.76
   vertex -12.23 -15.52 75.67
  endloop
 endfacet
 facet normal -0.74 -0.07 0.67
  outer loop
   vertex -14.36 6.90 92.53
   vertex -9.51 2.16 97.38
   vertex -11.56 5.20 95.44
  endloop
 endfacet
 facet normal 1.00 0.06 0.01
  outer loop
   vertex -12.76 3.29 28.01
   vertex -12.49 -0.47 23.08
   vertex -12.74 3.56 23.93
  endloop
 endfacet
 facet normal 0.75 -0.09 0.65
  outer loop
   vertex -12.74 3.56 23.93
   vertex -12.49 -0.47 23.08
   vertex -12.37 1.98 23.28
  endloop
 endfacet
 facet normal 1.00 -0.01 0.06
  outer loop
   vertex -12.76 3.29 28.01
   vertex -12.80 -0.60 28.02
   vertex -12.49 -0.47 23.08
  endloop
 endfacet
 facet normal -0.78 -0.61 0.11
  outer loop
   vertex -11.97 -2.57 29.42
   vertex -13.92 -1.70 20.75
   vertex -12.89 -2.83 21.72
  endloop
 endfacet
 facet normal -0.09 -0.10 0.99
  outer loop
   vertex -9.47 -5.19 10.66
   vertex -14.81 -3.65 10.35
   vertex -11.08 -8.20 10.22
  endloop
 endfacet
 facet normal -0.76 -0.64 -0.11
  outer loop
   vertex -12.56 -11.44 51.73
   vertex -13.23 -7.86 35.98
   vertex -8.85 -13.38 38.12
  endloop
 endfacet
 facet normal -0.64 -0.75 -0.17
  outer loop
   vertex -12.23 -15.52 75.67
   vertex -15.72 -12.56 75.72
   vertex -12.16 -15.09 73.51
  endloop
 endfacet
 facet normal -0.65 -0.76 0.03
  outer loop
   vertex -12.23 -15.52 75.67
   vertex -12.79 -14.66 84.76
   vertex -15.72 -12.56 75.72
  endloop
 endfacet
 facet normal -0.33 0.94 0.01
  outer loop
   vertex -16.43 8.45 0.29
   vertex -14.73 9.02 4.55
   vertex -12.77 9.74 0.21
  endloop
 endfacet
 facet normal -0.51 -0.40 0.76
  outer loop
   vertex -14.53 -1.69 59.96
   vertex -14.70 -2.97 59.17
   vertex -12.29 -7.75 58.25
  endloop
 endfacet
 facet normal -0.16 -0.16 0.97
  outer loop
   vertex -14.81 -3.65 10.35
   vertex -15.10 -8.08 9.59
   vertex -11.08 -8.20 10.22
  endloop
 endfacet
 facet normal -0.53 -0.05 0.85
  outer loop
   vertex -8.07 -1.79 98.06
   vertex -9.51 2.16 97.38
   vertex -12.38 -3.37 95.27
  endloop
 endfacet
 facet normal 0.72 -0.17 0.68
  outer loop
   vertex -13.64 1.69 59.87
   vertex -14.52 0.42 60.49
   vertex -14.53 -1.69 59.96
  endloop
 endfacet
 facet normal -0.55 -0.66 0.51
  outer loop
   vertex -11.35 -8.86 93.74
   vertex -15.80 -11.01 86.17
   vertex -12.79 -14.66 84.76
  endloop
 endfacet
 facet normal -0.61 0.43 0.66
  outer loop
   vertex -15.12 8.50 90.79
   vertex -14.36 6.90 92.53
   vertex -11.85 8.19 94.03
  endloop
 endfacet
 facet normal 0.59 0.55 0.59
  outer loop
   vertex -14.50 4.74 57.87
   vertex -15.24 3.84 59.44
   vertex -13.64 1.69 59.87
  endloop
 endfacet
 facet normal 0.19 0.32 0.93
  outer loop
   vertex -15.24 3.84 59.44
   vertex -14.52 0.42 60.49
   vertex -13.64 1.69 59.87
  endloop
 endfacet
 facet normal -0.73 -0.65 0.20
  outer loop
   vertex -10.52 -5.32 20.44
   vertex -16.08 -2.33 9.99
   vertex -14.81 -3.65 10.35
  endloop
 endfacet
 facet normal -0.61 0.17 0.78
  outer loop
   vertex -14.36 6.90 92.53
   vertex -16.37 3.81 91.66
   vertex -9.51 2.16 97.38
  endloop
 endfacet
 facet normal -0.44 -0.88 0.19
  outer loop
   vertex -16.78 -10.65 6.36
   vertex -17.09 -11.83 0.17
   vertex -12.92 -13.75 1.06
  endloop
 endfacet
 facet normal -0.13 -0.64 -0.76
  outer loop
   vertex -12.92 -13.75 1.06
   vertex -17.09 -11.83 0.17
   vertex -9.38 -13.35 0.12
  endloop
 endfacet
 facet normal 0.06 0.30 0.95
  outer loop
   vertex -15.24 3.84 59.44
   vertex -17.55 3.97 59.55
   vertex -14.52 0.42 60.49
  endloop
 endfacet
 facet normal 0.16 0.38 0.91
  outer loop
   vertex -14.52 0.42 60.49
   vertex -17.55 3.97 59.55
   vertex -17.86 1.93 60.46
  endloop
 endfacet
 facet normal -0.65 -0.36 0.67
  outer loop
   vertex -16.37 3.81 91.66
   vertex -18.99 2.53 88.43
   vertex -9.51 2.16 97.38
  endloop
 endfacet
 facet normal -0.68 0.08 0.73
  outer loop
   vertex -9.51 2.16 97.38
   vertex -18.99 2.53 88.43
   vertex -12.38 -3.37 95.27
  endloop
 endfacet
 facet normal -0.12 -0.24 0.96
  outer loop
   vertex -14.52 0.42 60.49
   vertex -17.86 1.93 60.46
   vertex -14.53 -1.69 59.96
  endloop
 endfacet
 facet normal -0.39 -0.13 0.91
  outer loop
   vertex -14.81 -3.65 10.35
   vertex -16.08 -2.33 9.99
   vertex -15.10 -8.08 9.59
  endloop
 endfacet
 facet normal -0.01 -0.92 0.39
  outer loop
   vertex -17.81 -2.85 59.37
   vertex -15.22 -4.36 55.87
   vertex -14.70 -2.97 59.17
  endloop
 endfacet
 facet normal -0.74 -0.33 0.59
  outer loop
   vertex -19.06 -1.54 88.25
   vertex -19.20 -4.59 86.36
   vertex -11.35 -8.86 93.74
  endloop
 endfacet
 facet normal -0.12 -0.74 0.66
  outer loop
   vertex -15.10 -8.08 9.59
   vertex -16.78 -10.65 6.36
   vertex -11.08 -8.20 10.22
  endloop
 endfacet
 facet normal -0.73 -0.40 0.55
  outer loop
   vertex -19.20 -4.59 86.36
   vertex -15.80 -11.01 86.17
   vertex -11.35 -8.86 93.74
  endloop
 endfacet
 facet normal 0.17 0.82 0.55
  outer loop
   vertex -14.50 4.74 57.87
   vertex -17.53 4.98 58.45
   vertex -15.24 3.84 59.44
  endloop
 endfacet
 facet normal 0.98 0.07 0.17
  outer loop
   vertex -17.26 3.52 30.88
   vertex -16.22 -2.44 27.38
   vertex -16.83 3.51 28.37
  endloop
 endfacet
 facet normal 0.95 -0.02 0.31
  outer loop
   vertex -17.26 3.52 30.88
   vertex -17.25 -3.20 30.51
   vertex -16.22 -2.44 27.38
  endloop
 endfacet
 facet normal -0.09 -0.22 0.97
  outer loop
   vertex -17.86 1.93 60.46
   vertex -17.81 -2.85 59.37
   vertex -14.53 -1.69 59.96
  endloop
 endfacet
 facet normal 0.04 -0.53 0.85
  outer loop
   vertex -14.53 -1.69 59.96
   vertex -17.81 -2.85 59.37
   vertex -14.70 -2.97 59.17
  endloop
 endfacet
 facet normal -0.24 -0.94 0.23
  outer loop
   vertex -17.81 -2.85 59.37
   vertex -19.78 -3.38 55.19
   vertex -15.22 -4.36 55.87
  endloop
 endfacet
 facet normal -0.17 -0.96 -0.22
  outer loop
   vertex -19.78 -3.38 55.19
   vertex -19.28 -2.69 51.78
   vertex -16.89 -2.78 50.33
  endloop
 endfacet
 facet normal -0.17 -0.96 -0.22
  outer loop
   vertex -15.22 -4.36 55.87
   vertex -19.78 -3.38 55.19
   vertex -16.89 -2.78 50.33
  endloop
 endfacet
 facet normal -0.63 0.42 0.66
  outer loop
   vertex -17.30 6.34 6.02
   vertex -19.35 2.04 6.79
   vertex -14.37 6.39 8.79
  endloop
 endfacet
 facet normal -0.65 0.47 0.59
  outer loop
   vertex -14.37 6.39 8.79
   vertex -19.35 2.04 6.79
   vertex -16.70 2.03 9.70
  endloop
 endfacet
 facet normal 0.83 -0.46 -0.30
  outer loop
   vertex -16.89 -2.78 50.33
   vertex -18.85 -1.53 42.99
   vertex -17.20 -1.49 47.50
  endloop
 endfacet
 facet normal 0.31 -0.92 -0.24
  outer loop
   vertex -16.89 -2.78 50.33
   vertex -23.72 -3.30 43.51
   vertex -18.85 -1.53 42.99
  endloop
 endfacet
 facet normal -0.97 -0.15 -0.20
  outer loop
   vertex -16.08 -2.33 9.99
   vertex -16.70 2.03 9.70
   vertex -15.10 -8.08 9.59
  endloop
 endfacet
 facet normal -0.63 -0.11 0.77
  outer loop
   vertex -15.10 -8.08 9.59
   vertex -16.70 2.03 9.70
   vertex -19.13 -6.49 6.49
  endloop
 endfacet
 facet normal -0.19 -0.94 -0.29
  outer loop
   vertex -17.25 -3.20 30.51
   vertex -19.61 -2.94 31.17
   vertex -16.22 -2.44 27.38
  endloop
 endfacet
 facet normal -0.50 -0.84 0.19
  outer loop
   vertex -16.78 -10.65 6.36
   vertex -18.27 -10.94 1.02
   vertex -17.09 -11.83 0.17
  endloop
 endfacet
 facet normal 0.43 0.05 0.90
  outer loop
   vertex -17.26 3.52 30.88
   vertex -18.71 3.17 31.60
   vertex -18.24 1.18 31.48
  endloop
 endfacet
 facet normal 0.97 -0.12 -0.19
  outer loop
   vertex -17.50 2.23 34.58
   vertex -17.69 -1.61 35.95
   vertex -18.24 1.18 31.48
  endloop
 endfacet
 facet normal 0.91 -0.40 -0.06
  outer loop
   vertex -17.26 3.52 30.88
   vertex -18.24 1.18 31.48
   vertex -18.48 0.70 31.08
  endloop
 endfacet
 facet normal 0.77 -0.29 0.57
  outer loop
   vertex -18.48 0.70 31.08
   vertex -18.61 -0.12 30.83
   vertex -17.26 3.52 30.88
  endloop
 endfacet
 facet normal 0.91 -0.27 -0.33
  outer loop
   vertex -17.20 -1.49 47.50
   vertex -18.85 -1.53 42.99
   vertex -17.34 0.41 45.58
  endloop
 endfacet
 facet normal -0.78 0.28 0.56
  outer loop
   vertex -18.61 -0.12 30.83
   vertex -18.49 -1.69 31.79
   vertex -17.26 3.52 30.88
  endloop
 endfacet
 facet normal 0.69 -0.04 0.72
  outer loop
   vertex -17.26 3.52 30.88
   vertex -18.49 -1.69 31.79
   vertex -17.25 -3.20 30.51
  endloop
 endfacet
 facet normal 0.01 -1.00 0.07
  outer loop
   vertex -16.89 -2.78 50.33
   vertex -19.28 -2.69 51.78
   vertex -23.72 -3.30 43.51
  endloop
 endfacet
 facet normal -0.54 -0.77 0.35
  outer loop
   vertex -20.03 -1.56 58.80
   vertex -19.78 -3.38 55.19
   vertex -17.81 -2.85 59.37
  endloop
 endfacet
 facet normal -0.86 -0.48 -0.16
  outer loop
   vertex -19.23 -7.00 77.87
   vertex -19.21 -6.14 75.07
   vertex -15.72 -12.56 75.72
  endloop
 endfacet
 facet normal -0.72 -0.54 -0.43
  outer loop
   vertex -17.09 -11.83 0.17
   vertex -18.27 -10.94 1.02
   vertex -19.07 -9.21 0.19
  endloop
 endfacet
 facet normal -0.36 0.69 0.63
  outer loop
   vertex -17.53 4.98 58.45
   vertex -19.56 3.41 59.03
   vertex -17.55 3.97 59.55
  endloop
 endfacet
 facet normal -0.34 0.43 0.84
  outer loop
   vertex -17.55 3.97 59.55
   vertex -19.56 3.41 59.03
   vertex -17.86 1.93 60.46
  endloop
 endfacet
 facet normal 0.92 0.24 -0.30
  outer loop
   vertex -18.71 3.17 31.60
   vertex -17.50 2.23 34.58
   vertex -18.24 1.18 31.48
  endloop
 endfacet
 facet normal 0.97 0.04 0.25
  outer loop
   vertex -19.66 3.89 42.46
   vertex -17.69 -1.61 35.95
   vertex -17.50 2.23 34.58
  endloop
 endfacet
 facet normal 0.84 0.07 -0.54
  outer loop
   vertex -19.66 3.89 42.46
   vertex -17.34 0.41 45.58
   vertex -18.85 -1.53 42.99
  endloop
 endfacet
 facet normal 0.98 -0.11 -0.19
  outer loop
   vertex -18.24 1.18 31.48
   vertex -17.69 -1.61 35.95
   vertex -18.49 -1.69 31.79
  endloop
 endfacet
 facet normal 0.17 -0.55 0.82
  outer loop
   vertex -18.49 -1.69 31.79
   vertex -19.61 -2.94 31.17
   vertex -17.25 -3.20 30.51
  endloop
 endfacet
 facet normal 0.97 0.16 0.16
  outer loop
   vertex -19.66 3.89 42.46
   vertex -18.85 -1.53 42.99
   vertex -17.69 -1.61 35.95
  endloop
 endfacet
 facet normal 0.91 -0.12 -0.39
  outer loop
   vertex -18.24 1.18 31.48
   vertex -18.49 -1.69 31.79
   vertex -18.48 0.70 31.08
  endloop
 endfacet
 facet normal 0.97 -0.08 -0.25
  outer loop
   vertex -18.49 -1.69 31.79
   vertex -18.61 -0.12 30.83
   vertex -18.48 0.70 31.08
  endloop
 endfacet
 facet normal 0.78 0.62 0.08
  outer loop
   vertex -19.66 3.89 42.46
   vertex -17.50 2.23 34.58
   vertex -20.94 6.69 33.09
  endloop
 endfacet
 facet normal -0.54 0.80 0.26
  outer loop
   vertex -21.02 3.14 56.84
   vertex -19.56 3.41 59.03
   vertex -17.53 4.98 58.45
  endloop
 endfacet
 facet normal 0.81 0.57 -0.15
  outer loop
   vertex -17.50 2.23 34.58
   vertex -18.71 3.17 31.60
   vertex -20.94 6.69 33.09
  endloop
 endfacet
 facet normal 0.60 0.77 -0.22
  outer loop
   vertex -21.37 5.31 42.77
   vertex -17.02 3.99 50.02
   vertex -19.66 3.89 42.46
  endloop
 endfacet
 facet normal 0.78 0.06 -0.62
  outer loop
   vertex -18.48 0.70 31.08
   vertex -18.61 -0.12 30.83
   vertex -19.53 -0.65 29.62
  endloop
 endfacet
 facet normal 0.71 0.43 0.55
  outer loop
   vertex -18.88 8.29 83.81
   vertex -20.02 6.73 86.49
   vertex -18.99 2.53 88.43
  endloop
 endfacet
 facet normal -0.71 0.14 0.69
  outer loop
   vertex -18.99 2.53 88.43
   vertex -20.02 6.73 86.49
   vertex -20.17 -2.21 88.21
  endloop
 endfacet
 facet normal 0.83 0.55 -0.07
  outer loop
   vertex -20.94 6.69 33.09
   vertex -18.71 3.17 31.60
   vertex -19.35 3.82 29.10
  endloop
 endfacet
 facet normal 0.96 -0.27 0.11
  outer loop
   vertex -19.50 3.46 25.45
   vertex -20.04 1.58 25.51
   vertex -19.29 3.54 23.82
  endloop
 endfacet
 facet normal 0.95 -0.29 0.09
  outer loop
   vertex -19.29 3.54 23.82
   vertex -20.04 1.58 25.51
   vertex -19.80 1.66 23.05
  endloop
 endfacet
 facet normal -0.01 -0.05 1.00
  outer loop
   vertex -20.17 -2.21 88.21
   vertex -19.06 -1.54 88.25
   vertex -18.99 2.53 88.43
  endloop
 endfacet
 facet normal -0.63 0.02 0.77
  outer loop
   vertex -19.56 3.41 59.03
   vertex -20.03 -1.56 58.80
   vertex -17.86 1.93 60.46
  endloop
 endfacet
 facet normal -0.36 -0.21 0.91
  outer loop
   vertex -17.86 1.93 60.46
   vertex -20.03 -1.56 58.80
   vertex -17.81 -2.85 59.37
  endloop
 endfacet
 facet normal 0.99 0.00 0.11
  outer loop
   vertex -19.20 -0.81 22.66
   vertex -19.40 -2.47 24.51
   vertex -19.19 -2.35 22.59
  endloop
 endfacet
 facet normal 0.28 -0.51 0.81
  outer loop
   vertex -19.06 -1.54 88.25
   vertex -20.17 -2.21 88.21
   vertex -19.20 -4.59 86.36
  endloop
 endfacet
 facet normal 0.77 -0.63 -0.14
  outer loop
   vertex -18.49 -1.69 31.79
   vertex -17.69 -1.61 35.95
   vertex -19.61 -2.94 31.17
  endloop
 endfacet
 facet normal 0.00 -0.99 -0.13
  outer loop
   vertex -19.61 -2.94 31.17
   vertex -20.34 -2.74 29.64
   vertex -16.22 -2.44 27.38
  endloop
 endfacet
 facet normal -0.19 -0.94 -0.29
  outer loop
   vertex -19.23 -7.00 77.87
   vertex -20.72 -6.12 75.99
   vertex -19.21 -6.14 75.07
  endloop
 endfacet
 facet normal 0.46 0.23 -0.86
  outer loop
   vertex -19.29 3.54 23.82
   vertex -19.80 1.66 23.05
   vertex -22.07 3.56 22.34
  endloop
 endfacet
 facet normal 0.68 0.51 0.53
  outer loop
   vertex -22.55 -0.69 26.86
   vertex -19.40 -2.47 24.51
   vertex -19.20 -0.81 22.66
  endloop
 endfacet
 facet normal -0.08 -0.63 0.77
  outer loop
   vertex -20.17 -2.21 88.21
   vertex -20.04 -5.86 85.22
   vertex -19.20 -4.59 86.36
  endloop
 endfacet
 facet normal -0.44 -0.55 -0.71
  outer loop
   vertex -20.72 -6.12 75.99
   vertex -20.54 -1.47 72.24
   vertex -19.21 -6.14 75.07
  endloop
 endfacet
 facet normal 0.74 -0.65 0.18
  outer loop
   vertex -19.20 -4.59 86.36
   vertex -20.04 -5.86 85.22
   vertex -19.23 -7.00 77.87
  endloop
 endfacet
 facet normal 0.60 -0.77 0.19
  outer loop
   vertex -19.23 -7.00 77.87
   vertex -20.04 -5.86 85.22
   vertex -20.20 -7.07 80.73
  endloop
 endfacet
 facet normal 0.62 -0.69 -0.38
  outer loop
   vertex -19.61 -2.94 31.17
   vertex -20.84 -4.57 32.16
   vertex -20.34 -2.74 29.64
  endloop
 endfacet
 facet normal 0.75 -0.65 0.13
  outer loop
   vertex -18.85 -1.53 42.99
   vertex -20.83 -4.62 38.86
   vertex -17.69 -1.61 35.95
  endloop
 endfacet
 facet normal 0.76 -0.64 -0.13
  outer loop
   vertex -17.69 -1.61 35.95
   vertex -20.84 -4.57 32.16
   vertex -19.61 -2.94 31.17
  endloop
 endfacet
 facet normal 0.69 -0.73 -0.01
  outer loop
   vertex -20.83 -4.62 38.86
   vertex -20.84 -4.57 32.16
   vertex -17.69 -1.61 35.95
  endloop
 endfacet
 facet normal -0.36 -0.92 -0.14
  outer loop
   vertex -19.23 -7.00 77.87
   vertex -20.20 -7.07 80.73
   vertex -20.72 -6.12 75.99
  endloop
 endfacet
 facet normal 0.42 0.81 -0.41
  outer loop
   vertex -20.94 6.69 33.09
   vertex -19.35 3.82 29.10
   vertex -21.34 5.38 30.11
  endloop
 endfacet
 facet normal 0.68 -0.04 -0.73
  outer loop
   vertex -19.28 1.12 29.76
   vertex -19.53 -0.65 29.62
   vertex -22.62 1.50 26.64
  endloop
 endfacet
 facet normal -0.83 -0.04 0.56
  outer loop
   vertex -20.03 -1.56 58.80
   vertex -21.62 1.41 56.63
   vertex -21.54 -0.26 56.64
  endloop
 endfacet
 facet normal 0.35 -0.82 0.45
  outer loop
   vertex -18.85 -1.53 42.99
   vertex -23.72 -3.30 43.51
   vertex -20.83 -4.62 38.86
  endloop
 endfacet
 facet normal 0.52 -0.12 0.84
  outer loop
   vertex -19.50 3.46 25.45
   vertex -22.25 3.63 27.18
   vertex -20.04 1.58 25.51
  endloop
 endfacet
 facet normal 0.02 -1.00 -0.03
  outer loop
   vertex -20.04 1.58 25.51
   vertex -22.62 1.50 26.64
   vertex -19.80 1.66 23.05
  endloop
 endfacet
 facet normal -0.68 -0.61 0.41
  outer loop
   vertex -19.28 -2.69 51.78
   vertex -23.86 0.76 49.34
   vertex -23.72 -3.30 43.51
  endloop
 endfacet
 facet normal 0.64 0.14 0.75
  outer loop
   vertex -22.55 -0.69 26.86
   vertex -22.69 -2.60 27.34
   vertex -19.40 -2.47 24.51
  endloop
 endfacet
 facet normal 0.23 -0.97 -0.04
  outer loop
   vertex -19.40 -2.47 24.51
   vertex -23.38 -3.50 27.08
   vertex -19.19 -2.35 22.59
  endloop
 endfacet
 facet normal 0.01 -1.00 -0.03
  outer loop
   vertex -23.54 1.62 22.92
   vertex -22.19 1.65 22.40
   vertex -19.80 1.66 23.05
  endloop
 endfacet
 facet normal 0.68 -0.05 -0.74
  outer loop
   vertex -22.62 1.50 26.64
   vertex -19.53 -0.65 29.62
   vertex -22.55 -0.69 26.86
  endloop
 endfacet
 facet normal 0.22 -0.98 -0.05
  outer loop
   vertex -23.38 -3.50 27.08
   vertex -20.16 -2.53 21.76
   vertex -19.19 -2.35 22.59
  endloop
 endfacet
 facet normal 0.65 -0.67 -0.36
  outer loop
   vertex -20.84 -4.57 32.16
   vertex -22.52 -4.42 28.80
   vertex -20.34 -2.74 29.64
  endloop
 endfacet
 facet normal 0.27 -0.87 0.41
  outer loop
   vertex -23.72 -3.30 43.51
   vertex -23.27 -5.29 39.02
   vertex -20.83 -4.62 38.86
  endloop
 endfacet
 facet normal 0.56 0.73 -0.40
  outer loop
   vertex -20.94 6.69 33.09
   vertex -21.34 5.38 30.11
   vertex -22.34 6.69 31.09
  endloop
 endfacet
 facet normal 0.39 -0.29 0.87
  outer loop
   vertex -22.25 3.63 27.18
   vertex -22.62 1.50 26.64
   vertex -20.04 1.58 25.51
  endloop
 endfacet
 facet normal -0.85 0.11 0.52
  outer loop
   vertex -21.41 1.72 53.15
   vertex -23.86 0.76 49.34
   vertex -21.50 0.68 53.23
  endloop
 endfacet
 facet normal 0.01 -1.00 -0.04
  outer loop
   vertex -19.80 1.66 23.05
   vertex -22.62 1.50 26.64
   vertex -23.54 1.62 22.92
  endloop
 endfacet
 facet normal -0.07 -1.00 -0.01
  outer loop
   vertex -25.37 -4.24 29.49
   vertex -22.52 -4.42 28.80
   vertex -20.84 -4.57 32.16
  endloop
 endfacet
 facet normal 0.91 0.30 0.30
  outer loop
   vertex -23.46 5.52 28.98
   vertex -22.25 3.63 27.18
   vertex -22.96 5.60 27.37
  endloop
 endfacet
 facet normal 0.26 -0.96 -0.05
  outer loop
   vertex -23.27 -5.29 39.02
   vertex -24.83 -5.37 32.44
   vertex -20.83 -4.62 38.86
  endloop
 endfacet
 facet normal 0.20 -0.98 -0.01
  outer loop
   vertex -20.83 -4.62 38.86
   vertex -24.83 -5.37 32.44
   vertex -20.84 -4.57 32.16
  endloop
 endfacet
 facet normal 0.54 -0.59 0.60
  outer loop
   vertex -22.69 -2.60 27.34
   vertex -23.38 -3.50 27.08
   vertex -19.40 -2.47 24.51
  endloop
 endfacet
 facet normal 0.16 -0.91 -0.38
  outer loop
   vertex -24.83 -5.37 32.44
   vertex -25.37 -4.24 29.49
   vertex -20.84 -4.57 32.16
  endloop
 endfacet
 facet normal -0.01 -1.00 -0.03
  outer loop
   vertex -22.62 1.50 26.64
   vertex -25.03 1.54 26.19
   vertex -23.54 1.62 22.92
  endloop
 endfacet
 facet normal -0.15 -0.90 -0.40
  outer loop
   vertex -25.37 -4.24 29.49
   vertex -23.38 -3.50 27.08
   vertex -22.52 -4.42 28.80
  endloop
 endfacet
 facet normal -0.41 -0.88 -0.25
  outer loop
   vertex -23.38 -3.50 27.08
   vertex -26.05 -1.96 25.98
   vertex -23.70 -2.14 22.77
  endloop
 endfacet
 facet normal -0.16 -0.91 0.39
  outer loop
   vertex -23.72 -3.30 43.51
   vertex -25.82 -4.07 40.81
   vertex -23.27 -5.29 39.02
  endloop
 endfacet
 facet normal -0.06 0.99 0.12
  outer loop
   vertex -20.74 6.70 37.98
   vertex -25.72 6.88 34.20
   vertex -24.67 6.09 41.03
  endloop
 endfacet
 facet normal -0.37 -0.92 0.10
  outer loop
   vertex -25.82 -4.07 40.81
   vertex -24.83 -5.37 32.44
   vertex -23.27 -5.29 39.02
  endloop
 endfacet
 facet normal -0.36 -0.87 -0.34
  outer loop
   vertex -27.39 -2.41 28.54
   vertex -26.05 -1.96 25.98
   vertex -23.38 -3.50 27.08
  endloop
 endfacet
 facet normal -0.54 -0.84 0.07
  outer loop
   vertex -25.82 -4.07 40.81
   vertex -28.69 -2.83 33.06
   vertex -24.83 -5.37 32.44
  endloop
 endfacet
 facet normal -0.56 -0.80 -0.20
  outer loop
   vertex -24.83 -5.37 32.44
   vertex -28.69 -2.83 33.06
   vertex -25.37 -4.24 29.49
  endloop
 endfacet
 facet normal -0.61 0.77 0.17
  outer loop
   vertex -28.13 5.02 33.46
   vertex -28.52 3.53 38.82
   vertex -24.67 6.09 41.03
  endloop
 endfacet
 facet normal -0.66 -0.74 0.13
  outer loop
   vertex -25.82 -4.07 40.81
   vertex -28.70 -1.83 38.84
   vertex -28.69 -2.83 33.06
  endloop
 endfacet
 facet normal 0.65 0.09 -0.76
  outer loop
   vertex 27.03 3.46 27.96
   vertex 27.10 -0.47 27.53
   vertex 24.69 2.15 25.80
  endloop
 endfacet
 facet normal 0.47 0.85 0.22
  outer loop
   vertex 22.17 5.19 44.80
   vertex 27.20 5.38 33.47
   vertex 24.41 7.05 32.91
  endloop
 endfacet
 facet normal 0.54 0.79 -0.29
  outer loop
   vertex 27.20 5.38 33.47
   vertex 27.03 3.46 27.96
   vertex 24.41 7.05 32.91
  endloop
 endfacet
 facet normal 0.15 0.99 0.08
  outer loop
   vertex 26.88 4.99 38.80
   vertex 27.20 5.38 33.47
   vertex 22.17 5.19 44.80
  endloop
 endfacet
 facet normal 0.52 0.80 -0.30
  outer loop
   vertex 24.41 7.05 32.91
   vertex 27.03 3.46 27.96
   vertex 23.09 5.84 27.42
  endloop
 endfacet
 facet normal 0.61 -0.49 -0.61
  outer loop
   vertex 24.16 -3.89 27.34
   vertex 27.10 -0.47 27.53
   vertex 26.22 -3.16 28.82
  endloop
 endfacet
 facet normal 0.42 0.85 0.30
  outer loop
   vertex 23.27 4.13 46.24
   vertex 26.88 4.99 38.80
   vertex 22.17 5.19 44.80
  endloop
 endfacet
 facet normal 0.52 0.85 -0.05
  outer loop
   vertex 23.09 5.84 27.42
   vertex 27.03 3.46 27.96
   vertex 25.39 4.36 26.25
  endloop
 endfacet
 facet normal 0.63 -0.51 -0.59
  outer loop
   vertex 24.14 -2.60 26.21
   vertex 27.10 -0.47 27.53
   vertex 24.16 -3.89 27.34
  endloop
 endfacet
 facet normal -0.15 -0.03 -0.99
  outer loop
   vertex 24.69 2.15 25.80
   vertex 24.15 0.41 25.94
   vertex 22.82 1.11 26.12
  endloop
 endfacet
 facet normal 0.15 0.75 -0.65
  outer loop
   vertex 23.09 5.84 27.42
   vertex 25.39 4.36 26.25
   vertex 24.58 4.14 25.81
  endloop
 endfacet
 facet normal 0.51 0.83 0.23
  outer loop
   vertex 22.17 5.19 44.80
   vertex 24.41 7.05 32.91
   vertex 21.84 7.00 38.95
  endloop
 endfacet
 facet normal 0.52 0.53 -0.67
  outer loop
   vertex 24.15 0.41 25.94
   vertex 27.10 -0.47 27.53
   vertex 21.62 -2.12 22.03
  endloop
 endfacet
 facet normal 0.05 0.97 -0.23
  outer loop
   vertex 21.70 6.92 31.79
   vertex 24.41 7.05 32.91
   vertex 23.09 5.84 27.42
  endloop
 endfacet
 facet normal 0.39 0.64 -0.66
  outer loop
   vertex 18.84 0.12 22.57
   vertex 24.15 0.41 25.94
   vertex 21.62 -2.12 22.03
  endloop
 endfacet
 facet normal -0.05 1.00 -0.01
  outer loop
   vertex 21.70 6.92 31.79
   vertex 21.84 7.00 38.95
   vertex 24.41 7.05 32.91
  endloop
 endfacet
 facet normal -0.84 0.40 -0.37
  outer loop
   vertex 21.70 6.92 31.79
   vertex 23.09 5.84 27.42
   vertex 22.11 5.06 28.80
  endloop
 endfacet
 facet normal -0.51 0.31 -0.80
  outer loop
   vertex 22.22 3.87 27.21
   vertex 23.09 5.84 27.42
   vertex 24.58 4.14 25.81
  endloop
 endfacet
 facet normal -0.08 1.00 0.04
  outer loop
   vertex 22.22 3.87 27.21
   vertex 24.58 4.14 25.81
   vertex 19.00 3.74 24.02
  endloop
 endfacet
 facet normal 0.32 0.76 -0.57
  outer loop
   vertex 22.82 1.11 26.12
   vertex 24.15 0.41 25.94
   vertex 18.84 0.12 22.57
  endloop
 endfacet
 facet normal -0.84 0.41 -0.36
  outer loop
   vertex 22.11 5.06 28.80
   vertex 23.09 5.84 27.42
   vertex 22.22 3.87 27.21
  endloop
 endfacet
 facet normal 0.00 0.98 -0.22
  outer loop
   vertex 24.58 4.14 25.81
   vertex 22.37 3.43 22.62
   vertex 19.00 3.74 24.02
  endloop
 endfacet
 facet normal 0.06 -0.31 -0.95
  outer loop
   vertex 20.26 3.48 22.48
   vertex 22.37 3.43 22.62
   vertex 22.59 1.54 23.24
  endloop
 endfacet
 facet normal -0.90 0.11 -0.42
  outer loop
   vertex 22.15 0.71 26.54
   vertex 22.22 3.87 27.21
   vertex 22.34 1.45 26.31
  endloop
 endfacet
 facet normal -0.46 -0.16 -0.87
  outer loop
   vertex 22.15 0.71 26.54
   vertex 22.34 1.45 26.31
   vertex 22.82 1.11 26.12
  endloop
 endfacet
 facet normal -0.40 0.90 0.20
  outer loop
   vertex 22.15 0.71 26.54
   vertex 22.82 1.11 26.12
   vertex 18.84 0.12 22.57
  endloop
 endfacet
 facet normal -0.31 -0.39 -0.87
  outer loop
   vertex 21.75 -2.39 26.98
   vertex 24.14 -2.60 26.21
   vertex 21.41 -3.57 27.63
  endloop
 endfacet
 facet normal -0.37 0.88 0.29
  outer loop
   vertex 19.31 4.42 43.53
   vertex 22.17 5.19 44.80
   vertex 21.84 7.00 38.95
  endloop
 endfacet
 facet normal -0.52 0.67 -0.53
  outer loop
   vertex 19.81 4.08 29.79
   vertex 22.11 5.06 28.80
   vertex 22.22 3.87 27.21
  endloop
 endfacet
 facet normal -0.83 0.13 -0.54
  outer loop
   vertex 22.22 3.87 27.21
   vertex 22.15 0.71 26.54
   vertex 21.74 -0.40 26.89
  endloop
 endfacet
 facet normal -0.52 0.83 0.18
  outer loop
   vertex 19.31 4.42 43.53
   vertex 21.84 7.00 38.95
   vertex 19.67 6.58 34.61
  endloop
 endfacet
 facet normal -0.95 0.12 -0.28
  outer loop
   vertex 21.41 -3.57 27.63
   vertex 21.76 -1.78 27.21
   vertex 21.75 -2.39 26.98
  endloop
 endfacet
 facet normal -0.51 0.69 -0.50
  outer loop
   vertex 21.70 6.92 31.79
   vertex 22.11 5.06 28.80
   vertex 19.81 4.08 29.79
  endloop
 endfacet
 facet normal 0.03 0.99 -0.14
  outer loop
   vertex 19.00 3.74 24.02
   vertex 22.37 3.43 22.62
   vertex 20.26 3.48 22.48
  endloop
 endfacet
 facet normal 0.19 0.94 -0.29
  outer loop
   vertex 19.80 0.58 24.64
   vertex 22.15 0.71 26.54
   vertex 18.84 0.12 22.57
  endloop
 endfacet
 facet normal -0.59 0.43 0.69
  outer loop
   vertex 21.74 -0.40 26.89
   vertex 22.15 0.71 26.54
   vertex 19.80 0.58 24.64
  endloop
 endfacet
 facet normal -0.67 -0.18 -0.72
  outer loop
   vertex 18.75 -0.34 29.66
   vertex 21.74 -0.40 26.89
   vertex 21.76 -1.78 27.21
  endloop
 endfacet
 facet normal -0.22 -0.04 -0.97
  outer loop
   vertex 18.84 0.12 22.57
   vertex 21.62 -2.12 22.03
   vertex 18.46 -1.70 22.74
  endloop
 endfacet
 facet normal -0.18 0.98 -0.01
  outer loop
   vertex 19.67 6.58 34.61
   vertex 21.84 7.00 38.95
   vertex 21.70 6.92 31.79
  endloop
 endfacet
 facet normal 0.39 0.86 0.33
  outer loop
   vertex 18.43 4.21 51.70
   vertex 23.27 4.13 46.24
   vertex 22.17 5.19 44.80
  endloop
 endfacet
 facet normal -0.67 0.13 -0.73
  outer loop
   vertex 22.22 3.87 27.21
   vertex 21.74 -0.40 26.89
   vertex 18.75 -0.34 29.66
  endloop
 endfacet
 facet normal -0.70 -0.03 -0.71
  outer loop
   vertex 21.76 -1.78 27.21
   vertex 21.41 -3.57 27.63
   vertex 19.02 -1.97 29.92
  endloop
 endfacet
 facet normal 0.49 0.63 -0.60
  outer loop
   vertex 19.58 8.54 76.35
   vertex 19.93 5.01 72.90
   vertex 18.54 7.21 74.10
  endloop
 endfacet
 facet normal -0.57 0.76 -0.32
  outer loop
   vertex 19.67 6.58 34.61
   vertex 21.70 6.92 31.79
   vertex 18.70 4.53 31.50
  endloop
 endfacet
 facet normal -0.50 0.69 -0.51
  outer loop
   vertex 18.70 4.53 31.50
   vertex 21.70 6.92 31.79
   vertex 19.81 4.08 29.79
  endloop
 endfacet
 facet normal 0.39 0.86 0.33
  outer loop
   vertex 18.43 4.21 51.70
   vertex 20.33 2.84 53.04
   vertex 23.27 4.13 46.24
  endloop
 endfacet
 facet normal -0.68 -0.23 -0.70
  outer loop
   vertex 18.75 -0.34 29.66
   vertex 21.76 -1.78 27.21
   vertex 19.02 -1.97 29.92
  endloop
 endfacet
 facet normal -0.74 -0.54 -0.40
  outer loop
   vertex 19.02 -1.97 29.92
   vertex 21.41 -3.57 27.63
   vertex 17.89 -1.75 31.72
  endloop
 endfacet
 facet normal 0.94 0.32 0.10
  outer loop
   vertex 19.40 8.41 83.74
   vertex 19.60 7.11 85.93
   vertex 19.89 8.80 78.04
  endloop
 endfacet
 facet normal -0.55 -0.79 0.27
  outer loop
   vertex 21.60 -3.52 43.21
   vertex 18.38 -3.05 38.01
   vertex 20.81 -5.34 36.22
  endloop
 endfacet
 facet normal -0.01 0.86 0.51
  outer loop
   vertex 18.19 7.96 84.49
   vertex 19.60 7.11 85.93
   vertex 19.40 8.41 83.74
  endloop
 endfacet
 facet normal -0.21 0.74 0.64
  outer loop
   vertex 18.22 5.83 86.97
   vertex 19.60 7.11 85.93
   vertex 18.19 7.96 84.49
  endloop
 endfacet
 facet normal 0.07 0.58 0.81
  outer loop
   vertex 18.22 5.83 86.97
   vertex 19.64 4.31 87.94
   vertex 19.60 7.11 85.93
  endloop
 endfacet
 facet normal 0.78 0.62 0.07
  outer loop
   vertex 18.49 4.60 58.18
   vertex 19.46 3.33 58.61
   vertex 20.33 2.84 53.04
  endloop
 endfacet
 facet normal -0.32 0.29 -0.90
  outer loop
   vertex 18.54 7.21 74.10
   vertex 19.93 5.01 72.90
   vertex 19.78 1.87 71.95
  endloop
 endfacet
 facet normal -0.67 -0.10 -0.74
  outer loop
   vertex 18.93 2.50 23.81
   vertex 20.26 3.48 22.48
   vertex 19.99 1.49 22.99
  endloop
 endfacet
 facet normal -0.71 0.19 -0.68
  outer loop
   vertex 18.75 -0.34 29.66
   vertex 19.81 4.08 29.79
   vertex 22.22 3.87 27.21
  endloop
 endfacet
 facet normal -0.33 0.94 0.04
  outer loop
   vertex 19.40 8.41 83.74
   vertex 19.89 8.80 78.04
   vertex 18.19 7.96 84.49
  endloop
 endfacet
 facet normal -0.29 0.96 0.05
  outer loop
   vertex 18.19 7.96 84.49
   vertex 19.89 8.80 78.04
   vertex 18.42 8.44 76.34
  endloop
 endfacet
 facet normal -0.09 0.99 -0.13
  outer loop
   vertex 19.89 8.80 78.04
   vertex 19.58 8.54 76.35
   vertex 18.42 8.44 76.34
  endloop
 endfacet
 facet normal -0.07 0.87 -0.48
  outer loop
   vertex 18.42 8.44 76.34
   vertex 19.58 8.54 76.35
   vertex 18.54 7.21 74.10
  endloop
 endfacet
 facet normal 0.64 0.75 -0.15
  outer loop
   vertex 17.68 5.59 55.51
   vertex 20.33 2.84 53.04
   vertex 18.43 4.21 51.70
  endloop
 endfacet
 facet normal -0.75 0.15 -0.64
  outer loop
   vertex 18.93 2.50 23.81
   vertex 19.00 3.74 24.02
   vertex 20.26 3.48 22.48
  endloop
 endfacet
 facet normal -0.90 0.22 0.37
  outer loop
   vertex 19.80 0.58 24.64
   vertex 18.84 0.12 22.57
   vertex 18.46 -1.70 22.74
  endloop
 endfacet
 facet normal 0.73 0.68 0.03
  outer loop
   vertex 18.49 4.60 58.18
   vertex 20.33 2.84 53.04
   vertex 17.68 5.59 55.51
  endloop
 endfacet
 facet normal -0.89 0.44 0.07
  outer loop
   vertex 19.31 4.42 43.53
   vertex 19.67 6.58 34.61
   vertex 17.76 1.94 39.51
  endloop
 endfacet
 facet normal 0.04 -0.02 -1.00
  outer loop
   vertex 19.30 -4.41 0.13
   vertex 18.35 -9.34 0.20
   vertex 16.62 -11.67 0.18
  endloop
 endfacet
 facet normal -0.87 0.49 -0.07
  outer loop
   vertex 17.94 3.99 37.76
   vertex 19.67 6.58 34.61
   vertex 16.93 2.01 36.18
  endloop
 endfacet
 facet normal -0.87 0.50 -0.06
  outer loop
   vertex 16.93 2.01 36.18
   vertex 19.67 6.58 34.