<p align="center">
  <img src="docs/public/logo.svg" alt="TensorViz logo" width="120" height="120">
</p>

<h1 align="center">TensorViz</h1>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License: MIT"></a>
  <a href="docs/install.md#extension"><img src="https://img.shields.io/badge/VS%20Code-%3E%3D1.106-007ACC.svg" alt="VS Code 1.106+"></a>
</p>

<p align="center">
  Explore your PyTorch or JAX/Flax model as an interactive graph. Follow tensor shapes, find the matching Python, and review changes alongside your code.
</p>

<a id="try-it"></a>

## Install

**Coding-agent plugin** (preview: macOS ARM64/x64, Linux x64 (glibc >=2.31), Linux ARM64 (glibc >=2.35), and Windows x64/ARM64, with CPython 3.12 and CPU capture):

Windows support is through native Codex entries; Windows Claude Code/Cursor and musl are outside the published acceptance scope. Runtime availability does not guarantee every client GUI, OS version, or model dependency works.

Codex:

```sh
codex plugin marketplace add tensorviz-org/tensorviz
codex plugin add tensorviz@tensorviz-standalone
```

Claude Code:

```sh
claude plugin marketplace add tensorviz-org/tensorviz
claude plugin install tensorviz@tensorviz-standalone --scope user
```

<a id="install-in-cursor"></a>

Cursor: download the **Cursor ZIP** from [this repository’s releases](https://github.com/tensorviz-org/tensorviz/releases/latest) and follow [Install in Cursor](docs/install.md#cursor).

**Editor extension** for VS Code, Cursor, or VSCodium ([Marketplace](https://marketplace.visualstudio.com/items?itemName=tensorviz.tensorviz-vscode), [Open VSX](https://open-vsx.org/extension/tensorviz/tensorviz-vscode)):

```sh
code --install-extension tensorviz.tensorviz-vscode
```

Already using the old plugin catalog? [Move your existing installation](docs/catalog-migration.md) before updating. All options, VSIX files, and platform limits are on the [Install](docs/install.md) page. Then open your first graph with the [quickstart](#quickstart) below.

Release automation and the installation catalog live in this public repository. The links above serve published packages; historical 0.x downloads retain their original locations. The source manifests declare the 1.0.0 release candidate; the installed version changes after publication. See [release operations](docs/releasing.md), [local setup](docs/local-setup.md), and [plugin build](docs/plugin-build.md).

## Quickstart

Open a small PyTorch model, inspect its tensor shapes, and find a layer's Python. You can follow the same steps with your own model.

Before you start, [install TensorViz](#install) and choose a Python environment with PyTorch installed. For JAX and Flax in the editor, see the [framework guide](docs/jax-support.md).

### 1. Create a model

Save this as `model.py` in an open project folder:

```python
import torch
from torch import nn

# tensorviz: input=1,16
class MlpTiny(nn.Module):
    def __init__(self):
        super().__init__()
        self.proj = nn.Linear(16, 32)
        self.activation = nn.ReLU(inplace=True)
        self.head = nn.Linear(32, 4)

    def forward(self, x):
        return self.head(self.activation(self.proj(x)))
```

The comment supplies an example input shape: one item with 16 features. TensorViz uses it when no saved setup or unambiguous example call supplies the inputs. You can review and change inputs before a capture.

### 2. Open your first graph

**In your editor:** click **Open as Graph** above `MlpTiny`. You can also run **tensorViz: Open as Graph** and choose the class.

**In your coding agent:** start a new chat in the project folder and ask:

> Use TensorViz to open MlpTiny in model.py. Use an example input with shape [1, 16]. Ask me which Python environment to use if one is not saved.

Confirm Python and the example input if asked. TensorViz asks before library changes and saves a complete setup in `tensorviz.toml`.

> **Capture runs your code.** Opening a graph executes one forward call of the model with the inputs you chose. **Inspect source only** opens a preview without running the model.

### 3. Inspect the result

The graph connects `proj` → `activation` → `head`, with input and output cards around them.

![The MlpTiny source preview in TensorViz Canvas](docs/images/explore-graph.png)

*This screenshot shows the source preview. Run the model to record shapes; the preview alone does not measure them.*

After a successful capture with input `[1, 16]`, the expected shapes are:

| Layer | Input | Output |
| --- | --- | --- |
| `proj` · Linear | `[1, 16]` | `[1, 32]` |
| `activation` · ReLU | `[1, 32]` | `[1, 32]` |
| `head` · Linear | `[1, 32]` | `[1, 4]` |

Select `proj` and enable **Code focus** to find its `nn.Linear(16, 32)` declaration. Pan, zoom, and explore without running another capture.

If shapes say **Not recorded**, check that a capture completed. **Inspect source only** does not produce recorded shapes.

<details>
<summary>If opening stops</summary>

| What you see | What to do |
| --- | --- |
| No Python, or import errors | [Environment recovery](docs/environment-recovery.md) and [model libraries](docs/graph-libraries.md) |
| **Choose a setup method** | [Setup and inputs](docs/graph-setup.md) |
| Capture failed | Fix the source or the inputs, then **Run again** |
| Agent cannot see tools | Start a new chat. For the extension, see [Connect MCP](docs/mcp.md) |

</details>

**Next steps:** [Explore the graph](docs/canvas.md) · [Follow the code](docs/code-focus.md) · [Review model changes](docs/graph-diff-review/README.md)

## Docs

Read the independently hosted documentation at <https://docs.tensorviz.dev/>.
To edit or preview it, follow the [docs contribution guide](CONTRIBUTING.md#documentation-contributions).
Only this repository and the docs dependencies are needed.

- [Install](docs/install.md)
- [Quickstart](docs/quickstart.md)
- [Coding-agent plugin](docs/agent-plugin.md)
- [Concepts](docs/concepts.md)
- [Documentation index](docs/README.md)

## Support and contributing

- [Plugin support and compatibility](https://github.com/tensorviz-org/tensorviz/blob/main/SUPPORT.md)
- [Contributing](CONTRIBUTING.md)
- [Security](SECURITY.md)
- [Code of conduct](CODE_OF_CONDUCT.md)

## Layout

| Path | What it is |
| --- | --- |
| `extension/` | VS Code, Cursor, and VSCodium extension |
| `canvas/` | React graph UI |
| `backend/` | Python capture and projection |
| `packages/contracts`, `packages/graph-host` | Shared protocol and MCP host |
| `plugin/`, `plugins/tensorviz/` | Coding-agent plugin host and manifests |
| `examples/` | Small models |
| `docs/` | Product docs. Index: [docs/README.md](docs/README.md) |

## License

TensorViz code is [MIT](LICENSE). tldraw, which renders the canvas, is not covered by that license. Read [NOTICE](NOTICE) and [docs/licensing.md](docs/licensing.md) before you give a build to other people.

The hosted website application is not in this repository. **Publish** and **tensorViz: Sign in to tensorViz** stay in the extension. See [share a graph](docs/share-to-website.md).

