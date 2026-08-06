from agents.engineering.code_generation_agent_v01 import (

    CodeGenerationAgent

)

def test_code_generation_agent():

    agent = CodeGenerationAgent()

    result = agent.generate(

        "Create user account model"

    )

    print("Code Generation Agent Test")

    print("-------------------------")

    print(result)

if __name__ == "__main__":

    test_code_generation_agent()