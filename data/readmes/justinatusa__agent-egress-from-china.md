# 从内网出海：AI Agent 的出网之路

[![在线阅读](https://img.shields.io/badge/阅读-从前言开始-blue)](book/00-preface.md) [![License](https://img.shields.io/badge/license-CC%20BY%204.0-lightgrey)](LICENSE)

公司的服务器集群放在中国大陆，上面跑的 AI Agent 每天要访问 Google、Hugging Face、GitHub、PubMed、SEC 这些境外网站，同时还要读公司内网的数据库。这本小书从最基础的网络知识讲起，一步步说明 Agent 的请求是怎么出去的、为什么会被网站拒绝，以及网络同事在群里说的那些行话是什么意思。

读者是会编程、但没接触过网络和云基础设施的程序员。全书由浅入深，每个术语第一次出现时都先用白话解释，按目录顺序读即可。

## 目录

- [前言](book/00-preface.md)

**背景与基础**

1. [背景：集群为什么默认不能上网](book/01-background.md)
2. [网络基础：从 IP 到代理](book/02-network-basics.md)
3. [云上的网络：VPC、NAT 网关与互联](book/03-cloud-basics.md)
4. [容器、K8s 与 Agent 沙箱](book/04-sandboxes.md)

**一个请求的五条路**

5. [总架构：一个请求有几条路](book/05-architecture.md)
6. [分支一和二：代理、白名单与自动注入的坑](book/06-proxy.md)
7. [分支三：三层直连出境，DNS 劫持、IP 池与 403](book/07-l3-egress.md)
8. [网站怎样认出机器人，以及官方接口的规矩](book/08-bot-detection.md)
9. [分支四：云上与云下，两类集群怎样互通](book/09-hybrid.md)
10. [分支五：境外 VPC 加 CEN 的跨境转发](book/10-cen.md)

**怎么选、怎么问**

11. [方案对比：正规路子与野路子](book/11-options.md)
12. [推荐做法：出境怎么建，沙箱放哪里](book/12-recommendation.md)
13. [群聊原话逐句翻译](book/13-chat-decoded.md)
14. [问网络同事的问题清单](book/14-checklist.md)

附录：[A 术语表](book/glossary.md) · [B 云产品对照表](book/products.md)

配图用 draw.io 绘制，源文件在 [`diagrams/`](diagrams/)。

## 许可

正文与配图采用 [CC BY 4.0](LICENSE) 许可。
