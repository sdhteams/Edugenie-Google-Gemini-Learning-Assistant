import os
import re
import json
from pathlib import Path
from dotenv import load_dotenv
from google import genai

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.6-flash")

client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None


def clean_json_block(text: str) -> str:
    # Remove Markdown ```json code fences
    return re.sub(r"```(?:json)?\s*(.*?)\s*```", r"\1", text, flags=re.DOTALL).strip()


def generate_quiz(text: str) -> list:
    try:
        if not client:
            return [{"error": "⚠️ Error: GEMINI_API_KEY is missing in .env"}]

        prompt = f"""You are a quiz generator.

From the following passage, create 3 multiple-choice questions. Each question should include:
- A "question"
- A list of 4 "options"
- A correct "answer" that must exactly match one of the options.

Format your output as **valid JSON**, like this:
[
  {{
    "question": "What is ...?",
    "options": ["A", "B", "C", "D"],
    "answer": "A"
  }}
]

Passage:
{text}
"""
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )
        quiz_text = response.text.strip()

        cleaned_text = clean_json_block(quiz_text)
        quiz_data = json.loads(cleaned_text)

        if isinstance(quiz_data, list):
            return quiz_data
        return [{"error": "Unexpected quiz format received from model."}]
    except Exception as e:
        return [{"error": f"⚠️ Error in Quiz Generation: {str(e)}"}]