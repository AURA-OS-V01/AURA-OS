from core.intelligence.planning.aura_goal_management_planning_engine_v01 import (

    AURAGoalManagementPlanningEngine

)

def test_goal_management_engine():

    planner = AURAGoalManagementPlanningEngine()

    goal = planner.create_goal(

        "Acquire 100 enterprise customers",

        "Grow AURA business adoption",

        "high"

    )

    milestone = planner.add_milestone(

        goal["id"],

        "Launch enterprise outreach campaign"

    )

    updated = planner.update_progress(

        goal["id"],

        50

    )

    state = planner.get_planning_state()

    print(

        "AURA Goal Management Planning Engine Test"

    )

    print(

        "----------------------------------------"

    )

    print(state)

    assert updated["progress"] == 50

    assert updated["status"] == (

        "active"

    )

    assert milestone["completed"] is False

if __name__ == "__main__":

    test_goal_management_engine()