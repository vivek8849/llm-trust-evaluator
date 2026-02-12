def classify_risk(prompt: str) -> str:
    """
    Improved risk classifier using broader medical, legal,
    and financial trigger words.
    """

    high_risk_keywords = [
        # medical
        "medical", "doctor", "diagnosis", "treatment",
        "dosage", "dose", "medicine", "medication",
        "drug", "ibuprofen", "antibiotic", "cancer",
        "child", "infant", "pregnant",

        # legal
        "lawsuit", "contract", "legal", "court",

        # financial
        "investment", "financial advice", "stock",
        "crypto", "tax"
    ]

    prompt_lower = prompt.lower()

    for word in high_risk_keywords:
        if word in prompt_lower:
            return "high"

    return "low"


def make_decision(trust_score: float, risk_level: str) -> str:
    """
    Decide whether to auto-accept, review, or reject.
    """

    if risk_level == "high":
        if trust_score > 0.85:
            return "review"
        else:
            return "reject"

    if risk_level == "low":
        if trust_score > 0.7:
            return "auto-accept"
        elif trust_score > 0.4:
            return "review"
        else:
            return "reject"
        
# Risk × Trust = Decision
# Low : definitions, general ML explanations
# Medium : coding advice, architecture decisions
# High : medical, legal, financial decisions
