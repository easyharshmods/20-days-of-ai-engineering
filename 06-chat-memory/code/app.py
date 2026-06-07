import requests
import streamlit as st
st.title("AI Assistant with Memory")
if "messages" not in st.session_state: st.session_state.messages=[]
for m in st.session_state.messages: st.chat_message(m["role"]).write(m["content"])
msg=st.chat_input("Ask a follow-up")
if msg:
    st.session_state.messages.append({"role":"user","content":msg})
    history="\n".join(f"{m['role']}: {m['content']}" for m in st.session_state.messages[-6:])
    response=requests.post("http://localhost:11434/api/generate",json={"model":"llama3.2:3b","prompt":history,"stream":False},timeout=60)
    response.raise_for_status()
    st.session_state.messages.append({"role":"assistant","content":response.json()["response"]})
    st.rerun()
