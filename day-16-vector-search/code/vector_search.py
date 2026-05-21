from typing import Any, TypedDict


EMBEDDING_MODEL = "nomic-embed-text"
OLLAMA_EMBED_URL = "http://localhost:11434/api/embeddings"


class VectorRecord(TypedDict):
    id: str
    text: str
    metadata: dict[str, Any]
    embedding: list[float]


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


def embed_text(text: str) -> list[float]:
    import requests

    response = requests.post(
        OLLAMA_EMBED_URL,
        json={"model": EMBEDDING_MODEL, "prompt": text},
        timeout=60,
    )
    response.raise_for_status()
    return response.json()["embedding"]


def search_vectors(query_embedding: list[float], records: list[VectorRecord], top_k: int = 2) -> list[dict[str, Any]]:
    scored = [
        {
            "id": record["id"],
            "text": record["text"],
            "metadata": record["metadata"],
            "score": cosine_similarity(query_embedding, record["embedding"]),
        }
        for record in records
    ]
    return sorted(scored, key=lambda item: item["score"], reverse=True)[:top_k]
