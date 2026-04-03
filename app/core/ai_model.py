import requests

class AIModel:
    def __init__(self):
        self.url = "http://localhost:11434/api/generate"
        self.model_name = "testsss"

    def generate_response(self, message: str) -> str:
        payload = {
            "model": self.model_name,
            "prompt": message,
            "stream": False
        }

        response = requests.post(self.url, json=payload)

        if response.status_code == 200:
            return response.json().get("response", "")
        else:
            return "เกิดข้อผิดพลาดในการเรียก AI"
