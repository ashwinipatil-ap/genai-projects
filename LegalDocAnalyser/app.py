import streamlit as st
from dotenv import load_dotenv
import os
from pdf_utils import extract_text_from_pdf
from chunker import chunk_text
from embeddings import get_vector_store
from qa_rag import answer_question
from summarizer import summarize_text

import asyncio

try:
    asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)


load_dotenv()

st.set_page_config(page_title="LegalDoc AI", layout="wide")
st.title("📄 Legal Document Assistant with Gemini + RAG")

# Sidebar - API key input
st.sidebar.header("🔐 Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")
st.session_state["api_key"] = api_key

# File Upload
uploaded_file = st.file_uploader("Upload a legal PDF file", type=["pdf"])
if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())
    text, error = extract_text_from_pdf("temp.pdf")
    if error:
        st.error(f"❌ {error}")
    else:
        st.success("✅ Text extracted successfully.")
        st.text_area("📄 Preview Extracted Text", text[:2000])

        # Chunking
        chunks = chunk_text(text)
        db = get_vector_store(chunks, api_key)
        st.session_state["vector_db"] = db
        st.session_state["chunks"] = chunks

        # Q&A
        st.subheader("💬 Ask a Question")
        question = st.text_input("Enter your legal question")
        if st.button("Get Answer") and question:
            answer = answer_question(question, db, api_key)
            st.markdown(f"**Answer:** {answer}")

        # Summarization
        st.subheader("🧾 Document Summary")
        if st.button("Generate Summary"):
            summary = summarize_text(chunks, api_key)
            st.markdown(f"""**Summary:**
            {summary}""")
