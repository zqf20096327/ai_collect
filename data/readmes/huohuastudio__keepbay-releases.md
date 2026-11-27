<div align="center">
  <a href="https://keepbay.app">
    <img src="logo.svg" width="80" height="80" alt="Keepbay" />
  </a>
  <h1>Keepbay</h1>
  <p>自部署的 AI 资料管家：直接管理您现有的文件夹，用一句话找到证件和照片，重要日期到期前提醒。</p>

  <p>
    <a href="https://keepbay.app">官网</a> · <a href="https://keepbay.app/docs/">文档</a> · <a href="https://demo.keepbay.app">在线演示</a> · <a href="https://github.com/huohuastudio/keepbay-releases/releases/latest">下载</a> · <a href="https://github.com/huohuastudio/keepbay-releases/issues">反馈</a>
  </p>

  <p>
    <a href="https://github.com/huohuastudio/keepbay-releases/releases/latest"><img src="https://img.shields.io/github/v/release/huohuastudio/keepbay-releases?include_prereleases&label=%E6%9C%80%E6%96%B0%E7%89%88%E6%9C%AC" alt="最新版本" /></a>
  </p>
</div>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="screenshots/files-window-dark.webp" />
  <img src="screenshots/files-window-light.webp" alt="Keepbay 的文件管理界面" />
</picture>

> [!IMPORTANT]
> Keepbay 目前处于内测阶段（1.0.0-beta），功能和界面还会调整。用于存放重要资料前，请先做好备份。

## 在线演示

