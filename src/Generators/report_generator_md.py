import os
import time
import logging
from datetime import datetime
from src.FetchPipeline.fetch_from_web import fetch_url_content

# 尝试导入 Gemini AI 工具
try:
    from src.utils.AI_Agent import gemini_summarize
    GEMINI_AVAILABLE = True
    GEMINI_RATE_LIMIT_DELAY = 2.0  # 避免触发 API 频率限制
except ImportError:
    GEMINI_AVAILABLE = False
    logging.getLogger(__name__).warning("Gemini AI_Agent 模块未找到，将仅使用原文摘要。")

logger = logging.getLogger(__name__)

def _get_ai_summary(content: str, prompt_name: str, item_id: str) -> str:
    """
    通用 AI 摘要获取函数
    """
    if not content or not GEMINI_AVAILABLE:
        return ""
    
    try:
        logger.info(f"[{item_id}] 正在生成 AI 摘要...")
        summary = gemini_summarize(content, prompt_name)
        time.sleep(GEMINI_RATE_LIMIT_DELAY)
        return summary
    except Exception as e:
        logger.error(f"[{item_id}] AI 摘要生成失败: {e}")
        return ""

def _format_expandable_block(text: str, label: str = "🤖 AI 摘要", cutoff: int = 90) -> str:
    """
    生成“无缝展开”的 HTML 块
    将文本切分为 Head (摘要可见部分) 和 Tail (折叠部分)
    """
    if not text:
        return ""

    if len(text) <= cutoff:
        # 文本很短，直接显示
        return f"> <strong>{label}:</strong> {text}\n"

    # 切割文本
    head = text[:cutoff]
    # tail = text[cutoff:]
    
    # 转义 summary 标签中的特殊字符，防止 HTML 渲染错误
    head_safe = head.replace('"', "'").replace("<", "&lt;").replace(">", "&gt;")

    html = [
        f"<details>",
        f"<summary><strong>{label}:</strong> {head_safe}...</summary>",
        f"\n{text}\n", 
        f"</details>\n"
    ]
    return "\n".join(html)

def generate_report_CN(intel: dict) -> str:
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    lines = [
        f"# 🌐 Global Tech Intelligence Briefing - {date_str}",
        f"**日期:** {date_str}",
        f"**生成时间:** {datetime.now().strftime('%H:%M')}",
        f"**数据源:** Hacker News, GitHub Trending, ArXiv",
        "",
        "---",
        ""
    ]

    # --- 1. Hacker News ---
    lines.append("## 📰 Hacker News (Top Stories)")
    if intel.get("hn"):
        for i, item in enumerate(intel["hn"], 1):
            title = item.get("title", "Untitled").replace("|", "&#124;")
            url = item.get("url", "#")
            score = item.get("score", 0)
            time_str = item.get("time", "")
            
            lines.append(f"### {i}. [{title}]({url})")
            lines.append(f"🔥 {score} | 🕒 {time_str}")
            
            # 获取内容 -> AI 总结 -> 格式化
            content = fetch_url_content(url)
            if content:
                # 优先用 AI 摘要，如果没有则截取原文
                ai_summary = _get_ai_summary(content, "TechDoc_Summarize_CN", f"HN-{i}")
                display_text = ai_summary if ai_summary else content[:500] + "..."
                
                # 添加折叠块
                lines.append(_format_expandable_block(display_text, label="📖 摘要"))
            
            lines.append("---")
    else:
        lines.append("*暂无数据*\n")

    # --- 2. GitHub Trending ---
    lines.append("## 🚀 GitHub Trending")
    lines.append("> 过去 24 小时高星增长项目\n")
    if intel.get("github"):
        for i, item in enumerate(intel["github"], 1):
            title = item.get("title", "Untitled")
            url = item.get("url", "#")
            stars = item.get("stars", 0)
            desc = item.get("description", "暂无描述").strip().replace("\n", " ")
            readme = item.get("readme", "").strip()
            
            lines.append(f"### {i}. [{title}]({url})")
            lines.append(f"⭐ **Stars:** {stars}")
            lines.append(f"> 📝 {desc}\n")
            
            if readme:
                ai_summary = _get_ai_summary(readme, "Github_Summarize_CN", f"GH-{i}")
                display_text = ai_summary if ai_summary else readme[:500] + "..."
                lines.append(_format_expandable_block(display_text, label="🤖 智能解析"))
            
            lines.append("---")
    else:
        lines.append("*暂无数据*\n")

    # --- 3. GitHub Latest ---
    lines.append("## ✨ GitHub (New & Shiny)")
    if intel.get("latest_github"):
        for i, item in enumerate(intel["latest_github"], 1):
            title = item.get("title", "Untitled")
            url = item.get("url", "#")
            stars = item.get("stars", 0)
            desc = item.get("description", "暂无描述").strip().replace("\n", " ")
            readme = item.get("readme", "").strip()
            
            lines.append(f"### {i}. [{title}]({url})")
            lines.append(f"⭐ **Stars:** {stars}")
            lines.append(f"> 📝 {desc}\n")
            
            if readme:
                ai_summary = _get_ai_summary(readme, "Github_Summarize_CN", f"GH-New-{i}")
                display_text = ai_summary if ai_summary else readme[:500] + "..."
                lines.append(_format_expandable_block(display_text, label="🤖 智能解析"))

            lines.append("---")
    else:
        lines.append("*暂无数据*\n")

    # --- 4. ArXiv Papers ---
    lines.append("## 📚 Latest Paper (ArXiv AI/CV Papers)")
    lines.append("> 最新人工智能与计算机视觉论文\n")
    if intel.get("arxiv"):
        for i, item in enumerate(intel["arxiv"], 1):
            title = item.get("title", "Untitled")
            url = item.get("url", "#")
            authors = item.get("authors", "")
            summary = item.get("summary", "").replace("\n", " ")
            
            lines.append(f"### {i}. [{title}]({url})")
            lines.append(f"👤 **Authors:** {authors}")
            
            if summary:
                ai_summary = _get_ai_summary(summary, "TechDoc_Summarize_CN", f"ArXiv-{i}")
                display_text = ai_summary if ai_summary else summary
                lines.append(_format_expandable_block(display_text, label="📄 论文摘要"))

            lines.append("---")
    else:
        lines.append("*暂无数据*\n")

    return "\n".join(lines)
