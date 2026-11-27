# hand-controller

Control any app or game with your hand, using only a webcam.

hand-controller watches one hand through the webcam and reports one of five states:
`RIGHT`, `LEFT`, `UP`, `DOWN` or `STOP`. It sends the state to your program as a small JSON
message over UDP, on every camera frame. It knows nothing about the app that receives it, so
any program that can open a UDP socket can use it: in any language and any engine.

<!-- Demo GIF placeholder: add docs/demo.gif and replace this line with ![Demo](docs/demo.gif) -->
*Demo GIF coming soon.*

## How it works

```
Webcam (OpenCV) -> MediaPipe Hand Landmarker -> classifier -> smoothing -> UDP JSON on 127.0.0.1:5005
```

1. **Capture:** the webcam image is mirrored, so pointing right on screen means right for you.
2. **Detection:** MediaPipe Hand Landmarker finds up to one hand and its 21 landmarks.
3. **Classification:** a rule-based classifier (or a model you train) turns the landmarks into a
   raw state. A pointing index finger gives a direction; anything else gives `STOP`.
4. **Smoothing:** a new direction must hold for 120 ms (STOP for 60 ms) before it is sent, so
   the output does not flicker.
5. **Output:** one JSON message per frame goes to UDP `127.0.0.1:5005`, even when nothing changed.
   The messages also act as a heartbeat.

Works on Linux (including Wayland) and Windows.

**Performance** (Fedora, 8 CPU cores, 640x480 webcam, GPU delegate): about 25-28 frames per second.
MediaPipe takes about 35 ms per frame. Run `uv run python tools/benchmark.py` to measure your machine.

## Install

