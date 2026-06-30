# 🌐 Global Tech Intelligence Briefing - 2026-06-30
**日期:** 2026-06-30
**生成时间:** 10:46
**数据源:** Hacker News, GitHub Trending, ArXiv

---

## 📰 Hacker News (Top Stories)
### 1. [Building a custom octocopter from scratch with no prior hardware experience](https://karolina.mgdubiel.com/drone/)
🔥 28 | 🕒 2026-06-28 04:17
---
### 2. [Open Source Low Tech](https://opensourcelowtech.org/)
🔥 270 | 🕒 2026-06-26 06:35
<details>
<summary><strong>📖 摘要:</strong> Open Source Low Tech $30 Wind Turbine Solar Cooker Rocket Mass Heater Solar Hot Water Pane...</summary>

Open Source Low Tech $30 Wind Turbine Solar Cooker Rocket Mass Heater Solar Hot Water Panel Wifi Dish ❮ ❯ My name is Daniel Connell. I prototype and develop basic technologies which anyone can make using recycled materials and simple tools. The aim is for everyone everywhere to be able to build and maintain their own infrastructure; producing their own energy, food, clean water, communications, and anything else they need. All designs are open source and license free for any purpose, and full co...

</details>

---
### 3. [Qwen 3.6 27B is the sweet spot for local development](https://quesma.com/blog/qwen-36-is-awesome/)
🔥 942 | 🕒 2026-06-29 17:05
<details>
<summary><strong>📖 摘要:</strong> **背景**

文章评测了 Qwen 3.6 27B 模型，认为其在本地开发场景下表现出色，是首个具备通用智能潜力的本地模型。作者对比了 Qwen 3.6 35B A3B（混合专家...</summary>

**背景**

文章评测了 Qwen 3.6 27B 模型，认为其在本地开发场景下表现出色，是首个具备通用智能潜力的本地模型。作者对比了 Qwen 3.6 35B A3B（混合专家模型，速度更快）和 Qwen 3.6 27B（密集模型，速度稍慢但能力更强），并重点推荐后者。文章指出，尽管运行该模型会显著增加硬件负载（“让电脑发热”），但其性能表现是值得的。

**技术实现**

文章详细介绍了使用 `llama.cpp` 在本地运行 Qwen 3.6 27B 的方法。核心步骤包括：从 Hugging Face 下载经过量化的模型（如 `unsloth/Qwen3.6-27B-MTP-GGUF:Q8_0`），其中 8 位量化能有效减小模型体积并保持较高质量。通过 `llama-server` 命令启动模型服务，并配置了关键参数，如使用 GPU 加速 (`-ngl 999`)、启用 Flash Attention (`-fa on`)、设置大上下文窗口 (`-c 65536`) 以及指定端口 (`--port 8080`)。此外，还提供了将此本地模型集成到 OpenCode 等开发工具的配置示例。

**应用场景**

Qwen 3.6 27B 在多种场景下展现了实用性。在创意生成方面，它能够进行有逻辑的诗歌创作（如关于 Zouk 舞和量子物理的诗），并能根据复杂需求生成代码（如使用 pnpm 创建六边形扫雷游戏），且代码质量较高。更重要的是，它在处理实际工作任务时也表现出不错的效率和响应速度，能够根据简短提示完成相对实用的任务，这标志着其已具备一定的生产力。

**总结**

Qwen 3.6 27B 模型凭借其在本地运行的优异性能和强大的通用智能潜力，成为当前本地开发的一个理想选择。通过 `llama.cpp` 等工具，用户可以相对便捷地部署和使用该模型，享受其在创意生成和实际任务处理方面的能力。尽管对硬件有一定要求，但其“超重”的表现使其成为值得投入的解决方案。

</details>

---
### 4. [Antares Achieves Criticality of Mark-0 Reactor](https://antaresindustries.com/updates/antares-achieves-criticality)
🔥 12 | 🕒 2026-06-30 09:15
<details>
<summary><strong>📖 摘要:</strong> Antares Team PRESS Updates Careers Back Antares Achieves Criticality of Mark-0 Reactor Ant...</summary>

