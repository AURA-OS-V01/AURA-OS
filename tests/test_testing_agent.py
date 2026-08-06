from core.evolution.testing.testing_agent import (

    AutomatedTestingAgent

)

def test_testing_agent():

    agent = AutomatedTestingAgent()

    result = agent.test(

        {

            "change":

            "Improve Memory System"

        },

        [

            True,

            True,

            True

        ]

    )

    print("Automated Testing Agent Test")

    print("---------------------------")

    print(result)

if __name__ == "__main__":

    test_testing_agent()