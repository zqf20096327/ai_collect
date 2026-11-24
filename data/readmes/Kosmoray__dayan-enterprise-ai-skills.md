<p align="center">
  <img src="./assets/hero-banner.svg" alt="大衍千机 · 168 个企业 AI 开源技能" width="100%"/>
</p>

<p align="center">
  <a href="https://github.com/Kosmoray/dayan-enterprise-ai-skills/stargazers"><img src="https://img.shields.io/github/stars/Kosmoray/dayan-enterprise-ai-skills?style=for-the-badge&color=AD7B27&label=STARS" alt="GitHub Stars"/></a>
  <a href="https://github.com/Kosmoray/dayan-enterprise-ai-skills/actions"><img src="https://img.shields.io/github/actions/workflow/status/Kosmoray/dayan-enterprise-ai-skills/ci.yml?branch=main&style=for-the-badge&label=CI_VALIDATE" alt="CI Status"/></a>
  <a href="https://skillhub.cn/enterprise-zone"><img src="https://img.shields.io/badge/腾讯_SkillHub-企业专区-1B365D?style=for-the-badge" alt="Tencent SkillHub Verified"/></a>
  <a href="./docs/DOUBAO-VOLCENGINE-GUIDE.md"><img src="https://img.shields.io/badge/豆包工作-接入指南-0066FF?style=for-the-badge" alt="Doubao Work Guide"/></a>
  <a href="https://www.skills.sh/kosmoray/dayan-enterprise-ai-skills"><img src="https://img.shields.io/badge/skills.sh-Global_Indexed-0F766E?style=for-the-badge" alt="skills.sh"/></a>
  <a href="./pyproject.toml"><img src="https://img.shields.io/badge/Python_CLI-Zero_Dependency-3776AB?style=for-the-badge" alt="Python Zero-Dep CLI"/></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-MIT-265592?style=for-the-badge" alt="MIT License"/></a>
</p>

<p align="center">
  <a href="https://kosmoray.github.io/dayan-enterprise-ai-skills/"><strong>🔍 在线关键词检索门户</strong></a> ·
  <a href="https://dayanqianji.com/open-source/"><strong>🌐 大衍千机官网与真实作品</strong></a> ·
  <a href="https://my.feishu.cn/share/base/shrcnhBYBWWVOeFnmlggAhnGXE0"><strong>📋 90秒企业AI落地自测</strong></a> ·
  <a href="./README_EN.md"><strong>🇬🇧 English README</strong></a>
</p>


**当前版本 v1.6.0** 提供 168 个企业 AI 技能、27 个 WorkBuddy 专家和专家团，以及 14 个离线命令行工具。新增船舶修造和半导体耗材两组工具，用于整理询价和交接材料、测算成本、比对质量检验数据。

