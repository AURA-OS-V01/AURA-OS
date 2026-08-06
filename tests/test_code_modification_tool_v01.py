from tools.code_modification_tool_v01 import (

    CodeModificationTool

)

def test_code_modification():

    tool = CodeModificationTool()

    result = tool.create_request(

        "agents/engineering/backend_builder_v01.py",

        "modify"

    )

    print("Code Modification Tool Test")

    print("---------------------------")

    print(result)

if __name__ == "__main__":

    test_code_modification()