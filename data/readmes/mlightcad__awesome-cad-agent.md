
# Awesome CAD Agent

A curated list of open-source projects that connect CAD (Computer-Aided Design) with AI agents, including AI-native CAD applications, MCP servers, autonomous CAD agents, agent skills, and harness plugins.

This list focuses on practical tools and technologies that enable AI agents to understand, create, inspect, edit, and automate CAD models and engineering drawings.

This project is the agent-focused companion of [Awesome CAD](https://github.com/mlightcad/awesome-cad).

Inspired by the [awesome-list](https://github.com/sindresorhus/awesome) philosophy.

## Contents

- [AI-Native CAD Applications](#-ai-native-cad-applications)
- [CAD MCP Servers](#-cad-mcp-servers)
  - [General CAD](#general-cad)
  - [AutoCAD and DWG/DXF](#autocad-and-dwgdxf)
  - [FreeCAD](#freecad)
  - [SolidWorks](#solidworks)
  - [Rhino](#rhino)
  - [Onshape](#onshape)
  - [KiCad](#kicad)
  - [OpenSCAD](#openscad)
- [CAD Agents & Agentic Workflows](#-cad-agents--agentic-workflows)
- [CAD Agent Skills](#-cad-agent-skills)
- [CAD Harness Plugins](#-cad-harness-plugins)
- [CAD Agent Infrastructure & SDKs](#-cad-agent-infrastructure--sdks)
- [CAD Benchmarks & Evaluation](#-cad-benchmarks--evaluation)
- [CAD AI Research](#-cad-ai-research)
- [Contributing](#-contributing)

---

## 🤖 AI-Native CAD Applications

CAD applications designed with AI agents and programmatic interaction as first-class capabilities, rather than adding a chatbot to an existing CAD interface.

### Parametric CAD

#### SolidCraft

https://github.com/tangency-labs/solidcraft

An open-source parametric 3D CAD application built in Rust, providing desktop, web, and agent automation capabilities.

Key Features

- Rust-based parametric B-Rep modeling kernel
- Desktop and browser-based CAD applications
- MCP server for AI agent integration
- CLI and programmatic modeling interfaces
- Parametric sketches, Boolean operations, fillets, and chamfers
- STEP import/export and other geometry formats

#### vcad

https://github.com/muni-works/vcad

An open-source parametric CAD system for the AI era, designed for both human users and autonomous agents.

Key Features

- Rust/WebAssembly B-Rep geometry kernel
- Dedicated `@vcad/mcp` server
- CAD document creation, inspection, and export
- Parametric sketching and solid modeling
- Assembly joints and forward kinematics
- Gym-style simulation interface for agent interaction
- Web, desktop, and CLI applications

### 2D / 3D CAD

#### CADCraft

https://github.com/storytold/cadcraft

An open-source, clean-room reimplementation of AutoCAD in Rust, with agent-friendly automation interfaces.

Key Features

- AutoCAD-style command-line workflow
- Native DXF and DWG read/write
- MCP server and JSON control channel
- Layers, blocks, dimensions, hatches, and object snaps
- Parametric geometric and dimensional constraints
- Cross-platform desktop and WebAssembly applications

#### OpenCAD Studio

https://github.com/HakanSeven12/OpenCADStudio

An open-source 2D drafting and 3D modeling application built in Rust, with native DWG/DXF support.

Key Features

- Native DWG/DXF read/write
- 2D drafting and 3D solid modeling
- MCP endpoint for AI agents
- Headless automation and plugin system
- GPU-accelerated rendering
- Cross-platform desktop and web applications

#### MLightCAD

https://github.com/mlightcad/cad-viewer

A fully web-based DWG/DXF viewer and editor that runs entirely in the browser, with a plugin architecture that includes an official AI assistant.

Key Features

- Browser-native DWG/DXF parsing, editing, and rendering with no backend
- Plugin system with official AI assistant and HTML/PDF/SVG export plugins
- AutoCAD-style command line and 2D drafting workflows
- High-performance WebGL/THREE.js rendering of large drawings
- Programmatic integration through npm packages or one-line iframe embed
- Desktop and mobile browser support with touch gestures

---

## 🔌 CAD MCP Servers

MCP (Model Context Protocol) servers expose CAD application functionality and data to AI agents through standardized tools and resources.

### General CAD

#### CAD-MCP

https://github.com/daobataotie/CAD-MCP

A general-purpose CAD MCP server that enables AI assistants to interact with CAD modeling workflows.

Key Features

- CAD operations exposed through MCP
- Natural-language-driven CAD workflows
- Integration with MCP-compatible AI assistants
- Open-source Python implementation

#### CAD-Agent-Hub

https://github.com/Cai-aa/CAD-Agent-Hub

A collection of MCP servers and automation bridges for professional mechanical CAD applications.

Key Features

- CATIA V5 MCP server
- SolidWorks MCP server
- Siemens NX/UG MCP server
- Autodesk Fusion integration
- Engineering automation examples and reusable skills
- Windows-based CAD application integration

### AutoCAD and DWG/DXF

#### AutoCAD-MCP

https://github.com/U-C4N/Autocad-MCP

An AutoCAD MCP server for AI agents, supporting both live AutoCAD automation and headless DWG/DXF workflows.

Key Features

- 240+ CAD tools for drawing creation and editing
- Live AutoCAD automation through Windows COM
- Headless DXF operations using ezdxf
- Entity inspection and modification
- Mechanical drafting and engineering drawing workflows
- P&ID and floor-plan automation

### FreeCAD

#### FreeCAD MCP

https://github.com/neka-nat/freecad-mcp

An MCP server that connects AI assistants to FreeCAD for parametric 3D modeling and engineering automation.

Key Features

- FreeCAD workbench integration
- Create and modify parametric CAD documents
- Execute FreeCAD Python commands
- Retrieve model information and viewport images
- Support for engineering workflows and FEM operations
- Compatible with MCP-based AI clients

#### FreeCAD MCP (ContextForm)

https://github.com/contextform/freecad-mcp

An alternative FreeCAD MCP implementation providing an AI automation bridge to FreeCAD.

Key Features

- FreeCAD API integration
- CAD document and object operations
- AI assistant integration
- Python-based automation

#### FreeCAD Robust MCP Server

https://github.com/spkane/freecad-addon-robust-mcp-server

A FreeCAD MCP integration focused on providing a robust connection between AI agents and the FreeCAD application.

Key Features

- FreeCAD add-on integration
- MCP server and application bridge
- CAD automation workflows
- Support for AI-driven modeling

### SolidWorks

#### SolidWorks Automation Skill

https://github.com/wzyn20051216/solidworks-automation-skill

An AI Skill and MCP toolkit for reliable desktop CAD automation with SolidWorks.

Key Features

- SolidWorks automation through Python and COM
- Part, assembly, and drawing operations
- MCP tools and reusable agent skills
- Codex, Claude Code, Cursor, and other agent integrations
- Execution tracing and result verification
- CAD Studio desktop automation environment

#### mcp-server-solidworks

https://github.com/eyfel/mcp-server-solidworks

An MCP server that integrates with the SolidWorks API and exposes CAD functionality to AI assistants.

Key Features

- SolidWorks API integration
- CAD planning and execution workflow
- MCP-based tool interfaces
- Python-based automation

#### Solidworks-MCP

https://github.com/alisamsam/solidworks-mcp

An MCP server for automating SolidWorks through Claude and other MCP-compatible assistants.

Key Features

- SolidWorks COM API integration
- Part and sketch creation
- Feature modeling and modification
- AI-driven CAD automation

### Rhino

#### RhinoMCP

https://github.com/jingcheng-chen/rhinomcp

Connects Rhino 3D and Grasshopper to AI agents through the Model Context Protocol.

Key Features

- Control Rhino through natural language
- Create and modify 3D geometry
- Interact with Grasshopper definitions
- Read Rhino document information
- Capture viewport images
- Reusable modeling guidance and verification workflows

### Onshape

#### Jarvis Onshape MCP

https://github.com/ReshefElisha/jarvis-onshape-mcp

An Onshape MCP integration and Claude Code plugin for AI-driven parametric CAD modeling.

Key Features

- Onshape document and feature operations
- Vision-guided geometry decomposition
- Parametric modeling and iteration
- FeatureScript integration
- Agent skill and Claude Code plugin
- Automated modeling workflows

### KiCad

#### KiCad MCP

https://github.com/lamaalrajih/kicad-mcp

An MCP server for controlling KiCad across macOS, Windows, and Linux.

Key Features

- KiCad PCB and schematic automation
- Component and footprint inspection
- Board editing and routing operations
- Electrical connectivity analysis
- MCP-compatible AI assistant integration

### OpenSCAD

#### OpenSCAD MCP

https://github.com/RobertCoop/openscad-mcp

An MCP server for OpenSCAD that enables AI agents to create, modify, and render script-based 3D models.

Key Features

- OpenSCAD script generation and editing
- Model rendering and inspection
- Geometry automation
- MCP integration
- OpenSCAD design agent skill
- Claude Code plugin support

---

## 🧠 CAD Agents & Agentic Workflows

Projects that provide higher-level autonomous CAD capabilities, including task planning, model generation, iterative refinement, execution, and validation.

#### CADAM

https://github.com/Adam-CAD/CADAM

An open-source AI-powered text-to-CAD application that transforms natural-language descriptions and images into parametric 3D models.

Key Features

- Natural-language-to-CAD generation
- Image-assisted 3D modeling
- Parametric model generation
- Interactive model refinement
- Browser-based 3D preview
- STL and OpenSCAD export

#### FreeCAD AI

https://github.com/ghbalf/freecad-ai

An AI-powered assistant workbench for FreeCAD that generates 3D models from natural-language instructions.

Key Features

- Natural-language-driven 3D modeling
- FreeCAD workbench integration
- LLM-based CAD generation
- Support for multiple AI providers
- Local model integration through Ollama

#### Forgent3D

https://github.com/forgent3d/forgent3d-desktop

A local AI CAD companion for building, previewing, and iterating parametric 3D models with coding agents.

Key Features

- Parametric part and assembly modeling
- Python-based build123d integration
- Live model preview and rebuild loop
- Geometry validation and measurements
- Agent integration through skills and MCP

Note: The desktop repository is currently in maintenance mode. See the separate [Forgent3D Skills](https://github.com/forgent3d/forgent3d-skills) project for its newer lightweight agent workflow.

#### MAC (Multi-Agent CAD)

https://github.com/Pan-Chera/Multi-Agent-CAD

A decoupled multi-agent framework from Tsinghua University that turns natural-language design briefs into editable CAD parts and multi-component assemblies.

Key Features

- Multi-agent pipeline for planning, geometry, coding, repair, and an independent Judge
- Single-part Text-to-CAD workflow with visual and geometric in-loop verification
- Experimental natural-language assembly generation with joint mating and part reuse
- Editable STEP, STL, GLB export, plus URDF handoff for robotics simulation
- Auditable structured briefs, geometry plans, measurements, and QA reports
- Browser-based UI with 3D preview and downloadable results
- Built on build123d, LangGraph, and Aider

---

## 🧩 CAD Agent Skills

Reusable instructions, domain knowledge, and workflows that teach AI agents how to perform CAD-related tasks.

#### text-to-cad

https://github.com/earthtojake/text-to-cad

A collection of agent skills for CAD, robotics, and hardware design.

Key Features

- Natural-language and image-driven CAD generation
- Parametric modeling using build123d and OpenCascade
- STEP, STL, 3MF, DXF, and GLB export
- CAD model inspection and visualization
- Robot description generation (URDF, SRDF, SDF)
- 3D printing and fabrication workflows
- Installation through Skills CLI, Codex, and Claude Code

#### SolidWorks Automation Skill

https://github.com/wzyn20051216/solidworks-automation-skill

An AI Skill toolkit for automating SolidWorks engineering workflows.

Key Features

- Part and assembly modeling
- Engineering drawing generation
- CAD export and conversion
- Modeling verification and review
- Reusable subskills for specialized operations
- MCP integration for tool execution

#### SimpleCADAPI Agent Skill

https://github.com/PhySpace/SimpleCADAPI

A bundled agent skill that teaches coding agents the SimpleCADAPI parametric modeling discipline.

Key Features

- Installable into agent harnesses via `sca skill install`
- Feature Tree Convention for verifier-first staged modeling
- Geometry-grounding selection and deterministic face tagging practices
- Recorded, replayable agent sessions with full tool-call transcripts
- Editor collaboration workflow for viewport picks and cell references

---

## 🧰 CAD Harness Plugins

Plugins and extensions that integrate CAD capabilities into AI coding agents and agent runtimes such as Claude Code, Codex, and other harness environments.

#### text-to-cad

https://github.com/earthtojake/text-to-cad

Provides provider-native plugins for installing CAD skills into coding-agent environments.

Key Features

- Claude Code plugin marketplace integration
- Codex plugin installation
- CAD skill and workflow integration
- Local project-based CAD generation
- Reusable instructions for agent-driven CAD development

#### Jarvis Onshape MCP

https://github.com/ReshefElisha/jarvis-onshape-mcp

A Claude Code plugin that connects coding agents to Onshape CAD through MCP.

Key Features

- Claude Code plugin manifest
- Onshape MCP integration
- Vision-guided modeling skill
- Parametric feature iteration
- Reusable CAD automation workflows

#### OpenSCAD MCP

https://github.com/RobertCoop/openscad-mcp

An MCP integration that also provides a Claude Code plugin and OpenSCAD-specific agent skill.

Key Features

- Claude Code plugin support
- OpenSCAD design skill
- MCP-based modeling operations
- Script generation and rendering

---

## 🏗 CAD Agent Infrastructure & SDKs

Developer tools and reusable interfaces that make CAD systems easier for AI agents to operate, inspect, and validate.

This category focuses on the underlying execution and integration layer rather than complete agent applications.

#### CAD-Agent-Hub

https://github.com/Cai-aa/CAD-Agent-Hub

A multi-CAD automation toolkit providing reusable MCP connectors and application bridges for engineering software.

Key Features

- CATIA, SolidWorks, Siemens NX, and Fusion integrations
- Reusable automation bridges
- MCP-based application interfaces
- Engineering workflow examples

#### vcad

https://github.com/muni-works/vcad

Provides a Rust/WebAssembly B-Rep kernel and a programmatic CAD interface designed for both applications and AI agents.

Key Features

- Rust-based geometry kernel
- TypeScript and CLI interfaces
- MCP integration
- Parametric modeling operations
- CAD inspection and export APIs
- Simulation and agent-oriented interaction

#### SimpleCADAPI

https://github.com/PhySpace/SimpleCADAPI

An agent-native, OpenCASCADE-based Python SDK for language models to create, inspect, and reconstruct complex, editable 3D models.

Key Features

- Parametric models as code notebooks with named parameters and physical units
- Functional B-Rep modeling operations on a C++ OpenCASCADE engine
- QL selectors for geometry grounding and stable feature selection
- Replayable operation graphs with JSON export and replay
- Semantic tags, STEP AP242/STL export, and editable FreeCAD package translation
- Agent-oriented STEP/BREP reconstruction with stable entity IDs and measured acceptance gates

---

## 📏 CAD Benchmarks & Evaluation

Benchmarks, datasets, and leaderboards for measuring how well AI agents and LLMs understand, generate, and edit CAD models.

#### CADGenBench

https://huggingface.co/spaces/HuggingAI4Engineering/CADGenBench

A public benchmark and leaderboard for CAD generation and editing, evaluating AI systems through tool-agnostic STEP/BREP artifact submissions.

Key Features

- CAD generation and editing task tracks
- Tool-agnostic STEP/BREP submission protocol
- Hosted evaluation pipeline on Hugging Face Spaces
- Public leaderboard comparing LLMs and CAD agent toolchains
- Used to evaluate MCP-based CAD modeling stacks

#### BenchCAD

https://github.com/BenchCAD/BenchCAD-main

An execution-grounded benchmark for evaluating whether models can understand and write parametric CadQuery code for real mechanical parts.

Key Features

- 17,900 execution-verified CadQuery programs across 106 industrial part families
- Parts drawn from 47 engineering standards (ISO, DIN, EN, ASME, IEC)
- Vision2Code, CodeEdit, Vision-QA, and Code-QA tasks
- Deterministic execution-based scoring via voxel IoU, with no LLM judge
- One-command runner with pinned environment and Hugging Face dataset

---

## 🔬 CAD AI Research

Research projects exploring generative CAD, geometry understanding, and AI-based modeling.

### Text-to-CAD Generation

#### NURBGen

https://github.com/SadilKhan/NURBGen

A research framework for generating industry-standard NURBS surfaces directly from text prompts.

Key Features

- LLM-driven NURBS geometry generation
- Fine-tuned Qwen model
- Editable CAD surface representation
- STEP and STL export
- Text-to-CAD evaluation pipeline
- AAAI 2026 research project

Note: Research projects with fewer than 100 GitHub stars may be included when they offer significant technical or scientific value.

---

## 🤝 Contributing

Contributions are welcome!

Please submit an issue or pull request to suggest new projects, correct existing entries, or improve project descriptions.

### Inclusion Criteria

Projects should meet most of the following criteria:

- Open-source and publicly accessible.
- Directly related to CAD, engineering design, or CAD automation.
- Provide practical capabilities for AI agents, such as MCP servers, agent skills, plugins, APIs, or autonomous workflows.
- Have a meaningful README, documentation, and installation instructions.
- Preferably have more than 100 GitHub stars.
- Actively maintained or technically significant.

### Project Classification

To keep the list organized:

- **MCP Servers** expose CAD functionality through the Model Context Protocol.
- **CAD Agents** provide autonomous planning, execution, and validation workflows.
- **Agent Skills** provide reusable instructions and domain-specific knowledge.
- **Harness Plugins** integrate CAD capabilities into agent runtimes and coding environments.
- **Infrastructure & SDKs** provide the underlying APIs, execution engines, and validation interfaces.

A project may provide multiple capabilities. It should be listed primarily in the category representing its main contribution, with cross-references where appropriate.

### Quality Guidelines

- Prefer projects with working code over conceptual demos.
- Clearly distinguish native CAD geometry from mesh-only generation.
- Mention supported CAD applications and file formats.
- Describe whether the project requires a locally installed CAD application.
- Avoid duplicate entries and abandoned forks unless they provide meaningful additional functionality.
- Star counts are indicative and should not be treated as a permanent inclusion requirement.
