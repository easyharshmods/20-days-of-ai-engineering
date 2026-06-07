from io import BytesIO
import requests
import streamlit as st
from pypdf import PdfReader
st.title("Local PDF Summarizer")
file=st.file_uploader("Upload PDF",type=["pdf"])
if file:
    reader=PdfReader(BytesIO(file.getvalue()))
    text="\n".join((p.extract_text() or "") for p in reader.pages)
    st.text_area("Preview",text[:2000],height=240)
    if st.button("Summarize"):
        prompt=f"Summarize for a DevOps engineer. Include risks and actions.\n{text[:6000]}"
        response=requests.post("http://localhost:11434/api/generate",json={"model":"llama3.2:3b","prompt":prompt,"stream":False},timeout=120)
        response.raise_for_status()
        st.write(response.json()["response"])
