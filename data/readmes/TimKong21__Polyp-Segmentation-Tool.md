# Polyp Segmentation Tool

[![Live app](https://img.shields.io/badge/Live%20app-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://polyp-segmentation-tool.streamlit.app/)

## Overview

Polyp Segmentation Tool is an interactive Streamlit application that produces segmentation masks for colonoscopy images. A U-Net model trained with the [Kvasir-SEG dataset](https://datasets.simula.no/kvasir-seg/) processes JPG/JPEG uploads, displays masks alongside the original images, and supports batch result downloads.

> This is a portfolio and research project, not a clinical device. It is not intended for diagnosis, treatment decisions, or patient care; outputs must be independently validated and used only with appropriate privacy, security, and clinical governance.

<p align="center">
  <img src="./assets/kvasir-seg-samples.png" alt="Kvasir-SEG colonoscopy images, segmentation masks, and annotated examples" width="80%"/>
</p>

## Streamlit App Usage

1. **Access the tool:** Open the [live Streamlit app](https://polyp-segmentation-tool.streamlit.app/).

2. **Download Sample Images**: Download sample images provided within the app. Look for the [link](https://github.com/TimKong21/Polyp-Segmentation/tree/main/new_data/test/images/test) to download sample images on the app's homepage.

3. **Upload Images**: Use the file uploader to select colonoscopy images (JPG/JPEG) for segmentation.

4. **Process Images**: Click 'Process Images' to start the segmentation process.

5. **View and Download Results**: Segmentation masks are displayed alongside the original images. A ZIP file containing all masks can be downloaded.

<p align="center">
  <img src="./streamlit/app_demo.gif" alt="App Demo" width="80%">
</p>

## Technical Highlights

- **Deep Learning Model Optimization**: Uses a U-Net architecture for pixel-wise medical image segmentation.

- **Data Preprocessing and Augmentation**: Includes a preprocessing and augmentation pipeline for image resizing and normalization.

- **Streamlit Web Application**: Developed a Streamlit web application that prioritizes ease of use. The application supports batch processing and provides downloadable results for offline analysis. The deep learning model used for segmentation is securely stored on AWS S3 and is dynamically loaded by the application as needed.

- **Exploratory Data Analysis (EDA)**: Conducted detailed EDA to gain insights into polyp characteristics, which informed the preprocessing and augmentation strategies to enhance detection accuracy.

## Installation
1. **Clone the Repository**

   First, clone the repository to local machine using Git.

   ```bash
   git clone https://github.com/TimKong21/Polyp-Segmentation-Tool.git
   cd Polyp-Segmentation-Tool
   ```

2. **Set Up a Virtual Environment**

   Create a virtual environment to manage the dependencies.

   ```bash
   # Create a virtual environment
   python -m venv venv
   ```

    Activate the virtual environment.
    ```bash
    # On Windows
    .\venv\Scripts\activate

    # On macOS and Linux
    source venv/bin/activate
    ```

3. **Install Dependencies**

   Install the required Python packages using `pip`.
   
   ```bash
   pip install -r requirements.txt
   ```

4. **Model Training**

   Prior to running the Streamlit app, the model must be trained unless a trained model file (`model/unet.h5`) is already available or can be downloaded [here](https://drive.google.com/drive/folders/1k_obp9QyBd5rWgQhf5NJskt6lM8kvrUN?usp=drive_link). Model training can be conducted by executing the `Image preprocessing Data generator and Modeling.ipynb` notebook. This process can occur locally if the environment is suitably equipped or on Google Colab for GPU access.

    - **Local Training**: Ensure the machine possesses necessary computational resources. **Dataset organization according to the data generator's requirements is crucial**, with distinct folders for images and masks. For example:

        ```markdown
        new_data/
        │
        ├── train/
        │   ├── images/
        │   │   ├── 0001.jpg
        │   │   ├── 0002.jpg
        │   │   └── ...
        │   │
        │   └── masks/
        │       ├── 0001.png
        │       ├── 0002.png
        │       └── ...
        │
        ├── validation/
        │   ├── images/
        │   │   ├── 0008.jpg
        │   │   ├── 0009.jpg
        │   │   └── ...
        │   │
        │   └── masks/
        │       ├── 0008.png
        │       ├── 0009.png
        │       └── ...
        │
        └── test/
            ├── images/
            │   ├── 0011.jpg
            │   ├── 0024.jpg
            │   └── ...
            │
            └── masks/
                ├── 0011.png
                ├── 0024.png
                └── ...
        ```

   - **Training on Google Colab**: Upload the notebook to Colab, adjusting paths for data loading and model saving accordingly. Colab's GPU access can significantly expedite the training process.

   **Note**: Training your own model allows for customization and adaptation to specific datasets. Consider setting up your own AWS S3 bucket or similar cloud storage solution for model storage and access if you plan to deploy or share your application.

5. **Run the Streamlit App**

   Initiate the application locally with Streamlit.

   ```bash
   streamlit run app.py
   ```

    This command activates the Streamlit server, generating a URL in the terminal for web browser access to the application.


## License

The source code in this repository is available under the [MIT License](LICENSE). The [Kvasir-SEG dataset](https://datasets.simula.no/kvasir-seg/) remains subject to its own license and terms of use.
