import chromadb
from app.llm.embeddings import get_embedding

client = chromadb.PersistentClient(path="./chroma_store")
collection = client.get_or_create_collection("docs")

def add_doc(text, id):
    emb = get_embedding(text)
    collection.add(documents=[text], embeddings=[emb], ids=[id])

def query_doc(query):
    emb = get_embedding(query)
    return collection.query(query_embeddings=[emb], n_results=2)