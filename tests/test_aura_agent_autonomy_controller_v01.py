from core.agents.autonomy.aura_agent_autonomy_controller_v01 import (

    AURAAgentAutonomyController

)

def test_autonomy_controller():

    controller = AURAAgentAutonomyController()

    decision = controller.evaluate(

        "Build enterprise automation platform"

    )

    action = controller.execute_action(

        decision

    )

    lesson = controller.learn(

        "Execution completed successfully"

    )

    state = controller.get_state()

    assert decision["decision"]["action"] == "implementation"

    assert action["status"] == "completed"

    assert lesson["lesson"] == "Execution completed successfully"

    assert len(state["decisions"]) == 1

if __name__ == "__main__":

    test_autonomy_controller()