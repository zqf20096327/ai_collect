# Agent Reach · 中文旅居检索

一个面向国内旅居、短住和租房调研的轻量 Python 工具。它把房租、天气、周边设施、B 站实地体验和 RSS 资讯整理成统一的命令行与 Python API。

项目只读取公开网页和公开接口，不要求提供平台账号、Cookie 或登录态。因此没有账号被封的风险；不过目标网站仍可能限流、弹出验证码或调整页面结构，部分来源只能尽力读取。

## 能做什么

| 场景 | 命令 | 默认来源 |
| --- | --- | --- |
| 查询房租 | `ch-travel rent` | 豆瓣租房小组、安居客、贝壳/链家 |
| 查看天气 | `ch-travel weather` | 中国天气网 7 天预报 |
| 查询周边设施 | `ch-travel facilities` | 大众点评（尽力读取） |
| 搜索实地体验 | `ch-travel bili` | bili-cli，失败时降级到 B 站公开搜索 API |
| 阅读网页 | `ch-travel read` | Jina Reader，失败时直连网页 |
| 阅读本地资讯 | `ch-travel feeds` | RSS / Atom |

所有功能均为只读。项目不会代替你联系房东、预订住宿，也不会验证房源真实性。

## 环境要求

- Python 3.10 或更高版本
- 能访问所选数据源的网络环境
- 可选：[bili-cli](https://github.com/public-clis/bilibili-cli)，用于更完整的 B 站搜索结果

## 安装

从 GitHub 安装：

```bash
git clone https://github.com/cpp285/agent-reach-ch-travel.git
cd agent-reach-ch-travel

python3 -m venv .venv
source .venv/bin/activate       # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -e .
```

如需使用 bili-cli：

```bash
pipx install bilibili-cli
```

没有安装 bili-cli 时，`ch-travel bili` 会自动尝试 B 站公开搜索 API。

## 快速开始

```bash
# 房租：城市、关键词、片区和指定来源
ch-travel rent 大理 -k 月租
ch-travel rent 成都 -k 一居室 -d 高新区
ch-travel rent 大理 -k 月租 -s 豆瓣租房小组

# 天气：支持内置城市名或中国天气网城市代码
ch-travel weather 大理
ch-travel weather 101290201

# 周边设施
ch-travel facilities 大理 菜市场

# B 站实地体验
ch-travel bili "大理旅居 房租" -n 10

# 网页与 RSS
ch-travel read "https://example.com/article"
ch-travel feeds "https://example.com/feed.xml"
```

查看全部参数：

```bash
ch-travel --help
ch-travel rent --help
```

## Python API

```python
from agent_reach_ch_travel import experience, facilities, rent, weather

rent_results = rent.search("大理", keyword="月租")
forecast = weather.forecast("大理")
nearby = facilities.search("大理", "菜市场")

try:
    videos = experience.bilibili_search("大理旅居 房租", limit=10)
except RuntimeError:
    videos = experience.bilibili_search_api("大理旅居 房租", limit=10)
```

`rent.search()` 和 `facilities.search()` 返回 `{来源名: 正文}` 字典。某个站点读取失败时，对应值以 `[失败]` 开头，其他来源仍会继续处理。

## 推荐调研流程

1. 先用 B 站搜索体验视频，了解目标城市常见旅居片区和大致价格。
2. 带上片区名称查询房租、天气和生活设施。
3. 用 RSS、当地政府网站或可信媒体补充交通、气象预警等时效信息。
4. 对房源价格、合同、押金和付款方式进行线下复核，不要仅凭搜索结果付款。

## 常用天气城市代码

| 城市 | 代码 | 城市 | 代码 | 城市 | 代码 |
| --- | --- | --- | --- | --- | --- |
| 大理 | `101290201` | 昆明 | `101290101` | 丽江 | `101291401` |
| 成都 | `101270101` | 三亚 | `101310201` | 北海 | `101301301` |
| 威海 | `101121301` | 海口 | `101310101` | 厦门 | `101230201` |
| 西双版纳 | `101291601` | 腾冲 | `101290503` | 桂林 | `101300501` |

如果城市不在内置表中，可直接传入中国天气网城市代码。

## 数据源与限制

- 贝壳、链家、安居客和大众点评的反爬策略较强，可能返回验证页或读取失败。
- Jina Reader 不可用时会降级为直连网页；直连结果是清洗后的纯文本，不一定保留原页面结构。
- B 站公开接口并非稳定的正式开放 API，可能调整或限流。
- 搜索结果具有时效性，租金、天气和营业信息应以来源页面及线下核验为准。

读取失败时，可以优先尝试豆瓣租房小组、当地政府网站、可信媒体或 B 站实地视频。

## 作为 Agent 技能使用

仓库中的 [`SKILL.md`](./SKILL.md) 定义了适合 AI Agent 的触发场景、检索顺序和失败降级策略。安装本包后，Agent 可以调用相同的 `ch-travel` 命令。

## 开发

```bash
python -m pip install -e ".[dev]"
pytest -q
```

项目测试默认不访问网络，主要覆盖 URL 生成和城市代码映射。

## 项目结构

```text
.
├── agent_reach_ch_travel/
│   ├── _http.py          # Jina Reader、直连降级和反爬页识别
│   ├── cli.py            # ch-travel 命令行入口
│   ├── experience.py     # B 站搜索与播客提示
│   ├── facilities.py     # 周边设施检索
│   ├── feeds.py          # RSS / Atom
│   ├── rent.py           # 房租检索
│   ├── sites.py          # 数据源 URL 与城市映射
│   ├── weather.py        # 天气预报
│   └── web.py            # 通用网页阅读
├── tests/
├── pyproject.toml
└── SKILL.md
```

## License

[MIT](./LICENSE)
