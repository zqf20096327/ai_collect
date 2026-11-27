# ControlWorld: A Plugin WebUI for World Snapshot Models

[[Paper]](https://arxiv.org/abs/2611.24917) |
[[Project Page]](https://world-snapshot.github.io/) |
[[WSMs]](https://github.com/World-Snapshot/WSMs) |
[[World Snapshot Graphics]](https://github.com/World-Snapshot/wsg) |
[[Models & Data]](https://huggingface.co/World-Snapshot) |
[[Documentation]](https://world-snapshot.github.io/doc/index.html) |
[[Organization]](https://github.com/World-Snapshot) |
[[Live Demo]](https://huggingface.co/spaces/FangSen9000/WSM-ControlWorld)

ControlWorld is the interactive control panel of the World Snapshot ecosystem. It turns a model's directed visual-task graph into an executable interface: select a trained route, provide its image or text conditions, run the recommended checkpoint, and inspect the decoded result and live inference log.

The host remains model-independent. Each model carries its own interface, backend, requirements, and task definitions as a plugin; ControlWorld supplies one consistent shell for discovery, execution, visualization, and plugin management.

![ControlWorld WebUI](static/images/user_demos/part_i_02_head_000578.png)

## What ControlWorld Provides

- **Visual task selection.** Select an input and output from the task graph, or click a trained edge directly.
- **Multi-condition execution.** Plugins may request image, text, audio, reference, or other conditions within one route.
- **Model-aware deployment.** A plugin can expose recommended checkpoints, task warnings, categorical refiners, and modality-specific controls.
- **Decoded visual evidence.** Non-RGB results can use the official WSG Reader visualization and value legend supplied by the model plugin.
- **Live inference logs.** Long model loading, preprocessing, sampling, decoding, and output generation remain visible in the interface.
- **Shared 3D visualization.** Plugins that require interactive scenes can attach to the common Viser service.
- **Non-destructive plugin management.** Uninstalling a plugin disables its tab without deleting its local folder; it remains available to install again.

## Quick Start

```bash
git clone --recursive git@github.com:World-Snapshot/ControlWorld.git
cd ControlWorld

conda create -n WSM python=3.11 -y
conda activate WSM
pip install -r env/requirements.txt

python start_modern.py
```

ControlWorld opens the main interface at `http://localhost:8080`. Its shared Viser service runs at `http://localhost:8081`.

The `WSM` environment is shared with WSM v1; ControlWorld does not require a second model environment.

For a remote machine or a custom port:

```bash
python start_modern.py --frontend-port 8080 --viser-port 8081 --no-browser
```

## Hugging Face GPU Space

The complete ControlWorld interface can run on Hugging Face GPU hardware. The
Docker deployment under
[`deploy/huggingface_space`](deploy/huggingface_space/) exports ControlWorld,
the WSM plugin, and WSG Reader as a standalone public Space repository and
reads the released single-file WSM checkpoint by byte range when it starts.

```bash
python deploy/huggingface_space/export_space.py \
  --output /tmp/wsm-controlworld-space
```

The default `paper-demo` profile loads the recommended TunnelingNets used by the paper
demonstrations. `selected` and `all` profiles provide smaller or broader
deployments without changing the application code.

## Model Plugins

ControlWorld scans both direct plugins and one-level plugin collections under `plugins/`. The official WSMs repository is included as a submodule:

```text
plugins/
├── WSMs/                            # repository submodule / plugin collection
│   ├── WSM_v1/
│   │   └── webui/                   # automatically discovered plugin
│   └── WSM_v2/                      # discovered automatically when available
└── MyModel/
    └── webui_controlworld/          # or webui/
        ├── index.js                 # frontend entry
        ├── config.json              # optional plugin metadata/configuration
        ├── viser_backend.py         # optional Viser/message backend
        ├── api_handler.py           # optional API handler
        └── requirements.txt         # optional plugin dependencies
```

For an existing clone, initialize or update the collection with:

```bash
git submodule update --init --recursive
```

Plugin interface files may live directly in a plugin root, `webui_controlworld/`, or `webui/`. A repository such as WSMs may contain multiple version directories; ControlWorld discovers each version independently without recursively treating ordinary model folders as plugins. For backward compatibility, `backend.py`, `plugin_backend.py`, and `requirement.txt` are also recognized. Duplicate plugin IDs are rejected so that one visible task tab always resolves to one implementation.

The Plugin Manager can:

- discover local plugin folders and symbolic links;
- enable or disable their tabs without deleting files;
- preserve the selected state in the browser;
- refresh the local registry after a plugin is added or updated;
- install supported GitHub or Hugging Face repositories from a URL.

## WSM v1

[WSM v1](https://github.com/World-Snapshot/WSMs) is the principal reference plugin. Its WebUI exposes the WSG Task Graph, recommended Channel Heads, multi-condition inputs, checkpoint selection, true inference, target-specific visualization, selectable output artifacts, and a live log panel.

A route can be chosen from either direction: selecting input and output controls highlights the corresponding graph edge, while clicking a trained graph edge updates the input, output, and checkpoint controls. Dense and sparse routes share the same interface.

## Architecture

```text
Browser
  ├── plugin tabs and Plugin Manager
  ├── task-specific controls
  └── decoded outputs and logs
          │ HTTP / WebSocket
          ▼
ControlWorld
  ├── FastAPI application and static frontend
  ├── plugin discovery and lifecycle
  ├── backend message routing
  └── shared Viser service
          │
          ▼
Model plugins
  ├── frontend entry
  ├── inference/backend worker
  ├── checkpoints and task registry
  └── model-specific readers and visualizations
```

Core entry points:

- `start_modern.py` starts the FastAPI frontend, WebSocket routing, plugin scanner, and shared Viser service.
- `viser_backend.py` discovers plugin backends and routes Viser controls and plugin messages.
- `plugins/plugin-loader.js` handles browser-side discovery, loading, ordering, and enabled state.
- `plugins/plugin-system.js` renders tabs and the Plugin Manager.
- `static/style/` defines the shared ControlWorld visual language inherited by plugins.

## User Demonstrations

| RGB to Relative Depth | DWPose + Text + RGB Reference to RGB |
|:--:|:--:|
| ![RGB to Relative Depth](static/images/user_demos/part_i_01_head_000001.png) | ![Pose-controlled RGB generation](static/images/user_demos/part_i_02_head_000578.png) |
| **Normal to Edge** | **Relative Depth + RGB to Normal** |
| ![Normal to Edge](static/images/user_demos/part_i_03_head_000275.png) | ![RGB-assisted normal reconstruction](static/images/user_demos/part_i_04_head_000157.png) |

These desktop captures retain the complete task graph, inputs, inference controls, and decoded output. The full set of 32 task demonstrations is available in [`static/images/user_demos`](static/images/user_demos/).

## Contributing

Model plugins, interface improvements, bug reports, and documentation updates are welcome. See [Contributing.md](Contributing.md) for the plugin interface and contribution workflow.

## Authors and Citation

ControlWorld was created by Sen Fang and Dimitris N. Metaxas as part of the
World Snapshot project. Citation metadata is provided in
[`CITATION.cff`](CITATION.cff).

## License

The original ControlWorld host software is released under the
[MIT License](LICENSE). This license does not apply to model plugins, Git
submodules, model weights, datasets, or third-party assets that carry their
own licenses. In particular, the WSMs plugin remains governed by the license
provided in the [WSMs repository](https://github.com/World-Snapshot/WSMs).
