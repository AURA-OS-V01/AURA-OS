from core.deployment.load_balancing_system_v01 import (

    LoadBalancingSystem

)

def test_load_balancing():

    system = LoadBalancingSystem()

    result = system.register_server(

        "AURA Server 01",

        1000,

        "active"

    )

    print("Load Balancing System Test")

    print("--------------------------")

    print(result)

if __name__ == "__main__":

    test_load_balancing()