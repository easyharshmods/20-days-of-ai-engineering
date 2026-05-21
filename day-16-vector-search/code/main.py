from vector_search import VectorRecord, embed_text, search_vectors


CHUNKS = [
    {"id": "retry:0", "text": "Retries should use backoff and jitter.", "metadata": {"source": "retry-runbook"}},
    {"id": "cost:0", "text": "Cost reviews inspect idle compute.", "metadata": {"source": "cost-runbook"}},
    {"id": "rollback:0", "text": "Rollback deploys the previous stable version.", "metadata": {"source": "rollback-runbook"}},
]


def main() -> None:
    records: list[VectorRecord] = [
        {
            "id": chunk["id"],
            "text": chunk["text"],
            "metadata": chunk["metadata"],
            "embedding": embed_text(chunk["text"]),
        }
        for chunk in CHUNKS
    ]
    results = search_vectors(embed_text("How do retries avoid overload?"), records)
    for result in results:
        print(f"{result['score']:.3f} | {result['metadata']['source']} | {result['text']}")


if __name__ == "__main__":
    main()
