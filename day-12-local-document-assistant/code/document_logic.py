from io import BytesIO


MAX_CONTEXT_CHARACTERS = 6_000


def extract_text_from_txt(file_bytes: bytes) -> str:
    return file_bytes.decode("utf-8", errors="replace").strip()


def extract_text_from_pdf(file_bytes: bytes) -> str:
    from pypdf import PdfReader

    reader = PdfReader(BytesIO(file_bytes))
    pages = []
    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        if text.strip():
            pages.append(f"[Page {page_number}]\n{text.strip()}")
    return "\n\n".join(pages).strip()


def truncate_context(text: str, max_characters: int = MAX_CONTEXT_CHARACTERS) -> str:
    cleaned = text.strip()
    if len(cleaned) <= max_characters:
        return cleaned
    return cleaned[:max_characters].rstrip() + "\n\n[Document truncated]"


def build_document_prompt(document_text: str, question: str, mode: str) -> str:
    return (
        "You are a local document assistant for DevOps and cloud engineers.\n"
        f"Mode: {mode}\n"
        "Use only the document context. If context is insufficient, say so.\n\n"
        "Document context:\n"
        "-----\n"
        f"{truncate_context(document_text)}\n"
        "-----\n\n"
        f"Question: {question.strip()}\n"
        "Answer with practical engineering detail."
    )
