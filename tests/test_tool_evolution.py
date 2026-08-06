from core.evolution.tools.tool_evolution import ToolEvolutionEngine

def test_tool_evolution():

    engine = ToolEvolutionEngine()

    result = engine.analyze(

        "Market Analyzer",

        0.45,

        500

    )

    print("Tool Evolution Test")

    print("-------------------")

    print(result)

if __name__ == "__main__":

    test_tool_evolution()