from app.agent.intent import detect_intent
from app.agent.context_builder import build_context
from app.agent.router import route_query
from app.processing.text2query import text_to_sql, clean_sql
from app.processing.summarizer import summarize
from app.retrieval.sql_db import run_query
from app.retrieval.chroma_db import query_doc
from app.memory.memory_store import save_memory, load_memory
from app.llm.azure_openai import generate_response


def intent_node(state):
  state["intent"] = detect_intent(state["user_input"])
  return state

def memory_node(state):
  history = load_memory()
  state["history"] = history[-5:] if history else []
  return state

def context_node(state):
  history = state.get("history", [])
  state["context"] = build_context(state["user_input"], history)
  return state

def router_node(state):
  state["route"] = route_query(state["user_input"])
  return state

def sql_node(state):
  route = state.get("route", "hybrid")

  if route not in ["sql", "hybrid"]:
    state["structured_data"] = []
    return state

  sql = text_to_sql(state["user_input"])
  state["sql_query"] = sql

  print("🧠 Generated SQL:", sql)   # DEBUG

  # 🚨 BLOCK BAD SQL
  if "sqlite_master" in sql.lower():
    state["structured_data"] = []
    return state

  result = run_query(sql)

  # 🔥 SELF-CORRECT SQL IF ERROR
  if isinstance(result, dict) and "error" in result:
    fix_prompt = f"""
Fix this SQL query.

Query:
{sql}

Error:
{result['error']}

Return ONLY SQL.
"""
    fixed_sql = generate_response(fix_prompt)
    fixed_sql = clean_sql(fixed_sql)

    state["sql_query"] = fixed_sql
    result = run_query(fixed_sql)

  state["structured_data"] = result
  return state

def vector_node(state):
  route = state.get("route", "hybrid")

  if route not in ["vector", "hybrid"]:
    state["vector_data"] = []
    return state

  result = query_doc(state["user_input"])
  state["vector_data"] = result

  return state

def reasoning_node(state):
  data = state.get("structured_data", [])
  user_q = state.get("user_input", "").lower()

  if not data:
    state["final_answer"] = "No relevant data found."
    return state

  prompt = f"""
Answer the user clearly using the data.

Question:
{user_q}

Data:
{data}

Rules:
- Show only useful information
- Keep it concise
- Format cleanly (bullets if needed)
"""

  state["final_answer"] = generate_response(prompt)
  return state

def summarizer_node(state):
  state["final_answer"] = summarize(state["final_answer"])
  return state

def memory_save_node(state):
  save_memory({
    "query": state["user_input"],
    "response": state["final_answer"]
  })

  return state

def merge_node(state):
  # just pass state forward safely
  return state

def route_decider(state):
  return state.get("route", "hybrid")