# ComfyUI Anima 3.8B LoRA Bridge

[日本語](README_JA.md)

ComfyUI nodes for applying original 28-block Anima Base LoRAs and 40-block
Anima 2.9B LoRAs to the matching inherited layers in the 52-block
[Anima 3.8B](https://huggingface.co/lylogummy/Anima-3.8B) model.

## Why this is needed

Anima 3.8B was produced through two interleaved layer expansions:

```text
Anima Base: 28 blocks -> Anima 2.9B: 40 blocks -> Anima 3.8B: 52 blocks
```

The normal ComfyUI LoRA loader matches block numbers directly. After the
insertions, a Base LoRA key such as `blocks.2` no longer belongs on block 2 in
the expanded model. This node remaps every supported key through both expansion
layouts before handing the result to ComfyUI's standard LoRA patcher.

The safe behavior is fixed and has no experimental switches:

- LoRA patches are applied only to inherited DiT blocks.
- The 24 expansion blocks remain untouched.
- Anima 3.8B's changed internal text adapter remains untouched for Base/2.9B LoRAs.
- Source layout is detected automatically.

The inherited Base mapping was checked against the official Anima Base v1.0
and Anima 3.8B checkpoints: all 560 tensors in the 28 inherited DiT blocks were
bit-identical at their mapped destinations.

## Installation

From `ComfyUI/custom_nodes`:

```bash
git clone https://github.com/Lakeside529/ComfyUI-Anima-3.8B-LoRA-Bridge.git
```

Restart ComfyUI. No additional Python packages are required.

## Nodes

### Load Anima LoRA on 3.8B (Model Only)

Use this for standard style, character, Turbo, RL, and other model-only Anima
LoRAs. It has the same three practical inputs as ComfyUI's model-only loader:

- `model`
- `lora_name`
- `strength_model`

### Load Anima LoRA on 3.8B

Use this variant when a LoRA also contains text-encoder weights. It accepts and
returns both `MODEL` and `CLIP`.

## Workflow placement

Place the bridge after `UNETLoader` and before both the sampler and any node
that reads the model to build conditioning:

```text
UNETLoader -> Anima 3.8B LoRA Bridge -> KSampler
                              |
                              +-------> Qwen3.5 Unified Prompt (model input)
```

When using the Qwen3.5 workflow, install the companion
[comfyui-anima-3-8B](https://github.com/GumGum10/comfyui-anima-3-8B) nodes and
connect the bridge's final `MODEL` output to both the Unified Prompt node and
the sampler. An API-format example is provided in
[`examples/api_workflow.json`](examples/api_workflow.json).

## Supported LoRA key formats

- ComfyUI generic keys such as `diffusion_model.blocks.0...lora_A.weight`
- Kohya-style keys such as `lora_unet_blocks_0_...`
- Full 28-block Anima Base and 40-block Anima 2.9B layouts
- Native 52-block LoRAs pass through unchanged

## Technical sources

- [Anima 2.9B expansion manifest](https://huggingface.co/Gazingstars123/Anima-2.9B/blob/main/expand_manifest.json)
- [Anima 3.8B model card](https://huggingface.co/lylogummy/Anima-3.8B/blob/main/README.md)
- The 40-to-52 insertion positions are also stored in the Anima 3.8B checkpoint metadata.

## License

The code in this repository is MIT licensed. Model files and LoRAs are not
included and remain subject to their respective licenses.
