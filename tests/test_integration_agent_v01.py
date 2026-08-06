from agents.engineering.integration_agent_v01 import (

    IntegrationAgent

)

def test_integration_agent():

    agent = IntegrationAgent()

    result = agent.integrate(

        [

            "Frontend",

            "Backend",

            "Database"

        ]

    )

    print("Integration Agent Test")

    print("---------------------")

    print(result)

if __name__ == "__main__":

    test_integration_agent()