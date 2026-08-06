from core.integration.aura_integration_test_environment_v01 import (

    AURAIntegrationTestEnvironment

)

def test_aura_integration():

    system = AURAIntegrationTestEnvironment()

    result = system.run_test(

        "Test User",

        "Create a project plan",

        [

            "Identity",

            "API Gateway",

            "Agent Team",

            "Memory",

            "Feedback",

            "Audit"

        ]

    )

    print("AURA Integration Test")

    print("--------------------")

    print(result)

if __name__ == "__main__":

    test_aura_integration()