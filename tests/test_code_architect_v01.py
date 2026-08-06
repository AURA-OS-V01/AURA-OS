from agents.engineering.code_architect_v01 import (

    CodeArchitect

)

def test_code_architect():

    architect = CodeArchitect()

    result = architect.analyze(

        "Add AURA user dashboard"

    )

    print("Code Architect Test")

    print("------------------")

    print(result)

if __name__ == "__main__":

    test_code_architect()