# SF6 AI Bot

A dual-mode AI system for Street Fighter 6 combining reinforcement learning training with LLM-powered real-time decision making.

## Architecture

The project has two independent operation modes:

**Training Mode** - Trains a PPO reinforcement learning agent using Stable-Baselines3 with a custom Gymnasium environment. The agent learns from screen capture observations and a structured reward signal.

**Juri AI Mode** - Uses DeepSeek R1:14B via Ollama for context-aware decision making. Analyzes game state through computer vision and executes Juri-specific combos, defensive options, and adaptive strategies.

## Prerequisites

- Windows 10/11
- Python 3.10+
- NVIDIA GPU with CUDA (recommended for training)
- Ollama with `deepseek-r1:14b` model (for Juri AI mode)
- vJoy (optional, for virtual controller input)

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Training parameters are defined in `config/training_config.yaml`. Juri-specific settings including move data, combos, automation behavior, and Ollama integration are in `config/juri_config.yaml`. Custom room safety settings are in `config/custom_room_config.yaml`.

## Usage

### Train a model

```bash
python train_bot.py --config config/training_config.yaml --total-timesteps 1000000
```

### Run trained model in real-time

```bash
python run_bot.py models/sf6_best_model.zip
```

### Launch Juri AI bot

```bash
python run_juri_bot.py --learning --config config/juri_config.yaml
```

### Custom room automation

```bash
python custom_room_bot.py models/sf6_best_model.zip --config config/custom_room_config.yaml
```

### Validate installation

```bash
python test_installation.py
```

## Project Structure

```
src/
  sf6_env.py            - Custom Gymnasium environment for SF6
  screen_capture.py     - High-performance screen capture via DXCam
  input_controller.py   - Virtual controller input via vJoy / keyboard
  reward_calculator.py  - Reward system for RL training
  callbacks.py          - Training callbacks (TensorBoard, checkpointing, early stopping)
  utils.py              - Configuration loading, logging, system utilities
  ollama_client.py      - DeepSeek R1:14B API client for Juri AI
  human_input_provider.py - Human-like input timing wrapper
  ollama_vision_provider.py - Multimodal frame analysis via Ollama
  combat_logger.py      - Markdown-based combat log writer
  n8n_client.py         - Async webhook client for external automation

config/
  training_config.yaml    - PPO hyperparameters, curriculum learning settings
  juri_config.yaml        - Juri move data, combos, automation, Ollama settings
  custom_room_config.yaml - Online safety limits, session management

train_bot.py            - PPO training entry point
run_bot.py              - Real-time inference with trained model
juri_ai_bot.py          - Juri AI main loop (Ollama decision making)
run_juri_bot.py         - Juri AI launcher with system validation
custom_room_bot.py      - Custom room automation with safety monitoring
test_installation.py    - Dependency and component verification
```

## Entry Points

| Script | Purpose |
|--------|---------|
| `train_bot.py` | Train PPO model in SF6 Training Mode |
| `run_bot.py` | Deploy trained model for real-time play |
| `juri_ai_bot.py` | Juri AI with LLM-based decision making |
| `run_juri_bot.py` | Juri AI launcher (validates Ollama, SF6, configs) |
| `custom_room_bot.py` | Automated online play with session safety limits |
| `test_installation.py` | Verify dependencies and component imports |

## Key Design Decisions

- **Observation**: 84x84 RGB frames captured at 60+ FPS via DXCam with MSS fallback
- **Action Space**: 21 discrete actions covering normals, specials, supers, and directional inputs
- **Reward Signal**: Damage dealt/taken, hit/block/parry outcomes, positional advantage, round results
- **Input Layer**: vJoy virtual joystick primary, Win32 keyboard fallback
- **LLM Integration**: DeepSeek R1:14B queried asynchronously to avoid blocking the combat loop
- **Persistence**: Learning data and combat logs stored as JSON and Markdown in `learning_data/` and `memory/`
