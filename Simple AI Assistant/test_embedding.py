from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

response = client.embeddings.create(
    model=os.getenv("EMBED_MODEL"),
    input=["hello how old are you","I am a good boy","this is going to be crazy"],
)
for i,emp in enumerate(response.data):
     print(f"Embedding {i}: length: {len(emp.embedding)}")  # Print first 5 dimensions of each embedding
     print(emp.embedding[:2])