from fastapi import FastAPI

from models import JDRequest, JDAnalysis
import jd_analyzer

app = FastAPI(
    title="AI Career Assistant",
    description="It will predict whether to apply to the job as per JD or not",
    version="0.0.1"
)

@app.post("/analyze-jd", response_model=JDAnalysis)
def analyze_job_description(jd_request: JDRequest):
    response = jd_analyzer.analyze_jd(jd_request.job_description)
    return response