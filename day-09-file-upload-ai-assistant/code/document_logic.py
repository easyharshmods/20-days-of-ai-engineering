MAX_CONTEXT_CHARACTERS = 4_000


def decode_uploaded_text(file_bytes: bytes) -> str:
    return file_bytes.decode("utf-8", errors="replace")


def clean_text(text: str) -> str:
    lines = [line.rstrip() for line in text.splitlines()]
    return "\n".join(lines).strip()


def truncate_context(text: str, max_characters: int = MAX_CONTEXT_CHARACTERS) -> str:
    cleaned_text = clean_text(text)

    if len(cleaned_text) <= max_characters:
        return cleaned_text

    return cleaned_text[:max_characters].rstrip() + "\n\n[Document truncated]"


def build_document_question_prompt(document_text: str, question: str) -> str:
    context = truncate_context(document_text)

    return (
        "You are answering questions about an uploaded text file.\n"
        "Use only the document context below. If the answer is not in the "
        "document, say that the document does not provide enough information.\n\n"
        "Document context:\n"
        "-----\n"
        f"{context}\n"
        "-----\n\n"
        f"Question: {question.strip()}\n\n"
        "Answer clearly and cite the relevant part of the document in plain words."
    )
