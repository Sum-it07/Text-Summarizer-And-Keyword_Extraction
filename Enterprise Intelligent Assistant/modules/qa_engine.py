from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")
documents = ["Company policies on leave", "Code of conduct", "Workplace safety rules"]

def answer_query(query):
    query_emb = model.encode(query, convert_to_tensor=True)
    doc_embs = model.encode(documents, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(query_emb, doc_embs)
    best_doc = documents[scores.argmax()]
    return f"Most relevant doc: {best_doc}"
