# feishu-pm-kit

[![tests](https://github.com/Winfred1024/feishu-pm-kit/actions/workflows/tests.yml/badge.svg)](https://github.com/Winfred1024/feishu-pm-kit/actions/workflows/tests.yml)
[![License: MIT](https://img.shields.io/github/license/Winfred1024/feishu-pm-kit)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Last commit](https://img.shields.io/github/last-commit/Winfred1024/feishu-pm-kit)](https://github.com/Winfred1024/feishu-pm-kit/commits/main)

> 可快速部署到飞书的 **AI 项目经理 Agent + 项目管理系统** 部署套件。
> 一份共享引擎驱动多个团队实例,新团队"加一份 config + 跑一条 bootstrap"即可上线。

## 这是什么

把"**Claude Code 本体 + `CLAUDE.md` 操作手册 + `lark-cli` 飞书通道**"这一已验证的 AI 项目经理模式产品化:

- **Agent 项目经理**:在飞书业务群里监听消息、@责任人跟进、识别风险、发日报。Agent 本体是 Claude Code,在实例目录启动即加载该实例的 `CLAUDE.md`,化身那个团队的项目经理。
- **项目管理系统**:项目档案以 markdown frontmatter 为唯一事实源,脚本生成索引 + 健康看板,并做四项治理校验;可单向镜像到飞书多维表格供团队查看。

## 架构(共享引擎 + 多实例配置)

```
feishu-pm-kit/
├── engine/            # 共享引擎(唯一一份代码)
│   ├── lib/           # config / frontmatter / lark 调用封装
│   ├── gen_index.py   # 索引生成 + 四项治理校验
│   ├── feishu.py      # 飞书通道:poll / send / ws-start|stop|status
│   ├── bitable_sync.py# 项目台账单向同步到飞书多维表格(Base)
│   ├── bootstrap.py   # 一键部署:脚手架 / 拉成员 / 建表 / 渲染 CLAUDE.md
│   └── health.py      # WebSocket 健康检查 + 自动重启
├── templates/         # 实例脚手架(config.example / CLAUDE.md / 项目档案模板 …)
├── instances/         # 各团队实例(每个 = 一份 config.yaml + 数据目录;不入库)
├── tests/             # pytest 测试
└── docs/              # 设计文档(spec / plan)+ 部署清单
```

引擎默认作用于当前实例目录(`--instance PATH` 可覆盖);运行时状态(轮询断点、WS 事件流)写实例内 `.state/`。**全部团队差异进 `config.yaml`,引擎零硬编码。**

## 依赖

- Python 3.10+、`pyyaml`
- [`@larksuite/cli`](https://www.npmjs.com/package/@larksuite/cli)(飞书/Lark 官方 CLI,`npm i -g @larksuite/cli`),凭据用 `lark-cli config init`,多实例用 `--profile`

## 快速开始

```bash
git clone https://github.com/Winfred1024/feishu-pm-kit.git
cd feishu-pm-kit
python3 -m venv .venv && ./.venv/bin/pip install -r requirements.txt
./.venv/bin/python -m pytest -q          # 22 passed
```

部署一个新团队实例(详见 `docs/部署清单.md`):

```bash
# 阶段0(手动):飞书后台建应用+授权、拉机器人进群、lark-cli config init
# 阶段1(自动):
python3 -m engine.bootstrap --name team-alpha
# 阶段2:在实例目录启动 Claude Code
cd instances/team-alpha && claude
```

## 常用命令

```bash
python3 -m engine.gen_index    --instance instances/<名> [--check]   # 索引+校验
python3 -m engine.feishu       poll|send|ws-start --instance instances/<名>
python3 -m engine.bitable_sync --instance instances/<名>            # 推飞书多维表格
python3 -m engine.health       --instance instances/<名> [--restart]
```

## 四项治理校验

| 校验 | 内容 | 级别 |
|------|------|------|
| 必填/占位 | 恒必填字段齐全、非「待补充」;完结/中止项目财务字段齐 | ⚠️ WARN |
| 公式/一致性 | 毛利=收入−成本、差异=实收−应得、风险计数与表格一致、编号类型位匹配 | 🔴 ERROR |
| 新鲜度 | 进行中项目超阈值未更新 → 僵尸预警 | ⚠️ WARN |
| 命名/编号 | 编号格式、文件名匹配、无重复、无残留时间戳旧版 | 🔴 ERROR |

ERROR 必须修;WARN 是待补数据提示。明细见 `.governance/report.json`。

## 设计文档

- 设计 spec:`docs/specs/2026-05-21-feishu-pm-kit-design.md`
- 实现 plan:`docs/plans/2026-05-21-feishu-pm-kit.md`
- 部署清单:`docs/部署清单.md`

> 文档中的团队名/人名/项目名(示例团队A、张三、示例项目等)均为占位示例,非真实信息。

## 状态

- ✅ Phases 0–4:引擎全部模块 + 模板,TDD,22 测试通过
- ⏸️ Phase 5:真实实例迁移 + 多维表格联调(依赖飞书侧应用权限)

## License

MIT
