from intelligence.planning.engine import PlanningEngine

def test_planning():

    planner = PlanningEngine()

    plan = planner.create_plan(

        "Build an AI marketing business"

    )

    planner.add_milestone(

        plan["id"],

        "Research market"

    )

    planner.add_task(

        plan["id"],

        "Analyze competitors"

    )

    print("Planning Engine Test")

    print("-------------------")

    print(

        planner.get_plans()

    )

if __name__ == "__main__":

    test_planning()