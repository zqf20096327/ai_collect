# 电气工程师 AI Copilot

> 一个本地运行的电气工程师智能体工作台：从**需求访谈**到**可直接用编程软件打开的 PLC 工程文件**，
> 覆盖梯形图编写 / 读懂 / 仿真、电气图纸理解与设计、元器件选型、HMI 画面设计、电气 BOM 与方案书输出。

对标「工控技术平台 / 玩工控」这类在线工控工具站，但**全部跑在本地**：知识库、项目文件、API Key 都不出网。

---

## 目录

- [核心能力](#核心能力)
- [快速开始](#快速开始)
- [11 个功能模块](#11-个功能模块)
- [PLC 工程文件直出（重点）](#plc-工程文件直出重点)
- [项目材料包交付物](#项目材料包交付物)
- [目录结构](#目录结构)
- [HTTP API](#http-api)
- [二次开发](#二次开发)
- [已知限制与诚实声明](#已知限制与诚实声明)
- [常见问题](#常见问题)

---

## 核心能力

| 能力 | 说明 |
|---|---|
| **AI 编写梯形图 → 直出工程文件** | 一句话描述需求，产出**能用 XDPPro / GX Works2 / 博途 / Pro7 / AutoShop / ISPSoft 打开或粘贴**的工程文件，不是文本说明 |
| **AI 读懂梯形图** | 上传梯形图截图，输出逐行逻辑解释、工作原理、潜在问题 |
| **梯形图模拟器** | 网页上直接点开关、看线圈/定时器/计数器状态，扫描周期模型仿真 |
| **AI 理解电气图** | 上传电气原理图照片，识别元件、分析连接关系、解读工作原理 |
| **AI 电气图设计** | 描述需求，自动生成电气原理图（DXF，AutoCAD 可开）+ 元件清单 |
| **智能选型** | PLC 点位/程序容量、伺服（含负载惯量校核）、断路器、接触器、开关电源计算 |
| **案例库** | 40 个实战案例（电机控制 / 定位 / 模拟量 / 通讯 / 报警 / 气动 / 联锁…），可一键载入模拟器 |
| **材料包交付** | 10 份工程文档（需求确认单 / 方案书 / 时序表 / IO 表 / 选型清单 / BOM / PLC 程序 / 接线图 / HMI 程序 / 调试清单） |
| **多品牌知识库** | 200+ 篇品牌知识（西门子 / 三菱 / 汇川 / 信捷 / 台达 / 欧姆龙 / 松下 / CODESYS / 雷赛 / 倍福 / 罗克韦尔 / 施耐德 / 基恩士）按品牌自动注入 |

---

## 快速开始

### 环境

- Windows 10/11
- Python 3.10+（实测 3.12）

### 启动

```bash
git clone https://github.com/clei32879-gif/electrical-copilot.git
cd electrical-copilot
pip install -r requirements.txt
python -m uvicorn app.main:app --host 127.0.0.1 --port 8321
```

浏览器打开 <http://127.0.0.1:8321>

Windows 下也可以直接双击：

- `启动.bat` — 自检服务是否在跑，没跑就拉起来，然后开浏览器
- `run.bat` — 装依赖 + 启动 + 开浏览器

想让**同一局域网里的手机/平板**也能访问，把启动参数改成 `--host 0.0.0.0`，然后用电脑的局域网 IP 访问
（例如 `http://192.168.1.100:8321`）。

### 配置模型

界面右上角「⚙ 模型设置」填入任意 **OpenAI 兼容**接口即可：

| 厂商 | base_url | 模型示例 |
|---|---|---|
| DeepSeek | `https://api.deepseek.com/v1` | `deepseek-chat` |
| 智谱 GLM | `https://open.bigmodel.cn/api/paas/v4` | `glm-4-plus` |
| Kimi | `https://api.moonshot.cn/v1` | `moonshot-v1-32k` |
| 通义千问 | `https://dashscope.aliyuncs.com/compatible-mode/v1` | `qwen-plus` |
| 本地 Ollama | `http://127.0.0.1:11434/v1` | `qwen2.5:14b` |

填 Key → 「测试连接」→ 保存。配置写入 `data/config.json`（已在 `.gitignore` 中，不会外泄）。

---

## 11 个功能模块

左侧导航是 11 个互相独立的功能页：

| # | 模块 | 做什么 |
|---|---|---|
| 1 | 🏠 首页 | 能力总览 + 各模块快捷入口 |
| 2 | 📁 项目管理 | 对话式需求访谈 → 生成 10 份材料包 → 预览/下载 |
| 3 | 🎮 梯形图模拟器 | 载入指令表或案例，实时仿真 X/Y/M/D/T/C 状态 |
| 4 | ✏️ AI 编写梯形图 | 中文描述 → IL → **品牌工程文件**（见下节） |
| 5 | 📖 AI 读懂梯形图 | 截图/指令表 → 逐行逻辑解释 + 问题诊断 |
| 6 | 🎓 PLC 学习助手 | 从零教学、练习出题、故障排查 |
| 7 | 🧮 智能选型 | PLC / 伺服 / 断路器 / 接触器 / 开关电源计算 |
| 8 | 👁 AI 视觉检测 | 工业缺陷检测方案（划痕/凹坑/裂纹/异物） |
| 9 | 📐 AI 理解电气图 | 电气原理图照片 → 元件识别 + 原理讲解 |
| 10 | 🏗 AI 电气图设计 | 中文需求 → 电气原理图 DXF + 元件清单 |
| 11 | 📚 案例库 | 40 个实战案例，按行业/品牌/关键词检索 |

---

## PLC 工程文件直出（重点）

这是本项目跟"只输出文档"的 AI 工具最大的区别：**产出文件能直接进编程软件**。

| 品牌 | 产物 | 导入方式 | 验证状态 |
|---|---|---|---|
| **信捷** XD/XC | `.xdp` 工程文件 | **双击直接用 XDPPro 打开** | ✅ 真机验证：打开 + `Ctrl+Shift+G` 编译 0 错误，梯形图连线和软元件注释完整 |
| **三菱** FX/Q | `_GXWorks2列表粘贴.txt` | GX Works2 列表视图整段粘贴 → `F4` 转换 | ✅ 真机验证（UI 自动化写入） |
| **三菱** FX5U/iQ-R | `_ST源.st` | GX Works3 ST 编辑器粘贴 | 官方 ST 语法 |
| **西门子** S7-1200/1500 | `_博途SCL源.scl` | 博途 → 外部源文件 → 添加 → 从源生成块 | 官方导入通道 |
| **西门子** S7-200 SMART | `_SMART_STL粘贴.txt` | STL 视图按 Network 粘贴 | 官方 STL 语法 |
| **松下** FP7/FP-X | `_Pro7_ST源.st` | Pro7 添加 ST 单元粘贴 | .pro 格式已逆向 |
| **汇川** H3U/H5U | `_AutoShop粘贴.txt` | 程序区 `Ctrl+A` → 粘贴 → `F4` 转换 | ✅ 真机验证 |
| **台达** DVP/AS | `_ISPSoft_IL粘贴.txt` | ISPSoft 新建 IL POU 粘贴 | 官方 IL 语法 |

各品牌用**自己的真实助记符**（西门子 `A/AN/S/R` + `TON` + `I0.0/Q0.0` 地址、松下 `ST/AN/OT/DT0`、
SMART `LD/A/=` + `TON T37` + `VW0`），不会输出"三菱化伪指令"。

### 信捷 .xdp 是怎么生成出来的

`.xdp` 是 ZIP 容器，内部是 UTF-8 的 XML。逆向要点（踩过的坑都写在代码注释里）：

1. **两个文件必须同步更新**：`plc1/ladnodes_instlist.xmd`（指令）与 `plc1/ladmodules.xmd`
2. `CompressLadNodes` 存指令，`CompressLines` 存**连线布局**——只写指令不写 Lines，梯形图会断线
3. `CompressLines` 行号 = LadNodes 行号 + 1，且注释行/GROUP 行**不占** Lines 行号
4. 连线起点列 = `max(触点列) + 1`，终点固定到第 10 列（指令框在第 11 列）
5. 没有前置触点的独立指令行必须补 `LD SM0`，否则 XDPPro 报"程序语法分析错误"
6. 软元件注释写进 `regcomment.xmd`，注意 `<CompressRegComments />` 是**自闭合标签**，正则替换要匹配自闭合形式

构造器：`app/automation/xinje_xdp2.py`，模板：`data/xinje_template_xd5.xdp`（XD5-32T4 骨架，
换成别的机型在 XDPPro 里改 PLC 型号即可，程序会保留）。

### 其他工程格式

- `07_电路接线图.dxf` — R12 ASCII DXF，手写生成（不依赖 ezdxf），AutoCAD / 浩辰 / 中望 / CAXA 均可打开
- `05_电气清单BOM.xlsx` — openpyxl 生成，含标题栏、表头样式、列宽自适应
- `01_方案书.docx` — python-docx 生成，Markdown 自动转 Word（标题/表格/列表/代码）

---

## 项目材料包交付物

「项目管理」走完访谈后，点「📦 生成材料包」，自动落盘到 `projects/电气项目_<名>_<id>/`：

| 文件 | 内容 |
|---|---|
| `00_需求确认单.md` | 确定项 / 待确认项 / 默认处理 + 结构化元数据 |
| `01_方案书.md` + `.docx` | 架构、控制方案、电气方案、风险 |
| `02_动作时序表.md` | 手动 / 自动 / 回零 / 报警时序 |
| `03_电气IO表.md` + `.csv` | DI/DO/AI/AO 全点位，CSV 可直接进 Excel |
| `04_选型清单.md` | 含选型计算式（如 `In ≥ Ie × 1.25`） |
| `05_电气清单BOM.md` + `.xlsx` | 物料表 + 预算 |
| `06_PLC程序_<品牌>.md` | 指令表 + ST/SCL 版本 + 导入步骤，并附品牌工程文件 |
| `07_电路接线图.md` + `.svg` + `.dxf` | 主回路 / 控制回路原理图 + 端子接线表 |
| `08_HMI触摸屏程序.md` | EBPro 通信设置 / 画面清单 / 控件表 / 变量映射 / 报警 |
| `09_调试检查清单.md` | 通电前 → IO → 手动 → 自动 → 安全 → 交付自检 |

**品牌识别策略**：访谈原文里明确提到的品牌，优先级高于 LLM 汇总的元数据——避免"品牌幻觉"
（用户说要信捷，模型却在元数据里写成三菱）。

---

## 目录结构

```
electrical-copilot/
├── run.bat / 启动.bat                # Windows 启动器
├── requirements.txt
├── app/
│   ├── main.py                       # FastAPI 入口 + 页面/项目/聊天/生成路由
│   ├── llm.py                        # OpenAI 兼容流式客户端（SSE）
│   ├── pipeline.py                   # 材料包生成管线
│   ├── knowledge.py                  # 知识库路由（按品牌/主题注入，带预算控制）
│   ├── prompt.py                     # 工程师 persona + 交付物规格
│   ├── store.py                      # SQLite 项目/会话存储
│   ├── exporters.py                  # CSV/SVG 提取、ZIP 打包、文件白名单
│   ├── config.py                     # 配置管理（data/config.json）
│   ├── modules/                      # ★ 11 个功能模块的后端
│   │   ├── simulator.py              #   梯形图仿真引擎（扫描周期模型）
│   │   ├── simulator_api.py          #   仿真接口
│   │   ├── ladder_gen_full.py        #   AI 编写梯形图 → 品牌工程文件
│   │   ├── ai_api.py                 #   6 个 AI 能力接口（tutor/vision/eread/edesign…）
│   │   ├── selection_api.py          #   智能选型计算
│   │   └── cases_api.py              #   40 个实战案例库
│   ├── automation/                   # ★ 工程文件直出
│   │   ├── xinje_xdp2.py             #   信捷 .xdp 构造器（核心）
│   │   ├── plc_text_export.py        #   全品牌程序文本导出（按品牌路由）
│   │   ├── dxf_export.py             #   R12 DXF 电气图生成
│   │   ├── office_export.py          #   xlsx / docx 导出
│   │   ├── gxw_builder.py            #   三菱 GX Works2 UI 自动化（可选）
│   │   └── huichuan_builder.py       #   汇川 AutoShop UI 自动化（可选）
│   └── static/                       # 前端（原生 JS，无构建步骤）
│       ├── index.html                #   11 模块导航 + 页面骨架
│       ├── style.css / modules.css   #   深色工业风主题
│       ├── modules.js                #   各功能模块前端逻辑
│       └── app.js                    #   项目管理 + 对话流
├── knowledge/                        # 200+ 篇知识库
│   ├── industrial/                   #   通用工程知识（PLC / HMI / EPLAN / 选型 / 视觉 / 规范）
│   ├── vendors/                      #   各品牌专章（西门子/三菱/欧姆龙/罗克韦尔/施耐德…）
│   ├── templates/                    #   交付物模板
│   └── real-*.md                     #   实战程序风格/范式
├── examples/                         # 示例对话产物（汇川）与样例工程
├── projects/                         # 生成的项目（含 2 个样例）
├── data/
│   ├── xinje_template.xdp            #   信捷 .xdp 模板（必须，勿删）
│   ├── xinje_template_xd5.xdp        #   XD5 专用模板
│   └── config.example.json           #   配置样例（复制为 config.json 使用）
└── tests/                            # 前端语法检查 + 生成的工程样本
```

---

## HTTP API

36 个接口，全部挂在 `/api` 下。核心几组：

```
# 项目管理
GET    /api/projects                    列出项目
POST   /api/projects                    新建项目
POST   /api/projects/{pid}/chat         对话（SSE 流式）
POST   /api/projects/{pid}/generate     生成材料包（SSE 流式，支持断点续传）
GET    /api/projects/{pid}/download     打包下载 ZIP

# AI 能力
POST   /api/modules/ladder-gen-full     中文描述 → 品牌工程文件 + 下载链接
POST   /api/modules/ladder-gen          中文描述 → 指令表
POST   /api/modules/ladder-read         梯形图 → 逻辑解释
POST   /api/modules/tutor               PLC 教学问答
POST   /api/modules/vision              视觉检测方案
POST   /api/modules/eread               电气图理解
POST   /api/modules/edesign             电气图设计
GET    /api/modules/download            下载生成的工程文件

# 梯形图仿真
POST   /api/simulator/load              载入指令表（编译成 Rung）
POST   /api/simulator/step /run         单步 / 连续运行
POST   /api/simulator/input /write      写 X 点 / 写任意软元件
GET    /api/simulator/state             读全部软元件状态

# 选型 & 案例
POST   /api/selection/plc|servo|breaker|contactor|power_supply
GET    /api/cases/list?brand=&industry=&keyword=
GET    /api/cases/{id}
```

---

## 二次开发

**加一个品牌的知识库**：把 md 丢进 `knowledge/vendors/<品牌>/`，然后在 `app/knowledge.py`
的 `BRAND_GLOBS` 里加一行 glob 路由。

**加一个品牌工程文件导出**：在 `app/automation/plc_text_export.py` 的 `brand_exports()`
里加一个分支函数，返回 `[(文件名, 内容)]` 列表。

**改仿真引擎语义**：`app/modules/simulator.py` 里的 `Rung` 数据类和 `_eval_rung()`。
目前支持 `LD/LDI/AND/ANI/OR/ORI/OUT/SET/RST/PLS/PLF/INC/DEC/ADD/SUB/TMR/CNT/CMP/…`。

**加案例**：`app/modules/cases_api.py` 的 `CASES` 列表追加一条 dict 即可。

**前端改动后先做语法自检**（前端是零构建的原生 JS，语法错误会让整个页面的交互静默失效）：

```bash
node --check app/static/modules.js
node --check app/static/app.js
```

没有输出即语法正确。改完前端记得清浏览器缓存（Ctrl+Shift+R 强制刷新）。

---

## 已知限制与诚实声明

这个项目是**工程辅助工具，不是"一键出图神器"**。以下边界请务必知悉：

- **只有信捷 .xdp 与三菱 GX Works2 / 汇川 AutoShop 是「真机验证过能打开并编译通过」的**。
  西门子 SCL / 松下 ST / 台达 IL 走的是各厂商**官方支持的导入通道**（官方语法，非逆向），
  但没有在本机逐一装机验证，首次使用请先拿小样例试导入。
- **AI 生成的程序必须人工审核**。工艺安全逻辑（急停链、安全门、限位、互锁）不可直接照搬上线，
  必须由持证电气工程师复核后才能下载到真实设备。
- **选型计算是工程估算**，用于方案阶段选型和报价；正式设计请以厂商样册与国标计算书为准。
- `knowledge/_manual_txt/`（厂商手册全文文本）与 `knowledge/_raw_archive/`（工程原始导出）
  **未包含在本仓库**——体积大且涉及厂商版权。程序运行不依赖它们（`BRAND_GLOBS` 未引用）。
  你可以把自己合法持有的手册文本放进去，自己用。
- 桌面自动化模块（`gxw_builder.py` / `huichuan_builder.py`）依赖本机装了对应编程软件，
  且依赖 `pywinauto` + `pywin32`（在 `requirements.txt` 里是注释掉的，需要时自行打开）。

---

## 常见问题

**Q: 启动报 `include_router` 相关错误，或者接口全 404？**
A: FastAPI 版本太新。`requirements.txt` 已锁 `<0.115`。0.141+ 的 `include_router` 返回
`_IncludedRouter`（无 `.path` 属性），会让所有模块路由注册失败。
重装：`pip install "fastapi>=0.110,<0.115" --force-reinstall`

**Q: 改了代码但没生效？**
A: 老进程占着 8321 端口。Windows 下：
```bash
netstat -ano | findstr :8321
taskkill /PID <上面查到的PID> /F
```
同时清一下 `__pycache__`（`app/` 下所有目录）。

**Q: 生成时报模型错误？**
A: 基本是 API Key / 额度 / base_url 写错。用「⚙ 模型设置」里的「测试连接」先验证。

**Q: 端口冲突？**
A: 改启动命令里的 `--port 8321`，同时改 `启动.bat` / `启动.vbs` 里的 URL。

**Q: 手机怎么访问？**
A: 用 `--host 0.0.0.0` 启动，手机连同一 WiFi，浏览器开 `http://<电脑局域网IP>:8321`。
Windows 防火墙首次会弹窗，选「允许」。

---

## License

MIT — 见 [LICENSE](LICENSE)。

> ⚠️ 软件按"现状"提供。用于真实设备前，所有程序与图纸必须经持证电气工程师审核。
