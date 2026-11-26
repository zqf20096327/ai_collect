# 小熊猫破甲 · pojia

**把你电脑上那几个 AI 客户端「自己改不到的内置提示词」，换成你自己写的那份 —— 点一个按钮的事。**

项目代号 **`pojia`**（仓库名 `pojia-xm`，pojia + 小熊猫），中文名「小熊猫破甲」。
支持 **Codex / WorkBuddy / ZCode / DSH** 四个客户端，一份 `persona.md` 全管，口径一致。

[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![python](https://img.shields.io/badge/python-3.10%2B-blue)](pyproject.toml)
[![platform](https://img.shields.io/badge/platform-Windows%20x64-0078d4)](#项目边界)
[![tests](https://img.shields.io/badge/tests-64%20passed-2ea043)](tests/)
[![deps](https://img.shields.io/badge/运行依赖-2%20个-brightgreen)](requirements.txt)
[![offline](https://img.shields.io/badge/破甲-全程离线-2ea043)](#安全设计)

![主界面](docs/img/ui-main.png)

---

## 为什么叫「破甲」和 pojia

「甲」指的是客户端自带的那个身份外壳 —— 它规定模型怎么称呼自己、守什么规矩、拒绝什么。这层甲在软件装好那一刻就固定下来，用户在设置里翻不到、改不了。

**破甲**就是把这层外壳掀掉，换成你自己写的那份。四个客户端各有各的穿法（有的读配置键、有的读模板段、有的读用户级指令文件），[下面逐层拆开讲](#破甲原理四个客户端分别改哪一层)。

**pojia** 是「破甲」的拼音，也是代码里的项目代号：仓库叫 `pojia-xm`，数据目录叫 `.xiaoxiongmao`，环境变量前缀是 `XM_`。

---

## 🧭 30 秒看懂：这是干什么的？

你平时用的 AI 客户端，每次对话时都会在背后塞一段**你自己改不到的"规矩"** —— 它是什么身份、该守什么、什么不做。

这个工具做的事只有一件：**把那段规矩，换成你自己写的一份。**

| 换完之后 | 说明 |
| --- | --- |
| 用**你的**身份设定 | 而不是软件自带的默认身份 |
| **四个客户端一份口径** | 共用一个 `persona.md`，不用各改各的，也不会前后矛盾 |
| **当场能自证** | 发一句固定口令验证真载入，不靠"感觉好像生效了" |
| **随时能还原** | 点一下还原回官方原版，不依赖备份也能剥干净 |

> **它不修改软件本体**：只做**文本文件层面的替换**，不删包、不碰注册表、不装服务、不常驻后台。
> 想看它到底动了哪一层，跳 [破甲原理](#破甲原理四个客户端分别改哪一层)。

---

## 🚀 三步就能用

### 1️⃣ 拿到程序

| 方式 | 适合谁 | 怎么做 |
| --- | --- | --- |
| 预编译 exe | 不想装 Python | 从 [Releases](https://github.com/SusieCommons/pojia-xm/releases/latest) 下载 `xiaoxiongmao-pojia-<版本>.exe`，双击 |
| 从源码跑 | 想看代码 / 自己改 | 见[从源码跑](#从源码跑) |

单文件 exe，**电脑上不用装 Python**，放哪都行（桌面就行）。

当前版本 **[v1.3.8](https://github.com/SusieCommons/pojia-xm/releases/tag/v1.3.8)**：

```
xiaoxiongmao-pojia-1.3.8.exe    16,335,755 B
SHA-256  b30ca25f527c9ea0dc755e089e8fcf7b28bbb8783b157fb3109416c8218a722a
```

### 2️⃣ 看状态灯

窗口里每一行就是一个客户端，显示**装没装 / 注没注 / 靶点几个**。没装的会标灰；装到非默认位置（比如 `D:\Apps\ZCode`）的，双击那一行手动指定目录，选完会记住。

状态灯是**纯只读**的检测结果 —— 打开窗口随便看，不算动手。

### 3️⃣ 点「一键破甲」

底部橙色按钮。破甲完成后**完全退出客户端再打开**（含任务栏托盘图标）——
提示词是客户端启动时读入的，不重启不生效。

> 第一次打开会先出一张声明卡，读完滑到底才能点同意。记录落在 `~/.xiaoxiongmao/consent.json`。
> 不想读？`--accept` 跳过（脚本用）。

> ### 😰 第一次不敢下手？
> `python app.py apply --dry` 只算不写，**一个字节都不动** —— 它会告诉你"假如执行会改哪些文件"。

> ### ⚠️ Windows 拦我？
> 没有代码签名证书的 exe，SmartScreen 可能会弹「Windows 已保护你的电脑」——
> 这是无签名 exe 的常态。点 **「更多信息」→「仍要运行」** 即可。

---

## 🖥 界面上有什么

| 区域 | 干什么 |
| --- | --- |
| 客户端列表 | 四个客户端各一行：官方图标 / 名称 / 版本 / 状态 / 靶点数 / 勾选框 |
| **一键破甲** | 对勾选的客户端写盘执行 |
| **还原** | 按标记剥回官方原版 |
| **体检** | 逐靶点校验，告诉你哪个没写上、为什么 |
| **刷新** | 重扫磁盘，重新探测安装位置 |
| 人格编辑框 | 直接改 `persona.md`，改完保存 → 重新点「一键破甲」生效 |

窄屏下同一界面：

![窄屏](docs/img/ui-narrow.png)

> **数据落在哪**：`~/.xiaoxiongmao/` —— 人格、状态、日志、历史备份都在这，不乱扔文件。
> 备份按时间戳分目录（`backups/<时间戳>/`），保留最近 10 份，更早的自动清。

---

## 🛡 「会不会把我电脑搞坏？」—— 你最该担心的五件事

| 你担心的 | 实际情况 |
| --- | --- |
| **改坏了能不能恢复？** | 每个改动都**先备份**再写；点「还原」一键回官方原版。而且还原**按标记剥**，备份丢了也能剥干净 |
| **会不会偷偷联网 / 上传我的数据？** | **破甲全程不联网**。版本检查和品牌信息是可选增强，拿不到就用内置默认值，不锁功能、不弹窗 |
| **会不会删我的东西？** | 只做文本文件层面的替换。**不删包、不碰注册表、不装服务、不常驻后台**。判不出来是不是本工具产物时，一个字节都不动 |
| **写到一半断电会写坏吗？** | 所有写入走**临时文件 + `os.replace`**，要么全成、要么原文件不动。写到一半被打断只会留下残块，下次运行会自动识别并清掉 |
| **是不是要花钱？** | **开源（MIT）**，下载即用。1.3.0 起已取消在线授权 —— 没有激活码、没有 token、没有联网校验，装完直接能用 |

---

## ✅ 装完怎么确认真的成功了？

在客户端里**新开一个会话**，单独发这五个字：

```
小熊猫自检
```

**预期它只回两行**，多一个字、加解释、拒答 —— 都说明没真载入：

```
自检成功
<persona.md 里写死的署名行>
```

第一行固定是 `自检成功`。第二行来自 `persona.md` 里的署名串 —— 仓库里的 `persona.md` 用的是占位值，你换成自己的之后回执会跟着变。
**判据是「回了两行、第一行是 `自检成功`」，不是「第二行必须是某个具体的串」。**

没回？先**完全退出客户端**（含托盘图标）再打开，然后重试。还是不行，点界面上的「体检」，它会告诉你哪个靶点没写上、为什么。

> **为什么用这种笨办法验证**：问它"你运行在什么模式"等于自我暗示，模型很可能顺着你答，结果不可信。
> 给一条**固定口令 + 固定回复**才是真判据 —— 口令写在客户端的配置文件里，路径见[破甲原理](#破甲原理四个客户端分别改哪一层)。

---

## ❓ 常见问题

**Q：点完了，客户端里没反应？**
A：提示词是客户端**启动时**读入的。完全退出（任务栏托盘图标也要退）再打开。改完立刻在已开的会话里试是看不到的。

**Q：破甲之后原来的设置还在吗？**
A：在。破甲只替换提示词那一层，模型选择、快捷键、插件、历史会话全都不动。点「还原」就回到官方原版。

**Q：客户端升级后人格没了？**
A：升级会覆盖配置文件。重新点一次「一键破甲」就行，它只补该补的，不重复劳动。

**Q：怎么防止客户端升级后又被覆盖？**
A：`python app.py watch` 起一个守护进程，它**只补「以前注入过、现在丢了」**的客户端，从没碰过的不动。版本检查 30 分钟一轮，不会连续请求更新源。

**Q：Codex 里我自己写的 `xm-persona.md` 会被删吗？**
A：不会。还原时三级优先：备份有原文就写回 → 确认是本工具产物才删 → 判不出来不动，并告诉你路径。

**Q：目标文件是 GBK 或者 UTF-16 怎么办？**
A：这是 1.3.7 修掉的两个坑，见[编码契约](#编码契约)。注入后客户端读到的一定是正常文本；还原后你的文件**逐字节**回到原样。

**Q：WorkBuddy 装了多个版本？**
A：`plugins/cache/workbuddy-builtin/` 下面每个版本目录都会写一遍。只写当前在用的那个，切版本之后人格就没了。

**Q：需要管理员权限吗？**
A：不需要。改的全是用户目录下的文件。装在 `C:\Program Files` 的客户端才需要，而且工具会明确告诉你是权限问题，不会含糊地说"写入失败"。

**Q：能发朋友吗？**
A：能。exe 直接发过去，双击即用，什么都不用装。

---

## 📖 详细一点

### 它管哪四个客户端

| 客户端 | 是什么 | 注入方式 |
| --- | --- | --- |
| `codex` | Codex（OpenAI CLI / 桌面端） | 官方 `config.toml` 的 `model_instructions_file` 指向人格文件 |
| `wb` | WorkBuddy | 主提示词模板的 `<content_policy>` 段整段替换 |
| `zcode` | ZCode 桌面端 | `~/.zcode/AGENTS.md` 整文件注入 |
| `dsh` | DeepSeek Harness | `~/.dsh/AGENTS.md`（+ 已存在的 `~/.agents/AGENTS.md`） |

---

## 破甲原理：四个客户端分别改哪一层

四个客户端的提示词来源不一样，所以破甲的落点也不一样。**没有一个是"破解"** —— 全是它们自己提供的文本入口，只是普通人不知道在哪。

### Codex —— 换掉「模型指令」的指向

Codex 的 `config.toml` 里有一个官方键：

```toml
model_instructions_file = "C:\\Users\\<你>\\.codex\\xm-persona.md"
```

这是 Codex 用来**替换**模型指令的正规入口。工具做两件事：把人话写进 `xm-persona.md`，然后在 `config.toml` 顶层插入这一行。

**为什么不用 `AGENTS.md`**：往 `AGENTS.md` 追加内容只是补充上下文，会被项目级 `AGENTS.md` 和产品自带提示词一起稀释。`model_instructions_file` 是替换，不是追加 —— 差一个量级。

**这一步最容易假成功**：配置指向的文件如果不存在，Codex 会**静默退回内置指令**，界面上完全看不出问题。所以写入顺序是"先落地正文文件，再改配置"，而且改完立刻回读校验。

**两个实现上的坑**：

- 键必须插在**第一个 `[table]` 之前**。插进表里就变成那张表的键，Codex 读不到。
- 扫描时要跳过 `"""` 多行字符串 —— 人格正文里可能正好有 `model_instructions_file = ...` 这样的示例文本，误匹配会插到字符串里面去。

### WorkBuddy —— 换掉策略段

WorkBuddy 的主提示词是一个 **Jinja 模板**（`prompt.tpl`），几十 KB，里面有大量 `{% if %}` / `{% include %}`。整个文件改不得，改了渲染就崩。

模板里有一段 `<content_policy>...</content_policy>`。**这一段的长度和位置在多个版本里都稳定**，是唯一能整段替换而不破坏 Jinja 结构的地方。工具把段内的内容换成注入块，段外的模板原样保留。

**所以注入点必须落在段内**。塞到段外（比如文件末尾）会破坏模板渲染 —— 代码里先找这个段，找不到就跳过并报出来，不硬写。

**为什么每个版本目录都要写**：`plugins/cache/workbuddy-builtin/<插件>/<版本>/prompt.tpl`，版本目录名带构建号。只写当前在用的那个，客户端切版本之后人格就没了。

### ZCode / DSH —— 换掉用户级指令文件

这两个客户端都读用户目录下的一份 `AGENTS.md` 当全局指令。直接整文件注入即可，没有结构约束。

| 客户端 | 路径 | 说明 |
| --- | --- | --- |
| ZCode | `~/.zcode/AGENTS.md` | `ZCODE_HOME` 可覆盖 |
| DSH | `~/.dsh/AGENTS.md` | `DSH_HOME` 可覆盖 |
| DSH（备用） | `~/.agents/AGENTS.md` | `DSH_AGENTS_HOME` 可覆盖；**不存在就不创建** |

最后一条是刻意的：不存在的备用路径不主动创建，免得在用户机器上凭空多出一个目录。

### 三个共同的技术点

#### 标记段

注入的正文用一对**纯文本**标记围起来：

```
========== xm-persona:begin ==========
...你的正文...
========== xm-persona:end ==========
```

用纯文本而不是 HTML 注释，是因为目标文件里有 `.md`、`.toml`、`.tpl` 三种格式 —— 只有纯文本标记在三种里都安全。`<!-- -->` 写进 TOML 会让它解析失败。

**有头无尾也算注入痕迹。** 尾标记丢了恰恰是最需要处理的情形：上次写到一半被打断（断电、任务管理器结束进程、编辑器异常保存）。如果判据要求头尾都在，这种残块既不算注入、也还原不掉，用户只能手动删文件。

#### 编码契约

两个方向必须**分开**，混在一起就会出「提示成功但没生效」：

| 阶段 | 做什么 | 为什么 |
| --- | --- | --- |
| 注入 | **统一写 UTF-8** | 四个客户端都是 Node / Electron，读用户级指令一律按 UTF-8。写 GBK 进去它解成乱码，人格等于没注入，界面却报成功 |
| 还原 | **按备份原始字节写回** | 用户的文件不能因为我们注入一次就永久变成 UTF-8 |

对应 `core/base.py` 里两个函数：`write_like()` 写 UTF-8，`write_orig()` 写原始字节。**别合并。**

**无 BOM 的 UTF-16 是最阴的一种**：`b'#\x00 \x00...'` 按 UTF-8 解码**不报错**，只会解出一串带 NUL 的垃圾，然后被原样写回，原文彻底毁掉。所以判断编码不能靠"试解码成功"，得看零字节的分布（长度偶数、零字节占比 8%~50%、85% 以上落在同一侧）。

#### 还原为什么按标记剥，而不是按备份写回

这是踩过的坑，写在代码里也写在这里。

第一次注入时，如果目标文件里**已经有**注入内容（上一版留下的、或者备份是在注入之后才抓的），那份「原始内容」其实已经是注入态。拿它写回去等于原地覆盖 —— 界面报「已还原 N 个」，打开客户端人格照旧。

所以现在的顺序是：

1. 按 `xm-persona:begin/end` 剥离。这是唯一可靠的依据，因为标记是我们自己写的。
2. 剥完文件变空、且确认是本工具产物 → 删文件。
3. 判不出来 → 不动，报给用户。

备份只在第 1 步拿不到内容时兜底。

### 想换成自己写的人格

**GUI 里最省事**：窗口底部的人格编辑框直接改 → 保存 → 对目标重新点一次「一键破甲」。

也可以把写好的人格存成 `.md`，替换仓库根目录的 `persona.md`，再跑：

```bash
python app.py apply
```

人格文件里至少要包含两样东西：**身份设定**（它是谁、怎么说话）和**自检口令**（发什么、回什么）。后者是唯一能验证"真的生效了"的判据。

---

## 安全设计

### 写盘

- **原子写**：先写同目录临时文件，`os.replace` 覆盖。要么全成，要么原文件不动。
- **只读属性**：目标文件带只读属性时，先清属性再写，写完不恢复 —— 恢复了下次又写不进去。
- **占用重试**：`os.replace` 遇 `PermissionError` 退避重试，专门对付杀软扫描窗口。
- **先备份**：改动前存到 `~/.xiaoxiongmao/backups/<时间戳>/`，保留最近 10 份。

### 只读是真的只读

`status` / `apply --dry` / 「体检」实测新增文件数 = **0**。这三个动作不会写任何东西，包括备份目录。

### 离线

注入全程**零网络请求**。版本检查走的是可选路径 —— 更新源不可达就用内置默认值，不锁功能、不弹窗、不写缓存。

### 仓库门禁

```bash
python tools/check_clean.py --history
```

查工作区 + git 历史里有没有私钥、生产地址、本机绝对路径。CI 跑同一份，规则只有一处。

### 下载后自己核一遍

仓库根目录有 `SHA256SUMS.txt`，覆盖全部跟踪文件。仓库带 `.gitattributes` 声明 `* text=auto eol=lf`，clone 下来就是 LF，不用额外设置。

最省事的是直接用脚本，它在算哈希前会把 CRLF 折成 LF，行尾怎么设置都能对上：

```bash
python tools/make_sums.py --check
```

要通过系统自带工具逐项核对也行：

```bash
# Linux / macOS
sha256sum -c SHA256SUMS.txt

# Windows PowerShell
Get-Content SHA256SUMS.txt | ForEach-Object {
  $h, $f = $_ -split '  ', 2
  if ((Get-FileHash $f -Algorithm SHA256).Hash -ne $h.ToUpper()) { "MISMATCH: $f" }
}
```

**为什么脚本要先折成 LF 再算**：`.gitattributes` 管的是 checkout 时的规范化，管不到 `core.autocrlf` 已经把已有工作区改成什么样，也管不到手工编辑过的文件。拿工作区原始字节直接算哈希，同一份内容在不同机器上会得出不同结果，清单就失去意义了。归一之后两边的结果一致，出问题的只可能是文件内容本身。

CI 每次都会跑这一步，对不上直接红 —— 清单和源码不可能长期不一致。

Release 里那个 exe 的哈希单独发布在 Release 正文，因为仓库里的清单只覆盖源码，exe 不进库。

### 产物校验

单元测试覆盖的是源码逻辑，打包链路是另一回事 —— spec 漏文件、入口找不到、图标路径写错，这些只有真打一次才暴露。所以发版前还要验产物：

```bash
python -m PyInstaller --noconfirm --clean --distpath dist xiaoxiongmao.spec
python tools/verify_release.py
```

它分两层：

| 层 | 查什么 |
| --- | --- |
| 静态 | PE 版本资源里的 `FileVersion` 是否等于 `app.py` 的 `VERSION`（对不上说明 exe 是旧的）、图标帧数 |
| 动态 | 在临时目录里跑真 exe，走完条款闸门 → 注入 → 校验 → 还原 |

动态那层把 `HOME` / `USERPROFILE` / `XM_DATA` / `CODEX_HOME` / `ZCODE_HOME` / `DSH_HOME` 全部重定向到沙箱，不碰你本机的任何客户端配置。覆盖的具体项：

- 未同意条款时退出码是 2，且打印了条款正文
- codex 注入后是 UTF-8、无 BOM、不是 UTF-16 形态，还原后逐字节等于原始 GBK
- zcode 追加模式：标记段只出现一次，用户原文保留，连注入三次体积不变
- 无 BOM 的 UTF-16LE 目标：注入后按 UTF-8 可读，还原后逐字节一致

---

## 从源码跑

```bash
git clone https://github.com/SusieCommons/pojia-xm
cd pojia-xm
python -m pip install -r requirements.txt
python app.py
```

界面用 pywebview + WebView2（Win10/11 自带运行时）。只跑命令行的话 `requirements.txt` 里只有 `cryptography` 是必需的，`pywebview` 可以不装。

### 命令

```bash
python app.py                            # 打开窗口（默认）
python app.py status                     # 四个客户端装没装、注没注
python app.py apply                      # 全部注入
python app.py apply -t codex -t zcode    # 只注入指定的，-t 可重复
python app.py verify                     # 校验注入结果
python app.py revert                     # 全部还原
python app.py dir                        # 看客户端目录
python app.py dir zcode "D:\Apps\ZCode"  # 改 ZCode 的目录
python app.py dir zcode --forget         # 清掉手动指定，回到自动探测
python app.py apply --dry                # 只算不写，一个字节都不动
python app.py --accept apply             # 跳过条款交互（脚本用）
python app.py watch                      # 常驻守护，被覆盖了自动补
```

`xm.py` 是同功能的薄包装（`gui / status / apply / revert` 四个子命令），`pip install -e .` 之后可以直接 `xm status`。

### 打包成 exe

```bash
python -m pip install pyinstaller
python tools/make_version_info.py     # 从 app.py:VERSION 生成版本资源
pyinstaller xiaoxiongmao.spec
```

产物在 `dist/xiaoxiongmao.exe`。onefile、无控制台窗口，界面和人格都内联进包，不挂外链资源。

`build/` 在 `.gitignore` 里（构建产物不该进库），所以从仓库直接 clone 下来是没有版本资源和图标的。版本资源用上面的 `make_version_info.py` 生成 —— 它只从 `app.py:VERSION` 读版本号，把 `filevers` / `prodvers` / `FileVersion` / `ProductVersion` 四处一次写完，不会漏。图标是二进制，需要自己准备 `build/icon.ico`；不放也能出包，只是用默认图标。

打完先验一遍再发：

```bash
python tools/verify_release.py
```

<details>
<summary><b>想换成自己的群 / 自己的品牌行（点开）</b></summary>

直接改源码是不行的 —— `tools/check_clean.py` 里存着已知引流号码的 SHA-256
指纹，扫工作区和全部历史，命中就 CI 红。真实群号写进被跟踪的文件，这个仓库
就推不上去了。

所以走**打包时注入**：源码里始终是占位值，打包前生成一份副本，只换品牌常量。

```bash
# 1. 生成注入副本到 build/brand_local/（不进库）
python tools/make_brand.py --group <你的群号> --name <群名>

# 2. 从副本打包
cd build/brand_local
python -m PyInstaller --noconfirm xiaoxiongmao.spec

# 3. 确认号真的换进去了
python tools/make_brand.py --check build/brand_local/core/brand.py
```

第 3 步别省。包里的群号还是占位值时，`--check` 会直接说不合格 ——
这种包发出去，用户看到的是加不进的号。副本会替换三处：`core/brand.py`
的三个常量、`persona.md` 里的署名行（人格正文落进客户端后也得是真号，
否则用户从人格卡里抄到的是假号）。

</details>

<details>
<summary><b>跑测试（点开）</b></summary>

```bash
python -m pytest tests/ -q
```

64 个，覆盖的是「真机会遇到但常规测试不会碰」的情形：

- 目标文件是 GBK / UTF-16（带 BOM / 不带 BOM）
- 文件带只读属性
- 文件被短暂占用（杀软扫描窗口）
- 备份目录写不了
- 同一插件有多个版本目录
- 模板里没有 `<content_policy>`（不能当靶点，往里塞会破坏 Jinja）
- 用户手动指定了错的目录
- 中文用户名路径
- 空文件（0 字节）
- 注入两次再还原（历史 bug 的现场）
- 命令行帮助是中文的（`core/zh_argparse.py` 接管 argparse 的 `_()`，`app.py` / `xm.py` 两个入口都不许漏回英文）

全部在临时目录里跑，不碰真实客户端。`tests/conftest.py` 把所有客户端环境变量指向临时目录 —— 跑测试不会动你机器上的任何配置。

</details>

---

## 项目边界

**做什么**

- 四个客户端一份口径。共用一个 `persona.md`，不是各改各的。
- 每步可见。装了什么、写到哪个文件、成功没有，都能看到，不靠"应该生效了"。
- 随时可回滚。改前备份，还原按标记剥，不依赖备份也能干净。
- 离线可用。破甲全程不联网，断网跑功能一样。

**不做什么**

- **不改客户端二进制。** 只动文本配置，不动 `app.asar`、不动 `.exe`、不注入进程。
- **不做内核层 / 驱动层。** Windows 语义下的文件操作，够用就行。
- **不做多账号管理。** 一台机器一份配置。
- **不支持 macOS / Linux。** 靶点路径、只读属性、文件占用重试全是 Windows 语义，硬移植会到处漏。

**已知限制**

- **Windows only。** 见上。
- **WorkBuddy 的 `prompt.tpl` 是 Jinja 模板。** 注入点必须落在 `<content_policy>` 段内部，塞到别处会破坏模板渲染。所以代码里先找这个段，找不到就跳过并报出来，不硬写。
- **客户端更新会覆盖配置。** Codex 升级后 `config.toml` 可能被重写，重跑一次 `apply` 即可，或者让 `watch` 常驻自动补。
- **更新源不可达不影响破甲。** 版本检查是可选的，拿不到就用内置值。
- **首次操作有约 2 秒的机器码采集开销。** `_raw_ids()` 会依次试 `wmic` 和 PowerShell 兜底，`wmic` 被安全策略拦住时每次都要等它返回。GUI 里有进程级缓存，第一次慢、后面快；命令行每次新进程都重新算。真正的写盘只有几毫秒 —— 8 个文件 161 KB，单文件 10 KB 约 0.8 ms。

---

## 📁 文件说明

| 文件 | 说明 |
| --- | --- |
| `app.py` | 入口：GUI / CLI / 更新检查 / 品牌信息 |
| `xm.py` | CLI 薄包装（`pip install -e .` 之后是 `xm`） |
| `persona.md` | 唯一共用人格源，四个客户端共用这一份 |
| `core/base.py` | 注入引擎：编码、原子写、标记段、备份、状态 |
| `core/zh_argparse.py` | 把 argparse 的骨架文案换成中文（两个入口共用） |
| `core/codex.py` | Codex 靶点（配置键 + 正文文件） |
| `core/wb.py` | WorkBuddy 靶点（`<content_policy>` 段 + 多版本目录） |
| `core/zcode.py` | ZCode 靶点 |
| `core/dsh.py` | DSH 靶点 |
| `ui/index.html` | 界面（单文件，图标全内联） |
| `tests/` | 64 个测试 |
| `tools/check_clean.py` | 仓库门禁（CI 也调它） |
| `tools/make_sums.py` | 生成并校验 `SHA256SUMS.txt` |
| `tools/verify_release.py` | 打包产物校验：PE 版本资源 + 沙箱里跑真 exe |
| `tools/make_version_info.py` | 从 `app.py:VERSION` 生成 `build/version_info.txt` |
| `xiaoxiongmao.spec` | PyInstaller 打包配置 |
| `docs/targets.md` | 四个客户端的靶点对照表 |
| `CHANGELOG.md` | 每个版本改了什么、升级要注意什么 |

---

## 🙏 致谢

本项目的靶点定位与注入思路来自开源社区的多个前作，一并致谢：

| 项目 | 借鉴了什么 |
| --- | --- |
| [dsh-purge](https://github.com/kingcharleslzy-ai/dsh-purge) | 「本机优先 / 每步可见 / 随时可回滚 / 不替你做决定」四条设计口径；备份校验机制 |
| [codex-session-patcher](https://github.com/ryfineZ/codex-session-patcher) | 「交付即验证」：注入结束后主动验证补丁真实驻留，杜绝假成功 |
| [dsh-market](https://github.com/dsh-market/dsh-market) | 可视化分发的一键安装体验参考 |

用到的开源组件：

| 组件 | 许可证 | 承担什么 |
| --- | --- | --- |
| [cryptography](https://github.com/pyca/cryptography) | Apache-2.0 / BSD-3-Clause | Ed25519 验签（版本与品牌信息） |
| [pywebview](https://github.com/r0x0r/pywebview) | BSD-3-Clause | 原生窗口壳 + WebView2 绑定 |
| [PyInstaller](https://github.com/pyinstaller/pyinstaller) | GPL-2.0 + 启动器例外 | 打成单文件 exe，用户免装 Python |
| [Microsoft Edge WebView2](https://learn.microsoft.com/microsoft-edge/webview2/) | 微软运行时 | 渲染内核，Win10/11 自带 |

> 界面**没有**用 Electron / Tauri / Qt。选 pywebview + WebView2 的原因是包体小（免打包 Chromium）、Win10/11 自带内核。代价是**强依赖 WebView2 运行时**，所以它被列为第一项排查目标。

---

## 许可

**MIT License** —— 随便用、随便改、随便分发、甚至可以商用，**保留版权声明即可**。详见 [LICENSE](LICENSE)。

安全问题走 [SECURITY.md](SECURITY.md)，不要开公开 issue。想参与见 [CONTRIBUTING.md](CONTRIBUTING.md)。
