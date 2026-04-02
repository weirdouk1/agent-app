import os
from dotenv import load_dotenv

load_dotenv()

AZURE_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")
EMBEDDING_DEPLOYMENT = os.getenv("AZURE_EMBEDDING_DEPLOYMENT")

SQL_DB = os.getenv("SQLITE_DB_PATH")
LOG_PATH = os.getenv("LOG_PATH")