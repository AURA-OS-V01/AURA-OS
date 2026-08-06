from agents.product.testing_manager_v01 import (

    TestingManager

)

def test_testing_manager():

    manager = TestingManager()

    report = manager.create_test_plan(

        "Fitness App"

    )

    result = manager.complete_testing(

        report["id"],

        True

    )

    print("Testing Manager Test")

    print("-------------------")

    print(result)

if __name__ == "__main__":

    test_testing_manager()