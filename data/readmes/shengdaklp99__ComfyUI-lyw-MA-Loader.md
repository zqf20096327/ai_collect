# ComfyUI-lyw-MA-Loader

A standalone, visual LoRA loader node for ComfyUI — organize LoRAs into groups, manage presets and favorites, fetch Civitai previews and trigger words, and optionally stay in sync with [Lora Manager](https://github.com/willmiao/ComfyUI-Lora-Manager).

中文说明：[README.zh.md](README.zh.md)

## Changelog

Only notable changes are listed here; minor visual or text tweaks are omitted.

### 1.0.9

- The LoRA edit dialog now shows a preview thumbnail and supports click/drag image upload or replacement
- New nodes default to the slider weight control with the CLIP and recommended-weight columns hidden
- Added "Edit info" to the LoRA row context menu
- Added a top toolbar MA button that opens the Add/Replace LoRA dialog, shows the target node name, and provides a jump-to-node button for topbar launches
- Added a global header background color for groups that are not ignored and contain enabled LoRAs

### 1.0.8

- LORA string import now ignores common personal prefixes (krea2, k2, anima) and tolerates small filename differences, including OCR-confusable 1/i/I/l/L and 0/o/O; near matches open a picker with local candidates
- Replacing a LoRA now resyncs trigger words, note, and recommended weight from the new file while keeping model/CLIP weights and enabled state
- Dragging LoRAs now treats folder top/bottom edges and inter-folder gaps as easier insert targets, while the header center still drops into the folder
- Folder ignore now uses a crossed-out eye icon and supports separate global colors for ignored and normal states

### 1.0.7

- Added ComfyUI Desktop compatibility by replacing native prompt/confirm/alert dialogs with in-page dialogs across presets, folders, weights, and metadata actions

### 1.0.5

- Added author recommended weights: row badges, metadata refresh statistics, and one-click apply
- Recommended weights are detected and saved from every metadata crawl path; newly added LoRAs inherit saved values
- The LoRA info dialog shows recommended weight; LORA string imports sync trigger words and recommended weights
- The metadata manager only lists LoRAs whose Civitai info has a recommendation but local info does not; items without one are skipped
- Added a layout option to hide the recommended-weight column

### 1.0.4

- Added preset and favorites export/import in Settings
- Trigger-word toggling moved to right-click; multi-word triggers support per-word blocking and only enabled words are previewed
- Folder ignore now uses a dedicated eye button; clicking the folder title collapses or expands it
- Added CLIP weight follow/custom modes
- Added one-click metadata refresh for all LoRAs in the current workflow
- Added "Save as preset group" to the folder context menu
- Added target-group selection in the Add LoRA dialog
- Added a layout guard that keeps the embedded panel aligned with the node width
- Added a layout option to hide the CLIP weight column

### 1.0.3

- Initial public ComfyUI Registry release with groups, presets, Civitai metadata, Lora Manager integration, colors, chaining and i18n

**Main node UI**

![lyw-MA Loader node](docs/preview-node.png)

**Add / Replace LoRA dialog**

![Add or Replace LoRA dialog](docs/preview-lora-picker.png)

> The screenshots show the Chinese UI. The node follows the system language: Chinese systems show Chinese, every other system shows English.

## Credits

This plugin is developed on top of [ComfyUI-ZML-Image](https://github.com/zml-w/ComfyUI-ZML-Image) (author: [**zml-w**](https://github.com/zml-w)) and [ComfyUI-Magic-Assistant](https://github.com/shigjfg/ComfyUI-Magic-Assistant) (author: [**shigjfg**](https://github.com/shigjfg)), and references [ComfyUI-Lora-Manager](https://github.com/willmiao/ComfyUI-Lora-Manager) (author: [**willmiao**](https://github.com/willmiao)). Thanks to all the original authors, and to group friend **you** for contributing bug fixes, new features, and improvement suggestions.

## Features

### Visual LoRA list

Every LoRA is a row with a thumbnail, weight slider, note field, trigger-word button and an enable toggle. Click a row to include/exclude it from loading; the row is dimmed when disabled. Weights, notes and trigger words are stored in the workflow, so each canvas keeps its own setup.

### Folders (groups)

- Group any selection of LoRAs into a folder
- Drag a row or a folder title's blank area to reorder freely — the position under the mouse pointer is the exact drop position, with a blue insertion line
- Drop a row onto a folder to move it inside; drop it on empty list space to move it back out
- **Ignore a group**: its LoRAs stop participating in loading while each row keeps its own enable state. Un-ignore and everything comes back exactly as before. Ignored groups also do not take part in *Group* / *Extra group* operations

### Presets and favorites

The left sidebar holds presets (multi-LoRA snapshots) and favorite collections. Drag a preset or favorite into the right-hand list and it is inserted exactly where you drop it — no more "always appended to the bottom". Single click still appends to the end.

### Multi-select and batch operations

Right-click any row to:

| Action | Behavior |
|---|---|
| Replace LoRA | Swap the model file, keep position and settings |
| Duplicate LoRA | Copy the selected rows to the end of the root list |
| Group selection | Move the selected rows into a new folder (original positions cleared) |
| Extra group | Copy the selected rows into a new folder, originals untouched |
| Fetch info | Batch-fetch Civitai metadata for the selection |
| Colors | Per-row color settings |
| Delete | Remove the row |

### Civitai metadata and previews

Trigger words and preview images are resolved by SHA256 against Civitai and saved next to the model file (`<model>.txt`, `<model>.png/.jpg/.webp`), together with a `<model>.metadata.json` sidecar. A built-in info manager can:

- batch fill missing info for the whole scope, a folder, or the current selection
- re-check sources, or update existing info
- keep **not found** items in their own category instead of polluting the fill results
- pause automatically when Civitai rate-limits the requests

### Lora Manager integration (optional)

When [Lora Manager](https://github.com/willmiao/ComfyUI-Lora-Manager) is installed, the loader reuses the same sidecar format and its download endpoint, so both UIs show the same previews, titles and trigger words. Without Lora Manager the loader falls back to its own crawl and still works standalone.

### Colors

Per-LoRA and per-folder colors, each with two modes:

- **Follow global** — the item uses the global default and changes with it
- **Fixed** — the item keeps its own colors regardless of global changes

The chosen mode is stored with the workflow.

### Chain output

`lora串输出` can be connected to another loader. Only the terminal loader applies LoRAs, so one model is patched once for the whole chain. Use `触发词输出` to emit the merged trigger words of the LoRAs that actually loaded.

### Language

Node title, ports and dialogs follow the system language: `zh-*` systems show Chinese, everything else shows English. You can force a language for testing with `localStorage.setItem("MPL_LANG", "en")` (or `"zh"`) in the browser console.

### Performance notes

Only enabled LoRAs outside ignored groups are serialized into the node's stack. Disabled and ignored rows never reach the backend. LoRA tensors are cached by `(path, weight)` and unused entries are released after each run, so switching weights does not leak memory.

## Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/shengdaklp99/ComfyUI-lyw-MA-Loader.git
```

Restart ComfyUI. The node appears under **✨ Magic Assistant → lyw-MA Loader**.

Requirements: ComfyUI with its bundled `torch`, `numpy` and `Pillow`. `opencv-python` is optional and only used to extract the first frame from video previews.

## Quick start

1. Add **lyw-MA Loader** and connect `model`.
2. Click **Add** to append LoRAs, or drag presets/favorites from the sidebar.
3. Click a row to toggle loading; adjust weight and note inline.
4. Right-click a row for batch operations.
5. Optionally connect the trigger-word output to a text encoder.

## Node reference

| Port | Direction | Description |
|---|---|---|
| `model` | input | Model to patch |
| `lora串接受` | input (optional) | LoRA chain from an upstream loader |
| `model` | output | Patched model |
| `触发词输出` | output | Merged trigger words of loaded LoRAs |
| `lora串输出` | output | LoRA chain for the next loader |

## Troubleshooting

- **Node title stays Chinese on an English system** — ComfyUI caches `/i18n` at startup; restart ComfyUI, then hard-refresh the browser (Ctrl+Shift+R).
- **"Missing LoRA file(s)" on queue** — the workflow references a model that no longer exists; the node validates the stack before running.
- **Preview not showing** — run the info manager once, or check that the preview file sits next to the model.

## Contributing

Issues and pull requests are welcome.

---

If this plugin helps you, please consider giving it a ⭐ **Star** — it helps other ComfyUI users find it.
