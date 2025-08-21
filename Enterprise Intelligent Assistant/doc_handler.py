# doc_handler.py

import streamlit as st
from modules import summarizer, keyword_extractor

def doc_ui():
    st.header("📂 Document Assistant")

    uploaded_file = st.file_uploader("Upload a document (PDF/DOCX)", type=["pdf", "docx"])

    if uploaded_file:
        # Read document text
        text = summarizer.read_document(uploaded_file)
        st.success("✅ Document uploaded and processed!")

        # Summarization section
        with st.expander("📑 Summarization"):
            if st.button("Generate Summary"):
                summary = summarizer.generate_summary(text)
                st.write(summary)

        # Keyword extraction section
        with st.expander("🔑 Keyword Extraction"):
            if st.button("Extract Keywords"):
                keywords = keyword_extractor.extract_keywords(text)
                st.write(keywords)
