<!-- This document was edited on October 25, 2025, fixing various unscientific expressions and translations from the original document and completely remaking the English and Vietnamese versions. -->
<p align="center">
  <br>
  <img src="./image/LOGO.png" style="width:28%;">
</p>
<br>

<h2>
  Power Load Classification and Prediction System Based on Deep Learning Algorithms <br><br>
  基于深度学习算法的电力负载分类与预测系统
</h2>

#### Documentation Languages

[**English**](./README.md) | [**Simplified Chinese**](./README.zh-CN.md) | [**Tiếng Việt**](./README.vi.md)

> This document was translated by OpenAI's GPT-5 model and is for reference only. Please refer to the Simplified Chinese version as the authoritative source.

### Project Overview

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Empowering energy conservation and emission reduction through the digital economy, and enhancing efficiency with high-tech innovation, has become a major trend across industries and households. However, the irrational use of electric resources in China remains severe and urgently needs to be addressed. According to the China Energy Conservation Product Certification Center, the standby power consumption of household appliances in an average urban family leads to considerable energy loss every day. The standby power consumption of 400 million televisions across the nation amounts to 2.92 billion kilowatt-hours per year — equivalent to one-third of the annual electricity generation of the Daya Bay Nuclear Power Plant. Therefore, the necessity of discovering and controlling electricity waste through power monitoring is increasingly evident. Among these technologies, non-intrusive monitoring is particularly vital. Our team has developed a **Power Load Classification and Prediction System based on Non-Intrusive Technology**, which utilizes artificial intelligence to help households and small businesses reduce electricity expenses and promote energy conservation.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Based on the above background, we designed a **power load classification and prediction system** tailored for household users and small-scale enterprises. The **classification** function informs users in real time about the operational status of each electrical appliance, while the **prediction** function forecasts short-term energy consumption. Whether for homes or factories, such an intelligent system is indispensable for monitoring appliance operation and identifying unnecessary power usage. This not only helps save energy but also reduces electricity costs. Moreover, short-term power consumption forecasting allows enterprises to plan power usage more efficiently — especially under tiered electricity pricing schemes.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;After logging into the system, household users can view the real-time power consumption waveform, the total electricity consumed in the past 50 minutes, and the appliances currently running as determined by the model (e.g., “water heater,” “computer,” or combinations of multiple devices). Users can also view the AI model’s 20-minute future consumption prediction (the forecasted power curve).

### Competitor Analysis

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;As power systems grow in scale, existing intrusive load monitoring products can no longer meet demand and are being phased out. Current products on the market mainly employ traditional non-intrusive algorithms based on **Decision Trees**, **Random Forests**, and **Support Vector Machines (SVM)**, or ensemble learning combinations thereof. Common load forecasting algorithms include **Regression Analysis**, **ARIMA**, and deep learning-based **LSTM** models. However, their prediction accuracy remains unsatisfactory and lacks specificity for power load scenarios — these methods merely address generic time-series classification or forecasting tasks without considering the unique properties of power data.  

The following figure compares the predicted power curves obtained under identical training and testing datasets using the ARIMA algorithm, the LSTM algorithm, and our proposed system:

<img src="./image/compare.png" style="width: 80%;" />

### System Design Concept

- **AI Model:** A cascaded model structure divides the task into two sequential modules: classification/decomposition and prediction. The classification module uses a deep fully connected neural network to process time-windowed features and achieve appliance recognition. The decomposition task is accomplished through classification. The prediction model, inspired by generative language models, is built around the `Transformer` structure — two deep neural networks connected via appliance-type labels.

- **System Architecture:** The architecture follows a **cloud-collaborative pattern of distributed applications and centralized computing**, suitable for modern supercomputing platforms. It consists of edge devices (power meters), distributed backend and database systems, AI models deployed at the supercomputing center for classification and prediction, and a WeChat Mini Program as the client interface. This design helps alleviate latency issues caused by high concurrency in large-scale user requests.

- **Frontend and Backend Design:** The frontend is developed using the WeChat Developer Tools, and waveform visualization is implemented via the **ECharts** line chart component. The frontend periodically polls the backend for updates. For performance, the backend service is built in **C++17** with a **single-Reactor multithreaded architecture**. The server core includes modules for logging, thread pool management, I/O multiplexing, HTTP handling, buffer management, and blocking queues. HTTP requests are read using scatter-read techniques and parsed efficiently via finite-state machines and regular expressions.

| Model Workflow | System Macro Architecture |
| ------ | ------ |
| <img src="./image/model.png" style="width: 65%;"/> | <img src="./image/system_arch.png" style="width: 65%;"/> |

### Model Details

