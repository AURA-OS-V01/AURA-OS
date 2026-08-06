from core.self_builder.rollback_system_v01 import (

    RollbackSystem

)

def test_rollback_system():

    system = RollbackSystem()

    result = system.rollback(

        "Dashboard update",

        "Failed tests"

    )

    print("Rollback System Test")

    print("-------------------")

    print(result)

if __name__ == "__main__":

    test_rollback_system()