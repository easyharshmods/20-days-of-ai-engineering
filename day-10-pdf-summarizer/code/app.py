import streamlit as st

from llm_client import DEFAULT_MODEL, LocalLlmError, generate_answer
from pdf_logic import build_summary_prompt, extract_text_from_pdf, truncate_text


def main() -> None:
    st.set_page_config(page_title="Local PDF Summarizer", layout="wide")
    st.title("Local PDF Summarizer")
    st.caption(f"Extract PDF text and summarize locally with `{DEFAULT_MODEL}`")

    uploaded_file = st.file_uploader("Upload a text-based PDF", type=["pdf"])

    if uploaded_file is None:
        st.info("Upload a PDF with embedded text to begin.")
        return

    try:
        pdf_text = extract_text_from_pdf(uploaded_file.getvalue())
    except Exception as error:
        st.error(f"Could not extract text from PDF: {error}")
        return

    if not pdf_text:
        st.warning("No extractable text found. This PDF may require OCR.")
        return

    st.metric("Extracted characters", len(pdf_text))
    st.subheader("Document preview")
    st.text_area("Extracted PDF text", value=truncate_text(pdf_text, 2_000), height=280)

    if st.button("Summarize PDF", type="primary"):
        prompt = build_summary_prompt(pdf_text)

        with st.spinner("Summarizing with local Ollama..."):
            try:
                summary = generate_answer(prompt)
            except LocalLlmError as error:
                st.error(str(error))
                return

        st.subheader("Summary")
        st.write(summary)

    st.caption(
        "Local demo: uploaded PDF bytes are processed in memory. Review file "
        "retention, access, and sensitivity controls before production use."
    )


if __name__ == "__main__":
    main()
