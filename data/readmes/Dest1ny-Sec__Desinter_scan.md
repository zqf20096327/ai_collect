<div align="center">

<img src="assets/hero.png" width="100%" alt="Desinter_scan — AI 自动化信息收集一揽子" />

</div>

<br/>

<div align="center">
  <img src="https://skillicons.dev/icons?i=python,claude,regex,docker,linux,git,nmap,sublime" alt="stacks" />
</div>




<div align="center">
  <img src="https://skillicons.dev/icons?i=python,claude,regex,docker,linux,git,nmap,sublime" alt="stacks" />
</div>

<br/>

<sub>多 Agent 并发 · Nuclei / Nmap / httpx 协同 · Claude 智能评分</sub>


> ⚠️ **仅供授权测试使用 · 未授权扫描可能违反法律法规 · 请确保所有目标已获得明确授权**

---

## 它不是 nmap 套壳，而是一个 **Claude 智能评分的多 Agent 侦察系统**

传统侦察工具是"哑管道" —— 跑扫描、拿数据、手动翻。Desinter_scan 不同：**22 个 collector 并发扫，Claude 按 6 维度智能评分，按攻击优先级排序输出**，告诉你"打哪"。

- **22 个** collector 并发扫（subfinder / nuclei / httpx / nmap / gau / waybackurls / assetfinder）
- Claude 按 **6 维度**（业务敏感度 / 攻击面 / 历史漏洞 / 暴露度 / 资产价值 / 攻击复杂度）智能评分
- 按**攻击优先级**排序输出 — Critical → High → Medium，告诉你"打哪"

# ⚡ interscan v2.0.1

> Multi-agent concurrent reconnaissance & intelligent asset scoring engine

**inter_scan** 是一个多 Agent 并发信息收集系统，将资产发现、服务探测、深度扫描三阶段流水线化，扫描完成后由 Claude AI 自动进行多维度价值评估，输出按攻击优先级排序的资产列表。

<p align="center">
  <a href="https://github.com/Dest1ny-Sec/Desinter_scan/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Dest1ny-Sec/Desinter_scan?style=flat-square&color=7B2CBF&labelColor=0d1117" alt="License" /></a>
  <a href="https://github.com/Dest1ny-Sec/Desinter_scan/stargazers"><img src="https://img.shields.io/github/stars/Dest1ny-Sec/Desinter_scan?style=flat-square&color=FF006E&labelColor=0d1117" alt="Stars" /></a>
  <a href="https://github.com/Dest1ny-Sec/Desinter_scan/actions"><img src="https://img.shields.io/github/actions/workflow/status/Dest1ny-Sec/Desinter_scan/ci.yml?style=flat-square&color=00D4AA&labelColor=0d1117&label=CI" alt="CI" /></a>
  <img src="https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white&labelColor=0d1117" alt="Python" />
  <img src="https://img.shields.io/badge/platform-macOS%20%7C%20Linux-lightgrey?style=flat-square&labelColor=0d1117" alt="Platform" />
</p>

<br/>

---

## 🎯 设计理念

传统的侦察工具是"哑管道" —— 你跑扫描，得到一堆数据，然后手动翻找有价值的东西。

**interscan 不同**：
1. **实时流式输出** — 不再是 `capture_output=True` 死等 5 分钟
2. **扫描完成 ≠ 工作完成** — Claude 自动读取结果，按 6 维度评分
3. **告诉你打哪** — 输出分层报告：Critical → High → Medium，带攻击路线

## 📦 安装

```bash
git clone https://github.com/Dest1ny-Sec/Desinter_scan.git
cd Desinter_scan
pip install -e .
```

### 外部工具（可选，按需安装）

| 工具 | 用途 | 安装 |
|------|------|------|
| `nuclei` | CVE 漏洞扫描 | `go install github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest` |
| `nmap` | 服务版本探测 | `brew install nmap` / `apt install nmap` |
| `subfinder` | 被动子域名 | `go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest` |
| `masscan` | 全端口扫描 | `brew install masscan` / `apt install masscan` |
| `dirsearch` | 目录爆破 | `pip install dirsearch` |
| `gowitness` | 网页截图 | `go install github.com/sensepost/gowitness@latest` |
| `whatweb` | CMS 指纹 | `brew install whatweb` / `apt install whatweb` |

缺少工具时自动跳过对应 collector，不影响其他步骤。

## 🚀 快速开始

