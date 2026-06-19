# Semantic Search with AWS Bedrock Documentation (GenAI Project)

## Overview

This project implements a **semantic search engine** over AWS Bedrock documentation using **OpenAI embeddings** and **ChromaDB as a vector database**.

Instead of keyword-based search, it allows querying the documentation using natural language and retrieves the most semantically relevant text chunks.

---

## Objective

Build a minimal end-to-end **Retrieval system (R in RAG)** to understand:

- How embeddings represent text
- How vector similarity search works
- How chunking affects retrieval quality
- How semantic ranking behaves in practice

---

## Architecture

```text
AWS Bedrock PDF
        │
        ▼
 Document Loader
        │
        ▼
    Chunking
 (500-word chunks)
        │
        ▼
 OpenAI Embeddings
        │
        ▼
     ChromaDB
  (Vector Store)
        │
        ▼
 Semantic Search
        │
        ▼
 Top-K Results
 + Metadata
```

The system follows a Retrieval pipeline:

1. Extract text from AWS Bedrock documentation.
2. Split content into chunks.
3. Generate embeddings using OpenAI.
4. Store vectors in ChromaDB.
5. Convert user queries into embeddings.
6. Retrieve the most semantically similar chunks.


---

## Tech Stack

- Python 3.10+
- OpenAI API (text embeddings)
- ChromaDB (vector database)
- PyPDF / PDF parsing library
- NumPy (similarity calculations)

---

## Features

- Load and process large PDF documents
- Split text into semantic chunks
- Generate embeddings using OpenAI
- Store embeddings in ChromaDB
- Perform semantic search over documentation
- Return ranked results based on vector similarity
- Include metadata for traceability (source, chunk id)

---

## Project Structure

```

src/
document_loader.py
chunker.py
embedding_service.py
vector_store.py
search_service.py

scripts/
index_documents.py
search_demo.py

tests/
(test scripts for validation)

data/
bedrock-ug.pdf

chroma_db/

```
---

## How to Run

1. Install dependencies
pip install -r requirements.txt

2. Index documents
python scripts/index_documents.py

This will:

Read the PDF
Create chunks
Generate embeddings
Store vectors in ChromaDB

3. Run semantic search
python scripts/search_demo.py

Example queries:

- What is Amazon Bedrock?
- What are Knowledge Bases?
- What is multimodal content?
- How does retrieval work?

---

## Key Learnings

- Embeddings represent meaning, not keywords
- Vector similarity enables semantic search
- Chunking strategy affects retrieval quality
- Not all queries will return relevant results (no thresholding yet)
- Ranking depends on distance in embedding space
- Corpus quality directly impacts retrieval quality

## Known Limitations

- No relevance threshold (irrelevant queries still return closest chunks)
- Chunking is fixed-size (no overlap strategy yet)
- No LLM-based answer generation (pure retrieval system)
- Limited evaluation of retrieval quality

## Next Steps (Future Work)
- Add relevance threshold filtering
- Improve chunking strategy (overlap / semantic chunking)
- Add LLM layer (RAG system)
- Improve metadata granularity (page-level tracking)
- Build simple UI (optional)

---

## Author Notes

This project was built as a hands-on exploration of:
embeddings, vector databases, and semantic search fundamentals

The goal was to deeply understand how retrieval systems work under the hood before building full RAG pipelines.
