from core.demo.aura_end_to_end_alpha_demo_v01 import (

    AURAEndToEndAlphaDemo

)

def test_aura_demo():

    aura = AURAEndToEndAlphaDemo()

    result = aura.run_demo(

        "Test User",

        "Coding",

        "Create a web application"

    )

    print("AURA End-to-End Alpha Demo")

    print("--------------------------")

    print(result)

if __name__ == "__main__":

    test_aura_demo()