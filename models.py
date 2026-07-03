from pydantic import BaseModel
from enum import Enum

class MatchRecommendation(str, Enum):
    APPLY = "apply"
    SKIP = "skip"
    
class JDRequest(BaseModel):
    job_description: str
    
class JDAnalysis(BaseModel):
    role_title: str
    required_skills: list[str]
    nice_to_have: list[str]
    experience_years: str
    location: str
    match_recommendation:  MatchRecommendation   