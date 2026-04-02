from openai import AzureOpenAI
from app.config import *

client = AzureOpenAI(
    api_key=AZURE_KEY,
    api_version="2024-02-15-preview",
    azure_endpoint=AZURE_ENDPOINT
)

def generate_response(prompt):
    response = client.chat.completions.create(
        model=DEPLOYMENT,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content