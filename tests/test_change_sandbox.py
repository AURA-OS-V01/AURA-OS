from core.evolution.sandbox.change_sandbox import (

    ChangeSandbox

)

def test_sandbox():

    sandbox = ChangeSandbox()

    environment = sandbox.create_environment(

        {

            "change":

            "Improve Finance Agent"

        }

    )

    result = sandbox.test_change(

        environment["id"],

        True

    )

    print("Change Sandbox Test")

    print("------------------")

    print(result)

if __name__ == "__main__":

    test_sandbox()