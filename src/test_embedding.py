from embedding_service import generate_embedding

text = """
Amazon Bedrock is a fully managed service
that provides access to foundation models.
"""

embedding = generate_embedding(text)

print(type(embedding))

print(f"Dimensiones: {len(embedding)}")

print("\nPrimeros 10 valores:\n")

print(embedding[:10])