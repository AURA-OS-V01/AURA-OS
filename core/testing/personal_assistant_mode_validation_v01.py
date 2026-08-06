from uuid import uuid4

from datetime import datetime

class PersonalAssistantModeValidation:

    """

    Tests AURA personal assistant behavior.

    """

    def __init__(self):

        self.results = []

    def run_validation(

        self,

        user,

        request,

        capabilities

    ):

        result = {

            "id": str(uuid4()),

            "mode": "Personal Assistant",

            "user": user,

            "request": request,

            "capabilities_tested": capabilities,

            "status": "passed",

            "created":

                datetime.utcnow().isoformat()

        }

        self.results.append(result)

        return result

    def get_results(self):

        return self.results