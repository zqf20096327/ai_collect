# Flowra

<p align="center">
  <strong>The Graph Execution Engine and Node Package Development Tool</strong>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#documentation">Documentation</a> •
  <a href="#examples">Examples</a>
</p>

---

## Introduction

Flowra is the core graph execution engine and node package development tool for FlowBench. It provides developers with a complete toolchain for creating, testing, debugging, and publishing custom node packages. With Flowra, you can easily encapsulate machine learning models, image processing algorithms.

## Features

- **Visual Node Development**: DAG (Directed Acyclic Graph) based node system supporting flexible workflow orchestration
- **Rich Type System**: Built-in component types and value types supporting multimedia data including images, videos, audio, and 3D meshes
- **Complete Development Toolchain**: Full lifecycle tools including project creation, node management, building, and debugging
- **High-Performance Execution Engine**: Supports node caching, distributed execution, and other optimization features
- **Model Integration**: Built-in ModelScope model download and management functionality
- **Flexible Storage Backend**: Supports multiple object storage services like OSS and MinIO

## Installation

### Prerequisites

- Python 3.10+
- Miniconda recommended for environment management

### Create Virtual Environment

```bash
conda create -n flowra python=3.10
conda activate flowra
```

### Install Flowra

```bash
pip install flowra
```

### Install Documentation Dependencies (Optional)

If you need to view or compile documentation locally:

```bash
pip install flowra[docs]
```

## Quick Start

### 1. Create a Node Package Project

Use the `flowra create` command to create a new node package project:

```bash
flowra create mynodes
```

Follow the prompts to configure your project. You can choose to add example node groups to quickly understand the development workflow.

### 2. Project Structure

The created project structure looks like this:

```
mynodes/
├── config.yaml           # Node package configuration file
├── setup.py             # Python package configuration
├── mynodes/             # Node package source directory
│   └── nodes/           # Node groups directory
│       ├── number_calc/ # Example: number calculation node group
│       └── image_process/ # Example: image processing node group
└── tests/               # Test directory
    ├── test_data/       # Test data
    └── ...
```

### 3. Develop Nodes

The core of node development is defining node classes that inherit from `flowra.dag.Node`:

```python
from flowra.dag.node import Node, BaseArgs
from flowra.dag.context import RunContext
from flowra.type.component_type import Placeholder, Number, Select
from flowra.type.value_type import AnyImage

class MyNode(Node):
    # Node initialization arguments
    class InitArgs(BaseArgs):
        model_name: Select(value_type=str, description="Model name")

    # Node input arguments
    class InputArgs(InitArgs):
        image: Placeholder(value_type=AnyImage, description="Input image")
        threshold: Number(value_type=float, description="Threshold", default=0.5)

    # Node output arguments
    class OutputArgs(BaseArgs):
        result: Placeholder(value_type=AnyImage, description="Processing result")

    # Initialization function (load models, etc.)
    def init(self, ctx: RunContext, args: InitArgs):
        # Initialize model
        self.model = load_model(args.model_name)

    # Run function (main logic)
    def run(self, ctx: RunContext, args: InputArgs) -> OutputArgs:
        # Process input and return result
        result = self.model.process(args.image, args.threshold)
        return self.OutputArgs(result=result)
```

### 4. Manage Node Groups and Nodes

Use the `flowra project` command to manage node groups and nodes:

```bash
cd mynodes
flowra project
```

Follow the interactive prompts to:
- Add/remove node groups
- Add/remove nodes from node groups
- Automatically update `config.yaml` configuration

### 5. Build Node Package

After development, build the node package:

```bash
flowra build
```

After successful build, a `.nodebin` file will be generated in the `dist/` directory. This is the node package that can be imported into FlowBench.

### 6. Use in FlowBench

1. Open FlowBench client
2. Click **Library** → **Nodes** → **Add Node**
3. Select the built `.nodebin` file
4. Wait for loading to complete, then use the new nodes in the canvas

## Documentation

### View Documentation Locally

If you have installed documentation dependencies, you can start a local documentation server with MkDocs:

```bash
mkdocs serve
```

Then visit `http://localhost:8000` in your browser.

### Build Documentation

```bash
mkdocs build
```

### Core Concepts

- **NodePackage**: The minimum publishable collection of nodes
- **NodeGroup**: Organizational unit for categorizing nodes
- **Node**: Basic execution unit in workflows
- **ComponentType**: Controls the frontend rendering style of node inputs/outputs
- **ValueType**: Controls the Python data type at runtime

### Main Commands

| Command | Description |
|---------|-------------|
| `flowra create <name>` | Create a new node package project |
| `flowra project` | Manage node groups and nodes |
| `flowra build` | Build node package |
| `flowra debug` | Debug nodes |
| `flowra config` | Configure Flowra settings |

## Examples

The project includes complete example node packages:

### Number Calculation Examples
- **Number Input Node**: Input numeric values
- **Add Node**: Calculate the sum of two numbers
- **Text Display Node**: Display calculation results

### Image Processing Examples
- **Image Input Node**: Import images
- **YOLO Node**: Object detection using YOLO model
- **Image Display Node**: Display processing results

Example code is located in the `flowra/command/demo/` directory.

## Dependencies

Core dependencies include:

- **pydantic**: Data validation and type definitions
- **fastapi** / **uvicorn**: API server
- **pillow**: Image processing
- **click**: Command-line tools
- **modelscope**: Model download and management
- **oss2** / **minio**: Object storage support
- **trimesh**: 3D mesh processing

See `requirements.txt` for the complete dependency list.

## Architecture

Flowra uses a layered architecture design:

```
flowra/
├── api/              # API server and application interface
├── dag/              # DAG execution engine
│   ├── context/      # Execution context
│   ├── plan/         # Execution plans (logical/physical)
│   └── graph.py      # Graph structure definition
├── execute/          # Executors and schedulers
│   └── session/      # Session management
├── type/             # Type system
│   ├── component_type/ # Component types
│   └── value_type/     # Value types
├── command/          # Command-line tools
├── nodes/            # Built-in nodes
├── common/           # Common modules (cache, storage, etc.)
└── util/             # Utility functions
```

## Version

Current version: **0.6.0**

Version format: `major.minor.bugfix`

- **bugfix**: Bug fixes only, no interface changes
- **minor**: Compatible updates or new features
- **major**: Major updates or breaking changes

## Maintainers

- **Team**: 呜哩WULI
- **Authors**: Zhipeng DI, Zihao CHU, Guoxuan ZHU, Jiancong DU, Weiyi LU
- **Email**: muse@alibaba-inc.com

## License

Please refer to the project license file.

## Contributing

Issues and contributions are welcome!


---

<p align="center">
  Made with ❤️ by 呜哩WULI Team
</p>
