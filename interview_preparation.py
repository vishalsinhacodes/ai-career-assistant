from config import MODEL, client
import json
from models import InterviewPrep
from pydantic import ValidationError



SYSTEM_PROMPT = """
You are a Technical Expert which takes interview on reguler basis. You will receive resume and job description
and on the basis of that you need to generate 5 interview questions and suggested answers with proper example.
Questions should be based on the candidate's experience in the resume and the requirements in the JD.

The format should be
[
  {
    "question": "Explain RAG pipeline",
    "suggested_answer": "RAG stands for..."
  },
  {
    "question": "How do you handle LLM failures?",
    "suggested_answer": "I return 502..."
  }
]
You will return proper json. No markdown.

"""

def generate_interview_prep(resume: str, job_description: str):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
               "role": "user",
               "content": f"Resume:\n{resume}\n\nJob description:\n{job_description}" 
            }
        ]
    )
    
    raw_response = response.choices[0].message.content or ""
    
    try:
        parsed_res = json.loads(raw_response)
        return InterviewPrep(questions=parsed_res)
    except (json.JSONDecodeError, ValidationError):
        try:
            raw_response = raw_response.strip()
            raw_response = raw_response.removeprefix('```json')
            raw_response = raw_response.removesuffix('```')
            raw_response = raw_response.strip()
            
            parsed_res = json.loads(raw_response)
            return InterviewPrep(questions=parsed_res)
        except (json.JSONDecodeError, ValidationError) as e:
            raise ValueError(f"Unable to parse LLM response: {e}")