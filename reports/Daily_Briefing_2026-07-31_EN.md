# 🌐 Global Tech Intelligence Briefing - 2026-07-31
**Date:** 2026-07-31
**Generated At:** 10:17
**Data Sources:** Hacker News, GitHub Trending, ArXiv

---

## 📰 Hacker News (Top Stories)
### 1. [The session you cannot take with you](https://earendil.com/posts/session-portability/)
🔥 355 | 🕒 2026-07-31 03:47
<details>
<summary><strong>📖 Summary:</strong> The Session You Cannot Take With You | EARENDIL The Session You Cannot Take With You Date:...</summary>

The Session You Cannot Take With You | EARENDIL The Session You Cannot Take With You Date: Thu, 30 Jul 2026 From: Earendil Engineering < rfc@earendil.com > To: You Subject: The Session You Cannot Take With You The original promise of an inference API was wonderfully simple: send some input, receive some output. If you kept both, you had the conversation. You could inspect it, archive it, replay it, or give it to a different model. That abstraction was never completely true. For instance prompt c...

</details>

---
### 2. [JEP 401: Value Objects (Preview) merged to OpenJDK master](https://github.com/openjdk/jdk/pull/31120)
🔥 116 | 🕒 2026-07-31 04:38
<details>
<summary><strong>📖 Summary:</strong> This pull request represents a significant step towards integrating 'Value Objects' into J...</summary>

This pull request represents a significant step towards integrating "Value Objects" into Java, as defined by JEP 401. The implementation is tightly coupled with JEP 539, "Strict Field Initialization in the JVM," indicating a foundational requirement for the value object feature. The work is distributed across the Java language, the JVM, and the standard library, highlighting the comprehensive nature of this enhancement.

The core technical insight is the introduction of value objects, which are intended to be immutable and have their state contained within their identity. This implies a shift towards more efficient data representation and potentially improved performance by reducing object overhead and enabling optimizations like primitive specialization. The dependency on strict field initialization suggests a design that enforces predictable object state from construction.

While the article focuses on the implementation details within the OpenJDK repository, the practical application scenarios for value objects are broad. They are ideal for representing simple data structures, such as coordinates, points, or configuration settings, where immutability and value-based equality are paramount. This can lead to cleaner code, fewer bugs related to mutable state, and enhanced performance in scenarios involving large collections of such objects.

In summary, this pull request marks the initial preview of Java's value objects, a feature that promises to enhance performance and code robustness by introducing a new category of immutable, value-based types. The integration with strict field initialization underscores the focus on predictable and efficient object handling. This development is poised to impact how developers model and manage data in Java applications.

</details>

---
### 3. [Google fixed more Chrome bugs in June than over the past two years, thanks to AI](https://blog.google/security/chrome-stronger-with-every-update/)
🔥 74 | 🕒 2026-07-31 07:29
<details>
<summary><strong>📖 Summary:</strong> Stronger with every update: How we’re making Chrome and the web safer in the AI Era Chrome...</summary>

Stronger with every update: How we’re making Chrome and the web safer in the AI Era Chrome Stronger with every update: How we’re making Chrome and the web safer in the AI Era Jul 30, 2026 | x.com Facebook LinkedIn Mail Copy link How Chrome is using AI to improve vulnerability discovery, triage, and patching. Chrome Security Team Share x.com Facebook LinkedIn Mail Copy link We’re living through a massive shift in the software security industry. Large Language Models (LLMs) are unlocking unprecede...

</details>

---
### 4. [DeepSeek-V4-Flash Update](https://api-docs.deepseek.com/updates/)
🔥 291 | 🕒 2026-07-31 06:08
<details>
<summary><strong>📖 Summary:</strong> Change Log | DeepSeek API Docs Skip to main content On this page Change Log Date: 2026-07-...</summary>

Change Log | DeepSeek API Docs Skip to main content On this page Change Log Date: 2026-07-31 ​ DeepSeek-V4-Flash Update ​ The official release of the DeepSeek-V4-Flash API is now in public beta. The API calling method remains unchanged — simply set the model name to deepseek-v4-flash to use the latest version. Significantly enhanced agent capabilities, with benchmark results far exceeding V4-Pro-Preview: Terminal Bench 2.1: 82.7 NL2Repo: 54.2 Cybergym: 76.7 DeepSWE: 54.4 Toolathlon verified: 70....

