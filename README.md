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

## Dataset

Download the AWS Bedrock User Guide PDF and place it in:

```
data/aws_docs/bedrock-ug.pdf
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
---

## Author Notes

This project was built as a hands-on exploration of:
embeddings, vector databases, and semantic search fundamentals

The goal was to deeply understand how retrieval systems work under the hood before building full RAG pipelines.

## What I Learned

Building this project helped me move from understanding semantic search concepts theoretically to understanding how they work in practice.

### 1. Embeddings represent meaning, not keywords

Before this project, I understood embeddings conceptually.

After implementing the full pipeline, I observed how semantically related questions retrieve similar chunks even when they do not share exact keywords.

### 2. Retrieval quality depends heavily on the corpus

The retrieval system worked correctly even when the results were not useful.

This taught me that retrieval quality is not only about embeddings or vector databases. The quality and relevance of the indexed content are equally important.

### 3. Ranking is based on vector similarity

Different questions often retrieved the same group of chunks, but in a different order.

This helped me understand how semantic ranking works and how small differences in query intent affect retrieval results.

### 4. Chunking is a critical design decision

The way documents are split directly impacts retrieval quality.

Chunk size influences what information is retrieved and how much context is available to downstream systems.

### 5. Vector databases always return the closest match

Even when asking questions completely unrelated to the indexed content, the system still returned results.

This highlighted the need for relevance thresholds and evaluation strategies in production Retrieval and RAG systems.

### 6. Retrieval is the foundation of RAG

Implementing semantic search from scratch provided a much deeper understanding of the Retrieval component that powers modern Retrieval-Augmented Generation (RAG) applications.

---

## Interesting Findings

### The "Oaxaca Cheese" Experiment

When querying:

"What is Oaxaca cheese?"

the system still returned results from the AWS Bedrock documentation.

This was not a bug.

The vector database correctly returned the closest chunks available in the corpus, even though they were not relevant to the question.

This experiment helped me understand why production Retrieval and RAG systems often implement relevance thresholds before returning results to users.
