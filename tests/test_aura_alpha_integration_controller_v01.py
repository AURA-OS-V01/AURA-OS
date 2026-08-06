from core.integration.aura_alpha_integration_controller_v01 import (

    AURAAlphaIntegrationController

)

def test_alpha_controller():

    controller = AURAAlphaIntegrationController()

    workflow = controller.start_workflow(

        "Build Enterprise AI Platform",

        "Business",

        "high"

    )

    controller.register_runtime_module(

        "Research Agent",

        "Research"

    )

    controller.register_runtime_module(

        "Strategy Engine",

        "Strategy"

    )

    result = controller.execute_workflow(

        workflow["id"]

    )

    state = controller.get_state()

    print(state)

    assert result["status"] == "completed"

    assert len(state["runtime"]["modules"]) == 2

    assert len(state["goals"]["goals"]) == 1

if __name__ == "__main__":

    test_alpha_controller()