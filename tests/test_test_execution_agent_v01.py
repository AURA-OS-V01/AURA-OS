from agents.engineering.test_execution_agent_v01 import (

    TestExecutionAgent

)

def test_execution_agent():

    agent = TestExecutionAgent()

    result = agent.execute(

        "User account changes"

    )

    print("Test Execution Agent Test")

    print("-------------------------")

    print(result)

if __name__ == "__main__":

    test_execution_agent()