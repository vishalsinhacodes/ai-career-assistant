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
    
class MatchResult(BaseModel):
    matched_skills: list[str]
    gap_skills: list[str]
    match_percentage: float
    recommendation: MatchRecommendation    
    
class InterviewQuestion(BaseModel):
    question: str
    suggested_answer: str
    
class InterviewPrep(BaseModel):
    questions: list[InterviewQuestion]        