# SDS · Super DeepSeek Harness Bot（超级 DSH）

> **非官方、社区开源项目，与 DeepSeek、xAI 等公司无关；基于 DeepSeek Harness（MIT）。**
> 简称 **SDS**（界面里就叫 SDS）。项目代码与文档采用 MIT；`shell/pets/` 里的角色形象是**第三方同人素材，采用 CC BY-NC-SA 4.0（仅限非商业），不在 MIT 范围内**，见下文「角色形象」。
> 当前是 **v0.2.0-beta 测试版**，请当测试版看待。

**English.** SDS (Super DeepSeek Harness Bot, "Super DSH") is an unofficial, community, phone-first hub that sits on top of
the DeepSeek Harness kernel and runs on your own machine. You talk to one lead assistant; it works with a small team of
assistants (each with its own avatar) and tracks everything on a kanban board with a ledger. Since v0.2.0-beta: long
conversations with topics, recoverable delete, an assistant that can edit SDS itself (with restore points and a rescue script),
three permission levels with four always-ask categories (spending, sending outward, deleting, touching live services), the assistant you talk to
answers you itself (no hand-off without your nod), voice input and "read aloud" through any OpenAI-compatible speech endpoint on a private network,
and a file-based task board. Status: beta, developed on macOS, docs mostly in Chinese for now, **contributions and English translations are very welcome**.
License: MIT for code and docs; the character art in `shell/pets/` is third-party fan art under CC BY-NC-SA 4.0 (non-commercial) and is not covered by MIT.

演示视频：即将发布

---

## 一句话

SDS 是一个**手机优先的个人助理中枢**，建在 DeepSeek Harness（DSH）内核之上、跑在你自己的机器上：你只和首席助理说话，它带着一小队带形象的助理替你干活，进度全在一块任务板上；花钱、对外发送、删除、动线上服务这四类事，一定先问你。

## 现在能做什么

（每一条的依据和还没做到的部分，见下文「现在做到哪」。）

- **一群助理，一个入口**：首席助理加几位同事，各有名字、形象和职责；对话、传文件、拉群讨论、今天页、账本都在手机宽度下做过。
- **谁被问谁答复**：你跟哪位助理说话，就由哪位自己答复、自己办完；要交给同事，得你点头才会建交接单，没点头不交接。
- **长对话和话题**：和首席的一条对话可以一直聊下去，系统按话题把它归成一个个话题栏；归错了可以改归，旧的话题能翻回去看。
- **删除可恢复**：消息和话题左滑可删，删掉的进「最近删除」，能恢复。
- **首席能改 SDS 自己**：你交代一句，首席可以改 SDS 的源码、检查、重新打包；每次改之前自动存一个还原点，生效前要你点头，改坏了可以在设置的「改动记录」里一键退回，也有一个单独的救援脚本。
- **权限三档，四类先问**：默认「全开」，也可以切到「改动前问」或「只读」。无论哪一档，**花钱、对外发送或公开发布、删除、动线上服务**这四类都先出确认卡，你点头才执行。
- **能听能说**：界面里点录音，转成文字发出去；回复旁有「念出来」。转写和合成都接你自己的、OpenAI 兼容的接口（见下文「语音怎么接」）。
- **任务板与接力**：一件事一张卡；可以派给某位助理、让空闲的助理自己领、交给首席安排、定时、排成一条接力路线（一棒交一棒，可要求「要我看一眼」才放行）；Codex、Claude Code、Grok 等外部 agent 用命令行领单。
- **任务板文件版**：后端可以把任务板同步成一个本机目录里的文本文件，给本机的 agent 读；回写只有命令行和一个投文件口两条路，规则和界面里一样。
- **账本**：记每位助理花了多少次调用；可选读你自己的额度插件写出的文件，显示额度卡，读不到就按价目估算。

## 截图

全部是仓库自带的虚构演示数据（手机宽度 390×844，无头浏览器截图）。六位助理的形象都是第三方同人素材（首席是动图「蓝毛小女仆」，其余五位是 CrossPet 的静态立绘，出处与许可见下文「角色形象与许可边界」）；没有这些素材时界面用自绘的示意团子。

| 首页 | 对话 | 看板（接力卡） |
| --- | --- | --- |
| ![首页](docs/images/home.png) | ![对话](docs/images/chat.png) | ![看板](docs/images/board.png) |

