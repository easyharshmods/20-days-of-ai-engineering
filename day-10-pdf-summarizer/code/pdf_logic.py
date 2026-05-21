from io import BytesIO


MAX_SUMMARY_CHARACTERS = 6_000


def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    from pypdf import PdfReader

    reader = PdfReader(BytesIO(pdf_bytes))
    page_text: list[str] = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        if text.strip():
            page_text.append(f"[Page {page_number}]\n{text.strip()}")

    return "\n\n".join(page_text).strip()


def truncate_text(text: str, max_characters: int = MAX_SUMMARY_CHARACTERS) -> str:
    cleaned_text = text.strip()

    if len(cleaned_text) <= max_characters:
        return cleaned_text

    return cleaned_text[:max_characters].rstrip() + "\n\n[Document truncated]"


def build_summary_prompt(pdf_text: str) -> str:
    context = truncate_text(pdf_text)

    return (
        "You are summarizing a PDF for a DevOps or cloud engineer.\n"
        "Use only the extracted text below.\n\n"
        "Return:\n"
        "1. A concise executive summary\n"
        "2. Key technical details\n"
        "3. Risks or unknowns\n"
        "4. Recommended next actions\n\n"
        "Extracted PDF text:\n"
        "-----\n"
        f"{context}\n"
        "-----"
    )
