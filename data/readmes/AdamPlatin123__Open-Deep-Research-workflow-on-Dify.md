# Deep Researcher 工作流复现方案

![Deep Researcher On Dify - Dify](https://github.com/user-attachments/assets/24df7ddb-6bdd-4b4a-9aa3-f7963f2c6f7f)

## 📖 概述
本工作流基于Dify平台构建，复现了Deep Research的核心功能，通过整合多源检索（本地知识库+网络搜索）与多模型协作，可在5分钟内生成万字级结构化研究报告。系统采用模块化设计，支持灵活替换底层模型与数据源。

## 🏆 收录与引用
本工作流（原发于本仓库，2025-02-13）已被 **[Awesome-Dify-Workflow](https://github.com/svcvit/Awesome-Dify-Workflow)**（10.7k★ 的 Dify 工作流合集）收录并署名：

- 上游收录条目 `DSL/Deep Researcher On Dify .yml`（[收录提交，2025-02-24](https://github.com/svcvit/Awesome-Dify-Workflow/commit/565ad61a6dcb564a158ddb420a47e058af9468a0)），文件与本仓库版本**字节一致**
- 上游 README 该条目作者列署名 [@AdamPlatin123](https://github.com/AdamPlatin123)，链接指回本仓库

## ✨ 核心功能
- **智能主题解析**  
  使用Gemini 2.0 Flash模型进行多层级主题拆解，支持4个维度深度分析
- **混合检索引擎**  
  `本地知识库 + 维基百科/Google/Bing API` 多通道检索
- **动态节奏控制**  
  采用2>1模型级联架构，通过条件分支和对话轮次标记实现处理节奏优化
- **高效报告生成**  
  集成deepseek-r1-distill等模型实现段落级内容生成，支持Markdown结构化输出

## 🛠️ 技术架构
```mermaid
graph TD
    A[用户提问] --> B{主题解析}
    B --> F[问题生成]
    F --> H[用户回答]
    H --> C
    B --> I[主题分析]
    I --> C{次级主题提取}
    C --> D[混合迭代检索引擎]
    D --> E[多模型协作生成]
    E --> G[结构化报告]
    
    style B fill:#4CAF50,stroke:#388E3C
    style D fill:#2196F3,stroke:#1565C0
```
## ⚠️ 注意事项
性能优化建议

工作流原则上支持任何模型，使用本地模型请求压力较大时可能会触发LLM节点的`Timepouterror`可以考虑切换线上API服务或是在Dify配置文件中修改timeout时间。

若为Google免费API用户可以插入本地模型节点对RPM进行限流（Google默认限流为15RPM，若短时间请求过多会报错）

## To Do List
·优化处理流程逻辑，平衡RPM与处理时间的矛盾

·修复回答中偶尔出现多个副标题的问题

·大规模重构工作流，对于用户的问题复杂度进行自适应问答

## Licences
LGPL3.0 Licence
