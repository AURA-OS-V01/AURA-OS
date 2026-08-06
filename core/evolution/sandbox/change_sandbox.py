from uuid import uuid4

from datetime import datetime

class ChangeSandbox:

    """

    Isolated environment for testing

    AURA improvement proposals.

    """

    def __init__(self):

        self.changes = []

    def create_environment(

        self,

        proposal

    ):

        environment = {

            "id": str(uuid4()),

            "proposal": proposal,

            "status": "created",

            "created": datetime.utcnow().isoformat()

        }

        self.changes.append(

            environment

        )

        return environment

    def test_change(

        self,

        environment_id,

        success

    ):

        for environment in self.changes:

            if environment["id"] == environment_id:

                environment["status"] = (

                    "passed"

                    if success

                    else

                    "failed"

                )

                return environment

        return None