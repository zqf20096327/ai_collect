<div align="center">

<img src="assets/camty-mark.png" width="180" alt="Camty"/>

# Camty

**红队交战工作台** —— 侦察 → 验证 → 利用 → 横向 → 报告 全链自动化

[English](README.en.md) | 简体中文

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Tests](https://img.shields.io/badge/tests-349%20passed-brightgreen)
![Adapters](https://img.shields.io/badge/adapters-42-orange)
![License](https://img.shields.io/badge/license-Apache%202.0-black)

</div>

---

## 是什么

Camty 是一套**可审计的红队交战工作台**：把一次渗透测试的全部动作——侦察测绘、漏洞验证、权限提升、横向移动、证据归档、报告生成——纳入同一条流水线，用范围护栏、审计哈希链和证据台账保证**每一步都合规、可回放、可交付**。

它同时是工具箱（41 个结构化适配器）、指挥台（多 agent 引擎 + Web 面板）和档案库（双图认知 + 血缘台账 + 三态报告）。

## 强势点

**1. 证据链优先的交战治理**
范围白名单 deny-by-default（DNS 解析防绕过）、每动作落 JSONL 审计哈希链（局部篡改必断链，可回放；配置 `CAMTY_AUDIT_KEY` 或保存锚点后可检测全量重算重写与尾部截断）、利用级动作必须引用台账中已验证发现（finding-ID 硬门控）、发现带血缘（`F-003 ← F-001` 一眼看清利用链从哪来）。

**2. 41 个结构化适配器**
外部工具（subfinder/httpx/nuclei/fscan）+ 自研武器（js-recon 前端测绘、inj-probe 多载体注入七变体、authz-probe 鉴权矩阵、code-audit 白盒审计、mail-code 验证码收件、osint-recon 目标画像、cve-intel CVE 情报、hashcrack GPU 破解）+ 内网全家桶（impacket 13 件 + 5 引擎横向移动）+ C2 三件套。工具输出自动进台账与资产图。

**3. 多 agent 引擎（双图认知）**
LLM 规划者读台账与资产覆盖度生成攻击链 todolist，N 个 worker 并行领意图执行并写回；资产图（真值库 + 覆盖度）与探索图（意图血缘）断点续跑；限流退避、连续失败自动降级确定性模式、人在环路随时转向。

**4. 对抗层**
HTTP 全流量 Chrome 指纹伪装（curl_cffi）、浏览器 stealth 三态（Turnstile 互斥实战校准）、注入七变体混淆 + chunked 传输、MITM 流量留痕代理（解密落盘、留痕先于响应、范围外 403 纵深）。

**5. 自研 C2 全链**
服务端 + 零依赖 C 植入体（AES/SHA/HMAC，KAT 对拍）、WinHTTP/schannel 加密信道、伪装 profile（URI/UA/Content-Type 可换）、beacon 回连抖动、无文件加载链（XOR 加密 → 内存节映射 → IAT 解析 → 重定位）真 E2E 验证。

**6. 交战产出即交付物**
HTML / docx / SRC 平台提交格式三态报告 + 复测对比；IM 推送（飞书/钉钉/企微/TG）；面板七页签（力导向资产覆盖图 / 流量逐条回放 / 攻击链 / 探索图 / 审批队列 / 人在环路转向）。

## 快速开始

```bash
git clone https://github.com/MiyanoShihoo/camty.git && cd camty
pip install -r requirements.txt                    # 或 pip install --target vendor <pkg>
pip install -r requirements-dev.txt                # 测试/CI 依赖（pytest + httpx2），与运行依赖分开安装
python -m camty keys set main --kind openai --base-url https://api.deepseek.com/v1     --api-key sk-xxx --model-decide deepseek-reasoner   # 配置 LLM（引擎/审批用）
python -m pytest tests/ -q                         # 349 项自检
```

支持 Python 3.10–3.13（CI 矩阵在 Ubuntu/Windows 实测）。

## 使用方式

**交战三步**：写授权配置 → 执行 → 出报告。

```yaml
# engagements/my-target.yaml —— 一次交战一份配置
name: my-target
pack: single-web            # 场景包（packs/ 下）：阶段链/攻击图声明
scope:
  domains: [target.com]     # 授权范围：白名单外一律拒绝
  min_interval_seconds: 0.3 # 速率护栏
auto_confirm: true          # operator 在线全权委托
```

```bash
# ① 确定性链：按场景包阶段推进（断点续跑）
python -m camty run engagements/my-target.yaml --phase probe
python -m camty auto engagements/my-target.yaml            # 全自动：全链 + 报告

# ② 多 agent 引擎：LLM 规划者自主探索（预算限步）
python -m camty engine engagements/my-target.yaml --agent --budget 30 --traffic

# ③ 产出
python -m camty report engagements/my-target.yaml --format html   # / docx / src
python -m camty audit engagements/my-target.yaml                 # 审计哈希链校验（输出 (count, head_hash) 锚点供外部存档）
```

**审计防篡改边界**：哈希链本身检测局部编辑（改/删/插任意一条即断链）；`save_state` 与报告生成会自动把 `(count, head_hash)` 锚点写入 `state.db` 用于检测尾部截断；设置环境变量 `CAMTY_AUDIT_KEY` 后条目追加 HMAC-SHA256，可检测"篡改全部记录并重算整条链"。无 key、无锚点时仅能检测局部编辑。

**面板**：`uvicorn camty.api.app:app --port 8090` → 仪表盘 / 台账 / 资产覆盖力导向图 / 攻击链 / 流量回放 / 探索图 / 审批队列，页头输入框随时注入转向指令（人在环路）。 面板 `/api/*` 需要 Bearer token：设置 `CAMTY_PANEL_TOKEN` 时用指定值，未设置时自动生成随机 token 并打印到 stderr。

**多目标并行**：`python -m camty multi a.yaml b.yaml c.yaml` —— 每交战一进程，汇总结录。

**交互式重放（Repeater）**：`python -m camty repeater engagements/my-target.yaml --port 8895` —— 手工验证向量时的提速器：持久会话（cookie 全程携带）、POST 前自动提取 csrf、向量批测一次打 N 条 payload 按指纹聚簇（只有异类簇需要人眼看）、`mode=browser` 走持久 stealth 浏览器（`render:true` 完整渲染，过反自动化客户端检测）。每个请求照过 scope 白名单 + 限速 + 审计哈希链三道闸。

```bash
# 单发：自动提取标题/表单/CSRF/错误标记，与该路径基线自动比对
curl -X POST localhost:8895/req -H "Content-Type: application/json" \
  -d '{"method":"GET","url":"https://target.example/"}'
# 批测：N 条 payload 一次打完，返回基线簇 + 异类簇
curl -X POST localhost:8895/vector -H "Content-Type: application/json" \
  -d '{"url":"https://target.example/","param":"q","payloads":["a","b","c"]}'
# POST 带 CSRF 自动跟随：auto_csrf 指向表单页即可
curl -X POST localhost:8895/req -H "Content-Type: application/json" \
  -d '{"method":"POST","url":"https://target.example/login","body":{"user":"x","pass":"y"},"auto_csrf":"https://target.example/login"}'
```

## 交战纪律（引擎强制，不靠自觉）

- 范围白名单外的目标一律拒绝（含 DNS 解析校验防"形似目标"）
- 利用级动作必须引用台账已验证发现，否则引擎拒绝执行
- 破坏性动作规则门 deny（删除类接口/SQL 破坏语句/危险 shell）
- 全动作审计留痕，哈希链 + seq + 可选 HMAC/锚点防篡改（无 key/锚点时仅能检测局部编辑；有 key/锚点可检测全量重算重写与尾部截断）；测试凭据/会话不进仓库（.gitignore 强制）

## 合规与免责声明

**本项目仅供已获明确书面授权的安全测试与研究使用。严禁用于任何未经授权的非法活动。因违反法律法规或未经授权测试所产生的一切法律后果与损失，均由使用者自行承担全部责任。本项目开发者不对任何滥用行为负责。**

## 目录结构

```
camty/
├── camty/                    # 主包
│   ├── cli.py                #   CLI 入口（run/auto/engine/multi/keys/report/audit）
│   ├── report.py             #   报告引擎（HTML/docx/SRC 提交格式/复测对比）
│   ├── storage.py            #   SQLite 断点续跑（进度/上下文/台账/探索图）
│   ├── tools.py              #   外部工具解析（工具目录 → 用户 Scripts → PATH）
│   ├── traffic.py            #   MITM 流量留痕代理（CA + 动态证书 + scope 纵深）
│   ├── mcpbridge.py          #   MCP 工具桥（外部 MCP 服务器 → 适配器）
│   ├── notify.py             #   IM 推送（飞书/钉钉/企微/TG/webhook）
│   ├── adapters/            #   41 个结构化适配器（工具集成层）
│   │   ├── 测绘:  osint-recon / subfinder / httpx / js-recon / secret-scan / dir-scan / cve-intel / scopesentry-sync
│   │   ├── 浏览器: browser-visit / browser-action（stealth 三态、A/B 双账号会话）
│   │   ├── 注入:  inj-probe / sqli-probe / sqli-exploit（七变体 evasion + chunked）
│   │   ├── 越权:  authz-probe（A/B 鉴权矩阵 + 强制浏览）
│   │   ├── 破解:  hashcrack（hashcat GPU，JWT/NTLM/Kerberoast/bcrypt 自动识别）
│   │   ├── AD:   fscan / smb-enum / samr-enum / ad-users / ad-computers / delegation-find /
│   │   │         kerberoast-check / asreproast-check / secretsdump / laps-read / gpp-password /
│   │   │         keylist / cred-test / lateral-move（5 引擎）/ machine-account / rbcd-set /
│   │   │         ticket-forgery / ntlmrelay
│   │   ├── C2:   c2-sessions / c2-task / c2-collect
│   │   └── 辅助:  code-audit（白盒）/ mail-code（IMAP 收码）/ evidence-search / report
│   ├── agent/                #   认知层
│   │   ├── assets.py         #     资产图（真值库：父子链自动推导 + 覆盖度）
│   │   ├── explore.py        #     探索图（goal/intent/fact 血缘 + 过程跟踪检索）
│   │   ├── engine.py         #     多 agent 引擎（planner → frontier → N worker 并行）
│   │   ├── planner.py        #     攻击树规划器 v2（并行批/priority/terminal/预算）
│   │   ├── orchestrator.py   #     交战级编排（阶段门控 + 断点 + 自动报告）
│   │   ├── runner.py         #     双 Runner（确定性链 / LLM Agent 循环）
│   │   └── state.py          #     Engagement + 血缘台账
│   ├── guardrail/            #   治理层
│   │   ├── scope.py          #     范围白名单（deny-by-default + DNS 校验 + 速率）
│   │   ├── audit.py          #     审计哈希链 + seq + 可选 HMAC/锚定（防篡改可回放）
│   │   ├── rules.py          #     破坏性动作规则门（deny 规则库）
│   │   ├── approval.py       #     三模式审批（交互/模型兜底/自动）
│   │   ├── preauth.py        #     预授权队列（批量放行 + 审计）
│   │   └── steer.py          #     人在环路转向（跑动中注入指令）
│   ├── modules/              #   纯逻辑武器（无外部依赖）
│   │   ├── js_recon.py       #     前端测绘（端点/路由/sourcemap/secret）
│   │   ├── inj_probe.py      #     多载体注入（GET/POST/JSON × 五类型 × 七变体）
│   │   ├── authz_probe.py    #     鉴权矩阵判定（相似度/ID 回显/会话提取）
│   │   ├── code_audit.py     #     白盒模式扫描（五语言 + 误报治理）
│   │   ├── cve_intel.py      #     CVE 情报（CIRCL 匹配 + CVSS 分级 + 版本过滤）
│   │   ├── waf.py            #     WAF 指纹（14 种被动响应头特征）
│   │   ├── http_fp.py        #     Chrome TLS/HTTP 指纹伪装（curl_cffi + urllib 回退）
│   │   └── secret_scan / dir_scan / sqli_probe / sqli_exploit
│   ├── llm/                  #   多 provider 路由（openai/responses/anthropic 协议
│   │   │                       + vault 加密 + 池化退避）
│   ├── api/                  #   FastAPI 面板（七页签 + 审批队列 + 引擎控制）
│   └── knowledge/            #   战术手册命中注入（"看到 X → 试 Y"）
├── c2/                       # 自研 C2
│   ├── server/               #   服务端（beacon 端点 + operator API + 伪装 profile）
│   ├── implant/              #   C 植入体源码（beacon.c/loader.c/crypto.c + 构建脚本 +
│   │                         #   无文件加载 E2E；产物本地构建不入库）
│   └── deploy/               #   部署套件（systemd/Caddyfile/env/deploy.sh/selfcheck.sh）
├── packs/                    # 场景包：single-web / ext-web / int-ad（阶段链 + 攻击图）
├── playbooks/                # 战术手册：web/（10+ 服务指纹应对）+ ad/（ASREP/Kerberoast/
│                             #   LAPS/委派/SMB relay）
├── tests/                    # 349 项测试（27 个套件：引擎/越权/对抗/MITM E2E/破解实测...）
├── scripts/                  # 辅助（build_beacon/pack_xor/smoke_browser/fetch_tools/build_dist）
├── docs/                     # design.md + c2-design.md（协议与路线）
├── engagements/              # 交战配置（demo 模板；真实交战数据被 .gitignore 隔离）
└── assets/                   # Logo（SVG 源 + 512/128 PNG）
```

## License

[Apache License 2.0](LICENSE)
