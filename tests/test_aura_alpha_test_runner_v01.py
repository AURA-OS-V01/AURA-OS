from core.testing.aura_alpha_test_runner_v01 import (

    AURAAlphaTestRunner

)

def test_alpha_runner():

    system = AURAAlphaTestRunner()

    result = system.run_test(

        "Coding Mode Test",

        "Build a login API",

        [

            "Agent Team",

            "Memory",

            "API Gateway"

        ]

    )

    print("AURA Alpha Test Runner")

    print("----------------------")

    print(result)

if __name__ == "__main__":

    test_alpha_runner()