| 接力时间线 | 今天（含等你处理） | 新建任务 |
| --- | --- | --- |
| ![接力时间线](docs/images/relay-timeline.png) | ![今天页](docs/images/today.png) | ![新建任务](docs/images/new-task.png) |

长对话的话题栏和回复旁的「念出来」（v0.2.0-beta 新增；这张是用本版构建重截的，其余几张沿用上一版的截图）：

![话题栏与念出来](docs/images/topics.png)

删掉 `shell/pets/` 目录之后六位助理都会变回自绘示意形象：

![没有 pets 目录时的首页](docs/images/home-no-pets.png)

## 现在做到哪（如实说）

**用真模型和真服务验过**（作者本人的环境，样本不多）：
- 对话与派活、看板、接力三棒自动走、卡住回答后继续、「交给首席安排」、一次性定时；Grok CLI 与 Claude Code 各真接了一张卡，Codex 经接单器接了一张卡。
- 长对话（首席一条线、话题栏）、删一条消息再恢复、左滑删除。
- 首席改自己走通一整圈：开始 → 改 → 检查 → 打包 → 「生效前问一次」确认卡；在「改动记录」里发退回，确认后源码与页面都恢复原样。
- 谁被问谁答复：对一位助理提一个需要同事内容的问题，它自己答复、没有建单；明确说「把这件事交给某位助理」才建单。
- 四类先问：`git push` 出确认卡并在拒绝后不执行；写共享区文件不出卡。
- 语音：一段中文录音转写出的字与原话一致，转写结果发出后助理照办；点「念出来」页面里能放出声（无头浏览器验证）；合成地址写错时播放条显示「这会儿念不出来」，不崩。

**只在测试里验过**（单元测试、假时钟、假执行器、假接口，没有真模型或真设备跑过）：重复定时、夜间不打扰、错过补跑、外部拉起的失败/超时/重试/每日上限、接棒助理被停用后换人、一棒超时催办；任务板文件版的镜像与投文件口；账本读插件文件；本体转写（`native`）与它的回落。

**已知问题 / 还没做**（写在前面，别被宣传词骗了）：
- **`ask_colleague` 还没接真模型**：助理想先问问同事再答复时，现在拿不到同事的正文（回空正文）。
- **Gemini 接单没通**：接单器的配置模板在，但作者试跑时官方个人版客户端已不被支持，**未验证**。
- **没有在真 iPhone 上验收过**：界面在手机宽度的无头浏览器里看过；iPhone 主屏幕模式下「念出来」能否自动播放**未验**。Android、Windows、Linux、其它手机浏览器没验。
- **「学技能」还没做**：助理不会从一次做过的活里自己总结出可复用的技能。
- 首席没有「退回还原点」的工具：要退回，请在设置的「改动记录」里点，或用救援脚本。
- 语音：没有全双工，也不能打断正在念的内容；播放条固定在底部，会盖住设置页里「自动念」开关那一行；同事分身功能包（`subagent`）没实测、默认不开。
- 全开档下有几条命令判定偏松（见 [CONTRIBUTING.md](CONTRIBUTING.md) 的已知失败）；需要更稳时请用「改动前问」档。
- 界面以竖屏手机为主；平板和宽屏只是能用。文档以中文为主，英文只有简介。
- 这是测试版：数据格式可能变，升级前请自己备份运行目录。

## 两分钟上手

### A. 只看演示（不需要后端、不需要钥匙、不联网）

需要 Python 3（只用标准库）。

```sh
git clone https://github.com/mouxue56-debug/super-dsh.git && cd super-dsh/shell
python3 build.py                  # 打出 dist-generic/DSH-Hub.html（单个文件，约 2 MB）
open dist-generic/DSH-Hub.html    # 或直接双击；里面是虚构的演示数据
```

想看到助理们的形象（首席带动作，其余五位按状态换姿态），用一个本地静态服务打开（浏览器不允许 `file://` 页面读取旁边的图片）：

```sh
python3 -m http.server 8000 -d dist-generic   # 然后打开 http://127.0.0.1:8000/DSH-Hub.html
```

### B. 接真后台（要装 DSH 内核）

