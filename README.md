# MedAssist AI

A beginner-friendly medical-information chatbot built with Gradio, FastAPI, and the OpenAI API. This is a classroom/demo application, not a clinically validated medical tool.

## Project structure

```text
MedAssist-AI/
├── backend/
│   ├── __init__.py
│   ├── main.py
│   └── chatbot.py
├── frontend/
│   └── app.py
├── .env.example
├── .gitignore
├── .dockerignore
├── requirements.txt
└── README.md
```

## Run locally on Windows PowerShell

1. Install Python 3.11 or a compatible Python 3.11+ release.
2. Open PowerShell in this folder.
3. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
   ```

4. Create your local `.env` file from the example:

   ```powershell
   Copy-Item .env.example .env
   ```

5. Edit `.env` and set `OPENAI_API_KEY` to your own API key. Never commit `.env` or put the key in source code.

6. Start the backend in Terminal 1 (from the project root):

   ```powershell
   python -m uvicorn backend.main:app --reload --port 8000
   ```

7. Start the frontend in Terminal 2 (also from the project root, with the same virtual environment activated):

   ```powershell
   python frontend/app.py
   ```

8. Open **http://localhost:7860**. Backend API docs are at **http://localhost:8000/docs**, and the health check is **http://localhost:8000/health**.

## Troubleshooting

- If the API key is missing, verify the `.env` file exists in the project root and contains `OPENAI_API_KEY=...`.
- If the UI cannot reach the backend, confirm Terminal 1 is running and `BACKEND_URL=http://127.0.0.1:8000` in `.env`.
- If package installation fails, upgrade pip with `python -m pip install --upgrade pip` and retry.
- API usage may incur charges under your OpenAI account. 

## Safety note

Use fictional/general questions only. Do not enter personal health information. The assistant can make mistakes; it must not be used for diagnosis, treatment, or emergency decision-making.
