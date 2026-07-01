from fastapi import FastAPI
from pydantic import BaseModel
from src.referee.core import AIReferee

app = FastAPI(
    title="AI Referee API",
    description="Automated governance layer for evaluating Code Health and WCAG accessibility.",
    version="0.1.0"
)

referee = AIReferee()

class AuditRequest(BaseModel):
    code: str
    type: str = "python" # e.g. python, html

class AuditResponse(BaseModel):
    score: int
    status: str
    feedback: list[str]

@app.post("/audit", response_model=AuditResponse)
def audit_code(payload: AuditRequest):
    if payload.type.lower() == "html":
        return referee.evaluate_accessibility(payload.code)
    else:
        return referee.evaluate_code_health(payload.code)

@app.get("/health")
def health_check():
    return {"status": "ok"}
