import os
import traceback
from pathlib import Path
from dotenv import load_dotenv
from google import genai

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")

client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None


def get_learning_recommendations(topic: str) -> str:
    prompt = f"""You are an AI tutor. The student wants to learn about: {topic}.
Suggest a structured and adaptive learning path including key topics, order of learning, and resources (videos, books, interactive tutorials).
Include beginner, intermediate, and advanced levels if needed.
"""
    try:
        if not client:
            return "⚠️ Error: GEMINI_API_KEY is missing in .env"
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )
        print("🧠 Gemini raw response:", response)

        if hasattr(response, "text") and response.text:
            return response.text.strip()
        else:
            return "❌ Could not extract content from Gemini response."
    except Exception as e:
        traceback.print_exc()
        return f"❌ Error occurred: {str(e)}"