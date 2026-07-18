# Perspective-Maintenance-RAG

## Project Overview

This project aims to build a Retrieval-Augmented Generation (RAG) system tailored for industrial equipment maintenance. By using technical manuals as a knowledge base, the system will provide intelligent, context-aware answers to maintenance-related queries, helping technicians troubleshoot problems and perform procedures more efficiently.

## Project Structure

The project is organized as follows:

```
data/
├── chunks/
│   ├── centrifugal_pump_CP500_manual_chunks.json
│   └── electric_motor_IM400_manual_chunks.json
├── manuals/
│   ├── centrifugal_pump_CP500_manual.txt
│   └── electric_motor_IM400_manual.txt
└── parsed/
    ├── centrifugal_pump_CP500_manual.md
    └── electric_motor_IM400_manual.md
```

-   `data/manuals`: Contains the raw, original maintenance manuals in `.txt` format.
-   `data/parsed`: Contains the manuals after being parsed into a structured Markdown (`.md`) format.
-   `data/chunks`: Contains the parsed manuals broken down into smaller JSON objects (chunks), which is a key step for the RAG embedding and retrieval process.

## Week 1 Progress

The first week focused on establishing the foundational data processing pipeline for the RAG system.

-   **Data Sourcing**: Acquired two representative maintenance manuals: one for a centrifugal pump (CP-500 series) and one for a three-phase induction motor (IM-400 series).
-   **Data Parsing and Structuring**: Converted the raw text manuals into a clean, structured Markdown format. This step makes the documents easier to process for downstream tasks.
-   **Data Chunking**: Implemented a strategy to segment the structured documents into smaller, semantically coherent chunks. These chunks, saved as JSON files, will be used to create vector embeddings for the retrieval model.
-   **Repository Setup**: Initialized the project repository with the current directory structure and data assets.