Antares Team PRESS Updates Careers Back Antares Achieves Criticality of Mark-0 Reactor Antares Achieves Criticality of Mark-0 Reactor Antares Achieves Criticality of Mark-0 Reactor Jun 4, 2026 Landmark DOE--INL--Antares collaboration ushers in new era for American Nuclear power IDAHO FALLS, Idaho--Antares today announced that its Mark-0 microreactor achieved initial criticality at Idaho National Laboratory (INL) under U.S. Department of Energy (DOE) authorization — making Antares the first priva...

</details>

---
### 5. [.self: A new top-level domain designed to support self-hosting](https://hccf.onmy.cloud/2026/06/21/reclaiming-our-digital-selves-hccfs-vision-for-a-human-centered-top-level-domain/)
🔥 527 | 🕒 2026-06-29 19:49
<details>
<summary><strong>📖 摘要:</strong> Reclaiming Our Digital Selves: HCCF’s Vision for a Human-Centered Top-Level Domain – Human...</summary>

Reclaiming Our Digital Selves: HCCF’s Vision for a Human-Centered Top-Level Domain – Human-Centered Computing Foundation Skip to content The Internet is the most powerful communication tool ever created, yet the infrastructure underpinning it has been leveraged by the tech industry to extract our data and exploit our attention. The Human-Centered Computing Foundation seeks to change this dynamic by creating an alternative architecture for the web. As an approved participant in ICANN’s Applicant ...

</details>

---
## 🚀 GitHub Trending
> 过去 24 小时高星增长项目

### 1. [simplex-chat/simplex-chat](https://github.com/simplex-chat/simplex-chat)
⭐ **Stars:** 17186
> 📝 SimpleX - the first messaging network operating without user identifiers of any kind - 100% private by design! iOS, Android and desktop apps 📱!

