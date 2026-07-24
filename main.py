from fastapi import FastAPI
from app.routes.telemetry import router as telemetry_router

app = FastAPI(
    title="Prescriptive Maintenance RAG API",
    description="API for industrial maintenance using RAG and IoT telemetry.",
    version="1.0.0"
)

# Health Check Endpoint
@app.get("/")
def root():
    return {
        "message": "Prescriptive Maintenance RAG API is running."
    }

# Register Routes
app.include_router(telemetry_router)