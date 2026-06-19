from src.document_loader import load_pdf_pages
from src.chunker import chunk_text
from src.embedding_service import generate_embedding
from src.vector_store import add_chunk


text = load_pdf_pages(
    "data/aws_docs/bedrock-ug.pdf",
    start_page=21,
    end_page=26
)

chunks = chunk_text(text)

first_chunk = chunks[0]

embedding = generate_embedding(first_chunk)

add_chunk(
    chunk_id="chunk_1",
    chunk_text=first_chunk,
    embedding=embedding,
    metadata = {
            "source": "bedrock-ug.pdf",
            "page_range": "21-26"
        }
)

print("Chunk guardado correctamente")