from transformers import pipeline
import PyPDF2, docx
import torch
device = 0 if torch.cuda.is_available() else -1
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=device)

def read_document(uploaded_file):
    if uploaded_file.type == "application/pdf":
        reader = PyPDF2.PdfReader(uploaded_file)
        text = "".join([page.extract_text() for page in reader.pages])
    else:
        doc = docx.Document(uploaded_file)
        text = " ".join([para.text for para in doc.paragraphs])
    return text

def generate_summary(text):
    return summarizer(text[:1000], max_length=150, min_length=50, do_sample=False)[0]['summary_text']
