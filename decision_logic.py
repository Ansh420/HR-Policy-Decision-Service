def get_policy_decision(question: str)-> str:
    if not question:
        return {
            "policy_type": "unknown",
            "policy_decision": "No question provided.",
            "confidence": "low"
            
        }
    
    q_lower = question.lower()
#  Leave Policy

    leave_keywords = ["leave", "vacation", "time off", "absence"]
    if any(keyword in q_lower for keyword in leave_keywords):
        if "sick" in q_lower:
            return {
                "policy_type": "leave",
                "policy_decision": "Sick leave is typically allowed with a medical certificate.",
                "confidence": "high"
            }
        elif "vacation" in q_lower or "time off" in q_lower:
            return {
                "policy_type": "leave",
                "policy_decision": "Vacation leave is usually granted based on company policy and tenure.",
                "confidence": "high"
            }
        

# Expense Policy

    expense_keywords = ["expense", "reimbursement", "travel", "meal"]

    if any(keyword in q_lower for keyword in expense_keywords):
        if "travel" in q_lower:
            return {
                "policy_type": "expense",
                "policy_decision": "Travel expenses are reimbursed with proper documentation and approval.",
                "confidence": "high"
            }
        elif "meal" in q_lower:
            return {
                "policy_type": "expense",
                "policy_decision": "Meal expenses may be reimbursed during business travel or meetings.",
                "confidence": "medium"
            }
        
    # Unknown Policy
    return {
        "policy_type": "unknown",
        "policy_decision": "The question does not match any known HR policy categories.",
        "confidence": "low"
    }


        