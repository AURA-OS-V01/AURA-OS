from uuid import uuid4

from datetime import datetime

class SelfImprovementReports:

    """

    Creates reports about AURA development activity.

    """

    def __init__(self):

        self.reports = []

    def generate(

        self,

        completed,

        current,

        recommendations

    ):

        report = {

            "id": str(uuid4()),

            "completed": completed,

            "current": current,

            "recommendations": recommendations,

            "created":

                datetime.utcnow().isoformat()

        }

        self.reports.append(

            report

        )

        return report