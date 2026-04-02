from openai import AzureOpenAI
from app.config import *

client = AzureOpenAI(
    api_key=AZURE_KEY,
    api_version="2024-02-15-preview",
    azure_endpoint=AZURE_ENDPOINT
)

def get_embedding(text):
    res = client.embeddings.create(
        model=EMBEDDING_DEPLOYMENT,
        input=text
    )
    return res.data[0].embedding