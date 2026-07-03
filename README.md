# AI Career Assistant

AI Career Assistant is a tool that helps job seekers analyze job descriptions and make informed decisions about whether to apply. It extracts key information from any JD — required skills, nice-to-have skills, experience requirements, and location — and provides a recommendation.

## Architecture

User pastes JD → Streamlit UI → jd_analyzer.py → OpenAI GPT-4o-mini → Structured JSON → Displayed in UI

FastAPI also exposes the same analyzer as a REST endpoint for programmatic access.

## Features

- JD analysis — extracts role title, required skills, nice-to-have skills, experience, and location
- Match recommendation — apply or skip
- Clean Streamlit UI with spinner and formatted output
- FastAPI REST endpoint for programmatic access
- Safe JSON parsing with markdown fence stripping
- Pydantic validation on all inputs and outputs

## Setup

1. Clone the repo
   git clone https://github.com/vishalsinhacodes/ai-career-assistant.git
   cd ai-career-assistant

2. Create and activate virtual environment

   Windows:
   python -m venv venv
   venv\Scripts\activate

   Mac/Linux:
   python3 -m venv venv
   source venv/bin/activate

3. Install dependencies
   pip install -r requirements.txt

4. Set your OpenAI API key

   Create a .env file in the project root:
   OPENAI_API_KEY=your_key_here

## How to Run

Streamlit UI:
streamlit run app.py

FastAPI server:
uvicorn main:app --reload
API docs at http://localhost:8000/docs

## Tech Stack

- FastAPI — REST API layer
- Streamlit — interactive UI
- OpenAI GPT-4o-mini — JD analysis and extraction
- Pydantic — request/response validation
- python-dotenv — environment variable management
