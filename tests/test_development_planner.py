from core.development.development_planner import (

    DevelopmentPlanner

)

def test_planner():

    planner = DevelopmentPlanner()

    result = planner.create_plan(

        "Improve memory retrieval",

        [

            "core/memory.py",

            "tests/test_memory.py"

        ],

        "Slow retrieval performance",

        "medium"

    )

    print("Development Planner Test")

    print("-----------------------")

    print(result)

if __name__ == "__main__":

    test_planner()