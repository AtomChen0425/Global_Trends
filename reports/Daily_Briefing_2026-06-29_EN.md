# 🌐 Global Tech Intelligence Briefing - 2026-06-29
**Date:** 2026-06-29
**Generated At:** 12:17
**Data Sources:** Hacker News, GitHub Trending, ArXiv

---

## 📰 Hacker News (Top Stories)
### 1. [Sandia National Labs SA3000 8085 CPU](https://www.cpushack.com/2026/06/03/sandia-national-labs-sa3000-8085-cpu/)
🔥 28 | 🕒 2026-06-29 10:20
<details>
<summary><strong>📖 Summary:</strong> Sandia National Labs SA3000 8085 CPU | The CPU Shack Museum CPU History Museum for Intel C...</summary>

Sandia National Labs SA3000 8085 CPU | The CPU Shack Museum CPU History Museum for Intel CPUs, AMD Processor, Cyrix Microprocessors, Microcontrollers and more. Total CPU's: 20,000+ Total Manufacturers: 150+ Total EPROM's: 2000+ Home About Pictures Reference Trade Links Contact Us Test Boards/Products The CPU Shack has a variety of Test boards available for sale including: MCS-4/40 Boards RCA COSMAC Boards MCS-80 Boards Z80/8085/NSC800 Expansions MCS-8 Test Systems National SC/MP Test Board 6800/...

</details>

---
### 2. [HackerRank open sourced its ATS. My resume scored 90/100. Oh wait 74. No – 88](https://danunparsed.com/p/hackerrank-open-source-ats)
🔥 583 | 🕒 2026-06-29 01:44
<details>
<summary><strong>📖 Summary:</strong> HackerRank's Open-Source ATS Gave My Resume a Different Score Every Time. Dan Unparsed Sub...</summary>

HackerRank's Open-Source ATS Gave My Resume a Different Score Every Time. Dan Unparsed Subscribe Sign in HackerRank open sourced its ATS. My resume scored 90/100. Oh wait 74/100. No — 88/100. Actually 83/100. How hiring is becoming a luck filter. Dan Kinsky Jun 28, 2026 12 1 4 Share This open-source ATS by HackerRank has been blowing up recently: https://github.com/interviewstreet/hiring-agent It’s popped up on LinkedIn and Reddit with hundreds, sometimes thousands, of likes. 1 A coworker mentio...

</details>

---
### 3. [GLM 5.2 beats Claude in our benchmarks](https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks/)
🔥 911 | 🕒 2026-06-28 17:50
<details>
<summary><strong>📖 Summary:</strong> Here's an analysis of the provided article, focusing on technical insights and practical e...</summary>

Here's an analysis of the provided article, focusing on technical insights and practical experience:

**Background**

The article details an experiment by Semgrep to evaluate the performance of AI models in detecting Insecure Direct Object References (IDORs), a common access control vulnerability. The core question driving the research was to differentiate the contribution of the AI model itself versus the surrounding "harness" or scaffolding that provides context and guidance. This is particularly relevant as organizations increasingly integrate AI into security workflows.

**Technical Implementation**

Semgrep benchmarked several models, including GLM 5.2 (an open-weight model) and Claude Code/Opus, using a specific IDOR detection prompt and dataset. A key distinction was the environment: GLM 5.2 was tested with a basic Pydantic AI harness and a focused prompt, while Semgrep's internal multimodal pipeline operated within a purpose-built harness. This harness actively enumerates application endpoints, filters relevant code context, and guides the model, significantly aiding its detection capabilities.

**Application Scenarios**

The findings highlight the potential of open-weight models like GLM 5.2, which, even with minimal scaffolding, demonstrated competitive performance against more advanced proprietary models in specific tasks. This suggests that for certain vulnerability detection scenarios, open-weight models, when properly integrated and guided, can offer a cost-effective and powerful alternative. Semgrep's own multimodal pipeline, leveraging a sophisticated harness, achieved higher F1 scores, underscoring the value of structured context and task-specific tooling in maximizing AI effectiveness for complex security analysis.

**Summary**

