from app.llm.azure_openai import generate_response


def detect_intent(user_input):
  prompt = f"""
Classify the intent of the user query.

Query: {user_input}

Possible intents:
- lookup (retrieve records)
- aggregation (max, avg, count)
- filtering (specific condition)
- general (non-database question)

Return ONLY one word.
"""

  intent = generate_response(prompt).strip().lower()

  # safety fallback
  if intent not in ["lookup", "aggregation", "filtering", "general"]:
    intent = "general"

  return intent