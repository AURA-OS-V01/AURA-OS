from core.runtime.aura_core_runtime_v01 import (

    AURACoreRuntime

)

def test_core_runtime():

    aura = AURACoreRuntime()

    session = aura.start_session(

        "Test User"

    )

    result = aura.process_request(

        session["id"],

        "Create a business plan"

    )

    print("AURA Core Runtime Test")

    print("----------------------")

    print(result)

    print(

        aura.get_status()

    )

if __name__ == "__main__":

    test_core_runtime()