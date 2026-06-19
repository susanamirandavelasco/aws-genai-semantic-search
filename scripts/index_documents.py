from src.document_loader import load_pdf_pages
from src.chunker import chunk_text
from src.embedding_service import generate_embedding
from src.vector_store import add_chunk

print("Leyendo PDF...")

text = load_pdf_pages(
    "data/aws_docs/bedrock-ug.pdf",
    start_page=2500,
    end_page=2900
)

print("Generando chunks...")

chunks = chunk_text(text)

print(f"Chunks generados: {len(chunks)}")

for index, chunk in enumerate(chunks):

    print(f"Procesando chunk {index}")

    embedding = generate_embedding(chunk)

    add_chunk(
        chunk_id=f"chunk_{index}",
        chunk_text=chunk,
        embedding=embedding,
        metadata = {
            "source": "bedrock-ug.pdf",
            "chunk_number": index,
            "page_range": "2500-2900"
        }
    )

print("Indexación completada")