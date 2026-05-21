import streamlit as st

from document_logic import build_document_question_prompt, decode_uploaded_text
from document_logic import truncate_context
from llm_client import DEFAULT_MODEL, LocalLlmError, generate_answer


def main() -> None:
    st.set_page_config(page_title="Local File Q&A Assistant", layout="wide")
    st.title("Local File Q&A Assistant")
    st.caption(f"Upload a text file and ask questions with `{DEFAULT_MODEL}`")

    uploaded_file = st.file_uploader("Upload a UTF-8 text file", type=["txt"])

    if uploaded_file is None:
        st.info("Upload a `.txt` file to begin. Try `sample/incident_notes.txt`.")
        return

    document_text = decode_uploaded_text(uploaded_file.getvalue())
    context_preview = truncate_context(document_text, max_characters=1_500)

    left_column, right_column = st.columns([1, 1])

    with left_column:
        st.subheader("Document preview")
        st.text_area("Extracted text", value=context_preview, height=360)

    with right_column:
        st.subheader("Ask a question")
        question = st.text_input(
            "Question",
            value="What caused the elevated errors?",
        )

        if st.button("Ask about this file", type="primary"):
            if not question.strip():
                st.warning("Enter a question first.")
                return

            prompt = build_document_question_prompt(document_text, question)

            with st.spinner("Asking local Ollama..."):
                try:
                    answer = generate_answer(prompt)
                except LocalLlmError as error:
                    st.error(str(error))
                    return

            st.markdown("### Answer")
            st.write(answer)

    st.caption(
        "Local demo: uploaded text is read into memory and sent to local Ollama. "
        "Do not use sensitive files without reviewing production controls."
    )


if __name__ == "__main__":
    main()
