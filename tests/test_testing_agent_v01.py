from agents.engineering.testing_agent_v01 import (

    TestingAgent

)

def test_testing_agent():

    agent = TestingAgent()

    result = agent.create_plan(

        "AURA User Dashboard"

    )

    print("Testing Agent Test")

    print("------------------")

    print(result)

if __name__ == "__main__":

    test_testing_agent()