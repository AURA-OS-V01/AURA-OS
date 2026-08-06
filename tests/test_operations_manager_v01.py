from core.operations.operations_manager_v01 import (

    OperationsManager

)

def test_operations_manager():

    manager = OperationsManager()

    result = manager.initialize(

        "Build AURA education platform"

    )

    print("Operations Manager Test")

    print("-----------------------")

    print(result)

if __name__ == "__main__":

    test_operations_manager()