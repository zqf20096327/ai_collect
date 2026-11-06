# 🔥 开源中医模型、数据、论文、专利

**语言 / Language:** [中文](README.md) | [English](README_EN.md)

![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-green)  [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) ![Stars](https://img.shields.io/github/stars/tyang816/Awesome-TCM-LLM?color=yellow)  ![Forks](https://img.shields.io/github/forks/tyang816/Awesome-TCM-LLM?color=blue&label=Fork) [![中文门户](https://img.shields.io/badge/中医资源-门户-blue)](https://tyang816.github.io/zh/projects/tcm/) [![Project](https://img.shields.io/badge/Project-tyang816.github.io-informational)](https://tyang816.github.io/projects/tcm/)

开源中医模型、数据、论文、专利精选，也带一点相关中文医疗。现在大概有 60 条新闻、116 个模型、71 篇综述、73 件专利、201 个数据集、387 篇方法论文，以及 445 位中医药人工智能导师。[欢迎补条目](CONTRIBUTING.md)。

[项目页](https://tyang816.github.io/projects/tcm/) · [中文项目页](https://tyang816.github.io/zh/projects/tcm/) · [Wiki](wiki/Home.md) · [主页](https://tyang816.github.io/zh/)

## 先看这里

真能下载复现的中医权重大概 20 个，都在[开源模型](#开源模型)里。新闻里医院、公司发的，多数没有公开权重，当不了实验底座。

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
| 找导师 | [导师](#导师) | 高校、产业、医院 |

同名不一定是同一个东西。「仲景」至少有 ZhongJingGPT 和 AAAI 那条 CMtMedQA；TCM-Eval 也不止一套。说不清时看 [Getting Started](wiki/Getting-Started.md)。

## 导师

先按地区，再按高校、医院或公司。

<details>
<summary>北京（80）</summary>

<details>
<summary>北京中医药大学（24）</summary>

- **陈建新** 北京中医药大学生命科学学院教授、博士生导师。做中医药数据挖掘和中西医结合人工智能，建设 SymMap。2026 年招收中医信息学、中医药大数据方向博士。 [北京中医药大学生命科学学院] [[主页](https://shengming.bucm.edu.cn/jyjx/yjs/dsfc/584c26a2af124c56841daf796c2d24c4.htm)] [[招生](https://shengming.bucm.edu.cn/docs/2026-03/094923d029c745a7aa5b3f7493ee8d2c.pdf)]
- **郭津丞** 北京中医药大学中医学院教授、博士生导师。做中医药生物信息学、数字孪生与智能体，建设 HERB、POINT。2026 年与中国科学院赵屹联合招收中医药生物信息学博士。 [北京中医药大学中医学院] [[主页](https://jichu.bucm.edu.cn/xygk/jxkyjg/yjstpt/zyxxxyjzx/szdw22/b1fbbc5c520c4cd88e780576f381dc05.htm)] [[招生](https://shengming.bucm.edu.cn/docs/2026-03/445adae3d9514d6580b200fb317f602c.pdf)]
- **谷晓红** 北京中医药大学教授、博士生导师，中医疫病研究院院长。做温病与名医数智传承，并与曹鹏等合作发表中医大模型天医。 [北京中医药大学] [[主页](https://jichu.bucm.edu.cn/xygk/jxkyjg/jys/wbjys/szdw6/220d8b80aef84862a6355b25dfef5f29.htm)] [[新闻](https://www.njucm.edu.cn/2025/0910/c6754a160459/page.htm)]
- **徐冰** 北京中医药大学中药学院教授、博士生导师、副院长。做中药智能制药，建设 iTCM 智慧制药系统，并负责薪火中国药大模型建设。 [北京中医药大学中药学院] [[主页](https://infopharm.bucm.edu.cn/kxyj/yjdw/31874.htm)] [[新闻](https://zhongyao.bucm.edu.cn/yyxw/57d9fb0a8af1496b88ca404e51e4e7d1.htm)]
- **张晓晴** 北京中医药大学生命科学学院博士生导师。做人工智能与中医数量化辨证、头面望诊和智慧中医装备。 [北京中医药大学生命科学学院] [[主页](https://shengming.bucm.edu.cn/jyjx/yjs/dsfc/31df29a5d6b04e539b7a90e1bff9d2bc.htm)] [[招生](https://shengming.bucm.edu.cn/docs/2026-03/9f61983b960a443ea888399d6d5b09d5.pdf)]
- **吴志生** 北京中医药大学研究员、博士生导师，中药智能制造学科带头人。做中药制造测量和中药智造平台。 [北京中医药大学] [[主页](https://infopharm.bucm.edu.cn/kxyj/yjdw/44025.htm)]
- **王耘** 北京中医药大学中药学院研究员、博士生导师，中药信息学系主任。做中药信息融合、药性组合智能设计，以及大模型与知识图谱。 [北京中医药大学中药学院] [[主页](https://zhongyao.bucm.edu.cn/szdw/sssds/szzyxssds/f55f7fd12b174137b01a59dd3d256dd1.htm)]
- **张燕玲** 北京中医药大学中药学院研究员、博士生导师。从虚拟筛选做到人工智能组方。 [北京中医药大学中药学院] [[主页](https://zhongyao.bucm.edu.cn/szdw/bssds/szzyx_20220622170829152708/a2c5cdca5e504f91b7f702a883bdd762.htm)]
- **张玫** 北京中医药大学研究员、博士生导师。研发数智中医嗅诊装备，推动闻诊与辨证客观化。 [北京中医药大学] [[主页](https://zhongyao.bucm.edu.cn/szdw/bssds/zyfxxbsds_20220622170729411401/d86a8ba8fa764445b796a6f218c2a79d.htm)]
- **王济** 北京中医药大学教授、博士生导师，国家中医体质与治未病研究院常务副院长。做中医体质、人工智能和数字健康。 [北京中医药大学] [[主页](https://tizhi.bucm.edu.cn/szdw/jsjj/2efe37af25e147e5af41ad78f80c669f.htm)]
- **张正军** 北京中医药大学数据科学与人工智能学院院长。用大数据和系统药理学打通辨证到精准用药。 [北京中医药大学数据科学与人工智能学院] [[新闻](http://finance.people.com.cn/n1/2026/0817/c1004-40781088.html)]
- **王旭** 北京中医药大学生命科学学院副研究员、硕士生导师。用图像和人工智能做舌、面、脑多模态证候分析。 [北京中医药大学生命科学学院] [[主页](https://shengming.bucm.edu.cn/jyjx/yjs/dsfc/ede8719994ab4d14904fd1e3f67bc5cd.htm)]
- **乔延江** 北京中医药大学教授、博士生导师。做中药信息学、药性数据和智能制造。 [北京中医药大学] [[主页](https://infopharm.bucm.edu.cn/kxyj/yjdw/31864.htm)]
- **牛欣** 北京中医药大学中医学院二级教授、博士生导师。做四诊合参数字化，研发脉诊仪和四诊合参辅助诊疗仪。 [北京中医药大学中医学院] [[主页](https://www.ais.cn/mentor/mentorDetail/e9bed53e-5e3b-11ec-b045-a85e45a23623)]
- **杨学智** 北京中医药大学教授。负责便携式中医四诊合参辅助诊疗仪，把望闻问切集到一台设备。 [北京中医药大学] [[主页](https://www.bucm.edu.cn/bzyyw/10779fdcfccf41a5b46e1f58530374ab.htm)]
- **王琦** 北京中医药大学中国工程院院士、国医大师。做中医体质辨识体系和数字化监测。 [北京中医药大学] [[主页](https://kgyjzzx.bucm.edu.cn/kjcg/zhcg/b523b0ce71924f8ea8ff5352b2252f0f.htm)]
- **关静** 北京中医药大学中医学院中医诊断学副教授、硕士生导师。做舌诊客观化，参与智能舌诊仪研制。 [北京中医药大学中医学院] [[主页](https://jichu.bucm.edu.cn/yjsjy/dsjs/zyzdx/78a37699a21e462bad60e04054b85890.htm)]
- **马星光** 北京中医药大学管理学院教授、研究生导师。做中医药数据库、名医医案挖掘和舌诊图像识别。 [北京中医药大学管理学院] [[主页](https://sm.bucm.edu.cn/szdw/ywds/880e3600089f422e8e747b9eeb6da0f6.htm)]
- **史新元** 北京中医药大学中药学院教授、博士生导师。做中药信息学、生产过程质量控制和近红外定量建模。 [北京中医药大学中药学院] [[主页](https://infopharm.bucm.edu.cn/kxyj/yjdw/31867.htm)]
- **李楠** 北京中医药大学中药信息工程研究中心副研究员、硕士生导师。做中药生产过程质量控制。 [北京中医药大学中药学院] [[主页](https://infopharm.bucm.edu.cn/kxyj/yjdw/index.htm)]
- **戚武振** 北京中医药大学中药学院讲师。做中药智能制造仪器、光谱传感和关键质量属性检测。 [北京中医药大学中药学院] [[主页](https://infopharm.bucm.edu.cn/kxyj/yjdw/77133.htm)]
- **戴幸星** 北京中医药大学中药学院高级实验师。做炮制工程装备、智能感官评价和过程质量数字化。 [北京中医药大学中药学院] [[主页](https://sysglzx.bucm.edu.cn/zxgk/jsdw/710b407f00ea4135b3d0d4612168b9a0.htm)]
- **闫聪** 北京中医药大学生命科学学院教授、博士生导师。具身智能推拿机器人研发负责人，用专家大模型复现名医手法。 [北京中医药大学生命科学学院] [[主页](https://shengming.bucm.edu.cn/jyjx/yjs/dsfc/553c4da4cd0943208218068860bff928.htm)]
- **郭淑贞** 北京中医药大学中医学院教授、博士生导师。做中西医结合药理，是 BATMAN-TCM 2.0 共同通讯作者。 [北京中医药大学中医学院] [[主页](https://jichu.bucm.edu.cn/xygk/jxkyjg/syzx/kysyzx/szdw28/9c337b804aed4160aaa36a33703db7da.htm)]

</details>

<details>
<summary>中国中医科学院（20）</summary>

- **许海玉** 中国中医科学院首席研究员，中药研究所整合中药学研究中心主任。做整合药理学与中医药大数据，建设 ETCM、SoFDA。2026 年在辽宁中医药大学招收中医人工智能科学与技术方向博士。 [中国中医科学院中药研究所] [[主页](https://www.icmm.ac.cn/zjjj/sxyjyd/content_128.html)] [[招生](https://gjhzjlc.lnutcm.edu.cn/liaoningzhongyiyaodaxue2026nianshenqing-kaohejishuobolianduboshiyanjiushengzhaoshengzhuanyemuluxueshuxuewei.pdf)]
- **刘保延** 中国中医科学院首席研究员。做中医临床疗效评价与中医药大数据，参与灵丹-V2，并与固生堂合作中医药大模型和真实世界数据。 [中国中医科学院] [[简介](https://www.ch-s.wtcmaw.events/%E5%8F%82%E4%BC%9A%E5%8D%95%E4%BD%8D/%E4%B8%BB%E5%B8%AD%E5%9B%A2/speaker-bio-%E5%88%98%E4%BF%9D%E5%BB%B6)] [[论文](https://arxiv.org/abs/2610.14705)] [[新闻](https://www.gstzy.cn/news/detail/10/14073.html)]
- **于彤** 中国中医科学院中医药信息研究所研究员、硕士生导师。做中医药知识图谱、术语系统和垂直领域大模型。 [中国中医科学院中医药信息研究所] [[主页](http://www.cintcm.ac.cn/tutor.thtml?id=8370)]
- **于琦** 中国中医科学院中医药信息研究所研究员、硕士生导师。做名医传承信息化、临床知识库和中医药人工智能。 [中国中医科学院中医药信息研究所] [[主页](http://www.cintcm.ac.cn/tutor.thtml?id=8272)]
- **李敬华** 中国中医科学院中医药信息研究所研究员、博士生导师，大健康智能研发中心主任。做中医临床辅助决策、古今医案平台和四诊机器人。 [中国中医科学院中医药信息研究所] [[主页](http://www.cintcm.ac.cn/tutor.thtml?id=8351)]
- **李海燕** 中国中医科学院中医药信息研究所研究员、博士生导师。做大模型中成药推荐，并用于医源中医大模型。 [中国中医科学院中医药信息研究所] [[主页](http://www.cintcm.ac.cn/tutor.thtml?id=8065)]
- **李兵** 中国中医科学院中药研究所研究员，本草数智中心副主任。做中医典籍知识图谱、古籍大模型和临床辅助决策。 [中国中医科学院中药研究所] [[主页](https://wenxian.sdutcm.edu.cn/info/1040/2352.htm)]
- **张彦琼** 中国中医科学院中药研究所研究员、博士生导师，中药药性理论研究中心主任。用组学大数据和生物网络解析中药作用与合理用药。 [中国中医科学院中药研究所] [[主页](https://zhongyao.bucm.edu.cn/szdw/bssds/lczyxbsds_20220622170829152708/a055bcd9f9a04c558a83f4a9c8c28ede.htm)]
- **杨洪军** 中国中医科学院副院长，研究员、博士生导师。做整合药理学和中医传承辅助平台，并提出 AI4TCM。 [中国中医科学院] [[主页](https://www.merc.ac.cn/zykx/detail.html?contentId=89&id=13)]
- **汪南玥** 中国中医科学院医学实验中心研究员、博士生导师。做四诊设备和人工智能四诊合参。 [中国中医科学院医学实验中心] [[主页](https://www.merc.ac.cn/zykx/detail.html?contentId=11&id=13)]
- **朱彦** 中国中医科学院中医药信息研究所副研究员、硕士生导师。做中医药术语、领域本体和方剂数据挖掘。 [中国中医科学院中医药信息研究所] [[主页](http://www.cintcm.ac.cn/tutor.thtml?id=8343)]
- **文天才** 中国中医科学院中医药数据中心正高级工程师、博士生导师。做真实世界病历挖掘和辅助决策。 [中国中医科学院中医药数据中心] [[主页](http://www.cintcm.ac.cn/tutor.thtml?id=8372)]
- **王俊文** 中国中医科学院中医基础理论研究所研究员、博士生导师。做智能中医辅助诊断技术和装备。 [中国中医科学院中医基础理论研究所] [[主页](https://www.ibtcm.ac.cn/zjds-detail.thtml?contentId=8342)]
- **陈士林** 成都中医药大学首席教授、中国中医科学院首席研究员。创立本草基因组学，建成中药全产业链大模型本草智库。 [成都中医药大学，中国中医科学院] [[新闻](https://academics.casad.cas.cn/xshd/kxyjsqylt/2024/d180c/202507/t20250731_5078674.html)]
- **赵玉凤** 中国中医科学院中医药信息研究所研究员、博士生导师，中医药数据中心副主任。做真实世界中医药大数据分析。 [中国中医科学院中医药信息研究所] [[主页](http://www.cintcm.ac.cn/tutor.thtml?id=8349)]
- **杨硕** 中国中医科学院中医药信息研究所研究员、硕士生导师。做中医证候本体、循证知识表达和数字化。 [中国中医科学院中医药信息研究所] [[主页](http://www.cintcm.ac.cn/tutor.thtml?id=8353)]
- **高俊虹** 中国中医科学院针灸研究所研究员、博士生导师，针刺手法研究室主任。研究针灸效应机制并研发针灸装备。 [中国中医科学院针灸研究所] [[主页](https://www.acuworld.ac.cn/info_content_ds.jsp?id=922)]
- **荣培晶** 中国中医科学院首席研究员、博士生导师，针灸研究所副所长。主持经脉功能脑表征研究，其中含经脉知识图谱。 [中国中医科学院针灸研究所] [[主页](http://www.acuworld.ac.cn/info_content.jsp?id=1583)]
- **黄璐琦** 中国中医科学院院长、研究员。做分子生药学和中药分子鉴定。 [中国中医科学院] [[主页](https://www.nrc.ac.cn/rcyjy/rcdw/yjy/eb9d33d888a14d189c75d46fc19ced5b.htm)]
- **袁媛** 中国中医科学院首席研究员、博士生导师。做中药鉴定和分子生药学。 [中国中医科学院] [[主页](https://www.nrc.ac.cn/rcyjy/rcdw/yjy/6c76223ab0574c35a0e8e0e35ab67249.htm)]

</details>

<details>
<summary>清华大学（5）</summary>

- **李梢** 清华大学教授、博士生导师，北京市中医药交叉研究所所长。做网络药理学与中医药人工智能，研究肿瘤等复杂疾病的中西医防治，招收博士后和工程博士。 [清华大学自动化系，清华大学北京市中医药交叉研究所] [[主页](https://www.tcm-x.tsinghua.edu.cn/info/1512/2662.htm)] [[招生](https://www.tcm-x.tsinghua.edu.cn/zszp.htm)]
- **孙茂松** 清华大学计算机系长聘教授、博士生导师，人工智能研究院常务副院长。做自然语言处理与大模型，团队与固生堂合作研发中医药大模型。 [清华大学计算机系，清华大学人工智能研究院] [[主页](https://nlp.csai.tsinghua.edu.cn/staff/sms/)] [[新闻](https://www.gstzy.cn/news/detail/10/14076.html)]
- **张鹏** 清华大学自动化系副研究员，北京市中医药交叉研究所副所长。参与中医消化模型 GastroTCM。 [清华大学自动化系，清华大学北京市中医药交叉研究所] [[主页](https://www.tcm-x.tsinghua.edu.cn/kydw.htm)]
- **罗国安** 清华大学化学系教授。提出中医药系统对系统研究，并做中药指纹图谱。 [清华大学化学系] [[主页](https://www.chem.tsinghua.edu.cn/info/1089/1941.htm)]
- **梁琼麟** 清华大学化学系长聘教授、博士生导师。做中药现代化、质谱多组学和器官芯片分析。 [清华大学化学系] [[主页](https://www.chem.tsinghua.edu.cn/info/1095/2735.htm)]

</details>

<details>
<summary>北京科技大学（3）</summary>

- **张德政** 北京科技大学计算机与通信工程学院教授、博士生导师。做中医知识图谱和智能辅助诊断，团队发布张仲景中医药大模型，并受聘河南中医药大学特聘教授。 [北京科技大学计算机与通信工程学院] [[主页](https://faculty.ustb.edu.cn/DezhengZhang/zh_CN/index.htm)] [[新闻](https://news.ustb.edu.cn/info/1087/67760.htm)]
- **阿孜古丽·吾拉木** 北京科技大学计算机与通信工程学院教授、博士生导师。做多维望诊融合和中医临床智能辅助诊断，并指导中医药大模型。 [北京科技大学计算机与通信工程学院] [[主页](https://it.xju.edu.cn/info/1327/2835.htm)] [[新闻](https://news.ustb.edu.cn/info/1981/67772.htm)]
- **谢永红** 北京科技大学计算机学院副教授、硕士生导师。参与张仲景中医药大模型，并做过中医知识图谱。 [北京科技大学计算机与通信工程学院] [[主页](https://faculty.ustb.edu.cn/YonghongXie/zh_CN/index.htm)]

</details>

<details>
<summary>中国中医科学院望京医院（2）</summary>

- **成永忠** 中国中医科学院望京医院主任医师、博士生导师。主持中医正骨智能接骨手术机器人。 [中国中医科学院望京医院] [[新闻](https://zyj.beijing.gov.cn/sy/rdzt/bjyyjkxtzyygzlyfgc/202501/P020250124625181340715.pdf)]
- **冯敏山** 中国中医科学院望京医院主任医师、博士生导师。介绍颈椎病名医经验垂直大模型。 [中国中医科学院望京医院] [[招生](https://yanjiusheng.bucm.edu.cn/docs/2024-12/c2448d698eca42848387882e725da184.pdf)]

</details>

<details>
<summary>中国中医科学院西苑医院（2）</summary>

- **徐浩** 中国中医科学院首席研究员、西苑医院副院长。用深度神经网络做名老中医知识库和智能辅助诊疗。 [中国中医科学院西苑医院] [[新闻](https://xyhospital.com/Html/News/Articles/21500.html)]
- **庞博** 中国中医科学院西苑医院副院长、博士生导师。分管信息，介绍本院数字孪生智能诊室。 [中国中医科学院西苑医院] [[主页](https://www.xyhospital.com/Html/News/Articles/22270.html)]

</details>

<details>
<summary>中日友好医院（2）</summary>

- **杜时雨** 中日友好医院消化科主任、博士生导师。中医脾胃大模型 GastroTCM 通讯作者。 [中日友好医院] [[主页](https://www.zryhyy.com.cn/zryh/c100442/zjxx.shtml)]
- **左先波** 中日友好医院大数据研究部主任。介绍本院可信数据空间和专病大模型。 [中日友好医院] [[主页](https://www.zryhyy.com.cn/zryh/c105700/zjxx.shtml)]

</details>

<details>
<summary>北京中医药大学东方医院（2）</summary>

- **骆长永** 北京中医药大学东方医院硕士研究生导师。做中医人工智能及疫病、慢病智能化防治，发表中医大模型天医。 [北京中医药大学东方医院] [[主页](https://www.dongfangyy.com.cn/Html/News/Articles/13293.html)] [[论文](https://doi.org/10.1016/j.inffus.2025.103663)]
- **商洪才** 北京中医药大学东方医院院长，研究员、博士生导师。做广义望诊智能采集和中医临床辅助决策。 [北京中医药大学东方医院] [[主页](https://dongfangyy.com.cn/Html/News/Articles/12504.html)]

</details>

<details>
<summary>北京大学（2）</summary>

- **屠鹏飞** 北京大学药学院教授、博士生导师，中医药现代研究中心主任。做中药靶点鉴定，并用量子化学计算鉴定化学异构体。 [北京大学药学院] [[主页](https://dnm.bjmu.edu.cn/szdw_20180110150803713087/trywhxyjs_20180110150803713087/192678.htm)]
- **曾克武** 北京大学药学院研究员、博士生导师。用蛋白质组方法鉴定中药成分的直接靶点。 [北京大学药学院] [[主页](https://dnm.bjmu.edu.cn/szdw_20180110150803713087/trywhxyjs_20180110150803713087/192684.htm)]

</details>

<details>
<summary>北京工业大学（2）</summary>

- **张新峰** 北京工业大学信息学部副教授、硕士生导师。做舌图像分割、多标签分类和多模态舌象感知。 [北京工业大学信息学部] [[主页](https://sist.bjut.edu.cn/info/1517/4319_2.htm)]
- **蔡轶珩** 北京工业大学信息学部教授、博士生导师。做舌象全维度采集、望诊色彩标准化和智能舌诊系统。 [北京工业大学信息学部] [[主页](https://sist.bjut.edu.cn/info/1426/2320.htm)]

</details>

<details>
<summary>国家蛋白质科学中心（北京）（2）</summary>

- **刘中扬** 国家蛋白质科学中心（北京）副研究员、硕士生导师。用人工智能和知识图谱做药物发现，是 BATMAN-TCM 2.0 共同通讯作者。 [国家蛋白质科学中心（北京）] [[主页](https://i-share.ncpsb.org.cn/genee/post/176)]
- **李栋** 国家蛋白质科学中心（北京）研究员、博士生导师。做生命组学大数据挖掘，是 BATMAN-TCM 2.0 共同通讯作者。 [国家蛋白质科学中心（北京）] [[主页](http://i-share.ncpsb.org.cn/genee/post/172)]

</details>

<details>
<summary>中国中医科学院广安门医院（1）</summary>

- **刘震** 中国中医科学院广安门医院党委书记。牵头四诊与辨证大模型，并发布广医·岐智。 [中国中医科学院广安门医院] [[新闻](https://www.gamyy.cn/gzb/news/big/115621.html)]

</details>

<details>
<summary>中国科学院计算技术研究所（1）</summary>

- **吴杨** 中国科学院计算技术研究所副研究员、课题负责人。建设 HERB、SymMap、POINT 等中药大数据平台。 [中国科学院计算技术研究所] [[主页](https://www.ict.ac.cn/sourcedb/cn/jssrck/202211/t20221101_6543064.html)]

</details>

<details>
<summary>中科闻歌（1）</summary>

- **王磊** 中国科学院自动化研究所研究员，中科闻歌董事长。与中国中医科学院联合研发大医金匮，并任中医药智能科学与工程技术研究中心学术指导委员会委员。 [中科闻歌，中国科学院自动化研究所] [[新闻](https://news.sciencenet.cn/htmlnews/2025/5/544108.shtm)] [[网站](https://tcm.wenge.com/)]

</details>

<details>
<summary>传神语联（1）</summary>

- **何恩培** 传神语联创始人、董事长兼首席执行官。公司发布任度大模型和传神素问中医大模型。 [传神语联] [[主页](https://www.transn.com/mobile/about_us/intro)]

</details>

<details>
<summary>北京中医药大学东直门医院（1）</summary>

- **刘春玲** 北京中医药大学东直门医院数字化与智慧医院建设处处长。推进本院智慧医院和数智融合。 [北京中医药大学东直门医院] [[新闻](https://yxb.dzmyy.com.cn/Html/News/Articles/18348.html)]

</details>

<details>
<summary>北京交通大学（1）</summary>

- **周雪忠** 北京交通大学计算机学院教授、博士生导师、人工智能系系主任。做中医药知识图谱、大语言模型和临床人工智能，团队发布灵丹、灵丹-V2。 [北京交通大学计算机学院] [[主页](https://faculty.bjtu.edu.cn/8029/)] [[论文](https://arxiv.org/abs/2610.14705)] [[代码](https://github.com/TCMAI-BJTU/Lingdan-V2)]

</details>

<details>
<summary>北京博奥晶方（1）</summary>

- **杨越** 北京博奥晶方董事长。主持分子本草大模型，用通路数据做中药组方筛选和活性评价。 [北京博奥晶方] [[新闻](http://www.zj.chinanews.com.cn/jzkzj/2025-12-24/detail-iheyfaae0556576.shtml)]

</details>

<details>
<summary>北京同仁堂研究院（1）</summary>

- **王志斌** 北京同仁堂研究院院长。做中药生物活性测定和质量控制。 [北京同仁堂研究院] [[主页](https://zhongyao.bucm.edu.cn/szdw/sssds/zyylx_20220622164850036668/75851.htm)]

</details>

<details>
<summary>北京航空航天大学（1）</summary>

- **柳泽明** 北京航空航天大学计算机学院副教授。主持中医领域专业大模型关键技术研发。 [北京航空航天大学计算机学院] [[主页](https://teacher.buaa.edu.cn/liuzeming/zh_CN/kyxm/206021/content/6796.htm)]

</details>

<details>
<summary>北京邮电大学（1）</summary>

- **王光宇** 北京邮电大学研究员。中医领域自适应预训练模型 TCM-GPT 通讯作者。 [北京邮电大学] [[新闻](https://news.qq.com/rain/a/20250110A03RJT00)]

</details>

<details>
<summary>博奥生物集团（1）</summary>

- **程京** 博奥生物集团董事长兼总裁。建分子本草与中医药大模型，并推进舌诊等数字化中医诊断。 [博奥生物集团] [[主页](https://www.capitalbio.com/about/45.html)]

</details>

<details>
<summary>解放军总医院（1）</summary>

- **肖小河** 解放军总医院联合培养博士生导师。招生方向为基于精准网络药理学的中药作用机制研究。 [解放军总医院] [[招生](https://yanjiusheng.bucm.edu.cn/docs/2026-01/f524a5d2c485489ab2be485be376a2b3.pdf)]

</details>

<details>
<summary>首都医科大学附属北京中医医院（1）</summary>

- **刘宝利** 首都医科大学附属北京中医医院常务副院长、博士生导师。腹泻中医大模型 Qwen-TCM-Dia 通讯作者。 [首都医科大学附属北京中医医院] [[主页](https://www.bjzhongyi.com/gzb_team_detail/13893.html)]

</details>

<details>
<summary>首都师范大学（1）</summary>

- **郝博文** 首都师范大学管理学院副教授。与团队发布中医方剂模型知方丹台，用图谱检索增强生成方剂。 [首都师范大学管理学院] [[主页](https://glxy.cnu.edu.cn/szdw/zrjs/ggsyglzy_05f39083c56d46acbb48d86628e8cc70/index.htm)] [[论文](https://arxiv.org/abs/2509.05867)]

</details>


</details>

<details>
<summary>天津（28）</summary>

<details>
<summary>天津中医药大学（13）</summary>

- **张俊华** 天津中医药大学教授、博士生导师，现代中医药海河实验室常务副主任。做循证中医药与组分中药，团队发布中医药循证评价智能体 AireviewAgent。 [天津中医药大学中医药研究院，现代中医药海河实验室] [[主页](https://institute.tjutcm.edu.cn/info/1049/2127.htm)] [[新闻](https://www.tjutcm.edu.cn/info/1047/1971.htm)]
- **孟昭鹏** 天津大学教授、博士生导师，原天津中医药大学副校长。做人工智能与中医药，包括中医药大模型、智能问答和四诊设备。 [天津大学，天津中医药大学] [[主页](https://kjc.gyu.edu.cn/info/1008/2020.htm)] [[新闻](https://yuyanwenhua.tjutcm.edu.cn/info/1036/1916.htm)]
- **周鹏** 天津大学副教授、博士生导师。做智能中医诊断装备和中医大数据，并创办依脉人工智能。 [天津大学，天津中医药大学] [[主页](https://zhongyi.tjutcm.edu.cn/info/1105/1456.htm)]
- **庄朋伟** 天津中医药大学教师。参与海河·岐伯的方剂知识图谱增强。 [天津中医药大学] [[论文](http://fcst.ceaj.org/CN/10.3778/j.issn.1673-9418.2407082)]
- **于志峰** 天津中医药大学中医学院教授、博士生导师，中医诊断教研室主任。用舌象采集系统分析失眠舌色、舌形和舌质。 [天津中医药大学中医学院] [[主页](https://zhongyi.tjutcm.edu.cn/info/1106/1262.htm)]
- **王益民** 天津中医药大学中医工程教授、博士生导师、硕士生导师。用图像采集做舌诊规范分析。 [天津中医药大学] [[主页](https://institute.tjutcm.edu.cn/info/1049/2124.htm)]
- **陆小左** 天津中医药大学教授、博士生导师。做脉图形成机制和中医诊疗仪器。 [天津中医药大学] [[主页](http://www.tjlnrdx.cn/system/2019/08/22/012340534.shtml)]
- **李正** 天津中医药大学中药制药工程学院院长、教授。做中药制造数字孪生、干燥过程机器视觉和绿色智能制药。 [天津中医药大学中药制药工程学院] [[主页](https://zygc.tjutcm.edu.cn/info/1276/2593.htm)]
- **李文龙** 天津中医药大学中药制药工程学院博士生导师。做近红外过程分析，覆盖煎煮、醇沉、柱层析和制剂单元。 [天津中医药大学中药制药工程学院] [[主页](https://zygc.tjutcm.edu.cn/info/1107/2597.htm)]
- **于洋** 天津中医药大学中药制药工程学院助理研究员。与李正共同指导干燥过程机器视觉建模和数字孪生。 [天津中医药大学中药制药工程学院] [[主页](https://zygc.tjutcm.edu.cn/info/1276/2593.htm)]
- **潘兴芳** 天津中医药大学教授。国家重点研发计划针灸机器人技术与系统课题负责人。 [天津中医药大学] [[主页](https://www.tjutcm.edu.cn/info/1039/1393.htm)]
- **任海燕** 天津中医药大学中医学院教师、硕士生项目导师。方向含智慧中医和计算针灸，并做针灸机器人手法采集和得气分析。 [天津中医药大学中医学院] [[主页](https://zhongyi.tjutcm.edu.cn/info/1105/1243.htm)]
- **高秀梅** 天津中医药大学校长、教授。做方剂多组分、多靶点和组分配伍。 [天津中医药大学] [[主页](https://institute.tjutcm.edu.cn/szdw/gxmjs.htm)]

</details>

<details>
<summary>天士力（6）</summary>

- **王文佳** 天士力数智本草大模型负责人，并参与灵丹-V2。 [天士力] [[新闻](https://www.taslypharma.com/tsl/41063.jhtml)] [[论文](https://arxiv.org/abs/2610.14705)]
- **闫凯境** 天士力医药集团董事长。发布数智本草语言大模型和数智中药路线。 [天士力] [[新闻](http://www.news.cn/20240509/a76f15aae0544defad943093214cd38b/c.html)]
- **周水平** 天士力研究院执行院长。用数智本草生成创新方，并做天然产物筛选。 [天士力] [[新闻](https://www.yicai.com/news/102185086.html)]
- **苏晶** 天津天士力数智中医药科技有限公司总经理。以数智本草为起点建设中医智能体和临床决策支持。 [天士力] [[新闻](http://tjtfea.com/News/202603/2026030514254819.htm)]
- **熊皓舒** 天士力先进制造技术经理。做中药过程检测、质量数字化和智能制造产线。 [天士力] [[新闻](http://www.banyuetan.org/ppgs/detail/20190508/1000200033137571557301637982839273_1.html)]
- **章顺楠** 天士力医药集团股份有限公司副总经理。负责天士力数智中药和智能制造技术体系。 [天士力] [[新闻](https://www.vbdata.cn/1518965213)]

</details>

<details>
<summary>天津大学（3）</summary>

- **王鑫** 天津大学人工智能学院教授、博士生导师。做知识图谱与大模型，与天津中医药大学合作发布中医大模型岐伯。 [天津大学智能与计算学部] [[主页](https://cic.tju.edu.cn/info/1114/2744.htm)] [[团队](http://www.tjudb.cn/dbgroup/Xin_Wang_zh)] [[论文](https://doi.org/10.1016/j.eswa.2025.127672)]
- **王煜** 天津大学人工智能学院教授、博士生导师。参与中医主动问诊系统 DoPI。 [天津大学人工智能学院] [[主页](https://faculty.tju.edu.cn/wangyu_ai/zh_CN/index.htm)]
- **王学民** 天津大学精仪学院副教授、中医工程实验室主任。做脉象采集和望闻问切四诊合参系统。 [天津大学精密仪器与光电子工程学院] [[新闻](https://news.tju.edu.cn/info/1012/345719.htm)]

</details>

<details>
<summary>国家超级计算天津中心（2）</summary>

- **孟祥飞** 国家超级计算天津中心首席科学家。推动天河中医药大模型和医院智慧医疗合作。 [国家超级计算天津中心] [[新闻](https://www.nscc-tj.cn/xwxq.php?id=626)]
- **傅浩** 国家超级计算天津中心数据智能部部长。介绍天河·灵枢 2.0 的中医全科推理。 [国家超级计算天津中心] [[新闻](https://epaper.tianjinwe.com/tjrb/h5/html5/2025-08/28/content_143090_2563267.htm)]

</details>

<details>
<summary>天大智图（2）</summary>

- **贾勇哲** 天大智图创始人、总经理。负责海河·岐伯中医药大模型的产业落地。 [天大智图] [[新闻](https://epaper.tianjinwe.com/tjrb/h5/html5/2024-05/27/content_143078_848091.htm)]
- **徐大为** 天大智图技术总监。参与研发海河·岐伯和方剂知识增强。 [天大智图] [[新闻](https://www.tjnk.gov.cn/NKQZF/XXDT856/nkyw/202401/t20240107_6501701.html)]

</details>

<details>
<summary>依脉人工智能医疗科技（天津）（1）</summary>

- **周鹏** 依脉人工智能医疗科技（天津）董事长。做舌诊仪、脉诊仪等望闻问切装备。 [依脉人工智能医疗科技（天津）] [[主页](https://www.tianzhongyimai.com/NewsStd_739.html)]

</details>

<details>
<summary>南开大学（1）</summary>

- **白钢** 南开大学药学院教授、博士生导师。用系统生物学和网络调控解析中药复方。 [南开大学药学院] [[主页](https://pharmacy.nankai.edu.cn/info/1011/1293.htm)]

</details>


</details>

<details>
<summary>河北（5）</summary>

<details>
<summary>河北中医药大学（2）</summary>

- **王少贤** 石家庄。河北中医药大学教授、博士生导师。招生方向为中医病证基础与数智中医诊法。 [河北中医药大学] [[主页](http://static.hhkaobo.com/upload/editor/ba712818-4047-4a3c-a62d-eb12188f7339.pdf)]
- **方朝义** 石家庄。河北中医药大学教授、博士生导师。团队研制中医四诊仪，并训练人工智能诊法模型。 [河北中医药大学] [[主页](http://static.hhkaobo.com/upload/editor/ba712818-4047-4a3c-a62d-eb12188f7339.pdf)]

</details>

<details>
<summary>河北北方学院（1）</summary>

- **通旭明** 河北北方学院信息科学与工程学院。悬壶和青囊两篇中医大模型论文的第一作者。 [河北北方学院] [[论文](https://link.springer.com/article/10.1186/s13020-025-01200-3)]

</details>

<details>
<summary>河北大学（1）</summary>

- **赵汉青** 保定。河北大学中医药信息学实验室主任、硕士生导师。做舌诊、脉诊客观化和中医大模型、知识图谱。 [河北大学] [[主页](https://zyxy.hbu.edu.cn/info/1037/2368.htm)]

</details>

<details>
<summary>河北省中医院（1）</summary>

- **杜艳茹** 河北省中医院副院长、博士生导师。做李佃贵经验的辨证开方大模型和脾胃病模型东垣。 [河北省中医院] [[主页](https://www.hbszyy.cn/html/product/2013-5-28/273.html)]

</details>


</details>

<details>
<summary>山西（4）</summary>

<details>
<summary>山西中医药大学（3）</summary>

- **杨继红** 太原。山西中医药大学教授、博士生导师。做中医药古籍数字化和机器学习智能辨证。 [山西中医药大学] [[主页](https://yjsb.sxtcm.edu.cn/info/1708/4743.htm)]
- **杜晨晖** 太原。山西中医药大学教授、博士生导师。用代谢组学和网络药理学研究晋药药效物质。 [山西中医药大学] [[主页](https://yjsb.sxtcm.edu.cn/info/1708/4736.htm)]
- **秦雪梅** 太原。山西中医药大学教授、博士生导师。用代谢组学、化学计量和网络药理学做中药质量评价。 [山西中医药大学] [[主页](https://yjsb.sxtcm.edu.cn/info/1708/4741.htm)]

</details>

<details>
<summary>中北大学（1）</summary>

- **张志东** 太原。中北大学教授、博士生导师，山西中医药大学硕士生导师。做中医数字化传感和智能四诊仪、智能艾灸机器人。 [中北大学] [[主页](https://6y.nuc.edu.cn/info/1025/28296.htm)]

</details>


</details>

<details>
<summary>内蒙古（8）</summary>

<details>
<summary>内蒙古大学（3）</summary>

- **飞龙** 内蒙古大学教授、博士生导师。牵头蒙医药知识库、临床辅助和蒙医药大模型。 [内蒙古大学] [[主页](https://ccs.imu.edu.cn/info/1034/2019.htm)]
- **高光来** 呼和浩特。内蒙古大学计算机学院博士生导师。做人工智能和蒙古文信息处理，并参与结合知识图谱的蒙医药大语言模型。 [内蒙古大学计算机学院] [[主页](https://ccs.imu.edu.cn/info/1034/2028.htm)]
- **张晖** 呼和浩特。内蒙古大学计算机学院硕士生导师。做蒙古语语音和文字识别，并参与蒙医药大语言模型。 [内蒙古大学计算机学院] [[主页](https://ccs.imu.edu.cn/info/1021/1888.htm)]

</details>

<details>
<summary>内蒙古民族大学（2）</summary>

- **张春生** 通辽。内蒙古民族大学硕士生导师。主持蒙医方剂数据挖掘，并用关联规则、决策树和聚类分析蒙药。 [内蒙古民族大学] [[主页](http://school.freekaoyan.com/neimenggu/imun/daoshi/2021/06-24/16245408291512706.shtml)]
- **张苏雅拉吐** 通辽。内蒙古民族大学硕士生导师。用激光诱导击穿光谱结合机器学习和深度学习区分蒙药材。 [内蒙古民族大学] [[主页](http://school.freekaoyan.com/neimenggu/imun/daoshi/2021/06-24/16245398151512483.shtml)]

</details>

<details>
<summary>内蒙古医科大学（1）</summary>

- **包哈申** 呼和浩特。内蒙古医科大学蒙医药研究院博士生导师、硕士生导师。建成蒙医药古文献数据库、方剂库和医案知识库。 [内蒙古医科大学蒙医药研究院] [[主页](https://www.ais.cn/mentor/mentorDetail/3f3173ff-5e3c-11ec-b045-a85e45a23623)]

</details>

<details>
<summary>内蒙古自治区中医药研究所（1）</summary>

- **李旻辉** 呼和浩特。内蒙古自治区中医药研究所博士生导师、硕士生导师。用遥感做蒙中药材种植规划，并有软件著作权。 [内蒙古自治区中医药研究所] [[主页](https://www.kczg.org.cn/xuezhe/details?id=214141)]

</details>

<details>
<summary>包头医学院（1）</summary>

- **阿古拉** 包头。包头医学院博士生导师。作人工智能在中医药和蒙医药中的应用报告。 [包头医学院] [[主页](https://www.btmc.edu.cn/info/1003/10449.htm)]

</details>


</details>

<details>
<summary>辽宁（8）</summary>

<details>
<summary>辽宁中医药大学（3）</summary>

- **冷锦红** 辽宁中医药大学第一临床学院博士生导师。2026 年招收中医人工智能科学与技术方向。 [辽宁中医药大学第一临床学院] [[招生](https://gjhzjlc.lnutcm.edu.cn/liaoningzhongyiyaodaxue2026nianshenqing-kaoheboshiyanjiushengzhaoshengzhuanyemuluzhuanyexuewei.pdf)]
- **赵相轩** 辽宁中医药大学基础医学院博士生导师。方向是中医药人工智能科学。 [辽宁中医药大学基础医学院] [[招生](https://gjhzjlc.lnutcm.edu.cn/liaoningzhongyiyaodaxue2026nianshenqing-kaohejishuobolianduboshiyanjiushengzhaoshengzhuanyemuluxueshuxuewei.pdf)]
- **乔铁** 辽宁中医药大学副教授、硕士生导师，中医人工智能学科负责人。做舌诊标准化采集与算法评估。 [辽宁中医药大学] [[主页](https://www.lnutcm.edu.cn/info/2231/55271.htm)]

</details>

<details>
<summary>东北大学（1）</summary>

- **覃文军** 东北大学计算机科学与工程学院教授、博士生导师。针灸机器人国家重点研发课题负责人，主持施针手法数据库和人体穴位知识图谱。 [东北大学计算机科学与工程学院] [[主页](https://faculty.neu.edu.cn/tanwenjun/zh_CN/index.htm)]

</details>

<details>
<summary>中国科学院大连化学物理研究所（1）</summary>

- **梁鑫淼** 中国科学院大连化学物理研究所研究员、博士生导师。提出本草物质组，并建中药标准组分库。 [中国科学院大连化学物理研究所] [[主页](https://mccm.dicp.ac.cn/info/1106/1204.htm)]

</details>

<details>
<summary>沈阳药科大学（1）</summary>

- **郭永学** 沈阳药科大学制药工程学院教授、副院长、硕士生导师。做过程分析技术，以及中药制药新技术和质量控制。 [沈阳药科大学制药工程学院] [[主页](https://grs.syphu.edu.cn/info/1103/7177.htm)]

</details>

<details>
<summary>辽宁中医药大学附属医院（1）</summary>

- **张哲** 辽宁中医药大学附属医院中医药创新工程技术中心副主任。对接中医舌诊辅助诊断应用，推动舌诊产品升级。 [辽宁中医药大学附属医院] [[主页](https://www.lnutcm.edu.cn/info/1031/44221.htm)]

</details>

<details>
<summary>辽宁中医药大学附属第二医院（1）</summary>

- **李国信** 沈阳。辽宁中医药大学附属第二医院博士生导师。招生方向含中西医结合临床和人工智能。 [辽宁中医药大学附属第二医院] [[主页](https://www.lnpatcm.com/product/170.html)]

</details>


</details>

<details>
<summary>吉林（4）</summary>

<details>
<summary>长春中医药大学（3）</summary>

- **冷向阳** 长春中医药大学校长、教授。牵头 AI+中医行动，联合发布众星·长白岐黄。 [长春中医药大学] [[新闻](https://www.chinanews.com.cn/cj/2025/12-20/10537422.shtml)]
- **陈锐** 长春。长春中医药大学基础医学院教授、博士生导师、硕士生导师。做中医诊断学和脉学。 [长春中医药大学基础医学院] [[主页](https://ccucm.teacher.360eol.com/teacherBasic/preview?teacherId=28019)]
- **皮子凤** 长春。长春中医药大学药学院教授、博士生导师、硕士生导师。用网络药理学做中药分析。 [长春中医药大学药学院] [[主页](https://ccucm.teacher.360eol.com/teacherBasic/preview?teacherId=28131)]

</details>

<details>
<summary>吉林工商学院（1）</summary>

- **赵佳** 吉林工商学院副校长、教授。领衔研发众星·长白岐黄多模态中医药推理大模型。 [吉林工商学院] [[新闻](https://jl.chinadaily.com.cn/a/202512/21/WS6947b1c2a310942cc4997b6e.html)]

</details>


</details>

<details>
<summary>黑龙江（4）</summary>

<details>
<summary>黑龙江中医药大学（4）</summary>

- **闫朝升** 黑龙江中医药大学教授、研究生导师，医学信息工程学院院长。做医学人工智能和中医经典知识图谱。 [黑龙江中医药大学医学信息工程学院] [[主页](https://rwyglxy.hljucm.net/info/1276/3122.htm)]
- **王喜军** 黑龙江中医药大学教授、博士生导师。做中药血清药物化学和中医方证代谢组学。 [黑龙江中医药大学] [[主页](https://kjc.hljucm.net/info/1097/1129.htm)]
- **孙晖** 黑龙江中医药大学博士生导师。做中药体内成分分析和质量标准。 [黑龙江中医药大学] [[主页](https://yjsy.hljucm.net/info/1292/6818.htm)]
- **吴修红** 黑龙江中医药大学二级教授、博士生导师。基于中医方证代谢组研究中药质量标志物和鉴定。 [黑龙江中医药大学] [[主页](https://yjsy.hljucm.net/info/1292/6818.htm)]

</details>


</details>

<details>
<summary>上海（45）</summary>

<details>
<summary>上海中医药大学（21）</summary>

- **李颉** 上海中医药大学中医药人工智能学院教授。带队做中医药大模型、多模态智能体和中药研发数字化。 [上海中医药大学中医药人工智能学院] [[主页](https://aishutcm.shutcm.edu.cn/2026/0327/c7887a172347/page.htm)] [[招生](https://yjsy.shutcm.edu.cn/_upload/article/files/f9/d9/0c9d59b941d3b1bb03c93fc8aa1c/a33367af-8441-476a-9ca6-74e1abc59992.pdf)]
- **胡晓娟** 上海中医药大学中医药人工智能学院硕士生导师。方向是中医智能诊疗技术。 [上海中医药大学中医药人工智能学院] [[招生](https://yjsy.shutcm.edu.cn/_upload/article/files/ac/da/f6a12cc64203bf845f45303b5326/4198283c-0059-4715-8008-103bbf3ef6fa.pdf)]
- **屠立平** 上海中医药大学中医药人工智能学院硕士生导师。方向是中医诊断信息化与智能化。 [上海中医药大学中医药人工智能学院] [[招生](https://yjsy.shutcm.edu.cn/_upload/article/files/ac/da/f6a12cc64203bf845f45303b5326/4198283c-0059-4715-8008-103bbf3ef6fa.pdf)]
- **孙继佳** 上海中医药大学中医药人工智能学院硕士生导师。方向是基于人工智能的计算药物发现。 [上海中医药大学中医药人工智能学院] [[招生](https://yjsy.shutcm.edu.cn/_upload/article/files/ac/da/f6a12cc64203bf845f45303b5326/4198283c-0059-4715-8008-103bbf3ef6fa.pdf)]
- **李少雄** 上海中医药大学中医药人工智能学院硕士生导师。方向是医学智能算法与智能硬件。 [上海中医药大学中医药人工智能学院] [[招生](https://yjsy.shutcm.edu.cn/_upload/article/files/ac/da/f6a12cc64203bf845f45303b5326/4198283c-0059-4715-8008-103bbf3ef6fa.pdf)]
- **郑广勇** 上海中医药大学交叉科学研究院硕士生导师。方向是基于人工智能的中药药理。 [上海中医药大学交叉科学研究院] [[招生](https://yjsy.shutcm.edu.cn/_upload/article/files/ac/da/f6a12cc64203bf845f45303b5326/4198283c-0059-4715-8008-103bbf3ef6fa.pdf)]
- **陆冬** 上海中医药大学交叉科学研究院硕士生导师。方向是人工智能与药物设计，用于中药研究。 [上海中医药大学交叉科学研究院] [[招生](https://yjsy.shutcm.edu.cn/_upload/article/files/ac/da/f6a12cc64203bf845f45303b5326/4198283c-0059-4715-8008-103bbf3ef6fa.pdf)]
- **关晓青** 上海中医药大学交叉科学研究院硕士生导师。方向是大数据与人工智能药物研发。 [上海中医药大学交叉科学研究院] [[招生](https://yjsy.shutcm.edu.cn/_upload/article/files/ac/da/f6a12cc64203bf845f45303b5326/4198283c-0059-4715-8008-103bbf3ef6fa.pdf)]
- **许家佗** 上海中医药大学二级教授、博士生导师，中医信息科学与技术研究中心主任。主持中医智能舌诊系统研发。 [上海中医药大学] [[主页](https://zhongyi.shutcm.edu.cn/2023/1213/c7141a157325/page.htm)]
- **王忆勤** 上海中医药大学教授、博士生导师。做舌、脉、面、问四诊客观化。 [上海中医药大学] [[主页](https://zhongyi.shutcm.edu.cn/2023/1213/c7141a157327/page.htm)]
- **李福凤** 上海中医药大学教授、博士生导师。做面诊图像标准化、特征识别和智能镜。 [上海中医药大学] [[主页](https://zhongyi.shutcm.edu.cn/2023/1213/c7141a157323/page.htm)]
- **燕海霞** 上海中医药大学教授、硕士生导师。做脉诊客观化和脉图风险模型。 [上海中医药大学] [[主页](https://zhongyi.shutcm.edu.cn/2023/1213/c7141a157316/page.htm)]
- **郝一鸣** 上海中医药大学中医学院研究员、硕士生导师。做慢性病四诊客观化和舌苔代谢组。 [上海中医药大学中医学院] [[主页](https://zhongyi.shutcm.edu.cn/2023/1213/c7141a157321/page.htm)]
- **许朝霞** 上海中医药大学研究员、博士生导师。做舌象参数分析，主编《中医舌诊研究与临床应用》。 [上海中医药大学中医学院] [[主页](https://zhongyi.shutcm.edu.cn/2023/1213/c7141a157324/page.htm)]
- **郭睿** 上海中医药大学研究员、硕士生导师。做脉诊客观化，并参与智能舌诊仪。 [上海中医药大学中医学院] [[主页](https://zhongyi.shutcm.edu.cn/2023/1213/c7141a157318/page.htm)]
- **崔骥** 上海中医药大学基础医学院副教授、硕士生导师。做阵列式三维脉图和中医四诊信息化。 [上海中医药大学基础医学院] [[主页](https://zhongyi.shutcm.edu.cn/2023/1213/c7141a157317/page.htm)]
- **钱鹏** 上海中医药大学高级实验师、硕士生导师。做可自动调压的脉象采集装置和四诊客观化。 [上海中医药大学] [[主页](https://zhongyi.shutcm.edu.cn/2023/1213/c7141a157320/page.htm)]
- **唐文超** 上海中医药大学中医药人工智能学院教授。做手针刺激量光力传感和镇痛量效建模，并带队做中医药大模型评测。 [上海中医药大学中医药人工智能学院] [[主页](https://zt.shutcm.edu.cn/2021/1019/c3352a137223/page.htm)]
- **刘堂义** 上海中医药大学针灸推拿学院副教授、硕士生导师。研发针刺手法电针仪、单穴位电阻检测和手法仿真采集。 [上海中医药大学针灸推拿学院] [[主页](http://school.freekaoyan.com/sh/shutcm/daoshi/2021/01-23/16113955791334845.shtml)]
- **张卫东** 上海中医药大学交叉科学研究院教授、博士生导师。做中药复方药效物质，并推动人工智能解析组方机制。 [上海中医药大学交叉科学研究院] [[主页](https://iiimr.shutcm.edu.cn/2019/0426/c4069a174532/page.htm)]
- **杨华元** 上海。上海中医药大学教授。用人工智能做推拿机器人，可模仿一指禅并按病灶定位。 [上海中医药大学] [[主页](https://www.shutcm.edu.cn/2023/0921/c751a155057/page.htm)]

</details>

<details>
<summary>上海中医药大学附属龙华医院（5）</summary>

- **陈昕琳** 上海中医药大学附属龙华医院院长。负责中医多模态辅助诊断智能体和数智龙承。 [上海中医药大学附属龙华医院] [[新闻](https://www.shanghai.gov.cn/gwk/search/content/441f95ac30e7432fa24730c79128df5c)]
- **刘萍** 上海中医药大学附属龙华医院副院长、主任医师、博士生导师。担任名中医辨证论治思维模型课题负责人。 [上海中医药大学附属龙华医院] [[主页](https://www.longhua.net/info/2921/64701.htm)]
- **董亮** 上海中医药大学附属龙华医院信息中心主任。负责名中医思维模型的信息化和思维链标注平台对接。 [上海中医药大学附属龙华医院] [[主页](https://www.longhua.net/info/1021/87312.htm)]
- **陈跃来** 上海中医药大学附属龙华医院时任院长。推动舌象、面象、脉象人工智能预问诊和中医临床辅助决策平台。 [上海中医药大学附属龙华医院] [[主页](https://www.longhua.net/info/1028/2519.htm)]
- **朱亮** 上海中医药大学附属龙华医院副院长。代表医院参加医疗大模型应用验证，医院同期建设方证大模型和中医四诊模式识别。 [上海中医药大学附属龙华医院] [[主页](https://www.longhua.net/info/1021/76211.htm)]

</details>

<details>
<summary>华东理工大学（5）</summary>

- **阮彤** 华东理工大学信息科学与工程学院教授、博士生导师。做医疗大模型与知识图谱，建过中医药知识图谱并用于辅助开方。 [华东理工大学信息科学与工程学院] [[主页](https://faculty.ecust.edu.cn/cise/rt/main.htm)]
- **唐赟** 华东理工大学药学院教授、博士生导师。做人工智能药物设计与网络药理学，并参与中医问诊模型 MedChatZH。 [华东理工大学药学院] [[主页](https://pharmacy.ecust.edu.cn/2008/1203/c2795a29378/page.htm)] [[论文](https://pubmed.ncbi.nlm.nih.gov/38503097/)]
- **颜建军** 华东理工大学副教授、硕士生导师。做脉诊仪、舌图像分割和中医信号分析。 [华东理工大学] [[主页](https://mech.ecust.edu.cn/2019/0516/c11271a90164/page.htm)]
- **虞慧群** 华东理工大学计算机学院教授、博士生导师。参与中医问诊模型 MedChatZH。 [华东理工大学计算机学院] [[主页](https://cise.ecust.edu.cn/2026/0615/c16487a191279/page.htm)]
- **范贵生** 华东理工大学计算机学院副研究员、博士生导师。参与中医问诊模型 MedChatZH。 [华东理工大学计算机学院] [[主页](https://cise.ecust.edu.cn/_t250/2011/0615/c7766a55144/page.htm)]

</details>

<details>
<summary>上海中医药大学附属曙光医院（2）</summary>

- **元唯安** 上海中医药大学附属曙光医院副院长、博士生导师。负责临床试验全生命周期平台和虚拟临床试验。 [上海中医药大学附属曙光医院] [[主页](https://zyyyjy.gdpu.edu.cn/info/1082/1370.htm)]
- **房敏** 上海中医药大学教授，曙光医院推拿研究所所长。领衔推拿仿生手机器人、脊柱筋骨评估和经穴刺激外骨骼，并做抑郁症智能诊断。 [上海中医药大学附属曙光医院] [[新闻](http://www.thepaper.cn/newsDetail_forward_31847870)]

</details>

<details>
<summary>上海中医药大学附属第七人民医院（2）</summary>

- **胡聃** 上海市第七人民医院院长。医院发布岐元中医大模型，与上海中医药大学、上海人工智能实验室合作。 [上海中医药大学附属第七人民医院] [[新闻](http://sh.news.cn/20260719/ef7034ccc6394653825f97a21452738e/c.html)]
- **曾艺鹏** 上海中医药大学附属第七人民医院硕士生导师。招生方向含中医脉诊和内分泌代谢病诊疗。 [上海中医药大学附属第七人民医院] [[招生](https://yjsy.shutcm.edu.cn/_upload/article/files/ac/da/f6a12cc64203bf845f45303b5326/4198283c-0059-4715-8008-103bbf3ef6fa.pdf)]

</details>

<details>
<summary>中国科学院上海药物研究所（2）</summary>

- **果德安** 中国科学院上海药物研究所研究员，中药标准化技术国家工程研究中心主任。做中药分析、质量标准和中药质量检测数据库。 [中国科学院上海药物研究所] [[主页](http://www.caim.org.cn/info_content_ds.jsp?id=10009)]
- **陈凯先** 中国科学院上海药物研究所研究员、博士生导师。做计算机辅助药物设计，招生方向含中药学。 [中国科学院上海药物研究所] [[主页](https://people.ucas.ac.cn/~0009438)]

</details>

<details>
<summary>华东师范大学（2）</summary>

- **李洪林** 华东师范大学药学院院长、博士生导师。做人工智能药物设计。学校联合上海中医药大学等发布数智岐黄中医药大模型。 [华东师范大学药学院，临港实验室] [[主页](https://pharm.ecnu.edu.cn/46547/list.htm)] [[新闻](https://www.ecnu.edu.cn/info/1426/65503.htm)]
- **王晓玲** 华东师范大学计算机学院教授。主持中医教育大模型关键技术，并参与神农中医药大模型。 [华东师范大学计算机学院] [[主页](https://faculty.ecnu.edu.cn/_s16/wxl2/main.psp)] [[代码](https://github.com/michael-wzhu/ShenNong-TCM-LLM)]

</details>

<details>
<summary>上海中医药大学附属岳阳中西医结合医院（1）</summary>

- **冯圣一** 上海中医药大学附属岳阳中西医结合医院硕士生导师。方向是人工智能赋能中医骨伤康复。 [上海中医药大学附属岳阳中西医结合医院] [[招生](https://yjsy.shutcm.edu.cn/_upload/article/files/ac/da/f6a12cc64203bf845f45303b5326/4198283c-0059-4715-8008-103bbf3ef6fa.pdf)]

</details>

<details>
<summary>上海交通大学（1）</summary>

- **马利庄** 上海交通大学计算机学院特聘教授、博士生导师。做中西医信息融合智能诊断，以及中医证候与面色的计算机诊断。 [上海交通大学计算机学院] [[主页](https://cs.sjtu.edu.cn/jiaoshiml/malizhuang.html)]

</details>

<details>
<summary>上海工程技术大学（1）</summary>

- **夏春明** 上海工程技术大学教授、博士生导师。做脉诊信息采集和四诊客观化。 [上海工程技术大学] [[主页](https://seee.sues.edu.cn/56/93/c23926a218771/page.htm)]

</details>

<details>
<summary>上海道生医疗科技有限公司（1）</summary>

- **李春清** 上海道生医疗科技有限公司董事长。做道生四诊仪、脉象仪和中医诊断设备标准。 [上海道生医疗科技有限公司] [[主页](https://www.acfic.org.cn/ztzlhz/2022bzcxdh/2022bzcxdh_4/202209/t20220913_313004.html)]

</details>

<details>
<summary>同济大学（1）</summary>

- **王昊奋** 同济大学特聘研究员、博士生导师。做知识图谱与对话系统，并指导中医大模型仲景。 [同济大学] [[主页](https://faculty.tongji.edu.cn/wanghaofen/zh_CN/index.htm)] [[代码](https://github.com/pariskang/CMLM-ZhongJing)]

</details>

<details>
<summary>复旦大学（1）</summary>

- **张文强** 复旦大学计算机学院研究员、博士生导师。指导中医大模型仲景 GPT，并做中医诊疗机器人。 [复旦大学计算机学院] [[主页](https://iipl.fudan.edu.cn/70/e4/c45863a684260/page.htm)]

</details>


</details>

<details>
<summary>江苏（21）</summary>

<details>
<summary>南京中医药大学（11）</summary>

- **胡孔法** 南京中医药大学副校长、博士生导师，省级人工智能学院院长。做中医药人工智能、知识图谱与大模型，主持舌诊、辨证大模型和江苏省中医垂直领域大模型。 [南京中医药大学人工智能与信息技术学院] [[主页](https://xxjs.njucm.edu.cn/2026/0424/c465a167934/pagem.htm)] [[新闻](http://xxjs.njucm.edu.cn/2025/0908/c467a160307/page.htm)]
- **周作建** 南京中医药大学人工智能与信息技术学院教授、博士生导师，中医药人工智能交叉学科带头人。做中医药人工智能、健康物联网和智能装备。 [南京中医药大学人工智能与信息技术学院] [[主页](https://xxjs.njucm.edu.cn/2018/0928/c465a43551/pagem.htm)]
- **曹鹏** 南京中医药大学研究员。团队与北京中医药大学谷晓红等合作发表中医大模型天医。 [南京中医药大学] [[新闻](https://www.njucm.edu.cn/2025/0910/c6754a160459/page.htm)] [[论文](https://doi.org/10.1016/j.inffus.2025.103663)]
- **高峰** 南京中医药大学人工智能与信息技术学院博士生导师。方向是机器学习与中医药人工智能。 [南京中医药大学人工智能与信息技术学院] [[招生](https://gra.njucm.edu.cn/_upload/article/files/8f/0a/bd6170cd44ad94f0d3108af24abe/aff48fcb-3589-4b90-a66d-c93ec91ba0d1.pdf)]
- **李海燕** 南京中医药大学人工智能与信息技术学院博士生导师。方向是机器学习与中医药人工智能。 [南京中医药大学人工智能与信息技术学院] [[招生](https://gra.njucm.edu.cn/_upload/article/files/8f/0a/bd6170cd44ad94f0d3108af24abe/aff48fcb-3589-4b90-a66d-c93ec91ba0d1.pdf)]
- **顾万君** 南京中医药大学人工智能与信息技术学院博士生导师。方向是生物信息与中医药大数据。 [南京中医药大学人工智能与信息技术学院] [[招生](https://gra.njucm.edu.cn/_upload/article/files/8f/0a/bd6170cd44ad94f0d3108af24abe/aff48fcb-3589-4b90-a66d-c93ec91ba0d1.pdf)]
- **杨涛** 南京中医药大学人工智能与信息技术学院教授、硕士生导师。做中医药人工智能、舌诊多模态体质辨识和医案知识图谱。 [南京中医药大学人工智能与信息技术学院] [[主页](https://xxjs.njucm.edu.cn/2021/0305/c449a71318/pagem.htm)]
- **王天舒** 南京中医药大学人工智能与信息技术学院副教授、硕士生导师。做中医药人工智能、视觉识别和全身望诊。 [南京中医药大学人工智能与信息技术学院] [[主页](http://xxjs.njucm.edu.cn/2024/0409/c465a125588/page.htm)]
- **戴彩艳** 南京中医药大学人工智能与信息技术学院副教授、硕士生导师。做智能图像处理、中医药网络模型和望诊信息采集。 [南京中医药大学人工智能与信息技术学院] [[主页](http://xxjs.njucm.edu.cn/2024/0409/c465a125589/page.htm)]
- **夏有兵** 南京中医药大学博士生导师，中国针灸学会数智针灸专业委员会主任委员。构建针灸学派与不孕症知识图谱，开发智能针灸辅助系统和针灸大模型。 [南京中医药大学，南京医科大学] [[主页](https://bmei.njmu.edu.cn/2025/1107/c11345a293500/page.htm)]
- **徐天成** 南京中医药大学特聘教授。提出数字经络并做智能针灸机器人，参与穴位定位、手法复现和得气力反馈。 [南京中医药大学] [[主页](https://zgze.cbpt.cnki.net/portal/journal/portal/client/news/zgze_b164694d-d190-4244-838a-908efa219f6e)]

</details>

<details>
<summary>大经中医（3）</summary>

- **李文友** 大经中医创始人、董事长。公司发布岐黄问道中医大模型，用知识图谱和临床数据做辅助诊疗。 [大经中医] [[新闻](https://www.vbdata.cn/1518996221)]
- **赵静** 大经中医联合创始人、副总经理，南京中医药大学产业教授、研究生导师。负责岐黄问道的研究，并与高校、医院合作。 [大经中医，南京中医药大学] [[新闻](https://www.vbdata.cn/1518996221)]
- **王祺** 大经中医技术总监。负责岐黄问道从预训练到强化学习的技术路径，并做脉诊仪和舌面诊仪。 [大经中医] [[新闻](http://js.news.cn/20230729/fa034db71a00487b819a4ad95b44673e/c.html)]

</details>

<details>
<summary>中国药科大学（2）</summary>

- **王引引** 中国药科大学中药学院副研究员、硕士生导师。用人工智能和多组学解析中药复方机制、配伍与归经。 [中国药科大学中药学院] [[主页](http://zyxy.cpu.edu.cn/ab/53/c19966a240467/page.htm)]
- **贾晓斌** 中国药科大学中药学院教授、博士生导师。做智能中药学，用人工智能和图神经网络研究中药物质基础与配伍。 [中国药科大学中药学院] [[主页](https://zyxy.cpu.edu.cn/ab/47/c19965a240455/page.htm)]

</details>

<details>
<summary>南京大学（1）</summary>

- **黄奇** 南京大学信息管理学院教授、博士生导师。参与中医古籍大模型黄帝。 [南京大学信息管理学院] [[主页](https://im.nju.edu.cn/info/1099/33751.htm)]

</details>

<details>
<summary>康缘药业（1）</summary>

- **肖伟** 康缘药业董事长，中药制药过程控制与智能制造技术全国重点实验室主任。推动制药工业智能化大模型和道地药材鉴定溯源。 [康缘药业] [[主页](https://www.kanion.com/about/about_us.htm)]

</details>

<details>
<summary>江苏省中医药研究院（1）</summary>

- **瞿鼎** 江苏省中医药研究院博士生导师。方向是人工智能赋能创新中药制剂。 [江苏省中医药研究院] [[招生](https://gra.njucm.edu.cn/_upload/article/files/69/4f/90badc1f4e238ef01e08cf30e770/caac9243-df3c-4435-8167-f3f4d2f44416.pdf)]

</details>

<details>
<summary>江苏省中医院（1）</summary>

- **吴婷** 江苏省中医院博士生导师。方向是疼痛功能影像的人工智能分类和纳米诊疗。 [江苏省中医院] [[招生](https://gra.njucm.edu.cn/_upload/article/files/69/4f/90badc1f4e238ef01e08cf30e770/caac9243-df3c-4435-8167-f3f4d2f44416.pdf)]

</details>

<details>
<summary>西苑医院苏州医院（1）</summary>

- **吴冰** 西苑医院苏州医院血液科主任。负责叶天士血证辅助诊疗大模型。 [西苑医院苏州医院] [[新闻](https://www.xyhospital.com/Html/News/Articles/22524.html)]

</details>


</details>

<details>
<summary>浙江（16）</summary>

<details>
<summary>浙江大学（7）</summary>

- **程翼宇** 浙江大学药学院教授、博士生导师。做医药工业人工智能、药品智能制造和质量分析。 [浙江大学药学院] [[主页](https://person.zju.edu.cn/chengyy)]
- **瞿海斌** 浙江大学药学院教授、博士生导师，药物信息学研究所所长。做中药创制、制药过程分析和制药工业大数据。 [浙江大学药学院] [[主页](http://www.cps.zju.edu.cn/59113/list.htm)]
- **廖杰** 浙江大学百人计划研究员、博士生导师，未来健康实验室中医药方向带头人。做中药系统生物学和中医药人工智能。 [浙江大学] [[主页](https://yrd.zju.edu.cn/2026/0326/c90460a3144544/page.htm)]
- **王毅** 浙江大学药学院教授、博士生导师。做中药药效物质、高内涵筛选和系统药理学。 [浙江大学药学院] [[主页](https://person.zju.edu.cn/yiwang)]
- **刘雪松** 浙江大学药学院研究员、博士生导师。做医药智能制造、近红外在线检测和生产全程质量控制。 [浙江大学药学院] [[主页](http://www.cps.zju.edu.cn/59114/list.htm)]
- **陈勇** 浙江大学药学院研究员、博士生导师。做中药先进制造技术。 [浙江大学药学院] [[主页](http://www.cps.zju.edu.cn/59114/list.htm)]
- **龚行楚** 浙江大学药学院副教授、博士生导师。做中药质量控制、制药工艺和装备。 [浙江大学药学院] [[主页](https://person.zju.edu.cn/gongxc)]

</details>

<details>
<summary>浙江中医药大学（4）</summary>

- **范骁辉** 浙江大学求是特聘教授、博士生导师，浙江中医药大学副校长。方向是中医药人工智能，课题组 TCM+X 发布 TCMChat。 [浙江大学药学院，浙江中医药大学] [[主页](https://person.zju.edu.cn/fanxh)] [[论文](https://doi.org/10.1016/j.phrs.2024.107530)] [[代码](https://github.com/ZJUFanLab/TCMChat)]
- **赖小波** 浙江中医药大学教授、博士生导师，医学技术与信息工程学院副院长。做智慧中医药和医学影像人工智能。 [浙江中医药大学] [[主页](https://yjxx.zcmu.edu.cn/info/1071/9229.htm)]
- **林树元** 浙江中医药大学副教授，中医药人工智能联合工程中心主任。用大模型和知识图谱做经方问诊系统轩岐问对。 [浙江中医药大学] [[主页](https://xhhos.com/department/doctor/5/30/233)]
- **周岳君** 浙江中医药大学教授、主任中医师、硕士生导师，中医诊断学教研室主任。做舌象辨证和诊法研究。 [浙江中医药大学] [[主页](https://jc.zcmu.edu.cn/info/1164/3346.htm)]

</details>

<details>
<summary>微医（1）</summary>

- **廖杰远** 微医创始人、董事长。做人工智能中药平台，把老中医经验转成可调配颗粒。 [微医] [[新闻](https://www.cls.cn/detail/1661807)]

</details>

<details>
<summary>杭州市中医院（1）</summary>

- **张永华** 杭州市中医院主任医师、博士生导师。团队打造张永华睡眠智能体。 [杭州市中医院] [[主页](https://zyy.lanews.com.cn/content/2022-02/17/content_9341799.htm)]

</details>

<details>
<summary>浙江工商大学（1）</summary>

- **庄毅** 浙江工商大学计算机学院教授。中医方剂模型 TCM-KLLaMA 第一作者。 [浙江工商大学计算机学院] [[主页](https://scie.zjgsu.edu.cn/zh-hans/node/400)]

</details>

<details>
<summary>浙江省中医院（1）</summary>

- **陈红波** 浙江省中医院肾病科负责人、主任医师。所在科室建有中医人工智能关键技术与装备工程研究中心，方向包括名老中医数字孪生机器人和智能中医机器人。 [浙江省中医院] [[主页](https://www.zjhtcm1931.cn/departmentInfo/54)]

</details>

<details>
<summary>脉景（1）</summary>

- **马峻昂** 脉景董事长。做中医垂直模型、辅助开方和舌面诊图像库。 [脉景] [[新闻](https://www.vbdata.cn/51488)]

</details>


</details>

<details>
<summary>安徽（12）</summary>

<details>
<summary>安徽中医药大学（6）</summary>

- **周雪梅** 安徽中医药大学教授、硕士生导师，中医基础系主任。所在诊断学团队研制人工智能舌诊实训考核平台。 [安徽中医药大学] [[主页](https://gjjk.ahtcm.edu.cn/info/1033/1970.htm)]
- **胡继礼** 合肥。安徽中医药大学医药信息工程学院副教授、硕士生导师。用大语言模型和知识图谱做中医智能诊断，并做舌象分类。 [安徽中医药大学医药信息工程学院] [[主页](https://xxgc.ahtcm.edu.cn/info/1821/53543.htm)]
- **俞磊** 合肥。安徽中医药大学教授、博士生导师。招收中医药信息学、医疗大数据与人工智能，做智能诊疗。 [安徽中医药大学] [[主页](https://xxgc.ahtcm.edu.cn/info/1821/56223.htm)]
- **阚红星** 合肥。安徽中医药大学医药信息工程学院院长、教授、博士生导师。做中医药数据挖掘和医药大数据与人工智能。 [安徽中医药大学医药信息工程学院] [[主页](https://xxgc.ahtcm.edu.cn/info/1821/53623.htm)]
- **束建华** 合肥。安徽中医药大学教授、硕士生导师。主持知识图谱和大模型驱动的新安医家智能辅助诊疗系统。 [安徽中医药大学] [[主页](https://yjsb.ahtcm.edu.cn/info/2071/41961.htm)]
- **杨银凤** 合肥。安徽中医药大学副教授、硕士生导师，人工智能专业负责人。把人工智能用于中药成分筛选和复方优化。 [安徽中医药大学] [[主页](https://yjsb.ahtcm.edu.cn/info/2521/47781.htm)]

</details>

<details>
<summary>科大讯飞（3）</summary>

- **周佳峰** 科大讯飞副总裁。与北京中医药大学合作建设薪火中国药中医药教育大模型。 [科大讯飞] [[新闻](https://zhongyao.bucm.edu.cn/yyxw/57d9fb0a8af1496b88ca404e51e4e7d1.htm)]
- **王珂** 科大讯飞副总裁。参与薪火中国药中医药教育大模型发布和后续建设。 [科大讯飞] [[新闻](https://www.bucm.edu.cn/bzyyw/1c0b0fe535764fcc886c87b560caa0ee.htm)]
- **李礼** 科大讯飞高教研究院院长。参与薪火中国药建设，做人工智能赋能中医药高校。 [科大讯飞] [[新闻](https://zhongyao.bucm.edu.cn/yyxw/1b48fd51feea43a2964b2a19f0ae4916.htm)]

</details>

<details>
<summary>合肥工业大学（1）</summary>

- **高隽** 合肥工业大学计算机与信息学院教授、博士生导师。参与中医舌诊大模型 TongueVLM。 [合肥工业大学计算机与信息学院] [[主页](https://ci.hfut.edu.cn/info/1134/13735.htm)]

</details>

<details>
<summary>安徽中医药大学第一附属医院（1）</summary>

- **忻凌** 合肥。安徽中医药大学第一附属医院高级工程师、硕士生导师，临床研究数据中心主任。做中医药信息化、医疗大数据和中医数字化传承。 [安徽中医药大学第一附属医院] [[主页](https://yjsb.ahtcm.edu.cn/info/2071/42051.htm)]

</details>

<details>
<summary>安徽中医药大学第二附属医院（1）</summary>

- **董昌武** 安徽中医药大学教授、博士生导师，第二附属医院院长。做四诊客观化和多模态舌诊。 [安徽中医药大学第二附属医院] [[主页](https://yjsb.ahtcm.edu.cn/info/1501/30891.htm)]

</details>


</details>

<details>
<summary>福建（13）</summary>

<details>
<summary>厦门大学（8）</summary>

- **罗志明** 厦门大学信息学院副教授、博士生导师。做中医病势时序图谱、文本实体识别和临床评价平台。 [厦门大学信息学院] [[主页](https://faculty.xmu.edu.cn/luozhiming/zh_CN/index.htm)]
- **王彦晖** 厦门大学医学院教授、硕士生导师。做舌象临床和舌诊辅助系统，任世界中联舌象研究专委会创会会长。 [厦门大学医学院] [[主页](https://xah.xmu.edu.cn/info/1625/2795.htm)]
- **张绍良** 厦门大学医学院助理教授。做中医诊断信息化、舌象图像分析和脉象信号。 [厦门大学医学院] [[主页](https://med.xmu.edu.cn/info/1238/4637.htm)]
- **何宽其** 厦门大学医学院副教授。做舌诊临床应用，研究证素、方药、体质与舌象。 [厦门大学医学院] [[主页](https://med.xmu.edu.cn/info/1237/4641.htm)]
- **黄晓阳** 厦门大学信息学院助理教授。做开放环境舌象检测、偏色校正和苔质分离。 [厦门大学信息学院] [[主页](https://scholar.xmu.edu.cn/Authors/Index?id=HuangXiaoYang)]
- **苏松志** 厦门大学人工智能系副教授、硕士生导师，观健在（厦门）创始人。做大语言模型、智能中医辅助诊断，以及望闻问切一体机。 [厦门大学，观健在（厦门）] [[主页](https://iai.xmu.edu.cn/team/PI/PI2024/jcll/zndmtjs.htm)] [[新闻](https://news.qq.com/rain/a/20240914A05NEU00)]
- **李绍滋** 厦门。厦门大学教授、博士生导师，同时是福建中医药大学中医诊断学博士生导师。做智能科学与智能中医信息处理。 [厦门大学] [[主页](https://imt.xmu.edu.cn/info/1003/1182.htm)]
- **刘昆宏** 厦门。厦门大学教授、博士生导师。做舌诊人工智能、数据挖掘和健康医疗大数据。 [厦门大学] [[主页](https://cdmc.xmu.edu.cn/info/1010/1055.htm)]

</details>

<details>
<summary>福建中医药大学（4）</summary>

- **丰迪生** 福建中医药大学药学院硕士生导师。方向是人工智能与代谢组学。 [福建中医药大学药学院] [[招生](https://static.kaoyan.cn/file/2025/09/22/681e4fb4056d67fff4ae7ff9501397da.pdf)]
- **刘永静** 福建中医药大学药学院硕士生导师。方向是人工智能与代谢组学。 [福建中医药大学药学院] [[招生](https://static.kaoyan.cn/file/2025/09/22/681e4fb4056d67fff4ae7ff9501397da.pdf)]
- **林雪娟** 福建中医药大学中医学院博士生导师。招生方向为四诊信息采集及标准化研究。 [福建中医药大学中医学院] [[招生](http://static.hhkaobo.com/upload/editor/f2e35d52-e85d-4e6b-a133-fa3eefd53cc9.pdf)]
- **李灿东** 福州。福建中医药大学教授、博士生导师，新黄埔中医药联合创新研究院首席科学家。做中医诊断。 [福建中医药大学] [[主页](https://www.jiicm.com/info/1078/1241.htm)]

</details>

<details>
<summary>福耀科技大学（1）</summary>

- **朱正忠** 福耀科技大学教授、博士生导师。做健康与中医大模型，仲景 GPT 共同通讯作者。 [福耀科技大学] [[主页](https://cs.fyust.edu.cn/szdw/jsdw/zzz.htm)]

</details>


</details>

<details>
<summary>江西（13）</summary>

<details>
<summary>江西中医药大学（11）</summary>

- **杜建强** 江西中医药人工智能重点研究室研究人员。知识图谱检索增强的中医问诊大模型 DualKAG-ShenNong 通讯作者。 [江西中医药大学] [[论文](http://cea.ceaj.org/CN/Y2026/V62/I9/133)]
- **章新友** 江西中医药大学智能医学与信息工程学院教授、博士生导师。做中药性效和方剂配伍数据挖掘。 [江西中医药大学智能医学与信息工程学院] [[主页](https://jsj.jxutcm.edu.cn/info/1071/1913.htm)]
- **叶青** 江西中医药大学教师。做中医知识图谱。 [江西中医药大学] [[主页](https://jsj.jxutcm.edu.cn/info/1036/1277.htm)]
- **朱彦陈** 江西中医药大学智能医学与信息工程学院教师。做中医药图像。 [江西中医药大学智能医学与信息工程学院] [[主页](https://jsj.jxutcm.edu.cn/info/1071/1917.htm)]
- **杨明** 江西中医药大学副校长、博士生导师。做中药装备数字化，集成多光谱、高光谱成像和机器视觉。 [江西中医药大学] [[主页](https://www.jiicm.com/info/1017/1179.htm)]
- **伍振峰** 现代中药制剂教育部重点实验室主任。负责中药制剂重点实验室，并参与中药智能制造协作。 [江西中医药大学] [[主页](https://www.catcm.org.cn/139/202407/4051.html)]
- **张鹤林** 南昌。江西中医药大学副教授、硕士生导师。做中医色诊客观化和舌质舌苔自动分类。 [江西中医药大学] [[主页](https://jsj.jxutcm.edu.cn/info/1071/1977.htm)]
- **熊旺平** 南昌。江西中医药大学教授、硕士生导师。做中医药数据挖掘，并主持基于知识图谱的中成药用药监测。 [江西中医药大学] [[主页](https://jsj.jxutcm.edu.cn/info/1071/1914.htm)]
- **聂斌** 南昌。江西中医药大学教授、硕士生导师。做中药数据分析和健康大数据与人工智能。 [江西中医药大学] [[主页](https://jsj.jxutcm.edu.cn/info/1071/1921.htm)]
- **吴地尧** 南昌。江西中医药大学副教授、硕士生导师。做中医药信息学和临床辅助决策模型。 [江西中医药大学] [[主页](https://jsj.jxutcm.edu.cn/info/1071/1928.htm)]
- **查青林** 南昌。江西中医药大学教授、硕士生导师。用大数据和人工智能辅助健康管理与治未病。 [江西中医药大学] [[主页](https://jcyxy.jxutcm.edu.cn/info/5171/21081.htm)]

</details>

<details>
<summary>华润江中（2）</summary>

- **费翼城** 华润江中先进制造研究室副主任。做中药工业智能体，把生产经验数字化。 [华润江中] [[新闻](https://www.jinantimes.com.cn/news-99-11066075.html)]
- **钟志坚** 华润江中湾里制造基地总经理。做固体制剂智能产线、制粒在线检测和人工智能视觉质检。 [华润江中] [[新闻](https://www.jinantimes.com.cn/news-99-11066075.html)]

</details>


</details>

<details>
<summary>山东（20）</summary>

<details>
<summary>山东中医药大学（11）</summary>

- **魏本征** 山东中医药大学教授、博士生导师，医学信息工程学院院长。主持医学人工智能、中医图像分析和智慧诊疗。 [山东中医药大学医学信息工程学院] [[主页](https://zxxy.sdutcm.edu.cn/info/1109/2430.htm)]
- **生慧** 山东中医药大学副教授、硕士生导师，医学信息工程学院副院长。研究医疗健康大数据与中医药智能化。 [山东中医药大学医学信息工程学院] [[主页](https://zxxy.sdutcm.edu.cn/info/1109/2445.htm)]
- **曹慧** 山东中医药大学医学信息工程学院二级教授、博士生导师。做中医药智能化和医学数据挖掘。 [山东中医药大学医学信息工程学院] [[主页](https://zxxy.sdutcm.edu.cn/info/1086/1972.htm)]
- **魏德健** 山东中医药大学医学信息工程学院副教授、硕士生导师。做中医药智能化和智能医学信息处理。 [山东中医药大学医学信息工程学院] [[主页](https://zxxy.sdutcm.edu.cn/info/1109/2439.htm)]
- **张树剑** 山东中医药大学中医文献与文化研究院教授。主持经脉功能脑表征与脏腑调控知识图谱，用自然语言处理和深度学习重组经络文献。 [山东中医药大学中医文献与文化研究院] [[主页](https://wenxian.sdutcm.edu.cn/info/1042/1234.htm)]
- **任健** 山东中医药大学中医学院教授、博士生导师。招生方向为四诊数实研究。 [山东中医药大学中医学院] [[主页](https://zyxyx.sdutcm.edu.cn/info/1075/5703.htm)]
- **程肖蕊** 山东中医药大学中医药创新研究院特聘教授、博士生导师，兼招硕士。方向含中药药理学和网络药理学。 [山东中医药大学] [[主页](https://cxyjy.sdutcm.edu.cn/info/1253/2588.htm)]
- **刘静** 济南。山东中医药大学医学信息工程学院教授、博士生导师。做中医药智能化和医学影像分析。 [山东中医药大学医学信息工程学院] [[主页](https://zxxy.sdutcm.edu.cn/info/1109/2433.htm)]
- **徐琬梨** 济南。山东中医药大学中医学院副教授、硕士生导师。做舌诊、脉诊和证候相关性。 [山东中医药大学中医学院] [[主页](https://zyxyx.sdutcm.edu.cn/info/1082/5763.htm)]
- **张魁星** 济南。山东中医药大学医学信息工程学院教授，生物医学工程学科主任，山东省中医药人工智能重点学科方向带头人。 [山东中医药大学医学信息工程学院] [[主页](https://zxxy.sdutcm.edu.cn/info/1109/2436.htm)]
- **李明** 济南。山东中医药大学医学信息工程学院教授，研究生处副处长，医疗健康大数据学科方向带头人。 [山东中医药大学医学信息工程学院] [[主页](https://zxxy.sdutcm.edu.cn/info/1109/2432.htm)]

</details>

<details>
<summary>齐鲁工业大学（3）</summary>

- **鹿文鹏** 齐鲁工业大学（山东省科学院）教授、博士生导师，自然语言处理与认知计算团队负责人。做医疗大语言模型与智能体，团队发布扁仓中医大模型。 [齐鲁工业大学（山东省科学院）] [[主页](https://nlp.qlu.edu.cn/wenpeng_lu/)] [[论文](https://arxiv.org/abs/2411.11027)] [[代码](https://github.com/QLU-NLP/BianCang)]
- **王英龙** 齐鲁工业大学（山东省科学院）教授、博士生导师。做医学人工智能与高性能计算，与团队发布扁仓中医大模型。 [齐鲁工业大学（山东省科学院）] [[主页](https://bdi.qlu.edu.cn/2021/1222/c10714a176991/page.htm)] [[代码](https://github.com/QLU-NLP/BianCang)]
- **管红娇** 齐鲁工业大学副教授、硕士生导师。研究医疗大模型，并参与扁仓的辨证与处方评测。 [齐鲁工业大学（山东省科学院）] [[论文](http://jsxb.scsc.cn/introlist_76/794.html)]

</details>

<details>
<summary>山东中医药大学附属医院（2）</summary>

- **邓华亮** 山东中医药大学附属医院院长。主持省级智汇岐黄大模型，面向名医经验和基层诊疗。 [山东中医药大学附属医院] [[新闻](http://ccpd.china.com.cn/2026-04/17/content_43401621.html)]
- **齐向华** 济南。山东中医药大学附属医院博士生导师。创立系统辨证脉学，并牵头智能化脉诊仪。 [山东中医药大学附属医院] [[主页](https://www.sdutcm.edu.cn/info/1003/9618.htm)]

</details>

<details>
<summary>华润东阿阿胶（1）</summary>

- **丁丰俐** 华润东阿阿胶首席信息官。布局滋补领域人工智能大模型，并用数字终端做中医体质辨识。 [华润东阿阿胶] [[新闻](https://cn.chinadaily.com.cn/a/202607/23/WS6a61a78ca310d709c2fbf393.html)]

</details>

<details>
<summary>哈尔滨工业大学（威海）（1）</summary>

- **初佃辉** 哈尔滨工业大学（威海）教授、博士生导师。领衔天功医疗大模型训练平台，并做中医问诊、辨证和食疗辅助。 [哈尔滨工业大学（威海）] [[主页](https://software.hit.edu.cn/12762/list.htm)]

</details>

<details>
<summary>山东大学（1）</summary>

- **臧恒昌** 山东大学药学院研究员、博士生导师。做中药口服制剂先进制造，以及近红外过程分析和连续制造质量可视化。 [山东大学药学院] [[主页](https://kltredp.sdu.edu.cn/rcpy/PItdjj.htm)]

</details>

<details>
<summary>步长制药（1）</summary>

- **束炼** 步长制药信息化建设与管理中心总经理。做中药制造板块的业财一体、仓储执行和产线机器人。 [步长制药] [[新闻](https://articles.e-works.net.cn/700/article153015.htm)]

</details>


</details>

<details>
<summary>河南（12）</summary>

<details>
<summary>河南中医药大学（7）</summary>

- **许玉龙** 河南中医药大学副教授、硕士生导师。用隐结构模型和机器学习建立中医证候辨证规则。 [河南中医药大学] [[主页](https://glxy.hactcm.edu.cn/info/1062/10540.htm)]
- **吴嘉瑞** 河南中医药大学药学院博士生导师。招生方向为基于精准网络药理学的中药抗肿瘤机制研究。 [河南中医药大学药学院] [[招生](https://yjsy.hactcm.edu.cn/images/Userfiles/file_20250506_6388212460132763432631524.pdf)]
- **王常海** 郑州。河南中医药大学副教授、硕士生导师。做四诊客观化、证候数据挖掘和中医诊断。 [河南中医药大学] [[主页](https://zyxy.hactcm.edu.cn/info/1110/2735.htm)]
- **党豪** 郑州。河南中医药大学副教授、硕士生导师。做中医药人工智能、舌象脉诊、知识图谱和数据挖掘。 [河南中医药大学] [[主页](https://cs.haut.edu.cn/info/1541/8594.htm)]
- **车志英** 郑州。河南中医药大学教授、博士生导师。做证候智能信息化和四诊信息人工智能。 [河南中医药大学] [[主页](https://zyxy.hactcm.edu.cn/info/2008/27315.htm)]
- **宋学坤** 郑州。河南中医药大学信息技术学院硕士生导师。做计算生物医学信息学。 [河南中医药大学] [[主页](https://glxy.hactcm.edu.cn/info/1062/8030.htm)]
- **冯素香** 郑州。河南中医药大学教授、博士生导师。做中药智能分析、多组学和质量评价。 [河南中医药大学] [[主页](https://kxy.hactcm.edu.cn/kytd/zyzlpjyxyyfsys.htm)]

</details>

<details>
<summary>河南工业大学（2）</summary>

- **李鹏** 河南工业大学教授、博士生导师，复杂性科学研究院院长。做中医人工智能、舌象和未病建模。 [河南工业大学] [[主页](https://computer.haut.edu.cn/info/1042/10906.htm)]
- **吕磊** 河南工业大学教授、博士生导师。做舌象三维感知和中药材视觉品质分析。 [河南工业大学] [[主页](https://cs.haut.edu.cn/info/1541/5754.htm)]

</details>

<details>
<summary>郑州大学（2）</summary>

- **昝红英** 郑州大学计算机与人工智能学院教授、博士生导师。实验室做中医大模型仲景。 [郑州大学计算机与人工智能学院] [[主页](https://www5.zzu.edu.cn/nlp/info/1004/1169.htm)]
- **贾玉祥** 郑州大学计算机与人工智能学院副教授、硕士生导师。AAAI 仲景论文通讯作者。 [郑州大学计算机与人工智能学院] [[主页](https://www5.zzu.edu.cn/nlp/info/1004/1157.htm)]

</details>

<details>
<summary>河南中医药大学第一附属医院（1）</summary>

- **朱明军** 河南中医药大学第一附属医院教授、岐黄学者。牵头数智中医慢病防控和中医大数据，并参与学校数智中医药研究院。 [河南中医药大学第一附属医院] [[主页](https://www.hnzhy.com/TDoctors-3.html)] [[新闻](http://www.ha.xinhua.org/20260817/ef25dd0c98e94a94be25f0f3b064ee1c/c.html)]

</details>


</details>

<details>
<summary>湖北（15）</summary>

<details>
<summary>湖北中医药大学（12）</summary>

- **沈绍武** 湖北中医药大学研究员、博士生导师，中医药大数据知识工程研究院执行院长。做中医药信息学和临床大数据知识工程。 [湖北中医药大学] [[主页](https://xxy.hbucm.edu.cn/info/1491/11342.htm)]
- **解丹** 湖北中医药大学信息工程学院教授、硕士生导师。做医学人工智能、数据挖掘和自然语言处理。 [湖北中医药大学信息工程学院] [[主页](https://xxy.hbucm.edu.cn/info/1491/11262.htm)]
- **邓文萍** 湖北中医药大学信息工程学院教师。做中医药信息化和标准化。 [湖北中医药大学信息工程学院] [[主页](https://xxy.hbucm.edu.cn/info/1491/11272.htm)]
- **肖勇** 武汉。湖北中医药大学信息工程学院正高级实验师、硕士生导师，中医药大数据知识工程研究院副院长。做中医药信息标准化和大数据。 [湖北中医药大学信息工程学院] [[主页](https://xxy.hbucm.edu.cn/info/1491/11282.htm)]
- **常凯** 武汉。湖北中医药大学信息工程学院高级实验师、硕士生导师。方向是中医药标准化、信息化和中医药人工智能。 [湖北中医药大学信息工程学院] [[主页](https://xxy.hbucm.edu.cn/info/1491/11312.htm)]
- **肖瑞** 武汉。湖北中医药大学信息工程学院副教授、硕士生导师。方向是自然语言处理、大数据分析和人工智能。 [湖北中医药大学信息工程学院] [[主页](https://xxy.hbucm.edu.cn/info/1491/11802.htm)]
- **王艳** 武汉。湖北中医药大学信息工程学院副教授、硕士生导师。方向是数据挖掘、智能优化、标准化与信息化和生物信息学。 [湖北中医药大学信息工程学院] [[主页](https://xxy.hbucm.edu.cn/info/1491/11332.htm)]
- **常健** 武汉。湖北中医药大学信息工程学院副教授、硕士生导师。做智慧医药、大数据分析和基于区块链的智能物联网。 [湖北中医药大学信息工程学院] [[主页](https://xxy.hbucm.edu.cn/info/1491/14162.htm)]
- **付文娇** 武汉。湖北中医药大学信息工程学院副教授、硕士生导师。方向是中医药数据处理、标准化和信息化。 [湖北中医药大学信息工程学院] [[主页](https://xxy.hbucm.edu.cn/info/1491/11792.htm)]
- **蔡晓鸿** 武汉。湖北中医药大学信息工程学院副教授、硕士生导师，医学信息工程教研室主任。方向是中医药信息化和数据挖掘。 [湖北中医药大学信息工程学院] [[主页](https://xxy.hbucm.edu.cn/info/1491/11302.htm)]
- **马利** 武汉。湖北中医药大学信息工程学院教授、硕士生导师。负责中医药大数据发展研究中心，做大数据分析和循证决策。 [湖北中医药大学信息工程学院] [[主页](https://xxy.hbucm.edu.cn/info/1491/11252.htm)]
- **管华** 武汉。湖北中医药大学信息工程学院高级实验师、硕士生导师。做中医药大数据分析和自然语言处理。 [湖北中医药大学信息工程学院] [[主页](https://xxy.hbucm.edu.cn/info/1491/11322.htm)]

</details>

<details>
<summary>湖北省中医院（2）</summary>

- **肖飞** 湖北省中医院信息中心主任。推进中医药与人工智能融合、智能医疗数据挖掘和数字化传承。 [湖北省中医院] [[主页](https://xxy.hbucm.edu.cn/info/1661/13882.htm)]
- **孙静** 湖北省中医院信息中心副主任。做智能医疗数据挖掘、中医药数字化传承，以及人工智能在诊疗和科研中的应用。 [湖北省中医院] [[主页](https://xxy.hbucm.edu.cn/info/1661/13882.htm)]

</details>

<details>
<summary>武汉市中医医院（1）</summary>

- **孙淼** 武汉市中医医院信息中心主任。介绍汉派中医骨伤诊疗数据集和骨伤智能体。 [武汉市中医医院] [[新闻](https://xxy.hbucm.edu.cn/info/1661/13042.htm)]

</details>


</details>

<details>
<summary>湖南（17）</summary>

<details>
<summary>湖南中医药大学（14）</summary>

- **彭绍亮** 湖南中医药大学中医学院博士生导师。方向是生物信息与人工智能。 [湖南中医药大学中医学院] [[招生](http://static.hhkaobo.com/upload/editor/7a445106-62d0-4b9e-86b1-25e9fed5229f.pdf)]
- **晏峻峰** 湖南中医药大学教授、博士生导师。做中医人工智能与计算中医学。 [湖南中医药大学] [[主页](https://xxgc.hnucm.edu.cn/info/1036/2517.htm)]
- **韦昌法** 湖南中医药大学教授、硕士生导师。做中医智能辅助诊疗，以及大模型与知识图谱问答。 [湖南中医药大学信息科学与工程学院] [[主页](https://xxgc.hnucm.edu.cn/info/1036/3990.htm)]
- **梁昊** 湖南中医药大学副教授、博士生导师。带学生做智能望诊，识别染苔并降低舌诊仪成本。 [湖南中医药大学] [[主页](https://kczx.hnucm.edu.cn/info/1005/2198.htm)]
- **丁长松** 湖南中医药大学信息科学与工程学院院长、教授、博士生导师。做中医药大数据和方剂功效的可计算研究。 [湖南中医药大学信息科学与工程学院] [[主页](https://xxgc.hnucm.edu.cn/info/1036/2522.htm)]
- **肖晓霞** 湖南中医药大学信息科学与工程学院教授、硕士生导师。做机器视觉和中医智能诊断设备。 [湖南中医药大学信息科学与工程学院] [[主页](https://xxgc.hnucm.edu.cn/info/1036/3987.htm)]
- **刘青萍** 湖南中医药大学信息科学与工程学院副教授、硕士生导师。做中医临床决策支持、数据挖掘和知识发现。 [湖南中医药大学信息科学与工程学院] [[主页](https://xxgc.hnucm.edu.cn/info/1036/3985.htm)]
- **严承** 湖南中医药大学信息科学与工程学院教授、博士生导师。做中药信息学、生物信息学和人工智能。 [湖南中医药大学信息科学与工程学院] [[主页](https://xxgc.hnucm.edu.cn/info/1036/3989.htm)]
- **李阳** 湖南中医药大学信息科学与工程学院教师。做中医药信息处理。 [湖南中医药大学信息科学与工程学院] [[主页](https://xxgc.hnucm.edu.cn/info/1036/6061.htm)]
- **刘旺华** 湖南中医药大学中医学院博士生导师。招生方向为四诊信息数字化与辨证智能化。 [湖南中医药大学中医学院] [[招生](http://static.hhkaobo.com/upload/editor/7a445106-62d0-4b9e-86b1-25e9fed5229f.pdf)]
- **谢梦洲** 湖南中医药大学中医学院博士生导师。招生方向为中医诊断四诊客观化。 [湖南中医药大学中医学院] [[招生](https://static.kaoyan.cn/file/2025/01/22/a5b4ec5e68ea0f116b85c64554c9f6a0.pdf)]
- **刘密** 长沙。湖南中医药大学针灸推拿与康复学院副院长、教授、博士生导师。做中医智能康复装备和针灸数智化教学。 [湖南中医药大学针灸推拿与康复学院] [[主页](https://zjtn.hnucm.edu.cn/info/1101/2793.htm)]
- **胡志希** 长沙。湖南中医药大学教授、博士生导师，中医诊断学学科带头人。做中医诊疗仪器，并有脉象监测和康复穿戴设备专利。 [湖南中医药大学] [[主页](https://dfzyxk.hnucm.edu.cn/info/1027/1351.htm)]
- **周小青** 长沙。湖南中医药大学中医学院二级教授、博士生导师。做数字中医诊断和舌苔计量诊断。 [湖南中医药大学中医学院] [[主页](https://zyxy.hnucm.edu.cn/info/1124/4872.htm)]

</details>

<details>
<summary>吉首大学（1）</summary>

- **周恺卿** 吉首。吉首大学计算机科学与工程学院硕士生导师。主持湘西土家医、苗医胃病诊断知识库和智能决策系统。 [吉首大学计算机科学与工程学院] [[主页](https://cse.jsu.edu.cn/yjsjy/dsjj/7ee92686c2c44467988ea549cc4dc868.htm)]

</details>

<details>
<summary>智慧眼（1）</summary>

- **邱建华** 智慧眼创始人、董事长。公司发布多模态大模型砭石，用于问诊、舌面诊和中医四诊。 [智慧眼] [[新闻](https://www.a-eye.cn/news_list/296.html)] [[网站](https://www.a-eye.cn/)]

</details>

<details>
<summary>湖南大学（1）</summary>

- **梁桥康** 湖南大学人工智能与机器人学院教授、博士生导师。针灸机器人国家重点研发课题负责人，做机器人力视触觉感知和控制。 [湖南大学人工智能与机器人学院] [[主页](https://robotics.hnu.edu.cn/info/1176/3095.htm)]

</details>


</details>

<details>
<summary>广东（30）</summary>

<details>
<summary>广州中医药大学（10）</summary>

- **许能贵** 广州中医药大学二级教授、博士生导师，华南针灸研究中心主任。主持基于人工智能的针刺治疗脑病机制研究。 [广州中医药大学华南针灸研究中心] [[主页](https://scrcam.gzucm.edu.cn/info/1101/1488.htm)]
- **赵屹** 广州中医药大学医学信息工程学院博士生导师。2026 年招收中医药人工智能方向。 [广州中医药大学医学信息工程学院] [[招生](https://yjsy.gzucm.edu.cn/info/1005/17376.htm)]
- **曹东** 广州中医药大学医学信息工程学院博士生导师。2026 年招收中医药人工智能方向。 [广州中医药大学医学信息工程学院] [[招生](https://yjsy.gzucm.edu.cn/info/1005/17376.htm)]
- **周武** 广州中医药大学医学信息工程学院博士生导师。方向是中医舌诊、面诊智能化和中医证候客观化。 [广州中医药大学医学信息工程学院] [[招生](https://yjsy.gzucm.edu.cn/info/1005/17376.htm)]
- **黎晖** 广州中医药大学基础医学院博士生导师。方向包括中医人工智能理论基础与应用。 [广州中医药大学基础医学院] [[招生](https://yjsy.gzucm.edu.cn/info/1005/17376.htm)]
- **陈新林** 广州中医药大学基础医学院博士生导师。方向是中医大数据统计分析和个体化设计评价。 [广州中医药大学基础医学院] [[招生](https://yjsy.gzucm.edu.cn/info/1005/17376.htm)]
- **林传权** 广州中医药大学科技创新中心博士生导师。方向包括人工智能与中医诊疗现代化。 [广州中医药大学科技创新中心] [[招生](https://yjsy.gzucm.edu.cn/info/1005/17376.htm)]
- **门韶洋** 广州中医药大学副教授、博士生导师。做智能中医诊断和医学信号信息处理。 [广州中医药大学医学信息工程学院] [[主页](https://ygxy.gzucm.edu.cn/info/1241/2551.htm)]
- **刘秀峰** 广州中医药大学教授、硕士生导师。做中医知识图谱、古籍整理和中医人工智能。 [广州中医药大学医学信息工程学院] [[主页](https://ygxy.gzucm.edu.cn/info/1241/2551.htm)]
- **潘胡丹** 广州中医药大学教授。做风湿病多模态数据和中西医结合大模型。 [广州中医药大学] [[新闻](https://www.cntcm.com.cn/content/202406/14/c251936.html)]

</details>

<details>
<summary>中医药广东省实验室（4）</summary>

- **刘良** 中国工程院院士，中医药广东省实验室（横琴实验室）主任。实验室从事辨证论治、现代诊疗装备和中医横琴大模型。 [中医药广东省实验室，广州中医药大学] [[招聘](https://www.gzucm.edu.cn/info/1461/117451.htm)]
- **梁勇** 中医药广东省实验室（横琴实验室）博士生导师。2026 年在广州中医药大学招收中医药人工智能方向。 [中医药广东省实验室，广州中医药大学] [[招生](https://yjsy.gzucm.edu.cn/info/1005/17376.htm)]
- **周华** 中医药广东省实验室副主任。负责中药新药智能自动化平台和数智诊疗基础设施。 [中医药广东省实验室，广东省中医院] [[新闻](https://www.hengqin.gov.cn/macao_zh_hans/hzqgl/dtyw/dtxx/content/post_3807664.html)]
- **罗胜达** 中医药广东省实验室研究人员。介绍中医横琴大模型、证候推理和中西药联用智能体。 [中医药广东省实验室] [[新闻](https://www.hengqin.gov.cn/macao_zh_hans/hzqgl/dtyw/dtxx/content/post_3807664.html)]

</details>

<details>
<summary>华为云（2）</summary>

- **乔楠** 华为云人工智能科学计算总经理。在数智本草发布会上讲解问答、生成和天然产物分子计算。 [华为云] [[新闻](https://news.qq.com/rain/a/20240515A04TAH00)]
- **杨鹏程** 数智本草大模型应用开发负责人。做语言与计算双模型筛方。 [华为云] [[新闻](https://bbs.huaweicloud.com/blogs/448824)]

</details>

<details>
<summary>固生堂（2）</summary>

- **郑项** 固生堂副总裁，负责国医 AI 分身和中医大脑。 [固生堂] [[新闻](https://www.gstzy.cn/news/detail/10/13791.html)]
- **扈中凯** 固生堂首席技术官，负责中医大模型、临床数据和诊疗场景落地。 [固生堂] [[新闻](https://www.gstzy.cn/news/detail/10/13791.html)]

</details>

<details>
<summary>广东工业大学（2）</summary>

- **何昭水** 广东工业大学自动化学院教授、博士生导师。针灸机器人国家重点研发计划项目负责人，做穴位定位、进针和提插捻转。 [广东工业大学自动化学院] [[主页](https://www.gdut.edu.cn/info/1709/18526.htm)]
- **郭靖** 广东工业大学自动化学院副教授、硕士生导师。以子课题负责人参与针灸机器人重点研发，负责手法采集、分析和复现。 [广东工业大学自动化学院] [[主页](https://teacher.gdut.edu.cn/guojing1/zh_CN/index.htm)]

</details>

<details>
<summary>广药集团（2）</summary>

- **李小军** 广药集团董事长。推动从药材种植介入的人工智能中药模型。 [广药集团] [[新闻](https://news.dayoo.com/guangzhou/202609/22/139995_55006504.htm)]
- **梁海峰** 广药集团首席信息官、数字经济研究院副院长。负责药品溯源、智能制造和人工智能。 [广药集团] [[新闻](http://event.d1net.com/cioyy2024/)]

</details>

<details>
<summary>华南理工大学（1）</summary>

- **文贵华** 华南理工大学计算机学院教授，广东省人工智能中医工程技术研究团队负责人。做可解释舌诊、体质辨识和智能中医诊疗。 [华南理工大学计算机学院] [[主页](https://www2.scut.edu.cn/cs/2017/0629/c22284a328095/page.htm)]

</details>

<details>
<summary>哈尔滨工业大学（深圳）（1）</summary>

- **张大鹏** 哈尔滨工业大学（深圳）计算机学院博士生导师。做计算机舌诊、脉诊等诊察生物特征。 [哈尔滨工业大学（深圳）计算机学院] [[主页](https://csen.hitsz.edu.cn/info/1023/1904.htm)]

</details>

<details>
<summary>广东省中医院（1）</summary>

- **杨志敏** 广东省中医院副院长、教授、主任医师、博士生导师。做中医健康状态辨识，中心重点做便携舌诊和脉诊装备。 [广东省中医院] [[主页](https://www.jiicm.com/info/1017/1177.htm)]

</details>

<details>
<summary>招联消费金融（1）</summary>

- **章杨清** 招联消费金融总经理。发起中医大模型仲思。 [招联消费金融] [[新闻](http://finance.people.com.cn/n1/2025/0430/c1004-40471496.html)]

</details>

<details>
<summary>暨南大学（1）</summary>

- **张荣华** 暨南大学教授、博士生导师，广东省中医药信息化重点实验室主任。 [暨南大学] [[主页](https://zyxy.jnu.edu.cn/2021/0903/c6333a646617/page.htm)]

</details>

<details>
<summary>深圳大学（1）</summary>

- **欧阳乐** 深圳大学电子与信息工程学院副教授、博士生导师。与深圳市中医院合作中医智能问诊大模型。 [深圳大学] [[主页](https://iip.szu.edu.cn/info/1017/1231.htm)]

</details>

<details>
<summary>腾讯健康（1）</summary>

- **闫鹏** 腾讯健康副总裁。与津药达仁堂合作，用大模型做中医药服务和中西医结合问答。 [腾讯健康] [[新闻](https://www.pharm.com.cn/content/details59_1561.html)]

</details>

<details>
<summary>香港中文大学（深圳）（1）</summary>

- **王本友** 香港中文大学（深圳）数据科学学院助理教授、博士生导师、校长青年教授。做医疗多模态大模型，团队发布中医多模态模型 ShizhenGPT。 [香港中文大学（深圳）数据科学学院] [[主页](http://www.slai.edu.cn/zh-hans/teacher/208)] [[论文](https://arxiv.org/abs/2508.14706)] [[团队](https://freedomintelligence.github.io/people/)] [[代码](https://github.com/FreedomIntelligence/ShizhenGPT)]

</details>


</details>

<details>
<summary>广西（9）</summary>

<details>
<summary>广西中医药大学（5）</summary>

- **邓鑫** 广西中医药大学瑞康临床医学院博士生导师。方向包括中医药治疗慢性肝病、肿瘤和中医药人工智能。 [广西中医药大学瑞康临床医学院] [[招生](https://www.gxtcmu.edu.cn/upload/yjsy/contentmanage/article/file/2025/11/25/%E5%B9%BF%E8%A5%BF%E4%B8%AD%E5%8C%BB%E8%8D%AF%E5%A4%A7%E5%AD%A62026%E5%B9%B4%E5%8D%9A%E5%A3%AB%E7%A0%94%E7%A9%B6%E7%94%9F%E6%8B%9B%E7%94%9F%E4%B8%93%E4%B8%9A%E7%9B%AE%E5%BD%95%EF%BC%88%E5%8F%91%E5%B8%83%E5%AE%98%E7%BD%91%EF%BC%89.pdf)]
- **朱华** 南宁。广西中医药大学博士生导师、硕士生导师。指导研究生做壮瑶药饮片图像识别、光谱和数据挖掘鉴定。 [广西中医药大学] [[主页](https://www.gxtcmu.edu.cn/yjsy/dsdw1/sssds/1056zyxss/content_45370)]
- **马雯芳** 南宁。广西中医药大学药学院硕士生导师。用人工神经网络做壮药谱效分析，并做壮药、瑶药质量标准。 [广西中医药大学药学院] [[主页](https://www.gxtcmu.edu.cn/yxy/kstd/zyjdjys/szdw11/content_47017)]
- **周祖亮** 南宁。广西中医药大学基础医学院硕士生导师。主持壮医药词汇语料库和古壮字医药文献整理。 [广西中医药大学基础医学院] [[主页](https://www.gxtcmu.edu.cn/jcyxy/jysjs/ygwjys/szdw8/content_47715)]
- **宋宁** 南宁。广西中医药大学壮医药学院硕士生导师。做壮医目诊教学信息化和名医用药数据挖掘。 [广西中医药大学壮医药学院] [[主页](https://www.gxtcmu.edu.cn/zyyxy/jysjs/zyjcjys/szdw1/content_46931)]

</details>

<details>
<summary>广西国际壮医医院（2）</summary>

- **黄国东** 南宁。广西国际壮医医院院长、博士生导师。医院已落地本地大模型体检解读、人工智能舌象辨识和远程四诊仪，并筹建壮医目诊辅助平台。 [广西国际壮医医院] [[主页](https://www.gxtcmu.edu.cn/xwzx/xyxw/fsdw/content_89250)]
- **黄汉儒** 南宁。广西国际壮医医院博士生导师、硕士生导师。领衔人工智能壮瑶医工程研究中心。 [广西国际壮医医院] [[主页](https://www.gxtcmu.edu.cn/msmy/myi/content_64198)]

</details>

<details>
<summary>南宁师范大学（1）</summary>

- **彭昱忠** 南宁。南宁师范大学教授、硕士生导师。做智能计算和机器学习的生物医学应用，并参与广西中医药交叉创新。 [南宁师范大学] [[主页](https://www.gxtcmu.edu.cn/yjsy/dsdw1/sssds/1053ggws/content_68640)]

</details>

<details>
<summary>广西中医药大学第一附属医院（1）</summary>

- **黄瑾明** 南宁。广西中医药大学第一附属医院硕士生导师。领衔人工智能壮瑶医工程研究中心。 [广西中医药大学第一附属医院] [[主页](https://www.gxtcmu.edu.cn/xwzx/xyxw/fsdw/content_14649)]

</details>


</details>

<details>
<summary>海南（1）</summary>

<details>
<summary>海南医科大学（1）</summary>

- **宫爱民** 海口。海南医科大学中医学院副院长、博士生导师、硕士生导师。用机器视觉和机器学习构建中医证候诊断模型。 [海南医科大学] [[主页](https://www.muhn.edu.cn/zyxy/info/1412/8735.htm)]

</details>


</details>

<details>
<summary>重庆（1）</summary>

<details>
<summary>西南大学（1）</summary>

- **李莉** 西南大学计算机与信息科学学院教授、博士生导师。中医大模型 TCM-R1 通讯作者。 [西南大学计算机与信息科学学院] [[主页](https://cis.swu.edu.cn/info/1184/4082.htm)]

</details>


</details>

<details>
<summary>四川（7）</summary>

<details>
<summary>成都中医药大学（7）</summary>

- **温川飙** 成都中医药大学博士生导师。团队建设中医药 AI 模型高质量数据集，并做中医药人工智能 AIGC；数据集入选人工智能医疗器械揭榜挂帅。 [成都中医药大学] [[招生](https://zyd.cdutcm.edu.cn/yjs/dsfc/bsyjsds)] [[新闻](https://www.cdutcm.edu.cn/info/1074/138321.htm)] [[论坛](https://www.cdutcm.edu.cn/info/1074/136241.htm)]
- **陈伟** 成都中医药大学讲席教授。团队发布中药全产业链大模型本草智库，覆盖药材基因、成分靶点和知识图谱。 [成都中医药大学] [[新闻](https://www.cdutcm.edu.cn/info/1080/4591.htm)]
- **曾芳** 成都中医药大学教授、博士生导师、校长。做针灸效应与人工智能辅助临床决策，团队研究大模型参与腧穴配伍决策。 [成都中医药大学] [[主页](https://www.cdutcm.edu.cn/info/1004/1005.htm)] [[新闻](https://www.cdutcm.edu.cn/info/1075/138561.htm)]
- **蒋涛** 成都中医药大学智能医学学院院长、教授、博士生导师。参与天惠中医大模型，并做中医智能装备。 [成都中医药大学智能医学学院] [[论文](https://arxiv.org/abs/2509.19834)]
- **王德贤** 成都中医药大学副教授、硕士生导师。做针灸处方智能推荐。 [成都中医药大学] [[主页](https://www.ntu.edu.cn/2026/1008/c8083a300123/page.htm)]
- **吴纯洁** 成都中医药大学药学院研究员、博士生导师。做中药饮片性状数字化评价，建有智能感官分析平台。 [成都中医药大学药学院] [[主页](https://www.cscsh.com/kj/198805.html)]
- **张艺** 成都。成都中医药大学民族医药学术传承创新研究中心博士生导师。主持西南少数民族医药文献数据库，对象包括藏、傣、彝、苗等文献，团队建成藏医药古籍和《四部医典》地理信息平台。 [成都中医药大学] [[主页](https://www.cdutcm.edu.cn/info/1080/52121.htm)] [[新闻](http://hgxy.hunnu.edu.cn/info/1175/5651.htm)]

</details>


</details>

<details>
<summary>贵州（13）</summary>

<details>
<summary>贵州中医药大学（10）</summary>

- **谢泉** 贵州中医药大学信息工程学院执行院长、教授。牵头中医药全产业链语料，服务垂类大模型。 [贵州中医药大学信息工程学院] [[主页](https://xxgc.gzy.edu.cn/info/1289/3160.htm)]
- **胡成刚** 贵阳。贵州中医药大学药学院硕士生导师、苗医药研究院副院长。主持标本馆数字化和贵州省中药资源信息数据库。 [贵州中医药大学药学院] [[主页](https://yaoxue.gzy.edu.cn/info/1458/3599.htm)]
- **江洪** 贵阳。贵州中医药大学药学院硕士生导师。主讲苗药，并指导苗医药人工智能项目苗慧智云。 [贵州中医药大学药学院] [[主页](https://yaoxue.gzy.edu.cn/info/1383/3020.htm)]
- **程文波** 贵阳。贵州中医药大学信息工程学院硕士生导师。招生方向为人工智能，并指导苗医药人工智能项目苗慧智云。 [贵州中医药大学信息工程学院] [[主页](https://yjs.gzy.edu.cn/info/2034/2631.htm)]
- **张昀** 贵阳。贵州中医药大学硕士生导师。用机器学习研究非编码RNA，并做药用植物小分子RNA深度学习分析。 [贵州中医药大学] [[主页](https://xxgc.gzy.edu.cn/info/1196/1464.htm)]
- **焦宏官** 贵阳。贵州中医药大学硕士生导师。参与中医药信息国际标准，并做苗医药文献分析。 [贵州中医药大学] [[主页](https://xxgc.gzy.edu.cn/info/1196/1464.htm)]
- **肖巧巧** 贵阳。贵州中医药大学药学院硕士生导师。用生物信息学建设药用植物基因功能数据库。 [贵州中医药大学药学院] [[主页](https://yaoxue.gzy.edu.cn/info/1458/3695.htm)]
- **郭正红** 贵阳。贵州中医药大学药学院硕士生导师。用计算和生物信息分析苗药等民族药活性成分。 [贵州中医药大学药学院] [[主页](https://yaoxue.gzy.edu.cn/info/1458/3571.htm)]
- **王仁民** 贵阳。贵州中医药大学副教授、硕士生导师。2026年招收电子信息人工智能方向。 [贵州中医药大学] [[主页](https://yjs.gzy.edu.cn/info/2034/2631.htm)]
- **杜光映** 贵阳。贵州中医药大学硕士生导师。招收人工智能和中药资源方向，并参与苗医药知识图谱分析。 [贵州中医药大学] [[主页](https://yjs.gzy.edu.cn/info/2034/2631.htm)]

</details>

<details>
<summary>贵州医科大学（2）</summary>

- **汤磊** 贵州医科大学党委书记，中药功效成分全国重点实验室执行主任。牵头发布民族药大模型华族本草。 [贵州医科大学] [[新闻](https://www.stdaily.com/web/gdxw/2026-08/03/content_558608.html)]
- **杨宁线** 贵阳。贵州医科大学青年博士生导师。用人工智能评价抗菌肽，并做特色食药资源开发。 [贵州医科大学] [[主页](https://fnh.gmc.edu.cn/info/1006/2194.htm)]

</details>

<details>
<summary>贵阳道生健康产业有限公司（1）</summary>

- **张建锋** 贵阳。贵阳道生健康产业有限公司研究人员，贵州中医药大学硕士生导师。做中药民族药工艺质量评价和网络分析。 [贵阳道生健康产业有限公司] [[主页](https://yaoxue.gzy.edu.cn/info/1458/3562.htm)]

</details>


</details>

<details>
<summary>云南（9）</summary>

<details>
<summary>云南中医药大学（6）</summary>

- **郭沛鑫** 云南中医药大学教授、博士生导师。用人工智能、科学计算和多组学做经典名方二次开发。 [云南中医药大学] [[主页](https://www.ynucm.edu.cn/info/1045/178391.htm)]
- **张超** 昆明。云南中医药大学博士生导师。在云南省傣医药与彝医药重点实验室负责傣医、彝医文献库、单验方库和院内制剂库。 [云南中医药大学] [[主页](https://dym.ynucm.edu.cn/info/1011/1049.htm)]
- **钱子刚** 昆明。云南中医药大学博士生导师。为傣族、彝族药材建立 DNA 条形码鉴定库和鉴定网站。 [云南中医药大学] [[主页](https://dym.ynucm.edu.cn/info/1011/1049.htm)]
- **温伟波** 昆明。云南中医药大学教授、博士生导师、硕士生导师。用数据挖掘做中医药临床队列，并做民族医药研发。 [云南中医药大学] [[主页](https://mbfzsys.ynucm.edu.cn/info/1020/1049.htm)]
- **罗艳秋** 昆明。云南中医药大学硕士生导师。编纂彝族、傣族医药古籍总目，并做彝医药古籍抢救。 [云南中医药大学] [[主页](https://dym.ynucm.edu.cn/info/1013/1167.htm)]
- **陈清华** 昆明。云南中医药大学硕士生导师、傣医学后备学科带头人。参与制定傣医病证分类代码和临床诊疗术语。 [云南中医药大学] [[主页](https://dym.ynucm.edu.cn/info/1013/1167.htm)]

</details>

<details>
<summary>云南白药集团（3）</summary>

- **万五洲** 云南白药集团中央研究院院长。讲人工智能赋能下从创新药到智慧中药的研发。 [云南白药集团] [[主页](https://www.yunnanbaiyao.com.cn/view/ynbyPc/1/92/view/9201.html)]
- **李少春** 云南白药集团数字战略科学家、数智科技公司总经理、首席信息官。领衔中医药雷公大模型。 [云南白药集团] [[新闻](http://www.datayuan.cn/article/22489.htm)]
- **范启强** 云南白药集团数智科技有限公司相关负责人。做灯塔工厂数智化和工业智能工厂升级。 [云南白药集团] [[主页](https://www.yunnanbaiyao.com.cn/view/ynbyPc/1/92/view/8368.html)]

</details>


</details>

<details>
<summary>西藏（3）</summary>

<details>
<summary>西藏大学（3）</summary>

- **拥措** 拉萨。西藏大学信息科学技术学院博士生导师、硕士生导师。做藏医药文献实体关系抽取，用于知识图谱。 [西藏大学信息科学技术学院] [[主页](https://xbna.pku.edu.cn/fileup/0479-8023/HTML/2025-5-860.html)]
- **尼玛扎西** 拉萨。西藏大学信息科学技术学院博士生导师、硕士生导师。参与藏医药文献关系抽取和藏文古籍数字化。 [西藏大学信息科学技术学院] [[招生](http://static.hhkaobo.com/upload/editor/fd7e90b8-9745-4ca6-97cc-d7fd16d332d2.pdf)]
- **王嗣岑** 拉萨。西藏大学博士生导师。与中央民族大学合作用人工智能模型筛选抗纤维化藏药。 [西藏大学] [[主页](https://www.muc.edu.cn/info/1052/36678.htm)]

</details>


</details>

<details>
<summary>陕西（3）</summary>

<details>
<summary>陕西中医药大学（2）</summary>

- **闻永毅** 陕西中医药大学教授、硕士生导师。做中医文献数字化、知识图谱、古籍信息抽取和大语言模型。 [陕西中医药大学] [[主页](http://yzb.sntcm.edu.cn/xjsds/rwglhy/0453gjzwjy/113981.htm)]
- **侯滢** 咸阳。陕西中医药大学人文管理学院硕士生导师。做智能医疗和中医药管理。 [陕西中医药大学] [[主页](http://yzb.sntcm.edu.cn/xjsds/rwglhy/1005z2zylglh/113986.htm)]

</details>

<details>
<summary>西北大学（1）</summary>

- **王永华** 西北大学生物信息中心教授。建中药系统药理学数据库 TCMSP。 [西北大学] [[主页](https://life.nwafu.edu.cn/yjsjy/yjsgl/070cf28723284d418f42b14c1175437b.htm)]

</details>


</details>

<details>
<summary>甘肃（2）</summary>

<details>
<summary>甘肃中医药大学药学院（1）</summary>

- **靳晓杰** 兰州。甘肃中医药大学药学院副教授、博士生导师。做中药化学信息学和计算机辅助药物发现。 [甘肃中医药大学药学院] [[主页](https://yxx.gszy.edu.cn/html/cid/83.html?page=1)]

</details>

<details>
<summary>甘肃省中医院（1）</summary>

- **张志明** 兰州。甘肃省中医院院长、博士生导师。推动数字化舌诊和人工智能辅助望诊。 [甘肃省中医院] [[主页](https://xxxy.xzhmu.edu.cn/info/1005/2985.htm)]

</details>


</details>

<details>
<summary>青海（2）</summary>

<details>
<summary>青海大学（2）</summary>

- **周则** 西宁。青海大学藏医学院硕士生导师。主持藏药药用植物图像库和藏药方剂数据库。 [青海大学藏医学院] [[主页](https://zyxy.qhu.edu.cn/szdw/qnjstd/29957.htm)]
- **多杰** 西宁。青海大学藏医学院硕士生导师。参与藏医药文献数字化和传统医籍加工。 [青海大学藏医学院] [[主页](https://zyxy.qhu.edu.cn/kxyj/yjxm/27856.htm)]

</details>


</details>

<details>
<summary>宁夏（3）</summary>

<details>
<summary>宁夏医科大学（3）</summary>

- **张文学** 银川。宁夏医科大学硕士生导师。做中医药信息学、名医方剂数据挖掘和医药知识图谱。 [宁夏医科大学] [[主页](https://www.nxmu.edu.cn/lxy/info/1051/1123.htm)]
- **杨德仁** 银川。宁夏医科大学硕士生导师。做中医药信息学。 [宁夏医科大学] [[主页](https://www.nxmu.edu.cn/lxy/info/1051/1122.htm)]
- **陈耀庚** 银川。宁夏医科大学硕士生导师。做医药数据挖掘，并讲授中医药信息学。 [宁夏医科大学] [[主页](https://www.nxmu.edu.cn/lxy/info/1051/1120.htm)]

</details>


</details>

<details>
<summary>新疆（3）</summary>

<details>
<summary>新疆医科大学（2）</summary>

- **木拉提·哈米提** 乌鲁木齐。新疆医科大学医学工程技术学院硕士生导师。做维医异常体液病数据挖掘辅助诊断、维药材图像资源库，以及哈萨克族食管癌图像分类。 [新疆医科大学医学工程技术学院] [[主页](http://school.freekaoyan.com/xj/xjmu/zhuanye/2016/01-31/1454243071480819.shtml)]
- **严传波** 乌鲁木齐。新疆医科大学副教授、硕士生导师。做维药材图像检索，并参与哈萨克族食管癌图像的支持向量机和神经网络分类。 [新疆医科大学医学工程技术学院] [[主页](https://xjyy.cbpt.cnki.net/portal/journal/portal/client/paper/a87ac666d8ff75c2aa5aa85b3c52f76d)]

</details>

<details>
<summary>新疆大学（1）</summary>

- **夏静静** 乌鲁木齐。新疆大学药学院硕士生导师。用中红外光谱和化学计量学评价维医用药毛菊苣种子，方向含机器学习和卷积神经网络。 [新疆大学药学院] [[主页](https://imm.xju.edu.cn/info/1059/1372.htm)]

</details>


</details>

<details>
<summary>香港（8）</summary>

<details>
<summary>香港浸会大学（5）</summary>

- **吕爱平** 香港浸会大学副校长、中医药学院讲座教授。做中医药转化与系统医学，推动中医药和人工智能、数据科学结合。 [香港浸会大学中医药学院] [[主页](https://endowed-professorships.hkbu.edu.hk/zh-hk/endowed-professors/professor-lyu-aiping.html)] [[新闻](https://jumc.jju.edu.cn/info/1049/6997.htm)]
- **张戈** 香港浸会大学中医药学院讲座教授、副院长。主持人工智能驱动的适配体发现。 [香港浸会大学中医药学院] [[主页](https://scholars.hkbu.edu.hk/en/persons/ZHANGGE/)]
- **田亮** 香港浸会大学物理系副教授。做中医药数据挖掘，以及网络药理和中药质控人工智能平台。 [香港浸会大学] [[主页](https://scholars.hkbu.edu.hk/en/persons/LIANGTIAN/)]
- **张璐** 香港浸会大学教授。做面向中药治疗胃肠癌的生物医学人工智能智能体。 [香港浸会大学] [[主页](https://research.hkbu.edu.hk/sc/1-1-1-scheme/projects)]
- **朱褔荣** 香港浸会大学教授。用近红外和人工智能鉴别中药材真伪优劣。 [香港浸会大学] [[主页](https://research.hkbu.edu.hk/sc/1-1-1-scheme/projects)]

</details>

<details>
<summary>香港大学（2）</summary>

- **沈剑刚** 香港大学中医药学院教授。用人工智能识别中医脉象及其与体质的关联。 [香港大学中医药学院] [[主页](https://eventregscm.hku.hk/Views/People/ProfessorJiangangShen.html)]
- **冯奕斌** 香港大学中医药学院教授、院长。用网络药理、组学和人工智能研究中医治则。 [香港大学中医药学院] [[主页](https://www.med.hku.hk/en/teaching-and-learning/postgraduate/rpg/projects/ai-assisted-investigation-to-understand-the-treatment-principle-of-chinmed)]

</details>

<details>
<summary>香港中文大学（1）</summary>

- **邢国良** 香港中文大学信息工程学系教授。团队做 OpenTCM，用图谱检索增强中医知识检索和诊断。 [香港中文大学] [[新闻](https://www.ie.cuhk.edu.hk/prof-guoliang-xing-and-prof-hongkai-chens-team-win-best-paper-award-at-bigcom-2025-for-innovative-traditional-chinese-medicine-ai-system/)]

</details>


</details>

<details>
<summary>澳门（4）</summary>

<details>
<summary>澳门大学（2）</summary>

- **路嘉宏** 澳门大学中华医药研究院副教授、副院长。用人工智能筛选抗阿尔茨海默病的中药小分子。 [澳门大学中华医药研究院] [[新闻](https://www.um.edu.mo/zh-hant/news-and-press-releases/presss-release/detail/63849/)]
- **胡元佳** 澳门大学中华医药研究院教授。用网络药理鉴定中药质控标志物，并用神经网络生成分子库。 [澳门大学中华医药研究院] [[主页](https://repository.um.edu.mo/profile/yuanjiahu)]

</details>

<details>
<summary>澳门科技大学（2）</summary>

- **韩子天** 澳门科技大学教授。药食同源方剂推荐大模型 TCM-DS 的通讯作者。 [澳门科技大学] [[主页](https://fie.must.edu.mo/id-848/person/view/id-448.html)]
- **李婷** 澳门科技大学中药质量研究国家重点实验室教授、人工智能跨学科应用研究院副院长。把人工智能用于中药机制和药物发现。 [澳门科技大学] [[简介](https://wm-fs2.must.edu.mo/group1/M00/0B/62/rBCDo2ohKsOAL4esAAMyNfTO-Ng912.pdf)]

</details>


</details>

<details>
<summary>台湾（7）</summary>

<details>
<summary>中国医药大学（3）</summary>

- **罗纶谦** 中国医药大学中医诊断学科教授、台湾中医诊断学会理事长。做中医诊断。 [中国医药大学中医学系] [[主页](http://webap.cmu.edu.tw/TchEportfolio/index_1/lclo)]
- **张恒鸿** 中国医药大学中医诊断学科教授。做中医诊断辅助仪器。 [中国医药大学中医学系] [[主页](https://webap.cmu.edu.tw/TchEportfolio/index_1/tcmchh55)]
- **黄升腾** 中国医药大学中医学系教授兼系主任、附设医院中医部主任。研发人工智能中医临床教学。 [中国医药大学中医学系] [[主页](http://webap.cmu.edu.tw/TchEportfolio/index_1/sthuang)] [[新闻](https://chmed.cmu.edu.tw/news/293/)]

</details>

<details>
<summary>长庚大学（3）</summary>

- **杨贤鸿** 长庚大学中医学系教授兼系主任。与电机系合作，用深度学习做舌体分割和体质辨识。 [长庚大学中医学系] [[主页](https://pure.lib.cgu.edu.tw/en/persons/sien-hung-yang)]
- **李建德** 长庚大学电机工程学系教授。用深度学习做舌体分割、体质辨识和舌象抑郁筛查。 [长庚大学电机工程学系] [[主页](https://pure.lib.cgu.edu.tw/en/persons/jiann-der-lee-3/)]
- **刘耕豪** 长庚大学中医学系助理教授、医预科主任。专长脉诊、针灸和中医诊断。 [长庚大学中医学系] [[主页](https://pure.lib.cgu.edu.tw/en/persons/geng-hao-liu-2)]

</details>

<details>
<summary>东华大学（1）</summary>

- **颜士净** 东华大学资讯工程学系教授、人工智能实验室主持人。与慈济医院合作，用深度学习分析舌诊影像和脉诊信号。 [东华大学资讯工程学系] [[新闻](https://www.csie.ndhu.edu.tw/uncategorized/csie_ai_in_chinese_medicine_ch/)]

</details>


</details>

<details>
<summary>日本（3）</summary>

<details>
<summary>千叶大学（2）</summary>

- **中口俊哉** 千叶大学前沿医工学中心教授、副中心长。做医学图像与计算机辅助诊断，并参与汉方舌诊图像研究。 [千叶大学前沿医工学中心] [[主页](https://www.cfme.chiba-u.jp/en/staff/detail.php?index=nakaguchi)] [[论坛](https://www.m.chiba-u.jp/class/wakan/tongue2021/)]
- **并木隆雄** 千叶大学特任教授。主持汉方舌诊图像研究，推动舌诊相关国际标准。 [千叶大学] [[主页](https://www.m.chiba-u.jp/class/wakan/outline/staff.html)] [[论坛](https://www.m.chiba-u.jp/class/wakan/tongue2021/)]

</details>

<details>
<summary>北里大学北里研究所医院（1）</summary>

- **川锅伊晃** 北里大学北里研究所医院副部长。用机器学习量化汉方舌象，并建立健康人舌象数据库。 [北里大学北里研究所医院] [[主页](https://nrid.nii.ac.jp/en/nrid/1000040445523/)]

</details>


</details>

<details>
<summary>韩国（5）</summary>

<details>
<summary>圆光大学（2）</summary>

- **李元融** 圆光大学韩医科大学教授。做韩药网络药理，并开发草药与化学药相互作用预测模型。 [圆光大学韩医科大学] [[新闻](https://www.wku.ac.kr/%ec%9d%b4%ec%9b%90%ec%9c%b5-%ea%b5%90%ec%88%98-%ec%97%b0%ea%b5%ac%ed%8c%80-%ed%95%9c%ec%95%bd-%ed%95%a9%ec%84%b1%ec%9d%98%ec%95%bd%ed%92%88-%ec%83%81%ed%98%b8%ec%9e%91%ec%9a%a9-%ec%98%88%ec%b8%a1-ai.html)]
- **Jungtae Leem** 圆光大学韩医科大学研究人员。研究脉诊仪用于韩医诊断教学。 [圆光大学韩医科大学] [[论文](https://jkom.org/journal/view.php?number=5266)]

</details>

<details>
<summary>庆熙大学（2）</summary>

- **朴延澈** 庆熙大学韩医科大学针灸科副教授。主持韩医组学与人工智能实验室，用大数据和机器学习研究韩医诊断。 [庆熙大学韩医科大学] [[主页](https://kmoa.khu.ac.kr/members)]
- **Yeonhak Kim** 釜山大学韩医学校兼任教授、庆熙大学研究员。把多组学和人工智能用于韩医研究。 [釜山大学韩医学校，庆熙大学] [[主页](https://kmoa.khu.ac.kr/members)]

</details>

<details>
<summary>大邱庆北科学技术院（1）</summary>

- **金昌业** 大邱庆北科学技术院副教授。用机器学习形式化韩医理论，并做草药网络药理。 [大邱庆北科学技术院] [[主页](https://scholar.dgist.ac.kr/researcher/0b0c2fa5-3add-421e-95cc-aeb8f8beb679)]

</details>


</details>

<details>
<summary>新加坡（1）</summary>

<details>
<summary>新加坡国立大学（1）</summary>

- **陈宇综** 新加坡国立大学药学系终身教授。维护中医药数据库 TCM-ID，并用机器学习研究草药作用。 [新加坡国立大学药学系] [[主页](https://bidd.group/)]

</details>


</details>

<details>
<summary>美国（1）</summary>

<details>
<summary>密苏里大学（1）</summary>

- **徐东** 密苏里大学教授。用深度学习分析舌象，并发布中医多模态问答基准 TCM-Ladder。 [密苏里大学] [[主页](https://bondlsc.missouri.edu/labs/dong-xu/)]

</details>


</details>

<details>
<summary>澳大利亚（1）</summary>

<details>
<summary>西悉尼大学（1）</summary>

- **Xian Zhou** 西悉尼大学 NICM 健康研究所高级研究员。用机器学习刻画草药活性分子的协同或拮抗，并指导研究生。 [西悉尼大学 NICM 健康研究所] [[主页](https://researchers.westernsydney.edu.au/en/persons/phoebe-zhou/)]

</details>


</details>

<details>
<summary>其他（4）</summary>

<details>
<summary>中医在线（2）</summary>

- **何剑** 中医在线创始人、首席执行官。用名老中医课程数据推动伊尹中医大模型。 [中医在线] [[新闻](https://www.vbdata.cn/1519007974)]
- **任毅** 中医在线首席技术官。带领团队部署并微调中医大模型。 [中医在线] [[新闻](https://www.vbdata.cn/1519007974)]

</details>

<details>
<summary>安顿健康（1）</summary>

- **白伟民** 安顿健康创始人、董事长。发布七诊合参中医机器人和中医大模型。 [安顿健康] [[新闻](https://www.xinhuanet.com/finance/20260720/f6a8625c1be4412d9c311a232c7a35fa/c.html)]

</details>

<details>
<summary>智赋岐黄（1）</summary>

- **李坤** 智赋岐黄创始人、董事长。负责四诊仪和天功中医人工智能大模型。 [智赋岐黄] [[新闻](http://business.china.com.cn/2025-12/16/content_43307776.shtml)]

</details>


</details>

## 开源模型

上面是起步用的。要翻全部能下的权重，或只有论文/产品、通用中文医疗底座、闭源产品和日韩汉方/韩医，点开即可。

<details>
<summary>能下载的权重，共 20 个</summary>

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
<summary>60 条，最近有：数据要素大赛新增中医药独立赛道与高质量数 · 广安门医院AI+中医药会议：可信数据集与 · 2026世界传统医药大会AI发展报告与中</summary>

<details>
<summary>2026 · 27</summary>

- [2026.11] 人民网11月5日采访国家中医药管理局监测统计中心主任厉将斌，介绍中医药独立赛道、名医智能体及高质量数据集建设。为新闻与建设线索，未附数据下载。 [[链接](https://finance.people.com.cn/n1/2026/1105/c1004-40828489.html)]
- [2026.11] 北京市卫健委11月4日刊载：10月30日会议讨论中医知识结构化、可信AI数据集、西苑医院中医药肿瘤科学数据系统等；报道未发布开放数据包。 [[链接](https://wjw.beijing.gov.cn/xwzx_20031/jcdt/202611/t20261104_4931739.html)]
- [2026.11] 数字中国建设峰会网站11月3日转载经济日报报道，介绍《人工智能赋能全球传统医学发展报告（2026）》及杭州市中医院“中医小安”机器人。报道涵盖AI传统医学整体，不等同于TCM大语言模型统计。 [[链接](https://www.digitalchina.gov.cn/2026/szzg/xyzx/202611/t20261103_5389002.htm)]
- [2026.10] 中国中医药报10月16日报道汉派中医骨伤诊疗数据集在湖北数据流通平台交易，涉及16.8万条结构化诊疗数据、3600个经验方与辨证论治思维链；属于许可流通案例。 [[链接](https://www.cntcm.com.cn/content/202610/16/c505880.html)]
- [2026.10] 报道称徐桂华团队10月9日发布灵素·艾护中医护理大模型，面向辨证施护、科研与居家康养，27所加盟医院为首批应用单位 [[链接](https://finance.sina.com.cn/jjxw/2026-10-10/doc-iniutqmk0582279.shtml)]
- [2026.09] 中国中医药报9月24日报道广安门医院慢性胃炎数据集完成产权登记，并建设中医专病可信数据空间；数据用于广医·岐智微调、科研和名医经验教学，未见公开下载。 [[链接](https://www.cntcm.com.cn/content/202609/24/c505607.html)]
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
- [2026.04] 北京中医药大学牵头研发的**薪火中国药**中医药教育大模型通过国家生成式人工智能服务备案，成为国内首个获批面向公众