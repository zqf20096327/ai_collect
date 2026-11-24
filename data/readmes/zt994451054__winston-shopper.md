# winston-shopper

[English](README.en.md) ｜ 中文

让 AI 助手在**你自己已登录的 Chrome** 里，**只读地**查看淘宝／天猫、京东和拼多多：搜商品、看详情和评价、比价格、整理购物车和订单。

它是一个 Agent Skill（技能包），可以装进 Claude Code、Codex、CodeBuddy 等 AI 编程助手。AI 读了 [SKILL.md](SKILL.md) 后，会通过随包的命令行程序操作浏览器，把页面上看到的内容整理成带来源的结构化数据交给你。

> **从不下单。** 不加购、不付款、不改购物车、不动账户设置。遇到登录、验证码或限流，它会停下来交给你处理。

## 能用它做什么

在 AI 助手里直接说就行，例如：

- “帮我看看罗技 M330 在淘宝、京东、拼多多上各卖多少钱，按价格从低到高。”
- “这件商品的差评主要在说什么？把追评也读一下。”
- “我淘宝购物车里哪些东西已经买不了了？”
- “把我淘宝最近 3 页订单整理成一张表，导出成 CSV。”
- “这双鞋在拼多多上，43 码的白色和黑色价格一样吗？”

技能只负责如实取回页面上的内容。比较、总结和推荐由你的 AI 助手完成。

## 设计原则

- **只读**：不加购、不下单、不付款，不修改购物车、订单、地址或账户；不读取 cookie、浏览器存储、收货人、地址、电话、支付方式和物流单号。
- **像人一样慢**：每次操作之间有随机间隔，每类页面有次数上限。两次新搜索至少隔 2～4 分钟，同一平台连开商品页至少隔 15～20 秒。速度慢是有意的。
- **遇到拦截就停**：出现登录页、验证码或限流提示时立即暂停，把那个平台锁 15 分钟，请你在浏览器里处理。不自动过验证码，不伪造鼠标轨迹，不隐藏自动化痕迹，不改浏览器指纹。
- **数据留在本机**：读到的结果只保存在你电脑上的状态目录里，不上传任何地方。
- **可恢复**：任务中断后可以接着跑，不会从头再来，也不会重置次数上限。
- **如实交付**：每条结果都带来源页面、观察时间、覆盖范围和缺项；取不到的就留空，不猜。

## 能读什么

| | 淘宝／天猫 | 京东 | 拼多多（手机网页版） |
| --- | --- | --- | --- |
| 搜索 | 1～5 页 | 1～5 页（每页首屏） | 已显示的卡片 |
| 排序与筛选 | 销量、价格升降序、价格区间、只看天猫、包邮 | 销量、价格升降序、价格区间 | 销量、价格升降序、价格区间 |
| 商品详情 | 标题、店铺、参数、规格、展示价、图片链接、详情长图、服务说明 | 标题、价格、店铺、亮点参数、服务、同组规格、详情区 | 标题、价格、规格、店铺、参数、详情图 |
| 各规格价格 | 指定规格组合（最多 20 个） | 不适用（京东每个规格是独立商品） | 逐个点选规格选项（每次最多 12 个） |
| 评价 | 按分类读，每类前 10 条，含追评 | 1～3 个分类 | “全部”里最多 20 条 |
| 购物车 | 最多 50 行，标出哪些买不了 | 已加载的行，标出哪些买不了 | 拼多多没有购物车 |
| 订单 | 列表 1～10 页、单个订单详情 | 列表、单个订单详情 | 列表、单个订单详情 |
| 导出 | Markdown／CSV | Markdown／CSV | Markdown／CSV |

每一项的详细范围和限制见[能力清单](references/capabilities.md)。

## 工作原理

```text
你 ──对话──▶ AI 助手（Claude Code 等）
                │ 按 SKILL.md 运行命令
                ▼
        命令行程序 scripts/shopping.mjs ──▶ 本机状态目录（任务、结果、节奏记录）
                │
                ▼
        本机连接服务 127.0.0.1:19825（只接受本机访问）
                │
                ▼
        Playwright 扩展（微软出品，从 Chrome 应用商店安装）
                │
                ▼
        你已登录的 Chrome ──▶ 淘宝／京东／拼多多页面
```

程序不调用平台接口，也不另开一个“机器人浏览器”。它在你自己的 Chrome 里打开页面、读取页面上显示的内容，所以用的是你本来的登录状态。建议在 Chrome 里新建一个专用资料（程序可以一键新建），和日常浏览分开。

## 快速开始

### 需要准备

