# AlgoPilot —— 自驱动搜广推算法迭代智能组织

> **像自动驾驶一样,让算法迭代能力本身成为一台可以复用的引擎。**
> 人类编程 `program.md`(组织代码),智能组织在固定评测装置里自主迭代算法代码。
> 核心理念(v0.2):**端到端对齐最终交付**——离线棘轮负责走得快,
> 交付门禁负责走得对,上线门禁永远在人类手里。

灵感与直接参考:[karpathy/autoresearch](https://github.com/karpathy/autoresearch)
(630 行代码,AI agent 自主跑 LLM 训练实验循环)。AlgoPilot 把这套"棘轮循环 +
组织代码"范式移植到搜广推算法域,并升级为**可跨域的通用迭代引擎**:
搜/广/推三个业务域通过同一份 `domain.json` 契约接入,引擎一行不改。

autoresearch 有一个隐含的幸运:val_bpb 本身就是交付。搜广推没有——AUC 只是代理,
业务结果才是交付。所以 AlgoPilot 在离线棘轮之后加了**端到端交付门禁**
(会话仿真:模型自选曝光、按真实因果 pCTR 产生点击),并用**兑现率
(offline Δ / delivery Δ)**让组织看见"哪些离线提升真的兑现为业务结果"。

---

## 十分钟上手(零依赖,零 API key)

```bash
# 1. 跑测试(含组织全循环端到端,约 1.5 分钟)
python tests/run_all.py

# 2. 启动一次自驱动迭代(推荐域,mock 引擎,10 轮;中断后再跑同命令即断点续跑)
python -m pilot run --domain domains/rec --engine mock --max-experiments 10

# 3. 早上看晨报(唯一的"人类出口"):experiments/rec/morning_report.md
python -m pilot status --domain domains/rec   # 随时查看台账摘要
```

mock 引擎不是假数据:它是确定性的策略遍历器,会在 `domains/rec/mock_policy.json`
的菜单上真实地改代码、真跑评测、真过双门禁。参考输出:

```
[pilot] warmup 完成: auc=0.605644 std=0.00e+00 → 有效提升阈值 min_delta=0.001
[pilot] 交付基线: session_ctr=0.148750 (端到端仿真, seed 固定)
[pilot] #3 保留 ▲ auc 0.6056 → 0.6265  <feat-cross> | 交付 0.2128
[pilot] #4 保留 ▲ auc 0.6265 → 0.7031  <aggressive-lr> | 交付 0.2784
[pilot] #7 × 失败  <pos-weight> 护栏 val_logloss=0.3872 超上限 0.35
[pilot] #10 保留 ▲ auc 0.7031 → 0.7111  <more-epochs> | 交付 0.2791
[pilot] #11 ✗ 回退  <heat-boost> auc 0.7113 未超过 elite 0.7111+0.001
[pilot] 研究员停止:方向已遍历/主动举手
```

11 次实验,AUC 0.6056→0.7111,交付 CTR 0.1488→0.2791(**+87.6%**),零人工干预。
晨报里的**兑现率谱系**是这套体系最有价值的产出:特征交叉兑现率 **3.07**,
而"多训一倍轮数"只有 **0.078**——同样是离线保留事件,交付价值差 40 倍,
端到端对齐让组织看得见这件事,不再把力气花在兑现率 0.078 的方向上。

## 接真 LLM(DeepSeek / 智谱 GLM 等 OpenAI 兼容接口)

```bash
export LLM_API_KEY=sk-xxx          # 必填
export LLM_BASE_URL=https://api.deepseek.com   # 或 oneapi/智谱网关
export LLM_MODEL=deepseek-chat
python -m pilot run --domain domains/rec --engine llm --level L3
```

研究员/工程师两个角色走真模型(假设生成 + 代码改写,观察上下文携带
离线-交付对齐历史),评审员仍是纯代码——**铁面无私的部分永远不交给模型**。

## 五文件铁律(每个算法域的全部)

| 文件 | 角色 | 谁可以改 |
|---|---|---|
| `prepare.py` | 冻结装置:数据准备、数据指纹、**真实因果 pCTR(delivery 的 ground truth)** | 谁都不许改 |
| `model.py` | 算法本体,agent 唯一可编辑文件 | 只有 agent |
| `judge.py` | 冻结评测器:固定预算、单一主指标、护栏、`###JUDGE###` 协议 | 谁都不许改 |
| `delivery.py` | 冻结装置:**端到端交付仿真**(第二道门),`###DELIVERY###` 协议 | 谁都不许改 |
| `program.md` | 组织代码:角色、铁律、策略建议、停止条件 | 只有人类 |

## 三道关体系

```
离线棘轮(秒级,高吞吐)──► 交付门禁(端到端会话仿真)──► 上线门禁(永远在人类手里)
  AUC ≥ elite+Δ               交付不回退 + 生态护栏不破            定边界
```

- 第一道门防"变差":固定预算 + 单一主指标 + 护栏(logloss/耗时/数据指纹)一票否决;
- 第二道门防"假好":模型在 400 会话 × 300 候选货架的仿真里自选曝光,按
  `prepare.true_logit` 的真实因果 pCTR 产生点击——钻离线空子、制造马太效应的模型
  在这里现形(交付主指标不回退 + 曝光熵/冷启用户护栏不破,才算真正保留);
- 被交付门禁拦下的离线提升以 `rejected_by_delivery` 入账——**离线涨但交付跌,
  是组织最贵的教训,也是最值钱的记忆**。

## L4:多分支并行(分叉点结算,最优者合并)

```bash
python -m pilot run --domain domains/rec --engine mock --level L4 --max-experiments 10
```

批内多路 worker 并行实验(各自独立沙箱,批内方向互斥),批末按「分叉点结算、
最优者合并」裁决:每分支相对批首快照过双门禁,kept 中主指标最高者并入主线,
落选分支由 append-only 的 **merge 决策事件**记录(经验入台账,代码不进主线)。
单 worker 时行为退化为普通棘轮,与 L3 完全一致。

实测:并行路径上交付门禁自然拦下 `aggressive-lr`(离线 +0.0024、交付 CTR
甚至 +0.0103,但曝光熵 0.68→0.16 生态坍缩)——**单一指标都会放行,
生态护栏维度起了决定作用**。

## L5 前奏:program.md 受限自迭代(组织改进组织代码)

```bash
python -m pilot propose --domain domains/rec            # 从台账提炼修改提案(不生效)
python -m pilot approve --domain domains/rec            # 人类审批 → 备份生效 → 台账记录
```

台账里的教训(低兑现率方向、高频失败、交付拦截)会被提炼为 program.md 的修改
提案;红线校验是纯代码:铁律区(`IMMUTABLE:RULES`)禁触、anchor 白名单、
幂等不重复。生效后下一次 run 的组织就在新的组织代码下工作——
**组织代码本身进入台账,组织的进化有了自己的历史**。

## L3.5:真实数据接入(30 分钟约定)

```text
domains/rec/data_raw/
├── train.csv    # 列:label, num_0..num_k, cat_a, cat_b, cat_c(改列名即可,无其他要求)
└── val.csv
```

`prepare.py` 检测到 `data_raw/` 即走真实数据路径:类别域哈希成桶(基数不限)、
manifest 标记 `kind=real`、模型特征空间自适应;交付仿真对 real 数据显式降级告警
(真因果缺失,会话化真实回放在 roadmap)。

## 目录结构

```
AlgoPilot/
├── pilot/                  # 通用引擎(域无关 = 通用迭代能力)
│   ├── domain.py           #   DomainSpec / DeliverySpec 契约
│   ├── driver.py           #   RatchetDriver 主循环 + 双门禁
│   ├── org.py              #   智能组织:研究员(LLM)/工程师(LLM)/评审员(纯代码)
│   ├── memory.py           #   台账:experiments.jsonl 追加式唯一事实源 + 策略库/失败库
│   ├── llm.py              #   LLM 接缝:MockLLM(零依赖)/ OpenAICompatLLM
│   ├── prompts.py          #   真 LLM 的角色 prompt(含对齐意识)
│   ├── report.py           #   晨报生成(含端到端对齐节)
│   └── __main__.py         #   CLI: run / status / report
├── domains/
│   ├── rec/                # 推荐域(可跑):合成 CTR + 稀疏 LR + 交付仿真,10 KNOB
│   ├── search/             # 搜索域蓝本(NDCG@10,待建)
│   └── ads/                # 广告域蓝本(模拟 eCPM + 竞价仿真,待建)
├── configs/autonomy_levels.json   # L1-L4 权限配置
├── experiments/            # 运行产物:台账/晨报/elite 快照(gitignore)
├── tests/run_all.py        # 零依赖测试(57 项,含交付门禁与组织全循环)
└── docs/
    ├── 调研报告_自驱动算法迭代智能体.md   # 调研→设计映射(本项目的设计依据)
    ├── philosophy.md       # 端到端对齐 + 自动驾驶等级 L0-L5 + 智能组织理念
    ├── architecture.md     # 架构、双门禁与 autoresearch 对照
    └── roadmap.md          # L1→L5 演进路线
```

## 与 AgenticRec 1.0/2.0 的关系

AlgoPilot 不是 AgenticRec 3.0——它换了一个问题:**不再优化"单次推荐的元决策",
而是优化"算法版本之间的迭代过程"**。继承的资产:2.0 的"日志即真相"台账范式、
MockLLM/DeepSeek 双档、profile/契约式配置;补上的短板:1.0/2.0 的评测规模小、
全靠人工驱动。详见 `docs/调研报告_自驱动算法迭代智能体.md` §2.3。

## License

MIT
