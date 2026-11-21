# AID Studio — 开源 AI 漫剧与影视创作工作台

<a id="source-repositories"></a>

<p align="center">
  <a href="https://atomgit.com/shijue-aid/aid-studio"><strong>AtomGit</strong></a>&nbsp;&nbsp;<a href="https://atomgit.com/shijue-aid/aid-studio"><img src="https://atomgit.com/shijue-aid/aid-studio/star/badge.svg" alt="AtomGit Stars" height="20" align="absmiddle"></a>
  &ensp;·&ensp;
  <a href="https://github.com/shijue-aid/aid-studio"><strong>GitHub</strong></a>&nbsp;&nbsp;<a href="https://github.com/shijue-aid/aid-studio/stargazers"><img src="https://img.shields.io/github/stars/shijue-aid/aid-studio?style=flat&amp;logo=github&amp;label=Stars" alt="GitHub Stars" height="20" align="absmiddle"></a>
</p>

**简体中文** · [English](README.en.md)

AID Studio 是可自托管的开源影视创作工作台，适合做漫剧、短剧和短片。

[在线体验](https://www.aidstudio.com.cn/) · [快速开始](#快速开始) · [产品截图](#产品预览) · [使用教程](https://gzxxaitdb.feishu.cn/docx/LZ5zdesEgo1z4Mxc7OWc7zTHnJc) · [版本发布](https://github.com/shijue-aid/aid-studio/releases) · [交流与反馈](#交流与反馈)

<p align="center">
  <a href="#产品预览"><img src="references/product/product-home.jpg" alt="AID Studio 当前首页，展示剧本成片和自由画布入口" width="100%"></a><br>
  <sub>当前 AID Studio 首页 · <a href="#产品预览">查看工作台实景</a></sub>
</p>

## 交流与反馈

扫码加入 AID 开源交流群，交流部署、模型配置和使用问题。也可查看[获取帮助](SUPPORT.md)。

**本群仅仅为开源交流、技术支持群，无广告，无任何隐形消费。**

<p align="center">
  <img src="https://img.shields.io/badge/交流群说明-%E6%9C%AC%E7%BE%A4%E4%BB%85%E4%BB%85%E4%B8%BA%E5%BC%80%E6%BA%90%E4%BA%A4%E6%B5%81%E3%80%81%E6%8A%80%E6%9C%AF%E6%94%AF%E6%8C%81%E7%BE%A4%EF%BC%8C%E6%97%A0%E5%B9%BF%E5%91%8A%EF%BC%8C%E6%97%A0%E4%BB%BB%E4%BD%95%E9%9A%90%E5%BD%A2%E6%B6%88%E8%B4%B9%E3%80%82-d93025?style=for-the-badge" alt="本群仅仅为开源交流、技术支持群，无广告，无任何隐形消费。">
</p>

<p align="center">
  <a href="references/community-qr.png">
    <img src="references/community-qr.png" alt="AID 开源交流群二维码" width="220">
  </a><br>
  <sub>二维码未显示时，可点击图片查看原图。</sub>
</p>

## 核心能力

| 工作台 | 可以做什么 |
| --- | --- |
| **流程化创作** | 撰写或导入剧本，准备角色和场景素材，按分镜生成视频，再配音、同步音画并预览成片。 |
| **无限画布** | 用节点和连线编排文本、图片、视频、音频，复用素材并多人协作。 |
| **导演台** | 排机位、定构图和运镜轨迹，用机位监视器检查镜头。 |
| **3D 预演台** | 搭白模、布灯光、排动作，在时间轴上回放并录制预演片段。 |
| **管理后台** | 配置模型、计费和业务绑定，管理 Agent、Skill、计算节点和任务。 |

项目代码采用 [MIT 协议](LICENSE)。模型调用、存储和计算资源可能产生费用。

## 第一个漫剧项目

1. 管理员在「配置中心 → 模型与计费 → 模型管理」配置需要的模型，确认可用能力、业务绑定和计费后启用。
2. 在首页选择「剧本成片」，输入创作需求或导入已有剧本，再准备角色和场景素材。
3. 先完成一个镜头，核对分镜脚本和参考图，再生成视频。需要时添加音频和配音，预览后再扩展为整集。
4. 需要自由组合素材时，在「自由画布」用节点和连线组织文本、图像、视频和音频。需要推演空间关系时，可从画布打开 3D 预演台。

## 功能特性

- **素材与节点工具**：复用角色、场景和道具，可裁剪、打光、做分镜构图，也可截帧、裁音频和调速。
- **场景助手**：配置兼容的计算节点并启用后，可用文字或参考图搭建三维场景。
- **案例广场**：成片和画布可提交审核，审核通过后公开展示。
- **自行部署**：支持 Docker 和 systemd，后台可配置供应商、计费和任务并发。

## 产品预览

点击小图查看原图。创作端为示例作品，后台为测试环境。

### 用户端创作工作台

#### 流程化创作

| 分镜与视频生成 | 分镜片段回放 |
| :---: | :---: |
| <a href="references/product/workflow-stages.jpg"><img src="references/product/workflow-stages.jpg" alt="分镜与视频生成" width="420"></a> | <a href="references/product/workflow-video.jpg"><img src="references/product/workflow-video.jpg" alt="分镜片段回放" width="212"></a> |

#### 无限画布

| 「乌鸦喝水」画布与素材连线 | 添加节点 |
| :---: | :---: |
| <a href="references/product/infinite-canvas.jpg"><img src="references/product/infinite-canvas.jpg" alt="「乌鸦喝水」画布与素材连线" width="380"></a> | <a href="references/product/canvas-node-menu.jpg"><img src="references/product/canvas-node-menu.jpg" alt="添加节点" width="165"></a> |

<details>
<summary>查看节点工具</summary>

| 文本编辑与节点菜单 | 图片工具栏与分镜构图 |
| :---: | :---: |
| <a href="references/product/canvas-text-tools.jpg"><img src="references/product/canvas-text-tools.jpg" alt="文本编辑与节点菜单" width="212"></a> | <a href="references/product/canvas-image-tools.jpg"><img src="references/product/canvas-image-tools.jpg" alt="图片工具栏与分镜构图" width="420"></a> |

| 视频工具栏与生成设置 | 运镜广场 |
| :---: | :---: |
| <a href="references/product/canvas-video-tools.jpg"><img src="references/product/canvas-video-tools.jpg" alt="视频工具栏与生成设置" width="302"></a> | <a href="references/product/canvas-video-moves.jpg"><img src="references/product/canvas-video-moves.jpg" alt="运镜广场" width="212"></a> |

<p align="center">
  <a href="references/product/canvas-audio-tools.jpg"><img src="references/product/canvas-audio-tools.jpg" alt="音频波形与变速" width="335"></a><br>
  <sub>音频波形与变速</sub>
</p>

</details>

#### 导演台与 3D 预演台

| 导演视角与机位监视器 | 3D 预演时间轴 |
| :---: | :---: |
| <a href="references/product/previz-scene.jpg"><img src="references/product/previz-scene.jpg" alt="导演视角与机位监视器" width="315"></a> | <a href="references/product/previz-timeline.jpg"><img src="references/product/previz-timeline.jpg" alt="3D 预演时间轴" width="420"></a> |

### 管理后台

| 模型与计费 | Skill 管理 |
| :---: | :---: |
| <a href="references/product/admin-models.jpg"><img src="references/product/admin-models.jpg" alt="模型与计费" width="400"></a> | <a href="references/product/admin-skills.jpg"><img src="references/product/admin-skills.jpg" alt="Skill 管理" width="400"></a> |

<details>
<summary>查看算力、任务和 Agent 配置</summary>

| 计算节点 | 异常任务 |
| :---: | :---: |
| <a href="references/product/admin-compute.jpg"><img src="references/product/admin-compute.jpg" alt="计算节点" width="420"></a> | <a href="references/product/admin-tasks.jpg"><img src="references/product/admin-tasks.jpg" alt="异常任务" width="285"></a> |

<p align="center">
  <a href="references/product/admin-agents.jpg"><img src="references/product/admin-agents.jpg" alt="Agent 配置" width="300"></a><br>
  <sub>Agent 配置</sub>
</p>

</details>

## 快速开始

### 生产部署

选择 64 位 Linux。中间件同机部署且未启用 RocketMQ 时，最低需要 2 核 CPU、4 GB 内存、40 GB 磁盘。完整资源要求和外置中间件配置见[部署指南](deploy/README.md)。

下列命令下载统一安装器并在下载成功后运行。首次部署会先生成配置，确认后才开始初始化和启动服务。

```bash
cd /root && if command -v curl >/dev/null 2>&1; then curl -fL --retry 3 --connect-timeout 15 -o /root/aid-install.sh https://api.atomgit.com/api/v5/repos/shijue-aid/aid-studio/raw/deploy%2Faid.sh?ref=master || curl -fL --retry 3 --connect-timeout 15 -o /root/aid-install.sh https://raw.githubusercontent.com/shijue-aid/aid-studio/master/deploy/aid.sh; elif command -v wget >/dev/null 2>&1; then wget -O /root/aid-install.sh https://api.atomgit.com/api/v5/repos/shijue-aid/aid-studio/raw/deploy%2Faid.sh?ref=master || wget -O /root/aid-install.sh https://raw.githubusercontent.com/shijue-aid/aid-studio/master/deploy/aid.sh; else echo '请先安装 curl 或 wget'; exit 1; fi && sudo env AID_REMOTE_BOOTSTRAP=1 AID_RELEASE_CHANNEL=auto bash /root/aid-install.sh install
```

安装后运行 `sudo aid default` 查看实际访问地址和后台访问码。首次登录后及时修改管理员密码，再配置自己使用的供应商、模型能力、计费和业务入口。需要 AI 搭建 3D 场景时，在「配置中心 → 画布与预演台 → 计算节点」配置并启用对应资源。

### 本地开发

使用 JDK 17、Maven、Bash、OpenSSL 和 Docker。从仓库根目录启动开发用 MySQL 和 Redis，再加载生成的凭证并启动后端。Web 和后台依赖、环境变量与外置服务配置见[部署指南](deploy/README.md)。

```bash
bash deploy/docker/middleware.sh up -d
source deploy/docker/.middleware.env
export DB_NAME=aid_test DB_USERNAME=root DB_PASSWORD="$MYSQL_ROOT_PASSWORD"
mvn clean package -DskipTests
java -jar aid-admin/target/aid-admin.jar
```

### 在线升级

可从后台版本入口升级，也可运行 `sudo aid update` 后用 `sudo aid progress` 查看进度。升级会校验发布清单、备份并执行相应增量 SQL。生产环境升级与回滚请按[部署指南](deploy/README.md)的备份、容量和版本要求执行。

## 公开源码目录

公开版统一使用同一版本标签，包含服务端、Web、后台管理和升级相关文件。可从 [GitHub](https://github.com/shijue-aid/aid-studio) 或 [AtomGit](https://atomgit.com/shijue-aid/aid-studio) 获取源码。

| 位置 | 内容 |
| --- | --- |
| `/` | Java 服务端、官方初始化与升级 SQL |
| `frontend/web/` | Web 创作端 |
| `frontend/admin/` | React 管理后台 |
| `deploy/` | 部署脚本、运行说明与独立升级器 |

### 官方资产包

示例图片、音频和视频等官方素材随对应版本单独分发。资产包沿用原有对象键，可导入到本地存储、OSS 或 COS。下载入口和 SHA-256 以[官网](https://www.aidstudio.com.cn/)及对应版本说明为准。

## 文档导航

| 文档 | 内容 |
| --- | --- |
| [部署指南](deploy/README.md) | 安装、HTTPS、中间件、升级、备份和回滚 |
| [公开 Provider 接入指南](doc/公开Provider接入指南.md) | 模型能力声明、调用协议、任务与计费 |
| [贡献指南](CONTRIBUTING.md) | 反馈问题、验证代码与提交 PR |
| [帮助](SUPPORT.md) · [安全问题](SECURITY.md) | 部署与使用支持、私下报告漏洞 |
| [行为准则](CODE_OF_CONDUCT.md) | 社区协作 |

<a id="donate"></a>

## 赞赏支持

<p align="center">
  <a href="references/wechat-donation.jpg"><img src="references/wechat-donation.jpg" alt="AID 微信赞赏码" width="320"></a>
</p>

## 开源协议

项目采用 [MIT 协议](LICENSE)。版权归光子讯息（杭州）科技有限公司所有，第三方声明见 [NOTICE](NOTICE)。感谢 [RuoYi-Vue](https://gitee.com/y_project/RuoYi-Vue) 和 [Linux.do](https://linux.do/) 社区。
