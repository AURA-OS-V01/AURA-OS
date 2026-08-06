from uuid import uuid4

class TestingEngineerAgent:

    """

    Designs testing strategies

    for applications.

    """

    def __init__(self):

        self.test_plans = []

    def create_plan(

        self,

        project,

        components

    ):

        plan = {

            "id": str(uuid4()),

            "project": project,

            "components": components,

            "tests": [

                "Unit Tests",

                "Integration Tests",

                "UI Tests",

                "Security Tests",

                "Performance Tests"

            ],

            "status": "planned"

        }

        self.test_plans.append(

            plan

        )

        return plan