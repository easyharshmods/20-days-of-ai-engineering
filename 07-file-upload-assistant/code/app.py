import requests
import streamlit as st
st.title("File Upload Assistant")
file=st.file_uploader("Upload text",type=["txt"])
question=st.text_input("Question","What is the likely cause?")
if file and st.button("Ask"):
    text=file.getvalue().decode("utf-8",errors="replace")
    prompt=f"Use only this document to answer.\n{text}\nQuestion: {question}"
    response=requests.post("http://localhost:11434/api/generate",json={"model":"llama3.2:3b","prompt":prompt,"stream":False},timeout=90)
    response.raise_for_status()
    st.write(response.json()["response"])
