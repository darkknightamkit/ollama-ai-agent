from openai import OpenAI
from dotenv import load_dotenv
import os
import numpy

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

def get_embeddings(text):
    response = client.embeddings.create(
        model=os.getenv("EMBED_MODEL"),
        input= text,
    )
    return response.data[0].embedding


def cosine_similarity(A,B):
    dot_prod = numpy.dot(A,B)
    norm_a = numpy.linalg.norm(A)
    norm_b = numpy.linalg.norm(B)
    return dot_prod / (norm_a * norm_b)


text1 = "Python is a programming language"
text2 = "python is programming laguage suitable for the ai world"
text3 = "I love to sleep and eat"

embedding1 = get_embeddings(text1)
embedding2 = get_embeddings(text2)
embedding3 = get_embeddings(text3)

similarity1_2 = cosine_similarity(embedding1, embedding2)
similarity1_3 = cosine_similarity(embedding1, embedding3)

print(f"Similarity between text1 and text2: {similarity1_2}")
print(f"Similarity between text1 and text3: {similarity1_3}")