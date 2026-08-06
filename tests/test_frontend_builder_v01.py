from agents.engineering.frontend_builder_v01 import (

    FrontendBuilder

)

def test_frontend_builder():

    builder = FrontendBuilder()

    result = builder.create_task(

        "Create AURA user dashboard"

    )

    print("Frontend Builder Test")

    print("--------------------")

    print(result)

if __name__ == "__main__":

    test_frontend_builder()