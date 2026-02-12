from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

from src.llm.response_generator import generate_multiple_responses
from src.embeddings.embedding_engine import EmbeddingEngine
from src.trust.self_critique import generate_self_critique, SemanticVulnerabilityScorer
from src.trust.trust_signals import TrustSignals
from src.trust.decision_engine import classify_risk, make_decision


app = FastAPI(title="LLM Trust Evaluator API")


class QueryRequest(BaseModel):
    prompt: str


@app.post("/evaluate")
def evaluate_trust(request: QueryRequest):

    prompt = request.prompt

    # Generate responses
    responses = generate_multiple_responses(prompt, n=5)

    # Consistency
    engine = EmbeddingEngine()
    embeddings = engine.encode(responses)
    sim_matrix = engine.compute_similarity_matrix(embeddings)
    consistency = engine.compute_consistency_score(sim_matrix)

    # Vulnerability
    critique = generate_self_critique(responses[0])
    scorer = SemanticVulnerabilityScorer()
    vulnerability = scorer.compute_score(critique)

    # Trust
    signals = TrustSignals(
        consistency_score=consistency,
        vulnerability_score=vulnerability
    )

    trust = signals.compute_final_score()

    # Risk decision
    risk = classify_risk(prompt)
    decision = make_decision(trust, risk)

    return {
        "consistency": float(consistency),
        "vulnerability": float(vulnerability),
        "trust_score": float(trust),
        "risk_level": risk,
        "decision": decision,
        "responses": responses,
        "critique": critique
    }