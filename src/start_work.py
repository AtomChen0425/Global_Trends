#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

import os
import logging
import concurrent.futures
from datetime import datetime
from typing import Dict, List

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [%(name)s] %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

HN_AVAILABLE = False
GITHUB_AVAILABLE = False
ARXIV_AVAILABLE = False
AI_AVAILABLE = False

try:
    from FetchPipeline.HN_pipeline import fetch_top_stories
    HN_AVAILABLE = True
except ImportError as e:
    logger.warning(f"Hacker News pipeline 不可用，跳过。原因: {e}")

try:
    from FetchPipeline.github_pipeline import fetch_github_from_web, enrich_trend_data
    GITHUB_AVAILABLE = True
except ImportError as e:
    logger.warning(f"GitHub pipeline 不可用，跳过。原因: {e}")

try:
    from FetchPipeline.arxiv_pipeline import fetch_papers_by_category
    ARXIV_AVAILABLE = True
except ImportError as e:
    logger.warning(f"ArXiv pipeline 不可用，跳过。原因: {e}")

try:
    from utils.AI_Agent import gemini_summarize
    AI_AVAILABLE = True
except ImportError as e:
    logger.error(f"AI 代理模块导入失败，将无法生成分析报告！原因: {e}")

FETCH_TIMEOUT = 60  # 单个数据源的最大等待时间（秒）

def _fetch_hn(limit: int) -> List[Dict]:
    """抓取 Hacker News 数据"""
    if not HN_AVAILABLE: return []
    logger.info("开始抓取 Hacker News...")
    results = []
    try:
        stories = fetch_top_stories(limit=limit)
        for s in stories:
            results.append({
                "source": "Hacker News",
                "title": s.title,
                "url": s.url or s.hn_url,
                "score": s.score
            })
        logger.info(f"Hacker News: 成功抓取 {len(results)} 条")
    except Exception as e:
        logger.warning(f"Hacker News 抓取失败: {e}")
    return results

def _fetch_github(limit: int) -> List[Dict]:
    """抓取 GitHub Trending 数据"""
    if not GITHUB_AVAILABLE: return []
    logger.info("开始抓取 GitHub Trending...")
    results = []
    try:
        trends_raw = fetch_github_from_web()
        # 截取前 N 个并获取 README 等详细信息
        trends = enrich_trend_data(trends_raw[:limit])
        for t in trends:
            results.append({
                "source": "GitHub 开源项目",
                "title": t.name,
                "url": t.url,
                "description": t.description,
                "stars": t.stars
            })
        logger.info(f"GitHub: 成功抓取 {len(results)} 条")
    except Exception as e:
        logger.warning(f"GitHub 抓取失败: {e}")
    return results

def _fetch_arxiv(category: str, limit: int) -> List[Dict]:
    """抓取 ArXiv 最新论文数据"""
    if not ARXIV_AVAILABLE: return []
    logger.info(f"开始抓取 ArXiv ({category})...")
    results = []
    try:
        papers = fetch_papers_by_category(category, limit=limit)
        for p in papers:
            results.append({
                "source": "ArXiv 学术论文",
                "title": p.title,
                "url": p.url,
                "authors": ", ".join(p.authors),
                "summary": p.summary[:400] 
            })
        logger.info(f"ArXiv: 成功抓取 {len(results)} 条")
    except Exception as e:
        logger.warning(f"ArXiv 抓取失败: {e}")
    return results


def fetch_all_sources(hn_limit=10, gh_limit=10, arxiv_limit=10) -> Dict[str, List[Dict]]:
    """并行抓取所有配置的数据源"""
    logger.info("启动数据抓取引擎...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # 并行提交任务
        future_hn = executor.submit(_fetch_hn, hn_limit)
        future_gh = executor.submit(_fetch_github, gh_limit)
        future_arxiv = executor.submit(_fetch_arxiv, "cs.CV", arxiv_limit)

        def _safe_result(future, name):
            try:
                return future.result(timeout=FETCH_TIMEOUT)
            except concurrent.futures.TimeoutError:
                logger.warning(f"[{name}] 数据源抓取超时 ({FETCH_TIMEOUT}s)")
                return []
            except Exception as e:
                logger.warning(f"[{name}] 数据源抓取异常: {e}")
                return []

        # 收集结果
        intel = {
            "hn": _safe_result(future_hn, "Hacker News"),
            "github": _safe_result(future_gh, "GitHub"),
            "arxiv": _safe_result(future_arxiv, "ArXiv"),
        }
        
    total_items = sum(len(v) for v in intel.values())
    logger.info(f"✅ All done! 收集到{total_items} 条。")
    return intel

def format_intel_for_ai(intel: Dict[str, List[Dict]]) -> str:
    formatted_text = ""
    
    for item in intel.get("hn", []):
        formatted_text += f"[来源: {item['source']}]\n标题: {item['title']}\n链接: {item['url']}\n热度: {item['score']} points\n---\n"
        
    for item in intel.get("github", []):
        formatted_text += f"[来源: {item['source']}]\n标题: {item['title']}\n链接: {item['url']}\n描述: {item.get('description', '')}\nStar数: {item['stars']}\n---\n"
        
    for item in intel.get("arxiv", []):
        formatted_text += f"[来源: {item['source']}]\n标题: {item['title']}\n作者: {item['authors']}\n链接: {item['url']}\n摘要: {item['summary']}...\n---\n"
        
    return formatted_text

def main():
    # 1. 并行收集数据
    intel_data = fetch_all_sources(hn_limit=5, gh_limit=3, arxiv_limit=3)
    raw_data_string = format_intel_for_ai(intel_data)
    
    if not raw_data_string.strip():
        logger.error("未收集到任何有效数据，程序退出。")
        return

    # 2. 调用 AI 进行分析
    if not AI_AVAILABLE:
        logger.error("AI 模块不可用，无法生成最终报告。原始数据:\n" + raw_data_string)
        return

    logger.info("🧠 正在将原始情报提交给大模型进行深度分析 (可能需要 15-30 秒)...")
    try:
        final_report = gemini_summarize(raw_data_string)
        if not final_report:
            raise ValueError("AI 返回内容为空")
    except Exception as e:
        logger.error(f"AI 生成报告时发生错误: {e}")
        return

    # 3. 存储报告
    output_dir = "reports"
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(output_dir, f"Intel_Report_{timestamp}.md")
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(final_report)
        
    logger.info(f"🎉 报告生成完毕！已保存至 -> {filename}")

if __name__ == "__main__":
    intel= fetch_all_sources()
    # print(intel)
    print(format_intel_for_ai(intel))