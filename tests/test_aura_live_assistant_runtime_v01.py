from core.interface.live.aura_live_assistant_runtime_v01 import (

    AURALiveAssistantRuntime

)

def test_live_assistant_runtime():

    aura = AURALiveAssistantRuntime()

    response = aura.process_input(

        "Research the AI market"

    )

    state = aura.get_session_state()

    print(

        "AURA Live Assistant Runtime Test"

    )

    print(state)

    assert (

        "research"

        in response.lower()

    )

    assert len(

        state["history"]

    ) == 1

if __name__ == "__main__":

    test_live_assistant_runtime()