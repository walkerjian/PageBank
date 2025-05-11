from sentence_transformers import SentenceTransformer
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_texts(texts):
    return model.encode(texts)

def search(query, docs, top_k=3):
    doc_embeddings = embed_texts(docs)
    query_embedding = embed_texts([query])
    sims = cosine_similarity(query_embedding, doc_embeddings)[0]
    ranked_indices = np.argsort(sims)[::-1][:top_k]
    return [(docs[i], sims[i]) for i in ranked_indices]