This research reveals that while advanced AI models show promise in code security, the effectiveness of their application is heavily influenced by the surrounding infrastructure and guidance. Open-weight models are rapidly closing the gap, offering viable options for vulnerability detection. However, purpose-built harnesses, as demonstrated by Semgrep's multimodal pipeline, significantly enhance AI performance by providing structured context and task-specific optimization, proving crucial for robust security applications.

</details>

---
### 4. [Pollen (CEO Negus-Fancey, CTO Wright) tried to remove article, and Google helped](https://blog.pragmaticengineer.com/pollen-tried-to-remove-my-article-about-callum-negus-fancey-and-google-is-assisting-to-it/)
🔥 318 | 🕒 2026-06-29 09:28
<details>
<summary><strong>📖 Summary:</strong> Pollen tried to remove my article about CEO Callum Negus-Fancey and CTO Bradley Wright, an...</summary>

Pollen tried to remove my article about CEO Callum Negus-Fancey and CTO Bradley Wright, and Google is assisting with it - The Pragmatic Engineer Menu Close Home Newsletter Popular Articles The Software Engineer's Guidebook My Books Early trends Reading List Ethics statement Write a guest article Sponsors Investing Now Contact me About RSS Feed bluesky twitter youtube linkedin Subscribe Home Newsletter Popular Articles The Software Engineer's Guidebook My Books Early trends Reading List Ethics st...

</details>

---
### 5. [NUMA: Cores, memory, and the distance between them](https://edera.dev/stories/numa-part-1-cores-memory-and-the-distance-between-them)
🔥 42 | 🕒 2026-06-24 16:10
<details>
<summary><strong>📖 Summary:</strong> NUMA Explained: Why Memory Distance Slows Your VMs NUMA - Part 1: Cores, memory, and the d...</summary>

NUMA Explained: Why Memory Distance Slows Your VMs NUMA - Part 1: Cores, memory, and the distance between them June 23, 2026 - Steven Noonan Two virtual machines on the same host, configured identically, running the same workload. One of them is 20% slower than the other, consistently. Nothing is wrong with the workload, nothing is wrong with the host, no contention from other tenants. The slow one's memory just happens to be on the wrong side of an interconnect from the CPUs running it, and the...

</details>

---
## 🚀 GitHub Trending
> Projects with the highest star growth in the past 24 hours

### 1. [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat)
⭐ **Stars:** 15954
> 📝 SimpleX - the first messaging network operating without user identifiers of any kind - 100% private by design! iOS, Android and desktop apps 📱!

<details>
<summary><strong>🤖 AI Summary:</strong> This analysis focuses on the technical aspects of the SimpleX Chat project, as presented i...</summary>

This analysis focuses on the technical aspects of the SimpleX Chat project, as presented in the provided README content.

**Project Purpose and Core Differentiator:**
SimpleX Chat positions itself as a messaging platform fundamentally designed for privacy, with its primary technical differentiator being the complete absence of user identifiers. This means no phone numbers, email addresses, or any other persistent unique identifiers are required or used for user accounts. The platform aims to protect not only message content through strong encryption but also metadata such as who is communicating with whom and when. This design choice directly addresses privacy concerns often associated with traditional messaging applications.

**Implementation and Technical Features:**
The platform employs robust security measures, including double ratchet end-to-end encryption, augmented by an additional encryption layer. This suggests a layered security approach to ensure message confidentiality. SimpleX Chat offers cross-platform availability with mobile applications for iOS and Android, accessible via major app stores and direct downloads (APK). Additionally, it provides a terminal (console) application for Linux, MacOS, and Windows, catering to users who prefer command-line interfaces. The project also highlights integration with open-source language models as an area of development and contribution.

**Connectivity and Community Aspects:**
User connectivity is managed through a unique SimpleX address, facilitating private connections between individuals. The platform also supports user groups and communities, discoverable through a SimpleX Directory, which can be managed via a dedicated bot. This decentralized approach to group management aligns with the platform's privacy-centric ethos. The project actively encourages community involvement through contributions and donations, indicating a collaborative development model. The mention of a security audit by Trail of Bits and endorsements from privacy-focused organizations like Privacy Guides and Whonix further underscore the project's commitment to security and privacy.

</details>

---
### 2. [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)
⭐ **Stars:** 118261
> 📝 A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

