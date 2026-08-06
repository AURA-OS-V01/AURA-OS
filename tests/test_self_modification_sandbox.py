from core.development.sandbox.self_modification_sandbox import (

    SelfModificationSandbox

)

def test_self_modification():

    sandbox = SelfModificationSandbox()

    environment = sandbox.create(

        {

            "change":

            "Improve memory system"

        }

    )

    result = sandbox.evaluate(

        environment["id"],

        True

    )

    print("Self Modification Sandbox Test")

    print("-----------------------------")

    print(result)

if __name__ == "__main__":

    test_self_modification()