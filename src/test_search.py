from embedding_service import generate_embedding
from vector_store import search

#query = "What is Amazon Bedrock?"

#query = "What are Knowledge Bases?"
#query = "What is multimodal content?"
query = "How can I choose a multimodal processing approach?"

#query = "What are Agents?"
#query = "What foundation models are available?"
#query = "What is Oaxaca cheese?"

query_embedding = generate_embedding(query)

results = search(
    query_embedding,
    n_results=3
)

print(query)

print("\nRESULTADOS ENCONTRADOS\n")
print(results["ids"])    


for i, doc in enumerate(results["documents"][0]):

    print("=" * 80)

    print(f"RESULTADO {i+1}")
    print(f"DISTANCES: {results["distances"][0][i]}")

    print("=" * 80)

    #print(doc[:500])
    print(doc)

    print("\n")