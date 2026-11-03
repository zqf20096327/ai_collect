# Food Recognition and Calorie Estimation

A deep learning project that identifies food items from images and estimates their calorie content using a CNN-based image classification model. Built with Python, TensorFlow, MobileNetV2, and Streamlit.

## Project Overview

Food recognition is an application of computer vision that enables computers to identify food items from digital images.

This project uses transfer learning with MobileNetV2 to classify food images into 101 categories from the Food-101 dataset. After identifying a food category, the application retrieves an approximate calorie reference from a local nutrition database and calculates estimated calories based on a user-selected serving weight.

The project provides an interactive web application for image-based food recognition and calorie estimation.

## Features

- Recognizes 101 food categories.
- Uses MobileNetV2 transfer learning.
- Uses the official Food-101 training and testing metadata.
- Performs image preprocessing and data augmentation.
- Displays the predicted food category and confidence score.
- Shows the top five predicted food categories.
- Estimates calories using a nutrition reference database.
- Allows users to adjust serving size in grams.
- Generates training history and confusion matrix visualizations.
- Provides a command-line image prediction tool.
- Includes an interactive Streamlit interface.

## Application Screenshots

### 1. Food Recognition

The application provides an image upload interface for food classification.

![Food recognition interface](assets/images/01-food-recognition.png)

### 2. Food Classification Results

The application displays the predicted food category and its recognition confidence.

![Food classification results](assets/images/02-food-recognition-results.png)

### 3. Calorie Estimation

Users can select a serving weight and view the estimated calorie content.

![Calorie estimation interface](assets/images/03-calorie-estimation.png)

### 4. Food Prediction Example

An example of food classification with multiple prediction scores.

![Food prediction example](assets/images/04-food-prediction-example.png)

### 5. Model Evaluation and Training Visualizations

The application presents test performance, training history, and the confusion matrix.

![Model evaluation and training visualizations](assets/images/05-model-evaluation.png)

### 6. FoodLens Application Dashboard

The complete FoodLens interface combines food recognition, calorie estimation, and model evaluation.

![FoodLens application dashboard](assets/images/06-foodlens-dashboard.png)

## Application Workflow

1. Upload a food image.
2. The trained MobileNetV2 model analyzes the image.
3. The model predicts the food category.
4. The application retrieves its approximate calorie value per 100 grams.
5. The user enters an estimated serving size.
6. The application calculates the estimated calorie content.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| TensorFlow / Keras | Deep learning and model training |
| MobileNetV2 | Pretrained image classification architecture |
| NumPy | Numerical operations |
| Pandas | Data handling |
| Pillow | Image processing |
| Scikit-learn | Model evaluation |
| Matplotlib | Training and evaluation visualization |
| Streamlit | Interactive web application |

## Dataset

This project uses the **Food-101 dataset**.

