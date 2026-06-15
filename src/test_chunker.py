from document_loader import load_pdf_pages
from chunker import chunk_text

text = load_pdf_pages(
    "data/aws_docs/bedrock-ug.pdf",
    start_page=21, #the first 21 pages are index
    end_page=26
)

chunks = chunk_text(text)

print(f"Total chunks: {len(chunks)}")

print(f"Palabras chunk 0: {len(chunks[0].split())}")

print(f"Caracteres chunk 0: {len(chunks[0])}")

for i in range(2):
    print("\n")
    print("=" * 80)
    print(f"CHUNK {i}")
    print("=" * 80)
    print(chunks[i][:500])

