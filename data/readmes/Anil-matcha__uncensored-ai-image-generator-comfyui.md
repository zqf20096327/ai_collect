# Uncensored AI Image Generator in ComfyUI

A plain-English guide to running unrestricted, low-filter AI image models inside ComfyUI on a laptop with no graphics card, using the Muapi nodes.

ComfyUI is a free app where you build AI workflows by connecting boxes (called nodes) with wires. Normally image models need a powerful graphics card. The Muapi nodes work differently: ComfyUI stays on your computer, the image model runs on a server, and the finished picture comes back into your workflow. This guide covers the image models listed in Muapi's [spicy AI image generator catalog](https://muapi.ai/ai-spicy-image-generator). It is the image counterpart of [uncensored-ai-video-generator-comfyui](https://github.com/Anil-matcha/uncensored-ai-video-generator-comfyui).

## Start here: the node pack

**All the nodes and example workflows live in one repo: [SamurAIGPT/muapi-comfyui](https://github.com/SamurAIGPT/muapi-comfyui).** This repo is the guide, that repo is the code.

1. Open your ComfyUI folder and clone the node pack into `custom_nodes`:
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/SamurAIGPT/muapi-comfyui
   pip install -r muapi-comfyui/requirements.txt
   ```
2. Restart ComfyUI.
3. Get an API key from [muapi.ai](https://muapi.ai) and paste it into the **MuAPI API Key** node (or the `api_key` field on any generation node).
4. Load an example: **File → Load**, then pick a file from the `workflows/` folder of the node pack (for example `MuAPI_Basic_TextToImage_Flux.json` for text-to-image or `MuAPI_ImageToImage_Seededit.json` for editing).
5. Use **MuAPI Text-to-Image** to start from words and **MuAPI Image-to-Image** to start from a picture. If the model you want is not in the `model` dropdown, use the **MuAPI Generate (Generic)** node and type the endpoint name from the table below, with a raw JSON payload.

## The image models

| Model | Starts from | Endpoint name | Notes |
|---|---|---|---|
| Seedream 5.0 Pro | Text, picture | `bytedance-seedream-5.0-pro` / `bytedance-seedream-5.0-pro-edit` | 1K or 2K, up to 10 source images for edits |
| Seedream 4.5 | Text, picture | `bytedance-seedream-v4.5` / `bytedance-seedream-v4.5-edit` | `quality`: basic or high |
| Qwen Image 3.0 (and Pro) | Text, picture | `qwen3-text-to-image` / `qwen3-image-to-image` (`qwen3-pro-…` for Pro) | 1k or 2k, up to 3 source images |
| Qwen Image 2.0 (and Pro) | Text, picture | `qwen-image-2.0` / `qwen-image-2.0-edit` (`-pro` for Pro) | Aspect ratio only |
| Wan 2.7 Image | Text, picture | `wan2.7-text-to-image` / `wan2.7-image-edit` | Up to 9 source images for edits |
| Grok Imagine | Text | `grok-imagine-text-to-image`, `grok-imagine-text-to-image-quality`, `grok-imagine-image-2` | Five aspect ratios |
| Z-Image Turbo | Text | `z-image-turbo` | Set `width` and `height` instead of an aspect ratio |

Field names come from Muapi's endpoint definitions as of November 2026; see [MODELS.md](MODELS.md) for a short "which one should I pick" guide, and the live Muapi pages for current pricing.

## Using the Generic node

Pick an endpoint from the table and send the fields it needs. Text-to-image on Seedream 5.0 Pro:

```json
{"prompt": "A cinematic editorial portrait with dramatic red lighting", "aspect_ratio": "2:3", "resolution": "2K"}
```

Editing on Seedream 4.5 (the node swaps `__file_1__` for your uploaded image):

```json
{"prompt": "Change the jacket to glossy black leather", "images_list": ["__file_1__"], "quality": "high"}
```

Fields differ between families, so do not copy a payload from one endpoint to another unchanged. For example Seedream 5.0 Pro uses capital `1K`/`2K` while Qwen Image 3.0 uses lowercase `1k`/`2k`.

## Honest limits

- **It is pay as you go.** The node pack and these guides are free. Each image you generate is billed by Muapi, so there are no free generations.
- **No graphics card needed, but ComfyUI still runs locally.** You need an internet connection and a Muapi API key.
- **Moderation varies by model and can change.** "Uncensored" here describes models with lighter filtering than mainstream tools, not a promise of unrestricted output. Test your own prompts and follow the law and the platform [terms](https://muapi.ai/terms).
- **Never use real people's photos to make intimate or non-consensual images.** That is not allowed on any Muapi endpoint.

## Related Projects

- [muapi-comfyui](https://github.com/SamurAIGPT/muapi-comfyui): the node pack and example workflows used in this guide.
- [uncensored-ai-video-generator-comfyui](https://github.com/Anil-matcha/uncensored-ai-video-generator-comfyui): the video version of this guide.
- [Spicy-AI-Image-Generator-API](https://github.com/Anil-matcha/Spicy-AI-Image-Generator-API): request schemas, cURL and Python examples for the same image endpoints.
- [awesome-uncensored-ai-image-models](https://github.com/Anil-matcha/awesome-uncensored-ai-image-models): a community catalog of open, low-filter AI image models.
- [Muapi](https://muapi.ai): the API behind the nodes. See the [spicy AI image generator page](https://muapi.ai/ai-spicy-image-generator).

## License

[MIT](LICENSE)
