from agents.tools.tool_interface import ToolInterface

class TestTool(ToolInterface):

    def execute(

        self,

        input_data

    ):

        return {

            "processed": input_data

        }

def test_tool():

    tool = TestTool(

        "Example Tool"

    )

    result = tool.execute(

        "hello AURA"

    )

    print("Tool Interface Test")

    print("-------------------")

    print(result)

if __name__ == "__main__":

    test_tool()