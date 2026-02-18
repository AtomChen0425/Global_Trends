# 🌐 Global Tech Intelligence

[English](#english) | [中文](doc/README_CN.md)

---
<a name="english"></a>

### 📖 Introduction
**Global Tech Intelligence** is an automated information aggregation pipeline designed to track the latest global technology trends. It fetches data from high-quality tech sources, utilizes **Google Gemini AI** for deep content summarization, and generates structured Daily Briefing reports.

### 🚀 Key Features
- **Multi-Source Aggregation**:
  - **Hacker News**: Fetches top stories and discussions.
  - **GitHub**: Tracks trending repositories and latest projects (supports filtering by time range).
  - **ArXiv**: Retrieves the latest academic papers in AI & Computer Vision (`cs.CV`).
- **AI-Powered Summarization**: Uses `gemini-2.5-flash-lite` to generate concise summaries for articles, READMEs, and paper abstracts.
- **Automated Reporting**: Generates polished Markdown reports in both **English** and **Chinese**.
- **High Performance**: Implements asynchronous concurrent fetching for efficient data processing.

### 🛠️ Tech Stack
- **Core**: Python 3.12+
- **Network**: `httpx`, `BeautifulSoup4`
- **AI Integration**: Google Gemini API
- **Utilities**: `python-dotenv` (Config), `tenacity` (Retries), `DeepL` (Translation support)

### ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/AtomChen0425/Global_Trends.git
   cd Global_Trends
   ```
2. **Install dependencies**
```bash
pip install httpx beautifulsoup4 python-dotenv tenacity deepl
```
3. **Configure Environment Variables**

Create a `.env` file in the root directory and add your API keys:
```plaintext
GITHUB_TOKEN=your_github_token
GEMINI_API_KEY=your_gemini_api_key
DEEPL_API_KEY=your_deepl_api_key
```

### 📝 Usage

Run the main collection script:
```bash
python collect_daily_information.py
```

### 📂 Project Structure
```
Global_Trends/
├── collect_daily_information.py  # Main entry point
├── src/
│   ├── FetchPipeline/            # Scrapers for HN, GitHub, ArXiv
│   ├── Generators/               # Markdown report generators
│   ├── utils/                    # AI Agent, Prompt Loader, Translator
│   └── start_work.py             # Orchestration logic
├── prompts/                      # Prompt templates for Gemini
└── reports/                      # Output directory for briefings
```

### GitHub Action Automation
A daily report has been generated in the [issue](https://github.com/AtomChen0425/Global_Trends/issues).

Historical data can be found in the reports folder.
