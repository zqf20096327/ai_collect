# DFACM Calendar · 赛事日历

把算法赛、AI 竞赛和黑客松放进同一份日历。为 HydroOJ 提供公开赛事清单、组合筛选，以及跟随筛选条件的 ICS / RSS 订阅。

[在线体验](https://dfacm.website/calendar) · [安装说明](docs/installation.md) · [下载发布版](https://github.com/11suixing11/dfacm-calendar/releases) · [反馈问题](https://github.com/11suixing11/dfacm-calendar/issues)

## 功能

- **统一赛事入口**：ICPC、CCPC、Codeforces、AtCoder、AI 挑战赛和黑客松，按进行中、即将到来、日期待公布、已结束分组。
- **找到感兴趣的比赛**：按算法 / AI 方向、赛事类型、Vibe Coding / Agent 标签、平台、状态和关键词组合筛选；支持赛程、截止时间、最新收录和同币种奖金排序。
- **订阅自己的赛程**：页面、ICS 和 RSS 使用同一套筛选；ICS 包含赛前与报名截止提醒，RSS 也保留日期未公布的赛事。
- **手机与深色主题**：适配 Hydro 默认主题，游客可访问；浏览器脚本不可用时仍能阅读清单、搜索和下载订阅。
- **多源自动更新**：CF / AtCoder 独立抓取，可接入 CLIST 和配套 AI 采集服务；重复赛事合并元数据，单个来源失败时保留上次成功缓存。
- **公开 JSON**：`/calendar/data` 可供自己的机器人或其他应用低频读取。

![桌面赛事清单](docs/images/calendar-desktop.png)

<details>
<summary>查看手机深色主题与订阅界面</summary>

<img src="docs/images/calendar-mobile-dark.png" width="340" alt="手机深色主题的赛事清单">

![按当前筛选订阅赛程](docs/images/calendar-subscription.png)

</details>

截图来自 d&f 算法网，演示数据会随比赛与采集情况变化。

## 仓库内容

| 目录 | 用途 |
| --- | --- |
| [plugin-dfacm-calendar](plugin-dfacm-calendar/README.md) | Hydro 插件、前端、数据合并、筛选与订阅 |
| [plugin-dfacm-ai-contests](plugin-dfacm-ai-contests/README.md) | FastAPI / SQLite 采集服务，向统一日历提供本机只读 API |
| [docs/installation.md](docs/installation.md) | Hydro 注册、采集服务、环境变量与旧插件迁移 |
| [scripts/package.cjs](scripts/package.cjs) | 按固定清单生成生产安装包和 SHA256 文件 |

AI 采集组件只需作为后台服务启动。网站的导航、清单和订阅由一个 Hydro 日历插件提供。

## 数据源

| 方式 | 平台 / 赛事 | 配置 |
| --- | --- | --- |
| 手工公告 | ICPC、CCPC、省赛、邀请赛、校赛、蓝桥杯、天梯赛等 | 维护 `calendar.json` |
| 日历直接抓取 | Codeforces、AtCoder 社区数据 | 默认启用 |
| CLIST v4 | 牛客、洛谷、LeetCode、CodeChef | 可选，CLIST 用户名与 API Key |
| AI 采集后台 | DataFountain、天池、讯飞、Kaggle、DrivenData、Devpost、lablab.ai | 可选，Kaggle 需要自己的 token |
| AI 后台补充源 | Codeforces、LeetCode | 与日历来源去重合并 |

手工公告优先。赛事时间统一显示为北京时间；仅公布月份或截止时间时，页面与订阅保留已知信息。仓库中的 `calendar.json` 是手工示例，首次安装后请自行维护。

## 本地预览

需要 Node.js 22 或更高版本。预览使用手工示例，不启动 Hydro、数据库或网络采集。

```bash
git clone https://github.com/11suixing11/dfacm-calendar.git
cd dfacm-calendar/plugin-dfacm-calendar
npm ci --include=dev
npm run preview
```

打开 <http://127.0.0.1:4174/calendar>。生产部署请按 [安装说明](docs/installation.md) 配置；已验证 HydroOJ 5.0.7 与 `@hydrooj/ui-default` 4.58.5。

## 开发与验证

日历的依赖只用于测试和预览，生产直接使用仓库中的 TS 入口、模板和浏览器资源，无需重建前端。

```bash
# 在 plugin-dfacm-calendar 中
npm test

# 在 plugin-dfacm-ai-contests 中，Python 3.12+
python -m venv .venv
# Linux / macOS；Windows 使用 .venv\Scripts\python.exe
.venv/bin/python -m pip install -r requirements.lock
.venv/bin/python -m unittest discover -s tests -p 'test_*.py' -v

# 在仓库根目录，需要系统 tar
node scripts/package.cjs
```

测试使用本地样例，覆盖缓存故障隔离、去重、前后端筛选、旧链接迁移、订阅格式及后端 API。GitHub Actions 运行同一套检查。贡献方式见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

代码采用 [MIT License](LICENSE)，由 [d&f 算法网](https://dfacm.website)维护。赛事数据来自对应官方平台，CLIST 来源在页面与订阅中保留标注。
