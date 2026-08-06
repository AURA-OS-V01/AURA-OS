from agents.builders.software_architect_agent import (

    SoftwareArchitectAgent

)

def test_architect():

    agent = SoftwareArchitectAgent()

    result = agent.design(

        "AURA Dashboard",

        [

            "User interface",

            "Agent monitoring",

            "Mission control"

        ]

    )

    print("Software Architect Agent Test")

    print("-----------------------------")

    print(result)

if __name__ == "__main__":

    test_architect()