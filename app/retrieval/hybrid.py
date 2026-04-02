from app.retrieval.chroma_db import query_doc
from app.retrieval.sql_db import run_query

def hybrid_search(query, sql_query=None):
  vector = query_doc(query)
  structured = run_query(sql_query) if sql_query else []

  return {
    "vector": vector,
    "structured": structured
  }