[查看完整技能目录](./docs/DOUBAO-VOLCENGINE-GUIDE.md#技能目录) · [下载 v1.6.0](https://github.com/Kosmoray/dayan-enterprise-ai-skills/releases/tag/v1.6.0)

制造企业已有 ERP、想从企业微信接入客户改单，可用[订单变更验收样例](./examples/erp-wecom-order-change-acceptance.md)核对审批、重复提交和超时恢复。

---

## 💬 为什么我把公司吃饭的 66 套内部 AI 武器全掀桌子开源了？

你好，我是**雷可扬**。我在四川成都高新区天府长岛（就在《王者荣耀》和《哪吒》团队隔壁）创立了园区首家入驻的一人公司（OPC）——**成都大衍千机科技有限公司**，专门帮实体与成长型企业做 **AI 全案落地（一把手首诊、分岗位实操内训、兜错型知识库、FDE 驻场与 ERP/CRM/GEO 系统建设）**。

过去一年跑遍工厂、外贸、连锁、工程和服务企业，我发现两件极其荒诞的事：
1. **市面上的普通 AI 提示词都是“个人玩具”**：写出来的中文满嘴“赋能、抓手、闭环”，审合同漏掉致命无限连带责任，灌进 Dify 的知识库满嘴胡编乱报价，老板根本不敢真用；
2. **把方法论藏着掖着毫无意义**：这一年我最大的感悟是——真正值钱的是帮客户把脏乱差台账跑通的工程交付力；单点武器与其锁在抽屉里落灰，不如干脆全部脱敏 MIT 开源出来，让大家免费拿去解决手头急活，交个实诚朋友！

> ⭐ **如果这 66 枚技能帮你少加了一次夜班、少踩了一个合同坑、或者洗掉了一篇浓重机器味文章，请顺手点亮右上角 `Star` 捧个人场！你的每一颗 Star，都是我们继续把压箱底工程资产开源出来的动力。**

<p align="center">
  <img src="./assets/before-after.svg" alt="裸调大模型 vs 挂载大衍千机实战 Skill 对比" width="100%"/>
</p>

---

## ⚡ 10 秒极速安装（支持所有主流 Agent 客户端）

兼容 **字节跳动豆包工作（Doubao Work）**、**火山方舟（Volcengine Ark）**、**扣子（Coze）**、**腾讯 WorkBuddy / SkillHub**、**Claude Code**、**Cursor**、**Codex CLI** 等所有支持 `SKILL.md` 标准的智能体工具（详见 [📘 字节豆包工作与火山方舟接入指南](./docs/DOUBAO-VOLCENGINE-GUIDE.md)）：

```bash
# 方式 1：使用 Vercel 官方 skills CLI（自动适配 Claude Code / Cursor / Codex 等）
npx -y skills add Kosmoray/dayan-enterprise-ai-skills

# 只装某一个高频技能（如：中文去AI味精修大师）
npx -y skills add Kosmoray/dayan-enterprise-ai-skills --skill dayan-humanize-pro

# 方式 2：使用腾讯官方 SkillHub / WorkBuddy（蓝V认证企业命名空间：dayanqianji）
skillhub install dayan-humanize-pro --namespace dayanqianji
skillhub install dayan-business-html --namespace dayanqianji
skillhub install dayan-bid-scoring-loop --namespace dayanqianji
skillhub install dayan-contract-4way-audit --namespace dayanqianji

# 方式 2B：在腾讯 WorkBuddy / CodeBuddy 客户端内一键挂载「大衍千机 27 个专家和专家团」插件源
/plugin marketplace add https://github.com/Kosmoray/dayan-enterprise-ai-skills

# 方式 2C：装入字节跳动「豆包工作（doubao.com/chat/skills）」
# 下载 v1.6.0 的豆包工作增量包，解压后选取单个技能 ZIP 上传

# 方式 3：克隆仓库并安装到本地（支持 Claude / Codex / WorkBuddy）
git clone https://github.com/Kosmoray/dayan-enterprise-ai-skills.git
cd dayan-enterprise-ai-skills && python3 installers/install_skills.py --agent workbuddy
```

---

## 🛠️ 开箱即跑：内置 14 个零依赖 Python 命令行急救神器（无需 API Key！）

除了 **168 枚**挂载进智能体的深度 `SKILL.md` 专家系统与 **27 个 WorkBuddy 专家和专家团**，本仓库在 [`scripts/`](./scripts/) 中内置了 **14 个纯标准库、零第三方依赖、离线毫秒级响应的 Python CLI 武器**（4 把通用高管武器 + 10 个行业测算工具，均支持本地直跑或 `uvx` 免克隆调用）：

```bash
# 1️⃣ 【乙方法务保命】1秒扫描合同里的「背靠背付款/无限连带赔偿/源码归甲方/默认不验收」等致命霸王条款
python3 scripts/dayan_contract_quickscan.py examples/sample_b2b_contract.md

# 2️⃣ 【外发净稿门禁】1秒测出中文「AI 塑料味指数（0-100分）」并拦截未删干净的演讲/内部制作备注
python3 scripts/dayan_humanize_lint.py examples/sample_ai_slop.md --fail-under 50

# 3️⃣ 【老板拍板呈现】1秒把任意 Markdown 报告编译成 #1B365D 深蓝政商风单文件 HTML 高管看板（微信点开即看）
python3 scripts/dayan_html_compiler.py examples/sample_ai_slop.md /tmp/executive_brief.html

# 4️⃣ 【痛点秒搜武器】输入任意经营卡点词（如：液冷 / 变压器 / 泳池 / 重卡 / 宠物 / 军工），从 168 枚武器秒搜
python3 scripts/dayan_skill_finder.py 液冷

# 行业离线测算示例
python3 scripts/industry/liquid_cooling_uqd_calc.py --demo     # AI算力机柜液冷流量、UQD快接头压降Cv与露点防凝露精算
python3 scripts/industry/pool_pump_filter_roi_calc.py --demo   # 欧美变频泳池泵DOE节能回本与SPA替换滤芯尺寸毛利核验
python3 scripts/industry/transformer_bom_quote_guard.py --demo # 出海变压器硅钢铜重联动与IEC/IEEE超耗罚金TOC精算
python3 scripts/industry/ev_station_tco_calc.py --demo         # 电动重卡超充站国网容量vs需量电费临界点与TCO回本测算
python3 scripts/industry/vet_dose_compliance_check.py --demo   # 宠物专科医院犬猫BSA体表面积剂量红线与人药兽用合规核查
python3 scripts/industry/gjb_kit_shortage_audit.py --demo      # 航空军工多工序特种外协齐套与断网不出域大模型显存精算
python3 scripts/industry/gb7718_oem_quote_guard.py --demo      # 川调食品GB7718-2025防职业打假扫描与炒制损耗三档核价
python3 scripts/industry/cis_export_doc_checker.py --demo      # 二手车工程机械中亚俄语出口17位VIN模11校验与SMGS核单
python3 scripts/industry/ship_cii_drydock_calc.py --demo
python3 scripts/industry/semi_fab_coa_yield_calc.py --demo
```

---

## 🏆 必装 Top 12 镇店重武器（90% 的人装完当天就回本）

| 技能 Slug | 名称 | 一句话看清它帮你干什么狠活 |
| --- | --- | --- |
| [`dayan-humanize-pro`](./skills/dayan-humanize-pro) | **文章去AI味与中文人话精修大师** | 按五大病灶清洗赋能/抓手/排比三连/破折号滥用，生成→换脑挑刺→净稿三段溶图 |
| [`dayan-business-html`](./skills/dayan-business-html) | **深蓝政商风HTML高管汇报看板** | 把万字长文压成 `#1B365D` 深蓝印刷感单文件网页，发微信点开即看即拍板 |
| [`dayan-svg-diagram`](./skills/dayan-svg-diagram) | **商务印刷风手算SVG架构流程图** | 先判该不该画图，再精确手算坐标输出零重叠单文件 `.svg`，告别 Mermaid 挤字 |
| [`dayan-slide-deck`](./skills/dayan-slide-deck) | **去模板味高管演示PPT与16:9架构师** | 画面与讲稿物理分离、一页一结论契约表，输出无塑料感 16:9 演示稿 |
| [`dayan-bid-scoring-loop`](./skills/dayan-bid-scoring-loop) | **高分投标技术方案写审改闭环系统** | 废标红绿灯自检 + 写手出稿 + **只读独立评委模拟打分找扣分项**多轮收敛 |
| [`dayan-contract-4way-audit`](./skills/dayan-contract-4way-audit) | **商业合同与报价单四视角审查官** | 交付、财务、法务、销售四双眼睛并行挑刺，输出绿黄红黑定级与逐句替换文本 |
| [`dayan-rag-guardrail-kb`](./skills/dayan-rag-guardrail-kb) | **兜错型企业知识库与RAG架构官** | 权限预过滤 + 权威版签字 + 超期硬熔断 + 原文模糊接地四态兜错，专治胡编报价 |
| [`dayan-org-ai-ct`](./skills/dayan-org-ai-ct) | **企业AI组织体检CT与流程规划官** | 从老板救火地图、跨部门断点与老师傅隐性手艺筛出 3 条 30 天见效 MVP 流程 |
| [`dayan-private-board`](./skills/dayan-private-board) | **创始人私董会六幕深度对话剧场** | 1 位私董官 + 4 位实战背景幕僚，一幕一停严禁鸡汤建议，照见关键决策真盲区 |
| [`dayan-rank-reducer`](./skills/dayan-rank-reducer) | **商业与产品本质降秩引擎** | 七步递归下沉 + Deutsch 难以变更双测，砍掉十几个表象挖出最小独立驱动力 |
| [`dayan-code-adversary`](./skills/dayan-code-adversary) | **代码变更三眼对抗审查官** | 只读隔离态下用生产破坏者、半年后新人、安全戍边三副反方眼镜审 PR 挡线上事故 |
| [`dayan-ai-bible-ae86`](./skills/dayan-ai-bible-ae86) | **大衍AI工程圣经25律与AE86边界宪章** | 完整公开大衍内部开工前六律、多轮溶图、委托验收与大模型五大不消失物理边界 |

---

## 📚 全部 66 枚企业实战技能完整索引（点击展开）

<details open>
<summary><strong>第一梯队 · 镇店通用成稿、高管呈现与 AI 工程宪章组（#19–#36 · 18 枚）</strong></summary>

| # | Skill Slug | 技能名称 | 解决什么高频痛点 |
|---:|---|---|---|
| 19 | `dayan-humanize-pro` | **文章去AI味与中文人话精修大师** | 系统清洗中文文稿里的赋能、抓手、闭环、排比三连、万能过渡与空洞结尾等AI腔，按老板汇报、客户提案、公众号等场景校准真人语感。 |
| 20 | `dayan-business-html` | **深蓝政商风HTML高管汇报看板生成器** | 将长篇分析、阶段总结、商业方案或投研报告一键编译成深蓝印刷感、自带KPI卡片与响应式排版的单文件HTML高管汇报页。 |
| 21 | `dayan-svg-diagram` | **商务印刷风手算SVG架构与流程图引擎** | 先判该不该画图，再用深蓝印刷感色板与精确手算坐标生成零重叠、一图一结论的单文件SVG系统架构图、流程图、时序图与决策树。 |
| 22 | `dayan-slide-deck` | **去模板味高管演示PPT与16比9幻灯片架构师** | 先立视觉方向与每页唯一结论契约，再生成16:9高管级HTML演示文稿与可编辑PPTX逐页结构，彻底告别廉价套模板感。 |
| 23 | `dayan-bid-scoring-loop` | **高分投标技术方案写审改闭环系统** | 解析招标评分点与废标红线，采用写手生成与只读评审专家独立打分找扣分项的多轮收敛闭环，把技术标打磨到高水准。 |
| 24 | `dayan-contract-4way-audit` | **商业合同与报价单四视角并行风险审查官** | 从项目交付、财务现金流、法务合规与销售成交四个独立视角并行拆解合同草案或报价单，输出绿黄红黑四级结论与逐句修改建议。 |
| 25 | `dayan-rag-guardrail-kb` | **兜错型企业知识库与RAG架构设计官** | 拒绝胡编乱造的全知问答框！按安全预过滤、权威版签字、过期熔断、原文接地四态兜错与老板缺口看板五道关卡设计企业知识库。 |
| 26 | `dayan-org-ai-ct` | **企业AI组织体检CT与高价值流程规划官** | 从老板救火地图、跨部门信息断点与老师傅隐性经验三个切口给企业做AI就绪度CT体检，精准筛出3条30天见效的MVP落地流程。 |
| 27 | `dayan-multi-agent-arch` | **企业多智能体架构师（规则优先砍复杂度）** | 先按『规则>Pipeline>单Agent>总控专家>并发审查』五级阶梯砍掉伪多智能体复杂度，再输出任务、角色、状态与熔断四件套。 |
| 28 | `dayan-prompt-contract` | **企业级生产提示词与Agent任务合约工厂** | 拒绝堆砌玄学咒语！通过7格欠参诊断把模糊需求锻造成包含角色边界、工作流、质量验收线、注入防御与红线的生产级Prompt合约。 |
| 29 | `dayan-copywriting-pro` | **高转化官网落地页与B2B产品卖点翻译官** | 把自嗨的技术参数与空洞口号翻译成买单老板一眼看懂的经营账，生成首屏价值主张、痛点共鸣、证据链与低摩擦CTA六段式高转化页面文案。 |
| 30 | `dayan-geo-ai-seo` | **生成式引擎优化GEO与AI搜索获客实战官** | 针对豆包、DeepSeek、元宝、Kimi、ChatGPT与Perplexity的采购提问链路，诊断品牌为何不被推荐，设计站内结构化事实与第三方信源矩阵。 |
| 31 | `dayan-content-radar` | **深度商业公众号与爆款选题架构师** | 从目标买方真实痛点、搜索意图与竞品内容缺口切入，筛出高转化商业选题，直接产出带锋利判断、证据锚点与传播钩子的文章大纲及成稿。 |
| 32 | `dayan-private-board` | **创始人私董会深度对话与决策盲区剧场** | 由AI私董官控场、多位经历迥异的实战派幕僚轮番开放式发问，严禁好为人师给鸡汤建议，陪创始人一层层照见关键经营决策背后的真盲区。 |
| 33 | `dayan-exec-stress-test` | **重大商业决策六高管视角压力测试官** | 一键路由CFO财务、CMO市场、CCO留存、CDO数据、CISO安全与CAIO人工智能六大高管质疑官视角，对新预算、新产品或转型方案做残酷压测。 |
| 34 | `dayan-rank-reducer` | **商业与产品本质降秩引擎（第一性原理）** | 输入一个行业、竞品、复杂产品需求或棘手经营困局，用七步递归下沉与难以变更测试砍掉十几个表象，挖出真正支撑全局的最小独立力（秩）。 |
| 35 | `dayan-code-adversary` | **代码变更三眼对抗审查官（破坏者/新人/戍边）** | 打破写完代码自我感觉良好的同温层！在只读隔离态下用生产破坏者、半年后新人与安全戍边三副反方眼镜穿透PR与代码变更，输出阻断级证据链。 |
| 36 | `dayan-ai-bible-ae86` | **大衍AI工程方法论圣经25律与AE86边界宪章** | 完整公开成都大衍千机科技内部压箱底的《AI方法论圣经25律》与《AE86大模型物理上限工作线》，帮团队建立不踩坑的企业级AI工程纪律。 |

</details>

<details>
<summary><strong>第二梯队 · 中国老板管钱管人、十大实体行业与 AI 卡点救急组（#37–#66 · 30 枚）</strong></summary>

| # | Skill Slug | 技能名称 | 解决什么高频痛点 |
|---:|---|---|---|
| 37 | `dayan-cashflow-13week-radar` | **企业13周滚动现金流预警与断流压测器** | 告别账面有利润、账上没钱发工资！按经营流入、刚性兑付、弹性支出与极端回款延迟三档情景测算企业13周现金安全垫。 |
| 38 | `dayan-ar-collection-escalator` | **企业应收账款分级催收函与回款谈判参谋** | 专治客户拖欠尾款又怕撕破脸丢单！按逾期天数与客户合作价值输出四级递进催收微信话术、正式对账催款函及以货抵债/分期协议要点。 |
| 39 | `dayan-supplier-price-slasher` | **采购比价核价与供应商阳光议价拆解官** | 防止采购吃暗亏或只看总价被配件辅料宰一刀！按BOM成本结构反推供应商真实毛利空间，生成三家同口径比价矩阵与阳光降本谈判剧本。 |
| 40 | `dayan-zhuanjingtexin-grant` | **专精特新与高企申报材料自检及亮点提炼** | 别花几万找黑中介套烂模板被刷下！对照高新技术企业与专精特新硬指标自检知识产权、研发费占比与细分市场补短板证明逻辑。 |
| 41 | `dayan-loss-line-stop-bleed` | **亏损业务线与低效门店关停止损算账官** | 剔除沉没成本执念！算清继续硬撑3个月的失血账与立即关停/转租/缩编的一次性遣散止损账，帮老板果断砍掉失血包袱。 |
| 42 | `dayan-partner-equity-guard` | **创业合伙人股权分配与退出回购防坑参谋** | 专治五五平分僵局、兼职股东白拿干股与合伙人中途散伙带走股份！输出控制权结构、四年成熟期动态兑现与回购计价核心条款要点。 |
| 43 | `dayan-sales-commission-design` | **B2B销售提成方案与毛利防钻空子测算器** | 防止销售为拿提成乱打折亏毛利、签完单不管回款！按实收回款与真实毛利双挂钩测算底薪提成阶梯，跑完极端算账模拟再发制度。 |
| 44 | `dayan-exec-hiring-bs-detector` | **高管与核心岗面试追问及简历水分挤干器** | 专防花大价钱招来PPT大厂混子！把候选人简历里的『主导千万级增长/搭建体系』拆成颗粒度追问链与实战小考题，当场验出真本事。 |
| 45 | `dayan-weekly-report-truth` | **员工周报去水份与项目真实卡点穿透官** | 把满篇『持续推进、积极协调、赋能协同』的糊弄式周报一键榨干水分，揪出逾期未闭环事项、跨部门扯皮点与需要老板拍板的真雷区。 |
| 46 | `dayan-meeting-to-accountability` | **经营例会录音转责任人死线追踪表** | 治好『会上激动、会后不动』！从杂乱口语会议转写稿里精准剥离拍板决议、唯一责任人、交付物标准、截止日期与未决争议。 |
| 47 | `dayan-sop-extractor-master` | **销冠与老师傅隐性经验萃取转标准SOP工具** | 不怕销冠跳槽、老师傅退休断代！通过情景追问与成败对比访谈，把老手脑子里说不清的『凭手感经验』翻成新人照着就能干的SOP与AI提示词。 |
| 48 | `dayan-okr-kpi-decomposer` | **年度营收目标拆解到部门月度必赢战役** | 拒绝年底拍脑袋喊『明年翻倍』、开年各部门各干各的！按老客留存、客单升维与新客漏斗把年度营收倒推成市场、销售、交付每月的领先指标。 |
| 49 | `dayan-factory-8d-quality` | **制造业客诉8D根因分析与防呆整改报告** | 大客户退货索赔火烧眉毛！严禁拿『员工粗心加强培训』糊弄审核员，用5Why双路径（发生因+流出因）生成专业8D质量改善报告。 |
| 50 | `dayan-factory-bom-shortage` | **工厂生产排产齐套核查与急单插单评估** | 专治销售拍胸脯接急单、车间干到一半发现缺一颗螺丝停线！快速核算BOM物料齐套缺口、产线换模损耗与被挤占老订单延期代价。 |
| 51 | `dayan-construction-claim-audit` | **建筑工程变更签证索赔与结算核减防御** | 干工程最怕活干完了结算被审掉一层皮！对照施工合同与图纸变更记录，梳理设计变更、甲方原因窝工签证证据链及审计核减应对口径。 |
| 52 | `dayan-restaurant-chain-audit` | **餐饮茶饮连锁单店盈亏平衡与外卖毛利诊断** | 专治餐饮老板看堂食外卖挺热闹、月底一算账全给平台和房东打工！精算食材损耗、人工人效、美团抖音扣点补贴后的真实单店净现金流。 |
| 53 | `dayan-clinic-dental-retention` | **口腔医美与大健康机构到店转化复购诊断** | 获客投流贵如金，客户到店一次就流失等于白干！梳理留资预约到店率、面诊咨询卡点、术后康养随访SOP与合规口碑转介绍链路。 |
| 54 | `dayan-edu-institution-renewal` | **教培与企培机构续费率提升及家校沟通官** | 消课慢、续费难、老师不会做服务外化！把枯燥课堂表现转化为家长/企业HR看得见的成长证据卡、阶段复盘报告与自然续报沟通剧本。 |
| 55 | `dayan-freight-customs-checker` | **国际货代报关单证核对与异常船期预警** | 错一个HS编码或箱单毛重不一致就要改单罚钱耽误船期！交叉核对商业发票、装箱单、提单草件与信用证条款，生成客户异常沟通中英文函。 |
| 56 | `dayan-ecommerce-roi-teardown` | **电商与抖音投流ROI漏斗拆解及差评归因** | GMV几百万一看净利倒亏！穿透千川/直通车投流费、退货率、达人佣金与平台扣点算清真实净ROI，并从百条差评挖出改款与详情页命门。 |
| 57 | `dayan-private-domain-wecom-sop` | **企业微信高客单私域跟进培育SOP设计官** | 加了五千个客户微信却不敢发声、一发硬广就被删！为高客单B2B与高净值消费品设计黄金首周破冰、朋友圈人设日历与沉默老客激活剧本。 |
| 58 | `dayan-law-cpa-intake-triage` | **律所财税与咨询机构案源初筛报价打包官** | 解放合伙人每天免费陪聊两小时白嫖咨询！快速梳理当事人/企业主案情时间线、核心诉求证据缺口，设计付费首诊与阶梯代理服务包。 |
| 59 | `dayan-hotel-homestay-revpar` | **酒店民宿OTA评价治理与淡旺季收益诊断** | 携程美团评分掉0.1分流量掉三成！诊断入住率OCC与平均房价ADR平衡点、差评高情商公开回复模板，并补齐AI旅行规划推荐词条。 |
| 60 | `dayan-agri-food-trace-spec` | **食品加工与农牧特产企采礼盒提案生成器** | 好特产好食材别只会在农产品批发市场拼低价！针对中秋年货企业福利团购、商超定制与工会集采，一键生成高溢价企采分级礼盒方案。 |
| 61 | `dayan-dify-coze-troubleshooter` | **Dify与扣子企业工作流排错及生产加固指南** | Demo跑得欢、一上真实业务就超时报错吐乱码！系统排查Dify/Coze长工作流JSON解析崩溃、知识库召回偏题、并发限流与生产落地加固项。 |
| 62 | `dayan-feishu-bitable-architect` | **飞书多维表格轻量ERP与CRM业务底座设计官** | 传统软件几十万太笨重、普通Excel多人改就乱套！帮20-200人团队设计表结构关联、行列权限隔离、AI字段自动提取与飞书群催办流。 |
| 63 | `dayan-local-llm-hardware-sizer` | **企业私有化大模型部署显存硬件成本精算器** | 别听卖服务器厂商忽悠先砸五十万买显卡吃灰！按并发人数、上下文长度与量化精度精算DeepSeek/Qwen私有部署显存需求及云API三年总账对比。 |
| 64 | `dayan-ai-data-security-policy` | **企业员工使用AI防泄密制度与红线规范生成** | 员工偷偷把未公开报价单、买方清单和核心源码贴进免费公网AI怎么办？一键生成一页纸能落地的《企业AI安全使用分级制度与脱敏规范》。 |
| 65 | `dayan-legacy-excel-cleaner` | **企业历史混乱Excel台账合并清洗规则生成** | 专治十年老厂一物五名、合并单元格满天飞、日期金额格式全乱的历史脏表格！设计标准化主数据编码规则与零误删Python/公式清洗脚本。 |
| 66 | `dayan-ceo-ai-morning-brief` | **老板每日经营异常与行业AI情报晨报编译器** | 拒绝每天早上被几十个微信群和海量行业噪音淹没！把内部昨日关键经营异动与外部竞品/大宗原材料/政策真信号压成3分钟可读拍板晨报。 |

</details>

<details>
<summary><strong>第三梯队 · 企业 AI 全案首诊、算力券测算与 ERP/CRM/GEO 桥接组（#01–#18 · 18 枚）</strong></summary>

| # | Skill Slug | 技能名称 | 解决什么业务痛点 |
|---:|---|---|---|
| 01 | `dayan-enterprise-ai-triage` | **企业AI落地首诊与高价值场景筛选** | 协助企业经营者盘点拟推进的AI场景，优先识别高确定性业务切口，梳理数据条件、人工复核边界与30天试点安排。 |
| 02 | `dayan-role-training-architect` | **企业分岗位AI实战内训课纲设计** | 围绕企业真实岗位工作，按经营决策层、销售运营行政业务岗或客户主题沙龙，定制带实操练习与核对方法的培训方案。 |
| 03 | `dayan-chengdu-ai-vendor-selector` | **企业AI服务商五赛道选型对照参谋** | 协助企业分清工业视觉、标准客服SaaS、算力底座、通用考证培训与FDE全案共创五类服务方向，匹配合适合作伙伴。 |
| 04 | `dayan-sichuan-token-voucher-roi` | **算力券词元券与AI项目投入测算** | 结合企业实际单据量与岗位工时，算清模型调用与工程实施成本结构，评估优先推进场景的预期经营回报。 |
| 05 | `dayan-ai-seminar-anti-scam` | **企业采购AI课程与工具审慎核对单** | 在企业采购外部AI商业课程、获客软件或代运营服务前，协助逐项核对适用条件、交付物明细与阶段协作边界。 |
| 06 | `dayan-client-ai-salon-planner` | **企业对客AI主题分享与园区沙龙策划** | 协助链主企业、产业园区、商协会与B2B机构策划贴近业务实际的AI主题分享活动，兼顾专业深度与现场互动体验。 |
| 07 | `dayan-erp-crm-agent-bridge` | **知识库防幻觉与ERP/CRM衔接评估** | 针对企业自建扣子、Dify或本地知识库回答不准、难以衔接现有ERP/CRM的问题，输出源头治理与受控接入方案。 |
| 08 | `dayan-sales-visit-to-crm` | **销售沟通纪要转CRM跟进记录助手** | 将零散的客户拜访笔记、电话沟通要点整理为结构化CRM字段、需求成熟度梳理与下一步跟进待办。 |
| 09 | `dayan-order-change-erp-guard` | **制造与贸易订单变更跨部门核对单** | 当客户提出规格、交期、数量或包装变更时，自动梳理销售、工程、采购、生产与财务的协同确认清单。 |
| 10 | `dayan-kb-clean-data-governor` | **企业知识库文档入库前标准化梳理** | 在将企业制度、产品资料与常见问答导入知识库前，协助排查前后口径差异、补齐生效范围并优化段落结构。 |
| 11 | `dayan-oa-doc-cross-checker` | **商务方案合同与多表数据交叉校对** | 面向多页方案、采购协议、验收材料与预算表格，逐项核对主体全称、金额合计、时间节点与附件编号一致性。 |
| 12 | `dayan-fde-pilot-prd-writer` | **企业AI单流程试点需求梳理说明书** | 将业务部门的提效设想转化为业务人员与开发工程师都能清晰对齐的单流程试点方案、字段契约与验收清单。 |
| 13 | `dayan-geo-visibility-check` | **企业品牌AI搜索可见度GEO诊断助手** | 围绕真实买方选型提问，协助梳理企业在主流搜索与AI问答中的信息缺口、同名混淆情况与内容优化次序。 |
| 14 | `dayan-export-spec-sync` | **工贸出海产品参数与报价一致性核对** | 比对跨境商品页、英文产品画册与报价单中的尺寸、重量、装箱数量、材质表述与贸易条款，提前发现跨表差异。 |
| 15 | `dayan-chain-store-geo-auditor` | **连锁门店公开信息与AI找店核对助手** | 面向建材家居、零售餐饮与本地服务连锁品牌，逐店梳理地址门牌、营业状态、服务范围与联系电话的公开准确度。 |
| 16 | `dayan-cold-chain-batch-margin` | **生鲜冷链与批零采购批次毛利测算** | 综合批次进价、运输分拣费、可售期损耗、冷库仓储周转与渠道扣点，核算不同货源批次的真实净贡献。 |
| 17 | `dayan-b2b-export-inquiry-quoter` | **外贸B2B技术询盘梳理与报价准备单** | 快速梳理海外买家英文询盘邮件与技术规格要求，列出已明确参数、待澄清工况条件与阶梯报价核对要点。 |
| 18 | `dayan-tender-redline-audit` | **政企招投标资格条件与响应核对单** | 协助商务与售前团队梳理招标公告与采购文件，提取准入资格条件、实质性响应条款、评分结构与封标前检查项。 |

</details>

---

## 🗺️ Star 里程碑持续开源承诺（捧个人场，一起解锁！）

- [x] **首发解锁**：66 枚企业级 AI 实战技能 + 腾讯 SkillHub 蓝V全量上架 + 在线检索门户
- [ ] **⭐ 100 Stars 解锁**：开源《大衍商务风 HTML / PPT 净稿自动化验收器（Python Verifiers）》——自动拦截页面溢出、孤字换行与内部制作备注泄露
- [ ] **⭐ 500 Stars 解锁**：开源《中国企业脏乱差历史 Excel 台账零误删清洗与对账脚本包》
- [ ] **⭐ 1,000 Stars 解锁**：开源《一人公司（OPC）多总监分权协同与上下文续航工程骨架》

---

## 🤝 单点提效免费拿走；企业真刀真枪落地，找大衍千机！

开源单点技能能帮个人省下大量手工时间；但如果您的企业正卡在**「散乱脏资料建知识库总胡说、员工培训完三天打回原形、Dify/智能体接不进现有 ERP/CRM、或想做 B2B 企业 GEO 让豆包/DeepSeek/元宝搜行业词主动推荐贵司」**，别自己闷头烧几十万冤枉钱：

- 🏢 **公司主体**：**成都大衍千机科技有限公司**（四川成都高新区天府长岛数字文创园首家入驻 OPC）
- 🌐 **官网与真实交付案例**：[https://dayanqianji.com/](https://dayanqianji.com/) （[English Site](https://dayanqianji.com/en/)）
- 📋 **90 秒测清贵司哪条流程最值得先改**：[点击填写飞书 10 题初筛](https://my.feishu.cn/share/base/shrcnhBYBWWVOeFnmlggAhnGXE0)
- 📞 **创始人雷可扬直通电话 / 微信**：`18628016927`（添加请备注：**`GitHub`**，优先通道交流）

---

## 📈 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Kosmoray/dayan-enterprise-ai-skills&type=Date)](https://star-history.com/#Kosmoray/dayan-enterprise-ai-skills&Date)

## 📄 License

MIT License © 2026 **成都大衍千机科技有限公司 (Chengdu Dayan Qianji Technology Co., Ltd.)**
