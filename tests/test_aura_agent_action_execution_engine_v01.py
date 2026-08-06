from core.agents.actions.aura_agent_action_execution_engine_v01 import (

    AURAAgentActionExecutionEngine

)

def test_action_execution_engine():

    engine = AURAAgentActionExecutionEngine()

    action = engine.create_action(

        "sales_agent",

        "customer_outreach",

        "Send introduction email to qualified lead"

    )

    result = engine.execute_action(

        action["id"]

    )

    print(

        "AURA Agent Action Execution Engine Test"

    )

    print(

        "--------------------------------------"

    )

    print(action)

    print(result)

    assert result["status"] == (

        "success"

    )

    assert len(

        engine.get_results()

    ) == 1

if __name__ == "__main__":

    test_action_execution_engine()