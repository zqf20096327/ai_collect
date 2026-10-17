# IRIS - Gesture-Controlled Animatronic Eyes

**I**nteractive **R**obotic **I**ris **S**ystem - a pair of 3D-printed animatronic eyes, built on an Arduino Uno, that either move on their own with lifelike randomized behavior, or track your hand in real time through a webcam using computer vision.

[![Arduino](https://img.shields.io/badge/Arduino-Uno-00979D?logo=arduino&logoColor=white)](https://www.arduino.cc/)
[![Python](https://img.shields.io/badge/Python-3.9-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Hands-00A98F)](https://google.github.io/mediapipe/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Demo

[![Watch the demo](https://img.youtube.com/vi/2hhD0EJ27sg/maxresdefault.jpg)](https://youtube.com/shorts/2hhD0EJ27sg?si=DAM--uv17VH0sRSe)

*Click to watch the eyes track a hand in real time.*

---

## Table of Contents

- [What This Is](#what-this-is)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Bill of Materials](#bill-of-materials)
- [Wiring](#wiring)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Hand & Gesture Control](#hand--gesture-control)
- [The Robotics & AI/ML Behind It](#the-robotics--aiml-behind-it)
- [Troubleshooting](#troubleshooting)
- [Future Scope](#future-scope)
- [Contributing](#contributing)
- [License](#license)

---

## What This Is

IRIS drives two 3D-printed eyeballs - six servos total, three per eye (left-right, up-down, eyelid) - off a single Arduino Uno. It supports two independent operating modes that share the same underlying motion-control code:

1. **Autonomous mode** - the eyes idle on their own: randomized saccades (quick eye movements) and blinking, timed and sized to feel organic rather than mechanical, entirely self-contained on the Arduino.
2. **Hand-tracking mode** - a webcam-driven computer vision pipeline (OpenCV + MediaPipe Hands) on a connected computer tracks your hand, and the eyes look wherever your hand goes. Clench your fist and the eyelids close; open it and they reopen.

Both modes converge on the same inverse-kinematics gaze controller, so however the target coordinates are produced - a random number generator or a live hand tracker - the eyes can never be driven past their calibrated, mechanically safe range.

## Features

- **Binocular gaze** - both eyes converge on the same 3D point (verging, the way real eyes track a nearby object), computed via per-eye trigonometry plus an empirically-fitted polynomial correcting for servo/linkage geometry.
- **Natural idle motion** - asynchronous randomized timers for blinking and saccades, with occasional short double-blinks and varied stare durations, so the rhythm never feels like a fixed loop.
- **Real-time hand tracking** - MediaPipe Hands locates a 21-point hand skeleton per frame; a stabilized palm centroid (not a single jittery fingertip) drives the gaze target.
- **Gesture-based blinking** - a debounced, hysteresis-filtered fist detector maps a clenched fist directly to closed eyelids, and an open hand to open eyelids.
- **Safety-first motion control** - every gaze command, autonomous or externally driven, is clamped to each eye's calibrated safe range before it ever reaches a servo.
- **Full calibration toolchain** - dedicated sketches for finding each servo's safe min/max/centre position before running the main behavior.
- **Serial protocol decoupling** - the Arduino only ever consumes plain `x,z,fist` text lines, so any language or device capable of opening a serial port can drive the eyes (see [Future Scope](#future-scope)).

## System Architecture

![System architecture diagram](assets/architecture-diagram.svg)

Both modes are built from the same two classes:

- **`Eye`** (`single_eye.h/.cpp`) - one eyeball's three servos plus its calibrated range.
- **`Eyes`** (`double_eye.h/.cpp`) - owns a left and right `Eye`, and provides the shared `lookAt(x, y, z)` gaze controller and blink/eyelid control that both the autonomous and hand-tracking sketches call into.

The only thing that changes between modes is *what decides the gaze target*: a random-number generator on the Arduino itself, or a Python + MediaPipe pipeline on a laptop, streaming coordinates over USB serial.

## Bill of Materials

| Part | Qty | Notes |
|---|---|---|
| Arduino Uno | 1 | Any AVR Uno-compatible board; ESP32/other MCUs would need only the `ServoEasing` pin selection adjusted |
| Micro servos (e.g. SG90/MG90S) | 6 | 3 per eye: left-right, up-down, eyelid |
| 3D-printed eye mechanism | 1 set | STL + 3MF files in [`print_files_double_eye/`](print_files_double_eye/) |
| External 5–6V servo power supply | 1 | See [wiring warning](#wiring) below - do not power 6 servos off the Uno's onboard 5V regulator |
| USB cable (data-capable) | 1 | For programming and, in hand-tracking mode, for the serial link to your computer |
| Webcam | 1 | Only needed for hand-tracking mode |

## Wiring

![Wiring diagram](assets/wiring-diagram.svg)

| Eye | Servo | Arduino Uno Pin |
|---|---|---|
| Left | Left-Right | 8 |
| Left | Up-Down | 9 |
| Left | Eyelid | 10 |
| Right | Left-Right | 11 |
| Right | Up-Down | 12 |
| Right | Eyelid | 13 |

> **"Left"/"Right" are the robot's own**, not the viewer's - match wiring to the `_L`/`_R` labels on the 3D-printed linkage parts, not to your own view facing the eyes.

> ⚠️ **Power warning:** six servos moving at once can draw more current than the Uno's onboard 5V regulator can safely supply. Power the servos from a separate 5–6V supply, with a common ground to the Uno - don't run them off the Uno's 5V pin.

## Repository Structure

```
IRIS/
├── double_eye_motion/        # Main autonomous-motion sketch (open this in Arduino IDE)
│   ├── double_eye_motion.ino
│   ├── double_eye.h / .cpp   # Eyes class - binocular gaze, blink, idle motion
│   └── single_eye.h / .cpp   # Eye class - one eyeball's servos + calibration
│
├── hand_eye_tracking/         # Hand-tracking control mode
│   ├── hand_eye_tracking.ino  # Arduino sketch - same Eyes/Eye classes, serial-driven
│   ├── hand_tracker.py        # Python/OpenCV/MediaPipe hand tracking + serial link
│   ├── requirements.txt
│   └── double_eye.h/.cpp, single_eye.h/.cpp  # same classes, reused
│
├── calibration/                 # Single-servo calibration tool (find min/max/centre)
├── calibration_servo_BIBLE/     # Second copy of the calibration tool
├── center_all/                  # Utility: park all servos at centre / eyelids open
│
├── print_files_double_eye/   # STL + 3MF 3D-printable parts
├── instructions/              # Original build PDF
├── assets/                    # Diagrams used in this README
└── README.md
```

## Getting Started

### 1. Print & assemble

Print the parts in [`print_files_double_eye/`](print_files_double_eye/) and assemble per [`instructions/instructions.pdf`](instructions/instructions.pdf). Mount the six servos per the [wiring table](#wiring) above, but **leave each servo horn mechanically disengaged from its linkage** until after calibration.

### 2. Calibrate every servo

Servos vary unit to unit, and the linkage geometry adds its own offset - you need each servo's actual safe min/max/centre before running anything else.

1. Install the [ServoEasing](https://github.com/ArminJo/ServoEasing) library via the Arduino Library Manager.
2. Open [`calibration/calibration.ino`](calibration/calibration.ino), set `servoPin` to the pin you're testing, and upload it.
3. Open the Serial Monitor at 9600 baud. Type a number 0–180 + Enter to move that servo, and note its comfortable min, max, and "looking straight ahead" centre.
4. Repeat for all six servos, then reconnect each linkage with the servo parked at its centre position.

### 3. Run autonomous mode

1. Open [`double_eye_motion/double_eye_motion.ino`](double_eye_motion/double_eye_motion.ino).
2. Enter your six calibration results in the `set*LowerUpperCentre()` / `setEyeLidOpenClose()` calls in `setup()`.
3. Upload. The eyes should centre, then start idling on their own.

### 4. Run hand-tracking mode

1. Open [`hand_eye_tracking/hand_eye_tracking.ino`](hand_eye_tracking/hand_eye_tracking.ino), enter the same calibration values, and upload it.
2. **Quit the Arduino IDE completely** - it holds the serial port open and will block the next step (see [Troubleshooting](#troubleshooting)).
3. On your computer:
   ```bash
   cd hand_eye_tracking
   pip install -r requirements.txt
   python3 hand_tracker.py
   ```
4. A window opens with your webcam feed and a hand skeleton overlay. Move your hand slowly - the eyes follow. Clench your fist to close the eyelids, release to open them. Press `q` (with the video window focused) to quit.

## Hand & Gesture Control

The Python and Arduino sides speak a minimal, human-readable serial protocol - deliberately simple so it's easy to drive from any other language or device:

```
x,z,fist\n
```

| Field | Meaning |
|---|---|
| `x` | Horizontal gaze target, millimetres, relative to centre |
| `z` | Vertical gaze target, millimetres, relative to centre |
| `fist` | `1` while the tracked hand is a clenched fist, `0` otherwise |

On the Python side (`hand_tracker.py`):

1. **OpenCV** grabs webcam frames.
2. **MediaPipe Hands** returns 21 normalized hand landmarks per frame.
3. The **palm centroid** (an average of the wrist + four finger-base knuckles, far more stable than any single fingertip) maps to `x`/`z`.
4. A **fist detector** counts how many fingertips sit below their own knuckle in the image (a curled finger folds its tip down past the knuckle) and applies hysteresis + debounce so one real clench can't register as multiple blinks.
5. Both values are smoothed (exponential moving average) and streamed to the Arduino at a fixed rate.

On the Arduino side (`hand_eye_tracking.ino`), each incoming line is parsed and fed straight into `Eyes::lookAt()` and `Eyes::setEyelids()` - the same gaze controller the autonomous mode uses, so the same safety clamping applies regardless of the source.

## The Robotics & AI/ML Behind It

This project sits right at the intersection of classical robotics and modern applied machine learning - worth calling out for anyone using it as a learning project:

- **Inverse kinematics** - `Eyes::lookAt()` is a small IK solver: given a target point in 3D space, it works backward to the joint (servo) angles that would achieve it. The trigonometry models each eye as sitting a fixed offset from the head's centreline (the same geometry behind real binocular vergence), and a polynomial correction accounts for the fact that a servo's rotation doesn't translate linearly to eyeball rotation through this particular mechanical linkage.
- **Closed-form vs. learned control** - this project uses a closed-form (directly computed) IK solution, deliberately chosen over a learned one because the geometry is simple and static. Contrast this with the ML half of the pipeline:
- **Computer vision via a trained neural network** - MediaPipe Hands is a pre-trained convolutional model (palm detector + hand landmark regressor) run entirely on-device, no cloud inference. It's a good concrete example of a perception model's output (21 3D keypoints) being fed as input to a classical control system (the IK solver) - a very common real-world robotics pattern: *learned perception, classical control*.
- **Heuristic vs. learned gesture recognition** - the fist detector here is a simple geometric heuristic (finger curl via landmark position), not a trained classifier. It's fast, interpretable, and needs no training data - but it's also brittle to hand orientation. A natural extension (see below) is training a small classifier on the landmark vectors MediaPipe already produces, for a more robust and expressive gesture vocabulary.
- **Filtering as a control primitive** - the exponential moving average smoothing and the debounce/hysteresis state machine are small but important control-systems ideas: raw sensor (or vision) output is almost never fed directly to actuators in a good design - it's filtered first to reject noise the physical system shouldn't react to.

## Troubleshooting

Issues actually hit while building this, in case they save you time:

**`Resource busy` / `SerialException` opening the port**
The Arduino IDE's background serial-monitor helper holds the port open even after closing its window. Quit the Arduino IDE application entirely (not just the window) before running `hand_tracker.py`. To find and clear it manually:
```bash
lsof | grep <your port, e.g. usbmodem11301>
pkill -f serial-monitor
pkill -f "Arduino IDE.app/Contents/MacOS/Arduino IDE"
```

**`programmer is not responding` / `not in sync: resp=0x00` during upload**
Usually unrelated to your code. Close any open Serial Monitor, re-select the correct port and board in the Arduino IDE, and try a different USB cable - a surprising number of USB cables are charge-only.

**`AttributeError: module 'mediapipe' has no attribute 'solutions'`**
Recent MediaPipe releases (0.10.10+, and all 1.0+) removed the legacy `solutions` API this project uses, in favor of a newer Tasks API. `requirements.txt` pins the last confirmed version that still ships it: `mediapipe==0.10.9`. If you see this, you likely have a newer version installed - `pip uninstall mediapipe && pip install -r requirements.txt`.

**MediaPipe crashes with `Check failed: service_ Service is unavailable` (macOS)**
This is a bug in MediaPipe's newer Tasks API: one of its internal calculators unconditionally requires a Metal/GPU service unavailable outside a full macOS app bundle, regardless of the CPU delegate setting. Avoided entirely by using the legacy `solutions` API as this project does (see above).

**Servos brown out / reset when several move at once**
See the [power warning](#wiring) above - use a dedicated servo power supply, not the Uno's onboard 5V rail.

## Future Scope

Ideas for extending IRIS, roughly ordered from straightforward to ambitious:

- **Face tracking** - swap MediaPipe Hands for MediaPipe Face Mesh/Face Detection so the eyes lock onto and follow a person's face automatically, no hand gesture needed.
- **Wireless control** - port to an ESP32 and replace the USB serial link with BLE or Wi-Fi, freeing the whole rig from a tethered laptop.
- **Learned gesture vocabulary** - replace the geometric fist heuristic with a lightweight classifier (even a small MLP) trained on MediaPipe's landmark output, enabling a richer vocabulary (peace sign = wink, open palm = look at viewer, etc.) beyond just open/closed.
- **Emotion-driven expressions** - pair with a facial-emotion-recognition model to drive expressive eye behavior (widened eyes for surprise, narrowed for suspicion) in response to a detected human emotion.
- **Voice control** - add a speech-to-intent pipeline (e.g. a small wake-word + command classifier) so spoken commands ("look left", "blink") drive the same `lookAt()`/`setEyelids()` interface.
- **Multi-person attention** - detect multiple faces/hands and implement an attention policy (track the closest, the loudest, the most recently moved) for more socially aware behavior.
- **Closed-loop precision** - add position feedback (potentiometer or magnetic encoder per servo) instead of open-loop `ServoEasing` control, for consistent absolute positioning independent of servo linearity.
- **ROS integration** - wrap the serial protocol in a ROS node, making IRIS a component in a larger robot (e.g. a full animatronic head or a social robot platform) that can be orchestrated alongside other actuators and sensors.
- **On-device inference** - port the hand-tracking pipeline to run on a Raspberry Pi or Jetson Nano attached directly to the rig, removing the dependency on a separate laptop entirely.

## Contributing

Issues and pull requests are welcome - whether that's a hardware improvement, a new control mode, or just a fix to something in the [Troubleshooting](#troubleshooting) section that didn't quite work for you.

## License

Released under the [MIT License](LICENSE). The mechanical design (3D-printed parts) originated from an open-source Instructables/GitHub animatronic eye project and has been substantially modified and extended here - see [`instructions/instructions.pdf`](instructions/instructions.pdf) for the original build reference.
