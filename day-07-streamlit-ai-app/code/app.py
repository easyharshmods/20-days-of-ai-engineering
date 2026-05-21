import streamlit as st

from llm_client import DEFAULT_MODEL, LocalLlmError, build_prompt, generate_answer


def main() -> None:
    st.set_page_config(page_title="Local AI Engineering Assistant", layout="centered")

    st.title("Local AI Engineering Assistant")
    st.caption(f"Running locally with Ollama model `{DEFAULT_MODEL}`")

    topic = st.text_input(
        "Engineering topic",
        value="why API retries need backoff",
        placeholder="Example: why API retries need backoff",
    )
    style = st.selectbox(
        "Response style",
        options=[
            "three practical bullets",
            "short incident-review explanation",
            "beginner-friendly analogy",
        ],
    )

    if st.button("Generate explanation", type="primary"):
        if not topic.strip():
            st.warning("Enter a topic first.")
            return

        prompt = build_prompt(topic, style)

        with st.spinner("Calling local Ollama..."):
            try:
                answer = generate_answer(prompt)
            except LocalLlmError as error:
                st.error(str(error))
                return

        st.subheader("Answer")
        st.write(answer)

    st.divider()
    st.caption(
        "Local-only demo: prompts are sent to Ollama on this machine. "
        "Review sensitive data handling before using this pattern in production."
    )


if __name__ == "__main__":
    main()
