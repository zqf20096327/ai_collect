# ChatGPT/AI 网站导航收集列表


本仓库旨在搜集整理当前流行可用的 AI 在线应用列表，以供关注AI应用与发展的同学参考使用。

**欢迎自荐，您的应用会获得更多的曝光机会。**

站点配置信息在 `site-info.json` 文件中设置，基本格式参考（为 `0` 的项不用填写）：

```ts
{
  "https://gpt.demo.com": {
      "type": "",           // 站点所属分类
      "source": "recommend",    // 站点来源
      "star": 3,                // 推荐星级，0-3。0 用于标记可访问但不可用、使用受限
      "needLogin": 1,           // 需要注册或绑定账号登录才可使用
      "desc": "描述",
      "title": "标题",
      "needPwd": 1,             // 是否需要密码、账号登录才能访问
      "needPay": 1,             // 付费应用
      "needVerify": 1,          // 需人工验证确认状态。-1 表示可用且无需程序验证
      "needVPN": 1,             // 需科学上网
      "hide": 1,                // 不显示在列表中，失效并将移除
      "repo": 'lzwme/gpt-demo', // 来源仓库
      "invalid": '20230310'    // 已失效，标注发现时间
  },
}
```

## 声明

以下站点列表来源于网络收集，若有侵权请提 [Issues](https://github.com/lzwme/chatgpt-nav/issues) 处理。

## 站点列表

```
⭐ 推荐星级。默认一星。免费、无需代理、无需 KEY 等，可增加星级
⛔ 0星标记。表示可访问，但功能暂不可用、需私有密钥、使用受限等
🔑 需输入API KEY。可使用自己的 KEY（应注意甄别、谨慎使用，避免您的 API KEY 泄露）
🚀 需代理。可代理登录、免费试用等
🔐 需要密码。需要私有密码、通过特殊渠道获取密码、认证码等
🧑‍💻 需登录。注册账号时请仔细甄别相关页面，不要使用常用密码
💰 需付费。请仔细识别，谨防受骗
❓ 需手动验证。访问异常、不确定是否失效、程序探测无法访问等
❌ 已失效。会在失效一段时间后移除
```

站点列表(837)：

### 国产大模型 (24)

1. [[⭐⭐⭐] https://bot.360.com](https://bot.360.com) **360智脑。** 360旗下的AI聊天助手
1. [[⭐⭐⭐] https://chat.sensetime.com](https://chat.sensetime.com) **商汤商量。** 商汤旗下的AI对话助手
1. [[⭐⭐⭐🧑‍💻] https://chatglm.cn](https://chatglm.cn) **智谱清言。** 全能 AI 助手，支持精通对话、写作与编程。为你答疑解惑，激发创意，更能理解图片与文档，提升学习与工作效率。
1. [[⭐⭐⭐🧑‍💻] https://cloud.siliconflow.cn/i/hDM9hDR6](https://cloud.siliconflow.cn/i/hDM9hDR6) **硅基流动。** 注册认证送16元全平台通用代金券。可使用GLM、Deepseek、Minmax等最新开源顶级模型
1. [[⭐⭐⭐🧑‍💻] https://hunyuan.tencent.com](https://hunyuan.tencent.com) **腾讯混元大模型。** 腾讯混元助手Chat
1. [[⭐⭐⭐🧑‍💻] https://image.hunyuan.tencent.com](https://image.hunyuan.tencent.com) **混元生图。** 腾讯混元生图
1. [[⭐⭐⭐🧑‍💻] https://kimi.moonshot.cn](https://kimi.moonshot.cn) **Kimi.ai。** Kimi智能助手能够支持约20万汉字的上下文输入，具备显著的中文优势，能够为用户提供回答问题、速读文件、整理资料、激发灵感、辅助创作等服务
1. [[⭐⭐⭐] https://klingai.kuaishou.com](https://klingai.kuaishou.com) **可灵AI。** 快手旗下的新一代AI创意生产力平台
1. [[⭐⭐⭐] https://longcat.chat](https://longcat.chat) **美团LongCat API开放平台。** 旗舰模型免费试用中！邀请新用户完成实名各得1000万Tokens！美团自研 LongCat 系列大模型API服务平台，基于MoE架构，兼容OpenAI和Anthropic API格式。支持深度思考、联网搜索、图像生成等能力。
1. [[⭐⭐⭐] https://pangu.huaweicloud.com](https://pangu.huaweicloud.com) **华为盘古。** 华为盘古大模型，重塑千行百业
1. [[⭐⭐⭐] https://platform.minimaxi.com](https://platform.minimaxi.com) **MiniMax 开放平台。** MiniMax 模型体系涵盖文本、语音、视频、图像与音乐五大方向。旗舰模型性能领先，助力开发者高效构建智能应用。无免费额度，提供了多种类型的开发者计划订阅套餐。
1. [[⭐⭐⭐] https://platform.xiaomimimo.com](https://platform.xiaomimimo.com) **Xiaomi Mimo开放平台。** 小米Mimo大模型开放平台。当前为公测阶段，提供免费无限制的模型调用服务。
1. [[⭐⭐⭐🧑‍💻] https://ppinfra.com/user/](https://ppinfra.com/user/) **派欧算力云。** 注册即送 50元 DeepSeek Token 代金券！派欧算力云提供全面的 AI 云端平台解决方案,包括模型 API、Serverless 和高性能 GPU 实例等,帮助您节省高达 50% 的成本,并同时加速 AI 产品的构建和业务发展,助力企业实现创新突破,赢得市场竞争优势。
1. [[⭐⭐⭐] https://www.deepseek.com](https://www.deepseek.com) **deepseek。** DeepSeek-V2是一款基于2千亿参数量的MoE（Mixture of Experts）模型的AI技术产品，它在对话官网和API上全面上线，提供领先性能和超低价格。该产品在中文综合能力（AlignBench）和英文综合能力（MT-Bench）的评测中表现出色，与GPT-4-Turbo等闭源模型处于同一梯队。DeepSeek-V2支持128K上下文的开源模型，而对话官网/API支持32K上下文。产品的主要优点包括即刻接入、能力卓越、价格低廉，并且兼容OpenAI API接口，提供丝滑的体验。
1. [[⭐⭐⭐] https://www.doubao.com/chat/](https://www.doubao.com/chat/) **豆包Chat。** 基于字节跳动研发的云雀大语言模型的Chat应用
1. [[⭐⭐⭐🧑‍💻] https://www.qiniu.com/ai/promotion/invited?cps_key=1h8fh294ny15e](https://www.qiniu.com/ai/promotion/invited?cps_key=1h8fh294ny15e) **七牛云。** 邀请注册多送1000万Token！提供Claude4.1 opus、Grok 4 Fast、Gemini、Kimi、Deepseek 等超全的当前国内外流行大模型 API 调用服务。
1. [[⭐⭐⭐] https://www.sensenova.cn/token-plan](https://www.sensenova.cn/token-plan) **商汤日日新Token Plan。** 商汤SenseNova Token Plan公测阶段免费使用！精选模型与用量方案，支持 Hermes Agent、OpenClaw 与 Cowork-Skills 办公场景。
1. [[⭐⭐⭐🧑‍💻] https://www.stepfun.com](https://www.stepfun.com) **阶跃AI。** 阶跃AI是阶跃星辰推出的一个聪明可靠的个人效率助手，可以帮你获取知识、查询信息、学习语言、创意写作、编写代码，在工作、学习、生活等各种场景下帮你解决问题。带你发现和理解世界
1. [[⭐⭐⭐] https://www.tongyi.com](https://www.tongyi.com) **通义千问。** 阿里达摩院提供的一个不断进化的AI大模型
1. [[⭐⭐⭐] https://xiaoyi.huawei.com/chat/](https://xiaoyi.huawei.com/chat/) **小艺。** 小艺是华为推出的智能助手，集成了自然语言处理和机器学习技术，能够提供聊天、写作、编程、翻译等多种功能。它基于深度学习模型，能够理解用户的问题并给出准确的回答。小艺的主要优点是功能丰富、响应速度快、智能化程度高。作为华为生态的一部分，小艺致力于为用户提供便捷的智能服务，提升用户体验。
1. [[⭐⭐⭐🧑‍💻] https://xinghuo.xfyun.cn](https://xinghuo.xfyun.cn) **讯飞星火。** 讯飞星火大模型
1. [[⭐⭐⭐🧑‍💻] https://yiyan.baidu.com](https://yiyan.baidu.com) **文心一言。** 百度全新知识增强大语言模型！使用百度账号登录即可
1. [[⭐⭐🧑‍💻] https://ai.360.cn](https://ai.360.cn) **360智脑。** 360 智脑 API 开放平台
1. [[⭐] https://www.baichuan-ai.com/chat](https://www.baichuan-ai.com/chat) **百川智能。** 百川智能旗下的AI对话助手

### AI 图像处理 (161)

1. [[⭐⭐⭐] https://arc.tencent.com/zh/ai-demos/faceRestoration](https://arc.tencent.com/zh/ai-demos/faceRestoration) **Arc Lab。** ARC是腾讯旗下ARC（Applied Research Center，应用研究中心）实验室推出的系列AI图片处理工具，目前提供了三项免费的AI图像功能：人像修复、人像抠图和动漫增强。
1. [[⭐⭐⭐] https://tongyi.aliyun.com/wanxiang/](https://tongyi.aliyun.com/wanxiang/) **通义万相。** 通义万相是一个不断进化的 AI 绘画创作模型。它能够刻削生千变，呈现出丰富多样的艺术作品。通义万相具有高度智能化的绘画能力，可以自主创作出优秀的绘画作品。它的优势在于通过深度学习算法不断进化，能够逐步提高绘画的质量和逼真度。通义万相的定价根据使用方式和使用场景而定，详情请登录官方网站了解。该产品定位于艺术创作领域，为艺术家、设计师和爱好者提供强大的创作工具。
1. [[⭐⭐⭐] https://www.midjourney.com](https://www.midjourney.com) **Midjourney。** Midjourney 是目前AI绘图最强大的存在
1. [[⭐⭐] https://d.design](https://d.design) **阿里堆友。** 堆友是Alibaba Design打造的设计师全成长周期服务平台，围绕品质、效率、技能、成就、收入五大用户价值布局平台能力，全力服务设计师，旨在成为设计师的好朋友。
1. [[⭐⭐] https://image3d.io](https://image3d.io) **Image3D。** AI 图片转 3D 模型工具，支持从单张图片生成 3D 资产，并导出 GLB、OBJ、STL、PLY 等格式。
1. [[⭐] https://ai.logo123.com](https://ai.logo123.com) **123LOGO生成器。** LOGO123 是一款超级智能好用的 Logo 在线设计生成器，为您提供免费公司 logo 设计制作。只需输入品牌名称就能免费在线生成公司 logo 设计及配套企业 VI，轻松打造您的个性品牌！我们还提供配套名片、企业 VI、专业出品、版权可商用等服务，帮助您打造完整的品牌形象。
1. [[⭐] https://ai.meitu.com/index](https://ai.meitu.com/index) **美图AI开放平台。** 美图推出的AI人脸图像处理平台
1. [[⭐] https://ai.nero.com/enhance](https://ai.nero.com/enhance) **Nero AI Image Upscaler。** Nero AI Image Upscaler是一款免费在线AI图像放大工具，支持jpg、png、bmp、webp等多种文件格式。它使用最先进的AI技术，可以将低分辨率的图像放大至高分辨率，同时保持图像细节和清晰度。Nero AI Image Upscaler可以在PC和移动设备上使用，是一款非常实用的图像处理工具。
1. [[⭐] https://aicolors.co](https://aicolors.co) **AIcolors。** 根据文本生成调色板，提供配色案例参考
1. [[⭐] https://aikiustudio.com/logo](https://aikiustudio.com/logo) **AI LogoBrainstorm。** AI LogoBrainstorm是一款使用人工智能技术的logo设计工具，根据您对品牌的描述生成定制化的logo选项。探索新的创意，找到完美的设计，体验我们先进的AI模型带来的革命性的logo设计体验！此外，AI LogoBrainstorm快速、高质量且价格实惠，无需设计技能。
1. [[⭐] https://app.deepbrain.io/dashboard](https://app.deepbrain.io/dashboard) **DeepBrain AI。** AI Studios提供了一个用户友好的仪表板，让用户可以轻松创建和管理AI项目。该平台可能包含多种AI工具和功能，以支持用户在图像、视频、音频等领域的创作和编辑。
1. [[⭐] https://app.recraft.ai/community](https://app.recraft.ai/community) **Recraft。** 便捷的AI生成矢量图像生成工具
1. [[⭐] https://appicons.ai](https://appicons.ai) **Appicons AI。** AI生成精致的App图标
1. [[⭐] https://arc.tencent.com/zh/ai-demos/humansegmentation](https://arc.tencent.com/zh/ai-demos/humansegmentation) **腾讯ARC官网。** 腾讯 ARC 官网是腾讯 PCG 旗下的应用研究中心，致力于探索和挑战智能媒体前沿技术。团队汇聚了国内外一流高端人才，主要研究领域涵盖视觉、音频、自然语言处理等，通过 AutoML、多模态和深度学习等方法提高算法性能。ARC 通过解耦业务需求和科研的机制，与业务团队合作，以业务需求和行业趋势为导向，不断探索、创新和突破。网站提供了关于 ARC 的使命、团队介绍、机制和领域等详细信息。
1. [[⭐] https://bgeraser.com](https://bgeraser.com) **Bg.Eraser。** 背景擦除器是一款使用AI技术快速、轻松地从照片中移除背景的工具。它能够帮助用户实现专业级的效果，增强图像的质量。背景擦除器还提供批量处理功能，节省用户大量的时间和精力。无论是用于产品照片、人像、图形、风景照片、动物照片还是物体，背景擦除器都能帮助用户实现理想的效果。
1. [[⭐] https://bgsub.cn](https://bgsub.cn) **BgSub。** BgSub 是一个完全自动化的图像处理工具，使用先进的人工智能技术自动消除或替换图像背景。它可以智能调整颜色，所有操作都在浏览器中完成，无需上传图像。BgSub 不仅能够节省时间，还能保护用户隐私。它适用于个人用户、网站 / 应用开发者、摄影师、电子商务、媒体从业者和市场营销人员等多个场景。
1. [[⭐] https://bigesj.com/ai-ppt/](https://bigesj.com/ai-ppt/) **比格PPT。** 比格PPT是一款功能强大的在线智能PPT设计SaaS平台。用户可以通过语言描述快速自动生成PPT,大大提升工作效率。平台拥有10000+精美PPT模板,覆盖商业、教育等多个行业场景。用户还可以利用平台强大的AI功能,一键优化PPT内容,实现高质量的演示文稿内容。平台提供了多种订阅方案,个人用户每月最低¥19元起,企业用户可享受更优惠价格
1. [[⭐] https://bigjpg.com](https://bigjpg.com) **Bigjpg。** AI图片在线无损放大
1. [[⭐] https://boolpic.fun/background-remover](https://boolpic.fun/background-remover) **Toolkit。** 多功能的AI图片处理工具箱
1. [[⭐] https://booltool.boolv.tech/home](https://booltool.boolv.tech/home) **Booltool。** 多合一AI图像处理网站，快速进行编辑修整
1. [[⭐] https://brandmark.io](https://brandmark.io) **BrandMark。** 最先进的人工智能Logo设计工具
1. [[⭐] https://cascadeur.com](https://cascadeur.com) **Cascadeur。** AI辅助制作3D关键帧动画
1. [[⭐] https://cgfaces.com/en](https://cgfaces.com/en) **CG Faces。** 免费的 AI 人像生成图片素材网站
1. [[⭐] https://chacha.so.com](https://chacha.so.com) **图查查。** 图查查是一个专业的图片版权查询平台，基于360搜索算法和图像AI识别能力，为广大运营、市场、广告、设计师等需要用到配图或者进行设计的用户服务。
1. [[⭐] https://chartdb.io](https://chartdb.io) **ChartDB。** ChartDB 是一个免费且开源的数据库设计编辑器，它允许用户通过单一查询快速生成数据库架构图。这个工具支持多种流行的数据库管理系统，如MySQL、MariaDB、PostgreSQL、Microsoft SQL Server和SQLite。它提供了一个直观的编辑器，用户可以轻松导入、编辑和导出数据库架构，同时支持AI生成DDL脚本，以便于数据库的管理和文档化。
1. [[⭐] https://claid.ai](https://claid.ai) **Claid AI Scene Creation。** Claid.ai是一个提供AI生成、增强和编辑产品图片的平台。它能够自动转换普通产品图片为具有拍摄品质的营销图片，提高图片的清晰度，去除背景，并创建令人惊叹的照片，从而提升转化率。Claid.ai支持生成多个适合品牌的产品图片，并提供统一的背景和图像大小，以适应不同的平台。用户可以通过API访问结果，实时获取编辑后的图片。Claid.ai还提供了多种功能，包括图片放大、智能去除背景、智能框架、AI颜色校正等，这些功能可以提高图片的质量和视觉效果。Claid.ai的目标是帮助企业实现图片的统一化和提升，从而提升转化率和销售业绩。
1. [[⭐] https://clipdrop.co](https://clipdrop.co) **Clipdrop。** 体验图像编辑的顶峰——水印移除AI，借助先进的人工智能技术轻松、精确地擦除水印，确保您的视觉效果保持完美清晰、无干扰。
1. [[⭐] https://designs.ai/cn](https://designs.ai/cn) **Designs AI。** 免费AI设计。使用生成型 AI 创建图像、视频等。利用人工智能的力量提升您的社交媒体营销水平。
1. [[⭐] https://dreamfusion3d.github.io](https://dreamfusion3d.github.io) **DreamFusion。** 谷歌推出的文本转3D模型
1. [[⭐] https://facecheck.id](https://facecheck.id) **Facecheck ID。** 利用人工智能技术通过照片在线查找人员。
1. [[⭐] https://flair.ai](https://flair.ai) **Flair AI。** 你的私人AI设计师！一键生成精美产品照片
1. [[⭐] https://free-trial.adcreative.ai/98krjvb7wdoq](https://free-trial.adcreative.ai/98krjvb7wdoq) **Adcreative.ai。** AD Creative是一款AI广告创作助手，通过智能算法和大数据分析，帮助用户快速生成优质广告创意。其功能包括智能创意生成、广告素材选择、广告分析和效果优化等。AD Creative具有高效、精准和创新的特点，适用于各种广告主和营销团队。定价灵活，可根据用户需求选择不同的套餐。定位于提升广告创作效率和效果的领先工具。
1. [[⭐] https://github.com/pAIrprogio/vscode-ui-sketcher](https://github.com/pAIrprogio/vscode-ui-sketcher) **UI Sketcher。** VSCode插件,借助GPT-4V的多模态能力,在插件中画出界面草图,就能生成一个基于ReactNative的UI界面
1. [[⭐] https://github.com/tldraw/make-real](https://github.com/tldraw/make-real) **Makereal Tldraw。** 通过草图生成可交互的UI界面和代码
1. [[⭐] https://haiper.ai](https://haiper.ai) **Haiper。** Haiper AI 是构建下一代内容创作的最佳感知基础模型的使命。它提供以下主要功能：文本转视频，图片动画，视频重绘，导演视角。Haiper AI 可以将文字内容和静态图片无缝转化为动态视频，只需拖放图像即可使其栩栩如生。使用 Haiper AI 的重绘工具，您可以轻松修改视频的颜色、纹理和元素，以提升视觉内容的品质。通过高级控制工具，您可以像导演一样调整镜头角度、灯光效果、角色姿势和物体运动。Haiper AI 适用于各种场景，如内容创作、设计、营销等。定价请参考官方网站。
1. [[⭐] https://hp.package-ai.jp](https://hp.package-ai.jp) **PLUG AI。** AI辅助包装设计！并对包装方案生成分析评估
1. [[⭐] https://huemint.com/brand-intersection](https://huemint.com/brand-intersection) **Huemint。** 用AI自定义和谐配色
1. [[⭐] https://icons8.com/bgremover](https://icons8.com/bgremover) **Background Remover。** AI 背景移除器通过人工智能检测图片主体、创建蒙版并消除背景。支持 PNG、JPG、WebP 格式，无需担心影响图片尺寸和质量。让您轻松制作透明背景图片。
1. [[⭐] https://img.logosc.cn](https://img.logosc.cn) **AI改图神器。** AI万能图片编辑器，在线修改图片颜色尺寸；智能抠图去水印；AI/EPS/PSD/SVG全格式支持的在线图片编辑器。
1. [[⭐] https://imgupscaler.com](https://imgupscaler.com) **Img Upscaler。** 使用最新的人工智能技术，通过批量处理将您的图像放大和增强。支持200%和400%的放大倍数，最高可达16000x16000像素分辨率。无需损失质量，放大您的图像。支持JPG、PNG和JPEG格式。起价3.9美元。
1. [[⭐] https://inpaintweb.lxfater.com](https://inpaintweb.lxfater.com) **Inpaint-web。** Inpaint-web 是一款永久免费的在线工具，只需一点击即可去除照片中的不想要对象，同时提供修复瑕疵功能。其独特的照片去除和修复功能让用户轻松实现照片编辑需求。用户无需下载安装任何软件，直接在网页上使用。Inpaint-web 定位于为用户提供便捷、高效的照片编辑解决方案。
1. [[⭐] https://insightface.ai](https://insightface.ai) **InsightFaceSwap。** 比Midjourney更丝滑的AI换脸工具
1. [[⭐] https://jimeng.jianying.com](https://jimeng.jianying.com) **即梦。** 即梦Dreamina是一款结合了AI技术的在线创作平台，它通过图片生成、智能画布和视频生成等功能，帮助用户将创意转化为视觉作品。该产品的主要优点在于简化了设计流程，使得非专业人士也能创作出高质量的图片和视频。产品背景信息显示，它由深圳市脸萌科技有限公司开发，定位于为广大创意工作者提供便捷的设计服务。目前产品提供免费试用，具体价格信息未在页面中明确。
1. [[⭐] https://jpghd.com/zh](https://jpghd.com/zh) **jpgHD。** 一键修复，让您的老照片变新照片
1. [[⭐] https://jpgrm.com](https://jpgrm.com) **jpgRM。** jpgRM 是一款利用 2024 年最先进人工智能技术的图片处理工具，可智能擦除图片中不需要的部分，填补背景内容，消除水印等。其主要优点在于高效快速地处理图片，并提供高质量的结果。定位于为用户提供便捷的图片编辑解决方案。
1. [[⭐] https://js.design/ai](https://js.design/ai) **即时设计。** 即时设计是一款AI生成式设计工具，通过输入文字即可生成相应的设计作品，帮助用户快速实现创意设计。产品定价根据用户需求而定，定位于提供高效便捷的设计解决方案。
1. [[⭐] https://ling.jd.com](https://ling.jd.com) **京东羚珑。** 京东羚珑是一站式内容生产与管理服务平台，提供商品主图设计、广告 banner 设计、店铺首页设计等功能。其主要优点包括丰富的模板选择、免费设计服务、高效便捷的操作流程。产品定位于为商家提供设计合作伙伴服务。
1. [[⭐] https://logocreatorai.com](https://logocreatorai.com) **LogoCreatorAI。** LogoCreatorAI是一款使用人工智能生成独特高质量标志设计的设计工具。它可以帮助初创公司、设计师和个体经营者生成专业的标志设计，节省时间和金钱。LogoCreatorAI使用简单，无需专业知识或技能。用户只需注册并选择适合自己需求的风格、概念和颜色，即可在几秒钟内获得定制的标志设计。用户可以从个人仪表板直接下载标志文件，并用于网站、名片和其他营销材料。
1. [[⭐] https://logodiffusion.com](https://logodiffusion.com) **Logo Diffusion。** Logo Diffusion是一款利用生成式人工智能来创建独特和定制的Logo的设计工具。用户可以通过文字提示、现有Logo或简单草图，快速生成符合自己需求的Logo设计。产品还提供2D转3D、图像转2D等功能，帮助用户实现品牌形象的多样化。Logo Diffusion定位于为用户提供简单、高效的Logo设计解决方案。
1. [[⭐] https://logofa.st](https://logofa.st) **LogoFast。** LogoFast是一个基于AI的免费在线标志制作工具,用户无需设计技能就可以在几秒内制作出漂亮和专业的标志。该产品拥有强大的AI功能,提供多种预设模板,支持自定义标志元素如图标、背景、大小、颜色等参数,操作简单快捷。主要优势是免费使用、效率高、易上手,适合新创企业、个人开发者等客户群体,可以助力他们快速高效地制作标志,减少设计成本。
1. [[⭐] https://logomakerr.ai](https://logomakerr.ai) **Logomakerr.ai。** LogoMaker是一个免费的AI logo制作工具，无需设计经验，只需几分钟就能创建出符合你需求的logo。它提供了数百个模板和AI生成的设计，帮助你快速开始你的品牌。LogoMaker已经得到了超过100万家企业的信任，拥有一切你需要的功能来打造你的品牌。
1. [[⭐] https://logomaster.ai](https://logomaster.ai) **Logomaster。** Logomaster.ai是一站式的专业Logo设计解决方案。用户可以轻松创建和编辑Logo，无需设计技能。使用Logomaster.ai，您可以在5分钟内获得专业Logo设计，而不是几天。我们提供多种定价方案，让您根据需求选择合适的方案。
1. [[⭐] https://logomaster.ai/de](https://logomaster.ai/de) **Logomaster。** Logomaster.ai ist Ihre All-in-One-Lösung für professionelles Logo-Design. Erstellen und bearbeiten Sie Logos mühelos, ohne Design-Fähigkeiten zu benötigen. Mit über 100 schönen Vorlagen können Sie in nur 5 Minuten ein einzigartiges und professionelles Logo erstellen. Logomaster.ai bietet auch eine Vielzahl von Funktionen, darunter Anpassungsmöglichkeiten für Schriftarten, Farben und Symbole. Die Nutzung von Logomaster.ai ist kostenlos, es stehen jedoch auch kostenpflichtige Abonnementpläne zur Verfügung, um Zugriff auf erweiterte Funktionen und hochauflösende Dateiformate zu erhalten. Mit Logomaster.ai können Sie Ihr Logo schnell und einfach erstellen, unabhängig von Ihrem Erfahrungsniveau.
1. [[⭐] https://looka.com](https://looka.com) **Looka。** AI辅助logo和品牌设计
1. [[⭐] https://magicstudio.com/zh](https://magicstudio.com/zh) **MagicStudio。** 图片处理必备效率神器！为你的图片提供神奇魔法
1. [[⭐] https://mastergo.com/ai](https://mastergo.com/ai) **MasterGo AI。** MasterGo AI使用人工智能辅助设计，开启数字交互新时代。
1. [[⭐] https://mastergo.com/upcoming-ai/apply](https://mastergo.com/upcoming-ai/apply) **MasterGo AI。** MasterGo AI 是一款基于人工智能技术的智能助手，具有强大的功能和优势。它可以帮助用户高效处理各种任务，并提供个性化的解决方案。MasterGo AI 定价合理，并提供灵活的定位选项，适用于个人用户和企业用户。
1. [[⭐] https://midlibrary.io](https://midlibrary.io) **Midlibrary。** 风格多样！实用超2000+MJ提示词资源
1. [[⭐] https://modao.cc/brand](https://modao.cc/brand) **墨刀AI。** 墨刀AI是国内知名产品设计协作平台「墨刀」最新推出的AI产品原型设计助手，帮助产品设计人高效实现和落地创意，激发无限创造力。
1. [[⭐] https://mokker.ai](https://mokker.ai) **Mokker AI。** Mokker 是一款利用人工智能技术，自动为电商平台或营销材料提供高质量产品图片的在线工具。使用时，只需上传几张产品的照片，Mokker 就会根据您的产品特征和风格，生成逼真的背景和场景。产品内置了一系列高质量模板，如家具、车辆、食物、珠宝等，可直接复用。当然，使用时也可以创建自己产品的专属模板，通过再次描述产品特征和需要在背景图中剔除的元素，最终生成更符合预期的图片效果。
1. [[⭐] https://nijijourney.com/zh](https://nijijourney.com/zh) **NijiJourney。** MJ出品！面向二次元风格，内容细致拿捏专业到位
1. [[⭐] https://nv-tlabs.github.io/GET3D](https://nv-tlabs.github.io/GET3D) **GET3D。** Nvidia的2D转3D模型
1. [[⭐] https://palette.fm](https://palette.fm) **Palette。** 用AI为黑白照片着色
1. [[⭐] https://palette.tone-row.com](https://palette.tone-row.com) **Palette。** 生成整套UI调色板
1. [[⭐] https://pebblely.com/zh/](https://pebblely.com/zh/) **Pebblely 宝贝丽。** Pebblely 宝贝丽是一款 AI 作图神器，专为电商而生。它能一键生成针对产品的精美场景图，可直接使用在淘宝、亚马逊、小红书等电商和社交媒体。每月免费 40 张场景图。自带 20 种默认主题，也支持自定义背景。适用于小企业家、广告公司和设计师，能在任何场景下生成创意图。深受多个品牌的信任和喜爱。
1. [[⭐] https://picwish.cn](https://picwish.cn) **佐糖。** 佐糖是一款智能 AI 图像处理平台，提供丰富的图像处理工具，包括抠图、去水印、模糊变清晰、图片裁剪、图片压缩、黑白照片上色等功能。操作简便，无需学习，一键处理图像。通过智能 AI 处理，提高工作效率，释放创造力。
1. [[⭐] https://picwish.com](https://picwish.com) **PicWish。** 这是一个免费的平台，可以为您的图片制作透明背景。一键去除背景，秒速合成透明照片。PicWish提供所有功能均免费。立即上传您的图片免费尝试！
1. [[⭐] https://pixcut.wondershare.com](https://pixcut.wondershare.com) **Pixcut。** Pixcut是一款自动免费去除图片背景的工具，新手只需点击几下就能使背景变透明。
1. [[⭐] https://pixian.ai](https://pixian.ai) **Pixian AI。** PixianAI是一款图像背景去除工具，可以以极低的价格获得出色的质量，在测试版期间完全免费。
1. [[⭐] https://pixlr.com/cn](https://pixlr.com/cn) **Pixlr。** Pixlr是一家提供基于云的照片编辑服务的供应商，为消费者和公司在浏览器中提供编辑功能。Pixlr提供了一个平台，可以进行各种第三方集成。
1. [[⭐] https://pixso.cn](https://pixso.cn) **Pixso AI。** 设计师只需用简短的文本描述，无需手动绘制或寻找现成素材，即可迅速生成图像内容。
1. [[⭐] https://placeit.net/logo-maker](https://placeit.net/logo-maker) **Placeit Logo Maker。** Placeit Logo Maker是一个在线商标制作工具，提供数千个商标模板，用户可以轻松地选择并编辑它们，无需雇佣昂贵的设计师即可创建完美的商标。该产品的优势在于简单易用，提供了丰富的商标模板和编辑工具，价格合理，适用于个人和企业用户。
1. [[⭐] https://plask.ai](https://plask.ai) **Plask。** AI捕捉运动！帮你制作流畅的3D动画
1. [[⭐] https://ppt.isheji.com](https://ppt.isheji.com) **爱设计PPT。** 爱设计PPT利用先进的AI技术,自动创建并优化PPT模版。爱设计的AI能为您生成适合的,高质量且独特的PPT模版。
1. [[⭐] https://promptomania.com](https://promptomania.com) **PromptoMania。** MJ和SD提示词生成器
1. [[⭐] https://qingtu.cn](https://qingtu.cn) **清图。** 在线修复！国产的 AI 图像处理工具
1. [[⭐] https://qoqo.ai](https://qoqo.ai) **QoQo。** AI快速创建用户旅程地图
1. [[⭐] https://remini.ai](https://remini.ai) **ReminiAI。** Remini使用创新的人工智能技术，将您的老照片转变为高清杰作。通过去模糊、降噪、修复老照片、图像放大、颜色修复、人脸增强、背景增强等功能，让您的照片更加清晰、细腻，达到专业级水平。Remini适用于社交平台、传承家族历史、打印服务、电商、教育、杂志等多个行业，让您的照片和视频内容更加出色。Remini还提供API支持，方便您将其集成到自己的产品中。下载Remini移动应用程序，随时随地使用AI对照片和视频进行增强。
1. [[⭐] https://removewatermark.ai](https://removewatermark.ai) **WatermarkRemoverAI。** Watermark Remover AI是一个在线图像水印删除工具,使用AI技术,只需单击一下即可自动识别并删除图像中的水印。它提供一键式操作,速度快,重建准确,可以批量处理多张照片。用户只需上传有水印的图片,系统即可智能识别水印区域并去除,输出清晰的无水印图像。该工具使用简单,删除效果专业,非常适合初学者或专业人士使用。
1. [[⭐] https://sora2watermarkremover.net](https://sora2watermarkremover.net) **Sora2 Watermark Remover。** 一款基于先进深度学习技术和计算机视觉模型的 AI 驱动 Web 应用，专为无缝去除 Sora 生成视频中的水印而设计。提供专业级的水印去除效果和直观的用户界面。
1. [[⭐] https://taishan.qq.com/brand/](https://taishan.qq.com/brand/) **智绘设计。** 智绘设计是一个多场景智能设计服务商，提供正版设计素材和丰富的场景，帮助用户创意无限。它包括以下主要功能：秒速创作，一键出图；智能封面，一键智能生成精美封面；AI视频剪辑，一键智能生成影片视频；智能抠图，一键分离图像画面中的主体内容；人像动漫化，一键生成个性化的二次元动漫形象。智绘做图定位于提供高效创作工具和丰富的设计素材，适用于个人和商业用户。
1. [[⭐] https://tldraw.dev](https://tldraw.dev) **tldraw.dev。** tldraw是一个为React开发者设计的无限画布SDK，它允许开发者在其产品中添加协作白板功能或创造新的基于画布的体验。该SDK包含组件、API和服务，支持开发者构建高性能、可定制的画布应用。tldraw以其强大的功能、实时协作能力和对开发者友好的设计而受到好评。它适用于需要在Web上实现复杂画布交互的各类应用，从个人项目到企业级解决方案。tldraw提供免费带有水印的版本，并提供付费版本以去除水印并获取额外支持。
1. [[⭐] https://tools.picsart.com](https://tools.picsart.com) **QuickTools By Picsart。** Picsart是全球最大的数字创作平台。其由人工智能驱动的工具使各个水平的创作者能够设计、编辑、绘制和分享照片和视频内容。
1. [[⭐] https://uizard.io/autodesigner](https://uizard.io/autodesigner) **Uizard。** 设计界 ChatGPT！利用AI生成多屏的UI界面
1. [[⭐] https://vectorizer.ai](https://vectorizer.ai) **Vectorize。** Vectorizer可以使用AI快速轻松地将JPEG和PNG位图转换为SVG矢量图。
1. [[⭐] https://wanxiang.aliyun.com](https://wanxiang.aliyun.com) **通义万相。** 通义万相是一个不断进化的 AI 绘画创作模型。它能够刻削生千变，呈现出丰富多样的艺术作品。通义万相具有高度智能化的绘画能力，可以自主创作出优秀的绘画作品。它的优势在于通过深度学习算法不断进化，能够逐步提高绘画的质量和逼真度。通义万相的定价根据使用方式和使用场景而定，详情请登录官方网站了解。该产品定位于艺术创作领域，为艺术家、设计师和爱好者提供强大的创作工具。
1. [[⭐] https://whimsical.com](https://whimsical.com) **Whimsical。** Whimsical是一个集图表、白板等多种功能于一体的视觉协作平台。用户可以使用Whimsical创建流程图、线框图、思维导图和文档，快速将想法变为现实。它可以帮助团队成员更好地协作，从而更快地构建出更好的产品。Whimsical还可以与Jira、GitHub、Notion、Figma和Slack等常用工具集成，提高工作效率。
1. [[⭐] https://withpoly.com](https://withpoly.com) **Poly。** 根据文本生成3D材质
1. [[⭐] https://www.acgnai.art](https://www.acgnai.art) **触手 AI 。** 触手 AI 绘画专业版是一款面向插画师、漫画师、设计师等专业用户的国产 AI 绘图平台。支持文生成图、图生成图、参考生成图、AI 模型训练等功能，用户可在基础风格模型上使用叠加模型，也可以收藏各类画风、IP、场景、人物、设计类模型。产品定位于提升专业用户的绘画效率和创作品质。
1. [[⭐] https://www.adobe.com/au/sensei/generative-ai/firefly.html](https://www.adobe.com/au/sensei/generative-ai/firefly.html) **Adobe Firefly。** Adobe Firefly 是由 Adobe 推出的基于生成式人工智能的创作工具。它可以通过简单的文字提示生成精美的图像、转换文字、玩转色彩等。Firefly 可以帮助创意人士释放想象力，创造出无尽的艺术作品。Firefly 目前处于测试阶段，预计在未来提供多种不同用途的 Firefly 模型。
1. [[⭐] https://www.adobe.com/express/create/logo](https://www.adobe.com/express/create/logo) **Adobe Express Logo Creator。** Adobe Express Logo Creator是一款免费的Logo制作工具，用户可以通过输入品牌或商业名称、选择喜欢的风格、图标和字体等，快速生成高质量的Logo。该工具还提供了丰富的动画效果和字体推荐功能，用户可以在在线编辑器中进一步定制Logo，并将其下载为高质量的PNG和JPG文件，方便在各种平台上使用。
1. [[⭐] https://www.ai.zitijia.com](https://www.ai.zitijia.com) **字体家AI神笔。** 造字神器！ 仅需8个汉字即可生成一套6K+中文字库
1. [[⭐] https://www.aiyou.art](https://www.aiyou.art) **艾绘。** 艾绘是一个结合了人工智能技术的绘本创作平台，它允许用户通过简单的输入来创作个性化的绘本故事。这个平台特别适合需要快速生成教育内容、品牌故事或个人创意作品的用户。艾绘通过其AI故事生成、AI绘画、图文编辑和仿真配音等功能，简化了绘本的创作流程，使得即使是没有专业设计或写作背景的用户也能轻松制作出高质量的绘本。产品背景信息显示，艾绘由湖南艾游互动科技有限公司开发，旨在通过技术降低创作门槛，激发创意。目前平台在公测期间，新用户注册赠送积分，可用于平台内的消费。
1. [[⭐] https://www.beautiful.ai](https://www.beautiful.ai) **Beautiful.ai。** Beautiful.ai是一个演示软件，为团队提供最佳设计、保持品牌一致性以及全球协作的功能。它应用先进的AI技术，使演示制作变得简单而美观。用户只需添加内容，Beautiful.ai会自动适应并应用出色的设计规则。不再需要在深夜调整文本和图片大小。每一个选择都能节省时间并带来出色的设计。
1. [[⭐] https://www.canva.cn](https://www.canva.cn) **Canva 可画。** Canva 可画是一款在线设计协作平台，提供海量的设计模板和素材，支持创建海报、简历、名片、Logo、PPT 等多种平面设计作图。用户可以个人使用或与团队共同合作，通过协同设计功能实时评论和协作设计，轻松创建并分享专业设计。
1. [[⭐] https://www.creati.studio](https://www.creati.studio) **AI Backdrop。** Viral AI Video Generator For Url, Image Or Text To Video
1. [[⭐] https://www.cutout.pro](https://www.cutout.pro) **Cutout Pro。** 全能视觉设计平台，包含 AI 照片和视频编辑工具。自动化背景移除、图像修复、平面设计等。
1. [[⭐] https://www.daftart.ai](https://www.daftart.ai) **Daft Art。** AI专辑封面图片生成器
1. [[⭐] https://www.designhill.com/tools/logo-maker](https://www.designhill.com/tools/logo-maker) **Designhill Logo Maker。** Designhill Logo Maker是一款AI-powered的在线logo制作工具，无需设计技能即可创建专业的logo。该工具拥有丰富的图形设计元素，包括字体、图标和图形，可以根据用户的喜好生成数百种设计。用户可以根据自己的品牌需求选择合适的logo样式、颜色和主题，并使用logo编辑器进行个性化修改。生成的logo可以下载为SVG、EPS、PNG和JPEG格式的高分辨率矢量文件，适用于印刷和数字版本。此外，该工具还提供品牌指南、24*7客户支持、彩色和透明背景的logo、黑白版本的logo以及100%可定制的logo等功能。Designhill Logo Maker适用于所有规模的企业和个人，是打造品牌形象的理想选择。
1. [[⭐] https://www.designify.com](https://www.designify.com) **Designify。** 免费在线抠图，识别内容，提供适合的合成设计
1. [[⭐] https://www.designkit.com](https://www.designkit.com) **美图设计室。** 美图设计室是美图秀秀旗下的智能设计在线协作平台，是一款平面设计工具和在线平面设计软件,提供海量海报模板,跨境电商模板,跨境电商banner,跨境电商主图,邀请函,公告通知,喜报,logo等免费设计素材和模板,可在线智能生成海报,一键换色,一键换装,一键去水印,图片高清修复,无损放大,抠图,拼图。
1. [[⭐] https://www.erase.bg](https://www.erase.bg) **Erase.bg。** Erase.bg是一款免费在线工具，可以去除人物、动物或物体图片的背景，并提供高分辨率的透明图片下载。无需信用卡，适用于电子商务和个人使用。
1. [[⭐] https://www.fabrie.cn/ai/imagine](https://www.fabrie.cn/ai/imagine) **Fabrie AI。** Fabrie AI是一款AI设计助手，提供线稿渲染、提升分辨率、去除图片背景、增强细节、调节权重、多种基础风格等功能。可用于工业设计、3D角色、游戏设计、人像、服装设计、二次元、动漫设计、建筑等领域。支持多种渲染模式和LoRA风格模型，可在社区案例中选择多样的风格模型。Fabrie AI旨在提高设计效率，让创意可视化，协助设计师快速迭代。定价方案灵活，支持免费试用。
1. [[⭐] https://www.florafauna.ai](https://www.florafauna.ai) **FLORA。** FLORA 是一个创意 AI 工具平台，将多种顶级文本、图像和视频 AI 模型连接在一个无限画布上，让用户能够以思维的速度进行创意创作。其核心优势在于整合多种 AI 模型，提供无缝的创作体验，能够帮助用户快速从想法到实现的转变。该产品主要面向创意工作者，如设计师、艺术家、视频创作者等，帮助他们提高创作效率和质量。目前 FLORA 提供免费试用，用户可以体验其强大的功能。
1. [[⭐] https://www.fotor.com/cn](https://www.fotor.com/cn) **Fotor。** Fotor是一款免费的在线照片编辑器，可以轻松编辑、裁剪、调整大小、添加效果和文字，创建拼贴等。
1. [[⭐] https://www.framer.com/ai](https://www.framer.com/ai) **Framer AI。** Framer AI是一个能够使用人工智能快速生成和发布网站的工具。通过提供详细信息，AI会生成独特的布局、文本和样式。您可以自由调整并删除不需要的部分，完全掌控网站的外观和功能。除了生成网站，Framer AI还提供了丰富的模板和资源库供用户使用。
1. [[⭐] https://www.goenhance.ai](https://www.goenhance.ai) **GoEnhance AI。** GoEnhance AI是一款基于人工智能的图像和视频增强工具。它可以实现视频到视频、图像增强和超分辨率scaling等功能。GoEnhance AI采用了最先进的深度学习算法,可以增强和上采样图像到极致的细节和高分辨率。它简单易用,功能强大,是创作者、设计师等用户释放创意的绝佳工具。
1. [[⭐] https://www.hama.app/zh](https://www.hama.app/zh) **Hama。** 使用轻松！一键无痕抹除画面内容
1. [[⭐] https://www.iconifyai.com](https://www.iconifyai.com) **Iconify。** IconifyAI是一款AI驱动的应用图标生成器，可以在几秒钟内为您的应用程序生成独特、漂亮、专业的图标。通过AI将文本转换为可直接使用的标识。
1. [[⭐] https://www.islide.cc](https://www.islide.cc) **iSlide。** iSlide 是一款简单、好用的 PPT 插件，拥有 30 万 + 原创可商用 PPT 模板、PPT 主题素材、PPT 案例、PPT 图表、PPT 图示、PPT 图标、PPT 插图和 800 万 + 正版图片。提供 38 个设计辅助实用功能，一键解决 PPT 设计制作中的各种难题。用户可通过 iSlide 快速找到符合需求的 PPT 素材和工具，提升 PPT 制作效率和专业度。
1. [[⭐] https://www.kaedim3d.com](https://www.kaedim3d.com) **KAEDIM。** 帮你迅速生成3D模型及纹理
1. [[⭐] https://www.khroma.co](https://www.khroma.co) **Khroma。** Khroma 利用人工智能学习您喜欢的颜色，并为您创建无限的调色板，帮助您快速发现、搜索和保存色彩组合。Khroma 的个性化算法训练神经网络，生成您喜欢的颜色，过滤您不喜欢的颜色。同时，还可以搜索和保存颜色组合，并获取颜色名称、hex 代码、RGB 值、CSS 代码以及 WCAG 辅助功能评分。
1. [[⭐] https://www.krea.ai/home](https://www.krea.ai/home) **Krea.ai。** KREA 是一款设计工具，拥有实时生成、AI 图像提升、AI 应用等功能。它能够帮助用户快速生成和增强图像，并提供多个简洁易用的 AI 应用。
1. [[⭐] https://www.laihua.com](https://www.laihua.com) **来画。** 来画是有创意的AI动画短视频制作平台，仅需几张图片，几段文字和声音简单组合， 即可在短时间内生成一个有趣的动画短视频。
1. [[⭐] https://www.logoai.com](https://www.logoai.com) **LogoAI。** LogoAi是一款AI助力的品牌构建平台，可以帮助您创建专业的Logo，设计相配套的形象，并通过符合品牌风格的社交媒体内容自动推广品牌。LogoAi的Logo设计引擎不仅理解Logo数据，还遵循最佳设计实践，确保Logo既美观又专业。从Logo模拟到Word和PPT模板，我们提供一切您需要的内容，让您的品牌更加出色。一键激活个人品牌中心，获得更一致的品牌视觉效果。选择数十种根据Logo样式和颜色自定义的名片设计。Facebook封面、Twitter头像和Instagram故事等社交媒体内容都是您品牌套餐的一部分。无论是招聘还是推广，您都可以自定义并下载您品牌的海报。
1. [[⭐] https://www.logobean.com](https://www.logobean.com) **logobean。** logobean是一款在线Logo制作工具，用户可以通过输入公司或品牌名称，快速生成多种Logo样式，并可自由编辑和调整。该产品提供高质量的PNG和SVG格式的Logo文件，以及100多种社交媒体平台的营销图片和品牌指南等。logobean的定价分为基础版和高级版，分别为29美元和49美元，用户可以根据自己的需求选择购买。
1. [[⭐] https://www.logopony.com](https://www.logopony.com) **LOGOPONY。** LOGOPONY是一个使用人工智能技术的在线 Logo 制作工具。它可以帮助您为您的业务、服务或项目创建专业的 Logo，提供无限次的定制修改。它的功能强大，操作简单，快速生成美观的 Logo 设计。一次购买，您将获得所有 Logo 文件以及终身无限次的编辑和重新下载。无需额外付费，享受一次付费的便利。
1. [[⭐] https://www.logosc.cn](https://www.logosc.cn) **标小智。** 标小智是一款智能LOGO在线设计生成器。只需输入品牌名称就能免费在线生成公司logo设计，商标设计，以及配套企业VI助您打造个性品牌。
1. [[⭐] https://www.mindshow.fun](https://www.mindshow.fun) **MindShow。** MindShow 是一款利用人工智能生成 PPT 模版的软件。它可以根据用户提供的文字内容，自动生成结构化的演示内容，大大节省排版和设计的时间。MindShow 提供多种主题和布局，用户可以随意切换和修改。使用 MindShow，用户可以在线演示或导出 PPTX 文件，方便灵活。MindShow 旨在帮助用户提升工作效率，解放他们的时间和精力，不再烦恼排版和设计。
1. [[⭐] https://www.modaiyun.com/mdy/ai](https://www.modaiyun.com/mdy/ai) **模袋云AI。** 模袋云AI是一款在线别墅设计神器。
1. [[⭐] https://www.muglife.com](https://www.muglife.com) **Mug Life。** Mug Life通过将计算机图形学专业知识与最新的计算机视觉技术相结合，创造出令人惊叹的3D角色。其技术分为三个阶段：拆解、动画和重构，结合社交平台，让用户能够连接和分享创作。
1. [[⭐] https://www.nolibox.com](https://www.nolibox.com) **图宇宙。** 图宇宙是计算美学是高品质的智能设计平台，致力于让每个人都能享受好设计。
1. [[⭐] https://www.noya.io](https://www.noya.io) **Noya。** 让线框图变成高保真设计
1. [[⭐] https://www.photorestore.io](https://www.photorestore.io) **PhotoRestore.io。** PhotoRestore.io 是一家提供免费 AI 照片修复服务的网站，利用先进的算法修复模糊、褪色或损坏的照片，为用户呈现清晰高质量的图像。用户可在保护隐私和数据安全的前提下体验恢复照片的魔法，创造代代传承的珍贵回忆。
1. [[⭐] https://www.photoroom.com](https://www.photoroom.com) **PhotoRoom。** 在几秒钟内创建高品质的图像。只需轻点一下，即可去除背景并合成一个能展示产品或模特的图像。PhotoRoom赋予每个人设计超能力，因为你编辑的是物体而不是像素。PhotoRoom是一款图像编辑应用程序，让您通过编辑物体来捕捉、编辑和混合图像。
1. [[⭐] https://www.piccopilot.com](https://www.piccopilot.com) **Pic Copilot。** Pic Copilot是一个利用图像生成模型为电商提供的AI驱动图片优化工具。它能够通过对大量图片点击量数据的训练,有效提高图片的点击转化率,从而优化电商的营销效果。其关键优势是提高图片的点击转化率,从而提升电商营销效果。它是阿里巴巴团队训练的数据结果,能够显著优化图片的点击转化表现。
1. [[⭐] https://www.picwish.com](https://www.picwish.com) **PicWish。** PicWish是一个人工智能驱动的图像处理平台,帮助用户高效编辑图片。它提供强大的工具,如背景移除、图像放大、照片修复、JPG转换器、图像压缩、人脸增强和照片增强。使用PicWish,用户可以一键移除背景、去模糊图像、增强分辨率和修复缺陷。该平台非常易于上手,没有学习曲线。它通过使照片编辑简单又专业,释放了创造力。PicWish极大地提高了图形设计师、摄影师、电子商务卖家和营销人员的工作效率。
1. [[⭐] https://www.polymet.ai](https://www.polymet.ai) **Polymet。** Polymet是一个利用人工智能技术帮助用户快速从创意到原型的设计工具。它通过连接Figma和代码库，使用户能够快速设计并迭代，同时导出符合设计模式的生产就绪代码。Polymet的主要优点包括提高设计和迭代速度，无缝连接设计工具和代码库，以及通过AI辅助设计，减少手动编码工作量，从而加速产品上市时间。
1. [[⭐] https://www.ponzu.gg](https://www.ponzu.gg) **Ponzu。** AI生成3D无缝贴图纹理
1. [[⭐] https://www.productai.photo](https://www.productai.photo) **ProductAI。** ProductAI是一个AI驱动的产品图片生成平台。用户只需上传产品图片,选择场景模板,就可以在几分钟内生成高质量的商业产品图片。该平台采用了最先进的生成式AI技术,无需用户进行复杂的提示,即可自动生成逼真的产品渲染图。该服务面向各类创业公司、品牌商、平面设计师等用户群体,可以显著提高他们内容生产的效率,降低产品图片的成本。
1. [[⭐] https://www.quququ.cn](https://www.quququ.cn) **水印一键去去去。** 水印一键去去去是一款智能 AI 图像处理网站，提供在线去水印、自动抠图、模糊照片变清晰等功能。采用人工智能技术，支持批量去除图片中的文字、标志，无痕、不糊图！
1. [[⭐] https://www.remove.bg](https://www.remove.bg) **Remove.bg。** 去背神器是一款可以一键去除图片背景的工具。它通过智能算法分析图片，将背景与主体分离，实现快速、准确的去背效果。该工具操作简单，无需任何设计经验，适用于个人用户和设计专业人士。去背神器提供免费试用和付费套餐，付费套餐提供更多高级功能和更大的使用额度。
1. [[⭐] https://www.restorephotos.io](https://www.restorephotos.io) **Restorephoto。** 效果惊艳的AI修复面容模糊的照片
1. [[⭐] https://www.runwayml.com](https://www.runwayml.com) **Runwayml。** Runway是一家应用人工智能研究公司，塑造着艺术、娱乐和人类创造力的下一个时代。我们提供多模态AI系统，帮助实现人类创造力的新纪元。
1. [[⭐] https://www.shuiyinyun.com](https://www.shuiyinyun.com) **水印云。** 水印云是一款集图片去水印等多功能去水印软件，采用先进的 AI 技术，能快速识别并删除照片中的文字、logo 等不需要的内容，保持高清画质。
1. [[⭐] https://www.sloyd.ai](https://www.sloyd.ai) **Sloyd。** 快速生成3D游戏资产
1. [[⭐] https://www.tracejourney.com](https://www.tracejourney.com) **Tracejourney。** 拯救MJ渣画质！图片一键转矢量
1. [[⭐] https://www.upscale.media/zh](https://www.upscale.media/zh) **Upscale media。** AI图片放大增强工具使用先进的人工智能技术，可将图像放大至2倍或4倍，同时保留纹理与细节。提供超分辨率处理，让您的图像焕发新生。我们有免费使用的选项，也提供不同套餐供个人和企业用户选择。欢迎访问官方网站了解更多信息。
1. [[⭐] https://www.upscayl.org](https://www.upscayl.org) **Upscayl。** 模糊图片秒变超清！开源免费 AI 图片无损放大工具
1. [[⭐] https://www.usegalileo.ai](https://www.usegalileo.ai) **Galileo AI。** AI生成可编辑的UI界面
1. [[⭐] https://www.usesuperflow.com](https://www.usesuperflow.com) **Superflow。** AI辅助高效网站协作设计
1. [[⭐] https://www.visily.ai](https://www.visily.ai) **Visily。** 实用！AI轻松将手绘线框转换为高保真度
1. [[⭐] https://www.whee.com](https://www.whee.com) **美图WHEE。** WHEE是一款AI绘画与图片生成器，提供一站式AI视觉创作服务。
1. [[⭐] https://www.wix.com/logo/maker](https://www.wix.com/logo/maker) **Wix Logo Maker。** Wix Logo Maker 是一款由人工智能驱动的在线设计工具，允许你免费创建和定制专业 Logo。通过回答几个简单问题，即可获得符合你需求的独特 Logo。
1. [[⭐] https://www.x-design.com](https://www.x-design.com) **美图 AI PPT。** 美图设计室是一款由中国互联网公司美图公司开发的图像处理、照片编辑和设计软件。
1. [[⭐] https://www.yijianlogo.com](https://www.yijianlogo.com) **一键Logo设计。** 一键Logo设计是一款基于AI大数据计算的智能设计生成器，只需简单输入名称口号，选择行业偏好，即可一键生成LOGO。所有元素均可调整修改，多种格式文件均可下载导出。一次购买长期使用，各种模板字体均可商用。适用于需要快速生成LOGO的个人、企业、团队等用户。
1. [[⭐] https://www.youchuan.com](https://www.youchuan.com) **悠船。** 悠船是Midjourney国内中文版本人工智能图像生成桌面客户端软件。它可以通过文字描述来生成图像,支持团队协作和高级控制,提供多种定价方案。主要功能包括文生图、协作创作、控制面板等。适合创意工作者、设计师、艺术家等群体使用,可以提高创意效率,激发灵感。
1. [[⭐] https://www.ysdaima.com](https://www.ysdaima.com) **颜色代码表。** 颜色代码表是一个为设计师和开发者提供一站式色彩解决方案的专业网站。运用机器学习技术，为您推荐最适合的配色方案AI辅助配色。它基于色彩理论，提供多种颜色工具，包括颜色代码转换、配色方案生成、渐变色生成等，帮助用户快速高效地完成设计工作。该网站支持多种颜色格式，并提供代码导出功能，方便用户将颜色方案直接应用到项目中。此外，它还符合WCAG 2.1标准，确保配色方案的无障碍设计。
1. [[⭐] https://www.zmo.ai](https://www.zmo.ai) **ZMO.AI。** ZMO可以轻松的生成令人惊叹的动漫、艺术或图像。
1. [[⭐] https://yige.baidu.com](https://yige.baidu.com) **文心一格。** 百度旗下AI艺术和创意辅助平台
1. [[⭐] https://yunxiu.meitu.com/home](https://yunxiu.meitu.com/home) **美图云修。** 商业级AI影像处理工具
1. [[⭐⭐💰] https://remove-watermark.org](https://remove-watermark.org) **iPurix - 轻松去除任何水印。** 几秒钟内获得干净、专业的图片。轻松移除水印——无需 Photoshop 技能
1. [[🚀] https://changestyleai.com](https://changestyleai.com) **Change Style AI。** 人工智能多风格肖像生成器！能够AI生成30种照片
1. [[🚀] https://creator.nightcafe.studio](https://creator.nightcafe.studio) **NightCafe。** 用AI生成惊艳的艺术品
1. [[🚀] https://designer.microsoft.com](https://designer.microsoft.com) **Microsoft Designer。** 微软推出的AI平面设计工具，实现快速完成设计加工。中国区不可用。
1. [[🚀] https://getimg.ai](https://getimg.ai) **Getimg。** 多功能AI图片编辑工具，让文字变成吸睛的视觉图像
1. [[🚀] https://lumalabs.ai](https://lumalabs.ai) **Luma Labs。** 将视频转为游戏资产
1. [[🚀] https://openai.com/research/dall-e](https://openai.com/research/dall-e) **DALL·E2。** OpenAI出品的绘画工具
1. [[🚀] https://skybox.blockadelabs.com](https://skybox.blockadelabs.com) **Text to Skybox。** AI生成360°无缝环境贴图
1. [[🚀] https://waifulabs.com](https://waifulabs.com) **WaifuLabs。** 一键生成动漫二次元头像
1. [[🚀] https://www.canva.com/ai-image-generator](https://www.canva.com/ai-image-generator) **Canva。** 将文字和短语变成美丽的图片。

### AI 视频生成 (97)

1. [[⭐⭐⭐] https://aivideo.hunyuan.tencent.com](https://aivideo.hunyuan.tencent.com) **腾讯混元文生视频。** 腾讯混元文生视频（HunyuanVideo）是一款突破性的视频生成模型，它拥有130亿参数，是目前开源模型中参数最多、性能最强的文生视频大模型。该模型能够生成具有较强物理准确性和一致性镜头的视频，提供超写实的视觉体验，并在真实与虚拟风格之间自由转换。它具备导演级运镜能力，实现艺术镜头的无缝衔接，完美融合真实效果与虚拟场景。同时，HunyuanVideo遵循物理定律，大幅降低违和感，并通过原生切镜和连续动作的设计，用户只需简单指令即可完成流畅创作，激发无限创意与灵感。
1. [[⭐⭐⭐] https://chat.qwen.ai](https://chat.qwen.ai) **Qwen Chat。** Qwen Chat offers comprehensive functionality spanning chatbot, image and video understanding, image generation, document processing, web search integration, tool utilization, and artifacts.
1. [[⭐⭐⭐🧑‍💻] https://chatglm.cn](https://chatglm.cn) **智谱清言。** 全能 AI 助手，支持精通对话、写作与编程。为你答疑解惑，激发创意，更能理解图片与文档，提升学习与工作效率。
1. [[⭐⭐⭐] https://kling.kuaishou.com](https://kling.kuaishou.com) **可灵大模型。** 可灵大模型是一款具备强大视频生成能力的自研大模型，采用先进的技术实现长达 2 分钟视频生成、模拟物理世界特性、概念组合能力等，可生成电影级画面。
1. [[⭐⭐⭐] https://klingai.kuaishou.com](https://klingai.kuaishou.com) **可灵AI。** 快手旗下的新一代AI创意生产力平台
1. [[⭐⭐⭐] https://runwayml.com](https://runwayml.com) **Runway。** Runway提供一系列易于使用的工具和平台，利用人工智能技术创造出令人惊叹的艺术作品和创意内容。他们的技术可以用于图像生成、视频编辑、音频合成、文字生成等多个创作领域。
1. [[⭐⭐] https://hailuoai.video](https://hailuoai.video) **Hailuo AI。** Hailuo AI Video Generator 是一款利用人工智能技术，根据文本提示自动生成视频内容的工具。它通过深度学习算法，将用户的文字描述转化为视觉图像，极大地简化了视频制作流程，提高了创作效率。该产品适用于需要快速生成视频内容的个人和企业，特别是在广告、社交媒体内容制作和电影预览等领域。
1. [[⭐⭐] https://ttsmaker.cn](https://ttsmaker.cn) **TTSMaker马克配音。** 免费的在线文本转语音神器
1. [[⭐] https://ai.invideo.io](https://ai.invideo.io) **InVideo。** 利用invideo AI，您可以立即将任何内容或想法转化为视频。
1. [[⭐] https://ai.jurilu.com](https://ai.jurilu.com) **巨日禄AI。** 巨日禄AI是一款全网性能卓越的故事AI绘画转视频工具，旨在让0基础小白也能轻松上手，快速实现从文案到视频的制作。该工具通过分析大量剧本数据和影视作品，为用户提供各种类型的故事情节和角色设置，帮助用户快速找到灵感，减少构思剧本的困难和犹豫。无需本地部署，快速出图，支持配音配乐，一站式解决小说、漫画推文等需求。角色固定，画风统一，提供多种风格选择。AI自动解析分镜，解析提示词，操作简单流畅，即使零基础小白也能轻松上手，做出精美的视频作品。
1. [[⭐] https://aigc.baidu.com](https://aigc.baidu.com) **百度度加创作工具。** 百度旗下产品，打造人人可用的AI创作工具
1. [[⭐] https://app.artflow.ai](https://app.artflow.ai) **Artflow AI。** Artflow.ai可以在浏览器中借助人工智能帮助你创建独特的动画故事，包括原创角色、场景和对话。让你的创意流淌，以全新的方式呈现你的故事。
1. [[⭐] https://app.deepbrain.io/dashboard](https://app.deepbrain.io/dashboard) **DeepBrain AI。** AI Studios提供了一个用户友好的仪表板，让用户可以轻松创建和管理AI项目。该平台可能包含多种AI工具和功能，以支持用户在图像、视频、音频等领域的创作和编辑。
1. [[⭐] https://audo.ai](https://audo.ai) **Audo Studio。** 听起来很棒！AI一键清除音频背景杂音
1. [[⭐] https://bibigpt.co](https://bibigpt.co) **BibiGPT。** 一键总结B站音视频内容
1. [[⭐] https://clipchamp.com/zh-hans](https://clipchamp.com/zh-hans) **Clipchamp。** 将文本转为视频旁白！几分钟即可创建导出视频。支持免费试用
1. [[⭐] https://clone.ttk.ink](https://clone.ttk.ink) **AI数字人分身系统。** 小狐狸AI数字人分身系统是一款结合了人工智能技术的数字人口型同步产品，支持无限多开和贴牌OEM，适用于需要虚拟形象进行口型同步互动的场景。该产品背景基于人工智能技术的发展，特别是在虚拟主播和在线教育领域的应用需求日益增长。产品价格为3580元，定位于中高端市场，主要优点包括完全开源、支持自主二次开发和定制二次开发，以及免费搭建服务。
1. [[⭐] https://colossyan.com](https://colossyan.com) **Colossyan Creator。** Colossyan Creator 是一款 AI 视频生成器，能够从文本快速生成 AI 视频。它提供了丰富的功能，包括根据文本创建学习视频、将 PDF 和 PPT 转化为视频、选择多样的 AI 主持人、自动翻译为多种语言等。Colossyan Creator 可广泛应用于企业学习、培训以及企业内部沟通等场景。定价方面，请咨询官方网站了解详细信息。
1. [[⭐] https://creatorkit.com/ai-product-photos](https://creatorkit.com/ai-product-photos) **AI Product Photos。** AI产品照片生成器是一个能够在几秒钟内生成增加销售的产品图片和照片的工具。它可以将产品图片转化为专业的产品照片，提高销售效果。使用这个工具，您可以添加AI背景，避免标签模糊或形状变化的问题。我们的AI照片生成器采用了全新的文本到图像扩散模型，专门为销售进行了训练和优化。您可以从Shopify中直接生成照片，并将其与我们的视频模板配合使用。生成的产品图片可以免费使用，并且您只需要为您真正喜欢的图片付费。
1. [[⭐] https://democreator.wondershare.com](https://democreator.wondershare.com) **DemoCreator。** DemoCreator可以记录您屏幕上的所有内容，可以使视频更具创意。可以平移和缩放，实时屏幕绘制，使用绿幕技术等等。
1. [[⭐] https://designs.ai/cn](https://designs.ai/cn) **Designs AI。** 免费AI设计。使用生成型 AI 创建图像、视频等。利用人工智能的力量提升您的社交媒体营销水平。
1. [[⭐] https://enriccorona.github.io/vlogger/](https://enriccorona.github.io/vlogger/) **VLOGGER。** VLOGGER是一种从单张人物输入图像生成文本和音频驱动的讲话人类视频的方法，它建立在最近生成扩散模型的成功基础上。我们的方法包括1)一个随机的人类到3D运动扩散模型，以及2)一个新颖的基于扩散的架构，通过时间和空间控制增强文本到图像模型。这种方法能够生成长度可变的高质量视频，并且通过对人类面部和身体的高级表达方式轻松可控。与以前的工作不同，我们的方法不需要为每个人训练，也不依赖于人脸检测和裁剪，生成完整的图像（而不仅仅是面部或嘴唇），并考虑到正确合成交流人类所需的广泛场景（例如可见的躯干或多样性主体身份）。
1. [[⭐] https://fancy.tech](https://fancy.tech) **Fancy Tech。** FancyTech是一个使用人工智能生成时尚风格的平台。通过AI视频和AI图像工具，用户可以上传自己的服装选择，并将其与各种背景合并，从而观察其风格效果。FancyTech让时尚创作变得简单有趣，无论是个人使用还是商业应用都能得到满足。
1. [[⭐] https://fanyi.caiyunapp.com](https://fanyi.caiyunapp.com) **彩云小译。** 兼具“你边说，我边译”的字字幕翻译功能。包括文字翻译、文档翻译、网页翻译、术语库、浏览器插件和双语对照服务
1. [[⭐] https://filmora.wondershare.com](https://filmora.wondershare.com) **Filmora。** Wondershare Filmora是一款简单的视频编辑器，可让您在Windows和Mac上编辑视频和音频。下载Filmora创建带有标题、转场和创意视觉效果的令人惊叹的影片。
1. [[⭐] https://fliki.ai](https://fliki.ai) **Fliki。** 高效帮用户创建视频，具有文本转语音功能
1. [[⭐] https://fullpeace.cn](https://fullpeace.cn) **风平智能。** 风平 IP 智造平台是基于 AIGC 的智能化 IP 打造平台，致力于提供虚拟数字人定制、AI 短视频内容生产和数字人直播的一站式解决方案。通过结合领先的 AI 技术，平台实现了数字人的高质量生产和互动能力，为用户打造全新的数字人 IP 体验。
1. [[⭐] https://gifshift.xyz](https://gifshift.xyz) **GifShift。** GifShift提供了一个简单的三步流程，用户可以上传GIF或从图库中选择一个，然后输入描述性的提示，以生成具有标志性角色或风格的新GIF版本。该服务由fal.ai提供支持。
1. [[⭐] https://github.com/Boese0601/MagicDance](https://github.com/Boese0601/MagicDance) **MagicDance。** MagicDance是一种新颖有效的方法，可以生成逼真的人类视频，实现生动的动作和面部表情转移，以及一致的2D卡通风格动画零调优生成。通过MagicDance，我们可以精确生成外观一致的结果，而原始的T2I模型（如稳定扩散和ControlNet）很难准确地保持主题身份信息。此外，我们提出的模块可以被视为原始T2I模型的扩展/插件，而不需要修改其预训练权重。
1. [[⭐] https://github.com/Picsart-AI-Research/StreamingT2V](https://github.com/Picsart-AI-Research/StreamingT2V) **StreamingT2V。** StreamingT2V 是一种先进的自回归技术，可以创建具有丰富动态运动的长视频，没有任何停滞。它确保视频中的时间一致性，与描述性文本紧密对齐，并保持高帧级图像质量。
1. [[⭐] https://github.com/Zejun-Yang/AniPortrait](https://github.com/Zejun-Yang/AniPortrait) **AniPortrait。** AniPortrait是一个根据音频和图像输入生成会说话、唱歌的动态视频的项目。它能够根据音频和静态人脸图片生成逼真的人脸动画，口型保持一致。支持多种语言和面部重绘、头部姿势控制。功能包括音频驱动的动画合成、面部再现、头部姿势控制、支持自驱动和音频驱动的视频生成、高质量动画生成以及灵活的模型和权重配置。
1. [[⭐] https://github.com/williamyang1991/FRESCO](https://github.com/williamyang1991/FRESCO) **FRESCO。** CVPR 2024会议论文项目，用于零样本视频翻译的空间-时间对应方法
1. [[⭐] https://hailuoai.com](https://hailuoai.com) **海螺AI。** 海螺AI是一个基于先进的AI生成技术打造的对话式智能助理。它可以通过简单的对话,为用户提供知识问答、信息检索、公众号文章写作、小红书笔记生成等服务,帮助用户快速获取信息,提高工作效率。主要功能包括:搜索问答、创意写作、语音交互等。适用于需要知识支持的创作者、自媒体从业者、学生群体等。
1. [[⭐] https://haiper.ai](https://haiper.ai) **Haiper。** Haiper AI 是构建下一代内容创作的最佳感知基础模型的使命。它提供以下主要功能：文本转视频，图片动画，视频重绘，导演视角。Haiper AI 可以将文字内容和静态图片无缝转化为动态视频，只需拖放图像即可使其栩栩如生。使用 Haiper AI 的重绘工具，您可以轻松修改视频的颜色、纹理和元素，以提升视觉内容的品质。通过高级控制工具，您可以像导演一样调整镜头角度、灯光效果、角色姿势和物体运动。Haiper AI 适用于各种场景，如内容创作、设计、营销等。定价请参考官方网站。
1. [[⭐] https://humanaigc.github.io/animate-anyone/](https://humanaigc.github.io/animate-anyone/) **Animate Anyone。** Animate Anyone旨在通过驱动信号从静态图像生成角色视频。我们利用扩散模型的力量，提出了一个专为角色动画量身定制的新框架。为了保持参考图像中复杂外观特征的一致性，我们设计了ReferenceNet来通过空间注意力合并详细特征。为了确保可控性和连续性，我们引入了一个高效的姿势指导器来指导角色的动作，并采用了一种有效的时间建模方法，以确保视频帧之间的平滑跨帧过渡。通过扩展训练数据，我们的方法可以为任意角色制作动画，与其他图像到视频方法相比，在角色动画方面取得了出色的结果。此外，我们在时尚视频和人类舞蹈合成的基准上评估了我们的方法，取得了最先进的结果。
1. [[⭐] https://humanaigc.github.io/emote-portrait-alive/](https://humanaigc.github.io/emote-portrait-alive/) **EMO。** 阿里巴巴的EMO:  是一款生成具有表情丰富的面部表情视频的工具，可以根据输入的角色图像和声音音频生成各种头部姿势和表情的声音头像视频。支持多语言歌曲和各种肖像风格，能够根据音频节奏生成动态、表现丰富的动画角色。
1. [[⭐] https://imagineclip.com](https://imagineclip.com) **ImagineClip。** ImagineClip 是一款 AI 视频生成工具，可从提示词、图片和效果生成头像短片、风格化场景和适合社交平台分享的视频。
1. [[⭐] https://inksprout.co](https://inksprout.co) **Inksprout Video。** Inksprout是一款AI助手，可以从博客生成社交视频。它使用AI生成字幕，让您可以在几秒钟内生成引人注目的、简洁的社交视频。您只需输入博客的URL，AI将自动摘要文章内容，并根据摘要生成视频。您可以使用这些视频在多个社交媒体平台上分享，并提高用户参与度。Inksprout提供免费计划，同时还有更多功能丰富的付费计划可供选择。
1. [[⭐] https://jeanne-wang.github.io/jumpcutsmoothing/](https://jeanne-wang.github.io/jumpcutsmoothing/) **MorphCut。** 该产品提供了一种新颖的框架，用于平滑跳切，特别是在对话视频中。它利用视频中主体的外观，通过 DensePose 关键点和面部标志驱动的中级表示来融合其他源帧中的信息。为了实现运动，它在切割周围的端帧之间插值关键点和标志。然后使用图像转换网络从关键点和源帧合成像素。由于关键点可能包含错误，因此提出了一种跨模态注意机制，以选择和为每个关键点挑选最合适的源。通过利用这种中级表示，我们的方法可以比强视频插值基准获得更强的结果。我们在对话视频的各种跳切上展示了我们的方法，例如切除填充词、暂停，甚至随机切割。我们的实验表明，即使在对话头部旋转或剧烈移动的挑战性情况下，我们也可以实现无缝过渡。
1. [[⭐] https://jimeng.jianying.com](https://jimeng.jianying.com) **即梦。** 即梦Dreamina是一款结合了AI技术的在线创作平台，它通过图片生成、智能画布和视频生成等功能，帮助用户将创意转化为视觉作品。该产品的主要优点在于简化了设计流程，使得非专业人士也能创作出高质量的图片和视频。产品背景信息显示，它由深圳市脸萌科技有限公司开发，定位于为广大创意工作者提供便捷的设计服务。目前产品提供免费试用，具体价格信息未在页面中明确。
1. [[⭐] https://jollytoday.com](https://jollytoday.com) **GhostCut。** GhostCut 可以帮助创作者、商家和 MCN（多渠道网络）通过高效完成视频翻译、硬字幕翻译和字幕移除等任务，进行本地化的视频营销。
1. [[⭐] https://kreadoai.com](https://kreadoai.com) **KreadoAI。** KreadoAI是一款数字营销创作平台，通过输入文本或关键词，可以创作真实/虚拟人物的多语言口播视频。为创作者提供AI赋能。同时，KreadoAI还提供模特创作平台，可以快速生成您的虚拟数字人，适用于假发、服装、美妆、眼镜等电商业务场景。
1. [[⭐] https://ltx.studio](https://ltx.studio) **LTX Studio。** LTX Studio是一个集成了AI技术的创新视频制作平台，它允许用户从概念到最终剪辑，全面控制视频的各个方面。该平台通过AI技术，将创意转化为连贯的视频故事，提供角色一致性、自动编辑、深度帧控制等功能，旨在简化视频制作流程，提高创作效率。
1. [[⭐] https://meeting.iflyrec.com](https://meeting.iflyrec.com) **讯飞会议。** 讯飞会议是安徽听见科技有限公司推出的一款AI高清视频会议系统，专注于提供线上远程网络云会议服务。它基于星火大模型，能够自动生成会议纪要，准确率高达97.5%。产品支持多端协同，包括PC、Mac、手机等，提供高清稳定流畅的音视频体验，同时具备弱网优化，确保声音清晰不卡顿，视频流畅不断。此外，讯飞会议还提供安全稳定的服务，采用AES256和SSL加密技术，保障数据安全。
1. [[⭐] https://meeting.tencent.com/ai/](https://meeting.tencent.com/ai/) **腾讯会议·AI小助手。** 腾讯会议是腾讯自主研发的一款会议软件,提供视频会议、网络研讨会、会议室等产品和服务,支持桌面客户端、移动端等多端使用。可实时共享屏幕,支持白板互动等,实现高清音视频会议。还提供开放API,可深度定制开发。适合企业员工在线会议、网络课堂、远程面试等多种场景使用。
1. [[⭐] https://member.bilibili.com/york/bilibili-studio](https://member.bilibili.com/york/bilibili-studio) **必剪 Studio。** 必剪 Studio 是一款数字分身工具，支持形象驱动和音色定制。用户可以定制专属数字分身，用于配音、口播等场景。产品背景为解决用户在音频制作中个性化需求的问题，定位于提供便捷的数字分身创作工具。
1. [[⭐] https://microsoftedge.microsoft.com/addons/detail/hpkbpmbgkhngdlopdpnfjelemchlmdko](https://microsoftedge.microsoft.com/addons/detail/hpkbpmbgkhngdlopdpnfjelemchlmdko) **AI课代表。** “AI课代表” 是您在B站最专业的人工智能助手 🤖 基于GPT4的“知识提问+“视频总结”+“字幕搜索” 每日刷新免费额度 解决问题，快速定位关键点，筛选视频，帮你成为人见人爱的“课代表” 无情吸赞，学霸人设，专栏大佬，最重要的是：您的声音至关重要，我们将以“3天1更”的速度持续改进！
1. [[⭐] https://modelscope.cn/studios/Damo_XR_Lab/motionshop/summary](https://modelscope.cn/studios/Damo_XR_Lab/motionshop/summary) **Motionshop。** Motionshop是一个 AI 角色动画的网站，它能够根据上传的视频自动检测视频中的人物，并替换成 3D 卡通角色模型，生成有趣的 AI 视频。该产品提供简单易用的界面和强大的 AI 算法，让用户能够轻松将自己的视频内容转化为生动有趣的动画作品。
1. [[⭐] https://mubert.com](https://mubert.com) **Mubert。** 使用人工智能为您的视频内容、播客和应用程序生成音乐。
1. [[⭐] https://no-lang.com](https://no-lang.com) **NoLang。** NoLang是一款基于AI技术的解释视频生成工具。它可以根据用户输入的文本或文档内容,实时生成解释性的视频。主要功能包括:1.文本到视频的实时转换;2.PDF文件等资料的自动视频化汇总;3.可持续对话形式生成视频;4.通过浏览器扩展程序随时调用使用。NoLang的优势是让复杂概念的理解变得更加简单直观,解决信息获取效率低下的问题。主要面向需要获取信息、学习新知识的用户群体,免费使用。
1. [[⭐] https://pixverse.ai](https://pixverse.ai) **PixVerse。** PixVerse是一款创新的AI创作平台，利用强大的生成式AI释放视频创作的全部潜力，让您的内容令人惊叹和难忘。PixVerse通过智能算法和深度学习技术，可以将您的创意转化为令人惊叹的视觉效果。我们提供丰富的功能，包括生成令人惊叹的场景、特效、音乐等，以满足不同类型视频的需求。PixVerse还提供定制化的选项，使您能够根据自己的需求进行个性化定制。无论您是想制作个人视频，还是需要为商业项目创作独特的宣传片，PixVerse都是您理想的选择。
1. [[⭐] https://senseavatar.sensetime.com](https://senseavatar.sensetime.com) **商汤如影。** 商汤日日新 SenseNova 大模型体系提供多种大模型及能力，助力各行业智能化创新，以大算力引领通用人工智能发展。
1. [[⭐] https://shanjian.tv](https://shanjian.tv) **闪剪-AI数字人。** 闪剪是一款 AI 数字人视频生成工具，用户可以定制自己的数字人，只需输入文字即可生成口播视频。
闪剪具备形象、声音克隆；链接成片以及直播切片等功能，手机端和网页端通用。
1. [[⭐] https://soundraw.io](https://soundraw.io) **Soundraw。** 用AI制作免费的音乐
1. [[⭐] https://taishan.qq.com/brand/](https://taishan.qq.com/brand/) **智绘设计。** 智绘设计是一个多场景智能设计服务商，提供正版设计素材和丰富的场景，帮助用户创意无限。它包括以下主要功能：秒速创作，一键出图；智能封面，一键智能生成精美封面；AI视频剪辑，一键智能生成影片视频；智能抠图，一键分离图像画面中的主体内容；人像动漫化，一键生成个性化的二次元动漫形象。智绘做图定位于提供高效创作工具和丰富的设计素材，适用于个人和商业用户。
1. [[⭐] https://tianyin.163.com](https://tianyin.163.com) **网易天音。** 网易出品！一站式AI编曲渲染导出，零基础写歌
1. [[⭐] https://typemovie.art](https://typemovie.art) **讯飞绘镜。** 一款AI视频创作平台。输入创意，即可生成脚本和分镜图片，并将静态分镜化为动态视频。支持快速生成图片与视频，帮助创作者高效捕捉灵感，轻松实现创意表达。
1. [[⭐] https://uberduck.ai](https://uberduck.ai) **uberduck。** 开源的AI语音生成平台
1. [[⭐] https://virbo.wondershare.cn](https://virbo.wondershare.cn) **Virbo。** Virbo是一款万兴科技旗下的数字人营销视频创作神器。
1. [[⭐] https://vizard.ai](https://vizard.ai) **Vizard AI。** 一款 AI 驱动的视频生成和编辑器，可将一段长视频瞬间转换成10多个剪辑。AI 驱动的在线视频编辑器和屏幕录像机，让您能够创建病毒式视频剪辑。自动字幕生成器。
1. [[⭐] https://wanxai.com](https://wanxai.com) **Wan。** Wan是阿里巴巴通义实验室开发的先进视觉生成模型，具备强大的视频生成能力。它能够根据文本、图像及其他控制信号生成视频。Wan2.1系列模型现已完全开源。其主要优点包括卓越的复杂运动生成能力，能够生成逼真的视频，涵盖广泛的身体动作、复杂旋转、动态场景转换和流畅的镜头运动；精准的物理模拟，生成符合真实物理规律的视频；电影质感的画面，提供丰富的纹理和多样化的风格化效果；可控的编辑功能，支持使用图像或视频参考进行精确编辑。该模型的开源为视频生成领域带来了新的可能性，降低了使用门槛，推动了相关技术的发展。
1. [[⭐] https://weta365.com/conduct](https://weta365.com/conduct) **奇妙元。** 奇妙元提供真人形象克隆、声音克隆、3D 数字人定制和 IP 活化等超前沿的克隆与定制服务。通过高质量数据输入和迭代克隆模型，实现高清还原真人形象。用户可使用真人形象克隆终身，通过输入文字使数字人说话，表情神态可比真人。此外，奇妙元还提供数字人视频制作、直播会员和定制服务等功能。数字人视频制作可一键将文本转为视频，无需繁琐拍摄；直播会员可选择真人数字人或 3D 数字人进行直播，为用户挣钱；定制服务可根据用户需求定制数字人形象。奇妙元的产品广泛应用于 20 多个行业，500 多个客户已经受益于数字人定制与克隆服务。
1. [[⭐] https://wonderdynamics.com](https://wonderdynamics.com) **Wonder Studio。** 真人表演自动转换为CG
1. [[⭐] https://www.aimix.pro](https://www.aimix.pro) **AIMIX智剪。** AIMIX智剪是一款集短视频批量剪辑、字幕生成、配音合成等多项功能于一体的短视频内容生产工具。它可以实现智能语音识别、视频脚本设计、快速混剪、字幕制作、配音合成等,大幅提高短视频内容制作效率。关键优势是内容原创性强、支持批量生产、简单易用。定位于需要大量原创短视频内容的个人或机构用户。
1. [[⭐] https://www.animiz.cn/microvideo](https://www.animiz.cn/microvideo) **万彩微影。** 万彩微影，一款全能的AI智能短视频制作软件合集，专门制作热门的手绘动画视频，文字动画视频，还能一键把图文/文章/PPT转换为视频。
1. [[⭐] https://www.arcads.ai](https://www.arcads.ai) **Arcads。** Arcads提供AI视频广告生成器，允许用户快速从文本创建视频广告，特别适合需要大量视频内容的品牌和营销团队。
1. [[⭐] https://www.beatoven.ai](https://www.beatoven.ai) **Beatoven.ai。** Beatoven.ai利用先进的AI音乐生成技术，为您的视频或播客创作独特的基于情感的音乐，以适应您内容的每个部分。我们提供免费试用，定价详细请访问官方网站。
1. [[⭐] https://www.capcut.cn](https://www.capcut.cn) **剪映专业版。** 强大的国产剪辑工具！支持AI智能生成字幕和配音
1. [[⭐] https://www.chanjing.cc](https://www.chanjing.cc) **蝉镜。** 蝉镜是一个在线数字人视频创作平台，利用 AI 简化视频创作过程，提供 AI 数字人播报、短视频制作、分身定制等服务。广告营销、跨境电商、短视频口播等领域的用户可以在此提升创作效率、降低成本。
1. [[⭐] https://www.creatifyone.com](https://www.creatifyone.com) **创一AI。** 创一AI是一款专业的AI短视频脚本创作工具，旨在通过人工智能技术帮助用户快速生成高质量的短视频脚本。该产品利用先进的自然语言处理技术，结合用户需求，能够自动分析并创作出符合主题的脚本内容，大大提高了视频创作者的工作效率。创一深入理解以及对用户需求的精准把握，价格定位为免费体验，以吸引更多用户使用。
1. [[⭐] https://www.d-id.com](https://www.d-id.com) **D-ID。** D-ID是一个创意AI平台，使用AI技术将照片转换为视频。它可以轻松地从文本生成视频，为培训材料、内部沟通、营销等提供AI驱动的、经济实惠的视频解决方案。D-ID还可以实现与聊天机器人进行面对面的对话，使用户获得更加沉浸式和人性化的体验。D-ID还提供API和自助工作室，供开发人员使用。
1. [[⭐] https://www.florafauna.ai](https://www.florafauna.ai) **FLORA。** FLORA 是一个创意 AI 工具平台，将多种顶级文本、图像和视频 AI 模型连接在一个无限画布上，让用户能够以思维的速度进行创意创作。其核心优势在于整合多种 AI 模型，提供无缝的创作体验，能够帮助用户快速从想法到实现的转变。该产品主要面向创意工作者，如设计师、艺术家、视频创作者等，帮助他们提高创作效率和质量。目前 FLORA 提供免费试用，用户可以体验其强大的功能。
1. [[⭐] https://www.genmo.ai](https://www.genmo.ai) **Genmo。** 更具创造性！使用文本指令编辑图像和视频
1. [[⭐] https://www.goenhance.ai](https://www.goenhance.ai) **GoEnhance AI。** GoEnhance AI是一款基于人工智能的图像和视频增强工具。它可以实现视频到视频、图像增强和超分辨率scaling等功能。GoEnhance AI采用了最先进的深度学习算法,可以增强和上采样图像到极致的细节和高分辨率。它简单易用,功能强大,是创作者、设计师等用户释放创意的绝佳工具。
1. [[⭐] https://www.kuaijianji.com](https://www.kuaijianji.com) **快剪辑SaaS版。** 快剪辑SaaS版是一款AI工具，提供丰富的视频模板库和智能剪辑功能，帮助用户快速创建高质量的视频内容。产品定价灵活，适用于个人创作者和企业用户。主要功能包括智能去字幕、智能去水印、智能抠像等。适用场景包括企业宣传、纪录片制作、个人创作等。
1. [[⭐] https://www.laihua.com](https://www.laihua.com) **来画。** 来画是有创意的AI动画短视频制作平台，仅需几张图片，几段文字和声音简单组合， 即可在短时间内生成一个有趣的动画短视频。
1. [[⭐] https://www.loom.com](https://www.loom.com) **Loom。** 使用 Loom AI 录制更好、更快的视频消息，让您的工作更加高效。
1. [[⭐] https://www.microsoft.com/en-us/research/project/vasa-1/](https://www.microsoft.com/en-us/research/project/vasa-1/) **VASA-1。** VASA-1是由微软研究院开发的一个模型，专注于实时生成与音频相匹配的逼真人脸动画。该技术通过深度学习算法，能够根据输入的语音内容，自动生成相应的口型和面部表情，为用户提供一种全新的交互体验。VASA-1的主要优势在于其高度逼真的生成效果和实时响应能力，使得虚拟角色能够更加自然地与用户进行互动。目前，VASA-1主要应用于虚拟助手、在线教育、娱乐等领域，其定价策略尚未公布，但预计将提供免费试用版本供用户体验。
1. [[⭐] https://www.modelscope.cn/studios/vigen/video_generation/summary](https://www.modelscope.cn/studios/vigen/video_generation/summary) **追影。** 追影-视频生成是一款基于人工智能技术的视频生成工具，能够快速生成高质量的视频内容。其优势在于提供丰富的视频模板和智能编辑功能，用户可以轻松制作出令人印象深刻的视频作品。定价灵活合理，定位于个人用户和小型企业，为用户提供高效的视频创作解决方案。
1. [[⭐] https://www.moki.cn](https://www.moki.cn) **Moki。** Moki是美图公司推出的AI短片创作工具，专注于辅助视频创作者打造动画短片、网文短剧、故事绘本和音乐视频（MV）。基于美图自研的奇想智能大模型（MiracleVision），通过智能剪辑、自动配乐、音效添加和字幕生成等功能，大幅简化视频制作流程，提高创作效率。MOKI深度理解创作者需求，实现内容和成本的双重可控，让视频创作变得更加简单和高效。
1. [[⭐] https://www.morphstudio.com](https://www.morphstudio.com) **Morph Studio。** Morph Studio是一款领先的文字转视频AI平台，通过智能算法，将用户输入的文字转化为精美视频。其优势在于快速、高效地实现用户的创意想法，为创作者提供了全新的表现方式。定价灵活多样，适合个人用户和企业用户。定位于提升视频创作效率，让创意更快实现。
1. [[⭐] https://www.narakeet.com/app/text-to-audio/](https://www.narakeet.com/app/text-to-audio/) **Narakeet。** Narakeet是一个在线工具，允许用户轻松创建逼真的文本转语音和旁白视频。它提供了多种语言和声音选择，支持多种文件格式上传，并允许用户自定义音量、速度和输出格式。Narakeet的定价模式为一次性支付，无需订阅，适合商业用户和需要大量音频文件的用户。
1. [[⭐] https://www.opus.pro](https://www.opus.pro) **Opus Clip。** Opus Clip可将长视频转换成高质量的短片，以在TikTok、YouTube Shorts 和 Reels上分享，以增加社交媒体的覆盖范围。
1. [[⭐] https://www.stableaudio.com](https://www.stableaudio.com) **Stable Audio。** Stability Al最新推出的音乐生成工具
1. [[⭐] https://www.swapstream.ai](https://www.swapstream.ai) **SwapStream。** SwapStream是一个基于云的实时人脸互换直播工具,用户可以通过浏览器轻松实现人脸互换的直播。它支持将任意人脸实时互换到直播视频中,同时可以多路流媒体直播到各种直播平台。主要功能包括:实时人脸互换,无需下载直接在浏览器使用,支持多种直播平台,可添加自定义RTMP直播通道等。优点是使用简单、扩展性强,适用于各类直播场景。
1. [[⭐] https://www.unscreen.com](https://www.unscreen.com) **Unscreen。** 智能AI去除视频背景在线神器
1. [[⭐] https://www.vidu.studio](https://www.vidu.studio) **Vidu。** Vidu 是一个创新的 AI 视频生成模型，能够根据用户提供的文本或图片快速生成高质量的视频内容。它的技术基于深度学习，能够理解并分析输入信息，从而创造出富有创意和视觉吸引力的视频。随着视频内容在各类平台上的流行，Vidu 以其便捷性和高效性，成为了内容创作者和市场营销人员的得力助手。该产品适用于个人和企业用户，旨在帮助他们提升内容制作的效率，且目前提供免费试用以吸引更多用户尝试其强大的功能。
1. [[⭐] https://www.yinziai.com](https://www.yinziai.com) **音子 AI。** 音子 AI 是一款在线音轨分离解决方案，用户可上传音频或视频文件，立即获取独立的人声和伴奏文件。该产品基于人工智能技术，提供高效的音轨提取功能。
1. [[⭐] https://youyan.xyz/platform/home/prime](https://youyan.xyz/platform/home/prime) **有言。** 一站式AI视频创作，1200+免费3D数字人
1. [[⭐] https://zeemo.ai/cn](https://zeemo.ai/cn) **绘影字幕。** 绘影字幕的AI 字幕准确率高达98%，能让字幕创建变得前所未有的简单。您可以用绘影字幕的自动化流程取代手动转录，为内容创作者、电影制作人或任何需要字幕的人节省时间。
1. [[⭐] https://zenvideo.qq.com](https://zenvideo.qq.com) **腾讯智影。** 腾讯出品的融合多种AIGC能力进行智能视频创作的一体化工具。
1. [[⭐] https://zh.rask.ai](https://zh.rask.ai) **Rask。** 领先的AI视频本地化和配音工具
1. [[⭐] https://zoomscape.ai](https://zoomscape.ai) **Zoomscape AI。** ZoomScape.ai是一款使用人工智能快速创建独特、有趣和创意背景的工具。它可以帮助您在几秒钟内制作个性化的Zoom背景，让您在视频会议中展现个人风格并给人留下深刻的印象。忘掉无聊的背景，尝试使用ZoomScape.ai让您的Zoom会议更有趣、更个性化。立即开始，展示您的工作个性！
1. [[⭐⭐⭐🚀] https://openai.com/sora](https://openai.com/sora) **Sora。** 碾压级更新！颠覆性的文生视频大模型
1. [[⭐⭐⭐🚀] https://pika.art](https://pika.art) **Pika。** Pika致力于用AI让每个人都能成为自己故事的导演，并激发我们每个人的创造力。
1. [[⭐⭐⭐🚀] https://www.heygen.com](https://www.heygen.com) **Heygen。** AI生成真人营销视频
1. [[🚀] https://lumalabs.ai](https://lumalabs.ai) **Luma Labs。** 将视频转为游戏资产

### AI 数字人 (9)

1. [[⭐] https://clone.ttk.ink](https://clone.ttk.ink) **AI数字人分身系统。** 小狐狸AI数字人分身系统是一款结合了人工智能技术的数字人口型同步产品，支持无限多开和贴牌OEM，适用于需要虚拟形象进行口型同步互动的场景。该产品背景基于人工智能技术的发展，特别是在虚拟主播和在线教育领域的应用需求日益增长。产品价格为3580元，定位于中高端市场，主要优点包括完全开源、支持自主二次开发和定制二次开发，以及免费搭建服务。
1. [[⭐] https://fullpeace.cn](https://fullpeace.cn) **风平智能。** 风平 IP 智造平台是基于 AIGC 的智能化 IP 打造平台，致力于提供虚拟数字人定制、AI 短视频内容生产和数字人直播的一站式解决方案。通过结合领先的 AI 技术，平台实现了数字人的高质量生产和互动能力，为用户打造全新的数字人 IP 体验。
1. [[⭐] https://keyue.cloud.baidu.com](https://keyue.cloud.baidu.com) **百度智能云客悦。** 百度智能云客悦基于百度文心一言大模型,全面重构智能客服系列产品,涵盖客户服务、智能营销、智能通信三大系列,满足企业智能客服全场景需求。主要产品包括:智能对话平台(提供大模型驱动的高智能客服机器人)、智能外呼平台(高拟人度语音对话营销)、对话洞察平台(对话数据分析洞见优化建议)、智能通信平台(集成通信资源API接入)等。产品优势有:基于大模型对话更准确友好全面、高效快速上线运营、多渠道无缝集成适配等。
1. [[⭐] https://shanjian.tv](https://shanjian.tv) **闪剪-AI数字人。** 闪剪是一款 AI 数字人视频生成工具，用户可以定制自己的数字人，只需输入文字即可生成口播视频。
闪剪具备形象、声音克隆；链接成片以及直播切片等功能，手机端和网页端通用。
1. [[⭐] https://virbo.wondershare.cn](https://virbo.wondershare.cn) **Virbo。** Virbo是一款万兴科技旗下的数字人营销视频创作神器。
1. [[⭐] https://weta365.com/conduct](https://weta365.com/conduct) **奇妙元。** 奇妙元提供真人形象克隆、声音克隆、3D 数字人定制和 IP 活化等超前沿的克隆与定制服务。通过高质量数据输入和迭代克隆模型，实现高清还原真人形象。用户可使用真人形象克隆终身，通过输入文字使数字人说话，表情神态可比真人。此外，奇妙元还提供数字人视频制作、直播会员和定制服务等功能。数字人视频制作可一键将文本转为视频，无需繁琐拍摄；直播会员可选择真人数字人或 3D 数字人进行直播，为用户挣钱；定制服务可根据用户需求定制数字人形象。奇妙元的产品广泛应用于 20 多个行业，500 多个客户已经受益于数字人定制与克隆服务。
1. [[⭐] https://www.chanjing.cc](https://www.chanjing.cc) **蝉镜。** 蝉镜是一个在线数字人视频创作平台，利用 AI 简化视频创作过程，提供 AI 数字人播报、短视频制作、分身定制等服务。广告营销、跨境电商、短视频口播等领域的用户可以在此提升创作效率、降低成本。
1. [[⭐] https://www.kreadoai.com](https://www.kreadoai.com) **Kreado AI。** 多语言AI视频创作，只需输入文本或关键词，即可创作真实/虚拟人物的多语言口播视频。
1. [[⭐] https://www.xiaoice.com](https://www.xiaoice.com) **小冰。** 小冰基于全球领先的完备人工智能小冰框架，推出了数字专家和数字员工等完整产品线。

### AI 语音生成 (50)

1. [[⭐⭐⭐] https://ai.wps.cn](https://ai.wps.cn) **WPS AI。** AI 设计助手，一键生成 PPT！WPS AI是由金山办公发布的具备大语言模型能力的人工智能应用，为用户提供智能文档写作、阅读理解和问答、智能人机交互的能力。
1. [[⭐⭐] https://ttsmaker.cn](https://ttsmaker.cn) **TTSMaker马克配音。** 免费的在线文本转语音神器
1. [[⭐] https://ace-studio.timedomain.cn](https://ace-studio.timedomain.cn) **ACE Studio。** ACE Studio 是时域科技旗下的 AI 歌声合成引擎，通过毫无妥协的高表现力人声，解除演唱能力的羁绊，释放人们的音乐想象力。ACE Studio 编辑器软件提供 Windows 客户端版本与 macOS 客户端版本，编辑器 UI 界面简便易操作，您可以轻松地选择 AI 歌手、创建音轨、导入 MIDI，在钢琴卷帘上新建音符、绘制 pitch，在调参面板调整 AI 参数，通过云渲染获得高质量、高可调性的 AI 歌声合成结果。ACE 歌声合成引擎的强大性能，使得虚拟歌手可以真正进入专业音乐生产领域，服务于广大音乐创作者。
1. [[⭐] https://app.deepbrain.io/dashboard](https://app.deepbrain.io/dashboard) **DeepBrain AI。** AI Studios提供了一个用户友好的仪表板，让用户可以轻松创建和管理AI项目。该平台可能包含多种AI工具和功能，以支持用户在图像、视频、音频等领域的创作和编辑。
1. [[⭐] https://audionotes.ai](https://audionotes.ai) **AudioNotes.ai。** AudioNotes.ai是一款利用智能AI将您的口述文字转化为有序文本摘要的应用程序，使得记笔记、头脑风暴和内容创作等活动变得更加轻松！您只需通过语音输入，即可获得清晰、有序的文字记录。此外，AudioNotes.ai还具有智能分类和标签功能，帮助您快速组织和检索笔记。该应用程序适用于各种场景，包括会议记录、学习笔记、写作草稿等。通过AudioNotes.ai，您可以更高效地记录和整理您的想法，提升工作和学习效率。
1. [[⭐] https://bgmcat.com/home](https://bgmcat.com/home) **BGM 猫。** BGM 猫提供版权背景音乐一站式服务，正版商业授权，AI 智能生成曲库，免费无限，快捷授权，一键下载。
1. [[⭐] https://crikk.com](https://crikk.com) **Crikk。** Crikk是一款价格实惠的强大文本转语音工具，支持56种语言，提供真实的语音合成技术。无论是用于语音播报、有声书还是教育，Crikk都能为用户提供高质量的声音合成。用户可以选择免费试用或者采用月费20美元的专业版，月额度为500,000个字符，拥有6种不同的声音和56种语言。此外，Crikk还将推出移动应用，实现图片或PDF的文字转语音。Monster Incorporation Inc.位于Delaware，United States。
1. [[⭐] https://elevenlabs.io](https://elevenlabs.io) **Eleven Labs。** ElevenLabs 带来了最逼真、丰富和生动的声音，为寻求叙事的终极工具的创作者和发布者提供了最具吸引力的文本转语音和语音克隆软件。
1. [[⭐] https://enriccorona.github.io/vlogger/](https://enriccorona.github.io/vlogger/) **VLOGGER。** VLOGGER是一种从单张人物输入图像生成文本和音频驱动的讲话人类视频的方法，它建立在最近生成扩散模型的成功基础上。我们的方法包括1)一个随机的人类到3D运动扩散模型，以及2)一个新颖的基于扩散的架构，通过时间和空间控制增强文本到图像模型。这种方法能够生成长度可变的高质量视频，并且通过对人类面部和身体的高级表达方式轻松可控。与以前的工作不同，我们的方法不需要为每个人训练，也不依赖于人脸检测和裁剪，生成完整的图像（而不仅仅是面部或嘴唇），并考虑到正确合成交流人类所需的广泛场景（例如可见的躯干或多样性主体身份）。
1. [[⭐] https://fanyi.xfyun.cn/console/trans/text](https://fanyi.xfyun.cn/console/trans/text) **讯飞智能翻译。** 科大讯飞推出的人工智能翻译平台
1. [[⭐] https://fireflies.ai](https://fireflies.ai) **fireflies.ai。** Fireflies.ai是一款利用生成式人工智能技术的AI会议记录助手，可自动转录、总结、搜索和分析语音对话。通过与Zoom、Google Meet、Microsoft Teams、Webex等平台集成，生成会议记录和智能摘要。
1. [[⭐] https://github.com/RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) **GPT-SoVITS。** GPT-SoVITS-WebUI是一个强大的零样本语音转换和文本到语音WebUI。它具有零样本TTS、少样本TTS、跨语言支持和WebUI工具等功能。该产品支持英语、日语和中文，提供了集成工具，包括语音伴奏分离、自动训练集分割、中文ASR和文本标注，帮助初学者创建训练数据集和GPT/SoVITS模型。用户可以通过输入5秒的声音样本，即可体验即时的文本到语音转换，还可以通过仅使用1分钟的训练数据对模型进行微调，以提高语音相似度和逼真度。产品支持环境准备、Python和PyTorch版本、快速安装、手动安装、预训练模型、数据集格式、待办事项和致谢。
1. [[⭐] https://github.com/Zejun-Yang/AniPortrait](https://github.com/Zejun-Yang/AniPortrait) **AniPortrait。** AniPortrait是一个根据音频和图像输入生成会说话、唱歌的动