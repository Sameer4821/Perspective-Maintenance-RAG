from pydantic import BaseModel


class TelemetryRequest(BaseModel):
    machine_id: str
    error_code: str
    temperature: float
    vibration: str