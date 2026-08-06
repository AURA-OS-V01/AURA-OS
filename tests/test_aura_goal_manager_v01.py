from core.goals.aura_goal_manager_v01 import (

    AURAGoalManager

)

def test_goal_manager():

    manager = AURAGoalManager()

    goal = manager.create_goal(

        "Build Automation System",

        "Create autonomous workflow",

        "high"

    )

    created = goal.copy()

    active = manager.activate_goal(

        goal["id"]

    )

    completed = manager.complete_goal(

        goal["id"]

    )

    state = manager.get_state()

    assert created["status"] == "created"

    assert active["status"] == "active"

    assert completed["status"] == "completed"

    assert state["total_goals"] == 1

if __name__ == "__main__":

    test_goal_manager()