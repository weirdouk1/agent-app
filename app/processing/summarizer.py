from app.llm.azure_openai import generate_response

def summarize(text):
  prompt = f"""
Clean and format this text properly.

Fix:
- broken numbers (0.99 → correct)
- weird spacing
- symbols issues

Text:
{text}
"""
  return generate_response(prompt)