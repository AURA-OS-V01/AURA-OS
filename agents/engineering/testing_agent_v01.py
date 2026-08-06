from uuid import uuid4

from datetime import datetime

class TestingAgent:

    """

    Creates software testing plans.

    """

    def __init__(self):

        self.tests = []

    def create_plan(

        self,

        product

    ):

        test_plan = {

            "id": str(uuid4()),

            "product": product,

            "areas": [

                "Functionality",

                "Security",

                "Performance",

                "User Experience"

            ],

            "status": "testing_required",

            "created":

                datetime.utcnow().isoformat()

        }

        self.tests.append(

            test_plan

        )

        return test_plan