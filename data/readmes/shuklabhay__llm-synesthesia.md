# llm-synesthesia

![banner](.github/assets/banner.gif)

LLM emotional state extraction/visualization pipeline, inspired by the neurological phenomenon 'synesthesia,' interfaced with via Hermes Agent.

## How It Works

- Hermes-4.3-36B generates the next token on Modal
- Layer-48 hidden states are EMA-smoothed and passed through an emotion MLP probe
- The probe predicts distribution of 9 emotions:
  `anger`, `joy`, `sadness`, `fear`, `curiosity`, `confidence`, `confusion`, `disgust`, `tenderness`
- Emotion probabilities are mapped into 2D emotion-space anchors for `x/y`
- Logit and hidden-state stats become renderer controls like `rotation`, `branching`, `glow`, `density`, `diffusion`, and `gate`
- These values are injected into WebGL2 flow field as color and velocity splats

## Setup

**Requirements**: Python 3.12+, `uv`, Modal account for training/serving, WebGL2-capable browser. Hermes Agent is optional.

### 1. Install dependencies

```bash
uv sync --group dev --group training
```

### 2. Authenticate Modal

```bash
modal setup
```

### 3. Optional: install Hermes Agent

You only need Hermes Agent if you want the full local `hermes` flow instead of just running the bridge/renderer.

## Usage

### 1. Train artifacts on Modal

```bash
# Train the emotion probe
uv run modal run training/emotion_probe.py

# Build EMA baseline stats used at inference
uv run modal run training/head.py
```

### 2. Deploy inference

```bash
uv run modal deploy training/inference_modal.py
```

Copy the deployed Modal URL and export it:

```bash
export SYNESTHESIA_MODAL_URL="https://your-modal-endpoint"
```

### 3. Optional: configure Hermes Agent provider

If you want Hermes Agent to talk to the synesthesia endpoint, copy the provider and merge the YAML snippet into your Hermes config.

```bash
mkdir -p ~/.hermes/providers
cp training/hermes_synesthesia_provider.py ~/.hermes/providers/
```

Then use `training/hermes_config_snippet.yaml` as the baseline for your Hermes provider config and point it at `SYNESTHESIA_MODAL_URL`.

### 4. Run locally against the Modal endpoint

Full local flow with Hermes Agent:

```bash
uv run python -m server.main --mode hermes
```

Bridge + renderer only, without launching Hermes Agent:

```bash
uv run python -m server.main --mode hermes-bridge --modal-url "$SYNESTHESIA_MODAL_URL"
```

Renderer-only mock mode:

```bash
uv run python -m server.main --mode random
```

## Project Structure

```text
llm-synesthesia/
├── server/
│   ├── main.py                          # Local entrypoint, static server, Hermes launcher
│   ├── hermes_bridge.py                 # Bridge from Hermes/OpenAI-style SSE to WebSocket params
│   ├── mock.py                          # Mock parameter generators for renderer-only testing
│   └── protocol.py                      # Splat parameter schema
├── renderer/
│   ├── index.html                       # Renderer entry page
│   ├── style.css                        # Basic UI styling
│   └── js/
│       ├── main.js                      # Browser client, WebSocket handling, animation loop
│       ├── splat.js                     # Maps params to fluid splats
│       ├── fluid.js                     # WebGL2 fluid simulation
│       ├── shaders.js                   # Shader sources
│       └── bloom.js                     # Bloom post-process pass
├── training/
│   ├── inference_modal.py               # Modal inference endpoint
│   ├── emotion_probe.py                 # Probe data collection and training
│   ├── head.py                          # EMA baseline stats builder for inference
│   ├── hermes_synesthesia_provider.py   # Hermes Agent provider wrapper
│   └── hermes_config_snippet.yaml       # Example Hermes provider config
├── pyproject.toml
└── README.md
```
