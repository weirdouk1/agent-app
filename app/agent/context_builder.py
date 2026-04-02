def build_context(user_input, history):
  context = ""

  for h in history:
    context += f"User: {h['query']}\n"
    context += f"Assistant: {h['response']}\n"

  context += f"\nCurrent Question: {user_input}"

  return context