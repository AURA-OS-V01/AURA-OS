from core.execution.aura_executor import AURAExecutor

class MockPlanner:

    def create_plan(

        self,

        objective,

        capabilities

    ):

        return {

            "mission": objective,

            "team": [

                {

                    "agent": "Research Agent"

                }

            ]

        }

class MockConnector:

    def execute_plan(

        self,

        plan

    ):

        return {

            "status": "started"

        }

def test_executor():

    executor = AURAExecutor(

        MockPlanner(),

        MockConnector()

    )

    result = executor.execute(

        "AI Business Analysis",

        [

            "market_analysis"

        ]

    )

    print("AURA Executor Test")

    print("------------------")

    print(result)

if __name__ == "__main__":

    test_executor()