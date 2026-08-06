from core.agents.reasoning.aura_agent_planning_reasoning_engine_v01 import (

    AURAAgentPlanningReasoningEngine

)

def test_planning_reasoning():

    engine = AURAAgentPlanningReasoningEngine()

    plan = engine.create_plan(

        "Build enterprise automation platform",

        "high"

    )

    steps = engine.reason(

        "Build enterprise automation platform"

    )

    engine.add_step(

        plan["id"],

        steps[0],

        "Planning Agent"

    )

    result = engine.execute_plan(

        plan["id"]

    )

    assert result["status"] == "completed"

    assert len(result["steps"]) == 1

if __name__ == "__main__":

    test_planning_reasoning()