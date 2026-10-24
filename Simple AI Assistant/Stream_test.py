import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

stream =client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[
        {
            "role":"user",
            "content" : "Explain what is api in 100 words no need to mention number of words used"
        }
    ],
    stream=True,
)

full_response = ""

for chunk in stream:
    if not chunk.choices[0]:
        continue
    piece=chunk.choices[0].delta.content
    if piece:
        print(piece,end="",flush=True)
        full_response += piece

print("\nfull response:")
print(full_response)