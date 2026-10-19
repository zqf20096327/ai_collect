# AI Repo Atlas

> 42,853 个 GitHub AI 仓库的中立编目:一仓一张解读卡——机器筛得动、人看得懂、证据可回溯。

![repos](https://img.shields.io/badge/repos-42%2C853-blue) ![cards](https://img.shields.io/badge/deep_cards-593→8%2C000-orange) ![update](https://img.shields.io/badge/update-daily-brightgreen) ![license](https://img.shields.io/badge/data-CC_BY_4.0-lightgrey)

## 这是什么

GitHub 上的开源 AI 项目有几十万个,README 长短不一、真假混杂、中英文都有。本项目把它们变成一张张标准卡片,每张卡片回答选型四问:**它是什么、给谁用、怎么装、有什么限制**——并且每个判断都标注 README 原文行号,可以回链核查。

- **中立编目,不做评价**:README 里的营销语言("blazingly fast")不会渗透进卡片;只陈述可验证的事实。
- **宁可空,不可猜**:文本里没有的信息是 `null`,不是猜的("GPU-accelerated"这种没给数字的形容词不算硬件要求)。
- **元数据反作弊**:许可证以 GitHub 仓库实况为准,不信 README 徽章(挂 MIT 徽章但无 LICENSE 文件的项目会被如实标注)。

## 数字(2026-10-18)

| 指标 | 数 |
|---|---|
| 覆盖仓库池 | 42,853 |
| 已收 README | 42,763 |
| 深度解读卡(A 层) | 593(放量至 ~8,000 中) |
| 迷你卡(B 层长尾) | ~34,000(计划) |
| 更新频率 | 每日 |

## 三种用法

**人看**——每仓一张 markdown 卡,直接在 GitHub 浏览:
[`data/cards/o/openclaw__openclaw.md`](data/cards/o/openclaw__openclaw.md)

**程序用**——一行一仓的 JSONL 主表,带 [JSON Schema](data/schema/card.schema.json):
```bash
curl -L https://raw.githubusercontent.com/ai-repo-atlas/ai-repo-atlas/main/data/catalog.jsonl \
  | jq -c 'select(.filters.license_risk=="permissive" and .meta.stars>10000)'
```

**AI 助手用**——本仓根目录有 [`llms.txt`](llms.txt),LLM 客户端可按该标准发现和读取全部内容;数据也可直接喂给模型。

## 卡片速览

以 [n8n](data/cards/n/n8n-io__n8n.md) 为例,一行筛掉三类顾虑:

```
ai_role=ai-native · license_risk=dual · deploy=self-host · install_friction=low
```

七个硬约束枚举(`ai_role / license_risk / deploy / model_dep / hardware / install_friction / maturity`)的定义见 [DATASET.md](DATASET.md)。

## 数据从哪来、可信吗

| 环节 | 做法 |
|---|---|
| 发现 | GitHub 公开搜索四通道(topic / 组织 / 新仓 / 观察),非爬虫 |
| 解读 | LLM 从 README 提取客观事实,枚举判定由确定性规则合成(同一 README 跑两遍,枚举一致率 ≥98% 才放量) |
| 证据 | 每个判断带 README 行号与原文引句,可点击回源核查 |
| 刷新 | README 内容变更(sha 变化)自动触发重解读;项目活跃度按事件重算 |

## 许可

- 卡片与衍生数据:**CC BY 4.0**(署名本仓即可,含商用)。
- 元数据来自 GitHub 公开 API;行号级引文版权归原项目所有,卡片均附原仓库链接。
- 本仓**不收录 README 全文**,只有解读、短引文与回链。

## 更新机制

每日增量 commit;每周出 [周趋势](trends/);每月冻结快照见 [releases](../../releases)。变更历史见 [CHANGELOG.md](CHANGELOG.md)。

## Roadmap

- [x] A 层试批 593 张(2026-10-18)
- [ ] A 层放量至 ~8,000
- [ ] B 层迷你卡 34,000
- [ ] 静态站点(搜索/对比/替代页)
- [ ] MCP 服务(AI 助手直接查询本数据)
- [ ] HuggingFace 数据集镜像

## 引用

```bibtex
@dataset{ai_repo_atlas,
  title  = {AI Repo Atlas: a neutral catalog of 42k+ open-source AI repositories},
  author = {AI Repo Atlas},
  year   = {2026},
  url    = {https://github.com/ai-repo-atlas/ai-repo-atlas}
}
```
