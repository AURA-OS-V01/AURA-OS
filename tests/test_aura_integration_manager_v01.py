from core.integrations.aura_integration_manager_v01 import (

    AURAIntegrationManager

)

def test_integration_manager():

    system = AURAIntegrationManager()

    result = system.register_integration(

        "Email Service",

        "communication"

    )

    print("AURA Integration Manager Test")

    print("-----------------------------")

    print(result)

if __name__ == "__main__":

    test_integration_manager()