from pathlib import Path

from chunking import chunk_text


def main() -> None:
    text = Path("sample/runbook.txt").read_text(encoding="utf-8")
    chunks = chunk_text(text, source="runbook", chunk_size_words=35, overlap_words=7)

    for chunk in chunks:
        preview = chunk["text"][:90]
        print(f"{chunk['chunk_id']} | words={chunk['word_count']} | {preview}")


if __name__ == "__main__":
    main()
