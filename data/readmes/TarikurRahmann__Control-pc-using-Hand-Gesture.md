# Control PC Using Hand Gestures (v3)

A professional, software-only solution to control your PC mouse, scrolling, and system features using real-time hand gestures via a webcam. Built with Python, OpenCV, and MediaPipe, version 3 introduces a fully modular architecture with advanced physics-based smoothing, HUD overlay, and system automation.

---

## ✨ Features

### 🎮 Multi-Mode Interaction & Controls
- **MOVE MODE:** Smooth and precise standard cursor tracking.
- **SCROLL MODE:** Intuitive hand-movement vertical scrolling.
- **SYSTEM INTEGRATION:** Control OS-level functions like volume, brightness, and basic shortcuts.
- **PAUSED MODE:** A safety state that halts pointer and system control instantly.

### 🛡️ Safety & Reliability
- **Global Kill Switch ('Q'):** Immediate, safe application shutdown.
- **Auto-Pause:** Instantly triggers safety state on hand loss or low FPS.
- **Smart Cooldowns & Intent Classification:** Prevents accidental double-clicks or erratic movements.

### 🎨 User Interface & Physics
- **Visual Dashboard (HUD):** On-screen real-time feedback showing current Mode, FPS, and detected gestures.
- **Mouse Physics:** Features pointer inertia and acceleration for a natural desktop feel.
- **Jitter Filtering:** Algorithmic smoothing to eliminate raw webcam hand-shake.

---

## 📂 Project Structure

The project utilizes a clean, production-ready modular layout under the `gesture_v3` package:

```text
Control_pc_using_Hand-Gesture-main/
├── gesture_v3/
│   ├── control/
│   │   └── mouse_physics.py      # Handles inertia, acceleration, and physical pointer behavior
│   ├── core/
│   │   └── system.py             # OS-level integrations (volume, brightness, shortcuts)
│   ├── intent/
│   │   └── classifier.py         # Translates hand landmarks into specific actions/gestures
│   ├── perception/
│   │   ├── smoothing.py          # Filters jitter and stabilizes cursor movement
│   │   └── tracker.py            # Wraps MediaPipe Hand Landmarker API
│   ├── ui/
│   │   └── hud.py                # Heads-Up Display / On-screen overlay for user feedback
│   └── config.py                 # Centralized configuration variables for v3
├── config.py                     # Legacy/Global configuration
├── gesture_recognition.py        # Core gesture inference logic
├── hand_landmarker.task          # Pre-trained MediaPipe Landmarker model file
├── hand_tracking.py              # Hand detection utility
├── main_v3.py                    # Main entry point for version 3
├── mouse_control.py              # Direct mouse interaction layer
├── requirements.txt              # Project dependencies
└── README.md                     # Project documentation
```

## Prerequisites
-   Python 3.8+
-   Webcam
-   MediaPipe Model (`hand_landmarker.task`)

## Setup Instructions

1.  **Clone/Download** this repository.
2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Download Model**:
    The system requires the `hand_landmarker.task` model file. [Download Link](https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task) or use:
    ```powershell
    Invoke-WebRequest -Uri https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task -OutFile hand_landmarker.task
    ```

4.  **Run the System**:
    ```bash
    python main.py
    ```

## ✋ Gesture Guide (Detailed Patterns)

### 1. **MOVE CURSOR**
*   **Pattern**: Raise **Index Finger** ONLY. Keep other fingers curled.
*   **Action**: The mouse cursor follows your index fingertip.
*   **Tips**: Keep your hand steady. Move within your camera's field of view.

### 2. **LEFT CLICK**
*   **Pattern**: Pinch your **Thumb** and **Index Finger** together.
*   **Action**: Triggers a Left Click.
*   **Requirement**:
    *   Fingers must touch (distance < 40px).
    *   Hold for **0.25 seconds** (prevents accidental clicks).

### 3. **RIGHT CLICK**
*   **Pattern**: Pinch your **Thumb** and **Middle Finger** together.
*   **Action**: Triggers a Right Click (Context Menu).
*   **Requirement**: Hold for **0.25 seconds**.

### 4. **SCROLL MODE**
*   **Pattern**: Raise **Index** + **Middle Fingers** (Peace Sign / Victory Sign).
*   **Action**: Enters SCROLL MODE.
    *   Move Hand **UP** -> Scroll Page UP.
    *   Move Hand **DOWN** -> Scroll Page DOWN.
*   **Exit**: Lower your middle finger to return to cursor control.

### 5. **PAUSE / SAFETY**
*   **Pattern**: Make a **Closed Fist**.
*   **Action**: Pauses all system control immediately.
*   **Visual**: Screen border turns RED, Text says "PAUSED".

### 6. **QUIT**
*   **Pattern**: Press **'Q'** on your keyboard.
*   **Action**: Safery shutdown of the application.

## Configuration
Tweak `config.py`:
-   `SCROLL_SPEED`: Adjust scroll sensitivity.
-   `GESTURE_COOLDOWN`: Time between clicks.
-   `SMOOTHING_FACTOR`: Cursor stability.

## Version 3 Roadmap (Future)
-   **Voice Control**: "Computer, open browser".
-   **Keyboard Input**: Air-typing interface.
-   **Custom Gestures**: ML Training for user-defined signaling.


---
*Created for Portfolio Demonstration*
