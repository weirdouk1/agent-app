from app.llm.azure_openai import generate_response


def route_query(user_input):
  prompt = f"""
Decide how to answer this query:

Options:
- sql → structured DB
- vector → semantic search
- hybrid → both

Query:
{user_input}

Return ONLY one word.
"""

  route = generate_response(prompt).strip().lower()

  if route not in ["sql", "vector", "hybrid"]:
    route = "hybrid"

  return route