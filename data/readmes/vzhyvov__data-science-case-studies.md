# Data Science Case Studies: ML, A/B Testing and Product Analytics

How real companies solved product analytics, experimentation and machine-learning problems: case studies from engineering blogs and conference talks, grouped by topic. Each entry has the company, the year, a link to the original and a structured digest.

![cases](https://img.shields.io/badge/cases-1247-6B4EE6) ![companies](https://img.shields.io/badge/companies-285-6B4EE6) ![updated](https://img.shields.io/badge/updated-2026--11--17-lightgrey) ![license](https://img.shields.io/badge/license-CC_BY_4.0-lightgrey)

**Jump to:** [A/B testing](topics/ab-testing.md) · [Recommendations](topics/recsys.md) · [Search](topics/search.md) · [Causal inference](topics/causal.md) · [LLM in analytics](topics/llm-in-analytics.md) · [Fraud](topics/fraud.md) · [All topics](#contents) · [By company](companies/README.md) · [CSV / JSON](data/)

Read the digests on **[effectsize.io](https://effectsize.io)**, or search them from Claude, ChatGPT or Cursor over MCP: `claude mcp add --transport http --scope user effectsize https://mcp.effectsize.io/mcp` ([setup](https://effectsize.io/mcp/)).

## Contents

- **Experiments & causal**: [Metrics](#metrics) (29) · [A/B testing](#ab-testing) (73) · [Advanced experimentation](#advanced-experimentation) (34) · [Causal inference](#causal-inference) (43) · [Uplift](#uplift) (16)
- **Recs & search**: [Recommendations](#recommendations) (220) · [Personalization](#personalization) (57) · [Search](#search) (142)
- **LLM**: [LLM in analytics](#llm-in-analytics) (242)
- **Predictive & behavior**: [Clickstream](#clickstream) (13) · [Behavior](#behavior) (15) · [Predictive models](#predictive-models) (147) · [Growth](#growth) (15)
- **Risk**: [Fraud](#fraud) (71)
- **Data & practice**: [Insights](#insights) (45) · [Analytics practice](#analytics-practice) (25) · [Data infrastructure](#data-infrastructure) (60)
- [Top companies](#top-companies) · [FAQ](#faq) · [Use it with your AI agent](#use-it-with-your-ai-agent)

## Experiments & causal

### Metrics

North Star, metric trees, proxy and surrogate metrics, guardrails, LTV/unit economics in a product context.

| Case | Company | Year | Source |
|---|---|---|---|
| [Metrics Board: Building an Agent-ready Metrics Layer](https://effectsize.io/cases/metrics-board-building-an-agent-ready-metrics-layer/) | Pinterest | 2026 | [original](https://medium.com/pinterest-engineering/metrics-board-building-an-agent-ready-metrics-layer-2c8fefe68756) |
| [How we built it: Real-time analytics for Stripe Billing](https://effectsize.io/cases/how-we-built-it-real-time-analytics-for-stripe-billing/) | Stripe | 2025 | [original](https://stripe.com/blog/how-we-built-it-real-time-analytics-for-stripe-billing) |
| [Behind the metric: how we developed “Time Spent Learning Well”](https://effectsize.io/cases/behind-the-metric-how-we-developed-time-spent-learning-well/) | Duolingo | 2024 | [original](https://blog.duolingo.com/time-spent-learning-well) |
| [Airbnb Brandometer: Powering brand perception measurement on social media data with AI](https://effectsize.io/cases/airbnb-brandometer-powering-brand-perception-measurement-on/) | Airbnb | 2024 | [original](https://medium.com/airbnb-engineering/airbnb-brandometer-powering-brand-perception-measurement-on-social-media-data-with-ai-c83019408051) |
| [Why Khan Academy will be using "skills to proficient" to measure learning outcomes (and you should too!)](https://effectsize.io/cases/why-khan-academy-will-be-using-skills-to-proficient-to/) | Khan Academy | 2023 | [original](https://blog.khanacademy.org/why-khan-academy-will-be-using-skills-to-proficient-to-measure-learning-outcomes) |
| [Quantifying Efficiency in Ridesharing Marketplaces](https://effectsize.io/cases/quantifying-efficiency-in-ridesharing-marketplaces/) | Lyft | 2023 | [original](https://eng.lyft.com/quantifying-efficiency-in-ridesharing-marketplaces-affd53043db2) |
| [Meaningful metrics: How data sharpened the focus of product teams](https://effectsize.io/cases/meaningful-metrics-how-data-sharpened-the-focus-of-product/) | Duolingo | 2023 | [original](https://blog.duolingo.com/growth-model-duolingo) |
| [How Zillow Data Science Measures Business Outcomes with Bayesian Statistics](https://effectsize.io/cases/how-zillow-data-science-measures-business-outcomes-with/) | Zillow | 2023 | [original](https://zillow.com/tech/how-zillow-data-science-measures-business-outcomes-with-bayesian-statistics) |

**[All 29 metrics cases →](topics/metrics.md)**

### A/B testing

Design, power and MDE, variance reduction (CUPED, stratification), sequential testing, multiple comparisons, SRM, peeking, ratio metrics, bootstrap, experimentation platforms.

| Case | Company | Year | Source |
|---|---|---|---|
| [Why Spotify Is Not Using Bayesian A/B Testing](https://effectsize.io/cases/why-spotify-is-not-using-bayesian-a-b-testing/) | Spotify | 2026 | [original](https://engineering.atspotify.com/2026/9/why-spotify-is-not-using-bayesian-a-b-testing) |
| [When Can LLMs Replace Humans in A/B Tests?](https://effectsize.io/cases/when-can-llms-replace-humans-in-a-b-tests/) | Spotify | 2026 | [original](https://engineering.atspotify.com/2026/8/when-can-llms-replace-humans-in-a-b-tests) |
| [Bootstrap Confidence Intervals for LLM Evaluation](https://effectsize.io/cases/bootstrap-confidence-intervals-for-llm-evaluation/) | Indeed | 2026 | [original](https://engineering.indeedblog.com/blog/2026/07/bootstrap-confidence-intervals-for-llm-evaluation) |
| [ABsalute: A/B Testing Automation](https://effectsize.io/cases/absalute-a-b-testing-automation/) | X5 Tech | 2026 | [original](https://www.youtube.com/watch?v=IUTFlXp_Oos) |
| [Why Reports Mislead, or How to Measure the Effect of an LLM Feature](https://effectsize.io/cases/why-reports-mislead-or-how-to-measure-the-effect-of-an-llm/) | Sber | 2026 | [original](https://www.youtube.com/watch?v=VLt4vY2icms) |
| [Better Experiments with LLM Evals — A funnel, not a fork](https://effectsize.io/cases/better-experiments-with-llm-evals-a-funnel-not-a-fork/) | Spotify | 2026 | [original](https://engineering.atspotify.com/2026/5/better-experiments-with-llm-evals-a-funnel-not-a-fork) |
| [Measure Less to Learn More: Using Fewer, Higher-quality Metrics to Capture What Matters](https://effectsize.io/cases/measure-less-to-learn-more-using-fewer-higher-quality/) | Discord | 2026 | [original](https://discord.com/blog/measure-less-to-learn-more-using-fewer-higher-quality-metrics-to-capture-what-matters) |
| [Reducing experiment duration with predicted control variates](https://effectsize.io/cases/reducing-experiment-duration-with-predicted-control-variates/) | Etsy | 2025 | [original](https://etsy.com/codeascraft/reducing-experiment-duration-with-predicted-control-variates) |

**[All 73 a/b testing cases →](topics/ab-testing.md)**

### Advanced experimentation

Network effects and interference, two-sided marketplaces, switchback, cluster randomization, long-term effects, bandits, interleaving.

| Case | Company | Year | Source |
|---|---|---|---|
| [Powering AI-led research through simulation](https://effectsize.io/cases/powering-ai-led-research-through-simulation/) | Grab | 2026 | [original](https://engineering.grab.com/powering-ai-led-research-through-simulation) |
| [Variance Reduction Below the Randomization Grain](https://effectsize.io/cases/variance-reduction-below-the-randomization-grain/) | Instacart | 2026 | [original](https://tech.instacart.com/variance-reduction-below-the-randomization-grain-31719f87a7d2) |
| [Leveraging PyFixest for High-Cardinality Marketplace Modeling at Instacart](https://effectsize.io/cases/leveraging-pyfixest-for-high-cardinality-marketplace/) | Instacart | 2026 | [original](https://tech.instacart.com/leveraging-pyfixest-for-high-cardinality-marketplace-modeling-at-instacart-3913df91a04b) · [code](https://effectsize.io/cases/leveraging-pyfixest-for-high-cardinality-marketplace/) |
| [Beyond A/B Testing: Using Surrogacy and Region-Splits to Measure Long-Term Effects in Marketplaces](https://effectsize.io/cases/beyond-a-b-testing-using-surrogacy-and-region-splits-to/) | Lyft | 2026 | [original](https://eng.lyft.com/beyond-a-b-testing-using-surrogacy-and-region-splits-to-measure-long-term-effects-in-marketplaces-9cb06d628f2d) |
| [Interleaving for Accelerated Testing](https://effectsize.io/cases/interleaving-for-accelerated-testing/) | Expedia Group | 2026 | [original](https://medium.com/expedia-group-tech/interleaving-for-accelerated-testing-75adc644027b) |
| [How Yelp Built a Back-Testing Engine for Safer, Smarter Ad Budget Allocation](https://effectsize.io/cases/how-yelp-built-a-back-testing-engine-for-safer-smarter-ad/) | Yelp | 2026 | [original](https://engineeringblog.yelp.com/2026/02/how-yelp-built-a-back-testing-engine-for-safer-smarter-ad-budget-allocation.html) |
| [Solving Dispatch in a Ridesharing Problem Space](https://effectsize.io/cases/solving-dispatch-in-a-ridesharing-problem-space/) | Lyft | 2025 | [original](https://eng.lyft.com/solving-dispatch-in-a-ridesharing-problem-space-821d9606c3ff) |
| [Using Marketplace Marginal Values to Address Interference Bias](https://effectsize.io/cases/using-marketplace-marginal-values-to-address-interference/) | Lyft | 2025 | [original](https://eng.lyft.com/using-marketplace-marginal-values-to-address-interference-bias-a11aff6e670f) |

**[All 34 advanced experimentation cases →](topics/experimentation-advanced.md)**

### Causal inference

DiD, synthetic control, RDD, IV, matching/PSM, CausalImpact, effect estimation without an A/B test, double ML.

| Case | Company | Year | Source |
|---|---|---|---|
| [A Human-Augmenting Agentic Workflow for Causal Inference](https://effectsize.io/cases/a-human-augmenting-agentic-workflow-for-causal-inference/) | Netflix | 2026 | [original](https://netflixtechblog.com/a-human-augmenting-agentic-workflow-for-causal-inference-4623f0a9c5af) · [code](https://effectsize.io/cases/a-human-augmenting-agentic-workflow-for-causal-inference/) |
| [Evolution of the Databricks Commercial Motion: Building Scalable Intelligence on Databricks](https://effectsize.io/cases/evolution-of-the-databricks-commercial-motion-building/) | Databricks | 2026 | [original](https://www.databricks.com/dataaisummit/session/evolution-databricks-commercial-motion-building-scalable-intelligence) |
| [How Developer Productivity Changed with AI4SDLC Tools](https://effectsize.io/cases/how-developer-productivity-changed-with-ai4sdlc-tools/) | T-Bank | 2026 | [original](https://www.youtube.com/watch?v=AKfcnrTZXYY) |
| [Problems and Prospects of Causal AI](https://effectsize.io/cases/problems-and-prospects-of-causal-ai/) | Sber | 2026 | [original](https://www.youtube.com/watch?v=5dAXL2yP3Ow) |
| [The New Policy Hasn't Run Yet: Comparing It to the Old One Before an A/B Test](https://effectsize.io/cases/the-new-policy-hasn-t-run-yet-comparing-it-to-the-old-one/) | Sber | 2026 | [original](https://www.youtube.com/watch?v=UeHoi7uLT1I) |
| [Trusting the Untestable: Validation and Diagnostics for the Doubly Robust Models](https://effectsize.io/cases/trusting-the-untestable-validation-and-diagnostics-for-the/) | Lyft | 2026 | [original](https://eng.lyft.com/trusting-the-untestable-validation-and-diagnostics-for-the-doubly-robust-models-00853df009df) |
| [My Starter Project on the Lyft Rider Data Science Team](https://effectsize.io/cases/my-starter-project-on-the-lyft-rider-data-science-team/) | Lyft | 2025 | [original](https://eng.lyft.com/my-starter-project-on-the-lyft-rider-data-science-team-86a60dddd935) |
| [Khan Academy Improves State Test Scores: Results from New 3-Year Efficacy Study](https://effectsize.io/cases/khan-academy-improves-state-test-scores-results-from-new-3/) | Khan Academy | 2025 | [original](https://blog.khanacademy.org/khan-academy-improves-state-test-scores-results-from-new-3-year-efficacy-study) |

**[All 43 causal inference cases →](topics/causal.md)**

### Uplift

CATE, meta-learners (S/T/X/R/DR), uplift trees, communication and promo targeting, policy learning, uplift evaluation (Qini, AUUC).

| Case | Company | Year | Source |
|---|---|---|---|
| [Smarter promotions with causal machine learning](https://effectsize.io/cases/smarter-promotions-with-causal-machine-learning/) | DoorDash | 2025 | [original](https://careersatdoordash.com/blog/doordash-smarter-promotions-with-causal-machine-learning) |
| [How We Grew Sales Team Efficiency with Customer Ranking](https://effectsize.io/cases/how-we-grew-sales-team-efficiency-with-customer-ranking/) | Avito | 2025 | [original](https://www.youtube.com/watch?v=1ozHNMcpLyw) |
| [How machine learning supercharged our revenue by millions of dollars](https://effectsize.io/cases/how-machine-learning-supercharged-our-revenue-by-millions-of/) | Duolingo | 2025 | [original](https://blog.duolingo.com/machine-learning-ads/) |
| [Experimenting with Machine Learning to Target In-App Messaging](https://effectsize.io/cases/experimenting-with-machine-learning-to-target-in-app/) | Spotify | 2023 | [original](https://engineering.atspotify.com/2023/06/experimenting-with-machine-learning-to-target-in-app-messaging) |
| [Improving Instagram notification management with machine learning and causal inference](https://effectsize.io/cases/improving-instagram-notification-management-with-machine/) | Meta | 2022 | [original](https://engineering.fb.com/2022/10/31/ml-applications/instagram-notification-management-machine-learning) |
| [How The New York Times Uses Machine Learning To Make Its Paywall Smarter](https://effectsize.io/cases/how-the-new-york-times-uses-machine-learning-to-make-its/) | The New York Times | 2022 | [original](https://open.nytimes.com/how-the-new-york-times-uses-machine-learning-to-make-its-paywall-smarter-e5771d5f46f8) |
| [Building for Balance](https://effectsize.io/cases/building-for-balance/) | Instacart | 2022 | [original](https://tech.instacart.com/building-for-balance-e61fb9511893) |
| [Scaling Subscriptions at The New York Times with Real-Time Causal Machine Learning](https://effectsize.io/cases/scaling-subscriptions-at-the-new-york-times-with-real-time/) | The New York Times | 2025 | [original](https://open.nytimes.com/scaling-subscriptions-at-the-new-york-times-with-real-time-causal-machine-learning-5f23a7b24ff4) |

**[All 16 uplift cases →](topics/uplift.md)**

## Recs & search

### Recommendations

Candidate generation, ranking, embeddings, sequential/session-based recommendations, cold start, diversity, feedback loops, offline/online evaluation.

| Case | Company | Year | Source |
|---|---|---|---|
| [Safe and Efficient Multi-Epoch Embedding Training](https://effectsize.io/cases/safe-and-efficient-multi-epoch-embedding-training/) | Pinterest | 2026 | [original](https://medium.com/pinterest-engineering/safe-and-efficient-multi-epoch-embedding-training-103bec2abc83) |
| [Meta Andromeda: Powering the Next Generation of Ads Retrieval Through Model-System Co-Design](https://effectsize.io/cases/meta-andromeda-powering-the-next-generation-of-ads-retrieval/) | Meta | 2026 | [original](https://engineering.fb.com/2026/10/28/ml-applications/meta-andromeda-next-gen-ads-retrieval-gpu-co-design) |
| [GenRecs Tokenization: Transforming Ads Recommendation at Meta with Stable Model Vocabulary](https://effectsize.io/cases/genrecs-tokenization-transforming-ads-recommendation-at-meta/) | Meta | 2026 | [original](https://engineering.fb.com/2026/10/19/ml-applications/genrecs-tokenization-transforming-ads-recommendation-at-meta-with-stable-model-vocabulary) |
| [Measuring the Impact of Personalized Recommendations](https://effectsize.io/cases/measuring-the-impact-of-personalized-recommendations/) | Netflix | 2026 | [original](https://netflixtechblog.com/measuring-the-impact-of-personalized-recommendations-4c26be3a4d96) |
| [Meta’s Generative Ads Model (GEM): Scaling the Central Model and Compute Engine for Frontier Ads AI](https://effectsize.io/cases/meta-s-generative-ads-model-gem-scaling-the-central-model/) | Meta | 2026 | [original](https://engineering.fb.com/2026/10/13/ml-applications/generative-ads-model-gem-scaling-frontier-ads-ai/) |
| [Advancing Generative Recommendation Inference: our collaboration with NVIDIA on TensorRT LLM](https://effectsize.io/cases/advancing-generative-recommendation-inference-our/) | Spotify | 2026 | [original](https://engineering.atspotify.com/2026/10/advancing-generative-recommendation-inference-our-collaboration-with-nvidia-on-tensorrt-llm) · [code](https://effectsize.io/cases/advancing-generative-recommendation-inference-our/) |
| [The guest journey, updated in real time: extending Airbnb’s sequence recommender with Chronon](https://effectsize.io/cases/the-guest-journey-updated-in-real-time-extending-airbnb-s/) | Airbnb | 2026 | [original](https://medium.com/airbnb-engineering/the-guest-journey-updated-in-real-time-extending-airbnbs-sequence-recommender-with-chronon-8f1582578553) · [code](https://effectsize.io/cases/the-guest-journey-updated-in-real-time-extending-airbnb-s/) |
| [Beyond Two Towers: Launching the 3-Tower Engagement Co-Train Model (Part 2)](https://effectsize.io/cases/beyond-two-towers-launching-the-3-tower-engagement-co-train/) | Pinterest | 2026 | [original](https://medium.com/pinterest-engineering/beyond-two-towers-launching-the-3-tower-engagement-co-train-model-part-2-0b96167d2c14) |

**[All 220 recommendations cases →](topics/recsys.md)**

### Personalization

Personalized UX, content, notifications, pricing and offers, contextual bandits, next-best-action.

| Case | Company | Year | Source |
|---|---|---|---|
| [From Activity to Intent: Generating User Journeys with LLMs](https://effectsize.io/cases/from-activity-to-intent-generating-user-journeys-with-llms/) | Pinterest | 2026 | [original](https://medium.com/pinterest-engineering/from-activity-to-intent-generating-user-journeys-with-llms-9652b9417626) |
| [Personalization without user identity](https://effectsize.io/cases/personalization-without-user-identity/) | Airbnb | 2026 | [original](https://medium.com/airbnb-engineering/personalization-without-user-identity-8e7891a1d486) |
| [MAPS: Netflix’s Multimodal Asset Personalization at Scale](https://effectsize.io/cases/maps-netflix-s-multimodal-asset-personalization-at-scale/) | Netflix | 2026 | [original](https://netflixtechblog.com/maps-netflixs-multimodal-asset-personalization-at-scale-32f96320785e) |
| [Thinking Fast & Slow for a Personalized Notification System](https://effectsize.io/cases/thinking-fast-slow-for-a-personalized-notification-system/) | Netflix | 2026 | [original](https://netflixtechblog.com/thinking-fast-slow-for-a-personalized-notification-system-4d89b26525cd) |
| [TargetRun: AI-Powered Trip Prediction for Delivering Timely Offers](https://effectsize.io/cases/targetrun-ai-powered-trip-prediction-for-delivering-timely/) | Target | 2026 | [original](https://tech.target.com/blog/targetrun-shopping-offers) |
| [What If Your Page Layout Could Learn? Optimizing with Bandits](https://effectsize.io/cases/what-if-your-page-layout-could-learn-optimizing-with-bandits/) | Target | 2026 | [original](https://tech.target.com/blog/page-layout-optimization-bandits) |
| [Inside the Archive: The Tech Behind Your 2025 Wrapped Highlights](https://effectsize.io/cases/inside-the-archive-the-tech-behind-your-2025-wrapped/) | Spotify | 2026 | [original](https://engineering.atspotify.com/2026/3/inside-the-archive-2025-wrapped) |
| [When GenAI Meets Personalization: Powering DoorDash's next-generation homepage experience](https://effectsize.io/cases/when-genai-meets-personalization-powering-doordash-s-next/) | DoorDash | 2025 | [original](https://careersatdoordash.com/blog/doordashs-next-generation-homepage-genai) |

**[All 57 personalization cases →](topics/personalization.md)**

### Search

Ranking, learning-to-rank, query understanding, autocomplete, relevance and its labeling, search metrics, semantic/hybrid search in a product.

| Case | Company | Year | Source |
|---|---|---|---|
| [CASTLE: training natural language search before the first real query](https://effectsize.io/cases/castle-training-natural-language-search-before-the-first/) | Airbnb | 2026 | [original](https://medium.com/airbnb-engineering/castle-training-natural-language-search-before-the-first-real-query-3818ef8b4828) |
| [Automating Search Relevance Assessment at Scale with LLM-as-a-Judge](https://effectsize.io/cases/automating-search-relevance-assessment-at-scale-with-llm-as/) | Allegro | 2026 | [original](https://blog.allegro.tech/2026/08/automating-search-relevance-llm-as-a-judge.html) |
| [Personalizing Airbnb search by learning from the guest journey](https://effectsize.io/cases/personalizing-airbnb-search-by-learning-from-the-guest/) | Airbnb | 2026 | [original](https://medium.com/airbnb-engineering/personalizing-airbnb-search-by-learning-from-the-guest-journey-bcefd1915624) |
| [Effective document management and retrieval for generative AI](https://effectsize.io/cases/effective-document-management-and-retrieval-for-generative/) | Databricks | 2026 | [original](https://www.databricks.com/dataaisummit/session/effective-document-management-and-retrieval-generative-ai) |
| [Thinking Fast & Slow: How Databricks Built High-Speed and Deep Research Agents](https://effectsize.io/cases/thinking-fast-slow-how-databricks-built-high-speed-and-deep/) | Databricks | 2026 | [original](https://www.databricks.com/dataaisummit/session/thinking-fast-slow-how-databricks-built-high-speed-and-deep-research) |
| [Semantic Search for AI Agents at Scale: Retrieval and Ranking for LinkedIn’s Hiring Assistant](https://effectsize.io/cases/semantic-search-for-ai-agents-at-scale-retrieval-and-ranking/) | LinkedIn | 2026 | [original](https://linkedin.com/blog/engineering/ai/semantic-search-for-ai-agents-at-scale-retrieval-and-ranking-for-linkedins-hiring-assistant) |
| [Shaping product understanding with contrastive reinforcement learning](https://effectsize.io/cases/shaping-product-understanding-with-contrastive-reinforcement/) | Etsy | 2026 | [original](https://etsy.com/codeascraft/shaping-product-understanding-with-contrastive-reinforcement-learning) |
| [AI Blender in Search: How We Stopped Worshipping Clicks and Moved Block Placement to LLMs](https://effectsize.io/cases/ai-blender-in-search-how-we-stopped-worshipping-clicks-and/) | Yandex | 2026 | [original](https://www.youtube.com/watch?v=KBizYjojiqY) |

**[All 142 search cases →](topics/search.md)**

## LLM

### LLM in analytics

LLMs for data analysis, evaluating LLM features with experiments, LLM ranking and recommendations.

| Case | Company | Year | Source |
|---|---|---|---|
| [How Pinterest Improved Analytics Agent Compliance with Loop Engineering](https://effectsize.io/cases/how-pinterest-improved-analytics-agent-compliance-with-loop/) | Pinterest | 2026 | [original](https://medium.com/pinterest-engineering/how-pinterest-improved-analytics-agent-compliance-with-loop-engineering-d3c52d0abaa2) |
| [Fact-Checking at Scale: Building a More Accurate and Efficient Synopsis Factuality System](https://effectsize.io/cases/fact-checking-at-scale-building-a-more-accurate-and/) | Netflix | 2026 | [original](https://netflixtechblog.com/fact-checking-at-scale-building-a-more-accurate-and-efficient-synopsis-factuality-system-d7d85859d808) |
| [Inside LinkedIn's data context layer: curating trustworthy context for humans and agents](https://effectsize.io/cases/inside-linkedin-s-data-context-layer-curating-trustworthy/) | LinkedIn | 2026 | [original](https://linkedin.com/blog/engineering/infrastructure/inside-linkedins-data-context-layer-curating-trustworthy-context-for-humans-and-agents) |
| [Workbench: Building an AI Content Generation and Quality Assurance System at Scale](https://effectsize.io/cases/workbench-building-an-ai-content-generation-and-quality/) | Thumbtack | 2026 | [original](https://medium.com/thumbtack-engineering/workbench-building-an-ai-content-generation-and-quality-assurance-system-at-scale-7a381b47c640) |
| [Building Gavel: AI evaluation infrastructure across Eternal](https://effectsize.io/cases/building-gavel-ai-evaluation-infrastructure-across-eternal/) | Zomato | 2026 | [original](https://zomato.com/blog/building-gavel-ai-evaluation-infrastructure-across-eternal) |
| [Inside Vera, DoorDash’s Data Agent](https://effectsize.io/cases/inside-vera-doordash-s-data-agent/) | DoorDash | 2026 | [original](https://careersatdoordash.com/blog/inside-vera-doordashs-data-agent) |
| [The Lifecycle of LLM-as-a-Judge: Building, Aligning, and Monitoring at scale](https://effectsize.io/cases/the-lifecycle-of-llm-as-a-judge-building-aligning-and/) | Netflix | 2026 | [original](https://netflixtechblog.com/the-lifecycle-of-llm-as-a-judge-building-aligning-and-monitoring-at-scale-c95bd8283508) |
| [Building Jarvis Pro: Route first, answer later](https://effectsize.io/cases/building-jarvis-pro-route-first-answer-later/) | Grab | 2026 | [original](https://engineering.grab.com/jarvis-pro-route-firsr-answer-later) |

**[All 242 llm in analytics cases →](topics/llm-in-analytics.md)**

## Predictive & behavior

### Clickstream

Sessionization, paths and funnels, process mining, sequence mining, transitions between events, journey maps, tracking plan and event design.

| Case | Company | Year | Source |
|---|---|---|---|
| [Advanced SQL Patterns for Production Analytics](https://effectsize.io/cases/advanced-sql-patterns-for-production-analytics/) | Databricks | 2026 | [original](https://www.databricks.com/dataaisummit/session/advanced-sql-patterns-production-analytics) |
| [How Canva collects 25 billion events per day](https://effectsize.io/cases/how-canva-collects-25-billion-events-per-day/) | Canva | 2024 | [original](https://canva.dev/blog/engineering/product-analytics-event-collection) |
| [Leveraging Flink to Detect User Sessions and Engage DoorDash Consumers with Real-Time Notifications](https://effectsize.io/cases/leveraging-flink-to-detect-user-sessions-and-engage-doordash/) | DoorDash | 2023 | [original](https://careersatdoordash.com/blog/leveraging-flink-to-detect-user-sessions-and-engage-doordash-consumers-with-real-time-notifications) |
| [Marketing Attribution: Evaluating The Path to Purchase in the Product Ecosystem](https://effectsize.io/cases/marketing-attribution-evaluating-the-path-to-purchase-in-the/) | trivago | 2022 | [original](https://tech.trivago.com/post/2022-12-06-marketing-attribution-evaluating-the-path-to-purchase) |
| [Demystifying user journeys: Revolutionizing troubleshooting with auto tracking](https://effectsize.io/cases/demystifying-user-journeys-revolutionizing-troubleshooting/) | Grab | 2025 | [original](https://engineering.grab.com/auto-track-sdk) |
| [dbt Generic Tests in Sessions Validation at Yelp](https://effectsize.io/cases/dbt-generic-tests-in-sessions-validation-at-yelp/) | Yelp | 2024 | [original](https://engineeringblog.yelp.com/2024/08/dbt-Generic-Tests-in-Sessions-Validation-at-Yelp.html) · [code](https://effectsize.io/cases/dbt-generic-tests-in-sessions-validation-at-yelp/) |
| [Event Tracking System at Wealthfront](https://effectsize.io/cases/event-tracking-system-at-wealthfront/) | Wealthfront | 2022 | [original](https://eng.wealthfront.com/2022/11/07/event-tracking-system-at-wealthfront) |
| [Generative and Contrastive Learning for Event Sequences: Which Is Better and Can They Be Combined?](https://effectsize.io/cases/generative-and-contrastive-learning-for-event-sequences/) | Skoltech | 2024 | [original](https://www.youtube.com/watch?v=btj9YiQjtEU) |

**[All 13 clickstream cases →](topics/clickstream.md)**

### Behavior

Retention, cohorts, activation, aha-moment, engagement, behavioral segmentation and clustering, behavior-based churn analysis.

| Case | Company | Year | Source |
|---|---|---|---|
| [Single AI View of Customer: A retailers guide to Know Your Customer Better using Customer Embeddings and Customer Persona](https://effectsize.io/cases/single-ai-view-of-customer-a-retailers-guide-to-know-your/) | Walmart | 2025 | [original](https://medium.com/walmartglobaltech/single-ai-view-of-customer-a-retailers-guide-to-know-your-customer-better-using-customer-6b588ff336bd) |
| [From Data to Insights: Segmenting Airbnb's Supply](https://effectsize.io/cases/from-data-to-insights-segmenting-airbnb-s-supply/) | Airbnb | 2024 | [original](https://medium.com/airbnb-engineering/from-data-to-insights-segmenting-airbnbs-supply-c88aa2bb9399) |
| [Understanding a diverse user base with frequency segmentation at scale](https://effectsize.io/cases/understanding-a-diverse-user-base-with-frequency/) | Canva | 2023 | [original](https://canva.dev/blog/engineering/understanding-a-diverse-user-base-with-frequency-segmentation-at-scale) |
| [Transformers for Generalizing User Behavior in Yandex.Taxi](https://effectsize.io/cases/transformers-for-generalizing-user-behavior-in-yandex-taxi/) | Yandex Go | 2022 | [original](https://www.youtube.com/watch?v=GdFqJPYyR3Q) |
| [The habit-building research behind your Duolingo streak](https://effectsize.io/cases/the-habit-building-research-behind-your-duolingo-streak/) | Duolingo | 2022 | [original](https://blog.duolingo.com/how-duolingo-streak-builds-habit) |
| [Are You a Dalia? How We Created Data Science Personas for Spotify’s Analytics Platform](https://effectsize.io/cases/are-you-a-dalia-how-we-created-data-science-personas-for/) | Spotify | 2024 | [original](https://engineering.atspotify.com/2024/09/are-you-a-dalia-how-we-created-data-science-personas-for-spotifys-analytics-platform) |
| [Recursive Embedding and Clustering](https://effectsize.io/cases/recursive-embedding-and-clustering/) | Spotify | 2023 | [original](https://engineering.atspotify.com/2023/12/recursive-embedding-and-clustering) · [code](https://effectsize.io/cases/recursive-embedding-and-clustering/) |
| [NLP at Alfa-Bank, Part 9: Structuring OFD Receipts](https://effectsize.io/cases/nlp-at-alfa-bank-part-9-structuring-ofd-receipts/) | Alfa-Bank | 2023 | [original](https://www.youtube.com/watch?v=fWU9EeqUpVo) |

**[All 15 behavior cases →](topics/behavior.md)**

### Predictive models

Churn prediction, propensity, LTV prediction, lead scoring, metric forecasting.

| Case | Company | Year | Source |
|---|---|---|---|
| [Roonomics: How Economics Helped Us to Build a Churn Prediction Model](https://effectsize.io/cases/roonomics-how-economics-helped-us-to-build-a-churn/) | Deliveroo | 2026 | [original](https://deliveroo.engineering/2026/09/22/roonomics-how-economics-helped-us-to-build-a-churn-prediction-model.html) |
| [How we knew COVID was over (and what our models had to unlearn)](https://effectsize.io/cases/how-we-knew-covid-was-over-and-what-our-models-had-to/) | Airbnb | 2026 | [original](https://medium.com/airbnb-engineering/how-we-knew-covid-was-over-and-what-our-models-had-to-unlearn-c606b9bdb0ab) |
| [Predicting Risk in Content Launches: How Data-Driven Insights can Transform Launch Planning](https://effectsize.io/cases/predicting-risk-in-content-launches-how-data-driven-insights/) | Netflix | 2026 | [original](https://netflixtechblog.com/predicting-risk-in-content-launches-how-data-driven-insights-can-transform-launch-planning-587b1f2de928) |
| [Agentic Feature Engineering: How McAfee Drives Personalization With Agent Bricks](https://effectsize.io/cases/agentic-feature-engineering-how-mcafee-drives/) | McAfee | 2026 | [original](https://www.databricks.com/dataaisummit/session/agentic-feature-engineering-how-mcafee-drives-personalization-agent) |
| [ML Ad Forecaster: Estimating Results Before Launch](https://effectsize.io/cases/ml-ad-forecaster-estimating-results-before-launch/) | Avito | 2026 | [original](https://www.youtube.com/watch?v=4UlBOay9nUU) |
| [Attribution of Long-Range Actions in Conversion Models](https://effectsize.io/cases/attribution-of-long-range-actions-in-conversion-models/) | Avito | 2026 | [original](https://www.youtube.com/watch?v=HKB0wnDwIMw) |
| [Applying Graph Neural Networks to Credit Scoring at Alfa-Bank](https://effectsize.io/cases/applying-graph-neural-networks-to-credit-scoring-at-alfa/) | Alfa-Bank | 2026 | [original](https://www.youtube.com/watch?v=ps-WRucCU3o) |
| [What COVID did to our forecasting models (and what we built to handle the next shock)](https://effectsize.io/cases/what-covid-did-to-our-forecasting-models-and-what-we-built/) | Airbnb | 2026 | [original](https://medium.com/airbnb-engineering/what-covid-did-to-our-forecasting-models-and-what-we-built-to-handle-the-next-shock-ccbf0e1f7fa9) |

**[All 147 predictive models cases →](topics/predictive.md)**

### Growth

Onboarding analysis, paywall/pricing experiments, reactivation, virality — when there is an analytical or experimental part.

| Case | Company | Year | Source |
|---|---|---|---|
| [Buyer Journey Insights with Data-Driven Attribution](https://effectsize.io/cases/buyer-journey-insights-with-data-driven-attribution/) | LinkedIn | 2025 | [original](https://linkedin.com/blog/engineering/marketing/buyer-journey-insights-with-data-driven-attribution) |
| [5 product lessons we learned from building Friend Streak](https://effectsize.io/cases/5-product-lessons-we-learned-from-building-friend-streak/) | Duolingo | 2024 | [original](https://blog.duolingo.com/product-lessons-friend-streak) |
| [End-to-end Keyword Bidding for Apple Search Ads](https://effectsize.io/cases/end-to-end-keyword-bidding-for-apple-search-ads/) | Canva | 2023 | [original](https://canva.dev/blog/engineering/end-to-end-asa-keyword-bidding) |
| [Improving the customer’s experience via ML-driven payment routing](https://effectsize.io/cases/improving-the-customer-s-experience-via-ml-driven-payment/) | LinkedIn | 2023 | [original](https://linkedin.com/blog/engineering/product-design/improving-the-customer-s-experience-via-ml-driven-payment-routin) |
| [Treating Pricing Changes Like Code Deploys](https://effectsize.io/cases/treating-pricing-changes-like-code-deploys/) | Thumbtack | 2026 | [original](https://medium.com/thumbtack-engineering/treating-pricing-changes-like-code-deploys-dc8c26ab6c5d) |
| [Marketing Attribution](https://effectsize.io/cases/marketing-attribution/) | Expedia Group | 2023 | [original](https://medium.com/expedia-group-tech/marketing-attribution-f76ac15c804e) |
| [Pricing at Lyft](https://effectsize.io/cases/pricing-at-lyft/) | Lyft | 2022 | [original](https://eng.lyft.com/pricing-at-lyft-8a4022065f8b) |
| [How we built Asana's Marketing Measurement Capabilities to power global customer growth](https://effectsize.io/cases/how-we-built-asana-s-marketing-measurement-capabilities-to/) | Asana | 2022 | [original](https://asana.com/inside-asana/marketing-measurement-capabilities) |

**[All 15 growth cases →](topics/growth.md)**

## Risk

### Fraud

Fraud and abuse detection in a product, transaction and authentication scoring, spam and fake objects/accounts, fraud economics and choosing the anti-fraud target, graph features, golden set for moderation.

| Case | Company | Year | Source |
|---|---|---|---|
| [About Anti-Fraud and Cats: How to Fight Fraud, Not Just Detect It Better](https://effectsize.io/cases/about-anti-fraud-and-cats-how-to-fight-fraud-not-just-detect/) | Yandex | 2026 | [original](https://www.youtube.com/watch?v=eCrZsHNCJ7Q) |
| [Deploying LLMs in Moderation: From PoC to the Target Solution](https://effectsize.io/cases/deploying-llms-in-moderation-from-poc-to-the-target-solution/) | Avito | 2026 | [original](https://www.youtube.com/watch?v=MURmxFBvuxQ) |
| [How Pinterest Built a Real‑Time Radar for Violative Content using AI](https://effectsize.io/cases/how-pinterest-built-a-real-time-radar-for-violative-content/) | Pinterest | 2025 | [original](https://medium.com/pinterest-engineering/how-pinterest-built-a-real-time-radar-for-violative-content-using-ai-d5a108e02ac2) |
| [SafeChat: DoorDash's AI-powered safety feature](https://effectsize.io/cases/safechat-doordash-s-ai-powered-safety-feature/) | DoorDash | 2025 | [original](https://careersatdoordash.com/blog/doordash-safechat-ai-safety-feature) |
| [Building an anomaly detection platform at DoorDash to catch fraud trends early](https://effectsize.io/cases/building-an-anomaly-detection-platform-at-doordash-to-catch/) | DoorDash | 2025 | [original](https://careersatdoordash.com/blog/doordash-anomaly-detection-platform-to-catch-fraud-trends) |
| [High-Speed Multimodal Moderation: LLMs and VLMs in Real Production](https://effectsize.io/cases/high-speed-multimodal-moderation-llms-and-vlms-in-real/) | Wildberries | 2025 | [original](https://www.youtube.com/watch?v=Cd5i01mTQ9c) |
| [Moderation Platformization](https://effectsize.io/cases/moderation-platformization/) | Avito | 2025 | [original](https://www.youtube.com/watch?v=cj-OLmxEwvA) |
| [The Entity Resolution Task: Atomic Factory](https://effectsize.io/cases/the-entity-resolution-task-atomic-factory/) | Yandex | 2025 | [original](https://www.youtube.com/watch?v=KMyqVwhEn2s) |

**[All 71 fraud cases →](topics/fraud.md)**

## Data & practice

### Insights

Metric change analysis (root cause), metric decomposition, anomaly detection, auto-insights, exploratory analysis frameworks.

| Case | Company | Year | Source |
|---|---|---|---|
| [Databricks on Databricks: Automating Service Reliability at Scale](https://effectsize.io/cases/databricks-on-databricks-automating-service-reliability-at/) | Databricks | 2026 | [original](https://www.databricks.com/dataaisummit/session/databricks-databricks-automating-service-reliability-scale) · [code](https://effectsize.io/cases/databricks-on-databricks-automating-service-reliability-at/) |
| [DrP: Meta’s Root Cause Analysis Platform at Scale](https://effectsize.io/cases/drp-meta-s-root-cause-analysis-platform-at-scale/) | Meta | 2025 | [original](https://engineering.fb.com/2025/12/19/data-infrastructure/drp-metas-root-cause-analysis-platform-at-scale) |
| [The Quest to Understand Metric Movements](https://effectsize.io/cases/the-quest-to-understand-metric-movements/) | Pinterest | 2025 | [original](https://medium.com/pinterest-engineering/the-quest-to-understand-metric-movements-8ab12ae97cda) |
| [Using ML to detect and respond to performance degradations in slices of Stripe payments](https://effectsize.io/cases/using-ml-to-detect-and-respond-to-performance-degradations/) | Stripe | 2025 | [original](https://stripe.com/blog/using-ml-to-detect-and-respond-to-performance-degradations-in-slices-of-stripe-payments) |
| [Using AI to Understand the Complexities and Pitfalls of Real Estate Data](https://effectsize.io/cases/using-ai-to-understand-the-complexities-and-pitfalls-of-real/) | Zillow | 2024 | [original](https://zillow.com/tech/using-ai-to-understand-the-complexities-and-pitfalls-of-real-estate-data) |
| [NLP at Alfa-Bank, Part 7: Analyzing Customer Feedback](https://effectsize.io/cases/nlp-at-alfa-bank-part-7-analyzing-customer-feedback/) | Alfa-Bank | 2023 | [original](https://www.youtube.com/watch?v=qWl3DHW3Y68) |
| [Warden: Real Time Anomaly Detection at Pinterest](https://effectsize.io/cases/warden-real-time-anomaly-detection-at-pinterest/) | Pinterest | 2023 | [original](https://medium.com/pinterest-engineering/warden-real-time-anomaly-detection-at-pinterest-210c122f6afa) · [code](https://effectsize.io/cases/warden-real-time-anomaly-detection-at-pinterest/) |
| [Building a large scale unsupervised model anomaly detection system — Part 2](https://effectsize.io/cases/building-a-large-scale-unsupervised-model-anomaly-detection/) | Lyft | 2023 | [original](https://eng.lyft.com/building-a-large-scale-unsupervised-model-anomaly-detection-system-part-2-3690f4c37c5b) |

**[All 45 insights cases →](topics/insights.md)**

### Analytics practice

Data-informed processes, experimentation culture, how an analyst works with the product, hypothesis prioritization.

| Case | Company | Year | Source |
|---|---|---|---|
| [Analytics, Data, Metrics and Motivation: How to Build a Data Labeling Process in a Large Bank](https://effectsize.io/cases/analytics-data-metrics-and-motivation-how-to-build-a-data/) | Alfa-Bank | 2025 | [original](https://www.youtube.com/watch?v=P18akQ6oyUY) |
| [Data Strategy in a Large Group of Companies](https://effectsize.io/cases/data-strategy-in-a-large-group-of-companies/) | MTS | 2024 | [original](https://www.youtube.com/watch?v=8b1PbxcAyQo) |
| [Increment vs Experiment: How to Reduce Uncertainty When Developing ML Models](https://effectsize.io/cases/increment-vs-experiment-how-to-reduce-uncertainty-when/) | Wildberries | 2025 | [original](https://www.youtube.com/watch?v=qKiulcmSeGM) |
| [Deliveroo experimentation principles](https://effectsize.io/cases/deliveroo-experimentation-principles/) | Deliveroo | 2025 | [original](https://deliveroo.engineering/2025/02/06/experimentation-principles.html) |
| [Three Pillars of Successful Data Science Implementation](https://effectsize.io/cases/three-pillars-of-successful-data-science-implementation/) | Alfa-Bank | 2024 | [original](https://www.youtube.com/watch?v=mUVZyXuqJT8) |
| [Building a strong foundation to accelerate StreetEasy’s data science efforts](https://effectsize.io/cases/building-a-strong-foundation-to-accelerate-streeteasy-s-data/) | Zillow | 2024 | [original](https://zillow.com/tech/building-a-strong-foundation-to-accelerate-streeteasys-data-science-efforts) |
| [Peer Reviews for Data Science](https://effectsize.io/cases/peer-reviews-for-data-science/) | Square | 2024 | [original](https://developer.squareup.com/blog/peer-reviews-for-data-science) |
| [Why You Need an Experimentation Template](https://effectsize.io/cases/why-you-need-an-experimentation-template/) | Block | 2023 | [original](https://developer.squareup.com/blog/why-you-need-an-experimentation-template) |

**[All 25 analytics practice cases →](topics/analytics-practice.md)**

### Data infrastructure

Event pipelines, event stores, feature store — only if directly tied to the topics above.

| Case | Company | Year | Source |
|---|---|---|---|
| [From Data Silos to Feature Serving: How We Unified Fragmented Data for Training, Inference, and Reuse](https://effectsize.io/cases/from-data-silos-to-feature-serving-how-we-unified-fragmented/) | HubSpot | 2026 | [original](https://product.hubspot.com/blog/from-data-silos-to-feature-serving-how-we-unified-fragmented-data-for-training-inference-and-reuse) |
| [Refreshing the Travel-Time Map Behind Lyft’s Marketplace: Rebuilding Neighborhood Reachability Signals](https://effectsize.io/cases/refreshing-the-travel-time-map-behind-lyft-s-marketplace/) | Lyft | 2026 | [original](https://eng.lyft.com/refreshing-the-travel-time-map-behind-lyfts-marketplace-rebuilding-neighborhood-reachability-5be3efbc82ea) |
| [Ultra Low Latency Streaming for Real-Time Feature Engineering](https://effectsize.io/cases/ultra-low-latency-streaming-for-real-time-feature/) | Databricks | 2026 | [original](https://www.databricks.com/dataaisummit/session/ultra-low-latency-streaming-real-time-feature-engineering) |
| [A Speech Platform in Production](https://effectsize.io/cases/a-speech-platform-in-production/) | X5 Tech | 2026 | [original](https://www.youtube.com/watch?v=zCD017S2vm4) |
| [An Authorization Model in a Lakehouse Without Downtime](https://effectsize.io/cases/an-authorization-model-in-a-lakehouse-without-downtime/) | X5 Tech | 2026 | [original](https://www.youtube.com/watch?v=3OgAIikAsNk) |
| [Real-Time Analytics on ClickHouse](https://effectsize.io/cases/real-time-analytics-on-clickhouse/) | X5 Tech | 2026 | [original](https://www.youtube.com/watch?v=ms4vgIf13EY) |
| [Balancing Speed and Accuracy in Digital Order Fulfillment: The Next-Gen Solution](https://effectsize.io/cases/balancing-speed-and-accuracy-in-digital-order-fulfillment/) | Target | 2026 | [original](https://tech.target.com/blog/balancing-speed-and-accuracy-digital-fulfillment) |
| [How We Teach Alice to Activate on Intonation](https://effectsize.io/cases/how-we-teach-alice-to-activate-on-intonation/) | Yandex | 2025 | [original](https://www.youtube.com/watch?v=CkqLGFubu5Q) |

**[All 60 data infrastructure cases →](topics/data-infra.md)**

## Top companies

[DoorDash](companies/doordash.md) (61) · [Pinterest](companies/pinterest.md) (47) · [Yandex](companies/yandex.md) (45) · [Avito](companies/avito.md) (37) · [LinkedIn](companies/linkedin.md) (36) · [Instacart](companies/instacart.md) (31) · [Netflix](companies/netflix.md) (30) · [Spotify](companies/spotify.md) (28) · [Airbnb](companies/airbnb.md) (27) · [Meta](companies/meta.md) (24) · [Alfa-Bank](companies/alfa-bank.md) (23) · [Grab](companies/grab.md) (22) · [Walmart](companies/walmart.md) (22) · [Lyft](companies/lyft.md) (21) · [Databricks](companies/databricks.md) (20) · [Expedia Group](companies/expedia-group.md) (19) · [Algolia](companies/algolia.md) (18) · [Etsy](companies/etsy.md) (18) · [Sber](companies/sber.md) (15) · [Mercari](companies/mercari.md) (15) · [Zillow](companies/zillow.md) (15) · [VTB](companies/vtb.md) (14) · [LY Corporation](companies/ly-corporation.md) (12) · [Ramp](companies/ramp.md) (12) · [Target](companies/target.md) (11) · [eBay](companies/ebay.md) (11) · [Thumbtack](companies/thumbtack.md) (10) · [Yelp](companies/yelp.md) (10) · [X5 Tech](companies/x5-tech.md) (10) · [Yandex Lavka](companies/yandex-lavka.md) (10) · [Celsus](https://effectsize.io/?company=celsus) (10) · [Canva](https://effectsize.io/?company=canva) (10) · [Uber](https://effectsize.io/?company=uber) (10) · [Criteo](https://effectsize.io/?company=criteo) (9) · [Stripe](https://effectsize.io/?company=stripe) (9) · [Wildberries](https://effectsize.io/?company=wildberries) (9) · [OLX](https://effectsize.io/?company=olx) (8) · [Whatnot](https://effectsize.io/?company=whatnot) (8) · [VK](https://effectsize.io/?company=vk) (8) · [CFT](https://effectsize.io/?company=cft) (8)

## FAQ

**How do I find A/B testing case studies?** Open [A/B testing](topics/ab-testing.md) or [Advanced experimentation](topics/experimentation-advanced.md): CUPED and variance reduction, sequential testing, switchback and interleaving experiments, each linked to the original post.

**Where are machine learning case studies by company?** See [By company](companies/README.md), e.g. [DoorDash](companies/doordash.md), [Pinterest](companies/pinterest.md), [Yandex](companies/yandex.md), [Avito](companies/avito.md).

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
