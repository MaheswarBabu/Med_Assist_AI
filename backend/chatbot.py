import os
from openai import OpenAI

SYSTEM_PROMPT = """
You are MedAssist AI, a friendly medical information assistant.
- Explain general health information in simple language.
- Do not diagnose diseases or prescribe medicines or dosages.
- Encourage users to consult a qualified healthcare professional for personal concerns.
- For potentially life-threatening symptoms, advise immediate emergency medical attention.
- Do not claim certainty when information is insufficient.
- Do not request or encourage sharing identifiable patient information.
"""

def generate_response(message: str, history: list[dict]) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not configured.")

    client = OpenAI(api_key=api_key)
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    for item in history or []:
        role = item.get("role")
        content = item.get("content")
        if role in ("user", "assistant") and isinstance(content, str):
            messages.append({"role": role, "content": content})

    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        messages=messages,
        temperature=0.3,
        max_tokens=400,
    )
    return response.choices[0].message.content or ""
