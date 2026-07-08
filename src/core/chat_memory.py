class ChatMemory:
    def __init__(self):
        self.messages = [
            {
                "role": "user",
                "parts": [{
                    "text": (
                        "Eres CareerPilotAI, un asistente especializado en "
                        "orientación profesional, empleabilidad, desarrollo "
                        "de carrera, entrevistas y análisis de hojas de vida."
                    )
                }]
            }
        ]

    def add_user_message(self, message):
        self.messages.append({
            "role": "user",
            "parts": [{"text": message}]
        })

    def add_model_message(self, message):
        self.messages.append({
            "role": "model",
            "parts": [{"text": message}]
        })

    def get_messages(self):
        return self.messages