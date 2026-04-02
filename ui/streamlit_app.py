import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from app.graph.graph_builder import build_graph

st.title("🧠 LangGraph AI Agent")

graph = build_graph()

user_input = st.text_input("Ask something:")

if st.button("Run Agent"):
  if user_input:
    with st.spinner("Thinking..."):

      result = graph.invoke({
        "user_input": user_input
      })

      st.success(result["final_answer"])