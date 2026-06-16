from embedding_service import generate_embedding
from math import sqrt


def cosine_similarity(v1, v2):

    dot_product = sum(a * b for a, b in zip(v1, v2))

    norm_v1 = sqrt(sum(a * a for a in v1))
    norm_v2 = sqrt(sum(b * b for b in v2))

    return dot_product / (norm_v1 * norm_v2)


text1 = "What is Amazon Bedrock?"

text2 = "Explain Amazon Bedrock."

text3 = "How do I cook pasta?"

text4 = "What foundation models are available in Bedrock?"


embedding1 = generate_embedding(text1)
embedding2 = generate_embedding(text2)
embedding3 = generate_embedding(text3)
embedding4 = generate_embedding(text4)


similarity_12 = cosine_similarity(
    embedding1,
    embedding2
)

similarity_13 = cosine_similarity(
    embedding1,
    embedding3
)

similarity_14 = cosine_similarity(
    embedding1,
    embedding4
)

print(f"text1 vs text2: {similarity_12}")

print(f"text1 vs text3: {similarity_13}")

print(f"text1 vs text4: {similarity_14}")