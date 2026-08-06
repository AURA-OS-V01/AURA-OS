from core.agents.safety.aura_agent_safety_governance_layer_v01 import (

    AURASafetyGovernanceLayer

)

def test_safety_governance():

    safety = AURASafetyGovernanceLayer()

    result = safety.evaluate(

        "Build enterprise automation platform"

    )

    assert result["approved"] is True

    state = safety.get_state()

    assert len(state["checks"]) == 1

if __name__ == "__main__":

    test_safety_governance()