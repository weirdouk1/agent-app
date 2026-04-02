from app.graph.graph_builder import build_graph

graph = build_graph()


def run_agent(user_input):
  result = graph.invoke({
    "user_input": user_input
  })

  return result["final_answer"]