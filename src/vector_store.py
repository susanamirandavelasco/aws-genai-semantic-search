import chromadb


def get_collection():

    client = chromadb.PersistentClient(
        path="./chroma_db"
    )

    collection = client.get_or_create_collection(
        name="bedrock_docs"
    )

    return collection

def add_chunk(
    chunk_id: str,
    chunk_text: str,
    embedding: list[float]
):

    collection = get_collection()

    collection.add(
        ids=[chunk_id],
        documents=[chunk_text],
        embeddings=[embedding]
    )

def count_chunks():

    collection = get_collection()

    return collection.count()

def search(
    query_embedding,
    n_results=3
):

    collection = get_collection()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results