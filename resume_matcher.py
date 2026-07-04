from models import MatchResult
from jd_analyzer import client, MODEL
import json
from pydantic import ValidationError

SYSTEM_PROMPT = """
                You are an expert resume and job description comparison. You need to compare resume with job description and return the 
                result in following format:
                    matched_skills: list[str]
                    gap_skills: list[str]
                    match_percentage: float
                    recommendation: apply or skip
                No markdown, No explaination. Result should be in JSON Format. 
"""

def match_resume(resume: str, job_description: str) -> MatchResult:
    response = client.chat.completions.create(
        model = MODEL,
        temperature = 0,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": f"Resume:\n{resume}\n\nJob Description:\n{job_description}"
            }
        ]
    )
    
    raw_response = response.choices[0].message.content or ""
    
    try:
        parsed = json.loads(raw_response)
        return MatchResult(**parsed)
    except (json.JSONDecodeError, ValidationError):
        try:
            raw_response = raw_response.strip()
            raw_response = raw_response.removeprefix('```json')
            raw_response = raw_response.removesuffix('```')
            raw_response = raw_response.strip()
            parsed = json.loads(raw_response)
            return MatchResult(**parsed)
        except (json.JSONDecodeError, ValidationError) as e:
            raise ValueError(f"Unable to parse LLM response: {e}")