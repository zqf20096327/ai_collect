# synthid-remover

[![MIT license][license-badge]](LICENSE)
[![Python 3.14][python-badge]](#installation)
[![Experimental][status-badge]](#limits)
[![GitHub issues][issues-badge]](https://github.com/balyakin/synthid-remover/issues)

A girl beside a pond. Ducks in the grass. An invisible signal tucked into the pixels.

**synthid-remover** is a collection of Python tools for experimenting with pixel-level
[SynthID watermarks](https://deepmind.google/models/synthid/). Its main approach replaces a selected band of
image detail with the corresponding band from a processed donor, keeping much of the original picture around it.
The scene stays recognisable. The texture changes.

The example below passed the author's manual watermark check. One image, one measured result;
other images need their own checks.

## Before and after

Click either image to open the full-resolution PNG.

| Original | Cleaned |
| --- | --- |
| [![Girl with ducks, original][original-image]][original-image] | [![Cleaned version][cleaned-image]][cleaned-image] |

Both files are **1536 × 1024**. The cleaned example uses `--split-sigma 1.2 --correct 8`,
`--keep-share 0.12`, and `--match-window 12`.

| Measurement | Cleaned example |
| --- | --- |
| Mean absolute pixel difference, on a 0–255 scale | **16.91** |
| PSNR against the original | **20.68 dB** |
| Recorded manual SynthID check | **Not detected** |

The detector result comes from the author's experiment recorded on October 9, 2026. It is not a fresh check
performed whenever this README is opened. The numerical measurements can be recalculated from the two bundled files.

## How it works

Blurring an image at two scales gives a band of detail between them. `bandmix.py` swaps that band with one from
a donor and blends back a chosen share of the original. Finer detail and broader shading come from the source;
local contrast matching helps the borrowed texture fit. Clipping and quantisation can still affect pixels elsewhere.

Where does the donor come from? `remaster.py` uses Stable Diffusion 1.5 with ControlNet Canny to repaint the scene
from its edges. That intermediate image can look quite different. It supplies the replacement band rather than
becoming the final picture outright.

The successful recipe used Gaussian scales of **1.2 and 8 pixels**. Those are experimental settings for this
example, not a universal map of where every SynthID watermark lives.

## Installation

Use **Python 3.14** to match the working source environment. Both dependency files pin the direct dependencies
installed there: the lightweight tools use Pillow 12.1.1 and NumPy 2.4.4, while the separate ML environment uses
its own tested versions. Earlier Python versions have not been validated for this release.

```bash
git clone https://github.com/balyakin/synthid-remover.git
cd synthid-remover
python3.14 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

That is enough for `bandmix.py`, the classical processing tools, and the metrics. To generate donors or run
GAN restoration, install the heavier dependencies separately:

```bash
python3.14 -m venv .venv-restore
.venv-restore/bin/python -m pip install -r requirements-diffusion.txt
```

The ML tools were run on macOS with Apple Silicon and PyTorch MPS. Their device selection falls back to CPU
when MPS is unavailable. The pinned PyTorch build requires macOS 14 or later on Apple Silicon.
The first donor run downloads several gigabytes of model weights into the Hugging Face cache;
those weights are not part of this repository.

## Process an image

Start with a donor. You do not need to describe every scene: `remaster.py` uses this general prompt by default:

> a photograph, natural light, sharp focus, fine detail, realistic textures

The original supplies the contours. If a scene needs more guidance, add a description with `--prompt`.
Write generated files into `candidates/` so they stay out of Git.

```bash
mkdir -p candidates
.venv-restore/bin/python remaster.py autumn-10x15-yellow-v2.png candidates/donor.png \
  --controlnet lllyasviel/control_v11p_sd15_canny \
  --control-mode canny --control-blur 0 --pre-blur 0 \
  --controlnet-scale 1.0 --strength 0.9 --steps 30 \
  --tile 640 --overlap 256
```

Then borrow the selected band:

```bash
.venv/bin/python bandmix.py autumn-10x15-yellow-v2.png candidates/donor.png candidates/cleaned.png \
  --split-sigma 1.2 --correct 8 --keep-share 0.12 --match-window 12
```

For another image, replace the input path in both commands. Each original needs its own donor: **ten different
photos mean ten donors**. The donor and original must have identical dimensions; once generated, a donor can
be reused while you tune the band-mixing settings. `bandmix.py` itself takes no prompt.

These commands demonstrate the workflow. The bundled cleaned image was produced with a scene-specific donor
prompt; a new donor made with the general default may change the texture and the detector result.

Four controls do most of the useful work:

| Flag | Effect |
| --- | --- |
| `--split-sigma` | Lower Gaussian scale of the replacement band |
| `--correct` | Upper Gaussian scale; zero replaces all detail coarser than the lower scale |
| `--keep-share` | Fraction of the original band retained, from 0 to 1 |
| `--match-window` | Scale of local contrast matching; zero disables it |

In the recorded experiment, retaining 10% or 12% of the original band passed the manual check. At 15%, the
watermark was detected again. A small movement of the dial can matter. Check the actual output.

Use `--help` for the remaining options. Alignment, phase scrambling, amplitude thresholds, local shuffling,
and luminance-only mixing are experimental controls; the example above does not require them.
Luminance-only mixing rejects active contrast matching, alignment, phase scrambling, adaptive shares, and
shuffling controls. Their auxiliary options must retain their defaults. Numeric controls are checked before processing.

## Check the result

Upload the output to [OpenAI Verify](https://openai.com/verify/) and read the **SynthID** result separately
from the metadata result. Removing EXIF or C2PA metadata alone does not remove a signal embedded in the pixels.

If your OpenAI organization has access to the Content Provenance API, the included client can check a file:

```bash
export OPENAI_API_KEY="your-api-key"
.venv/bin/python provenance_check.py candidates/cleaned.png
```

The client uploads the image to `POST /v1/content_provenance_checks` and logs the SynthID outcome. API uploads
are limited to 50 MiB per file, and rate limits apply. See the
[official API documentation](https://developers.openai.com/api/docs/guides/content-provenance).
The web tool is the simplest route if you do not have API access.

**Not detected** means the verifier did not find the supported watermark. It does not establish that a picture
was made without AI. [OpenAI explains how to interpret the result](https://openai.com/verify/).

## What else is included

Some experiments failed. They are still useful as comparisons, so the scripts are included with their roles
spelled out rather than presented as interchangeable removal methods.

| File | Purpose |
| --- | --- |
| [`bandmix.py`](bandmix.py) | Main tool: replace and blend a selected band from a donor |
| [`remaster.py`](remaster.py) | Generate a donor with ControlNet Canny or Tile |
| [`sinthid_remover.py`](sinthid_remover.py) | Classical perturbation chain and image fidelity metrics |
| [`restore.py`](restore.py) | GAN upscale/downscale restoration using a local checkpoint |
| [`recapture.py`](recapture.py) | Simulate a print-and-camera round trip, including halftoning |
| [`mottle.py`](mottle.py) | Apply smooth tone and chroma perturbations |
| [`provenance_check.py`](provenance_check.py) | Upload images to the OpenAI verification API |
| [`test_sinthid_remover.py`](test_sinthid_remover.py) | Tests for processing, formats, metadata, and error handling |
| [`test_remaster.py`](test_remaster.py) | Optional ML tests for tile geometry and conditioning modes |

On the example image, classical perturbations, GAN restoration, halftoning, and print/camera simulation left
SynthID detectable. ControlNet Tile did too. ControlNet Canny donors and the selected band replacement produced
the recorded successful checks. `mottle.py` has no recorded successful detector result.

For a classical comparison run:

```bash
.venv/bin/python sinthid_remover.py autumn-10x15-yellow-v2.png candidates/classical.png \
  --strength balanced --seed 20251008
```

The name `sinthid_remover.py` retains the original spelling for existing imports. The repository uses
`synthid-remover`, matching the watermark's name.

## Files and metadata

The processing tools write PNG or JPEG outputs. Frame dimensions, DPI, and an available ICC profile are
carried over; EXIF, XMP, and textual metadata are omitted. The band mixer retains the source alpha channel,
while the classical chain transforms transparency alongside the picture. JPEG output flattens transparency
onto white. Use PNG for comparisons to avoid an extra lossy encoding step.

Only the original and cleaned girl-with-ducks images are bundled. Generated candidates, model checkpoints,
virtual environments, local credentials, IDE files, and private working notes are excluded from publication.

## Limits

This is an experimental image-processing project. The published evidence covers **one scene**, and detector
behaviour can change. Grass, reeds, fabric, and other dense textures make the differences easier to see;
open the full-size images before deciding whether the trade-off suits your use.

Donor generation depends on the model, prompt, hardware, and library versions. A seed helps repeat a run on
the same setup; it does not promise identical output across machines. The image tools also hold several
floating-point copies of a frame in memory, so large inputs can consume substantial RAM.

Rotate images with EXIF orientation into their intended pixel orientation before processing: the tools omit
that metadata without applying its rotation. All processing tools enforce the same image size limit before decoding.

Use images you have the right to process and keep their origin clear when sharing them.

## Development

```bash
.venv/bin/python -m pip install pytest==9.0.2
.venv/bin/python -m pytest -q
```

The tests exercise the classical chain's reproducibility, alpha handling, image modes, metadata retention,
metrics, and failure paths. Donor tests are skipped when the optional ML dependencies are absent.
To run them in the ML environment:

```bash
.venv-restore/bin/python -m pip install pytest==9.0.2
.venv-restore/bin/python -m pytest -q test_remaster.py
```

The tests do not call the external watermark detector or download models.

## License

[MIT](LICENSE). Copyright (c) 2026 **Evgeny Balyakin**.

[license-badge]: https://img.shields.io/badge/license-MIT-3b8244
[python-badge]: https://img.shields.io/badge/python-3.14-3776ab?logo=python&logoColor=white
[status-badge]: https://img.shields.io/badge/status-experimental-d59b28
[issues-badge]: https://img.shields.io/github/issues/balyakin/synthid-remover
[original-image]: autumn-10x15-yellow-v2.png
[cleaned-image]: autumn-10x15-yellow-v2.clean.png
