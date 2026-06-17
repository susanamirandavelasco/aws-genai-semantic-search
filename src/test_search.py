from embedding_service import generate_embedding
from vector_store import search

#query = "What is Amazon Bedrock?"
#query = "What are foundation models?"
#query = "What are Knowledge Bases?"
query = "What is Oaxaca cheese?"

query_embedding = generate_embedding(query)

results = search(
    query_embedding,
    n_results=3
)

print(query)
print(results)
#print("\nResultado 1:\n")
#print(results["documents"][0][0])
#print("\nResultado 2:\n")
#print(results["documents"][0][1])