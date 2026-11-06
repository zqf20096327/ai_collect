# D2L 课程笔记与基础速成教材

本仓库用于整理李沐老师的《动手学深度学习》（D2L）课程笔记和基础速成教材，帮助具备基础 Python 知识的读者尽快看懂常见代码、跟上课程。当前收录的八讲采用 **PyTorch** 版示例，可结合 [D2L 中文教材](https://zh.d2l.ai/) 和课程讲解阅读。

[**在线阅读修订版**](D2L%E4%BB%A3%E7%A0%81%E9%80%9F%E6%88%90%E5%85%AB%E8%AE%B2%EF%BC%88PyTorch%E7%89%88%EF%BC%89-%E4%BF%AE%E8%AE%A2%E7%89%88.pdf) · [**下载修订版 PDF**](https://github.com/Needy1100/d2l-pytorch-crash-course/releases/download/course-pdf-revised/d2l-notes-and-crash-course-revised.pdf) · [查看教材目录](#教材目录)

[为什么先读速成教材](#为什么先读速成教材) · [D2L 课程介绍](#d2l-课程介绍) · [关于李沐老师](#关于李沐老师) · [课程与官方资源](#课程与官方资源)

## 为什么先读速成教材

D2L 把数学推导、模型原理和代码实现放在一起讲。对于刚接触深度学习的读者，即使会写 Python，第一次读到张量广播、自动求导或完整训练循环，也容易同时卡在公式、代码和张量形状上，直接跟课会有一定门槛。

这份基础速成教材把这些前置内容集中讲清楚：先认识常见写法和形状变化，再把数据加载、模型定义、损失计算和参数更新串成一条流程。带着这张流程图再学 D2L，就更容易判断一行代码在解决什么问题，把精力放到模型原理和实验结果上。

## 已收录资料：D2L 基础速成八讲（PyTorch 版）

<p align="center">
  <img src="assets/cover.png" alt="D2L 基础速成八讲 PDF 封面" width="380">
</p>

这份教辅适合在开始学习 D2L 前熟悉常见代码，也可在学习途中查阅。内容从张量的形状和运算入手，讲到怎样准备数据、定义模型、计算梯度，以及完成训练和评估。

教材适合已经掌握基础 Python 语法、刚开始学习深度学习的读者。书中结合代码示例说明每一步在做什么、数据怎样流动，以及遇到形状或类型不匹配时从哪里查起。

**全书共八讲，PDF 共 61 页，正文单独编号，共 57 页。** 部分代码示例参考李沐等人编写的《动手学深度学习》（D2L）。

## D2L 课程介绍

《动手学深度学习》（**Dive into Deep Learning**，简称 **D2L**）是一套将理论、代码和练习放在一起的深度学习教材。李沐老师主讲的[中文在线课程 v2](https://c.d2l.ai/zh-v2/)配合教材第二版，使用 PyTorch 演示模型实现。课程适合有基础 Python 编程和数学知识、希望自己动手训练模型的学习者。

- **打基础**：从数据操作、线性代数和自动求导开始，通过线性回归、softmax 回归和多层感知机理解损失函数、反向传播和训练循环。
- **学模型**：进一步学习卷积神经网络、循环神经网络和注意力机制，理解不同网络为什么适合处理不同的数据。
- **做实践**：结合图像分类、目标检测、机器翻译等任务，练习把模型原理落实到数据处理、代码实现和结果评估中。

课程主页按讲次列出学习内容，并提供对应课件和视频入口。学习时可以先读教材，再运行例子验证自己的理解；如果卡在张量形状、参数含义或训练代码，可以回查本仓库的基础速成八讲。

## 关于李沐老师

李沐（Mu Li）是 D2L 中文在线课程的主讲人，也是《动手学深度学习》的共同作者之一。2017 年获卡内基梅隆大学计算机科学博士学位，博士研究聚焦大规模分布式机器学习。 [卡内基梅隆大学计算机科学系](https://csd.cmu.edu/academics/doctoral/degrees-conferred/mu-li)

- **学术成果**　以第一作者在 USENIX OSDI 发表参数服务器论文，另获 ACM WSDM 最佳论文荣誉提名。 [OSDI 论文](https://www.usenix.org/conference/osdi14/technical-sessions/presentation/li_mu) · [WSDM 获奖名单](https://www.wsdm-conference.org/2016/)
- **工业与开源实践**　曾任 AWS 机器学习首席科学家，带领团队开发 Apache MXNet。 [AWS 研究者访谈](https://aws.amazon.com/blogs/machine-learning/in-the-research-spotlight-mu-li/)

**教材影响**

- **出版与高校采用**　李沐参与编写的英文教材 *Dive into Deep Learning* 由剑桥大学出版社出版。据 D2L 项目统计，教材中英文版已被 **70 多个国家的 500 多所大学**用于教学。项目列出的采用院校包括斯坦福大学、麻省理工学院和剑桥大学。 [剑桥大学出版社书目资料](https://assets.cambridge.org/97810093/89433/frontmatter/9781009389433_frontmatter.pdf) · [D2L 中文项目](https://github.com/d2l-ai/d2l-zh) · [D2L 英文项目](https://github.com/d2l-ai/d2l-en)
- **课堂案例**　加州大学伯克利分校 2019 年春季的《深度学习导论》（STAT 157）在课程网站上将 D2L 列为教材，并在自动求导、softmax 回归等教学单元中链接对应章节。 [伯克利 STAT 157 课程网站](https://courses.d2l.ai/berkeley-stat-157/index.html)
- **公开学习资源**　中英文教材均可在线阅读。书中的公式、图示和可运行代码编排在 Jupyter Notebook 中，读者可以边学原理边修改代码，观察结果如何变化。 [D2L 教材前言](https://www.d2l.ai/chapter_preface/index.html)

## 课程与官方资源

- [D2L 中文在线课程 v2](https://c.d2l.ai/zh-v2/)：课程安排、课件与视频入口。
- [B 站课程：《动手学深度学习 v2》](https://www.bilibili.com/list/1567748478?bvid=BV1oX4y137bC&oid=714717789)：从课程安排开始观看。
- [B 站账号：跟李沐学AI](https://space.bilibili.com/1567748478)：李沐老师发布课程视频的账号。
- [D2L 中文教材](https://zh.d2l.ai/)：在线正文、示例代码和练习。
- [D2L 英文教材（English）](https://d2l.ai/)：*Dive into Deep Learning* 英文原书。
- [D2L 中文版 GitHub 仓库（d2l-zh）](https://github.com/d2l-ai/d2l-zh)：中文教材源文件。
- [D2L 英文版 GitHub 仓库（d2l-en）](https://github.com/d2l-ai/d2l-en)：英文教材源文件。
- [D2L 中文课程 v2 GitHub 仓库](https://github.com/d2l-ai/courses-zh-v2)：中文课程网站及配套资料。

## 阅读建议

1. **第一至三章：熟悉张量和基本运算。** 先看一遍完整流程，再练习判断索引、变形和运算后的张量形状。
2. **第四至六章：读懂数据、模型与梯度。** 跟着一批数据，看它怎样进入模型、算出损失，再反向计算参数梯度。
3. **第七至八章：串起训练与评估。** 对照完整示例，找出训练模式切换、参数更新、指标统计和模型保存的位置。

> 阅读代码时，可以先写下输入和输出的形状，再判断这行是在整理数据、执行计算，还是更新参数。

### 运行环境与排查

直接阅读 PDF 无需安装环境。为方便对照学习，本教材的代码写法、接口和运行环境以 **D2L 中文版 2.0.0 的 PyTorch 示例**为准，采用课程指定版本。请按官方安装说明准备 Python 3.9、Jupyter Notebook、PyTorch 1.12.0、torchvision 0.13.0 和 `d2l==0.17.6`。[D2L 官方安装说明](https://zh-v2.d2l.ai/chapter_installation/index.html)

如果遇到导入失败、找不到函数或参数不兼容，先核对 Notebook 当前内核和已安装的版本。若版本不同，切换到课程环境，重启内核并按原顺序运行前置单元。仍有异常时，可到 Issues 附上报错、教材正文页码和依赖版本。

## 教材目录

以下章节按 PDF 原目录顺序列出，附英文标题。

### 第一章 代码全局结构（Anatomy of a Training Program）

**正文第 1 页。** 先认识一段训练程序中的数据、模型、损失和参数更新，再分别学习各部分的写法。

- 1.1 数据准备与整理（Data Preparation and Organization）
- 1.2 模型构建（Model Construction）
- 1.3 损失与参数学习（Loss and Parameter Learning）
- 1.4 训练流程概览（Overview of the Training Workflow）

### 第二章 张量基础操作（Basic Tensor Operations）

**正文第 5 页。** 学会读出张量的形状和类型，区分改变形状、调整轴顺序和修改元素。

- 2.1 创建张量（Creating Tensors）
- 2.2 形状、轴数与元素总数（Shape, Number of Dimensions, and Element Count）
- 2.3 数据类型与转换（Data Types and Conversion）
- 2.4 索引、切片与赋值（Indexing, Slicing, and Assignment）
- 2.5 改变形状（Reshaping Tensors）
- 2.6 增减长度为 1 的轴（Adding and Removing Size-One Dimensions）
- 2.7 调整轴顺序（Reordering Dimensions）
- 2.8 提取 Python 数字（Extracting a Python Scalar）
- 2.9 综合示例：读取与修改张量（Worked Example: Reading and Modifying Tensors）

### 第三章 张量运算（Tensor Computation）

**正文第 11 页。** 从输入形状判断运算是否可行，并用 softmax 示例串起按轴求和、保留维度和广播。

- 3.1 逐元素运算（Elementwise Operations）
- 3.2 求和、均值与轴（Sums, Means, and Axes）
- 3.3 保留汇总轴（Keeping Reduced Dimensions）
- 3.4 广播规则（Broadcasting Rules）
- 3.5 拼接与堆叠（Concatenation and Stacking）
- 3.6 点积与矩阵乘法（Dot Products and Matrix Multiplication）
- 3.7 比较、筛选与计数（Comparison, Filtering, and Counting）
- 3.8 综合示例：softmax（Worked Example: Softmax）

### 第四章 数据加载与预处理（Data Loading and Preprocessing）

**正文第 18 页。** 从单条样本追踪到一个批次，看清预处理在什么时候执行、特征与标签怎样对应。

- 4.1 数据集与数据加载器（Datasets and Data Loaders）
- 4.2 解析 load_array（Understanding `load_array`）
- 4.3 数据加载参数（Data Loader Arguments）
- 4.4 批次解包（Unpacking Batches）
- 4.5 迭代器与遍历控制（Iterators and Iteration Control）
- 4.6 生成器与 yield（Generators and `yield`）
- 4.7 图像预处理（Image Preprocessing）
- 4.8 表格预处理（Tabular Data Preprocessing）
- 4.9 常见 Python 语法（Common Python Syntax）
- 4.10 综合示例：检查图像批次（Worked Example: Inspecting an Image Batch）

### 第五章 模型定义与参数（Model Definition and Parameters）

**正文第 26 页。** 区分创建网络层和调用网络层，沿着 LeNet 的各层检查输出形状。

- 5.1 创建模型与调用模型（Creating and Calling Models）
- 5.2 顺序容器 Sequential（The `Sequential` Container）
- 5.3 全连接层的参数与计算（Fully Connected Layers: Parameters and Computation）
- 5.4 自定义模型 Module（Defining Custom Models with `Module`）
- 5.5 模型调用与函数式接口（Model Calls and the Functional API）
- 5.6 卷积、激活与池化（Convolution, Activation, and Pooling）
- 5.7 综合示例：LeNet（Worked Example: LeNet）
- 5.8 参数访问与管理（Accessing and Managing Parameters）
- 5.9 参数初始化（Parameter Initialization）
- 5.10 逐层检查输出形状（Checking Output Shapes Layer by Layer）

### 第六章 自动求导、损失与优化器（Automatic Differentiation, Loss, and Optimizers）

**正文第 34 页。** 看清损失值、参数梯度和参数本身之间的关系，理解清梯度、反向传播和更新各自的作用。

- 6.1 开启梯度追踪（Enabling Gradient Tracking）
- 6.2 反向传播与参数梯度（Backpropagation and Parameter Gradients）
- 6.3 单元素目标与损失汇总（Single-Element Objectives and Loss Aggregation）
- 6.4 梯度清理（Clearing Gradients）
- 6.5 分离结果与关闭梯度记录（Detaching Tensors and Disabling Gradient Tracking）
- 6.6 损失函数与损失值（Loss Functions and Loss Values）
- 6.7 损失汇总参数 reduction（The Loss `reduction` Argument）
- 6.8 交叉熵的输入要求（Input Requirements for Cross-Entropy）
- 6.9 优化器的职责（What Optimizers Do）
- 6.10 手写 SGD 与梯度缩放（Implementing SGD and Scaling Gradients）
- 6.11 综合示例：单批参数更新（Worked Example: Updating Parameters for One Batch）

### 第七章 训练与评估（Training and Evaluation）

**正文第 42 页。** 把单批更新放回整轮训练，分清训练模式和评估模式，以及准确率的计算方式。

- 7.1 训练模式与评估模式（Training and Evaluation Modes）
- 7.2 轮次、批次与更新步（Epochs, Batches, and Update Steps）
- 7.3 预测类别与 argmax（Predicted Classes and `argmax`）
- 7.4 正确数量与准确率（Correct Predictions and Accuracy）
- 7.5 指标累加器（Metric Accumulators）
- 7.6 解析单轮训练函数（Understanding the Single-Epoch Training Function）
- 7.7 整轮指标的加权统计（Weighted Metrics Across an Epoch）
- 7.8 解析评估函数（Understanding the Evaluation Function）
- 7.9 多轮训练与指标组合（Training Across Epochs and Combining Metrics）
- 7.10 结果展示与检查（Displaying and Checking Results）

### 第八章 设备、存取与综合阅读（Devices, Saving and Loading, and a Code Walkthrough）

**正文第 50 页。** 学习设备迁移和模型存取，最后通过多层感知机示例回顾从数据加载到训练的过程。

- 8.1 计算设备与设备选择（Compute Devices and Device Selection）
- 8.2 模型与数据的设备迁移（Moving Models and Data Between Devices）
- 8.3 张量与容器的存取（Saving and Loading Tensors and Containers）
- 8.4 模型状态字典（Model State Dictionaries）
- 8.5 重建模型与加载状态（Rebuilding a Model and Loading Its State）
- 8.6 加载设备映射与一致性检查（Device Mapping on Load and Consistency Checks）
- 8.7 训练检查点（Training Checkpoints）
- 8.8 D2L 辅助函数与辅助类（D2L Helper Functions and Classes）
- 8.9 综合阅读：多层感知机训练（Code Walkthrough: Training a Multilayer Perceptron）

## 问题反馈

- **问题反馈**：欢迎在 [Issues](https://github.com/Needy1100/d2l-pytorch-crash-course/issues) 提出勘误或阅读建议。附上正文页码及对应的语句或代码，便于定位。