- Dataset: [Food-101 on Kaggle](https://www.kaggle.com/datasets/dansbecker/food-101)
- Original dataset: [Food-101 project page](https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/)
- Number of categories: 101
- Total images: 101,000
- Training images: 75,750
- Testing images: 25,250

Each category contains 750 training images and 250 testing images.

The project uses the supplied `classes.txt`, `train.txt`, and `test.txt` metadata files.

Download and extract the dataset before training. Keep it inside the local `data/` directory. The complete dataset is excluded from GitHub because of its size and distribution terms.

## Project Structure

```text
Food-Recognition-and-Calorie-Estimation/
│
├── data/
│   └── food-101/
│       └── food-101/
│           ├── images/
│           └── meta/
│               ├── classes.txt
│               ├── train.txt
│               ├── test.txt
│               ├── train.json
│               ├── test.json
│               └── labels.txt
│
├── artifacts/
│   ├── food101_model.keras
│   ├── best_food101_model.keras
│   ├── class_names.json
│   ├── metrics.json
│   ├── confusion_matrix.png
│   └── training_history.png
│
├── assets/
│   └── images/
│       ├── 01-food-recognition.png
│       ├── 02-food-recognition-results.png
│       ├── 03-calorie-estimation.png
│       ├── 04-food-prediction-example.png
│       ├── 05-model-evaluation.png
│       └── 06-foodlens-dashboard.png
│
├── app.py
├── train_model.py
├── dataset_utils.py
├── predict_image.py
├── calorie_utils.py
├── nutrition_data.csv
├── requirements.txt
├── .gitignore
├── README.md
└── PROJECT_REPORT.md
```

The `artifacts/` files are generated automatically after model training.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/saratbanik/Food-Recognition-and-Calorie-Estimation.git

cd Food-Recognition-and-Calorie-Estimation
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment in Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip

python -m pip install -r requirements.txt
```

Python 3.10–3.13 is supported by the specified TensorFlow version. On native Windows, this setup uses CPU execution.

### 4. Prepare the dataset

Download Food-101 from Kaggle, extract it, and place the dataset under `data/`.

The dataset utility automatically searches for the folder containing `images/` and `meta/`, including the nested folder structure produced by some extractions.

## Model Training

### Quick test

Before training the full dataset, verify your environment and dataset using:

```bash
python train_model.py --quick
```

Quick mode uses a smaller image subset. Its results are only for checking that the pipeline works.

### Full training

Run:

```bash
python train_model.py --epochs 5 --fine-tune-epochs 1 --batch-size 16
```

The training script:

- Loads the Food-101 training and testing lists.
- Creates a stratified validation split from the training list.
- Builds a MobileNetV2 transfer-learning model.
- Trains the classification head.
- Fine-tunes the upper MobileNetV2 layers.
- Evaluates the model on the official testing list.
- Saves the trained model and evaluation files in `artifacts/`.

The first training run requires an internet connection to obtain pretrained ImageNet weights.

Training time depends on hardware and batch size. Full training on a CPU may take a substantial amount of time.

## Predict a Food Image

Use:

```bash
python predict_image.py --image "C:\path\to\your\food_image.jpg"
```

The script displays the top predicted food categories and their confidence scores.

## Run the Web Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal, normally:

`http://localhost:8501`

Upload a food image, view the prediction, adjust the estimated serving weight, and see the calculated calorie value.

The trained model and supporting artifacts must exist before starting the application.

## Calorie Estimation Method

The calorie calculation uses a local nutrition reference table.

Formula:

```text
Estimated Calories =
(Calories per 100 grams × Serving Weight in grams) / 100
```

For example, if a food has a reference value of 266 kcal per 100 g and the selected serving size is 150 g:

```text
(266 × 150) / 100 = 399 kcal
```

The values in `nutrition_data.csv` are initial generic estimates. They should be verified and updated using reliable nutritional references, such as [USDA FoodData Central](https://fdc.nal.usda.gov/), before being used for nutritional guidance.

**Important limitation:** The application does not measure food weight, volume, ingredients, or portion size from the uploaded image. The calorie output is based on the predicted food category and the serving weight entered by the user. It is an approximate educational estimate, not a dietary or medical measurement.

## Model Evaluation

The training script generates:

| File | Description |
|---|---|
| `food101_model.keras` | Saved trained model |
| `best_food101_model.keras` | Best validation checkpoint |
| `class_names.json` | Food class labels |
| `metrics.json` | Evaluation results |
| `confusion_matrix.png` | Classification confusion matrix |
| `training_history.png` | Training and validation curves |

Actual performance results should be taken from the generated evaluation files. Do not report quick-mode metrics as final model performance.

## Limitations

- Classification performance depends on image quality and training data.
- Similar-looking food categories may be confused by the model.
- Food-101 training images contain some label and image noise.
- Calorie references vary by ingredients, recipes, preparation methods, and serving sizes.
- The application does not automatically estimate food weight or volume.
- Calorie output is an approximation and should not be used as medical or dietary advice.

## Future Improvements

- Add automatic food detection and segmentation.
- Estimate food portion size using depth information.
- Integrate a verified nutrition database or API.
- Support multiple food items in one image.
- Add meal history and daily calorie tracking.
- Improve classification performance through further fine-tuning.
- Develop a mobile-friendly application.

## Potential Applications

- Food image classification
- Educational nutrition applications
- Food logging and meal tracking
- Experimental dietary monitoring
- Computer vision research

---

<div align="center">

**Developed by [SARAT BANIK](https://www.linkedin.com/in/saratbanik)**

</div>