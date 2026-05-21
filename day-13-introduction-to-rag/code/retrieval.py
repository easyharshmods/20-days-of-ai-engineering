import re
from typing import Any


def tokenize(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def score_document(query: str, document: dict[str, Any]) -> int:
    query_tokens = tokenize(query)
    document_tokens = tokenize(f"{document['title']} {document['text']}")
    return len(query_tokens.intersection(document_tokens))


def retrieve_documents(
    query: str,
    documents: list[dict[str, Any]],
    top_k: int = 2,
) -> list[dict[str, Any]]:
    scored = [
        (score_document(query, document), document)
        for document in documents
    ]
    ranked = sorted(scored, key=lambda item: item[0], reverse=True)
    return [document for score, document in ranked[:top_k] if score > 0]


def build_rag_prompt(query: str, documents: list[dict[str, Any]]) -> str:
    context = "\n\n".join(
        f"Source: {document['title']}\n{document['text']}"
        for document in documents
    )
    return (
        "Answer the question using only the retrieved context.\n\n"
        f"Retrieved context:\n{context}\n\n"
        f"Question: {query}\n"
        "Answer with source-aware reasoning."
    )