You need [uv](https://docs.astral.sh/uv/getting-started/installation/). uv installs the pinned
Python version (3.12, see `.python-version`) for you.

```bash
git clone https://github.com/a2zrr/hand-controller.git
cd hand-controller
uv sync
uv run python tools/download_model.py   # downloads the MediaPipe model (about 8 MB), once
```

`uv sync` installs MediaPipe 0.10.x and `opencv-contrib-python`, so no manual steps are needed.
The model file is not stored in git.

## Run

```bash
uv run hand-controller
```

A debug window opens (mirrored camera, landmarks, the state in large text, raw state, FPS).
Press `q` or `Esc` in the window, or Ctrl+C in the terminal, to quit. Every state change is printed.

Useful flags (they override `config.toml`):

```bash
uv run hand-controller --camera 1            # another webcam
uv run hand-controller --no-window           # headless, no debug window
uv run hand-controller --port 6000           # another UDP port
uv run hand-controller --classifier model    # use a trained model (see below)
uv run hand-controller --help
```

You can start it from any folder with `uv run --project /path/to/hand-controller hand-controller`.

## Gestures

Only one hand is used (either hand works).

| Gesture | State |
|---|---|
| Index finger pointing; middle, ring and pinky curled (thumb ignored). The direction is where the index finger points: right, left, up or down. | `RIGHT` / `LEFT` / `UP` / `DOWN` |
| Open palm (all four fingers extended) | `STOP` |
| Fist | `STOP` |
| No hand, low confidence, or anything unclear | `STOP` |

Pointing diagonally (in the dead zone between two directions) gives `STOP` by default.

## Configuration

All settings are in `config.toml`, with the built-in defaults shown. Comments in the file explain
each one. Relative paths (config file, model files) are relative to the project folder.

| Section | Key | Default | Meaning |
|---|---|---|---|
| `[camera]` | `index`, `width`, `height` | `0`, `640`, `480` | Webcam and resolution |
| `[detection]` | `min_*_confidence` | `0.5` | MediaPipe thresholds |
| `[detection]` | `delegate` | `"auto"` | `auto` (GPU, falls back to CPU), `gpu` or `cpu` |
| `[detection]` | `swap_handedness` | `false` | Flip the reported Left/Right label (informational only) |
| `[classifier]` | `name` | `"rules"` | `"rules"` or `"model"` |
| `[classifier]` | `dead_zone_deg` | `20.0` | Gap between two direction sectors |
| `[classifier]` | `finger_extend_ratio` | `1.15` | How much farther the tip must be from the wrist than the PIP joint |
| `[smoothing]` | `direction_ms` | `120` | Time a direction must stay stable before it is sent |
| `[smoothing]` | `stop_ms` | `60` | Time `STOP` must stay stable before it is sent |
| `[output]` | `host`, `port` | `127.0.0.1`, `5005` | Where messages are sent |
| `[display]` | `window` | `true` | Debug window on/off |

## Protocol

One UDP datagram per frame, containing JSON:

```json
{"v":1,"state":"LEFT","confidence":0.94,"hand":"Right","ts":1732057200123}
```

**Consumer rule:** if no valid message has arrived for 300 ms, treat the state as `STOP`.

The full specification, with the field table and the receiving algorithm, is in
[docs/PROTOCOL.md](docs/PROTOCOL.md).

## Using it from your app

The idea is the same in every language. Read the latest message on each frame, apply the 300 ms
rule, then turn the state into a direction:

```text
hand = open UDP socket on 127.0.0.1:5005 (receive on a background thread)

every frame:
    if no message in the last 300 ms:  state = STOP
    else:                              state = latest message's state
    direction = RIGHT->(1,0)  LEFT->(-1,0)  UP->(0,-1)  DOWN->(0,1)  STOP->(0,0)
    move the player by direction
```

(In most screen coordinates Y grows downward, so UP is (0,-1). Flip the sign if your engine uses Y-up.)

Ready-made clients:

| Language | Location | Notes |
|---|---|---|
| C# / .NET 6+ | [clients/csharp](clients/csharp/README.md) | One file, `HandInput.cs`, plus a console example |
| Python | [clients/python](clients/python/hand_input.py) | `hand_input.py` (one class) and `listen.py` example |
| JavaScript (Node.js) | [clients/javascript](clients/javascript/handInput.js) | `handInput.js` (one class) and `listen.js` example |

Anything else (Unity, Godot, Unreal, Pygame, MonoGame, a browser or a microcontroller bridge)
only needs a UDP socket and the rule above, so you can write a client in a few dozen lines.

## Record, train and evaluate a model (optional)

The rules work out of the box. A trained model can be more accurate for your hand and lighting.

1. **Record.** Opens the camera with the debug view. Press `1`-`5` to start recording a label
   (`1` RIGHT, `2` LEFT, `3` UP, `4` DOWN, `5` STOP); press the same number again to stop.
   Make the gesture while recording. Record at least two sessions (different days or light),
   because the split is by session.
   ```bash
   uv run python tools/record.py
   ```
   Each session is saved to `data/session-<timestamp>.csv`.

2. **Train.** Trains a small neural network. The test set is whole sessions, never random
   frames, which avoids inflated scores. It prints accuracy, a per-class report and a confusion
   matrix, then saves `models/gesture_clf.joblib`.
   ```bash
   uv run python tools/train.py
   ```

3. **Evaluate.** Compares the rules and the model on the same held-out sessions.
   ```bash
   uv run python tools/evaluate.py
   ```

4. **Use the model.** Set `name = "model"` in `[classifier]`, or pass `--classifier model`.

Features for training and runtime come from one function, `src/hand_controller/features.py`:
the 21 landmarks relative to the wrist and scaled by the palm size, computed on the mirrored image.

## Testing

```bash
uv run pytest
```

The unit tests use synthetic hand landmarks. They do not need a camera or the MediaPipe model.

Without a camera, you can test any client with:

```bash
uv run python tools/fake_sender.py       # send states from the keyboard (arrows / WASD, space = STOP)
uv run python clients/python/listen.py   # print state changes
```

## Troubleshooting

**Camera cannot be opened.** The app prints the index it tried. Try `--camera 1` (or 2, 3).
Close other programs that use the webcam (video calls, OBS, browsers). On Linux, check that the
device exists (`ls /dev/video*`) and that your user can read it (the `video` group).

**Windows: camera permission.** Go to *Settings > Privacy & security > Camera* and turn on
*Let desktop apps access your camera*. Then restart the terminal.

**Lighting.** The hand must be clearly visible. Avoid strong light behind you and dim rooms.
If the state flickers, improve the light or raise `min_detection_confidence`.

**Debug window does not open on Wayland.** OpenCV's window uses X11, so it needs XWayland.
Install `xwayland-satellite`, make sure `DISPLAY` is set in the terminal you run the app from,
and restart the app. If it still fails, use `--no-window`. The app keeps working headless and
prints the same explanation.

**"Hand model not found".** Run `uv run python tools/download_model.py`.

**Left/Right label looks wrong.** The label is informational only; direction logic never uses it.
If it is reversed on your machine, set `swap_handedness = true` in `[detection]`.

**Low frame rate.** Run `uv run python tools/benchmark.py`. The app prints which delegate it uses.
If it says CPU, check your GPU/OpenGL drivers. `delegate = "cpu"` is slower but always works.

**Check the detector.** `uv run python tools/check_detector.py` prints what MediaPipe returns for
real webcam frames.

### macOS

**Crash on the first frame: `unsupported ImageFrame format: 1`.** On some Macs (seen on Apple
M4 with MediaPipe 0.10.35) the GPU delegate (Metal) aborts the process on the first frame. The
app cannot catch this, so `delegate = "auto"` does not help. Use the CPU delegate instead, which
works everywhere and is slower:

```toml
# config.toml
[detection]
delegate = "cpu"
```

**`AVCaptureDeviceTypeExternal is deprecated` warning.** This comes from macOS and is harmless.
Ignore it.

**macOS uses an iPhone instead of the built-in webcam.** With Continuity Camera, the iPhone can
appear as camera 0. Use the built-in webcam with `--camera 1` (or try 2).

## Project layout

```
src/hand_controller/   app, capture, detection, classifier, features, smoothing, output, protocol, config, dataset
tools/                 download_model, record, train, evaluate, fake_sender, check_detector, benchmark
clients/csharp/        HandInput.cs (.NET client) and its README
clients/python/        hand_input.py (client class) and listen.py (example)
clients/javascript/    handInput.js (client class) and listen.js (example)
docs/PROTOCOL.md       message format
tests/                 pytest unit tests (no camera)
```

## License

MIT. See [LICENSE](LICENSE).
