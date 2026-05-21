from typing import Any, TypedDict


class Chunk(TypedDict):
    id: str
    text: str
    metadata: dict[str, Any]


class EmbeddedChunk(Chunk):
    embedding: list[float]


def chunk_text(text: str, chunk_size_words: int = 60, overlap_words: int = 10) -> list[Chunk]:
    words = text.split()
    chunks: list[Chunk] = []
    start = 0
    index = 0
    while start < len(words):
        end = min(start + chunk_size_words, len(words))
        chunks.append(
            {
                "id": f"chunk-{index}",
                "text": " ".join(words[start:end]),
                "metadata": {"chunk_index": index},
            }
        )
        if end == len(words):
            break
        start = end - overlap_words
        index += 1
    return chunks


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


def retrieve(query_embedding: list[float], chunks: list[EmbeddedChunk], top_k: int = 3) -> list[dict[str, Any]]:
    scored = [
        {
            "id": chunk["id"],
            "text": chunk["text"],
            "metadata": chunk["metadata"],
            "score": cosine_similarity(query_embedding, chunk["embedding"]),
        }
        for chunk in chunks
    ]
    return sorted(scored, key=lambda item: item["score"], reverse=True)[:top_k]


def build_rag_prompt(question: str, retrieved_chunks: list[dict[str, Any]]) -> str:
    context = "\n\n".join(
        f"Source {item['id']} (score {item['score']:.3f}):\n{item['text']}"
        for item in retrieved_chunks
    )
    return (
        "Answer using only the retrieved context. If the context is insufficient, say so.\n\n"
        f"Retrieved context:\n{context}\n\n"
        f"Question: {question.strip()}\n"
        "Answer with source-aware practical guidance."
    )