需要 Node 22 或更新，以及你自己装好的 DSH 内核（实测区间 `>=0.2.2-rc.1 <0.2.3`，本仓库不含它）。
先跑一个隔离的演示实例，假模型、虚构数据、只听 127.0.0.1：

```sh
cd hub
scripts/doctor.sh --target /绝对路径/demo           # 体检：缺什么、怎么办
scripts/start.sh --demo --target /绝对路径/demo     # 起，约两秒，会打印带一次性钥匙的本机地址
scripts/stop.sh  --target /绝对路径/demo            # 停
```

接你自己的模型、自己的助理，见 [docs/安装.md](docs/安装.md)。

## 语音怎么接

SDS 自己不带语音模型。转写（语音转文字）和合成（念出来）都去找**你自己准备的、OpenAI 兼容的接口**，在运行目录的 `config/hub.yaml` 里加一段 `voice`（地址、模型名、音色都换成你自己的）：

```yaml
voice: {"asr_url":"http://127.0.0.1:8000/v1/audio/transcriptions","asr_model":"你的转写模型名",
        "tts_url":"http://127.0.0.1:8001/v1/audio/speech","tts_model":"你的合成模型名","tts_voice":"你的音色名"}
```

- 转写按 OpenAI 的 `/v1/audio/transcriptions` 形状（multipart，字段 `file` 和 `model`，回 JSON 里的 `text`）；合成按 `/v1/audio/speech` 形状（JSON `model`、`input`、`voice`），返回音频。
- **地址必须是本机回环、私网（`10/8`、`172.16/12`、`192.168/16`）、Tailscale（`100.64/10`、`*.ts.net`）之一；公网地址和带账号密码的地址会被后端拒绝启动。** 想接云端服务，请先在你自己的私网里放一个转发。
- 不写 `tts_url`：界面上「念出来」回「还没接上」；不写 `asr_url`：录音留下，提示转写不可用。音频都不会丢。
- 单次「念出来」默认只念前 200 字、最多 16 句；代码块、表格和链接地址不念。
- 另有 `engine` 可以把「远程接口」和「本机的 DSH 自带转写」按顺序串起来（前一个失败才用下一个），细节见 [hub/packages/hub-bff/docs/语音与传文件.md](hub/packages/hub-bff/docs/语音与传文件.md)。

## 首席改自己，改坏了怎么退回

- 打开方式：运行目录配置里的 `self_edit`（默认关，接好线再开）和权限设置，见 [hub/packages/hub-bff/docs/改自己.md](hub/packages/hub-bff/docs/改自己.md)。公开版新装默认全开档，助理可以按你的交代直接改源码、检查、打包。
- 每次改之前自动存一个**还原点**；改完先自动检查，通过了才打包；**让改动生效（重启）前一定要你点头**。
- **怎么退回**：设置 → 改动记录 → 选一个还原点退回（同样要点一次确认）；界面进不去时，用运行目录里的救援脚本（`rescue.mjs`，只需 Node 与 Git；`list` 看还原点、`restore <id>` 退回、`restart` 重启、`status` 看状态，用法见改自己文档）。
- 它只改 SDS 自己的源码；花钱、对外发送、删除、动线上服务，照样先问。

## 权限规矩

- **三档**：`open` 全开（新装默认）、`ask` 改动前问、`readonly` 只读；档位文件缺失或损坏时按「改动前问」处理，不会放宽。
- **四类先问（任何档都一样）**：① 花钱或扣积分；② 对外发送或公开发布（`git push`、发邮件、会改写远端的请求……）；③ 删除，或覆盖没有备份的文件；④ 动线上服务、改系统、扩大授权、读密钥。**一键全停优先于任何档位。**
- 权限层是**第二道门**，第一道是 DSH 内核沙箱和一个专用的低权限系统用户，请先把第一道配好。
- **只建议在私网里用**：默认只听 `127.0.0.1`；给手机用请放在你信任的私有网络里，**不要把端口暴露到公网**。
- 模型读到的网页和文件当作资料而不是命令，但这是约定不是保证。
- 详见 [docs/安全与权限.md](docs/安全与权限.md)；发现漏洞请看 [SECURITY.md](SECURITY.md)（私下报告，别在公开 issue 里贴利用细节）。

## 怎么参与

