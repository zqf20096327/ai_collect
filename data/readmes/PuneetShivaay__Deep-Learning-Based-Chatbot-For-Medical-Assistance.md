# 🧠 Deep Learning Based Chatbot For Medical Assistance 

<p align="center">
  A Python-based deep learning chatbot that analyzes user-provided symptoms and predicts possible diseases using a trained neural network model.
</p>

<p align="center">
  <a href="https://github.com/PuneetShivaay/Deep-Learning-Based-Chatbot-For-Medical-Assistance/stargazers">
    <img src="https://img.shields.io/github/stars/PuneetShivaay/Deep-Learning-Based-Chatbot-For-Medical-Assistance?style=for-the-badge" alt="GitHub Stars" />
  </a>
  <a href="https://github.com/PuneetShivaay/Deep-Learning-Based-Chatbot-For-Medical-Assistance/network/members">
    <img src="https://img.shields.io/github/forks/PuneetShivaay/Deep-Learning-Based-Chatbot-For-Medical-Assistance?style=for-the-badge" alt="GitHub Forks" />
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-Deep%20Learning-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Neural%20Network-Machine%20Learning-FF6F00?style=for-the-badge" alt="Neural Network" />
</p>

---

## 🚀 About the Project

**Medical Assistance Chatbot** is a Python-based deep learning project that uses a trained neural network to process user-provided symptoms and identify possible disease categories based on the available training data.

The project demonstrates how machine learning can be combined with a conversational interface to create an experimental medical-assistance chatbot.

The system takes symptoms as input, processes them through the trained model, and returns the model's predicted disease category.

> **Note:** This project is intended for educational and experimental purposes only. It is not clinically validated and should not be used as a substitute for professional medical advice, diagnosis, or treatment.

---

## ✨ Features

* 🧠 Deep learning-based chatbot
* 💬 Interactive chatbot GUI
* 🩺 Symptom-based disease prediction
* 📊 Neural network model training
* 📁 JSON-based training data
* 💾 Pre-trained model included
* 🐍 Python-based implementation
* 🔧 Separate training and chatbot execution scripts

---

## ⚙️ How It Works

The application follows a simple machine learning workflow:

```text
User Symptoms
      │
      ▼
Symptom Processing
      │
      ▼
Neural Network Model
      │
      ▼
Disease Prediction
      │
      ▼
Chatbot Response
```

The training process uses the symptom and intent data stored in the JSON dataset. The trained model is then used by the chatbot application to process user input and generate a prediction.

---

## 🧠 Machine Learning Workflow

```text
Training Dataset
      │
      ▼
Data Preprocessing
      │
      ▼
Feature / Symptom Representation
      │
      ▼
Neural Network Training
      │
      ▼
Trained Model
      │
      ▼
Chatbot Application
```

The repository includes the trained model and supporting serialized files so the chatbot can be executed without necessarily retraining the model first.

---

## 🛠️ Tech Stack

| Technology     | Purpose                                         |
| -------------- | ----------------------------------------------- |
| Python         | Application and machine learning implementation |
| Deep Learning  | Disease prediction model                        |
| Neural Network | Pattern recognition and prediction              |
| JSON           | Training / intent data                          |
| Tkinter / GUI  | Chatbot interaction interface                   |
| Pickle         | Serialized model-related data                   |
| H5             | Saved trained neural network model              |

---

## 📂 Project Structure

```text
Deep-Learning-Based-Chatbot-For-Medical-Assistance/
│
├── chatbot_gui.py       # Chatbot GUI application
├── chatbot_train.py     # Model training script
├── chatbot_model.h5     # Trained neural network model
├── intents2.json        # Training / intent dataset
├── labels.pkl           # Serialized labels
├── words.pkl            # Serialized vocabulary
├── requirements.txt     # Python dependencies
├── pyvenv.cfg           # Python environment configuration
└── README.md            # Project documentation
```

---

## ⚙️ Requirements

The original project was built using **Python 3.7**.

Make sure Python and pip are installed on your system.

Check your Python installation:

```bash
python --version
```

Check pip:

```bash
pip --version
```

---

## 📥 Installation

### 1. Clone the repository

```bash
git clone https://github.com/PuneetShivaay/Deep-Learning-Based-Chatbot-For-Medical-Assistance.git
```

### 2. Navigate to the project directory

```bash
cd Deep-Learning-Based-Chatbot-For-Medical-Assistance
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🏋️ Train the Model

To train the neural network using the available dataset, run:

```bash
python chatbot_train.py
```

The training script uses the project dataset and generates the trained model and supporting files used by the chatbot.

---

## 💬 Run the Chatbot

After the required dependencies are installed and the model is available, start the chatbot GUI:

```bash
python chatbot_gui.py
```

The application will launch the chatbot interface where you can enter symptoms and interact with the model.

---

## 🔍 Example Workflow

```text
User:
"I have a headache and fever"

        ↓

Chatbot processes symptoms

        ↓

Trained neural network

        ↓

Model predicts a possible disease category

        ↓

Chatbot displays the prediction
```

The prediction is based entirely on the patterns learned from the available training dataset.

---

## 📊 Project Components

### `chatbot_train.py`

Responsible for preparing the training data and training the neural network model.

### `chatbot_gui.py`

Provides the interactive chatbot interface and allows users to communicate with the trained model.

### `intents2.json`

Contains the training data and intent information used by the chatbot.

### `chatbot_model.h5`

Contains the trained neural network model.

### `words.pkl`

Stores the serialized vocabulary used by the model.

### `labels.pkl`

Stores the serialized labels used during prediction.

---

## 🎯 Learning Objectives

This project demonstrates practical concepts including:

* Python programming
* Machine learning fundamentals
* Deep learning
* Neural networks
* Natural language processing concepts
* Dataset preparation
* Model training
* Model persistence
* Chatbot development
* GUI-based application development

---

## ⚠️ Medical Disclaimer

This project is created for **educational and experimental purposes only**.

The predictions generated by this application:

* Are not medical diagnoses
* Are not clinically validated
* Should not be used for medical decision-making
* Should not replace consultation with a qualified healthcare professional

If you have health concerns or symptoms, consult an appropriate medical professional.

---

## 📈 Open Source Community

This project has received support from the developer community.

⭐ **17 Stars**

🍴 **14 Forks**

Thank you to everyone who has starred and forked this repository!

---

## 🔮 Possible Future Improvements

Some possible improvements include:

* 🤖 Integrate a modern NLP model
* 🧠 Improve symptom classification
* 💬 Add conversational context
* 📊 Add model evaluation metrics
* 🧪 Add automated testing
* 🌐 Build a web-based interface
* 📱 Add a mobile interface
* 🔍 Improve symptom extraction
* 📚 Expand and improve the training dataset
* 🩺 Add stronger safety and medical-information boundaries

---

## 🤝 Contributing

Contributions, improvements, and suggestions are welcome.

To contribute:

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/your-feature-name
```

3. Make your changes
4. Commit your changes

```bash
git commit -m "Add your feature"
```

5. Push your branch

```bash
git push origin feature/your-feature-name
```

6. Open a Pull Request

---

## ⭐ Support

If you find this project useful or educational, please consider giving it a star.

Your support helps other developers discover the project and encourages continued development.

---

## 👨‍💻 Author

**Puneet Kumar**

Software Engineer focused on building modern web applications, AI systems, and practical software engineering projects.

🌐 Portfolio: https://puneetshivaay.vercel.app/

💻 GitHub: https://github.com/PuneetShivaay

---

<p align="center">
  Made with ❤️ using Python
</p>
