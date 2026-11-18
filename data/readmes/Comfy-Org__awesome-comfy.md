<div align="center">

# Awesome Comfy [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Things people build with ComfyUI: apps and plugins, films and campaigns, Workflows you can run, and the APIs and SDKs for building your own.

![Sections](https://img.shields.io/badge/see%20·%20run%20·%20build%20·%20learn-313131)
![Headings](https://img.shields.io/badge/from-Comfy%20Org%20·%20the%20community-0b8ce9)
![License CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-f0ff41)

</div>

<!--lint disable table-pipe-alignment-->

| | |
| --- | --- |
| **What it is** | A curated list of tools, apps, finished work, Workflows and docs built with ComfyUI. Each entry is one line with one link. |
| **Who it's for** | Artists who want to see what's possible, and engineers who want to know where to start. |
| **How it's organized** | Four parts: see what people make, run it, build on it, and learn. Inside most sections, **From Comfy** and **From the community** say who built each entry. |

Built something with ComfyUI? [Add it](SUBMISSION_GUIDELINES.md). Removals are as welcome as additions.

## Contents

- [01 · How to read this list](#01--how-to-read-this-list)
  - [Installing third-party projects](#installing-third-party-projects)
- [02 · See what people make](#02--see-what-people-make)
  - [Work made with Comfy](#work-made-with-comfy)
  - [Built with Comfy](#built-with-comfy)
- [03 · Run it](#03--run-it)
  - [Getting started](#getting-started)
  - [Workflows](#workflows)
  - [Hosting](#hosting)
- [04 · Build on it](#04--build-on-it)
  - [Build your own](#build-your-own)
  - [Node packs](#node-packs)
  - [Writing your own nodes](#writing-your-own-nodes)
- [05 · Learn](#05--learn)
  - [Learning](#learning)

## 01 · How to read this list

Sections group entries by what you want to do. Inside most sections, entries sit under one of two headings.

| Heading | What it means |
| --- | --- |
| **From Comfy** | Comfy Org's own team built it. Some entries are maintained products with regular releases. Many are demos, example apps or small builds. Ask about an entry on that project's issue tracker. |
| **From the community** | Someone else built it. It's here because it's useful. |
| Not a rating | Neither heading is a quality rating, a safety rating or a support commitment. A heading says who wrote the entry, and nothing more. |
| Partner integrations | Not Comfy Org products. Where a hosted service or partner model sits behind a Comfy API, the API is Comfy Org's and the service is the partner's. |

### Installing third-party projects

Every entry is checked against [the bar](CONTRIBUTING.md): it fits a section, its link resolves, and its description matches what it does. That's the whole check.

| The check is not | What that means for you |
| --- | --- |
| A safety audit | Comfy Org doesn't certify that a listed project is safe, and doesn't control, test or vet its code, models or data. |
| Ongoing | Comfy Org may review a listing, but doesn't promise to keep reviewing it. |
| An endorsement | Being on this list doesn't mean Comfy Org recommends the project. |

> [!WARNING]
> Custom Nodes and apps are executable code, not metadata. They run with the same access as the ComfyUI process that loads them. On a local install, that's your user account, your files and your network. Read the source, check who publishes it, and install it only if you trust it as you'd trust any other software.

If an entry is malicious, misleading or harmful, [report it](https://github.com/Comfy-Org/awesome-comfy/issues/new?template=report-an-entry.yml). That form is how an entry comes off the list. No timeframe is promised. Removing an entry doesn't change the project itself, which stays wherever its author put it.

## 02 · See what people make

Finished work, and the products and apps that run ComfyUI underneath.

### Work made with Comfy

Films, campaigns, games and public art. Each piece is the makers' own work, credited to the people and studios named in its line. Most links go to a write-up on Comfy Org's site, so this section has no affiliation headings.

**Galleries and roundups:**

- [Gallery](https://comfy.org/gallery/) - Community images, video and 3D, each credited to its maker.
- [Made with ComfyUI 2025](https://blog.comfy.org/p/made-with-comfyui-2025-from-open) - A year of work in one place, from open-source releases to brand campaigns.
- [Customer stories](https://comfy.org/customers/) - Studios, brands, artists and universities, with a [machine-readable index](https://comfy.org/customers/llms.txt).

**Film and television:**

- [The Song of Drifters](https://comfy.org/customers/xindi-zhang/) - Xindi Zhang built her USC thesis film in ComfyUI, using her own illustrations as the style guide ([in her own words](https://blog.comfy.org/p/the-tool-that-expands-my-art-xindi)). It won a Golden Award at the [Student Academy Awards](https://www.usf.edu/arts/news/2025/20251106-from-thesis-to-oscars-shortlist-xindi-zhang-ai-driven-film-wins.aspx).
- [YUI](https://comfy.org/customers/hakoniwa-yui/) - A 4:20 animated short by 852話 Hakoniwa, made in three days of focused work. ([longer write-up](https://blog.comfy.org/p/creating-the-story-of-yui-with-852))

**Advertising and campaigns:**

- [Svedka, Shake Your Bots Off](https://comfy.org/customers/svedka-silverside/) - Silverside AI rebuilt Svedka's lost Fembot on ComfyUI Workflows for a Super Bowl LX spot.
- [Groove Jones, Dick's Sporting Goods](https://comfy.org/customers/groove-jones/) - A hyper-realistic faux out-of-home holiday campaign for the Crocs x NFL collection, delivered against a short deadline.
- [Don Diablo, Blackout](https://www.youtube.com/watch?v=cPMNIIZkNIs) - Music video whose image work, including identity modelling and stylization, was done locally in ComfyUI. ([write-up](https://blogs.nvidia.com/blog/rtx-ai-garage-don-diablo-gen-ai-music-video))

**Games:**

- [ComfyCrawler](https://mowmeow.net/ComfyCrawlerTest/) - A dungeon crawler in a Windows 95 interface, with its art and music generated in ComfyUI. The hosted build is a read-only edition.

**Studios and 3D:**

- [Series Entertainment](https://comfy.org/customers/series-entertainment/) - Over 100,000 assets across multiple Netflix titles, kept consistent by repeatable Workflows. ([case study](https://blog.comfy.org/p/case-study-how-series-entertainment))
- [Ubisoft CHORD](https://comfy.org/customers/ubisoft-chord/) - Ubisoft La Forge open-sourced its PBR material estimation model with ComfyUI Custom Nodes. ([announcement](https://blog.comfy.org/p/ubisoft-open-sources-the-chord-model))

**Public art and installations:**

- [Moment Factory](https://comfy.org/customers/moment-factory/) - Rebuilt a 3D projection mapping pipeline for architectural-scale work. ([case study](https://blog.comfy.org/p/case-study-how-moment-factory-reimagined))
- [Ina Conradi's NTU students](https://comfy.org/customers/ina-conradi/) - Ninety-second films for building-sized LED walls, shown at Hangzhou's West Lake media facade.
- [Echoes of Time](https://blog.comfy.org/p/echoes-of-time-lighting-up-a-historic) - A projection piece on Niš Fortress, produced through a Comfy Org community challenge.

**Studios on their own pipelines**, recorded talks:

- [Reinventing the Production Pipeline](https://comfy.org/events/production-pipeline/) - Erin Sarofsky and Ryan Summers of Sarofsky on rebuilding a studio pipeline around ComfyUI.
- [Beyond the Models](https://comfy.org/events/beyond-the-models/) - Building custom Workflows for commercial and film production.
- [The Future of AI Post Production](https://comfy.org/events/future-ai-post-production/) - Ingi Erlingsson on custom LoRAs and motion graphics Nodes in post.
- [How Black Math built a hackathon in three weeks](https://comfy.org/events/black-math-hackathon/) - A design studio shipping an event-scale build.
- [Silverside AI](https://comfy.org/customers/videos/silverside-ai/) - Why Node-based Workflows give a creative team more control than single-prompt tools.
- [Black Math](https://comfy.org/customers/videos/black-math/) - Artists and technical directors on building extendable creative systems while keeping art direction.

**Teaching:**

- [Golan Levin, Carnegie Mellon](https://comfy.org/customers/golan-levin/) - "It's an image-processing workstation for completely new kinds of work."
- [Kathy Smith, USC](https://comfy.org/customers/kathy-smith/) - Inside the Expanded Animation MFA that built a curriculum around it.
- [UAL Creative Computing Institute](https://comfy.org/customers/ual-cci/) - A teaching and research partnership across masters, PhD and industry programmes.

**Events:**

- [Events](https://comfy.org/events/) - Livestreams, hackathons and meetups, scheduled and recorded, with a [machine-readable index](https://comfy.org/events.md).

### Built with Comfy

Products, tools and apps that run ComfyUI underneath.

#### From the community

Plugins that put ComfyUI inside the tools you already use, and apps built on top of your own ComfyUI. All of it is third-party code, so read **Installing third-party projects** under How to read this list first.

**Tools that bring ComfyUI to another solution:**

- [krita-ai-diffusion](https://github.com/Acly/krita-ai-diffusion) - Inpainting, outpainting and live painting inside Krita, against a local or remote ComfyUI server.
- [OpenLayer](https://mehran-ahmadi.com/OpenLayer/) - A Photoshop panel that generates, inpaints and upscales through your own ComfyUI server and hands back editable layers. Alpha.
- [StableGen](https://github.com/sakalond/StableGen) - A Blender addon that textures 3D meshes through a ComfyUI backend using multi-view projection.
- [ComfyUI-for-Nuke](https://github.com/vinavfx/ComfyUI-for-Nuke) - Builds and runs ComfyUI graphs inside Foundry Nuke, against your own ComfyUI server.
- [ComfyUI-TD](https://github.com/JiSenHua/ComfyUI-TD) - Streams images, video, point clouds and audio from ComfyUI into TouchDesigner in real time.
- [SwarmUI](https://github.com/mcmonkeyprojects/SwarmUI) - A forms-first front end over the same engine, with a ComfyUI Workflow tab when you want the graph back.
- [ComfyUI-Blender](https://github.com/alexisrolland/ComfyUI-Blender) - A Blender add-on and Custom Nodes that build a Blender panel from an exported Workflow's input and output Nodes, then run it on your ComfyUI server.
- [Comfy-for-Unreal-Engine](https://github.com/XXJones21/Comfy-for-Unreal-Engine) - An Unreal Engine 5.8 plugin that runs ComfyUI Workflows from the editor, Blueprints, Python and agents, on a local ComfyUI or Comfy Cloud, and imports the results as textures, sounds and meshes.

**Apps on top of your own ComfyUI:**

- [ComfyTV](https://github.com/jtydhr88/ComfyTV) - Turns ComfyUI into a canvas app where each stage is its own Node, across image, video, audio and 3D.
- [Velorn](https://velorn.ai) - An open-source desktop video workstation that runs any ComfyUI Workflow on a timeline, locally or in the cloud. ([source](https://github.com/VelornLabs/velorn))
- [ComfyLink](https://comfylink.app) - An iOS and Android remote for your own ComfyUI machine, paired through a Custom Node you install in ComfyUI. ([the Custom Node](https://github.com/huijiutian/ComfyUI-ComfyLink))
- [ComfyUI Metadata Viewer](https://huggingface.co/spaces/QES/ComfyUI_Metadata_Viewer) - Drop a ComfyUI output file in the browser and read back the models, parameters and prompt embedded in it.

#### From Comfy

**Hosted apps you can open:**

- [Emojinius](https://emojinius.comfy.org) - Upload a character and get back a pack of animated Slack emojis. Needs your own Comfy API Key, and generation is billed to your account.
- [Cinematic Studio](https://comfy.org/hub/apps/cinematic-studio/) - Direct a shot with a real camera, light and grade it, then run it on any image model.
- [Openjutsu](https://comfy.org/hub/apps/openjutsu/) - Swap the main person in a 5 to 15 second clip for the character in one image, keeping the scene, motion and sound. Runs MiniMax H3, needs a Comfy account, and bills runs in Comfy Credits.

**Clonable app guides**, a working app plus a walkthrough of how it's wired:

- [comfy-cinematic-studio](https://github.com/Comfy-Org/comfy-cinematic-studio) - Source and development guide for Cinematic Studio above.
- [comfy-reshoot](https://github.com/Comfy-Org/comfy-reshoot) - An app that deploys a Workflow, built to be cloned and changed.
- [comfy-openjutsu](https://github.com/Comfy-Org/comfy-openjutsu) - Source and development guide for Openjutsu above, run on your own Comfy deployment.

**Example apps:**

- [comfy-examples](https://github.com/Comfy-Org/comfy-examples) - Thirteen smaller apps, each a handful of files behind a deploy button: a Discord image bot, object removal, virtual try-on, sketch to image, profile shots and more.

## 03 · Run it

Install ComfyUI, open a Workflow, and find a GPU when you don't have one.

### Getting started

Pick an install path, run your first Workflow, and know where to look when something breaks.

#### From Comfy

- [ComfyUI](https://github.com/Comfy-Org/ComfyUI) - The Node graph engine itself: a Workflow runner for diffusion models with a Python backend.
- [Download page](https://comfy.org/download) - Picks the install path for your machine. Check the [system requirements](https://docs.comfy.org/installation/system_requirements) first.
- [Comfy Desktop](https://docs.comfy.org/installation/desktop/overview) - Packaged installer for Windows, macOS and Linux. The shortest path to a working setup.
- [Comfy Desktop source](https://github.com/Comfy-Org/Comfy-Desktop) - Source for Comfy Desktop, which installs and manages several ComfyUI setups side by side.
- [Manual install](https://docs.comfy.org/installation/manual_install) - Clone and pip, for when you want to control the Python environment. Windows also has a [portable build](https://docs.comfy.org/installation/comfyui_portable_windows): one folder, no installer, no system Python.
- [Your first generation](https://docs.comfy.org/get_started/first_generation) - Walks a default Workflow end to end and explains what each Node did. The [interface tour](https://docs.comfy.org/interface/overview) covers the canvas, the queue and the model library.
- [Comfy Cloud](https://docs.comfy.org/get_started/cloud) - Hosted ComfyUI, for when you don't have the GPU.
- [comfy-cli](https://github.com/Comfy-Org/comfy-cli) - Command-line installer and manager for ComfyUI, models and Custom Nodes. [Its docs](https://docs.comfy.org/comfy-cli/getting-started) cover launching, snapshots and switching versions.
- [Troubleshooting](https://docs.comfy.org/troubleshooting/overview) - Start here when something breaks, before you open an issue.

### Workflows

Graphs you can open and run, and the format they're saved in.

#### From Comfy

- [Comfy Workflows](https://comfy.org/workflows) - Browsable catalogue of runnable Workflows with the models each one needs, including walkthroughs for [character replacement](https://comfy.org/workflows/use-cases/ai-character-replacement/), [image to video](https://comfy.org/workflows/use-cases/ai-image-to-video/), [sprite sheets](https://comfy.org/workflows/use-cases/sprite-sheet-generator/), [photo restoration](https://comfy.org/workflows/use-cases/restore-old-photos/) and [image to 3D](https://comfy.org/workflows/use-cases/image-to-3d/).
- [workflows](https://github.com/Comfy-Org/workflows) - Comfy Org's Workflows from posts on X, Discord, LinkedIn and Reddit, each with a Comfy Cloud link and a version for Comfy Desktop or a local ComfyUI.
- [workflow_templates](https://github.com/Comfy-Org/workflow_templates) - The source of the templates that ship inside ComfyUI. Open a pull request here to add one.
- [Using templates](https://docs.comfy.org/interface/features/template) - How the built-in template browser works.
- [Workflow JSON spec](https://docs.comfy.org/specs/workflow_json) - The on-disk format, for reading or writing Workflows programmatically.
- [API Workflow format](https://docs.comfy.org/development/api-development/workflow-api-format) - The flattened form you POST to a server.

### Hosting

Run ComfyUI on someone else's GPU, by renting one or deploying an image.

#### From Comfy

- [Self-hosting guide](https://docs.comfy.org/development/deploy/self-hosting) - Running ComfyUI on a rented GPU.

#### From the community

Independent providers and container images, each run by the people who built it. Comfy Org doesn't operate them, hold your data or set their prices. **Installing third-party projects** applies.

- [ComfyUI-Docker](https://github.com/YanWenKun/ComfyUI-Docker) - Container images across several CUDA and Python combinations.
- [SaladCloud](https://docs.salad.com/container-engine/how-to-guides/ai-machine-learning/deploy-stable-diffusion-comfy) - Deploy image and video generation with ComfyUI on their container engine.
- [comfyui-api](https://github.com/SaladTechnologies/comfyui-api) - A stateless API server in front of ComfyUI that returns images or sends them to webhooks and S3, built for horizontal scaling.

## 04 · Build on it

Drive ComfyUI from your own code, and write Custom Nodes for it.

### Build your own

The API surfaces, SDKs and hosted endpoints for driving ComfyUI from your own code.

#### From Comfy

- [Development overview](https://docs.comfy.org/development/overview) - Map of the API surfaces and which one you want.
- [API quickstart](https://docs.comfy.org/development/api-development/quickstart) - Submit a Workflow and collect the result in a few calls, once you have [a Comfy API Key](https://docs.comfy.org/development/api-development/getting-an-api-key).

**Comfy Router**, one API in front of many hosted image, video and audio models:

- [Router quickstart](https://docs.comfy.org/development/comfy-router/quickstart) - One POST, no graph to build. The [API reference](https://docs.comfy.org/development/comfy-router/api) covers run, queue, poll and cancel.
- [Model catalogue](https://docs.comfy.org/development/comfy-router/models) - Every model it can run, with per-model input and output schemas.
- [Pricing](https://docs.comfy.org/development/comfy-router/pricing) - Per-model cost. Check it before you build on a model.

**Developer Platform**, for running your own Workflows as a service:

- [Cloud API overview](https://docs.comfy.org/development/cloud/overview) - Assets, jobs, queue and history on hosted ComfyUI.
- [Serverless overview](https://docs.comfy.org/development/serverless/overview) - Turn a Workflow into an endpoint you can call.

**SDKs**, which [cover the same ground in the same shape](https://docs.comfy.org/development/api-development/sdks):

- [Python SDK](https://github.com/Comfy-Org/comfy-python-sdk) - Client for self-hosted ComfyUI and Comfy Cloud.
- [TypeScript SDK](https://github.com/Comfy-Org/comfy-typescript-sdk) - Node client for the Comfy API v2, against Comfy Cloud, serverless or a self-hosted proxy.
- [Swift SDK](https://github.com/Comfy-Org/comfy-swift-sdk) - Thin client: submit, stream, collect outputs.

**Comfy MCP:**

- [Comfy MCP](https://comfy.org/mcp) - The hosted endpoint and what it can do.
- [comfy-mcp](https://github.com/Comfy-Org/comfy-mcp) - Exposes a local ComfyUI over the Model Context Protocol.
- [MCP documentation](https://docs.comfy.org/agent-tools/mcp) - Setup and the tools the server exposes.

**Talking to a ComfyUI server directly:**

- [Server API overview](https://docs.comfy.org/development/comfyui-server/comms_overview) - The REST and WebSocket model the editor itself uses, with a [reference for every route](https://docs.comfy.org/development/comfyui-server/comms_routes) and [working scripts](https://docs.comfy.org/development/comfyui-server/api-examples) for queueing prompts and reading results.
- [comfy-api-proxy](https://github.com/Comfy-Org/comfy-api-proxy) - Puts the v2 API in front of a self-hosted ComfyUI, so one client works against both.

#### From the community

Other people's libraries for driving ComfyUI from code. **Installing third-party projects** applies.

**Writing Workflows as code:**

- [ComfyScript](https://github.com/Chaoses-Ib/ComfyScript) - Write Workflows as Python instead of JSON.
- [ComfyUI-to-Python-Extension](https://github.com/pydn/ComfyUI-to-Python-Extension) - Exports a saved Workflow as a standalone Python script.

### Node packs

Custom Nodes are how ComfyUI grows, and there are thousands of them. The Comfy Registry ranks them by install count, with search, versions and security scanning, so browse there instead of a fixed list. Custom Nodes run inside your ComfyUI process, so read **Installing third-party projects** first.

**Find and install them with:**

- [ComfyUI Manager](https://github.com/Comfy-Org/ComfyUI-Manager) - Installs, updates, disables and security-scans Custom Node packs from inside ComfyUI. The usual way to install them.
- [Comfy Registry](https://registry.comfy.org/) - The package index for Custom Nodes, searchable and ranked by install count. Start here rather than with a clone URL from a comment.
- [Registry overview](https://docs.comfy.org/registry/overview) - What the Comfy Registry is, and how versions and publishers work.
- [Publishing to the registry](https://docs.comfy.org/registry/publishing) - For authors shipping a Custom Node pack, with the [standards](https://docs.comfy.org/registry/standards) a pack follows and [CI/CD](https://docs.comfy.org/registry/cicd) for publishing on tag.
- [Installing Custom Nodes](https://docs.comfy.org/installation/install_custom_node) - The manual route, and what it writes to disk.
- [Custom Node troubleshooting](https://docs.comfy.org/troubleshooting/custom-node-issues) - Import errors, dependency conflicts and how to bisect them.

### Writing your own nodes

Write a Custom Node of your own, from an empty folder to a published pack.

#### From Comfy

- [Custom Node overview](https://docs.comfy.org/custom-nodes/overview) - Start here for your first Custom Node.
- [Walkthrough](https://docs.comfy.org/custom-nodes/walkthrough) - Builds a working Custom Node from an empty folder.
- [Server-side reference](https://docs.comfy.org/custom-nodes/backend/server_overview) - `INPUT_TYPES`, `RETURN_TYPES`, `FUNCTION`, lifecycle and the rest of the contract.
- [Datatypes](https://docs.comfy.org/custom-nodes/backend/datatypes) - The type system that decides which sockets connect.
- [Shipping templates with a pack](https://docs.comfy.org/custom-nodes/workflow_templates) - So users get an example Workflow on install.
- [ComfyUI_frontend](https://github.com/Comfy-Org/ComfyUI_frontend) - The Vue front end the editor runs on.
- [comfyui-native-port-guide](https://github.com/Comfy-Org/comfyui-native-port-guide) - Conventions for adding native model support to core, rather than wrapping it in a Custom Node pack.
- [embedded-docs](https://github.com/Comfy-Org/embedded-docs) - The help pages shown inside the editor for core Nodes, and how to add yours.
- [comfy-model-tools](https://github.com/Comfy-Org/comfy-model-tools) - Scripts for merging, converting and quantizing model files for ComfyUI.
- [comfyui-benchmark](https://github.com/Comfy-Org/comfyui-benchmark) - Extension for measuring generation performance across configurations.

## 05 · Learn

Where to read, watch and ask once you're past the first run.

### Learning

#### From Comfy

- [Official documentation](https://docs.comfy.org/) - The reference for installation, Nodes, models and the APIs.
- [llms.txt](https://docs.comfy.org/llms.txt) - The full documentation index as one plain-text file. Search it to find a page.
- [Nodes](https://docs.comfy.org/basic-concepts/nodes) and [models](https://docs.comfy.org/basic-concepts/models) - The two concepts everything else is built on.
- [Basic tutorials](https://docs.comfy.org/tutorials/basic/text-to-image) - Text to image, image to image, inpaint, outpaint, upscale and LoRA, as annotated Workflows.
- [Blog](https://blog.comfy.org/) - Official release notes, case studies and announcements.
- [Forum](https://forum.comfy.org/) - Longer questions and answers that outlast a chat message.
- [Discord](https://discord.com/invite/comfyorg) - Where most day-to-day help happens.
- [YouTube](https://www.youtube.com/@comfyorg) - Official walkthroughs and release videos.
- [Community links](https://docs.comfy.org/community/links) - The official list of community spaces.
- [Contributing to ComfyUI](https://docs.comfy.org/community/contributing) - How to get a change into core.

#### From the community

- [Nerdy Rodent](https://www.youtube.com/@NerdyRodent) - Regular walkthroughs of model releases and Workflows.
