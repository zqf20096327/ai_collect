# Vehicle Detection and Counting

> Real-time vehicle detection and traffic flow analysis using OpenCV and Python.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-orange)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🚀 Features

* Real-time vehicle detection from video footage
* Motion-based object extraction using frame differencing
* Contour detection and filtering for vehicle identification
* Centroid-based vehicle tracking
* Automatic vehicle counting using virtual line crossing
* Bounding box visualization for detected vehicles
* Live vehicle count overlay on video frames
* Lightweight implementation using OpenCV and NumPy
* Easy to customize for traffic monitoring applications

---

## 🛠️ Tech Stack

| Category                | Technology          |
| ----------------------- | ------------------- |
| Language                | Python              |
| Computer Vision         | OpenCV (`cv2`)      |
| Numerical Computing     | NumPy               |
| Development Environment | Jupyter Notebook    |
| Input Source            | Video File (`.mp4`) |

---

## 📂 Project Structure

```text
Vehicle-Detection-and-Counting/
│
├── README.md
│   └── Project documentation
│
├── Vehicle Detection and Counting.ipynb
│   └── Main notebook containing vehicle detection and counting logic
│
└── Video.mp4
    └── Sample input video used for vehicle detection
```

### Main Components

| File                                   | Purpose                                                    |
| -------------------------------------- | ---------------------------------------------------------- |
| `Vehicle Detection and Counting.ipynb` | Implements vehicle detection, tracking, and counting logic |
| `Video.mp4`                            | Sample traffic footage used as input                       |
| `README.md`                            | Project documentation                                      |

---

## ⚙️ How It Works

The application follows a classical computer vision pipeline:

1. Load traffic video frames using OpenCV.
2. Compute frame differences between consecutive frames.
3. Convert frames to grayscale.
4. Apply Gaussian blur to reduce noise.
5. Perform thresholding and dilation.
6. Detect moving object contours.
7. Filter contours based on minimum width and height.
8. Calculate object centroids.
9. Track centroids crossing a predefined counting line.
10. Increment vehicle count and display results in real time.

---

## ⚡ Getting Started

### Prerequisites

Ensure the following software is installed:

* Python 3.9+
* Jupyter Notebook or JupyterLab
* pip

Verify installation:

```bash
python --version
pip --version
jupyter --version
```

---

### Installation

Clone the repository:

```bash
git clone https://github.com/your-username/Vehicle-Detection-and-Counting.git
```

Navigate to the project directory:

```bash
cd Vehicle-Detection-and-Counting
```

Install required dependencies:

```bash
pip install opencv-python numpy jupyter
```

---

### Environment Variables

This project does not currently require any environment variables.

If customization is added later, a `.env` file may look like:

```env
VIDEO_PATH=Video.mp4
MIN_CONTOUR_WIDTH=40
MIN_CONTOUR_HEIGHT=40
COUNTING_LINE_Y=550
OFFSET=10
```

---

### Running the Application

#### Launch Jupyter Notebook

```bash
jupyter notebook
```

Open:

```text
Vehicle Detection and Counting.ipynb
```

and run all cells.

---

### Alternative: Export and Run as Python Script

Convert notebook to a Python file:

```bash
jupyter nbconvert --to script "Vehicle Detection and Counting.ipynb"
```

Run:

```bash
python "Vehicle Detection and Counting.py"
```

---

## 📊 Detection Parameters

The notebook currently uses the following configuration:

```python
min_contour_width = 40
min_contour_height = 40
offset = 10
line_height = 550
```

### Parameter Description

| Parameter            | Description                    |
| -------------------- | ------------------------------ |
| `min_contour_width`  | Minimum detected object width  |
| `min_contour_height` | Minimum detected object height |
| `offset`             | Tolerance around counting line |
| `line_height`        | Y-coordinate of counting line  |

---

## 🧪 Running Tests

No automated tests are currently included in the repository.

Future testing recommendations:

```bash
pytest
```

Code quality checks:

```bash
flake8
```

Formatting:

```bash
black .
```

---

## 📈 Potential Use Cases

* Traffic monitoring systems
* Smart city infrastructure
* Road usage analytics
* Parking management
* Transportation research
* Environmental impact monitoring
* Traffic congestion analysis

---

## 🔮 Future Improvements

* YOLO-based vehicle detection
* Multi-class vehicle classification
* Vehicle speed estimation
* Real-time webcam support
* DeepSORT tracking integration
* Dashboard and analytics reporting
* GPU acceleration
* Vehicle type statistics

---

## 🤝 Contributing

Contributions are welcome.

### Workflow

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to your branch

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

Please ensure code is well documented and tested before submission.

---

## 📄 License

This repository does not currently include a license file.

Unless otherwise specified by the repository owner, consider adding an MIT License:

```text
MIT License
Copyright (c) 2026
```

---

## 🙏 Acknowledgements

* OpenCV Community
* NumPy Contributors
* Python Software Foundation

---

### Built with Python, OpenCV, and Computer Vision