打开 [demo.keepbay.app](https://demo.keepbay.app)，用下面的帐号登录。演示站每小时恢复一次，可以随意操作。

| 帐号 | 密码 | 身份 |
|---|---|---|
| `demo` | `keepbay-demo` | 所有者 |
| `family` | `keepbay-demo` | 家庭成员 |

## 能做什么

- **文件留在原来的文件夹里。** Keepbay 只建立索引，不导入、不改名、不改变目录结构。其他程序照常读写这些文件夹，卸载 Keepbay 后文件不受影响。
- **用一句话搜索。** 按意思搜文档，按画面搜照片，搜照片里的文字；文件名支持拼音首字母。
- **重要日期提醒。** 从护照、合同、保单中读出到期日，确认后通过 Bark、邮件、企业微信等渠道提醒。
- **照片按时间、地点、人物浏览。** 跨文件夹的照片时间线、照片地图，按人物和宠物归类。
- **AI 默认在本地运行。** 搜索、识别文字、人脸都有本地模型，不向外发送数据。使用云端模型由您决定，每次调用都有记录。
- **完整的网盘功能。** 预览相机 RAW、视频、Office 文档和压缩包；分享链接、家庭成员权限、回收站、历史版本、WebDAV。

<table>
  <tr>
    <td width="33%">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="screenshots/search-dark.webp" />
        <img src="screenshots/search-light.webp" alt="搜索" />
      </picture>
    </td>
    <td width="33%">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="screenshots/reminders-dark.webp" />
        <img src="screenshots/reminders-light.webp" alt="重要日期提醒" />
      </picture>
    </td>
    <td width="33%">
      <picture>
        <source media="(prefers-color-scheme: dark)" srcset="screenshots/places-dark.webp" />
        <img src="screenshots/places-light.webp" alt="照片地图" />
      </picture>
    </td>
  </tr>
  <tr>
    <td align="center">搜索</td>
    <td align="center">重要日期提醒</td>
    <td align="center">照片地图</td>
  </tr>
</table>

完整的功能列表见[介绍](https://keepbay.app/docs/introduce#features)。

## 快速安装

用 Docker Compose 安装（x86_64、arm64）。把下面的内容保存为 `compose.yaml`，修改标明的几行：

```yaml
services:
  keepbay:
    image: 0xxb/keepbay:<版本>   # 修改：最新的版本号，见本仓库的 Releases
    container_name: keepbay
    restart: unless-stopped
    ports:
      - "8899:8899"
    environment:
      TZ: Asia/Shanghai
      PUID: "1000"        # 修改：文件夹属主的用户 ID 和组 ID
      PGID: "1000"
    volumes:
      - ./data:/data
      - /srv/files:/files # 修改：您的文件夹
```

```sh
sudo docker compose up -d
sudo docker logs keepbay    # 日志中有首次设置的令牌
```

然后在浏览器中打开 `http://<服务器地址>:8899`，按设置向导创建帐号，再添加文件夹。

也可以直接使用 Linux 安装包（x86_64、arm64，glibc 2.28 及以上），解压即可运行，不依赖数据库等外部服务。详细步骤见[安装](https://keepbay.app/docs/install)和 [Docker 安装](https://keepbay.app/docs/docker)。

## 免费版与专业版

免费版是一个完整的私有网盘，不限文件夹和文件数量。专业版增加 AI 功能和远程文件夹。

| | 免费版 | 专业版 |
|---|:---:|:---:|
| 文件管理、预览、分享、回收站、历史版本 | ✓ | ✓ |
| 照片时间线、照片地图、标签、文件名和全文搜索 | ✓ | ✓ |
| 两步验证、通行密钥、外部帐号登录 | ✓ | ✓ |
| 家庭成员 | 最多 2 人（含所有者） | 不限 |
| 按意思搜索文档和照片、搜照片里的文字 | — | ✓ |
| 认识的人和宠物 | — | ✓ |
| 重要日期提醒、收件箱自动整理、AI 标签、AI 桌面 | — | ✓ |
| 远程文件夹（S3、WebDAV、SFTP） | — | ✓ |

专业版 ¥199，永久使用，含 1 年更新，每个授权可用于 3 台设备。专业版将在 1.0.0 正式版发布时开始销售。

新安装的 Keepbay 可以免费试用专业版 7 天：在「系统设置 › 授权」中点「开启 7 天试用」，不需要注册帐号。价格和授权方式见[专业版](https://keepbay.app/docs/pro)。

## 与同类软件的区别

| | 侧重 | 文件存放的位置 | 开源 |
|---|---|---|:---:|
| Keepbay | 文件、照片、证件一起管理，AI 搜索和到期提醒 | 原来的文件夹，Keepbay 只建索引 | 否 |
| Nextcloud | 网盘加协作套件（日历、联系人、在线办公） | Nextcloud 的数据目录，也可以挂载外部存储 | 是 |
| Immich | 照片和视频，手机自动备份 | 上传到 Immich 的图库，也可以读取外部图库 | 是 |
| Paperless-ngx | 扫描件和文档归档，识别文字 | 导入后存入 Paperless 的存储目录 | 是 |

如果您主要需要手机相册自动备份，Immich 更合适；如果需要团队协作和日历、联系人，Nextcloud 更合适。

## 常见问题

**Keepbay 是开源的吗？**

不是。Keepbay 是商业软件，不开源，这个仓库用于发布安装包和收集反馈。免费版可以长期免费使用。

**需要定期联网验证授权吗？**

不需要。激活专业版时联网一次，证书保存在您的数据目录中，之后每次启动在本地验证。不能联网的设备可以离线激活。

**数据存在哪里？会发送给你们吗？**

文件在您自己的文件夹里；索引、缩略图和设置存在您服务器上的数据目录中。不需要注册帐号，数据不经过我们的服务器。程序中没有统计、遥测和崩溃上报。主动联网的几种情况和发送的内容，见[隐私与安全](https://keepbay.app/docs/privacy)。

**会改动或移动我的文件吗？**

只有两种情况：您指定为收件箱的文件夹，其中的文件按规则归档；或者您在 AI 桌面确认了它列出的计划。每一次移动都有记录，可以撤销。删除的文件先进回收站。

**手机能用吗？**

用手机浏览器访问即可，界面适配手机。也可以用支持 WebDAV 的文件管理器连接。

## 提交反馈

请在 [Issues](https://github.com/huohuastudio/keepbay-releases/issues/new/choose) 中选择类型后填写，提交前请先搜索已有的 Issue。在 Keepbay 的「系统设置 › 关于」中点「提交问题」，也可以打开 Issues 页面。

- **版本信息**：在「系统设置 › 关于」中点「复制版本信息」，粘贴到 Issue 中。
- **诊断信息**：在「系统设置 › 维护」的「诊断信息」中点「生成」，下载后作为附件上传。诊断信息不包括密钥、密码、会话和文件内容。「隐藏路径、文件名和网址」默认打开，Issue 是公开的，请保持这个选项打开。

诊断信息、日志或截图中有不便公开的内容时，请发邮件到 support@huohuastudio.com，并在 Issue 中注明已通过邮件发送。

## 安全问题

发现安全漏洞时，请不要提交公开的 Issue，请发邮件到 support@huohuastudio.com。