欢迎一起改。**[CONTRIBUTING.md](CONTRIBUTING.md)** 里有：怎么跑测试、已知失败是哪几条以及原因、
**想要帮忙的方向清单**（Linux/Windows 验证、Gemini 接入、英文界面、角色包规范、`ask_colleague` 接真模型……都有新手能下手的题目），
还有提 issue 和 PR 的约定。不确定从哪下手，开个 issue 说一声就行。

## 目录

```
shell/   界面壳（纯静态网页，python3 build.py 出单文件）；shell/pets/ 是第三方角色素材（CC BY-NC-SA 4.0）
hub/     后端：hub-bff（接 DSH 的服务）、hub-plugin（权限层）、hub-web（网页服务与适配层）、tools/runner（外部 agent 接单器）
docs/    使用文档：安装、安全与权限、接力、任务板与外部 agent、角色包怎么自备、常见问题；后端各专题在 hub/packages/hub-bff/docs/（长对话、最近删除、改自己、语音与传文件、账本……）
```

各包里的 README、`hub/COMPAT.md` 是开发笔记，保留了一些历史代号，不是用户文档。

## 角色形象与许可边界

**MIT 只覆盖代码与文档。`shell/pets/` 目录下的角色素材采用 CC BY-NC-SA 4.0（署名、非商业、相同方式共享），版权属于各自作者，不在 MIT 范围内。**

- 仓库带六位，逐位的形象来源、原设、许可、来源地址、改动都写在 [shell/pets/CREDITS.md](shell/pets/CREDITS.md)：
  - 首席助理的「蓝毛小女仆」（DeepSeek 娘「大肥鱼」）：形象设计 B 站 @ZipZipPipe，动画素材来自开源项目 [PC2005-cloud/dsh-pet](https://github.com/PC2005-cloud/dsh-pet)，经 [hunmer/aboutme-pets](https://github.com/hunmer/aboutme-pets) 汇集；我们做了裁切和 4 倍超分。
  - 其余五位（Grok、GPT、Claude、千问、Gemini 的拟人形象）：**原样取自 [CrossPet](https://github.com/lokicorvus/crosspet) 的立绘**（字节没改，每个文件的 SHA-256 见 `shell/pets/MANIFEST-crosspet.txt`），该项目的 `characters/LICENSE.md` 明确允许转载与二创（CC BY-NC-SA 4.0）。原设作者 B 站 @ZipZipPipe 等，署名见 CREDITS。
- **非官方同人形象，与各 AI 公司无关；Claude、GPT、Grok、Gemini、Qwen、DeepSeek 等为各自公司的商标。**
- 别的角色（比如 hunmer/aboutme-pets 里另外生成的那批动作包）因为没有许可声明，**没有随仓库带**。
- 想商用，或者不想用这些形象：**删掉整个 `shell/pets/` 目录**，界面会自动换成自带的示意形象。
- **如果你是原作者并对使用方式有异议，请提 issue，我们会第一时间修改或移除。**
- 想用自己的角色包：见 [docs/角色包怎么自备.md](docs/角色包怎么自备.md)。

## 致谢

- DeepSeek Harness（MIT）：本项目运行在它之上；本仓库不含它的任何源码。
- CrossPet（lokicorvus 和贡献者）：站台桌宠的动作与状态机改编自它的代码（MIT，版权声明随附）；`shell/pets/` 里 Grok、GPT、Claude、千问、Gemini 五位的立绘取自它（CC BY-NC-SA 4.0，原设作者 B 站 @ZipZipPipe 等，署名见 [shell/pets/CREDITS.md](shell/pets/CREDITS.md)）。
- 角色形象「蓝毛小女仆」：ZipZipPipe（设计）、PC2005-cloud/dsh-pet（动画素材）、hunmer/aboutme-pets（汇集转码），CC BY-NC-SA 4.0，非官方同人，详见 [shell/pets/CREDITS.md](shell/pets/CREDITS.md)。
- Phosphor Icons（MIT）、以及一批只学了做法的开源项目，完整清单见 [CREDITS.md](CREDITS.md)。

## 许可证

代码与文档：[MIT](LICENSE)。`shell/pets/` 下的角色素材：CC BY-NC-SA 4.0（见 [shell/pets/LICENSE](shell/pets/LICENSE)），不在 MIT 范围内。变更记录见 [CHANGELOG.md](CHANGELOG.md)。
