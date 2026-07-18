from app.services.telemetry_parser import TelemetryParser

alert = {
    "machine_id": "PUMP-01",
    "error_code": "E-404",
    "temperature": 105,
    "vibration": "High"
}

query = TelemetryParser.generate_query(alert)

print(query)