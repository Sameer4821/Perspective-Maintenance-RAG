from app.services.embedding_service import EmbeddingService

chunks = [
    "The motor should be lubricated every 500 hours.",
    "Replace the filter if pressure exceeds the limit."
]

service = EmbeddingService()

embeddings = service.generate_embeddings(chunks)

print(f"Generated {len(embeddings)} embeddings")
print(f"Embedding dimension: {len(embeddings[0])}")