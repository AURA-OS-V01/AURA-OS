from agents.builders.frontend.frontend_builder_agent import (

    FrontendBuilderAgent

)

def test_frontend_builder():

    agent = FrontendBuilderAgent()

    result = agent.build_plan(

        "AURA Dashboard",

        [

            "Agent monitoring",

            "Mission control"

        ]

    )

    print("Frontend Builder Agent Test")

    print("--------------------------")

    print(result)

if __name__ == "__main__":

    test_frontend_builder()