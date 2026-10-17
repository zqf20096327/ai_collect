# Federated Learning Resources

[![Stars](https://img.shields.io/github/stars/youngfish42/Awesome-FL.svg?color=orange)](https://github.com/youngfish42/Awesome-FL/stargazers) [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re) [![License](https://img.shields.io/github/license/youngfish42/Awesome-FL.svg?color=green)](https://github.com/youngfish42/image-registration-resources/blob/master/LICENSE) ![](https://img.shields.io/github/last-commit/youngfish42/Awesome-FL) 

---

**Table of Contents**

- [Papers](#papers)
  - [FL in top-tier journal](#fl-in-top-tier-journal)
  - FL in top-tier conference and journal by category
    - [AI](#fl-in-top-ai-conference-and-journal) [ML](#fl-in-top-ml-conference-and-journal) [DM](#fl-in-top-dm-conference-and-journal) [Secure](#fl-in-top-secure-conference-and-journal) [CV](#fl-in-top-cv-conference-and-journal) [NLP](#fl-in-top-nlp-conference-and-journal) [IR](#fl-in-top-ir-conference-and-journal) [DB](#fl-in-top-db-conference-and-journal) [Network](#fl-in-top-network-conference-and-journal) [System](#fl-in-top-system-conference-and-journal) [Others](#fl-in-top-conference-and-journal-other-fields)
  - [FL on Graph Data and Graph Neural Networks](#fl-on-graph-data-and-graph-neural-networks) [[dblp]](https://dblp.uni-trier.de/search?q=Federated%20graph%7Csubgraph%7Cgnn) 
  - [FL on Tabular Data](#fl-on-tabular-data) [[dblp]](https://dblp.org/search?q=federate%20tree%7Cboost%7Cbagging%7Cgbdt%7Ctabular%7Cforest%7CXGBoost)
- [Framework](#framework)
- [Datasets](#datasets)
- [Surveys](#surveys)
- [Tutorials and Courses](#tutorials-and-courses)
- Key Conferences/Workshops/Journals
  - [Workshops](#workshops) [Special Issues](#journal-special-issues) [Special Tracks](#conference-special-tracks)
- [Update log](#update-log)
- [Acknowledgments](#acknowledgments)
- [Citation](#citation)



We use another project to automatically track updates to FL papers, click on [FL-paper-update-tracker](https://github.com/youngfish42/FL-paper-update-tracker) if you need it.

Please note that if this page does not display the full content, **please visit [the official homepage](https://youngfish42.github.io/Awesome-FL) for full information.**

**More items will be added to the repository**. Please feel free to suggest other key resources by opening an [issue](https://github.com/youngfish42/Awesome-FL/issues) report, submitting a pull request, or dropping me an email @ ([im.young@foxmail.com](mailto:im.young@foxmail.com)). If you want to communicate with more friends in the field of federated learning, please join the QQ group [联邦学习交流群], the group number is 833638275. Enjoy reading!



**Repository Update Notice** 

> 2024/09/30
>
> 
>
> Dear Users, We would like to inform you of a few changes that will affect this open source repository. The owner and principal contributor [@youngfish42](https://github.com/youngfish42) has successfully completed his doctoral studies 🎓 as of September 30, 2024, and has since shifted his research focus. This change in circumstances will impact the frequency and extent of updates to the repository's paper list. 
>
> Instead of the previous regular updates, we anticipate that the paper list will now be updated on a monthly or quarterly basis. Furthermore, the depth of these updates will be reduced. For instance, updates related to the author's institution and open source code will no longer be actively maintained. 
>
> We understand that this might affect the value you derive from this repository. Therefore, we humbly invite more contributors to participate in updating the content. This collaborative effort will ensure that the repository remains a valuable resource for everyone. 
>
> We appreciate your understanding and look forward to your continued support and contributions. 
>
> 
>
> Best Regards, 
>
> 白小鱼 (youngfish)
>




# papers

**categories**

- Artificial Intelligence (IJCAI, AAAI, AISTATS, ALT, AI)

- Machine Learning (NeurIPS, ICML, ICLR, COLT, UAI, Machine Learning, JMLR, TPAMI)

- Data Mining (KDD, WSDM)

- Secure (S&P, CCS, USENIX Security, NDSS)

- Computer Vision (ICCV, CVPR, ECCV, MM, IJCV)

- Natural Language Processing (ACL, EMNLP, NAACL, COLING)

- Information Retrieval (SIGIR)

- Database (SIGMOD, ICDE, VLDB)

- Network (SIGCOMM, INFOCOM, MOBICOM, NSDI, WWW)

- System (OSDI, SOSP, ISCA, MLSys, EuroSys, TPDS, DAC, TOCS, TOS, TCAD, TC) 

- Others (ICSE, FOCS, STOC)




<details open>
<summary> Events </summary>

| Venue                                                        | 2024-2020                                                    | before 2020                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [IJCAI](https://dblp.uni-trier.de/search?q=federate%20venue%3AIJCAI%3A) | [25](https://www.ijcai.org/proceedings/2025/), [24](https://www.ijcai.org/proceedings/2024/), [23](https://www.ijcai.org/proceedings/2023/), [22](https://www.ijcai.org/proceedings/2022/), [21](https://www.ijcai.org/proceedings/2021/), [20](https://www.ijcai.org/proceedings/2020/) | [19](https://www.ijcai.org/proceedings/2019/)                |
| [AAAI](https://dblp.uni-trier.de/search?q=federate%20venue%3AAAAI%3A) | [26](https://dblp.org/db/conf/aaai/aaai2026.html), [25](https://dblp.org/db/conf/aaai/aaai2025.html), [24](https://dblp.org/db/conf/aaai/aaai2024.html), [23](https://dblp.org/db/conf/aaai/aaai2023), [22](https://aaai.org/Conferences/AAAI-22/wp-content/uploads/2021/12/AAAI-22_Accepted_Paper_List_Main_Technical_Track.pdf), [21](https://aaai.org/Conferences/AAAI-21/wp-content/uploads/2020/12/AAAI-21_Accepted-Paper-List.Main_.Technical.Track_.pdf), [20](https://aaai.org/Conferences/AAAI-20/wp-content/uploads/2020/01/AAAI-20-Accepted-Paper-List.pdf) | -                                                            |
| [AISTATS](https://dblp.uni-trier.de/search?q=federate%20venue%3AAISTATS%3A) | [25](https://proceedings.mlr.press/v258/), [24](http://proceedings.mlr.press/v238/), [23](http://proceedings.mlr.press/v206/), [22](http://proceedings.mlr.press/v151/), [21](http://proceedings.mlr.press/v130/), [20](http://proceedings.mlr.press/v108/) | -                                                            |
| [ALT](https://dblp.uni-trier.de/search?q=federate%20streamid%3Aconf%2Falt%3A) | 22                                                           | -                                                            |
| [AI](https://dblp.uni-trier.de/search?q=federate%20streamid%3Ajournals%2Fai%3A) (J) | 26, 25, 23                                                   | -                                                            |
| [NeurIPS](https://dblp.uni-trier.de/search?q=federate%20venue%3ANeurIPS%3A) | [24](https://openreview.net/group?id=NeurIPS.cc/2024/Conference#tab-accept-oral), [23](https://openreview.net/group?id=NeurIPS.cc/2023/Conference#tab-accept-oral), [22](https://papers.nips.cc/paper_files/paper/2022), [21](https://papers.nips.cc/paper/2021), [20](https://papers.nips.cc/paper/2020) | [18](https://papers.nips.cc/paper/2018), [17](https://papers.nips.cc/paper/17) |
| [ICML](https://dblp.uni-trier.de/search?q=federate%20venue%3AICML%3A) | [25](https://icml.cc/Conferences/2025/Schedule?type=Poster), [24](https://icml.cc/Conferences/2024/Schedule?type=Poster), [23](https://icml.cc/Conferences/2023/Schedule?type=Poster), [22](https://icml.cc/Conferences/2022/Schedule?type=Poster), [21](https://icml.cc/Conferences/2021/Schedule?type=Poster), [20](https://icml.cc/Conferences/2020/Schedule?type=Poster) | [19](https://icml.cc/Conferences/2019/Schedule?type=Poster)  |
| [ICLR](https://dblp.uni-trier.de/search?q=federate%20venue%3AICLR%3A) | [25](https://openreview.net/group?id=ICLR.cc/2025), [24](https://openreview.net/group?id=ICLR.cc/2024/Conference), [23](https://openreview.net/group?id=ICLR.cc/2023/Conference), [22](https://openreview.net/group?id=ICLR.cc/2022/Conference), [21](https://openreview.net/group?id=ICLR.cc/2021/Conference), [20](https://openreview.net/group?id=ICLR.cc/2020/Conference) | -                                                            |
| [COLT](https://dblp.org/search?q=federated%20venue%3ACOLT%3A) | [23](https://proceedings.mlr.press/v195/)                    | -                                                            |
| [UAI](https://dblp.org/search?q=federated%20venue%3AUAI%3A)  | [25](https://www.auai.org/uai2025/accepted_papers), [24](https://www.auai.org/uai2024/accepted_papers), [23](https://www.auai.org/uai2023/accepted_papers), [22](https://www.auai.org/uai2022/accepted_papers), [21](https://www.auai.org/uai2021/accepted_papers) | -                                                            |
| [Machine Learning](https://dblp.uni-trier.de/search?q=federate%20streamid%3Ajournals%2Fml%3A) (J) | 26, 25, 24, 23, 22                                           | -                                                            |
| [JMLR](https://dblp.uni-trier.de/search?q=federated%20streamid%3Ajournals%2Fjmlr%3A) (J) | 25, 24, 23, 22                                               | -                                                            |
| [TPAMI](https://dblp.uni-trier.de/search?q=federated%20streamid%3Ajournals%2Fpami%3A) (J) | 26, 25, 24, 23, 22                                           | -                                                            |
| [KDD](https://dblp.uni-trier.de/search?q=federate%20venue%3AKDD%3A) | [26](https://dl.acm.org/doi/proceedings/10.1145/3770854), [25](https://dl.acm.org/doi/proceedings/10.1145/3690624), [24](https://dl.acm.org/doi/proceedings/10.1145/3637528), [23](https://dl.acm.org/doi/proceedings/10.1145/3580305), [22](https://kdd.org/kdd2022/paperRT.html), [21](https://kdd.org/kdd2021/accepted-papers/index), [20](https://www.kdd.org/kdd2020/accepted-papers) |                                                              |
| [WSDM](https://dblp.uni-trier.de/search?q=federate%20venue%3AWSDM%3A) | [26](https://dl.acm.org/doi/proceedings/10.1145/3773966),[25](https://www.wsdm-conference.org/2025/accepted-papers/), [24](https://www.wsdm-conference.org/2024/accepted-papers/), [23](https://www.wsdm-conference.org/2023/program/accepted-papers), [22](https://www.wsdm-conference.org/2022/accepted-papers/), [21](https://www.wsdm-conference.org/2021/accepted-papers.php) | [19](https://www.wsdm-conference.org/2019/accepted-papers.php) |
| [S&P](https://dblp.uni-trier.de/search?q=federated%20streamid%3Aconf%2Fsp%3A) | [25](https://sp2025.ieee-security.org/program-papers.html), [24](https://sp2024.ieee-security.org/program-papers.html), [23](https://sp2023.ieee-security.org/program-papers.html), [22](https://www.ieee-security.org/TC/SP2022/program-papers.html) | [19](https://www.ieee-security.org/TC/SP2019/program-papers.html) |
| [CCS](https://dblp.uni-trier.de/search?q=federate%20venue%3ACCS%3A) | [25](https://dl.acm.org/doi/proceedings/10.1145/3719027), [24](https://dl.acm.org/doi/proceedings/10.1145/3658644), [23](https://dl.acm.org/doi/proceedings/10.1145/3576915), [22](https://www.sigsac.org/ccs/CCS2022/program/accepted-papers.html), [21](https://sigsac.org/ccs/CCS2021/accepted-papers.html), [19](https://www.sigsac.org/ccs/CCS2019/index.php/program/accepted-papers/) | [17](https://acmccs.github.io/papers/)                       |
| [USENIX Security](https://dblp.uni-trier.de/search?q=federated%20streamid%3Aconf%2Fuss%3A) | [25](https://www.usenix.org/conference/usenixsecurity25/technical-sessions), [24](https://www.usenix.org/conference/usenixsecurity24/technical-sessions), [23](https://www.usenix.org/conference/usenixsecurity23/technical-sessions), [22](https://www.usenix.org/conference/usenixsecurity22/technical-sessions), [20](https://www.usenix.org/conference/usenixsecurity20/technical-sessions) | -                                                            |
| [NDSS](https://dblp.uni-trier.de/search?q=federate%20venue%3ANDSS%3A) | [26](https://www.ndss-symposium.org/ndss2026/accepted-papers/), [25](https://www.ndss-symposium.org/ndss2025/accepted-papers/), [24](https://www.ndss-symposium.org/ndss2024/accepted-papers/), [23](https://www.ndss-symposium.org/ndss2023/accepted-papers/), [22](https://www.ndss-symposium.org/ndss2022/accepted-papers/), [21](https://www.ndss-symposium.org/ndss2021/accepted-papers/) | -                                                            |
| [CVPR](https://dblp.uni-trier.de/search?q=federate%20venue%3ACVPR%3A) | [25](https://openaccess.thecvf.com/CVPR2025?day=all), [24](https://openaccess.thecvf.com/CVPR2024?day=all), [23](https://openaccess.thecvf.com/CVPR2023?day=all), [22](https://openaccess.thecvf.com/CVPR2022), [21](https://openaccess.thecvf.com/CVPR2021?day=all) | -                                                            |
| [ICCV](https://dblp.uni-trier.de/search?q=federate%20venue%3AICCV%3A) | [23](https://openaccess.thecvf.com/ICCV2023?day=all),[21](https://openaccess.thecvf.com/ICCV2021?day=all) | -                                                            |
| [ECCV](https://dblp.uni-trier.de/search?q=federate%20venue%3AECCV%3A) | [24](https://www.ecva.net/papers.php), [22](https://www.ecva.net/papers.php), [20](https://www.ecva.net/papers.php) | -                                                            |
| [MM](https://dblp.uni-trier.de/search?q=federated%20streamid%3Aconf%2Fmm%3A) | [25](https://dl.acm.org/doi/proceedings/10.1145/3746027), [24](https://dl.acm.org/doi/proceedings/10.1145/3664647), [23](https://dl.acm.org/doi/proceedings/10.1145/3581783), [22](https://dblp.uni-trier.de/db/conf/mm/mm2022.html), [21](https://2021.acmmm.org/main-track-list), [20](https://2020.acmmm.org/main-track-list.html) | -                                                            |
| [IJCV](https://dblp.uni-trier.de/search?q=federate%20streamid%3Ajournals%2Fijcv%3A) (J) | 25, 24                                                       | -                                                            |
| [ACL](https://dblp.uni-trier.de/search?q=federate%20venue%3AACL%3A) | [25](https://aclanthology.org/events/acl-2025/), [24](https://aclanthology.org/events/acl-2024/), [23](https://aclanthology.org/events/acl-2023/), [22](https://aclanthology.org/events/acl-2022/), [21](https://aclanthology.org/events/acl-2021/) | [19](https://aclanthology.org/events/acl-2019/)              |
| [NAACL](https://dblp.uni-trier.de/search?q=federate%20venue%3ANAACL-HLT%3A) | [24](https://aclanthology.org/events/naacl-2024/), [22](https://aclanthology.org/events/naacl-2022/), [21](https://aclanthology.org/events/naacl-2021/) | -                                                            |
| [EMNLP](https://dblp.uni-trier.de/search?q=federate%20venue%3AEMNLP%3A) | [25](https://aclanthology.org/events/emnlp-2025/), [24](https://aclanthology.org/events/emnlp-2024/), [23](https://aclanthology.org/events/emnlp-2023/), [22](https://aclanthology.org/events/emnlp-2022/), [21](https://aclanthology.org/events/emnlp-2021/), [20](https://aclanthology.org/events/emnlp-2020/) | -                                                            |
| [COLING](https://dblp.uni-trier.de/search?q=federate%20venue%3ACOLING%3A) | [25](https://aclanthology.org/volumes/2025.coling-main/), [20](https://aclanthology.org/events/coling-2020/) | -                                                            |
| [SIGIR](https://dblp.uni-trier.de/search?q=federate%20venue%3ASIGIR%3A) | [25](https://dl.acm.org/doi/proceedings/10.1145/3726302), [24](https://dl.acm.org/doi/proceedings/10.1145/3626772), [23](https://dl.acm.org/doi/proceedings/10.1145/3539618), [22](https://dl.acm.org/doi/proceedings/10.1145/3477495), [21](https://dl.acm.org/doi/proceedings/10.1145/3404835), [20](https://dl.acm.org/doi/proceedings/10.1145/3397271) | -                                                            |
| [SIGMOD](https://dblp.uni-trier.de/search?q=federated%20streamid%3Aconf%2Fsigmod%3A) | [25](https://2025.sigmod.org/sigmod_papers.shtml), [24](https://2024.sigmod.org/), [23](https://2023.sigmod.org/sigmod_research_list.shtml), [22](https://2022.sigmod.org/sigmod_research_list.shtml), [21](https://2021.sigmod.org/sigmod_research_list.shtml) | -                                                            |
| [ICDE](https://dblp.uni-trier.de/search?q=federate%20venue%3AICDE%3A) | [25](https://ieee-icde.org/2025/research-papers/), [24](https://icde2024.github.io/), [23](https://icde2023.ics.uci.edu/papers-research-track/), [22](https://icde2022.ieeecomputer.my/accepted-research-track/), [21](https://ieeexplore.ieee.org/xpl/conhome/9458599/proceeding) | -                                                            |
| [VLDB](https://dblp.org/search?q=federated%20streamid%3Ajournals%2Fpvldb%3A) | [25](https://vldb.org/pvldb/volumes/18), [24](https://vldb.org/pvldb/volumes/17), [23](https://vldb.org/pvldb/volumes/17), [22](https://vldb.org/pvldb/vol16-volume-info/), [21](https://vldb.org/pvldb/vol15-volume-info/), [21](http://www.vldb.org/pvldb/vol14/), [20](http://vldb.org/pvldb/vol13-volume-info/) | -                                                            |
| [SIGCOMM](https://dblp.uni-trier.de/search?q=federate%20venue%3ASIGCOMM%3A) | 25                                                           | -                                                            |
| [INFOCOM](https://dblp.uni-trier.de/search?q=federate%20venue%3AINFOCOM%3A) | [25](https://infocom2025.ieee-infocom.org/program/accepted-paper-list-main-conference), [24](https://infocom2024.ieee-infocom.org/program/accepted-paper-list-main-conference), [23](https://infocom2023.ieee-infocom.org/program/accepted-paper-list-main-conference), [22](https://infocom2022.ieee-infocom.org/program/accepted-paper-list-main-conference), [21](https://infocom2021.ieee-infocom.org/accepted-paper-list-main-conference.html), [20](https://infocom2020.ieee-infocom.org/accepted-paper-list-main-conference.html) | [19](https://infocom2019.ieee-infocom.org/accepted-paper-list-main-conference.html), 18 |
| [MobiCom](https://dblp.uni-trier.de/search?q=federate%20venue%3AMobiCom%3A) | [25](https://www.sigmobile.org/mobicom/2025/accepted.html), [24](https://www.sigmobile.org/mobicom/2024/accepted.html), [23](https://www.sigmobile.org/mobicom/2023/accepted.html), [22](https://www.sigmobile.org/mobicom/2022/accepted.html), [21](https://www.sigmobile.org/mobicom/2021/accepted.html), [20](https://www.sigmobile.org/mobicom/2020/accepted.php) |                                                              |
| [NSDI](https://dblp.uni-trier.de/search?q=federate%20venue%3ANSDI%3A) | [25](https://www.usenix.org/conference/nsdi25/technical-sessions), 23([1](https://www.usenix.org/conference/nsdi23/spring-accepted-papers), [2](https://www.usenix.org/conference/nsdi23/fall-accepted-papers)) | -                                                            |
| [WWW](https://dblp.uni-trier.de/search?q=federate%20venue%3AWWW%3A) | [26](https://dl.acm.org/doi/proceedings/10.1145/3774904), [25](https://dl.acm.org/doi/proceedings/10.1145/3696410), [24](https://www2024.thewebconf.org/accepted/research-tracks/), [23](https://www2023.thewebconf.org/program/accepted-papers/), [22](https://www2022.thewebconf.org/accepted-papers/), [21](https://www2021.thewebconf.org/program/papers-program/links/index.html) |                                                              |
| [OSDI](https://dblp.org/search?q=federated%20venue%3AOSDI%3A) | 21                                                           | -                                                            |
| [SOSP](https://dblp.org/search?q=federated%20venue%3ASOSP%3A) | 21                                                           | -                                                            |
| [ISCA](https://dblp.org/search?q=federated%20venue%3AISCA%3A) | [24](https://www.iscaconf.org/isca2024/program/)             | -                                                            |
| [MLSys](https://dblp.org/search?q=federated%20venue%3AMLSys%3A) | [25](https://proceedings.mlsys.org/paper_files/paper/2025), [24](https://proceedings.mlsys.org/paper_files/paper/2024), [23](https://proceedings.mlsys.org/paper_files/paper/2023), [22](https://proceedings.mlsys.org/paper_files/paper/2022), [20](https://proceedings.mlsys.org/paper_files/paper/2020) | [19](https://proceedings.mlsys.org/paper_files/paper/2019)   |
| [EuroSys](https://dblp.uni-trier.de/search?q=federated%20streamid%3Aconf%2Feurosys%3A) | [26](https://2026.eurosys.org/papers.html#papers), [25](https://2025.eurosys.org/accepted-papers.html), [24](https://2024.eurosys.org/accepted-papers.html), [23](https://2023.eurosys.org/accepted-papers.html), 22, 21, 20 |                                                              |
| [TPDS](https://dblp.uni-trier.de/search?q=federated%20streamid%3Ajournals%2Ftpds%3A) (J) | 26, 25, 24, 23, 22, 21, 20                                   | -                                                            |
| [DAC](https://dblp.uni-trier.de/search?q=federate%20venue%3ADAC%3A) | 25, 24, 22, 21                                               | -                                                            |
| [TOCS](https://dblp.uni-trier.de/search?q=federate%20streamid%3Ajournals%2Ftocs%3A) | -                                                            | -                                                            |
| [TOS](https://dblp.uni-trier.de/search?q=federate%20streamid%3Ajournals%2Ftos%3A) | -                                                            | -                                                            |
| [TCAD](https://dblp.uni-trier.de/search?q=federate%20streamid%3Ajournals%2Ftcad%3A) | 26, 25, 24, 23, 22, 21                                       | -                                                            |
| [TC](https://dblp.uni-trier.de/search?q=federate%20streamid%3Ajournals%2Ftc%3A) | 26, 25, 24, 23, 22, 21                                       | -                                                            |
| [ICSE](https://dblp.uni-trier.de/search?q=federated%20streamid%3Aconf%2Ficse%3A) | [25](https://conf.researchr.org/track/icse-2025/icse-2025-research-track), [23](https://conf.researchr.org/track/icse-2023/icse-2023-technical-track?#event-overview), 21 | -                                                            |
| [FOCS](https://dblp.uni-trier.de/search?q=federate%20streamid%3Ajournals%2Ffocs%3A) | -                                                            | -                                                            |
| [STOC](https://dblp.uni-trier.de/search?q=federate%20streamid%3Aconf%2Fstoc%3A) | -                                                            | -                                                            |

</details>




**keywords**

Statistics: :fire: code is available & stars >= 100 | :star: citation >= 50 | :mortar_board: Top-tier venue 

**`kg.`**: Knowledge Graph |   **`data.`**: dataset  |   **`surv.`**: survey




## fl in top-tier journal

Papers of federated learning in Nature(and its sub-journals), Cell, Science(and Science Advances) and PANS refers to [WOS](https://www.webofscience.com/wos/woscc/summary/ed3f4552-5450-4de7-bf2c-55d01e20d5de-4301299e/relevance/1) search engine.

<details open>
<summary>fl in top-tier journal</summary>

|Title                                                           |    Venue                    |    Year    |    Materials|
| ------------------------------------------------------------ | --------------------- | ---- | ------------------------------------------------------------ |
| Towards compute-efficient Byzantine-robust federated learning with fully homomorphic encryption | Nat. Mach. Intell. | 2025 | [[PUB](https://www.nature.com/articles/s42256-025-01107-6)] [[PDF](https://arxiv.org/abs/2408.06197)] [[CODE](https://github.com/siyang-jiang/Lancelot)] |
| Incentivizing inclusive contributions in model sharing markets | Nat. Commun. | 2025 | [[PUB](https://www.nature.com/articles/s41467-025-62959-5)] [[CODE](https://github.com/19dx/iPFL)] |
| FedECA: federated external control arms for causal inference with time-to-event data in distributed settings | Nat. Commun. | 2025 | [[PUB](https://www.nature.com/articles/s41467-025-62525-z)] [[CODE](https://github.com/owkin/fedeca)] |
| Privacy-preserving multicenter differential protein abundance analysis with FedProt | Nat. Comput. Sci. | 2025 | [[PUB](https://www.nature.com/articles/s43588-025-00832-7)] [[CODE](https://github.com/Freddsle/FedProt)] |
| Towards fair decentralized benchmarking of healthcare AI algorithms with the Federated Tumor Segmentation (FeTS) challenge | Nat. Commun. | 2025 | [[PUB](https://www.nature.com/articles/s41467-025-60466-1)] [[CODE](https://github.com/mlcommons/medperf/tree/fets-challenge)] |
| A fully open AI foundation model applied to chest radiography | Nature | 2025 | [[PUB](https://www.nature.com/articles/s41586-025-09079-8)] [[CODE](https://github.com/jlianglab/Ark)] |
| Federated learning using a memristor compute-in-memory chip with in situ physical unclonable function and true random number generator | Nat. Electron. | 2025 | [[PUB](https://www.nature.com/articles/s41928-025-01390-6)] |
| A framework reforming personalized Internet of Things by federated meta-learning | Nat. Commun. | 2025 | [[PUB](https://www.nature.com/articles/s41467-025-59217-z)] [[CODE](https://github.com/IntelligentSystemsLab/generic_and_open_learning_federator/)] |
| Achieving flexible fairness metrics in federated medical imaging | Nat. Commun. | 2025 | [[PUB](https://www.nature.com/articles/s41467-025-58549-0)] [[CODE](https://zenodo.org/records/15203267)] |
| Towards fairness-aware and privacy-preserving enhanced collaborative learning for healthcare | Nat. Commun. | 2025 | [[PUB](https://www.nature.com/articles/s41467-025-58055-3)] [[CODE](https://github.com/paridis-11/DynamicFL)] |
| Data-driven federated learning in drug discovery with knowledge distillation | Nat. Mach. Intell. | 2025 | [[PUB](https://www.nature.com/articles/s42256-025-00991-2)] [[CODE](https://github.com/LhasaLimited/FLuID_POC)] |
| Distributed cross-learning for equitable federated models - privacy-preserving prediction on data from five California hospitals | Nat. Commun. | 2025 | [[PUB](https://www.nature.com/articles/s41467-025-56510-9)] |
| Physical unclonable in-memory computing for simultaneous protecting private data and deep learning models | Nat. Commun. | 2025 | [[PUB](https://www.nature.com/articles/s41467-025-56412-w)] [[新闻](https://ic.pku.edu.cn/kxyj/kycg1/d2c084006150492c93ae3e6b0cb1d7df.htm)] |
| MatSwarm: trusted swarm transfer learning driven materials computation for secure big data sharing | Nat. Commun. | 2024 | [[PUB](https://www.nature.com/articles/s41467-024-53431-x)] [[CODE](https://github.com/SICC-Group/MatSwarm)] |
| Introducing edge intelligence to smart meters via federated split learning | Nat. Commun. | 2024 | [[PUB](https://www.nature.com/articles/s41467-024-53352-9)] [[新闻](https://www.ces.org.cn/html/report/24110829-1.htm)] |
| An international study presenting a federated learning AI platform for pediatric brain tumors | Nat. Commun. | 2024 | [[PUB](https://www.nature.com/articles/s41467-024-51172-5)] [[CODE](https://github.com/edhlee/FLPedBrain)] |
| PPML-Omics: A privacy-preserving federated machine learning method protects patients’ privacy in omic data | Science Advances | 2024 | [[PUB](https://www.science.org/doi/10.1126/sciadv.adh8601)] [[CODE](https://github.com/JoshuaChou2018/PPML-Omics)] |
| Federated learning is not a cure-all for data ethics | Nat. Mach. Intell.(Comment) | 2024 | [[PUB](https://www.nature.com/articles/s42256-024-00813-x)] |
| Robustly federated learning model for identifying high-risk patients with postoperative gastric cancer recurrence | Nat. Commun. | 2024 | [[PUB](https://www.nature.com/articles/s41467-024-44946-4)] [[CODE](https://github.com/baofengguat/RFLM-project/)] |
| Selective knowledge sharing for privacy-preserving federated distillation without a good teacher | Nat. Commun. | 2024 | [[PUB](https://www.nature.com/articles/s41467-023-44383-9)] [[PDF](https://arxiv.org/abs/2304.01731)] [[CODE](https://github.com/shaojiawei07/Selective-FD)] |
| A federated learning system for precision oncology in Europe: DigiONE | Nat. Med. (Comment) | 2024 | [[PUB](https://www.nature.com/articles/s41591-023-02715-8)] |
| Multi-client distributed blind quantum computation with the Qline architecture | Nat. Commun. | 2023 | [[PUB](https://www.nature.com/articles/s41467-023-43617-0)] [[PDF](https://arxiv.org/abs/2306.05195)] |
| Device-independent quantum randomness–enhanced zero-knowledge proof | PNAS | 2023 | [[PUB](https://www.pnas.org/doi/10.1073/pnas.2205463120)] [[PDF](https://arxiv.org/abs/2111.06717)] [[新闻](https://www.nsfc.gov.cn/publish/portal0/tab448/info90817.htm)] |
| Collaborative and privacy-preserving retired battery sorting for profitable direct recycling via federated machine learning | Nat. Commun. | 2023 | [[PUB](https://www.nature.com/articles/s41467-023-43883-y)] |
| Advocating for neurodata privacy and neurotechnology regulation | Nat. Protoc. (Perspective) | 2023 | [[PUB](https://www.nature.com/articles/s41596-023-00873-0)] |
| Federated benchmarking of medical artificial intelligence with MedPerf | Nat. Mach. Intell. | 2023 | [[PUB](https://www.nature.com/articles/s42256-023-00652-2)] [[PDF](https://arxiv.org/abs/2110.01406)] [[CODE](https://github.com/mlcommons/MedPerf)] |
| Algorithmic fairness in artificial intelligence for medicine and healthcare | Nat. Biomed. Eng. (Perspective) | 2023 | [[PUB](https://www.nature.com/articles/s41551-023-01056-8)] [[PDF](https://arxiv.org/abs/2110.00603)] |
| Differentially private knowledge transfer for federated learning | Nat. Commun. | 2023 | [[PUB](https://www.nature.com/articles/s41467-023-38794-x)] [[CODE](https://github.com/taoqi98/PrivateKT)] |
| Decentralized federated learning through proxy model sharing | Nat. Commun. | 2023 | [[PUB](https://www.nature.com/articles/s41467-023-38569-4)] [[PDF](https://arxiv.org/abs/2111.11343)] [[CODE](https://github.com/layer6ai-labs/ProxyFL)] |
| Federated machine learning in data-protection-compliant research | Nat. Mach. Intell.(Comment) | 2023 | [[PUB](https://www.nature.com/articles/s42256-022-00601-5)] |
| Federated learning for predicting histological response to neoadjuvant chemotherapy in triple-negative breast cancer | Nat. Med. | 2023 | [[PUB](https://www.nature.com/articles/s41591-022-02155-w)] [[CODE](https://github.com/Substra/substra)] |
| Federated learning enables big data for rare cancer boundary detection | Nat. Commun. | 2022 | [[PUB](https://www.nature.com/articles/s41467-022-33407-5)] [[PDF](https://arxiv.org/abs/2204.10836)] [[CODE](https://github.com/FETS-AI/Front-End)] |
| Federated learning and Indigenous genomic data sovereignty | Nat. Mach. Intell. (Comment) | 2022 | [[PUB](https://www.nature.com/articles/s42256-022-00551-y)] |
| Federated disentangled representation learning for unsupervised brain anomaly detection | Nat. Mach. Intell. | 2022 | [[PUB](https://www.nature.com/articles/s42256-022-00515-2)] [[PDF](https://doi.org/https://doi.org/10.21203/rs.3.rs-722389/v1)] [[CODE](https://doi.org/10.5281/zenodo.6604161)] |
| Shifting machine learning for healthcare from development to deployment and from models to data | Nat. Biomed. Eng. (Review Article) | 2022 | [[PUB](https://www.nature.com/articles/s41551-022-00898-y)] |
| A federated graph neural network framework for privacy-preserving personalization | Nat. Commun. | 2022 | [[PUB](https://www.nature.com/articles/s41467-022-30714-9)] [[CODE](https://github.com/wuch15/FedPerGNN)] [[解读](https://zhuanlan.zhihu.com/p/487383715)] |
| Communication-efficient federated learning via knowledge distillation | Nat. Commun. | 2022 | [[PUB](https://www.nature.com/articles/s41467-022-29763-x)] [[PDF](https://arxiv.org/abs/2108.13323)] [[CODE](https://zenodo.org/record/6383473)] |
| Lead federated neuromorphic learning for wireless edge artificial intelligence | Nat. Commun. | 2022 | [[PUB](https://www.nature.com/articles/s41467-022-32020-w)] [[CODE](https://github.com/GOGODD/FL-EDGE-COMPUTING/releases/tag/federated_learning)] [[解读](https://zhuanlan.zhihu.com/p/549087420)] |
| A novel decentralized federated learning approach to train on globally  distributed, poor quality, and protected private medical data | Sci. Rep. | 2022 | [[PUB](https://www.nature.com/articles/s41598-022-12833-x)] |
| Advancing COVID-19 diagnosis with privacy-preserving collaboration in artificial intelligence | Nat. Mach. Intell. | 2021 | [[PUB](https://www.nature.com/articles/s42256-021-00421-z)] [[PDF](https://arxiv.org/abs/2111.09461)] [[CODE](https://github.com/HUST-EIC-AI-LAB/UCADI)] |
| Federated learning for predicting clinical outcomes in patients with COVID-19 | Nat. Med. | 2021 | [[PUB](https://www.nature.com/articles/s41591-021-01506-3)] [[CODE](https://www.nature.com/articles/s41591-021-01506-3#code-availability)] |
| Adversarial interference and its mitigations in privacy-preserving collaborative machine learning | Nat. Mach. Intell.(Perspective) | 2021 | [[PUB](https://www.nature.com/articles/s42256-021-00390-3)] |
| Swarm Learning for decentralized and confidential clinical machine learning :star: | Nature :mortar_board: | 2021 | [[PUB](https://www.nature.com/articles/s41586-021-03583-3)] [[CODE](https://github.com/HewlettPackard/swarm-learning)] [[SOFTWARE](https://myenterpriselicense.hpe.com)] [[解读](https://zhuanlan.zhihu.com/p/379434722)] |
| End-to-end privacy preserving deep learning on multi-institutional medical imaging | Nat. Mach. Intell. | 2021 | [[PUB](https://www.nature.com/articles/s42256-021-00337-8)] [[CODE](https://doi.org/10.5281/zenodo.4545599)] [[解读](https://zhuanlan.zhihu.com/p/484801505)] |
| Communication-efficient federated learning | PANS. | 2021 | [[PUB](https://www.pnas.org/doi/full/10.1073/pnas.2024789118)] [[CODE](https://code.ihub.org.cn/projects/4394/repository/revisions/master/show/PNAS)] |
| Breaking medical data sharing boundaries by using synthesized radiographs | Science. Advances. | 2020 | [[PUB](https://www.science.org/doi/10.1126/sciadv.abb7973)] [[CODE](https://github.com/peterhan91/Thorax_GAN)] |
| Secure, privacy-preserving and federated machine learning in medical imaging :star: | Nat. Mach. Intell.(Perspective) | 2020 | [[PUB](https://www.nature.com/articles/s42256-020-0186-1)] |

<!-- END:fl-in-top-tier-journal -->

</details>



## fl in top ai conference and journal

Federated Learning papers accepted by top AI(Artificial Intelligence) conference and journal, Including [IJCAI](https://dblp.org/db/conf/ijcai/index.html)(International Joint Conference on Artificial Intelligence), [AAAI](https://dblp.uni-trier.de/db/conf/aaai/index.html)(AAAI Conference on Artificial Intelligence), [AISTATS](https://dblp.uni-trier.de/db/conf/aistats/index.html)(Artificial Intelligence and Statistics), [ALT](https://dblp.org/db/conf/alt/index.html)(International Conference on Algorithmic Learning Theory), [AI](https://dblp.uni-trier.de/db/journals/ai/index.html)(Artificial Intelligence).

- [IJCAI](https://dblp.uni-trier.de/search?q=federate%20venue%3AIJCAI%3A) [2025](https://www.ijcai.org/proceedings/2025/), [2024](https://www.ijcai.org/proceedings/2024/), [2023](https://www.ijcai.org/proceedings/2023/), [2022](https://www.ijcai.org/proceedings/2022/), [2021](https://www.ijcai.org/proceedings/2021/), [2020](https://www.ijcai.org/proceedings/2020/), [2019](https://www.ijcai.org/proceedings/2019/)
- [AAAI](https://dblp.uni-trier.de/search?q=federate%20venue%3AAAAI%3A) [2026](https://dblp.org/db/conf/aaai/aaai2026.html), [2025](https://dblp.org/db/conf/aaai/aaai2025.html), [2024](https://dblp.org/db/conf/aaai/aaai2024.html), [2023](https://dblp.org/db/conf/aaai/aaai2023), [2022](https://aaai.org/Conferences/AAAI-22/wp-content/uploads/2021/12/AAAI-22_Accepted_Paper_List_Main_Technical_Track.pdf), [2021](https://aaai.org/Conferences/AAAI-21/wp-content/uploads/2020/12/AAAI-21_Accepted-Paper-List.Main_.Technical.Track_.pdf), [2020](https://aaai.org/Conferences/AAAI-20/wp-content/uploads/2020/01/AAAI-20-Accepted-Paper-List.pdf)
- [AISTATS](https://dblp.uni-trier.de/search?q=federate%20venue%3AAISTATS%3A) [2025](https://proceedings.mlr.press/v258/), [2024](http://proceedings.mlr.press/v238/), [2023](http://proceedings.mlr.press/v206/), [2022](http://proceedings.mlr.press/v151/), [2021](http://proceedings.mlr.press/v130/), [2020](http://proceedings.mlr.press/v108/)
- [ALT](https://dblp.uni-trier.de/search?q=federate%20streamid%3Aconf%2Falt%3A) 2022
- [AI](https://dblp.uni-trier.de/search?q=federate%20streamid%3Ajournals%2Fai%3A) 2026, 2025, 2023

<details open>
<summary>fl in top ai conference and journal</summary>
<!-- START:fl-in-top-ai-conference-and-journal -->


<!-- END:fl-in-top-ai-conference-and-journal -->

### 2026

#### AAAI

- A Unified Self-Regulating Training Framework for Federated Deep Reinforcement Learning. [[PUB](https://doi.org/10.1609/aaai.v40i32.39946)]
- Bi-level Personalization for Federated Foundation Models: A Task-vector Aggregation Approach. [[PUB](https://doi.org/10.1609/aaai.v40i33.39991)]
- BIQ: Bisection Interval Quantization for Communication-efficient Federated Learning. [[PUB](https://doi.org/10.1609/aaai.v40i25.39259)]
- Breaking Cross-View Associations: Byzantine Model Poisoning Attack against Vertical Federated Learning. [[PUB](https://doi.org/10.1609/aaai.v40i48.42327)]
- Breaking the Aggregation Bottleneck in Federated Recommendation: A Personalized Model Merging Approach. [[PUB](https://doi.org/10.1609/aaai.v40i17.38472)]
- Causality-inspired Federated Learning for Dynamic Spatio-Temporal Graphs. [[PUB](https://doi.org/10.1609/aaai.v40i28.39569)]
- Causally-Aware Attribute Completion for Incomplete Federated Graph Clustering. [[PUB](https://doi.org/10.1609/aaai.v40i28.39547)]
- Class-Aware Active Annotation in Federated Semi-Supervised Learning for Medical Image Classification. [[PUB](https://doi.org/10.1609/aaai.v40i32.39964)]
- Communication-Efficient Heterogeneous Federated Learning with Sparse Prototypes in Resource-Constrained Environments. [[PUB](https://doi.org/10.1609/aaai.v40i27.39441)]
- CoRe-Fed: Bridging Collaborative and Representation Fairness via Federated Embedding Distillation. [[PUB](https://doi.org/10.1609/aaai.v40i29.39628)]
- DA-DFGAS: Differentiable Federated Graph Neural Architecture Search with Distribution-Aware Attentive Aggregation. [[PUB](https://doi.org/10.1609/aaai.v40i28.39573)]
- Data Heterogeneity and Forgotten Labels in Split Federated Learning. [[PUB](https://doi.org/10.1609/aaai.v40i31.39794)]
- Decoupling Shared and Personalized Knowledge: A Dual-Branch Federated Learning Framework for Multi-Domain with Non-IID Data. [[PUB](https://doi.org/10.1609/aaai.v40i29.39660)]
- Divide, Conquer and Unite: Hierarchical Style-Recalibrated Prototype Alignment for Federated Medical Segmentation. [[PUB](https://doi.org/10.1609/aaai.v40i34.40109)]
- DoBlock: Blocking Malicious Association Propagation for Backdoor-Robust Federated Learning Under Domain Skew. [[PUB](https://doi.org/10.1609/aaai.v40i30.39778)]
- Domain-Aware Suppression and Aggregation for Federated DG ReID. [[PUB](https://doi.org/10.1609/aaai.v40i14.38214)]
- DSFedMed: Dual-Scale Federated Medical Image Segmentation via Mutual Distillation Between Foundation and Lightweight Models. [[PUB](https://doi.org/10.1609/aaai.v40i15.38239)]
- Enhanced Federated Deep Multi-View Clustering Under Uncertainty Scenario. [[PUB](https://doi.org/10.1609/aaai.v40i32.39891)]
- Equilibrium-Driven Vertical Federated Learning with Selective Privacy Protection. [[PUB](https://doi.org/10.1609/aaai.v40i35.40206)]
- EvoFMVC: Trusted Federated Multi-View Clustering with Evolutionary Fusion. [[PUB](https://doi.org/10.1609/aaai.v40i33.40057)]
- Feature-Aware One-Shot Federated Learning via Hierarchical Token Sequences. [[PUB](https://doi.org/10.1609/aaai.v40i28.39557)]
- FedAdamW: A Communication-Efficient Optimizer with Convergence and Generalization Guarantees for Federated Large Models. [[PUB](https://doi.org/10.1609/aaai.v40i28.39549)]
- FedALT: Federated Fine-Tuning Through Adaptive Local Training with Rest-of-World LoRA. [[PUB](https://doi.org/10.1609/aaai.v40i24.39054)]
- FedARKS: Federated Aggregation via Robust and Discriminative Knowledge Selection and Integration for Person Re-identification. [[PUB](https://doi.org/10.1609/aaai.v40i14.38124)]
- FedAU2: Attribute Unlearning for User-Level Federated Recommender Systems with Adaptive and Robust Adversarial Training. [[PUB](https://doi.org/10.1609/aaai.v40i28.39500)]
- FedBRICK: Structural Bias Aware Heterogeneous Foundation Model Federated Tuning. [[PUB](https://doi.org/10.1609/aaai.v40i34.40083)]
- FedCD: Towards Consolidated Distillation for Heterogeneous Federated Learning. [[PUB](https://doi.org/10.1609/aaai.v40i28.39494)]
- FedCure: Mitigating Participation Bias in Semi-Asynchronous Federated Learning with Non-IID Data. [[PUB](https://doi.org/10.1609/aaai.v40i25.39176)]
- FedDNA: DNA Sequence Reconstruction via Deep Evidential Learning and Personalized Federated Aggregation. [[PUB](https://doi.org/10.1609/aaai.v40i28.39524)]
- Federated CLIP for Resource-Efficient Heterogeneous Medical Image Classification. [[PUB](https://doi.org/10.1609/aaai.v40i32.39912)]
- Federated Context-Aware Personalized Recommendation. [[PUB](https://doi.org/10.1609/aaai.v40i31.39888)]
- Federated Graph-level Clustering Network with Attribute Inference. [[PUB](https://doi.org/10.1609/aaai.v40i26.39307)]
- Federated Incomplete Multi-View Clustering with Tensorized Low-Rank Constraint. [[PUB](https://doi.org/10.1609/aaai.v40i25.39251)]
- Federated Learning Playground. [[PUB](https://doi.org/10.1609/aaai.v40i48.42349)]
- Federated Linear Dueling Bandits. [[PUB](https://doi.org/10.1609/aaai.v40i26.39361)]
- Federated Vision-Language-Recommendation with Personalized Fusion. [[PUB](https://doi.org/10.1609/aaai.v40i28.39503)]
- FedLAGC: Towards High Performance System-Heterogeneous Federated Learning via Layer-Adaptive Submodel Extraction and Gradient Correction. [[PUB](https://doi.org/10.1609/aaai.v40i26.39338)]
- FedMerge: Federated Model Merging for Personalization. [[PUB](https://doi.org/10.1609/aaai.v40i24.39113)]
- FedPKDA: Personalized Federated Learning with Privacy-Preserving Knowledge Dynamic Alignment. [[PUB](https://doi.org/10.1609/aaai.v40i33.40037)]
- FedPM: Federated Learning Using Second-order Optimization with Preconditioned Mixing of Local Parameters. [[PUB](https://doi.org/10.1609/aaai.v40i26.39368)]
- FedP²EFT: Federated Learning to Personalize PEFT for Multilingual LLMs. [[PUB](https://doi.org/10.1609/aaai.v40i27.39443)]
- FedRNC: Addressing Spatio-Temporal Label Misalignment in Federated Noisy Class-Incremental Learning. [[PUB](https://doi.org/10.1609/aaai.v40i26.39359)]
- FedSDA: Federated Stain Distribution Alignment for Non-IID Histopathological Image Classification. [[PUB](https://doi.org/10.1609/aaai.v40i12.37918)]
- FedSDWC: Federated Synergistic Dual-Representation Weak Causal Learning for OOD. [[PUB](https://doi.org/10.1609/aaai.v40i26.39364)]
- FedSEA-LLaMA: A Secure, Efficient and Adaptive Federated Splitting Framework for Large Language Models. [[PUB](https://doi.org/10.1609/aaai.v40i34.40100)]
- FedShard: Federated Unlearning with Efficiency Fairness and Performance Fairness. [[PUB](https://doi.org/10.1609/aaai.v40i32.39895)]
- FedSkeleton: Secure Multi-Party Graph Skeleton Construction for Privacy-Preserving Federated Time-Series Forecasting. [[PUB](https://doi.org/10.1609/aaai.v40i25.39210)]
- FedTopo: Topology-Informed Representation Alignment in Federated Learning Under Non-I.I.D. Conditions. [[PUB](https://doi.org/10.1609/aaai.v40i26.39337)]
- FILTER: A Framework for Defending Against Backdoor Attacks in Vertical Federated Learning. [[PUB](https://doi.org/10.1609/aaai.v40i42.40859)]
- Generalizable Heterogeneity-aware Federated Feature and Basic-matrix Consistency Learning. [[PUB](https://doi.org/10.1609/aaai.v40i27.39436)]
- Generic Adversarial Attack Framework Against Graph-based Vertical Federated Learning. [[PUB](https://doi.org/10.1609/aaai.v40i42.40878)]
- Good Gradients Poison Your Model: Evading Defenses in Federated Learning via Boundary-adaptive Perturbation. [[PUB](https://doi.org/10.1609/aaai.v40i16.38328)]
- HealSplit: Towards Self-Healing Through Adversarial Distillation in Split Federated Learning. [[PUB](https://doi.org/10.1609/aaai.v40i42.40908)]
- Horizontal and Vertical Federated Causal Structure Learning via Higher-order Cumulants. [[PUB](https://doi.org/10.1609/aaai.v40i24.39116)]
- Incomplete Multi-View Unsupervised Federated Feature Selection via Cooperative Particle Swarm Optimization and Tensor-Aligned Learning. [[PUB](https://doi.org/10.1609/aaai.v40i33.40005)]
- Inter-Client Dependency Recovery with Hidden Global Components for Federated Traffic Prediction. [[PUB](https://doi.org/10.1609/aaai.v40i34.40130)]
- Intra-Class Unbiased Prototype Aggregation and Classifier Collaboration for Personalized Federated Learning. [[PUB](https://doi.org/10.1609/aaai.v40i34.40113)]
- Investigating Social Bias Propagation in Federated Fine-tuning of Large Language Models. [[PUB](https://doi.org/10.1609/aaai.v40i46.41316)]
- LSHFed: Robust and Communication-Efficient Federated Learning with Locally-Sensitive Hashing Gradient Mapping. [[PUB](https://doi.org/10.1609/aaai.v40i25.39184)]
- MSCFL: Model Structure-Aware Clustered Federated Learning for System Heterogeneity and Data Drift. [[PUB](https://doi.org/10.1609/aaai.v40i32.39952)]
- Multi-Modal Style Transfer-based Prompt Tuning for Efficient Federated Domain Generalization. [[PUB](https://doi.org/10.1609/aaai.v40i25.39177)]
- MultiKD: Backdoor Defense in Federated Graph Learning via Attention-Guided Multi-Teacher Distillation. [[PUB](https://doi.org/10.1609/aaai.v40i33.40051)]
- Neuro-Symbolic Federated Learning over Heterogeneous Data-Views: A Structured Approach to Distributive EHR Modelling. [[PUB](https://doi.org/10.1609/aaai.v40i29.39624)]
- Oblivionis: A Lightweight Learning and Unlearning Framework for Federated Large Language Models. [[PUB](https://doi.org/10.1609/aaai.v40i33.40045)]
- Optimal Look-back Horizon for Time Series Forecasting in Federated Learning. [[PUB](https://doi.org/10.1609/aaai.v40i30.39781)]
- OPTION: An Online Pricing Strategy for Asynchronous Federated Learning Against Free-Riding Attacks. [[PUB](https://doi.org/10.1609/aaai.v40i29.39653)]
- OursFed: Provable Group Fairness-Aware Federated Learning Against Distrust and Fragility. [[PUB](https://doi.org/10.1609/aaai.v40i32.39926)]
- PAGE: A Unified Approach for Federated Graph Unlearning. [[PUB](https://doi.org/10.1609/aaai.v40i24.39038)]
- Personalized Federated Graph-Level Clustering Network. [[PUB](https://doi.org/10.1609/aaai.v40i28.39546)]
- Personalized Federated Learning with Bidirectional Communication Compression via One-Bit Random Sketching. [[PUB](https://doi.org/10.1609/aaai.v40i25.39185)]
- Plug-and-Play Parameter-Efficient Tuning of Embeddings for Federated Recommendation. [[PUB](https://doi.org/10.1609/aaai.v40i19.38660)]
- Poisoning with a Pill: Circumventing Detection in Federated Learning. [[PUB](https://doi.org/10.1609/aaai.v40i26.39290)]
- PPFL: A Parameter Behavior-Driven Plug-in Personalization Engine for Federated Learning. [[PUB](https://doi.org/10.1609/aaai.v40i24.39073)]
- Prior Refinement Is Better: Diffusion-Driven Graph Harmonization for Federated Graph Learning. [[PUB](https://doi.org/10.1609/aaai.v40i34.40163)]
- Re-architecting Personalized Federated Learning for Demanding Edge Environments. [[PUB](https://doi.org/10.1609/aaai.v40i29.39655)]
- REMISVFU: Vertical Federated Unlearning via Representation Misdirection for Intermediate Output Feature. [[PUB](https://doi.org/10.1609/aaai.v40i32.39911)]
- Retaliatory Attacks Against Federated Unlearning via Data Leakage. [[PUB](https://doi.org/10.1609/aaai.v40i30.39725)]
- Ripple Shapley: Data Influence Attribution in One Federated Training Run. [[PUB](https://doi.org/10.1609/aaai.v40i33.40034)]
- Scaling Law Analysis in Federated Learning: How to Select the Optimal Model Size?. [[PUB](https://doi.org/10.1609/aaai.v40i24.39122)]
- SFedHIFI: Fire Rate-Based Heterogeneous Information Fusion for Spiking Federated Learning. [[PUB](https://doi.org/10.1609/aaai.v40i31.39787)]
- ShadeEdit: A Utility-Preserving and Defense-Evasive Knowledge Manipulation Attack in Federated LLMs. [[PUB](https://doi.org/10.1609/aaai.v40i41.40787)]
- SMoFi: Step-wise Momentum Fusion for Split Federated Learning on Heterogeneous Data. [[PUB](https://doi.org/10.1609/aaai.v40i32.39977)]
- Tackling Resource-Constrained and Data-Heterogeneity in Federated Learning with Double-Weight Sparse Pack. [[PUB](https://doi.org/10.1609/aaai.v40i32.39979)]
- TOFA: Training-Free One-Shot Federated Adaptation for Vision-Language Models. [[PUB](https://doi.org/10.1609/aaai.v40i33.40058)]
- Topological Federated Clustering via Gravitational Potential Fields Under Local Differential Privacy. [[PUB](https://doi.org/10.1609/aaai.v40i28.39582)]
- Towards Federated Clustering: A Client-wise Private Graph Aggregation Framework. [[PUB](https://doi.org/10.1609/aaai.v40i26.39311)]
- Towards Robust Text-Attributed Federated Graph Learning: Multimodal Threats and Defense. [[PUB](https://doi.org/10.1609/aaai.v40i30.39732)]
- TransFR: Transferable Federated Recommendation with Adapter Tuning on Pre-trained Language Models. [[PUB](https://doi.org/10.1609/aaai.v40i33.40048)]
- Unlocking Dynamic Inter-Client Spatial Dependencies: A Federated Spatio-temporal Graph Learning Method for Traffic Flow Forecasting. [[PUB](https://doi.org/10.1609/aaai.v40i2.37083)]
- Venom: Liquid Diffusion-Guided Gradient Inversion for Breaking Differential Privacy in Federated Learning. [[PUB](https://doi.org/10.1609/aaai.v40i26.39333)]
- AEFGL: Reverse Auction and Value Evaluation-Based Federated Graph Learning Incentive Mechanism (Student Abstract). [[PUB](https://doi.org/10.1609/aaai.v40i48.42197)]
- Federated Cross-Modal Style-Aware Prompt Generation (Student Abstract). [[PUB](https://doi.org/10.1609/aaai.v40i48.42268)]
- UniVarFL: Uniformity and Variance Regularized Federated Learning for Heterogeneous Data (Student Abstract). [[PUB](https://doi.org/10.1609/aaai.v40i48.42220)]
- A Dialogue-Based Learning Analytics Framework for Collaborative Game-Based Learning. [[PUB](https://doi.org/10.1609/aaai.v40i48.42116)]
- Advancing Protein Design via Multi-Agent Reinforcement Learning with Pareto-Based Collaborative Optimization. [[PUB](https://doi.org/10.1609/aaai.v40i2.37142)]
- CL-Guard: Defending DNNs Against Backdoors via Fine-Grained Neuron Analysis and Collaborative Dual-Network Learning. [[PUB](https://doi.org/10.1609/aaai.v40i42.40904)]
- Collaborative Dual Representations for Semi-Supervised Partial Label Learning. [[PUB](https://doi.org/10.1609/aaai.v40i24.39049)]
- Collaborative Feature Matching with Progressive Correspondence Learning. [[PUB](https://doi.org/10.1609/aaai.v40i9.37669)]
- Collaborative Representation Learning for Alignment of Tactile, Language, and Vision Modalities. [[PUB](https://doi.org/10.1609/aaai.v40i22.38956)]
- Cross-Domain Few-Shot Learning via Multi-View Collaborative Optimization with Vision-Language Models. [[PUB](https://doi.org/10.1609/aaai.v40i24.39086)]
- DeLo: Dual Decomposed Low-Rank Experts Collaboration for Continual Missing Modality Learning. [[PUB](https://doi.org/10.1609/aaai.v40i28.39561)]
- Do Not Merge My Model! Safeguarding Open-Source LLMs Against Unauthorized Model Merging. [[PUB](https://doi.org/10.1609/aaai.v40i37.40433)]
- Drift-aware Collaborative Assistance Mixture of Experts for Heterogeneous Multistream Learning. [[PUB](https://doi.org/10.1609/aaai.v40i19.38656)]
- From Parameter to Representation: A Closed-Form Approach for Controllable Model Merging. [[PUB](https://doi.org/10.1609/aaai.v40i32.39902)]
- GLOBA: Rethinking Parameter Conflicts in Model Merging. [[PUB](https://doi.org/10.1609/aaai.v40i28.39572)]
- Learning to Collaborate: An Orchestrated-Decentralized Framework for Peer-to-Peer LLM Federation. [[PUB](https://doi.org/10.1609/aaai.v40i30.39742)]
- Learning to Deliberate: Meta-policy Collaboration for Agentic LLMs with Multi-agent Reinforcement Learning. [[PUB](https://doi.org/10.1609/aaai.v40i35.40228)]
- Learning to Generate and Extract: A Multi-Agent Collaboration Framework for Zero-Shot Document-Level Event Arguments Extraction. [[PUB](https://doi.org/10.1609/aaai.v40i41.40767)]
- LLM Collaboration with Multi-Agent Reinforcement Learning. [[PUB](https://doi.org/10.1609/aaai.v40i38.40487)]
- M-Loss: Quantifying Model Merging Compatibility with Limited Unlabeled Data. [[PUB](https://doi.org/10.1609/aaai.v40i31.39854)]
- MedSAMix: A Training-Free Model Merging Approach for Medical Image Segmentation. [[PUB](https://doi.org/10.1609/aaai.v40i14.38161)]
- MergeDNA: Context-Aware Genome Modeling with Dynamic Tokenization Through Token Merging. [[PUB](https://doi.org/10.1609/aaai.v40i1.37032)]
- Multi-view Invariance Learning for 3D Scene Graph Pre-training via Collaborative Cross-Modal Regularization. [[PUB](https://doi.org/10.1609/aaai.v40i7.37435)]
- Outlier Matters: Efficient Long-to-Short Reasoning via Outlier-Guided Model Merging. [[PUB](https://doi.org/10.1609/aaai.v40i41.40828)]
- RCP-Merging: Merging Long Chain-of-Thought Models with Domain-Specific Models by Considering Reasoning Capability as Prior. [[PUB](https://doi.org/10.1609/aaai.v40i40.40722)]
- Rep Deep &amp; Machine Learning: Exemplar-Free Continual Video Action Recognition via Slow-Fast Collaborative Learning. [[PUB](https://doi.org/10.1609/aaai.v40i42.40924)]
- Revisiting Contrastive Learning in Collaborative Filtering via Parallel Graph Filters. [[PUB](https://doi.org/10.1609/aaai.v40i17.38521)]
- Think Wise, Collaborate Effectively: A Rationale-Aware LLM-Based Recommender with Reinforcement Learning from Collaborative Signals. [[PUB](https://doi.org/10.1609/aaai.v40i18.38590)]
- Unifying Multi-View Knowledge for Graph Learning via Model Collaboration. [[PUB](https://doi.org/10.1609/aaai.v40i32.39914)]
- Geometrically Inspired Kernel Machines for Collaborative Learning Beyond Gradient Descent (Abstract Reprint). [[PUB](https://doi.org/10.1609/aaai.v40i47.41386)]

#### AI

- Disentangling data distribution for optimal and communication-efficient federated learning. [[PUB](https://doi.org/10.1016/j.artint.2025.104455)]
- Federated neural nonparametric point processes. [[PUB](https://doi.org/10.1016/j.artint.2025.104454)]

### 2025

#### IJCAI

- Exploiting Label Skewness for Spiking Neural Networks in Federated Learning. [[PUB](https://www.ijcai.org/proceedings/2025/767)]
- FedHAN: A Cache-Based Semi-Asynchronous Federated Learning Framework Defending Against Poisoning Attacks in Heterogeneous Clients. [[PUB](https://www.ijcai.org/proceedings/2025/379)]
- Heterogeneous Federated Learning with Scalable Server Mixture-of-Experts. [[PUB](https://www.ijcai.org/proceedings/2025/610)]
- Pixel-wise Divide and Conquer for Federated Vessel Segmentation. [[PUB](https://www.ijcai.org/proceedings/2025/540)]
- Universal Backdoor Defense via Label Consistency in Vertical Federated Learning. [[PUB](https://www.ijcai.org/proceedings/2025/528)]
- Where Does This Data Come From? Enhanced Source Inference Attacks in Federated Learning. [[PUB](https://www.ijcai.org/proceedings/2025/536)]
- Optimizing Personalized Federated Learning Through Adaptive Layer-Wise Learning. [[PUB](https://www.ijcai.org/proceedings/2025/541)] [[CODE](https://github.com/lancasterJie/FLAYER)]
- FedDLAD: A Federated Learning Dual-Layer Anomaly Detection Framework for Enhancing Resilience Against Backdoor Attacks. [[PUB](https://www.ijcai.org/proceedings/2025/559)] [[CODE](https://github.com/dingbinb/FedDLAD)]
- Federated Multi-view Graph Clustering with Incomplete Attribute Imputation. [[PUB](https://www.ijcai.org/proceedings/2025/570)]
- ADPFedGNN: Adaptive Decoupling Personalized Federated Graph Neural Network. [[PUB](https://www.ijcai.org/proceedings/2025/585)]
- Approximated Behavioral Metric-based State Projection for Federated Reinforcement Learning. [[PUB](https://www.ijcai.org/proceedings/2025/590)]
- FissionVAE: Federated Non-IID Image Generation with Latent Space and Decoder Decomposition. [[PUB](https://www.ijcai.org/proceedings/2025/597)]
- FedBG: Proactively Mitigating Bias in Cross-Domain Graph Federated Learning Using Background Data. [[PUB](https://www.ijcai.org/proceedings/2025/602)]
- FedCCH: Automatic Personalized Graph Federated Learning for Inter-Client and Intra-Client Heterogeneity. [[PUB](https://www.ijcai.org/proceedings/2025/333)]
- FedCPD:Personalized Federated Learning with Prototype-Enhanced Representation and Memory Distillation. [[PUB](https://www.ijcai.org/proceedings/2025/612)]
- Data Poisoning Attack Defense and Evolutionary Domain Adaptation for Federated Medical Image Segmentation. [[PUB](https://www.ijcai.org/proceedings/2025/146)]
- Distilling A Universal Expert from Clustered Federated Learning. [[PUB](https://www.ijcai.org/proceedings/2025/620)]
- CSAHFL:Clustered Semi-Asynchronous Hierarchical Federated Learning for Dual-layer Non-IID in Heterogeneous Edge Computing Networks. [[PUB](https://www.ijcai.org/proceedings/2025/621)]
- FAST: A Lightweight Mechanism Unleashing Arbitrary Client Participation in Federated Learning. [[PUB](https://www.ijcai.org/proceedings/2025/628)]
- Hypernetwork Aggregation for Decentralized Personalized Federated Learning. [[PUB](https://www.ijcai.org/proceedings/2025/161)]
- Federated Domain Generalization with Decision Insight Matrix. [[PUB](https://www.ijcai.org/proceedings/2025/633)]
- Generic Adversarial Attack Framework Against Vertical Federated Learning. [[PUB](https://www.ijcai.org/proceedings/2025/646)]
- One-shot Federated Learning Methods: A Practical Guide. [[PUB](https://www.ijcai.org/proceedings/2025/1174)]
- Federated Learning at the Forefront of Fairness: A Multifaceted Perspective. [[PUB](https://www.ijcai.org/proceedings/2025/1177)]
- Performance Guaranteed Poisoning Attacks in Federated Learning: A Sliding Mode Approach. [[PUB](https://www.ijcai.org/proceedings/2025/670)]
- Federated Deconfounding and Debiasing Learning for Out-of-Distribution Generalization. [[PUB](https://www.ijcai.org/proceedings/2025/677)]
- FedAPA: Server-side Gradient-Based Adaptive Personalized Aggregation for Federated Learning on Heterogeneous Data. [[PUB](https://www.ijcai.org/proceedings/2025/692)] [[CODE](https://github.com/Yuxia-Sun/FL_FedAPA)]
- An Empirical Study of Federated Prompt Learning for Vision Language Model. [[PUB](https://www.ijcai.org/proceedings/2025/1188)]
- FedCM: Client Clustering and Migration in Federated Learning via Gradient Path Similarity and Update Direction Deviation. [[PUB](https://www.ijcai.org/proceedings/2025/706)]
- Zero-shot Federated Unlearning via Transforming from Data-Dependent to Personalized Model-Centric. [[PUB](https://www.ijcai.org/proceedings/2025/733)]
- DaringFed: A Dynamic Bayesian Persuasion Pricing for Online Federated Learning Under Two-sided Incomplete Information. [[PUB](https://www.ijcai.org/proceedings/2025/744)]
- Backdoor Attack on Vertical Federated Graph Neural Network Learning. [[PUB](https://www.ijcai.org/proceedings/2025/877)]
- Federated Low-Rank Adaptation for Foundation Models: A Survey. [[PUB](https://www.ijcai.org/proceedings/2025/1196)]
- Learning Heterogeneous Performance-Fairness Trade-offs in Federated Learning. [[PUB](https://www.ijcai.org/proceedings/2025/761)]
- FedSaaS: Class-Consistency Federated Semantic Segmentation via Global Prototype Supervision and Local Adversarial Harmonization. [[PUB](https://www.ijcai.org/proceedings/2025/770)]
- A Multi-Granularity Clustering Approach for Federated Backdoor Defense with the Adam Optimizer. [[PUB](https://www.ijcai.org/proceedings/2025/771)]
- Federated Stochastic Bilevel Optimization with Fully First-Order Gradients. [[PUB](https://www.ijcai.org/proceedings/2025/784)]
- AdaptPFL: Unlocking Cross-Device Palmprint Recognition via Adaptive Personalized Federated Learning with Feature Decoupling. [[PUB](https://www.ijcai.org/proceedings/2025/787)]
- Rethinking Federated Graph Learning: A Data Condensation Perspective. [[PUB](https://www.ijcai.org/proceedings/2025/775)]
- MMGIA: Gradient Inversion Attack Against Multimodal Federated Learning via Intermodal Correlation. [[PUB](https://www.ijcai.org/proceedings/2025/886)]
- Enhancing the Performance of Global Model by Improving the Adaptability of Local Models in Federated Learning. [[PUB](https://www.ijcai.org/proceedings/2025/798)]
- Finite-Time Analysis of Heterogeneous Federated Temporal Difference Learning. [[PUB](https://www.ijcai.org/proceedings/2025/808)]
- Inconsistency-Based Federated Active Learning. [[PUB](https://www.ijcai.org/proceedings/2025/812)]
- CSAHFL: Clustered Semi-Asynchronous Hierarchical Federated Learning for Dual-layer Non-IID in Heterogeneous Edge Computing Networks. [[PUB](https://doi.org/10.24963/ijcai.2025/621)]
- FedCPD: Personalized Federated Learning with Prototype-Enhanced Representation and Memory Distillation. [[PUB](https://doi.org/10.24963/ijcai.2025/612)]
- Bidirectional Human-AI Collaboration for Equitable Student Performance Prediction via Deep Uncertainty Learning. [[PUB](https://doi.org/10.24963/ijcai.2025/1114)]
- Credit Assignment and Fine-Tuning Enhanced Reinforcement Learning for Collaborative Spatial Crowdsourcing. [[PUB](https://doi.org/10.24963/ijcai.2025/459)]
- Cross-modal Collaborative Representation Learning for Text-to-Image Person Retrieval. [[PUB](https://doi.org/10.24963/ijcai.2025/240)]
- Enhancing Mixture of Experts with Independent and Collaborative Learning for Long-Tail Visual Recognition. [[PUB](https://doi.org/10.24963/ijcai.2025/93)] [[CODE](https://github.com/PolarisLight/ICL)]

#### AISTATS

- Optimising Clinical Federated Learning through Mode Connectivity-based Model Aggregation. [[PUB](https://proceedings.mlr.press/v258/thakur25a.html)] [[CODE](https://github.com/AnshThakur/FedMode)]
- FedBaF: Federated Learning Aggregation Biased by a Foundation Model. [[PUB](https://proceedings.mlr.press/v258/park25b.html)]
- Global Group Fairness in Federated Learning via Function Tracking. [[PUB](https://proceedings.mlr.press/v258/rychener25a.html)] [[CODE](https://github.com/yvesrychener/Fair-FL)]
- On the Power of Adaptive Weighted Aggregation in Heterogeneous Federated Learning and Beyond. [[PUB](https://proceedings.mlr.press/v258/zeng25b.html)] [[CODE](https://github.com/dunzeng/FedAWARE)]
- Federated UCBVI: Communication-Efficient Federated Regret Minimization with Heterogeneous Agents. [[PUB](https://proceedings.mlr.press/v258/labbi25a.html)] [[CODE](https://github.com/Labbi-Safwan/Fed-UCBVI)]
- ADEPT: Hierarchical Bayes Approach to Personalized Federated Unsupervised Learning. [[PUB](https://proceedings.mlr.press/v258/ozkara25a.html)] [[CODE](https://github.com/kazkara/adept)]
- Federated Causal Inference: Multi-Study ATE Estimation beyond Meta-Analysis. [[PUB](https://proceedings.mlr.press/v258/khellaf25a.html)] [[CODE](https://github.com/RemiKhellaf/FedCausal-RCTs-Khellaf/)]
- The cost of local and global fairness in Federated Learning. [[PUB](https://proceedings.mlr.press/v258/duan25a.html)] [[CODE](https://github.com/papersubmission678/The-cost-of-local-and-global-fairness-in-FL)]
- Federated Communication-Efficient Multi-Objective Optimization. [[PUB](https://proceedings.mlr.press/v258/askin25a.html)] [[CODE](https://github.com/askinb/FedCMOO)]
- Refined Analysis of Constant Step Size Federated Averaging and Federated Richardson-Romberg Extrapolation. [[PUB](https://proceedings.mlr.press/v258/mangold25a.html)] [[CODE](https://pmangold.fr/papers/fed-richardson-romberg/supplementary.zip)]
- Personalizing Low-Rank Bayesian Neural Networks Via Federated Learning. [[PUB](https://proceedings.mlr.press/v258/zhang25l.html)] [[CODE](https://github.com/Bernie0115/LR-BPFL)]
- On the Convergence of Continual Federated Learning Using Incrementally Aggregated Gradients. [[PUB](https://proceedings.mlr.press/v258/keshri25a.html)] [[CODE](https://github.com/SatishKeshri/Continual_FL)]
- DPFL: Decentralized Personalized Federated Learning. [[PUB](https://proceedings.mlr.press/v258/kharrat25a.html)] [[CODE](https://github.com/salmakh1/DPFL)]
- Unbiased Quantization of the L1 Ball for Communication-Efficient Distributed Mean Estimation. [[PUB](https://proceedings.mlr.press/v258/babu25a.html)]

#### AI

- FedHM: Efficient federated learning for heterogeneous models via low-rank factorization. [[PUB](https://www.sciencedirect.com/science/article/pii/S0004370225000529)]

#### AAAI

- Learning Together Securely: Prototype-Based Federated Multi-Modal Hashing for Safe and Efficient Multi-Modal Retrieval. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34475)]
- Single-Loop Federated Actor-Critic across Heterogeneous Environments. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34469)]
- Improving Federated Domain Generalization Through Dynamical Weights Calculated from Data Influences on Global Model Update. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34468)]
- FedSA: A Unified Representation Learning via Semantic Anchors for Prototype-based Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34464)]
- FedGOG: Federated Graph Out-of-Distribution Generalization with Diffusion Data Exploration and Latent Embedding Decorrelation. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34459)]
- ConFREE: Conflict-free Client Update Aggregation for Personalized Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34449)]
- Personalized Label Inference Attack in Federated Transfer Learning via Contrastive Meta Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34438)]
- Rethinking Byzantine Robustness in Federated Recommendation from Sparse Aggregation Perspective. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33455)]
- Asynchronous Federated Clustering with Unknown Number of Clusters. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34429)]
- Generating Synthetic Data for Unsupervised Federated Learning of Cross-Modal Retrieval. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34415)]
- HaCore: Efficient Coreset Construction with Locality Sensitive Hashing for Vertical Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34409)]
- LoGoFair: Post-Processing for Local and Global Fairness in Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34404)]
- Multifaceted User Modeling in Recommendation: A Federated Foundation Models Approach. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33440)]
- Modeling Inter-Intra Heterogeneity for Graph Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34378)]
- pFedES: Generalized Proxy Feature Extractor Sharing for Model Heterogeneous Personalized Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34368)]
- First-Order Federated Bilevel Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34355)]
- GAS: Generative Activation-Aided Asynchronous Split Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/35503)]
- FedVCK: Non-IID Robust and Communication-Efficient Federated Learning via Valuable Condensed Knowledge for Medical Image Analysis. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/35497)]
- Federated Graph Condensation with Information Bottleneck Principles. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33417)]
- A High-Efficiency Federated Learning Method Using Complementary Pruning for D2D Communication (Student Abstract). [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/35318)]
- Federated Learning with Sample-level Client Drift Mitigation. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/35480)]
- Pilot: Building the Federated Multimodal Instruction Tuning Framework. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/35476)]
- Flexible Sharpness-Aware Personalized Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/35475)]
- MultiSFL: Towards Accurate Split Federated Learning via Multi-Model Aggregation and Knowledge Replay. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/32076)]
- PFedCS: A Personalized Federated Learning Method for Enhancing Collaboration among Similar Classifiers. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/35460)]
- Federated Graph Anomaly Detection Through Contrastive Learning with Global Negative Pairs. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/35458)]
- Fed-DFA: Federated Distillation for Heterogeneous Model Fusion Through the Adversarial Lens. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/35444)]
- Federated Recommendation with Explicitly Encoding Item Bias. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33395)]
- Defending Against Sophisticated Poisoning Attacks with RL-based Aggregation in Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34733)]
- Decentralized Federated Learning with Model Caching on Mobile Agents. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/35429)]
- Cluster Based Heterogeneous Federated Foundation Model Adaptation and Fine-Tuning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/35426)]
- FedFSL-CFRD: Personalized Federated Few-Shot Learning with Collaborative Feature Representation Disentanglement. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/35423)]
- Reinforcement Active Client Selection for Federated Heterogeneous Graph Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/35409)]
- Tackling Intertwined Data and Device Heterogeneities in Federated Learning with Unlimited Staleness. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/35405)]
- Federated Weakly Supervised Video Anomaly Detection with Multimodal Prompt. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/35398)]
- Overcoming Heterogeneous Data in Federated Medical Vision-Language Pre-training: A Triple-Embedding Model Selector Approach. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/32807)]
- Reputation-aware Revenue Allocation for Auction-based Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34296)]
- Learn How to Query from Unlabeled Data Streams in Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34287)]
- Efficient Federated Learning via Clients-to-Server Knowledge Distillation (Student Abstract). [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/35304)]
- Graph Consistency and Diversity Measurement for Federated Multi-View Clustering. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34277)]
- WHALE-FL: Wireless and Heterogeneity Aware Latency Efficient Federated Learning over Mobile Devices via Adaptive Subnetwork Scheduling. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34272)]
- Label-Free Backdoor Attacks in Vertical Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34246)]
- Incongruent Multimodal Federated Learning for Medical Vision and Language-based Multi-label Disease Detection. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/35054)]
- FedPIA – Permuting and Integrating Adapters Leveraging Wasserstein Barycenters for Finetuning Foundation Models in Multi-Modal Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34228)]
- Fair Federated Survival Analysis. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34214)]
- Federated t-SNE and UMAP for Distributed Data Visualization. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34204)]
- Cross-Silo Feature Space Alignment for Federated Learning on Clients with Imbalanced Data. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34201)]
- Federated Unsupervised Domain Generalization Using Global and Local Alignment of Gradients. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34197)]
- In-depth Analysis of Low-rank Matrix Factorisation in a Federated Setting. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34192)]
- Look Back for More: Harnessing Historical Sequential Updates for Personalized Federated Adapter Tuning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34187)]
- Breaking Data Silos in Parkinson’s Disease Diagnosis: An Adaptive Federated Learning Approach for Privacy-Preserving Facial Expression Analysis. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33572)]
- Federated Unlearning with Gradient Descent and Conflict Mitigation. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34181)]
- Dual-calibrated Co-training Framework for Personalized Federated Semi-Supervised Medical Image Segmentation. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/32671)]
- FedSPU: Personalized Federated Learning for Resource-Constrained Devices with Stochastic Parameter Update. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34172)]
- FedSum: Data-Efficient Federated Learning Under Data Scarcity Scenario for Text Summarization. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34129)]
- Data-Free Black-Box Federated Learning via Zeroth-Order Gradient Estimation. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34126)]
- FedCross: Intertemporal Federated Learning Under Evolutionary Games. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34104)]
- Exploit Gradient Skewness to Circumvent Byzantine Defenses for Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34094)]
- SemiDFL: A Semi-Supervised Paradigm for Decentralized Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34090)]
- Personalized Federated Learning for Spatio-Temporal Forecasting: A Dual Semantic Alignment-Based Contrastive Approach. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33328)]
- Federated Graph-Level Clustering Network. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34077)]
- LiD-FL: Towards List-Decodable Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34072)]
- Convergence Analysis of Federated Learning Methods Using Backward Error Analysis. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34060)]
- Progressive Distribution Matching for Federated Semi-Supervised Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/32551)]
- TTA-FedDG: Leveraging Test-Time Adaptation to Address Federated Domain Generalization. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34053)]
- Personalized Federated Collaborative Filtering: A Variational AutoEncoder Approach. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34047)]
- EBS-CFL: Efficient and Byzantine-robust Secure Clustered Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34046)]
- FedMSGL: A Self-Expressive Hypergraph Based Federated Multi-View Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/34007)]
- pFedGPA: Diffusion-based Generative Parameter Aggregation for Personalized Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33980)]
- FCOM: A Federated Collaborative Online Monitoring Framework via Representation Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33975)]
- FedCFA: Alleviating Simpson’s Paradox in Model Aggregation with Counterfactual Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33942)]
- Federated Learning with Heterogeneous LLMs: Integrating Small Student Client Models with a Large Hungry Model. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/35332)]
- PA3Fed: Period-Aware Adaptive Aggregation for Improved Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33912)]
- TRAIL: Trust-Aware Client Scheduling for Semi-Decentralized Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33524)]
- FedAA: A Reinforcement Learning Perspective on Adaptive Aggregation for Fair and Robust Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33878)]
- DCHM: Dynamic Collaboration of Heterogeneous Models Through Isomerism Learning in a Blockchain-Powered Federated Learning Framework. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33877)]
- Federated Assemblies. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33520)]
- Federated Causally Invariant Feature Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33866)] [[CODE](https://github.com/Xianjie-Guo/FedCIFL)]
- A New Federated Learning Framework Against Gradient Inversion Attacks. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33865)]
- Exploring Vacant Classes in Label-Skewed Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33864)]
- Capture Global Feature Statistics for One-Shot Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33862)]
- Multimodal Fusion Using Multi-View Domains for Data Heterogeneity in Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33839)]
- MFL-Owner: Ownership Protection for Multi-modal Federated Learning via Orthogonal Transform Watermark. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/32313)]
- Virtual Nodes Can Help: Tackling Distribution Shifts in Federated Graph Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33830)]
- Beyond Federated Prototype Learning: Learnable Semantic Anchors with Hyperspherical Contrast for Domain-Skewed Data. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33829)]
- Scalable Federated One-Step Multi-View Clustering with Tensorized Regularization. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33822)]
- SADBA: Self-Adaptive Distributed Backdoor Attack Against Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33820)]
- Large Language Models Enhanced Personalized Graph Neural Architecture Search in Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33814)]
- How Does the Smoothness Approximation Method Facilitate Generalization for Federated Adversarial Learning?. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33788)]
- Attribute Inference Attacks for Federated Regression Tasks. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33787)]
- Federated Binary Matrix Factorization Using Proximal Optimization. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33773)]
- Creating Coherence in Federated Non-Negative Matrix Factorization. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33772)]
- Rethinking the Starting Point: Collaborative Pre-Training for Federated Downstream Tasks. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33764)]
- DualGFL: Federated Learning with a Dual-Level Coalition-Auction Game. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33746)]
- Federated Foundation Models on Heterogeneous Time Series. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33739)]
- FedPop: Federated Population-based Hyperparameter Tuning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33732)]
- Enhancing Privacy in the Early Detection of Sexual Predators Through Federated Learning and Differential Privacy. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/35005)]
- EFSkip: A New Error Feedback with Linear Speedup for Compressed Federated Learning with Arbitrary Data Heterogeneity. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33700)]
- Little Is Enough: Boosting Privacy by Sharing Only Hard Labels in Federated Semi-Supervised Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/33678)]
- Breaking Data Silos in Parkinson&apos;s Disease Diagnosis: An Adaptive Federated Learning Approach for Privacy-Preserving Facial Expression Analysis. [[PUB](https://doi.org/10.1609/aaai.v39i13.33572)]
- FedCFA: Alleviating Simpson&apos;s Paradox in Model Aggregation with Counterfactual Federated Learning. [[PUB](https://doi.org/10.1609/aaai.v39i17.33942)]
- Collaborative Evolution: Multi-Round Learning Between Large and Small Language Models for Emergent Fake News Detection. [[PUB](https://doi.org/10.1609/aaai.v39i1.32109)]
- Collaborative Learning for 3D Hand-Object Reconstruction and Compositional Action Recognition from Egocentric RGB Videos Using Superquadrics. [[PUB](https://doi.org/10.1609/aaai.v39i7.32800)]
- DSRC: Learning Density-Insensitive and Semantic-Aware Collaborative Representation Against Corruptions. [[PUB](https://doi.org/10.1609/aaai.v39i9.33078)]
- Learning to Collaborate with Unknown Agents in the Absence of Reward. [[PUB](https://doi.org/10.1609/aaai.v39i13.33589)]
- MergeNet: Knowledge Migration Across Heterogeneous Models, Tasks, and Modalities. [[PUB](https://doi.org/10.1609/aaai.v39i5.32510)]
- Multi-concept Model Immunization through Differentiable Model Merging. [[PUB](https://doi.org/10.1609/aaai.v39i10.33145)]
- Multi-View Collaborative Learning Network for Speech Deepfake Detection. [[PUB](https://doi.org/10.1609/aaai.v39i1.32094)]
- Multimodal Promptable Token Merging for Diffusion Models. [[PUB](https://doi.org/10.1609/aaai.v39i16.33894)]
- Paid with Models: Optimal Contract Design for Collaborative Machine Learning. [[PUB](https://doi.org/10.1609/aaai.v39i13.33552)]
- The Dynamic Duo of Collaborative Masking and Target for Advanced Masked Autoencoder Learning. [[PUB](https://doi.org/10.1609/aaai.v39i18.34145)]
- Towards Efficient Collaboration via Graph Modeling in Reinforcement Learning. [[PUB](https://doi.org/10.1609/aaai.v39i16.33813)]

### 2024

#### alt
- Optimal Regret Bounds for Collaborative Learning in Bandits. [[PUB](https://proceedings.mlr.press/v237/shidani24a.html)]
#### IJCAI

- Federated Multi-View Clustering via Tensor Factorization. [[PUB](https://www.ijcai.org/proceedings/2024/438)]
- Efficient Federated Multi-View Clustering with Integrated Matrix Factorization and K-Means. [[PUB](https://www.ijcai.org/proceedings/2024/439)]
- LG-FGAD: An Effective Federated Graph Anomaly Detection Framework. [[PUB](https://www.ijcai.org/proceedings/2024/416)]
- Federated Prompt Learning for Weather Foundation Models on Devices. [[PUB](https://www.ijcai.org/proceedings/2024/638)]
- Breaking Barriers of System Heterogeneity: Straggler-Tolerant Multimodal Federated Learning via Knowledge Distillation. [[PUB](https://www.ijcai.org/proceedings/2024/419)]
- Unlearning during Learning: An Efficient Federated Machine Unlearning Method. [[PUB](https://www.ijcai.org/proceedings/2024/446)]
- Practical Hybrid Gradient Compression for Federated Learning Systems. [[PUB](https://www.ijcai.org/proceedings/2024/458)]
- Sample Quality Heterogeneity-aware Federated Causal Discovery through Adaptive Variable Space Selection. [[PUB](https://www.ijcai.org/proceedings/2024/450)] [[CODE](https://github.com/Xianjie-Guo/FedACD)]
- Feature Norm Regularized Federated Learning: Utilizing Data Disparities for Model Performance Gains. [[PUB](https://www.ijcai.org/proceedings/2024/457)] [[CODE](https://github.com/LonelyMoonDesert/FNR-FL)]
- Dirichlet-based Uncertainty Quantification for Personalized Federated Learning with Improved Posterior Networks. [[PUB](https://www.ijcai.org/proceedings/2024/788)]
- FedConPE: Efficient Federated Conversational Bandits with Heterogeneous Clients. [[PUB](https://www.ijcai.org/proceedings/2024/501)]
- DarkFed: A Data-Free Backdoor Attack in Federated Learning. [[PUB](https://www.ijcai.org/proceedings/2024/491)]
- Scalable Federated Unlearning via Isolated and Coded Sharding. [[PUB](https://www.ijcai.org/proceedings/2024/503)]
- Enhancing Dual-Target Cross-Domain Recommendation with Federated Privacy-Preserving Learning. [[PUB](https://www.ijcai.org/proceedings/2024/238)]
- Label Leakage in Vertical Federated Learning: A Survey. [[PUB](https://www.ijcai.org/proceedings/2024/902)]
- The Rise of Federated Intelligence: From Federated Foundation Models Toward Collective Intelligence. [[PUB](https://www.ijcai.org/proceedings/2024/980)]
- LEAP: Optimization Hierarchical Federated Learning on Non-IID Data with Coalition Formation Game. [[PUB](https://www.ijcai.org/proceedings/2024/515)]
- EAB-FL: Exacerbating Algorithmic Bias through Model Poisoning Attacks in Federated Learning. [[PUB](https://www.ijcai.org/proceedings/2024/51)]
- Knowledge Distillation in Federated Learning: A Practical Guide. [[PUB](https://www.ijcai.org/proceedings/2024/905)]
- FedGCS: A Generative Framework for Efficient Client Selection in Federated Learning via Gradient-based Optimization. [[PUB](https://www.ijcai.org/proceedings/2024/526)]
- FedPFT: Federated Proxy Fine-Tuning of Foundation Models. [[PUB](https://www.ijcai.org/proceedings/2024/531)] [[CODE](https://github.com/pzp-dzd/FedPFT)]
- A Systematic Survey on Federated Semi-supervised Learning. [[PUB](https://www.ijcai.org/proceedings/2024/911)]
- Intelligent Agents for Auction-based Federated Learning: A Survey. [[PUB](https://www.ijcai.org/proceedings/2024/912)]
- A Bias-Free Revenue-Maximizing Bidding Strategy for Data Consumers in Auction-based Federated Learning. [[PUB](https://www.ijcai.org/proceedings/2024/552)]
- Dual Calibration-based Personalised Federated Learning. [[PUB](https://www.ijcai.org/proceedings/2024/551)]
- Stakeholder-oriented Decision Support for Auction-based Federated Learning. [[PUB](https://www.ijcai.org/proceedings/2024/972)]
- Redefining Contributions: Shapley-Driven Federated Learning. [[PUB](https://www.ijcai.org/proceedings/2024/554)] [[CODE](https://github.com/tnurbek/shapfed}{https://github.com/tnurbek/shapfed)]
- A Survey on Efficient Federated Learning Methods for Foundation Model Training. [[PUB](https://www.ijcai.org/proceedings/2024/919)]
- From Optimization to Generalization: Fair Federated Learning against Quality Shift via Inter-Client Sharpness Matching. [[PUB](https://www.ijcai.org/proceedings/2024/575)] [[CODE](https://github.com/wnn2000/FFL4MIA)]
- FBLG: A Local Graph Based Approach for Handling Dual Skewed Non-IID Data in Federated Learning. [[PUB](https://www.ijcai.org/proceedings/2024/585)]
- FedFa: A Fully Asynchronous Training Paradigm for Federated Learning. [[PUB](https://www.ijcai.org/proceedings/2024/584)]
- FedSSA: Semantic Similarity-based Aggregation for Efficient Model-Heterogeneous Personalized Federated Learning. [[PUB](https://www.ijcai.org/proceedings/2024/594)]
- FedES: Federated Early-Stopping for Hindering Memorizing Heterogeneous Label Noise. [[PUB](https://www.ijcai.org/proceedings/2024/599)]
- Personalized Federated Learning for Cross-City Traffic Prediction. [[PUB](https://www.ijcai.org/proceedings/2024/611)]
- Federated Adaptation for Foundation Model-based Recommendations. [[PUB](https://www.ijcai.org/proceedings/2024/603)]
- BADFSS: Backdoor Attacks on Federated Self-Supervised Learning. [[PUB](https://www.ijcai.org/proceedings/2024/61)]
- Estimating before Debiasing: A Bayesian Approach to Detaching Prior Bias in Federated Semi-Supervised Learning. [[PUB](https://www.ijcai.org/proceedings/2024/290)] [[CODE](https://github.com/GuogangZhu/FedDB)]
- FedTAD: Topology-aware Data-free Knowledge Distillation for Subgraph Federated Learning. [[PUB](https://www.ijcai.org/proceedings/2024/632)]
- Graph Collaborative Expert Finding with Contrastive Learning. [[PUB](https://www.ijcai.org/proceedings/2024/253)]

#### AISTATS

- BOBA: Byzantine-Robust Federated Learning with Label Skewness. [[PUB](https://proceedings.mlr.press/v238/bao24a.html)] [[PDF](https://arxiv.org/abs/2208.12932)] [[CODE](https://github.com/baowenxuan/BOBA)]
- Federated Linear Contextual Bandits with Heterogeneous Clients. [[PUB](https://proceedings.mlr.press/v238/blaser24a.html)] [[PDF](https://arxiv.org/abs/2403.00116)] [[CODE](https://github.com/blaserethan/HetoFedBandit)]
- Federated Experiment Design under Distributed Differential Privacy. [[PUB](https://proceedings.mlr.press/v238/chen24c.html)] [[PDF](https://arxiv.org/abs/2311.04375)] [[CODE](https://drive.google.com/file/d/1ugYQQEIOwqc1oH8cUe6rf1mV91c-cF_g/view?usp=drive_link)]
- Escaping Saddle Points in Heterogeneous Federated Learning via Distributed SGD with Communication Compression. [[PUB](https://proceedings.mlr.press/v238/chen24d.html)] [[PDF](https://arxiv.org/abs/2310.19059)]
- Asynchronous SGD on Graphs: a Unified Framework for Asynchronous Decentralized and Federated Optimization. [[PUB](https://proceedings.mlr.press/v238/even24a.html)] [[PDF](https://arxiv.org/abs/2311.00465)]
- SIFU: Sequential Informed Federated Unlearning for Efficient and Provable Client Unlearning in Federated Optimization. [[PUB](https://proceedings.mlr.press/v238/fraboni24a.html)] [[PDF](https://arxiv.org/abs/2211.11656)] [[CODE](https://github.com/Accenture/Labs-Federated-Learning/tree/SIFU)]
- Compression with Exact Error Distribution for Federated Learning. [[PUB](https://proceedings.mlr.press/v238/hegazy24a.html)] [[PDF](https://arxiv.org/abs/2310.20682)] [[CODE](https://github.com/mahegz/CompWithExactError)]
- Adaptive Federated Minimax Optimization with Lower Complexities. [[PUB](https://proceedings.mlr.press/v238/huang24c.html)] [[PDF](https://arxiv.org/abs/2211.07303)]
- Adaptive Compression in Federated Learning via Side Information. [[PUB](https://proceedings.mlr.press/v238/isik24a.html)] [[PDF](https://arxiv.org/abs/2306.12625)] [[CODE](https://github.com/FrancescoPase/Federated-KLMS)]
- On-Demand Federated Learning for Arbitrary Target Class Distributions. [[PUB](https://proceedings.mlr.press/v238/jeong24a.html)] [[CODE](https://github.com/eai-lab/On-DemandFL)]
- FedFisher: Leveraging Fisher Information for One-Shot Federated Learning. [[PUB](https://proceedings.mlr.press/v238/jhunjhunwala24a.html)] [[PDF](https://arxiv.org/abs/2403.12329)] [[CODE](https://github.com/Divyansh03/FedFisher)]
- Queuing dynamics of asynchronous Federated Learning. [[PUB](https://proceedings.mlr.press/v238/leconte24a.html)] [[PDF](https://arxiv.org/abs/2405.00017)]
- Personalized Federated X-armed Bandit. [[PUB](https://proceedings.mlr.press/v238/li24a.html)] [[PDF](https://arxiv.org/abs/2310.16323)] [[CODE](https://github.com/WilliamLwj/PyXAB)]
- Federated Learning For Heterogeneous Electronic Health Records Utilising Augmented Temporal Graph Attention Networks. [[PUB](https://proceedings.mlr.press/v238/molaei24a.html)] [[CODE](https://github.com/AnshThakur/FL4HeterogenousEHRs)]
- Stochastic Smoothed Gradient Descent Ascent for Federated Minimax Optimization. [[PUB](https://proceedings.mlr.press/v238/shen24c.html)] [[PDF](https://arxiv.org/abs/2311.00944)]
- Understanding Generalization of Federated Learning via Stability: Heterogeneity Matters. [[PUB](https://proceedings.mlr.press/v238/sun24a.html)] [[PDF](https://arxiv.org/abs/2306.03824)] [[CODE](https://github.com/fedcodexx/Generalization-of-Federated-Learning)]
- Provable Mutual Benefits from Federated Learning in Privacy-Sensitive Domains. [[PUB](https://proceedings.mlr.press/v238/tsoy24a.html)] [[PDF](https://arxiv.org/abs/2403.06672)] [[CODE](https://github.com/nikita-tsoy98/mutually-beneficial-federated-learning-replication)]
- Analysis of Privacy Leakage in Federated Large Language Models. [[PUB](https://proceedings.mlr.press/v238/vu24a.html)] [[PDF](https://arxiv.org/abs/2403.04784)] [[CODE](https://github.com/vunhatminh/FL_Attacks.git)]
- Invariant Aggregator for Defending against Federated Backdoor Attacks. [[PUB](https://proceedings.mlr.press/v238/wang24e.html)] [[PDF](https://arxiv.org/abs/2210.01834)] [[CODE](https://github.com/Xiaoyang-Wang/InvariantAggregator)]
- Communication-Efficient Federated Learning With Data and Client Heterogeneity. [[PUB](https://proceedings.mlr.press/v238/zakerinia24a.html)] [[PDF](https://arxiv.org/abs/2206.10032)] [[CODE](https://github.com/ShayanTalaei/QuAFL)]

#### AAAI

- FedMut: Generalized Federated Learning via Stochastic Mutation. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/29146)]
- Federated Partial Label Learning with Local-Adaptive Augmentation and Regularization. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/29562)] [[PAGE](https://underline.io/lecture/93915-federated-partial-label-learning-with-local-adaptive-augmentation-and-regularization)]
- No Prejudice! Fair Federated Graph Neural Networks for Personalized Recommendation. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/28950)] [[PAGE](https://underline.io/lecture/93775-no-prejudice-fair-federated-graph-neural-networks-for-personalized-recommendation)] [[PDF](https://arxiv.org/abs/2312.10080)] [[CODE](https://github.com/nimeshagrawal/F2PGNN-AAAI24)]
- Formal Logic Enabled Personalized Federated Learning through Property Inference. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/28962)] [[PDF](https://arxiv.org/abs/2401.07448)]
- Task-Agnostic Privacy-Preserving Representation Learning for Federated Learning against Attribute Inference Attacks. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/28965)] [[PAGE](https://underline.io/lecture/91722-task-agnostic-privacy-preserving-representation-learning-for-federated-learning-against-attribute-inference-attacks)] [[PDF](https://arxiv.org/abs/2312.06989)] [[CODE](https://github.com/TAPPFL/TAPPFL)]
- FairTrade: Achieving Pareto-Optimal Trade-Offs between Balanced Accuracy and Fairness in Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/28971)] [[PAGE](https://underline.io/lecture/93537-fairtrade-achieving-pareto-optimal-trade-offs-between-balanced-accuracy-and-fairness-in-federated-learning)]
- Combating Data Imbalances in Federated Semi-supervised Learning with Dual Regulators. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/28974)] [[PAGE](https://underline.io/lecture/92397-combating-data-imbalances-in-federated-semi-supervised-learning-with-dual-regulators)] [[PDF](https://arxiv.org/abs/2307.05358)]
- Fed-QSSL: A Framework for Personalized Federated Learning under Bitwidth and Data Heterogeneity. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/29025)] [[PAGE](https://underline.io/lecture/93417-fed-qssl-a-framework-for-personalized-federated-learning-under-bitwidth-and-data-heterogeneity)] [[PDF](https://arxiv.org/abs/2312.13380)]
- On Disentanglement of Asymmetrical Knowledge Transfer for Modality-Task Agnostic Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/29010)]
- FedDAT: An Approach for Foundation Model Finetuning in Multi-Modal Heterogeneous Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/29007)] [[PAGE](https://underline.io/lecture/91710-feddat-an-approach-for-foundation-model-finetuning-in-multi-modal-heterogeneous-federated-learning)] [[PDF](https://arxiv.org/abs/2308.12305)] [[CODE](https://github.com/HaokunChen245/FedDAT)]
- Watch Your Head: Assembling Projection Heads to Save the Reliability of Federated Models. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/29012)] [[PAGE](https://underline.io/lecture/91776-watch-your-head-assembling-projection-heads-to-save-the-reliability-of-federated-models)] [[PDF](https://arxiv.org/abs/2402.16255)]
- FedGCR: Achieving Performance and Fairness for  Federated Learning with Distinct Client Types via Group Customization  and Reweighting. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/29031)] [[PAGE](https://underline.io/lecture/92275-fedgcr-achieving-performance-and-fairness-for-federated-learning-with-distinct-client-types-via-group-customization-and-reweighting)] [[CODE](https://github.com/celinezheng/fedgcr)]
- Federated Modality-Specific Encoders and Multimodal Anchors for Personalized Brain Tumor Segmentation. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/27909)] [[PAGE](https://underline.io/lecture/91824-federated-modality-specific-encoders-and-multimodal-anchors-for-personalized-brain-tumor-segmentation)] [[PDF](https://arxiv.org/abs/2403.11803)] [[CODE](https://github.com/qdaiing/fedmema)]
- Exploiting Label Skews in Federated Learning with Model Concatenation. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/29063)] [[PAGE](https://underline.io/lecture/92569-exploiting-label-skews-in-federated-learning-with-model-concatenation)] [[PDF](https://arxiv.org/abs/2312.06290)] [[CODE](https://github.com/sjtudyq/FedConcat)]
- Complementary Knowledge Distillation for Robust and Privacy-Preserving Model Serving in Vertical Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/29958)] [[PAGE](https://underline.io/lecture/92937-complementary-knowledge-distillation-for-robust-and-privacy-preserving-model-serving-in-vertical-federated-learning)]
- Federated Learning via Input-Output Collaborative Distillation. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/30209)] [[PAGE](https://underline.io/lecture/94089-federated-learning-via-input-output-collaborative-distillation)] [[PDF](https://arxiv.org/abs/2312.14478)] [[CODE](https://github.com/lsl001006/fediod)]
- Calibrated One Round Federated Learning with Bayesian Inference in the Predictive Space. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/29122)] [[PAGE](https://underline.io/lecture/92727-calibrated-one-round-federated-learning-with-bayesian-inference-in-the-predictive-space)] [[PDF](https://arxiv.org/abs/2312.09817)] [[CODE](https://github.com/hasanmohsin/betaPredBayesFL)]
- FedCSL: A Scalable and Accurate Approach to Federated Causal Structure Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/29113)] [[PDF](https://github.com/Xianjie-Guo/FedCSL)] [[CODE](https://github.com/Xianjie-Guo/FedCSL)]
- FedFixer: Mitigating Heterogeneous Label Noise in Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/29179)] [[PAGE](https://underline.io/lecture/92327-fedfixer-mitigating-heterogeneous-label-noise-in-federated-learning)] [[PDF](https://arxiv.org/abs/2403.16561)]
- FedLPS: Heterogeneous Federated Learning for Multiple Tasks with Local Parameter Sharing. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/29181)] [[PAGE](https://underline.io/lecture/93122-fedlps-heterogeneous-federated-learning-for-multiple-tasks-with-local-parameter-sharing)] [[PDF](https://arxiv.org/abs/2402.08578)] [[CODE](https://github.com/jyzgh/FedLPS)]
- Provably Convergent Federated Trilevel Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/29190)] [[PDF](https://arxiv.org/abs/2312.11835)]
- Performative Federated Learning: A Solution to Model-Dependent and Heterogeneous Distribution Shifts. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/29191)] [[PAGE](https://underline.io/lecture/93963-performative-federated-learning-a-solution-to-model-dependent-and-heterogeneous-distribution-shifts)]
- General Commerce Intelligence: Glocally Federated NLP-Based Engine for Privacy-Preserving and Sustainable Personalized  Services of Multi-Merchants. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/30309)] [[PAGE](https://underline.io/lecture/91475-general-commerce-intelligence-glocally-federated-nlp-based-engine-for-privacy-preserving-and-sustainable-personalized-services-of-multi-merchants)]
- EMGAN: Early-Mix-GAN on Extracting Server-Side Model in Split Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/29258)] [[PAGE](https://underline.io/lecture/91709-emgan-early-mix-gan-on-extracting-server-side-model-in-split-federated-learning)] [[CODE](https://github.com/zlijingtao/SFL-MEA)]
- FedDiv: Collaborative Noise Filtering for Federated Learning with Noisy Labels. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/28095)] [[PAGE](https://underline.io/lecture/91764-feddiv-collaborative-noise-filtering-for-federated-learning-with-noisy-labels)] [[PDF](https://arxiv.org/abs/2312.12263)] [[CODE](https://github.com/lijichang/FLNL-FedDiv)]
- Point Transformer with Federated Learning for  Predicting Breast Cancer HER2 Status from Hematoxylin and Eosin-Stained  Whole Slide Images. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/28082)] [[PAGE](https://underline.io/lecture/92706-point-transformer-with-federated-learning-for-predicting-breast-cancer-her2-status-from-hematoxylin-and-eosin-stained-whole-slide-images)] [[PDF](https://arxiv.org/abs/2312.06454)] [[CODE](https://github.com/Boyden/PointTransformerFL)]
- FedNS: A Fast Sketching Newton-Type Algorithm for Federated Learning. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/29254)] [[PDF](https://arxiv.org/abs/2401.02734)] [[CODE](https://github.com/superlj666/fedns)]
- Federated X-armed Bandit. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/29267)] [[PAGE](https://underline.io/lecture/93049-federated-x-armed-bandit)] [[PDF](https://arxiv.org/abs/2205.15268)] [[CODE](https://github.com/williamlwj/pyxab)]
- Algorithmic Foundation of Federated Learning with Sequential Data. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/30291)]
- UFDA: Universal Federated Domain Adaptation with Practical Assumptions. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/29311)] [[PAGE](https://underline.io/lecture/93578-ufda-universal-federated-domain-adaptation-with-practical-assumptions)] [[PDF](https://arxiv.org/abs/2311.15570)] [[CODE](https://github.com/Xinhui-99/UFDA)]
- FedASMU: Efficient Asynchronous Federated Learning with Dynamic Staleness-Aware Model Update. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/29297)] [[PAGE](https://underline.io/lecture/92855-fedasmu-efficient-asynchronous-federated-learning-with-dynamic-staleness-aware-model-update)] [[PDF](https://arxiv.org/abs/2312.05770)]
- Language-Guided Transformer for Federated Multi-Label Classification. [[PUB](https://ojs.aaai.org/index.php/AAAI/article/view/29295)] [[PAGE](https://underline.io/lecture/93447-language-guided-transformer-for-federated-multi-label-class