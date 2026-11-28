<p align="center">
  <img src="figures/logo.svg" alt="Auralis logo" width="112">
</p>

<h1 align="center">Auralis</h1>

<p align="center">
  <a href="https://github.com/frenchmarcel/auralis/actions/workflows/tests.yml"><img src="https://github.com/frenchmarcel/auralis/actions/workflows/tests.yml/badge.svg" alt="Tests"></a>
  <a href="https://auralis.readthedocs.io"><img src="https://readthedocs.org/projects/auralis/badge/?version=latest" alt="Documentation"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT licence"></a>
</p>

Auralis simulates the sound of a room and lets you listen to it. Load a
model, assign materials, and place sources and listeners. Auralis gives
binaural impulse responses, moving sources with Doppler, and ISO 3382
parameters.

**Documentation: [auralis.readthedocs.io](https://auralis.readthedocs.io)**

---

## How it works

Below a transition frequency, a **wave solver**
(FDTD, on the GPU) captures room modes, interference and diffraction. Above
it, **ray tracing and image sources** cover the rest of the audible range. A
crossover joins the two into one impulse response, rendered for headphones
with a measured head.

![Auralis engine overview: a wave-based FDTD solver and a geometrical-acoustics solver joined by a crossover at the transition frequency](figures/engine_overview.svg)

## Validated on BRAS

Auralis is validated against **BRAS**, the Benchmark for Room Acoustical
Simulation of TU Berlin: four rooms, and the reflection and diffraction
scenes. Materials come from the BRAS data. They are never tuned to the
measurements. Results, metrics and known errors are on the
[validation page](https://auralis.readthedocs.io/en/latest/validation/index.html).

## Performance

On a single RTX 2000 Ada (70 W):

- Ray tracer: **×25** faster than the multithreaded CPU engine
  (400 k rays × 200 bounces in 80 ms).
- FDTD: **≈ 2 Gcell/s** sustained. A full 10-pair CR2 run with a 600 Hz
  wave band takes **13 minutes** (an hour on the CPU).
- Everything falls back to native CPU code, then pure Python, with a clear
  message. Never silently.

## Quick start

```bash
# 1. Build the native engines (CUDA ones need nvcc)
bash native/build.sh
bash native/build_cuda.sh
bash native/build_cuda.sh --emulate

# 2. Check what was picked up
python3 -c "from auralis.engine import gpu_available, native_available; print(native_available(), gpu_available())"

# 3. Bake and listen: a furnished club, binaural IRs + convolved test signals
python3 examples/standalone_demo.py demo_out
python3 examples/demo_motion.py       # moving source, Doppler
```

Requirements: `docs/getting-started/installation.md`. Web app:
`bash webapp/start.sh` (see `webapp/README.md`).

## Licences

The code is under the MIT licence (`LICENSE`). Data has its own licences:
BRAS (CC BY-SA 4.0, `BRAS/LICENSE.md`), FABIAN head (CC BY 4.0), Odeon
(local research licence, never shared), OpenStreetMap (ODbL), Freesound and
Poly Haven (CC0). See `docs/reference/data-licences.md`.
