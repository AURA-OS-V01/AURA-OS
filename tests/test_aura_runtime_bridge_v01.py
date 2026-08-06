from core.interface.bridge.aura_runtime_bridge_v01 import (

    AURARuntimeBridge

)

def test_runtime_bridge():

    bridge = AURARuntimeBridge()

    request = bridge.process_request(

        "research",

        "Research AI market opportunities"

    )

    state = bridge.get_state()

    print(

        "AURA Runtime Bridge Test"

    )

    print(state)

    assert request["route"] == (

        "Research Agent"

    )

    assert request["status"] == (

        "processed"

    )

    assert len(

        state["requests"]

    ) == 1

if __name__ == "__main__":

    test_runtime_bridge()