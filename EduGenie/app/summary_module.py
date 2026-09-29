import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")

client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None


def summarize_text(text: str) -> str:
    try:
        if not client:
            return "⚠️ Error: GEMINI_API_KEY is missing in .env"
        prompt = f"Summarize the following text in simple language:\n\n{text}"
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error in Summary: {e}"