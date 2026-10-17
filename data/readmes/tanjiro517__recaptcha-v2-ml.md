

# reCAPTCHA v2 Solver using YOLO (For Testing & Learning Only)

This version is for **testing and educational demonstration only**.
For the **advanced version**, contact us on Telegram:
[https://t.me/ReX_update](https://t.me/ReX_update)


This project demonstrates how a YOLO (You Only Look Once) model can be used to analyze and predict objects in reCAPTCHA v2 image challenges.
It is **strictly for research, learning, and testing purposes only** **not for bypassing security systems** or real-world CAPTCHA protections.

---

## Prerequisites

Before you start, ensure you have the following installed on your system:

* **Python 3.10+**
* **pip**
* **Google Chrome** (latest version)
* **ChromeDriver** (matching your Chrome version)
* **Jupyter Notebook** (for training or testing the YOLO model)

---

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/tanjiro517/recaptcha-v2-ml.git
   cd recaptcha-v2-ml
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional)** Verify your ChromeDriver version:

   ```bash
   chromedriver --version
   ```

   If not installed, download it from: [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)

---

## Project Structure

```
recaptcha-v2-ml/
│
├── solver.py                   # Automates solving demo reCAPTCHA using YOLO model
├── YOLO_train.ipynb            # Notebook for training YOLO on labeled image data
├── YOLO_results.ipynb          # Visualizes YOLO predictions
├── yolov11_classification.ipynb # Extra notebook for image classification
├── best_yolo11cls.pt           # Pre-trained YOLO model (used by solver.py)
├── requirements.txt            # All Python dependencies
└── README.md                   # Project documentation
```

---

## Training the YOLO Model (Optional)

If you want to train your own model:

1. Launch Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

2. Open **`YOLO_train.ipynb`**

3. Run all cells this will:

   * Load labeled CAPTCHA images
   * Train a YOLO model for object detection
   * Save the best model as:

     ```
     best_yolo11cls.pt
     ```

---

## Running the Solver (Demo Only)

To test how the model detects image objects:

1. Ensure `best_yolo11cls.pt` is in the project folder.
2. Run:

   ```bash
   python solver.py
   ```
3. The script will:

   * Launch Chrome via Selenium
   * Visit a **reCAPTCHA demo page**
   * Detect images using YOLO
   * Show how predictions are made

> **Important:**
> This code is for **learning and demonstration** purposes only.

---

## Notes

* `solver.py` uses **Selenium + YOLO** to analyze images.
* To watch the browser in action, set `HEADLESS = False` inside `solver.py`.
* For performance, a GPU-enabled PyTorch installation is recommended.

---

## Example Use-Cases (Educational Only)

* Learning how YOLO detects small image patterns
* Understanding object detection and bounding boxes
* Experimenting with image classification datasets
* Research on CAPTCHA usability and accessibility

---

## Important Note

This version is for **testing and educational demonstration only**.
For the **advanced version**, contact us on Telegram:
[https://t.me/ReX_update](https://t.me/ReX_update)

---


