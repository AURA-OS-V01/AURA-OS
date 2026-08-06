from core.planning.mission_planner import MissionPlanner

class MockSelector:

    def select(self, capability):

        return {

            "agent": capability + " Agent"

        }

def test_planner():

    planner = MissionPlanner(

        MockSelector()

    )

    result = planner.create_plan(

        "AI Business Analysis",

        [

            "Research",

            "Finance",

            "Security"

        ]

    )

    print("Mission Planner Test")

    print("-------------------")

    print(result)

if __name__ == "__main__":

    test_planner()