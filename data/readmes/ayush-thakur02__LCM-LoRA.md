# LCM-LoRA

Few-step image generation with Latent Consistency Models and LoRA adapters, packaged as a
Google Colab notebook. The notebook supports SDXL, SD 1.5, and SSD-1B base models with
their matching LCM LoRA adapters.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ayush-thakur02/LCM-LoRA/blob/main/LCM_LoRA.ipynb)

## What is inside

`LCM_LoRA.ipynb` is the complete workflow:

1. Install `diffusers` and `accelerate`.
2. Select a matching base model and LCM LoRA adapter.
3. Load the pipeline in fp16 with `LCMScheduler`.
4. Generate an image from a prompt with a small number of inference steps.

The notebook defaults to SDXL + `latent-consistency/lcm-lora-sdxl`, four inference steps,
and guidance scale 1.0. Those values are starting points, not universal optima.

## Model pairs

Use a base model and adapter that belong together:

| Base model | LCM LoRA adapter |
|:--|:--|
| `stabilityai/stable-diffusion-xl-base-1.0` | `latent-consistency/lcm-lora-sdxl` |
| `runwayml/stable-diffusion-v1-5` | `latent-consistency/lcm-lora-sdv1-5` |
| `segmind/SSD-1B` | `latent-consistency/lcm-lora-ssd-1b` |

## Run it

1. Open the notebook in Colab.
2. Select a GPU runtime. A T4 is sufficient for the default SDXL path, though larger
   models may need more memory.
3. Run the install cell.
4. Choose a base model and its matching LoRA.
5. Enter a prompt and run the generation cell.

The notebook uses CUDA (`pipe.to("cuda")`). It is not configured as a CPU workflow.

## Scope and limitations

- This is a reference notebook, not a training or evaluation framework.
- No generated images or model weights are committed here.
- Model downloads and generated outputs are subject to the licenses and terms of the
  upstream model providers.
- No speed or quality benchmark is claimed. Generation time depends on the Colab GPU,
  model pair, dtype, and inference settings.
- The screenshots and examples in earlier versions of this README were illustrative.

## Repository layout

```text
LCM_LoRA.ipynb   Colab workflow and prompt cell
README.md        setup, model pairs, and scope
LICENSE          MIT license for this repository
```

## License

The notebook and repository content are released under the [MIT License](LICENSE). The
models and adapters downloaded at runtime have their own licenses.
