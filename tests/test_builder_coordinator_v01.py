from agents.product.builder_coordinator_v01 import (

    BuilderCoordinator

)

def test_builder_coordinator():

    coordinator = BuilderCoordinator()

    result = coordinator.create_tasks(

        "Fitness App Architecture"

    )

    print("Builder Coordinator Test")

    print("------------------------")

    print(result)

if __name__ == "__main__":

    test_builder_coordinator()