```bash
# 环境检测
python3 run.py --check-tools

# 快速扫描（默认）— DNS 爆破 2000 条 + Top 端口 + 中字典
python3 run.py --target example.com

# 深度扫描 — DNS 爆破 8000 条 + 全端口 + 大字典
python3 run.py --target example.com --deep

# 全并发模式（跳过 Phase 依赖，所有 collector 同时跑）
python3 run.py --target example.com --flat

# 启用截图 + 查看进度
python3 run.py --target example.com --phase4
python3 run.py --target example.com --status

# 断点续扫
python3 run.py --target example.com --resume

# 只跑指定 collector
python3 run.py --target example.com --agents subdomain,port_scan,source_leak
```

## 🤖 Claude AI 集成

在 Claude Code 中直接对话使用：

```
/recon example.com        # 扫描 + 智能评分，一键搞定
/prioritize example.com   # 已有扫描结果，只做评分分析
```

Claude 会自动：
1. 读取扫描结果（优先读 vulnerable / leak / cloud 高价值资产）
2. 按 6 维度评分引擎打分
3. 输出五层优先级报告（★★★★★ → ★）

## 🏗 架构

```
run.py (并行引擎)
  ├─ Phase 1: 6 个 Collector 串行（资产发现，有依赖）
  │   enterprise → subdomain → dns_enum → asn_bgp → cdn_ip → cloud_assets
  ├─ Phase 2: 2 个 Collector 串行（服务探测）
  │   port_scan → network_space
  ├─ Phase 3: 14 个 Collector 全并发（深度扫描）
  │   http_probe / waf_detect / dir_scan / cms_finger /
  │   source_leak / js_api / crawler / mobile / github_leak /
  │   nuclei_scan / wayback_history / site_metadata / api_probe /
  │   legacy_hunter
  └─ Phase 4: 可选（screenshot）
         ↓
  SQLite 数据库（实时写入）
         ↓
  Claude 读取 → 智能评估 → 输出优先攻击面
```

### 23 个 Collector

| Phase | Collector | 功能 |
|-------|-----------|------|
| 1 | enterprise | 企业产权 WHOIS/ICP 备案 |
| 1 | subdomain | 14 源子域名 + DNS 爆破（智能根域识别） |
| 1 | dns_enum | 全 DNS 记录 + AXFR + SPF |
| 1 | asn_bgp | ASN → IP 段展开 |
| 1 | cdn_ip | CDN 检测 + IP 反查 + Favicon 哈希 |
| 1 | cloud_assets | crt.sh 云搜索 + CNAME 分析 + Bucket 探测 |
| 2 | port_scan | 全端口 + UDP + 敏感服务检测 |
| 2 | network_space | FOFA / Shodan / ZoomEye |
| 3 | http_probe | 批量 HTTP + Title + 聚类 |
| 3 | waf_detect | WAF/CDN 15+ 特征识别 |
| 3 | dir_scan | 7000+9638+45522 字典 + 平台专属路径 |
| 3 | cms_finger | WhatWeb + 30+ 内置指纹 |
| 3 | source_leak | .git/.svn/.env/备份/Swagger/Actuator/Druid |
| 3 | js_api | JS 密钥 + API 端点提取 |
| 3 | crawler | 爬虫 + 隐藏子域/外链 |
| 3 | mobile | ⭐ APK下载+解包+密钥提取 + iOS探测 + 小程序检测 |
| 3 | github_leak | GitHub dork 搜索密钥/配置 |
| 3 | nuclei_scan | Nuclei CVE 扫描 |
| 3 | wayback_history | Wayback Machine 历史 URL |
| 3 | site_metadata | robots.txt/sitemap/邮箱/第三方服务 |
| 3 | api_probe | GraphQL 内省 + API 版本探测 |
| 3 | legacy_hunter | 🆕 过期框架检测 (Struts/Axis/WebLogic) + 死端点复活 + EOL 版本 |
| 4 | screenshot | gowitness 批量截图 |

## 📊 实时告警

扫描中以下发现会**立即标记** ★：

| 告警 | 触发条件 |
|------|---------|
| ★ Redis 未授权 | 6379 PING → PONG |
| ★ Docker API 未授权 | /containers/json → 200 |
| ★ Elasticsearch 未授权 | /_cat/indices 可读 |
| ★ MongoDB 未授权 | 27017/27018 开放 |
| ★ 公开 S3 Bucket | Bucket URL → 200 |
| ★ .git 泄露 | /.git/HEAD → 200/403 |
| ★ GitHub 密钥泄露 | AKIA / secret_key / password |
| ★ JS 硬编码密钥 | AK/SK/Bucket/Token |

