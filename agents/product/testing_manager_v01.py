from uuid import uuid4

from datetime import datetime

class TestingManager:

    """

    Creates and tracks product testing.

    """

    def __init__(self):

        self.reports = []

    def create_test_plan(

        self,

        product

    ):

        report = {

            "id": str(uuid4()),

            "product": product,

            "tests": [

                "Functionality",

                "Performance",

                "Security",

                "User Experience"

            ],

            "status": "testing",

            "created":

                datetime.utcnow().isoformat()

        }

        self.reports.append(

            report

        )

        return report

    def complete_testing(

        self,

        report_id,

        passed

    ):

        for report in self.reports:

            if report["id"] == report_id:

                report["status"] = (

                    "approved"

                    if passed

                    else

                    "needs_fixes"

                )

                return report

        return None