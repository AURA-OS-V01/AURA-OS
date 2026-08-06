from core.deployment.api_gateway_system_v01 import (

    APIGatewaySystem

)

def test_api_gateway():

    system = APIGatewaySystem()

    result = system.register_service(

        "Agent Service",

        "/agents",

        "active"

    )

    print("API Gateway System Test")

    print("-----------------------")

    print(result)

if __name__ == "__main__":

    test_api_gateway()