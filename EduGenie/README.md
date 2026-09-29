# EduGenie: Google Gemini Powered Learning Assistant 🧠✨

EduGenie is a lightweight AI-powered educational web application designed to assist learners across all academic levels. Built with **FastAPI** on the backend, the official **Google GenAI SDK** for generative reasoning, and an interactive **HTML5/CSS3/JavaScript** frontend, EduGenie provides instant concept clarification, text summarization, auto-generated self-assessment quizzes, and adaptive learning paths.

---

## 🚀 Key Modules & Features

### 1. Ask a Question (`/qa`)
Delivers smart and concise answers to general, scientific, and academic questions using Google Gemini.

### 2. Concept Explanation (`/explain/`)
Generates simplified, age-appropriate explanations designed especially for school students.

### 3. Text Summarization (`/summarize/`)
Condenses long educational passages and study materials into concise summaries while retaining the core concepts.

### 4. Quiz Generator (`/quiz`)
Generates **3 multiple-choice questions (MCQs)** with answer options and dynamic in-browser answer verification.

The interface provides immediate feedback:

- ✅ Correct!
- ❌ Incorrect

### 5. Learning Recommendations (`/learn/recommendations`)
Creates a structured, tiered study roadmap consisting of:

- Beginner
- Intermediate
- Advanced

Each level includes estimated learning timelines and recommended resources.

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Backend | Python 3.10+, FastAPI, Uvicorn, Jinja2 |
| AI SDK | Google GenAI SDK (`google-genai`) |
| AI Model | `gemini-2.5-flash` |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Communication | Asynchronous JavaScript using `fetch` API |
| Environment Management | `python-dotenv` |

---

## 📁 Project Directory Structure

```text
EduGenie/
├── .env                        # Gemini API key and model configuration
├── requirements.txt            # Python dependencies
├── run.bat                     # 1-click Windows startup & setup script
├── README.md                   # Project documentation
│
├── app/
│   ├── __init__.py             # Python package marker
│   ├── main.py                 # FastAPI application routes and template rendering
│   ├── explanation_module.py   # Concept explanation logic
│   ├── qna.py                  # Question-answering logic
│   ├── quiz_module.py          # 3-question MCQ generator and JSON parsing
│   ├── summary_module.py       # Educational passage summarization logic
│   └── learning_path.py        # Structured study roadmap generator
│
├── static/
│   └── style.css               # Styling and responsive layout
│
└── templates/
    └── index.html              # Frontend user interface and interactive forms
```

---

## ⚙️ Prerequisites & Environment Setup

### 1. Prerequisites

Before running EduGenie, make sure the following are installed:

- **Python 3.10 or higher**
- Python added to the system `PATH`
- A **Google Gemini API Key**

