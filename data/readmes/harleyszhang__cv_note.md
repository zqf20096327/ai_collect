<h1 align="center">
CV 算法工程师成长之路
</h1>

<p align="center">
  <a href="#License"><img src="./data/icons/License-Apache-2.0-green.svg" alt="LICENSE"></a>
  <a href="http://www.armcvai.com/"><img src="./data/icons/Website-armcvai-brightgreen.svg", alt="嵌入式视觉"></a>
  <a href="https://www.zhihu.com/people/tang-fen-44-49"><img src="https://img.shields.io/badge/zhihu-知乎-informational" alt="进击的程序猿"></a>
  <a href="https://blog.csdn.net/qq_20986663"><img src="https://img.shields.io/badge/csdn-CSDN-red.svg" alt="嵌入式视觉"></a>
  <a href="https://www.cnblogs.com/armcvai/"><img src="https://img.shields.io/badge/cnblogs-博客园-important.svg" alt="嵌入式视觉"></a>
  <a href="https://juejin.cn/user/3034307824977127/columns"><img src="https://img.shields.io/badge/juejin-%E6%8E%98%E9%87%91-important.svg" alt="嵌入式视觉"></a>
  <a href="https://github.com/HarleysZhang/2021_algorithm_intern_information/stargazers"><img src="https://badgen.net/github/stars/HarleysZhang/2021_algorithm_intern_information?color=cyan" alt="stars"></a>
  <a href="https://github.com/HarleysZhang/2021_algorithm_intern_information/network/members"><img src="https://badgen.net/github/forks/HarleysZhang/2021_algorithm_intern_information?color=cyan" alt="forks"></a>
</p>

