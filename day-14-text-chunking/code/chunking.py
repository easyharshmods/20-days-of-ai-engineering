from typing import TypedDict


class TextChunk(TypedDict):
    chunk_id: str
    source: str
    chunk_index: int
    text: str
    word_count: int


def chunk_text(
    text: str,
    source: str,
    chunk_size_words: int = 40,
    overlap_words: int = 8,
) -> list[TextChunk]:
    if chunk_size_words <= 0:
        raise ValueError("chunk_size_words must be positive")
    if overlap_words < 0 or overlap_words >= chunk_size_words:
        raise ValueError("overlap_words must be less than chunk_size_words")

    words = text.split()
    chunks: list[TextChunk] = []
    start = 0
    chunk_index = 0

    while start < len(words):
        end = min(start + chunk_size_words, len(words))
        chunk_words = words[start:end]
        chunks.append(
            {
                "chunk_id": f"{source}:{chunk_index}",
                "source": source,
                "chunk_index": chunk_index,
                "text": " ".join(chunk_words),
                "word_count": len(chunk_words),
            }
        )
        if end == len(words):
            break
        start = end - overlap_words
        chunk_index += 1

    return chunks
