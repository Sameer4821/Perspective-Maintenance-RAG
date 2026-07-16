import chromadb
from app.services.embedding_service import EmbeddingService


class VectorStore:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(
            name="maintenance_manuals"
        )
        self.embedding_service = EmbeddingService()

    def add_documents(self, chunks):
        embeddings = self.embedding_service.generate_embeddings(chunks)

        ids = [f"doc_{i}" for i in range(len(chunks))]

        # Metadata for each chunk
        metadatas = [
            {
                "source": "sample_manual.pdf",
                "chunk_id": i
            }
            for i in range(len(chunks))
        ]

        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings.tolist(),
            metadatas=metadatas
        )

    def search(self, query, top_k=3):
        query_embedding = self.embedding_service.generate_embeddings([query])[0]

        results = self.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=top_k
        )

        return results