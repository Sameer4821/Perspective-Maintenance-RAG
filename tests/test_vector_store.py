from app.services.vector_store import VectorStore

chunks = [
    "Lubricate the motor every 500 operating hours.",
    "Replace the air filter every 1000 operating hours.",
    "Inspect the gearbox monthly for wear."
]

store = VectorStore()

store.add_documents(chunks)

results = store.search("When should I lubricate the motor?")

print(results)