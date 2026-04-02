from typing import TypedDict, List, Dict

class AgentState(TypedDict):
  user_input: str
  intent: str
  context: str
  sql_query: str
  structured_data: List[Dict]
  vector_data: Dict
  final_answer: str