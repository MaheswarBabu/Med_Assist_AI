from pathlib import Path
from dotenv import load_dotenv

# Load .env from the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from backend.chatbot import generate_response

app = FastAPI(title="MedAssist AI API", version="1.0.0")

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000)
    history: list[ChatMessage] = Field(default_factory=list)

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/chat")
def chat(request: ChatRequest):
    try:
        history = [item.model_dump() for item in request.history]
        answer = generate_response(request.message, history)
        return {"answer": answer}
    except RuntimeError as exc:
        raise HTTPException(status_code=500, detail=str(exc))
    except Exception:
        # Keep provider/API details out of the public response.
        raise HTTPException(
            status_code=502,
            detail="Unable to generate a response. Check backend logs and API configuration."
        )
