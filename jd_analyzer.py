import os
from openai import OpenAI
import json
from dotenv import load_dotenv
from pydantic import ValidationError

from models import JDAnalysis

load_dotenv()

SYSTEM_PROMPT = """
                You are a Job description expert. You need to check the details from the shared
                JD and returnt the resonse in expected format.
                Format:
                    role_title: str
                    required_skills: list[str]
                    nice_to_have: list[str]
                    experience_years: str
                    location: str
                    match_recommendation:  "apply" or "skip" 
                No explaination, No markdown, Return only valid JSON.
"""

MODEL = "gpt-4o-mini"
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def analyze_jd(job_description: str):
    response = client.chat.completions.create(
        model=MODEL,
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": job_description
            }
        ]
    )
    
    raw_res = response.choices[0].message.content or ""
    
    try:
        parsed_res = json.loads(raw_res)
        return JDAnalysis(**parsed_res)
    except (json.JSONDecodeError, ValidationError):
        try:
            raw_res = raw_res.strip()
            raw_res = raw_res.removeprefix("```json")
            raw_res = raw_res.removesuffix("```")
            raw_res = raw_res.strip()
            parsed_res = json.loads(raw_res)
            return JDAnalysis(**parsed_res)
        except (json.JSONDecodeError, ValidationError):
            return {"error": f"Unable to parse raw response {raw_res}"}   