<details>
<summary><strong>🤖 AI Summary:</strong> # 🎭 The Agency: AI Specialists Ready to Transform Your Workflow

&gt; **A complete AI agency ...</summary>

# 🎭 The Agency: AI Specialists Ready to Transform Your Workflow

> **A complete AI agency at your fingertips** - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

[![GitHub stars](https://img.shields.io/github/stars/msitarzewski/agency-agents?style=social)](https://github.com/msitarzewski/agency-agents)
[![License: MIT](https://img.shields.io/badge/License-MIT-yell...

</details>

---
### 3. [cupy/cupy](https://github.com/cupy/cupy)
⭐ **Stars:** 11690
> 📝 NumPy & SciPy for GPU

<details>
<summary><strong>🤖 AI Summary:</strong> CuPy is a Python library designed to bring NumPy and SciPy-like array manipulation capabil...</summary>

CuPy is a Python library designed to bring NumPy and SciPy-like array manipulation capabilities to NVIDIA CUDA and AMD ROCm GPUs. Its primary purpose is to enable users to accelerate their existing Python scientific computing workflows by offloading computations to the GPU. This is achieved by providing a familiar API that closely mirrors NumPy, allowing for a relatively seamless transition for developers accustomed to these libraries. The goal is to offer a significant performance boost for array-intensive tasks without requiring a complete rewrite of the codebase.

The implementation of CuPy focuses on providing a drop-in replacement for NumPy. This means that most NumPy functions are available within CuPy, operating on GPU-resident arrays. The library leverages CUDA or ROCm to perform these operations in parallel across GPU cores. Beyond basic array operations, CuPy also offers direct access to lower-level GPU features. This includes the ability to integrate with CUDA C/C++ programs using RawKernels, manage execution order and concurrency with Streams, and even invoke CUDA Runtime APIs directly. This dual approach allows for both ease of use for existing code and fine-grained control for performance optimization.

Installation of CuPy is facilitated through standard package managers like pip and conda, with pre-built binary packages available for common CUDA and ROCm versions on Linux and Windows. Specific packages are provided for different CUDA versions (e.g., `cupy-cuda12x`), and a slim installation option (`cupy-core`) is available for users who want to manage CUDA dependencies separately. Docker images are also provided for convenient deployment in containerized environments. This comprehensive installation strategy aims to make CuPy accessible across various development and deployment scenarios.

</details>

---
### 4. [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice)
⭐ **Stars:** 4091
> 📝 FluidVoice - Fastest macOS Offline Dictation app - Voice to Text fully Local. One ⭐ takes us a long way :))

<details>
<summary><strong>🤖 AI Summary:</strong> # FluidVoice

[![GitHub stars](https://img.shields.io/github/stars/altic-dev/FluidVoice?st...</summary>

# FluidVoice

[![GitHub stars](https://img.shields.io/github/stars/altic-dev/FluidVoice?style=social)](https://github.com/altic-dev/FluidVoice/stargazers)
[![Sponsor FluidVoice](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ea4aaa?logo=githubsponsors&logoColor=white)](https://github.com/sponsors/altic-dev)
[![Supported Models](https://img.shields.io/badge/Models-Nemotron%20Speech%203.5%20%7C%20Parakeet%20Flash%20%7C%20Parakeet%20v3%20%26%20v2%20%7C%20Cohere%20%7C%20Apple%20Speech%20%7C%...

</details>

---
### 5. [soxoj/maigret](https://github.com/soxoj/maigret)
⭐ **Stars:** 34107
> 📝 🕵️‍♂️ Collect a dossier on a person by username from 3000+ sites

<details>
<summary><strong>🤖 AI Summary:</strong> Maigret is a Python-based tool designed for comprehensive username-based reconnaissance. I...</summary>

Maigret is a Python-based tool designed for comprehensive username-based reconnaissance. Its primary purpose is to gather publicly available information about an individual by searching for their presence across a vast number of online platforms. The tool aims to create a dossier by identifying social media profiles, forum accounts, and other web presences associated with a given username, without requiring any API keys. This makes it a valuable asset for OSINT (Open Source Intelligence) practitioners and security researchers.

The implementation of Maigret relies on a substantial database of site configurations, supporting over 3,000 websites. For each site, it defines patterns and methods to check for username existence and extract relevant data. The tool performs web scraping and interacts with site APIs where possible to retrieve information such as profile URLs, user details, and links to other connected accounts. A key technical feature is its recursive search capability, which allows Maigret to discover new usernames or identifiers from initial findings and continue the search, effectively expanding the scope of the investigation.

Technically, Maigret is built to be extensible and efficient. It offers programmatic access, allowing it to be embedded within larger Python projects for custom workflows. The tool also incorporates mechanisms to handle common anti-scraping measures, including detecting and partially bypassing blocks and censorship. Users can tailor their searches by specifying tags for site categories or countries, or by opting to scan all supported sites. The project is developed in Python and requires version 3.10 or higher, indicating a reliance on modern Python language features.

</details>

---
## ✨ GitHub (New & Shiny)
### 1. [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec)
⭐ **Stars:** 2913
> 📝 DeepSpec: a full-stack codebase for training and evaluating speculative decoding algorithms

<details>
<summary><strong>🤖 AI Summary:</strong> # DeepSpec

DeepSpec is a full-stack codebase for training and evaluating draft models for...</summary>

# DeepSpec

DeepSpec is a full-stack codebase for training and evaluating draft models for speculative decoding. It contains data preparation utilities, draft model implementations, training code, and evaluation scripts.

## Environment

Install the Python dependencies:

```bash
python -m pip install -r requirements.txt
```

Data preparation additionally requires an inference engine to serve the target model when regenerating answers; see [scripts/data/README.md](./scripts/data/README.md) for de...

</details>

---
### 2. [bozhouDev/codex-orange-book](https://github.com/bozhouDev/codex-orange-book)
⭐ **Stars:** 2329
> 📝 Codex 橙皮书：从安装到实战案例的全链路 Codex 使用指南（非官方开源，含可下载 PDF）

<details>
<summary><strong>🤖 AI Summary:</strong> # Codex 橙皮书：从安装到实战案例的全链路使用指南

&gt; 非官方开源指南 · 持续更新版  
&gt; 写给开发者、独立开发者和 AI 工具重度用户的 Codex 使用手册。

|...</summary>

# Codex 橙皮书：从安装到实战案例的全链路使用指南

> 非官方开源指南 · 持续更新版  
> 写给开发者、独立开发者和 AI 工具重度用户的 Codex 使用手册。

| 版本 | 最后校验 | 资料性质 |
| --- | --- | --- |
| v0.1.0 | 2026-06-22 | 非官方指南，不代表 OpenAI 官方文档或产品承诺 |

> 本文以 2026-06-22 可访问的 Codex App、Codex CLI、Codex IDE Extension、Codex Web / Cloud 公开能力和实测界面为参考。Codex 更新很快，安装方式、模型名称、额度、入口位置和命令参数都可能变化；涉及具体功能和价格时，请以 OpenAI 官方文档、Codex 当前版本和你账号实际显示为准。  
> CC Switch、DeepSeek 等第三方工具和模型接入方案仅作为扩展方法记录，不属于 OpenAI 官方功能。

## 阅读入口

- [在线阅读](https://vink567.github.io/codex-orange-book/)
- [下载 PD...

</details>

---
### 3. [Yu9191/wloc](https://github.com/Yu9191/wloc)
⭐ **Stars:** 1352
> 📝 修改 Apple 网络定位（gs-loc）返回坐标 · 支持 Surge / Quantumult X / Loon / Stash · 快捷指令一键设置/恢复定位

<details>
<summary><strong>🤖 AI Summary:</strong> &lt;p align='center'&gt;
  &lt;img src='wloc.jpg' width='144' /&gt;
&lt;/p&gt;

# Apple WLOC 定位修改

修改 Apple ...</summary>

<p align="center">
  <img src="wloc.jpg" width="144" />
</p>

# Apple WLOC 定位修改

修改 Apple 网络定位服务 (WiFi/基站) 返回的坐标，实现 iOS 网络定位虚拟定位。打开在线选点页面选位置即可生效，无需手动填经纬度。

---

## 订阅地址

**Surge:**
https://raw.githubusercontent.com/Yu9191/wloc/refs/heads/main/modules/wloc.sgmodule

**Quantumult X:**
https://raw.githubusercontent.com/Yu9191/wloc/refs/heads/main/modules/wloc.conf

**Loon:**
https://raw.githubusercontent.com/Yu9191/wloc/refs/heads/main/modules/wloc.lpx

**Stash:**
https://raw.githubusercontent.com/...

</details>

---
### 4. [winsznx/theeleven](https://github.com/winsznx/theeleven)
⭐ **Stars:** 712
> 📝 Eleven autonomous AI agents open live football prop markets on X Layer — custom Uniswap v4 hook, gasless USDT0 staking.

<details>
<summary><strong>🤖 AI Summary:</strong> # The Eleven

&gt; Live football prop markets, made by AI agents. Built for the 2026
&gt; tourna...</summary>

# The Eleven

> Live football prop markets, made by AI agents. Built for the 2026
> tournament on X Layer.

[![X Cup](https://img.shields.io/badge/X_Cup-OKX_×_X_Layer-ec652b?style=flat-square)](https://www.okx.com/xlayer)
[![Live](https://img.shields.io/badge/status-LIVE_on_X_Layer-44b48b?style=flat-square)](https://regista11.xyz/status)

[![X Layer](https://img.shields.io/badge/chain-X_Layer_196-111a4a?style=flat-square)](https://www.oklink.com/x-layer)
[![USDT0](https://img.shields.io/badge/se...

</details>

---
### 5. [Krishnagangwal/CS-Fundamentals](https://github.com/Krishnagangwal/CS-Fundamentals)
⭐ **Stars:** 707
> 📝 Curated CS fundamentals for placement prep: DSA,Computer Networks, DBMS & SQL, OOPs, Operating Systems, System Design & Software Engineering

<details>
<summary><strong>🤖 AI Summary:</strong> This GitHub repository serves as a comprehensive compilation of Computer Science fundament...</summary>

This GitHub repository serves as a comprehensive compilation of Computer Science fundamentals, specifically tailored for placement preparation. The project's primary objective is to consolidate essential learning materials across major CS domains into a readily accessible format. It aims to equip individuals with the necessary knowledge base and practice resources to excel in technical interviews and aptitude tests required for entry-level positions.

The implementation relies on a well-organized folder structure, categorizing resources by core CS subjects such as Computer Networks, DBMS & SQL, Data Structures & Algorithms (DSA), Object-Oriented Programming (OOPs), Operating Systems, Software Engineering, and System Design. Within these categories, a variety of file formats are utilized, including PDF documents for notes, cheatsheets, and interview question banks, as well as Markdown files for roadmaps and learning guides. This diverse format selection caters to different learning preferences and accessibility needs.

Key technical features include the provision of detailed notes, concise cheatsheets for quick review, and extensive interview question banks for both technical and HR aspects. The DSA section notably includes solutions to popular problem sets like the Striver SDE Sheet, and OOPs resources are presented with language-specific examples (Java, Python, JavaScript, C++). The inclusion of system design materials, SQL tutorials, and general interview preparation prompts further enhances its utility for holistic placement readiness.

</details>

---
## 📚 Latest Paper (ArXiv AI/CV Papers)
> Latest AI and Computer Vision Papers

### 1. [DexCompose: Reusing Dexterous Policies for Multi-Task Manipulation with a Single Hand](https://arxiv.org/abs/2606.28323v1)
👤 **Authors:** Dihong Huang, Zhenyu Wei, Zhuxiu Xu
<details>
<summary><strong>📄 Paper Summary:</strong> Here's an analysis of the provided article, focusing on technical insights and practical e...</summary>

Here's an analysis of the provided article, focusing on technical insights and practical experience:

**Background**
The core challenge addressed is the difficulty in composing individual dexterous manipulation skills into a single, multi-task policy for robotic hands. Existing methods struggle because adding new tasks often creates conflicts, where the actions required for a new task interfere with the state maintained by a previously learned skill, leading to task failure. This research proposes DexCompose, a framework designed to overcome this interference by explicitly assigning roles and action ownership to individual fingers.

**Technical Implementation**
DexCompose employs a role-aware residual composition approach. It begins by identifying critical fingers for maintaining an existing skill's outcome through release tests on successful post-task states. Based on this, it trains two distinct residual modules. A "bounded residual stabilizer" is responsible for preserving the state of the initial skill. Concurrently, a "context-aware residual" module adapts a frozen downstream policy, but crucially, only within the action subspace designated for the new task. This separation of concerns allows for the integration of new skills without disrupting established ones.

**Application Scenarios**
The framework's efficacy is demonstrated through extensive evaluation on 16 composite dexterous manipulation tasks. These tasks involve combinations of four object-retention skills and four distinct downstream interactions. The reported 77.4% average composite success rate indicates DexCompose's capability to effectively combine skills in practical scenarios, suggesting potential for more complex robotic manipulation in areas like assembly, grasping diverse objects, and intricate object manipulation.

**Summary**
DexCompose presents a novel and effective solution for composing pre-trained dexterous manipulation policies. By introducing explicit finger-level action ownership and employing dual residual modules for task preservation and context-aware adaptation, the framework successfully mitigates interference between overlapping skills. This approach offers a promising direction for building more versatile robotic manipulation capabilities, moving beyond simple policy chaining towards more robust and integrated multi-task performance.

</details>

---
### 2. [PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception](https://arxiv.org/abs/2606.28322v1)
👤 **Authors:** Yana Wei, Hongbo Peng, Yanlin Lai
<details>
<summary><strong>📄 Paper Summary:</strong> We introduce PerceptionRubrics, a rubric-based evaluation framework that addresses the gap...</summary>

We introduce PerceptionRubrics, a rubric-based evaluation framework that addresses the gap between saturated benchmark scores and real-world brittleness. Shifting evaluation from holistic semantic matching to rigorous atomic auditing, PerceptionRubrics pairs 1,038 information-dense images with over 12,000 instance-specific rubrics. These criteria are derived from golden captions constructed via a novel Circular Peer-Review consensus pipeline and then distilled into a dual-stream system of Must-Right (essential facts) and Easy-Wrong (fine-grained details) rubrics. Crucially, PerceptionRubrics implements a Gated Scoring mechanism: unlike linear averages, failure on mandatory visual facts triggers sharp binary penalties. Extensive evaluation yields critical insights: (1) The Reliability Gap: models often verify fragmented elements correctly yet fail strict conjunctive constraints, exposing brittleness in dense domains; (2) Open-Closed Stratification: contrary to reasoning trends, we reveal a persistent 8% perception deficit between open-source and proprietary frontiers; and (3) Human-Aligned Rigor: our gated metrics substantially out-align conventional benchmarks, validating that strict perceptual fidelity is the prerequisite for reliable generation.

</details>

---
### 3. [StructSplat: Generalizable 3D Gaussian Splatting from Uncalibrated Sparse Views](https://arxiv.org/abs/2606.28321v1)
👤 **Authors:** Jia-Chen Zhao, Beiqi Chen, Xinyang Chen
<details>
<summary><strong>📄 Paper Summary:</strong> We present StructSplat, a feed-forward and generalizable 3D Gaussian reconstruction framew...</summary>

We present StructSplat, a feed-forward and generalizable 3D Gaussian reconstruction framework that operates directly on uncalibrated images without requiring camera parameters. Existing methods either rely on per-scene optimization or assume known camera poses, and often entangle geometry and appearance within a unified backbone, limiting reconstruction fidelity and generalization. Our key idea is to adopt a structured representation that organizes geometry, semantic, and texture cues with explicit roles in the reconstruction process. Specifically, we introduce a pixel-aligned feature injection mechanism to enable accurate texture modeling from 2D observations, incorporate semantic-aware priors to improve global consistency, and design a camera alignment strategy to prevent information leakage and improve generalization. Experiments show that our method significantly outperforms prior approaches on challenging benchmarks. On DL3DV, our method achieves 28.045 PSNR, surpassing AnySplat (22.377) by +5.67 dB. In cross-dataset evaluation, our method achieves +1.94 dB over AnySplat on ACID and +1.72 dB on RealEstate10K. Project page: https://structsplat.github.io Code: https://github.com/J-C-Zhao/StructSplat

</details>

---
### 4. [SC3-Eval: Evaluating Robot Foundation Models via Self-Consistent Video Generation](https://arxiv.org/abs/2606.18610v3)
👤 **Authors:** Wei-Cheng Tseng, Gashon Hussein, Yuzhu Dong
<details>
<summary><strong>📄 Paper Summary:</strong> This analysis focuses on SC3-Eval, a novel approach for evaluating robot manipulation poli...</summary>

This analysis focuses on SC3-Eval, a novel approach for evaluating robot manipulation policies using action-conditioned video world models. The core challenge addressed is the cost and scalability limitations of real-world robot evaluation. SC3-Eval proposes a method to leverage video generation for policy simulation, aiming to overcome common issues like compounding errors, multi-view consistency, and generalization to unseen behaviors.

The technical implementation of SC3-Eval is built upon a self-consistent video generation recipe that adapts a pre-trained video foundation model. It enforces three key forms of consistency: forward-inverse dynamics consistency, which jointly trains the model to predict future frames from actions and to infer actions from observed frames, thereby grounding simulations in physical plausibility and mitigating drift. Cross-view consistency ensures that different camera perspectives remain coherent during long rollouts by training the model to inpaint views from each other, eliminating the need for explicit memory. Finally, test-time consistency utilizes the inverse dynamics model at inference to generate a per-action-chunk uncertainty signal, enabling the termination of rollouts when generated frames deviate significantly from intended actions.

SC3-Eval demonstrates its utility in application scenarios involving seven real-world vision-language-action policies. By reproducing real-world failure modes, it facilitates fine-grained diagnostic comparisons rather than just aggregate performance rankings. The method achieves a strong closed-loop Pearson correlation of $0.929$ and an MMRV of $0.119$, significantly outperforming existing video-model-based baselines and showing generalization capabilities to new tasks. This suggests SC3-Eval is a promising tool for scalable and insightful robot policy evaluation.

</details>

---
### 5. [SRMA-Mamba: Spatial Reverse Mamba Attention Network for Pathological Liver Segmentation in MRI Volumes](https://arxiv.org/abs/2508.12410v3)
👤 **Authors:** Jun Zeng, Quoc-Huy Trinh, Deepak Ranjan Nayak
<details>
<summary><strong>📄 Paper Summary:</strong> **Background**

The article addresses the critical challenge of accurately segmenting path...</summary>

**Background**

The article addresses the critical challenge of accurately segmenting pathological liver structures in volumetric MRI data, particularly in the context of liver cirrhosis. Current methods often fail to fully leverage the rich spatial anatomical information present in these datasets, leading to limitations in clinical effectiveness and interpretability. This deficiency hinders early detection and timely intervention, which are crucial for improving patient prognosis in chronic liver disease.

**Technical Implementation**

The proposed solution, SRMA-Mamba, is a novel Mamba-based network designed to effectively model complex spatial relationships within liver MRI volumes. A key component is the Spatial Anatomy-Based Mamba module (SABMamba), which selectively applies Mamba scans within pathological regions and fuses anatomical context from sagittal, coronal, and axial planes. This creates a comprehensive global spatial representation crucial for efficient volumetric segmentation. Additionally, the Spatial Reverse Mamba Attention (SRMA) module is introduced to progressively refine segmentation boundaries by integrating coarse segmentation maps with hierarchical encoding features.

**Application Scenarios**

SRMA-Mamba's primary application is in the precise 3D segmentation of pathological liver structures from volumetric MRI. This capability is directly relevant to clinical scenarios involving the diagnosis and monitoring of liver cirrhosis and other chronic liver diseases. By improving the accuracy and detail of segmentation, the method can support more informed clinical decision-making, potentially leading to earlier and more targeted interventions.

**Summary**

SRMA-Mamba presents a significant advancement in volumetric pathological liver segmentation by effectively integrating spatial anatomical context through its SABMamba and SRMA modules. The network's ability to model complex relationships and refine segmentation details surpasses existing state-of-the-art methods, offering enhanced clinical utility for early disease detection and management in liver conditions.

</details>

---