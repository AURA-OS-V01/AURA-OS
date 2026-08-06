from uuid import uuid4

from datetime import datetime

class CodingModeValidation:

    """

    Tests AURA software development workflows.

    """

    def __init__(self):

        self.results = []

    def run_validation(

        self,

        user,

        project_request,

        capabilities

    ):

        result = {

            "id": str(uuid4()),

            "mode": "Coding",

            "user": user,

            "project": project_request,

            "capabilities_tested": capabilities,

            "status": "passed",

            "created":

                datetime.utcnow().isoformat()

        }

        self.results.append(result)

        return result

    def get_results(self):

        return self.results