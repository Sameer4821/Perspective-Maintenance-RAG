from fastapi import APIRouter
from app.models.telemetry import TelemetryRequest
from app.services.telemetry_parser import TelemetryParser

router = APIRouter()


@router.post("/telemetry")
def receive_telemetry(request: TelemetryRequest):

    query = TelemetryParser.generate_query(request.model_dump())

    return {
        "status": "success",
        "generated_query": query
    }