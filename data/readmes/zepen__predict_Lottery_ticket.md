# AI 彩票号码预测

<img src="img/logo.png" alt="项目 Logo" width="80">

简体中文 | [English](README.en.md) | 

> **在线训练预测：** <https://www.ai-spinach.xyz>  
> **联系客服：** QQ1群: `246714623`，QQ2群: `980203303`

## 📖 项目简介

本项目是一个基于深度学习的彩票号码预测实验项目，**仅供娱乐，请勿用于任何非法用途或过度投注。**

项目的核心是**序列模型的预测能力**。与传统将每个号码独立预测不同，本项目将红球号码视为一个完整的序列进行建模，并引入 **CRF（条件随机场）** 层来捕捉号码之间的序列依赖关系。这种方式能有效避免独立预测产生的重复号码问题，提升预测结果的连贯性和合理性。蓝球则单独建立模型进行预测。

整个模型基于 TensorFlow 1.x 兼容模式构建，在 TensorFlow 2.x 下通过 `tf.compat.v1` 接口运行。

## ✨ 功能特性

- 支持双色球、大乐透、七乐彩、七星彩
- 提供在线训练预测 Web 应用，无需本地部署
- 采用 **LSTM + CRF 序列模型**，提升红球预测的连贯性
- 支持模型预测评估，可调整训练集/测试集比例
- 纯脚本化运行，无需 Docker 或微服务

## 🛠️ 安装

1. 安装 Anaconda（可参考 [教程](https://zhuanlan.zhihu.com/p/32925500)）
2. 创建 conda 环境：
   ```bash
   conda create -n your_env_name python=3.11
   ```
3. 激活环境并安装依赖：
      ```bash
      conda activate your_env_name
      pip install -r requirements.txt
      ```

## 🚀 快速开始
1. 获取训练数据
      ```bash
      python get_data.py --name ssq   # 双色球
      ```
    若解析错误，请检查网页 http://datachart.500.com/ssq/history/newinc/history.php 是否可正常访问。

    其他彩种参数：

    | 彩票名称 | 参数 |
    | --- | --- |
    | 大乐透 | `--name dlt` |
    | 七乐彩 | `--name qlc` |
    | 七星彩 | `--name qxc` |

2. 训练模型
    ```bash
    python run_train_model.py --name ssq
    ```
    先训练红球模型，再训练蓝球模型。模型参数和超参数在 config.py 中配置。训练时间取决于参数设置。

3. 预测号码
    ``` bash
    python run_predict.py --name ssq
    ```
    预测结果将打印在控制台。

## 📝 更新日志
* 新增七乐彩、七星彩支持（参数 qlc、qxc）

* 爬虫因风控改用 curl_cffi，Python 需升级至 3.11

* 上线 Web 端应用，无需下载源码即可在线训练预测

* 新增模型预测评估，可调整训练集/测试集比例（建议训练集采样比例 > 0.5）

* 修复大乐透蓝球号码预测超出取值范围的问题

* 修复训练传参导致数据维度不匹配的问题

* 新增对大乐透的完整支持（数据爬取、训练、预测），参数 --name dlt

* 废弃 Docker 模式和微服务，降低使用门槛，直接运行脚本即可

* 更新 requirements.txt 中相关库版本，解决大部分安装依赖问题

* 将红球作为整体序列模型（LSTM + CRF），替代原先红球独立预测的设定，避免重复号码。因 CRF 层 API 需在 tf.compat.v1.disable_eager_execution() 下运行，整个模型采用 1.x 构建和训练模式。