- [我的自制大模型推理框架课程介绍](#我的自制大模型推理框架课程介绍)
- [前言](#前言)
- [目录](#目录)
- [学习路线](#学习路线)
- [算法基础](#算法基础)
- [可投递公司](#可投递公司)
- [我的公众号](#我的公众号)
- [Star History](#star-history)

## 我的自制大模型推理框架课程介绍

1. **框架亮点**：基于 Triton + PyTorch 开发的轻量级、且简单易用的大模型推理框架，采用类 Pytorch 语法的 Triton 编写算子，绕开 Cuda 复杂语法实现 GPU 加速。
2. **价格：499**。非常实惠和便宜，课程 + 项目 + 面经 + 答疑质量绝对对得起这个价格。
3. **课程优势​**：
   - **手把手教你从 0 到 1 实现大模型推理框架**。
   - 项目导向 + 面试导向 + **分类总结的面试题**。
   - 2025 最新的高性能计算/推理框架岗位的大厂面试题汇总
4. **项目优势​**：
	- 架构清晰，代码简洁且注释详尽，覆盖大模型离线推理全流程。​
    - 运用 OpenAI Triton 编写高性能计算 Kernel，开发矩阵乘法内核，效率堪比 cuBLAS。​
    - 依托 PyTorch 进行高效显存管理。​
    - 课程项目完美支持 FlashAttentionV1、V2、V3 与 `GQA`，以及 `PageAttention` 的具体实现。​
    - 使用 `Triton` 编写融合算子，如 KV 线性层融合等。​
    - 适配最新的 `llama/qwen2.5/llava1.5` 模型，相较 transformers 库，在 llama3 1B 和 3B 模型上，加速比最高可达 `4` 倍。
5. **分类总结部分面试题**：

<table style="width: 100%; table-layout: fixed;">
  <tr>
    <td align="center"><img src="./data/images/read_me/interview1.png" width="100%" alt="llava_output2"></td>
    <td align="center"><img src="./data/images/read_me/interview2.png" width="100%" alt="llava_output"></td>
  </tr>
</table>

6. **项目运行效果**:

`llama3.2-1.5B-Instruct` 模型流式输出结果测试：

![流式输出](./data/images/read_me/generate.gif)

`Qwen2.5-3B` 模型（社区版本）流式输出结果测试：

![流式输出](./data/images/read_me/output.gif)

`Llava1.5-7b-hf` 模型流式输出结果测试:

<table style="width: 100%; table-layout: fixed;">
  <tr>
    <td align="center"><img src="./data/images/read_me/llava_output2.gif" width="90%" alt="llava_output2"></td>
    <td align="center"><img src="./data/images/read_me/llava_output1.gif" width="100%" alt="llava_output"></td>
  </tr>
</table>

感兴趣的同学可以扫码联系课程购买，这个课程是我和[《自制深度学习推理框架》作者](https://space.bilibili.com/1822828582)一起合力打造的，内容也会持续更新优化。

<div align="center">
<img src="./data/images/read_me/my_wechat.jpg" width="40%" alt="transformer_block_mp">
</div>

## 前言

> 本项目最初是当作 cv 算法工程师实习内推表、校招可投递公司汇总以及个人面经的汇总，后面逐步转变为个人 cv 算法工程师成长之路所记录的技术栈笔记、以及少部分面经等内容。

项目部分内容参考自 `github` 项目/网络博客/书籍和 [个人博客](http://www.armcvai.com/) 等，由于时间和精力有限，有些知识点还没有没有完成，请见谅。

本项目正逐步废弃，大部分内容不再更新，关于深度学习、大模型推理以及大模型推理框架开发的知识，欢迎移步 [dl_note](https://github.com/HarleysZhang/dl_note)、和 [lite_llama](https://github.com/harleyszhang/lite_llama) 仓库阅读。

> `GitHub` 已经支持直接显示 `latex` 公式，部分公式如果显示不全，也可在谷歌浏览器安装 [MathJax Plugin for Github](https://chrome.google.com/webstore/detail/mathjax-plugin-for-github/ioemnmodlmafdkllaclgeombjnmnbima?hl=zh-CN) 插件访问(需要翻墙下载安装)，或者下载仓库到本地，使用 `Typora` 软件阅读，也可以使用安装了 `Markdown+Math` 插件的 `VSCode` 软件阅读。

## 目录

作为一个计算机视觉算法工程师，需要掌握的不仅是计算机编程知识，还需要掌握**编程开发、机器学习/深度学习、图像识别/目标检测/语义分割、模型压缩、模型部署**等知识点，我整理了一个 [技术栈思维导图](./data/images/CV算法工程师应掌握知识点.png)。

强调一下如何从“零”起步，首先确保基础打好。建议完整修完一门国外经典课程（从课程视频、作业到项目），然后完整阅读一本机器学习或者深度学习教科书，同时熟练掌握一门基本的编程语言以及深度学习框架。（参考 [中国人民大学赵鑫：AI 科研入坑指南](https://mp.weixin.qq.com/s/h00VmCi1E7IhIDCj7X1ZjQ)）

+ [计算机基础](1-computer_basics)
+ [编程语言](2-programming_language)
+ [数据结构与算法](3-data_structure-algorithm)
+ [机器学习](4-machine_learning)
+ [深度学习](5-deep_learning)
+ [计算机视觉](6-computer_vision)
+ [模型压缩与量化](7-model_compression)
+ [高性能计算](8-high-performance_computing)
+ [模型部署](9-model_deploy)
+ [图像算法岗面经](interview_summary)

## 学习路线

[cv算法工程师学习成长路线](./cv算法工程师成长路线.md)

## 算法基础

> 深度学习基础的和 `Python` 编程基础知识总结。

+ [深度学习基础](4-deep_learning/深度学习基础总结.md)
+ [Python3 基础](2-programming_language/python3/python3编程总结.md)

## 可投递公司

> 鉴于 2019 年写的春招算法实习岗位表绝大部分已经失效，本人也再无精力维护，故将其移除，故不在展示在仓库主页上。

虽然算法工程师可投递的公司是较多的，但是岗位提供的 `hc` 是不及开发多的，这点需要注意。以下表格侧重于计算机视觉算法和算法优化/部署工程师岗位。

|`top`级公司|互联网公司|AI独角兽公司|其他大公司|
|------------|---------------|---------------|-------------|
|百度|美团|地平线机器人|顺丰科技|
|阿里巴巴|滴滴出行|图森未来|招银网络科技|
|腾讯|拼多多/菜鸟网络|momenta|平安科技|
|字节跳动|京东|小马智行|cvte|
|微软|网易|蔚来汽车|海康威视|
|谷歌|快手|小鹏汽车|虹软科技|
|商汤|爱奇艺|科大讯飞|传音手机|
|英伟达|小米|寒武纪/依图|大华|
|博世|陌陌|旷视|荣耀手机|
|大疆无人机|美图MTlab|文远知行|联想|
|蚂蚁金服|360安全|云天励飞|汇顶科技|
|Intel/亚马逊|搜狗|摩尔线程|美的中央研究院|
|华为|猿辅导|思必驰|锐明技术|
|无|新浪/搜狐/金山|奥比中光|联发科|
|无|YY/虎牙/BIGO/斗鱼|优必选|联影医疗|
|无|oppo/vivo/一加|度小满金融|戴尔|
|无|贝壳找房|深睿医疗|TP-LINK|
|无|携程/去哪儿/途家|镁佳科技|ZOOM|
|无|瓜子二手车|猎豹移动|广联达|
|无|作业帮/VIPKID/好未来|京东数科|深信服|
|无|阅文集团/58集团|追一科技|中国电信云计算|
|无|B站|深兰科技|三星电子研究所|
|无|小红书/英语流利说|明略科技|苏宁|
|无|趣头条/一点资讯|数美科技|微众银行|
|无|知乎|驭势科技|中国移动成研院|
|无|蘑菇街|随手科技|远景智能|
|无|转转|智加科技|牧原智能科技|
|无|同花顺/老虎证券|壁仞科技|便利蜂|
|无|乐信/有赞|趋势科技|中兴|
|无|金蝶软件(中国)|云从科技|航天二院706所|
|无|汽车之家|第四范式|吉利汽车|
|无|珍爱网/酷狗音乐|黑芝麻智能|碧桂园机器人|
|无|巨人网络/盛大游戏|格灵深瞳|华米/极米|无|
|无|最右/快看漫画|码隆科技|无|
|无|猫眼娱乐/多牛传媒|轻舟智航|无|无|

## 我的公众号

更多知识和最新博客，欢迎扫码关注我的公众号-**嵌入式视觉**，记录 `CV` 算法工程师成长之路，分享技术总结、读书笔记和个人感悟。

<p align="center">
  <a href="#嵌入式视觉"><img src="./data/qcode.png" alt="公众号-嵌入式视觉"></a>
</p>

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=HarleysZhang/cv_note&type=Date)](https://star-history.com/#HarleysZhang/cv_note&Date)
