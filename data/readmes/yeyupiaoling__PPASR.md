![python version](https://img.shields.io/badge/python-3.8+-orange.svg)
![GitHub forks](https://img.shields.io/github/forks/yeyupiaoling/PPASR)
![GitHub Repo stars](https://img.shields.io/github/stars/yeyupiaoling/PPASR)
![GitHub](https://img.shields.io/github/license/yeyupiaoling/PPASR)
![支持系统](https://img.shields.io/badge/支持系统-Win/Linux/MAC-9cf)

# PPASR流式与非流式语音识别项目

PPASR是一款基于PaddlePaddle实现的自动语音识别框架，PPASR中文名称PaddlePaddle中文语音识别（PaddlePaddle Automatic Speech Recognition），当前为V3版本，与V2版本不兼容，如果想使用V2版本，请在这个分支[V2](https://github.com/yeyupiaoling/PPASR/tree/release/2.4.x)。PPASR致力于简单，实用的语音识别项目。可部署在服务器，Nvidia Jetson设备，未来还计划支持Android等移动设备。**别忘了star**

**欢迎大家扫码入知识星球或者QQ群讨论，知识星球里面提供项目的模型文件和博主其他相关项目的模型文件，也包括其他一些资源。**

<div align="center">
  <img src="https://yeyupiaoling.cn/zsxq.jpg" alt="知识星球" width="400">
  <img src="https://yeyupiaoling.cn/qq.jpg" alt="QQ群" width="400">
</div>

<br/>

**本项目使用的环境：**
 - Anaconda 3
 - Python 3.11
 - PaddlePaddle 2.6.1
 - Windows 11 or Ubuntu 22.04


# 在线试用

**网页版：** [在线试用地址](https://tools.yeyupiaoling.cn/speech/masr)

<div align="center">
  <img src="https://tools.yeyupiaoling.cn/static/wechat-qr/masr.jpg" alt="微信小程序" width="200"><br/>
  微信小程序
</div>


## 项目特点

1. 支持多个语音识别模型，包含`deepspeech2`、`conformer`、`squeezeformer`、`efficient_conformer`等，每个模型都支持流式识别和非流式识别，在配置文件中`streaming`参数设置。
2. 支持多种解码器，包含`ctc_greedy_search`、`ctc_prefix_beam_search`、`attention_rescoring`、`ctc_beam_search`等。
3. 支持多种预处理方法，包含`fbank`、`mfcc`等。
4. 支持多种数据增强方法，包含噪声增强、混响增强、语速增强、音量增强、重采样增强、位移增强、SpecAugmentor、SpecSubAugmentor等。
5. 支持多种推理方法，包含短音频推理、长音频推理、流式推理、说话人分离推理等。
6. 更多特点等待你发现。

## 与V2版本的区别

1. 项目结构的优化，大幅度降低的使用难度。
2. 更换预处理的库，改用kaldi_native_fbank，在提高数据预处理的速度，同时也支持多平台。
3. 修改token的方法，使用sentencepiece制作token，这个框架极大的降低了多种语言的处理难度，同时还使中英文混合训练成为可能。

## 更新记录

 - 2025.03: 正式发布最终级的V3版本。


## 视频讲解

 - [知识点讲解（哔哩哔哩）](https://www.bilibili.com/video/BV1Rr4y1D7iZ)
 - [流式识别的使用讲解（哔哩哔哩）](https://www.bilibili.com/video/BV1Te4y1h7KK)


## 模型下载

1. [WenetSpeech](./docs/wenetspeech.md) (10000小时，普通话) 的预训练模型列表，错误率类型为字错率（CER）：

|    使用模型     | 是否为流式 | 预处理方式 |          解码方式          | test_net | test_meeting | aishell_test |   下载地址   |
|:-----------:|:-----:|:-----:|:----------------------:|:--------:|:------------:|:------------:|:--------:|
|  Conformer  | True  | fbank |   ctc_greedy_search    | 0.14758  |   0.19562    |   0.06925    | 加入知识星球获取 |
|  Conformer  | True  | fbank | ctc_prefix_beam_search | 0.14689  |   0.19323    |   0.06930    | 加入知识星球获取 |
|  Conformer  | True  | fbank |  attention_rescoring   | 0.13786  |   0.18922    |   0.06028    | 加入知识星球获取 |
|  Conformer  | True  | fbank |    ctc_beam_search     | 0.20660  |   0.29835    |   0.05336    | 加入知识星球获取 |
| DeepSpeech2 | True  | fbank |   ctc_greedy_search    |          |              |              | 加入知识星球获取 |
| DeepSpeech2 | True  | fbank | ctc_prefix_beam_search |          |              |              | 加入知识星球获取 |
| DeepSpeech2 | True  | fbank |    ctc_beam_search     |          |              |              | 加入知识星球获取 |

2. [AIShell](https://openslr.magicdatatech.com/resources/33) (179小时，普通话) 的预训练模型列表，错误率类型为字错率（CER）：

|    使用模型     | 是否为流式 | 预处理方式 |          解码方式          | 自带的测试集  |   下载地址   |
|:-----------:|:-----:|:-----:|:----------------------:|:-------:|:--------:|
|  Conformer  | True  | fbank |   ctc_greedy_search    | 0.06110 | 加入知识星球获取 |
|  Conformer  | True  | fbank | ctc_prefix_beam_search | 0.06114 | 加入知识星球获取 |
|  Conformer  | True  | fbank |  attention_rescoring   | 0.05412 | 加入知识星球获取 |
|  Conformer  | True  | fbank |    ctc_beam_search     | 0.04468 | 加入知识星球获取 |
| DeepSpeech2 | True  | fbank |   ctc_greedy_search    | 0.14134 | 加入知识星球获取 |
| DeepSpeech2 | True  | fbank | ctc_prefix_beam_search | 0.14132 | 加入知识星球获取 |
| DeepSpeech2 | True  | fbank |    ctc_beam_search     | 0.10598 | 加入知识星球获取 |


3. [Librispeech](https://openslr.magicdatatech.com/resources/12) (960小时，英语) 的预训练模型列表，错误率类型为词错率（WER）：

|    使用模型     | 是否为流式 | 预处理方式 |          解码方式          | 自带的测试集  |   下载地址   |
|:-----------:|:-----:|:-----:|:----------------------:|:-------:|:--------:|
|  Conformer  | True  | fbank |   ctc_greedy_search    | 0.07562 | 加入知识星球获取 |
|  Conformer  | True  | fbank | ctc_prefix_beam_search | 0.07518 | 加入知识星球获取 |
|  Conformer  | True  | fbank |  attention_rescoring   | 0.06669 | 加入知识星球获取 |
|  Conformer  | True  | fbank |    ctc_beam_search     |    /    | 加入知识星球获取 |
| DeepSpeech2 | True  | fbank |   ctc_greedy_search    | 0.15479 | 加入知识星球获取 |
| DeepSpeech2 | True  | fbank | ctc_prefix_beam_search | 0.15247 | 加入知识星球获取 |
| DeepSpeech2 | True  | fbank |    ctc_beam_search     |    /    | 加入知识星球获取 |


4. 其他数据集的预训练模型列表，错误率类型，如果是中文就是字错率（CER），英文则是词错率（WER），中英混合为混合错误率（MER）：

|   使用模型    |             数据集              |  语言  |          解码方式          |  测试数据   |   下载地址   |
|:---------:|:----------------------------:|:----:|:----------------------:|:-------:|:--------:|
| Conformer |            粤语数据集             |  粤语  |   ctc_greedy_search    | 0.05834 | 加入知识星球获取 |
| Conformer |            粤语数据集             |  粤语  | ctc_prefix_beam_search | 0.05815 | 加入知识星球获取 |
| Conformer |            粤语数据集             |  粤语  |  attention_rescoring   | 0.04734 | 加入知识星球获取 |
| Conformer |            粤语数据集             |  粤语  |    ctc_beam_search     | 0.06191 | 加入知识星球获取 |
| Conformer |           中英混合数据集            | 中英文  |   ctc_greedy_search    | 0.09462 | 加入知识星球获取 |
| Conformer |           中英混合数据集            | 中英文  | ctc_prefix_beam_search | 0.09416 | 加入知识星球获取 |
| Conformer |           中英混合数据集            | 中英文  |  attention_rescoring   | 0.08283 | 加入知识星球获取 |
| Conformer |           中英混合数据集            | 中英文  |    ctc_beam_search     |    /    | 加入知识星球获取 |
| Conformer |       更大数据集（16000+小时）        | 中英文  |   ctc_greedy_search    |         | 加入知识星球获取 |
| Conformer |       更大数据集（16000+小时）        | 中英文  | ctc_prefix_beam_search |         | 加入知识星球获取 |
| Conformer |       更大数据集（16000+小时）        | 中英文  |  attention_rescoring   |         | 加入知识星球获取 |
| Conformer |       更大数据集（16000+小时）        | 中英文  |    ctc_beam_search     |         | 加入知识星球获取 |
| Conformer | CommonVoice-Uyghur + THUYG20 | 维吾尔语 |   ctc_greedy_search    | 0.04510 | 加入知识星球获取 |
| Conformer | CommonVoice-Uyghur + THUYG20 | 维吾尔语 | ctc_prefix_beam_search | 0.04404 | 加入知识星球获取 |
| Conformer | CommonVoice-Uyghur + THUYG20 | 维吾尔语 |  attention_rescoring   | 0.02823 | 加入知识星球获取 |


**说明：** 
1. 这里字错率或者词错率是使用`eval.py`。
2. 分别给出了使用三个解码器的错误率，其中`ctc_prefix_beam_search`、`attention_rescoring`的解码搜索大小为10。
3. 训练时使用了噪声增强和混响增强，以及其他增强方法，具体请看配置参数`configs/augmentation.yml`。
4. 这里只提供了流式模型，但全部模型都支持流式和非流式的，在配置文件中`streaming`参数设置。
5. 使用`CommonVoice-Uyghur`的测试集作为本项目测试集，其余的和THUYG20全部作为训练集。

>有问题欢迎提 [issue](https://github.com/yeyupiaoling/PPASR/issues) 交流


## 文档教程

- [快速安装](./docs/install.md)
- [快速使用](./docs/GETTING_STARTED.md)
- [数据准备](./docs/dataset.md)
- [WenetSpeech数据集](./docs/wenetspeech.md)
- [合成语音数据](./docs/generate_audio.md)
- [数据增强](./docs/augment.md)
- [训练模型](./docs/train.md)
- [集束搜索解码](./docs/beam_search.md)
- [执行评估](./docs/eval.md)
- [导出模型](./docs/export_model.md)
- [使用标点符号模型](./docs/punctuation.md)
- 预测
   - [本地预测](./docs/infer.md)
   - [说话人日志语音识别](./docs/infer.md)
   - [Web部署模型](./docs/infer.md)
   - [GUI界面预测](./docs/infer.md)
- [常见问题解答](./docs/faq.md)


## 相关项目
 - 基于PaddlePaddle实现的声纹识别：[VoiceprintRecognition-PaddlePaddle](https://github.com/yeyupiaoling/VoiceprintRecognition-PaddlePaddle)
 - 基于PaddlePaddle静态图实现的语音识别：[PaddlePaddle-DeepSpeech](https://github.com/yeyupiaoling/PaddlePaddle-DeepSpeech)
 - 基于Pytorch实现的语音识别：[MASR](https://github.com/yeyupiaoling/MASR)


## 特别感谢

 - 感谢 <img src="docs/images/PyCharm_icon.png" height="25" width="25" >[JetBrains开源社区](https://jb.gg/OpenSourceSupport) 提供开发工具。

## 打赏作者

<br/>
<div align="center">
<p>打赏一块钱支持一下作者</p>
<img src="https://yeyupiaoling.cn/reward.jpg" alt="打赏作者" width="400">
</div>

## 参考资料
 - https://github.com/PaddlePaddle/PaddleSpeech
 - https://github.com/jiwidi/DeepSpeech-pytorch
 - https://github.com/wenet-e2e/WenetSpeech
