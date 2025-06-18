from ai_firewall.response_engine.decision_maker import take_action

def test_action_block():
    assert take_action(0.9) == "BLOCK"

def test_action_alert():
    assert take_action(0.6) == "ALERT"

def test_action_allow():
    assert take_action(0.2) == "ALLOW"
