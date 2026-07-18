class TelemetryParser:
    """
    Converts incoming IoT telemetry into a search query
    that can be used by the RAG system.
    """

    @staticmethod
    def generate_query(alert: dict) -> str:
        machine_id = alert.get("machine_id", "")
        error_code = alert.get("error_code", "")
        temperature = alert.get("temperature", "")
        vibration = alert.get("vibration", "")

        query = (
            f"Repair procedure for machine {machine_id} "
            f"error code {error_code} "
            f"temperature {temperature} "
            f"vibration {vibration}"
        )

        return query