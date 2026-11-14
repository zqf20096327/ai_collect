# 大肥鱼直播间 · git源宝工作室

<img src="web/yuanbao-cat.png" width="88" alt="git源宝小猫"> 

**养一只会聊天、会表演的鲸鱼娘。**  
Windows 本地虚拟直播工作室 · v0.7.2 · git源宝工作室出品

**Big Fat Fish Live Room** · [`gityuanbao/big-fat-fish-live-room`](https://github.com/gityuanbao/big-fat-fish-live-room) · [版本发布](https://github.com/gityuanbao/big-fat-fish-live-room/releases) · [反馈问题](https://github.com/gityuanbao/big-fat-fish-live-room/issues)

![大肥鱼工作室](docs/studio-preview.png)

观众发弹幕，大肥鱼用你配置的模型与音色回应，联动动作视频。先在虚拟直播间排练，再连接 B站 / 抖音与 OBS。

## 能做什么

- 回复模型 API、主播人设、观众昵称与简短口语回复。
- 语音 API、阿里百炼音色 ID、固定词句试听；可选本地 Piper 备用。
- 动作词库、触发词、起止时间、多个视频节点、播完恢复待机。
- 四向走动、转向、自由拖放、抓起落地、摇晕效果与随机才艺。
- 弹幕“点歌 + 歌名”，网易云播放可用歌曲，唱歌动作跟随播放。
- 可移动直播组件、横竖屏、OBS 浏览器源与本地联动测试。

## 下载与版本

当前提供 **v0.7.2 源码**，请按下方“从源码运行”启动。仓库包含角色动作视频，完整源码约 200 MB。

Windows 免安装运行包将单独放在 [Releases](https://github.com/gityuanbao/big-fat-fish-live-room/releases)，本次源码发布暂不包含 EXE。运行包发布后，完整解压 Windows ZIP，再双击 `启动大肥鱼.cmd` 或 `大肥鱼.exe`，无需安装 Python。首次解包会稍等片刻；保持控制台窗口打开。

若已运行旧版本，先关闭旧程序。默认界面是 http://127.0.0.1:8787/ 。旧端口被其他程序占用时，新版会提示，不会直接打开无关服务。

详细教程见 [便携版说明](docs/portable-readme.md)；运行包内附 `使用指南.html`，无需联网也能查看。

## 从源码运行

需要 Windows x64、Python 3.12，以及抖音登录所需的 Microsoft Edge。OBS 另行安装。

```powershell
git clone https://github.com/gityuanbao/big-fat-fish-live-room.git
cd big-fat-fish-live-room
powershell -ExecutionPolicy Bypass -File .\setup-dual.ps1
.\.venv\Scripts\python.exe main.py
```

也可以通过仓库的 **Code → Download ZIP** 下载源码，解压后在该目录运行后两条命令。

首次启动会创建本地 `config.json`。旧数据目录可通过 `DAFEIYU_DATA_DIR` 指定，兼容旧的 `WHALETALK_DATA_DIR`。不要将自己的配置文件提交到 GitHub。

## 第一次配置

1. “连接与回复”：填写自己的模型接口、模型名与 Key，设置主播人设，测试回复后保存。
2. “语音”：填语音服务 Key、对应模型和音色 ID。先试听；复刻音色使用本人或已获授权的声音。
3. “动作词库”：上传视频或使用内置动作。可设触发词及多个视频节点，按顺序播放。
4. “虚拟直播间测试”：输入观众昵称和弹幕，检查回复、语音、动作与回到待机。此步骤不需要直播间链接。
5. “直播间”：调整人物和组件位置，连接平台；在 OBS 启用 WebSocket 后同步场景。先本地录制检查，再推流。

模型与语音密钥分别配置，登录成功与弹幕连接成功分别检查。平台接口、音乐权限和 API 费用由各自账号决定，包内不含共享 Key、登录账号或歌曲文件。

## 开发与打包

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -q
Get-ChildItem tests -Filter *.cjs | ForEach-Object { node $_.FullName }
.\.venv\Scripts\python.exe -m pip install pyinstaller
powershell -ExecutionPolicy Bypass -File .\build-dual.ps1
.\.venv\Scripts\python.exe tools/verify_packaged.py
.\.venv\Scripts\python.exe tools/package_portable.py
.\.venv\Scripts\python.exe tools/package_github.py
```

源码与 Windows 运行包分开发布。参见 [GitHub 上传说明](docs/GITHUB.md)。运行包只使用公开默认配置，不读取作者的个人配置。

## 署名与许可

**大肥鱼的产品维护、新增和重写实现、源宝品牌界面：git源宝。**

**共创作者：[@2126431683a-netizen](https://github.com/2126431683a-netizen)。**

软件代码以 MIT 许可发布；使用与再分发保留相应版权声明。频道小猫、名称标识、角色视频和音色不随代码 MIT 许可授予通用商标或素材权利。项目并非 DeepSeek、网易云或直播平台的官方产品。

v0.7.2 更新见 [CHANGELOG.md](CHANGELOG.md)，v0.7.0 实现替换记录见 [REWRITE.md](docs/REWRITE.md)，项目沿革见 [UPSTREAM.md](UPSTREAM.md)。B站协议库 `blivedm` 及其他依赖保持各自作者署名和许可，详见 [第三方说明](THIRD-PARTY-NOTICES.md)。

反馈问题时请附版本号、复现步骤与已删除敏感信息的日志，不要公开 API Key 或 Cookie。
