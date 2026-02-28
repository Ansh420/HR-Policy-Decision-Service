from fastapi import FastAPI
from pydantic import BaseModel
from decision_logic import get_policy_decision

app =FastAPI(title="HR policy Decision Service")

class DecisionRequest(BaseModel):
    employee_id:str
    question:str

class DecisionResponse(BaseModel):
    employee_id :str
    policy_type: str
    decision: str
    confidence :str

@app.post("/decision", response_model=DecisionResponse)
async def handle_decision(request:DecisionRequest):
    decision_result = get_policy_decision(request.question)
    return DecisionResponse(employee_id=request.employee_id,
                            policy_type =decision_result["Policy_type"],
                            decision=decision_result["decision"],
                            confidence=decision_result["confidence"])