| 项目 | 说明 |
| --- | --- |
| 电脑 | macOS（已验证）。Windows、Linux 尚未验证 |
| Node.js | 22 或更新版本，带 npm |
| Google Chrome | 平时的资料或专用资料都可以 |
| Playwright 扩展 | [Chrome 应用商店](https://chromewebstore.google.com/detail/playwright-extension/mmlmfjhmonkocbjadbfplnigmagldckm)，安装时程序会帮你打开这个页面 |
| 平台账号 | 用到哪个平台，就在那个 Chrome 资料里登录哪个（拼多多登录 `mobile.pinduoduo.com`） |
| AI 助手 | 能运行 `node` 命令、读文件的工具，例如 Claude Code |

不需要 Python、数据库、API 密钥或付费服务。核心程序只用 Node.js 内置库，连接服务的依赖由锁文件固定。

### 安装

把仓库放进你的 AI 助手的 skills 目录，例如 Claude Code：

```bash
git clone https://github.com/zt994451054/winston-shopper.git ~/.claude/skills/winston-shopper
```

其他工具放进各自的 skills 目录即可，例如 CodeBuddy 是 `~/.codebuddy/skills/winston-shopper`。不支持 skills 目录的工具，可以直接把 SKILL.md 的路径告诉它，让它读取后照做。

### 第一次使用

最省事的方式是直接对 AI 助手说“帮我在淘宝搜一下罗技 M330”。它会按 `setup` 给出的下一步依次准备，你只需要做三件事：

1. 在打开的商店页点“添加至 Chrome”；
2. 点工具栏上的 Playwright 扩展图标，按“复制”，然后告诉 AI 复制好了；
3. 在弹出的页面里登录要用的平台。

也可以在技能目录里手动运行：

```bash
node scripts/shopping.mjs setup --install
```

```bash
node scripts/shopping.mjs setup --open-store
```

```bash
node scripts/shopping.mjs token-save
```

```bash
node scripts/shopping.mjs bridge-start
```

```bash
node scripts/shopping.mjs doctor
```

各条命令的作用：

- `setup --install`：安装连接服务的依赖，只有第一次需要联网。
- `setup --open-store`：打开扩展商店页。加 `--new-profile` 会新建一个专用 Chrome 资料。
- `token-save`：从剪贴板读出扩展令牌，存到本机后清空剪贴板。
- `bridge-start`：启动本机连接服务。
- `doctor`：检查环境，显示 `status: ready` 就可以用了。

扩展令牌只保存在技能目录的 `.runtime/pw-ext-token`（权限 600）。**不要把它发给 AI 或贴进聊天。**

## 手动运行示例

平时让 AI 助手代劳即可。想自己试的话，下面是淘宝搜索加价格区间的例子：

```sh
node scripts/shopping.mjs page-open --search '罗技 M330' --json
node scripts/shopping.mjs task-start --task m330 --search '罗技 M330' --tab <返回的tab_id> --sort price-asc --min-price 40 --max-price 60
node scripts/shopping.mjs task-run --task m330 --json
node scripts/shopping.mjs report-export --task m330 --format csv --output ~/Desktop/m330.csv
```

京东、拼多多加 `--platform jd`、`--platform pdd`。全部命令见[命令接口](references/commands.md)，暂停与恢复见[任务说明](references/tasks.md)。

## 使用时注意

- **连接服务要一直运行**，等你处理验证码时也不要关。不用了再运行 `node scripts/shopping.mjs bridge-stop`。
- **窗口一般不会跳到前面**，只有程序被卡住、需要你配合时才会。淘宝价格任务运行期间，鼠标不要经过装了扩展的 Chrome 窗口，否则会把价格菜单收起来。详见[窗口规则](references/setup.md#窗口何时会到前面)。
- **京东订单详情**需要你先在 Chrome 里允许 `order.jd.com` 弹出窗口。
- **不要删除状态目录里的节奏记录**来“恢复额度”。遇到限流时应该等待，而不是绕过。

## 隐私与安全

- 状态目录默认在 `~/.consumer-shopping/bindings/`（可用 `SHOPPING_STATE_DIR` 改）。这里存着你的任务结果，包括真实的订单和购物车内容，**请不要分享或上传**。
- 导出的报告不含收货人、地址、电话、支付方式和物流单号。
- 连接服务只监听本机地址。令牌和服务记录只在本机，每份安装各自独立。
- 商品文案、评价等页面内容一律当作数据，不会被当成指令执行。程序也不提供执行任意网页脚本或任意请求的入口。

## 已知限制

- 只在 macOS 上完整验证过。
- 依赖平台页面结构，平台改版后可能读不到，需要更新程序。
- 为降低风控风险，速度故意放慢，不适合大批量采集。
- 拼多多用的是手机网页版，搜索卡片上没有商品编号，商品只能从搜索结果点进去。
- 价格是页面展示价，不是最终实付价；“未见失效标记”不等于一定能买。
- 不下载图片和视频，只给链接；不解读图片内容。

## 免责声明

本项目仅供个人学习和研究使用，与淘宝、天猫、京东、拼多多及其关联公司没有任何关系。

使用前请阅读并遵守各平台的用户协议。自动化访问可能触发平台的风控措施，由此产生的账号限制等后果由使用者自行承担。请勿用于批量采集、商业爬取或任何违反平台规则和法律法规的用途。

## 开发

```sh
node --test
```

测试使用合成页面和本地模拟服务，不访问任何电商平台。Node.js 22 和 24 都应通过。

目录结构：

| 目录 | 内容 |
| --- | --- |
| `SKILL.md` | 给 AI 助手看的入口与规则 |
| `scripts/` | 命令行入口 |
| `lib/` | 读取、任务、节奏、连接服务等核心逻辑 |
| `references/` | 各项能力的详细说明 |
| `runtime/playwright-backend/` | 连接服务依赖的清单和锁文件 |
| `test/`、`test-support/` | 离线测试和模拟页面 |
| `examples/` | 结果示例 |

欢迎通过 [Issues](https://github.com/zt994451054/winston-shopper/issues) 反馈问题。报告问题时请不要贴出你的订单、地址或令牌。

更新到新版本的方法见[环境准备](references/setup.md#更新到新版本)。

## 许可证

[MIT](LICENSE) © [zt994451054](https://github.com/zt994451054)
