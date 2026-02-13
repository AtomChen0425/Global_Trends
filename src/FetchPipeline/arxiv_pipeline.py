"""
Fetches latest papers from arXiv.
"""
import sys
import re
from dataclasses import dataclass
from typing import List
from datetime import datetime
import httpx
@dataclass
class ArxivPaper:
    """An arXiv paper."""
    id: str
    title: str
    summary: str
    authors: List[str]
    published: str
    categories: List[str]
    
    @property
    def url(self) -> str:
        return f"https://arxiv.org/abs/{self.id}"
    
    @property
    def pdf_url(self) -> str:
        return f"https://arxiv.org/pdf/{self.id}.pdf"
def fetch_papers_by_category(category: str, limit: int = 10) -> List[ArxivPaper]:
    """Fetch papers from a specific arXiv category."""
    print(f"  → Fetching latest {limit} papers from category '{category}'...")
    query = f"cat:{category}"
    return _query_arxiv(query, "submittedDate", limit)

def _query_arxiv(query: str, sort_by: str, limit: int) -> List[ArxivPaper]:
    """Execute a single ArXiv API query and parse results."""
    url = f"https://export.arxiv.org/api/query?search_query={query}&start=0&max_results={limit}&sortBy={sort_by}&sortOrder=descending"
    
    try:
        resp = httpx.get(url, timeout=30)
        xml = resp.text
        
        if len(xml) < 500:
            print(f"    DEBUG: Short response ({len(xml)} bytes)")
            return []
    except Exception as e:
        print(f"    ERROR: {e}")
        return []
    
    papers = []
    entries = re.findall(r'<entry>(.*?)</entry>', xml, re.DOTALL)
    
    for entry in entries:
        arxiv_id_match = re.search(r'<id>http://arxiv.org/abs/([^<]+)</id>', entry)
        title_match = re.search(r'<title>(.*?)</title>', entry, re.DOTALL)
        summary_match = re.search(r'<summary>(.*?)</summary>', entry, re.DOTALL)
        published_match = re.search(r'<published>([^<]+)</published>', entry)
        authors = re.findall(r'<name>([^<]+)</name>', entry)
        categories = re.findall(r'<category term="([^"]+)"', entry)
        
        if arxiv_id_match and title_match:
            # Clean summary
            raw_summary = summary_match.group(1).strip() if summary_match else ""
            clean_summary = ' '.join(raw_summary.split())  # Collapse whitespace
            
            papers.append(ArxivPaper(
                id=arxiv_id_match.group(1),
                title=title_match.group(1).strip().replace('\n', ' '),
                summary=clean_summary,
                authors=authors[:3],  # First 3 authors
                published=published_match.group(1)[:10] if published_match else "",
                categories=categories[:3]
            ))
    
    return papers

def print_papers(papers: List[ArxivPaper]):
    """Print papers in a readable format."""
    print(f"\n{'='*60}")
    print(f"  📚 arXiv AI/ML Latest Papers")
    print(f"{'='*60}\n")
    
    for i, p in enumerate(papers, 1):
        print(f"{i}. {p.title}")
        print(f"   👤 {', '.join(p.authors)}")
        print(f"   📅 {p.published} | 🏷️ {', '.join(p.categories)}")
        print(f"   🔗 {p.url}")
        print()

if __name__ == "__main__":
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    # papers = fetch_ai_papers(limit)
    CV_papers=fetch_papers_by_category("cs.CV", limit)
    if CV_papers:
        print_papers(CV_papers)
    else:
        print("No papers found.")
