from core.execution.aura_executor import AURAExecutor

class MockPlanner:

    """

    Simulates AURA mission planning.

    """

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

                },

                {

                    "agent": "Finance Agent"

                },

                {

                    "agent": "Security Agent"

                }

            ]

        }

class MockConnector:

    """

    Simulates mission startup.

    """

    def execute_plan(

        self,

        plan

    ):

        return {

            "mission": plan["mission"],

            "agents": plan["team"],

            "status": "started"

        }

def test_full_mission():

    executor = AURAExecutor(

        MockPlanner(),

        MockConnector()

    )

    result = executor.execute(

        "Find a profitable AI business opportunity",

        [

            "market_analysis",

            "financial_analysis",

            "risk_analysis"

        ]

    )

    print("AURA Full Mission Test")

    print("---------------------")

    print(result)

if __name__ == "__main__":

    test_full_mission()