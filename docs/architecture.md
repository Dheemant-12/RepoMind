# RepoMind Architecture

## Overview

RepoMind is an AI-powered repository understanding system that combines
static code analysis, semantic search, retrieval-augmented generation (RAG),
and large language models to answer questions about source code.

---

## High-Level Pipeline

GitHub Repository
        │
        ▼
 Repository Cloning
        │
        ▼
 AST Parsing
        │
        ▼
 Function / Class Extraction
        │
        ▼
 Knowledge Graph
        │
        ▼
 ChromaDB Vector Store
        │
        ▼
 Hybrid Retrieval
        │
        ▼
 Context Builder
        │
        ▼
 NVIDIA LLM
        │
        ▼
 Natural Language Answer

---

## Project Modules

### ingestion/
Responsible for repository cloning, AST parsing, function extraction, class extraction, import extraction, and call extraction.

### graph/
Builds and manages the repository knowledge graph.

### vector/
Creates embeddings and performs semantic retrieval using ChromaDB.

### llm/
Handles context building, conversation memory, prompt generation, and NVIDIA LLM interaction.

### api/
Provides FastAPI endpoints for interacting with RepoMind.

### analysis/
Contains repository health reports, metrics, and statistics.

---

## Technologies Used

- Python
- FastAPI
- ChromaDB
- Sentence Transformers
- GitPython
- NVIDIA API
- OpenAI SDK
- Pydantic

---

## Future Improvements

- Neo4j Integration
- Docker Deployment
- React Frontend
- Authentication
- Multi-language Support
- Incremental Repository Indexing