from pydantic import BaseModel
from typing import Any, Dict, List, Callable


class Rule(BaseModel):
    id: str
    description: str
    condition: Callable[[Dict[str, Any]], bool]
    action: str  # "allow", "block", "alert", "throttle"


class RuleSet(BaseModel):
    rules: List[Rule]

    def evaluate(self, data: Dict[str, Any]) -> List[str]:
        triggered_actions = []
        for rule in self.rules:
            try:
                if rule.condition(data):
                    triggered_actions.append(rule.action)
            except Exception as e:
                print(f"[!] Error evaluating rule {rule.id}: {e}")
        return triggered_actions


def apply_policies(packet, model_prediction):
    # Placeholder: Add custom logic based on prediction
    if model_prediction == "BLOCK":
        return False
    return True
