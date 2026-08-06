from core.self_builder.self_builder_planner_v01 import (

    SelfBuilderPlanner

)

def test_self_builder_planner():

    planner = SelfBuilderPlanner()

    result = planner.create_plan(

        "Build AURA client dashboard"

    )

    print("Self Builder Planner Test")

    print("------------------------")

    print(result)

if __name__ == "__main__":

    test_self_builder_planner()