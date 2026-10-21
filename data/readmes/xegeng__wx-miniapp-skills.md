# wx-miniapp-skills

微信小程序(PC 端 WMPF)的 **AI 技能(SKILL)** 集合。一条工具链,三种用法:

**搭桥**(Frida 注入 / CDP) → **测功能**(用例、断言、回归) → **审安全**(路由全集、接口鉴权矩阵、越权)

基于「偏移自动提取 → Frida 注入 → CDP 代理 → MCP 工具链 → AI 渗透」完整工具链实战沉淀,
供支持 Skill 机制的 AI 助手(如 DeepSeek Harness / Claude 类 agent)直接加载复用。
三个技能共用同一条 CDP/MCP 链路,可分可合:只做回归测试就装前两个,只做安全审计就装搭桥 + 审计。

> ⚠️ **仅限对你本人拥有或已获明确授权的小程序做测试/安全评估。**
> 遵守《网络安全法》与微信平台条款;禁止破解、抓取、传播他人享有权利或隐私的数据。

## 包含的技能

| 技能 | 作用 | 关键文件 |
|---|---|---|
| `wx-miniapp-wmpf` | **工具链搭建**:WMPFDebugger(F12/CDP 桥接) + e0e1-wx + WMPFOffsetGen(偏移适配) + miniapp-cdp-mcp(MCP)。含环境检查、Node20+frida@16.6.6 约束、启动顺序、微信更新后取偏移、MCP 连接 | `skills/wx-miniapp-wmpf/SKILL.md` |
| `wx-miniapp-autotest` | **自动化测试执行**:用例设计/驱动/采样/断言/报告。Python 回归脚本(autotest.py)、断言表达式速查、AI 经 MCP 自主测试任务模板、官方方案(miniprogram-automator/Minium)速查 | `skills/wx-miniapp-autotest/SKILL.md` |
| `miniapp-audit-pipeline` | **接口面安全审计**:全量路由巡 → wxapkg 解包 → 接口全集 → **接口×4 态认证矩阵**(无凭据/真 id+空 token/真 id+假 token/随机 id)→ 凭据与混淆档位 → 分级定性。6 个可跑脚本(nav_sweep/auth_matrix/extract_apis/unpack/scan_secrets/mcp_batch) | `skills/miniapp-audit-pipeline/SKILL.md` |

架构链路:

```
微信小程序 ──Frida注入──▶ 62000 CDP 桥接 ──▶ MCP Server(:49999) ──▶ AI 助手(测试/渗透)
                              │                    │
                        DevTools(手动调试)    Python 回归脚本(CI)
```

三个技能按"搭桥 → 测 → 审"递进,共用同一条 CDP/MCP 链路:

```
wx-miniapp-wmpf      起桥、注入、连 MCP            (没有它,后面两个都跑不起来)
  ├─ wx-miniapp-autotest      功能侧:用例/断言/回归     (验证功能对不对)
  └─ miniapp-audit-pipeline   安全侧:接口全集/鉴权矩阵  (验证门有没有)
```

## 目录结构

```
wx-miniapp-skills/
├─ README.md
└─ skills/
   ├─ wx-miniapp-wmpf/
   │  └─ SKILL.md        # 环境搭建与工具链 SOP(十二节,含 MCP 工具链)
   ├─ wx-miniapp-autotest/
   │  └─ SKILL.md        # 自动化测试执行 SOP(用例/驱动/断言/报告)
   └─ miniapp-audit-pipeline/
      ├─ SKILL.md        # 接口面审计 SOP(六阶段/判据/安全边界)
      ├─ scripts/        # 6 个可跑脚本(通用化,无硬编码目标)
      └─ references/     # MCP 工具参数、13 类坑、认证矩阵配置模板
```

## 安装到你的 AI 环境

### DeepSeek Harness(DSH)

把 `skills/` 下三个目录复制到 harness 的技能目录(每个目录一个 `SKILL.md`):

```powershell
# 以 DSH 为例
$dst = "$HOME\.dsh\skills"
Copy-Item skills\wx-miniapp-wmpf    $dst\ -Recurse
Copy-Item skills\wx-miniapp-autotest $dst\ -Recurse
Copy-Item skills\miniapp-audit-pipeline $dst\ -Recurse
```

### Claude Code / 其他 Skill 机制

按各平台的 SKILL 规范，把 `SKILL.md`(含 YAML frontmatter:`name`/`description`)放入对应 skills 目录，
重启后即可被 agent 发现与调用(任务命中 description 时自动加载)。

## 运行环境要求(详见 wx-miniapp-wmpf)

- **Windows** + 桌面微信 4.x(PC 端,新版 WMPF 运行时)
- **Python 3.10+**(64 位)
- **Node.js 20 LTS**(关键!frida 二进制与 Node ABI 强绑定;22+ 报 `NODE_MODULE_VERSION`/ESM 不兼容)
- vendor frida 锁 **`16.6.6`**;MCP 依赖 **`mcp>=1.27.0,<2`**(mcp 2.x 把 FastMCP 改名 MCPServer)
- 端口:9421(debug)/ 62000(CDP)/ 49999(MCP)

## 免责声明

技能仅供**已授权**小程序的自动化测试与安全研究学习使用,使用者自行承担全部风险。
