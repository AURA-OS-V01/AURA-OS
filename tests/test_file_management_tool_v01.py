from tools.file_management_tool_v01 import (

    FileManagementTool

)

def test_file_management():

    tool = FileManagementTool()

    result = tool.create_operation(

        "agents/new_agent.py",

        "create"

    )

    print("File Management Tool Test")

    print("-------------------------")

    print(result)

if __name__ == "__main__":

    test_file_management()