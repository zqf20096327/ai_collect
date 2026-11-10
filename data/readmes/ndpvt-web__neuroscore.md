<div align="center">

# neuroscore

**The neural content intelligence engine.**

TRIBE v2 predicts brain activity. neuroscore tells you what it means.

[![PyPI version](https://img.shields.io/pypi/v/neuroscore.svg)](https://pypi.org/project/neuroscore/)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)
[![Built with TRIBE v2](https://img.shields.io/badge/built%20with-Meta%20TRIBE%20v2-blue)](https://github.com/facebookresearch/tribev2)

[Documentation](#cli-reference) | [Quick Start](#quick-start) | [Python API](#python-api) | [Architecture](#architecture)

</div>

---

Score any video, audio, or text for predicted neural engagement. Get back plain-English findings: where your content grabs attention, where it loses the audience, and what to fix. One command. No scanner. No lab.

```
$ neuroscore score pitch_deck.mp4

NEURAL ENGAGEMENT REPORT
Score: 5.2 / 10.0

Findings:
  [!] CRITICAL 0:09-0:15 -- Analytical resistance precedes value recognition
      dlPFC peaked at 9.5s but vmPFC only activated at 15.0s.
      The brain was resisting before it recognized any value.
      Fix: Move value/benefit messaging earlier in the content.
```

---

## neuroscore vs TRIBE v2

[TRIBE v2](https://github.com/facebookresearch/tribev2) is Meta FAIR's brain encoding foundation model. It takes media and outputs a raw fMRI-like tensor of shape `(timesteps, 20484)` -- 20,000+ cortical activation values per half-second. It is a research instrument built for neuroscientists.

**neuroscore is the interpretation layer.** It takes that raw tensor and turns it into something you can act on: named brain regions, temporal engagement scores, problem detection, A/B comparison, and natural-language recommendations. It is built for content creators, marketers, educators, researchers, and developers who want brain-level feedback without reading fMRI papers.

| | TRIBE v2 | neuroscore |
|---|---|---|
| **Outputs** | Raw cortical activation tensor | Named regions, scores, findings, suggestions |
| **Audience** | Neuroscience researchers | Content creators, developers, marketers, educators |
| **Interface** | Python research API | CLI + Python library |
| **Requires** | fMRI expertise to interpret results | No neuroscience background needed |
| **Effort** | Write parsing code for 20,484 vertices | `neuroscore score video.mp4` |

---

## Quick Start

### Zero-setup demo (no GPU, no downloads)

```bash
pip install neuroscore
neuroscore demo
```

Pre-computed examples ship with the package. Full neural engagement reports in seconds.

### Score your content

```bash
# Video
neuroscore score my_presentation.mp4

# Audio
neuroscore score podcast_episode.mp3

# Text (inline or file)
neuroscore score "Limited time offer -- get started free today"
neuroscore score email_draft.txt

# A/B neural diff
neuroscore compare version_a.mp4 version_b.mp4

# Accessibility scan (content warnings)
neuroscore score video.mp4 --mode accessibility

# Score a YouTube video directly
neuroscore youtube https://youtube.com/watch?v=dQw4w9WgXcQ

# HTML report with interactive brain heatmap
neuroscore score pitch.mp4 --format html --save report.html

# JSON for pipelines
neuroscore score pitch.mp4 --format json --save report.json
```

### Check available backends

```bash
neuroscore backends
```

---

## Python API

```python
from neuroscore import score, compare

report = score("my_video.mp4")
print(report.overall_score)  # 7.2
print(report.summary)

# Brain region data
print(report.region_map.amygdala.peak_value)      # 0.82
print(report.region_map.amygdala.peak_time_sec)    # 1.5
print(report.region_map.vmpfc.mean_value)          # 0.68

# Findings
for finding in report.findings:
    print(f"[{finding.severity}] {finding.title}")
    if finding.suggestion:
        print(f"  Fix: {finding.suggestion}")

# A/B comparison
diff = compare("v1.mp4", "v2.mp4")
print(diff.summary)
```

---

## What neuroscore Measures

neuroscore extracts seven brain regions from the TRIBE v2 cortical mesh and tracks their activation over time.

| Region | Name | What It Tells You |
|--------|------|-------------------|
| **Amygdala** | Relevance Gate | Did the content register as personally relevant? Must activate in the first 3 seconds or the brain classifies it as noise. |
| **ACC** | Decision Weighing | Is the viewer genuinely considering a decision? Moderate ACC means engagement. Too low means dismissed without thought. |
| **dlPFC** | Analytical Resistance | Is the viewer looking for reasons to say no? If this fires before value recognition, you lose the audience. |
| **vmPFC** | Value Recognition | Is the viewer mentally simulating the benefits? This is the "I want this" signal. |
| **Striatum** | Reward Drive | Is the viewer motivated to act? Co-activation with vmPFC is the strongest engagement predictor. |
| **Auditory** | Sound Processing | How strongly is the auditory channel engaged? Higher for speech-driven and music-rich content. |
| **Visual** | Visual Processing | How strongly is the visual channel engaged? Higher for video with dynamic visual complexity. |

### The Persuasion Sequence

neuroscore checks whether brain regions activate in the optimal order for engagement:

```
Amygdala (0-3s)  -->  ACC (3-10s)  -->  vmPFC (10-30s)  -->  dlPFC (after vmPFC)
"This matters"       "I'm weighing"    "I see the value"    "Let me analyze"
```

When dlPFC (resistance) fires **before** vmPFC (value), the brain is counter-arguing before it has recognized any benefit. neuroscore flags this as a critical finding.

---

## Architecture

Contract-based pipeline. Every layer has a clean interface. Every component is swappable.

```
Input (video / audio / text)
  --> Backend (GPU / CPU / Cloud / Demo)      swappable, auto-detected
  --> BrainActivation                          raw tensor (timesteps x 20484)
  --> ROI Extraction                           20,484 vertices -> 7 named regions
  --> RegionMap                                the central data structure
  --> Mode (score / compare / ...)             pluggable analysis layer
  --> NeuroReport                              unified output model
  --> Formatter (terminal / JSON)              same data, two views
```

### Backends

Auto-detected in priority order. Falls back gracefully.

| Backend | Requirements | Speed | Fidelity |
|---------|-------------|-------|----------|
| **GPU** | `pip install neuroscore[gpu]` + NVIDIA 16GB+ | 15-60s / 30s video | Full TRIBE v2 |
| **CPU** | `pip install neuroscore[gpu]` | Minutes / video | Full TRIBE v2 |
| **Cloud** | `NEUROSCORE_CLOUD_URL` env var | Network dependent | Full TRIBE v2 |
| **Demo** | Nothing | Instant | Synthetic |

### Extending neuroscore

Add a new analysis mode in one file. No core changes.

```python
# modes/accessibility.py
from neuroscore.modes.base import Mode, ModeResult
from neuroscore.core.regions import RegionMap

class AccessibilityMode(Mode):
    name = "accessibility"
    description = "Scan for neurological intensity triggers"

    def analyze(self, region_map: RegionMap, **kwargs) -> ModeResult:
        # Your analysis logic
        ...
```

```bash
neuroscore score video.mp4 --mode accessibility
```

Same pattern for new backends and output formats.

---

## Installation

```bash
# Basic (demo mode, no GPU needed)
pip install neuroscore

# With GPU support (real TRIBE v2 scoring)
pip install neuroscore[gpu]

# With YouTube support
pip install neuroscore[youtube]

# Development
git clone https://github.com/ndpvt-web/neuroscore.git
cd neuroscore
pip install -e ".[dev]"
```

---

## Use Cases

**Content creators** -- Score videos and copy before publishing. Find where the audience disengages.

**Sales teams** -- A/B test pitch decks and cold emails neurologically. Value before resistance.

**Educators** -- Identify which lecture segments lose student attention. Restructure for retention.

**UX researchers** -- Score onboarding flows and app screens for cognitive friction.

**Neuroscience researchers** -- Computational experiments at scale. No scanner needed.

**Accessibility teams** -- Detect neurologically intense content moments. Automate content warnings.

---

## CLI Reference

| Command | Description |
|---------|-------------|
| `neuroscore score <input>` | Score content for neural engagement |
| `neuroscore compare <a> <b>` | A/B neural diff between two inputs |
| `neuroscore youtube <url>` | Download and score a YouTube video |
| `neuroscore demo` | Pre-computed examples (no GPU needed) |
| `neuroscore backends` | Show available backends and status |

| Flag | Description |
|------|-------------|
| `--mode <name>` | Analysis mode: `score`, `compare`, `accessibility` |
| `--backend <name>` | Force backend: `gpu`, `cpu`, `cloud`, `demo` |
| `--format <type>` | Output: `terminal` (default), `json`, `html` |
| `--raw` | Include full timecourse data |
| `--save <path>` | Save report to file (JSON or HTML) |

---

## API Reference

```python
neuroscore.score(input, mode="score", backend=None) -> NeuroReport
neuroscore.compare(input_a, input_b, backend=None)  -> NeuroReport
```

**NeuroReport**

| Attribute | Type | Description |
|-----------|------|-------------|
| `overall_score` | `float` | 0.0 - 10.0 engagement score |
| `summary` | `str` | Natural language analysis |
| `findings` | `list[Finding]` | Detected patterns and suggestions |
| `region_map` | `RegionMap` | Full brain region data |
| `to_dict()` | `dict` | JSON-serializable output |

**Finding**

| Attribute | Type | Description |
|-----------|------|-------------|
| `severity` | `str` | `info`, `warning`, `critical` |
| `title` | `str` | Short description |
| `detail` | `str` | Full explanation |
| `suggestion` | `str \| None` | Recommended fix |
| `region` | `str \| None` | Primary brain region |
| `start_sec` | `float \| None` | Start time in content |

**RegionMap**

| Accessor | Returns |
|----------|---------|
| `region_map.amygdala` | `RegionTimecourse` |
| `region_map.acc` | `RegionTimecourse` |
| `region_map.dlpfc` | `RegionTimecourse` |
| `region_map.vmpfc` | `RegionTimecourse` |
| `region_map.striatum` | `RegionTimecourse` |

Each `RegionTimecourse` has: `.values`, `.peak_value`, `.peak_time_sec`, `.mean_value`, `.onset_time_sec`

---

## Roadmap

- [x] Core scoring engine with TRIBE v2 integration
- [x] CLI: score, compare, demo, backends
- [x] Python API with type hints
- [x] Four backends: GPU, CPU, cloud, demo
- [x] Score mode (engagement analysis with temporal sequence detection)
- [x] Compare mode (A/B neural diff)
- [x] JSON output for pipelines
- [x] HTML report with interactive brain heatmap and timeline
- [x] Accessibility mode (neurological trigger detection + content warnings)
- [x] YouTube integration (`neuroscore youtube <url>`)
- [ ] Study mode (lecture retention optimization)
- [ ] Present mode (presentation neural coaching)
- [ ] UX mode (screen flow neural audit)
- [ ] Streaming backend for real-time scoring
- [ ] Web dashboard

---

## Built On

| Component | Role |
|-----------|------|
| [TRIBE v2](https://github.com/facebookresearch/tribev2) | Brain encoding foundation model (Meta FAIR) |
| [fsaverage5](https://surfer.nmr.mgh.harvard.edu/) | Cortical surface atlas (~20,484 vertices) |
| [Rich](https://github.com/Textualize/rich) | Terminal output |
| [Click](https://github.com/pallets/click) | CLI framework |

---

## Citation

```bibtex
@software{neuroscore2026,
  title={neuroscore: Neural Content Intelligence Engine},
  url={https://github.com/ndpvt-web/neuroscore},
  year={2026}
}

@article{dAscoli2026TribeV2,
  title={A foundation model of vision, audition, and language for in-silico neuroscience},
  author={d'Ascoli, St\'{e}phane and Rapin, J\'{e}r\'{e}m\'{e} and Benchetrit, Yohann
          and Brookes, Teon and Begany, Katelyn and Raugel, Jos\'{e}phine
          and Banville, Hubert and King, Jean-R\'{e}mi},
  year={2026}
}
```

---

## License

**neuroscore** (this package): [Apache 2.0](LICENSE)

**TRIBE v2** (model weights): [CC-BY-NC-4.0](https://creativecommons.org/licenses/by-nc/4.0/) -- non-commercial use only when using GPU/CPU backends with real model weights.

---

## Contributing

The architecture is designed for extension:

- **New mode**: One file in `modes/`, implement the `Mode` interface
- **New backend**: One file in `core/backends/`, implement the `Backend` interface
- **New output format**: One file in `output/`, consume `NeuroReport`

No core changes needed. See [Architecture](#architecture).

---

<details>
<summary><strong>Search and Discovery Tags</strong></summary>

<br>

`brain activity prediction tool` `neural engagement scoring` `fMRI prediction without scanner` `computational neuroscience CLI` `Meta TRIBE v2 wrapper` `TRIBE v2 content scoring` `brain encoding model tool` `predict brain response to video` `predict brain response to text` `predict brain response to audio` `neuromarketing open source` `neural A/B testing tool` `content neural optimization` `sales pitch brain scoring` `presentation neural feedback` `lecture engagement predictor` `amygdala activation analysis` `prefrontal cortex engagement tool` `vmPFC reward prediction model` `cortical activation mapping tool` `fsaverage5 brain parcellation` `fMRI response prediction software` `in-silico neuroscience tool` `computational brain scoring model` `content effectiveness neural scoring` `persuasion sequence analysis` `audience attention neural prediction` `cognitive engagement measurement` `neural content intelligence` `video engagement brain predictor` `email copy neural scoring` `podcast engagement brain analysis` `open source neuroscience Python tool` `pip install brain scoring` `CLI brain activity analysis` `Python neural engagement API` `brain region content scoring` `content optimization neuroscience` `digital neuromarketing tool` `AI content brain feedback`

</details>
