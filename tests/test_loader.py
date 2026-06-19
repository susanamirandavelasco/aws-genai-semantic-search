from src.document_loader import load_pdf_pages, get_pdf_page_count

PDF_PATH = "data/aws_docs/bedrock-ug.pdf"

print("Leyendo PDF...")

page_count = get_pdf_page_count(PDF_PATH)

print(f"Número de páginas: {page_count}")

text = load_pdf_pages(
    "data//aws_docs/bedrock-ug.pdf",
    start_page=0,
    end_page=20
)

print("\nPrimeros 1000 caracteres:\n")
print(text[:1000])