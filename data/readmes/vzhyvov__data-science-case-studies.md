# Data Science Case Studies: ML, A/B Testing and Product Analytics

How real companies solved product analytics, experimentation and machine-learning problems: case studies from engineering blogs and conference talks, grouped by topic. Each entry has the company, the year, a link to the original and a structured digest.

![cases](https://img.shields.io/badge/cases-3210-6B4EE6) ![companies](https://img.shields.io/badge/companies-632-6B4EE6) ![updated](https://img.shields.io/badge/updated-2026--11--27-lightgrey) ![license](https://img.shields.io/badge/license-CC_BY_4.0-lightgrey)

**Jump to:** [A/B testing](topics/ab-testing.md) · [Recommendations](topics/recsys.md) · [Search](topics/search.md) · [Causal inference](topics/causal.md) · [LLM in analytics](topics/llm-in-analytics.md) · [Fraud](topics/fraud.md) · [All topics](#contents) · [By company](companies/README.md) · [CSV / JSON](data/)

Read the digests on **[effectsize.io](https://effectsize.io)**, or search them from Claude, ChatGPT or Cursor over MCP: `claude mcp add --transport http --scope user effectsize https://mcp.effectsize.io/mcp` ([setup](https://effectsize.io/mcp/)).

## Contents

- **Experiments & causal**: [Metrics](#metrics) (68) · [A/B testing](#ab-testing) (297) · [Advanced experimentation](#advanced-experimentation) (86) · [Causal inference](#causal-inference) (161) · [Uplift](#uplift) (48)
- **Recs & search**: [Recommendations](#recommendations) (460) · [Personalization](#personalization) (112) · [Search](#search) (332)
- **LLM**: [LLM in analytics](#llm-in-analytics) (698)
- **Predictive & behavior**: [Clickstream](#clickstream) (44) · [Behavior](#behavior) (51) · [Predictive models](#predictive-models) (333) · [Growth](#growth) (56)
- **Risk**: [Fraud](#fraud) (145)
- **Data & practice**: [Insights](#insights) (122) · [Analytics practice](#analytics-practice) (88) · [Data infrastructure](#data-infrastructure) (109)
- [Top companies](#top-companies) · [FAQ](#faq) · [Use it with your AI agent](#use-it-with-your-ai-agent)

## Experiments & causal

### Metrics

North Star, metric trees, proxy and surrogate metrics, guardrails, LTV/unit economics in a product context.

| Case | Company | Year | Source |
|---|---|---|---|
| [Metrics Board: Building an Agent-ready Metrics Layer](https://effectsize.io/cases/metrics-board-building-an-agent-ready-metrics-layer/) | Pinterest | 2026 | [original](https://medium.com/pinterest-engineering/metrics-board-building-an-agent-ready-metrics-layer-2c8fefe68756) |
| [A shift from content and topic to presentation: how the reading pattern for articles on Habr has changed](https://effectsize.io/cases/a-shift-from-content-and-topic-to-presentation-how-the/) | MTS | 2026 | [original](https://habr.com/ru/companies/ru_mts/articles/1063884/) |
| [Proxy This: How to Speed Up A/B Tests Without Falling into the Metrics Trap](https://effectsize.io/cases/proxy-this-how-to-speed-up-a-b-tests-without-falling-into/) | X5 Tech | 2025 | [original](https://habr.com/ru/companies/X5Tech/articles/974372/) |
| [How to Estimate Correlation Between Metrics from Past A/B Tests](https://effectsize.io/cases/how-to-estimate-correlation-between-metrics-from-past-a-b/) | Booking.com | 2025 | [original](https://booking.ai/how-to-estimate-correlation-between-metrics-from-past-a-b-tests-0a5d99e5a11d) |
| [How we built it: Real-time analytics for Stripe Billing](https://effectsize.io/cases/how-we-built-it-real-time-analytics-for-stripe-billing/) | Stripe | 2025 | [original](https://stripe.com/blog/how-we-built-it-real-time-analytics-for-stripe-billing) |
| [Behind the metric: how we developed “Time Spent Learning Well”](https://effectsize.io/cases/behind-the-metric-how-we-developed-time-spent-learning-well/) | Duolingo | 2024 | [original](https://blog.duolingo.com/time-spent-learning-well) |
| [Airbnb Brandometer: Powering brand perception measurement on social media data with AI](https://effectsize.io/cases/airbnb-brandometer-powering-brand-perception-measurement-on/) | Airbnb | 2024 | [original](https://medium.com/airbnb-engineering/airbnb-brandometer-powering-brand-perception-measurement-on-social-media-data-with-ai-c83019408051) |
| [Learning the Covariance of Treatment Effects Across Many Weak Experiments](https://effectsize.io/cases/learning-the-covariance-of-treatment-effects-across-many/) | Netflix | 2024 | [original](https://arxiv.org/abs/2402.17637) |

**[All 68 metrics cases →](topics/metrics.md)**

### A/B testing

Design, power and MDE, variance reduction (CUPED, stratification), sequential testing, multiple comparisons, SRM, peeking, ratio metrics, bootstrap, experimentation platforms.

| Case | Company | Year | Source |
|---|---|---|---|
| [The Hidden Cost of Winsorizing](https://effectsize.io/cases/the-hidden-cost-of-winsorizing-2/) | Spotify | 2026 | [original](https://confidence.spotify.com/blog/capping-vs-winsorizing) |
| [The Hidden Cost of Winsorizing](https://effectsize.io/cases/the-hidden-cost-of-winsorizing/) | Spotify | 2026 | [original](https://confidence.spotify.com/blog/capping-vs-winsorizing.md) |
| [Buckets instead of millions of rows: how we speed up A/B test calculations without losing accuracy](https://effectsize.io/cases/buckets-instead-of-millions-of-rows-how-we-speed-up-a-b-test/) | X5 Tech | 2026 | [original](https://habr.com/ru/companies/X5Tech/articles/1075722/) · [code](https://effectsize.io/cases/buckets-instead-of-millions-of-rows-how-we-speed-up-a-b-test/) |
| [How we redistributed alpha in A/B tests and reduced the sample size](https://effectsize.io/cases/how-we-redistributed-alpha-in-a-b-tests-and-reduced-the/) | T-Bank | 2026 | [original](https://habr.com/ru/companies/tbank/articles/1089482/) |
| [A problem well-defined is half solved: Measuring Hypothesis Quality at Booking.com](https://effectsize.io/cases/a-problem-well-defined-is-half-solved-measuring-hypothesis/) | Booking.com | 2026 | [original](https://booking.ai/a-problem-well-defined-is-half-solved-measuring-hypothesis-quality-at-booking-com-a85e845178a3) |
| [Why Spotify Is Not Using Bayesian A/B Testing](https://effectsize.io/cases/why-spotify-is-not-using-bayesian-a-b-testing/) | Spotify | 2026 | [original](https://engineering.atspotify.com/2026/9/why-spotify-is-not-using-bayesian-a-b-testing) |
| [When Can LLMs Replace Humans in A/B Tests?](https://effectsize.io/cases/when-can-llms-replace-humans-in-a-b-tests/) | Spotify | 2026 | [original](https://engineering.atspotify.com/2026/8/when-can-llms-replace-humans-in-a-b-tests) |
| [A Recap of the 2026 Experimentation Conference at Booking.com](https://effectsize.io/cases/a-recap-of-the-2026-experimentation-conference-at-booking/) | Booking.com | 2026 | [original](https://booking.ai/a-recap-of-the-2026-experimentation-conference-at-booking-com-f43d48698fcd) |

**[All 297 a/b testing cases →](topics/ab-testing.md)**

### Advanced experimentation

Network effects and interference, two-sided marketplaces, switchback, cluster randomization, long-term effects, bandits, interleaving.

| Case | Company | Year | Source |
|---|---|---|---|
| [Practical Lessons in Measuring Network Effects](https://effectsize.io/cases/practical-lessons-in-measuring-network-effects/) | Meta | 2026 | [original](https://www.youtube.com/watch?v=2ziq49bGDA8) |
| [Powering AI-led research through simulation](https://effectsize.io/cases/powering-ai-led-research-through-simulation/) | Grab | 2026 | [original](https://engineering.grab.com/powering-ai-led-research-through-simulation) |
| [Scaling Reliable Experimentation in a Two-Sided AdTech Marketplace: ZMS Budget Split](https://effectsize.io/cases/scaling-reliable-experimentation-in-a-two-sided-adtech/) | Zalando | 2026 | [original](https://engineering.zalando.com/posts/2026/09/scaling-reliable-experimentation-in-two-sided-adtech-marketplace.html) |
| [Variance Reduction Below the Randomization Grain](https://effectsize.io/cases/variance-reduction-below-the-randomization-grain/) | Instacart | 2026 | [original](https://tech.instacart.com/variance-reduction-below-the-randomization-grain-31719f87a7d2) |
| [Leveraging PyFixest for High-Cardinality Marketplace Modeling at Instacart](https://effectsize.io/cases/leveraging-pyfixest-for-high-cardinality-marketplace/) | Instacart | 2026 | [original](https://tech.instacart.com/leveraging-pyfixest-for-high-cardinality-marketplace-modeling-at-instacart-3913df91a04b) · [code](https://effectsize.io/cases/leveraging-pyfixest-for-high-cardinality-marketplace/) |
| [Switchback tests: infrastructure for experiments under network effects](https://effectsize.io/cases/switchback-tests-infrastructure-for-experiments-under/) | Avito | 2026 | [original](https://habr.com/ru/companies/avito/articles/1048780/) |
| [Why an A/B test is not suitable for evaluating ranking, and what to do about it](https://effectsize.io/cases/why-an-a-b-test-is-not-suitable-for-evaluating-ranking-and/) | Avito | 2026 | [original](https://habr.com/ru/companies/avito/articles/1043880/) |
| [Beyond A/B Testing: Using Surrogacy and Region-Splits to Measure Long-Term Effects in Marketplaces](https://effectsize.io/cases/beyond-a-b-testing-using-surrogacy-and-region-splits-to/) | Lyft | 2026 | [original](https://eng.lyft.com/beyond-a-b-testing-using-surrogacy-and-region-splits-to-measure-long-term-effects-in-marketplaces-9cb06d628f2d) |

**[All 86 advanced experimentation cases →](topics/experimentation-advanced.md)**

### Causal inference

DiD, synthetic control, RDD, IV, matching/PSM, CausalImpact, effect estimation without an A/B test, double ML.

| Case | Company | Year | Source |
|---|---|---|---|
| [DML vs PSM: how to estimate non-randomized experiments faster and more reliably?](https://effectsize.io/cases/dml-vs-psm-how-to-estimate-non-randomized-experiments-faster/) | Wildberries | 2026 | [original](https://habr.com/ru/companies/rwb/articles/1070206/) |
| [A Human-Augmenting Agentic Workflow for Causal Inference](https://effectsize.io/cases/a-human-augmenting-agentic-workflow-for-causal-inference/) | Netflix | 2026 | [original](https://netflixtechblog.com/a-human-augmenting-agentic-workflow-for-causal-inference-4623f0a9c5af) · [code](https://effectsize.io/cases/a-human-augmenting-agentic-workflow-for-causal-inference/) |
| [Evolution of the Databricks Commercial Motion: Building Scalable Intelligence on Databricks](https://effectsize.io/cases/evolution-of-the-databricks-commercial-motion-building/) | Databricks | 2026 | [original](https://www.databricks.com/dataaisummit/session/evolution-databricks-commercial-motion-building-scalable-intelligence) |
| [How Developer Productivity Changed with AI4SDLC Tools](https://effectsize.io/cases/how-developer-productivity-changed-with-ai4sdlc-tools/) | T-Bank | 2026 | [original](https://www.youtube.com/watch?v=AKfcnrTZXYY) |
| [Problems and Prospects of Causal AI](https://effectsize.io/cases/problems-and-prospects-of-causal-ai/) | Sber | 2026 | [original](https://www.youtube.com/watch?v=5dAXL2yP3Ow) |
| [The New Policy Hasn't Run Yet: Comparing It to the Old One Before an A/B Test](https://effectsize.io/cases/the-new-policy-hasn-t-run-yet-comparing-it-to-the-old-one/) | Sber | 2026 | [original](https://www.youtube.com/watch?v=UeHoi7uLT1I) |
| [The Causality Gap: Measuring the True Impact of Voluntary Adoption in Digital Marketplaces](https://effectsize.io/cases/the-causality-gap-measuring-the-true-impact-of-voluntary/) | Booking.com | 2026 | [original](https://booking.ai/the-causality-gap-measuring-the-true-impact-of-voluntary-adoption-in-digital-marketplaces-ea68b5a35120) |
| [Meta: A Blueprint for Valuing Content When A/B Tests Are Not an Option](https://effectsize.io/cases/meta-a-blueprint-for-valuing-content-when-a-b-tests-are-not/) | Meta | 2026 | [original](https://medium.com/@AnalyticsAtMeta/meta-a-blueprint-for-valuing-content-when-a-b-tests-are-not-an-option-7880bac721f1) |

**[All 161 causal inference cases →](topics/causal.md)**

### Uplift

CATE, meta-learners (S/T/X/R/DR), uplift trees, communication and promo targeting, policy learning, uplift evaluation (Qini, AUUC).

| Case | Company | Year | Source |
|---|---|---|---|
| [A Championship of Uplift Models: Group Stage, Playoffs and an Unexpected Leader](https://effectsize.io/cases/a-championship-of-uplift-models-group-stage-playoffs-and-an/) | Avito | 2026 | [original](https://habr.com/ru/companies/avito/articles/1061032/) · [code](https://effectsize.io/cases/a-championship-of-uplift-models-group-stage-playoffs-and-an/) |
| [Smarter promotions with causal machine learning](https://effectsize.io/cases/smarter-promotions-with-causal-machine-learning/) | DoorDash | 2025 | [original](https://careersatdoordash.com/blog/doordash-smarter-promotions-with-causal-machine-learning) |
| [Heterogeneous Treatment Effects at Netflix](https://effectsize.io/cases/heterogeneous-treatment-effects-at-netflix/) | Netflix | 2025 | [original](https://netflixtechblog.medium.com/heterogeneous-treatment-effects-at-netflix-da5c3dd58833) |
| [How We Grew Sales Team Efficiency with Customer Ranking](https://effectsize.io/cases/how-we-grew-sales-team-efficiency-with-customer-ranking/) | Avito | 2025 | [original](https://www.youtube.com/watch?v=1ozHNMcpLyw) |
| [Are All Wolves Scary: AUF or How to Tame Uplift?](https://effectsize.io/cases/are-all-wolves-scary-auf-or-how-to-tame-uplift/) | Alfa-Bank | 2025 | [original](https://habr.com/ru/companies/alfa/articles/895002/) · [code](https://effectsize.io/cases/are-all-wolves-scary-auf-or-how-to-tame-uplift/) |
| [How machine learning supercharged our revenue by millions of dollars](https://effectsize.io/cases/how-machine-learning-supercharged-our-revenue-by-millions-of/) | Duolingo | 2025 | [original](https://blog.duolingo.com/machine-learning-ads/) |
| [Experimenting with Machine Learning to Target In-App Messaging](https://effectsize.io/cases/experimenting-with-machine-learning-to-target-in-app/) | Spotify | 2023 | [original](https://engineering.atspotify.com/2023/06/experimenting-with-machine-learning-to-target-in-app-messaging) |
| [Causal machine learning for a smart paywall at The New York Times](https://effectsize.io/cases/causal-machine-learning-for-a-smart-paywall-at-the-new-york/) | The New York Times | 2023 | [original](https://www.youtube.com/watch?v=6CmS96K6-EE) |

**[All 48 uplift cases →](topics/uplift.md)**

## Recs & search

### Recommendations

Candidate generation, ranking, embeddings, sequential/session-based recommendations, cold start, diversity, feedback loops, offline/online evaluation.

| Case | Company | Year | Source |
|---|---|---|---|
| [HEGM: Predicting the Distribution of Watch Time in Short-Video Recommendations](https://effectsize.io/cases/hegm-predicting-the-distribution-of-watch-time-in-short/) | VK | 2026 | [original](https://habr.com/ru/companies/vk/articles/1107030/) · [code](https://effectsize.io/cases/hegm-predicting-the-distribution-of-watch-time-in-short/) |
| [Safe and Efficient Multi-Epoch Embedding Training](https://effectsize.io/cases/safe-and-efficient-multi-epoch-embedding-training/) | Pinterest | 2026 | [original](https://medium.com/pinterest-engineering/safe-and-efficient-multi-epoch-embedding-training-103bec2abc83) |
| [Meta Andromeda: Powering the Next Generation of Ads Retrieval Through Model-System Co-Design](https://effectsize.io/cases/meta-andromeda-powering-the-next-generation-of-ads-retrieval/) | Meta | 2026 | [original](https://engineering.fb.com/2026/10/28/ml-applications/meta-andromeda-next-gen-ads-retrieval-gpu-co-design) |
| [Incremental recommendation via causal models](https://effectsize.io/cases/incremental-recommendation-via-causal-models/) | Spotify | 2026 | [original](https://research.atspotify.com/publications/incremental-recommendation-via-causal-models) |
| [How we split recommendations into streams in AI VK](https://effectsize.io/cases/how-we-split-recommendations-into-streams-in-ai-vk/) | VK | 2026 | [original](https://habr.com/ru/companies/vk/articles/1096708/) |
| [GenRecs Tokenization: Transforming Ads Recommendation at Meta with Stable Model Vocabulary](https://effectsize.io/cases/genrecs-tokenization-transforming-ads-recommendation-at-meta/) | Meta | 2026 | [original](https://engineering.fb.com/2026/10/19/ml-applications/genrecs-tokenization-transforming-ads-recommendation-at-meta-with-stable-model-vocabulary) |
| [Measuring the Impact of Personalized Recommendations](https://effectsize.io/cases/measuring-the-impact-of-personalized-recommendations/) | Netflix | 2026 | [original](https://netflixtechblog.com/measuring-the-impact-of-personalized-recommendations-4c26be3a4d96) |
| [Meta’s Generative Ads Model (GEM): Scaling the Central Model and Compute Engine for Frontier Ads AI](https://effectsize.io/cases/meta-s-generative-ads-model-gem-scaling-the-central-model/) | Meta | 2026 | [original](https://engineering.fb.com/2026/10/13/ml-applications/generative-ads-model-gem-scaling-frontier-ads-ai/) |

**[All 460 recommendations cases →](topics/recsys.md)**

### Personalization

Personalized UX, content, notifications, pricing and offers, contextual bandits, next-best-action.

| Case | Company | Year | Source |
|---|---|---|---|
| [From Activity to Intent: Generating User Journeys with LLMs](https://effectsize.io/cases/from-activity-to-intent-generating-user-journeys-with-llms/) | Pinterest | 2026 | [original](https://medium.com/pinterest-engineering/from-activity-to-intent-generating-user-journeys-with-llms-9652b9417626) |
| [Personalization without user identity](https://effectsize.io/cases/personalization-without-user-identity/) | Airbnb | 2026 | [original](https://medium.com/airbnb-engineering/personalization-without-user-identity-8e7891a1d486) |
| [Building Ask DoorDash (Part 6): A Grocery Reorder Case Study](https://effectsize.io/cases/building-ask-doordash-part-6-a-grocery-reorder-case-study/) | DoorDash | 2026 | [original](https://careersatdoordash.com/blog/building-ask-doordash-part-6-grocery-reorder-case-study/) |
| [MAPS: Netflix’s Multimodal Asset Personalization at Scale](https://effectsize.io/cases/maps-netflix-s-multimodal-asset-personalization-at-scale/) | Netflix | 2026 | [original](https://netflixtechblog.com/maps-netflixs-multimodal-asset-personalization-at-scale-32f96320785e) |
| [From manual rules to a model: how to automate subsidies when you can't hurt metrics in an A/B test](https://effectsize.io/cases/from-manual-rules-to-a-model-how-to-automate-subsidies-when/) | Avito | 2026 | [original](https://habr.com/ru/companies/avito/articles/1053408/) |
| [Thinking Fast & Slow for a Personalized Notification System](https://effectsize.io/cases/thinking-fast-slow-for-a-personalized-notification-system/) | Netflix | 2026 | [original](https://netflixtechblog.com/thinking-fast-slow-for-a-personalized-notification-system-4d89b26525cd) |
| [TargetRun: AI-Powered Trip Prediction for Delivering Timely Offers](https://effectsize.io/cases/targetrun-ai-powered-trip-prediction-for-delivering-timely/) | Target | 2026 | [original](https://tech.target.com/blog/targetrun-shopping-offers) |
| [Offline LLMs, Online Personalization: Generating carousels at DoorDash](https://effectsize.io/cases/offline-llms-online-personalization-generating-carousels-at/) | DoorDash | 2026 | [original](https://careersatdoordash.com/blog/doordash-offline-llms-online-personalization-generating-carousels/) |

**[All 112 personalization cases →](topics/personalization.md)**

### Search

Ranking, learning-to-rank, query understanding, autocomplete, relevance and its labeling, search metrics, semantic/hybrid search in a product.

| Case | Company | Year | Source |
|---|---|---|---|
| [Most Search Answers Are Ready Before the Query Arrives](https://effectsize.io/cases/most-search-answers-are-ready-before-the-query-arrives/) | Wildberries | 2026 | [original](https://habr.com/ru/companies/rwb/articles/1099536/) |
| [Robust Fusion of Semantic and Behavioural Signals for LLM Reranking in Personalised Search](https://effectsize.io/cases/robust-fusion-of-semantic-and-behavioural-signals-for-llm/) | Spotify | 2026 | [original](https://research.atspotify.com/publications/robust-fusion-of-semantic-and-behavioural-signals-for-llm-reranking-in-personalised-search) |
| [CASTLE: training natural language search before the first real query](https://effectsize.io/cases/castle-training-natural-language-search-before-the-first/) | Airbnb | 2026 | [original](https://medium.com/airbnb-engineering/castle-training-natural-language-search-before-the-first-real-query-3818ef8b4828) |
| [Distilling LLM Understanding into Marketplace Discovery](https://effectsize.io/cases/distilling-llm-understanding-into-marketplace-discovery/) | DoorDash | 2026 | [original](https://www.youtube.com/watch?v=ACPEpji5NV4) |
| [Automating Search Relevance Assessment at Scale with LLM-as-a-Judge](https://effectsize.io/cases/automating-search-relevance-assessment-at-scale-with-llm-as/) | Allegro | 2026 | [original](https://blog.allegro.tech/2026/08/automating-search-relevance-llm-as-a-judge.html) |
| [When captions are not enough: how we cleaned up the "gray zone" in Image Search](https://effectsize.io/cases/when-captions-are-not-enough-how-we-cleaned-up-the-gray-zone/) | Yandex | 2026 | [original](https://habr.com/ru/companies/yandex/articles/1066946/) |
| [The Evolution of Job Search at Avito Rabota: ML Optimizations and Insights from A/B Tests](https://effectsize.io/cases/the-evolution-of-job-search-at-avito-rabota-ml-optimizations/) | Avito | 2026 | [original](https://habr.com/ru/companies/avito/articles/1064546/) |
| [Personalizing Airbnb search by learning from the guest journey](https://effectsize.io/cases/personalizing-airbnb-search-by-learning-from-the-guest/) | Airbnb | 2026 | [original](https://medium.com/airbnb-engineering/personalizing-airbnb-search-by-learning-from-the-guest-journey-bcefd1915624) |

**[All 332 search cases →](topics/search.md)**

## LLM

### LLM in analytics

LLMs for data analysis, evaluating LLM features with experiments, LLM ranking and recommendations.

| Case | Company | Year | Source |
|---|---|---|---|
| [How Pinterest Improved Analytics Agent Compliance with Loop Engineering](https://effectsize.io/cases/how-pinterest-improved-analytics-agent-compliance-with-loop/) | Pinterest | 2026 | [original](https://medium.com/pinterest-engineering/how-pinterest-improved-analytics-agent-compliance-with-loop-engineering-d3c52d0abaa2) |
| [Visual search: fine-tuning ColPali and ColQwen3 for the Russian domain and comparing text and multimodal retrieval](https://effectsize.io/cases/visual-search-fine-tuning-colpali-and-colqwen3-for-the/) | X5 Tech | 2026 | [original](https://habr.com/ru/companies/X5Tech/articles/1103334/) |
| [Fact-Checking at Scale: Building a More Accurate and Efficient Synopsis Factuality System](https://effectsize.io/cases/fact-checking-at-scale-building-a-more-accurate-and/) | Netflix | 2026 | [original](https://netflixtechblog.com/fact-checking-at-scale-building-a-more-accurate-and-efficient-synopsis-factuality-system-d7d85859d808) |
| [How we reduced T2M content from 7 days to 1 hour by applying a data-driven approach and turning a well-known meme upside down](https://effectsize.io/cases/how-we-reduced-t2m-content-from-7-days-to-1-hour-by-applying/) | Sber | 2026 | [original](https://habr.com/ru/companies/sberbank/articles/1103056/) |
| [From Static Help Content to a RAG-Based Onboarding Agent for Partners](https://effectsize.io/cases/from-static-help-content-to-a-rag-based-onboarding-agent-for/) | Booking.com | 2026 | [original](https://booking.ai/from-static-help-content-to-a-rag-based-onboarding-agent-for-partners-f7d5a789c4f7) |
| [The Lifecycle of LLM-as-a-Judge: Building, Aligning, and Monitoring at scale](https://effectsize.io/cases/the-lifecycle-of-llm-as-a-judge-building-aligning-and-2/) | Netflix | 2026 | [original](https://netflixtechblog.medium.com/the-lifecycle-of-llm-as-a-judge-building-aligning-and-monitoring-at-scale-c95bd8283508) |
| [Inside LinkedIn's data context layer: curating trustworthy context for humans and agents](https://effectsize.io/cases/inside-linkedin-s-data-context-layer-curating-trustworthy/) | LinkedIn | 2026 | [original](https://linkedin.com/blog/engineering/infrastructure/inside-linkedins-data-context-layer-curating-trustworthy-context-for-humans-and-agents) |
| [Scaling AI in Legal: Building Uber's Redlining Agent](https://effectsize.io/cases/scaling-ai-in-legal-building-uber-s-redlining-agent/) | Uber | 2026 | [original](https://www.uber.com/gb/en/blog/building-ubers-redlining-agent/) |

**[All 698 llm in analytics cases →](topics/llm-in-analytics.md)**

## Predictive & behavior

### Clickstream

Sessionization, paths and funnels, process mining, sequence mining, transitions between events, journey maps, tracking plan and event design.

| Case | Company | Year | Source |
|---|---|---|---|
| [Advanced SQL Patterns for Production Analytics](https://effectsize.io/cases/advanced-sql-patterns-for-production-analytics/) | Databricks | 2026 | [original](https://www.databricks.com/dataaisummit/session/advanced-sql-patterns-production-analytics) |
| [How a transaction graph helps the bank get to know its customer better](https://effectsize.io/cases/how-a-transaction-graph-helps-the-bank-get-to-know-its/) | Sber | 2026 | [original](https://habr.com/ru/companies/sberbank/articles/1018456/) · [code](https://effectsize.io/cases/how-a-transaction-graph-helps-the-bank-get-to-know-its/) |
| [What's in the black box? Finding out on our own without attracting colleagues' attention](https://effectsize.io/cases/what-s-in-the-black-box-finding-out-on-our-own-without/) | Yandex | 2025 | [original](https://habr.com/ru/companies/yandex/articles/921122/) |
| [How Canva collects 25 billion events per day](https://effectsize.io/cases/how-canva-collects-25-billion-events-per-day/) | Canva | 2024 | [original](https://canva.dev/blog/engineering/product-analytics-event-collection) |
| [Leveraging Flink to Detect User Sessions and Engage DoorDash Consumers with Real-Time Notifications](https://effectsize.io/cases/leveraging-flink-to-detect-user-sessions-and-engage-doordash/) | DoorDash | 2023 | [original](https://careersatdoordash.com/blog/leveraging-flink-to-detect-user-sessions-and-engage-doordash-consumers-with-real-time-notifications) |
| [BDUI Analytics, or Why You Can't Just Take and Send Dynamic Field Values to the Tracker](https://effectsize.io/cases/bdui-analytics-or-why-you-can-t-just-take-and-send-dynamic/) | Alfa-Bank | 2023 | [original](https://habr.com/ru/companies/alfa/articles/752068/) |
| [Marketing Attribution: Evaluating The Path to Purchase in the Product Ecosystem](https://effectsize.io/cases/marketing-attribution-evaluating-the-path-to-purchase-in-the/) | trivago | 2022 | [original](https://tech.trivago.com/post/2022-12-06-marketing-attribution-evaluating-the-path-to-purchase) |
| [How a neural network outperformed boosting, and Sber's team took 1st place in the Data Fusion Contest 2022](https://effectsize.io/cases/how-a-neural-network-outperformed-boosting-and-sber-s-team/) | Sber | 2022 | [original](https://habr.com/ru/companies/sberbank/articles/674272/) · [code](https://effectsize.io/cases/how-a-neural-network-outperformed-boosting-and-sber-s-team/) |

**[All 44 clickstream cases →](topics/clickstream.md)**

### Behavior

Retention, cohorts, activation, aha-moment, engagement, behavioral segmentation and clustering, behavior-based churn analysis.

| Case | Company | Year | Source |
|---|---|---|---|
| [From 'Someday' to a Working Prototype: How an LLM Gave an Idea a Chance](https://effectsize.io/cases/from-someday-to-a-working-prototype-how-an-llm-gave-an-idea/) | Avito | 2026 | [original](https://habr.com/ru/companies/avito/articles/1078084/) · [code](https://effectsize.io/cases/from-someday-to-a-working-prototype-how-an-llm-gave-an-idea/) |
| [How retro games raised retention? Our experience of introducing gamification at MTS](https://effectsize.io/cases/how-retro-games-raised-retention-our-experience-of/) | MTS | 2025 | [original](https://habr.com/ru/companies/ru_mts/articles/960552/) |
| [How we use RFM segmentation to improve CRM communications at Avito](https://effectsize.io/cases/how-we-use-rfm-segmentation-to-improve-crm-communications-at/) | Avito | 2025 | [original](https://habr.com/ru/companies/avito/articles/956746/) |
| [Engagement, user expertise, and satisfaction: Key insights from the Semantic Telemetry Project](https://effectsize.io/cases/engagement-user-expertise-and-satisfaction-key-insights-from/) | Microsoft | 2025 | [original](https://microsoft.com/en-us/research/blog/engagement-user-expertise-and-satisfaction-key-insights-from-the-semantic-telemetry-project) |
| [Single AI View of Customer: A retailers guide to Know Your Customer Better using Customer Embeddings and Customer Persona](https://effectsize.io/cases/single-ai-view-of-customer-a-retailers-guide-to-know-your/) | Walmart | 2025 | [original](https://medium.com/walmartglobaltech/single-ai-view-of-customer-a-retailers-guide-to-know-your-customer-better-using-customer-6b588ff336bd) |
| [Using differential privacy to understand usage patterns in AI applications](https://effectsize.io/cases/using-differential-privacy-to-understand-usage-patterns-in/) | Microsoft | 2025 | [original](https://medium.com/data-science-at-microsoft/using-differential-privacy-to-understand-usage-patterns-in-ai-applications-ad6538a81f30) · [code](https://effectsize.io/cases/using-differential-privacy-to-understand-usage-patterns-in/) |
| [What difficulties we overcame when introducing RFM customer segmentation at Avito Real Estate](https://effectsize.io/cases/what-difficulties-we-overcame-when-introducing-rfm-customer/) | Avito | 2024 | [original](https://habr.com/ru/companies/avito/articles/863960/) |
| [From Data to Insights: Segmenting Airbnb's Supply](https://effectsize.io/cases/from-data-to-insights-segmenting-airbnb-s-supply/) | Airbnb | 2024 | [original](https://medium.com/airbnb-engineering/from-data-to-insights-segmenting-airbnbs-supply-c88aa2bb9399) |

**[All 51 behavior cases →](topics/behavior.md)**

### Predictive models

Churn prediction, propensity, LTV prediction, lead scoring, metric forecasting.

| Case | Company | Year | Source |
|---|---|---|---|
| [Why an Ensemble Needs Negative Weights: From Portfolio Theory to Credit Scoring](https://effectsize.io/cases/why-an-ensemble-needs-negative-weights-from-portfolio-theory/) | Alfa-Bank | 2026 | [original](https://habr.com/ru/companies/alfa/articles/1108082/) |
| [From Customer Flow Forecast to Optimal Staff Size](https://effectsize.io/cases/from-customer-flow-forecast-to-optimal-staff-size/) | Alfa-Bank | 2026 | [original](https://habr.com/ru/companies/alfa/articles/1085676/) |
| [Roonomics: How Economics Helped Us to Build a Churn Prediction Model](https://effectsize.io/cases/roonomics-how-economics-helped-us-to-build-a-churn/) | Deliveroo | 2026 | [original](https://deliveroo.engineering/2026/09/22/roonomics-how-economics-helped-us-to-build-a-churn-prediction-model.html) |
| [How we knew COVID was over (and what our models had to unlearn)](https://effectsize.io/cases/how-we-knew-covid-was-over-and-what-our-models-had-to/) | Airbnb | 2026 | [original](https://medium.com/airbnb-engineering/how-we-knew-covid-was-over-and-what-our-models-had-to-unlearn-c606b9bdb0ab) |
| [How to compare apples with oranges: Proper evaluation of article-level demand forecasts](https://effectsize.io/cases/how-to-compare-apples-with-oranges-proper-evaluation-of/) | Zalando | 2026 | [original](https://www.youtube.com/watch?v=W4rjcvSzB1A) |
| [Application of Object Detection Methods in the Task of Long-Term Event Forecasting](https://effectsize.io/cases/application-of-object-detection-methods-in-the-task-of-long/) | Sber | 2026 | [original](https://habr.com/ru/companies/sberbank/articles/1054286/) · [code](https://effectsize.io/cases/application-of-object-detection-methods-in-the-task-of-long/) |
| [General Neural Network Model with Cross-Module Interaction for Personal Credit Scoring](https://effectsize.io/cases/general-neural-network-model-with-cross-module-interaction/) | Alfa-Bank | 2026 | [original](https://habr.com/ru/companies/alfa/articles/1050626/) |
| [Graph Neural Networks for Personal Default Prediction: How We Tried a New Approach and Didn't Miss the Mark](https://effectsize.io/cases/graph-neural-networks-for-personal-default-prediction-how-we/) | Alfa-Bank | 2026 | [original](https://habr.com/ru/companies/alfa/articles/1050464/) · [code](https://effectsize.io/cases/graph-neural-networks-for-personal-default-prediction-how-we/) |

**[All 333 predictive models cases →](topics/predictive.md)**

### Growth

Onboarding analysis, paywall/pricing experiments, reactivation, virality — when there is an analytical or experimental part.

| Case | Company | Year | Source |
|---|---|---|---|
| [Contextual user education in interfaces: how focusing grows product metrics](https://effectsize.io/cases/contextual-user-education-in-interfaces-how-focusing-grows/) | VK | 2026 | [original](https://habr.com/ru/companies/vk/articles/1053854/) |
| [How we launched a subscription at Alfa-Bank and gathered a million subscribers in six months](https://effectsize.io/cases/how-we-launched-a-subscription-at-alfa-bank-and-gathered-a/) | Alfa-Bank | 2025 | [original](https://habr.com/ru/companies/alfa/articles/967228/) |
| [From Data to Action: How We Scaled Direct Communications in RuStore](https://effectsize.io/cases/from-data-to-action-how-we-scaled-direct-communications-in/) | VK | 2025 | [original](https://habr.com/ru/companies/vk/articles/902056/) |
| [How Avito Used an Interpretable WoE Scorecard to Tell Service Providers How to Get More Orders](https://effectsize.io/cases/how-avito-used-an-interpretable-woe-scorecard-to-tell/) | Avito | 2025 | [original](https://habr.com/ru/companies/avito/articles/879680/) · [code](https://effectsize.io/cases/how-avito-used-an-interpretable-woe-scorecard-to-tell/) |
| [Buyer Journey Insights with Data-Driven Attribution](https://effectsize.io/cases/buyer-journey-insights-with-data-driven-attribution/) | LinkedIn | 2025 | [original](https://linkedin.com/blog/engineering/marketing/buyer-journey-insights-with-data-driven-attribution) |
| [RNNs for data-driven multi-touch attribution at Booking.com](https://effectsize.io/cases/rnns-for-data-driven-multi-touch-attribution-at-booking-com/) | Booking.com | 2024 | [original](https://www.youtube.com/watch?v=Z5cdB6ntJZc) |
| [5 product lessons we learned from building Friend Streak](https://effectsize.io/cases/5-product-lessons-we-learned-from-building-friend-streak/) | Duolingo | 2024 | [original](https://blog.duolingo.com/product-lessons-friend-streak) |
| [Ensuring Even Ad Spend on the Zalando Homepage: How Our New Bidding Algorithm Maximizes Value for Advertisers and Shoppers](https://effectsize.io/cases/ensuring-even-ad-spend-on-the-zalando-homepage-how-our-new/) | Zalando | 2024 | [original](https://engineering.zalando.com/posts/2024/09/even-ad-spend-on-zalando-homepage.html) |

**[All 56 growth cases →](topics/growth.md)**

## Risk

### Fraud

Fraud and abuse detection in a product, transaction and authentication scoring, spam and fake objects/accounts, fraud economics and choosing the anti-fraud target, graph features, golden set for moderation.

| Case | Company | Year | Source |
|---|---|---|---|
| [How We Introduced LLMs into Avito Moderation](https://effectsize.io/cases/how-we-introduced-llms-into-avito-moderation/) | Avito | 2026 | [original](https://habr.com/ru/companies/avito/articles/1095230/) · [code](https://effectsize.io/cases/how-we-introduced-llms-into-avito-moderation/) |
| [Convenient or secure? How we stopped choosing in bot protection](https://effectsize.io/cases/convenient-or-secure-how-we-stopped-choosing-in-bot/) | Yandex | 2026 | [original](https://habr.com/ru/companies/yandex/articles/1089666/) |
| [Everything in Its Place, or How We Built a Single Metric for Hundreds of Antifraud Models](https://effectsize.io/cases/everything-in-its-place-or-how-we-built-a-single-metric-for/) | Avito | 2026 | [original](https://habr.com/ru/companies/avito/articles/1064332/) |
| [Vector search in content moderation: fitting 200+ models into one ensemble](https://effectsize.io/cases/vector-search-in-content-moderation-fitting-200-models-into/) | Wildberries | 2026 | [original](https://habr.com/ru/companies/rwb/articles/1059776/) |
| [Under the hood of a single slider: how bot protection works at Yandex](https://effectsize.io/cases/under-the-hood-of-a-single-slider-how-bot-protection-works/) | Yandex | 2026 | [original](https://habr.com/ru/companies/yandex/articles/1045981/) |
| [About Anti-Fraud and Cats: How to Fight Fraud, Not Just Detect It Better](https://effectsize.io/cases/about-anti-fraud-and-cats-how-to-fight-fraud-not-just-detect/) | Yandex | 2026 | [original](https://www.youtube.com/watch?v=eCrZsHNCJ7Q) |
| [Deploying LLMs in Moderation: From PoC to the Target Solution](https://effectsize.io/cases/deploying-llms-in-moderation-from-poc-to-the-target-solution/) | Avito | 2026 | [original](https://www.youtube.com/watch?v=MURmxFBvuxQ) |
| [How we automated product card moderation with Computer Vision at Wildberries](https://effectsize.io/cases/how-we-automated-product-card-moderation-with-computer/) | Wildberries | 2026 | [original](https://habr.com/ru/companies/rwb/articles/992716/) |

**[All 145 fraud cases →](topics/fraud.md)**

## Data & practice

### Insights

Metric change analysis (root cause), metric decomposition, anomaly detection, auto-insights, exploratory analysis frameworks.

| Case | Company | Year | Source |
|---|---|---|---|
| [Databricks on Databricks: Automating Service Reliability at Scale](https://effectsize.io/cases/databricks-on-databricks-automating-service-reliability-at/) | Databricks | 2026 | [original](https://www.databricks.com/dataaisummit/session/databricks-databricks-automating-service-reliability-scale) · [code](https://effectsize.io/cases/databricks-on-databricks-automating-service-reliability-at/) |
| [The Math of Clusters: Understanding Smart Data Clustering Through Our Log Anomaly Detection System. Part 1](https://effectsize.io/cases/the-math-of-clusters-understanding-smart-data-clustering/) | MTS | 2026 | [original](https://habr.com/ru/companies/ru_mts/articles/1037752/) |
| [When Metrics Go Crazy: Automatic Anomaly Detection in Time Series in Yandex Monium](https://effectsize.io/cases/when-metrics-go-crazy-automatic-anomaly-detection-in-time/) | Yandex | 2026 | [original](https://habr.com/ru/companies/yandex/articles/1035520/) |
| [How and why we built a system for analyzing anomalous logs. The MWS case](https://effectsize.io/cases/how-and-why-we-built-a-system-for-analyzing-anomalous-logs/) | MTS | 2025 | [original](https://habr.com/ru/companies/ru_mts/articles/977624/) |
| [DrP: Meta’s Root Cause Analysis Platform at Scale](https://effectsize.io/cases/drp-meta-s-root-cause-analysis-platform-at-scale/) | Meta | 2025 | [original](https://engineering.fb.com/2025/12/19/data-infrastructure/drp-metas-root-cause-analysis-platform-at-scale) |
| [How we taught ML to group 50,000 events into incidents](https://effectsize.io/cases/how-we-taught-ml-to-group-50-000-events-into-incidents/) | MTS | 2025 | [original](https://habr.com/ru/companies/oleg-bunin/articles/929928/) |
| [Methods for Analyzing Text Data from User Support Requests](https://effectsize.io/cases/methods-for-analyzing-text-data-from-user-support-requests/) | T-Bank | 2025 | [original](https://habr.com/ru/companies/tbank/articles/899130/) |
| [The Quest to Understand Metric Movements](https://effectsize.io/cases/the-quest-to-understand-metric-movements/) | Pinterest | 2025 | [original](https://medium.com/pinterest-engineering/the-quest-to-understand-metric-movements-8ab12ae97cda) |

**[All 122 insights cases →](topics/insights.md)**

### Analytics practice

Data-informed processes, experimentation culture, how an analyst works with the product, hypothesis prioritization.

| Case | Company | Year | Source |
|---|---|---|---|
| [Your First Process Mining Project: How to Choose a Process to Optimize, Build a Team and Not Get Stuck at the Pilot Stage](https://effectsize.io/cases/your-first-process-mining-project-how-to-choose-a-process-to/) | VK | 2026 | [original](https://habr.com/ru/companies/vktech/articles/1100106/) |
| [The Real ROI of Experimentation](https://effectsize.io/cases/the-real-roi-of-experimentation/) | Spotify | 2026 | [original](https://confidence.spotify.com/blog/experimentation-roi) |
| [A Redesign Nobody Asked For, and Everyone Ended Up Happy](https://effectsize.io/cases/a-redesign-nobody-asked-for-and-everyone-ended-up-happy/) | Alfa-Bank | 2025 | [original](https://habr.com/ru/companies/alfa/articles/931938/) |
| [Thousands of hours saved for a UX researcher: how we taught AI to do the routine (and our system prompts)](https://effectsize.io/cases/thousands-of-hours-saved-for-a-ux-researcher-how-we-taught/) | Alfa-Bank | 2025 | [original](https://habr.com/ru/companies/alfa/articles/917114/) |
| [Analytics, Data, Metrics and Motivation: How to Build a Data Labeling Process in a Large Bank](https://effectsize.io/cases/analytics-data-metrics-and-motivation-how-to-build-a-data/) | Alfa-Bank | 2025 | [original](https://www.youtube.com/watch?v=P18akQ6oyUY) |
| [How We Learned to Manage Metrics and Why It's Important for the Product](https://effectsize.io/cases/how-we-learned-to-manage-metrics-and-why-it-s-important-for/) | Sber | 2025 | [original](https://habr.com/ru/companies/sberbank/articles/883228/) |
| [Data Strategy in a Large Group of Companies](https://effectsize.io/cases/data-strategy-in-a-large-group-of-companies/) | MTS | 2024 | [original](https://www.youtube.com/watch?v=8b1PbxcAyQo) |
| [Beating Routine in Data Science: How to Stop Being Under-Programmers and Under-Researchers](https://effectsize.io/cases/beating-routine-in-data-science-how-to-stop-being-under/) | Alfa-Bank | 2024 | [original](https://habr.com/ru/companies/alfa/articles/788290/) |

**[All 88 analytics practice cases →](topics/analytics-practice.md)**

### Data infrastructure

Event pipelines, event stores, feature store — only if directly tied to the topics above.

| Case | Company | Year | Source |
|---|---|---|---|
| [From Data Silos to Feature Serving: How We Unified Fragmented Data for Training, Inference, and Reuse](https://effectsize.io/cases/from-data-silos-to-feature-serving-how-we-unified-fragmented/) | HubSpot | 2026 | [original](https://product.hubspot.com/blog/from-data-silos-to-feature-serving-how-we-unified-fragmented-data-for-training-inference-and-reuse) |
| [Refreshing the Travel-Time Map Behind Lyft’s Marketplace: Rebuilding Neighborhood Reachability Signals](https://effectsize.io/cases/refreshing-the-travel-time-map-behind-lyft-s-marketplace/) | Lyft | 2026 | [original](https://eng.lyft.com/refreshing-the-travel-time-map-behind-lyfts-marketplace-rebuilding-neighborhood-reachability-5be3efbc82ea) |
| [Ultra Low Latency Streaming for Real-Time Feature Engineering](https://effectsize.io/cases/ultra-low-latency-streaming-for-real-time-feature/) | Databricks | 2026 | [original](https://www.databricks.com/dataaisummit/session/ultra-low-latency-streaming-real-time-feature-engineering) |
| [FIFO on millions of rows: how to make bonuses, SQL and an asymmetric N×M graph work together](https://effectsize.io/cases/fifo-on-millions-of-rows-how-to-make-bonuses-sql-and-an/) | Avito | 2026 | [original](https://habr.com/ru/companies/avito/articles/1043532/) |
| [A Speech Platform in Production](https://effectsize.io/cases/a-speech-platform-in-production/) | X5 Tech | 2026 | [original](https://www.youtube.com/watch?v=zCD017S2vm4) |
| [An Authorization Model in a Lakehouse Without Downtime](https://effectsize.io/cases/an-authorization-model-in-a-lakehouse-without-downtime/) | X5 Tech | 2026 | [original](https://www.youtube.com/watch?v=3OgAIikAsNk) |
| [Real-Time Analytics on ClickHouse](https://effectsize.io/cases/real-time-analytics-on-clickhouse/) | X5 Tech | 2026 | [original](https://www.youtube.com/watch?v=ms4vgIf13EY) |
| [Balancing Speed and Accuracy in Digital Order Fulfillment: The Next-Gen Solution](https://effectsize.io/cases/balancing-speed-and-accuracy-in-digital-order-fulfillment/) | Target | 2026 | [original](https://tech.target.com/blog/balancing-speed-and-accuracy-digital-fulfillment) |

**[All 109 data infrastructure cases →](topics/data-infra.md)**

## Top companies

[Spotify](companies/spotify.md) (99) · [Yandex](companies/yandex.md) (91) · [Avito](companies/avito.md) (90) · [Alfa-Bank](companies/alfa-bank.md) (70) · [DoorDash](companies/doordash.md) (68) · [Sber](companies/sber.md) (60) · [Meta](companies/meta.md) (51) · [VK](companies/vk.md) (51) · [Microsoft](companies/microsoft.md) (51) · [X5 Tech](companies/x5-tech.md) (50) · [Pinterest](companies/pinterest.md) (48) · [LinkedIn](companies/linkedin.md) (43) · [Netflix](companies/netflix.md) (42) · [MTS](companies/mts.md) (39) · [T-Bank](companies/t-bank.md) (33) · [Instacart](companies/instacart.md) (33) · [Wildberries](companies/wildberries.md) (28) · [Airbnb](companies/airbnb.md) (28) · [Booking.com](companies/booking-com.md) (26) · [GetYourGuide](companies/getyourguide.md) (24) · [Nubank](companies/nubank.md) (24) · [Lyft](companies/lyft.md) (24) · [Databricks](companies/databricks.md) (24) · [Uber](companies/uber.md) (23) · [Grab](companies/grab.md) (23) · [Trendyol](companies/trendyol.md) (23) · [VTB](companies/vtb.md) (23) · [Walmart](companies/walmart.md) (23) · [Shopify](companies/shopify.md) (22) · [Amazon](companies/amazon.md) (21) · [Monzo](https://effectsize.io/?company=monzo) (21) · [Magnit Tech](https://effectsize.io/?company=magnit-tech) (20) · [Apple](https://effectsize.io/?company=apple) (20) · [Ozon Tech](https://effectsize.io/?company=ozon-tech) (20) · [Expedia Group](https://effectsize.io/?company=expedia-group) (20) · [Etsy](https://effectsize.io/?company=etsy) (19) · [Algolia](https://effectsize.io/?company=algolia) (18) · [Kuper](https://effectsize.io/?company=kuper) (18) · [Yandex Lavka](https://effectsize.io/?company=yandex-lavka) (15) · [Mercari](https://effectsize.io/?company=mercari) (15)

## FAQ

**How do I find A/B testing case studies?** Open [A/B testing](topics/ab-testing.md) or [Advanced experimentation](topics/experimentation-advanced.md): CUPED and variance reduction, sequential testing, switchback and interleaving experiments, each linked to the original post.

**Where are machine learning case studies by company?** See [By company](companies/README.md), e.g. [Spotify](companies/spotify.md), [Yandex](companies/yandex.md), [Avito](companies/avito.md), [Alfa-Bank](companies/alfa-bank.md).

**Can I use the data?** Yes: [data/cases.csv](data/cases.csv) and [data/cases.json](data/cases.json) list titles, companies, years, topics and links (no article text), under CC BY 4.0.

**Where is the code?** Cases marked `code` link to repositories; the links are on the case page on effectsize.io (free sign-in with Google or an email code).

## Use it with your AI agent

Connect the archive to **Claude, ChatGPT or Cursor** over MCP. Describe your problem; your agent searches the cases, reads the closest ones and tells you what worked elsewhere, with links to the originals, code and slides.

```bash
claude mcp add --transport http --scope user effectsize https://mcp.effectsize.io/mcp
```

Setup for other clients: **[effectsize.io/mcp](https://effectsize.io/mcp/)** · free, sign in with Google or an email code.

## Related

- [data-ml-engineering-blogs](https://github.com/vzhyvov/data-ml-engineering-blogs) — data science and ML engineering blogs by industry (with OPML).
- [effectsize.io](https://effectsize.io) — browse and filter the cases, read the digests.

## Contributing

Know a strong case study — a real product problem and a disclosed method? [Suggest it](../../issues/new/choose). See [CONTRIBUTING.md](CONTRIBUTING.md). Authors can ask to correct or remove a case: [effectsize.io/authors](https://effectsize.io/authors/).

## Cite

effectsize.io, *Data Science Case Studies*, https://github.com/vzhyvov/data-science-case-studies (use “Cite this repository”).

## License

Lists and data: [CC BY 4.0](LICENSE). Linked articles and digests belong to their authors.
