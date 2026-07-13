from fastapi import FastAPI

app = FastAPI(
    title="Perspective Maintenance RAG",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Perspective Maintenance RAG API is running!"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }