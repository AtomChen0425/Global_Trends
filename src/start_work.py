#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

import os
import logging
import concurrent.futures
from typing import Dict, List
from FetchPipeline.HN_pipeline import fetch_top_stories
from FetchPipeline.github_pipeline import fetch_github_from_web, enrich_trend_data, fetch_latest_Github
from FetchPipeline.arxiv_pipeline import fetch_papers_by_category
from Generators.report_generator_md import generate_report,save_report
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [%(name)s] %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)


FETCH_TIMEOUT = 60 

def _fetch_hn(limit: int) -> List[Dict]:
    """抓取 Hacker News 数据"""
    logger.info("开始抓取 Hacker News...")
    results = []
    try:
        stories = fetch_top_stories(limit=limit)
        for s in stories:
            results.append({
                "source": "Hacker News",
                "title": s.title,
                "url": s.url or s.hn_url,
                "score": s.score,
                "time": s.timestr or ""
            })
        logger.info(f"Hacker News: 成功抓取 {len(results)} 条")
    except Exception as e:
        logger.warning(f"Hacker News 抓取失败: {e}")
    return results

def _fetch_github(limit: int) -> List[Dict]:
    """抓取 GitHub Trending 数据"""
    logger.info("开始抓取 GitHub Trending...")
    results = []
    try:
        trends_raw = fetch_github_from_web()
        trends = enrich_trend_data(trends_raw[:limit])
        for t in trends:
            results.append({
                "source": "GitHub 开源项目",
                "title": t.name,
                "url": t.url,
                "description": t.description,
                "stars": t.stars,
                "readme": t.readme_text if t.readme_text else ""
            })
        logger.info(f"GitHub: 成功抓取 {len(results)} 条")
    except Exception as e:
        logger.warning(f"GitHub 抓取失败: {e}")
    return results
def _fetch_latest_github(limit: int) -> List[Dict]:
    """抓取 GitHub 最新项目数据"""
    logger.info("开始抓取 GitHub 最新项目...")
    results = []
    try:
        trends = fetch_latest_Github()[:limit]
        for t in trends:
            results.append({
                "source": "GitHub 最新项目",
                "title": t.name,
                "url": t.url,
                "description": t.description,
                "stars": t.stars,
                "readme": t.readme_text if t.readme_text else ""
            })
        logger.info(f"GitHub: 成功抓取 {len(results)} 条")
    except Exception as e:
        logger.warning(f"GitHub 最新项目 抓取失败: {e}")
    return results
def _fetch_arxiv(category: str, limit: int) -> List[Dict]:
    """抓取 ArXiv 最新论文数据"""
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
                "summary": p.summary 
            })
        logger.info(f"ArXiv: 成功抓取 {len(results)} 条")
    except Exception as e:
        logger.warning(f"ArXiv 抓取失败: {e}")
    return results


def fetch_all_sources(limit=10) -> Dict[str, List[Dict]]:
    """并行抓取所有配置的数据源"""
    logger.info("启动数据抓取引擎...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        fetch_hn = executor.submit(_fetch_hn, limit)
        fetch_gh = executor.submit(_fetch_github, limit)
        fetch_arxiv = executor.submit(_fetch_arxiv, "cs.CV", limit)
        fetch_latest_gh = executor.submit(_fetch_latest_github, limit)

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
            "hn": _safe_result(fetch_hn, "Hacker News"),
            "github": _safe_result(fetch_gh, "GitHub"),
            "arxiv": _safe_result(fetch_arxiv, "ArXiv"),
            "latest_github": _safe_result(fetch_latest_gh, "GitHub Latest")
        }
        
    total_items = sum(len(v) for v in intel.values())
    logger.info(f"✅ All done! 收集到{total_items} 条。")
    return intel

def format_intel(intel: Dict[str, List[Dict]]) -> str:
    formatted_text = ""
    
    for item in intel.get("hn", []):
        formatted_text += f"[来源: {item['source']}]\n标题: {item['title']}\n链接: {item['url']}\n热度: {item['score']} points\n---\n"
        
    for item in intel.get("github", []):
        formatted_text += f"[来源: {item['source']}]\n标题: {item['title']}\n链接: {item['url']}\n描述: {item.get('description', '')}\nStar数: {item['stars']}\n---\n"
        
    for item in intel.get("latest_github", []):
        formatted_text += f"[来源: {item['source']}]\n标题: {item['title']}\n链接: {item['url']}\n描述: {item.get('description', '')}\nStar数: {item['stars']}\n---\n"

    for item in intel.get("arxiv", []):
        formatted_text += f"[来源: {item['source']}]\n标题: {item['title']}\n作者: {item['authors']}\n链接: {item['url']}\n摘要: {item['summary']}...\n---\n"
        
    return formatted_text

if __name__ == "__main__":
    intel= fetch_all_sources(limit=5)
    # print(intel)
    print("\n" + "="*40)
    print("开始生成并排版Markdown 报告...")
    markdown_content = generate_report(intel)
    
    # 保存文件
    file_path = save_report(markdown_content)
    # print(format_intel(intel))