from app.services.document_loader import DocumentLoader

loader = DocumentLoader()

docs = loader.load_documents()

print(f"Loaded {len(docs)} documents")

for d in docs:
    print(d["file_name"])