def generate_report_EN(intel: dict) -> str:
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    lines = [
        f"# 🌐 Global Tech Intelligence Briefing - {date_str}",
        f"**Date:** {date_str}",
        f"**Generated At:** {datetime.now().strftime('%H:%M')}",
        f"**Data Sources:** Hacker News, GitHub Trending, ArXiv",
        "",
        "---",
        ""
    ]

    # --- 1. Hacker News ---
    lines.append("## 📰 Hacker News (Top Stories)")
    if intel.get("hn"):
        for i, item in enumerate(intel["hn"], 1):
            title = item.get("title", "Untitled").replace("|", "&#124;")
            url = item.get("url", "#")
            score = item.get("score", 0)
            time_str = item.get("time", "")
            
            lines.append(f"### {i}. [{title}]({url})")
            lines.append(f"🔥 {score} | 🕒 {time_str}")
            
            # 获取内容 -> AI 总结 -> 格式化
            content = fetch_url_content(url)
            if content:
                # 优先用 AI 摘要，如果没有则截取原文
                ai_summary = _get_ai_summary(content, "TechDoc_Summarize", f"HN-{i}")
                display_text = ai_summary if ai_summary else content[:500] + "..."
                
                # 添加折叠块
                lines.append(_format_expandable_block(display_text, label="📖 Summary"))
            
            lines.append("---")
    else:
        lines.append("*No data available*\n")

    # --- 2. GitHub Trending ---
    lines.append("## 🚀 GitHub Trending")
    lines.append("> Projects with the highest star growth in the past 24 hours\n")
    if intel.get("github"):
        for i, item in enumerate(intel["github"], 1):
            title = item.get("title", "Untitled")
            url = item.get("url", "#")
            stars = item.get("stars", 0)
            desc = item.get("description", "No description available").strip().replace("\n", " ")
            readme = item.get("readme", "").strip()
            
            lines.append(f"### {i}. [{title}]({url})")
            lines.append(f"⭐ **Stars:** {stars}")
            lines.append(f"> 📝 {desc}\n")
            
            if readme:
                ai_summary = _get_ai_summary(readme, "Github_Summarize", f"GH-{i}")
                display_text = ai_summary if ai_summary else readme[:500] + "..."
                lines.append(_format_expandable_block(display_text, label="🤖 AI Summary"))
            
            lines.append("---")
    else:
        lines.append("*No data available*\n")

    # --- 3. GitHub Latest ---
    lines.append("## ✨ GitHub (New & Shiny)")
    if intel.get("latest_github"):
        for i, item in enumerate(intel["latest_github"], 1):
            title = item.get("title", "Untitled")
            url = item.get("url", "#")
            stars = item.get("stars", 0)
            desc = item.get("description", "No description available").strip().replace("\n", " ")
            readme = item.get("readme", "").strip()
            
            lines.append(f"### {i}. [{title}]({url})")
            lines.append(f"⭐ **Stars:** {stars}")
            lines.append(f"> 📝 {desc}\n")
            
            if readme:
                ai_summary = _get_ai_summary(readme, "Github_Summarize", f"GH-New-{i}")
                display_text = ai_summary if ai_summary else readme[:500] + "..."
                lines.append(_format_expandable_block(display_text, label="🤖 AI Summary"))

            lines.append("---")
    else:
        lines.append("*No data available*\n")

    # --- 4. ArXiv Papers ---
    lines.append("## 📚 Latest Paper (ArXiv AI/CV Papers)")
    lines.append("> Latest AI and Computer Vision Papers\n")
    if intel.get("arxiv"):
        for i, item in enumerate(intel["arxiv"], 1):
            title = item.get("title", "Untitled")
            url = item.get("url", "#")
            authors = item.get("authors", "")
            summary = item.get("summary", "").replace("\n", " ")
            
            lines.append(f"### {i}. [{title}]({url})")
            lines.append(f"👤 **Authors:** {authors}")
            
            if summary:
                ai_summary = _get_ai_summary(summary, "TechDoc_Summarize", f"ArXiv-{i}")
                display_text = ai_summary if ai_summary else summary
                lines.append(_format_expandable_block(display_text, label="📄 Paper Summary"))

            lines.append("---")
    else:
        lines.append("*No data available*\n")

    return "\n".join(lines)

def save_report(content: str, output_dir: str = "reports",lang='CN') -> str:
    """保存 Markdown 报告"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    date_str = datetime.now().strftime("%Y-%m-%d")
    file_path = os.path.join(output_dir, f"Daily_Briefing_{date_str}_{lang}.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    logger.info(f"✅ 报告已保存: {file_path}")
    return file_path