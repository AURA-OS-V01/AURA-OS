from core.intelligence.aura_strategic_planning_engine_v01 import (

    AURAStrategicPlanningEngine

)

def test_strategic_planning_engine():

    engine = AURAStrategicPlanningEngine()

    plan = engine.create_plan(

        "Increase Business Automation",

        "Create automation roadmap for clients."

    )

    engine.add_action(

        plan["id"],

        "Deploy AI Sales Agent",

        90

    )

    engine.add_action(

        plan["id"],

        "Create Marketing Workflow",

        70

    )

    action = engine.generate_next_action(

        plan["id"]

    )

    print(

        "AURA Strategic Planning Engine Test"

    )

    print(

        "-----------------------------------"

    )

    print(action)

    assert action["action"] == (

        "Deploy AI Sales Agent"

    )

    assert action["priority"] == 90

if __name__ == "__main__":

    test_strategic_planning_engine()