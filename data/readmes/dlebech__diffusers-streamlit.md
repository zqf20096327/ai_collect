# diffusers-streamlit

A *super minimal* Streamlit app for playing around with open image generation models: Z-Image Turbo, FLUX.2 [klein] and Stable Diffusion XL 1.0. (It started out as a Stable Diffusion 2 app.)

Includes:
- Text to image (txt2img): Z-Image Turbo, FLUX.2 [klein] 4B, XL 1.0, SDXL Turbo
- Image to image (img2img): Z-Image Turbo, FLUX.2 [klein] 4B, XL 1.0 refiner
- Inpainting: Z-Image Turbo, FLUX.2 [klein] 4B, XL 1.0
- Negative prompt input for all methods (ignored by the models that don't support it, e.g. FLUX.2).

Uses Z-Image Turbo by default. The steps and guidance sliders start at sensible values for each model (the turbo/distilled models want few steps, around 2-9, and guidance 0; FLUX.2 ignores guidance), the txt2img width and height start at the model's native size (1024x1024, 512x512 for SDXL Turbo), and the app shows a short hint for each.

FLUX.2 [klein] works like an image editor in img2img and inpainting: it uses the input image as a reference, so the prompt should describe the change ("replace the dog with a cat"), and the img2img strength is ignored.

**Note:** Stable Diffusion 2.0/2.1 were dropped because Stability AI removed those repositories from Hugging Face. Stable Diffusion 3.5 is left out because its repositories are gated behind a licence agreement.

### Models and licences

| Model | Hugging Face repo | Licence |
|---|---|---|
| Z-Image Turbo | [Tongyi-MAI/Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo) | Apache 2.0 |
| FLUX.2 [klein] 4B | [black-forest-labs/FLUX.2-klein-4B](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B) | Apache 2.0 |
| XL 1.0, XL 1.0 refiner | [stabilityai/stable-diffusion-xl-base-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0), [stabilityai/stable-diffusion-xl-refiner-1.0](https://huggingface.co/stabilityai/stable-diffusion-xl-refiner-1.0) | CreativeML OpenRAIL++-M |
| SDXL Turbo | [stabilityai/sdxl-turbo](https://huggingface.co/stabilityai/sdxl-turbo) | Stability AI Non-Commercial Research Community License (`sai-nc-community`) |

## Requirements

- Z-Image Turbo needs a 16GB GPU (with CPU offload, ~12GB peak), FLUX.2 [klein] 4B ~8GB with CPU offload, and the XL models run on 8GB.
- Make sure you have the Nvidia drivers and all that.
- The newer models are bigger. On a 16GB GPU (RTX 4070 Ti SUPER), Z-Image Turbo and FLUX.2 [klein] both need CPU offload, which the app turns on automatically for them on GPUs with less than 24GB; it brings peak GPU memory down to roughly 12GB for Z-Image Turbo and 8GB for FLUX.2 [klein] 4B. You also need plenty of system RAM for the offloaded parts (32GB+): with CPU offload the whole model lives in host RAM (~20GB for Z-Image Turbo). Switching mode (txt2img, img2img, inpaint) on the same model reuses the loaded model; switching model unloads it first. Unloading (the sidebar button, or a model switch) returns the memory to the OS on Linux. Memory is also trimmed after each image, so RSS between images stays near the model's size. The XL models run without offload on 16GB.
- Disk: Z-Image Turbo is roughly 33GB and FLUX.2 [klein] 4B roughly 16GB.

Observations based on my own machine:
- Using Ubuntu 22.04 with an RTX 2070 GPU (8GB memory)
- Using Python 3.10 in a fresh conda environment.
- The 2.1 768 model works out of the box with 768x768 images.
- For the XL 1.0 model, I personally have to use CPU offloading. Model CPU offloading is enough so it doesn't slow down inference so much.
  - With CPU offloading, I have been able to generate 1024x1024 images using the XL model.

## Install & Run

Requires Python 3.12 (pinned in `.python-version` and the version it's tested with; `requires-python` allows newer, which may work). Dependencies are managed with [uv](https://docs.astral.sh/uv/) (`pyproject.toml` + `uv.lock`):

```
uv sync
uv run streamlit run main.py
```

`uv sync` creates a `.venv` with Python 3.12 (uv downloads it if needed).

Alternatively with pip, using the `requirements.txt` exported from the lock file:

```
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run main.py
```

### GPU / CUDA wheels

On Linux and Windows, PyTorch is installed from the official PyTorch wheel index with CUDA 13.2 builds (`https://download.pytorch.org/whl/cu132`). This is configured in `pyproject.toml` for uv, and `requirements.txt` includes it as an `--extra-index-url` for pip. The CUDA libraries come bundled with the wheels, you only need a recent Nvidia driver (CUDA 13 needs driver 580 or newer, check with `nvidia-smi`). If you need a different CUDA version, change the index URL in `pyproject.toml` and run `uv lock` (not every PyTorch release is built for every CUDA version, so you may also have to relax the `torch`/`torchvision` versions).

To regenerate `requirements.txt` after changing dependencies:

```
uv export --no-hashes --no-dev --emit-index-url --format requirements-txt -o requirements.txt
```

The first time it runs, it will download the model from Hugging Face automatically.

Images are automatically saved in an `outputs/` folder, each with a `.txt` file next to it that records the settings used: prompt, negative prompt, mode (txt2img/img2img/inpaint), model, steps, guidance scale, output size, strength (img2img/inpaint), seed and whether CPU offload was on.

Each tab has an optional seed input. Leave it empty for a random seed; the seed used is shown under the image. The same seed with the same settings gives the same image.

### Out of memory errors

Out of memory errors occur frequently in my setup (8GB GPU), even though I've tried to limit the usage of cache and clean up the CUDA. They are quickly fixed with the "Unload model" button in the sidebar, which frees the GPU memory and system RAM (the model is loaded again on the next generate). Streamlit's "Clear cache" no longer unloads the model, so use that button instead.

## MCP server

`mcp_server.py` is a [Model Context Protocol](https://modelcontextprotocol.io) server, so AI agents (Claude Code and others) can generate and edit images with the same models, settings and CPU offload tuning as the app. It is a long-running streamable HTTP server, so the model stays loaded across sessions:

```
uv run python mcp_server.py
```

It listens on `http://127.0.0.1:8765/mcp`. Use `--port` to change the port, and `--preload <slug>` to load a model at startup instead of on the first call. To add it to Claude Code:

```
claude mcp add --transport http diffusers http://127.0.0.1:8765/mcp
```

Models are named by slug: `z-image-turbo` (default), `flux2-klein-4b`, `sdxl`, `sdxl-turbo` and `sdxl-refiner`. Tools:

- `list_models`: every model with its slug, name, Hugging Face repo, the tools (and modes) it supports, default steps/guidance/size and its hint.
- `generate_image(prompt, model, width, height, steps, guidance_scale, negative_prompt, seed)`: text to image (z-image-turbo, flux2-klein-4b, sdxl, sdxl-turbo).
- `edit_image(image_path, prompt, model, strength, steps, guidance_scale, negative_prompt, seed)`: image to image (z-image-turbo, flux2-klein-4b, sdxl-refiner). Input images are local file paths.
- `inpaint(image_path, mask_path, prompt, model, strength, steps, guidance_scale, negative_prompt, seed)`: inpainting (z-image-turbo, flux2-klein-4b, sdxl). White in the mask means repaint, as in the app's canvas.

The server accepts sizes from 64 to 2048 pixels per side (the app's sliders stop at 1600). For edit_image and inpaint that applies to the input image's size, except for sdxl inpaint, which always outputs 1024px and only needs 64 or more. Anything you leave out uses the model's defaults, as in the app. Every result is saved in `outputs/` with its `.txt` settings file, like in the app. The tool returns the absolute path of the PNG, the settings used (including the seed, the size and any settings the model ignored) and a small thumbnail (256px on the long side), not the full image. Without a seed, a random one is used; it is returned, so a result can be reproduced by passing it back. Bad input (unknown model, a model that doesn't support the tool, missing image, invalid or too small/large size, out of memory) comes back as a tool error.

Notes:
- It only listens on localhost and has no authentication.
- One image is generated at a time; other calls wait their turn. Progress is reported per step.
- The first call with a model loads it, which is slow. Only one model is kept in memory, so switching models reloads; switching between tools on the same model reuses it.
- Don't run the app and the server at the same time on a 16GB GPU, they would both want the memory.

## Tests

```
uv run pytest
```

The tests use a fake pipeline, so they need no GPU and download no models.

## Why

Mostly created this because I couldn't find a simple UI in the days right after the release of Stable Diffusion 2 (and also because I wanted to refresh my memory of Streamlit).

## License

Code in this repository, written by me, can be freely used under the [CC0 license](/LICENSE). This covers all code except where otherwise noted.

Always remember to check the license of the downloaded models as well :-)
