import streamlit as st

from document_logic import build_document_prompt, extract_text_from_pdf
from document_logic import extract_text_from_txt, truncate_context
from llm_client import DEFAULT_MODEL, LocalLlmError, generate_answer


def main() -> None:
    st.set_page_config(page_title="Local Document Assistant", layout="wide")
    st.title("Local Document Assistant")
    st.caption(f"Local document Q&A with `{DEFAULT_MODEL}`")

    uploaded_file = st.file_uploader("Upload `.txt` or text-based `.pdf`", type=["txt", "pdf"])
    mode = st.selectbox("Mode", ["answer question", "summarize", "find risks", "extract actions"])
    question = st.text_input("Question", "What should the on-call engineer do first?")

    if uploaded_file is None:
        st.info("Try `sample/ops_runbook.txt`.")
        return

    if uploaded_file.name.lower().endswith(".pdf"):
        document_text = extract_text_from_pdf(uploaded_file.getvalue())
    else:
        document_text = extract_text_from_txt(uploaded_file.getvalue())

    if not document_text:
        st.warning("No extractable text found.")
        return

    st.text_area("Document preview", truncate_context(document_text, 2_000), height=260)

    if st.button("Ask document assistant", type="primary"):
        prompt = build_document_prompt(document_text, question, mode)
        with st.spinner("Calling local Ollama..."):
            try:
                answer = generate_answer(prompt)
            except LocalLlmError as error:
                st.error(str(error))
                return
        st.subheader("Answer")
        st.write(answer)

    st.caption("Uploaded files can contain sensitive data. This local demo does not persist uploads.")


if __name__ == "__main__":
    main()
