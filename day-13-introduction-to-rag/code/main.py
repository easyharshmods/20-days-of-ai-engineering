from pathlib import Path
import json

from llm_client import generate_answer
from retrieval import build_rag_prompt, retrieve_documents


def main() -> None:
    documents = json.loads(Path("sample/knowledge_base.json").read_text(encoding="utf-8"))
    query = "How should we roll back a bad deployment?"
    retrieved = retrieve_documents(query, documents)
    prompt = build_rag_prompt(query, retrieved)
    print(generate_answer(prompt))


if __name__ == "__main__":
    main()
