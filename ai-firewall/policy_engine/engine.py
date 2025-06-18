from .rules import RuleSet
from typing import Dict, Any, List
# policy_engine/engine.py

from typing import Dict, Any
from loguru import logger
from policy_engine.policy_rules import PolicyRuleSet

class PolicyEngine:
    def __init__(self):
        self.rules = PolicyRuleSet()
        logger.info("PolicyEngine initialized with default rules.")

    def evaluate(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate input against defined policies."""
        logger.debug(f"Evaluating input: {input_data}")
        decision, reason = self.rules.apply_rules(input_data)
        logger.info(f"Policy decision: {decision} | Reason: {reason}")
        return {
            "action": decision,
            "reason": reason,
            "input_summary": input_data.get("summary", "N/A")
        }

