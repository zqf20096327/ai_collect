# Root Agent for dsh-go

给 [dsh-go](https://github.com/) 这类手机 AI 助手用的 root 执行通道。

装一个 KernelSU / Magisk 模块，AI 就能在自己的 bash 工具里调用一个本地代理，以 root 身份跑命令，不用每次弹授权框。

```
AI 助手 ──python──> rootagent_cli.py ──TCP 127.0.0.1:18777──> rootagent (uid=0) ──> /system/bin/sh
```

> ### 🤖 如果你是把仓库地址发给 AI 的用户
>
> **直接对你的 AI 说：**
>
> > 按这个仓库里的 AI-INSTRUCTIONS.md 帮我装好
>
> AI 会读 [AI-INSTRUCTIONS.md](AI-INSTRUCTIONS.md)，先检查你的手机有没有 root、是 KernelSU 还是 Magisk，
> 再一步步带你装完、验证通过。**不需要你自己看懂下面这些内容。**

---

> **人类自己看？**
> - 想被手把手带：看 [docs/教程.md](docs/教程.md)
> - 想快速查命令：看下面的速查

---

## 它解决什么问题

在手机上让 AI 干需要 root 的活（读 `/data/adb`、改系统属性、抓包、管模块），会卡在两件事上：

1. **每次都要弹授权** —— `su -c` 一条命令弹一次，几十条命令就是几十次弹窗，根本没法用
2. **拿不到持续会话** —— 每条命令开一个新 shell，环境变量、工作目录全都丢

这个模块起一个常驻的 root 进程，通过本机 TCP 收命令、回结果，一次授权，长期可用。

---

## 特性

- **仅本机可达** —— 只绑 `127.0.0.1`，同一 Wi-Fi 下的设备连不上
- **每设备独立令牌** —— 安装时从 `/dev/urandom` 随机生成 32 字节，写进 `/data/adb/rootagent/token`（权限 600）
- **令牌不落命令行** —— 代理从文件读令牌，`ps` 里看不到
- **开机自启** —— 重启后自动拉起，不用手点
- **看门狗保活** —— 每 60 秒巡检，进程被杀自动恢复
- **点「执行」有完整自检** —— 五步检查，哪步失败直接告诉你原因
- **令牌投放有自愈** —— 装模块、开机、看门狗三层保障，副本丢了自动补回来
- **单文件静态二进制** —— 713KB，无动态依赖，不挑系统 libc

---

## 安装

### 要求

- ARM64 安卓机（Android 7+）
- 已装 KernelSU / Magisk / APatch 之一
- 约 1MB 存储空间

### 步骤

1. 从 [Releases](../../releases) 下载 `rootagent-*.zip`
2. 打开 KernelSU（或 Magisk）→ 模块 → 安装 → 选这个 zip
3. 重启手机

完事。开机后代理就自己起来了。

### ⚠️ 从 v2.0.x 升级的必读

v2.0.x 会把令牌抄一份到**公共存储区**：

```
/sdcard/Download/DSH-Go/rootagent.token
```

这个位置**所有应用都能读**。v2.1.0 起不再写这里，改为投放到应用私有目录。

**升级后请手动删掉那个旧文件：**

```sh
su -c 'rm /sdcard/Download/DSH-Go/rootagent.token'
```

不删也能用，但那个令牌还是有效的，等于留了个后门。

**确认还在不在：**

```sh
su -c 'ls -l /sdcard/Download/DSH-Go/rootagent.token'
```

报 `No such file or directory` 就是删干净了。

**注意**：升级本身不会帮你删这个文件，因为它在模块目录之外，卸载模块也带不走。

**想确认装好了**：到模块页点 Root Agent 那一行的「执行」，会打印：

```
================================================
 Root Agent 自检 & 启动
================================================
时间 2026-11-03 09:40:44
身份 uid=0  u:r:ksu:s0

[1/5] 可执行文件
  [OK]   713592 字节，可执行

[2/5] 令牌
  [OK]   存在，权限 600，长度 64

[3/5] 启动代理
  [OK]   已启动，pid=3550

[4/5] 保活看门狗
  [OK]   已启动，pid=5455，每 60 秒巡检

[5/5] 连通性自测
  [OK]   发命令有回包
================================================
```

---

## 使用

### 拿到令牌

点模块的「执行」，令牌会**自动投放到应用私有目录**，客户端直接就能读到，不用手动复制。

令牌出现在两个地方：

| 位置 | 谁能读 |
|---|---|
| `/data/adb/rootagent/token`（0600 root:root） | 只有 root |
| `<应用私有目录>/rootfs/root/.rootagent_token`（0600 应用uid） | 只有该应用自己 |

> **为什么投放到私有目录**：安卓普通应用受 SELinux 限制读不到 `/data/adb`。
> 投放到应用自己的私有目录后，**只有这个应用能读**，其他应用即使权限相同也读不到，
> 比放 `/sdcard`（所有应用可读）安全得多。

客户端按顺序找令牌：

1. `$ROOTAGENT_TOKEN_FILE`（环境变量）
2. `~/.rootagent_token`（proot 家目录，即投放目标）

**不想投放**（只显示不落盘）：把 `none` 写进 `/data/adb/rootagent/tokendir`：

```sh
su -c 'echo -n none > /data/adb/rootagent/tokendir'
```

**自定义投放位置**：

```sh
su -c 'echo -n /your/path > /data/adb/rootagent/tokendir'
```

**换令牌**：删掉令牌文件后重新点「执行」：

```sh
su -c 'rm /data/adb/rootagent/token'
```

### Python 客户端

```sh
python3 client/rootagent_cli.py 'id'
python3 client/rootagent_cli.py 'ls /data/adb/modules'
python3 client/rootagent_cli.py 'cat /proc/net/arp'
```

### sh 客户端（Termux 里最方便）

```sh
su -c "sh client/rootagent.sh 'id'"
```

### 接到 AI 助手

**方式一：临时交代**（每次新会话都要说一遍）

把 `client/rootagent_cli.py` 放到 AI 的工作区，然后告诉它：

> 需要 root 权限的命令，用 `python3 rootagent_cli.py '<命令>'` 执行

**方式二：写进全局指令**（推荐，一次配置永久生效）

把 [docs/AGENTS-snippet.md](docs/AGENTS-snippet.md) 里的片段贴进 AI 助手的全局指令文件：

| 工具 | 全局指令文件 |
|---|---|
| dsh-go（安卓） | `~/.dsh/AGENTS.md` |
| Claude Code | `~/.claude/CLAUDE.md` |
| Codex CLI | `~/.codex/AGENTS.md` |
| 通用 | `~/.agents/AGENTS.md` |

贴进去之后，AI 在新会话里就知道 root 通道在哪，不用你每次交代。

> **dsh-go 用户注意**：`~/.dsh/AGENTS.md` 是 App 管理的，会定时整个重写，
> 写进去会消失。请写 `~/.agents/AGENTS.md`。

**为什么必须写这段**

不写的话，AI 第一反应会去试 `su` / `sudo`，或者在容器里 `ls /data/adb`，
拿到的全是「不存在」「权限不足」，然后**误判成这台机器没有 root**。

真 root 是有的，只是被 SELinux 和 mount namespace 挡在容器外面了。

### 协议（自己实现客户端）

```
TCP 连 127.0.0.1:18777
  ↓
发令牌一行，\n 结尾
  ↓
发命令的 UTF-8 字节
  ↓
shutdown(SHUT_WR)         ← 必须，否则代理会一直等
  ↓
读回 stdout + stderr + "\n__RC__=<退出码>\n"
```

---

## 安全模型

**这个模块给了本机能拿到令牌的任意进程以 root 权限。** 说清楚它挡什么、不挡什么：

| 威胁 | 是否挡住 | 原因 |
|---|---|---|
| 同 Wi-Fi / 外网设备 | ✅ 挡住 | 只绑 `127.0.0.1` |
| 本机普通应用读 `/data/adb` | ✅ 挡住 | SELinux 不让读 |
| 本机普通应用读投放副本 | ✅ 挡住 | 文件属主是应用自己 uid + 600，别的应用读不到 |
| 本机其他 root 应用 | ❌ 挡不住 | root 不受限，能读令牌 |
| 能运行任意代码的 AI 助手 | ❌ 挡不住 | 它本来就该有权限 |

**设计取舍**：这个模块的用途就是「让一个可信的本机程序长期以 root 执行命令」。它不会、也无法区分调用者是哪个应用 —— 只认令牌。

如果你要更严格的隔离，可以：
- 定期轮换令牌：`su -c 'rm /data/adb/rootagent/token'`，然后点模块的「执行」重新生成（会同时更新投放副本）
- 不用时停掉：`su -c 'pkill -f rootagent'`
- 彻底移除：KernelSU 里卸载模块并重启

---

## 自建

```sh
git clone <this-repo>
cd RootAgent-For-DSHGo

# 依赖交叉编译器（Debian/Ubuntu）
sudo apt-get install -y gcc-aarch64-linux-gnu zip

./scripts/build.sh
# 产出 dist/rootagent-v2.1.2.zip
```

只重新打包、不编译：

```sh
./scripts/build.sh --no-binary
```

---

## 排障

日志在 `/data/local/tmp/rootagent.log`：

```sh
su -c 'tail -50 /data/local/tmp/rootagent.log'
```

| 现象 | 原因 | 处理 |
|---|---|---|
| `bind 失败: Address already in use` | 旧进程占着端口 | `su -c 'pkill -f rootagent/rootagent'` 再点执行 |
| `无法打开令牌文件` | 令牌没生成，模块没装完整 | 重刷模块 |
| `bad token` | 令牌对不上 | 重新 `cat` 令牌，或换掉客户端里的旧值 |
| 连不上 | 进程没起 | 点「执行」看自检 |

---

## 目录结构

```
.
├── src/rootagent.c        # 代理源码
├── module/                # 可刷入的模块内容
│   ├── customize.sh       # 安装时生成令牌
│   ├── service.sh         # 开机启动
│   ├── watchdog.sh        # 保活
│   ├── action.sh          # 执行按钮（自检）
│   ├── uninstall.sh       # 卸载清理
│   └── module.prop
├── client/                # 客户端
│   ├── rootagent_cli.py
│   └── rootagent.sh
├── docs/
│   ├── 教程.md            # 保姆级安装使用教程
│   └── AGENTS-snippet.md  # 给 AI 助手用的全局指令片段
├── scripts/build.sh       # 构建 + 打包
└── .github/workflows/     # CI
```

---

## 许可

MIT
