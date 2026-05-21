import streamlit as st

from llm_client import DEFAULT_MODEL, EMBEDDING_MODEL, LocalLlmError, embed_text, generate_answer
from rag_logic import build_rag_prompt, chunk_text, retrieve


def main() -> None:
    st.set_page_config(page_title="Local RAG Assistant", layout="wide")
    st.title("Local RAG Assistant")
    st.caption(f"Generation: `{DEFAULT_MODEL}` | Embeddings: `{EMBEDDING_MODEL}`")

    uploaded_file = st.file_uploader("Upload a UTF-8 text file", type=["txt"])
    question = st.text_input("Question", "Why do retries need backoff?")

    if uploaded_file is None:
        st.info("Try `sample/platform_notes.txt`.")
        return

    document_text = uploaded_file.getvalue().decode("utf-8", errors="replace")

    if st.button("Run local RAG", type="primary"):
        try:
            with st.spinner("Chunking, embedding, retrieving, and generating..."):
                chunks = chunk_text(document_text)
                embedded_chunks = [
                    {**chunk, "embedding": embed_text(chunk["text"])}
                    for chunk in chunks
                ]
                retrieved = retrieve(embed_text(question), embedded_chunks)
                answer = generate_answer(build_rag_prompt(question, retrieved))
        except LocalLlmError as error:
            st.error(str(error))
            return

        st.subheader("Answer")
        st.write(answer)
        st.subheader("Retrieved chunks")
        for item in retrieved:
            st.write(f"{item['id']} | score={item['score']:.3f}")
            st.caption(item["text"])


if __name__ == "__main__":
    main()
