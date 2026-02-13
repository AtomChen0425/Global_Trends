"""
Fetches GitHub repositories.
"""

import os
import sys
import datetime
from dataclasses import dataclass, field
from typing import Optional
from bs4 import BeautifulSoup
import httpx
import logging

logger = logging.getLogger(__name__)

GITHUB_API_URL = "https://api.github.com/graphql"

@dataclass
class GitHubTrend:
    """A single repository."""
    name: str                   # e.g., "owner/repo"
    url: str
    description: str
    language: Optional[str]
    stars: int
    forks: int
    created_at: str
    pushed_at: str
    readme_text: Optional[str] = None 
    hype_score: int = field(init=False)

    def __post_init__(self):
        import math
        self.hype_score = min(100, int(math.log10(max(self.stars, 1)) * 25))

def load_env_token() -> Optional[str]:
    """Load GITHUB_TOKEN from .env file manually."""
    candidates = [
        os.path.join(os.path.dirname(__file__), "..", ".env"),
        os.path.join(os.getcwd(), ".env")
    ]
    
    for env_path in candidates:
        if os.path.exists(env_path):
            try:
                with open(env_path, "r", encoding="utf-8-sig", errors="ignore") as f:
                    for line in f:
                        line = line.strip()
                        if not line or line.startswith("#"): continue
                        if "GITHUB_TOKEN=" in line:
                            return line.split("=", 1)[1].strip()
                        if line.startswith("ghp_") or line.startswith("github_pat_"):
                            return line
            except Exception:
                pass
                
    return os.environ.get("GITHUB_TOKEN")

def enrich_trend_data(trends: list[GitHubTrend]) -> list[GitHubTrend]:
    """Fetch README and other details for each trend."""
    token = load_env_token()
    if not token:
        logger.error("ERROR: GITHUB_TOKEN not found in .env or environment variables.")
        return trends  # Return original trends without enrichment
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "Commercial-Agent-Sensor"
    }
    query_template = """
        query ($owner: String!, $name: String!) {
        repository(owner: $owner, name: $name) {
            createdAt
            pushedAt
            readme: object(expression: "HEAD:README.md") {
            ... on Blob {
                text
            }
            }
        }
        }
        """
    for trend in trends:
        try:
            owner, repo = trend.name.split("/")
            variables = {"owner": owner, "name": repo}
            response = httpx.post(GITHUB_API_URL, json={"query": query_template, "variables": variables}, headers=headers, timeout=30.0)
            if response.status_code == 200:
                data = response.json()
                repo_data = data.get("data", {}).get("repository", {})
                trend.created_at = repo_data.get("createdAt", "")
                trend.pushed_at = repo_data.get("pushedAt", "")
                readme_obj = repo_data.get("readme")
                trend.readme_text = readme_obj.get("text", "")[:5000] if readme_obj else ""
            else:
                logger.warning(f"Failed to fetch details for {trend.name}: {response.status_code}")
        except Exception as e:
            logger.warning(f"Exception while enriching {trend.name}: {e}")
    return trends
def fetch_github_from_web() -> list[GitHubTrend]:
    try:
        response = httpx.get("https://github.com/trending",timeout=10)
    except httpx.RequestError as e:
        logger.warning(f"GitHub trending fetch failed: {e}")
        return []
    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    trends = []
    for article in soup.select('article.Box-row'):
        try:
            h2 = article.select_one('h2 a')
            if not h2:
                continue
            title = h2.get_text(strip=True).replace('\n', '').replace(' ', '')
            link = "https://github.com" + h2['href']

            desc = article.select_one('p')
            desc_text = desc.get_text(strip=True) if desc else ""
    
            stars_tag = article.select_one('a[href$="/stargazers"]')
            stars = stars_tag.get_text(strip=True) if stars_tag else ""

            forks_tag = article.select_one('a[href$="/forks"]')
            forks = forks_tag.get_text(strip=True) if forks_tag else ""
            
            language_tag = article.select_one('span[itemprop="programmingLanguage"]')
            language = language_tag.get_text(strip=True) if language_tag else None
            trends.append(GitHubTrend(
                name=title,
                url=link,
                description=desc_text,
                language=language,
                stars=int(stars.replace(',', '')) if stars else 0,
                forks=int(forks.replace(',', '')) if forks else 0,
                created_at="",
                pushed_at="",
                readme_text=""
            ))
        except (AttributeError, KeyError, TypeError) as e:
            logger.debug(f"Failed to parse GitHub row: {e}")
            continue
    return trends
