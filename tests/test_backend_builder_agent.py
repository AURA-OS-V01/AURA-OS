from agents.builders.backend.backend_builder_agent import (

    BackendBuilderAgent

)

def test_backend_builder():

    agent = BackendBuilderAgent()

    result = agent.build_plan(

        "AURA Dashboard",

        [

            "User accounts",

            "Agent monitoring",

            "Mission history"

        ]

    )

    print("Backend Builder Agent Test")

    print("-------------------------")

    print(result)

if __name__ == "__main__":

    test_backend_builder()