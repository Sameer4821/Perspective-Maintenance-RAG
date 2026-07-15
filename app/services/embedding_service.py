from sentence_transformers import SentenceTransformer

class EmbeddingService:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def generate_embeddings(self, chunks):
        return self.model.encode(chunks, convert_to_numpy=True)