</details>

---
### 5. [Show HN: Gander, an Android file viewer that asks for no permissions at all](https://github.com/mokshablr/gander)
🔥 62 | 🕒 2026-07-31 05:45
<details>
<summary><strong>📖 Summary:</strong> GitHub - mokshablr/gander: Take a gander at any file. Offline, zero-permission Android vie...</summary>

GitHub - mokshablr/gander: Take a gander at any file. Offline, zero-permission Android viewer for PDF, Word, Excel, PowerPoint, photos, video, audio, Markdown and code. · GitHub Skip to content You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert mokshablr / gander Public Notifications You must be signed in to ...

</details>

---
## 🚀 GitHub Trending
> Projects with the highest star growth in the past 24 hours

### 1. [huggingface/speech-to-speech](https://github.com/huggingface/speech-to-speech)
⭐ **Stars:** 9504
> 📝 Build local voice agents with open-source models

<details>
<summary><strong>🤖 AI Summary:</strong> This project, 'Speech To Speech,' provides a highly modular and low-latency pipeline for b...</summary>

This project, "Speech To Speech," provides a highly modular and low-latency pipeline for building voice agents. Its core purpose is to enable seamless voice interaction by chaining together four key components: Voice Activity Detection (VAD), Speech-to-Text (STT), a Large Language Model (LLM), and Text-to-Speech (TTS). The system is designed to be flexible, allowing each of these stages to be independently swapped with alternative implementations, facilitating customization and optimization for various use cases.

The implementation is built around a cascade of threaded components connected by queues, ensuring efficient processing. VAD, using Silero VAD, handles speech boundary detection. STT transcribes audio, with support for live partial transcripts. The LLM generates responses, capable of streaming text and tool calls. Finally, TTS synthesizes audio output, which is then streamed back to the client. A significant technical feature is its OpenAI Realtime-compatible WebSocket API, enabling easy integration with existing OpenAI clients or custom applications.

Key technical highlights include the swappable nature of all pipeline components, promoting an open and adaptable architecture. The LLM integration is particularly versatile, supporting OpenAI-compatible protocols. This allows users to connect to hosted LLM providers, Hugging Face Inference Providers, or self-hosted solutions like vLLM or llama.cpp for fully local deployments. The project emphasizes ease of use with a straightforward quickstart guide and clear CLI options for configuring different model backends and API endpoints, making it accessible for both rapid prototyping and production deployment.

</details>

---
### 2. [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners)
⭐ **Stars:** 54791
> 📝 12 Weeks, 24 Lessons, AI for All!

<details>
<summary><strong>🤖 AI Summary:</strong> This repository provides a comprehensive, 12-week curriculum designed to introduce beginne...</summary>

This repository provides a comprehensive, 12-week curriculum designed to introduce beginners to the field of Artificial Intelligence. Its primary objective is to demystify AI concepts through a structured learning path, encompassing 24 practical lessons, integrated quizzes, and hands-on labs. The curriculum aims to equip learners with foundational knowledge, covering essential AI topics and introducing them to widely-used tools and ethical considerations within the domain.

Technically, the project leverages a modular lesson structure, likely organized into distinct files or directories for each week and lesson. The inclusion of TensorFlow and PyTorch as featured tools suggests that the practical components will involve coding exercises and demonstrations using these popular deep learning frameworks. The emphasis on "practical lessons" and "labs" indicates a hands-on approach, encouraging learners to apply theoretical concepts through experimentation and development.

A notable technical feature is the extensive multi-language support, managed automatically via GitHub Actions. This ensures that the curriculum is accessible to a global audience. For developers concerned with repository size, the project offers a solution through sparse checkout, allowing for the cloning of the repository without the large volume of translated content. This demonstrates a thoughtful approach to managing project resources and catering to different user needs.

</details>

---
### 3. [paperswithbacktest/awesome-systematic-trading](https://github.com/paperswithbacktest/awesome-systematic-trading)
⭐ **Stars:** 11422
> 📝 A curated list of awesome libraries, packages, strategies, books, blogs, tutorials for systematic trading.

<details>
<summary><strong>🤖 AI Summary:</strong> &lt;div align='center'&gt;
  &lt;img src='static/images/awesome-systematic-trading.jpeg' height=200...</summary>

<div align="center">
  <img src="static/images/awesome-systematic-trading.jpeg" height=200 alt=""/>
  <h1>Awesome Systematic Trading</h1>
</div>
<div align=center><img src="https://awesome.re/badge.svg" /></div>

[希望阅读中文版？点我](./README_zh.md)

We are collecting a list of resources papers, softwares, books, articles for finding, developing, and running systematic trading (quantitative trading) strategies.

<!-- omit in toc -->
### What will you find here?

- [97 libraries and packages](#libraries-...

</details>

---
### 4. [different-ai/openwork](https://github.com/different-ai/openwork)
⭐ **Stars:** 19081
> 📝 The open-source alternative to Claude Cowork (powered by opencode)

<details>
<summary><strong>🤖 AI Summary:</strong> OpenWork is positioned as an open-source desktop application designed to facilitate the sh...</summary>

OpenWork is positioned as an open-source desktop application designed to facilitate the sharing and utilization of AI workflows across various platforms and agents. Its core purpose is to provide a centralized and interoperable system for managing AI capabilities, acting as an alternative to proprietary solutions. The application aims to enable users to create, share, and reuse AI skills, plugins, and connected services across different AI agents and development environments, fostering collaboration and efficiency.

Technically, OpenWork achieves this interoperability through a modular approach centered around its "MCP" (Modular Capability Provider) concept. Users can integrate an OpenWork MCP into compatible AI agents like Codex, Claude Code, or Cursor. This MCP exposes two primary tools: `search_capabilities` for discovering available AI functions and `execute_capability` for invoking them. The system supports remote MCP connections, with a provided URL (`https://api.openworklabs.com/mcp/agent`) serving as a universal endpoint for various agents. This architecture allows for the seamless integration of OpenWork's managed AI skills and services into existing AI agent workflows without requiring users to operate within the dedicated OpenWork desktop application.

For organizational management, OpenWork introduces "OpenWork Den," a control plane designed for centralized administration. This interface allows for provisioning and managing AI inference at scale, controlling access to model providers, inviting and organizing team members, and enforcing desktop policies. A key feature of Den is its marketplace functionality, enabling the publishing and assignment of skills and plugins to specific users, teams, or the entire organization. It also supports the import of Anthropic-compatible plugins, further expanding the ecosystem of available AI capabilities. The local development setup utilizes `pnpm` and offers flexible configurations for managing multiple development instances and handling credential management, particularly concerning the macOS keychain.

</details>

---
### 5. [WhiskeySockets/Baileys](https://github.com/WhiskeySockets/Baileys)
⭐ **Stars:** 10519
> 📝 Socket-based TS/JavaScript API for WhatsApp Web

<details>
<summary><strong>🤖 AI Summary:</strong> Baileys is a TypeScript library designed for programmatic interaction with WhatsApp's Web ...</summary>

Baileys is a TypeScript library designed for programmatic interaction with WhatsApp's Web API. Its primary purpose is to enable developers to build applications that can send and receive messages, manage contacts, and perform other WhatsApp-related functionalities without direct user intervention through the official WhatsApp client. This is achieved by leveraging a direct WebSocket connection to the WhatsApp Web backend, bypassing the need for browser automation tools like Selenium.

The implementation of Baileys centers around a direct WebSocket protocol. This approach offers significant advantages in terms of resource efficiency, notably reducing RAM consumption compared to browser-based solutions. The library supports interaction with both the multi-device and the traditional web versions of WhatsApp. Its development has been influenced by community efforts and reverse-engineering insights into the WhatsApp Web and Multi-Device protocols, with acknowledgments to prior work in this area.

Key technical features include the ability to connect accounts using QR codes or pairing codes, facilitating session management and restoration. Baileys also supports advanced functionalities such as receiving full message history, caching group metadata for performance, and handling various events emitted by the WhatsApp service. The library is distributed via npm, with options for stable and edge releases, and provides clear import paths for integration into TypeScript projects.

</details>

---
## ✨ GitHub (New & Shiny)
### 1. [MoonshotAI/Kimi-K3](https://github.com/MoonshotAI/Kimi-K3)
⭐ **Stars:** 7635
> 📝 Open Frontier Intelligence

<details>
<summary><strong>🤖 AI Summary:</strong> &lt;div align='center'&gt;
  &lt;picture&gt;
      &lt;img src='assets/kimi-logo.png' width='30%' alt='Ki...</summary>

<div align="center">
  <picture>
      <img src="assets/kimi-logo.png" width="30%" alt="Kimi K3">
  </picture>
</div>
<hr>
<div align="center" style="line-height:1">
  <a href="https://www.kimi.com" target="_blank"><img alt="Chat" src="https://img.shields.io/badge/🤖%20Chat-Kimi%20K3-ff6b6b?color=1783ff&logoColor=white"/></a>
  <a href="https://www.moonshot.ai" target="_blank"><img alt="Homepage" src="https://img.shields.io/badge/Homepage-Moonshot%20AI-white?logo=Kimi&logoColor=white"/></a>
</div...

</details>

---
### 2. [mshumer/Claude-of-Duty](https://github.com/mshumer/Claude-of-Duty)
⭐ **Stars:** 2447
> 📝 A Call of Duty-quality FPS in Three.js, built from a single prompt.

<details>
<summary><strong>🤖 AI Summary:</strong> # Claude of Duty

Get updates [here](https://shumer.dev/newsletter).

A first-person shoot...</summary>

# Claude of Duty

Get updates [here](https://shumer.dev/newsletter).

A first-person shooter built in the browser with Three.js r180 and WebGL2. Roughly
55k lines across 11 subsystems, written by a fleet of AI agents under orchestration.

**There are no art assets.** Every texture, mesh, animation and sound is generated
procedurally at load time from code. No models, no HDRIs, no image files, no audio
files. The only runtime dependency is `three`.

```bash
npm install
npm run dev          # http...

</details>

---
### 3. [VictorTaelin/OptMem](https://github.com/VictorTaelin/OptMem)
⭐ **Stars:** 969
> 📝 Permanent memory for AI agents. A 426-token prompt, a script, plug and play.

<details>
<summary><strong>🤖 AI Summary:</strong> OptMem provides a persistent memory solution for AI agents, designed for seamless integrat...</summary>

OptMem provides a persistent memory solution for AI agents, designed for seamless integration and efficient operation. Its core purpose is to enable AI agents to retain knowledge across sessions, ensuring continuity and preventing loss of context or learned information. This is achieved through a simple installation process and a clear set of commands that manage the memory lifecycle.

The implementation relies on a single Python 3 script with no external dependencies, located at `~/.optmem/memo`. This script manages an append-only log (`LOG.txt`) of individual memories and a hierarchical summary tree (`TREE/`) for faster retrieval. The fixed-width nature of memory records is a key technical feature, allowing for direct seeks and extremely fast lookups, even with a large memory footprint. Configuration options, such as `WAKE_LINES`, control the amount of memory presented to the agent at startup, acting as a reading budget rather than a storage limit.

Key technical features include a "wake" command for initial memory loading, "note" for recording new memories (limited to a single line and 280 bytes), and "recall" for full-text search using regular expressions. The system also supports a hierarchical memory structure, allowing agents to "zoom" into specific summary nodes to explore finer-grained details. A "nap" command handles the merging of memories into summaries, and "forget" allows for the removal of outdated summaries. The design emphasizes immutability of the raw memory log, with the tool managing all updates and reorganizations.

</details>

---
### 4. [xikhar/persona](https://github.com/xikhar/persona)
⭐ **Stars:** 693
> 📝 Bringing real-time voice to life.

<details>
<summary><strong>🤖 AI Summary:</strong> Persona is a desktop application designed to provide a real-time visual representation for...</summary>

Persona is a desktop application designed to provide a real-time visual representation for voice conversations. Its core purpose is to enhance desktop voice experiences by adding an expressive character presence that synchronizes with audio activity. This aims to bring a more engaging and personalized dimension to digital communication, moving beyond purely auditory interactions.

The implementation leverages cross-platform technologies, with specific audio capture mechanisms tailored for each operating system. Linux utilizes PipeWire for process-stream capture, while Windows employs WASAPI for process-loopback capture. macOS relies on Core Audio for process tapping. Crucially, Persona focuses solely on capturing application audio output and does not engage in microphone recording, audio saving, speech generation, transcription, or network audio transmission. This design prioritizes user privacy and limits the scope of its audio processing capabilities.

Technical features include a flexible customization system allowing users to import and manage their own `.vrm` character models and `.vrma` animation files. Persona supports defining custom animation actions, such as "Idle" and "Speaking," which can incorporate multiple animation clips. This allows for dynamic visual responses to user-defined scenarios. Furthermore, Persona exposes a local MCP (Meta Communication Protocol) server, enabling integration with other applications like Codex. This connection allows external agents to control Persona's visibility, trigger animations, and query its status, facilitating more sophisticated interactive experiences. The application also offers robust window management features, adapting to different desktop environments and window managers for optimal display.

</details>

---
### 5. [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer)
⭐ **Stars:** 691
> 📝 (No description)

<details>
<summary><strong>🤖 AI Summary:</strong> This project, 'Decimen Optical Transfer,' presents a novel approach to file transfer betwe...</summary>

This project, "Decimen Optical Transfer," presents a novel approach to file transfer between devices using only a screen and a camera, eliminating the need for network connectivity, pairing, or specific applications. Its core purpose is to demonstrate a minimal proof-of-concept for transmitting files via an animated stream of QR codes displayed on one device and captured by another. This method bypasses traditional communication channels, relying solely on visual data transmission.

The implementation leverages fountain codes, specifically a Luby transform coding approach, to address the inherent challenges of a one-way visual channel. Instead of sending file blocks directly, each QR code frame contains an XOR combination of a pseudorandom subset of file blocks. This subset is deterministically generated based on the frame's sequence number. The receiver can reconstruct the file by collecting a sufficient number of these frames, regardless of their order or any dropped frames, as the fountain code ensures redundancy and error tolerance. Each frame is self-describing, containing essential metadata like session ID, sequence number, and block information, facilitating seamless mid-transfer connection and automatic receiver reset upon sender restart.

Key technical features include the use of WebRTC's `getUserMedia` for camera access and `requestVideoFrameCallback` for efficient frame processing. Decoding is handled by `zxing-cpp` compiled to WebAssembly, running in workers to avoid blocking the main thread. The project highlights several "hard-won details" crucial for robust operation, such as deterministic generation of soliton distributions to ensure bit-identical results across JavaScript engines, precise camera frame rate handling on iOS, and managing the lifecycle of video frame callbacks. The QR error correction is set to the minimum level (L), balancing in-frame error correction with the erasure-correcting capabilities of the fountain code.

</details>

---
## 📚 Latest Paper (ArXiv AI/CV Papers)
> Latest AI and Computer Vision Papers

### 1. [ReToken: One Token to Improve Vision-Language Models for Visual Retrieval](https://arxiv.org/abs/2607.28627v1)
👤 **Authors:** Yao Xiao, Reuben Tan, Zhen Zhu
<details>
<summary><strong>📄 Paper Summary:</strong> **Background**

Vision-language models (VLMs) face significant challenges when processing ...</summary>

**Background**

Vision-language models (VLMs) face significant challenges when processing long visual contexts. Performance degrades notably with an increasing number of distractors, and the computational cost of processing all visual tokens simultaneously becomes prohibitive due to GPU memory limitations. This necessitates efficient methods for selecting relevant information from extensive visual inputs.

**Technical Implementation**

The core innovation presented is ReToken, a novel approach that addresses long visual context processing. ReToken introduces a single, learnable embedding designed as an explicit retrieval target. This embedding intelligently selects a sparse subset of query-relevant visual tokens from a pre-populated visual Key-Value (KV) cache. The training process is remarkably efficient, requiring only a small image-Question Answering (QA) dataset. This lightweight design allows for both training and long-video inference to be performed on a single H100 GPU, highlighting its practical feasibility.

**Application Scenarios**

ReToken demonstrates consistent performance improvements across various vision-language benchmarks. On the Visual Haystacks dataset, it significantly boosts performance for models like Qwen3VL-8B (by 13.4 points) and InternVL3.5 (by 12.4 points), representing substantial relative gains. Furthermore, ReToken exhibits strong zero-shot transfer capabilities for long video tasks, as evidenced by an 8.0-point improvement on LVBench using Qwen3VL-8B. This adaptability to different modalities and tasks underscores its broad applicability.

**Summary**

ReToken offers a computationally efficient and effective solution for enhancing VLM performance on tasks involving long visual contexts. By employing a learnable retrieval embedding to sparsely select relevant visual tokens from a KV cache, it overcomes the limitations of processing full contexts. Its lightweight training and inference requirements, coupled with demonstrated gains on image and video benchmarks, make ReToken a valuable contribution for developing more scalable and performant vision-language systems.

</details>

---
### 2. [ACE-Data-0: Human-Centric Ambient Capture as Embodied Data Engine](https://arxiv.org/abs/2607.28625v1)
👤 **Authors:** Yukang Cao, Haozhe Xie, Beichen Wen
<details>
<summary><strong>📄 Paper Summary:</strong> This article addresses the critical data bottleneck in embodied intelligence, specifically...</summary>

This article addresses the critical data bottleneck in embodied intelligence, specifically the challenge of capturing the complex, synchronized evolution of first-person perception, whole-body motion, dexterous manipulation, object states, sound, and touch as humans pursue goals. Existing datasets often fragment these modalities, hindering the observation of the complete perception-action loop.

The core technical innovation presented is the Ambient Capture Engine (ACE). ACE transforms real home environments into synchronized recording studios by employing two complementary scales: a table-scale setup for detailed hand-object manipulation and a room-scale setup for capturing broader whole-body motion and interactions. This system records a unified multisensory stream, including egocentric and multi-view video, full-body and hand kinematics, object geometry and trajectories, audio, and tactile signals.

The resulting ACE-Data-0 dataset comprises 150 hours of synchronized human demonstrations across 200 task categories, performed by 50 participants in two distinct home environments. This dataset is designed to support research in imitation learning, world models, and vision-language-action systems by providing aligned perceptual, kinematic, and contact supervision. The authors also introduce a hierarchical benchmark to evaluate current state-of-the-art methods, highlighting significant performance gaps in areas such as contact, occlusion, egomotion, and long temporal horizons.

</details>

---
### 3. [PhiZero: A World Model Built Around Physical Language](https://arxiv.org/abs/2607.28624v1)
👤 **Authors:** Shuyao Shang, Yuqi Wang, Ruopeng Gao
<details>
<summary><strong>📄 Paper Summary:</strong> Here's a technical analysis of the provided article on PhiZero:

**Background**

PhiZero a...</summary>

Here's a technical analysis of the provided article on PhiZero:

**Background**

PhiZero addresses a fundamental challenge in physical world modeling: the implicit nature of dynamics in existing pixel-space prediction models. These models often learn to generate future video frames directly, embedding complex physical laws within high-dimensional visual predictors without explicit representation. This makes them less amenable to direct reasoning about world evolution. PhiZero's core innovation lies in introducing "physical language," a compact, discrete representation of world-state transitions. This approach is inspired by human cognitive abilities to abstract predictive structures and articulate them through language, enabling explicit reasoning.

**Technical Implementation**

The model employs a "reason-then-render" paradigm. First, PhiZero learns this physical language from in-the-wild videos via self-supervision. This learned language then serves as an intermediate representation to infer future world evolution as a sequence of discrete physical language tokens. Subsequently, these inferred transitions are rendered back into video frames. This separation of reasoning (predicting state transitions) from rendering (generating visual output) is a key architectural distinction, allowing for more interpretable and controllable physical simulations.

**Application Scenarios**

The experimental validation of PhiZero demonstrates its capability in generating physically coherent world evolution across various benchmarks. Beyond generation, the model shows promise in several advanced applications. These include realistic and interactive world modeling, where explicit reasoning can lead to more predictable and controllable simulations. Furthermore, its ability to support fine-grained action-conditioned simulation suggests potential for robotics and control tasks. The zero-shot motion transfer capability highlights its robustness and generalization, enabling the application of learned dynamics to novel scenarios without explicit retraining.

**Summary**

PhiZero represents a significant advancement in physical world modeling by introducing a discrete "physical language" for explicit reasoning about world-state transitions. This "reason-then-render" approach contrasts with traditional pixel-space predictors, offering improved interpretability and control. Its demonstrated success in generating physically coherent videos and its potential for interactive simulation, action-conditioned generation, and zero-shot motion transfer position it as a promising framework for more sophisticated and generalizable physical world understanding and generation tasks.

</details>

---
### 4. [Chimera: Designing and Chinchilla-Scaling Hybrid Visual Diffusion Transformers](https://arxiv.org/abs/2607.28611v1)
👤 **Authors:** Chongjian Ge, Hanwen Jiang, Tianyu Wang
<details>
<summary><strong>📄 Paper Summary:</strong> **Background**

The increasing demand for high-resolution visual generation, including lon...</summary>

**Background**

The increasing demand for high-resolution visual generation, including long videos and multimodal content, presents a significant computational challenge due to the quadratic complexity of traditional full attention mechanisms. Chimera addresses this by proposing a novel hybrid visual diffusion backbone designed for efficiency and scalability. It unifies text, image, and video processing within a single, raster-ordered stream, eliminating the need for explicit positional embeddings.

**Technical Implementation**

Chimera's architecture is a sophisticated blend of specialized attention mechanisms and convolutional layers. It incorporates Kimi Delta Attention (KDA) for efficient long-context state tracking with linear O(N) complexity. This is complemented by interleaved Multi-head Latent Attention (MLA) layers, which enable direct global interactions. For capturing local spatiotemporal context, modality-aware short convolutions are employed. To further enhance capacity while managing computational cost, Sparse Mixture-of-Experts (MoE) layers are integrated, ensuring only relevant experts are activated. Scaling this heterogeneous design is achieved through HeteroP, a module-wise hyperparameter transfer scheme that dynamically adjusts parameters based on tensor fan-in and model depth. This principled scaling recipe is guided by Chinchilla-style compute-optimal laws, balancing activated model size, training token count, and data ratios for optimal performance.

**Application Scenarios**

The effectiveness of Chimera is demonstrated through several key findings. Firstly, its dense backbone exhibits 1.7x greater compute efficiency than a comparable full-attention baseline, with the complete system achieving a remarkable 7.3x improvement in pretraining diffusion loss. Secondly, Chimera showcases impressive zero-shot generalization capabilities, extrapolating from short training clips to significantly longer videos (e.g., 5 seconds to 30 seconds) with minimal FID degradation. This suggests its suitability for applications requiring the generation of extended visual sequences without extensive length-specific fine-tuning. Finally, the study provides insights into compute-optimal training strategies, indicating that for image pretraining, compute should be roughly split between model size and token count, while video pretraining benefits more from increased model size at higher compute budgets.

**Summary**

Chimera represents a significant advancement in efficient long-context visual diffusion modeling. By employing a hybrid architecture that strategically combines different attention mechanisms and convolutions, alongside a principled scaling strategy (HeteroP) and compute-optimal training laws, it overcomes the quadratic cost limitations of traditional methods. The demonstrated improvements in compute efficiency, zero-shot generalization to longer sequences, and insights into optimal training configurations establish Chimera as a robust foundation for future research and development in high-resolution and long-form visual generation.

</details>

---
### 5. [OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models](https://arxiv.org/abs/2607.28609v1)
👤 **Authors:** Qiushi Sun, Kanzhi Cheng, Yian Wang
<details>
<summary><strong>📄 Paper Summary:</strong> Computer-using agents (CUAs) are advancing rapidly across the digital world. A CUA traject...</summary>

Computer-using agents (CUAs) are advancing rapidly across the digital world. A CUA trajectory records the agent's actions, states, and reasoning. Verifying whether it fulfilled the task instruction is central to CUA evaluation, data curation, and reinforcement learning. Neither human-written verifiers nor human annotators can provide such verification at scale, so the field increasingly turns to vision-language models (VLMs) as judges of CUA trajectories. But a fundamental question has long gone unexamined: are these VLM judges reliable enough? To study it systematically, we introduce OSReward, a realistic, high-quality benchmark that evaluates VLM judges on CUA trajectories. The trajectories come from diverse agent backbones executing human-verified instructions across platforms, then rigorously labeled with ground-truth verdicts through multi-stage human annotation. Building on it, we derive OSReward-Hard, a challenge set concentrating genuinely hard cases, and OSReward-Multi for fine-grained efficiency and alignment scoring. The most comprehensive evaluation of VLM judges to date finds even state-of-the-art models fall short of an ideal judge, sharing a systematic leniency bias that mislabels failed runs as successes. The few reliable enough to trust are too expensive to run at scale, while affordable open models trail far behind. To close this gap, we construct and release OS-Shepherd-100K, an open corpus of reasoning-annotated trajectory judgments for the CUA community. On it, we train OS-Shepherd (9B and 35B), open reward models that supply low-cost, stable, and reliable reward signals, matching commercial judges at 30-60% lower cost than the frontier. Extensive analyses further inform the design of reliable CUA reward at scale. Our code, benchmark, dataset, and model checkpoints are available at https://os-copilot.github.io/OSReward-Home/.

</details>

---