## 🧠 AI 评分引擎

扫描完成后 Claude 按以下维度评分：

| 维度 | 权重 | 满分标准 |
|------|------|---------|
| 服务风险 | 30% | Redis/Docker 未授权, 敏感端口 |
| 泄露严重度 | 25% | GitHub 密钥, .git 可恢复, 备份文件 |
| 云资产暴露 | 15% | 公开 S3, 受限 Bucket, 云函数 |
| CMS 漏洞潜力 | 15% | 已知 RCE CMS + 旧版本 |
| API/管理面 | 10% | Swagger+Actuator+Druid, 管理后台 |
| 关联度 | 5% | 直连 IP > CDN 后 > 同 C 段 |

输出五层报告：

```
★★★★★ Critical — 立即处置
★★★★  高危 — 优先深入
★★★   中危 — 重点排查
★★    低危 — 常规资产
★     信息 — 持续监控
```

## 📁 配置文件

复制 `config.yaml` 填入 API Key（不填也能跑，用免费数据源）：

```yaml
apis:
  fofa_email: ""
  fofa_key: ""
  shodan_key: ""
  zoomeye_key: ""
  ipinfo_token: ""    # 免费 50k/月
```

## 📊 报告导出

```bash
# HTML 报告（推荐）— 高价值资产表格 + 评分理由 + 一键导出 CSV
python3 -m core.reporter --target example.com --db output/example.com.db --mode html --open

# JSON 报告 — 完整数据
python3 -m core.reporter --target example.com --db output/example.com.db --mode json

# Markdown 报告
python3 -m core.reporter --target example.com --db output/example.com.db --mode markdown
```

> 扫描完成（或被 Ctrl+C 中断）后自动生成 HTML 报告到 `output/<target>_report.html`

## 🔧 高级用法

```bash
# 通过代理扫描
INTERSCAN_PROXY_ENABLE=1 INTERSCAN_PROXY_TYPE=socks5 python3 run.py --target example.com

# 纯文本模式（无 Rich 依赖）
INTERSCAN_NO_RICH=1 python3 run.py --target example.com

# 深度扫描
python3 run.py --target example.com --deep

# 跳过 Phase 3（只做资产发现 + 服务探测）
python3 run.py --target example.com --skip-phase3
```

## 📝 Changelog

### v1.0.1 (2026-05-30)

#### 🆕 新增
- **legacy_hunter** — 老旧服务猎人，系统性检测过期框架（Struts/Axis/WebLogic/JBoss）和死端点
- **mobile v2** — APK 下载+解包+硬编码密钥提取 + iTunes API iOS App 探测 + 小程序检测
- 子域爆破字典从通用垃圾词替换为 950 个中文高校高频词

#### 🔧 Bug 修复
- **subdomain**: `www.hust.edu.cn` 输入时错误枚举 `*.www.hust.edu.cn` → 修复为 `extract_root_domain()` 提取 `hust.edu.cn`
- **wayback_history**: 同上，查询 `*.www.xxx` 而非 `*.xxx`
- **port_scan**: nmap `--top-ports 3000` 被当成单个参数传递导致 `unrecognized option` → 拆分为 `["--top-ports", "3000"]`
- **port_scan**: `_parse_nmap` 解析 grepable 输出崩溃 (`Ports: 80` 被当 int 解析) → 重构解析器
- **nuclei_scan**: `-json` 标志在 nuclei v3.x 中不存在 → 改为 `-j`
- **10 个 collector**: 只读 `domain` 类型但子域存的是 `subdomain` → 统一添加 `subdomain` fallback
  - http_probe, dir_scan, nuclei_scan, source_leak, site_metadata, waf_detect, js_api, api_probe, cms_finger, crawler, mobile, cdn_ip, cloud_assets, dns_enum, screenshot

#### 📊 修复效果
```
修复前: 1 个子域, 0 wayback, 0 nuclei
修复后: 141 个子域, 5000 wayback URL, 201 nuclei 目标, 176 个存活 Web
```

### v1.0.0 (初始版本)
- 22 个 Collector 多阶段并发引擎
- Claude AI 6 维度智能评分
- SQLite 实时写入 + HTML 报告

## ⚠️ 免责声明

本工具仅供安全研究和授权测试使用。使用者需自行确保获得目标授权。作者不对任何未授权使用承担法律责任。