You can obtain a Gemini API key from [Google AI Studio](https://aistudio.google.com/).

---

### 2. Environment Configuration

Create a `.env` file in the root `EduGenie/` directory.

```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
GEMINI_MODEL=gemini-3.6-flash
```

> **Important:** Never commit your `.env` file or expose your Gemini API key publicly.

---

### 3. Install Dependencies

Make sure your `requirements.txt` contains the required dependencies:

```text
fastapi>=0.115.0
uvicorn[standard]>=0.34.0
jinja2>=3.1.4
python-dotenv>=1.0.1
google-genai>=1.0.0
pydantic>=2.10.0
```

---

## 💻 Running the Application

EduGenie can be started either using the provided Windows startup script or manually from the terminal.

---

### Option A: One-Click Startup on Windows

Double-click:

```text
run.bat
```

Or execute it from Command Prompt or PowerShell:

```bat
run.bat
```

The startup script automatically:

1. Validates the Python installation.
2. Creates the virtual environment if required.
3. Activates the virtual environment.
4. Installs the required dependencies.
5. Validates the `.env` configuration.
6. Starts the Uvicorn development server.

---

### Option B: Manual Setup

#### Step 1: Create a Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

#### Step 2: Install Dependencies

Upgrade `pip` and install the project dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

#### Step 3: Start the FastAPI Server

```bash
python -m uvicorn app.main:app --reload
```

The application will start on:

```text
http://127.0.0.1:8000
```

---

#### Step 4: Access the Application

**Web Interface:**

```text
http://127.0.0.1:8000
```

**Interactive API Documentation (Swagger UI):**

```text
http://127.0.0.1:8000/docs
```

---

## 🔌 REST API Endpoints

| Endpoint | Method | Parameters / Payload | Description |
|----------|--------|----------------------|-------------|
| `/` | `GET` | None | Renders the EduGenie web interface |
| `/qa` | `GET` | `question` query parameter | Answers academic questions using Gemini |
| `/explain/` | `POST` | `{"topic": "string"}` | Generates simplified explanations for students |
| `/summarize/` | `POST` | `{"text": "string"}` | Summarizes educational passages |
| `/quiz` | `POST` | `{"text": "string"}` | Generates 3 multiple-choice questions in structured JSON format |
| `/learn/recommendations` | `GET` | `topic` query parameter | Generates a structured learning path |

---

## 📡 API Usage Examples

### Ask a Question

**Request:**

```http
GET /qa?question=Which%20is%20the%20largest%20ocean?
```

**Example Response:**

```text
The Pacific Ocean is the largest ocean on Earth.
```

---

### Generate a Concept Explanation

**Request:**

```http
POST /explain/
Content-Type: application/json
```

**Payload:**

```json
{
  "topic": "Binary Search Algorithm"
}
```

**Expected Result:**

A simple and student-friendly explanation of the Binary Search Algorithm.

---

### Summarize Text

**Request:**

```http
POST /summarize/
Content-Type: application/json
```

**Payload:**

```json
{
  "text": "The Industrial Revolution was a period of major industrialization..."
}
```

**Expected Result:**

A concise summary containing the major concepts from the provided passage.

---

### Generate a Quiz

**Request:**

```http
POST /quiz
Content-Type: application/json
```

**Payload:**

```json
{
  "text": "Pythagoras theorem"
}
```

**Expected Result:**

Three multiple-choice questions with answer options and structured answers for validation.

---

### Generate a Learning Path

**Request:**

```http
GET /learn/recommendations?topic=SQL
```

**Expected Result:**

A structured learning roadmap containing:

- Beginner milestones
- Intermediate milestones
- Advanced milestones
- Estimated timelines
- Recommended learning resources

---

## 🧪 Testing Scenarios

The following scenarios can be used to verify the functionality of each major EduGenie module.

### 1. Q&A Module

**Test Query:**

```text
Which is the largest ocean?
```

**Expected Output:**

```text
The Pacific Ocean is the largest ocean on Earth.
```

---

### 2. Explanation Module

**Test Queries:**

```text
quantum computing
```

or

```text
Binary Search Algorithm
```

**Expected Output:**

A clear and simplified explanation suitable for school-level learners.

---

### 3. Summarization Module

**Test Input:**

Paste a paragraph describing the **Industrial Revolution**.

**Expected Output:**

A concise summary highlighting the major concepts and important information from the original text.

---

### 4. Quiz Module

**Test Input:**

```text
Pythagoras theorem
```

**Expected Output:**

Three multiple-choice questions containing:

- Question text
- Multiple answer options
- Correct answer
- Dynamic answer validation in the browser

The interface should provide immediate feedback:

```text
✅ Correct!
```

or

```text
❌ Incorrect
```

---

### 5. Learning Path Module

**Test Input:**

```text
SQL
```

**Expected Output:**

A structured roadmap containing:

```text
Beginner
    ↓
Intermediate
    ↓
Advanced
```

along with estimated timelines and recommended learning resources.

---

## 🔐 Security Considerations

- Store the Gemini API key only in the `.env` file.
- Do not hard-code API credentials inside Python source files.
- Do not commit `.env` to Git.
- Add `.env` to `.gitignore`.
- Avoid exposing sensitive configuration through API responses.
- Use environment variables for configurable AI model settings.

Example `.gitignore` entry:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

---

## 📚 Application Workflow

The overall EduGenie workflow can be represented as:

```text
                 ┌─────────────────────┐
                 │      User Input     │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   FastAPI Backend   │
                 └──────────┬──────────┘
                            │
             ┌──────────────┼──────────────┐
             │              │              │
             ▼              ▼              ▼
        Q&A Module    Explanation      Summarization
             │           Module            Module
             │              │              │
             └──────────────┼──────────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Google Gemini     │
                 │    AI Model         │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    Generated        │
                 │      Response       │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ HTML / JavaScript   │
                 │     Frontend        │
                 └─────────────────────┘
```

---

## 🎯 Project Objectives

EduGenie is designed to:

- Provide quick answers to educational questions.
- Simplify complex academic concepts.
- Reduce lengthy study materials into concise summaries.
- Help students test their understanding through automatically generated quizzes.
- Provide structured learning paths for different levels of expertise.
- Demonstrate the practical integration of Generative AI into an educational application.
- Provide a lightweight and accessible learning assistant through a web interface.

---

## 🌟 Future Enhancements

Potential future improvements include:

- User authentication and personalized profiles.
- Learning progress tracking.
- Persistent quiz history.
- Difficulty-based quiz generation.
- Subject-specific learning modes.
- Voice-based question input.
- Text-to-speech responses.
- Multilingual educational explanations.
- Personalized recommendations based on learning history.
- Database integration for storing learning progress.
- Deployment to a cloud platform.

---

## 📄 License

This project is intended for educational and learning purposes.

---

## 👨‍💻 Project

**EduGenie – Google Gemini Powered Learning Assistant**

Built using **FastAPI**, **Google GenAI SDK**, and modern web technologies to demonstrate the application of Generative AI in education.