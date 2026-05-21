import streamlit as st

from chat_logic import ChatMessage, build_chat_prompt, create_message
from llm_client import DEFAULT_MODEL, LocalLlmError, generate_answer


def initialize_session() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = [
            create_message(
                "assistant",
                "Ask me a practical AI engineering or cloud engineering question.",
            )
        ]


def render_messages(messages: list[ChatMessage]) -> None:
    for message in messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])


def main() -> None:
    st.set_page_config(page_title="Local Chat Assistant", layout="centered")
    st.title("Local Chat Assistant")
    st.caption(f"Session memory with Ollama model `{DEFAULT_MODEL}`")

    initialize_session()
    render_messages(st.session_state.messages)

    user_message = st.chat_input("Ask about AI engineering, DevOps, or cloud work")

    if user_message:
        st.session_state.messages.append(create_message("user", user_message))

        with st.chat_message("user"):
            st.write(user_message)

        prompt = build_chat_prompt(st.session_state.messages)

        with st.chat_message("assistant"):
            with st.spinner("Thinking locally..."):
                try:
                    answer = generate_answer(prompt)
                except LocalLlmError as error:
                    st.error(str(error))
                    return

            st.write(answer)

        st.session_state.messages.append(create_message("assistant", answer))

    st.caption(
        "Memory is stored only in this Streamlit session. Refreshing the page "
        "or restarting the app clears the conversation."
    )


if __name__ == "__main__":
    main()
