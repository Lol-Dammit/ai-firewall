def take_action(threat_level: float, threshold: float = 0.8):
    if threat_level >= threshold:
        return "BLOCK"
    elif threat_level >= 0.5:
        return "ALERT"
    else:
        return "ALLOW"

