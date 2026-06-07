import requests
import streamlit as st
st.title("Local AI Chat App")
question = st.text_input("Question", "Why do retries need backoff?")
if st.button("Ask"):
    response = requests.post("http://localhost:11434/api/generate", json={"model":"llama3.2:3b","prompt":question,"stream":False}, timeout=60)
    response.raise_for_status()
    st.write(response.json()["response"])
