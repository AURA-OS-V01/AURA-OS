from core.agents.specialist_agent_framework_v01 import (

    SpecialistAgentFramework

)

def test_specialist_agents():

    framework = SpecialistAgentFramework()

    result = framework.create_agent(

        "Research Agent",

        "Information Analysis"

    )

    print("Specialist Agent Framework Test")

    print("--------------------------------")

    print(result)

if __name__ == "__main__":

    test_specialist_agents()