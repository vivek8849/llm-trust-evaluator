import requests
import random


# OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_URL = "http://host.docker.internal:11434/api/generate"


def generate_single_response(prompt: str, temperature: float = 0.7) -> str:
    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": temperature
        }
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=120)

    return response.json().get("response", "").strip()


def generate_multiple_responses(prompt: str, n: int = 5) -> list:
    responses = []

    for _ in range(n):
        # introduce slight randomness in temperature
        temp = random.uniform(0.6, 0.9)
        answer = generate_single_response(prompt, temperature=temp)
        responses.append(answer)

    return responses