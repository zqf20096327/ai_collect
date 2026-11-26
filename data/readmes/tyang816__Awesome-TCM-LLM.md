# 🔥 开源中医模型、数据、论文、专利

**语言 / Language:** [中文](README.md) | [English](README_EN.md)

![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-green)  [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Stars](https://img.shields.io/github/stars/tyang816/Awesome-TCM-LLM?color=yellow)  ![Forks](https://img.shields.io/github/forks/tyang816/Awesome-TCM-LLM?color=blue&label=Fork) [![中文门户](https://img.shields.io/badge/中医资源-门户-blue)](https://tyang816.github.io/zh/projects/tcm/) [![Project](https://img.shields.io/badge/Project-tyang816.github.io-informational)](https://tyang816.github.io/projects/tcm/)

开源中医模型、数据、论文、专利精选，也带一点相关中文医疗。现在大概有 104 条新闻、117 个模型、95 篇综述、73 件专利、206 个数据集、449 篇方法论文、36 门公开课，以及 [452 位中医药人工智能导师](wiki/People.md)。[欢迎补条目](CONTRIBUTING.md)。

[项目页](https://tyang816.github.io/projects/tcm/) · [中文项目页](https://tyang816.github.io/zh/projects/tcm/) · [Wiki](wiki/Home.md) · [主页](https://tyang816.github.io/zh/)

## 先看这里

真能下载复现的中医权重大概 21 个，都在[开源模型](#开源模型)里。新闻里医院、公司发的，多数没有公开权重，当不了实验底座。

近年的研究逐渐扩展到多模态、Agent 和临床推理评测。对比模型时，应分别查看考试知识、证候判别和处方任务；TCM-Ladder、LingLanMedBench、MTCMB 提供了互补的评测资源。

| 你想做什么 | 可以先看 | 备注 |
| --- | --- | --- |
| 本机跑通一个模型 | **[扁仓 (BianCang)](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct)**、**[仲景 (ZhongJing)](https://huggingface.co/CMLM/ZhongjingGPT1_13B)** | 论文、权重、代码都有 |
| 做中医问诊 | **[MedChatZH](https://github.com/tyang816/MedChatZH)** | 还有配套问诊数据 |
| 舌诊、四诊 | **[ShizhenGPT](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni)** | 多模态，数据和权重都开 |
| 自己接着训 | **[ChatTCM](https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain)**、**[神农大模型 (ShenNong-TCM-LLM)](https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM)** | 预训练或指令数据是公开的 |
| 电脑比较一般 | **[杏核 (Xinghe)](https://huggingface.co/zsyjsld/Xinghe1.2-9B)** | 9B，有 GGUF |
| 做对比实验 | **[TCM-Ladder](https://arxiv.org/abs/2505.24063)**、**[LingLanMedBench（灵兰）](https://arxiv.org/abs/2602.01779v2)** | 任务说得比较清楚；更多在[数据集](#数据集) |
| 写相关工作 | 近两年的 scoping review | 先翻[综述](#综述)，别从单篇模型论文起 |
| 找公开课 | [学习资料](#学习资料) | 高校公开课和系列讲座，只收可核验的一手链接 |
| 找导师 | [导师](wiki/People.md) | 完整名单按高校、产业、医院和地区排列 |

同名不一定是同一个东西。「仲景」至少有 ZhongJingGPT 和 AAAI 那条 CMtMedQA；TCM-Eval 也不止一套。说不清时看 [Getting Started](wiki/Getting-Started.md)。

## 导师

完整名单共 452 位，写在 [Wiki · 导师](wiki/People.md)，先按地区，再按高校、医院或公司。这里只保留人数统计。

**按单位类型**

| 分类 | 人数 |
| --- | ---: |
| 高校 | 360 |
| 产业 | 47 |
| 医院 | 45 |

**按地区**

| 分类 | 人数 |
| --- | ---: |
| 北京 | 80 |
| 天津 | 28 |
| 河北 | 5 |
| 山西 | 4 |
| 内蒙古 | 8 |
| 辽宁 | 8 |
| 吉林 | 4 |
| 黑龙江 | 4 |
| 上海 | 45 |
| 江苏 | 21 |
| 浙江 | 16 |
| 安徽 | 12 |
| 福建 | 13 |
| 江西 | 13 |
| 山东 | 20 |
| 河南 | 12 |
| 湖北 | 15 |
| 湖南 | 17 |
| 广东 | 30 |
| 广西 | 9 |
| 海南 | 1 |
| 重庆 | 4 |
| 四川 | 7 |
| 贵州 | 13 |
| 云南 | 9 |
| 西藏 | 3 |
| 陕西 | 3 |
| 甘肃 | 2 |
| 青海 | 3 |
| 宁夏 | 3 |
| 新疆 | 3 |
| 香港 | 9 |
| 澳门 | 4 |
| 台湾 | 7 |
| 日本 | 3 |
| 韩国 | 5 |
| 新加坡 | 1 |
| 美国 | 1 |
| 澳大利亚 | 1 |
| 其他 | 6 |

## 开源模型

上面是起步用的。要翻全部能下的权重，或只有论文/产品、通用中文医疗底座、闭源产品和日韩汉方/韩医，点开即可。

<details>
<summary>能下载的权重，共 21 个</summary>

| 模型 | 年 | 机构 | 特色 | 链接 |
| --- | :---: | --- | --- | --- |
| **知方丹台 (ZhiFangDanTai)** | 2026 | 首都师范大学 | RAG · 图谱 | [论文](https://arxiv.org/abs/2509.05867) · [权重](https://huggingface.co/tczzx6/ZhiFangDanTai1.0) · [数据](https://huggingface.co/datasets/tczzx6/ZhiFangDanTai1.0) |
| **灵丹-V2 (Lingdan-V2)** | 2026 | 北京交通大学 | 处方 · 推理 | [论文](https://arxiv.org/abs/2610.14705) · [权重](https://huggingface.co/TCMLLM/Lingdan-8B-R1) · [代码](https://github.com/TCMAI-BJTU/Lingdan-V2) |
| **杏核 (Xinghe)** | 2026 | Xinghe-TCM | 推理 · 古籍 | [权重](https://huggingface.co/zsyjsld/Xinghe1.2-9B) · [数据](https://huggingface.co/datasets/zsyjsld/neijing-sft-v1.2) |
| **仲景 (ZhongJing)** | 2026 | 福耀科技大学 | 专家知识引导的中医大模型 ZhongJingGPT。它把领域微调和认知心… | [论文](https://doi.org/10.26599/TST.2025.9010046) · [权重](https://huggingface.co/CMLM/ZhongjingGPT1_13B) · [代码](https://github.com/pariskang/CMLM-ZhongJing) |
| **中医体质 Qwen3-8B 量化权重** | 2026 | — | 面向中医体质的 Qwen3-8B 量化权重，仓库里有 q4、q5 和 q… | [权重](https://huggingface.co/chenhaodev/tcm-constitution-qwen3-8b-gguf) |
| **TCM-Qwen3.5-9B-SFT-R2** | 2026 | Xxiao2023 (Hugging Face) | 推理 | [权重](https://huggingface.co/Xxiao2023/TCM-Qwen3.5-9B-SFT-R2) |
| **TCM-Qwen2.5-7B-SFT** | 2026 | — | 基于 Qwen2.5-7B 的中医监督微调权重，模型文件是完整的 saf… | [权重](https://huggingface.co/Xxiao2023/TCM-Qwen2.5-7B-SFT-V1) |
| **Qwen3.5-9B 中医继续预训练** | 2026 | — | Qwen3.5-9B 做完中医继续预训练后的全量权重，一个约 17.9… | [权重](https://huggingface.co/arthur789/qwen3.5-9b-tcm-cpt) |
| **MiMo-9B-TCM-Andrology-LoRA** | 2026 | johnson (Hugging Face) | 处方 | [权重](https://huggingface.co/johnson/MiMo-9B-TCM-Andrology-LoRA) · [数据](https://huggingface.co/datasets/johnson/TCM-Andrology-EMR) |
| **Fu-TCM-9B** | 2026 | fudanxai (Hugging Face account) | fudanxai账号发布的9.41B参数BF16权重，已核验8个safe… | [权重](https://huggingface.co/fudanxai/Fu-TCM-9B) · [数据](https://huggingface.co/datasets/fudanxai/Fu_TCM) |
| **Fu-TCM-27B** | 2026 | 复旦大学 | 多模态 | [论文](https://arxiv.org/abs/2610.38333) · [权重](https://huggingface.co/fudanxai/Fu-TCM-27B) · [数据](https://huggingface.co/datasets/fudanxai/Fu_TCM) |
| **白泽 (Baize-TCM-LLM)** | 2025 | 中国中医科学院中药研究所 | 中国中医科学院中药研究所基于Qwen3的中医问答模型系列（0.6B/8B… | [权重](https://huggingface.co/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model) · [数据](https://huggingface.co/datasets/DigitalIntelligenceCenter-of-ICMM/Baize-TCM-Corpus-for-Large-Language-Models-V3) |
| **扁仓 (BianCang)** | 2025 | 齐鲁工业大学 | 系列中医大模型（JBHI 正式发表）；2025.12 开源 14B 版本 | [论文](https://arxiv.org/abs/2411.11027) · [权重](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct) · [代码](https://github.com/QLU-NLP/BianCang) |
| **ViTCM-LLM** | 2025 | Tsinghua Shenzhen International Graduate School | 多模态 · RAG | [论文](https://doi.org/10.1109/bibm66473.2025.11357113) · [权重](https://huggingface.co/Mark-CHAE/ViTCM-LLM) · [代码](https://github.com/jw-chae/ViTCM_LLM) |
| **TCM-VisResolve (TCM-VR)** | 2025 | 云南民族大学 | 多模态 | [论文](https://doi.org/10.1109/BIBM66473.2025.11356679) · [权重](https://huggingface.co/dylanyang963/TCM-VR) |
| **ShizhenGPT** | 2025 | 香港中文大学(深圳)等 | 多模态 | [论文](https://arxiv.org/abs/2508.14706) · [权重](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni) · [代码](https://github.com/FreedomIntelligence/ShizhenGPT) |
| **TCMLLM / 灵丹 (Lingdan)** | 2024 | 北京交通大学 | 中医药大模型与处方推荐 | [论文](https://doi.org/10.1016/j.dcmed.2025.01.007) · [权重](https://huggingface.co/TCMLLM/Lingdan-13B-Base) · [代码](https://github.com/2020MEAI/TCMLLM) |
| **TCMChat** | 2024 | 浙江大学 | 生成式中医药大模型，经预训练+监督微调构建，配套 60 万条中药知识对话… | [论文](https://doi.org/10.1016/j.phrs.2024.107530) · [权重](https://huggingface.co/ZJUFanLab/TCMChat-600k) · [代码](https://github.com/ZJUFanLab/TCMChat) · [数据](https://huggingface.co/datasets/ZJUFanLab/TCMChat-dataset-600k) |
| **MedChatZH** | 2024 | 华东理工大学 | 基于 Baichuan-7B 的中医问诊对话模型，公开配套问诊数据与模型… | [论文](https://doi.org/10.1016/j.compbiomed.2024.108290) · [代码](https://github.com/tyang816/MedChatZH) · [权重](https://huggingface.co/tyang816/medchatzh) · [数据](https://huggingface.co/datasets/tyang816/MedChatZH) |
| **ChatTCM** | 2024 | — | HF 用户 SylvanL 开源的中医 LLM：Qwen2-7B 继续预… | [权重](https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain) |
| **神农大模型 (ShenNong-TCM-LLM)** | 2023 | 华东师范大学 | 首个中医药大规模语言模型"神农"，配套 ShenNong_TCM_Dat… | [权重](https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM) · [代码](https://github.com/michael-wzhu/ShenNong-TCM-LLM) · [数据](https://huggingface.co/datasets/michaelwzhu/ShenNong_TCM_Dataset) |

</details>

<details>
<summary>只有论文或产品、没有核验权重的（50）</summary>

<details>
<summary>2026 · 15</summary>

- [*Digital Chinese Medicine*] **青囊 (QingNangTCM)** 基于 GLM-4-9B-Chat，以 P-Tuning v2 适配中医问答与临床推理；构建 100,000 条 QnTCM_Dataset 训练语料。 [河北北方学院] [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.002)]
- [*ISCTIS 2026*] **舌面多模态融合智能诊断** 舌-面多模态特征融合+LLM驱动的中医智能诊断 [厦门理工学院] [[DOI](https://doi.org/10.1109/ISCTIS70043.2026.11572361)]
- **砭石云中医** **砭石云中医**是智慧眼基于已备案砭石多模态大模型的中医方案，用症状到方药的知识图谱支持四诊采集和辅助辨证。 [智慧眼科技] [[官网](https://www.a-eye.cn/news_list/420.html)] [[网站](https://www.a-eye.cn/news_list/356.html)]
- **岐元** **岐元**是上海中医药大学附属第七人民医院的中医垂类大模型，采用预训练、领域微调和专家强化学习，支持生成式病历和名老中医 Agent 数字孪生。 [上海中医药大学附属第七人民医院] [[新闻](https://finance.sina.com.cn/jjxw/2026-07-26/doc-inikassr0678770.shtml)]
- [*Information Fusion*] **天医 (Tianyi)** 南京中医药大学等提出 7.6B 参数中医大模型，按读书—临证—跟师多阶段训练，配套TCMEval评测与真实世界验证（Information Fusion 2026年2月） [南京中医药大学] [[正式发表](https://doi.org/10.1016/j.inffus.2025.103663)] [[论文](https://arxiv.org/abs/2505.13156)] [[新闻](https://blog.sciencenet.cn/blog-279293-1501581.html)]
- **华族本草** **华族本草**是贵州医科大学中药全国重点实验室牵头的民族药大模型，以数智岐黄和 Qwen 为底座，融合多民族医药古籍与知识图谱，覆盖成分筛选、配伍、质控和教学。 [贵州医科大学，中药功效成分发掘与利用全国重点实验室] [[官网](https://www.gmc.edu.cn/info/1059/30300.htm)] [[新闻](https://www.news.cn/tech/20260804/f973d6fa9de640328fec0194c63335a3/c.html)]
- [*JMIR Medical Informatics*] **TongueVLM** 中医舌诊多模态大模型，支持舌象描述生成与体质推理。JMIR 页被拦截，OpenAlex 记录作者单位为合肥工业大学与安徽中医药大学等 [合肥工业大学，安徽中医药大学等] [[论文](https://doi.org/10.2196/87237)] [[JMIR](https://medinform.jmir.org/2026/1/e87237)]
- [*APWeb-WAIM 2025*] **TCM-R1** 通过GRPO增强中医推理能力的大模型 [西南大学] [[论文](https://link.springer.com/chapter/10.1007/978-981-95-5640-3_21)]
- [*世界科学技术-中医药现代化*] **TCM Classic-Translator（中医古籍今译）** 用《黄帝内经》《伤寒论》等文言—白话平行语料，对 DeepSeek、Qwen、Baichuan 做 LoRA 微调并融合注释，得到 TCM Classic-Translator。BLEU-4、ROUGE-1、ROUGE-2、ROUGE-L 分别为 39.3534、55.0474、35.8099、54.6551。 [中国中医科学院中医药信息研究所，南京中医药大学人工智能与信息技术学院] [[DOI](https://doi.org/10.11842/wst.20250916005)]
- [*Digital Chinese Medicine*] **Qwen-TCM-Dia** 基于 Qwen2.5 的中医泄泻专科模型，以两阶段 LoRA 完成领域续训和思维链指令微调，连接症状、病机、治法与方药。 [首都医科大学附属北京中医医院，北京中医药大学等] [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.003)]
- [*arXiv*] **Med-Shicheng（师承）** 沿用 Tianyi 的多阶段训练思路，在 Qwen2.5-1.5B-Base 上实施续训、监督微调和 KTO，学习 5 位中医名家的经验，覆盖 7 类任务。 [南京中医药大学等] [[论文](https://arxiv.org/abs/2603.23520)] [[代码](https://github.com/NJUCM-BJUCM-TCM-AI/Med-Shicheng)]
- [*Chinese Herbal Medicines*] **HerbWise** 面向传统草药（THM）的领域大模型，服务草药现代化与标准化 [成都中医药大学] [[DOI](https://doi.org/10.1016/j.chmed.2026.02.010)]
- [*Chinese Medicine*] **GastroTCM** 中医消化内科大模型，基于Llama3-8B微调并结合RAG与智能体框架。Chinese Medicine 论文署名清华大学 TCM-X 与中日友好医院等 [清华大学，中日友好医院等] [[论文](https://link.springer.com/article/10.1186/s13020-025-01295-8)]
- [*arXiv*] **DongYuan** 中西医结合脾胃病诊断LLM框架，融合中医辨证与西医诊断推理。arXiv PDF 署名河北省中医院、中科院自动化所、中科闻歌与天津大学 [河北省中医院，中国科学院自动化研究所等] [[论文](https://arxiv.org/abs/2603.28191)]
- [*Chinese Medicine*] **DFGLM-TCM** 北京中医药大学东方医院与智谱等的中医临床系统，把通用中医知识与名医经验分模块建模后多任务协同。论文已发；代码和训练、验证数据未公开，合格研究者可向通讯作者申请。 [北京中医药大学，智谱华章] [[DOI](https://doi.org/10.1186/s13020-026-01512-y)]

</details>

<details>
<summary>2025 · 23</summary>

- **薪火中国药** **薪火中国药**是北京中医药大学牵头建设的中医药教育大模型，覆盖助学、助教、助研、助管和对外传播，并于2026年通过生成式人工智能服务备案。 [北京中医药大学，科大讯飞，中国中医药出版社] [[官网](https://www.bucm.edu.cn/xwgl/6762cbff37ae4939829bbd3efae96225.htm)] [[网站](https://www.bucm.edu.cn/bzyyw/1c0b0fe535764fcc886c87b560caa0ee.htm)] [[新闻](https://www.beijing.gov.cn/fuwu/lqfw/gggs/202604/t20260423_4605343.html)]
- [*arXiv*] **智明堂 (ZMT-M1)** 中医大模型及TCM-Eval动态可扩展评测基准 [北京航空航天大学] [[论文](https://arxiv.org/abs/2511.07148)] [[平台](https://tcmeval.bamaidical.com)]
- [*Chinese Medicine*] **悬壶 (XuanHuGPT)** 基于 ChatGLM2-6B，采用 LoRA 与 P-Tuning v2 进行中医领域参数高效微调。 [河北北方学院] [[DOI](https://doi.org/10.1186/s13020-025-01200-3)]
- **张仲景中医药大模型** **张仲景中医药大模型**由河南中医药大学与北京科技大学等联合发布，覆盖智能辨证、证素推荐、经方应用和方药分析，并接入临床辅助诊疗。 [河南中医药大学，北京科技大学] [[官网](https://hactcm.edu.cn/info/1022/211754.htm)] [[网站](https://news.ustb.edu.cn/info/1981/67772.htm)]
- **广医·岐智** **广医·岐智**是中国中医科学院广安门医院的中医医疗服务大模型，支持导诊、预问诊、病历生成和辨证方剂建议，2.0增加智能体医生，并已完成算法备案。 [中国中医科学院广安门医院] [[官网](https://www.gamyy.cn/gzb/news/big/110133.html)] [[网站](https://www.gamyy.cn/gzb/news/big/114632.html)] [[新闻](https://www.gamyy.cn/gzb/news/big/113898.html)]
- [*Expert Systems with Applications*] **岐伯 (Qibo)** 天津大学等提出的中医大模型与Qibo Benchmark，持续预训练+SFT提升辨证与问答能力 [天津大学，天津中医药大学] [[正式发表](https://doi.org/10.1016/j.eswa.2025.127672)] [[论文](https://arxiv.org/abs/2403.16056)] [[DOI](https://doi.org/10.1016/j.eswa.2025.127672)]
- **女娲 (Nüwa / TCM-Nvwa)** 一套中医大模型训练流程：持续预训练、监督微调、奖励模型和 RLAIF，底座是 Ziya-LLaMA-13B。仓库放了部分预训练、问答和奖励数据，权重没有单独放出来。 [[代码](https://github.com/synbol/TCM-Nvwa)]
- [*arXiv*] **天惠 (TianHui)** 面向12类中医场景的领域LLM（DeepSeek-R1-Distill-Qwen-14B+PT/SFT），开源代码与评测脚本。arXiv PDF 署名成都中医药大学智能医学院 [成都中医药大学] [[论文](https://arxiv.org/abs/2509.19834)] [[代码](https://github.com/JYfantast/TianHui)]
- **固生堂中医大脑** **固生堂中医大脑**把国医 AI 分身接入医院信息系统，在病情采集、病历生成、辅助辨证和开方环节给出可溯源的名医思路。 [固生堂] [[官网](https://www.gstzy.cn/news/detail/10/14076.html)] [[网站](https://www.gstzy.cn/news/detail/10/14125.html)]
- **众星·长白岐黄** **众星·长白岐黄**是长春中医药大学、吉林工商学院等联合研发的多模态中医药推理大模型，设有家庭健康助手和吉派中医医生助手两个入口。 [长春中医药大学，吉林工商学院，长春工程学院] [[官网](https://www.jlbtc.edu.cn/info/1042/93113.htm)] [[新闻](https://news.cnjiwang.com/jwyc/202512/4006547.html)]
- **伊尹中医经典大模型** **伊尹中医经典大模型**由中医在线用医典和经方经验训练，在问诊中展示辨证思路，并在嵩县基层医疗机构提供辅助诊疗。 [中医在线，中原药谷] [[新闻](https://www.cntcm.com.cn/content/202509/17/c284139.html)]
- **任度·素问** **任度·素问**是传神语联基于任度大模型和自研 moH 混合熵架构的中医模型，提供主动问诊、辨证和方剂建议，并通过信通院中医药大模型 4+ 级评估。 [传神语联] [[网站](https://www.transn.com/about_us/consult/article/1965645664716955649)]
- **中医横琴 (Hengqin-R1)** **中医横琴（Hengqin-R1）**是中医药广东省实验室的垂类推理大模型，融合精调、强化学习与知识图谱，支撑辨证、中西药联用智能体和四诊客观化。 [中医药广东省实验室（横琴实验室）] [[官网](https://www.hengqin.gov.cn/macao_zh_hans/hzqgl/dtyw/dtxx/content/post_3807664.html)] [[网站](https://www.gzucm.edu.cn/info/1621/109561.htm)]
- [*Computers in Biology and Medicine*] **TCM-KLLaMA** 知识图谱与大模型融合的中医方剂智能生成模型。PubMed 40056842 署名浙江工商大学与西湖大学医学院附属杭州市第一人民医院 [浙江工商大学，西湖大学医学院附属杭州市第一人民医院] [[DOI](https://doi.org/10.1016/j.compbiomed.2025.109887)] [[PubMed](https://pubmed.ncbi.nlm.nih.gov/40056842)]
- [*Chinese Medicine*] **TCM-DS** 基于 DeepSeek-LLM-7B，结合 LoRA 与检索增强生成（RAG），用于药食同源食疗方推荐。 [澳门科技大学] [[DOI](https://doi.org/10.1186/s13020-025-01249-0)]
- [*arXiv*] **RACE-Align** 检索增强+CoT 式 DPO 的轻量中医对齐模型（Qwen3-1.7B），探索小模型对齐路线。arXiv PDF 署名上海科技大学、河南大学与辽宁中医药大学 [上海科技大学，河南大学，辽宁中医药大学] [[arXiv](https://arxiv.org/abs/2506.02726)]
- [*IEEE ICIP 2025*] **MCM** 多智能体协同的中医多模态诊断框架（ICIP 2025） [上海计算机软件技术开发中心] [[代码](https://github.com/JerryMazeyu/MCM)] [[正式发表](https://doi.org/10.1109/icip55913.2025.11084334)]
- [*arXiv*] **Ladder-base (GRPO-TCM)** TCM-Ladder团队提出的首个GRPO强化学习对齐中医LLM。arXiv PDF 署名密苏里大学与上海中医药大学等 [密苏里大学，上海中医药大学等] [[论文](https://arxiv.org/abs/2510.17402)]
- [*arXiv*] **Hengqin-RA-v1** 类风湿关节炎中医诊疗大模型及配套数据集。这篇预印本已由 arXiv 撤回，撤回说明是作者身份和单位无法核实；当前作者栏为 Yishen Liu。 [[论文](https://arxiv.org/abs/2501.02471)]
- [*Applied Sciences*] **Gen-SynDi** 知识引导的生成式AI框架，用于辨证与疾病诊断的双向教学 [College of Korean Medicine, Wonkwang University, Iksan 54538, Republic of Korea，College of Korean Medicine, Woosuk University, Jeon-Ju 54987, Republic of Korea，Dongje Medical Co., Ltd., Daegu 42187, Republic of Korea，College of Medicine, Yeungnam University, Daegu 42415, Republic of Korea] [[DOI](https://doi.org/10.3390/app15094862)]
- [*arXiv*] **DoPI** 引导模型与专家模型协同的主动问诊系统；在论文模拟问诊评测中，DoPI-7B 的最终诊断准确率为 84.68%。 [天津大学，香港中文大学等] [[论文](https://arxiv.org/abs/2507.04877)]
- [*IEEE BIBM 2025*] **ChatGLM-FGIDs-TCM** 知识融合的ChatGLM中医临床决策支持模型，面向功能性胃肠病（FGIDs） [中国医学科学院/北京协和医学院] [[DOI](https://doi.org/10.1109/BIBM66473.2025.11356283)]
- [*arXiv*] **BenCao（指令微调本草助手）** 基于ChatGPT自然语言指令对齐的中医多模态助手，对接舌象API与知识库，部署于GPTs Store（区别于华驼/本草）。arXiv HTML 署名密苏里大学与上海中医药大学等 [密苏里大学，上海中医药大学等] [[论文](https://arxiv.org/abs/2510.17415)]

</details>

<details>
<summary>2024 · 10</summary>

- **智赋岐黄天功** **智赋岐黄天功**是智赋岐黄与哈尔滨工业大学联合研发的中医大模型，用医案和名医验方训练多种辨证体系，作为四诊仪体质辨识的算法底座并已完成算法备案。 [智赋岐黄，哈尔滨工业大学] [[官网](https://qihuang-ai.com/ai-platform/tiangong)] [[网站](https://qihuang-ai.com/about)]
- **数智本草** **数智本草**是天士力与华为云基于盘古语言大模型和盘古药物分子大模型开发的中医药双模态模型，用古籍、方剂和文献支持问答、分子计算与中药研发筛选。 [天士力，华为云] [[官网](https://www.huawei.com/cn/huaweitech/publication/202503/pioneer-developers-of-huaweicloud)] [[网站](https://tjdsj.tjcac.gov.cn/tjsg/hyzx/202405/t20240523_6632807.html)] [[新闻](https://www.news.cn/politics/20240509/be28f085474b45fd9d6829766195568d/c.html)]
- **数智岐黄** **数智岐黄**由华东师范大学联合上海中医药大学等研发，1.0提供中医药问答、健康咨询和知识图谱交互，2.0升级为覆盖中西药数据的多模态大模型。 [华东师范大学，上海中医药大学，临港实验室] [[官网](https://www.ecnu.edu.cn/info/1426/65503.htm)] [[网站](https://www.shanghai.gov.cn/nw4411/20240120/1a19dcf117f7430b971db72e53ed4d9b.html)] [[新闻](https://hub.baai.ac.cn/view/41476)]
- **天河·灵枢** **天河·灵枢**由国家超算天津中心联合天津中医药大学等研发，1.0面向针灸并配三维穴位数字人，2.0把覆盖范围扩到20余个临床学科。 [国家超级计算天津中心，天津中医药大学，现代中医药海河实验室] [[官网](https://www.nscc-tj.cn/xwxq.php?id=628)] [[网站](https://www.tjutcm.edu.cn/info/1047/2084.htm)] [[新闻](https://www.tjlgbj.gov.cn/tjlgb/system/2025/08/09/030003838.shtml)]
- **大数中医 (BigDataTCM)** 河南工业大学复杂性科学研究院与阿帕斯联合研发的中医垂直领域大模型（34B），提供医疗问答、诊断支持与中医知识服务 [河南工业大学] [[代码](https://github.com/HAUT-CS/BigDataTCM)]
- **大医金匮** **大医金匮**是中科闻歌与中国中医科学院联合打造的中医大模型，学习典籍与临床医案，用于辨证推理、治疗方案生成和四诊健康管理。 [中科闻歌，中国中医科学院] [[网站](https://tcm.wenge.com/)]
- [*AAAI*] **仲景（CMtMedQA 线，Yang et al.）** 与 Kang 系 ZhongJingGPT 同名不同源的中医大模型：Ziya-LLaMA-13B 全流程 CPT+SFT+RLHF，基于约 7 万条真实多轮医患对话 CMtMedQA（AAAI 2024；注意与 Tsinghua Sci Technol 的 ZhongJingGPT 无作者与工件交集） [华东师范大学等] [[论文](https://doi.org/10.1609/aaai.v38i17.29907)] [[arXiv](https://arxiv.org/abs/2308.03549)]
- **仲思** **仲思**是招联消费金融联合中山大学、广州中医药大学深圳医院发布的中医垂直大模型，覆盖知识问答、问诊病历生成和方剂推荐，并在深圳社康场景使用。 [招联消费金融，中山大学，广州中医药大学深圳医院] [[新闻](https://www.stcn.com/article/detail/1454029.html)]
- [*Computer Methods and Programs in Biomedicine Update*] **TCM-GPT** 面向中医领域自适应的高效预训练大模型。期刊元数据署名北京邮电大学与伦敦大学学院 [北京邮电大学，伦敦大学学院] [[DOI](https://doi.org/10.1016/j.cmpbup.2024.100158)] [[论文](https://arxiv.org/abs/2311.01786)]
- [*Scientific Reports*] **CPMI-ChatGLM** 中成药指令数据的 ChatGLM 参数高效微调模型。OpenAlex/期刊单位为安徽中医药大学与中国中医科学院安徽中医药计算机应用研究所 [安徽中医药大学，中国中医科学院安徽中医药计算机应用研究所] [[DOI](https://doi.org/10.1038/s41598-024-56874-w)]

</details>

<details>
<summary>2023 · 2</summary>

- **黄帝 (HuangDi)** 基于 Ziya-LLaMA-13B 的中医古籍知识问答大模型，预训练融合 22 本"十三五"中医教材与中医网站语料，古籍指令数据 SFT（图书馆论坛 2024 报道） [南京大学, 郑州大学] [[代码](https://github.com/Zlasejd/HuangDI)]
- **岐黄问道** **岐黄问道**是南京大经中医发布的中医垂直大模型，基于千万级知识图谱和临床数据，面向医疗机构做辨证、处方和养生建议。 [南京大经中医药信息技术有限公司] [[新闻](https://js.cnr.cn/rdzt/qnjs/qnjsgdxw/20230801/t20230801_526358407.shtml)]

</details>


</details>

<details>
<summary>通用中文医疗模型，常当底座或对照（30）</summary>

<details>
<summary>2026 · 1</summary>

- [*arXiv*] **百川-M3 (Baichuan-M3)** 百川第三代开源医疗推理模型（235B，底座Qwen3），用SPAR分段RL与事实感知RL做主动问诊和抑幻觉；HealthBench与SCAN-bench开源前列 [百川智能] [[论文](https://arxiv.org/abs/2602.06570)] [[代码](https://github.com/baichuan-inc/Baichuan-M3-235B)] [[模型](https://huggingface.co/baichuan-inc/Baichuan-M3-235B)]

</details>

<details>
<summary>2025 · 4</summary>

- [*arXiv*] **百川-M2 (Baichuan-M2)** 百川第二代开源医疗推理模型（32B，底座Qwen2.5-32B），用大规模验证器与多阶段RL做临床对话对齐，HealthBench开源前列 [百川智能] [[论文](https://arxiv.org/abs/2509.02208)] [[代码](https://github.com/baichuan-inc/Baichuan-M2-32B)] [[模型](https://huggingface.co/baichuan-inc/Baichuan-M2-32B)]
- [*arXiv*] **百川-M1 (Baichuan-M1)** 百川智能从零训练的开源医疗大模型（14B），约20万亿token医疗+通用数据，覆盖20+科室；常被后续中医微调当作底座 [百川智能] [[论文](https://arxiv.org/abs/2502.12671)] [[代码](https://github.com/baichuan-inc/Baichuan-M1-14B)] [[模型](https://huggingface.co/baichuan-inc/Baichuan-M1-14B-Instruct)] [[Base](https://huggingface.co/baichuan-inc/Baichuan-M1-14B-Base)]
- **太一2 (Taiyi-2)** 太一二代开源生物医学模型，底座从Qwen-7B换成GLM4-9B，重做数据过滤与任务指令。官方模型卡仍引用太一1的JAMIA论文（10.1093/jamia/ocae037），没有单独的太一2论文 [大连理工大学] [[模型](https://huggingface.co/DUTIR-BioNLP/Taiyi2-chat)] [[代码](https://github.com/DUTIR-BioNLP/Taiyi-LLM)]
- [*arXiv*] **卫宁WiNGPT3** 卫宁第三代医疗推理模型（32B，底座Qwen2.5），多阶段SFT+RL与长思维链，对接WiNEX医院流程；技术报告和代码已公开，权重未核验可下载 [卫宁健康] [[论文](https://arxiv.org/abs/2505.17387)] [[代码](https://github.com/winninghealth/WiNGPT3)]

</details>

<details>
<summary>2024 · 5</summary>

- [*arXiv*] **明医 (MING)** 中文医疗问诊大模型 MING，以稀疏 LoRA 混合专家（MING-MoE）增强医疗多任务学习能力（arXiv 2024） [上海交通大学] [[论文](https://arxiv.org/abs/2404.09027)] [[相关 MedCare](https://aclanthology.org/2024.findings-emnlp.619/)] [[代码](https://github.com/MediaBrain-SJTU/MING)]
- [*JAMIA*] **太一 (Taiyi)** 大连理工DUTIR的中英双语生物医学大模型，底座Qwen-7B，覆盖问答、医患对话、报告生成与信息抽取等 [大连理工大学] [[DOI](https://doi.org/10.1093/jamia/ocae037)] [[代码](https://github.com/DUTIR-BioNLP/Taiyi-LLM)] [[模型](https://huggingface.co/DUTIR-BioNLP/Taiyi-LLM)]
- [*arXiv*] **华佗GPT-o1 (HuatuoGPT-o1)** 华佗系列医疗复杂推理模型，用可验证医题和医学验证器做搜索微调与强化学习。仓库给出 7B、8B 和 70B。 [香港中文大学(深圳)，深圳市大数据研究院] [[论文](https://arxiv.org/abs/2412.18925)] [[代码](https://github.com/FreedomIntelligence/HuatuoGPT-o1)] [[模型](https://huggingface.co/FreedomIntelligence/HuatuoGPT-o1-7B)]
- [*arXiv*] **华佗GPT-Vision (HuatuoGPT-Vision)** 华佗系列医学多模态模型，大规模注入医学视觉知识，常作中文医学影像/多模态对照 [香港中文大学(深圳)，深圳市大数据研究院] [[论文](https://arxiv.org/abs/2406.19280)] [[代码](https://github.com/FreedomIntelligence/HuatuoGPT-Vision)] [[模型](https://huggingface.co/FreedomIntelligence/HuatuoGPT-Vision-7B-Qwen2.5VL)]
- [*arXiv*] **Apollo** 中大深圳FreedomIntelligence的多语种医疗LLM（含中文），配套ApolloCorpus与XMedBench [香港中文大学(深圳)，深圳市大数据研究院] [[论文](https://arxiv.org/abs/2403.03640)] [[代码](https://github.com/FreedomIntelligence/Apollo)] [[模型](https://huggingface.co/FreedomIntelligence/Apollo-7B)]

</details>

<details>
<summary>2023 · 20</summary>

- [*arXiv*] **麒麟-Med (Qilin-Med)** 多阶段知识注入的中文医疗LLM（CPT+SFT+DPO，底座Baichuan-7B），发布约3GB ChiMed语料，可再加RAG。arXiv PDF 署名北京大学、港科大（广州）等 [北京大学，香港科技大学（广州）等] [[论文](https://arxiv.org/abs/2310.09089)] [[代码](https://github.com/williamliujl/Qilin-Med)] [[数据集](https://huggingface.co/datasets/williamliu/ChiMed)]
- [*arXiv*] **本草[原名：华驼(HuaTuo)]** 哈工大社会计算与信息检索研究中心做的本草，原来叫华驼。它用中文医学知识做指令微调，论文是 2023 年的 HuaTuo。同组后来又写了知识微调的工作，2025 年 2 月登在 ACM TKDD。 [哈尔滨工业大学] [[论文](https://arxiv.org/abs/2304.06975)] [[相关论文](https://arxiv.org/abs/2309.04175)] [[期刊](https://doi.org/10.1145/3686807)] [[代码](https://github.com/SCIR-HI/Huatuo-Llama-Med-Chinese)]
- **扁鹊-2 (BianQue-2)** 扁鹊二代开源医疗问诊模型，强化多轮追问；CMB 等中文医疗评测里的常见对照 [华南理工大学，广东省数字孪生人重点实验室] [[代码](https://github.com/scutcyr/BianQue)] [[模型](https://huggingface.co/scutcyr/BianQue-2)]
- [*arXiv*] **扁鹊 (BianQue)** 中文领域生活空间主动健康大模型 [华南理工大学，广东省数字孪生人重点实验室] [[代码](https://github.com/scutcyr/BianQue)] [[论文](https://arxiv.org/abs/2310.15896)]
- **孙思邈 (Sunsimiao)** 孙思邈中文医疗大模型，Sunsimiao-7B 基于 Qwen2-7B 以高质量医疗数据微调，在 CMB-Exam 达 30B 量级 SOTA [华东理工大学] [[代码](https://github.com/X-D-Lab/Sunsimiao)]
- **启真医学大模型 (QiZhenGPT)** 中文医疗场景、药品知识问答、优化疾病、手术、检验等 [浙江大学] [[代码](https://github.com/CMKRG/QiZhenGPT)]
- **卫宁WiNGPT2** 卫宁健康开源医疗大模型，底座Qwen，覆盖医学问答、病历理解和多轮问诊，7B/14B可下载 [卫宁健康] [[模型](https://huggingface.co/winninghealth/WiNGPT2-14B-Chat)] [[7B](https://huggingface.co/winninghealth/WiNGPT2-7B-Chat)]
- [*arXiv*] **华佗GPT-II (HuatuoGPT-II)** 中大深圳华佗系列二代，单阶段领域适配；7B/13B以Baichuan2为底座，是中文医疗评测里最常见的开源对照之一 [香港中文大学(深圳)，深圳市大数据研究院] [[论文](https://arxiv.org/abs/2311.09774)] [[代码](https://github.com/FreedomIntelligence/HuatuoGPT-II)] [[模型](https://huggingface.co/FreedomIntelligence/HuatuoGPT2-7B)]
- [*EMNLP findings*] **华佗GPT** 中文医学语料训练的大型语言模型 [香港中文大学(深圳)，深圳市大数据研究院] [[DOI](https://doi.org/10.18653/v1/2023.findings-emnlp.725)] [[论文](https://aclanthology.org/2023.findings-emnlp.725/)] [[代码](https://github.com/FreedomIntelligence/HuatuoGPT)]
- [*arXiv*] **SoulChat** 华南理工数字孪生人实验室的心理健康对话大模型，与扁鹊同系列，常作中文医疗/健康对话对照 [华南理工大学，广东省数字孪生人重点实验室] [[论文](https://arxiv.org/abs/2311.00273)] [[代码](https://github.com/scutcyr/SoulChat)] [[模型](https://huggingface.co/scutcyr/SoulChat)]
- **PULSE** 上海人工智能实验室 OpenMEDLab 的中文医疗大模型。PULSE-7b 基于 bloomz-7b1-mt，PULSE-20b 基于 InternLM-20B，覆盖医考、报告解读、病历结构化与模拟诊疗。 [上海人工智能实验室] [[代码](https://github.com/openmedlab/PULSE)] [[模型](https://huggingface.co/OpenMEDLab/PULSE-7bv5)]
- **MedicalGPT** 开源中文医疗LLM训练框架（预训练/SFT/RLHF/DPO），也被大量中医微调实验当作基线实现 [[代码](https://github.com/shibing624/MedicalGPT)]
- [*arXiv*] **IvyGPT** 基于 LLaMA 的中文医疗问答模型，用高质量医患 QA 与 RLHF 微调，CMB 论文对照列表中的开源基线。arXiv PDF 署名澳门理工大学 [澳门理工大学] [[论文](https://arxiv.org/abs/2307.10512)] [[代码](https://github.com/Ivy0529/IvyGPT)]
- [*arXiv*] **DoctorGLM** 基于ChatGLM-6B的早期开源中文问诊模型，用多科室医患数据做LoRA/P-Tuning，常出现在2023年中文医疗对照表。arXiv HTML 署名上海科技大学、联影智能、复旦大学华山医院等 [上海科技大学，联影智能等] [[论文](https://arxiv.org/abs/2304.01097)] [[代码](https://github.com/xionghonglin/DoctorGLM)]
- [*arXiv*] **DISC-MedLLM** 复旦DISC实验室的医疗对话大模型，底座Baichuan-13B，配套DISC-Med-SFT；知识图谱+真实问诊重构 [复旦大学] [[论文](https://arxiv.org/abs/2308.14346)] [[代码](https://github.com/FudanDISC/DISC-MedLLM)] [[模型](https://huggingface.co/Flmc/DISC-MedLLM)] [[数据集](https://huggingface.co/datasets/Flmc/DISC-Med-SFT)]
- [*arXiv*] **ClinicalGPT** 北邮等用病历、知识、医考和多轮问诊微调的临床向中文医疗模型（BLOOM-7B），CMB等对照表常见；HF有medicalai快照 [北京邮电大学] [[论文](https://arxiv.org/abs/2306.09968)] [[模型](https://huggingface.co/medicalai/ClinicalGPT-base-zh)]
- [*arXiv*] **ChiMed-GPT** 中科大等在Ziya-v2上做继续预训练+SFT+RLHF的中文医疗大模型，覆盖抽取、问答与多轮对话 [中国科学技术大学] [[论文](https://arxiv.org/abs/2311.06025)] [[代码](https://github.com/synlp/ChiMed-GPT)] [[模型](https://huggingface.co/SYNLP/ChiMed-GPT-1.0)]
- **ChatMed** ChatMed 系列中文医疗大模型，含基于 50 万+ 在线问诊数据训练的 ChatMed-Consult。GitHub README 引用 Wei Zhu / Xiaoling Wang，无独立期刊论文 [华东师范大学] [[代码](https://github.com/michael-wzhu/ChatMed)] [[模型](https://huggingface.co/michaelwzhu/ChatMed-Consult)]
- **ChatGLM-Med** 哈工大SCIR用中文医学知识图谱指令微调的ChatGLM-6B，与本草/华驼同源数据，CMB常用对照 [哈尔滨工业大学] [[代码](https://github.com/SCIR-HI/Med-ChatGLM)]
- **CareGPT** 开源中文医疗LLM全流程训练框架（预训练到DPO）与配套权重，常被复现中文医疗微调。README 写明由澳门理工大学应用科学学院完成 [澳门理工大学] [[代码](https://github.com/WangRongsheng/CareGPT)]

</details>


</details>

<details>
<summary>闭源中文医疗产品，无核验权重（4）</summary>

- **讯飞星火医疗** 科大讯飞的星火医疗大模型X1，2025年3月发布，用在讯飞晓医上。报道里的测试数据来自讯飞晓医、智医助理等真实场景。 [科大讯飞] [[官网](https://www.xunfeihealthcare.com/)] [[新闻](https://www.cn-healthcare.com/article/20250303/wap-content-585822.html)]
- **蚂蚁阿福 / 蚂蚁医疗大模型** 2024年7月5日，支付宝在世界人工智能大会发布多模态医疗大模型，基座是百灵，能看药品、报告和影像。2025年12月15日，健康应用AQ升级为蚂蚁阿福，可以拍皮肤、检查报告和药盒来问。 [蚂蚁集团] [[官网](https://www.antafu.com/)] [[新闻稿](https://www.antgroup.com/news-media/press-releases/1720166400000)] [[新闻](https://www.antgroup.com/news-media/press-releases/1765785600000)]
- **腾讯混元医疗** 腾讯健康基于混元的闭源医疗大模型，覆盖问答、导诊、病历与影像；天衍实验室发布，无公开权重 [腾讯] [[官网](https://healthcare.tencent.com/)] [[新闻](https://healthcare.tencent.com/news/1603)]
- [*Sci China Life Sci*] **盘古药物分子大模型 (PanGu Drug Model)** 华为云与中科院上海药物所的闭源分子预训练模型（约17亿小分子），做属性预测/生成/优化；数智本草曾以其为底座之一 [华为云，中国科学院上海药物研究所] [[DOI](https://doi.org/10.1007/s11427-022-2239-y)] [[官网](https://www.huaweicloud.com/cases/pgyw.html)]

</details>

<details>
<summary>日韩汉方 / 韩医模型与系统（1）</summary>

- **KAMPO LLM** 官网仍开：VARYTEX 与日本东洋医学会合作的闭源汉方 API；页面写明 471 题评测 Pro 97.4%、Flash 92.1%，无公开权重 [VARYTEX，日本东洋医学会] [[官网](https://kampollm.varytex.co.jp/)]

</details>

<details>
<summary>Hugging Face 上的其他尺寸和 GGUF（11）</summary>

- **杏核内经推理模型** [[模型](https://huggingface.co/zsyjsld/Xinghe1.2-9B)] [[GGUF](https://huggingface.co/zsyjsld/Xinghe1.2-9B-GGUF)]
- **仲景** [[ZhongjingGPT1_13B](https://huggingface.co/CMLM/ZhongjingGPT1_13B)] [[ZhongJing-2-1.8B](https://huggingface.co/CMLL/ZhongJing-2-1_8b)]
- **白泽中医大模型** [[模型](https://huggingface.co/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model)] [[8B-16bit](https://huggingface.co/DigitalIntelligenceCenter-of-ICMM/Baize-Traditional-Chinese-Medicine-Large-Language-Model-V3-16bit)]
- **ShizhenGPT 系列** [[7B-LLM](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-LLM)] [[7B-VL](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-VL)] [[7B-Omni](https://huggingface.co/FreedomIntelligence/ShizhenGPT-7B-Omni)] [[32B-LLM](https://huggingface.co/FreedomIntelligence/ShizhenGPT-32B-LLM)] [[32B-VL](https://huggingface.co/FreedomIntelligence/ShizhenGPT-32B-VL)]
- **扁仓 (BianCang) 系列** [[Qwen2.5-7B-Instruct](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-7B-Instruct)] [[Qwen2.5-14B-Instruct](https://huggingface.co/QLU-NLP/BianCang-Qwen2.5-14B-Instruct)]
- **MedChatZH** [[medchatzh](https://huggingface.co/tyang816/medchatzh)]
- **TCMChat** [[TCMChat-600k](https://huggingface.co/ZJUFanLab/TCMChat-600k)]
- **灵丹** [[Lingdan-13B-Base](https://huggingface.co/TCMLLM/Lingdan-13B-Base)] [[Lingdan-13B-PR](https://huggingface.co/TCMLLM/Lingdan-13B-PR)]
- **ChatTCM全参SFT版** [[模型](https://huggingface.co/SylvanL/ChatTCM-7B-SFT)]
- **ChatTCM** [[ChatTCM-7B-Pretrain](https://huggingface.co/SylvanL/ChatTCM-7B-Pretrain)]
- **神农** [[ShenNong-TCM-LLM](https://huggingface.co/michaelwzhu/ShenNong-TCM-LLM)]

</details>

## 新闻

<details>
<summary>104 条，最近有：上海市卫生健康委员会、上海市中医药管理局 · 云南省人民政府办公厅印发《云南省中医药振 · 岐元</summary>

<details>
<summary>2026 · 68</summary>

- [2026.11.19] 上海市卫生健康委员会、上海市中医药管理局印发《上海市中医药高质量发展实施方案（2026—2030年）》（沪卫中发〔2026〕13号，成文2026年11月16日，上海市卫生健康委员会官网中医药工作栏目发布日期2026年11月19日）。方案依据国家《中医药振兴发展“十五五”规划》和《上海市国民经济和社会发展第十五个五年规划纲要》，经市卫生健康委第97次委务会审议通过，部署完善服务体系、全生命周期服务、中西医结合、人才队伍、传承创新、产业、文化、开放发展、数智化赋能与标准化、领域改革等10个方面30项任务。到2030年的目标包括：区属公立中医类医院全市覆盖率达100%；公立中医医院中医类别执业（助理）医师比例达60%、设置老年病科比例达90%、提供儿科服务比例达100%；社区卫生服务中心第一执业点中医类别执业（助理）医师比例达20%，能提供6类15项以上中医适宜技术的比例达80%；65岁以上老年人中医药健康管理率达80%，0—36个月儿童中医药健康管理率达90%；公立中医医院电子病历系统应用水平达到4级以上的比例达95%、三级公立中医医院达到5级以上的比例达50%；居民中医药健康文化素养水平达45%左右；新增牵头发布的国际标准不低于5项。数智化部分提出打造“数智中医药”，构建开放标准语料库，深化上海中药云平台，并开展中医药人工智能大模型研发与应用。本次打开了上海市卫生健康委员会官方通知全文页，并打开了同站2026年11月24日发布的政策解读页。这是上海市“十五五”中医药实施方案，不是单项产品发布。 [[上海市卫生健康委员会](https://wsjkw.sh.gov.cn/zyygz2/20261119/5ddfb74bd99345c5a97619b324230e35.html)] [[政策解读](https://wsjkw.sh.gov.cn/zyygz2/20261124/b3aae808c20f46a19d6372a449948dde.html)]
- [2026.11.11] 云南省人民政府办公厅印发《云南省中医药振兴发展“十五五”规划》（云政办发〔2026〕46号，成文2026年11月5日，云南省人民政府门户网站2026年11月11日公布）。规划提出到2030年中医药振兴发展取得新成效，实现人人享有中医药服务；部署建强服务体系、全生命周期服务供给、中西医协同、人才队伍、传承创新、产业和健康服务、文化繁荣、开放发展，以及加速中医药数智化赋能与标准化建设。数智化部分明确推进各级中医医疗机构规范接入省级全民健康信息平台，促进中医药高质量数据集建设和数据安全合规流通利用；探索“中医药+人工智能”，推动中医智能辅助诊疗等技术应用，加快智慧中医医院、中医互联网医院建设，并支持引进针灸、推拿机器人、智能煎制装备等数智化装备。规划还专节部署提升藏、傣、彝等少数民族医药服务能力。本次打开了云南省人民政府门户网站官方全文页。这是省级规划部署，不是已经上线的模型发布。 [[云南省人民政府](https://www.yn.gov.cn/zwgk/zcwj/yzfb/202611/t20261111_4383311.html)]
- [2026.11.09] 中新网11月9日报道，第九届进博会上，上海市第七人民医院完成进博会首秀，中医药人工智能中心主任赵铎路演**岐元**中医垂类大模型，现场还有AI面诊智能体与中医教学机器人「小柒」。岐元已于2026年7月发布，本报道写的是进博会展示与对口支援医院应用，不是首次发布。 [[链接](https://www.chinanews.com.cn/jk/2026/11-09/10729099.shtml)]
- [2026.11.09] 新华社北京11月9日电，国务院总理李强签署国务院令（国令第850号），公布《中医药传统知识保护条例》。条例共32条，明确建立保护数据库与保护名录等制度，自2027年1月1日起施行。 [[新华社](https://www.news.cn/politics/leaders/20261109/115bf875b154445787539419282ce542/c.html)] [[中国政府网](https://www.gov.cn/yaowen/liebiao/202611/content_7085599.htm)] [[条例全文](https://www.gov.cn/zhengce/zhengceku/202611/content_7085592.htm)]
- [2026.11.05] 新京报11月5日转载称，第五届问止中医临床学术会议于11月1日在深圳举行，会上正式发布中医评测基准**TCMQA**。报道称该基准含38279道执业医考选择题，并公布101位执业中医师作答形成的参考基线；题库与评测材料已在Hugging Face开源。本站已收录该基准条目，此为发布新闻。报道未把答题成绩等同于临床辨证能力。 [[链接](https://www.bjnews.com.cn/detail/1793844088129508.html)]
- [2026.11.05] 人民网11月5日采访国家中医药管理局监测统计中心主任厉将斌，介绍中医药独立赛道、名医智能体及高质量数据集建设。为新闻与建设线索，未附数据下载。 [[链接](https://finance.people.com.cn/n1/2026/1105/c1004-40828489.html)]
- [2026.11.05] 中科闻歌11月5日称，其国科智医团队联合中国中医科学院构建的中医大模型辨证论治评测基准**TCM-BEST4SDT**，论文在Nature Portfolio旗下《Scientific Data》在线发表。报道称基准含600条样本、27个评测维度，数据集和评测代码已公开。本站已收录该基准条目，此为发表新闻。 [[链接](https://www.wenge.com/site/a/202611/05/1070720261105103301.html)]
- [2026.11.04] 北京市卫健委11月4日刊载：10月30日会议讨论中医知识结构化、可信AI数据集、西苑医院中医药肿瘤科学数据系统等；报道未发布开放数据包。 [[链接](https://wjw.beijing.gov.cn/xwzx_20031/jcdt/202611/t20261104_4931739.html)]
- [2026.11.03] 山西省卫生健康委员会、山西省发展和改革委员会印发《山西省“十五五”中医药发展规划》（晋卫中医药科技发〔2026〕3号，成文2026年10月28日，省卫生健康委官网2026年11月3日公布）。规划提出到2030年中医药强省建设取得决定性进展，以科技创新、数智化转型、中西医协同为牵引，做大做强中医药“晋”字品牌；并专章部署加速中医药数智化赋能，包括建立中医药行业可信数据空间和人工智能高质量数据集，支持多模态大模型等技术用于中医辅助决策、病历质控、名老中医经验传承和中药新药研发，加强智慧中医医院建设并推动基层应用中医智能辅助诊疗。本次打开了山西省卫生健康委官方全文页。这是省级规划部署，不是已经上线的模型发布。 [[山西省卫生健康委](https://wjw.shanxi.gov.cn/tzgg/zcwj/202611/t20261103_10251747.shtml)]
- [2026.11.03] 山东省人民政府印发《山东省中医药发展“十五五”规划》（鲁政发〔2026〕23号，成文2026年10月23日，2026年11月3日公布）。规划提出实施齐鲁中医药振兴发展“六名四化”战略，推动中医药现代化、产业化、智慧化、生活化，到2030年实现人人享有中医药服务；重点任务包括中医药古籍数字化、数字智能应用人才培养，以及推动中医药数智化赋能。这是省级规划部署，不是已经上线的模型发布。 [[山东省人民政府](http://www.shandong.gov.cn/art/2026/11/3/art_267492_89889.html)] [[政策解读](http://www.shandong.gov.cn/art/2026/11/3/art_306404_21741.html)]
- [2026.11.03] 数字中国建设峰会网站11月3日转载经济日报报道，介绍《人工智能赋能全球传统医学发展报告（2026）》及杭州市中医院“中医小安”机器人。报道涵盖AI传统医学整体，不等同于TCM大语言模型统计。 [[链接](https://www.digitalchina.gov.cn/2026/szzg/xyzx/202611/t20261103_5389002.htm)]
- [2026.11.02] 广东省卫生健康委、广东省中医药局、广东省发展改革委印发《广东省中医药发展“十五五”规划》（粤卫〔2026〕4号，成文2026年10月8日，2026年11月2日在省中医药局官网公布）。规划以中西医协同、数智化转型、粤港澳联动为引领，提出到2030年全面实现人人享有优质中医药服务；并专章部署加速中医药数智化赋能，支持中医药大模型和智能体开发应用，探索建设高质量数据集、数字化平台与知识图谱，加强智慧中医医院建设。这是省级规划部署，不是已经上线的模型发布。 [[广东省中医药局](http://szyyj.gd.gov.cn/zwgk/gsgg/content/post_4974266.html)]
- [2026.10.28] 国家中医药管理局综合司印发《2026—2028年周期全国基层中医药工作示范市（县）建设标准》（国中医药综医政函〔2026〕225号，成文2026年10月10日，国家中医药管理局官网页面标注时间为2026年10月28日）。通知依据《全国基层中医药工作示范市（县）管理办法》（国中医药医政发〔2026〕5号），规范开展本周期示范市（县）创建工作，并废止2022年印发的示范市、示范县建设标准（国中医药医政发〔2022〕1号）。本次检索打开了湖南省人民政府门户网站转载的国家中医药管理局网站全文（该站标注发文日期2026-10-10、发布时间2026-11-03、信息来源为国家中医药管理局网站），并核到官网原链为http://www.natcm.gov.cn/yizhengsi/gongzuodongtai/2026-10-28/39041.html；本轮直接访问该官网地址返回超时或HTTP 500。这是示范创建标准，不是单项产品发布。 [[国家中医药管理局](http://www.natcm.gov.cn/yizhengsi/gongzuodongtai/2026-10-28/39041.html)] [[湖南省人民政府转载](http://www.hunan.gov.cn/zqt/zcsd/202611/t20261103_34093522.html)]
- [2026.10.28] 国家中医药管理局综合司公布2026—2028年周期全国基层中医药工作示范市（县）创建单位名单（国中医药综医政函〔2026〕238号，成文2026年10月23日）。通知要求各创建单位对照本周期建设标准推进创建任务，省级中医药主管部门加强管理指导与日常监测，国家中医药管理局将在周期结束前组织评估验收，合格的正式命名。本次打开了湖南省人民政府门户网站转载的国家中医药管理局网站全文（该站标注发文日期2026-10-23、发布时间2026-11-03、信息来源为国家中医药管理局网站）；官网原链为http://www.natcm.gov.cn/yizhengsi/gongzuodongtai/2026-10-28/39040.html，本轮直接访问该官网地址返回超时或HTTP 500。这是创建单位名单公布，不是单项产品发布。 [[国家中医药管理局](http://www.natcm.gov.cn/yizhengsi/gongzuodongtai/2026-10-28/39040.html)] [[湖南省人民政府转载](http://www.hunan.gov.cn/zqt/zcsd/202611/t20261103_34093548.html)]
- [2026.10.28] 国家中医药局综合司、国家卫生健康委办公厅印发《关于推进基层中医适宜技术推广应用的通知》（国中医药综医政发〔2026〕8号，成文2026年10月14日，国家中医药管理局官网及中国政府网转载新华社稿2026年10月28日发布）。通知要求建设国家、省、市、县推广网络，到2030年县级推广中心基本全覆盖，优先推广6类15项以上中医适宜技术；并专章部署推广工作数智化支撑，探索应用人工智能辅助教学、辅助诊疗和质控分析工具。这是基层适宜技术推广政策，不是单项产品发布。 [[国家中医药管理局](http://www.natcm.gov.cn/yizhengsi/gongzuodongtai/2026-10-28/39042.html)] [[中国政府网](https://www.gov.cn/lianbo/202610/content_7084413.htm)]
- [2026.10.27] 凤凰网财经10月31日报道，天纪易岐称其端侧模型**易岐中医AI**已于10月27日完成调试并上线，可在完全断网的本地终端推理，面向体质辨识、健康评估等场景。此为公司发布稿转载，本页未独立核验其临床效果或部署范围。该模型与古籍数据库ETCM不是同一事物。 [[链接](https://news.10jqka.com.cn/20261031/c681322899.shtml)]
- [2026.10.26] 福建省卫生健康委员会、福建省中医药管理局等十三部门印发《福建省提升中药质量促进中医药产业高质量发展的若干措施》（闽卫规〔2026〕4号，成文2026年10月15日，省卫生健康委官网2026年10月26日公布，有效期至2030年12月31日）。措施落实国办发〔2025〕11号，部署闽产道地药材保护、规范化种植、产业集群和中药工业升级等，并明确引导中药企业加快智能化改造、梯度建设智能工厂，以及建设信息化追溯系统。本次打开了省政府卫生健康委官方页面和主动公开PDF。这是省级产业质量政策，不是单项产品发布。 [[福建省卫生健康委](https://wjw.fujian.gov.cn/xxgk/fgwj/zxwj/202610/t20261026_7240705.htm)] [[官方PDF](https://wjw.fujian.gov.cn/xxgk/fgwj/zxwj/202610/P020261026658500638498.pdf)]
- [2026.10.24] 广安门医院10月24日报道，10月17日至18日的2026世界传统医药大会上，**广医·岐智**展示院内部署与病历生成，杭州市中医院具身智能机器人**中医小安**演示舌面象和脉象采集，中科云诊则展示**妙悟岐黄**辅助诊疗与可追溯辨证。报道中的分诊人次、书写时长和辨证一致率来自参展方介绍，不宜直接当成评测结论。 [[链接](https://www.gamyy.cn/gzb/news/trends/118061.html)]
- [2026.10.22] 湖北省卫生健康委员会官网2026年10月22日发布政策解读称，经省人民政府同意后，省卫生健康委、省发展改革委、省中医药管理局于2026年9月19日联合印发《湖北省中医药发展“十五五”规划》。解读明确规划提出到2030年实现人人享有中医药服务，并部署数智赋能与标准化等重点任务，包括持续推进智慧医院建设、深化数据资源开发利用和推进中医药人工智能建设。本次打开了湖北省卫生健康委的官方解读页；官网列出的规划正文链接在本次核验中返回404，故不以正文页作为依据。这是省级规划部署，不是已经上线的模型发布。 [[政策解读](https://wjw.hubei.gov.cn/zfxxgk/zc/zcjd_1/202610/t20261022_6037633.shtml)]
- [2026.10.21] 智通财经10月21日报道，医渡科技在2026世界传统医药大会成果发布环节推出中医循证智能体**小黄岐**，面向古籍与指南检索、辅助辨证、方剂查询和中医术语中英互译，并称回答可追溯证据来源。报道中的知识条目数量与医院落地范围来自企业介绍，本页未独立核验。 [[链接](https://www.zhitongcaijing.com/content/detail/1509924.html)]
- [2026.10.20] 川观新闻10月20日报道，《四川省中医药发展“十五五”规划》印发，提出支持中医药数智创新平台建设，开发名中医智能化诊疗等大模型，开展基层中医智能辅助诊疗试点，并建设高质量数据集与数智中医药协同创新中心。这是规划部署，不是已经上线的模型发布。 [[链接](https://cbgc.scol.com.cn/news/8074897)]
- [2026.10.18] 北京市科技信息门户转载《北京日报》报道，10月18日在2026世界传统医药大会“北京成果”专场，北京数智中医产业发展研究院发布智能体“数小禾”，基于本地算力和自主知识产权知识库，提供中英文中医智能服务。 [[链接](https://www.ncsti.gov.cn/kjdt/xwjj/202610/t20261027_259363.html)]
- [2026.10.18] 凤凰网科技10月19日转载称，传神素问与名医在线于10月18日在2026世界传统医药大会联合发布**范吉平数字孪生**，以传神素问中医大模型为底座，整理医案与诊疗资料后用于问诊、辨证和处方建议。这是名医数字孪生的单例发布，报道未给出可独立核验的临床对照结果。 [[链接](https://tech.ifeng.com/c/8xLt1uquwDi)]
- [2026.10.16] 中国中医药报10月16日报道汉派中医骨伤诊疗数据集在湖北数据流通平台交易，涉及16.8万条结构化诊疗数据、3600个经验方与辨证论治思维链；属于许可流通案例。 [[链接](https://www.cntcm.com.cn/content/202610/16/c505880.html)]
- [2026.10.14] 国家中医药管理局印发《中医医疗质量控制中心管理规定》（国中医药医政发〔2026〕10号，成文2026年10月8日，国家中医药管理局官网2026年10月14日公布全文，自印发之日起施行）。规定适用于各级中医质控中心建设与管理，明确国家级中心由国家中医药局设置管理，省级及以下参照执行；并规定质控中心应利用信息化手段开展质控，使用现有数据采集平台收集分析中医质控数据，落实网络和数据安全要求。本次打开了国家中医药管理局官方全文页及政策解读页。这是质控组织管理规定，不是单项产品发布。 [[国家中医药管理局](http://www.natcm.gov.cn/yizhengsi/zhengcewenjian/2026-10-14/38883.html)] [[政策解读](http://www.natcm.gov.cn/yizhengsi/zhengcewenjian/2026-10-14/38884.html)]
- [2026.10.12] 《海南自由贸易港中医药发展促进条例》已由海南省第七届人民代表大会常务委员会第二十六次会议于2026年9月30日通过，以海南省人民代表大会常务委员会公告第114号公布，自2026年11月1日起施行，共九章五十条。条例结合海南自由贸易港实际，对中医药服务、中药保护与产业发展、黎苗等民族医药发展、人才培养与科技支撑、传承创新与文化传播、开放发展与国际合作及保障措施作出制度安排；明确鼓励智慧中医医疗机构建设，允许综合运用互联网等现代信息技术和具备医疗器械资质的人工智能设备提供中医药服务，支持黎苗医药传承人运用数字设备和人工智能建立数字化、影像化传承档案，并支持建设中医药真实世界研究平台。本次打开了三亚市人大官网登载的条例全文，以及《海南日报》2026年10月12日文件版刊登的常委会公告。这是省级地方性法规，不是已经上线的模型发布。 [[三亚市人大](https://rd.sanya.gov.cn/rdsite/jgjs/202610/abc6e991368744248da826826aa4d6f3.shtml)] [[海南日报](http://news.hndaily.cn/html/2026-10/12/content_58468_19930810.htm)]
- [2026.10.09] 湖南省人民政府办公厅印发《湖南省中医药发展“十五五”规划》（湘政办发〔2026〕53号，发文日期2026年10月9日）。规划提出到2030年实现人人享有中医药服务，部署九个方面34项重点任务，其中包括加速中医药数智化赋能：建设智慧中医医院、探索处方共享与数据互联，加快中医药人工智能应用场景建设，扩大智能辅助诊疗和中药智能调配在基层的应用，并加强高质量数据集建设。省中医药管理局解读于2026年11月11日在省政府门户发布。这是省级规划部署，不是已经上线的模型发布。 [[湖南省人民政府](https://www.hunan.gov.cn/hnszf/xxgk/wjk/szfbgt/202610/t20261023_34087538.html)] [[政策解读](http://www.hunan.gov.cn/hnszf/xxgk/jd/bmjd/202611/t20261111_34099599.html)]
- [2026.10.09] 报道称徐桂华团队10月9日发布灵素·艾护中医护理大模型，面向辨证施护、科研与居家康养，27所加盟医院为首批应用单位 [[链接](https://finance.sina.com.cn/jjxw/2026-10-10/doc-iniutqmk0582279.shtml)]
- [2026.10.08] 国家中医药管理局医政司发布《关于做好中医护理方案和护理人员中医技术使用手册使用工作的通知》（国家中医药管理局官网标注时间2026年10月8日）。通知称，为提升中医护理能力、优化中医护理服务，国家中医药局委托中华中医药学会组织专家修订形成中风等13个病种中医护理方案（2026年版）和《护理人员中医技术使用手册（2026年版）》，并已在中华中医药学会网站发布，要求各级中医药主管部门组织相关医疗机构结合实际推广应用。本次打开了国家中医药管理局官方通知页。这是护理方案推广通知，不是单项产品发布。 [[国家中医药管理局](http://www.natcm.gov.cn/yizhengsi/zhengcewenjian/2026-10-08/38852.html)]
- [2026.09.30] 福建省卫生健康委员会、福建省中医药管理局印发《福建省“十五五”中医药振兴发展规划》（2026年9月29日印发，省卫生健康委官网标注发布时间2026年9月30日）。规划提出到2030年中医药高质量发展体制机制更加健全，实现人人享有中医药服务，推进中医药强省建设；部署服务体系、全生命周期服务、中西医协同、人才队伍、传承创新、产业新体系、文化传播、闽台融合与开放发展，以及数智化赋能、标准化和“三医”协同改革。数智化部分提出打造闽派中医特色高质量数据集与中医智能体，开展数据资产确权转化试点，落实“数据要素×”三年行动，支持省级中医医院打造智慧院区、建设专科大模型，归集名老中医经验，推动中医智能辅助决策系统与诊疗装备落地应用。这与已入库的《福建省提升中药质量促进中医药产业高质量发展的若干措施》不是同一份文件。本次打开了福建省卫生健康委官方全文页及附件PDF。这是省级规划部署，不是已经上线的模型发布。 [[福建省卫生健康委](https://wjw.fujian.gov.cn/xxgk/fgwj/zxwj/202610/t20261008_7222126.htm)] [[规划PDF](https://wjw.fujian.gov.cn/xxgk/fgwj/zxwj/202610/P020261008767413247349.pdf)]
- [2026.09.30] 宁夏回族自治区卫生健康委员会、自治区发展和改革委员会印发《宁夏回族自治区中医药振兴发展“十五五”规划》（自治区人民政府宁政函〔2026〕55号于2026年9月11日批复同意，两部门2026年9月16日印发，自治区卫生健康委官网2026年9月30日公布全文）。规划提出到2030年覆盖全民和全生命周期的中医药服务体系更加健全，实现人人享有中医药服务；部署完善服务体系、提升全生命周期服务能力、中西医协同、人才队伍、传承创新、健康服务融合、文化繁荣和开放发展，以及数智化标准化赋能与治理。数智化部分提出探索人工智能赋能中医药对外交流和高质量发展路径，实施自治区中医药智慧赋能项目，规范建设智慧中医医院和智慧中药房，并加强人工智能技术在基层中医药服务中的精准应用。本次打开了自治区卫生健康委官方全文页和自治区人民政府批复页。这是省级规划部署，不是已经上线的模型发布。 [[宁夏卫生健康委](https://wsjkw.nx.gov.cn/zfxxgk_279/fdzdgknr/gfxwj/202609/t20260930_5362324.html)] [[宁夏回族自治区人民政府](https://www.nx.gov.cn/zwgk/qzfwj/202609/t20260924_5356174.html)]
- [2026.09.24] 中国中医药报9月24日报道广安门医院慢性胃炎数据集完成产权登记，并建设中医专病可信数据空间；数据用于广医·岐智微调、科研和名医经验教学，未见公开下载。 [[链接](https://www.cntcm.com.cn/content/202609/24/c505607.html)]
- [2026.09.22] 大洋网9月22日报道，第二届广东省人工智能应用对接大会上，广东省中医院介绍名老中医辅助诊疗大模型矩阵，并称**禤国维**皮肤病诊疗大模型已于2025年6月投用。报道写核心病种诊断准确率达95%以上、已辅助决策2917次，上述数字来自院方介绍，不是外部对照试验结论。该院矩阵启动此前已有报道。 [[链接](https://news.dayoo.com/guangzhou/202609/22/139995_55006505.htm)]
- [2026.09.21] 中国中医药报9月30日报道，9月20日至21日，2026年数智中医药推进现场会暨数据要素综合试验区现场会在重庆举行，交流人工智能赋能中医药、数据要素与应用场景。报道提到横琴垂类模型、中药工业大模型和各地智能体实践，是会议综述，不代表新的模型首发。 [[链接](https://www.cntcm.com.cn/content/202609/30/c505658.html)]
- [2026.09.19] 中新网报道方证大模型9月19日开放接入，覆盖临床辅助诊疗、科研数据挖掘和人才培养，并计划部署到龙华医院及医联体 [[链接](https://www.chinanews.com.cn/jk/2026/09-19/10699553.shtml)]
- [2026.09.15] 界面新闻报道，9月15日第七届馆交会暨中医药发展大会上，传神素问推出**百医孪生计划**，拟依托其「素问」中医大模型为全国100位名老中医打造数字分身。这是计划发布，报道未列出已完成的全部名单，也未提供可独立核验的一致率数据。 [[链接](https://www.jiemian.com/article/15106308.html)]
- [2026.09.07] 工业和信息化部等六部门印发工信部联消费〔2026〕204号意见，将中药列为历史经典产业，并部署编制人工智能赋能实施指南、建设高质量数据集、用大模型解析传统工艺，以及发展智慧药房和产业工艺知识图谱。 [[工信部](https://www.miit.gov.cn/jgsj/xfpgys/wjfb/art/2026/art_ece6902ba0b24ad2806e670618f17a9f.html)] [[新华社](http://www.news.cn/politics/20260907/1d0ae2bfeb1f4d0fb58f7611ba77a3c3/c.html)]
- [2026.09] 中国中医科学院广安门医院在2026服贸会展示**广医·岐智2.0**，以AI医生「安安」覆盖患者服务、临床诊疗、病房管理等六大场景 [[链接](https://app.xinhuanet.com/news/article.html?articleId=202609101de3e66a53f7474ba7d373deaaa7e122)]
- [2026.09] 2026服贸会中医药展区，北京中医药大学**首发首展**中医体质辨识体系与具身智能推拿机器人，同期还有智能诊脉设备体验 [[链接](https://wjw.beijing.gov.cn/xwzx_20031/mtjj/202608/t20260807_4812596.html)]
- [2026.08.27] 学校官网称，8月27日“黔小杏医疗大模型”在2026数博会发布，以中医药文献、名医经验和临床数据训练，用于辅助诊断、体质辨识、养生推荐和用药指导。 [[链接](https://www.gzy.edu.cn/info/1501/12735.htm)]
- [2026.08] 南方财经报道，广州中医药大学以通用大模型为基座、用约20亿词元中医药数据持续训练“杏林智慧教学大模型”，已在中医各家学说、中国医学史和中医外科学试点。 [[链接](https://m.21jingji.com/article/20260824/herald/ef692f3ceba10c36edd3952f4d5ca892.html)]
- [2026.07.31] 广西壮族自治区人民政府办公厅印发《广西中医药（壮瑶医药）振兴发展“十五五”规划》（桂政办发〔2026〕50号，成文2026年7月24日，自治区人民政府门户网站2026年7月31日公布，刊于政府公报2026年第15期）。规划提出到2030年中医药传承创新发展机制更加完善，覆盖全民、全生命周期的中医药服务体系更加健全，基本形成服务惠民、产业兴旺、创新活跃、开放包容的中医药发展新格局；并专章部署加速中医药数智化赋能，实施“人工智能＋中医药”行动，建设智慧中医医院，支持基层配备中医智能辅助诊疗系统，建立中医药人工智能高质量数据集，推进人工智能在中医辅助决策、名老中医经验传承、诊疗康复等场景应用，支持自治区人工智能壮瑶医诊疗场景工程研究中心等项目。本次打开了自治区人民政府门户网站官方全文页。这是省级规划部署，不是已经上线的模型发布。 [[广西壮族自治区人民政府](http://www.gxzf.gov.cn/zfwj/zxwj/t27966422.shtml)]
- [2026.07.29] 贵州医科大学等在中国—东盟教育交流周发布全国首个民族药创制全域智能平台**华族本草**，以数智岐黄+Qwen为底座融汇多民族医药古籍 [[链接](https://www.gmc.edu.cn/info/1058/30267.htm)]
- [2026.07.28] 国家中医药局等十一部门印发《医疗卫生强基工程中医药行动方案》（国中医药医政发〔2026〕6号，成文2026年7月11日）。方案提出到2030年基层中医药服务网络全面建立，基础设施和数智化条件明显改善，并部署七项行动；其中明确加快县级中医医院信息化、持续推进智慧中医医院建设，探索医学人工智能辅助诊疗在基层中医药服务和名中医经验传承等场景的应用。 [[中国政府网](https://www.gov.cn/zhengce/zhengceku/202607/content_7076920.htm)] [[国家中医药管理局](http://www.natcm.gov.cn/yizhengsi/zhengcewenjian/2026-07-28/38433.html)]
- [2026.07.24] 上海中医药大学附属第七人民医院正式发布**岐元大模型**，采用预训练+领域微调+专家强化学习，支持生成式病历与名老中医Agent数字孪生，并亮相WAIC [[链接](https://dwgk.shutcm.edu.cn/2026/0725/c1890a175544/page.htm)]
- [2026.07.23] 经国务院批复同意（国函〔2026〕71号），国家中医药局、国家发展改革委联合印发《中医药振兴发展“十五五”规划》（国中医药规财发〔2026〕8号）。规划提出到2030年实现人人享有中医药服务，并部署十个方面重点任务，其中包括加速中医药数智化赋能与标准化建设；政策解读明确提出运用人工智能等新技术挖掘和传承中医药宝库。这是国家层面的五年规划，不是单项产品发布。 [[中国政府网](https://www.gov.cn/zhengce/zhengceku/202607/content_7076394.htm)] [[国家中医药管理局](http://www.natcm.gov.cn/guicaisi/zhengcewenjian/2026-07-22/38398.html)] [[新华社](https://www.news.cn/20260723/d6c2ca040e534b9186271da832c4ec6b/c.html)]
- [2026.07.03] 北京市卫生健康委网站转载《中国妇女报》报道，7月3日论坛以“数启岐黄·智赋本草”为主题在京举行，发布中医药智能体技术要求等标准、16项数字中医药应用场景案例，并启动“数据要素×”大赛北京分赛中医药赛道。 [[链接](https://wjw.beijing.gov.cn/xwzx_20031/mtjj/202607/t20260706_4748255.html)]
- [2026.07.01] 山西省卫生健康委员会、山西省药品监督管理局印发《中药饮片代煎服务质量管理规范》（晋卫中医药科技规〔2026〕1号，成文2026年6月16日）。规范适用于省内各级各类医疗机构，以及承接省内中药饮片代煎服务的生产、经营企业，覆盖医疗机构委托企业代煎和患者委托零售药店代煎两类场景；明确代煎属于中药饮片使用和销售的延伸服务，坚持患者自愿。规范厘清质量责任，医疗机构对代煎剂质量负主体责任，受托企业承担直接质量责任，禁止毒性中药、麻醉类中药饮片处方委托代煎，禁止将代煎业务再委托。追溯方面要求煎药过程视频监控资料留存不少于90天，代煎药液附带追溯二维码，原始处方、煎制工艺数据和设备运行日志至少保存一年，数据保存期限不少于三年。附则写明本规范有效期五年，自2026年8月1日起施行。本次打开了山西省卫生健康委员会政策文件栏目官方全文页，该页标注发布时间为2026-07-01 13:40，页面URL路径为2026-07-29。2026年11月24日，省卫生健康委员会新闻页和人民网山西频道（来源《山西日报》）对同一规范作了报道，作为后发新闻链接保留，不另作新条目。这是省级中药饮片代煎质量规范，此前目录漏收。 [[山西省卫生健康委员会](https://wjw.shanxi.gov.cn/tzgg/zcwj/202607/t20260729_10186628.shtml)] [[省卫生健康委员会新闻](https://wjw.shanxi.gov.cn/xwzx/szyw/202611/t20261124_10265935.shtml)] [[人民网山西频道](http://sx.people.com.cn/n2/2026/1124/c352662-41759168.html)]
- [2026.07] 新华网报道，2026年7月国家人工智能应用中试基地（医疗）在河南省人工智能大会集中发布中医经络辅诊模型、中西医结合食管癌大模型、中医药高质量数据集、中药研发大模型和名中医数字智能体。 [[链接](http://www.ha.xinhuanet.com/20260928/c8569fe1fbdb4ebc81053d86c6d93682/c.html)]
- [2026.07] 智慧眼携**砭石云中医**亮相WAIC 2026，以已备案砭石多模态大模型为底座，展示四诊仪与辅助诊疗系统 [[链接](http://www.eeo.com.cn/2026/0720/965556.shtml)]
- [2026.07] 安顿健康在WAIC 2026首发**七诊合参**中医机器人，集成面/红外面/舌/耳/闻/问/脉采集；报道称底座为2350亿参数的中医大模型。该页未写天回 [[链接](https://www.news.cn/finance/20260720/f6a8625c1be4412d9c311a232c7a35fa/c.html)]
- [2026.06] 中科闻歌通过港交所上市聆讯；报道提及与中国中医科学院合作的**大医金匮**中医大模型已通过中国信通院最高级别可信AI认证 [[链接](https://www.ncsti.gov.cn/kjdt/xwjj/202606/t20260610_249369.html)]
- [2026.05] 北京中医药大学中药学院称薪火中国药在世界数字教育大会发布，问答版已上线国家智慧教育公共服务平台 [[链接](https://zhongyao.bucm.edu.cn/yyxw/fb4b320d30c34e358de28a637c9f6f2c.htm)]
- [2026.04.24] 浙江省人民政府办公厅印发《浙江省“十五五”中医药发展规划》（浙政办发〔2026〕14号，2026年4月24日）。规划提出到2030年基本建成中医药现代化先行省，中医药人工智能应用水平全国领先，并统筹服务、产业、科技、人才、文化、治理、数智“七位一体”现代化；主要指标明确中医类医疗机构医学大模型应用率到2030年达到100%，同时提出推动浙江成为中医药人工智能发展的重要策源地。这是省级规划部署，不是已经上线的模型发布。 [[浙江省政府公开文本](https://zjjcmspublicnew.oss-cn-hangzhou-zwynet-d01-a.internet.cloud.zj.gov.cn/cms_files/filemanager/1567290/attach/20266/054C52CACC6589E4F1917D8B993978B9.pdf)] [[商务部转载](https://tradeinservices.mofcom.gov.cn/article/zcfb/zcfg/202607/200234.html)] [[浙江中医药大学转载](https://itc.zcmu.edu.cn/202607132.pdf)]
- [2026.04.21] 国家中医药管理局印发《全国基层中医药工作示范市（县）管理办法》（国中医药医政发〔2026〕5号）。办法规定示范市（县）创建每3年为一个周期，由国家中医药管理局负责总体规划与组织管理；申报经市县级自评、省级审核推荐、国家局复核后确定为创建单位，创建周期结束前6个月开展省级和国家评估验收，合格后命名。中国中医药报官网全文页标注来源为国家中医药管理局、日期为2026年4月22日；官网原链为http://www.natcm.gov.cn/yizhengsi/zhengcewenjian/2026-04-21/37964.html。本次打开了中国中医药报全文页；本轮直接访问国家中医药管理局原页返回超时或HTTP 500。这是示范创建管理办法，不是单项产品发布。 [[国家中医药管理局](http://www.natcm.gov.cn/yizhengsi/zhengcewenjian/2026-04-21/37964.html)] [[中国中医药报](https://www.cntcm.com.cn/m/content/202604/22/c502106.html)] [[政策解读](http://www.natcm.gov.cn/yizhengsi/zhengcewenjian/2026-04-21/37965.html)]
- [2026.04.21] 北京中医药大学牵头研发的**薪火中国药**中医药教育大模型通过国家生成式人工智能服务备案，成为国内首个获批面向公众服务的中医药领域大模型 [[链接](https://regional.chinadaily.com.cn/education/cn/2026-04/22/c_1177692.htm)]
- [2026.04.14] 广西壮族自治区卫生健康委员会、自治区中医药管理局、自治区工业和信息化厅印发《广西中医药产业高质量发展三年行动方案（2026—2028年）》（桂中医药发〔2026〕10号，成文2026年4月9日，经自治区人民政府同意，自治区卫生健康委官网2026年4月14日公布全文）。方案提出到2028年中医药全产业链总产值突破1100亿元；部署中药材种植养殖、中药制造数智化绿色化改造、质量追溯体系，以及拓展人工智能＋中医药诊疗服务应用场景，支持基层配备中医智能辅助诊疗系统、便携式智能理疗设备和远程会诊终端，并投入支持智慧中医医院建设。这与同日核验入库的《广西中医药（壮瑶医药）振兴发展“十五五”规划》不是同一份文件。本次打开了自治区卫生健康委官方全文页及政策解读页。这是省级产业行动方案，不是已经上线的模型发布。 [[广西卫生健康委](https://wsjkw.gxzf.gov.cn/xxgk_49493/fdzdgk/gkwj/zzqzcwj/t27468144.shtml)] [[政策解读](https://wsjkw.gxzf.gov.cn/xxgk_49493/fdzdgk/gkwj/zcjd/t27468260.shtml)]
- [2026.04.08] 国家中医药局、国家卫生健康委印发《医院中药饮片管理规范（2026版）》（国中医药医政发〔2026〕3号，成文2026年4月8日，中国政府网国务院部门文件库刊登全文）。规范适用于各级各类医院中药饮片采购、验收、贮藏与养护、调剂、临方炮制、煎煮、临方加工、处方点评等管理，自发布之日起施行，2007年版规范同时废止。文件要求以质量管理为核心，鼓励使用信息化手段加强中药饮片管理；对代煎服务明确医院负主体责任、受托机构负直接责任，并要求建立健全代煎质量跟踪、追溯、监控体系。本次打开了中国政府网官方全文页。这是部门管理规范，不是已经上线的模型发布。 [[中国政府网](https://www.gov.cn/zhengce/zhengceku/202604/content_7066059.htm)]
- [2026.04] 山东中医药大学附属医院启动山东省卫健委「人工智能＋」中医药重点场景**智汇岐黄**大模型项目 [[链接](http://ccpd.china.com.cn/2026-04/17/content_43401621.html)]
- [2026.03.27] 国家中医药管理局印发《三级中医医院评审标准（2026年版）》（国中医药医政函〔2026〕39号，成文2026年3月13日）。通知提出，为落实“强基、稳二、控三”工作部署和分级诊疗制度要求，优化完善中医医院评审制度，该标准自通知印发之日起实施，2017年版三级中医医院、三级中西医结合医院、三级民族医医院评审标准及其实施细则等评审规定同时废止。本次打开了中国政府网国务院部门文件页（来源标注为国家中医药局网站）及可公开下载的官方PDF（政府网文件最后修改时间为2026年3月28日）。官网原链为http://www.natcm.gov.cn/yizhengsi/zhengcewenjian/2026-03-27/37885.html。这是医院评审标准，不是单项产品发布。 [[中国政府网](https://www.gov.cn/zhengce/zhengceku/202603/content_7064072.htm)] [[官方PDF](https://www.gov.cn/zhengce/zhengceku/202603/P020260328646933871054.pdf)] [[国家中医药管理局](http://www.natcm.gov.cn/yizhengsi/zhengcewenjian/2026-03-27/37885.html)]
- [2026.03.23] 国家中医药局、国家卫生健康委、国家疾控局印发《乡镇卫生院 社区卫生服务中心中医药服务管理基本规范》（国中医药医政发〔2026〕2号，成文2026年3月11日），对2003年版乡镇卫生院、社区卫生服务中心两项基本规范进行合并修订。规范共六章，适用于依法设立的乡镇卫生院、社区卫生服务中心，明确中医科和中药房建设、人员配备、服务内容及业务指导等要求。本次打开了中国政府网国务院部门文件页全文（来源标注为国家中医药局网站），并核到新华社经中国政府网转发的报道（2026年3月24日）。官网原链为http://www.natcm.gov.cn/yizhengsi/zhengcewenjian/2026-03-23/37872.html。这是基层中医药服务管理规范，不是单项产品发布。 [[中国政府网](https://www.gov.cn/zhengce/zhengceku/202603/content_7063623.htm)] [[国家中医药管理局](http://www.natcm.gov.cn/yizhengsi/zhengcewenjian/2026-03-23/37872.html)] [[新华社报道](https://www.gov.cn/lianbo/202603/content_7063620.htm)]
- [2026.03.17] 中国中医药报报道，2026年3月17日研讨会上，中医药信息研究所所长李海燕介绍医源中医大模型已用于医案结构化、智能问诊、处方推荐和中成药合理使用等场景。 [[链接](https://www.cntcm.com.cn/content/202603/20/c501417.html)]
- [2026.03] 上海中医药大学称方证多模态大模型入选医疗领域国家人工智能应用中试基地阶段成果，基座为视觉语言模型 [[链接](https://kjrw.shutcm.edu.cn/2026/0330/c805a172392/page.htm)]
- [2026.02] 工信部等八部门印发《中药工业高质量发展实施方案（2026—2030年）》，明确运用人工智能与知识图谱赋能经典名方与名老中医经验方研发 [[链接](https://www.gov.cn/zhengce/zhengceku/202602/content_7057174.htm)]
- [2026.01.09] 科技日报报道，1月9日广东省中医院启动名老中医辅助诊疗大模型矩阵；禤国维皮肤病诊疗大模型和心血管病诊疗大模型已投入临床。 [[链接](https://www.stdaily.com/web/gdxw/2026-01/12/content_460323.html)]
- [2026.01] 新华网报道，2025年12月24日河南健康产业大会上，河南省卫生健康委展示中医经络辅助诊断模型和豫产豫药多模态神农本草大模型，后者用于药材识别、真伪鉴别、成分定量和产地溯源。 [[链接](http://www.ha.xinhuanet.com/20260105/b91d84bacd1c46389a007e0cc201962d/c.html)]
- [2026.01] 成都中医药大学官网称，温川飙团队牵头的“中医药AI模型高质量数据集”（项目编号2025-AISJK-02013）入选工信部与药监局2025年度人工智能医疗器械创新任务揭榜名单。 [[链接](https://www.cdutcm.edu.cn/info/1074/138321.htm)]
- [2026.01] 中医聪宝称素问中医内容生成大模型算法列入国家网信办第十四批深度合成服务算法备案 [[链接](https://www.tcmbrain.com/?list_43/180.html)]

</details>

<details>
<summary>2025 · 30</summary>

- [2025.12.20] 吉林发布**众星·长白岐黄1.0** AI原生多模态中医药大模型 [[链接](https://www.chinanews.com.cn/cj/2025/12-20/10537422.shtml)]
- [2025.12] **智明堂ZMT-M1**在国家中医执业医师资格考试模拟测试中以96.26分获得该领域最佳成绩，已在全国100余间诊室试点应用 [[链接](https://m.tech.china.com/redian/2025/1229/122025_1789291.html)]
- [2025.12] 广安门医院官网称广医·岐智取得国家级深度合成算法备案，并称是国内首家完成该项备案的中医院 [[链接](https://www.gamyy.cn/gzb/news/big/114632.html)]
- [2025.12] 固生堂发布“中医大脑”及国医大师施杞教授AI数字分身，已累计发布14位顶级专家数字分身。八大专科出自另一则十大分身报道，本页未写 [[链接](https://www.jjckb.cn/20251231/693ca93b14ff4f57adc359959dc0320d/c.html)]
- [2025.11.02] 北京科技大学新闻网称，2025年11月2日郑州大会上，学校联合郑州市卫健委、郑州市中医院和河南中医药大学数智中医药研究院发布岐黄针灸大模型，四诊采集后生成针灸处方。 [[链接](https://news.ustb.edu.cn/info/1087/72015.htm)]
- [2025.11] 国家卫健委等五部门印发《关于促进和规范”人工智能+医疗卫生”应用发展的实施意见》，明确支撑建设中医药诊疗大模型 [[链接](https://www.gov.cn/zhengce/zhengceku/202511/content_7047018.htm)]
- [2025.10.26] 中国经济网报道10月26日发布中西医结合高血压诊疗大模型Idiom-Hypertension，用于高血压规范管理 [[链接](https://www.ce.cn/cysc/yy/hydt/202510/t20251027_2541616.shtml)]
- [2025.10.21] 科技日报报道CTA在中医药临床疗效评价大会发布，基于Qwen2.5-14B微调，面向临床试验方案、数据管理与统计 [[链接](https://www.stdaily.com/web/gdxw/2025-10/21/content_418966.html)]
- [2025.09.18] 中原药谷基层中医药振兴工程下，**伊尹中医经典大模型**在嵩县发布启用，融合中医教育与AI辅助诊疗服务县域基层 [[链接](http://www.ha.xinhuanet.com/20250918/a3da94037689422dbcd1fe57fa62ef94/c.html)]
- [2025.09.12] 广安门医院官网称，2025年9月12日服贸会论坛发布广医·岐智2.0，并推出AI医生安安，已出现在门诊导诊屏和预问诊界面。 [[链接](https://www.gamyy.cn/gzb/news/big/113898.html)]
- [2025.09] **智赋岐黄天功**中医AI大模型通过国家深度合成服务算法备案，应用于中医四诊仪与体质辨识 [[链接](http://zs.scbzol.com/zs/2025/0919/328624.html)]
- [2025.09] 页面受评对象是**传神素问**中医大模型，获得可信AI中医药大模型4+级；正文写它由传神语联基于任度大模型打造 [[链接](https://zhongyi.gmw.cn/2025-09/10/content_38277329.htm)]
- [2025.09] 中国中医科学院官网称，2025年9月10日至14日服贸会上，其智能科学与工程技术研究中心展示大医金匮大语言模型与多轮问诊系统，以及舌诊仪和移动中医智能检测厅。 [[链接](https://www.cacms.ac.cn/news_dynamic/detail/5080.html)]
- [2025.08.09] 国家超算天津中心联合天津中医药大学等发布**天河·灵枢**2.0，由针灸专科扩展至20余科；同步启动中医药智能模型评价体系 [[链接](http://tj.people.com.cn/n2/2025/0809/c375366-41317410.html)]
- [2025.08.06] 湖北日报报道，2025年8月6日湖北中医药大学、湖北时珍实验室与传神语联签约，以传神·素问中医大模型开展产学研用合作。 [[链接](https://news.hubeidaily.net/mobile/c_4393128.html)]
- [2025.08.01] **固生堂**正式发布十大“国医AI分身”，基于国医大师及名中医临床经验构建。页面写专家模拟一致性达86%以上，不是辨证准确率 [[链接](http://sz.people.com.cn/n2/2025/0801/c202846-41310443.html)]
- [2025.07] 中国中医科学院广安门医院与多家医联体单位成立**广医·岐智大模型智能体联盟**，推进跨机构智能诊疗能力辐射 [[链接](https://www.gamyy.cn/gzb/news/big/112751.html)]
- [2025.06.19] **中医横琴**垂类大模型正式发布 [[链接](https://www.stdaily.com/web/gdxw/2025-06/20/content_357526.html)]
- [2025.06.18] 国家数据局收录成都中医药大学案例：用大模型对996册中医古籍做自动分词和实体识别，并基于ChatGLM-6B关联中医术语、构建穴位-脏腑等知识图谱。 [[链接](https://www.nda.gov.cn/sjj/ywpd/szkjyjcss/0618/20250618095629525611799_pc.html)]
- [2025.06.06] 南京中医药大学人工智能与信息技术学院页面称，2025年6月6日发布灵山中医大模型（小杏仁）和素山中药大模型（素山智思体），分别服务中医临床教学科研和中药学教学科研。 [[链接](https://xxjs.njucm.edu.cn/2025/0529/c445a156198/pagem.htm)]
- [2025.05.17] 四川在线5月17日报道，成都体育学院联合中科视语发布中医运动医学**寰枢**大模型与智能体，定位竞技体育、大众健康和科教场景，可生成运动处方和节气养生方案。这是2025年的发布报道，本页未核验权重或对外接口是否公开。 [[链接](https://sichuan.scol.com.cn/ggxw/202505/82968100.html)]
- [2025.05.10] 北京中医药大学官网称，2025年5月10日发布薪火中国药智思体1.0，依托讯飞星火与DeepSeek，参数超700亿，面向助学、助教、助研、助管和国际合作。 [[链接](https://www.bucm.edu.cn/bzyyw/1c0b0fe535764fcc886c87b560caa0ee.htm)]
- [2025.05.10] 中国中医科学院发布中医药大模型评测标准 [[链接](https://www.news.cn/politics/20250510/5e6a0b4978b44b69b67dbfb7282fd220/c.html)]
- [2025.04.11] 凤凰网报道，2025年4月11日华为云生态大会上，九为健康发布基于盘古大模型的九为神农中医大模型智能体，覆盖药物研发、复方优化和辅助诊疗。 [[链接](https://biz.ifeng.com/c/8iTNRXVw44k)]
- [2025.04] 传神语联发布**任度·素问**中医大模型，基于全自研混合熵(moH)技术架构，支持智能问诊、辨证分析、方剂推荐 [[链接](https://www.transn.com/about_us/consult/article/1924766101036437505)]
- [2025.03.28] 中国中医科学院广安门医院28日正式发布**广医·岐智**中医大模型，成为国内首家本地化部署”算力+模型+应用”一体化服务的中医医院 [[链接](https://www.xinhuanet.com/tech/20250328/8b1685ad8c6f48c9bdc2add1658edac3/c.html)]
- [2025.03.20] 国务院办公厅印发《关于提升中药质量促进中医药产业高质量发展的意见》（国办发〔2025〕11号，成文2025年3月15日，中国政府网国务院文件栏目发布日期2025年3月20日）。意见经国务院同意，从中药资源保护利用、中药材产业发展、产业转型升级、药品价值评估和配备使用、科技创新、质量监管、开放发展和综合保障等方面提出措施。产业升级部分提出推进中药工业数字化智能化发展，运用数智技术、绿色技术赋能全产业链，建设数字化车间和智能工厂；临床价值评估部分提出利用循证医学等手段，开发中医药临床疗效评价大模型，促进人用经验向临床证据转化；并支持特色优势医疗机构中药制剂依法调剂使用，鼓励建设基层共享中药房。本次打开了中国政府网官方全文页。这是国务院办公厅产业质量政策，不是单项产品发布。目录此前仅有福建省落实该意见的若干措施，未收本文件本身。 [[中国政府网](https://www.gov.cn/zhengce/zhengceku/202503/content_7014717.htm)]
- [2025.03.13] 新华网报道，2025年3月13日南京中医药大学黄煌团队与杭州脉景健康发布黄煌经方AI辅助诊疗系统，用大语言模型与知识图谱把“方人相应”做成可计算诊疗流程。 [[链接](http://www.js.xinhuanet.com/20250314/aa816bb98d1041afa0fa7bca45583d1b/c.html)]
- [2025.03] 云诊科技官网称，公司基于自研舌诊多模态模型TongueLMM和DeepSeek-R1发布云诊华医大模型，用于辨证论治、体质辨识和诊疗报告生成。 [[链接](https://www.ai-tongue.com/pages/news/2025/04/9a6f1920-4819-406e-8d1f-6ba0b838a7f8.html)]
- [2025.01.08] 2025年1月8日，北京科技大学联合河南中医药大学发布张仲景中医药大模型1.0，功能包括智能辨证、证素推荐、经方应用和方药分析。 [[链接](https://news.ustb.edu.cn/info/1087/67760.htm)]

</details>

<details>
<summary>2024 · 5</summary>

- [2024.12] 招联消费金融联合中山大学、广州中医药大学深圳医院发布中医垂直大模型**仲思**，落地深圳多家社康中心智能问诊 [[链接](https://finance.sina.com.cn/jjxw/2024-12-16/doc-inczrzsp5791684.shtml)]
- [2024.11] 华东师范大学、上海中医药大学、华东理工大学、海军军医大学、临港实验室和华润江中一起做了**数智岐黄**。1.0 在 2024 年 1 月 19 日发布。2024 年 11 月 25 日，他们在上海一场论坛上介绍了 2.0。 [[链接](https://pharm.ecnu.edu.cn/08/27/c43775a657447/page.htm)]
- [2024.09] 中科闻歌发布**大医金匮**中医大模型及中医智能健康管理平台，基于1500余本中医典籍及海量临床医案训练 [[链接](https://36kr.com/newsflashes/2946967562099592)]
- [2024.07.19] 两部门印发国中医药综发〔2024〕6号意见，推动中医药数字化转型，提出加强数据要素开发利用、打造中医药大模型和智慧服务应用。文件成文日期为2024年7月19日。 [[链接](http://www.natcm.gov.cn/bangongshi/zhengcewenjian/2024-08-14/34672.html)]
- [2024.05.10] 天士力与华为云联合发布**数智本草**大模型，基于盘古语言与药物分子模型。 [[链接](https://www.taslypharma.com/tsl/40931.jhtml)]

</details>

<details>
<summary>2023 · 1</summary>

- [2023.07.29] 南京大经中医发布**岐黄问道·大模型**，基于千万级知识图谱与临床数据，面向医疗机构开放内测 [[链接](http://js.news.cn/20230729/fa034db71a00487b819a4ad95b44673e/c.html)]

</details>


</details>

## 综述

<details>
<summary>95 篇，按年收着</summary>

<details>
<summary>2026 · 47</summary>

- [*Frontiers in Pharmacology*] **Deng et al. 2026: 人工智能解码中药复方抗癌机制的进展、挑战与展望** 赣州市人民医院邓永康、娄宗泽、李国政、黄苗、吴桂华在 Frontiers in Pharmacology 发表叙述性综述，系统整理人工智能用于解码中药复方抗癌机制的近期工作，重点覆盖多味复方及其组合机制，包括机器学习筛选、深度学习活性预测、文献挖掘、网络药理学、分子对接与虚拟筛选，以及多组学整合，并讨论数据不标准、模型可解释性不足、外部验证不够以及中医理论与生物医学计算框架衔接困难等瓶颈。页面标注日期为2026年8月19日与2026年11月4日。本次打开了期刊官方全文页。这是综述，不是新模型发布。 [Ganzhou People's Hospital] [[论文](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2026.1972299/full)] [[DOI](https://doi.org/10.3389/fphar.2026.1972299)]
- [*Frontiers in Pharmacology*] **Huang 等：以代谢综合征为案例评估人工智能用于中医经典名方研发的技术成熟度** Huang、Jiang、Hu、Ye、Liu 等以代谢综合征为案例，回顾知识图谱、大语言模型和高通量验证三条技术线在中医经典名方精准研发中的就绪程度。作者引用《中医方剂大辞典》第二版约 99,584 个方名条目，并称 2013–2024 年国家药监局年均批准中药新药不足 10 个（合计 77 个）。文中评估知识图谱约处在技术成熟度等级（TRL）3–6，大语言模型约在 TRL 1–5，并指出三条技术线并不均衡。这是技术就绪度叙事综述，不是新药获批报告或疗效试验。本次打开了期刊全文页。 [中药经典名方现代化国家重点实验室，南昌大学第二附属医院江西省分子医学重点实验室，江西省科技基础条件平台中心江西省计算中心，江西中医药大学附属医院，中山大学深圳校区生物医学工程学院广东省传感技术与生物医学仪器重点实验室] [[DOI](https://doi.org/10.3389/fphar.2026.1970742)] [[论文](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2026.1970742/full)]
- [*Frontiers in Artificial Intelligence and Applications*] **Hu Ziquan：中医药院校学科群建设中的人工智能应用定量系统综述（2023–2025）** Hu Ziquan 在 IOS Press 丛书 Frontiers in Artificial Intelligence and Applications 第 433 卷《Digitalization and Management Innovation V》发表定量系统综述（第 730–743 页），纳入 2023–2025 年 372 篇同行评议文献（国际 98、国内 274），并用作者自建的 TI、RDI、IDI、CKII 等指数描述研究主题、区域差异与技术瓶颈。文中给出五类主题的 TI 值，并报告模型可解释性总体偏低（平均 IDI=0.72）、古典中医知识融入不足（平均 CKII=0.20）等作者计算结果。页面可见摘要，未见作者单位。这是机构与学科发展导向的定量综述，不是临床试验。本次打开了 IOS Press 电子书官方页面。 [[DOI](https://doi.org/10.3233/FAIA261138)] [[论文](https://ebooks.iospress.nl/doi/10.3233/FAIA261138)]
- [*Guidelines and Standards of Chinese Medicine*] **Liu Changning、Zhang Xiaoduo、Shang Hongcai：数智技术驱动的循证中医药研究系统整合** Liu Changning、Zhang Xiaoduo、Shang Hongcai 通讯在《Guidelines and Standards of Chinese Medicine》2026 年 10 月 26 日优先发表综述，讨论循证中医药研究体系在方法与中医整体观不完全兼容、辨证主观性和疗效评价指标共识不足等问题，并综述大数据、人工智能和“互联网+”等数智技术在证据库建设、规范化临床研究设计和中药质量保障中的可能路径。这是标准与方法学综述，不是已部署系统的效果评价。本次打开了 Ovid 期刊官方页面，可见摘要与作者单位。 [北京中医药大学东直门医院教育部中医内科学重点实验室，广州中医药大学深圳市宝安中医院心内科，北京中医药大学东方医院] [[DOI](https://doi.org/10.1097/gscm.0000000000000131)] [[论文](https://www.ovid.com/jnls/gscm/fulltext/10.1097/gscm.0000000000000131~systematic-integration-of-evidence-based-traditional-chinese)]
- [*Frontiers in Neurology*] **Huang 等：舌诊用于中风中医辨证的诊断准确性系统综述、荟萃分析与人工智能模型叙事综合** Huang、Yin、Shao、Jiang、Wang、Xu 按诊断试验准确性方法检索至 2026 年 2 月 23 日，纳入中国大陆 10 项研究、3,437 名受试者（人工舌诊 6 项 2,191 人，人工智能辅助 4 项 1,246 人），并在 PROSPERO 注册 CRD420261288502。作者明确警告证据确定性很低、金标准独立性得不到保证，因此把结果视为与既有证候分类流程的探索性一致，而不是已经临床验证的诊断准确性。人工智能部分按 SWiM 做叙事综合。本次打开了期刊全文页。 [安徽中医药大学针灸推拿学院，安徽中医药大学医药信息工程学院，安徽中医药大学第二附属医院，安徽中医药大学第一附属医院，皖北卫生职业学院临床医学系，安徽中医药大学第一临床医学院] [[DOI](https://doi.org/10.3389/fneur.2026.1874937)] [[论文](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2026.1874937/full)]
- [*Frontiers in Physiology*] **Li 等：2015–2026 年中医舌诊人工智能研究的文献计量综述** Li、Yang、Lin、Wang、Yan、Zheng、Xiang、Tang 对 2015 年 1 月至 2026 年 8 月 Web of Science 核心合集与 CNKI 中的中医舌诊人工智能文献做文献计量比较，纳入 482 篇（WoSCC 295、CNKI 187），并用 CiteSpace、VOSviewer 分析合作网络、关键词与突现主题。作者强调两个库需分开分析。这是研究格局综述，不是诊断准确性的临床验证。本次打开了期刊全文页。 [广州市干部和人才健康管理中心中医科，长沙医学院护理学院，中信湘雅生殖与遗传专科医院影像科 / 湖南省生殖与遗传临床研究中心] [[DOI](https://doi.org/10.3389/fphys.2026.1895902)] [[论文](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2026.1895902/full)]
- [*Frontiers in Medicine*] **Wang 等：人工智能舌象分析用于胃癌、癌前病变及相关胃肠疾病无创筛查的系统综述** Wang、Li、Zhang、Shao、Gao、Zhang 按 PRISMA 2020 检索至 2026 年 6 月 10 日，纳入 2018–2025 年 9 项用机器学习或深度学习分析数字舌象、并报告定量指标的研究，覆盖胃癌、胃黏膜癌前病变或高风险筛查及相关胃肠疾病。作者报告内部验证 AUC 约 0.61–0.99，但仅 3 项有外部验证且普遍出现性能下降，校准评估少见。结论把该方法定位为有前景、仍处早期的胃镜前辅助分层工具，而不是胃镜替代。PROSPERO 注册号 CRD420261444857。本次打开了期刊全文页。 [山东中医药大学第一临床医学院，山东中医药大学附属医院神经内二科] [[DOI](https://doi.org/10.3389/fmed.2026.1931256)] [[论文](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1931256/full)]
- [*Biomedical and Environmental Sciences*] **Jia 等：中西医结合视角下心血管疾病临床决策支持系统的双轨并行与融合创新综述** Jia、Zhang、Tong 等，Ma、Li、Zhang Huamin 通讯，在《生物医学与环境科学》2026 年 39 卷 9 期第 1115–1130 页综述心血管疾病临床决策支持系统，并专节讨论中医临床决策支持系统（TCM-CDSS）借助“理法方药”、名医经验和知识图谱，形成从辨证到推荐方药的闭环。文中称高血压相关研究已报告处方和血压方面的改善，但对主要心血管事件和死亡率的影响仍需进一步评价。这是综述，不是新系统的前瞻性临床试验。本次打开了 besjournal.com 官方论文页。官网可见收稿日期 2026-03-01、接受日期 2026-08-17、在线日期 2026-09-20。 [中国中医科学院中医基础理论研究所，中国中医科学院中医药信息研究所，中国中医科学院中医临床基础医学研究所，中国中医科学院中医药数据中心，北京中医药大学中医学院，中国中医科学院中药研究所] [[DOI](https://doi.org/10.3967/bes2026.094)] [[论文](https://www.besjournal.com/en/article/doi/10.3967/bes2026.094)]
- [*集成技术*] **贺宇翔等 2026：人工智能驱动的中医药现代化：从经验范式到数据智能范式的转变** 深圳理工大学生物医学工程学院贺宇翔、唐若凝、尤志峰、张鹏，药学院冯志炜，医疗器械产业技术研究院李健，与中国科学院深圳先进技术研究院成文翔、柯丽青等在《集成技术》发表综述。张鹏另有山东中科先进技术有限公司署名。文章以“从经验范式到数据智能范式的转变”为主线，围绕中药物质基础解析、复方配伍优化、制药工程与产业转型、知识工程与大模型应用四个方向，讨论人工智能如何通过数据建模、跨模态融合与系统推理推动中医药研究走向数据驱动、证据约束和人机协同；同时指出各方向成熟度不均衡，以及可解释性、知识标准化和伦理治理方面的挑战。期刊元数据标注刊于2026年第15卷第5期第83–101页，发表日期2026-09-16，在线日期2026-06-15，DOI为10.12146/j.issn.2095-3135.20260517001。本次打开了期刊官方论文页，并核到可公开获取的官方PDF（许可标注为CC BY 3.0）。这是综述，不是新模型发布。 [深圳理工大学，中国科学院深圳先进技术研究院，山东中科先进技术有限公司] [[论文](https://jcjs.siat.ac.cn/article/doi/10.12146/j.issn.2095-3135.20260517001)] [[PDF](https://jcjs.siat.ac.cn/cn/article/pdf/preview/10.12146/j.issn.2095-3135.20260517001.pdf)] [[DOI](https://doi.org/10.12146/j.issn.2095-3135.20260517001)]
- [*兰州大学学报(医学版)*] **从大语言模型到智能体（兰州大学学报医学版综述）** 以「大模型→智能体」演进为主线的中医临床辅助诊疗中文系统综述，梳理研究进展、关键问题与方向（兰州大学学报(医学版) 2026;52(4):49-57） [[DOI](https://doi.org/10.13885/j.issn.2097-681X.T20260032)]
- **Agentic and Knowledge-Grounded LLMs in TCM（预注册）** 2026 年 7 月在 OSF 登记的综述计划，准备从证据图谱、文本挖掘和能不能用到临床上，看中医里的智能体和带知识的大模型。综述还在做。 [[预注册](https://doi.org/10.17605/osf.io/kq8jx)]
- [*International Journal of Pattern Recognition and Artificial Intelligence*] **中医大模型关键技术综述（IJPRAI）** 系统综述中医大模型知识组织、辅助诊断与临床决策支持关键技术（World Scientific IJPRAI正式发表） [Guangdong Provincial Hospital of Traditional Chinese Medicine，Guangdong University Of Finances and Economics，Guangdong University of Finance] [[DOI](https://doi.org/10.1142/s0218001426590263)]
- [*Journal of Traditional Chinese Medical Sciences*] **AI驱动中医诊断智能化综述（JTCMS）** 综述多模态融合与大模型在中医四诊智能化中的应用、挑战与展望（JTCMS正式发表） [暨南大学，北京中医药大学] [[DOI](https://doi.org/10.1016/j.jtcms.2026.05.002)]
- [*Frontiers in Medicine*] **Nie et al. 2026: Artificial intelligence guided acupuncture decision making and treatment: a review of research** 长春中医药大学针灸推拿学院聂茹、邓凯月、何静、贾佳琳、王鸿烨、袁淑婷、李铁在 Frontiers in Medicine 发表综述，按临床流程回顾人工智能在针灸中的应用，覆盖穴位选择标准化、定位辅助、实时安全监测和个性化疗效预测四方面，并讨论现有工作与后续智能针灸系统发展建议。作者指出已有中医人工智能综述多为宽泛概览，较少直接对照针灸临床工作流。期刊页标注文章类型为 Review，在线 2026年4月13日、发表 2026年4月27日，刊于第13卷。本次打开了 Frontiers 官方全文页并下载了官方 PDF。这是综述，不是新模型发布。 [Changchun University of Chinese Medicine] [[论文](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1752082/full)] [[PDF](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1752082/pdf)] [[DOI](https://doi.org/10.3389/fmed.2026.1752082)]
- [*Frontiers in Neurology*] **Chan et al. 2026: Integrating machine learning into acupuncture research: a scoping review** 中国医药大学针灸研究所与附属安南医院 Chan Wancy、Huang Guan-Jun、Huang Chien-Chen、Chen Yi-Hung 在 Frontiers in Neurology 发表范围综述（期刊页标注文章类型为 Systematic Review），梳理 2011–2024 年 PubMed 中针灸与机器学习交叉文献。作者纳入 36 篇，称 2019 年后明显增加、多数来自中国；17 篇关注疗效预测且以疼痛相关病种为主，其余涉及手法识别、处方推荐、穴位敏化与特异性、使用频次预测、经脉传导以及针刺机器人定位等。疗效预测研究中支持向量机最常用，11 项中有 7 项将磁共振成像作为特征，并以治疗应答分类为标签。作者认为预测表现整体积极，但样本量小、方法异质、数据类型不一和缺乏标准化数据集限制了可泛化性。期刊页标注在线 2025年12月22日、发表 2026年1月14日，刊于第16卷，文章号 1689061。本次打开了 Frontiers 官方全文页并下载了官方 PDF。这是综述，不是新模型发布。 [China Medical University，An Nan Hospital, China Medical University] [[论文](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2025.1689061/full)] [[PDF](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2025.1689061/pdf)] [[DOI](https://doi.org/10.3389/fneur.2025.1689061)]
- [*上海中医药杂志*] **人工智能驱动下的中医智能诊疗研究进展与挑战** 以中医辨治六步程式为骨架的全链路（四诊-辨证-处方-疗效预测）中文综述，对照监督/无监督/强化/深度学习范式（上海中医药杂志 2026;60(1)） [[DOI](https://doi.org/10.16305/j.1007-1334.2026.z20250609004)]
- [*Chinese Science Bulletin*] **面向临床的中西药联用安全性数智评价** 中西药联用的不良反应隐匿、机制复杂，且个体差异大。文章提出一条从智能预测、风险识别、机制验证到数智决策的评价路径，覆盖用药前预警和用药中识别。 [[DOI](https://doi.org/10.1360/csb-2026-0084)]
- [*Communications in Computer and Information Science (Springer)*] **多模态大模型驱动舌脉面诊智能化综述（Springer 书章）** 唯一以「多模态LLM×四诊感知」为题的综述性文本，覆盖舌/脉/面诊智能化（Springer CCIS 会议书章，评审强度低于期刊） [Chinese Academy of Social Sciences，Institute of Ethnology and Anthropology，University of Chinese Academy of Social Sciences] [[DOI](https://doi.org/10.1007/978-981-95-7299-1_15)]
- [*中华中医药学刊*] **人工智能赋能中医数字化诊断：现状与挑战（中华中医药学刊）** 短文，写人工智能在中医数字化诊断里能做什么，也写了数据质量、说得清说不清、以及和中医理论怎么接上。刊在《中华中医药学刊》。 [[DOI](https://doi.org/10.13193/j.issn.1673-7717.2026.01.004)]
- [*Chinese Medicine*] **中医为何需要可解释人工智能** 认为中医人工智能的障碍不只是预测分数，而是数据驱动模型和证候、病机这类理论推理对不上，所以需要可解释性。 [[DOI](https://doi.org/10.1186/s13020-026-01455-4)]
- [*Healthcare*] **东亚传统医学如何进入国际卫生信息标准** 范围综述：检索 2016 年 1 月至 2026 年 3 月的英文文献，看韩医、中医和汉方概念怎样映射进主流卫生信息标准。 [[DOI](https://doi.org/10.3390/healthcare14183011)]
- [*Integrative Medicine Research*] **Yao et al. 2026: LLM 与循证中医整合（Scoping Review）** PRISMA scoping review，纳入 12 篇（2022-11 至 2026-01），覆盖 LLM 循证中医的证据生成、合成与转化 [University of Geneva，中国医学科学院，Gansu University of Traditional Chinese Medicine，Lanzhou University] [[DOI](https://doi.org/10.1016/j.imr.2026.101349)]
- [*Journal of Pharmaceutical Analysis*] **Xu et al. 2026: 基于 LLM 的中医智能问答系统综述** 中医智能问答系统谱系综述（KG-QA→LLM-QA、RAG） [天津大学，Tianjin haihe hospital] [[DOI](https://doi.org/10.1016/j.jpha.2025.101406)]
- [*Engineering*] **XiangShu Omics: A Framework Based on the Spatio–Temporal Field Rhythms of Human Life and Systems Intelligence Methodology** 这篇综述首次系统提出象数组学，并写道其大模型按理、法、方、药的经典治疗逻辑整合大语言模型，例如数智岐黄。 [[DOI](https://doi.org/10.1016/j.eng.2026.02.018)]
- [*Artificial Intelligence Review*] **Wu et al. 2026: AI 在中药材中的应用综述** 中药学×AI 全栈 survey（成分、靶点、质控，含 LLM 一节） [Northeastern University，First Hospital of China Medical University，China Medical University，Liaoning University] [[DOI](https://doi.org/10.1007/s10462-026-11513-w)]
- [*Medical Review*] **Wang et al. 2026: 重思中医大模型评测** 指出中医大模型评测仍缺少质量底线：未筛选古籍和网页语料可能含过时或禁用建议，单病例基准也不足以代表临床 [北京中医药大学] [[DOI](https://doi.org/10.1515/mr-2026-0006)]
- [*Chinese Medicine*] **Wang et al. 2026: 人工智能在中医药研发中的发展与应用综述** 2026年1月8日发表于 Chinese Medicine 的综述，梳理人工智能在中药研发设计、制药过程与市场准入等环节的应用与局限，并讨论与新兴技术结合的方向。 [[DOI](https://doi.org/10.1186/s13020-025-01288-7)] [[论文](https://link.springer.com/article/10.1186/s13020-025-01288-7)]
- [*Chinese Herbal Medicines*] **Sun et al. 2026: 生成模型在中医药中的进展与应用** 综述生成模型在中医药中的进展与应用 [[DOI](https://doi.org/10.1016/j.chmed.2026.08.013)]
- [*Information*] **Lu et al. 2026: 深度学习中医诊断方法学质量审计** 系统综述+验证缺口分析：DL 中医疾病诊断研究的方法学质量与临床转化 [香港中文大学] [[DOI](https://doi.org/10.3390/info17060554)]
- [*ACL 2026*] **LLM-Based Multi-Agent Systems for Clinical Workflows（ACL 2026，邻近）** 工作流级多智能体综述+四层评测栈（safety/process/outcome/operations）；无TCM交集但过程评测主张方法学同构（邻近） [Sanford Health，University of Massachusetts Lowell，University of Massachusetts Amherst] [[DOI](https://doi.org/10.18653/v1/2026.acl-long.2123)]
- [*Chinese Medicine*] **Han et al. 2026: LLM 在中医中的调优与临床应用（Scoping Review）** PRISMA-ScR scoping review，纳入 27 篇（至 2025-05），聚焦 LoRA/CPT/RAG 调优配方与临床应用统计 [中国医学科学院，Jining Traditional Chinese Medicine Hospital，中国中医科学院，北京中医药大学] [[DOI](https://doi.org/10.1186/s13020-026-01346-8)]
- [*Chinese Medicine*] **Guo et al. 2026: AI 与多模态数据融合推动中医现代化** AI 全景综述（ML/DL/KG/NLP/LLM），LLM 为一节，附多尺度数据资源与平台编目 [Ningbo College of Health Sciences，Shenzhen Second People's Hospital，Hunan University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1186/s13020-025-01194-y)]
- [*Chinese Medicine and Culture*] **From Empirical Wisdom to Computational Intelligence: A Knowledge-Data Dual-Driven Paradigm for Modernizing Traditional Chinese Medicine** 该文提出知识与数据双驱动范式：用大规模知识图谱和中医专用大语言模型把隐性经验变成可计算结构，并把四诊数字化为多模态中医表型。 [[DOI](https://doi.org/10.1097/mc9.0000000000000198)]
- [*Science of Traditional Chinese Medicine*] **Dong et al. 2026: 中医处方推荐计算方法综述** 综述从临床数据学习处方规律的计算方法，覆盖智能处方推荐如何支持中医临床决策 [南京中医药大学，北京交通大学] [[DOI](https://doi.org/10.1097/st9.0000000000000110)]
- [*Journal of Integrative Medicine*] **Deep learning in TCM（J Integr Med）** 深度学习单技术线综述：医学影像、药材物质研究、数据挖掘等应用实例（J Integr Med 2026;24(4):471-480） [天津大学] [[DOI](https://doi.org/10.1016/j.joim.2026.03.001)]
- [*OSF Registries*] **Cong H et al. 中医古籍知识挖掘范围综述（OSF 预注册）** 2026 年 4 月 15 日在 OSF 登记的一份范围综述计划，准备梳理知识图谱、大模型和两者结合的框架怎样从中医古籍里整理知识。综述还在做。 [[DOI](https://doi.org/10.17605/osf.io/5z367)]
- [*Science of Traditional Chinese Medicine*] **Chen et al. 2026: LLM 在中医的下一步（叙述性综述）** 叙述性前瞻：多模态、Agent 与临床落地路线 [北京中医药大学] [[DOI](https://doi.org/10.1097/st9.0000000000000109)]
- [*OSF Registries*] **Cai R et al. 中医辨证分类范围综述（OSF 预注册）** 2026 年 4 月 3 日在 OSF 登记的一份范围综述计划，准备梳理大模型怎样做中医辨证、证素和辨证推理，并按 PRISMA-ScR 来写。综述还在做。 [[DOI](https://doi.org/10.17605/osf.io/2hyeq)]
- [*Intelligence-Based Medicine*] **Artificial intelligence: A catalyst for the modernization of traditional Chinese medicine** 这篇范围综述检索PubMed、Web of Science和中国知网截至2025年的文献，并写道深度学习和大语言模型在舌象分析与辨证上表现有前景，部分研究接近专家水平。 [[DOI](https://doi.org/10.1016/j.ibmed.2026.100415)]
- [*Journal of Advanced Research*] **AI-driven multi-scale target analysis of traditional Chinese medicine: From the pharmacological effects of single compounds to the synergistic mechanisms of formulae** 这篇中药多尺度靶点分析综述把研发面向中医的专用大语言模型列为未来方向，用来解码中药的药理逻辑。 [[DOI](https://doi.org/10.1016/j.jare.2026.03.050)]
- [*Pharmacological Research - Modern Chinese Medicine*] **AI in TCM: multimodal data to pharmacology and clinical decision（PRMCM 综述）** 一篇英文综述，从多模态数据、药理研究写到临床决策。2026 年发表在 Pharmacological Research - Modern Chinese Medicine。 [Saveetha University] [[DOI](https://doi.org/10.1016/j.prmcm.2026.100842)]
- [*Research*] **AI in TCM: Unraveling Herbal Medicine's Mechanisms（Research）** 主张AI从相关分析范式走向重建证候辨证与方剂配伍生物逻辑的药材机制中心宽口径综述（Research 2026;9:1224） [Zhejiang Chinese Medical University] [[DOI](https://doi.org/10.34133/research.1224)]
- [*Journal of Integrative Medicine*] **AI empowers the innovation of TCM（J Integr Med 评论）** 单作者评论性综述：古籍挖掘、诊疗标准化、药物研发周期三痛点×AI（J Integr Med 2026） [上海中医药大学] [[DOI](https://doi.org/10.1016/j.joim.2026.05.004)]
- [*Chinese Medicine and Culture*] **AI and Big Data in TCM Standardization and Internationalization（Chin Med Cult）** 谈人工智能和大数据怎样帮助中医做标准化、走到国际上去。刊在 Chinese Medicine and Culture 2026 年第 9 卷第 3 期。 [南洋理工大学] [[DOI](https://doi.org/10.1097/mc9.0000000000000203)]
- [*Science of Traditional Chinese Medicine*] **2026: 面向中医药证据知情决策的数字智能循证** 讨论如何用数字智能循证方法，把辨证论治推进到证据知情的中医药决策 [兰州大学，University of Geneva] [[DOI](https://doi.org/10.1097/st9.0000000000000105)]
- [*Science of Traditional Chinese Medicine*] **2026: 数字化与智能化时代的中医药机遇与挑战** 从专家系统到深度学习和大语言模型，讨论数字化、智能化给中医药带来的机遇与挑战 [中国中医科学院] [[DOI](https://doi.org/10.1097/st9.0000000000000102)]
- [*Digital Chinese Medicine*] **2026: 中医智能诊断的跨学科融合与发展趋势** 讨论中医智能诊断的跨学科融合与发展趋势 [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.001)]

</details>

<details>
<summary>2025 · 29</summary>

- [*Frontiers in Medicine*] **Hou et al. 2025: Artificial intelligence in acupuncture: bridging traditional knowledge and precision integrative medicine** 辽宁中医药大学针灸推拿学院侯国梁、董宝强、于本祥、戴建宇、林星星、程泽忠在 Frontiers in Medicine 发表综述，整理人工智能用于针灸疗效预测及相关技术的进展，覆盖深度学习、元分析建模、自然语言处理、计算机视觉和神经影像分析等，并举卷积神经网络用于舌象分类与证型识别、基于 Transformer 的模型从经典文献中自动抽取临床知识等例子。作者讨论数据有限且异质、标注不一致和临床验证不足，并建议建设联邦多模态数据平台、可解释框架和开放科学实践。期刊页标注文章类型为 Review，在线 2025年7月15日、发表 2025年7月31日，刊于第12卷。本次打开了 Frontiers 官方全文页并下载了官方 PDF。这是综述，不是新模型发布。 [Liaoning University of Traditional Chinese Medicine] [[论文](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2025.1633416/full)] [[PDF](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2025.1633416/pdf)] [[DOI](https://doi.org/10.3389/fmed.2025.1633416)]
- [*协和医学杂志*] **陈子佳 et al. 2025: 大语言模型在中医药领域的应用、挑战与前景** 综述大语言模型与中医四诊合参、辨证诊疗和复方研究的结合，并讨论价值风险、可解释性、技术短板与政策准入等挑战。 [中国中医科学院] [[DOI](https://doi.org/10.12290/xhyxzz.2024-0315)] [[论文](https://xhyxzz.pumch.cn/article/doi/10.12290/xhyxzz.2024-0315)]
- [*Pharmaceuticals*] **评估药物–草药相互作用的人工智能工具** 综述用人工智能模型评估药物和草药相互作用的工具。 [[DOI](https://doi.org/10.3390/ph18030282)]
- [*iScience*] **计算机辅助穴位定位系统综述** 系统综述用传统算法和深度学习在不同解剖区域做穴位定位的研究，并讨论效果和限制。 [[DOI](https://doi.org/10.1016/j.isci.2025.113708)]
- [*Chinese Medicine*] **肿瘤治疗中的草药–化学药相互作用** 综述肿瘤患者联用草药和抗癌药时的相互作用，包括药效、药代机制和风险预测。 [[DOI](https://doi.org/10.1186/s13020-025-01156-4)]
- [*Chinese Medicine*] **深度学习穴位定位综述** 按身体部位、网络结构、定位策略和图像模态，综述深度学习穴位定位的数据集、指标和适用场景。 [[DOI](https://doi.org/10.1186/s13020-025-01173-3)]
- [*中华中医药学刊*] **杨乐乐 et al. 2025: 大语言模型在中医药领域的应用展望思考** 梳理医学大语言模型发展脉络，展望其在中医药研究、知识挖掘与辅助诊疗中的应用，并讨论风险、对策与发展方向。 [中国中医科学院中医药信息研究所，Leipzig University] [[DOI](https://doi.org/10.13193/j.issn.1673-7717.2025.02.004)]
- [*中华中医药学刊*] **叶桦 et al. 2025: 大语言模型赋能中医药传承：前沿进展与应用展望** 2025年11月11日网络首发的中文综述，系统梳理大语言模型在中医药数据挖掘、临床辅助决策与文化传承中的研究进展、挑战与展望。期刊页未提供DOI。 [成都中医药大学智能医学学院，成都中医药大学基础医学院] [[论文](https://zyhs.cbpt.cnki.net/portal/journal/portal/client/paper/3e19461f3fb08c22b2659ea83eb41d5a)]
- [*Chinese Medicine*] **古籍知识图谱×多智能体融合综述（Chin Med）** 古籍KG构建（术语统一、数据标准化）挑战-展望型综述，首次把multi-agent写入中医古籍议题（Chin Med 2025;20:168） [北京大学] [[DOI](https://doi.org/10.1186/s13020-025-01226-7)]
- [*智能系统学报*] **医疗领域的大型语言模型综述（智能系统学报，邻近）** 中文医疗LLM通用综述（训练流程/策略/场景/挑战），与中医LLM综述圈属母子集关系（邻近） [[DOI](https://doi.org/10.11992/tis.202405003)]
- [*智能系统学报*] **医学大语言模型的研发与应用系统综述（智能系统学报，邻近）** 系统综述129个医学专用LLM（截至2024-06）+4类临床应用研究；系统检索协议方法学可比（邻近） [[DOI](https://doi.org/10.11992/tis.202410020)]
- [*上海中医药杂志*] **刘嘉艺 et al. 2025: 生成式人工智能在中医药标准化研究中的应用前景与挑战** 综述生成式人工智能在中医药健康服务、质量提升、信息管理与智能诊疗等标准化相关场景中的应用现状、前景与挑战。 [兰州大学，中国中医科学院中医临床基础医学研究所，广东省中医院] [[DOI](https://doi.org/10.16305/j.1007-1334.2025.z20241121005)] [[论文](https://shzyyzz.shzyyzz.com/zh/article/doi/10.16305/j.1007-1334.2025.z20241121005/)]
- [*中华中医药学刊*] **人工智能实现中医四诊的发展现状、问题及解决路径（中华中医药学刊）** 从望、闻、问、切看人工智能做中医四诊走到哪。望诊用摄像头拍面、舌、舌下、唇和眼睛，结合分割和颜色模型做量化；闻诊采集异常声音和气味，用神经网络和电子鼻做分析。刊在《中华中医药学刊》2025年第43卷第11期。 [[论文](https://www.sinomed.ac.cn/article.do?ui=2026106036)]
- [*AI Medicine*] **Zhang et al. 2025: 中医 LLM 短综述与展望** 短 survey+展望，TCM LLM 模型与任务速览 [Northeastern University] [[DOI](https://doi.org/10.53941/aim.2025.100003)]
- [*Journal of Evidence-Based Medicine*] **Yip et al. 2025: 中西医结合 LLM 进展与挑战** 综述：LLM 在整合医学（中西医结合）中的进展、挑战与机遇 [Hong Kong Baptist University，Guangdong-Hongkong-Macau Joint Laboratory of Collaborative Innovation for Environmental Quality] [[DOI](https://doi.org/10.1111/jebm.70031)]
- [*Acta Materia Medica*] **Yin et al. 2025: 数据挖掘、大模型与多模态融合的中医AI综述** 从数据挖掘、大语言模型和多模态融合三条线综述人工智能如何解析中药复方的多成分、多靶点机制 [浙江大学] [[DOI](https://doi.org/10.15212/amm-2025-0045)]
- [*American Journal of Chinese Medicine*] **Wang et al. 2025: AI 驱动中医诊断模型进展** 综述：AI 诊断模型（四诊客观化、辨证） [清华大学，南京大学] [[DOI](https://doi.org/10.1142/S0192415X25500259)]
- [*Journal of Pharmaceutical Analysis*] **The integration of machine learning into TCM（J Pharm Anal）** 机器学习×中医整合综述：诊断客观化与机制阐释两条线（J Pharm Anal 2025;15(8):101157） [Hangzhou Normal University] [[DOI](https://doi.org/10.1016/j.jpha.2024.101157)]
- [*American Journal of Chinese Medicine*] **Shataer et al. 2025: LLM 在中医应用（State-of-the-Art Review）** 叙述性综述，扫描 TCM LLM 应用场景（诊疗、教育、翻译、科研） [Centre for Intelligent Healthcare, Coventry University, Coventry CV1 5RW, UK] [[DOI](https://doi.org/10.1142/S0192415X25500375)]
- [*Journal of Evidence-Based Medicine*] **Ren et al. 2025: 中医大语言模型（Scoping Review）** Arksey–O'Malley scoping review，纳入 29 篇（至 2024-04），覆盖知识管理、辅助诊疗与考试准确率 [成都中医药大学，中国医学科学院，Institute of Health Data Science Lanzhou University Lanzhou China，Institute of Global Health University of Geneva Geneva Switzerland] [[DOI](https://doi.org/10.1111/jebm.12658)]
- [*Pharmacological Research*] **Meng et al. 2025: 大模型+虚拟细胞助力中医变革** 综述：大模型与虚拟细胞用于中风方药现代分析 [Northeastern University，Shenyang Medical College] [[DOI](https://doi.org/10.1016/j.phrs.2025.107953)]
- [*Science of Traditional Chinese Medicine*] **Liu et al. 2025: 网络药理学推动大模型用于中医药研究** 综述网络药理学如何把药物—靶点—疾病网络与大语言模型结合起来，解释中药复方的多靶点机制 [清华大学] [[DOI](https://doi.org/10.1097/st9.0000000000000073)]
- [*Healthcare*] **Intelligent Question-Answering Systems in Healthcare（Healthcare，邻近）** 2018-2025医疗QA综述+CiteSpace计量，明确含中医方剂开发应用场景（邻近综述，非TCM专用） [Beijing Information Science & Technology University] [[DOI](https://doi.org/10.3390/healthcare13182269)]
- [*Journal of Evidence-Based Medicine*] **Guo et al. 2025: GPT 能否加速中医智能诊疗（综述+实证）** 综述+实证分析，讨论 GPT 适配中医诊疗的挑战与幻觉问题 [Xiyuan Hospital China Academy of Chinese Medicinal Sciences Beijing China，北京大学] [[DOI](https://doi.org/10.1111/jebm.70004)]
- [*Asia-pacific Journal of Convergent Research Interchange*] **Domestic and International Research Trends in Artificial Intelligence Applications in Korean Medicine: An Analysis from 2019 to 2025** 作者系统回顾了2019至2025年23项韩医人工智能研究（国内10篇、国际13篇），并指出近期工作越来越多使用大语言模型和其他生成式人工智能。 [[DOI](https://doi.org/10.47116/apjcri.2025.11.02)]
- [*Acupuncture and Herbal Medicine*] **Chen et al. 2025: 中医大语言模型系统综述** 系统综述，纳入 10 篇（至 2024 年中），聚焦生成任务证据 [天津大学，现代中药海河实验室，Italian National Institute of Health, Rome, Italy] [[DOI](https://doi.org/10.1097/HM9.0000000000000143)]
- [*Current Medical Science*] **Artificial Intelligence in Traditional Chinese Medicine: Multimodal Fusion and Machine Learning for Enhanced Diagnosis and Treatment Efficacy** 综述人工智能在中医诊断和治疗中的多模态融合与机器学习。 [[DOI](https://doi.org/10.1007/s11596-025-00103-6)]
- [*MedComm – Future Medicine*] **Artificial Intelligence in Traditional Chinese Medicine: Bridging Ancient Practice and Future Innovation** 该综述按“构建—应用—挑战—展望”分析中医大模型，并指出Qibo和MedChatZH等系统已经出现，但此前综述缺少对共同特征的综合分析。 [[DOI](https://doi.org/10.1002/mef2.70042)]
- [*Current Medical Science*] **AI for Spleen-Stomach Disorders in TCM（Curr Med Sci）** 单病种（脾胃病）KG+智能诊疗综述：「症状-证候-疾病-方剂」框架的知识工程化（Curr Med Sci 2025;45(6):1348-1357） [Hubei University of Chinese Medicine，Hubei Provincial Hospital of Traditional Chinese Medicine，Hospital Conde S. Januário，Union Hospital] [[DOI](https://doi.org/10.1007/s11596-025-00128-x)]

</details>

<details>
<summary>2024 · 7</summary>

- [*Engineering*] **系统论框架下整合人工智能与中医药整体物质基础研究（框架综述）** 曾敬其、贾晓斌通讯。发表于 Engineering 2024 年 40 卷第 9 期的框架性综述，提出用系统功能解码模型（SFDM）把人工智能接到中医药整体物质基础研究，整理自上而下五个维度与自下而上的要素—结构—功能路径，并展望“组分-证候”端到端模型与口服制剂 IVIVC 机理模型。这不是系统评价，两种技术方案在本文中没有实现和定量评测。许可为 CC BY-NC-ND 4.0。中文正式本 25 页。 [中国药科大学中药学院，中国药科大学天然药物活性组分与药效国家重点实验室] [[DOI](https://doi.org/10.1016/j.eng.2024.04.009)] [[论文](https://www.engineering.org.cn/engi/CN/10.1016/j.eng.2024.04.009)]
- [*中草药*] **萧文科 et al. 2024: 中医药大语言模型的关键技术与构建策略** 专论梳理中医药大模型的数据存储与处理、RAG、MoE、RLHF、知识蒸馏及训练评测方法，并提出面向中医药数据特点的构建策略与应用场景。 [成都中医药大学] [[DOI](https://doi.org/10.7501/j.issn.0253-2670.2024.17.001)] [[论文](http://www.tiprpress.com/zcy/article/pdf/20241701)]
- [*计算机工程与应用*] **苏尤丽 et al. 2024: 人工智能在中医诊疗领域的研究综述** 中文综述：专家系统→机器学习→深度学习三阶段中医 AI 诊疗发展与挑战 [[DOI](https://doi.org/10.3778/j.issn.1002-8331.2312-0400)]
- [*南京中医药大学学报*] **李欣桐 et al. 2024: 中医药领域大语言模型的研究进展与应用前景** 中文综述：中医药 LLM 研究过程、前沿技术（提示工程/RAG/RLHF）与应用前景 [[DOI](https://doi.org/10.14148/j.issn.1672-0482.2024.1393)]
- [*Computers in Biology and Medicine*] **Tian et al. 2024: 四诊机器学习综述** 望闻问切四诊的 ML 传感与模型综述 [Northeastern University，Ningbo University，辽宁中医药大学] [[DOI](https://doi.org/10.1016/j.compbiomed.2024.108074)]
- [*中国工程科学*] **Song et al. 2024: AI 辅助中医辨证关键问题与技术挑战** 战略研究综述：多模态数据融合、症状关联、证候量化与推理及中医药大模型关键问题 [Shanghai University of Engineering Science，Digital China Health (China)，Zhejiang Lab，中国医学科学院] [[DOI](https://doi.org/10.15302/J-SSCAE-2024.02.010)]
- [*Computer Materials & Continua*] **Qu et al. 2024: 中医知识图谱综述** 中医知识图谱的分析、构建、应用与展望 [中国医学科学院，Beijing Forestry University] [[DOI](https://doi.org/10.32604/cmc.2024.055671)]

</details>

<details>
<summary>2023 · 3</summary>

- [*Chinese Medicine*] **中医药与天然产物中的机器学习：现状与展望** Ma、Liu、Li 共同第一，Li 与 Wang 通讯。这是发表于 Chinese Medicine 的叙述性综述，回顾中医药与天然产物研究中的机器学习，介绍团队的冠心病证素模型，并提出把机器学习、中医理论和计算生物学结合起来的展望。不是系统评价，表中准确率来自被引文献。未见新代码或新数据。许可为 CC BY 4.0。 [中国中医科学院广安门医院，天津中医药大学] [[DOI](https://doi.org/10.1186/s13020-023-00741-9)] [[论文](https://cmjournal.biomedcentral.com/articles/10.1186/s13020-023-00741-9)]
- [*Annals of Translational Medicine*] **中医四诊人工智能研究现状与趋势的科学计量研究** Tian、Hongwu Wang 通讯等。发表于 Annals of Translational Medicine 2023 年 11 卷第 3 期的科学计量研究，用 Web of Science、VOSviewer 和 CiteSpace 分析中医四诊人工智能文献。正文写 2007–2022 年 136 篇有效研究，不是系统评价，也没有 PRISMA。许可为 CC BY-NC-ND 4.0。正式本 16 页，DOI 10.21037/atm-22-6431。与本站已有 surv-tian2024 不是同一篇。 [天津中医药大学健康科学与工程学院，华北理工大学中医学院，南京中医药大学研究生院，南京中医药大学附属医院高血压研究所] [[DOI](https://doi.org/10.21037/atm-22-6431)] [[论文](https://atm.amegroups.org/article/view/109099)]
- [*Current Opinion in Structural Biology*] **中药计算毒性研究小综述** 综述用计算方法研究中药毒性的工作。 [[DOI](https://doi.org/10.1016/j.sbi.2023.102588)]

</details>

<details>
<summary>2022 · 1</summary>

- [*Frontiers in Pharmacology*] **人工智能在补充替代医学中的应用：系统性范围综述** Chu、Youn 通讯等按 JBI 和 PRISMA-ScR 梳理人工智能在补充替代医学中的应用，检索三个英文库，终选 32 篇，主要涉及针灸、舌唇诊和草药。这是系统性范围综述，不是元分析。正文、流程图和表 1 的计数不完全一致。未见新代码或新数据。许可为 CC BY。 [仁川 Daecheong Public Health Subcenter，庆熙大学研究生院，圆光大学韩医学院，韩国韩医药振兴院，庆熙大学韩医学院预防医学科] [[DOI](https://doi.org/10.3389/fphar.2022.826044)] [[论文](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2022.826044/full)]

</details>

<details>
<summary>2021 · 2</summary>

- [*Frontiers in Pharmacology*] **人工智能、深度学习与云计算用于中西医诊治类风湿关节炎** Wang、Hou 共同第一，Zhang 与 Wang 通讯。这是发表于 Frontiers in Pharmacology 的叙述性综述，讨论人工智能、深度学习和云计算在传统医学与西医诊治类风湿关节炎中的应用设想，并给出概念模型。不是系统评价，也不是已实现的诊疗系统。未见新代码或新数据。许可为 CC BY。 [成都中医药大学民族医药学院，成都中医药大学药学院，成都市第二人民医院，西南特色中药资源国家重点实验室，成都中医药大学中医药创新研究院] [[DOI](https://doi.org/10.3389/fphar.2021.765435)] [[论文](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2021.765435/full)]
- [*Computers in Biology and Medicine*] **Zhang et al. 2021: 计算中医诊断文献综述** 计算化中医诊断的文献综述（症状采集、辨证建模与系统） [澳门大学] [[DOI](https://doi.org/10.1016/j.compbiomed.2021.104358)]

</details>

<details>
<summary>2020 · 1</summary>

- [*Artificial Intelligence in Medicine*] **Chu et al. 2020: 中医定量知识表示模型综述** 中医知识定量表示模型（本体、规则、统计）综述 [Xidian University，Xi'an Polytechnic University，Guangdong Polytechnic Normal University，CM Hospital] [[DOI](https://doi.org/10.1016/j.artmed.2020.101810)]

</details>

<details>
<summary>2019 · 1</summary>

- [*Engineering*] **中药安全性研究：方法、应用与展望** 综述中药不良反应为何难研究：成分复杂，药物和机体的相互作用也难事先判断，和化学药、生物药的毒性研究不是同一类问题。 [[DOI](https://doi.org/10.1016/j.eng.2018.11.019)]

</details>

<details>
<summary>2018 · 1</summary>

- [*Journal of Clinical and Translational Hepatology*] **中药肝损伤与药物性肝损伤的比较（叙述性综述）** Jing 与 Teschke 通讯。2018 年发表于 Journal of Clinical and Translational Hepatology 的叙述性综述，比较中药／草药性肝损伤与化学药物性肝损伤的流行病学、临床特征和 RUCAM 分级。不是系统评价，主要比较表转述既有队列。摘要与表 4、正文与表 6／图 2 存在文字和数字冲突。许可为 CC BY-NC 4.0。 [中国人民解放军医学院，解放军第302医院整合医学中心，哈瑙医院内科II消化与肝病科（歌德大学教学医院）] [[DOI](https://doi.org/10.14218/JCTH.2017.00033)] [[论文](https://www.xiahepublishing.com/ArticleFullText.aspx?sid=2&jid=1&id=10.14218%2fJCTH.2017.00033)]

</details>

<details>
<summary>2015 · 1</summary>

- [*Evidence-Based Complementary and Alternative Medicine*] **Zhao et al. 2015: 中医患者分类进展（ML 视角）** ML 驱动的中医病人/证候分类综述 [同济大学] [[DOI](https://doi.org/10.1155/2015/376716)]

</details>

<details>
<summary>2013 · 1</summary>

- [*Briefings in Bioinformatics*] **Gu & Chen 2013: 生物信息学遇见中医** 生物信息学×中医（组学、文本挖掘）历史综述 [浙江大学] [[DOI](https://doi.org/10.1093/bib/bbt063)]

</details>

<details>
<summary>2007 · 1</summary>

- [*Computer Methods and Programs in Biomedicine*] **Lukman et al. 2007: 中医计算方法综述** 计算方法（专家系统、ML、数据挖掘）全景，中医计算研究的方法学鼻祖 [University of Cambridge，University of Reading，南洋理工大学] [[DOI](https://doi.org/10.1016/j.cmpb.2007.09.008)]

</details>


</details>

## 专利

收中医大模型、知识图谱、RAG、智能问诊与处方推荐等系统专利，不限中国；不收中药组方、制剂专利全集。

<details>
<summary>73 件，按公开年收着</summary>

<details>
<summary>2026 · 33</summary>

- [*CN122531762A*] **基于生成式模拟医案构建的定制化中医处方推荐大模型** 用规则引擎穷举结构化中医特征，再由大语言模型写成模拟医案，并微调得到定制化处方推荐大模型（公开，未授权） [北京中医药大学] [[专利](https://patents.google.com/patent/CN122531762A/zh)]
- [*CN122529089A*] **基于大语言模型的中医对话生成方法及装置** 用长期记忆库与用户画像生成个性化中医对话（公开，未授权） [杭州旺柴科技] [[专利](https://patents.google.com/patent/CN122529089A/zh)]
- [*CN122508432A*] **一种面向中医药知识图谱的综合质量评估方法** 把小样本送入中医药微调大语言模型，做知识图谱质量预评估（公开，未授权） [湖北省标准化与质量研究院] [[专利](https://patents.google.com/patent/CN122508432A/zh)]
- [*CN122599028A*] **一种基于AI大模型的中医天地岁人四维辨证辅助诊疗系统** 结合多部位多压力脉象、时序节律编码与体质识别，生成中药和经络穴位推荐。2026年8月18日公开；原页显示Pending，仅为技术方案公开。 [Gaobele Biotech Guangzhou Co ltd] [[专利](https://patents.google.com/patent/CN122599028A/zh)]
- [*CN122436154A*] **张锡纯中医理法方药数字化传承与智能分析系统** 辨病辨证规则 + 三路检索 + LLM 融合，做张锡纯学派理法方药分析（公开，未授权） [广州知云草堂医疗科技] [[专利](https://eureka.patsnap.com/patent/CN122436154A)]
- [*CN122436116A*] **基于知识图谱与大语言模型的脾胃学派理法方药分析系统** 融合脾胃学派知识图谱、向量检索与大语言模型，完成选方验证、安全校验和处方生成（公开，未授权） [广州智韵草堂医学科技有限公司] [[专利](https://patents.google.com/patent/CN122436116A/zh)]
- [*CN122436251A*] **一种融合时空特征的针灸推理模型构建方法、系统及设备** 对齐四诊与病程的时空特征，检索历史针灸方案后，用微调大模型和思维链做针灸推理并三维展示（公开，未授权） [北京科技大学] [[专利](https://patents.google.com/patent/CN122436251A/zh)]
- [*CN121436110B*] **一种基于知识图谱的中医垂域大模型的训练方法** 以证候—症状词库、易混元组和上下文消歧整理预训练语料。A公开页时间线显示2026年7月31日授权并公布B文本；B正文此次未取得，技术摘要依据A公开文本。 [Daan Health Technology Beijing Co ltd] [[授权](https://patents.google.com/patent/CN121436110B/zh)] [[公开](https://patents.google.com/patent/CN121436110A/zh)]
- [*CN122364665A*] **一种基于大语言模型的中医古籍症状标准化处理方法** 用大语言模型从中医古籍切片识别候选症状，并映射到标准症状语义场完成术语标准化（公开，未授权） [黑龙江中医药大学] [[专利](https://patents.google.com/patent/CN122364665A/zh)]
- [*CN122135923A*] **辅助诊断结果和参考处方生成方法、装置、介质及计算机设备** 病历和诊疗思路各走向量与文本两路，四路召回后融合排序，由大模型生成中医诊断、证型、西医诊断和中药处方。2026年6月2日公开，尚未授权。 [浙江固生智能科技有限公司] [[专利](https://eureka.patsnap.com/patent/CN122135923A)]
- [*CN122245713A*] **基于大语言模型的中医智能问诊方法及系统** 从多模态问诊数据解析问诊意图，再用双路径检索中医知识，生成问诊结果（公开，未授权） [深圳市蓝宇飞扬科技有限公司] [[专利](https://patents.google.com/patent/CN122245713A/zh)]
- [*CN120913881B*] **基于多模态中医大语言模型的数据分析方法、系统、终端及介质** 用舌象、语音和问诊文本训练多模态中医大模型，输出初步中医分析。2026年6月12日授权。 [深圳心语心言智能技术有限公司] [[专利](https://eureka.patsnap.com/patent/CN120913881B)]
- [*CN122135936A*] **一种面向中医方剂推荐的知识图谱大模型问答方法及系统** 用中文指令大语言模型编码病历语义，与动态中医知识图谱的图向量做门控融合，推荐方剂并生成问答结果（公开，未授权） [北京科技大学] [[专利](https://patents.google.com/patent/CN122135936A/zh)]
- [*CN122025029A*] **融合类别信息与LLM的因果驱动对比学习与图注意力的中药处方推荐方法** 症状-草药异构/同构图 + LLM 增强因果机制做处方推荐（公开，未授权） [湖州师范学院] [[专利](https://eureka.patsnap.com/patent/CN122025029A)]
- [*CN122050861A*] **基于大模型结合双通道检索的中医智慧诊疗平台构建方法** LLM+中医知识图谱双通道检索，面向名医经验传承与处方生成（公开，未授权） [上海中医药大学附属岳阳中西医结合医院，上海市皮肤病医院] [[专利](https://patents.google.com/patent/CN122050861A/zh)]
- [*CN120913769B*] **基于多模态大模型的中医舌诊药饮推荐方法** 用大模型根据舌象生成病症描述并推荐药饮。2025年11月7日公开，2026年5月29日授权。 [天大智图（天津）科技有限公司，桂林电子科技大学] [[专利](https://patents.google.com/patent/CN120913769B/zh)]
- [*CN122117314A*] **一种基于大语言模型的智能针灸诊断Agent系统及诊断方法** 针灸知识库 + 图谱 + 向量检索 + 重排序，LLM 智能体分类问题并主动追问（公开，未授权） [河南工业大学] [[专利](https://eureka.patsnap.com/patent/CN122117314A)]
- [*CN121436111B*] **一种基于多模态数据融合的中医智能辨证模型训练系统及方法** 通过症状链、证候要素评分、证型逻辑组合与矛盾检测组织辨证推理。2026年5月15日授权，Google Patents显示Active；其权利要求侧重结构化推理，未据此认定公开了LLM权重。 [Daan Health Technology Beijing Co ltd] [[专利](https://patents.google.com/patent/CN121436111B/zh)]
- [*CN122091073A*] **一种基于多任务联合优化的中药处方生成方法与装置** 预训练大模型做自回归处方序列 + 草药集合预测，照顾低频药（公开，未授权） [杭州电子科技大学] [[专利](https://eureka.patsnap.com/patent/CN122091073A)]
- [*CN122050683A*] **一种基于图注意力网络与大语言模型的中药处方生成方法** 把中药处方生成转为多标签分类，用图注意力网络和大语言模型建模药物协同与禁忌。2026年5月15日公开。 [杭州市第一人民医院（西湖大学附属杭州市第一人民医院）] [[专利](https://patents.google.com/patent/CN122050683A/zh)]
- [*CN121862376A*] **基于知识图谱和大语言模型的中医辨证问答系统及方法** 古籍/医案分块抽实体建图谱，再按局部与全局关键词检索生成辨证问答（公开，未授权） [南京邮电大学] [[专利](https://patents.google.com/patent/CN121862376A/zh)]
- [*CN121687367A*] **基于结构化证据子图检索增强生成的中医草药推荐方法及系统** 多跳证据子图 + Hopfield 联想检索做草药推荐，并用图谱约束压幻觉（公开，未授权） [浙江中医药大学] [[专利](https://patents.google.com/patent/CN121687367A/zh)]
- [*CN121743505A*] **基于知识增强的中医医案按语生成方法及装置** 图谱子图混合检索后，按病因病机、治则、方药、预后四要素生成医案按语（公开，未授权） [浙江大学] [[专利](https://patents.google.com/patent/CN121743505A/zh)]
- [*CN121709160A*] **一种基于视觉语言模型的中医舌诊智能分析方法** 以Qwen-VL为舌诊视觉语言模型，经舌诊知识引导微调后，由舌象生成舌色、苔色等结构化结果及自然语言描述（公开，未授权） [中国计量大学] [[专利](https://patents.google.com/patent/CN121709160A/zh)]
- [*CN121480736A*] **基于知识蒸馏与强化学习的肿瘤中医智能处方推荐方法及系统** GPT-4o 教师蒸馏 Qwen 学生，再 DPO，做可解释的肿瘤中医处方（公开，未授权） [南京中医药大学] [[专利](https://patents.google.com/patent/CN121480736A/zh)]
- [*CN121524286A*] **一种心血管疾病的基于针灸诊疗知识图谱的智能问答系统** 构建心血管疾病针灸诊疗知识图谱，结构化查询结果交云端大语言模型润色；查不到时由大语言模型直接作答并提示仅供参考（公开，未授权） [天津中医药大学第一附属医院，江汉大学] [[专利](https://patents.google.com/patent/CN121524286A/zh)]
- [*CN121562809A*] **一种基于动态语义分块、知识图谱与多跳路径规划的中医大语言模型AI题库智能生成方法及系统** 对中医文本做语义分块和知识图谱多跳路径，再训练大语言模型生成中医题库（公开，未授权） [北京安戈普罗科技有限公司] [[专利](https://patents.google.com/patent/CN121562809A/zh)]
- [*CN121460056A*] **一种基于人工智能的方剂配制方法、系统、介质和设备** 用大语言模型从医案实体判定病名与证型并生成初步方剂，再由大语言模型评分，未达标则按结构化建议重新生成（公开，未授权） [中国计量大学] [[专利](https://patents.google.com/patent/CN121460056A/zh)]
- [*CN121460113A*] **一种基于中医语言大模型的中医智能分析方法及系统** 用LoRA微调得到中医语言大模型，按证型和主诉输出方剂（公开，未授权） [杭州轩岐智能科技有限公司，浙江中医药大学附属第三医院，北京航空航天大学] [[专利](https://patents.google.com/patent/CN121460113A/zh)]
- [*CN121393746A*] **基于大语言模型的经络辨证与针灸方案生成方法及系统** 把多源诊疗数据量化并提质后，结合经络辨证知识库和大语言模型生成针灸方案。2026年1月23日公开。 [广州双龙脉健康产业科技有限公司] [[专利](https://patents.google.com/patent/CN121393746A/zh)]
- [*CN121281871A*] **基于医学大语言模型多智能体的中医药临床数据自动化处理系统** 任务理解智能体、临床数据治理工具库和数据治理智能体协作，做中医疗效评价数据的结构化、标准化与流程生成。2026年1月6日公开；Google Patents显示Pending。 [四川大学华西医院] [[专利](https://patents.google.com/patent/CN121281871A/zh)]
- [*CN121331451A*] **一种融合舌象、心率及文本的多模态健康状态评估方法** 以舌象为主、结合心率和使用者自述文本，用提示词引导DeepSeek大模型生成健康状态评估（公开，未授权） [刘家豪] [[专利](https://patents.google.com/patent/CN121331451A/zh)]
- [*CN121436134A*] **一种多模态知识图谱构建方法及系统** 用大模型从中医药文本抽三元组，再融合真实病历层做成多模态图谱（公开，未授权） [杭州甘之草科技] [[专利](https://patents.google.com/patent/CN121436134A/zh)]

</details>

<details>
<summary>2025 · 25</summary>

- [*CN121210613A*] **基于检索增强生成的针灸大模型构建方法、系统及装置** 训练针灸大语言模型，问答请求做知识库向量检索后生成回答，诊断请求再检索针灸方案库给出治疗条目。2025年12月26日公开。 [北京科技大学] [[专利](https://patents.google.com/patent/CN121210613A/zh)]
- [*CN120690391B*] **一种基于知识图谱技术的中药经典名方智能推荐方法** 口语到术语的语义映射 + 体质过滤 + 多症状协同，推荐经典名方。2025年12月16日授权。 [顺福科技集团] [[专利](https://patents.google.com/patent/CN120690391B/zh)]
- [*CN121212280A*] **一种基于大语言模型的人-信息-物理三元数据融合中药制造知识图谱构建系统、电子设备及存储介质** 用大语言模型按中药术语和关系约束从制造文本抽取三元组，再按人-信息-物理本体构建中药制造知识图谱。2025年12月25日公开。 [北京中医药大学] [[专利](https://patents.google.com/patent/CN121212280A/zh)]
- [*CN121096596A*] **一种基于多模态大语言模型的中医临床辅助决策系统和方法** 融合舌象视觉特征与临床文本，检索相似病例后，由多模态大语言模型生成证候、诊断、中药处方和推理过程。2025年12月9日公开。 [清华大学深圳国际研究生院] [[专利](https://patents.google.com/patent/CN121096596A/zh)]
- [*CN121034544A*] **融合动态知识图谱的针灸大模型辨证方法及调理优化系统** 动态更新针灸知识图谱，结合患者时序临床特征，用图注意力和强化学习辨证并生成针灸方案。2025年11月28日公开。 [广东中科凯泽信息科技有限公司] [[专利](https://patents.google.com/patent/CN121034544A/zh)]
- [*CN120998428A*] **大小模型协同中药方剂优化方法、系统、终端及存储介质** 用方剂优化大语言模型给出宏观优化方，再用药效物质小模型溯源药材并调整组成，综合后形成最终方剂推荐。2025年11月20日公开，尚未授权。 [天津中医药大学] [[专利](https://patents.google.com/patent/CN120998428A/zh)]
- [*CN120809097A*] **基于大语言模型的中医五音疗疾个性化音乐生成系统及其构建方法** 先用大语言模型做中医辨证，再在五音特征约束下生成个性化五音治疗音乐。2025年10月17日公开。 [苏州昂升网络科技有限公司] [[专利](https://patents.google.com/patent/CN120809097A/zh)]
- [*CN120674039A*] **针灸穴位推荐方法及其模型获取方法、装置、设备及介质** 用病历对语言模型做初步训练，建立症状与针灸穴位的语义映射，再经参数微调与策略优化得到穴位推荐模型（公开，未授权） [河南工业大学] [[专利](https://patents.google.com/patent/CN120674039A/zh)]
- [*CN120337029A*] **一种基于大模型的中药分类方法** 对多源中药数据做实体识别并映射现代药理指标，再自适应微调预训练大模型完成中药分类。2025年7月18日公开。 [湖南省中医药研究院] [[专利](https://patents.google.com/patent/CN120337029A/zh)]
- [*CN120299726A*] **一种基于大模型智能体协作规划的中医诊断场景模拟方法** 把非结构化医案做成结构化知识，再用患者、医生、助手和专家几类大模型智能体协作，模拟中医诊断流程。2025年7月11日公开，尚未授权。 [华南理工大学] [[专利](https://eureka.patsnap.com/patent/CN120299726A)]
- [*CN120108651A*] **基于胸肺科中医问诊报告大语言模型的中医方剂推荐方法和系统** 用多知识域共享微调胸肺科中医问诊大语言模型，输出体质和症状参数，并推荐药食同源方剂。2025年6月5日公开。 [澳门科技大学] [[专利](https://patents.google.com/patent/CN120108651A/zh)]
- [*CN120108694A*] **基于知识图谱与医案增强RAG的中医智能问诊方法及系统** Leiden 子图检索 + 全局/本地混合召回，再由大模型统一生成问诊建议（公开，未授权） [江苏大学] [[专利](https://patents.google.com/patent/CN120108694A/zh)]
- [*CN120216657A*] **基于大语言模型的中药药物警戒问答系统的构建方法** 建立中药知识库并训练药物警戒检索增强模型PV-RAG，按自然语言提问生成中药安全回答。2025年6月27日公开。 [南京邮电大学] [[专利](https://patents.google.com/patent/CN120216657A/zh)]
- [*CN120221058A*] **基于多模态知识图谱与大语言模型的中医康复诊断系统** 舌苔、脉象与问诊特征对齐知识图谱嵌入，再交给中医康复专家大模型（公开，未授权） [浙江中医药大学] [[专利](https://patents.google.com/patent/CN120221058A/zh)]
- [*CN120067279B*] **基于AI大语言模型的中医智能问诊方法及系统** 面舌形体图像、语音气息与病症库融合的多模态问诊系统。2025年6月27日授权。 [医脉人工智能医疗科技（天津）] [[专利](https://patents.google.com/patent/CN120067279B/zh)]
- [*CN120148827A*] **一种基于大模型的心血管疾病医疗决策支持方法** 用预训练大模型融合中医证候知识和西医病理图谱，生成含西药、中医方剂和非药物干预的心血管决策方案。2025年6月13日公开，尚未授权。 [溧阳市中医医院] [[专利](https://eureka.patsnap.com/patent/CN120148827A)]
- [*CN119941636A*] **中医药多模态LLM训练方法及其应用** 分别提取舌苔与脉象特征，经跨模态注意力与文本特征融合后接入大语言模型，训练中医药多模态LLM。2025年5月6日公开。 [粤港澳大湾区精准医学研究院（广州）] [[专利](https://patents.google.com/patent/CN119941636A/zh)]
- [*CN119811630A*] **应用大语言模型的泌尿科中医问诊结果预测方法和系统** 用大语言模型从泌尿科中医问诊描述预测病灶核心关键词，并按反馈数据实时调整模型参数。2025年4月11日公开。 [中医药广东省实验室] [[专利](https://patents.google.com/patent/CN119811630A/zh)]
- [*CN119905208A*] **基于多源特征融合的中医方剂智能推荐方法、介质和设备** 融合内容推荐、协同过滤，并用大语言模型分析症状文本，按加权得分推荐个性化方剂（公开，未授权） [福建中医药大学] [[专利](https://patents.google.com/patent/CN119905208A/zh)]
- [*CN119763764A*] **一种基于大语言模型的中药处方推荐方法及系统** 软提示 + 交叉注意力把患者文本送进大模型，输出可控中药处方（公开，未授权） [杭州甘之草科技] [[专利](https://patents.google.com/patent/CN119763764A/zh)]
- [*CN119811698A*] **一种基于OCR识别和大模型的中药方数据解析方法及装置** 对手写中药方做OCR，把相冲、用量和服药建议拼成提示词送入大模型，生成处方综合判断。2025年4月11日公开。 [同力天合（北京）管理软件股份有限公司] [[专利](https://patents.google.com/patent/CN119811698A/zh)]
- [*CN119416782A*] **基于大语言模型的中医方学习方法、装置、设备及介质** 用 Qwen 等大模型对齐文言医案术语与白话，做名老中医方学习（公开，未授权） [成都字节流科技] [[专利](https://patents.google.com/patent/CN119416782A/zh)]
- [*CN119517372A*] **一种基于大语言模型的中医问答系统及方法** 从中医药文献构建数据集并训练大语言模型，接收用户医学问题后生成对话回答。2025年2月27日公开。 [郑新翰] [[专利](https://patents.google.com/patent/CN119517372A/zh)]
- [*CN119446558A*] **一种基于大语言模型的中医知识图谱生成方法及系统** 以中药和诊察治疗数据训练模型，按患者信息可视化输出治疗方案，并用疗效反馈继续更新模型。2025年2月17日公开。 [中国中医科学院中医药信息研究所] [[专利](https://patents.google.com/patent/CN119446558A/zh)]
- [*CN119252469A*] **一种用于智能中医系统的大语言模型的构建方法** 用舌诊图像标记和历史病历训练舌诊问诊模型，并据此构建用于智能中医系统的大语言模型。2025年1月7日公开。 [深圳问止中医健康科技有限公司] [[专利](https://patents.google.com/patent/CN119252469A/zh)]

</details>

<details>
<summary>2024 · 15</summary>

- [*CN119149754A*] **基于大模型和知识图谱的中医药方剂配伍方法及装置** 中医药大模型与知识图谱协同做方剂配伍（公开，未授权） [天津大学，天大智图（天津）科技] [[专利](https://patents.google.com/patent/CN119149754A/zh)]
- [*CN119069137A*] **利用AI大模型进行舌象分析的方法及装置** 在中医舌诊场景用AI大模型按体质、症状和综合解读做舌象分析（公开，未授权） [深圳伯德睿捷健康科技有限公司] [[专利](https://patents.google.com/patent/CN119069137A/zh)]
- [*CN119092157B*] **一种基于大语言模型的中药问答方法、装置、设备及介质** 在 Baichuan2-7B-Chat 上做中药问答。2025年2月7日授权。 [浙江大学，长三角智慧绿洲创新中心] [[专利](https://patents.google.com/patent/CN119092157B/zh)]
- [*CN119049664A*] **基于AI大模型的中医元气充盈智能健康管理系统** 把可穿戴数据转成中医术语后送入AI中医大模型（公开；2026-02-06已视为撤回） [重庆鼐龙生物科技有限公司] [[专利](https://patents.google.com/patent/CN119049664A/zh)]
- [*CN119049665A*] **基于AI大模型智能人体域网的中医六经辨证智能对话健康管理系统** 包含中医六经辨证术语大模型和对话式健康管理（公开；2026-02-06已视为撤回） [重庆鼐龙生物科技有限公司] [[专利](https://patents.google.com/patent/CN119049665A/zh)]
- [*CN118899077A*] **一种基于多模态大模型的中医舌诊分析系统及方法** 用云诊 TongueAI 生成舌面象解读、多轮问答和体质推理数据，指令微调得到 TongueLMM，用于舌诊解读、多轮问答和体质推理。2024年11月8日公开。 [合肥云诊信息科技有限公司] [[专利](https://patents.google.com/patent/CN118899077A/zh)]
- [*CN118838996A*] **基于大语言模型和知识图谱的中医药问答系统构建方法** LLM 生成与知识图谱补全闭环的中医药问答（公开，未授权） [北京理工大学，北京理工大学唐山研究院] [[专利](https://patents.google.com/patent/CN118838996A/zh)]
- [*CN118430833A*] **一种基于大语言模型的中医知识深度挖掘方法** 同时训练检索增强和模型微调，使系统既能解释中医名词和证候，也能按患者输入给出治疗方案（公开，未授权） [西南大学] [[专利](https://patents.google.com/patent/CN118430833A/zh)]
- [*CN117828050B*] **基于长文档检索增强生成的中医问答方法、设备及介质** 长文档 RAG（扩展、召回、重排序、来源标注）做中医问答。2024年4月5日公开，2024年7月9日授权。 [北京智谱华章科技] [[专利](https://patents.google.com/patent/CN117828050B/zh)]
- [*CN118280556A*] **一种基于计算视觉与大语言模型辅助中医诊疗的系统** 大语言模型处理语音问诊，计算机视觉把患者图像转成诊断信息，检索增强后作为大语言模型输入，辅助中医诊疗（公开，未授权） [深圳金草健康科技有限公司] [[专利](https://patents.google.com/patent/CN118280556A/zh)]
- [*CN118230893A*] **一种基于AI大模型的中医处方智能推荐方法和系统** 用病历训练 AI 大模型生成个性化中药处方，并接到医院信息系统（公开，未授权） [杭州甘之草科技] [[专利](https://patents.google.com/patent/CN118230893A/zh)]
- [*CN118098506A*] **一种基于大语言模型的针灸辅助诊疗和模型评价的方法** 用标注症状和穴位操作的数据微调ChatGLM3-6B，输出针灸方案，并用句子相似度评价生成结果（公开，未授权） [东北大学] [[专利](https://patents.google.com/patent/CN118098506A/zh)]
- [*CN118070907A*] **一种基于大语言模型的中医客服回复系统** 用同义词增广中医资料并训练Transformer大语言模型，微调后解析客户请求并生成回复；该申请于2024-07-09授权为CN118070907B [卓世智星（天津）科技有限公司] [[专利](https://patents.google.com/patent/CN118070907A/zh)]
- [*CN117786590A*] **以大语言模型为先验的智能中医系统** 用大语言模型优化患者诊断文本，再做语义理解，预测中医证候和病因并给出治疗建议。2024年4月1日公开。 [上海源庐加佳信息科技有限公司] [[专利](https://patents.google.com/patent/CN117786590A/zh)]
- [*CN117493579A*] **一种基于大语言模型的中医知识图谱构建方法** 用大语言模型从中医文本抽取命名实体和实体关系，按相似度融合后生成中医知识图谱（公开，未授权） [同济大学] [[专利](https://patents.google.com/patent/CN117493579A/zh)]

</details>


</details>

## 论文

这里只收方法、评测和系统论文。发布了领域大模型的条目在「开源模型」，不在这里重复。

<details>
<summary>Agent（20）：问诊流程、多智能体</summary>

<details>
<summary>2026 · 12</summary>

- [*Chinese Medicine*] **MAGR-TCM：知识图谱驱动的多智能体中医妇科居家问诊与分诊模型（Lv 等）** Lv、Pan、Li、Hu、Xu、Jin、Fang 等提出 MAGR-TCM，在专家监督下从 741 份高质量医案抽取知识图谱（文中称 10,231 个实体、32,051 条关系），并以四个智能体组成的检索增强生成框架，试图从口语化主诉重建中医“病–证–法–方–药”推理链，用于妇科居家健康咨询与分诊。作者报告该模型在 RAGAS 自动评估和专家人工评估中优于所比较基线，并在安全性测试集上达到 100% 敏感度与特异度；这些数字均为论文自报。这是面向居家场景的方法学与原型评估，不是临床疗效试验。本次打开了 Springer Nature / Chinese Medicine 论文页。 [安徽中医药大学医药信息工程学院，安徽中医药大学中医学院，安徽中医药大学中西医结合学院] [[DOI](https://doi.org/10.1186/s13020-026-01485-y)] [[论文](https://link.springer.com/article/10.1186/s13020-026-01485-y)]
- [*arXiv*] **Evidence-Based TCM Visualization Diagnosis System** 以症状—证候知识图谱、症状匹配和信息增益策略进行主动问诊，配合诊疗可视化；问诊策略展示以案例为主。 [[论文](https://arxiv.org/abs/2606.06869)]
- [*arXiv*] **DeepTCM1.0** 基于DeepSeek V3.2的11专家多智能体，解析中药复方机制（桂枝汤验证）；Research Square后上到arXiv [广州中医药大学，Chinese Medicine Guangdong Laboratory (Hengqin)，Changzhi Medical College] [[论文](https://arxiv.org/abs/2608.18103)] [[预印本](https://doi.org/10.21203/rs.3.rs-9844166/v1)]
- [*arXiv*] **DeepRoot** 多智能体把《神农本草经》建成可核验Neo4j图谱再做治疗推理，代码与评测脚本已开源 [[论文](https://arxiv.org/abs/2606.15931)] [[代码](https://github.com/CarlisleMa/deeprootv1)]
- [*Studies in Health Technology and Informatics*] **韩医CPX场景自动生成** 用大模型和检索增强，加上多模态临床线索，自动生成韩医标准化病人CPX场景并给出量化反馈；10名专家验证 [韩国韩医学研究院] [[DOI](https://doi.org/10.3233/shti260671)]
- [*arXiv*] **TCMScience** 中医科研发现智能体，把语言模型提案与执行、发布权限分开，避免不同证据类型混推 [[论文](https://arxiv.org/abs/2610.24601)]
- [*Journal of Pharmaceutical Analysis*] **TCM-Agent** 面向网络药理学与中药发现的 LLM 多智能体系统 [[论文](https://doi.org/10.1016/j.jpha.2026.101581)] [[代码](https://github.com/AITCM/TCM-Agent)]
- [*arXiv*] **MACAT** 多智能体文化感知翻译框架，实验覆盖中医经典与《论语》文化负载词英译 [[论文](https://arxiv.org/abs/2606.01276)]
- [*Applied Sciences*] **KM-Agent** 韩医/东亚传统医学工具增强Agent，检索4780条药材–证候–穴位元数据，并在TCMBench等上评测。MDPI/OpenAlex 署名圆光大学、釜山大学、东国大学等 [圆光大学，釜山大学等] [[论文](https://www.mdpi.com/2076-3417/16/7/3377)] [[代码](https://github.com/wonyung-lee/km-agent)]
- [*arXiv*] **DERM-3R** 资源受限下的中医皮肤病多模态多智能体框架（识别/表征/辨证论治三智能体） [[论文](https://arxiv.org/abs/2604.09596)]
- [*arXiv*] **CORE-Acu** 针灸临床决策：结构化推理轨迹与知识图谱安全否决闭环 [[论文](https://arxiv.org/abs/2603.08321)]
- [*Engineering Applications of Artificial Intelligence*] **AcuModel / AcuAgent** 结合 AcuModel、针灸知识图谱、语义路由与规则约束，进行主动追问和针灸推理；公开项目说明及样例，完整权重与训练数据需向作者申请。 [[DOI](https://doi.org/10.1016/j.engappai.2026.116139)] [[资料](https://github.com/mosheng555/AcuModel-And-AcuAgent)]

</details>

<details>
<summary>2025 · 7</summary>

- [*arXiv*] **经方 (Jingfang)** 多智能体中医问诊与辨证论治系统，结合十问歌引导问诊、证候判别模型和双阶段处方检索。 [[论文](https://arxiv.org/abs/2502.04345)]
- [*中医杂志*] **基于雅意大模型的中医智能预问诊** 刘奕清、李迎、杨洪军等用 DeepSpeed ZeRO-3 微调 YAYI 2-30B，并用症状关系带权无向图做智能体辨证。模拟测试里，执业医师题正确率 94.09%，执业中药师 78.00%，症状术语 87.50%，经络 68.80%。临床测试辨证准确率 88.33%，问诊轮次和时间少于主治医师。2025年第 66 卷第 9 期 895–900 页。 [中国中医科学院医学实验中心，中国科学院自动化研究所，天津中科闻歌科技有限公司，中国中医科学院中医基础理论研究所] [[DOI](https://doi.org/10.13288/j.11-2166/r.2025.09.005)] [[论文](https://link.cnki.net/doi/10.13288/j.11-2166/r.2025.09.005)]
- **仁术AI (RenShu-AI)** FastAPI + LangGraph 多智能体中医问诊系统，融合 GraphRAG 与 DeepSeek-TCM [[代码](https://github.com/yanlinPeng-code/RenShu-AI)]
- [*Information*] **中药化合物检索智能体** 中药化合物信息检索AI智能体系统 [郑州大学] [[DOI](https://doi.org/10.3390/info16070543)]
- [*Journal of King Saud University Computer and Information Sciences*] **DiagX-DT** 辨证排除式推理框架，结合思维链与外部中医知识库迭代剔除不合理证候选项 [[DOI](https://doi.org/10.1007/s44443-025-00123-1)]
- [*proceedings-article*] **An Intelligent TCM Diagnosis System with Localized LLMs and Modular Multimodal Reasoning Enhanced by RAG** 该本地部署系统用望、闻、问、切四个智能体，经模块化组件处理和多模态检索增强生成，把舌象、声音、脉象和症状交给中心推理模块生成诊断与健康建议。 [Hosei University，Fuzhou University，Hong Kong Polytechnic University，Beihang University] [[DOI](https://doi.org/10.1109/cyberscitech68397.2025.00061)]
- [*Neurocomputing*] **AcuGPT-Agent** 围绕针灸治疗不孕，结合专科大模型、知识图谱和跨知识库路由，并以 EvalAcu 评估知识与任务能力。 [南京中医药大学] [[DOI](https://doi.org/10.1016/j.neucom.2025.131116)]

</details>

<details>
<summary>2024 · 1</summary>

- [*대한한의학회지*] **Pilot Development of a 'Clinical Performance Examination (CPX) Practicing Chatbot' Utilizing Prompt Engineering** 作者把韩国韩医学研究院的标准化病人情景改写成文本，用角色提示和少样本提示调用GPT-4，做成韩医临床技能考试练习聊天机器人；内部评价中正确性和依从性较高，保密性和自然度仍需改进。 [Gachon University，Pusan National University] [[DOI](https://doi.org/10.13048/jkm.24013)]

</details>


</details>

<details>
<summary>多模态 / 四诊（37）：舌、面、脉</summary>

<details>
<summary>2026 · 17</summary>

- [*arXiv*] **Seeing Is Not Enough: Knowledge-Grounded Active Inquiry from Uncertain Visual Evidence** 牛津大学 Yucheng Liu 与中国科学院北京纳米能源与系统研究所 Everett X. Wang（通讯）提出，在中医舌诊中相似舌象可能对应不同证候，而关键症状并不出现在照片里，因此用舌象与脉象预测来引导针对性地问诊，并用获得的回答收窄证候清单后再报告。作者构建 2600 例由真实舌象照片、指定证候、模拟症状回答和生成脉象组成的病例，其中 2599 例进入来源不相交的五折评估。论文称在干净图像上，仅用舌象/脉象预测的细粒度证候准确率为 46.4%；在获取代价为 12 时，不问诊图像/脉象证据的问诊准确率为 34.4%，二者结合达到 65.8%，前三纳入率为 90.8%。本次打开了 arXiv 摘要页与真实 PDF（2610.38774，页面为 v2）。结果均为作者自报。 [University of Oxford，Beijing Institute of Nanoenergy and Nanosystems, Chinese Academy of Sciences] [[论文](https://arxiv.org/abs/2610.38774)] [[PDF](https://arxiv.org/pdf/2610.38774)]
- [*arXiv*] **acuSimNet: Multi-View Self-Occlusion-Awared Visibility Learning for Cranio-Cervical Acupuncture Points** 佐治亚理工学院马佳涛与德比大学孙启磊提出面向头颈部穴位多视角、自遮挡可见性预测的多任务网络 acuSimNet。论文称穴位由抽象原则定义而非清晰解剖标志，现有方法多为单视角或依赖相对位置推算，对自身、毛发或衣物遮挡关注不足；该工作在174个头颈部穴位的高维分类设定下训练，作者报告验证集准确率达99.97%，并将达到99%准确率的训练轮次从既有方法的约3000轮降至86轮。标题按原文保留 Awared 拼写。本次打开了arXiv摘要页（2611.20025，2026年11月15日提交）。结果均为作者自报。 [Georgia Institute of Technology，University of Derby] [[论文](https://arxiv.org/abs/2611.20025)] [[PDF](https://arxiv.org/pdf/2611.20025)]
- [*arXiv*] **SEAT: Sign-Type Evidence-Audited Transport for Multi-Label Tongue Diagnosis** 东北大学徐柳怡、王青、梁子凯、卢安阳与钱一宁（通讯，东北大学秦皇岛分校）提出面向多标签舌诊的证据审核框架 SEAT。论文称单张舌象常同时出现多种体征，证据类型包括局部形态、全局色度及标签共现，既有方法多用共享表征和统一多标签头，难以核验预测是否来自临床相关证据。SEAT 在冻结的 DINOv2 图像块特征上，分别用掩膜引导的体征特异注意力处理局部形态，用 LAB/HSV 颜色原型上的半松弛最优传输强化淡白舌识别，并用共现感知传输正则塑造批次级标签边际。作者报告在 TongueDx 基准上，六个随机种子的平均宏平均 F1 为 72.59（标准差 1.04），六模型集成达到 74.15。论文注明已投 IEEE。本次打开了 arXiv 摘要页与真实 PDF（2611.19748），并打开了作者给出的代码仓库页。结果均为作者自报。 [Northeastern University] [[论文](https://arxiv.org/abs/2611.19748)] [[PDF](https://arxiv.org/pdf/2611.19748)] [[代码](https://github.com/NEU-TCM-Lab/Sign-type-Evidence-Audited-Transport)]
- [*Frontiers in Medicine*] **Cracks-YOLO：结合可切换空洞卷积与 Transformer 的舌裂纹 YOLOv5 检测方法（Ding 等）** Ding、Wu、Shen、Lin、Men 针对舌裂纹形态、尺度和分布多变、既有检测精度与速度不足的问题，在 YOLOv5 骨干中引入可切换空洞卷积以调整感受野，并加入 Transformer 编码器以捕捉长程依赖，用于中医舌裂纹检测。这是目标检测方法论文；本次打开的摘要未在提取范围内给出完整定量结果，故不转写具体准确率。不是临床疗效试验。本次打开了期刊全文页。 [广州中医药大学医药信息工程学院，香港城市大学商学院] [[DOI](https://doi.org/10.3389/fmed.2026.1901533)] [[论文](https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1901533/full)]
- [*Health Information Science and Systems*] **ConsTCM: aligning fundus images with constitution differentiation in multimodal language model for Traditional Chinese Medicine** 天津大学纪翔宇、饶国政等提出 ConsTCM，用两阶段监督微调把眼底影像与中医体质辨识对齐到多模态语言模型：先在通用眼底检查数据上做基础微调，再以医院真实自标注病例做面向体质任务的特定微调，并混合已有分类任务与医院数据构建微调集。作者报告相对基线提升 5.6%，消融中相对基础模型在客观评估上提升 47%。期刊页标注在线 2026年4月6日，刊于 Health Information Science and Systems 2026年14卷1期文章号 50，封面日期 2026年12月。本次打开了 Springer 官方文章页。页面版权为版权所有、非开放获取，官方 PDF 链路返回的是 HTML 而非 PDF。指标均为作者自报。 [Tianjin University，Tianjin University of Traditional Chinese Medicine，La Trobe University，Institute of Science Tokyo] [[论文](https://link.springer.com/article/10.1007/s13755-026-00442-1)] [[DOI](https://doi.org/10.1007/s13755-026-00442-1)]
- [*BMC Medical Informatics and Decision Making*] **脉波与语音联合筛查冠心病和心衰** 上海中医药大学等把桡动脉脉搏波当作脉诊，把语音当作闻诊，用来筛查冠心病和心力衰竭。同步记了 553 人，包括健康人、冠心病和心衰，另有 194 人做外部验证。 [[DOI](https://doi.org/10.1186/s12911-026-03518-w)]
- [*Sensors*] **红外热像面部穴位两级定位** 按骨度分寸和中医解剖规则整理多姿态红外面部热像，先检测人脸，再回归穴位位置。 [[DOI](https://doi.org/10.3390/s26144498)]
- [*Journal of Traditional Chinese Medicine*] **空腹过程的寸关尺脉图定量** 51 名健康人在空腹前（第 0 天）、空腹中（第 4 天）和空腹后（第 7 天）采集左寸、右寸和右关脉图，比较与胃肠虚实有关的脉象参数。 [[DOI](https://doi.org/10.19852/j.cnki.jtcm.2026.02.019)]
- [*arXiv*] **白睛异常分割（HD-DinoMoE）** 中医目诊看白睛缺少定量。这篇用分层混合专家网络，在复杂拍摄条件下分割巩膜表面异常。 [[论文](https://arxiv.org/abs/2606.04888)]
- [*Medicine in Novel Technology and Devices*] **基于中医脉诊矩阵的客观脉象分析** 用中医脉诊矩阵做客观脉象分析。文章认为现有脉图定义不完整，客观化标准也不统一。 [[DOI](https://doi.org/10.1016/j.medntd.2026.100429)]
- [*IEEE Journ