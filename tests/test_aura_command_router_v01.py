from core.interface.router.aura_command_router_v01 import (

    AURACommandRouter

)

def test_command_router():

    router = AURACommandRouter()

    command = router.analyze_command(

        "AURA research the AI market and create a strategy"

    )

    result = router.route_command(

        command

    )

    state = router.get_state()

    print(

        "AURA Command Router Test"

    )

    print(state)

    assert result["intent"] == "research"

    assert result["route"] == "Research Agent"

    assert len(state["commands"]) == 1

if __name__ == "__main__":

    test_command_router()