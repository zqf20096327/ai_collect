# Qwen Image API on MuAPI

Compare Qwen image generation and editing endpoints, then run a request with the same REST API shape across the Qwen model family. MuAPI provides unified access to these media endpoints; this repository is an independent integration guide and is not an official Alibaba Cloud or Qwen project.

- **MuAPI:** https://muapi.ai
- **Qwen API comparison and examples:** https://muapi.ai/qwen-api
- **Qwen Image playground:** https://muapi.ai/qwen-image
- **Qwen 2.1 playground:** https://muapi.ai/qwen-2.1
- **Create/manage an API key:** https://muapi.ai/access-keys
- **API introduction:** https://muapi.ai/docs/introduction
- **Pricing:** https://muapi.ai/pricing

## Related Projects

- [Open Generative AI](https://github.com/Anil-matcha/Open-Generative-AI) — practical generative-media API examples and model references.
- [OpenAI API examples](https://github.com/Anil-matcha/OpenAI-API) — compare another unified API covering image-generation and image-editing workflows.
- [Google Gemini Media API](https://github.com/Anil-matcha/Google-Gemini-Media-API) — image and video generation API examples.
- [MiniMax Media API](https://github.com/Anil-matcha/MiniMax-Media-API) — video, speech, music, and image editing examples.
- [Kling Video API](https://github.com/Anil-matcha/Kling-Video-API) — examples for another model-family API exposed through MuAPI.

## Qwen API scope

This is a **Qwen image API** guide. The live MuAPI catalog currently exposes Qwen image generation, image-to-image editing, LoRA-assisted image generation/editing, and LoRA training endpoints. It does not expose Qwen text/chat endpoints through this Qwen media catalog. Use Alibaba Cloud's official service for Qwen chat, embeddings, or other text-model APIs.

All examples use MuAPI's unified task API:

1. Submit `POST https://api.muapi.ai/api/v1/{endpoint}` with an `x-api-key` header and JSON body.
2. Read the returned `request_id`.
3. Poll `GET https://api.muapi.ai/api/v1/predictions/{request_id}/result` until the task is complete.

## Choose an endpoint

| Workflow | Endpoint | What it does | Required input |
|---|---|---|---|
| Text to image, Qwen 2.1 | `qwen2-1-text-to-image` | Qwen 2.1 1K/2K image generation; supports aspect ratio, transparent background, format, prompt enhancement, and seed | `prompt` |
| Image editing, Qwen 2.1 | `qwen2-1-image-to-image` | Edit or combine reference images; optional mask enables local edits | `prompt`, `images_list` |
| Text to image, Qwen 3 | `qwen3-text-to-image` | Qwen 3 image generation with 1K/2K resolution and prompt extension controls | `prompt` |
| Image editing, Qwen 3 | `qwen3-image-to-image` | Edit up to three reference images | `prompt`, `images_list` |
| Qwen Image 2.0 / Pro | `qwen-image-2.0`, `qwen-image-2.0-pro` | Generation endpoints with aspect-ratio control | `prompt` |
| Qwen Image 2.0 / Pro editing | `qwen-image-2.0-edit`, `qwen-image-2.0-pro-edit` | Image editing from reference image URLs | `prompt`, `images_list` |
| LoRA image workflows | `qwen-image-*-lora` | Generate or edit using supplied LoRA weights | Depends on endpoint; see schema below |
| Train a LoRA | `qwen-image-lora-trainer`, `qwen-image-2512-lora-trainer` | Train Qwen image LoRA weights from a dataset | `data` |

The comparison above is based on MuAPI's live model catalog and request schemas. Endpoint availability and inputs can change; check the model playground for the current form and availability before production use.

## Quick start: generate an image

Set your API key in the environment:

```bash
export MUAPI_KEY="your_muapi_api_key"
```

Submit a Qwen 2.1 text-to-image request:

```bash
curl -X POST "https://api.muapi.ai/api/v1/qwen2-1-text-to-image" \
  -H "x-api-key: $MUAPI_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A corgi wearing a yellow rain hat sitting on stone steps after the rain, shallow depth of field",
    "aspect_ratio": "16:9",
    "resolution": "1K",
    "output_format": "png"
  }'
```

The response includes a `request_id` and status. Use the result endpoint to retrieve the generated image URL after completion:

```bash
curl "https://api.muapi.ai/api/v1/predictions/REQUEST_ID/result" \
  -H "x-api-key: $MUAPI_KEY"
```

## Image editing example

`images_list` is a list of publicly reachable image URLs. Qwen 2.1 accepts 1–10 reference URLs; image order matters when the prompt refers to the first or second image. `mask_url` is optional and enables local editing when used with exactly one input image.

```bash
curl -X POST "https://api.muapi.ai/api/v1/qwen2-1-image-to-image" \
  -H "x-api-key: $MUAPI_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Replace the backpack in the first image with the colour scheme from the second image, and leave everything else unchanged",
    "images_list": [
      "https://example.com/backpack.jpg",
      "https://example.com/color-reference.jpg"
    ],
    "resolution": "1K",
    "aspect_ratio": "auto"
  }'
```

Replace the example URLs with image URLs that the API can access. The API receives URLs; this endpoint does not upload local files directly.

## Python example

Requires Python 3.9+ and `requests`. Run `python examples/qwen_image.py --help` for options. The script submits either a Qwen 2.1 generation or edit request and polls for the result.

```bash
python -m pip install -r requirements.txt
export MUAPI_KEY="your_muapi_api_key"
python examples/qwen_image.py --prompt "A tiny greenhouse on a rainy city rooftop at dusk"
```

For editing, provide one or more accessible reference URLs:

```bash
python examples/qwen_image.py \
  --mode edit \
  --prompt "Turn the product into a brushed aluminum desk lamp; keep the composition" \
  --image-url "https://example.com/product.jpg"
```

## Qwen 2.1 request schema

### `qwen2-1-text-to-image`

| Field | Type | Required | Accepted values / behavior |
|---|---|---:|---|
| `prompt` | string | Yes | Up to 5,000 characters; any language is supported |
| `aspect_ratio` | string | No | `1:1`, `4:3`, `3:4`, `3:2`, `2:3`, `16:9`, `9:16`, `21:9`, `9:21`; default `1:1` |
| `resolution` | string | No | `1K` or `2K`; default `1K` |
| `background` | string | No | `opaque` or `transparent`; default `opaque` |
| `output_format` | string | No | `png`, `webp`, or `jpeg`; default `png` |
| `enhance_prompt` | boolean | No | Prompt rewrite; default `true` |
| `seed` | integer | No | Omit for a random seed |

Transparent background is incompatible with JPEG.

### `qwen2-1-image-to-image`

| Field | Type | Required | Accepted values / behavior |
|---|---|---:|---|
| `prompt` | string | Yes | Describe the desired result; for masked edits, describe the white mask region |
| `images_list` | string[] | Yes | 1–10 publicly reachable reference image URLs; order is meaningful |
| `mask_url` | string | No | Inpainting mask; requires exactly one reference image |
| `aspect_ratio` | string | No | `auto`, `1:1`, `4:3`, `3:4`, `3:2`, `2:3`, `16:9`, `9:16`, `21:9`, `9:21` |
| `resolution` | string | No | `1K` or `2K`; default `1K` |
| `background` | string | No | `opaque` or `transparent`; default `opaque` |
| `output_format` | string | No | `png`, `webp`, or `jpeg`; default `png` |
| `enhance_prompt` | boolean | No | Ignored in local-edit mode |
| `seed` | integer | No | Optional seed |

## Response and polling

Submission returns a `request_id` and task status. Poll the predictions result endpoint with that ID. The Qwen 2.1 result schema contains `request_id` (identifier), `status` (current task state), and `output` (array of generated image URL strings). On completion, read the image URLs from `output`. Handle pending/processing statuses, terminal errors, and network timeouts in your client. Output URLs should be downloaded or copied to your own storage if you need long-term availability.

## Pricing and limits

MuAPI uses account credits and per-model billing. Exact costs can vary by model and settings such as output count or resolution. Check the live [MuAPI pricing page](https://muapi.ai/pricing) and each Qwen model's playground before submitting production workloads. The request examples do not promise a fixed cost, latency, or output availability period.

## Local verification

The Python example can be syntax-checked without an API key:

```bash
python -m py_compile examples/qwen_image.py
```

## License

MIT. MuAPI, Qwen, and Alibaba Cloud are trademarks of their respective owners. This repository is an independent community example and is not endorsed by Alibaba Cloud.