- **Classification and Decomposition Model:**  
  *Feature Engineering:* The input data is first windowed and grouped based on power values. The number of samples in each group within a window is counted to form a frequency distribution. Each frequency vector is normalized by window length to generate feature vectors, which are then compressed using **PCA**.  
  *Model Design:* A **Fully Connected Neural Network (FNN)** takes the feature vector for each window as input and outputs the one-hot encoded appliance category. A 3-layer FNN (28, 14, 7) is used for single-appliance classification, and another 3-layer FNN (84, 42, 21) handles power-label decomposition (21 appliance combinations).  
  We compared FNN with **GRU** models and found their maximum accuracies to be 91% and 90%, respectively. However, GRU’s inference requires higher power consumption because it considers inter-window dependencies. Assuming that each time window is independent allows the FNN to focus solely on its contained features, passing label data to the prediction model’s embedding layer for further processing. The prediction model then captures temporal dependencies — each performing its role.  
  For these reasons, we selected the fully connected architecture. The classification model structure is illustrated below:

<img src="./image/分类模型图示.svg" style="width: 70%;" />

<br><br>

- **Power Load Prediction Model:**  
  For time-series forecasting of electric power, the model processes the data as follows: first, frame segmentation is performed, and then each frame is windowed. Each time window produces a feature vector, and multiple feature vectors form a feature matrix. These vectors consist of **transient features** (high-frequency variations) and **steady-state features** (low-frequency stability).  
  Transient features are derived from **FFT** amplitudes and phases, excluding the DC component since its mean information is already contained in steady-state features.  
  Steady-state features include maximum, minimum, mean, RMS, and crest factor values — guided by electrical theory. Appliance category embeddings are incorporated into the steady-state vector through an **Embedding layer**.  
  Inspired by generative language models, the feature matrix is treated as a “sentence embedding matrix.” It passes through **5–6 Transformer Blocks** (we selected 6) followed by attention-based averaging to produce the **prediction vector** (analogous to token embeddings in language models). Finally, the transient part of the prediction vector (in frequency domain) undergoes **inverse FFT** to generate the time-series prediction of power consumption.  

The power prediction model structure is illustrated below:

<img src="./image/功率数值预测模型图示.svg" style="width: 70%;" />

### Model Performance on Experimental Dataset

The dataset was collected from real electrical devices, totaling **2 million minutes** of data with **1-minute granularity**. The prediction task shown below uses 100 minutes of data to forecast the next 20 minutes. All data are normalized.  
The dataset involves proprietary enterprise data and is not open-sourced.

<img src="./image/result.png" style="width: 55%;">

### Deployment and Usage

- **Client:**  
  The project uses a **WeChat Mini Program** as the frontend. Simply open the `WeChat_client` directory in the WeChat Developer Tool, then either publish it or package it with third-party tools.

- **Distributed Backend (Client Service):**  
  The backend module is developed in **C++17** for Linux systems (non-cross-platform). Use CMake to build the executable:

```bash
mkdir build
cd build
cmake ..
make
```

The generated executable `webserver` will appear in the `build` directory. Ensure that the `powerload.db` SQLite database file is in the same directory.
If C++ deployment is inconvenient, a **Python Flask backend** can be used instead, functionally equivalent though slightly less efficient (`/Python_backend/app.py`).

* **Distributed Backend (Data Processing) and AI Model Server:**
  This component resides in the `Python_backend` directory. It provides two options for backend-AI communication:

  * HTTP-based: (`app-backend.py` and `app-ai.py`)
  * RabbitMQ-based: (`app-backend-mq.py` and `app-ai-mq.py`)
    Run the AI model server first, then the distributed backend. The binary model files for classification and prediction are located in the `classify` and `prediction` directories, respectively.

* **Model Training:**
  Ensure that the `dataset` folder exists under `Python_backend`, containing multiple CSV files named after appliance labels or combinations.
  Execute the following commands to train the classification/decomposition model (~3 min on CPU) and the prediction model (~2 hrs on CPU):

```bash
Python ./classify/Classification_Train_v6.3.py
Python ./classify/prediction.py
```

You may modify hyperparameters according to your dataset.
In `prediction.py`, the following code sections may need adjustment:

```python
# Located in main function
batches, labels_batched, categories, category2filename_dict = data_process("./dataset")
model = train(batches, labels_batched, categories, category2filename_dict, num_heads=27, num_blocks=6, \
        lr=0.00004, epochs=13, static_vector_len=7, total_number_categories=21)
torch.save(model, "model-large.pt")

# Located in data_process function
data = get_data(os.path.join(directory, filename + ".csv"), skip_header=1, usecol=4)
```

In `Classification_Train_v6.3.py`, modify parameters as needed:

```python
# Located near file start
dc = r'../dataset'
model_save_path = r'Classification-Model-v6.3-2.2.keras'
matrix_save_path = r'Classification_feature-2.2.mat'
dict_save_path = r"label2index_dict.pkl"
pca_save_path = r"pca.pkl"
testRate = 0.15
frameLength = 800
step = 800
max_value = 3000000
eps = 75
lamb = 0.001
pca_n_components = 67
es_patience = 3
power_column = -1
```

### Client GUI Examples

The following screenshots show four main interfaces: login, user homepage, real-time waveform and classification/decomposition, and power prediction waveform.

<img src="./image/gui.png" style="width: 70%;" />

### Project Demo Video

<video src="https://github.com/duyu09/Powerload-Classification-and-Prediction-System/assets/92843163/0684486d-e391-4301-834f-0c5af6e6ce90" style="width: 65%;"></video>

