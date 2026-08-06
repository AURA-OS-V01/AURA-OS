from core.agents.goals.aura_agent_goal_management_engine_v01 import (

    AURAAgentGoalManagementEngine

)

def test_goal_management_engine():

    engine = AURAAgentGoalManagementEngine()

    goal = engine.create_goal(

        "Launch AURA Alpha System",

        "AI Development",

        "high"

    )

    assert goal["objective"] == (

        "Launch AURA Alpha System"

    )

    assert goal["category"] == (

        "AI Development"

    )

    assert goal["priority"] == (

        "high"

    )

    task = engine.add_task(

        goal["id"],

        "Research AI market",

        "Research Agent"

    )

    assert task["task"] == (

        "Research AI market"

    )

    assert task["capability"] == (

        "Research Agent"

    )

    state = engine.get_goal_state()

    print(

        "AURA Goal Management Engine Test"

    )

    print(state)

    assert len(

        state["goals"]

    ) == 1

    assert len(

        state["goals"][0]["tasks"]

    ) == 1

if __name__ == "__main__":

    test_goal_management_engine()