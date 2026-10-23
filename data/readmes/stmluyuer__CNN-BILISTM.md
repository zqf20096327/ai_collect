# 基于CNN和BiLSTM实现时间序列预测模型

## 简介

这是我早期做的时间序列预测实验，用卷积神经网络（CNN）和双向长短期记忆网络（BiLSTM）从历史数据中提取特征、预测后续数值。仓库包含数据预处理、模型训练、评估和结果可视化的代码。

## 说明

CNN + BiLSTM 是初期测试用的基础模型。模型用 Python 的 Keras 构建，Pandas、NumPy 处理数据，Scikit-learn 做标准化，Matplotlib 绘图，SciPy 做统计分析。只用 Scikit-learn 做标准化，当时也觉得有点大材小用。

仓库里还有一个结合 LSTM 和特征工程的模型。当时试了不少办法，效果还是很差：

- 原始特征较少，因此用 `PolynomialFeatures` 生成多项式特征和交叉特征，再用随机森林评估特征重要性，保留关键特征。
- 数据分布不均，当时尝试用 `train_test_split` 划分训练集和测试集，希望减小两者的差异。随机划分本身不能保证分布接近。
- 训练时用 `EarlyStopping` 在验证损失不再改善时停止训练，用 `ReduceLROnPlateau` 降低学习率，希望减少过拟合并改善效果；损失函数为均方误差（MSE）。

这是早期练习，模型比较基础。当时被要求使用拼音命名，代码里保留了这些名字；已经熟悉这些模型的话，可以直接跳过。

## 预测模型的评估图

### 动态

![CNN-BILISTMdongtai](Test-1.png)

### 静态

![CNN-BILISTMjingtai](Test-2.png)

## 使用方法

1. 安装依赖：

   ```bash
   pip install -r requirements.txt
   ```

2. 在仓库根目录选择脚本运行，例如：

   ```bash
   python CNN-BILISTMdongtai.py
   ```

   `CNN-BILISTMdongtai.py`、`CNN-BILSTMjingtai.py` 和 `LSTMdongtai.py` 都从当前工作目录读取 `data.csv`。其中动态 CNN + BiLSTM 脚本取前 7 列作为输入、第 8 列作为目标，并用前 1190 行训练；更换数据时需要同时核对这些硬编码设置。

现有依赖清单只列出了当时使用的 Python 库，没有固定 Keras 的计算后端。运行前还需要准备与 Keras 3 兼容的后端；绘图使用 `TkAgg` 和 `SimHei`，需要相应的桌面绘图环境与字体。仓库保留的是实验代码，安装依赖并不代表已经在当前环境完成复现。