---

### Copyright Notice

Copyright &copy; 2024
*The research and development group for Power Load Classification and Prediction System Based on Deep Learning Algorithm, Faculty of Computer Science & Technology, Qilu University of Technology (Shandong Academy of Sciences)*

All rights reserved by the R&D Group of the project “Power Load Classification and Prediction System Based on Deep Learning Algorithms,” Faculty of Computer Science & Technology, Qilu University of Technology (Shandong Academy of Sciences).

* **Group Members:**

  * **DU Yu** (Chinese: _杜宇_; Vietnamese: _ĐỖ Vũ_; Faculty of Computer Science & Technology, Qilu University of Technology (Shandong Academy of Sciences), No.202103180009)
  * **JIANG Chuan** (Chinese: _姜川_; Vietnamese: _KHƯƠNG Xuyên_; Faculty of Computer Science & Technology, Qilu University of Technology (Shandong Academy of Sciences), No.202103180020)
  * **LI Xiaoyu** (Chinese: _李晓语_; Vietnamese: _LÝ Hiểu Ngữ_; Faculty of Computer Science & Technology, Qilu University of Technology (Shandong Academy of Sciences), No.202103180001)
  * **LI Qinglong** (Chinese: _李庆隆_; Vietnamese: _LÝ Khánh Long_; Faculty of Computer Science & Technology, Qilu University of Technology (Shandong Academy of Sciences), No.202103180027)
  * **ZHANG Yiwen** (Chinese: _张一雯_; Vietnamese: _TRƯƠNG Nhất Văn_; Faculty of Computer Science & Technology, Qilu University of Technology (Shandong Academy of Sciences), No.202103180051)
* **Advisors:**

  * **JIA Ruixiang** (Chinese: _贾瑞祥_; Vietnamese: _GIẢ Thụy Tường_; Lecturer, Department of Software Engineering, Faculty of Computer Science & Technology, Qilu University of Technology (Shandong Academy of Sciences))
  * **CHEN Jing** (Chinese: _陈静_; Vietnamese: _TRẦN Tĩnh_; Shandong Computer Center (National Supercomputing Center in Jinan))

This project is open-sourced under our **custom license agreement**. Before obtaining the source code by any means, please read and understand the [LICENSE](./LICENSE) thoroughly.

* **Additional Notes:**

  * This project participated in the **17th China Collegiate Computing Competition (4C2024)**, Artificial Intelligence Practice Track.
  * The project **LOGO** was generated using the `CogView` AI art tool by Zhipu Qingyan (Chinese: _智谱清言_), then modified for use.
    **LOGO Meaning:**
    The metallic ring represents a power meter, symbolizing our non-intrusive monitoring approach.
    The internal stripes signify power waveform data and also resemble city skyscrapers, representing how our system serves urban power management.
    The wooden background symbolizes sustainable development and carbon reduction.

---

### Special Acknowledgement

* **Qilu University of Technology (Shandong Academy of Sciences)** (Chinese: _齐鲁工业大学（山东省科学院）_; Vietnamese: _Đại học Công nghiệp Tề Lỗ (Viện Khoa học tỉnh Sơn Đông)_)

<img src="./image/qlu.svg" style="width:40%;border-radius:20px;">

* **Faculty of Computer Science and Technology, National Supercomputing Center in Jinan** (Chinese: _计算机科学与技术学部，国家超级计算济南中心_; Vietnamese: _Học bộ Khoa học và Kỹ thuật Máy tính, Trung tâm Tính toán Siêu Máy tính Quốc gia Tế Nam_)

<img src="./image/fcst.svg" style="width:40%;border-radius:20px;">
<br>

* **Developer Association of Qilu University of Technology (Shandong Academy of Sciences)** (Chinese: _齐鲁工业大学（山东省科学院）开发者协会_; Vietnamese: _Hiệp hội Nhà phát triển Đại học Công nghiệp Tề Lỗ (Viện Khoa học tỉnh Sơn Đông)_)

<img src="./image/logo_of_developer_association.jpg" style="width:40%;border-radius:20px;">

### Links

* School of Electronic and Information Engineering, Lanzhou Jiaotong University [https://dxxy.lzjtu.edu.cn/](https://dxxy.lzjtu.edu.cn/)

* Qilu University of Technology (Shandong Academy of Sciences) [https://www.qlu.edu.cn/](https://www.qlu.edu.cn/)

* Shandong Computer Science Center (National Supercomputing Center in Jinan) [https://www.nsccjn.cn/](https://www.nsccjn.cn/)

* Faculty of Computer Science & Technology, Qilu University of Technology (Shandong Academy of Sciences) [http://jsxb.scsc.cn/](http://jsxb.scsc.cn/)

* Du Yu’s homepage in the research group [https://faculty.lzjtu.edu.cn/chenmei/zh_CN/xsxx/2554/content/1837.htm](https://faculty.lzjtu.edu.cn/chenmei/zh_CN/xsxx/2554/content/1837.htm)

* Du Yu’s GitHub Profile [https://github.com/duyu09/](https://github.com/duyu09/)
