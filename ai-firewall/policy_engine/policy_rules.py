# policy_engine/policy_rules.py

from typing import Tuple, Dict, Any

class PolicyRuleSet:
    def __init__(self):
        # Future: dynamically load these from YAML or DB
        self.thresholds = {
            "anomaly_score": 0.8,
            "suspicion_level": 0.7
        }

    def apply_rules(self, input_data: Dict[str, Any]) -> Tuple[str, str]:
        score = input_data.get("anomaly_score", 0)
        suspicion = input_data.get("suspicion_level", 0)
        malicious = input_data.get("predicted_label", "benign") == "malicious"

        if score > self.thresholds["anomaly_score"] or suspicion > self.thresholds["suspicion_level"]:
            return "block", "High anomaly or suspicion level"
        elif malicious:
            return "block", "Model classified traffic as malicious"
        else:
            return "allow", "No critical threats detected"
