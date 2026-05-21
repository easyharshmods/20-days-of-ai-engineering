from embeddings import get_embedding, rank_by_similarity


NOTES = [
    "Retries should use exponential backoff during downstream failures.",
    "Cloud cost reviews should inspect idle compute and storage lifecycle rules.",
    "Rollback procedures should identify the previous stable deployment.",
]


def main() -> None:
    query = "How do we avoid retry storms?"
    query_embedding = get_embedding(query)
    items = [
        {"text": note, "embedding": get_embedding(note)}
        for note in NOTES
    ]

    print(f"Query: {query}")
    for result in rank_by_similarity(query_embedding, items):
        print(f"{result['score']:.3f} | {result['text']}")


if __name__ == "__main__":
    main()
