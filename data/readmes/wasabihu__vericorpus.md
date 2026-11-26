# VeriCorpus (`wasabihu/vericorpus`) — 合规多语种参考语料、PDF 表格几何重建与双语检索基准

> **Trademark & Non-Affiliation Notice**: VeriCorpus is an independent community project built for XERJ and Elasticsearch-compatible engines. It is not affiliated with, sponsored by, or endorsed by The XERJ Authors.

> **Legal, Financial & Medical Disclaimer**: Not Legal, Investment, or Medical Advice — strictly for retrieval benchmarking and document verification research.

> [!IMPORTANT]
> **工程架构宪章与 AI 协作准则（Mandatory Engineering Charter）**：本仓库及配套纯文本语料仓的一切架构设计、语料准入、CI 门禁与公开评测均受以下三份宪章约束，修改或贡献前请先阅读：
> - **[`docs/ENGINEERING_PHILOSOPHY.md`](./docs/ENGINEERING_PHILOSOPHY.md)** — 四大第一性原理工程支柱（纯文本 `corpus-*` 分仓边界、零依赖标准库控制面与 `AGPL-3.0` 惰性隔离、`pathgate` 防御纵深、去 SaaS 化 `.contributors` CLA 与双层许可证门禁）
> - **[`AGENTS.md`](./AGENTS.md)** — AI 编码代理操作守则、本地 `:9200` 隔离红线与发版前 10 项强制自检清单
> - **[`.github/AI_CONTRIBUTIONS.md`](./.github/AI_CONTRIBUTIONS.md)** — 上游贡献三路决策树、第 1 行 `Provenance` 声明规范与零 `Co-Authored-By` AI 尾注铁律

