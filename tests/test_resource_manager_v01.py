from core.operations.resource_manager_v01 import (

    ResourceManager

)

def test_resource_manager():

    manager = ResourceManager()

    result = manager.allocate(

        "Build education platform"

    )

    print("Resource Manager Test")

    print("--------------------")

    print(result)

if __name__ == "__main__":

    test_resource_manager()