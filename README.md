# Perspective-Maintenance-RAG
# 🚀 Prescriptive Maintenance RAG Agent

An AI-powered Retrieval-Augmented Generation (RAG) system for industrial maintenance. This project enables maintenance engineers to retrieve relevant repair procedures from equipment manuals using IoT telemetry alerts.

---

## 📌 Project Overview

Industrial equipment continuously generates telemetry data such as error codes, temperature, and vibration levels. Instead of manually searching hundreds of pages in maintenance manuals, this system automatically converts machine alerts into search queries and retrieves the most relevant maintenance instructions.

This project is being developed as part of a Generative AI internship.

---

## 🏗️ Current Features

### ✅ Week 1
- PDF document loading
- PDF text extraction
- Recursive text chunking with overlap
- Sentence Transformer embeddings
- ChromaDB vector database integration
- Semantic similarity search

### ✅ Week 2 (In Progress)
- IoT Telemetry Parser
- FastAPI Telemetry Endpoint
- Automatic search query generation from telemetry alerts

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| FastAPI | REST API Framework |
| ChromaDB | Vector Database |
| Sentence Transformers | Text Embeddings |
| LangChain | Text Chunking |
| PyMuPDF | PDF Parsing |
| Pydantic | Request Validation |

---

## 📂 Project Structure

```text
Perspective-Maintenance-RAG/
│
├── app/
│   ├── models/
│   │   └── telemetry.py
│   │
│   ├── routes/
│   │   └── telemetry.py
│   │
│   ├── services/
│   │   ├── document_loader.py
│   │   ├── pdf_parser.py
│   │   ├── text_chunker.py
│   │   ├── embedding_service.py
│   │   ├── vector_store.py
│   │   └── telemetry_parser.py
│   │
│   └── __init__.py
│
├── data/
│   └── manuals/
│
├── tests/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone <repository-url>
cd Perspective-Maintenance-RAG
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoint

### POST `/telemetry`

Accepts an IoT telemetry alert and generates a maintenance search query.

### Sample Request

```json
{
    "machine_id": "PUMP-01",
    "error_code": "E-404",
    "temperature": 105,
    "vibration": "High"
}
```

### Sample Response

```json
{
    "status": "success",
    "generated_query": "Repair procedure for machine PUMP-01 error code E-404 temperature 105 vibration High"
}
```

---

## 🔄 Current Workflow

```text
Industrial Manual (PDF)
          │
          ▼
Document Loader
          │
          ▼
PDF Parser
          │
          ▼
Text Chunker
          │
          ▼
Embedding Model
          │
          ▼
ChromaDB Vector Store
          ▲
          │
Telemetry API
          │
          ▼
Telemetry Parser
          │
          ▼
Generated Search Query
```

---

## 🚧 Upcoming Features

- Retrieve relevant maintenance manual chunks
- Integrate LLM for prescriptive maintenance recommendations
- Support multiple industrial manuals
- Context-aware RAG responses
- LangGraph workflow integration
- IoT telemetry simulation
- Maintenance recommendation API

---

## 📖 Learning Objectives

This project demonstrates:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases
- FastAPI Backend Development
- Industrial AI Applications
- IoT Data Processing
- Generative AI Workflows

---

## 👩‍💻 Author

**Niharika Yadav**

Computer Science Student | AI & Machine Learning Enthusiast

---

## 📄 License

This project is developed for educational and internship purposes.