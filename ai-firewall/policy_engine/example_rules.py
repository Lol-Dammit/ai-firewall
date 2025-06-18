from .rules import Rule, RuleSet


def get_default_ruleset() -> RuleSet:
    rules = [
        Rule(
            id="r1",
            description="Block suspicious ports",
            condition=lambda d: d.get("dst_port") in [4444, 6667],
            action="block"
        ),
        Rule(
            id="r2",
            description="Alert on high packet rate",
            condition=lambda d: d.get("packet_rate", 0) > 1000,
            action="alert"
        ),
        Rule(
            id="r3",
            description="Throttle known spamming IP",
            condition=lambda d: d.get("src_ip") in ["192.0.2.10"],
            action="throttle"
        ),
    ]
    return RuleSet(rules=rules)
