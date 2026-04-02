from langgraph.graph import StateGraph
from app.graph.state import AgentState
from app.graph.nodes import *


def build_graph():

  graph = StateGraph(AgentState)

  # Nodes
  graph.add_node("intent", intent_node)
  graph.add_node("memory_load", memory_node)
  graph.add_node("context", context_node)
  graph.add_node("router", router_node)
  graph.add_node("sql", sql_node)
  graph.add_node("vector", vector_node)
  graph.add_node("reasoning", reasoning_node)
  graph.add_node("summarize", summarizer_node)
  graph.add_node("memory_save", memory_save_node)

  # Entry
  graph.set_entry_point("intent")

  # Flow
  graph.add_edge("intent", "memory_load")
  graph.add_edge("memory_load", "context")
  graph.add_edge("context", "router")

  # 🔥 STRICT ROUTING (NO PARALLEL)
  graph.add_conditional_edges(
    "router",
    route_decider,
    {
      "sql": "sql",
      "vector": "vector",
      "hybrid": "sql"
    }
  )

  # 🔥 SERIAL FLOW (IMPORTANT)
  graph.add_edge("sql", "vector")       # hybrid continues
  graph.add_edge("vector", "reasoning") # everything ends here

  graph.add_edge("reasoning", "summarize")
  graph.add_edge("summarize", "memory_save")

  return graph.compile()