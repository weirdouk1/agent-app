from sqlalchemy import create_engine, text
from app.config import SQL_DB

engine = create_engine(SQL_DB)
def run_query(q):
  try:
    with engine.connect() as conn:
      result = conn.execute(text(q))
      return [dict(row._mapping) for row in result]
  except Exception as e:
    return {"error": str(e)}