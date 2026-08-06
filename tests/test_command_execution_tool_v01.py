from tools.command_execution_tool_v01 import (

    CommandExecutionTool

)

def test_command_execution():

    tool = CommandExecutionTool()

    result = tool.execute(

        "run tests"

    )

    print("Command Execution Tool Test")

    print("--------------------------")

    print(result)

if __name__ == "__main__":

    test_command_execution()