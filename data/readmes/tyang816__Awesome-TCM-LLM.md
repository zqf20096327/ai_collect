# 🔥 开源中医模型、数据、论文、专利

**语言 / Language:** [中文](README.md) | [English](README_EN.md)

![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-green)  [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Stars](https://img.shields.io/github/stars/tyang816/Awesome-TCM-LLM?color=yellow)  ![Forks](https://img.shields.io/github/forks/tyang816/Awesome-TCM-LLM?color=blue&label=Fork) [![中文门户](https://img.shields.io/badge/中医资源-门户-blue)](https://tyang816.github.io/zh/projects/tcm/) [![Project](https://img.shields.io/badge/Project-tyang816.github.io-informational)](https://tyang816.github.io/projects/tcm/)

开源中医模型、数据、论文、专利精选，也带一点相关中文医疗。现在大概有 55 条新闻、113 个模型、71 篇综述、69 件专利、186 个数据集、386 篇方法论文。[欢迎补条目](CONTRIBUTING.md)。

[项目页](https://tyang816.github.io/projects/tcm/) · [中文项目页](https://tyang816.github.io/zh/projects/tcm/) · [Wiki](wiki/Home.md) · [主页](https://tyang816.github.io/zh/)

## 先看这里

真能下载复现的中医权重大概 16 个，都在[开源模型](#开源模型)里。新闻里医院、公司发的，多数没有公开权重，当不了实验底座。

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

同名不一定是同一个东西。「仲景」至少有 ZhongJingGPT 和 AAAI 那条 CMtMedQA；TCM-Eval 也不止一套。说不清时看 [Getting Started](wiki/Getting-Started.md)。

## 开源模型

上面是起步用的。要翻全部能下的权重，或只有论文/产品、通用中文医疗底座、闭源产品和日韩汉方/韩医，点开即可。

<details>
<summary>能下载的权重，共 16 个</summary>

| 模型 | 年 | 机构 | 特色 | 链接 |
| --- | :---: | --- | --- | --- |
| **知方丹台 (ZhiFangDanTai)** | 2026 | 首都师范大学 | RAG · 图谱 | [论文](https://arxiv.org/abs/2509.05867) · [权重](https://huggingface.co/tczzx6/ZhiFangDanTai1.0) · [数据](https://huggingface.co/datasets/tczzx6/ZhiFangDanTai1.0) |
| **杏核 (Xinghe)** | 2026 | Xinghe-TCM | 推理 · 古籍 | [权重](https://huggingface.co/zsyjsld/Xinghe1.2-9B) · [数据](https://huggingface.co/datasets/zsyjsld/neijing-sft-v1.2) |
| **仲景 (ZhongJing)** | 2026 | 福耀科技大学 | 专家知识引导的中医大模型 ZhongJingGPT。它把领域微调和认知心… | [论文](https://doi.org/10.26599/TST.2025.9010046) · [权重](https://huggingface.co/CMLM/ZhongjingGPT1_13B) · [代码](https://github.com/pariskang/CMLM-ZhongJing) |
| **中医体质 Qwen3-8B 量化权重** | 2026 | — | 面向中医体质的 Qwen3-8B 量化权重，仓库里有 q4、q5 和 q… | [权重](https://huggingface.co/chenhaodev/tcm-constitution-qwen3-8b-gguf) |
| **TCM-Qwen2.5-7B-SFT** | 2026 | — | 基于 Qwen2.5-7B 的中医监督微调权重，模型文件是完整的 saf… | [权重](https://huggingface.co/Xxiao2023/TCM-Qwen2.5-7B-SFT-V1) |
| **Qwen3.5-9B 中医继续预训练** | 2026 | — | Qwen3.5-9B 做完中医继续预训练后的全量权重，一个约 17.9… | [权重](https://huggingface.co/arthur789/qwen3.5-9b-tcm-cpt) |
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
<summary>只有论文或产品、没有核验权重的（51）</summary>

<details>
<summary>2026 · 16</summary>

- [*Digital Chinese Medicine*] **青囊 (QingNangTCM)** 基于 GLM-4-9B-Chat，以 P-Tuning v2 适配中医问答与临床推理；构建 100,000 条 QnTCM_Dataset 训练语料。 [河北北方学院] [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.002)]
- [*ISCTIS 2026*] **舌面多模态融合智能诊断** 舌-面多模态特征融合+LLM驱动的中医智能诊断 [厦门理工学院] [[DOI](https://doi.org/10.1109/ISCTIS70043.2026.11572361)]
- **砭石云中医** **砭石云中医**是智慧眼基于已备案砭石多模态大模型的中医方案，用症状到方药的知识图谱支持四诊采集和辅助辨证。 [智慧眼科技] [[官网](https://www.a-eye.cn/news_list/420.html)] [[网站](https://www.a-eye.cn/news_list/356.html)]
- **灵丹-V2 (Lingdan-V2)** Qwen3 4B/8B/14B 中医推理模型家族，依次进行续训、监督微调和处方 GRPO。作者仓库明确声明模型权重采用 Apache-2.0；第三方数据沿用原许可。 [北京交通大学] [[代码](https://github.com/TCMAI-BJTU/Lingdan-V2)] [[ModelScope](https://modelscope.cn/models/TCMAIBJTU/Lingdan-14B-R1)] [[论文](https://arxiv.org/abs/2610.14705)]
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
<summary>55 条，最近有：南京中医药大学发布灵素·艾护中医护理大模 · 广医·岐智2.0 · 首发首展</summary>

<details>
<summary>2026 · 22</summary>

- [2026.10] 报道称徐桂华团队10月9日发布灵素·艾护中医护理大模型，面向辨证施护、科研与居家康养，27所加盟医院为首批应用单位 [[链接](https://finance.sina.com.cn/jjxw/2026-10-10/doc-iniutqmk0582279.shtml)]
- [2026.09] 中国中医科学院广安门医院在2026服贸会展示**广医·岐智2.0**，以AI医生「安安」覆盖患者服务、临床诊疗、病房管理等六大场景 [[链接](https://app.xinhuanet.com/news/article.html?articleId=202609101de3e66a53f7474ba7d373deaaa7e122)]
- [2026.09] 2026服贸会中医药展区，北京中医药大学**首发首展**中医体质辨识体系与具身智能推拿机器人，同期还有智能诊脉设备体验 [[链接](https://wjw.beijing.gov.cn/xwzx_20031/mtjj/202608/t20260807_4812596.html)]
- [2026.09] 中新网报道方证大模型9月19日开放接入，覆盖临床辅助诊疗、科研数据挖掘和人才培养，并计划部署到龙华医院及医联体 [[链接](https://www.chinanews.com.cn/jk/2026/09-19/10699553.shtml)]
- [2026.08] 学校官网称，8月27日“黔小杏医疗大模型”在2026数博会发布，以中医药文献、名医经验和临床数据训练，用于辅助诊断、体质辨识、养生推荐和用药指导。 [[链接](https://www.gzy.edu.cn/info/1501/12735.htm)]
- [2026.08] 南方财经报道，广州中医药大学以通用大模型为基座、用约20亿词元中医药数据持续训练“杏林智慧教学大模型”，已在中医各家学说、中国医学史和中医外科学试点。 [[链接](https://m.21jingji.com/article/20260824/herald/ef692f3ceba10c36edd3952f4d5ca892.html)]
- [2026.07] 贵州医科大学等在中国—东盟教育交流周发布全国首个民族药创制全域智能平台**华族本草**，以数智岐黄+Qwen为底座融汇多民族医药古籍 [[链接](https://www.gmc.edu.cn/info/1058/30267.htm)]
- [2026.07] 新华网报道，2026年7月国家人工智能应用中试基地（医疗）在河南省人工智能大会集中发布中医经络辅诊模型、中西医结合食管癌大模型、中医药高质量数据集、中药研发大模型和名中医数字智能体。 [[链接](http://www.ha.xinhuanet.com/20260928/c8569fe1fbdb4ebc81053d86c6d93682/c.html)]
- [2026.07] 智慧眼携**砭石云中医**亮相WAIC 2026，以已备案砭石多模态大模型为底座，展示四诊仪与辅助诊疗系统 [[链接](http://www.eeo.com.cn/2026/0720/965556.shtml)]
- [2026.07] 安顿健康在WAIC 2026首发**七诊合参**中医机器人，集成面/红外面/舌/耳/闻/问/脉采集；报道称底座为2350亿参数的中医大模型。该页未写天回 [[链接](https://www.news.cn/finance/20260720/f6a8625c1be4412d9c311a232c7a35fa/c.html)]
- [2026.07] 上海中医药大学附属第七人民医院正式发布**岐元大模型**，采用预训练+领域微调+专家强化学习，支持生成式病历与名老中医Agent数字孪生，并亮相WAIC [[链接](https://dwgk.shutcm.edu.cn/2026/0725/c1890a175544/page.htm)]
- [2026.06] 中科闻歌通过港交所上市聆讯；报道提及与中国中医科学院合作的**大医金匮**中医大模型已通过中国信通院最高级别可信AI认证 [[链接](https://www.ncsti.gov.cn/kjdt/xwjj/202606/t20260610_249369.html)]
- [2026.05] 北京中医药大学中药学院称薪火中国药在世界数字教育大会发布，问答版已上线国家智慧教育公共服务平台 [[链接](https://zhongyao.bucm.edu.cn/yyxw/fb4b320d30c34e358de28a637c9f6f2c.htm)]
- [2026.04] 山东中医药大学附属医院启动山东省卫健委「人工智能＋」中医药重点场景**智汇岐黄**大模型项目 [[链接](http://ccpd.china.com.cn/2026-04/17/content_43401621.html)]
- [2026.04] 北京中医药大学牵头研发的**薪火中国药**中医药教育大模型通过国家生成式人工智能服务备案，成为国内首个获批面向公众服务的中医药领域大模型 [[链接](https://regional.chinadaily.com.cn/education/cn/2026-04/22/c_1177692.htm)]
- [2026.03] 中国中医药报报道，2026年3月17日研讨会上，中医药信息研究所所长李海燕介绍医源中医大模型已用于医案结构化、智能问诊、处方推荐和中成药合理使用等场景。 [[链接](https://www.cntcm.com.cn/content/202603/20/c501417.html)]
- [2026.03] 上海中医药大学称方证多模态大模型入选医疗领域国家人工智能应用中试基地阶段成果，基座为视觉语言模型 [[链接](https://kjrw.shutcm.edu.cn/2026/0330/c805a172392/page.htm)]
- [2026.02] 工信部等八部门印发《中药工业高质量发展实施方案（2026—2030年）》，明确运用人工智能与知识图谱赋能经典名方与名老中医经验方研发 [[链接](https://www.gov.cn/zhengce/zhengceku/202602/content_7057174.htm)]
- [2026.01] 新华网报道，2025年12月24日河南健康产业大会上，河南省卫生健康委展示中医经络辅助诊断模型和豫产豫药多模态神农本草大模型，后者用于药材识别、真伪鉴别、成分定量和产地溯源。 [[链接](http://www.ha.xinhuanet.com/20260105/b91d84bacd1c46389a007e0cc201962d/c.html)]
- [2026.01] 科技日报报道，1月9日广东省中医院启动名老中医辅助诊疗大模型矩阵；禤国维皮肤病诊疗大模型和心血管病诊疗大模型已投入临床。 [[链接](https://www.stdaily.com/web/gdxw/2026-01/12/content_460323.html)]
- [2026.01] 成都中医药大学官网称，温川飙团队牵头的“中医药AI模型高质量数据集”（项目编号2025-AISJK-02013）入选工信部与药监局2025年度人工智能医疗器械创新任务揭榜名单。 [[链接](https://www.cdutcm.edu.cn/info/1074/138321.htm)]
- [2026.01] 中医聪宝称素问中医内容生成大模型算法列入国家网信办第十四批深度合成服务算法备案 [[链接](https://www.tcmbrain.com/?list_43/180.html)]

</details>

<details>
<summary>2025 · 28</summary>

- [2025.12] **智明堂ZMT-M1**在国家中医执业医师资格考试模拟测试中以96.26分获得该领域最佳成绩，已在全国100余间诊室试点应用 [[链接](https://m.tech.china.com/redian/2025/1229/122025_1789291.html)]
- [2025.12] 广安门医院官网称广医·岐智取得国家级深度合成算法备案，并称是国内首家完成该项备案的中医院 [[链接](https://www.gamyy.cn/gzb/news/big/114632.html)]
- [2025.12] 固生堂发布“中医大脑”及国医大师施杞教授AI数字分身，已累计发布14位顶级专家数字分身。八大专科出自另一则十大分身报道，本页未写 [[链接](https://www.jjckb.cn/20251231/693ca93b14ff4f57adc359959dc0320d/c.html)]
- [2025.12] 吉林发布**众星·长白岐黄1.0** AI原生多模态中医药大模型 [[链接](https://www.chinanews.com.cn/cj/2025/12-20/10537422.shtml)]
- [2025.11] 北京科技大学新闻网称，2025年11月2日郑州大会上，学校联合郑州市卫健委、郑州市中医院和河南中医药大学数智中医药研究院发布岐黄针灸大模型，四诊采集后生成针灸处方。 [[链接](https://news.ustb.edu.cn/info/1087/72015.htm)]
- [2025.11] 国家卫健委等五部门印发《关于促进和规范”人工智能+医疗卫生”应用发展的实施意见》，明确支撑建设中医药诊疗大模型 [[链接](https://www.gov.cn/zhengce/zhengceku/202511/content_7047018.htm)]
- [2025.10] 中国经济网报道10月26日发布中西医结合高血压诊疗大模型Idiom-Hypertension，用于高血压规范管理 [[链接](https://www.ce.cn/cysc/yy/hydt/202510/t20251027_2541616.shtml)]
- [2025.10] 科技日报报道CTA在中医药临床疗效评价大会发布，基于Qwen2.5-14B微调，面向临床试验方案、数据管理与统计 [[链接](https://www.stdaily.com/web/gdxw/2025-10/21/content_418966.html)]
- [2025.09] 广安门医院官网称，2025年9月12日服贸会论坛发布广医·岐智2.0，并推出AI医生安安，已出现在门诊导诊屏和预问诊界面。 [[链接](https://www.gamyy.cn/gzb/news/big/113898.html)]
- [2025.09] **智赋岐黄天功**中医AI大模型通过国家深度合成服务算法备案，应用于中医四诊仪与体质辨识 [[链接](http://zs.scbzol.com/zs/2025/0919/328624.html)]
- [2025.09] 页面受评对象是**传神素问**中医大模型，获得可信AI中医药大模型4+级；正文写它由传神语联基于任度大模型打造 [[链接](https://zhongyi.gmw.cn/2025-09/10/content_38277329.htm)]
- [2025.09] 中原药谷基层中医药振兴工程下，**伊尹中医经典大模型**在嵩县发布启用，融合中医教育与AI辅助诊疗服务县域基层 [[链接](http://www.ha.xinhuanet.com/20250918/a3da94037689422dbcd1fe57fa62ef94/c.html)]
- [2025.09] 中国中医科学院官网称，2025年9月10日至14日服贸会上，其智能科学与工程技术研究中心展示大医金匮大语言模型与多轮问诊系统，以及舌诊仪和移动中医智能检测厅。 [[链接](https://www.cacms.ac.cn/news_dynamic/detail/5080.html)]
- [2025.08] 国家超算天津中心联合天津中医药大学等发布**天河·灵枢**2.0，由针灸专科扩展至20余科；同步启动中医药智能模型评价体系 [[链接](http://tj.people.com.cn/n2/2025/0809/c375366-41317410.html)]
- [2025.08] **固生堂**正式发布十大“国医AI分身”，基于国医大师及名中医临床经验构建。页面写专家模拟一致性达86%以上，不是辨证准确率 [[链接](http://sz.people.com.cn/n2/2025/0801/c202846-41310443.html)]
- [2025.08] 湖北日报报道，2025年8月6日湖北中医药大学、湖北时珍实验室与传神语联签约，以传神·素问中医大模型开展产学研用合作。 [[链接](https://news.hubeidaily.net/mobile/c_4393128.html)]
- [2025.07] 中国中医科学院广安门医院与多家医联体单位成立**广医·岐智大模型智能体联盟**，推进跨机构智能诊疗能力辐射 [[链接](https://www.gamyy.cn/gzb/news/big/112751.html)]
- [2025.06] 南京中医药大学人工智能与信息技术学院页面称，2025年6月6日发布灵山中医大模型（小杏仁）和素山中药大模型（素山智思体），分别服务中医临床教学科研和中药学教学科研。 [[链接](https://xxjs.njucm.edu.cn/2025/0529/c445a156198/pagem.htm)]
- [2025.06] 国家数据局收录成都中医药大学案例：用大模型对996册中医古籍做自动分词和实体识别，并基于ChatGLM-6B关联中医术语、构建穴位-脏腑等知识图谱。 [[链接](https://www.nda.gov.cn/sjj/ywpd/szkjyjcss/0618/20250618095629525611799_pc.html)]
- [2025.06] **中医横琴**垂类大模型正式发布 [[链接](https://www.stdaily.com/web/gdxw/2025-06/20/content_357526.html)]
- [2025.05] 北京中医药大学官网称，2025年5月10日发布薪火中国药智思体1.0，依托讯飞星火与DeepSeek，参数超700亿，面向助学、助教、助研、助管和国际合作。 [[链接](https://www.bucm.edu.cn/bzyyw/1c0b0fe535764fcc886c87b560caa0ee.htm)]
- [2025.05] 中国中医科学院发布中医药大模型评测标准 [[链接](https://www.news.cn/politics/20250510/5e6a0b4978b44b69b67dbfb7282fd220/c.html)]
- [2025.04] 传神语联发布**任度·素问**中医大模型，基于全自研混合熵(moH)技术架构，支持智能问诊、辨证分析、方剂推荐 [[链接](https://www.transn.com/about_us/consult/article/1924766101036437505)]
- [2025.04] 凤凰网报道，2025年4月11日华为云生态大会上，九为健康发布基于盘古大模型的九为神农中医大模型智能体，覆盖药物研发、复方优化和辅助诊疗。 [[链接](https://biz.ifeng.com/c/8iTNRXVw44k)]
- [2025.03] 中国中医科学院广安门医院28日正式发布**广医·岐智**中医大模型，成为国内首家本地化部署”算力+模型+应用”一体化服务的中医医院 [[链接](https://www.xinhuanet.com/tech/20250328/8b1685ad8c6f48c9bdc2add1658edac3/c.html)]
- [2025.03] 云诊科技官网称，公司基于自研舌诊多模态模型TongueLMM和DeepSeek-R1发布云诊华医大模型，用于辨证论治、体质辨识和诊疗报告生成。 [[链接](https://www.ai-tongue.com/pages/news/2025/04/9a6f1920-4819-406e-8d1f-6ba0b838a7f8.html)]
- [2025.03] 新华网报道，2025年3月13日南京中医药大学黄煌团队与杭州脉景健康发布黄煌经方AI辅助诊疗系统，用大语言模型与知识图谱把“方人相应”做成可计算诊疗流程。 [[链接](http://www.js.xinhuanet.com/20250314/aa816bb98d1041afa0fa7bca45583d1b/c.html)]
- [2025.01] 2025年1月8日，北京科技大学联合河南中医药大学发布张仲景中医药大模型1.0，功能包括智能辨证、证素推荐、经方应用和方药分析。 [[链接](https://news.ustb.edu.cn/info/1087/67760.htm)]

</details>

<details>
<summary>2024 · 4</summary>

- [2024.12] 招联消费金融联合中山大学、广州中医药大学深圳医院发布中医垂直大模型**仲思**，落地深圳多家社康中心智能问诊 [[链接](https://finance.sina.com.cn/jjxw/2024-12-16/doc-inczrzsp5791684.shtml)]
- [2024.11] 华东师范大学、上海中医药大学、华东理工大学、海军军医大学、临港实验室和华润江中一起做了**数智岐黄**。1.0 在 2024 年 1 月 19 日发布。2024 年 11 月 25 日，他们在上海一场论坛上介绍了 2.0。 [[链接](https://pharm.ecnu.edu.cn/08/27/c43775a657447/page.htm)]
- [2024.09] 中科闻歌发布**大医金匮**中医大模型及中医智能健康管理平台，基于1500余本中医典籍及海量临床医案训练 [[链接](https://36kr.com/newsflashes/2946967562099592)]
- [2024.05] 天士力与华为云联合发布**数智本草**大模型，基于盘古语言与药物分子模型。本页没有信通院4+级评估 [[链接](https://news.pharmnet.com.cn/news/2024/05/10/591622.html)]

</details>

<details>
<summary>2023 · 1</summary>

- [2023.07] 南京大经中医发布**岐黄问道·大模型**，基于千万级知识图谱与临床数据，面向医疗机构开放内测 [[链接](http://js.news.cn/20230729/fa034db71a00487b819a4ad95b44673e/c.html)]

</details>


</details>

## 综述

<details>
<summary>71 篇，按年收着</summary>

<details>
<summary>2026 · 35</summary>

- [*兰州大学学报(医学版)*] **从大语言模型到智能体（兰州大学学报医学版综述）** 以「大模型→智能体」演进为主线的中医临床辅助诊疗中文系统综述，梳理研究进展、关键问题与方向（兰州大学学报(医学版) 2026;52(4):49-57） [[DOI](https://doi.org/10.13885/j.issn.2097-681X.T20260032)]
- **Agentic and Knowledge-Grounded LLMs in TCM（预注册）** 2026 年 7 月在 OSF 登记的综述计划，准备从证据图谱、文本挖掘和能不能用到临床上，看中医里的智能体和带知识的大模型。综述还在做。 [[预注册](https://doi.org/10.17605/osf.io/kq8jx)]
- [*International Journal of Pattern Recognition and Artificial Intelligence*] **中医大模型关键技术综述（IJPRAI）** 系统综述中医大模型知识组织、辅助诊断与临床决策支持关键技术（World Scientific IJPRAI正式发表） [Guangdong Provincial Hospital of Traditional Chinese Medicine，Guangdong University Of Finances and Economics，Guangdong University of Finance] [[DOI](https://doi.org/10.1142/s0218001426590263)]
- [*Journal of Traditional Chinese Medical Sciences*] **AI驱动中医诊断智能化综述（JTCMS）** 综述多模态融合与大模型在中医四诊智能化中的应用、挑战与展望（JTCMS正式发表） [暨南大学，北京中医药大学] [[DOI](https://doi.org/10.1016/j.jtcms.2026.05.002)]
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
<summary>2025 · 24</summary>

- [*Pharmaceuticals*] **评估药物–草药相互作用的人工智能工具** 综述用人工智能模型评估药物和草药相互作用的工具。 [[DOI](https://doi.org/10.3390/ph18030282)]
- [*iScience*] **计算机辅助穴位定位系统综述** 系统综述用传统算法和深度学习在不同解剖区域做穴位定位的研究，并讨论效果和限制。 [[DOI](https://doi.org/10.1016/j.isci.2025.113708)]
- [*Chinese Medicine*] **肿瘤治疗中的草药–化学药相互作用** 综述肿瘤患者联用草药和抗癌药时的相互作用，包括药效、药代机制和风险预测。 [[DOI](https://doi.org/10.1186/s13020-025-01156-4)]
- [*Chinese Medicine*] **深度学习穴位定位综述** 按身体部位、网络结构、定位策略和图像模态，综述深度学习穴位定位的数据集、指标和适用场景。 [[DOI](https://doi.org/10.1186/s13020-025-01173-3)]
- [*Chinese Medicine*] **古籍知识图谱×多智能体融合综述（Chin Med）** 古籍KG构建（术语统一、数据标准化）挑战-展望型综述，首次把multi-agent写入中医古籍议题（Chin Med 2025;20:168） [北京大学] [[DOI](https://doi.org/10.1186/s13020-025-01226-7)]
- [*智能系统学报*] **医疗领域的大型语言模型综述（智能系统学报，邻近）** 中文医疗LLM通用综述（训练流程/策略/场景/挑战），与中医LLM综述圈属母子集关系（邻近） [[DOI](https://doi.org/10.11992/tis.202405003)]
- [*智能系统学报*] **医学大语言模型的研发与应用系统综述（智能系统学报，邻近）** 系统综述129个医学专用LLM（截至2024-06）+4类临床应用研究；系统检索协议方法学可比（邻近） [[DOI](https://doi.org/10.11992/tis.202410020)]
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
<summary>2024 · 5</summary>

- [*计算机工程与应用*] **苏尤丽 et al. 2024: 人工智能在中医诊疗领域的研究综述** 中文综述：专家系统→机器学习→深度学习三阶段中医 AI 诊疗发展与挑战 [[DOI](https://doi.org/10.3778/j.issn.1002-8331.2312-0400)]
- [*南京中医药大学学报*] **李欣桐 et al. 2024: 中医药领域大语言模型的研究进展与应用前景** 中文综述：中医药 LLM 研究过程、前沿技术（提示工程/RAG/RLHF）与应用前景 [[DOI](https://doi.org/10.14148/j.issn.1672-0482.2024.1393)]
- [*Computers in Biology and Medicine*] **Tian et al. 2024: 四诊机器学习综述** 望闻问切四诊的 ML 传感与模型综述 [Northeastern University，Ningbo University，辽宁中医药大学] [[DOI](https://doi.org/10.1016/j.compbiomed.2024.108074)]
- [*中国工程科学*] **Song et al. 2024: AI 辅助中医辨证关键问题与技术挑战** 战略研究综述：多模态数据融合、症状关联、证候量化与推理及中医药大模型关键问题 [Shanghai University of Engineering Science，Digital China Health (China)，Zhejiang Lab，中国医学科学院] [[DOI](https://doi.org/10.15302/J-SSCAE-2024.02.010)]
- [*Computer Materials & Continua*] **Qu et al. 2024: 中医知识图谱综述** 中医知识图谱的分析、构建、应用与展望 [中国医学科学院，Beijing Forestry University] [[DOI](https://doi.org/10.32604/cmc.2024.055671)]

</details>

<details>
<summary>2023 · 1</summary>

- [*Current Opinion in Structural Biology*] **中药计算毒性研究小综述** 综述用计算方法研究中药毒性的工作。 [[DOI](https://doi.org/10.1016/j.sbi.2023.102588)]

</details>

<details>
<summary>2021 · 1</summary>

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
<summary>69 件，按公开年收着</summary>

<details>
<summary>2026 · 29</summary>

- [*CN122531762A*] **基于生成式模拟医案构建的定制化中医处方推荐大模型** 用规则引擎穷举结构化中医特征，再由大语言模型写成模拟医案，并微调得到定制化处方推荐大模型（公开，未授权） [北京中医药大学] [[专利](https://patents.google.com/patent/CN122531762A/zh)]
- [*CN122529089A*] **基于大语言模型的中医对话生成方法及装置** 用长期记忆库与用户画像生成个性化中医对话（公开，未授权） [杭州旺柴科技] [[专利](https://patents.google.com/patent/CN122529089A/zh)]
- [*CN122508432A*] **一种面向中医药知识图谱的综合质量评估方法** 把小样本送入中医药微调大语言模型，做知识图谱质量预评估（公开，未授权） [湖北省标准化与质量研究院] [[专利](https://patents.google.com/patent/CN122508432A/zh)]
- [*CN122436154A*] **张锡纯中医理法方药数字化传承与智能分析系统** 辨病辨证规则 + 三路检索 + LLM 融合，做张锡纯学派理法方药分析（公开，未授权） [广州知云草堂医疗科技] [[专利](https://eureka.patsnap.com/patent/CN122436154A)]
- [*CN122436116A*] **基于知识图谱与大语言模型的脾胃学派理法方药分析系统** 融合脾胃学派知识图谱、向量检索与大语言模型，完成选方验证、安全校验和处方生成（公开，未授权） [广州智韵草堂医学科技有限公司] [[专利](https://patents.google.com/patent/CN122436116A/zh)]
- [*CN122436251A*] **一种融合时空特征的针灸推理模型构建方法、系统及设备** 对齐四诊与病程的时空特征，检索历史针灸方案后，用微调大模型和思维链做针灸推理并三维展示（公开，未授权） [北京科技大学] [[专利](https://patents.google.com/patent/CN122436251A/zh)]
- [*CN122364665A*] **一种基于大语言模型的中医古籍症状标准化处理方法** 用大语言模型从中医古籍切片识别候选症状，并映射到标准症状语义场完成术语标准化（公开，未授权） [黑龙江中医药大学] [[专利](https://patents.google.com/patent/CN122364665A/zh)]
- [*CN122135923A*] **辅助诊断结果和参考处方生成方法、装置、介质及计算机设备** 病历和诊疗思路各走向量与文本两路，四路召回后融合排序，由大模型生成中医诊断、证型、西医诊断和中药处方。2026年6月2日公开，尚未授权。 [浙江固生智能科技有限公司] [[专利](https://eureka.patsnap.com/patent/CN122135923A)]
- [*CN122245713A*] **基于大语言模型的中医智能问诊方法及系统** 从多模态问诊数据解析问诊意图，再用双路径检索中医知识，生成问诊结果（公开，未授权） [深圳市蓝宇飞扬科技有限公司] [[专利](https://patents.google.com/patent/CN122245713A/zh)]
- [*CN120913881B*] **基于多模态中医大语言模型的数据分析方法、系统、终端及介质** 用舌象、语音和问诊文本训练多模态中医大模型，输出初步中医分析。2026年6月12日授权。 [深圳心语心言智能技术有限公司] [[专利](https://eureka.patsnap.com/patent/CN120913881B)]
- [*CN122135936A*] **一种面向中医方剂推荐的知识图谱大模型问答方法及系统** 用中文指令大语言模型编码病历语义，与动态中医知识图谱的图向量做门控融合，推荐方剂并生成问答结果（公开，未授权） [北京科技大学] [[专利](https://patents.google.com/patent/CN122135936A/zh)]
- [*CN122025029A*] **融合类别信息与LLM的因果驱动对比学习与图注意力的中药处方推荐方法** 症状-草药异构/同构图 + LLM 增强因果机制做处方推荐（公开，未授权） [湖州师范学院] [[专利](https://eureka.patsnap.com/patent/CN122025029A)]
- [*CN122050861A*] **基于大模型结合双通道检索的中医智慧诊疗平台构建方法** LLM+中医知识图谱双通道检索，面向名医经验传承与处方生成（公开，未授权） [上海中医药大学附属岳阳中西医结合医院，上海市皮肤病医院] [[专利](https://patents.google.com/patent/CN122050861A/zh)]
- [*CN120913769B*] **基于多模态大模型的中医舌诊药饮推荐方法** 用大模型根据舌象生成病症描述并推荐药饮。2025年11月7日公开，2026年5月29日授权。 [天大智图（天津）科技有限公司，桂林电子科技大学] [[专利](https://patents.google.com/patent/CN120913769B/zh)]
- [*CN122117314A*] **一种基于大语言模型的智能针灸诊断Agent系统及诊断方法** 针灸知识库 + 图谱 + 向量检索 + 重排序，LLM 智能体分类问题并主动追问（公开，未授权） [河南工业大学] [[专利](https://eureka.patsnap.com/patent/CN122117314A)]
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
<summary>Agent（17）：问诊流程、多智能体</summary>

<details>
<summary>2026 · 9</summary>

- [*arXiv*] **DeepTCM1.0** 基于DeepSeek V3.2的11专家多智能体，解析中药复方机制（桂枝汤验证）；Research Square后上到arXiv [广州中医药大学，Chinese Medicine Guangdong Laboratory (Hengqin)，Changzhi Medical College] [[论文](https://arxiv.org/abs/2608.18103)] [[预印本](https://doi.org/10.21203/rs.3.rs-9844166/v1)]
- [*arXiv*] **DeepRoot** 多智能体把《神农本草经》建成可核验Neo4j图谱再做治疗推理，代码与评测脚本已开源 [[论文](https://arxiv.org/abs/2606.15931)] [[代码](https://github.com/CarlisleMa/deeprootv1)]
- [*Studies in Health Technology and Informatics*] **韩医CPX场景自动生成** 用大模型和检索增强，加上多模态临床线索，自动生成韩医标准化病人CPX场景并给出量化反馈；10名专家验证 [韩国韩医学研究院] [[DOI](https://doi.org/10.3233/shti260671)]
- [*arXiv*] **TCMScience** 中医科研发现智能体，把语言模型提案与执行、发布权限分开，避免不同证据类型混推 [[论文](https://arxiv.org/abs/2610.24601)]
- [*Journal of Pharmaceutical Analysis*] **TCM-Agent** 面向网络药理学与中药发现的 LLM 多智能体系统 [[论文](https://doi.org/10.1016/j.jpha.2026.101581)] [[代码](https://github.com/AITCM/TCM-Agent)]
- [*arXiv*] **MACAT** 多智能体文化感知翻译框架，实验覆盖中医经典与《论语》文化负载词英译 [[论文](https://arxiv.org/abs/2606.01276)]
- [*Applied Sciences*] **KM-Agent** 韩医/东亚传统医学工具增强Agent，检索4780条药材–证候–穴位元数据，并在TCMBench等上评测。MDPI/OpenAlex 署名圆光大学、釜山大学、东国大学等 [圆光大学，釜山大学等] [[论文](https://www.mdpi.com/2076-3417/16/7/3377)] [[代码](https://github.com/wonyung-lee/km-agent)]
- [*arXiv*] **DERM-3R** 资源受限下的中医皮肤病多模态多智能体框架（识别/表征/辨证论治三智能体） [[论文](https://arxiv.org/abs/2604.09596)]
- [*arXiv*] **CORE-Acu** 针灸临床决策：结构化推理轨迹与知识图谱安全否决闭环 [[论文](https://arxiv.org/abs/2603.08321)]

</details>

<details>
<summary>2025 · 7</summary>

- [*arXiv*] **经方 (Jingfang)** 多智能体中医问诊与辨证论治系统，结合十问歌引导问诊、证候判别模型和双阶段处方检索。 [[论文](https://arxiv.org/abs/2502.04345)]
- [*中医杂志*] **基于雅意大模型的中医智能预问诊** 刘奕清、李迎、杨洪军等用 DeepSpeed ZeRO-3 微调 YAYI 2-30B，并用症状关系带权无向图做智能体辨证。模拟测试里，执业医师题正确率 94.09%，执业中药师 78.00%，症状术语 87.50%，经络 68.80%。临床测试辨证准确率 88.33%，问诊轮次和时间少于主治医师。2025年第 66 卷第 9 期 895–900 页。 [中国中医科学院医学实验中心，中国科学院自动化研究所，天津中科闻歌科技有限公司，中国中医科学院中医基础理论研究所] [[DOI](https://doi.org/10.13288/j.11-2166/r.2025.09.005)] [[论文](https://link.cnki.net/doi/10.13288/j.11-2166/r.2025.09.005)]
- **仁术AI (RenShu-AI)** FastAPI + LangGraph 多智能体中医问诊系统，融合 GraphRAG 与 DeepSeek-TCM [[代码](https://github.com/yanlinPeng-code/RenShu-AI)]
- [*Information*] **中药化合物检索智能体** 中药化合物信息检索AI智能体系统 [郑州大学] [[DOI](https://doi.org/10.3390/info16070543)]
- [*Journal of King Saud University Computer and Information Sciences*] **DiagX-DT** 辨证排除式推理框架，结合思维链与外部中医知识库迭代剔除不合理证候选项 [[DOI](https://doi.org/10.1007/s44443-025-00123-1)]
- [*proceedings-article*] **An Intelligent TCM Diagnosis System with Localized LLMs and Modular Multimodal Reasoning Enhanced by RAG** 该本地部署系统用望、闻、问、切四个智能体，经模块化组件处理和多模态检索增强生成，把舌象、声音、脉象和症状交给中心推理模块生成诊断与健康建议。 [Hosei University，Fuzhou University，Hong Kong Polytechnic University，Beihang University] [[DOI](https://doi.org/10.1109/cyberscitech68397.2025.00061)]
- [*Neurocomputing*] **AcuGPT-Agent** 面向针灸治疗不孕的大模型智能系统 [南京中医药大学] [[DOI](https://doi.org/10.1016/j.neucom.2025.131116)]

</details>

<details>
<summary>2024 · 1</summary>

- [*대한한의학회지*] **Pilot Development of a 'Clinical Performance Examination (CPX) Practicing Chatbot' Utilizing Prompt Engineering** 作者把韩国韩医学研究院的标准化病人情景改写成文本，用角色提示和少样本提示调用GPT-4，做成韩医临床技能考试练习聊天机器人；内部评价中正确性和依从性较高，保密性和自然度仍需改进。 [Gachon University，Pusan National University] [[DOI](https://doi.org/10.13048/jkm.24013)]

</details>


</details>

<details>
<summary>多模态 / 四诊（26）：舌、面、脉</summary>

<details>
<summary>2026 · 11</summary>

- [*BMC Medical Informatics and Decision Making*] **脉波与语音联合筛查冠心病和心衰** 上海中医药大学等把桡动脉脉搏波当作脉诊，把语音当作闻诊，用来筛查冠心病和心力衰竭。同步记了 553 人，包括健康人、冠心病和心衰，另有 194 人做外部验证。 [[DOI](https://doi.org/10.1186/s12911-026-03518-w)]
- [*Sensors*] **红外热像面部穴位两级定位** 按骨度分寸和中医解剖规则整理多姿态红外面部热像，先检测人脸，再回归穴位位置。 [[DOI](https://doi.org/10.3390/s26144498)]
- [*Journal of Traditional Chinese Medicine*] **空腹过程的寸关尺脉图定量** 51 名健康人在空腹前（第 0 天）、空腹中（第 4 天）和空腹后（第 7 天）采集左寸、右寸和右关脉图，比较与胃肠虚实有关的脉象参数。 [[DOI](https://doi.org/10.19852/j.cnki.jtcm.2026.02.019)]
- [*arXiv*] **白睛异常分割（HD-DinoMoE）** 中医目诊看白睛缺少定量。这篇用分层混合专家网络，在复杂拍摄条件下分割巩膜表面异常。 [[论文](https://arxiv.org/abs/2606.04888)]
- [*Medicine in Novel Technology and Devices*] **基于中医脉诊矩阵的客观脉象分析** 用中医脉诊矩阵做客观脉象分析。文章认为现有脉图定义不完整，客观化标准也不统一。 [[DOI](https://doi.org/10.1016/j.medntd.2026.100429)]
- [*IEEE Journal of Biomedical and Health Informatics*] **可控 Transformer 面诊** 用一个可控的 Transformer，同时做多项中医面诊任务。2026 年发表。 [[DOI](https://doi.org/10.1109/jbhi.2026.3706751)]
- [*proceedings-article*] **Multimodal TCM Seven-Emotion Recognition: A Three-Modality Joint Consultation Framework Based on LLMs and Cross-Attention Fusion** 该七情识别框架在IEMOCAP的10593个样本上宏观F1为87.6%，再用冻结的大语言模型把神经预测写成中医辨证报告。 [Zhejiang University of Technology] [[DOI](https://doi.org/10.1145/3829441.3829486)]
- [*Lecture Notes in Computer Science Medical Image Computing and Computer Assisted Interventi*] **MLLM-Enhanced Region-Aware Bidirectional Evidence-Based Model for Tongue Diagnosis** 用多模态大模型做区域感知的双向循证舌诊。 [[DOI](https://doi.org/10.1007/978-3-032-38098-2_44)]
- [*arXiv*] **LingLan多模态辨证大模型** 面向望闻问切多模态数据的中医诊断大模型。与灵兰秘典评测基准（arXiv 2602.01779）不是同一篇 [清华大学深圳国际研究生院] [[论文](https://arxiv.org/abs/2609.25715)]
- [*Chinese Medicine*] **GNN-BERT 的症状–穴位推荐** 用异构图和图神经网络，再配合微调的 BERT，建模症状和穴位的配伍，用来推荐穴位。 [[DOI](https://doi.org/10.1186/s13020-026-01458-1)]
- [*Studies in Rhythm Engineering Cognitive Neuroscience and Artificial Intelligence*] **AI Tongue Diagnosis: Expert System with LLMs for Abdominal Disease Detection Through Mobile App** 用大语言模型做移动端舌诊专家系统，面向腹部疾病检测。 [[DOI](https://doi.org/10.1007/978-3-032-19966-9_2)]

</details>

<details>
<summary>2025 · 7</summary>

- [*Scientific Reports*] **脉诊机器学习识别妊娠与冠心病** 用 MEMS/CMOS 便携脉诊仪采集健康女性、冠心病女性和孕早期女性的脉图，再用机器学习区分妊娠和冠心病。 [[DOI](https://doi.org/10.1038/s41598-025-19780-3)]
- [*IEEE BIBM 2025*] **用大模型构建中医舌诊本体** 用大语言模型辅助构建中医舌诊本体 [[DOI](https://doi.org/10.1109/bibm66473.2025.11356313)]
- [*Lecture Notes in Electrical Engineering*] **智能脉诊：信号处理与深度学习** 用信号处理和深度学习对中医脉诊信号做健康状态分类。 [[DOI](https://doi.org/10.1007/978-981-95-1999-6_19)]
- [*ICASSP 2025*] **少样本舌诊上下文多任务微调** 舌象到体质直接判别的少样本上下文多任务LLM微调方法 [东北大学] [[DOI](https://doi.org/10.1109/ICASSP49660.2025.10887764)]
- [*International Conference on Digital Transformation and Management*] **多通道桡动脉信号的脉象识别** 用多通道设备采集桡动脉搏动，去噪并提取特征后，用卷积神经网络识别常见脉象。样本量和记录都没有公开。 [[DOI](https://doi.org/10.1145/3795546.3795575)]
- [*Medical Engineering & Physics*] **TPC-GCN：中医脉象分类** 先用改进的 SMOTE 扩充脉象样本，再提取多域特征，用图卷积网络做中医脉象分类。 [[DOI](https://doi.org/10.1016/j.medengphy.2025.104401)]
- [*arXiv*] **TCDiff** 三联级联扩散模型生成高保真多模态中医EHR，并构建**TCM-SZ1**基准数据集 [[论文](https://arxiv.org/abs/2508.01615)]

</details>

<details>
<summary>2024 · 5</summary>

- [*IEEE ECBIOS*] **高血压的中医面色分类** 建立用于高血压的中医面色分类模型。 [[DOI](https://doi.org/10.1109/ecbios61468.2024.10885481)]
- [*Digital Chinese Medicine*] **面色与体型的中医体质图像辨识** 给健康人拍全身站立照，按中医体质量表标上体质。面色和体型用颜色空间和局部二值模式提取，全身图像再用双分支网络提取深度特征，合在一起用随机森林辨认体质。准确率 0.842，精确率 0.868，F1 0.790。 [[DOI](https://doi.org/10.1016/j.dcmed.2024.09.002)]
- [*Bioengineering*] **面向糖尿病的中医脉诊卷积神经网络** 整理脉诊信号供卷积神经网络使用，以提高中医脉诊判断糖尿病的一致性。脉诊长期依赖指下感觉，重复性差。 [[DOI](https://doi.org/10.3390/bioengineering11060561)]
- [*IEEE ITNEC*] **统计特征与 MobileViT 的中医面色分类** 用统计特征和 MobileViT 做中医面色自动分类。 [[DOI](https://doi.org/10.1109/itnec60942.2024.10733073)]
- **Chinese-LLaVA-Med** 基于 LLaVA 架构的中文医学多模态大模型，支持中文医学影像问答，配套 llava-med-zh-eval 评测集与开源 7B 权重 [[代码](https://github.com/BUAADreamer/Chinese-LLaVA-Med)]

</details>

<details>
<summary>2023 · 3</summary>

- [*BMC Complementary Medicine and Therapies*] **桡动脉脉搏波识别多囊卵巢综合征** 用桡动脉脉搏波参数和机器学习区分多囊卵巢综合征与健康人，共 459 名受试者，用来把中医脉诊客观化。 [[DOI](https://doi.org/10.1186/s12906-023-04249-5)]
- [*Phenomics*] **仿生设备采集中医脉象的规程** 给出用仿生脉诊设备把中医脉象信息数字化采集的规程。 [[DOI](https://doi.org/10.1007/s43657-023-00104-2)]
- **XrayGLM** 会看胸部X光片的中文多模态医学大模型 [澳门理工大学] [[代码](https://github.com/WangRongsheng/XrayGLM)]

</details>


</details>

<details>
<summary>RAG / 知识图谱（62）：检索和医案、方剂图谱</summary>

<details>
<summary>2026 · 15</summary>

- [*Communications in Computer and Information Science (Springer)*] **Hybrid Retrieval + Re-ranking TCM Prescription Generation** 混合检索+重排序增强LLM的中医处方生成（Springer CCIS会议论文） [齐鲁工业大学，Shandong University，Shandong Academy of Sciences，山东中医药大学] [[论文](https://doi.org/10.1007/978-981-92-3563-6_21)]
- [*arXiv*] **Evidence-Based TCM Visualization Diagnosis System** Neo4j知识图谱（241证型/1263症状）+四阶段症状匹配（含LLM验证）+信息增益主动问诊的中医可视化诊疗系统 [[论文](https://arxiv.org/abs/2606.06869)]
- **儿童流感中成药推荐系统（KG+LLM）** 整合权威指南构建儿童流感中成药知识图谱并与LLM集成（JMIR Preprints预印本） [[预印本](https://doi.org/10.2196/preprints.101648)]
- [*Frontiers in Medicine*] **靳三针知识图谱问答 (Jin San Zhen KG-QA)** 靳三针针灸流派知识图谱+大模型问答工具 [广州中医药大学] [[DOI](https://doi.org/10.3389/fmed.2026.1755583)]
- [*IEEE BigComp 2026*] **知识图谱增强的中医问答大模型** 用知识图谱增强大模型的中医问答，补辨证推理并降低多源数据带来的幻觉 [燕山大学，福建中医药大学，暨南大学] [[DOI](https://doi.org/10.1109/bigcomp68355.2026.00029)]
- [*Frontiers in Medicine*] **树状自反思检索中医问答** 树状组织语料+自反思检索的中医 QA 方法（Frontiers in Medicine 2026） [澳门科技大学] [[DOI](https://doi.org/10.3389/fmed.2026.1752778)]
- [*Journal of King Saud University - Computer and Information Sciences*] **TCMKG: Knowledge-Grounded question answering in Traditional Chinese Medicine via dynamic prompt evolution framework** TCMKG在新安医案上用专家引导提示抽取实体，建成含37192个实体、130030条关系的中医知识图谱，信息抽取精确率0.89、召回率0.88、F1为0.88。 [Anhui University of Traditional Chinese Medicine，Hefei University] [[DOI](https://doi.org/10.1007/s44443-026-00743-1)]
- [*Digital Chinese Medicine*] **TCM-HyperRAG** 用高阶知识超图增强中医疾病诊断和处方推荐，并把可追溯证据交给骨干大模型 [[DOI](https://doi.org/10.1016/j.dcmed.2026.08.004)]
- [*Frontiers in Medicine*] **TCM-DiffRAG** 通用知识图谱 + 个性化知识图谱 + CoT 的辨证推理 RAG 框架 [Guangdong Institute of Intelligence Science and Technology, Zhuhai，Hangzhou Ganzhicao Technology Co., Ltd，BoardWare Information System Limited] [[正式发表](https://doi.org/10.3389/fmed.2026.1804478)] [[论文](https://arxiv.org/abs/2602.22828)] [[代码](https://github.com/LiJianmin6706/Tcm_Diff_RAG)]
- [*Frontiers in Pharmacology*] **TCM-CoT-RAG** 面向中医风湿病临床决策的检索增强系统，用思维链约束专家式推理，降低大模型幻觉 [[DOI](https://doi.org/10.3389/fphar.2026.1884526)]
- [*Neural Networks*] **LLM-SDaT** 把知识注入大模型，用于中医辨证 [浙江大学] [[DOI](https://doi.org/10.1016/j.neunet.2026.108812)]
- [*世界科学技术-中医药现代化*] **KG-IMHRE（赵炳南流派可解释多跳检索增强问答）** 以赵炳南皮肤科流派知识图谱为库，用子图挖掘和动态检索语句引导大模型做可解释多跳问答。流派测试基准上选择题 85.2、问答题 45.78、总分 73.38，问答题专家评分 4.2。 [中国中医科学院中医药信息研究所] [[DOI](https://doi.org/10.11842/wst.20250706001)]
- [*proceedings-article*] **Construction of a Knowledge Graph for Functional Specification Standards of Traditional Chinese Medicine Information Systems Based on Large Language Models** 作者以中医药信息学会22份中医信息系统功能规范团体标准为语料，用CRISPE框架约束提示，让DeepSeek抽取实体和关系并加规则约束来建知识图谱。 [Hubei University of Chinese Medicine] [[DOI](https://doi.org/10.1145/3833450.3833480)]
- [*International Conference on Optics, Electronics, and Communication Engineering (*] **A knowledge-enhanced prescription generation model for TCM syndrome differentiation via multilevel memory retrieval** 该处方生成模型用加权BM25检索相似病例，并接入《本草纲目》药物知识图谱以及十八反、十八畏，再把检索结果交给大语言模型，实验在CCL2025中医基准上进行。 [Chengdu Medical College，First Affiliated Hospital of Chengdu Medical College] [[DOI](https://doi.org/10.1117/12.3123588)]
- [*Journal of Visualized Experiments*] **A Study on An Intelligent Diagnosis and Treatment Assistant System For Acupuncture in Diminished Ovarian Reserve Based on A Knowledge Graph** 作者用大语言模型加人工标注，从82部针灸文献和临床数据中建成含16558个实体、80084条关系的图谱；在90例卵巢储备功能减退患者中，系统辨证与专家的一致率为86.7%。 [Nanjing University of Chinese Medicine，Xuzhou Medical College，Nanjing General Hospital of Nanjing Military Command，Nanjing University] [[DOI](https://doi.org/10.3791/71182)]

</details>

<details>
<summary>2025 · 28</summary>

- [*世界科学技术-中医药现代化*] **阿尔茨海默病指南知识库问答（ChatGLM3）** 用 LangChain 把 ChatGLM3-6B 接到本地库，库含中国中西医结合学会、中华医学会认证的阿尔茨海默病诊疗指南、规范和教科书。相对裸 ChatGLM3-6B，事实准确性 Win 88.09%、完整性 Win 85.71%。 [湖南中医药大学信息科学与工程学院] [[DOI](https://doi.org/10.11842/wst.20240329007)]
- [*世界科学技术-中医药现代化*] **监督微调结合检索增强的中医知识问答** 以 ChatGLM3 为基座，用 PissA 做监督微调并接 RAG。文中模型 BLEU 14.5830、ROUGE-1 34.6730；接入 RAG 后中医题库推理 F 值 0.6398，高于 ChatGLM3 基线 0.2654。 [南京中医药大学人工智能与信息技术学院，南京大学信息管理学院，江苏省中医流派研究院] [[DOI](https://doi.org/10.11842/wst.20241121002)]
- [*Journal of Pharmaceutical Analysis*] **可解释图神经网络量化中药配伍** 在中医药多维知识图谱上，用可解释图神经网络量化配伍。图谱把术语和饮片连起来，药性作为虚拟节点；在 6080 首方上评估饮片在方中的作用，并用 215 首新冠相关方做验证。 [[DOI](https://doi.org/10.1016/j.jpha.2025.101342)] [[arXiv](https://arxiv.org/abs/2411.11474)]
- [*IEEE ICCBDAI 2025*] **动态知识图谱与大模型的中医生理建模** 把动态知识图谱接进大模型，补中医生理知识覆盖不足和更新成本高的问题 [北京科技大学] [[DOI](https://doi.org/10.1109/iccbdai66607.2025.11388184)]
- [*IEEE BIBM 2025*] **中成药知识体系构建** LLM+知识图谱构建中成药知识体系 [[DOI](https://doi.org/10.1109/BIBM66473.2025.11356149)]
- [*CCIS*] **中医问诊中的大模型与知识图谱** 以中医问诊为例，把大语言模型和知识图谱结合起来 [天津大学，天津中医药大学] [[DOI](https://doi.org/10.1007/978-981-96-1809-5_28)]
- [*CCIS*] **中医药知识图谱问答系统** 把中医药知识图谱和大语言模型接成智能问答系统 [[DOI](https://doi.org/10.1007/978-981-96-1809-5_26)]
- [*数据分析与知识发现*] **中医药标准知识问答系统** 检索增强技术构建中医药标准知识问答系统的探索与实践 [中国中医科学院等] [[DOI](https://doi.org/10.11925/infotech.2096-3467.2024.0747)]
- [*Frontiers in Medicine*] **中医医案问答系统** 融合大语言模型与知识图谱的中医医案问答系统，提升医案检索与分析效率（Frontiers in Medicine 2025） [安徽中医药大学] [[DOI](https://doi.org/10.3389/fmed.2024.1512329)]
- [*JMIR Medical Informatics*] **Yaoshi-RAG（药食同源RAG）** 基于不确定知识图谱的药食同源膳食推荐RAG，提升LLM个性化与可解释性 [[DOI](https://doi.org/10.2196/75279)]
- [*Frontiers in Pharmacology*] **TCMRD-KG** 基于古籍文献的风湿病中医知识图谱创新设计 [北京中医药大学] [[DOI](https://doi.org/10.3389/fphar.2025.1535596)]
- [*Digital Chinese Medicine*] **TCMLCM** 基于KG2TRAG的中医肺癌智能问答模型 [南京中医药大学] [[DOI](https://doi.org/10.1016/j.dcmed.2025.03.011)]
- [*Journal of Pharmaceutical Analysis*] **TCMKD 中医药知识发现平台** 手工校对后汇集证候、方剂、中成药、药材、成分、靶点和疾病。平台提供挖掘、富集和网络定位分析。 [[DOI](https://doi.org/10.1016/j.jpha.2025.101297)] [[网站](https://cbcb.cdutcm.edu.cn/TCMKD/)]
- **TCM-Sage** 面向中医师的证据合成RAG助手（混合向量+知识图谱） [[代码](https://github.com/AndyZHENG0715/TCM-Sage)]
- [*proceedings-article*] **Smart Virtual Patients for TCM: Combining Knowledge Graphs and Language Models** 该中医虚拟病人把大语言模型和知识图谱与束搜索、Sentence-BERT剪枝结合，症状一致性53.2%、召回率62.5%，均高于提示加知识图谱的基线。 [Universiti Sains Malaysia，Sultan Qaboos University] [[DOI](https://doi.org/10.1109/icitda68167.2025.11332301)]
- [*IEEE International Conference on Electrical, Automation and Computer Engineering*] **Research on the Organization and Application of Traditional Chinese Medicine Processing Knowledge in Lingnan Herbal Medicine Ancient Texts by Integrating Large Models and Knowledge Graph Technology** 作者用大语言模型和知识图谱整理岭南本草古籍中的药材、炮制方法、辅料和功效，在Neo4j中建图，并结合BERT-CAN-NER与大模型生成做自然语言问答。 [Guangzhou University of Chinese Medicine] [[DOI](https://doi.org/10.1109/iceace67491.2025.11439512)]
- [*proceedings-article*] **Research on the Construction of a Traditional Chinese Medicine Coronary Heart Disease Question-Answering System Integrating Large Language Models and Knowledge Graphs** 作者用提示引导大语言模型从近十年8部冠心病中医或中西医结合指南中抽取实体和关系，建成含452个节点、690条关系的知识图谱，并以BERT+CNN做最优意图识别。 [China Academy of Chinese Medical Sciences，Tongji University] [[DOI](https://doi.org/10.1145/3777577.3777709)]
- [*Pharmacological Research*] **RAG-CPMF** 多LLM校验+RAG的中成药智能推荐框架，并发布持续更新的大规模中成药公开数据集 [[DOI](https://doi.org/10.1016/j.phrs.2025.107883)] [[数据](https://gitee.com/tcmdoc/cpm)]
- [*arXiv*] **OpenTCM** 基于 GraphRAG 的中医知识检索与诊断系统，含妇科古籍知识图谱 [[论文](https://arxiv.org/abs/2504.20118)] [[代码](https://github.com/OpenTCM01/OpenTCM)]
- [*proceedings-article*] **Method for Constructing TCM Syndrome Differentiation Q&A System with LLM-RAG** 该中医辨证问答框架把整理过的中医知识库通过结构化检索接到大语言模型上，以提高回答的事实准确性、语境精度和专业性。 [Baoshan University] [[DOI](https://doi.org/10.1145/3784013.3784061)]
- [*IEEE BIBM*] **MRD-RAG** 模拟临床推理的多轮诊断RAG框架，并构建覆盖中西医的**DiagnosGraph**（876病/7997节点/37201三元组） [香港科技大学] [[正式发表](https://doi.org/10.1109/bibm66473.2025.11357107)] [[论文](https://arxiv.org/abs/2504.07724)]
- [*Interdisciplinary Sciences*] **LLM驱动中医知识图谱构建** LLM驱动的中医知识图谱构建与应用 [河南工业大学] [[DOI](https://doi.org/10.1007/s12539-025-00735-1)]
- [*Journal of Medical and Biological Engineering*] **LLM+RAG中医推理** LLM与RAG结合的中医推理方法 [台北市立联合医院] [[DOI](https://doi.org/10.1007/s40846-025-00988-7)]
- [*International Conference on e-Education, e-Business, e-Management and e-Learning*] **Knowledge Graphs Combined with ChatGPT in the Field of Acupuncture: A Case Study on the Treatment of Depression** 该研究把针灸原理做成抑郁症知识图谱，并用大语言模型优化知识整合，供研究者和临床医生使用。 [Nanjing University，Nanjing University of Chinese Medicine] [[DOI](https://doi.org/10.1109/ic4e65071.2025.11075342)]
- [*International Conference on Biomedical and Intelligent Systems*] **Jiezhai Gong 妇产科医案知识图谱** 用 Neo4j 构建 Jiezhai Gong 妇产科医案知识图谱。 [[DOI](https://doi.org/10.1145/3745034.3745089)]
- [*Proceedings of the 2nd International Conference on Machine Learning and Automation, CONF-M*] **Chinese Medicine Question Answering Robot Based on RAG and Self-Built Dataset** 用检索增强生成和自建数据集构建中医问答机器人。 [大连理工大学，西安电子科技大学] [[DOI](https://doi.org/10.4108/eai.21-11-2024.2354617)]
- [*JAMIA*] **AcuKG** 用实体识别、关系抽取和本体映射，把针灸指南、文献和临床试验整理成知识图谱 [中国中医科学院] [[DOI](https://doi.org/10.1093/jamia/ocaf179)]
- [*Communications in Computer and Information Science Health Information Processing. Evaluati*] **A TCM Syndrome Differentiation Thinking Method Based on Chain of Thought and Knowledge Retrieval Augmentation** CotKE-TCM 用思维链提示，并检索相似医案、模型生成的中医知识和临床经验，辅助大模型做辨证；在 CHIP 2024 评测集上测试。 [之江实验室，上海理工大学，ANTA Group] [[DOI](https://doi.org/10.1007/978-981-96-4298-4_3)]

</details>

<details>
<summary>2024 · 14</summary>

- [*中国数字医学*] **循证中医指南 PICO 知识图谱问答** 崔唐明、孙美玲、孙华君、李海燕以多囊卵巢综合征指南为例，用文心一言抽取 PICO 知识，Neo4j 存成 13 类、248 节点、337 条关系的指南图谱，并预设 12 类临床问题、24 个问句模板。2024 年第 19 卷第 5 期 20–27 页。 [中国中医科学院中医药信息研究所] [[论文](https://www.zgszyx.org.cn/CN/Y2024/V19/I5/20)]
- [*IEEE BIBM 2024*] **名老中医针灸医案知识图谱** 用大模型做信息抽取，构建名老中医针灸医案知识图谱 [中国中医科学院] [[DOI](https://doi.org/10.1109/bibm62325.2024.10821904)]
- [*JMIR Medical Informatics*] **中医领域知识图谱补全** 中医领域知识图谱补全与质量评估研究 [Zhejiang Chinese Medical University，Guangdong Provincial Hospital of Traditional Chinese Medicine] [[DOI](https://doi.org/10.2196/55090)]
- [*南京中医药大学学报*] **中医药问答大语言模型** RAG 结合 P-Tuning v2 微调的中医药问答大模型（ChatGLM2-6B） [南京中医药大学] [[DOI](https://doi.org/10.14148/j.issn.1672-0482.2024.1375)]
- [*计算机科学与探索*] **中医药大模型知识增强方法** 面向中医药大模型的知识增强方法，基于约十万首经典方剂构建图谱并保持方剂结构性 [天津大学] [[DOI](https://doi.org/10.3778/j.issn.1673-9418.2407082)]
- [*Methods of Information in Medicine*] **TCMSF** 中医证候古籍知识图谱构建框架 TCMSF，将古籍中的证候知识系统化组织并语义关联，为中医信息化提供基础（Methods of Information in Medicine 2024） [中国中医科学院] [[DOI](https://doi.org/10.1055/a-2590-6348)]
- [*IEEE International Conference on Medical Artificial Intelligence (MedAI)*] **TCMRD-KG: Design and Development of a Rheumatism Knowledge Graph Based on Ancient Chinese Literature** TCMRD-KG是首个基于中医古籍痹证内容的知识图谱，实体标注结合了主流大语言模型自动标注和人工复核。 [Beijing University of Chinese Medicine，China Academy of Chinese Medical Sciences，Guang’anmen Hospital，Institute of Basic Theory for Chinese Medicine] [[DOI](https://doi.org/10.1109/medai62885.2024.00083)]
- [*Computational and Structural Biotechnology Journal*] **TCMM 中药现代化统一数据库** 提出一个面向中药现代化和治疗创新的统一数据库。 [[DOI](https://doi.org/10.1016/j.csbj.2024.04.016)]
- [*EIECC*] **TCM MLKG-RAG** 多层知识图谱检索增强生成的中医智能诊断 [University of Science and Technology of China] [[DOI](https://doi.org/10.1109/EIECC64539.2024.10929529)]
- [*OSF Preprints（预印本）*] **RAG 增强中医问答置信度** 检索增强生成提升大模型中医问答置信度（预印本） [[DOI](https://doi.org/10.31219/osf.io/ns2v3)]
- [*arXiv*] **Prompt-RAG: Pioneering Vector Embedding-Free Retrieval-Augmented Generation in Niche Domains, Exemplified by Korean Medicine** Prompt-RAG不使用向量嵌入，在韩医问答聊天机器人上，其相关性和信息量优于ChatGPT以及基于向量嵌入的检索增强生成。 [Gachon University，Stanford Medicine，Stanford University] [[论文](https://arxiv.org/abs/2401.11246)]
- [*Phytomedicine*] **PresRecRF** 把分子知识图谱与大模型抽出的中医语义表示融合，同时预测草药和剂量。代码与数据在 GitHub。 [北京交通大学] [[DOI](https://doi.org/10.1016/j.phymed.2024.156116)] [[代码](https://github.com/2020MEAI/PresRecRF)]
- [*Electronics*] **LLM 构建中医知识图谱** 基于大语言模型的中医知识图谱构建 [同济大学] [[DOI](https://doi.org/10.3390/electronics13071395)]
- [*Database (Oxford)*] **ACUBERT** 针灸适应证知识库的经络实体识别与分类模型 [南京中医药大学，Nanjing KG Data Technology] [[DOI](https://doi.org/10.1093/database/baae083)]

</details>

<details>
<summary>2023 · 5</summary>

- [*Frontiers of Information Technology & Electronic Engineering*] **知识引导的中医荐药（FITEE）** 用典籍和处方抽出的症状–草药知识图谱做图注意力表示，并在预测层加入方剂学信息。 [[DOI](https://doi.org/10.1631/FITEE.2200662)]
- [*IEEE ICIEA*] **温病文献的 BERT 命名实体识别** 用 BERT 识别中医温病文献中的命名实体。 [[DOI](https://doi.org/10.1109/iciea58696.2023.10241595)]
- [*计算机科学与探索*] **大模型融合知识图谱问答系统** LLM 与知识图谱深度融合的中医药方剂垂直领域问答系统 [天津大学] [[DOI](https://doi.org/10.3778/j.issn.1673-9418.2308070)]
- [*Computers in Biology and Medicine*] **《伤寒论》问题意图分类（TinyBERT-CNN）** 用 TinyBERT 和卷积神经网络融合，对《伤寒论》里的问题做意图分类。 [[DOI](https://doi.org/10.1016/j.compbiomed.2023.107075)]
- [*世界科学技术-中医药现代化*] **MMKGQA（海洋中药知识图谱问答）** 以细粒度海洋中药图谱 MMKG 为库，用 Aho-Corasick 与 Word2Vec 做实体识别和问题分类，建成 MMKGQA。问卷调查语料上平均精确率 97.93%、召回率 83.41%、F1 89.10%。不是大语言模型系统。 [南京中医药大学人工智能与信息技术学院] [[DOI](https://doi.org/10.11842/wst.20220514002)]

</details>


</details>

<details>
<summary>处方 / 组方（36）：荐药、组方、药对</summary>

<details>
<summary>2026 · 15</summary>

- [*arXiv*] **Patient-Conditioned Dual Hypergraph Reasoning** 患者条件化双超图推理实现可审计的中医处方支持，将症状/舌/脉证据围绕证型与治则组织（天津大学） [[论文](https://arxiv.org/abs/2607.04025)]
- [*KSII Transactions on Internet and Information Systems*] **GAT+LLM TCM Prescription Generation** 图注意力网络与LLM结合的中医处方智能生成模型（KSII TIIS正式发表） [[DOI](https://doi.org/10.3837/tiis.2026.05.006)]
- [*世界科学技术-中医药现代化*] **知识蒸馏中医辨证论治模型** 以 GPT-4o 为教师，从中医医案蒸馏辨证论治指令，再对 Qwen2.5-7B 做 LoRA 监督微调。论文报告推理过程更可读，同时保住处方推荐精度。未给独立品牌名，也未见公开权重。 [南京中医药大学人工智能与信息技术学院，南京大学信息管理学院，江苏省中医流派研究院] [[DOI](https://doi.org/10.11842/wst.20250422007)]
- [*arXiv*] **理法方药对齐的中医处方生成** 四阶段对齐处方生成：补可审计的理法方药推理、随证加减，以及十八反等禁忌 [清华大学] [[论文](https://arxiv.org/abs/2609.25755)]
- [*Expert Systems with Applications*] **异构网络预测中药毒性** 用异构网络预测中药毒性。 [[DOI](https://doi.org/10.1016/j.eswa.2025.129969)]
- [*CCIS*] **多阶段学习的中医处方推荐大模型** 用多阶段学习训练面向中医处方推荐的大语言模型 [厦门大学] [[DOI](https://doi.org/10.1007/978-981-92-0291-1_11)]
- [*Evidence-Based Chinese Medicine and Technology Assessment*] **中西药相互作用专论库** 为临床决策支持库整理有证据的中西药相互作用专论。2026 年发表。 [[DOI](https://doi.org/10.26599/ecmta.2026.9570040)] [[网站](https://www.imgateway.net)]
- [*Frontiers in Pharmacology*] **中药复方剂量调整方法** 讨论怎样把经验用药收成可调整的复方剂量，往更精细的用法走。2026 年发表在 Frontiers in Pharmacology。 [[DOI](https://doi.org/10.3389/fphar.2026.1815285)]
- [*Pharmacological Research - Modern Chinese Medicine*] **中药化合物的多监管安全评价机器学习框架** 从 TCMSP、TCMID、PubChem 和 ChEMBL 汇集 24 种药材的 127 个活性成分，用随机森林，并按 FDA、EMA 和 CFDA 的不同侧重点做安全评分。 [[DOI](https://doi.org/10.1016/j.prmcm.2026.100772)]
- [*Zenodo*] **UniTCM** 把方剂和疾病对应到分子层面的反向药理学平台，包含标准化、临床发现、分子分析、系统核对和分析工具五层。 [[代码](https://doi.org/10.5281/zenodo.21711675)] [[网站](https://unitcm.qfxulab.com/)]
- [*Chinese Medicine*] **TCMNet** LLM辅助疾病知识挖掘+PPI网络与结合预测的方剂优化策略 [浙江省中医药研究院] [[DOI](https://doi.org/10.1186/s13020-026-01360-w)]
- [*Current Molecular Pharmacology*] **TCMDATA** 面向靶点的中医网络药理分析和人工智能解读的 R 包。2026 年发表在 Current Molecular Pharmacology。 [[代码](https://github.com/YuLab-SMU/TCMDATA)] [[DOI](https://doi.org/10.1016/j.cmp.2026.09.003)]
- [*Frontiers in Pharmacology*] **MSAT：中药物不良反应预测** 用 FAERS 自发报告训练异构图神经网络，预测中药相关的不良反应。2026 年发表在 Frontiers in Pharmacology。 [[DOI](https://doi.org/10.3389/fphar.2026.1774128)]
- [*Mathematics*] **LLM-Driven Unsupervised Discovery of Semantic Decision Dimensions for Dynamic Scheduling and Intelligent Systems: A Traditional Chinese Medicine Case Study** DeepSeek-V3.2从12163条中药记录、64107个短句中归纳出458个原始标签并合并为22个语义类；Qwen3-Embedding-8B测得19个概念的内部一致性平均超过60%，专家合理性均分4.64（1到5分）。 [Changchun University of Chinese Medicine，Shandong University of Arts，Tsinghua University] [[DOI](https://doi.org/10.3390/math14152681)]
- [*Digital Chinese Medicine*] **CMM-EmbedCluster** 基于LLM与药性理论的中药聚类框架，构建567味药性知识库 [南京中医药大学] [[DOI](https://doi.org/10.1016/j.dcmed.2026.05.010)]

</details>

<details>
<summary>2025 · 11</summary>

- [*IEEE Journal of Biomedical and Health Informatics*] **草药-药物相互作用预测** LLM增强的草药-药物相互作用预测 [深圳大学] [[DOI](https://doi.org/10.1109/jbhi.2025.3558667)]
- [*IEEE BIBM*] **方剂推荐中的剂量预测** 在推荐中药方剂的同时预测剂量，用了扩散模型和异构层次网络。2025 年 IEEE BIBM。 [[DOI](https://doi.org/10.1109/bibm66473.2025.11357222)]
- [*Chinese Medicine*] **强化学习的可解释中医处方推荐** 用强化学习做可解释的中医处方推荐，并把较小语言模型里的隐含偏好用上。2025 年发表在 Chinese Medicine。 [[DOI](https://doi.org/10.1186/s13020-025-01250-7)]
- [*Scientific Reports*] **图注意力网络预测中药相互作用** 用图注意力网络预测中药之间的相互作用，用来提前发现配伍风险。 [[DOI](https://doi.org/10.1038/s41598-025-00725-9)]
- [*arXiv*] **可解释框架量化中医症状–方药对应** 用古代和经典方剂记录训练模型，把症状模式对应到个体化方药这条原则量化，以便和现代生物医学对照。 [[论文](https://arxiv.org/abs/2507.11176)]
- [*IEEE BIBM 2025*] **医学知识增强的双层对齐中药处方推荐** 用医学知识增强的双层对齐网络做中药处方推荐，避免只依赖结构化输入或多阶段流水线 [南京信息工程大学] [[DOI](https://doi.org/10.1109/bibm66473.2025.11356282)]
- [*JMIR Medical Informatics*] **中医方剂分类加权投票** LLM加权投票中医方剂分类方法 [中国医学科学院/北京协和医学院] [[DOI](https://doi.org/10.2196/69286)]
- [*IEEE International Conference on Bioinformatics and Biomedicine (BIBM)*] **Two-Stage Chain-of-Thought Fine-Tuning for TCM Medication Decision-Making in Nsclc** 针对非小细胞肺癌，两阶段思维链微调在处方生成和中成药推荐上分别比基线提高1.2%和6.1%。 [China Academy of Chinese Medical Sciences，Qinghai Normal University，Chinese Academy of Social Sciences，Institute of Ethnology and Anthropology] [[DOI](https://doi.org/10.1109/bibm66473.2025.11356901)]
- [*IEEE JBHI*] **TEmbed-DDI：中西药相互作用标注** 用大语言模型和双向神经网络做跨域药物相互作用标注，并把中药相互作用纳入评测 [[DOI](https://doi.org/10.1109/jbhi.2025.3563289)]
- [*proceedings-article*] **Dynamic Disease Tracking and Personalized Prescription Recommendation Using Large Language Model in Traditional Chinese Medicine** 该系统把多轮问诊和时间序列分析接进大语言模型以推荐个体化中药处方，并在1000例失眠病例上提高了初诊推断、诊断准确性和系统适应性。 [National Central University，National Taiwan University of Science and Technology，Research Center for Humanities and Social Sciences, Academia Sinica] [[DOI](https://doi.org/10.1109/iccbe65177.2025.11255949)]
- [*IEEE Transactions on Computational Biology and Bioinformatics*] **AN-IHP：注意力网络预测配伍禁忌药对** 用注意力网络预测中药里配伍禁忌的药对。 [[DOI](https://doi.org/10.1109/tcbbio.2024.3498094)]

</details>

<details>
<summary>2024 · 5</summary>

- [*Analytical Chemistry*] **质谱机器学习预测中药毒性** 用质谱和机器学习预测中药毒性。 [[DOI](https://doi.org/10.1021/acs.analchem.4c05311)]
- [*Computer Methods in Biomechanics and Biomedical Engineering*] **复方煎煮时长分类** 按多维特征给中药复方的煎煮时长做分类。2024 年发表。 [[DOI](https://doi.org/10.1080/10255842.2024.2302225)]
- [*IEEE BIBM*] **TCM-FTP** 面向中药处方预测的大模型微调方法 [香港科技大学，北京交通大学，中国中医科学院，河南中医药大学] [[DOI](https://doi.org/10.1109/BIBM62325.2024.10822451)]
- [*JAMIA*] **PresRecST** 按「辨证—立法—荐药」递进推荐中药处方（JAMIA 2024）；配套公开 TCM-Lung 编码子集与 TCM-PD 复现表，代码在 GitHub [北京交通大学，中国中医科学院，河南中医药大学] [[DOI](https://doi.org/10.1093/jamia/ocae066)] [[代码](https://github.com/2020MEAI/PresRecST)]
- [*IEEE International Conference on Computer and Communication Engineering Technolo*] **A Study of Automated Data Mining of Medication Rules in Traditional Chinese Medicine Prescriptions Based on Large Language Model** 作者用大语言模型通过人机问答，对治疗骨质疏松的中药处方做频次、聚类和Apriori关联分析，结果与SPSS人工统计高度相似。 [Jinan University] [[DOI](https://doi.org/10.1109/ccet62233.2024.10837914)]

</details>

<details>
<summary>2023 · 5</summary>

- [*arXiv*] **深度强化学习的序贯中药治疗规划** 把慢性病的中药治疗看成多次就诊上的序贯决策，用深度强化学习规划后续处方，而不是只给一次方。 [[论文](https://arxiv.org/abs/2304.12828)]
- [*Chinese Medicine*] **喜炎平严重不良事件的投影重要性** 用变量投影重要性分析年龄和中西药联用，对喜炎平注射液不良事件严重程度的影响。2023 年发表在 Chinese Medicine。 [[DOI](https://doi.org/10.1186/s13020-023-00718-8)]
- [*IEEE BIBM*] **中医方剂 LLM 分类** 微调大语言模型并结合提示模板进行中医方剂分类，数据源自中成药国家医保目录等（IEEE BIBM 2023） [Leipzig University，Changchun University of Chinese Medicine，Liaoning Technical University，Sichuan Academy of Traditional Chinese Medicine] [[DOI](https://doi.org/10.1109/BIBM58861.2023.10385776)]
- [*IEEE Access*] **PreGenerator** 检索与生成方法结合的中医处方推荐模型 [College of Physics, Taiyuan University of Technology, Taiyuan, China，North Automatic Control Technology Institute, Taiyuan, China] [[DOI](https://doi.org/10.1109/ACCESS.2023.3316219)]
- [*IEEE BIBM*] **LLM+GNN 中医处方推荐** 大语言模型与图神经网络结合的中医处方推荐模型 [南京中医药大学] [[DOI](https://doi.org/10.1109/BIBM58861.2023.10385489)]

</details>


</details>

<details>
<summary>抽取 / 编码器（11）：NER、关系抽取、BERT 类编码器</summary>

- [*世界科学技术-中医药现代化*] **杏林-NER (XingLin-NER)** 面向中医临床文本术语多变的问题，用结构化指令和推理式指令做生成式命名实体识别，得到杏林-NER 系列，并用 TCM-BERT 语义相似度作评估。属抽取方法，不是通用领域对话大模型。 [中国中医科学院中医药信息研究所] [[DOI](https://doi.org/10.11842/wst.20250327010)]
- [*Scientific Reports*] **中医命名实体识别的知识蒸馏** 用知识蒸馏做中医命名实体识别，把大模型的识别能力收进更小的模型。2026 年发表在 Scientific Reports。 [[DOI](https://doi.org/10.1038/s41598-026-56313-y)]
- [*Artificial Intelligence in Medicine*] **中医临床命名实体与关系联合识别** 用字符级卷积循环交互网络，同时做中医临床命名实体识别和关系抽取。2026 年发表在 Artificial Intelligence in Medicine。 [[DOI](https://doi.org/10.1016/j.artmed.2026.103372)]
- [*proceedings-article*] **Named Entity Recognition in Traditional Chinese medicine Literature Data for Obesity Based on Large Language Models** 在中医肥胖文献实体识别上，经多轮提示优化的DeepSeek-R1在测试集F1达到0.927。 [Hubei University of Chinese Medicine] [[DOI](https://doi.org/10.1145/3833450.3833478)]
- [*Applied Intelligence*] **KDC-NER** 知识引导数据增强+大模型微调的中医嵌套命名实体识别框架 [江西中医药大学] [[DOI](https://doi.org/10.1007/s10489-026-07095-3)]
- [*npj Digital Medicine*] **补充替代医学文献抽取语言模型** 用于补充替代医学文献数据抽取与偏倚风险评估的语言模型 [兰州大学] [[DOI](https://doi.org/10.1038/s41746-025-01457-w)]
- [*Scientific Reports*] **双通道知识注意力辨证模型** 双通道知识注意力的中医辨证NLP模型，缓解生僻字与术语抽取难题 [[DOI](https://doi.org/10.1038/s41598-025-96404-w)]
- [*Lecture Notes on Data Engineering and Communications Technologies*] **中医药专利关系抽取** 用大语言模型和多样化语义交互抽取中医药专利中的关系 [湖北工业大学] [[DOI](https://doi.org/10.1007/978-3-032-10344-4_1)]
- [*Scientific Reports*] **中医病历嵌套实体识别** 识别中医电子病历里套在一起的实体，比如症状和它所在的部位。2025 年发表在 Scientific Reports。 [[DOI](https://doi.org/10.1038/s41598-025-22283-w)]
- [*Journal of the American Medical Informatics Association*] **LLM 腧穴定位关系抽取** 大语言模型关系抽取案例研究：腧穴定位知识 [中国中医科学院，The University of Texas MD Anderson Cancer Center , Houston, TX 77030] [[DOI](https://doi.org/10.1093/jamia/ocae233)]
- [*Frontiers in Artificial Intelligence*] **Evi-BERT** 中医RCT证据自动抽取的信息抽取模型开发与验证 [北京航空航天大学，北京中医药大学] [[DOI](https://doi.org/10.3389/frai.2024.1454945)]

</details>

<details>
<summary>评测论文（75）：基准和考试；要下载评测集走下面「数据集」</summary>

<details>
<summary>2026 · 40</summary>

- [*Future Internet (MDPI)*] **RAG+LoRA 中医执照考试推理架构** RAG+LoRA生成式架构，构建台湾中医师执照考试11,476题（2005–2025）数据集，准确率61.0%→89.0%+（Future Internet） [Chung Shan Medical University Hospital，Chung Shan Medical University] [[DOI](https://doi.org/10.3390/fi18060280)]
- [*Scientific Data*] **辨证论治大模型基准数据集** Scientific Data发布的辨证论治基准，用来评估大模型在中医个体化、整体性临床任务上的能力 [中国中医科学院，中国科学院，天津大学] [[DOI](https://doi.org/10.1038/s41597-026-07587-4)]
- [*arXiv*] **证伪导向的可审计辨证协议** 在公开TCMEval-SDT的200例辨证上，用与具体模型无关的证伪协议约束可审计决策，强调输出纪律而不只是换更大的模型 [[论文](https://arxiv.org/abs/2610.18298)]
- [*Frontiers in Plant Science*] **药用植物多模态大模型评测** 多模态LLM药用植物识别系统评测 [绍兴文理学院] [[DOI](https://doi.org/10.3389/fpls.2026.1765281)]
- [*Frontiers in Medical Technology*] **胸痹/冠心病的中西医数据治理** 以胸痹（冠心病）为例，按 HL7 FHIR 和 SNOMED CT 建了 9 个子集、352 个数据元，其中 42.6% 是中医专用。触发引擎有 128 条规则。前瞻对照纳入 972 人。 [[DOI](https://doi.org/10.3389/fmedt.2026.1759773)]
- [*Digital Chinese Medicine*] **知识图谱增强的长尾证候辨证** 用知识图谱增强长尾学习，做中医证候辨证。 [[DOI](https://doi.org/10.1016/j.dcmed.2026.02.005)]
- [*Journal of Evidence-Based Medicine*] **中医证候诊断标准适用性评价指南** 用德尔菲法给出证候诊断标准的适用性评价指南，共 5 个域、25 条：可获得性、可读性、可实施性、可接受性和总评。每条按 5 点量表打分。 [[DOI](https://doi.org/10.1111/jebm.70153)]
- [*Journal of Evidence-Based Medicine*] **中医考题大/轻量模型对比** 大规模与轻量级LLM中医考题系统对比 [河南大学第一附属医院] [[DOI](https://doi.org/10.1111/jebm.70118)]
- [*Expert Systems with Applications*] **中医端到端临床支持基准** 面向端到端临床支持全链路的中医LLM评测基准 [华东师范大学] [[DOI](https://doi.org/10.1016/j.eswa.2026.132267)]
- [*Journal of Traditional Chinese Medical Sciences*] **中医智能预问诊临床评估** LLM智能预问诊系统三甲医院临床评估，采用医-AI-患三元模式 [北京中医医院] [[DOI](https://doi.org/10.1016/j.jtcms.2026.06.002)]
- [*Frontiers in Medicine*] **中医教育AI导师评估** 跨认知层级的多模态LLM中医教育评估 [北京中医药大学] [[DOI](https://doi.org/10.3389/fmed.2026.1893231)]
- [*Scientific Reports*] **中医执业考试三模型评估** Gemini等3个LLM在中医国家执业医师考试上的系统评估 [上海交通大学] [[DOI](https://doi.org/10.1038/s41598-026-49200-z)]
- [*Guidelines and Standards of Chinese Medicine*] **中医大模型临床实践评测方法** 针对现有医学大模型评测以西医范式为主、缺少中医专用标准的问题，构建面向临床实践的中医大模型评测方法 [中国中医科学院] [[DOI](https://doi.org/10.1097/gscm.0000000000000123)]
- [*npj Digital Medicine*] **中医场景中医疗大模型的提示词效应** 在中医任务上评估16个大模型，说明提示词效应随模型而变，制约医疗大模型在中医场景的稳定部署 [长庚纪念医院，阳明交通大学，长庚大学] [[DOI](https://doi.org/10.1038/s41746-026-03397-5)]
- [*JMIR Formative Research*] **中医临床决策5-LLM对比** 5个LLM中医临床决策能力对比研究 [南京中医药大学] [[DOI](https://doi.org/10.2196/80167)]
- [*arXiv*] **TongueDx2** 舌诊深度学习设计空间系统消融研究（20+模型版本），含5109图像/976专家标注 [[论文](https://arxiv.org/abs/2607.28148)]
- [*arXiv*] **TCMQA** 38279道中医执照考试题，并配101名执业医师的15151条作答作为人类参照 [[论文](https://arxiv.org/abs/2609.33014)]
- [*Frontiers in Artificial Intelligence*] **TCMI-F-6D** 中医信息学跨学科基础能力六维基准 [安徽中医药大学] [[DOI](https://doi.org/10.3389/frai.2026.1780967)] [[代码](https://github.com/123adf-dev/TCMI-F-6D-Benchmark)]
- [*arXiv*] **TCMClinicalReason-Bench** 用2000份多中心电子病历，检验模型能否按病例证据完成从病因病机、证候、治则到处方的推理 [南京中医药大学] [[论文](https://arxiv.org/abs/2610.04215)]
- [*ICIC 2026*] **TCMBenchEval** 基于真实临床医案的LLM中医评测基准 [汕头大学] [[DOI](https://doi.org/10.1007/978-981-92-3498-1_1)]
- [*WISE 2025*] **TCM-Eval (WISE 2025)** 天津大学、天津大学福州国际联合学院、天津中医药大学及其第一附属医院、天津大学国际工程师学院合作的多维中医评测框架；与智明堂TCM-Eval（arXiv 2511.07148）同名但为不同工作 [天津大学，天津大学福州国际联合学院，天津中医药大学，天津中医药大学第一附属医院，天津大学国际工程师学院] [[DOI](https://doi.org/10.1007/978-981-95-7251-9_15)]
- [*Scientific Data*] **TCM-BEST4SDT** 600 条评测样本：300 条辨证论治病例，以及中医基础知识、医学伦理和内容安全各 100 题；涵盖 27 个评价维度。 [[DOI](https://doi.org/10.6084/m9.figshare.30615956)] [[论文](https://arxiv.org/abs/2512.02816)] [[代码](https://github.com/DYJG-research/TCM-BEST4SDT)] [[正式发表](https://doi.org/10.1038/s41597-026-07587-4)]
- [*Communications Medicine*] **TCM-3CEval** 中医大模型三轴评测（核心知识、经典理解、临床决策） [[论文](https://arxiv.org/abs/2503.07041)] [[正式发表](https://doi.org/10.1038/s43856-026-01631-5)]
- [*Frontiers in Medicine*] **Supporting postgraduate exam preparation with large language models: implications for traditional Chinese medicine education** 在2023年中医考研题上，文心一言准确率50.30%、ChatGLM为46.67%，两者都超过及格线，医学人文模块得分最高。 [Beijing University of Chinese Medicine，Dongzhimen Hospital Affiliated to Beijing University of Chinese Medicine，Changchun University of Chinese Medicine，Leipzig University] [[DOI](https://doi.org/10.3389/fmed.2025.1667104)]
- [*JMIR*] **STC-NF：中医症状术语两段式规范化** 针对一条原文对应多个症状、缺少行业标准术语的问题，先把症状拆成 12 类细粒度语义，再用三个命名实体识别模型做两段式规范化，拼回标准术语。数据来自电子病历。 [[DOI](https://doi.org/10.2196/85825)]
- **Med-Bench-Arena** 面向医学与中医药LLM/Agent的开源评测平台，支持HF/vLLM/LiteLLM、多模态与中医特色指标（ZhongJing团队） [[代码](https://github.com/pariskang/Med-Bench-Arena)]
- [*Scientific Data*] **MTCMB** 中医多任务评测基准，12 个数据集、7,100 个样本，覆盖知识、推理、方剂与安全任务（Scientific Data 2026）。 [[论文](https://arxiv.org/abs/2506.01252)] [[代码](https://github.com/Wayyuanyuan/MTCMB)] [[正式发表](https://doi.org/10.1038/s41597-026-07967-w)]
- [*arXiv*] **MMIR-TCM** 记忆增强的多模态舌诊与临床决策框架，提出 MedTCM 数据集与 TDEU 评测指标 [[论文](https://arxiv.org/abs/2607.01814)]
- [*arXiv*] **LingLanMedBench（灵兰）** LingLanMedBench（原 LingLanMiDian）：5 大域、13 个子任务，共 25,620 条专家核验样本；每个子任务从完整集内选取 400 条构成 Hard 子集。 [北京交通大学等] [[论文](https://arxiv.org/abs/2602.01779v2)] [[代码](https://github.com/TCMAI-BJTU/LingLan)] [[网站](http://tcmnlp.com)]
- [*Brain Behavior and Immunity Integrative*] **Large language models vs traditional Chinese medicine clinical reasoning: Analysis of a single migraine case study** 在一份标准化偏头痛病例上，9个大语言模型与两名中医师及已发表病例对照作答，32名专家盲评；GPT o3、Qwen 3和Gemini 2.5 Pro在部分维度上不低于对照，Aya Expanse 32B得分更低。 [Harvard University，Massachusetts General Hospital] [[DOI](https://doi.org/10.1016/j.bbii.2026.100192)]
- [*arXiv*] **Large Language Models Versus Physicians in Traditional Chinese Medicine: A Real-World Clinical Case Evaluation** 作者收集62家医院349例脱敏门诊病例，用其中60例比较16个大语言模型和60名执业中医师，并由5名资深中医专家按9个诊疗维度盲评。 [University of Missouri，Seventh People's Hospital of Shanghai，Yunnan University of Traditional Chinese Medicine，Northwestern University] [[论文](https://arxiv.org/abs/2609.17544)]
- [*JMIR Formative Research*] **Korean Medical Consultation With Open-Weight Large Language Models: Pilot Comparative Evaluation of Retrieval-Augmented Generation With Metadata Filtering** 用开源权重大模型和检索增强做韩医问诊聊天机器人，并比较带元数据过滤的检索增强效果。 [[DOI](https://doi.org/10.2196/72604)]
- [*Frontiers in Medicine*] **Knowledge-guided adaptive educational support for traditional Chinese medicine using large language models and knowledge graphs: integrating Confucian educational principles** 该智能中医辅导系统把大语言模型接到由《医宗金鉴》构建的知识图谱上；125名学生志愿者中102份问卷纳入分析，集成系统的即时后测成绩高于纯大语言模型组和自学组。 [Anhui University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.3389/fmed.2026.1943401)]
- [*AI Engineering*] **Knowledge of Chatbots on Oriental Medicine-Based Theory and Practice of Acupuncture Is Inferior to That on Western Medicine-Based Acupuncture-Transmitted Infections** 用 2528 道东方医学针灸理论与操作题、100 道针灸相关感染题，比较五个免费聊天机器人（ChatGPT、Claude、Copilot、Gemini、Perplexity）和三个订阅版（ChatGPT、Claude、Perplexity）。针灸理论中位分 75%，低于感染题的 86%。 [National Chung Hsing University，Tung Wah College，The University of Hong Kong，Fuke Fengze Chinese Medicine Clinic] [[DOI](https://doi.org/10.53941/aieng.2026.100004)]
- [*medRxiv*] **KampoBench** 医师修订的汉方问诊基准：74个问诊场景、310条对话级评分标准，评的是问诊应用而不是考试得分 [[DOI](https://doi.org/10.64898/2026.10.07.26365005)]
- [*Terminology International Journal of Theoretical and Applied Issues in Specializ*] **From readable to executable** 作者用同一套三种提示，让ChatGPT-4o检验世界卫生组织2007年和2022年中医术语标准是否给出了足够明确的信息，以便在并存的英译变体中做可审计的选择。 [University of Malaya] [[DOI](https://doi.org/10.1075/term.00097.yu)]
- [*proceedings-article*] **Evaluating Semantic Fidelity and Cohesion in NMT and LLM-based Translation of Traditional Chinese Medicine Classics** 在中医经典英译上，以BERTScore对照人工参考译文，DeepSeek的语义保真高于Google Translate和ChatGPT-5，而ChatGPT-5的句间语义连贯更好。 [Northwestern Polytechnical University，Air Force Engineering University] [[DOI](https://doi.org/10.1109/icnlp69856.2026.11528039)]
- [*Current Bioinformatics*] **Evaluating Large Language Models for Query Refinement in Systematic Review Retrieval of Traditional Chinese Medicine** 作者用GPT-4o、GPT-5、DeepSeek-V3和DeepSeek-R1、六种提示，在知网、万方、PubMed和Embase上检索银屑病、新冠肺炎和2型糖尿病文献；去重后的金标准集有182条记录（分别为50、74和58条）。 [China Academy of Chinese Medical Sciences，Hunan University of Traditional Chinese Medicine] [[DOI](https://doi.org/10.2174/0115748936492177260915061800)]
- [*JMIR Formative Research*] **ChatGPT、DeepSeek与医师针灸方案对照** 比较ChatGPT、DeepSeek和医师生成的针灸治疗方案 [[DOI](https://doi.org/10.2196/95851)]
- [*Pattern Recognition*] **ATCMD-Bench** 首个Agentic中医诊断基准，通过多智能体模拟问诊评估LLM诊疗能力 [华南理工大学] [[DOI](https://doi.org/10.1016/j.patcog.2026.113679)]

</details>

<details>
<summary>2025 · 19</summary>

- [*Expert Systems with Applications*] **针灸大模型驯化与生成评估 (Taming LLMs for Acupuncture)** 面向针灸推拿诊断的大模型驯化方法，并在语义相似度层面评估生成质量 [[DOI](https://doi.org/10.1016/j.eswa.2024.125920)]
- [*JMIR Medical Informatics*] **辨证思维评测 (Syndrome Differentiation Thinking)** 评估并提升大语言模型中医辨证思维能力的方法开发研究 [[DOI](https://doi.org/10.2196/75103)]
- [*Bulletin of the World Health Organization*] **国际疾病分类与传统医学数据缺口** 讨论国际疾病分类体系里传统医学数据仍然缺失的问题。 [[DOI](https://doi.org/10.2471/blt.25.293540)]
- [*BMC Medical Informatics and Decision Making*] **中医症状的细粒度实体与关系抽取** 针对病历里半结构化、会嵌套的症状描述，做细粒度症状实体和关系抽取，避免粗标注把信息丢掉。 [[DOI](https://doi.org/10.1186/s12911-025-03257-4)]
- [*UbiComp Companion 2025*] **中医大模型误导信息检测评测** 评估大语言模型的中医知识表现与误导信息检测能力。 [清华大学] [[DOI](https://doi.org/10.1145/3714394.3756275)]
- [*JMIR Formative Research*] **中医卒中LLM评测** 中医卒中领域LLM定量基准研究 [成都中医药大学] [[DOI](https://doi.org/10.2196/81545)]
- [*Frontiers in Pharmacology*] **中医临床指南遵循评估** LLM遵循中医临床实践指南的内容分析评估 [兰州大学] [[DOI](https://doi.org/10.3389/fphar.2025.1649041)]
- [*CCL 2025*] **TCM-TBOSD 辨证论治评测** CCL 2025 评测任务。齐鲁工业大学（山东省科学院）与山东中医药大学附属医院用脱敏病历做成 TCM-TBOSD，1500 条，覆盖 10 种证型、4 种疾病、381 味药。处方字段是药名列表，论文写明不包括剂量。仓库有基线代码和数据使用保密承诺书，病例表没有直接放在文件列表里。 [齐鲁工业大学（山东省科学院），山东中医药大学附属医院] [[论文](https://aclanthology.org/2025.ccl-2.45/)] [[PDF](https://aclanthology.org/2025.ccl-2.45.pdf)] [[代码](https://github.com/QLU-NLP/TCM-Syndrome-and-Disease-Differentiation-and-Prescription-Recommendation)]
- [*NeurIPS 2025*] **TCM-Ladder** 中医多模态问答基准，含 52,169 个问答对，并包含图像、音频和视频数据（NeurIPS 2025）。 [[论文](https://arxiv.org/abs/2505.24063)] [[代码](https://github.com/orangeshushu/TCM-Ladder)] [[HF](https://huggingface.co/datasets/timzzyus/TCM-Ladder)] [[榜单](https://tcmladder.com)] [[正式发表](https://proceedings.neurips.cc/paper_files/paper/2025/file/cbdd26a4490f5a8dad0d732508714029-Paper-Datasets_and_Benchmarks_Track.pdf)]
- [*arXiv*] **TCM-5CEval** 五维中医评测，含来自 30 门课程的 2,260 道题；对选择题进行选项循环置换，以检验回答对选项位置的敏感性。 [[论文](https: