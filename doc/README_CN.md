### 📖 项目介绍

**Global Tech Intelligence (全球技术情报)** 是一个自动化的信息聚合流水线，旨在追踪全球最新的技术趋势。它从高质量的技术源抓取数据，利用 **Google Gemini AI** 进行深度的内容摘要，并生成结构化的每日简报。

### 🚀 核心功能

* **多源信息聚合**：
  * **Hacker News**：抓取热门科技新闻与讨论。
  * **GitHub**：追踪热门趋势项目及最新发布的开源项目。
  * **ArXiv**：获取 AI 与计算机视觉领域 (`cs.CV`) 的最新学术论文。


* **AI 智能摘要**：调用 `gemini-2.5-flash-lite` 模型，对长文章、项目文档和论文摘要进行精准提炼。
* **自动报告生成**：支持一键生成排版精美的 **中文** 和 **英文** Markdown 简报。
* **高效并发**：采用异步并发机制，大幅提升数据抓取与处理效率。

### 🛠️ 技术栈

* **核心语言**：Python 3.12+
* **网络请求**：`httpx`, `BeautifulSoup4`
* **AI 集成**：Google Gemini API
* **工具库**：`python-dotenv` (配置管理), `tenacity` (重试机制), `DeepL` (翻译支持)

### ⚙️ 安装与配置

1. **克隆项目**
```bash
git clone [https://github.com/your-username/Global_Trends.git](https://github.com/your-username/Global_Trends.git)
cd Global_Trends

```


2. **安装依赖**
```bash
pip install httpx beautifulsoup4 python-dotenv tenacity deepl

```


3. **配置环境变量**
在项目根目录下创建 `.env` 文件，并填入您的 API 密钥：
```ini
# GitHub Token (用于提高 API 调用限额)
GITHUB_TOKEN=sk_...

# Google Gemini API Key (用于 AI 摘要生成)
GEMINI_API_KEY=AIza...

# DeepL API Key (可选，用于翻译功能)
DEEPL_API_KEY=...

```



### 🏃‍♂️ 使用方法

运行主程序开始采集与生成：

```bash
python collect_daily_information.py

```

运行完成后，生成的简报将保存在 `reports/` 目录下：

* `reports/Daily_Briefing_YYYY-MM-DD_CN.md` (中文日报)
* `reports/Daily_Briefing_YYYY-MM-DD_EN.md` (英文日报)

### 📂 项目结构

```text
Global_Trends/
├── collect_daily_information.py  # 程序入口
├── src/
│   ├── FetchPipeline/            # 数据抓取模块 (HN, GitHub, ArXiv)
│   ├── Generators/               # 报告生成模块 (Markdown 渲染)
│   ├── utils/                    # 工具模块 (AI Agent, Prompt 加载, 翻译)
│   └── start_work.py             # 任务编排逻辑
├── prompts/                      # 存放给 Gemini 的提示词模板
└── reports/                      # 存放生成的日报文件

```