**VeriCorpus** 是面向 [XERJ](https://github.com/xerj-org/xerj) 及 Elasticsearch 兼容检索引擎构建的**许可证严审语料工具包、可选坐标级 PDF 表格重建管线与零泄漏中英双语检索评测基准**（`Apache-2.0`）。核心控制面与双语检索适配器保持 **100% Python 标准库零第三方依赖（`dependencies = []`）**；公开 Python 包统一为 `import vericorpus`。

### 配套纯文本开源语料仓（Companion Pure-Text Corpus Repositories）

为便于直接通过 `xerj corpus add` 或任意全文检索器按单条法条/单篇试验表挂载（`language=None`，零构建脚本污染），我们同步拆分并维护两座纯文本配套仓库：

- **[`wasabihu/corpus-cn-statutes`](https://github.com/wasabihu/corpus-cn-statutes)**：依据《中华人民共和国著作权法》第五条第一项公有领域规则，将 29 部中国现行核心民商法、资本市场法规与企业会计准则按实质条文拆分为独立单条文件（100% 字节守恒校验），附完整 `MANIFEST.tsv` 清单。
- **[`wasabihu/corpus-clinical-trials`](https://github.com/wasabihu/corpus-clinical-trials)**：收录 NIH ClinicalTrials.gov v2 已公布结果干预试验表（`CC0-1.0`）与 Europe PMC 开放获取 JATS XML 临床试验三线表（`CC-BY-4.0`，完整保留真实作者、DOI/PMCID、许可 URI 与 XML→Markdown 转换声明），与 FDA DailyMed 药品说明书形成定量疗效与安全性互补。

### 配套纯洁净开源模型（Clean-Room Open Models on Hugging Face）

[![Hugging Face xerj-bilingual-fin-law-384](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-xerj--bilingual--fin--law--384-FFD21E?logoColor=black)](https://huggingface.co/wasabihu/xerj-bilingual-fin-law-384)
[![Hugging Face VeriCorpus-Reranker-0.6B](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-VeriCorpus--Reranker--0.6B-FFD21E?logoColor=black)](https://huggingface.co/wasabihu/VeriCorpus-Reranker-0.6B)

以下两款开源模型均基于 **100% 纯洁净许可语料**（`CC0-1.0` 中国法规、`SEC-Public-Filing`、NLM Public Domain / `CC-BY-4.0` 临床试验表，零 CNINFO/HKEX/私有数据混入，附 `CLEAN_ROOM_AUDIT.json` 与 `SHA256SUMS.txt`）训练并公开发布：

- **[`wasabihu/xerj-bilingual-fin-law-384`](https://huggingface.co/wasabihu/xerj-bilingual-fin-law-384)**（`MIT`）：基于 `intfloat/multilingual-e5-small` 的 384 维中英双语金融/法规/临床句向量模型（同时提供 FP32/FP16 ONNX 与原生 XERJ Candle `safetensors`），在 `xerj v1.0.0-rc.105` 原生 `hybrid` 混合检索中达到 `92.00%` R@1 / `100.00%` R@5（阿拉伯数字法条 `100%`、繁体查询 `97.06%`）。
- **[`wasabihu/VeriCorpus-Reranker-0.6B`](https://huggingface.co/wasabihu/VeriCorpus-Reranker-0.6B)**（`Apache-2.0`）：基于 `Qwen/Qwen3-Reranker-0.6B` 的双语金融/法规/临床口径校准重排器，240 组零泄漏净室盲测 `Top1 0.8625 → 1.0000`、`MRR 0.9188 → 1.0000`、`StrictCal 0.2083 → 0.9833`。

### 签名示例语料包（Signed Public Sample Pack）

- **[`examples/formd-sample-30d/`](./examples/formd-sample-30d/)**（`SEC-Public-Filing` + 分离式 `Ed25519` 签名）：收录连续 30 个自然日（`2026-10-06` 至 `2026-11-04`，21 个 SEC 申报日）内 **3,685 条**去重后的美国 SEC EDGAR 公开 Form D 首次申报记录（`3,577` 家唯一 CIK，仅实体级公开字段、零付费 API），每条附官方 `sec_edgar_url` 与原始 XML 的 `source_xml_sha256`，运行 `python3 examples/formd-sample-30d/verify_pack.py` 可离线单命令验签并校验完整性。

---

## 核心基础设施概览

在不修改底层检索引擎一行业务代码的前提下，VeriCorpus 提供五项核心开源组件：

1. **版权零纠纷合规语料准入与 `pathgate` 安全门禁（[`vericorpus.compliance`](./src/vericorpus/compliance.py)）**：严格按法定公有领域（`Public-Domain-CN-Law`）、宽松开源协议（`Apache-2.0` / `MIT` / `BSD`，强制锁定 40 位完整 Commit SHA）、开放获取学术许可（`CC-BY-4.0` / `CC0-1.0`）与美国联邦法定披露（`SEC-Public-Filing`）准入；明确拦截 `NOASSERTION`、`-NC` 非商用及无协议仓库，内置 `validate_slug`、`validate_rel_path` 与仅允许 `https://` 的 `_safe_urlopen`；A 股/港股/韩股披露原件仅以 `recipe` 配方分发并在 `.gitignore` 隔离的 `data/` 下本地处理，不随仓二次发布。
2. **可选几何坐标级 PDF 表格重建与纯标准库 HKEX CMap 修复器（[`vericorpus.pdf_table_fix`](./src/vericorpus/pdf_table_fix.py)）**：`normalize_cell` 与 `repair_hkex_cmap` 在纯标准库下运行，修复中英文表格折行丢小数点（`39.\n9 亿美元` → `39.9 亿美元`）、会计括号负数折行及港交所 PDF 日期语境下 `"月 → 尸"` CMap 错映（严格限定月份/日期上下文，绝不误伤 `"尸检"` 等正常医学法医词汇）；PDF 页面几何解析按需通过可选扩展 `vericorpus[pdf]`（`PyMuPDF`，`AGPL-3.0`）惰性加载，结合进程级崩溃隔离与长 PDF 页级面包屑标题（[`financial_10y.py`](./src/vericorpus/financial_10y.py)、[`ipo_prospectus.py`](./src/vericorpus/ipo_prospectus.py)），保障 200 页+ 招股书与年报全量分块不丢公司与年份上下文。
3. **纯净零依赖双语检索增强适配器（[`vericorpus.query_cn`](./src/vericorpus/query_cn.py)）**：100% Python 标准库实现简繁词表精准互通（区分 `"注册制→註冊制"` 与 `"制造业→製造業"`、补齐 `"病歷→病历"` / `"幹細胞→干细胞"`）、法条/期号与年份阿拉伯↔中文数字映射（支持 `"亿"` 级与 `"第X条之一"`）、千分位数值完整性保护、多标的对比查询 `should` 召回、陆港英会计口径对齐（如 `归母净利润` ↔ `归属于上市公司股东的净利润` ↔ `普通股股東應佔溢利`）及无中生有严格 0 命中拒答。
4. **多基准隔离实弹评测与分离签名套件（[`eval_hub.py`](./src/vericorpus/eval_hub.py) + [`eval_primary_weekly.py`](./src/vericorpus/eval_primary_weekly.py) + [`eval_e2e_rag.py`](./src/vericorpus/eval_e2e_rag.py) + [`scripts/build_hubpacks.py`](./scripts/build_hubpacks.py)）**：覆盖 24 题跨领域核心基准、32 题一级市场硬科技招股书 + 开源 AI 工程文档基准、30 题 AI/生物医学公开表格评测（100% 实核 `CC-BY-4.0` 作者署名与字符偏移），以及 33,575 分块混合库上的 60 题零泄漏端到端 RAG（`R / W / N`、`Net = R - 2W`、4,000 次配对 Bootstrap 95% CI）实测；打包脚本在归档外同步输出分离式 `<slug>-SHA256SUMS` 与 Ed25519 `<slug>-SHA256SUMS.sig` 支持先验签后解压。
5. **零泄漏 SEC 公开评测集构造器（[`vericorpus.cn_reader_pack`](./src/vericorpus/cn_reader_pack.py)）**：从 100% `SEC-Public-Filing` 语料（10 年期年报 + XBRL + 美股硬科技招股书）按 SHA-256 去重与 11 家保留标的防火墙导出带精确字符偏移真值的公开问答评测集（`eval_sec_ipo_heldout.json` 与 `dev_sec_qa_benchmark.json`）。

---

## 一、11 大已审计合规语料目录（8 个 `pack` + 3 个 `recipe`）

完整许可审查、依赖隔离说明与拒绝拦截记录见 [LICENSES_AUDIT.md](./LICENSES_AUDIT.md)。

| Slug | 领域 | 许可协议 | 分发模式 | 规模与收录内容 |
|---|---|---|---|---|
| [`cn-law-core`](./corpora/cn-law-core/manifest.json) | 法律合规 (`LAW`) | `Public-Domain-CN-Law`（《著作权法》第五条） | `pack` | 9 部中国现行核心法律全文（《民法典》总则/物权/合同/侵权责任四编、《公司法》2023、《证券法》、《劳动合同法》、《数据安全法》、《个人信息保护法》），319 分块（单条拆分版见 [`wasabihu/corpus-cn-statutes`](https://github.com/wasabihu/corpus-cn-statutes)） |
| [`cn-capital-market-law`](./corpora/cn-capital-market-law/manifest.json) | 资本市场与财税审计法规 (`LAW`) | `Public-Domain-CN-Law`（《著作权法》第五条） | `pack` | 20 部资本市场、财税审计与企业会计准则核心法规（《会计法》2024、《注册会计师法》2026、《审计法》及实施条例、《企业所得税法》、《增值税法》及实施条例、《期货和衍生品法》、《证券投资基金法》、《企业破产法》、财政部基本准则及会计处理规定 4 部、证监会信披/重组/收购/科创板/创业板注册制办法 5 部、最高法证券虚假陈述民事赔偿规定） |
| [`cn-github-stars`](./corpora/cn-github-stars/manifest.json) | 开源 AI 工程 (`AI`) | `Apache-2.0`（SPDX 逐仓核验） | `pack` | 锁定 40 位 Commit SHA 收录 5 个中文高星 Apache-2.0 项目核心中文文档（`infiniflow/ragflow`、`PaddlePaddle/PaddleOCR`、`hiyouga/LLaMA-Factory`、`chatchat-space/Langchain-Chatchat`、`datawhalechina/self-llm`），22 篇 / 191 分块 |
| [`cn-science-ccby`](./corpora/cn-science-ccby/manifest.json) | 科学医学论文 (`HEALTH`) | `CC-BY-4.0`（OpenAlex QA 实核） | `pack` | 40 篇 2020 年后高被引开放获取中文/双语论文与临床诊疗指南（POCT 传感、生物 3D 打印、肺癌 LDCT 指南、ALL 白血病诊疗指南、`PD-1/PD-L1` 等），保留完整作者、DOI 与期刊署名，61 分块 |
| [`ai-papers-ccby`](./corpora/ai-papers-ccby/manifest.json) | 前沿 AI 论文 (`AI`) | `CC-BY-4.0`（OpenAlex + arXiv/EPMC 实核） | `pack` | 50 篇 2022–2026 年高影响力开放获取 AI 论文（覆盖 RAG 与幻觉溯源、推理验证、LLM Agents、文档表格理解、AI4Science），严格拦截 `-NC`/`-ND`/非排他许可，40 篇提取评测结果 Markdown 表 |
| [`biomed-clinical-ccby`](./corpora/biomed-clinical-ccby/manifest.json) | 临床医学与试验数据 (`HEALTH`) | `CC-BY-4.0` / `CC0-1.0`（EPMC + CT.gov） | `pack` | Europe PMC / NCBI PMC JATS XML 临床全文表（`CC-BY-4.0`）+ ClinicalTrials.gov v2 已公布结果干预试验表（`CC0-1.0`）（独立纯文本配套仓见 [`wasabihu/corpus-clinical-trials`](https://github.com/wasabihu/corpus-clinical-trials)） |
| [`sec-10y-core`](./corpora/sec-10y-core/manifest.json) | 美股与中概近 10 年财报 (`FINANCE`) | `SEC-Public-Filing` | `pack` | 48 家美股核心科技/消费/金融/能源/医药龙头与中概 ADR（含 `SPCX`），共 442 份 SEC 原文 Markdown（`10-K`/`20-F`/`10-Q`/`424B4`）+ 48 份双语 XBRL 近 10 年财务总表 |
| [`sec-ipo-prospectus-pack`](./corpora/sec-ipo-prospectus-pack/manifest.json) | 美股硬科技招股书与上市后对照 (`FINANCE`) | `SEC-Public-Filing` | `pack` | 覆盖 Astera Labs (`ALAB`)、Credo (`CRDO`)、CoreWeave (`CRWV`)、Arm (`ARM`)、SpaceX (`SPCX`) 共 5 家一级市场硬科技 `424B4` 招股书、上市后年报/季报及 XBRL 对照（19 份 Markdown / 6,290 分块） |
| [`cn-hkus-disclosures`](./corpora/cn-hkus-disclosures/manifest.json) | 港美股与表格回归 (`FINANCE`) | `HKEX-Public-Disclosure` | `recipe` | 阿里巴巴 `9988.HK / BABA`（SEC 6-K HTML + 港交所 9 月季报 PDF）与腾讯控股 `0700.HK`（2026Q3 季报 PDF）；仅公开清洗配方，原件于 `data/` 本地隔离，161 分块 |
| [`cn-hk-financial-10y`](./corpora/cn-hk-financial-10y/manifest.json) | 中美港韩 92 家近 10 年财报 (`FINANCE`) | `Multi-Exchange-Public-Disclosure` | `recipe` | 统一编目 92 家代表性公司代码与披露目录（[companies_master.json](./corpora/cn-hk-financial-10y/companies_master.json)、[filing_catalog.json](./corpora/cn-hk-financial-10y/filing_catalog.json)）；原件与重建文本严格隔离于本地 `.gitignore` 的 `data/` |
| [`cn-hk-ipo-prospectus-recipe`](./corpora/cn-hk-ipo-prospectus-recipe/manifest.json) | 港股 18C 与科创板招股书配方 (`FINANCE`) | `Multi-Exchange-Public-Disclosure` | `recipe` | 覆盖港股 18C 4 家（`02533`、`09660`、`02513`、`02432`）与科创板 3 家（`688041`、`688498`、`688295`），仅分发清洗配方，不在公开仓分发原件 |

---

## 二、隔离实测基准结果汇总

全部评测均在隔离临时 `xerj v1.0.0-rc.101`（`macOS arm64 Apple M5`，`XERJ_DISABLE_QUERY_CACHE=1`）节点上跑通，未触碰任何持久化个人索引。

### 1. 24 题跨领域核心基准（5 类语料 / 7,022 分块）

完整逐题报告见 [BENCHMARK_REPORT.md](./BENCHMARK_REPORT.md) 与 [evals/latest_report.json](./evals/latest_report.json)。

| 评测指标 | Native XERJ (`multi_match` 基线) | VeriCorpus 双语检索适配器 |
|---|---:|---:|
| 20 题库内查询 **Top-1 精确命中率** | `16 / 20` (80.0%) | **`20 / 20` (100.0%)** |
| 20 题库内查询 **Top-3 命中率** | `17 / 20` (85.0%) | **`20 / 20` (100.0%)** |
| 4 题无中生有 **严格 0 误召拒答** | `0 / 4` (每次误召 15–319 条) | **`4 / 4` (100.0% 精准归零)** |

### 2. 32 题一级市场硬科技招股书 + 开源 AI 工程文档基准（64 份文档 / 15,194 分块）

完整逐题报告与误差分解见 [PRIMARY_EVAL_REPORT.md](./PRIMARY_EVAL_REPORT.md) 与 [evals/primary_market_and_weekly_eval_32.json](./evals/primary_market_and_weekly_eval_32.json)。

| 评测指标 | Native XERJ (`multi_match` 基线) | VeriCorpus 双语检索适配器 |
|---|---:|---:|
| 28 题域内真值 **Top-1 精确命中率** | `20 / 28` (71.4%) | **`25 / 28` (89.3%)** |
| 28 题域内真值 **Top-3 召回率** | `23 / 28` (82.1%) | **`28 / 28` (100.0%)** |
| 4 题无中生有 **严格 0 误召拒答** | `0 / 4` (每次误召 78–3,319 条) | **`4 / 4` (100.0% 精准归零)** |

### 3. 33,575 分块混合库端到端 RAG 基准（60 题零泄漏）

在单命名空间 `e2e-*`（208 份 100% `pack` 合规文件 / **33,575 chunks** / 建索 `9,214.5 ms`）上，通过标准 HTTP 验证接口（默认 `http://127.0.0.1:8000/api/verify`，可通过 `VERICORPUS_VERIFY_URL` 配置）测试三分支（`20` SEC 财报/XBRL 严格保留标的 + `10` ARM IPO + `15` 中国法规与资本市场新规 + `15` 硬拒答陷阱）。完整报告见 [E2E_BENCHMARK_REPORT.md](./E2E_BENCHMARK_REPORT.md) 与 [evals/e2e_latest_report.json](./evals/e2e_latest_report.json)。

| 评测分支 (Arm) | R / W / N | Net (`R - 2W`) | Score (`% Oracle`) [95% CI] | 证据块 `R@1 / R@3 / nDCG@3` | 检索 `p50 / p95` (ms) | 验证端 `p50 / p95` (ms) |
|---|---|---:|---:|---:|---:|---:|
| **Arm 1: Oracle Passage + Verifier** | `52 / 7 / 1` | **38** | `100.0` `[100.0, 100.0]` | `- / - / -` | `0.0 / 0.0` | `1891.25 / 3616.64` |
| **Arm 2: Native XERJ BM25 Top-3 + Verifier** | `24 / 11 / 25` | **2** | `5.3` `[-44.7, 48.5]` | `0.1778 / 0.2222 / 0.2029` | `113.67 / 306.94` | `2461.85 / 6421.15` |
| **Arm 3: VeriCorpus (`query_cn`) Top-3 + Verifier** | `49 / 6 / 5` | **37** | **`97.4`** `[64.1, 147.8]` | **`0.7778 / 0.9111 / 0.8561`** | `102.5 / 521.88` | `2502.2 / 5319.96` |

> Arm 3 相比 Arm 2 的 4,000 次配对 Bootstrap 净分差 `ΔNet = +35`（95% CI `[15.0, 55.0]`），文档级 `R@3 = 0.9778`，全部三分支引文字符偏移 100% 合法（`60/60`）。

### 4. PDF 表格几何重建与 HKEX CMap 修复实证对照

- **单元格小数点与会计负数修复**：修复跨行拆分小数点（如将 `39.\n9 亿美元` 修复为 `39.9 亿美元`、`(\n1,234.5)` 修复为 `(1,234.5)`）及行序倒置问题。
- **HKEX CMap 日期错字消除**：腾讯 `0700.HK` 港交所繁体季报 PDF 直出 `"月"` **341 处**、`"尸"` 残留 **0 处**；同时严格限定月份/日期语境，确保医学与法医文献中的 `"尸检"` 等词汇 100% 原样保留。
- **越疆机器人 (`02432.HK`) 7 份招股/年报定比对照**：`pdf_table_fix` 输出 **699 行标准管道表格** 与 **486 个顺序页码锚点（`<!-- page: p/N -->`）**，`0` 处乱码。
- **大规模财报重建实测**：A 股 241 份重建 **7,068** 张表格，港股 166 份重建 **2,311** 张表格，7 家港/科创板招股书重建 **341** 张表格（合计 **9,720** 张表格）。

---

## 三、快速上手与依赖分层安装

### 1. 纯标准库核心安装 vs. 可选 `[pdf]` 扩展（`AGPL-3.0` 隔离）

- **默认安装（100% Python 标准库零依赖，`Apache-2.0`）**：包含 `compliance`、`query_cn`、`fetchers`、`science_packs`、`cn_reader_pack`、评测脚本与 `pdf_table_fix` 纯文本修复函数（`normalize_cell`、`repair_hkex_cmap`），不安装任何第三方包：
  ```bash
  python3 -m venv .venv
  .venv/bin/pip install -e .
  ```
- **可选 PDF 坐标重建扩展（安装 `PyMuPDF >= 1.24.0`，遵循 `AGPL-3.0`）**：仅当您需要在本地从原始 PDF 提取并重建几何表格时按需安装：
  ```bash
  .venv/bin/pip install -e '.[pdf]'
  # 或发布包安装: pip install 'vericorpus[pdf]'
  ```

### 2. 配置 SEC EDGAR 合规请求头（访问 `sec.gov` 必读）

按照美国 SEC EDGAR 公平访问规范（Fair Access Policy），在运行任何访问 `sec.gov` / `data.sec.gov` 的实时抓取脚本前，**必须通过环境变量声明包含有效联系邮箱（`@`）的机构标识**（未设置或缺少邮箱时将立即抛出 `RuntimeError` 拒绝发包）：

```bash
export SEC_USER_AGENT="YourOrg contact@example.org"
```

### 3. 运行单元测试与发版安全门禁（无需安装任何第三方库）

```bash
# 1. 验证禁用 PyMuPDF 时的 100% 纯标准库导入隔离
PYTHONPATH=src python3 -c '
import sys
sys.modules["pymupdf"] = None
import vericorpus
from vericorpus import compliance, query_cn, pdf_table_fix
assert pdf_table_fix.normalize_cell("39.\n9 亿美元") == "39.9 亿美元"
assert pdf_table_fix.repair_hkex_cmap("本尸检报告") == "本尸检报告"
'

# 2. 运行全套确定性单元测试与负向控制用例
PYTHONPATH=src python3 -m unittest discover -s tests -v

# 3. 运行公开仓库合规、二进制/大文件与全量 Git 历史防泄漏审计
PYTHONPATH=src python3 scripts/audit_public_release.py
```

### 4. 运行隔离基准与数据管线

```bash
# 跑 24 题跨领域核心基准（自动合规校验 -> 隔离 XERJ 节点实测与 Ed25519 签名验证）
SEC_USER_AGENT="YourOrg contact@example.org" PYTHONPATH=src .venv/bin/python -m vericorpus.eval_hub

# 跑 32 题一级市场招股书 + 开源工程文档评测基准
PYTHONPATH=src .venv/bin/python -m vericorpus.eval_primary_weekly

# 跑 33,575 分块混合库 60 题端到端 RAG 评测
PYTHONPATH=src .venv/bin/python -m vericorpus.eval_e2e_rag

# 从 100% SEC-Public-Filing 语料导出零泄漏公开问答评测集（Held-out + Dev JSON）
PYTHONPATH=src python3 -m vericorpus.cn_reader_pack

# 构建带分离式 SHA256SUMS 与 Ed25519 .sig 的公开语料包
PYTHONPATH=src python3 scripts/build_hubpacks.py --corpora-dir corpora --raw-dir data/raw --out-dir data/hubpacks
```

---

## 四、许可证与合规声明

- **仓库代码与评测基准集**：遵循标准 [Apache License, Version 2.0](./LICENSE) 及 [NOTICE](./NOTICE) 声明；核心包 `vericorpus` 无任何第三方运行时依赖（`dependencies = []`），可选扩展 `vericorpus[pdf]` 按需引入 `PyMuPDF`（`AGPL-3.0`）。
- **语料包与开放获取署名**：各语料目录遵循 [LICENSES_AUDIT.md](./LICENSES_AUDIT.md) 所列法定公有领域、宽松开源或开放获取协议（`Public-Domain-CN-Law`、`Apache-2.0`、`CC-BY-4.0`、`CC0-1.0`、`SEC-Public-Filing`）；`evals/sci_ai_biomed_eval_30.json` 内全部 `CC-BY-4.0` 表格摘录均按第 3(a) 条完整保留真实作者、DOI/PMCID、标准许可链接及转换说明；`recipe` 目录仅提供清洗脚本与公开披露链接编目，不二次分发交易所受限原件。
- **免责声明（Disclaimer）**：本仓库及配套仓库（[`wasabihu/corpus-cn-statutes`](https://github.com/wasabihu/corpus-cn-statutes)、[`wasabihu/corpus-clinical-trials`](https://github.com/wasabihu/corpus-clinical-trials)）中的所有法规、财报与临床试验数据**仅供信息检索基准测试与文档核验技术研究使用，不构成任何法律意见、投资建议或医疗诊疗建议（Not Legal, Investment, or Medical Advice）**。
