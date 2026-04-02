from app.llm.azure_openai import generate_response
from app.models.schemas import SCHEMA


def clean_sql(sql):
  return sql.replace("```sql", "").replace("```", "").strip()


def text_to_sql(user_input):
  prompt = f"""
You are an expert SQL generator.

{SCHEMA}

Rules:
- Use correct table and column names
- Select only relevant columns
- Avoid SELECT *
- Limit results to 10 unless asked otherwise
- Return only SQL

User Query:
{user_input}
"""

  return clean_sql(generate_response(prompt))