def fetch_trending(language: Optional[str] = None) -> list[GitHubTrend]:
    """
    Search for repos created in the last 7 days, sorted by stars.
    """
    token = load_env_token()
    if not token:
        logger.error("ERROR: GITHUB_TOKEN not found in .env or environment variables.")
        return []
    # Calculate date 7 days ago
    seven_days_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime("%Y-%m-%d")
    
    search_query = f"created:>{seven_days_ago} sort:stars"
    if language:
        search_query += f" language:{language}"

    graphql_query = """
    query($search_query: String!) {
      search(query: $search_query, type: REPOSITORY, first: 10) {
        edges {
          node {
            ... on Repository {
              nameWithOwner
              url
              description
              stargazerCount
              forkCount
              createdAt
              pushedAt
              primaryLanguage {
                name
              }
              object(expression: "HEAD:README.md") {
                ... on Blob {
                  text
                }
              }
            }
          }
        }
      }
    }
    """

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "Commercial-Agent-Sensor"
    }

    payload = {
        "query": graphql_query,
        "variables": {"search_query": search_query}
    }
    
    try:
        print(f"  → Sending GraphQL query to GitHub ({search_query})...")
        response = httpx.post(GITHUB_API_URL, json=payload, headers=headers, timeout=30.0)
        
        if response.status_code != 200:
            print(f"ERROR: API returned {response.status_code}")
            print(response.text)
            return []
            
        data = response.json()
        if "errors" in data:
            print(f"ERROR: GraphQL errors: {data['errors']}")
            return []

        return _parse_graphql_response(data)

    except Exception as e:
        print(f"ERROR: Request failed: {e}")
        return []

def _parse_graphql_response(data: dict) -> list[GitHubTrend]:
    trends = []
    edges = data.get("data", {}).get("search", {}).get("edges", [])
    
    for edge in edges:
        node = edge.get("node")
        if not node:
            continue
            
        # Extract README
        readme_obj = node.get("object")
        readme_text = readme_obj.get("text", "") if readme_obj else ""
            
        trends.append(GitHubTrend(
            name=node["nameWithOwner"],
            url=node["url"],
            description=node["description"] or "(No description)",
            language=node["primaryLanguage"]["name"] if node["primaryLanguage"] else None,
            stars=node["stargazerCount"],
            forks=node["forkCount"],
            created_at=node["createdAt"],
            pushed_at=node["pushedAt"],
            readme_text=readme_text[:5000]  # Truncate to save memory/tokens
        ))
        
    return trends

def print_trends(trends: list[GitHubTrend]) -> None:
    print(f"\n{'='*60}")
    print(f" 🚀 Breakout Repos (Last 7 Days) - Top {len(trends)}")
    print(f"{'='*60}\n")

    for i, t in enumerate(trends, 1):
        print(f"{i}. [{t.hype_score:3d}] {t.name}")
        print(f"   ⭐ {t.stars} | 🍴 {t.forks} | Created: {t.created_at[:10]}")
        if t.language:
            print(f"   📝 {t.language}")
        print(f"   {t.description[:100]}...")
        print(f"   README (first 2000 chars):")
        print(f"   {t.readme_text[:2000]}...")
        print(f"   🔗 {t.url}")
        print()

if __name__ == "__main__":
    lang = sys.argv[1] if len(sys.argv) > 1 else None
    # trends = fetch_trending(lang)
    trends = fetch_github_from_web()
    trends = enrich_trend_data(trends)
    print(f"Number of trends fetched: {len(trends)}")
    if trends:
        print_trends(trends)
        
        # MVP: Auto-trigger for the Top 1 item
        top_trend = trends[0]
        print(f"\n[Commercial Agent] 🧠 Automatically analyzing top opportunity: {top_trend.name}")
        
    else:
        print("No trends found.")
