def evaluate_policy(threat_score: float) -> str:
    if threat_score > 0.9:
        return "block"
    elif threat_score > 0.7:
        return "alert"
    return "allow"