<details>
<summary><strong>🤖 智能解析:</strong> [![build](https://github.com/simplex-chat/simplex-chat/actions/workflows/build.yml/badge.s...</summary>

[![build](https://github.com/simplex-chat/simplex-chat/actions/workflows/build.yml/badge.svg?branch=stable)](https://github.com/simplex-chat/simplex-chat/actions/workflows/build.yml)
[![GitHub downloads](https://img.shields.io/github/downloads/simplex-chat/simplex-chat/total)](https://github.com/simplex-chat/simplex-chat/releases)
[![GitHub release](https://img.shields.io/github/v/release/simplex-chat/simplex-chat)](https://github.com/simplex-chat/simplex-chat/releases)
[![Join on Reddit](https:...

</details>

---
### 2. [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)
⭐ **Stars:** 119814
> 📝 A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

<details>
<summary><strong>🤖 智能解析:</strong> # 🎭 The Agency: AI Specialists Ready to Transform Your Workflow

&gt; **A complete AI agency ...</summary>

# 🎭 The Agency: AI Specialists Ready to Transform Your Workflow

> **A complete AI agency at your fingertips** - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

[![GitHub stars](https://img.shields.io/github/stars/msitarzewski/agency-agents?style=social)](https://github.com/msitarzewski/agency-agents)
[![License: MIT](https://img.shields.io/badge/License-MIT-yell...

</details>

---
### 3. [cupy/cupy](https://github.com/cupy/cupy)
⭐ **Stars:** 11957
> 📝 NumPy & SciPy for GPU

<details>
<summary><strong>🤖 智能解析:</strong> &lt;div align='center'&gt;&lt;img src='https://raw.githubusercontent.com/cupy/cupy/main/docs/image/...</summary>

<div align="center"><img src="https://raw.githubusercontent.com/cupy/cupy/main/docs/image/cupy_logo_1000px.png" width="400"/></div>

# CuPy : NumPy & SciPy for GPU

[![pypi](https://img.shields.io/pypi/v/cupy)](https://pypi.python.org/pypi/cupy)
[![Conda](https://img.shields.io/badge/conda--forge-cupy-blue)](https://anaconda.org/conda-forge/cupy)
[![GitHub license](https://img.shields.io/github/license/cupy/cupy)](https://github.com/cupy/cupy)
[![Matrix](https://img.shields.io/matrix/cupy_commun...

</details>

---
### 4. [altic-dev/FluidVoice](https://github.com/altic-dev/FluidVoice)
⭐ **Stars:** 4664
> 📝 FluidVoice - Fastest macOS Offline Dictation app - Voice to Text fully Local. One ⭐ takes us a long way :))

<details>
<summary><strong>🤖 智能解析:</strong> FluidVoice 是一款专为 macOS 设计的开源语音转文本（STT）应用程序，其核心亮点在于强大的本地 AI 增强功能。该项目旨在提供一种高效、私密的语音输入解决方案，用户...</summary>

FluidVoice 是一款专为 macOS 设计的开源语音转文本（STT）应用程序，其核心亮点在于强大的本地 AI 增强功能。该项目旨在提供一种高效、私密的语音输入解决方案，用户无需依赖云服务即可实现高质量的语音转写和指令控制。

该项目通过集成多种先进的语音识别模型（如 Nemotron Speech 3.5、Parakeet 等）来处理原始语音输入，并提供极低的延迟，确保用户 speaking and seeing words on screen 的体验流畅。其关键创新点在于“Fluid Intelligence”模块，这是一个完全在设备本地运行的 AI 运行时。它负责对语音识别结果进行智能后处理，包括自动格式化、上下文感知的首字母大写以及其他文本优化，从而显著提升了文本的准确性和可用性。

FluidVoice 的技术特点在于其对本地化 AI 的深度集成。与许多依赖云 API 的同类应用不同，FluidVoice 强调数据的隐私性，所有 AI 处理都在用户 Mac 本地完成，不涉及任何数据上传。此外，该应用还提供了“Command Mode”，允许用户通过语音执行 Mac 上的各种操作，如启动应用、运行快捷指令等，进一步拓展了语音交互的边界。这种本地化、高性能的语音处理能力，结合其开源的特性，使其成为注重隐私和效率的 macOS 用户的一个有吸引力的选择。

</details>

---
### 5. [soxoj/maigret](https://github.com/soxoj/maigret)
⭐ **Stars:** 34677
> 📝 🕵️‍♂️ Collect a dossier on a person by username from 3000+ sites

<details>
<summary><strong>🤖 智能解析:</strong> ## Maigret 项目分析

Maigret 是一个强大的开源工具，其核心功能是通过单个用户名在海量网站上搜集目标人物的公开信息。该项目旨在自动化信息收集过程，无需任何API密...</summary>

## Maigret 项目分析

Maigret 是一个强大的开源工具，其核心功能是通过单个用户名在海量网站上搜集目标人物的公开信息。该项目旨在自动化信息收集过程，无需任何API密钥，即可构建一个关于目标用户的数字画像。它能够检测用户在不同平台上的账户存在情况，并提取与之相关的公开数据，例如个人资料信息、其他社交媒体链接等，从而实现对目标用户数字足迹的全面梳理。

该工具的实现方法主要依赖于对目标网站的爬取和解析。Maigret 维护了一个庞大的网站列表（超过3000个），并能够识别和访问这些网站。在默认情况下，它会优先检查流量排名靠前的500个网站，但用户可以通过参数指定扫描所有网站或按类别/国家进行筛选。其独特之处在于，它不仅能发现账户，还能通过提取的用户名和其他标识符进行递归搜索，进一步扩展信息收集的范围，并具备一定的绕过网站反爬虫机制（如封锁、审查和验证码）的能力。

Maigret 的技术亮点在于其广泛的网站覆盖范围、无需API密钥的便利性以及强大的递归搜索能力。它还支持作为Python库嵌入到其他项目中，提供了灵活的二次开发接口。此外，项目还提及了AI分析的潜在应用（尽管具体实现细节未在Readme中详述），预示着未来可能集成更高级的数据分析和洞察能力。该项目对Python 3.10+版本有要求，并提供了多种安装和使用方式，包括命令行工具、Telegram机器人以及潜在的Web界面。

</details>

---
## ✨ GitHub (New & Shiny)
### 1. [deepseek-ai/DeepSpec](https://github.com/deepseek-ai/DeepSpec)
⭐ **Stars:** 4678
> 📝 DeepSpec: a full-stack codebase for training and evaluating speculative decoding algorithms

<details>
<summary><strong>🤖 智能解析:</strong> DeepSpec 是一个用于训练和评估用于推测性解码（speculative decoding）的草稿模型（draft models）的全栈代码库。其核心目标是构建一个高效的系统，...</summary>

DeepSpec 是一个用于训练和评估用于推测性解码（speculative decoding）的草稿模型（draft models）的全栈代码库。其核心目标是构建一个高效的系统，通过训练一个较小的草稿模型来加速大型目标模型的推理过程。该项目提供了完整的数据准备、模型训练和评估流程，旨在为研究和应用推测性解码技术提供一个便捷的平台。

该项目通过一个清晰的三阶段工作流实现其功能。首先是“数据准备”，该阶段负责下载原始提示（prompts），利用目标模型重新生成答案，并构建一个目标模型输出的缓存。这一步至关重要，因为它为后续的草稿模型训练提供了高质量的监督信号。其次是“训练”阶段，利用预先准备好的目标模型输出缓存来训练草稿模型。最后是“评估”阶段，通过在多个基准任务上衡量草稿模型在推测性解码过程中的接受率来评估其性能。

在技术实现上，DeepSpec 支持多种推测性解码算法，包括 DSpark、DFlash 和 Eagle3。它提供了详细的配置选项，允许用户指定目标模型、草稿模型算法以及训练和评估的参数。项目强调了硬件配置的重要性，默认配置适用于多 GPU 环境，并提供了相应的调整指南。此外，DeepSpec 还提供了预训练的检查点，方便用户直接使用或作为进一步微调的基础，同时也鼓励用户根据特定领域的需求对草稿模型进行微调以获得最佳性能。

</details>

---
### 2. [Yu9191/wloc](https://github.com/Yu9191/wloc)
⭐ **Stars:** 1757
> 📝 修改 Apple 网络定位（gs-loc）返回坐标 · 支持 Surge / Quantumult X / Loon / Stash · 快捷指令一键设置/恢复定位

<details>
<summary><strong>🤖 智能解析:</strong> ## 项目分析：Apple WLOC 定位修改

本项目旨在实现 iOS 设备上的网络定位（WiFi/基站）虚拟化，允许用户修改 Apple 的网络定位服务返回的坐标，从而达到虚拟...</summary>

## 项目分析：Apple WLOC 定位修改

本项目旨在实现 iOS 设备上的网络定位（WiFi/基站）虚拟化，允许用户修改 Apple 的网络定位服务返回的坐标，从而达到虚拟定位的目的。其核心功能是通过代理工具拦截并修改系统发起的网络定位请求，将用户设定的虚拟坐标注入到响应中，从而欺骗应用程序获取错误的地理位置信息。

该项目通过代理模块（如 Surge, Quantumult X, Loon, Stash 等）实现，主要工作原理是拦截对 `gs-loc.apple.com` 域名的请求。当设备触发网络定位时，代理模块会拦截对 `/clls/wloc` 接口的响应，解析其中包含的定位信息（通常为 Protobuf 格式），并用用户设定的虚拟坐标替换原始坐标。同时，一个配套的在线选点页面（通过 Cloudflare Workers/Pages 提供）允许用户通过地图交互直观地选择目标位置，并将其保存到设备的持久化存储中，供代理模块读取。

技术特点方面，该项目支持多种地图应用（Apple Maps, 高德地图等）的链接解析，并能处理不同坐标系（如 GCJ-02 和 WGS84）的转换，特别是针对中国大陆地区。它还提供了快捷指令，简化了虚拟定位的设置和恢复流程，无需频繁打开选点页面。值得注意的是，针对较新版本的 iOS（26 及以上），由于系统加强了定位缓存机制，可能需要重启设备才能使修改生效，项目也提供了相应的操作指南。此外，项目开源了 Worker 源码，用户可以自行部署以规避公共服务的使用限制或增强隐私性。

</details>

---
### 3. [Krishnagangwal/CS-Fundamentals](https://github.com/Krishnagangwal/CS-Fundamentals)
⭐ **Stars:** 1076
> 📝 Curated CS fundamentals for placement prep: DSA,Computer Networks, DBMS & SQL, OOPs, Operating Systems, System Design & Software Engineering

<details>
<summary><strong>🤖 智能解析:</strong> # CS Fundamentals

A curated collection of Computer Science fundamentals for placement pre...</summary>

# CS Fundamentals

A curated collection of Computer Science fundamentals for placement preparation, covering all major CS subjects. Includes PDFs, notes, cheatsheets, and interview question banks.

## 📁 Folder Structure

```
CS-Fundamentals/
├── 📁 Computer-Network/          (3 files)
├── 📁 DBMS-and-SQL/              (9 files)
├── 📁 DSA/                       (6 files)
├── 📁 OOPs/                      (5 files)
├── 📁 Operating-System/          (5 files)
├── 📁 Software-Engineering/      (2 files)
...

</details>

---
### 4. [baairon/torlink](https://github.com/baairon/torlink)
⭐ **Stars:** 917
> 📝 A sleek, zero-setup torrent finder and downloader that lives right in your terminal.

<details>
<summary><strong>🤖 智能解析:</strong> ## torlink 项目分析

**项目用途与定位：**

torlink 是一款旨在解决用户在终端环境中寻找和下载 BT 种子文件的痛点。它提供了一个无需配置、即开即用的命令行...</summary>

## torlink 项目分析

**项目用途与定位：**

torlink 是一款旨在解决用户在终端环境中寻找和下载 BT 种子文件的痛点。它提供了一个无需配置、即开即用的命令行工具，能够聚合多个信誉良好的种子源，并直接将选定的文件下载到本地。其核心价值在于简化了传统 BT 资源搜索的繁琐流程，避免了虚假下载链接、弹窗干扰以及资源死链等问题，为技术用户提供了一个高效、干净的种子获取途径。

**实现方法与技术特点：**

torlink 的实现基于 Node.js，用户只需安装 Node.js 环境，即可通过 `npx torlnk` 命令快速启动。项目通过一个精心挑选的、可信赖的种子源列表（包括游戏、电影、电视、动漫等类别）进行搜索。搜索结果会实时聚合展示，并包含文件大小和分享人数等关键信息，方便用户判断下载速度。用户可以通过简单的键盘操作进行搜索、选择和下载，整个交互过程设计得直观易懂。

**核心技术亮点与优势：**

该项目最大的技术亮点在于其“零配置”和“终端原生”的体验。它将复杂的种子搜索和下载管理集成到简洁的终端界面中，极大地提升了效率。下载过程在后台进行，允许用户同时进行其他搜索操作，并且支持断点续传。项目还强调了隐私保护，所有通信直接面向 BT 网络，不经过中心服务器。下载完成后，文件默认会继续进行种子分享（seeding），以支持社区生态，但用户也拥有完全的控制权，可以随时暂停或停止分享。

</details>

---
### 5. [winsznx/theeleven](https://github.com/winsznx/theeleven)
⭐ **Stars:** 716
> 📝 Eleven autonomous AI agents open live football prop markets on X Layer — custom Uniswap v4 hook, gasless USDT0 staking.

<details>
<summary><strong>🤖 智能解析:</strong> # The Eleven

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
## 📚 Latest Paper (ArXiv AI/CV Papers)
> 最新人工智能与计算机视觉论文

### 1. [Open-Vocabulary and Referring Segmentation for 3D Gaussians Using 2D Detectors](https://arxiv.org/abs/2606.30638v1)
👤 **Authors:** Jameel Hassan, Yasiru Ranasinghe, Vishal Patel
<details>
<summary><strong>📄 论文摘要:</strong> 3D Gaussian Splatting (3DGS) has emerged at the forefront of 3D scene reconstruction. Exte...</summary>

3D Gaussian Splatting (3DGS) has emerged at the forefront of 3D scene reconstruction. Extending 3DGS with language-driven, open-vocabulary understanding has gained significant attention for real-world applications such as embodied AI. Recent methods achieve this by learning an instance feature attribute and assigning semantics by distilling high-dimensional Contrastive Language-Image Pretraining (CLIP) features directly into the scene representation. However, the instance grouping mechanisms of these methods either require a predefined number of instances or suffer from noise in their bottom-up grouping strategies. Furthermore, the reliance on CLIP restricts semantic understanding to simple noun phrases, preventing complex spatial reasoning and referential expression grounding. We present GaussDet, a method that circumvents the need for dense CLIP features by leveraging discrete, open-vocabulary 2D object detectors with referring expression capabilities. We learn instance features for individual Gaussians to decompose the scene into 3D instance groups. By rendering these groups and aggregating semantic votes from multi-view 2D detections, we generate a robust View-Aggregated Semantic Label Distribution (VASD) for each 3D instance. This view-aggregation strategy acts as a strong regularizer, attenuating spurious labels caused by low-quality instance grouping. Our approach enables a straightforward, zero-shot extension from simple language queries to complex referential grounding. Extensive evaluations across two key tasks -- open-vocabulary segmentation (LeRF-OVS, ScanNet) and referring expression grounding (Ref-LeRF) -- demonstrate that GaussDet achieves consistent improvements over existing methods. Most notably, we achieve a substantial 16.7% mIoU improvement in referential grounding within a strict zero-shot setting.

</details>

---
### 2. [GROW$^2$: Grounding Which and Where for Robot Tool Use](https://arxiv.org/abs/2606.30632v1)
👤 **Authors:** Yuhong Deng, Yuyao Liu, David Hsu
<details>
<summary><strong>📄 论文摘要:</strong> **技术分析：GROW$^2$ - 开放世界下的机器人工具使用与能力泛化**

**背景**
机器人若想在复杂多变的开放世界环境中执行任务，其核心能力之一在于灵活运用工具。然而，现...</summary>

**技术分析：GROW$^2$ - 开放世界下的机器人工具使用与能力泛化**

**背景**
机器人若想在复杂多变的开放世界环境中执行任务，其核心能力之一在于灵活运用工具。然而，现有技术在让机器人超越工具的预设功能，实现创造性工具使用方面仍面临挑战。这主要体现在“开放世界下的能力关联”（open-world affordance grounding）问题上，即机器人需要从开放类别的物体中选择合适的工具，并精确地定位其作用区域。

**技术实现**
为解决上述挑战，研究提出了GROW$^2$（GROunding Which and Where）框架。该框架创新性地将工具使用能力关联过程分解为语义和几何两个层级，并引入了“物体部件”作为自然抽象。在语义层面，GROW$^2$利用视觉语言模型（VLMs）的常识推理能力，解析自然语言指令，从而选择合适的工具，并识别工具与目标物体上的任务相关部件。在几何层面，则借助视觉基础模型，从单目RGB-D图像中将选定的部件精确地映射到三维空间区域。这种分层处理方式有效规避了对海量数据和端到端训练的依赖。

**应用场景与实验验证**
GROW$^2$在多个基准测试中展现出优异性能，其在能力关联预测方面的表现超越了现有最先进的基线方法。更重要的是，该框架实现了对开放类别物体的零样本泛化能力，并在模拟和真实机器人工具使用实验中均取得了领先的成果。这意味着机器人能够学习到如何利用未曾见过的物体作为工具，并在实际操作中成功执行任务，例如文章开头提到的用盘子切蛋糕的设想。

**总结**
GROW$^2$框架通过引入部件作为中间表示，并结合VLM和视觉基础模型的优势，为机器人实现了高效且泛化能力强的开放世界工具使用能力。这一技术突破为机器人执行更复杂、更具创造性的任务奠定了基础，尤其是在缺乏预定义工具或任务场景变化时，其价值尤为突出。

</details>

---
### 3. [Pause and Think: A Dataset and Benchmark for Video-Grounded Assistive Action Suggestion](https://arxiv.org/abs/2606.00616v3)
👤 **Authors:** Shivam Singh, Saptarshi Majumder, Pratik Prabhanjan Brahma
<details>
<summary><strong>📄 论文摘要:</strong> Recent Vision-Language Models (VLMs) struggle with grounded reasoning, temporal consistenc...</summary>

Recent Vision-Language Models (VLMs) struggle with grounded reasoning, temporal consistency, and context aware planning in videos. We introduce pause-and-think-T, a reasoning-centric training dataset that encourages models to pause, reason over visual evidence, and produce concise, actionable responses. The dataset promotes structured reasoning prior to answer generation, guiding models toward human-like, scene-grounded assistance. We fine-tune a compact 4B-parameter model and evaluate it on our pause-and-think-B benchmark targeting contextual understanding and goal planning tasks. The model achieves 58.0% accuracy at 59x fewer parameters than Qwen3-VL-235B (58.9%), matching GPT-5.2 on scene understanding and surpassing GPT-4o. Beyond our benchmark, it also shows strong out-of-distribution performance on EgoThink and TempCompass, with substantial gains in affordance, assistance, attribution recognition, situated reasoning, and temporal order, without benchmark-specific training. Our results indicate that targeted reasoning supervision enables compact models to deliver actionable, visually grounded guidance while generalizing beyond training data, without requiring large-scale model expansion.

</details>

---
### 4. [Reweighting Framewise Attention in Video Transformers for Facial Expression Understanding](https://arxiv.org/abs/2606.30611v1)
👤 **Authors:** Seongro Yoon, Donghyeon Cho, Jinsun Park
<details>
<summary><strong>📄 论文摘要:</strong> Understanding facial expressions in videos requires modeling subtle and localized facial d...</summary>

Understanding facial expressions in videos requires modeling subtle and localized facial dynamics under unconstrained conditions. Although recent Vision Transformer~(ViT)-based video models have shown strong performance through large-scale self-supervised pretraining, their attention mechanisms often emphasize dominant global motions and coarse temporal dynamics, limiting sensitivity to fine-grained facial variations. To address this limitation, we propose MiRA (Marginal-induced Attention Redistribution), a plug-in frame-marginal attention redistribution framework for ViT backbones that enhances spatio-temporal selectivity toward subtle facial dynamics without introducing additional trainable parameters. MiRA derives frame-level confidence and intra-frame concentration statistics from self-attention maps to estimate frame-wise marginal importance and redistribute attention toward spatiotemporally localized facial cues. We first introduce a principled \textit{exact mode} based on post-softmax attention redistribution. To further improve efficiency, we propose \textit{flashLite mode}, a lightweight pre-softmax approximation that integrates frame-marginal redistribution into FlashAttention kernels while preserving the effectiveness of the exact formulation. Experimental results on challenging Facial Expression Recognition~(FER) benchmarks demonstrate consistent improvements over strong ViT baselines.

</details>

---
### 5. [SVCBench: A Streaming Video Counting Benchmark for Spatial-Temporal State Maintenance](https://arxiv.org/abs/2603.12703v3)
👤 **Authors:** Pengyiang Liu, Zhongyue Shi, Hongye Hao
<details>
<summary><strong>📄 论文摘要:</strong> Video understanding requires models to continuously track and update world state during pl...</summary>

Video understanding requires models to continuously track and update world state during playback. Although existing benchmarks have advanced video understanding evaluation across multiple dimensions, they provide limited visibility into how models maintain world state over time. We propose SVCBench, a Streaming Video Counting Benchmark that repositions counting as a minimal, controlled probe for diagnosing models' world-state maintenance capability. We decompose this capability into object counting and event counting, forming 8 fine-grained subcategories. Object counting covers tracking currently visible objects and cumulative unique identities, while event counting covers detecting instantaneous actions and tracking complete activity cycles. SVCBench contains 406 videos with frame-by-frame annotations of 10,071 event occurrences and object state changes, yielding 1,000 streaming QA pairs with 4,576 query points distributed along video timelines. By observing state maintenance trajectories through streaming multi-point queries, we design three complementary metrics to diagnose numerical precision, trajectory consistency, and temporal awareness. Evaluations of mainstream video-language models show that current models still exhibit significant deficiencies in spatial-temporal state maintenance, with especially poor performance on periodic event counting. SVCBench provides a diagnostic framework for measuring and improving state maintenance in video understanding systems. Our code and data are available at https://buaa-colalab.github.io/SVCBench.

</details>

---