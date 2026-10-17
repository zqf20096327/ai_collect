# ComfyUI-CachedSearch

Best-of-N seed search for video (and image) models at about 60% of the cost. The N drafts are sampled with ComfyUI's native EasyCache, a verifier scores them, and only the winning seed is sampled again at full compute. Sampling is seed-deterministic, so the latent you get is exactly what full best-of-N would have delivered whenever both pick the same seed.

Paper: [CachedSearch: Training-Free Cached Exploration for Test-Time Search in Video Diffusion](https://arxiv.org/abs/2607.23159) (Saini, Birkbeck, Wang, Adsumilli, Bovik). Python package for diffusers: [`pip install cachedsearch`](https://github.com/shreshthsaini/CachedSearch). Blog: [Explore every candidate under caching, spend full compute only on the winner](https://shreshthsaini.github.io/blogs/cachedsearch.html).

## Install

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/shreshthsaini/ComfyUI-CachedSearch
pip install -r ComfyUI-CachedSearch/requirements.txt   # image-reward, for the default verifier
```

Restart ComfyUI. Requires a ComfyUI build that ships the native `EasyCache` node (`comfy_extras/nodes_easycache.py`).

## Nodes

**CachedSearch Sampler (best-of-N, cached drafts)**, category `sampling/CachedSearch`. Drop-in for `KSampler`, with these extra inputs:

| Input | What it does |
|---|---|
| `vae` | Decodes each draft so the verifier can score it |
| `prompt` | The text the verifier scores against (the same prompt you encoded into `positive`) |
| `verifier` | A `CS_VERIFIER`, for example from the ImageReward node below |
| `search_width` | N. Candidates use `seed`, `seed+1`, ..., `seed+N-1` |
| `cache_threshold`, `cache_start_percent`, `cache_end_percent` | EasyCache settings for the drafts. Higher threshold skips more steps. 0.2 is the EasyCache default; calibrate per model family |
| `commit` | Re-sample the winner with caching off (recommended). Off returns the cached draft itself |

Outputs: the winning `LATENT`, the `winner_seed` (feed it to a plain KSampler to reproduce the result), and `draft_scores` as a JSON string.

**CachedSearch ImageReward Verifier**: the paper's verifier, ImageReward averaged over uniformly spaced frames. Any node that outputs a `CS_VERIFIER` object with a `score(images, prompt) -> float` method works in its place.

## Wiring

Model loader, CLIP text encodes, and an empty latent as usual, then:

```
CachedSearch ImageReward Verifier ──┐
Model / positive / negative / latent / VAE ──> CachedSearch Sampler ──> VAE Decode ──> Save
```

Type the prompt into the sampler's `prompt` box as well, so the verifier sees it. Do not attach the EasyCache node yourself; the sampler applies it to the drafts and samples the winner without it.

## Choosing settings

- `search_width` 4 to 8. Recommitting the winner pays off from about 4 candidates.
- `cache_threshold`: the paper calibrates one threshold per model family. Start at the EasyCache default (0.2) for Wan; lower it if the draft ranking disagrees with your eye, raise it for cheaper drafts.
- Every draft is VAE-decoded for scoring, which costs time and memory on video models. On small GPUs reduce `search_width` rather than `frames_to_score`, since the VAE decodes the whole clip either way.

## Citation

```bibtex
@article{saini2026cachedsearch,
  title   = {CachedSearch: Training-Free Cached Exploration for Test-Time Search in Video Diffusion},
  author  = {Saini, Shreshth and Birkbeck, Neil and Wang, Yilin and Adsumilli, Balu and Bovik, Alan C.},
  journal = {arXiv preprint arXiv:2607.23159},
  year    = {2026}
}
```
