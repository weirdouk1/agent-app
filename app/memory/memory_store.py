import json
import os
from app.config import LOG_PATH
from app.retrieval.chroma_db import add_doc


def save_memory(entry):
  try:
    with open(LOG_PATH, "r") as f:
      data = json.load(f)
  except:
    data = []

  data.append(entry)

  with open(LOG_PATH, "w") as f:
    json.dump(data, f, indent=2)
  text = f"User: {entry['query']} | Assistant: {entry['response']}"
  add_doc(text, str(len(data)))


def load_memory():
  try:
    if not os.path.exists(LOG_PATH):
      return []

    with open(LOG_PATH, "r") as f:
      return json.load(f)
  except:
    return []