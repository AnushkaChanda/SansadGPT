import streamlit as st
from helpers import sansad_gpt

st.set_page_config(page_title="SansadGPT", layout="centered")

st.title("🏛️ SansadGPT")
st.subheader("Indian Parliament Question–Answer Chatbot")

st.write(
    "Ask questions based on Lok Sabha & Rajya Sabha records. "
    "For recent or missing information, the bot automatically searches the internet."
)

query = st.text_input("💬 Ask your question:")

if query:
    with st.spinner("Thinking..."):
        result = sansad_gpt(query)

    st.markdown("### 📌 Answer")
    st.write(result["answer"])

    st.markdown(f"**Source:** {result['source']}")
