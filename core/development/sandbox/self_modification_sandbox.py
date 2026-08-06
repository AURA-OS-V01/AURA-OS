from uuid import uuid4

from datetime import datetime

class SelfModificationSandbox:

    """

    Tests AURA generated changes

    in an isolated environment.

    """

    def __init__(self):

        self.environments = []

    def create(

        self,

        change_package

    ):

        environment = {

            "id": str(uuid4()),

            "change_package": change_package,

            "status": "created",

            "created": datetime.utcnow().isoformat()

        }

        self.environments.append(

            environment

        )

        return environment

    def evaluate(

        self,

        environment_id,

        result

    ):

        for environment in self.environments:

            if environment["id"] == environment_id:

                environment["status"] = (

                    "approved"

                    if result

                    else

                    "rejected"

                )

                return environment

        return None