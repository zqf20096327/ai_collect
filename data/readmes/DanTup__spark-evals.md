# DGX Spark Evals

Some basic evals run on various models that fit on a single DGX Spark.

## Leaderboard

I ran these in a new VM created with `multipass launch --cpus 12 --disk 50G --memory 32G --name spark-evals` using [run_benchmarks.sh](./run_benchmarks.sh).


| name                                              | evo eval (codex) | evo eval (terminus-2) | aider polyglot (codex) | aider polyglot (terminus-2) | swe-rebench (codex) | swe-rebench (terminus-2) |
| -                                                 |  -: |  -: |  -: |  -: |  -: |  -: |
| [Qwen 3.8 27B](configs/qwen38-27b.md)             | 80% | 80% | 50% | 25% | 80% | 60% |
| [Qwen 3.8 27B FP8](configs/qwen38-27b-fp8.md)     | 70% | 70% | 29% | 13% | 70% | 60% |
| [Muse Glimmer 30B](configs/muse-glimmer-30b.md)   | 80% | 70% | 33% | 25% | 70% | 40% |
| [Gemma4 31B](configs/gemma4-31b.md)               | 80% | 80% | 17% | 25% | 20% |  0% |



## Legacy Leaderboard

Below are scores from the original evals run via Inspect AI, before switching to Harbor.

