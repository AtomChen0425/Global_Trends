import os
import sys
import httpx
from dotenv import load_dotenv
import deepl

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv()  # Load .env variables
def translate_text_by_deepl(text: str, target_lang: str = "ZH") -> str:
    """Translate text using DeepL API."""
    api_key = os.getenv("DEEPL_API_KEY")
    
    try:
        translator = deepl.DeepLClient(api_key)
        result = translator.translate_text(text, target_lang=target_lang)
        return result.text
    except Exception as e:
        print(f"  ❌ Translation error: {e}")
        return text
if __name__ == "__main__":
    test_text = "Test-time scaling has become a standard way to improve performance and boost reliability of neural network models. However, its behavior on agentic, multi-step tasks remains less well-understood: small per-step errors can compound over long horizons; and we find that naive policies that uniformly increase sampling show diminishing returns. In this work, we present CATTS, a simple technique for dynamically allocating compute for multi-step agents. We first conduct an empirical study of inference-time scaling for web agents. We find that uniformly increasing per-step compute quickly saturates in long-horizon environments. We then investigate stronger aggregation strategies, including an LLM-based Arbiter that can outperform naive voting, but that can overrule high-consensus decisions. We show that uncertainty statistics derived from the agent's own vote distribution (entropy and top-1/top-2 margin) correlate with downstream success and provide a practical signal for dynamic compute allocation. Based on these findings, we introduce Confidence-Aware Test-Time Scaling (CATTS), which uses vote-derived uncertainty to allocate compute only when decisions are genuinely contentious. CATTS improves performance on WebArena-Lite and GoBrowse by up to 9.1% over React while using up to 2.3x fewer tokens than uniform scaling, providing both efficiency gains and an interpretable decision rule."
    print("原文:", test_text)
    print("翻译:", translate_text_by_deepl(test_text, target_lang="ZH"))
