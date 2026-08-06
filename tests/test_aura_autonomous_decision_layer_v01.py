from core.intelligence.decision.aura_autonomous_decision_layer_v01 import (

    AURAAutonomousDecisionLayer

)

def test_autonomous_decision_layer():

    decision_layer = AURAAutonomousDecisionLayer()

    decision = decision_layer.analyze_situation(

        "Major customer opportunity detected",

        90

    )

    agent = decision_layer.select_agent(

        decision

    )

    plan = decision_layer.create_action_plan(

        decision,

        agent

    )

    state = decision_layer.get_decision_state()

    print(

        "AURA Autonomous Decision Layer Test"

    )

    print(

        "-----------------------------------"

    )

    print(state)

    assert decision["priority"] == (

        "high"

    )

    assert agent == (

        "enterprise_orchestrator"

    )

    assert plan["status"] == (

        "ready"

    )

if __name__ == "__main__":

    test_autonomous_decision_layer()