import os
from pathlib import Path

import gradio as gr
import requests
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000").rstrip("/")

def chat(message, history):
    payload = {
        "message": message,
        "history": history or [],
    }
    try:
        response = requests.post(
            f"{BACKEND_URL}/chat",
            json=payload,
            timeout=90,
        )
        response.raise_for_status()
        return response.json()["answer"]
    except requests.RequestException:
        return (
            "I couldn't reach the chatbot service. Please check that the "
            "backend is running and BACKEND_URL is correct."
        )

demo = gr.ChatInterface(
    fn=chat,
    title="MedAssist AI",
    description=(
        "General medical information for learning purposes only. "
        "Not a diagnosis or a substitute for professional medical care. "
        "Please don't enter personal or identifiable patient information."
    ),
    examples=[
        "What is blood pressure?",
        "What is the difference between viruses and bacteria?",
        "Why is hydration important?",
    ],
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
