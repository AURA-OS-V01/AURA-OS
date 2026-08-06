from core.action.aura_action_execution_engine_v01 import (

    AURAActionExecutionEngine

)

def test_action_execution_engine():

    engine = AURAActionExecutionEngine()

    engine.create_action(

        "Run Research",

        "Research Agent",

        {

            "topic": "AI"

        }

    )

    created = engine.actions[0].copy()

    result = engine.execute(

        created["id"]

    )

    state = engine.get_state()

    assert created["status"] == "created"

    assert result["status"] == "completed"

    assert result["name"] == "Run Research"

    assert state["total_actions"] == 1

if __name__ == "__main__":

    test_action_execution_engine()