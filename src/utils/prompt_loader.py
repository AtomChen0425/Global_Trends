from pathlib import Path

def load_prompt(name: str, **kwargs) -> str:
    text = (Path("prompts") / f"{name}.md").read_text(encoding="utf-8")
    for k, v in kwargs.items():
        text = text.replace(f"{{{{{k}}}}}", v)
    return text
