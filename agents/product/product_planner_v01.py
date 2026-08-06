from uuid import uuid4

from datetime import datetime

class ProductPlanner:

    """

    Converts ideas into structured product plans.

    """

    def __init__(self):

        self.plans = []

    def create_plan(

        self,

        idea

    ):

        plan = {

            "id": str(uuid4()),

            "idea": idea,

            "status": "planned",

            "features": [

                "Requirements analysis",

                "Architecture design",

                "Development plan",

                "Testing strategy"

            ],

            "created":

                datetime.utcnow().isoformat()

        }

        self.plans.append(plan)

        return plan

    def list_plans(self):

        return self.plans