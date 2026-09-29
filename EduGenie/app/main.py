import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Resolve root directory (EduGenie/) and ensure it is in sys.path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

load_dotenv(BASE_DIR / ".env")

from app.explanation_module import explain_topic
from app.qna import answer_question_with_gemini
from app.quiz_module import generate_quiz
from app.summary_module import summarize_text
from app.learning_path import get_learning_recommendations

if not os.getenv("GEMINI_API_KEY"):
    print("⚠️ WARNING: GEMINI_API_KEY is not set in the .env file.")

app = FastAPI(
    title="EduGenie: Google Gemini Powered Learning Assistant",
    description="Lightweight AI-powered educational assistant for Q&A, Explanations, Summaries, Quizzes, and Learning Paths.",
    version="1.0.0"
)

# Mount static and templates folders from project root
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


# Frontend Home Route (Updated for latest Starlette/FastAPI signature)
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


# Q&A - GET API using Gemini
@app.get("/qa")
async def answer_question(question: str = Query(...)):
    answer = answer_question_with_gemini(question)
    return {"answer": answer}


# Explanation - POST API
@app.post("/explain")
@app.post("/explain/")
async def explain_api(request: Request):
    data = await request.json()
    topic = data.get("topic")
    if not topic:
        return JSONResponse(content={"error": "Please provide a topic."}, status_code=400)
    explanation = explain_topic(topic)
    return {"topic": topic, "explanation": explanation}


# Summarization - POST API
@app.post("/summarize")
@app.post("/summarize/")
async def summarize_api(request: Request):
    data = await request.json()
    text = data.get("text")
    if not text:
        return JSONResponse(content={"error": "Please provide text to summarize."}, status_code=400)
    summary = summarize_text(text)
    return {"summary": summary}


# Quiz Generation - POST API
@app.post("/quiz")
@app.post("/quiz/")
async def quiz_api(request: Request):
    data = await request.json()
    text = data.get("text")
    if not text:
        return JSONResponse(content={"error": "Please provide text for quiz."}, status_code=400)
    quiz = generate_quiz(text)
    print("Generated quiz:", quiz)
    return JSONResponse(content={"quiz": quiz})


# Learning Recommendations - GET API
@app.get("/learn/recommendations")
async def learning_recommendation_api(topic: str = Query(...)):
    recommendation = get_learning_recommendations(topic)
    return {"topic": topic, "recommendation": recommendation}