| name | bfcl | bigcodebench | IfEvalCode | Overall |
| --- | ---: | ---: | ---: | ---: |
| Gemma4 31B<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>2h 30m, 504k in, 613k out</nobr> | <nobr>76.0%</nobr> | ***<nobr>72.0%</nobr>*** | ***<nobr>20.0%</nobr>***<br>ts: <nobr>38.0%</nobr> / <nobr>38.0%</nobr> | ***<nobr>48.8%</nobr>*** |
| Qwen3.6 35B-A3B FP8<br>kv-cache-dtype=fp8<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>10h 40m, 569k in, 5,229k out</nobr> | <nobr>76.0%</nobr> | <nobr>60.0%</nobr> | ***<nobr>20.0%</nobr>***<br>ts: <nobr>38.0%</nobr> / ***<nobr>50.0%</nobr>*** | ***<nobr>48.8%</nobr>*** |
| Gemma4 31B<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>9h 44m, 495k in, 550k out</nobr> | <nobr>78.0%</nobr> | ***<nobr>72.0%</nobr>*** | <nobr>18.0%</nobr><br>ts: <nobr>36.0%</nobr> / <nobr>38.0%</nobr> | <nobr>48.4%</nobr> |
| Qwen3.6 35B-A3B FP8<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>9h 42m, 569k in, 5,247k out</nobr> | <nobr>78.0%</nobr> | <nobr>64.0%</nobr> | <nobr>18.0%</nobr><br>ts: <nobr>38.0%</nobr> / <nobr>44.0%</nobr> | <nobr>48.4%</nobr> |
| Qwen3.6 35B-A3B NVFP4<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>8h 47m, 571k in, 5,334k out</nobr> | ***<nobr>80.0%</nobr>*** | <nobr>64.0%</nobr> | <nobr>12.0%</nobr><br>ts: <nobr>36.0%</nobr> / <nobr>44.0%</nobr> | <nobr>47.2%</nobr> |
| Qwen3.6 27B FP8<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>19h 58m, 507k in, 3,112k out</nobr> | <nobr>78.0%</nobr> | <nobr>66.0%</nobr> | <nobr>18.0%</nobr><br>ts: ***<nobr>42.0%</nobr>*** / <nobr>30.0%</nobr> | <nobr>46.8%</nobr> |
| Gemma4 26B-A4B<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>1h 50m, 504k in, 822k out</nobr> | <nobr>76.0%</nobr> | <nobr>62.0%</nobr> | <nobr>16.0%</nobr><br>ts: <nobr>34.0%</nobr> / <nobr>42.0%</nobr> | <nobr>46.0%</nobr> |
| Gemma4 31B<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>1h 12m, 504k in, 618k out</nobr> | <nobr>76.0%</nobr> | ***<nobr>72.0%</nobr>*** | <nobr>16.0%</nobr><br>ts: <nobr>34.0%</nobr> / <nobr>32.0%</nobr> | <nobr>46.0%</nobr> |
| Ornith 35B<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>20h 47m, 514k in, 2,588k out</nobr> | ***<nobr>80.0%</nobr>*** | <nobr>62.0%</nobr> | ***<nobr>20.0%</nobr>***<br>ts: <nobr>34.0%</nobr> / <nobr>30.0%</nobr> | <nobr>45.2%</nobr> |
| Qwen3.6 27B<br>enable_thinking=False<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>4h 14m, 569k in, 702k out</nobr> | <nobr>78.0%</nobr> | <nobr>64.0%</nobr> | <nobr>16.0%</nobr><br>ts: <nobr>32.0%</nobr> / <nobr>36.0%</nobr> | <nobr>45.2%</nobr> |
| Qwen3.6 27B<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>25h 11m, 478k in, 2,706k out</nobr> | <nobr>78.0%</nobr> | <nobr>68.0%</nobr> | <nobr>16.0%</nobr><br>ts: <nobr>32.0%</nobr> / <nobr>26.0%</nobr> | <nobr>44.0%</nobr> |
| Qwen3.6 35B-A3B<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>19h 51m, 508k in, 4,037k out</nobr> | <nobr>76.0%</nobr> | <nobr>62.0%</nobr> | <nobr>10.0%</nobr><br>ts: <nobr>28.0%</nobr> / <nobr>38.0%</nobr> | <nobr>42.8%</nobr> |
| KAT Coder v2.5 Dev<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>7h 37m, 559k in, 1,168k out</nobr> | <nobr>72.0%</nobr> | <nobr>66.0%</nobr> | <nobr>12.0%</nobr><br>ts: <nobr>26.0%</nobr> / <nobr>34.0%</nobr> | <nobr>42.0%</nobr> |
| Qwen3 Coder Next FP8<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>2h 14m, 567k in, 681k out</nobr> | <nobr>78.0%</nobr> | <nobr>62.0%</nobr> | <nobr>12.0%</nobr><br>ts: <nobr>24.0%</nobr> / <nobr>34.0%</nobr> | <nobr>42.0%</nobr> |
| Gemma4 Diffusion<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>1h 47m, 500k in, 664k out</nobr> | <nobr>76.0%</nobr> | <nobr>56.0%</nobr> | <nobr>12.0%</nobr><br>ts: <nobr>24.0%</nobr> / <nobr>34.0%</nobr> | <nobr>40.4%</nobr> |
| Intern S2 Mobius<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>3h 4m, 571k in, 1,458k out</nobr> | <nobr>76.0%</nobr> | <nobr>62.0%</nobr> | <nobr>8.0%</nobr><br>ts: <nobr>18.0%</nobr> / <nobr>32.0%</nobr> | <nobr>39.2%</nobr> |
| Nemotron 3.5 Lightning NVFP4<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>11h 36m, 561k in, 4,770k out</nobr> | <nobr>66.0%</nobr> | <nobr>62.0%</nobr> | <nobr>10.0%</nobr><br>ts: <nobr>36.0%</nobr> / <nobr>22.0%</nobr> | <nobr>39.2%</nobr> |
| Intern S2 Preview<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>12h 17m, 547k in, 2,815k out</nobr> | <nobr>72.0%</nobr> | <nobr>64.0%</nobr> | <nobr>8.0%</nobr><br>ts: <nobr>20.0%</nobr> / <nobr>28.0%</nobr> | <nobr>38.4%</nobr> |
| Qwen3.6 27B<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>34h 19m, 422k in, 1,986k out</nobr> | <nobr>78.0%</nobr> | <nobr>62.0%</nobr> | <nobr>12.0%</nobr><br>ts: <nobr>22.0%</nobr> / <nobr>14.0%</nobr> | <nobr>37.6%</nobr> |
| North Mini Code<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>31h 31m, 441k in, 1,742k out</nobr> | <nobr>68.0%</nobr> | <nobr>54.0%</nobr> | <nobr>8.0%</nobr><br>ts: <nobr>26.0%</nobr> / <nobr>14.0%</nobr> | <nobr>34.0%</nobr> |
| Laguna S.2<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>11h 17m, 520k in, 1,856k out</nobr> | <nobr>30.0%</nobr> | <nobr>62.0%</nobr> | <nobr>14.0%</nobr><br>ts: <nobr>26.0%</nobr> / <nobr>32.0%</nobr> | <nobr>32.8%</nobr> |
| Nemotron3 Nano Omni 30B-A3B BF16<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>15h 35m, 537k in, 1,719k out</nobr> | <nobr>76.0%</nobr> | <nobr>54.0%</nobr> | <nobr>4.0%</nobr><br>ts: <nobr>10.0%</nobr> / <nobr>18.0%</nobr> | <nobr>32.4%</nobr> |
| Qwen AgentWorld 35B A3B<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>48h 27m, 287k in, 1,869k out</nobr> | <nobr>74.0%</nobr> | <nobr>58.0%</nobr> | <nobr>4.0%</nobr><br>ts: <nobr>10.0%</nobr> / <nobr>6.0%</nobr> | <nobr>30.4%</nobr> |
| Laguna XS.2<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>6h 35m, 573k in, 1,783k out</nobr> | <nobr>16.0%</nobr> | <nobr>54.0%</nobr> | <nobr>14.0%</nobr><br>ts: <nobr>22.0%</nobr> / <nobr>24.0%</nobr> | <nobr>26.0%</nobr> |
| Nemotron3 Super 120B-A12B NVFP4<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>14h 37m, 535k in, 1,595k out</nobr> | <nobr>12.0%</nobr> | <nobr>60.0%</nobr> | <nobr>8.0%</nobr><br>ts: <nobr>32.0%</nobr> / <nobr>18.0%</nobr> | <nobr>26.0%</nobr> |
| Ornith 35B FP8<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>48h 24m, 329k in, 1,124k out</nobr> | ***<nobr>80.0%</nobr>*** | <nobr>0.0%</nobr> | <nobr>8.0%</nobr><br>ts: <nobr>18.0%</nobr> / <nobr>12.0%</nobr> | <nobr>23.6%</nobr> |
| Muse Glimmer<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>11h 39m, 441k in, 1,335k out</nobr> | <nobr>12.0%</nobr> |  | <nobr>14.0%</nobr><br>ts: <nobr>38.0%</nobr> / <nobr>26.0%</nobr> | <nobr>22.5%</nobr> |
| Deepseek v4 Flash<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>31h 48m, 222k in, 103k out</nobr> | <nobr>70.0%</nobr> |  | <nobr>0.0%</nobr><br>ts: <nobr>0.0%</nobr> / <nobr>0.0%</nobr> | <nobr>17.5%</nobr> |
| Orion GRM 2.6 Plus<br>&nbsp;&nbsp;&nbsp;&nbsp;<nobr>88h 58m</nobr> | <nobr>20.0%</nobr> | <nobr>0.0%</nobr> | <nobr>0.0%</nobr><br>ts: <nobr>0.0%</nobr> / <nobr>0.0%</nobr> | <nobr>4.0%</nobr> |
