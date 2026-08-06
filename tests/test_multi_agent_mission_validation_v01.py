from core.testing.multi_agent_mission_validation_v01 import (

    MultiAgentMissionValidation

)

def test_multi_agent_mission():

    system = MultiAgentMissionValidation()

    result = system.run_mission(

        "Test User",

        "Create a startup launch plan",

        [

            "Strategy Agent",

            "Research Agent",

            "Coding Agent",

            "Analysis Agent",

            "Writing Agent"

        ]

    )

    print("Multi-Agent Mission Validation")

    print("--------------------------------")

    print(result)

if __name__ == "__main__":

    test_multi_agent_mission()