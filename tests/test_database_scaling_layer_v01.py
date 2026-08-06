from core.deployment.database_scaling_layer_v01 import (

    DatabaseScalingLayer

)

def test_database_scaling():

    system = DatabaseScalingLayer()

    result = system.register_database(

        "AURA Memory Database",

        "Distributed",

        True,

        "Healthy"

    )

    print("Database Scaling Layer Test")

    print("---------------------------")

    print(result)

if __name__ == "__main__":

    test_database_scaling()