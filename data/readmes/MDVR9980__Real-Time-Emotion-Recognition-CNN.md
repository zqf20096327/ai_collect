# Real-Time Emotion Recognition with Filters 🎭

A Computer Vision project that detects human emotions from facial expressions in real-time using a **Convolutional Neural Network (CNN)**. The application uses **OpenCV** to apply dynamic, emotion-specific image filters (like tints, blur, and sepia) to the live webcam feed based on the detected mood.

## 📌 Features

*   **Deep Learning Model:** A custom VGG-style CNN trained on the FER-2013 dataset (48x48 pixel grayscale images).
*   **Real-Time Inference:** Detects faces and classifies emotions live using OpenCV and Haar Cascades.
*   **Dynamic Visual Filters:** Applies unique visual effects corresponding to the detected emotion:
    *   😠 **Angry:** Red Tint
    *   🤢 **Disgust:** Green Tint
    *   😱 **Fear:** Sepia Tone (Vintage effect)
    *   😀 **Happy:** Gaussian Blur
    *   😢 **Sad:** Grayscale
    *   😲 **Surprise:** Negative (Color Inversion)
    *   😐 **Neutral:** Normal (Green Bounding Box)
*   **Robustness:** Includes Data Augmentation, Dropout, and Batch Normalization to improve generalization.

## 🛠️ Tech Stack

*   **Language:** Python 3.11
*   **Deep Learning:** TensorFlow, Keras
*   **Computer Vision:** OpenCV (cv2)
*   **Data Manipulation:** NumPy, Pandas
*   **Visualization:** Matplotlib, Seaborn

## 📂 Project Structure

```text
├── dataset/                  # Dataset folder (Place FER-2013 'train' & 'validation' here)
├── Emotion_Recognition.ipynb # Main Jupyter Notebook (Data preprocessing, Training, Evaluation)
├── realtime_emotion.py       # Python script to run the webcam demo
├── emotion_model.h5          # Pre-trained model weights (saved)
├── requirements.txt          # List of dependencies
└── README.md                 # Project documentation
```

## 🚀 Installation

Follow these steps to set up the project locally:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/mdvr9980/Real-Time-Emotion-Recognition-CNN.git
    cd Real-Time-Emotion-Recognition-CNN
    ```

2.  **Create a virtual environment (Optional but Recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🎥 Usage

### 1. Run the Real-Time Webcam Demo
You can use the pre-trained `emotion_model.h5` included in this repo to test the application immediately.

```bash
python realtime_emotion.py
```

*   The webcam window will open.
*   The system will detect your face and apply a filter based on your expression.
*   Press **'q'** to close the window.

### 2. Train the Model (Optional)
If you wish to retrain the model or improve it:
1.  Download the **FER-2013** dataset (or any standard emotion dataset).
2.  Organize it into `dataset/train` and `dataset/validation` folders.
3.  Open the Jupyter Notebook:
    ```bash
    jupyter lab Emotion_Recognition.ipynb
    ```
4.  Run all cells to train and save a new `emotion_model.h5`.

## 🧠 Model Architecture

The CNN architecture consists of 4 convolutional blocks designed to capture facial features at different scales:

1.  **Conv2D (32 filters)** -> BatchNorm -> ReLU -> MaxPool -> Dropout
2.  **Conv2D (64 filters)** -> BatchNorm -> ReLU -> MaxPool -> Dropout
3.  **Conv2D (128 filters)** -> BatchNorm -> ReLU -> MaxPool -> Dropout
4.  **Conv2D (256 filters)** -> BatchNorm -> ReLU -> MaxPool -> Dropout
5.  **Flatten** -> Dense (512) -> Dense (7 classes, Softmax)

## 📊 Results

*   **Training Accuracy:** ~61%
*   **Validation Accuracy:** ~64%
*   **Loss Function:** Categorical Crossentropy
*   **Optimizer:** Adam (with Learning Rate Reduction on Plateau)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/mdvr9980/Real-Time-Emotion-Recognition-CNN/issues).