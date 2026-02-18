import httpx
from bs4 import BeautifulSoup
from urllib.parse import quote
import logging
logger = logging.getLogger(__name__)
CONTENT_TRUNCATE_LIMIT = 5000
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
def _validate_url(url: str) -> bool:
    return bool(url and url.startswith(('http://', 'https://')))
def fetch_url_content(url: str) -> str:
    """
    Fetches the content of a URL and extracts text from paragraphs.
    """
    if not _validate_url(url):
        return ""
    try:
        response = httpx.get(url, headers=HEADERS, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.extract()
        text = soup.get_text(separator=' ', strip=True)
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        return text[:CONTENT_TRUNCATE_LIMIT]
    except (httpx.RequestError, ValueError, AttributeError) as e:
        logger.debug(f"Failed to fetch content from {url}: {e}")
        return ""
