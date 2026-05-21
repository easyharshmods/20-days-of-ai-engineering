from typing import Any


EMBEDDING_MODEL = "nomic-embed-text"
OLLAMA_EMBED_URL = "http://localhost:11434/api/embeddings"


def cosine_similarity(left: list[float], right: list[float]) -> float:
    try:
        import numpy as np

        left_vector = np.array(left, dtype=float)
        right_vector = np.array(right, dtype=float)
        denominator = np.linalg.norm(left_vector) * np.linalg.norm(right_vector)
        if denominator == 0:
            return 0.0
        return float(np.dot(left_vector, right_vector) / denominator)
    except ModuleNotFoundError:
        pass

    dot_product = sum(left_value * right_value for left_value, right_value in zip(left, right))
    left_norm = sum(value * value for value in left) ** 0.5
    right_norm = sum(value * value for value in right) ** 0.5
    denominator = left_norm * right_norm
    if denominator == 0:
        return 0.0
    return dot_product / denominator


def build_embedding_payload(text: str) -> dict[str, Any]:
    return {"model": EMBEDDING_MODEL, "prompt": text}


def get_embedding(text: str) -> list[float]:
    import requests

    response = requests.post(
        OLLAMA_EMBED_URL,
        json=build_embedding_payload(text),
        timeout=60,
    )
    response.raise_for_status()
    return response.json()["embedding"]


def rank_by_similarity(query_embedding: list[float], items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    ranked = []
    for item in items:
        ranked.append(
            {
                "text": item["text"],
                "score": cosine_similarity(query_embedding, item["embedding"]),
            }
        )
    return sorted(ranked, key=lambda item: item["score"], reverse=True)
