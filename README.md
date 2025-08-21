# 📑 Text Summarizer & Keyword Extractor  

An **AI-powered document assistant** that helps users quickly understand long documents by:  
- 📝 **Summarizing** uploaded PDFs/DOCX files into concise text.  
- 🔑 **Extracting keywords** to highlight the most important terms.  
- 🚀 Built with **Streamlit** for an easy-to-use interface.  

---

## ✨ Features  
- Upload **PDF/DOCX** documents.  
- Generate **extractive summaries** (shortened text without losing meaning).  
- Extract **keywords** for quick insights.  
- Interactive **Streamlit web app**.  

---

## 🛠️ Tech Stack  
- **Python 3.9+**  
- **Streamlit** (frontend UI)  
- **NLTK / spaCy / scikit-learn** (text preprocessing)  
- **PyMuPDF / python-docx** (document parsing)  

# Create virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

#Run
streamlit run app.py
