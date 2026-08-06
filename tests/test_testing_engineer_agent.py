from agents.builders.testing.testing_engineer_agent import (

    TestingEngineerAgent

)

def test_testing_engineer():

    agent = TestingEngineerAgent()

    result = agent.create_plan(

        "AURA Dashboard",

        [

            "Frontend",

            "Backend",

            "Database"

        ]

    )

    print("Testing Engineer Agent Test")

    print("---------------------------")

    print(result)

if __name__ == "__main__":

    test_testing_engineer()