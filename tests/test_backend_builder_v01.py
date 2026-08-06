from agents.engineering.backend_builder_v01 import (

    BackendBuilder

)

def test_backend_builder():

    builder = BackendBuilder()

    result = builder.create_task(

        "Create user account API"

    )

    print("Backend Builder Test")

    print("-------------------")

    print(result)

if __name__ == "__main__":

    test_backend_builder()